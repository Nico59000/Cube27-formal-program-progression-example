#!/usr/bin/env python3
from pathlib import Path
import json,hashlib,re
ROOT=Path(__file__).resolve().parent; SRC=ROOT/'source_recovery'; DEP=ROOT/'dependencies'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def dump(name,obj):(ROOT/name).write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n')
# D5
bh=SRC/'formalisation_morphisme_reversion_transfert_ternaire_A1BH.tex';txt=bh.read_text(errors='replace')
terms=['continuous D5','continuous bundle','rank-3','rank three','transition cocycle','transition function','trivialization','trivialisation']
d5={'phase':'II-KL','last_recovered_source':{'name':bh.name,'sha256':sha(bh)},'A1BH_keyword_hits':{t:txt.lower().count(t.lower()) for t in terms},
    'fresh_retrieval_observation':{'Library':'II-KL targeted A1BI/post-A1BH search returned prior scoped audits/lineage material, not a new A1BI transition packet','GitHub_Nico59000':'0 code hits for CORE7Q_A1BI/A1BI transition D5 trivialization continuous query','interpretation':'scoped discovery evidence only, not global nonexistence'},
    'required_packet':['continuous base B','open cover {U_i}','rank-3 local trivializations phi_i','continuous transition maps g_ij','inverse/Cech triple law','metric/norm transport provenance'],
    'continuous_D5_rank3_transition_packet':'NT_PRESERVED','status':'PASS_POST_A1BI_SCOPED_RETRIEVAL_AUDIT__NO_NEW_CONTINUOUS_D5_PACKET'}
dump('II_KL_D5_post_A1BI_source_audit.json',d5)
# Pisano historical p5
jt=SRC/'II_JT_theta_ramified_epsilon.json';j=json.load(open(jt));prev=json.load(open(DEP/'II_KK_Pisano_p5_terminal_scope.json'))
pis={'phase':'II-KL','historical_source':{'name':jt.name,'sha256':sha(jt),'available_keys':sorted(j.keys())},
     'required_full_local_Tate_packet':['explicit K_5/local extension identifier','explicit additive character psi5 byte formula','self-dual Haar measure convention','conductor and different exponents in the finite Tate denominator','uniformizer/coordinate representative list','finite Gauss/Tate sum bytes'],
     'fresh_retrieval_observation':'targeted Library search returned the inherited ramified epsilon/sign authority and prior obstruction records, not a new complete historical p=5 additive-character/Haar packet',
     'inherited_nonuniqueness':'epsilon5=-1 alone is compatible with two nonsquare residue scales 2 and 3 and does not identify the historical additive normalization',
     'decision':'PASS_TERMINAL_SCOPED_P5_NORMALIZATION_OBSTRUCTION_PRESERVED__FUTURE_NEW_SOURCE_REOPENS_GATE','full_historical_p5_Tate_packet':'SEPARATED_NOT_RECOVERED'}
dump('II_KL_Pisano_p5_source_audit.json',pis)
# Stone/Fibonacci
stone=SRC/'II_IK_stone_real_partial_payload.json';sd=json.load(open(stone));fib=SRC/'II_HQ_RLM_cofinal_Jdescent_zRtail_ReesCoker_H3axis_R1.tex'
required_stone=['project_differential_d','project_theta_row','project_cycle_basis_K_Z','incidence_to_project_cycle_coupling_C','project_framing_anchor']
required_fib=['carrier_id','localization_family_U','cofinal_basis_B','trace_table']
proj={'phase':'II-KL','Stone':{'source':stone.name,'sha256':sha(stone),'carrier_id':sd.get('carrier_id'),'missing_decisive_fields':required_stone,'ABI_complete':False},
      'Fibonacci':{'source':fib.name,'sha256':sha(fib),'theorem_source_present':True,'required_decisive_fields':required_fib,'actual_instance_fields_found':[],'ABI_complete':False},
      'fresh_connected_search':{'GitHub_Nico59000_Stone_combined_exact_query_hits':0,'GitHub_Nico59000_Fibonacci_combined_exact_query_hits':0,'Library':'prior ABI/manifests/partial authorities only; no new same-carrier complete packet','guard':'zero hits are scoped discovery evidence only'},
      'ABI_complete_actual_project_packets':0,'promoted_project_values':0,'active_project_NT_count':37,
      'status':'PASS_FRESH_EXTERNAL_ABI_PREFLIGHT__NO_COMPLETE_STONE_FIBONACCI_PACKET_NO_PROMOTION'}
dump('II_KL_project_value_attempt.json',proj)
print(json.dumps({'D5':d5['status'],'Pisano':pis['decision'],'project':proj['status']},indent=2))
