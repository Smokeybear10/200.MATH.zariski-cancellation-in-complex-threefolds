# Pass75 proof, source, and execution audit

This packet disproves a common-slice selection shortcut, gives exact
criteria for a complete explicit conic family, and isolates a
slice-independent primitive quotient test. A separate all-degree
argument excludes a triangular fixed-point candidate from the required
simultaneous nice/partial frame. None solves unrestricted cancellation.

The preceding user check-in polled a particular previously live exact
checker and received its successful completion, then reported status.
Conservatively it added no new root mathematical result. This
continuation revalidated the current files and completed new proofs,
independent reviews, applicability checks and a full regression.
The full objective and unconfirmed complex-threefold interpretation
remain unchanged.

## 1. Written mathematical arguments

| Artifact | Exact contribution | Independent AI review |
| --- | --- | --- |
| [Good-partial boundary](nice-good-partial-boundary-pass75.md) | Eight equations; the retained action's derived field need not be nice or fix the supplied slice. | Root and General read the full saved proof. Root also read its complete checker. |
| [Slice adjustment](good-partial-slice-adjustment-scope-pass75.md) | Seven equations; coefficientwise LND adjustment on A[s], exact iterate identity, arbitrarily high adjusted coordinate flow degree. | Root, Jet and General reconstructed the full saved proof, including both inverse orders of the degree family. |
| [Line-family and shear boundary](nice-good-direction-construction-boundary-pass75.md) | Sixteen equations; actual inverse criterion, constant good-direction tests, unbounded-degree single-shear classification and restricted two-shear obstruction. | Root and Jet read the full saved proof; no general good-direction existence follows. |
| [No common slice](nice-common-slice-obstruction-pass75.md) | Fifteen equations; a nice sliced action and its sole-good-partial derived action both have slices, but no slice for the first is invariant under the second. | Jet, Geometry and General independently reconstructed both inverse orders, both slices, the exact constant good space and the all-polynomial divisor obstruction. |
| [Conic-family criteria](conic-nice-pair-classification-pass75.md) | Fifteen equations; all coprime parameter pairs, derivative-ideal and common-slice criteria, constant boundaries, Bezout independence and primitive repair for every supplied slice. | Root, Jet and Geometry read the complete proof. Root also checked the final checker-link-only change. |
| [Primitive quotient test](primitive-good-quotient-scope-pass75.md) | Seven equations; canonical intrinsic gcd, exact wedge quotient ideal, independence from slice choice and the distinction from infinite saturation. | Root, Jet and General read the full proof. Root and General freshly read the retained intrinsic quotient argument and selected primary recognition statement. |
| [Triangular candidate obstruction](triangular-primitive-candidate-obstruction-pass75.md) | Twelve equations; actual inverse pair, primitive fixed line, all-polynomial calculation of the nice part of kerT, and exclusion of every T-coordinate nice frame. | Root and General reconstructed the full proof. Root also independently checked both inverses, transported fields and all seven coefficients of the general second-derivative operator symbolically. |
| [Frontier synthesis](good-partial-frontier-pass75.md) | Four equations; bounded results, exact next ideal test and unchanged unrestricted obligations. | Jet and General read the full original synthesis. Both requested an explicit nonconstant-pair qualifier before division by W; Root corrected it. Both separately reviewed that change and the later triangular-obstruction paragraph; General also reread the final file in full. |

Authors also performed complete saved-file self-reviews. Those are
not counted as independent reconstructions. Reviews here are separate
AI algebra and scope checks, not human expert or proof-assistant
certification. The triangular operator calculation uses an arbitrary
polynomial F; its written coefficient argument is not a bounded-degree
search. Its inline symbolic check adds no reusable test method.

The unrestricted Q-cube identity and primitive fixed-point-free
implication both remain unproved. The family calculations are not
extrapolated to all nice actions. No actual frame making an arbitrary
sliced action nice was obtained.

## 2. Selected primary-source gates

Root and Geometry freshly read Proposition2 and its full displayed
proof in Bedratyuk--Chapovskyi--Petravchuk's
[*Centralizers of linear and locally nilpotent derivations*](https://arxiv.org/html/2302.02441v1).
Root also read the adjacent maximal-rank theorem and its proof.
The result was already in the retained literature note. Its new use
here is the elementary coefficientwise LND specialization, not a new
centralizer theorem. Maximal rank among arbitrary derivations does not
give commuting locally nilpotent coordinate generators.

Root, Geometry and General checked Kaliman--Saveliev's
[*C+-actions on contractible threefolds*](https://www.math.miami.edu/~kaliman/library/KaSa.michigan.2004.quotient.pdf),
Corollary2.8 and its complete displayed proof, against the retained
cylinder-domination argument. The unit ideal for the intrinsic
primitive action is a known sufficient recognition hypothesis.
The longer topology and free-action results invoked in that corollary
were not newly re-audited here.

The exact Theorem2 statement in Derksen--van den Essen--Finston--Maubach's
[*Unipotent group actions on affine varieties*](https://arxiv.org/html/1002.4181v1)
was checked by Root, Geometry and General; Root and Geometry also
read its displayed proof. It requires a quotient of dimension one,
and the global product part requires freeness at every point. It
does not apply to the two-action four-dimensional pair merely from
generic independence or two individual slices. The compressed abstract
is not substituted for those precise hypotheses.

Geometry additionally reread the retained de Bondt homogeneous
rank-two classification and Dasgupta--Gupta's nice PID theorem.
The latter needs an actual invariant coordinate to apply in the
four-variable setting. No such coordinate is obtained automatically
from a good partial or Jacobian rank. The sources and access limits
are recorded in the two scope notes. This is a bounded applicability
audit, not an exhaustive historical novelty search.

## 3. Exact finite execution and failure provenance

The [fresh full capture](verification-pass75-working.json) passed
**146 suites and 1047 test methods**. It contains all 140 commands
from full73 and six added suites from74 and75. Exactly three suites
and six methods are new in75. The six retained addition outputs are:

| Suite | Methods | Reported unittest time |
| --- | --- | --- |
| [Affine74](affine_linear_adapted_checks_pass74.py) | 2 | 2.430s |
| [Nice adjoints74](nice_slice_adjoint_checks_pass74.py) | 3 | 1.633s |
| [Projection74](slice_projection_checks_pass74.py) | 2 | 0.086s |
| [Good-partial75](nice_good_partial_checks_pass75.py) | 1 | 0.453s |
| [Common-slice75](nice_common_slice_checks_pass75.py) | 2 | 3.108s |
| [Conic-family75](conic_slice_family_checks_pass75.py) | 3 | 0.289s |

The run began at 2026-09-14T05:16:06.484506+00:00 and finished at
2026-09-14T05:17:54.705695+00:00. Its monotonic timer reported
100.184486 seconds, while the UTC timestamp difference is
108.221189 seconds. Both measurements are retained; no cause of
that clock difference is inferred, and neither is used as a proof
or performance claim. The run and every suite returned exit zero.

The saved JSON SHA-256 is
`960cab63db3d427d5e25d142edc2f53b543f9fefd0d55d0b0d17dcd7d0fab247`.
Root verified the saved aggregate count, every exit/count/pass flag,
nine before/after source hashes and all six retained output hashes.
The complete output of every command was hashed by the frozen67
helper. Successful inherited output is omitted by that helper;
the six additions and any failed output are retained. The output
flag current_pass_addition means added since full73, not necessarily
authored in75. The new runner itself is read-only and was fully read
after saving.

The three new standalone checkers import only unittest and SymPy.
Root read all three completely. Jet independently audited and ran
the common-slice checker: two methods in3.054s. General independently
audited and ran the final conic-family checker: three methods in0.307s.
Earlier author, reviewer and user-check-in runs are not additional
methods or separate theorem verifications.

The first conic checker run raised two ZeroDivisionErrors inside
SymPy1.13.3 gcdex when its second polynomial was zero. These were
test-harness errors in constant-axis Bezout cases, not counterexamples
to the formulas. Root added exact guards for both zero-component
constant cases and verified their Bezout identities. The corrected
initial run passed three methods in0.251s; after adding further
gauge and coefficient-kernel controls, the final author run passed
in0.302s, followed by General's independent run and the full capture.
No mathematical hypothesis was weakened to obtain the passing runs.

Python compilation passed for the three new checker files and the
runner. Git whitespace checking passed, but the project is untracked
in its parent repository, so that check alone does not cover these
files. The explicit packet text scan is recorded separately.

Finite exact examples do not computationally verify the all-parameter
degree proof, the general adjustment/saturation lemmas, the source
theorems, universal coordinate existence, novelty or expert review.

## 4. Integrity and outstanding obligations

At 2026-09-14T05:20:54.666Z, Root revalidated297 prior hash records
through74, including all eleven working checkpoints64--74 and their
listed artifacts, and the full60 records other than the two explicitly
mutable presentation files. The previous checkpoint retained
SHA-256 `95cd034bf88ed421c0fc64daf538f3ad8ff34caafef5d7a157b3f059f47f822a`.
The central registry still contains544 claims and remains at full60.

The [working75 checkpoint](checkpoint-pass75-working.json) records
the current packet's hashes, equation numbering, local link paths,
saved run accounting and text hygiene. Hash equality proves file
identity, not mathematics. Local-path checking does not check link
anchors or certify continued remote availability.

The general conjecture, arbitrary nice-action recognition, universal
frame existence, the professor's intended interpretation, historical
novelty, expert review and formal verification remain incomplete.
The all-profile threshold stays ten. No public claim, submission,
external contact, credential use, capital or order placement occurred.
The active research goal remains open, not complete or blocked.
