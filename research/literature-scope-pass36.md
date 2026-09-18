# Source audit for the separated-torsor and integrability arguments

This is a statement-level audit of the inputs used in pass 36. It is not a
completed novelty search or a claim to have settled complex threefold
cancellation. The correction of the professor's statement and the choice
of the complex field remain unconfirmed.

## The geometric quotient gates

[Stacks 06PH, Lemma 80.11.7](https://stacks.math.columbia.edu/tag/06PH)
was read with its proof. A free action of a flat, locally finitely
presented group algebraic space has an algebraic-space quotient, and the
quotient map is an fppf torsor. This applies to the additive group after
scheme-theoretic freeness is established. The initially inspected
[071R](https://stacks.math.columbia.edu/tag/071R) treats an abstract
constant group; it is not by itself the required additive-group theorem.

[Stacks 0DU0, Lemma 101.32.1](https://stacks.math.columbia.edu/tag/0DU0)
was read with its proof. An open equivalence relation on a flat, locally
finitely presented space over a base has an étale quotient over that
base. In the present application the actual quotient-plane map is
smooth of relative dimension one. The nonvanishing additive vector
field makes the action relation étale. Trivial geometric stabilizers
make it universally injective, and
[025G](https://stacks.math.columbia.edu/tag/025G), also read with proof,
makes that relation an open immersion. Neither quotient affineness nor
connectedness of every invariant-theoretic fiber is assumed.

[Stacks 04GG, Lemma 10.153.3](https://stacks.math.columbia.edu/tag/04GG)
was checked particularly at implication (1) to (8), including its
standard-étale proof. It supplies a retraction through the chosen
residue-field point of an affine étale chart over a henselian local
ring. The chart need not be finite. Composing with an étale chart of
the algebraic space gives an actual section.
[024T](https://stacks.math.columbia.edu/tag/024T) supplies the
open-diagonal proof that this section is an open immersion. It need
not be closed because the quotient need not be separated.

[Stacks 0DEV, Lemma 59.101.1](https://stacks.math.columbia.edu/tag/0DEV)
and its proof explicitly supply the quasi-coherent fppf comparison and
affine vanishing used to trivialize the additive torsor on each chart.
[00MC](https://stacks.math.columbia.edu/tag/00MC) gives faithful flatness
of noetherian local completion. The argument applies ordinary scheme
base change to the completed base ring. It does not identify a formal
completion with an algebraic total space or use an algebraization
principle.

The fork obstruction itself is the written saturated-graph computation
in [the new geometry proof](nodal-second-exponent-pass36.md). Its
application additionally uses the earlier exact invariant-residue and
node-isolation results. The primary quotient lemmas do not identify
those residue rings for us.

## The closest classical torsor comparison

Adrien Dubouloz's
[*Danielewski-Fieseler surfaces*](https://arxiv.org/pdf/math/0401225),
arXiv v3, was checked at its introduction, Proposition 2.6 and the
surrounding discussion through Proposition 2.9. The paper describes
torsors over a curve with multiple origins and gives a transition-pole
criterion for the relevant affine surfaces. This is established
background for the method, not a new use of nonseparated quotients.

The present written graph obstruction has a two-dimensional complete
base and different overlaps D(y), D(x), and D(xy). The curve-base
statement cannot simply be substituted for it. The direct calculation
with arbitrary pole orders is retained. This comparison does not
establish that the exact two-dimensional consequence is new.

## Pencils and intrinsic transfer

The planar invariant-coordinate input and primitive-kernel contraction
were audited in [pass 35](literature-scope-pass35.md). The new
[integrability proof](q1-integrability-pass36.md) supplies its own
single-correction necessity, pole contraction, first-jet calculation,
finite nilpotent inverse, Chinese remainder construction and inverse
denominator clearing. A Jacobian-one criterion is not used to infer
invertibility. No source is claimed to turn this fixed-model result
into a theorem about an unknown polynomial cylinder.

The [intrinsic transfer note](intrinsic-transfer-pass36.md) retains the
published leading-filtration input attributed in the preceding notes
to Alhajjar and Daigle. Its additional volume argument is written
explicitly. Invariant preservation is equivalent to a particular
commutator being locally nilpotent; neither property is proved
automatic. A source about semi-rigid domains alone cannot fill this
cylinder-specific gap.

## Search and access limits

Targeted searches covered separated additive torsors, nodal orbit
spaces, Danielewski trees, locally nilpotent pencils and 2026
cancellation results. Search results are discovery leads, not proof.
The abstract of Hajra and Upmanyu's
[*Generalized Zariski cancellation for Brieskorn--Pham varieties*](https://arxiv.org/abs/2606.26890)
was checked. Its specified singular-variety scope does not supply
smooth affine-space cancellation. No full-text audit of that paper is
claimed here.

A search also surfaced Tao Su's character-variety cell-decomposition
paper. The first main-agent attempt to open its BIMSA PDF returned an
internal retrieval error. The accessible
[arXiv v4](https://arxiv.org/pdf/2307.16657v4) was then checked directly
by both the general agent and main agent at Definition 1.1, Theorem
2.10's quotient construction and Remark 2.12. Its candidate cells are
a next-work lead, not a proof of nonpolynomiality or an input to the
three new proofs. Exact scope and a selected index appear in
[the separate lead note](su-candidate-lead-pass36.md). No paywall was
bypassed and no external contact was made.

An initial local search was rejected by zsh because an unmatched
bibliography glob was expanded before rg ran; a scoped rg command
without that glob was then used. No mathematical evidence depended on
the failed command. No inaccessible source, informal forum, other AI
page, or absence of a search match is counted as independent proof or
evidence of novelty.
