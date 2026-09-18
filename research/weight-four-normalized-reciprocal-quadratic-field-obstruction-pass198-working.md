# Exact field-return obstruction for the normalized reciprocal quadratic projection

Status: bounded working exclusion, pending independent source review.
For the actual square-root initial kernel, the normalized reciprocal
family \(f=1/q\) cannot occur in the quadratic-projection alternative.
The scalar equations force all projected entries to depend on the
coefficient parameter through a cubic function. Actual field return
would make that cubic generate the full rational function field,
which is impossible.

This proof starts with normalized actual potentials. The original
polynomial normalization of arbitrary lower terms is a separate
obligation. Nothing is inferred from a formal rational chart alone.

## 1. Actual normalized hypotheses

Retain the actual globally sliced chart of
[universal184](weight-four-universal-chart-potentials-pass184-working.md):
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad
\deg_E(X,Y,Z,W)=(1,1,2,2),\\
\ker\theta_0=(\mathsf Z^2-\mathsf X^3\mathsf Y),\qquad q^2=t,\\
[L:\mathbb C(t,\rho)]<\infty,\quad
K=\ker_L\partial_\rho,\quad [K:\mathbb C(q)]<\infty,\quad
\ker_K\partial_q=\mathbb C,\\
L[y,z,w]=L[y,\vartheta]=L[v],\qquad
\mathbb C(y,z,w)=L(v),\\
\det\frac{\partial(Y,Z,W)}{\partial(t,\rho,v)}
=-(EX)^3\in L^* .
\end{gathered}
\tag{1}
\]
The determinant is independent of \(X\). The initial ideal is the
entire kernel. The variables \(t,\rho\) are independent, and \(v\)
is the exact generic-line parameter with \(Nv=1\).
No rationality of \(K\), original-ring unit speed, or polynomial
coordinate status of \(q\) is assumed.

Assume the following actual coefficient normalization:
\[
R=q,\qquad k=q\rho,\qquad n=-\frac q2\rho^2,\qquad
\ell=-\frac q2\rho^3+l,\quad l\in K,\qquad f=1/R=1/q.
\tag{2}
\]
These are hypotheses for this note, not a conclusion from the
classification of necessary ODEs. Put \(g=l/q\in K\). Subscripts \(q\)
below differentiate with respect to \(q\), extending to the exact
finite fields and holding \(\rho\) fixed; thus
\(\partial_t=(2q)^{-1}\partial_q\).

## 2. Universal potentials and the quadratic parametrization

The second and third universal potentials, evaluated after taking
their coefficient derivatives, give
\[
\begin{gathered}
P(U)=\frac{\rho^2}{2}+\frac{\rho U}{2q^2}-\frac{3U^2}{8q^4},
\qquad \zeta=\vartheta-P(y),\qquad h=\rho-\frac{y}{2q^2},\\
z=q\zeta+\frac{yh}{q},\qquad
w=h\zeta+\frac{yh^2}{2q^2}+g.
\end{gathered}
\tag{3}
\]
For example the second potential is
\(z=-y^2/(8q^3)+\rho y/(2q)+q\vartheta-q\rho^2/2\);
substitution of \(P\) gives exactly (3).
Substitution of (2) in \(Rw+S(y,\vartheta)=\ell\) gives the
displayed third potential, including the additive term \(g\).

The cleared fourth-potential eliminant is
\[
\mathcal H(U,V)
=-\frac{q^2}{2}(V-P(U))^2
-\frac{qg_q}{2}U
+\frac{5q^2\rho^4}{8}-q^2\rho g-qm,
\qquad m\in L.
\tag{4}
\]
This follows directly from
\(R(T-\ell_tU-\ell_\rho V-m)+(R'U+n_\rho)(\ell-S)\)
using the universal polynomials \(S,T\).
In particular its linear remainder is \(B_1=-qg_q/2\).

We consider only the quadratic-projection alternative \(B_1\ne0\).
Thus \(g_q\ne0\), and \(\mathcal H(y,\vartheta)=0\) becomes
\[
y=-\frac{q\zeta^2}{g_q}+\mathcal B,\qquad
\mathcal B=\frac{5q\rho^4/4-2q\rho g-2m}{g_q}\in L.
\tag{5}
\]
Since \(\vartheta=\zeta+P(y)\), (1) and (5) give
\(L[\zeta]=L[v]\). Hence \(\zeta\) is affine over \(L\), and
\(\Gamma=N\zeta\in L^*\).
Changing to the coordinates \((q,\rho,\zeta)\) retains the
calibrated scalar determinant
\[
J_0:=\det\frac{\partial(y,z,w)}{\partial(q,\rho,\zeta)}
=-\frac{2q(EX)^3}{\Gamma}\in L^* .
\tag{6}
\]
Coefficient partials now fix \(\zeta\); their values on \(L\)
are unchanged.

## 3. Three determinant coefficients force a Laurent polynomial

One can expand the determinant without a long matrix expression.
Set \(H=h/q=\rho/q-y/(2q^3)\). Then
\(z=q\zeta+yH\) and \(w=Hz-yH^2/2+g\).
Row subtraction in \(dy\wedge dz\wedge dw\) gives
\[
J_0=qg_q y_\rho
-\zeta\left(qy_q+
       \left(\rho-\frac{3y}{2q^2}\right)y_\rho\right)
+y_\zeta\left(\zeta^2-\frac{yg_q}{q}\right).
\tag{7}
\]
For example, after removing multiples of \(dy,dz\), the last row
is \(\zeta\,d\rho+
(g_q+\zeta(-\rho/q+3y/(2q^3)))\,dq\);
this verifies the signs in (7).

Substituting (5), the only nonconstant coefficients are
\[
\begin{aligned}
[\zeta^3]J_0
&=-\frac{2q^3g_{qq}+6q^2g_q+3\mathcal B_\rho g_q}
          {2qg_q^2},\\
[\zeta]J_0
&=-\frac{2q^3\mathcal B_q+2q^2\rho\mathcal B_\rho
                 -4q^2\mathcal B-3\mathcal B\mathcal B_\rho}
          {2q^2},\\
[\zeta^0]J_0&=q\mathcal B_\rho g_q .
\end{aligned}
\tag{8}
\]
The scalarity and nonvanishing in (6) therefore imply
\[
\begin{gathered}
\mathcal B=a\rho+b,\qquad
a=-\frac{2q^2}{3}\left(\frac{qg_{qq}}{g_q}+3\right)\in K^*,
\qquad b\in K,\\
2q^3a_q-2q^2a-3a^2=0,\qquad
2q^3b_q-4q^2b-3ab=0.
\end{gathered}
\tag{9}
\]
Indeed the cubic coefficient first makes
\(\mathcal B_\rho=a\in K\); subtracting \(a\rho\) then gives \(b\in K\).
The linear coefficient can be compared in the independent \(\rho\).

Differentiating the expression for \(a\) gives the exact identity
\[
2q^3a_q-2q^2a-3a^2
=-\frac{4q^4}{3g_q}
       \left(q^2g_{qqq}+8qg_{qq}+12g_q\right).
\tag{10}
\]
Consequently the expression in parentheses is zero.
Its complete solution in the exact finite field is
\[
\begin{gathered}
g=\frac{\alpha}{q^2}+\frac{\beta}{q^3}+\gamma,\qquad
\alpha,\beta,\gamma\in\mathbb C,\quad \beta\ne0,\\
a=\frac{2\beta q^2}{2\alpha q+3\beta},\qquad
b=\frac{\delta q^3}{2\alpha q+3\beta},\qquad \delta\in\mathbb C.
\end{gathered}
\tag{11}
\]
Here completeness requires no analytic ansatz. The two expressions
\[
-\frac{q^3}{2}(qg_{qq}+4g_q),\qquad
\frac{q^4}{3}(qg_{qq}+3g_q)
\]
have derivative zero under the equation in (10), so are complex
constants \(\alpha,\beta\); subtracting
\(\alpha/q^2+\beta/q^3\) leaves the constant \(\gamma\).
The condition \(a\ne0\) forces \(\beta\ne0\).
Finally the last equation in (9) says that
\(((2\alpha q+3\beta)b/q^3)_q=0\), giving \(\delta\).
All divided factors are nonzero field elements.

## 4. The projected entries see only a cubic function

Set
\[
\xi=q\zeta,\qquad
T=g-\gamma=\frac{\alpha}{q^2}+\frac{\beta}{q^3},
\qquad
\mathcal P=\frac{Ty-(\xi^2+\delta)/2}{\beta}.
\tag{12}
\]
The symbol \(T\) in this section is a coefficient function, not the
fourth-potential polynomial in the universal chart.

Equations (5) and (11) are equivalent to
\[
(2\alpha q+3\beta)y
=q^3\xi^2+2\beta q^2\rho+\delta q^3.
\tag{13}
\]
Thus \(y,\xi\) are independent over \(K\): \(\xi\) is transcendental
over \(L\), and (13) is an invertible affine change between \(\rho\)
and \(y\) over \(K(\xi)\).
It also gives \(h/q=\mathcal P\), by direct rearrangement.
Consequently the projected entries take the form
\[
z=\xi+y\mathcal P,\qquad
w=\xi\mathcal P+\frac y2\mathcal P^2+T+\gamma
\quad\in\mathbb C(y,\xi,T).
\tag{14}
\]
In particular all their dependence on \(q\) is through \(T\).

Now use actual field return, not merely the potential equations.
Initially \(L/K(\rho)\) could be a proper finite extension. But (1),
(13), and (14) imply the following inclusions in the same field:
\[
L(\xi)=\mathbb C(y,z,w)
\ \subseteq\ \mathbb C(y,\xi,T)
\ \subseteq\ K(y,\xi)=K(\rho,\xi)
\ \subseteq\ L(\xi).
\tag{15}
\]
Every inclusion is an equality. Comparing rational functions in
the independent \(\xi\) gives \(L=K(\rho)\).
Intersecting the middle equality with \(K\), using independence
of \(y,\xi\), gives
\[
K=\mathbb C(T).
\tag{16}
\]

This is impossible. Put \(p=1/q\). Then
\(T=\alpha p^2+\beta p^3\), with \(\beta\ne0\).
Since \(p\in K\) and \(T\in\mathbb C(p)\), (16) would imply
\(\mathbb C(p)=\mathbb C(T)\).
In fact \([\mathbb C(p):\mathbb C(T)]=3\).
For an elementary proof, use an independent variable \(S\):
\(\beta P^3+\alpha P^2-S\) is irreducible in
\(\mathbb C[P,S]\), since its quotient identifies \(S\) with
\(\beta P^3+\alpha P^2\) and is the domain \(\mathbb C[P]\).
It is primitive as a polynomial in \(P\) over \(\mathbb C[S]\),
so Gauss's lemma makes it irreducible over \(\mathbb C(S)\).
Substituting \(S=T\), which is transcendental, gives the asserted
degree three. This contradicts (16) and proves the exclusion.

## Scope and checks

The conclusion is only the impossibility of the normalized actual
reciprocal quadratic-projection branch (1)--(2).
The graph alternative is a separate argument. To exclude the entire
reciprocal family \(f=\beta_0/q\), one must first apply a valid
original polynomial normalization, preserving all the hypotheses,
and then treat both alternatives.

The nonmonomial \(f=at+bq\) family with \(a\ne0\), the two-root
nonzero-R branches, higher profiles and arbitrary coordinate entry
are not settled. The full cancellation goal remains active.
There is no human expert review, proof-assistant certification,
novelty clearance or external communication.

The raw determinant was independently expanded in a new inline
symbolic calculation, and the ODE/parameter/field-containment identities
were checked separately. These are exploratory arithmetic, not extra
canonical test-suite runs. No197 or earlier source was changed.

