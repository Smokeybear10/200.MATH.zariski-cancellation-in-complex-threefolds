# Proof and verification audit for the plane and zero-normal restrictions

The [working synthesis98](quadratic-plane-and-zero-normal-frontier-pass98.md)
records two conditional actual-frame results. Neither is a proof of
general cancellation, an arbitrary-frame reduction, or recognition
of every supplied constant-acceleration action. Reviews below are
separate AI reconstructions, not human expert or formal verification.

## 1. Saved companion-collapse proof

The [eight-equation proof](quadratic-normal-companion-collapse-pass98.md)
was written by Geometry from Root's proposed use of the global
volume relation. Root read the saved proof through EOF and checked
the full-fiber specialization, disjoint-line contradiction, actual
affine coordinate change, nonzero second-order speed, and evaluation
of the exact extended component ideals. Current read chunks are
99ccfd and 4e1802; the earlier full read was 7348dc.

General's complete saved-file reconstruction is clean, including
all eight equations and the radical fiber formula, chunk ec1b31.
Jet separately read the saved proof through EOF and reconstructed
the same gates. The author read the listed volume88, invariant-plane88,
global-Jacobian91, collapsed-plane92, compatibility96 and weighted
defect97 dependencies through EOF. No fresh full audit of all
foundational topology is represented by these reviews.

In particular the proof uses freeness of the exact N on A_Omega,
not freeness of a rational multiple; disjointness of the actual
embedded components, not chosen lines; and a constant affine
coordinate change, not a matrix over S treated as an automorphism.
The component-ideal evaluation is global. Its intersection formula
is only for the radical of the fiber. Eell is explicitly nonzero.

No checker or actual-frame example is supplied for this geometric
proof. It leaves L(m)=0 and the existence of the mixed fiber open.

## 2. Saved zero-first-normal proof

The [eight-equation proof](quadratic-zero-normal-row-pass98.md)
was written by Jet. Root read its full saved proof and checker
(a85504 and 77497f), independently reconstructed the constant-column
step, all-point transverse coefficient, actual volume factor,
strict weighted operator, cubic derivative identities and row-span
classification. Root also reread the entire conormal-layer93,
weighted94, column94 and quotient-rank95 proofs for the relevant
local, volume and whole-thickening gates (6f2f7c, 704d14, b2b8c4,
dbe7eb).

General's full saved proof/code audit is clean, all eight equations,
chunk 2e8009. The exact coefficient is evaluated on the vector
(-q,p) at every complex c, including p=0 charts. The finite-free
rank-two component thickening gives length two at every transverse
section. This is stronger than generic multiplicity and is needed
to conclude that the coefficient is a nonzero constant.

The leading translation is computed only in the weighted ring.
Its coefficients yield p'''=q'''=0 through the two actual identities
N^3F=N^3G=0. Neither local nilpotence on a completion nor N^5c is
used. The intrinsic primitive LND control has N^2c=-2x^2, so the
leading square-zero identity is expressly not promoted to A.

The four row spans classify conormal data, not actions. No relative
generator is silently declared an original ambient coordinate.

## 3. Canonical exact execution and coverage

The [saved canonical capture](verification-pass98-working.json)
was produced by Root from the unchanged standalone checker:

~~~sh
/opt/anaconda3/bin/python -m unittest -v research.quadratic_zero_normal_checks_pass98
~~~

The execution began at 2026-09-14T17:51:04.316Z and ended at
17:51:04.748Z. It passed one suite/one method, exit zero, in
0.426175125 wall seconds and 0.040 unittest seconds. The complete
execution result is chunk 9fb463. Its exact stdout/newline/stderr
digest is 524f92347b1bacfb4480aad2643b8bb854a2b9e4aa06de65cd885ed202a2d868.
Input bytes were hashed before and after execution and did not change.

The checker imports only unittest and SymPy. It covers the formal
weighted identities for general quadratic p,q, a cubic-row negative,
a chart with p=0 but unit transverse coefficient, and the separate
intrinsic polynomial action. It does not check actual geometric
realizability, all local points of all actions, formal completion
theorems, whole-fiber finiteness, or recognition of A.

The author execution passed one method in 0.080 seconds, chunk
494882, wall 0.562201208 seconds. General's independent repeat
passed the same method in 0.043 seconds, chunk 9db406, wall
0.354280417 seconds. These are repeats, not additional coverage.
No new full regression was performed. The historical full75 capture
remains 146 suites/1047 methods, and the central registry remains
544 historical claims without integration of these later proofs.

## 4. Adversarial predecessor and source-scope checks

General made an additional targeted adversarial reconstruction of
the total-four exclusion97, specifically the equality D=O' and
the identification of normalized source entries with integral
component columns. The complete source-balance97, base-change94,
flat-rank93 and relevant dependency96/lattice97 reads found no gap
in that passage (5cf4e1 and 634b0f).

The decisive steps are actual finiteness: integral inverses of
localized denominators already lie in D; finite normalization retains
all source labels; every permitted base denominator evaluates at
each label to the same nonzero polynomial in the independent
projection variable. Residue degree is not dropped. General's
intrinsic quadratic quotient test gives e=1,f=2 and two transverse
complex branches, reproducing the entry ef=2. This is a handwritten
control, not a new test execution or an original-frame realization.
The final contradiction still needs the full integral lattice basis.

The bounded literature check found no recognition shortcut. The
nice-derivation hypothesis mismatch is already recorded in85/90,
so reencountering it is not new mathematical progress. Root freshly
read the displayed Theorem3.6 proof and Corollary3.8 in
[Dasgupta--Gupta](https://arxiv.org/pdf/1701.03635).

The distinct Pascal-finite lead also did not close the gap. General
read the original authors' selected statements/proofs and the full
[Adamus--Hajto HTML preprint](https://arxiv.org/html/2604.11693v1).
Root checked the displayed difference-operator definition,
strong-nilpotence definition, Theorem5.1 and Remark5.2 with their
complete short proofs. Original strong-nilpotence, wildness and
other cited dependencies were not all freshly audited. No entire
literature or novelty clearance is claimed.

## 5. State integrity and limits

The preceding check-in was a status answer and is classified as no
progress. This continuation revalidated the saved state and completed
the new proof integration and exact capture. All 586 frozen records
through checkpoint97 were verified unchanged at the start of the
investigation (19ee53) and again in this continuation (564af9).
The retained full-regression inputs and output digests also matched.

Only new98 artifacts and the live README/ledger are included in
this integration. The [checkpoint98](checkpoint-pass98-working.json)
records final input, output, artifact, equation and link accounting.
Any later99 scratch work is separate and is not certified by this
checkpoint or silently included among the completed98 deductions.

The research skill influenced the evidence separation and the bounded
primary-source applicability check. No no-progress literature lane
was inflated into a new theorem. General cancellation and the
arbitrary-frame reduction remain unresolved. No expert review,
Lean certificate, historical novelty clearance, external contact,
submission, public posting, or automation was performed.

General's final synthesis/audit and README/ledger review was clean
after one wording correction: F,G are E-invariant because they
belong to A; the unproved additional assertion is N-invariance.
The read-only capture check (dac7b2) confirmed five synthesis
equations, exactly one AST test method, the single input digest
and the complete output digest, without rerunning the checker.
