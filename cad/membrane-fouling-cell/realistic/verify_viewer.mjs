import fs from 'node:fs/promises';
import assert from 'node:assert/strict';
import * as THREE from 'three';
import {GLTFLoader} from 'three/examples/jsm/loaders/GLTFLoader.js';
import {prepareModel} from './model_scene.js';

export async function verify(root){
  const manifest=JSON.parse(await fs.readFile(root+'/parts.json','utf8'));
  const records=new Map(manifest.components.map(p=>[p.name,p]));
  async function load(name){const b=await fs.readFile(root+'/'+name+'.glb');return (await new GLTFLoader().parseAsync(b.buffer.slice(b.byteOffset,b.byteOffset+b.byteLength),'')).scene;}
  const assembled=await load('fouling_cell_realistic');
  const originalBox=new THREE.Box3().setFromObject(assembled);
  const material=()=>new THREE.MeshStandardMaterial();
  const ready=prepareModel(assembled,records,material);
  assert.equal(ready.components.length,166);
  assert.equal(ready.meshes.length,166);
  function sameBounds(a,b){for(const k of ['min','max'])assert.ok(a[k].distanceTo(b[k])<.00001,`${k} differs by ${a[k].distanceTo(b[k])} metres`);}
  sameBounds(originalBox,new THREE.Box3().setFromObject(assembled));
  for(const c of ready.components)c.position.copy(c.userData.home).add(c.userData.delta);
  const expected=await load('fouling_cell_exploded');
  sameBounds(new THREE.Box3().setFromObject(expected),new THREE.Box3().setFromObject(assembled));
  const cutaway=prepareModel(await load('fouling_cell_cutaway'),records,material);
  assert.ok(cutaway.components.length>80);
  console.log(JSON.stringify({assembled_components:ready.components.length,cutaway_components:cutaway.components.length,
    merged_geometry_bounds:'PASS',exploded_bounds_match_STEP_export:'PASS',component_identities:'PASS'}));
}
