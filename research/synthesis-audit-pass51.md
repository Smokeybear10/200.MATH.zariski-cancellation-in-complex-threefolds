# Independent synthesis audit for pass51

The complete current [pass51 synthesis](../deep-pass-51.md), including
its verification paragraph and three source notes, reconstructs cleanly
against the saved mathematical packet. No mathematical correction is
requested. This is an independent AI read/proof reconstruction, not human
expert review or proof-assistant verification.

## 1. Material actually reviewed

This audit read the complete synthesis and all 25 tagged equations,
then compared the condensed arguments with:

- [The complete cubic-generation proof](cubic-generation-obstruction-pass51.md)
  and its entire two-method checker, both newly read in this review.
- [The ordinary-triple and quartic proof](triple-point-quartic-corrections-pass51.md)
  and its complete three-method checker, fully independently reviewed
  earlier in pass51, with the relevant formulas checked again against
  the synthesis.
- [The complete velocity-invariance proof](fiber-velocity-invariance-pass51.md),
  independently reviewed earlier and reread for this comparison.
- The [working proof audit](proof-audits-pass51-working.md),
  [working checkpoint](checkpoint-pass51-working.json), and current
  [captured regression record](../verification-pass-51.json), read as
  evidence records rather than mathematical proofs.

The working files retain their earlier pre-integration status. The
synthesis separately links the later completed expanded regression;
this audit does not silently replace those historical records.

## 2. Cubic presentation and scope

Equations (6)-(16) retain the decisive full-module statement:
\(K=R[F_3]\), not just the algebra of one projected coordinate list.
The actual height-one conic identifications are invoked with the correct
localization at base primes. They are not used to assert closed-point
equality without the additional presentation argument.

The coprimality argument is valid. A common factor becomes a unit over
the base fraction field and hence is a base prime factor in the UFD.
The nonzero localized prime ideal, which avoids that base prime, cannot
be contained in its principal ideal. Cancellation gives the stated
contradiction.

The length-two resolution gives the associated-prime height bound.
The divisor domains exclude associated primes over height-one base
points; the residual dimension excludes primes over the closed point.
The remaining generic prime gives base torsion-freeness and the actual
presentation. No flatness of the cubic approximation is inferred.

In rank zero, the determinant relation and all signs of the two-column
complex match the full proof. Coprimality of \(F,G\) makes an appropriate
minor invertible at every height-one prime of the ambient UFD, which
justifies contraction of the rational syzygy coefficients. The monic
quadratic in \(T\) retains the possibly nonreduced surface fiber.
Both rank cases therefore establish full cubic non-generation, not
existence or impossibility of an actual reduced obstruction.

## 3. Triple, quartic and whole-fiber statements

The ordinary-full-triple argument preserves invariant basis covariance
and the exact local generator form \(J=(a,b^n)\). It does not replace
the local ring by its completion. Along the branch tangent to \(a=0\),
the trace inequality contradicts \(n\ge2\), so \(J=\mathfrak n\).
An ordinary triple is not thereby excluded.

The two actual quartic divisions use preserved regular sequences
\((a,b^2)\) and \((b,a^2)\), not merely identities in a fraction
field. Their coefficients \(6\epsilon^3ap^2\) and
\(6\epsilon^3bp^2\), and the divisor fourth-image coefficient
\(24p^2\), agree with the full proof. The synthesis correctly keeps
the pass51 alternative
\(I_4=p^2\mathfrak n\) or \(I_4=p^2R\).
It neither chooses the ideal nor asserts quartic generation. It also
explicitly distinguishes nonmembership in the module \(F_3\) from
nonmembership in its generated algebra.

The velocity argument works on the entire possibly nonreduced fiber.
The two unit-ideal opens descend derivative vanishing globally. The
Artinian factor argument contracts the relevant unit ideal using an
actual embedding and nonzero idempotents, without a flatness assumption
on that subalgebra. The bound of six concerns the stated finite image
subalgebra, not the whole curve fiber or its component count.

The additional independent degree-two frame remains a hypothesis.
Neither the original cancellation problem nor universal frame reduction
is represented as settled. Working pass52 conclusions are not imported
into this pass51 audit.

## 4. Source and finite-verification record

This review directly read the full statements and proofs of
[Stacks 00LX](https://stacks.math.columbia.edu/tag/00LX) and
[Stacks 00NQ](https://stacks.math.columbia.edu/tag/00NQ), checking the
depth estimate used by the synthesis. The prior completed
[foundational source audit](intrinsic-quotient-foundation-audit-pass51.md)
already records the direct Kaliman-Saveliev, Kaliman and miracle-flatness
reads and their access limits. Those sources were not broadly searched
again for this integration audit. The synthesis correctly attributes
the normalized-cover and trace refinements to the project proofs, not
verbatim to Kaliman's paper.

After reading every line of the cubic checker, this reviewer independently
ran it: **2 methods passed in 0.067 seconds, exit zero**. The earlier
independent quartic checker run passed **3 methods in 0.205 seconds,
exit zero**. These are the same five methods already in the packet,
not five additional methods. Both checkers import only unittest and
SymPy and keep their bounded controls distinct from universal proofs.

The current report's expanded verification paragraph was checked against
the saved JSON: **120 suite records, 989 methods**, with the sum of
per-suite methods equal to 989, every suite marked passed and every exit
code zero. The recorded interval is **20:25:02-20:26:35 UTC on
September 13, 2026**. This was read-only inspection of the captured
record, not an independently repeated full regression. No shared
metadata, report, or frozen mathematical file was edited.
