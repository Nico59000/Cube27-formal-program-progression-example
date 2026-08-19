from pathlib import Path
import json,hashlib,os
R=Path(__file__).resolve().parent
ver=json.load(open(R/'verifier_stdout_II_KL_deep.json'));st=json.load(open(R/'master_status_registry_II_KL.json'));mg=json.load(open(R/'master_merge_registry_II_KL.json'))
cube=json.load(open(R/'II_KL_cube27_filtered_rees_ext.json'));gauss=json.load(open(R/'II_KL_gauss_seventh_reduced_resolvent.json'));cod=json.load(open(R/'II_KL_codim3_quotient_germinal.json'));gold=json.load(open(R/'II_KL_golden_H5_wall_audit.json'));rec=json.load(open(R/'II_KL_recurrence_order_value_89_96_105.json'));d5=json.load(open(R/'II_KL_D5_post_A1BI_source_audit.json'));pis=json.load(open(R/'II_KL_Pisano_p5_source_audit.json'));proj=json.load(open(R/'II_KL_project_value_attempt.json'))
safe=("II-KM -- Cube27 2-local conductor-Ext module filtration and completed Rees exactness/periodic-module audit; "
      "Gauss eighth Fredholm trace/coefficient and certified reduced-resolvent norm or proof-grade numerical third-pressure enclosure; "
      "codimension-three cross-singular quotient/holonomy source ingestion with sharper Arb crossing localization; "
      "Golden third native H5/B5 closure or a trusted free F2[H]-Wall degree-four producer; post-A1BI/A1BJ D5 transition-source ingestion; "
      "Pisano historical p5 additive-character/Haar/Tate packet acquisition; recurrence FLINT repair of full orders 91/93/95 plus full orders 106--115 and divisibility/collision theorem refinement; "
      "plus external Stone/Fibonacci ABI-complete packet execution.")
cert={'phase':'II-KL','predecessor':'II-KK','overall':'PASS','title':'Full filtered Cube27 Rees/Ext localization; seventh Gauss Fredholm and reduced resolvent; codim3 regular germ atlas; second native Golden H5 closure; FLINT order89 repair and full 96-105 recurrence atlas',
      'status_counts':st['counts'],'merge_counts':mg['counts'],'observational_continuity':ver['observational_continuity'],'historical_replay':ver['historical_replay'],'ABI_complete_actual_project_packets':0,'promoted_project_values':0,'active_project_NT_count':37,
      'verification':{'family_count':ver['family_count'],'explicit_verifier_assertions':ver['explicit_verifier_assertions'],'explicit_witness_records':ver['explicit_witness_records'],'coverage_units':ver['coverage_units']},
      'key_results':[
       'Cube27: full all-n degree-one multiplication data on gr_I is serialized by low maps plus the proven period-two tail; A2/2A2 has dimension 13, the nonzero conductor class is explicitly detected, survives 2-localization, dies away from 2, and its detected Ext1(Z/2,Z/2) pushout has zero Yoneda square in Ext2.',
       'Gauss: certified seventh trace and d7 intervals; the reduced resolvent on the Riesz complement exists abstractly from the simple isolated leading eigenvalue, giving an exact third-pressure Riesz identity; numerical reduced-resolvent norm and numerical third response remain separated.',
       'Codimension-3: one further Arb interval-Newton contraction on each unique crossing; seven regular axis-start germinal holonomy records H_c=R_u S_0 T; C8 bad-stratum atlas source-bound, cross-singular quotient groupoid still separated.',
       'Golden: a second exact native H5/B5 closure is obtained for type4/order32: six elementary-abelian E8 restrictions with independent actual B5 blocks reach the independent dimension 34 after 196608 rows; type2=14 remains closed; free Wall degree4 remains separated.',
       'D5: fresh post-A1BI scoped retrieval finds no continuous rank3 transition packet; NT preserved.',
       'Pisano: no new historical p5 additive-character/Haar/Tate byte packet; terminal obstruction only for the retrieved scope.',
       'Recurrence: python-flint factor engine completes the previously resource-gated full order89 sweep (88/88 taps) and matches all nine old probes; full orders96-105 contribute 995 exact records; 124/124 reflection pairs and five fixed centers pass; 237 new/repaired collision classes are serialized.',
       'Stone/Fibonacci: no ABI-complete actual packet; zero promoted values; 37 gates preserved.'
      ],
      'guards':['truth and mergeability axes remain orthogonal and append-only','89 is a Fibonacci-number coordinate worth studying, but the old SymPy timeout is not itself mathematical evidence of specialness; FLINT completes the full sweep rapidly','full filtered associated-graded multiplication data are not a new identity with geometric carriers','Ext localization/product claims are in the abelian-group conductor exact sequence','reduced-resolvent existence does not imply absolute time-domain three-point cumulant summability or a numerical P third derivative','regular holonomy germs and C8 bad-stratum incidence do not manufacture a cross-singular leaf groupoid','type4 H5 closure is not extrapolated to repeated-dimension stabilizer types','free Wall degree4 remains separated despite native H5 progress','zero source hits are scoped discovery evidence only'],
      'safe_successor':safe}
# self-excluding digest for certificate reproducibility
raw=json.dumps(cert,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode();cert['certificate_digest_without_self']=hashlib.sha256(raw).hexdigest()
(R/'II_KL_certificate.json').write_text(json.dumps(cert,indent=2,sort_keys=True,ensure_ascii=False)+'\n')
auth={'phase':'II-KL','authority_order':['II_KL_cube27_filtered_rees_ext.json','II_KL_gauss_seventh_reduced_resolvent.json','II_KL_codim3_quotient_germinal.json','II_KL_golden_native_H5_type4.json','II_KL_golden_H5_wall_audit.json','II_KL_recurrence_order_value_89_96_105.json','II_KL_D5_post_A1BI_source_audit.json','II_KL_Pisano_p5_source_audit.json','II_KL_project_value_attempt.json','master_status_registry_II_KL.json','master_merge_registry_II_KL.json','verifier_stdout_II_KL_deep.json','II_KL_certificate.json'],'failed_or_non_authoritative':['golden_type4_test.py','II_KL_golden_native_H5_type4_test.json','golden_e8_aug_diag.py','codim3_test_newton.py'],'guards':['producer JSONs are authorities only on their declared carriers','PDF is editorial synthesis','source_recovery files are provenance dependencies and acquire no project authority by inclusion','diagnostic/failed candidate files are excluded from authority'],'safe_successor':safe}
(R/'II_KL_authority_registry.json').write_text(json.dumps(auth,indent=2,sort_keys=True)+'\n')
md=f'''# II-KL — compte rendu de fermeture

**Verdict :** `OVERALL=PASS`  
**Prédécesseur :** II-KK / PASS  
**Continuité observationnelle :** `{ver['observational_continuity']}`  
**Replay historique exhaustif :** `{ver['historical_replay']}`

## Résultats principaux

- Cube27 : données de multiplication par les 15 générateurs d'augmentation fermées en tout degré par raccord bas degré + queue 2-périodique ; classe Ext conductrice explicitement 2-locale et détectée.
- Gauss : `tr(L^7)` et `d7` certifiés ; résolvante réduite existante sur le complément de Riesz, formule exacte du troisième ordre, mais pas encore de norme numérique proof-grade.
- Codimension 3 : nouvelles contractions Arb et atlas de sept germes réguliers ; le recollement singulier réel reste séparé.
- Golden : deuxième fermeture native `H5/B5`, type 4 d'ordre 32, rang exact 34 par six sous-groupes élémentaires `E8`; le Wall libre degré 4 reste séparé.
- D5/Pisano : aucun nouveau paquet source complet dans les scopes récupérés.
- Récurrences : remplacement de la voie SymPy haute-degré par `python-flint`; ordre 89 complet `88/88`, qualification `9/9` avec les sondes de II-KK ; ordres 96--105 complets (`995` enregistrements).
- Stone/Fibonacci : zéro paquet ABI complet, zéro valeur promue, 37 portes actives.

## Checkpoint

`{st['counts']['PASS']} PASS / {st['counts']['ZERO']} ZERO / {st['counts']['SEPARATED']} SEPARATED / {st['counts']['REFUTED']} REFUTED / {st['counts']['NT']} NT`

`{mg['counts']['PROVEN-MERGEABLE']} PROVEN-MERGEABLE / {mg['counts']['PROVEN-NOT-MERGEABLE']} PROVEN-NOT-MERGEABLE`

## Vérification

{ver['family_count']} familles, {ver['explicit_verifier_assertions']} assertions explicites, {ver['explicit_witness_records']} témoins, {ver['coverage_units']} unités de couverture.

## Frontière sûre suivante

{safe}
'''
(R/'II_KL_compte_rendu.md').write_text(md)
# values for TeX
tr7=gauss['seventh_trace']['certified_interval'];d7=gauss['fredholm_d7']['certified_interval'];b1=cod['arb_crossing_localization']['sqrt5_over_4']['final_interval'];b2=cod['arb_crossing_localization']['pi_over_6']['final_interval'];s89=rec['engine_upgrade']['full_order89'];fixed=rec['reflection_theorem']['fixed_centers']
rows='\\\\\n'.join(f"{x['k']} & {x['v']} & {x['matrix_order']} & {x['global_antiperiod_h']}" for x in fixed)
tex=r"""\documentclass[10pt,a4paper]{article}
\usepackage[margin=1.42cm]{geometry}
\usepackage[T1]{fontenc}\usepackage{lmodern}
\usepackage{amsmath,amssymb,mathtools,booktabs,array,tabularx,microtype,xurl}
\usepackage[colorlinks=true,linkcolor=blue!45!black,urlcolor=blue!45!black]{hyperref}
\setlength{\parindent}{0pt}\setlength{\parskip}{0.32em}\setlength{\emergencystretch}{3em}
\newcommand{\PASS}{\textsf{PASS}}\newcommand{\ZERO}{\textsf{ZERO}}\newcommand{\SEP}{\textsf{SEPARATED}}\newcommand{\REF}{\textsf{REFUTED}}\newcommand{\NT}{\textsf{NT}}
\title{\textbf{II-KL -- Filtered Cube27 Rees/Ext localization, seventh Gauss Fredholm,}\\\textbf{codimension-three germinal atlas, second native Golden $H^5$ closure,}\\\textbf{full order-89 repair and recurrence orders 96--105}}
\author{Nico Begue Marquot -- formal HT+NT continuation bundle}\date{19 August 2026}
\begin{document}\maketitle\vspace{-1.35em}
\begin{abstract}\small
II-KL freezes II-KK and preserves the append-only HT+NT discipline.  The Cube27 augmentation filtration is now serialized by degree-one multiplication data in every associated-graded degree and the nonzero conductor extension class is audited under $2$-localization and Yoneda pushout.  A seventh Gauss trace/Fredholm coefficient is enclosed with Arb and the simple leading Riesz point yields a genuine reduced-resolvent existence certificate, without inventing a numerical third pressure response.  Codimension three gains a seven-level regular germinal atlas but no cross-singular quotient identification.  Golden closes a second native $H^5/B^5$ carrier, type 4 of order 32, through six elementary-abelian $E_8$ restrictions.  The recurrence engine is upgraded to FLINT: the previously resource-gated Fibonacci order $89$ is completed in full and orders $96$--$105$ are scanned exhaustively.  No Stone/Fibonacci project value is fabricated.
\end{abstract}
\section{Cube27: filtered Rees data and the $2$-primary Ext class}
Let $I$ be the dimension-augmentation ideal.  The low pieces remain
\[
\operatorname{gr}_I^0R\simeq\mathbb Z,\qquad
\operatorname{SNF}(I/I^2)=(2,2,12),
\]
\[
\operatorname{SNF}(I^2/I^3)=(2,2,2,2,2,12),\qquad
\operatorname{SNF}(I^n/I^{n+1})=(2,2,2,2,2,2,12)\quad(n\ge3).
\]
II-KL now places in one authority object the $15$ multiplication maps $\operatorname{gr}^1\to\operatorname{gr}^2$, the $15$ maps $\operatorname{gr}^2\to\operatorname{gr}^3$, and the two $15$-operator families of the proven odd/even period-two tail.  Thirty descent checks and $225$ low-degree commutativity checks pass.  Since the declared augmentation ideal is generated by these fifteen classes, this reconstructs multiplication by degree-one generators on every $\operatorname{gr}_I^n$.  No new polynomial-quotient presentation of the completed Rees algebra is asserted.

For the conductor pullback class $e=[2x]\in\operatorname{Ext}^1_{\mathbb Z}(\mathbb Z/2,A_2)$, II-KL computes
\[
\boxed{\dim_{\mathbb F_2} A_2/2A_2=13}
\]
and an explicit detector $\lambda$ with $\lambda(e)=1$.  The class survives at the $2$-localization and vanishes after inverting $2$ (hence at every odd localization).  Pushing out by $\lambda$ gives a nonzero
\[
\epsilon\in\operatorname{Ext}^1_{\mathbb Z}(\mathbb Z/2,\mathbb Z/2),
\]
while
\[
\boxed{\epsilon^2=0\in\operatorname{Ext}^2_{\mathbb Z}(\mathbb Z/2,\mathbb Z/2)}
\]
because $\mathbb Z/2$ has projective dimension one over $\mathbb Z$.

\section{Gauss and codimension-three holonomy}
Seven inverse branches have determinant $-1$.  Summing the $7^7=823543$ exact branch contributions and enclosing the positive complement yields
\[
\boxed{%s<\operatorname{tr}(L^7)<%s}.
\]
Newton's identity then gives
\[
\boxed{%s<d_7<%s}.
\]
The interval crosses zero, so no sign is claimed.

The leading eigenvalue at $t=0$ is simple and isolated with Riesz projector $P$ inherited on the declared Gauss carrier.  For $Q=I-P$ the reduced resolvent
\[
\boxed{S=Q(I-L_0\vert_{QX})^{-1}Q}
\]
exists as a bounded operator.  Hence the third perturbative identity
\[
\lambda_3=\ell(L_3h)+3\ell(L_2Su_1)+3\ell(L_1Su_2),\qquad
P'''(0)=\lambda_3-3\lambda_2\lambda_1+2\lambda_1^3
\]
is now well-typed and exact.  A numerical norm for $S$, a numerical $P'''(0)$ and absolute time-domain three-point cumulant summability remain \SEP.

At $192$-bit Arb precision the two unique regular crossings are further enclosed by
\[
\boxed{c_{\sqrt5/4}\in[%s,%s]},\qquad
\boxed{c_{\pi/6}\in[%s,%s]}.
\]
Seven regular levels $c=0.84,0.86,\ldots,0.96$ carry interval-certified germs
\[
H_c=R_{u(c)}S_0T,\qquad H_c^2=1.
\]
The source-bound bad-stratum atlas remains the alternating $C_8$ incidence of four $S^3$ and four $T^2$ pieces.  No source-bound cross-singular holonomy arrows are recovered; the actual compactified leaf groupoid remains \SEP.

\section{Golden-Hodge: second native $H^5/B^5$ closure}
Type 2 remains closed at $\dim H^5=14$.  II-KL treats type 4, whose stabilizer has order $32$.  Sixteen elementary-abelian $E_8$ subgroups are found on the actual group.  The candidate family consists only of restrictions of actual native products built from inherited native $H^1,H^2,H^3$ representatives.  For each selected $E_8$, the actual inhomogeneous coboundary block
\[
B^5(E)=\operatorname{im}\bigl(\delta:C^4(E;\mathbb F_2)\to C^5(E;\mathbb F_2)\bigr)
\]
is inserted as an independent block in one joint augmented rank calculation.  After six subgroups and
\[
\boxed{196608\text{ streamed }C^5(E_8)\text{ rows}}
\]
the direct-sum restriction image reaches exactly $34$ independent candidate pivots.  The independent abstract upper bound is also $34$, therefore
\[
\boxed{\dim H^5_{\rm native}(\text{type }4)=34,\qquad\text{native displayed products span it}:\PASS.}
\]
This is the second native degree-five closure.  It is not extrapolated to types $0,1,3,5,6$.  The genuine free $\mathbb F_2[H]$ Wall degree-four producer still lacks a free basis, equivariant $d_4$, twisting data and $\Phi_4$ bytes and remains \SEP.

\section{Recurrence: full Fibonacci order 89 and orders 96--105}
The previous order-$89$ resource overrun belonged to the SymPy implementation path.  II-KL switches the factor ABI to \texttt{python-flint} \texttt{nmod\_poly.factor} plus \texttt{fmpz.factor}, with cached factorizations of $3^d-1$.  The nine old II-KK order-$89$ probes agree $9/9$ with the new engine.  The complete sweep now contains
\[
\boxed{88/88\text{ tap values at }k=89}
\]
with %d distinct matrix orders; no full global antiperiod occurs, in accordance with the odd-order determinant theorem.  The old timeout is therefore \emph{not} an engine-independent invariant.  Since $89$ is nevertheless a Fibonacci number, it remains an explicitly typed structural coordinate for later order/value comparisons.

All tap values are also factorized for every $k=96,\ldots,105$:
\[
\boxed{995\text{ new exact factor records}.}
\]
On $k=96,98,100,102,104$, the reflection theorem passes
\[
\boxed{124/124}
\]
applicable odd-$v$ pairs.  The fixed centers are
\begin{center}\begin{tabular}{rrrr}\toprule $k$&$v=k/2$&$\operatorname{ord}C$&$h_{\rm anti}$\\\midrule
%s\\\bottomrule\end{tabular}\end{center}
so again $\operatorname{ord}C=4k$ and $h_{\rm anti}=2k$.  The repaired/new collision quotient contains $237$ classes, $68$ cross-order, including four classes involving the now-complete order $89$.  No new record satisfies $\operatorname{ord}C=k$ or $k+v$.  The divisibility coordinates remain richer than any single linear order/value law and are kept internal to the recurrence carrier.

\section{$D_5$, Pisano, project gates and checkpoint}
Fresh post-A1BI retrieval yields no continuous rank-three $D_5$ transition packet in the declared Library/GitHub scope.  This is scoped retrieval evidence only; the continuous packet remains \NT.  The historical Pisano $p=5$ lane still lacks a complete additive-character/self-dual-Haar/conductor/uniformizer/Tate byte packet, so its scoped obstruction is preserved.  Stone still lacks project $d,\theta,K_Z,C$ and the framing anchor; Fibonacci still lacks an instantiated carrier/localization/cofinal-basis/trace-table packet.  Hence
\[
\boxed{\text{ABI-complete packets}=0,\quad\text{promoted values}=0,\quad37\text{ project gates active}.}
\]
The append-only checkpoint is
\[
\boxed{%d\ \PASS,\ %d\ \ZERO,\ %d\ \SEP,\ %d\ \REF,\ %d\ \NT},
\]
\[
\boxed{%d\ \textsf{PROVEN-MERGEABLE},\qquad %d\ \textsf{PROVEN-NOT-MERGEABLE}.}
\]
The deep verifier closes %d families with %d explicit assertions, %d witness records and %d coverage units.  Observational continuity advances to \texttt{PASS\_297}; exhaustive historical replay remains \texttt{NT\_NOT\_EXHAUSTIVE}.

\textbf{Safe successor.}\par\begin{minipage}{\linewidth}\scriptsize\ttfamily\sloppy
%s
\end{minipage}
\end{document}
"""%(tr7[0],tr7[1],d7[0],d7[1],b1[0],b1[1],b2[0],b2[1],s89['distinct_matrix_orders'],rows,st['counts']['PASS'],st['counts']['ZERO'],st['counts']['SEPARATED'],st['counts']['REFUTED'],st['counts']['NT'],mg['counts']['PROVEN-MERGEABLE'],mg['counts']['PROVEN-NOT-MERGEABLE'],ver['family_count'],ver['explicit_verifier_assertions'],ver['explicit_witness_records'],ver['coverage_units'],safe)
(R/'II_KL_FilteredRees_Fredholm_Germinal_Golden_FLINT_R1.tex').write_text(tex)
print('wrote final docs')
