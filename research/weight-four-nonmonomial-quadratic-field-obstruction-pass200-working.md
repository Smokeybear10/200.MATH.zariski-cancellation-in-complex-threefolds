# Quartic field-return obstruction for the normalized nonmonomial projection

Status: bounded working proof, awaiting independent source review.
Under the actual normalized square-root hypotheses below, the
nonmonomial quadratic-projection alternative is impossible. The
obstruction is an irreducible quartic over the actual projected
rational function field, not a numerical test or a rationality
assumption on the coefficient field.

## 1. Actual normalized hypotheses

Retain the globally sliced actual chart of
[universal184](weight-four-universal-chart-potentials-pass184-working.md)
and the normalization of
[nonmonomial199](weight-four-nonmonomial-square-root-actual-normalization-pass199-working.md):
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=\mathcal A[u],\qquad E=\partial_u,\qquad
\deg_E(X,Y,Z,W)=(1,1,2,2),\\
\ker\theta_0=(\mathsf Z^2-\mathsf X^3\mathsf Y),\qquad q^2=t,\\
K=\ker_L\partial_\rho,\quad [K:\mathbb C(q)]<\infty,\quad
\ker_K\partial_q=\mathbb C,\quad [L:K(\rho)]<\infty,\\
L[y,z,w]=L[y,\vartheta]=L[v],\qquad
\mathbb C(y,z,w)=L(v),\qquad Nv=1.
\end{gathered}
\tag{1}
\]
The initial kernel is the entire ideal. The actual scalar Jacobian
from that chart is retained. In particular \(y,z,w\) are algebraically
independent over \(\mathbb C\), and actual field return in (1) is an
equality inside the same ambient field. It is not inferred from the
potentials.

The canonical coefficient potentials are
\[
\begin{gathered}
R=\frac1{q(q+1)},\qquad
\nu=\frac1{q^3(q+1)^3(3q-1)},\qquad
k=R\rho,\quad n=\nu\rho^2/2,\\
\ell=-\frac{q^2+4q-1}{2q^5(q+1)^5(3q-1)^3}\rho^3+Rg,
\qquad g\in K .
\end{gathered}
\tag{2}
\]
The \(q\)-derivatives below fix \(\rho\); they extend uniquely to
the finite coefficient fields. Thus \(\partial_t=(2q)^{-1}\partial_q\).
Denominators are nonzero field elements, not original-ring units.

## 2. Simplified projected equations

Use the literal \(S,T,\mathcal H\) and square polynomial \(P\) in
[normalization199, equations (5)--(6)](weight-four-nonmonomial-square-root-actual-normalization-pass199-working.md).
Specifically
\[
\begin{gathered}
\Delta=RR_{tt}/2-R_t^2,\quad
\mathcal B=Rn_{t\rho}-2R_tn_\rho,\quad
\mathcal C=-R\ell_\rho-n_\rho^2,\\
P(U)=-\frac{\Delta U^2+\mathcal B U+\mathcal C}{R\nu},\qquad
\zeta=\vartheta-P(y),\qquad \xi=R\zeta,\\
D=q(q+1)(3q-1),\qquad h=\frac{y}{2q}-\frac{\rho}{D}.
\end{gathered}
\tag{3}
\]
Taking coefficient derivatives before substituting \(U=y,V=\vartheta\),
the second and third potentials give the short identities
\[
z=\xi-\frac32h^2,\qquad
w=(h+y)z+\frac12h^3+g.
\tag{4}
\]
They can be checked directly by substituting
\(\rho=D(y/(2q)-h)\) into
\[
z=-\frac{y^2}{8q^3}+k_ty+R\vartheta+n,\qquad
w=\frac{\ell-S(y,\vartheta)}R .
\]
No free change of the original polynomial coordinates is involved in
(3)--(4); these are identities in the actual fraction field.

The square eliminant has linear remainder
\[
\mathcal H(U,V)=\frac{R\nu}{2}(V-P(U))^2+B_1U+B_0,\qquad
B_1=-\frac{R^2g_q}{2q},\qquad B_0\in L.
\tag{5}
\]
We treat the quadratic-projection case \(B_1\ne0\), so \(g_q\ne0\).
Set
\[
e=\frac q{3q-1},\qquad A=\frac e{g_q},\qquad
y=A\xi^2+\mathcal D,\quad \mathcal D=-B_0/B_1\in L .
\tag{6}
\]
The factor is \(A=q\nu/(R^3g_q)=q/((3q-1)g_q)\).
The power \(R^3\) matters: \(\xi=R\zeta\), rather than \(\zeta\),
is the parameter used here.

Equations (3) and (6) imply
\(L[y,\vartheta]=L[\xi]=L[v]\).
Thus \(\xi\) is an affine parameter of the whole generic line and
\(\Gamma=N\xi\in L^*\). The calibrated determinant becomes
\[
J=\det\frac{\partial(y,z,w)}{\partial(q,\rho,\xi)}
=-\frac{2q(EX)^3}{\Gamma}\in L^* .
\tag{7}
\]
It is independent of \(\xi\). Replacing \(\zeta\) by \(\xi\) does not
lose the parameter-speed factor.

## 3. Scalarity forces a complete exact-field ODE

Subtracting \(yz\) from the last projected coordinate in (4) leaves
\(\omega=hz+h^3/2+g\). Hence
\[
d\omega-h\,dz=\xi\,dh+g_q\,dq,\qquad
dh=\frac{dy}{2q}
 +\left(-\frac y{2q^2}+\frac{\rho D_q}{D^2}\right)dq
 -\frac{d\rho}{D}.
\]
Taking exterior products, or expanding the determinant, gives
\[
J=g_q y_\rho+
\xi\left\{\left(-\frac y{2q^2}+\frac{\rho D_q}{D^2}\right)y_\rho
                  +\frac{y_q}{D}\right\}
-\frac{3hg_q}{D}y_\xi .
\tag{8}
\]
After substituting (6), only the powers \(\xi^3,\xi,1\) occur:
\[
\begin{aligned}
[\xi^3]J&=-\frac{A\mathcal D_\rho}{2q^2}
             +\frac{A_q}{D}-\frac{3g_qA^2}{qD},\\
[\xi]J&=\left(-\frac{\mathcal D}{2q^2}
                  +\frac{\rho D_q}{D^2}\right)\mathcal D_\rho
          +\frac{\mathcal D_q}{D}
          -\frac{3e\mathcal D}{qD}+\frac{6e\rho}{D^2},\\
[1]J&=g_q\mathcal D_\rho .
\end{aligned}
\tag{9}
\]
Consequently
\[
\begin{gathered}
\mathcal D=a\rho+b,\qquad a\in K^*,\ b\in K,\\
a=\frac{2q^2}{D}\left(\frac{A_q}{A}-\frac{3e}{q}\right)
=-\frac{2\{q(3q-1)g_{qq}+(3q+1)g_q\}}
        {(q+1)(3q-1)^2g_q},\\
-\frac{a^2}{2q^2}+\frac{D_q a}{D^2}
      +\frac{a_q}{D}-\frac{3ea}{qD}+\frac{6e}{D^2}=0,\qquad
b_q=\left(\frac{aD}{2q^2}+\frac{3e}{q}\right)b .
\end{gathered}
\tag{10}
\]
The cubic coefficient first places \(\mathcal D_\rho\) in \(K\);
subtracting \(a\rho\) gives \(b\in K\). The constant coefficient is
nonzero, which gives \(a\ne0\). The linear coefficient then gives
the last two equations by comparing powers of the transcendental
\(\rho\).

The left side of the first differential equation in (10), after
substitution for \(a\), is exactly
\[
-\frac{2\{(3q-1)g_{qqq}+9g_{qq}\}}
       {(q+1)^2(3q-1)^3g_q}.
\tag{11}
\]
Thus every actual solution satisfies
\((3q-1)g_{qqq}+9g_{qq}=0\). Its complete solution in \(K\) is
\[
g=\alpha q+\frac{\beta}{3q-1}+\gamma,\qquad
\alpha,\beta,\gamma\in\mathbb C,\quad(\alpha,\beta)\ne(0,0).
\tag{12}
\]
For completeness, the derivative of \((3q-1)^3g_{qq}\) is zero.
Call this constant \(18\beta\). Since
\((\beta/(3q-1))_{qq}=18\beta/(3q-1)^3\), subtraction leaves a
function with second derivative zero. Two more constant-field
subtractions give \(\alpha q+\gamma\).
This works in every allowed finite \(K\), with no rational ansatz.

Put
\[
\begin{gathered}
d=\alpha(3q-1)^2-3\beta,\qquad
A=\frac{q(3q-1)}d,\\
a=-\frac{2(9\alpha q^2-\alpha+3\beta)}
          {(q+1)(3q-1)d},\qquad
b=\delta A,\quad \delta\in\mathbb C .
\end{gathered}
\tag{13}
\]
Here \(d\ne0\) because \(g_q\ne0\).
Indeed (10) gives
\(b_q=(A_q/A)b\), so \((b/A)_q=0\).
These formulas include both \(\alpha=0\) and \(\beta=0\);
no division by either individual constant has been made.

## 4. Actual field return contradicts an irreducible quartic

Set \(T=g-\gamma\). Substitute
\(\rho=D(y/(2q)-h)\) into \(y=A(\xi^2+\delta)+a\rho\).
The identities
\[
\frac{1-aD/(2q)}A=6\alpha,\qquad
-\frac{aD}A=6T+2\alpha
\]
give
\[
6\alpha y=\xi^2+\delta+(6T+2\alpha)h .
\tag{14}
\]
In particular this step does not require \(\alpha\ne0\).

From (4),
\(\xi=z+3h^2/2\) and
\(T=w-yz-hz-h^3/2-\gamma\).
Eliminating \(\xi,T\) in (14) therefore yields
\[
F(h)=3h^4+12zh^2-
       \{24(w-yz-\gamma)+8\alpha\}h
       +24\alpha y-4z^2-4\delta=0 .
\tag{15}
\]
All the constants in (15) are complex. Meanwhile actual field return
in (1) and the affine change of generic parameter give
\[
h\in L(\xi)=\mathbb C(y,z,w).
\tag{16}
\]
This is impossible because \(F(H)\) is irreducible of degree four
over \(\mathbb C(y,z,w)\).

Here is an explicit irreducibility argument, including the exceptional
parameter choices. Regard \(F(H)\) first as a polynomial in \(w\)
over the UFD \(\mathbb C[y,z,H]\). Its coefficient of \(w\) is
\(-24H\). Its constant term, reduced modulo \(H\), is
\(24\alpha y-4z^2-4\delta\), which is not the zero polynomial for
any \(\alpha,\delta\). Therefore the two coefficients are relatively
prime. This primitive degree-one polynomial is irreducible over
\(\mathbb C(y,z,H)\), and Gauss's lemma makes it irreducible in
\(\mathbb C[y,z,H,w]\). Viewed instead as a polynomial in \(H\)
over \(\mathbb C[y,z,w]\), it is primitive because its leading
coefficient is the nonzero constant \(3\). A second use of Gauss's
lemma proves the assertion over \(\mathbb C(y,z,w)\).
The algebraic independence in (1) justifies treating these as
independent variables throughout.

Thus \(F\) cannot have the rational-field root in (16). This excludes
the normalized actual nonmonomial quadratic-projection branch.

## Scope, verification and remaining problem

This result needs the actual normalization199 to treat arbitrary lower
potentials, and a separate graph argument to treat the whole
nonmonomial family. It neither assumes nor proves \(K=\mathbb C(q)\).
It makes no statement about arbitrary coordinate entry, the two-root
initial kernel, height-two initial kernels or higher time profiles.

The raw potential simplification, determinant coefficients, exact ODE,
parameter substitution and quartic elimination were checked in new
inline symbolic calculations. They are not executions of a saved
checker. The field-return and irreducibility steps are written
arguments, not conclusions of computer algebra.

There is no human expert review, formal proof certification or
novelty clearance. The unrestricted cancellation problem remains open
in this research program. No external communication or submission
was made, and no198 or earlier source was changed.

