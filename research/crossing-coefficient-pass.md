# The constant-intersection branch for a crossing quadratic coefficient

Let

\[
 F(x,y,z,u)=xyu+H(x,y,z),\qquad H(0,0,z)=b\in\mathbb C.
\]

There is no degree bound on \(H\). In this constant-intersection branch, \(F\) is a stable coordinate if and only if, after possibly exchanging \(x\) and \(y\), it has the form

\[
 \boxed{H=a y+c x^kz+B(x)+xyK(x,y,z),}
 \tag{1}
\]

where

\[
 a,c\in\mathbb C^*,\qquad k\geq1,\qquad B(0)=b.
\]

Every polynomial satisfying (1) is an ordinary coordinate with an explicit inverse. Thus, in this branch, being a coordinate, a stable coordinate, or the slice of an LND are equivalent. This is a checked derivation for the stated branch, with no assertion of novelty or of a reduction of the general cancellation problem to it.

## 1. Stable fibers and the open set

Suppose \(F\) is a stable coordinate. For every \(\lambda\), its fiber \(X_\lambda\) satisfies

\[
 X_\lambda\times\mathbb A^N\simeq\mathbb A^{N+3}
\]

for some fixed \(N\). Consequently it is smooth, has only constant algebraic units, and has integral compactly supported cohomology concentrated in degree six:

\[
 H_c^i(X_\lambda;\mathbb Z)=
 \begin{cases}\mathbb Z,&i=6,\\0,&i\ne6.
 \end{cases}
 \tag{2}
\]

The cohomology assertion follows from compact-support Künneth applied to the affine-space factor. The corresponding consequences for a slice follow because a slice is a one-stable coordinate.

On \(xy\ne0\), solve uniquely for \(u\). This gives

\[
 U_\lambda:=X_\lambda\cap\{xy\ne0\}
 \simeq(\mathbb C^*)^2\times\mathbb A^1_z.
\]

Thus

\[
 H_c^4(U_\lambda)=\mathbb Z,\quad
 H_c^5(U_\lambda)=\mathbb Z^2,\quad
 H_c^6(U_\lambda)=\mathbb Z,
 \tag{3}
\]

with all other groups zero. All cohomology in this note has integral coefficients.

## 2. The two plane restrictions are nonconstant and smooth off the crossing

Put

\[
 f(y,z)=H(0,y,z),\qquad g(x,z)=H(x,0,z).
\]

Both take the constant value \(b\) on the crossing line. Neither can be a constant polynomial. For example, if \(f=b\), a fiber with \(\lambda\ne b\) has no point with \(x=0\), so \(x\) is a nonconstant unit on \(X_\lambda\). It is nonconstant because the displayed open set permits every nonzero \(x\)-value. This contradicts the units consequence of stability. The same argument applies to \(g\) and \(y\).

Critical-point-freeness of \(F\) implies that \(f\) is a submersion on \(y\ne0\). Indeed, if \(f_y=f_z=0\) at \((y,z)\) with \(y\ne0\), choose

\[
 x=0,\qquad u=-H_x(0,y,z)/y.
\]

All four derivatives of \(F\) would vanish there. Likewise \(g\) is a submersion on \(x\ne0\).

Fix any \(\lambda\ne b\). The curves

\[
 C_x(\lambda)=\{f(y,z)=\lambda\},\qquad
 C_y(\lambda)=\{g(x,z)=\lambda\}
\]

are nonempty because \(f,g\) are nonconstant plane polynomials. They avoid respectively \(y=0\) and \(x=0\), and hence are smooth affine curves. In the coefficient divisor \(xy=0\), they are disjoint, since their possible intersection would lie on the crossing line where \(H=b\). Therefore

\[
 Z_\lambda:=X_\lambda\setminus U_\lambda
 =\bigl(C_x(\lambda)\sqcup C_y(\lambda)\bigr)\times\mathbb A^1_u.
 \tag{4}
\]

These assertions hold for every \(\lambda\ne b\), not only for generic values.

## 3. Exactly one plane curve is an affine line

The two segments of the compact-support sequence for \(Z_\lambda\subset X_\lambda\), using (2)–(3), give

\[
 H_c^3(Z_\lambda)\simeq H_c^4(U_\lambda)=\mathbb Z,
 \qquad
 H_c^4(Z_\lambda)\simeq H_c^5(U_\lambda)=\mathbb Z^2.
\]

After removing the degree-two shift of the affine-line factor in (4),

\[
 \begin{aligned}
 H_c^1(C_x(\lambda))\oplus H_c^1(C_y(\lambda))&\simeq\mathbb Z,\\
 H_c^2(C_x(\lambda))\oplus H_c^2(C_y(\lambda))&\simeq\mathbb Z^2.
 \end{aligned}
 \tag{5}
\]

For a nonempty smooth affine curve, the rank of \(H_c^2\) is its number of connected components. Thus each curve in (5) is connected, hence irreducible. If its smooth projective completion has genus \(\gamma\) and omits \(n\geq1\) points, its \(H_c^1\) is free of rank \(2\gamma+n-1\). The two ranks in the first line of (5) must therefore be zero and one. One curve is \(\mathbb A^1\), and the other is \(\mathbb C^*\).

There are infinitely many values \(\lambda\ne b\). By the pigeonhole principle, the same plane supplies the affine-line curve for infinitely many of them. Exchange \(x,y\) if necessary so that it is \(C_x(\lambda)\).

On each of these affine lines, \(y\) is a unit, since the line avoids \(y=0\). Every unit of \(\mathbb C[t]\) is constant, so \(y=a_\lambda\ne0\). A closed irreducible curve contained in the line \(y=a_\lambda\) is that entire line. Distinct values of \(\lambda\) give distinct such vertical lines.

The polynomial \(f_z(y,z)\) therefore vanishes on infinitely many distinct vertical lines. Its coefficients as a polynomial in \(z\) vanish at infinitely many \(y\)-values, and hence all vanish. Thus \(f=f(y)\). Connectedness of its generic fiber forces \(\deg f=1\), since a polynomial of degree greater than one has more than one distinct root on a generic level. Consequently

\[
 f(y,z)=a y+b,\qquad a\ne0.
 \tag{6}
\]

It now follows from (5) that \(C_y(\lambda)\simeq\mathbb C^*\) for every \(\lambda\ne b\).

## 4. The other restriction is linear in the free variable

Consider

\[
 h=g|_S,
 \qquad S=\operatorname{Spec}\mathbb C[x,x^{-1},z]
 \simeq\mathbb C^*\times\mathbb A^1.
\]

It is a submersion, and every fiber with value \(\lambda\ne b\) is \(\mathbb C^*\). On such a fiber, the function \(x\) is a nonconstant unit. It cannot be constant: otherwise that closed curve would lie in a vertical affine line \(x=a\) and would equal that line, contradicting its being \(\mathbb C^*\).

Writing the coordinate ring of the fiber as \(\mathbb C[t,t^{-1}]\), its unit \(x\) must be \(c_\lambda t^n\), with \(n\ne0\). Hence the map from the fiber to \(\mathbb C^*\) given by \(x\) is surjective and étale. In particular, its differential is nowhere zero along that fiber.

The tangent space to a fiber of the submersion \(h\) is \(\ker dh\). In the coordinates \((x,z)\), a tangent vector spanning it is

\[
 h_z\partial_x-h_x\partial_z.
\]

The differential of \(x\) on this vector is \(h_z\). Therefore

\[
 h_z\ne0\quad\text{at every point with }h\ne b.
 \tag{7}
\]

In particular, \(h_z\) is not the zero polynomial. If it had a zero, its zero divisor in the smooth affine surface \(S\) would have an irreducible curve component \(E\), by the principal ideal theorem. Equation (7) implies \(h=b\) on \(E\). Since \(h_z=0\) there and \(h\) is a submersion, \(h_x\ne0\) along \(E\). Restricting \(dh\) to the smooth locus of \(E\) gives

\[
 0=dh|_E=h_x\,dx|_E,
\]

so \(dx|_E=0\). In characteristic zero, a rational function on an irreducible curve with zero differential is constant. Thus \(x=a\in\mathbb C^*\) on \(E\), and the closed curve \(E\) equals the entire vertical line \(x=a\).

It follows that \(h(a,z)=b\). But every fiber with \(\lambda\ne b\) maps surjectively to \(\mathbb C^*\) under \(x\), and hence must contain a point with \(x=a\). This is impossible. Therefore \(h_z\) has no zero on \(S\) and is a unit of its coordinate ring:

\[
 h_z=c x^k,\qquad c\ne0,\quad k\in\mathbb Z.
\]

Since \(g\) extends polynomially to \(x=0\), its derivative does too, forcing \(k\geq0\). The condition \(g(0,z)=b\) rules out \(k=0\). Integrating in \(z\) gives

\[
 g(x,z)=c x^kz+B(x),\qquad k\geq1,\quad B(0)=b.
 \tag{8}
\]

Equations (6) and (8) show that

\[
 H-a y-c x^kz-B(x)
\]

is divisible by both \(x\) and \(y\), hence by \(xy\). This proves the necessary normal form (1).

## 5. A polynomial inverse proves sufficiency

Assume (1). Set

\[
 V=u+K(x,y,z),\quad q=a+xV,\quad r=c x^k.
\]

The first substitution is a polynomial shear, and

\[
 F=qy+rz+B(x).
\]

The pair \((q,r)\) is unimodular over \(\mathbb C[x,V]\). Explicit coefficients are

\[
 S=\frac1a\sum_{j=0}^{k-1}\left(-\frac{xV}{a}\right)^j,
 \qquad T=\frac{(-1)^kV^k}{c a^k},
 \qquad Sq+Tr=1.
 \tag{9}
\]

Define

\[
 W=-Ty+Sz.
\]

The matrix

\[
 \begin{pmatrix}q&r\\-T&S\end{pmatrix}
\]

has determinant one. Thus \((x,V,F,W)\) is a polynomial coordinate system. Its inverse is

\[
 \begin{aligned}
 y&=S(F-B(x))-rW,\\
 z&=T(F-B(x))+qW,\\
 u&=V-K(x,y,z),
 \end{aligned}
 \tag{10}
\]

with the first two expressions substituted into the last. All entries are polynomials. The kernel of the transported derivation \(\partial/\partial F\) is \(\mathbb C[x,V,W]\).

This explicit inverse establishes the positive conclusion without an external theorem about jointly linear polynomials.

As supplementary algebraic checks, (9) and both full coordinate compositions in (10) were verified exactly for \(k=1,2,3\), using \(a=2\), \(c=3\), \(B(x)=5+x+2x^2\), and the nonlinear shear \(K=xy+z^2\). All checks passed. The geometric necessity remains a written proof, not a finite-search conclusion or a proof-assistant certificate.

## Scope

The assumption \(H(0,0,z)=b\) is part of this theorem. If the restriction to the crossing line is nonconstant, the closed plane strata meet and the cohomological decomposition (4) changes. That branch requires its own argument. No assertion about it, about arbitrary cubic slice polynomials, or about general cancellation is made here.
