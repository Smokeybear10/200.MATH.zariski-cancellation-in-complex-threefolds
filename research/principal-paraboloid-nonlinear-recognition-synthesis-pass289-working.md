# Recognition of all nonlinear selected components in the supplied principal chart

Every nonlinear selected plane component in the supplied actual branch271
is now recognized by the retained working arguments. This synthesis is an
exhaustive degree split, not an additional coefficient computation. It
does not recognize the remaining projected lines or the full1222 profile.

## 1. Exact retained entry

Retain every actual hypothesis, exact field construction, calibrated
Jacobian and whole-line return in
[271](principal-paraboloid-nonconstant-intercept-plane-reduction-pass271-working.md)
and the nonlinear reduction
[280](principal-paraboloid-nonlinear-constant-slope-pass280-working.md).
In particular,
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad
\deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(X^2Z-Y^2)\text{ is the full weighted initial kernel},\\
\operatorname{shift}(\partial_Z)=4,\quad k_s=0,\quad n_s\ne0,\\
K=\operatorname{Frac}A=\mathbb C(y,z,w)=L(v),\quad
Nv=1,\quad L[y,\sigma]=L[v].
\end{gathered}
\]
All coefficient fields and commuting partials are those of that actual
construction, not arbitrary algebraic extensions. Assume that the full
irreducible plane relation \(G\) of \((y,\sigma)\) is nonlinear:
\[
g=\deg G\ge2.
\]
The working conclusion, subject to the retained proof dependencies, is
\[
\boxed{A\cong\mathbb C^{[3]}.}
\]

## 2. The degree split is exhaustive

The conclusion of280 gives \(H=hn+c\), \(h\in\mathbb C^*\),
\(T=pn+q\), and a literal primitive \(Q\) of degree at most four.
Its unit evaluated cofactor has the precise form
\[
Q-q_0=\eta G+G^2R,\qquad \eta\in L^*.
\]
This nonzero polynomial is divisible by \(G\), so \(2\le g\le4\).
There are exactly the following alternatives.

- If \(g=3\), then \(R=0\) by degree, and \(\deg Q=3\).
  [283, Sections2--4](principal-paraboloid-cubic-and-degenerate-conic-pass283-working.md)
  excludes this case by the calibrated scalar determinant.
- If \(g=4\), then again \(R=0\), and \(\deg Q=4\).
  The genuine quartic graph is excluded in280. Every other genuine
  quartic satisfies the corrected exact-field reduction
  [281](principal-paraboloid-quartic-exact-field-reduction-pass281-working.md).
  Its \(p'=0\) alternative is excluded by
  [284](principal-paraboloid-constant-p-quartic-exclusion-pass284-working.md).
  Its \(p'\ne0\) alternative is recognized by
  [285](principal-paraboloid-nonzero-p-derivative-quartic-recognition-pass285-working.md).
  These are exhaustive in the exact coefficient field.
- If \(g=2\) and \(R=0\), then \(\deg Q=2\). Write \(B\) for
  the \(U^2\) coefficient of \(Q\), not the ambient ring.
  The \(B=0\) case is recognized by
  [283, Section5](principal-paraboloid-cubic-and-degenerate-conic-pass283-working.md).
  The \(B\ne0\) case is recognized by
  [286](principal-paraboloid-quadratic-conic-recognition-pass286-working.md).
- If \(g=2\) and \(R\ne0\), then \(\deg R=0\) and \(\deg Q=4\).
  The selected conic of this quartic primitive is recognized by
  [287](principal-paraboloid-quartic-selected-conic-recognition-pass287-working.md).
  Its completed-square quantity is a coefficient-field constant, not
  the affine line parameter in281; that note reconstructs the appropriate
  scalar and field return separately.

There is no degree-three whole primitive with a selected conic: if
\(R\ne0\), its square term has degree at least four; otherwise the
whole polynomial has degree two. No irreducibility of \(Q-q_0\) was
assumed in this split. Every realizable alternative above has the stated
recognition conclusion.

## 3. Exact remaining boundary

This proves only the nonlinear sector of the supplied actual271 chart.
The hypothesis \(g\ge2\) is essential to the use of280. Its conclusion
that \(h\) is complex is not silently assigned to projected lines.
The separately recognized constant-second line278 and canonical line275
do not exhaust all projected lines. Their remaining modes are being
investigated separately.

The other coupling branch of264, other selected shifts, other initial
kernels, and arbitrary-coordinate entry remain outside this theorem.
No full sum-seven profile or unrestricted cancellation is established.

Root completely read the final corrected281 and the held283--287
sources before this composition. The endpoint arguments include exact
field return and actual-ring descent, not merely finite determinant
checks. The new contribution here is the exhaustive composition; no
saved checker is rerun, imported or compiled. Historical dependencies
remain working inputs, not recursively certified theorems. There is no
human peer review, formal proof-assistant certification, or novelty claim.
