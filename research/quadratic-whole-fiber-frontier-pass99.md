# Whole fiber equations and constant normal rows

The original volume identity now determines the entire scheme of
a collapsed quadratic double fiber when the speed normal is
nonzero. It also rules out the nonconstant zero-normal conormal
rows in that sector. These conclusions strengthen the previous
parallel-plane and degree-two row restrictions without proving
that the remaining fibers cannot exist.

The full corrected complex-threefold cancellation question remains
unresolved. Recognition of this supplied frame and its reduction
from an arbitrary sliced action are also unresolved. The field
and correction intended by Luo's email have not been confirmed.

## 1. The supplied original frame

Retain the full hypotheses of [checkpoint98](checkpoint-pass98-working.json):
\[
\begin{gathered}
B=\mathbb C[x_1,x_2,x_3,z]=A[u],\qquad E=\partial_u,
\quad u=Ez/q_0,\quad E^2z=q_0\in\mathbb C^*,\quad E^2x_i=0,\\
S=\ker(N|_A)=\mathbb C[s_1,s_2],\qquad
\mathbf b=Ex_{\rm tr}\in S^3,\quad
L=\mathbf b_{s_1}\times\mathbf b_{s_2},\quad
\Omega=L\cdot\mathbf b\ne0.
\end{gathered}
\tag{1}
\]
N is the specified primitive canonical Jacobian LND, not an
arbitrary derivation sharing these invariants. The actual frame
includes its full kernel, faithful flatness, the retained smooth
factorial contractible threefold, and the generic degree bounds.
Only the fixed-containing profiles (2) and (2,1) remain after97.
The statements below require a collapsed double component and
\(L_0=L(\mathfrak m)\ne0\). In the mixed case98 also makes the
simple component collapsed. No first-normal-action hypothesis is
needed until a case is explicitly distinguished.

## 2. The volume identity acts on the whole fiber

Let \(\mathbf a=x_{\rm tr}-u\mathbf b\in A^3\). Its restriction
to a collapsed component is a constant vector o. The global
identity \(L(s)\cdot\mathbf a=\kappa(s)\in S\) implies
\[
\begin{gathered}
\ell=L_0\cdot x_{\rm tr}-\kappa(\mathfrak m),\qquad
F=\ell-uE\ell,\\
F=(L_0-L(s))\cdot\mathbf a+\kappa(s)-\kappa(\mathfrak m)
 \in\mathfrak mA,\\
E\ell\in\mathfrak m^2\setminus\{0\},\qquad
\boxed{\quad\ell\in\mathfrak mB.\quad}
\end{gathered}
\tag{2}
\]
This is stronger than membership in the radical of the fiber.
It is the key new use of the original volume. The coordinate
ell is genuinely an original affine-linear good coordinate, but
F is only its centered E-invariant in A. Neither is proved
N-invariant, and ell is explicitly not E-invariant.

Complete ell by an original normal Y; in the mixed case take its
values to be zero and one on the two planes. Put G=Y-uEY.
The exact component ideals are then (F,G) and, when present,
(F,G-1). Modulo the double component's ideal square, (2) gives
F=d(s-m) with a nonzero constant row d. Thus its quotient conormal
matrix C(c) satisfies dC=(1,0). Rank one forces its second column
to vanish after a constant base change.

The whole length-two thickening makes the transverse quadratic
coefficient a nonzero constant b at every c. The actual cubic
identity N^3G=0 then gives the normalized conormal and weighted form
\[
\begin{gathered}
\binom{x}{f}\equiv
\begin{pmatrix}1&0\\a_0+a_1c&0\end{pmatrix}
\binom F G\pmod{(F,G)^2},\qquad
\mathfrak m=(x,f),\qquad a_0,a_1\in\mathbb C,\\
f_*=(a_0+a_1c)x+b y^2,\qquad
D_* =\nu(-a_1x\partial_y+2b y\partial_c),\qquad b,\nu\in\mathbb C^*.
\end{gathered}
\tag{3}
\]
Before the affine conclusion, the x-squared coefficient of
D_*^3y is \(2\nu^3b a'a''\), so a is affine.
Zero first normal action is precisely a_1=0. In that case the
entire conormal matrix is constant. All three nonconstant row
spans from the zero-normal theorem98 are therefore excluded when
L(m) is nonzero. They remain possible data only in the unhandled
L(m)=0 sector; no actual realization is claimed there.

The [complete volume-normal proof](quadratic-volume-normal-splitting-pass99.md)
also gives \(NF\in\mathfrak mA\sqrt{\mathfrak mA}\) when all
components are collapsed and \(N^2F\in\mathfrak m^2S\).
Neither inclusion makes its left side zero.

## 3. Exact whole-fiber equations in the original coordinates

Quotient B by the actual coordinate ell from (2), obtaining
\(R=\mathbb C[Y,W,z]\). The remaining fiber ideal has only
height-one associated primes. Indeed the two base parameters
form a regular sequence in B, so the whole fiber is
Cohen--Macaulay and has no embedded associated primes.[^cm]

Each remaining primary ideal contracts from its height-one DVR
as an ordinary prime power in the polynomial UFD R. Its exponent
is the actual generic scheme length. This proves, with
\(H(T)=T^2\) for profile (2) and \(H(T)=T^2(T-1)\) for profile (2,1),
\[
\boxed{\quad
\mathfrak mB=(\ell,H(Y)),\qquad
\mathfrak mA=(F,H(G)),\qquad
A/\mathfrak mA\simeq\mathbb C[G,c]/(H(G)).
\quad}
\tag{4}
\]
The last presentation uses the actual G and c, including the
nilpotents. The original alternative slice sigma specializes to
W plus an affine function of Y. Its finite E-retraction sends z
to the actual invariant \(c=z-q_0u\sigma+q_0\sigma^2/2\).
Ordinary evaluation at sigma=0 proves injectivity, even over the
nonreduced coefficient ring \(\mathbb C[Y]/(H(Y))\).

The [whole-fiber proof](quadratic-whole-plane-fiber-pass99.md)
keeps the primary contraction, multiplicity-preserving polynomial
extension, and nilpotent-safe injectivity separate. The actual
partial \(\partial_z\) now preserves the whole B-fiber ideal,
not just its radical. This does not show that it preserves A or
commutes with E on that whole nonreduced fiber.

## 4. Failed shortcuts and superseded cases

The [parallel-plane Jacobian calculation](quadratic-parallel-plane-normal-pass99.md)
remains valid: the simple plane has nonzero constant successive
transverse coefficients, while their product vanishes on the fixed
double plane. Restricting EY to ell=0 gives divisibility by
\(Y^2(Y-1)^2\), but EY still has a nonzero linear ell term on
the simple plane. Discarding ell does not prove normal-square
membership. Spatial degree is distinct from group-parameter degree.

The earlier
[nonconstant zero-normal compatibility note](quadratic-zero-normal-companion-compatibility-pass99.md)
is now marked as a conditional calculation in an excluded actual
sector. Its NF inclusion is superseded by the stronger consequence
of (2), without that first-normal-action hypothesis. It must not
be counted as evidence that the excluded sector exists.

An exact intrinsic polynomial control has leading D_*^2G=0 but
full N^2G=-2X^2 nonzero. Thus the affine leading translation in
(3) cannot be substituted for a square-zero identity in A.
Likewise the complete fiber presentation (4) does not present A
itself as a polynomial ring.

## 5. Verification and the next proof gap

The [canonical finite capture](verification-pass99-working.json)
passes one method covering the weighted coefficient formula,
affine positives, higher-degree negatives, constant-left-inverse
matrix identities, and the intrinsic full-square boundary.
These are finite symbolic controls, not verification of the
universal geometric proofs. The [proof audit](proof-audits-pass99-working.md)
records the separate reconstructions and their limits.

~~~sh
/opt/anaconda3/bin/python -m unittest -v research.quadratic_volume_normal_checks_pass99
~~~

The next task is to compute the actual induced actions on the
whole rings in (4), retaining their nilpotents, and compare them
with the third good generator's exact degree bound. Any claim
about the entire threefold still needs an actual global argument.
The L(m)=0 sector and noncollapsed whole double fibers remain
untreated by these new results.

No general recognition, arbitrary-frame reduction, human expert
review, Lean certificate, historical novelty clearance, publication
or external contact is asserted. The [checkpoint99](checkpoint-pass99-working.json)
is bookkeeping evidence, not a theorem verifier.

## Sources

[^cm]: The Stacks Project,
    [Lemma 10.103.7, tag 0BUS](https://stacks.math.columbia.edu/tag/0BUS),
    Cohen--Macaulay modules have no embedded associated primes.
    The complete displayed statement and proof were reread for
    this application; the entire background theory was not newly
    reconstructed. The original-volume and actual-frame inputs
    are the linked retained proofs88--98.
