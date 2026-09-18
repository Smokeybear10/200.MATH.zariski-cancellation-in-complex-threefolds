# A six-shear bypass for the Nagata orbit-degree obstruction

A known polynomial translation admits a useful elementary reduction
with a temporary increase of orbit degree. The explicit construction
below straightens a Nagata coordinate frame in six elementary shears.
It works over the polynomial ring, including the divisor z=0. No
rational coordinate change or converse to the Jacobian criterion is used.

This is a strategy control for the unrestricted cancellation problem,
not a new cancellation theorem. Stable tameness of Nagata's map is
classical. The contribution of this calculation to the investigation is
the exact orbit-degree profile and a reusable polynomial certificate.
No historical novelty is asserted for the factorization or degree data.

## 1. Actual polynomial coordinates

Start in B=C[u,v,z,w], with E=partial_u, and put

\[
\delta=zu+v^2,\qquad
X=u-2v\delta-z\delta^2,\quad Y=v+z\delta,
\quad Z=z,\quad W=w.
\tag{1}
\]

The identity ZX+Y^2=delta gives the polynomial inverse

\[
d=ZX+Y^2,\qquad
u=X+2Yd-Zd^2,\quad v=Y-Zd,\quad z=Z,\quad w=W.
\tag{2}
\]

Substitution verifies both orders. In particular the original action
is an actual locally nilpotent derivation with a global slice, and
its kernel is already C[v,z,w]. Its E-degrees in the supplied frame
are (2,1,0,0). An elementary move means replacing one current
coordinate F_i by c F_i+H in the other three current coordinates,
with c a nonzero complex constant. It has its elementary inverse.

The separate [minimization argument](coordinate-degree-elementary-descent-obstruction-pass124.md)
proves that no one
such move strictly reduces the sum of these E-degrees. That does not
rule out a sequence of degree-preserving moves followed by a decrease.
The present proof does not require that stronger assertion.

## 2. Six moves with a complete degree trace

All right-hand sides in the following table use the current tuple,
after the preceding row. Every unlisted coordinate is fixed.

| Step | Elementary replacement | E-degree tuple | Sum |
| --- | --- | --- | --- |
| 0 | Initial tuple (1) | (2,1,0,0) | 3 |
| 1 | W <- W+ZX+Y^2 | (2,1,0,1) | 4 |
| 2 | X <- X+2WY-W^2Z | (1,1,0,1) | 3 |
| 3 | Y <- Y-WZ | (1,0,0,1) | 2 |
| 4 | W <- W-ZX-Y^2 | (1,0,0,0) | 1 |
| 5 | X <- X-2WY-W^2Z | (1,0,0,0) | 1 |
| 6 | Y <- Y+WZ | (1,0,0,0) | 1 |

After step 1, W=w+delta. Steps 2 and 3 give the actual tuple

\[
\bigl(u+2wv-w^2z,\ v-wz,\ z,\ w+\delta\bigr).
\tag{3}
\]

For its first three entries ZX+Y^2=delta still holds. Thus step 4
recovers w. Steps 5 and 6 then recover u and v. This proves the
final tuple is exactly (u,v,z,w). The degree entries follow by
expanding in u; for example delta has u-degree one and the first
entry of (3) has u-degree one with leading coefficient one.

The path's maximum sum is four. It therefore supplies an upper
bound, not a lower bound on every possible elementary path. No
claim about minimal path length or minimum necessary peak is made.
The fourth variable was present from the start; no fifth variable
was adjoined during these steps.

## 3. The same mechanism for polynomial replicas

Let f(Z,T) be any polynomial of positive T-degree m, with nonzero
leading coefficient a_m(Z), and put h=f(z,delta). Replace (1) by

\[
X=u-2vh-zh^2,\qquad Y=v+zh,\qquad Z=z,\quad W=w.
\tag{4}
\]

Again ZX+Y^2=delta. Its inverse is (2) with d replaced by
f(Z,ZX+Y^2). This identity proves actual polynomial invertibility
for every f, without assuming a_m(z) or z invertible. The initial
degree tuple is (2m,m,0,0), since the leading coefficients of X,Y
are respectively -a_m(z)^2 z^(2m+1) and a_m(z) z^(m+1).

Use the six moves in Section 2, but replace ZX+Y^2 in steps 1
and 4 by f(Z,ZX+Y^2). The pairs of X,Y moves preserve ZX+Y^2,
so the intermediate tuple after step 3 is

\[
\bigl(u+2wv-w^2z,\ v-wz,\ z,\ w+h\bigr).
\tag{5}
\]

The final tuple is again (u,v,z,w). The successive degree sums are

\[
3m,\quad4m,\quad2m+1,\quad m+1,\quad1,\quad1,\quad1.
\tag{6}
\]

This is an all-polynomial identity proof, not an extrapolation from
sampled values of m. For constant f the frame is already triangular
over C[z]; it is not included in the positive-m degree formula.

## 4. Meaning for the missing coordinate reduction

The action and its polynomial kernel were known at the start of
this control. Consequently the bypass supplies no coordinate frame
for an arbitrary unknown cylinder. Its implication is methodological:
a reduction that accepts only an immediately degree-decreasing
elementary shear would stop on this recognized example. A candidate
general algorithm needs compound moves, an appropriate look-ahead
rule, or a different proof of termination. Allowing an increase by
itself proves no termination theorem.

Likewise the nonunit leading coefficient cannot be canceled by
replacing X with ZX+Y^2 while fixing Y,Z,W. That map has Jacobian
Z and is not a polynomial automorphism. The six shears explicitly
preserve invertibility on Z=0, where this invalid replacement fails.

The [standalone checker](nagata_degree_bypass_checks_pass124.py)
checks both original inverse orders, each elementary inverse, the
complete six-step identity and degree trace, and the replica family
for several finite polynomial choices. Those finite checks support
the written proof; they do not establish arbitrary-frame entry,
global descent, or the full cancellation conjecture.

## Sources and review scope

The underlying commutator method is classical. Drensky and Yu,
[*Tame and wild coordinates of K[z][x,y]*](https://hub.hku.hk/bitstream/10722/48401/1/63202.pdf),
Transactions of the AMS 353 (2001), 519-537, prove Theorem3.6(iii)
on printed page533 by adjoining a variable and composing its
translation with a triangular exponential. They explicitly attribute
that method to Martha K. Smith,
[*Stably tame automorphisms*](https://doi.org/10.1016/0022-4049(89)90158-8),
Journal of Pure and Applied Algebra 58 (1989), 209-212.

The displayed commutator proof, its composition convention, and the
Smith reference were directly read in the accessible Drensky--Yu
paper. The original Smith publisher page returned HTTP403; no fresh
read of Smith's full paper is claimed. The six elementary identities
and their orbit-degree trace above are independently explicit. They
instantiate this old method, rather than establish a new stable-
tameness theorem. No ordinary-spatial-degree reduction theorem is
being applied to the different E-degree measure used here.

This is a private AI-written research control, not human expert
review, formal proof verification, or a cleared novelty claim.
