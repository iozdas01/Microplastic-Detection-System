// Bundle a self-contained, offline HTML viewer. No server or network required.
// Usage: node package_viewer.mjs /path/to/node_modules/containing/three/and/esbuild
import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';
const root=path.dirname(fileURLToPath(import.meta.url));
const modules=path.resolve(process.argv[2]||'node_modules');
const {build}=await import(pathToFileURL(path.join(modules,'esbuild/lib/main.js')).href);
const output=await build({entryPoints:[path.join(root,'viewer.js')],bundle:true,write:false,minify:true,
  nodePaths:[modules],format:'iife',target:'es2020',legalComments:'inline'});
const [template,manifest,assembled,section]=await Promise.all([
  fs.readFile(path.join(root,'viewer.template.html'),'utf8'),
  fs.readFile(path.join(root,'parts.json'),'utf8'),
  fs.readFile(path.join(root,'fouling_cell_realistic.glb')),
  fs.readFile(path.join(root,'fouling_cell_cutaway.glb')),
]);
const asset=JSON.stringify({manifest:JSON.parse(manifest),assembled:assembled.toString('base64'),section:section.toString('base64')});
const html=template.replace('__ASSET_DATA__',()=>asset.replaceAll('<','\\u003c'))
  .replace('__BUNDLE__',()=>output.outputFiles[0].text.replaceAll('</script','<\\/script'));
if(html.includes('__ASSET_DATA__')||html.includes('__BUNDLE__'))throw new Error('Unexpanded template token');
await fs.writeFile(path.join(root,'viewer.html'),html);
console.log(`Offline viewer: ${(Buffer.byteLength(html)/1024/1024).toFixed(1)} MB`);
