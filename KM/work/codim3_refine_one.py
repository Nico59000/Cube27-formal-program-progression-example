from pathlib import Path
import json,sys,time
from flint import arb,ctx
SRCROOT=Path('/mnt/data/II_KM_predecessor')
exec((SRCROOT/'codim3_newton_funcs.py').read_text())
ctx.prec=256
KL=json.load(open(SRCROOT/'II_KL_codim3_quotient_germinal.json'))
name=sys.argv[1]
PN=int(sys.argv[2]) if len(sys.argv)>2 else 25000
DN=int(sys.argv[3]) if len(sys.argv)>3 else 2200
target={'sqrt5_over_4':arb(5).sqrt()/4,'pi_over_6':arb.pi()/6}[name]
br=KL['arb_crossing_localization'][name]['final_interval']
def abin(lo,hi):return arb(str(lo)).union(arb(str(hi)))
a,b=map(float,br);m=(a+b)/2;t=time.time()
fm=integrate(m,m,PN,False);F=abin(*fm['u'])-target
dr=integrate(a,b,DN,True);D=abin(*dr['du_dc']);assert D<0
N=arb(str(m))-F/D
nlo=float(N.lower());nhi=float(N.upper());ia=max(a,nlo);ib=min(b,nhi)
out={'name':name,'input':br,'midpoint':m,'point_cells':fm['cells'],'derivative_cells':dr['cells'],'u_mid':fm['u'],'du_dc':dr['du_dc'],'newton_image':outward(N),'intersection':[ia,ib],'strict_contraction':ia<ib and ib-ia<b-a,'runtime_seconds':round(time.time()-t,3)}
print(json.dumps(out,indent=2))
Path(f'/mnt/data/II_KM/work/{name}_refine_{PN}_{DN}.json').write_text(json.dumps(out,indent=2)+'\n')
assert out['strict_contraction']
