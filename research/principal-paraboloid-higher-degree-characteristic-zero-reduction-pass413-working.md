# Every remaining higher-degree leading direction has zero characteristic coefficient

Working necessary reduction under the complete actual264 hypotheses,
with k=s and n_ss nonzero. For every remaining equal intrinsic
degree d>=2, the leading slopes satisfy

    (partial_t+mu*partial_s)(lambda)=0,
    (partial_t+mu*partial_s)(mu)=-4lambda.

The proof uses412's all-degree high gates and407's nonexceptional
curvature obstruction. It does not transfer the degree-one scalar
exclusions to larger degrees. The higher-degree families are narrowed,
not excluded or realized.

## 1. Exact hypotheses, two different coefficients and the claim

Retain EVERY supplied actual hypothesis in
[412, Section1](principal-paraboloid-equal-degree-leading-scalar-gates-pass412-working.md),
including the original global slice, full initial kernel,
literal selected partial, both actual returns, all genuine levels,
their unit conditions and calibrated scalar. Let
\[
\begin{gathered}
2\le d=\deg_v\sigma=\deg_v\theta\le6,\qquad\deg_v y\le d,\\
\lambda=[v^d]y/[v^d]\sigma,\qquad
\mu=[v^d]\theta/[v^d]\sigma\in L^*,\\
\nu=n_s,\quad e=n_{ss}\ne0,\quad b=n_{ts},\quad c=n_{tt},
\quad\delta=\lambda-\nu,\\
\mathscr D=\partial_t+\mu\partial_s,\quad
\alpha=\mathscr D\lambda,\quad\beta=\mathscr D\nu=b+e\mu,\\
\mathcal K=\mathscr D\mu+4\lambda,\qquad
\mathcal C=\beta^2+2e\delta^2.
\end{gathered}
\tag{1}
\]
Thus Kcal is the characteristic coefficient, whereas Ccal is the
quadratic curvature. They are not the same element. Lambda can be
zero, in particular when deg(y)<d.

By412, the exact leading equations are
\[
\begin{gathered}
c+2b\mu+e\mu^2+2\lambda^2-4\nu\lambda=0,\\
2\delta\alpha+\beta\mathcal K=0,\qquad
(\beta-\delta\mu_s)\alpha+\delta\mathcal K\lambda_s=0.
\end{gathered}
\tag{2}
\]
All coefficient partials are exact commuting extensions on the
finite field L/C(t,s), with joint constants C. By
[407, Section3](principal-paraboloid-equal-degree-higher-rank-split-pass407-working.md),
\[
(\delta,\beta)\ne(0,0)\quad\Longrightarrow\quad\mathcal C\ne0.
\tag{3}
\]
This rank statement uses the actual whole polynomial return and
full genuine-gradient condition. Those hypotheses are retained.

We prove
\[
\boxed{\mathcal K=0,\qquad\alpha=0.}
\tag{4}
\]

## 2. Delta zero and complex constant slopes are covered first

If delta=0, then lambda=nu and alpha=beta. The second high equation
in (2) gives beta squared zero, hence beta=0. Thus mu=-b/e, and
the first equation gives c=2nu^2+b^2/e. In the separating basis
(t,xi=nu), the exact partial at fixed xi is Dscript. The Legendre
element f=n-xi*s satisfies dot f=n_t, f'=-s and
ddot f=2xi^2. Exact integration defines U,V in ker(dot) with
f=xi^2*t^2+U*t+V. Consequently
s=-2xi*t^2-U'*t-V', mu=-4xi*t-U', and dot mu=-4xi.
This proves Kcal=0. This is precisely407's degree-independent
Legendre calculation, not the degree-one conductor theorem403.

Next suppose lambda is complex. Then alpha=0, so the first high
equation gives beta*Kcal=0. If beta is nonzero, Kcal=0. If beta=0,
use the same separating basis(t,xi=nu), available because e!=0.
Now c-b^2/e=4lambda*xi-2lambda^2. The exact Legendre element
satisfies ddot f=4lambda*xi-2lambda^2, so
\[
\begin{gathered}
f=(2\lambda\xi-\lambda^2)t^2+Ut+V,\qquad U,V\in\ker\dot{\ },\\
s=-2\lambda t^2-U't-V',\qquad
\mu=-4\lambda t-U',\qquad \dot\mu=-4\lambda.
\end{gathered}
\tag{5}
\]
Again Kcal=0, including lambda=0. Each integration is a definition
by subtracting a known primitive inside L. It does not identify
L with a rational field. No actual coordinate change is needed.

For the rest of the proof assume for contradiction
\[
\mathcal K\ne0,\qquad\delta\ne0,\qquad\lambda\notin\mathbb C.
\tag{6}
\]
The preceding paragraphs license the last two conditions.

## 3. An s-constant noncomplex slope would force zero curvature

Suppose lambda_s=0. Then lambda_t is nonzero, and (2) gives
\[
v_1:=\mu_s\ne0,\quad \beta=\delta v_1,\qquad
\lambda_t=-v_1\mathcal K/2.
\tag{7}
\]
Here v1 is a coefficient function, not the intrinsic parameter
or407's lower theta term. This section reproduces the necessary
coefficient calculation of406 without its degree-one scalar part.

Differentiate the last equation in s and the H-top equation in s.
Since lambda_s=0, the resulting compatibilities are
\[
\begin{gathered}
\mathscr Dv_1+v_1^2=-\mathcal K(v_1)_s/v_1,\\
\mathscr D\beta=\mathcal K e-2v_1\beta,\\
e=-\delta(v_1)_s/v_1-v_1^2/2,
\qquad f:=\delta/v_1-\mu/2\in S:=\ker_L\partial_s.
\end{gathered}
\tag{8}
\]
For the last line, differentiate beta=delta*v1 by Dscript and
use Dscript(delta)=lambda_t-beta, then compare the first two lines.
Its formula for e makes the s derivative of f zero.

Put U=mu+2f, so U_s=v1 and delta=v1*U/2. Then U is nonzero
and transcendental over S: a separable algebraic relation over S
would force U_s=0. The remaining compatibility in (8) gives
\[
U(v_1)_s=2v_1^2+C_1v_1^3,\qquad
C_1=(2\lambda-f_t)/\lambda_t\in S.
\tag{9}
\]
For verification, differentiate delta=v1*U/2 using
Dscript(U)=Kcal-4lambda+2f_t and (7); substitution of the first
line of (8) gives (9). Its exact integral implies
\[
s=p_0U+p_1/U+p_2,\qquad
v_1^{-1}=p_0-p_1/U^2,\quad p_i\in S,\quad p_0=-C_1/2.
\tag{10}
\]
Indeed partial_s(U^2/v1+C1*U^2/2)=0. Define p1 as the negative
of this constant. The derivative of p0*U+p1/U is then one,
and p2 is defined by subtraction from s.

In the separating basis(t,U), elements of S keep their old
t derivatives. With mu=U-2f, equation (7) becomes
\[
\begin{aligned}
U-2f-[(p_0)_tU+(p_1)_t/U+(p_2)_t]
={}&-2\lambda_t(p_0-p_1/U^2)^2\\
&-(4\lambda-2f_t)(p_0-p_1/U^2).
\end{aligned}
\tag{11}
\]
To obtain this, use Dscript(U)=v1*(mu-s_t|U), then
Kcal=Dscript(U)+4lambda-2f_t. Compare Laurent coefficients in
the transcendental U. The U^{-4} coefficient gives
-2lambda_t*p1^2=0, so p1=0. Thus v1^{-1}=p0 belongs to S and
(v1)_s=0. Equation (8) then gives e=-v1^2/2, hence
\[
\mathcal C=\delta^2v_1^2+2e\delta^2=0.
\tag{12}
\]
Since delta is nonzero, this contradicts (3). This argument did
not use a degree-one determinant, the actual normalization in406,
or the compact lemma408.

## 4. The remaining nonzero branch has a coefficient contact form

We may now impose lambda_s nonzero in addition to (6). The two
high gates force beta and alpha nonzero. Set
\[
\xi=\lambda,\qquad A=\delta/\beta\ne0.
\tag{13}
\]
Use the exact(t,xi) coefficient partials, dot at fixed xi and
prime at fixed t. The algebraic elimination in (2) gives
\[
\begin{gathered}
s'=A(2A+\mu')\ne0,\qquad
\dot s=\mu+A(\dot\mu+4\xi),\\
\mathcal K=\frac{2A(\dot\mu+4\xi)}{2A+\mu'},\qquad
A'(\dot\mu+4\xi)=(\dot A-1)(\mu'+4A).
\end{gathered}
\tag{14}
\]
These are409's coefficient calculations, requiring only (2),
not affine intrinsic functions. In particular dot(mu)+4xi and
2A+mu' are nonzero by the displayed equations.

Put q=A-t. If dot(q)=0, the last equation in (14) forces q'=0,
so q is complex. If q is not complex, dot(q) is nonzero and
(q,xi) is a separating basis. Define
\[
B=A(\mu+4\xi A)-2\xi A^2-s.
\]
Equations (14) give dB=(mu+4xi*A)dq. Hence in the exact new
coordinate partials, B_xi=0 and
\[
\mu=B_q-4\xi A,\qquad
s=-2\xi A^2+AB_q-B,\qquad A=t+q.
\tag{15}
\]
No coefficient field is identified with a rational field.

For clarity, here is the degree-independent incompatibility used
at this point. Put Wcal=Dscript(n),
J=Wcal+2xi^2*t-xi*B_q+4xi^2*q, and
M=n-xi*s-xi^2*t^2-J*t. The original H-top and
beta=(xi-n_s)/A, together with (15), give
\[
\begin{gathered}
J_q=0,\\
M_q=-\tfrac12(B_{qq}-4\xi)(B_q-4\xi q+J_\xi),\qquad
M_\xi=-2\xi q^2+qJ_\xi+B.
\end{gathered}
\tag{16}
\]
The complete differential derivation is410, Sections2--3. It uses
only these coefficient equations and the existing functions n,J,M;
no scalar row, intrinsic degree, r,h,ell or original-ring conclusion
is used there. All derivatives of the arbitrary retained t cancel.
Thus this is an extraction of that coefficient lemma, not an
application of the entire degree-one theorem to a different chart.

Commutation applied to (16) gives
\[
\mathcal E=B_q+J_\xi+2qB_{qq}-12\xi q
 -B_{qq}J_{\xi\xi}/2+2\xi J_{\xi\xi}=0.
\tag{17}
\]
Its mixed derivative forces B_qqq*J_xixixi=-24. Differentiating
in q gives B_qqqq=0; then E_qq=5B_qqq=0, a contradiction.
This proves q must be complex. It does NOT use409's separate
degree-one exclusion of constant q, which is not available here.

## 5. Constant q contradicts the higher-degree curvature instead

Now q=q0 is complex and A=T=t+q0. The same high gates give
\[
\beta=\delta/T,\quad\alpha=-\mathcal K/(2T),\qquad
2T^2\lambda_s+T\mu_s=1.
\tag{18}
\]
Directly differentiating beta=delta/T by Dscript gives
Dscript(beta)=-Kcal/(2T^2)-2delta/T^2. On the other hand, the
s derivative of the original H-top equation, this time retaining
lambda_s, gives
\[
\mathscr D\beta=\mathcal K e-2\mu_s\beta-4\delta\lambda_s
              =\mathcal K e-2\delta/T^2.
\tag{19}
\]
Subtract the two identities. Kcal is nonzero by (6), so
e=-1/(2T^2). Therefore
\[
\mathcal C=\delta^2/T^2+2e\delta^2=0,
\tag{20}
\]
again contradicting (3). No integration of n, normalization of
original coordinates or use of408 occurs in this step.

Every case with Kcal nonzero has now been excluded. Hence Kcal=0.
If delta is nonzero, the first high equation in (2) gives alpha=0.
If delta=0, Section2 already proved alpha=beta=0. This proves (4).

## 6. A useful coefficient family, and what it does not prove

If lambda is noncomplex, (4) forces lambda_s nonzero. Then with
xi=lambda the exact coordinate partial in(t,xi) is Dscript.
Write F=ker(Dscript) and primes for the xi partial. Exact integration
of Dscript(mu)=-4xi, Dscript(s)=mu and
Dscript squared(n)=-2xi^2 yields
\[
\boxed{
\mu=\zeta-4\xi t,\qquad
s=-2\xi t^2+\zeta t+S_0,\qquad
n=-\xi^2t^2+Ut+V,\qquad
\zeta,S_0,U,V\in F.
}
\tag{21}
\]
This is the coefficient family from405, but its degree-one
full-scalar contradiction is NOT available for the higher-degree
intrinsic functions. The lower intrinsic remainders are not
coefficient constants here. They remain essential unknowns.

For complex lambda, one may instead use the already licensed
actual384 constant shear to put that leading slope at zero;
400 ensures the leading theta slope does not cancel. This optional
normalization does not permit the degree-one conductor exclusion404.
In the zero-slope frame, (4) only says Dscript(mu)=0.

All seven nonexceptional profiles from407 and its exceptional
quadratic family remain subject to (4); none is excluded by this
note. The full scalar, lower genuine potentials, unit conditions
and actual returns remain to be exploited. General coupling,
other initial ideals, arbitrary entry and original-ring recognition
are still unresolved.

## 7. Verification and limits

Root read412 through EOF inf688c6,407 in3a5722,406 in0f34ac,
409 in1b1b49 with correction3e755c, and410 in84cd99. Root's
fresh d8ad6b reconstructed the two raw affine Htop residuals
and independent degree-two/three controls retaining nonzero
leading-coefficient derivatives and lower jets. The all-degree
argument remains412's exact weight proof, not those controls.

Before this source was saved, Jet independently checked the entire
case argument, including the complex-lambda Legendre calculation,
the necessary Laurent argument of Section3, the precise inputs
to the coefficient lemma in Section4, and the replacement of
degree-one408 by higher-degree407 in Section5. Its fresh a21062
also independently verified412's wedge identities and raw Htop
residuals. Full saved-source review of this note is still required.

No saved checker was executed, imported, compiled or rerun. This
is a necessary higher-degree reduction, not an exclusion of all
equal degrees, a cancellation proof, a novelty claim, human-expert
review or formal certification.
