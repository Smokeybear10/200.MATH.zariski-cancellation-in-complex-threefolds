# A smooth quadratic family whose Euler characteristics miss the obstruction

For any integer \(m\geq2\), consider

\[
 F_m(x,u,v,w)=x+x^muv+w^2,
 \qquad X_\lambda=\{F_m=\lambda\}\subset\mathbb A^4_{\mathbb C}.
\]

Every fiber is smooth and every fiber has compactly supported Euler characteristic one. Nevertheless, \(F_m\) is not a stable coordinate and is not the slice of any locally nilpotent derivation. The obstruction is a nonzero cohomology group that Euler characteristic alone does not detect:

\[
 \boxed{H_c^3(X_\lambda;\mathbb Q)\simeq\mathbb Q
 \quad\text{for every }\lambda\ne0.}
 \tag{1}
\]

This is an independently checked negative control, not a novelty claim. It shows why the generic-Euler-characteristic gate cannot be extended to arbitrary four-variable polynomials, and why the affine hypothesis in the full-rank quadratic-pencil argument matters.

## 1. All fibers are smooth

The partial derivatives are

\[
 (F_m)_x=1+mx^{m-1}uv,\quad
 (F_m)_u=x^mv,\quad
 (F_m)_v=x^mu,\quad
 (F_m)_w=2w.
\]

If \(x\ne0\), simultaneous vanishing of the last three derivatives would force \(u=v=w=0\), where the first derivative is one. If \(x=0\), the first derivative is one because \(m\geq2\). Thus the gradient never vanishes, so every \(X_\lambda\) is a smooth complex threefold.

The restriction \(m\geq2\) is essential here. For \(m=1\), points with \(x=w=0\) and \(uv=-1\) are critical points of the zero fiber.

## 2. The open fiber is a quadric complement

On the locus \(x\ne0\), put

\[
 U=x^mu,\qquad V=v,\qquad W=w.
\]

The equation of the fiber becomes

\[
 x=\lambda-UV-W^2.
\]

Consequently,

\[
 X_\lambda^\circ:=X_\lambda\cap\{x\ne0\}
 \simeq\mathbb A^3\setminus S_\lambda,
 \qquad S_\lambda=\{UV+W^2=\lambda\}.
 \tag{2}
\]

The inverse is explicit:

\[
 x=\lambda-UV-W^2,\quad
 u=\frac{U}{(\lambda-UV-W^2)^m},\quad v=V,\quad w=W.
\]

Its denominator is a unit on the indicated open complement. No polynomial inverse on all of \(\mathbb A^3\) is being asserted.

The closed complement \(Z_\lambda=X_\lambda\setminus X_\lambda^\circ\) is given set-theoretically by

\[
 x=0,\qquad w^2=\lambda,
\]

with \(u,v\) free. For \(\lambda\ne0\), it is two disjoint affine planes. For \(\lambda=0\), its reduced support is one affine plane. The scheme-theoretic closed fiber at zero is defined by \(w^2=0\) and is nonreduced, but compactly supported cohomology and the Euler characteristic depend on its underlying complex topological space.

## 3. Every fiber has Euler characteristic one

The elementary decomposition of \(S_\lambda\) into \(U\ne0\) and \(U=0\) gives

\[
 S_\lambda\cap\{U\ne0\}\simeq\mathbb C^*\times\mathbb A^1.
\]

Its Euler characteristic is zero. On \(U=0\), the equation is \(W^2=\lambda\) and \(V\) is free. Thus

\[
 \chi_c(S_\lambda)=
 \begin{cases}2,&\lambda\ne0,\\1,&\lambda=0.\end{cases}
\]

Using (2) and additivity,

\[
 \begin{aligned}
 \chi_c(X_\lambda)
 &=\chi_c(\mathbb A^3)-\chi_c(S_\lambda)
     +\chi_c(Z_\lambda)\\
 &=\begin{cases}1-2+2,&\lambda\ne0,\\1-1+1,&\lambda=0,
 \end{cases}
 =1.
 \end{aligned}
 \tag{3}
\]

This verifies all fibers, not only one generic fiber.

## 4. The quadric contributes a nonzero middle group

Assume \(\lambda\ne0\). Compactify \(S_\lambda\) to

\[
 Q_\lambda=\{UV+W^2=\lambda T^2\}\subset\mathbb P^3.
\]

This is a smooth projective quadric, and its boundary

\[
 D_\infty=Q_\lambda\cap\{T=0\}
 =\{UV+W^2=0\}\subset\mathbb P^2
\]

is a smooth conic. The standard identification \(Q_\lambda\simeq\mathbb P^1\times\mathbb P^1\) can be seen directly: after choosing \(\sqrt\lambda\), set \(A=\sqrt\lambda T+W\) and \(B=\sqrt\lambda T-W\), so its equation becomes \(UV=AB\), the rank-one-matrix Segre quadric. Under this identification, \(D_\infty\simeq\mathbb P^1\) has bidegree \((1,1)\).

The compact-support sequence for \(S_\lambda=Q_\lambda\setminus D_\infty\) contains

\[
 H^1(D_\infty)=0
 \longrightarrow H_c^2(S_\lambda)
 \longrightarrow H^2(Q_\lambda)\simeq\mathbb Q^2
 \xrightarrow{\rho}H^2(D_\infty)\simeq\mathbb Q.
\]

The two ruling classes both have degree one on the boundary conic, so \(\rho(a,b)=a+b\). Its kernel has dimension one. Therefore

\[
 H_c^2(S_\lambda;\mathbb Q)\simeq\mathbb Q.
 \tag{4}
\]

This derivation uses the cohomology of projective lines, the Künneth formula, and the compact-support exact sequence. It does not require a claimed deformation retraction of the affine quadric.

## 5. The class survives in the threefold fiber

The closed-open sequence for \(S_\lambda\subset\mathbb A^3\), together with (2), contains

\[
 H_c^2(\mathbb A^3)=0
 \longrightarrow H_c^2(S_\lambda)
 \longrightarrow H_c^3(X_\lambda^\circ)
 \longrightarrow H_c^3(\mathbb A^3)=0.
\]

Thus (4) gives \(H_c^3(X_\lambda^\circ)\simeq\mathbb Q\). Next use the sequence for \(Z_\lambda\subset X_\lambda\):

\[
 H_c^2(Z_\lambda)
 \longrightarrow H_c^3(X_\lambda^\circ)
 \longrightarrow H_c^3(X_\lambda)
 \longrightarrow H_c^3(Z_\lambda).
\]

For \(\lambda\ne0\), \(Z_\lambda\) is two affine planes, whose compactly supported cohomology is concentrated in degree four. Both outside groups vanish, proving (1).

If \(F_m\) became a coordinate after adjoining \(N\) variables, every fiber would satisfy

\[
 X_\lambda\times\mathbb A^N\simeq\mathbb A^{N+3}.
\]

But Künneth and (1) give nonzero compactly supported cohomology in degree \(3+2N\) on the left. The right side has compactly supported cohomology only in degree \(6+2N\). This is a contradiction. Thus \(F_m\) is not a stable coordinate. A slice is always a one-stable coordinate by the slice theorem, so it cannot be a slice either.

## 6. The precise hypothesis that fails in the affine-pencil proof

As a quadratic form in \((u,v,w)\), this example has matrix

\[
 A(x)=
 \begin{pmatrix}
 0&x^m/2&0\\
 x^m/2&0&0\\
 0&0&1
 \end{pmatrix},\qquad
 \det A(x)=-\frac{x^{2m}}4.
\]

It has generic rank three, rank one at zero, and degree \(m\geq2\) in the base variable. The linear coefficient vector is zero. For an affine matrix pencil, critical-point-freeness excludes a rank-one specialization with its linear coefficient in the quadratic form's image. Here that rank-one specialization occurs without any critical point, because the missing rank first appears in order \(x^m\), not in the first-order matrix pencil.

Its contribution to a generic fiber is two rather than at most one. This exactly explains why the bound \(\chi_c\leq0\) established for nonconstant determinants of affine pencils fails for a general polynomial matrix. It does **not** give a counterexample to the conclusion that stable coordinates in a larger family might be coordinates: these examples are not stable coordinates in the first place.

The family also lies outside the previously classified form \(p(x)y+g(x,z,w)\) as displayed: its coefficient of \(u\) is \(x^mv\), depending on another fiber variable. There is no contradiction with that theorem's stronger cohomological necessity.

Nothing here decides an abstract cylinder isomorphism for the zero fiber alone. The obstruction was proved using nonzero fibers of the specified map \(F_m\).

## Verification scope

The open inverse, determinant formula, and unit gradient ideal were independently checked with exact symbolic arithmetic for \(m=2,3,5\). They all passed. The displayed arguments prove these assertions for every \(m\geq2\); the finite checks are supplementary. The cohomological proof is a written derivation, not a proof-assistant certificate.
