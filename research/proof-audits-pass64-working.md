# Working proof and source audits after actual graph recognition

The principal new result is the conditional recognition theorem in
[pass64](actual-quadratic-graph-cancellation-pass64.md). It proves that
the original kernel is a polynomial three-ring under the full actual
independent-defect quadratic-graph assumptions. It does not establish
the frame assumptions for arbitrary sliced derivations.

This record distinguishes mathematical reconstruction, symbolic
controls, source applications, and file consistency. None is presented
as human expert review or formal proof-assistant verification.

## 1. Square-speed proof and exact controls

The main agent read the complete final
[square-speed proof](square-speed-schur-generation-pass61.md),
the complete [leading-determinant note](square-speed-leading-determinant-pass61.md),
and its [one-method checker](square_speed_leading_checks_pass61.py).

The complete Schur determinant aligns all graph coefficient vectors,
not only their quadratic leading terms. For independent odd quartics,
the actual coordinate field would force degree one for a rational
function whose poles have total degree at least four. In the other
two odd ranks, actualness is used before claiming regularity of a
potential or constant term. The final rank-zero case uses the original
arbitrary slice on the whole localized polynomial ring.

The affine author and the jet and geometry reviewers each reconstructed
the complete square-speed proof. Both separate full-file reviewers
returned clean verdicts. The final source file records those reviews
and preserves the exact global square-speed scope.

The [captured root run](verification-pass61-working.json) at
23:03:27–23:03:28 UTC passed the one checker method in 0.183 seconds.
Additional scratch equalities verified both odd quartic derivatives,
their combined quadratic expression, the direct full base Jacobian,
its determinant and both inverse orders, and the sign involution.
Those scratch identities add no test-method count. The sign-invariant
rational example fails actual coordinate-field generation and is not
a full-frame realization.

## 2. Weighted monomials and actual local parameters

The main agent read both complete pass62 notes.

The [global monomial proof](monomial-speed-exclusion-pass62.md)
proves exact exponent gcd at most two. Its Bezout Laurent monomial
gives the actual field \(k(r,z)\), rather than silently identifying
the powered parameters with polynomial coordinates. The jet agent
read the entire proof and independently reconstructed every rank.
A later stronger theorem supersedes the exponent restriction;
it does not make the earlier proof false.

The [normalization note](ramified-normalization-scope-pass62.md)
proves the rational weighted-Euler kernel statement for actual local
regular parameters. The main agent reconstructed its weighted
initial-form argument: a nonzero invariant fraction has order zero;
subtracting its initial homogeneous ratio would leave an invariant
fraction of positive order, which is impossible. This works without
assuming that the local parameters generate the whole actual field.

The note's formal-root control is intentionally different. The unit
in \(a^2(1+a)\) has no square root in the original fraction field,
despite admitting formal and etale roots near the origin. Its
valuation at \(a+1\) is odd. This does not produce an actual sliced
full frame or a cancellation counterexample.

The affine agent read the full normalization note and the selected
complete primary sources independently, with a clean verdict.
The main agent also freshly read Stacks Tag 07NM, its full statement
and proof; Tag 00UB's definition; and the full standard-etale proof
following Definition 59.26.3 in Tag 03PA. These support only the
parameter change and root-cover descriptions. The weighted rational
argument itself is supplied in the note.

## 3. Rational Euler graph rigidity

The [pass63 theorem](rational-euler-graph-rigidity-pass63.md) allows
arbitrary finite polynomial graph support, not merely quartics.
The new pole argument was developed by the main agent and separately
reconstructed by the affine and jet agents before writing.
The jet, geometry, and affine agents subsequently each read the
complete saved proof and reconstructed all 22 equations.

Its actual ring-intersection hypothesis is essential to the stated
constant-direction contradiction. The proof does not infer a
polynomial invariant is constant before using that hypothesis.
For the positive monomial application, positivity supplies the
hypothesis, so every positive exponent pair is excluded.

Both the jet and geometry reviewers flagged one precise opening
word: transcendence degree alone gives an algebraic separable
extension, not immediately a finite one for an arbitrary base ring.
The main agent changed the wording to algebraic separable.
The proof only uses that property there. The jet agent checked the
correction, and the affine full-file audit read the corrected version.

All three full-file verdicts were clean after that clarification.
No general field-rationality theorem is asserted by this abstract
result: its constant-field premise remains explicit.

## 4. Recognition of the complete actual graph

The [pass64 theorem](actual-quadratic-graph-cancellation-pass64.md)
first proves that the Euler constant field has transcendence degree
one, then invokes the precise classical rationality input recorded
by de Bondt, Theorem 1.1. Thus its rational parameter is an element
of the unchanged actual field.

The nonconstant-direction pole contradiction never uses triviality
of the polynomial Euler-invariant ring. For a constant direction,
the difference
\[
I=Q_2-\rho Q_1-D(X,Y)
\]
belongs to the actual invariant plane. More importantly, it is an
ambient polynomial coordinate, with inverse
\(Q_2=I+\rho Q_1+D(X,Y)\). The original action kills it.
The known sliced Dedekind theorem then applies over \(k[I]\).

The alternative with no varying coefficients gives \(B=C[X,Y]\)
and an explicit affine slice and kernel directly. It does not
require the Dedekind theorem. Both branches retain the original
derivation and the original supplied slice.

The affine and jet agents independently read the complete saved
pass64 proof through EOF, reconstructed all 22 equations and both
source applications, and returned clean verdicts. Their source
audits were independent of the main agent's selected source reads.
The geometry agent independently reread the whole inherited pass44
proof and reconstructed the two-case coordinate argument. Its
separate supplied-profile dependency audit is not conflated with
a full pass64 file review.

The main agent reconstructed every inference in the written proof,
including the coefficient-field independence, the common pole
divisor, the genuine coordinate inverse, and the global-versus-local
distinction. No inference requires that an invariant-plane generator
be an ambient coordinate merely because it is an invariant.

## 5. Exact scope of the primary inputs

The main agent freshly read the retained de Bondt v4 primary text:
Theorem 1.1 and attribution on PDF page 4, and Theorem 3.1,
Corollary 3.2 and Lemma 3.3 with their complete printed proofs on
pages 19–21. The latter polynomial-intersection results were
investigated for a possible coprime-speed route but are not needed
by the stronger final pass64 proof.

Theorem 1.1 is a recorded classical statement with references to
earlier proofs. Neither the main agent nor the proof note claims
that de Bondt supplies its full proof in that passage.

The main agent freshly opened the Derksen, van den Essen and
van Rossum author-uploaded primary manuscript and read Theorem 4.4
and its complete proof, together with Corollary 4.5 and its proof.
The invocation in pass64 uses an actual invariant ambient coordinate
and the one-variable Dedekind base \(k[I]\). It is not cancellation
over the two-dimensional invariant plane.

The bounded web searches located this existing recognition input.
They are not a completed priority search or evidence of novelty.
The proof's source links and precise bibliographic scope are in
[pass64's Sources section](actual-quadratic-graph-cancellation-pass64.md#sources-and-verification-boundary).

## 6. Numerical and consistency evidence

The latest full numerical regression remains
[full60](../verification-pass-60.json): 1000 methods in 126 suites.
The previously missing [full60 consistency record](../consistency-pass-60.json)
was completed in this continuation, with 172 hash records and
an independent Node rehash. Its four shared metadata files are
historical snapshots and may change in later working stages.

The [latest captured standalone run](verification-pass64-working.json)
at 23:18:57–23:18:58 UTC reran the one new pass61 method successfully
in 0.178 seconds. Separate scratch equalities checked the generic
two-by-two rank-one determinant, the all-quadratic-coefficient
triangular coordinate Jacobian and both substitutions, and both
unimodular affine inverse orders.

There is still only one new method in one new suite after full60.
Repeated executions and scratch assertions are not extra methods.
No full61–64 regression is claimed. The written pole argument and
classical source inputs are not established by these symbolic tests.

The main agent also reran the three affected inherited suites for
the degree-two reduction, projection-rank closure, and full generic
graph. The [captured results](verification-pass64-inherited.json)
record twelve methods passing at 23:23:22–23:23:24 UTC, with
zero new methods or suites. Their original source files are unchanged.

The jet agent independently read this audit record, both final proof
tails, and all three captured verification records, finding their
provenance and counts consistent. It independently reran the new
square checker and the three inherited suites: respectively one,
five, three, and four methods passed in 0.189, 0.295, 0.220, and
0.341 seconds, all exit zero. These reruns add no distinct methods.

The previous status-only user turn was followed by substantive proof
work and saved evidence. The active objective remains the original
cancellation problem. Neither the conditional theorem, these AI
audits, nor an integrity checkpoint is substituted for its solution.
