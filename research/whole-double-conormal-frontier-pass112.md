# Whole-double coefficient and conormal restrictions

The actual proper-image whole-double branch now has a nonzero conic
coefficient, a constant leading transverse chart along its entire reduced
line, and sharp cubic residue bounds. A separate finite preparation
argument supplies an actual hidden quadratic parameter throughout an
arbitrary-polynomial triangular class. The proper branch itself remains
open, as do arbitrary-frame entry and the full cancellation problem.

## 1. The target and the actual scope

The unconfirmed working interpretation of Luo's email remains
A[u] isomorphic to C^[4] implies A isomorphic to C^[3]. The literal
conclusion A^1 has the wrong dimension for general r. Nothing in this
pass resolves that interpretation or proves the global implication.

The retained111 work excludes the mixed multiplicity-(2,1) quadratic
sector for every speed normal within the supplied original frame. It
also proves that a collapsed whole double has a hidden quadratic
parameter exactly when its first and second derivative-image ideals
are equal. The current question is its proper-image alternative.
The exact retained hypotheses are in
[whole-double111](whole-double-second-degree-dichotomy-pass111.md) and
[all-normal111, Section 6](quadratic-all-normal-mixed-exclusion-pass111.md).

Here R is the localized regular invariant surface, F_j is the actual
kernel of N^(j+1), and the whole fiber is C[c,G]/G squared with
Nbar=lambda G partial_c, lambda a nonzero complex constant. The actual
F2-basis is 1,G,H, with H zero in that fiber. The proper residual ideal
is J2=(a,b), coprime, nonunit, and supported at the closed base point.
The scalar coefficient h is defined by NG=epsilon b(aG+bH)+h.

## 2. New deductions inside the proper branch

The [product-index proof112](whole-double-product-index-pass112.md)
uses the five actual products 1,G,H,G squared,GH in F4. Their generic
coefficient determinant is epsilon^4 b squared/(16P^4). Comparing
with every actual height-one degree basis makes their index determinant
a unit times b squared. The adjugate then gives b squared F4 in
their span. This is not a basis assertion or a cyclic-cokernel theorem.

Differentiation and purity of the one-element span of Nc contract the
index containment to b squared in (h)+a(a,b). It follows that h is
nonzero, gcd(h,a)=1, and h does not belong to m(a,b) squared. The
gcd is with a, not with b. The mixed proof's sharper a squared
coefficient extraction remains unavailable because G squared is zero
in the whole double.

The same exact divisor data yield N(F3) contained in mF2. Every
cubic element is therefore constant on the reduced c-line, and the
specified c has degree exactly four. This is stronger than the old
statement that no quadratic element parametrizes that line, but does
not rule out a cubic nilpotent residue depending on c.

The [conormal proof112](whole-double-global-conormal-chart-pass112.md)
then controls that dependence. The conormal base-image line has a
global generator F=P(c)s1+Q(c)s2. With G it gives a formal transverse
chart over the actual C[c]. The canonical stable-polynomial volume
has constant unit coefficient along the whole affine line. Comparing
the weight-two Jacobian formula with the first base jet of h proves
that the two base conormal coefficients form an affine vector w(c).
Its unimodularity supplies a constant base combination x with nonzero
transverse differential everywhere.

In this chart the other base coordinate has leading part
f=A(c)x+B G squared, with A affine and B a nonzero constant. The
leading field is N*=gamma x partial_G+lambda G partial_c, where gamma
is a complex constant, zero exactly when h belongs to m squared.
No ambient polynomial-coordinate or original-normal-ideal assertion
is made. The cubic image W3 consequently satisfies:

| Base coefficient | Whole-fiber cubic image |
| --- | --- |
| h not in m squared | W3=C span{1,G} |
| h in m squared | C span{1,G} contained in W3 contained in C span{1,G,Gc} |

The second line does not assert that Gc lifts to F3. Both lines still
allow the actual quartic c, so they are not exclusions.

## 3. A separate all-polynomial triangular theorem

The [finite preparation proof112](triangular-whole-double-preparation-pass112.md)
handles every e at least one and every Q in C[x,y] for
f=y squared+xQ+x^e z and
N=-x^e partial_y+(2y+xQ_y)partial_z on C[x,y,z]. Finite monic division
modulo x^e constructs an actual polynomial U. There is no infinite
convergence or unproved cancellation of denominators:
U=(y squared+A_e(x,f)y+B_e(x,f))/x^e belongs to the original ring,
and z=-V_e(x,f,y)U-R_e(x,f,y).

Thus A=S[y,U] has an exact monic conic presentation over S=C[x,f].
Its free S-basis is U^j,yU^j. Distinct generic degrees determine every
F_n and every derivative-image ideal: I_n=x^(e ceil(n/2))S. In
particular I1=I2=x^eS. Every member of this class has a hidden quadratic
parameter even when Q has odd terms or arbitrary large degree.

This generalizes the retained even-power Catalan calculation104 by
a finite preparation algorithm. It is not a new normal-form theorem
for arbitrary frames. Its starting algebra is already polynomial,
and its exact invariant coordinate and triangular formula are supplied.
The theorem resolves a test family, not the cancellation target.

## 4. Reproducible verification

The [capture112](verification-pass112-working.json) records the complete
command, six input hashes and full output. Run from the project root:

```sh
/opt/anaconda3/bin/python -m unittest -v \
  research.whole_double_conormal_checks_pass112 \
  research.triangular_whole_double_checks_pass112 \
  research.whole_double_nilrank_checks_pass111 \
  research.whole_double_coordinate_checks_pass111 \
  research.quadratic_degree_module_checks_pass102 \
  research.quadratic_divisor_filtration_checks_pass107
```

Canonical execution459b6b passed six suites and eight test methods,
three new and five retained. Its measured elapsed time was 3.422076459
seconds; unittest reported 3.054 seconds. The complete stdout-newline-
stderr hash is
375dcaed52886b3132ec6d00e5048a993f80d9c5ab66e4c7cd91ecb83e9aa43a.
All input hashes remained unchanged.

The two new methods in the
[conormal checker](whole_double_conormal_checks_pass112.py) verify
the product determinant and symbolic connection identities. The one
new [triangular checker](triangular_whole_double_checks_pass112.py)
tests a polynomial with odd and quartic terms for e=1 through4,
and leading derivative instances n=0 through6. It is not an exhaustive
test of all Q, all e or all n. The written proof supplies that argument.
Finite tests do not certify flatness, module purity, actual coordinate
selection, all-divisor classifications or arbitrary-frame entry.

All694 frozen records through111 were revalidated unchanged in fd5cf7.
The historical full75 verification remains146 suites/1047 methods and
the frozen claim registry544. That historical full run was not repeated.
The [checkpoint112](checkpoint-pass112-working.json) records the current
artifacts, proof reviews and exact scope. Separate AI reconstructions
are not human expert review, formal verification or novelty clearance.

## 5. Remaining proof obligations

First, eliminate the proper whole-double branch or construct an actual
frame satisfying all of its hypotheses. A compatible coefficient tuple
or a formal derivation is insufficient. The coefficient control in
product-index112 satisfies the new ideal restrictions without supplying
an algebra or the required degree modules.

Second, a formal quadratic normalization of the base equation does not
by itself construct a parameter of N-degree two: the canonical field
retains a generally variable unit multiplier. A volume-compatible
construction, or a separate proof of N cubed Uhat=0, is required first.
Even such a formal Uhat must not be mistaken for an actual element
of F2 in A. Since q squared is contained in mA
and mA is contained in q, the transverse and base-ideal completions
have the same topology here. Nevertheless, equality of the kernel of
N cubed on the completion with F2 tensor the completed base is not an
automatic consequence of flat completion: N is R-linear, not A-linear,
and A is not finite as an R-module. A descent theorem needs a proof.

Third, the independent global task remains to place an arbitrary
cancellation input into a useful actual frame and recognize A globally.
The conormal chart does not solve that task. No fixed ordinary-degree
search bound or stable coordinate construction proves the needed
unstable coordinate exists. The relative cubic branch also remains open.

## Sources

The three current proof notes cite their retained actual-frame inputs.
The newly consulted external foundations are the complete selected
statements and displayed proofs of The Stacks Project,
[Lemma31.22.12, regular immersions](https://stacks.math.columbia.edu/tag/0E9J),
[Lemma31.22.5, conormal characterization](https://stacks.math.columbia.edu/tag/063M),
and [the symmetric conormal-algebra map](https://stacks.math.columbia.edu/tag/0632).
These supply the regular-immersion and associated-graded facts, not
a cancellation or novelty result. This pass did not perform a new
general cancellation literature audit. No external contact, submission,
posting, paid access, financial action or new automation occurred.
