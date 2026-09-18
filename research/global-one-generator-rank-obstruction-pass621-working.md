# A global one-generator reconstruction excludes rank three

Status: source-dependent corollary, written September 17, 2026.
This is an application of published Kaliman--Venereau--Zaidenberg
results, not a claim of a new primary theorem or a solution of
cancellation. No primitivity, minimality or plinth-multiplicity
hypothesis is needed for the main statement.

## 1. Statement and its role

Let k be the complex numbers, R=k^[3], D a nonzero locally
nilpotent derivation, and A=ker(D), the actual embedded invariant
ring. Then A is isomorphic to k^[2]. Let r in R be a local slice,
so c=D(r) is a nonzero element of A.

**Proposition.** If some q in R satisfies

    R = A[r,q],

then A contains an actual coordinate of R. Consequently rank(D)<=2.

Equivalently, a rank-three action cannot reconstruct its whole
polynomial three-ring from its full kernel, one local slice, and
only one additional element. This does not bound the number of
generators needed after invariant localization, or apply to an
arbitrary two-element generating set not containing a local slice.

For the current research route, a global presentation

    R = A[T,Y]/(pY-G(T)),

with the given copy of A fixed by D, would already be outside the
rank-three frontier. A presentation of this type on a localized
open set is not excluded. The distinction prevents replacing the
missing globalization argument by an assumed normal form.

## 2. Exact presentation from the generating assumption

The local-slice theorem gives R_c=A_c[r]. It follows directly by
applying the slice theorem to D/c and its slice r after inverting c.
The kernel of that localized derivation is A_c. In particular r is
transcendental over A.

Express q as G(r)/c^N, with G in A[T]. Cancel the common polynomial
factors of c^N and G in the UFD A[T]. This gives

    q = b(r)/a,
    0 != a in A, a divides c^N, b in A[T], gcd(a,b)=1.

The zero-polynomial case causes no difficulty: if q=0, take a=1
and b=0. Consider the surjective map

    phi: A[T,Y] -> R,  T |-> r, Y |-> q.

Its kernel is prime of height one, since the source and target
have complex dimensions four and three. The polynomial

    P = aY-b(T)

belongs to this kernel. It is primitive as a polynomial in Y over
A[T] and is irreducible over Frac(A[T]), since its Y-degree is one.
Gauss's lemma therefore makes it irreducible in the UFD A[T,Y].
Its principal ideal is a height-one prime. Containment in ker(phi)
and equality of heights now imply

    ker(phi)=(P),  R = A[T,Y]/(P).

These are identities of A-algebras, with the original A embedded.
No additional saturation, missing relation, or torsion component
is discarded. If a is a unit, this already gives R=A[r], and any
coordinate of A is a coordinate of R.

## 3. The published recognition step

Choose coordinates s,t of A. The polynomial P has precisely the
form a(s,t)Y-b(s,t,T). Its zero fiber is the actual polynomial
threefold R. KVZ Theorem 3.21(i)=>(v) supplies a coordinate change
of the base plane k[s,t], with a new coordinate x, such that P is
a residual x-variable. In particular it is a residual x-plane.
KVZ Theorem 4.23, specifically its quotient calculation in proof
4.26, yields

    R is isomorphic to k[x]^[2] as a k[x]-algebra.

The isomorphism fixes the actual embedded element x in ker(D).
Thus x completes to coordinates of R and rank(D)<=2, as asserted.

The k[x]-linearity is essential. An abstract isomorphism R=k^[3]
alone is already an input and would establish nothing about x.
The proof also does not infer coordinatehood just from the phrase
"all closed fibers are planes." It uses the explicit relative
conclusion of KVZ for this particular polynomial form.

Primary source: S. Kaliman, S. Venereau and M. Zaidenberg,
[*Simple birational extensions of the polynomial ring C^[3]*](https://arxiv.org/pdf/math/0104204),
arXiv:math/0104204v2. The base-coordinate convention and Theorem
3.21 are on printed pages 36--37. Definitions 4.19--4.21 and
Theorem 4.23 are on page 44; proof 4.26 and its relative quotient
calculation are on page 46. The proof does not assert that P is
an ambient coordinate in four variables.

The local-slice and polynomial-kernel facts are also recorded in
[Dasgupta--Gaifullin, Proposition 2.6 and Theorem 2.8](https://arxiv.org/html/2306.00510v2#S2).
Their Definition 2.9 gives the rank convention used here.

## 4. Consequences and exclusions

The proposition applies to every local slice of a rank-three D,
not only a minimal one. Multiplying D by a nonzero invariant does
not change the assertion: its kernel and rank remain unchanged.

It does not say that all rank-two actions have such a presentation.
It does not say that two additional generators suffice for every
rank-three action. It does not rule out finite covers by open sets
where different extra generators give simple presentations.

In the current doubled-plinth investigation, Masuda's one-stage
localized description cannot simply be promoted to a global
one-stage polynomial presentation while retaining the same full
kernel and a rank-three action. Possible next routes still include
genuine multi-stage structure and recognition using a different
action. Their existence or success is not proved here.

The result is not itself a recognition theorem for the stably
polynomial modification M=R[r/(1+rho Q)]. It identifies a proposed
extra hypothesis under which the difficult rank-three input would
not exist. Neither general cancellation nor arbitrary four-variable
entry has been resolved.

## 5. Evidence and deduplication boundary

Root read the current README and latest ledger, the complete
two-linear-literature-audit.md, and the relevant KVZ statements
directly before writing. Root source reads turn5174view0 and
turn5173view1 include the exact implication and relative quotient;
turn5174view1 contains the residual-plane and stable-equivalence
definitions. Local-slice and rank definitions were checked in
turn5176view2. No saved checker was executed, imported or compiled.

General and Jet separately reconstructed the mathematical argument
and checked the original theorem hypotheses before this file was
written. A separate saved-source review is still required before
this file is accepted in the canonical ledger.

The archive already uses KVZ in two-linear-literature-audit.md,
central-arrangement-slice-pass.md, and repeated-crossing-slice-descent.md.
The focused search did not locate this exact generator/rank
corollary, but that is not a literature novelty audit. Its status
is a source-dependent obstruction, not a newly discovered theorem.
No human expert review or formal proof certification has occurred.
