# Recognition for every complex-constant coupling in the supplied chart

Working scoped synthesis, conditional on the explicitly retained
recognition dependencies: under EVERY actual hypothesis of264,
\[
\boxed{k_s\in\mathbb C\quad\Longrightarrow\quad
A\simeq\mathbb C^{[3]}.}
\tag{1}
\]
In the nonzero-constant case there is the stronger necessary conclusion
\[
\boxed{k_s\in\mathbb C^*\quad\Longrightarrow\quad
n_{ss}=n_{ts}=0,\qquad n_s\in\mathbb C.}
\tag{2}
\]
There is NO longitudinal derivative restriction on k and no added
restriction on either potential n or ell. The new part is the
nonzero-constant case with arbitrary longitudinal dependence.
The zero-coupling part was already covered by268 and294; its inclusion
in(1) is a retained composition, not a new zero-coupling result.

This is not a reduction of arbitrary cancellation candidates to this
chart. The general cancellation problem remains unsolved.

## 1. Exact actual scope

Retain the entire original-ring setup of
[264](principal-one-affine-paraboloid-chart-pass264-working.md):
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad
\deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\quad\hbox{is the ENTIRE weighted initial kernel},\\
a_0=EX\ne0,\qquad X=a_0u+x_0,\quad x_0\in A,\\
N=[u^4]\partial_Z|_A\ne0,\quad
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,\\
Nv=1,\quad Na_0=Nt=Ns=0,\qquad O=L[A]=L[v]=L[y,z,w],\\
\operatorname{Frac}A=L(v)=\mathbb C(y,z,w),\qquad
J_{t,s,v}(X)=-a_0^4\in L^*.
\end{gathered}
\tag{3}
\]
Every localization, selected-partial, genuine-potential and original
global-slice condition remains required, not just the displayed
consequences. The original slice u is not replaced by X/a0.

The literal rows are
\[
Y=y+\sigma X+tX^2,\qquad
Z=z+(2t\sigma+k)X+t^2X^2,\qquad
W=w+\theta X+sX^2.
\tag{4}
\]
Coefficient partials on L commute and have joint constants C.
The field F=ker_L(partial_s) is finite over C(t), not presumed
rational. When m=k_s is nonzero,264 additionally proves
O=L[y,sigma,theta]. This additional return is NOT asserted in
the zero-coupling branch without its separate proof.

## 2. Normalize only a nonzero complex constant

Suppose m=k_s belongs to C*. Use the actual complex polynomial map
\[
X_*=X,\quad Y_*=Y,\quad Z_*=Z,\quad W_*=mW,
\qquad t_*=t,\quad s_*=ms.
\tag{5}
\]
Its inverse divides W* by the nonzero complex constant m. It fixes
the full initial relation, preserves all four exact time degrees,
and leaves the literal Z-partial, N, L, original global slice and
kernel unchanged. The intercepts and slopes obey
\[
y_*=y,\quad z_*=z,\quad w_*=mw,\qquad
\sigma_*=\sigma,\quad\theta_*=m\theta,
\quad k_*=k,\quad n_*=n,\quad\ell_*=\ell.
\tag{6}
\]
Both polynomial-ring and fraction-field returns survive. The actual
row determinant contributes m and the parameter change contributes
1/m, leaving the complete scalar exactly -a0^4.

For completeness, in the first potential the term m*theta becomes
theta*. In the second, m*w becomes w* and n_s*theta becomes
(n_s/m)*theta*. The mixed and second s-derivatives of k are zero
because m is complex constant. Hence neither potential transport
assumes n_ss=0. The exact derivatives give
\[
(k_*)_{s_*}=1,\qquad
(n_*)_{s_*s_*}=n_{ss}/m^2,\qquad
(n_*)_{t_*s_*}=n_{ts}/m,
\tag{7}
\]
and t-derivatives of k are unchanged. These are the arbitrary-n
scaling licenses in469 Section2, without its later fourth-derivative
restriction. Write k*=s*+f with f_{s*}=0 by exact subtraction.
This is not normalization of a nonconstant m by a field-valued
ambient coordinate change.

## 3. Exhaust the nonlinear first-potential branch

We first prove in the normalized chart
\[
f'''\ne0\quad\Longrightarrow\quad (n_*)_{s_*s_*}=0,
\tag{8}
\]
where primes are the exact t* derivatives. Suppose to the contrary
that e=(n*)_{s*s*} is nonzero. Suppress stars for this contradiction.

The complete
[468](principal-paraboloid-nonlinear-first-balanced-frontier-pass468-working.md),
Sections2--3, retains the separate constant-sigma exclusion462 and
affine-sigma exclusion463. Thus a=deg_v(sigma)>=2. Its full460
input gives deg(y)=deg(theta)=r and 2r>=3a. Its strict-branch
argument, using461,465,467 and466, excludes 2r>3a in EVERY degree.
No upper degree bound is used in that exclusion.

Therefore 2r=3a. Since a,r are positive integers, a=2c and r=3c
for a positive integer c. The possibilities are exhausted as follows.

- If c=1, the complete parity argument
  [470](principal-paraboloid-balanced-quadratic-sigma-parity-exclusion-pass470-working.md)
  excludes the profile(2,3). Whole generation handles both the
  distinct-point and derivative-zero common-root boundaries.
- If c>1, the necessary remainder restrictions of
  [471](principal-paraboloid-balanced-cubic-reduction-pass471-working.md),
  Sections1--2 and4--5, give R=rho*P+S, deg(S)=c and d nonzero.
  The complete descent
  [472](principal-paraboloid-balanced-residual-descent-exclusion-pass472-working.md)
  then excludes the profile in every such degree.

Here is the mechanism in the latter case. Its complete elimination
polynomial K has exact degree3c-1. The first residual U=S^2+delta*P
has degree at most c. After V=U-mu*S, the exact expression is
\[
K=\frac{C_*}{\delta^2}S^5V+\widetilde R_5(S,V),\qquad
\deg_{S,V}\widetilde R_5\le5,\quad C_*\delta\ne0.
\tag{9}
\]
The highest-degree comparison first gives deg(V)<c, then rules out
every positive degree of V. Thus V belongs to L, including V=0.
The genuine fourth relation puts q in L(S), and the explicit
intersection proof puts q in L[S]. All three intrinsic generators
therefore belong to L[S]. Whole generation forces L[v]=L[S], hence
c=1, a contradiction. No finite degree enumeration, degree-nine
bound, or projective plane-degree argument is used here.

Every alternative under e nonzero has now been excluded. This proves
(8). Transport by(7) gives n_ss=0 in the ORIGINAL chart.

## 4. Recognition and the zero-coupling union

Return to the original chart with m in C*. There are exactly two
possibilities for the field element k_ttt.

If k_ttt=0, the retained working synthesis
[422](principal-paraboloid-constant-coupling-recognition-synthesis-pass422-working.md)
already gives n_ss=n_ts=0 and A isomorphic to C^[3]. Joint exact
constants give n_s in C.

If k_ttt is nonzero, Section3 gives n_ss=0. The ORIGINAL chart now
meets the retained working synthesis
[457](principal-paraboloid-affine-first-potential-recognition-pass457-working.md).
It imposes no condition on k_ttt, n_ttt or ell, and gives n_ts=0,
n_s in C and A isomorphic to C^[3]. This proves(2) and the nonzero
case of(1). No condition on k_tttt was introduced.

Finally suppose k_s=0. If n_s=0, retained
[268](principal-paraboloid-zero-coupling-recognition-pass268-working.md)
recognizes the original kernel. If n_s is nonzero, retained
[294](principal-paraboloid-nonconstant-intercept-recognition-synthesis-pass294-working.md)
recognizes it. These are exhaustive alternatives over the exact
field L. They prove the zero case of(1), not the extra conclusions
about n in(2). This zero-coupling union was already explicitly
recorded in the earlier README and research ledger.

## 5. Dependencies, verification and the actual remaining gap

The new contradiction is Section3's assembly of strict exhaustion
with both balanced exclusions. The recognition endpoints remain
RETAINED working inputs.422 uses363 and348/346.457 uses436, retaining
348/346,427 and the specified actual-entry266/invariant-coordinate
and regularity route.268 and294 retain their own actual descent and
published preslice/regular-kernel inputs. This note does not recursively
re-certify those ancestors or freshly primary-audit their published
theorems. An intrinsic L-coordinate is never substituted for an actual
complex polynomial coordinate in these recognition steps.

Root read the complete current264,422,457,468,469,470,471 and472
before this synthesis. Both zero-coupling sources268/294 were freshly
read through EOF, as were the scope sources324/426 and the next-target
source325. Current held hashes, full-read evidence and independent
source verdicts belong in the ledger.

Fresh unsaved b5242d reconstructed the entire original balanced Phi,
the transported minor, all four high coefficients of K, its exact
off-level elimination identity, and the complete universal degree-five
residual. Every identity residual was zero. Fresh6f6733 checked the
entire displayed Q2 and R5 in472. The written degree and whole-return
arguments, not finite computations alone, supply the exclusion.

Within the specified chart, any still-unrecognized case must now have
k_s outside C. Some of those cases are already covered too: retained
[324](principal-paraboloid-reducible-surface-recognition-synthesis-pass324-working.md)
recognizes reducible H0 over the exact field L. No assertion that all
remaining coefficient functions are realizable or finitely classified
is made. The filtered-frame obstruction426 prevents normalizing a
variable k_s to a complex constant by its bounded class of maps.
It does not preclude other actual automorphisms.

A next bounded target is325's irreducible-surface, birational projected
line with variable coupling. Its intrinsic generators are affine, but
that does not by itself produce an original invariant coordinate.
The variable-coupling fourth potential and full scalar remain required.

Outside this supplied chart, arbitrary actual-frame entry, other full
initial kernels and time-degree profiles remain unresolved. The intended
field and dimension of Luo's email are still unconfirmed. No unrestricted
cancellation, historical novelty, human expert review, formal certification
or publication readiness is claimed. All saved checkers remain frozen;
none was executed, imported, compiled or rerun. No external contact,
submission, publication, paid service, git mutation or automation occurred.
