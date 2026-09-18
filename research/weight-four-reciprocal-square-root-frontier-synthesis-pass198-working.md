# Exclusion of the entire reciprocal square-root family

Status: bounded working synthesis. Under the supplied actual
square-root initial kernel and exact time profile, the whole
nonzero-R reciprocal family \(f=\beta_0/q\) is impossible.
Both generic square alternatives are excluded after actual polynomial
normalization. This leaves the nonmonomial \(f=at+bq\), \(a\ne0\),
as the remaining unresolved family for this particular nonzero-R
configuration.

## 1. Exact hypotheses and conclusion

Assume an actual globally sliced frame and the selected coefficient
chart of [universal184](weight-four-universal-chart-potentials-pass184-working.md):
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad
\deg_E(X,Y,Z,W)=(1,1,2,2),\\
\ker\theta_0=(\mathsf Z^2-\mathsf X^3\mathsf Y),\qquad q^2=t,\\
R=k_\rho\ne0,\qquad f=1/R=\beta_0/q,\qquad
\beta_0\in\mathbb C^* .
\end{gathered}
\tag{1}
\]
The full initial kernel, actual global slice, exact coefficient fields,
whole generic line, actual projected field return and scalar Jacobian
are retained. The claim is that no such configuration exists.
It is not a claim about freely prescribed formal coefficient data.

The [nonzero-R reduction195](weight-four-double-cover-nonzero-r-reduction-pass195-working.md)
leaves only the quadratic graph and quadratic projection.
The [reciprocal normalization198](weight-four-reciprocal-square-root-actual-normalization-pass198-working.md)
uses the positive-rho coefficient gates to solve two Euler systems
inside the exact finite field. Its original polynomial scaling,
shears and constant translation, with both inverse orders, then give
\[
R=q,\qquad k=q\rho,\qquad n=-q\rho^2/2,\qquad
\ell=-q\rho^3/2+l,\qquad l\in K .
\tag{2}
\]
The selected original partial, intrinsic derivation, exact coefficient
fields, generic affine-versus-quadratic degree, full initial ideal
and exact time profile are preserved. Thus both normalized arguments
below apply to the same original problem, not to a substituted
formal model.

## 2. The graph alternative is impossible

In the [normalized graph proof198](weight-four-normalized-reciprocal-square-root-graph-obstruction-pass198-working.md),
the graph equation first forces \(l=Cq\), \(C\in\mathbb C\), and
\(\zeta=\vartheta-P(y)=\gamma\in L\).
Its scalar determinant, with the parameter factor retained, then
gives \(\gamma\in K^*\) and \((q\gamma)_q\ne0\).

There are two complete contradictions. Actual projected field return
forces \(K=\mathbb C((q\gamma)^2)\) even though the transcendental
element \(q\gamma\) belongs to \(K\). The index-two field extension
makes this impossible.

Independently, the original entries satisfy
\[
Z^2-X^3Y-2Y(W-C)=(q\gamma)^2 .
\tag{3}
\]
Actual fraction-field membership and normality would make
\(q\gamma\) polynomial. But the left side is primitive and linear
in \(W\), hence irreducible and not a square. This second argument
also rules out \(\gamma=0\), without needing the scalar descent.

## 3. The quadratic-projection alternative is impossible

The [normalized quadratic proof198](weight-four-normalized-reciprocal-quadratic-field-obstruction-pass198-working.md)
keeps \(g=l/q\) unrestricted initially. The three scalar-Jacobian
coefficients force
\[
g=\alpha/q^2+\beta/q^3+\gamma,\qquad
\alpha,\gamma\in\mathbb C,\quad \beta\in\mathbb C^* .
\tag{4}
\]
This is an exact-field conclusion, not a rational-function ansatz.

Writing \(\xi=q\zeta\) and \(T=g-\gamma\), the proof shows that the
projected \(y,z,w\) all lie in \(\mathbb C(y,\xi,T)\).
The actual field-return inclusions then give
\(L=K(\rho)\) and \(K=\mathbb C(T)\).
Since \(p=1/q\in K\), this would identify \(\mathbb C(p)\) with
\(\mathbb C(\alpha p^2+\beta p^3)\), a proper index-three subfield.
The contradiction holds for \(\alpha=0\) too, because \(\beta\ne0\).

Together Sections 2 and 3 exclude both alternatives left after
the valid normalization. This proves the full reciprocal-family
exclusion under (1).

## 4. Verification and remaining frontier

The finite checker
[reciprocal identities198](weight_four_reciprocal_square_root_controls_pass198.py)
checks the raw coefficient gates, actual polynomial
changes and both inverse orders, graph identities, and quadratic
Jacobian/Laurent/field-containment formulas. Its saved-source reviews
and sole canonical execution are recorded separately. All four methods
passed in 0.435 seconds, with exit status zero.
It cannot prove actual field return, finite-field completeness,
integral closure or the stated field-extension degrees; those remain
explicit written arguments.

For this full square-root initial kernel, the zero-R case was
recognized in195 and the nonzero-R monomial \(f=\beta q\) in197.
The complete necessary-equation list195 now leaves only
\(f=at+bq\), with \(a,b\ne0\), unresolved in the nonzero-R case.
No conclusion about that remaining actual family follows from (1).

The two-root nonzero-R cases, other positive-rank initial kernels,
height-two kernels, higher time profiles and arbitrary coordinate
entry remain open. In particular the unrestricted cancellation
conjecture is not solved. The full goal remains active.
There is no human expert review, formal proof certification,
novelty clearance, external contact or public submission.
No197 or earlier source was changed.
