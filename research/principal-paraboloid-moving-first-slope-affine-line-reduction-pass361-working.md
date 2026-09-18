# The entire moving first-slope sector has an affine generic line

Working reduction: under every actual chart264 hypothesis, suppose
k=s, n_ss=0 and n_ts is nonzero. Then sigma has intrinsic degree one,
y and theta are affine polynomials in sigma, and y_sigma is complex.
The initially arbitrary finite-field first potential reduces to the
two explicit coefficient families in353.

This closes the nonlinear intrinsic-curve alternatives within this
sector. It does not recognize the remaining affine cases, establish
arbitrary entry into the sector, or solve cancellation. This note is
a composition of the individually written arguments, not another
numerical experiment or a new assumption that the coefficients are
rational functions.

## 1. Full actual statement

Retain the full setup of
[264](principal-one-affine-paraboloid-chart-pass264-working.md) and
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md):
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,
\quad\deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(X^2Z-Y^2)\text{ is the entire initial kernel},\\
a_0=EX\ne0,\quad N=[u^4]\partial_Z|_A\ne0,
\quad L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,\\
O=L[v]=L[y,\sigma,\theta],\quad Nv=1,\quad
K=L(v)=\mathbb C(y,z,w),\quad J(X)=-a_0^4\in L^*.
\end{gathered}
\tag{1}
\]
Assume the further coefficient gates
\[
k=s,\qquad n_{ss}=0,\qquad n_{ts}\ne0.
\tag{2}
\]
Set F=ker_L partial_s. Exact integration in this finite extension of
C(t), not a rational ansatz, gives n=B(t)s+f(t), with B,f in F and
b=B' nonzero. The literal expansions and first two potentials are
those of349; the coefficient derivatives and full scalar remain the
ones supplied by the actual ring.

The conclusion is
\[
\boxed{O=L[\sigma],\quad\deg_v\sigma=1,\quad
y=j\sigma+k_0,\quad\theta=c\sigma+e,
\quad j\in\mathbb C,\quad k_0,c,e\in L.}
\tag{3}
\]
Constants among y and theta are allowed. Equation(3) concerns the
generic line over L, not a polynomial-coordinate presentation of A.

## 2. Exhausting the nonlinear alternatives

The exact reductions
[349](principal-paraboloid-variable-intercept-slope-quadric-reduction-pass349-working.md)
and [350](principal-paraboloid-moving-first-slope-constant-sigma-exclusion-pass350-working.md)
give sigma nonconstant, birational plane projection, and the intrinsic
degree bound six. Use their affine L-coordinates x,p,q, with
\[
x^2+bpq=d\in L,\quad O=L[x,p,q],\quad
p=\sigma-(\ell_s+B^2)/b.
\tag{4}
\]
The degree list in
[354](principal-paraboloid-moving-slope-intrinsic-degree-patterns-pass354-working.md)
is exhaustive. Its two branches must both be retained:

* If q=0, whole return forces p affine and x a nonzero constant.
* If q is nonzero, its only possible degree triples are those in the
  following table. They are ordered as (deg p,deg x,deg q).

| Degree triple | Exact disposition |
| --- | --- |
| (1,1,1) | Affine p, hence affine sigma; retained for353. |
| (1,2,3) | 353 excludes quadratic x by a full-X specialization to an impossible quadratic/cubic plane pair. |
| (2,2,2) | 358 forces a two-point collision or a simultaneous zero derivative in an actual all-X specialization. |
| (2,3,4) | 356 excludes zero level by the odd module, and nonzero level by residual ruling intersections. |
| (3,4,5) | 355 forces a residual ruling to have intersection both three and at most one with the polynomial-line closure. |
| (2,4,6) | 357 gives a nonzero odd coefficient in the corrected fourth relation. |

The relevant complete proofs are
[353](principal-paraboloid-affine-sigma-moving-slope-frontier-pass353-working.md),
[355](principal-paraboloid-degree-three-sigma-ruling-exclusion-pass355-working.md),
[356](principal-paraboloid-degree-two-three-four-exclusion-pass356-working.md),
[357](principal-paraboloid-quadratic-sigma-quartic-x-exclusion-pass357-working.md)
and [358](principal-paraboloid-equal-quadratic-all-x-collision-exclusion-pass358-working.md).
Their hypotheses agree with(1),(2); none introduces a rationality
assumption on L or a sufficient-condition claim about formal examples.

In particular the ruling arguments use the unit gradient-minor ideal,
not just two equations of low degree. The collision arguments use
L[X,Y,Z,W]=L[X,v] and retain repeated-point boundary cases. The odd-part
argument only divides in the function field for an identity computation,
not to assert a polynomial-ring return.

Thus only deg sigma=1 remains. Applying353 now makes y and theta affine
in sigma and proves j=y_sigma complex. This proves(3). There is no
dependence on recognition of the residual coefficient families.

## 3. The remaining coefficient functions are constrained, not recognized

For precision,353 defines the exact coefficient-field derivation
delta=partial_t+c partial_s and proves
\[
\delta j=0,\quad\delta c=-4j,\quad
\kappa=c+4tj,\quad\rho=s-\kappa t+2jt^2\in G:=\ker_L\delta.
\tag{5}
\]
It derives j in C by differentiating shortest coefficient-field linear
relations. Its result leaves exactly the following necessary families.

If b'=0, all displayed constants except rho are complex, b is nonzero,
and
\[
\begin{aligned}
B&=bt+B_0,\\
f&=2bj t^3+(2B_0j-j^2-b\kappa)t^2+f_1t+f_0,\\
c&=\kappa-4tj,\qquad s=\kappa t-2jt^2+\rho,
\quad\rho\in G\setminus\mathbb C.
\end{aligned}
\tag{6}
\]
If b' is nonzero, there are complex constants tau,B0,c_minus1,rho,f1,f0,
with c_minus1 nonzero, such that, writing T=t-tau and using353's
translated G-constants,
\[
\begin{aligned}
B&=B_0+c_{-1}/T,\\
f&=(-j^2+2B_0j)T^2-c_{-1}\rho/T+f_1T+f_0,\\
c&=\kappa-4Tj,\qquad s=\kappa T-2jT^2+\rho,
\quad\kappa\in G\setminus\mathbb C.
\end{aligned}
\tag{7}
\]
The apparent simplification of B and f is proved inside the exact
field, not imposed in an ansatz. Neither k0, e, ell nor the remaining
lower scalar conditions have been discarded. These displayed families
are not actual examples and not yet endpoints proving A=C^[3].

## 4. Verification and the unresolved full objective

Root completely read every direct source used in this composition.
The saved-source reviews, identity checks, primary geometry references,
and sole-run checker evidence are recorded in the research ledger.
The six methods in352 passed after full source read and a separate
static review; that checker tests349--351 identities and deliberately
failing formal controls, not this entire composition. Any additional
checker is recorded separately only after its actual execution completes.

The polynomial-line statements and the actual-ring return must not be
confused. Over L, a straight generic line still has coefficients in a
field of transcendence degree two over C. Recovering original polynomial
coordinates, or excluding both remaining actual families, is a separate
proof obligation. Other first potentials with n_ss nonzero, general
coupling functions k, other full initial kernels, and arbitrary actual
coordinate entry are outside this reduction.

The unrestricted cancellation goal remains active and unsolved. The
professor has not confirmed the working complex-threefold interpretation.
No public novelty, publication, submission, expert-review, or formal-proof
claim is made.
