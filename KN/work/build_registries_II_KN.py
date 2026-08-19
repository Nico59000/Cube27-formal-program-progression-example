#!/usr/bin/env python3
from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
D=R/'dependencies'
PH='II-KN'
old=json.loads((D/'master_status_registry_II_KM.json').read_text())
oldm=json.loads((D/'master_merge_registry_II_KM.json').read_text())
assert old['counts']=={'PASS':1457,'ZERO':100,'SEPARATED':460,'REFUTED':295,'NT':90}
assert oldm['counts']=={'PROVEN-MERGEABLE':687,'PROVEN-NOT-MERGEABLE':464}

def s(i,status,domain,subject,reason):
    return {'id':i,'status':status,'domain':domain,'subject':subject,'reason':reason,'source_phase':PH,'last_reassessment':PH,'tier':'head'}
rows=[
 s('PASS-KN-01','PASS','Cube27','Z_(2)-torsion-freeness of every completed augmentation power','Noetherian completion is flat over R_(2); finite I^n complete by tensoring and inject into the torsion-free completed order'),
 s('PASS-KN-02','PASS','Cube27','all-stage completed filtration non-splitting theorem','every quotient gr^n contains nonzero 2-primary torsion whereas the completed middle term is Z_(2)-torsion-free'),
 s('PASS-KN-03','PASS','Cube27','complete separated inverse-limit topological algebra presentation','Rhat_(2)=lim R_(2)/I^m_(2) is the exact I-adic topological-algebra presentation on the frozen carrier'),
 s('REF-KN-01','REFUTED','Cube27','completed filtration exact sequence splits as a Z_(2)-module','a section would inject nonzero finite 2-torsion into a torsion-free completed augmentation module'),
 s('REF-KN-02','REFUTED','Cube27','period-two associated graded yields a split product presentation of the completed Rees algebra','associated-graded periodicity does not erase the proven nonzero filtered extension classes'),
 s('SEP-KN-01','SEPARATED','Cube27','explicit polynomial generators/relations for the completed topological algebra','inverse-limit presentation is exact, but no source-bound convergent polynomial presentation has been serialized'),

 s('PASS-KN-04','PASS','Gauss','ninth Fredholm trace enclosure','10,077,696 exact branch words with rigorous positive complement majorant give the certified tr(L^9) interval'),
 s('PASS-KN-05','PASS','Gauss','ninth Fredholm coefficient d9','Newton identity applied to certified trace/coefficient intervals gives a proof-grade enclosure crossing zero'),
 s('PASS-KN-06','PASS','Gauss','source-bound leading-eigenvalue resolvent contour','Nisoli primary-source certification gives sup_Gamma1 ||(zI-L)^-1|| <= 4.25e2 on H^2(D1)'),
 s('PASS-KN-07','PASS','Gauss','quantitative reduced-resolvent norm on H^2(D1)','the Laurent regular-part contour identity gives ||S_H|| <= sup_Gamma1 ||R(z)|| <= 425 without normality'),
 s('SEP-KN-02','SEPARATED','Gauss','weighted-branch reduced-resolvent operator norm','AB/BA transports nonzero spectrum/Riesz data but does not by itself preserve the H^2 operator norm'),
 s('SEP-KN-03','SEPARATED','Gauss','proof-grade numerical third-pressure P third derivative','the exact Riesz identity and resolvent norm do not yet evaluate S on the perturbative vectors u1,u2 with certified weighted norms'),

 s('PASS-KN-08','PASS','Golden','type5/order32 elementary-abelian E8 restriction census','29 actual E8 subgroups are enumerated from the native type5 multiplication table'),
 s('PASS-KN-09','PASS','Golden','type5 native H5/B5 product-span rank','17 actual E8 restriction/coboundary blocks process 557056 rows and raise the quotient candidate rank to the independent upper bound 56'),
 s('PASS-KN-10','PASS','Golden','fourth independent native H5 closure','type5 closes at dim H5=56 from its own bytes, after the previously independent type2,type4,type3 closures'),
 s('SEP-KN-04','SEPARATED','Golden','free F2[H]-Wall degree-four producer','native/coinvariant restriction closure does not manufacture the missing equivariant free basis,d4,twisting and free Phi lifts'),

 s('PASS-KN-11','PASS','Recurrence','full FLINT orders 116--125','all 1195 tap-pair polynomials are factorized exactly after 15/15 qualification against frozen records'),
 s('PASS-KN-12','PASS','Recurrence','five new fixed-reflection centers','k=116,118,120,122,124 at v=k/2 satisfy ordC=4k and global antiperiod h=2k'),
 s('PASS-KN-13','PASS','Recurrence','general polynomial dilation-order theorem','for monic f over F_p with f(0)!=0, ord(f(x^d))=d ord(f), proved using prime-to-p root orbit, p-power multiplicity, and injective substitution'),
 s('PASS-KN-14','PASS','Recurrence','tap-pair dilation theorem','f_{dk,dv}(x)=f_{k,v}(x^d) gives ord C(dk,dv)=d ord C(k,v)'),
 s('PASS-KN-15','PASS','Recurrence','primitive-ray reduction and divisibility law','with g=gcd(k,v), ordC(k,v)=g ordC(k/g,v/g), so g divides every matrix order'),
 s('PASS-KN-16','PASS','Recurrence','full exact theorem qualification through order125','7750 primitive-reduction checks and 12217 divisor-scaling checks on full orders2--125 have zero violations'),
 s('PASS-KN-17','PASS','Recurrence','45--125 collision/divisibility stratification','6804 exact main-atlas records give 1354 matrix-order collision classes, 351 cross-order, with normalized primitive-ray invariants serialized'),
 s('PASS-KN-18','PASS','Recurrence','equal-order reflection theorem extension through 125','the inherited even-k odd-v reflection law remains exact on all applicable 45--125 pairs and is compatible with the dilation stratification'),
 s('ZERO-KN-01','ZERO','Recurrence','odd-order global-antiperiod sector for new full orders','orders117,119,121,123,125 have zero global-antiperiod families, consistent with the determinant obstruction'),
 s('ZERO-KN-02','ZERO','Recurrence','new linear formula hits ordC=k or ordC=k+v','the full 116--125 records contain no such equality hits'),

 s('PASS-KN-19','PASS','SourceAudit','fresh codim3/D5/p5/Stone/Fibonacci scoped ingestion audit','Library/current-input and connected-repository searches are replayed with zero-hit scope guards and exact required-field lists'),
 s('SEP-KN-05','SEPARATED','Codimension3','actual compactified cross-singular leaf groupoid','no source-bound cross-singular arrow/topology/composition packet was recovered'),
 s('SEP-KN-06','SEPARATED','Codimension3','compactified leaf-groupoid holonomy cocycle','without the actual cross-singular arrow carrier there is no project cocycle domain on which to certify composition/gauge laws'),
 s('PASS-KN-20','PASS','D5','fresh post-A1BJ/A1BK source retrieval attempt','declared Library/current-input/GitHub scope was searched against the frozen rank3 transition ABI'),
 s('NT-KN-01','NT','D5','continuous rank3 D5 transition bundle','base, cover, local trivializations, continuous gij, Cech laws and metric/norm transport provenance remain unrecovered'),
 s('PASS-KN-21','PASS','Pisano','fresh historical p5 local Tate packet retrieval attempt','the stored sign/residue lineage and current scopes were re-audited against the exact six-field local normalization ABI'),
 s('SEP-KN-07','SEPARATED','Pisano','historical p5 additive-character/self-dual-Haar/Tate packet','psi5 bytes, Haar convention, conductor/different denominator, uniformizer coordinates and finite sum bytes remain absent'),
 s('PASS-KN-22','PASS','ProjectABI','fresh Stone/Fibonacci ABI-completeness preflight','the exact same-carrier decisive fields are checked before any value promotion; complete packet count remains zero'),
 s('NT-KN-02','NT','Stone','actual project lambdaTheta/integer value','project d,theta,K_Z,C,residue/framing and secondary-chain provenance remain absent'),
 s('NT-KN-03','NT','Fibonacci','actual same-carrier project support/complement value','instantiated carrier, localization/cofinal basis and decisive trace table or trace-zero witness remain absent'),
]
counts=dict(old['counts'])
for r in rows: counts[r['status']]+=1
out={'phase':PH,'predecessor':'II-KM','inherited_counts':old['counts'],'append_rows':rows,'counts':counts,'active_project_NT_count':37,'note':'append-only truth axis; active project-gate count is distinct from raw NT ledger count'}
(R/'master_status_registry_II_KN.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')

def m(i,status,src,tgt,why):
 return {'id':i,'merge_status':status,'source_carrier':src,'target_carrier':tgt,'adapter_or_obstruction':why,'source_phase':PH}
mrows=[
 m('PM-KN-01','PROVEN-MERGEABLE','finite I^n_(2) modules','their I-adic completions','Noetherian finite-module completion/tensor identification and flatness'),
 m('PM-KN-02','PROVEN-MERGEABLE','certified H^2(D1) resolvent contour','H^2(D1) reduced resolvent','Laurent regular-part contour integral at the isolated simple eigenvalue'),
 m('PM-KN-03','PROVEN-MERGEABLE','type5 native cocycles and E8 restrictions','type5 native H5 quotient','actual subgroup restriction plus actual B5 block quotient rank'),
 m('PM-KN-04','PROVEN-MERGEABLE','polynomial substitution f(y)->f(x^d)','companion matrix order','minimal-polynomial order equals least N with f|x^N-1'),
 m('PM-KN-05','PROVEN-MERGEABLE','nonprimitive tap pair (k,v)','primitive ray (k/g,v/g) plus scale g','exact dilation theorem with g=gcd(k,v)'),
 m('PM-KN-06','PROVEN-MERGEABLE','orders116--125 exact FLINT records','45--125 collision atlas','same recurrence ABI and exact factor/order schema'),
 m('PM-KN-07','PROVEN-MERGEABLE','source requirement ledgers','fresh scoped retrieval audit','typed missing-field ABI is reused without changing project semantics'),
 m('PM-KN-08','PROVEN-MERGEABLE','II-KM exact completion sequences','II-KN non-splitting decision','torsion-free middle-term theorem decides the previously separated splitting question'),

 m('PNM-KN-01','PROVEN-NOT-MERGEABLE','period-two associated graded','split completed Rees/topological product','proven torsion obstruction forbids stagewise sections'),
 m('PNM-KN-02','PROVEN-NOT-MERGEABLE','conductor Ext^1 class','completed augmentation-filtration extension classes','different exact sequences and carriers; no identification is used'),
 m('PNM-KN-03','PROVEN-NOT-MERGEABLE','H^2(D1) reduced-resolvent norm','weighted-branch reduced-resolvent norm','AB/BA spectral transport is not an isometric norm adapter'),
 m('PNM-KN-04','PROVEN-NOT-MERGEABLE','alternating C8 bad-stratum incidence','actual compactified leaf groupoid','incidence/local links omit cross-singular arrows and topology'),
 m('PNM-KN-05','PROVEN-NOT-MERGEABLE','native Golden H5 closure','free F2[H]-Wall degree4 producer','coinvariant/native cocycles do not determine equivariant free lifts'),
 m('PNM-KN-06','PROVEN-NOT-MERGEABLE','historical p5 sign/residue shadow','full p5 local Tate normalization packet','sign does not determine additive-character scale,Haar,denominator or coordinates'),
 m('PNM-KN-07','PROVEN-NOT-MERGEABLE','partial Stone/Fibonacci source objects','promoted project values','same-carrier ABI decisive fields remain absent'),
 m('PNM-KN-08','PROVEN-NOT-MERGEABLE','recurrence primitive-ray/order strata','Golden/Cube27/D5/Stone/Fibonacci carriers','arithmetic coincidences provide no typed cross-carrier adapter'),
]
mc=dict(oldm['counts'])
for r in mrows: mc[r['merge_status']]+=1
mout={'phase':PH,'predecessor':'II-KM','inherited_counts':oldm['counts'],'append_rows':mrows,'counts':mc,'note':'mergeability axis remains orthogonal to PASS/ZERO/SEPARATED/REFUTED/NT'}
(R/'master_merge_registry_II_KN.json').write_text(json.dumps(mout,indent=2,sort_keys=True)+'\n')
print(json.dumps({'status_counts':counts,'merge_counts':mc,'status_append':len(rows),'merge_append':len(mrows)},indent=2))
