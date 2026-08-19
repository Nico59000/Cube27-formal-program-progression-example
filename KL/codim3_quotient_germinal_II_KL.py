#!/usr/bin/env python3
from __future__ import annotations
import json,sys
from pathlib import Path
from flint import arb,ctx,__version__ as flint_version
ROOT=Path(__file__).resolve().parent;DEP=ROOT/'dependencies';SRC=ROOT/'source_recovery';ctx.prec=192
exec((ROOT/'codim3_newton_funcs.py').read_text())
kk=json.load(open(DEP/'II_KK_codim3_source_groupoid_newton.json'))
jf=json.load(open(SRC/'II_JF_codimension3_support_context.json'))
jr=json.load(open(SRC/'II_JR_codim3_nonhausdorff_leafspace_model.json'))
targets={'sqrt5_over_4':arb(5).sqrt()/4,'pi_over_6':arb.pi()/6}
def abin(lo,hi):return arb(str(lo)).union(arb(str(hi)))
def refine_newton(br,target):
    a,b=map(float,br);m=(a+b)/2
    fm=integrate(m,m,25000,False);F=abin(*fm['u'])-target
    dr=integrate(a,b,2200,True);D=abin(*dr['du_dc']);assert D<0
    N=arb(str(m))-F/D;nlo=float(N.lower());nhi=float(N.upper());ia=max(a,nlo);ib=min(b,nhi)
    assert ia<ib and ib-ia<b-a
    return [ia,ib],{'input':[a,b],'midpoint':m,'point_cells':fm['cells'],'derivative_cells':dr['cells'],'u_mid':fm['u'],'du_dc_on_input':dr['du_dc'],'newton_image':outward(N),'intersection':[ia,ib],'strict_contraction':True}
b1,h1=refine_newton(kk['interval_newton']['sqrt5_over_4']['final_interval'],targets['sqrt5_over_4'])
b2,h2=refine_newton(kk['interval_newton']['pi_over_6']['final_interval'],targets['pi_over_6'])
levels=[0.84,0.86,0.88,0.90,0.92,0.94,0.96]
germs=[]
for c in levels:
    q=integrate(c,c,450,False)
    germs.append({'level':c,'u_interval':q['u'],'w_angle':'0 on the declared axis-start representative','half_return_germ':'H_c=R_{u(c)} S_0 T','involution_identity':'H_c^2=1','cells':q['cells']})
shadow=jf['exact_combinatorial_shadow'];assert shadow['graph']=='C8' and shadow['vertices']==8 and shadow['edges']==8
strata=[{'bead':i,'type':'S3' if i%2==0 else 'T2','shared_circle_left':(i-1)%8,'shared_circle_right':i} for i in range(8)]
source_atlas={'objects':strata,'shared_circle_count':8,'incidence_cycle':'C8','two_step_rotation':'C4 on each bead-type four-set','source_role':'bad-set stratum incidence only; not a leaf holonomy quotient atlas'}
out={'phase':'II-KL','runtime':{'python':sys.version.split()[0],'python_flint':flint_version,'arb_precision_bits':ctx.prec},
 'arb_crossing_localization':{'method':'one further interval-Newton contraction from each II-KK enclosure','sqrt5_over_4':{'final_interval':b1,'history':[h1]},'pi_over_6':{'final_interval':b2,'history':[h2]},'distinct':b1[1]<b2[0],'status':'PASS_FURTHER_ARB_INTERVAL_NEWTON_CONTRACTION_ON_BOTH_UNIQUE_CROSSINGS'},
 'regular_germinal_holonomy_atlas':{'carrier':'axis-start regular transverse one-parameter family on the certified regular level strip','records':germs,'germ_formula':'H_c=R_{u(c)}S_0T and H_c^2=1','status':'PASS_SOURCE_FORMULA_PLUS_ARB_INTERVAL_GERMS_ON_SEVEN_REGULAR_LEVELS'},
 'source_bound_bad_stratum_atlas':source_atlas,
 'nonhausdorff_support':{'model':jr['model'],'theorems':jr['theorems'],'guard':jr['guard'],'status':'PASS_TYPED_LOCAL_SUPPORT_MODEL_ONLY'},
 'cross_singular_quotient_atlas':'SEPARATED_NO_SOURCE_BOUND_MAP_IDENTIFYING_REGULAR_GERMS_WITH_THE_TRUE_C8_BAD_STRATUM_LEAF_QUOTIENT',
 'compactified_germinal_leaf_groupoid':'SEPARATED_NO_ACTUAL_CROSS_SINGULAR_HOLONOMY_TRANSITION_BYTES',
 'guards':['regular germ records use the actual return-holonomy formula but only the declared axis-start family','C8 is a source-bound bad-stratum incidence shadow, not by itself a holonomy groupoid','the doubled-origin model remains a local non-Hausdorff support model and is not identified with the actual leaf space','crossing constants are exact target levels with unique roots on the certified strip, not asymptotic attractors'],
 'status':'PASS_SHARPER_ARB_CROSSINGS_AND_REGULAR_GERMINAL_HOLONOMY_ATLAS__CROSS_SINGULAR_QUOTIENT_GROUPOID_SEPARATED'}
(ROOT/'II_KL_codim3_quotient_germinal.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps({'sqrt5':b1,'pi6':b2,'widths':[b1[1]-b1[0],b2[1]-b2[0]],'germs':len(germs)},indent=2))
