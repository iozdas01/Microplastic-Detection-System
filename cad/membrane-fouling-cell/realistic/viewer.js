import * as THREE from 'three';
import {OrbitControls} from 'three/examples/jsm/controls/OrbitControls.js';
import {GLTFLoader} from 'three/examples/jsm/loaders/GLTFLoader.js';
import {RoomEnvironment} from 'three/examples/jsm/environments/RoomEnvironment.js';
import {prepareModel} from './model_scene.js';

const data = JSON.parse(document.getElementById('cad-data').textContent);
const manifest = data.manifest;
const records = new Map(manifest.components.map(p => [p.name,p]));
const el = id => document.getElementById(id);
const stage = el('stage');
const scene = new THREE.Scene();
scene.background = new THREE.Color('#edf1f3');
const renderer = new THREE.WebGLRenderer({antialias:true, alpha:false});
renderer.setPixelRatio(Math.min(window.devicePixelRatio,2));
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFSoftShadowMap;
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 1.35;
stage.appendChild(renderer.domElement);
renderer.domElement.setAttribute('aria-label','Rotate, zoom and select parts in the 3D instrument');
const camera = new THREE.PerspectiveCamera(32,1,.001,20);
const controls = new OrbitControls(camera,renderer.domElement);
controls.enableDamping = true;
controls.dampingFactor = .09;
controls.minDistance = .055;
controls.maxDistance = 2;
controls.maxPolarAngle = Math.PI*.96;
const pmrem = new THREE.PMREMGenerator(renderer);
const room = new RoomEnvironment();
scene.environment = pmrem.fromScene(room,.04).texture;
room.dispose();
scene.environmentIntensity = 1.1;
scene.add(new THREE.HemisphereLight(0xf3f8ff,0x9ca7ad,1.4));
function light(x,y,z,power){const l=new THREE.DirectionalLight(0xffffff,power);l.position.set(x,y,z);scene.add(l);return l;}
const key = light(-.3,.6,.5,3);
key.castShadow = true;
key.shadow.mapSize.set(2048,2048);
Object.assign(key.shadow.camera,{left:-.32,right:.32,top:.5,bottom:-.4,near:.01,far:2});
key.shadow.bias = -.00005;
key.shadow.normalBias = .0002;
key.shadow.radius = 4;
light(.3,.15,-.3,1.8);
const floor = new THREE.Mesh(new THREE.PlaneGeometry(5,5),new THREE.ShadowMaterial({color:0x667a88,opacity:.18}));
floor.rotation.x = -Math.PI/2;floor.receiveShadow = true;scene.add(floor);
const models = new Map();
let active,mode='assembled',spread=0,targetSpread=0,selected=null;
const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
const loader = new GLTFLoader();
const meshes = new Map();
const descriptions = {
  assembled:['The complete instrument.','Rotate to inspect the machined bodies, optical train and fluid connections. Select a part for its details.'],
  exploded:['Every layer, exposed.','Separate the assembly to see the windows, seals, membrane support and dry illumination optics.'],
  cutaway:['Inside the flow cell.','A physical half-section through the CAD solids reveals the membrane, fluid passages and optical stack.'],
};

function buffer(base64){const s=atob(base64),a=new Uint8Array(s.length);for(let i=0;i<s.length;i++)a[i]=s.charCodeAt(i);return a.buffer;}
function partRecord(object){for(let p=object;p;p=p.parent){const record=records.get(p.userData.cad_component||p.name);if(record)return record;}return null;}
function finishModel(root){
  const prepared=prepareModel(root,records,p=>{
    const spec=manifest.materials[p.material];
    const opts={color:spec.color,metalness:spec.metalness||0,roughness:spec.roughness??.3,side:THREE.DoubleSide};
    if(spec.transmission){Object.assign(opts,{transmission:spec.transmission,ior:spec.ior||1.46,thickness:.002,transparent:true,opacity:p.material==='quartz'?.52:.72,depthWrite:false});}
    if(spec.emissive)Object.assign(opts,{emissive:spec.emissive,emissiveIntensity:spec.emissiveIntensity});
    return new THREE.MeshPhysicalMaterial(opts);
  });
  meshes.set(root,prepared.meshes);
  scene.add(root);return root;
}

async function model(kind){
  if(models.has(kind))return models.get(kind);
  const gltf=await loader.parseAsync(buffer(data[kind]),'');
  const root=finishModel(gltf.scene);models.set(kind,root);root.visible=false;return root;
}
function name(p){return p.name.replace(/^\d+_/,'').replaceAll('_',' ').replace(/\b\w/g,c=>c.toUpperCase());}
function select(mesh){
  if(selected)selected.material.emissive.copy(selected.userData.baseEmission);
  selected=mesh;
  if(!mesh)return;
  const p=mesh.userData.record;
  mesh.userData.baseEmission=mesh.material.emissive.clone();
  mesh.material.emissive.set('#24566b').multiplyScalar(.2);
  el('part-kicker').textContent=p.material.replaceAll('_',' ');
  el('part-name').textContent=name(p);
  el('part-description').textContent=p.description||`${p.volume_mm3.toFixed(1)} mm³ · individually named CAD solid`;
}
function visibility(){
  if(!active)return;
  for(const obj of meshes.get(active)){
    const p=obj.userData.record;
    obj.visible=(!['camera','lens','analyser'].includes(p.group)||el('show-optics').checked)
      &&(p.group!=='tubing'||el('show-tubes').checked)
      &&(p.group!=='fasteners'||el('show-fasteners').checked);
    if(el('show-edges').checked&&!obj.userData.edges){
      const edges=new THREE.LineSegments(new THREE.EdgesGeometry(obj.geometry,28),new THREE.LineBasicMaterial({color:0x344550,transparent:true,opacity:.18}));
      obj.add(edges);obj.userData.edges=edges;
    }
    if(obj.userData.edges)obj.userData.edges.visible=el('show-edges').checked;
  }
}
function fit(){
  const isExploded=mode==='exploded';
  const scale=isExploded?1.68:1;
  const narrow=stage.clientWidth<700;
  const distance=scale*(narrow?1.2:1);
  if(mode==='cutaway')camera.position.set(.20*distance,.22*distance,.58*distance);
  else camera.position.set(.29*distance,.26*distance,.50*distance);
  controls.target.set(0,isExploded?.072:.061,0);controls.update();
}
let viewRequest=0;
async function setView(next){
  const request=++viewRequest;
  try{
    const root=await model(next==='cutaway'?'section':'assembled');
    if(request!==viewRequest)return;
    select(null);models.forEach(m=>m.visible=false);active=root;root.visible=true;mode=next;
    targetSpread=next==='exploded'?1:0;if(reduceMotion)spread=targetSpread;
    el('spread').disabled=next==='cutaway';el('spread').value=targetSpread*100;
    el('spread-value').textContent=`${targetSpread*100}%`;
    el('view-title').textContent=descriptions[next][0];el('view-description').textContent=descriptions[next][1];
    el('mode-indicator').textContent=`${next} · millimetres`;
    el('step-link').href=next==='assembled'?'fouling_cell_realistic.step':`fouling_cell_${next}.step`;
    document.querySelectorAll('[data-view]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.view===next)));
    el('part-name').textContent=`${meshes.get(root).length} visible CAD components`;
    el('part-kicker').textContent='Select any component';
    el('part-description').textContent='Generated from the same geometry as the STEP assembly.';
    visibility();fit();el('loading').hidden=true;
  }catch(error){el('loading').hidden=false;el('load-status').textContent=`Could not load the model: ${error.message}`;console.error(error);}
}
document.querySelectorAll('[data-view]').forEach(b=>b.addEventListener('click',()=>setView(b.dataset.view)));
for(const id of ['show-optics','show-tubes','show-fasteners','show-edges'])el(id).addEventListener('change',visibility);
el('fit').addEventListener('click',fit);
el('spread').addEventListener('input',event=>{
  targetSpread=Number(event.target.value)/100;
  el('spread-value').textContent=`${event.target.value}%`;
  const next=targetSpread>0?'exploded':'assembled';
  if(mode!==next){mode=next;document.querySelectorAll('[data-view]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.view===mode)));el('view-title').textContent=descriptions[next][0];el('view-description').textContent=descriptions[next][1];el('mode-indicator').textContent=`${next} · millimetres`;el('step-link').href=next==='assembled'?'fouling_cell_realistic.step':'fouling_cell_exploded.step';fit();}
});
const raycaster=new THREE.Raycaster(),pointer=new THREE.Vector2();let down;
renderer.domElement.addEventListener('pointerdown',e=>{down=[e.clientX,e.clientY];});
renderer.domElement.addEventListener('pointerup',e=>{
  if(!down||Math.hypot(e.clientX-down[0],e.clientY-down[1])>5||!active)return;
  const box=renderer.domElement.getBoundingClientRect();pointer.set((e.clientX-box.left)/box.width*2-1,-(e.clientY-box.top)/box.height*2+1);
  raycaster.setFromCamera(pointer,camera);
  const hit=raycaster.intersectObjects(meshes.get(active).filter(o=>o.visible),false)[0];
  if(hit)select(hit.object);
});
function resize(){const w=stage.clientWidth,h=stage.clientHeight;renderer.setSize(w,h);camera.aspect=w/h;camera.updateProjectionMatrix();}
new ResizeObserver(resize).observe(stage);resize();
el('part-count').textContent=manifest.components.length;
el('part-name').textContent=`${manifest.components.length} editable solids`;
renderer.setAnimationLoop(()=>{
  spread=reduceMotion?targetSpread:THREE.MathUtils.lerp(spread,targetSpread,.075);
  if(active)for(const obj of active.userData.components)obj.position.copy(obj.userData.home).addScaledVector(obj.userData.delta,mode==='cutaway'?0:spread);
  floor.position.y=-.0526-(mode==='cutaway'?0:.09*spread);
  controls.update();renderer.render(scene,camera);
});
setView('assembled');
