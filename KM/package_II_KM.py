#!/usr/bin/env python3
from pathlib import Path
import hashlib,json,zipfile,shutil
ROOT=Path('/mnt/data/II_KM'); STAGE=Path('/mnt/data/II_KM_bundle_stage'); ZIP=ROOT/'II_KM_formal_bundle_R1.zip'
if not STAGE.exists(): raise SystemExit('staging directory missing; build stage first')
files=sorted(p for p in STAGE.rglob('*') if p.is_file() and p.name not in {'SHA256SUMS.txt','bundle_manifest_II_KM.json'})
manifest={'phase':'II-KM','predecessor':'II-KL','files':[{'path':str(p.relative_to(STAGE)),'size_bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in files]}
(STAGE/'bundle_manifest_II_KM.json').write_text(json.dumps(manifest,indent=2,sort_keys=True)+'\n')
all_for_sha=sorted(p for p in STAGE.rglob('*') if p.is_file() and p.name!='SHA256SUMS.txt')
(STAGE/'SHA256SUMS.txt').write_text(''.join(f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.relative_to(STAGE)}\n" for p in all_for_sha))
with zipfile.ZipFile(ZIP,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for p in sorted(p for p in STAGE.rglob('*') if p.is_file()): z.write(p,p.relative_to(STAGE))
print(json.dumps({'zip':str(ZIP),'size_bytes':ZIP.stat().st_size,'sha256':hashlib.sha256(ZIP.read_bytes()).hexdigest(),'file_count':sum(1 for p in STAGE.rglob('*') if p.is_file())},indent=2))
