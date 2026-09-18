# Independent bounded proof audits for pass 48

This record covers the two new mathematical notes and their complete standalone
checkers. The reviews below were completed independently of the authors' own
runs. They are AI proof reconstructions and exact finite controls, not human
expert certification or proof-assistant verification. No pass-47 file or shared
metadata was changed. No full pass-48 regression or integrity result is claimed
here.

## 1. Repeated smooth support

The complete [repeated-support note](repeated-smooth-support-pass48.md) and every
line of its checker were read. No mathematical or scope correction was found.

The reconstruction checked the following points.

- The whole global quadratic presentation requires the explicit additional
  premise \(J=C\). Smooth reduced plinth support alone does not provide it.
- The closed complement is the actual disjoint union
  \(\coprod_i C_i\times\mathbb A^1\), including singular curves. Contractibility
  and smoothness give \(H_c^3(X)=0\); the punctured-line product chart gives
  \(H_c^4(U)=0\). The closed/open sequence and the affine-line shift therefore
  force each individual \(H_c^1(C_i)=0\).
- The displayed normalization is finite and birational. Its constant-sheaf
  quotient has dimension equal to the number of branches minus one at each
  point. Compact supports give precisely the number of distinct roots of
  \(h_i\) away from the branch value. Root multiplicities do not multiply that
  count. This proves the odd-power residue form, not smoothness of the curve.
- The gradient computation separates the plinth exponent from the cusp
  exponent. A cusp requires a repeated plinth component and a nonzero transverse
  derivative of \(d\); the latter is sufficient along the entire cusp line.
- When all residues are linear in the invariant-plane coordinate, the invoked
  repeated-root coordinate theorem applies to the actual global equation.
- The all-degree image formula follows from the existing global monic basis.
  It is not a new freeness theorem or an extra obstruction after \(J=C\).
- The Russell example realizes the stated weaker conjunction. Its known
  nonpolynomiality is not a counterexample to the original cylinder problem:
  the note does not assert a polynomial cylinder or the unresolved supplied
  coordinate-partial frame for that example.

The primary [Maubach manuscript](https://www.math.ru.nl/~maubach/Papers/The_Commuting_Dervations.pdf),
dated October 5, 2001, was directly read at Theorem 4.5 and its full proof,
together with the surrounding setup and Corollary 4.2. Its sufficiency theorem
allows the displayed arbitrary positive root multiplicities; it is not the
conditional general-dimensional necessity theorem.
The cited introduction of [Dubouloz's paper](https://arxiv.org/pdf/0807.4085),
PDF page 1, was directly read for the exact Russell cubic, its real-six-space
diffeomorphism, its Makar-Limanov invariant and nonpolynomiality. The cylinder's
trivial invariant is distinct from a polynomial-cylinder isomorphism. The
original historical proofs of those Russell facts were not independently
re-proved in this audit. The earlier monodromy theorem and invariant-plane
rectification remain identified, previously audited inputs; this review does
not claim a new full source audit of all their dependencies.

## 2. Cubic lift and first-jet exclusion

The complete [cubic-gate note](third-image-cubic-gate-pass48.md) and every line
of its checker were read. No mathematical or scope correction was found.

The explicit premise \(B_1,B_2\in J\) is essential away from a reduced
obstruction point. Faithful-flat contraction then supplies \(Q\in J\).
Preservation of the regular sequence \((a,b)\) yields the actual element
\(t\), not only a fraction-field expression. Direct differentiation gives
\(D^3t=3\epsilon^2p^2\). The inherited full quadratic divisor models bound
the third image at every height-one prime, and UFD contraction gives
\(I_3R=p^2R\) and the stated direct-sum decomposition of \(F_3\).

The derivative formula, its sign and constant term
\(2(cf-de)\), and independence of the residue determinant from the chosen
coefficient decompositions all reconstruct exactly.

Under a unit determinant, the two proposed relations were checked as an
actual presentation. Height-one localization eliminates \(T\) and gives the
known full conic model. The two independent closed-fiber linear equations have
ambient height four, excluding a minimal prime over the closed base point.
Together with the generic domain this gives one minimal prime. Height two
provides a regular sequence; Cohen-Macaulayness excludes embedded primes, and
generic reducedness then gives the domain presentation. At the generic and
closed points of the resulting fiber line, the local dimensions are exactly
those required by miracle flatness. Flat height-one intersection, rather than
an unsupported equality of subalgebras, proves generation of the actual ring.

The intrinsic pointwise plinth criterion consequently excludes the unit
determinant. This proves only the stated first-jet rank bound and
\(D(F_3)\subset\mathfrak nF_3\). It does not say that the derivation vanishes
on the whole closed fiber or that degree-three elements generate in the
remaining determinant-zero cases.

The exact statements and displayed proofs of Stacks
[00R4](https://stacks.math.columbia.edu/tag/00R4),
[02JN](https://stacks.math.columbia.edu/tag/02JN), and
[0BUS](https://stacks.math.columbia.edu/tag/0BUS) were directly read. The local
regularity, Cohen-Macaulayness and dimension hypotheses used in the note match
these results. The earlier actual height-one intersection and intrinsic
pointwise plinth results are used in their previously audited scope, not as
theorems about an arbitrary abstract conic algebra.

## 3. Independently observed exact runs

Both complete checkers import only `unittest` and SymPy. Each was run using
`/opt/anaconda3/bin/python`, with exit status zero.

| Standalone checker | Methods | Observed unittest runtime |
| --- | ---: | ---: |
| [repeated_smooth_support_checks_pass48.py](repeated_smooth_support_checks_pass48.py) | 2 | 0.141 s |
| [third_image_cubic_gate_checks_pass48.py](third_image_cubic_gate_checks_pass48.py) | 3 | 0.122 s |

The first suite checks normalization maps, finite branch identifications,
gradient conditions, the actual Russell action and bounded adapted-basis
identities. The second checks the cubic formulas, generic elimination, closed
linear equations and negative coefficient/rank controls. Neither suite proves
universal cohomology, flatness, image classification or cylinder recognition.
The formal cubic controls are not presented as actual examples satisfying all
the original geometric hypotheses. These five methods are not a claim about
the total project regression.

## 4. Remaining boundaries

The two deductions leave second-image basepoints with the permitted lower-rank
jets, including nonreduced points lacking the extra coefficient premise. Even
after \(J=C\), repeated support can leave the cuspidal thickenings described
in the note. Neither deduction proves that every sliced derivation on
\(\mathbb C^{[4]}\) admits a recognized frame. The original unrestricted
cancellation statement remains unresolved by this packet. No historical
novelty claim is inferred from these audits.
