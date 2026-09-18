# Independent reconstructions and verification for the bridge results

The complete proofs and controls are working research results.
The unrestricted cancellation conjecture, family-level novelty,
human expert review, and proof-assistant verification remain unestablished.
The records below distinguish written arguments from finite exact tests.

## 1. Primitive noninvariant extension

The main proof is
[primitive-noninvariant-bridge-pass21.md](primitive-noninvariant-bridge-pass21.md).
The separate [primitive audit](primitive-bridge-audit-pass21.md) reconstructs
the monic-chart second image, arbitrary-invariant valuation, minimum slice
degree, polynomial surface inverse, and both physical denominator clearings.
It found one scope defect: the universal coefficient domain must contain
the rational fractions. This was corrected to a Q-domain before the final
regression and report. The physical complex family was unaffected.

The independent preliminary calculation verified eleven universal map
identities and three square-zero congruences. These inline calculations
are not additional unittest methods. The checker was also independently
rerun before cleanup: fourteen methods passed in 28.826 seconds.
The two cleaned-up methods passed independently again in 0.063 seconds.
The main final complete execution ran the final fourteen-method source
in 31.904 unittest seconds.

The checker uses a separately written inverse and computes the physical
base derivation from its Jacobian. Inverse jets recompute the new invariant
coefficient. It does not expand the entire physical four-generator inverse;
that conclusion combines the displayed identities with written divisibility
and domain arguments. Finite residue and coefficient tests do not prove
the complete image ideal or rank classification by themselves.

## 2. Universal center reduction

The [universal-center proof](universal-bridge-pass21.md) was read fully
by the main investigation and independently reconstructed in
[universal-bridge-audit-pass21.md](universal-bridge-audit-pass21.md).
The two inclusions in both modification presentations hold exactly.
The test example's ideal is the canonical contracted center, so the
Jacobian obstruction satisfies the actual lemma's hypotheses.

The failed lift allows arbitrary complex polynomial automorphisms
preserving the denominator ideal, not just invariant-plane-fixing maps.
The alternate triangular ideal transport has a polynomial inverse.
The modified ring remains polynomial. Thus the counterexample excludes
the prescribed jet, not all center transports or cancellation.

The cited modified-commuting hypotheses and the canonical singular
degree stage were reopened in the primary author papers. The finite
presentation does not supply universal polynomial recognition or a
compatible kernel-graph path.

## 3. Arbitrary slice frames

The [frame note](arbitrary-slice-frame-pass21.md) separates an actual
polynomial complement from an abstract polynomial subalgebra.
The stable-base restriction/extension principle is credited as known.
Its normalizer consequence and zero constant-centralizer example were
checked independently by the main derivation and by exact controls.

The affine-linear example is already a coordinate translation with
an explicit nonlinear inverse. Neither that example nor the primitive
fixed-base obstruction is used to deny all nonlinear stable frames.
Calling a general commuting LND with a slice a coordinate partial
would still assume an unproved recognition step.

## 4. Nodal surface and K-theory

The [global nodal proof](nodal-embedding-pass21.md) retains exactly the
scaled gluing of the preceding conductor construction.
The main reconstruction and [separate audit](nodal-audit-pass21.md)
both check the actual Milnor square, residue interpolation, divisor
relations, regular-normalization point classes, and determinant boundary.

Weibel's relevant Units-Pic and projective-module Milnor statements,
regular-surface generation by point classes, and the Stacks cotangent
complex statement were read in primary references. No regularity of
the singular ring or vanishing of SK1 of its normalization was inserted.
The cotangent-class equality uses the actual trivial dualizing module,
not merely the local nodal equations.

The report explicitly refuses to turn module generators into algebra
generators or a stable cotangent class into an embedding. The remaining
three-algebra-generator question and stronger ambient quotient problem
are separate.

## 5. Final execution and report audit

The [final full regression](../verification-pass-21.json) ran from
September 13, 2026, 05:07:47 through 05:09:15 UTC.
All **451 methods across 34 suites** passed.
The new [standalone checker](primitive_bridge_checks_pass21.py)
contains fourteen methods and imports only SymPy and unittest.

The [reusable runner](run_regression_pass21.py) retains the prior
33-suite command list and adds the new suite. Its five parser controls
are not mathematical methods. An initial one-off aggregator wrongly
required OK to be the final output line, misclassifying eight successful
older suites that append summaries. The reusable runner fixes that
boundary, and every suite was rerun. No test failure was concealed.

A further complete read of [the report](../deep-pass-21.md) checked
the theorem formulas, inverse, center contraction, nodal gluing, and
all scope qualifications. It found two exposition corrections, both
applied: the split-line indices are j and epsilon, and the four removed
lines generate the normalization's class group, not that of its
factorial localization.

The [bounded priority audit](primitive-bridge-audit-pass21.md) identifies
definite narrower two-variable coverage by Berson-van den Essen-Maubach.
The general local-slice and modification machinery is prior work.
The [2009 family comparison](priority-comparison-pass21.md) records
an actual outstanding full-text comparison. The author abstract was read,
but full formulas were not obtained. No collision or distinction is claimed.
These audits do not certify novelty, constitute human expert review,
or solve unrestricted complex threefold cancellation.
