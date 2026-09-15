import fs from 'node:fs/promises';
import path from 'node:path';
import {Presentation, PresentationFile, FileBlob} from '@oai/artifact-tool';
import {finalizePresentation} from '/Users/izginozdas/.codex/plugins/cache/openai-primary-runtime/presentations/26.909.11814/skills/presentations/container_tools/artifact_tool_utils.mjs';

const root='/Users/izginozdas/Documents/Startup/Microplastic Detection System';
const workspaceDir=path.join(root,'reports/pitch-deck');
const build=path.join(workspaceDir,'.build');
const out=path.join(workspaceDir,'output');
const skill='/Users/izginozdas/.codex/plugins/cache/openai-primary-runtime/presentations/26.909.11814/skills/presentations';
const runtime='/Users/izginozdas/.cache/codex-runtimes/codex-primary-runtime/dependencies';
await fs.mkdir(out,{recursive:true});
await fs.mkdir(path.join(workspaceDir,'assets'),{recursive:true});
await fs.copyFile('/Users/izginozdas/.codex/generated_images/01a0a306-876d-7690-80e6-7a7deaf0be9e/exec-fb4b782c-d080-404a-a9a0-10369ced1b12.png',path.join(workspaceDir,'assets/fibre-artwork.png'));
const hero=new Uint8Array(await fs.readFile(path.join(workspaceDir,'assets/fibre-artwork.png')));
const p=Presentation.create({slideSize:{width:1280,height:720}});
const C={white:'#FFFFFF',cream:'#E9E4D6',muted:'#A7A5AE',violet:'#8A4FC7',cyan:'#3CC8D8',black:'#000000'};
const font='Helvetica Neue';
let id=0;
function txt(s,t,x,y,w,h,size=28,color=C.white,bold=false){
 const b=s.shapes.add({geometry:'textbox',name:'text-'+(++id),position:{left:x,top:y,width:w,height:h},fill:'none',line:{fill:'none',width:0}});
 b.text=t;b.text.style={typeface:font,fontSize:size,color,bold,autoFit:'none',verticalAlignment:'top',insets:{top:0,bottom:0,left:0,right:0}};return b;
}
function line(s,x,y,w,color='#34313A',height=1){s.shapes.add({geometry:'line',position:{left:x,top:y,width:w,height:0},fill:'none',line:{fill:color,width:height}});}
function slide(label,num){const s=p.slides.add();s.background.fill=C.black;txt(s,label.toUpperCase(),64,42,1000,26,16,C.muted);txt(s,String(num).padStart(2,'0'),1160,42,55,25,16,C.muted);return s;}
function note(s,t){s.speakerNotes.textFrame.setText(t);}
function art(s,pos={left:0,top:0,width:1280,height:720}){s.images.add({blob:hero,contentType:'image/png',position:pos,fit:'cover',alt:'Conceptual violet textile fibre artwork, not a measured micrograph'});}
const source='Source: reports/outreach/copy/pitch.md, 2026-09-14. Editorial draft from the existing investor brief.\n';

// 01. Minimal cover with native editable typography.
{
 const s=p.slides.add();s.background.fill=C.black;art(s);
 txt(s,'Lattice',60,166,700,205,174,C.white,true);
 txt(s,'Sensing the impossible.',66,385,680,62,43,C.white);
 txt(s,'Microfibre measurement\nat the factory outlet',68,467,580,100,29,C.cream);
 txt(s,'Sandra Zalas  /  Izgin Ozdas',68,650,640,28,20,C.cream);
 txt(s,'PRE-SEED DRAFT  /  SEPT 2026',68,50,700,26,15,C.muted);
 note(s,source+'Lattice is the working company name in the founder brief. Opening: Textile manufacturing needs a microfibre number while the process can still respond. We are developing measurement at the dye-machine outlet. The technology is pre-prototype, not a validated product.\nCover artwork generated with OpenAI image generation: false-colour violet textile fibre on black, cream pixel dithering and cyan detection highlight. Conceptual brand artwork, not laboratory evidence.\nName/relationship to Baltic Jungle Lab remains a founder decision.');
}

// 02. The problem, anchored in a concrete lab example and a customer observation.
{
 const s=slide('Problem',2);
 txt(s,'The batch is gone.\nThe result is still in the lab.',64,106,1135,158,61,C.white,true);
 txt(s,'4',58,284,320,190,170,C.cyan,true);
 txt(s,'weeks',68,473,370,67,51,C.white,true);
 txt(s,'€390 per wastewater sample¹',70,564,490,39,25,C.cream);
 txt(s,'“We do not necessarily\ncontrol microfiber.”',585,314,626,130,42,C.white);
 txt(s,'H&M water team',587,459,590,30,22,C.muted);
 txt(s,'Mills use total suspended solids as a proxy.\nIt does not identify which particles are fibres.',587,523,610,80,25,C.cream);
 txt(s,'¹ Measurlabs listing cited in the brief. Four weeks after receipt, plus €97 per order.',69,662,1120,27,15,C.muted);
 note(s,source+'Evidence E7: H&M supplier wastewater control uses TSS (30 mg/L), not fibre counts. The team reported that it does not necessarily control microfibre directly. Quote kept in context.\nEvidence E15: Measurlabs micro-Raman wastewater analysis, €390 per sample plus €97 order fee, results four weeks after receipt. This is one commercial example, not a universal turnaround. https://measurlabs.com/products/microplastics-in-water-and-wastewater-micro-raman/\nSources: reports/03-validation/evidence.md, E3, E7, E15.');
}

// 03. Editable process diagram from the pitch's proposed architecture.
{
 const s=slide('Solution',3);
 txt(s,'A microfibre number\nfor every batch',64,106,1110,151,62,C.white,true);
 txt(s,'An optical module beside the dye-machine discharge line.',66,283,1130,44,29,C.cream);
 const stages=[['01','Sample','A bypass draws\nprocess water.'],['02','Capture + image','A membrane holds fibres\nfor polarised imaging.'],['03','Measure','Count and size fibres,\nlinked to the batch.']];
 const xs=[68,472,886];
 for(let i=0;i<3;i++){
  const [n,title,body]=stages[i];const x=xs[i];
  txt(s,n,x,389,90,48,32,i===1?C.cyan:C.violet,true);
  txt(s,title,x,453,340,48,31,C.white,true);
  txt(s,body,x,516,326,83,24,C.cream);
  if(i<2){line(s,x+110,408,240,i===0?C.violet:C.cyan,2);}
 }
 txt(s,'Development target. Next test: optical contrast in dyed wastewater.',68,658,1140,30,18,C.muted);
 note(s,source+'Proposed at-line architecture from the optical technology brief, 2026-09-07, private/tech/optical-tech-brief-2026-09-07.pdf. Discharge bypass, conditioning, membrane capture, polarised imaging, classifier, output linked to stage, batch and machine.\nCount and size first. Synthetic versus natural classification remains a testable technical target. Do not claim that natural fibres universally stay dark under crossed polarisers. Do not assert polymer identity, accuracy or a measured response time.\nEvidence E10: adidas prioritises size distribution and identifies contrast/background noise in dyed effluent as a key risk. Evidence E8: interest in before/after ETP measurement without flow stoppage.\nCurrent state in the source brief: imaging-rig design exists. Stage 0 has not run and the lab kit is planned after investment.');
}

// 04. Evidence of industry attention, without implying a universal regulation.
{
 const s=slide('Why now',4);
 txt(s,'The industry is testing\nits own proxy',64,107,1150,151,62,C.white,true);
 txt(s,'15',58,294,400,178,154,C.cyan,true);
 txt(s,'facilities',67,469,425,58,46,C.white,true);
 txt(s,'TMC + ZDHC study, April 2026',68,549,500,70,25,C.cream);
 txt(s,'Can suspended solids stand in\nfor actual fibre counts?',624,319,588,100,34,C.white,true);
 txt(s,'adidas, lululemon, Primark and Tesco\nco-fund the second research phase.',626,443,580,85,26,C.cream);
 txt(s,'Inditex also grades mills on whether\nthey control fibre release.',626,558,580,74,26,C.cream);
 txt(s,'Industry research and supplier standards. No universal mill discharge limit claimed.',68,663,1142,27,15,C.muted);
 note(s,source+'Evidence E13: The Microfibre Consortium and ZDHC launched Phase 2 research at 15 facilities, co-funded by adidas, lululemon, Primark and Tesco, comparing TSS with image-based fibre counts. https://www.roadmaptozero.com/post/the-microfibre-consortium-and-zdhc-advance-joint-research-to-strengthen-wastewater-monitoring-of-fibre-fragmentation\nEvidence E4: Inditex Green to Wear 3.2, July 2026, B-ranking criterion for fibres/microfibres released without internal control. This is a supplier grading requirement, not a demand for a numerical fibre count.\nEvidence E14: TMC/ZDHC state intent to set maximum allowable effluent fibre limits, but no timing is given.\nCountercase: if the proxy validates, existing TSS measurement may be good enough. E11: adidas expects limited near-term regulatory/claims pull. All dates and research claims here are from supplied source artifacts, not independently refreshed for this draft.');
}

// 05. Typography-led team slide; biographies and proposed advisers retain their status.
{
 const s=slide('Team',5);
 txt(s,'Factory engineering meets\ntextile industry access',64,108,1150,148,60,C.white,true);
 txt(s,'Sandra Zalas',67,309,567,63,48,C.white,true);
 txt(s,'CEO',68,382,550,35,23,C.cyan,true);
 txt(s,'Founder, Baltic Jungle Lab\nPFR School of Pioneers winner\nLed the brand discovery calls',68,440,544,118,26,C.cream);
 txt(s,'Izgin Ozdas',692,309,530,63,48,C.white,true);
 txt(s,'CTO',694,382,500,35,23,C.cyan,true);
 txt(s,'CNC-line automation at IMTEK\nCambridge MPhil\nManufacturing interoperability',694,440,510,118,26,C.cream);
 line(s,68,595,1140);
 txt(s,'Engineering: Jeffrey Chang, ML  /  Irfan Ali, textile data',68,618,1140,34,22,C.cream);
 txt(s,'Proposed advisors: Manu Prakash, Sam Brooks, Daniel Theobald. Naming approval pending.',68,666,1140,26,16,C.muted);
 note(s,source+'Founder biographies: founders/sandra-zalas.md and founders/izgin-ozdas.md. Current title allocation follows the 2026-09-14 pitch, which is newer than some founder records. Sandra founded Baltic Jungle Lab and is a PFR School of Pioneers winner. Izgin contributed to CNC robot automation at IMTEK and holds a Cambridge MPhil in Industrial Systems, Manufacturing & Management with interoperability work.\nJeffrey Chang introduced ML/computer-vision experience on the Matter call. Irfan Ali role comes from the founder pitch, with his one-line bio still open. Proposed advisor names remain explicitly unconfirmed for external naming.\nFounder decisions outstanding: Igor Veredyn introduced himself on H&M call as technical co-founder; whether he belongs on the team slide is unresolved. Confirm final roles, Sandra biography and advisor consent before external circulation.');
}

// 06. Distinguish interest, access and commercial commitment.
{
 const s=slide('Traction',6);
 txt(s,'Industry conversations\nare opening doors',64,105,1140,152,62,C.white,true);
 const rows=[
  ['adidas','“This is the first time I’ve come across such a device.”','Partner introductions conditional on a working prototype.'],
  ['H&M Group','“No one is… monitoring.”','Open to exploring access to a supplier site.'],
  ['Matter','Technical conversations under NDA','Industrial microfibre filtration.']
 ];
 let y=301;
 for(const [name,quote,status]of rows){
  txt(s,name,68,y,325,50,36,C.white,true);
  txt(s,quote,431,y,775,53,name==='adidas'?26:29,C.cream);
  txt(s,status,433,y+52,772,34,21,C.muted);
  if(y<545)line(s,68,y+108,1140);
  y+=127;
 }
 txt(s,'Pre-revenue. Pre-funding. No signed LOI or paid pilot.',68,674,1140,27,18,C.cyan);
 note(s,source+'Evidence E10: adidas microfibre lead Varija Subasingha said this was the first such device she had come across. It is an observation by one interviewee, not a novelty or exclusivity claim. E9: offered potential brand-partner/Fashion for Good introductions conditional on a good prototype.\nEvidence E8: H&M innovation/water team quote, with ellipsis retained, referred to monitoring compared with filtration/ETP solutions known to them. E9: supplier access was tentative, not arranged.\nMatter conversations are under NDA. This slide intentionally carries only relationship status and publicly described industry. Any further pilot invitation details require the founders to approve wording against the NDA.\nAll relationships are active conversations, not revenue, paid design partnerships or signed pilots. Sources: E5-E10, reports/03-validation/evidence.md.');
}

// 07. The larger ambition and a clearly conditional market model.
{
 const s=slide('Why the future',7);
 txt(s,'Every dye machine first.\nIndustrial liquids next.',64,104,1140,151,62,C.white,true);
 txt(s,'50–150k',58,291,715,140,112,C.cyan,true);
 txt(s,'dyeing machines in service',67,443,736,50,33,C.white,true);
 txt(s,'Estimated installed base',69,501,650,35,23,C.muted);
 txt(s,'$60–450M',858,326,370,65,47,C.white,true);
 txt(s,'annual software opportunity\nat full modelled adoption',861,405,352,86,24,C.cream);
 txt(s,'Fibre measurement is the first application.\nThe ambition is observability for physical processes.',69,559,1135,82,31,C.white);
 txt(s,'Scenario: 50–150k machines × $100–250/month. Assumptions, not a revenue forecast.',69,655,1140,24,15,C.muted);
 txt(s,'Next: validate optical contrast, then a plant pilot. Funding target to be confirmed.',69,684,1140,23,15,C.cream);
 note(s,source+'Market figures are assumptions in the existing pitch. Installed base 50,000-150,000 inferred from shipment flow, an assumed 15-20 year service life and local manufacturers outside the reporting sample. Do not present the installed base as a measured count.\nAnnual software scenario: 50,000 × $100/month × 12 = $60M; 150,000 × $250/month × 12 = $450M. Assumes 100% adoption and one paid subscription per machine. No tested willingness to pay, validated price or sales forecast.\nShipment source used in the brief: ITMF via https://www.textileworld.com/textile-world/2026/07/itmf-global-textile-machinery-shipments-shrunk-in-2025-except-for-spinning/ . Do not confuse annual shipments with the installed base.\nExpansion is a founder vision from input-context/belief.md, not validated demand in every liquid process. Funding amount, use-of-funds allocation, and timeline remain founder decisions.');
}

const candidate=path.join(build,'candidate.pptx');
await(await PresentationFile.exportPptx(p)).save(candidate);
console.log('Draft exported. Finalizing.');
const finalPath=path.join(out,'Lattice-investor-draft.pptx');
const result=await finalizePresentation({workspaceDir,candidatePath:candidate,finalPath,pythonExecutable:path.join(runtime,'python/bin/python3'),integrityValidatorPath:path.join(skill,'container_tools/inspect_presentation_package_integrity.py'),layoutValidatorPath:path.join(skill,'container_tools/inspect_presentation_layout_geometry.py'),layoutArgs:['--expected-slide-size-emu','12192000,6858000','--validate-bullet-geometry','--validate-heading-fit'],explicitTotalSlideCount:7,requiredNativeTableOwnerSlides:[],requiredNativeChartOwnerSlides:[],fontPolicy:{basis:'design',families:[font]},verifyArtifactToolImport:true,receiptPath:path.join(build,'validation.json')});
console.log(JSON.stringify(result));
const final=await PresentationFile.importPptx(await FileBlob.load(finalPath));
for(let i=0;i<final.slides.items.length;i++){
 const b=await final.export({slide:final.slides.items[i],format:'png',scale:1});
 await fs.writeFile(path.join(build,`slide-${i+1}.png`),new Uint8Array(await b.arrayBuffer()));
 console.log('Rendered slide '+(i+1));
}
await fs.writeFile(path.join(build,'presentation.json'),JSON.stringify(p.toProto()));
console.log('FINAL: '+finalPath);
