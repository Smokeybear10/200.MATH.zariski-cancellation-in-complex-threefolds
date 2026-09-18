# Recognition of nice sliced actions on complex four-space

Every nice locally nilpotent derivation on the complex polynomial
four-ring with a global polynomial slice has polynomial kernel.
The supplied-good-direction assumption of the preceding result is
no longer needed. This is a written working theorem, subject to the
proof-review record, not a human-reviewed or formally certified result.

The general complex-threefold cancellation conjecture is not solved.
An arbitrary cylinder presentation gives a sliced action but does not
currently give a nice polynomial coordinate frame.

## 1. Exact statement

Let B=C[x_1,x_2,x_3,x_4], and suppose
\[
E\in\operatorname{LND}_{\mathbb C}(B),\qquad
E(s_*)=1,\qquad E^2(x_i)=0\quad(1\le i\le4).
\tag{1}
\]
Then
\[
\boxed{\ker E\simeq\mathbb C^{[3]}.}
\tag{2}
\]
In particular there are actual polynomial coordinates (a,b,c,s_*)
of B in which E is the derivative with respect to s_*.
There is no bound on the ordinary polynomial degrees of E(x_i).
The field is C; the geometric quotient inputs are not being extended
here to arbitrary fields of characteristic zero.

## 2. Exhaustive proof by the actual Jacobian and cone

Put P_i=E(x_i), J=Jac_x(P), and A=ker E. The
[sliced rank theorem74](nice-slice-adjoint-rank-pass74.md) gives
J cubed zero and rank J at most two. If J squared is zero,
the retained all-double-adjoint recognition theorem applies, exactly
as in the first case of
[supplied-good recognition79](nice-good-direction-recognition-pass79.md).

Assume J squared is nonzero. Define the actual constant vector space
\[
G_2=\{v\in\mathbb C^4:J^2v=0\}.
\tag{3}
\]
If it is nonzero, choose any nonzero member. It supplies exactly the
constant good direction in recognition79, so that theorem gives (2).

It remains that G2 is zero. The
[no-apex cone theorem80](nice-no-apex-quadric-pass80.md) applies to
these same actual coordinates and slice. Its proof uses the published
GN-plane incidence theorem only after verifying the homogenized rank
and removing intersections with other zero-set components. The
projective incidence argument then proves that the velocity cone has
a nondegenerate homogeneous quadratic equation. Thus P satisfies
P transpose C P=0 for an invertible constant symmetric matrix C.

The [quadric recognition theorem80](nondegenerate-quadric-nice-recognition-pass80.md)
now gives (2), without choosing a good direction. Its actual common
invariant plane contains all velocities. The unimodular quadric
velocity has a global polynomial Segre frame, giving A=S[Y,Z]/(F).
The original coordinate-generation determinant makes F a Darboux
polynomial for an affine saddle derivation over Frac(S). The generic
fiber is a polynomial line, so the possible hyperbola is excluded and
F is affine-linear in Y,Z. Nonempty curve fibers force its coefficient
row to be unimodular over S, giving A=S[t]=C^[3].

These cases exhaust (1). Choose polynomial generators a,b,c of A.
The original slice theorem gives B=A[s_*], so (a,b,c,s_*) really
is a polynomial coordinate system of B. It is not only a rational
coordinate system or a coordinate system on a principal open.

## 3. A multiplicative-action consequence

For any nonzero integer N, the action that fixes A and sends
s_* to t to the power N times s_* is linear in the coordinates
(a,b,c,s_*). Equivalently, the multiplicative action associated
with the semisimple derivation N s_* E is linearizable in dimension
four under (1). This follows directly from (2) and the slice theorem.
The nearby linearizability criterion of Cid's preprint is a comparison
source, not a substitute for the quadric recognition proof.[^cid]

## 4. What has not been proved

The original working question is
\[
A[s]\simeq\mathbb C^{[4]}\quad\Longrightarrow\quad
A\simeq\mathbb C^{[3]}.
\tag{4}
\]
This remains an unconfirmed correction and specialization of Luo's
pasted email. He has not confirmed the intended field or dimension.
Transporting the derivative with respect to s gives E in LND(B)
and E(s)=1. It does not imply E squared kills the four polynomial
generators of B. Local nilpotence only says that some sufficiently
large iterate kills each generator. Replacing those generators by
a nice polynomial coordinate system is a genuine remaining problem,
not a consequence of local nilpotence or of this theorem.

The theorem also does not say every nice frame has a constant good
direction. The no-good case has been recognized, not excluded. Raw
normal cofactors may retain nonconstant content even though their
primitive quadric row is unimodular. No common slice or freeness of
an unnormalized intrinsic replica is required or asserted.

Thus a hypothetical nonpolynomial kernel with a polynomial cylinder
cannot possess any nice polynomial coordinate frame. The retained
general all-profile height threshold is unchanged. The old hypothetical
nice height-twelve case is no longer an open recognition case, but
no lower bound for every general frame is being silently raised.

## 5. Sources and verification boundaries

The source-dependent geometric input is de Bondt's Theorem 3.8(i),
with its exact hypotheses checked in the linked cone proof.[^bondt]
The common invariant-plane and flat-fiber input is the retained
application of Kaliman--Saveliev to the actual cylinder threefold.[^ks]
The coordinate-generation determinant uses the conormal exact sequence,
with its injective left map and basis checked for this hypersurface.[^conormal]
The explicit [Segre frame](quadric-segre-frame-pass80.md) uses only
UFD division and Bezout identities; a projective-module completion
theorem is not needed in that construction.

The [finite checker](normal_row_parameter_checks_pass80.py) addresses
formal matrix identities and parameter controls, not every theorem
hypothesis, the projective incidence proof, or all invariant curves.
A passing checker is therefore not a formal proof of (2) or (4).
The [proof audit](proof-audits-pass80-working.md) records independent
written reconstructions and the
[targeted capture](verification-pass80-working.json) separately.
Historical novelty and human expert
review remain unestablished. No message, submission or public claim
is authorized by this private working result.

[^bondt]: Michiel de Bondt, [*Homogeneous quasi-translations in dimension 5*](https://arxiv.org/html/1501.04845v3), arXiv:1501.04845v3, October 18, 2017, Definition 3.7 and Theorem 3.8(i). See the linked cone note for selected primary-proof reads and applicability.

[^ks]: Shulim Kaliman and Nikolai Saveliev, [*C+-actions on contractible threefolds*](https://www.math.miami.edu/~kaliman/library/KaSa.michigan.2004.quotient.pdf), Lemma 2.1, Theorem 2.7 and Corollary 2.8. Exact cylinder, domination and flatness gates are written in [the retained quotient proof](intrinsic-quotient-surface-pass.md).

[^conormal]: The Stacks Project, [Lemma 10.131.9, Tag 00RU](https://stacks.math.columbia.edu/tag/00RU). Its displayed proof was freshly read; injectivity in the present hypersurface is checked separately, not assumed in the general source statement.

[^cid]: Luis Cid, [*On nice Gm-actions arising from locally nilpotent derivations with slice*](https://arxiv.org/html/2604.03471v1), arXiv:2604.03471v1. The landing-page submission date is April 3, 2026, while the viewed HTML heading displays August 24, 2026. Theorem 5.4 is a linearization/conjugacy criterion; Section 6.4 does not supply universal four-variable nice recognition. The selected Lemma 5.3 and Theorem 5.4 proofs and Section 6.4 were read, not the entire paper's cited dependencies. This bounded comparison is not an exhaustive novelty audit.
