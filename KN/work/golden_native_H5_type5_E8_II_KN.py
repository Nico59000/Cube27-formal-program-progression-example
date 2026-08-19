#!/usr/bin/env python3
from __future__ import annotations
import itertools,numpy as np,json,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; DEP=ROOT/'dependencies'/'golden'
JY=json.load(open(DEP/'II_JY_golden_native_raw_all.json'));JZ=json.load(open(DEP/'II_JZ_golden_residual_H3.json'));H5=json.load(open(DEP/'II_KG_golden_H5_entry.json'))

def rank_mod(A,p=2):
 A=np.array(A,dtype=np.int64)%p
 if A.size==0:return 0
 r=0;m,n=A.shape
 for c in range(n):
  q=next((i for i in range(r,m) if A[i,c]%p),None)
  if q is None:continue
  A[[r,q]]=A[[q,r]]
  for i in range(m):
   if i!=r and A[i,c]%p:A[i]^=A[r]
  r+=1
 return r

def inv2(M):
 n=M.shape[0];X=np.concatenate([M.copy()%2,np.eye(n,dtype=np.uint8)],axis=1);r=0
 for c in range(n):
  q=next(i for i in range(r,n) if X[i,c]);X[[r,q]]=X[[q,r]]
  for i in range(n):
   if i!=r and X[i,c]:X[i]^=X[r]
  r+=1
 return X[:,n:]%2
I3=np.eye(3,dtype=np.uint8);I6=np.eye(6,dtype=np.uint8);GL=[]
for bits0 in itertools.product([0,1],repeat=9):
 M=np.array(bits0,dtype=np.uint8).reshape(3,3)
 if rank_mod(M)==3:GL.append(M)
O3=[M for M in GL if np.array_equal((M.T@M)%2,I3)]
inds=[(0,0),(0,1),(0,2),(1,1),(1,2),(2,2)];SY=[]
for bits0 in itertools.product([0,1],repeat=6):
 S=np.zeros((3,3),dtype=np.uint8)
 for bit0,(i,j) in zip(bits0,inds):S[i,j]=S[j,i]=bit0
 SY.append(S)
CENT=[np.block([[M,(M@S)%2],[np.zeros((3,3),dtype=np.uint8),M]])%2 for M in O3 for S in SY];CINV=[inv2(M) for M in CENT]
V6=[tuple(v) for v in itertools.product([0,1],repeat=6)]
def qval(v,p,r):
 a=np.array(v[:3],dtype=np.uint8);b=np.array(v[3:],dtype=np.uint8);return int((a@b+np.array(p,dtype=np.uint8)@a+np.array(r,dtype=np.uint8)@b)%2)
params=[(p,r) for p in itertools.product([0,1],repeat=3) for r in itertools.product([0,1],repeat=3)];ftop={tuple(qval(v,p,r) for v in V6):(p,r) for p,r in params}
def qact(pr,Mi):return ftop[tuple(qval(tuple(((Mi@np.array(v,dtype=np.uint8))%2).tolist()),*pr) for v in V6)]
def arf(pr):return sum(pr[0][i]*pr[1][i] for i in range(3))%2
un=set(params);orbs=[]
while un:
 pr=min(un);o={qact(pr,M) for M in CINV};orbs.append(o);un-=o
ORBS=sorted(orbs,key=lambda x:(len(x),arf(min(x))))
def mkey(M):return bytes(M.reshape(-1).tolist())
def raw(rec):return bytes.fromhex(rec['raw_hex'])
def bit(data,idx):return (data[idx>>3]>>(idx&7))&1
def bits_int(mask):
 while mask:
  lb=mask&-mask;yield lb.bit_length()-1;mask^=lb
def closure(tbl,e,gens):
 S={e};front=[e]
 while front:
  a=front.pop()
  for g in gens:
   b=tbl[a][g]
   if b not in S:S.add(b);front.append(b)
 return frozenset(S)
def span_rank_int(vectors):
 piv={}
 for x in vectors:
  y=x
  while y:
   p=y.bit_length()-1
   if p in piv:y^=piv[p]
   else:piv[p]=y;break
 return len(piv)
# type5 order32
t0=time.time();ti=5;pr=min(ORBS[ti]);G=[M for M in CINV if qact(pr,M)==pr];q=len(G);assert q==32
idx={mkey(M):i for i,M in enumerate(G)};e=idx[mkey(I6)];tbl=[[idx[mkey((A@B)%2)] for B in G] for A in G]
inv=[i for i in range(q) if i!=e and tbl[i][i]==e]
subs=set()
for a,b,c in itertools.combinations(inv,3):
 if tbl[a][b]!=tbl[b][a] or tbl[a][c]!=tbl[c][a] or tbl[b][c]!=tbl[c][b]:continue
 S=closure(tbl,e,[a,b,c])
 if len(S)==8 and all(tbl[x][x]==e for x in S):subs.add(S)
subs=sorted(subs,key=lambda s:tuple(sorted(s)));print('E8 subgroups',len(subs),flush=True)
rec=JY['records'][ti];zrec=JZ['records'][ti]
H1=[raw(x) for x in rec['native_H1_representatives']];H2=[raw(x) for x in rec['native_H2_basis']];SQ=[raw(x) for x in rec['native_Sq1_H3_representatives']];RES=[raw(x) for x in zrec['records']]
d1,d2=len(H1),len(H2);cubeN=d1**3;ng3=cubeN+len(SQ)+len(RES);target=H5['H5_E2_dimensions'][ti]
nA=d1*d2*d2;nB=d1*d1*ng3;nC=d1*ng3*d1;nD=d2*ng3;nE=ng3*d2;offA=0;offB=nA;offC=offB+nB;offD=offC+nC;offE=offD+nD;nc=offE+nE

def product3(ma,mb,mc,db,dc):
 out=0
 for i in bits_int(ma):
  for j in bits_int(mb):
   for k in bits_int(mc):out |= 1 << ((i*db+j)*dc+k)
 return out
def product2(ma,mb,db):
 out=0
 for i in bits_int(ma):
  for j in bits_int(mb):out |= 1 << (i*db+j)
 return out


# Joint direct-sum restriction quotient rank by one augmented row system.
piv={};cand_piv=0;details=[];rows_total=0;qp=8;q4=qp**4

def idx4(a,b,c,d):return ((a*qp+b)*qp+c)*qp+d
for si,S in enumerate(subs):
 P=sorted(S);pidx={g:i for i,g in enumerate(P)};ptbl=[[pidx[tbl[a][b]] for b in P] for a in P]
 h1=[]
 for aG in P:
  m=0
  for i,x in enumerate(H1):
   if bit(x,aG):m|=1<<i
  h1.append(m)
 h2=[]
 for aG in P:
  for bG in P:
   j=aG*q+bG;m=0
   for i,x in enumerate(H2):
    if bit(x,j):m|=1<<i
   h2.append(m)
 h3=[]
 for ai,aG in enumerate(P):
  ma=h1[ai]
  for bi,bG in enumerate(P):
   mb=h1[bi]
   for ci,cG in enumerate(P):
    mc=h1[ci];mm=product3(ma,mb,mc,d1,d1);idxG=(aG*q+bG)*q+cG
    for j,x in enumerate(SQ):
     if bit(x,idxG):mm|=1<<(cubeN+j)
    for j,x in enumerate(RES):
     if bit(x,idxG):mm|=1<<(cubeN+len(SQ)+j)
    h3.append(mm)
 before=cand_piv; rows_here=0; block_shift=nc+si*q4
 for a in range(qp):
  for b in range(qp):
   ab=ptbl[a][b]
   for c in range(qp):
    bc=ptbl[b][c]
    for d in range(qp):
     cd=ptbl[c][d]
     for ee in range(qp):
      de=ptbl[d][ee]
      dm=(1<<idx4(b,c,d,ee))^(1<<idx4(ab,c,d,ee))^(1<<idx4(a,bc,d,ee))^(1<<idx4(a,b,cd,ee))^(1<<idx4(a,b,c,de))^(1<<idx4(a,b,c,d))
      ma,mb,mc,md,me=h1[a],h1[b],h1[c],h1[d],h1[ee]
      m2ab=h2[a*qp+b];m2bc=h2[b*qp+c];m2de=h2[d*qp+ee]
      m3abc=h3[(a*qp+b)*qp+c];m3bcd=h3[(b*qp+c)*qp+d];m3cde=h3[(c*qp+d)*qp+ee]
      cm=0
      cm |= product3(ma,m2bc,m2de,d2,d2) << offA
      cm |= product3(ma,mb,m3cde,d1,ng3) << offB
      cm |= product3(ma,m3bcd,me,ng3,d1) << offC
      cm |= product2(m2ab,m3cde,ng3) << offD
      cm |= product2(m3abc,m2de,d2) << offE
      row=cm | (dm<<block_shift)
      while row:
       p=row.bit_length()-1
       if p in piv:row^=piv[p]
       else:
        piv[p]=row
        if p<nc:cand_piv+=1
        break
      rows_total+=1;rows_here+=1
 details.append({'subgroup':P,'rows':rows_here,'new_candidate_pivots':cand_piv-before,'joint_candidate_pivots':cand_piv,'total_augmented_rank':len(piv)})
 print('sub',si,'new',cand_piv-before,'joint',cand_piv,flush=True)
 if cand_piv>=target:break
closed=cand_piv>=target
out={'phase':'II-KN','type_index':ti,'group_order':q,'target_native_H5_dimension':target,'elementary_abelian_E8_subgroups_found':len(subs),'subgroups_used':len(details),'candidate_family':{'H1_H2_H2':nA,'H1_H1_H3':nB,'H1_H3_H1':nC,'H2_H3':nD,'H3_H2':nE,'total':nc},'joint_augmented_restriction_certificate':{'candidate_pivots':cand_piv,'rows_processed':rows_total,'subgroups':details},'closure_logic':'the augmented matrix has shared candidate columns and an independent B5 block for each E8 subgroup; candidate-pivot rank is exactly the rank of the direct-sum restriction images modulo direct-sum coboundaries, hence a lower bound for the native product span in H5(G). Reaching the independent abstract H5 dimension closes the product span.','decision':'PASS_TYPE5_ORDER32_NATIVE_H5_PRODUCT_CLOSURE_BY_MULTI_E8_RESTRICTION' if closed else 'SEPARATED_TYPE5_NOT_CLOSED_BY_E8_RESTRICTION','guards':['all subgroup restrictions use actual native H1/H2/H3 bar cocycles','each B5 block is the actual inhomogeneous coboundary C4(E)->C5(E)','no restriction rank is transferred to another stabilizer type','closure uses only image-rank lower bound plus the independent H5 dimension upper bound'],'runtime_seconds':round(time.time()-t0,3),'status':'PASS_FOURTH_NATIVE_H5_B5_CLOSURE_TYPE5' if closed else 'PASS_E8_RESTRICTION_PROGRESS_TYPE5_REMAINS_SEPARATED'}
(ROOT/'II_KN_golden_native_H5_type5.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps({'closed':closed,'used':len(details),'rank':cand_piv,'runtime':out['runtime_seconds']},indent=2))
