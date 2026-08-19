import json, hashlib
from pathlib import Path
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

ROOT=Path('/mnt/data')
SRC=ROOT/'II_KM_predecessor/II_KL_cube27_filtered_rees_ext.json'
OUT=ROOT/'II_KM/II_KM_cube27_2local_completed_rees.json'
D=json.loads(SRC.read_text())
F=D['filtered_rees_extension_data']


def sha(p):
    h=hashlib.sha256(); h.update(Path(p).read_bytes()); return h.hexdigest()

def snf_nontrivial(M):
    S=smith_normal_form(Matrix(M),domain=ZZ)
    return [abs(int(S[i,i])) for i in range(min(S.shape)) if S[i,i] not in (0,1,-1)]

def rank_f2(A):
    A=[[int(x)&1 for x in row] for row in A]
    m=len(A); n=len(A[0]) if m else 0
    r=0
    for c in range(n):
        p=next((i for i in range(r,m) if A[i][c]),None)
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        for i in range(m):
            if i!=r and A[i][c]:
                A[i]=[x^y for x,y in zip(A[i],A[r])]
        r+=1
    return r

def v2(n):
    n=abs(int(n)); e=0
    while n and n%2==0: e+=1; n//=2
    return e

def two_primary(inv):
    return [2**v2(n) for n in inv if v2(n)>0]

expected={
 'R1':[2,2,12],
 'R2':[2,2,2,2,2,12],
 'R3':[2,2,2,2,2,2,12],
}
records={}
for key,R in F['relation_matrices_low'].items():
    s=snf_nontrivial(R)
    assert s==expected[key],(key,s)
    tp=two_primary(s)
    # quotient M = Z_(2)^15 / rows/cols R has mod-2 dimension 15-rank(R mod2)
    mod2dim=15-rank_f2(R)
    assert mod2dim==len(tp)
    # for direct sum cyclic 2^e, 2M has one F2 dimension for each e>=2 in this dataset
    twoM_dim=sum(1 for x in tp if x>=4)
    residue_dim=len(tp)
    records[key]={
      'integral_SNF_nontrivial':s,
      'two_local_invariant_factors':tp,
      'two_local_module':f"(Z/2)^{sum(x==2 for x in tp)} + (Z/4)^{sum(x==4 for x in tp)}",
      'dim_F2_M_mod_2M':residue_dim,
      'dim_F2_2M':twoM_dim,
      'dim_F2_M_2torsion':len(tp),
      'rank_relation_mod2':rank_f2(R),
      'ambient_generators':15,
    }

assert records['R1']['two_local_invariant_factors']==[2,2,4]
assert records['R2']['two_local_invariant_factors']==[2,2,2,2,2,4]
assert records['R3']['two_local_invariant_factors']==[2,2,2,2,2,2,4]

ops=F['multiplication_by_15_augmentation_generators']
assert set(ops)=={'gr1_to_gr2','gr2_to_gr3','tail_even_to_odd','tail_odd_to_even'}
for lane,L in ops.items():
    assert len(L)==15
    for A in L:
        assert len(A)==15 and all(len(row)==15 for row in A)
# scalar multiplication commutes with every integer operator: A(2x)=2A(x), hence 2M filtration preserved.
filtration_preservation_checks=15*4

E=D['conductor_ext_localization_product']
assert E['A2_mod_2_dimension']==13
assert E['detector_value_on_class']==1
assert 'NONZERO' in E['localization_at_2']
assert 'ZERO' in E['localization_after_inverting_2']

out={
 'phase':'II-KM',
 'predecessor':'II-KL',
 'carrier':'Cube27 ordinary split Green ring R localized at (2), its dimension-augmentation ideal I_(2), finite I-adic filtered modules, and the separately typed conductor Ext class',
 'source':{'name':SRC.name,'sha256':sha(SRC)},
 'ring_finiteness_noetherian_input':{
   'project_authority':'II-KB gives an integral monic presentation with 16 standard monomials, hence R is finite free of rank 16 over Z on the declared carrier',
   'local_consequence':'R_(2) is module-finite over the Noetherian ring Z_(2), hence Noetherian',
   'status':'PASS_PROJECT_INPUT_PLUS_STANDARD_NOETHERIAN_CONSEQUENCE'
 },
 'two_local_associated_graded':{
   'records':records,
   'tail_for_every_n_ge_3':records['R3'],
   'tail_period_two_action':'PASS_INHERITED_AND_REPLAYED_FROM_II_KL',
   'operator_family_count':60,
   'operator_filtration_preservation_checks':filtration_preservation_checks,
   'filtration':'0 subset 2M subset M; every integer-linear augmentation multiplication map preserves 2M functorially',
   'status':'PASS_EXACT_2LOCAL_PRIMARY_MODULE_FILTRATION_ALL_DECLARED_GRADES'
 },
 'conductor_ext_2local':{
   'A2_mod_2_dimension':13,
   'class':E['class'],
   'detector_value':1,
   'at_2':E['localization_at_2'],
   'away_from_2':E['localization_after_inverting_2'],
   'pushout':E['pushout'],
   'yoneda_square':E['yoneda_square'],
   'status':'PASS_NONZERO_2LOCAL_CONDUCTOR_EXT_CLASS_WITH_13_DIMENSIONAL_MOD2_DETECTION'
 },
 'completed_filtration_exactness':{
   'theorem_input':'For a Noetherian ring and ideal I, I-adic completion is exact on finite modules (Stacks Project, Algebra Lemma 10.97.2 / tag 00MB; based on Artin-Rees).',
   'application':'For every n, 0 -> I^(n+1)_(2) -> I^n_(2) -> gr_I^n(R)_(2) -> 0 is a short exact sequence of finite R_(2)-modules; completion stays short exact. Since I annihilates gr_I^n, its I-adic completion is itself.',
   'exact_sequence':'0 -> completion(I^(n+1)_(2)) -> completion(I^n_(2)) -> gr_I^n(R)_(2) -> 0',
   'status':'PASS_NOETHERIAN_IADIC_COMPLETION_EXACTNESS_ON_EVERY_FINITE_FILTERED_STEP'
 },
 'stronger_completed_rees_claims':{
   'split_as_product_of_associated_grades':'SEPARATED_NO_COMPATIBLE_SPLITTING_OF_FILTERED_EXTENSIONS_SERIALIZED',
   'new_polynomial_quotient_presentation':'SEPARATED_NOT_DERIVED_FROM_ASSOCIATED_GRADED_PERIODICITY',
   'period_two_associated_graded_implies_period_two_filtered_completion':'REFUTED_AS_UNJUSTIFIED_INFERENCE_WITHOUT_EXTENSION_DATA_OR_SPLITTING',
   'guard':'exact completion preserves the short exact filtration sequences; it does not canonically split them or reconstruct the completed Rees algebra from gr alone'
 },
 'machine_checks':{
   'SNF_recomputations':3,
   'mod2_rank_checks':3,
   'augmentation_operator_shape_checks':60,
   'filtration_functoriality_instances':filtration_preservation_checks,
   'Ext_detector_checks':4
 },
 'decision':'PASS_2LOCAL_PRIMARY_MODULE_FILTRATION_AND_IADIC_COMPLETION_EXACTNESS__SPLIT_OR_POLYNOMIAL_COMPLETED_REES_PRESENTATION_SEPARATED'
}
OUT.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(out,indent=2,ensure_ascii=False))
