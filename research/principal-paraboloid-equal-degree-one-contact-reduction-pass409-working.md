# The remaining degree-one branch has an exact contact-form reduction

Working necessary reduction under every actual264 hypothesis, with
k=s, n_ss nonzero and equal intrinsic degree one. The previously
reviewed exclusions remove constant slopes and three zero branches.
For the surviving branch, the high scalar equations imply the
contact family (24) below. Its parameter q cannot be complex.

This is not an exclusion of that family, a converse realization,
an ambient coordinate normalization, or a cancellation proof.
The coefficient field and its one-variable subfield are retained
exactly and are not assumed rational.

## 1. Complete entry and the already proved exclusions

Retain the complete actual entry and literal rows of
[401](principal-paraboloid-equal-degree-one-delta-zero-necessary-family-pass401-working.md):
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A_0[u],\quad E=\partial_u,
\quad a_0=EX\ne0,\quad\deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the full kernel},\quad
0\ne N=[u^4]\partial_Z|_{A_0},\\
L=\operatorname{Frac}\ker_{A_0}N,\quad
[L:\mathbb C(t,s)]<\infty,\quad
K=L(P)=\mathbb C(y,z,w),\\
O=L[P]=L[y,\sigma,\theta]=L[y,z,w],\quad
P=\sigma,\quad\rho=NP\in L^*,\\
y=\lambda P+r,\quad\theta=\mu P+h,\quad\mu\in L^*,\quad
k=s,\quad n_{ss}\ne0,\\
\det\frac{\partial(Y,Z,W)}{\partial(t,s,P)}
       =-a_0^4/\rho\in L^*.
\end{gathered}
\tag{1}
\]
The global slice, both returns, all genuine potential equations,
their unit conditions and the calibrated scalar remain imposed.
The coefficient partials commute and have joint constants C.

Write
\[
\begin{gathered}
\nu=n_s,\quad e=n_{ss}\ne0,\quad b=n_{ts},\quad c=n_{tt},
\quad\delta=\lambda-\nu,\\
\mathscr D=\partial_t+\mu\partial_s,\quad
\alpha=\mathscr D\lambda,\quad\beta=\mathscr D\nu=b+e\mu,
\quad\mathcal K=\mathscr D\mu+4\lambda.
\end{gathered}
\tag{2}
\]
Here c is a Hessian coefficient; a separate constant C0 will be
used for a coordinate shear. By401 the high necessary equations are
\[
\begin{gathered}
c+2b\mu+e\mu^2+2\lambda^2-4\nu\lambda=0,\\
2\delta\alpha+\beta\mathcal K=0,\qquad
(\beta-\delta\mu_s)\alpha+\delta\mathcal K\lambda_s=0.
\end{gathered}
\tag{3}
\]
These equations themselves have no nonzero-slope assumption.

First, lambda cannot be complex. Otherwise take the ACTUAL384 map
\[
X^*=X+C_0/2,\quad Y^*=Y,\quad Z^*=Z,\quad
W^*=W+C_0Z,\qquad C_0=2\lambda\in\mathbb C.
\tag{4}
\]
Its full actual transport was proved in
[384, Sections 3--4](principal-paraboloid-actual-filtered-symmetry-obstruction-pass384-working.md).
In the degree-one presentation it gives
\[
\begin{gathered}
t^*=t,\quad s^*=s+C_0t^2,\quad P^*=P-C_0t,\\
\lambda^*=\lambda-C_0/2=0,\quad
r^*=r+C_0t\lambda-C_0^2t/4,\\
\mu^*=\mu+2C_0t,\quad h^*=h+C_0t\mu+C_0^2t^2,
\quad \nu^*=\nu-C_0/2.
\end{gathered}
\tag{5}
\]
The previously proved400 condition mu not in C+C*t ensures
mu* is nonzero. Thus the new theta still has degree one, and
[404](principal-paraboloid-equal-degree-one-zero-slope-conductor-exclusion-pass404-working.md)
excludes the transformed zero slope. This uses a complex constant
in an actual automorphism, not an L-valued shear. The original
selected N survives because the omitted-W partial has lower shift.

The remaining reviewed exclusions now give
\[
\boxed{\lambda\notin\mathbb C,\quad
\delta\ne0,\quad\lambda_s\ne0,\quad\mathcal K\ne0.}
\tag{6}
\]
Here403 excludes delta=0;406 excludes lambda_s=0 for noncomplex
lambda;405 excludes Kcal=0 for noncomplex lambda and delta nonzero.
If beta were zero, the first scalar equation in (3) would give
alpha=0, and the second would contradict (6). Consequently
\[
\beta\ne0,\quad\alpha\ne0,\qquad
2\delta^2\lambda_s+\delta\beta\mu_s-\beta^2=0.
\tag{7}
\]
The last equality follows by eliminating alpha and canceling only
the proved nonzero Kcal. This is the licensed surviving branch.

## 2. A separating coefficient basis and its contact equation

Set
\[
\xi=\lambda,\qquad A=\delta/\beta\ne0.
\tag{8}
\]
Because lambda_s is nonzero, (t,xi) is a separating coefficient
basis and L is finite over C(t,xi). Use dot=partial_t at fixed xi
and prime=partial_xi at fixed t. They are exact commuting partials
on L, with joint constants C. They are NOT the characteristic
operator Dscript in (2). In particular
\[
s'=1/\lambda_s\ne0,\qquad
\mathscr D=\dot{\ }+\alpha\,{}',\qquad
\alpha=(\mu-\dot s)/s'.
\tag{9}
\]
Dividing (7) by beta squared and changing derivatives gives
\[
s'=2A^2+A\mu'.
\tag{10}
\]
The first high scalar equation becomes 2A*alpha+Kcal=0.
Use Kcal=dot(mu)+alpha*mu'+4xi and (9),(10) to obtain
\[
\dot s=\mu+A\dot\mu+4A\xi,\qquad
\mathcal K=\frac{2A(\dot\mu+4\xi)}{2A+\mu'}.
\tag{11}
\]
Every denominator is nonzero: (10) implies 2A+mu' nonzero, and
(6),(11) imply dot(mu)+4xi nonzero. In differential form,
\[
\boxed{ds=A\,d\mu+(\mu+4A\xi)\,dt+2A^2\,d\xi.}
\tag{12}
\]
All differentials here are in the coefficient field over C.
Commutation of the partials in (10),(11) gives
\[
A'(\dot\mu+4\xi)=(\dot A-1)(\mu'+4A).
\tag{13}
\]
This compatibility retains the possible zero value of mu'+4A.

## 3. The constant-q boundary is impossible

Define q=A-t. If dot(q)=0, then (13) and the nonzero gate
dot(mu)+4xi imply q'=0, so q is complex. We first exclude that
case without dividing by either derivative of q.

Suppose q=q0 in C and put T=t+q0, so A=T. Then (7) and (3) give
\[
2T^2\lambda_s+T\mu_s=1,\qquad
\mathcal K=-2T\alpha,\qquad\beta=\delta/T.
\tag{14}
\]
The element T is nonzero because t is transcendental over C.
Integrating the first equation in the exact field gives
mu=(s+b0(t))/T-2T*lambda, where b0 initially belongs to
S=ker(partial_s). Direct differentiation then gives
Kcal=(b0)_t/T-2T*alpha. Thus (b0)_t=0, and b0 is complex.

To control the Hessian, differentiate the first equation in (3)
in s, retaining lambda_s. The Hessian symmetries yield
\[
\mathscr D\beta=\mathcal K e-2\mu_s\beta-4\delta\lambda_s.
\tag{15}
\]
For clarity, the third-derivative terms are
c_s+2mu*b_s+mu^2*e_s; they equal Dscript(beta)-e*Dscript(mu).
On the other hand beta=delta/T and Dscript(delta)=alpha-beta
give Dscript(beta)=-Kcal/(2T^2)-2delta/T^2. The first equation
in (14) makes the last two terms of (15) equal -2delta/T^2.
Since Kcal is nonzero,
\[
e=-\frac1{2T^2},\quad
\mu=\frac{s+b_0}{T}-2T\lambda.
\tag{16}
\]
Let S0=s+b0. Integrating nu_s=e gives
nu=-S0/(2T^2)+U, with U in S. The relation beta=delta/T makes
(T*U)_t=0, so T*U=eta in C. Integrate n_s=nu and substitute
in the H equation of (3). The remaining element H0 in S has
(H0)_tt=0. Its affine coefficients are joint constants. Thus
\[
\nu=\frac\eta T-\frac{S_0}{2T^2},\qquad
n=-\frac{S_0^2}{4T^2}+\frac{\eta S_0}{T}+\gamma t+c_0,
\quad\eta,\gamma,c_0\in\mathbb C.
\tag{17}
\]
No restriction on lambda_s was imposed in this derivation.

Use the ACTUAL polynomial normalization (19) of
[406](principal-paraboloid-equal-degree-one-s-constant-slope-exclusion-pass406-working.md),
with tau=-q0 and s0=-b0. That map was explicitly proved to preserve
all actual gates for arbitrary y,theta, before the lambda_s=0
condition was used for its final scalar calculation. It has
t*=T, s*=S0, sigma*=sigma, theta*=theta, y*=y+gamma/2 and
n*=n-gamma*t-c0. Hence the slope lambda, characteristic Kcal
and its nonzero status are unchanged. Dropping stars gives
\[
n=-s^2/(4t^2)+\eta s/t,\qquad
\mu=s/t-2t\lambda,\qquad\mathcal K\ne0.
\tag{18}
\]
This is exactly the conditional actual family excluded by
[408, Section 2](principal-paraboloid-compact-equal-degree-scalar-obstruction-pass408-working.md).
It follows that
\[
\boxed{q\notin\mathbb C,\qquad\dot q\ne0.}
\tag{19}
\]
The second assertion uses the implication preceding (14).
This eliminates a boundary of the contact reduction, not all of it.

## 4. Exact integration on the remaining coefficient surface

Because dot(q) is nonzero, (q,xi) is a separating coefficient
basis. Let partial_q and partial_xi at fixed q denote its exact
commuting partials on L, and put
\[
\mathcal F=\ker_L(\partial_{\xi}|_q),\qquad
\zeta=\mu+4\xi A.
\tag{20}
\]
The transformation from the previous basis gives
\[
\partial_{\xi}|_q={}'-\frac{A'}{\dot A-1}\dot{\ }.
\tag{21}
\]
Apply it to mu+4xi*t. Equation (13) gives
partial_xi|q(mu+4xi*t)=-4q. Consequently zeta belongs to F.
This argument does not divide by A' or mu'+4A.

Define an element of L, without adjoining an antiderivative,
\[
B=A\zeta-2\xi A^2-s.
\tag{22}
\]
Equation (12), with dA=dt+dq and zeta=mu+4xi*A, gives exactly
\[
dB=\zeta\,dq.
\tag{23}
\]
Thus B lies in F and its exact q derivative is zeta. Write B_q
for that derivative. We have proved the necessary family
\[
\boxed{
\begin{gathered}
A=t+q,\qquad\xi=\lambda,\qquad
\mu=B_q-4\xi(t+q),\\
s=-2\xi(t+q)^2+(t+q)B_q-B,\qquad B\in\mathcal F,\\
q\notin\mathbb C,\quad\dot q\ne0,\qquad
[L:\mathbb C(q,\xi)]<\infty.
\end{gathered}}
\tag{24}
\]
Dots in the nonzero gate still refer to fixed xi and old t as in
(9). They are not q derivatives.

The field F contains C(q), is stable under the q derivative, and
is finite over C(q). For an elementary justification, any f in F
has a monic minimal polynomial over C(q,xi). Differentiate that
polynomial at f by partial_xi|q. Since f has zero derivative,
minimality forces every coefficient derivative to vanish. Rational
functions in xi with zero xi derivative belong to C(q), so f is
algebraic over C(q). Also xi is transcendental over F. Every finite
subextension F0 of F/C(q) satisfies
[F0:C(q)]=[F0(xi):C(q,xi)] <= [L:C(q,xi)]. The bounded dimensions
imply finiteness of F itself. This does not imply F=C(q).

In particular t remains an arbitrary retained element of L subject
to all equations. Neither t in F nor a rational formula t=t(q,xi)
is asserted. No parameter in (24) is proved to be an original
polynomial coordinate. The lower genuine potentials, unit conditions,
full scalar and actual returns must still be solved or contradicted.

## 5. Verification and remaining obligations

Root freshly read384 through EOF in ed1ec5,401 in e9cf64/dfef18,
406 in0f34ac and corrected408 through EOF inbe8a72. Root's fresh
unsaved5072b2 independently checked the coordinate high gates,
Kcal denominator, commutation identity, constant-q Kcal formula,
the full H-top substitution with arbitrary lambda(t,s), and the
beta ratio. All displayed residuals were zero. This computation
does not verify the actual-ring transports by itself.

The actual shift (4) uses384's complete source proof, including the
omitted-partial bound and full return. The constant-q normalization
uses406's complete actual map, not its narrower final scalar proof.
408 permits derivatives of lambda in both coefficient directions.
Separate full-source review of this note is required before canonical
acceptance. The finite identity checks support the written proof;
they are not proof-assistant certification or human-expert review.

This reduction leaves the nonconstant-q degree-one family open.
Higher equal degrees, general coupling, other initial ideals,
arbitrary-chart entry and original-ring recognition also remain open.
No saved checker was executed, imported, compiled or rerun. No
unrestricted cancellation result, novelty claim, external contact
or submission is made.
