# The entire invariant flow-coefficient span can contain no coordinate

Date: September 18, 2026. Private working proof. Novelty: UNKNOWN.

There is an actual polynomial coordinate frame on C^[4], a locally
nilpotent derivation E, and a specified polynomial slice s such that
EVERY nonconstant complex linear combination of ALL the invariant
coefficients rho(E^j z_i) has a critical point. Thus none is an
ambient coordinate, even though these coefficients generate ker E.

The example has E^3(z_i)=0. Its invariant coordinates are recoverable
by quadratic combinations, and changing the slice also permits linear
extraction. This excludes one proposed universal construction for a
specified slice. It is not a cancellation counterexample, an all-slice
obstruction, or recognition of an unknown kernel.

## 1. Actual frame, whole inverse, and exact coefficient space

Start in B=C[a,b,c,s], with E=partial_s and A=C[a,b,c]. Define

    t1=s+a^2,       x1=a+t1^2,
    t2=t1+b^2,      x2=b+t2^2,
    t3=t2+c^2,      x3=c+t3^2,
    z=(x1,x2,x3,t3).                                  (1)

This is a composition of six polynomial shears. Given independent
target coordinates (X1,X2,X3,U), recover the original variables by

    c=X3-U^2,      t2=U-c^2,
    b=X2-t2^2,     t1=t2-b^2,
    a=X1-t1^2,     s=t1-a^2.                          (2)

Each reverse step undoes its forward pair in (1), proving BOTH
inverse identities. In particular this is an actual coordinate
frame, not merely a tuple with unit Jacobian. The supplied s is
the polynomial given by (2) in the original z-coordinates.

Let rho be the canonical slice retraction, which here is evaluation
at s=0. Put

    S1=a^2, S2=a^2+b^2, S3=a^2+b^2+c^2,
    g1=a+S1^2, g2=b+S2^2, g3=c+S3^2.

Then, for i=1,2,3,

    xi=gi+2Si*s+s^2,  E(xi)=2ti,  E^2(xi)=2,
    E^3(xi)=0,       E(t3)=1.                         (3)

Consequently the ENTIRE coefficient span is exactly

    V=span_C {rho(E^j z_i): i=1,...,4, j>=0}
     =span_C {1,a^2,b^2,c^2,g1,g2,g3}.                 (4)

The seven functions in (4) are linearly independent: their linear
terms first separate g1,g2,g3, and the remaining distinct quadratic
monomials and constant are independent. In particular every member
has a unique expression

    H=kappa+alpha*a^2+beta*b^2+gamma*c^2
       +d*(a+a^4)+e*(b+(a^2+b^2)^2)
       +h*(c+(a^2+b^2+c^2)^2).                        (5)

We now prove, for ALL complex coefficients, that every nonconstant
H has an affine critical point.

## 2. Reduction to active variables and the intersection-count input

Constants do not affect the gradient. If d=e=h=0, the origin is
critical. Otherwise set a variable to zero whenever its corresponding
coefficient in (d,e,h) is zero. Its derivative then vanishes: apart
from that linear term, (5) depends on the variable only through its
square. The remaining polynomial is the same nested family in the
retained order, with one, two, or three active variables and all its
linear-bearing coefficients nonzero.

We use only the following complete-intersection case of projective
Bezout: m homogeneous cubics in P^m with finite common zero scheme
have total scheme length 3^m. Multiplicity at a point is the length
of its local quotient algebra, not the number of distinct points.

For clarity, its degree calculation is as follows. Finiteness makes
the homogeneous ideal have height m in the polynomial ring in m+1
variables. Such a list is a regular sequence: polynomial rings are
Cohen--Macaulay, and the height condition characterizes regular
sequences in their localizations at the homogeneous maximal ideal.
The graded condition then gives regularity in the polynomial ring.
The successive multiplication exact sequences give Hilbert series

    (1-T^3)^m/(1-T)^(m+1)=(1+T+T^2)^m/(1-T).

The eventual Hilbert function, hence the length of this projective
zero scheme, is 3^m. This is the usual complete-intersection proof,
not an assumption of generic or transverse intersection. See
[Stacks, polynomial Cohen--Macaulayness](https://stacks.math.columbia.edu/tag/00ND)
and [the dimension criterion for a regular sequence](https://stacks.math.columbia.edu/tag/02JN).
The projective intersection statement is also given in
[Vakil, Intersection Theory, Class1, Section2.2](https://math.stanford.edu/~vakil/245/245class1.pdf).

We apply this only under the temporary assumption that there is no
affine critical point. The explicit classification below then puts
all projective solutions in a finite set at infinity, establishing
the required finiteness. If an affine critical locus is positive
dimensional, the desired existence already holds.

Lengths may be computed in completed local rings. The polynomial
equations with invertible linear part permit formal elimination,
and completion preserves the length of these finite quotients.

## 3. One and two active variables

For one active variable the polynomial is
d*a+alpha*a^2+d*a^4, where d is nonzero. Its derivative is a
nonconstant cubic and therefore has a complex root.

For two active variables use names a,b and write

    H=alpha*a^2+beta*b^2+d*(a+a^4)+e*(b+(a^2+b^2)^2),
    d*e != 0.

The homogenized gradient in projective coordinates [a:b:w] is

    G1=4a*((d+e)*a^2+e*b^2)+2alpha*a*w^2+d*w^3,
    G2=4e*b*(a^2+b^2)+2beta*b*w^2+e*w^3.              (6)

At w=0, both a and b nonzero would force a^2+b^2=0 and then
d*a^2=0, a contradiction. The b-axis is impossible since e!=0.
Thus the only possible infinity point is [1:0:0], and it occurs
only when d+e=0.

At that point set a=1. The equation G2=0 solves b as a formal
series divisible by w^3, since its b-linear coefficient is 4e.
Substitution in G1 leaves

    2alpha*w^2+d*w^3+O(w^6).

Its order is 2 if alpha!=0 and 3 otherwise. Thus the total
intersection length at infinity is at most 3. Under the assumption
of no affine critical point, Section2 requires total length 9.
This contradiction completes the two-variable case.

## 4. Three active variables: all points at infinity

Assume d*e*h!=0. Homogenize the gradient of (5) in [a:b:c:w]:

    G1=4a*((d+e+h)*a^2+(e+h)*b^2+h*c^2)
        +2alpha*a*w^2+d*w^3,
    G2=4b*((e+h)*(a^2+b^2)+h*c^2)
        +2beta*b*w^2+e*w^3,
    G3=4h*c*(a^2+b^2+c^2)+2gamma*c*w^2+h*w^3.         (7)

The quadratic coefficient matrix in the squared variables is

          [ d+e+h  e+h  h ]
    M  =  [ e+h    e+h  h ],       det M=d*e*h.
          [ h      h    h ]

At infinity, take the support of the nonzero entries among a,b,c.
Their squares must lie in the kernel of the corresponding principal
submatrix. Full support is impossible because det M!=0. The
two-variable principal determinants for ab,ac,bc are respectively

    d*(e+h),  h*(d+e),  e*h.

For ab support, e+h=0 leaves the a entry forced to zero, so there
is no genuine ab point. The bc determinant never vanishes. For ac
support, d+e=0 gives a^2+c^2=0. Single supports give precisely the
following exhaustive list:

| Point in P^3 | Existence condition |
| --- | --- |
| P_a=[1:0:0:0] | d+e+h=0 |
| P_b=[0:1:0:0] | e+h=0 |
| P_zeta=[1:0:zeta:0], zeta^2=-1 | d+e=0 |

There is no c-axis point because h!=0.

## 5. Local lengths at the two axis points

At P_a use a=1. Because e+h=-d!=0 and h!=0, the equations G2,G3
have invertible linear part in b,c. They solve b,c=O(w^3).
The remaining G1 equals

    2alpha*w^2+d*w^3+O(w^6).

The length is therefore 2 if alpha!=0 and 3 otherwise.

At P_b use b=1 and e+h=0. The third equation is

    G3=c*(4h*(a^2+1+c^2)+2gamma*w^2)+h*w^3.

It solves c=w^3 eta(a,w), where eta is a formal unit. Thus

    G2=w^2*(2beta+e*w+4h*w^4*eta(a,w)^2).

This generates (w^2) when beta!=0 and (w^3) when beta=0.
Call that exponent p, so p=2 or3. Modulo w^p, G1 becomes

    4d*a^3                           if p=2,
    4d*a^3+2alpha*a*w^2              if p=3.

After division by 4d this is monic of degree three in a. Its
quotient over C[[w]]/(w^p) is free with basis 1,a,a^2, of length
3p. Hence the P_b length is exactly 6 or9. This retains the
corank-two case; it is not an implicit smoothness assumption.

## 6. Local lengths at the mixed points, including resonance

Assume d+e=0 and use a=1 near P_zeta, with c=zeta+delta and
zeta^2=-1. The pair G1,G2 has invertible linear part in c,b:
the corresponding diagonal entries are 8h*zeta and 4e.
It therefore solves c,b as formal series in w. In particular

    b=-w^3/4+O(w^5).

Replace G3 by G3-c*G1, an operation preserving the local ideal.
The exact remaining expression is

    R=4d*c*b^2+2*(gamma-alpha)*c*w^2+(h-d*c)*w^3.       (8)

If gamma!=alpha, its order is2. If gamma=alpha but h!=d*zeta,
its order is3.

It remains to cover gamma=alpha and h=d*zeta. From G1=0 we get

    delta=alpha*w^2/(4d)+w^3/8+O(w^4).                 (9)

In (8), the w^5 coefficient is -alpha/4. Thus if alpha!=0 the
length is5. If alpha=0, (9) has no quadratic term, and the w^6
coefficient of (8) is

    d*zeta/4-d/8=d*(2zeta-1)/8 != 0.                  (10)

The length is then6. These exhaust the resonance: a point cannot
have higher length under the stated hypotheses. The two choices
zeta=i and zeta=-i cannot both satisfy h=d*zeta.

## 7. The infinity count cannot absorb the whole intersection

P_a cannot coexist with either P_b or either mixed point, because
such coexistence would make d=0 or h=0. Its total contribution is
at most3.

If P_b and the mixed points coexist, then d=h and e=-h. Neither
mixed point can resonate, since zeta is i or -i rather than1.
Their combined length is at most 9+3+3=15.

If only the mixed points occur, at most one resonates. Their total
length is at most6+3=9. If only P_b occurs, its length is at most9.
These possibilities include the empty infinity set. In every case
the total length at infinity is at most15.

Under the assumption of no affine critical point, (7) would be a
finite projective intersection of three cubics with total length27
by Section2. All its points would be at infinity, contradicting
the bound15. Therefore an affine critical point exists. Together
with Sections2--3 this proves the assertion for every coefficient
choice in (5), including all vanishing-coefficient cases.

## 8. Coordinate consequences and the exact boundary

Let H be any nonconstant member of V. At its critical point in
Spec A=C^3, the differential also vanishes in Spec B=C^4, because
H has zero s-derivative. This remains true in the actual z-frame
by its polynomial inverse. A polynomial coordinate has nowhere-zero
differential: differentiate a full polynomial inverse to see this.
Thus NO nonconstant member of V is a coordinate of A or of B.

At such a point p, H-H(p) is a nonzero element of the square of
the regular local maximal ideal of A. Its hypersurface local ring
has dimension two and cotangent dimension three, so that fiber is
not regular. Consequently no nonconstant member of V supplies an
affine-plane fibration of A either.

Nevertheless the nonlinear extraction degree in this example is
exactly two. Equations (3) give, for a1=a,a2=b,a3=c,

    ai=rho(xi)-(rho(E xi)/2)^2.                        (11)

These are quadratic expressions in the displayed coefficient list,
and degree one is impossible by the critical-point theorem. In
particular C[V]=A. No universal quadratic extraction bound for
arbitrary sliced actions is asserted.

The same action has the DIFFERENT slice u=t3, itself an original
ambient coordinate. Since x3=c+u^2 and Ec=0, its slice retraction
satisfies rho_u(x3)=c. Linear extraction therefore succeeds after
this change of slice. The obstruction retains the specified s;
it is not quantified over all slices or all ambient frames.

## 9. Antecedents, verification, and the remaining global question

The two-dimensional seed (s+a^2,a+(s+a^2)^2) already occurs in
[81](quadratic-flow-filter-obstruction-pass81.md). Its padded
four-variable version leaves invariant coordinates b,c untouched
and does not establish the present no-coordinate claim.

[95](projected-generator-linear-extraction-obstruction-pass95.md)
excludes linear extraction from four projected generators, but its
higher Taylor coefficients recover coordinates. The generating-space
controls428/432 do not arise as the exact full coefficient list of
four specified ambient coordinates. The present nested shear chain
retains that constraint. A targeted archive comparison is not a
historical novelty audit, and no priority claim is made.

Root, Jet, General and Geometry independently checked the uniform
critical-point argument before this saved version. Fresh unsaved
root621334 verifies both whole inverse orders, the Jacobian,
all Taylor coefficients, constant accelerations, homogenized
gradients, principal minors and the mixed-point residual identity.
An earlier scratch assertion645a3a compared unexpanded expressions
structurally; c2d66d verified that every polynomial residual was zero,
and621334 replaced that comparison with exact polynomial equality.
No mathematical identity failed. Independent fresh checks are
Jet27aa25 and General6af933.

The proof above, not those finite computations, covers every complex
coefficient vector. No saved checker was executed, imported,
compiled or edited. Internal AI reviews and symbolic computations
are not proof-assistant verification or human expert review.

The proposed specified-slice linear-extraction route is now refuted,
even using the entire finite orbit-coefficient list. Nonlinear
extraction, justified slice selection, and genuinely global degree
control remain open routes. This note supplies no general such
construction. Corrected complex-threefold cancellation remains
UNSOLVED, and the working interpretation has not been confirmed
by Luo.

