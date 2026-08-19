#!/usr/bin/env python3
import json
from pathlib import Path
from collections import Counter
ROOT=Path('/mnt/data/II_KM')
PRE=Path('/mnt/data/II_KM_predecessor/II_KL_bundle')
prev=json.load(open(PRE/'master_status_registry_II_KL.json'))
pm_prev=json.load(open(PRE/'master_merge_registry_II_KL.json'))
rows=[]
def add(st,n,dom,sub,reason): rows.append({'id':f'{st}-KM-{n:02d}','status':st,'domain':dom,'subject':sub,'reason':reason,'source_phase':'II-KM','last_reassessment':'II-KM','tier':'head'})
pass_rows=[
('Cube27','2-local associated-graded primary decomposition','actual Smith forms localize 12 to 4 and give exact gr1/gr2/all-tail primary modules'),
('Cube27','2-step module filtration 0<2M<M','the mod-2 and 2M dimensions are recomputed on gr1, gr2 and the all-n tail'),
('Cube27','augmentation-operator filtration preservation','all 60 integer-linear degree-one multiplication operators preserve 2M functorially'),
('Cube27','2-local Noetherian input','the declared rank-16 integral Green algebra is module-finite over Z; localization at 2 is Noetherian'),
('Cube27','I-adic completion exactness on finite filtered steps','Noetherian completion exactness applies to every 0->I^(n+1)->I^n->gr^n->0 over R_(2)'),
('Cube27','2-local conductor Ext filtration/detector','the 13-dimensional mod-2 detector keeps the nonzero conductor class at 2 and kills it away from 2'),
('Gauss','eighth transfer trace','6^8 exact branch words grouped by matrix trace plus a positive conservative continuant tail give a 192-bit enclosure'),
('Gauss','eighth Fredholm coefficient','Newton identity combines the frozen d1..d7/trace intervals with the new trace L^8 enclosure'),
('Codimension-3','sqrt5/4 256-bit crossing refinement','higher-resolution Arb interval-Newton contracts the inherited unique regular crossing strictly'),
('Codimension-3','pi/6 256-bit crossing refinement','higher-resolution Arb interval-Newton contracts the inherited unique regular crossing strictly'),
('Codimension-3','higher-resolution regular return campaign','both refined intervals have strictly negative derivative enclosures on the declared regular carrier'),
('Golden-Hodge','type3 E8 subgroup census','29 elementary-abelian E8 subgroups are enumerated on the actual type3 order32 stabilizer'),
('Golden-Hodge','type3 joint B5 restriction detection','17 independent actual B5 blocks and native product restrictions reach 56 candidate pivots after 557056 rows'),
('Golden-Hodge','third native H5 closure','type3 displayed native products attain the independent H5 dimension 56'),
('Recurrence','full repair orders91/93/95','all 276 formerly selected odd-order tap pairs are now factor-certified exactly by FLINT'),
('Recurrence','full orders106-115 census','all 1095 tap-pair families are factor-certified exactly'),
('Recurrence','full exact atlas45-115','all 5609 pairs (k,v), 45<=k<=115 and 1<=v<k, are present exactly once'),
('Recurrence','general reflection equal-order collision theorem','determinant parity sharpens C_ref~-C^-1 to ord C(k,k-v)=ord C(k,v) for every even k and odd v'),
('Recurrence','reflection theorem full-atlas replay','all 691 unordered applicable reflection pairs in the full 45-115 atlas have equal exact matrix order'),
('Recurrence','fixed-center divisibility refinement','all 35 even fixed centers satisfy ordC=4k, hanti=2k, gcd(ordC,k+v)=k/2 and (k+v) does not divide ordC'),
('Recurrence','full collision quotient45-115','1130 equal-order collision classes are serialized, including 297 cross-order classes'),
('Recurrence','full divisibility census45-115','exact counts k|ord=621, v|ord=1311, (k+v)|ord=494 are serialized on 5609 records'),
('D5','post-A1BI/A1BJ retrieval audit','fresh Library and connected-repository scopes are checked against the complete continuous rank3 ABI'),
('Pisano-Theta','historical p5 retrieval audit','fresh scopes are checked against the explicit additive-character/Haar/conductor/uniformizer/Tate ABI'),
('Project oracle','Stone/Fibonacci ABI preflight','fresh exact-field preflight preserves zero complete actual packets, zero promotions and 37 active gates')]
for i,(d,s,r) in enumerate(pass_rows,1): add('PASS',i,d,s,r)
zero_rows=[
('Recurrence','odd-order global antiperiod sector on full 45-115 atlas','no odd k record has a global antiperiod; determinant obstruction and full replay agree'),
('Recurrence','ordC equals k on full 45-115 atlas','no exact record in the declared full finite atlas satisfies ordC=k'),
('Recurrence','ordC equals k+v on full 45-115 atlas','no exact record in the declared full finite atlas satisfies ordC=k+v')]
for i,(d,s,r) in enumerate(zero_rows,1): add('ZERO',i,d,s,r)
sep_rows=[
('Cube27','split/product presentation of completed Rees','exact completion of filtration sequences does not supply compatible splittings'),
('Cube27','new polynomial quotient presentation of completed Rees','associated-graded periodicity alone does not determine a polynomial presentation of the completion'),
('Gauss','certified numerical reduced-resolvent norm','existence of the bounded reduced resolvent does not provide a proof-grade numerical norm'),
('Gauss','proof-grade numerical third pressure','no certified numerical P third derivative enclosure is produced'),
('Gauss','absolute time-domain three-point cumulant summability','the Fredholm calculation is a distinct evidence channel and does not close absolute three-point summability'),
('Codimension-3','cross-singular quotient/holonomy source','no source-bound transition arrows glue the regular germs across the C8 bad stratum'),
('Codimension-3','actual compactified leaf groupoid','sharper regular-root localization does not identify the source-bound singular quotient groupoid'),
('Golden-Hodge','trusted free F2[H]-Wall degree4 producer','free basis, equivariant d4, twisting data, free Phi3 and Phi4 remain absent'),
('Golden-Hodge','remaining native H5 types0,1,5,6','type3 closure is not transferred or extrapolated to other stabilizer carriers'),
('Pisano-Theta','historical p5 full local Tate packet','explicit additive-character/Haar/conductor/uniformizer/Tate bytes remain unrecovered')]
for i,(d,s,r) in enumerate(sep_rows,1): add('SEPARATED',i,d,s,r)
add('REFUTED',1,'Cube27','period-two associated graded implies period-two filtered/completed splitting','extension data can vary while associated graded repeats; no compatible splitting has been serialized')
nt_rows=[
('D5','continuous rank3 project transition packet','no post-A1BI/A1BJ or independent complete transition packet is recovered in the declared scopes'),
('Stone','actual project lambdaTheta/integer value','project d, theta, K_Z, C and framing/residue provenance remain absent'),
('Fibonacci','actual same-carrier project value','carrier/localization/cofinal-basis/trace-table decisive packet remains absent')]
for i,(d,s,r) in enumerate(nt_rows,1): add('NT',i,d,s,r)
c=Counter(r['status'] for r in rows); counts=dict(prev['counts'])
for k,v in c.items(): counts[k]=counts.get(k,0)+v
status={'phase':'II-KM','predecessor':'II-KL','inherited_counts':prev['counts'],'append_rows':rows,'counts':counts,'active_project_NT_count':37,'note':'append-only truth/status axis; mergeability remains separate; ZERO rows are scoped to the declared full finite recurrence atlas where stated'}
(ROOT/'master_status_registry_II_KM.json').write_text(json.dumps(status,indent=2,sort_keys=True)+'\n')
mr=[]
def m(st,n,src,tgt,why): mr.append({'id':f'{"PM" if st=="PROVEN-MERGEABLE" else "PNM"}-KM-{n:02d}','merge_status':st,'source_carrier':src,'target_carrier':tgt,'adapter_or_obstruction':why,'source_phase':'II-KM'})
pm=[
('integral Cube27 Smith data','2-local primary graded modules','localization at (2) and 2-primary Smith reduction'),
('finite Cube27 filtered steps','their I-adic completions','Noetherian exact completion theorem on finite R_(2)-modules'),
('conductor Ext class','2-local conductor Ext class','2-primary localization preserves the explicit detector'),
('Gauss traces1-8','Fredholm d8','Newton identity on the same trace-class carrier'),
('II-KL regular crossings','II-KM sharper crossings','same axis-start return function and nested Arb interval-Newton enclosure'),
('native Golden type3 products','type3 H5 quotient','direct-sum E8 restrictions modulo actual independent B5 blocks'),
('selected recurrence 91/93/95','full repaired scans','same FLINT factor/order ABI and exact tap identifiers'),
('predecessor recurrence atlases45-105','full recurrence atlas45-115','disjoint exact (k,v) keys plus repaired odd-order replacements'),
('reflection polynomial involution','equal-order collision quotient','explicit similarity to -C^-1 plus determinant parity theorem'),
('fixed-center recurrence theorem','divisibility corollary','ordC=4k and v=k/2 imply the gcd/divisibility identities'),
('matrix-order equality records','collision quotient classes','exact equality equivalence relation on one recurrence carrier'),
('historical ABI contracts','II-KM source preflight','same exact required-field schemas for D5/Pisano/Stone/Fibonacci')]
for i,(a,b,cause) in enumerate(pm,1): m('PROVEN-MERGEABLE',i,a,b,cause)
pnm=[
('associated-graded period-two tail','split filtered/completed Rees algebra','missing extension/splitting data block the merge'),
('abstract reduced resolvent existence','numerical resolvent norm','bounded existence does not provide a quantitative norm certificate'),
('Fredholm trace coefficients','absolute time-domain third cumulant summability','distinct analytic evidence channels without a summability adapter'),
('regular codim3 Arb germs','cross-singular leaf groupoid','missing source-bound holonomy transitions'),
('type3 native H5 closure','remaining Golden stabilizer H5 carriers','no restriction-rank transport or carrier identification'),
('coinvariant/native Golden bytes','free F2[H]-Wall degree4 producer','free equivariant lift data are absent'),
('historical p5 sign/shadow','full local Tate packet','sign does not determine additive character/Haar/coordinates'),
('partial Stone/Fibonacci source objects','promoted project values','decisive same-carrier ABI fields remain absent')]
for i,(a,b,cause) in enumerate(pnm,1): m('PROVEN-NOT-MERGEABLE',i,a,b,cause)
mc=Counter(r['merge_status'] for r in mr); mcounts=dict(pm_prev['counts'])
for k,v in mc.items(): mcounts[k]=mcounts.get(k,0)+v
merge={'phase':'II-KM','predecessor':'II-KL','inherited_counts':pm_prev['counts'],'append_rows':mr,'counts':mcounts,'note':'mergeability axis independent from truth-status axis'}
(ROOT/'master_merge_registry_II_KM.json').write_text(json.dumps(merge,indent=2,sort_keys=True)+'\n')
print(json.dumps({'append_status':dict(c),'counts':counts,'append_merge':dict(mc),'merge_counts':mcounts},indent=2,sort_keys=True))
