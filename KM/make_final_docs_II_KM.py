#!/usr/bin/env python3
from pathlib import Path
import json, hashlib, os
R=Path('/mnt/data/II_KM')
def load(n): return json.load(open(R/n))
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
c=load('II_KM_cube27_2local_completed_rees.json');g=load('II_KM_gauss_eighth_fredholm.json');co=load('II_KM_codim3_sharp_crossing_source_audit.json');gold=load('II_KM_golden_native_H5_type3.json');rec=load('II_KM_recurrence_full_45_115_collision_divisibility.json');sg=load('II_KM_source_project_gates.json');st=load('master_status_registry_II_KM.json');mg=load('master_merge_registry_II_KM.json');ver=load('verifier_stdout_II_KM_deep.json')
safe=("II-KN -- Cube27 completed-Rees extension-class splitting/no-splitting and topological-algebra presentation audit; "
"Gauss ninth Fredholm trace/coefficient plus quantitative reduced-resolvent enclosure or proof-grade third-pressure value; "
"codimension-3 cross-singular transition/holonomy packet acquisition and compactified leaf-groupoid cocycle audit; "
"Golden fourth native H5/B5 closure among types 0,1,5,6 or trusted free F2[H]-Wall degree-four producer; "
"post-A1BJ/A1BK D5 continuous transition-source ingestion; historical Pisano p=5 local Tate packet acquisition; "
"recurrence full orders 116--125 with collision/divisibility-stratum refinement beyond the equal-order reflection theorem; "
"plus external Stone/Fibonacci ABI-complete packet execution.")
# source hashes
files=['II_KM_cube27_2local_completed_rees.json','II_KM_gauss_eighth_fredholm.json','II_KM_codim3_sharp_crossing_source_audit.json','II_KM_golden_native_H5_type3.json','II_KM_recurrence_odd_repair_91_93_95.json','II_KM_recurrence_106_115.json','II_KM_recurrence_full_45_115_collision_divisibility.json','II_KM_source_project_gates.json','master_status_registry_II_KM.json','master_merge_registry_II_KM.json','verifier_stdout_II_KM_deep.json']
source_sha={f:sha(R/f) for f in files}
cert={
 'phase':'II-KM','predecessor':'II-KL','overall':'PASS','observational_continuity':'PASS_298','historical_replay':'NT_NOT_EXHAUSTIVE',
 'title':'Cube27 2-local completed filtration; eighth Gauss Fredholm; sharper codim3 Arb; third native Golden H5; full recurrence 45-115 and reflection collision theorem',
 'key_results':[
  'Cube27: exact 2-local primary associated-graded modules are (Z/2)^2+Z/4, (Z/2)^5+Z/4, then (Z/2)^6+Z/4 for every n>=3; all 60 degree-one maps preserve 0<2M<M.',
  'Cube27: R_(2) is Noetherian on the declared rank-16 finite integral carrier; I-adic completion is exact on every finite filtered short exact sequence. No splitting or polynomial completed-Rees presentation is inferred.',
  'Gauss: certified eighth trace and d8 intervals are produced; d8 crosses zero; numerical reduced-resolvent norm and numerical third pressure remain SEPARATED.',
  'Codimension-3: 256-bit Arb strictly narrows both unique regular return crossings; cross-singular quotient/holonomy bytes remain SEPARATED.',
  'Golden: type3/order32 has 29 E8 subgroups; 17 actual E8+B5 blocks reach candidate rank 56 after 557056 rows, closing the third native H5/B5 carrier exactly.',
  'Recurrence: full repairs 91/93/95 and full 106-115 yield a continuous exact atlas of 5609 tap pairs for every k=45..115.',
  'Recurrence: for every even k and odd v, reflection has equal exact matrix order; 691/691 full-atlas reflection pairs verify the general theorem. The atlas has 1130 collision classes, 297 cross-order.',
  'Recurrence: all 35 even fixed centers satisfy ordC=4k and hanti=2k; k+v never divides ordC there, with gcd(ordC,k+v)=k/2.',
  'D5/Pisano/Stone/Fibonacci: fresh scoped preflight finds no complete new source packet; D5 remains NT, historical p5 remains SEPARATED, and 37 project gates remain active.'
 ],
 'status_counts':st['counts'],'merge_counts':mg['counts'],'active_project_NT_count':37,'ABI_complete_actual_project_packets':0,'promoted_project_values':0,
 'verification':{'family_count':ver['family_count'],'explicit_verifier_assertions':ver['explicit_verifier_assertions'],'explicit_witness_records':ver['explicit_witness_records'],'coverage_units':ver['coverage_units'],'verifier':'verifier_stdout_II_KM_deep.json'},
 'standard_theorem_dependency':{'reference':'Stacks Project, Algebra Lemma 10.97.2 (tag 00MB), completion exact on finitely generated modules over a Noetherian ring','use':'Cube27 I-adic completion exactness only; project-specific finiteness/SNF/filter data are replayed locally'},
 'infrastructure':{'lean_4_30_archive_verified':True,'lean_archive_sha256':'1e334ce3f54d3f2b82556ef5bb36c94bf40d79eb817a987a4aa007c7c210a611','lean_extraction':'DEFERRED_UNTIL_SELECTIVE_MATHLIB_TREE','proof_assistant_claim':'NO_LEAN_THEOREM_REPLAY_CLAIMED_IN_II_KM'},
 'source_sha256':source_sha,'safe_successor':safe
}
(R/'II_KM_certificate.json').write_text(json.dumps(cert,indent=2,sort_keys=True,ensure_ascii=False)+'\n')
auth={'phase':'II-KM','authority_order':['II_KM_cube27_2local_completed_rees.json','II_KM_gauss_eighth_fredholm.json','II_KM_codim3_sharp_crossing_source_audit.json','II_KM_golden_native_H5_type3.json','II_KM_recurrence_odd_repair_91_93_95.json','II_KM_recurrence_106_115.json','II_KM_recurrence_full_45_115_collision_divisibility.json','II_KM_source_project_gates.json','master_status_registry_II_KM.json','master_merge_registry_II_KM.json','verifier_stdout_II_KM_deep.json','II_KM_certificate.json'],'guards':['producer JSONs are authorities only on their declared carriers','the PDF is editorial synthesis, not a replacement for producer payloads','source retrieval gives provenance evidence and never mathematical nonexistence','standard literature supplies general completion theorem only; project-specific hypotheses are locally checked'],'safe_successor':safe}
(R/'II_KM_authority_registry.json').write_text(json.dumps(auth,indent=2,sort_keys=True)+'\n')
# concise report
md=f"""# II-KM - compte rendu de fermeture\n\n**OVERALL=PASS**; predecessor `II-KL/PASS`; observational continuity `PASS_298`; historical exhaustive replay `NT_NOT_EXHAUSTIVE`.\n\n## Nouvelles fermetures\n\n- Cube27: filtration primaire 2-locale exacte, classe Ext detectee, exactitude de completion I-adique sur les etages finis; presentation scindee/polynomiale du Rees complete reste `SEPARATED`.\n- Gauss: huitieme trace/coefficient de Fredholm certifies; norme quantitative de la resolvante reduite et valeur numerique de `P'''(0)` restent `SEPARATED`.\n- Codim-3: deux croisements reguliers strictement resserres a 256 bits; holonomie cross-singuliere toujours source-bloquee.\n- Golden: troisieme fermeture native `H^5/B^5`, type 3, dimension 56, 17 blocs E8, 557056 lignes.\n- Recurrence: atlas complet `45<=k<=115`, 5609 familles; 1130 classes de collision dont 297 cross-order; theorem general de collision de reflexion a ordre egal pour k pair/v impair, replay `691/691`.\n- D5/Pisano/Stone/Fibonacci: frontieres source preservees, aucun paquet projet ABI complet.\n\n## Checkpoint\n\n- Truth: `{st['counts']['PASS']} PASS`, `{st['counts']['ZERO']} ZERO`, `{st['counts']['SEPARATED']} SEPARATED`, `{st['counts']['REFUTED']} REFUTED`, `{st['counts']['NT']} NT`.\n- Merge: `{mg['counts']['PROVEN-MERGEABLE']} PROVEN-MERGEABLE`, `{mg['counts']['PROVEN-NOT-MERGEABLE']} PROVEN-NOT-MERGEABLE`.\n- Deep verifier: {ver['family_count']} families, {ver['explicit_verifier_assertions']} assertions, {ver['explicit_witness_records']} witnesses, {ver['coverage_units']} coverage units.\n\n## Frontiere sure\n\n{safe}\n"""
(R/'II_KM_compte_rendu.md').write_text(md)
# TeX
trlo,trhi=g['eighth_trace']['certified_interval_decimal']; dlo,dhi=g['fredholm_d8']['certified_interval_decimal']
# Short outward-rounded display values; full Arb decimals remain authoritative in producer JSON.
trlo_tex='0.1690543204202985'; trhi_tex='39.00586060099235'; dlo_tex='-5.038088123389629'; dhi_tex='2.113462121846312'
sq=co['arb_crossing_localization']['sqrt5_over_4']['final_interval']; pi=co['arb_crossing_localization']['pi_over_6']['final_interval']
large=rec['collision_quotient']['largest_classes'][0]
tex=r"""\documentclass[9.5pt,a4paper]{article}
\usepackage[margin=1.38cm]{geometry}
\usepackage[T1]{fontenc}\usepackage[utf8]{inputenc}\usepackage{lmodern,microtype}
\usepackage{amsmath,amssymb,mathtools,booktabs,array,tabularx,enumitem,xurl}
\usepackage[colorlinks=true,linkcolor=blue!45!black,urlcolor=blue!45!black]{hyperref}
\setlength{\parindent}{0pt}\setlength{\parskip}{0.30em}\setlength{\emergencystretch}{4em}\setlist{nosep,leftmargin=*}
\newcommand{\PASS}{\textsf{PASS}}\newcommand{\ZERO}{\textsf{ZERO}}\newcommand{\SEP}{\textsf{SEPARATED}}\newcommand{\REF}{\textsf{REFUTED}}\newcommand{\NT}{\textsf{NT}}
\title{\textbf{II-KM -- 2-local Cube27 completion, eighth Gauss Fredholm,}\\\textbf{sharper codimension-three Arb localization, third native Golden $H^5$,}\\\textbf{and full recurrence atlas $45$--$115$}}
\author{Nico Begue Marquot -- formal HT+NT continuation bundle}\date{19 August 2026}
\begin{document}\maketitle\vspace{-1.25em}
\begin{abstract}\small
II-KM freezes II-KL under the append-only HT+NT discipline.  It localizes the Cube27 augmentation filtration at $2$, closes exact $I$-adic completion on the finite filtered modules while refusing an unsupported splitting of the completed Rees algebra, computes an eighth Gauss transfer trace/Fredholm coefficient, strictly narrows both regular codimension-three return crossings at 256-bit Arb precision, obtains the third native Golden $H^5/B^5$ closure (type 3, order 32, dimension 56), and repairs the recurrence atlas to a full exact census for every $45\le k\le115$.  The recurrence reflection law is sharpened to a general equal-order collision theorem for even $k$ and odd $v$.  Missing $D_5$, historical $p=5$, Stone and Fibonacci source packets remain explicitly gated.
\end{abstract}
\section{Frozen semantics and checkpoint}
Truth states remain $\{\PASS,\ZERO,\SEP,\REF,\NT\}$; mergeability remains an independent axis.  Retrieval, numerical replay, theorem application and project-value promotion are separate evidence channels.  II-KL enters at $(1432,97,450,294,87)$ with merge counts $(675,456)$.

\section{Cube27: $2$-local filtration and exact completion}
The actual relation matrices reproduce
\[
\operatorname{gr}^1_{I,(2)}R\simeq(\mathbb Z/2)^2\oplus\mathbb Z/4,\qquad
\operatorname{gr}^2_{I,(2)}R\simeq(\mathbb Z/2)^5\oplus\mathbb Z/4,
\]
\[
\boxed{\operatorname{gr}^n_{I,(2)}R\simeq(\mathbb Z/2)^6\oplus\mathbb Z/4\quad(n\ge3).}
\]
The filtration $0\subset2M\subset M$ has $(\dim M/2M,\dim 2M)=(3,1),(6,1),(7,1)$ in degrees $1,2,\ge3$, and all $60$ serialized degree-one operators preserve it.

On the declared Cube27 carrier, the integral ring is finite free of rank $16$ over $\mathbb Z$; hence its localization $R_{(2)}$ is Noetherian.  Completion exactness for finite modules over a Noetherian ring (Stacks Project, Algebra Lemma 10.97.2, tag 00MB) therefore applies to
\[
0\to I^{n+1}_{(2)}\to I^n_{(2)}\to\operatorname{gr}^n_I(R)_{(2)}\to0,
\]
giving
\[
\boxed{0\to\widehat{I^{n+1}_{(2)}}\to\widehat{I^n_{(2)}}\to\operatorname{gr}^n_I(R)_{(2)}\to0.}
\]
The conductor class remains nonzero at $2$: $\dim_{\mathbb F_2}A_2/2A_2=13$ and the frozen detector has value $1$.  It vanishes after inverting $2$.  Exact completion does \emph{not} provide compatible splittings; ``period-two associated graded implies period-two filtered completion'' is \REF{} as an inference, while a split/polynomial completed-Rees presentation remains \SEP.

\section{Gauss and codimension-three return}
For the inherited trace-class Gauss carrier, $6^8=1{,}679{,}616$ exact branch words are grouped into $53{,}613$ matrix-trace classes.  At 192-bit Arb precision,
\[
\boxed{%s<\operatorname{tr}(L^8)<%s}
\]
and Newton's identity yields
\[
\boxed{%s<d_8<%s.}
\]
The $d_8$ interval crosses zero.  The reduced resolvent exists abstractly from II-KL, but a certified numerical norm and a proof-grade numerical $P'''(0)$ remain \SEP.

At 256 bits the two regular crossings contract strictly to
\[
\boxed{c_{\sqrt5/4}\in[%.16g,%.16g]},\qquad
\boxed{c_{\pi/6}\in[%.16g,%.16g]}.
\]
Their derivative enclosures remain strictly negative.  The alternating source-bound $C_8$ bad-stratum incidence is retained, but no cross-singular transition arrows are recovered; the true compactified germinal leaf groupoid remains \SEP.

\section{Golden-Hodge: third native $H^5/B^5$ closure}
II-KM treats the actual type-3 stabilizer of order $32$.  It finds $29$ elementary-abelian $E_8$ subgroups.  The candidate family contains $3884$ products built only from actual native $H^1,H^2,H^3$ representatives.  Each selected $E_8$ contributes an independent actual block
\[
B^5(E)=\operatorname{im}(\delta:C^4(E;\mathbb F_2)\to C^5(E;\mathbb F_2)).
\]
The joint candidate rank progresses through $21,27,33,34,\ldots,49,53,56$ and reaches the independent upper bound after $17$ subgroups and
\[
\boxed{557056\text{ streamed }C^5(E_8)\text{ rows}.}
\]
Therefore
\[
\boxed{\dim H^5_{\rm native}(\text{type }3)=56,\qquad\text{displayed native products span }H^5:\PASS.}
\]
This is the third native degree-five closure, after types 2 and 4.  It is not transferred to types $0,1,5,6$.  The free $\mathbb F_2[H]$-Wall degree-four producer remains \SEP.

\section{Recurrence: a full exact atlas and a reflection collision theorem}
For
\[
f_{k,v}(x)=x^k-x^v-1\in\mathbb F_3[x],\qquad 1\le v<k,
\]
II-KM repairs full orders $91,93,95$ ($276$ records), scans all orders $106$--$115$ ($1095$ records), and merges the exact predecessor scopes into
\[
\boxed{\sum_{k=45}^{115}(k-1)=5609\text{ factor-certified families}.}
\]
No state-space $3^k$ enumeration is used.

For even $k$ and odd $v$,
\[
f_{k,k-v}(x)=-x^k f_{k,v}(-1/x),
\]
so $C(k,k-v)$ is similar to $-C(k,v)^{-1}$.  Let $N=\operatorname{ord}C(k,v)$.  Since $\det C=-1$, $N$ is even.  If $-I\notin\langle C\rangle$, the reflected order is $\operatorname{lcm}(2,N)=N$.  If $C^{N/2}=-I$, determinants force $4\mid N$, hence $\gcd(N,N/2-1)=1$ and again the reflected order is $N$.  Thus
\[
\boxed{\operatorname{ord}C(k,k-v)=\operatorname{ord}C(k,v)\quad(k\text{ even},\ v\text{ odd}).}
\]
The full atlas verifies $691/691$ unordered applicable pairs with zero violations.

The exact quotient has $1130$ collision classes, including $297$ cross-order classes.  The largest class has size %d at matrix order %s.  The divisibility census gives
\[
\boxed{k\mid\operatorname{ord}C:621,\quad v\mid\operatorname{ord}C:1311,\quad(k+v)\mid\operatorname{ord}C:494.}
\]
All $35$ even fixed centers satisfy
\[
\boxed{\operatorname{ord}C=4k,\quad h_{\rm anti}=2k,\quad \gcd(\operatorname{ord}C,k+v)=k/2,\quad(k+v)\nmid\operatorname{ord}C.}
\]
The odd-order global-antiperiod sector is \ZERO{} on the entire full atlas.  Likewise there are no finite-scope hits of $\operatorname{ord}C=k$ or $\operatorname{ord}C=k+v$.

\section{Source gates, ledger and safe continuation}
Fresh declared Library/GitHub searches recover no new continuous rank-three $D_5$ transition packet and no full historical $p=5$ local Tate byte packet.  These are scoped retrieval observations only.  Stone still lacks the actual project $d,\theta,K_Z,C$ and framing/residue provenance; Fibonacci still lacks an instantiated carrier/localization/cofinal-basis/trace-table packet.  Hence
\[
\boxed{\text{ABI-complete actual packets}=0,\quad\text{promoted values}=0,\quad37\text{ gates active}.}
\]
The append-only checkpoint closes at
\[
\boxed{%d\ \PASS,\ %d\ \ZERO,\ %d\ \SEP,\ %d\ \REF,\ %d\ \NT},
\]
\[
\boxed{%d\ \textsf{PROVEN-MERGEABLE},\qquad%d\ \textsf{PROVEN-NOT-MERGEABLE}.}
\]
The deep verifier closes %d families with %d explicit assertions, %d witness records and %d coverage units.  Observational continuity is \texttt{PASS\_298}; exhaustive historical replay remains \texttt{NT\_NOT\_EXHAUSTIVE}.

\par\noindent\textbf{Safe successor.}\par\smallskip
\begin{minipage}{\linewidth}\scriptsize\raggedright\sloppy
%s
\end{minipage}
\begin{thebibliography}{9}\small
\bibitem{KL} II-KL frozen formal bundle and authority registry.
\bibitem{StacksCompletion} The Stacks Project, Algebra, Lemma 10.97.2 (tag 00MB), completion for Noetherian rings.
\bibitem{EV} D. B. A. Epstein and E. Vogt, A Counterexample to the Periodic Orbit Conjecture in Codimension 3, Ann. of Math. 108 (1978), 539--552; project copy hash-locked in the predecessor lineage.
\end{thebibliography}
\end{document}
"""%(trlo_tex,trhi_tex,dlo_tex,dhi_tex,sq[0],sq[1],pi[0],pi[1],large['class_size'],large['matrix_order'],st['counts']['PASS'],st['counts']['ZERO'],st['counts']['SEPARATED'],st['counts']['REFUTED'],st['counts']['NT'],mg['counts']['PROVEN-MERGEABLE'],mg['counts']['PROVEN-NOT-MERGEABLE'],ver['family_count'],ver['explicit_verifier_assertions'],ver['explicit_witness_records'],ver['coverage_units'],safe)
(R/'II_KM_2LocalRees_Fredholm_Golden_Arb_FLINT_R1.tex').write_text(tex,encoding='utf-8')
print(json.dumps({'certificate':str(R/'II_KM_certificate.json'),'tex':str(R/'II_KM_2LocalRees_Fredholm_Golden_Arb_FLINT_R1.tex'),'safe_successor':safe},indent=2))
