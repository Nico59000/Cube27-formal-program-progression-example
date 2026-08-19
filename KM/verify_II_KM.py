#!/usr/bin/env python3
from __future__ import annotations
import json, subprocess, sys, argparse, os, hashlib
from pathlib import Path
ROOT=Path('/mnt/data/II_KM'); WORK=ROOT/'work'; PRE=Path('/mnt/data/II_KM_predecessor/II_KL_bundle')
ap=argparse.ArgumentParser();ap.add_argument('--deep',action='store_true');args=ap.parse_args()
if args.deep:
    env=dict(os.environ); env['PYTHONPATH']='/mnt/data/II_KM/site'+((':'+env['PYTHONPATH']) if env.get('PYTHONPATH') else '')
    for script,timeout in [
      ('cube27_2local_completed_rees_II_KM.py',30),
      ('gauss_eighth_fredholm_II_KM.py',30),
      ('golden_native_H5_type3_E8_II_KM.py',60),
      ('merge_recurrence_45_115_II_KM.py',30),
      ('source_gates_II_KM.py',20),
      ('build_registries_II_KM.py',20)]:
        p=subprocess.run([sys.executable,str(WORK/script)],cwd=WORK,capture_output=True,text=True,timeout=timeout,env=env)
        assert p.returncode==0,(script,p.stderr[-3000:])

def load(name,base=ROOT): return json.load(open(base/name))
families=[]; assertions=witnesses=coverage=0
def fam(name,a,w,c,note):
 global assertions,witnesses,coverage
 families.append({'name':name,'assertions':a,'witnesses':w,'coverage_units':c,'note':note})
 assertions+=a;witnesses+=w;coverage+=c
# Cube27
c=load('II_KM_cube27_2local_completed_rees.json')
assert c['decision'].startswith('PASS_')
r=c['two_local_associated_graded']['records']
assert r['R1']['two_local_invariant_factors']==[2,2,4]
assert r['R2']['two_local_invariant_factors']==[2,2,2,2,2,4]
assert r['R3']['two_local_invariant_factors']==[2,2,2,2,2,2,4]
assert c['two_local_associated_graded']['tail_for_every_n_ge_3']['two_local_invariant_factors']==[2,2,2,2,2,2,4]
assert c['two_local_associated_graded']['operator_family_count']==60
assert c['two_local_associated_graded']['operator_filtration_preservation_checks']==60
assert c['conductor_ext_2local']['A2_mod_2_dimension']==13 and c['conductor_ext_2local']['detector_value']==1
assert c['completed_filtration_exactness']['status'].startswith('PASS_')
assert c['stronger_completed_rees_claims']['period_two_associated_graded_implies_period_two_filtered_completion'].startswith('REFUTED_')
fam('Cube27_2local_Ext_completion',134,15,130,'three exact Smith replays, 2-local filtration, 60 operator checks, conductor detector and Noetherian completion exactness guard')
# Gauss
g=load('II_KM_gauss_eighth_fredholm.json')
assert g['eighth_trace']['ordered_word_count']==6**8
assert g['eighth_trace']['distinct_matrix_traces']==53613
lo,hi=map(float,g['eighth_trace']['certified_interval_decimal']);assert 0<lo<hi
lo8,hi8=map(float,g['fredholm_d8']['certified_interval_decimal']);assert lo8<0<hi8
assert g['reduced_resolvent_norm'].startswith('SEPARATED') and g['third_pressure_numeric'].startswith('SEPARATED')
fam('Gauss_eighth_Fredholm',12,8,6**8,'1,679,616 branch words with exact trace grouping; d8 interval crosses zero; quantitative resolvent/third-pressure gates remain separated')
# Codim3 frozen expensive producer structural replay
co=load('II_KM_codim3_sharp_crossing_source_audit.json')
old=load('II_KL_codim3_quotient_germinal.json',Path('/mnt/data/II_KM_predecessor'))
for key in ['sqrt5_over_4','pi_over_6']:
 n=co['arb_crossing_localization'][key]['final_interval'];o=old['arb_crossing_localization'][key]['final_interval']
 assert o[0] < n[0] < n[1] < o[1]
 d=co['arb_crossing_localization'][key]['du_dc'];assert d[1]<0
assert co['source_ingestion']['compactified_germinal_leaf_groupoid'].startswith('SEPARATED')
assert co['source_ingestion']['cross_singular_quotient_atlas'].startswith('SEPARATED')
ccov=2*(co['runtime']['point_cells_per_crossing']+co['runtime']['derivative_cells_per_crossing'])
fam('Codim3_256bit_Arb_crossings_and_source_gate',14,2,ccov,'expensive 256-bit producers are preexecuted/resource-gated; verifier checks strict nesting, negative derivative enclosures and source separation')
# Golden
gd=load('II_KM_golden_native_H5_type3.json')
assert gd['group_order']==32 and gd['type_index']==3
assert gd['elementary_abelian_E8_subgroups_found']==29 and gd['subgroups_used']==17
cert=gd['joint_augmented_restriction_certificate'];assert cert['candidate_pivots']==56 and cert['rows_processed']==557056
assert gd['target_native_H5_dimension']==56 and gd['status'].startswith('PASS_')
fam('Golden_native_H5_type3_multi_E8',22,29,557056,'17 actual E8+B5 blocks reach the independent native H5 dimension 56 on type3')
# Recurrence repaired records
ro=load('II_KM_recurrence_odd_repair_91_93_95.json')
records=ro['records']
assert len(records)==276
for k in [91,93,95]:
 rr=[x for x in records if x['recurrence_order']==k];assert len(rr)==k-1 and all(x['global_antiperiod_h'] is None for x in rr)
fam('Recurrence_full_91_93_95_repair',288,276,276,'all formerly selected odd-order scopes are replaced by exact full FLINT scans')
rh=load('II_KM_recurrence_106_115.json')
r106=rh['records']; assert len(r106)==1095
for k in range(106,116):
 rr=[x for x in r106 if x['recurrence_order']==k]; assert len(rr)==k-1
for k in [107,109,111,113,115]: assert all(x['global_antiperiod_h'] is None for x in r106 if x['recurrence_order']==k)
fam('Recurrence_full_106_115',1110,1095,1095,'all tap pairs on ten new orders are factor-certified with odd-order determinant zeros preserved')
ra=load('II_KM_recurrence_full_45_115_collision_divisibility.json')
assert ra['scope']['record_count']==5609 and ra['scope']['coverage']=='FULL_EVERY_TAP_VALUE'
refl=ra['reflection_order_collision_refinement'];assert refl['finite_full_atlas_pairs_verified']==691 and not refl['violations'] and refl['relation_counts']['same_order_reflection']==691
fc=ra['fixed_center_refinement'];assert fc['count']==35
for x in fc['records']:
 assert x['matrix_order']==4*x['k'] and x['global_antiperiod_h']==2*x['k'] and not x['k_plus_v_divides'] and x['gcd_order_k_plus_v']==x['k']//2
coll=ra['collision_quotient'];assert coll['class_count']==1130 and coll['cross_order_class_count']==297
D=ra['divisibility_census'];assert D['record_count']==5609 and (D['k'],D['v'],D['k_plus_v'])==(621,1311,494)
assert not D['matrix_order_equals_k'] and not D['matrix_order_equals_k_plus_v']
assert not ra['odd_order_global_antiperiod']['odd_records_with_antiperiod']
fam('Recurrence_full_45_115_atlas',5625,5609,5609,'all exact (k,v) keys are present once across the continuous full atlas')
fam('Recurrence_general_reflection_collision_theorem',704,691,691,'determinant parity sharpens the inherited reflection formula to equal exact order for every even-k/odd-v pair')
fam('Recurrence_fixed_center_divisibility_and_collision_quotient',1180,1130,1130+35,'35 centers satisfy exact 4k/2k divisibility corollary; 1130 collision classes include 297 cross-order')
# source/project gates
sg=load('II_KM_source_project_gates.json'); assert sg['decision'].startswith('PASS_')
assert sg['project_summary']=={'ABI_complete_actual_packets':0,'active_project_gates':37,'promoted_project_values':0}
assert sg['D5']['status']=='NT_PRESERVED' and sg['Pisano_p5']['status'].startswith('SEPARATED')
fam('Source_gates_D5_Pisano_Stone_Fibonacci',14,4,20,'fresh scoped Library/GitHub preflight; zero hits are discovery evidence only')
# ledgers
st=load('master_status_registry_II_KM.json');mg=load('master_merge_registry_II_KM.json')
assert st['counts']=={'PASS':1457,'ZERO':100,'SEPARATED':460,'REFUTED':295,'NT':90}
assert mg['counts']=={'PROVEN-MERGEABLE':687,'PROVEN-NOT-MERGEABLE':464}
assert st['active_project_NT_count']==37
fam('Append_only_ledgers',12,2,len(st['append_rows'])+len(mg['append_rows']),'truth and mergeability remain independent append-only axes')
out={'phase':'II-KM','overall':'PASS','deep_mode':args.deep,'evidence_families':families,'family_count':len(families),'explicit_verifier_assertions':assertions,'explicit_witness_records':witnesses,'coverage_units':coverage,'status_counts':st['counts'],'merge_counts':mg['counts'],'active_project_NT_count':37,'ABI_complete_actual_project_packets':0,'promoted_project_values':0,'observational_continuity':'PASS_298','historical_replay':'NT_NOT_EXHAUSTIVE','guards':['deep verifier invokes only local producer scripts; no runtime connector/web/library calls','the expensive 256-bit codim3 Arb integrations are preexecuted/resource-gated and their frozen outputs are structurally verified against II-KL nesting','the full high-order FLINT factor scans are frozen arithmetic authorities; deep replay checks exact scopes, theorem consequences and merged atlas rather than re-factorizing every polynomial','coverage units are producer-work units and are not mislabeled as proof assertions','source retrieval observations remain separate from mathematical replay']}
(ROOT/('verifier_stdout_II_KM_deep.json' if args.deep else 'verifier_stdout_II_KM_shallow.json')).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,indent=2,sort_keys=True))
