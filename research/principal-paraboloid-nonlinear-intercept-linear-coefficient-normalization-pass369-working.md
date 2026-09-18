# Actual removal of the linear coefficient in the strict reciprocal sector

Working result: in365's theta-dominant sector, suppose
1<=deg sigma<deg theta<2deg sigma. After an actual complex
translation of the leading ratio t, the coefficient
n=-s^2/(4t^2)+B(t)s+f(t) satisfies
B=b1/t+b2/t^2 with b1,b2 complex. An explicit actual polynomial
automorphism then gives k=s and n=-s^2/(4t^2)+f_new(t), preserving
the full initial kernel, selected literal partial, both returns,
and exact scalar calibration.

This applies in particular to the two necessary pairs (2,3) and
(4,6) left by367. It does not assert this derivative gate for the
constant-residual pair (1,2), recognize the resulting kernel, or
normalize arbitrary nonzero coupling.

## 1. The full actual sector and its coefficient fields

Retain the complete actual hypotheses of
[365](principal-paraboloid-nonlinear-intercept-unequal-degree-gate-pass365-working.md):
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad
\deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(X^2Z-Y^2)\text{ is the full initial kernel},\quad
a_0=EX\ne0,\quad N=[u^4]\partial_Z|_A,\\
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,\quad
Nv=1,\quad O=L[v]=L[y,\sigma,\theta]=L[y,z,w],\\
K=L(v)=\mathbb C(y,z,w),\qquad
\det\frac{\partial(Y,Z,W)}{\partial(t,s,v)}=-a_0^4\in L^*.
\end{gathered}
\tag{1}
\]
Here k=s, n_ss is nonzero, and
\[
\begin{aligned}
Y&=y+\sigma X+tX^2,\\
Z&=z+(2t\sigma+s)X+t^2X^2,\\
W&=w+\theta X+sX^2,\\
z&=2ty+\sigma^2+\theta+n,\qquad
w=\ell-2\sigma y-n_t\sigma-n_s\theta .
\end{aligned}
\tag{2}
\]
All coefficient partials commute on the exact finite field L.
Let F=ker_L partial_s, finite over C(t); its partial_t constants
are exactly C. No equality L=F(s) or F=C(t) is assumed.

Write
\[
a=\deg_v\sigma,\qquad h=\deg_v\theta,\qquad
1\le a<h<2a,\qquad r=2a-h>0.
\tag{3}
\]
The letters a,h in (3) are degrees and not the speed or potential
level. By365, n_ss=-1/(2(t-tau)^2) for tau in C.

## 2. The translation t-tau can be made in the actual ring

Use the actual polynomial change
\[
X_1=X,\qquad Y_1=Y-\tau X^2,\qquad
Z_1=Z-2\tau Y+\tau^2X^2,\qquad W_1=W.
\tag{4}
\]
Its inverse is
\[
X=X_1,\quad Y=Y_1+\tau X_1^2,\quad
Z=Z_1+2\tau Y_1+\tau^2X_1^2,\quad W=W_1.
\tag{5}
\]
Both compositions are polynomial identities. The weighted identity
X_1^2 Z_1-Y_1^2=X^2Z-Y^2 preserves the entire initial kernel.
The new ratios and intercepts are
\[
t_1=t-\tau,\quad s_1=s,\quad
y_1=y,\quad \sigma_1=\sigma,\quad
z_1=z-2\tau y,\quad \theta_1=\theta,\quad w_1=w.
\tag{6}
\]
Thus k1=s1, n1=n, and ell1=ell in the rebuilt first two potentials.
All four leading coefficients remain nonzero, since t-tau and s
are algebraically independent. The literal partial
partial_Z1 equals old partial_Z, so N,L,O and Nv=1 are unchanged.
The coefficient change and actual bad-coordinate change have
determinant one, preserving the calibration in (1). The intercept
change is complex and invertible, preserving both returns.

Drop the subscripts. By the exact integration in365, we now have
\[
n=-\frac{s^2}{4t^2}+B s+f,\qquad B,f\in F.
\tag{7}
\]
This is an actual normalized chart, not merely the use of the
symbol t-tau in a coefficient identity.

## 3. A modified genuine cubic isolates B

Use the exact formal coefficients and variables of365:
\[
\begin{gathered}
\nu=n_s,\quad b=n_{ts},\quad e=n_{ss}=-1/(2t^2),\quad
A=n_{tt}/2-\nu^2,\quad C=\ell_s+\nu^2,\\
x=U+n_t/2-\nu P,\quad \zeta=x+V/(2t),\quad
R=\zeta-tbP+tC,\quad \Omega=A+t^2b^2\ne0.
\end{gathered}
\tag{8}
\]
After evaluation,
deg P=a, deg V=h, deg R=r=2a-h<a.
The full third level is
\[
H-h_0
=\zeta^2+AP^2-\ell_tP-\bar h-\frac VtR,\qquad
\bar h=h_0-\nu\ell+n_t^2/4.
\tag{9}
\]
Let Q be the complete cubic in365, whose actual level is q0.
For clarity its homogeneous degree-three part in U,P,V is
\[
Q_3=-2bP^2U-2ePVU+
\frac{n_{ttt}}6P^3+\frac{n_{tts}}2P^2V
+\frac{n_{tss}}2PV^2+\frac{n_{sss}}6V^3 .
\tag{10}
\]
Every omitted term of Q has total degree at most two, and all
coefficient partials in (10) hold formal variables fixed.

Substitute the affine inverse
\[
U=(tb+\nu)P+R-\frac{V}{2t}-tC-\frac{n_t}{2}
\tag{11}
\]
into both levels, and define
\[
\widetilde Q=(Q-q_0)+\frac Pt(H-h_0).
\tag{12}
\]
It still vanishes on the actual line. Moreover its gradient minors
with H equal those of Q on that line, since the added gradient is
(P/t)grad H there.

The entire homogeneous cubic part in the independent variables
P,R,V is
\[
\boxed{
\widetilde Q_3=D_0P^2V+E_0P^3+\frac1tPR^2,
}
\qquad
\begin{aligned}
D_0&=\frac{B''}{2}+\frac{2B'}t+\frac B{t^2}
       =\frac{(t^2B)''}{2t^2},\\
E_0&=\frac{n_{ttt}}6-tb^2-2b\nu+\frac At.
\end{aligned}
\tag{13}
\]
All remaining terms have total degree at most two.
Here primes denote partial_t on F, which preserves F.

The cancellations in (13) can be checked without dropping lower
coefficient derivatives. Since n_sss=0 and n_tss=1/t^3, the PV^2
coefficient in (10),(11) cancels. Before the addition in (12),
the P^2R and PRV coefficients are -2b and 1/t^2.
The cubic part of (P/t)(H-h0) is
Omega P^3/t+2bP^2R+PR^2/t-PRV/t^2.
These cancel both mixed terms. The remaining P^2V coefficient is
\[
\frac{n_{tts}}2+\frac{2b}t+\frac{\nu}{t^2}
=\frac{B''}{2}+\frac{2B'}t+\frac B{t^2},
\]
because the terms involving s cancel exactly. This gives (13),
including the P^3 coefficient.

The intrinsic degree of P^2V is 2a+h. It is strictly larger than
3a and a+2r, the degrees of the other two cubic monomials.
Every lower total-degree term has intrinsic degree at most 2h,
and
2a+h-2h=2a-h=r>0.
Thus the only possible term of largest intrinsic degree in (12)
is D0 sigma^2 theta. Its leading coefficient must vanish:
\[
(t^2B)''=0.
\tag{14}
\]
Integrate in the exact field F. The first derivative of t^2B is
a constant of partial_t and hence is a complex number b1.
Subtract b1 t and integrate once more. Therefore
\[
\boxed{B=\frac{b_1}{t}+\frac{b_2}{t^2},\qquad b_1,b_2\in\mathbb C.}
\tag{15}
\]
The constants can vanish. No rational-function ansatz was used.

The strict inequality h<2a is essential to this argument.
If r=0, a quadratic V^2 term has the same intrinsic degree as
P^2V. Consequently the proof does not establish (14) for the
pair (1,2).

## 4. An actual complex polynomial map removes B

Only after (15), make the actual change
\[
\boxed{
X_*=X,\quad Y_*=Y+b_1X,\quad Z_*=Z-2b_2X,\quad
W_*=W-2b_1Y-2b_2X^2.
}
\tag{16}
\]
Its complete polynomial inverse is
\[
\boxed{
X=X_*,\quad Y=Y_*-b_1X_*,\quad Z=Z_*+2b_2X_*,\quad
W=W_*+2b_1Y_*+2b_2X_*^2-2b_1^2X_*.
}
\tag{17}
\]
Both compositions are the identity, including when either constant
is zero. The full X-dependent substitutions give
\[
\begin{gathered}
t_*=t,\quad s_*=s-2b_1t-2b_2,\quad a_{0,*}=a_0,\\
y_*=y,\quad \sigma_*=\sigma+b_1,\quad z_*=z,\quad
\theta_*=\theta-2b_1\sigma,\quad w_*=w-2b_1y,\\
k_*=s_*,\qquad n_*=n-b_1^2.
\end{gathered}
\tag{18}
\]
For example the new linear coefficient of Z is
2t sigma+s-2b2=2t sigma_*+s_*, and the new quadratic
coefficient of W is s_*.

The first potential and (7),(15) now give
\[
\boxed{
n_*=-\frac{s_*^2}{4t^2}+f_*,\qquad
f_*=f+\frac{2b_1b_2}t+\frac{b_2^2}{t^2}\in F .
}
\tag{19}
\]
To retain the derivative convention explicitly, the rebuilt partials
on the same coefficient field are
\[
\partial_{t,*}=\partial_t+2b_1\partial_s,\qquad
\partial_{s,*}=\partial_s.
\tag{20}
\]
Thus (n_*)_{t,*}=n_t+2b1 n_s and (n_*)_{s,*}=n_s.
Substitution into the literal second potential gives exactly
\[
\ell_*=\ell+b_1 n_t+2b_1^2n_s.
\tag{21}
\]
No restriction on ell or ell_ss was imposed or silently preserved
under the wrong holding variables.

## 5. Original-ring, selected-partial, and scope gates

The weighted leading map of (16) fixes X,Y,Z and sends
W to W-2b1Y-2b2X^2. It is an invertible complex weighted
polynomial map fixing the generator X^2Z-Y^2 of the full initial
ideal. Hence the full initial-kernel hypothesis is preserved.
The new leading ratio s_* is algebraically independent of t,
so every required leader remains nonzero and the exact profile
is still (1,2,2,2).

The inverse (17) shows literally that
\(\partial_{Z_*}=\partial_Z\).
Consequently the same original slice u selects the same N, with
the same L,O and Nv=1. The first two intrinsic degrees are
unchanged: sigma_* differs from sigma by a complex constant, while
theta_* differs from theta by a polynomial of strictly smaller
intrinsic degree. Thus (3) survives the reframe.

The intercept map (y,z,w) -> (y,z,w-2b1y) has a complex polynomial
inverse, preserving both K=C(y,z,w) and L[y,z,w]=O.
The actual bad-coordinate Jacobian of (16), at fixed X, is one.
The coefficient map (t,s) -> (t,s_*) also has determinant one.
Therefore the complete rebuilt scalar remains -a0^4, not merely
some unspecified nonzero scalar. The remaining potentials can
thus be rebuilt in the same actual264 chart with coefficients
(19),(21).

Combined with the independently scoped exclusions of
[367](principal-paraboloid-nonlinear-intercept-geometric-degree-exclusions-pass367-working.md),
this supplies the actual normal form (19) for its pairs (2,3) and
(4,6). The pair (1,2) is outside this coefficient gate.
Nothing here excludes or recognizes the normalized family (19),
or changes the status of equal/reversed degree patterns.

The exact cubic support was independently reconstructed in fresh
unsaved algebra. Separate unsaved substitution verified all full
X-map identities, both inverse orders, both determinant factors,
the two lower-potential transports, and the normalized first
potential, with zero residuals. These checks do not certify the
exact-field or original-ring arguments in place of the written proof.
No saved checker was executed, imported or compiled; no retained
source or index was changed. No arbitrary-coupling, unrestricted
cancellation, novelty, human-expert or proof-assistant certification
claim is made.
