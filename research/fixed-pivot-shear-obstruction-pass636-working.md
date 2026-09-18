# Polynomial invariant shears can fail for every coefficient at a fixed pivot

Private working proof, September 17, 2026. On actual polynomial
three-space there are independent commuting primitive nonsliced LNDs
P,Q with no common fixed point such that every Q-H P, H in ker P,
is still primitive and has fixed points. In fact the entire LND
centralizer of P has no fixed-point-free member, even after primitive
division. Switching the pivot does produce a sliced action. This is
a boundary for fixed-pivot repair,
not an obstruction to recognizing the ring, which is explicitly C^[3].
General cancellation remains UNSOLVED. Novelty is UNKNOWN.

## 1. The actual polynomial pair

Work on A=C[x,y,z], and set

    r=xz+y^2,             g=r^2+y,
    Q=x partial_y-2y partial_z,
    P=2r Q-partial_z
      =2xr partial_y-(4yr+1)partial_z.                 (1)

The exact identities are

    Px=Qx=0,  Pr=-x,  Pg=0,  Qr=0,  Qg=x,
    [P,Q]=0,  P wedge Q=x partial_y wedge partial_z.   (2)

For the commutator, Q(r)=0 and [Q,partial_z]=0 in (1)
suffice. The wedge formula also follows directly from (1).
In particular the pair is independent over Frac(A).

The assertions to be proved are

    ker P=C[x,g],       pl(P)=x C[x,g],
    ker Q=C[x,r],       pl(Q)=x C[x,r],                (3)

where pl(L)=L(A) intersect ker L, together with the all-coefficient
failure

    for every H in C[x,g], Q-H P is a primitive
    nonzero LND with a nonempty fixed locus.          (4)

Thus these are full hypotheses on an actual polynomial ring. They
do not merely specify the leading fields of a putative coordinate
frame. The cylinder A[u]=C^[4] is already polynomial.

## 2. Whole actions, inverses, and the exact local chart

The Q-flow with independent complex parameter T is

    x -> x,
    y -> y+xT,
    z -> z-2yT-xT^2.                                 (5)

The P-flow is the whole polynomial map

    x -> x,
    y -> y+2xrT-x^2T^2,
    z -> z-(1+4yr)T+(2xy-4xr^2)T^2
             +4x^2rT^3-x^3T^4.                      (6)

Here r on the right means the original polynomial xz+y^2.
No denominator occurs in either map. On the x-localization the
actual inverse coordinate formulas are

    A_x=C[x,x^(-1),g,r],
    y=g-r^2,   z=(r-(g-r^2)^2)/x.                    (7)

In these coordinates

    P=-x partial_r,       Q=x partial_g.              (8)

Formula (6) results by replacing r by r-xT in (7), keeping
g fixed, and expanding. This proves its group law with independent
parameters T,S and its inverse at -T on A_x. Both sides of the
group law are whole polynomial maps on A and A injects into A_x,
so the same identities hold on A. Formula (5) has the same direct
group-law and inverse verification. The infinitesimal fields are
exactly (1). Equivalently, the locally nilpotent derivations in
(8) preserve the original generators by (1), so their restrictions
to A are locally nilpotent. This does not assert an exponential of
a variable-time derivation without checking its coefficients.

The fixed loci are

    Fix(Q)={x=0,y=0},
    Fix(P)={x=0,4y^3+1=0}.                            (9)

Indeed when x!=0, the equation P(y)=0 forces r=0, at which
P(z)=-1. At x=0, r=y^2 and P(z)=-(4y^3+1).
The formulas for Q are immediate. Both fixed loci are nonempty,
so neither action has a polynomial slice: evaluating L(s)=1 at
a fixed point would give 0=1. Their fixed loci are disjoint.
More intrinsically, (1) gives the whole identity

    P-2rQ=-partial_z,                                (10)

which also excludes any common fixed point.

Both actions are primitive. For Q the coefficient gcd is
gcd(x,2y)=1. For P, a common prime divisor of 2xr and 4yr+1
cannot divide r and hence would have to divide x; the latter
does not divide 4yr+1, whose reduction is 4y^3+1.

## 3. Exact kernels and full plinth ideals

These assertions can be proved by an elementary basis argument,
without importing a recognition theorem or merely computing some
local-slice values.

For Q, adjoining the named invariant r gives the exact presentation

    A=C[x,r,y,z]/(xz-r+y^2).                          (11)

This is an isomorphism because r=xz+y^2 eliminates the extra
variable. Replacing y^2 by r-xz expresses every element as a
C[x,r]-linear combination of

    y^i z^j,     i=0,1, j>=0.                        (12)

After inverting x, z=(r-y^2)/x. The images in (12) have distinct
y-degrees i+2j with nonzero leading coefficients (-1)^j x^(-j).
They are therefore linearly independent over C[x,r]. They form
a basis, and their Q-degrees are exactly i+2j since Q=x partial_y
on this chart. It follows that

    ker Q=C[x,r],
    ker Q^2=C[x,r] direct_sum C[x,r]y.                (13)

Applying Q to the latter and using Qy=x proves the second
plinth assertion in (3). If Q(a) is invariant, then Q^2(a)=0,
so this accounts for the entire plinth, not just one inclusion.

For P, adjoining r and g and then eliminating y=g-r^2 gives
the exact presentation

    A=C[x,g,r,z]/(xz-r+(g-r^2)^2).                    (14)

It has the monic rewrite rule

    r^4 -> 2g r^2+r-g^2-xz.

With weights one for r and four for z, and tie-breaking r>z,
this rule strictly lowers monomials. It supplies the spanning
set over C[x,g]

    r^i z^j,     0<=i<4, j>=0.                       (15)

Under (7), these polynomials have distinct r-degrees i+4j and
leading coefficients (-1)^j x^(-j). Thus they form a basis.
Their P-degrees are i+4j because P=-x partial_r. Consequently

    ker P=C[x,g],
    ker P^2=C[x,g] direct_sum C[x,g]r.                (16)

Since Pr=-x, this proves the first full plinth assertion in (3).
The two kernels have common intersection C[x]: if both actions
kill an element, (10) makes it independent of z, and Q then
makes it independent of y. This also verifies the common
quotient variable in the setting of the fixed-pivot criterion.

## 4. Every invariant-dependent shear remains nonsliced and primitive

Take an arbitrary H=H(x,g) in ker P and put L_H=Q-H P.
On the actual chart (7),

    L_H=x partial_g+x H(x,g) partial_r.               (17)

This is triangular and locally nilpotent over C[x,x^(-1)].
For example, choose a weight on r larger than deg_g H and
weight one on g; the field strictly lowers positive weight.
Its values on A are polynomial by its original definition.
Restriction from the localization proves that L_H is a whole
LND on A. It is nonzero, since L_H(g)=x.

Its full coordinate coefficients are

    L_H(x)=0,
    L_H(y)=x C,  C=1-2rH,
    L_H(z)=B,    B=-2y+(4yr+1)H.                     (18)

Write H_0(G)=H(0,G). On the entire fiber x=0 these become

    L_H(y)=0,
    L_H(z)=B_0(y)
          =-2y+(4y^3+1)H_0(y^4+y).                 (19)

If H_0=0, B_0=-2y has degree one. If H_0 is nonzero of
degree k>=0 and leading coefficient c, then B_0 has degree
4k+3 and leading coefficient 4c. In particular B_0 is always
nonconstant and never the zero polynomial. Over C it has a root.
For every such root y_0 the line x=0,y=y_0 is fixed by L_H.
Thus no H gives a fixed-point-free action or a slice.

This failure cannot be repaired by removing a polynomial gcd.
There is an exact Bezout identity in the whole A:

    (4yr+1)C+2rB=1.                                  (20)

So C and B have no common nonunit divisor. Any prime dividing
both xC and B would have to divide x. But B modulo x is the
nonzero polynomial (19), so x does not divide B. Hence L_H
is primitive for every H. No degree bound on H was assumed;
the two cases in (19) cover all polynomial coefficients.

The complete kernels of these shears can also be identified. Choose
F(x,G) in C[x,G] with F_G=H(x,G), and put

    k_H=r-F(x,g).
    L_H(k_H)=0,  ker L_H=C[x,k_H],
    pl(L_H)=x C[x,k_H].                               (21)

To prove the kernel assertion, the actual triangular coordinate
change on (7) gives A_x=C[x,x^(-1),g,k_H], with L_H=x partial_g.
On x=0,

    k_H bar=y^2-F(0,y^4+y).                           (22)

This polynomial has degree two if F(0,G) is constant, and degree
4 deg_G F(0,G) otherwise. In either case it is nonconstant.
If an element of C[x,x^(-1),k_H] had a minimal negative
x-denominator and belonged to A, its numerator modulo x would
vanish after substituting (22). The map C[K]->C[y] defined by
this nonconstant polynomial is injective, contradicting minimality.
This proves the kernel equality in (21). The full plinth is
principal by the polynomial-threefold statement in
[Dasgupta--Gaifullin, Theorem 2.10(ii)](https://arxiv.org/pdf/2306.00510v2).
Its generator divides L_H(g)=x, and cannot be a unit by (19).
Since x is prime in C[x,k_H], it is therefore associated to x.
This use of the published plinth theorem is on the actual C^[3].

## 5. The entire LND centralizer of the fixed pivot

There is a stronger exact classification on this same actual A:

    {E in LND(A): [E,P]=0}
       = {A_0(x)Q+B_0(x,g)P:
                         A_0 in C[x], B_0 in C[x,g]}. (23)

Zero is included on both sides. Every member of (23) has a fixed
point. The following proof concerns whole polynomial derivations,
not their associated graded fields.

Let E be an LND commuting with P. It preserves ker P. Since
P(r)=-x, the identity E(x)=-P(E(r)) and E(x) in ker P put
E(x) in pl(P)=x C[x,g]. The LND divisibility lemma forces
E(x)=0: if E(x)=x c were nonzero, derivation degrees would give
deg_E(E(x))=deg_E(x)-1 but deg_E(xc)>=deg_E(x).

The restriction to C[x,g] is therefore a C[x]-linear LND.
After inverting the nonzero elements of C[x], a one-variable
LND on C(x)[g] sends g to a constant in C(x). Intersecting
back with C[x,g] gives

    E(g)=a(x),            E(r)=-b(x,g).               (24)

The second assertion follows from P(E(r))=E(-x)=0. Now use
y=g-r^2 and r=xz+y^2 to obtain the entire identities

    E(y)=a+2rb,
    x E(z)=-2ay-(4yr+1)b.                            (25)

Whole regularity of E(z), reduced modulo x, requires

    2a(0)y+(4y^3+1)b(0,y^4+y)=0.                     (26)

If b(0,G) is a nonzero polynomial of degree k, its displayed
term has degree 4k+3, whereas the other term has degree at
most one. Thus b(0,G)=0, and (26) then forces a(0)=0.
It follows that a=x A_0 and b=x B_0 in their respective
polynomial rings. Equations (8),(24) now give precisely
E=A_0 Q+B_0 P on A_x, hence on A. Conversely each field on
the right of (23) commutes with P and, on (7), equals

    x A_0(x) partial_g-x B_0(x,g) partial_r.

It is triangular and preserves A, so it is an LND on A.
The set (23) is not asserted abelian. With coefficients a,c in
C[x] and b,d in C[x,g], the exact bracket is

    [aQ+bP,cQ+dP]=x(a d_g-c b_g)P.

On x=0 its only possibly nonzero coordinate value is

    E(z)=-2A_0(0)y-(4y^3+1)B_0(0,y^4+y).            (27)

If B_0(0,G)!=0 this polynomial has degree at least three.
If B_0(0,G)=0 and A_0(0)!=0 it has degree one; otherwise
it is identically zero. Each case gives fixed points on x=0.
Thus the whole centralizer has no free action and no sliced member.

This remains true after primitive normalization. Indeed write a
nonzero commuting E=c E_0, where E_0 is its primitive LND and
c is the polynomial gcd of its coordinate values. From

    P(c)E_0+c[P,E_0]=0

and the gcd-one coefficients of E_0, each prime with its full
multiplicity in c must divide P(c). Hence c divides P(c).
The same LND divisibility lemma for P gives P(c)=0 and then
[P,E_0]=0. The field E_0 belongs to (23), so it too has fixed
points. The standard primitive division is legitimate here:
E(c) is divisible by c, hence E(c)=0, and E=c E_0 with
E_0(c)=0 implies E^j=c^j E_0^j on A, proving local nilpotence.

## 6. A pivot switch succeeds, and its residual degree calculation

The obstruction is to the fixed pivot P, not to invariant shears
with every choice of pivot. The element r belongs to ker Q, and
(10) is the permitted invariant-dependent shear with pivot Q.
It gives -partial_z, whose actual coordinate slice is -z.
This field leaves the centralizer of the old pivot:
[P,-partial_z]=2xQ!=0, so it does not contradict Section 5.

The precise polynomial identity explaining this success is

    g-r^2=y.                                          (28)

On x=0 the two residual invariant functions are

    rbar=y^2,        gbar=y^4+y,
    C[rbar,gbar]=C[y].                                (29)

Their degrees are two and four. Replacing gbar by
gbar-rbar^2 lowers the degree four to one, with all lower
terms retained. The derivative of this whole replacement is
exactly the coefficient 2r in (10). Thus this example admits
an actual alternating-pivot reduction which no shear with
the original fixed pivot can perform.

Equation (29) is proved for this example only. An alternating
degree argument in the unknown stably polynomial setting would
need a justified common residual curve parameter, control of
the algebra generated by both residual invariants, and whole
polynomial lifts of the proposed replacements. Even a normal
polynomial image algebra by itself does not identify its parameter
with that of a supplied covering curve: C[v^2,v^4]=C[v^2] is a
normal polynomial line but is not C[v]. Neither those inputs nor
compatibility of reductions at different exceptional fibers follow
from this control. No general alternating-termination claim is made.

## 7. Scope, prior controls, and verification boundary

The conditional [fixed-pivot division criterion633](intrinsic-fixed-pivot-residue-repair-pass633-working.md)
remains valid. Its earlier shifted triangular pair disproves
automatic division at a bad fiber, but a constant pair change
already slices that example. Here all polynomial coefficients in
the fixed pivot kernel fail, even with disjoint fixed loci and
primitive normalization already performed. A pivot change works.

The preservation of local nilpotence under Q-H P is already a
case of [Dasgupta--Gaifullin, Lemma 3.2](https://arxiv.org/pdf/2306.00510v2),
using their ordered pair (Q,P) and coefficients (1,-H).
Their Lemma 3.17 constructs modified commuting chains on a
supplied global polynomial algebra R[x_1,x_2]=R^[2]; its proof
starts from the partials of those whole coordinates. Corollary
3.18 likewise assumes actual polynomial coordinates with the
remaining variables invariant. These statements cover the present
known-polynomial example, but a generic plane chart over C(f)
does not supply their global hypothesis for an unknown A.
Invoking that chain result as the missing A=C[f]^[2] recognition
step would assume the very coordinate presentation still needed.

The triangular field Q is a signed version of the standard action
already used in [44](heisenberg-height-one-bound-pass44.md).
The pair is structurally the elementary one-invariant-coefficient
shear construction, with its pivot interchanged and signs/scalars
adjusted; it is not presented as a separate new family. The focused
strengthening here is the exact fixed-pivot centralizer obstruction.
A bounded archive search found no previous occurrence
of this exact pair or its all-H obstruction. That search is not
priority clearance and supplies no claim of novelty.

Fresh unsaved algebra checks the complete flows, both group laws
and inverse orders, commutation, the localization inverse, the
kernel and cross-speed identities, and the universal Bezout
identity (20). The proof for all H is the degree argument (19),
not a finite coefficient search. No saved checker was executed,
imported or compiled. This saved source requires independent
complete review before acceptance. No human expert review or
formal proof-assistant verification is claimed.
