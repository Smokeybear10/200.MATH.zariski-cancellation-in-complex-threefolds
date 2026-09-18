# Primitive intrinsic actions are normalized Jacobian fields

Private working proof, September 17, 2026. On the actual unknown
threefold A with A[u] isomorphic to C^[4], a primitive LND with
kernel C[f,g] is a nonzero constant multiple of its intrinsic
Jacobian field. This does not assume A is C^[3].

Two consequences for a primitive commuting independent pair are:

- Its two polynomial cross-values are constant associates. Their
  exceptional supports and multiplicities agree.
- Every critical point of the common invariant f is a common fixed
  point of the pair.

These statements do not produce a pair without common fixed points.
General cancellation remains UNSOLVED and novelty is UNKNOWN.

## 1. Actual geometric and algebraic input

Let A be a finitely generated complex domain with A[u]=C^[4], up
to a supplied algebra isomorphism. Then A is smooth of dimension
three, is factorial, and has unit group C*. Smoothness and factoriality
descend from a polynomial extension. The usual decomposition

    Omega^1_(A[u])/C = (Omega^1_A/C tensor_A A[u]) direct_sum A[u] du

and restriction at u=0 show that Omega^1_A direct_sum A is free
of rank four. Taking its top exterior power makes Omega^3_A free
of rank one. Fix a generator omega. It is a nowhere-zero algebraic
volume form, not a presumed coordinate volume on A.

Contraction with omega is an A-module isomorphism

    Der_C(A) -> Omega^2_A,   V |-> i_V omega.          (1)

These are finite projective modules; a global basis for Der_C(A)
is not required. For f,g in A define J(f,g) by

    i_J(f,g) omega = df wedge dg.                    (2)

Equivalently, for a in A,

    J(f,g)(a) omega = df wedge dg wedge da.           (3)

Let P be a nonzero primitive LND on A. Primitivity means that no
nonunit of A divides all values of P. The actual quotient theorem
from [the intrinsic quotient note](intrinsic-quotient-surface-pass.md)
gives a plane kernel S=ker P=C[f,g]. In particular f,g here are
coordinates of S, not asserted to be coordinates of A.

The kernel S is factorially closed in A. Thus every irreducible
element of S stays irreducible and prime in the UFD A. Also for
every nonzero b in S,

    S intersect bA = bS.                             (4)

Indeed if ba is killed by P, so is a. These facts retain the
actual invariant inclusion.

## 2. The Jacobian has no codimension-one factor

Choose a local slice v for P, with nonzero s=P(v) in S. The
local-slice theorem gives

    A_s=S_s[v]=C[f,g,s^(-1),v].                      (5)

On this chart df,dg,dv form a differential basis, and omega is
a unit times df wedge dg wedge dv. Thus J(f,g) is a unit times
partial_v there. In particular J has no prime divisor outside s.

It remains to exclude primes dividing s. Factor s in S. Each of
its irreducible factors pi remains prime in A; these account for
all its prime factors in A by factorial closure.

Choose ell=f or g so that

    d pi wedge d ell = epsilon df wedge dg,
    epsilon in S,  epsilon not in pi S.              (6)

Such a choice is possible because an irreducible polynomial pi
in two variables over C cannot divide both its formal partials.
One may choose ell=f when pi_g is nonzero modulo pi, and ell=g
when pi_f is nonzero modulo pi. The image of ell in S/pi S is
transcendental over C: otherwise ell-c would be a multiple of pi
for some c, contradicting the nonzero Jacobian in (6).

Let L=Frac(A/pi A). Equation (4) embeds S/pi S into A/pi A,
so ell remains transcendental in L. At this generic point the
conormal sequence is

    L d pi -> Omega^1_A tensor_A L -> Omega^1_L/C -> 0. (7)

The middle space has dimension three since A is smooth. The
right space has dimension two since L has transcendence degree
two over C and characteristic zero. Exactness therefore makes
the image of d pi a nonzero one-dimensional subspace.

The image of d ell in Omega^1_L/C is nonzero. For a transcendental
element of a finitely generated characteristic-zero field extension,
this follows by extending it to a separating transcendence basis.
Consequently d pi and d ell are linearly independent in the middle
space of (7), so their wedge is nonzero.

If pi divided J, (1)--(2) would make df wedge dg zero after tensoring
with L. Equation (6) would then make d pi wedge d ell zero, a
contradiction. This excludes pi. It excludes every prime factor of s,
and together with (5) proves that J is primitive on all of A.

Only generic points of the prime divisors were used. No normality,
smoothness or connectedness of every closed quotient fiber is being
assumed. Primitivity does not mean the field is nowhere zero.

## 3. Primitive proportionality has a constant multiplier

Over K=Frac(A), the two elements f,g are algebraically independent
and K has transcendence degree one over C(f,g). The K-vector space
of derivations killing f,g is one-dimensional in characteristic zero.
Both P and J are nonzero members, so

    P=cJ,   c in K*.                                (8)

For every prime pi of A, primitive J has a value not divisible by pi.
Polynomiality of P then gives ord_pi(c)>=0. Primitive P similarly
gives ord_pi(c)<=0. Hence c has valuation zero at every prime.
Since A is a UFD, c is a unit of A, and A*=C*. Therefore

    P=c J(f,g),   c in C*.                           (9)

This also proves J is locally nilpotent, but only after its constant
proportionality to the given LND is established. An arbitrary
Jacobian field need not be locally nilpotent.

## 4. Equalized cross-values for a primitive commuting pair

Let P,Q be primitive commuting LNDs, independent over Frac(A).
The actual plane quotients and Rentschler's theorem give

    ker P=C[f,g],   ker Q=C[f,h],
    Q(g)=q(f),     P(h)=p(f),
    ker P intersect ker Q=C[f],                      (10)

with p,q nonzero. The simultaneous choice of f is justified in
[635](fiberwise-free-direction-gluing-pass635-working.md), Section 1.

Apply (9) with the SAME omega to get

    P=c J(f,g),  Q=d J(f,h),    c,d in C*.            (11)

By the alternating identity (3),

    J(f,h)(g)=-J(f,g)(h),
    q=-(d/c)p.                                      (12)

Thus p and q are associates by a nonzero COMPLEX scalar, not just
by a rational function of f. They need not be constant polynomials.
All their root multiplicities agree. Rescaling Q by -c/d makes

    P(h)=Q(g)=p(f).                                 (13)

This adjustment preserves primitivity, commutation and every fixed
point locus. The equal-cross-value input for a switching argument
can therefore be imposed for a primitive pair without adding a
geometric hypothesis.

This refinement does not apply to an arbitrary pair before removing
replica factors. For example P=x partial_y and Q=partial_z commute
on C[x,y,z], with cross-values x and 1 in the natural kernel
coordinates; P is not primitive. The prior unequal-valuation
discussion for unrestricted pairs must not be carried into the
both-primitive case unchanged.

## 5. Critical points force joint fixed points

At a closed point a of X=Spec(A) where df(a)=0, (11) gives

    (i_P omega)(a)=0,  (i_Q omega)(a)=0.

Since contraction with the nonvanishing omega is an isomorphism on
each tangent space, P(a)=Q(a)=0. Consequently

    Crit(f) subset Fix(P) intersect Fix(Q).           (14)

In particular, if the pair has no common fixed point, df never
vanishes. The map f:X->A1 is then smooth, and every fiber is a
smooth surface. Each f-c is prime and nonunit by factorial closure
of C[f], so all these fibers are integral and nonempty.

This removes the NORMAL-fiber assumption from the earlier possible
recognition route. The independent source
[639](no-joint-fixed-point-recognition-pass639-working.md)
supplies its precise acyclicity and affine-space recognition
endpoint. Equation (14) alone is not a coordinate theorem.

The converse inclusion need not hold. On C[x,y,z], the primitive
commuting pair x partial_y+2y partial_z and
(xz-y^2)(x partial_y+2y partial_z)+x partial_z has a common fixed
line x=y=0 although dx never vanishes. Both fields are whole LNDs:
the second is triangular after inverting x, with g=xz-y^2,
Q(g)=x^2 and Q(y)=xg. Its two coefficients xg and 2yg+x have
gcd one. Thus the no-joint condition is a genuine extra restriction
on a supplied pair, even when the ambient threefold is polynomial.

## 6. Provenance and the remaining gap

The conormal method is already present in
[79](relative-jacobian-primitive-pass79.md) for an exact binary
hypersurface presentation, and in
[151](dense-all-degree-primitive-jacobian-factor-pass151-working.md),
Section 3, for an ambient four-variable Jacobian in a specialized
frame. The present proof removes those presentation/frame inputs:
it works directly with an arbitrary primitive intrinsic action
whose actual kernel plane is available. No new method or priority
claim is made.

The exact differential input (7) is the conormal sequence in the
[Stacks Project, Lemma 10.131.9, tag 00RU](https://stacks.math.columbia.edu/tag/00RU),
followed by localization. Its full statement and proof were read
directly. The dimension, factorial-closure and valuation arguments
are written out above. Separate proof reconstructions are required
before acceptance; symbolic polynomial controls cannot certify the
general module argument.

Nothing here constructs an independent commuting pair on every
stably polynomial A, or removes an existing common fixed point.
Those remain substantive gaps toward the original cancellation
goal. No human expert review, Lean certification, public contact
or novelty claim is asserted.

