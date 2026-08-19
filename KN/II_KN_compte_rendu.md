# II-KN - compte rendu

`OVERALL=PASS`; predecessor `II-KM/PASS`; observational continuity `PASS_299`; historical exhaustive replay `NT_NOT_EXHAUSTIVE`.

## Checkpoint append-only

- PASS: 1479
- ZERO: 102
- SEPARATED: 467
- REFUTED: 297
- NT: 93
- PROVEN-MERGEABLE: 695
- PROVEN-NOT-MERGEABLE: 472
- active project gates: 37
- promoted project values: 0

## Fermetures

Cube27: toutes les suites filtrees completees sont exactes mais non scindees, car leurs termes du milieu sont `Z_(2)`-sans torsion et leurs quotients gradues portent du 2-torsion. La presentation topologique par limite inverse est PASS; le produit scinde des grades est REFUTED; une presentation polynomiale topologique explicite reste SEPARATED.

Gauss: `tr(L^9)` et `d9` sont certifies; l'intervalle de `d9` traverse zero. Le certificat primaire GKW sur `H^2(D1)` donne une borne de resolvante `<=425` sur le cercle du pole dominant; l'identite de Laurent donne donc `||S_H||<=425`. Le transport de cette norme vers le carrier pondere et une valeur numerique proof-grade de `P'''(0)` restent SEPARATED.

Golden: le stabilisateur natif type 5, ordre 32, ferme `dim H^5=56` apres 17 sous-groupes E8 et 557056 lignes. C'est la quatrieme fermeture native independante, apres types 2,4,3.

Recurrence: 1195 familles exactes nouvelles sur 116--125. Le theoreme general `ord(f(x^d))=d ord(f)` est prouve et qualifie sur l'atlas complet 2--125; il donne `ordC(k,v)=g ordC(k/g,v/g)` avec `g=gcd(k,v)`. L'atlas principal 45--125 contient 6804 familles et 1354 classes de collision, dont 351 cross-order.

Codim-3, D5, Pisano p=5 et Stone/Fibonacci restent strictement source-gates selon leurs ABI declares.

## Infrastructure Lean/mathlib

Lean 4.30.0 est maintenant extrait et executable localement; les 14,486 entrees du manifeste source ont ete verifiees sans erreur et le digest source-tree est reproduit. Aucun fragment mathlib n etait monte au freeze II-KN; leur reconstruction sans manifeste amont est reportee a II-KO avec SHA locaux, validation du flux/TAR et smoke test `import Mathlib` obligatoires.

## Verification

Deep verifier: 12 familles, 20,960 assertions explicites, 258,990 temoins, 20,741,896 unites de couverture. PDF: 4 pages A4, zero overfull, zero violation de bbox, inspection visuelle PASS.

## Frontiere sure

II-KO -- Cube27 explicit completed-Rees extension cocycle/pro-system and minimal topological generators-relations or obstruction audit; Gauss tenth Fredholm trace/coefficient plus weighted reduced-resolvent norm transport or proof-grade numerical third-pressure enclosure; codimension-3 cross-singular arrow/topology packet acquisition and compactified leaf-groupoid cocycle realization; Golden fifth native H5/B5 closure among types 0,1,6 or trusted free F2[H]-Wall degree-four producer; post-A1BK/A1BL D5 continuous transition-source ingestion; historical Pisano p=5 local Tate packet acquisition; recurrence full orders 126--135 and quotient classification modulo reflection/dilation primitive rays; local Lean/mathlib workspace reconstruction and first native formal replay when the transferred archive is complete; plus external Stone/Fibonacci ABI-complete packet execution.
