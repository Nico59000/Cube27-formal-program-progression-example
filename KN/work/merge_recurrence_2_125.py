import json,math,collections,hashlib
from pathlib import Path
root=Path(__file__).resolve().parents[1]
R=[]
def add(path,key='records',filterk=None):
 d=json.load(open(path)); rr=d[key]
 if filterk is not None: rr=[r for r in rr if r['recurrence_order'] in filterk]
 R.extend(rr)
add(root/'II_KN_recurrence_aux_2_44.json')
B=root/'dependencies/recurrence'
add(B/'II_KG_recurrence_order_value_45_55.json')
add(B/'II_KH_recurrence_order_value_56_65.json')
add(B/'II_KI_recurrence_order_value_66_75.json')
add(B/'II_KJ_recurrence_order_value_76_85.json')
add(B/'II_KK_recurrence_order_value_86_95.json',filterk={86,87,88,90,92,94})
d=json.load(open(B/'II_KL_recurrence_order_value_89_96_105.json'));R+=d['records_89']+d['records_96_105']
add(B/'II_KM_recurrence_odd_repair_91_93_95.json')
add(B/'II_KM_recurrence_106_115.json')
add(root/'II_KN_recurrence_116_125.json')
by={(int(r['recurrence_order']),int(r['tap_value'])):r for r in R}
expected={(k,v) for k in range(2,126) for v in range(1,k)}
assert set(by)==expected and len(by)==7750
# Dilation theorem test against primitive reduction and all divisors of gcd.
viol=[];checks=0
ray=collections.defaultdict(list)
for (k,v),r in sorted(by.items()):
 g=math.gcd(k,v); N=int(r['matrix_order'])
 a,b=k//g,v//g; N0=int(by[(a,b)]['matrix_order'])
 checks+=1
 if N!=g*N0:viol.append({'k':k,'v':v,'g':g,'N':N,'primitive':[a,b],'N0':N0})
 ray[(a,b)].append((k,v,N,g))
assert not viol
# every divisor scaling check
div_checks=0;div_viol=[]
for (k,v),r in by.items():
 g=math.gcd(k,v);N=int(r['matrix_order'])
 for d in range(1,g+1):
  if g%d==0:
   N0=int(by[(k//d,v//d)]['matrix_order']);div_checks+=1
   if N!=d*N0:div_viol.append([k,v,d,N,N0])
assert not div_viol
# Scope 45-125 main atlas
main={(k,v):r for (k,v),r in by.items() if 45<=k<=125}
assert len(main)==6804
# equal order collision stats
byN=collections.defaultdict(list)
for (k,v),r in main.items():byN[int(r['matrix_order'])].append((k,v))
classes=[]
for N,pairs in byN.items():
 if len(pairs)>=2:
  orders=sorted(set(k for k,v in pairs))
  classes.append({'matrix_order':N,'class_size':len(pairs),'order_value_pairs':[list(x) for x in sorted(pairs)],'recurrence_orders':orders,'cross_order':len(orders)>1})
classes.sort(key=lambda x:(x['matrix_order'],x['order_value_pairs']))
# normalized order quotient M=N/gcd(k,v)
byM=collections.defaultdict(list)
for (k,v),r in main.items():
 g=math.gcd(k,v); M=int(r['matrix_order'])//g
 byM[M].append((k,v,k//g,v//g,g))
norm_classes=[]
for M,pairs in byM.items():
 if len(pairs)>=2:
  primitive=set((a,b) for k,v,a,b,g in pairs)
  norm_classes.append({'primitive_normalized_order':M,'class_size':len(pairs),'primitive_ray_count':len(primitive),'contains_multiple_dilations_same_ray':len(pairs)>len(primitive),'pairs':[list(x) for x in sorted(pairs)]})
norm_classes.sort(key=lambda x:(x['primitive_normalized_order'],x['pairs']))
# Ray multiplicities within main scope
rays=collections.defaultdict(list)
for (k,v),r in main.items():
 g=math.gcd(k,v); rays[(k//g,v//g)].append({'d':g,'k':k,'v':v,'N':int(r['matrix_order'])})
ray_multi=[{'primitive':[a,b],'primitive_order':int(by[(a,b)]['matrix_order']),'members':sorted(ms,key=lambda x:x['d'])} for (a,b),ms in rays.items() if len(ms)>=2]
ray_multi.sort(key=lambda x:(x['primitive'][0],x['primitive'][1]))
# Dilation theorem proof metadata
proof=[
 'For a monic f with f(0)!=0 over F_p, ord(f) is the least N with f | x^N-1 (companion minimal polynomial).',
 'Upper bound: f|x^N-1 implies f(x^d)|(x^d)^N-1=x^(dN)-1.',
 'For the converse write d=p^a e with (e,p)=1. If f(x^d)|x^M-1, the e-th root-of-unity orbit among roots forces e|M.',
 'The substitution x^(p^a e) multiplies every root multiplicity by p^a; roots of x^M-1 have multiplicity p^v_p(M), so p^a|M. Hence d|M.',
 'Write M=dL. Polynomial division after the injective substitution y->x^d shows f|y^L-1, hence ord(f)|L. Therefore d*ord(f)|M.',
 'Combining with the upper bound gives ord(f(x^d))=d*ord(f).'
]
out={
 'phase':'II-KN',
 'family':'f_{k,v}(x)=x^k-x^v-1 over F3',
 'main_scope':{'orders':[45,125],'record_count':len(main),'expected':'sum_{k=45}^{125}(k-1)=6804','coverage':'FULL_EVERY_TAP'},
 'auxiliary_theorem_replay_scope':{'orders':[2,125],'record_count':len(by),'coverage':'FULL_EVERY_TAP','purpose':'qualify primitive reductions for dilation theorem; auxiliary scope is not a carrier replacement'},
 'dilation_theorem':{
  'statement':'For every d>=1 and 1<=v<k, ord C(dk,dv)=d*ord C(k,v) over F3.',
  'general_polynomial_statement':'For every monic f over F_p with f(0)!=0, if ord(f)=min{N:f|x^N-1}, then ord(f(x^d))=d*ord(f).',
  'proof':proof,
  'primitive_corollary':'With g=gcd(k,v), ord C(k,v)=g*ord C(k/g,v/g); hence gcd(k,v) always divides the matrix order.',
  'normalized_ray_invariant':'ord C(k,v)/gcd(k,v) depends only on the primitive pair (k/g,v/g).',
  'full_2_125_primitive_checks':checks,
  'all_divisor_scaling_checks':div_checks,
  'violations':viol,
  'status':'PASS_GENERAL_PROOF_PLUS_FULL_2_125_EXACT_FLINT_REPLAY'
 },
 'main_collision_quotient':{'class_count':len(classes),'cross_order_class_count':sum(c['cross_order'] for c in classes),'largest_class_size':max(c['class_size'] for c in classes),'classes':classes,'status':'PASS_EXACT_45_125'},
 'normalized_order_stratification':{'class_count_with_multiplicity':len(norm_classes),'classes_spanning_multiple_primitive_rays':sum(c['primitive_ray_count']>1 for c in norm_classes),'classes_with_same_ray_multiple_dilations':sum(c['contains_multiple_dilations_same_ray'] for c in norm_classes),'multi_member_ray_count':len(ray_multi),'ray_records':ray_multi,'status':'PASS_DILATION_RAY_QUOTIENT'},
 'guards':['dilation theorem is internal to polynomial/companion-order carrier','auxiliary orders 2-44 are theorem qualification data, not a rewrite of earlier project atlases','no recurrence normalized-order class is identified with Golden/Cube27/D5/Stone/Fibonacci carriers'],
 'decision':'PASS_FULL_116_125_AND_GENERAL_DILATION_DIVISIBILITY_STRATIFICATION_BEYOND_REFLECTION'
}
P=root/'II_KN_recurrence_45_125_dilation_collision.json';P.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps({'main_records':len(main),'all_records':len(by),'dilation_checks':checks,'divisor_checks':div_checks,'collisions':len(classes),'cross':sum(c['cross_order'] for c in classes),'norm_classes':len(norm_classes),'norm_cross_rays':sum(c['primitive_ray_count']>1 for c in norm_classes),'multi_rays':len(ray_multi)},indent=2))
print(hashlib.sha256(P.read_bytes()).hexdigest())
