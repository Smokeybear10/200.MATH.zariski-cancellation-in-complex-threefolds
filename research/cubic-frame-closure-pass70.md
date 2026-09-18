# Cubic flow recognition under the supplied coordinate frame

Every sliced action of coordinate flow degree at most three in the
supplied two-quadratic frame is recognized by the written proof chain.
The new step removes the remaining dependent moving-cubic alternative.
A finite algebraic root extension proves the common-power form that
the separate cubic recognition argument needs.

The coordinate-frame assumption remains essential to the statement.
This is not unrestricted complex-threefold cancellation, and no
historical novelty or human expert-review conclusion is asserted.

## 1. Exact conditional theorem

Let
\[
B=\mathbb C[Q_1,Q_2,X,Y],\qquad E\in\operatorname{LND}(B),
\qquad E(s_*)=1,\qquad A=\ker E.
\]
The four displayed generators must be actual polynomial coordinates.
Their genuine partials satisfy
\[
\operatorname{ad}_E^2T_1=\operatorname{ad}_E^2T_2=0,
\qquad \operatorname{ad}_E^3T_X=\operatorname{ad}_E^3T_Y=0.
\tag{1}
\]
Then the complete cubic statement is
\[
\boxed{\ E^4(Q_1,Q_2,X,Y)=0
\quad\Longrightarrow\quad A\simeq\mathbb C^{[3]}.\ }
\tag{2}
\]
There is no independence assumption on the two second-adjoint
defects. The bound concerns degree in the action's flow parameter,
not ordinary polynomial degree of its coefficients.

The larger working objective remains
\(A[s_*]\simeq\mathbb C^{[4]}\Rightarrow A\simeq\mathbb C^{[3]}\).
The professor has not confirmed this corrected complex-threefold
interpretation of the original email. In particular neither the field
and dimension nor existence of (1) is inferred from the partial theorem.

## 2. Complete case exhaustion

Put \(V_X=\operatorname{ad}_E^2T_X\) and
\(V_Y=\operatorname{ad}_E^2T_Y\). Ranks in this paragraph are
over \(\operatorname{Frac}B\).

If the two defects have a nonzero complex constant relation, a
constant change within the bad coordinate pair creates a third
good partial. The resulting actual mixed frame is recognized by
the complete [mixed slice theorem](../deep-pass-13.md), Section 1.
This includes both defects zero, one defect zero, and constant
proportionality. It retains the original polynomial slice.

If the defects have rank two, the complete
[independent cubic theorem](independent-cubic-closure-pass69.md)
already proves (2). Its moving cubic case distinguishes the
original joint ranks two and three, and its proof does not silently
assume that invariant normalization preserves defect rank.

It remains rank one with no complex constant relation. The genuine
[primitive decomposition](dependent-quadratic-defects-pass42.md)
writes the defects as \(aD,bD\), with \(D\) a polynomial LND,
\([E,D]=0\), and \(a,b\in\ker E\cap\ker D\).

| Remaining dependent case | Recognition argument |
| --- | --- |
| Coordinate flow degree at most two | The complete [low-flow theorem](low-flow-closure-pass66.md). |
| Nonzero constant third coordinate derivative | The [constant cubic recognition](constant-cubic-closure-pass67.md). |
| Nonconstant third derivative, zero multiplier \(r\) in the full highest-vector reduction | The original commuting good-partial branch of [the dependent highest-vector proof](dependent-defect-top-line-pass43.md). |
| Nonconstant third derivative, nonzero \(r\) | The new finite-root theorem followed by the separately proved common-power cubic transfer. |

The highest nonzero derivative exists because \(E\) is locally
nilpotent on the four generators. Under (2)'s hypothesis it is at
most the third derivative, so these cases are exhaustive.

## 3. The new step: a root must descend to the original ring

The full dependent highest-vector reduction supplies
\[
E^m x=cq,\qquad z=E^{m-1}x,\qquad Dz=c\theta,
\qquad a z_X+b z_Y=qr\ne0,
\tag{3}
\]
where \(m\) is three or four, \(c\) is a nonzero constant good
direction, \(q\in\ker E\cap\ker D\) is nonconstant, and the
original fields \(E,D\) are fraction-field independent. Only
\(m=3\) is needed for theorem (2).

The [finite-root proof](dependent-algebraic-root-top-pass70.md)
first chooses \(g^m=q\) in a finite algebraic extension
\(L=\operatorname{Frac}(B)(g)\). At this point it does not assume
that \(g\) is rational or polynomial. The extended original
partials form a derivation basis on \(L\), but are not presumed
locally nilpotent on the adjoined ring.

The divided action \(\delta=E/g\) is an actual LND on
\(R=B[g,g^{-1}]\). Its normalized defects are
\[
\widetilde V_i=\frac{a_i}{g^2}
\left(D-\frac{\theta}{q}E\right),
\qquad (a_X,a_Y)=(a,b).
\tag{4}
\]
Their rank is exactly one. The actual divided flow and conjugated
partials give mutually inverse polynomial matrices over \(R[t]\).
The complete five-dimensional companion therefore remains valid,
with its variable auxiliary row retained.

Since \(\delta^m x=c\), two-sided block descent makes that
companion's nilpotence index exactly \(m\). For \(m=3,4\),
dimension five permits only one Jordan block of maximal size.
The preceding Jacobian has rank one with image \(Lc\).
Every component of its transverse remainder is thus killed by
all four extended partials.

Differentiating a monic minimal polynomial shows that their common
constants in \(L\) are still \(\mathbb C\). Consequently
\[
z=c\tau+e g^{m-1},\qquad
\tau\in B,\quad e\in\mathbb C^4,\quad e_B\ne0.
\tag{5}
\]
For a bad index with \(e_i\ne0\), equation (5) gives
\(g=e_iq/z_i\in\operatorname{Frac}B\). This is the necessary
rational descent. The monic relation \(g^m=q\) and normality
of the original polynomial ring then give \(g\in B\).
It is a genuine nonconstant polynomial invariant of both original
fields.

No polynomial-ring recognition theorem is used on the adjoined ring.
The conclusion depends on the complete actual frame, not merely on
the earlier weighted differential equation or its formal controls.

## 4. Why this completes the cubic case

For \(m=3\), equation (5) supplies exactly the actual common-power
bad pair required by the
[dependent cubic transfer](dependent-common-power-cubic-pass70.md).
That proof re-establishes normalized rank one without original
defect independence. It then derives the full residual differential
identity used in the rational-symmetry recognition argument.

A nonconstant normalized transverse speed is recognized by the
[rational two-direction theorem](rational-two-direction-recognition-pass69.md).
Zero speed gives an original invariant coordinate. Nonzero constant
speed gives the explicit original polynomial shear to the mixed
frame. These recognition gates retain the original slice and their
stated established plane and invariant-coordinate inputs.[^recognition]

This proves the final row of the table and hence (2). The earlier
rotating formal coefficient examples remain valid examples of
weaker equations; they were never actual realizations of all the
frame hypotheses. They therefore do not contradict the new exclusion.

## 5. Remaining obligations and evidence limits

The root theorem also excludes rotating dependent quartics, but a
common-power quartic is not recognized by the cubic transfer.
The separate [moving-quartic reduction](common-power-moving-quartic-reduction-pass70.md)
recognizes its nonconstant residual-pair branches. Its terminal
constant-pair alternative supplies only a justified localized
three-direction symmetry, with global descent still unresolved.
The higher independent moving sectors, of degrees four and five,
also remain outside theorem (2). The supplied two-quadratic frame
as a whole is therefore not yet recognized.

Even a complete recognition theorem under (1) would leave the
separate problem of producing an applicable actual frame for an
arbitrary sliced action. The general cancellation objective has
not been replaced by the easier conditional statement (2).

Written proof reconstruction, exact example calculations and file
integrity are separate forms of evidence. The completed historical
[pass69 regression](verification-pass69-working.json) contains
1,021 methods in 136 suites. Its test count does not verify the
finite-root argument or certify a theorem, and it is not renamed
as a fresh pass70 regression. The [targeted current capture](verification-pass70-working.json)
records two passing methods in one standalone suite. The
[control note](finite-root-top-controls-pass70.md) separates actual
actions that fail the required frame from altered-field and
nonnormal-ring boundaries. Current proof reviews are recorded
separately in the [working audit](proof-audits-pass70-working.md).

There is no human expert review, formal proof-assistant verification,
historical novelty certification, public posting, submission or
external contact. The historical central registry and experiment
manifest remain at their full60 integration state.

## Sources

[^recognition]: The exact recognition hypotheses and inherited source gates are given in [the rational two-direction theorem](rational-two-direction-recognition-pass69.md), Sections 4--5. Its established inputs include Rentschler's plane theorem, stated in Dasgupta and Gaifullin, [*On locally nilpotent derivations of polynomial algebra in three variables*](https://arxiv.org/html/2306.00510v2), Theorem 2.7, and Bhatwadekar, Gupta and Lokhande, [*Some K-theoretic properties of the kernel of a locally nilpotent derivation on k[X1,...,X4]*](https://arxiv.org/abs/1501.01438), Theorem 3.5. They are not general threefold cancellation results. The finite-root deduction supplies its field-extension and descent arguments directly; it does not require a new curve-factorization input.
