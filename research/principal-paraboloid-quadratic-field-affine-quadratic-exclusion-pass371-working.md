# The quadratic coefficient-field mode has zero scalar Jacobian

Working exclusion: the nonzero-D alternative of368 cannot occur in
its full actual chart. The finite quadratic coefficient field is
accepted and used as an exact parameter field. After an actual
complex normalization, two full-J coefficients and the third-level
compatibility integrate the relevant lower coefficients. The final
intercept determinant has a positive-degree coefficient whose
vanishing forces its calibrated value to vanish as well.

This excludes only368's D nonzero branch. It does not exclude the
different D=0 branch, identify F with a rational field, or recognize
the other nonlinear degree profiles.

## 1. Retained actual entry and the exact nonzero-D alternative

Retain the complete hypotheses and normal form of
[368](principal-paraboloid-affine-quadratic-nonlinear-profile-normal-form-pass368-working.md),
with the actual264 and296 chart supplied through365. In particular
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,
\quad\deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(X^2Z-Y^2)\text{ is the full initial kernel},
\quad a_0=EX\ne0,\\
O=L[P],\quad P=\sigma,\quad\tau_0=NP\in L^*,
\quad [L:\mathbb C(t,s)]<\infty,\\
K=L(P)=\mathbb C(y,z,w),\quad k=s,
\qquad J_{t,s,P}(X)=-a_0^4/\tau_0\in L^*.
\end{gathered}
\tag{1}
\]
Here F=ker_L(partial_s) is finite over C(t), and its exact
t-derivative has constant field C. The actual complex tau-translation
has already been performed in368. Its remaining data are
\[
\begin{aligned}
n&=-s^2/(4t^2)+B(t)s+f(t),\\
D&=(t^2B)''\ne0,\quad 2tD'+3D=0,\quad t^3D^2=d_0\in\mathbb C^*,\\
B&=b_1/t+b_2/t^2-4D,\qquad b_1,b_2\in\mathbb C,\\
\theta&=-P^2+\beta P+\gamma,\qquad
\beta=s/(2t)+\beta_0(t),\\
y&=-\theta/(2t)+jP+k,\quad j=n_s+t n_{ts},\\
G&=2tk+n-t^2j^2=Ds+g(t),\qquad f,\beta_0,g\in F.
\end{aligned}
\tag{2}
\]
The function gamma belongs to L and is not initially restricted.
Both exact partials on L commute, and all later changes specify
their holding variables.

## 2. Removing only the complex part of B is an actual map

Use the actual polynomial automorphism
\[
X_*=X,\quad Y_*=Y+b_1X,\quad Z_*=Z-2b_2X,
\quad W_*=W-2b_1Y-2b_2X^2.
\tag{3}
\]
Its inverse is
\[
X=X_*,\quad Y=Y_*-b_1X_*,\quad Z=Z_*+2b_2X_*,
\quad W=W_*+2b_1Y_*+2b_2X_*^2-2b_1^2X_*.
\tag{4}
\]
This is the complex map appearing in Section4 of
[369](principal-paraboloid-nonlinear-intercept-linear-coefficient-normalization-pass369-working.md).
We use its literal identities, not369's strict-degree gate D=0,
which does not apply here. Direct substitution in the full map gives
\[
\begin{gathered}
t_*=t,\quad s_*=s-2b_1t-2b_2,\quad
P_*=P+b_1,\quad y_*=y,\quad z_*=z,\\
\theta_*=\theta-2b_1P,\quad w_*=w-2b_1y,\quad
k_*=s_*,\quad n_*=n-b_1^2,\\
\partial_{t,*}=\partial_t+2b_1\partial_s,\quad
\partial_{s,*}=\partial_s,\quad
\ell_*=\ell+b_1n_t+2b_1^2n_s.
\end{gathered}
\tag{5}
\]
The first potential therefore becomes, with D unchanged,
\[
n_*=-s_*^2/(4t^2)-4Ds_*+f_*,\qquad
f_*=f+2b_1b_2/t+b_2^2/t^2-8D(b_1t+b_2)\in F.
\tag{6}
\]
In particular the nonconstant term -4D was not used as a coefficient
of the ambient automorphism. The full initial kernel is preserved by
the invertible weighted leading map. The ratios t and s* remain
algebraically independent, so all required leaders and exact time
degrees survive. The literal Z*-partial equals
the old Z-partial, so N,L,O and tau0 are unchanged. The actual and
coefficient Jacobians are one. The complex invertible intercept map
(y,z,w) to (y,z,w-2b1y) preserves both returns.

The intrinsic coefficient of P_* squared in theta_* is still -1,
and its linear coefficient has the required form s_*/(2t)+a function
in F. Also j_*=j-b1/t and U_*=P_*+t(X_*+j_*)=P+t(X+j).
The new G is Ds_* plus an element of F. Thus the entire normal form
(2) survives after dropping stars, now with B=-4D.

## 3. The quadratic extension is a legitimate separating parameter

Choose d in C* with d^2=d0 and set a=t^2D/d. Then
\[
a^2=t,\qquad D=d/a^3,\qquad
\partial_a=2a\partial_t\text{ on F}.
\tag{7}
\]
Here a belongs to F, F is finite over C(a), and its a-derivative
constants are C. There is no assertion F=C(a). The exact partials
in a,s commute. The new scalar is
\[
J_{a,s,P}(X)=-2a a_0^4/\tau_0\in L^*.
\tag{8}
\]
The element a is a coefficient parameter, not an original coordinate
or the actual speed a0. From now on primes mean d/da on F, and
the old fixed-s t-derivative means (1/(2a))partial_a.

We can rewrite the remaining data as
\[
\begin{aligned}
t&=a^2,\quad B=-4d/a^3,\quad n=-s^2/(4a^4)-4ds/a^3+f(a),\\
j&=s/(2a^4)+2d/a^3,\qquad
\beta=s/(2a^2)+b_0(a),\qquad G=ds/a^3+g(a),\\
k&=(G-n+a^4j^2)/(2a^2),\qquad
\theta=-P^2+\beta P+\gamma,\qquad
y=-\theta/(2a^2)+jP+k.
\end{aligned}
\tag{9}
\]
The functions f,g,b0 lie in F; gamma and ell still lie in L.
The first two potentials and actual map remain precisely
\[
\begin{aligned}
z&=2a^2y+P^2+\theta+n,\qquad
w=\ell-2Py-n_tP-n_s\theta,\\
Y&=y+PX+a^2X^2,\\
Z&=z+(2a^2P+s)X+a^4X^2,\\
W&=w+\theta X+sX^2.
\end{aligned}
\tag{10}
\]
In (10), n_t is computed at fixed s before any other substitution.

## 4. Three exact lower-coefficient integrations

Put zeta0=k+n_t/2 and Omega=n_tt/2-n_s^2+a^4 n_ts^2.
The two third-level coefficient identities of368 are
\[
\ell_s=-\zeta_0/a^2-n_{tt}/2-a^4n_{ts}^2,\qquad
\ell_a=2a\{2a^2n_{ts}\zeta_0+\beta\Omega\}.
\tag{11}
\]
Use the polynomial parameter U=P+a^2(X+j) at fixed actual X.
Its parameter determinant is one, so (8) is unchanged. Define
\[
L_3=-8a^4d\gamma_s-a^4g'+2a^3d b_0'+40ad^2+7ds,
\qquad T_3=a^4g'+2a^2d b_0+8ad^2.
\tag{12}
\]
Differentiate the full map (10), and then substitute (11). Its two
coefficients are
\[
[U^3X^0]J=\frac{L_3}{4a^{10}},\qquad
[U^0X^3]J=-\frac{L_3+2T_3}{4a^4}.
\tag{13}
\]
All coefficient derivatives here fix U; none differentiates an
evaluated moving point. Since the actual scalar is independent of
U,X, both L3 and T3 vanish. Thus
\[
b_0=-\frac{a^2g'}{2d}-\frac{4d}{a},\qquad
\gamma_s=\frac{7s}{8a^4}+\frac{6d}{a^3}
                -\frac{3g'+a g''}{8d}.
\tag{14}
\]
The second formula follows from L3=0 after differentiating the first
formula for b0. No g' or lower integration constant is divided by.

Before using (14), the exact mixed compatibility of (11) is
\[
\partial_a(\ell_s)-\partial_s(\ell_a)
=-\frac{a^5f'''+4a^3g'+8ad b_0-352d^2}{8a^7}.
\tag{15}
\]
Insert the first equation of (14). It gives f'''=384d^2/a^5.
Integrating in the exact field F, and integrating the second equation
of (14) in s, now gives the complete relevant family
\[
\boxed{\begin{aligned}
f&=-16d^2/a^2+f_2a^2+f_1a+f_0,
             &&f_2,f_1,f_0\in\mathbb C,\\
\gamma&=\frac{7s^2}{16a^4}
 +\left(\frac{6d}{a^3}-\frac{3g'+a g''}{8d}\right)s+c_0(a),
             &&c_0\in F.
\end{aligned}}
\tag{16}
\]
For precision, the displayed primitive of f''' has that exact third
derivative; the difference has zero third derivative and is complex
quadratic in a. The difference in the gamma integration has zero
s-derivative, placing it in F. These facts do not require rationality
of g or c0, which remain arbitrary elements of F subject to the
remaining scalar equations.

## 5. A positive-degree coefficient kills the calibrated value

It is enough now to set actual X=0. Let
\[
J_0(P)=\det\frac{\partial(y,z,w)}{\partial(a,s,P)}
       =-2a a_0^4/\tau_0\in L^*.
\tag{17}
\]
Use (9),(10),(14),(16), and substitute the two derivatives of ell
from (11) after differentiating. The following expression belongs to L:
\[
\begin{aligned}
R={}&-a^8g'g''-a^7(g')^2-8a^5d^2g''+a^5ds g'''\\
&+8a^4d^2f_1-8a^4d^2c_0'+40a^4d^2g'
 +3a^4ds g''\\
&+16a^3d^2(f_0+c_0-g)-192ad^4+24d^3s.
\end{aligned}
\tag{18}
\]
The literal three-by-three determinant gives
\[
\deg_P J_0\le2,\qquad [P^2]J_0=-\frac{R}{16a^{11}d}.
\tag{19}
\]
There is also an exact identity for its value at P0=-a^2j:
\[
\boxed{
J_0(P_0)=
2a^2\left(y(P_0)+\frac{f_2}{2}+\frac{f_1}{4a}\right)
[P^2]J_0.}
\tag{20}
\]
This is polynomial evaluation after formation of J0, not
differentiation while holding the moving P0 fixed. All quantities
in (18)--(20) use the original a,s partials fixing P.

Here are explicit expansion data for verifying the second identity
without differentiating P0. Define
\[
\begin{aligned}
M={}&-8a^5df_1-16a^5dg'+2a^5s g''
 -16a^4d(f_0+c_0-g)\\
&+2a^4s g'+128a^2d^3-32ad^2s+ds^2.
\end{aligned}
\tag{21}
\]
Direct determinant expansion gives J0(P0)=-MR/(256a^15d^2).
Separately, substituting P0 into the explicit y in (9) gives
M=32a^6d(y(P0)+f2/2+f1/(4a)). Together with (19), these prove (20).
Thus both sides can be checked from the two literal potentials,
without a closed form for ell or a special choice of g,c0.

Calibration (17) makes [P^2]J0 zero. Equation (20) then makes J0(P0)
zero, contradicting the same nonzero constant in (17). Equivalently,
(19) first forces R=0 and the factorized constant value then vanishes.
This contradiction includes f1=0, g'=0, c0'=0, and all zero values of
the complex integration constants; none was divided away.

## 6. Conclusion and evidence boundaries

The nonzero-D alternative of368 is excluded. The proof uses the
finite quadratic coefficient field rather than rejecting it as
nonrational over C(t). The actual polynomial map only removes the
complex b1,b2 terms. The parameters a and U, and the value P0, are
never promoted to original coordinates.

The zero-D alternative of368 remains outside this result, as do the
other intrinsic degree pairs. The complete368 and369 sources were
read; the earlier complete264/296/365 reads supplied their direct
entry. Fresh unsaved422c11 checked the generalized actual map and
both potential transports. Calculation0232f5 reconstructed (13),(15)
with arbitrary lower coefficient functions. Calculation7557f7 rebuilt
the remaining full determinant after (16), including the common
factor (18). A separate formal-jet reconstruction356f54 independently
recomputed (19) and J0(P0) from the original X=0 rows and verified
the displayed relation between M and y(P0). Every stated residual
was zero. These checks supplement the written exact-field argument,
not a rationality assumption or finite-sample certification.

No saved checker was executed, imported, compiled, or rerun by this
author. No earlier source or canonical index was edited. No
unrestricted recognition, cancellation, historical novelty, external
expert review, or proof-assistant certification is claimed.
