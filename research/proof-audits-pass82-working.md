# Proof and evidence audit for the rank-one speed scheme

This working pass proves exact divisorial and dimension-dependent
acceleration bounds under the original rank-one quadratic hypotheses.
It does not prove q belongs to the full speed ideal in every case,
recognize every rank-one action, or solve general cancellation.

The preceding check-in turn completed independent proof reviews,
corrected ambiguous ground-field notation, and recorded the review
status in the ambient-bound note. It therefore made progress in
authoritative state, despite also answering a status question. This
continuation completes the evidence packet, without changing the
unrestricted goal or claiming an external blocker.

## 1. Written proof reconstructions

The [divisorial note](rank-one-acceleration-divisorial-ideal-pass82.md)
has nine numbered equations. General wrote the complete reduction;
Root supplied and independently checked the full-gcd extension.
Geometry and Jet each read the whole saved note and reconstructed
its argument. The checks retain prime multiplicities, separate gcd
one from a Bezout identity, and handle the zero and unit ideals.
The original slice is used to cancel only a proven unit modulo I
or J. The result is q in gB and the equivalence between q in I
and primitive divergence in J, not automatic membership in J.

The [quotient note](rank-one-speed-quotient-pass82.md) has nine
numbered equations. Geometry wrote it, Root supplied the direct
derivative-injectivity proof, and General and Jet independently
read and reconstructed the complete saved text. The identity of
embedded invariant rings is obtained from two derivations on the
same quotient, not cancellation of an unknown polynomial factor.
The finite Catalan inverse keeps all nilpotents. Its abstract examples
are explicitly not ambient four-variable realizations.

The [ambient-bound note](rank-one-ambient-nilpotence-bound-pass82.md)
has nine numbered equations. Root derived and wrote the argument.
General, Geometry and Jet each independently reconstructed it through
EOF. Both derivative containments in its equation (3) are needed to
reduce the last column of the actual flow Jacobian. No entry of the
bottom-left block is set to zero. Coefficient comparison proves the
n-variable bound without cancelling a zero divisor. The characteristic
polynomial and Cayley--Hamilton assertion hold modulo I only.

The notation 'over C[t]' in the flow paragraph was clarified to the
complex ground field rather than the quotient ring C. This was a prose
ambiguity, not a changed determinant computation. The displayed result
is q to the fourth power in I for dimension four; sharpness and the
existence of a nonzero residual acceleration are not asserted.

These are coordinated, separate AI proof reconstructions. They are
not independent human referee reports, a formal prover certificate,
or a determination of historical novelty.

## 2. Primary-source read and its effect

Root read the complete eight-page author-hosted Berson, van den Essen
and Maubach Report 9918, including references. Jet separately read
the retained complete text and opened the original URL. The
[source-boundary note](nonreduced-divergence-source-boundary-pass82.md)
has three numbered equations; Jet independently reconstructed all
three and audited the exact hypotheses of property B(R) and Theorem
3.7. Its relative-plane and zero-divergence premises are not removed
by the presence of a slice or a unit coefficient ideal.

This source check excludes a circular application: in the quotient
used here, relative zero divergence is equivalent to the desired q
membership itself. The domain proof about polynomial units cannot
be transferred unchanged to a nonreduced coefficient ring. The
primary PDF and pdftotext extraction have separate SHA-256 records.
No claim is made to have independently reproved all earlier theorems
cited by that source, inspected its later journal version, or completed
a novelty audit.

The deep-research workflow led to this exact applicability boundary
and a durable primary-source record. It did not supply a recognition
theorem for the original four-variable action.

## 3. The four finite exact methods

Jet wrote the standalone
[checker](rank_one_speed_checks_pass82.py), which imports only
unittest and SymPy. Root and Geometry independently read the whole
checker, its [controls note](rank-one-speed-controls-pass82.md),
and its [print-only runner](run_targeted_pass82.py). They check
explicit polynomial inverses and identities, not solver output.

The first method constructs an actual nonprincipal speed ideal,
checks the original transported slice and iterates, proves both
Groebner ideal containments, and verifies membership and divergence
in that example. The second checks a retained principal Nagata frame,
including q in I but not I squared. The third checks finite Catalan
inverses and unit speeds in five nonreduced quotient rings. The
fourth checks the formal four-by-four block determinant, its coefficient
recurrence, and a companion matrix identity. It does not realize that
matrix as an actual velocity Jacobian.

There are exactly four unittest methods, not nine: the five nilpotence
orders are subtests of one method. Formal matrices are not ambient
actions. Quotient examples of order at least five violate the written
ambient bound, and the other orders are not thereby realized.

The first author run passed in 0.277 seconds, tool chunk 6fa0a4.
Root's separate direct run passed in 0.284 seconds, chunk 1e4b61.
The canonical [targeted capture](verification-pass82-working.json)
then passed all four methods in one suite, in 0.287 seconds of unittest
time and 0.501625 seconds of monotonic wall time, chunk ca8161.
General separately read the checker, controls and runner through EOF,
then ran only the checker: four methods passed in 0.297 seconds,
chunk ced551. Geometry's code review did not execute a suite.
Its timestamps are 2026-09-14T09:43:14.203050+00:00 through
2026-09-14T09:43:14.705090+00:00. All three tracked inputs stayed
unchanged, and its complete output and output hash are retained.

Checker SHA-256:
4e05c14b45bc1a8bbcba46fdb7df50fed205672858525ad4d63ad9a5aee19a5c.
Runner SHA-256:
42e3b02803936cd7e92129c9ff71ba1b65ca91b98e7be23ebbc38cc5d706ea78.
There was no mathematical test failure in these recorded runs. Repeats
do not add methods. No new full regression is claimed.

## 4. Bounded actual-frame search and corrected classification

The [search script](rank_one_speed_search_pass82.py),
[scope note](rank-one-speed-search-scope-pass82.md), and
[complete capture](rank-one-speed-search-evidence-pass82.json)
are separate from the unit tests. Root read the entire script and
scope note, checked the inverse mechanisms of the seeds and elementary
moves, and replayed the initial 3,000 attempted candidates. All scientific
counts matched the classified capture: 1,670 accepted frames, 697
rank-one profiles, 141 proper-ideal membership checks, of which 140
were genuinely nonprincipal, over 24 distinct nonprincipal ideal
representations. The replay's algorithm wall time was 6.851331 seconds,
tool chunk a91ebc. It was a repeated candidate set, not a new search.

The earlier inline count named nonprincipal was only a gcd-based
screen. The exact primitive-ideal test corrected this before the saved
evidence packet. Root independently confirms the classification rule:
in a polynomial UFD, I=gJ is principal precisely when its primitive
generator ideal J is the unit ideal. This is checked by exact Groebner
reduction, not by requiring an individual constant generator.

Only one broader candidate batch was run: 1,239 attempts, 687 accepted
frames, 244 rank-one profiles, sixteen proper membership checks,
eleven genuinely nonprincipal checks and seven distinct nonprincipal
ideal representations. The 35-second between-attempt cap allowed the
last symbolic operation to finish at 41.971650 seconds. No strict
per-operation timeout or complete exhaustion is claimed. Root did not
rerun that broader batch in this integration.

All tested remainders were zero. The two batches can overlap; distinct
counts are not summed across them. This finite failure to find a
counterexample is not a proof of q in I. Search candidates add zero
unittest methods. The raw outputs parse exactly to their saved records
and carry the current script hash.

## 5. Integrity, dependencies and remaining work

The [synthesis](rank-one-speed-frontier-pass82.md) has four numbered
equations and distinguishes all the preceding scopes. Its theorem
count is not inferred from passing examples. Jet independently read
the full synthesis and canonical capture and found no scope inflation.
The new research notes
contain 34 numbered equations in total; controls, search records and
this audit add no numbered theorem equations.

The fresh predecessor check at 2026-09-14T09:37:33.382Z passed all
393 retained hash records through81. It also checked nine full75
source hashes and six retained successful outputs. The central
historical registry remains 544 claims. The unchanged last full75
record remains 146 suites and 1047 methods. Its successful record is
not described as a newly executed full82 run.

The final [checkpoint](checkpoint-pass82-working.json) records current
artifact hashes, equation numbering, local-link path checks, targeted
scope and the final predecessor audit. Link-path existence does not
validate anchors or mathematical claims. Mutable README and ledger
indexes are intentionally excluded from the frozen historical hashes.

General q membership, simultaneous polynomial reduction, arbitrary
rank-one recognition and unrestricted cancellation remain unresolved.
The professor's intended correction, field and dimension remain
unconfirmed. No historical novelty certification, human expert review,
formal verification, external contact, public posting or submission
occurred. Future investigations are not silently included in this
frozen pass's conclusions or its four-method count.
