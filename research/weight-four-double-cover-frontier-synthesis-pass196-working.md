# Two-root zero-R recognition and the square-root monomial graph exclusion

Status: bounded working synthesis of the new196 proofs. The supplied
two-root double-cover configuration is recognized in its zero-R branch.
For the different square-root configuration, the entire nonzero-R
monomial quadratic-graph branch is impossible after actual polynomial
normalization. The formal index-two example motivated, but does not
by itself prove, that broader exclusion.

## 1. Common actual hypotheses and the two different conclusions

Work throughout with an actual globally sliced polynomial four-ring
\[
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad
\deg_E(X,Y,Z,W)=(1,1,2,2).
\tag{1}
\]
The initial ideal below means the entire weighted initial kernel,
not merely a relation among its leading coefficients. The exact
coefficient fields, whole generic line, projected field return, and
calibrated scalar Jacobian are those of
[universal184](weight-four-universal-chart-potentials-pass184-working.md).
No global unit speed or rational coefficient field is assumed.

The [two-root zero-R proof196](weight-four-two-root-zero-r-coordinate-recognition-pass196-working.md)
shows
\[
\ker\theta_0=(\mathsf Z^2-\mathsf X^2\mathsf Y(\mathsf X-\mathsf Y)),
\quad q^2=t(1-t),\quad R=k_\rho=0
\quad\Longrightarrow\quad A\cong\mathbb C^{[3]}.
\tag{2}
\]
The proof first establishes exact field return. A pole of order at
least nine excludes a quadratic coefficient cover. The remaining
slope equation has only the algebraic solutions \(b=\lambda q\).
A hypothetical second solution would make a nonzero everywhere-regular
differential on a projective curve exact; the proof gives all local
charts and the finite-extension pullback argument.

The actual coordinate is
\(I=W-\lambda Z^2/2-(\alpha Y+\beta X+D)Z-Q_0(X,Y)\),
with all coefficients complex. Both polynomial inverse orders and
the original coefficient transport are supplied. The global slice
gives a regular kernel, so the cited Bhatwadekar--Gupta--Lokhande
invariant-coordinate theorem applies. Neither \(q\) nor the auxiliary
curve parameters is asserted to be that coordinate.

## 2. A complete exclusion for one monomial graph branch

For the other full initial kernel, the new conclusion is
\[
\begin{gathered}
\ker\theta_0=(\mathsf Z^2-\mathsf X^3\mathsf Y),\qquad q^2=t,\\
R\ne0,\qquad f=1/R=\beta q,\quad \beta\in\mathbb C^*:
\qquad\text{the quadratic-graph square branch cannot occur.}
\end{gathered}
\tag{3}
\]
This is the monomial member of the family \(f=at+bq\) in
[classification195](weight-four-square-root-two-gate-classification-pass195-working.md).
It does not exclude that full family or its other square alternative.

Here is the composition, including the extra hypothesis needed by the
normalized obstruction.

First apply
[actual normalization196](weight-four-square-root-monomial-actual-normalization-pass196-working.md).
It derives the lower coefficient functions from the raw potential
equations and the rho-constant linear remainder, rather than making
a rational-function ansatz. The displayed original polynomial maps
and their inverses preserve (1), the full initial kernel, the selected
intrinsic derivation, and the generic graph degree. They give
\(R=1/q,\ k=\rho/q,\ n=-\rho^2/(2q^3)\).
In the graph subbranch a final constant translation also gives
\(\ell=-\rho^3/(2q^5)\).

The graph property means that \(y\) is affine in the generic line
parameter and \(\vartheta\) is quadratic in \(y\). After the
normalization, its completed square is
\[
\mathcal H=-\frac{(V-P(U))^2}{2q^4}+B_0,\qquad
P(U)=\frac{(U+2\rho)^2}{8q^2},\qquad B_0\in L.
\tag{4}
\]
The linear remainder vanishes: if it did not, the equality
\(\mathcal H(y,\vartheta)=0\) would equate the square of a polynomial
in the affine parameter to a nonconstant linear polynomial, which
is impossible by degree.

Thus \(\zeta=\vartheta-P(y)\in L[y]\) has its square in \(L\),
so \(\zeta\in L\). The second potential now gives \(z=\zeta/q\in L\).
If \(\zeta=0\), the third potential gives \(w=0\) as well.
Then \(\mathbb C(y,z,w)=\mathbb C(y)\) would have transcendence
degree one, contrary to the actual equality with \(L(v)\), whose
transcendence degree is three. Consequently \(z=g\in L^*\).

These are precisely the hypotheses of
[normalized-graph obstruction196](weight-four-normalized-square-root-graph-obstruction-pass196-working.md).
That note retains the possible constant in \(w\), derives \(g_\rho=0\)
from the scalar Jacobian, and obtains
\(Z^2-X^3Y-2X(W-C)=g^2\).
Actual fraction-field membership and normality would make \(g\) an
element of the original polynomial ring. The polynomial on the left
is primitive and linear in \(W\), hence irreducible, a contradiction.
This proves (3) for all lower potentials allowed by the actual gates,
not only for the explicit formal fixture.

## 3. What the formal example and finite checks establish

The separate
[index-two fixture196](weight-four-square-root-formal-index-two-boundary-pass196-working.md)
has the universal potentials, formal leading relation, projected field
return, and constant rational Jacobian, but its original field degree
is two. Its formal time derivation does not preserve the four-entry
polynomial subring. That example is not an actual LND or a cancellation
counterexample. The generalized actual exclusion in (3) depends on
the normalization and normality proof, not on extrapolating from that
single fixture.

The new finite controls are
[two-root identities196](weight_four_two_root_zero_r_controls_pass196.py)
and [square-root graph identities196](weight_four_square_root_graph_controls_pass196.py).
They check algebraic identities, local chart formulas, lower
coefficient equations, and both orders of the polynomial changes.
They do not prove the projective-curve, field-return, integral-closure,
irreducibility, or complete-recognition arguments in the written notes.
Their exact execution evidence belongs in the196 verification record.

## 4. Remaining scope

The nonzero-R quadratic-projection branch with \(f=\beta q\) is not
recognized by this packet. Separate197 work investigates it.
The other square-root families \(f=at+bq\) with \(a\ne0\), and
\(f=b/q\), also remain unresolved here. The two-root nonzero-R
square alternatives are not settled. Neither entire double-cover
configuration, the whole positive-quadratic-rank stratum, nor
arbitrary entry into these time profiles has been proved.

There is no unrestricted cancellation solution, minimum-profile or
entry theorem, human expert review, proof-assistant certification,
or novelty clearance. The full goal remains active. No external
contact, public posting, or submission has occurred. Earlier frozen
sources are unchanged.

