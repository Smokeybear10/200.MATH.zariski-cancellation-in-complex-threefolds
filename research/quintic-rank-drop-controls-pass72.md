# Exact controls for the quintic rank-drop deductions

The separate [standalone checker](quintic_rank_drop_checks_pass72.py)
contains five bounded exact methods. It accompanies the written
[third-image lemma](quintic-rank-drop-third-image-pass72.md),
[polynomial-clearing argument](quintic-rank-drop-polynomial-symmetry-pass72.md),
and [terminal recognition proof](terminal-quintic-recognition-pass72.md).
It does not prove their original-frame hypotheses or certify the
recognition theorems by computation.

## 1. Third full-image subtraction and rank

The first method keeps all five entries in the three formal vectors
representing \(24M^4(P,0)^t\), \(6M^3(P,0)^t\), and
\(2M^2(P,0)^t\). It performs the two stated subtractions exactly.
Their resulting upper directions are the independent constant vectors
\(c,e,v_0\); the auxiliary entries retain their variable coefficients.
A three-by-three upper minor is the nonzero parameter \(\mu_2\),
so the three full vectors have rank three. The actual constant dual
row for the remaining coordinate kills all three upper directions.

A separate constant Jordan matrix verifies the ranks of its second,
third, fourth, and fifth powers as \(3,2,1,0\). This matrix is not
asserted to be an actual companion of a four-dimensional action, nor
is it identified with the formal vectors above. The written argument
supplies membership of those vectors in the actual image and uses
the resulting spanning statement. The checker does not infer the
rank of an actual upper-left block by deleting auxiliary entries.

## 2. Polynomial clearing and repeated factors

The second method expands the two formulas for
\(n=g^2\beta\) and \(Q=g^4\kappa\), using the formal normalized
coefficient variables \(\sigma,u_0\) and the two actual-layer
expressions for \(E^2z,E^2b\). Differentiation by
\(g\partial_\sigma\), fixing \(g,u_0\), checks
\[
En=g^3/3,\qquad EQ=g^3n/2,\qquad E^2Q=g^6/6,
\qquad E(Q-3n^2/4)=0.
\]
This differentiating model tests the stated coefficient identities;
it is not a realization of the original action in four coordinates.

Another explicitly larger polynomial coefficient ring tests that the
field with outputs \((Q,g^2n,g^4,0)\) has zero second iterates on
its generators when the coefficient variables are fixed. It does not
give a global slice to that field.

Three selected repeated-factor cases use \(g=x^2y^3\), with
\(n=gr\), \(n=xy^2\), and \(n=1\). Exact rational cancellation
checks polynomiality of the cleared coefficients for powers two,
three, and four, together with the conditions
\[
g^2S\text{ polynomial}\iff g\mid n,
\qquad g^3S\text{ polynomial}\iff g\mid n^2.
\]
The middle case distinguishes these two conditions. In the coprime
numerator case the denominator exponents of \(\kappa\) are eight
and twelve, retaining four times each actual multiplicity of \(g\).
These are conditional algebraic controls, not examples asserted to
satisfy the original frame. The all-prime equivalences and conditional
minimality are proved in the separate written clearing argument.

## 3. Linear and quadratic coordinate-flow coefficients

The third method extracts the exact highest time coefficient of
\(A(w)\kappa+B(w)\beta+C(w)\) under both linear and quadratic
\(w\)-flows. The coefficient flows are
\[
\beta\mapsto\beta+tg/3,\qquad
\kappa\mapsto\kappa+tg\beta/2+t^2g^2/12.
\]
Seven selected polynomial triples cover omitted terms, low weighted
degrees, ties, and each possible uniquely highest contribution.
The quadratic cases use weights \(2\deg A+2,2\deg B+1,2\deg C\)
and include both an even quadratic/constant tie and an odd uniquely
highest linear contribution. These finite cases are coefficient
identities, not asserted zero relations or a classification by degree.

The special quadratic-flow identity uses
\(p=g(3\lambda\beta+2\lambda k)\) and verifies that
\(\kappa-w/(6\lambda)+k\beta-j\) stays fixed. It also checks
the exact completed-square identity used in the coefficient-field
argument and the degree-one squarefree polynomial on its right.
The checker does not prove the universal rational-square valuation
obstruction or the transcendence assertions; those are written proofs.

## 4. Actual polynomial shears and normalized defect signs

The fourth method verifies both inverse orders, both Jacobian inverse
orders, and determinant one for the endpoint coordinate changes.
For zero acceleration and nonzero constant speed, it uses
\[
f=w/(3\rho),\quad L=3f/2+\alpha,\quad
R=-3f^2/4-\alpha f+\gamma,
\]
\[
(a,b,z,w)\mapsto(a-Lb-Rz,\ b-fz,\ z,w).
\]
The formal symmetry has new outputs \((0,u,1,0)\). The actual
inverse gives \(\partial_{b'}=\partial_b+L\partial_a\),
and \(\delta L=1/2\) gives the exact formal adjoint identities
\[
D'=-D\ne0,\qquad[\delta,\partial_{a'}]=2D'.
\]
In particular no zero second adjoint is asserted for that output.
The additional constant-\(u\) shear is checked only after treating
\(u\) as a constant, as justified separately by the written
fixed-good-base argument.

The separate vanished-quadratic-coefficient branch checks the primitive
\(P=w^2/(12\rho^2)+u_1w/(2\rho)\), its derivative, and the
two shears leaving \(\partial_a\) as the original good output.

For nonzero acceleration, the actual map is
\[
(a,b,z,w)\mapsto
(a+kb-(w/(6\lambda)+j)z,\ b,z,w).
\]
It has new formal outputs \((0,\beta,1,0)\). Its transported
partial is \(\partial_{b'}=\partial_b-k\partial_a\), so
\(D'=D\ne0\) and \([\delta,\partial_{a'}]=-2D'\).
The coordinate-function equality \(b'=b\) is not mistaken for
equality of their coordinate partials.

All these maps are genuine polynomial automorphism calculations over
the displayed constant field, with only nonzero constants inverted.
Their derivative and adjoint tables are stipulated formal input,
not manufactured original-frame actions. The separate
[fixed-good-base lemma](fixed-good-base-coefficient-pass72.md)
is a written rational Lie-algebra argument, not a numerical inference
from these signs.

## 5. Actual fixed-base derivations and a necessary hypothesis

The fifth method computes brackets directly from polynomial vector
fields on the actual coordinate ring \(\mathbb C[a,w,b,z]\).
Put \(J=b-wz\) and take
\[
\delta=\partial_w+J^2\partial_a+(z+1)\partial_b,
\qquad S=\partial_z+w\partial_b.
\]
Here \(\delta w=\delta J=1\), \([\delta,S]=0\), and
\[
[\delta,\partial_a]=0,\qquad
\operatorname{ad}_\delta^2\partial_a=0,\qquad
D'=\operatorname{ad}_\delta^2\partial_b=-2\partial_a\ne0.
\]
Thus this is an actual positive control for the fixed-base lemma with
\(v=w\), constant \(\delta v=1\), and \(q=0\).
The brackets are calculated, not assumed as a table, and are also
checked on a rational probe. The actual polynomial map
\[
(a,w,b,z)\mapsto(a-J^3/3,\ w,\ J-w,\ z)
\]
has both inverse orders checked and transports \(\delta\) to the
second coordinate partial. In particular this particular derivation
is locally nilpotent and has slice \(w\). It is not asserted to
realize the terminal quintic or the full original rank-two frame.

The negative control instead takes
\(\delta=\partial_w\), \(S=\partial_z+a\partial_b\),
and \(v=a\). All other fixed-base hypotheses with \(q=0\)
hold, but \(D'=0\) and \(\partial_a v=1\).
This is an exact counterexample to deleting the nonzero-defect
premise, not a counterexample to the lemma or the recognition theorem.

## Verification and provenance

The final completed five-method version passed in **0.234 seconds**,
exit zero. Earlier four-method development versions passed in
0.149 and 0.203 seconds before the fifth method was added.
Those earlier runs are not additional current methods or suites.
Only `unittest` and SymPy are imported; no project solver or source
classification implementation is imported.

The checker author independently read and reconstructed the complete
saved third-image lemma, fixed-good-base lemma, and terminal endpoint
through EOF. That proof review is distinct from author self-review
of the clearing note and these computational artifacts. The retained
source scope does not become a fresh original Wang-proof read, human
expert review, or proof-assistant verification.

No fresh full regression, checkpoint, historical novelty claim, or
unrestricted cancellation conclusion is asserted by this note.
Frozen pass71 and earlier artifacts and shared metadata are unchanged.
