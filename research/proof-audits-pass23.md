# Proof and execution record for pass 23

This record distinguishes working proofs, independent model reconstructions,
finite exact checks, and artifact integrity. None is human peer review,
a Lean formalization, or verification of unrestricted cancellation.

## Coefficient theorem

The main derivation is the complete
[polynomial local-slice coefficient proof](polynomial-local-slice-coefficients-pass23.md).
Its assumptions are C, the displayed canonical base, n>=1, and
b in C[f,h,r]. Both monic remainder conditions are necessary in
every degree, and together they give a polynomial slice and polynomial
kernel.

Two independently assigned model reconstructions were completed:

- The [first reconstruction](polynomial-coefficients-audit-pass23.md)
  checked both DVR curves without simple-root assumptions, the ring
  intersection and gauge, a chosen f-divisible independent representative,
  the nonlinear inverse, and both physical denominator clearings.
  Fifty inline exact scalar assertions passed. They are not test methods.
- The [second reconstruction](polynomial-coefficients-second-audit-pass23.md)
  checked the same universal steps independently, with separate physical
  Jacobian, remainder, nonlinear inverse, and finite-repair controls.
  The two inline command groups took 0.209 and 0.912 seconds.
  Repeated identities are not additional tests.

Neither reconstruction requested a correction to the full theorem.
The main agent subsequently read both audit files completely and
rechecked their ring and scope distinctions. The proper-subring boundary
is explicit: y is not in C[f,h,r]. No all-coefficient reduction to that
subring is inferred.

The final report's independent transcription review found three
expository errors before finalization. Its opening needed to restrict
the homotopy failure to the chosen natural horizontal derivation.
After equation (9), the invariants are rho and X, not L.
Before equation (14), the local-slice value must be nonzero, invariant,
and nonunit, with the unit case separate. All three were corrected.
These corrections narrow the summary to the already stated full proofs.

## Surface theorem and the two general routes

The [four-generator surface proof](nodal-elimination-pass23.md) retains
the original pinching and uniform coordinate normalization. Polynomial
Bezout recovery gives finiteness. The full-conductor quotient and
Nakayama give equality of rings. A separate point-and-cotangent argument
reconstructs the same conclusion.

The [independent surface audit](nodal-four-generator-audit-pass23.md)
recovered the formulas, all branch restrictions, global finite-module
argument and cotangent determinants. The main agent read the proof,
audit and entire independent checker and reconstructed the conductor
argument. This proves four algebra generators, not four independent
coordinates, an A^3 embedding, or an ambient quotient.

The [presentation homotopy](presentation-homotopy-pass23.md) was derived
independently alongside the main coefficient proof and read fully by
the main agent. Its finite Bezout identity, cylinder map, formal jets,
horizontal recurrence and exact slice-lemma equivalence were checked.
The formal-to-Zariski negative control is explicitly not stably polynomial.
Ninety-five inline assertions reported during its derivation are controls,
not methods in the regression.

The [leading-derivation gate](leading-derivation-pass23.md) was also
read completely by the main agent and cross-checked by the homotopy
investigator. It credits the already recorded leading-LND principle.
The new restriction gate does not confuse coefficient projection with
descent of an action. The primitive degeneration control concerns loss
of properness or a slice in a particular limiting action, not all frames.
These auxiliary notes received mathematical cross-checking but are not
represented as additional independent reconstructions of cancellation.

## Actual independent test execution

The new [coefficient checker](polynomial_coefficient_checks_pass23.py)
implements its own monic remainders, gauge normal form, multiplication-
truncated finite-jet operations, inverse pullback and physical curve
congruences. It imports only unittest and SymPy, not a project solver
or prior checker.

Its fourteen methods cover the constant and n=1 boundaries, the old
linear/invariant axes, nonlinear positive and negative coefficients,
the G0 identity and gauge differentiation, finite correction and both
divisor orbit formulas. One method each supplies bounded homotopy and
leading-action controls. A further case in an existing method verifies
that b=1+5hr^4 is physical-positive but the raw auxiliary action has
fixed points. It did not increase the method count.

An initial checker assertion rejected a polynomial with a nontrivial
constant denominator, such as f*x/2. It was corrected to use
the actual polynomiality predicate. No theorem identity failed.
The author's first passing run had fourteen methods in 0.934 seconds.
The main expanded targeted run had fourteen methods in 0.913 seconds.

The independent [surface checker](nodal_elimination_checks_pass23.py)
has seven methods covering six branch restrictions, both Bezout
identities, polynomial recovery, finiteness, conductor quotient and
cotangent determinants. The main targeted runs passed, including
seven methods in 0.280 seconds after the coefficient checker expansion.
Other independent and repeated runs are not extra methods.

The complete thirty-eight-suite regression actually ran twice:

| Run | UTC start | UTC completion | Result |
| --- | --- | --- | --- |
| Initial expanded regression | 06:32:09 | 06:33:25 | 494 methods, all passed |
| Final recorded regression | 06:33:57 | 06:35:12 | 494 methods, all passed |

Both runs were on 2026-09-13. The
[final structured log](../verification-pass-23.json) retains every
suite command, exit status, method count and runtime. In that final
run the coefficient suite had fourteen methods in 0.939 unittest
seconds and 1.145 wall seconds; the surface suite had seven methods
in 0.280 unittest seconds and 0.505 wall seconds.

The 473 preceding methods plus 21 new methods give 494 distinct
methods across 38 suites. The runner's five output-parser assertions
are orchestration controls, not mathematical methods.

~~~sh
/opt/anaconda3/bin/python research/run_regression_pass23.py
/opt/anaconda3/bin/python research/consistency_checks_pass23.py
~~~

The separate consistency checker verifies JSON, claim order, AST
method counts, explicit command coverage, flags, links, whitespace,
equation and footnote numbering, and SHA256 hashes. It does not
mathematically verify the written proofs.
Its first run found the report's link to the not-yet-created consistency
output. An explicitly pending output target was created, then replaced
only after a successful read-only run. No mathematical test was affected.

## Priority and release boundary

The [bounded primary-statement comparison](priority-comparison-pass23.md)
retains definite inherited credit and checks the hypotheses that prevent
automatic application of the closest translation theorems. Its physical
affine-slice versus auxiliary-fixed-point control was reconstructed
independently during report review. The fourteen inline scalar assertions
reported in that source comparison are not new test methods.

No full 2009-example access, comprehensive database audit, mathematical
novelty determination, human review, formalization, public posting,
submission, external contact, payment, or automation occurred in this
pass. The unrestricted goal remains active and unsolved.
