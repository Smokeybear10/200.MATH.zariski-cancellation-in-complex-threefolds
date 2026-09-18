# Finite-thickening nilpotence and the algebraization gap

The nilpotence of a derivation on every finite thickening of an
irreducible hypersurface does not imply its local nilpotence on the
ambient polynomial ring. In fact, once a quotient LND is fixed, the
entire collection of finite-thickening tests collapses to a first
normal coefficient. A separate degree estimate gives an exact
quantitative condition under which a finite test really does prove
ambient nilpotence.

These statements address the ambient-action lifting gap. They do
not assert existence of a lift, a universal degree bound, or a
solution of affine-space cancellation. No novelty is claimed.

## 1. Exact criterion for all finite thickenings

Let W be an affine domain over a field k of characteristic zero, let F be a nonzero
prime nonunit, and let E be a k-linear derivation preserving (F). Put
R=W/(F), D=E mod F, and write E(F)=Fg. Assume D is locally
nilpotent. Then the following three conditions are equivalent:

1. E induces an LND on W/(F^N) for every positive integer N.
2. E induces an LND on W/(F^2).
3. g belongs to (F), equivalently E(F) belongs to (F^2).

The implication from 1 to 2 is immediate. For 2 to 3, identify
(F)/(F^2) with the R-module R by sending the class of Fh to
the class of h. The induced operator is

\[
T(h)=D(h)+\bar g h.
\]

In particular E^q(F) corresponds to T^q(1). If bar(g) is
nonzero, this can never vanish. If D is zero this follows from
T^q(1)=bar(g)^q and the domain hypothesis. If D is nonzero,
localize R at all nonzero elements of ker D. The usual local
slice identity gives K[s], where K=Frac(ker D) and D=partial_s.
The nonzero image of bar(g) is a polynomial in s. For positive
degree, the highest term of (partial_s+bar(g))^q(1) is the
q-th power of the highest term of bar(g); differentiation has
strictly smaller degree. For degree zero the iterate is simply
bar(g)^q. Both cases contradict nilpotence on F. Thus bar(g)=0.

For 3 to 1, filter W/(F^N) by the powers of F. Since E(F) is
in (F^2), its induced operator on every successive quotient
(F^k)/(F^(k+1)) is exactly D under the same identification
with R. Each such operator is locally nilpotent. Given an
element, a finite number of iterations moves it one step
deeper in this finite filtration; repeating this N times
annihilates it. The number of iterations can depend on the
element and on N, as local nilpotence permits.

This proof uses a prime F so that R is a domain. It does not
apply the domain LND-degree rule directly to a nonreduced
thickening. In particular, preservation of (F) alone is not
enough, and exact preservation E(F)=0 is sufficient but not
necessary for all the finite-thickening tests.

## 2. A sliced derivation passing every thickening and failing globally

In W=C[f,s,z,t], for any integer a at least one, set

\[
E=\partial_s+f^a z\partial_z,\qquad F=f.
\]

Then E(F)=0 and E(s)=1. Its quotient at f=0 is the genuine
coordinate LND partial_s. Every finite thickening passes the
criterion in Section 1. Nevertheless

\[
E^q(z)=f^{aq}z\ne0
\]

for every q. E is not locally nilpotent. This remains a
countercontrol even with an actual ambient slice function,
an irreducible coordinate hypersurface, and a polynomial
quotient. The existence of the different good lift partial_s
is not denied; the example distinguishes a bad chosen lift
from nonexistence of all algebraic lifts.

The least positive q for which E^q(z) vanishes modulo f^N is
ceil(N/a). Thus each finite quotient has a finite exponential,
but the required degree in the additive parameter is unbounded
as N grows. The formal expression exp(T f^a)z does not define
a polynomial algebraic action on the ambient ring.

Exact F preservation is not needed for this phenomenon. The
derivation E=partial_s+f^2 partial_f has E(F)=F^2, and hence
passes every thickening, but E^q(f)=q! f^(q+1) never vanishes
in W. Both examples have a slice and fail global local nilpotence.

## 3. The necessary uniformity is exact

Suppose now W=k[x_1,...,x_n] and the equivalent conditions
of Section 1 hold. Let nu_i(N) be the least positive q with
E^q(x_i) in (F^N), which is finite for each N. Then E is
locally nilpotent on W if and only if, for every i, nu_i(N)
is bounded independently of N.

One direction is immediate from a coordinatewise nilpotence
bound for E. Conversely suppose nu_i(N) is bounded by L_i.
Because E preserves (F), it preserves every power of that
ideal. Thus E^(L_i)(x_i) lies in (F^N) for every N, even
when the first vanishing power is smaller than L_i. The
intersection of these powers in a polynomial domain is zero:
a nonzero polynomial cannot be divisible by powers of F of
arbitrarily large degree. Therefore E^(L_i)(x_i)=0. The
Leibniz rule gives local nilpotence on the whole ring.

The condition is uniformity in the thickening order, not just
compatibility of the actions on successive quotients.

## 4. A sharp linear lower bound for failed algebraization

Let d=max(1,max_i deg E(x_i)), using total polynomial degree,
and e=deg F, which is positive. Any nonzero coordinate iterate
satisfies

\[
\deg E^q(x_i)\le 1+q(d-1).
\]

Indeed differentiating lowers degree by at least one and
multiplying by a derivation coefficient raises it by at most d.
If x_i is not locally nilpotent under E, all its iterates are
nonzero. Their divisibility at the first vanishing order
modulo F^N therefore implies

\[
N e\le 1+\nu_i(N)(d-1).
\]

When d=1 this is impossible for large N. Hence an affine-linear
derivation passing every thickening is globally locally nilpotent.
When d is greater than one, a failed coordinate must satisfy

\[
\nu_i(N)\ge\frac{Ne-1}{d-1},\qquad
\liminf_{N\to\infty}\frac{\nu_i(N)}N\ge\frac e{d-1}.
\]

Thus unbounded indices cannot grow arbitrarily slowly. Each
coordinate has either a uniform actual nilpotence bound or
this linear lower bound. The family in Section 2 has e=1,
d=a+1 and nu_z(N)=ceil(N/a), attaining the asymptotic bound.

There is also a finite positive certificate. If, for each
coordinate, an exact modular calculation gives

\[
E^{q_i}(x_i)\equiv0\pmod {F^{N_i}},\qquad
N_i e>1+q_i(d-1),
\]

then the degree estimate forces E^(q_i)(x_i)=0 in W itself.
All such identities together prove that E is an LND. This
is a sufficient certificate with explicit numerical premises,
not a claim that those premises hold for every proposed lift
or that searching for a certificate always terminates.

## 5. Consequence for the cancellation investigation

Any strategy that lifts an action on a candidate hypersurface
and checks only finitely many F-adic thickenings must establish
an algebraization condition in addition to those tests. Checking
all thickening orders separately is still insufficient. The
criterion and lower bound above explain exactly why: the
nilpotence indices can grow linearly while the ambient field
continues to have nonzero iterates forever.

The companion exact controls verify the displayed families,
their nilpotence-index formula, the double-thickening operator,
and the positive degree certificate on a genuine LND. The
universal assertions have the written proofs above. This does
not lift the fixed surface's action into any unspecified
hypersurface embedding, exclude that embedding, or resolve
the original complex threefold conjecture.
