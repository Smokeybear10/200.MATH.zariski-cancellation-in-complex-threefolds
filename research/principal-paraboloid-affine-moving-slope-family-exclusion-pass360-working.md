# The complex-affine moving-slope family is excluded

Working exclusion: the affine-B family (26) of353 cannot occur in its
full actual chart. An explicit complex polynomial reframe makes both
y and theta constant on the selected intrinsic line. The corrected
fourth-potential coefficient and the original scalar then force the
entire t-column of the intercept Jacobian to vanish.

This note treats only that affine-B family, not the reciprocal family
(28) of353. It gives the inverse of the actual reframe. No assertion
about a merely rational coordinate change or the kernel of a different
auxiliary action is needed.

## 1. The exact353 family and full actual inputs

Retain the full hypotheses of
[353](principal-paraboloid-affine-sigma-moving-slope-frontier-pass353-working.md),
including its clarified use of the scalar at X=0. In particular
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad
\deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(X^2Z-Y^2)\text{ is the full initial kernel},
\quad a_0=EX\ne0,\\
O=L[v]=L[y,\sigma,\theta],\quad Nv=1,\quad
K=L(v)=\mathbb C(y,z,w),\quad [L:\mathbb C(t,s)]<\infty,\\
k=s,\quad n=Bs+f,\quad \deg_v\sigma=1,\quad
J(X)=-a_0^4\in L^*.
\end{gathered}
\tag{1}
\]
The family has complex constants \(b\ne0,B_0,j,\kappa,f_1,f_0\), and
\[
\begin{aligned}
B&=bt+B_0,\\
f&=2bj\,t^3+(2B_0j-j^2-b\kappa)t^2+f_1t+f_0,\\
y&=j\sigma+k_0,\qquad
\theta=(\kappa-4jt)\sigma+e_0,\qquad k_0,e_0\in L.
\end{aligned}
\tag{2}
\]
Neither j nor kappa is assumed nonzero. The first two potentials are
\[
z=2ty+\sigma^2+\theta+n,\qquad
w=\ell-2\sigma y-n_t\sigma-B\theta,\qquad \ell\in L.
\tag{3}
\]
All coefficient partials are the exact commuting extensions to L.

## 2. Actual complex reframe, inverse, and selected derivation

Make the following change in the original polynomial ring:
\[
\boxed{X^*=X+j,\quad Y^*=Y+\frac{\kappa}{2}(X+j),\quad Z^*=Z,
\quad W^*=W+2jZ-\kappa Y.}
\tag{4}
\]
Its polynomial inverse is
\[
\boxed{X=X^*-j,\quad Y=Y^*-\frac\kappa2X^*,\quad Z=Z^*,\quad
W=W^*-2jZ^*+\kappa Y^*-\frac{\kappa^2}{2}X^*.}
\tag{5}
\]
Substitution in either order is the identity. Only complex constants
occur. Both the ambient Jacobian and the fixed-X bad-slot Jacobian
are one. This is not a shift by the nonconstant B(t).

The leading ratios in the new actual frame are
\[
t^*=t,\qquad s^*=s+2jt^2-\kappa t,\qquad a_0^*=a_0.
\tag{6}
\]
Since t,s are algebraically independent, so are t,s*, and s* is
nonzero. The exact time degrees remain (1,2,2,2). The invertible
weighted leading change fixes X,Y,Z and replaces W by
\(W+2jZ-\kappa Y\). It fixes the full initial ideal
\((X^2Z-Y^2)\), not merely one relation in that ideal.

The literal partial in the new coordinates is
\[
\partial_{Z^*}=\partial_Z-2j\partial_W.
\tag{7}
\]
Under the full initial kernel, the omitted W-pivot has shift at most
three, whereas the literal Z-pivot has shift four, by the complete
occurring-pivot statement of
[158](arbitrary-positive-weight-initial-bound-pass158-working.md).
Thus the selected leading derivation N, its constant field L, and O
are unchanged. No auxiliary kernel replaces the selected one.

## 3. Full literal transport of the potentials and scalar

At fixed X*, direct expansion gives
\[
\begin{aligned}
y^*&=y-j\sigma+j^2t,\\
\sigma^*&=\sigma-2jt+\kappa/2,\\
z^*&=z-j(2t\sigma+s)+j^2t^2,\\
\theta^*&=\theta+(4jt-\kappa)\sigma-4j^2t^2+2\kappa jt.
\end{aligned}
\tag{8}
\]
By (2), both y* and theta* belong to L, while sigma* is affine
nonconstant in the original v with the same speed \(\sigma_v\).
The slope of Z* is \(2t\sigma^*+s^*\), so \(k^*=s^*\).
The first potential is computed exactly:
\[
\begin{aligned}
n^*&=z^*-2ty^*-(\sigma^*)^2-\theta^*
       =n-js-j^2t^2-\kappa^2/4\\
&=(bt+B_0-j)s^*+\{f_1+\kappa(B_0-j)\}t+f_0-\kappa^2/4.
\end{aligned}
\tag{9}
\]
Thus, for the new derivatives holding s* fixed,
\[
(n^*)_{tt}=0,\quad (n^*)_{s^*}=bt+B_0-j,\quad
(n^*)_{ts^*}=b\ne0.
\tag{10}
\]
These derivatives on L are
\(\partial_{s^*}=\partial_s\) and
\(\partial_t|_{s^*}=\partial_t-(4jt-\kappa)\partial_s\).
They are not derivatives at fixed old s.

The new W-intercept is likewise the full literal expression
\[
w^*=w+2jz-\kappa y-j\theta-4j^2t\sigma+\kappa j\sigma
       -j^2s+2j^3t^2-\kappa j^2t.
\tag{11}
\]
The second potential of the rebuilt actual chart supplies
\(\ell^*\in L\); its value need not be restricted in advance.
The whole line and strong complex intercept field returns are the
actual ones of264 in this frame. The latter also follows directly by
evaluating at X*=0 in \(\mathcal B_{a_0}=A_{a_0}[X^*]\).

The actual bad-slot determinant in (4) and the coefficient determinant
\(\partial(t,s^*)/\partial(t,s)\) both equal one, so the rebuilt
full scalar remains \(-a_0^4\). With \(P=\sigma^*\), it becomes
\[
J_{t,s^*,P}(X^*)=-a_0^4/\sigma_v\in L^*.
\tag{12}
\]
This checks calibration as well as the actual entry and selected N.

## 4. The corrected scalar obstruction with y and theta constant

Drop stars in the rebuilt notation. We now have
\[
k=s,\quad y,\theta\in L,\quad P=\sigma,\quad
n=Bs+F_1t+F_0,\quad B=bt+\beta_0,
\tag{13}
\]
where \(b\in\mathbb C^*\) and \(\beta_0,F_1,F_0\) are complex.
Put
\[
u_1=n_t=bs+F_1,\qquad h_1=2y+u_1,\qquad w_0=\ell-B\theta.
\tag{14}
\]
The intercepts are exactly
\[
z=P^2+2ty+\theta+n,\qquad w=w_0-h_1P.
\tag{15}
\]
Using coefficient derivatives holding P fixed gives
\[
[P^2]\det\frac{\partial(y,z,w)}{\partial(t,s,P)}=2b\,y_t.
\tag{16}
\]
Indeed \(y_P=0,z_P=2P,w_P=-h_1\), while
\((h_1)_t=2y_t\) and \((h_1)_s=2y_s+b\). Expanding these entries
proves (16), with no omitted total derivative. The nonzero scalar
(12) forces \(y_t=0\), and then \((h_1)_t=0\).

Since y and theta are constant in P, the coefficient of P in the
third level (6) of349 gives
\[
\ell_t=b\theta-Bh_1.
\tag{17}
\]
The coefficient of \(P^2\) in the full fourth potential (9) of349 is
\[
-2by-\frac{\ell_{tt}+2b n_t}{2}=0,
\qquad\text{hence}\qquad \ell_{tt}=-2b h_1.
\tag{18}
\]
The term \(-b n_t\) in this coefficient is essential. Omitting it
would give the false gate \(\ell_{tt}=-4by\). An initial unsaved
calculation did omit that term; it was corrected before any endpoint
source was saved. In particular we do not use the resulting false
claim \((w_0)_t=-2Bn_t\).

Differentiate the correct (17), using \(B_t=b\) and \((h_1)_t=0\).
Together with (18) this yields
\[
b\theta_t-bh_1=-2bh_1,\qquad
\theta_t=-h_1,\qquad
(w_0)_t=\ell_t-b\theta-B\theta_t=0.
\tag{19}
\]
Equation (15) now gives
\[
y_t=0,\qquad z_t=2y+\theta_t+n_t=0,\qquad
w_t=(w_0)_t-(h_1)_tP=0.
\tag{20}
\]
The entire t-column of the intercept Jacobian vanishes, contradicting
(12) at X=0. This excludes the affine-B family. No division by y,
theta, j, kappa, or any lower coefficient was used.

## 5. Scope and verification

Only353's complex-affine-B family is excluded here. The reciprocal
family has a nonconstant theta slope after the same j-normalization
and cannot be put into (13) by treating that slope as complex.
It requires a separate argument.

The complete353,349,350,264,296 inputs and the complete158 pivot source
were read. Fresh unsaved algebra reconstructed the full starred map
and (9), the raw scalar coefficient (16), the corrected coefficient
(18), and the zero determinant after (19); every residual was zero.
The actual initial kernel, selected derivation, inverse and field
returns are checked separately above. No saved checker was executed,
imported, compiled or rerun. No earlier source or canonical index was
edited, and no unrestricted cancellation or novelty claim is made.
