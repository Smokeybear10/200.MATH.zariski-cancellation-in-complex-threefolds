# Independent audit of the pass-48 synthesis

The complete [deep-pass-48.md](../deep-pass-48.md) was read, including all
26 tagged equations, the three mathematical arguments and the five source
notes. It was compared against the complete
[cubic-gate proof](third-image-cubic-gate-pass48.md),
[initial-conic-fiber proof](initial-conic-fiber-pass48.md), and
[repeated-support proof](repeated-smooth-support-pass48.md).
No mathematical, sign or scope correction was found.

The condensed cubic argument retains the extra premise
\(B_1,B_2\in J_R\), its automatic validity at reduced obstruction points,
and the distinction between actual regular-sequence division and a rational
formula. The factors in the cubic derivative, the third-image contraction and
the constant \(2(cf-de)\) agree with the full proof. The domain presentation,
local miracle flatness and height-one intersection are not assumed before
they are established. The resulting rank exclusion is not presented as
generation of the whole algebra in the lower-rank cases.

The initial-conic argument was independently reconstructed in full for this
audit. Flatness gives the asserted associated-graded base change without
requiring the total algebra to be a finite module. The first-order affine
equations have the stated signs. In the rank-zero case the second-order
equations reduce every quadratic monomial to the span of \(1,\bar z,\bar w\).
This bounds the image subalgebra, not the full fiber, and retains nilpotents.
The warning against imposing higher coefficients after only evaluated
lower-order vanishing is correct.

The repeated-support condensation keeps \(J=C\) separate from smooth reduced
plinth support, and uses the actual singular zero fibers in compactly
supported cohomology. The normalization map, distinct-branch count, cusp
form, transverse smoothness condition and two different exponents agree
with the full note. The Maubach input is the unconditional repeated-root
sufficiency theorem. The all-degree image formula is a consequence of the
actual global monic basis. The Russell example is explicitly a countercontrol
to weaker hypotheses, not a polynomial-cylinder example.

Source access and the two independently observed checker runs are recorded
in [proof-audits-pass48.md](proof-audits-pass48.md). That record remains
unchanged. No extra test method, full regression result, integrity checkpoint,
historical novelty, external expert review or proof-assistant certification
is claimed in this synthesis audit.

This review concerns the frozen mathematical scope of pass 48. Subsequent
pass-49 investigations are not silently inserted into its list of remaining
branches. The original unrestricted cancellation question and universal
actual-frame reduction are not claimed solved. No existing proof, synthesis
or shared metadata was edited during this audit.
