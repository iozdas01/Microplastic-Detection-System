import * as THREE from 'three';
import {mergeGeometries} from 'three/examples/jsm/utils/BufferGeometryUtils.js';

// OCCT exports a primitive per face. Merge those faces inside each component,
// preserving the component's transform, identity and STEP-derived normals.
export function prepareModel(root,records,makeMaterial){
  root.updateMatrixWorld(true);
  const originals=[];
  root.traverse(o=>{if(records.has(o.userData.cad_component||o.name))originals.push(o);});
  const components=[],meshes=[];
  for(const source of originals){
    const p=records.get(source.userData.cad_component||source.name);
    const inverse=source.matrixWorld.clone().invert(),geometries=[];
    source.traverse(o=>{
      if(!o.isMesh)return;
      let geometry=o.geometry.clone();
      if(geometry.index)geometry=geometry.toNonIndexed();
      for(const attr of Object.keys(geometry.attributes))if(!['position','normal'].includes(attr))geometry.deleteAttribute(attr);
      if(!geometry.attributes.normal)geometry.computeVertexNormals();
      geometry.applyMatrix4(inverse.clone().multiply(o.matrixWorld));geometries.push(geometry);
    });
    const geometry=mergeGeometries(geometries,false);
    if(!geometry)throw new Error(`Could not merge component ${p.name}`);
    geometries.forEach(g=>g.dispose());
    const component=new THREE.Group();component.name=p.name;
    component.position.copy(source.position);component.quaternion.copy(source.quaternion);component.scale.copy(source.scale);
    component.userData={record:p,home:source.position.clone(),delta:new THREE.Vector3(...p.explode).multiplyScalar(.001)};
    const mesh=new THREE.Mesh(geometry,makeMaterial(p));mesh.name=p.name+'_surface';
    mesh.userData.record=p;mesh.castShadow=!mesh.material.transmission;mesh.receiveShadow=true;
    component.add(mesh);source.parent.add(component);source.removeFromParent();
    components.push(component);meshes.push(mesh);
  }
  root.userData.components=components;
  return {root,components,meshes};
}
