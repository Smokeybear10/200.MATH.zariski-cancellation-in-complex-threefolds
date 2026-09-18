# A common actual chart for the weight-four frontier

**Status: working coefficient reduction, not cancellation recognition.**

For a supplied full height-one initial relation of weight four, the
actual fixed-\(X\) chart has four integrated coefficient identities.
They work even when the second bad leading ratio is algebraic, not
rational, over the two selected ratios. In particular, the last
identity generally contains a quadratic term in the projected \(w\).
Dropping that term would incorrectly reuse the split-cubic argument.

For the two normal forms linear in the bad variables with independent
quadratic coefficients, these identities produce an explicit plane
quintic containing the projected curve. Its selected component has
normalization the entire affine line. This does not prove that the
plane curve is smooth or that its two projected coordinates generate
that line ring.

## 1. Supplied hypotheses and exact coefficient field

Assume
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad A=\ker E,\\
(\deg_E X,\deg_E Y,\deg_E Z,\deg_E W)=(1,1,2,2),\\
a=EX,\quad b=EY,\quad e=E^2Z/2,\quad h=E^2W/2,\\
\theta_0:(\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
\longmapsto(a\tau,b\tau,e\tau^2,h\tau^2),\quad
\ker\theta_0=(F),\quad \operatorname{wt}F=4 .
\end{gathered}
\tag{1}
\]
The four original generators are actual polynomial coordinates,
\(F\) is irreducible, and its weight uses \((1,1,2,2)\).
Choose the names of the quadratic slots so that \(F_{\mathsf Z}\ne0\).
The exact-shift result157 then gives
\[
\begin{gathered}
0\ne N=[u^3](\partial_Z|_A)\in\operatorname{LND}(A),\qquad
N(a)=N(b)=N(e)=N(h)=0,\\
S=\ker_A N,\quad L=\operatorname{Frac}S,\quad A_L=L[v],\quad Nv=1,\\
t=b/a,\quad \rho=h/a^2,\quad q=e/a^2,\qquad
[L:\mathbb C(t,\rho)]<\infty .
\end{gathered}
\tag{2}
\]
Here \(t,\rho\) are algebraically independent: the contraction of
\((F)\) to the subring omitting \(\mathsf Z\) is zero. Their two
partials extend uniquely and commute on the finite separable field
\(L\), and extend to \(L[v]\) fixing \(v\).
The coefficient \(q\) is in \(L\) and obeys \(F(1,t,q,\rho)=0\).
It is not assumed to lie in \(\mathbb C(t,\rho)\).

The derivation \(N\), local slice, independence and finiteness in (2)
are the mechanisms reconstructed in
[initial-bound157](two-linear-two-quadratic-initial-bound-pass157-working.md),
Sections 2--8. In particular an occurring quadratic pivot has exact
shift three. The full initial ideal in (1), not a single vanishing
equation, supplies this conclusion.

## 2. Actual projection and the calibrated determinant

The finite Taylor projection for \(E/a\) on \(B_a\), with slice \(X\),
gives
\[
\begin{gathered}
B_a=A_a[X],\qquad A_a=\mathbb C[y,z,w]_{a_0},\qquad
a=a_0(y,z,w)\in L^*,\\
Y=y+tX,\qquad Z=z+\sigma X+qX^2,\qquad
W=w+\vartheta X+\rho X^2,\\
y,z,w,\sigma,\vartheta\in L[v],\qquad
L[y,z,w]=L[v],\qquad \mathbb C(y,z,w)=L(v).
\end{gathered}
\tag{3}
\]
For completeness, quotienting \(B_a=A_a[X]\) by \(X\) identifies
\(A_a\) with \(\mathbb C[Y,Z,W]_{a(0,Y,Z,W)}\). This proves both
the polynomial three-generator localization and algebraic
independence of the projected entries over \(\mathbb C\).
Localizing further at nonzero elements of \(S\) makes the only
denominator \(a_0=a\) a scalar in \(L^*\), proving the whole-line
equality in (3).

The actual localized polynomial map and its inverse have inverse
Jacobian units. After pullback, such a unit of \(A_a[X]\) is
independent of \(X\); at \(X=0\) its value is one. Thus the determinant
in the projected variables is one, not an assumed formal Jacobian
condition. By the chain rule,
\[
J(X)=\det
\begin{pmatrix}
X+y_t&y_\rho&y_v\\
q_tX^2+\sigma_tX+z_t&q_\rho X^2+\sigma_\rho X+z_\rho&
 \sigma_vX+z_v\\
\vartheta_tX+w_t&X^2+\vartheta_\rho X+w_\rho&
 \vartheta_vX+w_v
\end{pmatrix}
=J_0 .
\tag{4}
\]
The nonzero determinant uses rows \(Y,Z,W\), columns \(t,\rho,v\),
and holds \(X\) fixed. The cofactor for the original partial is
\[
\partial_Z(v)=-
\frac{(X+y_t)(X^2+\vartheta_\rho X+w_\rho)
-y_\rho(\vartheta_tX+w_t)}{J_0}.
\tag{5}
\]
On the other hand, \(Nv=1\), and \(X=x_0+au\), so its coefficient
of \(X^3\) is \(a^{-3}\). Comparing (5) proves
\[
J(X)=J_0=-a^3\in L^* .
\tag{6}
\]
This reconstruction is also the one used in the actual charts159
and175. No change makes \(a\) an original-ring unit.

## 3. The first two integrated identities

Use independent formal variables \(U,V\), and for \(c\in L\) define
\[
H_j(c;U,V)=
\sum_{i=0}^j\frac{c_{t^i\rho^{j-i}}}{i!(j-i)!}U^iV^{j-i}.
\tag{7}
\]
All subscripts on coefficients use the partials of (2). The
coefficient of \(X^4\) in (4) is
\(q_\rho\vartheta_v-\sigma_v+q_t y_v\).
It vanishes, so
\[
\sigma=q_t y+q_\rho\vartheta+k,\qquad k\in L .
\tag{8}
\]
Indeed the kernel of \(\partial_v\) on \(L[v]\) is \(L\).

Take total differentials over \(\mathbb C\), with \(X\) fixed.
Subtracting \(q_\rho dW+q_tX\,dY\) from the middle row gives
\[
dZ-q_\rho dW-q_tX\,dY
 =dz-q_\rho dw
 +X\{(k_t+q_{tt}y+q_{t\rho}\vartheta)\,dt
 +(k_\rho+q_{t\rho}y+q_{\rho\rho}\vartheta)\,d\rho\}.
\tag{9}
\]
The determinant is unchanged by these row operations. Its
\(X^3\) coefficient is the \(v\)-derivative of
\(-z+q_\rho w+H_2(q;y,\vartheta)+H_1(k;y,\vartheta)\).
Consequently, for some \(n\in L\),
\[
z-q_\rho w=f(y,\vartheta),\qquad
f(U,V)=H_2(q;U,V)+H_1(k;U,V)+n .
\tag{10}
\]
No projected coordinate derivative was divided out.

## 4. The two remaining polynomial potentials

Put
\[
\begin{gathered}
R=f_V(y,\vartheta),\qquad
B_1=f_t(y,\vartheta)+q_{t\rho}w,\qquad
C_1=f_\rho(y,\vartheta)+q_{\rho\rho}w,\\
g_3=H_3(q)+H_2(k)+H_1(n),\qquad
g_4=H_4(q)+H_3(k)+H_2(n),\qquad
\omega=d\vartheta+X\,d\rho .
\end{gathered}
\tag{11}
\]
The formal arguments of \(g_3,g_4\) are \(U,V\).
Differentiating (10), including the term \(w\,dq_\rho\), and
subtracting \(f_U(y,\vartheta)dY\) from (9), gives the three rows
\[
dY=dy+Xdt,\qquad
dZ_{\rm red}=R\omega+B_1dt+C_1d\rho,\qquad
dW=dw+X\omega .
\tag{12}
\]
The \(X^2\) coefficient of their wedge is
\[
dt\wedge d\rho\wedge(R\,dw+B_1\,dy+C_1\,d\vartheta).
\tag{13}
\]
Since \((g_3)_U=f_t\), \((g_3)_V=f_\rho\),
\(R_U=q_{t\rho}\), and \(R_V=q_{\rho\rho}\), its scalar coefficient
is the \(v\)-derivative of \(Rw+g_3(y,\vartheta)\). Therefore
\[
Rw+g_3(y,\vartheta)=\ell,\qquad \ell\in L .
\tag{14}
\]

To obtain the next coefficient without inverting \(R\), define
\[
\Lambda_i=\ell_i-(g_3)_i(y,\vartheta)-R_iw,\qquad i=t,\rho .
\tag{15}
\]
Here \(R_i\) differentiates coefficients of the formal polynomial
\(f_V\), then evaluates at \(y,\vartheta\); it is not the total
derivative of that evaluated polynomial. Differentiation of (14)
gives exactly
\[
R\,dw=-B_1dy-C_1d\vartheta+\Lambda_tdt+\Lambda_\rho d\rho.
\tag{16}
\]
The \(X\) wedge coefficient of (12), after this substitution only
in the terms containing \(R\,dw\), is
\[
dt\wedge d\rho\wedge
(-\Lambda_tdy-\Lambda_\rho d\vartheta+C_1dw).
\tag{17}
\]
The formal derivative identities
\((f_\rho)_U=(f_V)_t\), \((f_\rho)_V=(f_V)_\rho\),
\((g_4)_U=(g_3)_t\), and \((g_4)_V=(g_3)_\rho\)
show that its scalar is the \(v\)-derivative of
\[
\frac{q_{\rho\rho}}2w^2+f_\rho(y,\vartheta)w
 +g_4(y,\vartheta)-\ell_t y-\ell_\rho\vartheta .
\]
Thus there is \(m\in L\) with
\[
\boxed{\frac{q_{\rho\rho}}2w^2+f_\rho(y,\vartheta)w
 +g_4(y,\vartheta)-\ell_t y-\ell_\rho\vartheta=m.}
\tag{18}
\]
The term \(q_{\rho\rho}w^2/2\) is essential in general.
The remaining coefficient is the simultaneous nonzero condition
\[
\left[dy\wedge(R\,d\vartheta+B_1dt+C_1d\rho)\wedge dw
\right]_{dt\wedge d\rho\wedge dv}=-a^3 .
\tag{19}
\]
Equations (14) and (18) are polynomial equations in the three
projected entries of total degrees at most three and four. They
are not asserted to generate their full evaluation ideal.

## 5. A denominator exclusion for two bad-linear normal forms

Suppose more specifically
\[
q=-r(t)\rho+s(t),\qquad r,s\in\mathbb C(t),\qquad r'(t)\ne0.
\tag{20}
\]
Then \(q_{\rho\rho}=0\) and
\(R=k_\rho-r'(t)y\). Under the actual hypotheses above,
\[
R\ne0\quad\hbox{in }L[v].
\tag{21}
\]
Here is the full exclusion. If \(R=0\), then \(y\in L\).
If also \(y_\rho=0\), the first row of (4) would be
\((X+y_t,0,0)\), making the nonzero constant determinant divisible
by the monic positive-degree polynomial \(X+y_t\). Hence
\(y_\rho\ne0\).

Since \(q_{\rho\rho}=0\), \(f\) is linear in \(V\), with coefficient
\(R\). Equation (10) in the branch \(R=0\) is
\(z=-r(t)w+A_0\) for \(A_0\in L\).
The whole-line equality (3) gives \(L[w]=L[v]\), so \(w\) is
nonconstant. At \(X=0\), add \(r(t)\) times the last row to the
middle row. The determinant becomes
\[
J(0)=w_v\{y_t(A_0)_\rho-y_\rho(A_0)_t
             +r'(t)y_\rho w\}.
\tag{22}
\]
For \(\deg_vw=d\ge1\) and leading coefficient \(c\ne0\), its leading
term has degree \(2d-1\) and coefficient
\(d\,r'(t)y_\rho c^2\ne0\).
This contradicts (6), proving (21).
The argument does not show that \(R\) has no zeros.

## 6. The selected curve lies on an explicit quintic

The two forms in this section are supplied literally as full initial
kernels, not inferred from a single relation:
\[
F_{\rm a}=X^2Z+Y^2W,\qquad
F_{\rm b}=X^2Z+XYW-Y^4 .
\tag{23}
\]
They give respectively \(q=-t^2\rho\) and \(q=-t\rho+t^4\).
Thus (20)--(21) apply. Define the formal polynomial
\[
\mathcal H(U,V)=f_V(U,V)
       \{g_4(U,V)-\ell_tU-\ell_\rho V-m\}
       +f_\rho(U,V)\{\ell-g_3(U,V)\}.
\tag{24}
\]
Eliminating \(w\) from (14) and (18), without dividing in the
line ring, gives \(\mathcal H(y,\vartheta)=0\).

For \(F_{\rm a}\) its component polynomials are
\[
\begin{aligned}
f&=-\rho U^2-2tUV+H_1(k)+n,&
f_V&=k_\rho-2tU,\\
g_3&=-U^2V+H_2(k)+H_1(n),&
f_\rho&=-U^2+H_1(k_\rho)+n_\rho,\\
g_4&=H_3(k)+H_2(n).
\end{aligned}
\tag{25}
\]
It follows that \(\deg\mathcal H=5\), with top total-degree part
\(-U^4V\): only the product of the quadratic leading part of
\(f_\rho\) and the cubic part of \(-g_3\) contributes degree five.
For \(F_{\rm b}\),
\[
\begin{aligned}
f&=6t^2U^2-UV+H_1(k)+n,&
f_V&=k_\rho-U,\\
g_3&=4tU^3+H_2(k)+H_1(n),&
f_\rho&=H_1(k_\rho)+n_\rho,\\
g_4&=U^4+H_3(k)+H_2(n).
\end{aligned}
\tag{26}
\]
Here \(\deg\mathcal H=5\), with top part \(-U^5\).
In particular neither displayed eliminant is zero.

Equation (10) and (3) imply \(L[y,\vartheta,w]=L[v]\). Since \(R\ne0\),
(14) also implies
\[
L(y,\vartheta)=L(v),\qquad
C:=L[y,\vartheta]\subset L[v]
\text{ is finite and birational, with normalization }L[v].
\tag{27}
\]
To check finiteness explicitly, \(y,\vartheta\) cannot both be in \(L\),
since (14) would then make \(w\in L\).
Choose a nonconstant one, \(p(v)\). The equation
\(p(T)-p(v)=0\), divided by its nonzero leading coefficient in \(L\),
makes \(v\) integral over \(L[p(v)]\), hence over \(C\).
Thus \(L[v]=C[v]\) is finite over \(C\). The equality of fraction
fields follows from (14) and (10). The integrally closed ring \(L[v]\)
is therefore precisely the integral closure of \(C\) in that field.

The prime kernel of \(L[U,V]\longrightarrow L[v]\),
\((U,V)\mapsto(y,\vartheta)\), has height one. Its irreducible
generator \(G\) divides \(\mathcal H\), so
\[
1\le\deg G\le5 .
\tag{28}
\]
This is a necessary, finite-degree projected-curve problem.
Neither \(G=\mathcal H\), a unit evaluated cofactor, nor
\(L[y,\vartheta]=L[v]\) follows from the argument above.

## 7. Scope and the next proof gap

This note is an actual-chart reduction for a supplied exact1122 frame.
It gives no procedure placing an arbitrary sliced action into that
frame. It does not settle either quartic form in (23), the other
quartic forms, height-two initial kernels, or unrestricted cancellation.

The next question in (23) is whether the actual determinant and field
return exclude singular projected quintic components or permit an
explicit invariant ambient coordinate. A generic rational component
or its normalization is not such a coordinate.

The general chart specializes to the previously written cusp chart
\(q=t^3\) and split chart \(q=-t\rho\); their recognition theorems
are not inputs here. This note was written after full rereads of157,
[chart159](cusp-generic-chart-first-reductions-pass159-working.md),
[chart175](split-cubic-generic-chart-pass175-working.md), and
[zero-R175](split-zero-R-exclusion-pass175-working.md).
The projection, calibration and the denominator argument were
reconstructed above with the new \(q\).

Written derivation and any accompanying finite symbolic controls are
not human expert review or proof-assistant certification. No historical
novelty clearance, unrestricted solution, external contact or submission
is asserted. All183 and earlier frozen artifacts are unchanged.
