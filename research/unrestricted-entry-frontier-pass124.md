# Coordinate reduction after the constant-acceleration case

The full complex-threefold cancellation question remains unsolved. This
pass tests the missing coordinate reduction, rather than extending the
already closed cubic calculation. It produces two exact obstructions
to proposed shortcuts and an explicit bypass for one control family.
It recognizes no new class of arbitrary sliced derivations.

The working interpretation remains A[u] isomorphic to C^[4] implying
A isomorphic to C^[3]. The professor's intended field, dimension and
corrected conclusion remain unconfirmed. The
[restricted recognition statement123](cubic-exclusion-frontier-pass123.md)
retains its AI-only, source-dependent proof status.

## 1. Strict elementary degree descent is not universal

For E=partial_u on C[u,v,z,w], set Delta=zu+v squared. For every
m at least one, the actual coordinate frame

\[
(X,Y,Z,W)=
(u-2v\Delta^m-z\Delta^{2m},\ v+z\Delta^m,\ z,\ w)
\]

has E-degree tuple (2m,m,0,0). Its sum 3m is arbitrarily larger
than the global minimum one, attained by (u,v,z,w). Nevertheless,
no single elementary coordinate replacement strictly reduces that sum.
The [all-m proof](coordinate-degree-elementary-descent-obstruction-pass124.md)
checks arbitrary added polynomials, not a bounded ansatz.

For X, canceling its top term using the other coordinates would
require a coefficient c/Z with c nonzero constant. That is not a
polynomial. For Y, any positive power of X already has too large
an E-degree. The two remaining degrees are zero. The exact
cancellation identity ZX+Y squared=Delta does not itself give a
polynomial coordinate replacement: the corresponding determinant
is the nonunit Z.

This refutes the algorithm that insists on a strictly decreasing
elementary step at every stage. It does not refute a sequence of
degree-preserving steps followed by a decrease. In particular,
degree-zero moves can insert hidden invariants into the displayed
invariant slots, so those slots cannot be assumed to stay in a
fixed polynomial subalgebra throughout a proposed plateau argument.

## 2. A verified compound move bypasses that control

The [six-shear construction](nagata-stabilized-degree-bypass-pass124.md)
straightens the entire family above using the fourth variable
already present. Its successive degree sums are

\[
3m,\quad4m,\quad2m+1,\quad m+1,\quad1,\quad1,\quad1.
\]

Every step is an elementary polynomial automorphism with its
elementary inverse. The calculation works on Z=0 as well as away
from that divisor. It extends from Delta to any polynomial
f(z,Delta) of positive Delta-degree. The temporary increase is
an upper bound for this path, not a proved minimum over all paths.

The mechanism is an explicit instance of the classical Smith
stable-tameness commutator, as restated and proved in
[Drensky--Yu, Theorem3.6(iii)](https://hub.hku.hk/bitstream/10722/48401/1/63202.pdf).
Neither the construction nor this pass is presented as a new
stable-tameness theorem. The useful information is how its actual
steps behave for the different orbit-degree measure under study.

## 3. Quadratic time does not provide a constant good direction

The second [actual-frame control](quasi-nice-full-acceleration-span-pass124.md)
starts with the same translation E=partial_u and elementary changes

\[
r=u+v^2,\quad Y=v+r^2,\quad Z=z+vY,\quad
W=w+v^2Y,\quad X=r+YW-Z^2.
\]

There is a complete polynomial inverse. Since
YW-Z squared=Y(w-2vz)-z squared, all four final coordinates have
exact E-degree two. Their acceleration row is

\[
(E^2X,E^2Y,E^2Z,E^2W)=2(w-2vz,1,v,v^2).
\]

These four functions are complex-linearly independent. Hence no
nonconstant affine-linear combination of X,Y,Z,W is E-affine,
and no constant affine change provides even one zero-acceleration
coordinate. This remains true although E squared Y equals two,
so the acceleration ideal is the unit ideal.

The inverse supplies a nonlinear nice frame. The example therefore
requires nonlinear improvement of this supplied frame, not failure
of improvement altogether. It disproves a constant-linear reduction
from quadratic time to the assumptions of123, not cancellation.

## 4. What the source check establishes

The [primary-source audit](source-audit-pass124.md) distinguishes
the published m-quasi-nice condition, which kills second derivatives
of selected coordinates, from third derivatives vanishing on all
four coordinates. The nearby relative recognition theorems require
actual invariant coordinate rings that the arbitrary cylinder has
not supplied. A published quadratic-time example with singular
kernel has no slice and is not a counterexample to the question here.

The stable-coordinate reformulation and invariant-coordinate
recognition gate were already in the earlier ledger. They were
not rediscovered or counted as new deductions. No primary theorem
recognizing every sliced quadratic-time four-coordinate frame was
located in this bounded search; that is not an exhaustive proof
of the literature's current open status.

## 5. The first possible true-minimum profile

There is a precise conditional lower bound for a hypothetical
counterexample, using the retained recognition results. For its
actual sliced derivation E, minimize the sum of E-degrees over
all actual polynomial coordinate frames. Such a minimum exists
because the set is a nonempty set of nonnegative integers.

No entry in any such frame could have degree zero: an invariant
ambient coordinate and the slice's regular kernel would invoke
Bhatwadekar--Gupta--Lokhande Theorem3.5, as checked in the source
audit, and identify the kernel as a polynomial three-ring. Thus
all four degrees would be positive. A sum of four is the nice
case covered by the retained working theorem80. Consequently
the minimum would have to be at least five.

If it were exactly five, the only profile, up to permutation,
would be (2,1,1,1). Its sole nonzero acceleration q would be
invariant. The recognition statement123 now excludes q in C*,
so this first possible profile must have nonconstant q.

Two elementary necessary conditions sharpen that first profile.
Writing a_i=E(x_i) for the three degree-one coordinates, the four
functions 1,a_1,a_2,a_3 must be complex-linearly independent.
Otherwise a nontrivial linear combination of the x_i has constant
velocity. Zero velocity gives an invariant ambient coordinate;
nonzero velocity gives an ambient coordinate slice. Either case
recognizes the kernel, contradicting the hypothetical counterexample.

Also q cannot lie in E squared(C[x_1,x_2,x_3]). If q=E squared F,
the elementary change z to z-F makes the whole actual frame nice.
In particular q cannot be a quadratic form with complex constant
coefficients in the a_i: the corresponding half-quadratic form
in the x_i is such an F. These are necessary gates, not a proof
that arbitrary coefficient-ideal membership integrates to a shear.

This is a dependency-based location of the first unresolved
profile, not a proof that every hypothetical counterexample can
reach height five. Heights above five remain in the full problem.
Nor does a one-step elementary minimum qualify as this true
global minimum, as Section1 shows. The lower bound inherits the
AI-only confidence limits of the retained nice and constant-
acceleration proofs; it is not a newly published classification.

## 6. Verification and the next obligation

The two new checkers verify actual inverses, elementary moves,
complete polynomial flow identities and degree/acceleration
coefficients. The arbitrary-m obstruction and arbitrary-polynomial
bypass also have written proofs. Separate AI reconstructions are
not human expert review or formal proof verification.

The [canonical verification capture](verification-pass124-working.json)
records three suites and eight passing methods: four new and four
retained scalar checks from123. All three input hashes are unchanged.
The run took 5.385752958012745 seconds; unittest reports 5.094
seconds. These checks do not certify a universal descent theorem,
the all-m proof, source dependencies or cancellation. No full
historical regression was rerun.

The research must now distinguish true global minimizers of a
coordinate-degree measure from frames that merely defeat one
greedy elementary step. The new controls make that distinction
concrete. Any subsequent general reduction must allow genuinely
nonlinear changes, verify their polynomial inverses, and prove
why an admissible sequence terminates. An arbitrary look-ahead
search does not supply such a theorem.

No universal entry into a recognized frame has been proved. No
submission, external contact, public novelty claim, paid resource,
new automation or modification of research artifacts through123
was part of this pass.
