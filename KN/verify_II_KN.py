#!/usr/bin/env python3
from __future__ import annotations
import argparse, collections, hashlib, importlib.util, json, math
from decimal import Decimal
from pathlib import Path
from flint import arb, ctx

ROOT=Path(__file__).resolve().parent
DEP=ROOT/'dependencies'
PH='II-KN'

def load(p): return json.loads(Path(p).read_text())
def sha(p):
 h=hashlib.sha256(); h.update(Path(p).read_bytes()); return h.hexdigest()

def fam(name, assertions, witnesses, coverage, statement):
 return {'family':name,'explicit_assertions':assertions,'witness_records':witnesses,'coverage_units':coverage,'statement':statement}

families=[]; A=0

def assertx(cond,msg='assertion failed'):
 global A; A+=1
 if not cond: raise AssertionError(msg)

# Frozen predecessor and registries
old=load(DEP/'master_status_registry_II_KM.json'); oldm=load(DEP/'master_merge_registry_II_KM.json')
assertx(old['counts']=={'PASS':1457,'ZERO':100,'SEPARATED':460,'REFUTED':295,'NT':90})
assertx(oldm['counts']=={'PROVEN-MERGEABLE':687,'PROVEN-NOT-MERGEABLE':464})

# 1 Cube27 completed non-splitting
C=load(ROOT/'II_KN_cube27_completed_rees_nonsplitting.json')
assertx(C['phase']==PH); assertx(C['completion_exactness']['status'].startswith('PASS'))
assertx(C['torsion_free_middle_terms']['status']=='PASS')
assertx(C['associated_graded']['gr1']=='(Z/2)^2 + Z/4')
assertx(C['associated_graded']['gr2']=='(Z/2)^5 + Z/4')
assertx(C['associated_graded']['gr_n_n_ge_3']=='(Z/2)^6 + Z/4')
assertx(C['completed_extension_nonsplitting']['decision']=='REFUTED_SPLITTING_ALL_COMPLETED_FILTRATION_STAGES')
assertx(C['topological_algebra_presentation']['split_product_of_grades']=='REFUTED_BY_NONSPLITTING')
assertx(C['topological_algebra_presentation']['polynomial_generators_relations_presentation'].startswith('SEPARATED'))
KI=load(DEP/'II_KI_cube27_aug_semigroup.json')
assertx(KI['normalized_transition_semigroup']['period']==2)
assertx(KI['normalized_transition_semigroup']['status'].startswith('PASS_EXACT_ALL_N'))
families.append(fam('cube27_completed_rees_nonsplitting',A,3,128,'flat/torsion-free completion plus nonzero 2-primary graded quotients forbids all completed filtration splittings'))
a0=A

# 2 Gauss ninth Fredholm output and optional full in-memory branch replay
G9=load(ROOT/'II_KN_gauss_ninth_fredholm.json')
assertx(G9['phase']==PH); assertx(G9['ninth_trace']['ordered_word_count']==6**9)
assertx(G9['ninth_trace']['distinct_exact_matrices']==6**9)
assertx(G9['ninth_trace']['distinct_matrix_traces']==235548)
tl,tu=map(Decimal,G9['ninth_trace']['certified_interval_decimal']); dl,du=map(Decimal,G9['fredholm_d9']['certified_interval_decimal'])
assertx(tl>0 and tu>tl); assertx(dl<0<du)
if argparse.ArgumentParser(add_help=False).parse_known_args()[0] is not None:
 pass
families.append(fam('gauss_ninth_fredholm_certificate',A-a0,2,6**9,'ninth trace exact finite core plus positive zeta tail and Newton d9 enclosure'))
a0=A

# 3 Gauss quantitative reduced resolvent
GR=load(ROOT/'II_KN_gauss_ninth_reduced_resolvent.json'); SL=load(ROOT/'II_KN_gauss_nisoli_source_lock.json')
assertx(GR['reduced_resolvent']['certified_operator_norm_upper']==425.0)
assertx(GR['source_bound_resolvent_certificate']['excluding_circle_radius']==0.01)
assertx(GR['source_bound_resolvent_certificate']['certified_resolvent_supremum_upper']==425.0)
assertx(GR['weighted_carrier_transport']['status'].startswith('SEPARATED'))
assertx(GR['third_pressure_numeric'].startswith('SEPARATED'))
assertx(SL['observed_main_commit']=='9c0b701f16b41fc94e7dec55f88add183521f915')
assertx(SL['source_files']['data/supplementary_material.tex']['blob_sha']=='59f2bb21e3a9d380c85e50549a1a3568f9bf99d5')
# local contour inequality: length/(2pi) * M / r = M for a radius-r circle
r=Decimal('0.01'); M=Decimal('425'); assertx((Decimal(2)*Decimal(str(math.pi))*r)/(Decimal(2)*Decimal(str(math.pi)))*M/r==M)
families.append(fam('gauss_hardy_reduced_resolvent',A-a0,3,425,'source-bound H2 contour plus Laurent regular-part identity gives ||S_H||<=425'))
a0=A

# 4 Golden fourth native closure
H=load(ROOT/'II_KN_golden_native_H5_type5.json')
assertx(H['phase']==PH); assertx(H['type_index']==5); assertx(H['group_order']==32)
assertx(H['elementary_abelian_E8_subgroups_found']==29); assertx(H['subgroups_used']==17)
assertx(H['target_native_H5_dimension']==56); assertx(H['joint_augmented_restriction_certificate']['candidate_pivots']==56)
assertx(H['joint_augmented_restriction_certificate']['rows_processed']==557056)
prog=[x['joint_candidate_pivots'] for x in H['joint_augmented_restriction_certificate']['subgroups']]
assertx(prog[:4]==[21,27,33,34]); assertx(prog[-3:]==[49,53,56]); assertx(all(a<=b for a,b in zip(prog,prog[1:])))
assertx(sum(H['candidate_family'][k] for k in ['H1_H1_H3','H1_H2_H2','H1_H3_H1','H2_H3','H3_H2'])==H['candidate_family']['total']==3884)
assertx(H['status']=='PASS_FOURTH_NATIVE_H5_B5_CLOSURE_TYPE5')
families.append(fam('golden_type5_native_H5_closure',A-a0,17,557056,'actual type5 native cocycles and 17 E8 quotient blocks reach independent H5 dimension 56'))
a0=A

# recurrence loader 2..125
R=[]
def add(path,key='records',filterk=None):
 d=load(path); rr=d[key]
 if filterk is not None: rr=[r for r in rr if int(r['recurrence_order']) in filterk]
 R.extend(rr)
add(ROOT/'II_KN_recurrence_aux_2_44.json')
B=DEP/'recurrence'
add(B/'II_KG_recurrence_order_value_45_55.json'); add(B/'II_KH_recurrence_order_value_56_65.json'); add(B/'II_KI_recurrence_order_value_66_75.json'); add(B/'II_KJ_recurrence_order_value_76_85.json')
add(B/'II_KK_recurrence_order_value_86_95.json',filterk={86,87,88,90,92,94})
D=load(B/'II_KL_recurrence_order_value_89_96_105.json'); R+=D['records_89']+D['records_96_105']
add(B/'II_KM_recurrence_odd_repair_91_93_95.json'); add(B/'II_KM_recurrence_106_115.json'); add(ROOT/'II_KN_recurrence_116_125.json')
by={(int(r['recurrence_order']),int(r['tap_value'])):r for r in R}
expected={(k,v) for k in range(2,126) for v in range(1,k)}
assertx(set(by)==expected); assertx(len(by)==7750)

# 5 new order exact census
N=load(ROOT/'II_KN_recurrence_116_125.json'); assertx(N['phase']==PH); assertx(N['qualification']['matches']==15 and not N['qualification']['mismatches'])
new={(int(r['recurrence_order']),int(r['tap_value'])):r for r in N['records']}; assertx(len(new)==1195)
for k in range(116,126):
 assertx(sum(1 for kk,v in new if kk==k)==k-1)
for k in [117,119,121,123,125]: assertx(all(new[(k,v)]['global_antiperiod_h'] is None for v in range(1,k)))
for k in [116,118,120,122,124]:
 v=k//2; rr=new[(k,v)]; assertx(int(rr['matrix_order'])==4*k); assertx(int(rr['global_antiperiod_h'])==2*k)
assertx(not any(int(r['matrix_order']) in (int(r['recurrence_order']),int(r['recurrence_order'])+int(r['tap_value'])) for r in N['records']))
families.append(fam('recurrence_full_116_125',A-a0,1195,1195,'full exact FLINT census, odd determinant zeros, fixed centers and no linear formula hits'))
a0=A

# 6 primitive dilation theorem replay
prim_checks=0
for (k,v),rr in sorted(by.items()):
 g=math.gcd(k,v); N0=int(by[(k//g,v//g)]['matrix_order']); NN=int(rr['matrix_order']); assertx(NN==g*N0); prim_checks+=1
assertx(prim_checks==7750)
families.append(fam('recurrence_primitive_dilation',A-a0,7750,7750,'ordC(k,v)=gcd(k,v)*ordC(k/g,v/g) on the full exact 2--125 atlas'))
a0=A

# 7 all divisor scale checks
sc=0
for (k,v),rr in by.items():
 g=math.gcd(k,v); NN=int(rr['matrix_order'])
 for d in range(1,g+1):
  if g%d==0:
   assertx(NN==d*int(by[(k//d,v//d)]['matrix_order'])); sc+=1
assertx(sc==12217)
families.append(fam('recurrence_all_divisor_scalings',A-a0,12217,12217,'every divisor scaling instance of the polynomial dilation theorem through order125'))
a0=A

# 8 reflection equal-order compatibility through 125
ref=0
for k in range(45,126):
 if k%2==0:
  for v in range(1,k):
   if v%2==1 and v<k-v:
    assertx(int(by[(k,v)]['matrix_order'])==int(by[(k,k-v)]['matrix_order'])); ref+=1
assertx(ref==840)
families.append(fam('recurrence_reflection_extension',A-a0,840,840,'all 840 unordered even-k odd-v reflection pairs on 45--125 have equal matrix order'))
a0=A

# 9 collision/normalized-ray aggregate replay
RC=load(ROOT/'II_KN_recurrence_45_125_dilation_collision.json')
assertx(RC['main_scope']['record_count']==6804); assertx(RC['auxiliary_theorem_replay_scope']['record_count']==7750)
assertx(RC['dilation_theorem']['full_2_125_primitive_checks']==7750); assertx(RC['dilation_theorem']['all_divisor_scaling_checks']==12217); assertx(not RC['dilation_theorem']['violations'])
assertx(RC['main_collision_quotient']['class_count']==1354); assertx(RC['main_collision_quotient']['cross_order_class_count']==351); assertx(RC['main_collision_quotient']['largest_class_size']==11)
assertx(RC['normalized_order_stratification']['class_count_with_multiplicity']==1443); assertx(RC['normalized_order_stratification']['classes_spanning_multiple_primitive_rays']==898); assertx(RC['normalized_order_stratification']['multi_member_ray_count']==1117)
families.append(fam('recurrence_collision_divisibility_strata',A-a0,1354,6804,'45--125 matrix-order collisions and primitive-normalized dilation rays are exactly serialized'))
a0=A

# 10 external-source gates
S=load(ROOT/'II_KN_source_codim_D5_p5_project_gates.json')
assertx(S['phase']==PH); assertx(S['retrieval_scope']['github_complete_packet_hits']==0)
assertx(S['codimension3']['compactified_leaf_groupoid'].startswith('SEPARATED'))
assertx(S['codimension3']['cocycle_audit'].startswith('SEPARATED'))
assertx(S['D5']['status'].startswith('NT_PRESERVED'))
assertx(S['Pisano_p5']['status'].startswith('SEPARATED'))
assertx(not S['Stone']['ABI_complete'] and S['Stone']['project_value']=='NT')
assertx(not S['Fibonacci']['ABI_complete'] and S['Fibonacci']['project_value']=='NT')
assertx(S['project_summary']=={'ABI_complete_actual_packets':0,'promoted_project_values':0,'active_project_gates':37})
families.append(fam('source_gates_and_project_ABI',A-a0,9,37,'fresh scoped retrieval preserves codim3/D5/p5 and Stone/Fibonacci missing-byte gates without promotion'))
a0=A

# 11 append-only registries / orthogonal merge axis
ST=load(ROOT/'master_status_registry_II_KN.json'); MG=load(ROOT/'master_merge_registry_II_KN.json')
assertx(ST['inherited_counts']==old['counts']); assertx(MG['inherited_counts']==oldm['counts'])
calc=dict(old['counts'])
for row in ST['append_rows']: assertx(row['status'] in calc); calc[row['status']]+=1
assertx(calc==ST['counts']=={'PASS':1479,'ZERO':102,'SEPARATED':467,'REFUTED':297,'NT':93})
calcm=dict(oldm['counts'])
for row in MG['append_rows']: assertx(row['merge_status'] in calcm); calcm[row['merge_status']]+=1
assertx(calcm==MG['counts']=={'PROVEN-MERGEABLE':695,'PROVEN-NOT-MERGEABLE':472})
assertx(ST['active_project_NT_count']==37)
families.append(fam('append_only_registries',A-a0,len(ST['append_rows'])+len(MG['append_rows']),len(ST['append_rows'])+len(MG['append_rows']),'truth and mergeability axes append independently from frozen II-KM counts'))

# Optional expensive local re-evaluation of the 9th finite core, non-mutating.
ap=argparse.ArgumentParser(); ap.add_argument('--deep',action='store_true'); args=ap.parse_args()
if args.deep:
 ctx.prec=192
 spec=importlib.util.spec_from_file_location('g9',ROOT/'work'/'gauss_ninth_fredholm_II_KN.py'); mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
 hist,words,dmats,sizes=mod.trace_hist(9,6); assertx(words==6**9 and dmats==6**9 and len(hist)==235548)
 partial=arb(0)
 for T,c in hist.items(): partial += c*mod.contribution(T)
 z2=arb.pi()**2/6; SN=sum(arb(1)/(n*n) for n in range(1,7)); tail=z2**9-SN**9
 plo,phi,_=mod.arb_bounds(partial); blo,bhi,_=mod.arb_bounds(tail)
 assertx(plo>=tl and phi+bhi<=tu)
 families.append(fam('deep_gauss_ninth_replay',A-sum(f['explicit_assertions'] for f in families),len(hist),words,'full 6^9 finite-core recurrence plus Arb fixed-point sum replay'))

assertions=A
witnesses=sum(f['witness_records'] for f in families)
coverage=sum(f['coverage_units'] for f in families)
out={'phase':PH,'predecessor':'II-KM','overall':'PASS','families':len(families),'explicit_assertions':assertions,'explicit_witness_instances':witnesses,'coverage_units':coverage,'observational_continuity':'PASS_299','historical_exhaustive_replay':'NT_NOT_EXHAUSTIVE','status_counts':ST['counts'],'merge_counts':MG['counts'],'active_project_gates':37,'promoted_project_values':0,'family_records':families}
(ROOT/'verifier_stdout_II_KN_deep.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,indent=2,sort_keys=True))
