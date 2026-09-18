# The two-stage control loses its ML obstruction on the cylinder

General cancellation remains UNSOLVED and novelty UNKNOWN. For the explicit
nonpolynomial family R of671, this note proves

    ML(R)=k[a],       ML(R[u])=k.                            (1)

The first equality is proved in671 using Kaliman's published theorem.
Here the second follows from an explicit cylinder isomorphism after
inverting b, followed by invariant-denominator clearing. In particular,
trivial cylinder ML cannot repair the graded-data recognition shortcut.
Neither equality decides whether R[u] is a polynomial four-ring.

The construction adapts published Danielewski-cylinder interpolation. It
is not claimed as a new general cylinder theorem or a new cancellation
counterexample. All formulas below are defined over k[b,b^(-1)] itself;
no choice of algebraic roots or unproved Galois descent is used.

## 1. Setup and explicit localized comparison

Let k=C, n,m,q>=2, gcd(q,n*m)=1, and

    R=k[a,b,r,y,z]/(a*y-r^n-b^q-a, a*z-y^m+r).

Write T=k[b,b^(-1)], d=n*m, and use an auxiliary variable V. Define

    P(V)=V^d+b^q,
    H(V)=V^m/(n*b^q),
    g0(V)=V^m+P(V)*H(V),
    g1(V)=-(V-1)*H(V),
    G(a,V)=g0(V)+a*g1(V).                                  (2)

These belong to T[V] or T[a,V]. Consider the standard comparison ring

    B=T[a,V,W,S]/(a*W-P(V)).                               (3)

There is an isomorphism of T[a]-algebras B -> R_b[u] given by

    V -> y+a*u,
    W -> P(y+a*u)/a,
    S -> (r-G(a,y+a*u))/a^2.                               (4)

Both apparent a-denominators in (4) divide their numerators in the WHOLE
ring R_b[u]. Thus the comparison includes a=0 and is not just a generic
chart identity. The inverse sends r,y,z,u respectively to

    r'=G(a,V)+a^2*S,
    y'=(r'^n+b^q+a)/a,
    z'=(y'^m-r')/a,
    u'=(V-y')/a.                                          (5)

Again these are elements of the whole B. This section states the maps;
Sections2--4 prove all divisibilities and both inverse identities.

## 2. Three interpolation identities over T

The required identities in T[V] are

    P divides g0',
    P^2 divides g0^n+b^q,
    1+n*g0^(n-1)*g1 congruent V modulo P.                   (6)

For the first, differentiating g0 gives, modulo P,

    g0' = m*V^(m-1)+d*V^(d-1)*V^m/(n*b^q)
         = m*V^(m-1)*(1+V^d/b^q) = 0.

For the second use g0=V^m*(1+P/(n*b^q)) and V^d=P-b^q:

    g0^n+b^q
      congruent (P-b^q)*(1+P/b^q)+b^q
      congruent 0 modulo P^2.

Finally g0 congruent V^m modulo P, so

    n*g0^(n-1)*g1
      congruent -(V-1)*V^d/b^q
      congruent V-1 modulo P.

All denominators here are powers of b and the nonzero integer n, hence
are units of T. This calculation works without splitting P into roots.

## 3. Every forward coordinate is regular

Inside R define

    Sigma=sum_(j=0)^(n-1) y^(m*(n-1-j))*r^j.

Since y^m-r=a*z and r^n+b^q=a*(y-1),

    P(y)=y^d+b^q=a*(y-1+z*Sigma).                          (7)

Hence P(y+a*u) lies in aR[u], so W in (4) is regular even before
inverting b. For S, first calculate

    r-G(a,y)
      =r-y^m-P(y)*H(y)+a*(y-1)*H(y)
      =-a*z*(1+Sigma*H(y)).                               (8)

Modulo a, r=y^m and y^d=-b^q. Thus

    Sigma=n*y^(m*(n-1)),
    1+Sigma*H(y)=1+y^d/b^q=0 modulo a.

Consequently (8) belongs to a^2*R_b. Substituting y+a*u for y in G
changes g0(y) by a*u*g0'(y) modulo a^2 and changes a*g1(y) by a multiple
of a^2. By (6)--(7), g0'(y) belongs to aR_b. Therefore

    r-G(a,y+a*u) belongs to a^2*R_b[u].                    (9)

This proves S is regular. The relation aW=P(V) holds by construction,
so (4) defines a homomorphism on the entire quotient (3).

## 4. Every inverse coordinate is regular, and the maps are inverse

The ring B is a domain: T[a,V] is a UFD, and the primitive degree-one
polynomial aW-P(V) is irreducible over its fraction field and hence in
T[a,V,W]. Adjoining S preserves this. Also

    B_a=T[a,a^(-1),V,S],
    B/aB=(T[V]/(P))[W,S].                                 (10)

The same domain and injection statements for R_b[u] follow from671.
Put r'=g0+a*g1+a^2*S. Expansion yields

    r'^n+b^q+a
      =(g0^n+b^q)+a*(1+n*g0^(n-1)*g1)+a^2*L             (11)

for a polynomial L in T[a,V,S]. By (6), g0^n+b^q=P^2*A0 for A0 in T[V].
Inside B this term is a^2*W^2*A0. Thus y' in (5) belongs to B, and

    y' mod a = 1+n*g0^(n-1)*g1 = V in B/aB.                (12)

It follows that u'=(V-y')/a belongs to B. Also r' mod a=g0 mod P=V^m,
so y'^m-r' belongs to aB and z' belongs to B. The defining relations of
R hold identically for r',y',z'. This constructs the inverse homomorphism
on the whole rings.

One can write the inverse without any displayed a-denominators. Define

    A0=(g0^n+b^q)/P^2,
    B0=(1+n*g0^(n-1)*g1-V)/P,
    C0=((g0+a*g1+a^2*S)^n-g0^n-n*a*g0^(n-1)*g1)/a^2,
    K=W^2*A0+W*B0+C0.                                    (13)

The divisibilities above make A0,B0 elements of T[V] and C0 a polynomial
in T[a,V,S]. Then the same inverse is

    y'=V+a*K, u'=-K,
    z'=sum_(ell=1)^m binom(m,ell)*a^(ell-1)*V^(m-ell)*K^ell
          -W*H-g1-a*S.                                   (14)

Thus the formulas can be evaluated at a=0 using actual polynomials.

After inverting a, equations (4)--(5) plainly undo one another: V=y+a*u
and r=G(a,V)+a^2*S, with y determined by r and z determined by r,y. Both
rings inject into their a-localizations. Hence the two composition maps
are the identity BEFORE localization as well. This proves the isomorphism,
including all points with a=0 and b!=0.

## 5. A cylinder action moving a and extension across b=0

On B the standard derivation

    delta(a)=P'(V)=d*V^(d-1), delta(V)=W,
    delta(W)=delta(S)=delta(b)=0                           (15)

preserves aW-P(V). It is locally nilpotent: order W,S,b first, then V,
then a, and (15) is triangular with invariant first entries. Transport
it through (4), obtaining a locally nilpotent derivation delta_R on R_b[u].
In particular

    delta_R(b)=0,
    delta_R(a)=d*(y+a*u)^(d-1) != 0.                       (16)

Choose an integer L>=0 clearing the finitely many b-denominators in
delta_R(a), delta_R(b), delta_R(r), delta_R(y), delta_R(z), delta_R(u).
Then Theta=b^L*delta_R preserves R[u]. Because delta_R(b)=0,

    Theta^j(f)=b^(L*j)*delta_R^j(f).

It follows that Theta is a whole locally nilpotent derivation of R[u],
including b=0, and Theta(a)!=0. This does NOT extend the isomorphism (4)
across b=0. It extends a derivation by multiplying an invariant denominator.

Now extend the two derivations D,Delta of671 to kill u. Intersecting their
kernels with ker(partial_u) gives

    ML(R[u]) subset R intersect ker D intersect ker Delta = k[a].

For nonconstant f(a), Theta(f(a))=f'(a)*Theta(a)!=0 in characteristic zero.
Thus only constants remain in the full invariant, proving ML(R[u])=k.
Together with671 this proves (1), with a whole a-moving cylinder action.

## 6. Published antecedent and consequences for the research route

Moser-Jauslin--Poloni, *Isomorphisms between cylinders over Danielewski
surfaces*, Theorem4.0.1 and Section4, give the interpolation construction
underlying (4). Their Sections3.3--3.4 cover iterated/double surfaces with
modification exponents at least one and simple special roots. Our b=c!=0
fibers fall into that setting. Rather than infer a relative isomorphism
from separate fiberwise ones, Sections2--4 verify uniform formulas directly
over T. These formulas are an explicit adaptation of the published method,
not an assertion of a new cylinder-isomorphism principle.
[Primary preprint](https://arxiv.org/pdf/2002.12202).

The localized comparison has base b!=0; it does not prove
R[u]=k^[4]. A trivial Makar-Limanov invariant is necessary for a polynomial
ring but is not a recognition theorem. Here the intrinsic invariant is
nontrivial even though the cylinder invariant is trivial. In particular,
the existence of an action moving a after stabilization does not supply an
intrinsic action moving a on R. Such an intrinsic action is impossible
by671. A proof of general cancellation cannot simply assume that descent.

The explicit control now passes all image-ideal tests, shares the whole
graded data of a polynomial example, has the ordinary topology of C^3,
and has trivial cylinder ML. An actual polynomial cylinder is STILL not
established. No novelty clearance or cancellation counterexample is claimed.

## 7. Verification status

General and root independently reconstructed the uniform formulas and all
forward/inverse divisibilities; Jet independently reconstructed them and
supplied the denominator-free version (13)--(14). Root personally read the
relevant published construction and its hypotheses. The complete 229-line
source was held at SHA256
8846925de6e2c22337da96b5963ad3c86eb3650fab7a7f0a30eed7b2d2986061.
General (8d64ee/edb47e), Geometry (285f41/fcf3e5), and Jet
(ddf963/1a318d/c4b26d) each read the entire source through EOF and returned
CLEAN. All reviews finished before this provenance-only update.

Jet's fresh unsaved test1ca054 verified all congruences, whole forward and
inverse regularity, both inverse compositions, and the target derivation for
(n,m,q)=(2,2,3),(2,3,5). Root's independent unsaved run2d83c5/2fd819 passed
the three interpolation identities, whole inverse, defining equations and
coordinate reconstruction for the same two tuples. Its optional third
sample (3,2,5) was deliberately stopped during expensive symbolic expansion,
with no assertion failure; that sample is NOT recorded as passing. These
finite controls supplement the all-parameter proof, not replace it.

Saved checker scripts remain frozen. AI review is not human expert review
or formal certification. The original cancellation objective remains active.
