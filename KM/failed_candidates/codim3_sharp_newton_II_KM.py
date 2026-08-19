from pathlib import Path
import json, time, hashlib
from flint import arb,ctx,__version__ as flint_version
SRCROOT=Path('/mnt/data/II_KM_predecessor')
exec((SRCROOT/'codim3_newton_funcs.py').read_text())
ctx.prec=256
KL=json.load(open(SRCROOT/'II_KL_codim3_quotient_germinal.json'))
targets={'sqrt5_over_4':arb(5).sqrt()/4,'pi_over_6':arb.pi()/6}
def abin(lo,hi): return arb(str(lo)).union(arb(str(hi)))
def refine(br,target,pointN=16000,derN=1600):
    a,b=map(float,br); m=(a+b)/2
    fm=integrate(m,m,pointN,False); F=abin(*fm['u'])-target
    dr=integrate(a,b,derN,True); D=abin(*dr['du_dc']); assert D<0
    N=arb(str(m))-F/D
    nlo=float(N.lower());nhi=float(N.upper());ia=max(a,nlo);ib=min(b,nhi)
    assert ia<ib and ib-ia < b-a
    return [ia,ib], {'input':[a,b],'midpoint':m,'point_cells':fm['cells'],'derivative_cells':dr['cells'],'u_mid':fm['u'],'du_dc_on_input':dr['du_dc'],'newton_image':outward(N),'intersection':[ia,ib],'strict_contraction':True}
start=time.time(); outrec={}
for name,t in targets.items():
    br=KL['arb_crossing_localization'][name]['final_interval']
    b1,h1=refine(br,t)
    outrec[name]={'input_interval':br,'final_interval':b1,'history':[h1],'width':b1[1]-b1[0]}
print('crossings',outrec,flush=True)
assert outrec['sqrt5_over_4']['final_interval'][1] < outrec['pi_over_6']['final_interval'][0]
out={
 'phase':'II-KM','predecessor':'II-KL',
 'carrier':'Epstein-Vogt source-bound regular axis-start return family; numerical crossing localization kept separate from the unresolved cross-singular leaf quotient',
 'runtime':{'python_flint':flint_version,'arb_precision_bits':ctx.prec,'runtime_seconds':round(time.time()-start,3)},
 'arb_crossing_localization':{'method':'one additional interval-Newton contraction from each II-KL enclosure at 256-bit Arb precision','records':outrec,'distinct':True,'status':'PASS_FURTHER_256BIT_ARB_INTERVAL_NEWTON_CONTRACTION_BOTH_CROSSINGS'},
 'source_ingestion':{
   'new_cross_singular_holonomy_packet_supplied_this_phase':False,
   'inherited_source_bad_stratum':'alternating C8 incidence of four S3 and four T2 pieces',
   'cross_singular_quotient_atlas':'SEPARATED_NO_SOURCE_BOUND_MAP_IDENTIFYING_REGULAR_GERMS_WITH_TRUE_BAD_STRATUM_LEAF_QUOTIENT',
   'compactified_germinal_leaf_groupoid':'SEPARATED_NO_ACTUAL_CROSS_SINGULAR_HOLONOMY_TRANSITION_BYTES'
 },
 'guards':['Arb localization concerns the declared regular axis-start return family only','narrower root enclosures do not create missing singular holonomy arrows','source C8 incidence is not promoted to a quotient groupoid'],
 'decision':'PASS_SHARPER_256BIT_ARB_CROSSINGS__CROSS_SINGULAR_QUOTIENT_HOLONOMY_REMAINS_SEPARATED'
}
P=Path('/mnt/data/II_KM/II_KM_codim3_sharp_crossing_source_audit.json');P.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps({'final':{k:v['final_interval'] for k,v in outrec.items()},'widths':{k:v['width'] for k,v in outrec.items()},'runtime':out['runtime']['runtime_seconds']},indent=2))
