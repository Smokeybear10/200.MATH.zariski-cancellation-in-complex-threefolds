# Rigidity of a recovered-invariant divided-difference template

Allowing both affine good speeds in this template to depend on all
three invariants does not produce a new coupled actual frame.
A polynomial inverse exists exactly when one speed depends only
on the explicitly recovered invariant and the other is affine,
with constant nonzero slope, in the remaining invariant variable.
The resulting dense family has a primitive first tail in every degree.

This is a classification of the displayed template, not of all
non-autonomous three-good frames. Its positive members are explicit
translations. No actual extra first-tail factor or general
cancellation conclusion is asserted.

## 1. The template and its exact Jacobian

Let \(a,b,v,u\) be independent over \(\mathbb C\), let
\(E=\partial_u\), and fix \(F\in\mathbb C[t]\) of degree
\(d\ge2\). For arbitrary \(f,g\in\mathbb C[a,b,v]\), define
\[
\begin{gathered}
\Delta_F(f,v,u)=
 \sum_{j=1}^{d}c_j\sum_{k=1}^{j}
       \binom jk v^{j-k}f^k u^{k-1},
 \qquad F(t)=\sum_{j=0}^{d}c_jt^j,\\
u\Delta_F(f,v,u)=F(v+uf)-F(v),\\
X=v+uf,\qquad Y=a-F(v)+ug,\qquad Z=u,\qquad
W=g+\Delta_F(f,v,u),\\
a=Y-ZW+F(X).
\end{gathered}
\tag{1}
\]
The divided difference is polynomial, including at \(u=0\).
The last identity holds before any inverse is assumed.
It is the same elementary recovery pattern as the retained
univariate construction129.[^1]

The following conditions are equivalent:
\[
\begin{gathered}
\mathbb C[X,Y,Z,W]=\mathbb C[u,a,v,b],\\
J\in\mathbb C^*,\\
f=P(a),\qquad g=cb+G(a,v),
\quad P\in\mathbb C[a],\ G\in\mathbb C[a,v],\ c\in\mathbb C^*,
\end{gathered}
\tag{2}
\]
where the sign convention and explicit Jacobian are
\[
\begin{gathered}
J=\det\frac{\partial(Z,\;Y-ZW+F(X),\;X,\;W)}
                   {\partial(u,a,v,b)}
 =\det\frac{\partial(X,W)}{\partial(v,b)}
       \bigg|_{u,a},\\
J=g_b+F'(v)f_b+u(f_vg_b-f_bg_v),\\
\det\frac{\partial(X,Y,Z,W)}{\partial(u,a,v,b)}=-J .
\end{gathered}
\tag{3}
\]
Indeed \(X_v=1+uf_v\), \(X_b=uf_b\), and differentiating
the polynomial divided-difference identity cancels all
\(F'(X)\) terms in this two-by-two determinant.
The final sign comes from the swap of \(X\) and \(Z\) in the
displayed target ordering.

An actual polynomial inverse implies that its Jacobian is a
complex unit, so the first line of (2) implies the second.
The converse below is special to this template. No general
Jacobian-to-inverse implication is used.

## 2. The unit Jacobian removes the coupled speeds

Suppose \(J=c\in\mathbb C^*\). Comparing the constant and
linear coefficients of \(u\) in (3), and putting
\(h=g+F'(v)f\), gives
\[
\begin{gathered}
g_b+F'(v)f_b=c,\qquad f_vg_b-f_bg_v=0,\\
h=cb+H(a,v),\qquad
c f_v=\bigl(H_v-F''(v)f\bigr)f_b .
\end{gathered}
\tag{4}
\]
The second identity in the first line and
\(g=cb+H-F'f\) give the last equality by direct substitution.

If \(n=\deg_b f\ge2\), write the leading coefficient as
\(A(a,v)\ne0\). In the last equation of (4), the term
\(-F''ff_b\) has \(b\)-degree \(2n-1>n\), with leading
coefficient \(-nF''A^2\ne0\). Neither \(c f_v\) nor
\(H_vf_b\) has that degree. This is impossible.

If \(n=1\), the coefficient of \(b\) gives
\(cA_v=-F''A^2\). Regard this as an equality in
\(\mathbb C(a)[v]\). If \(r=\deg_v A>0\), its left side
has degree \(r-1\), whereas the right side has degree
\(\deg F''+2r>r-1\). If \(r=0\), the left side vanishes
and the right side does not. This excludes \(n=1\).

Thus \(f_b=0\), including the case \(f=0\).
Equation (4) now gives \(f_v=0\), so \(f=P(a)\).
The constant coefficient of (3) gives \(g_b=c\), hence
\(g=cb+G(a,v)\). This proves the necessity of the last
line of (2).

Conversely, for that last line define successively
\[
u=Z,\qquad
a=Y-ZW+F(X),\qquad
v=X-ZP(a),\qquad
b=c^{-1}\bigl(W-\Delta_F(P(a),v,Z)-G(a,v)\bigr).
\tag{5}
\]
Every expression is polynomial. Substitution of the forward
tuple recovers \(u,a,v,b\) by (1). In the other order,
\(Z=u\), \(X=v+uP(a)\), and the definition of \(b\)
recover \(W\). The remaining forward expression is
\[
a-F(v)+u(cb+G(a,v))
 =a-F(v)+uW-u\Delta_F
 =a+uW-F(X)=Y.
\]
This proves both inverse orders, including \(Z=0\),
and completes (2).

The assumption \(F''\ne0\) is essential for this template
statement. For \(F(t)=t,\ f=b,\ g=0\), one has
\((X,Y,Z,W)=(v+ub,a-v,u,b)\), an actual frame even
though \(f\) depends on \(b\). Its inverse is
\(u=Z,\ b=W,\ v=X-ZW,\ a=Y+v\).

## 3. The dense positive family has an exact primitive tail

In the classified family put \(\beta=cb+G(a,v)\).
The change \((a,b,v)\mapsto(a,\beta,v)\) is a polynomial
automorphism of the invariant ring. In these coordinates (1)
becomes
\[
X=v+P(a)u,\qquad
Y=a-F(v)+\beta u,\qquad Z=u,\qquad
W=\beta+\Delta_F(P(a),v,u).
\tag{6}
\]
Its good speeds in the order \((Z,X,Y)\) are
\((1,P(a),\beta)\). They have rank two and a dense homogeneous
cone exactly when \(P\) is nonconstant: then \(P(a),\beta\)
are independent, and homogeneous evaluation at
\((1,P(a),\beta)\) is injective.
If \(P\) is constant, the speed rank is one.

Assume now that \(P\) is nonconstant. Use \(Z=u\) as the
selected first coordinate in the dense chart139.[^2]
The actual bad partial, holding \(X,Y,Z\) fixed, is
\[
\begin{gathered}
T u=0,\qquad T a=-u,\qquad T v=P'(a)u^2,\qquad
T\beta=1+P'(a)F'(v)u,\\
N=[u^2]T|_{\mathbb C[a,\beta,v]}
   =P'(a)\partial_v,\qquad
L=\mathbb C(a,\beta),\\
\tau=P(a),\qquad \rho=\beta,\qquad
K=\mathbb C(\tau,\rho),\qquad [L:K]=\deg P,\\
r=\frac{v}{P'(a)},\qquad Nr=1,\qquad
y=v,\quad z=a-F(v),\quad w_0=\beta+P(a)F'(v).
\end{gathered}
\tag{7}
\]
For \(T\beta\), differentiate
\(u\Delta_F=F(X)-F(v)\) with \(T\), then cancel \(u\)
in the polynomial domain. The formula for \(N\) proves
its kernel and the displayed coefficient field directly.
The field degree is the degree of the polynomial map
\(a\mapsto P(a)\): \(P(T)-\tau\) is irreducible over
\(\mathbb C(\tau)\), by its primitive linear-in-\(\tau\)
presentation, and adjoining the independent \(\beta\)
preserves that degree.

The initial determinant in \((\tau,\rho,v)\) is
\(1/P'(a)\). Changing to \(r=v/P'(a)\) multiplies it by
\(P'(a)\), giving the normalized determinant one.
Thus (7) uses the actual intrinsic parameter, not an
uncalibrated variable with a different derivative scale.
Since the selected speed is \(1\), \(N'=N\).

To distinguish the Taylor coefficients from the speed
polynomial \(P\), write them as \(\lambda_j\).
With \(m=d-1\), the canonical peeling and signed tails are
\[
\begin{gathered}
\lambda_0=\rho+c_1\tau,\qquad
\lambda_j=c_{j+1}\tau^{j+1}\quad(1\le j\le m),\qquad
\lambda_{-1}=c_0-a,\\
\Phi(U,V)=a-V-F(U),\qquad
\Psi(U,V)=\frac{U}{P'(a)},\qquad
\Psi(y,z)=r .
\end{gathered}
\tag{8}
\]
Here the coefficient partials extend from \(K\) to \(L\)
and fix \(r\). In particular \(\partial_\tau a=1/P'(a)\).
For a direct verification, their Taylor map satisfies
\(\Theta(\tau)=(v+\tau u)/u\) and
\(\Theta(\rho)=(z+\rho u)/u\), so
\[
\sum_{j=0}^{m}u^j\Theta(\lambda_j)
 =\beta+\frac{z+F(v+\tau u)-c_0}{u}
 =W+\frac{a-c_0}{u}.
\]
Thus the first evaluated negative coefficient is \(c_0-a\).
The homogeneous Taylor polynomials give
\(\Phi=a-V-F(U)\); all order-\(j+2\) derivatives of the
nonnegative \(\lambda_j\) vanish, and
\(-H_1(c_0-a)=U/P'(a)\), proving the second tail.

The polynomial \(\Phi\) is irreducible and is a plane
coordinate over \(L\), since it is linear in \(V\) with
constant nonzero coefficient. It is the exact kernel
of \(U\mapsto v,\ V\mapsto a-F(v)\).
Its degree is \(d\). The last-coordinate time degree
is exactly \(m=d-1\), and the fixed-good shear theorem141
therefore gives \(\mu=d-1\).[^3]
An arbitrary finite coefficient-field degree coexists
with a primitive first tail in this family.
Moreover \(K(\lambda_{-1})=L\), since
\(a=c_0-\lambda_{-1}\).

The original ordering also gives a genuinely nonconstant selected
speed, \(EX=P(a)\). In that chart the other projected goods are
\[
\widetilde y=a-F(v)-\frac{\beta v}{P(a)},\qquad
\widetilde z=-\frac{v}{P(a)},\qquad
\widetilde g(U,V)=U-a+F(-P(a)V)-\beta V.
\tag{9}
\]
They generate \(L[v]\), and \(\widetilde g\) is their exact
irreducible equation of degree \(d\). The ratio field is still
\(\mathbb C(\beta/P(a),1/P(a))=K\). Permuting the goods leaves
their polynomial ring and hence the fixed-good minimum unchanged.
The degree criterion141 therefore makes this chart's first tail
primitive as well: both its degree and \(\deg\widetilde g\) are
\(\mu+1=d\). No equality of the two formally normalized tail
polynomials under that permutation is asserted.

## 4. Construction scope

These positive curves of automorphisms are not autonomous
exponentials when \(P\) is nonconstant. Identify the parameter-zero
source coordinates as
\(x=v,\ y_0=a-F(v),\ w_0=\beta+P(a)F'(v)\).
If the curve were \(\exp(u\delta)\) for one derivation \(\delta\)
of this polynomial three-ring, its first derivatives would give
\(\delta v=P(a)\) and \(\delta y_0=\beta\).
Consequently \(\delta a=w_0\) and
\(\delta^2v=P'(a)w_0\ne0\), contradicting the exactly
affine formula \(X=v+uP(a)\).
Thus the template is outside the autonomous construction
excluded separately in142.

The necessity proof nevertheless uses the special recovered
identity \(a=Y-ZW+F(X)\) throughout. It does not restrict an
arbitrary actual frame to that identity or prove that every
actual first tail is primitive. It only rules out new coupled
speeds inside (1), and computes the tails of the surviving
explicit family. No historical novelty claim is made.

## Sources

1. [Cubic acceleration outside the fixed-good quadratic span129](three-good-cubic-acceleration-span-obstruction-pass129.md),
   Sections 1 and 3. The polynomial divided difference, explicit
   recovery pattern and selected-partial calculation in its original
   univariate-speed specialization.
2. [A dense all-degree chart and its formal Taylor peeling139](dense-all-degree-taylor-chart-pass139-working.md)
   and [The first two negative Taylor coefficients in a dense chart139](dense-negative-tail-relations-pass139-working.md).
   The fixed intrinsic normalization and signed-tail conventions.
   The specialization (7)--(8) is checked directly above.
3. [Fixed-good shears preserve the tails and determine minimal time degree141](dense-shear-minimal-tail-pass141-working.md),
   Sections 2--4. The exact identity \(\mu=\deg\Phi-1\) for the
   selected dense fixed-good frame.

The Jacobian rigidity and both inverse orders are elementary
proofs for this specified template. No external classification
theorem is used.

[^1]: Source 1. The quotient notation for a divided difference
    denotes its displayed polynomial, not a localization.
[^2]: Source 2. The generic coefficient field is not replaced by
    its rational speed-ratio subfield.
[^3]: Source 3. This is a minimum under fixed-good bad shears,
    not a minimum over arbitrary coordinate frames.
