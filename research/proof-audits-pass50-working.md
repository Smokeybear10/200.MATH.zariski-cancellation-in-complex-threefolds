# Working proof audit for the multi-tangent and bounded-slice results

This record preserves two new bounded mathematical investigations and a
fresh topology re-audit. It does not integrate them into the claim registry
or the full regression. The authoritative integrated checkpoint is pass49:
500 claims and 980 methods in 116 suites. General cancellation remains
unresolved, and no historical novelty, human review, or formal proof
verification is asserted.

## Multi-tangent trace bound

General authored [multitangent-plinth-boundary-pass50.md](multitangent-plinth-boundary-pass50.md).
Root read the entire saved proof and checker. Jet independently read both
completely, reconstructed the actual tangent bound and the exact weaker
control, and reported a clean three-method run in 0.069 seconds.

Root checked that a branch of multiplicity e gives order at least e+1
for each derivative coefficient, including identically zero denominators.
Its linear part therefore vanishes on that branch's tangent. Two distinct
tangents force B1,B2 into m^2 and p into m^2J. The order inequality uses
the actual regular plane local ring. It excludes an ordinary node, but
at a triple point only forces J to have a nonzero linear term.

The explicit triple-point control is a domain with a genuine LND. Its
dominating component on each branch has a quadratic invariant field,
normalized cover t=s^2, positive-order trace, and no missed normalized
point. The full branch pullback, however, includes a double vertical
plane. Root checked that this distinction is visible in the exact equation,
not just in a disclaimer. The displayed regular-sequence failure proves
nonflatness, and the entire vertical plane is singular. The model is not
claimed to satisfy the actual polynomial-cylinder hypotheses.

The three-method checker was reread completely and independently run by
root in 0.070 seconds, exit zero. Its finite polynomial identities do not
mechanize the universal tangent argument. The author's first run passed
in 0.071 seconds. Reruns add no methods.

## Fiber opens, denominator contraction, and projected-list obstruction

Jet authored [fiber-invariant-opens-pass50.md](fiber-invariant-opens-pass50.md).
Root read the entire saved proof and checker. General independently read
both completely, reconstructed every algebraic step, and reported a clean
one-method run in 0.290 seconds. No correction was requested.

The actual slice identity gives a unimodular pair of good velocities on
the scheme-theoretic fiber. Their squares are residues of actual F2
invariants, so two principal opens cover the whole fiber, including
nilpotents. These denominators are E-invariant, not necessarily D-invariant.

Root checked the UFD denominator proof: a prime can become a unit over
the invariant fraction field only when it divides an invariant. LND
degree additivity then makes the prime itself invariant. Moving prime
factors stay prime nonunits in L[j] and cannot remain in the denominator
of a polynomial there. At a nonempty closed-fiber open, an invariant
nonunit factor would make its defining invariant identically zero on
the fiber. Hence the D-finite part contracts to the original local ring.

For a localized actual E-slice, subtract the existing actual slice.
The difference lies in the localized invariant ring. The two bad-coordinate
projections differ by a nonzero invariant speed times that difference;
finite D-degree therefore descends the difference to the original ring.
No improper use of local nilpotence on a moving localization is made.

For the genuine degree-two generic graph, write a slice as an affine
generic slice plus H(j). If deg H=N>=2, some good projected coordinate
has degree exactly 2N because its acceleration is nonzero. Its other
terms have degree at most N+1 and two. Thus one F3-bounded projected
original list is already F2-bounded. At a hypothetical second-image
basepoint, this would make the exact conic the whole ring and contradict
the actual fiber dimension. The result does not forbid another generating
set inside F3, or prove that such basepoints actually occur.

## Square-root route and the failed degree implication

Root proposed the rational formula 2X/(P+kappa), with
kappa^2=P^2-2HX, while explicitly flagging that P+kappa is not an
E-invariant denominator. Jet developed the correct invariant version.
Writing P=Hs_*+a and X=Hs_*^2/2+a s_*+b gives the actual slice
s_*+2b/(a+kappa) on an invariant finite-etale open. Root independently
checked H sigma=P-kappa without dividing by H, and the two sign opens
cover because kappa is a unit.

The resulting algebraic extension is not covered by the polynomial
denominator lemma. In the genuine lower-profile polynomial coordinate
example, D^n(kappa) is nonzero for every n. Thus the constructed slice
does not supply a bounded intrinsic derivative degree. The control
explicitly has profile (0,1,2,0), not the unresolved (1,1,2,2) profile,
and already has an ordinary coordinate slice. Its role is limited to
refuting the etale-slice-to-bounded-degree inference.

Root independently ran the one-method checker in 0.302 seconds, exit
zero, after reading all its lines. The author's first run passed in
0.297 seconds. The finite checks verify the actual coordinate inverse,
partial/adjoint identities, square-root identities and derivative
recurrence through order seven. The all-degree recurrence and general
denominator theorem remain written arguments.

## Topology re-audit

Geometry saved [normalized-cover-adversarial-audit-pass50.md](normalized-cover-adversarial-audit-pass50.md).
Root read it completely. It reconstructs finite-normalization properness
by monic-coordinate bounds, whole-fiber excision for every chosen
neighborhood, the correctly typed local Thom map, and the exact sequence
giving peripheral-loop independence. The reduced-divisor normal degree
and product-complement isomorphism are explicitly checked. The old
deleted-line control locates failure when H3 does not vanish.

No gap or mathematical correction to pass49 was found. This was a fresh
adversarial pass by the same author, not another independent reviewer.
It adds no numerical method and no new external source theorem.

## Remaining next step

The single-slice projected-list repair is now ruled out at a hypothetical
obstruction point, even after the stated nonempty invariant fiber opens.
An alternative F3 generating set, a direct higher-filtration argument,
or the actual flat/prime exceptional geometry must supply the next step.
The triple-point model prevents reliance on trace and normalized-cover
conditions alone. These conclusions narrow the original investigation
without changing its unresolved end goal.
