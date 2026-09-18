# An exact gluing criterion for free invariant-coefficient actions

Private source-dependent working proof, September 17, 2026. The
criterion below is conditional, and its extra hypothesis is false
in general even on an actual polynomial three-ring. It is not a
solution of cancellation. Novelty is UNKNOWN.

## 1. Actual hypotheses and the finite test

Let A be an affine complex domain with A[u] isomorphic to C^[4].
Let P,Q be commuting locally nilpotent derivations independent over
Frac(A). The intrinsic quotient theorem gives actual coordinates

    ker P=C[f,g],  ker Q=C[f,h],
    Q(g)=q(f),    P(h)=p(f),
    ker P intersect ker Q=C[f],                       (1)

where p,q are nonzero polynomials. Here p and q denote cross-values;
they need not be the respective full plinth generators.

To justify this simultaneous notation, Q restricts to a nonzero LND
on the actual plane ker P. Rentschler supplies f,g and the first
cross-value. The restriction of P to ker Q is likewise nonzero.
Its kernel is the same ring C[f], so its Rentschler generator is an
affine-linear change of f, which can be absorbed in the other
coordinate. No coordinate of A or A[u] has been assumed.

Put Sigma={c in C:p(c)q(c)=0}. The following conditions are equivalent:

1. There exist a,b in C[f] such that L=aP+bQ is nowhere zero on
   Spec(A).
2. For each c in Sigma there exist constants (alpha_c,beta_c)!=(0,0)
   such that alpha_c P+beta_c Q is nowhere zero on the ENTIRE
   fiber f=c.

When they hold, the coefficients a,b can be constructed by ordinary
polynomial interpolation with gcd(a,b)=1 and b!=0. The resulting
action has a global slice, and there are actual elements t,s with

    A=C[f,t,s],  A[u]=C[f,t,s,u].                     (2)

The construction produces coefficients, not an explicit formula for
the final slice. Its existence uses the published free-action
theorem stated in Section 5.

## 2. The open chart and whole fibers

The cylinder makes A smooth and factorial, with constant units.
The intersection C[f] of the two kernels is factorially closed.
Thus each f-c is irreducible, hence prime, in A and is a nonunit.
Its fiber is consequently nonempty and integral. This observation
does not say that the fiber is normal or smooth.

Since P(h)=p and P(p)=0, the local-slice theorem gives the ACTUAL
presentation

    A_p=C[f,p^(-1),g,h],
    A_(pq)=C[f,(pq)^(-1),g,h].                       (3)

In particular, outside Sigma, P and Q are pointwise independent:
their values on g,h are respectively (0,p) and (q,0). This is a
statement at every point of that open set, not just at its generic
point. All possible failures of independence lie in the finite
collection of whole fibers indexed by Sigma.

## 3. Coprime interpolation of the directions

Suppose condition 2 holds. Let

    I0={c in Sigma:beta_c=0},
    b(f)=product over c in I0 of (f-c).               (4)

The empty product is 1. In particular b is never the zero
polynomial. Choose a polynomial a by interpolation with values

    a(c)=1                         if c in I0,
    a(c)=b(c) alpha_c/beta_c        if c in Sigma\I0. (5)

Distinct complex evaluation points allow these finitely many
conditions. If Sigma is empty, take a=0 and b=1.

Every root of b is in I0 and has a(c)=1, so gcd(a,b)=1. At a point
c in I0 the vector (a(c),b(c))=(1,0) is a nonzero scalar multiple
of (alpha_c,beta_c). At every other exceptional point, b(c)!=0
and (5) gives the same projective direction. Thus L=aP+bQ is
nowhere zero on all exceptional fibers by the stated hypothesis.

At a point outside those fibers,

    L(g)=b(f)q(f),  L(h)=a(f)p(f).                   (6)

Since p,q are nonzero there and a,b have no common root, these two
values cannot both vanish. This proves that L is nowhere zero
everywhere on Spec(A).

For the converse, evaluating any globally nowhere-zero aP+bQ
on f=c gives the required constant direction. The two evaluated
coefficients cannot both vanish because the fiber is nonempty.
This proves the equivalence, not just the sufficient direction.

## 4. Local nilpotence is global

Because a,b belong to the common kernel, the derivations aP and bQ
commute. For any v in A choose integers N,M with P^N(v)=0 and
Q^M(v)=0. Their binomial expansion shows

    (aP+bQ)^(N+M)(v)=0.

Every summand contains at least N applications of P or M of Q;
commutation allows these to be applied to v first. Hence L is
locally nilpotent on the whole ring A. This does not rely on
local nilpotence of an associated graded action or only on a
formal neighborhood.

The algebraic additive group over C has no nontrivial proper
algebraic subgroup. Thus a nowhere-zero LND defines a free
additive action.

## 5. Published recognition and the actual f-coordinate

The cylinder makes X=Spec(A) smooth and contractible. It also gives
a dominant morphism A^3 -> X: restrict the transported projection
A^4 -> X to an affine linear three-plane on which its differential
has rank three at one point. Kaliman--Saveliev Corollary 2.8(1)--(3)
therefore applies to the free action of L and yields

    A=(ker L)[s],  L(s)=1,  ker L isomorphic to C^[2]. (7)

These are the same verified primary inputs used in
[the intrinsic quotient note](intrinsic-quotient-surface-pass.md).

There is a further coordinate conclusion. Since b!=0, P is
independent of L over Frac(A). It commutes with L and restricts
to a nonzero LND on ker L. To see nonzeroness, if P killed ker L,
then in (7) it would be a multiple of partial_s and would be
dependent on L. Also

    ker(P|ker L)=ker P intersect ker L=C[f],          (8)

because for v in ker P, L(v)=b Q(v) and b!=0. Rentschler's
theorem on the actual plane ker L gives ker L=C[f,t]. This
proves (2). Neither the original cylinder variable u nor f was
assumed to be an ambient polynomial coordinate.

## 6. Why gluing adds something to a constant-pencil test

There is a simple actual-C3 control with a free direction on each
bad fiber but no globally free constant direction. Set

    A=C[x,y,z],  d=x(x-1),  g=dz-y^2,
    P=d partial_y+2y partial_z,
    Q=xP+partial_z.                                  (9)

They are commuting LNDs, independent where d!=0, with common
kernel C[x]. For a nonzero constant pair (alpha,beta), put
k=alpha+beta x. Then

    (alpha P+beta Q)(y)=kd,
    (alpha P+beta Q)(z)=2ky+beta.                    (10)

If alpha!=0 there is a fixed point on x=0, obtained by taking
y=-beta/(2alpha). If alpha+beta!=0 there is a fixed point on
x=1. At least one of these alternatives holds for every nonzero
pair. Thus no constant combination is free.

On x=0, however, Q=partial_z is free; on x=1, Q-P=partial_z
is free. Interpolating these choices gives

    Q-xP=partial_z,                                 (11)

a globally sliced action. Off x=0,1, pointwise independence holds
by (10). The exact same interpolation proof therefore applies
using this finite exceptional set, without needing to compute
the second quotient coordinate h in this example.

The underlying P,d,g were already present in
[19](relative-modification-classification-pass19.md). The control
is not claimed as a new family.

## 7. The essential premise really can fail

Absence of a common fixed point of P,Q is strictly weaker than
condition 2. The fully polynomial control in
[634](saturated-pencil-no-free-direction-pass634-working.md) has

    P=x partial_y+2y partial_z,
    g=xz-y^2,  Q=gP+partial_z.                       (12)

The pair has no common fixed point. On x=0 its constant directions
have z-speed

    2 alpha y+beta(1-2y^3).                         (13)

For every nonzero pair this is a nonconstant complex polynomial
and has a root. Thus no constant direction is free on that entire
fiber. In fact every action in the saturated C(x)-span fails there,
while Q-gP=partial_z succeeds outside that span.

Consequently the theorem above must not be promoted to an automatic
selection theorem under the stable-polynomial cylinder hypothesis.
Normality or smoothness of the f-fibers does not repair that
selection premise either: all x-fibers in (12) are affine planes.
Another recognition argument could use those geometric hypotheses,
but cannot conclude that this particular module contains a free
action.

## 8. Scope, prior work, and verification

The coefficient construction is elementary interpolation. The
endpoint uses established free-action recognition and plane LND
classification. A bounded comparison with the rank-two action and
saturation notes, passes35/43/44/47, and the intrinsic quotient note
found related local-slice and stronger fiberwise-independence
criteria, not this exact finite free-direction formulation. This
is not an exhaustive novelty audit and licenses no priority claim.

The useful conclusion is an exact finite obstruction for a specified
module of commuting actions. It neither constructs the initial
independent pair on every stably polynomial threefold nor supplies
the missing free directions when the criterion fails. General
cancellation remains UNSOLVED. Separate AI source reviews and fresh
symbolic checks are not human expert review or Lean certification.

Primary source: Shulim Kaliman and Nikolai Saveliev,
[*C+-actions on contractible threefolds*](https://www.math.miami.edu/~kaliman/library/KaSa.michigan.2004.quotient.pdf),
Theorem 2.7 and Corollary 2.8. The root reopened the entire
Corollary 2.8 statement and proof during this continuation.
