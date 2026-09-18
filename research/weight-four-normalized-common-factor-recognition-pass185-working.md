# Recognition of a normalized common-factor weight-four branch

**Status: complete written conditional proof, pending independent saved-source review.**

A supplied full weight-four initial kernel
\(X^2Z+XYW-Y^4\), with the additional actual-chart normalization
specified below, has an explicit invariant ambient coordinate.
The determinant forces the remaining potential coefficient to be
\(\rho\)-constant. Its integral return is then a polynomial whose
companion gives an inverse over the original ring.

This does not prove that every frame with that initial kernel admits
the normalization, or that its projected coordinate is affine.
Those are hypotheses, not conclusions of this note.

## 1. Actual hypotheses and retained chart

Assume
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\qquad Eu=1,\\
(\deg_E X,\deg_E Y,\deg_E Z,\deg_E W)=(1,1,2,2),\\
a=EX,\quad b=EY,\quad e=E^2Z/2,\quad h=E^2W/2,\\
\theta_0:(\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
 \longmapsto(a\tau,b\tau,e\tau^2,h\tau^2),\\
\ker\theta_0=(\mathsf X^2\mathsf Z+\mathsf X\mathsf Y\mathsf W-\mathsf Y^4).
\end{gathered}
\tag{1}
\]
The generators \(X,Y,Z,W\) are actual polynomial coordinates.
The weight of the full initial generator is four, for weights
\((1,1,2,2)\). In particular \(a\ne0\).

Use the selected derivation and exact coefficient field of
[the universal actual chart184](weight-four-universal-chart-potentials-pass184-working.md):
\[
\begin{gathered}
N=[u^3](\partial_Z|_A)\ne0,\qquad
S=\ker_A N,\qquad L=\operatorname{Frac}S,\qquad A_L=L[v],\qquad Nv=1,\\
t=b/a,\qquad \rho=h/a^2,\qquad q=e/a^2=-t\rho+t^4,\qquad
[L:\mathbb C(t,\rho)]<\infty,\\
K=\ker_L\partial_\rho,\qquad [K:\mathbb C(t)]<\infty.
\end{gathered}
\tag{2}
\]
Here \(t,\rho\) are algebraically independent. The two coefficient
partials extend uniquely and commute on \(L\); their joint constants
are exactly \(\mathbb C\). For clarity, this last assertion follows
by differentiating the monic minimal polynomial of a joint constant
over \(\mathbb C(t,\rho)\): minimality makes all its coefficients
joint constants, hence complex; algebraic closedness of \(\mathbb C\)
then gives the assertion. No rationality assumption on \(K\) is made.

The actual Taylor chart and its calibration are
\[
\begin{gathered}
B_a=A_a[X],\qquad
Y=y+tX,\quad Z=z+\sigma X+(-t\rho+t^4)X^2,\quad
W=w+\vartheta X+\rho X^2,\\
y,z,w,\sigma,\vartheta\in L[v],\qquad
L[y,z,w]=L[v],\qquad \mathbb C(y,z,w)=L(v),\\
\det\frac{\partial(Y,Z,W)}{\partial(t,\rho,v)}\Big|_{X\ {\rm fixed}}
 =-a^3\in L^* .
\end{gathered}
\tag{3}
\]
The chart184 derives these from the original coordinate map and the
selected \(N\), not from a formal Jacobian assumption.

The **additional assumptions of this lemma** are
\[
\begin{gathered}
y=\gamma v+\eta,\qquad \gamma=Ny\in L^*,\quad \eta\in L,\\
k_\rho=0,\qquad n=d\rho+n_0,\qquad
d\in\mathbb C^*,\qquad k,n_0,\ell\in K .
\end{gathered}
\tag{4}
\]
The coefficients \(k,n,\ell\) are the integrated coefficients of
chart184. Neither \(a\) nor \(\gamma\) is assumed a complex constant
or a unit of the original ring. In particular (4) is not an
authorization to replace the actual frame by a coefficient-field
coordinate change.

Because \(y\) is affine in \(v\), \(L[y]=L[v]\), so
\(\vartheta,w,z\) can be read as polynomials in \(y\) over \(L\).
No pure eliminant or specified degree for that graph is assumed.

## 2. The exact normalized potentials

In the universal chart the polynomial
\(f=H_2(q)+H_1(k)+n\), where \(H_j\) is the factorial-normalized
degree-\(j\) coefficient Taylor form, becomes
\[
f(U,V)=6t^2U^2-UV+k'U+d\rho+n_0 .
\]
The formulas for \(\sigma\), \(z-q_\rho w\), and the next two
integrated potentials therefore read
\[
\begin{aligned}
\sigma&=(-\rho+4t^3)y-t\vartheta+k,\\
z&=-tw+6t^2y^2+k'y-y\vartheta+d\rho+n_0,\\
-yw+4ty^3+\frac{k''}{2}y^2+n_0'y+d\vartheta&=\ell,\\
dw+y^4+\frac{k'''}6y^3+\frac{n_0''}2y^2-\ell'y&=m,\qquad m\in L.
\end{aligned}
\tag{5}
\]
Primes denote the coefficient partial \(\partial_t\), not a
derivative along \(y\). In this case \(q_{\rho\rho}=0\), so the
quadratic-in-\(w\) term of the general fourth potential is absent.
It has not been omitted for arbitrary algebraic \(q\).

Solving (5) divides only by the nonzero complex constant \(d\):
\[
\begin{aligned}
w&=\frac{m-y^4-k'''y^3/6-n_0''y^2/2+\ell'y}{d},\\
\vartheta&=\frac{yw-4ty^3-k''y^2/2-n_0'y+\ell}{d}.
\end{aligned}
\tag{6}
\]
All calculations that follow use these literal polynomial identities.
In particular no division by the projected polynomial \(y\) occurs.

## 3. The determinant forces \(m_\rho=0\)

Replace the generic parameter \(v\) by \(y\), retaining the
Jacobian factor \(\gamma\) of (4). At \(X=0\), equation (3) gives
\[
J_y:=\det\frac{\partial(y,z,w)}{\partial(t,\rho,y)}
 =z_t w_\rho-z_\rho w_t
 =-\frac{a^3}{\gamma}\in L^* .
\tag{7}
\]
All derivatives in this section keep \(y\) fixed. Although \(a\)
and \(\gamma\) can depend on the coefficient field, the right-hand
side has no \(y\)-dependence.

Put \(c=t+y^2/d\). Differentiating (5)--(6) gives
\[
\begin{aligned}
w_\rho&=\frac{m_\rho}{d},&
z_\rho&=d-cw_\rho,\\
w_t&=\frac{m_t-k''''y^3/6-n_0'''y^2/2+\ell''y}{d},\\
z_t+cw_t
 &=\frac{5y^4}{d}+\frac{2k'''}{3d}y^3
   +\left(12t+\frac{3n_0''}{2d}\right)y^2\\
 &\hspace{1.4em}
   +\left(k''-\frac{2\ell'}d\right)y+n_0'-\frac md,\\
J_y&=w_\rho(z_t+cw_t)-dw_t .
\end{aligned}
\tag{8}
\]
For example \(\vartheta_\rho=yw_\rho/d\) in the second formula.
For the fourth formula, differentiation of \(z\) first yields
\(-w+4y^4/d+k'''y^3/(2d)+(12t+n_0''/d)y^2+
(k''-\ell'/d)y+n_0'\); substitution of \(w\) from (6) gives
the displayed expression.

The \(y^4\) coefficient of \(J_y\) is \(5m_\rho/d^2\).
By (7) it must vanish. Thus \(m\in K\). Now (8) reduces to
\(J_y=-dw_t\), and its three remaining positive-degree coefficients
give
\[
m_\rho=0,\qquad k''''=0,\qquad n_0'''=0,\qquad \ell''=0,
\qquad J_y=-m_t=-\frac{a^3}{\gamma}\ne0 .
\tag{9}
\]
This is an exact coefficient comparison in the polynomial ring
\(L[y]\). It does not replace the determinant by a cube or assume
\(Ny=1\).

The joint constant field now gives complex constants with
\[
\begin{aligned}
k&=k_3t^3+k_2t^2+k_1t+k_0,\\
n_0&=n_2t^2+n_1t+n_{00},\qquad
\ell=\ell_1t+\ell_0 .
\end{aligned}
\tag{10}
\]
For example \(k'''\) is killed by both coefficient partials,
so it equals \(6k_3\) with \(k_3\in\mathbb C\). Subtracting
\(k_3t^3\) and repeating proves all of the first formula.
The other two follow by the same finite polynomial subtractions.
There is no integration of an arbitrary algebraic function.
Equation (9) imposes no assertion that \(m\) itself is polynomial
in \(t\).

## 4. Returning \(m\) to an original polynomial invariant

Define polynomials with the complex coefficients of (10):
\[
\begin{aligned}
F_{\rm b}&=X^2Z+XYW-Y^4,\\
K_3(X,Y)&=k_3Y^3+k_2XY^2+k_1X^2Y+k_0X^3,\\
N_2(X,Y)&=n_2Y^2+n_1XY+n_{00}X^2,\\
Q(X,Y)&=K_3(X,Y)+N_2(X,Y)-\ell_1Y-\ell_0X,\\
I&=dW-F_{\rm b}+Q(X,Y).
\end{aligned}
\tag{11}
\]
The subscripts indicate homogeneous degrees; their coefficients
may be zero. The displayed \(F_{\rm b}\) is the actual polynomial
in the frame, not an assumption that the initial relation is itself
\(E\)-invariant.

Substitution of the full chart (3),(5) gives the exact expansion
\[
\begin{aligned}
F_{\rm b}
 &=-y^4+(yw-4ty^3)X+(k'y+d\rho+n_0)X^2+kX^3,\\
K_3(X,y+tX)&=kX^3+k'yX^2+\frac{k''}{2}y^2X+\frac{k'''}6y^3,\\
N_2(X,y+tX)&=n_0X^2+n_0'yX+\frac{n_0''}2y^2 .
\end{aligned}
\tag{12}
\]
For the first line, the \(X^4\) coefficient is
\((-t\rho+t^4)+t\rho-t^4=0\).
The \(X^3\) coefficient is
\(\sigma+t\vartheta+\rho y-4t^3y=k\).
The \(X^2\) coefficient follows from the displayed \(z\) in (5).
Thus no leading-order approximation is involved.

Combining (11)--(12) with the first potential in (5) cancels
every positive power of \(X\):
\[
\begin{aligned}
I
 &=dw+y^4+\frac{k'''}6y^3+\frac{n_0''}2y^2-\ell_1y\\
 &\quad
 +X\left(d\vartheta-yw+4ty^3+\frac{k''}{2}y^2+n_0'y
                -\ell_1t-\ell_0\right)\\
 &=dw+y^4+\frac{k'''}6y^3+\frac{n_0''}2y^2-\ell'y\\
 &=m .
\end{aligned}
\tag{13}
\]
Here the \(X\) coefficient is \(\ell-\ell_1t-\ell_0=0\).
The equality holds in the actual chart localization.
Since \(E\) kills \(L\), (13) implies \(EI=0\) there.
The original domain \(B\) embeds in that localization, so
\(EI=0\) in \(B\). In particular this proves integral return
of this specific \(m\), rather than importing an arbitrary
generic coordinate into the original ring.

## 5. An explicit companion and both polynomial inverse orders

Put \(P(X,Y)=Y^4+Q(X,Y)\), and define
\[
\begin{gathered}
I-P=-X^2Z+(d-XY)W,\qquad
J=(d+XY)Z+Y^2W,\\
\begin{pmatrix}I-P\\J\end{pmatrix}
 =
\begin{pmatrix}-X^2&d-XY\\d+XY&Y^2\end{pmatrix}
\begin{pmatrix}Z\\W\end{pmatrix},
\qquad \det=-d^2\in\mathbb C^* .
\end{gathered}
\tag{14}
\]
For independent target variables \(x,y_1,i,j\), put
\(U_0=i-P(x,y_1)\). The candidate inverse is
\[
X=x,\qquad Y=y_1,\qquad
Z=\frac{(d-xy_1)j-y_1^2U_0}{d^2},\qquad
W=\frac{(d+xy_1)U_0+x^2j}{d^2}.
\tag{15}
\]
These are original polynomial formulas because \(d\in\mathbb C^*\).

Substituting (14) into (15) recovers the old coordinates by
\[
(d-XY)J-Y^2(I-P)=d^2Z,\qquad
(d+XY)(I-P)+X^2J=d^2W .
\tag{16}
\]
For the other order, substitute (15) into the first row of (14).
The coefficient of \(j\) is zero, and that of \(U_0\) is
\(\{x^2y_1^2+(d-xy_1)(d+xy_1)\}/d^2=1\).
The second row has coefficient zero on \(U_0\) and one on \(j\).
Adding \(P(x,y_1)\) recovers \(i\), while \(X,Y\) recover
\(x,y_1\). Consequently
\[
B=\mathbb C[X,Y,I,J],\qquad I\in A .
\tag{17}
\]
No assertion that \(J\) is invariant is needed.

## 6. Exact recognition endpoint

The slice gives \(A\simeq B/(u)\). In the original coordinates,
\(Eu=1\) expresses one as a polynomial linear combination of the
four partial derivatives of \(u\). Thus the hypersurface \(u=0\)
is smooth over \(\mathbb C\), and \(A\) is a regular ring.

Bhatwadekar, Gupta and Lokhande
[Theorem 3.5](https://arxiv.org/html/1501.01438v1)
applies to a nonzero \(k[T]\)-linear LND of
\(k[T,X_1,X_2,X_3]\) in characteristic zero whose kernel is regular.
Its conclusion is that the kernel equals \(k[T]^{[2]}\).
Apply it with \(k=\mathbb C\), \(T=I\), and the actual coordinates
in (17). The original \(E\) is nonzero because \(Eu=1\), and
\(EI=0\) makes it \(\mathbb C[I]\)-linear. Therefore
\[
A=\mathbb C[I]^{[2]}\simeq\mathbb C^{[3]}.
\tag{18}
\]
The exact statement and its displayed short proof were freshly read
in the primary paper. Its prerequisite theorems have not been
recursively re-proved here.

## Scope and dependencies

The conclusion is conditional on the full initial kernel (1),
the actual chart supplied by184, affine \(y\), and every
normalization condition in (4), particularly the complex unit \(d\).
This note does not show that arbitrary frames with \(F_{\rm b}\)
reach those conditions. It neither recognizes
\(X^2Z+Y^2W\), the other weight-four normal forms, height-two initial
kernels, nor unrestricted cancellation or arbitrary coordinate entry.

The direct inverse has the same constant-determinant structure as
[the earlier split coordinate construction179](split-rho-constant-potential-coordinate-pass179-working.md).
It has been reconstructed here with the new \(Y^4\) contribution
and does not use that note's split initial-kernel hypothesis.
The intrinsic coefficient-field and calibration inputs are retained
from the universal chart184; no whole-plane completion theorem or
pure-eliminant statement is needed in addition to affine \(y\).

No checker has been written, executed, imported or compiled for
this lemma. No frozen183 or earlier source, packet or index is
changed. The argument is an AI-authored working proof, not a
human-expert or proof-assistant certification, a novelty clearance,
or a claim that the unrestricted goal is complete.

