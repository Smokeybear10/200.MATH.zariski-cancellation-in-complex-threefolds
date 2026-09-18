# Unit selected cofactor and affine first projection for two quartic forms

**Status: working proof, pending independent saved-source review.**

Under the actual hypotheses of the
[whole-plane completion184](weight-four-bad-linear-whole-plane-projection-pass184-working.md),
for either \(X^2Z+Y^2W\) or \(X^2Z+XYW-Y^4\), the evaluated
cofactor of the selected plane relation is a nonzero field scalar.
Moreover the first projected entry \(y\) is constant or affine in
the normalized generic parameter. No constant-projection exclusion
or original-ring recognition is assumed.

## 1. Exact retained identities

Use the exact field \(L\), parameter \(v\), projected entries
\(y,\vartheta,w\), and actual scalar \(J_0=-a^3\in L^*\) from the
universal chart and its whole-plane companion. In particular
\[
O=L[v]=L[y,\vartheta],\qquad
L[y,\vartheta,w]=O,\qquad
\deg G=\max(\deg_vy,\deg_v\vartheta)\le5,
\tag{1}
\]
where \((G)\) is the full prime relation ideal of \((y,\vartheta)\).
Write
\[
\begin{gathered}
S=g_3,\quad \mathcal R(U)=k_\rho-cU,\quad
c=2t\ \hbox{or}\ 1,\quad c\in L^*,\quad c_\rho=0,\\
R=\mathcal R(y)\ne0,\quad A=S_V(y,\vartheta),\quad
B_1=S_U(y,\vartheta)-cw,\\
C_i=S_i(y,\vartheta)+\mathcal R_i(y)w-\ell_i,\quad i=t,\rho,\\
\mathcal P=\mathcal R W_0+S-\ell,\qquad
\Psi=S_VW_0+g_4-\ell_tU-\ell_\rho V,\\
\mathcal P(y,\vartheta,w)=0,\qquad
\Psi(y,\vartheta,w)=m .
\end{gathered}
\tag{2}
\]
All coefficient partials precede evaluation. The formal gradients
after evaluation are \((B_1,A,R)\) for \(\mathcal P\), and
\((C_t,C_\rho,A)\) for \(\Psi\). The determinant identity is
\[
J_0=\left[
dy\wedge(R\,d\vartheta+B_1dt+A\,d\rho)\wedge dw
\right]_{dt\wedge d\rho\wedge dv}.
\tag{3}
\]

The plane eliminant and its selected factor satisfy
\[
\begin{gathered}
\mathcal H=\mathcal R(g_4-\ell_tU-\ell_\rho V-m)
                  +S_V(\ell-S)=GQ,\\
\deg\mathcal H=5,\qquad \deg_V\mathcal H\le3,\qquad
G\nmid Q,\qquad 0\ne Q(y,\vartheta)\mid R^2,\\
\mathcal H_U(y,\vartheta)=RC_t-AB_1,\qquad
\mathcal H_V(y,\vartheta)=RC_\rho-A^2 .
\end{gathered}
\tag{4}
\]
The degree-five statement and simple selection were proved in the
companion. To check the additional \(V\)-degree bound directly, in
both forms \(S\) has \(V\)-degree at most two, \(S_V\) at most one,
\(g_4\) at most three, and \(\mathcal R\) is independent of \(V\).
Thus every summand in the displayed eliminant has \(V\)-degree
at most three. No full-plane coordinate theorem is used here.

## 2. The two return coefficients have no common zero

We prove
\[
(R,A)O=O.
\tag{5}
\]
Suppose instead that \(R,A\) vanish together at a parameter value
\(v_0\) over an algebraic closure of \(L\). Put
\(\lambda=k_\rho/c\), so \(y(v_0)=\lambda\), and define
\[
p(V)=S(\lambda,V)-\ell,\qquad
\deg_Vp\le2,\qquad [V^2]p=k_{\rho\rho}/2.
\tag{6}
\]
The potential and \(A=0\) give
\(p(\vartheta(v_0))=p'(\vartheta(v_0))=0\).

If \(p=0\) identically, the exact formal division from the
companion gives
\(\mathcal P=\mathcal R(W_0-\overline D(U,V))\).
Because \(R\ne0\) and \(O\) is a domain, \(w=\overline D(y,\vartheta)\)
on the entire line. At \(v_0\), the three formal gradient entries
\(B_1,A,R\) are consequently zero. The middle row in (3) would
vanish, contrary to \(J_0\ne0\).

Otherwise (6) and the common root imply
\[
p(V)=\kappa(V-\vartheta_0)^2,\qquad
\kappa=k_{\rho\rho}/2\in L^*,\quad \vartheta_0\in L,\qquad
\vartheta(v_0)=\vartheta_0.
\tag{7}
\]
At the alleged common zero, \(B_1\ne0\), since otherwise the
middle row in (3) again vanishes. Differentiate the first
potential in the parameter direction, fixing \(L\):
\[
B_1y_v+A\vartheta_v+Rw_v=0.
\]
Evaluation at \(v_0\) therefore gives \(y_v(v_0)=0\).

Now use the exact coefficient-field identity
\(\ell=S(\lambda,\vartheta_0)\). Differentiating it in the rho
direction, and using \(S_V(\lambda,\vartheta_0)=0\), yields
\[
\ell_\rho=S_\rho(\lambda,\vartheta_0)
                   +\lambda_\rho S_U(\lambda,\vartheta_0),
\qquad
\lambda_\rho=\frac{k_{\rho\rho}}c=\frac{2\kappa}c\ne0.
\tag{8}
\]
The possible derivative of the moving center \(\vartheta_0\)
has zero coefficient. Since
\(\mathcal R_\rho=k_{\rho\rho}\), (8) gives, at \(v_0\),
\[
C_\rho=k_{\rho\rho}w-\lambda_\rho S_U
       =-\lambda_\rho B_1\ne0.
\tag{9}
\]
Differentiating the second potential in \(v\) gives
\(C_ty_v+C_\rho\vartheta_v+Aw_v=0\).
Consequently \(\vartheta_v(v_0)=0\).

But the whole-plane equality (1) provides a polynomial
\(T(U,V)\in L[U,V]\) with \(T(y,\vartheta)=v\).
Differentiating and then evaluating gives
\(1=T_Uy_v+T_V\vartheta_v=0\), a contradiction.
All root evaluations occur after forming the indicated identities.
In particular (8) differentiates a coefficient-field identity, not
the algebraic parameter value \(v_0\).
Thus there is no common zero over the algebraic closure, proving (5).
This also covers constant \(y\), where \(R\in L^*\) already proves it.

## 3. Unit cofactor and the degree-two bound on y

If the nonzero polynomial \(Q(y,\vartheta)\) had a zero, its
divisibility into \(R^2\) in (4) would force \(R=0\) there.
At that point \(\mathcal H_V=QG_V=0\), so the last identity in
(4) gives \(A=0\). This contradicts (5). Therefore
\[
Q(y,\vartheta)=\omega\in L^*,\qquad
Q-\omega\in(G).
\tag{10}
\]
It is important that this is an evaluated-unit assertion:
the polynomial \(Q(U,V)\) itself is not yet asserted constant.

Suppose \(y\) is nonconstant. At a root \(v_0\) of \(R\) one
has \(A(v_0)\ne0\). If \(y_v(v_0)=0\), the derivative of the
first potential would give \(\vartheta_v(v_0)=0\), contradicting
the same polynomial inverse \(T\). Thus
\(R_v(v_0)=-c y_v(v_0)\ne0\).
The polynomial \(R\) is squarefree.

Distinct roots of \(R\) have distinct values of \(\vartheta\):
otherwise they have the same pair \((y,\vartheta)\), contradicting
the polynomial inverse. At each root the potential gives
\(p(\vartheta)=0\) for the center in (6).
This center is nonzero, since if it were zero then its derivative
would make \(A=0\) at every such root. Hence the degree at most two
of \(p\), together with squarefreeness of \(R\), proves
\[
1\le\deg_vy=\deg_vR\le2.
\tag{11}
\]
Neither this step nor (10) invokes an algebraically closed
coefficient-field hypothesis; algebraic closure is used only to
count roots of exact polynomials.

## 4. A degree-two first projection contradicts the quintic

Suppose \(\deg_vy=2\). After an affine parameter translation
over \(L\), write \(y=b+a_2x^2\), \(a_2\in L^*\).
The degree bound (1) expresses the other polynomial as
\[
\vartheta=P_2(y)+xD(x^2),\qquad
\deg P_2\le2,\quad \deg D\le2.
\tag{12}
\]
The formal inverse \(T(y,\vartheta)=x\) implies
\(D(0)=\vartheta_x(0)\ne0\), by differentiation at \(x=0\).
If \(D\) were nonconstant, it would have a nonzero root \(s\)
over an algebraic closure. At \(x_0^2=s\), the distinct points
\(x_0,-x_0\) would have the same \(y\) and \(\vartheta\), contrary
to the inverse. Thus \(D\) is a nonzero constant.
Rescale the affine parameter to \(\zeta=D x\). Over the same
exact field \(L\) this gives
\[
y=b+a\zeta^2,\quad
\vartheta=P_2(y)+\zeta,\quad a\in L^*,\qquad
G=U-b-a(V-P_2(U))^2 .
\tag{13}
\]
The displayed \(G\) generates the full relation ideal: put
\(T_0=V-P_2(U)\), then recover \(U=G+b+aT_0^2\) and
\(V=T_0+P_2(U)\). These are formal polynomial inverse formulas
over \(L\), not changes of the original complex fourfold.

If \(P_2\) has degree two, \(G\) has total degree four.
Then \(Q=\mathcal H/G\) has degree one. Equation (10) makes
\(Q-\omega\) divisible by the degree-four \(G\), so
\(Q=\omega\). This contradicts \(\deg\mathcal H=5\).

If \(P_2\) has degree at most one, including a constant or zero,
\(G\) has total degree two and degree two in \(V\), with leading
\(V\)-coefficient \(-a\). Equation (10) now gives
\[
\mathcal H=\omega G+L_1(U,V)G^2,\qquad \deg L_1\le1.
\tag{14}
\]
Write \(L_1=\alpha U+\beta V+\gamma\). The coefficient of \(V^5\)
in (14) is \(\beta a^2\), so \(\deg_V\mathcal H\le3\) forces
\(\beta=0\). Its coefficient of \(V^4\) is then
\(a^2(\alpha U+\gamma)\), forcing \(\alpha=\gamma=0\).
Again \(\mathcal H=\omega G\) contradicts its degree five.
Both cases exclude degree-two \(y\).

Combining this with (11), the conclusion for both actual forms is
\[
\boxed{\,y\in L\quad\hbox{or}\quad y=\gamma v+\eta,\qquad
                 \gamma\in L^*,\ \eta\in L.\,}
\tag{15}
\]
If the second alternative holds, the whole-line conclusion makes
\(\vartheta\) a polynomial in \(y\) of degree at most five.
This is only a projected graph over \(L\).

## Scope and verification

The universal and whole-plane184 proofs and the simple-selected
component176 argument were read for this derivation. The moving-center
coefficient identity, unit argument, root count and quadratic
parameter calculation are all reproduced here with the new factor
\(c=2t\) or \(1\). No Abhyankar--Moh theorem or other plane-embedding
classification is used.

The actual constant-\(y\) branch is not excluded, and no global
invariant coordinate or recognition is obtained. The proof does not
replace an evaluated constant cofactor with an unwarranted literal
constant-cofactor assertion. No checker was written, executed,
imported or compiled, and no earlier file was changed. This is not
an arbitrary-entry, unrestricted-cancellation, novelty, human-expert
or proof-assistant claim.
