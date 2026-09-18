# The nonlinear theta-dominant branch is excluded

Working synthesis: in the complete actual principal chart264, assume
the normalized coupling k=s and n_ss is nonzero. Then sigma is
nonconstant, and neither theta nor y has larger intrinsic degree
than sigma. In particular the largest intrinsic degree is an integer
between one and six, attained by sigma.

This excludes one orientation of the nonlinear degree profiles. It
does not recognize the remaining original invariant ring, classify
equal or reversed degrees, or establish that arbitrary cancellation
candidates admit the supplied chart.

## 1. Actual hypotheses and the precise assertion

Retain the complete actual chart of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
including the original global slice and the full initial kernel:
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A_0[u],\qquad
E_{\rm slice}=\partial_u,\qquad A_0=\ker E_{\rm slice},\\
\deg_{E_{\rm slice}}(X,Y,Z,W)=(1,2,2,2),\qquad
I_{\rm initial}=(X^2Z-Y^2),\\
a_0=E_{\rm slice}X\ne0,\qquad
N=[u^4]\partial_Z|_{A_0}\ne0,\qquad
L=\operatorname{Frac}\ker_{A_0}N,\\
[L:\mathbb C(t,s)]<\infty,\qquad
O=L[v]=L[y,\sigma,\theta]=L[y,z,w],\qquad Nv=1,\\
K=\operatorname{Frac}A_0=L(v)=\mathbb C(y,z,w).
\end{gathered}
\tag{1}
\]
The selected partial in (1) is the literal actual Z-partial. The
coefficient partials extend those on C(t,s) and commute. In this
note the coupling is assumed already normalized to k=s, giving
\[
\begin{aligned}
Y&=y+\sigma X+tX^2,\\
Z&=z+(2t\sigma+s)X+t^2X^2,\\
W&=w+\theta X+sX^2,\\
z&=2ty+\sigma^2+\theta+n,\\
w&=\ell-2\sigma y-n_t\sigma-n_s\theta,\\
\det\frac{\partial(Y,Z,W)}{\partial(t,s,v)}&=-a_0^4\in L^*.
\end{aligned}
\tag{2}
\]
The genuine third and fourth potentials and their evaluated unit
gradient/minor ideals remain those of296 and365. They follow from
this actual entry; arbitrary polynomials satisfying just two formal
equations do not replace it.

Assume n_ss is nonzero. With degree taken in the independent
intrinsic v over L, the conclusion is
\[
\boxed{1\le\deg_v\sigma\le6,\qquad
\deg_v\theta\le\deg_v\sigma,\qquad
\deg_v y\le\deg_v\sigma.}
\tag{3}
\]
The degree of zero is understood as minus infinity. Constants among
y or theta are allowed. No finite coefficient field is identified
with a rational field in the assertion.

## 2. Exhaustion of the theta-dominant possibilities

The complete constant-sigma exclusion
[366](principal-paraboloid-nonlinear-first-constant-sigma-exclusion-pass366-working.md)
first gives sigma not in L. Thus its degree is positive.

Suppose, for a contradiction, that theta has strictly larger degree.
The genuine quadric/cubic degree bound and reciprocal derivative gate
[365](principal-paraboloid-nonlinear-intercept-unequal-degree-gate-pass365-working.md),
followed by the geometric exclusions
[367](principal-paraboloid-nonlinear-intercept-geometric-degree-exclusions-pass367-working.md),
leave precisely the necessary pairs
\[
(\deg\sigma,\deg\theta)\in\{(1,2),(2,3),(4,6)\}.
\tag{4}
\]
This is a necessary finite list, not an existence assertion.

For (1,2), the two alternatives in368 are both excluded:371 uses
the calibrated scalar in the finite quadratic-field alternative,
and375 uses the degree-six complex-field-return contradiction in the
other alternative. Neither exclusion assumes a coefficient field
rational merely because it is finite over a rational field.

For (4,6),370 gives the complete surviving whole-line normal form.
The genuine-cubic and full-ideal argument373 excludes it, including
both zero and nonzero centered quadric levels.

For (2,3), the actual complex polynomial normalization369 and the
coefficient gates372 reduce the problem to
\[
n=-s^2/(4t^2)+f,\qquad g=f''/2\ne0,\qquad
E=g'/3+g/t.
\tag{5}
\]
Here E denotes a coefficient, not the slice derivation. The entire
E=0 branch is excluded by374. In the E nonzero branch376 proves
its exact normal form with F=ker_L(partial_s), L=F(s), and
K=F(s,r), where r is an affine intrinsic parameter. The explicit
lower-potential equations377, scalar equations378, and their
composition380 exhaust this branch into
\[
\zeta=tH'/H+2\ne0,\qquad
\zeta=0,\ G_0'=0,\qquad
\zeta=0,\ G_0'\ne0.
\tag{6}
\]
The zero-slope overlap has not been divided out.

The polynomial-return theorem379, using the original slice and the
actual derivations, proves
\[
F[\mathcal B]=F[X,s,r],\qquad F[A_0]=F[s,r],\qquad
J_{t,s,r}(X),a_0,Nr\in F^*.
\tag{7}
\]
These stronger ring and scalar statements are essential inputs to
the final two exclusions, not consequences of field equality alone.

The first two cases in (6) are excluded by
[381](principal-paraboloid-rank-one-polynomial-generation-exclusions-pass381-working.md).
After a polynomial change over F and localization at a proved plane
coordinate z, actual polynomial return forces two polynomials of
degrees (6,8), (4,6), or (3,5) to generate a one-variable polynomial
ring. The characteristic-zero Abhyankar--Moh degree-divisibility
theorem forbids each pair. Its use is justified over the algebraic
closure of F(z), with generation and degrees preserved.

The last case in (6) is excluded by
[382](principal-paraboloid-reciprocal-slope-nonconstant-return-scalar-exclusion-pass382-working.md).
It has H=b/t^2 and G0'=lambda*b^2/t^2, with nonzero complex b,lambda.
The invertible F-polynomial change eta=sigma+s/(2t) preserves the
F-valued scalar up to a factor in F*. Yet its literal determinant
has the nonzero coefficient
\[
[r^7\eta^0]\det\frac{\partial(y,z,w)}{\partial(t,\eta,r)}
=\frac{1152D^6t^{14}}{b^6\lambda(g_0t-3D)^8}\ne0,
\quad D\in\mathbb C^*,\ g_0\in\mathbb C.
\tag{8}
\]
The arbitrary remaining function l in F and the g0=0 boundary are
retained. Thus all alternatives in (6), and every pair in (4),
are impossible. It follows that deg theta is at most deg sigma.

## 3. The remaining maximum degree and what is not proved

The third potential is monic quadratic in its first formal variable U.
Its other terms are at most linear in U, with coefficient of U
of degree at most one in P; its U-independent terms have total
degree at most two in P,V. After evaluation at y,sigma,theta,
if deg y exceeded both deg sigma and deg theta, the y-squared
term would have uniquely greatest degree. It could not evaluate to
the coefficient-field level. Hence deg y is at most deg sigma.
The six-bound from365 then completes (3).

The next unresolved profiles have sigma of maximal intrinsic
degree, with theta of equal or smaller degree. No change of original
coordinates reducing them to the excluded orientation has been
proved here. More general coupling k, other full initial ideals,
and entry of an arbitrary cancellation candidate into any supplied
chart remain outside this conclusion. In particular (3) does not
prove n_ss=0 or A0 is a polynomial ring.

## 4. Evidence and status

This is a composition of the cited working arguments, not a new
recursive verification of every older dependency. Root freshly read
264 in2d20f9;365 in40df39/5b492d;366 in3deca0/9a8095;367 in
9066ba/be9b09;376 in dba4c9;377 in d2d066;378 in b9694b;
379 in62b854;380 in6b33d0;381 in5632fb;382 in2b834d.
The held368--376 hashes were revalidated unchanged in b4bcbb.
The held377--382 hashes were revalidated in b2af40.

Independent audits of377--380 are recorded in the research ledger.
Root independently reconstructed382's leading-form coefficient in
fresh unsaved9daaf0 before reading its final source, with zero
residual. Its initial large determinant attempt was deliberately
interrupted before producing a result; no claim depends on it.
The final saved381 and this synthesis require their separate source
audits before the canonical index can describe this branch as closed.

No saved checker was executed, imported, compiled or rerun. No
unrestricted cancellation, novelty, human-expert review, publication,
or proof-assistant certification is claimed.
