# Pass 40 proof audits and exact verification scope

The completed AI proof audits found no remaining mathematical defect
in the bounded statements recorded below. They close the degree-six
cubic-column residual and the constant-factor degree-five residual.
For nonconstant degree-five factors, the two-output case also
closes by a separate denominator and coordinate-descent argument.
The three-output case remains open despite recognition of its
auxiliary nice kernel.

This is a process record of independent AI reconstruction and exact
algebraic controls. It is not human expert review, Lean verification,
a novelty assessment, or a solution of general cancellation.

## 1. Proofs reconstructed and their limits

The main agent fully read and audited the
[degree-five proof](cubic-degree-five-pass40.md),
[degree-six proof](cubic-degree-six-pass40.md), and
[unified compatibility calculation](cubic-compatibility-pass40.md),
including the relevant checker files. The two algebra investigators
independently cross-read the coefficient and localization arguments.
The degree-five investigator also fully reconstructed the degree-six
proof and the complete unified note.

The checked gates include the surviving rescaled top field, full
auxiliary matrix rows, exact Taylor factors in both degrees, the
rational function-field contradiction in the exceptional case,
the affine relation among invariant coefficients, and the corrected
nice field. The original polynomial slice is explicitly used to
prove that this field fixes the inverted invariant. That is what
establishes actual local nilpotence on the localized ring.

For the polynomial degree-six and constant-factor degree-five
branches, the second action has an actual ambient-coordinate
slice. Its section projection and inverse give a genuine
polynomial three-ring. The classical three-variable kernel theorem
is applied there, followed by an explicit polynomial integration.
It is not applied indiscriminately to a localized three-ring.

The main agent fully read and audited the
[two-defect critical-locus proof](two-defect-critical-locus-pass40.md)
and its six-method checker. The geometry investigator independently
reconstructed the full proof and wrote the
[separate audit](two-defect-critical-locus-audit-pass40.md).
That audit checks both exact height notions, the complete leading
ideal, the four reduced points, and the repeated-root cases.
The degree-five investigator separately read the full proof and
checker and reconstructed those same statements without a defect.
The result obstructs nonvanishing in a prescribed leading module;
it does not obstruct every intrinsic LND or every coordinate frame.

The main agent wrote and fully checked the
[nice-centralizer bridge](nice-centralizer-bridge-pass40.md).
The geometry investigator reported a clean independent audit.
The degree-five investigator also fully read that bridge and
directly reread Dasgupta and Gupta's Theorem 3.6, its complete
proof, and Corollary 3.8; that independent audit was clean.
The source theorem is used after primitive division and after
exhibiting the required invariant linear coordinate. Its conclusion
is polynomiality of the auxiliary kernel. The original kernel is
not identified with that auxiliary kernel, and an original slice
is not assumed to descend to it.

The subsequent [two-output closure](two-output-cubic-closure-pass40.md)
was fully read and reconstructed by the main agent and independently
by both the degree-five and geometry investigators. Its actual localized-flow determinant,
nonunit denominator invariant, inherited good partial, both
commuting-pair branches, and relative Hamann descent were clean.
The exact Hamann statement in Dasgupta and Gupta's Theorem 2.6
was directly read. The main and geometry agents also directly
read Maubach's Theorem 3.6 and Proposition 3.5; the degree-five
investigator checked the corresponding three-variable statement
and the complete inherited single-partial case split. This proof supplies an actual invariant
ambient coordinate without assuming a unimodular coefficient
pair or transfer of the original slice to the auxiliary kernel.

## 2. Actual standalone runs

Each checker imports only `unittest` and `sympy`. Counts below are
test methods, not scalar assertions or the number of parameter
values used within a method.

| Standalone suite | Methods | First run | Main-agent direct rerun |
| --- | ---: | ---: | ---: |
| [Degree-six and shared coefficient controls](cubic_degree_six_checks_pass40.py) | 5 | 0.396 s | 0.439 s |
| [Degree-five rescaling and unit controls](cubic_degree_five_checks_pass40.py) | 5 | 0.461 s | 0.513 s |
| [Two-defect critical-locus controls](two_defect_critical_locus_checks_pass40.py) | 6 | 0.196 s | 0.196 s |
| [Nice-centralizer controls](nice_centralizer_checks_pass40.py) | 3 | 0.068 s | 0.068 s |
| [Two-output cubic controls](two_output_cubic_checks_pass40.py) | 4 | 0.070 s | 0.067 s |

All these executions passed with exit zero. The degree-five
investigator independently read and reran the shared degree-six
suite: five methods passed in 0.396 seconds. These reruns do not
increase the number of test methods.
The same investigator independently read the appended centralizer
control and its complete checker; all three methods passed in
0.067 seconds. Its actual moved-plane example does not claim
failure of every possible choice of invariant plane.
The independent critical-locus rerun passed all six methods in
0.195 seconds.
The complete two-output checker was independently read and rerun
by the degree-five investigator: all four methods passed in
0.079 seconds. Its finite denominator and coordinate controls
are not machine proofs of Hamann's theorem or the universal
kernel-contraction argument, and no actual degree-five residual
example is claimed.

The shared coefficient suite separates formal coefficient algebra
from an actual lower-degree action and actual coordinate-splitting
controls. Neither it nor the degree-five suite claims to construct
an actual degree-five or degree-six residual example. The latter
suite's four-variable denominator control is explicitly excluded
from the full degree-five hypotheses. The critical-locus suite
does use genuine polynomial-cylinder examples for its stated
leading-module obstruction.

The [complete regression](../verification-pass-40.json) actually ran
from 2026-09-13 14:58:58 UTC through 15:00:16 UTC. All 869 methods
across 88 suites passed, including all 23 methods in the five new
suites. The full completed JSON was captured and saved directly.
Repeated executions, five orchestration parser controls and two
integrity link-parser controls are not counted as mathematical methods.

The main agent also fully read the final two-output proof and its
four-method checker; the direct rerun passed in 0.067 seconds.
The geometry investigator independently reconstructed that complete
proof and all its source gates. The main centralizer rerun passed
three methods in 0.068 seconds. A further independent two-output
rerun passed four methods in 0.071 seconds. All are finite controls,
not machine proofs of the cited classification or cancellation inputs.

## 3. Corrections retained in the audit trail

The following issues were corrected during derivation or drafting:

- An initially overbroad critical-locus module statement treated
  all kernel-coefficient combinations as LNDs. The main agent
  narrowed it to combinations over the invariant plane
  \(\mathbb C[u,v]\) before independent audits. Arbitrary
  kernel-coefficient combinations still belong to the stated
  vector-field module, but need not be locally nilpotent.
- Generator-wise niceness of the rational corrected field was
  initially insufficient to claim an LND on the localization.
  The original-slice unit argument now explicitly checks the
  inverse of the localized invariant. Clearing a denominator
  still does not supply a global polynomial slice.
- Two TeX spacing issues in the degree-six note were corrected.
  They did not change an equation or its mathematical content.
- The nice-derivation classification paper was already present
  in earlier project literature notes. This pass rechecked and
  applied it to the newly constructed auxiliary field; it did
  not newly discover that source or its theorem.
- The synthesis corrected a literal plus sign joining draft
  lines and expanded the Bhatwadekar, Gupta and Lokhande title
  to its actual title. Its final scope audit also made the
  slice assumption explicit in the low-degree recognition
  sentence, named Theorem 2.8 rather than an ambiguous
  antecedent for the Miyanishi attribution, and included the
  zero-restriction case before the two-output case split.
  These corrections are present in the independently reread
  synthesis; the complete proof already covered the zero case.

No test assertion failed in the recorded first runs. The corrections
above concern mathematical scope or transcription, not a hidden
failed test being reported as an initial success.

## 4. What remains unverified

The finite checks do not prove the universal matrix-rank,
rational-field, or localization arguments. Those are supported
by the written deductions and the independent AI audits. The
published recognition inputs retain their exact hypotheses and
credit; no new external classification theorem is claimed.

The nonconstant-factor, three-output degree-five passage remains
open in these notes. So does the existence of a bounded or reducible
coordinate frame for an arbitrary polynomial cylinder. No public
posting, expert outreach, submission, or novelty claim is part
of this checkpoint.
