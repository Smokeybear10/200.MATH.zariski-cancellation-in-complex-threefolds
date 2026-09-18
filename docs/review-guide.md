# A reading guide for mathematical review

[Home](../README.md) · [Current status](current-status.md) · [Archive map](archive-map.md)

This is a route through a private working notebook, not a submission-ready
paper. The main conjecture remains unsolved and originality is unestablished.
Start with the two current notes, then follow their dependencies as needed.

## Recommended sequence

| Step | Document | What to inspect |
| --- | --- | --- |
| 1 | [Current status](current-status.md) | The working scope, positive implication, negative controls, and missing existence step. |
| 2 | [703: common-centralizer slice criterion](../research/raw-projection-centralizer-slice-criterion-pass703-working.md) | Sections 1–3 for the proof; Sections 4–5 for controls and the existence boundary. |
| 3 | [702: all-slice projection obstruction](../research/all-slice-projected-lnd-obstruction-pass702-working.md) | Sections 2–4 for the uniform classification and primitivity; Section 5 for the nonlinear repair. |
| 4 | [654: projection identities](../research/commuting-projected-partials-retraction-recognition-pass654-working.md) | The exact relation module and constant-normal endpoint used in703. |
| 5 | [656: polynomial-curve antecedent](../research/three-commuting-projected-partials-unit-normal-recognition-pass656-working.md) | Sections 2–3 and the cited curve-factorization theorem. |
| 6 | [Latest mathematical ledger entry](../research-ledger.md#september-18-2026-all-slice-projection-obstruction-and-a-single-field-translation-criterion) | Review provenance, exact checks, corrections, source scope, and what was not proved. |

For background definitions rather than the current frontier, use
[research-note.md](../research-note.md), Sections 2–4.

## Questions worth challenging in703

- Do the principal-retraction assumptions justify the relation module,
  unimodular normal data, and smoothness used in the proof?
- Does commutation with **all raw** projected fields really reduce the
  coefficient functions to one polynomial curve?
- Does the imported curve theorem place its parameter in the original
  polynomial ring and in the right fraction field? Does retraction put
  it in A?
- Are the derivative-gcd normalization, scalar-unit argument, and both
  branches of the Wronskian argument valid?
- Does the derivation-stable ideal argument handle nonradical ideals and
  justify the explicit slice, not just local nilpotence?
- Is the distinction between a conditional criterion and existence of
  a nonzero common centralizer maintained throughout?

The square-zero statement X^2(r_i)=0 applies only to the specified
branches. The constant-normal control explicitly refutes a universal
version of that bound.

## Questions worth challenging in702

- Does the frame have the printed whole polynomial inverse, not just a
  unit Jacobian?
- Does the divergence argument cover every nonconstant polynomial h,
  with constant h treated separately?
- Does the primitivity proof handle every coefficient case, including
  its separate cubic eliminant boundary?
- Are “gcd one” and “coefficient ideal is the unit ideal” kept distinct?
- Are all-slice failure of the specified method and successful nonlinear
  repair both retained, rather than being presented as an obstruction to
  cancellation?

## Dependencies and source attribution

The selected older notes have different roles:

- [643](../research/primitive-leading-fixed-locus-frame-obstruction-pass643-working.md)
  supplies the actual frame reused in702 and its primitive leading-field result.
- [644](../research/slice-scaling-root-extraction-closure-pass644-working.md)
  treats homogeneous components and a specified internal closure, not all
  raw projections.
- [658](../research/all-slice-linear-frame-family-classification-pass658-working.md)
  treats a different complementary-basis criterion. Its obstruction is not
  the same as702's single-field extraction obstruction.
- [Polynomial-curve source audit](../research/polynomial-curve-factorization-source.md)
  identifies the imported de Bondt statement and its precise limitations.

These are antecedents of the current notes, not new results of this
documentation update. For primary citations and exact versions, follow
the references in the proof notes.
This reading guide does not constitute a new literature or priority audit.

## Reporting a mathematical issue

A useful review identifies the file and section, the exact hypothesis or
inference in question, and either a correction, counterexample, or missing
argument. Distinguish a mathematical gap from a presentation issue.
No outreach or review request has been sent as part of this cleanup.

Saved checker scripts are frozen. The historical commands are evidence
records, not a current instruction to execute them. This documentation
update does not run, import, compile, edit, or newly validate those scripts.
