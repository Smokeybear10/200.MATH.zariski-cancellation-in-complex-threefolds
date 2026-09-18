# Quadratic coefficient obstructions and a sharp slice-degree bound

## 1. Scope

All rings below are polynomial rings over C, with the displayed
ordinary total degree. Two distinct controls delimit a proposed
low-coefficient-degree route to cancellation.

First, an actual quadratic-coefficient sliced LND can have neither
an affine-linear invariant nor an affine-linear slice, and its
coefficient Jacobian need not be nilpotent. Its homogeneous quadratic
homogenization can have no genuine linear local slice at all.
Second, an already-recognized triangular family of coefficient
degree n has minimum total slice degree exactly2n+1. In particular,
quadratic coefficients do not guarantee a quadratic polynomial slice.

Both sliced controls here have whole polynomial translation certificates
and polynomial kernels. The homogenized action in Section3 instead fixes
the origin and has no slice; its kernel is not identified here. None
provides a counterexample to cancellation. No classification of arbitrary
quadratic-coefficient sliced actions is proved. General cancellation
remains UNSOLVED; novelty is UNKNOWN.
The known actions and replica constructions are separated below from
the exact total-degree minimum established for the retained family.

## 2. A quadratic action with neither affine-linear alternative

On B=C[X,Y,Z,W] put

    E=(1+2YZ) partial_X+(X-Z^2) partial_Y
      +Y partial_Z+Z partial_W, s=X-Z^2.                (1)

The polynomial shear replacing X by s is invertible, with
X=s+Z^2. In the coordinates(s,Y,Z,W), equation(1) becomes

    E=partial_s+s partial_Y+Y partial_Z+Z partial_W.

This triangular affine action is locally nilpotent, and Es=1.
Explicit invariant coordinates are

    A=Y-s^2/2,
    B0=Z-sY+s^3/3,
    C0=W-sZ+s^2Y/2-s^4/8.                             (2)

For independent new coordinates(S,A,B0,C0) the whole inverse is

    Y=A+S^2/2,
    Z=B0+SA+S^3/6,
    W=C0+SB0+S^2 A/2+S^4/24,
    X=S+Z^2.                                         (3)

Substitution in both orders gives the identity: the first three
lines are the finite translation flow from s=0, and the last
undoes the shear. Direct differentiation gives E(A)=E(B0)=E(C0)=0.
Thus B=C[s,A,B0,C0] and ker E=C[A,B0,C0]. Invertibility is
established by(3), not inferred from a constant Jacobian.

For any affine-linear polynomial ell, E(ell) is a constant
combination of the four coefficient polynomials in(1). If

    a(1+2YZ)+b(X-Z^2)+cY+dZ is constant,

comparison of the coefficients of X,YZ,Y,Z gives b=a=c=d=0.
Consequently E(ell) can be constant only when ell itself is
constant. This simultaneously excludes nonconstant affine-linear
invariants and affine-linear slices. In particular no affine-linear
change can triangularize this action: the first coordinate in a
triangular ordering would have constant derivative. A nonlinear
triangularization is explicitly present above.

## 3. The coefficient Jacobian and homogenization

Let J be the Jacobian of the four coefficient polynomials of E
with respect to X,Y,Z,W. Its upper-left three-by-three block is

    [ 0  2Z   2Y ]
    [ 1   0  -2Z ]
    [ 0   1    0 ].

The fourth column of J is zero and its last row is(0,0,1,0).
The characteristic polynomial is

    det(lambda Id-J)=lambda*(lambda^3-2Y).             (4)

It is not lambda^4, so J is not a nilpotent polynomial matrix.
For example at Y=1 it has nonzero eigenvalues. Local nilpotence
of E and a polynomial slice therefore do not supply the Jacobian
nilpotence hypothesis required by the audited quadratic-map results.

Introduce a homogenizing variable h. The homogeneous quadratic
derivation on C[X,Y,Z,W,h] is

    Ehat X=h^2+2YZ, Ehat Y=hX-Z^2,
    Ehat Z=hY, Ehat W=hZ, Ehat h=0.                   (5)

It is locally nilpotent. More generally, homogenizing any
quadratic-coefficient LND in this manner gives, for each original
coordinate V and every m>=1,

    Ehat^m(V)=h^(m+1)*(E^m V)(X/h,Y/h,Z/h,W/h).

The right side is polynomial because deg(E^m V)<=m+1; the chain
rule proves the formula by induction. Local nilpotence of E
therefore proves that of Ehat on every generator.

The only homogeneous linear invariants of(5) are C h, by comparing
monomials in its four nonzero coefficients. In fact

    Ehat^2 X=2hY^2+2hZX-2Z^3,
    Ehat^2 Y=h^3,
    Ehat^2 Z=h^2X-hZ^2,
    Ehat^2 W=h^2Y.

These four cubics are linearly independent over C. Hence

    ker(Ehat^2) intersect span_C(X,Y,Z,W,h)=C h.       (6)

A genuine local slice ell must have Ehat ell nonzero and
Ehat^2 ell=0. No homogeneous linear ell has that property; adding
a constant does not help. Thus homogenization cannot invoke a
general theorem promising an additional linear local slice. The
positive results for quadratic homogeneous QUASI-TRANSLATIONS have
a different hypothesis and are not contradicted by this example.

## 4. A necessary degree bound for commuting homogeneous pieces

Let R=C[z1,...,zm], D=L+H, where L is a constant-coefficient
derivation, H has homogeneous coefficients of degree n>=2, and
[L,H]=0. Suppose v is a polynomial slice: Dv=1, deg v=d.
Set k=floor((d-1)/n). Then there is a homogeneous linear form
ell such that

    L ell=1, H^(k+1) ell=0.                           (7)

Here no existence of a slice is deduced from(7). The implication
is necessary and does not require a classification of ker H.

Proof: both L and H lower total degree by1 modulo n, since their
actual degree shifts are -1 and n-1. Retain from v just its
homogeneous pieces of degrees1 modulo n. Their sum is still a
slice, because only that congruence class can contribute to the
constant output. Write it as sum_(j=0)^k v_(1+jn), allowing zero
pieces. Comparing actual homogeneous degrees gives

    L v1=1,
    H v_(1+jn)+L v_(1+(j+1)n)=0 for 0<=j<k,
    H v_(1+kn)=0.

Commuting H past L and successively substituting these equations
gives H^(k+1)v1=(-L)^k H v_(1+kn)=0. Taking ell=v1 proves(7).

In particular, let r be the least positive integer for which
some linear form ell satisfies L ell=1 and H^r ell=0. If a slice
exists, (7) ensures that this r is defined, and every slice obeys

    deg v>=1+n*(r-1).                                (8)

This is a lower bound in the DISPLAYED grading. It is not invariant
under arbitrary nonlinear coordinate changes. Finiteness of r is
not asserted to be sufficient for a slice or for recognition.

## 5. An existing replica family attains the bound

For every n>=2 set, on R=C[x,y,z],

    D_n=x^n partial_y+(1+x^(n-1)y) partial_z,
    delta=x partial_y+y partial_z,
    F=y^2-2xz, T=x^(n-2)F/2.

Here delta is triangular locally nilpotent, delta F=0, and delta T=0.
Consequently exp(T delta) is a whole polynomial automorphism with
inverse exp(-T delta). It fixes x and sends y,z to

    p=y+x^(n-1)F/2,
    q=z+x^(n-2)yF/2+x^(2n-3)F^2/8.                   (9)

For new coordinates(x,P,Q), put F_*=P^2-2xQ and
T_*=x^(n-2)F_*/2. The full inverse is

    y=P-xT_*, z=Q-PT_*+xT_*^2/2.                    (10)

Indeed p^2-2xq=F, so T_*=T on substitution, and the opposite
triangular flows compose to the identity in both orders.
Also D_n F=-2x, which directly gives D_n p=0 and D_n q=1.
Thus D_n is exactly partial_q in these coordinates and
ker D_n=C[x,p]. Its coefficient degree is n, while q has total
degree exactly2n+1; its unique highest homogeneous summand is
x^(2n-3)F^2/8.

To prove MINIMALITY, write D_n=L+H with L=partial_z and
H=x^(n-1)delta. They commute and satisfy Section4's degree
conditions. Every linear form with L ell=1 has z coefficient1,
so

    H^2 ell=x^(2n-1) nonzero, H^3 ell=0.

Therefore r=3 in(8), and every polynomial slice has total degree
at least2n+1. Equation(9) attains that bound. Equivalently, if a
slice of degree<=2n existed, its degree1 modulo n part would be
v1+v_(n+1). Applying delta to the degree-n equation and using
[delta,partial_z]=0 would force x^n=0, a contradiction.

The exact result is

    min{deg v : D_n v=1}=2n+1 for every n>=2.         (11)

It persists after adjoining any number of D_n-invariant polynomial
variables. A lower-degree slice in that extension would specialize
those variables to zero to give a lower-degree slice in R, while q
still supplies the upper bound. In particular n=2 gives an ACTUAL
sliced quadratic-coefficient action on C^[4] whose smallest slice
has total degree5. This is an already-recognized polynomial kernel.

## 6. Deduplication and the remaining global obligation

The n=2 action and its exact expanded q already occur in
[arbitrary-coefficients-pass.md](arbitrary-coefficients-pass.md),
Sections1--2. That note's general replica construction also contains
the polynomial automorphism mechanism above. The separate
[commuting-coordinate-partial note](commuting-coordinate-partial-pass.md),
Section2, proves that the smallest degree in the ADDED VARIABLE is
two for n=2. That is not the smallest ordinary TOTAL degree. The
additional claim here is the proved exact total-degree minimum(11)
and its homogeneous recurrence proof, not a new action or replica.

The recurrence itself also has a retained antecedent: the
[weighted extension note607](homogeneous-extension-slice-degree-window-boundary-pass607-working.md),
Sections4--5. In the four-variable LND setting, normalize L=partial_t
and write H=H_base+psi partial_t. Commutation makes the coefficients
t-independent. Note607 with d=n-1, ell=n and weight q=1 gives exactly
the degree-class equations and terminal condition used here. Its
recurrence does not require an irreducible base. Applied to(9), with
H_base=x^n partial_y and psi=x^(n-1)y, every linear base correction
leaves H_base-degree one. Note607's M>=2 therefore already implies
degree>=1+2n. Thus(11) is an explicit corollary of retained methods,
not a newly discovered recurrence. Section4 packages that argument
in arbitrary dimension without requiring local nilpotence.

The retained [quadratic source audit74](quadratic-nice-source-scope-pass74.md)
correctly distinguishes ordinary coefficient degree, nice flow,
time degree, and slice degree. It did not establish that general
quadratic-coefficient LNDs have nilpotent coefficient Jacobians.
Equation(4) explicitly disproves that possible extra implication.
The older time-degree control251 has a different degree premise.

The retained affine-linear recognition74 remains valid. Our first
control prevents extending its affine-linear choice directly to all
quadratic coefficients. Our second prevents replacing the hypothesis
of a quadratic-slice theorem by quadratic COEFFICIENTS. Neither
control excludes a nonlinear invariant coordinate, a higher-degree
slice, or a general recognition theorem using additional arguments.

No reduction of an arbitrary A[u]=C^[4] to coefficient degree two
has been shown, and even general quadratic recognition is not proved
here. The original target still requires a genuinely global entry
or a sufficient degree estimate, not one of these false shortcuts.
No mathematical novelty or priority clearance is asserted.

## 7. Published antecedent and verification record

El Houari and El Kahoui, *Algorithms for recognizing coordinates in two
variables over UFD's*, ISSAC2004, Section6.2 Example1, give the Nagata
coordinate and a minimum-degree mate over Z[Z][X,Y]. Under
(X,Y,Z)=(-4z,y,x/2), their displayed pair is exactly(p_2,-4q_2).
Their algorithms measure relative degree in X,Y, treating coefficients
in Z[Z] as degree zero. They do not state the all-n ordinary total-degree
formula(11). However, the n=2 ordinary minimum follows from this known
pair and a short leading-coefficient argument. It must not be presented
as a newly discovered family. This bounded comparison gives no novelty
clearance for the general recurrence or all-n statement.
[Author-uploaded primary paper](https://www.researchgate.net/publication/221563987_Algorithms_for_recognizing_coordinates_in_two_variables_over_UFD%27s),
DOI10.1145/1005285.1005306. Root directly read the displayed Example1,
Theorem2.3 with proof, Theorem4.3 with proof, and the degree conventions
in the implementation. Geometry independently checked the comparison.
Fresh unsaved root check5a35f0 verified the exact pair substitution.

The initial242-line source had SHA256
cb7e61c866b9a8cd5636563ee402f272b9ad7c664eb4aedec7ab68d5c7b6d3f4.
Root read it through EOF in38c5cc and again9d6888. Full-source AI reviews
were General(cfdabb/baa412, final aa8b21), Jet(0dd991, final a27bc9),
and Geometry(2b20f2, final1f0f21). General and Jet found the unqualified
scope sentence claiming every example had a translation certificate.
It is now explicitly restricted to the two sliced controls: the
homogenized action fixes the origin and cannot have a slice. No changes
to the formulas or mathematical proofs in Sections2--6 were required.

Fresh unsaved root d4d247 checked both inverse orders for(2)--(3), the
derivation identities, characteristic polynomial(4), and all four
homogenized second iterates. It also checked(9)--(10) in both orders,
the invariant and slice identities, and total degrees for n=2,...,6.
Jet independently checked the inverses(e10cd7), n=2,...,5(e7c09a),
and the homogenized cubic independence and fixed origin(a27bc9).
The general recurrence, all-n minimality, and all-stabilization result
are proved in the text, not inferred from these finite computations.

No saved checker was run, imported, compiled, or edited. Internal AI
reconstructions and symbolic identity checks are not formal verification,
human expert review, or evidence of mathematical originality. The
corrected complex-threefold cancellation goal remains UNSOLVED.
