#!/usr/bin/env python3
import json
from pathlib import Path
from collections import Counter
ROOT=Path(__file__).resolve().parent;DEP=ROOT/'dependencies'
prev=json.load(open(DEP/'master_status_registry_II_KK.json')); pm_prev=json.load(open(DEP/'master_merge_registry_II_KK.json'))
rows=[]
def add(st,n,dom,sub,reason):rows.append({'id':f'{st}-KL-{n:02d}','status':st,'domain':dom,'subject':sub,'reason':reason})
pass_rows=[
('Cube27','all-n filtered associated graded','low maps plus period-two tail serialize multiplication by 15 augmentation generators on every graded degree'),
('Cube27','low/tail Rees glue','gr3 is the exact odd tail entry and tail operator hashes match the KJ authority'),
('Cube27','A2 mod 2 detector','A2/2A2 has dimension 13 and an explicit F2 functional detects the Yoneda class'),
('Cube27','2-local Ext survival','the nonzero class survives localization at 2'),
('Cube27','away-from-2 Ext vanishing','the 2-primary class dies after inverting 2 and at odd localizations'),
('Cube27','detected Yoneda product audit','pushout epsilon is nonzero in Ext1_Z(Z2,Z2) and epsilon squared vanishes in Ext2 by projective dimension one'),
('Gauss','seventh transfer trace','7^7 inverse-branch words plus positive continuant tail give an Arb enclosure'),
('Gauss','seventh Fredholm coefficient','Newton identity combines certified traces/coefficient intervals through d6 with trL7'),
('Gauss','reduced resolvent existence','simple isolated leading eigenvalue and Riesz projector imply bounded inverse on the complementary spectral subspace'),
('Gauss','third Riesz-pressure identity','the exact reduced-resolvent formula defines lambda3 and P third derivative on the analytic perturbation carrier'),
('Codimension-3','sqrt5/4 crossing refinement','one additional 192-bit Arb interval-Newton contraction succeeds'),
('Codimension-3','pi/6 crossing refinement','one additional 192-bit Arb interval-Newton contraction succeeds'),
('Codimension-3','regular germinal holonomy atlas','seven axis-start regular levels carry interval-certified H_c=R_u S_0 T involutive germs'),
('Codimension-3','source-bound bad-stratum atlas','retrieved Epstein-Vogt support gives C8 with alternating four S3/four T2 pieces and shared-circle incidence'),
('Golden-Hodge','E8 subgroup census type4','sixteen elementary abelian order-eight subgroups are enumerated on the actual type4 order32 stabilizer'),
('Golden-Hodge','joint E8 B5 detection','six independent actual B5 blocks and native product restrictions give 34 candidate pivots after 196608 rows'),
('Golden-Hodge','second native H5 closure','type4 native product span reaches the independent H5 dimension 34'),
('Recurrence','FLINT factor engine upgrade','python-flint nmod_poly/fmpz engine replaces the resource-heavy SymPy route for high-degree tap-pair factorization'),
('Recurrence','order89 engine qualification','all nine old selected order89 certificates match the new FLINT full-sweep values'),
('Recurrence','full order89 census','all 88 tap values are factorized exactly in the upgraded engine'),
('Recurrence','full orders96-105 census','all 995 tap values for k=96..105 are factorized exactly'),
('Recurrence','reflection theorem validation','124/124 applicable even-k odd-v reflection pairs pass on k=96,98,100,102,104'),
('Recurrence','fixed-center theorem validation','five new centers satisfy ord(C)=4k and h_anti=2k'),
('Recurrence','collision quotient','237 collision classes involving repaired/new pairs are serialized, including 68 cross-order classes'),
('Recurrence','divisibility atlas','k|ord, v|ord and (k+v)|ord strata are tabulated with fixed-center ratio4 preserved'),
('D5','post-A1BI retrieval audit','fresh Library/GitHub scopes are audited against the explicit continuous rank3 transition ABI'),
('Pisano-Theta','historical p5 retrieval audit','fresh source scan preserves the exact missing additive-character/Haar/Tate byte schema'),
('Project oracle','Stone/Fibonacci ABI preflight','fresh exact-field searches preserve zero complete packets, zero promotions and 37 active gates')]
for i,(d,s,r) in enumerate(pass_rows,1):add('PASS',i,d,s,r)
add('ZERO',1,'Recurrence','new odd-order global antiperiod sectors','full order89 and full odd orders97,99,101,103,105 remain ZERO by the determinant theorem')
sep_rows=[
('Gauss','absolute three-point cumulant summability','reduced-resolvent existence alone does not prove an absolutely summable time-domain three-point cumulant series'),
('Gauss','numerical third pressure response','no certified reduced-resolvent operator norm or numerical S u1/S u2 evaluation is available'),
('Codimension-3','cross-singular quotient atlas','no source-bound map glues the regular germ atlas to the true C8 bad-stratum leaf quotient'),
('Codimension-3','compactified germinal leaf groupoid','actual cross-singular holonomy transition bytes are still absent'),
('Golden-Hodge','free Wall degree4 producer','free basis, equivariant d4, twisting cochain and Phi4 bytes remain absent'),
('Golden-Hodge','remaining native H5 types','types0,1,3,5,6 are not extrapolated from the new type4 closure'),
('Recurrence','universal divisibility law beyond fixed center','exact atlas shows multiple strata; no single linear order/value law is promoted'),
('Pisano-Theta','historical p5 full Tate packet','historical additive character, self-dual Haar, denominator and representative bytes remain unrecovered')]
for i,(d,s,r) in enumerate(sep_rows,1):add('SEPARATED',i,d,s,r)
add('REFUTED',1,'Recurrence','engine-independent order89 resource obstruction','the old SymPy bounded-window overrun is not invariant: the FLINT engine completes all 88 taps and matches all nine prior probes')
nt_rows=[
('D5','continuous rank3 project transition packet','no A1BI-or-later or independent complete transition packet recovered'),
('Stone','project lambdaTheta/integer value','five decisive project fields remain absent'),
('Fibonacci','project same-carrier value','carrier/U/cofinal-basis/trace-table instance remains absent')]
for i,(d,s,r) in enumerate(nt_rows,1):add('NT',i,d,s,r)
c=Counter(r['status'] for r in rows);counts=dict(prev['counts'])
for k,v in c.items():counts[k]=counts.get(k,0)+v
status={'phase':'II-KL','predecessor':'II-KK','inherited_counts':prev['counts'],'append_rows':rows,'counts':counts,'active_project_NT_count':37,'note':'append-only truth/status axis; mergeability remains separate'}
(ROOT/'master_status_registry_II_KL.json').write_text(json.dumps(status,indent=2,sort_keys=True)+'\n')
# merge axis
mr=[]
def m(st,n,src,tgt,why):mr.append({'id':f'{"PM" if st=="PROVEN-MERGEABLE" else "PNM"}-KL-{n:02d}','merge_status':st,'source_carrier':src,'target_carrier':tgt,'adapter_or_obstruction':why})
pm=[
('low augmentation maps','all-n associated graded','exact gr3 tail glue plus period-two semigroup'),('conductor Yoneda class','2-local Ext class','localization at 2 preserves the finite 2-primary quotient'),('A2/2A2 class','Ext1(Z2,Z2) pushout','explicit F2 detector functional'),('Gauss traces1-7','Fredholm d7','Newton identity on the same trace-class carrier'),('Gauss Riesz projector/gap','reduced resolvent S','spectral complementary inverse via Riesz decomposition'),('regular return formula','seven interval germ records','same axis-start transverse carrier and Arb integration'),('Epstein-Vogt bad-set support','C8 stratum atlas','source-bound alternating incidence'),('native Golden products','type4 H5 closure','direct-sum E8 restrictions with actual B5 blocks'),('old selected order89 records','full FLINT order89 census','9/9 exact matrix-order/antiperiod qualification'),('FLINT factor ABI','full orders96-105 atlas','same characteristic polynomial and root-order semantics'),('matrix-order equality','collision quotient','exact finite equivalence relation'),('historical ABI schemas','current D5/Pisano/Stone/Fib preflight','same required-field contracts')]
for i,(a,b,cause) in enumerate(pm,1):m('PROVEN-MERGEABLE',i,a,b,cause)
pnm=[
('2-primary conductor class','odd-prime localization','class is annihilated after inverting 2'),('pairwise Gauss information','absolute third cumulant series','pairwise data remain insufficient; reduced-resolvent existence is a different channel'),('C8 stratum incidence','actual leaf holonomy groupoid','incidence data do not supply cross-singular holonomy arrows'),('doubled-origin support model','actual Epstein-Vogt leaf space','no homeomorphism/quotient-atlas adapter'),('coinvariant Golden comparison bytes','free F2[H]-Wall degree4 map','coinvariants are nonfaithful and do not reconstruct a free lift'),('old SymPy timeout','mathematical order89 specialness','runtime behavior is engine-dependent evidence, not a carrier invariant'),('A1BH finite lineage','continuous D5 rank3 bundle','no transition/trivialization adapter'),('partial Stone/Fibonacci sources','promoted project values','missing decisive fields block merge')]
for i,(a,b,cause) in enumerate(pnm,1):m('PROVEN-NOT-MERGEABLE',i,a,b,cause)
mc=Counter(r['merge_status'] for r in mr);mcounts=dict(pm_prev['counts'])
for k,v in mc.items():mcounts[k]=mcounts.get(k,0)+v
merge={'phase':'II-KL','predecessor':'II-KK','inherited_counts':pm_prev['counts'],'append_rows':mr,'counts':mcounts}
(ROOT/'master_merge_registry_II_KL.json').write_text(json.dumps(merge,indent=2,sort_keys=True)+'\n')
print(json.dumps({'append_status':dict(c),'counts':counts,'append_merge':dict(mc),'merge_counts':mcounts},indent=2))
