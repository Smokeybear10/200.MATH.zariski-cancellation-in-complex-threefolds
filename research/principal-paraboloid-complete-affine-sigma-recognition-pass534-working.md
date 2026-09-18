# Recognition of the entire supplied affine-sigma sector

Working scoped synthesis. Retain EVERY actual hypothesis of264.
If its intrinsic first slope sigma is affine nonconstant in the
selected line parameter, then
\[
\boxed{\deg_v\sigma=1\quad\Longrightarrow\quad k_s\in\mathbb C.}
\tag{1}
\]
Subject to the historical recognition dependencies retained in473,
\[
\boxed{\deg_v\sigma=1\quad\Longrightarrow\quad
       A\simeq\mathbb C^{[3]}.}
\tag{2}
\]
There is NO extra restriction on the intrinsic degree of theta,
the degree of y, either derivative of m=k_s, or a leading
coefficient of the original Z or W row.

This is still a supplied-chart theorem. It neither produces that
chart from arbitrary cancellation data nor makes a nonlinear sigma
affine by an actual coordinate change. The general conjecture
remains unsolved. The results and their retained dependencies are
working AI-reviewed arguments, not expert review or formal
proof-assistant certification.

## 1. Exact supplied input

Retain the original hypotheses and construction of
[264](principal-one-affine-paraboloid-chart-pass264-working.md):
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,
\quad X=a_0u+x_0,\quad a_0\ne0,\quad x_0\in A,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\qquad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the ENTIRE coordinate-initial kernel},\\
0\ne N=[u^4]\partial_Z|_A\in\operatorname{LND}(A),\quad
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,\\
Na_0=Nt=Ns=0,\quad Nv=1,\quad O=L[A]=L[v],\\
\operatorname{Frac}A=L(v)=\mathbb C(y,z_{\rm int},w),\qquad
L[y,z_{\rm int},w]=L[v].
\end{gathered}
\tag{3}
\]
The original global slice, localizations, selected partial, full
initial kernel and both actual returns remain required. The symbol
z_int is the literal original Z-intercept, not z_int-2ty.
The coefficient partials commute and their joint constant field
is C. L is not assumed rational.

The extra hypothesis in this note is only deg_v(sigma)=1.
Set P=sigma. Then O=L[P], NP=rho in L*, and the exact
coefficient partials on L are extended to fix P. The literal rows
and potentials are
\[
\begin{aligned}
Y&=y+PX+tX^2,\\
Z&=2ty+P^2+k_tP+m\theta+n+(2tP+k)X+t^2X^2,\\
W&=w+\theta X+sX^2,\qquad m=k_s,\\
mw&=\ell-(2P+k_t)y-k_{tt}P^2/2-m_tP\theta
                         -m_s\theta^2/2-n_tP-n_s\theta,\\
J_{t,s,P}(Y,Z,W)&=-a_0^4/\rho\in L^*,\qquad
L[X,Y,Z,W]=L[X,P].
\end{aligned}
\tag{4}
\]
All intrinsic functions are polynomials in P over L. No upper
bound on their degrees is assumed. The scalar in (4) can vary
with t,s. P is an intrinsic parameter, not necessarily an actual
complex polynomial coordinate.

When m is nonzero, the genuine levels, evaluated unit gradients
and minors of296 and the UNIVERSAL Sections1--3 of494 apply.
Their later conic-specific restrictions are not imposed on the
other branches in this synthesis.

## 2. Exclude noncomplex coupling when theta has higher degree

Suppose m is not in C, hence in particular m is nonzero.
First assume d=deg_P(theta)>=3. The accepted
[521](principal-paraboloid-higher-slope-intercept-degree-bound-pass521-working.md)
gives deg_P(y)<=d, including y=0.

If h=m_s is nonzero, the uniform
[528](principal-paraboloid-transverse-coupling-higher-degree-bound-pass528-working.md)
forces d to be three or four. Its degree-at-least-five comparison
retains the moving leading-shear derivatives, and does not extend
that comparison across the quartic degree tie. The two remaining
degrees are now separately excluded:

- [530](principal-paraboloid-transverse-cubic-exclusion-pass530-working.md)
  excludes cubic theta and every deg(y)<=3. Its complete odd-part
  resultant has a finite common root, after which a single constant
  X0 is chosen. A proper parity subring contradicts the all-X return.
- [531](principal-paraboloid-transverse-quartic-exclusion-pass531-working.md)
  excludes quartic theta and every deg(y)<=4. Its resultant treats
  the only possible infinite-root exception explicitly and forces
  deg(y)<=3. The full monic level handles lower y degrees; the full
  scalar and tangent-minor coefficients contradict cubic y.

Thus h=0. Since m is noncomplex and the joint constant field is C,
we necessarily have p=m_t nonzero. There are two remaining degree
possibilities. The complete
[526](principal-paraboloid-equal-higher-degree-univariate-coupling-exclusion-pass526-working.md)
excludes deg(y)=d, including either value of the leading W
coefficient. The separate
[527](principal-paraboloid-unequal-higher-degree-univariate-coupling-exclusion-pass527-working.md)
excludes deg(y)<d under p nonzero. The latter includes zero y
and is not an application of the equal-degree theorem outside
its hypotheses. These alternatives are exhaustive by521.
Therefore noncomplex m is impossible whenever d>=3.

This composition is uniform in d. It does not rely on the finite
intrinsic-degree window of299 or bound the complexity of the
coefficient functions in L.

## 3. Quadratic theta and its degree-drop boundary

If theta has exact degree two, the complete retained synthesis
[520](principal-paraboloid-complete-affine-sigma-quadratic-graph-recognition-pass520-working.md)
already gives m in C. It includes BOTH values of
delta=1+m*[P^2]theta. Its nonzero-delta proof is510; its zero-delta
proof retains511--519 with their separate zero-quadratic and
zero/nonzero cubic-W cases. No nondegenerate parity theorem is
extended across delta zero here. Thus this degree also contradicts
our assumption that m is noncomplex.

## 4. Affine or zero theta gives an affine intrinsic line

The remaining case is deg_P(theta)<=1, taking the zero polynomial
to have degree minus infinity. Write theta=mu*P+e with mu,e in L.
Since sigma=P, the projected plane algebra L[sigma,theta] is
already L[P]; its complete plane equation V-mu*P-e is a line
and its function-field projection has degree one.

Consequently the retained
[325](principal-paraboloid-all-specializations-affine-line-profile-pass325-working.md)
applies with precisely its birational projected-line hypotheses.
It gives deg_P(y)<=1, so y=lambda*P+r. Briefly, the monic third
level first bounds the degree by two, and the all-X polynomial
return excludes the quadratic possibility. This endpoint of325
was independently reconstructed in fresh162143, including zero
theta; it is a retained result, not a new low-degree claim.

The second potential in (4) now has degree at most two, hence
w=omega*P^2+bP+c, allowing omega=0. These are exactly the affine
intrinsic data needed by the following complete split:

- If omega is complex, the retained
  [479](principal-paraboloid-complex-quadratic-slope-two-quasi-exclusion-pass479-working.md)
  excludes the branch under noncomplex m. Both alternatives of
  its field two-quasi theorem and its zero-slope cases are retained.
- If lambda is complex, the retained
  [483](principal-paraboloid-constant-linear-slope-exclusion-pass483-working.md)
  excludes the branch under noncomplex m. Its zero normalized
  lambda and every lower scalar term are covered, not divided out.
- If lambda and omega are both noncomplex, the new
  [533](principal-paraboloid-affine-line-initial-growth-exclusion-pass533-working.md)
  excludes the branch. Its actual polynomial three-ring has
  intrinsic profile (1,2,2). The actual W-partial and growth of two
  independent invariants force its entire initial relation to have
  weight two. Two regular complex-X values then give a contradiction.

This covers all lambda and omega in L, including zero values.
No contact parameter, beta-nonzero condition or square-root family
classification is needed for this last split. In particular the
necessary families left by489 do not furnish an omitted actual
case: they did not establish the actual-ring conditions now used
in533. No existing necessary coefficient identity is retracted.

Sections2--4 exhaust every polynomial theta over L and contradict
m outside C. This proves (1).

## 5. Recognition and retained dependency status

Apply the scoped synthesis
[473](principal-paraboloid-complete-constant-coupling-recognition-pass473-working.md)
in the ORIGINAL actual chart. Its m=0 branch is the separate
268/294 union; none of our arguments dividing by m is used there.
For m in C*, its retained recognition endpoints are422 and457.
The original actual-coordinate, regularity and preslice hypotheses
in their stated dependency chains are not replaced by intrinsic
coefficient-field assertions. This proves (2) conditional on those
retained recognition inputs.

The proof of (1) also retains earlier exclusions520,526,527,479,483.
Their complete historical ancestry has not been recursively
re-certified in this synthesis. The new sources530,531,533 and
the composition here require complete independent saved-source
reviews in addition to algebraic outline checks. Their held hashes
and verdicts are recorded separately in the research ledger.
Auxiliary532 independently explains the quartic leading tie but
is not needed as a dependency of531 or this composition.

## 6. What remains outside the theorem

The result covers the entire affine-nonconstant-sigma sector of
the supplied, oriented principal chart. It does not cover arbitrary
nonlinear sigma, nor does it establish the original time profile
or entire initial kernel for a general sliced derivation on C^[4].
The bounded actual map family426 preserves positive intrinsic
sigma degree, so it cannot itself make a nonlinear sigma affine.

The general-entry problem and the intended field and dimension
in Luo's email remain unresolved. No theorem here changes the
objective to this special case. The corrected complex-threefold
cancellation question remains UNSOLVED and the full goal active.
No human expert review, Lean certificate, established novelty,
publication readiness or external endorsement is claimed.

The author fully reread264,325,473,479,483,494,520,521,528,530,
531 and533 for their scopes, and revalidated the held526/527
statements and hashes against the already accepted full reviews.
All saved checkers remain frozen. No saved checker was executed,
imported, compiled or rerun; no external contact, public submission
or earlier-source edit occurred while authoring this synthesis.
