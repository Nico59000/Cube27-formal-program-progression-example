import json, math, collections, hashlib
from pathlib import Path
B=Path('/mnt/data/II_KM_predecessor/recurrence')
KM=Path('/mnt/data/II_KM'); KL=Path('/mnt/data/II_KM_predecessor/II_KL_recurrence_order_value_89_96_105.json')
records=[]; sources=[]
def add(path,key='records',filterk=None):
 d=json.load(open(path)); rr=d[key]
 if filterk is not None: rr=[r for r in rr if r['recurrence_order'] in filterk]
 records.extend(rr); sources.append({'name':Path(path).name,'sha256':hashlib.sha256(Path(path).read_bytes()).hexdigest(),'records_used':len(rr)})
add(B/'II_KG_recurrence_order_value_45_55.json')
add(B/'II_KH_recurrence_order_value_56_65.json')
add(B/'II_KI_recurrence_order_value_66_75.json')
add(B/'II_KJ_recurrence_order_value_76_85.json')
add(B/'II_KK_recurrence_order_value_86_95.json',filterk={86,87,88,90,92,94})
dkl=json.load(open(KL)); records.extend(dkl['records_89']);sources.append({'name':KL.name+':records_89','sha256':hashlib.sha256(KL.read_bytes()).hexdigest(),'records_used':len(dkl['records_89'])})
add(KM/'II_KM_recurrence_odd_repair_91_93_95.json')
records.extend(dkl['records_96_105']);sources.append({'name':KL.name+':records_96_105','sha256':hashlib.sha256(KL.read_bytes()).hexdigest(),'records_used':len(dkl['records_96_105'])})
add(KM/'II_KM_recurrence_106_115.json')
# validate exact continuous full atlas
bykv={}
for r in records:
 k=int(r['recurrence_order']);v=int(r['tap_value']); key=(k,v)
 if key in bykv:
  # selected/full overlap must be byte-value consistent if encountered; our filters should avoid this
  assert int(bykv[key]['matrix_order'])==int(r['matrix_order'])
 else: bykv[key]=r
records=[bykv[x] for x in sorted(bykv)]
expected={(k,v) for k in range(45,116) for v in range(1,k)}
assert set(bykv)==expected,(len(bykv),len(expected),sorted(expected-set(bykv))[:5])
assert len(records)==5609
# normalize property helpers
def bfield(r,*names):
 for n in names:
  if n in r:return bool(r[n])
 return None
def v2(n):
 e=0
 while n%2==0 and n:
  e+=1;n//=2
 return e
# formula hits and divisibility
formula_k=[];formula_kv=[]; div={'k':0,'v':0,'k_plus_v':0}
antis=[]
for r in records:
 k=r['recurrence_order'];v=r['tap_value'];N=int(r['matrix_order'])
 if N==k:formula_k.append([k,v])
 if N==k+v:formula_kv.append([k,v])
 if N%k==0:div['k']+=1
 if N%v==0:div['v']+=1
 if N%(k+v)==0:div['k_plus_v']+=1
 if r.get('global_antiperiod_h') is not None:antis.append(r)
assert not formula_k and not formula_kv
# reflection theorem + sharpened order/collision classification on even k odd v, unordered pairs v<k-v
refl=[];viol=[];same_count=0;double_count=0;half_count=0
for k in range(46,116,2):
 for v in range(1,k//2):
  if v%2==0:continue
  a=bykv[(k,v)]; b=bykv[(k,k-v)]
  N=int(a['matrix_order']);Np=int(b['matrix_order'])
  anti=a.get('global_antiperiod_h') is not None
  if anti:
   assert a['global_antiperiod_h']==N//2
   pred=N//math.gcd(N,N//2-1)
   simple=N//2 if v2(N)==1 else N
  else:
   pred=math.lcm(2,N)
   simple=2*N if v2(N)==0 else N
  ok=(Np==pred==simple)
  if not ok:viol.append([k,v,N,Np,anti,pred,simple])
  relation='same' if Np==N else ('double' if Np==2*N else ('half' if 2*Np==N else 'other'))
  if relation=='same':same_count+=1
  elif relation=='double':double_count+=1
  elif relation=='half':half_count+=1
  refl.append({'k':k,'v':v,'reflected_v':k-v,'N':N,'N_reflected':Np,'v2_N':v2(N),'minus_I_in_cyclic_group':anti,'relation':relation})
assert not viol
# fixed centers theorem consequences
fixed=[]
for k in range(46,116,2):
 v=k//2;r=bykv[(k,v)];N=int(r['matrix_order']);h=r.get('global_antiperiod_h')
 assert N==4*k and h==2*k
 fixed.append({'k':k,'v':v,'matrix_order':N,'global_antiperiod_h':h,'gcd_order_k_plus_v':math.gcd(N,k+v),'k_plus_v_divides':N%(k+v)==0})
 assert math.gcd(N,k+v)==k//2 and N%(k+v)!=0
# collisions
classes=[]
for N,grp in collections.defaultdict(list).items():pass
byN=collections.defaultdict(list)
for r in records:byN[int(r['matrix_order'])].append((r['recurrence_order'],r['tap_value']))
for N,pairs in byN.items():
 if len(pairs)>=2:
  orders=sorted(set(k for k,v in pairs))
  classes.append({'matrix_order':N,'class_size':len(pairs),'order_value_pairs':[list(x) for x in sorted(pairs)],'recurrence_orders':orders,'cross_order':len(orders)>1,'contains_fixed_center':any(k%2==0 and v==k//2 for k,v in pairs)})
classes.sort(key=lambda x:(x['matrix_order'],x['order_value_pairs']))
cross=sum(x['cross_order'] for x in classes)
maxsize=max(x['class_size'] for x in classes)
largest=[x for x in classes if x['class_size']==maxsize]
# Count collision classes explained by at least one same-order reflection pair
reflection_collision_classes=0
for c in classes:
 S={tuple(x) for x in c['order_value_pairs']};found=False
 for k,v in list(S):
  if k%2==0 and v%2==1 and (k,k-v) in S:found=True;break
 if found:reflection_collision_classes+=1
# odd global anti theorem audit
odd_anti=[(r['recurrence_order'],r['tap_value']) for r in antis if r['recurrence_order']%2]
assert not odd_anti
out={
 'phase':'II-KM','family':'f_{k,v}(x)=x^k-x^v-1 over F3, full factor-certified atlas',
 'scope':{'orders':[45,115],'record_count':len(records),'expected_sum':'sum_{k=45}^{115}(k-1)=5609','coverage':'FULL_EVERY_TAP_VALUE'},
 'sources':sources,
 'reflection_order_collision_refinement':{
  'theorem':'For even k and odd v, f_{k,k-v}(x)=-x^k f_{k,v}(-1/x), so C_ref is similar to -C^{-1}. If N=ord(C): when -I is absent from <C>, N_ref=lcm(2,N), hence N_ref=2N for v2(N)=0 and N_ref=N for v2(N)>=1. When C^(N/2)=-I, N_ref=N/gcd(N,N/2-1), hence N_ref=N/2 for v2(N)=1 and N_ref=N for v2(N)>=2.',
  'finite_full_atlas_pairs_verified':len(refl),'violations':viol,
  'relation_counts':{'same_order_reflection':same_count,'double_order_reflection':double_count,'half_order_reflection':half_count},
  'status':'PASS_SHARP_2ADIC_REFLECTION_ORDER_CLASSIFICATION_AND_COLLISION_CRITERION'
 },
 'fixed_center_refinement':{
   'count':len(fixed),'records':fixed,
   'theorem':'For every even k, v=k/2 has ord(C)=4k and h_anti=2k; consequently k|ord(C), v|ord(C), gcd(ord(C),k+v)=k/2 and (k+v) does not divide ord(C).',
   'status':'PASS_FIXED_CENTER_DIVISIBILITY_AND_NON_DIVISIBILITY_COROLLARY'
 },
 'divisibility_census':{**div,'record_count':len(records),'matrix_order_equals_k':formula_k,'matrix_order_equals_k_plus_v':formula_kv,'status':'PASS_EXACT_CENSUS_ON_FULL_45_115_ATLAS'},
 'odd_order_global_antiperiod':{'odd_records_with_antiperiod':odd_anti,'status':'ZERO_BY_DETERMINANT_THEOREM_AND_FULL_ATLAS_REPLAY'},
 'collision_quotient':{'class_count':len(classes),'cross_order_class_count':cross,'classes_containing_same_order_reflection_collision':reflection_collision_classes,'largest_class_size':maxsize,'largest_classes':largest,'classes':classes,'status':'PASS_EXACT_EQUAL_MATRIX_ORDER_QUOTIENT_FULL_45_115'},
 'guards':['all collision/divisibility assertions live only on the recurrence carrier','full means every tap 1<=v<k for each integer order 45<=k<=115; no state-space 3^k enumeration is used','factor certificates/matrix orders are exact FLINT-derived arithmetic data','no numerical coincidence is identified with Golden, Cube27, D5, Stone or Fibonacci project carriers'],
 'decision':'PASS_FULL_45_115_ATLAS_AND_SHARP_2ADIC_REFLECTION_COLLISION_DIVISIBILITY_REFINEMENT'
}
P=KM/'II_KM_recurrence_full_45_115_collision_divisibility.json';P.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps({
 'records':len(records),'reflection_pairs':len(refl),'relations':out['reflection_order_collision_refinement']['relation_counts'],
 'collision_classes':len(classes),'cross_order':cross,'reflection_collision_classes':reflection_collision_classes,
 'largest_size':maxsize,'largest_examples':largest[:3], 'divisibility':div,'anti_count':len(antis)
},indent=2))
print('sha',hashlib.sha256(P.read_bytes()).hexdigest())
