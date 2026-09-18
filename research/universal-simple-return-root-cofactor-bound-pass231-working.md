# At a simple return root, the cofactor has order at most one

Status: bounded working consequence of the actual universal chart.
The earlier strict cofactor bound loses at least one order at every
return root. At a simple return root the full differential identities
give the stronger bound \(\operatorname{ord}q_1\le1\).

No smoothness or normality of the projected plane ring is required
for this local assertion. In the product-radical conic left by227,
it forces \(q_1=\eta R\) and a noncritical first projection at the
return root. It does not exclude that conic.

## 1. Universal actual hypotheses

Retain the supplied globally sliced exact1122 hypotheses of
[universal184](weight-four-universal-chart-potentials-pass184-working.md):
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\\
\deg_E(X,Y,Z,W)=(1,1,2,2),\\
a=EX,\quad b=EY,\quad e=E^2Z/2,\quad h=E^2W/2,\\
\ker\bigl((\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
\longmapsto(aT,bT,eT^2,hT^2)\bigr)=(F),\\
F\text{ irreducible of weight four},\qquad F_{\mathsf Z}\ne0 .
\end{gathered}
\tag{1}
\]
The ideal is the entire initial kernel, and the capital letters are
actual polynomial coordinates. The literal \(Z\) pivot supplies
\[
\begin{gathered}
N=[u^3](\partial_Z|_A)\ne0,\quad
L=\operatorname{Frac}(\ker_A N),\quad A_L=L[v],\quad Nv=1,\\
t=b/a,\quad \rho=h/a^2,\quad q=e/a^2,\qquad
[L:\mathbb C(t,\rho)]<\infty,\\
Y=y+tX,\quad Z=z+\sigma X+qX^2,\quad
W=w+\vartheta X+\rho X^2,\\
y,z,w,\sigma,\vartheta\in L[v],\qquad L[y,z,w]=L[v],
\qquad J_0=-a^3\in L^* .
\end{gathered}
\tag{2}
\]
The two ratios are algebraically independent. Their coefficient
partials extend uniquely and commute on \(L\), and then hold \(v\)
fixed. The coefficient \(q\) may be algebraic over
\(\mathbb C(t,\rho)\). No rationality of \(L\) is imposed.

Use the coefficient Taylor polynomials \(H_j\) of universal184
and independent formal variables \(U,V\). For \(k,n,\ell,m\in L\),
set
\[
\begin{gathered}
f=H_2(q)+H_1(k)+n,\quad \mathcal R=f_V,\quad
R=\mathcal R(y,\vartheta),\\
S=H_3(q)+H_2(k)+H_1(n),\quad T_0=\ell-S,\\
Q=H_4(q)+H_3(k)+H_2(n)-\ell_tU-\ell_\rho V-m,\\
\mathcal H=(q_{\rho\rho}/2)T_0^2+
                       \mathcal R f_\rho T_0+\mathcal R^2Q.
\end{gathered}
\tag{3}
\]
Assume \(R\ne0\) in \(L[v]\). The actual potentials include
\[
z=q_\rho w+f(y,\vartheta),\qquad
Rw=T_0(y,\vartheta),\qquad
(q_{\rho\rho}/2)w^2+f_\rho(y,\vartheta)w+Q(y,\vartheta)=0.
\tag{4}
\]
In particular \(\mathcal H(y,\vartheta)=0\).

Write \(\mathcal C=L[y,\vartheta]\subset\mathcal O=L[v]\).
Equations (2),(4) imply
\(\operatorname{Frac}\mathcal C=L(v)\): the full return gives
\(\mathcal O=\mathcal C[w]\), and \(w=T_0(y,\vartheta)/R\).
Thus the evaluation ideal in \(L[U,V]\) has an irreducible
generator \(G\). No assertion that \(\mathcal C=\mathcal O\)
is needed.

## 2. Exact differential and cofactor identities

Define
\[
\begin{gathered}
B_1=f_t(y,\vartheta)+q_{t\rho}w,\qquad
C_1=f_\rho(y,\vartheta)+q_{\rho\rho}w,\\
\Lambda_i=\ell_i-S_i(y,\vartheta)-\mathcal R_i(y,\vartheta)w,
\quad i=t,\rho,\\
D_U=R(y_v\vartheta_\rho-y_\rho\vartheta_v)+C_1y_v,\qquad
D_V=R(y_t\vartheta_v-y_v\vartheta_t)-B_1y_v .
\end{gathered}
\tag{5}
\]
In \(\Lambda_i\), coefficient differentiation precedes evaluation.
All subscripts on actual polynomials in \(L[v]\) are the actual
extended partials. The arbitrary-\(q\) derivation in
[cofactor222](rank-two-saturated-pair-cofactor-exclusion-pass222-working.md)
and the reconstruction in
[product-radical227](rank-one-product-radical-sextic-pruning-pass227-working.md)
give
\[
\begin{gathered}
\mathcal H_U(y,\vartheta)=-R(C_1B_1+R\Lambda_t),\qquad
\mathcal H_V(y,\vartheta)=-R(C_1^2+R\Lambda_\rho),\\
R\,dw=-B_1\,dy-C_1\,d\vartheta+\Lambda_t\,dt+\Lambda_\rho\,d\rho,\\
J_0=[dy\wedge(R\,d\vartheta+B_1dt+C_1d\rho)\wedge dw]
                                      _{dt\wedge d\rho\wedge dv},\\
R^3J_0=D_U\mathcal H_U(y,\vartheta)+D_V\mathcal H_V(y,\vartheta).
\end{gathered}
\tag{6}
\]
These identities follow from the formal Taylor derivative identities
and the actual determinant, not a special formula for \(q\).

The last equality implies \(\mathcal H\ne0\) and that \(G\)
occurs simply in \(\mathcal H\). Hence
\[
\mathcal H=GQ_1,\qquad
0\ne q_1:=Q_1(y,\vartheta)\mid R^3,\qquad
\mathcal H_i(y,\vartheta)=q_1G_i(y,\vartheta)\quad(i=U,V).
\tag{7}
\]
If \(G\) occurred repeatedly, both evaluated gradients would vanish,
contradicting \(R^3J_0\ne0\). The divisor statement then follows
from the same last identity in (6). These are polynomial identities
in \(\mathcal O\), not original-ring unit statements.

## 3. Simple-root order bound without plane smoothness

Extend scalars to an algebraic closure \(\Omega\) of \(L\). Let
\(r\in\Omega\) be a simple root of \(R\), so
\[
R(r)=0,\qquad R_v(r)\ne0.
\tag{8}
\]
All order comparisons take place in the local ring
\(\Omega[v]_{(v-r)}\). Suppose for contradiction that \(q_1\)
has order at least two at \(r\). The second gradient identity of (6), divided by the
nonzero polynomial \(R\), and (7) imply
\(C_1(r)^2=0\). Thus \(C_1(r)=0\).

At \(r\), the middle row in the determinant in (6) is
\((B_1(r),0,0)\). Since \(J_0\ne0\), it follows that
\(B_1(r)\ne0\). The \(dv\)-coefficient of the third identity
in (6) now gives \(y_v(r)=0\).
Substituting these conclusions into the determinant yields
\[
J_0=-B_1(r)y_\rho(r)w_v(r)\ne0.
\tag{9}
\]
In particular \(y_\rho(r)\ne0\).

The return is affine in the two projected entries. Differentiating
in \(v\) before evaluation gives
\[
R_v=q_{t\rho}y_v+q_{\rho\rho}\vartheta_v.
\tag{10}
\]
Equations (8),(10) and \(y_v(r)=0\) force
\(\vartheta_v(r)\ne0\), and also \(q_{\rho\rho}\ne0\) in this
hypothetical case. Differentiating the actual relation
\(G(y,\vartheta)=0\) in \(v\) therefore gives
\(G_V(y(r),\vartheta(r))=0\).

The \(d\rho\)-coefficient in (6), evaluated at \(r\), gives
\[
\Lambda_\rho(r)=B_1(r)y_\rho(r)\ne0.
\tag{11}
\]
Since \(C_1(r)=0\), its square has order at least two at \(r\).
Since \(R\) has order one and (11) is nonzero, the polynomial
\(C_1^2+R\Lambda_\rho\) has order exactly one. Thus
\(\mathcal H_V(y,\vartheta)=-R(C_1^2+R\Lambda_\rho)\)
has order exactly two.

On the other hand, its expression \(q_1G_V(y,\vartheta)\) has
order at least three, since \(q_1\) has order at least two and
the evaluated \(G_V\) vanishes at \(r\). If that evaluated
gradient is identically zero, the contradiction is even immediate.
We conclude
\[
\boxed{\operatorname{ord}_r q_1\le1
\quad\text{at every simple geometric root }r\text{ of }R.}
\tag{12}
\]
All coefficient partials above are taken with \(v\) fixed before
evaluation. No derivative is applied to the moving algebraic root
\(r\). Neither smoothness of \(G=0\), normality of \(\mathcal C\),
nor nonvanishing of an a priori chosen gradient was assumed.
The proof does not assert this bound at multiple roots of \(R\).

As a direct consequence, if \(R\) is squarefree, then (7),(12)
give \(q_1\mid R\) up to a scalar. Descent back to \(L[v]\)
follows from polynomial division, or from the multiplicities of
the irreducible factors of \(R\) in characteristic zero.

## 4. The remaining product-radical conic has a simple cofactor

Now specialize to the full initial kernel \(Z^2-XYW\) and the
conic retained in227. Put \(s=q/t\), so \(\rho=s^2t\).
The affine parameter
\[
\chi=\vartheta-s^2y\in L[v],\qquad \deg_v\chi=1
\]
gives, for coefficients in the exact field,
\[
y=P(\chi)=A_2\chi^2+A_1\chi+A_0,\quad A_2\ne0,\qquad
\vartheta=s^2P(\chi)+\chi .
\tag{13}
\]
This is a description of the projected ring only.
Write \(k_s\) for the coefficient partial at fixed \(t\), so
the old \(k_\rho=k_s/(2st)\).
The exact return and a generator of the projected relation are
\[
R=\frac{2s^2k_s-\chi}{4s^3t},\qquad
G(U,V)=U-P(V-s^2U),\qquad G_U+s^2G_V=1.
\tag{14}
\]
The graph presentation proves directly that \(G\) generates the
evaluation ideal. The polynomial \(R\) is linear in \(v\), with
one simple root over \(L\), corresponding to
\(\chi_R=2s^2k_s\).

Combine the two evaluated gradient identities in (6) with the last
identity of (14). Their left side is
\(q_1(G_U+s^2G_V)=q_1\), and their right side is divisible
by \(R\). Thus \(R\mid q_1\). Equations (7),(12) now force
\[
\boxed{q_1=\eta R,\qquad \eta\in L^*.}
\tag{15}
\]
This excludes the order-two alternative allowed by the earlier
strict bound \(q_1\mid R^2\).

At the return root, \(C_1\) cannot vanish. Otherwise dividing both
gradient identities in (6) by \(R\) and using (15) would give
\(G_U=G_V=0\) there, contradicting (14).
The \(dv\)-coefficient in (6) then also shows \(y_v\ne0\) at
that root: if \(y_v=0\), formula (13) gives
\(\vartheta_v=\chi_v\ne0\), contradicting
\(B_1y_v+C_1\vartheta_v=0\).
Consequently
\[
C_1(r)\ne0,\qquad
P'(\chi_R)=2A_2\chi_R+A_1\ne0 .
\tag{16}
\]
Thus the return root cannot be the critical point of the quadratic
first projection. This is a necessary condition, not an exclusion
or realization of the conic.

## 5. Scope and verification

The universal part requires the full actual chart and its nonzero
calibrated determinant. Polynomial potentials without that condition
do not justify (9) or (12). It applies to simple return roots only;
it gives no replacement bound for multiple roots.

For the product-radical conic, equations (15)--(16) leave further
coefficient identities and the original-ring endpoint unresolved.
No coefficient-field coordinate is promoted to an ambient coordinate,
and no claim about arbitrary frame entry or unrestricted cancellation
is made.

The universal sources and strict225 mechanism were fully read and
reconstructed during227. The new order argument was independently
reconstructed by separate AI agents before this note was written.
It is a polynomial local-order proof, not an inference from a finite
list of examples. No saved checker was executed, imported, or compiled;
no previous source, index, JSON, or packet was changed. This is working
mathematics, not human expert review, formal verification, or a
historical novelty claim.
