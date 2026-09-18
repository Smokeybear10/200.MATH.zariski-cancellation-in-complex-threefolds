# Two linear variables with coprime coefficients

Let

\[
R=\mathbb C[x,y],\qquad
F=A(x,y)u+B(x,y)z+C(x,y)\in R[u,z].
\]

Assume \(A,B\) are not both zero and are coprime in the UFD
\(R\). Then the following are equivalent:

1. \(F\) is a stable coordinate.
2. \(F\) is a coordinate.
3. \(F\) is a coordinate over \(R\), retaining \(x,y\).
4. \((A,B)=R\).

In particular, original LND slices in this coprime branch descend
to coordinates and have polynomial three-variable kernels. No
degree bound is imposed. Coprimality alone is not being identified
with the unit-ideal condition: the proof explicitly eliminates
their possible finite common-zero set.

## 1. A general fiber is an affine-line torsor off the common zeros

Put \(E=V(A,B)_{\mathrm{red}}\subset\mathbb A^2\).
This is a finite set. Indeed, a positive-dimensional component
would give a height-one prime containing both polynomials, hence
a common irreducible factor. Empty \(E\) is allowed.

Choose \(\lambda\notin C(E)\), a finite set of values. The
fiber \(X_\lambda=\{F=\lambda\}\) has no point over \(E\).
Over its complement \(S=\mathbb A^2\setminus E\), projection
to \((x,y)\) is a Zariski locally trivial affine-line bundle:

- Over \(A\ne0\), use \(z\) as fiber coordinate and solve
  \(u=(\lambda-C-Bz)/A\).
- Over \(B\ne0\), use \(u\) as fiber coordinate and solve
  \(z=(\lambda-C-Au)/B\).

These opens cover \(S\). More precisely, the action

\[
t\cdot(u,z)=(u-Bt,z+At)
\]

makes this an additive-group torsor. The vector \((-B,A)\)
generates the kernel of the coefficient row at every point of
\(S\). No global section or global product over \(S\) is
assumed. Such a section would already fail in examples with a
nonempty common-zero set at the chosen level.

Compactly supported Euler characteristic is additive and is
multiplicative for this locally trivial affine-line bundle. This
also follows directly by the disjoint stratification into
\(A\ne0\) and \(A=0,B\ne0\), on each of which the bundle
is explicitly a product. Consequently

\[
\chi_c(X_\lambda)=\chi_c(S)\chi_c(\mathbb A^1)
=1-\#E.
\tag{1}
\]

The number in this formula is the number of distinct geometric
points, not the length of the possibly nonreduced scheme
\(\operatorname{Spec}R/(A,B)\).

If \(F\) is stable, then for some \(m\ge0\),
\(X_\lambda\times\mathbb A^m\cong\mathbb A^{m+3}\).
Multiplicativity therefore gives \(\chi_c(X_\lambda)=1\).
Equation (1) implies \(E=\varnothing\). The Nullstellensatz
now gives \((A,B)=R\). This proves 1 implies 4.

## 2. Explicit coordinate completion

Choose \(P,Q\in R\) with

\[
AP+BQ=1.
\]

Set

\[
T=-Qu+Pz.
\]

The matrix with rows \((A,B)\) and \((-Q,P)\) has
determinant one. Keeping \(x,y\), its translated coordinate
map is \((u,z)\mapsto(F,T)\), and the polynomial inverse is

\[
u=P(F-C)-BT,\qquad z=Q(F-C)+AT.
\tag{2}
\]

Thus condition 4 implies condition 3. The implications
3 implies 2 implies 1 are immediate. Neither Quillen--Suslin nor
a conjectural completion theorem is required for this length-two
row.

For the original-slice corollary, if \(K=\ker D\) and
\(D(F)=1\), then \(R[u,z]=K[F]\). Swapping \(F\) with
one new variable in \(K[F,t]\) proves stability. The theorem
then gives \(K\cong R[u,z]/(F)\cong\mathbb C^{[3]}\).

## 3. Multiplicities and zero coefficients

For \(A=x^r,B=y^s\), with \(r,s\ge1\), the coefficient
ideal is not the unit ideal, even though the polynomials are
coprime. The common-zero scheme has length \(rs\), but its
reduced support has one point. Formula (1) gives generic Euler
characteristic zero for every \(C\), so no such \(F\) is
stable. There is no multiplicity-dependent replacement such as
\(1-rs\).

For example,

\[
F=x^2u+y^3z+x
\]

is everywhere submersive: vanishing of \(F_u=x^2\) and
\(F_z=y^3\) forces \(x=y=0\), where \(F_x=1\).
Its nonzero fibers nevertheless have Euler characteristic zero.
Smoothness does not replace the stable-fiber hypothesis.

If exactly one coefficient is zero, the coprime hypothesis forces
the other to be a nonzero constant; the theorem and (2) still
apply. If the nonzero coefficient is nonconstant, that case is
outside the coprime theorem but is already settled by the
[general binomial-fiber result](generic-rational-binomial-pass.md):
the unused variable splits off, and stability supplies smooth
rationally acyclic general fibers of the remaining three-variable
polynomial, to which its exponent-one case applies.

If both coefficients are zero, \(F=C(x,y)\). A stable
nonconstant \(C\) has a smooth contractible general plane-curve
fiber, since its product with affine space is an affine space.
That curve is \(\mathbb A^1\), and plane-line rectification
of its reduced equation makes \(C\) a plane coordinate.
A constant \(C\) is not a stable coordinate. These are separate
edge cases, not applications of a gcd condition to \((0,0)\).

## 4. What remains when the gcd is nonconstant

Write

\[
A=D A_0,\qquad B=D B_0,\qquad
\gcd(A_0,B_0)=1,
\]

with \(D\) nonconstant. Put
\(\Delta=V(D)_{\mathrm{red}}\),
\(E_0=V(A_0,B_0)_{\mathrm{red}}\), and
\(E_{\mathrm{out}}=E_0\setminus\Delta\).
The coefficient-zero set is now \(\Delta\cup E_0\), not
just a finite set. Away from it, the projection is still an
affine-line torsor. At a point of that set where \(C=\lambda\),
the fiber over the base point is a full affine plane.

Choose \(\lambda\) avoiding \(C(E_0)\) and the values of
any constant restrictions of \(C\) to components of
\(\Delta\) and otherwise general. Then
\(\Delta\cap\{C=\lambda\}\) is a finite reduced set
topologically, and stratification gives

\[
\chi_c(X_\lambda)
=1-\chi_c(\Delta)-\#E_{\mathrm{out}}
+\#\bigl(\Delta\cap\{C=\lambda\}\bigr).
\tag{3}
\]

Thus the finite-puncture argument (1) does not by itself make the
normalized row \((A_0,B_0)\) unimodular: the divisor introduces
additional affine-plane strata. Formula (3) is only an Euler
constraint, not a classification of this branch.

In fact, residual row basepoints on the gcd divisor can occur for
coordinates. Consider

\[
F=x^2u+xy z+y.
\tag{4}
\]

Here \(D=x\), \((A_0,B_0)=(x,y)\), and
\(E_0=\{(0,0)\}\subset\Delta\). Yet over
\(\mathbb C[x,z]\), the same polynomial is
\(x^2u+(1+xz)y\), and

\[
x^2z^2+(1+xz)(1-xz)=1.
\]

It is a coordinate with companion
\(T=-(1-xz)u+z^2y\) and inverse

\[
u=z^2F-(1+xz)T,\qquad y=(1-xz)F+x^2T.
\]

A broader argument must therefore address how residual row
basepoints interact with the gcd divisor and the restriction of
\(C\); it cannot simply require \((A_0,B_0)=R\).
The example also shows why allowing a change of the retained base
coordinates can matter. This note does not close the general
common-divisor case or claim all-linear stable-coordinate descent.

## 5. Exact controls and scope

Symbolic controls checked both directions of (2) for a nonconstant
unimodular row, each one-zero constant-coefficient row, and the
coordinate (4). They also checked that the gradient ideal of
\(x^2u+y^3z+x\) is the unit ideal. The Euler formulas follow
from the geometric stratifications, not from those finite tests.

The theorem here is exactly the coprime coefficient branch, with
the stated separate zero-coefficient cases. It neither reduces
arbitrary slices to two linear variables nor uses coprimality as
a substitute for a polynomial Bezout identity.
