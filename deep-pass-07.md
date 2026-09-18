# Stable-coordinate descent through degree three in four variables

## Result

The new working proof reaches a degree-bounded conclusion:

\[
 \boxed{\begin{gathered}
 F\in\mathbb C[x_1,x_2,x_3,x_4],\quad \deg F\le3,\\
 F\text{ becomes a coordinate after adjoining finitely many variables}\\
 \Longrightarrow F\text{ is already a coordinate}.
 \end{gathered}}
 \tag{1}
\]

In particular, if a locally nilpotent derivation \(D\) on
\(\mathbb C[x_1,x_2,x_3,x_4]\) has a slice \(s\) of degree at most three,
then
\[
 \ker D\simeq\mathbb C^{[3]}.
 \tag{2}
\]

The proof combines a projective-boundary obstruction with an exhaustive
classification of quadratic coefficients. The latter even allows the
remaining polynomial to have arbitrary degree. The detailed arguments
and separate model reconstructions are linked below.

This is **not a solution of the full cancellation conjecture**. An arbitrary
cylinder isomorphism need not give a slice of degree at most three, and no
degree-reduction theorem has been proved here. The result has no human
expert review, no proof-assistant certificate, and no established novelty.
A proof-specific literature audit is part of this pass, not a substitute
for those checks.

## 1. Why a slice supplies the stable-coordinate hypothesis

If \(D(s)=1\), the slice theorem gives \(B=K[s]\), where \(K=\ker D\)
and \(B=\mathbb C^{[4]}\). After adjoining \(t\), the ring \(K[t]\)
is isomorphic to \(K[s]\), hence is a four-variable polynomial ring.
Therefore \(B[t]=K[t][s]\) is a polynomial ring with \(s\) as one
coordinate. This implication is standard in the stable-coordinate
formulation of cancellation.[^1]

For any stable coordinate \(F\), every fiber \(X_\lambda=V(F-\lambda)\)
satisfies
\[
 X_\lambda\times\mathbb A^N\simeq\mathbb A^{N+3}.
\]
It follows that every fiber is smooth and contractible, its units are
constant, and
\[
 H_c^j(X_\lambda;\mathbb Z)=
 \begin{cases}\mathbb Z,&j=6,\\0,&j\ne6.\end{cases}
 \tag{3}
\]
In particular \(F\) has no critical point and every fiber has compactly
supported Euler characteristic one.

## 2. The missing cubic reduction

Write a genuine cubic as \(F=f_3+f_2+f_1+f_0\), with \(f_i\)
homogeneous of degree \(i\). We prove that there is a projective point
\[
 p\in\operatorname{Sing}V(f_3)\subset\mathbb P^3
 \quad\text{such that}\quad f_2(p)=0.
 \tag{4}
\]

The singular locus here is the Jacobian locus of the possibly nonreduced
hypersurface scheme defined by \(f_3\), not of its reduced support.
This distinction matters, for example, when \(f_3=y^3\).

If the singular locus is positive-dimensional, it meets the degree-two
hypersurface \(V(f_2)\) by projective dimension theory. If \(f_2=0\)
identically, every singular point works.

Suppose instead that no point in (4) exists. The singular locus of
\(S=V(f_3)\subset\mathbb P^3\) must then be finite, possibly empty.
The cubic surface is reduced: a repeated component would give a
positive-dimensional singular locus. Likewise, distinct components
would intersect along a curve, so in the finite-singularity case it
is irreducible.

For every \(\lambda\), the projective closure of the affine fiber is
\[
 Y_\lambda=
 V\!\left(f_3+w f_2+w^2 f_1+w^3(f_0-\lambda)\right)
 \subset\mathbb P^4.
\]
Its gradient along \(w=0\) is \((\nabla f_3,f_2)\).
The contrary assumption makes \(Y_\lambda\) smooth at infinity.
It is smooth on the affine chart because \(F\) has no critical point.
Thus \(Y_\lambda\) is a smooth cubic threefold.

The Euler characteristics of a smooth cubic threefold and a smooth
cubic surface are respectively \(-6\) and \(9\). The usual
hypersurface formula gives these values directly; they can also be
computed from the tangent-bundle Chern class.[^2]
For a cubic surface with isolated singularities, smoothing changes
Euler characteristic by the sum of the local Milnor numbers:
\[
 \chi(S)=9-\sum_{p\in\operatorname{Sing}S}\mu_p.
 \tag{5}
\]
The minus sign is essential and is exactly the complex-dimension-two
case of the cited formula.[^2]

The polar-degree identity gives
\[
 0\le\deg(\nabla f_3)=2^3-\sum_p\mu_p,
 \qquad \sum_p\mu_p\le8.
 \tag{6}
\]
This identity allows polar degree zero, so cones are not omitted.[^3]
Since \(X_\lambda=Y_\lambda\setminus S\), additivity now gives
\[
 \chi_c(X_\lambda)
 =-6-\left(9-\sum_p\mu_p\right)
 =-15+\sum_p\mu_p\le-7.
 \tag{7}
\]
This contradicts (3). Therefore (4) holds.

Choose linear coordinates \((u,v_1,v_2,v_3)\) with
\(p=[1:0:0:0]\). Singularity of \(f_3\) at \(p\) removes its
\(u^3\) and \(u^2v_i\) terms. The equation \(f_2(p)=0\) also
removes the \(u^2\) term from \(f_2\). Consequently
\[
 \boxed{F=uP(v_1,v_2,v_3)+H(v_1,v_2,v_3),
 \qquad\deg P\le2,\quad\deg H\le3.}
 \tag{8}
\]

This is stronger than merely finding a singular point of the leading
cubic. It removes the troublesome square branch by choosing an
appropriate point at infinity. The
[independent infinity audit](research/cubic-infinity-audit.md)
records the exact hypotheses and source checks.

## 3. Every quadratic coefficient is covered

The [quadratic-coefficient theorem](research/quadratic-coefficient-theorem.md)
proves, with no degree bound on \(H\),
\[
 F=P(v)u+H(v),\quad\deg P\le2,\quad F\text{ stable}
 \quad\Longrightarrow\quad F\text{ a coordinate}.
 \tag{9}
\]

Here is the complete division into cases. Rank refers to the homogeneous
quadratic part of \(P\), not to its zero set.

| Coefficient after normalization | Mechanism |
|---|---|
| A nonzero linear term on the quadratic radical | \(P\) itself is a coordinate; reduce to a univariate coefficient |
| Rank zero or one | Direct shear, known three-variable descent, or Maubach's univariate-coefficient theorem |
| Rank two, nonzero centered constant: \(xy-1\) | Restricted curves must all be \(\mathbb C^*\); an explicit unimodular matrix gives coordinates |
| Rank two, zero centered constant: \(xy\) | Two plane strata and their intersection force one of two explicit coordinate forms |
| Rank three, nonzero centered constant | A nonzero rational cohomology group excludes stability |
| Rank three, zero centered constant: \(xy-z^2\) | Integral \(\mathbb Z/2\) torsion excludes stability |

The normalization is exhaustive by completing the square on the image
of the symmetric quadratic matrix. It uses only invertible changes
of variables, and no degree bound on \(H\) is needed after those
changes. The rank-zero and rank-one steps explicitly use established
results, not new claims.[^4][^5]

### Rank-two coordinate formulas

For \(P=xy-1\), stability is equivalent to
\[
 H(x,x^{-1},z)=c x^kz+B(x),\quad
 c\ne0,\quad k\in\mathbb Z,\quad B\text{ Laurent}.
\]
The [hyperbolic proof](research/hyperbolic-coefficient-pass.md)
lifts this to \(H=az+b+PK\), with \((P,a)\) a unimodular pair.
After the shear \(u\mapsto u+K\), a determinant-one two-by-two
matrix gives a polynomial inverse.

For \(P=xy\), if \(H(0,0,z)\) is nonconstant, the
[intersecting-strata proof](research/crossing-nonconstant-pass.md)
forces
\[
 H=az+b+B(x)+C(y)+xyK,\qquad a\ne0.
\]
After the same shear, solve directly for \(z\). This branch uses
plane-line rectification and a relative-coordinate lemma.[^6]

If \(H(0,0,z)=b\) is constant, the
[disjoint-strata proof](research/crossing-coefficient-pass.md)
forces, up to interchanging \(x,y\),
\[
 H=ay+cx^kz+B(x)+xyK,\quad
 a,c\ne0,\quad k\ge1,\quad B(0)=b.
\]
Put \(V=u+K\). The pair \(q=a+xV,r=cx^k\) has explicit
Bézout coefficients
\[
 A=\frac1a\sum_{j=0}^{k-1}\left(-\frac{xV}{a}\right)^j,
 \qquad B_0=\frac{(-1)^kV^k}{ca^k},\qquad Aq+B_0r=1.
\]
The matrix with rows \((q,r)\) and \((-B_0,A)\) produces
coordinates over \(\mathbb C[x,V]\).

### Why rank three is excluded

For the smooth affine quadric \(D=V(P)\),
\(H_c^2(D;\mathbb Q)=\mathbb Q\). Solving for \(u\) identifies
the open fiber with \(\mathbb A^3\setminus D\). The closed
stratum is a generic smooth affine curve times \(\mathbb A^1\);
its cohomology cannot remove the resulting nonzero
\(H_c^3\) class of the fiber. The
[smooth-quadric proof](research/quadratic-coefficient-obstruction.md)
handles arbitrary \(H\).

For the cone, \(D\) is topologically \(\mathbb C^2/\{\pm1\}\).
Its link is \(\mathbb{RP}^3\), and
\(H_c^3(D;\mathbb Z)=\mathbb Z/2\). The fiber exact sequence
would identify a smooth affine curve's free abelian
\(H_c^1\) with \(\mathbb Z/2\), which is impossible.
Both adjacent vanishings in the sequence matter:
a surjection from a free group to torsion alone would not
be a contradiction. The [cone proof](research/quadric-cone-obstruction.md)
keeps these degree shifts explicit.

Together these arguments prove (9). Combining (8) and (9) proves
the genuine-cubic case of (1).

## 4. Lower degrees and the kernel conclusion

A stable coordinate is not constant. A linear one is already a
coordinate. For a quadratic polynomial \(q=v^TAv+b^Tv+c\),
critical-point-freeness means \(b\notin\operatorname{im}A\).
Hence \(b\) is nonzero on some radical direction, making \(q\)
linear with a nonzero constant coefficient in that direction.
A triangular change makes it a coordinate. This completes
degree at most three.

If \(s\) is an LND slice of that degree, it is a coordinate by (1).
The slice theorem identifies
\(\ker D\simeq B/(s)\), and a coordinate quotient is
\(\mathbb C^{[3]}\), proving (2).

## 5. What has and has not been verified

The previous eleven exact suites passed 152 test methods. The new
[quadratic-coefficient checker](verify_quadratic_coefficients.py)
adds eight passing methods, giving **160 passing test methods**
across twelve suites. The new tests verify:

- both compositions of the hyperbolic and crossing coordinate maps;
- Bézout identities for positive, negative, and zero applicable exponents;
- Laurent lifts, parameter guards, and smoothness controls.

The computational checks use exact rational symbolic arithmetic and
do not import the derivation solver. They do **not** prove compact-support
exact sequences, the Milnor formulas, the universal theorem, or novelty.
Those are mathematical dependencies in the written proof.

Run the new suite with

~~~sh
/opt/anaconda3/bin/python verify_quadratic_coefficients.py
~~~

The earlier suite commands remain in [README.md](README.md).
Separate model audits are useful attempts to find errors, not
independent human peer review. The
[post-proof literature audit](research/cubic-postproof-literature.md)
records exact overlaps and access limits; search absence is not
evidence of originality.

## 6. The actual remaining cancellation problem

The original working question is
\[
 X\times_{\mathbb C}\mathbb A^1\simeq\mathbb A^4
 \quad\Longrightarrow\quad X\simeq\mathbb A^3.
\]
It supplies a slice in a polynomial ring, but no bound on its degree.
This pass closes a low-degree case. It does not show that every
slice can be moved into that case by a polynomial automorphism.

There is a precise, limited next reduction. The same infinity proof
works for every degree \(d\ge3\): it forces a point of
\(\operatorname{Sing}V(f_d)\cap V(f_{d-1})\), because otherwise
\[
 \chi_c(X_\lambda)\le1-(d-1)^3(d-2)<1.
\]
In a direction supplied by that point, \(\deg_uF\le d-2\).
Thus a quartic stable coordinate can be written
\[
 F=A_{\le2}(v)u^2+B_{\le3}(v)u+C_{\le4}(v).
\]
The [extension of the infinity lemma](research/cubic-infinity-audit.md)
proves this necessary form. It does not lower total degree and does
not classify its quadratic-in-\(u\) cases.

The next obligation is to control those higher-degree cases, or find
a different intrinsic argument on their kernels. Repeating searches
inside the completed quadratic-coefficient linear families does not
address that obligation.

No external message, expert contact, public claim, submission, or
publication was made. This remains private research material for
Thomas to understand and have checked before relying on it externally.

## Sources

[^1]: L. Makar-Limanov, P. van Rossum, V. Shpilrain, and J.-T. Yu, [*The stable equivalence and cancellation problems*](https://ems.press/content/serial-article-files/43009), Theorem 1.2 and proof. The stable-coordinate framework is established prior work.
[^2]: L. G. Maxim, L. Păunescu, and M. Tibăr, [*Vanishing cohomology and Betti bounds for complex projective hypersurfaces*](https://www.numdam.org/item/10.5802/aif.3486.pdf), *Annales de l'Institut Fourier* **72** (2022), 1705–1731. Equation (1.3), printed p. 1706, gives smooth Euler characteristics; Remark 3.2, equation (3.11), printed p. 1720, gives the isolated-singularity correction.
[^3]: June Huh, [*Milnor numbers of projective hypersurfaces with isolated singularities*](https://arxiv.org/pdf/1210.2690), version 2, p. 1, displayed polar-degree identity, attributed there to Dimca–Papadima and related work. Published in *Duke Mathematical Journal* **163** (2014), 1525–1548. Only the identity and nonnegativity of degree are used, not a stronger theorem that excludes cones.
[^4]: Stefan Maubach, [*The Commuting Derivations Conjecture*](https://www.math.ru.nl/~maubach/Papers/The_Commuting_Dervations.pdf), Theorem 4.5 and Corollary 4.2. Used for univariate coefficients with arbitrary root multiplicities.
[^5]: V. Shpilrain and J.-T. Yu, [*Affine varieties with equivalent cylinders*](https://arxiv.org/html/math/0110324), Proposition 1.1(c) and proof. Used for stable-coordinate descent in three variables, including arbitrary finite stabilization.
[^6]: Nguyen Van Chau, [*Polynomial maps of the complex plane with the branched value sets isomorphic to the complex line*](https://math.ac.vn/uploads/files/0202197.pdf), Section 2 and Lemma 1. Records the plane-line rectification consequence used in the crossing proof.
