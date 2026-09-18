# Nonlinear cancellation frontier after the nice-action rank exclusion

The unrestricted complex-threefold cancellation problem remains unsolved.
The current deductions remove a previously retained quadratic search region,
give an exact obstruction to a proposed linear-coordinate shortcut, and
construct degree-bounded inverse coordinates for specified projection families.
None proves that an arbitrary sliced action belongs to one of those families.

## 1. Fixed objective and proof status

The working interpretation remains
\[
B=A[s]\simeq\mathbb C^{[4]}
\quad\Longrightarrow\quad A\simeq\mathbb C^{[3]}.
\tag{1}
\]
The professor has not confirmed the intended field, dimension, or correction
of the dimensional typo in the original email. The investigation of (1)
is private. No expert review, formal proof, novelty certification, external
contact, or submission has occurred.

The [pass73 conditional theorem](height-ten-closure-pass73.md) recognizes
every supplied actual two-quadratic adjoint frame. Its all-profile threshold
is still ten. This pass does not raise that threshold or prove a universal
frame bound. Separate AI reconstructions and exact finite controls remain
different kinds of evidence; neither is human or proof-assistant review.

## 2. A necessary condition for every actual nice sliced frame

Suppose in actual polynomial coordinates that
\[
E=\sum_iP_i\partial_{x_i},\qquad E(s)=1,\qquad E(P_i)=0,
\qquad J=(\partial_jP_i).
\tag{2}
\]
The [complete rank-exclusion proof](nice-slice-adjoint-rank-pass74.md)
derives the actual adjoint identities
\[
\operatorname{ad}_E^r(\partial_{x_i})(x)
=(-1)^r r!J^re_i,
\qquad J^3=0,\qquad\operatorname{rank}_{\operatorname{Frac}B}J\le2.
\tag{3}
\]
The decisive input is the original slice. A nilpotent four-block would
make a nonzero highest third adjoint of an actual coordinate partial
parallel to E. The [vertical exclusion](vertical-top-exclusion-pass69.md)
rules that out through a genuine locally nilpotent Laurent degeneration,
restriction and stable-ideal quotient. It never assumes A polynomial.

For spatial coefficient degree at most two, (3) supplies the hypothesis
of de Bondt's published triangularization theorem. An extreme component
then gives an actual invariant linear coordinate or an actual linear
slice, and the retained recognition results apply. The
[source-scope note](quadratic-nice-source-scope-pass74.md) also gives an
independent published route through Sun's homogeneous theorem and an
explicit strong-nilpotence descent. Its original-proof access limitation
is stated, and is not needed for the first route.

Thus the rank-three quadratic packet in the historical
[nice-route inventory](nice-route.md) is empty under its original slice
hypothesis. It should not be researched as a surviving packet. This is
a correction to that inventory, not a claim to a new quadratic classification.
Arbitrary quadratic-coefficient LNDs are not thereby covered: niceness is
an additional hypothesis and their Jacobians need not satisfy the same
identities.

## 3. The exact remaining nice-frame profiles

Define constant vector spaces, not fraction-field kernels,
\[
G_1=\{v\in\mathbb C^4:Jv=0\},\qquad
G_2=\{v\in\mathbb C^4:J^2v=0\}.
\tag{4}
\]
If \(\dim G_2\ge2\), two independent constant vectors in G_2
can be completed to an actual linear coordinate frame. Equation (3)
then gives exactly the two-good/two-quadratic bounds recognized in pass73.
If \(G_1\ne0\), a nonzero vector in G_1 gives a commuting coordinate
partial, while the other three have adjoint height at most two. The
profile is bounded by (0,2,2,2), so the same height-ten theorem applies.
A possible filtration-degree-minus-one direction is also recognized by
that theorem's separate first case.

Consequently an unrecognized nice sliced action in this frame must have
\[
\operatorname{rank}J=2,\qquad\operatorname{rank}J^2=1,\qquad
G_1=0,\qquad\dim G_2\in\{0,1\}.
\tag{5}
\]
Indeed, J^2=0 would make every direction good, and the only nilpotent
partition of four with J^3=0 and J^2 nonzero is (3,1). In a constant
basis adapted to G_2, the two remaining profiles are exactly
(1,2,2,2), of displayed height eleven, or (2,2,2,2), of displayed
height twelve. These are bounds in the nice frame, not statements about
the minimum over all polynomial frames. They are necessary residual
conditions, not claims that a nonpolynomial example exists.

The rank-exclusion note supplies an exact recognized action with
\(\dim G_2=1\). Therefore rank one of J^2 over the fraction field
does not produce two constant good directions. Rational row reduction
cannot replace a justified polynomial coordinate change.

Further already recognized cases remain excluded: any actual invariant
coordinate, any slice of degree at most two, and any nonzero constant
row \(\lambda\) for which \(\lambda P\) is constant. These are
recognition gates, not assumptions to insert without proof. In particular
absence of a linear invariant alone does not identify a hard example.

## 4. An actual control for the indispensable original slice

There is a simple countercontrol to dropping the slice from (3). In
coordinates (x,y,z,w), put
\[
q=y-xz,\quad g=w-xq,\quad
E_0=\partial_x+z\partial_y+q\partial_w,\quad E=gE_0.
\tag{6}
\]
The original E_0 is nice and E_0g=0, so E is also an actual nice LND.
Every coefficient of E is divisible by the nonunit g, hence it cannot
have a polynomial slice. For its coefficient column P and Jacobian J,
direct polynomial calculation gives
\[
J^3=gP e_z^{\mathsf T}\ne0,\qquad J^4=0,
\qquad \operatorname{ad}_E^3\partial_z=-6gE\ne0.
\tag{7}
\]
The ranks of J,J^2,J^3 are respectively 3,2,1. This realizes the
excluded configuration when the slice assumption is absent.

On B_g there is a local slice x/g, but \(\partial_zg=x^2\ne0\).
Thus the original coordinate partial is not locally nilpotent on B_g:
an LND of a domain kills every unit. Applying the vertical lemma there
would violate its other LND hypothesis. The complete calculation and
exact controls are in Section 5 of the rank-exclusion note. This is not
a cancellation counterexample or a claim of historical novelty.

## 5. Explicit inverse certificates without a universal reduction

The general slice projection \(\pi(x)=\Phi_{-s(x)}x\) already
gives four invariant generators, not automatically three coordinates.
This pass constructs actual two-sided inverse maps in the following
specified families. All degrees are ordinary total degrees in the
specified actual input and output coordinates.

| Sufficient input | Forward degree | Inverse degree | Proof |
| --- | --- | --- | --- |
| Affine-linear E and supplied slice degree at most d | max(4,d) | 4d | [Affine construction](affine-slice-degree-bound-pass74.md) |
| Actual slice projection of degree at most two | 2 | 4 | [Quadratic projection](quadratic-slice-projection-pass74.md) |
| Complete projection Lx+H_m after an actual affine change at a fixed point, with only one nonlinear homogeneous degree m | m | m+(N-1)(m(e-1)+1) | [Single-layer projection](single-layer-slice-projection-pass74.md) |

For the last row, e≥1 bounds coefficient degree and E^N x=0.
The full idempotence identity forces the image to be a polynomial graph;
comparison with the original slice ideal and the actual flow proves both
inverse orders. The quadratic case is already a recognized low-degree-slice
family. Its added content here is a quantitative inverse construction.
No optimality or regular parameterwise choice is asserted for these bounds.

A polynomial retract by itself does not justify this promotion. The
quadratic note retains \(\rho(u,v,w,t)=(u(1+t),v,w,0)\): its image
is a polynomial graph, but those image generators together with t are
not coordinates. It is not a slice projection of the required kind.

## 6. Next mathematical obligation

The deductions above narrow the nice subclass and supply checkable
coordinate certificates. They do not show that every sliced action can
be made nice, that (5) can always be repaired by nonlinear coordinates,
or that an arbitrary projection can be reduced to one homogeneous layer.
A reduction to a recognized certificate family must retain
the original polynomial ring and supply actual coordinate inverses.
Automatic rank, formal splitting, local slices and bounded generators
do not fill that gap.

The unrestricted objective is still (1). The
[pass74 audit](proof-audits-pass74-working.md) separates written
deductions, external theorem dependencies, finite controls and file
integrity; the [checkpoint](checkpoint-pass74-working.json) records
their exact scope. No complete solution is asserted.
