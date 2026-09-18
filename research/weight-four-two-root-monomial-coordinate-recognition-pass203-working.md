# Recognition of the two-root family f=cq by an original polynomial automorphism

Status: bounded working theorem, pending independent saved-source review.
For the supplied actual two-root initial kernel and nonzero-R family
\(f=cq\), the graph is impossible and the quadratic-projection branch
has an invariant coordinate in the original polynomial ring.
The published regular-kernel endpoint then recognizes the kernel.
No arbitrary coordinate-entry or unrestricted cancellation result is claimed.

## 1. Actual hypotheses and normalized input

Assume the actual chart and square alternatives of
[universal184](weight-four-universal-chart-potentials-pass184-working.md),
[reduction195](weight-four-double-cover-nonzero-r-reduction-pass195-working.md)
and [classification201](weight-four-two-root-two-gate-classification-pass201-working.md):
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=\mathcal A[u],\qquad E=\partial_u,\qquad
\deg_E(X,Y,Z,W)=(1,1,2,2),\\
\ker\theta_0=(\mathsf Z^2-\mathsf X^2\mathsf Y(\mathsf X-\mathsf Y)),
\qquad q^2=t(1-t),\qquad f=1/R=cq,\quad c\in\mathbb C^* .
\end{gathered}
\tag{1}
\]
The entire initial kernel is prescribed. These are actual polynomial
coordinates with a global slice, not a formal chart satisfying some
necessary equations.

The [actual normalization202](weight-four-two-root-monomial-actual-normalization-pass202-working.md)
has explicit polynomial inverse stages and preserves the selected
derivation, exact fields, full initial kernel and generic alternatives.
It reduces (1) to
\[
R=\frac1q,\quad k=\frac{\rho}{q},\quad
n=-\frac{\rho^2}{2q^3},\quad
\ell=-\frac{\rho^3}{2q^5}+\ell_0,\qquad \ell_0\in K .
\tag{2}
\]
Here \(L\) is the selected coefficient field,
\(K=\ker_L\partial_\rho\) is finite over \(\mathbb C(t,q)\), and its
derivative constants are \(\mathbb C\). The coefficient partials commute.
Neither field is assumed rational. Put
\[
s=1-2t,\qquad g=q\ell_0,\qquad
q_t=\frac{s}{2q},\quad q_{tt}=-\frac1{4q^3},\quad
s^2+4q^2=1 .
\tag{3}
\]
The retained actual identities include
\[
\begin{gathered}
Y=y+tX,\quad Z=z+(q_ty+k)X+qX^2,\quad
W=w+\vartheta X+\rho X^2,\\
L[y,\vartheta]=L[y,z,w]=L[v],\qquad Nv=1,\qquad
\mathbb C(y,z,w)=L(v),\\
\det\frac{\partial(Y,Z,W)}{\partial(t,\rho,v)}
=-(EX)^3\in L^* .
\end{gathered}
\tag{4}
\]
The projected entries \(y,z,w\) belong to \(\operatorname{Frac}\mathcal A\).
The nonzero-R reduction has already excluded constant \(y\).
No scalar determinant is used below as a substitute for an actual inverse.

## 2. Literal potentials and the common short form

For independent \(U,V\), form the coefficient polynomials
\[
\begin{aligned}
S&=q_{ttt}U^3/6+k_{tt}U^2/2+R_tUV+n_tU+n_\rho V,\\
T&=q_{tttt}U^4/24+k_{ttt}U^3/6+R_{tt}U^2V/2
                   +n_{tt}U^2/2+n_{t\rho}UV+n_{\rho\rho}V^2/2,\\
\mathcal H&=R(T-\ell_tU-\ell_\rho V-m)
                        +(R_tU+n_\rho)(\ell-S),\qquad m\in L.
\end{aligned}
\tag{5}
\]
Every derivative in (5) is a coefficient derivative before evaluation.
The universal identities give
\(z=q_{tt}y^2/2+k_ty+R\vartheta+n\),
\(Rw+S(y,\vartheta)=\ell\), and \(\mathcal H(y,\vartheta)=0\).

Set
\[
P(U)=\frac{U^2+4s\rho U+4\rho^2}{8q^2},\qquad
\zeta=\vartheta-P(y).
\]
Substitution of (2) into (5) and completion of the square give
\[
\mathcal H(U,V)=-\frac{(V-P(U))^2}{2q^4}
                     -\frac{g_t}{q^2}U+B_0,\qquad B_0\in L,
\qquad
z=\frac{\zeta}{q},\quad
w=g+z\,\frac{\rho+sy/2}{q}.
\tag{6}
\]
For the second-potential identity, its \(y^2,\rho y,\rho^2\)
terms cancel those in \(P/q\). In the third potential, substitution
of \(\vartheta=P(y)+qz\) gives the last equality of (6).
The residual \(U\)-coefficient of the square is
\(-R(\ell_0)_t+R_t\ell_0=-R^2g_t\); every residual term of higher
\(U\)-degree vanishes. Thus no specialization of \(\ell_0\) has been
used to obtain (6).

## 3. The graph is excluded in the original ring

In the graph alternative, \(\vartheta\in L[y]\).
Then \(\zeta\in L[y]\), and (6) makes \(\zeta^2\) a polynomial of
degree at most one in the transcendental \(y\). Hence \(\zeta\in L\)
and \(g_t=0\). Since \(g\in K\), it follows that \(g=C\in\mathbb C\).
There is no assumption here that \(\zeta\ne0\) or \(\zeta\in K\).

More generally, the short forms (6), the chart (4) and \(q^2=t(1-t)\)
give the fraction-field identity
\[
Z^2-X^2Y(X-Y)-2XW=z^2-2Xg .
\tag{7}
\]
For the graph, this is the original polynomial
\[
I_C=Z^2-X^2Y(X-Y)-2X(W-C)=z^2 .
\tag{8}
\]
The element \(z\) belongs to \(\operatorname{Frac}\mathcal A\),
hence to \(\operatorname{Frac}B\). Equation (8) makes it integral
over the normal ring \(B\), so \(z\in B\).

But \(I_C\) is irreducible in the actual polynomial four-ring.
Regard it as a polynomial in \(W\) over \(\mathbb C[X,Y,Z]\).
Its linear coefficient is \(-2X\); its constant coefficient is
\(Z^2-X^2Y(X-Y)+2CX\), relatively prime to \(X\).
It is primitive and linear over the coefficient fraction field,
so Gauss's lemma gives irreducibility. A nonconstant irreducible
polynomial cannot be a square in \(B\). The boundary \(z=0\)
would give \(I_C=0\), also impossible for independent original
coordinates. This excludes the entire normalized graph.

This step explicitly uses actual fraction-field membership and
normality. It is not an obstruction to a formal chart in which
\(z\) lies in a proper algebraic extension of the original field.

## 4. Quadratic projection and the exact scalar equation

Now take the other alternative, so \(g_t\ne0\). The eliminant (6)
expresses
\[
y=-\frac{z^2}{2g_t}+B(t,\rho),\qquad B\in L .
\tag{9}
\]
Since \(q\ne0\), (6) and (9) give
\(L[y,\vartheta]=L[z]\). By (4), \(L[z]=L[v]\), so
\(\Gamma:=Nz\in L^*\). In coefficient partials fixing \(z\),
the calibrated \(X=0\) determinant is
\[
J=\det\frac{\partial(y,z,w)}{\partial(t,\rho,z)}
=-\frac{(EX)^3}{\Gamma}\in L^* .
\tag{10}
\]
Thus it is independent of \(z\). The affine-parameter factor has
not been dropped or declared an original-ring unit.

For an independent direct computation put
\(H=(\rho+sy/2)/q\), so \(w=g+zH\).
Expanding along the middle row of the determinant gives
\[
J=g_t y_\rho-
z\left\{\frac{(y+2s\rho)y_\rho}{4q^3}+\frac{y_t}{q}\right\}.
\tag{11}
\]
Indeed \(J=g_ty_\rho+z(y_\rho H_t-y_tH_\rho)\);
using \(s_t=-2,\ q_t=s/(2q)\) and \(s^2+4q^2=1\) gives (11).

Write \(A=-1/(2g_t)\), so \(y=Az^2+B\).
The coefficients of \(z^3,z,1\) in (11) are respectively
\[
-\frac{A B_\rho}{4q^3}-\frac{A_t}{q},\qquad
-\frac{(B+2s\rho)B_\rho}{4q^3}-\frac{B_t}{q},\qquad
g_tB_\rho .
\tag{12}
\]
Scalarity and nonvanishing imply
\[
\begin{gathered}
B=a\rho+b,\quad a,b\in K,\quad
a=4q^2\frac{g_{tt}}{g_t}\ne0,\\
4q^2a_t+a^2+2sa=0,\qquad 4q^2b_t+ab=0 .
\end{gathered}
\tag{13}
\]
The cubic coefficient first gives \(B_\rho=a\in K\);
subtracting \(a\rho\) places \(b\) in \(\ker_L\partial_\rho=K\).
The constant coefficient is nonzero. Finally the linear coefficient,
compared in the transcendental \(\rho\), gives both ODEs in (13).
This does not infer \(L=K(\rho)\).

Substituting \(a\) in its equation gives the exact identity
\[
4q^2a_t+a^2+2sa
=\frac{8q^2}{g_t}\{2q^2g_{ttt}+3s g_{tt}\}.
\]
Consequently \((q^3g_{tt})_t=0\).
Since \(q_{tt}=-1/(4q^3)\), successive explicit subtractions
and the exact constant field give the complete solution
\[
g=\alpha t+\beta q+\gamma,\qquad
b=\frac{\delta}{g_t},\qquad
\alpha,\beta,\gamma,\delta\in\mathbb C,\qquad \beta\ne0 .
\tag{14}
\]
Here \(\beta\ne0\) follows from \(a\ne0\), not an extra assumption.
For \(b\), its equation in (13) is
\((b g_t)_t=0\). This reasoning holds in every allowed finite \(K\),
not only in \(\mathbb C(t,q)\).

Multiplying (9) by \(g_t\), using (13)--(14), gives
\[
H_0:=\frac{\rho+sy/2}{q}
=\frac{2\delta-z^2-2\alpha y}{2\beta},\qquad
G:=g-\gamma=\alpha t+\beta q .
\tag{15}
\]
No division by an original polynomial coordinate appears here.

## 5. Literal chart return and an original invariant coordinate

The entire original chart now becomes
\[
\begin{aligned}
Y&=y+tX,\\
Z&=z+H_0X+qX^2,\\
W&=\gamma+G+zH_0+
       \left(\frac{H_0^2+y^2}{2}+qz\right)X
       +(qH_0-sy/2)X^2 .
\end{aligned}
\tag{16}
\]
In particular \(\vartheta=(H_0^2+y^2)/2+qz\) follows by substituting
\(\rho=qH_0-sy/2\) into \(P(y)+qz\). This uses \(s^2+4q^2=1\).

Define original polynomials
\[
\begin{gathered}
I=Z^2-X^2Y(X-Y)-2X(W-\gamma),\\
J=\frac{2\delta-I-2\alpha Y}{2\beta},\\
z_* =Z-XJ,\qquad
G_* =W-\gamma-ZJ+\frac X2J^2-\frac X2Y(Y-X).
\end{gathered}
\tag{17}
\]
All their coefficients are complex and the only division is by
the nonzero complex constant \(2\beta\).
Equations (7) and (15)--(16) give
\[
I=z^2-2GX,\qquad J=H_0+qX,\qquad z_*=z,\qquad G_*=G .
\tag{18}
\]
For the last equality, first substitute \(J=H_0+qX\). The remaining
difference is
\[
\frac X2\{y^2-syX-q^2X^2-Y(Y-X)\}=0 .
\]
The middle equality for \(J\) uses the actual scalar relation (15);
it is not asserted for arbitrary independent \(H_0,y,z\).

## 6. Both polynomial inverse orders and the published endpoint

Here is a polynomial inverse, independently of any coefficient field.
For independent new entries \(X,Y,z_*,G_*\), put
\[
\begin{gathered}
J_*=\frac{2\delta-z_*^2+2XG_*-2\alpha Y}{2\beta},\\
Z=z_*+XJ_*,\qquad
W=G_*+\gamma+\frac X2Y(Y-X)+z_*J_*+\frac X2J_*^2 .
\end{gathered}
\tag{19}
\]
Both maps fix \(X,Y\). Substitution of (19) in (17) gives
\(J=J_*\), then \(z_*,G_*\) back. Conversely, substitution of (17)
in \(J_*\) gives \(J_*=J\), so (19) returns \(Z,W\).
The cancellation in \(J_*=J\) follows from
\[
-(Z-XJ)^2+2X\left(W-\gamma-ZJ+\frac X2J^2
                         -\frac X2Y(Y-X)\right)
=-Z^2+2X(W-\gamma)+X^2Y(X-Y).
\]
These are identities in the independent original polynomial ring.
Thus
\[
B=\mathbb C[X,Y,z_*,G_*] .
\tag{20}
\]

There is also an intrinsic explanation for this inverse.
The actual triangular LND
\(D_0=X\partial_Z+Z\partial_W\) fixes \(X,Y\) and satisfies \(D_0J=0\).
Therefore \(JD_0\) is locally nilpotent, and
\(\exp(-JD_0)\) sends
\(Z\) to \(Z-XJ\) and \(W\) to \(W-ZJ+XJ^2/2\).
Following it by the complex polynomial translation of the final
\(W\)-entry gives exactly (17). The explicit inverse (19) means
that no external automorphism theorem is needed.

Since \(G_*=G\in K\subset\operatorname{Frac}\mathcal A\), equation
(18) gives \(EG_*=0\). It is an ambient polynomial coordinate by
(20), not merely an algebraic coefficient parameter.
The slice makes \(\mathcal A\simeq B/(u)\) regular: \(Eu=1\)
expresses one as a combination of the original partial derivatives
of \(u\), so its zero fiber is smooth.

The precise characteristic-zero regular-kernel statement in
[Bhatwadekar--Gupta--Lokhande, Theorem3.5](https://arxiv.org/html/1501.01438v1)
now applies to the nonzero
\(\mathbb C[G_*]\)-linear LND \(E\) on the polynomial ring (20).
It yields
\[
\mathcal A=\mathbb C[G_*]^{[2]}\simeq\mathbb C^{[3]} .
\tag{21}
\]
The theorem statement and proof were freshly checked in the primary
source for this application. No condition such as
\(\alpha^2+\beta^2=0\), no rationality of \(K\), and no field-degree
argument is required to obtain this invariant coordinate.

## Scope and verification

The graph exclusion and projection recognition, together with the
actual normalization202, treat the supplied nonzero-R family \(f=cq\)
for this full two-root initial kernel. The other coefficient families
\(cq/t,cq/(t-1)\), the earlier zero-R case and arbitrary coordinate
entry are separate. No claim of actual nonvacuity for every parameter
choice in (14) is made. The unrestricted cancellation problem remains
unsolved in this program.

New inline exact arithmetic reconstructed the literal potentials,
scalar determinant, ODE substitution and both original polynomial
inverse orders. Rational coefficient collection and the relation
(15) were retained explicitly in those checks. Finite identities
do not replace the exact-field argument, normality or the published
regular-kernel theorem. No saved checker was executed, imported or
compiled; no202 or earlier artifact was edited. This is a working
restricted proof, not human expert certification, formal verification,
public submission or novelty clearance.
