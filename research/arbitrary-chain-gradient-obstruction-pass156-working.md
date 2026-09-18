# Obstruction to every nonlinear chain of length at least three

**Status: complete working proof under the stated differential-field hypotheses.**

A single canonical coefficient-gradient identity is incompatible with
the fixed-axis nonlinear chains considered here, of any finite length
at least three. The argument first bounds the leading
coefficient derivative in the first residual chart. It then evaluates
the already differentiated identity at a critical point of the last
polynomial and obtains incompatible degrees on that coordinate fiber.

The main statement is over a differential field. Its conditional
application to actual normalized dense frames retains the precise
canonical parameter and degree hypotheses. No arbitrary-coordinate
entry or full cancellation conclusion is claimed here. The saved155
three-stage proof and every earlier artifact are unchanged.

## 1. The differential-field chain and the statement

Let \(L\) be a characteristic-zero field with a derivation
\(\delta:L\to L\), extended to fix independent variables \(U,V\).
Let \(n\ge3\) and \(A_i\in L[T]\) with
\(d_i:=\deg A_i\ge2\) for \(1\le i\le n\). Define
\[
\begin{gathered}
P_0=U,\qquad P_1=V-A_1(U),\\
P_i=P_{i-2}-A_i(P_{i-1})\quad(2\le i\le n-1),\\
\Phi=A_n(P_{n-1})+\lambda P_{n-2}+\nu,
\qquad \lambda\in L^*,\quad\nu\in L .
\end{gathered}
\tag{1}
\]
There do not exist \(\alpha\in L^*\) and \(\beta,c\in L\) with
\[
\Psi=\alpha P_{n-1}+\beta+c\Phi,
\qquad \delta\Phi=\partial_U\Psi .
\tag{2}
\]
No centering or extraction of coefficient roots is used before
forming the polynomial derivative identity. One algebraic critical
point is used later only to evaluate that identity.

Write \(A_{i,\delta}\) for coefficient differentiation at a fixed
argument, and \(A_i'\) for differentiation in the argument.
Set \(\mathscr D=\delta-c\partial_U\), a derivation of
\(L[U,V]\). Equation (2) is equivalent to
\(\mathscr D\Phi=\alpha(P_{n-1})_U\). Its residual derivatives are
\[
\begin{gathered}
Q_i=\mathscr D P_i,\qquad Q_0=-c,\\
Q_1=P(U),\qquad P(T)=cA_1'(T)-A_{1,\delta}(T),\quad
\deg P\le r:=d_1,\\
Q_i=Q_{i-2}-A_{i,\delta}(P_{i-1})
                 -A_i'(P_{i-1})Q_{i-1}\quad(2\le i\le n-1).
\end{gathered}
\tag{3}
\]
Every coefficient derivative is retained. In particular
\(\mathscr D\) does not fix the coefficients of the chain.

## 2. First residual chart and the exact transformed identity

Put \(R=P_1\), \(H=P_2\), and \(q=d_2\). Their inverse is
\[
U=H+A_2(R),\qquad V=R+A_1(H+A_2(R)),\qquad
L[U,V]=L[H,R].
\tag{4}
\]
Let \(F(H,R)\) denote \(\Phi\), and \(G(H,R)\) denote
\(P_{n-1}\), expressed in this chart. Coefficient derivation
of \(F\) at fixed \(H,R\) is written \(F_\delta\).
Using \(Q_2=-c-A_{2,\delta}(R)-A_2'(R)P(U)\), the full
identity is
\[
\begin{aligned}
&(F_R-A_2'(R)F_H)P(H+A_2(R))
 +F_\delta-(c+A_{2,\delta}(R))F_H\\
&\qquad
=\alpha\Bigl\{G_H+
 (A_2'(R)G_H-G_R)A_1'(H+A_2(R))\Bigr\}.
\end{aligned}
\tag{5}
\]
The right side uses \(R_U=-A_1'(U)\) and
\(H_U=1+A_2'(R)A_1'(U)\). The derivatives of \(A_3\) and
all later polynomials, as well as \(\lambda,\nu\), are inside
\(F_\delta\); they have not been suppressed.

We first prove \(\deg P\le r-1\).
For \(n=3\), \(F=A_3(H)+\lambda R+\nu\) and \(G=H\).
If \(P\) has degree \(r\), the term
\(-A_2'(R)A_3'(H)P(H+A_2(R))\) has degree
\(q(r+1)-1\) in \(R\). Its coefficient is nonzero.
The term \(\lambda P\) has degree at most \(qr\), the
right side degree at most \(qr-1\), and the remaining
terms degree at most \(q\). Since \(q\ge2\), cancellation
is impossible. This is the first-degree step of155, reproduced
here rather than assumed as an additional classification input.[^1]

## 3. The top two coefficients for every longer chain

Assume \(n\ge4\), and first use the independent variables
\(H,K\), where \(K=P_3=R-A_3(H)\).
Write \(Z_j(H,K)\) for \(P_j\); then
\(Z_2=H, Z_3=K\), and
\(Z_j=Z_{j-2}-A_j(Z_{j-1})\) for \(j\ge4\).

For every \(j\ge4\), the exact \(K\)-degree is
\(e_j=\prod_{i=4}^j d_i\), and the coefficients of
\(K^{e_j}\) and \(K^{e_j-1}\) belong to \(L\), with
the first nonzero. Here is the full induction. For \(j=4\),
\(Z_4=H-A_4(K)\), so the assertion follows from \(d_4\ge2\).
For \(j\ge5\), put \(e=\deg_K Z_{j-1}\ge2\).
The lower powers in \(A_j(Z_{j-1})\) have degree at most
\(d_j e-e\le d_j e-2\). The added \(Z_{j-2}\) also
has degree at most \(d_j e-2\), since its degree is smaller
than \(e\). The top two coefficients therefore come only
from the leading power of \(Z_{j-1}\), and depend only on
its top two coefficients. Both remain in \(L\).

The same proof applies to
\(\widetilde F(H,K)=A_n(Z_{n-1})+\lambda Z_{n-2}+\nu\).
For \(n=4\) it is immediate from
\(\widetilde F=A_4(K)+\lambda H+\nu\).
Consequently, setting
\(D=\deg_R F\), \(E_0=\deg_R G\), and
\(f_D=\operatorname{lc}_R F\), we have
\[
\begin{gathered}
E_0=\prod_{i=4}^{n-1}d_i,\qquad
D=d_nE_0>E_0,\qquad f_D\in L^*,\\
\widetilde F(H,K)=f_DK^D+f_{D-1}K^{D-1}
 +\text{terms of lower }K\text{-degree},\qquad f_{D-1}\in L,\\
F(H,R)=\widetilde F(H,R-A_3(H)),\\
\deg_R F_H=D-1,\qquad
[R^{D-1}]F_H=-D f_D A_3'(H)\ne0 .
\end{gathered}
\tag{6}
\]
The empty product in \(E_0\), for \(n=4\), is one.
The last assertion follows either from the two displayed
coefficients or from
\(F_H=\widetilde F_H-A_3'(H)\widetilde F_K\).
The first term has \(K\)-degree at most \(D-2\).

Let \(b_q\) be the nonzero leading coefficient of \(A_2\).
If \(P\) has degree \(r\) with coefficient \(p_r\ne0\),
the first product on the left of (5) has exact \(R\)-degree
\[
D+q(r+1)-2,\qquad
\text{leading coefficient }Dqf_Db_q^{r+1}A_3'(H)p_r\ne0 .
\tag{7}
\]
Indeed \(F_R\) has degree \(D-1\), whereas
\(-A_2'F_H\) has degree \(D+q-2\).
All other terms on the left of (5) have degree at most
\(D+q-1\). The right side has degree at most
\(E_0+qr-1\), using \(\deg_R G_H\le E_0\) and
\(\deg_R G_R\le E_0-1\).
The degree in (7) strictly exceeds both bounds because
\(qr-1>0\) and \(D-E_0+q-1>0\).
Thus \(p_r=0\), proving \(\deg P\le r-1\) for all
\(n\ge3\).

## 4. A critical fiber of the last polynomial

The last pair
\(T=P_{n-2}\), \(K_*=P_{n-1}\) is a polynomial coordinate
pair over \(L\). Each recurrence in (1) has the inverse
\(P_{i-2}=P_i+A_i(P_{i-1})\); the initial inverse is
\(V=P_1+A_1(P_0)\).
The first pair \((P_0,P_1)\) has Jacobian one in \((U,V)\),
and each subsequent pair change has determinant minus one.
Hence
\[
\det\frac{\partial(T,K_*)}{\partial(U,V)}
 =(-1)^{n-2}=:\epsilon_0 .
\tag{8}
\]

Choose \(k_0\) in an algebraic closure \(\overline L\) with
\(A_n'(k_0)=0\). Such a root exists because \(d_n\ge2\)
and the characteristic is zero. Evaluate the already formed
polynomial identities on \(K_*=k_0\). This is evaluation
over \(\overline L[T]\), not coefficient differentiation of
\(k_0\). In particular no term \(\delta k_0\) is introduced.

Backward substitution gives exact degrees
\[
\begin{gathered}
h_i:=\deg_T(P_i|_{K_*=k_0})
 =\prod_{j=i+2}^{n-1}d_j
 \quad(0\le i\le n-2),\qquad h_{n-2}=1,\\
h_{i-2}=d_i h_{i-1},\qquad
M:=\deg_T(V|_{K_*=k_0})=r h_0\ge4,\\
(K_*)_U\big|_{K_*=k_0}
 =-\epsilon_0\frac{d}{dT}(V|_{K_*=k_0}),\qquad
\deg_T((K_*)_U|_{K_*=k_0})=M-1 .
\end{gathered}
\tag{9}
\]
For the degree formula, start with \(P_{n-2}=T\) and
\(P_{n-1}=k_0\). At each backward step the nonlinear
composition has larger degree than the added later residual,
so its nonzero leading coefficient cannot cancel.
Also \(V=P_1+A_1(P_0)\) has degree \(r h_0\), since
\(r h_0>h_1\).
The inverse Jacobian formula applied to (8) gives the derivative
identity in (9). It remains valid on this fiber. Characteristic
zero makes its leading derivative nonzero.

## 5. The coefficient derivatives have strictly smaller fiber degree

The initial bound \(\deg P\le r-1\) gives
\(\deg_T(Q_1|_{K_*=k_0})\le(r-1)h_0=M-h_0\).
We claim inductively that
\[
\deg_T(Q_i|_{K_*=k_0})\le M-h_{i-1}
\quad(1\le i\le n-2),\qquad
\deg_T(Q_{n-2}|_{K_*=k_0})\le M-d_{n-1}\le M-2 .
\tag{10}
\]
A zero polynomial satisfies these upper bounds by convention.
For \(i\ge2\), the product term in (3) has degree at most
\[
(d_i-1)h_{i-1}+M-h_{i-2}=M-h_{i-1}.
\]
The coefficient-derivative term has degree at most
\(d_i h_{i-1}=h_{i-2}\), also below the desired bound,
because
\(h_{i-2}+h_{i-1}<2h_0\le M\).
The remaining term \(Q_{i-2}\) has smaller allowed degree
by induction; at \(i=2\), it is simply the constant \(-c\).
This proves (10). For \(n=3\), its last bound is already
the initial \(Q_1\) bound, with \(h_0=d_2\).

The identity \(\mathscr D\Phi=\alpha(K_*)_U\), evaluated
at the critical point after differentiation, becomes
\[
A_{n,\delta}(k_0)+\lambda_\delta T
 +\lambda\,Q_{n-2}|_{K_*=k_0}+\nu_\delta
 =\alpha(K_*)_U|_{K_*=k_0} .
\tag{11}
\]
Its left side has degree at most \(\max(1,M-2)\), by (10).
Its right side has the exact degree \(M-1\), by (9) and
\(\alpha\ne0\). Since \(M\ge4\), these are incompatible.
This proves the differential-field obstruction.

The algebraic closure is only a place to evaluate a polynomial
identity and derive a contradiction. It is not used to select
an unchecked factor of a generic curve or to replace the exact
coefficient field in an actual canonical-tail statement.

## 6. Conditional actual-frame gate and scope

In the normalized actual dense setting153, use the retained
literal tails139/145, so
\[
\begin{gathered}
L[y,z]=L[v],\qquad
\ker(L[U,V]\longrightarrow L[v])=(\Phi),\\
\deg\Phi=d=\mu+1,\qquad
f_\mu=\gamma\tau^d,\quad\gamma\in\mathbb C^*,\\
\Psi(y,z)=v+\beta_0,\quad\beta_0\in L,\qquad
\deg\Psi\le d,\qquad \Psi_U=\Phi_\tau .
\end{gathered}
\tag{12}
\]
The improved second-tail degree bound uses the normalized
complex polynomial \(f_\mu\). Association to the whole generic
kernel and the exact polynomial-line equality are retained
actual results, not consequences of an arbitrary formal chain.[^2]

Suppose the literal \(\Phi\), in those fixed \(U,V\) axes,
has the form (1). Its degree is \(\prod_{i=1}^n d_i\).
The formal pair inverse preceding (8) shows
\(L[U,V]/(\Phi)=L[P_{n-1}]\), by solving
\(P_{n-2}=-(A_n(P_{n-1})+\nu)/\lambda\).
Consequently \(P_{n-1}(y,z)\) is affine-linear in \(v\).
The canonical parameter in (12) then gives
\(\Psi-\alpha P_{n-1}-\beta\in(\Phi)\) for some
\(\alpha\in L^*\), \(\beta\in L\).
Since \(\deg P_{n-1}=\prod_{i=1}^{n-1}d_i<d\) and
\(\deg\Psi\le d\), the quotient is a coefficient
\(c\in L\). Thus the exact hypothesis (2) holds with
\(\delta=\partial_\tau\) on the finite separable field \(L\).
The obstruction applies to every such literal chain of length
at least three.

This conditional gate is distinct from proving that every
nongraph embedded line has such a chain in its fixed normalized
axes. No exhaustive plane-embedding reduction is proved here.
The length-two case is also not part of this differential-field
statement; it requires the separate actual-coordinate argument154.
There is no conclusion about arbitrary entry into a three-good
frame, the full cancellation problem, or historical novelty.
No finite tests, human expert certification, recursive audit of
all retained sources, or proof-assistant verification are claimed.

## Sources and retained inputs

1. [Three-stage gradient obstruction155](three-stage-gradient-obstruction-pass155-working.md).
   The length-three first-degree comparison is reproduced in
   Section 2. The new longer-chain degree and critical-fiber
   argument is written explicitly here.
2. [Leading normalization153](dense-all-degree-leading-normalization-pass153-working.md),
   [dense chart139](dense-all-degree-taylor-chart-pass139-working.md),
   [signed negative tails139](dense-negative-tail-relations-pass139-working.md),
   and [first-tail primitivity145](common-gauss-integrality-tail-primitivity-pass145-working.md).
   The exact actual canonical hypotheses in (12), including
   the bounded second tail and whole generic-line parameter.
3. [Two-stage exclusion154](two-stage-nongraph-continuation-pass154-working.md).
   This is the distinct length-two endpoint, not a premise of
   the differential-field obstruction for \(n\ge3\).

[^1]: Source 1. Only the elementary first-degree calculation is
    invoked, and it is displayed in this note.
[^2]: Source 2. No root of a coefficient polynomial introduced
    in Sections 4--5 changes those exact-field actual hypotheses.
