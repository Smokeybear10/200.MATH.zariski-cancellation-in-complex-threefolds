# Finite exact controls for the relative quadratic calculation

The standalone [checker](relative_quadratic_checks_pass79.py) has
four unittest methods and imports only `unittest` and SymPy.
Every assertion uses exact polynomial or rational-function arithmetic.
There are no solver/research imports, random samples, numerical
approximations or automatic source-theorem checks.

## 1. The formal five-row determinant

The first method retains all five rows and computes the full
determinant and all five entries in the original-w cofactor column.
It also multiplies that cofactor column by the original matrix,
checking its precise right-hand side and orientation. Substitution
of the affine-in-sigma coefficient expressions verifies the exact
coefficient of sigma.

The coefficient of Y in rho is separately extracted. The method
checks the expression eliminated by equality of the two mixed H
partials, and one formal cancellation specialization. It does not
assert that arbitrary entries in this matrix are actual partial
derivatives, that the determinant is a unit in an unknown quotient,
or that the matrix realizes an original polynomial action.

The actual-generation and integrability arguments remain in
[the complete quadratic proof](relative-quadratic-generation-pass79.md).

## 2. An actual retained conic action

The second method uses the original conic action and the relative
coordinates sigma,u,Y,v. Both polynomial inverse compositions use
simultaneous substitution. The transported original partial kills
the three transverse coordinates and sends w to one. The method
computes its bracket with E, goodness, original niceness and the
base Wronskian -2.

It also forms the actual five-variable lifted reconstruction with
F=Z-u-Y squared, computes its determinant -1, and checks all five
transported-partial values against that Jacobian. The sign of QZ
is positive. On the original coordinate list, Q squared has fourth
entry two and all other entries zero, Q cubed is zero, and the
specified two-by-two minor proves the second iterate is not parallel
to the first.

This is an already recognized actual action, not a new family.
It checks the formulas of the
[transported system](relative-good-partial-equations-pass79.md),
not the existence of such coordinates for an arbitrary action.

## 3. A formal quadratic relative equation

The third method works over a rational function field in the displayed
base coefficients, with F=aZ+bY squared+cY+d. It checks both triangular
coordinate inverse orders over that field, the invariant of the
triangular derivation, and the relative equation in the new variable.
For the exact formal Q coefficients from the quadratic proof, it
checks tangency to F, all second iterates and vanishing third iterates
on Y,Z,sigma. A displayed minor records nonparallel second iterates
for these independent formal coefficients.

The method also checks the precise cofactor self-divisibility
identity for T(a). It does not prove that the
formal T is locally nilpotent, apply the invariant-omission theorem,
or prove that a is a complex unit. Those are original-action gates
in the [recognition argument](nice-good-direction-recognition-pass79.md).
The actual polynomial derivation u partial_u supplies the negative
boundary: it takes u to u, so the derivative is self-divisible but
nonzero. Its eigenfunction identity makes every positive iterate
equal to u; the checker explicitly calculates four instances.
This field is not locally nilpotent and is not a substituted
original partial. In particular the triangular map over the
fraction field is not silently called a polynomial map over S.

## 4. A whole nonreduced fiber and its replica

The last method uses the weaker intrinsic polynomial model
D=u partial_y+2y partial_z with invariant v=uz-y squared.
Its coefficient gcd is one but its fixed ideal is proper.
Reduction is made modulo the full fiber ideal (u,y squared),
not its radical. The surviving nonzero class D(z)=2y and its
nilpotent coefficient are both checked.

The invariant replica uD has gcd u and vanishes on that whole
fiber; dividing its two coefficients by their actual common
factor recovers D. The generic slice t=y/u and the two relative
generators are checked only over the fraction field of the
intrinsic plane. Their gradient and differential-kernel vectors
agree there, with the displayed unit coefficient.

These are controls for the distinctions in the
[primitive relative-Jacobian proof](relative-jacobian-primitive-pass79.md).
They do not supply the simultaneous original nice/good frame,
claim a global slice for this D, or contradict recognition proved
with stronger actual-coordinate hypotheses.

## 5. Execution and provenance

The complete checker was read through EOF by its author and the
whitespace check passed. Its first run passed all four methods
in 0.192 seconds, exit zero, with complete stdout in tool chunk
`3eb279`. At Root's request the non-LND self-divisibility control
was added inside the existing third method. The final four-method
file again passed in 0.192 seconds, exit zero, with complete stdout
in tool chunk `af338a`; these identical rounded runtimes belong
to distinct runs. There were no failed test versions or runs.
The final checker SHA-256 is
`e574fa21954c8d1867a1f38fbd061231233d1f9979d746a9b1f4dc61b673626a`.

These finite checks are separate from the author's full written-proof
audits. They do not establish arbitrary irreducible-factor descent,
the conormal theorem, faithful flatness, invariant omission or a
universal recognition theorem. No runner or verification capture
was created by the controls author, and no new full regression is
claimed. Frozen files through pass78 and shared metadata were not
edited. There is no historical novelty, human expert review or
formal proof-certificate claim.
