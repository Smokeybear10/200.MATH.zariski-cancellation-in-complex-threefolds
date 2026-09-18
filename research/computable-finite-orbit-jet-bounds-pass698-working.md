# Computable bounds for finite orbit normalization, without a growth estimate

## 1. Result and scope

Fix integers e>=0, d>=1, N>=1 and k>=2. Consider polynomial
derivations E of B=C[z1,z2,z3,z4] with coefficient degrees at most e,
a supplied polynomial s of degree at most d, and a point q satisfying

    E(s)=1, E^N(zi)=0 for all i, s(q)=0.                 (1)

There is a total computable integer D(e,d,N,k) such that every such
triple admits a polynomial automorphism F with polynomial inverse G,
both of degree at most D, which sends the E-orbit through q to the
standard fourth-coordinate line and makes E a translation modulo
the kth power of that orbit's ideal.

Computable means that an algorithm on these four INTEGER inputs
terminates with a valid uniform degree bound. No implementation,
numerical value, feasible running time, or favorable growth in k
is supplied here. In particular, this does not solve cancellation.

This is a combined corollary of the published finite-jet extension
theorem, the constructible-exhaustion argument in
[73](universal-family-degree-boundary-pass73.md), and decidability
of algebraically closed fields of characteristic zero. The finite
orbit-normalization premise and exact degree gate were established in
[696](orbit-jet-normalization-and-primitive-top-discontinuity-pass696-working.md).
No historical novelty is asserted. General cancellation is UNSOLVED.

## 2. A finite parameter scheme and its embedded orbit

Introduce coefficients for P1,...,P4 of degree at most e and s of
degree at most d, and four coordinates for q. Set

    E=sum_i Pi(z) partial_zi.

All coefficients of E(s)-1 and E^N(zi), together with s(q), are
finitely many effectively computable polynomials over Q in these
parameters. Their common zero scheme is denoted T=T(e,d,N).

Every complex point of T gives a locally nilpotent derivation:
the Leibniz rule kills any fixed monomial after sufficiently many
iterations, since its factors are original generators killed by E^N.
The slice theorem gives B=(ker E)[s]. The zero derivation is excluded
by E(s)=1. For N=1 the family is empty, which causes no exception
to the statements below.

Write the orbit through q as the polynomial map

    O_i(tau)=sum_{j=0}^{N-1} tau^j E^j(zi)(q)/j!.       (2)

Its coefficients are computable polynomials over Q in the parameters.
Equation (1) gives s(O(tau))=tau. Consequently the pullback
C[z1,...,z4] -> C[tau] is surjective, so O is a closed immersion
of schemes, not merely an injective set map. Denote its ideal by I.
It is the ideal of the fiber over the corresponding closed point
of Spec(ker E). Every closed orbit has a unique point on s=0;
existence also follows by flowing any point for time -s(point).

## 3. Exact finite witness equations

For an integer D>=1 introduce coefficient variables for four-tuples
F(z) and G(Y), each of total degree at most D. Impose coefficient
identities for

    G(F(z))=z, F(G(Y))=Y,                              (3)
    F(O(tau))=(0,0,0,tau).                             (4)

Define polynomials in Y by

    R_i(Y)=(E(F_i))(G(Y)) for i=1,2,3,
    R_4(Y)=(E(F_4)-1)(G(Y)).                           (5)

For every R_i, set to zero every coefficient of a monomial
Y1^a1 Y2^a2 Y3^a3 Y4^a4 with a1+a2+a3<k. These are exactly
the equations

    R_i in (Y1,Y2,Y3)^k for i=1,2,3,4.                 (6)

There is no bound on a4 in the meaning of normal order. There are
nevertheless only finitely many coefficients to test, since (5)
has total degree at most D(e+D-1). This bound also covers the
constant term -1, because e>=0 and D>=1. The inverse compositions
have degree at most D^2. The orbit compositions have tau-degree
at most D(N-1); when recording (4), the right side additionally
has degree one. Thus all equations are effectively finite.

Both inverse identities are retained. They prove that F is an
actual automorphism, not merely a constant-Jacobian map. Moreover,
(4) and their inverses give the scheme-theoretic equality

    I=(F1,F2,F3).                                     (7)

Indeed F composed with O is the standard closed line embedding.
Transport its kernel (Y1,Y2,Y3) under the ring isomorphism F*.
The inverse substitution G* therefore carries I^k precisely to
(Y1,Y2,Y3)^k. Conditions (5)--(6) are equivalent to

    E(F_i) in I^k for i<=3, E(F4)-1 in I^k.            (8)

No unbounded ideal-membership certificate is hidden in the encoding.
F4=s is NOT required. Only its value tau along the chosen orbit
and its order-k translation property are required.

## 4. Why a finite uniform degree exists at each order

Equations (3)--(6) define an affine witness scheme W(k,D) over T.
Its image C(k,D) is constructible by Chevalley's theorem, as in73.
Membership of a complex parameter point means exactly that a
complex inverse pair satisfying these equations exists. Padding
higher coefficients with zeros makes the images increasing in D.

Every complex point belongs to some C(k,D). The precise imported
premise is696 Sections2--3: near a slice orbit, invariant formal
parameters can be adjusted to preserve the ambient volume; their
order-k truncation, with s as the orbit parameter, extends to an
actual polynomial automorphism by Kaliman--Udumyan. The additive
group A4 meets their dimension and character hypotheses. Because
E preserves the orbit ideal, differentiating the lifted congruences
does not lower normal order. Both the map and its inverse have
some finite polynomial degree. [Kaliman--Udumyan, Theorem0.1,
Definition8.2 and Corollary8.6](https://arxiv.org/pdf/2008.02221).

The increasing constructible sets C(k,D) therefore cover T(C).
The exhaustion lemma in73 Sections2--3 gives a finite covering
level. Briefly, countably many proper closed subsets cannot cover
an irreducible complex variety. Some member of a constructible
cover is consequently dense and contains a dense open subset.
Dimension induction covers its closed complement, and the maximum
of finitely many resulting indices covers all components. Apply
this to the reduction of T if its scheme structure is nonreduced.

Define D_k=D(e,d,N,k) to be the least D>=1 covering T(C).
It exists. On an empty family take D_k=1. Larger k imposes
stronger conditions, so D_k is nondecreasing in k.

This is uniform existence at each fixed k, not one regularly
varying choice of F over T and not one coordinate map for all k.

## 5. Why the bound is computable in principle

For every proposed D form the first-order sentence

    forall coefficients(P,s), q:
      [(1) implies exists coefficients(F,G): (3)--(6)]. (9)

Here each displayed polynomial identity abbreviates its finite
coefficient equations, not another unbounded quantifier. Denominators
in (2) can be cleared over characteristic zero. Thus (9) is a
computably constructed sentence in the language of fields over Q.

ACF_0 decides (9). One may use effective quantifier elimination;
alternatively, enumerate formal proofs until a proof of (9) or
its negation appears. Recursive axiomatizability, completeness and
consistency ensure termination of the latter decision procedure.
[Marker, Lemma4.8 and Corollary4.9](https://homepages.math.uic.edu/~marker/orsay/orsay2.pdf).
For a constructive elimination treatment see [Pastuszak, Theorem3.2](https://arxiv.org/html/1607.05505).

Decide (9) successively for D=1,2,3,... and return the first true
level. Each individual decision terminates. Section4 proves that
a true level exists, so the entire search terminates and computes
the minimum D_k. This is a mathematical algorithm description,
not a claim that a quantifier-elimination program was run here.

No arbitrary complex coefficients have to be represented as
algorithm inputs. They are quantified variables in (9); the
actual inputs are the four integers e,d,N,k.

## 6. The growth condition is still the cancellation obligation

Fix (e,d,N). The following three statements are equivalent:

1. Every sliced action in this family has kernel C^[3].
2. The integer sequence D_k is bounded as k tends to infinity.
3. Some k>=2 satisfies k>e+D_k-1.

For 1 implies2, use the supplied-slice adapted variant of73
Section5. Pointwise polynomial kernels give exact inverse pairs
(a1,a2,a3,s); constructible exhaustion bounds both degrees by
one B uniformly in (E,s). At any q with s(q)=0 replace ai by
ai-ai(q). This is a constant translation of the first three
output coordinates, with the inverse translated in its inputs.
Neither degree increases. The resulting pair satisfies (3)--(8)
for every k and has the required orbit parameterization. Hence
D_k<=B uniformly in k, including all choices of q.

Boundedness gives3 by choosing k larger than e+B-1.
For 3 implies1 choose any action and an orbit through q on s=0.
The forward frame has degree at most D_k. Every residual in (8)
has original-coordinate total degree at most e+D_k-1 but lies
in I^k, which is contained in the kth power of the maximal ideal
at q. A nonzero polynomial of that degree cannot vanish to order
k>e+D_k-1. All residuals are zero. Since F has the actual inverse
G, E is exactly partial_F4 and its kernel is C[F1,F2,F3].

Consequently, if even one action in the family is a counterexample,

    D_k>=k-e+1 for every k>=2.                        (10)

If all kernels are polynomial, D_k eventually equals the least
UNIFORM exact inverse-pair degree with the SAME orbit normalization
as (3)--(4), allowing F4 to differ from s. For that minimum B_*,
D_k<=B_*; at k>e+B_*-1 every such jet witness is exact, so
B_*<=D_k as well. This statement does not require a single
frame to be chosen compatibly across parameters or orders.

It is important not to replace this B_* by the minimum for F4=s.
For E=partial_u on C[a,b,c,u] and supplied s=u+a^m, m>=2,
the translated standard frame at any q on s=0 has degree one,
including its inverse, and obeys (3)--(8) exactly. A frame whose
last component is the specified s has forward degree at least m.
Changing an exact frame to contain s can increase its degree.

## 7. What remains missing

The established statement is forall k there exists a computable
finite D_k. It is not that there exists a finite D working for
all k. Computability by itself proves neither boundedness nor
any inequality sufficient for the degree gate.

In particular, finitely many computed levels cannot establish
boundedness of the whole sequence without an additional theorem.
First-order compactness with arbitrarily many coefficient slots
does not turn an infinite formal series into a polynomial with
finite support. Prescribing compatible jets also does not force
bounded extension degrees, as696 Section3.2 already demonstrates.

The missing task is a bound that crosses k>e+D_k-1, or a
different global coordinate construction. This note supplies no
counterexample, no recognition of a previously unrecognized kernel,
and no claim of publication readiness. Internal AI reviews are
not proof-assistant verification or human expert review.
