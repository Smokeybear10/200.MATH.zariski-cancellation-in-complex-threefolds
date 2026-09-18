# Recognition for the supplied full mixed-quartic initial kernel

Status: restricted working theorem. The conic exclusion219 completes
the line/conic analysis begun in217. Under the exact supplied-frame
hypotheses below, the original action fixes an ambient coordinate and
its invariant ring is a polynomial three-ring.

This is not a solution of unrestricted complex-threefold cancellation.
No result here puts an arbitrary cancellation instance into this frame.
There is no human expert review, formal verification, or novelty clearance.

## 1. Precise statement

Let X,Y,Z,W be actual polynomial coordinates, and suppose
\[
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad
A=\ker E,\qquad \deg_E(X,Y,Z,W)=(1,1,2,2).
\tag{1}
\]
These are degrees in the actual slice variable u, not ordinary degrees
of the coefficients of E. Define the nonzero leading coefficients
\[
a=EX,\qquad b=EY,\qquad e_0=E^2Z/2,\qquad h_0=E^2W/2.
\tag{2}
\]
For an independent variable s, assume the full initial evaluation map is
\[
\begin{gathered}
\theta_0:\mathbb C[\mathsf X,\mathsf Y,\mathsf Z,\mathsf W]\longrightarrow A[s],
\\
\theta_0(\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
       =(as,bs,e_0s^2,h_0s^2),\\
\ker\theta_0=(\mathsf Z\mathsf W-\mathsf X^2\mathsf Y^2).
\end{gathered}
\tag{3}
\]
The source has weights (1,1,2,2). A single identity
e0 h0=a^2 b^2 is not the full-kernel hypothesis.

**Working theorem.** Under (1)--(3), E fixes an ambient polynomial
coordinate of B, and
\[
\boxed{A\simeq\mathbb C^{[3]}.}
\tag{4}
\]
No minimum-degree frame, unit speed, rational coefficient field or
additional realization hypothesis is silently imposed.

## 2. Exact reduction from the actual frame

The actual selected-chart construction in
[mixed projection217](rank-two-mixed-ratio-projection-reduction-pass217-working.md)
uses the literal original partial derivative with respect to Z.
It supplies
\[
\begin{gathered}
0\ne N=[u^3](\partial_Z|_A),\qquad
L=\operatorname{Frac}(\ker_A N),\qquad A_L=L[v],\quad Nv=1,\\
t=b/a,\qquad \rho=h_0/a^2,\qquad q=e_0/a^2=t^2/\rho,\qquad
[L:\mathbb C(t,\rho)]<\infty,\\
Y=y+tX,\quad W=w+\vartheta X+\rho X^2,\quad
Z=z+\sigma X+(t^2/\rho)X^2,\\
L[y,z,w]=L[v],\qquad J_0=-a^3\in L^* .
\end{gathered}
\tag{5}
\]
Here t,rho are algebraically independent. The actual nonzero scalar
Jacobian, exact coefficient field and whole-line return are derived
inputs, not consequences of a formal parametrization.

The universal potentials give a return polynomial R in L[v].
The [zero-return exclusion217](rank-two-mixed-ratio-zero-return-exclusion-pass217-working.md)
rules out R=0. In brief, the scalar determinant and complete potentials
would make the actual auxiliary derivation nice; its required fixed
linear row contradicts independence of the ratio and its square.
This does not assert that a nonzero R is root-free.

For R nonzero, the complete
[projection argument217](rank-two-mixed-ratio-projection-reduction-pass217-working.md)
proves L[y,theta]=L[v], where theta denotes vartheta, and the
irreducible plane component is a line or a conic. Its degree exclusions
use the full potentials and calibrated cofactor identities. Normality
of the projected ring is not assumed in advance.

## 3. Exhausting the two projected possibilities

Every line direction is handled in
[line recognition217](rank-two-mixed-ratio-line-recognition-pass217-working.md).
One direction is impossible; another becomes constant second projection
after an actual good-coordinate interchange. In that remaining chart,
the complete scalar equations force a complex slope. An actual polynomial
shear, primitive division and explicit auxiliary-slice inverse maps give
a polynomial three-variable auxiliary kernel.

The original E acts on that actual three-ring. The precise
three-variable fixed-coordinate theorem used in the line proof produces
an E-invariant coordinate that is also a coordinate of B. The regular
kernel theorem then yields (4), with regularity supplied by the global
slice Eu=1. These are original-ring arguments, not descent of a variable
over L.

It remains to rule out the conic. The
[quadratic reduction217](rank-two-mixed-ratio-quadratic-graph-reduction-pass217-working.md)
strengthens the cofactor divisor and identifies two radial branches.
An actual X/Y interchange in one of them makes all projected intercepts
at most quadratic. All quantities are rebuilt in the changed chart.
The nonzero cubic formula excludes reentry into its old branch, leaving
the normalized case II used in218.

The radial and next-Jacobian218 arguments force C to be a nonzero complex
constant. The [zero-M argument218](mixed-conic-zero-M-jacobian-exclusion-pass218-working.md)
rules out M=0 by evaluating the already differentiated scalar determinant
at an exact field point. The independent
[lower-potential proof218](mixed-conic-lower-potential-radial-restrictions-pass218-working.md)
then gives epsilon=delta_h and quadratic G without a rational-field
assumption. The [cofactor-order note218](mixed-conic-return-cofactor-order-dichotomy-pass218-working.md)
also identifies the surviving cofactor as a scalar multiple of R; this
extra restriction is not needed for the final exclusion.

Finally [the complete conic exclusion219](mixed-conic-final-jacobian-exclusion-pass219-working.md)
uses the full cubic and quadratic Jacobian coefficients to integrate
all remaining function coefficients into explicit complex-constant
polynomials. Its structural factorization forces a nonzero quadratic
relation among three generically invertible affine-linear combinations
of Y,Z,W over C(X). Clearing denominators gives a nonzero original
polynomial relation, contradicting (1).

Thus the conic is impossible, and all surviving cases are covered by
the original-ring line recognition. This proves the stated restricted
working theorem.

## 4. What the theorem does not establish

The supplied time profile and entire initial ideal are essential. There
is no theorem here that every globally sliced derivation admits this
profile or this leading kernel. Other leading kernels and arbitrary
frame entry are not resolved by the conic contradiction.

The full goal is still the unrestricted implication
A[u] isomorphic to C^[4] implies A isomorphic to C^[3], under the
unconfirmed interpretation of the professor's intended question.
The restricted theorem is evidence toward that investigation, not a
replacement for its objective.

The linked working proofs have written AI reconstructions and separate
finite-algebra controls. Checkers establish their stated identities,
not actual-chart existence, the published recognition theorems, or
formal proof-assistant verification. Final execution and packet
provenance are recorded separately; no earlier packet is expanded
retroactively.
