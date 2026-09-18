# Integral torsion obstruction for a quadratic-cone coefficient

**Status:** complete conditional-family exclusion; no claim about general cubic slices

## 1. The statement

Let

\[
P(x,y,z)=xy-z^2,
\qquad
F(x,y,z,u)=P(x,y,z)u+H(x,y,z),
\]

where \(H\in\mathbb C[x,y,z]\) is arbitrary.  Then \(F\) is not a stable
coordinate of \(\mathbb C[x,y,z,u]\).  In particular, it is neither an
ordinary coordinate nor a slice of a locally nilpotent derivation.

The degree of \(H\) is irrelevant.  Thus this eliminates the rank-three
homogeneous-cone coefficient in the remaining cubic normal form

\[
F=P(v)u+H(v),\qquad \deg P\leq2,\quad\deg H\leq3.
\]

Every nondegenerate homogeneous ternary quadratic form over \(\mathbb C\)
is linearly equivalent, up to a nonzero scalar, to \(xy-z^2\), so the same
conclusion holds for every rank-three quadratic cone.  More generally, if a
rank-three affine quadratic polynomial has completed-square constant zero,
translation to its center reduces it to this homogeneous case.  The
conclusion therefore covers exactly that zero-constant rank-three branch.

The obstruction is integral torsion.  Rational Euler characteristic alone
does not see it.

## 2. Compactly supported cohomology of the cone

Put

\[
D=V(xy-z^2)\subset\mathbb A^3,
\qquad U=\mathbb A^3\setminus D.
\]

The finite map

\[
\mathbb C^2\longrightarrow D,\qquad
(r,s)\longmapsto(r^2,s^2,rs)
\]

identifies \(D\) topologically with \(\mathbb C^2/\{\pm1\}\).  Radial
coordinates therefore identify \(D\) with the open cone on

\[
S^3/\{\pm1\}=\mathbb {RP}^3.
\]

Its one-point compactification is the suspension
\(\Sigma\mathbb {RP}^3\).  Hence

\[
H_c^i(D;\mathbb Z)
=\widetilde H^i(D^+;\mathbb Z)
=\widetilde H^{i-1}(\mathbb {RP}^3;\mathbb Z).
\tag{1}
\]

Integral homology and the universal-coefficient theorem give

\[
H^2(\mathbb {RP}^3;\mathbb Z)=\mathbb Z/2,
\qquad
H^3(\mathbb {RP}^3;\mathbb Z)=\mathbb Z.
\]

Consequently,

\[
H_c^3(D;\mathbb Z)=\mathbb Z/2,
\qquad
H_c^4(D;\mathbb Z)=\mathbb Z.
\tag{2}
\]

This degree placement can also be checked by writing
\(D\setminus\{0\}\simeq(0,\infty)\times\mathbb {RP}^3\) and using the
closed--open sequence for the vertex.  In particular, the \(\mathbb Z/2\)
is in degree three, not degree two or four.

Now use the closed--open sequence for \(D\subset\mathbb A^3\).  Since

\[
H_c^i(\mathbb A^3;\mathbb Z)=
\begin{cases}
\mathbb Z,&i=6,\\
0,&i\ne6,
\end{cases}
\]

the segments containing (2) give canonical isomorphisms

\[
H_c^4(U;\mathbb Z)\cong H_c^3(D;\mathbb Z)=\mathbb Z/2,
\qquad
H_c^5(U;\mathbb Z)\cong H_c^4(D;\mathbb Z)=\mathbb Z.
\tag{3}
\]

Only the first isomorphism in (3) is needed for the contradiction.

## 3. A generic fiber of \(F\)

For \(\lambda\in\mathbb C\), write

\[
X_\lambda=V(Pu+H-\lambda)\subset\mathbb A^4,
\qquad
C_\lambda=V(P,H-\lambda)\subset\mathbb A^3.
\]

On \(P\ne0\), the equation uniquely determines

\[
u=\frac{\lambda-H}{P}.
\]

Thus the open part of \(X_\lambda\) is exactly \(U\).  Its reduced closed
complement is

\[
Z_\lambda=C_\lambda\times\mathbb A^1_u.
\tag{4}
\]

Choose \(\lambda\) as follows.  If the restriction \(H|_D\) is constant,
take \(\lambda\) different from that constant; then \(C_\lambda\) is empty.
If \(H|_D\) is nonconstant, its restriction to the smooth surface
\(D\setminus\{0\}\) is dominant.  Generic smoothness in characteristic
zero, followed by excluding the one value \(H(0)\), supplies a \(\lambda\)
for which \(C_\lambda\) is a nonempty smooth affine complex curve contained
in \(D\setminus\{0\}\).  Disconnectedness is allowed.

The generic-smoothness assertion can be seen directly here.  The critical
locus of the regular function on the smooth surface has finitely many
irreducible components.  The function is constant on every
positive-dimensional critical component, while isolated critical points are
finite.  Removing those finitely many values and \(H(0)\) makes the fiber
smooth and avoids the cone vertex.

## 4. What stability would force

Assume for contradiction that \(F\) becomes a coordinate after adjoining
\(N\) independent variables.  Then, for every \(\lambda\),

\[
X_\lambda\times\mathbb A^N\cong\mathbb A^{N+3}.
\]

The product deformation-retracts onto \(X_\lambda\), so \(X_\lambda\) is
contractible.  Smoothness descends from the product.  Poincare duality for
the smooth complex threefold therefore gives

\[
H_c^i(X_\lambda;\mathbb Z)=0\quad(i\ne6).
\tag{5}
\]

Apply compactly supported cohomology with integral coefficients to the
closed inclusion \(Z_\lambda\subset X_\lambda\) and its open complement
\(U\).  The relevant exact segment is

\[
H_c^3(X_\lambda)\longrightarrow H_c^3(Z_\lambda)
\longrightarrow H_c^4(U)\longrightarrow H_c^4(X_\lambda).
\]

Both outside groups vanish by (5), while (3) identifies the third group.
Therefore

\[
H_c^3(Z_\lambda;\mathbb Z)\cong\mathbb Z/2.
\tag{6}
\]

The compact-support Kunneth formula and (4) give, without a Tor term,

\[
H_c^3(Z_\lambda;\mathbb Z)
\cong H_c^1(C_\lambda;\mathbb Z),
\tag{7}
\]

because \(H_c^2(\mathbb A^1;\mathbb Z)=\mathbb Z\) and its other
compactly supported cohomology groups vanish.

If \(C_\lambda\) is empty, the right side of (7) is zero, contradicting
(6).  Otherwise \(C_\lambda\) is a smooth affine complex curve.  It is an
oriented real surface of finite type, so Poincare duality identifies
\(H_c^1(C_\lambda;\mathbb Z)\) with its integral first homology; this is a
free abelian group.  It cannot be \(\mathbb Z/2\).  This contradiction proves
the theorem.

## 5. From slices to stability

If an LND \(E\) satisfied \(E(F)=1\), the slice theorem would write

\[
\mathbb C[x,y,z,u]=K[F].
\]

After adjoining one variable \(T\), interchange \(F\) and \(T\) over
\(K\).  Since \(K[T]\cong K[F]\), this makes \(F\) a one-stable
coordinate.  The obstruction above therefore excludes LND slices as well
as stable and ordinary coordinates.

## 6. Boundary: the rank-two split quadric

The torsion argument is special to the rank-three cone.  For comparison,
if \(P=xy\), then

\[
D=V(xy)=\mathbb A^2\cup_{\mathbb A^1}\mathbb A^2.
\]

Mayer--Vietoris gives

\[
H_c^3(D;\mathbb Z)=\mathbb Z,
\qquad
H_c^4(D;\mathbb Z)=\mathbb Z^2.
\]

Thus

\[
H_c^4(\mathbb A^3\setminus D)=\mathbb Z,
\qquad
H_c^5(\mathbb A^3\setminus D)=\mathbb Z^2.
\]

The same stable-fiber sequence would require a generic, possibly nodal,
\(C_\lambda=V(xy,H-\lambda)\) to satisfy

\[
H_c^1(C_\lambda;\mathbb Z)=\mathbb Z,
\qquad
H_c^2(C_\lambda;\mathbb Z)=\mathbb Z^2.
\]

These groups are possible even for a disconnected smooth affine curve,
and also for suitable nodal curves, so there is no torsion
contradiction.  The rank-two branch needs additional information about the
two plane pieces and their intersection; it is not proved by the present
argument.

## 7. Claim boundary

This is a complete topological exclusion for coefficients affine-equivalent
to the homogeneous rank-three quadric cone, equivalently the rank-three
quadratics with zero completed-square constant.  It does not classify
rank-two quadrics, affine quadrics with a nonzero completed-square constant,
arbitrary quadratic \(P\), or the full cubic normal form.  It uses integral
compactly supported cohomology essentially: tensoring (6) with
\(\mathbb Q\) would erase the contradiction.  The proof is a written
reconstruction, not a Lean formalization or a human expert review, and no
originality claim is made.
