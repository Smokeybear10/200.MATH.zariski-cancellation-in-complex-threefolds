# The zero quadratic coefficient is excluded at the degree drop

Working bounded result, subject to separate saved-source review: retain
the FULL actual264 chart, the genuine296 potentials, and universal494.
Suppose sigma is affine and nonconstant, theta is quadratic, and

    m=k_s is not complex, m_s=0, theta=−P^2/m+bP+c, P=sigma.

Then the quadratic coefficient e of y cannot be zero. This is an
exclusion inside the supplied actual chart, not a general cancellation
theorem. No rational coefficient-field assumption is used.

The entry reduction is the separately reviewed
[reciprocal-coupling argument513](principal-paraboloid-degree-drop-affine-intercept-reciprocal-rigidity-pass513-working.md).
Its explicit complex polynomial normalization gives

\[
m=1/t,\quad k=s/t+f(t),\quad y=r,\quad
\theta=-tP^2+bP+c,\quad n=n_1(t)s+n_0(t).
\tag{1}
\]

Every original actual hypothesis survives that normalization. In
particular the original global slice, entire initial kernel, literal
selected partial, both actual returns, and scalar calibration survive.
No claim here is based on normalizing a field-valued coefficient by
an ambient polynomial map.

## 1. Exact normalized input and transverse parameter

Keep the notation and full hypotheses of
[264](principal-one-affine-paraboloid-chart-pass264-working.md) and
[512](principal-paraboloid-degree-drop-univariate-coupling-reduction-pass512-working.md):

\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,
\quad X=a_0u+x_0,\quad a_0\ne0,\\
N=[u^4]\partial_Z|_A\ne0,\quad
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,\\
Na_0=Nt=Ns=0,\quad L[P]=O,\quad NP=\rho\in L^*.
\end{gathered}
\tag{2}
\]

The full initial kernel remains X^2Z−Y^2 with time profile (1,2,2,2).
Write F_0=ker(partial_s) inside L. It is finite over C(t), and the
constants of its exact t derivative are C.

Set z=epsilon=k_t+mb. The top multiplier identity512 gives

\[
z_s=\frac{3\kappa}{2t^3}\ne0,\qquad
b=tz+s/t-tf',\qquad \kappa\in L^*.
\tag{3}
\]

Consequently (t,z) is an exact separating basis, with s an existing
element of its finite coefficient-field extension. Below, t derivatives
hold z fixed and z derivatives hold t fixed. Subscripts s denote the
original transverse derivative. The two new partials commute and have
joint constants C. Derivatives of elements of F_0 are unchanged.
In particular z is transcendental over F_0.

For (1), the full evaluated H_V has linear coefficient
g_1=n_1'+2n_1/t. The P coefficient of the multiplier equation
A=kappa*g_H is −2t*r_s=kappa*g_1. Together with (3) this gives

\[
d=\frac{(t^2n_1)'}3\in F_0,\qquad
r=-dz+r_0,\qquad r_0\in F_0.
\tag{4}
\]

All integrations in this note mean differentiation of existing
differences, followed by the stated constant-field property. They
do not assume that an arbitrary rational function has a primitive.

The entire literal rows are

\[
\begin{aligned}
Y&=XP-dz+r_0+tX^2,\\
Z&=(2tX+z)P+2tr+c/t+n_1s+n_0+kX+t^2X^2,\\
W&=t\{\ell-(2P+k_t)r-F(P,\theta)\}+\theta X+sX^2,\\
F(P,V)&=(2s/t^3+f'')P^2/2-PV/t^2
             +(n_1's+n_0')P+n_1V,\\
k_t&=-s/t^2+f',\qquad \theta=-tP^2+bP+c.
\end{aligned}
\tag{5}
\]

Here c,ell and s remain arbitrary existing coefficient-field
elements before the necessary equations are imposed. The scalar is

\[
\det\frac{\partial(Y,Z,W)}{\partial(t,z,P)}
 =-\frac{a_0^4s_z}{\rho}\in L^*.
\tag{6}
\]

It can depend on t,z. Only independence of X,P is used below.

## 2. The actual field two-quasi theorem gives one invariant

Extend N from A to A[u] by Nu=0. The actual polynomial derivation

\[
\Delta=a_0N-(NX)E
\tag{7}
\]

fixes X, kills L and equals g_0*partial_P on the injective overring
L[X,P], where g_0=a_0*rho is a nonzero coefficient constant for P.
Thus Delta is locally nilpotent on the original polynomial ring,
not merely a formal derivation on a parametrized curve. Over
K=\mathbb C(X), it acts on the actual three-ring K[Y,Z,W].
By (5), its coordinate degrees are exactly (1,1,3), since

\[
Y_1=X,\qquad Z_1=2tX+z,\qquad W_3=-1.
\tag{8}
\]

Take a gcd g of its three polynomial coefficients. Since g divides
Delta(g), additivity of Delta-degree shows Delta(g)=0: otherwise
the derivative would have degree deg_Delta(g)−1 but its multiple
of g would have degree at least deg_Delta(g). Therefore Delta/g
is a nonzero irreducible LND with the same kernel, and its second
iterates on Y,Z vanish.

The primary [Dasgupta--Gupta, Theorem4.1](https://arxiv.org/html/1701.03635v1)
gives two alternatives over this field. An invariant nonzero
K-linear form in Y,Z is impossible, because their velocity ratio
is 2t+z/X, which is transcendental over K. The other alternative
provides an invariant I with K[Y,Z,W]=K[Y,Z,I]. Comparing degrees
in W for this polynomial map and its inverse over K[Y,Z] shows
that I is a nonzero K-multiple of W plus a polynomial in Y,Z.
Rescale I and subtract its constant in K to obtain

\[
I=W+\Phi(Y,Z),\quad \Phi\in K[Y,Z],\quad \Phi(0,0)=0,
\qquad I_P=0.
\tag{9}
\]

This I is a generic-field coordinate only. It is never promoted
to a coordinate of the original ring over C[X]. Both alternatives
of the theorem have been addressed.

For a nonzero homogeneous form of degree h in Y,Z, substitution of
the two leading coefficients in (8) is nonzero: after dividing by
X^h it is a nonzero polynomial in the transcendental 2t+z/X.
Thus deg(Phi) cannot exceed three. Its homogeneous cubic part must
cancel W_3, so it is exactly Y^3/X^3. Write

\[
I=W+Y^3/X^3+A_2Y^2+B_2YZ+C_2Z^2+aY+b_1Z,
\quad A_2,B_2,C_2,a,b_1\in K.
\tag{10}
\]

## 3. The quadratic P coefficient forces exact complex constants

The full coefficient of P^2 in W is

\[
W_2=z-f'-tf''/2+t^2n_1-tX.
\tag{11}
\]

Consequently the P^2 equation for (10) is

\[
0=W_2+3(-dz+r_0+tX^2)/X
      +A_2X^2+B_2X(2tX+z)+C_2(2tX+z)^2.
\tag{12}
\]

Comparison in the transcendental z first gives C_2=0 and
B_2=−1/X+3d/X^2. Since B_2 lies in C(X), differentiation in t
gives d'=0. Thus d=D belongs to C, including zero for now.
The remaining part of (12) is

\[
C(t)+3r_0/X+A_2X^2=0,\qquad
C(t)=-f'-tf''/2+t^2n_1+6Dt.
\tag{13}
\]

Differentiating and comparing powers of X gives C'=r_0'=0.
Write their complex values C and R. Exact integration of (4),(13)
then gives complex constants N,F_c,F_c^0 such that

\[
\begin{aligned}
r&=-Dz+R,\qquad n_1=(3Dt+N)/t^2,\\
f&=3Dt^2+(N-C)t-F_c/t+F_c^0,\\
A_2&=-C/X^2-3R/X^3,\qquad B_2=-1/X+3D/X^2.
\end{aligned}
\tag{14}
\]

For example (13) says f'+tf''/2=9Dt+N−C. Integrating
(t^2f')'=18Dt^2+2(N−C)t first, then f', gives precisely (14).

The case D=0 is already impossible in the actual ring. It gives
Y−R=X(P+tX) in B localized at a_0. But a_0 does not belong to
the prime ideal (X): deg_E(a_0)=0 whereas deg_E(X)=1, and
E-degree is additive on nonzero products. Contraction therefore
gives Y−R in (X) in C[X,Y,Z,W], which contradicts its actual
coordinate independence. Hence from now on

\[
D\in\mathbb C^*.
\tag{15}
\]

## 4. The full linear P equation, with all lower terms

Put V_0=c/t+n_1s+n_0. Before adding aY+b_1Z in (10), its
complete linear P coefficient, after (14), is

\[
-(F_c^0+2Nt)X+G_0-Nz+G_{-1}/X+(3DRz-3R^2)/X^2,
\tag{16}
\]

where

\[
\begin{aligned}
G_0={}&-6CDt-CN+27D^2t^2+3DF_c^0+12DNt
                 +F_cN/t^2+N^2-6Rt-tn_0'-n_0,\\
G_{-1}={}&Dz^2+(2CD-12D^2t-R)z+3DV_0+12DRt-2CR.
\end{aligned}
\tag{17}
\]

The complete P equation adds aX+b_1(2tX+z) to (16).
Differentiate it in z. Because b_1 belongs to C(X), it forces
(G_{-1})_z=H in C: differentiating this coefficient in either
exact coefficient direction gives zero by comparison of X powers.
Thus G_{-1}=Hz+B(t), with B in F_0. The remaining equation and
the fact that a belongs to C(X) then force complex A_0,B_0 with

\[
\begin{aligned}
G_0&=2Ht+A_0,\quad G_{-1}=Hz+6DRt+B_0,\\
a&=F_c^0-A_0/X-B_0/X^2+3R^2/X^3,\\
b_1&=N-H/X-3DR/X^2.
\end{aligned}
\tag{18}
\]

The first equality integrates the existing n_0. The second solves
for the existing V_0. With one further complex constant K_0,

\[
\begin{aligned}
n_0={}&9D^2t^2+(-3CD+6DN-3R-H)t-CN+3DF_c^0+N^2-A_0\\
&\hspace{12mm}-F_cN/t^2+K_0/t,\\
V_0={}&-z^2/3+(4Dt+L_0)z-2Rt+K_1,\\
L_0&=(H-2CD+R)/(3D),\qquad K_1=(B_0+2CR)/(3D).
\end{aligned}
\tag{19}
\]

Only the already justified nonzero D is divided here. Every other
complex constant in (14),(18),(19) may vanish. The quantities s
and ell, and all of their derivatives, remain unrestricted at this
stage. Equation (19) expresses c=t(V_0−n_1s−n_0); it does not
discard that coefficient.

## 5. Four Laurent coefficients give a contradiction

Use the entire rows (5), with (14),(18),(19), in (10). Its positive
P coefficients cancel identically. Its P-constant value has a finite
Laurent expansion in the independent actual variable X:

\[
I=\sum_{j=-3}^{2} h_j(t,z)X^j.
\tag{20}
\]

The arbitrary K-constant in I was removed in (9), so it contributes
no additional rational X term. Direct expansion, retaining the
whole lower data s and ell in h_0,h_{-1}, gives

\[
\begin{aligned}
h_2&=F_c,\qquad h_1=-3DF_c+F_c^0N-K_0,\\
h_{-3}&=-D^3z^3+R^3,\\
h_{-2}&=-B_0R+CD^2z^2-CR^2-6D^3tz^2
                     +D^2z^3-DHz^2-DRz^2.
\end{aligned}
\tag{21}
\]

In particular h_1 and h_2 are complex constants. No assertion
about the derivatives of the unknown scalar (6) is being made.

Since I=W+Phi(Y,Z), replacing the W row by I preserves the full
Jacobian at fixed X. The P coefficient of that Jacobian is exactly
X(2X*I_z−I_t), using the two linear leaders in (8). Its vanishing
in (6) proves the exact identity

\[
I_t=2XI_z.
\tag{22}
\]

Compare three coefficients in the finite Laurent identity (22):

\[
(h_1)_t=2(h_0)_z,\qquad
(h_0)_t=2(h_{-1})_z,\qquad
(h_{-1})_t=2(h_{-2})_z.
\tag{23}
\]

The first equality and (21) give (h_0)_z=0. Differentiating the
second equality in z gives (h_{-1})_{zz}=0. Differentiate the
third equality twice in z, commuting the exact coefficient
partials. Its left side is zero, but (21) gives

\[
0=2(h_{-2})_{zzz}=12D^2\ne0.
\tag{24}
\]

This contradiction excludes D nonzero, and Section3 excluded D=0.
Thus e=0 is impossible under the full retained degree-drop chart
hypotheses.

## 6. Verification boundary

Fresh unsaved root8b9648 reconstructed (11),(12) from the complete
literal W and checked the generic quadratic cancellation. Fresh
b81ce4 extracted the complete linear coefficient (16),(17).
Fresh f66b4c substituted all of (14),(18),(19) into the original
Y,Z,W, checked every positive P coefficient of I, and produced the
full Laurent expansion, including (21). Fresh609e6e checked a
longer compatibility route; the proof above uses only the shorter
exact three-coefficient implication (23),(24).

Separate fresh reconstruction53ec02 independently rebuilds the full
literal W, the raw linear coefficient, every positive-P cancellation
and all four Laurent coefficients (21). Fresh0fde98 checks the raw
multiplier entry (3),(4), both integrations in (19), and the complete
scalar P coefficient used in (22). Both were reported clean, including
the D=0 contraction and the nonzero-D contradiction. That independent
reconstruction is distinct from the subsequent saved-source review.

These calculations do not replace the actual-ring, generic-field
theorem, exact-field or contraction arguments written above. A
separate reconstruction and full saved-source review are required
before canonical acceptance. All saved checkers remain frozen.
No earlier source, public claim, submission or external contact
is authorized or made by this note. The e nonzero degree-drop
cases, other projected curves and arbitrary chart entry remain
outside its conclusion.
