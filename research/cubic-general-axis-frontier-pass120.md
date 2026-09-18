# The general cubic branch has a nondegenerate conic and a constant axis

The supplied actual cubic framework now gives a necessary normal-form
restriction without assuming a polynomial or coordinate first integral.
Its velocity metric Q has rank three, its restriction to the plane
ker n has rank two, and det Q is nonconstant. Moreover there is a
nonzero constant complex vector v0 such that n transposed v0=0 and
Qv0 is a nonzero constant complex covector.

This combines two exclusions with a new restriction on the remaining
case. It does not exclude that remaining case, supply a global original
coordinate inverse, or solve cancellation. Entry of an arbitrary sliced
polynomial cylinder into the special framework is also unresolved.

## 1. Exact scope of the combined result

Assume the full actual constant-acceleration hypotheses90, the embedded
invariant plane S=C[s1,s2], its actual generic ring K[v,u], and an
exact cubic relative relation. Retain the rational cubic direction V
and canonical Q,n from118. Its full rational constant field is
L=C(H), relatively algebraically closed in K. No new condition is
imposed on the rational generator H in this pass.

The [degenerate-metric exclusion](cubic-general-degenerate-metric-exclusion-pass120.md)
rules out ranks one and two. Rank-one derivative minors force a fixed
image direction and then contradict Q_H nonzero. In rank two, Jacobi's
identity for det Q=0 puts the radical of Q inside ker n. Differentiating
that radical makes its ambient direction constant. The polynomial
velocity then has nonconstant polynomial projections in L.

The exact one-dimensional field criterion supplies a polynomial g with
L=C(g) and S intersect L=C[g]. It does not make g a coordinate. This
is enough: the rational derivative constants transfer the complete
polynomial-curve proof119, and a root of the resulting one-variable
polynomial a gives a nonunit g-g0 dividing an original affine-linear
coordinate. Their forced association contradicts its nonzero velocity.
The polynomial-generator theorem is the specifically stated consequence
of de Bondt, not a new claim about all foliations.[^field]

The [general ruled exclusion](cubic-general-ruled-exclusion-pass120.md)
then rules out rank-one restriction of the rank-three metric to ker n.
Relative algebraic closedness supplies the point on its affine line
and the line-valued velocity b=p(H)+wq(H), over L. It also proves the
full constant field of the rational ruling derivative. The actual
potential and unit-volume calculations119 therefore transfer unchanged,
even when K is a proper finite extension of L(w). Their nonzero
-7ar3w coefficient gives the contradiction. The surviving restriction
has rank two; Jacobi's identity now makes det Q nonconstant.

Thus119's coordinate-field hypothesis is no longer needed for either
of these two exclusions. The results concern the same supplied frame;
they do not extend that frame hypothesis to arbitrary sliced actions.

## 2. The remaining conic has a fixed ambient direction

[The conic-axis proof](cubic-nondegenerate-conic-axis-pass120.md)
addresses the remaining rank-three, rank-two-restriction case. A finite
algebraic extension of L splits the conic and normalizes its isotropic
basis and normal. Write b=pw+q/w and
p'=ap+cr, q'=-aq+dr, r'=2dp+2cq+er, with e nonzero. This normalization
requires square roots, not an assumed exponential solution or a global
change of polynomial coordinates.

Set Z=cw+d/w. The actual cubic tensor is 2eZ squared times dH cubed.
The fifth and fourth coefficients of the original-volume determinant
force the leading graph coefficients to have forms r3=k wZ to the
fourth power and r2=j wZ cubed. In its third coefficient, the terms
involving r2 squared cancel. Exactness of the linear potential part
then cancels the r1 terms. The remaining identity forces
c'd-cd'-2acd=0.

If cd is nonzero, an algebraic square root theta of c/d satisfies
theta'/theta=a. Scaling p,q reciprocally makes their derivatives equal,
so their difference is a nonzero constant ambient complex vector v0.
If one of c,d vanishes, normalizing the corresponding column gives
a constant null vector instead. In both cases Qv0 is a nonzero
constant covector. The proof includes the constant-field and finite
extension arguments that make these genuine constants in C cubed.

A constant ambient coordinate change can therefore make the first
entry of n zero and the first row and column of Q constant. The
lower volume coefficients and global original-coordinate constraints
have not yet excluded either the null or the non-null axis case.

## 3. Controls against overextending the result

The polynomial nondegenerate coefficient example119 already has a
constant first column of Q. It is not excluded by the axis restriction.
It has never been supplied with the full actual cubic potential,
unit-volume graph, and global original inverse. Thus it neither proves
that the remaining case exists as an actual frame nor disproves a
future exclusion of that case.

The new rational-transfer check uses H=s/t and w=s squared+t squared.
Its base map has degree two, and its commuting derivatives and
Jacobian multiplier are exact. Pulling back the principal-open
formulas118 preserves their calculated nonzero volume. But the outputs
are fixed by the simultaneous sign change of s,t, so cannot recover
the original base coordinates even rationally. This is an explicit
limit on inferring original generation from rational derivative and
Jacobian identities alone.

The conic checker also treats the finite gauge conditionally. It checks
that compatible coefficient functions give the claimed cancellation;
the existence of the finite splitting field and its exact constants
is a separate written argument. No arbitrary analytic gauge is being
treated as algebraic because its derivatives match a finite sample.

## 4. Verification and the next proof obligation

The [canonical capture120](verification-pass120-working.json) passes
five suites and nine methods, three new and six retained, with all
five input hashes unchanged. The new methods check the generic conic
connection/tensor, actual determinant coefficients, exactness and
conditional gauge, and the rational finite-transfer/noninverse control.
The all-degree polynomial-curve argument is retained from its written
proof119, not certified by another finite sample.

Each of the three full120 proofs has separate independent AI
reconstructions with no invalidating gap found in its stated scope.
These are not human expert review, Lean verification, or statement-level
novelty clearance. The source criterion and the rational first-integral
theorem remain explicitly scoped dependencies. No external classification
theorem is used to obtain the conic axis.

The next task is to exploit the constant axis in the lower volume
coefficients and in the original polynomial reconstruction. It separates
into null and non-null cases. A useful proposed coordinate reduction
expresses the surviving velocity by a quadratic identity over the
one-variable invariant field. The ratio of its two normal entries
must not silently be treated as a generator of the full field L;
it may define a proper finite subfield. Establishing and using those
forms is the next bounded proof task, not a completed claim here.

The full cancellation goal remains active and unsolved. The working
interpretation is still complex-threefold cancellation, which has not
been confirmed as the professor's intended correction to the pasted
dimensionally inconsistent conclusion. No public posting, submission,
external contact, paid resource, or new automation occurred.

## Source

[^field]: Michiel de Bondt, [*Rational maps H for which K(tH) has
transcendence degree 2 over K*, arXiv:1501.06046v4](https://arxiv.org/html/1501.06046v4),
Theorem3.1 and Lemma3.3. The rationality statement and its classical
attribution are Theorem1.1. The selected displayed proofs and their
applicability are recorded in119 and the degenerate-metric proof120;
every deeper classical dependency has not been newly reconstructed.
