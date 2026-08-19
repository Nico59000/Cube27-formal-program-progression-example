#!/usr/bin/env python3
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent;DEP=ROOT/'dependencies'
kk=json.load(open(DEP/'II_KK_golden_wall_H5_audit.json'));t2=json.load(open(DEP/'II_KI_golden_native_H5_type2.json'));t4=json.load(open(ROOT/'II_KL_golden_native_H5_type4.json'))
assert t2['target_native_H5_dimension']==14 and t4['target_native_H5_dimension']==34 and t4['joint_augmented_restriction_certificate']['candidate_pivots']==34
out={'phase':'II-KL','abstract_H5_dimensions':[38,38,14,56,34,56,34],
 'native_H5_closures':{
   'type2':{'group_order':48,'dimension':14,'method':'odd-index Sylow2 restriction plus actual streamed B5 reduction','status':'PASS_INHERITED_II_KI'},
   'type4':{'group_order':32,'dimension':34,'method':'direct-sum restrictions of actual native product cocycles to six elementary abelian E8 subgroups with independent actual B5 blocks','E8_subgroups_found':t4['elementary_abelian_E8_subgroups_found'],'E8_subgroups_used':t4['subgroups_used'],'rows_processed':t4['joint_augmented_restriction_certificate']['rows_processed'],'candidate_pivots':34,'status':'PASS_NEW_II_KL_SECOND_NATIVE_H5_CLOSURE'},
   'remaining_types':[0,1,3,5,6]},
 'free_Wall_degree4':{
   'predecessor_no_go':'coinvariant degree3 bytes do not determine a unique F2[H]-free lift; REFUTED preserved from II-KK',
   'required_bytes':['free Wall basis through degree4','equivariant d4','twisting cochain or contracting homotopy','free Phi3 lift','Phi4 with d_bar Phi4=Phi3 d4'],
   'new_trusted_producer_found':False,
   'status':'SEPARATED_TRUSTED_FREE_WALL_DEGREE4_PRODUCER_NOT_FOUND'},
 'guards':['type4 closure is independent of the invalid naive shuffle and does not use a free Wall comparison','E8 restrictions are detection maps on actual native cocycles, not carrier identifications','closure of type4 is not extrapolated to types3,5,6 even when dimensions repeat'],
 'status':'PASS_SECOND_NATIVE_H5_B5_CLOSURE_TYPE4__FREE_WALL_DEGREE4_STILL_SEPARATED'}
(ROOT/'II_KL_golden_H5_wall_audit.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,indent=2))
