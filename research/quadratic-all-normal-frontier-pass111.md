# The quadratic fiber frontier after removing the speed-normal hypothesis

The mixed double-plus-simple fiber is excluded throughout the supplied
actual nonconical quadratic frame, including zero speed normal. A separate
whole-double dichotomy now holds with the same generality: a hidden
quadratic parameter exists exactly when the first two derivative-image
ideals agree. The proper-image whole-double alternative remains open.

These are conditional results inside the existing frame investigation.
The unconfirmed intended question is still
A[u] isomorphic to C^[4] implies A isomorphic to C^[3]. No reduction of
an arbitrary cancellation input to this frame has been proved, and no
global polynomial recognition follows merely from the local conic.
The general target is not solved and novelty is not established.

## 1. Why the new hypothesis removal is substantive

The completed110 argument excluded the collapsed mixed profile (2,1)
only where L(m), the speed normal, was nonzero. That premise entered
through an original linear-normal equation and the resulting whole
nonreduced fiber coordinates. Applying the final algebraic contradiction
at L(m)=0 without rebuilding those inputs would have been invalid.

The [fixed-fiber lemma111](quadratic-fixed-fiber-low-degree-collapse-pass111.md)
supplies the first replacement. For any U with N cubed U=0,
p=N squared U and eta=2pU-(NU) squared are invariant. At a fixed point
both invariants vanish, so (NU) squared vanishes on the entire fiber.
Every F2 element is therefore constant on each translating simple
component. This collapses the mixed companion without L(m) nonzero.

On a collapsed fixed double, finite freeness over the actual C[c]
gives the entire factor C[c,epsilon]/epsilon squared. Local nilpotence
kills N epsilon, and the canonical unit-volume Jacobian makes Nc
generate the nilradical at every point. Hence Nc=lambda epsilon,
with lambda a nonzero constant, also without L(m) nonzero. This is
an all-point statement, not only a calculation at a generic component.

The [nilpotent-rank theorem111](quadratic-double-nilpotent-rank-pass111.md)
provides the second replacement. Two independent quadratic nilpotent
coefficients would give an actual free basis of F2. Its conic relation
forces scalar coefficients into the square of the base maximal ideal.
In a chart chosen with y equal to one of these quadratic elements,
the weight-two parts of Ny and NV force their coefficient ratio to be
constant, a contradiction. The volume factor and transverse coefficient
are allowed to vary before that calculation. The proof does not extend
the older constant-coefficient chart beyond its hypotheses.

Actual generation by A1,A2,c then forces the two good nilpotent
coefficients to be constants generating the unit ideal. A constant good
combination is an actual G in F2 that generates the double nilradical.
In the mixed case another generic constant-row choice also separates
the simple component. This yields the full algebra D[c], where
D=C[G]/G squared(G-1), with its actual N-action.

## 2. The resulting exclusions and remaining alternatives

The [all-normal transfer proof111](quadratic-all-normal-mixed-exclusion-pass111.md)
checks the old arguments at the level of their actual algebraic inputs.
Every F2 residue is Artin-valued: a nonconstant reduced double parameter
would force the entire single-double cyclic conic, while the new
nilpotent-rank lemma controls its nilpotent coefficient. The full,
unit and proper second-image branches are then excluded respectively
by107,108 and110. The original whole-ideal equation and its stability
under the original partial derivative are not needed by that chain.

| Sector in the supplied quadratic frame | Current proved conclusion | Remaining obligation |
| --- | --- | --- |
| A fixed fiber with a simple companion | Every F2 element is constant on the reduced simple component | This lemma alone does not classify the whole fiber |
| A collapsed fixed double component | Actual dual-number factor, nonzero constant Nc coefficient, at most one quadratic nilpotent direction | Other factors and global recognition are separate |
| Whole multiplicity profile (2,1), any L(m) | Excluded by the rebuilt107/108/110 chain | Not an arbitrary-frame reduction |
| Collapsed whole double with a hidden F2 parameter | Exact all-degree cyclic conic; I2=I1 | Recognize the global threefold |
| Collapsed whole double without a hidden F2 parameter | W1=C, W2=C+C G; I1=PR and I2=PJ with J proper maximal-primary and a complete intersection | Exclude or realize this actual-frame alternative |
| Arbitrary cancellation input | No general entry theorem obtained | Prove a valid frame reduction or use another recognition method |

The [original whole-double dichotomy111](whole-double-second-degree-dichotomy-pass111.md)
first proved its statement under L(m) nonzero. Section 6 of the
all-normal transfer now removes that premise by using the new
nilpotent-rank theorem. Its stronger original normal-ideal equality
is not asserted in the extension.

The whole-double proper branch cannot use the mixed argument unchanged.
G squared has zero whole residue, so 1,G,G squared is not an independent
piece for coefficient extraction. Nc remains a nonzero nilpotent, which
is enough for one-element purity but does not produce the missing sharp
coefficient ideal. The absence of a simple-point unit is not the only
difference between the two cases.

## 3. A polynomial control and its exact failed assumption

The [intrinsic coordinate control111](whole-double-good-coordinate-control-pass111.md)
uses A=C[x,y,t], f=y squared+x^e t, and
N=-x^e partial_y+2y partial_t for e at least one.
Its coordinates F=x, G=y+xt, c=t+G squared have polynomial inverse
t=c-G squared, y=G-x(c-G squared). The selected good elements y,G
have degree at most two, the specified c has degree four, and the
whole double has hidden quadratic parameter t.

This is a genuine polynomial quotient control, not an actual-frame
counterexample. At the invariant divisor x=0, both selected good
residues are y and are algebraic over C(f), whereas t survives.
That violates the selected-good whole-divisor noncollapse theorem91.
The exact all-height-one input needed by the actual investigation
therefore cannot be inferred from this example's flatness, degree
bounds or coordinate inverse alone.

## 4. Verification and source boundaries

The new written arguments received separate full-file AI reconstructions.
The important checks were the actual coefficient-field choice, the
nonzero nilpotent class making y=U a regular transverse parameter,
basis-first projection to one double factor, the variable-volume
connection terms, and the good-generator ideal on the entire c-line.
The transfer review separately traced every geometric input used
by107/108/110. No proof was accepted solely because several outputs
agreed or a finite test passed.

The [canonical capture111](verification-pass111-working.json) records
six suites and ten methods, three new and seven retained. It passed
in 1.708044708 wall seconds, 1.343 unittest seconds, with unchanged
source hashes. Its complete stdout-plus-newline-plus-stderr hash is
1e0e8e4e06739ab585e30557278ec373a136e817eb1ee0ea932e4a19d54943d7.
The exact command is:

    /opt/anaconda3/bin/python -m unittest -v \
      research.whole_double_nilrank_checks_pass111 \
      research.whole_double_coordinate_checks_pass111 \
      research.quadratic_degree_module_checks_pass102 \
      research.quadratic_divisor_filtration_checks_pass107 \
      research.mixed_pure_quartic_checks_pass108 \
      research.mixed_singular_coefficient_checks_pass110

The new controls check invariant/conic identities, variable-coefficient
weighted derivatives, coordinate inverses, degree bounds and sample
quotient restrictions. Retained controls check conic, divisor and quartic
identities. They do not prove flatness, all-point Jacobian nonvanishing,
actual coordinate availability, all-height-one noncollapse, purity or
the universal geometric exclusions. They are not Lean formalization.

The standard purity input is retained
[residue-basis107](residue-basis-purity-pass107.md), based on the
[Stacks Lazard theorem](https://stacks.math.columbia.edu/tag/058G).
The local nonzero-fiber faithful-flat criterion is
[Stacks00HP](https://stacks.math.columbia.edu/tag/00HP).
The complete selected statements and displayed proofs of these two
sources were reread for this pass. Their deeper foundations were not
all rebuilt. No new general cancellation literature result or
exhaustive novelty audit is claimed.

All 684 frozen records through110 were revalidated unchanged.
Historical full75 remains 146 suites/1047 methods and registry544;
that entire suite was not rerun. The
[checkpoint111](checkpoint-pass111-working.json) records the new
artifact versions, canonical run, proof reviews and limitations.
Human expert review and statement-level novelty clearance remain absent.

## 5. Next proof tasks and stop conditions

The next local task is the proper-image whole-double alternative.
Derive an actual replacement for the missing three-term purity, or
construct an actual original frame realizing it. A coefficient tuple,
completed formal model or a polynomial quotient that fails the
selected-good divisor hypothesis is not such a realization.
The exact target is an argument forcing a hidden U in F2, equivalently
I2=I1, or a decisive actual-frame obstruction to that target.

Do not restart the mixed (2,1) branch as though L(m)=0 remained open.
Do not transfer its sharp a squared ideal to the whole double, where
G squared has zero residue. Whole-double cyclic recognition, the
relative cubic branch and arbitrary-action frame entry remain
distinct tasks. Progress on a local sector does not complete the
original cancellation objective.

This remains private research. No message to Luo, expert contact,
submission, public posting, paid resource action, capital use or
new automation occurred.
