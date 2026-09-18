# Monomial-coefficient slice descent and integral obstructions

## Result and scope

There is a complete working argument for the following restricted
cancellation criterion:

\[
\boxed{\begin{gathered}
F=x^r y^s u+H(x,y,z)\in\mathbb C[x,y,z,u],\qquad r,s\ge1,\\
D(F)=1\text{ for a locally nilpotent derivation on this same ring}\\
\Longrightarrow
F\text{ is a coordinate and }\ker D\cong\mathbb C^{[3]}.
\end{gathered}}
\tag{1}
\]

There is no degree bound on \(H\). The theorem includes every repeated
crossing coefficient \(xy^2\), but not every cubic coefficient and not
every quartic slice. Its proof combines an explicit finite inverse,
integral topology, and a published affine-plane fibration theorem.
Originality is not established.

The unrestricted target
\[
X\times\mathbb A^1_{\mathbb C}\cong\mathbb A^4_{\mathbb C}
\quad\Longrightarrow\quad X\cong\mathbb A^3_{\mathbb C}
\]
is **not solved here**. Nothing in (1) shows that every possible slice
admits this presentation.

The distinction between an original slice and a stable coordinate is
essential. Requiring every stable coordinate in this family to be a
coordinate would include the first Vénéreau polynomial, a harder
embedding question. The original cancellation target does not require
proving that stronger statement.

## 1. Why the original slice hypothesis matters

Put \(T=\mathbb C[x,y,z,u]\). The slice theorem gives
\[
D(F)=1\quad\Longrightarrow\quad T=K[F],\qquad K=\ker D.
\tag{2}
\]
Consequently \(T/(F-\lambda)\cong K\) for every scalar \(\lambda\).
To prove \(K\) polynomial, it is therefore enough to identify a single
fiber of this specific polynomial map as affine three-space.

A slice also becomes a coordinate after one stabilization. If \(W\)
is another indeterminate, \(K[W]\cong K[F]=T\), so
\(T[W]=K[W][F]\) is a polynomial ring with \(F\) as a coordinate.
Every fiber of a stable coordinate is smooth and contractible because
its product with an affine space is an affine space.

The reverse implication, from a slice on a stabilized ring to a slice
on the original ring, is not used and is not established. This is exactly
where a superficially similar argument for a general stable coordinate
would fail.

## 2. The two possible restrictions along the crossing

Write \(h(z)=H(0,0,z)\). On any fiber \(X_\lambda=V(F-\lambda)\),
the open set where \(xy\ne0\) is
\[
U\cong(\mathbb C^*)^2\times\mathbb A^1.
\]
The reduced closed complement is a cylinder over the two plane curves
\[
C_x=V(H(0,y,z)-\lambda),\qquad
C_y=V(H(x,0,z)-\lambda).
\]
These reduced sets do not depend on the exponents \(r,s\).
Integral compact-support cohomology and the closed-open sequence force
\[
H_c^1(C_x\cup C_y)=\mathbb Z,\qquad
H_c^2(C_x\cup C_y)=\mathbb Z^2.
\tag{3}
\]

### Nonconstant intersection restriction

If \(h\) has positive degree \(d\), take a regular value where the plane
curves are smooth and meet in \(d\) distinct points. Their top cohomology
in (3) makes each curve connected. The compact-support Mayer–Vietoris
sequence gives
\[
0\longrightarrow\mathbb Z^d\longrightarrow\mathbb Z
\longrightarrow H_c^1(C_x)\oplus H_c^1(C_y)\longrightarrow0.
\]
Hence \(d=1\), and both plane curves are affine lines. Plane-line
rectification, together with their common linear restriction on the
intersection axis, yields exactly
\[
H=az+b+B(x)+C(y)+xyR(x,y,z),\qquad a\ne0,
\quad B(0)=C(0)=0.
\tag{4}
\]
The complete justification, including reduced equations and the relative
plane-coordinate lemma, is in the
[repeated-crossing proof](research/repeated-crossing-pass.md).

There is a direct inverse for every polynomial (4). Let
\[
p=x^ry^s,\quad n=xy,\quad E=b+B(x)+C(y),\quad N=\max(r,s).
\]
Define
\[
I_0(S)=\frac{S-E}{a},\qquad
I_{j+1}(S)=\frac{S-E-nR(x,y,I_j(S))}{a}.
\]
After \(N-1\) updates, both errors are divisible by \(n^N\), hence by \(p\):
\[
H(I(S))-S\in(p),\qquad I(H(z))-z\in(p).
\]
The coordinates and their inverse are
\[
(x,y,z,u)\longmapsto
\left(x,y,F,\frac{z-I(F)}p\right),
\]
\[
z=I(S)+pV,\qquad
u=\frac{S-H(I(S)+pV)}p.
\tag{5}
\]
Both quotients are polynomials by the two displayed congruences.
The recurrence is finite polynomial arithmetic, not a convergent power
series argument. This branch proves stable-coordinate descent itself.

### Constant intersection restriction

If \(h=b\), the generic plane curves are disjoint. Equation (3) makes
one an affine line and the other a punctured affine line.
An affine-line component on which a base coordinate is a unit must have
that coordinate constant. Infinitely many such fibers force one plane
restriction to be \(ay+b\), or its exchanged version.

The other restriction needs more than rational cohomology. On a generic
fiber the two closed cylinders are disjoint smooth divisors. The integral
Gysin sequence contains an isomorphism
\[
H^2(U;\mathbb Z)\longrightarrow H^1(C_x\sqcup C_y;\mathbb Z),
\qquad \mathbb Z\longrightarrow\mathbb Z.
\]
On the punctured-line component, the unit base coordinate is \(dt^m\).
The residue map is multiplication by \(m\), up to sign. Therefore
\(|m|=1\). Its projection to the base punctured line is an isomorphism,
forcing the remaining plane restriction to be linear in \(z\).
The resulting necessary forms are
\[
\begin{aligned}
\mathrm A:\quad&H=ay+cx^kz+B(x)+xyR(x,y,z),\\
\mathrm B:\quad&H=ax+cy^kz+C(y)+xyR(x,y,z),
\end{aligned}
\tag{6}
\]
where \(a,c\ne0\), \(k\ge1\), and \(B(0)=C(0)=b\).

The exponents in the coefficient do not multiply this residue map.
At the chosen regular value, the quotients by \((x)\) and \((y)\)
are reduced, so each function has divisor order one. The full integral
argument is independently reconstructed in the
[residue audit](research/repeated-crossing-independent-audit.md).

## 3. Closing every constant-axis slice

Consider form A. Fix \(\lambda\), and project
\[
A_\lambda=T/(F-\lambda)
\]
to the base \(\mathbb C[x]\). At \(x=0\), the relation is
\(ay+B(0)=\lambda\), so the base fiber is exactly
\(\mathbb C[z,u]\), including when \(\lambda=B(0)\).

After inverting \(x\), the coefficient \(cx^k\) of \(z\) is a unit.
The same finite-inverse construction as (5), now modulo \(x^ry^s\)
over \(\mathbb C[x,x^{-1},y]\), gives
\[
A_\lambda[1/x]\cong\mathbb C[x,x^{-1}]^{[2]}.
\tag{7}
\]
This proves the generic fiber as well as all nonzero base fibers.

The defining equation is primitive and linear in \(u\): neither \(x\)
nor \(y\) divides its remaining coefficient. Its quotient is a domain,
and the map from \(\mathbb C[x]\) is injective. Thus \(A_\lambda\)
is torsion free, hence flat, over this PID. It is finitely presented,
and every residue-field fiber is an affine plane.

The classical affine-plane fibration theorem over a characteristic-zero
PID now gives \(A_\lambda\cong\mathbb C[x]^{[2]}\).[^1]
Kaliman, Vénéreau and Zaidenberg's residual-plane theorem also applies
directly and gives the same conclusion.[^2] Form B uses the base \(y\)
instead. These are published closing theorems, not new fibration results.

Finally, (2) identifies \(A_\lambda\) with the actual kernel \(K\).
Hence \(K\cong\mathbb C^{[3]}\) and \(T=K[F]\) makes \(F\) a
coordinate. No assumption \(D(x)=0\) or \(D(y)=0\) was needed.
The [full slice-descent appendix](research/repeated-crossing-slice-descent.md)
records each hypothesis and both classical closure routes.

This proves (1). It also explains why merely proving individual fibers
to be affine spaces would not settle the corresponding embedding problem:
without (2), their coordinate systems need not assemble into a coordinate
system for the polynomial map.

## 4. An infinite family missed by smoothness and Euler tests

For integers \(r\ge1,\ s\ge2,\ q\ge2\), set
\[
G_{r,s,q}=x^ry^su+y+xz^q.
\tag{8}
\]
Every fiber is smooth. Off \(xy=0\), the derivative in \(u\) is nonzero;
on either coordinate plane the derivative in \(y\) is one.
Every fiber also has compactly supported Euler characteristic one.
Nevertheless, for every \(\lambda\ne0\),
\[
H^j(G_{r,s,q}^{-1}(\lambda);\mathbb Z)=
\begin{cases}
\mathbb Z,&j=0,\\
\mathbb Z/q,&j=3,\\
0,&\text{otherwise}.
\end{cases}
\tag{9}
\]
Thus none of these polynomials is a stable coordinate or an LND slice.

Here is the obstruction explicitly. The closed divisors of a nonzero
fiber are
\[
E_x=\{x=0,y=\lambda\}\cong\mathbb A^2,\qquad
E_y=\{y=0,xz^q=\lambda\}\cong\mathbb C^*\times\mathbb A^1.
\]
The complement is \((\mathbb C^*)^2\times\mathbb A^1\).
Both divisors are reduced. The first integral residue matrix is the
identity on the \(x,y\) meridians, while the next map is multiplication
by \(q\), since \(x=\lambda z^{-q}\) on \(E_y\).
Exactness gives (9). Rational coefficients erase its only nontrivial
reduced cohomology group.

At zero, the two boundary planes meet and the divisor calculation changes.
Their reduced union has Euler characteristic \(1+1-1=1\), which proves
the claimed Euler statement at that value. Equation (9) is not asserted
for the zero fiber. The smallest example is the quartic
\(xy^2u+y+xz^2\), with \(\mathbb Z/2\) in ordinary third cohomology.

## 5. Other routes and their exact limits

The [degree-three theorem](deep-pass-07.md) remains a complete working
argument. Its singular locus at infinity is now explicitly the Jacobian
locus of the possibly nonreduced leading form. Using the singular locus
of reduced support instead would be false for the coordinate \(x+y^3\).
The [additional hostile audit](research/cubic-second-hostile-audit.md)
records this correction and reconstructs the other branches.

For a quartic monic quadratic in one variable, square completion gives
\(s^2+G(v)\), but \(G\) can have degree six. Stability forces every
surface \(G=\lambda\) to be smooth and mod-2 acyclic by Smith theory.[^3]
The general such surface is integrally acyclic by the global
Sebastiani–Thom theorem.[^4] Neither conclusion makes it an affine plane.
An involution-compatible LND slice would suffice for coordinate descent,
but averaging a slice derivation need not preserve local nilpotence.
The [monic-branch note](research/quartic-quadratic-variable-pass.md)
contains an exact quartic counterexample to that averaging shortcut.

For two intrinsic commuting additive actions, the global closure and
saturation statements already appear in Derksen, van den Essen and
Maubach.[^5] The [saturation calculation](research/saturated-rank-two-pass.md)
shows that the standard pair on the Russell cubic is already saturated
over its one-variable invariant ring and still loses rank on a fiber.
Saturation alone therefore does not resolve the global obstruction.
This does not decide whether that variety has a polynomial cylinder.

There is also a general coefficient-support obstruction. If
\(D=V(P)_{\mathrm{red}}\subset\mathbb A^3\) has \(H_c^2(D;\mathbb Z)\ne0\),
then \(Pu+H\) cannot be stable for any \(H\). At a suitable value, the
closed center is an affine curve or empty, so its cylinder has zero
\(H_c^2\). The closed-open sequence injects
\(H_c^2(D)\cong H_c^3(\mathbb A^3\setminus D)\) into the fiber's
\(H_c^3\), contradicting stability. The
[support proof](research/repeated-crossing-slice-independent-audit.md)
checks purity of the center and computes \(H_c^2(D)=\mathbb Z\) for
both \(P=xyz\) and \(P=z(xy-1)\). Positive multiplicities do not
change this exclusion.

## 6. Verification, attribution, and remaining target

The exact suite contains 175 passing tests across thirteen suites,
including fifteen new checks of finite inverses, localized inverses,
residue integers, the averaging counterexample and scope controls.
The new suite is
[verify_repeated_crossing.py](verify_repeated_crossing.py); the complete
commands are in [README.md](README.md). The algebraic topology and
universal statements are written proofs, not conclusions from those
finite tests. No proof-assistant formalization or human expert review
is present.

The first Vénéreau polynomial is
\[
v_1=xy^2u+y+x^2z+xyz^2.
\]
It has total degree four and is known to be one-stable. A 2022 primary
publication reports its coordinate question unresolved.[^6] The
[literature audit](research/quartic-literature-pass.md) located no later
resolution through its stated search date, but does not certify current
openness. The known affine-space fibers of this example are not a new
result. Nor is the implication from a hypothetical original slice on
this example to a coordinate a solution of its coordinate question.

The remaining quartic reduction permits
\[
A(v)u^2+B(v)u+C(v),\qquad
\deg A\le2,\quad\deg B\le3,\quad\deg C\le4.
\]
The theorem above closes the \(A=0\) cases whose cubic coefficient
reduces to a monomial crossing, in addition to the preceding quadratic
coefficient theorem. It does not cover arbitrary cubic coefficients,
nonconstant \(A\), or the whole constant-nonzero-\(A\) branch.
The unrestricted problem also has no general bound on total slice degree.
Those are the remaining mathematical obligations; none is replaced by a
claim of novelty, a test count, or a successful special case.

## Sources

[^1]: Janaki Raman Babu and Prosenjit Das, [*Structure of \(\mathbb A^2\)-fibrations having fixed point free locally nilpotent derivations*](https://arxiv.org/html/2001.07632v5), Section 1 and the discussion following Problem 4.6. The source states the PID consequence of Sathaye's DVR theorem and Bass–Connell–Wright globalization.

[^2]: Shulim Kaliman, Stéphane Vénéreau and Mikhail Zaidenberg, [*Simple birational extensions of the polynomial ring \(\mathbb C^{[3]}\)*](https://arxiv.org/pdf/math/0104204), arXiv version 2 (2001), definition 4.19, Theorem 4.23 and proof 4.26.

[^3]: Peter Symonds, [*Smith Theory for algebraic varieties*](https://personalpages.manchester.ac.uk/staff/peter.symonds/preprints/smith.pdf), *Algebraic & Geometric Topology* 4 (2004), 121–131, Section 4 and its ordinary-cohomology formulation.

[^4]: András Némethi, [*Generalized local and global Sebastiani-Thom type theorems*](https://www.numdam.org/article/CM_1991__80_1_1_0.pdf), *Compositio Mathematica* 80 (1991), 1–14, Theorem G1 and Example 3.4(a).

[^5]: Harm Derksen, Arno van den Essen and Stefan Maubach, [*A commuting derivations theorem on UFD's*](https://arxiv.org/pdf/0806.2038), initial arXiv version 2008, Theorem 2.1, Example 1.1, Lemma 3.7 and the following question.

[^6]: Jérémy Blanc and Pierre-Marie Poloni, [*Bivariables and Vénéreau polynomials*](https://afst.centre-mersenne.org/item/10.5802/afst.1724.pdf), published 2022, Introduction, Lemma 2.1 and Proposition 2.3. The distinction between a degree-three bundle transition and the polynomial's degree four is material.
