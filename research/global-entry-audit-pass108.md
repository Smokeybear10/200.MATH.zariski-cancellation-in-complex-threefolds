# The actual coordinate frame remains the first global entry gate

The current mixed-fiber exclusions do not yet begin with an arbitrary
polynomial cylinder. They begin with a supplied polynomial coordinate
frame whose orbit degrees have a particular small shape. Producing that
frame, or a recognized alternative, is the first unproved reduction on
this route from cancellation to the local calculations.

This is a dependency and prioritization audit, not a new recognition
theorem or a new obstruction. It updates the retained
[global-reduction audit101](global-reduction-audit-pass101.md) through
the current108 unit-second-image exclusion.

## 1. What the unrestricted input actually supplies

The working cancellation input supplies
\[
B=A[u]\simeq\mathbb C^{[4]},\qquad
E=\partial_u\in\operatorname{LND}(B),\qquad
\ker E=A,\qquad Eu=1.
\tag{1}
\]
Thus E is an actual polynomial locally nilpotent derivation with a
polynomial slice. The slice theorem is already built into (1).
It does not say that u is an ambient polynomial coordinate: that
conclusion would identify its quotient A with a polynomial three-ring.
Finite generation and regularity of A are retained consequences of
the cylinder, not a substitute for that identification.

The present local route instead starts by supplying genuine polynomial
coordinates, with a polynomial inverse, satisfying
\[
B=\mathbb C[x_1,x_2,x_3,z],\qquad
E^2x_i=0\ (1\le i\le3),\qquad
E^2z=q\in\mathbb C^*,\qquad u_c=Ez/q.
\tag{2}
\]
The canonical slice in (2) may differ from the slice initially chosen
in (1); both have kernel A. No retained argument supplies (2) for
every action in (1). The required witness is an actual coordinate
tuple, not a proposed tuple with an unproved inverse, a rational
change of variables, or a basis change over an invariant subring.

Given (2), [frame87](constant-acceleration-three-good-frame-pass87.md)
proves the quadratic-in-time flow and the original Jacobian identities.
Those identities are consequences of the actual frame, not a proof of
its existence. The [intrinsic-plane construction88](constant-acceleration-invariant-plane-pass88.md)
then supplies the particular invariant plane and relative generators
used below. Its completion of a unit speed row over that plane must
not be reinterpreted as an ambient polynomial coordinate change.
Some leading-derivation or invariant-plane constructions can have
broader applicability; this audit does not identify the bare existence
of a plane with the missing gate. The missing gate is the actual
low-time-degree coordinate structure and its resulting bounded
relative generators.

## 2. The further restrictions before the mixed local sector

The chain after (2) has several distinct branches.

| Stage | Established output or additional restriction |
| --- | --- |
| Speed geometry | [89](homogeneous-speed-recognition-frontier-pass89.md) recognizes the homogeneous speed branch. The nonconical branch retains the intrinsic plane S, the actual generators, and a nonzero determinant Omega. |
| Relative presentation | [90](nonconical-cubic-relation-pass90.md) bounds the degree of the relative plane relation by three. [91](nonconical-linear-relation-recognition-pass91.md) recognizes degree one. The current quadratic program takes relative degree two; relative degree three is another branch. |
| Closed exceptional fiber | The later quadratic results restrict the possible fibers. The present calculation selects a mixed multiplicity-(2,1) fiber and requires the speed normal L(m) to be nonzero. |
| Whole-fiber structure | Under those hypotheses, [98](quadratic-normal-companion-collapse-pass98.md) forces the simple companion to collapse too, and [99](quadratic-whole-plane-fiber-pass99.md) gives the actual whole nonreduced fiber presentation. |
| Degree-module image | [107](mixed-full-artin-quartic-exclusion-pass107.md) excludes the full three-dimensional second-degree image. [108](mixed-unit-second-image-exclusion-pass108.md) excludes the unit normalized second-image ideal in the remaining rank-two image branch. |

In particular the last two rows concern
\[
R=S_m,\qquad
A_R/\mathfrak mA_R=\mathcal D[c],\qquad
\mathcal D=\mathbb C[G]/(G^2(G-1)),\qquad
\mathcal W_2=\operatorname{span}_{\mathbb C}\{1,\bar G\},
\quad \mathcal W_1=\mathbb C.
\tag{3}
\]
Here the Wj are actual images of degree modules in the entire
nonreduced fiber. Their dimensions are not asserted for an arbitrary
flat algebra or arbitrary sliced action. The unit-ideal exclusion
leaves a proper maximal-primary complete intersection as the
normalized second-image ideal; the independent
[proper-case jets108](mixed-proper-second-image-jets-pass108.md)
impose further conditions without excluding every such ideal.

Closing this mixed sector would not itself address every closed
quadratic fiber, including the other retained normal-direction
sectors, or prove global polynomiality from the remaining fibers.
Even a complete quadratic-branch recognition would leave the relative
cubic branch. Even a complete theorem under (2) would still need the
entry from (1), unless an independent global recognition argument
replaced it. The [107 frontier](mixed-full-artin-exclusion-frontier-pass107.md)
keeps these distinctions; the present audit does not promote local
restrictions to any of these larger conclusions.

## 3. What the retained recognition theorems do not supply

The [universal-frame audit52](universal-frame-reduction-audit-pass52.md)
and [coordinate-degree audit58](coordinate-slice-degree-scope-pass58.md)
already identify the difference between a supplied frame and a
universal minimizing-frame theorem. Their historical height bounds
must be read with [height-ten closure73](height-ten-closure-pass73.md):
recognition for the supplied adjoint-frame profiles through height
ten is established, but a universal minimum-height bound is not.
Adjoint height, time degree in (2), relative relation degree in90,
and ordinary degree in the supplied coordinates are different
quantities. None can silently replace another.

There is also a recognized endpoint that avoids this particular frame:
an actual invariant ambient coordinate. Bhatwadekar, Gupta and
Lokhande, Theorem 3.5, treats a nonzero LND on a polynomial four-ring
fixing an ambient coordinate and having regular kernel, and concludes
that the kernel is polynomial over that coordinate ring. Its short
proof uses a DVR proposition and PID patching. Regularity is available
in (1); the theorem does not supply the invariant coordinate.
The complete displayed statement and short proof were freshly read
for this audit, not their deeper dependencies.
[*Some K-theoretic properties of the kernel of a locally nilpotent derivation on k[X1,...,X4]*, Theorem 3.5](https://arxiv.org/html/1501.01438v1).

This bounded source check supplies no theorem filling the entry gate.
It is not an exhaustive claim that no such theorem exists in the
literature, nor a new audit of the deeper source dependencies.

## 4. The exact search boundary and the priority consequence

The already proved [101 control](global-reduction-audit-pass101.md)
also rules out a dimension-only ordinary-degree cutoff for finding a
first witness. For each k at least two, its four successive shears
start with coordinates u,a,b,c and have the exact inverse
u=x4-x3^k, a=x1-u^k, b=x2-x1^k, c=x3-x2^k. The distinct base-k
leading orbit weights prove that every nonconstant polynomial of
ordinary degree less than k has E-degree at least k. This covers all
coefficients and all polynomials in that range, not sampled ansatzes.

Nevertheless its kernel is explicitly C[a,b,c], and an adapted frame
satisfying (2) is explicitly available. Thus it obstructs a fixed
spatial search cutoff, not frame existence, a universal adjoint-height
bound, or cancellation. This is reused evidence, not a new108 result.

The global lane therefore still needs an actual degree-adaptive
witness theorem, a justified terminating change of frame, or a
recognition argument that does not require that witness. The local
mixed-fiber lane can narrow the consequences of (2), but those
deductions should not be counted as supplying its universal entry.

## Reading and verification scope

This audit used the current README entries and the complete retained
52,58,73,87,88,89,90,101 and107 frontier notes, plus the relevant exact
definitions and the current108 unit and proper-case proofs. The
selected91 and98 dependency passages were read for their stated
local hypotheses, not recorded as new complete primary-source audits.
The Bhatwadekar--Gupta--Lokhande statement and short proof are the only
fresh primary recognition read here. No numerical method, checker
execution, new theorem, or file edit through107 is part of this note.
Independent AI reconstruction is not expert or formal certification.
