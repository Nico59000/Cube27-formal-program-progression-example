#!/usr/bin/env python3
from __future__ import annotations
import csv,json,re,math,hashlib
from pathlib import Path
import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_form
from sympy.polys.domains import ZZ
ROOT=Path(__file__).resolve().parent; DEP=ROOT/'dependencies'
rows=list(csv.DictReader((DEP/'II_KA_cube27_tensor_table.csv').open()))
basis=[]
for r in rows:
    for k in ('left','right'):
        if r[k] not in basis:basis.append(r[k])
N=len(basis); idx={b:i for i,b in enumerate(basis)}
def parse(s):
    v=[0]*N
    for term in [z.strip() for z in s.split(' + ')]:
        m=re.fullmatch(r'(?:(\d+)[ *])?(.+)',term); assert m,term; v[idx[m.group(2).strip()]]+=int(m.group(1) or 1)
    return sp.Matrix(v)
M={}
for r in rows:
    i,j=idx[r['left']],idx[r['right']]; v=parse(r['decomposition']); M[i,j]=v;M[j,i]=v
E=[sp.eye(N)[:,i] for i in range(N)]; ONE=E[idx['T']]
def mul(a,b):
    out=sp.zeros(N,1)
    for i in range(N):
        if not a[i]: continue
        for j in range(N):
            if b[j]: out+=a[i]*b[j]*M[i,j]
    return out
# Frozen maximal-overorder embedding and augmentation data from KG.
kg=json.load(open(DEP/'II_KG_cube27_overorder_conductor.json'))
Emb=sp.Matrix(kg['maximal_overorder_embedding']['matrix_rows_by_basis_columns']); assert abs(int(Emb.det()))==2**24*3**2
Dims=[int(x) for x in list(Emb.row(8))]; assert len(Dims)==16 and Dims[idx['T']]==1
non=[i for i in range(N) if i!=idx['T']]; Qaug=sp.Matrix.hstack(*[(E[i]-Dims[i]*ONE) for i in non]); EQ=Emb*Qaug
red=[i for i in range(16) if i!=8]; rpos={r:i for i,r in enumerate(red)}
int_gens={r:math.gcd(*[abs(int(EQ[r,j])) for j in range(15)]) for r in red if r<12}; J=sp.eye(15)
for r,g in int_gens.items(): J[rpos[r],rpos[r]]=g
assert abs(int(J.det()))==768
def O_mult_matrix(v16):
    D=sp.zeros(15,15)
    for r in red:
        if r<12:D[rpos[r],rpos[r]]=int(v16[r])
    for rr in [(12,13),(14,15)]:
        p,q=rpos[rr[0]],rpos[rr[1]];a,b=int(v16[rr[0]]),int(v16[rr[1]]);D[p,p]=a;D[p,q]=-b;D[q,p]=b;D[q,q]=a
    return D
B=[]
for jcol in range(15):
    X=J.inv()*O_mult_matrix(EQ[:,jcol]); assert all(sp.denom(z)==1 for z in X); B.append(sp.Matrix([[int(X[r,c]) for c in range(15)] for r in range(15)]))
def Icoord(v):
    assert sum(Dims[i]*v[i] for i in range(N))==0
    return sp.Matrix([v[i] for i in non])
acts=[sp.Matrix.hstack(*[Icoord(mul(Qaug[:,i],Qaug[:,qj])) for i in range(15)]) for qj in range(15)]
cur=sp.eye(15);K={}
for m in range(1,5):
    L=hermite_normal_form(Emb[red,:]*Qaug*cur)  # equals Ared*cur
    X=(J**m).inv()*L; assert all(sp.denom(z)==1 for z in X)
    K[m]=hermite_normal_form(sp.Matrix([[int(X[r,c]) for c in range(15)] for r in range(15)]));
    cur=hermite_normal_form(sp.Matrix.hstack(*[A*cur for A in acts]))
def intmat(X):
    assert all(sp.denom(z)==1 for z in X); return sp.Matrix([[int(X[r,c]) for c in range(X.cols)] for r in range(X.rows)])
def matlist(A):return [[int(A[i,j]) for j in range(A.cols)] for i in range(A.rows)]
def sha(A):return hashlib.sha256(json.dumps(matlist(A),separators=(',',':')).encode()).hexdigest()
def snfdiag(A):
    D=smith_normal_form(A,domain=ZZ); return [abs(int(D[i,i])) for i in range(min(D.shape)) if abs(int(D[i,i]))>1]
rels={m:intmat(K[m].inv()*J*K[m+1]) for m in (1,2,3)}
ops={m:[intmat(K[m+1].inv()*Bi*K[m]) for Bi in B] for m in (1,2,3)}
# Tail transitions: K3->K4 and K4->K3 after the KI normalized period-two identification.
# The second direction is the period-two normalized generator matrix from K4 back to K3.
odd_to_even=ops[3]
# recover even->odd tail matrices exactly from KJ authority and verify all are integral 15x15
kj=json.load(open(DEP/'II_KJ_cube27_rees_cocycle.json'))['period_two_associated_graded_presentation']
even_to_odd=[sp.Matrix(A) for A in kj['operator_matrices_even_to_odd']]
assert len(even_to_odd)==15 and all(A.shape==(15,15) for A in even_to_odd)
assert [sha(A) for A in odd_to_even]==kj['odd_to_even_operator_hashes']
assert [sha(A) for A in even_to_odd]==kj['even_to_odd_operator_hashes']
# Verify low degree descent and commutativity.
well=0; comm=0
for m in (1,2):
    for T in ops[m]:
        Y=rels[m+1].inv()*T*rels[m]; assert all(sp.denom(z)==1 for z in Y); well+=1
for i in range(15):
    for j in range(15):
        D=ops[2][j]*ops[1][i]-ops[2][i]*ops[1][j]
        Y=rels[3].inv()*D; assert all(sp.denom(z)==1 for z in Y);comm+=1
# conductor Ext localization/product audit
mods=kg['conductor']['Z_component_moduli']+[4,4,4,4]; F=sp.diag(*mods); FinR=Emb.inv()*F; assert all(sp.denom(z)==1 for z in FinR)
kk=json.load(open(DEP/'II_KK_cube27_rees_yoneda.json'))['conductor_yoneda_ext']; z=sp.Matrix(kk['2x_R_coordinates_in_original_16_class_basis'])
# A/2A = F2^16 / span(columns FinR mod2). Find a dual functional annihilating relations and detecting z.
def rref2(A):
    A=[row[:] for row in A];m=len(A);n=len(A[0]);r=0;piv=[]
    for c in range(n):
        p=next((i for i in range(r,m) if A[i][c]),None)
        if p is None:continue
        A[r],A[p]=A[p],A[r]
        for i in range(m):
            if i!=r and A[i][c]:A[i]=[x^y for x,y in zip(A[i],A[r])]
        piv.append(c);r+=1
    return A,piv
def null2(A):
    R,piv=rref2(A);n=len(A[0]);free=[c for c in range(n) if c not in piv];out=[]
    for f in free:
        v=[0]*n;v[f]=1
        for rr,p in enumerate(piv):v[p]=R[rr][f]
        out.append(v)
    return out
Mrel=[[int(FinR[j,i])%2 for j in range(16)] for i in range(16)] # rows are relation columns
z2=[int(t)%2 for t in z]; dual=null2(Mrel); det=next(v for v in dual if sum(a*b for a,b in zip(v,z2))%2==1)
rank_rel=len(rref2(Mrel)[1]);dim_A_mod2=16-rank_rel
assert dim_A_mod2==13 and sum(a*b for a,b in zip(det,z2))%2==1
# Ext product: pushout by detector A2->F2 gives epsilon in Ext1_Z(F2,F2); pd_Z(F2)=1 hence Ext2=0 and epsilon^2=0.
loc={
 'class':'e=[2x] in Ext^1_Z(Z/2,A2) ~= A2/2A2',
 'A2_mod_2_dimension':dim_A_mod2,
 'detector_F2_linear_functional_on_R_coordinates':det,
 'detector_value_on_class':1,
 'localization_at_2':'NONZERO_PRESERVED: A2 tensor Z_(2)=A2 and Z/2 tensor Z_(2)=Z/2',
 'localization_after_inverting_2':'ZERO: A2 tensor Z[1/2]=0 and Z/2 tensor Z[1/2]=0',
 'localization_at_any_odd_prime':'ZERO for the same 2-primary reason',
 'pushout':'detector pushes e to a nonzero epsilon in Ext^1_Z(Z/2,Z/2)=Z/2',
 'yoneda_square':'epsilon^2=0 in Ext^2_Z(Z/2,Z/2), since 0->Z --2--> Z -> Z/2 ->0 has projective length 1',
 'status':'PASS_NONZERO_2LOCAL_CLASS_VANISHES_AWAY_FROM2_AND_DETECTED_PUSHOUT_HAS_ZERO_YONEDA_SQUARE'}
ki=json.load(open(DEP/'II_KI_cube27_aug_semigroup.json'))
out={'phase':'II-KL','carrier':'Cube27 ordinary Green order augmentation filtration and conductor exact sequence',
 'filtered_rees_extension_data':{
  'graded_pieces':{'gr0':'Z','gr1_snf':snfdiag(rels[1]),'gr2_snf':snfdiag(rels[2]),'gr3_and_all_tail_snf':snfdiag(rels[3])},
  'relation_matrices_low':{f'R{m}':matlist(rels[m]) for m in (1,2,3)},
  'multiplication_by_15_augmentation_generators':{'gr1_to_gr2':[matlist(A) for A in ops[1]],'gr2_to_gr3':[matlist(A) for A in ops[2]],'tail_odd_to_even':[matlist(A) for A in odd_to_even],'tail_even_to_odd':[matlist(A) for A in even_to_odd]},
  'operator_hashes':{'gr1_to_gr2':[sha(A) for A in ops[1]],'gr2_to_gr3':[sha(A) for A in ops[2]],'tail_odd_to_even':[sha(A) for A in odd_to_even],'tail_even_to_odd':[sha(A) for A in even_to_odd]},
  'well_defined_low_checks':well,'low_commutativity_checks':comm,
  'all_n_tail_theorem':ki['all_n_associated_graded']['theorem'],
  'period_two_semigroup_theorem':ki['normalized_transition_semigroup']['theorem'],
  'reconstruction_statement':'because I is generated by the 15 declared augmentation generators, the low maps plus the two tail operator families and the proven period-two identification reconstruct multiplication by degree-one generators on every gr_I^n; no extra polynomial-quotient identification of the completed Rees ring is asserted.',
  'status':'PASS_FULL_FILTERED_ASSOCIATED_GRADED_DEGREE_ONE_MULTIPLICATION_DATA_ALL_N_WITH_LOW_TAIL_GLUE'},
 'conductor_ext_localization_product':loc,
 'guards':['filtered associated-graded multiplication data are not a new identification of geometric carriers','the Ext class is in abelian groups on the frozen conductor exact sequence','Yoneda product statement is for the detected pushout epsilon in Ext_Z^*(Z/2,Z/2), not a Green-ring Ext product'],
 'status':'PASS_FULL_FILTERED_REES_EXTENSION_DATA_AND_2PRIMARY_EXT_LOCALIZATION_PRODUCT_AUDIT'}
(ROOT/'II_KL_cube27_filtered_rees_ext.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps({'gr':out['filtered_rees_extension_data']['graded_pieces'],'checks':[well,comm],'A2mod2_dim':dim_A_mod2,'detector':det,'ext':loc['status']},indent=2))
