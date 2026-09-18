# Necessary coefficient family for the constant-theta nonzero slope

Working necessary classification: retain the complete actual264 chart
with k=s, n_ss nonzero and theta in the exact coefficient field.
The affine slope from386 is nonzero by396. Its differential subsystem
then forces the specific complex-constant family
\[
\boxed{\lambda=\frac{s-s_0}{2(t-\tau)^2},\qquad
n=-\frac{(s-s_0)^2}{4(t-\tau)^2}
  +\frac{\eta(s-s_0)}{t-\tau}+\gamma t+c_0,\qquad
\tau,s_0,\eta,\gamma,c_0\in\mathbb C.}
\tag{1}
\]
The case eta=0 is included and proved separately. This is a necessary
coefficient-field statement, not an actual realization, original
coordinate normalization, or identification of the full field L.

## 1. Exact actual input and the transferable subsystem

Retain every original-ring and actual-chart hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
the constant-theta reduction
[386](principal-paraboloid-nonlinear-constant-theta-line-gates-pass386-working.md),
and the zero-slope exclusion
[396](principal-paraboloid-constant-theta-zero-slope-exclusion-pass396-working.md).
In particular B=C[X,Y,Z,W]=A0[u] has its original slice derivation
E_slice, exact time degrees(1,2,2,2), full initial kernel(X^2Z-Y^2),
and selected nonzero derivation N=[u^4]partial_Z restricted to A0.
The exact field L=Frac(ker N) is finite over C(t,s). The whole-line
and strong complex-field returns, and the calibrated full determinant,
are all retained:
\[
\begin{gathered}
O=L[v]=L[y,\sigma,\theta]=L[\sigma],\qquad
K=L(v)=\mathbb C(y,z,w),\\
\theta=h\in L,\qquad y=\lambda\sigma+r,\quad r\in L,
\qquad \rho=N\sigma\in L^*,\\
J_{t,s,P}(X)=-a_0^4/\rho\in L^*,\qquad P=\sigma,
\quad a_0=E_{\rm slice}X\ne0.
\end{gathered}
\tag{2}
\]
The exact coefficient partials on L commute. They extend the usual
partials on C(t,s); the independent intrinsic P and actual X are
held fixed in the determinant. The symbol tau in(1) is a complex
constant, not the intrinsic speed denoted rho here.

Set
\[
\nu=n_s,\qquad e=n_{ss}\ne0,\qquad b=n_{ts}=\nu_t,
\qquad \Delta=\lambda-\nu\ne0.
\tag{3}
\]
The nonzero Delta is proved in386 without dividing by lambda;
396 separately establishes lambda nonzero. The leading genuine
potential coefficients and the full literal scalar in386 give
\[
\begin{gathered}
n_{tt}=4\nu\lambda-2\lambda^2,\qquad
n_{ttt}=12b\lambda,\qquad
\Delta\lambda_t=-2b\lambda,\\
\lambda_s=\frac{b^2}{2\Delta^2},\qquad
b_t=4e\lambda-4\Delta\lambda_s.
\end{gathered}
\tag{4}
\]
The last identity is the s derivative of the first, not a further
ansatz. The full actual hypotheses remain imposed even though the
classification below only needs(3),(4) and the exact field structure.

The joint constants of the coefficient partials on L are C. Indeed
differentiate the monic minimal polynomial of a joint constant over
C(t,s). Minimality forces all its coefficients to be joint constants
in C(t,s), hence complex; C is algebraically closed. This also proves
that exact integrations below introduce complex constants when both
derivatives of the integration constant vanish.

The element b is nonzero. If b=0, then(4) gives lambda_t=lambda_s=0,
so lambda would be a nonzero complex constant. The final equality
of(4) would then be 0=4e*lambda, impossible. Consequently
\[
\boxed{b\ne0,\qquad \lambda_t\ne0.}
\tag{5}
\]
These facts are established before any later division by b or
lambda_t. In particular a nonzero constant lambda cannot be a lost
boundary of the classification.

## 2. Only the coefficient-field lemma of387 is transferred

Put chi=nu+lambda. Sections2--3 of
[387](principal-paraboloid-sigma-dominant-coefficient-integrability-pass387-working.md)
prove from precisely(3),(4), with lambda nonzero, that
\[
\boxed{\chi_s=0.}
\tag{6}
\]
This lemma does not use the strict-degree rank coefficient Omega.
No such nonzero-rank assertion is imported into the constant-theta
branch. In particular the contradiction in387 Section4 is not used.

For clarity, the exact-field step behind the transferable lemma is
as follows. The case chi=0 is immediate. Otherwise define
\[
\kappa=\chi^2/\lambda,\qquad \omega=\chi/\lambda,
\qquad \zeta=\omega-2,\qquad
\mathcal S=\ker_L\partial_t.
\tag{7}
\]
The subsystem gives kappa_t=0, zeta nonzero, omega_t nonzero and
\[
\omega_s=\frac{\omega(2\kappa_s-\omega_t^2)}{4\kappa},
\qquad (\omega-2)\omega_{tt}+\omega_t^2+2\kappa_s=0.
\tag{8}
\]
The second equality integrates exactly to zeta^2=P(t), where
P=-2kappa_s*t^2+A1*t+A0 belongs to S[t]. Commutation keeps the
coefficients of P_s in S. The first equality gives the cleared
identity
\[
\zeta(8\kappa P_s-D)=2D,\qquad
D=8\kappa_sP-P_t^2\in\mathcal S[t].
\tag{9}
\]
Here t is transcendental over its exact t-constant field S. If D=0,
its t^2 coefficient forces kappa_s=0 and its constant coefficient
then forces A1=0. That would give zeta_t=0, a contradiction. Thus
(9) proves zeta in S(t). Since zeta^2 is in S[t], integrality and
normality of S[t] imply zeta in S[t], of degree at most one.
Therefore omega_tt=0. Equation(8) now gives(6), as written in387.
This argument never assumes L=S(t) or S=C(s).

## 3. The branch chi nonzero

Assume chi nonzero and retain kappa=chi^2/lambda. Directly from(4),
\[
\kappa_t=0,\qquad
\chi_t=b+\lambda_t=-\frac{b\chi}{\Delta}\ne0.
\tag{10}
\]
Using(6) and the s equation in(4) yields
\[
e=-\lambda_s=-\frac{b^2}{2\Delta^2}
             =-\frac{\chi_t^2}{2\chi^2},\qquad
\frac{\kappa_s}{\kappa^2}
       =\frac e{\chi^2}=-\frac{\chi_t^2}{2\chi^4}.
\tag{11}
\]
Define the actual field element H1=-chi_t/chi^2, which is nonzero.
Since chi_s=0 and the partials commute, H1_s=0. The left side of
the second identity in(11) is t-constant, so (H1^2)_t=0. In
characteristic zero, H1 nonzero implies H1_t=0. Thus
\[
H_1=h_1\in\mathbb C^*.
\tag{12}
\]
No square root has been adjoined to reach this complex constant.

Integrating the reciprocals in both coefficient directions gives
\[
\frac1\chi=h_1t+j_1,\qquad
\frac1\kappa=\frac{h_1^2}{2}s+c_1,
\qquad j_1,c_1\in\mathbb C.
\tag{13}
\]
For the second identity, (1/kappa)_s=h1^2/2 by(11), and
(1/kappa)_t=0 by(10). For the first, both derivatives of
1/chi-h1*t vanish. These observations justify each constant in(13)
inside the retained finite field.

Set
\[
\tau=-j_1/h_1,\quad s_0=-2c_1/h_1^2,\quad
\eta=1/h_1,\quad T=t-\tau.
\tag{14}
\]
All three constants are complex and eta is nonzero in this branch.
Since lambda=chi^2/kappa and nu=chi-lambda, equations(13) give
\[
\lambda=\frac{s-s_0}{2T^2},\qquad
\nu=\frac\eta T-\frac{s-s_0}{2T^2},\qquad
\chi=\frac\eta T.
\tag{15}
\]
The element T is nonzero because t is transcendental over C.
All reciprocals used above were of established nonzero elements.

## 4. The separate branch chi zero

Now suppose chi=0. Then nu=-lambda, Delta=2lambda and
b=-lambda_t. Equation(5) still applies. The subsystem becomes
\[
\lambda_s=\frac{\lambda_t^2}{8\lambda^2},\qquad
n_{tt}=-6\lambda^2.
\tag{16}
\]
Differentiate the second equality in s and use n_s=-lambda to get
\[
\lambda_{tt}=12\lambda\lambda_s
            =\frac{3\lambda_t^2}{2\lambda}.
\tag{17}
\]
Define T=-2lambda/lambda_t in L. This is nonzero by(5). Equations
(16),(17) give
\[
T_t=1,\qquad
\lambda_{ts}=\frac{\lambda_t^3}{8\lambda^3},\qquad
T_s=0.
\tag{18}
\]
For the middle identity, differentiate the first equation of(16)
in t and replace lambda_tt using(17). Substituting it and(16)
into the s derivative of -2lambda/lambda_t proves the last identity.
Hence tau=t-T is a joint constant, so tau belongs to C.

Let A1=lambda*T^2. Its t derivative is zero by the definition of T,
and (16) gives (A1)_s=1/2. Therefore s0=s-2A1 is also a joint
complex constant. We obtain
\[
\lambda=\frac{s-s_0}{2(t-\tau)^2},\qquad
\nu=-\lambda.
\tag{19}
\]
This is exactly(15) with eta=0. The proof has not divided by chi,
eta or a quantity that becomes zero in this branch.

## 5. Integrate n and record the exact nonzero boundaries

In both cases define
\[
n_{\rm base}=-\frac{(s-s_0)^2}{4T^2}
                  +\frac{\eta(s-s_0)}T,
\qquad T=t-\tau.
\tag{20}
\]
Equation(15) or(19) gives (n-n_base)_s=0. Direct differentiation
also gives (n_base)_tt=4nu*lambda-2lambda^2. Hence(4) makes
(n-n_base)_tt=0. The t derivative of n-n_base is killed by both
coefficient partials, so equals a complex constant gamma.
Subtracting gamma*t leaves a joint constant c0. This proves(1).

The family gives the following exact identities:
\[
\begin{gathered}
\nu=\frac\eta T-\frac{s-s_0}{2T^2},\qquad
e=-\frac1{2T^2},\qquad \chi=\frac\eta T,\\
\Delta=\frac{s-s_0-\eta T}{T^2},\qquad
b=\frac{s-s_0-\eta T}{T^3}=\frac\Delta T,\qquad
\lambda_t=-\frac{s-s_0}{T^3}.
\end{gathered}
\tag{21}
\]
The nonvanishing of e, Delta, b, lambda and lambda_t is consistent
with every preceding division: t,s are algebraically independent
over C, and all displayed parameters are complex constants. The
case eta=0 remains allowed; it is exactly chi=0, not a missing limit.

The particular elements n and lambda have now been proved rational
in t,s. This does not prove that L=C(t,s), that every coefficient
is rational, or that any displayed coefficient is an original
polynomial coordinate. No actual change of frame has been made to
set tau,s0,gamma or c0 to zero. The remaining functions ell,h,r,
the original-ring returns and all other scalar coefficients still
impose conditions. Conversely, satisfaction of(4) by(1) alone does
not establish a realization of the full chart.

## 6. Evidence and scope

The complete saved386 and396 sources were read through EOF in
3bcc49 and freshly reread in a4099f/4facab. The complete saved387
was read through EOF in f9e231 and freshly reread in4facab. Only
its Sections2--3 coefficient-field lemma is transferred; its
strict-degree rank contradiction is explicitly outside this proof.

Fresh unsaved982b32 reconstructed kappa_t, chi_t, both quotients
in(11), the chi=0 identities T_t=1 and T_s=0, and every equation
of(4) after substituting(1). All residuals were zero. It also
recovered every identity in(21). These finite identities supplement
the written exact-field, integrality and integration arguments;
they do not certify the complete original-ring problem.

No saved checker was executed, imported, compiled or rerun by this
author. No earlier held proof or canonical index was edited. This
note claims only the necessary family(1), not exclusion, recognition,
unrestricted cancellation, novelty, human-expert verification or
formal certification.
