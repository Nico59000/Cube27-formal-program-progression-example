from pathlib import Path
import hashlib,json,zipfile,shutil,tempfile
ROOT=Path(__file__).resolve().parent
MAN=ROOT/'bundle_manifest_II_KL.json'
SUMS=ROOT/'SHA256SUMS.txt'
ZIP=ROOT/'II_KL_formal_bundle_R1.zip'
for p in (MAN,SUMS,ZIP):
    if p.exists(): p.unlink()

def sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1<<20),b''): h.update(b)
    return h.hexdigest()

def payload_files():
    out=[]
    for p in ROOT.rglob('*'):
        if not p.is_file(): continue
        if p in (MAN,SUMS,ZIP): continue
        if p.name == 'package_II_KL_stdout.json': continue
        rel=p.relative_to(ROOT)
        # hard exclude transient latex/render/cache artifacts
        if any(part in {'render_kl','__pycache__'} for part in rel.parts): continue
        if p.suffix in {'.aux','.log','.out','.fls','.fdb_latexmk','.synctex.gz'}: continue
        out.append(p)
    return sorted(out,key=lambda p:str(p.relative_to(ROOT)))

files=payload_files()
entries=[]
for p in files:
    entries.append({'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':sha(p)})
manifest={
 'phase':'II-KL','bundle_revision':'R1','payload_file_count':len(entries),
 'authority_registry':'II_KL_authority_registry.json',
 'pdf':'II_KL_FilteredRees_Fredholm_Germinal_Golden_FLINT_R1.pdf',
 'source_tex':'II_KL_FilteredRees_Fredholm_Germinal_Golden_FLINT_R1.tex',
 'files':entries
}
MAN.write_text(json.dumps(manifest,indent=2,sort_keys=True,ensure_ascii=False)+'\n',encoding='utf-8')
sumfiles=files+[MAN]
SUMS.write_text(''.join(f'{sha(p)}  {p.relative_to(ROOT)}\n' for p in sorted(sumfiles,key=lambda p:str(p.relative_to(ROOT)))),encoding='utf-8')
with zipfile.ZipFile(ZIP,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for p in sorted(files+[MAN,SUMS],key=lambda p:str(p.relative_to(ROOT))):
        z.write(p,arcname=str(p.relative_to(ROOT)))
# clean extraction verification
with tempfile.TemporaryDirectory(prefix='ii_kl_verify_') as td:
    td=Path(td)
    with zipfile.ZipFile(ZIP) as z:
        bad=z.testzip()
        if bad is not None: raise RuntimeError(f'testzip bad={bad}')
        z.extractall(td)
    bads=[]
    for line in (td/'SHA256SUMS.txt').read_text().splitlines():
        dg, rel=line.split('  ',1)
        q=td/rel
        if not q.is_file() or sha(q)!=dg: bads.append(rel)
    if bads: raise RuntimeError(f'hash mismatches: {bads[:10]}')
print(json.dumps({
 'payload_file_count':len(entries),
 'sha256sum_file_count':len(sumfiles),
 'zip_entry_count':len(files)+2,
 'zip_sha256':sha(ZIP),
 'zip_bytes':ZIP.stat().st_size,
 'manifest_sha256':sha(MAN),
 'sha256sums_sha256':sha(SUMS),
 'testzip':None,
 'extraction_rehash_bad_count':0
},indent=2))
