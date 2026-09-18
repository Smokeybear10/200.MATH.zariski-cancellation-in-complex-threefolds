# Independent synthesis audit of pass 50

The complete [deep-pass-50.md](../deep-pass-50.md) is consistent with
the three frozen pass-50 proof records. No mathematical correction,
dropped hypothesis, sign error, or unsupported general-solution claim
was found. All 26 equation tags occur once in order, and all three
source footnotes have the stated limited roles.

This audit concerns the pass-50 snapshot. Later pass-51 investigations
are not silently imported into its remaining-branch statements.

## 1. Material actually read

The geometry reviewer read the synthesis through its final footnotes,
and read these complete saved files:

- [multitangent-plinth-boundary-pass50.md](multitangent-plinth-boundary-pass50.md);
- [fiber-invariant-opens-pass50.md](fiber-invariant-opens-pass50.md);
- [normalized-cover-adversarial-audit-pass50.md](normalized-cover-adversarial-audit-pass50.md);
- [proof-audits-pass50-working.md](proof-audits-pass50-working.md);
- both complete standalone checker source files.

The topology re-audit was originally authored by this same geometry
reviewer. Its inclusion here is a consistency check, not a new
independent reviewer of that argument. The full readings of the other
two proof notes and checker files are independent of their authors.

## 2. Equations (1)–(9): actual hypotheses and tangent bounds

The report keeps the unknown threefold \(A\), original sliced
four-variable action \(E\), and intrinsic primitive action \(D\)
distinct. The local coefficient ring is the actual quotient
\(C=\ker D\), not an assumed coordinate plane of \(B\).
The definitions of the full plinth, \(F_n\), and \(I_2=pJ\)
precede their use.

The quotient input was independently revalidated in
[the new foundational audit](intrinsic-quotient-foundation-audit-pass51.md).
That audit does not add a hypothesis to pass 50: the cylinder gives
smoothness and contractibility of the unknown threefold and a
dominant actual affine-three-space restriction of its projection.
Kaliman–Saveliev then gives \(C\simeq\mathbb C^{[2]}\).
Nonempty curve fibers and miracle flatness give faithful flatness.

The conic relations (3)–(5) correctly retain
\(a,b,B_1,B_2,Q\in\mathfrak n\), with no assumption
\(J=\mathfrak n\) or \(B_1,B_2\in J\).
The actual primitive quadratic residue and normalized-cover
surjectivity are explicitly prerequisites for the trace inequality.

For a possibly singular branch of multiplicity \(e\), a nonzero
linear term on its tangent has order exactly \(e\); all terms of
\(\mathfrak n^2\) have order at least \(2e\). The trace inequality
therefore kills the linear term on that tangent. Two different
directions give \(B_1,B_2\in\mathfrak n^2\) and
\(p\in\mathfrak n^2JR\). The order inequality
\(\operatorname{ord}J\le\operatorname{ord}p-2\) has the correct
direction. It concerns the full plinth with multiplicities.

The report's ordinary-triple statement describes what this extracted
order inequality alone gives. It does not claim the inequality is a
classification of every actual triple-point configuration.

## 3. Equations (10)–(14): the weaker triple-point control

I reconstructed the generic linear change
\[
(z,w)\longmapsto(r,j)=(az+bw,-b^2z-a^2w),
\]
whose determinant is \(b^3-a^3\), and the primitive irreducible conic.
The displayed derivation preserves the defining relation, has
\(Dr=p\), and is locally nilpotent on the actual auxiliary domain.

For every cube root \(\zeta\), the normalization
\[
t=s^2,\qquad r=\zeta^2s^2+s^3
\]
has the displayed fraction-field inverse, quadratic extension and
trace. The induced action on the dominating surface really is
\(\zeta s^5\partial_z\), with invariant ring \(\mathbb C[s]\).

The important full-pullback factor \(t^2\) is retained in (13).
The report does not replace that pullback by its dominating surface.
The nonzero zero-divisor witness modulo \(b\), the plane closed
fiber, and the singular vertical plane prove the claimed failures
of actual flatness and smoothness. In particular:

- no polynomial-cylinder presentation is claimed for this domain;
- no full primitive-plinth computation is claimed for it;
- the reached quadratic covers do not upgrade it to a model of the
  complete actual quotient;
- its role is only to show that the extracted conic, cover and trace
  conditions are insufficient by themselves.

## 4. Equations (15)–(22): fiber opens and exact polynomial descent

The good velocity residues form a unit ideal on the full
scheme-theoretic fiber by reducing the original slice identity and
evaluating at \(s_*=0\). Their squares also form a unit ideal.
The two \(F_2\) opens therefore cover the entire fiber, including
nilpotents. The report correctly calls their denominators
\(E\)-invariant, not necessarily \(D\)-invariant.

For the denominator lemma, a prime of \(A_R\) becomes a unit over
\(L=\operatorname{Frac}C\) precisely when it divides a nonzero
invariant. Additivity of LND degree then puts it in the invariant
ring. All other primes remain nonunit primes of \(L[j]\), and
cannot survive in a reduced denominator of a polynomial there.
This proves (18) with repeated prime factors permitted.

Repeated derivatives of a rational function with a finite pole do
not vanish in characteristic zero. Hence finite \(D\)-degree in
\(L(j)\) is equivalent to being polynomial in \(j\), giving (19).
These kernel formulas use the extended derivation on the localization;
they do not assert it is locally nilpotent on that entire ring.

A fiber open that is nonempty cannot invert a nonunit invariant
factor of its defining element: such a factor belongs to
\(\mathfrak mR\) and would make the residue zero. The denominator
lemma thus contracts its finite-degree elements to the original
\(A_R\).

The bounded-slice descent sign is correct:
\[
\rho_{s_*}(x_3)-\rho_\sigma(x_3)=f(\sigma-s_*).
\]
Since \(Df=0\) and \(f\ne0\), finite derivative degree of the
left side gives finite degree of \(\sigma-s_*\), and the actual
polynomial slice descends. No division by \(f\) inside \(A_R\)
is asserted.

For the genuine degree-two graph, at least one \(h_i\ne0\).
If the invariant correction \(H(j)\) has degree \(N\ge2\), the
good projected coordinate has exact degree \(2N\); the other
terms have smaller degrees \(N+1\) and at most two. Thus (22)
correctly includes the constant and zero cases of \(H\).

The final non-generation implication is restricted to one projected
original-coordinate list for one actual slice. The report expressly
does not rule out generation by all elements of \(F_3\), or by
another generating set. It also does not assert that a second-image
obstruction point occurs in an actual unresolved frame.

## 5. Equations (23)–(26): the étale construction and its boundary

After inverting \(I\), the monic polynomial
\(T^2-I\) has invertible derivative \(2\kappa\), so the
extension is finite étale. I directly read
[Stacks 03PA](https://stacks.math.columbia.edu/tag/03PA),
Definition 59.26.3 and its following complete standard-étale proof.
This source supports that algebraic extension, not any derivative
bound for the resulting slice.

The actual formulas obey
\[
H\left(s_*+\frac{2b}{a+\kappa}\right)
=Hs_*+a-\kappa=P-\kappa.
\]
They define a slice without inverting \(H\).
The two invariant sign opens cover because \(2\kappa\) is a unit.
The report separately flags \(P+\kappa\) as a moving
\(E\)-denominator, so it does not use the slice theorem on that
unjustified localization.

The intrinsic extension \(D\kappa=(DI)/(2\kappa)\) is distinguished
from the original \(E\)-action. The lower-profile control has a
polynomial inverse, exact adjoint heights \((0,1,2,0)\), and the
nonzero all-order recurrence (26). Its slice and the projection of
\(s\) have infinite intrinsic degree. It already has the ordinary
coordinate slice \(s\), and is not labeled as a full
\((1,1,2,2)\) realization.

## 6. Sources, finite runs and final scope

The three synthesis citations are accurate in scope:

1. Kaliman–Saveliev and miracle flatness support the inherited
   quotient, not polynomiality of the unknown threefold.
2. Stacks 03PA supports the étale extension, not finite degree.
3. Kaliman's exceptional-factorization and homology diagram support
   the setting of the normalized-surjectivity deduction. That
   refinement is not attributed verbatim to the published theorem.

The recent foundational audit directly re-read the relevant
Kaliman–Saveliev author-primary proofs and arXiv statements, Kaliman's
factorial-quotient and surjectivity passages, and Stacks 00R4 and
00RC. Project Euclid's typeset article was not accessible in that
run. The separate topology re-audit records its own direct primary
read and its same-author status.

After reading both checker files in full, this reviewer independently
ran them with the saved Python executable:

| Checker | Observed result |
| --- | --- |
| multitangent_plinth_boundary_checks_pass50.py | 3 methods passed in 0.074 seconds, exit zero |
| fiber_invariant_opens_checks_pass50.py | 1 method passed in 0.302 seconds, exit zero |

Both import only unittest and SymPy. The finite controls do not
mechanize the universal topology, tangent inequality, denominator
lemma, or generation quantifiers. These reruns add no methods.

After the root's integration, this reviewer read the actual verification
paragraph and inspected verification-pass-50.json read-only. Its 118
suite records sum to 984 methods; every recorded exit code is zero and
every recorded suite passed. The recorded run spans 20:05:06–20:06:39
UTC on 13 September 2026, and its totals agree with the current synthesis.
This checks the saved captured record, not an independent full rerun or
a new examination of every underlying process output. No global
regression result is inferred from the four targeted methods above.

The synthesis retains the professor's unconfirmed dimensional
correction, the unresolved general cancellation question, and the
unproved universal-frame reduction. No frozen proof, checker,
synthesis, registry, or hash record was edited. This new audit file
is the sole pass-50 write in this review.
