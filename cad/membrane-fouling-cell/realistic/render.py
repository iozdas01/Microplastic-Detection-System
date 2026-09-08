"""Render the exported CAD geometry in Blender (no image synthesis).

blender --background --factory-startup --python render.py -- --view assembled
Surface lettering and microscopic finish are presentation layers, not STEP cuts.
"""
import argparse
import json
from math import pi, sin, cos
from pathlib import Path
import sys

import bpy
from mathutils import Vector

ROOT = Path(__file__).resolve().parent
parser = argparse.ArgumentParser()
parser.add_argument("--view", choices=("assembled", "exploded", "cutaway", "detail"), default="assembled")
parser.add_argument("--samples", type=int, default=96)
parser.add_argument("--width", type=int, default=1500)
parser.add_argument("--height", type=int, default=1800)
parser.add_argument("--save-blend", action="store_true")
args = parser.parse_args(sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else [])
manifest = json.loads((ROOT / "parts.json").read_text())
parts = {p["name"]: p for p in manifest["components"]}


def rgba(value):
    h = value.lstrip("#")
    # Material input colors are linear, source swatches are sRGB.
    rgb = [int(h[i:i+2], 16) / 255 for i in (0, 2, 4)]
    return tuple(v / 12.92 if v < 0.04045 else ((v + 0.055) / 1.055)**2.4 for v in rgb) + (1,)


def material(name, spec):
    mat = bpy.data.materials.new(name)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    bsdf.inputs["Base Color"].default_value = rgba(spec["color"])
    bsdf.inputs["Metallic"].default_value = spec.get("metalness", 0)
    bsdf.inputs["Roughness"].default_value = spec.get("roughness", 0.3)
    if "transmission" in spec:
        bsdf.inputs["Transmission Weight"].default_value = spec["transmission"]
        bsdf.inputs["IOR"].default_value = spec.get("ior", 1.46)
    if name in ("quartz", "optical_glass", "polarising_glass"):
        bsdf.inputs["Transmission Weight"].default_value = 0.97
        bsdf.inputs["Coat Weight"].default_value = 0.25
        bsdf.inputs["Coat Roughness"].default_value = 0.05
    if "emissive" in spec:
        bsdf.inputs["Emission Color"].default_value = rgba(spec["emissive"])
        bsdf.inputs["Emission Strength"].default_value = spec.get("emissiveIntensity", 1.0)
    if name in ("aluminium", "black_anodised", "rubber_grip", "membrane"):
        noise = mat.node_tree.nodes.new("ShaderNodeTexNoise")
        noise.inputs["Scale"].default_value = 4800 if name == "aluminium" else 14000
        noise.inputs["Detail"].default_value = 2
        coords = mat.node_tree.nodes.new("ShaderNodeTexCoord")
        mat.node_tree.links.new(coords.outputs["Object"], noise.inputs["Vector"])
        bump = mat.node_tree.nodes.new("ShaderNodeBump")
        bump.inputs["Strength"].default_value = 0.11 if name == "membrane" else 0.045
        bump.inputs["Distance"].default_value = 0.000008 if name == "membrane" else 0.000003
        mat.node_tree.links.new(noise.outputs["Fac"], bump.inputs["Height"])
        mat.node_tree.links.new(bump.outputs["Normal"], bsdf.inputs["Normal"])
    return mat


def look_at(obj, point):
    obj.rotation_euler = (Vector(point) - obj.location).to_track_quat("-Z", "Y").to_euler()


def area(name, location, target, power, size, color=(1, 1, 1), size_y=None):
    light = bpy.data.lights.new(name, "AREA")
    light.energy = power * 0.06
    light.color = color
    light.shape = "RECTANGLE"
    light.size = size
    light.size_y = size_y if size_y else size
    obj = bpy.data.objects.new(name, light)
    bpy.context.collection.objects.link(obj)
    obj.location = location
    look_at(obj, target)
    return obj


bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete(use_global=False)
source = "fouling_cell_realistic.glb"
if args.view == "exploded":
    source = "fouling_cell_exploded.glb"
elif args.view == "cutaway":
    source = "fouling_cell_cutaway.glb"
bpy.ops.import_scene.gltf(filepath=str(ROOT / source))
mats = {name: material(name, spec) for name, spec in manifest["materials"].items()}
meshes = []
for obj in list(bpy.context.scene.objects):
    if obj.type != "MESH":
        continue
    name = obj.name
    if name not in parts:
        print("Unmapped CAD object:", name)
        continue
    meshes.append(obj)
    obj.data.materials.clear()
    obj.data.materials.append(mats[parts[name]["material"]])
    # Respect STEP-derived split normals: do not blur milled corners.
    obj["cad_component"] = name
    if args.view == "detail" and parts[name]["group"] in ("lens", "camera", "analyser"):
        obj.hide_render = True

bpy.context.view_layer.update()
points = [obj.matrix_world @ Vector(corner) for obj in meshes for corner in obj.bound_box if not obj.hide_render]
low = Vector(tuple(min(p[i] for p in points) for i in range(3)))
high = Vector(tuple(max(p[i] for p in points) for i in range(3)))
print("CAD world bounds, metres:", tuple(low), tuple(high), flush=True)

# Lettering is positioned on the actual part surfaces. Dimensions match the CAD.
ink = material("Laser-mark ink", {"color": "#394249", "roughness": 0.6, "metalness": 0.1})
white_ink = material("Lens lettering", {"color": "#e6e8df", "roughness": 0.7, "metalness": 0.0})


def part_delta(name):
    return Vector(parts[name]["explode"]) / 1000 if args.view == "exploded" else Vector((0, 0, 0))


def text(body, position_mm, size_mm, parent, rotation=(pi/2, 0, 0), color=None, align="CENTER"):
    curve = bpy.data.curves.new("Marking " + body, "FONT")
    curve.body = body
    curve.align_x = align
    curve.align_y = "CENTER"
    curve.size = size_mm / 1000
    curve.resolution_u = 4
    obj = bpy.data.objects.new("Marking " + body, curve)
    bpy.context.collection.objects.link(obj)
    obj.location = Vector(position_mm) / 1000 + part_delta(parent)
    obj.rotation_euler = rotation
    obj.data.materials.append(color or ink)
    return obj


def barrel_text(body, height, radius, size=1.7, spacing=1.15):
    for i, character in enumerate(body):
        angle = (i - (len(body)-1)/2) * spacing / radius
        text(character, (radius*sin(angle), -radius*cos(angle), height), size,
             "lens_scale_barrel", (pi/2, 0, angle), white_ink)


if args.view != "cutaway":
    text("CROSSFLOW  /  5 mm", (0, -44.76, 5.4), 2.1, "01_flow_chamber")
    text("FILTRATE", (0, -44.76, -12.5), 2.3, "02_filtrate_chamber")
    text("530 nm  /  ILLUMINATION", (0, -44.76, -43.3), 1.8, "11_led_heat_sink")
    text("MF-47", (0, -28, 19.02), 3.5, "03_window_retainer", (0, 0, 0))
    text("POLARISED IMAGING CELL", (0, -33, 19.02), 1.4, "03_window_retainer", (0, 0, 0))
    text("IN", (-39, -10, 19.02), 1.5, "03_window_retainer", (0, 0, 0))
    text("RETURN", (35, -10, 19.02), 1.4, "03_window_retainer", (0, 0, 0))
    if args.view != "detail":
        text("MONO", (0, -22.14, 166), 3.7, "camera_id_plate", color=white_ink)
        text("MACHINE VISION", (0, -22.14, 161.5), 1.25, "camera_id_plate", color=white_ink)
        barrel_text("MACRO 1:1", 116.0, 20.48, 1.9, 1.35)
        barrel_text("f = 50 mm", 112.8, 20.48, 1.7, 1.15)

scene = bpy.context.scene
scene.render.engine = "CYCLES"
scene.cycles.samples = args.samples
scene.cycles.use_denoising = True
scene.cycles.max_bounces = 12
scene.cycles.transmission_bounces = 8
scene.cycles.transparent_max_bounces = 12
scene.cycles.seed = 47
try:
    prefs = bpy.context.preferences.addons["cycles"].preferences
    prefs.compute_device_type = "METAL"
    prefs.get_devices()
    gpu = False
    for device in prefs.devices:
        device.use = device.type == "METAL"
        gpu |= device.use
    if gpu:
        scene.cycles.device = "GPU"
    print("Render device:", scene.cycles.device, [(d.name, d.type) for d in prefs.devices], flush=True)
except Exception as exc:
    print("Using CPU:", str(exc), flush=True)

scene.render.resolution_x = args.width
scene.render.resolution_y = args.height
scene.render.resolution_percentage = 100
scene.render.image_settings.file_format = "PNG"
scene.render.image_settings.color_mode = "RGBA"
scene.render.film_transparent = False
scene.view_settings.view_transform = "AgX"
scene.view_settings.look = "AgX - Medium High Contrast"
scene.view_settings.exposure = 0
scene.world.use_nodes = True
scene.world.node_tree.nodes["Background"].inputs[0].default_value = (0.72, 0.78, 0.84, 1)
scene.world.node_tree.nodes["Background"].inputs[1].default_value = 0.35

# Neutral photography sweep and large reflected softboxes.
floor_z = low.z - 0.001
bpy.ops.mesh.primitive_plane_add(size=200, location=(0, 0, floor_z))
floor = bpy.context.object
floor.name = "Studio sweep"
floor.data.materials.append(material("Studio surface", {"color": "#dfe4e7", "roughness": 0.82}))
target = (low + high) * 0.5
area("Main softbox", (-0.35, -0.45, high.z + 0.25), target, 105, 0.48, (1.0, 0.96, 0.9), 0.6)
area("Tall silver reflection", (0.4, -0.05, high.z + 0.08), target, 78, 0.16, (0.85, 0.92, 1.0), 0.5)
area("Rear rim", (-0.2, 0.3, high.z + 0.12), target, 110, 0.35, (1, 1, 1), 0.45)
area("Front fill", (0.03, -0.5, 0.03), target, 18, 0.3, (1, 1, 1), 0.4)

# Actual illumination is confined to the LED cavity.
emission_z = parts["14_led_array_board"]["bbox"]["max"][2] / 1000
emission_z += part_delta("14_led_array_board").z + 0.001
light = bpy.data.lights.new("530 nm array light", "AREA")
light.energy = 0.008
light.color = (0.25, 1.0, 0.07)
light.shape = "DISK"
light.size = 0.034
led_light = bpy.data.objects.new("530 nm array light", light)
bpy.context.collection.objects.link(led_light)
led_light.location = (0, 0, emission_z)
led_light.rotation_euler = (pi, 0, 0)

camera_data = bpy.data.cameras.new("Review camera")
camera = bpy.data.objects.new("Review camera", camera_data)
bpy.context.collection.objects.link(camera)
camera_data.type = "ORTHO"
camera_data.lens = 70
height = high.z - low.z
if args.view == "detail":
    target = Vector((0, 0, -0.015))
    camera.location = (0.25, -0.43, 0.23)
    camera_data.ortho_scale = 0.18
elif args.view == "cutaway":
    target = Vector((0, 0.002, 0.057))
    camera.location = (0.19, -0.60, 0.27)
    camera_data.ortho_scale = 0.292
elif args.view == "exploded":
    target = Vector((0, 0, 0.072))
    camera.location = (0.33, -0.70, 0.36)
    camera_data.ortho_scale = 0.505
else:
    target = Vector((0, 0, 0.061))
    camera.location = (0.34, -0.58, 0.31)
    camera_data.ortho_scale = 0.300
look_at(camera, target)
scene.camera = camera
output = ROOT / "renders"
output.mkdir(exist_ok=True)
scene.render.filepath = str(output / f"{args.view}.png")
if args.save_blend:
    # Open the saved project looking through the configured photography camera.
    for screen in bpy.data.screens:
        for area in screen.areas:
            if area.type == "VIEW_3D":
                area.spaces.active.region_3d.view_perspective = "CAMERA"
                area.spaces.active.shading.type = "MATERIAL"
    bpy.ops.wm.save_as_mainfile(filepath=str(ROOT / "instrument_studio.blend"))
print("Rendering:", scene.render.filepath, flush=True)
bpy.ops.render.render(write_still=True)
