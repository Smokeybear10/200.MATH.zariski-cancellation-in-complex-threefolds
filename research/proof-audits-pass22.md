# Pass-22 proof reconstruction and verification record

The all-q family proof has two independent model reconstructions.
Neither found a mathematical gap under the stated assumptions.
This is not human expert review or proof-assistant verification.
The full cancellation conjecture and mathematical priority remain
unresolved.

## All-coefficient family

The main argument is
[radical-noninvariant-pass22.md](radical-noninvariant-pass22.md).
The reconstructions are
[radical-noninvariant-audit-pass22.md](radical-noninvariant-audit-pass22.md)
and [all-q-bridge-audit-pass22.md](all-q-bridge-audit-pass22.md).
Both checked:

- Nilpotence of the additive difference of the reduced substitution,
  including its valid use over a nonreduced Q-algebra.
- The orientation H=phi_0^-1(K), polynomiality of the corrected slice,
  unit reduced slope, and the global denominator lemma.
- Both physical curve directions and prime cancellation in both
  physical polynomial rings, not merely on reduced closed points.
- The algebraic curve and DVR obstruction without a simple-root
  assumption, including actual integral endpoints and a nonintegral
  orbit parameter.
- Exact descriptions of the first five derivation-degree modules,
  sharp affine/quadratic necessity, and cubic construction/minimality
  in its specified parameter window.

The main agent read both audits completely. Two editorial suggestions
were incorporated: link the n=1 base proof directly, and give the
fully f-localized z reconstruction beside the orbit endpoint argument.
No all-degree minimum formula was added beyond what was proved.

The first audit records 25 independent inline exact controls.
The second records four independent finite-repair examples and a
universal check of the displayed cubic expansion and derivative.
These do not add to the number of distinct regression test methods.

## General-center obstruction

The main agent read
[center-recognition-pass22.md](center-recognition-pass22.md) completely
and independently reconstructed the following steps:

1. N>=5 clears the exact x,y,z denominator formulas and gives actual
   contracted centers, not chosen substitute ideals.
2. The two reduced center curves have degrees five and two in T, so
   a denominator-support-preserving map cannot interchange f and h.
3. Comparison forces the translation into fh*C[f,h], with scaling
   constraints kappa^5=mu^3 and kappa^2=lambda^5.
4. The choice u=mu/lambda^4 satisfies u^6=lambda, u^25=mu,
   u^15=kappa, so all remaining scalings genuinely lift and normalize.
5. The induced modification map has the stated direction r/V plus
   translation. Its first-order y-divisibility obstruction is
   5*x^5*(alpha*x^3-B(0,x^5)), impossible for alpha nonzero.
6. The prior positive coordinate construction applies to V=1+fh;
   hence the failure is of this descending center transport, not of
   the abstract polynomiality of either modification.

The author also ran 17 inline exact controls. The new main suite
checks the first-order identity and Bezout relation independently.
The all-map exclusion is the written argument, not a finite grid.

## Nonlinear frames

The main agent read
[nonlinear-frame-pass22.md](nonlinear-frame-pass22.md) completely and
reconstructed the tangent projection, both polynomial inverses, the
curvature coefficient, and the horizontal polynomial differential
equation. A separate agent independently checked both projected
connections. The main suite includes their idempotence and projection
identities.

The conditional closed-coframe lemma uses its actual commuting-basis
and H^1_dR hypotheses. It is not a construction of that basis.
The flat example does not deny existence of a different useful
connection on the same polynomial kernel.

## Actual conductor-surface generators

The main agent read the complete
[five-generator proof](nodal-generators-pass22.md) and its seven-method
checker. It independently reconstructed the uniform original-variable
rescaling, polynomial Bezout recovery, finite extension, exceptional
point cases, the nodal normal-direction determinant, and both Nakayama
steps. In particular, finiteness follows for R as a submodule of the
finite S-module B, without assuming freeness or equality in advance.

The [separate reconstruction](nodal-generators-audit-pass22.md)
independently computes the rational point-collision gcds and conductor
cotangent minors. The conclusion is an explicit A^5 embedding, not
minimality of five generators, an A^3 embedding, or an ambient quotient.
The two failed triple arguments exclude only their specified forms.

## Execution record and limitations

The standalone main checker imports only unittest and SymPy, with no
project solver. Its finite quotient composition was optimized after
an initial slow expansion was interrupted. The original cases and
assertions were retained; the targeted 15-method suite then passed.
The later full regression includes all prior methods without counting
repeated executions as new methods. A Python integer reciprocal in
one exceptional-slope control was replaced by an exact SymPy integer
before the final run, retaining rational/Gaussian-rational arithmetic.

The final execution log is maintained separately as
[verification-pass-22.json](../verification-pass-22.json), and the
read-only packet checker validates registry counts, local links, source
hashes, and status flags. Those integrity checks are not mathematical
proof verification.

The [priority comparison](priority-comparison-pass22.md) credits the
published base, n=1 degree modules, and modification machinery.
The full 2009 example comparison remains unresolved. No novelty,
submission, external communication, human review, or Lean proof is
implied by this audit record.
