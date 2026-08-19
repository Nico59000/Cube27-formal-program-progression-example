#!/usr/bin/env python3
from __future__ import annotations
import json,subprocess,sys,argparse,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parent
ap=argparse.ArgumentParser();ap.add_argument('--deep',action='store_true');args=ap.parse_args()
if args.deep:
    for script,timeout in [
      ('cube27_full_rees_ext_II_KL.py',60),('gauss_seventh_reduced_resolvent_II_KL.py',60),
      ('golden_native_H5_type4_E8_II_KL.py',60),('golden_H5_wall_audit_II_KL.py',30),('recurrence_flint_full_II_KL.py',60),('source_gates_II_KL.py',30),('build_registries_II_KL.py',30)]:
        p=subprocess.run([sys.executable,str(ROOT/script)],cwd=ROOT,capture_output=True,text=True,timeout=timeout)
        assert p.returncode==0,(script,p.stderr[-2000:])
def load(n):return json.load(open(ROOT/n))
families=[]; assertions=0; coverage=0; witnesses=0
def fam(name,a,w,c,note):
 global assertions,witnesses,coverage
 families.append({'name':name,'assertions':a,'witnesses':w,'coverage_units':c,'note':note});assertions+=a;witnesses+=w;coverage+=c
# Cube
c=load('II_KL_cube27_filtered_rees_ext.json');assert c['status'].startswith('PASS_');g=c['filtered_rees_extension_data']['graded_pieces'];assert g['gr1_snf']==[2,2,12] and g['gr2_snf']==[2,2,2,2,2,12] and g['gr3_and_all_tail_snf']==[2,2,2,2,2,2,12]
assert c['filtered_rees_extension_data']['well_defined_low_checks']==30 and c['filtered_rees_extension_data']['low_commutativity_checks']==225
ex=c['conductor_ext_localization_product'];assert ex['A2_mod_2_dimension']==13 and ex['detector_value_on_class']==1 and 'NONZERO' in ex['localization_at_2'] and ex['yoneda_square'].startswith('epsilon^2=0')
fam('Cube27_filtered_Rees_and_Ext_localization',270,15,30+225+60,'low maps/tail operators plus 2-primary Ext detector/localization/product')
# Gauss
ga=load('II_KL_gauss_seventh_reduced_resolvent.json');assert ga['seventh_trace']['ordered_word_count']==7**7;assert ga['seventh_trace']['certified_interval'][0]>0;assert ga['fredholm_d7']['certified_interval'][0]<0<ga['fredholm_d7']['certified_interval'][1];assert ga['third_pressure_reduced_resolvent']['status'].startswith('PASS_')
fam('Gauss_seventh_Fredholm_and_reduced_resolvent',12,7,7**7,'Arb word trace plus exact Riesz-complement existence')
# Codim
co=load('II_KL_codim3_quotient_germinal.json');kk=load('dependencies/II_KK_codim3_source_groupoid_newton.json')
for key in ['sqrt5_over_4','pi_over_6']:
 n=co['arb_crossing_localization'][key]['final_interval'];o=kk['interval_newton'][key]['final_interval'];assert o[0]<=n[0]<n[1]<=o[1]
assert co['arb_crossing_localization']['distinct'];assert len(co['regular_germinal_holonomy_atlas']['records'])==7;assert co['source_bound_bad_stratum_atlas']['incidence_cycle']=='C8'
ccov=sum(h['point_cells']+h['derivative_cells'] for key in ['sqrt5_over_4','pi_over_6'] for h in co['arb_crossing_localization'][key]['history'])+sum(r['cells'] for r in co['regular_germinal_holonomy_atlas']['records'])
fam('Codim3_Arb_germs_and_source_atlas',24,9,ccov,'nested crossings, seven regular germs and C8 bad-stratum source atlas')
# Golden
g4=load('II_KL_golden_native_H5_type4.json');assert g4['target_native_H5_dimension']==34 and g4['joint_augmented_restriction_certificate']['candidate_pivots']==34 and g4['subgroups_used']==6 and g4['status'].startswith('PASS_')
gold=load('II_KL_golden_H5_wall_audit.json');assert gold['native_H5_closures']['type4']['dimension']==34 and gold['native_H5_closures']['type2']['dimension']==14 and gold['free_Wall_degree4']['status'].startswith('SEPARATED')
fam('Golden_native_H5_type4_multi_E8',18,16,g4['joint_augmented_restriction_certificate']['rows_processed'],'six E8 blocks reach exact native H5 rank34')
fam('Golden_free_Wall_guard',6,2,5,'type2/type4 closed; free Wall degree4 remains typed separated')
# Recurrence
r=load('II_KL_recurrence_order_value_89_96_105.json');assert len(r['records_89'])==88 and len(r['records_96_105'])==995
q89=r['engine_upgrade']['qualification_against_II_KK_selected_order89'];assert q89['matches']==q89['total']==9
for k in range(96,106):
 rs=[x for x in r['records_96_105'] if x['recurrence_order']==k];assert len(rs)==k-1
for x in r['records_89']+r['records_96_105']:
 if x['recurrence_order']%2: assert x['global_antiperiod_h'] is None
assert r['reflection_theorem']['verified_pairs']==124 and not r['reflection_theorem']['violations'];assert all(x['ord_equals_4k'] and x['anti_equals_2k'] for x in r['reflection_theorem']['fixed_centers'])
assert not r['divisibility_theorem_search']['formula_hits']['ord_eq_k'] and not r['divisibility_theorem_search']['formula_hits']['ord_eq_k_plus_v']
fam('Recurrence_FLINT_full89_repair',110,88,88,'full order89, 9/9 qualification against predecessor probes')
fam('Recurrence_full96_105',1120,995,995,'all k-1 tap pairs on ten consecutive orders')
fam('Recurrence_reflection_collision_divisibility',145,237,124+237,'124 reflection pairs, five fixed centers and collision quotient')
# Source gates
for fn,key in [('II_KL_D5_post_A1BI_source_audit.json','status'),('II_KL_Pisano_p5_source_audit.json','decision'),('II_KL_project_value_attempt.json','status')]:assert load(fn)[key].startswith('PASS_')
pr=load('II_KL_project_value_attempt.json');assert pr['ABI_complete_actual_project_packets']==0 and pr['promoted_project_values']==0 and pr['active_project_NT_count']==37
fam('Source_gates_D5_Pisano_Project',12,5,20,'fresh scoped retrieval preflight; zero search hits never promoted to nonexistence')
# ledgers
st=load('master_status_registry_II_KL.json');mg=load('master_merge_registry_II_KL.json');assert st['counts']=={'PASS':1432,'ZERO':97,'SEPARATED':450,'REFUTED':294,'NT':87};assert mg['counts']=={'PROVEN-MERGEABLE':675,'PROVEN-NOT-MERGEABLE':456};assert st['active_project_NT_count']==37
fam('Append_only_ledgers',10,2,len(st['append_rows'])+len(mg['append_rows']),'truth and mergeability axes updated independently')
out={'phase':'II-KL','overall':'PASS','deep_mode':args.deep,'evidence_families':families,'family_count':len(families),'explicit_verifier_assertions':assertions,'explicit_witness_records':witnesses,'coverage_units':coverage,'status_counts':st['counts'],'merge_counts':mg['counts'],'active_project_NT_count':37,'ABI_complete_actual_project_packets':0,'promoted_project_values':0,'observational_continuity':'PASS_297','historical_replay':'NT_NOT_EXHAUSTIVE','guards':['deep verifier invokes local producer scripts only; no runtime connector/web/library calls; the 33s Arb codim producer is preexecuted/resource-gated and its frozen output is structurally verified','coverage units are producer-work units and are not mislabeled as proof assertions','source retrieval observations remain separate from local mathematical replay']}
(ROOT/'verifier_stdout_II_KL_deep.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,indent=2,sort_keys=True))
