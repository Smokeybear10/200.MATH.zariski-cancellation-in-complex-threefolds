# Equal intrinsic degree one is excluded in the supplied actual chart

Working synthesis. Under EVERY actual264 hypothesis, with k=s and
n_ss nonzero, equal intrinsic degree one is impossible. Combined
with400, the remaining intrinsic degree is between two and six.
This is an exclusion inside a specified actual chart, not a proof
that arbitrary cancellation candidates enter that chart.

## 1. Statement and full scope

Use the complete supplied actual entry of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
as restated in401 and409. It includes
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A_0[u],\quad E=\partial_u,
\quad a_0=EX\ne0,\quad\deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ as the full kernel},\quad
0\ne N=[u^4]\partial_Z|_{A_0},\\
L=\operatorname{Frac}\ker_{A_0}N,\quad
[L:\mathbb C(t,s)]<\infty,\quad Nv=1,\\
O=L[v]=L[y,\sigma,\theta]=L[y,z,w],\quad
\operatorname{Frac}A_0=L(v)=\mathbb C(y,z,w),\quad k=s,\\
\det\frac{\partial(Y,Z,W)}{\partial(t,s,v)}=-a_0^4\in L^*,
\qquad n_{ss}\ne0.
\end{gathered}
\tag{1}
\]
All actual genuine potential equations, their evaluated unit ideals,
the literal selected partial, original global slice and both returns
are retained. The coefficient partials commute and have joint
constant field C. The conclusion is the necessary condition
\[
\boxed{
2\le d=\deg_v\sigma=\deg_v\theta\le6,\qquad
\deg_v y\le d,\qquad
\frac{\operatorname{lc}_v\theta}{\operatorname{lc}_v\sigma}
\notin\mathbb C+\mathbb Ct.
}
\tag{2}
\]
The only new improvement over400 is the exclusion of d=1.
Neither existence nor impossibility for d=2,...,6 is claimed.

## 2. Exhaustive proof of the degree-one exclusion

The earlier
[400](principal-paraboloid-equal-degree-leading-ratio-obstruction-pass400-working.md)
gives (2) with lower bound one. Suppose d=1. Set P=sigma, so
O=L[P], and write
\[
y=\lambda P+r,\quad\theta=\mu P+h,\quad
\delta=\lambda-n_s,\quad
\mathscr D=\partial_t+\mu\partial_s,\quad
\beta=\mathscr D(n_s),\quad
\mathcal K=\mathscr D\mu+4\lambda.
\tag{3}
\]
The characteristic Kcal in this section is not the curvature
coefficient used for higher degrees in407.

The following cases are exhaustive and are applied in order.

1. If lambda is complex, the actual384 polynomial map with
   constant C0=2lambda sends lambda to zero. Its new theta slope
   is mu+4lambda*t, nonzero by400. It preserves all actual gates.
   The zero-slope conductor contradiction of
   [404](principal-paraboloid-equal-degree-one-zero-slope-conductor-exclusion-pass404-working.md)
   excludes it. The complete transport and use of the leading-ratio
   gate are recorded in409, Section1.

2. For noncomplex lambda, if delta=0, the actual finite-return and
   conductor contradiction of
   [403](principal-paraboloid-delta-zero-conductor-exclusion-pass403-working.md)
   applies. That argument does not assume normality of a smaller
   coefficient-extended ring.

3. With lambda noncomplex and delta nonzero, lambda_s=0 is excluded
   by [406](principal-paraboloid-equal-degree-one-s-constant-slope-exclusion-pass406-working.md).
   Its actual normalization is followed by a full scalar
   contradiction, not just a necessary high equation.

4. For the remaining lambda_s nonzero branch, Kcal=0 is excluded by
   [405](principal-paraboloid-equal-degree-one-characteristic-zero-exclusion-pass405-working.md).
   Its complete scalar vanishes after the licensed coefficient
   comparisons, including all zero integration constants.

5. The remaining nonzero branch is exactly the input of
   [409](principal-paraboloid-equal-degree-one-contact-reduction-pass409-working.md).
   Its high equations prove beta and Dscript(lambda) nonzero.
   Put A=delta/beta and xi=lambda. In the separating coefficient
   basis(t,xi), put q=A-t. If q is complex,409 derives an actual
   normalized family excluded by
   [408](principal-paraboloid-compact-equal-degree-scalar-obstruction-pass408-working.md).
   If q is not complex,409 proves (q,xi) is separating and derives
   its exact contact family, with no rationality assumption.
   The potential-compatibility contradiction of
   [410](principal-paraboloid-equal-degree-one-contact-compatibility-exclusion-pass410-working.md)
   excludes that family.

No case remains, so d=1 is impossible. All uses of a quotient,
nonzero derivative or coefficient basis occur only after its gate
has been established in the cited proof. In particular the last
case is not a generic-case argument with exceptional branches
silently discarded. This proves (2).

## 3. What the higher-degree frontier actually contains

The independently checked
[407](principal-paraboloid-equal-degree-higher-rank-split-pass407-working.md)
already gives a necessary split for the surviving d>=2. Set
lambda=[v^d]y/[v^d]sigma, mu=lc(theta)/lc(sigma),
u1=y-lambda*sigma, v1=theta-mu*sigma, and
m=max(deg u1,deg v1)<d. Use delta=lambda-n_s,
beta=n_ts+n_ss*mu and the HIGHER-DEGREE curvature
\[
\mathcal C=\beta^2+2n_{ss}\delta^2.
\tag{4}
\]
In particular lambda=0 when deg(y)<d; it is not the ratio of
the two nonzero leading coefficients in that lower-degree case.

If (delta,beta) is not (0,0),407 proves Ccal nonzero. If
R=2delta*u1+beta*v1+j is its complete evaluated linear coefficient,
where j=delta*n_t-ell_t-(ell_s+n_s^2)*mu, then R is nonzero and
\[
\begin{gathered}
r=\deg R,\quad 0\le r<m<d,\quad d+r=2m,\\
(r,m,d)\in\{(0,1,2),(1,2,3),(1,3,5),(2,3,4),
                       (2,4,6),(3,4,5),(4,5,6)\}.
\end{gathered}
\tag{5}
\]
These are necessary possibilities, not realizations. None of the
seven entries is excluded by the degree-one proof above.

If delta=beta=0,407 proves d=2,m=1 and a further necessary
two-pole coefficient family. Its nonzero discriminant parameter
is retained. This exceptional quadratic family has not been
excluded or realized; the lower potentials, full scalar and actual
returns are still imposed. In particular the degree-one
delta-zero conductor theorem403 cannot simply be applied to it.

Thus the next mathematical task is a higher-degree actual-scalar
or return argument, with the quadratic cases the smallest remaining
ones. General coupling k, other full initial kernels, arbitrary
entry and recognition of the original invariant ring remain
separate obligations before cancellation could be claimed.

## 4. Verification status

This synthesis contains no new uncomputed determinant. It combines
the actual transport, conductor and full scalar exclusions with
409's necessary reduction and410's exact potential obstruction.
Separate saved-source review must check this exhaustive dependency
composition before canonical acceptance. The ledger records hashes,
complete source reads and independent symbolic reconstructions.

Root freshly reread404 through EOF in27c69d/dd78bd,405 in01eaa2,
406 in0f34ac,407 in3a5722,408 inbe8a72 and409 in1b1b49
(followed by its Markdown-only correction3e755c). Root's independent
2a599d reconstructed the410 differential forms, the closure
identity, mixed derivative and final contradiction with arbitrary
t(q,xi). All residuals were zero. These finite identities do not
by themselves certify every written actual-ring argument.

No saved checker was executed, imported, compiled or rerun.
There is no human-expert review, formal certification, novelty
claim, public posting or submission. The original conjecture is
still unsolved and Luo's intended field and dimension remain
unconfirmed.
