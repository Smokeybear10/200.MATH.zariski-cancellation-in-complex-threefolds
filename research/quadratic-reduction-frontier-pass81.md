# Coordinate reduction beyond nice sliced actions

The next reduction cannot be justified by scalar Taylor truncation,
automatic extraction of an acceleration LND, a local holomorphic flow
box, or a change fixing all three already-nice coordinates. Each of
these proposed bridges now has an exact obstruction under actual
polynomial-coordinate and slice hypotheses.

This advances the choice of proof strategy. It does not recognize
all quadratic-time sliced actions and does not solve cancellation.
The preceding [nice-action working proof](nice-slice-recognition-pass80.md)
remains the recognition endpoint, with its existing review limitations.

## 1. The next case and the unchanged main question

The current bounded input is
\[
B=\mathbb C[x_1,x_2,x_3,x_4],\quad E\in\operatorname{LND}(B),
\quad E(s_*)=1,\quad E^3x_i=0.
\tag{1}
\]
Unlike the recognized nice case, some E squared(x_i) may be nonzero.
The bound is on degree in the group parameter, not on ordinary
polynomial degree or on adjoints of the coordinate partials.
There is no assertion that every cylinder action admits even (1).

The full working question remains
\[
A[s]\simeq\mathbb C^{[4]}
\quad\Longrightarrow\quad A\simeq\mathbb C^{[3]}.
\tag{2}
\]
This is still an unconfirmed correction and specialization of Luo's
email. The intended field, dimension and corrected conclusion have
not been confirmed. No partial result below is substituted for (2).

## 2. Universal scalar filters are exactly slice dilations

The [all-degree filter theorem](universal-slice-filter-obstruction-pass81.md)
proves the following for every fixed integer d>=2. A scalar filter
\[
x_i\longmapsto\sum_{j=0}^d c_j s_*^j E^j(x_i),\qquad c_0=1,
\tag{3}
\]
preserves every actual coordinate frame of E-degree at most d if and
only if c_j=(k-1)^j/j! for a nonzero complex k. Its images then agree
with the automorphism fixing ker E and sending s_* to k s_*.
All original E-degrees are preserved.

Necessity follows on a single actual frame
x_1=s+a^2, x_2=a+x_1^d, x_3=b, x_4=c. The nonzero-constant
Jacobian condition forces consecutive weight multipliers to satisfy
r_{j+1}=k r_j. Sufficiency uses the actual slice presentation and
the inverse dilation. No Jacobian-conjecture converse is assumed.

The [quadratic control](quadratic-flow-filter-obstruction-pass81.md)
specializes this to all scalar pairs. In particular x-s E(x)/2
has nice entries on that frame but Jacobian -1/2-as. Keeping the
extra s squared E squared(x)/8 term gives a genuine half-slice
dilation, which does not lower the nonzero quadratic degree.
Changing the supplied slice can make a particular filter succeed;
the result excludes the universal formula, not such choices.

## 3. Acceleration invariance is not an auxiliary-action theorem

With P=Ex and Q=E squared(x), one has E(Q)=0. But the derivation
H=sum Q_i partial_i need not be locally nilpotent or commute with E.
The [actual acceleration control](acceleration-field-obstruction-pass81.md)
uses the inverse polynomial frame
x=s, y=(1+s squared)a+sb, z=sa+b, w=c+s squared.
Here H=2(y-xz)partial_y+2partial_w. Its coefficients generate the
unit ideal and H(w/2)=1, yet H^n(y)=2^n(y-xz) never vanishes.
Dividing coefficient content cannot repair it.

The issue is also visible in the chain rule: coordinate acceleration
acquires a Hessian term under a nonlinear coordinate change. It is
not the transport of a fixed vector field. Separate actual examples
exclude commutation even when H happens to be a nice LND. These
examples all have polynomial kernels already.

## 4. Local straightening has an exact global degree obstruction

The selected primary time-polynomial flow theorem supplies a local
holomorphic straightening, not a global polynomial inverse.[^flow]
The [flow-box analysis](quadratic-flow-box-source-boundary-pass81.md)
proves the precise algebraic boundary: for any actual coordinate ell
of positive E-degree m, the map from A^1 times V(ell) obtained by
following the flow has function-field degree m. Its B-algebra is
B[T]/(exp(-TE)ell); the defining polynomial is primitive and
irreducible of T-degree m.

The map is a global polynomial isomorphism exactly when E(ell) is
a nonzero constant. Quadratic ell gives a generic double cover.
Even degree one permits a birational map with a missing divisor.
Using the supplied slice instead gives the original cylinder over
Spec A, not a known polynomial three-space. Thus this construction
does not bypass the required coordinate-slice argument.

## 5. Rank-one acceleration requires more than fixing the good coordinates

Suppose E squared(x_i)=0 for the first three coordinates and
E squared(z)=q. Put I=(Ex_1,Ex_2,Ex_3)B. The
[shear criterion and obstruction](rank-one-acceleration-shear-boundary-pass81.md)
give
\[
E^2F=\sum_{i,j=1}^3 Ex_i Ex_j F_{x_ix_j}\in I^2,
\qquad F\in\mathbb C[x_1,x_2,x_3].
\tag{4}
\]
If this equation equals q, then z-F is an actual triangular change
to a nice frame, and the preceding recognition proof applies.
But q in I squared is not automatic and alone is not asserted
sufficient for solving the displayed Hessian equation.

The explicit original action E=a squared partial_x+(1+ax)partial_y
on C[a,x,y,c] has a polynomial slice and an explicit adapted inverse,
yet q=a cubed is not in I squared=(a to the fourth power).
Every automorphism fixing C[a,x,c] pointwise sends y to lambda y+F,
with lambda a nonzero constant. None can remove this acceleration.
Its known adapted coordinates change x as well as y. The counterexample
therefore specifies a necessary freedom for the next coordinate
construction instead of disproving nice-frame existence.

## 6. Remaining proof obligations

The next useful construction must permit simultaneous changes in the
already-nice coordinates, or supply an independent recognition route.
One concrete intermediate target is the actual rank-one-acceleration
case without an assumed invariant ambient coordinate. A proposed
algorithm must handle the nonreduced ideal powers in Section 5 and
give two-sided polynomial inverses on their vanishing fibers.

No constant good-direction existence, arbitrary nice-frame existence,
or new general height bound has been proved here. The last general
all-profile threshold remains ten, exactly as previously recorded.
The source audit is bounded, and none of these elementary obstructions
is claimed historically novel.

The [proof audit](proof-audits-pass81-working.md),
[targeted verification](verification-pass81-working.json) and
[checkpoint](checkpoint-pass81-working.json) keep written proofs,
source applicability, finite tests and integrity evidence separate.
The checkers address explicit polynomial identities, not every
action in (1) or the full implication (2). The last full regression
remains the recorded pass75 run; pass81 does not claim a fresh full
regression or central registry integration.

This material has separate AI proof reconstructions. Human expert
review, formal verification and a historical novelty assessment remain
incomplete. No external contact, submission or public claim has been made.

[^flow]: Dominique Cerveau, Julie Déserti and Alcides Lins Neto,
[*Holomorphic vector fields with a barycentric condition*](https://arxiv.org/html/2206.06475v2),
arXiv:2206.06475v2, May 12, 2023, Proposition 4.2 and Theorems 4.5,
4.8. The flow-box note records the precise selected proof reads and
the distinct published bibliographic record. The generic-degree and
global-inverse criteria used here are proved in that note, not
attributed to a stronger version of the primary theorem.
