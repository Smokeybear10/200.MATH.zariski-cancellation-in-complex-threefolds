# A necessary coefficient family for the complex-slope equal cubic profile

Working necessary reduction under the complete supplied actual264 chart,
with k=s and n_ss nonzero. In the equal-cubic profile(r,m,d)=(1,2,3),
a complex leading y/sigma slope can be normalized to zero by an actual
complex polynomial map. The full scalar and genuine fourth potential
then exclude beta=0 and force an exact quadratic coefficient family.
Its nonzero curvature ratio has nonzero characteristic derivative.

This note does not exclude the entire cubic profile. In particular it
does not assume a constant-ratio conclusion from a separate collision
argument. No coefficient-field parameter is an original coordinate,
and no degree-one or degree-two scalar exclusion is reused.

## 1. Complete actual hypotheses and the complex normalization

Retain EVERY actual hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
the genuine quadric/cubic of
[365](principal-paraboloid-nonlinear-intercept-unequal-degree-gate-pass365-working.md),
and the necessary higher-degree frontier in
[417](principal-paraboloid-equal-quadratic-exclusion-synthesis-pass417-working.md).
In particular,
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A_0[u_0],\quad E=\partial_{u_0},
\quad \deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the full initial kernel},\quad
0\ne N=[u_0^4]\partial_Z|_{A_0},\\
L=\operatorname{Frac}\ker_{A_0}N,\quad [L:\mathbb C(t,s)]<\infty,
\quad Nv_0=1,\quad a_0=EX\in L^*,\\
O=L[v_0]=L[y,\sigma,\theta]=L[y,z,w],\quad
K=L(v_0)=\mathbb C(y,z,w),\\
J_{t,s,v_0}(X)=-a_0^4\in L^*,\qquad k=s,\qquad e=n_{ss}\ne0.
\end{gathered}
\tag{1}
\]
Both original returns, the global slice, all actual polynomial-ring
conditions, literal selected partial, full genuine levels and their
unit ideals remain imposed. The coefficient partials on L commute
and have joint constant field C.

Assume the remaining profile is(r,m,d)=(1,2,3), with
\[
\lambda=\frac{[v_0^3]y}{[v_0^3]\sigma}\in\mathbb C,
\qquad \mu=\frac{[v_0^3]\theta}{[v_0^3]\sigma}\in L^*.
\tag{2}
\]
The ratio lambda is zero if deg(y)<3. By400 and417,
mu does not belong to C+C*t.

Use the ACTUAL384 constant shear with c=2lambda:
\[
X^*=X+c/2,\quad Y^*=Y,\quad Z^*=Z,\quad W^*=W+cZ.
\tag{3}
\]
Its polynomial inverse is X=X*-c/2, W=W*-cZ*, with Y,Z fixed.
The exact transports proved in
[384](principal-paraboloid-actual-filtered-symmetry-obstruction-pass384-working.md)
include
\[
\begin{gathered}
t^*=t,\quad s^*=s+ct^2,\quad \sigma^*=\sigma-ct,\\
y^*=y-c\sigma/2+c^2t/4,\quad
\theta^*=\theta+2ct\sigma-c^2t^2,\\
n^*=n-cs/2-c^2t^2/4,\qquad n^*_{s^*s^*}=n_{ss}.
\end{gathered}
\tag{4}
\]
The new leading y-slope is zero. The theta leader does not cancel:
its ratio is mu+2ct, nonzero by the400 restriction. Thus both
intrinsic degrees remain three. The full384 license preserves the
full initial kernel, actual time profile, both returns and scalar.
Its literal partial is partial_Z*=partial_Z-c*partial_W; the retained
omitted-partial shift bound makes its degree-four leading part N.
Consequently L and intrinsic degrees are unchanged.

Drop stars. The nonexceptional profile conclusion407 and d=3 give
(r,m,d)=(1,2,3) again in this normalized frame. Henceforth lambda=0.
Only the displayed complex actual map has been used; subsequent
parameter choices are coefficient-field or intrinsic choices.

## 2. Exact characteristic basis and the affine intrinsic remainder

Set nu=n_s, beta=n_ts+mu*e and Dscript=partial_t+mu*partial_s.
The all-degree necessary reduction
[413](principal-paraboloid-higher-degree-characteristic-zero-reduction-pass413-working.md)
gives Dscript(mu)=0 at lambda=0. Since mu is not complex, mu_s is
nonzero. Therefore q=mu is a separating coefficient parameter.
Use the exact commuting partials
\[
\dot{\ }=\mathscr D,\qquad {}'=\mu_s^{-1}\partial_s,\qquad
F=\ker_L\dot{\ },\qquad \dot t=1,\quad\dot q=0,\quad t'=0,\quad q'=1.
\tag{5}
\]
F is stable under primes and the joint constants remain C. No
equality F=C(q) or L=F(t) is imposed.

The top third-potential equation is n_tt+2q*n_ts+q^2*e=0.
It says ddot(n)=0, because dot(q)=0. Exact integration defines
\[
\begin{gathered}
s=qt+f,\quad n=At+B,\qquad f,A,B\in F,\\
D:=t+f'=s'=\mu_s^{-1}\ne0,\quad M:=A't+B',\\
\nu=M/D\ne0,\quad
\beta=\dot\nu=\frac{A'f'-B'}{D^2}
             =\frac{A'-\nu}{D},\qquad
\dot\beta=-\frac{2\beta}{D}.
\end{gathered}
\tag{6}
\]
For example A=dot(n), B=n-t*dot(n), f=s-qt are existing elements
of F. Nonzero nu follows from nu_s=e nonzero.

Put eta=theta-q*sigma and g=2y+A. In407 the affine-in-leading-
variable coefficient is now
\[
R=-\nu g+\beta\eta-\dot\ell.
\tag{7}
\]
Its intrinsic degree is one by the profile. Use the existing
affine intrinsic parameter zeta=R. Then O=L[zeta] and
rho=N(zeta) belongs to L*. Solving(7) gives
\[
g=k\eta+l\zeta+g_0,\qquad
k=\beta/\nu,\quad l=-1/\nu,\quad g_0=-\dot\ell/\nu.
\tag{8}
\]
The maximum intrinsic degree of y and eta is two. If eta had
degree at most one, (8) would make y have degree at most one,
a contradiction. Consequently
\[
\begin{gathered}
\eta=h_2\zeta^2+h_1\zeta+h_0,\quad h_2\in L^*,\\
P:=\sigma=p_3\zeta^3+p_2\zeta^2+p_1\zeta+p_0,
\quad p_3\in L^*,\qquad g_2:=[\zeta^2]g=k h_2.
\end{gathered}
\tag{9}
\]
The symbol h0 in this polynomial is distinct from the third level,
which will be denoted H0 below. No intrinsic parameter has been
declared an original coordinate.

For C=ell_s+nu^2 the complete third level is
\[
\zeta P+\frac{g^2}{4}-\frac{q\nu g}{2}
 +\frac e2\eta^2-C\eta
 -\frac{A^2}{4}+\frac{q\nu A}{2}+\nu\ell-H_0=0.
\tag{10}
\]
Its degree-four coefficient gives the exact leader relation
\[
p_3=-\frac{h_2^2}{4}(k^2+2e).
\tag{11}
\]
In particular k^2+2e is nonzero. This also follows from407's
nonzero curvature beta^2+2e*nu^2, with delta=-nu.

## 3. A full scalar coefficient separates the zero boundary

The literal original rows, now expressed in the exact(t,q,zeta)
basis but still using the original independent X, are
\[
\begin{aligned}
Y&=XP+(g-A)/2+tX^2,\\
Z&=P^2+(q+2tX)P+tg+\eta+B+(qt+f)X+t^2X^2,\\
W&=-gP+qXP+(X-\nu)\eta+\ell+(qt+f)X^2.
\end{aligned}
\tag{12}
\]
These follow directly from both264 potentials. In particular
n_t in the original basis is A-q*nu, not A.

The parameter change has Jacobian rho/D from(t,s,v0) to(t,q,zeta).
Thus the actual calibration becomes
\[
\widehat J(X)=\det\frac{\partial(Y,Z,W)}{\partial(t,q,\zeta)}
             =-\frac{Da_0^4}{\rho}\in L^*.
\tag{13}
\]
All dots and primes on coefficients of(9),(12) fix zeta and X.
Their possibly nonzero derivatives are retained.

Here is the complete top-coefficient ledger needed from(12).
For arbitrary lower coefficients p2,p1,p0,h1,h0 and g1,g0, put
\[
K_0=3p_3\dot g_2-2g_2\dot p_3.
\]
Directly taking the indicated coefficient of the three literal
differential rows in(12) gives
\[
\begin{aligned}
[X\zeta^7]\widehat J
=p_3\{&M K_0+(A'-\nu)(2\dot p_3h_2-3\dot h_2p_3)\\
       &-5A'g_2p_3+3\beta h_2p_3\}.
\end{aligned}
\tag{14}
\]
This identity uses dot(A)=dot(B)=dot(f)=0 and dot(nu)=beta,
but does not require any other scalar coefficient to vanish.
In particular derivatives of p3 and h2 were not set to zero.
The displayed ledger is obtained before using the actual relation
g2=k*h2. All lower-coefficient contributions cancel in this
single coefficient; the coefficient [X*zeta^8] is identically zero.

To simplify(14), use M=nu*D, A'-nu=beta*D and
\[
\dot k=-\frac{2\beta}{D\nu}-\frac{\beta^2}{\nu^2}.
\]
With g2=k*h2, the terms containing dot(p3) and dot(h2) cancel:
\[
\begin{aligned}
[X\zeta^7]\widehat J
&=h_2p_3^2\left(3\nu D\dot k-5A'k+3\beta\right)\\
&=-\frac{8A'\beta h_2p_3^2}{\nu}.
\end{aligned}
\tag{15}
\]
All factors other than A' and beta are already nonzero. By(13),
\[
\boxed{A'\beta=0.}
\tag{16}
\]
Neither factor has been divided out. This is a cubic-profile scalar
calculation; it is not the degree-one determinant from404.

## 4. The genuine Q coefficient with all actual level derivatives

Use the FULL365 polynomial with original t,s coefficient partials:
\[
\begin{aligned}
Q={}&[(c+2\ell_s)P+bV-2bP^2-2ePV-\ell_t]U\\
&+\frac{n_{ttt}}6P^3+\frac{n_{tts}}2P^2V
  +\frac{n_{tss}}2PV^2+\frac{n_{sss}}6V^3\\
&-\frac{\ell_{tt}+2bn_t}{2}P^2
 -(\ell_{ts}+\nu b+en_t)PV
 -\frac{\ell_{ss}+2\nu e}{2}V^2\\
&+(b\ell+n_t\ell_s-(H_0)_t)P
 +(e\ell+\nu\ell_s-(H_0)_s)V,
\end{aligned}
\tag{17}
\]
where b=n_ts and c=n_tt. Both actual level derivatives remain
present. Form this polynomial before making the substitution
\[
U=(k\eta+l\zeta+g_0-A)/2,\qquad V=qP+\eta.
\]
The exact derivative identities from(5),(6) are
\[
\begin{gathered}
b=\beta-qe,\quad c=-2qb-q^2e,\quad n_t=A-q\nu,\\
n_{tss}=\dot e-qe_s,\qquad
n_{tts}=\dot\beta-2q\dot e+q^2e_s,\\
n_{ttt}+3q n_{tts}+3q^2n_{tss}+q^3e_s=0.
\end{gathered}
\tag{18}
\]
In particular the last identity differentiates the H-top equation
by dot, using dot(q)=0. No old-s derivative is silently held fixed.

Treat P,eta,zeta as independent formal variables at this step.
Expanding(17) after(18), its only monomials of weighted degree at
least seven, for weights(3,2,1), are those in the following ledger:
\[
\begin{array}{c|c}
\text{monomial}&\text{complete coefficient}\\ \hline
P^3&0\\
P^2\eta&\dot\beta/2-\beta k\\
P^2\zeta&-\beta l\\
P\eta^2&\dot e/2-ek
\end{array}
\tag{19}
\]
Every omitted monomial has weighted degree at most six. This
includes the full H0-derivative terms, which after evaluation have
degree at most three. The ledger does not remove them from Q.

Since(6),(16) imply
\[
\dot\beta/2-\beta k
=-\frac{A'\beta}{D\nu}=0,
\tag{20}
\]
the P^2*eta term vanishes identically, not only at its top leader.
Therefore all degrees above seven vanish after inserting(9).
The exact remaining top coefficient is
\[
[\zeta^7]Q
=p_3\left\{\frac{\beta}{\nu}p_3
              +(\dot e/2-ek)h_2^2\right\}.
\tag{21}
\]
The genuine Q level is an element of L, so this coefficient is zero.

## 5. Beta zero is impossible without any collision theorem

Suppose beta=0. By(6), B'=A'f' and nu=A' belongs to F*.
The original partial_s is D^{-1} times prime, so
\[
e=\frac{A''}{D},\qquad A''\ne0,\qquad
\dot e=-\frac{A''}{D^2}\ne0.
\tag{22}
\]
Here k=0. Equation(21) is then p3*h2^2*dot(e)/2, which is
nonzero by(9),(22). This contradicts the genuine Q level.
Thus beta=0 has been excluded with no division by beta and no
use of an all-X collision restriction.

Consequently beta is nonzero, and(16) now gives A'=0. As A belongs
to F, it is a complex constant. Equations(6) simplify to
\[
\nu=\frac{B'}D\ne0,\qquad
\beta=-\frac\nu D\ne0,\qquad k=-\frac1D,\qquad
e=\frac{B''D-B'f''}{D^3}.
\tag{23}
\]
Only now has a nonzero-beta branch been selected.

## 6. The exact quadratic B and the varying curvature ratio

Substitute(11),(23) into the full coefficient(21). Since dot(D)=1
and B',B'',f'' belong to F, the result is exactly
\[
[\zeta^7]Q=\frac{p_3h_2^2}{4D^3}(2B''+1).
\tag{24}
\]
All displayed prefactors are nonzero. Therefore B''=-1/2.
Subtracting the known quadratic and using joint constants gives
\[
\boxed{
A\in\mathbb C,\qquad
B=-q^2/4+b_1q+b_0,\qquad b_1,b_0\in\mathbb C .}
\tag{25}
\]
For example B'+q/2 is killed by dot and prime, and is therefore
the complex constant b1. The remaining constant is obtained by
one further subtraction. No rationality assumption on F is used.

The leader relation(11) now reads
\[
p_3=\frac{B'f''h_2^2}{2D^3}.
\tag{26}
\]
Thus f'' is nonzero, as are B' and h2. In particular the result
does not permit the rank-zero boundary to survive as a special
choice of the coefficient function f.

Define the actual coefficient ratio
\[
\kappa=\frac{\beta^2+2e\delta^2}{\beta^2},\qquad
\delta=-\nu .
\]
The denominator is nonzero by Section5; the numerator is nonzero
by407. From(23)--(26),
\[
\boxed{
\kappa=-\frac{2B'f''}{D}\ne0,\qquad
\dot\kappa=\frac{2B'f''}{D^2}
            =-\frac\kappa D\ne0 .}
\tag{27}
\]
This is the proved endpoint here. The derivative remains nonzero
in the exact finite coefficient field, irrespective of whether
f is rational over C(q).

## 7. Scope, evidence and the remaining gap

The complete complex-slope cubic profile must, after the licensed
actual normalization, satisfy(23)--(27). In particular beta=0 is
excluded, A is complex, B is the displayed complex quadratic,
f'' is nonzero, and the curvature ratio is not characteristic-
constant. This is a necessary family, not a realization claim.

A separately proved all-X generation obstruction could conflict
with(27), but no such theorem is assumed or proved in this note.
There is no unconditional exclusion of d=3 here, no extension to
noncomplex lambda or higher degrees, and no conclusion about
arbitrary chart entry, other initial kernels or cancellation.
The original actual return and full scalar remain imposed.

The complete417 and413 sources were freshly read in18837f.
Direct407 was fully reread in e591f3+19e10f, and264 in6d6ef8.
The actual384 transport was read completely in fbc259 during the
preceding414 work; no change to its hypotheses has been made here.
The writing guide was freshly read in22ed91 before authoring.

Fresh unsaved234e63, completed on its original process89533 in
e12a94, rebuilt the full literal determinant coefficient(14),
including all lower polynomial coefficients and their first jets.
Fresh a8fe6e independently reduced it to(15) with zero residual.
Fresh252b79 rebuilt the FULL Q in(17), retained both actual level
derivatives, and checked every entry of(19), the identically zero
degrees above seven after(20), the full coefficient(21), its beta-
zero boundary and its specialization(24). Every residual was zero.
Those controls verify finite identities, not the exact-field
integrations or actual normalization license, which are written above.

No saved checker was executed, imported, compiled or rerun.
No earlier held source or canonical index was edited. This source
is held for independent review and asserts no novelty, unrestricted
cancellation, human-expert verification or formal proof certification.
