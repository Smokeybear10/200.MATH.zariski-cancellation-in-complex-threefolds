# Independent audit of the initial-conic fiber restrictions

The complete [initial-conic note](initial-conic-fiber-pass48.md),
including equations (1)–(8) and the final scope, was independently
read and reconstructed by the parallel algebra agent after the root
agent expanded the initial-form observation. No mathematical or
scope correction was found. This is an AI proof audit, not human
expert review or formal proof verification.

## Algebra reconstructed

1. Tensoring the inclusions and quotient sequence for
   \(\mathfrak n^{d+1}\subset\mathfrak n^d\subset R\)
   with the actual flat algebra gives the displayed associated-graded
   isomorphism. It does not require the algebra to be a finite
   \(R\)-module. The tensor product factors through the full
   closed-fiber algebra because the coefficient quotient is killed
   by \(\mathfrak n\).

2. Equation (2) applies when every coefficient belongs to the
   stated base ideal. Taking independent base-monomial coefficients
   then gives equations in the actual image algebra. The note
   correctly prohibits continuing to higher base coefficients merely
   because lower equations vanish after residue evaluation. Variations
   of the lifts of \(z,w\) would contribute at those higher orders.

3. At \(J_R=\mathfrak n=(a,b)\), the first-jet coefficients in
   the chosen regular parameters are well defined. The two affine
   equations have coefficient rank equal to the matrix in (6).
   An inconsistent augmented system would make a nonzero complex
   scalar vanish in the nonzero full fiber, so the affine rank
   condition is valid without reducedness. Rank one supplies a
   quotient of a polynomial line for the two-function image, not a
   polynomial presentation of the whole fiber.

4. Rank zero puts \(B_1,B_2,Q\) in \(\mathfrak n^2\), so the
   second application of the graded-flatness identity is legitimate.
   The three independent parameter-square coefficients give all
   three quadratic monomials in the span of \(1,\bar z,\bar w\).
   Repeated reduction lowers monomial degree and bounds the dimension
   of the actual image algebra by three. This retains nilpotents;
   it is not merely a bound on the number of reduced image points.

5. The optional reduced and connected conclusions also check.
   A finite reduced complex subalgebra is a product of copies of
   \(\mathbb C\). If the full fiber is connected, its subalgebra
   cannot contain a nontrivial idempotent, so that product has one
   factor. Neither hypothesis is used earlier or asserted automatic.

## Provenance and limits

The original initial-form observation arose in the parallel cubic
investigation; the audited note is the root agent's separate full
expansion. Its rank-two exclusion is explicitly imported from the
cubic proof and is not attributed to the linear equations alone.
This audit adds no numerical suite or new theorem beyond checking
the saved argument. It does not eliminate rank-one or rank-zero
images, identify the full closed fiber, or remove the remaining
global cancellation obstruction. No frozen pass-47 file was changed.
