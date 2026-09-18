# Equal-degree leading slopes satisfy the two high scalar gates

Working necessary result in the complete actual264 chart with k=s.
For equal positive intrinsic degrees of sigma and theta, with y of
no larger degree, the leading slopes satisfy both high scalar
equations previously written in401 for affine intrinsic functions.

The proof cancels the excessive jet-weight terms in the full
literal determinant before discarding any lower-degree functions.
It retains an arbitrary moving leading coefficient and all of its
coefficient derivatives. No degree-one exclusion, original-coordinate
normalization, or classification of the higher-degree cases follows
from this note alone.

## 1. Actual hypotheses and leading data

Retain every actual hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md)
and the complete k=s potentials in
[365](principal-paraboloid-nonlinear-intercept-unequal-degree-gate-pass365-working.md).
In particular,
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A_0[u],\qquad E=\partial_u,\qquad
a_0=EX\ne0,\qquad \deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the full initial kernel},\qquad
0\ne N=[u^4]\partial_Z|_{A_0},\\
L=\operatorname{Frac}\ker_{A_0}N,\quad
[L:\mathbb C(t,s)]<\infty,\quad Nv=1,\quad
O=L[v]=L[y,\sigma,\theta]=L[y,z,w],\\
\operatorname{Frac}A_0=L(v)=\mathbb C(y,z,w),\qquad k=s,\\
J(X)=\det\frac{\partial(Y,Z,W)}{\partial(t,s,v)}
=-a_0^4\in L^* .
\end{gathered}
\tag{1}
\]
The exact coefficient partials on L commute, have joint constants C,
and are extended to fix the original intrinsic parameter v.
All differential rows below hold the actual X fixed.

In the higher equal-degree sector of
[407](principal-paraboloid-equal-degree-higher-rank-split-pass407-working.md),
assume
\[
d=\deg_v\sigma=\deg_v\theta\ge2,\qquad \deg_vy\le d,
\qquad e=n_{ss}\ne0.
\tag{2}
\]
The argument does not need the bound d<=6, but retains all hypotheses
which supplied it. The zero polynomial has degree minus infinity.

Put
\[
\begin{gathered}
\mathfrak a=[v^d]\sigma\in L^*,\qquad
\lambda=\frac{[v^d]y}{\mathfrak a},\qquad
\mu=\frac{[v^d]\theta}{\mathfrak a}\in L^*,\\
y=\lambda\sigma+u_1,\qquad
\theta=\mu\sigma+v_1,\qquad
\deg_vu_1,\deg_vv_1<d.
\end{gathered}
\tag{3}
\]
The slope lambda may be zero. Neither mathfrak-a nor either slope is
assumed constant under the coefficient partials. In particular,
mathfrak-a_t and mathfrak-a_s will not be discarded.

Use the exact coefficient abbreviations
\[
\begin{gathered}
a=n_t,\quad \nu=n_s,\quad b=n_{ts},\quad c=n_{tt},\quad
e=n_{ss},\quad C=\ell_s+\nu^2,\\
\delta=\lambda-\nu,\qquad
\beta=b+e\mu,\qquad
\mathscr D=\partial_t+\mu\partial_s,\\
\alpha=\mathscr D\lambda=\lambda_t+\mu\lambda_s,\qquad
\mathcal K_{\rm char}=\mathscr D\mu+4\lambda.
\end{gathered}
\tag{4}
\]
Here a is not a0 or mathfrak-a. The characteristic K in this note
is not407's quadratic-curvature coefficient.

The leading coefficient of the genuine third relation is
\[
\mathcal H_{\rm top}:=
c+2b\mu+e\mu^2+2\lambda^2-4\nu\lambda=0.
\tag{5}
\]
Indeed the coefficient of v^(2d) in that relation is
mathfrak-a^2 times Htop/2; all its affine terms have smaller degree.
This remains valid when lambda=0.

The conclusion will be the two zero-safe identities
\[
\boxed{
2\delta\alpha+\beta\mathcal K_{\rm char}=0,\qquad
(\beta-\delta\mu_s)\alpha+
               \delta\mathcal K_{\rm char}\lambda_s=0.
}
\tag{6}
\]
No factor in either equation will be divided out.

## 2. Full literal rows before taking intrinsic leading terms

The complete first two potentials and actual map are
\[
\begin{aligned}
z&=2ty+\sigma^2+\theta+n,&
w&=\ell-2\sigma y-a\sigma-\nu\theta,\\
Y&=y+\sigma X+tX^2,&
Z&=z+(2t\sigma+s)X+t^2X^2,\\
W&=w+\theta X+sX^2.
\end{aligned}
\tag{7}
\]
For the differential calculation write \(p=\sigma\) and \(z_1=\theta\).
The notation z1 is not the intercept z. Define the coefficient-
polynomial expressions
\[
\begin{aligned}
L_0&=2\nu p-2y-a,\\
T_0&=-cp-bz_1+2\nu y+\nu a+\ell_t,\\
S_0&=-bp-ez_1+C.
\end{aligned}
\tag{8}
\]
These definitions include all lower coefficient terms.

First replace the second differential row by dZ-2t*dY. Then
replace the third row by dW+2p*dY+nu*(dZ-2t*dY).
These are determinant-preserving row operations. Their multipliers
are not differentiated. Set
\[
\begin{aligned}
B_{\rm small}&=dz_1+(2y+a)\,dt+\nu\,ds,\\
B_0&=2p\,dp+B_{\rm small},&
B_1&=2p\,dt+ds,\\
C_0&=L_0\,dp+T_0\,dt+S_0\,ds,&
C_1&=B_0+L_0\,dt.
\end{aligned}
\tag{9}
\]
The complete resulting rows are exactly
\[
\boxed{
\mathcal A_X=dy+X\,dp+X^2dt,\qquad
\mathcal B_X=B_0+XB_1,\qquad
\mathcal C_X=C_0+XC_1+X^2B_1.
}
\tag{10}
\]
For example C1=2p*dp+dz1+2nu*p*dt+nu*ds, including every
coefficient derivative that arose from the second potential.
Nothing in (8)--(10) assumes affine intrinsic functions.

For any three differential rows A,B,C, write [A,B,C] for their
determinant in the ordered basis dt,ds,dv. If
J(X)=J0+X*J1+..., equation (10) gives
\[
\begin{aligned}
J_0&=[dy,B_0,C_0],\\
J_1&=[dp,B_0,C_0]+[dy,B_1,C_0]+[dy,B_0,C_1].
\end{aligned}
\tag{11}
\]
The following cancellations are exact identities in the full
functions and all their first derivatives.

## 3. Excessive weights cancel before any truncation

From (9), the term containing
\(2p\,dp\wedge L_0\,dp\) is zero. Thus the full constant coefficient
has the exact expression
\[
\boxed{
J_0=2p[dy,dp,T_0dt+S_0ds]
       +[dy,B_{\rm small},L_0dp+T_0dt+S_0ds].
}
\tag{12}
\]
This cancellation removes the only possible weight-five terms.

For J1, the first determinant in (11) loses both repeated-dp
contributions. In its other two determinants, use C1=B0+L0*dt.
The contributions
\(2pL_0\,dy\wedge dt\wedge dp\) and
\(2pL_0\,dy\wedge dp\wedge dt\) cancel. The exact result is
\[
\boxed{
\begin{aligned}
J_1={}&[dp,B_{\rm small},T_0dt+S_0ds]\\
 &+(2pS_0-T_0-\nu L_0)[dy,dt,ds]\\
 &+L_0[dy,ds,dp]+L_0[dy,dz_1,dt].
\end{aligned}}
\tag{13}
\]
In particular this cancellation occurs before substituting
y=lambda*p+u1 or z1=mu*p+v1. It is not a cancellation justified
only after evaluating leading monomials.

Here is the precise filtration being used. Give weight one to
each of y,p,z1 and each of its first derivatives with respect
to t,s or v. Give weight zero to all coefficient-field elements,
including their derivatives, and to dt,ds. Equivalently, in
the differential notation dy,dp,dz1 each has weight one.
The expressions L0,T0,S0 and Bsmall have weight at most one.

Every summand of (12) has weight at most four. Every summand of
(13) has weight at most three. Thus all higher-weight terms of
J0 and J1 have canceled identically. The constant a terms and
all ell derivatives in (8),(9) respect these same bounds; they
were never omitted in establishing them.

To translate weight to intrinsic degree, coefficient derivatives
of an element of L[v] do not increase its degree in v. A v
derivative lowers a nonconstant polynomial's degree by one.
Every nonzero determinant term in the coefficient of dt*ds*dv
has exactly one v-derivative contribution. The rows dt,ds
themselves cannot contribute to that column. Therefore a
weight-w monomial appearing here has intrinsic degree at most
wd-1. Vanishing derivatives of constants cause no exception.
Consequently
\[
\deg_v J_0\le4d-1,\qquad
\deg_v J_1\le3d-1.
\tag{14}
\]

More is true for their top coefficients. In either expression,
replacing any one occurrence of y,p,z1 or a derivative thereof
by its lower intrinsic part reduces the degree bound by at least
one. For a coefficient derivative the lower degree is at most
d-1; for a v derivative it is at most d-2, or that derivative
is zero. Hence
\[
[v^{4d-1}]J_0,\quad [v^{3d-1}]J_1
\]
depend only on the leading polynomials
\[
y_{\rm lead}=\lambda\mathfrak a v^d,\qquad
p_{\rm lead}=\mathfrak a v^d,\qquad
(z_1)_{\rm lead}=\mu\mathfrak a v^d.
\tag{15}
\]
This also discards the lower part of p itself, not just u1,v1.
All coefficient derivatives of the leading data in (15) are retained.

## 4. The leading substitution and its exact chain factor

For coefficient extraction only, introduce an independent formal
P and substitute y=lambda*P, p=P, z1=mu*P in the full literal
rows (7). Denote the resulting determinant in t,s,P by
Jaff(X,P). This is an algebraic auxiliary expression, not an
actual replacement of the original frame.

Now substitute \(P=\mathfrak a v^d\). The chain-rule determinant is
\[
\det\frac{\partial(t,s,P)}{\partial(t,s,v)}
=P_v=d\mathfrak a v^{d-1}.
\tag{16}
\]
In particular the entries P_t=mathfrak-a_t*v^d and
P_s=mathfrak-a_s*v^d remain present in the chain-rule matrix.
Its triangular form, not an assumption that they vanish,
makes the determinant equal to Pv. This is a polynomial identity;
no inverse to Pv or coordinate assertion about P is required.

For completeness, expanding the full affine auxiliary rows gives
\[
\begin{aligned}
[P^3]J_{\rm aff}(0,P)
={}&2\{(\beta-\delta\mu_s)\alpha+
                     \delta\mathcal K_{\rm char}\lambda_s\}
                  -2\lambda_s\mathcal H_{\rm top},\\
[XP^2]J_{\rm aff}(X,P)
={}&-\{2\delta\alpha+\beta\mathcal K_{\rm char}\}
                  +\mu_s\mathcal H_{\rm top}.
\end{aligned}
\tag{17}
\]
These are the untruncated expressions before imposing Htop=0.
They agree with the zero-safe affine computation in
[401, Section3](principal-paraboloid-equal-degree-one-delta-zero-necessary-family-pass401-working.md).
They can also be obtained directly from (12),(13) with
\(dy=P\,d\lambda+\lambda\,dP\) and
\(dz_1=P\,d\mu+\mu\,dP\).

Combining (14)--(17), and then applying the genuine identity (5),
proves the exact original leading-coefficient formulas
\[
\boxed{
\begin{aligned}
[v^{4d-1}]J_0
 &=2d\mathfrak a^4
    \{(\beta-\delta\mu_s)\alpha+
                       \delta\mathcal K_{\rm char}\lambda_s\},\\
[v^{3d-1}]J_1
 &=-d\mathfrak a^3
    \{2\delta\alpha+\beta\mathcal K_{\rm char}\}.
\end{aligned}}
\tag{18}
\]
The powers of mathfrak-a include the single chain factor in (16).
No derivatives of its value have been suppressed.

The actual scalar (1) has J0=-a0^4 in L* and J1=0.
The exponents in (18) are positive. Since characteristic is zero
and mathfrak-a is nonzero, (18) proves both equations in (6).
This argument permits lambda=0, delta=0, beta=0 and
Kchar=0 individually; it concludes the equations, not that any
of those factors is nonzero.

## 5. Scope and the remaining branch obligations

The same two high scalar gates therefore hold for the leading
slopes of every equal-degree case (2), not only for affine
intrinsic functions. The first gate is consistent with
differentiating Htop and applying the highest fourth-potential
coefficient, but the calculation above independently obtains
both from the literal full scalar.

Nothing here transfers the degree-one exclusions404,405,406
or408 to a higher-degree frame. Their proofs use additional
degree-one row or ring information. Nor has a degree-one
constant-q exclusion been made available automatically.

A subsequent coefficient argument may use (6) on a separately
licensed nonzero branch, but must justify each division and
each branch reduction there. In particular this note does not
show that a higher-degree case enters409's nonconstant contact
family. The generality of these two gates is not a proof that
all equal degrees are excluded.

The coefficient-field and formal substitutions in this proof
do not alter any original coordinate. The global slice,
selected N, both actual returns, all lower potential equations
and the complete calibrated scalar remain hypotheses. No
coefficient-field equality, original-ring recognition,
arbitrary-chart entry, or unrestricted cancellation statement
has been added.

## 6. Independent finite controls and proof boundary

The complete direct sources264,365 and296 were freshly read
through EOF in4abd4f,142531 and08e97c. The complete401 high-system
source and400 were reread across fe4a37,a78e8e and87a5b1.
The complete407 input was read in66989e and its hash revalidated
in1ff859. Those are scoped direct-input reads, not a recursive
verification of every historical dependency.

Fresh unsaved94187c reconstructed the exact wedge cancellations
(12),(13) with arbitrary full-function and derivative symbols.
Both residuals were zero before any leading substitution.
Fresh unsaved55fcba reconstructed (17), including exactly the
two Htop residual terms displayed there.

Fresh unsaved5ec0fe performed independent degree-two and
degree-three controls. It retained an arbitrary leading
coefficient with independent t,s jets, arbitrary lower
coefficients in all three intrinsic functions, and all of their
first coefficient jets. In both degrees, the two residuals
against (18) were zero. Every J0 coefficient of degree 4d
through 5d-1, and every J1 coefficient of degree 3d through
5d-1, was also identically zero. The controls used the full
determinants from (10),(11), not only the reduced expressions.

These finite controls do not prove the all-degree assertion;
the exact cancellations and filtration argument in Sections2--4
do. No saved checker was executed, imported, compiled or rerun.
No earlier held source or canonical index was edited. This note
is held for independent review and makes no novelty, human-expert
verification or formal-certification claim.

