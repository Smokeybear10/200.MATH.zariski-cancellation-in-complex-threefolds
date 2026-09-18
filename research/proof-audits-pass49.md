# Proof and verification audit for the normalized-cover and frame results

## Scope and provenance

This is a private process record, not an external certification. The three
mathematical notes concern the corrected complex-threefold interpretation
of the professor's email. That interpretation remains unconfirmed. The
unrestricted cancellation question remains open in this project.

The root agent reread all three saved notes completely in the continuation
after the status check-in, including the final verification paragraph in
the actual-frame note. The prior turn had already reconstructed their
arguments. Independent agents reviewed the mathematical arguments as
recorded below. Agreement between AI agents does not establish human
expert review, formal proof checking, or historical novelty.

## Normalized exceptional-cover surjectivity

Artifact: [normalized-cover-surjectivity-pass49.md](normalized-cover-surjectivity-pass49.md).

Geometry authored the note. General and Jet independently read the full
argument. Both identified a wording defect in the exceptional invariant
ring corollary: localization at a function defining the product chart
gives an invariant curve ring, not the entire rational function field.
The saved version first localizes the ring and then passes to fraction
fields. Root checked that corrected passage and reread the complete note.

The support argument requires the actual global homology diagram and the
product complement. It does not follow from normalizing a surjective
morphism. In the proof, finite normalization is proper in the complex
topology; the complement of the image of its closed bad set is a
neighborhood of the entire exceptional fiber. This avoids assuming that
the fiber is compact, reduced, smooth, or an affine line.

The loop contradiction also requires every normalized affine curve
component to have a puncture at infinity. The finite peripheral loops
are then independent. Rational coefficients permit division by the
ramification indices of the selected cover points. Reduced pullback
divisors are needed to identify the middle map with ordinary pushforward.

For the no-poles corollary, surjectivity gives an actual point above every
potential pole. The equation t^n f = unit contradicts regularity after
pullback to that local ring. The resulting finite intermediate invariant
ring has the same normalization as the source's curve; equality with the
particular nonnormal curve model is not asserted.

Root directly opened and read the displayed statements and proofs of
Stacks tags [035Q](https://stacks.math.columbia.edu/tag/035Q),
[0C1R](https://stacks.math.columbia.edu/tag/0C1R), and
[035S](https://stacks.math.columbia.edu/tag/035S) in this continuation.
Their uses are normal-source factorization, semilocal curve normalization,
and finiteness of normalization. The separate primary-source topology
review is attributed to Geometry. A further adversarial pass50 audit
is separate from this checkpoint and is not presumed complete here.

## Ordinary-node exclusion

Artifact: [nodal-plinth-obstruction-pass49.md](nodal-plinth-obstruction-pass49.md).

General authored the note. Geometry and Jet independently reconstructed
the full proof and reported no remaining gap. Root's complete reread
checked the same sequence, including the following boundary cases.

The actual minimal-slice residue must generate the quadratic invariant
field. An arbitrary quadratic relation in a smaller conic algebra does
not suffice. At a normalized base DVR, the integral closure is a finite
free rank-two module. Vanishing at every point above the base point makes
multiplication by the slice residue nilpotent after reduction. Its trace
therefore vanishes even at ramified points with nonreduced residue algebra.

If b is not identically zero on a plinth component, the exact minimal
polynomial gives trace -2B1/(epsilon b). If b is zero there, coprimality
forces a nonzero and p=aB1+bB2 forces B1 to vanish identically. The swapped
argument treats B2 without dividing by a zero residue. Two branches of
one irreducible nodal curve are included.

The trace gives order at least two for both coefficients on both smooth
branches of an ordinary node. Their linear parts vanish on two distinct
tangents, so B1,B2 belong to m^2, forcing p into m^3. The contradiction
uses the full plinth's multiplicity exactly two. It does not exclude a
higher-multiplicity singularity merely because two tangents are distinct.
No reducedness of J, and no premise B1,B2 in J, is needed for this proof.

## Actual low-degree generation

Artifact: [frame-filtration-generation-pass49.md](frame-filtration-generation-pass49.md).

Jet authored the note. General read the full proof and reported it clean.
Root reread it completely, including its explicit arbitrary-slice control.
The key premise is the inherited equality B_L=L[x3,x4], together with the
quadratic expressions for the good coordinates. It is not only a generic
Jacobian calculation.

When one of f,g,h1,h2 is invertible, the displayed slice is an actual
element of B_R and is affine-linear over L in the bad coordinates. Its
slice projection maps all four original generators into intrinsic degree
at most two. Surjectivity of that projection proves generation of the
whole A_R. The gluing argument uses an arbitrary module element and
annihilating powers on a finite principal cover, not finite generation
of the quotient module.

At an alleged second-image basepoint, the exact conic presentation has
all coefficients vanishing. If it were the entire algebra, its fiber
would have dimension two, contrary to the actual one-dimensional fiber.
Thus the basepoint support lies in V(f,g,h1,h2). This is a support
inclusion, not an ideal equality, and it does not settle that zero locus.

The actual-coordinate example has projected degrees (2N,2N,N,N) for an
arbitrary supplied nonlinear slice. It disproves a uniform bound on
that generating list. Its ring is already generated by F1, so it is not
a counterexample to low-degree generation of the ring itself.

## Observed exact checks

The checker imports only unittest and SymPy. It checks the explicit
actual frame, adjoint bounds, independent determinant, inverse maps and
slice projections at N=2,3,5. It is one method, not three methods or a
mechanized proof of either universal geometric statement.

The author's successful run reported one method in 10.270 seconds.
The preceding root run reported one method in 10.291 seconds.
In this continuation root reran the actual saved source using:

~~~sh
/opt/anaconda3/bin/python research/frame_filtration_generation_checks_pass49.py
~~~

The completed process, session 41676, reported one method in 10.435
seconds and exited zero. The author's earlier failure was an
expanded-versus-factored equality assertion, corrected by normalizing
the difference. No mathematical identity changed in that repair.

Root also reran the existing pass48 integrity checker successfully.
It still reports 492 scoped claims, 979 methods, 115 suites, and 159
hash records. Those totals do not include the pass49 checker or claims.
No full pass49 regression is claimed by this audit record.

## Remaining obligations

The general-frame reduction, the whole supplied (1,1,2,2) profile,
simultaneous speed/acceleration zero fibers, more singular or repeated
plinth components, and the remaining global quadratic recognition
questions are not closed. These results must not be advertised as a
solution of the professor's conjecture.
