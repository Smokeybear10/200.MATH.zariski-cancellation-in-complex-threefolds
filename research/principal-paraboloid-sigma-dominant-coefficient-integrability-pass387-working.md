# Exact compatibility forces zero leading slope in the sigma-dominant sector

Working necessary reduction: under the complete actual385 hypotheses,
the leading ratio lambda must vanish. Consequently n_ts=0, n_t is
complex constant, and y has strictly smaller intrinsic degree than
theta. This does not recognize or exclude the remaining profiles.

The key is an exact coefficient-field lemma. When lambda is nonzero,
the retained differential equations force (n_s+lambda)_s=0. This
contradicts the nonzero quadratic-rank coefficient already established
in385. A rational-function conclusion used inside the proof is derived
from a cleared equation and integrality, not assumed for the finite
coefficient field.

## 1. Actual input and the precise differential subsystem

Retain the full actual entry, genuine third and fourth potentials,
whole polynomial-line return, and calibrated scalar of
[385](principal-paraboloid-nonlinear-sigma-dominant-degree-reduction-pass385-working.md).
In particular k=s, L is a finite extension of C(t,s), its exact
coefficient partials commute, and
\[
O=L[v]=L[y,\sigma,\theta],\qquad
\deg_v\sigma>\deg_v\theta\ge1,\qquad e=n_{ss}\ne0.
\tag{1}
\]
The original coordinate ring and selected literal leading derivation
are not replaced by a formal surface. All intrinsic changes remain
over L, not in the original polynomial ring.

Use385's exact coefficients
\[
\nu=n_s,\qquad b=n_{ts}=\nu_t,\qquad
\lambda=\frac{[v^{\deg\sigma}]y}{[v^{\deg\sigma}]\sigma},
\qquad \Delta=\lambda-\nu\ne0.
\tag{2}
\]
The leading potential comparisons and the genuine cubic give
\[
\begin{gathered}
n_{tt}=4\nu\lambda-2\lambda^2,\qquad n_{ttt}=12b\lambda,\\
\Delta\lambda_t=-2b\lambda,\qquad
\lambda_s=\frac{b^2}{2\Delta^2},\qquad
b_t=4e\lambda-4\Delta\lambda_s.
\end{gathered}
\tag{3}
\]
The last equation follows by differentiating the first in s; it is
not an additional arbitrary compatibility assumption. The same385
argument establishes the nonzero quadratic-rank coefficient
\[
\Omega=\frac e2+\frac{b^2}{4\Delta^2}\ne0.
\tag{4}
\]
The proof below first treats(3) independently of(4), then uses(4)
only at the final contradiction.

The joint constants of the exact partials on L are C. One way to
check this is to differentiate the monic minimal polynomial of a
joint constant over C(t,s). Its coefficients are joint constants,
so are complex; the algebraic closedness of C finishes the argument.
Write
\[
\mathcal S=\ker_L\partial_t.
\tag{5}
\]
Commutation makes S stable under partial_s. We do not identify S
with C(s), or L with any rational two-variable field. The element t
is transcendental over S: otherwise differentiating its separable
minimal polynomial over the t-constant field would give a contradiction.

## 2. Nonzero lambda: invariant quotient and exact equations

Assume temporarily that lambda is nonzero. Then b is nonzero.
Indeed b=0 in(3) would imply lambda_t=lambda_s=0, so lambda would
be a nonzero complex constant. The last equality of(3) would then
give 0=4e*lambda, contrary to e nonzero.

Put chi=nu+lambda. If chi=0, then chi_s=0 already. We therefore
treat chi nonzero without discarding its zero branch. Define only
coefficient-field elements
\[
\kappa=\frac{\chi^2}{\lambda},\qquad
\omega=\frac\chi\lambda,\qquad \zeta=\omega-2.
\tag{6}
\]
Here kappa is unrelated to the original coefficient k=s, and omega
is not the intercept w. All divisions in(6) are by known nonzero
field elements. Direct differentiation gives
\[
\kappa_t=0,\qquad
\lambda=\frac\kappa{\omega^2},\qquad
\nu=\frac{\kappa(\omega-1)}{\omega^2},\qquad
\Delta=-\frac{\kappa\zeta}{\omega^2},\qquad
\omega_t=\frac{b\omega}{\Delta}\ne0.
\tag{7}
\]
For the first identity, its numerator is
chi times [2lambda*b+Delta*lambda_t], which vanishes by(3).
In particular kappa belongs to S and zeta is nonzero.

The s equation of(3), followed by compatibility of n_tt with
nu_tt, becomes the exact system
\[
\boxed{
\omega_s=\frac{\omega(2\kappa_s-\omega_t^2)}{4\kappa},
\qquad
(\omega-2)\omega_{tt}+\omega_t^2+2\kappa_s=0.
}
\tag{8}
\]
For explicit verification, substitute(7) in lambda_s=b^2/(2Delta^2)
to obtain the first identity. Then use
nu_tt=partial_s(4nu*lambda-2lambda^2). After replacing omega_s by
the first identity, the difference of its two sides is
\[
-\frac\kappa{\omega^3}
\big[(\omega-2)\omega_{tt}+\omega_t^2+2\kappa_s\big].
\tag{9}
\]
Thus(8) keeps every coefficient derivative, rather than imposing a
chosen rational ansatz for omega.

## 3. The cleared equation forces a polynomial in t

The second equation of(8) says (zeta^2)_{tt}=-4kappa_s.
Consequently exact integration inside L gives
\[
\zeta^2=P(t):=-2\kappa_s t^2+A_1t+A_0,
\qquad A_1,A_0\in\mathcal S.
\tag{10}
\]
For example A1=(zeta^2)_t+4kappa_s*t has zero t derivative;
subtracting its linear term defines A0 with zero t derivative.
There is no assertion that every element of L is polynomial in t.

Define the polynomial over S
\[
D=8\kappa_sP-P_t^2
 =-32\kappa_s^2t^2+16A_1\kappa_st-A_1^2+8A_0\kappa_s.
\tag{11}
\]
Substitute zeta_t=P_t/(2zeta) and zeta_s=P_s/(2zeta) in the first
equation of(8). Clearing the known nonzero denominators gives
\[
8\kappa\zeta P_s=(\zeta+2)D,
\qquad
\zeta(8\kappa P_s-D)=2D.
\tag{12}
\]
All coefficients of P_s still lie in S, by commutation.

The polynomial D is nonzero. Otherwise its leading coefficient in
(11) forces kappa_s=0, and then its constant coefficient forces
A1=0. Equation(10) would make zeta_t=0, contradicting omega_t
nonzero in(7). This argument includes the case when P has degree
less than two; no leading coefficient was divided out.

Equation(12) also makes 8kappa*P_s-D nonzero. Therefore it proves
\[
\zeta=\frac{2D}{8\kappa P_s-D}\in\mathcal S(t).
\tag{13}
\]
This is the specific rationality conclusion needed here, obtained
after retaining the finite-field branch in(10). Since zeta^2=P lies
in S[t], zeta is integral over the integrally closed polynomial ring
S[t]. Its membership in that ring's fraction field now gives
zeta in S[t]. Equation(10) implies deg_t zeta<=1. In fact its degree
is one by(7), but only the consequence omega_tt=0 is needed.

The second equation of(8) thus gives omega_t^2+2kappa_s=0.
Finally chi=kappa/omega and the first equation of(8) yield
\[
\chi_s=\frac{2\kappa_s+\omega_t^2}{4\omega}=0.
\tag{14}
\]
Together with the separately retained chi=0 branch, this proves the
coefficient-field lemma
\[
\boxed{\lambda\ne0\text{ under(3)}\quad\Longrightarrow\quad
(\nu+\lambda)_s=0.}
\tag{15}
\]
No equality S=C(s) or L=S(t) has been used.

## 4. The actual rank condition excludes the nonzero slope

By the s equation of(3), the rank coefficient in(4) is precisely
\[
\Omega=\frac12(e+\lambda_s)=\frac12(\nu+\lambda)_s.
\tag{16}
\]
Equations(4),(15) are incompatible. Hence lambda must be zero.
This conclusion uses the nonzero Omega of the actual strict-degree
argument, not a gradient assertion about a sliced factorization.

When lambda=0, equation(3) instead gives n_tt=0 and b=0. Therefore
both coefficient derivatives of n_t vanish. There is a complex
constant gamma with
\[
\boxed{\lambda=0,\qquad b=0,\qquad
n=\gamma t+f,\quad \gamma\in\mathbb C,\quad
f\in\mathcal S,\quad f_{ss}\ne0.}
\tag{17}
\]
The function f is not asserted to be rational in s.

There is a useful intrinsic refinement. In385's notation d1=0,
Delta=-nu, and its nonzero evaluated remainder is
R=y+gamma/2-j, with j in L. Since that proof gives deg_v R<deg_v theta,
one also has
\[
\deg_v y<\deg_v\theta<\deg_v\sigma,
\tag{18}
\]
where a constant y is allowed. In the pair(1,2) boundary this simply
means y belongs to L. No intrinsic parameter or function f has been
promoted to a coordinate of the original polynomial ring.

## 5. Scope and verification boundary

The rank condition is essential. For example take complex constants
tau,s0,eta,gamma,c0, put T=t-tau, and set
\[
\lambda=\frac{s-s_0}{2T^2},\qquad
n=-\frac{(s-s_0)^2}{4T^2}+\frac{\eta(s-s_0)}T+\gamma t+c_0.
\tag{19}
\]
These rational functions satisfy every equation in(3), with e nonzero
and Delta nonzero, while nu+lambda=eta/T and Omega=0. The example is
only a differential-subsystem control. It is not asserted to satisfy
the whole actual chart, full scalar, or polynomial-ring returns.
It shows why the conclusion is the rank obstruction(16), not an
unconditional inconsistency of the equations in(3).

The final385 source was completely read through EOF in ce41c6 at
SHA000b67a0cf0abddb82bc1ff8dc6f75a6bc92bb45f0ab025a0a64a91f00c38741.
Only its coefficient equations and full-rank conclusion are needed
for(17); its later geometric profile exclusions are not re-proved
or needed for this compatibility argument.

Fresh unsaved02d86c independently reconstructed both transformed
equations(8), the difference(9), the cleared relation and all
coefficients in(11), and every equation of the control(19), with
zero residuals. These finite identities supplement the written
exact-field and integrality arguments.

No saved checker was executed, imported, compiled or rerun by this
author. No earlier source or canonical index was edited. This note
claims neither recognition of the remaining profiles nor unrestricted
cancellation, novelty, human-expert review or formal certification.
