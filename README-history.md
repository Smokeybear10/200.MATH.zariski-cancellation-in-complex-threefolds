# Historical research front page

[Return to the reading guide](README.md) · [Current status](docs/current-status.md)

Snapshot preserved on September 18, 2026, during the navigation cleanup.
The original front page follows unchanged. It contains historical status
updates and should not be read as a current summary. Its relative links
still resolve from the repository root.

---

# Zariski cancellation investigation

Private working material for the conjecture supplied by Xiangrui Luo.
Created September 12, 2026. Thomas authorized a private GitHub backup on
September 18, 2026. This does not authorize public release, a novelty claim,
external outreach, or submission. Downloaded papers and local caches are
excluded from version control; saved checker scripts remain frozen.

The working question is corrected complex-threefold cancellation,
A[s]=C^[4] implies A=C^[3]. Luo has not confirmed this interpretation.
The pasted conclusion X=A^1 has a dimensional error for r>1; the likely
intended conclusion is X=A^r. The general problem is not solved here.

## Latest investigation: a single centralizing field supplies a translation

General cancellation remains UNSOLVED and novelty UNKNOWN. The
[common-centralizer criterion703](research/raw-projection-centralizer-slice-criterion-pass703-working.md)
proves that a nonzero intrinsic derivation commuting with ALL the raw
projected coordinate partials of a principal polynomial retraction is
automatically locally nilpotent and has a slice. No local-nilpotence
assumption is needed. The proof uses the special projection identities
and the previously source-checked polynomial-curve theorem.

Existence is still missing: an exact polynomial-cylinder example has
ZERO common centralizer in its supplied frame. Nonlinear frame selection
is not solved by the conditional theorem. A separate
[all-slice obstruction702](research/all-slice-projected-lnd-obstruction-pass702-working.md)
classifies every constant-direction raw projection at every polynomial
slice of that example. All nonzero projections are already primitive;
the only locally nilpotent ones fix a line. Thus slice changes, constant
reframings and common-factor removal cannot make that extraction work.
An explicit nonlinear recombination succeeds, so neither result is a
cancellation counterexample.

The [ledger](research-ledger.md) records complete-source AI reviews and
fresh exact checks for both notes, their antecedents, and the unproved
existence step. These are not human expert review, proof-assistant
certification or novelty clearance.

## Previous investigation: origin dilation does not supply polynomial lifting

General cancellation remains UNSOLVED and novelty UNKNOWN. The
[origin-dilation audit701](research/origin-dilation-rees-and-polynomial-lifting-gap-pass701-working.md)
constructs, for every actual input, a smooth family whose central fiber
is affine three-space and whose nonzero fibers are the unknown variety.
Its cylinder is polynomial over the parameter ring. This is the standard
deformation to the tangent space of a point, not a recognition theorem.

An exact low-degree example shows that the canonical projected formal
inverse need not terminate and that the natural horizontal derivation
need not be locally nilpotent. Other polynomial coordinates succeed in
that example. A successful global lift for every input remains equivalent
to the original cancellation conclusion, so formal agreement alone has
not reduced the global proof gap. The antecedents in23 and654 are credited.

The [ledger](research-ledger.md) records three full-source AI reviews,
independent exact calculations, and the precise standard-grading gate:
in the supplied frame, that grading condition holds only when the
original action already has constant coefficients. No expert review,
proof-assistant verification or novelty clearance has been obtained.

## Previous investigation: all flow coefficients still need nonlinear extraction

General cancellation remains UNSOLVED and novelty UNKNOWN. The
[full-coefficient obstruction700](research/full-orbit-coefficient-linear-extraction-obstruction-pass700-working.md)
gives an actual four-coordinate polynomial example in which every
nonconstant linear combination of ALL invariant flow coefficients
has a critical point. None can therefore be an ambient coordinate.
The proof covers every complex coefficient choice, including the
exceptional intersection cases, not just a generic or sampled list.

This closes the stronger fixed-slice linear-extraction proposal left
unresolved in699. It does not obstruct nonlinear extraction: quadratic
expressions recover all three invariant coordinates. A different
slice also makes linear extraction succeed. The example already has
a polynomial kernel and is not a counterexample to cancellation.

The [ledger](research-ledger.md) records all-source AI reviews and
supplemental exact computations. No human expert review, proof-assistant
verification or historical novelty clearance has been obtained.
The missing global construction or useful degree bound remains.

## Previous investigation: an exact completion test and an all-order failure

General cancellation remains UNSOLVED and novelty UNKNOWN. The
[projection-completion note699](research/projected-coordinate-completion-criterion-pass699-working.md)
gives an exact test for projecting three actual ambient coordinates
onto the invariants and adjoining the supplied slice. When the test
succeeds, the proof supplies a whole polynomial inverse.

An explicit family shows that actual coordinate frames can satisfy
the translation conditions to any finite normal order while this
projection step still destroys invertibility. The underlying action
is an ordinary translation with a degree-one exact solution. Thus
this rules out automatic completion of arbitrary approximate frames,
not better frame choices, cancellation, or the degree bound sought
in698. Existence of a frame passing the new test remains equivalent
to the original recognition problem. No new kernel is recognized.

The [ledger](research-ledger.md) records the proof checks, attribution,
and additional literature-scope checks. Internal AI reviews are not
formal verification, human expert review, or novelty clearance.

## Previous investigation: computable finite-order bounds, with the growth gap intact

General cancellation remains UNSOLVED and novelty UNKNOWN. The
[finite-order bound note698](research/computable-finite-orbit-jet-bounds-pass698-working.md)
combines the published orbit-jet extension theorem with retained
constructible exhaustion and field-theory decidability. For fixed
input-complexity bounds and approximation order k, a uniform forward
AND inverse degree bound D_k is computable in principle. No such
search was implemented or run, and no useful growth rate is proved.

The missing implication is now explicit: every kernel in a fixed
input family is polynomial if and only if D_k stays bounded, or
equivalently some order satisfies k>e+D_k-1. Computability at each
finite order does not establish that condition. The note also keeps
orbit-normalized frames distinct from frames containing a specified
slice, which may need greater degree even for ordinary translations.

This is a corollary and a precise computational formulation, not a
new recognition theorem or evidence of novelty. Independent AI
reviews do not replace formal verification or human expert review.
The [ledger](research-ledger.md) records source checks and the exact
remaining global obligation.

## Previous investigation: quadratic controls, attribution, and a closed subclass

General cancellation remains UNSOLVED and novelty UNKNOWN. The
[quadratic control note697](research/quadratic-coefficient-obstructions-and-sharp-slice-degree-pass697-working.md)
rules out two unsupported shortcuts: a sliced quadratic-coefficient
action need not have a nilpotent coefficient Jacobian or an affine-linear
invariant/slice, and quadratic coefficients do not force a quadratic
slice. One recognized family has exact minimum slice degree 2n+1.

The source audit materially limits that result's significance. Its
recurrence is a specialization of the retained weighted recurrence607,
and its n=2 coordinate pair is a rescaled published Nagata example.
The degree minimum is recorded as an explicit corollary, not a new
construction or a claim of originality. The homogenized fixed-point
control is explicitly distinguished from the two sliced controls.

The latest [ledger](research-ledger.md) closes the commuting subclass
E=L+H, where L is constant, H is homogeneous quadratic, and [L,H]=0,
assuming an actual polynomial slice. A homogeneous three-variable kernel
argument supplies an invariant linear coordinate, and the published
Bhatwadekar--Gupta--Lokhande theorem recognizes the kernel. This is a
corollary of known results. No reduction of arbitrary cylinders to this
subclass or even to quadratic coefficients has been established.

The unresolved work remains the global entry or degree-control step
for an arbitrary A[u]=C^[4]. Further examples inside recognized families
do not supply that step. Internal AI reviews and exact checks are not
human expert review, formal certification, or novelty clearance.

## Previous investigation: finite orbit normalization and the global degree gap

General cancellation remains UNSOLVED and novelty UNKNOWN. The completed
[orbit-jet note696](research/orbit-jet-normalization-and-primitive-top-discontinuity-pass696-working.md)
applies the published Kaliman--Udumyan extension theorem to every actual
polynomial cylinder. At any chosen closed orbit, translation coordinates
exist to every finite normal order. These restrictions ARE compatible;
what is not supplied is one polynomial map realizing all orders.

There is an exact sufficient degree test. In fixed original coordinates,
let e be the coefficient degree of the sliced derivation and d the
forward degree of an actual frame correct through order k. If
k>e+d-1, the residuals vanish identically and the frame is globally
adapted. No suitable bound on d is proved. A rational formal example
shows that a preselected compatible system can force degree growth even
when standard coordinates already solve the problem.

The same note gives an all-order control: finite normal-jet agreement
along an ENTIRE orbit does not force the extracted primitive leading
actions to move its base point. Every constant frame direction can
still have the same prescribed primitive fixed-point action. This does
not describe all intrinsic actions or exclude a better global frame.

The latest [ledger](research-ledger.md) also proves a relative-extension
failure in ordinary polynomial space. Even for a globally smooth
invariant function, a function-preserving formal volume jet can have
no function-preserving polynomial extension. Unrestricted extension
still exists. Thus neither degree control nor preservation of a chosen
invariant may be assumed from the published finite-extension theorem.

The next task remains a genuinely global coordinate/action construction
or a justified degree estimate, not further finite-order normalization.
All-source AI reviews and exact checks are not human expert review,
formal certification or novelty clearance. No general solution exists here.

## Previous investigation: local nonisomorphism, exact repair, and preserved plinth

General cancellation remains UNSOLVED and novelty UNKNOWN. The completed
[local obstruction693](research/quadratic-localization-absolute-isomorphism-obstruction-pass693-working.md)
proves that the old height-one localizations of a globally solved
quadratic example are not even isomorphic as C-algebras. A general
proof therefore cannot assume these particular local rectifications
exist and leave only their gluing to be done. Global coordinate
changes may need to move the invariant localization itself.

The separate [exact repair criterion694](research/quadratic-constant-shift-exact-descent-pass694-working.md)
classifies every invariant-constant correction of the specified
exponential. It gives an iff divisibility test and proves that the
full-thickness height-one constant tests descend globally. Tests on
only reduced divisors do not suffice. Failure excludes this family
of exponentials, not every possible coordinate completion.

The [inherited-action proof695](research/quadratic-inherited-full-plinth-preservation-pass695-working.md)
shows that the quadratic construction preserves the ENTIRE full
plinth, including repeated factors, and gives an explicit minimal
slice for the inherited action. Primitive normalization does not
improve it either. Thus repeating this operation along that action
cannot supply a decreasing-plinth proof of cancellation.

These statements are compatible: full-thickness descent for one
constant is not an isomorphism theorem for the localized total rings.
The remaining target requires a genuinely different action, a global
invariant-moving construction, or another consequence of the arbitrary
polynomial-cylinder hypothesis. Internal AI reconstructions and exact
checks are not human expert review, formal certification or novelty
clearance. No reduction of arbitrary cylinders to these quadratic
models, and no solution of the full problem, has been established.

## Previous investigation: complete family repair and a general squarefree criterion

General cancellation remains UNSOLVED and novelty UNKNOWN. The completed
[family proof690](research/polynomial-curve-all-quadratic-extensions-pass690-working.md)
recognizes EVERY admissible quadratic datum from688 on the arbitrary
monic polynomial-curve base family. It supplies the whole corrected
automorphism and its polynomial inverse, including every higher-pole
boundary term and the original supplied slice.

The completed [kernel-class proof691](research/polynomial-curve-kernel-class-quadratic-extensions-pass691-working.md)
extends this to EVERY nonzero LND having that SAME EMBEDDED invariant
ring, equivalently all nonzero invariant replicas of the primitive
base. Repeated factors of the multiplier are included. This is not
a classification of all embeddings of a polynomial two-ring in C^[3].

The separate [general criterion692](research/general-quadratic-squarefree-plinth-recognition-pass692-working.md)
leaves the model family: the quadratic constructions are recognized
for ANY base with squarefree full plinth, including all its invariant
replicas. No connectedness or smoothness of the plinth support is
required. A sufficient divisibility criterion constructs a whole
exponential; for general plinths it bounds possible generator poles
by half the component multiplicity. A bound is not a global repair.

These are restricted recognition statements, not a cancellation proof.
The remaining obligations are whole repair along arbitrary multiple
plinth components, including their intersections, and a separate
reduction from an arbitrary A[s]=C^[4] to a recognized construction.
Neither is established. Exact checks and internal AI reconstructions
do not constitute human expert review, formal certification or
novelty clearance. The ledger records each full-source review and
the earlier subfamilies already covered by known or retained work.

## Previous investigation: an exact quadratic model and the global repair gap

General cancellation remains UNSOLVED and novelty UNKNOWN. The completed
[quadratic-extension proof688](research/quadratic-sliced-extension-normal-form-and-repair-gate-pass688-working.md)
starts inside ACTUAL polynomial four-space. For Dr=a^2 b it identifies
the supplied sliced kernel with R[Q]/(r+Q+abQ^2/2), using whole inverse
maps. It computes the inherited action and its full fixed scheme and
gives an iff criterion for the uncorrected exponential to be polynomial.
Existing primary results recognize every rank<=2 base derivation;
arbitrary rank-three input remains unresolved.

The completed [global-repair proof689](research/quadratic-repair-normalizer-and-formal-gluing-gap-pass689-working.md)
matches the complement and EVERY finite thickening of the exceptional
divisor, but distinguishes these separate matches from a global map.
An explicit family proves that a completion can be impossible if it
must preserve the old invariant plane EVEN SETWISE, despite the supplied
slice actually being a coordinate. Thus a successful universal repair
must be allowed to move that subalgebra, not merely rename its generators.

Both full notes passed three independent AI proof reconstructions and
fresh exact checks. This is not human peer review, formal certification,
or novelty clearance. No general completion or cancellation proof exists
here. The next task is a genuinely invariant-moving global construction
or another consequence of the arbitrary polynomial-cylinder hypothesis,
not another finite-jet check of the already matched neighborhoods.

## Previous investigation: all z-fixed and plane-projectable actions

General cancellation remains UNSOLVED and novelty UNKNOWN. The completed
[z-fiber proof686](research/two-stage-z-fiber-rigidity-and-normalizer-gates-pass686-working.md)
classifies EVERY z-fixed action on the (2,2,3) test cylinder R[u]: it is
exactly h*partial_u for h in R. Generic z-fibers are affine cubic surfaces
with finite automorphism groups, and the proof uses one-variable rigidity.
This action classification is not asserted for arbitrary stabilization.
Its complete Euler profile, however, excludes every nonconstant f(z) as
a coordinate or slice after ANY polynomial stabilization.

The completed [plane-projectable proof687](research/two-stage-plane-projectable-action-classification-pass687-working.md)
handles coupled formulas, not just fixing y or z separately. For ANY number
of added variables, every automorphism preserving C[y,z] fixes that plane
subalgebra pointwise and preserves R and the critical locus. Every LND
preserving C[y,z] is R-linear. The full plane-fiber Euler stratification
forces this conclusion; no polynomial-degree restriction is imposed.

Both complete notes passed three independent full-source AI reviews and
fresh exact checks. These are not human peer review, formal certification,
or novelty clearance. An action whose y,z formulas leave C[y,z] remains
outside the new classification, and no escaping whole action was found.

The latest ledger records explicit transverse curves through every point
of the b=0 critical line, ruling out a curve-absence shortcut. No group
action follows from those curves. The z-fixed and plane-projectable routes
are now closed; the next priority returns to a consequence of the ACTUAL
polynomial-cylinder hypothesis, not another restricted degree search.

## Previous investigation: all y-fixed actions and a stable Euler obstruction

General cancellation remains UNSOLVED and novelty UNKNOWN. The completed
[uniform y-fiber proof685](research/two-stage-y-fiber-rigidity-and-euler-profile-pass685-working.md)
shows that every y-fixed LND on EVERY polynomial stabilization of the
test family671 annihilates its original threefold ring R. On the open
y!=1 this class is the entire LND set; its exact ML invariant is R localized
at y-1. For one cylinder variable the full formula is R_g*partial_u.
The proof identifies generic y-fibers as affine surfaces of logarithmic
Kodaira dimension one, rather than assuming a general rigidity statement.

The same note computes every scalar-fiber Euler value of every polynomial
f(y), including repeated roots and exceptional fibers. Their variation
excludes ALL nonconstant f(y) as coordinates or LND slices, even after
arbitrary polynomial stabilization. Three complete internal AI reviews
passed, with exact checks and primary theorem-scope audits. Human review,
formal certification and novelty clearance remain absent.

The latest ledger separately excludes the proposed affine shifts/swaps
a to cA+d or cb+d, and records an actual polynomial four-space where
compatible translations do not yield any compatible affine-linear torus.
Nonlinear torus actions still exist in that control. None of these results
settles unrestricted actions, polynomiality of the test cylinder, or the
general cancellation conjecture. The next step must leave the newly
classified y-fixed route and use genuinely unrestricted structure.

## Previous investigation: complete projectable-action classification and a relative comparison obstruction

General cancellation remains UNSOLVED and novelty UNKNOWN. The completed
[whole-action proof683](research/two-stage-whole-action-and-quotient-lifting-pass683-working.md)
computes the minimally cleared primitive action Theta and its exact kernel
H=C[b,A,T]. Every whole LND preserving H as a subalgebra is exactly
q(b,A)Xi+h(b,A,T)Theta. All preserve the critical plane and fix z there.
The known group, even enlarged by these actions and the specified replicas,
has one open orbit and fixed-z lines on the plane; its conjugated sliced
kernels still cannot generate u. This is NOT a classification of all LNDs.

The completed [comparison proof684](research/two-stage-relative-comparison-and-motivic-audit-pass684-working.md)
excludes every comparison with the displayed deformed first-kind family
that sends its base parameter to a nonzero multiple of a, even after
adding any equal number of free variables. It does not exclude isomorphisms
moving that parameter to an unrelated function. A separate published-
criterion application gives finite-P1-smash-suspended motivic contractibility,
not polynomial stabilization. All full-source reviews and fresh exact
checks passed; human review, formal certification and novelty clearance
remain absent.

The latest ledger also supplies an actual polynomial four-ring with the
same two-divisor generic quotient rigidity and the same missing-line image
pattern. Those coarse quotient properties alone do not recognize an exotic
cylinder. The next construction must go beyond the classified actions and
the excluded relative comparisons; none of these results solves cancellation.

## Previous investigation: every function in the selected plane is excluded as a coordinate or slice

General cancellation remains UNSOLVED and novelty UNKNOWN. The complete
[all-function proof682](research/two-stage-all-plane-functions-euler-profile-pass682-working.md)
extends681 from selected functions to EVERY nonconstant f in C[x,b].
Its entire scalar-fiber Euler profile is the root-count profile of
g(t)=f(t³,-t⁴). The generic value is either0 or at least3, never1.
Thus no such f can be a global coordinate or a slice of any global LND.
This closes that entire subalgebra search, without a polynomial-degree bound.

The note also gives a safeguard inside actual affine four-space: the
smooth retract C[X+X²Y,Z+Z²T] contains no ambient coordinate or LND slice.
It is a product of published Shpilrain--Yu retract examples. Its complete
Euler profile is checked here, without claiming novelty. This retract is
not factorially closed and its kernel is not principal, so it does not
satisfy the stronger hypotheses of the original cancellation problem.

Three full-source internal AI reviews passed, with independent exact
checks. No human expert review, formal verification or novelty clearance
has been obtained. Neither polynomiality nor nonpolynomiality of the test
cylinder follows, and the full cancellation goal remains active.

## Previous investigation: exact global-coordinate and action-completion exclusions

General cancellation remains UNSOLVED and novelty UNKNOWN. The complete
[global-completion proof681](research/two-stage-reciprocal-chart-and-global-frame-gates-pass681-working.md)
shows that the two retained chart functions x=-V and b are individually
NOT global coordinates on the test cylinder. Their nonzero fibers have
divisor class groups Z² and Z³. It also classifies every generic-affine-line
projection retaining x,b and proves that each misses some whole fibers.
This excludes those constructions, not every possible global isomorphism.

An explicit reciprocal involution of an ordinary polynomial principal
open reproduces the apparent polar Jacobian and removes the volume factor.
That calculation cannot distinguish polynomial ambient spaces. Separately,
no fourth independent LND can normalize the known rank-three distribution;
a different global action frame remains outside this exclusion.

All three complete internal AI reviews passed, with independent exact
arithmetic and full proofs rather than finite-degree searches. Human
expert review, formal certification and novelty clearance remain absent.
Neither polynomiality nor nonpolynomiality of this test cylinder is proved,
and the arbitrary complex-threefold cancellation target remains active.

## Previous investigation: three affine-space open charts cover the whole test cylinder

General cancellation remains UNSOLVED and novelty UNKNOWN. The complete
[three-chart proof680](research/two-stage-three-chart-cover-and-complement-limits-pass680-working.md)
constructs an explicit atlas for the ENTIRE two-stage cylinder B from671.
Three translates of one principal open cover B, and each is isomorphic to
a principal open in affine four-space. A finite polynomial Bezout identity
certifies that no point is omitted. This proves ordinary uniform rationality,
not B=C^[4]. It supplies local coordinates everywhere, not global coordinates.

The underlying [chart-and-boundary proof679](research/two-stage-polynomial-chart-and-coordinate-test-limits-pass679-working.md)
identifies B_A with C[v,b,s,T]_h, h=1+v+v²T+b³s, and computes the complete
normalization and conductor of A=0. It also proves that EVERY polynomial
change of the three residual variables still passes the stated Mulay
necessary test. That entire coordinate-search variant is therefore parked;
unrelated presentations or changes mixing the distinguished variable are
not covered by this exclusion.

Neither direction of this particular chart identification extends to the
whole ambient varieties. Known Poloni complement examples also show that
a smooth versus nonnormal boundary cannot alone obstruct polynomial
ambient spaces. The precise global recognition question remains open.

Both complete sources passed three independent full-source internal AI
reviews, supported by exact whole-polynomial checks. Human expert review,
formal certification and novelty clearance are absent. The unrestricted
special-fiber action question below is also unresolved. The cancellation
goal has not been replaced by the atlas or these construction exclusions.

## Previous investigation: every special-fiber action has an explicit Cox-ring lift

General cancellation remains UNSOLVED and novelty UNKNOWN. The complete
[action-lifting proof678](research/two-stage-cox-lifting-and-factorization-obstruction-pass678-working.md)
removes one unproved premise from677. For the specific special fiber
C0=C[V,b,S,T]/(V²T+b³S+V), the auxiliary graded ring is its Cox ring, and
EVERY additive-group action lifts uniquely preserving the integer grading.
The proof computes Pic(C0)=Z, gives both principal-bundle charts, and
establishes the action cocycle and uniqueness explicitly.

The remaining special-fiber question is now exactly whether a degree-zero
LND of C[p,q,v,w,T]/(q³w-p³vT-1) can move p. Fine-homogeneous classification
does not answer this. A proved construction obstruction shows that no
nonzero degree-zero LND preserves the factorization subring
C[p,q,vT,w]. The complement of the critical plane is a known flexible exotic
affine three-sphere, but its actions do not automatically extend across
that plane. No escaping action has been obtained.

Three complete internal AI reviews reconstructed678, and two fresh exact
calculations checked its maps and identities. A justification was clarified
after review; the normalized-linearization uniqueness proof is the one
that establishes injectivity. Human and formal verification remain absent.
Neither this result nor the current literature audit supplies the actual
polynomial-cylinder recognition step. The full cancellation target is active.

## Previous investigation: the remaining two-stage action must move both parameters

General cancellation remains UNSOLVED and novelty UNKNOWN. The complete
[joint-motion proof677](research/two-stage-joint-escape-and-graded-convex-gap-pass677-working.md)
sharpens676's gate. On the critical chart fiber V²T+b³S+V=0, EVERY LND fixing
S or fixing T preserves the critical plane. A chart action escaping that
plane must therefore move both functions on this fiber. The proof uses
complex specializations and Poloni's published Danielewski theorem; it is
not an all-action plane-invariance result.

The note also proves that a displayed action is free but has no slice, and
gives an exact graded presentation with a concrete obstruction to a proposed
convex-degree shortcut. The relevant escaping tangent degree can lie inside
the convex hull of legitimate homogeneous LND degrees. This supplies no
escaping LND, and no local nilpotence of the sum is claimed.

Direct source checks do not provide the missing global recognition step:
the nearest quotient theorem requires factorial closed fibers of the induced
map on the quotient; the residual-variable theorem requires polynomial
fibers at every prime. Neither missing condition follows from the arguments
here. Three full-source AI reviews reconstructed677, with one source-wording
clarification recorded. No cylinder polynomiality or cancellation solution
has been obtained, and formal/human verification remains outstanding.

## Previous investigation: full cylinder invariant and a separate conjecture consequence

General cancellation remains UNSOLVED and novelty UNKNOWN. Building on
[Poloni's September 12 preprint](https://arxiv.org/html/2609.14090v1),
the complete [quadratic-cylinder proof673](research/quadratic-cylinder-flexibility-and-modified-derksen-pass673-working.md)
extends its four-action construction from the Russell cubic to

    X_h={x²y+z²+x+h(t)=0}, for every nonconstant h in C[t].

The cylinder is flexible and its full modified Derksen invariant equals
its entire coordinate ring. The new cubic action is credited to Poloni,
not presented as our independent discovery. No novelty clearance is claimed
for the general-h extension or the conductor deduction.

The [finite certificate675](research/finite-sliced-kernel-certificate-quadratic-cylinder-pass675-working.md)
gives a second, entirely algebraic proof of the invariant equality. An explicit
Bezout identity and a finite derivative recursion express membership in
the algebra generated by sliced kernels. This proof needs neither transitivity
nor the Nullstellensatz. It is not a polynomial-coordinate system.

Together with the established fixed origin of the Russell cubic, this gives
the [precise consequence674](research/russell-cylinder-bgs-conjecture-counterexample-pass674-working.md):
the cubic contradicts Conjecture 1 in BGS arXiv:2312.08421v2, specifically
the proposed implication from a full cylinder invariant to no special-
automorphism fixed point on the BASE. This is a separate conjecture, not
Zariski cancellation. Its version and hypotheses were checked directly.
Neither priority nor human expert verification has been established.

The [two-stage transfer test676](research/two-stage-unit-chart-elliptic-action-barrier-pass676-working.md)
constructs an exact chart through its critical plane, but shows that the
most direct escaping tangent derivation is not locally nilpotent. The
proposed three fixed functions leave genus-one curves, so no nonzero LND
can fix all three. Other actions, including global ones moving the chart
function, remain possible. This is a bounded construction failure, not an
invariant of every cylinder action.

The complete proofs673,674,675 each passed three separate full-source AI reviews,
with independent exact polynomial checks of the finite certificate.
The older flexibility and modified-Derksen notes carry dated corrections.
No polynomial-cylinder isomorphism is proved for the Russell cubic or the
two-stage control. The original global recognition gap therefore remains.

## Previous investigation: genuine two-stage controls and loss of the cylinder ML obstruction

General cancellation remains UNSOLVED and novelty UNKNOWN. The complete
[two-stage control671](research/two-stage-cuspidal-graded-countercontrol-pass671-working.md)
pairs an actual polynomial three-ring with a smooth factorial contractible
nonpolynomial three-ring. Both supplied actions have smooth reduced plinth
support, two genuinely nonlinear modification stages, the same FULL plinth,
the same image ideals in EVERY degree, and the same entire associated graded
algebra and induced derivation. These data do not force exceptional-fiber
normality or polynomial recognition, even together with ordinary topology.

The [cylinder calculation672](research/two-stage-cuspidal-cylinder-ml-drop-pass672-working.md)
then proves ML(R)=C[a] but ML(R[u])=C for that negative control. An explicit
uniform isomorphism after inverting b compares its cylinder with a standard
Danielewski cylinder. Both inverse maps are regular even at a=0. Transporting
an action and clearing invariant b-denominators produces a WHOLE cylinder
action moving a. Only the action extends across b=0; the isomorphism has not
been extended. Trivial cylinder ML does not supply an intrinsic a-moving action.

Both complete proofs passed three internal full-source reviews. The family
has close iterated Koras-Russell antecedents, and the interpolation method is
adapted from Moser-Jauslin--Poloni. No new-family or general-theorem priority
is claimed. Human expert review and formal certification remain outstanding.

Crucially, R[u]=C^[4] is NOT established. Thus this is not a counterexample
to cancellation. It closes a stronger version of a proposed invariant-based
shortcut and leaves the actual polynomial-cylinder recognition gap intact.
Ordinary topology, graded action data and trivial cylinder ML together are
still weaker than the hypothesis required by the original problem.

## Previous investigation: smooth-boundary recognition and arbitrary multiplicities

General cancellation remains UNSOLVED and novelty UNKNOWN. The complete
[recognition proof669](research/smooth-squarefree-plinth-recognition-pass669-working.md)
removes the earlier quadratic restriction: an actual polynomial-cylinder
candidate is affine three-space if a supplied primitive intrinsic action has
smooth squarefree FULL plinth divisor. The proof constructs an exact global
presentation and applies established recognition theorems, with an independent
topological reconstruction of the residual-curve step. It does not prove that
an action satisfying the divisor condition exists on every candidate.

The [all-multiplicity proof670](research/arbitrary-plinth-divisor-tower-finite-criterion-pass670-working.md)
also extends668's exact finite image-ideal test to repeated plinth factors.
At every boundary divisor it reconstructs the entire ring by a finite tower
of monic modifications, retaining the supplied minimal slice. The resulting
all-degree valuation formula has an exact period determined by the residual
field degrees. Hence all-image principality reduces to finitely many exact
ideal equalities, even with arbitrary multiplicities. Neither the test passing
nor principality of every image alone establishes cancellation.

Both complete proofs passed three separate internal full-source reviews.
The local tower existence and the recognition endpoint have published
antecedents; these results are not presented as established new discoveries.
Repeated components really require a different presentation argument, as a
known affine-three-space example demonstrates. In the smooth-support branch,
the remaining recognition condition can be phrased as normality of exceptional
fibers or an intrinsic action moving the fence coordinate, as in641. Neither
has been deduced from the actual polynomial cylinder. Human expert review and
formal certification remain outstanding.

## Previous investigation: a finite exact test in the squarefree-plinth case

General cancellation remains UNSOLVED and novelty UNKNOWN. The
[squarefree-plinth proof668](research/squarefree-plinth-divisor-envelope-pass668-working.md)
gives exact one-stage models at every boundary divisor for a primitive
action on a finite-type complex UFD with polynomial-plane kernel and
squarefree full plinth. The supplied minimal slice generates each
residual constant field. Write their degrees as d_i>=2.

The proof determines every higher image ideal up to a defect supported
on one fixed finite set of base points. For N=lcm(d_i), principality
of ALL image ideals is equivalent to finitely many exact ideal
equalities through degree N. Explicit witnesses in these degrees
then generate an adapted basis in every degree. This is a proved
finite reduction, not extrapolation from a numerical search.
The complete expanded proof passed three internal full-source reviews.

These finite equalities have not been proved for an arbitrary unknown
cancellation candidate. Moreover a known exponent-one second-kind
Koras-Russell threefold has squarefree full plinth, principal images
in every degree, smooth factorial contractible total space and flat
quotient, but is not affine three-space. No polynomial cylinder for
that control is established here. Thus even completing the finite
test would leave a separate recognition argument using the ACTUAL
polynomial-cylinder assumption, and existence of a qualifying action
is itself unproved in general.

No solution, novelty clearance, formal certificate or human expert
review is claimed. The new result narrows one conditional proof route.

## Previous investigation: all invariant-ring-preserving changes

General cancellation remains UNSOLVED and novelty UNKNOWN. The
[full stabilizer proof667](research/nonfence-invariant-ring-stabilizer-normal-form-pass667-working.md)
classifies every polynomial automorphism preserving S=(ker D)[u], under
the explicit primitive, full non-fence plinth and constant-unit hypotheses.
Each uniquely factors into a replica exponential exp(P(u)D), P(0)=0,
and an intrinsic automorphism with an affine slice change. No degree
bound, tameness assumption, or intrinsic rank-one hypothesis is needed.

Consequently all conjugates of the cylinder translation within this
stabilizer have the form beta*partial_u+q(u)D, with beta a nonzero
constant. Their horizontal coefficients cannot supply a second direction
independent of D. This covers all such invariant-ring-preserving changes,
not transformations moving S or arbitrary ways of constructing actions.
An exact fence control shows why the non-fence assumption is necessary.
The complete proof passed two separate internal full-source reviews.

The current literature audit supplied no missing existence theorem. In
particular, universal existence of the affine-linear action required
by666 is equivalent to the original cancellation target, not a weaker
known statement. The linear-threefold result assumes its special
presentation; its general stable-polynomial recognition clauses also
require intrinsic ML or Derksen hypotheses. The simple-root branch
does not need that additional condition.
The detailed source and access limits are in the latest ledger entry.

Neither this classification nor the earlier conditional recognition
proves cancellation. Human expert review, formal certification and a
novelty determination remain outstanding.

## Previous investigation: an intrinsic-action recognition criterion

General cancellation is still UNSOLVED and novelty UNKNOWN. The
[affine-linear recognition proof666](research/affine-linear-intrinsic-action-recognition-pass666-working.md)
proves a sufficient condition on an arbitrary actual cylinder A[u]=C^[4]:
if a nonzero intrinsic additive action, extended to fix u, is affine-linear
in some actual polynomial coordinates of the four-ring, then A=C^[3].
The proof handles both fixed-point and fixed-point-free actions. Its
fixed-point argument forces the cylinder translation to fix an actual
coordinate, so an established regular-kernel theorem applies. A normalized
abelian family of generic rank four also supplies this criterion, without
requiring the cylinder translation to belong to that family.

The [degree-one exclusion664](research/degree-one-commuting-orbit-tangent-exclusion-pass664-working.md)
closes the apparent degree-one escape in662. Saturating the entire fixed
cylinder line, not just one orbit, makes the proposed nonzero tangent
impossible. Within that single commuting conjugation span, tangent
recovery can occur only when T(u)=0, or when T(u) is nonzero and invariant
under the intrinsic action, with the respective tangent condition.

The complete [vertical-kernel proof665](research/rank-one-abelian-vertical-kernel-rigidity-pass665-working.md)
records a further structural restriction under explicit primitive and
non-fence full-plinth hypotheses. With the additional intrinsic rank-one
hypothesis, an abelian ambient family either has no descending constant
combination, or it centralizes the intrinsic action and has generic orbit
rank at most two. All three complete proofs passed two separate internal
source reviews; no theorem about existence of a useful family follows.

Combining664 with the centralizer statement of665 also bounds each such
single-orbit construction by rank two along a fixed cylinder line. That
deduction does not need intrinsic rank one. Its full short proof is in the
latest ledger entry. It is not a bound on arbitrary families or arbitrary
points.

The remaining obligation is unchanged: construct a qualifying action or
give another general recognition argument for every actual cylinder.
These notes have no human expert review, formal certificate, or novelty
clearance. Conditional recognition and excluded proof routes do not solve
the main conjecture.

## Previous investigation: exact cutoff for commuting-orbit descent

General cancellation is still UNSOLVED and novelty UNKNOWN. The
[whole-orbit proof662](research/commuting-orbit-coefficient-tangent-test-pass662-working.md)
gives an exact test for recovering an intrinsic additive action from
a commuting conjugation family. If e is the degree of T(u) under the
intrinsic action L, only adjoint coefficients of order greater than e
can descend through u=0. At an L-fixed smooth threefold point, the
entire family fails to move that point when e is at least two.
In the remaining cases the first descending coefficient suffices
exactly when its stated tangent vector is nonzero.

This corrects a tempting interpolation shortcut: higher coefficients
cannot cancel lower vertical values within a single orbit. Root found
that mistake after two initial AI reviews had missed the explanatory
sentence. The corrected full proof received two fresh internal reviews.
An exact control has three independent tangent directions but no
nonzero combination that actually descends.

The [single-shear boundary663](research/dg-single-mixed-shear-leading-line-obstruction-pass663-working.md)
also proves that every single mixed slice shear of a specified DG flow
frame retains the same one-dimensional intrinsic leading span. There
is no degree bound on the shear polynomial. The example's base is
already affine space; it is not a cancellation counterexample, and
the statement does not cover sequences of shears.

Neither result constructs the required action on an arbitrary unknown
base. The next obligation is a general existence argument meeting the
nilpotence and quotient conditions, not more variations of the DG
example. These notes have no human expert review or formal certificate.

## Previous investigation: all-slice obstructions and the section-lifting gap

General cancellation is still UNSOLVED and novelty UNKNOWN. The
[uniform family proof658](research/all-slice-linear-frame-family-classification-pass658-working.md)
shows that changing the slice and trying every constant linear frame
can still fail to produce the commuting basis required by656. It
classifies exactly when that repair works in an explicit family.
The bases in these examples are already polynomial, so these are
limits of the repair method, not cancellation counterexamples.

The [higher-derivative test659](research/slice-shift-higher-derivative-ideal-obstruction-pass659-working.md)
gives a finite necessary test in the ambient polynomial ring. Its
failure excludes every polynomial slice shift and every linear
frame at once, and also all polynomial frame changes preserving
the supplied embedded invariant algebra. Nonlinear changes moving
that algebra are not excluded. Keeping the ideal's nonreduced
structure is essential; replacing it by its radical can lose the
obstruction.

Passing the test is not enough. The
[proper-ideal controls660](research/proper-higher-derivative-ideal-nonsection-control-pass660-working.md)
pass it while excluding every polynomial graph correction and linear
frame, even with a proper reduced ideal. The
[formal-lifting proof661](research/residual-normal-formal-graph-lifting-gap-pass661-working.md)
identifies the next exact obstruction and gives examples that exclude
even a formal graph along the whole divisor. Other explicit controls
have formal corrections that are rational but not polynomial, or
algebraic but not rational. Point-local existence does not remove
these global gaps.

All four complete saved proofs passed two separate internal AI
reviews in addition to root reconstruction. One review requested
that658 state its field hypothesis explicitly; that correction was
made and checked. Fresh exact calculations verify the example maps
and identities, not the universal conclusions by finite sampling.
These are not human expert reviews, formal certificates, or novelty
determinations.

The ledger also proves that summing the higher-derivative ideals
over every nonlinear frame always gives the unit ideal, so that
particular extension cannot supply a coordinate-independent obstruction.
The remaining obligation is a genuinely useful nonlinear-frame or
intrinsic-action construction for an arbitrary actual cylinder.
The full goal remains unchanged; these examples do not solve it.

## Previous investigation: a stronger projected-frame recognition criterion

General cancellation is still UNSOLVED and novelty UNKNOWN. The
[new recognition proof656](research/three-commuting-projected-partials-unit-normal-recognition-pass656-working.md)
needs only three of the four projected coordinate directions to
commute and form a basis everywhere. Under those conditions it
constructs actual polynomial coordinates on the retract. Local
nilpotence need not be assumed, and the theorem works for principal
polynomial retractions without an initial cylinder presentation.

The proof reduces the coefficient data to one polynomial curve,
then shows that a one-extra-generator presentation must eliminate
that extra generator. Both steps are written in full. Two separate
AI reviewers read the entire saved proof and found no gap; fresh
exact calculations check the complete positive and negative controls.
These are internal checks, not human expert review or formal certification.

This criterion is strictly less restrictive than the
[all-four-direction test654](research/commuting-projected-partials-retraction-recognition-pass654-working.md):
it succeeds in an explicit fixed frame where no retraction with
that kernel can make all four projected directions commute. Mere
generic independence is insufficient, as a contrasting actual
cylinder demonstrates. The basis must hold everywhere.

The [frame-change boundary655](research/hypersurface-preserving-frame-obstruction-pass655-working.md)
also shows exactly when preserving the zero hypersurface can repair
the earlier all-four test, including its formal constant-normal
version. Separately, a finite-dimensional Lie algebra of projected
fields can still contain noncomplete fields, so that shortcut fails.

The [exact frame-selection test657](research/constant-linear-frame-projected-commutation-test-pass657-working.md)
searches ALL constant linear ambient coordinate changes for this
criterion through one finite linear system. It can recover a useful
combination even when every listed normal component is nonconstant.
An inconsistent system excludes linear changes for that retraction,
not nonlinear changes or a polynomial base. Its complete saved proof
also passed two separate AI reviews and fresh exact control checks.

The unresolved obligation is to produce a useful commuting basis
for an ARBITRARY actual polynomial cylinder, or a different general
recognition argument. None of these conditional results establishes
that existence statement or a solution of cancellation. The
[ledger](research-ledger.md) records full evidence and next tasks.

## Previous investigation: an entire quotient-and-lift family is exhausted

General cancellation is still UNSOLVED and novelty UNKNOWN. The
constant-speed action D+b*partial_u on the known second-kind control
now has a complete [kernel and plinth calculation651](research/constant-speed-cuspidal-quotient-plinth-pass651-working.md).
Its plinth has an extra generator beyond the initially visible two.
The quotient is normal but singular, and its quotient map misses
most points of its singular line. These exceptional features were
checked explicitly rather than inferred from the smooth source.

The [full action classification652](research/cuspidal-quotient-full-lnd-classification-pass652-working.md)
then proves that EVERY additive action on this quotient fixes the
original two base variables. The proof handles arbitrary actions by
a degree filtration and an explicit normalization of the exceptional
graded case. It applies uniformly with any base polynomial in place
of the quotient equation's lower term. Thus the extra plinth generator
cannot supply the missing base-moving auxiliary action through this
construction. Both saved proofs passed complete separate AI reviews;
neither is expert-reviewed or formally certified.

The [all-coefficient result653](research/all-constant-base-speeds-lifting-obstruction-pass653-working.md)
now handles EVERY f in C[a,b] in D+f*partial_u, including zero.
Three divisibility cases have different whole invariant algebras;
their exceptional-divisor saturation is proved separately. A second
graded-action argument, checked both against a published rigidity
theorem and by an explicit polynomial-orbit proof, closes the last
case. No plinth-compatible auxiliary lift in this entire family can
move the base. Two complete independent AI source reviews passed.

This closes a specific construction on a known nonpolynomial control.
It does not classify all cylinder actions, compute the cylinder's
full invariant, or establish a polynomial cylinder. The remaining
general obligation is to use the ACTUAL polynomial-cylinder assumption
to supply an action or recognition argument beyond these constructions.

## Previous investigation: nonlinear action repair and a changed-quotient lifting gate

General cancellation is still UNSOLVED. The current source audit
confirms one nonzero intrinsic additive action, not two independent
ones. A misleading sentence in the older quotient-foundation note51
has been corrected to preserve this distinction.

The [repair tests649](research/simultaneous-replica-and-whole-frame-descent-gates-pass649-working.md)
give two whole polynomial controls. Individually valid invariant
replicas can cancel to a tangent field commuting with the sliced
action that is nevertheless not locally nilpotent. Separately, a
genuine elementary coordinate change can lower the selected partial
while increasing the whole frame's height. Successful alternative
repairs are explicit in both examples; neither rules out all repairs.

The [changed-action proof650](research/polynomial-speed-suspension-plinth-gate-pass650-working.md)
tests an entire family, Delta=P(u)D+f*partial_u, with nonconstant
scalar polynomial P and nonzero D-invariant f. Its full plinth is
exactly f*ker(Delta), and all such P have isomorphic quotient
algebras. Plinth-compatible lifting from these actions cannot move
the original base's Makar-Limanov invariant. This is a restriction
on that construction, not a stable-invariant or cancellation theorem.
Both notes passed two complete saved-source AI reviews. They have
not received human expert review or formal certification.

The next bounded investigation changes to the constant-speed action
D+b*partial_u on the second-kind control625 and computes its whole
quotient before testing a new lift. The constant-speed case is
explicitly outside650's universal plinth formula. No polynomial
cylinder for that control, new independent action, or general
recognition argument is being assumed. Novelty remains UNKNOWN.

## Previous investigation: retraction obstructions and a checked transfer boundary

The [retraction note647](research/kr-retraction-zariski-etale-gap-pass647-working.md)
has passed two complete saved-source AI reviews. For every m,p,q>=2,
no retraction onto X={x+x^m y+z^p+t^q=0}, defined on a Zariski
neighborhood of the entire X, can preserve z^p+t^q exactly. The proof
uses units and localization and has no degree bound or coprimality
assumption. Any affine-space retract presentation would give a
retraction for this standard embedding, but need not preserve that
polynomial. Thus the obstruction does not exclude general retractions.

Compatible retractions preserving z and t nevertheless exist at EVERY
finite order. For the Russell cubic, the specified formal solution
comes from an explicit etale neighborhood but is not rational over
the ambient function field. A coordinate-hyperplane comparator shows
why one nonrational formal solution cannot rule out another global
polynomial solution. More finite Taylor orders cannot close this gap.

The [transfer note648](research/principal-retraction-birational-transfer-pass648-working.md)
then closes another proposed shortcut. Even transferring the ordinary
projection of actual affine space can produce a retraction with
principal kernel and factorially closed polynomial image but with
no compatible nonzero ambient additive action. An explicit family
has generic fibers of every positive genus. Both reviewers read
the full source and reported CLEAN.

The same note gives an elementary positive test: for a supplied
retraction with kernel(s), factorial closure plus the exact equality
Frac(B)=Frac(A)(s) implies B=A[s]. The countercontrol loses this
field equality by degree2g. The final descent step is attributed to
Das-Dutta's published Lemma3.6 and Remark3.7. This tests product
structure for that retraction; it neither supplies a successful
transfer nor proves that an unknown base is affine three-space.

The next obligation is a global consequence of the actual cylinder
that controls unrestricted coordinate mixing. Neither that consequence
nor the general cancellation theorem is proved. Cancellation remains
UNSOLVED; novelty remains UNKNOWN. AI reviews are not expert review or
formal certification.

## Previous investigation: smooth covers and a false section shortcut

The [explicit cover645](research/kr-polynomial-domination-smooth-cover-pass645-working.md)
has passed full saved-source AI review. For every m,p,q>=2 it gives
an everywhere smooth surjection A5 onto the hypersurface
x+x^m y+z^p+t^q=0, including its exceptional locus. Its fibers are
computed exactly. It supplies neither a retraction nor a product
structure, and it is not a cancellation proof.

The new [section audit646](research/smooth-affine-cover-no-rational-section-pass646-working.md)
proves that this cover has no rational section after ANY affine base
stabilization unless (p,q)=(2,2); that exception has an explicit
section. Crucially, the failure is not a cancellation obstruction:
646 also constructs a smooth surjection A5 -> A3 between ACTUAL
affine spaces with the same failure, including after stabilization.
Its smoothness has a uniform exact gradient-ideal certificate, and
surjectivity has explicit preimage formulas. Two separate reviewers
read the entire saved proof and reported CLEAN.

This rules out the proposed inference from smooth covering to a
rational section, even with the same dimensions as645. The actual
cylinder supplies a different splitting: a regular retraction and
extension across closed affine embeddings. The notes distinguish
that property from sections of smooth surjections and from algebraic
Oka conditions. The general existence gap has not been resolved.
Cancellation remains UNSOLVED; novelty remains UNKNOWN. These are
AI-assisted proof checks, not expert review or formal certification.

## Previous investigation: checked extraction obstruction and nonlinear descent limits

The [slice-scaling note644](research/slice-scaling-root-extraction-closure-pass644-working.md)
has passed a complete saved-source AI review. It classifies all
homogeneous additive actions for the actual cylinder grading. In the
explicit polynomial frame from643, extracting EVERY locally nilpotent
homogeneous component of EVERY constant direction, including primitive
division, still finds only two primitive directions. Their permitted
recombinations and internal flow conjugations cannot leave a specified
relative-derivation module. Other homogeneous actions do escape it, so
this is a limitation of the extraction procedure, not of all actions.

The next attempted repairs were checked against the existing archive.
Variable-time substitution already has the exact obstruction in23.
Forcing its defining ideal to be invariant preserves local nilpotence
exactly when the full horizontal field was locally nilpotent already.
A finite polynomial adjoint orbit also need not generate a finite Lie
algebra, even with just the sliced field and one coordinate partial.
The proofs, exact checks, deduplication and source gates are recorded
in the [ledger](research-ledger.md). No additional numbered note was
created for these consequences. The general existence gap is unchanged:
cancellation remains UNSOLVED and novelty remains UNKNOWN.

## Previous investigation: an exact nonlinear repair test, with no general existence proof

The latest pass turns polynomial recombination into a bounded linear
test whose candidates are locally nilpotent by construction. In a
given ambient coordinate order, search for a strictly triangular
derivation T commuting with the supplied sliced E. If the independent
commuting pair of641 is available, T moving its common invariant f
is a sufficient recognition certificate. The test does not assume
coordinates on the unknown base, but no successful bound or coordinate
order is guaranteed.

On the explicit fixed-line control in643, imposing also T(u)=0 gives
no nonzero candidate through degree three. At degree four there is
exactly one direction, and it has an intrinsic slice. A full written
classification proves that threshold; separate fresh exact linear
searches and algebra checks confirm it. Thus the control is repairable
by certified nonlinear recombination, not only by being handed its
inverse coordinates.

This is a bounded operational consequence of existing recognition
arguments, not a new general cancellation theorem. No additional
numbered theorem note was created. The renewed global-fiber source
audit still requires an ambient presentation that has not been
constructed. Full details and limits are in the [ledger](research-ledger.md).
The main conjecture remains UNSOLVED and novelty remains UNKNOWN.

## Previous investigation: two checked limits of action-based approaches

General cancellation remains UNSOLVED. Two additional working arguments
have passed complete saved-source review by separate AI reviewers and
fresh exact algebra checks. They eliminate specific proof shortcuts;
they do not establish cancellation or literature novelty.

The [formal-neighborhood control642](research/critical-plane-formal-action-nonalgebraization-pass642-working.md)
constructs compatible translation actions on EVERY finite neighborhood
of a Koras-Russell-type critical plane. Those particular actions cannot
come from even a global regular derivation: their forced formula has
a pole away from that plane. A polynomial comparator has the same
completed local data but different general fibers. Thus these formal
data alone cannot supply the required global action. This is not a
claim that the candidate cylinder is polynomial or that all possible
global actions are excluded.

The [whole-frame control643](research/primitive-leading-fixed-locus-frame-obstruction-pass643-working.md)
shows that ANY prescribed primitive locally nilpotent derivation on
a known polynomial three-ring can arise as the primitive leading part
of EVERY nonzero constant direction in one actual polynomial
four-coordinate frame. Individual invariant replicas and vertical
shifts preserve this outcome, even when interleaved finitely many
times. Consequently, that extraction procedure cannot by itself
guarantee a free action or a favorable invariant divisor. Arbitrary
nonlinear changes of coordinates and recombinations of transformed
directions are explicitly outside this obstruction.

The remaining gap still requires genuinely global use of the actual
polynomial cylinder, or a stronger action-selection construction.
Neither argument excludes such a construction. See the
[research ledger](research-ledger.md) for the exact hypotheses,
verification evidence, and limitations. These are AI-assisted checks,
not human expert review or Lean certification.

## Previous investigation: published recognition sharpens the intrinsic-action gap

General cancellation remains UNSOLVED. The independently reviewed
[conditional result641](research/kaliman-intrinsic-ml-recognition-pass641-working.md)
applies Kaliman's published recognition and Makar-Limanov theorem to
the actual A[u]=C^[4] setup WITH a supplied independent commuting pair.
For that pair's common invariant f, it proves

    A=C[f,t,s]
      iff Crit(f) is empty
      iff ML(A)=C
      iff some intrinsic LND E has E(f)!=0.

Normality of every exceptional f-fiber is another equivalent test.
The proof checks the actual open affine-plane cylinder, topology,
and integral fibers needed by the published theorem. It also
handles a possible change of parameter on the open base curve,
so the conclusion uses the supplied f itself.

If the coordinate presentation fails, then ML(A)=C[f], at least one
exceptional fiber is nonnormal, and EVERY intrinsic additive action
fixes Crit(f) pointwise. That locus contains a curve. This is a
conditional description, not an example under the polynomial-cylinder
hypothesis and not a proof that the bad branch is impossible.

The missing steps remain existence of a suitable commuting pair and,
even with one supplied, a cylinder argument forcing the positive
branch. ML(A[u])=C does not establish ML(A)=C. The recent literature
checked here retains the base-invariant condition as an extra premise.
This gap already includes the Koras-Russell cubic cylinder question.

The [ledger](research-ledger.md) also records an exact flow-transfer
control and a replica-normalizer boundary. The zero constant-normalizer
obstruction was already known in this archive, so no duplicate note
was created for that result. These controls reject shortcuts; they do not exclude
nonlinear constructions or establish cancellation.

Result641 is a published-theorem application with separate AI-assisted
proof reviews, not a new recognition theorem, human expert review,
or Lean certification. Novelty remains UNKNOWN and the full goal
is unchanged.

## Previous investigation: recognition and the fixed-base critical-locus obstruction

General cancellation remains UNSOLVED. The reviewed
[intrinsic Jacobian proof637](research/intrinsic-primitive-jacobian-normalization-pass637-working.md)
works on the actual unknown A with A[u]=C^[4], without a polynomial
coordinate frame on A. A primitive LND with actual plane kernel
C[f,g] is a nonzero constant multiple of the intrinsic Jacobian
J(f,g). For a primitive independent commuting pair with kernels
C[f,g], C[f,h], the cross-values Ph and Qg are constant associates.
They need not be constant polynomials.

The reviewed [recognition proof639](research/no-joint-fixed-point-recognition-pass639-working.md)
then proves the following CONDITIONAL result:

    If such a pair has no common fixed point, A=C[f,t,s].

The Jacobian identities put every critical point of f in the joint
fixed locus. Its absence makes every f-fiber smooth. Factorial
closure gives nonempty integral fibers, the local slice gives the
actual open affine-plane chart, and published acyclicity and
recognition theorems finish the argument. Existence of the required
pair is not proved. Its universal existence on all A[u]=C^[4]
would be equivalent to the cancellation statement, not a weaker
entry that has already been established.

The reviewed [fixed-base theorem640](research/fixed-base-critical-locus-obstruction-pass640-working.md)
strengthens the obstruction beyond any prescribed pair: EVERY LND E
with E(f)=0 fixes Crit(f) pointwise, even if E commutes with neither
original action. For each nonzero E, its proof makes f an actual
coordinate of ker E by spreading the generic invariant line and constructing a whole
plane LND. Under the supplied-pair hypotheses, it gives the exact gate

    Crit(f) is empty
      iff A=C[f,t,s]
      iff some free LND E satisfies E(f)=0.

Thus even arbitrary reselection of actions preserving f cannot
remove critical points. This action-based route must establish smoothness
of such an f using the cylinder, or obtain a useful different common
invariant. Neither step is proved. No critical f is claimed actually
to exist under the cylinder hypothesis.

The reviewed [multifiber descent638](research/multifiber-embedded-residue-descent-pass638-working.md)
has a different, constructive output under an EXTRA premise: at
each exceptional fiber, the joint residual algebra C[gbar,hbar]
must equal C[t_c], with C(t_c) the full residual invariant field.
Classical embedded-line degree reduction,
localized by interpolation in f, then gives a finite list of whole
LND shears. A strictly decreasing sum of residual degrees proves
termination. Whole kernel contraction and637 preserve primitivity;
the boundary plinth criterion supplies a free action on each entire
exceptional fiber, and explicit polynomial coefficients glue them.
The resulting free action has a slice by published recognition.

This descent does NOT remove existing common fixed points. Its
invertible polynomial changes preserve the joint fixed ideal, so
its input premise already implies that the original pair has no
common fixed point. No broader recognition regime than639 is claimed.

These are separate AI-assisted written-proof reviews and fresh exact
algebra checks, not human expert review or Lean certification.
Novelty remains UNKNOWN. The original arbitrary entry and general
modification-recognition gaps remain open, and the full goal is unchanged.

## Previous investigation: even the entire fixed-pivot centralizer can fail

General cancellation remains UNSOLVED. The reviewed
[centralizer obstruction636](research/fixed-pivot-shear-obstruction-pass636-working.md)
rules out a stronger shortcut than fixed-pivot division or a bounded
coefficient search. On the actual polynomial ring C[x,y,z], set

    r=xz+y^2,  g=r^2+y,
    Q=x partial_y-2y partial_z,
    P=2rQ-partial_z.

The two fields are primitive commuting LNDs with no common fixed
point. Their exact kernels are C[x,g] and C[x,r], and both full
plinths are (x). Nevertheless the ENTIRE LND centralizer of P is

    {a(x)Q+b(x,g)P : a in C[x], b in C[x,g]},

and every member has fixed points on x=0. This includes every
invariant-dependent shear Q-HP with H in ker P, and the obstruction
persists after primitive division. The proof treats every polynomial
coefficient and every commuting LND, not a finite search ansatz.
These fields all commute with P, not necessarily with one another.

Switching the pivot succeeds immediately:

    P-2rQ=-partial_z.

Thus a viable general free-action construction cannot insist on
commuting with one fixed intrinsic action. The example is already
affine three-space, not a cancellation counterexample or a new-family
claim. Its residual identity gbar-rbar^2=y explains its successful
degree reduction, but no universal alternating-pivot descent follows.

The reviewed [saturated-module control634](research/saturated-pencil-no-free-direction-pass634-working.md)
also excludes automatic free-direction selection inside an entire
C(f)-saturated module, even with no joint fixed points and smooth
affine-plane fibers. The reviewed [gluing criterion635](research/fiberwise-free-direction-gluing-pass635-working.md)
gives the precise conditional alternative: a free C[f]-linear
combination exists exactly when every exceptional whole fiber has
some free constant direction. Coprime interpolation then produces
a free action, and published recognition gives actual coordinates
A=C[f,t,s]. Control634 shows that the fiberwise premise is not
automatic under the full cylinder hypothesis.

The next unresolved action-selection issue is an alternating-pivot
procedure with justified whole-ring operations and a terminating
invariant. Existing modified commuting-chain results start with a
global polynomial plane over the base; that is not supplied by a
generic plane chart on the unknown A. The original arbitrary entry
and modification-recognition gaps also remain open.

These are separate AI-assisted written-proof reviews and fresh exact
algebra checks, not human expert review or Lean certification.
Novelty remains UNKNOWN, and the full cancellation goal is unchanged.

## Previous investigation: monic reduction and a failed fixed-pivot shortcut

General cancellation remains UNSOLVED. The separately reviewed
[normalization631](research/nonlinear-two-stage-monic-normalization-pass631-working.md)
removes the first-stage monicity and residual-domain assumptions
from the nonlinear two-stage analysis. For the exact supplied
presentation on R=C^[3], with actual A=ker(D), f irreducible and
Dr=f^2, it preserves A,D,r and gives

    R=A[r,y,z]/(fy-G(r), fz-y^m-K(r,y)),
    G monic of degree n, deg_r K<n, deg_y K<m.

The actual residual curve is free of rank nm over A/f. The same-r
collapse R=A[r,w] holds exactly when m=1. Exact plinth f^2 forces
n>=2; a remaining rank-three candidate in this presentation class
must have n,m>=2. This normalizes equations, not integral closures,
and does NOT prove the residual curve normal.

The separately reviewed [filtration proof632](research/two-stage-mixed-radix-basis-and-image-ideals-pass632-working.md)
gives a basis r^i y^j z^k with i<n,j<m and, in every degree N,

    D^N(R) intersect A
      = f^(2N-floor(N/n)-floor(N/(nm))) A.

It has a uniform written proof, not an extrapolation from numerical
checks. The associated graded ring forgets the lower coefficients
and is always nonnormal when f is a nonunit and n>=2, even for
polynomial R. Neither principal images nor graded normality supply
the missing recognition argument.

A separate investigation addresses the unknown stably polynomial
threefold directly. The reviewed [fixed-pivot criterion633](research/intrinsic-fixed-pivot-residue-repair-pass633-working.md)
starts with commuting independent intrinsic actions P,Q, P primitive,
ker P=C[f,g], and Q(g)=q(f). At a root F=f-c of q, the repair

    W=(Q-H P)/F, H in ker P,

is possible exactly when the residual ratio Qbar/Pbar belongs to
C[gbar]. A successful repair is a whole LND and lowers deg(q) by
one; successful repairs through all roots give actual coordinates.
Lifting is automatic away from the pivot's plinth support.

Automatic lifting at the remaining roots is FALSE, not a missing
theorem to assume. Already on C[x,y,z], the primitive nonsliced pair

    P=x partial_y+2y partial_z,
    Q=x partial_y+(2y+1) partial_z

has Q(xz-y^2)=x but residual ratio 1+1/(2y), which cannot lift
from C[-y^2]. No polynomial H makes Q-HP divisible by x.
Nevertheless Q-P=partial_z has a slice. A viable general strategy
must allow changing the action pair or justify a stronger selection
condition; fixed-pivot divisibility is not universal.

The original four-variable entry and arbitrary modification
recognition remain open. These are separate AI-assisted proof
reviews and fresh exact-algebra checks, not human expert review
or Lean certification. Novelty remains UNKNOWN, and Luo has not
confirmed the working complex-threefold interpretation.

## Previous investigation: narrowing exact prime-square presentations

General cancellation remains UNSOLVED. The separately reviewed
[linear-stage lemma628](research/general-linear-two-stage-rank-obstruction-pass628-working.md)
removes the monicity and residual-domain assumptions of the earlier
[restricted lemma626](research/monic-linear-two-stage-rank-obstruction-pass626-working.md).
For R=C^[3], actual A=ker(D), f irreducible, Dr=f^2 and an EXACT
presentation

    R=A[r,y,z]/(fy-G(r), fz-u(r)y-K(r)),

it proves R=A[r,W], hence rank(D)<=2. The proof first selects the
actual finite exceptional curve, recovers a monic equation from
finite flatness, and then gives polynomial recovery formulas.
The original residual curve can be reducible: its localization
may discard a component. No claim that u is a unit on every
discarded component is made. The final rank deduction applies
published KVZ results, not a new general embedding theorem.

The separately reviewed [exponent budget630](research/triangular-denominator-exponent-budget-pass630-working.md)
also limits an exact global triangular chain with denominators
f^(a_i), all a_i positive, and D(t_0)=f^e:

    e >= sum a_i,   gcd_R D(R)=f^(e-sum a_i).

Thus a primitive action has e=sum a_i, and every such chain has
at most e stages. This is about the CHOSEN slice, not necessarily
the minimal plinth exponent. At a minimal prime-square slice,
one stage is already covered by621; the only remaining possibility
in this presentation class is a genuinely nonlinear two-stage case.

The separately reviewed [residue criterion629](research/nonlinear-two-stage-residue-degree-and-ramification-pass629-working.md)
shows that the exceptional curve algebra B is finite locally free
over C=A/f. When the first-stage polynomial is monic with integral
residual algebra S, the same-r collapse R=A[r,W] holds exactly when
[Frac(B):Frac(S)]=1. A published polynomial family has this degree
arbitrarily large even with exact plinth f^2, so a degree bound cannot
be inferred from the stage bound. The residual Jacobian determinant
also gives the exact fixed subscheme on the exceptional surface.

The separately reviewed [coordinate certificate627](research/two-stage-modification-center-shear-and-coordinate-control-pass627-working.md)
computes the exact change of the second center for a general
two-stage modification. It also gives full forward and inverse
polynomial coordinates for the class

    A=C[f,s], G(r)=g(f,r)-s, H(r,y)=r+F(f,y), V=1+fQ(f,s),

with arbitrary g,F,Q. This construction need not preserve the old
invariant plane. It is a concrete certificate in a known rank-at-most-two
setting, not recognition of arbitrary rank-three inputs.

Recognition in the remaining nonlinear case and the existence of
usable global presentations remain open in this investigation.
The full relative-isomorphism obstruction was already proved in19
and is not counted again. Neither arbitrary modification recognition
nor the four-variable entry to cancellation is solved. Novelty is
UNKNOWN; the reviews are separate AI-assisted checks, not human
expert review or Lean certification.

## Previous investigation: the single-prime case requires a polynomial-specific argument

General cancellation remains UNSOLVED. The source-dependent
[normality criterion624](research/single-prime-plinth-normality-rank-gate-pass624-working.md)
shows that, for a primitive D on R=C^[3] with sole plinth f^e,
the exceptional surface R/fR is normal if and only if f is a
kernel coordinate, if and only if D has rank two. In that case
f is an ambient coordinate and the surface is actually A2.
Every point above a singular point of the reduced plinth curve
is nonnormal on the exceptional surface. This holds for all e>=1;
it does not establish normality when e=2.

The [known Koras-Russell control625](research/prime-square-cuspidal-plinth-smooth-factorial-control-pass625-working.md)
rules out deriving that missing assumption solely from smoothness,
factoriality, faithful flatness, contractibility or principal
higher-image ideals. Its explicit ring is

    B=C[a,b,s,t]/((b^2-a^3)^2 t-s^5+b),  f=b^2-a^3,
    D(s)=f^2, D(t)=5s^4, D(a)=D(b)=0.

It has exact plinth f^2 and I_j=(f^(2(j-floor(j/5)))), yet B/fB
is the nonnormal cusp cylinder C[a,s,t]/(s^10-a^3). This is a
known NONPOLYNOMIAL threefold, not an example in C^[3] or a
cancellation counterexample. The all-degree assertion has a
monic-basis proof, not a finite numerical extrapolation.

These results narrow one subproblem; they do not replace the
full cancellation goal. The unresolved step needs the actual
polynomial-ring hypothesis or a construction in that exact ring.
Novelty is not asserted, and no human expert or Lean review has
occurred. The arbitrary modification and four-variable entry
problems remain unresolved.

## Previous investigation: fixing the old plinth cannot supply a new action

General cancellation remains UNSOLVED. The separately reviewed
[action classification623](research/rank-three-modification-lifted-action-classification-pass623-working.md)
works on the actual modification M=R[r/V], where R=C^[3], D is
primitive of rank three, A=ker(D), Dr=p generates its plinth,
rho=rad(p), and V=1+rho Q with Q nonzero. Put Delta=VD on M.
It proves the exact equality

    {Theta in LND(M): Theta(p)=0}
      = {Theta in LND(M): Theta(V)=0}
      = {Theta in LND(M): Theta(R) is contained in R}
      = A Delta.

Thus an action with a different kernel must move both p and V
and fail to preserve the original R. Fixing p or V does not
initially assume preservation of R. The proof uses Daigle's
kernel-intersection result on the stably polynomial M and applies
the coordinate-transfer lemma only on the original polynomial R.
The condition p dividing rho^2 is not needed for this result.

No action in this restricted class has a slice. If M is polynomial,
each coordinate partial must therefore lie outside the class.
This is not a nonpolynomiality proof or a classification of all
actions. Already solved polynomial examples require just such
moving actions. The next recognition attempt must construct those
actions or coordinates, rather than repair only p-fixed actions.
Novelty remains UNKNOWN; no human expert or Lean review has occurred.

## Previous investigation: two global-presentation shortcuts are excluded

General cancellation remains UNSOLVED. The separately reviewed
[one-generator obstruction621](research/global-one-generator-rank-obstruction-pass621-working.md)
applies published KVZ theorems: if R=C^[3], A=ker(D), r is ANY
local slice, and R=A[r,q], then A contains an actual coordinate
of R. Thus rank-three actions admit no such global reconstruction.
This is a consequence of prior work, not a claimed new theorem.

The separately reviewed [cylinder obstruction622](research/global-triangular-presentation-cylinder-obstruction-pass622-working.md)
addresses exact global triangular presentations with more stages.
A prime dividing the last denominator must cut out a curve times
an affine line. It cannot cut out a surface with an isolated
singular point. This excludes the proposed same-denominator
globalization for the standard DG rank-three family, whose
xz-y^m=0 divisor has an isolated singularity. Localized
presentations can remove that point and are not contradicted.
A published rank-two control also shows that genuine two-stage
structure need not collapse to one extra generator.

These results narrow the proof route, not the cancellation statement.
The next recognition argument must retain the omitted locus and
allow more general global centers, relations, or actions. Neither
global polynomiality of the arbitrary first-nonreduced-plinth
modification nor arbitrary four-variable entry is established.
Novelty is not asserted; no human expert or Lean review has occurred.

## Previous investigation: a coordinate-preserving obstruction and a corrected proof frontier

General cancellation remains UNSOLVED. The independently reviewed
[induced-action proof614](research/nonunit-speed-coordinate-induced-action-pass614-working.md)
starts with a sliced derivation E on B=C^[4], B=A[u], Eu=1, and ONE
actual ambient coordinate v=au+b with a a nonzero nonunit of A=ker(E).
Every coordinate partial for v has nonnegative u-degree shift. Its
full leading derivation induces a nonzero LND N on A with N(a)=0.
At shift zero the two derivations commute and give an actual
presentation E=H+a partial_v over the polynomial three-ring ker(D).
No existence of the first coordinate, or of a zero-shift completion,
is assumed or proved for an arbitrary input.

The [whole polynomial example615](research/venereau-coordinate-positive-shift-obstruction-pass615-working.md)
and [uniform refinement617](research/venereau-coordinate-shift-one-exclusion-pass617-working.md)
show that the zero-shift choice can be impossible for a specified
coordinate. On C[x,y,z,u], with E=partial_u, set

\[
v_n=y+x^n\bigl(xz+y(yu+z^2)\bigr).
\]

For EVERY LND D satisfying D(v_n)=1, its exact u-degree shift is
at least 2. This conditional statement holds for n>=1. For n>=3,
an explicit whole polynomial flow and its inverse complete v_n to
coordinates, and that completion has shift 10. Thus the lower bound
is not vacuous in the stated coordinate range. The minimum between
2 and 10 is not determined. The Vénéreau coordinates themselves
are classical prior work, not discoveries of this project.

The subsequent [uniform x-fixed obstruction619](research/venereau-x-fixed-shift-two-exclusion-pass619-working.md)
proves the stronger bound delta(D)>=3 whenever Dx=0, for every n>=1.
The proof compares exact polynomial coefficients and uses the whole
zero-divergence identity, including the derivative of the middle
coefficient of Dz. Its final identity reduces to 0=-2. Thus for n>=3
the x-fixed minimum lies between 3 and 10. The unrestricted minimum
still lies between 2 and 10: this argument does not infer Dx=0 or
exclude a shift-two derivation that moves x. The proof and its exact
algebra received separate checks; this is a restricted result.

The [shift-two audit618](research/venereau-shift-two-constraints-and-failed-lift-pass618-working.md)
records the unrestricted necessary coefficient equations and an exact
false positive: a polynomial derivation sends v_3 to 1 and has a locally
nilpotent initial action, but nonzero divergence rules out local
nilpotence of the whole derivation. Matching the leading action and
the slice equation is therefore not a sufficient completion test.

The independently audited [moving-x proof620](research/venereau-moving-x-residue-and-volume-control-pass620-working.md)
retains all moving-x terms and derives an exact necessary coefficient
relation with value 2/11, in two independent all-degree reconstructions.
It is a consistency condition, not a contradiction. Two entire
polynomial derivations satisfy the slice equation, zero divergence,
and the locally nilpotent u-initial test, but are not locally nilpotent.
One moves x modulo x; its full ordinary-degree initial action supplies
the rejection. Even adding zero divergence does not make these tests
sufficient. Neither the unrestricted lower bound nor the upper bound
has changed. This example branch is parked pending a route that bears
on actual kernel recognition, rather than more necessary tests alone.

The completion in615 is exactly the published Kaliman--Zaidenberg
construction, up to the sign of one coordinate, not just an example
covered by their coordinate theorem. A separately checked alternative
from Lewis has shift 13 for v_3 and does not improve the upper bound.
This bounded source comparison establishes neither novelty of the
lower bounds nor optimality of either construction.

This is an obstruction to keeping a particular coordinate while
simplifying its coordinate partial. The original E is already a
translation and u is a different coordinate with zero shift. It is
NOT a counterexample to cancellation or to recognition after changing
the chosen coordinate. The proof must permit such a change or handle
the positive-shift branch. No terminating global change is supplied.

The archive audit also corrects a recent loss of proof context.
The saturation reduction in
[616](research/invariant-extension-higher-image-saturation-pass616-working.md)
is a consolidation of [pass16](research/invariant-affine-slice-pass16.md),
not a new theorem. The stronger source-dependent
[pass17 affine-replacement proof](research/general-invariant-affine-pass17.md)
already treats all invariant-coefficient extensions over C^[3], using
the [pointwise plinth argument](research/pointwise-plinth-pass17.md).
It must not be replaced by the weaker conditional reduction or labeled
unproved merely because it was absent from the recent working context.
An affine slice still does not identify its kernel with C^[3]; the
[principal-modification formulation](research/arbitrary-invariant-kernel-pass18.md)
records that separate problem. Arbitrary four-variable entry remains
the main gap.

The recognition investigation has returned to a specific unresolved
subcase of that modification problem: primitive D on R=C^[3],
Dr=p generating its plinth, rho=rad(p), p dividing rho^2, and
M=R[r/(1+rho Q)] for Q in ker(D). Its cylinder is polynomial;
abstract polynomiality of M is not proved for arbitrary D. The
proposed Dasgupta--Gaifullin-family test was already fully recognized
in [the earlier family theorem17](research/general-local-slice-lift-pass17.md)
and is not a new advance. The existing [formal-neighborhood result18](research/radical-modification-attack-pass18.md)
and [plinth-preservation result19](research/global-modification-bridge-pass19.md)
show why repeating these modifications cannot remove a singular
plinth divisor of the retained action. Coordinate conjugacy merely
transports that divisor. A singularity-descent approach needs a
genuinely different action with controlled new plinth data, or a
different recognition argument; no such general construction is supplied.

All new proofs have separate written-source checks. Novelty remains
UNKNOWN; no human expert review or Lean certification has occurred.

## Previous investigation: exact coefficient classifications for one fixed rank-three base

General cancellation remains UNSOLVED. The independently reviewed
[classification613](research/dg-degree-five-classification-and-invariant-family-pass613-working.md)
settles two coefficient families for the fixed homogeneous (2,5) base

\[
f=xz-y^2,\quad r=x^3+yf,\quad g=zf^2+2x^2yf+x^5,
\qquad H=\operatorname{Jac}(f,g,\cdot).
\]

For EVERY complex homogeneous degree-five psi, including zero,

\[
H+(1+\psi)\partial_t\text{ has a polynomial slice}
\quad\Longleftrightarrow\quad \psi\in H(R_1),
\qquad R=\mathbb C[x,y,z].
\]

All these sliced cases have explicit whole polynomial rectifications.
The [two-return reduction611](research/rank-three-dg-degree-five-joint-return-reduction-pass611-working.md)
first gives psi in Cg+H(R_1), using all 21 coefficients and exact
finite certificates. The [residual obstruction612](research/rank-three-dg-invariant-coefficient-slice-classification-pass612-working.md)
excludes every nonzero remaining multiple of g. This is a complete
classification for that degree and base, not a grid-only observation.
The separate [second-return proof610](research/rank-three-dg-second-return-noslice-pass610-working.md)
also excludes the H-degree-17 blind-spot example left open by609.

For an arbitrary invariant polynomial h(f,g), with NO degree bound,
the same note proves

\[
H+h\partial_t\text{ has a slice}
\quad\Longleftrightarrow\quad h=c+fgP(f,g),\quad
c\in\mathbb C^*,\ P\in\mathbb C[f,g].
\]

Here the actual coordinate T=(t+rP)/c gives a slice and finite-flow
rectification. Pole-time returns over both invariant axes prove
necessity. A supplied coefficient h+H(F) reduces to this case by
t-F; no general decomposition assertion is made.

The base and its five-line/two-line exceptional fibers are already
published in [Freudenburg, Section8.2](https://arxiv.org/html/1602.08786).
Priority for the exact extension classifications remains UNKNOWN.
No human expert review or Lean certification has occurred.

The essential gap is still arbitrary four-variable entry. An actual
triangularizable-base presentation of a sliced derivation would already
give an invariant ambient coordinate, so a published regular-kernel
theorem would recognize its kernel without our degree bound. Such an
entry cannot be treated as an automatic normal-form choice. Neither
classification above supplies it or resolves general cancellation.

## Previous investigation: a necessary slice-degree bound for triangularizable bases

General cancellation remains UNSOLVED. The separately reviewed
[full-coefficient argument607](research/homogeneous-extension-slice-degree-window-boundary-pass607-working.md)
and [lower-term extension608](research/linear-triangular-homogeneous-slice-degree-bound-pass608-working.md)
prove the following necessary condition. Let H be an irreducible
ordinary-homogeneous triangularizable LND on C[x,y,z], of degree d>0,
and psi be nonzero homogeneous of degree ell>d. If
E=H+(1+psi)partial_t has a polynomial slice, then

\[
\deg_H(\psi)+1\le (\ell-d)(d+2).
\]

Here N=d+2 is the maximum H-degree of a linear coordinate. The proof
retains every coefficient of the triangular base and of psi. An
overcritical coefficient would produce two formal integral endpoints
on one orbit whose connecting time has a pole, contradicting the
polynomial slice identity. The cited linear-triangularization lemma
licenses the triangularizable corollary; no assumption that every
rank-two base is triangularizable is made.

At critical equality,605 supplies a lowering base shear. This does
not give a terminating algorithm:607 also contains a fully rectified
strictly subcritical example, H=x^2 partial_y+y^2 partial_z, psi=xy,
where NO polynomial fixed-base shear lowers the displayed t-degree.
Different coordinate changes can be necessary even for this simple
irreducible base. The positive condition ell>d is essential.

These proofs do not establish the degree bound for arbitrary
nontriangularizable or rank-three homogeneous bases, or place an
arbitrary sliced four-variable derivation in the required form.
Novelty remains UNKNOWN; there is no human expert or Lean review.

## Previous investigation: whole rectification from a radical-image criterion

General cancellation remains UNSOLVED. The independently reviewed
[finite-repair proof606](research/radical-image-sliced-extension-finite-repair-pass606-working.md)
proves a broader exact repair for extensions already presented as
E=aD+(1+DP)partial_t, where D is a locally nilpotent derivation of a
polynomial ring and 0!=a belongs to its kernel. If DP is divisible by
every distinct prime factor of a, the proof constructs a whole
polynomial coordinate system in which E is a translation. P itself
need not have that divisibility. Both inverse directions are proved,
including when a is nonprime.

If a is nonconstant ordinary homogeneous and DP is zero or positive
ordinary homogeneous, that divisibility condition is equivalent to
absence of zeros, existence of a polynomial slice, and polynomial
rectification. This equivalence is ONLY for the displayed image
subclass. It does not put an arbitrary coefficient in D(R), and does
not turn general fixed-point-free actions into translations.

The positive-degree entry investigation is recorded in607--608 above.
Neither this repair nor the previously reviewed lemma below supplies arbitrary
four-variable entry or a terminating coordinate-descent algorithm.
Novelty remains UNKNOWN; there is no human expert or Lean review.

## Previous investigation: top-degree removal for every irreducible homogeneous base

General cancellation remains UNSOLVED. The reviewed
[valuation proof605](research/irreducible-homogeneous-top-removal-via-plane-valuations-pass605-working.md)
extends the highest-degree reduction beyond the specific DG examples.
Let H be any nonzero irreducible ordinary-homogeneous LND on C[x,y,z],
of ordinary derivation degree d>0. Here irreducible means that its
coordinate coefficients have no nonconstant common factor. Choose a
linear coordinate z of maximal H-degree N. For every q>=1, with
ell=d+q and k=qN-1, the exact conclusion is

\[
R_\ell\cap\ker H^{k+1}
=\mathbb C H(z^q)\ \oplus\ (R_\ell\cap\ker H^k).
\]

Thus a homogeneous psi with those degrees admits a scalar lambda
such that psi-H(lambda z^q) has strictly smaller H-degree. In the
extension E=H+(1+psi)partial_t, the actual polynomial shear
T=t-lambda z^q strictly lowers the positive E-degree of t. It does
not assert that the new frame retains its previous Euler shift.

The proof uses published kernel and plane-valuation theorems, with
their exact hypotheses listed in605. If homogeneous kernel generators
have degrees a,b, then gcd(a,b)=1, d=a+b-3 and N=ab. The induced
primitive valuation on the projective plane has muhat=N. Two distinct
irreducible curves attain this ratio, so the published uniqueness of a
supraminimal curve forces its inverse volume to be N^2. The published
Poincare formula makes every graded piece below N^2 at most
one-dimensional. The desired value dN+1 lies below that cutoff.
This is an inference from those theorems, not a new proof of them.

The separately reviewed [monomial proof601](research/homogeneous-dg-top-degree-removal-pass601-working.md)
and [full homogeneous DG proof602](research/homogeneous-dg-family-leading-degree-removal-pass602-working.md)
give direct elementary valuation reconstructions in their specified
families, retaining every allowed coefficient in602. They provide
independent checks on the geometric mechanism in605.

The irreducibility boundary is substantive. The reviewed
[sliced replica603](research/homogeneous-replica-top-removal-sliced-counterexample-pass603-working.md)
has a fully polynomially rectified kernel, exact Euler shift one, and
the same critical degree relation, but NO polynomial base shear of any
degree lowers t. Its base derivation has a nonconstant invariant factor.
A finite nilpotent correction supplies its whole rectification, including
both inverse directions; it changes the base coordinates.

The [fixed-base criterion604](research/homogeneous-extension-base-shear-top-obstruction-pass604-working.md)
explains this distinction exactly: when deg_E(t)=m>=2, a base shear
exists if and only if H^m(P)=H^(m-1)(psi), and homogeneity reduces
every possible P to its ordinary degree ell-d component. Failure of
that test does not establish a global coordinate minimum. The replica
has another actual frame with all four E-degrees one.

The missing general step is still actual entry: an arbitrary sliced
LND on C^[4], especially in an actual degree-minimizing frame, has not
been placed in the triangular form with the hypotheses above. Nor can
an invariant replica factor be divided out inside the given extension.
No terminating arbitrary recognition algorithm has been established.

Sources601--605 have complete root and separate AI saved-source reviews,
with fresh exact checks. The interpretation of Luo's question remains
unconfirmed, novelty is UNKNOWN, and there has been no human expert
review or Lean certification. The full goal remains active.

## Previous investigation: sliceness does not rescue the first-shift coefficient shortcut

The general cancellation problem remains NOT solved. The reviewed
[sliced counterexample598](research/homogeneous-sliced-first-shift-image-kernel-counterexample-pass598-working.md)
disproves a proposed bridge in the homogeneous common-kernel branch:
even with a polynomial slice and actual Euler shift one, the extension
coefficient need not belong to the image of the base derivation plus
its kernel. The quotient in this example is already recognized affine
three-space, so this is a counterexample to that bridge, not to cancellation.

For every n>=2, in R=C[x,y,z] put

\[
f=xz-y^2,\quad r=x^{2n+1}+yf^n,\quad
g=(f^{2n+1}+r^2)/x,\quad H=\operatorname{Jac}(f,g,\cdot),
\]
\[
\psi_0=-gf^{n-1}r,\qquad
\psi=\psi_0+H(z^{4n}),\qquad E=H+(1+\psi)\partial_t.
\]

Here g is polynomial, H has ordinary derivation degree4n, and psi
is homogeneous of degree8n. The actual shear T=t-z^(4n) recovers
the recognized595 extension with coefficient1+psi0. Its explicit
polynomial slice transports across that shear, as does its polynomial
kernel. This does not assume a slice merely from freeness or a degree test.

Writing N=8n+2, the actual linear frame(x+z,y+z,z,t) has E-degrees
(N,N,N,4nN). Its actual weighted Euler field D satisfies

\[
[E,D]=8nN\partial_t-4nN E,\qquad [E,[E,D]]=0.
\]

A polynomial invariant with nonzero t-derivative witnesses exact
shift one, not just the upper bound. The two homogeneous LND
components commute. Nevertheless psi is not in H(R)+ker H.
Thus no base shear t->t-Q, Q in R, can make its derivative invariant.

The nonmembership proof is uniform, not a bounded preimage search.
In R_fg=C[f,f^-1,g,g^-1,r], a putative decomposition of psi0 would
force Q=r^2/(2f)+A(f,g)r+B(f,g). Modulo the prime f, g=x^(4n+1)
and r=x^(2n+1). Higher poles cannot cancel, and the simple-pole
residue has three distinct exponent classes modulo4n+1. More generally,
for every c in C[f,g], the same proof gives the exact criterion

\[
cr\in H(R)+\ker H\quad\Longleftrightarrow\quad
f^n\mid c\quad\Longleftrightarrow\quad cr\in H(R).
\]

The separately reviewed [control597](research/homogeneous-first-shift-degree-condition-unsliced-boundary-pass597-working.md)
had already refuted the degree-condition-only shortcut. Its complete
formal-DVR orbit proof establishes that it has no polynomial slice.
Result598 supplies the missing sliced counterexample; it does not
change597 into one. Neither selected frame is claimed globally minimal.

The reviewed [gauge lemma599](research/homogeneous-extension-gauge-first-shift-promotion-pass599-working.md)
explains a broader limit of this test. If H is ordinary homogeneous
of degree d>0, a coordinate z has maximal H-degree N, psi has ordinary
degree ell>d, and deg_H(psi)<=(ell-d)N-1, a generic shear
t=T+gamma z^(ell-d) supplies an actual shift-one frame. The proof
handles tied leading coefficients and the degree-one boundary.
This changes the selected frame and recomputes its Euler field;
simultaneous conjugacy of a fixed derivation/Euler pair preserves shift.
An explicit sliced control changes shift2 to1 while increasing the
degree sum from5 to6. It is not a descent for a degree-minimizing frame.

The reviewed [direct-intertwining addendum600](research/rank-three-pole-repair-direct-rectification-and-descended-action-pass600-working.md)
also strengthens the description of the recognized595 family. Its
repaired whole map satisfies E Psi=Psi partial_t, so Psi(x),Psi(y),Psi(z)
already generate ker E. The Taylor projection used in595 is valid and
is the identity on these images. The original commuting partial_t
descends, in those actual coordinates, to -Jac(f,gtilde,.), where
gtilde is the same published family with

\[
\widetilde F(X,Z)=F(X,Z)+\frac{C(X)}{X}Z^{n-1}.
\]

Here C is the repair residue defined in the family proof below.
Since n>=2, Ftilde(X,0)=F(X,0); the published rank-three theorem
applies exactly. Thus the descended action fixes no coordinate of
the three-variable kernel, even though that kernel is polynomial.
Slicing the four-variable action does not force that additional
coordinate simplification. This conclusion also transports to598.

Sources597--600 have complete root and separate AI written reviews and
fresh exact checks. These are working mathematical results, not Lean
certification or human expert review. The homogeneous base is already
published, the gauge is elementary, and novelty is UNKNOWN. The next
general bridge must allow genuinely non-invariant coefficients and
must distinguish a selected-frame degree change from an intrinsic
recognition argument. No reduction from arbitrary cancellation candidates
to these extensions has been established. The next bounded test asks
whether only the highest H-degree part of a homogeneous coefficient
can be removed by a base shear, which is weaker than the refuted
image-plus-kernel assertion. It remains a question, not a theorem.
The full goal stays active.

## Previous investigation: a whole polynomial repair recognizes a rank-three extension family

The general cancellation problem remains NOT solved. The reviewed
[family proof595](research/rank-three-family-pole-repair-recognition-pass595-working.md)
now recognizes the following specified extensions on B=C[x,y,z,t].
For m,n>=2 and F(x,0) nonconstant, put

\[
f=xz-y^m,\quad r=xF(x,f)+yf^n,\quad
g=(f^{mn+1}+r^m)/x,\quad H=\operatorname{Jac}(f,g,\cdot),
\]
\[
E=H+(1-gf^{n-1}r)\partial_t,\quad v=ft-r^2/2,\quad
u=t+gf^{n-2}rv+\tfrac12g^2f^{2n-3}v^2.
\]

The quotient defining g is polynomial. The proof establishes local
nilpotence, Eu=1, and a genuine automorphism of the entire B taking t
to this u. Consequently ker E is C^[3]. All coefficients of F remain
arbitrary within the stated scope, including dependence on f. This is
a family theorem, not an extrapolation from numerical examples.

The key construction repairs a localized exponential. Write b=-gf^(n-2)
and L=H/f+br partial_t. Then Phi=exp(-vL) is an automorphism of B_f
with Phi(t)=u and Phi(x)=X polynomial, but Phi(y) can have a simple
f-pole. If s=xF(x,0), its residue is

\[
C(x)=\tfrac m2 s^{m+1}s'-\frac{s^{m+2}}{2x}.
\]

The second localized map
Gamma=exp(-(C(x)/(xf))(x partial_y+m y^(m-1) partial_z))
cancels that pole. Its composition Psi=Phi Gamma has every original
coordinate image polynomial. The proof computes the full induced map
modulo f, including the extra n=2 terms and an explicit quotient inverse.
Injectivity modulo f clears every denominator in the localized inverse.
Thus neither the divisor f=0 nor any other exceptional fiber is omitted.

The finite Taylor projection pi_E(h)=sum (-u)^j E^j(h)/j! then gives
actual invariant generators pi_E(Psi(x)), pi_E(Psi(y)), pi_E(Psi(z)).
The repaired coordinate images themselves are not incorrectly assumed
to be E-invariant.

The [concrete proof594](research/rank-three-sliced-extension-pole-repair-recognition-pass594-working.md)
is the member m=n=2,F=x^4. The independent
[obstruction592](research/rank-three-nonaffine-extension-and-affine-frame-boundary-pass592-working.md)
proves that this example has no slice affine in the original t, and
that its minimum actual Euler shift over positive affine-linear frames
is exactly two. The nonlinear invariant coordinates above give a
positive frame with shift zero. The obstruction is therefore to the
restricted affine methods, not to polynomial recognition. The earlier
[audit593](research/rank-three-sliced-extension-recognition-audit-pass593-working.md)
correctly found the pole of Phi alone; its unresolved endpoint is now
superseded, not its calculation.

The reviewed [priority audit596](research/rank-three-pole-repair-priority-audit-pass596-working.md)
records definite prior coverage. The base is the published
Dasgupta--Gaifullin family. The old internal pass22 already recognizes
the m=2,F=x^2 subfamily after an exact sign transport. Localized pole
cancellation and the birational, unit-Jacobian invertibility principle
have classical predecessors. No verified statement-level match for the
entire specific repair was established in the bounded source set, but
that is not evidence of absence from the literature. Novelty is UNKNOWN.

Sources592--596 have complete root and separate AI written reviews,
with fresh exact algebra checks and explicit primary-source comparisons.
These are working proofs, not proof-assistant certification, human
expert review, or a public novelty claim. All saved checkers remain frozen.

The missing general step has not changed: an arbitrary sliced polynomial
four-ring has not been reduced to this family or another recognized
nonlinear frame. Common-kernel first-shift recognition and reduction
from arbitrary higher shift remain open in the current approach.
Luo's intended field and dimension are still unconfirmed. The full
cancellation goal stays active.

## Previous investigation: the homogeneous disjunction fails; a restricted recognition theorem survives

The general cancellation problem remains NOT solved. The reviewed
[counterexample588](research/weighted-euler-first-shift-homogeneous-recognition-disjunction-pass588-working.md)
settles the previous first-shift question negatively: an actual frame
can have neither a homogeneous E-slice nor a homogeneous E-invariant
ambient coordinate, even when its Euler shift is exactly one and its
three spectral components commute. The example uses Freudenburg's known
homogeneous derivation H=Jac(f,g,.) on C[x,y,z], with

\[
f=xz-y^2,\quad r=x^3+yf,\quad
g=zf^2+2x^2yf+x^5,\quad h=Hr=-fg.
\]

On C[x,y,z,t], take E=H+(1+h)partial_t and u=t-r. The actual frame
(x+z,y+z,z,t) has E-degrees(10,10,10,1). Only weights1 and10 can
contain a homogeneous slice or coordinate; the complete coefficient
calculation excludes both tests. Finite Taylor coordinates give an
explicit polynomial kernel and a whole inverse. This is a counterexample
to the fixed-frame recognition disjunction, NOT to cancellation or to
recognition after changing the frame. No rank-three theorem is needed
for this obstruction; its required H-identities are proved directly.

The reviewed [recognition theorem589](research/torus-normalized-additive-action-recognition-audit-pass589-working.md)
gives a genuine positive branch. For a sliced E with commuting homogeneous
LND components under any actual positive coordinate weighting, a negative
component has a coordinate slice t and an explicit polynomial quotient
R=C^[3]. If two nonzero component restrictions on R have distinct kernels,
Maubach's three-variable theorem supplies an actual common coordinate f.
Every other restriction sends f to a scalar. The sum E therefore either
has a coordinate slice or kills an ambient coordinate; in the latter case
the published Bhatwadekar--Gupta--Lokhande regular-kernel theorem applies.
Both cases prove A=C^[3]. This also recognizes the zero-restriction case
and any case where all restrictions kill an actual coordinate of R.
The remaining common-kernel case is not assumed to meet that condition.

The reviewed [four-weight theorem590](research/weighted-euler-first-shift-repeated-spectrum-boundary-pass590-working.md)
extends the spectral argument: at exact first shift, at most four distinct
spectral weights always give locally nilpotent components and Lie algebra
dimension at most six. With four weights, the only possible pair-sum
collision produces a central bracket and a two-step nilpotent component
algebra. A complete actual frame of degrees(1,2,4,3) attains dimension six.
Finite closure for five or more weights, and recognition from the
noncommuting finite action alone, remain unresolved.

The reviewed [affine-slice obstruction591](research/commuting-first-shift-common-kernel-extension-pass591-working.md)
checks another tempting common-kernel reduction. For
E=x^2 partial_y+(1+xy)partial_t, the actual frame
(t,x+t,y+t,z+t) has degrees(2,2,2,2), exact first shift and two commuting
spectral components. Nevertheless no slice is affine in the selected t,
even with arbitrary polynomial coefficients from R=C[x,y,z]; its minimum
t-degree is exactly two. The whole polynomial inverse is given. This is
the actual first-shift placement of an already retained example, not a
new rank-three obstruction. Its invariant coordinate x recognizes it.

The next proof gap is recognition of the common-kernel branch without
an available base coordinate. Neither the homogeneous disjunction nor
automatic affine slicing can be used as a general bridge. General
first-shift recognition and reduction from arbitrary higher shift are
also still required. At the end of588--591 a rank-three extension was
still under investigation;592--595 above now recognize that extension
and the specified larger family, without resolving the general branch.

Sources588--591 have complete root and separate AI written reviews and
fresh exact algebra checks. The positive recognition theorem explicitly
retains its published inputs. These are working proofs, not formal
certification, human expert review, established novelty, or a solution.
Luo's intended field and dimension remain unconfirmed. The full goal
stays active, and all saved checkers remain frozen.

## Previous investigation: first-shift recognition tests and a joint counterexample

The general cancellation problem remains NOT solved. The reviewed
[homogeneous-slice test582](research/weighted-euler-homogeneous-slice-test-and-first-shift-boundaries-pass582-working.md)
gives a finite linear criterion in the actual source coordinates. A
successful test proves that A is polynomial and explicitly completes
the slice to coordinates. This is a conditional recognition theorem,
not an implemented solver or a guaranteed successful test. The reviewed
[invariant-coordinate criterion586](research/weighted-homogeneous-invariant-coordinate-recognition-pass586-working.md)
adds a different finite linear test: search for a homogeneous invariant
with a nonzero linear term. Its ambient coordinate status has an explicit
proof; recognition of A then uses the published regular-kernel theorem
of Bhatwadekar, Gupta and Lokhande. The remaining invariant generators
are not claimed to have been computed.

Exact Euler shift one does not guarantee a homogeneous slice. The actual field

\[
E=(1+a^2)\partial_x+a\partial_z,\qquad
u=x-az,\qquad b=ax-(1+a^2)z
\]

has the whole inverse x=(1+a^2)u-ab, z=au-b. In the positive frame
(x,a+x,z,c+x), all four E-degrees are one. Its actual Euler field
has shift one, but no homogeneous E-slice exists. In fact, making the
slice coefficient constant would require simultaneously lambda=1 at
a=0 and lambda=0 at a=1. The invariant ring in this example is already
C[a,b,c]; primitive division of its recovered direction gives the sliced
derivation partial_b. This disproves a proof shortcut, not cancellation.

The stronger reviewed [joint counterexample585](research/weighted-euler-first-shift-joint-recognition-test-pass585-working.md)
shows that the homogeneous-slice and primitive-N-slice fallbacks can fail together: at exact
shift one, there need be neither a homogeneous E-slice nor a slice for
the primitive recovered N. Its full actual frame has degrees(1,1,1,2).
At an N-fixed line the slice coefficient b1 vanishes, so any homogeneous
slice would have forbidden eigenweight zero. The same fixed line rules
out a slice for the already primitive N. Nevertheless this example has
the homogeneous invariant coordinate a=Y-X and succeeds under586.
The result is not an obstruction to every hybrid or iterative strategy.

The reviewed [fixed-slice chain obstruction583](research/weighted-euler-fixed-slice-replica-plateau-chain-obstruction-pass583-working.md)
strengthens the earlier one-step obstruction: another actual frame at
(degree sum, Euler shift)=(13,1) admits NO finite nonincreasing escape
using replicas of its recomputed recovered direction, with the same
supplied slice. This includes every invariant polynomial coefficient.
The proof classifies all nonincreasing moves and shows that they preserve
the direction. Other directions explicitly escape; a homogeneous slice
also recognizes this example immediately. Slice changes and temporarily
increasing complexity were not ruled out.

The reviewed [spectral boundary584](research/weighted-euler-spectral-and-lie-closure-boundaries-pass584-working.md)
proves that finite spectral decomposition of each field does not make
the full generated Lie algebra finite dimensional. Its complete actual
shift-eleven example has infinitely many independent brackets; spectral
components of the recovered LND can lose local nilpotence, preservation
of A, or commutation with E. This does not settle the more restrictive
shift-one case, and does not rule out finding useful Lie directions.

For first shift, the reviewed [spectral test587](research/weighted-euler-first-shift-spectral-closure-test-pass587-working.md)
does prove finite Lie closure when the unordered sums of distinct
spectral weights do not collide. The components then commute and are
LNDs; at most three distinct weights always meet this sufficient
condition. Actual583 has noncommuting components but a nine-dimensional
Lie closure. Neither this example nor the sufficient test decides
general finite closure at shift one. An action by a finite-dimensional
algebraic group alone has not supplied general kernel recognition.

These results identified exact failed bridges. At the end of582--587,
coverage by a homogeneous invariant coordinate or homogeneous slice at
first shift remained unproved;588 above now disproves that coverage.
Both finite tests already failed in the same higher-shift polynomial
example. A general reduction or a different recognition argument is
still needed. Sources582--587 have complete root and separate AI
written reviews and fresh exact algebra checks. This is not formal certification, human
expert review, established novelty, or a solution. Luo's intended field
and dimension remain unconfirmed. The full goal stays active and all
saved checkers remain frozen.

## Previous investigation: replica obstruction and an exact two-step escape

The general cancellation problem remains NOT solved. The proposed rule
"use the recovered derivation to strictly lower the degree sum or Euler
shift in one step" is now disproved, including for a primitive nonsliced
recovered derivation and arbitrary invariant polynomial coefficients.
This is an obstruction to that reduction rule, not to cancellation.

The reviewed [replica bound579](research/weighted-euler-replica-degree-bound-and-finite-descent-test-pass579-working.md)
proves a finite bound on the slice degree of any nonincreasing replica
exp(f(u)N). If I is the set of coordinates changed by N, coordinatewise
nonincrease requires deg_u(f)<=min_{i in I} d_i; nonincrease of the
degree sum requires deg_u(f)<=max_{i in I} d_i. Both statements allow
coefficients in ker_A N. For scalar coefficients there is an exact finite
constructible existence criterion, using actual Taylor generators and
the correctly recomputed Euler weights for each new degree profile.
This is not an implemented solver or a proof that a successful move
exists. Effective implementation also requires an exact effective
coefficient field. Arbitrary invariant coefficients are not reduced to
a finite-dimensional complex parameter space by this bound.

The reviewed [scalar control580](research/scalar-slice-replica-euler-descent-obstruction-pass580-working.md)
first separates scalar and invariant coefficients: all scalar replicas
of its recovered direction, even after primitive normalization, fail
to improve (degree sum, Euler shift)=(25,10). An explicit
invariant-coefficient replica nevertheless lowers the sum to 22.

The stronger reviewed [full replica control581](research/weighted-euler-invariant-replica-descent-obstruction-pass581-working.md)
uses the actual frame

\[
(u,\ a+u^2,\ b+au+u^4,\ c+(b+1/5)u+au^2/2+u^6).
\]

Its degree tuple is (1,2,4,6), Euler shift is 1, and its recovered
derivation is N=a partial_b+(b+1) partial_c. This N is primitive
and nonsliced. No exp(FN), for ANY F in (ker_A N)[u], lowers
(13,1): a full degree calculation prevents degree-sum decrease,
and an exact first-order commutator obstruction prevents shift zero.
The proof covers all invariant coefficients, not only a search grid.

The same control explicitly permits a two-step escape. Applying
exp(-uN) leaves (13,1) unchanged but changes the recovered direction
to N1=-4 partial_c. The next replica exp((-u/5)N1) reaches shift zero:

\[
(13,1)\longrightarrow(13,1)\longrightarrow(13,0).
\]

Thus the result rules out guaranteed STRICT ONE-STEP descent, not
recovery after a plateau move or arbitrary coordinate changes. The
example has a known polynomial kernel and is explicitly nonminimal.
No finite-escape theorem for plateau moves, well-founded secondary
measure, or general coordinate reduction has been established.
Testing that finite-escape route is a next research question, not an
equivalent reformulation already proved here.

Sources579--581 have complete root and separate AI written reviews,
with fresh exact algebra checks. No novelty, human expert review,
formal verification, or solution of cancellation is claimed. The
earlier conditional cubic result and Euler dichotomy are retained
below with their existing limits. Luo's intended field and dimension
remain unconfirmed; the full goal stays active, and all saved checkers
remain frozen.

## Previous investigation: a general Euler dichotomy and the conditional cubic sector

The general cancellation problem remains NOT solved. There are two
reviewed advances, with different scopes.

The [weighted Euler dichotomy576](research/weighted-euler-positive-shift-and-homogeneous-initial-rank-pass576-working.md)
applies to any actual sliced polynomial n-ring B=A[u], n>=2, in a
positive-degree coordinate frame. Such a frame is always available by
an invertible linear shear, without assuming entry into the special
paraboloid chart. For the weighted Euler derivation
D=sum d_i X_i partial_Xi, its exact E-degree shift delta is finite
and nonnegative:

- If delta=0, A inherits a connected positive grading. Smoothness at
  its homogeneous vertex proves A is a polynomial (n-1)-ring, and
  its generators together with the given slice are actual coordinates.
- If delta>0, the induced derivation is eta^delta N for a nonzero
  locally nilpotent derivation N on A. The initials of EVERY polynomial
  homogeneous in the original source weights lie in (ker N)[eta].
  Their entire initial field has transcendence degree at most n-1.

Thus a hypothetical nonpolynomial factor must satisfy the second
alternative in every positive frame. This removes the generator-count
restriction from the homogeneous-initial rank bound in that case.
It does not supply a coordinate reduction or a terminating procedure.
Explicit polynomial controls attain the bound and show why changing
presentation weights is not the same as preserving Euler homogeneity.
The induced N can have a fixed divisor and no slice; in that example
a separate primitive division does recover a sliced derivation.
The standard grading and locally finite derivation ingredients are
not claimed as novel.

The reviewed [commutator recovery577](research/weighted-euler-commutator-recovery-and-zero-shift-test-pass577-working.md)
makes this split directly testable from the actual polynomial fields.
For these particular Euler weights, delta=0 is equivalent to
[E,D]=E. Otherwise the final nonzero iterated commutator recovers
the induced LND, with an explicit correction to kill the supplied
slice. No generators of A are needed for this calculation.
Zero shift also forces every coordinate leader to be complex;
initial rank one by itself does not imply zero shift.

The reviewed [primitive nonsliced control578](research/weighted-euler-primitive-nonsliced-actual-control-pass578-working.md)
rules out another shortcut. An explicit invertible translation frame
induces N=a partial_b+b partial_c. Its components have greatest
common divisor one, but all images lie in the proper ideal (a,b),
so even this primitive N has no slice. More generally, any supplied
nonzero LND homogeneous for positive weights on a KNOWN polynomial
ring can be realized as an Euler-induced derivation in such a frame.
This does not give a positive grading or polynomial generators for
an unknown invariant ring. All these controls are nonminimal.

Inside the FULL actual264/296/535 chart, the separately reviewed
[nonzero-h exclusion574](research/principal-paraboloid-cubic-lower-degree-nonzero-h-exclusion-pass574-working.md)
and [zero-h exclusion575](research/principal-paraboloid-cubic-lower-degree-zero-h-exclusion-pass575-working.md)
exclude all noncomplex-coupling cases with intrinsic degrees
sigma=2, theta=3 and y<=3, including zero y. Combined with553's
degree bound and the previously reviewed complete cubic-excess
exclusion, this proves the scoped conclusion

\[
\deg\sigma=2,\quad\deg\theta=3\quad\Longrightarrow\quad m\in\mathbf C.
\]

The retained [constant-coupling recognition473](research/principal-paraboloid-complete-constant-coupling-recognition-pass473-working.md)
then recognizes A as C^[3], conditional on its explicitly retained
historical recognition dependencies. Those ancestors were not
recursively recertified by this composition. No arbitrary candidate
has been shown to enter this chart.

Sources574--578 have complete root and separate AI written-source
reviews, with fresh exact algebra checks. This is not human expert
review, proof-assistant certification, established novelty, or a
solution of general cancellation. The central next task remains a
justified coordinate reduction or recognition in the positive-shift
case. The primitive-normalization shortcut is now ruled out by578.
Actual automorphisms generated by the recovered commuting LND
remain a possible direction, but no general decreasing invariant
or termination theorem is established.
Other intrinsic profiles and arbitrary coordinate entry remain open.
Luo's intended field and dimension remain unconfirmed. The full goal
stays active; all saved checkers remain frozen.

## Previous investigation: an exception-free conditional degree bound

The general cancellation problem remains NOT solved. Under EVERY
actual264/296/535 hypothesis, with noncomplex m and quadratic intrinsic
sigma, the reviewed results now give

\[
\deg\theta\ge3\quad\Longrightarrow\quad\deg y\le\deg\theta.
\]

The zero polynomial y is included. This removes both exceptions from553's
earlier uniform bound; it is not an arbitrary-chart-entry or recognition
theorem.

The reviewed
[last cubic-excess exclusion571](research/principal-paraboloid-nontransverse-cubic-noncomplex-ratio-exclusion-pass571-working.md)
uses the entire initial kernel, a finite positive-weight presentation
argument and genuine coefficient derivatives to obtain a nonzero
polynomial contradiction. Combined with555,558,568 and570, it excludes
the complete intrinsic profile (2,3,4), without extra conic or pair-unit
restrictions.

The independently reviewed
[quartic-excess exclusion572](research/principal-paraboloid-quartic-excess-parity-exclusion-pass572-working.md)
excludes (2,4,6). Actual initial-relation degree bounds force its leading
cancellations. Full lower equations then force y, sigma and theta to
be even in the intrinsic parameter, contradicting their required
polynomial generation of the whole line. Every zero lower-coefficient
case and the exceptional denominator boundary are retained.

Sources571 and572 have complete root and separate AI saved-source
reviews, with whole-polynomial exact checks. This is neither human
expert review nor proof-assistant certification or established novelty.
Lower-y cubic and quartic cases remain under investigation, and
arbitrary coordinate entry remains the central general gap. The reviewed
[general presentation lemma573](research/full-initial-presentation-rank-obstruction-and-boundaries-pass573-working.md)
extends one argument to full multi-relation initial ideals, but its
dimension bound does not improve the current rank-one (4,5,6,7)
frontier. Explicit actual examples show why selected relations and
degree-zero remainders cannot be treated as the positive full-generator
case. It does not supply coordinate descent. Luo's intended field and
dimension remain unconfirmed. The full goal is active, and all saved
checkers stay frozen.

## Previous investigation: conditional cubic-branch exclusions and the coordinate boundary

The general cancellation problem remains NOT solved. Under EVERY
actual264/296/535 hypothesis and the cubic-excess family554, the reviewed
[transverse branch exclusion568](research/principal-paraboloid-transverse-cubic-branch-exclusion-pass568-working.md)
rules out the noncomplex-ratio part of the entire h nonzero, v1=0
family. Together with558 this excludes that full transverse family.
The proof uses full polynomial equations and genuine derivative
compatibility, not an extra quartic-coefficient restriction. In
particular the candidate conic families studied in563/564/567 do not
survive these additional equations.

The reviewed
[complex-ratio exclusion570](research/principal-paraboloid-nontransverse-cubic-complex-ratio-exclusion-pass570-working.md)
also excludes the h nonzero, v1 nonzero branch when T0 is complex.
Its full initial-kernel argument forces a linear source-weight growth
bound on the invariant algebra, contradicting its two algebraically
independent polynomial invariants. The formerly pending noncomplex-ratio
part is now excluded by the reviewed571, as recorded above.

Away from this special chart, the reviewed
[coordinate-descent criterion569](research/rank-one-cancellation-remainder-coordinate-obstruction-pass569-working.md)
identifies the exact elementary descent condition using the entire
associated graded algebra of the other three coordinates. An explicit
polynomial example shows that a degree-lowered relation remainder need
not be a coordinate. That example nevertheless has an explicit descent
in another coordinate; it is not a minimal frame or a counterexample.

Sources568--570 have complete root and separate AI saved-source reviews,
with fresh exact algebra checks. These are conditional working proofs,
not human expert review, proof-assistant certification or established
novelty. Other intrinsic profiles and arbitrary coordinate entry remain
unresolved. Luo's intended field and dimension remain unconfirmed.
The full goal stays active, and all saved checkers remain frozen.

## Previous investigation: actual controls, conditional normalization and a unit exclusion

Historical status below is retained. The previously surviving conic
families in this section are now excluded under the full original
inputs by568, as stated above.

The general cancellation problem remains NOT solved. The reviewed
[actual translation family565](research/rank-one-semigroup-minimal-actual-translation-controls-pass565-working.md)
realizes every degree tuple (n,n+1,n+2,n+3), n>=4, despite the absence
of a single-monomial degree reduction. A two-monomial polynomial shear
recovers the slice. These are explicit nonminimal polynomial examples,
not cancellation counterexamples or a classification of minimal frames.

The reviewed
[maximal-cofactor restriction566](research/rank-one-maximal-cofactor-leading-line-boundary-pass566-working.md)
shows that, at initial rank one and total degree S>4, the leading
fields of the partials attaining their cofactor upper bounds lie on
one common line. There cannot be exactly one attaining partial.
Actual examples show why this does not include nonattaining fields
or the S=4 boundary. It supplies no general coordinate reduction.

Inside the full conditional transverse chart, the reviewed
[actual normalization564](research/principal-paraboloid-degenerate-quartic-actual-conic-normalization-pass564-working.md)
puts the two conic-field possibilities into simpler forms using an
invertible complex polynomial shear, preserving all original equations
and both pair branches. The reviewed
[boundary restriction567](research/principal-paraboloid-degenerate-quartic-pair-boundary-exponent-restriction-pass567-working.md)
excludes the unit numerator lambda*D^2 when delta is nonzero and
restricts one parameter value for lambda*u^2*D. The surviving forms
are neither constructed nor excluded by these necessary conditions.

Sources564--567 have complete root and separate AI source reviews,
supported by fresh exact symbolic checks. These checks are not human
expert review, proof-assistant certification or a novelty assessment.
Arbitrary coordinate entry remains the central unresolved gap.
Luo's intended field and dimension remain unconfirmed. The goal is
active; all saved checkers remain frozen.

## Previous investigation: sharper general bounds and the minimal-frame boundary

The general cancellation problem remains NOT solved. The reviewed
[full-kernel derivative-order argument560](research/arbitrary-initial-kernel-derivative-order-bound-pass560-working.md)
works without assuming a principal initial relation. The reviewed
[rank-sensitive refinement562](research/rank-sensitive-cofactors-and-rank-one-semigroup-boundary-pass562-working.md)
sharpens the actual cofactor bounds and proves that an initial-rank-one
frame admits a genuine lowering coordinate shear whenever one degree
belongs to the semigroup generated by the other three. A globally
minimal positive frame of initial rank one cannot have that redundancy.

These tests do not force a reduction. The formal degree tuple (4,5,6,7)
passes the stated numerical inequalities, including every derivative
order in an explicit three-variable top algebra. This is an abstract
compatibility control, not an actual frame or a cancellation counterexample.

The reviewed
[saturated-family control561](research/saturated-commuting-leading-family-fiber-obstruction-pass561-working.md)
also rules out a proposed shortcut: even all four leading coordinate
partials can generate a saturated commuting family that loses rank on
a perfectly polynomial fiber. Its explicit example is already a
translation and is not a minimal frame. The literal question in an
older preprint is answered negatively, but related published examples
exist and no historical novelty is claimed.

The reviewed
[conditional conic-field restriction563](research/principal-paraboloid-degenerate-quartic-conic-field-restriction-pass563-working.md)
reduces the U4=0 part of the full transverse chart
to two explicit possible conic forms, retaining both delta branches.
It does not exclude or realize either form, or address arbitrary entry.

Sources560--563 have complete root and separate AI source reviews,
with fresh exact algebraic checks.
These are working mathematical arguments, not human expert review,
formal certification, established novelty or a solution to cancellation.
The full goal remains active; all saved checkers remain frozen.

## Previous investigation: the transverse cubic branch is more constrained

The general cancellation conjecture remains NOT solved. Under EVERY
actual264/296/535 hypothesis and the v1=0 cubic-excess family554,
the reviewed
[degree-profile restriction556](research/principal-paraboloid-cubic-transverse-degree-profile-restriction-pass556-working.md)
proves that noncomplex T0=2t+1/r forces the actual intrinsic
degree profile (4,4,4): w5=0 and w4 is nonzero. The proof uses
the actual coordinate partials and the entire initial kernel,
not a sampled leading model. It does not yet exclude that profile.

The reviewed
[conic and differential restriction557](research/principal-paraboloid-cubic-transverse-conic-and-differential-restriction-pass557-working.md)
then forces the full initial relation among the three leaders to
be an irreducible complex quadratic, and gives exact differential
restrictions. An explicit formal control satisfies its high-degree
gates but fails a lower equation, so those gates do not establish
an actual example or solve the remaining case.

The reviewed
[complex-ratio exclusion558](research/principal-paraboloid-cubic-transverse-complex-ratio-exclusion-pass558-working.md)
rules out every complex value of T0, including zero, in this
transverse family. Its proof uses an actual complex coordinate
change and excludes all three resulting degree profiles. Thus the
noncomplex conic case is the remaining case in this family.

The reviewed
[quartic pair-unit restriction559](research/principal-paraboloid-cubic-transverse-quartic-pair-unit-restriction-pass559-working.md)
further splits that remaining case. A nonzero fourth coefficient
forces two precise choices of a lower coefficient; a zero fourth
coefficient forces h^11=c1*t+c0. The degenerate pair component is
retained and its unit is determined more sharply. Neither branch
is excluded or realized by these necessary conditions.

The bounded literature refresh found no applicable theorem supplying
arbitrary coordinate entry; its exact hypothesis mismatches are in
the ledger. This does not establish absence from the literature.

Sources556--559 have complete root and separate AI source reviews and
fresh exact coefficient checks. These remain conditional working
arguments, not human expert review, formal certification or an
established novelty claim. The full goal stays active and all saved
checkers remain frozen.

## Previous investigation: the equal-quadratic sector is conditionally recognized

The general cancellation conjecture remains NOT solved. Under EVERY
actual264 hypothesis, the new
[complete equal-quadratic synthesis552](research/principal-paraboloid-equal-quadratic-recognition-synthesis-pass552-working.md)
proves that deg(sigma)=deg(theta)=2 forces m=k_s to be complex.
The retained473 endpoint then recognizes the original kernel as
C^[3], conditional on its stated historical dependencies. This
does not produce the required actual chart from arbitrary input.

The final
[variable-ratio exclusion551](research/principal-paraboloid-equal-quadratic-variable-fiber-ratio-exclusion-pass551-working.md)
closes the last positive-Laurent branch. After licensed complex
normalizations, its entire scalar has an Xx coefficient equal to
2/B times its nonzero X=0 value, contradicting independence from
X and the intrinsic variable. The proof retains the original
2tB+md term, both actual returns, every lower coefficient and all
zero cases. The synthesis reapplies the whole return after each
normalization rather than assuming branch labels survive it.

For quadratic sigma and theta degree n>=3, the new
[uniform degree bound553](research/principal-paraboloid-quadratic-sigma-higher-theta-degree-bound-pass553-working.md)
gives deg(y)<=n except possibly (n,deg(y))=(3,4) or (4,6).
The
[cubic leading-family reduction554](research/principal-paraboloid-cubic-excess-leading-families-pass554-working.md)
keeps three necessary families. Its m_s=0 branch forces
m^5=c1*t+c0 with nonzero complex c1. The subsequent
[full divided-pair argument555](research/principal-paraboloid-cubic-pair-unit-and-longitudinal-exclusion-pass555-working.md)
now excludes that m_s=0 excess branch. It retains both the ordinary
pair curve and its degenerate vertical component. The two m_s
nonzero excess families, lower-degree y and other profiles remain
open; necessary leading formulas are not actual realizations.

Sources551--555 passed complete root and separate AI source reviews,
with fresh exact algebraic checks. This is not human expert review,
formal certification or established novelty. Historical recognition
ancestry is retained, not recursively recertified. Other nonlinear
profiles and arbitrary chart entry remain open. The full goal stays
active, and every saved checker remains frozen.

## Previous investigation: the entire affine-or-constant-theta sector is conditionally recognized

The general cancellation conjecture remains NOT solved. Under EVERY
actual264 hypothesis, the new
[complete affine-theta synthesis544](research/principal-paraboloid-complete-affine-theta-recognition-pass544-working.md)
recognizes A=C^[3] whenever deg(theta)<=1, including zero or constant
theta and every degree of sigma. The stated historical recognition
dependencies of473 and478 remain required. This is not an arbitrary
chart-entry theorem.

The new [uniform higher-sigma argument543](research/principal-paraboloid-higher-sigma-affine-theta-exclusion-pass543-working.md)
handles all sigma degrees at least three when theta has degree one.
It uses full polynomial identities and an exact degree-(3,5)
generation obstruction, not finite-degree sampling. With nonconstant
sigma these results force m=k_s to be complex. Constant sigma is
different: the retained478 endpoint recognizes a possible variable
coupling and must not be strengthened to a constant-m assertion.

For the genuinely quadratic/quadratic sector, the new
[necessary characteristic equation545](research/principal-paraboloid-equal-quadratic-nonzero-characteristic-exclusion-pass545-working.md)
proves m_t+mu*m_s=0, where mu is the ratio of the two quadratic
leaders. It does not recognize the remaining branch. The proof
uses an actual complex coordinate shear, a full initial-relation
degree bound and a rational-function divisibility contradiction.

Inside that remaining branch, [546](research/principal-paraboloid-equal-quadratic-zero-characteristic-constant-intercept-exclusion-pass546-working.md)
excludes a complex quadratic y coefficient. The necessary
[reflection-rigidity result547](research/principal-paraboloid-equal-quadratic-zero-characteristic-reflection-rigidity-pass547-working.md)
then forces that coefficient to have the form a=alpha/m+beta, and
the related coefficient chi=2alpha/m^2+delta, with alpha a nonzero
complex constant and beta,delta complex. This restricts the remaining
family; it does not exclude or recognize it.

After licensed complex normalization, [548](research/principal-paraboloid-equal-quadratic-constant-laurent-exclusion-pass548-working.md)
excludes the constant Laurent alternative and
[549](research/principal-paraboloid-equal-quadratic-inverse-laurent-exclusion-pass549-working.md)
excludes the inverse alternative. The positive-Laurent alternative,
with nonzero linear y coefficient, remains open.

Within that last alternative, [550](research/principal-paraboloid-equal-quadratic-stationary-linear-fiber-exclusion-pass550-working.md)
excludes a constant fiber-coefficient ratio using the full X-dependent
scalar. The variable-ratio case has a new candidate contradiction,
but its complete written source and independent source review are
still pending.

Sources543--550 passed complete root and separate AI source reviews,
with fresh exact algebraic checks. These are conditional working
proofs, not external expert review, formal certification or established
novelty. Their full historical ancestry has not been recursively
recertified. Other nonlinear profiles and arbitrary actual chart
entry remain open. The full goal stays active; saved checkers remain
frozen.

## Previous investigation: the quadratic-sigma, affine-theta case is conditionally recognized

The general cancellation conjecture remains NOT solved. Under EVERY
actual264 hypothesis, the new
[scoped synthesis542](research/principal-paraboloid-quadratic-affine-recognition-synthesis-pass542-working.md)
proves that intrinsic degrees (deg sigma,deg theta)=(2,1) force
m=k_s to be complex. The retained constant-coupling endpoint473
then recognizes A=C^[3], subject to its stated historical dependencies.
This is a complete case split inside the supplied chart, not a
reduction from arbitrary cancellation data.

The new [actual normalization539](research/principal-paraboloid-quadratic-affine-transverse-normal-form-pass539-working.md)
preserves the original slice, selected partial, entire initial kernel,
both field/ring returns and scalar. Its two possible branches are
excluded by [540](research/principal-paraboloid-quadratic-affine-constant-midpoint-exclusion-pass540-working.md)
and [541](research/principal-paraboloid-quadratic-affine-zero-midpoint-exclusion-pass541-working.md).
Both final contradictions use the complete scalar in the ORIGINAL
field. No square root from a finite coefficient extension is assumed
to descend. Vanishing lower coefficients and integration constants
are included.

Sources539--542 passed complete root and separate AI source reviews,
supported by fresh exact algebra. These are conditional working proofs,
not human expert review, formal certification or established novelty.
Their entire historical ancestry has not been recursively recertified.
Other nonlinear degree profiles and arbitrary actual chart entry remain
open. The full goal is active; all saved checkers remain frozen.

## Previous investigation: a nonlinear degree profile forces m_t=0

The general cancellation conjecture remains NOT solved. Under EVERY
actual264 hypothesis, nonzero m=k_s and intrinsic degrees
(deg sigma,deg theta)=(2,1), the new
[conditional restriction537](research/principal-paraboloid-quadratic-sigma-affine-theta-longitudinal-exclusion-pass537-working.md)
proves deg y<=2 and m_t=0. If m is noncomplex, the normalized
quadratic intercept has no linear term and k_tt is complex.
The remaining dependence on s is not excluded or recognized.

The proof combines the denominator-free identities with the all-X
return, then uses an actual coordinate partial to contradict the
only two possible leading relations in the m_t-nonzero branch.
It retains the finite coefficient extension and its changed intrinsic
speed. Complete root and separate AI source reviews agree, supported
by fresh exact algebra. This is not human expert or formal certification.

The separate
[finite-converse note538](research/principal-paraboloid-finite-midpoint-saturation-converse-pass538-working.md)
turns the earlier midpoint obstruction into an equivalent generation
test when the first-potential polynomial is nonconstant. Its explicit
constant-polynomial counterexample passes every fixed-parameter
embedding test but fails whole-family generation. Neither this test
nor the new degree-profile result supplies arbitrary chart entry.
The full goal remains active and all saved checkers remain frozen.

## Previous investigation: nonlinear critical points retained, general entry still open

The general cancellation conjecture remains NOT solved. The new
[denominator-free lemma535](research/principal-paraboloid-nonlinear-sigma-unit-multiplier-pass535-working.md)
extends the multiplier identities to arbitrary nonconstant sigma
under the FULL actual264/296 hypotheses with m nonzero. The proof
retains every critical point of sigma, even where both selected
gradient components vanish. Root and separate AI source reviews,
with exact generic-jet algebra, agree. This is a necessary identity,
not an exclusion of the nonlinear cases or a general entry theorem.

The independently reviewed
[entry-boundary note536](research/sliced-fourspace-actual-coordinate-entry-boundary-pass536-working.md)
explains why finding an invariant actual coordinate or a unit-speed
coordinate would already recognize the kernel. An actual positive
diagonal homogeneous frame suffices, but the intrinsic slice grading
does not supply one. The bounded literature check did not establish
an unconditional entry route. A proposed additional quadratic
critical-point restriction was found to be an algebraic restatement
of the existing cross-product identity, not a new proof advance.

The affine-sigma synthesis below remains conditional, with its
historical dependencies explicit. Nonlinear exclusion and arbitrary
chart entry remain open. None of these AI audits is external expert
review, proof-assistant certification or evidence of novelty.
All saved checkers remain frozen.

## Previous investigation: the entire supplied affine-sigma sector is recognized conditionally

The general cancellation conjecture remains NOT solved. The new
[scoped synthesis534](research/principal-paraboloid-complete-affine-sigma-recognition-pass534-working.md)
retains EVERY actual264 hypothesis and proves the working implication

    deg_v(sigma)=1  =>  m=k_s belongs to C.

The retained constant-coupling endpoint473 then gives A=C^[3],
subject to its explicitly retained historical recognition dependencies.
There is no additional restriction on theta degree, y degree,
either derivative of m, or the original Z/W leading coefficients.
This closes the entire affine-nonconstant-sigma sector of this
specified chart, not all cancellation candidates.

The new [cubic exclusion530](research/principal-paraboloid-transverse-cubic-exclusion-pass530-working.md)
and [quartic exclusion531](research/principal-paraboloid-transverse-quartic-exclusion-pass531-working.md)
close the transverse higher-degree cases left by528. The quartic
argument handles the resultant's false finite-root possibility
explicitly; its complete scalar and minor equations finish the
proof. The independent [quartic tie lemma532](research/principal-paraboloid-transverse-quartic-leading-tie-obstruction-pass532-working.md)
checks the unequal-degree and zero-Z-leading boundaries.

A separate [actual-ring argument533](research/principal-paraboloid-affine-line-initial-growth-exclusion-pass533-working.md)
closes the remaining affine intrinsic line. An actual coordinate
partial and growth of the invariant ring force a weight-two
initial relation; two regular complex-X values contradict both
varying slopes. Together with retained479/483, this excludes
every variable-coupling line with nonconstant sigma, including
the necessary coefficient families left by489. Their necessary identities remain valid;
they were never established as actual chart realizations.

Sources530--534 have complete separate saved-source AI reviews.
Fresh exact algebra reconstructs the relevant full identities,
and the composition audit covers all degree and zero cases.
These are working conditional proofs, not human expert review,
formal certification, established novelty or publication readiness.
The entire historical dependency chain has not been recursively
recertified by the new audits.

Nonlinear sigma, other original initial kernels/time profiles,
and arbitrary actual chart entry remain genuine obligations.
The next bounded investigations address nonlinear-sigma critical
points and the exact actual-coordinate entry gap. No coefficient
parameter or global slice is presumed to be an ambient coordinate.
The intended field and dimension of Luo's email remain unconfirmed.
The full goal stays active, and all saved checkers remain frozen.

## Previous investigation: higher-degree recognition and the cubic/quartic frontier

The general cancellation conjecture remains NOT solved. The new
conditional result retains the FULL actual264 chart, its genuine
levels and universal multiplier, and affine nonconstant sigma:

    m_s=0 and deg_P(theta)>=3  =>  m=k_s belongs to C.

The retained constant-coupling recognition473 then gives A=C^[3],
subject to its stated historical dependencies. This is recognition
inside the supplied chart, not a reduction of arbitrary cancellation
data to that chart.

The case split is explicit. If m=0, use473's separate zero-coupling
branch. Otherwise521 gives deg_P(y)<=deg_P(theta). The new
[equal-degree exclusion526](research/principal-paraboloid-equal-higher-degree-univariate-coupling-exclusion-pass526-working.md)
rules out equality, including both values of the leading W
coefficient. The new
[unequal-degree exclusion527](research/principal-paraboloid-unequal-higher-degree-univariate-coupling-exclusion-pass527-working.md)
rules out strict inequality when m_t is nonzero. Thus m_t=0;
together with m_s=0 and the exact joint constant field, this gives
m in C. No rationality of the coefficient field is assumed.

The equal-degree proof first reduces to cubic and quartic cases.
Full polynomial-ring generation, tested after a coefficient-field
specialization, excludes all but one exceptional cubic. That
cubic supplies an actual three-coordinate frame of intrinsic
degrees (1,2,3). A cofactor and invariant-growth argument forces
an initial relation incompatible with its exact differential
equation. The unequal-degree proof uses a separate complete
odd-part calculation, not an extension of the equal-degree
theorem outside its hypotheses.

Held522--529 have complete separate saved-source AI reviews and
fresh exact algebraic checks recorded in the ledger. These are
conditional working results, not human expert review, formal
proof-assistant certification or established novelty. Historical
recognition dependencies have not been recursively recertified.

Separately, the
[boundary-primality note525](research/affine-slice-coordinate-boundary-primality-obstruction-pass525-working.md)
gives a necessary condition for a proposed actual coordinate
in ker(E^2). Its explicit smooth, integral-fiber counterexample
shows that generic polynomial completion and nonsingularity
alone do not provide an actual coordinate. It does not refute
existence of a different suitable coordinate or cancellation.
The example's overlap with earlier work is expressly credited.

For m_s nonzero, the independently reviewed
[transverse bound528](research/principal-paraboloid-transverse-coupling-higher-degree-bound-pass528-working.md)
now proves that higher theta degree is either three or four.
The full moving-coefficient equations are essential; the quartic
degree tie is explicitly retained. The separate
[low-intercept cubic exclusion529](research/principal-paraboloid-transverse-cubic-low-intercept-exclusion-pass529-working.md)
rules out cubic theta when deg y<=1, including y=0, by a
self-contained degree-(3,5) divided-difference resultant.

Thus the still-unrecognized HIGHER-degree sector within this
affine-sigma chart has m_s nonzero and theta degree three or four.
A further exact outline appears to exclude the entire transverse
cubic sector, including equal-degree y; it is being written and
is not yet an accepted saved proof. Quartic scalar compatibility
and the finite-root exceptions in its resultant are the next
bounded investigations. Nonlinear sigma, other original initial
kernels/time profiles and arbitrary actual chart entry remain
separate obligations. The intended field and dimension of Luo's
email remain unconfirmed. The full objective stays active, and
all saved checkers remain frozen.

## Previous investigation: the supplied quadratic-graph sector includes its degree drop

The general cancellation conjecture remains NOT solved. The new
[scoped synthesis520](research/principal-paraboloid-complete-affine-sigma-quadratic-graph-recognition-pass520-working.md)
retains EVERY actual264 hypothesis and proves the working implication

    deg_v(sigma)=1, theta=a*sigma^2+b*sigma+c, a nonzero
        => k_s belongs to C.

The retained constant-coupling endpoint473 then recognizes A as C^[3],
subject to its explicitly retained historical dependencies. This now
includes the boundary 1+k_s*a=0, not just510's nondegenerate case.
It does not recognize every projected conic or establish arbitrary
entry into this supplied, oriented chart.

The new degree-drop proof has two complementary parts. After the
earlier511--515 reductions, the
[actual initial-relation argument519](research/principal-paraboloid-degree-drop-cubic-row-initial-exclusion-pass519-working.md)
excludes the entire nonzero cubic W branch. Its exact degree bound
is independent of the two conditional ODE families in517. The
[curvature reduction516](research/principal-paraboloid-degree-drop-moving-curvature-exclusion-pass516-working.md)
and [complete scalar exclusion518](research/principal-paraboloid-degree-drop-zero-cubic-row-exclusion-pass518-working.md)
exclude the zero cubic W branch, retaining both transverse-slope
possibilities and both values of the normalized complex offset.

The saved proofs and synthesis have separate complete AI source
reviews and fresh exact reconstructions recorded in the ledger.
The synthesis's literal-intercept notation was clarified during
review, without replacing the strong C-field return by an unproved
moving-coordinate version. These are conditional working results,
not human expert review, proof-assistant certification or established
novelty. Historical recognition ancestors are not newly recertified.

Beyond the quadratic case, the new
[higher-degree bound521](research/principal-paraboloid-higher-slope-intercept-degree-bound-pass521-working.md)
proves deg_P(y)<=deg_P(theta) whenever theta has degree at least
three, with affine sigma and nonzero coupling. Its uniform proof
retains all lower coefficients and the cubic-theta boundary. It is
a necessary restriction, not recognition of those higher-degree
cases. This saved proof also has a complete independent source audit.

Affine sigma with theta of degree at least three, nonlinear sigma,
other initial kernels and time profiles, and arbitrary chart entry
remain separate obligations. In particular the bounded actual map
family426 preserves positive intrinsic sigma degree and cannot make
a nonlinear sigma affine. The full goal remains active, and the
professor's intended field and dimension remain unconfirmed.
All saved checkers remain frozen.

## Previous investigation: two degree-drop branches are excluded

This subsection records the earlier frontier, superseded in the
quadratic-graph sector by the synthesis above.

The general cancellation conjecture is still NOT solved. All new
results retain the FULL actual264/296 chart and universal494, with
affine nonconstant sigma=P and theta=−P^2/m+bP+c, m=k_s nonzero.
They do not assume the quadratic-level parity theorem327, whose
nonzero-degree hypothesis fails here.

The [transverse-coupling exclusion511](research/principal-paraboloid-degree-drop-transverse-coupling-exclusion-pass511-working.md)
forces m_s=0. In the remaining noncomplex-m sector, the
[necessary system512](research/principal-paraboloid-degree-drop-univariate-coupling-reduction-pass512-working.md)
gives y=eP^2+lP+r with e_s=0, two exact differential equations,
and nonzero epsilon=k_t+mb and F2=2e−3m_t/m.

The new [zero-quadratic exclusion515](research/principal-paraboloid-degree-drop-zero-quadratic-exclusion-pass515-working.md)
rules out e=0. Its [actual entry513](research/principal-paraboloid-degree-drop-affine-intercept-reciprocal-rigidity-pass513-working.md)
first forces reciprocal affine coupling and a complex linear
coefficient, then gives a verified complex polynomial normalization.
A published field two-quasi theorem supplies a generic invariant.
The complete coefficient equations require both D=0 and D nonzero:
the final exact contradiction is 0=12D^2, while the D=0 case
separately violates an actual coordinate fiber. No generic invariant
is promoted to an original-ring coordinate.

Thus the remaining variable-coupling degree-drop cases have e nonzero.
If the literal W cubic coefficient also vanishes,512 forces affine
coupling, and the [direct moving-frame entry514](research/principal-paraboloid-degree-drop-quadratic-row-moving-frame-pass514-working.md)
provides the complete corrected equations. It does NOT exclude that
case; both zero and nonzero transverse moving slopes remain to be
treated. Nonzero-cubic W cases are also unresolved.

All five new sources have complete separate saved-source AI reviews
and fresh exact algebraic reconstructions recorded in the ledger.
These are conditional working results, not human expert review,
proof-assistant certification, or established novelty. Other projected
curves, other initial kernels/time profiles and arbitrary chart entry
remain open. Saved checkers remain frozen. The full goal is active.

## Previous investigation: the supplied nondegenerate quadratic-graph sector is recognized

The general cancellation conjecture is still NOT solved. The new
[scoped synthesis510](research/principal-paraboloid-affine-sigma-quadratic-graph-recognition-pass510-working.md)
retains EVERY actual264 hypothesis and proves the following working
result in the supplied, oriented parameterization:

    deg_v(sigma)=1, theta=a*sigma^2+b*sigma+c,
    a*(1+k_s*a) nonzero  =>  k_s belongs to C.

The earlier retained constant-coupling recognition473 then gives
A isomorphic to C^[3], including its separately treated k_s=0 case.
The historical recognition dependencies are retained, not newly
recertified by the present synthesis.

The final new steps close the moving-coefficient cases:
[508](research/principal-paraboloid-moving-conic-curvature-exclusion-pass508-working.md)
uses two exact first integrals and a pole-order argument to force
h''=0. The actual normalized H=0 case is excluded by507, and
[509](research/principal-paraboloid-moving-conic-nonzero-normalized-offset-exclusion-pass509-working.md)
excludes H nonzero. Along with505/506 and the earlier zero-case
exclusions, this is an exhaustive split for the stated profile.

This is NOT a theorem about all projected conics: no actual change
making sigma affine in every conic has been proved. The degree-drop
boundary 1+k_s*a=0, higher-degree theta, other projected curves,
other initial kernels/time profiles and arbitrary chart entry remain
separate. The next bounded investigation is that degree-drop boundary,
without reusing the parity argument that assumed it was nonzero.

The new sources have complete separate saved-source AI reviews and
fresh exact reconstructions recorded in the ledger. The final510
scope review is clean. None of this constitutes human expert review,
proof-assistant certification or an established novelty claim.
Saved checkers remain frozen. The full objective remains active.

## Previous investigation: both transverse conic profiles are excluded

The general cancellation conjecture is NOT solved. Under the FULL
actual264/296/327 conic hypotheses retained in498 and500, the new
[mixed-derivative exclusion506](research/principal-paraboloid-constant-transverse-conic-mixed-derivative-exclusion-pass506-working.md)
rules out the entire constant-gamma alternative. It uses the
[actual normal form504](research/principal-paraboloid-constant-transverse-conic-cubic-time-normal-form-pass504-working.md),
not an assumed polynomial ansatz. Three complete scalar coefficients
require incompatible mixed derivatives of existing coefficient-field
elements. The separately checked
[inverse-square exclusion505](research/principal-paraboloid-inverse-square-transverse-conic-exclusion-pass505-working.md)
rules out the other profile: its complete equations force an actual
coordinate minus a complex constant to be a rational square, in
conflict with its prime valuation. Together these exclude the whole
m_s nonzero sector under the retained conic-chart hypotheses.

For m_s=0, the new [zero-transverse exclusion503](research/principal-paraboloid-moving-conic-leader-zero-transverse-exclusion-pass503-working.md)
further rules out b_s-pa=0. The necessary surviving conditions are

    m=pt+d, p in C*, d in C;
    a_s=0, a_t nonzero, b_s-pa nonzero.

Within that surviving m_s=0 sector, the new
[zero-offset boundary exclusion507](research/principal-paraboloid-moving-conic-zero-normalized-offset-exclusion-pass507-working.md)
shows: IF h''=0, the licensed normalized constant H cannot be zero.
It does not infer h''=0 or exclude H nonzero. Those are separate
remaining cases. The full m_s=0 conic sector is not yet excluded.

Sources502,503,504,505,506,507 have complete separate saved-source AI reviews
and fresh exact reconstructions recorded in the ledger. These are
conditional working results, not human expert review, proof-assistant
verification or an established novelty claim. The degree-drop
boundary, other projected curves, other initial kernels/time
profiles and arbitrary actual-chart entry remain unresolved.
Saved checkers remain frozen; the full objective remains active.

## Previous investigation: the constant conic leader is excluded; transverse coupling has two time profiles

The general cancellation conjecture is still unsolved. All results
below retain the FULL actual264/296/327 chart, variable m=k_s,
affine nonconstant sigma=P, theta=aP^2+bP+c, and
a*(1+ma) nonzero. They do not supply arbitrary chart entry.

In the m_s=0 sector, the earlier495 gives m_tt=0, and494 gives
a_s=0. The new [complete moving-frame reduction496](research/principal-paraboloid-affine-coupling-conic-moving-frame-pass496-working.md)
and [actual-fiber exclusion499](research/principal-paraboloid-constant-conic-leader-two-quasi-exclusion-pass499-working.md)
now prove that a_t cannot vanish. Thus the remaining necessary
conditions in this sector are

    m=pt+d, p in C*, d in C; a_s=0, a_t nonzero.

The proof treats both alternatives of the published field
two-quasi theorem and every zero-constant case. Its final
contradiction specializes an actual polynomial coordinate at
a complex X value; it never specializes a rational invariant
at a pole. An earlier unsaved argument omitted a cubic term
and was rejected. The accepted proof retains that term and
uses a different, fully checked lower-coefficient obstruction.

For the complementary m_s nonzero sector,498 supplies
gamma=m_s/m^3 in F0*, F0=ker(partial_s) finite over C(t), and

    m^-2=B-2*gamma*s, k=K-1/(gamma*m), B,K in F0.

The new [initial-form rigidity500](research/principal-paraboloid-transverse-conic-initial-rigidity-pass500-working.md)
restricts this coefficient to exactly two possible time profiles:

    gamma in C*, or gamma=C/(t-tau)^2 with C in C*, tau in C.

This is necessary, not a realization or exclusion of either profile.
In the constant-gamma branch, [slope rigidity501](research/principal-paraboloid-constant-transverse-conic-slope-rigidity-pass501-working.md)
further gives y=lP+r and

    K in C[t] of degree at most 2,
    l=Lc*m*a-K''/4, Lc in C, including Lc=0,
    b=a*K'+B'/(2*gamma).

The lower equations in these surviving branches remain unresolved.
Sources496,499,500,501 have complete separate saved-source AI
reviews and fresh exact reconstructions recorded in the ledger.
These are working results, not human expert review, Lean
certification or established novelty. The degree-drop boundary,
other projected curves, other initial kernels/time profiles and
arbitrary actual-chart entry remain open. Saved checkers remain
frozen. The full objective remains active.

## Previous investigation: the fifth-root conic branch is excluded

The general cancellation conjecture is still unsolved. Within the
FULL actual264 chart, with variable m=k_s, affine nonconstant sigma,
quadratic theta and quadratic S=sigma^2+k_t*sigma+m*theta, the new
[exclusion495](research/principal-paraboloid-fifth-root-conic-initial-exclusion-pass495-working.md)
proves

    m_s=0  =>  m_tt=0, hence m=pt+d with p in C*, d in C.

This excludes the entire necessary fifth-root family493, including
its zero residual constant. An actual complex polynomial change
creates a coordinate of intrinsic degree one. The complete
coefficient equations then make two initial ratios algebraically
independent. That would force a genuine nonzero locally nilpotent
derivation on a polynomial three-ring to have no nonconstant
invariants, which is impossible. No coefficient root is promoted
to an ambient coordinate, and no quasi-nice classification is used.

The new [unit-multiplier lemma494](research/principal-paraboloid-unit-tangent-multiplier-pass494-working.md)
uses both remaining full scalar coefficients and the genuine
gradient minors. In any affine-sigma chart it makes the common
tangent multiplier a nonzero element of the coefficient field.
In the conic sector with m_s=0 this proves a_s=0, where
a=[sigma^2]theta, even when m_tt=0. It also supplies a valid
transverse coefficient parameter without assuming rationality.

For the complementary m_s nonzero conic sector, the new
[reduction498](research/principal-paraboloid-transverse-coupling-conic-reduction-pass498-working.md)
excludes a cubic intrinsic y and proves

    deg_sigma(y)<=2, m_ss=3*m_s^2/m,
    1/m^2=B-2*gamma*s, k=K-1/(gamma*m),
    gamma in F0*, B,K in F0, F0=ker(partial_s) finite over C(t).

This is only a necessary family. Its lower scalar equations and
actual realization remain unresolved. The gamma,B,K functions
need not be complex or rational, and no root is adjoined.

All three sources494,495,498 have complete separate AI source
reviews and fresh exact reconstructions recorded in the ledger.
They are working results, not human expert review, Lean
certification or an established novelty claim.
The earlier birational projected-plane-line recognition492
remains in force under its retained dependencies.

The remaining q=0 conic cases, the degree drop deg(S)<2,
other nonlinear projected curves, other initial kernels/time
profiles and arbitrary chart entry are still unresolved.
Saved checkers remain frozen. The full objective remains active.

## Previous investigation: the birational projected plane-line sector is recognized

The general cancellation conjecture is still unsolved. The new
[scoped synthesis492](research/principal-paraboloid-birational-plane-line-recognition-pass492-working.md)
proves, conditional on its retained recognition dependencies:

    Full actual264 chart, m=k_s nonzero, projected plane equation of
    degree one, and function-field projection of degree one
      => A isomorphic to C^[3].

In its variable-coupling part, every remaining chart must have
sigma constant in the intrinsic line parameter, and

    m_s=m_tt=0, m=at+d with a in C*, d in C.

Here intrinsic constancy means sigma in L, not sigma in C.
The constant-sigma recognition478 and constant-coupling recognition473
are retained endpoints, not recursively re-certified here. A nonlinear
plane curve can be abstractly an affine line without satisfying this
degree-one plane-equation hypothesis.

The last nonconstant-sigma branch closes in two steps. The
[actual normalization490](research/principal-paraboloid-transverse-contact-universal-normalization-pass490-working.md)
forces the square-root family's h0 to vanish and gives an explicit
complex polynomial coordinate map with inverse. The
[full scalar exclusion491](research/principal-paraboloid-square-root-contact-scalar-exclusion-pass491-working.md)
then excludes its entire normalized family, including the exceptional
zero factor. Synthesis492 records the exhaustive slope, direction and
contact splits, rather than leaving the square-root family as a current
open case.

For a genuinely nonlinear projected conic, the new
[necessary reduction493](research/principal-paraboloid-nonlinear-conic-fifth-root-reduction-pass493-working.md)
treats only the full actual chart with m_s=0, variable m, affine
nonconstant sigma, quadratic theta, quadratic
S=sigma^2+k_t*sigma+m*theta, and m_tt nonzero. It forces

    u^5=t-tau, m=d(t-tau)+C*u^4, [sigma^2]theta=-5/(C*u^4),
    tau,d,C in C, C nonzero, u an EXISTING coefficient-field element.

The proof uses the full scalar and genuine gradient minors, followed
by an algebraic exact-differential obstruction valid in the exact
finite function field. It does not assume that field is rational or
adjoin a root. This is only a necessary family. Its lower scalar
equations, actual realization, the m_tt=0 case and the degree-drop
case remain unresolved.

All four sources490--493 have separate complete AI source reviews.
Fresh unsaved exact reconstructions and read/hash evidence are in
the ledger. These are working results, not human expert review,
proof-assistant certification or an established novelty claim.
All saved checkers remain frozen. Arbitrary chart entry, other
initial kernels/time profiles and the remaining nonlinear projected
curves are still open parts of the full objective.

## Previous investigation: constant contact is excluded; the surviving branch has square-root coefficients

The general cancellation conjecture is still unsolved. Within the
full actual264/296/325 variable-coupling projected-line branch,
with nonconstant sigma, the contact parameter of482 now satisfies

    tau outside C, D tau != 0, D omega != 0.

These are necessary conditions inside this particular chart. They
do not put an arbitrary cancellation candidate into the chart or
prove that its projected curve is a line.

The [invariant-contact exclusion485](research/principal-paraboloid-invariant-contact-scalar-exclusion-pass485-working.md)
closes the entire noncomplex-tau, D tau=0 branch. Its exact
[coefficient reduction484](research/principal-paraboloid-invariant-contact-parameter-reduction-pass484-working.md)
retains a finite algebraic constant field, rather than assuming a
rational one. The full scalar then forces a determinant to vanish.
The proof includes zero moving-intercept derivative and zero
effective-coupling derivative cases, as well as the zero residual
constants that could otherwise be lost by division.

The [constant-contact exclusion487](research/principal-paraboloid-constant-contact-invariant-omega-exclusion-pass487-working.md)
separately excludes tau in C with D omega=0. Its two complete
terminal determinant identities retain the actual scalar's possible
dependence on the coefficient parameters. A separate review corrected
the notation for an original Jacobian after rebasing the derivatives.

For the other constant-tau branch, the
[transverse reduction486](research/principal-paraboloid-constant-contact-transverse-reduction-pass486-working.md)
first gave a necessary quadratic coefficient family. The new
[full scalar exclusion488](research/principal-paraboloid-transverse-contact-scalar-exclusion-pass488-working.md)
now excludes that entire family. One remaining case makes the
three coordinate differentials depend on just two functions, so
the full determinant vanishes. The other leaves a quadratic
coefficient with a necessarily nonzero leading term. Together
with487, this closes every constant-tau alternative in this chart.

The surviving noncomplex-tau branch has the
[square-root reduction489](research/principal-paraboloid-transverse-contact-square-root-reduction-pass489-working.md).
After a licensed actual normalization, there are EXISTING elements
r,w of the coefficient field such that

    s=r^2/2, omega=w^2/2, mu=-r*w,
    lambda=h0*w^2/4+c1*w/2+lambda0,
    k=-h0*r^2/2+(c1*t+c0)*r-2*lambda0*t^2+C*t+E.

The displayed parameters are complex constants, with the nonzero
conditions and exact directional derivative stated in489. No root
is adjoined to the field. This is still only a necessary family:
its lower scalar equations and actual realization remain unresolved.

All six sources484--489 have complete separate AI source reviews and
fresh unsaved algebraic reconstructions recorded in the ledger.
They are working proofs, not human expert review, proof-assistant
certification or an established novelty claim. Saved checkers remain
frozen. The remaining square-root family, nonlinear projected curves,
other initial kernels/time profiles and arbitrary chart entry are
still unresolved.

## Previous investigation: both slopes and the coupling direction must vary

The full cancellation conjecture is still unsolved. Retaining EVERY
actual264 hypothesis, variable coupling m=k_s, a birational projected
line and nonconstant sigma, the new exclusions now give

    lambda outside C, omega outside C, beta=(partial_t+mu partial_s)m != 0.

These are necessary conditions inside the supplied chart, not a
construction of a remaining example or a proof that arbitrary
cancellation candidates enter this chart.

The [quadratic-slope exclusion479](research/principal-paraboloid-complex-quadratic-slope-two-quasi-exclusion-pass479-working.md)
removes every complex omega. It uses both alternatives of a published
two-quasi derivation theorem over C(X), without promoting its generic
coordinate to an ambient coordinate. Its coefficient input is the
[normalized reduction480](research/principal-paraboloid-variable-coupling-zero-quadratic-slope-reduction-pass480-working.md);
the remaining full determinant has a forbidden complex-X factor.

The [zero-direction exclusion481](research/principal-paraboloid-variable-coupling-zero-direction-exclusion-pass481-working.md)
removes the entire beta=0 family left by474. Its proof retains the
exact finite constant field, the zero-intercept-derivative case and all lower
scalar terms. The final identity forces the whole determinant to
vanish, contradicting its nonzero calibration.

The [first-slope exclusion483](research/principal-paraboloid-constant-linear-slope-exclusion-pass483-working.md)
removes every complex lambda. An actual coordinate fiber and an
elementary plane-derivation lemma first force omega to be a rational
function of the invariant intercept. Two coefficients of the full
scalar then contradict its nonconstancy. This argument is independent
of479 and481, retaining477 only for the already excluded case when
both slopes are complex.

The remaining branch has the [contact reduction482](research/principal-paraboloid-nonzero-direction-contact-reduction-pass482-working.md).
With q=B2/beta and a=1/q, put

    tau=t+a, v_contact=mu+2a*omega, b_contact=s+a*mu+a^2*omega.
    d(b_contact)=v_contact*d(tau).

The case of constant tau remains explicit. Exact formal controls show
that neither q nor the auxiliary coefficient beta/q-m is automatically
a separating parameter. Those controls satisfy the high equations
only, not the actual polynomial-ring and full-scalar requirements.

All five new sources have complete separate AI source reviews and
fresh unsaved identity checks, recorded in the ledger. They are not
expert-reviewed or proof-assistant-certified, and originality is not
established. Saved checkers remain frozen. Nonlinear projected curves,
other initial kernels/time profiles and arbitrary chart entry remain
unresolved, as does the surviving nonconstant-slope line branch.

## Previous investigation: variable coupling on a projected line

The full cancellation conjecture is still unsolved. The new results
retain EVERY actual264 hypothesis and restrict to a projected plane
line whose function-field projection is birational. They do not show
that an arbitrary cancellation candidate enters this chart or has
such a projected line.

For variable coupling m=k_s outside C, the
[constant-sigma synthesis478](research/principal-paraboloid-constant-sigma-variable-coupling-recognition-pass478-working.md)
now proves

    sigma in L  =>  m_s=m_tt=0, m=at+d with a in C*, d in C,
                   and A isomorphic to C^[3].

The [full scalar reduction475](research/principal-paraboloid-constant-sigma-variable-coupling-reduction-pass475-working.md)
first excludes every m_s nonzero alternative, with all exceptional
columns and zero slopes handled. Its actual plane-derivation argument
keeps track of denominators in the original polynomial ring. The new
step in478 applies Wang's linear-invariant theorem over C(X) to all
three remaining actual coordinate velocities, forcing m_tt=0.
The exact actual-coordinate recognition endpoint of475 then applies.
The m_tt nonzero alternative left open inside475 is therefore closed
by478, not an additional open branch of the current frontier.

When sigma is nonconstant, put P=sigma and write

    y=lambda P+r, theta=mu P+h, w_int=omega P^2+bP+c.

The [complex-slope exclusion477](research/principal-paraboloid-variable-coupling-complex-slope-exclusion-pass477-working.md)
proves that lambda and omega cannot both belong to C in an actual
variable-coupling chart. There is NO extra assumption on
D r=(partial_t+mu partial_s)r. An actual complex polynomial reframe
removes both constant slopes; the complete scalar then forces m to
be constant, a contradiction. The
[invariant-intercept exclusion476](research/principal-paraboloid-variable-coupling-invariant-intercept-exclusion-pass476-working.md)
handles D r=0, and477 handles its entire complement.
The provisional recognition interpretation of476 was strengthened
before canonical acceptance: that purported subfamily is empty.

The [high-coefficient system474](research/principal-paraboloid-variable-coupling-affine-line-high-gates-pass474-working.md)
also supplies a zero-safe differential system and an exact necessary
coefficient family for beta=D m=0. In that family lambda is complex
if and only if omega is complex, so477 forces both to be noncomplex
in any surviving actual chart. The high constant scalar coefficient
is redundant, not an additional independent constraint. The family
does not establish actual realization or solve the lower equations.

Within the supplied chart,473 still covers every complex-constant
coupling;324 retains reducible third surfaces;303/307 retain degree-two
projection. The remaining irreducible, variable-coupling birational
projection can be nonlinear. If it is a line, the unrecognized data
must have nonconstant sigma and at least one of lambda,omega
noncomplex. None of these necessary conditions constructs an example.

The new sources have full separate AI source reviews and fresh unsaved
exact identity checks, with the precise evidence in the ledger.
Published theorem statements were inspected in their primary texts.
Earlier chart-entry dependencies remain retained, not recursively
re-certified. No expert review, Lean certification, historical novelty
claim, public contact or submission has occurred. Saved checkers remain
frozen, and the full goal remains active and unsolved.

## Previous investigation: all complex-constant coupling is recognized in the supplied chart

The [working synthesis473](research/principal-paraboloid-complete-constant-coupling-recognition-pass473-working.md)
now proves, retaining EVERY actual264 hypothesis and the explicitly
inherited recognition dependencies,

    k_s in C  =>  A isomorphic to C^[3].

For k_s in C*, it also proves n_ss=n_ts=0 and n_s in C.
There is no longitudinal derivative restriction on k and no added
condition on either potential n or ell. The new part is nonzero
constant coupling with arbitrary longitudinal dependence. Zero
coupling was already covered by268 and294 and is not a new discovery.
This remains a supplied-chart result, not unrestricted cancellation.

The [balanced cubic reduction471](research/principal-paraboloid-balanced-cubic-reduction-pass471-working.md)
and [complete balanced descent472](research/principal-paraboloid-balanced-residual-descent-exclusion-pass472-working.md)
close the previously remaining degree patterns. The latter excludes
every higher balanced degree, without an upper-degree bound. Combined
with470's smallest balanced case and468's strict exhaustion, it removes
the entire n_ss*k_ttt nonzero branch when coupling is a nonzero
complex constant.
The original chart then meets the retained recognition theorem457;
the k_ttt=0 branch retains422. This replaces469's cubic restriction.

Within this specified chart, any still-unrecognized case must have
k_s outside C. Retained324 already covers reducible H0 over the exact
field L, and retained303/307 cover degree-two projection. Remaining
work can therefore focus on irreducible H0 and a birational projected
curve. Birationality alone does not make its coordinate ring normal.
A current bounded target is325's projected-line case, whose intrinsic
generators are affine but which still needs an actual-coordinate
recognition or exclusion argument with variable coupling.

The new sources have full separate AI source reviews and fresh exact
identity checks. Two published recognition endpoints were also checked
in their primary texts. Earlier internal recognition dependencies remain
retained, not recursively re-certified. No external expert review,
Lean certification or historical novelty claim has occurred. All saved
checkers remain frozen. The full cancellation conjecture is unsolved,
including arbitrary chart entry and other initial kernels/time profiles.

Scope correction: some recent historical updates below incorrectly
listed zero coupling as still open. The exact268/294 union already
covered it in this chart. The research ledger records the correction
and distinguishes that old coverage from the new473 result.

## Previous investigation: cubic longitudinal coupling is recognized in the supplied chart

The [working recognition corollary469](research/principal-paraboloid-cubic-longitudinal-coupling-recognition-pass469-working.md)
now proves, retaining EVERY actual264 hypothesis and the explicitly
inherited recognition dependencies,

    k_s in C*, k_tttt=0  =>  n_ss=n_ts=0, n_s in C, A isomorphic to C^[3].

There is no additional condition on n or ell. This extends422's
at-most-quadratic longitudinal coupling to at most cubic dependence.
It does NOT prove that arbitrary cancellation candidates enter264,
have constant coupling, or satisfy k_tttt=0.

The new ingredient is the complete exclusion of the strict degree
branch when k=s+f and n_ss*f''' is nonzero. The
[balanced-frontier synthesis468](research/principal-paraboloid-nonlinear-first-balanced-frontier-pass468-working.md)
combines the degree refinement465, the full residual descent467 and
the independent quadratic parity exclusion466. This strict exclusion
works without an upper degree bound. The only alternative is balanced,
and its necessary condition f'''' nonzero rules out the nonlinear
first potential when f''''=0. The original chart then meets457.
The f'''=0 branch instead retains422 directly.

For arbitrary longitudinal f in this same nonlinear branch, the
[balanced quadratic exclusion470](research/principal-paraboloid-balanced-quadratic-sigma-parity-exclusion-pass470-working.md)
now removes (deg sigma,deg y)=(2,3). Together with468, the remaining
necessary degree pairs, with deg(y)=deg(theta), are

    (4,6), (6,9), (8,12).

These are three degree patterns, not three numerical cases or known
examples. Their coefficient functions and actual realizability remain
unclassified. The proof of470 uses the full odd fourth relation and
even primitive minor; whole generation handles both distinct-point
collisions and the derivative-zero boundary.

The new component notes and both syntheses have separate AI source
reviews and fresh unsaved exact identity checks recorded in the ledger.
The recognition endpoints of422 and457 remain retained inputs, not a
new recursive certification of the historical project. No external
expert review, Lean certification or novelty claim has occurred.
Saved checkers remain frozen. The full cancellation conjecture is
still unsolved, including arbitrary chart entry and other coupling,
initial-kernel and time-degree cases.

## Previous investigation: a nonlinear branch has a finite degree frontier

The [working synthesis464](research/principal-paraboloid-nonlinear-first-potential-finite-frontier-pass464-working.md)
retains EVERY actual264 hypothesis and assumes k=s+f, f_s=0,
n_ss nonzero and f''' nonzero. It proves n_sss=0, excludes constant
and affine sigma, and leaves these nine necessary degree pairs,
with a=deg(sigma) and r=deg(y)=deg(theta):

| Alternative | Necessary pairs (a,r) |
| --- | --- |
| r=2a | (2,4), (3,6), (4,8), (5,10), (6,12) |
| 2r=3a | (2,3), (4,6), (6,9), (8,12) |

These are degree patterns, not nine numerical models or realized charts.
Their coefficient functions are not bounded or classified. This does
not recognize the nonlinear branch or prove arbitrary chart entry.

The [tangent-minor argument460](research/principal-paraboloid-nonlinear-first-slope-tangent-degree-reduction-pass460-working.md)
forces quadratic transverse dependence and equal high degrees. The
[degree-ratio proof461](research/principal-paraboloid-strict-nonlinear-degree-ratio-pass461-working.md)
leaves precisely r=2a or 2r=3a. The elementary degree bound from299
then gives r<=12, without requiring a normal plane projection.

Two boundary arguments are separate. The
[constant-sigma exclusion462](research/principal-paraboloid-constant-sigma-nonlinear-first-slope-exclusion-pass462-working.md)
works for arbitrary f, without requiring f''' nonzero: the original
scalar would make an irreducible actual-coordinate polynomial a
square in its fraction field. The
[affine-sigma exclusion463](research/principal-paraboloid-affine-sigma-irrational-residue-exclusion-pass463-working.md)
uses459's degree reduction and the genuine minor unit. It forces
lambda=-1 plus or minus sqrt(3), then a logarithmic derivative with
irrational residue. Taking the norm from the finite coefficient field
to C(t) contradicts the integer residue of a rational logarithmic
derivative. No rational-coefficient-field ansatz is used.

All six new notes459--464 have separate AI source reviews and fresh
unsaved identity checks recorded in the ledger. Earlier264/296/458
dependencies remain retained, not recursively re-certified here.
There is no expert review, Lean certification or novelty claim.
All saved checkers remain frozen. Higher-degree strict and balanced
cases remain under investigation, and the full cancellation conjecture
is still unsolved.

## Previous investigation: the transversely affine first-potential family is recognized

The [working synthesis457](research/principal-paraboloid-affine-first-potential-recognition-pass457-working.md)
now proves, retaining EVERY actual hypothesis of264,

    k_s in C*, n_ss=0  =>  n_ts=0, n_s in C, A isomorphic to C^[3].

There is no added restriction on k_ttt, n_ttt or ell. This removes
the assumption that n_s was already a complex constant in436.
It does NOT establish constant coupling or n_ss=0 for an arbitrary
chart, or put arbitrary cancellation candidates in this chart.

The moving-slope alternative is now exhausted. The complete lists441/442
contain eleven resonant and eight nonresonant positive-degree cases,
together with separately treated constant and zero boundaries.
The synthesis gives the exact exclusion for every case. New
[451](research/principal-paraboloid-nonresonant-quadratic-cofactor-exclusion-pass451-working.md)
and [453](research/principal-paraboloid-nonresonant-affine-minor-scalar-exclusion-pass453-working.md)
remove the nonresonant quadratic and affine cases respectively.
The [parity/minor argument454](research/principal-paraboloid-cubic-profile-parity-minor-exclusion-pass454-working.md)
excludes (2,3,4) in BOTH regimes; it does not extend450's
resonance-only collision proof by dropping a coefficient.

The main new device is an exact tangent identity. Whole polynomial-line
generation makes the derivative vector primitive, and the genuine
gradient-minor unit forces the cross product of the two gradients
to be a NONZERO CONSTANT multiple of that derivative vector.
This sharply limits the degree of one explicit minor. The
[four exclusions455](research/principal-paraboloid-tangent-minor-intermediate-profile-exclusions-pass455-working.md)
then remove the intermediate cases, and the
[final high-degree exclusion456](research/principal-paraboloid-quartic-sextic-octic-minor-exclusion-pass456-working.md)
removes (4,6,8) in both regimes, including all zero-coefficient boundaries.
The resulting constant first-potential slope meets the retained
recognition theorem436 in the original ring.

A separate [explicit control452](research/principal-paraboloid-cubic-quartic-quintic-all-parameter-control-pass452-working.md)
satisfies the quadric and every all-parameter polynomial return,
but fails the genuine fourth potential. It shows why those weaker
conditions alone cannot supply the new exclusions. It is not an
actual chart or a cancellation counterexample.

The new component arguments, exact degree coverage and synthesis have
separate AI reviews and fresh unsaved identity checks. The recognition
dependencies of436 remain explicit retained inputs, not a newly
completed recursive audit of the entire project. There is no expert
review, Lean certification or novelty claim. Saved checkers stay frozen.

The [follow-on reduction458](research/principal-paraboloid-arbitrary-first-potential-birational-projection-pass458-working.md)
now treats arbitrary n. It retains every additional n_ss term in
the complete third and fourth equations and proves that, when n_ss
and k_ttt are nonzero, the projection to L[sigma,theta] is finite
birational. For nonconstant sigma its explicit conductor denominator
is nonzero; this does not make the projected ring normal or equal
to the whole polynomial line. The all-parameter polynomial return
also survives arbitrary n, with an explicit inverse transformation.

At that stage the remaining constant-coupling branch permitted n_ss
nonzero when k_ttt was nonzero.458 reduced it without recognizing it;
473 above now closes it. Variable coupling, other initial kernels and
degree profiles, and arbitrary actual-frame entry remain unresolved in
general. The earlier inclusion of zero coupling in this paragraph was
incorrect:268/294 had already covered that branch in the supplied chart.
The full cancellation conjecture is still unsolved here.

## Previous investigation: the moving-slope frontier has narrowed further

Under EVERY actual264 hypothesis, the new investigation assumes
k=s+f, n=nu*s+n0, with f,nu,n0 killed by partial_s and nu' nonzero.
These are still substantial restrictions on an already specified
initial kernel and degree profile. Arbitrary cancellation candidates
are not known to enter this chart.

The [complete fourth potential438](research/principal-paraboloid-moving-transverse-slope-fourth-potential-pass438-working.md)
excludes a degree-two projection using the genuine gradient-minor
unit. The surviving projection is finite birational, not necessarily
an equality of polynomial rings. The
[direct exclusion440](research/principal-paraboloid-arbitrary-longitudinal-moving-first-slope-constant-sigma-exclusion-pass440-working.md)
also rules out constant sigma, including the zero-denominator boundary.

The [quadric reduction441](research/principal-paraboloid-arbitrary-longitudinal-moving-slope-quadric-degrees-pass441-working.md)
uses an invertible polynomial change of the three intrinsic generators,
without dividing by an evaluated nonunit. Their new degrees are at
most eight. When f''' differs from 6nu', only eight nonconstant
degree profiles remain. The separate
[resonance analysis442](research/principal-paraboloid-moving-slope-resonance-degree-profiles-pass442-working.md)
treats f'''=6nu', including both constant-q boundaries. It also
excludes the zero-q boundary outside resonance. Combining the two
cases gives bounds for the ORIGINAL intrinsic generators:

    1 <= deg(sigma) <= 4,  deg(y) <= 6,  deg(theta) <= 8.

The [equal-quartic exclusion443](research/principal-paraboloid-equal-quartic-two-quadric-exclusion-pass443-working.md)
then removes the resonance profile (4,4,4). A whole polynomial
line of the forced degree triple (4,3,2) has only one quadratic
relation, contradicting the two genuine independent gradients.
The [quadratic-cofactor exclusion444](research/principal-paraboloid-cubic-profiles-quadratic-cofactor-exclusion-pass444-working.md)
also removes (3,2,1) and (3,3,3): the entire quadratic-relation
space forces a nonunit common gradient factor.

The [zero-boundary exclusion445](research/principal-paraboloid-moving-slope-zero-remainder-scalar-exclusion-pass445-working.md)
now removes q=0 completely. The full scalar places a coefficient
on a fixed conic. At nonzero conic level a nontrivial involution
contradicts the actual fraction-field return; at zero level the
original slice contradicts the exact coefficient-adjoined ring.
Neither endpoint assumes that the invariant curve field is rational.

The [all-parameter collision lemma446](research/principal-paraboloid-affine-sigma-resultant-collision-pass446-working.md)
also excludes (1,2,3) in BOTH resonance and nonresonance. More
generally, when sigma is affine, the centered x cannot have
degree at least two. An exact resultant produces either a pair
of indistinguishable points or a point where every generator
derivative vanishes, contradicting the original all-X ring return.

The full-scalar arguments
[447](research/principal-paraboloid-affine-resonant-profile-scalar-exclusion-pass447-working.md)
and [448](research/principal-paraboloid-quadratic-resonant-profile-scalar-exclusion-pass448-working.md)
exclude the resonant profiles (1,1,1) and (2,2,2). The first keeps
both scalar-factor branches and uses the ORIGINAL polynomial slice;
an unjustified slice normalization in its draft was caught and repaired
before acceptance. The second proves that its scalar specialization
is at a complex constant before using it.

The [quadratic-sigma collision proof449](research/principal-paraboloid-quadratic-sigma-resultant-collision-pass449-working.md)
excludes (2,4,6) in both regimes, and the
[linear-resultant proof450](research/principal-paraboloid-cubic-resonant-profile-collision-pass450-working.md)
excludes (2,3,4) only in resonance. Both explicitly construct a
pair outside the equal-p exceptional set and cover repeated roots.

The necessary positive-degree frontiers are now:

    Resonance:     (3,4,5), (4,5,6), (4,6,8).
    Nonresonance:  (1,1,1), (2,2,2), (3,4,5),
                  (2,3,4), (4,6,8), (3,5,7).

These are degree patterns, not asserted actual models. Arbitrary
cancellation candidates are still not known to enter this chart.

The [collision boundary439](research/principal-paraboloid-moving-slope-centered-collision-boundary-pass439-working.md)
keeps the exceptional average coefficient in the all-X collision
equations. A formal example shows why the centered surface relation
and all-parameter generation alone do not justify a proposed
two-generator return. It is not an actual264 realization or a
counterexample to cancellation.

The next bounded tasks examine the complete calibrated scalar in
the nonresonant (1,1,1) case and the all-X collision conditions
in the remaining higher-degree resonant cases. The nonresonant
(2,3,4) boundary cannot simply reuse450: a quadratic correction
is present there and cannot be dropped. All other profiles retain
the full original constraints. A finite degree list is not a recognition
theorem, a finite list of numerical models, or a solution of the
full cancellation conjecture. The notes have separate AI reviews
and fresh unsaved exact identity checks, not expert or Lean
certification. Saved checkers remain frozen.

## Previous investigation: the constant-first-slopes family is recognized

The [working synthesis436](research/principal-paraboloid-constant-first-slopes-recognition-pass436-working.md)
now gives, under EVERY actual hypothesis of264,

    k_s in C*, n_s in C  =>  A isomorphic to C^[3].

There is no added condition on ell_s, k_ttt or n_ttt.
This removes429's relation m*ell_s+nu^2=0. The full actual
principal initial kernel, profile, slice, selected derivation,
localization and both polynomial returns are still required.
No result says every cancellation candidate satisfies them.

The new nonzero-second-slope branch is finite and explicit.
[434](research/principal-paraboloid-constant-second-slope-discriminant-reduction-pass434-working.md)
reduces it to two nonconstant intrinsic profiles and one constant
profile, retaining every moving level. The nonconstant profiles
are excluded by the complete collision arguments
[435](research/principal-paraboloid-affine-sigma-nonlinear-time-exclusion-pass435-working.md)
and [437](research/principal-paraboloid-quadratic-sigma-collision-exclusion-pass437-working.md).
Both include repeated roots. The latter uses an elementary
degree-eight root-avoidance lemma, not numerical sampling.

In the remaining case, the actual coordinate frame
X,Y,W-XZ,Z makes Z polynomial in the first three coordinates
over an invariant curve field. The retained criterion266 and
its published regular-kernel theorem then recognize the
original ring. This does not promote a generic line parameter
to an original coordinate. The old zero-third-derivative and
zero-second-slope branches retain348/346 and427 respectively.

The component proofs and synthesis have separate AI reviews
and fresh unsaved exact checks. Their dependency boundaries
are recorded in the ledger; this is not recursive verification
of every historical source, expert review, Lean certification
or novelty clearance. Saved checkers remain frozen.

The next principal-chart question allows a varying first-potential
slope. Its third relation has a potentially nonunit coefficient
of theta, so the present plane elimination cannot simply be
reused. General coupling, other initial kernels/profiles and
arbitrary actual-frame entry remain unresolved.
The full cancellation conjecture is still unsolved here.

## Previous investigation: two variable second-potential slopes are excluded

The [complete plane reduction430](research/principal-paraboloid-arbitrary-longitudinal-plane-reduction-pass430-working.md)
and [weighted exclusion431](research/principal-paraboloid-nonlinear-time-weighted-plane-exclusion-pass431-working.md),
followed by the [variable-slope exclusion433](research/principal-paraboloid-variable-second-slope-exclusion-pass433-working.md),
give this necessary condition under EVERY actual hypothesis of264:

    k=s+f, f_s=n_s=0, f_ttt nonzero, ell_s nonzero
        => ell_ss=ell_ts=0, so ell_s is a nonzero complex constant.

430 retains the complete moving levels and uses the full scalar
to derive a polynomial-plane relation whose evaluated gradient
generates the unit ideal. If ell_ss is nonzero, its weighted
leading form forces incompatible degrees for two polynomials
that must generate the entire polynomial line. If ell_ss=0 but
ell_ts is nonzero, monicity and the gradient condition force
affine projections. Evaluating at one actual X value then leaves
a quadratic and a cubic that would have to generate a polynomial
line, which is impossible by a short collision/derivative proof.

This is a reduction, not recognition of the surviving nonzero
constant-slope family. No theorem here places every cancellation
candidate in this chart or forces n_s=0 or k_s constant.
The full conjecture remains unsolved.

The separate [irredundancy supplement432](research/flow-affine-irredundant-generators-no-coordinate-pass432-working.md)
proves that deleting any member of428's eleven-generator list
destroys generation. Thus even deletion-irredundancy does not
repair the proposed linear-coordinate extraction. The same
ring has four known coordinates, recovered nonlinearly; there
is no minimum-cardinality claim or cancellation counterexample.

The ledger records exact source hashes, independent AI reviews
and fresh unsaved identity checks. Saved checkers remain frozen.
None of these results has human-expert or Lean certification,
and no historical novelty, external submission or contact is claimed.

## Previous investigation: removing a coupling derivative restriction in a specified sector

The [working recognition427](research/principal-paraboloid-arbitrary-longitudinal-coupling-recognition-pass427-working.md)
proves, under EVERY actual hypothesis of264,

    k_s in C*, n_s=ell_s=0  =>  A isomorphic to C^[3],

with no condition on k_ttt. This is not all of422 with its derivative
restriction removed: the two displayed potential conditions are
substantial additional assumptions. No actual realization of the
new k_ttt nonzero subcase is claimed.

The [actual transverse-slope corollary429](research/principal-paraboloid-constant-transverse-slope-recognition-pass429-working.md)
extends this to k_s=m in C*, n_s=nu in C and m*ell_s+nu^2=0.
The genuine polynomial map X*=X+nu/m, W*=mW+2(nu/m)Z, with
Y,Z fixed, reduces exactly to427. It places no bound on k_ttt
or n_ttt, but does not remove the displayed transverse conditions.

The new branch has a short direct obstruction. A centered polynomial
relation x^2=R(sigma), with R cubic, has an evaluated gradient unit
forced by the full actual Jacobian. Repeated roots violate that unit.
Three simple roots would force more zeros of sigma' than its degree
allows. Thus two intrinsic projections are constant. An explicitly
constructed global locally nilpotent derivation then preserves an
ACTUAL polynomial three-ring, and published recognition theorems
apply. The k_ttt zero branch retains348/337's working dependencies.

The separate [filtered-frame obstruction426](research/general-coupling-normalization-obstruction-pass426-working.md)
shows that normalization to k=s by the precisely specified original
weighted-degree-bounded polynomial frames is possible exactly when
k_s is a nonzero complex constant and k_ttt=0. It does not classify
maps with higher weighted terms that cancel in E-time.427 therefore
uses a recognition argument, not an unjustified extension of the old
normalizing shear.

The global-entry search also produced the explicit
[flow-affine generating-space obstruction428](research/flow-affine-generating-space-no-coordinate-control-pass428-working.md).
Eleven flow-affine polynomials generate an actual polynomial four-ring,
but their entire affine-linear span contains no coordinate. Their
velocities generate the unit ideal and their differentials generate
the cotangent module. This disproves the proposed linear-extraction
step, not nonlinear coordinate recovery, which is explicit in the
example. It is not a cancellation counterexample.

The completed [bounded dependency audit425](research/recognition-dependency-audit-pass425-working.md)
and [nonunit-speed control424](research/principal-paraboloid-nonunit-speed-actual-control-pass424-working.md)
are now recorded. The audit found no new gap in its selected bridges;
it did not recursively certify422. The actual control has a nonunit
speed and a generic line parameter outside the original invariant
ring, illustrating why localization cannot be silently reversed.

The ledger records full-source reviews, fresh unsaved exact checks
and held hashes. All saved checkers remain frozen. These are
AI-reviewed working arguments, not human-expert or Lean certification,
and no historical novelty is claimed.

General coupling and potentials, other initial kernels and profiles,
and arbitrary actual-frame entry remain unresolved. The full
cancellation goal is active and unsolved. Luo's intended field and
dimension are still unconfirmed; no external contact or submission
has occurred.

## Previous investigation: a constant-coupling restricted chart is recognized

The [working synthesis422](research/principal-paraboloid-constant-coupling-recognition-synthesis-pass422-working.md)
closes the remaining nonlinear first-potential cases under EVERY
supplied actual264 hypothesis with k=s. In this exact restricted
chart, it proves n_ss=0. Combined with the retained recognition
dependencies363/348/346, it gives

    full actual264, k_s in C*, k_ttt=0
        => n_ss=n_ts=0 and A0 isomorphic to C^[3].

The constant-coupling normalization is an actual complex polynomial
map and does not initially assume n_ss=0. The new result removes
that assumption; it does not remove the other actual264 gates.

The former six-profile list is now exhausted. The full-potential
[curvature evolution419](research/principal-paraboloid-higher-degree-curvature-evolution-pass419-working.md)
forces a coefficient ratio to have nonzero characteristic derivative.
In the cubic profile, the separate
[all-X collision proof420](research/principal-paraboloid-equal-cubic-collision-curvature-ratio-pass420-working.md)
forces that same ratio to be complex, a contradiction. The
[geometric transfer421](research/principal-paraboloid-equal-degree-geometric-profile-reduction-pass421-working.md)
excludes four profiles, treating the zero centered level separately.
The final [sextic exclusion423](research/principal-paraboloid-equal-sextic-filtered-cubic-exclusion-pass423-working.md)
uses the entire intrinsic curve ideal and a nonzero forbidden cubic
coefficient. No lower potential function is discarded.

The new component proofs have separate full-source AI reviews and
fresh exact identity reconstructions. The ledger records final
hashes, the synthesis review, and the inherited-dependency boundary.
These checks are not human-expert review or Lean certification.
The recognition corollary retains earlier working theorems, not
a newly completed recursive certification of the entire project.
All saved checkers remain frozen.

The full cancellation question is still unsolved here. General
coupling k, other full initial kernels and degree profiles, and
entry from an arbitrary sliced polynomial four-ring remain open
in this investigation. No proof says that every candidate lies
in the restricted chart. Luo has not confirmed the intended
field and dimension. No novelty claim, outreach, publication,
submission or formal certification occurred.

## Previous investigation: the entire equal-quadratic branch is excluded

Under EVERY supplied actual264 hypothesis, with k=s and n_ss nonzero,
the [reviewed working synthesis417](research/principal-paraboloid-equal-quadratic-exclusion-synthesis-pass417-working.md)
now gives

    3 <= d=deg theta=deg sigma <= 6,    deg y <= d;
    mu=lc(theta)/lc(sigma) does not belong to C+C*t.

Degree one was excluded by411. New414--416 exhaust the quadratic
case. The [complex-slope exclusion414](research/principal-paraboloid-equal-quadratic-complex-slope-exclusion-pass414-working.md)
combines actual polynomial generation with incompatible full scalar
and genuine-potential coefficients. The
[nonconstant-slope exclusion416](research/principal-paraboloid-nonconstant-slope-quadratic-collision-exclusion-pass416-working.md)
uses a collision at a finite original X value. The
[exceptional exclusion415](research/principal-paraboloid-exceptional-quadratic-leading-direction-exclusion-pass415-working.md)
retains the remaining coefficient freedom, then derives a full
determinant with a nonzero intrinsic linear term. Repeated-root
collisions and zero integration constants are included.

The actual global slice is essential: after adjoining the retained
coefficient field, it gives L[B]=L[X,v]. Specializing any X must
therefore leave generators of the entire intrinsic polynomial line.
The argument does not infer an original coordinate from a
coefficient-field parameter or from rational-field equality.

All surviving directions are nonexceptional, with delta=lambda-n_s
nonzero. Here lambda=[v^d]y/[v^d]sigma, so it is zero when deg y<d.
Writing u1=y-lambda*sigma, v1=theta-mu*sigma,
m=max(deg u1,deg v1), and r=deg(2delta*u1+beta*v1+j),
the exact remaining necessary list from407 is

    (r,m,d) = (1,2,3), (1,3,5), (2,3,4),
              (2,4,6), (3,4,5), (4,5,6).

The characteristic restrictions D(lambda)=0 and D(mu)=-4lambda
from413 remain imposed, with D=partial_t+mu*partial_s. No member
of this list is yet excluded or realized by the new result.

The component proofs and synthesis have separate full-source AI
reviews and fresh exact algebra reconstructions. The ledger records
the final hashes and a corrected omission in a supplemental Root
check; that omission was not in the saved proof. All saved checkers
remain frozen.

This is still a restricted-chart result, not a cancellation proof.
Higher degrees, general coupling k, other full initial kernels,
arbitrary-chart entry and original-ring recognition remain unresolved.
No human-expert review, formal certification, novelty claim,
outreach or submission occurred. Luo has not confirmed the intended
field and dimension of the original question.

## Previous investigation: degree one is excluded and higher leading slopes are constrained

Under EVERY supplied actual264 hypothesis, with k=s and n_ss nonzero,
the [reviewed working synthesis411](research/principal-paraboloid-equal-degree-one-exclusion-synthesis-pass411-working.md)
now gives

    2 <= d=deg theta=deg sigma <= 6,    deg y <= d;
    lc(theta)/lc(sigma) does not belong to C + C*t.

The whole equal-degree-one case is excluded, not just a generic
subcase. The proof combines the earlier delta-zero conductor argument
with the [zero-slope exclusion404](research/principal-paraboloid-equal-degree-one-zero-slope-conductor-exclusion-pass404-working.md),
the [vanishing-characteristic exclusion405](research/principal-paraboloid-equal-degree-one-characteristic-zero-exclusion-pass405-working.md)
and the [s-constant-slope exclusion406](research/principal-paraboloid-equal-degree-one-s-constant-slope-exclusion-pass406-working.md).
An actual complex polynomial automorphism handles every complex
constant slope; no coefficient-dependent ambient shear is used.

The remaining branch has the necessary
[contact reduction409](research/principal-paraboloid-equal-degree-one-contact-reduction-pass409-working.md).
Its constant-parameter boundary reaches the full
[compact-scalar obstruction408](research/principal-paraboloid-compact-equal-degree-scalar-obstruction-pass408-working.md).
For its nonconstant parameter, the new
[potential-compatibility contradiction410](research/principal-paraboloid-equal-degree-one-contact-compatibility-exclusion-pass410-working.md)
forces two third derivatives to have nonzero product, then forces
one of those derivatives to vanish. All functions are retained in
the exact coefficient field, and no rationality ansatz is made.

For d>=2, the separately reviewed
[rank split407](research/principal-paraboloid-equal-degree-higher-rank-split-pass407-working.md)
leaves seven nonexceptional degree profiles and one exceptional
quadratic family. Those possibilities are not excluded or realized.
The new [leading-scalar proof412](research/principal-paraboloid-equal-degree-leading-scalar-gates-pass412-working.md)
extends two necessary equations to all equal degrees by an exact
degree argument. The [higher-degree reduction413](research/principal-paraboloid-higher-degree-characteristic-zero-reduction-pass413-working.md)
then forces, with lambda=[v^d]y/[v^d]sigma and D=partial_t+mu*partial_s,

    D(lambda)=0,    D(mu)=-4lambda.

These are additional necessary conditions on the remaining profiles.
No degree-one-only scalar exclusion is being applied to them.
The ledger records full-source AI reviews, independent exact
reconstructions, corrected errors and final source hashes.

This remains a restricted-chart result, not a proof of cancellation.
Higher degrees, general coupling k, other full initial kernels,
arbitrary-chart entry and recognition of the original invariant ring
are unresolved. No human-expert review, formal certification or
novelty claim has occurred. Luo has not confirmed the intended field
and dimension of the original question.

## Previous investigation: constant theta and a degree-one boundary are excluded

Under every supplied actual264 hypothesis, with k=s and n_ss nonzero,
the [reviewed working synthesis400](research/principal-paraboloid-equal-degree-leading-ratio-obstruction-pass400-working.md)
now gives the necessary conditions

    1 <= deg theta = deg sigma <= 6,    deg y <= deg sigma;
    lc(theta)/lc(sigma) does not belong to C + C*t.

The entire constant-theta boundary is excluded. For its nonzero-slope
branch, [397](research/principal-paraboloid-constant-theta-nonzero-slope-coefficient-family-pass397-working.md)
derives the necessary coefficient family, and
[398](research/principal-paraboloid-constant-theta-coefficient-family-actual-normalization-pass398-working.md)
normalizes it by an actual complex polynomial automorphism. The
[complete scalar contradiction399](research/principal-paraboloid-constant-theta-nonzero-slope-scalar-exclusion-pass399-working.md)
then excludes the family, including its zero-parameter case. The
separate396 proof had already excluded zero slope.

The additional leading-ratio obstruction uses two explicit actual
maps from384. A complex-affine ratio could be canceled, producing
either a strict degree order or constant theta, both now excluded.
This argument does not allow arbitrary coefficient-field shears.

The degree-one case has now been narrowed further. Writing
y=lambda*sigma+r, the new
[conductor exclusion403](research/principal-paraboloid-delta-zero-conductor-exclusion-pass403-working.md)
proves lambda cannot equal n_s. The
[necessary family401](research/principal-paraboloid-equal-degree-one-delta-zero-necessary-family-pass401-working.md)
alone left a potentially nonzero scalar. The
[actual-return argument402](research/principal-paraboloid-delta-zero-finite-normalization-pass402-working.md)
then gave an explicit finite polynomial normalization. Its conductor
must be preserved by the original derivation, and403 proves that
this is impossible. No unsupported normality assumption is used.

The new notes have separate full-source AI reviews and fresh
exact reconstruction of their concrete identities. The
[ledger](research-ledger.md) records the dependency reviews and hashes.

These are restricted-chart results, not a cancellation proof.
The degree-one lambda!=n_s sector, higher equal degrees, general
coupling k, other full initial ideals and arbitrary-chart entry remain
unresolved. The new proof excludes a subcase, not the whole degree-one
sector or an arbitrary cancellation candidate.
No human-expert review, formal certification or novelty claim has
occurred, and Luo has not confirmed the working interpretation.

## Previous investigation: both nonconstant strict degree orders are excluded

Under every supplied actual264 hypothesis, with k=s and n_ss nonzero,
the [reviewed working synthesis395](research/principal-paraboloid-nonlinear-strict-order-exclusion-pass395-working.md)
now leaves exactly these necessary alternatives:

    theta nonconstant: 1 <= deg theta = deg sigma <= 6,
                       deg y <= deg sigma;
    theta constant:   deg sigma = deg y = 1,
                       y = lambda*sigma+r, lambda in L nonzero.

The formerly remaining strict sigma-dominant pair(2,3) is excluded
in both coefficient cases. The [zero-gate proof391](research/principal-paraboloid-sigma-dominant-quadratic-cubic-zero-gate-exclusion-pass391-working.md)
combines the complete lower potential with a scalar coefficient and
an exact rationality/integrality argument. In the other case,
[392](research/principal-paraboloid-sigma-cubic-nonzero-gate-normal-form-pass392-working.md)
derives a polynomial normal form over the retained coefficient field.
The original global slice then gives the actual
[polynomial return393](research/principal-paraboloid-sigma-dominant-polynomial-return-degree-gate-pass393-working.md),
whose degree bound is essential to the
[lower-potential contradiction394](research/principal-paraboloid-sigma-dominant-nonzero-gate-lower-potential-exclusion-pass394-working.md).
No free lower coefficient function is dropped to obtain that contradiction.

Separately, [396](research/principal-paraboloid-constant-theta-zero-slope-exclusion-pass396-working.md)
excludes the zero-slope constant-theta boundary through four coefficients
of the full actual determinant. It does not apply the nonconstant-theta
normalization to that boundary.

The new notes have full source reads and separate AI audits, with
critical identities independently reconstructed in fresh exact algebra.
No saved checker was executed or rerun. The [ledger](research-ledger.md)
records source hashes, review evidence and the remaining gaps.

This is a result within a supplied chart, not a solution of cancellation.
Equal-degree cases and the nonzero-slope affine boundary remain open
here. General coupling k, other initial ideals and arbitrary-chart entry
are also unresolved. There has been no human-expert review, formal
certification or novelty claim. The professor has not confirmed the
working interpretation of the original question.

## Previous investigation: one nonconstant strict-order degree pair remains

Under every supplied actual264 hypothesis, with k=s and n_ss nonzero,
the reviewed working arguments now exclude the entire theta-dominant
orientation and two of the three possible nonconstant sigma-dominant
profiles. In the latter orientation the only remaining pair is

    (deg theta, deg sigma) = (2,3), with deg y = 1.

The [moving-intercept exclusion388](research/principal-paraboloid-affine-theta-moving-intercept-exclusion-pass388-working.md)
and [constant-t-intercept exclusion389](research/principal-paraboloid-affine-theta-constant-t-intercept-exclusion-pass389-working.md)
cover the two exhaustive subcases of the pair(1,2). Both use the
literal calibrated determinant;389 also needs the strong complex
field return, not just generation after adjoining the coefficient
field. The [literal-cubic exclusion390](research/principal-paraboloid-sigma-dominant-four-six-cubic-exclusion-pass390-working.md)
rules out(4,6) using the entire intrinsic curve ideal and a finite
degree-reduction argument. Its cubic was rebuilt in this orientation,
not inferred by exchanging the two intercepts.

All three drafts have full source reads and separate AI audits.
Their finite algebraic identities were independently reconstructed
in fresh unsaved computations. No saved checker was executed.
The [ledger](research-ledger.md) records the precise evidence.

This is a reduction within the supplied chart, not a proof of
cancellation. The remaining pair(2,3), equal-degree profiles,
constant theta, general coupling k, other initial ideals and
arbitrary-chart entry are still unresolved. There has been no
human-expert review, formal certification or novelty claim.

## Previous investigation: the nonlinear theta-dominant branch is excluded

The [working synthesis383](research/principal-paraboloid-nonlinear-theta-dominant-exclusion-pass383-working.md)
now excludes every theta-dominant intrinsic degree profile under the
complete supplied actual264 hypotheses, with k=s and n_ss nonzero.
The precise necessary conclusion is

    1 <= deg sigma <= 6,
    deg theta <= deg sigma, and deg y <= deg sigma.

Thus sigma must attain the largest intrinsic degree. Equal degrees
and the opposite strict inequality remain unresolved. This does not
show n_ss=0, recognize the original invariant ring, or establish that
arbitrary cancellation candidates enter this chart.

The previous investigation left one degree pair, (2,3), in this
orientation. The new [lower-potential gates377](research/principal-paraboloid-quadratic-cubic-lower-potential-two-mode-gate-pass377-working.md),
[scalar gates378](research/principal-paraboloid-quadratic-cubic-sixth-scalar-gate-pass378-working.md)
and [composition380](research/principal-paraboloid-quadratic-cubic-mode-composition-pass380-working.md)
reduce its nonzero-E case to explicit coefficient families, retaining
the zero-slope overlap. The key additional
[original-ring return379](research/principal-paraboloid-quadratic-cubic-polynomial-return-speeds-pass379-working.md)
proves polynomial-plane equality after adjoining the exact coefficient
field and forces the calibrated scalar into that field.

The [degree exclusion381](research/principal-paraboloid-rank-one-polynomial-generation-exclusions-pass381-working.md)
then eliminates two families: actual polynomial generation would
contradict the characteristic-zero Abhyankar--Moh degree theorem.
The [scalar exclusion382](research/principal-paraboloid-reciprocal-slope-nonconstant-return-scalar-exclusion-pass382-working.md)
eliminates the remaining family using a nonzero seventh-degree
coefficient in a determinant required to be constant in those variables.
The arbitrary residual coefficient function and its zero boundaries
are retained. No rationality of the exact coefficient field is assumed.

All seven new notes377--383 have complete source reads and separate
AI audits. The critical finite algebraic identities were independently
reconstructed in fresh unsaved computations. No saved checker was
executed or rerun. The [ledger](research-ledger.md) records hashes,
review evidence and the remaining gaps. This is a working proof chain,
not recursive formalization, human-expert certification, or a novelty
claim. The unrestricted conjecture is still unsolved, and the
professor has not confirmed the working interpretation.

Further reviewed notes constrain the next investigation.
The [actual-frame analysis384](research/principal-paraboloid-actual-filtered-symmetry-obstruction-pass384-working.md)
proves exact valid transports, but shows that frames with the stated
original weighted-degree bounds cannot move an equal/reversed
profile into the excluded orientation. Higher-weight cancellations
are not covered by this obstruction.
The [opposite-order reduction385](research/principal-paraboloid-nonlinear-sigma-dominant-degree-reduction-pass385-working.md)
shows that, when theta is nonconstant and has smaller degree,
the necessary pairs (deg theta,deg sigma) are (1,2), (2,3), (4,6).
It also proves exact differential equations for the leading y/sigma
ratio without dividing out its possible zero value. These pairs
have not yet been excluded.
The [exact compatibility argument387](research/principal-paraboloid-sigma-dominant-coefficient-integrability-pass387-working.md)
now forces that leading ratio to be zero in this strict opposite-order
case. Consequently n_ts=0, n_t is complex constant, and
deg y<deg theta<deg sigma. A rationality step inside the proof is
derived from an exact equation; no rational coefficient-field ansatz
is assumed. The three remaining pairs still require further work.
The [constant-theta reduction386](research/principal-paraboloid-nonlinear-constant-theta-line-gates-pass386-working.md)
shows that theta in L forces sigma to be an affine intrinsic parameter
and y affine in sigma. Its differential gates retain the zero slope;
this boundary has not been excluded or recognized.

## Previous investigation: two nonlinear degree patterns are excluded

Under every hypothesis of the supplied actual principal chart264,
assume k=s, n_ss is nonzero, and theta has larger intrinsic degree
than sigma. The reviewed reductions now leave only

    (deg sigma, deg theta) = (2,3).

This is a necessary restriction within that supplied chart, not
recognition or a proof that arbitrary cancellation candidates enter it.
Equal degrees and the reverse inequality remain outside this conclusion.

The [normal form368](research/principal-paraboloid-affine-quadratic-nonlinear-profile-normal-form-pass368-working.md)
split the degree pair (1,2) into two alternatives. The
[quadratic-field exclusion371](research/principal-paraboloid-quadratic-field-affine-quadratic-exclusion-pass371-working.md)
excludes the first using the full nonzero calibrated determinant.
The new [field-return exclusion375](research/principal-paraboloid-affine-quadratic-rational-return-exclusion-pass375-working.md)
excludes the other: exact integration gives a rational map of degree
six where the original complex field equality requires degree one.
The residual scalar in that second argument is nonzero; the strong
field return, not a supposed zero Jacobian, supplies the contradiction.

The [whole-line normal form370](research/principal-paraboloid-degree-two-four-six-odd-part-normal-form-pass370-working.md)
and [genuine-cubic exclusion373](research/principal-paraboloid-degree-four-six-filtered-cubic-exclusion-pass373-working.md)
exclude (4,6). The complete curve ideal and a finite degree-reduction
argument force a cubic highest part incompatible with the actual
fourth potential. Zero and nonzero centered quadric levels are retained.

For the remaining (2,3) pair, the
[actual normalization369](research/principal-paraboloid-nonlinear-intercept-linear-coefficient-normalization-pass369-working.md)
gives n=-s^2/(4t^2)+f(t). The
[coefficient gates372](research/principal-paraboloid-quadratic-cubic-leading-coefficient-gates-pass372-working.md)
and [exceptional-case exclusion374](research/principal-paraboloid-quadratic-cubic-zero-leading-gate-exclusion-pass374-working.md)
then force, in the exact finite one-variable coefficient field,

    g=f''/2 != 0,     E=g'/3+g/t != 0.

That remaining nonzero-E family is not yet excluded or recognized.
The new [exact-field reduction376](research/principal-paraboloid-quadratic-cubic-nonzero-leading-normal-form-pass376-working.md)
does force G=H(t)s+G0(t), E=d*t^3*H^4 with d complex nonzero,
and polynomial coefficients in s for sigma. The original field
return then proves L=F(s), removing that finite extension while
retaining the exact finite field F over C(t).
No rationality assumption on the coefficient fields was used to
discard their algebraic elements.

All nine new sources have complete reads and separate AI audits;
their algebraic identities were independently reconstructed in fresh
unsaved computations. No saved checker was executed or rerun in this
pass. The [ledger](research-ledger.md) records exact hashes, review
evidence and remaining gaps. These are working arguments, not recursive
formalization, human-expert certification, or a novelty claim.
The unrestricted conjecture remains unsolved, and the professor has
not confirmed the working interpretation.

## Previous investigation: the affine-in-s first-potential sector is covered

The [working synthesis363](research/principal-paraboloid-first-potential-affine-in-s-recognition-pass363-working.md)
removes an assumption from348. Under every hypothesis of the supplied
actual principal chart264, it gives

    k_s in C*, k_ttt=0, n_ss=0  =>  n_ts=0 and A=C^[3].

There is no extra restriction on ell or n_ttt. The first potential
may initially have coefficients in the exact finite algebraic field;
it is not assumed rational. The proof does not show that arbitrary
cancellation candidates enter this chart or satisfy these derivatives.

The new [reduction361](research/principal-paraboloid-moving-first-slope-affine-line-reduction-pass361-working.md)
exhausts the nonlinear intrinsic-degree patterns when k=s, n_ss=0
and n_ts is nonzero. It leaves two necessary coefficient families.
The [affine-family exclusion360](research/principal-paraboloid-affine-moving-slope-family-exclusion-pass360-working.md)
and [reciprocal-family exclusion362](research/principal-paraboloid-reciprocal-moving-slope-exclusion-pass362-working.md)
exclude both by actual polynomial reframings and the full calibrated
determinant. This forces n_ts=0, after which348 applies. The exact
arbitrary-n normalization in363 extends that conclusion to the three
derivative conditions displayed above.

The saved arguments have complete source reads and separate AI reviews.
Fourteen exact methods passed across the new352,359 and364 controls,
each in its sole execution after complete source and static review.
They check algebraic identities, inverse maps and deliberately wrong
formula controls, not the entire recognition theorem. The
[ledger](research-ledger.md) records hashes, reviews, execution handles,
corrections and retained dependencies. Completed checkers remain frozen.

The subsequent nonlinear investigation has also produced reviewed
reductions, not recognition of that sector.
[366](research/principal-paraboloid-nonlinear-first-constant-sigma-exclusion-pass366-working.md)
excludes constant sigma when k=s and n_ss is nonzero: the full scalar
eventually makes an actual coordinate polynomial a square in its
fraction field, contradicting its prime-factor valuation.
[365](research/principal-paraboloid-nonlinear-intercept-unequal-degree-gate-pass365-working.md)
and [367](research/principal-paraboloid-nonlinear-intercept-geometric-degree-exclusions-pass367-working.md)
bound every intrinsic degree by six and, when theta has larger degree
than sigma, force a reciprocal n_ss and leave only degree pairs
(1,2), (2,3), (4,6). Equal degrees and the reverse inequality are
not covered by that three-pair list.

The unrestricted conjecture remains unsolved. Nonlinear dependence of
n on s, more general k, other initial ideals and arbitrary-chart entry
remain outside the recognition result. These notes are not recursively formalized
or human-expert certified; no novelty or publication claim is made.

## Previous investigation: every supplied one-variable first potential is covered

The new [working synthesis346](research/principal-one-variable-first-potential-recognition-pass346-working.md)
recognizes the entire supplied actual264 sector k=s, n_s=0, with no
additional restriction on ell. The first potential may belong to the
finite algebraic coefficient field; it is not assumed rational or
quadratic. Every hypothesis of that actual polynomial-coordinate chart
is still required. This does not prove that arbitrary candidates enter it.

The proof first settles the full complex-quadratic family in
[344](research/principal-paraboloid-complex-quadratic-family-recognition-pass344-working.md).
Its conic branch has an explicit inverse in the original polynomial ring,
not only in a function field. Separate branches use actual polynomial
derivations or are excluded by the calibrated determinant and the strong
field return. The new
[variable-slope exclusion345](research/principal-one-variable-first-variable-second-slope-exclusion-pass345-working.md)
and 346's cubic argument then remove the restriction that the first
potential was initially quadratic.

Under k=s, n_s=0, the proof also gives the necessary identities
ell_ss=0 and ell_s*n_ttt=0. When ell_s is nonzero, the first potential
is forced to be complex quadratic. When ell_s is zero, the broader
one-variable-pair theorem337 applies directly.

The new [actual normalization348](research/principal-paraboloid-constant-coupling-general-first-normalization-pass348-working.md)
further recognizes every supplied chart satisfying k_s=m0 in C*,
k_ttt=0 and n_ss=n_ts=0. It removes 344's earlier n_ttt restriction
and imposes no condition on ell. These are coefficient gates, not
assumptions established for arbitrary polynomial actions.

The new proofs have complete source reads and separate AI reviews.
Nine new exact methods passed across
[343](research/principal_quadratic_plane_endpoint_controls_pass343.py)
and [347](research/principal_one_variable_first_controls_pass347.py),
each executed once after its full source read and separate static review.
They verify stated algebraic identities and inverse formulas, not all
field arguments or inherited recognition theorems. Exact control status
and full hashes are recorded in the [ledger](research-ledger.md).

The unrestricted conjecture remains unsolved. General coupling and
first potentials, and entry from arbitrary coordinate frames, remain
open. The retained proof dependencies have not been recursively
formalized or human-expert certified. No novelty or publication claim
is made, and the professor has not confirmed the working interpretation.

## Previous investigation: a full one-variable coefficient sector and actual normalizations

The new [recognition337](research/principal-paraboloid-two-one-variable-potentials-recognition-pass337-working.md)
proves the working implication k=s, n_s=ell_s=0 implies A=C^[3],
under every hypothesis of the supplied actual264 chart. The two
potentials may lie in its finite algebraic coefficient field; neither
is assumed rational or polynomial in t. The proof excludes one branch
by actual polynomial divisibility and constructs a preserved polynomial
three-ring in the other. It does not require arbitrary field-valued
coefficients to be polynomial coordinates.

This closes the ell_s=0 part of the nonzero quadratic residual below.
Under334's additional coefficient-family gates,337 also recognizes the
case m0*ell_s+n_s^2=0, regardless of that residual's value. Neither
the coefficient gates nor k=s have been proved for arbitrary candidates.

The new [transport332](research/principal-paraboloid-quadratic-affine-first-potential-transfer-pass332-working.md)
keeps the original polynomial ring and every actual chart hypothesis.
For k=s and n=D*t^2+A*t+B*s+C with complex coefficients, it gives
n*=(D-B^2)*t^2. Thus D=B^2 reaches the working normalized-family
theorem330. The residual does not vanish for general affine n: when
D=0 and B is nonzero, it is -B^2*t^2.

The [composition334](research/principal-paraboloid-complex-quadratic-normalization-composition-pass334-working.md)
extends this to k=m0*s+kappa*t^2/2+b*t+d and
n=(B+kappa/2)*k+D*t^2+A*t+C, all coefficients complex and m0 nonzero.
It supplies the actual polynomial map and inverse, the complete
coefficient transport, and an equivalent derivative-only membership
test. D=B^2 is recognized using330's retained working dependencies.
An additional explicitly stated complex-coefficient condition produces
an original invariant coordinate even when D-B^2 is nonzero.

The remaining nonzero residual has an actual1123 coordinate frame,
but that transfer is not a completed recognition theorem or a strict
decrease in total degree. The [one-variable reduction333](research/principal-paraboloid-one-variable-first-potential-plane-reduction-pass333-working.md)
gives the exact centered potentials for general n=f(t) in the finite
coefficient field, without assuming f rational. For a nonzero complex
quadratic f, it gives either affine intrinsic generators or a constrained
quadratic plane equation, under its stated ell-derivative hypotheses.
Neither remaining alternative is declared recognized. The
[specialization gate336](research/principal-quadratic-first-affine-line-specialization-gate-pass336-working.md)
identifies the affine alternative's1123 full initial ideal as principal;
the previously studied height-two1123 results therefore do not apply
automatically.

332--334,336 and337 have complete source reads and separate AI reviews. The five
new exact identity tests in [335](research/principal_quadratic_normalization_controls_pass335.py)
and three in [338](research/principal_one_variable_pair_controls_pass338.py)
passed in each suite's sole execution, with inverse-map and coefficient-field
denominator restrictions stated explicitly. These finite checks do not
verify the full cancellation theorem, polynomial descent, or all retained
recognition dependencies. The [ledger](research-ledger.md) records the
source hashes, reviews, execution, and outstanding work.

The unrestricted conjecture is still unsolved. Arbitrary-chart entry,
general k,n, and the remaining nonzero-residual branches are still open
in this investigation. No human expert review or novelty claim is made.

## Previous investigation: normalized potentials and reducible surfaces are covered

The [normalized-potential result330](research/principal-paraboloid-normalized-potential-family-recognition-pass330-working.md)
now recognizes every supplied actual principal chart with k=s and n=0,
without an extra restriction on the remaining potential ell. It excludes
all three degree pairs that remained in corrected301's nonlinear sector:
(1,2), (1,4), and (2,4). Together with298 and mandatory-corrected301,
this gives a polynomial three-variable kernel for this subfamily. The new
proof has a complete Root read and separate saved-source AI review.

This is genuine additional coverage within the investigation, not a proof
that a general chart can be normalized to k=s,n=0. A separate coordinate
identity329 turned out to cover an already-settled subcase; its corrected
source and the ledger explicitly record that overlap rather than count
it as another new case.

The [reviewed synthesis324](research/principal-paraboloid-reducible-surface-recognition-synthesis-pass324-working.md)
now covers every reducible monic surface level under the full actual
nonzero-coupling principal-chart hypotheses264. All but one branch are
excluded; the surviving branch gives an original invariant coordinate
and a polynomial three-variable kernel. This is a conditional working
theorem, not a proof that arbitrary candidates enter this chart.

| Reducible sector | Working endpoint |
| --- | --- |
| Formal factor difference constant | Excluded by308 |
| Genuine projected conic | Excluded by323, including both reciprocal cases |
| Projected line, m_s nonzero | Excluded by314/317 |
| Projected line, m_s=0, sigma_v nonzero | Excluded by310/312 |
| Projected line, m_s=0, sigma_v=0 | Original polynomial kernel recognized by313 |

The [polynomial-specialization proof323](research/principal-paraboloid-all-conic-polynomial-specialization-exclusion-pass323-working.md)
excludes the genuine conic remaining in the supplied actual nonzero-coupling
principal chart. Both reciprocal parameter cases are covered. This replaces
the conic coordinate-descent problem in the previous update with a direct
contradiction, under the same retained chart and reducibility hypotheses.

The key step is an exact polynomial-ring equality after adjoining the
coefficient field. At a specific value of the independent coordinate X,
one generator becomes redundant. The remaining quadratic and cubic would
have to generate a one-variable polynomial ring. An elementary even/odd
decomposition proves that they cannot. No coefficient-field coordinate is
asserted to descend to a complex polynomial coordinate.

The complete323 source has three separate AI source reviews. Its four
targeted exact-algebra checks passed in one execution. Six further checks
passed for the auxiliary conic calculations321. Eight further checks across
328 and331 cover the broader specialization identities, their insufficiency
control, and330's three quartic exclusions. Each suite was executed once
after a complete source read. These are written proofs and finite algebra
checks, not human expert certification or proof-assistant
verification. The [ledger](research-ledger.md) records hashes and execution
boundaries, including which results do not depend on those computations.

The separate [all-specializations argument325](research/principal-paraboloid-all-specializations-affine-line-profile-pass325-working.md)
extends the ring equality beyond reducible surfaces. Its reviewed consequence
excludes the intrinsic degree profile (2,1,at most 1) and bounds the birational
projected-line case by affine functions. The
[differential and divided-difference result326](research/principal-paraboloid-all-specializations-differential-obstruction-pass326-working.md)
gives an exact squarefree gcd restriction and simultaneous no-collision
identities. Both sources have complete Root and separate AI reviews.
Neither is an original-ring recognition result.

The unrestricted cancellation problem remains unsolved. Irreducible surfaces
outside the covered normalized family and entry from arbitrary coordinates
still require arguments. In particular, all-X generation
alone is insufficient: a formal family can satisfy it while failing the full
calibrated Jacobian. No publication, external contact, novelty clearance or
human expert review has occurred.

## Previous investigation: all reducible projected lines are settled in the supplied chart

The [variable-coupling exclusion317](research/principal-paraboloid-variable-coupling-line-exclusion-pass317-working.md)
rules out the remaining projected-line branch with m_s nonzero. Its full
lower-coefficient calculation retains every algebraic-field integration
constant until the equations force complex coefficients. The unit factor
difference leaves exactly two line directions. For each direction, both
possible selected factors contradict the original calibrated determinant.
Constant h and the other quadratic degenerations are included.

Together with312 and313, this settles every reducible projected-line case
under the retained actual principal-chart hypotheses. It does not settle
every reducible surface or prove entry into this chart.

| Reducible sector in the supplied nonzero-coupling chart | Current working conclusion |
| --- | --- |
| Projected line, m_s=0, sigma_v=0 | Original kernel recognized by313 |
| Projected line, m_s=0, sigma_v nonzero | Excluded by310+312 |
| Projected line, m_s nonzero | Excluded by314+317, both directions and selections |
| Genuine conic | Exact generic polynomial plane by315+316+318; original-ring descent remains |

For the conic, [scalar rigidity316](research/principal-paraboloid-conic-factor-unit-scalar-rigidity-pass316-working.md)
proves eta and the restricted fourth-gradient coefficient belong to the
exact curve field F, and L=F(s). Its full scalar retains the derivative
of eta and forces (eta/m)' nonzero. The
[original-slice consequence318](research/principal-paraboloid-conic-original-slice-speed-pass318-working.md)
then proves a=EX and sigma_v are units of F. Actual derivatives recover
s and sigma, giving F[B]=F[X,s,sigma] and F[A]=F[s,sigma]. These are
equalities after adjoining F, not coordinates over the complex numbers.
The actual commuting auxiliary derivation also has a proved low-degree
profile, including its distinct d=0 case.

All three new sources have complete Root reads and separate AI reviews.
Nine new exact methods passed across two standalone suites, each executed
once after a full final-source read. The [ledger](research-ledger.md)
records the exact sources, checks and their scope. These checks verify
algebra, not all field arguments or a formal proof-assistant theorem.

The full cancellation conjecture remains unsolved. Conic coordinate
descent, irreducible surfaces, and arbitrary entry into this supplied chart
remain. Separate319 and later endpoint investigations are outside this
reviewed packet. No human expert certification, novelty clearance, public
posting or external contact has occurred. The earlier double-cover
result303+307 is unchanged.

## Previous investigation: a line endpoint and two sharper remaining reductions

The [constant-sigma recognition313](research/principal-paraboloid-constant-sigma-reducible-line-recognition-pass313-working.md)
reaches an actual invariant coordinate and then the original polynomial
kernel, under its full retained chart assumptions. Its auxiliary derivation
has an actual polynomial three-ring kernel preserved by the original E.
A primitive restriction satisfies Daigle's degree-one-coordinate theorem;
the original slice supplies the regularity needed for the published final
kernel theorem. No slice of the auxiliary or restricted derivation is assumed.

Together with312, this settles the m_s=0 projected-line cases within the
reducible principal-chart sector. The other new results are reductions,
not recognition:

| Reducible sector in the supplied chart | Current working conclusion |
| --- | --- |
| Projected line, m_s=0, sigma_v=0 | Original kernel recognized by313 |
| Projected line, m_s=0, sigma_v nonzero | Excluded by310+312 |
| Projected line, m_s nonzero | Actual normal form k^2=2h(t)s, with h a nonzero complex polynomial of degree at most two, by314 |
| Genuine conic | Affine-selected reciprocal coupling306; polynomial coefficient bounds and exact field return L=F(s,eta) by315 |

The [variable-coupling reduction314](research/principal-paraboloid-variable-coupling-hodograph-reduction-pass314-working.md)
keeps both line directions and every degree of h, including constant h.
Its actual coordinate changes have explicit polynomial inverses, and
preserve the full initial relation, selected derivation, strong return and
formal surface level. The
[conic coefficient return315](research/principal-paraboloid-conic-polynomial-coefficient-return-pass315-working.md)
bounds k,n,ell in degrees one,two,three in s over an exact curve field.
It does not establish integrality of eta or normalization of the actual ring.

All three working sources have complete Root and separate AI source reviews.
Ten new exact controls passed in two sole executions after full source reads.
They check algebraic identities and actual inverse maps, not the universal
field or published-theorem arguments. The [ledger](research-ledger.md)
records source hashes, reviews and execution evidence.

The full cancellation conjecture remains unsolved. The conic and
variable-coupling line cases still need endpoints, irreducible surfaces
remain, and arbitrary entry into the supplied principal chart is unproved.
Separate316 and317 investigations are not included in this reviewed packet.
No human expert certification, formal verification or novelty clearance
has occurred. The earlier double-cover result303+307 is unchanged.

## Previous investigation: a conductor obstruction excludes a remaining line branch

The [new conductor exclusion312](research/principal-paraboloid-legendre-conductor-exclusion-pass312-working.md)
rules out the reducible projected-line branch with sigma_v nonzero and
m_s=0, under the full actual principal-chart hypotheses264. This is a
working proof of an exclusion, not just a failure of one attempted method.

The [Legendre reduction310](research/principal-paraboloid-line-legendre-field-reduction-pass310-working.md)
first identifies an exact curve field and a finite polynomial normalization.
Its rational coordinate formulas have genuine denominators, so they do not
meet266's polynomial-entry criterion. Instead312 computes the conductor,
the ideal that measures this normalization's failure to equal the original
curve-field ring. The actual locally nilpotent derivation must preserve
that principal ideal, forcing its generator to be invariant. Its literal
derivative has a nonzero coefficient, giving a contradiction. The proof
does not assume that the curve-field ring is normal or that its coordinates
descend to polynomial coordinates over the complex numbers.

Both sources have complete Root reads and independent AI reviews. The
[new standalone checker](research/principal_line_legendre_conductor_controls_pass312.py)
passed all six methods in its sole execution after a complete source read.
It checks the full map, scalar, module arithmetic and contradiction identity;
the exact-field and conductor arguments remain written proofs, not formal
proof-assistant verification. No human expert review or novelty clearance
has occurred. See the [ledger](research-ledger.md) for hashes and evidence.

The full cancellation conjecture remains unsolved. Other projected-line
directions, the reciprocal conic case, irreducible surface cases, and the
reduction from arbitrary coordinates to this supplied chart remain open
within this investigation. The separate313 investigation is not part of
this reviewed packet. The earlier double-cover result303+307 is unchanged.

## Previous investigation: actual coordinates and a narrower coupled frontier

The [completed double-cover argument307](research/principal-paraboloid-constant-sigma-double-cover-recognition-pass307-working.md),
together with [303](research/principal-paraboloid-double-cover-line-obstruction-pass303-working.md),
now recognizes the entire degree-two projection branch of the supplied
principal chart. The remaining constant-sigma case has polynomial entry
over an invariant curve field in an actual coordinate frame, allowing
the retained266 criterion to apply. No slice is assumed for the auxiliary
derivation. The separate zero-remainder case uses303's projection-free
invariant family and its impossible square degeneration.

The [reducible-surface bound302](research/principal-paraboloid-reducible-surface-conic-reduction-pass302-working.md)
reduces that sector to a projected line or conic, with all three intrinsic
generators of degree at most two. Combining its actual normalization with
the projection-free family identity gives the
[constant-factor-difference exclusion308](research/principal-paraboloid-constant-factor-difference-exclusion-pass308-working.md).
[306](research/principal-paraboloid-selected-conic-factor-rigidity-pass306-working.md)
now proves that a conic must select the affine factor; selection of the
quadratic factor is impossible. Its coupling has the exact reciprocal
form m=d+c/(t-tau), with complex constants and c nonzero, strengthening
[305](research/principal-paraboloid-affine-selected-conic-coupling-pass305-working.md).
This is not an ambient coordinate substitution.
The [projected-line refinement309](research/principal-paraboloid-reducible-line-affine-generators-pass309-working.md)
makes all three intrinsic generators affine in that remaining line case.

The special k=s,n=0 sector also advances. The original
[301](research/principal-paraboloid-affine-second-potential-reduction-pass301-working.md)
contains an incorrect fixed-Y assertion in Section3 and must not be used
alone. The separately preserved
[correction](research/principal-paraboloid-affine-second-potential-pass301-correction-working.md)
withdraws that argument and replaces it with a direct scalar contradiction.
The corrected pair gives recognition when ell_s is nonzero and ell_ss=0,
subject to its explicitly retained1122 recognition input257. The quartic
sector remains open.

Twenty-four finite exact methods passed across six newly executed standalone
suites301,302,303,305,306,307_v2. Each source was read in full before its
sole run. The original307 suite was interrupted during an expensive first
method and is not counted as passed; the standalone v2 checks the same
identity after cancellations, with an additional affine-support check.
The working proofs have separate AI reviews; these are not formal proofs,
human expert certification, or novelty clearance. The
[source screen304](research/targeted-cancellation-source-screen-pass304-working.md)
records why a purported general shortcut from one preprint was rejected.

The unrestricted cancellation goal remains active and unsolved. The
birational projection branch remains, including the newly narrowed
reducible line/conic cases. This entire frontier still assumes the specified
actual principal chart; arbitrary-coordinate entry is not proved. Separate
310 exploratory work is not included in this reviewed packet.

## Previous investigation: bounded degree in the coupled principal chart

The [fourth-potential result296](research/principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md)
uses the previously unused linear Jacobian coefficient in the actual
nonzero-coupling branch of264. It gives a quartic polynomial level,
and the full scalar determinant makes its gradient independent of
the cubic level's gradient along the whole generic line.

The [degree bound299](research/principal-paraboloid-generic-degree-bound-pass299-working.md)
then proves that each of y, sigma and theta has degree at most12
in the intrinsic line variable. Its gcd and dimension-count proof
does not assume the two equations generate the full curve ideal.
The [plane refinement300](research/principal-paraboloid-plane-degree-refinement-pass300-working.md)
gives plane degree at most10. If the cubic level factors, the plane
functions genuinely generate the line ring and the plane degree is
at most4, or at most2 when the two factors' difference is nonconstant.

The [double-projection reduction295](research/principal-paraboloid-double-projection-line-reduction-pass295-working.md)
is stronger in its own case: every degree-two projection has a
linear plane image. Its two projected functions have degree at most2
and its first function has degree at most4. This does not recognize
the remaining double-cover lines or eliminate the birational case.

There is also an actual coordinate endpoint for the explicitly
special family k=s, n=0, ell_s=0. The
[one-variable argument298](research/principal-paraboloid-one-variable-potential-recognition-pass298-working.md)
uses the full scalar and exact field return to exclude its nonlinear
potential when y is nonconstant. The
[explicit polynomial map297](research/principal-paraboloid-nagata-degree-lowering-pass297-working.md)
handles the remaining affine potential, subject to the retained
three-good recognition theorem156. Arbitrary coefficients have not
been normalized to this special family.

Twenty-two exact algebra methods passed across six new standalone
suites, each executed once after Root read its final saved source.
All six proof notes have separate AI source reviews. These are
working proofs and algebra controls, not human expert review,
formal proof verification or historical novelty clearance.
The unrestricted conjecture remains unsolved. In particular the
degree bound is internal to the supplied principal chart; it is
not a bound on arbitrary coordinate profiles or on coefficient
functions in t,s. The ledger records exact inputs and execution evidence.

## Previous investigation: the zero-coupling part of one supplied principal chart

The [complete branch synthesis294](research/principal-paraboloid-nonconstant-intercept-recognition-synthesis-pass294-working.md)
now covers every selected plane component in the actual branch271,
including the previously remaining lines. The new
[constant-slope endpoint291](research/principal-paraboloid-constant-slope-line-recognition-pass291-working.md),
[moving-line endpoint292](research/principal-paraboloid-moving-line-pencil-recognition-pass292-working.md),
and [constant-first exclusion293](research/principal-paraboloid-constant-first-nonconstant-slope-exclusion-pass293-working.md)
complete that case split after the [line reduction288](research/principal-paraboloid-projected-line-polynomial-reduction-pass288-working.md).

Precisely,294 recognizes the supplied principal chart with
`k_s=0, n_s!=0`. The retained [268](research/principal-paraboloid-zero-coupling-recognition-pass268-working.md)
separately recognizes `k_s=n_s=0`. Together these working arguments
cover `k_s=0` in that specified chart, not all principal charts,
all exact1222 frames, or unrestricted cancellation.

For the other branch, `k_s!=0`, the [projection result290](research/principal-paraboloid-nonzero-coupling-projection-pass290-working.md)
gives new constraints but no recognition theorem. Its explicit
countercontrol satisfies the potential and intercept-return conditions
yet fails the full Jacobian equation. It rules out a shortcut; it is
not a counterexample to cancellation.

Fourteen new finite algebra checks passed across five standalone suites.
The proofs have separate AI source reviews with their exact scope
recorded in the ledger. Neither these checks nor those reviews are
human peer review, formal proof verification, or novelty clearance.
The unrestricted conjecture remains unsolved, with arbitrary-coordinate
entry still unproved.

## Previous investigation: all nonlinear components of one supplied principal branch

The [nonlinear synthesis289](research/principal-paraboloid-nonlinear-recognition-synthesis-pass289-working.md)
now covers every nonlinear selected plane component in the supplied
principal branch271. Its exhaustive degree split uses the corrected
quartic arguments below and the two remaining conic endpoints
[286](research/principal-paraboloid-quadratic-conic-recognition-pass286-working.md)
and [287](research/principal-paraboloid-quartic-selected-conic-recognition-pass287-working.md).
This is a conditional working recognition theorem, not recognition of
all principal charts, all1222 frames, or unrestricted cancellation.

Both genuine quartic components in the specified principal branch271 now
have scoped working endpoints. The [corrected exact-field reduction281](research/principal-paraboloid-quartic-exact-field-reduction-pass281-working.md)
retains a factor-of-two correction found during separate review. Its
[constant-p branch284](research/principal-paraboloid-constant-p-quartic-exclusion-pass284-working.md)
is impossible: an explicitly derived degree-four polynomial is irreducible
over the actual returned field but would have a root in that field.
The [nonconstant-p branch285](research/principal-paraboloid-nonzero-p-derivative-quartic-recognition-pass285-working.md)
reduces the actual derivation to a polynomial three-ring with a coordinate
of time degree one, allowing the published preslice recognition theorem.

The [constant-second-projection endpoint278](research/principal-paraboloid-constant-second-line-recognition-pass278-working.md)
constructs an explicit invariant coordinate. Separately,
[283](research/principal-paraboloid-cubic-and-degenerate-conic-pass283-working.md)
excludes selected cubics and recognizes one degree-two conic case by
an explicit degree-lowering shear. Together286/287 close its remaining
conic alternatives. Projected lines are still being investigated; the
whole principal branch is not claimed.

The working sources and the exhaustive composition have complete separate
AI source reviews. Nineteen new finite algebra checks passed, including
a raw determinant that rejects281's former coefficient. These are not
human review, formal verification, or novelty clearance. The unrestricted
conjecture remains unsolved.

## Previous investigation: one complete supplied chart and a stronger principal reduction

The [chart synthesis282](research/nonzero-coupling-quadratic-cubic-recognition-pass282-working.md)
now gives a working recognition proof for the entire supplied
nonzero-coupling chart263, including its previously remaining lower-degree
components. The [conic obstruction279](research/quadratic-cubic-selected-conic-square-obstruction-pass279-working.md)
excludes its genuine conic configuration. In the remaining zero-leading-
coefficient case, an explicit polynomial change of the original coordinates
lowers the cubic coordinate to time degree at most two, where retained
recognition results apply. This does not cover all1123 frames or arbitrary
coordinate entry.

For the separate principal1222 branch,
[280](research/principal-paraboloid-nonlinear-constant-slope-pass280-working.md)
forces a complex constant slope and affine auxiliary potential whenever
the selected plane relation is nonlinear. It also gives exact differential
constraints for the genuine quartic case. That branch remains unresolved.

These arguments have separate complete AI source reviews. Eight new finite
algebra checks passed across279,280,282; they verify specified identities,
not the universal proof or its entire dependency chain. New drafts278 and281
are under review and are not included in these completed claims.
The full conjecture remains unsolved, with no human expert review, formal
certification, or established novelty.

## Previous investigation: the second genuine quartic endpoint and a parameter restriction

The [quadratic-first quartic endpoint276](research/quadratic-first-quartic-actual-coordinate-recognition-pass276-working.md)
constructs two invariant actual polynomial coordinates in the specified
maximal-pivot1123 chart. The exact reductions
[270](research/quadratic-cubic-quadratic-first-field-boundary-pass270-working.md),
[273](research/quadratic-first-full-potential-discriminant-reduction-pass273-working.md)
and [274](research/quadratic-first-complex-potential-rigidity-pass274-working.md)
remove the coefficient-field obstruction. Strong actual field return then
rules out a quadratic dependence in one potential. The proof transports
the resulting identities through the entire original coordinate expansion
and supplies both polynomial inverse orders. Together with267, this closes
both genuine degree-four projected shapes under263's actual assumptions.
Lower-degree selected components and other1123 charts remain open.

For the nonconstant-intercept principal1222 branch,
[271](research/principal-paraboloid-nonconstant-intercept-plane-reduction-pass271-working.md)
gives a sextic plane relation with an evaluated unit cofactor.
The [actual normalization272](research/principal-paraboloid-high-derivative-line-normalization-pass272-working.md)
and [canonical-line endpoint275](research/principal-paraboloid-canonical-line-recognition-pass275-working.md)
exclude its nonzero third-parameter-derivative mode. The latter also gives
an explicit actual shear to a recognized exact1122 frame on its canonical line.
The new [affine-parameter restriction277](research/principal-paraboloid-affine-parameter-restriction-pass277-working.md)
goes further: throughout271, H is affine in n over the exact curve field.
Its proof excludes the remaining quadratic dependence using top-factor
multiplicities, a parabola coefficient, moving-line compatibility and the
nonzero actual determinant. The resulting affine family is not yet recognized.

These are scoped working proofs with separate complete AI source reviews,
not human peer review, proof-assistant certification or historical novelty
clearance. The unrestricted conjecture remains unsolved. In particular,
neither complete sum-seven profile nor an arbitrary-coordinate entry theorem
has been established. The ledger records exact source hashes and the finite
checkers' separate, limited scope.

## Previous investigation: two restricted recognition endpoints

The [quartic-graph endpoint267](research/quadratic-cubic-quartic-graph-polynomial-entry-pass267-working.md)
now recognizes the genuine affine-first quartic component of the supplied
maximal-pivot1123 chart. An actual complex-coefficient shear, followed by
the scalar and full determinant identities, proves polynomial entry over
an invariant curve field. The quadratic-first quartic and lower-degree
components are not covered.

The [paraboloid endpoint268](research/principal-paraboloid-zero-coupling-recognition-pass268-working.md)
recognizes the subcase k_s=n_s=0 of the supplied principal1222 chart.
Its actual field return makes a nonzero block-Jacobian factorization
available. This forces the first two intercepts to be fixed by an
auxiliary derivation and produces an actual invariant coordinate.
The other coupling branches remain open.

The [curve-field criterion266](research/curve-field-polynomial-entry-criterion-pass266-working.md)
proves cancellation if an actual coordinate is polynomial in the other
three over a one-variable invariant field. It has no time-degree bound.
The condition itself is not proved in general. An explicit sliced example
shows why replacing polynomial membership by rational membership does not
justify the same invariant-coordinate construction.

In the [coupled quadratic-cubic chart263](research/two-affine-quadratic-cubic-whole-plane-cofactor-pass263-working.md),
the selected plane component has a unit evaluated cofactor, including when
the displayed quartic is reducible. This forces the coupling derivative
to vanish and recognizes the constant-first-projection case. Its two
genuine quartic shapes and lower-degree components were retained explicitly;
267 now closes only the affine-first genuine quartic shape.

The [principal paraboloid chart264](research/principal-one-affine-paraboloid-chart-pass264-working.md)
gives exact potentials and a monic quadratic cubic-surface relation in a
supplied1222 sector. Three projected generators still need not reduce to
two; this relation alone does not recognize that sector. The new268
instead handles the separate zero-coupling, scalar-intercept subcase.

The [rational-entry clarification269](research/curve-field-rational-entry-equivalence-pass269-working.md)
identifies rational curve-field entry with an invariant linear in one
actual coordinate, whose leading coefficient need not be a unit.
An additional invariant Bezout identity is sufficient for recognition;
its existence is not automatic.

The new263,264,266,267,268 standalone suites passed eighteen finite algebra methods.
Complete written-source AI reviews support the scoped arguments, not
unrestricted cancellation, historical novelty or human certification.
The full conjecture remains unsolved. The ledger records the exact scope
and the sole execution of each new suite.

## Previous investigation: restricted sum-seven cases and an arbitrary-degree rank test

The [one-affine/three-quadratic argument259](research/one-affine-three-quadratic-frontier-pass259-working.md)
recognizes the supplied exact1222 profile when a selected bad partial has
shift zero or all three have shift one. The latter proof reconstructs
an exact localized polynomial ring and uses its unit Jacobian to force
a genuine degree-lowering shear. The remaining higher-shift cases have
proportional intrinsic leading actions and are not recognized.

The [two-affine quadratic-cubic chart258](research/two-affine-quadratic-cubic-frontier-pass258-working.md)
reduces one maximal-pivot height-two1123 case to a nonzero quartic
polynomial-line relation or an affine graph.
The [new graph endpoint262](research/two-affine-quadratic-cubic-graph-pencil-pass262-working.md)
closes its nonzero-scalar affine graph, including the old square-root
mode, by an exact parameter change and an actual invariant polynomial
coordinate. Together with258's zero-scalar endpoint and the retained
degree-lowering gate, this recognizes the zero-coupling branch of that
specified maximal-pivot chart. The nonzero-coupling quartic, principal
initial ideals and lower selected shifts remain unresolved.

The [horizontal-minor criterion261](research/horizontal-triple-minor-rank-criterion-pass261-working.md)
works at arbitrary positive coordinate time degrees. It gives an exact
equality test for three independent commuting intrinsic actions, which
would recognize the kernel. Actual polynomial examples show that the
test can fail in every triple, so it is not an arbitrary-entry theorem.

An [independent chain audit260](research/three-good-chain-independent-audit-pass260-working.md)
reconstructs the stated long-chain obstruction and gives a sharp
formal-chart countercontrol: whole-line return and a unit Jacobian do
not imply the actual rational-field return needed by the proof.
The five new standalone algebra suites258--262 passed all eighteen
methods. They check identities and explicit controls, not universal
field descent, the full retained dependency chain, or cancellation.

These are working mathematical results with separate complete AI
source reviews, not human expert or proof-assistant certification.
The unrestricted conjecture remains unsolved. There is no upper bound
on the minimum coordinate time degree, historical novelty clearance,
or publication claim. The ledger records exact remaining gaps.

## Previous investigation: a working proof for the entire supplied exact1122 sector

The [new synthesis257](research/full-exact1122-recognition-synthesis-pass257-working.md)
combines the retained height-one arguments with new height-two
endpoints. Subject to those working proof dependencies, it recognizes
every globally sliced complex polynomial four-ring supplied with an
actual coordinate frame of time degrees \((1,1,2,2)\).
There is no additional height-one assumption.

The height-two argument uses the actual coordinate partials and
their exact shifts. Shift zero is handled by249; the pair \((1,1)\)
by253--254; a shift two by250,252 and the new
[reciprocal normalization255](research/height-two-graph-reciprocal-normalization-pass255-working.md)
and [explicit-coordinate endpoint256](research/height-two-canonical-cubic-pencil-recognition-pass256-working.md).
The last endpoint constructs an invariant polynomial coordinate
with a polynomial inverse. Its curve-field parameter is not
assumed to be an ambient coordinate.

The latest two independent algebra suites passed all nine methods.
Their scope is polynomial identities, determinant calculations,
inverse maps and negative controls, not the universal geometric
proofs. The new proof sources and exhaustive composition have
separate complete AI source reviews. This is not recursive formal
verification of every retained historical dependency.

With the retained three-good theorem156,257 raises the necessary
minimum coordinate time-degree sum for a hypothetical counterexample
to seven. The next sorted profiles at that sum are \((1,1,2,3)\)
and \((1,2,2,2)\). No theorem recognizing those profiles, upper bound
on the minimum, or route from arbitrary coordinates is claimed.

The unrestricted cancellation conjecture remains unsolved. There
is no human expert review, proof-assistant certification, historical
novelty clearance or publication claim. The ledger records precise
assumptions, hashes, reviews and finite execution results.

## Previous investigation: the full height-one exact1122 sector is recognized

The [new synthesis248](research/full-height-one-exact1122-recognition-pass248-working.md)
recognizes every supplied globally sliced exact1122 frame whose
entire generated initial kernel has height one. The initial-bound
theorem157 limits its irreducible relation to weights two, three
or four. The retained weight-two and cubic theorems cover the
first two;194 and the new247 together cover every weight-four
quadratic rank.

The last repeated-root pair is excluded by the
[conductor/trace proof246](research/cubic-repeated-root-four-six-conductor-trace-exclusion-pass246-working.md).
The independent four-method algebra suite246 passed its sole
canonical run. The [positive-rank synthesis247](research/positive-bad-quadratic-recognition-synthesis-pass247-working.md)
and full248 composition have complete saved-source AI reviews.
These do not recursively certify every historical dependency.

Within a supplied exact1122 frame, the remaining possible
nonpolynomial-kernel case has a height-two initial ideal.
Its leading-ratio field has transcendence degree one, and both
selected bad-coordinate shifts are at most two.
The [actual examples212](research/height-two-no-quadratic-relation-actual-control-pass212-working.md)
prevent assuming a quadratic relation or a uniform bound on all
initial-ideal generators. New work is addressing this lower-shift
structure, not reopening the completed principal-kernel cases.

The unrestricted cancellation conjecture remains unsolved. No
arbitrary-frame entry, height-two recognition or higher-profile
theorem is claimed. There is no human expert review, formal proof
certification, historical novelty clearance or publication claim.
The ledger records exact scopes, hashes, reviews and finite checks.

## Previous investigation: one projected degree pair remained in the cubic model

The [quartic exclusion241](research/repeated-root-quartic-conic-exclusion-pass241-working.md)
excludes the supplied full initial kernel
\(Z^2-X^2W-Y^4\). It combines the
[rebuilt-chart boundary proof237](research/repeated-root-rebuilt-chart-line-exclusion-pass237-working.md),
the [local cofactor bound238](research/repeated-root-return-excess-order-bound-pass238-working.md),
and the [complete centered identities239](research/radical-minus-polynomial-centered-eliminant-pass239-working.md).
The last quadratic graph forces incompatible coefficient derivatives.

For the separate cubic model \(Z^2-X^2W-XY^3\), the
[degree frontier240](research/cubic-repeated-root-projection-frontier-pass240-working.md)
excludes pairs \((2,4),(2,5)\). The
[quadratic graph242](research/repeated-root-cubic-conic-exclusion-pass242-working.md),
[trace obstruction243](research/cubic-repeated-root-three-six-trace-exclusion-pass243-working.md),
[original-ring square obstruction244](research/repeated-root-cubic-graph-square-obstruction-pass244-working.md),
and [parity-conductor obstruction245](research/cubic-repeated-root-two-three-conductor-exclusion-pass245-working.md)
remove \((1,2),(3,6),(1,3),(2,3)\), respectively.
Only
\[
(\deg_vy,\deg_v\theta)=(4,6)
\]
remains within this supplied cubic chart. A possible conductor/trace
approach to it is under investigation, not an established endpoint.

These are working written proofs under the supplied globally sliced
exact1122, full-principal-initial-kernel hypotheses. The algebra
suites239,241,242 passed their sole canonical runs. Other new finite
controls are recorded separately as they complete. The proof reviews
are AI reviews, not human expert review or proof-assistant certification.
No novelty clearance or unrestricted cancellation solution is claimed.

## Previous investigation: two rank-one residual models remained

The [distinct-root residue proof236](research/rank-one-distinct-root-residue-exclusion-pass236-working.md)
excludes the nonzero-residue deformations of the product-radical
kernel, using the [sextic and line reduction235](research/rank-one-distinct-root-residue-sextic-line-reduction-pass235-working.md).
Zero return is ruled out by a nonzero cubic coefficient; the remaining
lines force incompatible original-ring derivation identities.

Together with the previously classified normal forms and retained
recognition results, only these two models remain in the supplied
rank-one bad-quadratic, principal-weight-four, exact1122 class:

\[
Z^2-X^2W-XY^3,\qquad Z^2-X^2W-Y^4.
\]

The [four-model synthesis234](research/rank-one-bad-quadratic-four-model-frontier-pass234-working.md)
records the actual coordinate normalizations;236 removes its first
two models. This is a restricted remaining list, not an entry theorem
for arbitrary cancellation instances. The full conjecture is unsolved,
and the working results lack human expert review, formal verification
and novelty clearance.
The separate235 and236 algebra suites each passed four methods once.

## Previous investigation: the supplied product-radical sector is excluded

The [final conic proof233](research/product-radical-conic-final-exclusion-pass233-working.md)
closes the remaining conic for the precise supplied full initial
kernel \((Z^2-XYW)\). Its lower coefficient equations force a complete
constant-coefficient parametrization. That parametrization imposes
an explicit nonzero polynomial relation among the original four
coordinates, contradicting their algebraic independence.

Together with227--232, this excludes that entire supplied globally
sliced exact1122 configuration. It is an impossibility theorem for
a restricted hypothesis class, not a new nonempty family of solved
cancellation examples. Independent raw reconstructions agree on
both the polynomial relation and the vanishing of the full final
Jacobian. Complete-source reviews and finite-control evidence are
recorded in the [ledger](research-ledger.md).
The standalone final-conic233 suite passed all six methods in its
sole canonical run.

Other initial-kernel sectors, arbitrary frame entry and higher
profiles remain unresolved. The full cancellation conjecture is
still unsolved. These are AI-reviewed working arguments, without
human expert review, proof-assistant certification or novelty clearance.

## Previous investigation: the supplied nondegenerate bad-quadratic sector is recognized

The [strict cofactor obstruction225](research/rank-two-strict-return-cofactor-obstruction-pass225-working.md)
excludes the last cubic case in the triple-plus-simple root pattern.
The earlier bound allowed an evaluated cofactor to equal a scalar times
the return polynomial cubed. The full differentiated equations now force
a strict loss at every return root, contradicting that equality.
This handles cusps and smooth projected cubics together.

The new [recognition synthesis226](research/nondegenerate-bad-quadratic-recognition-synthesis-pass226-working.md)
combines this with the retained exclusions and fourth-power theorem216.
It covers every supplied globally sliced exact1122 frame with a full
principal weight-four initial kernel and nondegenerate quadratic part
in the two degree-two slots. Actual homogeneous coordinate changes reduce
that entire sector to the recognized fourth-power case.

This is a restricted working theorem, not the full cancellation conjecture.
No nonempty new example family or historical novelty is claimed.
Arbitrary frame entry, other initial-kernel sectors and higher profiles
remain unresolved. The new argument has separate AI reconstructions,
not human expert review or proof-assistant certification.

## Product-radical proof chain

For the separate supplied full kernel \((Z^2-XYW)\), the
[new sextic pruning227](research/rank-one-product-radical-sextic-pruning-pass227-working.md)
leaves only two lines and one conic in its nonzero-return chart.
The [constant-first-line proof228](research/rank-one-product-radical-constant-first-line-exclusion-pass228-working.md)
excludes one line, and the [zero-return proof229](research/rank-one-product-radical-zero-return-exclusion-pass229-working.md)
excludes the omitted identically-zero return branch.
The [constant-return-line proof230](research/rank-one-product-radical-constant-return-line-exclusion-pass230-working.md)
excludes the other line using a literal scalar-Jacobian coefficient
and an actual nice auxiliary derivation. These four notes left only
the conic, now excluded by232--233 above.
The independent227 algebra suite passed four methods once; it does not
cover the original-ring exclusions228--230.
The separate combined228--230 controls have also passed four methods
once, checking their displayed coefficient calculations rather than all
original-ring arguments.

The [simple-return-root theorem231](research/universal-simple-return-root-cofactor-bound-pass231-working.md)
further forces the remaining conic's evaluated cofactor to be a nonzero
scalar times its return polynomial. Its return root cannot be the
critical point of the quadratic first projection. This is the
necessary condition used in both final conic exclusions.

The [square-root-mode exclusion232](research/product-radical-conic-nonzero-square-root-mode-exclusion-pass232-working.md)
now excludes the conic branch with a nonzero algebraic square-root
mode. Its zero mode is carried by an actual interchange of X and Y
to the branch where the projected w has degree at most two.
That lower-degree branch is excluded by233.
The separate simple-root231 controls passed three methods once.
The separate square-root-mode232 controls passed four methods once.

## Previous investigation: only an injective cubic projection remained

The [cofactor exclusion222](research/rank-two-saturated-pair-cofactor-exclusion-pass222-working.md)
also rules out the root pattern consisting of one double root and two
simple roots. It reconstructs a universal divisibility bound and compares
it with the exact degree of the evaluated cofactor. The remaining line
directions are excluded by the actual normalized derivation argument.
This proof also gives an independent squarefree exclusion.

The [triple-root line argument223](research/rank-two-triple-root-constant-second-line-exclusion-pass223-working.md)
and [degree-two pruning223](research/rank-two-triple-root-cubic-frontier-pass223-working.md)
leave only projected cubics in the remaining triple-plus-simple pattern.
The [cubic-fiber obstruction224](research/rank-two-saturated-cubic-fiber-injectivity-pass224-working.md)
then excludes every two-point normalization fiber, including a node.
That note alone does not exclude a cusp or settle a smooth cubic graph;
the stronger225 argument above now does. Injectivity was not treated as
normality or as an original polynomial coordinate.
These written arguments are separate from the completed220/221 packets.

## Previous investigation: squarefree quartics are excluded

The [squarefree exclusion221](research/rank-two-squarefree-quartic-line-exclusion-pass221-working.md)
gives a working proof that no supplied globally sliced exact1122 frame
can have entire initial kernel \((ZW-F_4(X,Y))\) with four distinct
projective roots of \(F_4\).
The [zero-return lemma221](research/rank-two-nonsquare-quartic-zero-return-exclusion-pass221-working.md)
first proves that zero return forces \(F_4\) to be a square.
The six-factor reduction220 then forces a projected line, and an actual
constant coordinate change puts its direction into a normal form.
Wang's precise alternatives for the resulting auxiliary derivation
both lead to contradictions. No coordinate over a coefficient field
is promoted to an original polynomial coordinate.

Within this supplied rank-two quartic family, the current status is:

| Root multiplicities of the binary quartic | Working status |
| --- | --- |
| Four distinct roots | Excluded by221, independently by222 |
| Two double roots | Excluded by220 |
| One quadruple root | Conditional cancellation recognition216 |
| One double root and two simple roots | Excluded by222 |
| One triple root and one simple root | Excluded by225 with the223 frontier |

These are restricted working results with separate AI reviews, not human
expert review, formal verification, or novelty clearance.
Arbitrary frame entry and the full cancellation conjecture remain unresolved.

The separate [verification220](research/verification-pass220-working.json)
and [verification221](research/verification-pass221-working.json) packets
are complete and audited. Their standalone algebra suites passed four
and five methods respectively, once each. The independent222 algebra
suite has now also passed five methods in its sole canonical execution;
its [verification222](research/verification-pass222-working.json) packet
is complete.
It checks the universal gradient/wedge identities and selected algebraic
reductions, not the entire written proofs. It contains no223--226 coverage.
These finite checks do not certify the full conjecture.
The separate [strict cofactor controls225](research/strict_return_cofactor_controls_pass225.py)
also passed three methods once. They check the cancellation identities,
an explicit algebraic root contradiction and assumption-sensitive
countercontrols, not the entire original-ring theorem.

## Previous investigation: the supplied full mixed-quartic configuration is impossible

The [stronger line obstruction220](research/mixed-quartic-line-nonrealizability-pass220-working.md)
rules out the last line branch for a supplied globally sliced exact1122
frame whose entire initial kernel is \((ZW-X^2Y^2)\).
Together with the previous zero-return and conic exclusions, this gives
a working proof that this precise configuration cannot occur.
The earlier recognition statement219 is therefore true with an empty
hypothesis class. It is not a nonempty family of solved cancellation examples.

The new step applies the same original-ring argument twice. It forces
both an auxiliary first derivative and an auxiliary second derivative
to be complex constants, contradicting the transcendence of a leading
ratio. The proof has complete separate AI reviews, but no human expert
review, formal verification, or novelty clearance.

A separate [general quartic reduction220](research/rank-two-binary-quartic-leading-sextic-pass220-working.md)
factors the leading sextic into six root-pair factors. Under its exact
nonzero-return hypothesis, a quartic with four distinct projective roots
has a projected line. That is a reduction, not original-coordinate
recognition or a solution of the general cancellation problem.

## Previous investigation: conditional recognition for the supplied mixed kernel

The [recognition synthesis219](research/mixed-quartic-initial-kernel-recognition-synthesis-pass219-working.md)
now gives a working proof of an actual invariant coordinate and
\(A\simeq\mathbb C^{[3]}\) for a supplied globally sliced exact1122 frame
whose entire initial kernel is \((ZW-X^2Y^2)\).
The [final conic exclusion219](research/mixed-conic-final-jacobian-exclusion-pass219-working.md)
closes the branch left by217. Two lower Jacobian coefficients force
explicit complex-constant formulas. Those formulas impose a nonzero
polynomial relation on the original independent coordinates, a contradiction.
No generic-field variable is promoted to an ambient coordinate.

The preceding218 arguments exclude a zero determinant factor and remove
the possible square-root term using the complete lower potentials.
The independent218 checker passed five methods in0.758 seconds; the
separate219 checker passed three methods in2.034 seconds. Both ran once,
and their original execution handles have completed with exit zero.
Their separate [verification218](research/verification-pass218-working.json)
and [verification219](research/verification-pass219-working.json) packets
are complete and audited. The corresponding checkpoints are
[218](research/checkpoint-pass218-working.json) and
[219](research/checkpoint-pass219-working.json). The stronger220
nonrealizability result is not retroactively included in either packet.

The exact supplied frame and full initial ideal remain essential.
Arbitrary frame entry, other leading kernels, and the full cancellation
conjecture are unresolved. This is a working theorem with AI review and
finite algebra checks, not human expert review, formal verification or
novelty clearance.

## Previous investigation: the mixed quartic case reduces to a conic

For the different supplied full initial kernel \(ZW-X^2Y^2\), the
[projection reduction217](research/rank-two-mixed-ratio-projection-reduction-pass217-working.md)
excludes cubic and quartic projected components. The
[zero-return proof217](research/rank-two-mixed-ratio-zero-return-exclusion-pass217-working.md)
excludes that branch, and the
[line proof217](research/rank-two-mixed-ratio-line-recognition-pass217-working.md)
gives actual original-ring recognition for every remaining line direction.
At217 only the conic remained unresolved within this supplied frame;
its later exclusion is recorded above.

The [conic reduction217](research/rank-two-mixed-ratio-quadratic-graph-reduction-pass217-working.md)
strengthens the cofactor bound and uses an actual coordinate interchange
to make all three projected intercepts at most quadratic. This is not
the square-zero condition needed for a nice-derivation recognition theorem.
The four saved proofs have complete independent AI source reviews.
Their separate five-method finite checker passed its sole canonical run
(0.611 seconds). [Verification217](research/verification-pass217-working.json)
and [checkpoint217](research/checkpoint-pass217-working.json) are complete:
68 tagged equations, five methods, and 1,338 chained records.

Further [radial leading-coefficient work218](research/mixed-conic-radial-constant-leading-ratios-pass218-working.md)
is separate from217. The [next Jacobian coefficient218](research/mixed-conic-next-jacobian-constant-pass218-working.md)
forces one radial constant to be a nonzero complex constant. Both notes
retain the exact coefficient field and supply necessary constraints,
not a conic recognition theorem by themselves. Their later completion
is recorded above. Arbitrary frame entry and the full cancellation
conjecture remain unresolved.

## Previous investigation: recognition for the supplied Y-independent quartic sector

The [recognition synthesis216](research/rank-two-initial-kernel-recognition-synthesis-pass216-working.md)
gives a working proof of cancellation for a supplied globally sliced
exact1122 frame whose entire initial kernel is generated by an irreducible
weight-four polynomial independent of the second good coordinate.
It also covers dependence on just one complex linear combination of the
two good coordinates. Actual weighted normal forms reduce this sector to
the radical case211 or the rank-two case completed here. Each changed
frame gets a fresh chart; preservation of an old auxiliary derivation
is not assumed.

The [new endpoint216](research/rank-two-normalized-linear-center-wang-exclusion-pass216-working.md)
excludes the last nonconstant-second-projection case in the supplied
exact1122 frame with full initial kernel \((ZW-X^4)\).
It uses Wang's classification only over \(\mathbb C(X)\), then makes
an actual constant translation of \(X\). The resulting projected
generators contradict the previously proved whole-line equality.
No coefficient-field parameter is promoted to an ambient coordinate.

The route includes [high-degree exclusions214](research/rank-two-affine-second-high-degree-exclusion-pass214-working.md),
two quadratic-center exclusions in215, and an
[actual reduction of the last linear center](research/rank-two-linear-center-affine-reduction-pass215-working.md).
Their full source reviews and finite algebra checks are recorded below
and in the ledger. The recognition synthesis and its216 packet are complete.

[Packet213](research/checkpoint-pass213-working.json) is complete:
20 equations, four methods, one passing run (0.116 seconds), and1,314
chained records. [Packet214](research/checkpoint-pass214-working.json)
is complete:49 equations, five methods, one passing run (0.450 seconds),
and1,320 records. [Packet215](research/checkpoint-pass215-working.json)
is complete with37 equations, four methods, one passing run
(0.172 seconds), and1,326 records. [Verification216](research/verification-pass216-working.json)
and [checkpoint216](research/checkpoint-pass216-working.json) record29 equations,
four methods in one passing run (0.282 seconds), and1,331 records.
No later pass is retroactively included in an earlier packet.

This is progress within a restricted supplied frame, not a solution
of the full cancellation conjecture. Arbitrary frame entry and other
leading kernels remain unresolved. There is no human expert review,
formal verification, or novelty clearance.

## Previous investigation: an entry shortcut fails, and another center is excluded

The [actual height-two family212](research/height-two-no-quadratic-relation-actual-control-pass212-working.md)
has fixed E-time degrees \((1,1,2,2)\), but the first relation
outside its initial cubic ideal has weight \(\lceil2n/3\rceil\),
which is unbounded. This rules out a uniform bounded-weight
classification of the entire height-two initial ideal as a general
entry argument. Every member still has an invariant coordinate of
weight three. These are known polynomial translations, not
cancellation counterexamples or minimum-degree frames.

For the different full initial kernel \((ZW-X^4)\), the
[rank-two reduction212](research/rank-two-t-independent-sextic-reduction-pass212-working.md)
derives the exact sextic and excludes repeated quadratic centers.
Its new curve lemma needs a degree bound only on the first cone
coordinate. Squarefree centers were unresolved at212; their later
exclusions are included in216 above. The affine-pair argument211
does not apply to their degree profile.

Both notes have complete written AI reviews. Two independent
finite-algebra suites passed once, four methods each
(0.088 and0.470 seconds).
[Verification212](research/verification-pass212-working.json) and
[checkpoint212](research/checkpoint-pass212-working.json) record
50 equations and1,309 chained artifacts.
Separate213 working notes give
[sharper squarefree degree lists](research/rank-two-squarefree-center-degree-pruning-pass213-working.md)
and an [exact node/cusp ring in one linear-center branch](research/rank-two-linear-center-quadratic-projection-pass213-working.md).
They now have the separate213 packet described above.
The full cancellation goal remains unsolved, with no human expert
review, formal verification or novelty clearance.

## Previous investigation: recognition for the full supplied radical frame

The [recognition synthesis211](research/radical-initial-kernel-recognition-synthesis-pass211-working.md)
now concludes \(A\simeq\mathbb C^{[3]}\) for a globally sliced
actual frame of exact E-degrees \((1,1,2,2)\) whose entire
weighted initial kernel is \((X^2Z-W^2)\).
The [affine-pair proof211](research/radical-affine-pair-coordinate-recognition-pass211-working.md)
closes the last branch left by210. One slope case supplies an
actual auxiliary slice; the other is excluded by polynomial
contraction and the [fiber parity argument211](research/radical-wang-second-case-fiber-obstruction-pass211-working.md).

This is a restricted working theorem. No argument puts an arbitrary
cancellation instance into this frame, and other initial kernels
remain untreated. In particular a single vanishing leading relation
does not supply the full-kernel hypothesis.
The full conjecture remains unsolved.

All three211 sources have complete saved-source AI reviews.
Their40 tagged equations are accompanied by a standalone
four-method finite-algebra checker, fully read before its sole
passing run (0.110 seconds).
[Verification211](research/verification-pass211-working.json) and
[checkpoint211](research/checkpoint-pass211-working.json) record1,303
chained artifacts. Separate212 work is not included. These checks are not
human expert review, proof-assistant verification or novelty clearance.

## Previous investigation: the remaining radical projection is an affine pair

The [frontier synthesis210](research/radical-affine-pair-frontier-synthesis-pass210-working.md)
reduces the supplied exact1122 radical chart to an actual recognition
case or a nonconstant affine projected pair. It does not yet recognize
that last pair or put arbitrary examples into the supplied chart.

The new working proofs recognize
[constant second projection](research/weight-four-constant-second-projection-recognition-pass210-working.md),
recognize a zero center and
[exclude repeated quadratic centers](research/radical-zero-and-repeated-center-reduction-pass210-working.md),
and exclude both
[quadratic second projections](research/radical-squarefree-whole-plane-reduction-pass210-working.md)
and [quadratic-first affine-second graphs](research/radical-affine-second-quadratic-first-exclusion-pass210-working.md)
in the squarefree whole-plane case. The exclusions force an
irreducible polynomial in the original four-ring to be a square in
its fraction field, then use the contradiction. They do not assume
that a generic parameter is an ambient coordinate.

In the remaining case, the actual auxiliary derivation has coordinate
degrees \((0,1,2,1)\). It is not the nice, invariant-coefficient
derivation needed by criterion205. This precise recognition gap,
other leading sectors and arbitrary frame entry remain open.
The five210 notes have81 tagged equations and independent written
AI reconstruction. [Verification210](research/verification-pass210-working.json)
and [checkpoint210](research/checkpoint-pass210-working.json) record five
methods in one passing canonical run (0.225 seconds), and1,297 chained
records. Separate211 recognition work is not included in that packet.

The preceding [verification209](research/verification-pass209-working.json)
and [checkpoint209](research/checkpoint-pass209-working.json) are complete:
46 tagged equations, four methods in one passing canonical run
(0.191 seconds), and1,289 chained records. Separate210 work is not
retroactively included. The full conjecture remains unsolved, without
human expert review, formal verification or novelty clearance.

## Previous investigation: the proper radical projected-plane branch is recognized

The [synthesis209](research/radical-proper-plane-unit-speed-synthesis-pass209-working.md)
now gives a complete working proof for this restricted branch:
under the supplied globally sliced exact1122 frame, full radical
initial kernel, and nonzero return coefficient, a proper generic
projected plane forces \(EX\in\mathbb C^*\) and
\(A\simeq\mathbb C^{[3]}\).

The [cubic-second exclusion](research/radical-cubic-second-projection-exclusion-pass209-working.md)
eliminates the remaining cusp and node alternatives of second degree
three. The [cubic/quadratic recognition](research/radical-cubic-first-quadratic-second-unit-speed-pass209-working.md)
and retained quartic-first theorem below cover the two surviving
degree pairs with actual polynomial inverses. This is not an
inference from a generic parameter or a nonzero field scalar.

Consequently any unresolved nonunit-speed case within this chart
must have the whole projected plane \(L[y,\vartheta]=L[v]\).
That equality is not yet original-ring coordinate recognition.
Other leading kernels and arbitrary entry remain open.
The three209 notes are outside the frozen208 packet. Their later
independent reviews and canonical run are recorded in209 above.
The full conjecture remains unsolved; there is no human expert
review, formal verification, or novelty clearance.

## Previous investigation: actual recognition beyond the positive examples

The [quartic first-generator theorem208](research/radical-quartic-first-projection-unit-speed-pass208-working.md)
recognizes a restricted actual radical branch. If its projected plane
is proper and the original first projected generator has degree four,
the full equations force constant parameters. Both orders of an
explicit polynomial inverse then recover coordinates of the original
ring. Only after that step does the global slice force \(EX\) to be a
nonzero complex constant and \(A\simeq\mathbb C^{[3]}\).

Two companion notes delimit the
[I-only replica mechanism](research/radical-replica-invariant-slot-unit-speed-obstruction-pass208-working.md)
and prove [sharper local degree restrictions](research/radical-proper-projection-degree-refinement-pass208-working.md).
[Verification208](research/verification-pass208-working.json) and
[checkpoint208](research/checkpoint-pass208-working.json) record
53 tagged equations, five methods in one passing canonical run
(0.532 seconds), and 1,283 chained records.

The later209 completion of the proper-plane branch is recorded above,
not retroactively included in208. The whole-plane branch and arbitrary
entry into the supplied hypotheses remain open.

## Previous investigation: the projected node and cusp actually occur

The [uniform example207](research/radical-nodal-cuspidal-actual-frame-pass207-working.md)
realizes both a node and a cusp in the projected plane of actual
globally sliced polynomial frames. Both orders of the polynomial
inverse are explicit. These examples have \(EX=1\) and a known
polynomial kernel, so they are not cancellation counterexamples
or examples of the unresolved nonunit-speed case.

This rules out universal exclusion of those projected defects as a
proof strategy. A polynomial replica recovers an actual invariant
coordinate in the examples. The later branch results above use
additional derivations, not an assumed extension of the example.

[Verification207](research/verification-pass207-working.json) and
[checkpoint207](research/checkpoint-pass207-working.json) record
17 tagged equations and three methods in one passing canonical
run (0.122 seconds), bringing the chain to 1,277 records.

The preceding [classification206](research/weight-four-t-independent-leading-kernel-classification-pass206-working.md),
[eliminant206](research/weight-four-radical-nonzero-r-eliminant-pass206-working.md),
and [conductor reduction206](research/radical-projection-conductor-cubic-reduction-pass206-working.md)
now have a completed [verification packet206](research/verification-pass206-working.json)
and [checkpoint206](research/checkpoint-pass206-working.json).
The four-method finite checker passed once in 0.209 seconds.
The packet contains 46 tagged equations and brings the chain to
1,273 records. Example207 is separate and is not counted in206.
Finite algebra checks and AI peer review are not human expert review,
formal verification, or novelty clearance. The full conjecture
remains unsolved.

## Previous investigation: an actual commuting-pair recognition criterion

The [criterion205](research/nice-commuting-invariant-coefficients-recognition-pass205-working.md)
closes the restricted coordinate gap left in204. A nice commuting
derivation whose coordinate coefficients are invariant under the
original action yields an auxiliary polynomial slice. This makes
the coordinate supplied by the three-variable theorem an actual
coordinate of the original four-ring, where the regular-kernel
recognition theorem applies.

The [application205](research/weight-four-t-independent-zero-r-recognition-pass205-working.md)
verifies these extra hypotheses in the supplied weight-four chart
when \(q_t=0\), \(q_{\rho\rho}\ne0\), and \(R=0\).
It recognizes the specified zero-R radical and rank-two branches.
An actual countercontrol shows why commutation alone does not
supply the extra coefficient invariance.

[Verification205](research/verification-pass205-working.json) and
[checkpoint205](research/checkpoint-pass205-working.json) record two
notes, one checker and two JSON records: 37 tagged equations, three
methods in one canonical run, and 1,267 chained records. The run
passed in 0.220 seconds, initially terminal with no session or rerun.
These finite identities supplement the written proofs and exact
published-theorem checks. No expert, formal, or novelty certification
is claimed.

Separate206 working proofs now
[classify the t-independent sector](research/weight-four-t-independent-leading-kernel-classification-pass206-working.md),
[bound its nonzero-R radical projection](research/weight-four-radical-nonzero-r-eliminant-pass206-working.md),
and [reduce any remaining projection defect to a node or cusp](research/radical-projection-conductor-cubic-reduction-pass206-working.md).
These are not included in205; their later verification is recorded
in206 above.
Neither a generic plane coordinate nor the node/cusp reduction is
an invariant coordinate of the original four-ring. The full
cancellation goal remains active and unsolved.

## Previous investigation: actual controls and a conditional commuting derivation

The [positive example204](research/weight-four-two-root-actual-nonvacuity-pass204-working.md)
realizes the full two-root hypotheses of203 with explicit polynomial
inverses and a global slice. For the different kernel \(Z^2-X^2W\),
the [zero-R pivot reduction](research/weight-four-radical-pivot-zero-r-nice-derivation-pass204-working.md)
produces an actual nonzero nice LND commuting with \(E\) and fixing
\(X\). It does not yet produce an \(E\)-invariant ambient coordinate.

The [fixed-last-slot countercontrol](research/one-quadratic-replica-two-good-counterexample-pass204-working.md)
excludes every polynomial invariant replica parameter followed by a
shear linear in the other bad slot on one actual two-good frame.
The other slot is already invariant for \(J=X\), so the result does
not obstruct general coordinate entry or longer compositions.

[Verification204](research/verification-pass204-working.json) and
[checkpoint204](research/checkpoint-pass204-working.json) record three
notes, one checker and two JSON records: 31 tagged equations, four
methods in one canonical run, and 1,262 chained records. The suite
passed in 0.841 seconds through its original session, with no rerun
or pending handle. Finite controls do not prove the all-degree or
derivation arguments. Separate205 work is outside this packet;
the unrestricted cancellation goal remains active and unsolved.

## Previous investigation: the absent-W rank-one boundary is recognized

The [synthesis203](research/weight-four-absent-w-rank-one-recognition-synthesis-pass203-working.md)
proves the restricted conclusion \(A\simeq\mathbb C^{[3]}\) for the
supplied actual global-slice frame, exact E-time degrees \((1,1,2,2)\),
and entire initial kernel \((Z^2-X^2Y(X-Y))\). With retained results,
it covers the whole absent-\(W\), rank-one weight-four boundary.
It does not put arbitrary coordinates into that class.

The [monomial proof](research/weight-four-two-root-monomial-coordinate-recognition-pass203-working.md)
constructs an invariant ambient coordinate by a polynomial automorphism
with both inverse compositions. The
[reciprocal proof](research/weight-four-two-root-reciprocal-field-obstruction-pass203-working.md)
excludes the other families by exact degree-two and degree-three field
contradictions. These complement zero-R recognition196 and the complete
necessary classification201, through actual normalizations202.

[Verification203](research/verification-pass203-working.json) and
[checkpoint203](research/checkpoint-pass203-working.json) record three
notes, one checker and two JSON records:46 tagged equations, four
methods in one canonical run, and1,256 chained records. The run passed
in16.927 seconds through its original session, with no rerun or pending
handle. Finite checks support the written proofs, not the full conjecture.

Separate [nonvacuity204](research/weight-four-two-root-actual-nonvacuity-pass204-working.md)
gives a fully polynomial positive example of the supplied full-kernel
hypotheses; it is not counted in203. The next priority is actual
invariant-coordinate entry beyond these assumptions. The unrestricted
goal remains active and unsolved. No human expert certification,
formal verification, novelty clearance or external action is claimed.

## Previous investigation: all three two-root families have actual normal forms

The [monomial normalization202](research/weight-four-two-root-monomial-actual-normalization-pass202-working.md)
and [reciprocal-pair normalization202](research/weight-four-two-root-reciprocal-actual-normalization-pass202-working.md)
remove every lower mode using polynomial coordinate maps with explicit
inverses. Exact-field differential arguments prove completeness without
assuming a rational ambient coefficient field. The remaining third
potential is retained unless the branch itself forces it constant.

[Verification202](research/verification-pass202-working.json) and
[checkpoint202](research/checkpoint-pass202-working.json) record two notes,
one checker and two JSON records: 43 tagged equations, six methods in
one canonical run, and 1,250 chained records. The run passed in 1.952
seconds through its original session, with no rerun or pending handle.
These are finite algebra controls supporting the written normalization
proofs, not certification of cancellation. Separate203 branch work is
not included in this packet. The full goal remains active and unsolved.

## Previous investigation: the two-root differential gates have three families

The [classification201](research/weight-four-two-root-two-gate-classification-pass201-working.md)
solves the two nondegenerate necessary square-completion equations for
\(q^2=t(1-t)\) over every allowed finite algebraic coefficient field:
\(f=cq,\ cq/t,\ cq/(t-1)\), with \(c\in\mathbb C^*\).
This is a differential classification, not actual recognition or
realization of those families.

The separate [linear-factor proof](research/weight-four-two-root-linear-factor-rigidity-pass201-working.md)
uses field trace and nonzero residues to exclude an algebraic
logarithmic primitive. The other factor is controlled by two exact
resultants. Neither argument assumes that the ambient coefficient
field is rational.

[Verification201](research/verification-pass201-working.json) and
[checkpoint201](research/checkpoint-pass201-working.json) add two
notes, one checker and two JSON records: 33 tagged equations, four
methods in one canonical run, and 1,245 chained records. The suite
passed in 1.516 seconds through its original session, with exit zero
and no rerun or pending handle. No earlier run is recounted.

The three families still require actual lower-potential, scalar,
field-return and original-coordinate analysis. Work from202 onward
is outside this packet. The general cancellation goal remains active
and unsolved; no expert certification, formal verification or novelty
clearance is claimed.

## Previous investigation: the full square-root initial kernel is recognized

The [synthesis200](research/weight-four-square-root-complete-recognition-synthesis-pass200-working.md)
proves \(A\simeq\mathbb C^{[3]}\) for a supplied actual global-slice
frame with exact E-time degrees \((1,1,2,2)\) and entire initial
kernel \((Z^2-X^3Y)\). This is a restricted working theorem, not
a coordinate-entry theorem or a solution of general cancellation.

After the actual normalization199, the
[nonmonomial graph](research/weight-four-normalized-nonmonomial-graph-obstruction-pass200-working.md)
contradicts a cubic field degree, and the
[quadratic projection](research/weight-four-nonmonomial-quadratic-field-obstruction-pass200-working.md)
contradicts an irreducible quartic over the actual projected field.
These exclude the last nonmonomial family. The synthesis composes
them with zero-R recognition195, monomial recognition197 and
reciprocal exclusion198, using the exhaustive necessary classification195.
No rational coefficient-field assumption is made.

[Verification200](research/verification-pass200-working.json) and
[checkpoint200](research/checkpoint-pass200-working.json) add three
notes, one checker and two JSON records: 39 tagged equations, four
methods in one canonical run, and 1,240 chained records. The suite
passed in 0.922 seconds through its original session, with exit zero
and no rerun or pending handle. The earlier199 run is not recounted.

The different two-root kernel with nonzero \(R\), other initial
forms and ranks, height-two kernels, higher profiles and arbitrary
entry remain open. The general cancellation goal is active and
unsolved. These are AI-reviewed working proofs, not human expert
certification, formal verification or novelty clearance.

## Previous investigation: actual nonmonomial normalization and a bounded literature audit

The [normalization199](research/weight-four-nonmonomial-square-root-actual-normalization-pass199-working.md)
puts the nonmonomial family \(f=at+bq\), \(a,b\ne0\), \(q^2=t\),
into a canonical lower-potential form using actual polynomial maps
with polynomial inverses. The supplied hypotheses remain a global
slice, exact E-time profile \((1,1,2,2)\), and entire initial kernel
\((Z^2-X^3Y)\).

The proof obtains the full coefficient solution in the exact finite
field, then preserves the selected derivation, fields and generic
alternatives through every actual change. It does not itself recognize
or exclude either remaining alternative.

The separate [primary-literature audit](research/time-degree-1122-primary-literature-audit-pass199-working.md)
checks six searches and four nearby primary papers. Their inspected
statements do not supply the missing actual-coordinate hypotheses
from1122 alone. This is an applicability audit, not novelty clearance.

[Verification199](research/verification-pass199-working.json) and
[checkpoint199](research/checkpoint-pass199-working.json) add two notes,
one checker and two JSON records: 22 tagged equations, three methods
in one canonical run, and 1,234 chained records. The run passed in
0.924 seconds through its original session, with exit zero and no
rerun or pending handle. Separate200 results and its run are not counted.

Two-root nonzero-\(R\) cases, other initial forms, height-two kernels,
higher profiles and arbitrary entry remain outside this packet.
The general cancellation goal is active and unsolved. No expert
certification, formal verification or novelty claim is made.

## Previous investigation: the reciprocal square-root family is excluded

The [synthesis198](research/weight-four-reciprocal-square-root-frontier-synthesis-pass198-working.md)
excludes the entire nonzero-\(R\) family \(f=\beta_0/q\),
\(\beta_0\in\mathbb C^*\), \(q^2=t\), for the supplied full initial
kernel \((Z^2-X^3Y)\). The hypotheses remain an actual global slice
and exact E-time degrees \((1,1,2,2)\).

The [actual normalization](research/weight-four-reciprocal-square-root-actual-normalization-pass198-working.md)
preserves the selected derivation, coefficient fields, generic degrees
and full initial ideal. The
[graph argument](research/weight-four-normalized-reciprocal-square-root-graph-obstruction-pass198-working.md)
then gives an impossible index-two field return, independently confirmed
by an irreducible original polynomial forced to be a square.
The [quadratic-projection argument](research/weight-four-normalized-reciprocal-quadratic-field-obstruction-pass198-working.md)
gives an impossible index-three field return. These exclude both
actual alternatives, not merely selected formal formulas.

[Verification198](research/verification-pass198-working.json) and
[checkpoint198](research/checkpoint-pass198-working.json) add four notes,
one checker and two JSON records: 59 tagged equations, four methods
in one canonical run, and 1,229 chained records. The run passed in
0.435 seconds, initially terminal with exit zero, no session handle
and no rerun. The separate199 literature audit is not counted.

For this full square-root kernel, only the nonmonomial
\(f=at+bq\), \(a,b\ne0\), remains unresolved in the nonzero-\(R\)
classification. Two-root nonzero-\(R\) cases, other positive bad
quadratic rank configurations, height-two kernels, higher minimum
profiles and arbitrary entry remain open. The general cancellation
goal is active and unsolved. No expert certification, formal verification
or novelty clearance is claimed.

## Previous investigation: full monomial square-root branch recognized

The [synthesis197](research/weight-four-square-root-monomial-frontier-synthesis-pass197-working.md)
recognizes the entire nonzero-\(R\) family \(f=\beta q\),
\(\beta\in\mathbb C^*\), \(q^2=t\), for the supplied full kernel
\((Z^2-X^3Y)\). The assumptions remain an actual global slice and
exact E-time degrees \((1,1,2,2)\).

After the actual normalization and graph exclusion196, the
[new quadratic-projection proof](research/weight-four-normalized-square-root-quadratic-projection-recognition-pass197-working.md)
gives a polynomial inverse recovering \(y,z,q\) in the original ring.
It proves \(B=\mathbb C[X,y,z,q]\) and \(A=\mathbb C[y,z,q]\)
directly, without dividing by \(X\). The formulas also give genuine
examples with the entire stated initial kernel. This branch is
nonempty, not another exclusion.

[Verification197](research/verification-pass197-working.json) and
[checkpoint197](research/checkpoint-pass197-working.json) add two notes,
one checker and two JSON records: 30 tagged equations, three methods
in one canonical run, and 1,222 chained records. The run passed in
3.110 seconds through its original execution handle, with exit zero
and no pending handle or rerun.

The other \(f=at+bq\), \(a\ne0\), and \(f=b/q\) families, two-root
nonzero-\(R\) cases, positive bad quadratic rank as a whole, height-two
kernels, higher minimum profiles and arbitrary entry remain open.
The general cancellation goal is active and unsolved. No minimum or
entry theorem, expert certification, formal verification or novelty
clearance is claimed. Separate198 work is outside this packet.

## Previous investigation: a second zero-R branch recognized and one square graph excluded

The [synthesis196](research/weight-four-double-cover-frontier-synthesis-pass196-working.md)
recognizes the zero-\(R\) branch of the supplied full kernel
\((Z^2-X^2Y(X-Y))\), under an actual global slice and exact E-time
degrees \((1,1,2,2)\). The [proof](research/weight-four-two-root-zero-r-coordinate-recognition-pass196-working.md)
uses exact field return, a pole bound and a regular-differential
obstruction, then constructs an invariant coordinate with a polynomial
inverse in the original ring.

For the different full kernel \((Z^2-X^3Y)\), the
[actual normalization](research/weight-four-square-root-monomial-actual-normalization-pass196-working.md)
and [normality obstruction](research/weight-four-normalized-square-root-graph-obstruction-pass196-working.md)
exclude the entire quadratic-graph branch with \(f=\beta q\),
\(\beta\in\mathbb C^*\), \(q^2=t\).
The [formal index-two fixture](research/weight-four-square-root-formal-index-two-boundary-pass196-working.md)
is kept separate: it satisfies several coefficient identities but is
not an actual polynomial frame or a cancellation counterexample.

[Verification196](research/verification-pass196-working.json) and
[checkpoint196](research/checkpoint-pass196-working.json) add five notes,
two checkers and two JSON records: 78 tagged equations, six methods
in two once-only canonical runs, and 1,217 chained records.
Both runs passed, in 0.429 and 0.413 seconds, initially terminal with
exit zero and no pending handle or rerun.

Other square branches, the full positive bad quadratic rank stratum,
height-two kernels, higher minimum profiles and arbitrary entry remain
open. Neither entire double-cover configuration is settled here.
The general cancellation goal remains active and unsolved. There is no
minimum or entry theorem, human expert certification, formal verification
or novelty clearance. Separate197 work is not counted.

## Previous investigation: one double-cover branch recognized, remaining coefficients classified

The [synthesis195](research/weight-four-double-cover-frontier-synthesis-pass195-working.md)
recognizes the zero-\(R\) branch of the supplied full kernel
\((Z^2-X^3Y)\), under an actual global slice and exact E-time degrees
\((1,1,2,2)\). The [proof](research/weight-four-double-root-zero-r-coordinate-recognition-pass195-working.md)
uses exact field return to exclude two coefficient covers, then gives
an invariant coordinate by subtracting a quadratic polynomial in \(Z\)
from \(W\). Its inverse is polynomial in the original ring.

For nonzero \(R\), the
[algebraic leading-ratio reduction](research/weight-four-double-cover-nonzero-r-reduction-pass195-working.md)
excludes the pure-quartic alternative for both \(q^2=t\) and
\(q^2=t(1-t)\), leaving two square-completion alternatives.
For \(q^2=t\), the [complete two-gate classification](research/weight-four-square-root-two-gate-classification-pass195-working.md)
gives \(f=at+bq\), with \(a\in\mathbb C,\ b\in\mathbb C^*\),
or \(f=b/q\). These solve two necessary equations. They do not yet
give realized polynomial frames or recognition of the actual square
branches. The second double-cover form has additional unresolved cases.

[Verification195](research/verification-pass195-working.json) and
[checkpoint195](research/checkpoint-pass195-working.json) add four notes,
two checkers and two JSON records: 66 tagged equations, five methods
in two once-only canonical runs, and 1,208 chained records.
The runs passed in 0.293 and 0.390 seconds, both initially terminal
with exit zero and no pending handle or rerun.

Neither full double-cover configuration is settled by195.
Positive bad quadratic rank, height-two kernels, higher minimum
profiles and arbitrary entry remain open. No minimum or entry theorem,
human expert certification, formal verification or novelty clearance is
claimed. The general cancellation goal remains active and unsolved.
Separate196 work is outside this packet.

## Previous investigation: recognition of the zero-bad-quadratic-part weight-four stratum

The [grouped193--194 synthesis](research/weight-four-split-initial-recognition-synthesis-pass194-working.md)
recognizes the supplied full split kernel \((XYZ+X^4+Y^4)\).
Together with the retained actual normal forms and completed rows,
it recognizes every full irreducible weight-four kernel
\(F=P_2(X,Y)Z+Q_2(X,Y)W+H_4(X,Y)\), with no quadratic terms in \(Z,W\).
The hypotheses remain an actual polynomial four-ring with a global
slice, exact E-time degrees \((1,1,2,2)\), and the entire initial kernel.

The [actual reduction193](research/weight-four-split-nonzero-r-three-alternatives-pass193-working.md)
leaves a pure quartic graph or two square alternatives.
The [general Jacobian gate193](research/weight-four-split-square-candidate-jacobian-obstruction-pass193-working.md)
and [two-equation exclusion194](research/weight-four-split-two-gate-algebraic-exclusion-pass194-working.md)
remove both square alternatives over the exact coefficient field.
The earlier \(f=t^5+3t\) remains a solution of the first necessary
equation, but fails the additional actual-Jacobian condition.
The [pure-quartic proof193](research/weight-four-split-pure-quartic-coordinate-recognition-pass193-working.md)
returns an invariant coordinate to the original ring by two polynomial
shears. The published regular-kernel theorem then gives
\(A=\mathbb C[I]^{[2]}\).

[Verification194](research/verification-pass194-working.json) and
[checkpoint194](research/checkpoint-pass194-working.json) add five notes,
three checkers and two JSON records: 83 tagged equations, nine methods
in three once-only canonical runs, and 1,200 chained records.
The runs passed in 0.091, 1.382 and 0.301 seconds; the middle run
completed through its original execution handle. No rerun occurred.

This is a written restricted proof with saved-source AI review and finite
algebraic controls, not human expert review, formal certification or
novelty clearance. Positive bad quadratic rank, height-two kernels,
higher minimum time profiles and arbitrary coordinate entry remain open.
No minimum or entry theorem is claimed, and not every weight-four
kernel belongs to this stratum. The general cancellation goal remains
active and unsolved. Separate195 work is outside this packet.

## Previous investigation: split zero-R recognition and a necessary-equation obstruction

The [grouped191--192 synthesis](research/weight-four-split-frontier-synthesis-pass192-working.md)
recognizes the zero-\(R\) branch of the supplied split initial kernel
\((XYZ+X^4+Y^4)\), under an actual globally sliced frame of exact
E-time degrees \((1,1,2,2)\).
The [proof192](research/weight-four-split-zero-r-coordinate-recognition-pass192-working.md)
derives its coefficient and exact-field gates, then constructs an original
invariant coordinate by a polynomial shear. The published regular-kernel
theorem gives \(A=\mathbb C[I]^{[2]}\).

The [coefficient lemmas191](research/weight-four-split-coefficient-ode-lemmas-pass191-working.md)
exclude a quadratic cover by a pole-degree obstruction and force the
linear slope to be \(\lambda t\), not constant.
The [negative result192](research/weight-four-split-nonzero-r-ode-counterexample-pass192-working.md)
shows that the earlier affine-only differential exclusion does not extend
to the next nonzero-\(R\) equation: \(f=t^5+3t\) solves that equation.
This is a necessary-equation counterexample, not an actual frame or
a counterexample to cancellation.

Separately, [two actual frames191](research/weight-four-absent-variable-two-actual-frames-pass191-working.md)
realize both branches of the different absent-variable kernel
\((X^2Z-Y^4)\). Their polynomial inverses and literal selected partials
are supplied; no globally minimal time-profile claim is made.

[Verification192](research/verification-pass192-working.json) and
[checkpoint192](research/checkpoint-pass192-working.json) add five notes,
three checkers and two JSON records: 80 tagged equations, nine methods
in three canonical runs, and 1,190 chained records.
The runs passed in 0.115, 0.947 and 0.355 seconds.
The middle run completed through its original execution handle.
Saved-source AI review and finite tests are not human expert review,
formal verification or novelty clearance.

The split nonzero-\(R\) branch and arbitrary entry remain unresolved
in this packet. Separate193--194 investigations are not counted here.
The general cancellation problem remains unsolved and the full goal active.

## Previous investigation: working recognition of the absent-variable quartic configuration

The [synthesis190](research/weight-four-absent-variable-recognition-synthesis-pass190-working.md)
now recognizes the supplied full initial kernel \((X^2Z-Y^4)\)
in an actual globally sliced frame of exact E-time degrees
\((1,1,2,2)\). Both branches left by189 produce an invariant coordinate
of the original polynomial four-ring, with a polynomial inverse.
The published regular-kernel theorem then gives
\(A=\mathbb C[I]^{[2]}\).

In the zero-\(R\) branch, the
[field normal form](research/weight-four-absent-zero-r-field-normal-form-pass190-working.md)
uses exact function-field return to force the remaining slope to be
complex. The independently written
[coordinate return](research/weight-four-absent-zero-r-coordinate-return-pass190-working.md)
then gives an original polynomial shear. In the nonzero-\(R\) branch,
the [recognition proof](research/weight-four-absent-nonzero-r-coordinate-recognition-pass190-working.md)
first proves its coefficient gates, then uses two actual shears and
the full determinant to return an invariant coordinate.
Neither argument assumes a rational coefficient field or turns
a generic denominator into an original-ring unit.

[Verification190](research/verification-pass190-working.json) and
[checkpoint190](research/checkpoint-pass190-working.json) add four
written sources, two checkers and two JSON records: 68 tagged equations,
six methods in two once-only canonical runs, and 1,180 chained records.
Saved-source AI reviews and finite algebra controls are not human
expert review, formal verification or novelty clearance.

This result does not prove that an arbitrary globally sliced action
enters the specified frame. The split coefficient form
\(XYZ+X^4+Y^4\), positive quadratic bad-variable rank, height-two kernels,
higher possible minimum time profiles and arbitrary entry remain
unresolved. Unrestricted cancellation is not solved; the full goal
remains active. Separate191 work is not included in this packet.

## Previous investigation: the absent-variable quartic reduces to two exact-field graph branches

The [synthesis189](research/weight-four-absent-variable-frontier-synthesis-pass189-working.md)
reduces the supplied full initial kernel \((X^2Z-Y^4)\), in an actual
globally sliced frame of exact E-time degrees \((1,1,2,2)\), to two
generic graph branches. Constant projected \(y\) is excluded. In the
zero-\(R\) branch, \(y\) is affine, the graph is cubic and its coefficient
cover has constant linear slope. In the nonzero-\(R\) branch, \(y\) is
affine, the graph is quartic and \(R=1/(At+B)\) with complex \(A,B\).

The [cover-collapse proof](research/weight-four-absent-zero-r-cover-collapse-pass189-working.md)
uses actual function-field return and a pole-degree argument.
The [quartic-graph reduction](research/weight-four-absent-nonzero-r-quartic-graph-reduction-pass189-working.md)
keeps the exact algebraic coefficient field and proves its ODE
restriction through a finite-ramification local expansion.
Neither reduction constructs an invariant coordinate in the original
four-ring. Recognition of this absent-variable configuration remains open.

A separate [actual example187](research/weight-four-common-factor-actual-frame-pass187-working.md)
verifies both polynomial inverse orders, the selected derivation and
the full initial kernel for the different common-factor form
\((X^2Z+XYW-Y^4)\), already recognized186. It does not realize the
absent-variable branch or establish a globally minimal time profile.

[Verification189](research/verification-pass189-working.json) and
[checkpoint189](research/checkpoint-pass189-working.json) group passes187–189:
seven written sources, six checkers and two JSON records, with114 tagged
equations,16 methods in six once-only canonical runs, and1,172 chained
records. Every run returned OK and exit zero in its initial response,
without a pending handle or rerun. Saved-source AI reviews and finite
controls are not human expert review, formal verification or novelty
clearance.

The next step is to solve the residual coefficient identities and prove
any required original-ring coordinate return. Other weight-four forms,
height-two kernels, higher possible minimum time profiles and arbitrary
entry remain unresolved. Unrestricted cancellation is not solved;
the full goal remains active.

## Previous investigation: working recognition of the common-factor quartic configuration

The [synthesis186](research/weight-four-common-factor-recognition-synthesis-pass186-working.md)
now covers the full initial kernel \((X^2Z+XYW-Y^4)\) in a supplied
actual globally sliced frame of exact E-time degrees \((1,1,2,2)\).
The [constant-projection exclusion](research/weight-four-common-factor-constant-projection-exclusion-pass186-working.md),
[low-graph exclusion](research/weight-four-common-factor-low-graph-exclusion-pass186-working.md)
and [quadratic-graph exclusion](research/weight-four-common-factor-quadratic-graph-exclusion-pass186-working.md)
close the cases left open in185. The only surviving graph has degree
five, where the retained construction gives an invariant coordinate
in the original four-ring and a two-sided polynomial inverse.
The published regular-kernel theorem then gives
\(A=\mathbb C[I]^{[2]}\).

Together with the coprime-pair exclusion185 and the
[actual normal forms184](research/weight-four-zero-bad-rank-normal-forms-pass184-working.md),
this handles full irreducible weight-four initial relations
\(P_2(X,Y)Z+Q_2(X,Y)W+H_4(X,Y)\) with independent quadratic
coefficients \(P_2,Q_2\). It is not a theorem for every quartic
relation or a proof that an arbitrary action enters this frame.

[Verification186](research/verification-pass186-working.json) and
[checkpoint186](research/checkpoint-pass186-working.json) add four
written sources, two checkers and two JSON records: 53 tagged equations,
five methods in two once-only canonical runs, and 1,157 chained records.
The two-method suite passed in 0.117 seconds and the three-method suite
in 0.126 seconds, both initially terminal with exit zero and no handle
or rerun. Saved-source AI reviews and finite controls are not human
expert review, formal verification or novelty clearance.

One-dimensional bad-coefficient spans, positive quadratic bad-variable
rank, height-two initial kernels, higher possible minimum time profiles
and arbitrary coordinate entry remain unresolved. Unrestricted
cancellation is not solved; the full goal remains active.

## Previous investigation: a quartic configuration excluded, another branch recognized

The [weight-four synthesis185](research/weight-four-frontier-synthesis-pass185-working.md)
excludes the full initial kernel \((X^2Z+Y^2W)\) under a supplied
actual globally sliced frame of exact E-time degrees \((1,1,2,2)\).
The [affine-projection argument](research/weight-four-coprime-graph-degree-obstruction-pass185-working.md)
and independent [constant-projection argument](research/weight-four-coprime-constant-projection-exclusion-pass185-working.md)
contradict both alternatives left by the exact-field projection proofs.
Actual homogeneous normal forms extend this exclusion to every
independent coprime pair of quadratic bad-variable coefficients.

For the different initial kernel \((X^2Z+XYW-Y^4)\), the
[high-graph proof185](research/weight-four-common-factor-high-graph-recognition-pass185-working.md)
constructs an actual invariant coordinate when projected \(y\) is
affine and the graph has degree at least three. Its
[normalized endpoint](research/weight-four-normalized-common-factor-recognition-pass185-working.md)
has an explicit two-sided polynomial inverse.
The constant-\(y\) and graph-degree-at-most-two branches remain open.
Separately, the [squarefree double-cover proof184](research/weight-four-squarefree-double-cover-exclusion-pass184-working.md)
excludes the absent-\(W\) form \(Z^2+H_4(X,Y)\) for squarefree \(H_4\);
it does not exclude \(ZW+H_4\).

The [universal chart184](research/weight-four-universal-chart-potentials-pass184-working.md)
keeps algebraic coefficient fields and its essential quadratic
potential term. The [whole-plane](research/weight-four-bad-linear-whole-plane-projection-pass184-working.md)
and [selected-component](research/weight-four-bad-linear-selected-component-pass184-working.md)
arguments treat zeros of the return coefficient without assuming
an inverse there.
Other quartic families, height-two initial kernels, higher possible
minimum time profiles and arbitrary coordinate entry remain unresolved.
Unrestricted cancellation is not solved; the full goal remains active.

[Verification185](research/verification-pass185-working.json) and
[checkpoint185](research/checkpoint-pass185-working.json) bundle
twelve proof sources, three checkers and two JSON records:
186 tagged equations, nine methods in three once-only canonical runs,
and 1,149 chained records. The three-method suites passed in
0.233, 0.124 and 0.100 seconds, each initially terminal with exit zero
and no handle or rerun. Saved-source AI reviews and finite controls
are not human expert review, formal verification or novelty clearance.

## Previous investigation: working recognition of the full split configuration

The [split synthesis183](research/split-initial-recognition-synthesis-pass183-working.md)
now covers every projected graph degree under a supplied actual
globally sliced frame with exact E-time degrees \((1,1,2,2)\) and
full weighted initial kernel \((XZ+YW)\). Each surviving branch
produces an invariant coordinate of the original polynomial four-ring,
with a polynomial inverse. The published regular-kernel theorem
then gives \(A\simeq\mathbb C^{[3]}\).

The [low-graph proof181](research/split-low-degree-graph-three-good-recognition-pass181-working.md)
uses only the evaluated cofactor and actual field return.
For nonlinear graphs, [normalization178](research/split-affine-graph-coefficient-normal-form-pass178-working.md)
leads either to the [zero-slope coordinate179](research/split-rho-constant-potential-coordinate-pass179-working.md)
or to [reciprocal rigidity180](research/split-nonzero-rho-slope-reciprocal-rigidity-pass180-working.md)
and the [coordinate construction182](research/split-reciprocal-slope-invariant-coordinate-pass182-working.md).
The revised nonlinear route includes degree two and does not require
the general three-good recognition156 endpoint.

This is not unrestricted cancellation or a proof of entry into this
frame. Full weight-four initial relations, height-two initial kernels,
higher possible minimum E-time profiles and arbitrary coordinate entry
remain unresolved. The full cancellation goal remains active.

[Verification183](research/verification-pass183-working.json) and
[checkpoint183](research/checkpoint-pass183-working.json) bundle
seven written sources and three checkers: 101 tagged equations,
nine methods in three distinct canonical runs, and 1,132 chained
records. The runs passed in 0.244, 0.125 and 0.218 seconds, each
terminal in its initial response with no handle or rerun.
The degree-two proof extension added no test methods or execution.
Saved-source AI reviews and finite controls are not human expert
review, formal verification or novelty clearance.

## Previous investigation: the actual split chart has an affine projected parameter

The [quadratic exclusion177](research/split-quadratic-projection-exclusion-pass177-working.md)
shows that the projected \(y\) cannot have degree two.
Whole-plane generation gives an exact-field nested quadratic form
for its relation. The evaluated unit cofactor from176 and the
eliminant's degree bounds make that relation pure. Its cubic
coefficient in the second formal variable then contradicts the
required quadratic center.

Together with176's independent constant-projection exclusion,
this gives \(L[y]=L[v]\) and \(\vartheta=P(y)\) with
\(\deg P\le4\). The parameter is affine over the exact field \(L\);
it is not thereby a coordinate of the original four-ring.
Split-kernel recognition and unrestricted cancellation remain open.

[Verification177](research/verification-pass177-working.json) and
[checkpoint177](research/checkpoint-pass177-working.json) record
14 equations and 1,120 chained records. This step is proof-only:
no177 checker or test execution was added, and176's run is not
counted again. No178 result is included. Saved-source AI reviews
are not human expert review, formal certification or novelty clearance.

## Previous investigation: the split projection is nonconstant and has degree at most two

The [constant-projection exclusion176](research/split-constant-projection-exclusion-pass176-working.md)
uses one determinant computation over the exact coefficient field.
It produces an actual commuting locally nilpotent derivation whose
kernel is a polynomial three-ring. Wang's two-coordinate theorem
then forces an invariant split quadratic form with an arbitrary
good-coordinate correction, contradicting the global slice at its
nondegenerate critical point. This excludes \(y\in L\) without using
the whole-plane completion or assuming a rational coefficient field.

The separate [selected-component proof176](research/split-cubic-simple-selected-component-pass176-working.md)
uses that whole-plane completion to rule out a common zero of
\(R\) and \(f_V\). The evaluated quartic cofactor is a unit, although
disjoint extra components are not excluded. Simple roots of \(R\)
and point separation then give \(\deg_v y\in\{1,2\}\).

[Verification176](research/verification-pass176-working.json) and
[checkpoint176](research/checkpoint-pass176-working.json) record
37 equations, three methods and 1,117 chained records.
One canonical suite passed in0.158 seconds, terminal immediately
without a handle or rerun. This remains a restricted split-chart
result, not kernel recognition or unrestricted cancellation.
No177 or178 result is included in176.

## Previous investigation: the actual split chart has a whole generic plane embedding

The [split chart175](research/split-cubic-generic-chart-pass175-working.md)
retains a supplied actual sliced frame with exact E-degrees
\((1,1,2,2)\) and full initial kernel \((XZ+YW)\). Its determinant
gives two polynomial coefficient potentials without dividing by
\(R=k_\rho-y\). The [zero-R argument](research/split-zero-R-exclusion-pass175-working.md)
excludes \(R\) vanishing identically, while the
[quartic bound](research/split-cubic-projected-quartic-bound-pass175-working.md)
proves that the selected projected relation has degree at most four.

The [whole-plane proof](research/split-projection-exceptional-cone-pass175-working.md)
then shows \(L[y,\vartheta]=L[v]\), including points where \(R=0\).
Its squarefree case uses both potentials and a finite integral extension.
The repeated quadratic case uses the actual determinant to avoid the
cone vertex, then applies the
[vertex-free cone lemma](research/split-vertex-free-quartic-cone-lemma-pass175-working.md).
A formal nodal example explains why the degree bound and birational
field equality alone would not have been enough.

This is a polynomial plane embedding over the exact coefficient field
\(L\), not a coordinate construction in the original four-ring.
Split-case recognition, weight-four initial relations, height-two
initial kernels and arbitrary coordinate entry remain unresolved.
The full cancellation problem is still unsolved.

[Verification175](research/verification-pass175-working.json) and
[checkpoint175](research/checkpoint-pass175-working.json) record
61 tagged equations, seven finite-control methods and 1,112 chained
records. Two distinct suites passed four methods in 0.316 seconds and
three in 0.128 seconds. Both completed in their initial responses,
with no pending handle or rerun. The first run was concrete progress
in the preceding goal/status turn and is counted once here.
Saved-source AI reviews are not expert review, formal verification
or novelty clearance. No176 or177 result is included.

## Previous investigation: working recognition under the full cusp initial-kernel hypothesis

The [synthesis174](research/cusp-initial-recognition-synthesis-pass174-working.md)
now covers every branch of the actual sliced cusp chart: exact
E-degrees \((1,1,2,2)\) and full weighted initial kernel
\((XZ-Y^3)\). This is a theorem under a supplied coordinate-frame
hypothesis, not a proof that every polynomial cylinder admits that frame.

The last branch, \(r\ne0,\ y\in L\), uses a new
[field and localization proof174](research/cusp-constant-projection-parabola-field-pass174-working.md).
The actual speed localization forces the projected parabola coefficients
into \(\mathbb C(y)\). The
[global recognition proof174](research/cusp-constant-projection-global-recognition-pass174-working.md)
then uses the determinant to make a polynomial shear possible in the
original four-ring. A commuting coordinate partial reduces the action
to an actual three-variable derivation, where the cited classification
and regular-kernel theorems apply.

Together with171,172 and173, this completes the stated cusp case split.
It does not replace the full initial-kernel hypothesis by one leading
identity. The split cubic \((XZ+YW)\), weight-four height-one relations,
height-two initial kernels and arbitrary coordinate entry remain open.
No upper bound on an arbitrary action's minimum E-degree is proved.
Unrestricted complex-threefold cancellation remains unsolved.

[Verification174](research/verification-pass174-working.json) and
[checkpoint174](research/checkpoint-pass174-working.json) record
32 tagged equations, three finite-control methods and 1,103 chained
records. The single canonical run passed in 0.080 seconds and was
terminal in its initial response, without a pending handle or rerun.
The173 run is separate and is not counted again. The saved-source
AI reviews and primary-source checks are not human expert review,
formal verification or novelty clearance. No175 result enters this packet.

## Previous investigation: the zero-r cusp branch has a global invariant coordinate

The [coefficient proof173](research/cusp-zero-r-coefficient-normal-form-pass173-working.md)
and [field-forcing proof173](research/cusp-zero-r-field-forcing-pass173-working.md)
handle the actual branch \(k_\rho=0,\ n_\rho\ne0\), without assuming
a trivial coefficient cover or a unit selected speed. Exact coefficient
integration and the field equality supplied by the polynomial inverse
force a projected triangular coordinate.

The [global construction173](research/cusp-zero-r-global-coordinate-pass173-working.md)
then returns that coordinate to the original ring. It subtracts an
explicit quadratic term in \(Z\) from \(W\), and proves that the
remaining correction coefficients lie in \(\mathbb C[X,Y]\).
The resulting invariant is monic in \(W\) with a polynomial inverse.
The published regular-kernel theorem therefore recognizes the kernel
under these actual-frame hypotheses.

This includes the genuine quadratic-cover example171. Combined with
the separate172 exclusion, it covers the zero-\(r\) branch of this
cusp chart. The nonzero-\(r\), constant-\(y\) branch, other initial
configurations and arbitrary entry remain outside this result.
The full cancellation problem is still unsolved.

[Verification173](research/verification-pass173-working.json) and
[checkpoint173](research/checkpoint-pass173-working.json) record
47 tagged equations, three finite-control methods and 1,097 chained
records. The one canonical run passed in 0.196 seconds and completed
in its initial response, without a pending handle or rerun.
Saved-source AI reviews and an exact primary-source check support
the working proof; they are not human expert or formal verification,
nor novelty clearance. No174 result enters this packet.

## Previous investigation: the zero-r, zero-second-coefficient cusp branch is excluded

The [proof172](research/cusp-zero-r-constant-projection-exclusion-pass172-working.md)
excludes the branch \(k_\rho=n_\rho=0\) in the actual cusp chart.
The polynomial inverse identifies its coefficient field and makes
the original partial \(\partial_W\) commute with the action.
The resulting polynomial three-variable restriction satisfies
Wang's two-coordinate classification. Both alternatives contradict
the cusp identity among its leading coefficients.

This is a proof-only result: 15 tagged equations, no new checker
and no172 test execution. The exact published classification
statement and its applicability were checked, and the saved proof
received independent model reconstruction.
[Verification172](research/verification-pass172-working.json) and
[checkpoint172](research/checkpoint-pass172-working.json) preserve
1,091 chained records without changing171's two completed runs.

The remaining cusp branches include \(r=0,\ n_\rho\ne0\), whose
coefficient field can have the genuine quadratic cover exhibited
in171, and \(r\ne0,\ y\in L\). Other initial profiles and unrestricted
entry also remain open. No173 development is included in this
packet. The full cancellation problem remains unsolved, without
human expert, formal or novelty certification.

## Previous investigation: the nonconstant-y, nonzero-r cusp branch is recognized

The [direct reframe171](research/cusp-pure-quadratic-three-good-recognition-pass171-working.md)
recognizes every pure quadratic whole relation in the stated actual cusp
chart. Its explicit triangular coordinate change supplies a third slot
annihilated by \(E^2\), so the retained three-good theorem applies.
This bypasses170's extra linear-rho-intercept assumption; it does not
prove that assumption automatic. Combining the new result with the
retained extra-factor, cubic and quartic results gives the exact
[case synthesis171](research/cusp-nonconstant-projected-coordinate-recognition-pass171-working.md):
\(r\ne0\) and \(y\notin L\) imply working recognition under those
actual-frame hypotheses. The separate
[nonconstant-ratio supplement](research/cusp-pure-quadratic-nonconstant-ratio-exclusion-pass171-working.md)
also excludes one quadratic-intercept alternative by actual field return.

The next zero-r branch has an important
[actual boundary171](research/cusp-zero-r-square-root-actual-boundary-pass171-working.md).
The frame with \(W=t+c(XZ-Y^3)^2\) has a two-sided polynomial inverse
and a genuine quadratic coefficient field. It satisfies
\(s_\rho\ne0\), so a universal vanishing claim is false.
This example already has an invariant coordinate and a polynomial
invariant ring; it is not a cancellation counterexample.

Two distinct171 suites passed three methods each, in0.125 and0.181
seconds. Both runs completed in their initial responses, with no
handle, interruption or rerun.
[Verification171](research/verification-pass171-working.json) and
[checkpoint171](research/checkpoint-pass171-working.json) preserve
33 tagged equations, six new methods and1,088 chained records.
The preceding status-only goal turn made no new progress; this
continuation supplied the proofs, actual boundary and canonical runs.

Zero-r charts, the nonzero-r constant-y case, other initial profiles
and unrestricted coordinate entry remain outside this recognition
statement. Later172 work is excluded from this packet. The full goal
remains unsolved, without human expert, formal or novelty certification.

## Previous investigation: quadratic extra factors are excluded, with a conditional coordinate

The [extra-factor proof169](research/cusp-quadratic-extra-factor-exclusion-pass169-working.md)
excludes a nonconstant extra factor for an actual quadratic graph in
the fixed cusp chart. Its coefficient equations force exact degrees
two and three in rho. Comparing the residue fields at rho-infinity
then contradicts the field equality supplied by the original polynomial
inverse. The argument keeps the exact coefficient field and does not
assume that the selected speed is a unit.

The separate [conditional proof170](research/cusp-pure-quadratic-linear-intercept-pass170-working.md)
constructs a global invariant coordinate when the remaining pure
quadratic graph has \(p_0\in K[\rho]\) of degree at most one.
That condition is an additional hypothesis, not a consequence of169.
The explicit polynomial inverse and retained regular-kernel theorem
recognize this subbranch. Whether every actual pure quadratic graph
satisfies the condition remains open.

Three169 methods passed in0.788 seconds. The initial call returned
a live session, and one poll completed that same run; nothing was
restarted or rerun. There is no170 checker or test execution.
[Verification169](research/verification-pass169-working.json),
[checkpoint169](research/checkpoint-pass169-working.json),
[verification170](research/verification-pass170-working.json) and
[checkpoint170](research/checkpoint-pass170-working.json) preserve
the distinct scopes and1,080 chained records.

The next bounded task is to remove or refute the linear-rho-intercept
hypothesis. Constant or linear graphs, the zero-r branches, other
initial profiles and unrestricted coordinate entry remain separate.
The full cancellation problem is unsolved. These are working results
without human expert, formal or novelty certification.

## Previous investigation: the actual cubic graph branch has a global coordinate

The [global proof168](research/cusp-cubic-global-coordinate-pass168-working.md)
constructs a polynomial invariant coordinate in the actual cubic graph
branch of the cusp initial form \(XZ-Y^3\). A literal chart expansion
and six differential identities show that its correction has complex
coefficients. An explicit two-sided polynomial inverse then returns
the coordinate to the original four-ring. The retained regular-kernel
theorem gives \(A\simeq\mathbb C^{[3]}\) in this branch.

The proof includes an actual cubic example. It also records and corrects
an earlier omitted mixed coefficient; the resulting proposed obstruction
was withdrawn. Three168 methods passed in0.686 seconds without a rerun.
[Verification168](research/verification-pass168-working.json) and
[checkpoint168](research/checkpoint-pass168-working.json) preserve the
canonical evidence and1,073 chained records.

Together with166, this recognizes the stated actual cubic and quartic
graph branches. Lower graph degrees, other initial profiles and
unrestricted coordinate entry remain open. These are working proofs,
not a solution of the full cancellation conjecture or human, formal,
or novelty certification. Later169 work is not included in this packet.

## Previous investigation: exact cubic coefficients and a projected coordinate

The [field-forcing proof167](research/cusp-cubic-field-forcing-pass167-working.md)
uses the actual projected field equality and the elementary pencil lemma
to force the cubic coefficient constants. It proves \(K=\mathbb C(g_0)\)
and gives a polynomial inverse for the projected coordinates. The167
result alone does not put \(g_0\) in the original invariant ring; the
global construction is the separate168 result above.

[Verification167](research/verification-pass167-working.json) and
[checkpoint167](research/checkpoint-pass167-working.json) contain a
proof-only record with1,069 chained entries. No167 checker exists and
no167 test execution is claimed.

## Previous investigation: the actual quartic graph branch is recognized

The [field-return proof166](research/cusp-quartic-actual-field-recognition-pass166-working.md)
completes a working recognition proof for the actual quartic graph
subcase of the cusp initial form \(XZ-Y^3\). The original polynomial
inverse forces an exact projected field equality. An elementary
plane-curve degree argument then forces the remaining coefficient to
be constant, giving the degree-four condition required by165.
This does not assume that the coefficient field is rational or that
the selected speed is a unit.

Combining166 with165 constructs an actual invariant coordinate with
a two-sided polynomial inverse. The cited regular-kernel theorem of
Bhatwadekar, Gupta and Lokhande then gives \(A\simeq\mathbb C^{[3]}\)
in this subcase. A separate formal example has projected field index
eight, so it fails the actual inverse hypothesis despite satisfying
the lower coefficient equations.

Three166 methods passed in0.174 seconds, after the complete source
read. [Verification166](research/verification-pass166-working.json)
and [checkpoint166](research/checkpoint-pass166-working.json) record
the exact canonical evidence and1,066 chained records. No checker
was rerun during closure. This is a working subcase proof, not a
solution of the full cancellation conjecture or human, formal, or
novelty certification. Lower-degree graphs, other initial profiles,
and unrestricted coordinate entry remain outside the result.

## Previous investigation: an exact weight-four existence criterion

The [criterion165](research/cusp-quartic-weight-four-sufficiency-pass165-working.md)
proves that an invariant of original weight at most four exists in
the actual quartic branch exactly when \((A\tau+B)k_0\) is a complex
polynomial of degree at most four. The sufficient direction uses
actual constant coordinate changes, exact finite-field Euler
identities, and an explicit polynomial invariant. Setting \(J=W-YZ\)
gives its direct coordinate inverse. The free graph intercept is
retained, and no generic coefficient-dependent shear is assumed integral.

Three165 methods passed in0.120 seconds.
[Verification165](research/verification-pass165-working.json) and
[checkpoint165](research/checkpoint-pass165-working.json) record the
criterion, source reviews and1,062 records. The proof of the condition
throughout the quartic branch belongs to the separate166 packet above.

## Previous investigation: a conditional polynomial coordinate and pole restrictions

The [weight-four gate164](research/cusp-weight-four-coordinate-gate-pass164-working.md)
proves that, in the actual quartic-graph cusp branch, any nonconstant
invariant of original weight at most four is an actual polynomial
coordinate. It gives the complete ansatz, excludes its two degenerate
cases, and supplies a two-sided polynomial inverse in the surviving case.
Existence remains unproved. A necessary condition is that
\((c_1\tau+c_0)k_0\) be a complex polynomial of degree at most four.

The [field and divisor argument164](research/cusp-coefficient-field-and-contracted-divisors-pass164-working.md)
also proves \(L=K(\rho)\), with \(K\) finite over \(\mathbb C(\tau)\).
An elementary specialization identity makes the pole locus outside
\(a=0\) map to finitely many points under the two coefficient ratios.
It does not remove the omitted locus or construct an invariant.
Three exact methods passed in 0.147 seconds; the full arguments are written
separately from those finite controls.
[Verification164](research/verification-pass164-working.json) and
[checkpoint164](research/checkpoint-pass164-working.json) record
scope and evidence. Human review, formal certification and novelty
clearance remain absent. The full cancellation conjecture is unsolved.

The next bounded question is whether the necessary degree-four
coefficient condition is also sufficient under all the quartic equations.
Other initial profiles and unrestricted coordinate entry remain open.

## Previous investigation: actual quartic graphs and two failed shortcuts

The [quartic restrictions163](research/cusp-quartic-graph-coefficient-rigidity-pass163-working.md)
force a reciprocal-affine coefficient and give an example satisfying
the generic equations but failing actual field return.
A distinct [actual quartic example163](research/cusp-actual-quartic-graph-boundary-pass163-working.md)
has a polynomial inverse and invariant coordinate
\(t=Y^4+(1-XY)Z+XW\). Thus this branch cannot simply be excluded.
Four exact methods passed in 0.125 seconds.
[Verification163](research/verification-pass163-working.json) and
[checkpoint163](research/checkpoint-pass163-working.json) distinguish
the two examples and preserve the canonical execution.

The [low-weight obstruction162](research/cusp-low-weight-invariant-parameter-obstruction-pass162-working.md)
rules out invariants of weight at most three when \(r\) is zero
or nonconstant. An [actual family162](research/cusp-selected-plinth-countercontrol-pass162-working.md)
also shows that the selected derivation can have a nonunit plinth,
although its primitive quotient has a global slice.
[Verification162](research/verification-pass162-working.json) preserves
the three passing methods, the intentionally interrupted slow
implementation and the intermediate structural-assertion failure.
[Checkpoint162](research/checkpoint-pass162-working.json) freezes this
restricted result. Neither shortcut failure disproves cancellation.

## Previous investigation: the nonlinear generic cusp branch is excluded

The [exclusion161](research/cusp-nongraph-quartic-exclusion-pass161-working.md)
rules out the remaining nongraph quartic under the actual cusp-chart
hypotheses. The full constant determinant imposes an even-parity
identity. Its highest rho coefficient disagrees with the necessary
fifth-power functions by the nonzero rational function \(63/(4t^4F)\).
The proof handles all lower integration coefficients over the exact
coefficient field; it does not assume that field is rational.

Together with the zero-r result160, this means that the projected
coordinate y is constant or affine on the generic intrinsic line:
\(N^2y=0\). This is a restriction in the localized chart, not an
original polynomial coordinate or a global slice.

Three new exact methods passed in 1.808 seconds. They check the
even determinant identity, the full fifth-power coefficient
discrepancy, and a direct formal-chart Jacobian that fails the
required constancy. The formal example is not claimed actual.
[Verification161](research/verification-pass161-working.json) and
[checkpoint161](research/checkpoint-pass161-working.json) preserve
the written proof, separate AI reconstructions and terminal evidence.

The full cancellation conjecture remains unsolved. The next work
is integral denominator removal or a justified actual coordinate
change in the remaining graph cases. No human expert review,
formal proof certification or novelty clearance is claimed.

## Previous investigation: generic graph and quartic restrictions

The [quartic restriction160](research/cusp-nongraph-quartic-restriction-pass160-working.md)
shows that a nonlinear first projection in the nonzero-r cusp branch
would force fixed generic degrees (2,4). Its coefficient equations then
force the reciprocal of r to be a shifted fifth power plus a constant.
This is a necessary condition, not an actual realization or exclusion.

The [zero-r reduction160](research/cusp-zero-r-generic-graph-pass160-working.md)
settles the other generic branch: the next determinant coefficient
makes y an affine parameter when n_rho is nonzero. When n_rho is
zero, the earlier chart instead makes w an affine parameter.
Neither conclusion removes denominators in the original ring.

Six finite exact methods passed in two terminal runs. They check
coefficient identities, an abstract plane inverse, and a separate
actual zero-r cusp boundary.
[Verification160](research/verification-pass160-working.json) and
[checkpoint160](research/checkpoint-pass160-working.json) record the
complete written arguments, separate AI reviews and execution evidence.

The subsequent161 parity exclusion is recorded above; it is not part
of this160 packet. The full cancellation conjecture remains unsolved.
Global coordinate descent, formal certification, human expert review
and novelty clearance remain absent.

## Previous investigation: the actual cusp chart and its selected factor

The [actual chart159](research/cusp-generic-chart-first-reductions-pass159-working.md)
derives the remaining cusp case over its exact coefficient field.
The original polynomial inverse gives a calibrated constant Jacobian.
In the nonzero-r branch, successive coefficient identities produce a
plane relation of degree at most four, with a unit gradient on the
selected whole affine line.

The [factor reduction159](research/cusp-generic-selected-factor-reduction-pass159-working.md)
handles the possibility that this equation has extra factors.
An extra factor can occur only when the first projected coordinate
is constant or an affine generic parameter. Otherwise the whole
relation is the irreducible equation of the selected line.
This does not make that parameter a global polynomial coordinate.

Four exact methods passed in 0.433 seconds. Three use formal
coefficient and factor controls; one checks both polynomial inverse
orders in an actual cusp example, so that form cannot be excluded
altogether. The example already has a coordinate slice.
[Verification159](research/verification-pass159-working.json) and
[checkpoint159](research/checkpoint-pass159-working.json) record the
source hashes, independent AI reviews and terminal execution.

The subsequent160/161 restrictions are recorded above; they are not
part of this159 packet. The full cancellation conjecture remains
unsolved. Integral denominator removal, human expert review, formal
certification and novelty clearance remain absent.

## Previous investigation: general weight bounds and cubic correction limits

The [positive-weight proof158](research/arbitrary-positive-weight-initial-bound-pass158-working.md)
now applies to any supplied sliced four-frame with all four time degrees
positive. If its generated initial algebra has a height-one prime kernel,
the relation has weight at most the sum of the time degrees minus two.
The proof also determines which coordinate partials attain maximal
shift. This is a necessary condition, not a bound on the degree sum
or a method for finding better coordinates.

The [split-cubic obstruction158](research/split-cubic-invariant-correction-obstruction-pass158-working.md)
rules out every invariant correction of XZ+YW by lower-weight terms:
such a polynomial has a unique nondegenerate critical point, forcing
any derivation that fixes it to vanish there, contrary to a global slice.
The actual split-cubic frame itself is not excluded.

For the other cubic form, the [integral-intercept gate158](research/cusp-cubic-low-weight-invariant-gate-pass158-working.md)
shows that any nonconstant invariant of weight at most three must
involve the fourth coordinate with nonzero constant coefficient.
It would therefore be an actual invariant coordinate and recognize
the kernel. Existence of that invariant remains unproved.

All nine new exact methods passed across three separate runs.
[Verification158](research/verification-pass158-working.json) and
[checkpoint158](research/checkpoint-pass158-working.json) preserve the
proof assumptions, independent AI reconstructions and terminal evidence.
Finite computations do not certify the universal arguments.

The full cancellation conjecture remains unsolved. The current next
step is the actual cusp generic chart and its remaining correction
conditions. Human expert review, formal verification and novelty
clearance are still absent.

## Previous investigation: the two-linear/two-quadratic frontier

The [initial-bound proof157](research/two-linear-two-quadratic-initial-bound-pass157-working.md)
now restricts the genuine E-time pattern (1,1,2,2). If its generated
initial algebra has exactly one prime relation, that relation has
weighted degree at most four. Weight two gives an actual coordinate
change into the recognized three-good case. The proof separately shows
that every quadratic variable occurring in that relation has maximal
selected-partial shift three; looking for a smaller shift there cannot
close the remaining cases.

The [cubic normal forms157](research/two-linear-cubic-normal-forms-pass157-working.md)
reduce weight three to XZ+YW or XZ-Y^3 through actual polynomial changes.
An explicit sliced frame realizes the first form while its actual
polynomial is not invariant. This prevents a false shortcut, not the
possibility of proving recognition by an additional correction.

Four new exact methods passed in 0.412 seconds. They check actual
two-sided inverses, selected shifts, the cubic boundary, and the failure
of principal multiplicity when there are two initial relations.
Separate synthetic controls are explicitly not claimed as actual frames.
[Verification157](research/verification-pass157-working.json) and
[checkpoint157](research/checkpoint-pass157-working.json) preserve the
written arguments, separate AI reviews, exact source hashes and terminal
run. Finite checks do not certify the universal proof.

Weight-three/four relations and the lower-rank initial algebra remain
unrecognized in general. Arbitrary-coordinate entry and full cancellation
remain unsolved. There has been no human expert review, formal proof
verification or novelty clearance.

## Previous investigation: every supplied three-good frame

The [all-degree synthesis156](research/three-good-all-degree-recognition-pass156-working.md)
now covers a sliced action on C^[4] whenever three supplied polynomial
coordinates are affine in its slice parameter. There is no degree bound
on the fourth coordinate. This restricted working theorem combines the
new dense-case argument with the retained rank-one and conical proofs.
It does not construct such coordinates for an arbitrary action.

The [arbitrary-chain obstruction156](research/arbitrary-chain-gradient-obstruction-pass156-working.md)
excludes every nonlinear chain of length at least three. One leading
coefficient comparison bounds the coefficient derivatives. Evaluating
the differentiated identity on a critical fiber then gives a strict
degree contradiction. The [exact extraction156](research/dense-all-degree-chain-recognition-pass156-working.md)
uses AMS degree divisibility over the original coefficient field to
show that every nongraph has a literal chain in the required axes.
The separate two-stage exclusion154 completes that case split.

Three new finite exact methods passed in 0.735 seconds. They check
short mixed-degree chains, critical-fiber derivatives and a valid
length-two boundary. The [verification156](research/verification-pass156-working.json)
and [checkpoint156](research/checkpoint-pass156-working.json) record the
complete proof dependencies, separate AI reviews and terminal run.
Neither those reviews nor the finite checks certify all retained
arguments. Human expert review, formal verification and novelty
clearance are still absent.

The full cancellation conjecture remains unsolved. The next investigation
is the genuine flow-degree pattern (1,1,2,2), not an older adjoint-degree
pattern with the same numbers. A hypothetical counterexample has minimum
degree sum at least six, and only that pattern is possible at equality.
There is no proved universal upper bound on this minimum.

## Previous investigation: a three-stage coefficient obstruction

The [three-stage proof155](research/three-stage-gradient-obstruction-pass155-working.md)
excludes every specified three-stage placement with nonlinear stages,
using just one coefficient-gradient identity. Comparing two successive
powers of the middle residual would force a nonconstant derivative to
equal a nonzero field constant. The result is algebraic over a
differential field; its application to the actual dense frame includes
the precise canonical second-tail degree and parameter hypotheses.

Two independent finite methods passed in 0.788 seconds, checking full
parameter jets in four degree triples and a valid degree-one boundary.
Separate AI reviews found no gap in the written conditional proof.
[Verification155](research/verification-pass155-working.json) and
[checkpoint155](research/checkpoint-pass155-working.json) preserve the
exact sources, terminal run and scope. Neither finite tests nor AI
reviews are formal proof certification or human expert review.

An arbitrary-length extension and its exhaustive placement argument
are separate156 work still under review. They are not results of this
completed packet. The full cancellation conjecture and arbitrary entry
into the supplied coordinate setting remain unsolved.

## Previous investigation: all two-stage nongraphs excluded

The [two-stage proof154](research/two-stage-nongraph-continuation-pass154-working.md)
excludes every specified fixed-axis equation
Phi=B(V-A(U))+ell*U+n with both polynomial degrees at least two.
This is conditional on the supplied actual dense three-good frame.
Coefficient comparison rules out inner degree above two. In inner
degree two, the exact canonical coefficients and an actual polynomial
inverse give two invariant coordinates. The original third-good
identity then contradicts parity at a linear coordinate prime.

The [semiprime corollary154](research/semiprime-generic-degree-recognition-pass154-working.md)
shows that when the generic degree mu+1 is a product of two primes,
every nongraph would have exactly this fixed-axis two-stage form.
It follows that the generic curve is a graph, and the retained153
recognition proof gives A=C^[3]. In particular minimum mu=5 is now
recognized in this setting. No coefficient-dependent plane change
is silently transported into the original polynomial ring.

Three new exact methods passed in 1.394 seconds. They check both
polynomial inverse orders, behavior at x=0, formal Taylor/Laurent
cancellations and finite coefficient identities. Those checks do
not prove the universal arguments. The written deductions received
separate AI reconstructions, not formal or human expert verification.
The [verification154](research/verification-pass154-working.json) and
[checkpoint154](research/checkpoint-pass154-working.json) preserve the
sources, reviews, terminal execution and exact scope.

Longer-chain arguments are separate155 work, not completed154 claims.
The next unrecognized dense minimum in this packet is mu=7.
Arbitrary-coordinate entry and the full cancellation conjecture
remain unsolved. Novelty has not been established.

## Previous investigation: new global recognition cases

The [leading-normalization proof153](research/dense-all-degree-leading-normalization-pass153-working.md)
now treats every fixed-good minimum degree m>=2 in the supplied
dense three-good setting. An actual complex coordinate change
puts the initial relation in the form XW-gamma Y^(m+1).
Here the minimum is over polynomial shears of the last coordinate
that keep the three good coordinates fixed.

The [graph-correction proof153](research/dense-all-degree-graph-correction-pass153-working.md)
then constructs an invariant ambient coordinate whenever the
generic embedded line is a graph in those normalized axes.
The [all-degree suspension proof153](research/normalized-suspension-recognition-pass153-working.md)
gives explicit polynomial generators of A in that case. This is
global recognition, including the previously exceptional divisor,
not just recognition on an open set.

The graph condition follows automatically when m+1 is prime.
Minimum m=3 is also resolved: its only other generic degree pair
is (2,4), and the [nested-quartic proof153](research/nested-quartic-exclusion-pass153-working.md)
excludes it. An explicit Nagata-type transformation gives two
invariant coordinates; the third-good identity would then make
a nonconstant affine-linear coordinate polynomial a rational square.
Its prime valuation rules that out.

Thus m=3 and m=4 are newly covered, as are all graph cases in
arbitrary degree and every prime generic degree. The next
unrecognized dense minimum in this record is m=5, specifically
its nongraph alternatives. A possible two-stage extension is
still a follow-up, not part of the completed153 claims.

Five new exact methods passed in 0.513 seconds, covering
inverse-verified examples of minimum2,3,4, normalization inverses,
the Nagata inverse, complete quartic Taylor identities and
separately labeled synthetic boundary controls. Those finite
checks do not prove the universal theorems. Separate AI
reconstructions found no gap in the written arguments; no
human expert review, formal proof verification or novelty
clearance has occurred.
The [verification153](research/verification-pass153-working.json)
and [checkpoint153](research/checkpoint-pass153-working.json)
record the final sources, proof dependencies, reviews and terminal run.

The arbitrary-coordinate entry problem and remaining nongraph
degrees are unresolved. These conditional results do not solve
the full cancellation conjecture.

## Previous investigation: an explicit exceptional-divisor exponent

The [bound152](research/effective-selected-plinth-bound-pass152-working.md)
proves alpha divides (Omega rad(Omega))^(mu+1) for the primitive
first-image plinth under the actual dense139/151 hypotheses.
Two finite exact methods passed. A nonconstant derivative value
is not a slice; this bound by itself does not remove the divisor.
The [verification152](research/verification-pass152-working.json)
and [checkpoint152](research/checkpoint-pass152-working.json)
preserve the exact source, terminal run and scope.

## Previous investigation: an actual polynomial coordinate off a specified divisor

The [all-degree proof151](research/dense-all-degree-primitive-jacobian-factor-pass151-working.md)
constructs a polynomial coordinate on the entire open set where
the speed determinant Omega is nonzero. In the actual dense
three-good setting, with intrinsic base S=C[P,Q], it proves
A_Omega=S_Omega[r]. In particular, every full divisor constant
extension away from Omega=0 is trivial. If Omega is a nonzero
constant, the conclusion is global: A=C^[3].

The key step is regularity of the coefficient derivatives and
the canonical Taylor coefficients on that open set. The corrected
second negative coefficient then supplies actual local slices,
which patch with invariant coefficients. This is stronger than
the previously established freeness statement. It does not assume
that a free action automatically has a slice.

Two new exact methods passed in 0.780 seconds. A separate
[failed-construction proof151](research/nonsliced-top-three-good-gate-pass151-working.md)
has three passing exact methods and shows why a genuine sliced
pair with a nonsliced top still cannot supply the required three
coordinates. The [verification151](research/verification-pass151-working.json)
and [checkpoint151](research/checkpoint-pass151-working.json)
distinguish written proofs, finite tests and separate AI reviews.

This is a conditional partial result, not a solution or a novelty
claim. The determinant-zero divisor and entry into the three-good
setting from an arbitrary sliced action remain open. There has
been no human expert review or complete formal verification.

## Previous investigation: arbitrary triangular polynomials and rational exceptions

The [rank-two exclusion150](research/base-dependent-nonlinear-intercept-exclusion-pass150-working.md)
now covers every polynomial H(p,x) in the displayed embedding
p=y-R(x), q=a(p)z-H(p,x), with nonlinear R and nonconstant a.
Nilpotence of the original speed Jacobian forces polynomial
coefficient speeds in C[p,q] to have field rank at most one.
The note also classifies all rational rank-two exceptions and
checks a genuine inverse showing why the polynomial-coefficient
assumption cannot be replaced by ambient polynomiality.

Four exact tests passed in 0.207 seconds. The
[verification150](research/verification-pass150-working.json) and
[checkpoint150](research/checkpoint-pass150-working.json) separate
the written arguments, finite checks and independent AI reviews.
The ambient polynomial exception overlaps established nilpotent-map
normal forms; no historical novelty is claimed.

The [structural audit150](research/selected-divisor-and-entry-gaps-pass150-working.md)
explains the two remaining general steps: proving the required
full-divisor statement without the special placement, and obtaining
the three-good coordinate setting from an arbitrary sliced action.
The W=u applications already have polynomial A. These family
results do not solve cancellation or show that its general gaps
are nearly closed.

## Previous investigation: nonlinear placements and an exceptional divisor

The [nonlinear projected exclusions149](research/nonlinear-projected-plane-obstructions-pass149-working.md)
rule out two specified nonlinear placements. One quadratic family passes
the generic rank test but fails on a surviving exceptional divisor.
The [intercept classification149](research/nonlinear-intercept-triangular-kernel-exclusion-pass149-working.md)
also handles one nonlinear intercept shear, with its coefficient
polynomial independent of the base variable.

The [generic criterion and scope note149](research/generic-critical-determinant-and-relative-scope-pass149-working.md)
explains why a generic unit minor ideal does not prove divisor descent.
It also extends148 to quotient-preserving nonlinear changes, without
claiming that arbitrary changes preserve the quotient.

Three exact tests passed in0.149 seconds. The
[verification149](research/verification-pass149-working.json) and
[checkpoint149](research/checkpoint-pass149-working.json) preserve the
conditional proofs and their scope. These are restricted exclusions,
not a solution to cancellation or a verified novelty claim.

## Previous investigation: excluding triangular residue models in specified frames

The [conditional exclusion148](research/triangular-residue-frame-exclusion-pass148-working.md)
rules out the standard triangular residue-extension models when their
two projected goods have any constant-affine placement in the specified
chart coordinates. The triangular equation may have arbitrary polynomial
base dependence and a multiple coefficient root. No bound on the last
original coordinate's time degree is used.

The proof combines a necessary Jacobian rank condition with a local
Laurent-coefficient argument, generic-line generation and divisor
noncollapse. A [separate line-family classification](research/line-family-triangular-kernel-exclusion-pass148-working.md)
also excludes these embedded speed subrings when the last coordinate
is the actual slice. Neither statement covers arbitrary nonlinear
placements or proves that every divisor residue extension is trivial.

Four exact tests passed in 266.951 seconds. The
[verification148](research/verification-pass148-working.json) and
[checkpoint148](research/checkpoint-pass148-working.json) distinguish
the conditional written proofs, finite formal controls and separate
AI reviews. Full cancellation, human verification and novelty clearance
remain unresolved.

## Previous investigation: a bound on all full divisor fibers

The [all-degree residue bound147](research/dense-all-degree-divisor-residue-bound-pass147-working.md)
works with the full invariant algebra, not just its projected plane
model. Every prime-divisor fiber is a polynomial line over a finite
extension of its coefficient residue field. The extension degree is
at most mu+1, where mu is the smallest last-coordinate time degree
obtainable by a polynomial shear in the fixed three good coordinates.

The proof chooses a nonvanishing good speed separately at each divisor,
so the bound also covers divisors omitted by an initially chosen chart.
A surviving projected coordinate of generic degree one gives local
polynomial recognition. The finite residue extensions are not proved
trivial in general. This extends the scope of the earlier91 argument;
it is not a new general valuation theorem or a solution to cancellation.

Two new exact methods passed. The
[verification147](research/verification-pass147-working.json) and
[checkpoint147](research/checkpoint-pass147-working.json) separate
the proof, retained geometric dependencies, model reviews and finite
tests. Global descent, arbitrary coordinate entry and independent
human/priority review remain outstanding.

## Previous investigation: an actual counterexample to the proposed descent step

The [divisorial counterexample146](research/divisorial-descent-audit-pass146-working.md)
shows that a primitive generic first-tail equation can split into two
lines at an unremoved coefficient divisor, even in a genuine polynomial
coordinate frame. The original invariant algebra is still polynomial.
Its additional projected coordinate removes the extra component, with
an explicit two-relation presentation and open-cover calculation.

A [second actual control146](research/actual-descent-controls-pass146-working.md)
separates a different issue: its curve equation descends everywhere,
but the canonical normalized parameter has a pole. The
[source comparison146](research/divisorial-descent-literature-pass146-working.md)
records precisely why the available residual-coordinate and fibration
theorems do not bypass either distinction.

Four new exact methods passed. The
[verification146](research/verification-pass146-working.json) and
[checkpoint146](research/checkpoint-pass146-working.json) preserve
the evidence. These are counterexamples to proposed proof shortcuts,
not to cancellation or the generic primitivity result145. The next
target is the full invariant algebra's divisor fibers and their
possible finite residue-constant extensions.

## Previous investigation: the first-tail factor gap closes in the retained chart

The [working proof145](research/common-gauss-integrality-tail-primitivity-pass145-working.md)
uses one common degree-at-infinity valuation and polynomial integrality
of actual invariants to show that the first tail has exactly the selected
simple irreducible factor. It also proves that the fixed Taylor data
recover the full intrinsic coefficient field. This supersedes the
automatic-compatibility, inactive-factor and missing-coefficient gaps
listed in the historical entries below, within the retained chart only.

Together with139/141, the result identifies the fixed-good shear minimum
with the generic embedded-curve degree minus one. The
[verification145](research/verification-pass145-working.json) records
four passing exact test methods, their limited scope and the model
reviews. The [checkpoint145](research/checkpoint-pass145-working.json)
preserves the proof and source hashes.

The next investigation tests descent at special coefficient values.
Generic primitivity does not by itself remove denominators or produce
coordinates on the original variety. Global descent, arbitrary
coordinate entry and full cancellation remain unresolved. These are
private AI-reviewed working arguments, not human peer review, formal
verification or a novelty determination.

## Previous investigation: trace comparison and exact compatible factors

The [trace proof144](research/dense-base-compatible-trace-rigidity-pass144-working.md)
removes the equal-constant-field assumption from143. On every active
component, returning the two source speed ratios is equivalent to
agreement of the formal and transported normalized actions. This still
assumes the two return identities; it does not prove them automatic.

The [closed-fiber proof144](research/closed-tail-field-parallel-fibers-pass144-working.md)
then identifies the compatible components exactly: they are the factors
of the minimal source equation over the tail-coefficient field.
The actual polynomial invariant projection closes that fiber. A known
Parallel Lines Lemma puts its equation in one coordinate. This classical
normal form is cited as published mathematics, not claimed as new.

The [projected-ring criterion144](research/projected-ring-equality-and-formal-boundary-pass144-working.md)
shows that the projected polynomial ring equals the original invariant
ring precisely when the selected speed is constant. Its formal boundary
separates polynomial source data from a genuine coordinate inverse.
A [two-recovery exclusion144](research/two-recovery-linear-coupling-exclusion-pass144-working.md)
also closes one larger construction family without bounding the last
coordinate's degree.

Six new exact test methods passed. The
[verification144](research/verification-pass144-working.json) and
[checkpoint144](research/checkpoint-pass144-working.json) retain
their terminal evidence, proof reviews and scope limits.
Automatic base compatibility, full first-tail primitivity, global
descent, arbitrary coordinate entry and cancellation remain unsolved.
These are private AI-reviewed working arguments, not human peer review
or a novelty determination.

## Previous investigation: polynomial return and two distinct compatibility gaps

The [polynomial-fiber proof143](research/polynomial-coefficient-fiber-presentation-pass143-working.md)
strengthens142: the actual inverse supplies four polynomial invariant
equations whose ideal is exactly the intended curve ideal, without
denominators or saturation. It still does not make those equations
automatic consequences of the first tail.

The [conditional stabilizer theorem143](research/dense-base-compatible-component-stabilizer-pass143-working.md)
compares the formal and actual normalized actions when a component has
the same algebraic constants and fixes the two initial speed ratios.
Those components correspond exactly to coefficient-field automorphisms
fixing all tail data.
The [degree and norm theorem143](research/tail-coefficient-field-degree-pass143-working.md)
bounds any coefficient extension omitted by those data: its degree
times the selected curve degree cannot exceed the first-tail degree.

Two formal examples keep the conditions separate. The cubic example in
the degree note enlarges the constant field despite a trivial
automorphism group. The
[base-mismatch example143](research/formal-base-incompatible-tail-pass143-working.md)
keeps that field unchanged but changes one speed ratio. Both fail the
actual inverse premise; neither is a cancellation counterexample.

The [recovered-invariant template143](research/recovered-invariant-template-rigidity-pass143-working.md)
also classifies a broader explicit non-autonomous construction. Every
dense surviving actual member has a primitive tail, even with arbitrary
finite coefficient-cover degree and a varying first selected speed.
This remains one construction template, not the unrestricted case.

Seven new exact methods passed. The
[verification143](research/verification-pass143-working.json) and
[checkpoint143](research/checkpoint-pass143-working.json) preserve
the proofs, scope limits and terminal test evidence. The next target is
actual base-ratio return or an actual inverse-verified counterexample.
Full cancellation, global descent and arbitrary coordinate entry remain
unsolved here. No human expert verification or novelty claim is implied.

## Previous investigation: exact source compatibility, not yet automatic compatibility

The [coefficient criterion142](research/dense-tail-coefficient-compatibility-pass142-working.md)
gives three explicit rational identities that select the intended
generic-line component. They retain both speed ratios and a primitive
element of their finite coefficient extension.

The [stronger ring proof142](research/source-generic-fiber-saturation-pass142-working.md)
shows that these equations recover the entire generic-line scheme after
their common denominator is inverted, with no first-tail equation needed.
An actual family explains why the primitive-element condition cannot
simply be omitted. Its first tail is already primitive; it is not a
counterexample to actual first-tail primitivity.

A [separate construction boundary142](research/autonomous-two-quasi-suspension-boundary-pass142.md)
rules out autonomous two-quasi exponential suspensions as a source of
an unwanted actual tail factor, using a published classification.
Four new exact test methods passed in14.503 seconds. The
[verification142](research/verification-pass142-working.json) and
[checkpoint142](research/checkpoint-pass142-working.json) record
the proof reviews, correction of an initial weaker draft, and test scope.

The central gap is unchanged: the original inverse has not been shown
to force the compatibility equations on every first-tail component.
Global descent and arbitrary coordinate entry are also unresolved.
Full cancellation is not solved; these are private AI-reviewed working
arguments, not a novelty claim or human expert verification.

## Previous investigation: an exact shear minimum and the remaining inverse gate

The [fixed-good shear theorem141](research/dense-shear-minimal-tail-pass141-working.md)
proves that adding any complex polynomial in the first three coordinates
to the last coordinate leaves both formal tails unchanged. It also
constructs a minimizing correction: the least possible last-coordinate
time degree is exactly one less than the first-tail degree.

In the [linear-tail regime](research/linear-first-tail-recognition-pass141-working.md),
this gives an actual invariant coordinate. A published nice-derivation
theorem then identifies A with a polynomial three-ring. This is a
sufficient criterion, not a claim that every tail is linear.

The [component-persistence lemma141](research/dense-tail-component-persistence-pass141-working.md)
shows why the remaining inverse condition matters: on any first-tail
component where the second tail is transcendental over the coefficient
field, all later formal recurrences follow automatically. They do not
make that component a branch of the original polynomial inverse.
The [uniform formal family141](research/formal-tail-inverse-branch-family-pass141-working.md)
exhibits that distinction in every degree.

Six new exact test methods passed. The
[verification141](research/verification-pass141-working.json) and
[checkpoint141](research/checkpoint-pass141-working.json) distinguish
finite tests, written arguments and external classification inputs.
Actual first-tail primitivity, the remaining global descent, arbitrary
coordinate entry and full cancellation are still unresolved.
These are internally reviewed working results, not expert-reviewed
or proof-assistant-verified claims of novelty.

## Previous investigation: actual boundaries for generic-coordinate descent

The [actual sharp family140](research/sharp-dense-tail-family-pass140-working.md)
attains the two tail-degree bounds from139. It also disproves one
specific shortcut: the second tail supplies a parameter on the
generic line, but need not complete its defining equation to a plane
coordinate system, even when the original four-coordinate inverse
is polynomial.

A separate [actual field-extension family140](research/unbounded-actual-coefficient-field-pass140-working.md)
has last-coordinate time degree one and coefficient-field extension
degree equal to any integer n>=2. Thus actual invertibility does not
make the coefficient field equal to the speed-ratio field, and the
time degree alone does not bound that extension.

The [formal tail obstruction140](research/dense-tail-coordinate-obstruction-pass140-working.md)
satisfies the entire Taylor system but has a reducible first tail.
It fails the actual polynomial-inverse premise. Consequently it
does not decide whether an actual frame can have that extra factor.
That precise actual-frame question is the next bounded target.

All four methods of the new
[exact checker140](research/sharp_dense_tail_controls_pass140.py)
passed. The arbitrary-degree and arbitrary-extension statements
have written proofs; they are not inferred from those samples.
The [verification140](research/verification-pass140-working.json)
and [checkpoint140](research/checkpoint-pass140-working.json)
record the distinction. These examples are recognized translations,
not cancellation counterexamples or a solution to global descent.

## Previous investigation: an all-degree generic line with degree bounds

The [dense generic-line proof139](research/dense-generic-embedded-line-pass139-working.md)
gives a nonzero plane relation of degree at most m+1 and a polynomial
generic-line parameter of degree at most m+2, where m is the last
coordinate's time degree. Its
[actual Taylor chart](research/dense-all-degree-taylor-chart-pass139-working.md)
and [negative-tail argument](research/dense-negative-tail-relations-pass139-working.md)
retain the exact finite separable coefficient field.

The primitive implicit degree equals the maximum of the two generic
coordinate degrees, hence is at most m+1. Classical plane
epimorphism then makes that equation a coordinate over the
coefficient field. None of these conclusions removes invariant
denominators or supplies original complex polynomial coordinates.
The [verification139](research/verification-pass139-working.json)
records four passing finite methods and internal proof reviews;
the [checkpoint139](research/checkpoint-pass139-working.json)
preserves the remaining global and arbitrary-entry gaps.

## Previous investigation: the nonlinear conical case needs no degree bound

The [working all-degree exclusion138](research/all-degree-conical-exclusion-pass138-working.md)
removes the last-coordinate degree restriction from the nonlinear
homogeneous rank-two speed case. An actual sliced fourfold with
three E-affine coordinates cannot have that speed profile, regardless
of the fourth coordinate's finite E-degree.

The [actual chart recurrence](research/all-degree-conical-chart-pass138-working.md)
first recovers the whole generic line. A separate
[weighted coefficient lemma](research/weighted-coefficient-polynomiality-pass138.md)
then supplies a monic relation over a one-variable invariant field.
The exact monic-pencil descent and slice obstruction finish the
restricted contradiction. The intermediate correction has degree
at most twice the last coordinate's E-degree.

An [arbitrary-degree family without a slice](research/higher-degree-no-slice-boundary-pass138.md)
shows the hypothesis boundary. The new
[exact checker](research/all_degree_conical_controls_pass138.py) passed
three methods covering formal coefficient identities and actual
examples at degrees three, four and five. Those finite tests do not
prove the universal theorem. The
[verification138](research/verification-pass138-working.json) and
[checkpoint138](research/checkpoint-pass138-working.json) separate
the written argument, internal reviews, finite controls and remaining gaps.

The dense-speed case beyond quadratic last degree is still unresolved.
Obtaining the three-good coordinate profile from an arbitrary cylinder
is also unproved. Full cancellation, human expert validation and
historical novelty clearance remain outstanding.

## Previous investigation: the supplied three-good quadratic profile is covered

The [case-coverage theorem137](research/three-good-quadratic-profile-recognition-pass137.md)
combines the recorded working proofs to recognize every sliced
polynomial fourfold supplied with three coordinates killed by E squared
and a fourth killed by E cubed. Under that actual coordinate assumption,
the kernel is C^[3]. The proof-dependency table states which older
arguments each case retains.

The new [speed-based conical proof137](research/universal-conical-tangent-reduction-pass137.md)
removes136's nonradial assumption. The selected speed cofactor forces
the tangent graph even in resonance. The resulting monic descent and
linear-invariant obstruction exclude the nonlinear rank-two conical
case entirely within this profile.

An [explicit action without a slice](research/conical-no-slice-boundary-pass137.md)
shows why the slice hypothesis matters. Its polynomial inverse,
resonant nonlinear cone and nonunit derivative ideal are checked exactly.
It is not a cancellation counterexample. The
[verification137](research/verification-pass137-working.json) separates
this actual boundary example from the formal coefficient controls.

This does not solve general cancellation: no proof supplies the stated
coordinate profile from an arbitrary cylinder. Nor does it settle every
abstract partial-height-eleven profile. The
[checkpoint137](research/checkpoint-pass137-working.json) records that
remaining entry problem, inherited source dependencies, and the lack
of human expert review, formal verification and novelty clearance.

## Previous investigation: the nonradial conical branch is excluded

The [working nonexistence proof136](research/conical-nonradial-quartic-coordinate-pass136-working.md)
rules out the nonradial alternative in every supplied sliced
three-good quadratic frame with nonlinear conical speed rank two.
Such a frame would produce a genuine invariant coordinate
W+P(X,Y,Z), with P of degree at most four. A published generic
linear-invariant theorem then forces its speeds to have transcendence
degree at most one, contradicting the assumed rank two.

The proof uses an
[actual localized tangent graph](research/conical-mismatch-tangent-graph-reduction-pass136.md),
[polynomial coefficient bounds over an exact one-variable field](research/conical-mismatch-coefficient-polynomiality-pass136.md),
and a full monic rational-pencil descent to the original polynomial ring.
It does not replace a rational field generator by a polynomial one or
select an algebraic component and treat it as the complete generic equation.

The [verification136](research/verification-pass136-working.json) records
six passing new exact test methods and independent AI proof reconstructions.
The formal test data are not examples of the now-excluded branch.
The [checkpoint136](research/checkpoint-pass136-working.json) records the
then-remaining resonant branch and arbitrary coordinate-entry problem.
The former is now excluded within the supplied profile by137 above.
Human expert review, formal verification and novelty clearance remain
outstanding. Full cancellation is not solved.

## Previous investigation: a sharper conical case split

The [conical frontier135](research/conical-branch-frontier-pass135-working.md)
separates the next unresolved supplied-frame sector into two cases.
The [selected-adjoint proof](research/conical-three-good-adjoint-degree-pass135.md)
lowers the bad partial's degree to at most one, including its coefficient
on the original slice. It needs no bound on the last coordinate's time degree.

For quadratic acceleration, the Euler derivation R of the homogeneous
speed field supplies the split. If Rq differs from 2q, the
[nonradial proof](research/conical-nonradial-degree-bound-pass135.md)
forces the nonlinear cone equation to have degree two or three.
If Rq equals 2q, the
[resonance proof](research/conical-resonant-good-partial-bounds-pass135.md)
bounds each good partial's degree by two, giving partial height at most
eleven. The further exclusion of lower heights uses the separate retained
height-ten working theorem. Height eleven is not recognized here.

These historical reductions were not a proof of cancellation for the
remaining conical sector. The nonradial alternative is now excluded
by136 above; its resonant alternative remains outside that packet.
Neither a general coordinate-entry theorem,
human expert review, formal verification, nor novelty clearance is supplied.
The [verification135](research/verification-pass135-working.json) records
four completed targeted test methods, distinguishing three formal controls
from one retained inverse-verified family. The
[checkpoint135](research/checkpoint-pass135-working.json) preserves the
remaining obligations and the next bounded investigation.

## Previous investigation: primitive corrections and direct recognition

The [working proof134](research/primitive-cubic-correction-existence-pass134-working.md)
closes both lower correction conditions in every supplied actual
sliced, dense, rank-two, three-good quadratic frame whose acceleration
is outside the constant quadratic speed span. It produces an invariant
of original weight three, then an explicit normalized cubic coordinate.
The retained algebraic classification132 gives a nonzero constant
leading speed and a polynomial kernel in this restricted class.

The proof first extends the
[pure-cube restriction through invariant localization](research/primitive-binary-cubic-localization-rigidity-pass134-working.md).
It then excludes a
[generic line component](research/primitive-generic-line-exclusion-pass134-working.md).
The remaining cubic graph and its unit Jacobian put all coefficients
in a one-variable invariant field. The
[exact rational-pencil lemma](research/rational-pencil-weight-descent-pass134-working.md)
bounds a rational generator's numerator and denominator by weight three.
One is nonconstant, supplying the invariant. A final coefficient
comparison makes the coordinate change explicit.

This chain uses the original positive coordinate filtration throughout.
It does not assume a polynomial rational-field generator, cancel factors
in a normal graded ring, or treat a component over a larger field as
the whole generic equation. Its direct final normalization avoids the
earlier invariant-suspension topology theorem130. The classical
Lüroth theorem and Wang classification remain stated source inputs.

The [verification134](research/verification-pass134-working.json) records
29 passing targeted exact methods, ten new and nineteen retained, and
separates those finite controls from the universal written argument. Three
independent AI reconstructions found no defect in the correction proof
and its final normalization. This is not human expert review,
proof-assistant verification, or historical novelty clearance.

The [checkpoint134](research/checkpoint-pass134-working.json) records
the finished bounded investigation. Even within supplied quadratic
profiles, the nonlinear conical rank-two sector with variable acceleration
outside the constant-plus-quadratic speed span remains unresolved.
General cancellation also requires handling an arbitrary sliced
polynomial fourfold without assuming this coordinate profile. Do not continue treating
the two primitive correction conditions as an open gap in this class.

## Previous investigation: existence of the quadratic or primitive cubic relation

The [leading dichotomy133](research/three-good-quadratic-cubic-leading-dichotomy-pass133.md)
proves that every supplied actual sliced dense rank-two three-good
quadratic frame has a relation of weighted degree two or three.
Either a quadratic elementary shear removes the acceleration, or
the unique primitive relation L(a)q=2F3(a) exists. This closes the
leading-relation existence gap in this class. It does not prove
the two lower-degree corrections or entry from an arbitrary action.

The proof combines the actual bad partial with a
[multiplicity-sensitive degree estimate](research/three-good-multiplicity-degree-bound-pass133.md).
If an original-weight top contains the initial relation k times,
its E-degree is at least its original weight minus 4k. Applying
this to all invariants excludes higher-degree relations: degree four
would give only linear filtered growth, whereas three independent
invariants give cubic growth. The derivative method is classical;
the note compares it with Vénéreau's primary paper.

A separate [commuting-direction lemma133](research/three-good-commuting-direction-quadratic-invariant-pass133.md)
forces an invariant quadratic bad-coordinate correction when an
ambient constant translation commutes with the action. It sharpens
an already recognized symmetry case, without assuming a global slice.

The [verification133](research/verification-pass133-working.json)
records 19 passing exact test methods and a completed 1,296-word
inverse-checked search. No primitive endpoint occurred in that finite
family. These examples do not prove the universal arguments.
Three independent AI reconstructions found no gap in the written
dichotomy; human review, formal verification and novelty clearance
remain outstanding.

The [checkpoint133](research/checkpoint-pass133-working.json)
records the exact scope and remaining gaps. General cancellation
is still unsolved. Work now proceeds to the two corrections or
the unrestricted coordinate-frame reduction.

## Previous investigation: cubic normal forms and exact adjoint degree

The [normalized classification132](research/normalized-cubic-action-classification-pass132.md)
gives all irreducible actions satisfying the displayed cubic invariant
presentation and derivative bounds. Their distinguished speeds have the
form EX=c*h^3, EY=h^2*g with coprime h,g in C[I]. The reduced fixed locus
is h(I)=X=0. Fixed-point-free members have h=1 and admit an explicit
polynomial straightening. This statement does not assume a slice or a
unit row before deriving the constant-speed conclusion.

Applied after the retained130 normalization, it proves that every
successful primitive correction in a sliced dense frame already has
a nonzero constant-speed affine good direction. This removes the
extra unit-row hypothesis from the
[independent elementary proof132](research/primitive-unit-row-slice-necessity-pass132.md).
It characterizes the successful side but does not prove that an
arbitrary candidate passes the two corrections.

The [general cofactor proof132](research/dense-three-good-adjoint-degree-pass132.md)
also forces the selected bad adjoint degree to be exactly two in every
supplied dense rank-two three-good frame, with no degree bound on the
last coordinate. The former degree-one possibility is excluded in this
dense branch, independently of the cubic classification.
The [two-shear restriction132](research/two-shear-primitive-return-rigidity-pass132.md)
rules out another specified counterexample construction.

The [verification132](research/verification-pass132-working.json) records
thirteen passing exact methods, six new and seven retained. These test
explicit families, inverses, derivative identities and boundary cases;
they are not formal verification of the universal proofs. Wang's
classification was checked in the Dasgupta--Gupta restatement and his
original thesis. Independent AI reconstruction and bounded source
comparison do not establish human approval or novelty.

The [checkpoint132](research/checkpoint-pass132-working.json) records
versions, assumptions and gaps. General cancellation remains unsolved.
Next work must address actual mixed-relation existence or correction
failure/passage in the remaining dense degree-two branch, not search
for a degree-one frame ruled out by the new argument. Entry into any
such coordinate profile remains a separate obligation.

## Previous investigation: stability within the primitive cubic profile

The [working proof131](research/three-good-primitive-profile-orbit-closure-pass131.md)
shows that a successful primitive mixed-cubic correction stays successful
along every finite elementary coordinate word whose intermediate frames
retain three linearly moving coordinates, one quadratically moving coordinate,
and the specified dense speed cone. Its invariant subring C[I] is unchanged.
The proof does not assume the moving coefficient is a unit.

The intermediate restriction is essential. An explicit seven-shear word
leaves this class and returns to it, replacing C[a] by C[a+b]. The total
automorphism even commutes with the sliced derivation. This is a counterexample
to unrestricted invariant-subring preservation, not to cancellation or to
passage of the two derivative tests.

The [verification131](research/verification-pass131-working.json) records
seven passing exact methods, three new and four retained130, and a separate
192-word rational search with both inverse orders checked for every word.
Only nine distinct endpoints meet the search's final profile and relation
filters; all nine pass both corrections. That finite result is not an
absence theorem. Separate AI proof reconstructions are not human review,
formal verification, or novelty clearance.

The [checkpoint131](research/checkpoint-pass131-working.json) records scope
and versions. Searches staying inside this elementary class cannot produce
a primitive correction failure from a successful seed. The next task must
allow profile-leaving paths or prove the derivative tests directly without
assuming such connectivity. General cancellation and unrestricted frame
entry remain unsolved. The deep-research workflow kept the all-word proof,
finite experiments, and explicit limit of the argument separate.

## Previous investigation: an automatic invariant-coordinate criterion

The [all-degree working theorem130](research/invariant-linear-suspension-recognition-pass130.md)
recognizes a sliced action on an actual polynomial four-ring when it fixes
an invariant I=wz-g(y,t), with Ew nonzero and E^2w=0. It proves that g is
a plane coordinate, I is an ambient coordinate, and the kernel is a
polynomial three-ring. There is no degree bound on g or on the action
degrees of y,t,z.

The proof combines the homology of a generic fiber, classical affine
homotopy-dimension and plane-line rectification results, and an integral
rational-flow argument. Explicit counterexamples explain why the slice,
Ew nonzero, and E^2w=0 assumptions cannot simply be dropped.

The [mixed-cubic criterion130](research/three-good-mixed-cubic-correction-criterion-pass130.md)
now has two exact derivative correction tests, not three independent
obstructions: if both tests pass, coordinate recognition follows from
the theorem. Their passage, and existence of a suitable relation in an
arbitrary frame, remain unproved. Unrestricted entry into such a frame
and the full cancellation conjecture remain unresolved.

The [targeted run130](research/verification-pass130-working.json) passed
six methods, four new and two retained129. These are exact example and
boundary checks, not a computational proof of the universal theorem.
Separate AI reconstructions checked the written proof. Neither human
review, formal verification nor historical novelty clearance is claimed.
The deep-research workflow kept classical inputs separate from the
derived conditional statement and made the remaining hypotheses explicit.

The [checkpoint130](research/checkpoint-pass130-working.json) records
the versions and verification scopes. The next proof task is to determine
whether a primitive mixed cubic relation must pass the two corrections,
or construct an actual polynomial-coordinate counterexample if not.

## Previous investigation: fixed-good minimality does not repair the shortcut

The [working proof129](research/three-good-cubic-acceleration-span-obstruction-pass129.md)
answers the next question negatively with an actual polynomial inverse
family. A cubic specialization has good speeds (1,a,b) and acceleration
a cubed, outside their constant quadratic-product span. Its quadratic
last coordinate cannot be simplified by any fixed-good polynomial shear.
The first commutator still fails to preserve the intrinsic speed plane,
even though both that commutator and the intrinsic action have slices.

The proof also identifies the exact first weighted relation. It has
weight three and a nonconstant coefficient on the bad initial, and the
four coordinate initials generate a smaller algebra than the full
associated graded ring. A mixed cubic cancellation recovers an actual
invariant coordinate. This example is therefore a recognized translation,
not a globally minimal frame or a counterexample to cancellation.

The [targeted run129](research/verification-pass129-working.json) passes
four methods: two new and two retained128. The written family proof and
the separate AI reconstructions have not had human expert review or
formal verification. Historical novelty remains unconfirmed. The full
cancellation goal remains active and unsolved. The next bounded task
concerns mixed cubic relations and the exact conditions under which
they yield a genuine invariant coordinate.

The [checkpoint129](research/checkpoint-pass129-working.json) records
the frozen versions, exact test coverage and independent review scopes.

## Previous investigation: a failed rank-two shortcut and exact shear criteria

The [working proof128](research/three-good-rank-two-commutator-instability-pass128.md)
gives an actual polynomial-coordinate example where the first commutator
fails to preserve the intrinsic speed plane. The example meets the unit,
rank-two, nonconical and quadratic-last-coordinate hypotheses. It is
already a translation, not a counterexample to cancellation.

The same note proves exact criteria for commutator preservation and
quadratic simplification while the three good coordinates stay fixed.
Under the specified density premise, every good-only polynomial retains
its ordinary degree as action degree, and the good rational-function
field contains no nonconstant invariant. Any nonlinear replacement of
a good coordinate by another good coordinate must involve the fourth
coordinate. The example's own quadratic
term is removable, so it says nothing against an assertion with an
additional shear-minimality hypothesis.

The [targeted run128](research/verification-pass128-working.json) passes
seven methods: two new and five retained127. Independent AI source
reviews and finite symbolic checks are not human expert review, formal
verification or novelty clearance. The full cancellation conjecture is
still unsolved. The next bounded task is to test the stronger stability
claim under fixed-good shear minimality, without treating an unrealized
coefficient polynomial as an actual coordinate construction.

The [checkpoint128](research/checkpoint-pass128-working.json) records
the frozen proof, checker, capture and independent review scopes.

## Previous investigation: speed-curve recognition without a time-degree bound

The [complete working proof127](research/three-good-speed-curve-recognition-pass127.md)
recognizes a sliced action on an actual polynomial four-ring when three
specified coordinates have zero second derivative and their three
speeds generate a field of transcendence degree at most one. There is
no bound on the fourth coordinate's time degree. The conclusion is
that the kernel is a polynomial three-ring.

The argument constructs an actual invariant ambient coordinate. A
finite-flow determinant identity preserves all divisor multiplicities;
a polynomial normal and a Wronskian degree comparison then produce an
explicit triangular coordinate. The zero-parameter-derivative branch
has an elementary degree proof and no longer requires the separate
nice-three classification theorem. Polynomial curve factorization and
the published regular-kernel recognition theorem remain source inputs.

This closes the speed-rank-one branch, including the narrower
unit-joint-curve recognition gap recorded in126. The separate
[canonical-volume identity127](research/three-good-canonical-volume-factorization-pass127.md)
is additional structure in that narrower presentation, not a required
step or a second cancellation result.

The [source and proof audit127](research/three-good-speed-curve-source-proof-audit-pass127.md)
records separate AI reconstructions and the exact published inputs.
The [targeted run127](research/verification-pass127-working.json) passes
eleven methods in three suites, five new and six retained. Neither AI
agreement nor finite examples are formal verification or expert review.
Historical novelty is unconfirmed.

An [actual rank-two control127](research/three-good-rank-two-quotient-instability-pass127.md)
also rejects a possible next-step shortcut: even a unit-speed case
with the specified intrinsic plane need not have that plane preserved
by the original last-coordinate partial. The example is an explicit
translation, not a cancellation counterexample. Speed rank two and
unrestricted entry into a three-good-coordinate frame remain unresolved,
so the full cancellation goal remains active and unsolved.

The [checkpoint127](research/checkpoint-pass127-working.json) records
the frozen proof versions, independent review scopes and exact test
coverage. The next investigation concerns the first commutator's
action on the rank-two intrinsic plane; no answer is assumed.

## Previous investigation: cofactor bounds and the joint-curve frontier

The [working126 synthesis](research/three-good-cofactor-frontier-pass126.md)
proves rank-sensitive bounds for the original coordinate partials in
a supplied three-good frame. It also recognizes any commuting-original-
partial case, and the speed-rank-one case with a proper selected speed
ideal. Neither recognition gate needs a last-coordinate degree bound.

For a quadratic last coordinate, the general partial-height bound is
fifteen, not eleven. In the joint-rank-one case, a hypothetical
nonpolynomial kernel must have a unit speed ideal and exact partial
profile (2,2,2,1), with height eleven. The new commutator identities
give an actual presentation A=S[Y,F(Y)/a], S=C^[2]. They do not show
that the denominator a is a unit, or recognize the entire curve case.

The [targeted run126](research/verification-pass126-working.json) passes
six methods in two suites, three new and three retained. Separate
AI reconstructions check the written proofs. These are not universal
formal verification, expert review, or historical novelty clearance.
Full cancellation and unrestricted coordinate entry remain unresolved.

The [checkpoint126](research/checkpoint-pass126-working.json) records
the frozen proof versions, exact example-test scope and source limits.

## Previous investigation: common intrinsic quotient and acceleration square

The [working125 synthesis](research/three-good-variable-acceleration-frontier-pass125.md)
constructs an intrinsic additive action fixing all three speeds in any
supplied three-good-coordinate frame, without a bound on the fourth
coordinate's time degree. The retained quotient theorem places those
speeds in the same faithfully flat polynomial plane. In the quadratic
case the acceleration q belongs to that plane too.

This closes the earlier square-membership gap: q squared always belongs
to the good-speed ideal. The proof uses the actual common quotient and
the published dimension-two Briancon-Skoda theorem. A separate support
argument reaches the same conclusion. First-power membership, freeness
of the intrinsic action, recognition of the whole supplied class, and
unrestricted entry remain unresolved.

The [targeted run125](research/verification-pass125-working.json) passed
six methods in three suites, three new and three retained. These check
explicit polynomial inverses, leading coefficients, return identities,
and scope controls, not the universal theorem quantifiers. The proof
notes have separate AI reconstructions. No human expert review, formal
verification, historical novelty clearance, or cancellation solution is
claimed.

The [checkpoint125](research/checkpoint-pass125-working.json) records
the frozen proof versions, source scopes and exact review evidence.

## Previous investigation: testing the unrestricted coordinate reduction

The [working124 synthesis](research/unrestricted-entry-frontier-pass124.md)
shows why two candidate shortcuts do not supply the missing entry:
strictly decreasing one-coordinate shears can stall on known
translations, and a quadratic-time frame can lack every nonconstant
affine-linear zero-acceleration direction. Both controls have complete
polynomial inverses. A six-shear classical stabilization construction
bypasses the first control with an explicit temporary degree increase.

These are verified strategy restrictions, not a new cancellation
theorem. The [source audit](research/source-audit-pass124.md) separates
nearby published recognition hypotheses from the unresolved input.
Under the retained recognition results, a hypothetical counterexample's
minimum coordinate-degree sum is at least five; at five, its profile
must be (2,1,1,1) with nonconstant acceleration. There is no proof that
all counterexamples reduce to this first profile.

The [capture124](research/verification-pass124-working.json) records
eight passing methods in three suites, four new and four retained.
General cancellation remains unsolved. Human expert review, formal
verification and novelty clearance have not occurred.
The [checkpoint124](research/checkpoint-pass124-working.json) records
the frozen artifacts and exact review scopes.

## Previous investigation: the supplied cubic branch is excluded

The [working123 synthesis](research/cubic-exclusion-frontier-pass123.md)
closes the exact cubic branch under the actual original-coordinate
framework90. A potential-pole argument gives Y squared dividing P
cubed. An elementary repeated-fiber argument excludes the triple-root
scalar; a separate Jacobian and degree argument excludes every other
cubic scalar. The null axis was already excluded in122.

Combined with the retained conical, linear and quadratic cases, this
gives a working recognition theorem for an actual polynomial frame
with three zero second derivatives and one nonzero constant second
derivative. It does not establish such a frame for an arbitrary
polynomial cylinder. General cancellation remains unsolved.

The [capture123](research/verification-pass123-working.json) records
six suites/twelve passing methods, four new and eight retained.
The written proofs have separate AI reconstructions, not human expert
review, formal verification or novelty clearance.
The [checkpoint123](research/checkpoint-pass123-working.json) records
the frozen versions and their exact verification scopes.

## Previous investigation: the null axis is excluded, with non-null divisor restrictions

The [working122 synthesis](research/cubic-global-axis-frontier-pass122.md)
excludes the entire null-axis alternative under the supplied actual
exact cubic framework. A constant change of original coordinates turns
the non-null reciprocal type into a cubic type. The remaining non-null
cubic case has strict speed-divisor bounds, and its axis speed must have
a reducible fiber at 1 or -1. A polynomial unimodular speed control still
satisfies those restrictions without supplying an actual frame.

The remaining non-null cubic case, arbitrary-frame entry and general
cancellation are unresolved. The [canonical capture122](research/verification-pass122-working.json)
passes six suites/eight methods, four new and four retained. It supersedes
the recent eight-test status rerun, which was verification progress only,
not a new discovery or additional coverage. The [checkpoint122](research/checkpoint-pass122-working.json)
records the versions and review scopes. AI reconstructions and finite
checks are not human expert review, formal verification or novelty clearance.

## Previous investigation: scalar classification and a null reciprocal exclusion

The [working121 synthesis](research/cubic-scalar-classification-frontier-pass121.md)
forces the remaining scalar metric coefficient D to be either cubic
or quadratic plus a nonzero reciprocal affine-linear term, for both
null and non-null constant axes. Its rationality in the normal ratio
h is proved, not assumed. Polynomial Jacobian divisibility excludes
the reciprocal null-axis case. The surviving null cubic case has a
nonconstant perfect-cube polynomial speed component.

Three axis/type combinations remain unresolved. Explicit polynomial,
unimodular speed controls show why coefficient identities alone do
not exclude them. The actual generic volume is a base-field unit;
upgrading it to a complex constant without normalizing the relative
parameter is invalid. The global original-coordinate reconstruction,
arbitrary-frame entry and full cancellation problem remain unsolved.

The [capture121](research/verification-pass121-working.json) passes
seven suites/nine methods, five new and four retained. Separate
full-file AI reconstructions are clean in the stated scopes, not
human expert review, formal verification or novelty clearance.
The [checkpoint121](research/checkpoint-pass121-working.json) records
the precise artifacts, review evidence and remaining obligations.

## Previous investigation: general cubic metric exclusions and a constant axis

The [working120 synthesis](research/cubic-general-axis-frontier-pass120.md)
removes the coordinate-first-integral premise from the lower-rank and
ruled cubic exclusions. In every remaining actual cubic frame, Q has
rank three, its plane restriction has rank two, and det Q is nonconstant.
A new conic coefficient argument gives a nonzero constant ambient
direction v0 with Qv0 constant. This direction may be null or non-null.

The fixed-direction result is a restriction, not an exclusion of the
remaining case. Its lower volume coefficients and global polynomial
reconstruction remain unresolved, as does arbitrary-frame entry.
The full cancellation problem remains unsolved.

The [capture120](research/verification-pass120-working.json) passes five
suites/nine methods, three new and six retained. Independent full-file
AI reconstructions found no invalidating gap in the stated proofs.
They are not human expert review, formal verification, or novelty
clearance. The [checkpoint120](research/checkpoint-pass120-working.json)
records exact scope, artifact versions and the next proof obligations.

## Previous investigation: the coordinate-first-integral cubic branch is excluded

The [working119 theorem and synthesis](research/cubic-coordinate-field-frontier-pass119.md)
exclude the exact cubic branch whenever its rational first-integral
field is generated by an actual polynomial coordinate of the invariant
plane. A line/rank reduction leaves two cases. The nondegenerate one
contradicts an exact volume coefficient; the other reduces to a
polynomial curve and contradicts original-coordinate irreducibility.
The latter proof now allows a noncoordinate polynomial first component.

The [source and obstruction note](research/cubic-first-integral-polynomial-gates-pass119.md)
separates rational, polynomial and coordinate generators and excludes
common-basepoint pencils with constant geometric affine units. The
extra coordinate-field hypothesis has not been established generally.
Arbitrary-frame entry and the full cancellation problem remain unsolved.

The [capture119](research/verification-pass119-working.json) passes six
suites/twelve methods, five new and seven retained. Separate full-file
AI reconstructions are clean in their stated scopes. These are not
human expert review, formal verification, or novelty clearance.
The [checkpoint119](research/checkpoint-pass119-working.json) records
the artifact versions and remaining proof obligations. Its synthesis
also clarifies that118's velocity-family exclusion is restricted to
the exact cubic branch; the historical files remain unchanged.

## Previous investigation: a global obstruction in the cubic branch

The [working118 synthesis](research/cubic-global-obstruction-frontier-pass118.md)
and [pullback exclusion](research/cubic-polynomial-pullback-exclusion-pass118.md)
exclude exact cubic relative degree for velocities b=(s,p(s,t),f(s)),
with s,t actual invariant-plane coordinates and p_t nonzero. The
proof combines a scalar potential/volume calculation with irreducibility
of an original affine-linear coordinate. It does not require a global
inverse to the polynomial base pullback.

A [general cubic constraint](research/cubic-moving-frame-constraint-pass118.md)
gives a nonconstant rational first integral for the leading cubic
direction. It does not make that integral a polynomial base coordinate.
An [exact principal-open model](research/cubic-principal-open-frame-control-pass118.md)
has a full inverse and unit Jacobian but a genuine slice pole, even
after a pullback makes its speed row unimodular. Local compatibility
alone therefore cannot finish the argument.

The [capture118](research/verification-pass118-working.json) passes four
suites/seven methods, four new and three retained. Separate AI proof
reviews and a bounded [recognition dependency audit](research/nice-recognition-adversarial-dependency-audit-pass118.md)
found no invalidating gap in their stated scopes. They are not human
expert review, formal verification or novelty clearance.
The general cubic branch and arbitrary-frame entry remain unresolved.
The full cancellation conjecture remains unsolved.
The [checkpoint118](research/checkpoint-pass118-working.json) records
the exact artifacts, proof-review scopes and unresolved obligations.

## Previous investigation: an explicit shear for the quadratic branch

The [working117 synthesis](research/quadratic-shear-frontier-pass117.md)
and [six-equation proof](research/quadratic-velocity-shear-pass117.md)
derive a global triangular coordinate change from the exact quadratic
relative relation and the actual unit volume determinant. In the new
frame every original coordinate has zero second derivative. Combined
with the separately retained working nice-slice theorem80, this
recognizes the quadratic branch under its supplied frame hypotheses.

This shorter proof bypasses the conic and exceptional-fiber arguments
91 through116. Their quadratic recognition obligation is superseded.
The relative cubic branch and entry from an arbitrary polynomial
cylinder remain unresolved. The full conjecture is not solved.

Two independent AI readings of the new reduction are clean. The
[capture117](research/verification-pass117-working.json) records seven
passing targeted methods, two new and five retained. These are not
human expert review, a formal proof certificate, or novelty clearance.
The [checkpoint117](research/checkpoint-pass117-working.json) records
artifact hashes, proof-review scope and the unresolved obligations.

## Previous investigation: fixed-surface criteria and coefficient restrictions

The [working116 synthesis](research/quadratic-involution-frontier-pass116.md)
gives an exact recognition criterion for the global conic: its fixed
surface is an affine plane if and only if the sign involution is
polynomially linearizable, equivalently its odd parameter is an
ambient polynomial coordinate. These conditions remain unproved.

The [intrinsic-shift proof116](research/quadratic-intrinsic-shift-odd-row-pass116.md)
uses two actual polynomial flows and original generation to constrain
closed-point coefficient degeneration. It excludes a specific
proportional-column pattern on P=0 and proves
Omega belongs to the radical of (P,Delta), where Delta=det[b,d,e].
It does not make Delta a unit or identify the fixed surface as a plane.

A zero-column coordinate implication is valid, but a scope check
shows that its antecedent was already excluded by the exact quadratic
branch's generic-generation theorem. It is not counted as a new
nonempty solved sector. General cancellation remains unsolved.

The [capture116](research/verification-pass116-working.json) passes four
suites/eight methods, four new and four retained. These exact identities
and the separate AI proof reviews are not formal or human expert
verification. The [checkpoint116](research/checkpoint-pass116-working.json)
records the artifact versions and unresolved obligations.

## Previous investigation: the supplied quadratic frame has a global conic

The [working115 synthesis](research/quadratic-global-conic-frontier-pass115.md)
and [global patching proof](research/quadratic-global-conic-patching-pass115.md)
give one actual presentation A=S[U,r]/(r squared-2P U+eta), with
S=C[s,t], under the supplied nonconical quadratic-frame hypotheses.
The [free-fiber proof](research/free-quadratic-fiber-conic-pass115.md)
excludes three translating components and proves I2=I1 at all remaining
free fibers. Combined with fixed114, this gives the all-closed-point
equality needed for the global coefficient-intersection argument.

Global conic generation is not affine-space recognition. The
[source and boundary audit](research/quadratic-conic-global-recognition-gates-pass115.md)
checks that a Russell cubic has the same intrinsic conic filtration
without being affine three-space; no polynomial cylinder or actual
special frame is assigned to that example. Recognition in the supplied
frame, the relative cubic branch, and arbitrary-frame entry remain open.
The full cancellation conjecture remains unsolved and novelty unverified.

The [capture115](research/verification-pass115-working.json) passes five
suites/eight methods, two new and six retained. These exact identities
and the separate AI proof reconstructions are not human expert review
or formal verification. The [checkpoint115](research/checkpoint-pass115-working.json)
records scope, provenance and frozen artifact hashes.

## Previous investigation: the proper whole-double branch is excluded

The [working114 synthesis](research/whole-double-universal-frontier-pass114.md)
and [explicit factorization proof](research/whole-double-universal-factorization-pass114.md)
exclude the entire proper second-image whole-double alternative under
the retained actual112 coefficient and113 analytic-prime hypotheses.
A simple root of a cubic produces two nonunit factors of P whose
joint ideal is maximal-primary, contradicting its single prime support.
An [independent division proof](research/whole-double-cubic-division-exclusion-pass114.md)
reconstructs the same exclusion.

Thus every fixed closed fiber in the supplied nonconical quadratic
frame has an actual local cyclic-conic presentation. This does not
classify fixed-point-free fibers or patch the local conics globally at
checkpoint114; pass115 supplies those two steps in the same frame.
It does not settle the relative cubic lane or supply arbitrary-frame entry.
Full cancellation remains unsolved. Earlier bounded114 exclusions
are preserved as superseded research history, not necessary premises.
The [capture114](research/verification-pass114-working.json) passes six
suites/eight methods, four new and four retained; the
[checkpoint114](research/checkpoint-pass114-working.json) records scope.
AI reconstructions and exact identities are not human expert review,
formal verification or novelty clearance.

## Previous investigation: two local exclusions and completed-kernel rigidity

The [working113 synthesis](research/whole-double-completion-frontier-pass113.md)
excludes a smooth first coefficient h and the residual ideal J=m in
the supplied proper whole-double branch. Both force incompatible
factorizations of the actual first-image scalar P. The remaining branch
has nonzero h in m squared and J strictly contained in m.

A separate complete proof shows that whole-fiber completion introduces
no new invariants and that every finite-degree module descends to the
completed base, including at zero first normal action. This closes a
specific descent gap, not the missing quadratic-parameter construction.
At checkpoint113 the proper branch, arbitrary-frame entry and full
cancellation remained open. Pass114 supersedes the proper-branch status.
The [capture113](research/verification-pass113-working.json) passes four
suites/six methods, two new and four retained; the
[checkpoint113](research/checkpoint-pass113-working.json) records scope.
AI reconstructions and identity checks are not human expert review,
formal verification or novelty clearance.

## Previous investigation: the whole double has a uniform leading chart

The [working112 synthesis](research/whole-double-conormal-frontier-pass112.md)
adds coefficient restrictions and cubic residue bounds to the remaining
proper-image whole-double branch. A global conormal argument recovers a
constant leading transverse chart without assuming a nonzero speed
normal. This is still a conditional frame result, not an exclusion.

A separate finite preparation proof constructs a hidden quadratic
parameter for every polynomial perturbation in an explicit triangular
class. It does not put arbitrary inputs into that class. Full cancellation,
proper-branch elimination and global recognition remain unresolved.
The [capture112](research/verification-pass112-working.json) passes six
suites/eight methods, three new and five retained. The
[checkpoint112](research/checkpoint-pass112-working.json) records exact
scope. AI reviews and symbolic tests are not human or formal verification;
novelty is not established.

## Previous investigation: the mixed exclusion no longer needs a speed normal

The [working111 synthesis](research/quadratic-all-normal-frontier-pass111.md)
and [all-normal proof](research/quadratic-all-normal-mixed-exclusion-pass111.md)
exclude the mixed quadratic fiber of profile (2,1) even at zero speed
normal, within the supplied actual frame. A new invariant-conic lemma
and nilpotent-rank argument reconstruct the needed whole-fiber
coordinates and action without the old original-normal equation.

The whole-double sector now has an exact dichotomy without that premise:
a hidden quadratic parameter exists exactly when I2=I1. Its proper-image
alternative remains open, as do global recognition and arbitrary-frame
entry. Full cancellation is unsolved and novelty is not established.
The [capture111](research/verification-pass111-working.json) passes six
suites/ten methods, three new finite controls and seven retained.
The [checkpoint111](research/checkpoint-pass111-working.json) records
scope and evidence. AI proof reviews are not human or formal verification.

## Previous investigation: the collapsed mixed quadratic sector is excluded

The [working110 synthesis](research/mixed-sector-exclusion-frontier-pass110.md)
and [complete proper-case proof](research/mixed-proper-image-exclusion-pass110.md)
exclude the remaining collapsed mixed quadratic fiber with nonzero
speed normal under the supplied actual-frame hypotheses. A divided
quartic gives a finite module of index ideal (b); differentiation and
flat contraction force an impossible coprimality relation. The proof
includes higher-order and nonreduced conic-constant divisors.

The [capture110](research/verification-pass110-working.json) passes four
suites/eight methods, three new finite controls and five retained checks.
Separate AI proof reconstructions are not human or formal verification.
The [checkpoint110](research/checkpoint-pass110-working.json) records
the finalized109 material and the new110 result. Whole-double fibers,
zero speed normal, the relative cubic branch, global recognition and
arbitrary-frame entry remain open. Full cancellation remains unsolved;
novelty is not established.

## Previous investigation: proper second-image ideals and an actual quartic

The [working108 synthesis](research/mixed-proper-ideal-frontier-pass108.md)
excludes the unit second-image ideal in the remaining collapsed mixed
quadratic branch. The proper-ideal case has new sharp coefficient
restrictions. When one specified base coefficient has order one, an
actual quartic determines the whole fourth-degree basis and forces the
third-degree residue image to be the full Artin algebra. The normalized
fourth-image ideal is (a,t^n), with 1 <= n < 2 length(R/J2).

The [capture108](research/verification-pass108-working.json) passes three
suites/six methods, two new finite checks and four retained controls.
The written arguments have separate AI reconstructions, not formal or
human certification. The [checkpoint108](research/checkpoint-pass108-working.json)
records the exact versions and scope. The proper mixed branch is not
excluded, and the [global-entry audit](research/global-entry-audit-pass108.md)
keeps the unproved arbitrary-action frame reduction explicit. Full
cancellation remains unsolved and novelty is not established.

## Previous investigation: the full second-degree mixed branch is excluded

The [working107 synthesis](research/mixed-full-artin-exclusion-frontier-pass107.md)
excludes a full three-dimensional second-degree residue image in the
actual collapsed mixed quadratic sector with nonzero speed normal.
The remaining mixed branch therefore has second-degree image of
dimension two. This is a branch-specific result, not cancellation.

The proof first determines the exact quadratic-divisor algebra and
all derivative-image valuations. A standard flat-module purity lemma
then extracts coefficients in the square of the actual point ideal,
including its nonreduced structure. Actual quartic divisions and a
unit-determinant argument give an exact presentation whose closed
fiber has dimension two, contradicting the actual one-dimensional
fiber and degree-four generation. No reduced-point assumption remains.

The [capture107](research/verification-pass107-working.json) passes four
suites/seven methods, two new finite controls and five retained checks.
The universal proof has separate AI reconstructions, not formal or
human certification. The [checkpoint107](research/checkpoint-pass107-working.json)
records exact evidence and remaining gaps. Lower residue rank,
whole-double fibers, zero speed normal, global recognition and
arbitrary-frame entry remain unresolved. Novelty is not established.

## Previous investigation: a nonprincipal fourth derivative image

The [working106 synthesis](research/mixed-fourth-image-frontier-pass106.md)
proves that the actual fourth derivative-image ideal is nonprincipal
in the collapsed mixed sector with nonzero speed normal. It requires
two or three generators. This follows by extending the normalization
boundary to every admissible fourth-degree parameter and contradicting
a putative ideal generator with an actual local slice.

When the second-degree image is the full Artin algebra, the ideal has
exactly two generators: I3=(g), I4=theta gJ, with J a proper closed-point
complete-intersection ideal and g in JI2. This forces I3 into the third
base power and I4 into the fourth. The proof also records the exact
degree-two divisor support and additional multiplication constraints.
It does not exclude the mixed fiber or solve cancellation.

A genuine intrinsic LND algebra has the same nonprincipal module
pattern and low-degree products, but fails the actual flatness and
nonzero fiber-derivation assumptions. Its exact failure is part of
the result, not an actual-frame counterexample. The
[capture106](research/verification-pass106-working.json) passes three
suites/four methods, two new and two retained. Separate AI proof
reconstructions are not formal or human certification. The
[checkpoint106](research/checkpoint-pass106-working.json) records the
proof versions and remaining gaps.

## Previous investigation: cubic rank loss and the actual boundary

The [working105 synthesis](research/mixed-cubic-rank-and-boundary-frontier-pass105.md)
proves an actual third-degree image defect in the collapsed mixed sector
with L(m) nonzero. Every F3 element is constant on both reduced components,
and its rank-four module has whole-fiber image of dimension at most three.
This uses a new normalization-boundary argument and exact DVR slice
lifting, not a nilpotent coefficient count alone.

The c-projection has a finite rank-four normal closure with one omitted
reduced closed point. Its boundary forces a degree-one invariant divisor
on which c has degree three. This rules out the full-rank cubic alternative;
it does not exclude the mixed fiber. No parameter of any degree makes
the entire localized algebra finite over its relative polynomial ring.

An intrinsic quartic family has an explicit hidden cubic parameter, but
its divisor constant-field degree is three and violates the actual-frame
bound two. The proof records that exact incompatibility. A separate
transverse-surface calculation identifies moving branch tangents without
claiming that they lie in the fixed quotient exceptional curve.

The [capture105](research/verification-pass105-working.json) passes five
suites/seven methods: three new finite controls and four retained checks.
Universal arguments have separate written AI reconstructions, not formal
or human certification. The [checkpoint105](research/checkpoint-pass105-working.json)
records the proof versions and remaining gaps. Unrestricted cancellation
is still unsolved.

## Previous investigation: mixed-fiber rigidity and transverse surfaces

The [working104 synthesis](research/mixed-fiber-and-transverse-frontier-pass104.md)
proves that every degree-two residue is Artin-valued on the actual
mixed fiber with L(m) nonzero. A hidden quadratic component parameter
cannot exist there. The degree-three module and its multiplication
are now the relevant missing generation step, not a rank count alone.

The finite translation kernels are the neighborhoods of an actual
smooth transverse surface. Their completion is a finite free ramified
cover of the corrected formal base, which need not be the original
base embedding. Separately, the smooth local conic cannot have a
section over its specified base, so the checked section-patching
theorem cannot apply. A Catalan construction recovers a hidden
quadratic parameter in an intrinsic whole-double family only.

The [capture104](research/verification-pass104-working.json) passes
four suites/six methods, comprising three new finite controls and
three retained dependency checks. The universal arguments have
separate AI reconstructions, not human or Lean certification.
Unrestricted cancellation remains unsolved. The
[checkpoint104](research/checkpoint-pass104-working.json) records
the exact proof versions, reviews, test scope and remaining gaps.

## Previous investigation: finite neighborhoods and an exact local conic

The [working103 synthesis](research/adic-and-cyclic-conic-frontier-pass103.md)
extends the collapsed-fiber result to every finite base-adic thickening:
the projected original partial has a compatible locally nilpotent action
and slice on each quotient. This does not make that projected field
locally nilpotent on the original ring or on its completion.

Separately, a noncollapsed fixed double component determines every
localized degree module and yields an exact conic presentation over
the local invariant base. It includes both first-normal cases and
does not require a nonzero speed normal. Higher-order plinths and
global recognition remain unresolved.

An actual three-good-coordinate control disproves global local
nilpotence of the projected partial from the broad frame alone.
It has no stable base fiber, so it is not a counterexample to the
finite-neighborhood theorem. The [canonical capture103](research/verification-pass103-working.json)
passes two finite methods, not the universal geometric arguments.
The full cancellation conjecture remains unsolved.
The [checkpoint103](research/checkpoint-pass103-working.json) records the
proof reviews, exact inputs and retained limits.

~~~sh
/opt/anaconda3/bin/python -m unittest -v research.projected_derivation_thickening_checks_pass103
~~~

## Previous investigation: the actual module removes the remaining correction

The [working102 proof](research/quadratic-degree-module-fiber-rigidity-pass102.md)
extends the polynomial-lifting idea to the actual supplied quadratic
frame. For a collapsed whole double or mixed fiber with nonzero speed
normal, the slice correction is independent of the component parameter,
including its nilpotent part. This closes the nonconstant-correction
case left open in100, without assuming the threefold is polynomial.

The proof uses the actual finite free degree modules, a basis obtained
from three independent fiber residues under a contradiction assumption,
and the first base coefficients of an intrinsic conic identity.
It does not import the stronger image-ideal hypotheses of the older
filtration program. Root and a separate AI reviewer reconstructed the
complete saved proof; this is not human or formal certification.

Consequently the original last-coordinate partial preserves the
intrinsic whole-fiber ring and commutes with E there. This is still
only a fiber statement. Global preservation, fixed-fiber exclusion,
the L=0 sector and the arbitrary-frame reduction remain unresolved.
The full cancellation conjecture is not solved.

The [canonical capture102](research/verification-pass102-working.json)
passes one finite symbolic method. The [checkpoint102](research/checkpoint-pass102-working.json)
records the proof reviews and exact scope.

~~~sh
/opt/anaconda3/bin/python -m unittest -v research.quadratic_degree_module_checks_pass102
~~~

## Previous investigation: polynomial lifting and the unrestricted entry problem

The [working101 synthesis](research/polynomial-lift-and-global-entry-frontier-pass101.md)
proves an exact degree-two module formula for a specified infinite family
of smooth polynomial threefolds. It rules out every polynomial lift of
the nonconstant nilpotent correction in that family, including arbitrary
higher-order corrections. This is not yet a reduction of the actual
remaining four-coordinate frame to that family.

The supplied actual frame also yields one stronger base-order bound.
A sharp intrinsic example prevents automatic iteration of that argument.
Separately, an explicit tame translation family proves there is no
dimension-only spatial-degree cutoff for finding a slice or invariant
coordinate. It does not disprove nonlinear frame existence.

The [canonical capture](research/verification-pass101-working.json)
passes one suite/two finite methods; the all-polynomial arguments are
written proofs with separate AI reconstructions, not formal or human
certification. The full conjecture remains unsolved. See the
[checkpoint](research/checkpoint-pass101-working.json).

~~~sh
/opt/anaconda3/bin/python -m unittest -v research.quadratic_polynomial_lift_checks_pass101
~~~

## Previous investigation: exact actions on the nonreduced fiber

The [working100 synthesis](research/quadratic-action-frontier-pass100.md)
determines the canonical Jacobian action and the original last-coordinate
partial on the whole collapsed double or mixed fiber, when the speed-map
normal is nonzero. The canonical coefficient is constant on each component
factor after retaining its required multiplicity.

A global cubic identity forces whole-fiber commutation when the first
normal action is nonzero. With zero first normal action, a quadratic
nilpotent correction remains. An exact fiber-algebra example shows why
polynomial invertibility on that fiber alone cannot remove the correction.
Neither result proves a lift to the original ring or recognizes A.

The [canonical capture](research/verification-pass100-working.json)
passes one finite symbolic method. Separate AI proof reconstructions found
no gap in the stated special-case argument; they are not human review or
formal verification. The larger arbitrary-frame reduction remains open.
See the [checkpoint](research/checkpoint-pass100-working.json).

~~~sh
/opt/anaconda3/bin/python -m unittest -v research.quadratic_whole_fiber_checks_pass100
~~~

## Previous investigation: exact whole fibers and a constant normal row

The [working99 synthesis](research/quadratic-whole-fiber-frontier-pass99.md)
uses the original volume identity to put an actual normal coordinate
inside the whole fiber ideal. When L(m) is nonzero, a collapsed
double component has a constant conormal row and an affine column.
Zero first normal action makes the entire matrix constant, excluding
the three nonconstant row types considered in98 for this sector.

The whole original fiber ideal is exactly (ell,Y²) for a collapsed
whole double, or (ell,Y²(Y-1)) for the mixed (2,1) case. Its actual
E-invariant ring is C[G,c]/(G²) or C[G,c]/(G²(G-1)), including nilpotents.
These are fiber presentations, not a polynomial presentation of A.

The full conjecture, recognition of the supplied frame, and
arbitrary-frame reduction remain unresolved. The
[canonical capture](research/verification-pass99-working.json)
passes one finite method, not the universal geometric proofs.
See the [audit](research/proof-audits-pass99-working.md) and
[checkpoint](research/checkpoint-pass99-working.json).
Separate AI reviews are not human or formal certification.

~~~sh
/opt/anaconda3/bin/python -m unittest -v research.quadratic_volume_normal_checks_pass99
~~~

## Previous investigation: parallel planes and the zero-normal restriction

The [working98 synthesis](research/quadratic-plane-and-zero-normal-frontier-pass98.md)
narrows two remaining sectors of the supplied actual quadratic frame.
For a mixed (2,1) fiber, a nonzero speed-map normal forces both
components into parallel affine planes in the original four-space.
Their exact component ideals have shared global generators in A,
but these generators are not proved to be coordinates or N-invariant.

At a collapsed double component with zero first normal action,
the quotient conormal row has degree at most two and a constant
transverse quadratic coefficient. A separate intrinsic control
shows why the weighted leading translation cannot be promoted to
a square-zero identity for the full derivation.

Neither theorem excludes the remaining fixed fibers or recognizes A.
The general conjecture and arbitrary-frame reduction remain unsolved.
The [canonical capture](research/verification-pass98-working.json)
passes one finite exact method. See the
[audit](research/proof-audits-pass98-working.md) and
[checkpoint](research/checkpoint-pass98-working.json).
Separate AI reviews are not human or formal verification, and no
historical novelty claim is made.

~~~sh
/opt/anaconda3/bin/python -m unittest -v research.quadratic_zero_normal_checks_pass98
~~~

## Previous investigation: total-four exclusion and exact degree defect

The [working97 synthesis](research/quadratic-tangent-and-coordinate-frontier-pass97.md)
excludes every total-four closed fiber in the supplied actual quadratic
frame. Each component has multiplicity at most two, and a fiber
containing a fixed component has only profile (2) or (2,1).
The full conjecture and the arbitrary-frame reduction remain unsolved.

The proof makes a saturated local projection finite, then equates
normalized branch degrees with the actual integral component columns.
Their total would be divisible inside a lattice in which it must be
primitive. No first-normal-action assumption is needed for this step.

A weighted extension shows that every total-three fiber has exact
projection defect one: generic degree four and special dimension three.
The relevant flat module is provably nonfinite. Its reduced components
are straight lines in the actual relative generators, and in profile
(2,1) a low-degree good function separates the reduced components.
These facts do not yet exclude that fiber.

A conditional singular-tangent restriction still applies to its double
component. A separate original-coordinate argument gives global
complete-intersection equations for a noncollapsed whole double fiber.
Neither supplies a global recognition theorem.

The [canonical capture](research/verification-pass97-working.json)
passes three finite exact methods, not the universal geometry.
See the [audit](research/proof-audits-pass97-working.md) and
[checkpoint](research/checkpoint-pass97-working.json). Separate AI
proof reviews are not human expert review or formal verification.

~~~sh
/opt/anaconda3/bin/python -m unittest -v research.quadratic_double_branch_checks_pass97 research.quadratic_triple_branch_checks_pass97 research.quadratic_source_balance_checks_pass97
~~~

## Previous investigation: whole affine lines and fixed-component compatibility

The [working96 synthesis](research/quadratic-fiber-recognition-frontier-pass96.md)
strengthens the actual quadratic branch: every reduced closed-fiber
component is an entire affine line, and any noncollapsed fixed
component is the whole reduced fiber. In particular, fixed components
in reducible fibers must be collapsed. Remaining fixed fibers have
not been excluded or recognized.

A fresh dependency argument proves the needed irreducible-fiber
multiplicity exclusion with fewer topological source assumptions.
An explicit polynomial-ring control shows why the improved quotient
geometry and an exact relative inverse still cannot replace the
original-coordinate hypothesis in the global step.

The [canonical capture](research/verification-pass96-working.json)
passes one finite symbolic method, not the universal geometry.
See the [audit](research/proof-audits-pass96-working.md) and
[checkpoint](research/checkpoint-pass96-working.json).
General cancellation and the arbitrary-frame reduction remain open
in this investigation.

~~~sh
/opt/anaconda3/bin/python -m unittest -v research.quadratic_global_bridge_checks_pass96
~~~

## Previous investigation: quadratic fibers and everywhere quotient rank

The [working95 synthesis](research/nonconical-quadratic-rank-frontier-pass95.md)
proves that, in the supplied actual quadratic frame, all reduced
quotient-fiber components are smooth and pairwise disjoint, and
the quotient differential has rank at least one everywhere.
The argument retains the full nonreduced fiber. It does not
exclude rank-one fixed curves or recognize the threefold.

A surviving good generator gives an exact local model under a
nonzero first-normal-action hypothesis. The cubic branch gains
a restricted polynomial leading-pencil classification. A separate
actual polynomial example rules out every constant-linear
coordinate extraction from one specified slice projection.

The [canonical capture](research/verification-pass95-working.json)
passes three suites and three methods. These finite exact controls
do not certify the universal proofs. See the
[audit](research/proof-audits-pass95-working.md) and
[checkpoint](research/checkpoint-pass95-working.json).
The full conjecture and arbitrary-frame reduction remain unresolved.

~~~sh
/opt/anaconda3/bin/python -m unittest -v research.double_component_initial_checks_pass95 research.projected_generator_extraction_checks_pass95 research.cubic_quadratic_pencil_checks_pass95
~~~

## Previous investigation: weighted conormal rigidity and saturated cubic fibers

The [working94 synthesis](research/nonconical-weighted-frontier-pass94.md)
extends the quadratic collapsed rank-one conormal restriction
from double fibers to every multiplicity under the same actual
frame assumptions. The varying conormal column has two possible
polynomial shapes. At multiplicity two its rank drop forces a
noncollapsed fixed companion in a (2,2) fiber, not a contradiction.

For cubic fibers of total multiplicity six, the finite local
normalization is the actual base change. The reduced components
are relative affine lines, and the two relative generators are
regular parameters at rank-zero components. No such fiber has
been excluded. The arbitrary-frame reduction and the full
conjecture remain unresolved.

The [canonical capture](research/verification-pass94-working.json)
passes one method with three finite multiplicity subtests.
This is a symbolic control, not formal proof verification.
See the [audit](research/proof-audits-pass94-working.md) and
[checkpoint](research/checkpoint-pass94-working.json).

~~~sh
/opt/anaconda3/bin/python -m unittest -v research.weighted_conormal_checks_pass94
~~~

## Previous investigation: double-fiber normal order and cubic source gluing

The [working93 synthesis](research/nonconical-second-normal-frontier-pass93.md)
uses the actual quadratic degree identities one normal order
further. For a collapsed rank-one double fiber, it forces a
constant conormal row or column, including the speed-derivative
case the first-layer argument left open. This is not an invariant
coordinate or an exclusion of the fixed component.

Saturated cubic multiplicity gives a finite free local normalization.
The remaining heavy profiles require specific source gluing, and
some also require singular base branches. Finite-curve and lattice
controls show why these necessary conditions do not yet contradict
those profiles. The full conjecture remains unsolved.

The [canonical capture](research/verification-pass93-working.json)
passes two suites and three methods: finite-curve/lattice controls
and a symbolic normal-order identity. They are not formal proof
verification. See the [audit](research/proof-audits-pass93-working.md)
and [checkpoint](research/checkpoint-pass93-working.json).

~~~sh
/opt/anaconda3/bin/python -m unittest -v research.ramification_gluing_controls_pass93 research.double_fiber_normal_order_checks_pass93
~~~

## Previous investigation: total fiber multiplicity and quadratic rank exclusion

The [working92 synthesis](research/nonconical-fixed-fiber-frontier-pass92.md)
bounds the total generic multiplicity of every closed quotient
fiber by twice the relative degree. In the supplied quadratic
frame this excludes every generically rank-zero component.
Rank-one fixed curves and isolated rank drops are not excluded.
The cubic case has a short remaining list of multiplicity profiles.

The fixed scheme is a pure Cohen--Macaulay curve if nonempty.
When both relative generators collapse, the component's cylinder
is exactly an affine plane in the original four coordinates.
These restricted deductions have written proofs and separate AI
reviews, not human review, formal verification or novelty clearance.

The [targeted capture](research/verification-pass92-working.json)
passes one suite/two finite Artin-control methods. It does not
certify the universal arguments. See the
[proof audit](research/proof-audits-pass92-working.md) and
[checkpoint](research/checkpoint-pass92-working.json).
The unrestricted conjecture and arbitrary-frame reduction remain open.

~~~sh
/opt/anaconda3/bin/python -m unittest -v research.fixed_scheme_artin_checks_pass92
~~~

## Previous investigation: linear recognition and the exceptional-fiber boundary

The [working91 synthesis](research/nonconical-exceptional-fiber-frontier-pass91.md)
adds a written recognition proof for the relative degree-one branch
of the actual nonconical constant-acceleration frame, even when the
velocity determinant is nonconstant. Independent AI proof reviews
are complete; human review, formal certification and novelty remain
outstanding.

For the remaining quadratic and cubic branches, an exact global
Jacobian factor is a primitive intrinsic LND. Its possible fixed
locus lies over finitely many base points in the exceptional divisor.
Every generic divisor constant extension has degree at most three.
On the smooth principal open, disconnected closed fibers are two
or three parallel lines. An exact changed-presentation control shows
why whole smaller-ring fibers cannot be replaced by their images.

The [targeted capture](research/verification-pass91-working.json)
passes two finite-control methods, not the universal proofs. See
the [proof audit](research/proof-audits-pass91-working.md) and
[checkpoint](research/checkpoint-pass91-working.json).
The general conjecture and the arbitrary-frame reduction remain
unresolved.

~~~sh
/opt/anaconda3/bin/python -m unittest -v research.nonconical_global_jacobian_checks_pass91 research.nonconical_multiplicity_boundary_checks_pass91
~~~

## Previous investigation: nonconical volume identities and constant-determinant recognition

The [working90 synthesis](research/nonconical-volume-frontier-pass90.md)
proves exact descent of the relative generator ring after inverting
the velocity determinant, and bounds its defining equation by degree
three. The remaining original volume coefficients give a fixed-point-free
intrinsic LND on that open set and a smooth relative curve morphism.

When the determinant is a nonzero constant, the new action is global.
The [constant-determinant proof](research/constant-omega-recognition-pass90.md)
then applies the published Kaliman--Saveliev free-action theorem
to identify the kernel with a polynomial three-ring.
The nonconstant-determinant case and the reduction from arbitrary
sliced actions remain unresolved.

The [targeted capture](research/verification-pass90-working.json)
passes two finite-control methods. They do not certify the
written universal arguments. See the
[proof audit](research/proof-audits-pass90-working.md) and
[checkpoint](research/checkpoint-pass90-working.json).
Human expert review, formal proof and novelty determination remain
outstanding. The general conjecture is not solved.

~~~sh
/opt/anaconda3/bin/python -m unittest -v research.nonconical_higher_commutator_checks_pass90 research.nonconical_quadratic_potential_checks_pass90
~~~

## Previous investigation: recognition with a homogeneous speed relation

The [working89 synthesis](research/homogeneous-speed-recognition-frontier-pass89.md)
states a restricted recognition theorem for an actual four-variable
LND: three coordinate second derivatives vanish, the fourth is a
nonzero constant, and the three good speeds satisfy a nonzero
homogeneous polynomial relation. Under those hypotheses, the kernel
is a polynomial three-ring.

The proof combines unit normals, a whole-divisor-fiber argument and
a critical-point contradiction for the original last-partial
commutator. It covers both rank-one speeds and rank-two conical
speeds. The nonconical case and the reduction from an arbitrary
sliced action remain open in this investigation.

See the [combined proof](research/constant-acceleration-relative-slice-descent-pass89.md),
[proof audit](research/proof-audits-pass89-working.md), and
[checkpoint](research/checkpoint-pass89-working.json).
The [targeted capture](research/verification-pass89-working.json)
passes two finite-control methods. Those tests do not certify the
recognition theorem. Human expert review, formal verification and
novelty determination are still outstanding.

~~~sh
/opt/anaconda3/bin/python research/run_targeted_pass89.py
~~~

## Previous investigation: invariant-plane generators and descent

The [working88 synthesis](research/invariant-plane-pencil-frontier-pass88.md)
obtains an actual polynomial invariant plane and a universal relative
generator identity in the three-good-coordinate constant-acceleration
case. The original coordinate volume bounds a slice-difference
denominator by an explicit velocity determinant. Its nonvanishing
also forces equal fraction fields; its vanishing has a separate
good-partial reduction, not a recognition conclusion.

An exact polynomial-ring control shows that even normality and the
known faithful-flat plane inclusion cannot justify the missing descent.
Its proposed last coordinate fails an explicit zero-fiber unit test.
This is a counterexample to a proof shortcut, not to cancellation.

The [targeted88 capture](research/verification-pass88-working.json)
passes four standalone methods. No full regression or exhaustive
action search ran. The [proof audit](research/proof-audits-pass88-working.md)
and [checkpoint](research/checkpoint-pass88-working.json) distinguish
AI proof reviews, finite controls, source assumptions and outstanding
work. General cancellation, expert review and novelty remain unresolved.

~~~sh
/opt/anaconda3/bin/python research/run_targeted_pass88.py
~~~

## Previous investigation: constant acceleration and exact linearization gates

The [working87 synthesis](research/constant-acceleration-frontier-pass87.md)
constructs actual involutions on every original coordinate fiber when
one coordinate has nonzero constant acceleration. Their invariant ring
is the unknown threefold ring. A specified odd generator is an ambient
coordinate exactly when the fiber involution is linearizable, using
the stated affine-plane-fibration inputs. Neither condition is automatic.

Actual examples rule out the proposed averaging and invariant-matrix
shortcuts. With three E-affine companions, the velocity Jacobian has
exact nilpotence and adjoint identities, but can have rank three.
The highest bad-partial coefficient is an LND, possibly zero; even
when nonzero it need not move the critical-value function.

The [targeted87 capture](research/verification-pass87-working.json)
passes three independent suites, one method each. It is not a full
regression or a universal proof. See the
[proof audit](research/proof-audits-pass87-working.md) and
[checkpoint](research/checkpoint-pass87-working.json).
General cancellation, expert review and novelty certification remain
incomplete. The full goal stays active.

~~~sh
/opt/anaconda3/bin/python research/run_targeted_pass87.py
~~~

## Previous investigation: one quadratic coordinate and its discriminant

The [working86 synthesis](research/coordinate-quadratic-frontier-pass86.md)
uses only one original coordinate of quadratic slice degree, with
no degree restriction on the other three. It proves a smooth
critical-value function on the reduced-denominator open set and
exact quadratic field/discriminant constraints for every original
coordinate fiber. An actual example prevents promoting that smooth
function to an LND slice; another distinguishes a squarefree
normalized discriminant from a repeated raw discriminant.

The [source/modification audit](research/quadratic-coordinate-modification-source-pass86.md)
keeps the exact saturated modification and the missing relative
coordinate/dimension hypotheses separate. It does not recognize the
invariant threefold. The [targeted86 capture](research/verification-pass86-working.json)
passes two methods covering three actual actions through subtests.
There was no full regression or exhaustive action search. See the
[proof audit](research/proof-audits-pass86-working.md) and
[checkpoint](research/checkpoint-pass86-working.json).
General cancellation remains unproved, without expert review, formal
verification or a verified novelty claim.

~~~sh
/opt/anaconda3/bin/python research/run_targeted_pass86.py
~~~

## Previous investigation: exact return domains and fixed polynomials

The [working85 synthesis](research/rank-one-return-domain-frontier-pass85.md)
determines the exact domain of the rational return in the restricted
one-quadratic-coordinate case. That domain excludes every good-speed
zero, closing the proposed regular-return route at those points.
The polynomial fixed ring is exactly A[T], but the induced morphism
is finite only when the reduced denominator is a unit. Thus the
proper-speed-ideal case gives no finite global quotient shortcut.

The [targeted85 capture](research/verification-pass85-working.json)
passes two exact methods in one suite. It checks actual actions,
including a cancelled divisor and distinct residue-field behaviors.
It is not a full regression or a universal proof. The
[source audit](research/rank-one-quasi-nice-source-scope-pass85.md)
keeps established recognition theorems behind their actual coordinate
hypotheses. See the [proof audit](research/proof-audits-pass85-working.md)
and [checkpoint](research/checkpoint-pass85-working.json).
General cancellation and the missing coordinate reduction remain
unproved, with no expert or formal review or verified novelty claim.

~~~sh
/opt/anaconda3/bin/python research/run_targeted_pass85.py
~~~

## Previous investigation: strict slice containment and embedded support

The [working84 synthesis](research/rank-one-strict-frontier-pass84.md)
uses the original polynomial slice to strengthen the acceleration
bound: if its degree in the three good variables is D, then
q^((D-1)^2) belongs to I^((D-1)^2+1) in the nonzero-acceleration,
proper-ideal case. In particular D=2 gives q in I squared. The
proof is an explicit Taylor identity and finite ideal computation.

A separate local argument confines any nonzero square class q squared
modulo I to finitely many embedded critical points in the specialized
three-variable speed scheme. No embedded maximal associated primes
therefore implies q squared in I. Those embedded points are not
excluded automatically. A further original-action return determinant
identity does not remove its possible poles.

Two exact ideal-only controls prevent invalid upgrades of these
necessary conditions to actual-action membership theorems. The
[targeted84 capture](research/verification-pass84-working.json)
passes three methods in two suites. No full regression or exhaustive
action search ran. See the [audit](research/proof-audits-pass84-working.md)
and [checkpoint](research/checkpoint-pass84-working.json).
General cancellation remains unproved, with no human expert or formal
review and no established novelty claim.

~~~sh
/opt/anaconda3/bin/python research/run_targeted_pass84.py
~~~

## Previous investigation: the return map and the cubic acceleration bound

The [working83 synthesis](research/rank-one-return-frontier-pass83.md)
uses the original polynomial flow to construct a rational return
involution. An explicit monic Taylor equation puts the acceleration
in the integral closure of the full speed ideal. Briancon--Skoda
then improves the fourth-power bound to a third-power bound. A separate
Jacobian/socle argument excludes isolated good-speed zeros.

This does not prove that the acceleration itself, or its square,
always belongs to the ideal. Embedded components remain relevant,
and there is no unrestricted coordinate reduction or cancellation
proof. These are AI-reviewed working deductions, not expert-reviewed
or historically certified novel results.

The [targeted83 capture](research/verification-pass83-working.json)
passes three exact methods in one suite. It is not a full regression
or an exhaustive action search. See the
[proof audit](research/proof-audits-pass83-working.md) and
[checkpoint](research/checkpoint-pass83-working.json) for the exact
source dependencies, retained evidence and open obligations.

~~~sh
/opt/anaconda3/bin/python research/run_targeted_pass83.py
~~~

## Previous investigation: exact bounds on the rank-one speed scheme

The [working82 synthesis](research/rank-one-speed-frontier-pass82.md)
keeps the full, possibly nonreduced ideal of the three nice-coordinate
velocities. The acceleration belongs to its divisorial hull, hence to
the ideal itself when that ideal is principal. In the general rank-one
quadratic case, the actual flow determinant proves q to the fourth
power lies in the ideal. It does not yet prove q itself lies there.

The quotient has an exact polynomial-cylinder description, but its
nilpotents cannot be discarded. Abstract quotient examples with
nilpotence order at least five are now excluded as ambient realizations;
orders two through four remain unconstructed. A primary-source check
also identifies the missing relative-divergence premise in a tempting
application of a two-variable theorem.

The [targeted82 capture](research/verification-pass82-working.json)
passes four exact methods in one suite. Separate bounded actual-frame
searches found no counterexample and add zero test methods. Written
proofs have separate AI reconstructions, not human expert or formal
verification. General cancellation and arbitrary rank-one recognition
remain unresolved. See the [audit](research/proof-audits-pass82-working.md)
and [checkpoint](research/checkpoint-pass82-working.json).

~~~sh
/opt/anaconda3/bin/python research/run_targeted_pass82.py
~~~

## Previous investigation: obstructions to quadratic coordinate reduction

The [working81 synthesis](research/quadratic-reduction-frontier-pass81.md)
tests the first non-nice orbit-degree case. It proves that universal scalar
Taylor filters which preserve polynomial coordinates are exactly nonzero
slice dilations, so they cannot lower orbit degree. Actual countercontrols
also rule out automatic acceleration-LND extraction and coordinate changes
fixing the three already-nice coordinates. The coordinate flow-box map has
generic degree equal to the chosen coordinate's orbit degree; local
holomorphic straightening does not supply a global polynomial inverse.

These are proof-strategy obstructions, not cancellation counterexamples
or recognition of all quadratic-time actions. The next construction must
allow simultaneous changes in the already-nice coordinates, or provide
an independent recognition argument. The preceding all-nice working
theorem remains intact, with no new general height bound.

The [targeted81 capture](research/verification-pass81-working.json)
passes six exact methods in two new suites. Written proofs received
independent AI reconstructions; human review, formal verification and
novelty assessment remain incomplete. No full81 regression ran. See
the [audit](research/proof-audits-pass81-working.md) and
[checkpoint](research/checkpoint-pass81-working.json) for exact scope.

~~~sh
/opt/anaconda3/bin/python research/run_targeted_pass81.py
~~~

## Previous working result: all nice sliced actions on complex four-space

The [working80 theorem](research/nice-slice-recognition-pass80.md)
removes the supplied-good-direction assumption: every locally nilpotent
derivation E of the actual complex polynomial four-ring with a global
slice and E squared zero on the four coordinate generators has polynomial
kernel. The formerly open no-good case now has a nondegenerate quadratic
velocity cone, an explicit polynomial Segre frame, and a relative
generation determinant that forces its remaining relation to be linear.

The complete new proof has separate AI reconstructions. It is not
human-reviewed, formally verified, or historically certified as novel.
General cancellation remains unresolved because no nice coordinate frame
has been produced for an arbitrary cylinder action. The theorem recognizes
the no-good case; it does not assert that every nice frame has a good
direction.

The [targeted80 capture](research/verification-pass80-working.json)
passes four exact methods in one new suite. The unchanged four-method
pass79 checker was also rerun successfully. Neither is a full regression;
the last full record remains 146 suites and 1047 methods from75. See the
[proof audit](research/proof-audits-pass80-working.md) and
[checkpoint](research/checkpoint-pass80-working.json) for exact scope.

~~~sh
/opt/anaconda3/bin/python research/run_targeted_pass80.py
~~~

## Previous working result: recognition with one supplied good direction

The [working79 synthesis](research/nice-good-recognition-frontier-pass79.md)
records a complete written proof for a restricted class: a nice
locally nilpotent derivation on the original complex polynomial
four-ring, with a global slice and a nonzero constant good direction,
has polynomial kernel. The
[recognition proof](research/nice-good-direction-recognition-pass79.md)
uses the actual coordinate-generation determinant to obtain a
relative quadratic equation. Its exact cofactors and invariant
omission force the coefficient of Z to be a nonzero constant,
so Z can be eliminated globally.

The proof has separate AI reconstructions, not human expert or
formal verification. The bounded source comparison does not
certify novelty. General cancellation remains unresolved: a good
direction has not been produced in every nice frame, and a nice
frame has not been produced for an arbitrary cylinder action.
The [common-highest-field note](research/nice-common-top-normal-identity-pass79.md)
starts the no-good-direction case with an actual quotient-plane
normal identity, without claiming recognition there.

The [targeted79 capture](research/verification-pass79-working.json)
passes four exact methods in one suite. The last full run remains
146 suites and 1047 methods from75. The
[audit](research/proof-audits-pass79-working.md) and
[checkpoint](research/checkpoint-pass79-working.json) distinguish
proof, source, finite-test and integrity evidence. No external
contact, submission or public claim occurred.

~~~sh
/opt/anaconda3/bin/python research/run_targeted_pass79.py
~~~

## Previous working result: the proper binary parameter ideal is excluded

The [working78 synthesis](research/binary-unit-ideal-frontier-pass78.md)
closes the proper-parameter obstruction in the actual nonlinear,
nice, supplied-good-direction branch. The
[normal-invariant proof](research/binary-normal-syzygy-exclusion-pass78.md)
shows that p,q and the three transverse velocities generate unit
ideals. It retains ramification and nilpotents and uses the
published intrinsic quotient theorem with its cylinder hypotheses.

An explicit [relative reconstruction](research/binary-relative-hypersurface-pass78.md)
then gives A=S[Y,Z] over the common invariant plane S, with one
defining relation. This is not polynomial recognition. The next
live question is to exploit the actual original-action equations
on this relative hypersurface to control primitive fixed points.
The no-good-direction and arbitrary-frame problems also remain open.

The [targeted78 capture](research/verification-pass78-working.json)
passes four finite exact methods in one suite. The last full run
remains 146 suites and 1047 methods from75. The
[proof audit](research/proof-audits-pass78-working.md) and
[checkpoint](research/checkpoint-pass78-working.json) distinguish
written AI reconstructions, published inputs, finite tests and
file integrity. No general solution, historical novelty, expert
review, formal verification or external contact is claimed.

~~~sh
/opt/anaconda3/bin/python research/run_targeted_pass78.py
~~~

## Previous working result: binary parameters and exact scheme content

The [working77 synthesis](research/binary-scheme-frontier-pass77.md)
parametrizes the nonlinear ternary-cone branch by actual invariant
polynomials p,q. Their common zero set is exactly the transverse
velocity zero set. If their ideal is proper, they must be
algebraically independent. These statements retain the original
nice frame, slice and supplied good direction.

The [content theorem](research/primitive-fiber-content-pass77.md)
turns high raw vanishing into exact ideal-power membership of the
derived field's common factor, without assuming primitive freeness.
It does not exclude the proper ideal. An
[all-degree two-shear control](research/stationary-parameter-omission-control-pass77.md)
shows that stationarity plus invariant omission alone cannot do so;
the original niceness equations separately rule out that exact pair.

The [targeted capture](research/verification-pass77-working.json)
passes five methods in one new suite. The last full regression
remains 146 suites and 1047 methods from75. The
[audit](research/proof-audits-pass77-working.md) and
[checkpoint](research/checkpoint-pass77-working.json) retain the
proof, source and finite-test boundaries. General cancellation,
arbitrary nice-frame existence, historical novelty, expert review
and formal verification remain unresolved.

~~~sh
/opt/anaconda3/bin/python research/run_targeted_pass77.py
~~~

## Previous working result: velocity-cone geometry and construction exclusions

The [working76 synthesis](research/velocity-cone-frontier-pass76.md)
identifies constant good directions with translation-apex directions
of the homogeneous cone over the velocity image. In the Jacobian
square-nonzero branch their dimension is exactly zero, one or three,
never two. A leading gcd containing only linear factors recognizes
the original kernel through a source-checked geometric criterion.

With a supplied good direction and a nonlinear cone, every nonconstant
polynomial invariant must use all four original constant directions.
The [source application](research/nice-good-direction-invariant-omission-pass76.md)
also proves the transverse velocities have gcd one. It does not
make their ideal, or the primitive derived fixed-point ideal, a unit.

The same pass excludes several larger primitive fixed-point
constructions, including the full triangular f,g,k pencil and a
variable-direction family outside affine-linear triangularity.
These are explicit restricted theorems, not a classification of all
nice actions. The no-apex and general primitive-freeness questions
remain unresolved, as does producing a nice frame for an arbitrary
original action.

The [fresh targeted capture](research/verification-pass76-working.json)
passes six methods in one new suite. The last actual full regression
remains 146 suites and 1047 methods from75. The
[audit](research/proof-audits-pass76-working.md) records independent
AI proof reconstructions, selected primary-source proofs and finite
test limits. The [checkpoint](research/checkpoint-pass76-working.json)
preserves the frozen predecessors. There is no general solution,
historical novelty verdict, expert review or formal verification.

~~~sh
/opt/anaconda3/bin/python research/run_targeted_pass76.py
~~~

## Previous working result: common-slice obstruction and exact family criteria

The [working75 synthesis](research/good-partial-frontier-pass75.md)
rules out common-slice selection even for a nice sliced action whose
sole good partial produces another globally sliced action. An explicit
polynomial inverse verifies the example and shows that it is not a
cancellation counterexample.

The [conic-family proof](research/conic-nice-pair-classification-pass75.md)
gives exact all-degree criteria for common slices and global slices
throughout the coprime parameter family. In every nonconstant member,
its primitive adjusted field is a coordinate partial for every supplied
slice. This is a constructive family calculation, not a theorem about
arbitrary nice actions.

The [primitive quotient test](research/primitive-good-quotient-scope-pass75.md)
is independent of the supplied slice: remove the common factor of
the six wedge coefficients, then test the resulting ideal for one.
The special hypotheses have not been proved to make that ideal the
unit ideal. A separate [all-degree obstruction](research/triangular-primitive-candidate-obstruction-pass75.md)
excludes a proposed fixed-point candidate from any simultaneous
nice/partial frame preserving its chosen auxiliary field.

The [fresh full regression](research/verification-pass75-working.json)
passes 146 suites and 1047 methods. Exactly three suites and six
methods are new in75. The [audit](research/proof-audits-pass75-working.md)
records independent AI reconstructions, source scope, corrected harness
errors and finite-test limits. The [checkpoint](research/checkpoint-pass75-working.json)
preserves all frozen predecessors. General cancellation, arbitrary
nice-action recognition, expert review, formal verification and
historical novelty remain unresolved. The all-profile threshold is ten.

~~~sh
/opt/anaconda3/bin/python research/run_regression_pass75.py
~~~

## Previous working result: nonlinear rank exclusion and coordinate certificates

The [working74 synthesis](research/nonlinear-frontier-pass74.md) proves
that a nice sliced action in an actual four-variable frame has Jacobian
cube zero and rank at most two. This eliminates the historical quadratic
nice rank-three search packet using published triangularization results.
It does not recognize every nonlinear nice action or produce a nice
frame for an arbitrary sliced action.

An exact recognized action has only one constant good direction, so the
rank result does not automatically provide the two-good-direction frame.
A separate actual nonslice action realizes the excluded rank-three case
and shows why a localized slice cannot replace the original slice.
Explicit adapted inverse-degree certificates are also saved for affine
actions and specified slice-projection families. These are constructive
baselines, not newly claimed recognition families.

The [fresh targeted capture](research/verification-pass74-working.json)
passes seven methods in three suites. At that checkpoint the last full
regression was the 140 suites and 1034 methods from73; no full74 run is claimed.
The [audit](research/proof-audits-pass74-working.md) and
[checkpoint](research/checkpoint-pass74-working.json) separate AI proof
reviews, published inputs, finite checks and file integrity. The
all-profile threshold remains ten. General cancellation, historical
novelty, human review and formal verification remain unproved.

## Previous working result: complete supplied frame and height ten

The [working73 synthesis](research/height-ten-closure-pass73.md)
recognizes the entire supplied actual two-quadratic coordinate frame
under the original polynomial slice. The
[higher-rank transfer](research/independent-higher-joint-rank-closure-pass73.md)
closes its last moving quartic and quintic sectors. Separate complete
AI reconstructions and a saved-file scope audit found no gap within
the stated hypotheses. The all-profile height threshold is now ten.
No universal frame bound or unrestricted cancellation proof is supplied.

The separate [bounded-family reduction](research/universal-family-degree-boundary-pass73.md)
shows that pointwise polynomial recognition in a fixed degree/slice/
nilpotence family would imply a uniform forward/inverse degree bound,
even for coordinates adapted to the supplied slice. It proves neither
pointwise existence nor a value of that bound. Its coefficient-field
and exceptional-locus limits are explicit.

The [fresh full regression](research/verification-pass73-working.json)
passed 1034 methods across 140 suites. Only three methods in one suite
are new in73; four suites have been added since the previous full69
run. The [audit](research/proof-audits-pass73-working.md) separates
written AI reviews, finite controls and source dependencies.
The [working73 checkpoint](research/checkpoint-pass73-working.json)
preserves the frozen predecessors and excludes later74 drafts.
There is no human expert review, formal proof or novelty verdict.

~~~sh
/opt/anaconda3/bin/python research/run_regression_pass73.py
~~~

## Previous checkpointed result: joint rank at most two

The [working72 synthesis](research/joint-rank-two-frame-closure-pass72.md)
recognizes all cases with original joint rank at most two under the
supplied actual frame. Its [terminal quintic proof](research/terminal-quintic-recognition-pass72.md)
uses a good fixed-base partial and a nonzero defect, followed by actual
coordinate changes and original-ring recognition. The
[checkpoint](research/checkpoint-pass72-working.json) freezes eleven
artifacts and preserves71 and earlier files. The
[targeted capture](research/verification-pass72-working.json) passed
five bounded exact methods; these are now also rerun in full73.
See its [audit](research/proof-audits-pass72-working.md) for precise scope.

## Previous checkpointed result: complete dependent-defect recognition

The [working71 theorem](research/dependent-frame-closure-pass71.md)
recognizes every fraction-field dependent defect pair under the actual
two-quadratic coordinate frame and original polynomial slice. The
[terminal moving-quartic proof](research/terminal-quartic-recognition-pass71.md)
closes the last dependent case. It constructs a global nice replica,
uses a known linear-invariant theorem to constrain original speed,
and gives actual polynomial shears into the rational two-direction
recognition theorem. The new good partial is explicitly checked.

Independent moving orders four and five and universal frame existence
remain unresolved. This is not unrestricted cancellation. The
[source note](research/nice-linear-invariant-source-pass71.md) records
the precise characteristic-zero theorem and an accessible alternative
proof route, including finite-coefficient-field descent.

The [targeted capture](research/verification-pass71-working.json)
passes three exact symbolic methods in one suite. These are coefficient
and coordinate-map controls, not full-frame examples or formal proofs.
The last full regression remains 1021 methods in 136 suites from69.
The [audit](research/proof-audits-pass71-working.md) separates AI proof
reviews, finite runs and source gates. There is no human expert review,
proof-assistant certificate or novelty verdict. The
[checkpoint](research/checkpoint-pass71-working.json) preserves70 and
earlier frozen files; subsequent72 drafts are outside it.

~~~sh
/opt/anaconda3/bin/python research/terminal_quartic_recognition_checks_pass71.py
~~~

## Previous checkpointed result: complete supplied-frame cubic recognition

The [working70 theorem](research/cubic-frame-closure-pass70.md) recognizes
every defect rank when the actual two-quadratic coordinate frame has
coordinate flow degree at most three. The new
[finite-root argument](research/dependent-algebraic-root-top-pass70.md)
proves that the remaining dependent moving case has an actual
polynomial common-power factor. Together with the separately checked
cubic transfer, this closes the dependent cubic gap left by69.

The same argument excludes rotating dependent quartics. The
[quartic reduction](research/common-power-moving-quartic-reduction-pass70.md)
recognizes its nonconstant residual branches but leaves a terminal
localized three-direction symmetry's global descent unresolved.
Independent moving orders four and five and universal frame existence
also remain open. General cancellation is not solved.

The [current targeted capture](research/verification-pass70-working.json)
passes two methods in one suite. It is not a fresh full regression;
the last full run remains 1021 methods in 136 suites from69. The
[working audit](research/proof-audits-pass70-working.md) distinguishes
separate AI proof reconstructions, actual finite controls and source
dependencies. No human expert review, proof-assistant certificate or
novelty verdict is claimed. The
[checkpoint](research/checkpoint-pass70-working.json) preserves the
frozen predecessors and excludes later drafts.

~~~sh
/opt/anaconda3/bin/python research/finite_root_top_checks_pass70.py
~~~

## Previous checkpointed result: independent-defect cubic recognition

The [working69 theorem](research/independent-cubic-closure-pass69.md)
recognizes every independent-defect case of flow degree at most
three under the supplied two-quadratic coordinate frame. The
original joint-rank-two moving cubic is now covered, including
its formerly unresolved constant-speed branch. This does not
close the dependent-defect moving cubic or the full frame.

For nonconstant normalized speed, a full differential relation
supplies a rational nice symmetry. A new two-direction recognition
lemma handles both its parallel and radial alternatives without
assuming that every rational nice field is locally nilpotent.
For nonzero constant speed, an explicit polynomial shear reaches
the proved mixed bound and lowers the coordinate flow degree.

The [fresh captured regression](research/verification-pass69-working.json)
passes 1021 methods in 136 suites. Eight methods in three suites
are new in pass69; the combined run also includes the two-method68
addition. The [audit record](research/proof-audits-pass69-working.md)
separates written AI reconstructions, exact finite controls,
source dependencies and the corrected symbolic-test harness.

The [working69 checkpoint](research/checkpoint-pass69-working.json)
preserves frozen predecessors. General cancellation, dependent
moving cases, higher independent moving cases and universal
coordinate-frame existence remain unresolved. There is no human
expert review, proof-assistant verification or novelty verdict.

~~~sh
/opt/anaconda3/bin/python research/run_regression_pass69.py
~~~

## Previous checkpointed result: constant highest vectors and rank-three cubic motion

The [working68 synthesis](research/constant-and-moving-closure-pass68.md)
recognizes every constant-highest-vector sector in the supplied
two-quadratic coordinate frame. It also recognizes its independent
moving cubic sector when the original action and two defects have
joint rank three. These are conditional frame theorems, not a
solution of general cancellation or a proof of universal frame existence.

The higher constant proofs construct a second global commuting action
with an actual coordinate slice, or an explicitly justified localized
nice symmetry. The moving cubic proofs retain the original coordinates
through invariant localization, then use either actual field generation
or a polynomial derivative-ratio argument to obtain an invariant
ambient coordinate. All six new proof notes have recorded independent
full-file AI reviews, with author self-review separated.

The [targeted verification](research/verification-pass68-working.json)
passes two new formal coefficient methods. It is not a fresh full
regression; the last full result is still 1011 methods in 132 suites
from67. The [audit record](research/proof-audits-pass68-working.md)
and [integrity packet](research/checkpoint-pass68-working.json)
record the precise scope and preserve frozen predecessors.

The remaining supplied-frame work is nonconstant-top: independent
cubic rank drop, higher independent motion, and dependent motion.
The universal coordinate-frame problem remains separate. There is
no human expert review, proof-assistant certificate, novelty verdict,
external communication or submission. Central metadata remains at full60.

~~~sh
/opt/anaconda3/bin/python research/independent_higher_constant_checks_pass68.py
/opt/anaconda3/bin/python research/consistency_checks_pass68.py
~~~

## Previous checkpointed result: constant third flow derivative

The [working67 theorem](research/constant-cubic-closure-pass67.md)
recognizes the original sliced kernel under the supplied two-quadratic
coordinate frame whenever the third flow derivative of its coordinate
vector is constant, including zero. This combines the prior low-flow
theorem with both newly closed constant-top cubic sectors. It is not
the assertion that every flow-degree-three case is recognized.

The [independent cubic proof](research/independent-cubic-graph-closure-pass67.md)
constructs an explicit ambient coordinate slice from an actual generic
graph and three determinant coefficients. The [dependent cubic proof](research/dependent-constant-cubic-closure-pass67.md)
constructs an actual localized nice symmetry and checks every hypothesis
of the existing one-good-output recognition lemma. An [actual countercontrol](research/constant-cubic-nonomission-control-pass67.md)
rules out assuming the common parameter omits a constant direction.

The [fresh captured full regression](research/verification-pass67-working.json)
passes 1011 methods in 132 suites. Only three methods in two suites are
new in working67. The [audit record](research/proof-audits-pass67-working.md)
separates author self-review, independent AI reconstructions, formal
coefficient checks and actual polynomial examples. The [integrity packet](research/checkpoint-pass67-working.json)
preserves frozen predecessors. The central 544-claim registry remains
at its historical full60 integration state.

Moving cubic tops, higher-flow sectors and universal frame existence
remain outside this checkpoint. No general solution, human expert
review, proof-assistant verification or novelty certification is claimed.

~~~sh
/opt/anaconda3/bin/python research/run_regression_pass67.py
/opt/anaconda3/bin/python research/constant_cubic_nonomission_checks_pass67.py
/opt/anaconda3/bin/python research/constant_cubic_graph_checks_pass67.py
/opt/anaconda3/bin/python research/consistency_checks_pass67.py
~~~

## Previous working result: complete supplied-frame low flow

The [working66 synthesis](research/low-flow-closure-pass66.md)
recognizes every original sliced kernel in the supplied two-quadratic
frame when its coordinate flow has degree at most two. A new
[source-free rank cap](research/rank-three-speed-curve-pass66.md)
excludes the last rank-three configuration from working65. Its full
five-dimensional preimage argument needs no speed-rank or projective
speed assumption. This is still a conditional supplied-frame theorem,
not unrestricted cancellation.

The [dependent constant-top cubic reduction](research/dependent-constant-cubic-pass66.md)
gives affine acceleration in an actual polynomial slice and a residual
tangent curve. The [independent cubic refinement](research/constant-top-cubic-good-fields-pass66.md)
identifies the good-field basis and rational curve coefficients.
Both retain explicit unresolved cubic obligations.

The [fresh full regression](research/verification-pass66-working.json)
passes 1008 methods in 130 suites, including all distinct working61--66
additions. The [proof audit](research/proof-audits-pass66-working.md)
records the complete independent AI reviews and capture provenance.
There is no human expert review, formal proof, novelty certification,
or universal frame-existence proof. The central 544-claim registry
remains at its historical full60 integration state.

The [working66 integrity packet](research/checkpoint-pass66-working.json)
records the new artifacts and revalidates the frozen predecessors.

~~~sh
/opt/anaconda3/bin/python research/run_regression_pass66.py
/opt/anaconda3/bin/python research/dependent_low_flow_rank_checks_pass66.py
/opt/anaconda3/bin/python research/consistency_checks_pass66.py
~~~

## Previous working result: low-flow rank reduction

The [working65 synthesis](research/low-flow-synthesis-pass65.md)
narrows the low-flow part of the supplied two-quadratic frame to one
remaining configuration: dependent defects with no constant relation,
flow degree two, a nonconstant-projective curve of bad speeds, and
joint leading rank three. This is a necessary residual list, not an
existence claim or a general cancellation solution.

The [speed-curve graph theorem](research/dependent-speed-curve-graph-pass65.md)
and [dependent low-flow theorem](research/dependent-low-flow-pass65.md)
recognize the other specified low-flow branches. Separate
[cubic normal forms](research/constant-top-cubic-pass65.md) reduce,
but do not close, that higher-flow case. A further audit proves the
[cubic correction has zero parameter motion](research/constant-top-cubic-heisenberg-pass65.md);
its earlier proposed positive-motion subcase was empty and is not
counted as a recognition advance.

The [actual moving-frame control](research/moving-frame-divisibility-control-pass65.md)
refutes automatic speed divisibility and automatic nonvanishing of
a proposed repair. It is already recognized by an omitted direction.
The [captured checks](research/verification-pass65-working.json)
pass four new methods in two suites and rerun 26 existing methods.
The [proof audit](research/proof-audits-pass65-working.md) distinguishes
these checks and independent AI reviews from human or formal verification.
These working proofs remain outside the historical full60 counts.
The [working65 integrity packet](research/checkpoint-pass65-working.json)
freezes eleven artifacts, checks their local links and exact checker
structure, and revalidates the prior working64 and frozen full60 files.

## Previous working result: actual quadratic graphs

The newest [working theorem](research/actual-quadratic-graph-cancellation-pass64.md)
recognizes the original kernel for the full actual independent-defect
quadratic graph of pass44. A rational Euler-field argument either
removes all varying graph coefficients or produces an actual
ambient invariant coordinate; the latter permits the established
Dedekind-base cancellation theorem to apply.

Two independent AI reviewers read the complete proof and found no
gap. This closes that supplied graph, not unrestricted cancellation
or the existence of a universal frame. It has no human expert review,
formal verification, or novelty certification.

The supporting [graph rigidity theorem](research/rational-euler-graph-rigidity-pass63.md)
also excludes every exact positive monomial speed pair under the
actual frame assumptions. The [local normalization note](research/ramified-normalization-scope-pass62.md)
keeps actual local parameters separate from formal root extensions.
These working61–64 proofs are outside the full60 registry and
regression counts below. The [standalone verification](research/verification-pass64-working.json)
adds one method in one suite, plus uncounted exact identity controls;
it is not a fresh full-project regression or a formal proof.

The [frozen working packet](research/checkpoint-pass64-working.json)
records thirteen artifacts and revalidates all 168 nonmutable full60
hash records. The [dependency map](research/post-graph-closure-scope-pass64.md)
identifies the remaining constant-top, moving-top, and dependent-defect
sectors. A [three-paper applicability audit](research/graph-recognition-literature-scope-pass64.md)
checks the source hypotheses without claiming historical novelty.

~~~sh
/opt/anaconda3/bin/python research/square_speed_leading_checks_pass61.py
~~~

## Historical full60 checkpoint: coordinate compatibility

The full60 [coordinate-compatibility report](deep-pass-60.md)
excludes every simple common zero of the actual bad-coordinate
speeds. It uses exact local Euler eigenfunctions and the full
good-coordinate equations. This eliminates the older extra
parameter-speed sector, not every reduced intrinsic image point.

A divisor theorem excludes nonconstant reduced projective speed
directions at genuine plinth or common-speed divisors. The full
fixed-pair quadratic classification rules out every compatible
good-generator choice in the faithful control.

The [captured full60 regression](verification-pass-60.json) passes
**1000 exact methods across 126 suites**, adding five methods in
three suites to full57. There are 544 scoped registry entries.
The [synthesis audit](research/synthesis-audit-pass60.md) separates
written proofs from finite checks. There is no human expert review,
Lean proof, novelty certification or general cancellation solution.

~~~sh
/opt/anaconda3/bin/python research/run_regression_pass60.py
/opt/anaconda3/bin/python research/faithful_frame_rank_checks_pass58.py
/opt/anaconda3/bin/python research/faithful_quadratic_module_checks_pass59.py
/opt/anaconda3/bin/python research/simple_speed_zero_checks_pass60.py
/opt/anaconda3/bin/python research/consistency_checks_pass60.py
~~~

The [working58–60 packet](research/checkpoint-pass60-working.json)
retains its historical standalone-stage flags. No intermediate
full58 or full59 run is invented. New61 work is outside these
counts. Ramified speed zeros and the universal frame problem
remain unresolved in this checkpoint.

## Previous checkpoint: affine-slice and radial boundary

The latest [slice-selection and radial-boundary report](deep-pass-57.md)
proves that the actual generic-affine functions form a finite free
rank-three module. Its derivative image is a two-generated base
ideal; an affine slice exists exactly when that ideal is the unit ideal.

A smooth faithfully flat polynomial-cylinder control has minimum
slice-gauge degree exactly three. Its four quadratic generators are
not ambient coordinates. This disproves the weaker generator shortcut,
not the full coordinate-frame implication. A separate argument rules
out regular radial centers at genuine primitive plinth divisors.

The [captured pass57 regression](verification-pass-57.json) passes
**995 exact methods across 123 suites**. This consolidation adds eight
scoped claims, for 539 total, and zero numerical methods or suites.
The [independent synthesis audit](research/synthesis-audit-pass57.md)
separates written proofs, source applications and finite controls.
There is no human expert review, Lean proof, novelty certification
or unrestricted cancellation solution.

~~~sh
/opt/anaconda3/bin/python research/run_regression_pass57.py
/opt/anaconda3/bin/python research/consistency_checks_pass57.py
~~~

This checkpoint integrates frozen working55, working56 and working57
without rewriting their historical standalone-stage flags. The
new pass58 and later investigations remain outside these counts.
The actual-frame recognition and unrestricted frame-reduction gaps
remain open.

## Previous checkpoint: quintic and whole-fiber obstruction

The latest [quintic and whole-fiber report](deep-pass-54.md)
constructs the entire fifth filtration in the actual reduced
zero-first-jet sector: I5=p^3R and F5=F4 plus RY.

Its generated algebra still cannot equal the actual ring.
The induced derivation kills the whole quintic image on the
closed fiber, but a primitive derivation on the actual smooth
factorial threefold cannot kill the entire scheme fiber.
Every generating set in this sector therefore needs intrinsic
degree at least six. Nilpotents are retained throughout.

The same report identifies the separate slice-selection gate.
A projected F5 list is already a projected F4 list; arbitrary
high-degree slice replicas do not disprove the existence of a
different bounded choice. No upper bound on the minimum
generating degree is supplied by the generic quadratic graph.

The [captured pass54 regression](verification-pass-54.json) passes
**995 exact methods across 123 suites**, including the one new
two-method quintic suite. There are 531 scoped claims. The
[construction audit](research/proof-audits-pass53-working.md),
[geometric audit](research/proof-audits-pass54-working.md) and
[synthesis audit](research/synthesis-audit-pass54.md) distinguish
written proofs and primary-source applications from finite checks.
There is no human expert review, Lean proof, historical novelty
certification or unrestricted cancellation solution.

~~~sh
/opt/anaconda3/bin/python research/run_regression_pass54.py
/opt/anaconda3/bin/python research/quintic_correction_checks_pass53.py
/opt/anaconda3/bin/python research/consistency_checks_pass54.py
~~~

This checkpoint consolidates the separate
[working53](research/checkpoint-pass53-working.json) and
[working54](research/checkpoint-pass54-working.json) packets
directly after pass52. Their historical standalone-stage flags
remain unchanged. No intervening full pass53 regression is
invented, and new pass55 work is outside these counts.

The full supplied profile, residual global recognition and
universal frame reduction remain unresolved. The original
cancellation goal has not been narrowed.

## Previous checkpoint: fourth image and fibration boundary

The preceding [fourth-image and fibration report](deep-pass-52.md)
settles the fourth-image alternative in the actual reduced,
zero-first-jet sector: I4=p^2m. The entire F4 module has the
explicit free basis 1,z,w,U,V.

Its generated algebra has an exact saturated three-equation
presentation. The closed fiber remains a finite nonempty scheme
times an affine plane, so the full F4 algebra cannot equal the
actual ring with a curve fiber. Every generating set in this sector
requires intrinsic degree at least five. Rank-one first jets at
general reduced obstruction points are not covered.

The polynomial intrinsic quotient does not supply an affine-plane
fibration automatically. For the chosen action, the fibration
premise holds precisely when its primitive plinth is a unit;
proper finite divisor constant fields block it otherwise. A
polynomial control shows that this relative failure is compatible
with an already polynomial threefold.

The [captured pass52 regression](verification-pass-52.json) passes
**993 exact methods across 122 suites**, including four new methods
in two suites. There are 523 scoped claims. The
[working proof audit](research/proof-audits-pass52-working.md),
[applicability audit](research/universal-frame-reduction-audit-pass52.md)
and [synthesis audit](research/synthesis-audit-pass52.md)
distinguish actual proofs and assumptions from finite controls.
There is no human expert review, Lean proof, novelty certification
or unrestricted cancellation solution.

~~~sh
/opt/anaconda3/bin/python research/run_regression_pass52.py
/opt/anaconda3/bin/python research/fourth_image_boundary_checks_pass52.py
/opt/anaconda3/bin/python research/quartic_fiber_gate_checks_pass52.py
/opt/anaconda3/bin/python research/consistency_checks_pass52.py
~~~

The [working snapshot](research/checkpoint-pass52-working.json)
retains the earlier standalone-only stage and its historical flags.
The expanded captured regression supersedes that earlier scope
without rewriting it. New pass53 quintic and fiber-support work
is not counted in this checkpoint.

The actual higher-degree algebra, full supplied profile, residual
global recognition and universal actual-frame reduction remain
unresolved. The original cancellation goal has not been narrowed.

## Previous checkpoint: cubic non-generation and quartic corrections

The preceding [cubic and quartic report](deep-pass-51.md) proves that
the entire algebra generated by intrinsic degree at most three
cannot equal the actual algebra at a reduced second-image obstruction.
Its exact presentation retains a two-dimensional closed fiber.

An ordinary triple of the full plinth forces any actual second-image
obstruction there to be reduced. At reduced points with vanishing
first jet, actual flatness supplies quartic corrections and a two-ideal
alternative for the fourth image. This checkpoint does not choose
between the alternatives or prove degree-four generation.

The two good velocity residues are killed by the intrinsic derivation
on the whole possibly nonreduced fiber. In the rank-zero case they
generate, together with the degree-two image, a subalgebra of complex
dimension at most six. This is not a bound on the full curve fiber.

The [captured pass51 regression](verification-pass-51.json) passes
**989 exact methods across 120 suites**, including five new methods
in two suites. There are 517 scoped claims. The
[working proof audit](research/proof-audits-pass51-working.md),
[foundational source audit](research/intrinsic-quotient-foundation-audit-pass51.md)
and [synthesis audit](research/synthesis-audit-pass51.md)
distinguish written proofs, AI reconstructions, finite tests and
inherited sources. There is no human expert review, Lean proof,
historical novelty claim or unrestricted cancellation solution.

~~~sh
/opt/anaconda3/bin/python research/run_regression_pass51.py
/opt/anaconda3/bin/python research/cubic_generation_obstruction_checks_pass51.py
/opt/anaconda3/bin/python research/triple_point_quartic_checks_pass51.py
/opt/anaconda3/bin/python research/consistency_checks_pass51.py
~~~

The [working snapshot](research/checkpoint-pass51-working.json)
retains the historical standalone-only stage. Its no-full-regression
flag is superseded by the captured expanded regression, not rewritten.
New pass52 work is not included in these registry or test totals.

The full supplied profile, actual higher-degree generation, residual
global quadratic recognition and universal actual-frame reduction
remain open. A conditional local result does not settle the original goal.

## Previous checkpoint: multi-tangent bounds and localized slices

The preceding [multi-tangent and slice-boundary report](deep-pass-50.md)
proves p in m^2J whenever the reduced plinth support has two
distinct tangent directions at an actual obstruction point.
The exact ordinary-triple control shows that trace and normalized
cover conditions alone do not eliminate higher multiplicity.
That control explicitly fails actual flatness and prime pullbacks.

At the remaining simultaneous speed/acceleration zero fibers,
two actual F2 invariants cover the entire scheme-theoretic fiber.
However, bounded polynomial slices on those nonempty opens already
descend to the original local ring. In the genuine quadratic graph,
one F3-bounded projected original-coordinate list is already
F2-bounded, so cannot repair an actual second-image basepoint.
This argument alone does not rule out another F3 generating set.

An invariant etale square-root construction does give actual local
slices. A genuine lower-profile polynomial-coordinate control shows
that their intrinsic derivative degree can be infinite. It is not
an unresolved full-frame realization or a cancellation counterexample.

The [captured pass50 regression](verification-pass-50.json) passes
**984 exact methods across 118 suites**, including four new methods
in two suites. There are 509 scoped claims. The
[working proof audit](research/proof-audits-pass50-working.md) and
[synthesis audit](research/synthesis-audit-pass50.md) keep universal
written proofs separate from finite checks and inherited source inputs.
There is no human expert review, Lean proof or novelty certification.

~~~sh
/opt/anaconda3/bin/python research/run_regression_pass50.py
/opt/anaconda3/bin/python research/multitangent_plinth_boundary_checks_pass50.py
/opt/anaconda3/bin/python research/fiber_invariant_opens_checks_pass50.py
/opt/anaconda3/bin/python research/consistency_checks_pass50.py
~~~

The [working snapshot](research/checkpoint-pass50-working.json)
retains its historical pre-integration flags. The captured full
regression above supersedes its earlier standalone-only scope.
New pass51 notes, if present, are not counted in this checkpoint.

The full supplied (1,1,2,2) profile, the higher-degree actual
fiber algebra, residual global quadratic recognition and universal
actual-frame existence remain unresolved. A special-case result
does not settle the original cancellation goal.

## Previous checkpoint: normalized covers and frame generation

The preceding [normalized-cover and frame report](deep-pass-49.md)
proves that every normalized exceptional-cover point is reached
in the actual contractible quotient. Its no-poles corollary makes
the full exceptional invariant ring finite over the base curve.
This uses the whole-fiber homology argument, not a general claim
that normalization preserves surjectivity.

Within the actual quadratic setup, the trace of the minimal-slice
residue excludes ordinary nodes from second-image obstruction
support, including nonreduced obstruction schemes. A reduced full
plinth with only ordinary nodes therefore gives J=C and a full
global quadratic equation. Polynomial recognition of that equation
with intersecting or nodal plinth components remains separate.

The original supplied frame also gives A_R=R[F2_R] wherever
(f,g,h1,h2)R=R. Hence every second-image obstruction lies at a
simultaneous zero of these four invariants, in the singular full
plinth locus and away from ordinary nodes. No universal-frame
existence or solution of the complete (1,1,2,2) profile follows.

All **980 exact methods across 116 suites** pass in the
[captured pass49 regression](verification-pass-49.json). There
are 500 scoped claims. The [proof/source audit](research/proof-audits-pass49.md)
and [synthesis audit](research/synthesis-audit-pass49.md) distinguish
universal written arguments from finite polynomial controls.
There is no human expert review, Lean proof or novelty claim.

Reproduce the pass49 regression (its shared-metadata integrity
checker is historical after pass50 integration):

~~~sh
/opt/anaconda3/bin/python research/run_regression_pass49.py
/opt/anaconda3/bin/python research/frame_filtration_generation_checks_pass49.py
/opt/anaconda3/bin/python research/consistency_checks_pass49.py
~~~

The [working snapshot](research/checkpoint-pass49-working.json)
records the earlier standalone checks before full integration.
Its historical no-full-regression flag is superseded by the
captured regression above, not silently rewritten.

Next bounded tasks: control the whole algebra at simultaneous
zero fibers, use flatness and prime exceptional pullbacks at more
singular plinth points, and address the separate global quadratic
recognition and universal-frame obligations. New pass50 working
notes, if present, are not included in this checkpoint's totals.

## Previous checkpoint: cubic correction and cusps

The preceding [cubic-correction and cusp report](deep-pass-48.md)
proves stronger conditional restrictions on the remaining quadratic
branch. At a reduced local second-image obstruction J=m, actual
regular-sequence division supplies a cubic element. The third image
is principal, I3=p^2, even though the second image pJ is not.

A unit determinant of the derivative coefficient matrix would make
the cubic subalgebra the entire actual ring, with a reduced
translation-line fiber forbidden by the plinth theorem. Thus the
first-jet matrix has rank at most one. The same argument applies
at nonreduced J only under the explicit extra premise B1,B2 in J.

Lowest conic coefficients further distinguish the two surviving
reduced-J configurations. Rank one confines the degree-two image
to an affine line; rank zero makes its actual image algebra
finite-dimensional of dimension at most three, retaining nilpotents.
Neither assertion describes the entire quotient fiber.

After the separate assumption J=C supplies a full global quadratic
equation, smooth reduced plinth support allows repeated factors.
Contractibility then forces each residue to be a pure odd power
of one linear polynomial. A genuine cusp requires repeated
plinth multiplicity and a nonzero transverse derivative.
The inherited Russell cubic realizes the weaker topology and
all-image-principality package while remaining nonpolynomial.
No polynomial cylinder or target coordinate frame for it is asserted.

The prior smooth reduced full-plinth recognition remains proved
within its actual quadratic setup. The full supplied (1,1,2,2)
profile and universal actual-frame reduction remain open.
Complete H<=9 and supplied (1,1,1,3),(0,2,2,2) coverage are unchanged.
There is no unrestricted solution or novelty claim.

All **979 exact methods across 115 suites** pass in the
[pass48 full regression](verification-pass-48.json), including five
new methods in two standalone suites. There are 492 scoped claims.
The [proof/source audit](research/proof-audits-pass48.md),
[initial-form audit](research/initial-conic-audit-pass48.md) and
[synthesis audit](research/synthesis-audit-pass48.md) separate written
arguments, finite controls and inherited published inputs.
No human expert review or Lean verification is asserted.

Reproduce the pass48 regression (its shared-metadata integrity
checker is historical after pass49 integration):

~~~sh
/opt/anaconda3/bin/python research/run_regression_pass48.py
/opt/anaconda3/bin/python research/third_image_cubic_gate_checks_pass48.py
/opt/anaconda3/bin/python research/repeated_smooth_support_checks_pass48.py
/opt/anaconda3/bin/python research/consistency_checks_pass48.py
~~~

Next bounded tasks: use the original coordinate frame to control
the whole algebra at lower-rank or nonreduced obstruction points;
address genuine cuspidal thickenings after J=C; and complete the
separate moving-frame and universal-reduction obligations.

## Preceding checkpoints

The [pass-47 report](deep-pass-47.md) identified the exact
second-image section-zero scheme, confined it to singular points
of the full plinth, and recognized the smooth reduced full-plinth
case with explicit coordinates. Its
[saved regression](verification-pass-47.json) contains 974 methods
in 113 suites and its historical artifacts remain unchanged.

~~~sh
/opt/anaconda3/bin/python research/run_regression_pass47.py
/opt/anaconda3/bin/python research/flat_conic_gate_checks_pass47.py
/opt/anaconda3/bin/python research/smooth_plinth_recognition_checks_pass47.py
/opt/anaconda3/bin/python research/second_image_countercontrol_checks_pass47.py
/opt/anaconda3/bin/python research/consistency_checks_pass47.py
~~~

The [pass-46 report](deep-pass-46.md) proved the good-direction
recognition and ramification gates, full quadratic divisor models,
normalized one-branch covers, and the exact second-image criterion.
Its [saved regression](verification-pass-46.json) contains 964 methods
in 110 suites. The current report strengthens its closed-point and
hypersurface-recognition results; its historical files are unchanged.

~~~sh
/opt/anaconda3/bin/python research/run_regression_pass46.py
/opt/anaconda3/bin/python research/dependent_motion_ramification_checks_pass46.py
/opt/anaconda3/bin/python research/moving_commuting_repair_checks_pass46.py
/opt/anaconda3/bin/python research/minimal_quadratic_slice_checks_pass46.py
/opt/anaconda3/bin/python research/consistency_checks_pass46.py
~~~

The [pass-45 report](deep-pass-45.md) recognized both nonconstant
high-flow zero-motion branches and classified full divisor models
where a speed or acceleration is a unit. Its
[saved regression](verification-pass-45.json) has 954 methods in
107 suites. The current local lifting strengthens its remaining
simultaneous-divisor boundary. Its historical proofs and checkers
remain unchanged.

~~~sh
/opt/anaconda3/bin/python research/run_regression_pass45.py
/opt/anaconda3/bin/python research/quadratic_divisor_checks_pass45.py
/opt/anaconda3/bin/python research/rotating_zero_motion_checks_pass45.py
/opt/anaconda3/bin/python research/actual_partial_obstruction_checks_pass45.py
/opt/anaconda3/bin/python research/independent_zero_motion_checks_pass45.py
/opt/anaconda3/bin/python research/consistency_checks_pass45.py
~~~

The [pass-44 report](deep-pass-44.md) established the actual generic
quadratic graph, determinant-square denominator bound, principal
compatibility support and preceding-layer normal forms. Its
[saved regression](verification-pass-44.json) has 939 methods in
103 suites. The new report strengthens its zero-motion and full-divisor
conclusions; all historical proof and checker files remain unchanged.

~~~sh
/opt/anaconda3/bin/python research/run_regression_pass44.py
/opt/anaconda3/bin/python research/generic_bad_pair_checks_pass44.py
/opt/anaconda3/bin/python research/dependent_preceding_curve_checks_pass44.py
/opt/anaconda3/bin/python research/compatible_slice_support_checks_pass44.py
/opt/anaconda3/bin/python research/independent_preceding_layer_checks_pass44.py
/opt/anaconda3/bin/python research/consistency_checks_pass44.py
~~~

The [pass-43 report](deep-pass-43.md) constructs the global Heisenberg
normalizer and commuting repair, proves the omitted-coordinate
recognition criterion, and excludes rank-one bad projection with
independent speeds. Its [saved regression](verification-pass-43.json)
contains 924 methods in 99 suites. Its proof and checker files remain
frozen. The current common-base audit supersedes only the overly
conservative roadmap claim that the abstract invariant base was unknown.

~~~sh
/opt/anaconda3/bin/python research/run_regression_pass43.py
/opt/anaconda3/bin/python research/heisenberg_repair_checks_pass43.py
/opt/anaconda3/bin/python research/bad_projection_determinant_checks_pass43.py
/opt/anaconda3/bin/python research/dependent_defect_top_line_checks_pass43.py
/opt/anaconda3/bin/python research/bad_projection_rank_closure_checks_pass43.py
/opt/anaconda3/bin/python research/consistency_checks_pass43.py
~~~

The [pass-42 report](deep-pass-42.md) recognizes the complete supplied
(0,2,2,2) profile without transferring a slice to its three-variable
base. It records the degree-two leading-plane reduction, the higher
power law and the quantified leading-module repair obstruction.
Its [saved regression](verification-pass-42.json) has 906 methods in
95 suites. The latest report strengthens several residual conclusions;
its original proofs and checkers remain unchanged.

~~~sh
/opt/anaconda3/bin/python research/run_regression_pass42.py
/opt/anaconda3/bin/python research/three_variable_quadratic_frame_checks_pass42.py
/opt/anaconda3/bin/python research/dependent_quadratic_defects_checks_pass42.py
/opt/anaconda3/bin/python research/two_quadratic_degree_two_checks_pass42.py
/opt/anaconda3/bin/python research/two_quadratic_top_line_checks_pass42.py
/opt/anaconda3/bin/python research/leading_plane_repair_checks_pass42.py
/opt/anaconda3/bin/python research/consistency_checks_pass42.py
~~~

The [pass-41 report](deep-pass-41.md) recognized the complete supplied
one-cubic-column family with 881 methods across 90 suites. Its exact
speed classification, actual shears and global one-good-partial lemma
remain unchanged. Its [Lie-rigidity scope check](research/lie-rigidity-scope-pass41.md)
also remains valid.

~~~sh
/opt/anaconda3/bin/python research/run_regression_pass41.py
/opt/anaconda3/bin/python research/three_output_cubic_speed_checks_pass41.py
/opt/anaconda3/bin/python research/three_output_cubic_closure_checks_pass41.py
~~~

The [pass-40 report](deep-pass-40.md) closed the constant-top degree-six,
constant-factor degree-five and dependent-output degree-five branches,
with 869 methods in 88 suites. Its remaining three-output case is now
closed by the current report. The proof/checker files are unchanged.

~~~sh
/opt/anaconda3/bin/python research/run_regression_pass40.py
/opt/anaconda3/bin/python research/cubic_degree_six_checks_pass40.py
/opt/anaconda3/bin/python research/cubic_degree_five_checks_pass40.py
/opt/anaconda3/bin/python research/two_defect_critical_locus_checks_pass40.py
/opt/anaconda3/bin/python research/nice_centralizer_checks_pass40.py
/opt/anaconda3/bin/python research/two_output_cubic_checks_pass40.py
~~~

The [pass-39 report](deep-pass-39.md) established polynomiality through
flow degree four in the one-cubic profile, the two-defect rank dichotomy,
and exact supplied-family coordinate-reduction criteria. Its two remaining
cubic configurations are narrowed further by the current report.
Its [saved regression](verification-pass-39.json) has 846 methods in
83 suites. Pass 39 also reconciles pass 38's frame proof with the
stronger earlier H<=9 threshold; the fixed-model integrability result
from pass 38 is unaffected.

~~~sh
/opt/anaconda3/bin/python research/run_regression_pass39.py
/opt/anaconda3/bin/python research/one_cubic_defect_checks_pass39.py
/opt/anaconda3/bin/python research/two_quadratic_defects_checks_pass39.py
/opt/anaconda3/bin/python research/coordinate_reduction_checks_pass39.py
/opt/anaconda3/bin/python research/consistency_checks_pass39.py
~~~

The [pass-38 report](deep-pass-38.md) completes the vanishing branch
of the fixed primitive polynomial normal form: actual integrability
holds exactly when rad(p) divides g, Q0=q0+q1*T with q1 nonzero, and
g1=2/(3*q1). The full overlapping divisor and repeated roots are
retained; every vanishing-branch primitive top remains nonsliced.
This classification is unaffected by the frame-result reconciliation.
Its whole-frame proof remains a weaker alternate argument, not a
new polynomiality gap beyond the earlier height-eight theorem.

Its [saved regression](verification-pass-38.json) has 824 methods
across 80 suites, including fourteen new methods at that checkpoint.

~~~sh
/opt/anaconda3/bin/python research/run_regression_pass38.py
/opt/anaconda3/bin/python research/actual_frame_checks_pass38.py
/opt/anaconda3/bin/python research/vanishing_plinth_integrability_checks_pass38.py
/opt/anaconda3/bin/python research/consistency_checks_pass38.py
~~~

The preceding [rank-two candidate report](deep-pass-37.md) finishes the
explicit Su-cell investigation. The selected four-coordinate action is
simultaneous translation, with polynomial quotient coordinates
b-a, c-a, d-a. The actual first braid parameter is a coordinate slice
on every rank-two affine fiber, including those with additional affine
factors. Thus all 80 indexed threefold candidates in Remark 2.12 are
affine three-spaces under the audited construction.

This does not solve general cancellation. The [literature audit](research/literature-scope-pass37.md)
found definite prior credit: Mellit already states compatible rank-two
cancellation. The present work is a reconstruction and identification of
Su's factors, not a new rank-two cancellation theorem. Both Su's arXiv
and actually retrieved journal definitions were checked, including
the exact equivariant projection and quotient fiber.

All **810 exact methods across 78 suites** pass in the
[saved full regression](verification-pass-37.json). Eight methods
are new. The [proof audit](research/proof-audits-pass37.md) distinguishes
AI reconstructions, finite algebraic controls and prior literature.
There is no expert review, Lean verification or novelty claim.

Reproduce the pass-37 checkpoint:

```sh
/opt/anaconda3/bin/python research/run_regression_pass37.py
/opt/anaconda3/bin/python research/su_cell_checks_pass37.py
/opt/anaconda3/bin/python research/consistency_checks_pass37.py
```

That checkpoint's next question concerned higher-rank residual actions.
Their source stabilization is by more than one variable, so pass 38
instead returns to the original single-line cylinder. Do not resume
nonpolynomiality searches over these 80 rank-two indices without a
specific error in the proof.

The preceding [separated-torsor and integrability report](deep-pass-36.md)
closes the auxiliary ambient-action route at every exponent. Under any
hypothetical hypersurface presentation of the unchanged pinched surface,
no ambient additive action can induce a nonzero action on the surface.
The proof constructs actual open quotient charts and contradicts
separatedness of their total space. It does not exclude an embedding
without extendable actions or solve the original conjecture.

Every prescribed degree-one polynomial normal form now has an exact
single-correction integrability criterion. On p(0)!=0 it is constructive
and necessary-and-sufficient. A genuine example with common derivative
x² still has a nonsliced primitive top. These statements concern the
fixed polynomial model, not an unknown cylinder.

Under the actual cylinder hypothesis and intrinsic rank one, preservation
of the invariant plane by a degree-one ambient action is equivalent to
local nilpotence of a specified double commutator. Neither property is
proved automatic. A [source-audited Su cell](research/su-candidate-lead-pass36.md)
was the next explicit-action reconstruction target at that checkpoint,
not a proved nonpolynomial candidate. Pass 37 resolves its recognition.

All **802 exact methods across 77 suites** pass in the
[saved full regression](verification-pass-36.json). Thirteen methods
are new. Separate AI proof reconstructions are documented in the
[audit](research/proof-audits-pass36.md); they are not expert review,
formal proof or verification of novelty.

Reproduce the pass-36 checkpoint and its two new suites:

```sh
/opt/anaconda3/bin/python research/run_regression_pass36.py
/opt/anaconda3/bin/python research/nodal_fork_checks_pass36.py
/opt/anaconda3/bin/python research/q1_integrability_checks_pass36.py
/opt/anaconda3/bin/python research/consistency_checks_pass36.py
```

The preceding [cylinder, pencil and nodal-exhaustion report](deep-pass-35.md)
classifies the entire degree-one horizontal sector of the fixed canonical
polynomial model. Every such pair has a common polynomial local slice,
a finite nilpotent all-LND Lie algebra of generic rank three, and a
constant-speed triangular boundary form. A polynomial repair path for
every horizontal remains unproved, and the model already has a polynomial
quotient. These conclusions do not settle an unknown threefold.

A supplied rank-three unipotent group on any threefold cylinder,
containing the slice translation, would give two commuting independent
intrinsic actions on its base. The existence of that group is still
unproved from the full polynomial-cylinder hypothesis.

At that checkpoint, the compatible nodal realization had an all-later-modification
restriction: every minimal quadratic lift has order strictly below
the full plinth exponent, so that exponent must be at least two.
Exponent one is excluded without assuming a one-step model. Higher
exponents and the arbitrary embedding question remained unresolved.
Pass 36 closes the former ambient-action question, not the latter.

All **789 exact methods across 75 suites** passed in that checkpoint's
[saved full regression](verification-pass-35.json). Twelve methods are
new. The source-dependent geometric argument has no artificial numerical
suite. No general solution, novelty, expert review or formalization is
claimed. The [proof audit](research/proof-audits-pass35.md) separates
written reconstruction from finite controls.

Reproduce the pass-35 regression and its two new suites:

```sh
/opt/anaconda3/bin/python research/run_regression_pass35.py
/opt/anaconda3/bin/python research/isolated_node_checks_pass35.py
/opt/anaconda3/bin/python research/general_q1_repair_checks_pass35.py
/opt/anaconda3/bin/python research/consistency_checks_pass35.py
```

The preceding [integral-isolation and repair report](deep-pass-34.md)
proves that a hypothetical compatible ambient action on the fixed
conductor surface would have an isolated nodal plinth component. Integer
ramification restrictions exclude intersections with other components,
but do not construct or exclude the remaining realization.

An exact geometric generic class-group formula closes a proposed
factorial-slicing shortcut, including a countercontrol satisfying the
full polynomial-cylinder hypothesis for every coordinate in its chosen
invariant plane. It does not rule out intrinsic rank one. A polynomial
path repairs the explicit arbitrary-plinth family at degree one, while
the standard scaling path has an exact degree-five barrier. Neither is
a universal repair or cancellation argument.

The unrestricted conjecture is not solved. These are scoped written
proofs and independently checked algebraic controls, not human peer
review, a Lean formalization or an established novelty claim.

The preceding [all-speed and nonlinear-selection report](deep-pass-33.md)
removes the nonzero-speed premise from the conditional surface action
obstruction. In every hypothetical hypersurface presentation, the set
of surface LNDs with ambient extensions is either zero or exactly the
odd-multiplier subspace u*(C+(u^4-1)C[u^2])*delta_0. A particular even
action has divergence-free lifts at every finite order but no ambient
LND lift. The presentation itself is still unknown.

The same fixed canonical polynomial model now has degree-one
global minimizing horizontals with arbitrary prescribed primitive-top
plinth divisors away from x=0, including multiplicities. Full polynomial
inverse maps, kernel, plinth and fixed scheme are proved. This refutes
another selection shortcut but retains successful choices in that model.

All nonlinear coordinate frames recover exactly the generic span of
intrinsic additive actions. The prior three-field determinant exists
if and only if ML(A)=C; neither condition is proved from the full
cylinder hypothesis. The open-orbit one-seed mechanism already follows
from published flexibility theory and is explicitly credited.

If the surface's surviving odd action extends, every minimal local
slice forces a singular quadratic first modification at the node.
A smooth realization must enlarge it; all later repairs remain
unclassified. No general cancellation solution, novelty, human
expert review or proof-assistant verification is claimed.

The preceding [residue and selection-obstruction report](deep-pass-32.md)
proves a conditional obstruction for the unchanged conductor surface:
under any hypersurface presentation, an ambient additive action of
nonzero conductor speed must have the exact nodal invariant image
C+(u^4-1)C[u^2] and an odd multiplier. The actual action
(u+u^4-1)delta_0 cannot have any such ambient extension. This does
not exclude the surface embedding, which remains unknown, or
the different action u*delta_0. It does not compute the divergence
obstruction of the excluded action.

A separate actual polynomial counterexample has global minimum
horizontal degree one but a nonsliced primitive top. This refutes
the every-unrestricted-minimizer rule, while retaining both a good
minimizer and the positive triangular-sector theorem. Full polynomial
inverse formulas and the slice-ring kernel and plinth are included.

The divergence obstruction factors through an exact four-dimensional
source quotient; its four target classes remain uncomputed.
A finite cross-frame determinant is sufficient for intrinsic
Makar-Limanov triviality, but its existence for every polynomial
cylinder is unproved. No general cancellation solution, novelty,
human review or formalization is claimed.

The preceding [minimum-degree and ambient-lifting report](deep-pass-31.md)
proves that the canonical model's minimum over all x-fixing horizontal
actions is one, not two. Every minimizer in the triangular sector has
a sliced primitive top, and an explicit nontangent minimizer escapes
the old normalizer reduction. Sliced tops for every unrestricted
minimizer were unproved there and are refuted in pass 32. Selection
for an unknown cylinder remains unproved.

Conditional on any hypersurface presentation of the unchanged
conductor surface, every classified LND has an exactly
equation-preserving polynomial derivation lift. It induces an LND
on every finite equation-adic thickening. This still does not give
an ambient LND: explicit sliced, even divergence-free, controls
pass all thickenings while their ambient iterates never vanish.
A general prime-hypersurface criterion, a sharp index-growth lower
bound and a finite sufficient degree certificate identify the
required extra uniformity. A separate divergence obstruction is
an uncomputed equation-torsion class, not an embedding obstruction.

The symmetry control is now contractible: the Koras-Russell cubic
has only trivial vector bundles and a codimension-one flexible
cylinder, yet no intrinsic LND tangent frame. Full flexibility
or a polynomial cylinder is not asserted. The full cancellation
hypothesis already gives free projective modules; compatible
additive symmetry extraction remains the missing step.
No general solution, novelty, human review or formalization is claimed.

The preceding [frame, gauge and all-symmetry report](deep-pass-30.md)
classifies every additive action and every automorphism of the fixed
conductor surface. All nonzero actions have the same invariant ring,
and every automorphism fixes that ring pointwise. The actual module
spanned by additive velocities has exact Picard order four. Thus
changing the action cannot bypass the previous invariant-generator
obstruction; the all-noninvariant embedding case is still unresolved.

An exact two-shear calculation shows that finite closure is not
automatic in a prescribed polynomial frame, even when its sliced
derivation has an explicit polynomial kernel. Every affine-linear
frame replacement can fail while a nonlinear one succeeds. The
finite/infinite boundary is a special case of a published homogeneous
Lie-algebra criterion, not a new classification theorem.

Every supplied horizontal action in the established canonical frame
can be normalized constructively. But a fixed-locus obstruction shows
that doing so may necessarily change the vertical action. A classical
noncontractible Danielewski-cylinder control also disproves automatic
descent of transitive cylinder symmetry. None supplies the missing
universal recognition construction. The general conjecture is not solved.

The preceding [finite-closure and global-branch report](deep-pass-29.md)
removes solvability from the finite-Lie recognition criterion: actual
finite-dimensional closure with all ambient coordinate partials suffices
to triangularize an LND. In dimension four a slice then gives a polynomial
kernel. A published transitive-radical theorem supplies the bridge;
existence of a successful frame for every cylinder remains unproved.

The canonical nonunit model now has an exact all-parameter selection
criterion within the specified auxiliary-plane-fixing family. Equal
relative degrees can have opposite primitive-top slice outcomes.
The actual surface has a stronger global obstruction: no invariant of
its fixed action belongs to any generating triple, including d and
d(u^2-1), whose individual fibers are all planar. An abstract three-branch
quadratic obstruction explains this and has an explicit two-branch
boundary example. All-noninvariant triples and ambient rank-three
realization remain unresolved. The general conjecture is not solved.

The preceding [finite-symmetry and canonical-fiber report](deep-pass-28.md)
gives a sufficient finite transitive all-LND recognition criterion, with
a finite solvable version. Existence of the required symmetry for an
arbitrary cylinder is not proved. A fixed-frame finite word test detects
linear triangularization; a smaller published strong-Jacobian test
already does the same. An exact five-dimensional perfect Lie algebra
shows that finite closure alone does not imply linear triangularization.

An actual canonical model with nonunit full plinth has both a horizontal
choice whose primitive top is nonsliced and another choice whose top
is sliced. Selection is essential. The exact closed-fiber classification
of every invariant of the fixed surface excludes some possible generators,
but d and d(u^2-1) have planar fibers at every complex value. Their global
companion generators remain unresolved. The general conjecture is not
solved, and no novelty, human review or formal proof is claimed.

The preceding [intrinsic-boundary and special-fiber report](deep-pass-27.md)
proves that the fixed surface's h=0 fiber cannot embed in a plane.
Consequently no three-element generating set of that surface can contain h,
even with two arbitrary noninvariant replacements. Presentations replacing
h and the required ambient primitive-action realization remain unresolved.

For every intrinsic action on the unknown stable threefold, faithful
flatness makes the full plinth principal by an established gcd argument.
Its prime support is exactly where the boundary invariant field extension
has degree greater than one. This is compatible with the candidate surface;
it does not establish nonpolynomiality or a free action. The intrinsic
fence case closes under the additional, unproved condition that exceptional
surface fibers are factorial.

The free relative-plane completion is already covered by a published
two-variable theorem. A finite formula corrects any Bezout complement,
but existence of a useful free intrinsic action remains unproved.
An actual pair of sliced primitive coordinate actions has a nonsliced
primitive highest adjoint even with trivial joint rational invariants
and finite nilpotent Lie closure. One different bracket succeeds, so
all Lie-word methods are not excluded.

All four proofs received separate AI reconstructions and targeted
primary-source audits. General cancellation, novelty, human expert review
and proof-assistant verification remain incomplete.

The preceding [simultaneous-coordinate and realization report](deep-pass-26.md)
proves a conditional coordinate-completion criterion over a Q-domain:
a commuting unit-determinant pair of relative polynomial fields is an
actual coordinate frame if either field is locally nilpotent.
Removing that hypothesis is exactly a two-variable Jacobian-conjecture
reformulation. The missing relative plane and commuting complement
are not assumed to exist for an arbitrary threefold.

An actual plane-changing pair has only constant common polynomial and
rational invariants and an infinite-dimensional Lie closure, despite
finite repeated adjoints by one LND. Its primitive highest adjoint
nevertheless gives a successful sliced action and a new invariant plane.
The intrinsic centralizer argument separates a second commuting
direction from the much stronger coordinate or slice conclusion.
Published rank/fence theory is credited; fiberwise polynomiality is
not incorrectly promoted to a uniform trivialization over a surface.

For the fixed pinched surface, every invariant replacement retaining
g,h and every affine-linear projection of the given four-generator
embedding fails. An explicit rank-nine free basis over C[g,h] gives
an exact determinant criterion for future noninvariant generators.
The abstract generator bound remains three to four.
The general conjecture remains unsolved, with novelty, human review,
and proof-assistant verification unestablished.

The preceding [normalizer, elimination and algebraic-lifting report](deep-pass-25.md)
proves exact limits on three general approaches. A coordinate-pair row
operation preserves local nilpotence precisely when its coefficient is
invariant under the partial being subtracted. A forced leading cancellation
fails that test even though it lowers degree and sends a coordinate to one.
Regular saturation within a primitive rational orbit line cannot create
a missing slice.

For the principal-modification homotopy, every horizontal LND preserving
the old invariant subalgebra setwise must centralize the vertical action
and kill its full plinth. If the plinth divisor is not a fence, such a
horizontal action exists exactly when the full plinth divides the
perturbation. This uses published plane-stabilizer theory. Even a
specified polynomial fence family has no such normalizer, while a
successful horizontal partial exists outside that subalgebra.

The fixed surface is faithfully flat over its smaller nodal base,
despite being nonflat over its full invariant ring. Its invariant algebra
needs exactly two generators over the nodal base, excluding every
specified one-step algebraic modification. The first genuine quadratic
algebra/LND attempt has the wrong invariant defect and a singular line.
Arbitrary ambient polynomial realizations remain unexcluded.

The general conjecture remains unsolved. No novelty, human expert review,
or proof-assistant verification is claimed. The new proofs and report
received separate AI reconstructions, with scope corrections recorded.

The preceding [coordinate-reduction and invariant-lifting report](deep-pass-24.md)
gives an exact complementary criterion for coefficients c(f,h)+rB(f,h,x)
on the specified canonical base. Every positive case has global polynomial
coordinates. The example 1+2fxr is positive for all n>=1, but for n>=2
cannot be moved into the preceding coefficient ring C[f,h,r] by any
polynomial automorphism fixing the original base. The obstruction covers
gauges of every degree and has two independent written reconstructions.

The general routes have sharper limits: an entire plane-moving triangular
horizontal projection ansatz fails even on an explicitly polynomial family,
and all six canonical primitive tangent generators can fail local nilpotence
despite genuine descent. Successful coupled actions and combinations exist
in those controls. Neither result rules out an arbitrary useful action.

For the fixed pinched surface, the full invariant curve has one four-branch
point, not three nodes. Any prescribed ambient realization must have a
specific nonfree invariant-lifting defect. A module-only countercontrol
shows why free degree modules alone cannot eliminate that defect; it is
not an algebra derivation or an embedding obstruction. The unrestricted
conjecture remains unsolved, with priority and human/formal review absent.

The preceding [polynomial-coefficient and cancellation-gap report](deep-pass-23.md)
classifies every extension D+b*partial_t of the displayed canonical base
with b in C[f,h,r], for all n>=1. Two exact monic remainder conditions,
with the same nonzero constant coefficient, are necessary and sufficient
for a slice. Every positive case has global polynomial coordinates.
Both negative tests exclude every slice degree, using actual integral
orbit endpoints and a nonintegral translation parameter. Two independent
model reconstructions found no gap within the stated coefficient subring.

The same fixed pinched surface now has four explicit algebra generators,
with a short full-conductor Nakayama proof and a separate cotangent
reconstruction. Its minimum generator count is between three and four.
Neither an A^3 embedding nor the required ambient LND quotient is proved.

A general principal-modification deformation is smooth, stably polynomial
and trivial at all finite central jets, but its chosen natural horizontal
derivation is not locally nilpotent for nonzero perturbation. This does
not exclude other horizontal derivations. A separate exact restriction
gate shows why ambient actions need not descend to the slice section.
The unrestricted cancellation conjecture is still unsolved, mathematical
priority unresolved, and human/formal review absent.

The preceding [all-coefficient and recognition report](deep-pass-22.md)
classifies every extension D+(1+qr)*partial_t of the displayed canonical
primitive rank-three base: it has a slice exactly when f divides q,
and every positive case has polynomial kernel. It gives exact affine,
quadratic and adjacent cubic minimum-degree regimes. A finite nilpotent
correction and a multiple-root-safe algebraic orbit obstruction handle
the positive and negative directions in all coefficients.

A stronger counterexample rules out every full-center transport preserving
the reduced denominator support in a specified polynomial-modification
example, not merely one prescribed quotient jet. Two coordinate translations
show why tangent projection need not give a flat connection, and why even
a flat projected connection need not have a polynomial horizontal frame.
These refute particular proof steps, not cancellation.

The actual fixed conductor surface now has five explicit algebra generators
and a closed A^5 embedding, proved by finite-module recovery, exact polynomial
collision certificates, and global cotangent checks. Its minimum generator
count is between three and five. No A^3 embedding or ambient quotient is
constructed. The all-q proof has two independent model reconstructions;
the surface proof has a separate exact audit. Priority and human review
remain unresolved, and the unrestricted conjecture is not solved.

The preceding [noninvariant-extension and universal-bridge report](deep-pass-21.md)
proves that an explicit primitive rank-three family has quadratic slices
and polynomial kernels, but no slice affine in the original added variable.
It cannot be made into an invariant-coefficient extension while preserving
the original three-variable coordinate subring. The positive kernel proof
includes global polynomial coordinates and an independent inverse.

Every invariant principal modification now has an exact bounded-thickening
center presentation. An automatic lift of its prescribed reduced-identity
jet is false, even in an explicit case where a different full-center
transport works and the modified ring is polynomial. A separate coordinate
translation has no stable three-ring in any affine-linear frame.
Neither obstruction excludes all nonlinear frames or solves cancellation.

The actual conductor surface passes further global tests:
two normalization module generators, two conductor ideal generators,
Picard group (C*)^3 plus Z^2, and vanishing SK0. Its cotangent complex
has the necessary stable class of a hypersurface, but three algebra
generators and the required ambient quotient are still unconstructed.
Established local-slice, restriction/extension, modification, and
two-variable slice results are credited. Full-family priority remains
unresolved.

The preceding [nonunit-multiplier and conductor report](deep-pass-20.md)
proves polynomial kernels for every invariant slice extension of the
power-of-f local-slice family, using two finite polynomial corrections
and an actual global inverse. Arbitrary nonzero multipliers are covered
under explicit sufficient coefficient conditions; the separate
a=f-1,Q=h family admits all-slice coverage. A quadratic exception
has a smaller minimal plinth, so the general sufficient conditions
are not incorrectly promoted to necessity.

The unchanged inverse has an exactly quantified pole, repaired by
the corrected construction. A separate actual affine conductor
surface now realizes the earlier four-branch/three-component nodal
data, with a descended LND, trivial dualizing sheaf and matching
integral compact-support cohomology. It is not embedded as the
required exceptional surface of a global C3 quotient.

The [literal cylinder comparison](research/cylinder-comparison-pass20.md)
identifies the last-slice matrix as a published BPV construction.
The [further priority audit](research/priority-boundary-pass20.md)
reduces both weighted lifts to established Kaliman-Zaidenberg
modification theory, with explicit full-ideal saturation calculations.
Neither is a new abstract construction principle. Priority for the
specific compatible curve jets and uniform family conclusion is
unestablished. The general cancellation conjecture remains unsolved.

The preceding [iterated-coordinate and relative-classification report](deep-pass-19.md)
extends polynomial kernels to every invariant slice extension after an
additional additive local-slice construction, including its genuine
rank-three branch. A finite-chain version retains explicit final kernel,
local-slice and coefficient hypotheses. The construction supplies actual
global polynomial coordinates and an independently audited inverse;
it is not merely a formal-neighborhood identification.

For arbitrary primitive bases with connected reduced plinth, it also
proves that a principal modification is isomorphic over the original
invariant subring exactly when its coefficient is constant modulo the
full plinth. All higher image ideals and the associated graded algebra
are preserved even when that relative isomorphism is impossible.
A concrete old coordinate loses its affine-plane fibers despite the
modified ring being polynomial. That pass's nodal argument required
three disjoint contractible fiber components for the four-branch
control. Pass 20 realizes those surface-level data, while the global
ambient quotient remains unresolved.

The earlier [targeted priority audit](research/literature-boundary-pass19.md)
identifies exact prior work on pure-translation automorphisms, local-slice
replacement, and finite-congruence cylinder maps. The pass-20 comparisons
now resolve the precise cylinder step and weighted lifting principle
as inherited machinery. No novelty is established by the proof or tests.

The preceding [polynomial-curve and global-gap report](deep-pass-18.md)
extends the explicit invariant-extension coordinates to every monic curve
polynomial F of degree at least two, with arbitrary positive plinth
multiplicity and nonconstant residue parameter P(x,0). It proves the
base kernel, exact plinth and primitivity, and supplies a full polynomial
inverse. The base construction is an application of established
Freudenburg local-slice theory, not a newly invented construction.

The same report proves a sharp obstruction: canonical kernel-fixing
local-slice rescaling extends across the plinth exactly when the multiplier
is 1 modulo the full plinth, under a radical-congruence premise. Formal
agreement to every finite order alone cannot recognize the global map.
A separate plane-curve argument restricts hypothetical disconnected
rank-three plinths to multibranch singular fibers of one noncoordinate
polynomial. Explicit nodal controls prevent treating that restriction
as an exclusion or an actual LND realization.

The preceding [coordinate-lift and affine-replacement report](deep-pass-17.md)
gives a source-dependent working proof for every nonzero LND D of
C^[3]: an invariant extension AD+B*partial_t has a slice exactly when
A*plinth(D)+B*ker(D) is the unit ideal, and hence exactly when it has
a slice affine in t. The proof closes the previous pointwise fiber gap
using Kaliman's homology diagram and a whole-fiber normalization
argument. It does not assume the Freeness Conjecture.

A finite-jet construction then gives explicit polynomial coordinates
and a polynomial inverse for every slice extension of the entire
Dasgupta--Gaifullin Theorem 5.7 local-slice family. This includes
arbitrary m>=2, n>=1 and nonhomogeneous polynomial parameters, not
only the canonical quadratic example. A relative Danielewski
obstruction shows that those coordinates cannot always preserve
the original common invariant subring. That obstruction is not a
cancellation counterexample.

For the canonical subfamily, all higher image ideals are reconstructed
uniformly in n, with exact global witnesses in every derivation degree.
The n=1 adapted basis is already Freudenburg's published result.
Priority for the uniform extension, the coordinate application, and
the pointwise deduction is not established.

The main remaining requirements are polynomial-kernel recognition for
invariant extensions outside the treated family, and a reduction of an
arbitrary slice derivation to an appropriate polynomial frame. Neither
is supplied by an affine-slice criterion alone.

A [bounded continuation](research/arbitrary-invariant-kernel-pass18.md)
now writes every invariant affine-slice kernel as the precise principal
modification R[r/V], with Dr=p and (p,V)=1, and proves the converse.
Its two local charts do not by themselves give polynomial coordinates.
The [plinth-unit deduction](research/plinth-units-pass18.md) closes the
additional connected squarefree primitive-plinth case by the earlier
matrix lift. Repeated components outside the explicit polynomial-curve
family and disconnected support remain unresolved.
A [second geometric audit](research/pointwise-plinth-second-audit-pass17.md)
also records a quasi-affine countercontrol showing why the pointwise
argument needs the original global topology.

The preceding [invariant-slice report](deep-pass-16.md) proved the
triangular case, whole-component exclusion, and the principal-higher-image
conditional reduction. Its rank-at-most-two consequence used a published
freeness input. The new pointwise proof removes that conditional
restriction from affine replacement, not from the general Freeness
Conjecture. Its localized cubic-slice and nodal countercontrols remain
valid outside the polynomial-threefold quotient hypotheses.

The preceding [nonlinear-coordinate report](deep-pass-15.md) proves an
explicit polynomial matrix-lift theorem. For a local slice Dr=g and
invariant coefficients A,B with B congruent to 1 modulo g, the
extension AD+B*partial_t has a slice exactly when (A,B) is the unit
ideal in ker(D). The positive case has explicit invariant coordinates
and a polynomial inverse. This includes a two-invariant Cohn-type row
which elementary row operations cannot reduce over its coefficient
subring. A separate one-parameter algorithm gives complete normal forms
in every degree, including nonslice cases.

The same report proves that a slice extension and its induced quotient
action have canonically isomorphic fixed schemes and equal plinth
radicals. Thus a rank-three base forces that particular induced action
to be nonfree. Neither result reduces an arbitrary slice to the
classified coefficient families.

The preceding [global-bridge report](deep-pass-14.md) proves a uniform
obstruction to searching only affine-linear coordinate planes. Even an
explicit polynomial-coordinate translation can have no nonconstant
invariant in any such plane. The proof covers all complex plane
parameters, not a finite grid. It does not obstruct nonlinear planes
or refute cancellation. The actual plane-recognition criterion is
identified with published quasi-extension and intersection theorems.
A nonconstant-gcd commuting plane-row subcase also closes without a
height bound. The primitive row and global nonlinear-coordinate
construction remain unresolved.

The preceding [mixed-commutator report](deep-pass-13.md) gives a complete
working proof that a slice LND on a complex polynomial four-ring has
polynomial kernel if three coordinate partials satisfy
\(\operatorname{ad}_E^2(T_i)=0\) and the fourth satisfies
\(\operatorname{ad}_E^3(T_4)=0\). Its final power-law cases close
by rational Burgers classification, a positive-weight fixed-locus
contradiction, and invariant denominator clearing to a polynomial
plane LND. The original coordinate conditions are substantive.

The preceding [double-commutator report](deep-pass-12.md) proves the
stronger nonslice coordinate conclusion under its stronger hypotheses:
an LND \(E\) with
\([E,[E,\partial_{x_i}]]=0\) for every coordinate partial fixes an
ambient polynomial coordinate. If its kernel is regular, in particular
if \(E\) has a slice, the kernel is \(\mathbb C^{[3]}\).
The residual rank-two case closes by an exact rank-preserving
homogenization and a published quasi-translation theorem.

Together these close every coordinate frame of slice-filtration height
at most nine. A hypothetical nonpolynomial factor must have minimum
height at least ten. The preceding [full argument](research/height-eight-algebra-pass.md)
and [independent reconstruction](research/pass12-full-proof-audit.md)
cover the original all-double branches. No universal height bound or decreasing coordinate
operation has been proved. The mixed pattern \((1,1,1,2)\) is now
closed by the [rational-rescale proof](research/height-nine-rational-rescale-pass.md);
arbitrary higher patterns remain outside this result.

There are **802 passing exact test methods across 77 suites**,
recorded in [the current verification log](verification-pass-36.json).
These are finite algebraic controls, not formal verification of the
general source theorems. Separate model reconstructions are not
human peer review. Novelty is not established, and **the unrestricted
cancellation conjecture is not solved**.

For the latest proofs, read the [pass-36 report](deep-pass-36.md),
[all-exponent action obstruction](research/nodal-second-exponent-pass36.md),
[exact q1 integrability](research/q1-integrability-pass36.md),
[intrinsic gate](research/intrinsic-transfer-pass36.md),
[primary comparison](research/literature-scope-pass36.md), and
[independent audit record](research/proof-audits-pass36.md).
The [current regression command](research/run_regression_pass36.py)
and [packet checker](research/consistency_checks_pass36.py) reproduce
execution and artifact-integrity checks separately.

For the preceding proofs, read the [pass-34 report](deep-pass-34.md),
[geometric generic class groups](research/intrinsic-rank-pass34.md),
[integer ramification restrictions](research/integral-ramification-pass34.md),
[conditional nodal isolation](research/odd-realization-pass34.md),
[degree-preserving repair](research/plinth-repair-pass34.md),
[primary comparison](research/literature-scope-pass34.md), and
[independent audit record](research/proof-audits-pass34.md).
The [preceding regression command](research/run_regression_pass34.py)
and [packet checker](research/consistency_checks_pass34.py) reproduce
execution and artifact-integrity checks separately.

For the preceding proofs, read the [pass-33 report](deep-pass-33.md),
[arbitrary-plinth minimum family](research/minimum-top-structure-pass33.md),
[all-speed ambient obstruction](research/all-speed-ambient-obstruction-pass33.md),
[forced singular first stage](research/nodal-plinth-realization-pass33.md),
[cross-frame saturation](research/cross-frame-saturation-pass33.md),
[bounded primary comparison](research/literature-scope-pass33.md),
and [independent audit record](research/proof-audits-pass33.md).
The [preceding regression command](research/run_regression_pass33.py)
and [packet checker](research/consistency_checks_pass33.py) reproduce
execution and artifact-integrity checks separately.

For the preceding proofs, read the [pass-32 report](deep-pass-32.md),
[unrestricted-minimum counterexample](research/unrestricted-minimum-pass32.md),
[conditional ambient residue theorem](research/ambient-residue-obstruction-pass32.md),
[four residual divergence classes](research/divergence-torsion-pass32.md),
[cross-frame invariant certificate](research/stable-polynomial-invariants-pass32.md),
and [independent audit record](research/proof-audits-pass32.md).
The [preceding regression command](research/run_regression_pass32.py)
and [packet checker](research/consistency_checks_pass32.py) reproduce
execution and artifact-integrity checks separately.

For the preceding proofs, read the [pass-31 report](deep-pass-31.md),
[exact minimum and triangular classification](research/minimal-horizontal-pass31.md),
[contractible symmetry control](research/contractible-symmetry-pass31.md),
[conditional hypersurface lifting](research/hypersurface-lifting-pass31.md),
[all-thickening criterion and degree certificate](research/finite-thickening-algebraization-pass31.md),
and [independent audit record](research/proof-audits-pass31.md).
The [preceding regression command](research/run_regression_pass31.py)
and [packet checker](research/consistency_checks_pass31.py) reproduce
execution and artifact-integrity checks separately.

The preceding [pass-30 report](deep-pass-30.md) contains the
[prescribed-frame obstruction](research/finite-closure-frame-obstruction-pass30.md),
[horizontal gauge obstruction](research/horizontal-gauge-pass30.md),
[noncontractible symmetry control](research/intrinsic-symmetry-pass30.md),
and [full surface symmetry classification](research/all-noninvariant-surface-pass30.md).

For the preceding proofs, read the [pass-29 report](deep-pass-29.md),
[finite closure without solvability](research/levi-bridge-pass29.md),
[positive certificate format](research/finite-lie-certificates-pass29.md),
[horizontal selection](research/horizontal-selection-pass29.md),
[global invariant-embedding obstruction](research/global-invariant-embedding-pass29.md),
[abstract branch criterion](research/invariant-branch-obstruction-pass29.md),
and [independent audit record](research/proof-audits-pass29.md).
The [preceding regression command](research/run_regression_pass29.py)
and [preceding packet checker](research/consistency_checks_pass29.py) reproduce
execution and artifact-integrity checks separately.

For the preceding proofs, read the [pass-28 report](deep-pass-28.md),
[finite algebraic symmetry](research/finite-lie-recognition-pass28.md),
[translation-frame criterion](research/translation-frame-pass28.md),
[canonical nonunit top control](research/canonical-top-pass28.md),
[actual invariant fibers](research/changed-fiber-surface-pass28.md),
and [independent audit record](research/proof-audits-pass28.md).
The [preceding regression command](research/run_regression_pass28.py)
and [preceding packet checker](research/consistency_checks_pass28.py) reproduce
execution and artifact-integrity checks separately.

For the preceding proofs, read the [pass-27 report](deep-pass-27.md),
[intrinsic plinth and boundary fields](research/intrinsic-plinth-boundary-pass27.md),
[relative free-action completion](research/relative-completion-pass27.md),
[primitive highest-adjoint control](research/primitive-top-slice-pass27.md),
[actual nonplanar surface fiber](research/noninvariant-surface-pass27.md),
and [independent audit record](research/proof-audits-pass27.md).
The [preceding regression command](research/run_regression_pass27.py)
and [preceding packet checker](research/consistency_checks_pass27.py) reproduce
the execution and artifact-integrity checks separately.

For the preceding proofs, read the [pass-26 report](deep-pass-26.md),
[simultaneous-coordinate criterion](research/simultaneous-frame-pass26.md),
[moving-plane and Lie controls](research/moving-plane-lie-pass26.md),
[rank boundary and intrinsic centralizer](research/fence-centralizer-sector-pass26.md),
[actual surface realization proof](research/actual-surface-realization-pass26.md),
and [independent audit record](research/proof-audits-pass26.md).
The [preceding regression command](research/run_regression_pass26.py)
and [preceding packet checker](research/consistency_checks_pass26.py) reproduce
the execution and artifact-integrity checks separately.

For the preceding proofs, read the [pass-25 report](deep-pass-25.md),
[coordinate-pair and orbit-line criteria](research/commuting-leading-pass25.md),
[full invariant-plane normalizer gate](research/coupled-homotopy-pass25.md),
[non-fence plane rigidity](research/nonfence-plane-rigidity-pass25.md),
[actual surface lifting obstruction](research/ambient-lifting-pass25.md),
and [independent audit record](research/proof-audits-pass25.md).
The [preceding regression command](research/run_regression_pass25.py)
and [preceding packet checker](research/consistency_checks_pass25.py) reproduce
the execution and artifact-integrity checks separately.

For the preceding proofs, read the [pass-24 report](deep-pass-24.md),
[complementary coefficient criterion and obstruction](research/odd-coefficient-gauge-pass24.md),
[horizontal-action projection analysis](research/horizontal-lnd-pass24.md),
[intrinsic tangent-frame controls](research/intrinsic-frame-repair-pass24.md),
[surface invariant-lifting analysis](research/nodal-hypersurface-pass24.md),
and [independent audit record](research/proof-audits-pass24.md).
The [preceding regression command](research/run_regression_pass24.py)
and [packet checker](research/consistency_checks_pass24.py) reproduce
the execution and artifact-integrity checks separately.

For the preceding proofs, read the [pass-23 report](deep-pass-23.md),
[polynomial-coefficient classification](research/polynomial-local-slice-coefficients-pass23.md),
[four surface generators](research/nodal-elimination-pass23.md),
[general presentation homotopy](research/presentation-homotopy-pass23.md),
[leading-action restriction gate](research/leading-derivation-pass23.md),
and [independent audit record](research/proof-audits-pass23.md).
The preceding [primary-statement comparison](research/priority-comparison-pass23.md)
retains inherited credit and unresolved priority. An explicit control
has a physical affine slice but fixed points in the raw auxiliary ring,
so properness cannot be silently transferred between presentations.

For the preceding proofs, read the [pass-22 report](deep-pass-22.md),
[all-q classification](research/radical-noninvariant-pass22.md),
[full-center obstruction](research/center-recognition-pass22.md),
[nonlinear-frame controls](research/nonlinear-frame-pass22.md),
[five surface generators](research/nodal-generators-pass22.md),
and [independent audit record](research/proof-audits-pass22.md).
The [pass-22 regression command](research/run_regression_pass22.py)
reproduces that historical thirty-six-suite checkpoint.
Its [priority comparison](research/priority-comparison-pass22.md)
retains the unresolved 2009 example comparison and definite inherited credit.

For the preceding proofs, read the [pass-21 report](deep-pass-21.md),
[primitive noninvariant theorem](research/primitive-noninvariant-bridge-pass21.md),
[finite-center lemma and failed lift](research/universal-bridge-pass21.md),
[arbitrary slice-frame gap](research/arbitrary-slice-frame-pass21.md),
[global conductor tests](research/nodal-embedding-pass21.md),
and [independent reconstruction record](research/proof-audits-pass21.md).
The [single regression command](research/run_regression_pass21.py)
reproduces all 34 recorded suites.
The [packet checker](research/consistency_checks_pass21.py) separately
verifies claim numbering, recorded method counts, links and file hashes.
The [2009 family comparison](research/priority-comparison-pass21.md)
records an unresolved full-text priority check, not a novelty finding.
For the preceding proofs, read the [pass-20 report](deep-pass-20.md),
[nonunit coordinates and inverse](research/nonunit-local-slice-pass20.md),
[exact unchanged-inverse obstruction](research/nonunit-inverse-obstruction-pass20.md),
[actual conductor surface](research/nodal-conductor-pass20.md),
and [independent reconstruction record](research/proof-audits-pass20.md).
The [CRT audit](research/crt-audit-pass20.md) checks the stronger
coefficient premise and distinct-divisor boundary.
For the preceding proofs, read the [pass-19 report](deep-pass-19.md),
[relative classification](research/relative-modification-classification-pass19.md),
[iterated coordinates and inverse](research/iterated-local-slice-bridge-pass19.md),
and [independent reconstruction record](research/proof-audits-pass19.md).
For the preceding proofs, read the [polynomial-curve report](deep-pass-18.md),
[arbitrary-monic coordinate construction](research/polynomial-curve-lift-pass18.md),
[finite rescaling obstruction](research/rescaling-obstruction-audit-pass18.md),
and [disconnected-support reduction](research/disconnected-plinth-pass18.md).
The [literature audit](research/polynomial-curve-literature-pass18.md)
separates existing construction machinery from the explicit deduction.
For the preceding proofs, read the [coordinate-lift report](deep-pass-17.md),
[full-family polynomial inverse](research/general-local-slice-lift-pass17.md),
and [all-rank affine-replacement argument](research/general-invariant-affine-pass17.md).
The [pointwise geometric proof](research/pointwise-plinth-pass17.md) and its
[separate audit](research/pointwise-plinth-audit-pass17.md) state the
source-dependent topological input. The
[relative obstruction](research/danielewski-relative-pass17.md) explains
why preserving both original invariants is too strong.

For the preceding proof, read the [invariant-slice report](deep-pass-16.md)
and [triangular reconstruction](research/invariant-affine-controls-pass16.md).
The [whole-component proof](research/whole-plinth-component-pass16.md)
and [rank-two source boundary](research/rank-two-image-ideals-pass16.md)
record the stronger conditional and published-input consequences.
Run its 22-method standalone suite with
`/opt/anaconda3/bin/python research/invariant_slice_checks.py`.

For the preceding construction, read the [matrix-lift proof](deep-pass-15.md)
and [separate reconstruction](research/extension-mixing-pass15.md).
The [exact certificate solver](research/invariant_mixing_solver.py)
and [independent verifier](research/invariant_mixing_verifier.py)
implement the one-parameter normal forms. Run its twenty-three-method
suite with `/opt/anaconda3/bin/python research/invariant_mixing_verifier.py --self-test`.
It includes all 728 small nonzero coefficient pairs, not 728 separate
general proofs. The certificate checker explicitly retains the
derivation and local-slice hypotheses as external obligations.

For the preceding obstruction, read the [full linear-plane proof](research/linear-plane-obstruction-pass.md)
and its [independent reconstruction](research/linear-plane-obstruction-audit.md).
Run its standalone controls with
`/opt/anaconda3/bin/python research/projective_plane_checks.py`.
The [coordinate-partial audit](research/commuting-coordinate-partial-pass.md)
also records why affine-slice and constant-coefficient shear reductions
cannot be assumed, even for examples with polynomial kernels.

The preceding [structural report](deep-pass-11.md) also applies to an
arbitrary complex threefold factor \(K\) with \(K[s]\cong\mathbb C^{[4]}\).
Every nonzero intrinsic additive action has an affine-plane quotient,
surjective and faithfully flat, by an application of Kaliman--Saveliev.
A single fixed-point-free intrinsic action would settle cancellation,
but existence of one is not proved. Explicit controls exclude inferring
a quotient section or a free action by primitive normalization.

The preceding [two-power coordinate report](deep-pass-10.md) gives a
complete working proof of stable-coordinate descent for
\(F=A(x,y)u^n+B(x,y)z^q+C(x,y)\), with \(A,B\ne0\), positive
exponents, and no degree bound. When both exponents are
at least two, stability holds exactly when base coordinates \(a,b\)
give \(C=b,A=r(a),B=p(a)\). The final inverse is triangular.
The all-linear boundary is the already published KVZ Theorem 3.24,
not a new result of this investigation.

The auxiliary general-fiber result strengthens the binomial surface
argument: a general smooth rationally acyclic fiber of
\(f(x,y)z^q+g(x,y)\) already forces coordinatehood. It also completes
coordinatehood for three-variable polynomials of degree at most three
with such general fibers. These are deductions from published
topological and rectification results with explicit intervening proofs.

That checkpoint had **225 passing exact test methods across seventeen suites**,
recorded in [its verification log](verification-pass-10.json). The
checks cover finite algebra and examples, not the general topology.
Separate model audits found no theorem-level gap in the stated family
arguments; they are not human peer review or proof-assistant verification.
Novelty is not established.

**The unrestricted cancellation conjecture is not solved.** No
arbitrary slice has been reduced to these families. Reduced leading
forms now eliminate torsion in the relevant surface branch, but
algebraic recognition remains a separate step. The
[FISI source audit](research/fisi-coordinate-gap-audit.md) records a
historical question rather than treating topological triviality as
polynomial coordinatehood.

The preceding [arrangement and separated-sum report](deep-pass-09.md)
extends the original-slice theorem to
\(F=(\prod_i\ell_i^{m_i})u+H(x,y,z)\), where the distinct lines
\(\ell_i\) in the \(x,y\) plane are concurrent and all \(m_i\ge1\).
There is no degree bound on \(H\). It also proves stable-coordinate
descent for \(h(s)+f(x,y)z^q+g(x,y)\), with \(\deg h\ge2\),
\(f\ne0\), and \(q\ge1\), by combining published global-join and
surface-rectification theorems.

The pure-power branch \(xu^n+G\) remains incomplete. Stability forces
\(G(0,y,z)\) to be a plane coordinate and rectifies the cyclic quotient,
but not the cover. Explicit quartic counterexamples rule out replacing
that missing step by smoothness or an assumed residual-coordinate
condition. The report includes the proofs, exact scope, and source links.

The [torsion constraint](research/all-fiber-torsion-constraint.md)
also restricts the remaining finite homology groups across the pure
branch's fibers. It does not establish their vanishing. A published
quartic disproves assuming general-fiber torsion-freeness without
additional hypotheses.

That checkpoint had **208 passing exact tests across sixteen suites**.
They check algebraic identities and examples, not the general topology.
Separate model audits are not human peer review, formal verification,
or established novelty. No reduction of an arbitrary slice to these
families has been proved, and the unrestricted goal remains unresolved.

The preceding [monomial-coefficient slice proof](deep-pass-08.md) gives a
complete working argument for every original LND slice
\(F=x^r y^s u+H(x,y,z)\), with \(r,s\ge1\) and arbitrary \(H\):
the slice is a coordinate and its kernel is a polynomial ring in three
variables. This settles the repeated-crossing presentation, not every
possible slice.

The key distinction is that an original slice identifies its kernel
with any fiber. The constant-axis fibers are affine three-spaces by
the already published Kaliman–Vénéreau–Zaidenberg residual-plane theorem.
The proof credits that prior result and does not claim to resolve the
first Vénéreau polynomial's harder embedding question from stability.
There are explicit inverses in the nonconstant-axis branch, independent
reconstructions, and 175 exact tests across thirteen suites at that checkpoint.
None of this is human peer review, formal verification, or established novelty.

The new [integral obstruction](research/repeated-crossing-pass.md) also
excludes \(x^r y^s u+y+xz^q\), \(r\ge1,\ s,q\ge2\): all fibers
are smooth with Euler characteristic one, yet nonzero fibers have
ordinary third cohomology \(\mathbb Z/q\). Rational tests miss this.
The [support obstruction](research/repeated-crossing-slice-independent-audit.md)
excludes coefficients with reduced supports \(xyz=0\) or \(z(xy-1)=0\).

The preceding [cubic descent proof](deep-pass-07.md) gives a complete working
argument that **every stable coordinate of degree at most three in four
complex variables is a coordinate**. Consequently an LND slice of that
degree has a polynomial three-variable kernel.

The missing bridge is now supplied: a stable cubic has a singular point
at infinity where its quadratic homogeneous part vanishes. That makes
it linear in one variable with a quadratic coefficient. The
[exhaustive coefficient theorem](research/quadratic-coefficient-theorem.md)
then covers every matrix rank, including the crossing and cone cases.
The proof uses primary-source Euler/Milnor formulas, written topology,
and explicit coordinate inverses. It is not formally verified, human
peer reviewed, or established as new.

**The unrestricted cancellation conjecture is still not solved.** No
theorem here reduces an arbitrary slice to degree three. The
[post-proof audit](research/cubic-postproof-literature.md) records
the current attribution and search limits.

The preceding [slice-polynomial continuation](deep-pass-06.md) gives complete
working slice-to-coordinate arguments for two further families:

- \(p(x)y+g(x,z,w)\), with arbitrary degrees and root multiplicities.
- \(v^T(A_0+xA_1)v+b(x)^Tv+c(x)\), for every symmetric three-by-three
  affine pencil, including rank-deficient matrices.

The first family's coordinate criterion is already Maubach's theorem.
The new notes explicitly attribute that overlap, reconstruct the stability
necessity through compactly supported cohomology, and give explicit inverse
formulas in the single-root and full-rank constant-determinant cases.
No novelty is claimed. The [rank-two action note](research/rank-two-action-pass.md)
reconstructs a known conditional global result of Derksen, van den Essen
and Maubach. The [saturation audit](research/saturated-rank-two-pass.md)
shows exactly why a whole-fiber degeneration can persist after saturation.
None of these results proves that an
arbitrary slice falls into the classified cases.

The [cubic literature audit](research/cubic-literature-pass.md) separates
published special cases from the still-uncovered normal forms. A
[stronger negative control](research/nonaffine-quadratic-control.md) has
smooth fibers and Euler characteristic one in every fiber, but nonzero
middle cohomology excludes stabilization to affine space. Euler
characteristic alone is therefore not an adequate completion test.

Another complete family result is a **working classification for every polynomial
coefficient** in a fixed rank-three vertical-extension family:

```text
Delta + a(x,y,z)*d/dw has a slice
    if and only if a = c + Delta(H), with c != 0 and H polynomial.
```

The higher-denominator proof is written in full and has survived two separate
model audits. All positive cases have explicit polynomial kernel coordinates.
The same condition also characterizes properness of the action in this family.
This closes the chosen coefficient investigation, not the full cancellation
conjecture. It has no human expert review or established originality.

Start with [the all-coefficient theorem](deep-pass-04.md) and its
[complete proof appendix](research/arbitrary-coefficients-pass.md).
The preceding [global continuation](deep-pass-05.md) proves the nonrigidity
restriction on possible counterexamples, exhibits exact failures of leading-term
and commutator shortcuts, and excludes a smooth infinite family of potential
slice polynomials by their fiber Euler characteristics. These are not a proof
of the full conjecture. The [fresh full-chain audit](research/full-chain-audit.md)
reconstructs the preceding restricted proof and records its remaining review limits.
The [global bridge audit](research/global-bridge-pass.md) states precisely why
the result cannot be extrapolated to arbitrary slice derivations on affine
four-space. [Additional exact checks](verify_nonlinear.py) include polynomial
inverse maps and controls disproving an overgeneralized gauge criterion.

The full conjecture is **not solved here**. The material contains a literature
map, a proof of the standard slice reduction, elementary positive subcases,
explicit inverse maps, and counterexamples to misleading proof shortcuts.
No mathematical novelty is claimed. The coordinate-preserving case already
follows from a theorem of Bhatwadekar, Gupta, and Lokhande.

The first deeper follow-up adds two complete slice classifications for extensions
of Freudenburg's nonlinear rank-three derivation. One rules out every
nonconstant coefficient in `k[x,f]`; the other characterizes the successful
coefficients in `k[f,g]` as `c+fgP`, with `c != 0`. The negative proof is an
all-degree orbit obstruction, not a bounded-search inference. These results
are **proved in the working note, originality unestablished**, and do not
solve cancellation.

The preceding pass extended this to **every coefficient in `k[x,f,g]`**. A slice
exists exactly when the coefficient is a nonzero constant plus an actual
polynomial `Delta`-derivative. Every positive case has explicit polynomial
coordinates. The proof also gives a finite primitive classifier and a
first-pole criterion covering an additional specified family outside that
algebra. These remain private working results with originality unestablished.

- [Full coefficient-family theorem](deep-pass-03.md): complete proof,
  assumptions, examples, sources, and the exact next unresolved question.
- [Finite exact classifier](research/primitive_classifier.py): primitive,
  canonical-decomposition, and family-specific slice commands.
- [Additional independent identities](verify_first_pole.py): 16 checks using
  the standard-library arithmetic of the independent extension checker.
- [Detailed normal forms](research/extension-normal-forms.md) and
  [modified-Derksen investigation](research/modified-derksen-pass.md).
- [Post-proof literature audit](research/extension-literature.md): exact
  theorem comparisons, primary sources, access limits, and unresolved scope.

- [Deep follow-up](deep-pass-02.md): complete family proofs, other research
  routes, references, and the remaining gap.
- [Independent extension checker](verify_extension.py): 16 passing checks,
  standard library only, with no solver or SymPy imports.
- [Research ledger](research-ledger.md): evidence and abandoned calculations.
- [Experiment manifest](experiment-manifest.json): exact bounded-search scope.

- [Research note](research-note.md): assumptions, proofs, references, and the
  exact unresolved step.
- [Exact checks](verify_exact.py): symbolic identities and negative controls.
- [Claim registry](claims.json): separates known theorems, elementary
  reconstructions, and the open target.

Run the companion in the available local environment:

```sh
cd '/Users/thomasou/Documents/ChatGPT/Long term/zariski-cancellation'
/opt/anaconda3/bin/python verify_exact.py
python3 verify_extension.py
python3 verify_first_pole.py
python3 verify_nonlinear.py
python3 verify_higher_poles.py
python3 verify_outside_coefficients.py
/opt/anaconda3/bin/python research/primitive_classifier.py --self-test
/opt/anaconda3/bin/python research/full_coefficient_classifier.py --self-test
/opt/anaconda3/bin/python verify_global_filtration.py
/opt/anaconda3/bin/python verify_linear_variable.py
/opt/anaconda3/bin/python verify_quadratic_pencils.py
/opt/anaconda3/bin/python verify_quadratic_coefficients.py
/opt/anaconda3/bin/python verify_repeated_crossing.py
/opt/anaconda3/bin/python verify_central_arrangements.py
/opt/anaconda3/bin/python verify_quadratic_obstructions.py
python3 verify_torsion_monodromy.py
/opt/anaconda3/bin/python verify_two_power_slices.py
/opt/anaconda3/bin/python verify_intrinsic_quotients.py
/opt/anaconda3/bin/python research/frame_height_checks.py
/opt/anaconda3/bin/python research/height_eight_algebra_checks.py
/opt/anaconda3/bin/python research/mixed_height_checks.py
/opt/anaconda3/bin/python research/projective_plane_checks.py
/opt/anaconda3/bin/python research/invariant_mixing_verifier.py --self-test
/opt/anaconda3/bin/python research/invariant_slice_checks.py
/opt/anaconda3/bin/python research/rank_three_image_checks_pass17.py
/opt/anaconda3/bin/python research/nonreduced_jet_checks.py
/opt/anaconda3/bin/python research/general_jet_lift_checks.py
/opt/anaconda3/bin/python research/polynomial_fiber_checks_pass18.py
/opt/anaconda3/bin/python research/rescaling_curve_controls_pass18.py
/opt/anaconda3/bin/python research/global_bridge_checks_pass19.py
/opt/anaconda3/bin/python research/iterated_local_slice_checks_pass19.py
/opt/anaconda3/bin/python research/multiplier_surface_controls_pass20.py
/opt/anaconda3/bin/python research/nonunit_local_slice_checks_pass20.py
/opt/anaconda3/bin/python research/primitive_bridge_checks_pass21.py
/opt/anaconda3/bin/python research/radical_nonlinear_checks_pass22.py
/opt/anaconda3/bin/python research/nodal_generators_checks_pass22.py
/opt/anaconda3/bin/python research/polynomial_coefficient_checks_pass23.py
/opt/anaconda3/bin/python research/nodal_elimination_checks_pass23.py
/opt/anaconda3/bin/python research/reduction_controls_pass24.py
/opt/anaconda3/bin/python research/nodal_hypersurface_checks_pass24.py
/opt/anaconda3/bin/python research/commuting_leading_controls_pass25.py
/opt/anaconda3/bin/python research/coupled_homotopy_checks_pass25.py
/opt/anaconda3/bin/python research/ambient_lifting_checks_pass25.py
/opt/anaconda3/bin/python research/simultaneous_frame_checks_pass26.py
/opt/anaconda3/bin/python research/moving_plane_lie_checks_pass26.py
/opt/anaconda3/bin/python research/actual_surface_checks_pass26.py
/opt/anaconda3/bin/python research/relative_completion_checks_pass27.py
/opt/anaconda3/bin/python research/primitive_top_checks_pass27.py
/opt/anaconda3/bin/python research/noninvariant_surface_checks_pass27.py
/opt/anaconda3/bin/python research/translation_frame_checks_pass28.py
/opt/anaconda3/bin/python research/canonical_top_checks_pass28.py
/opt/anaconda3/bin/python research/changed_fiber_surface_checks_pass28.py
/opt/anaconda3/bin/python research/finite_lie_certificate_checks_pass29.py
/opt/anaconda3/bin/python research/horizontal_selection_checks_pass29.py
/opt/anaconda3/bin/python research/global_invariant_embedding_checks_pass29.py
/opt/anaconda3/bin/python research/finite_closure_frame_checks_pass30.py
/opt/anaconda3/bin/python research/horizontal_gauge_checks_pass30.py
/opt/anaconda3/bin/python research/all_noninvariant_surface_checks_pass30.py
/opt/anaconda3/bin/python research/minimal_horizontal_checks_pass31.py
/opt/anaconda3/bin/python research/hypersurface_lifting_checks_pass31.py
/opt/anaconda3/bin/python research/finite_thickening_checks_pass31.py
/opt/anaconda3/bin/python research/unrestricted_minimum_checks_pass32.py
/opt/anaconda3/bin/python research/ambient_residue_checks_pass32.py
/opt/anaconda3/bin/python research/divergence_torsion_checks_pass32.py
/opt/anaconda3/bin/python research/stable_polynomial_invariants_checks_pass32.py
/opt/anaconda3/bin/python research/minimum_top_structure_checks_pass33.py
/opt/anaconda3/bin/python research/all_speed_ambient_checks_pass33.py
/opt/anaconda3/bin/python research/nodal_plinth_checks_pass33.py
/opt/anaconda3/bin/python research/cross_frame_saturation_checks_pass33.py
/opt/anaconda3/bin/python research/full_coefficient_classifier.py '1+2*f*r'
/opt/anaconda3/bin/python research/primitive_classifier.py --mode slice --json '1+3*G*X-2*F**3'
```

The companion uses SymPy 1.13.3 in the tested environment. It checks explicit
polynomial identities, not arbitrary varieties, the cited papers' complete
proofs, or the open conjecture. No Lean formalization is included.

Current verification: **802 passing test methods** across 77 suites,
recorded in [verification-pass-36.json](verification-pass-36.json).
The latest two suites add 13 exact separated-torsor and integrability
congruence, inverse, parity and graph-closure controls.
The preceding two suites added 12 exact nodal-exhaustion and general-q1
coordinate, coefficient-ideal, bracket-chain and boundary controls.
The preceding four suites add 20 exact geometric-generic divisor, integral
ramification, conditional-isolation and polynomial-repair controls.
The preceding four suites add 25 exact arbitrary-plinth inverse, branch-count,
all-speed action, first-center and intrinsic-saturation controls.
The preceding four suites add 29 exact unrestricted-minimum, residue,
divergence-source and cross-frame controls.
The preceding three suites add 20 exact horizontal-minimum, conditional-lifting,
divergence-correction and all-thickening/degree controls.
The preceding three suites add 24 exact two-shear, horizontal-gauge,
normalizer, full-action residue and actual velocity-module controls.
The preceding three suites add 25 finite-closure certificate, horizontal
selection and global branch/Hamiltonian controls. The certificate verifier
rejects relation objects and malformed numeric indices after independent
adversarial review; all suites were rerun after those repairs.
The preceding three suites add 29 fixed-frame, canonical nonunit-plinth,
primitive-top and actual global invariant-fiber controls.
The preceding three suites add 25 relative-completion, primitive-highest-adjoint,
finite Lie-algebra and actual nonplanar-special-fiber controls.
The preceding three suites add 27 simultaneous-coordinate, exact-height,
moving-plane, Lie-recurrence and actual surface multiplication methods.
The preceding three suites add 28 coordinate-elimination, orbit-line,
normalizer, parity, formal-branch and actual algebraic-lifting methods.
The preceding two suites add 31 complementary-coefficient, nongauge,
horizontal-projection, tangent-frame, invariant-curve and module controls.
The preceding two suites added 21 polynomial-coefficient, gauge, finite-jet,
two-divisor orbit, auxiliary-presentation, homotopy, leading-action
and four-generator surface methods.
The four pass-34 standalone commands are:

~~~sh
/opt/anaconda3/bin/python research/intrinsic_rank_checks_pass34.py
/opt/anaconda3/bin/python research/integral_ramification_checks_pass34.py
/opt/anaconda3/bin/python research/odd_realization_checks_pass34.py
/opt/anaconda3/bin/python research/plinth_repair_checks_pass34.py
~~~

Run all suites with:

~~~sh
/opt/anaconda3/bin/python research/run_regression_pass34.py
/opt/anaconda3/bin/python research/consistency_checks_pass34.py
~~~

The runner's five output-parser controls are not mathematical test methods.
The preceding two suites added 22 finite-repair inverse, sharp-degree,
orbit, nonlinear-frame and five-generator surface methods.
The preceding suite added 14 primitive noninvariant, finite-center,
nonlinear-frame and conductor methods.
The preceding two suites add 17 multiplier-pole, corrected Q/P jet,
CRT, surface-incidence and residue methods. The preceding two suites
added 16 affine-extension, global-fiber, higher-image and
iterated-coordinate methods. The prior two suites
added 18 polynomial-curve jet, rescaling valuation, Jacobian and
nodal-curve control methods. The full command list above reproduces
all suites.

Historical two-power checkpoint: 225 passing methods across seventeen suites.
That suite added 17 two-power inverse, residue, obstruction, and
surface-infinity checks. The preceding pass added 33 tests across three
suites. The cubic checkpoint had 160 tests, including 8 quadratic-coefficient,
9 linear-variable, and 17 quadratic-pencil tests.
The topological proofs are written arguments, not finite-test
certificates or proof-assistant formalizations. Earlier counts below describe
the historical progression, not the current total.

Verification on September 12, 2026: all **19 tests passed**, including
deliberately incorrect inverse maps as negative controls. The program also
rejects an unverified nonterminating derivative sequence and refuses to run
with optimized Python `-O`. The claim registry parses as JSON and the new
files pass whitespace checks. None of these checks certifies the open target.
The deeper pass also passes all 16 extension checks, for **35 tests total**.
Its positive bounded-search control recovers the slice `w` when `a=1`.
That pass added 16 identity checks and 17 classifier tests, giving
**68 passing tests total**, including a deterministic 120-monomial grid.
These checks support the written proofs; they do not formally verify an
all-degree theorem or establish originality.

The all-coefficient pass brings the total to **107 passing test methods**:
18 additional nonlinear/inverse/properness checks, 9 higher-pole checks,
3 independent moment checks, and 9 complete-classifier checks. Grouped tests
include finite monomial grids; the count is not a claim of 107 independent
proofs. The new [full classifier](research/full_coefficient_classifier.py)
uses a complete homogeneous image calculation, returns a directly verified
primitive and slice when successful, and returns `unknown` when its work
limit is exceeded. For example, `1+2*f*r` yields `H=x` and slice `w-x`.

## Provenance

At the historical global-filtration checkpoint, that continuation added
**19 exact test methods**, for **126 passing methods across its suites**.
These check explicit coordinate changes,
rank-loss examples, and invalid-repair counterexamples. The infinite-family
Euler-characteristic obstruction is a separate written proof, not a claim
that these polynomial tests calculate or formalize topology.

AI assistance supplied the literature investigation, mathematical exposition,
proposed deductions, and code. Separate model critiques are not independent
human review. Thomas and a qualified mathematical reader should reconstruct
the argument and check the cited hypotheses before relying on it externally.
Source versions and specific statements are identified in the research note.

This folder is separate from the robust-execution project. Its creation does
not change that project's claims, data, or schedule.
