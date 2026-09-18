# Nonconical volume identities and a constant-determinant recognition criterion

The nonconical three-good-coordinate case now has an exact open-set
reduction, a relative equation of degree at most three, and a
fixed-point-free intrinsic additive action on that open set.
When the velocity determinant is a nonzero constant, the action is
global and an established theorem identifies the kernel with affine
three-space. A nonconstant determinant still leaves exceptional
fibers to analyze.

This is a restricted result, not a solution of the general cancellation
problem. The working target remains the unconfirmed interpretation
\(A[s]\simeq\mathbb C^{[4]}\Rightarrow A\simeq\mathbb C^{[3]}\).
The original email did not confirm this field, dimension, or correction
to its dimensionally inconsistent conclusion.

## 1. Precise setting

The present arguments require original polynomial coordinates and an
actual complex locally nilpotent derivation:
\[
B=\mathbb C[x_1,x_2,x_3,z],\qquad
E^2x_i=0\ (i=1,2,3),\qquad E^2z=q\in\mathbb C^* .
\tag{1}
\]
The element \(u=Ez/q\) satisfies \(Eu=1\), so \(B=A[u]\) for
\(A=\ker E\). The
[actual invariant-plane construction88](constant-acceleration-invariant-plane-pass88.md)
produces a nonzero commuting intrinsic LND W with
\(Wu=0\), \(S=\ker(W|A)=\mathbb C[s_1,s_2]\), and
\(b=(Ex_1,Ex_2,Ex_3)^t\in S^3\).
The speed row generates the unit ideal in S.

Define
\[
\Omega=\det[b,b_{s_1},b_{s_2}]\in S .
\tag{2}
\]
This investigation treats \(\Omega\ne0\). The previous
[homogeneous-speed proof89](homogeneous-speed-recognition-frontier-pass89.md)
handles the separate homogeneous-relation case. No argument yet
puts every sliced derivation of a polynomial four-ring into (1).
Closing every case under (1) would therefore still leave a separate
reduction obligation for unrestricted cancellation.

The actual completed speed row gives relative generators
\(R=S[A_1,A_2]\subset A=R[c]\). These are equalities of
subalgebras, not declarations that the relative generators are
algebraically independent.

## 2. How the volume coefficients change the problem

The original coordinate volume is invariant under the E-flow.
After centering the original coordinates at u, all its positive
u-coefficients vanish. Its constant coefficient is a unit.
The distinct consequences are:

| Coefficient or identity | Exact consequence | Remaining limitation |
| --- | --- | --- |
| Cubic coefficient, retained88 | A normal relation and \(\Omega h\in R\) | Division by \(\Omega\) is only local |
| Quadratic coefficient | A symmetric quadratic potential recovers c, giving \(A_\Omega=R_\Omega\) | Does not cross \(\Omega=0\) |
| Linear coefficient | A closed polynomial one-form gives a cubic relation | The generic coordinate may have base denominators |
| Constant conormal coefficient | A unit pair gives a fixed-point-free intrinsic LND on \(A_\Omega\) | A free action on this principal open is not a global action on A |
| Cubic relation plus unit pair | Unit relative gradient and smooth relative curve morphism | Smooth fibers can be geometrically disconnected |

The full
[quadratic proof](nonconical-quadratic-potential-pass90.md)
uses the moving basis \([b,b_{s_1},b_{s_2}]\) to express the
centered good coordinates by two invariants \(y_1,y_2\).
An explicit symmetric quadratic form recovers the centered fourth
coordinate. Contraction with the actual W-kernel removes the auxiliary
local-slice denominator. The result is
\[
A_\Omega=R_\Omega=S_\Omega[y_1,y_2].
\tag{3}
\]
The preliminary finite unramified normalization is retained only as
a [superseded weaker argument](nonconical-unramified-normalization-pass90.md),
with an algebra-only node showing why that weaker argument did not
already prove (3).

The [cubic proof](nonconical-cubic-relation-pass90.md) uses
equality of the third mixed derivatives of b to show that the
remaining polynomial one-form is closed. Its potential has degree
at most three in the two relative variables. It gives a nonzero
multiple of the defining hypersurface relation. A change between
two bases of rows annihilating b transfers the bound to the
original relative ring R:
\[
R\simeq S[T_1,T_2]/(F_0),\qquad
1\le\deg_{T_1,T_2}F_0\le3 .
\tag{4}
\]
Over \(K=\operatorname{Frac}(S)\), the actual intrinsic local slice
gives \(A_K=K[v]\). An elementary degree argument then shows that
some K-linear combination of \(A_1,A_2\) generates this polynomial
ring. The only problematic low-degree pair, degrees two and three,
would give either a common critical point or two different geometric
points with the same generator values. Both contradict the actual
polynomial recovery of v.

The [free-derivation proof](nonconical-open-free-derivation-pass90.md)
uses the actual conormal sequence to obtain a unit, not merely a
nonzero generic determinant. The resulting derivation D has
\[
\ker(D|A_\Omega)=S_\Omega,\qquad
D(A_\Omega)A_\Omega=A_\Omega,\qquad
\operatorname{Spec}A_\Omega\longrightarrow
\operatorname{Spec}S_\Omega\ \text{smooth of relative dimension one}.
\tag{5}
\]
Local nilpotence is checked separately: on \(K[v]\), the unit
coefficient ideal forces D to be a nonzero constant multiple of
\(\partial_v\). The cubic relation and the same unit pair give
a unit relative gradient. The smoothness deduction uses the
standard split-conormal hypersurface criterion.[^smooth]

## 3. A recognized nonconical subcase

If \(\Omega\in\mathbb C^*\), no localization is needed in (3)--(5).
The new D is a fixed-point-free LND of A itself. The cylinder
\(\operatorname{Spec}A\times\mathbb A^1\simeq\mathbb A^4\)
makes \(\operatorname{Spec}A\) a smooth contractible affine
complex threefold. Its D-quotient is the actual affine plane
\(\operatorname{Spec}S\).

Kaliman--Saveliev Corollary 2.8(1) identifies a smooth contractible
affine complex threefold with a free additive action as the
translation product of its quotient and an affine line. It has
no further properness or retraction hypothesis.[^ks] Hence
\[
\boxed{\quad
\text{under (1) and the actual invariant-plane construction, }
\Omega\in\mathbb C^*
\ \Longrightarrow\ A\simeq S[t]\simeq\mathbb C^{[3]} .
\quad}
\tag{6}
\]
The [constant-determinant proof](constant-omega-recognition-pass90.md)
records the exact applicability checks. The published free-action
theorem is an input, not a new result claimed here.
Whether this restricted recognition criterion already follows
from other literature remains unverified.

## 4. Global constraints and exact obstructions

The [cyclic-fiber proof](nonconical-cyclic-fiber-omission-pass90.md)
shows that \(E,\partial_z,[E,\partial_z]\) and its next E-bracket
are independent over the original rational-function field.
Consequently E and the original last partial have no common
nonconstant rational invariant.

Combining this with the universal tensor-pencil identity excludes
collapse of both relative generators on any whole generic divisor
fiber of S. At least one remains transcendental over the base
residue field. This does not prove that pR is prime or that all
components of an R-fiber are hit by \(\operatorname{Spec}A\).

Two controls keep the remaining implications honest.
The [actual polynomial inverse-frame example](nonconical-higher-commutator-control-pass90.md)
has a locally nilpotent highest E-adjoint H but a non-locally-nilpotent
bracket \([\partial_z,H]\). Another bracket is locally nilpotent
but does not preserve A. The example is already recognized by an
original coordinate slice; it is not a cancellation counterexample.

The [source audit, Section 5](homogeneous-speed-recognition-source-scope-pass90.md)
localizes a standard Weitzenbock action. It has a smooth factorial
total space, a fixed-point-free intrinsic LND and a quadratic relative
equation, but a base divisor has a nontrivial quadratic residue-field
extension. Thus these abstract open-set properties do not imply a
relative polynomial line or section. This control does not realize
the additional original-frame identities. It also cannot refute
(6), because its localized total space is not supplied as a
contractible cancellation threefold.

## 5. Verification and evidence limits

The proof notes distinguish written universal arguments from finite
symbolic checks. The
[targeted capture](verification-pass90-working.json) passes two
methods: one verifies an actual polynomial inverse and its commutators;
the other checks a formal determinant coefficient and symmetric
quadratic potential. They import no research solver or older checker.
They do not verify the arbitrary-ring, quotient, cubic-degree or
recognition arguments.

Independent AI reconstructions cover the saved mathematical arguments.
They are not Lean proofs or human expert review. Five literal missing
plus signs in the first saved cubic note were found in full-file
reads and corrected before the clean final reviews. There is no
claim of a flawless first draft.

No full regression or exhaustive action search ran. Historical
regression and claim-registry counts are retained rather than
inflated with repeat executions. The
[proof audit](proof-audits-pass90-working.md) and
[checkpoint](checkpoint-pass90-working.json) separate these records.
The primary-source comparison is bounded and inconclusive on novelty.
No expert contact, public posting, submission or publication occurred.

## 6. Next mathematical obligations

For a nonconstant \(\Omega\), extending the free localized action
across \(\Omega=0\) may introduce fixed points. The next proof task
is to use the degree-at-most-three relation and actual coefficient
identities to control those divisors, not to assume a generic
coordinate extends or that a free action on an open set is globally
free. The whole-divisor noncollapse constraint is available there.

Independently, the full target still needs a route from arbitrary
sliced actions to this frame, or a broader argument that avoids
the frame. The general conjecture is unsolved and the goal remains
active. Human review, formal verification, and novelty determination
are separate outstanding obligations.

## Sources

[^smooth]: The Stacks Project, [Smooth ring maps, tag 00T1](https://stacks.math.columbia.edu/tag/00T1), opening hypersurface calculation and Definition 10.137.1. The application uses the unit-gradient split-conormal criterion, not a classification of affine-line fibrations.

[^ks]: Shulim Kaliman and Nikolai Saveliev, [*C+-actions on contractible threefolds*](https://www.math.miami.edu/~kaliman/library/KaSa.michigan.2004.quotient.pdf), Corollary 2.8(1), printed page 6. Its statement and complete displayed proof were freshly read. The invoked earlier free-action theorem and topology dependencies are inherited published inputs, not new independently formalized proofs.
