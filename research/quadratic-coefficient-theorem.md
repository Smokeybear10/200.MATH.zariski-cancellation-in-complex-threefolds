# Stable-coordinate descent for every quadratic coefficient

Let \(P\in\mathbb C[x,y,z]\) have degree at most two, and let
\(H\in\mathbb C[x,y,z]\) be arbitrary. Then

\[
 \boxed{F=P(x,y,z)u+H(x,y,z)\text{ is a stable coordinate}
 \quad\Longrightarrow\quad F\text{ is a coordinate}.}
 \tag{1}
\]

Consequently being a coordinate, a stable coordinate, and an LND slice are
equivalent in this family. There is no degree bound on \(H\).

This is a working theorem assembled from explicit arguments and known
lower-dimensional results. The constituent proofs have separate model
reconstructions, not human expert review. No originality is claimed.

## 1. Exhaustive normalization of the coefficient

Write
\[
 P(v)=v^TAv+b^Tv+c,\qquad A=A^T,\quad v=(x,y,z)^T.
\]

Suppose first that \(b\) is nonzero on the radical \(\ker A\).
Choose a constant radical vector \(n\) with \(b^Tn\ne0\).
In linear coordinates \((r,s,t)\) with \(r\)-direction \(n\),
\[
 P=a r+Q(s,t),\qquad a\ne0.
\]
The triangular change \((r,s,t)\mapsto(P,s,t)\) is a polynomial
automorphism. Thus \(P\) itself can be used as a base coordinate.

If \(b\) vanishes on the radical, it belongs to the image of \(A\).
Translation completes the square and gives \(P=q_r+\gamma\), where
\(q_r\) is a nondegenerate quadratic in \(r=\operatorname{rank}A\)
variables and has no dependence on the other \(3-r\) variables.
Over \(\mathbb C\), the following list is exhaustive, up to affine
changes, nonzero rescaling, and renaming variables.

| Coefficient case | Normal form or reduction | Proof |
|---|---|---|
| Nonzero radical-linear term | \(P\) is a coordinate | Univariate coefficient theorem after a triangular change |
| Rank zero | \(P\) constant, including zero | Direct shear, or known three-variable stable descent |
| Rank one | \(P=p(x)\), \(\deg p\le2\) | Univariate coefficient theorem, repeated roots allowed |
| Rank two, nonzero centered constant | \(P=xy-1\) | Hyperbolic coefficient proof |
| Rank two, zero centered constant | \(P=xy\) | Two crossing-divisor branches |
| Rank three, nonzero centered constant | Smooth affine quadric | Nonzero rational cohomology excludes stability |
| Rank three, zero centered constant | \(P=xy-z^2\) | Integral torsion excludes stability |

Nonzero rescaling of \(P\) is absorbed by scaling \(u\). A polynomial
change in \(x,y,z\) extends by fixing \(u\) and does not affect coordinate,
slice, or stable-coordinate status. It may raise the degree of \(H\),
which causes no problem because that degree is unrestricted.

## 2. The elementary and previously established cases

If \(P\) is a nonzero constant, solve for \(u\) directly.
If \(P=0\), then \(F=H(x,y,z)\) is a stable coordinate of the
three-variable ring after including \(u\) among the stabilizing
variables. Stable-coordinate descent in three variables is a known
theorem.[^1]

If \(P\) is a coordinate, use it as \(x\). If \(P\) has rank one
and no radical-linear term, it is already a polynomial in one variable.
In both cases,
\[
 F=p(x)u+H(x,y,z),\qquad p\ne0.
\]
The [univariate coefficient proof](multiple-root-linear-pass.md)
forces each root specialization of \(H\) to be a plane coordinate.
Maubach's Theorem 4.5 then gives an actual coordinate, with arbitrary
root multiplicities.[^2]

## 3. The hyperbolic divisor

For \(P=xy-1\), the
[full hyperbolic proof](hyperbolic-coefficient-pass.md) gives the
exact criterion
\[
 H(x,x^{-1},z)=c x^kz+B(x),\quad
 c\ne0,\quad k\in\mathbb Z,\quad B\in\mathbb C[x,x^{-1}].
\]

Its necessity uses all the fibers, not just Euler characteristic.
The compact-support sequence forces every restricted curve on
\(P=0\simeq\mathbb C^*\times\mathbb A^1\) to be \(\mathbb C^*\).
The unit \(x\) on such a curve is a nonconstant monomial parameter,
and hence has no critical point. This forces \(H_z|_{P=0}\) to be
a unit, yielding the displayed normal form.

For sufficiency, lift it to
\[
 H=az+b+PK,\qquad (P,a)=\mathbb C[x,y].
\]
After \(U=u+K\), an explicit determinant-one matrix over
\(\mathbb C[x,y]\) completes \(PU+az\) to coordinates.

## 4. The crossing divisor

For \(P=xy\), put \(h(z)=H(0,0,z)\). There are exactly two branches.

If \(h\) is nonconstant, the
[crossing-curve argument](crossing-nonconstant-pass.md) forces
\[
 H=az+b+B(x)+C(y)+xyK,\qquad a\ne0.
\]
Indeed, generic plane strata meet at \(\deg h\) points. The
compact-support sequence and Mayer–Vietoris force exactly one
intersection and two affine-line strata. Plane-line rectification,
together with the linear restriction along their shared axis, makes
both restrictions affine-linear in \(z\).[^3] The resulting formula makes
\(F\) a coordinate after the shear \(u\mapsto u+K\).

If \(h=b\) is constant, the
[disjoint-strata argument](crossing-coefficient-pass.md) forces,
up to interchanging \(x,y\),
\[
 H=ay+cx^kz+B(x)+xyK,\quad
 a,c\ne0,\quad k\ge1,\quad B(0)=b.
\]
For every \(\lambda\ne b\), one plane stratum is an affine line
and the other is \(\mathbb C^*\). Units and tangent directions
force the displayed form. After \(V=u+K\),
\[
 F=(a+xV)y+cx^kz+B(x).
\]
The two coefficients \(a+xV,cx^k\) form a unimodular pair over
\(\mathbb C[x,V]\); the appendix gives their exact Bézout coefficients
and a polynomial inverse.

## 5. Rank three is impossible for a stable coordinate

For a smooth affine-quadric coefficient divisor \(D\), the
[rational obstruction](quadratic-coefficient-obstruction.md) gives
\[
 H_c^2(D;\mathbb Q)=\mathbb Q
 \quad\Longrightarrow\quad
 \mathbb Q\hookrightarrow H_c^3(F^{-1}(\lambda);\mathbb Q)
\]
for generic \(\lambda\). The generic closed curve stratum cannot
remove this class. This contradicts stability.

For the cone \(D=V(xy-z^2)\), the
[integral obstruction](quadric-cone-obstruction.md) uses
\[
 D\simeq_{\mathrm{top}}\mathbb C^2/\{\pm1\},
 \qquad H_c^3(D;\mathbb Z)=\mathbb Z/2.
\]
Stability would force the first compactly supported cohomology of
a generic smooth affine curve to be \(\mathbb Z/2\).
That group is free abelian, a contradiction.

Both arguments allow arbitrary \(H\), including constant restrictions
to the divisor. The cone argument is not replaceable by rational
Euler characteristic.

The coefficient cases in Section 1 are exhaustive, completing (1).

## 6. Verification and scope

The independent [exact checker](../verify_quadratic_coefficients.py)
tests both compositions of the explicit positive inverse maps,
Laurent lifts, Bézout identities, and parameter guards. These are
finite algebraic checks. The all-degree necessities are the written
topology and algebra arguments linked above, not inferred from a grid.

This theorem only handles a polynomial linear in one chosen variable
with quadratic coefficient in the other three. Any deduction about
all cubic polynomials still requires a separate theorem supplying
that presentation. The full cancellation problem also requires
control of slice polynomials of unrestricted degree.

## Sources

[^1]: V. Shpilrain and J.-T. Yu, [*Affine varieties with equivalent cylinders*](https://arxiv.org/html/math/0110324), Proposition 1.1(c) and its proof. The proof explicitly allows arbitrary stabilization beyond three variables.
[^2]: Stefan Maubach, [*The Commuting Derivations Conjecture*](https://www.math.ru.nl/~maubach/Papers/The_Commuting_Dervations.pdf), Theorem 4.5 and Corollary 4.2. The positive univariate-coefficient criterion is attributed to this published result, not claimed as new here.
[^3]: Nguyen Van Chau, [*Polynomial maps of the complex plane with the branched value sets isomorphic to the complex line*](https://math.ac.vn/uploads/files/0202197.pdf), Section 2 and Lemma 1. Records the plane-line rectification input used in the crossing and univariate proofs.
