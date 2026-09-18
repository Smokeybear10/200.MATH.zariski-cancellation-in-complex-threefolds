# A saturated commuting pencil with no free direction

Private bounded working proof, September 17, 2026.

On the actual polynomial three-ring there are two primitive commuting
LNDs with no common fixed point whose entire invariant-field-saturated
module contains no free action and no sliced derivation. A coefficient
outside the common invariant field nevertheless gives a coordinate
translation. Thus neither saturation nor reselection within that module
automatically supplies a free direction on a bad fiber.

This is a boundary for a proposed method, not a cancellation counterexample.
The ring is already polynomial. General cancellation remains UNSOLVED and
novelty is UNKNOWN. No general deformation family is asserted here.

## 1. Whole polynomial input and statement

Work in the actual ring A=C[x,y,z], and put

    g=xz-y^2,
    h=2y-g^2,
    P=x partial_y+2y partial_z,
    Q=g P+partial_z.
    Q(x)=0,  Q(y)=xg,  Q(z)=1+2yg.                    (1)

In particular A[u]=C[x,y,z,u] is an actual polynomial cylinder. No
coordinate recognition or formal leading-field realization is assumed.
The conclusions are

    ker P=C[x,g],       ker Q=C[x,h],
    ker P intersect ker Q=C[x],
    pl(P)=x C[x,g],     pl(Q)=x C[x,h],               (2)

and the exact saturation equality

    M=(C(x)P+C(x)Q) intersect Der_C(A)
      =C[x]P direct-sum C[x]Q.                        (3)

Every nonzero member of M is an LND and has a fixed point on x=0.
In particular none has a slice. The original P,Q have no common
fixed point, but no constant direction in their pencil is free on
the whole fiber x=0. This remains true after every polynomial
common-invariant coefficient choice in (3).

The successful alternative is the whole identity

    Q-gP=partial_z,                                  (4)

whose coefficient g does not belong to C(x). The action on the right
is outside the rational span used in (3).

## 2. LND licenses and complete polynomial flows

P is triangular. For an independent complex flow parameter tau its
polynomial exponential is

    x_tau=x,
    y_tau=y+x tau,
    z_tau=z+2y tau+x tau^2.                           (5)

The inverse is obtained by replacing tau by -tau. Direct substitution
also gives the addition law for two independent parameters.

The identities

    P(g)=0,   Q(g)=x,   P(h)=2x,   Q(h)=0             (6)

follow from (1). Localizing at x gives the actual presentations

    A_x=C[x,x^(-1),g,y]
       =C[x,x^(-1),g,h],
    z=(g+y^2)/x,    y=(h+g^2)/2.
    Q(g)=x,  Q(y)=xg,  Q(h)=0.                       (7)

Thus Q is triangular on A_x and is locally nilpotent there. Its
values on A are polynomial by (1), so local nilpotence descends to A:
an iterate zero in the injective localization is already zero in A.

For completeness its whole flow, without a denominator in x, is

    x_tau=x,
    g_tau=g+x tau,
    y_tau=y+xg tau+(x^2/2)tau^2,
    z_tau=z+(1+2yg)tau+x(y+g^2)tau^2
            +x^2g tau^3+(x^3/4)tau^4.                (8)

The auxiliary g_tau is the value of x_tau z_tau-y_tau^2, not a
fourth independent coordinate. Expanding this relation verifies (8).
The formulas for g_tau and y_tau satisfy the parameter-addition law.
In A_x the identity z=(g+y^2)/x then gives the same law for z_tau.
All terms in (8) are polynomial in A, so injectivity of localization
proves that law in A itself. In particular substitution of -tau
after tau, and tau after -tau, gives the identity on all x,y,z.
Differentiation at tau=0 recovers the full Q in (1).

Since P(g)=0 and [P,partial_z]=0, equation (1) also proves

    [P,Q]=0.
    det [[P(y),P(z)],[Q(y),Q(z)]]=x.                  (9)

The determinant is a nonzero polynomial, so the fields are independent
over Frac(A). It is not asserted to be a unit.

## 3. Exact kernels, primitivity and plinths

From A_x=C[x,x^(-1),g,y] and P=x partial_y,
the localized P-kernel is C[x,x^(-1),g]. To contract it, write a
putative polynomial invariant as x^(-d)F(x,g), with F in C[x,g]
and d minimal. If d>0, its polynomiality implies

    F(0,-y^2)=0.

The substitution C[g]->C[y], g->-y^2, is injective. Hence x divides
F in C[x,g], contradicting minimality. This proves ker P in (2).

The second presentation in (7) gives ker(Q|A_x)=C[x,x^(-1),h].
The same contraction argument uses

    h mod x=2y-y^4.                                  (10)

Substitution of this nonconstant polynomial defines an injection
C[h]->C[y], so no minimal negative power of x can occur. Thus
ker Q=C[x,h]. On ker P the restriction of Q is x partial_g,
which proves the common kernel assertion in (2).

P is primitive since gcd(x,2y)=1. For Q, a common prime divisor
of xg and 1+2yg would divide x or g. It cannot divide g, since
1+2yg is 1 modulo g. It cannot be x, since

    (1+2yg) mod x=1-2y^3 !=0.                         (11)

Thus Q is primitive as well.

P vanishes on the line x=y=0. Q vanishes on each line x=0,
2y^3=1, with z arbitrary. A derivation vanishing at a point cannot
have a polynomial slice: evaluating D(s)=1 there is impossible.
Consequently neither P nor Q is sliced.

The full plinth principality theorem retained in
[27](intrinsic-plinth-boundary-pass27.md), Section 2, applies here:
the base is the actual polynomial three-ring, hence satisfies the
stably polynomial hypothesis used there. The plinth generator for P
divides P(y)=x; that for Q divides Q(g)=x. In each exact plane kernel,
x is prime. The generator is therefore a unit or an associate of x.
A unit would give a slice, excluded by the fixed lines. This proves
the two exact full plinth statements in (2). This use of principality
concerns the first image ideal only, not all higher image ideals.

There is no common fixed point of P and Q. Indeed if both vanished
at some point, (4) would make partial_z vanish there, which is false.
Equivalently, on P's fixed line Q(z)=1.

## 4. Exact invariant-field saturation

First, A intersect C(x)=C[x]. For a reduced rational expression in x
to be a polynomial in x,y,z, its denominator must divide its numerator
in C[x], as follows by comparing coefficients in y,z.

Let T=r(x)P+s(x)Q be any derivation in the left side of (3).
Applying T to the WHOLE polynomials g,h in A gives

    T(g)=s(x)x,     T(h)=2r(x)x.                       (12)

Both values lie in A intersect C(x). Therefore we can write
r=a(x)/x and s=b(x)/x, with a,b in C[x]; a factor 2 is absorbed
in a. Regularity of T(z) now says

    2a(x)y+b(x)(1+2yg) belongs to x A.

Reduction modulo x gives the polynomial identity

    2a(0)y+b(0)(1-2y^3)=0 in C[y,z].                 (13)

The constant coefficient forces b(0)=0, and then the coefficient
of y forces a(0)=0. Thus x divides both a and b, proving
r,s in C[x]. The reverse inclusion in (3) is immediate. Independence
from (9) makes the sum direct. This argument covers every rational
coefficient, with no degree bound or finite ansatz.

Every T=A_0(x)P+B_0(x)Q in (3) is locally nilpotent. The coefficients
are killed by both commuting fields. On any element of A, a sufficiently
high power of T vanishes by the binomial expansion and local nilpotence
of P,Q. All pairs of these derivations commute for the same reason.

## 5. No member of the saturated module is free

On the entire fiber x=0 one has

    Tbar=[2A_0(0)y+B_0(0)(1-2y^3)] partial_z.         (14)

If both constants are zero, T vanishes on the whole fiber. Otherwise
the bracketed polynomial has degree 3 when B_0(0)!=0, and degree 1
when B_0(0)=0. It is always nonconstant in the latter nonzero cases.
Over C it has a root. At any such root and any z, all three values
T(x),T(y),T(z) vanish. Thus every member has a fixed point, and no
nonzero member is free or sliced.

In particular there is no projective constant direction [alpha:beta]
whose action alpha P+beta Q is nowhere zero on the whole fiber x=0.
The absence of a common fixed point of P,Q is strictly weaker than
the existence of such a direction, even with the full polynomial
cylinder hypothesis.

Saturation cannot remove this obstruction: (3) already includes every
regular rational common-invariant combination. Dividing a member by
an invariant factor is no exception if the result stays in that rational
span and maps A into A; the result still belongs to (3).

## 6. Exact constant-pencil boundary

For every finite lambda in C put

    L_lambda=P+lambda Q,
    t_lambda=2g-lambda h.
    L_lambda(t_lambda)=0,
    P(t_lambda)=-2lambda x,   Q(t_lambda)=2x.          (15)

On A_x, L_lambda(h)=2x is a unit and t_lambda is the complementary
coordinate, since g=(t_lambda+lambda h)/2. Its kernel there is
C[x,x^(-1),t_lambda]. The specialization

    t_lambda mod x=lambda y^4-2y^2-2lambda y           (16)

is nonconstant for every lambda, including zero. The contraction
argument of Section 3 therefore proves

    ker L_lambda=C[x,t_lambda].                      (17)

Every nonzero constant combination alpha P+beta Q is primitive.
For beta!=0 its two nonzero coefficients are
x(alpha+beta g) and 2y(alpha+beta g)+beta. A common prime other
than x would divide alpha+beta g and then beta, impossible. The
prime x does not divide the second coefficient, whose specialization
is the nonzero polynomial 2alpha y+beta(1-2y^3). For beta=0 use
primitivity of P. Every such member is nonsliced by Section 5.
Its full plinth is (x) in its exact kernel, since for L_lambda
the invariant derivative L_lambda(h)=2x is available; for Q use (2).

In the affine extraction notation p=P(h)=2x, q=Q(g)=x, the whole
identity is

    p g-lambda q h=x t_lambda.                       (18)

Thus its multiplier is exactly x for every finite lambda. On x=0
the nonzero residue of L_lambda is a polynomial multiple of partial_z,
so its invariant fraction field is C(y). Equation (16) gives

    [C(y):C(t_lambda mod x)]=2 if lambda=0,
                                4 if lambda!=0.      (19)

For the infinity member Q the degree is also 4, by (10). Here the
degree of a polynomial u(y) equals [C(y):C(u(y))]: the polynomial
u(Y)-T is irreducible over C(T), as follows from its linearity in T
and Gauss's lemma, and has degree deg u in Y.
There is no drop to degree 1 anywhere in the constant pencil.
This computation is compatible with the primitive plinth-support
criterion in [27](intrinsic-plinth-boundary-pass27.md), Section 3.

## 7. Escape outside the module and precise scope

Identity (4) supplies the actual slice z and the known coordinates
x,y,z. It is not a rational common-invariant combination. If
partial_z=r(x)P+s(x)Q, evaluation on g gives s=1, and evaluation
on y then gives r=-g. But g is not in C(x), a contradiction.
The coefficient g does lie in ker P, so gP is itself an LND.
No assertion that an arbitrary such subtraction preserves local
nilpotence is needed: the full result of this subtraction is exactly
partial_z.

The bounded deduplication used the old
[rank-two action](rank-two-action-pass.md) and
[saturation](saturated-rank-two-pass.md) notes, the
[cross-frame argument](cross-frame-saturation-pass33.md), together with
relevant reads and text searches in pass-24/25/26/27, pass-35, pass-76 and
[561](saturated-commuting-leading-family-fiber-obstruction-pass561-working.md)
material. The Russell control in the saturation note has weaker input
than an actual polynomial three-ring. The positive 561 example already
shows why C(f)-saturation need not restore fiberwise independence, but
its saturated module contains a sliced direction. The shifted pair in
[633](intrinsic-fixed-pivot-residue-repair-pass633-working.md) obstructs
fixed-pivot residue lifting while a constant difference already slices.
The present control additionally excludes every free direction in the
whole saturated common-invariant module. No exact duplicate was located
in that bounded read; this is not a literature-priority conclusion.

The supplied example does not show that all intrinsic actions belong to
this module, that pair changes outside it fail, or that every unknown
stably polynomial threefold has such a pair. It rules out automatic
free-direction selection within the prescribed module. The general
cancellation objective is unchanged.

The construction and whole algebra were developed in the Jet subtask
while checking Root's constant-pencil proposal. Fresh unsaved calculations
check the full identities and both flow inverses; the written proofs give
the unrestricted kernel and saturation assertions. No saved checker was
executed. No public contact, human expert review, formal certification,
or novelty claim is reported. Independent saved-source review is required
before acceptance.
