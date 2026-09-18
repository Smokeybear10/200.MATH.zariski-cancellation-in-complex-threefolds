# The affine-theta boundary with a moving intercept is impossible

Working scoped exclusion: retain the complete actual sigma-dominant
entry385/387 with (deg theta,deg sigma)=(1,2). After its actual
constant Y translation makes n=f(s), the subcase y_t nonzero is
impossible. The proof uses the complete literal calibrated scalar,
not an abstract quadric or a presumed rational coefficient field.

The complementary y_t=0 case is not used or proved here. No
coefficient-field recentering below is promoted to an original
polynomial coordinate change.

## 1. Actual input and the valid initial translation

Retain every actual hypothesis of
[385](principal-paraboloid-nonlinear-sigma-dominant-degree-reduction-pass385-working.md)
and the exact conclusion of
[387](principal-paraboloid-sigma-dominant-coefficient-integrability-pass387-working.md).
Thus the original globally sliced four-ring has the exact1222 frame,
full initial kernel (X^2Z-Y^2), literal selected partial and its
nonzero leading LND N, exact finite coefficient field L/C(t,s),
and all the polynomial/field returns and calibrated scalar of264.
In particular
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad
a_0=EX\ne0,\quad N=[u^4]\partial_Z|_A,\\
Nv=1,\quad L=\operatorname{Frac}\ker_A N,\quad
O=L[v]=L[y,\sigma,\theta]=L[y,z,w],\\
K=L(v)=\mathbb C(y,z,w),\qquad
\deg_v\theta=1,\quad\deg_v\sigma=2,\quad k=s,\quad n_{ss}\ne0.
\end{gathered}
\tag{1}
\]
The exact coefficient partials commute. Their joint constants are C.
By387,
\[
n=\gamma t+f,\qquad \gamma\in\mathbb C,\qquad
f\in\ker_L\partial_t,\qquad f_{ss}\ne0,\qquad y\in L.
\tag{2}
\]
The actual polynomial translation Y*=Y+gamma/2, with X,Z,W fixed,
has inverse Y=Y*-gamma/2. Its new intercept is y*=y+gamma/2.
The first potential becomes n*=n-gamma*t=f, while the second
potential remains ell*=ell: the added gamma*sigma in 2sigma*y*
cancels the subtracted gamma*sigma in n*_t*sigma. All leaders,
the full initial ideal, k=s, the literal Z-partial, the scalar and
both returns are unchanged. Also y*_t=y_t.

Apply this verified actual map and drop stars. Henceforth
\[
n=f,\qquad f_t=0,\qquad
\nu=f_s\ne0,\qquad e=f_{ss}\ne0,\qquad y\in L,\qquad y_t\ne0.
\tag{3}
\]
No equality ker_L(partial_t)=C(s) is assumed.

Since theta has degree one, set V=theta as intrinsic line parameter.
Then O=L[V], tau:=Ntheta belongs to L*, and the actual scalar in
this parameter is
\[
J_{t,s,V}(X)=-a_0^4/\tau\in L^*.
\tag{4}
\]
The coefficient derivatives still restrict to the same partials on L,
but now fix V. This change is made before any determinant expansion.

## 2. The literal quadratic and the first two scalar gates

Write
\[
\sigma=A V^2+B V+C_0,\qquad A\in L^*,\quad B,C_0\in L,\qquad
D=\ell_t+2\nu y.
\tag{5}
\]
The full third equation specializes to
-D*sigma+(e/2)V^2-(ell_s+nu^2)V+y^2+nu*ell-h0=0.
If D were zero, its nonzero V^2 coefficient e/2 would contradict
the transcendence of V. Therefore
\[
D\ne0,\qquad A=\frac e{2D},\qquad
B=-\frac{\ell_s+\nu^2}{D}.
\tag{6}
\]
The complete literal rows are
\[
\begin{aligned}
Y&=y+\sigma X+tX^2,\\
Z&=2ty+\sigma^2+V+f+(2t\sigma+s)X+t^2X^2,\\
W&=\ell-2\sigma y-\nu V+VX+sX^2 .
\end{aligned}
\tag{7}
\]
Derivatives in their determinant hold the original actual X fixed.
Calibration(4) forces every coefficient involving a positive power
of X or V to vanish.

For reproducibility, direct expansion of(7) gives
\[
\begin{aligned}
[X^2V]J&=e-2AD,&
[X^2]J&=-BD-\ell_s-\nu^2,\\
[XV^3]J&=4A^2\nu y_t+eA_t,&
[V^4]J(0)&=2A\big[(2Ae-\nu A_s)y_t+\nu A_t y_s\big].
\end{aligned}
\tag{8}
\]
The first two agree with(6). Because e_t=nu_t=0,
A_t=-eD_t/(2D^2) and D_t=ell_tt+2nu*y_t. Thus the third is
-e^2*ell_tt/(2D^2), and it proves
\[
\ell_{tt}=0.
\tag{9}
\]

Put p=ell_t, so p_t=0. In the last coefficient of(8), substitute
\[
A_t=-\frac{e\nu y_t}{D^2},\qquad
A_s=\frac{e_sD-e(p_s+2ey+2\nu y_s)}{2D^2}.
\]
Using D=p+2nu*y, the complete coefficient is
\[
[V^4]J(0)=\frac{e y_t}{2D^3}
 \left[p(2e^2-\nu e_s)+\nu e p_s
                       +2\nu y(3e^2-\nu e_s)\right].
\tag{10}
\]
All denominators and its prefactor are nonzero. The bracket vanishes.
Its t derivative is 2nu*y_t*(3e^2-nu*e_s), since p,nu,e and their
s derivatives are t-constant. Consequently
\[
\nu e_s=3e^2,\qquad \nu p_s=ep.
\tag{11}
\]
No division by p is involved.

## 3. Exact integrations and a separating coefficient basis

Both partials annihilate p/nu and e/nu^3. Their joint constants
therefore give complex constants
\[
p=\kappa\nu,\qquad e=\rho\nu^3,\qquad
\kappa\in\mathbb C,\quad \rho\in\mathbb C^*.
\tag{12}
\]
Direct differentiation, inside the original exact field, now gives
\[
s=s_0-\frac1{2\rho\nu^2},\qquad
f=f_0-\frac1{\rho\nu},\qquad
\ell=\kappa\nu t+L_0,
\quad s_0,f_0\in\mathbb C,\quad (L_0)_t=0.
\tag{13}
\]
For example s+1/(2rho*nu^2) has both derivatives zero, using
nu_s=e=rho*nu^3. Similarly f+1/(rho*nu) is a joint constant.
Subtracting kappa*nu*t from ell gives the last assertion. The
possible algebraicity of nu over C(s) has not been discarded.

Define
\[
\eta=y+\kappa/2.
\tag{14}
\]
Its t derivative is y_t nonzero, so eta is a nonzero field element.
The Jacobian of (eta,nu) with respect to (t,s) is y_t e, nonzero.
Thus eta,nu form a separating transcendence basis of L/C and L is
finite over C(eta,nu). Use its exact commuting coefficient partials
partial_eta,partial_nu, and write T for the old element t in this
basis. In particular
\[
T_\eta=1/y_t\ne0,\qquad (L_0)_\eta=0.
\tag{15}
\]
This notation is not an assertion that T or L0 is rational in its
displayed coefficient arguments. On t-constant elements,
partial_nu equals e^(-1)partial_s.

The scalar in the new coefficient basis, still using V=theta, is
\[
J_{\eta,\nu,V}(X)
 =-\frac{a_0^4}{\tau y_t e}\in L^*.
\tag{16}
\]
Therefore it is still independent of both X and V.

## 4. A third scalar coefficient makes L0 affine

In the new basis, (6),(12),(13) give
\[
A=\frac{\rho\nu^2}{4\eta},\qquad
B=-2A\left(\kappa T+(L_0)_\nu+\frac1{\rho\nu}\right).
\tag{17}
\]
Indeed ell_s=kappa*e*t+e*(L0)_nu, with that derivative originally
taken at fixed t. Also y=eta-kappa/2.

At X=0, the first determinant row is (1,0,0). The other intercepts
are z=2Ty+sigma^2+V+f and
w=kappa*nu*T+L0-2y*sigma-nu*V. Hence
J(0)=z_nu*w_V-z_V*w_nu. Its V^3 coefficient is exactly
\[
-2\nu(AB_\nu+BA_\nu)
 -4A^2\big(\kappa T+\kappa\nu T_\nu+(L_0)_\nu\big)+6AB
 =\frac{\rho^2\nu^5}{4\eta^2}(L_0)_{\nu\nu}.
\tag{18}
\]
For the equality, use A_nu=2A/nu and the full derivative of B
in(17); all T_nu terms cancel. This retains all field derivatives.

Calibration(16) and the nonzero prefactor force (L0)_nunu=0.
Together with (L0)_eta=0 and the exact joint constant field, this
integrates to
\[
L_0=p_0\nu+q_0,\qquad p_0,q_0\in\mathbb C.
\tag{19}
\]
No equality between a one-variable coefficient field and C(nu)
is required for this integration.

## 5. The centered literal map and the contradiction

Now make only an intrinsic affine parameter change
\[
\xi=V-\kappa T-p_0-\frac1{\rho\nu},\qquad
\sigma=\frac{\rho\nu^2}{4\eta}\xi^2+D_0,\qquad D_0\in L.
\tag{20}
\]
The absence of a linear xi term follows exactly from(17),(19).
This translation has derivative one with respect to V, so it does
not change the scalar(16); no moving evaluation is differentiated.

Set z0=p0+f0 and w0=q0-1/rho, both complex. The literal intercepts
and rows(7) become
\[
\begin{aligned}
y&=\eta-\kappa/2,&
z&=\sigma^2+\xi+2\eta T+z_0,&
w&=w_0-(2\eta-\kappa)\sigma-\nu\xi,\\
Y&=y+\sigma X+TX^2,\\
Z&=\sigma^2+\xi+2\eta T+z_0
                         +(2T\sigma+s)X+T^2X^2,\\
W&=w_0-(2\eta-\kappa)\sigma-\nu\xi
 +\left(\xi+\kappa T+p_0+\frac1{\rho\nu}\right)X+sX^2,\\
s&=s_0-\frac1{2\rho\nu^2}.
\end{aligned}
\tag{21}
\]
Every displayed row is the original coordinate, not an ambient
operation over L. The element T in all its occurrences is retained
with both of its exact derivatives.

Writing J for the determinant of(21) in the basis (eta,nu,xi),
direct expansion gives the two exact coefficients
\[
\begin{aligned}
[X\xi]J&=
 \frac{2\eta\nu(D_0)_\eta-2\eta+\kappa+2\nu D_0}
      {2\eta\nu},\\
[\xi^2]J(0)&=
 \frac{\rho\nu}{2\eta}
       \big(2\eta-\kappa-\nu^2(D_0)_\nu\big).
\end{aligned}
\tag{22}
\]
One can check the second using only
J(0)=z_nu*w_xi-z_xi*w_nu as in Section4.
For the first one must retain the full X terms in(21); it is not
an intercept-only determinant claim.

Both coefficients vanish by(16). Thus
\[
\eta(D_0)_\eta+D_0=\frac{\eta-\kappa/2}{\nu},\qquad
(D_0)_\nu=\frac{2\eta-\kappa}{\nu^2}.
\tag{23}
\]
Differentiate the first in nu and the second in eta. Since the exact
coefficient partials commute, substitution yields
\[
\frac{4\eta-\kappa}{\nu^2}
 =-\frac{\eta-\kappa/2}{\nu^2},
\qquad\text{hence}\qquad 5\eta=\frac{3\kappa}{2}.
\tag{24}
\]
This contradicts eta_t=y_t nonzero. The y_t-nonzero affine-theta
boundary is therefore excluded.

## 6. Scope and verification record

This proof excludes only the actual pair(1,2) after387 with y_t
nonzero. It neither assumes nor proves the complementary constant-t
case, and it does not treat the other surviving sigma-dominant pairs.
The finite coefficient fields and actual calibration are retained
through every change of variables. None of eta,nu,xi,T,D0 is
asserted to be an original coordinate.

The complete held387 source was read through EOF in af9b7a and its
hash revalidated in bf31b4. Its prior actual385 input was independently
fully reviewed in f1494e. The initial Y translation is proved directly
in Section1 rather than imported from a formal coefficient reframe.

Fresh unsaved510a64 reconstructed the full literal determinant and
the four coefficients(8), with all original coefficient jets arbitrary.
A separate expansion898a3e, completed on its original handle54622
in9ac55e, gave(18) without a rational-field assumption. The shorter
coefficient ledgers(10),(18) were independently reduced to zero in
3e4ae5. Fresh unsaved349f85 reconstructed the entire determinant
of(21) and the two coefficients(22); Root independently rebuilt the
same literal map and both coefficients in23abeb.

No saved checker was executed, imported, compiled or rerun. No earlier
source or canonical index was edited. The finite computations
supplement the written coefficient-field and scalar argument. No
unrestricted cancellation, realization, novelty, human-expert review
or proof-assistant certification is claimed.

