# The cubic graph forces an impossible square in the original polynomial ring

In the actual rebuilt chart \(q=\rho^2-t^3\), the projected branch
\((\deg_vy,\deg_v\theta)=(1,3)\) cannot occur. The full centered
eliminant and the actual cofactor condition determine all relevant
lower potentials up to complex constants. Explicit invertible affine
changes of the original four coordinates then give a polynomial
square identity of degree one in one of those coordinates.

This excludes one branch of the supplied cubic repeated-root model.
It does not settle its other projected degree pairs or an arbitrary
exact1122 frame.

## 1. Actual input and the cubic graph

Use the rebuilt literal \(Z\) chart of
[237](repeated-root-rebuilt-chart-line-exclusion-pass237-working.md)
and the full potentials of
[239](radical-minus-polynomial-centered-eliminant-pass239-working.md).
Thus
\[
\begin{gathered}
\mathscr B=\mathbb C[X,Y,Z,W]=\mathscr A[u],\qquad E=\partial_u,\qquad
\deg_E(X,Y,Z,W)=(1,1,2,2),\\
\ker(\text{full leading evaluation})=(X^2Z-W^2+XY^3),\\
N=[u^3]\partial_Z|_{\mathscr A}\ne0,\qquad
L=\operatorname{Frac}(\ker_{\mathscr A}N),\qquad
\mathscr A_L=L[v],\quad Nv=1,\\
[L:\mathbb C(t,\rho)]<\infty,\qquad q=\rho^2-t^3,\\
Y=y+tX,\quad Z=z+\sigma X+qX^2,\quad
W=w+\theta X+\rho X^2,\quad L[y,z,w]=L[v],\\
J(X)=J_0=-(EX)^3\in L^* .
\end{gathered}                                                    \tag{1}
\]
The displayed full kernel is required, not merely a relation.
The ratios \(t,\rho\) are algebraically independent. Their partials
extend uniquely and commute on the finite separable field \(L\),
then fix \(v\). The chart is reconstructed after the actual bad-slot
exchange from \(Z_{\rm old}^2-X^2W_{\rm old}-XY^3\).
No old selected derivation or field is implicitly transported.

In this note assume the particular remaining branch
\[
\deg_vy=1,\qquad \deg_v\theta=3 .
\tag{2}
\]
Then \(L[y]=L[v]\), and \(\theta=\widehat P(y)\) for a polynomial
\(\widehat P\in L[U]\) of degree three.
Put
\[
\kappa=k_\rho,\quad c=k_{\rho\rho},\quad
\zeta=V+\kappa/2,\quad P(U)=\widehat P(U)+\kappa/2,\quad
G(U,\zeta)=\zeta-P(U).
\tag{3}
\]
Here \(U,V,\zeta\) are formal plane variables. The shift in (3) is
over \(L\), not an ambient coordinate change.
The evaluated return polynomial is \(R=2P(y)\ne0\).

The local theorem of
[238](repeated-root-return-excess-order-bound-pass238-working.md)
gives \(q_1\mid R\), since \(\deg_vy=1\).
The exact evaluated gradient, together with \(G_\zeta=1\), gives
the reverse divisor. Thus the complete centered eliminant \(H\) has
\[
H=GQ_1,\qquad q_1:=Q_1(y,P(y))=\eta R,\qquad \eta\in L^* .
\tag{4}
\]
These conclusions use the actual calibrated determinant. They are not
assumptions on a freely chosen generic graph.

## 2. The entire centered eliminant is a difference of two squares

The complete polynomial \(H\) has total degree six and top \(U^6\).
Since \(G\) has degree three, \(Q_1\) has degree three.
By (4), \(Q_1-2\eta\zeta\) belongs to the evaluation ideal \((G)\).
Consequently
\[
H=G^2M+2\eta\zeta G,\qquad M\in L^* .
\tag{5}
\]
The degree bound makes \(M\) a scalar, not a polynomial of positive
degree. Let
\[
p(U)=S(U,-\kappa/2)-\ell
 =-U^3+\frac{k_{tt}}2U^2+
 \left(n_t-\frac{\kappa k_{t\rho}}2\right)U
 +\frac{\kappa^2c}{8}-\frac{\kappa n_\rho}{2}-\ell .
\tag{6}
\]
The full centered identity239 gives \(H(U,0)=p(U)^2\) and
\([\zeta]H=0\). Since \(P^2M=p^2\), unique factorization in \(L[U]\)
gives \(p=\lambda P\) for \(\lambda\in L^*\), and \(M=\lambda^2\).
No square root extension of \(L\) is used: \(\lambda=p/P\) already
lies in \(L\), since both polynomials have degree three.
The zero linear coefficient in (5) gives \(\eta=-\lambda^2\).
Therefore
\[
\boxed{p=\lambda P,\qquad H=p^2-\lambda^2\zeta^2 .}
\tag{7}
\]
The scalar \(\lambda\) is not assumed complex or regular in the
original ring.

## 3. Exact coefficient identities

Retain arbitrary \(k,n,\ell,m\in L\) in the raw potentials
\[
\begin{aligned}
S={}&-U^3+\frac{k_{tt}}2U^2+k_{t\rho}UV+
                  \frac{k_{\rho\rho}}2V^2+n_tU+n_\rho V,\\
Q={}&\frac{k_{ttt}}6U^3+\frac{k_{tt\rho}}2U^2V+
       \frac{k_{t\rho\rho}}2UV^2+\frac{k_{\rho\rho\rho}}6V^3\\
&+\frac{n_{tt}}2U^2+n_{t\rho}UV+\frac{n_{\rho\rho}}2V^2
                                      -\ell_tU-\ell_\rho V-m,\\
\mathcal R={}&2V+k_\rho,\quad
\beta=k_{t\rho}U+k_{\rho\rho}V+n_\rho,\quad
H=\left((\ell-S)^2+\mathcal R\beta(\ell-S)+\mathcal R^2Q\right)
                                      \big|_{V=\zeta-\kappa/2}.
\end{aligned}                                                    \tag{8}
\]
All coefficient partials in (8) are taken before centering.
Afterwards, (7) says that every positive-\(\zeta\) coefficient
vanishes except its scalar \(\zeta^2\) coefficient.

The coefficients of \(\zeta^5,U\zeta^4,\zeta^4,U^2\zeta^3,
U\zeta^3,U^3\zeta^2\), respectively, give
\[
\begin{gathered}
k_{\rho\rho\rho}=k_{t\rho\rho}=0,\qquad
n_{\rho\rho}=3c^2/8,\\
k_{tt\rho}=0,\qquad n_{t\rho}=c\,k_{t\rho}/2,\qquad
k_{ttt}=-3c/2 .
\end{gathered}                                                    \tag{9}
\]
Write \(a=k_{t\rho}\). The remaining coefficients
\(U^2\zeta^2,\zeta^3,U\zeta^2\) give
\[
\begin{gathered}
n_{tt}=a^2/2+c k_{tt}/4,\\
\ell_\rho=\kappa c^2/16-c n_\rho/2,\qquad
\ell_t=-a n_\rho/2-c n_t/4+c\kappa a/8 .
\end{gathered}                                                    \tag{10}
\]
For example the raw \(U^2\zeta^2\) coefficient is
\(2n_{tt}-a^2-c k_{tt}/2\). The scalar \(\zeta^3\) coefficient is
\(\kappa c^2/4-4\ell_\rho-2c n_\rho\), and the \(U\zeta^2\)
coefficient is \(-4\ell_t-2a n_\rho-c n_t+c\kappa a/2\).
These verify all three entries of (10) directly.
No derivative of a shifted variable is omitted: subsequent
differentiations apply to the resulting equalities in \(L\).

## 4. Complete integration over the exact finite field

The joint constants of \(\partial_t,\partial_\rho\) in \(L\) are
exactly \(\mathbb C\). Indeed, if an element is killed by both,
differentiate its monic minimal polynomial over \(\mathbb C(t,\rho)\).
The resulting polynomial has smaller degree, so all differentiated
coefficients vanish. The coefficients are then joint constants of
\(\mathbb C(t,\rho)\), hence complex. The element is algebraic over
the algebraically closed field \(\mathbb C\), so is complex.

In particular (9) gives \(c,a\in\mathbb C\).
It also makes \(d=k_{tt}+3ct/2\) and
\(b=k_\rho-c\rho-at\) complex. Integrating the remaining first
derivatives gives \(k_0,k_1\in\mathbb C\) and
\[
k=\frac c2\rho^2+(at+b)\rho-\frac c4t^3
                                 +\frac d2t^2+k_1t+k_0 .
\tag{11}
\]
This statement can equivalently be checked without choosing
primitives: the two partials of the difference between \(k\) and
the displayed polynomial vanish successively after defining \(k_1\)
from \(k_t\) and then \(k_0\).

Equations (9),(10) similarly give \(e,f,g\in\mathbb C\) and
\[
n=\frac{3c^2}{16}\rho^2+
    \left(\frac{ca}{2}t+e\right)\rho-\frac{c^2}{16}t^3
    +\left(\frac{a^2}{4}+\frac{cd}{8}\right)t^2+ft+g .
\tag{12}
\]
For precision,
\[
e=n_\rho-\frac{3c^2}{8}\rho-\frac{ca}{2}t,\qquad
f=n_t-\frac{ca}{2}\rho+\frac{3c^2}{16}t^2
                         -\left(\frac{a^2}{2}+\frac{cd}{4}\right)t
\]
have both partials zero by (9),(10); subtracting their polynomial
primitive leaves the complex constant \(g\).

Finally the two specified partials of \(\ell\) in (10) give
\[
\begin{aligned}
\ell={}&\frac{c^3}{64}t^3
 -\left(\frac{ca^2}{8}+\frac{c^2d}{32}\right)t^2\\
&+\left(-\frac{3ac^2}{16}\rho-\frac{ae}{2}
                         -\frac{cf}{4}+\frac{cab}{8}\right)t
 -\frac{c^3}{16}\rho^2+
                  \left(\frac{bc^2}{16}-\frac{ce}{2}\right)\rho+j,
\qquad j\in\mathbb C .
\end{aligned}                                                    \tag{13}
\]
Both derivatives of the displayed expression are the ones in (10).
Their difference from \(\ell\) is a joint constant, proving that
(13) loses no coefficient-field integration mode.
No division by \(a,b,c,d,e,f,g,j,k_0,k_1\) occurs in this integration.
All their zero and degenerate cases are included. The element
\(\lambda\in L^*\) remains unrestricted by this step.

## 5. Explicit changes of actual polynomial coordinates

Set the following complex constants:
\[
\begin{gathered}
n_0=g-\frac{b^2}{4}+\frac{ck_0}{4}+\frac{dk_1}{6},\qquad
B_0=f-\frac{ab}{2}+\frac{d^2}{12},\\
C_0=-\frac{abd}{12}+\frac{b^2c}{8}-\frac{be}{2}
                              +\frac{d^3}{108}+\frac{df}{6}-j .
\end{gathered}                                                    \tag{14}
\]
Define actual coordinates, not coefficient-field replacements, by
\[
\begin{aligned}
X_1&=X-c/4,&\qquad Y_1&=Y-d/6,\\
W_1&=W+aY/2+bX/2-bc/4+e/2,&
Z_1&=Z-k_1Y_1-k_0X_1-n_0 .
\end{aligned}                                                    \tag{15}
\]
This is a complex affine polynomial automorphism. Its exact inverse is
\[
\begin{aligned}
X&=X_1+c/4,&\qquad Y&=Y_1+d/6,\\
W&=W_1-a(Y_1+d/6)/2-b(X_1+c/4)/2+bc/4-e/2,&
Z&=Z_1+k_1Y_1+k_0X_1+n_0 .
\end{aligned}                                                    \tag{16}
\]
Substitution in either order gives the identity. In particular
\(\mathscr B=\mathbb C[X_1,Y_1,Z_1,W_1]\).
Only complex constants are used in (15),(16).

For checking their exact expressions in the faithful chart (1), put
\[
h=y+ct/4-d/6,\qquad
p_0(h)=-h^3+B_0h+C_0,\qquad P_0=p_0(h)/\lambda .
\tag{17}
\]
This parameter \(h\in L[v]\) is used only in the coefficient-field
chart; it is not declared an ambient coordinate.
Substituting (11)--(13) into (6) gives
\(p(y)=p_0(h)\), hence \(P(y)=P_0\).
The centered third potential reads
\[
Rw=-p(y)-\left(a y+n_\rho-\kappa c/2\right)P(y)
                                      -\frac c2P(y)^2 .
\]
Since \(R=2P(y)\) and \(p(y)=\lambda P(y)\), cancellation gives
\[
w=-\frac{\lambda}{2}
       -\frac{a y+n_\rho-\kappa c/2}{2}
       -\frac c4P(y).
\tag{18}
\]
Combining (18) with
\[
\theta=P(y)-\kappa/2,\qquad
z=2\rho w+P(y)^2-\kappa^2/4-3ty^2+k_t y+n,\qquad
\sigma=-3t^2y+2\rho\theta+k
\]
and then applying the actual changes (15) gives
\[
\begin{aligned}
Y_1={}&h+tX_1,\\
W_1={}&-\lambda/2+P_0X_1+\rho X_1^2,\\
Z_1={}&-\rho\lambda+P_0^2-3th^2+B_0t\\
     &+\left(-3t^2h+2\rho P_0\right)X_1
                            +(\rho^2-t^3)X_1^2 .
\end{aligned}                                                    \tag{19}
\]
Every term is retained, especially the constant term
\(-\rho\lambda\) in \(Z_1\). For example, before subtracting \(n_0\)
in (15), the new second lower potential is exactly \(B_0t+n_0\).
These are direct identities in the existing faithful localization.
No new choice of selected derivation, primitive parameter, or
coefficient field is needed after (15).

## 6. The actual polynomial square is impossible

Use (17),(19) to expand the original-coordinate expression
\[
F_1=X_1^2Z_1-W_1^2+X_1Y_1^3-B_0X_1Y_1-C_0X_1 .
\]
The terms involving \(\rho\), \(P_0^2\), and all powers of \(t\)
cancel. The remaining linear term uses
\(\lambda P_0=-h^3+B_0h+C_0\).
This gives exactly
\[
\boxed{F_1=-\lambda^2/4 .}
\tag{20}
\]
In particular \(\lambda^2=-4F_1\) is an element of the actual
polynomial ring \(\mathscr B\).
Because \(\lambda\in L\subset\operatorname{Frac}\mathscr B\), it is
integral over \(\mathscr B\), being a root of
\(T^2+4F_1\).
The polynomial ring is integrally closed, so \(\lambda\in\mathscr B\).

But the polynomial \(-4F_1\), in the actual coordinate system
(15), has degree exactly one in \(Z_1\): its coefficient there is
\(-4X_1^2\ne0\).
The square of a nonzero polynomial in
\(\mathbb C[X_1,Y_1,W_1][Z_1]\) has even \(Z_1\)-degree.
Thus (20) is impossible.
This argument does not assume that an arbitrary nonzero element
of \(L\) is regular or a unit in the original ring. Regularity of
this particular \(\lambda\) is forced by its explicit monic equation.

## 7. Scope and verification boundary

The supplied actual cubic repeated-root chart cannot have projected
degrees \((1,3)\). The proof uses its actual cofactor and full lower
potentials, with a complete finite-field integration and explicit
inverse maps in the original polynomial ring. It does not claim that
the coefficient-field graph parameter itself is an ambient coordinate.

No further scalar-Jacobian coefficient or differential equation for
\(\lambda\) is required after (4). In particular no exploratory
assumption that \(\lambda\) is constant is used. The square obstruction
is valid uniformly for every nonzero \(\lambda\in L\).

Independent unsaved algebra checked all nine integrated jet identities,
both orders of the affine inverse, every normalized entry in (19),
and the cancellation in (20). These calculations supplement the
written proof and do not certify the imported actual-chart results.
No saved checker was executed, imported, or compiled, and no earlier
source, index, or packet was edited.
The other projected degree pairs, arbitrary-frame entry, unrestricted
cancellation, historical novelty, and human expert review remain
outside the claim.
