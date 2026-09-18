# The collapsed mixed quadratic sector is excluded

Under the supplied actual quadratic-frame hypotheses and nonzero speed
normal, the remaining collapsed mixed multiplicity-(2,1) fiber cannot
occur. The new proper-ideal argument110 closes the higher-order case
left by the smooth-parameter exclusion109. Its proof is written in full
and has separate AI reconstructions. General complex-threefold
cancellation remains unsolved, and novelty is not established.

## 1. The precise scope

The working target is still the unconfirmed interpretation of Luo's
email: A[u] isomorphic to C^[4] should imply A isomorphic to C^[3].
The literal A^1 conclusion has a dimension mismatch for general r.
Nothing in this checkpoint establishes the intended field or dimension
with Luo, supplies a general coordinate reduction, or changes that target.

The current theorem starts later, with a supplied polynomial coordinate
frame whose original sliced derivation satisfies E squared x_i=0 for
three coordinates and E squared z equal to a nonzero constant. The
nonconical, relative quadratic branch gives an invariant surface and
a primitive derivation N. The local theorem concerns the collapsed
mixed fiber with nonzero speed normal. These hypotheses remain
essential; they are not known for an arbitrary cancellation input.
The [global-entry audit108](global-entry-audit-pass108.md) records this gate.

For this local sector the earlier arguments reduced the second-degree
residue image to dimension two and its residual derivative-image ideal
to a proper complete intersection. The following three proofs now
cover the relevant alternatives:

| Second-degree alternative | Result and proof |
| --- | --- |
| Full three-dimensional Artin image | Excluded by [the actual full-Artin argument107](mixed-full-artin-quartic-exclusion-pass107.md). |
| Rank-two residue image and unit residual ideal | Excluded by [the exact monic-conic argument108](mixed-unit-second-image-exclusion-pass108.md). |
| Rank-two residue image and proper residual ideal | Excluded by [the determinant-index and contraction argument110](mixed-proper-image-exclusion-pass110.md), without a smoothness assumption. |

This covers the stated collapsed mixed sector, not every quadratic
fiber or the relative cubic branch. A full recognition theorem under
the original special frame would still not prove its existence for
an arbitrary sliced action.

## 2. The new proof mechanism

The proper case has a free second-degree basis 1,G,H with H zero in
the whole fiber, a first-degree generator r=aG+bH, and a conic
constant h=B1. The exact identities are

\[
NG=\epsilon br+h,\quad NH=-\epsilon ar+B_2,\quad
P=Nr=ah+bB_2,\quad
a^2,B_2,Q\in\mathfrak m(h)+\mathfrak m(ab)+\mathfrak m^2(b^2).
\]

The coefficient restrictions come from purity of the independent
residue piece 1,G,G squared, not purity of the whole second-degree
module. The elements a,b,h are nonzero nonunits, with a and b
coprime and h and b coprime.

Represent the three constrained coefficients in that sharp ideal.
The conic becomes hA0+bA1=0. Flatness and coprimality give an actual
quartic W=A1/h=-A0/b. This works even when R/(h) is nonnormal or
nonreduced, and it does not require a shear making a divisible by h.

The five actual elements 1,G,G squared,GH,W have generic determinant
-epsilon to the fourth times b divided by 8P to the fourth. Exact
DVR bases determine the determinant valuation at every invariant
divisor. Therefore their matrix inside the free fourth-degree module
has determinant a unit times b. Its adjugate gives bF4 contained
in their span M. It does not make M a basis or identify its cokernel
with R/(b).

Set J=(h)+m(a)+m squared(b). Direct differentiation shows N(M)
contained in JA. Since c belongs to F4, bNc belongs to JA. Its
whole-fiber derivative is nonzero, so flat residue-basis contraction
gives b in J. The same contraction can be checked at a simple-fiber
point where Nc is a unit, using faithful flatness of that localization.
These are two ways to justify the same gate, not two separate results.[^flat]

Absorbing m squared(b) gives b in (h)+m(a). Modulo h, substitute
b=av with v in m into the sharp relation for a squared. Unit
absorption forces h to divide a squared, without a normality or
reducedness assumption on R/(h). But any common prime factor of
h and a would then divide b, contrary to the original coprimality.
This is the contradiction. The full nine-equation proof records every
division, derivative term and finite-matrix step.

## 3. What the singular control explains

The [singular coefficient control110](mixed-singular-coefficient-controls-pass110.md)
uses R=C[x,y] localized at (x,y), with
h=y squared-x to the fifth, a=y(x+y), b=x squared, B2=xh and Q=yh.
It satisfies the sharp coefficient restrictions and all the order
bounds obtained in109. Nevertheless a/b is integral over R/(h)
without belonging to that quotient, so the old smooth shear cannot
be inferred from the coefficients alone.

This is not an actual algebra with the prescribed mixed fiber. The
stronger actual argument requires b in J, whereas the control has
J=(y squared,x squared y,x to the fourth) and b not in J.
It therefore separates the weak coefficient constraints from the
new derivative information. It is not a counterexample to either
the local theorem or cancellation.

The accompanying three-method checker verifies the coefficient and
Artin-ideal identities, the derivative formula when a shear is supplied,
and the general divided-W determinant and unit-absorption identities.
The actual flatness, divisibility, divisor classification and contraction
are written proofs, not conclusions of a finite symbolic test.

## 4. The finalized109 results and their current role

The [smooth-B1 proof109](mixed-smooth-B1-exclusion-pass109.md) first
excluded a smooth conic constant, even when a had higher order. It
used a divided quartic with zero whole residue and a unit determinant.
It forced a,B1 into m squared, B2,Q into m cubed, and P into m to
the fourth. The [narrower smooth-a proof](mixed-smooth-quartic-determinant-exclusion-pass109.md)
and [cubic-image argument](mixed-smooth-cubic-image-pass109.md) remain
valid conditional deductions. They are superseded as active local
branches by the full proper-case exclusion110, not inputs to it.

Separately, the [strong-nilpotence obstruction109](constant-acceleration-strong-nilpotence-obstruction-pass109.md)
uses an actual polynomially invertible frame from103. Its velocity
Jacobian is nilpotent at each point, but two evaluated Jacobians have
product M with trace -4 and M squared=-4M. Thus alternating products
are nonzero at arbitrarily large length. Constant simultaneous
triangularization, and the automatic strong-nilpotence shortcut, are
unavailable. The action is already nonlinearly conjugate to translation,
so this says nothing against nonlinear recognition or cancellation.
The relevant primary criterion is de Bondt's Proposition 1.3.[^bondt]

## 5. Verification and evidence boundaries

The [saved verification110](verification-pass110-working.json) runs:

```sh
/opt/anaconda3/bin/python -m unittest -v \
  research.mixed_singular_coefficient_checks_pass110 \
  research.mixed_divisor_determinant_checks_pass109 \
  research.mixed_pure_quartic_checks_pass108 \
  research.quadratic_divisor_filtration_checks_pass107
```

All four suites and eight methods pass: three new110 methods and five
retained methods. Input hashes are unchanged. The captured execution
took 4.356164083 wall seconds; unittest reported 3.499 seconds. Its
complete-output SHA is
5693696c3e4a06b25055275461919caf41338897a4d4c1f502bfc91bc945551b.
The earlier user check-in also ran five retained checks successfully;
that status run is not additional mathematical coverage.

The historical full75 execution remains 146 suites and 1047 methods,
with 544 entries in its retained claim registry. It was not rerun.
All 673 frozen records through108 were rehashed unchanged. The
[checkpoint110](checkpoint-pass110-working.json) consolidates the five
previously uncheckpointed109 artifacts with this proof, the110 control,
checker, capture and synthesis. README and the research ledger stay live.

The exclusion has complete independent AI reconstructions, including
checks of the retained divisor and purity dependencies. These are not
human expert review, Lean formalization, or an exhaustive novelty audit.
The exact source reads support the indicated algebraic gates, not an
independent verification of every earlier research note.

## 6. Remaining proof work

The immediate local task is now a different sector, not another
order estimate inside the excluded mixed fiber. Whole-double fibers
and zero speed normal require their own degree-module and derivative
arguments. In particular the pure piece 1,G,G squared and nonzero Nc
used here cannot be silently transferred to those cases.

The relative cubic branch and global recognition also remain open.
Separately, an arbitrary sliced action has not been put into the actual
three-good coordinate frame. A concrete weaker entry target is one
actual coordinate f with E squared f=0, certified by a polynomial
inverse. Its existence is unproved and would not by itself identify
the whole kernel. A fixed ordinary-degree search cutoff is already
known to be inadequate, so bounded unsuccessful searches cannot
settle that existence question.

The bounded global literature check found no newly applicable entry
theorem. Reencountered unipotent-action and constructibility results
were not promoted to new reductions: their additional hypotheses
remain unsupplied. The full cancellation goal stays active.

## Sources

The local proof's exact dependencies are linked in its footnotes.
The newly rechecked primary statements used in this synthesis are:

[^flat]: The Stacks Project Authors, [Theorem 10.81.4, Lazard's theorem, 058G](https://stacks.math.columbia.edu/tag/058G), [Section 10.81, finite factorization and the free-colimit construction, 058C](https://stacks.math.columbia.edu/tag/058C), and [Lemma 10.39.15, faithful flatness and nonzero fibers, 00HP](https://stacks.math.columbia.edu/tag/00HP). Complete displayed statements and proofs read September 14, 2026. The one-element contraction is proved through the linked local purity note; its geometric alternative uses faithful flatness. Deeper foundations were not all reconstructed again.

[^bondt]: Michiel de Bondt, [Quadratic polynomial maps with Jacobian rank two](https://arxiv.org/html/1601.00579v4), v4, November 2, 2017, Proposition 1.3. The complete displayed criterion and proof were rechecked. The ordinary quadratic-map hypotheses elsewhere in the paper are not inferred from quadratic time dependence.
