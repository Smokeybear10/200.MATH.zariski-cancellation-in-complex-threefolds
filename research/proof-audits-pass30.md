# Independent proof and source audits for pass 30

This is an internal process record, separate from the mathematical report.
AI reconstructions and finite exact checks are not human expert review,
formal verification, or novelty certification. The general complex
threefold cancellation target remains unsolved.

## Two-shear finite closure

The main agent wrote the complete parameter dichotomy and a standalone
ten-method checker. The first direct run passed in 0.229 seconds.
general_affine17 independently read both complete files, reconstructed
the extraction of the four basic fields, all finite cases, and the
nonzero all-depth Hamiltonian recurrence. Its run passed ten methods
in 0.216 seconds. No correction was requested.

The main agent then directly read Arzhantsev, Gaifullin and Lopatkin,
arXiv:2408.05627, Theorem 3.1 and its complete Section 3 proof.
That existing directed-cycle criterion specializes exactly to the
finite/infinite parameter boundary. The literature paragraph was
strengthened accordingly: this is a reconstruction and application,
not a plausibly novel finite-dimensionality theorem. This literature
correction changes attribution, not a checker or a mathematical identity.

The independent final report review caught one necessary transcription
repair: its abbreviated Hamiltonian recurrence paragraph had omitted
the assumption m,n at least two before asserting that no coefficients
vanish. That assumption was already explicit in the full proof note.
It is now explicit in the report as well; the unqualified statement
would have been false on an axis. No checker was changed by this repair.

## Horizontal gauges

jet_checker17 wrote the full normalized-gauge algorithm, full inverse,
residue-normalizer obstruction and intrinsic fixed-locus formulation.
general_affine17 independently reconstructed the proof without finding
a gap. The main agent read the entire note and checker and obtained
eight passing methods in 0.201 seconds.

The first author run had one structural expanded-versus-factored
expression comparison. The expected polynomial was normalized before
the final author run, which passed eight methods in 0.409 seconds.
This was a test assertion correction, not a changed mathematical formula.
It occurred before every full pass-30 regression.

The explicit ambient-coordinate premise for lambda is retained in
the theorem, algorithm and report. Gauging a supplied horizontal alone
does not preserve the second action. No unknown slice is silently
declared an ambient coordinate.

## Intrinsic symmetry transfer

general_affine17 wrote the exact centralizer calculation and classical
Danielewski-cylinder countercontrol. jet_checker17 independently
reconstructed the torsor fiber product, transitive SL2 action and
normalizer descent. Its initial source-dependent assertion about
the entire base automorphism group was conditional on the primary
classification; the author checked that classification directly.

The main agent read the complete note, then directly read
Dubouloz-Poloni arXiv:math/0602549v2, Theorem 3.10 and its proof
on PDF pages 11-12. All generators preserve x=0 for exponent at
least two; the interchange exception is exponent one. The main
agent also directly read Moser-Jauslin-Poloni arXiv:2002.12202,
Section 2.2 on printed page 3, including the exact one-cylinder
fiber-product argument. The coordinate formulas and topology are
reconstructed in the note. No new mathematical test method is
counted for this source-and-proof branch.

The example has nonzero second homology. It is explicitly excluded
from the contractible polynomial-cylinder target. Normalization of
the chosen additive subgroup is not confused with its containment
in a transitive group.

## Complete fixed-surface symmetry classification

geometry_audit17 wrote separate complete arguments for all LNDs,
the full automorphism group, and the actual velocity module of
exact Picard order four. Six standalone exact controls passed in
the initial author run, 0.289 seconds. The main agent read the
whole note and checker and independently obtained six passing
methods in 0.288 seconds.

general_affine17 read the complete proof and reconstructed every
classification. Its audit checked both split components in the pole
argument, all rotations and the excluded branch swap, the exact
Picard order after pullback using normalization units, and the
distinction between individual fixed points and a common fixed point.
It requested no correction. It did not claim to run the surface checker.

jet_checker17 separately reconstructed the complete surface proof and
read the entire checker. It checked the normalization lift, both split
branches, all root maps, module multiplication and exact order after
pullback, and the conditional ambient-extension consequences. All six
methods passed in its independent run, 0.361 seconds. It requested
no correction and made no edits.

The main agent directly read Flenner-Zaidenberg arXiv:math/0403215,
Proposition 1.1 and Corollary 1.2 including its proof, printed
pages 3-4. The principal-ideal argument is applied on the integral
normalization. Their normal-surface classification is not applied
to the nonnormal ring R. Normalization lifting is proved directly
by extending the polynomial exponential, not by transferring a
theorem about a different cyclic-extension setup.

The missing hypersurface inference is stated explicitly. Neither
the full automorphism classification nor the nontrivial velocity
module proves that R needs four generators. An ambient LND lift
is only a conditional hypothesis, never a consequence of the
normalization lift.

## Regression and packet integrity

The initial full regression ran September 13, 2026, from 09:39:45 UTC
through 09:41:14 UTC. All 683 test methods in 58 suites passed:
the previous 659 methods plus ten frame, eight gauge and six
surface methods. A repeated full run supplies the saved JSON
log, running from 09:42:28 UTC through 09:43:57 UTC with all
683 methods in 58 suites passing again. Repeated executions and the runner's five parser controls
are not additional mathematical test methods.

The packet checker separately validates flags, claim numbering,
test counts, imports, file syntax, local links and SHA256 digests.
These checks establish record consistency, not truth of the
general theorem or of published classification inputs.
