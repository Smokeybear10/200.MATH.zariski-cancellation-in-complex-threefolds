# Scalar classification and the remaining global cubic cases

The supplied actual cubic framework now forces a rational scalar
coefficient of one of two explicit types. A polynomial divisibility
argument eliminates the reciprocal type for a null axis. The other
three axis/type combinations remain unresolved and all admit
polynomial, unimodular speed controls. Those controls do not realize
the full original-coordinate hypotheses.

This is a conditional restriction and one case exclusion. It is not
a proof of complex-threefold cancellation. The working interpretation
of the professor's email, A[u] isomorphic to C^[4] implying A isomorphic
to C^[3], remains unconfirmed, and entry from an arbitrary cylinder
into the supplied special frame remains open.

## 1. Precise conditional result

Assume the full actual setting of
[potential90](nonconical-quadratic-potential-pass90.md) and
[cubic relation90](nonconical-cubic-relation-pass90.md): an original
polynomial four-ring B=C[x1,x2,x3,z]=A[u], E=partial_u, E squared
xi=0 for the three good coordinates, Ez=q u with q in C*, and the
intrinsic invariant plane S=C[s,t]. Its speed b belongs to S cubed,
Omega=det[b,bs,bt] is nonzero, and the actual relative generators
over K=Frac(S) generate K[v] with exact plane relation degree three.
The original generation, potential and base-only unit-volume
hypotheses are retained, not replaced by independently chosen arrays.

The [general restriction120](cubic-general-axis-frontier-pass120.md)
supplies a constant ambient axis v0 with Qv0 a nonzero constant
covector, rank Q=3 and nondegenerate plane restriction. The
[constant-basis normal forms121](cubic-axis-scalar-normal-forms-pass121.md)
then put b=(g,hY,Y) with g,hY,Y in S. The normal ratio h is
nonconstant, but the full first-integral field L may be a proper
finite extension of C(h).

Both axis calculations prove that D actually belongs to C(h) and
has one of the forms

\[
D(h)=d_3h^3+d_2h^2+d_1h+d_0\quad(d_3\ne0),
\qquad\text{or}\qquad
D(h)=d_2h^2+d_1h+d_0+\frac{c}{ah+b}\quad(ac\ne0),
\]

with all displayed constants complex. The matrix block is determined
by M11=Dhh/2, M12=(Dh-hDhh)/2 and M22=D-hDh+h squared Dhh/2.
The appropriate determinant nonvanishing condition remains imposed.
These are necessary forms, not sufficient realizability conditions.

| Selected axis | Cubic scalar | Quadratic plus reciprocal scalar |
| --- | --- | --- |
| Null | Not excluded; Y is a nonconstant polynomial cube up to a complex unit. | Excluded by polynomial Jacobian divisibility. |
| Non-null | Not excluded. | Not excluded. |

The axis need not be unique, so the table does not assert that the
rows are intrinsically disjoint under every possible axis choice.

## 2. What forces rationality

For the [null axis](cubic-null-axis-scalar-constraint-pass121.md),
the actual connection is explicit in the commuting rational h,Y
derivatives. The volume's lower coefficients force 1/l to have
zero second h-derivative, while Dhhh is a nonzero constant times
l to the fourth power. The derivative constants are C even when
L is finite over C(h). Integrating that exact third derivative
gives the two displayed forms and proves their rationality.

For the [non-null axis](cubic-nonnull-axis-scalar-constraint-pass121.md),
a finite square-root extension normalizes the conic and rescales
the coefficient derivative. No algebraic primitive of that
derivative is assumed. The lower volume coefficients yield a
second-order equation for z0=1/l and a first-order equation for e.
Returning to h transforms the former into (sqrt(D)z0)hh=0. The
latter becomes the first integral
Dhhh(ah+b) to the fourth power equal to a nonzero complex constant.
This again gives exactly the two forms.

The field-extension step uses relative algebraic closedness and
characteristic-zero separability. The primary irreducibility lemma
was checked directly.[^1] It is not a source for the scalar
classification or a published cancellation result.

## 3. The new global exclusion and its limit

For the [null reciprocal exclusion](cubic-null-axis-polynomial-speed-pass121.md),
write P=hY and Z=aP+bY. A constant linear change of polynomial
speeds gives an identity
2GYZ+A Z cubed+cY cubed+Z=0 with c nonzero. Its derivative FZ is
coprime to YZ. Differentiation therefore makes YZ divide
Jac(Y,Z). Its total degree is too small unless that Jacobian is
zero. The identity then forces all speed differentials to have
rank at most one, contradicting Omega nonzero.

For the null cubic alternative, the exact prime valuations instead
give Y=uR cubed and P=RT with u a complex unit, R nonconstant and
R,T coprime. This is not a contradiction. The same note gives
an explicit polynomial speed with Omega=3s to the fourth power
and an exact polynomial unit-row certificate.

The [global boundary note](cubic-scalar-global-boundaries-pass121.md)
provides analogous polynomial, unimodular speeds for both non-null
types. Thus none of the remaining three combinations can be
discarded using only those coefficient-level hypotheses.

The boundary note also records a rejected argument: the relative
Jacobian is a base-field unit, not automatically a complex constant.
For the canonical global Jacobian derivation N, the exact chain-rule
identity is J N(v)=1. Choosing the degree-one generator v=y1 does
not imply N(v)=1. Any argument requiring a constant volume must
first justify that normalization and transform the formulas with it.

## 4. Verification and reproducibility

The [canonical capture121](verification-pass121-working.json) records
seven passing suites and nine methods, five new and four retained.
All seven test-source hashes were unchanged across the run. The
complete captured output and its hash are included. The command is:

```sh
/opt/anaconda3/bin/python -m unittest -v \
  research.cubic_null_axis_checks_pass121 \
  research.cubic_nonnull_axis_checks_pass121 \
  research.cubic_null_polynomial_speed_checks_pass121 \
  research.cubic_scalar_speed_boundary_checks_pass121 \
  research.cubic_conic_axis_checks_pass120 \
  research.cubic_rational_transfer_checks_pass120 \
  research.nonconical_quadratic_potential_checks_pass90
```

The checks reconstruct the finite connection, tensor, potential and
volume identities; the non-null derivative conversions; the null
reciprocal absorption and differentiated identity; and the explicit
polynomial controls. They do not prove the constant-field statements,
UFD degree argument, existence of an original frame, or cancellation.
Separate full-file AI proof reconstructions found no invalidating
gap in the stated conditional results. They are not human expert
review, formal verification, or novelty clearance.

The earlier frozen record chain was revalidated through120. The
historical whole-suite counts in that integrity audit are not a
new execution of those historical tests. All files through120 remain
unchanged; only the README and research ledger remain live indexes.

## 5. Remaining proof obligations

The next work must constrain the full original polynomial
reconstruction in the three surviving combinations. A rational
potential, polynomial speeds, a unit row, a generic nonzero volume,
and even a canonical metric do not individually supply that step.
The null cubic perfect-power divisor is a concrete place to apply
original-coordinate irreducibility and the canonical derivation,
while retaining the factor N(v) instead of imposing a constant
Jacobian. The two non-null types require a corresponding global
argument, not another coefficient-only example.

Even a complete exclusion of the exact cubic branch would not
prove that an arbitrary cylinder admits the original supplied
constant-acceleration frame. That independent entry obligation,
confirmation of the intended conjecture, and eventual human and
novelty review remain. The full research goal stays active and
unsolved. No external contact, public claim, submission or new
automation is part of this result.

## Sources

[^1]: The Stacks Project, [Lemma 10.47.8, tag 037P](https://stacks.math.columbia.edu/tag/037P),
    geometric irreducibility from relative algebraic closedness.
    The exact characteristic-zero coefficient-field use is detailed
    in the linked non-null proof. The remaining results here cite
    the specific local proof artifacts that contain their derivations.
