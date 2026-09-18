# A linear second stage collapses without monicity assumptions

Private source-dependent proof, September 17, 2026. General cancellation
remains UNSOLVED. This strengthens the restricted presentation lemma626:
neither monicity of the first relation nor integrality of its residual
curve is required. It does not remove the linear second-stage hypothesis
or supply a global presentation for an arbitrary action. Novelty is UNKNOWN.

## 1. Statement

Let R=C^[3], let D be a nonzero locally nilpotent derivation, and
let A=ker(D)=C[a,b] be its actual embedded kernel. Suppose f is
irreducible nonconstant in A, Dr=f^2, and the following is an exact
presentation as an A-algebra:

    R=A[r,y,z]
     =A[T,Y,Z]/(fY-G(T), fZ-u(T)Y-K(T)),                 (1)

where G,u,K lie in A[T]. The displayed ideal is the full kernel,
without localization or an unmentioned saturation. There are no
degree, monicity, or residual irreducibility assumptions on G.

Then there exists W in R such that

    R=A[r,W].                                           (2)

Consequently rank(D)<=2, by the retained application of KVZ in621.
In particular no rank-three action has the presentation (1). If D
is additionally primitive with exact plinth f^2 A, rank(D)=2 and
f is an ambient coordinate by624. These extra assumptions are not
needed for (2).

## 2. The actual exceptional curve, including component selection

Set C=A/fA and S=C[T]/(Gbar). Factorial closure of A in R makes
f prime in R. Also A intersect fR=fA: if a=fh is invariant, then
0=D(a)=fD(h), so h belongs to A. Thus C embeds in R/fR, which
is a nonzero domain of dimension two.

The quotient map Spec(R)->Spec(A) has no surface fiber, by
Kaliman Lemma 2.1.[^kaliman] If a closed point of Spec(S) satisfied
ubar=Kbar=0, the exact equations (1) would allow y,z to vary
freely over one fixed point of Spec(A). This would give such a
surface fiber. The Nullstellensatz therefore yields

    (ubar,Kbar)S=S,
    R/fR=S[Y,Z]/(ubar Y+Kbar)=B[Z],  B=S_ubar.           (3)

For example, c ubar+d Kbar=1 gives ubar(c-dY)=1 in the middle
quotient, and conversely Y=-Kbar/ubar constructs its inverse.
The ring B is a domain because B[Z] is, but S need not be one.
The localization may discard an entire component of Spec(S).

Let Gamma=Spec(C), Z0=Spec(B), and E=Spec(R/fR)=Z0 x A1.
For each closed point of Gamma, the corresponding fiber of E
is the fiber of Z0 times A1. The preceding fiber-dimension bound
makes the map theta:Z0->Gamma quasi-finite. This also holds at
the generic point, or follows from the openness of the quasi-finite
locus and the Jacobson property. In particular Z0 is a curve.

## 3. Why theta is finite even when S is not finite

The following construction identifies the exact factor needed for
Kaliman's theorem; it does not infer properness from quasi-finiteness.

Zariski's Main Theorem factors the separated quasi-finite theta as
an open immersion Z0 into a curve Zbar finite over Gamma.[^zmt]
Replace Zbar by the reduced closure of Z0 if necessary. Then

    E=Z0 x A1  is open in  Zbar x P1.

Projection Zbar x P1->Zbar has connected fibers and pushforward
structure sheaf O_Zbar. Its composite with the finite map to Gamma
is proper, with precisely Zbar as Stein factor. Its restriction
to E has image Z0. This realizes theta itself in the construction
of Kaliman Lemma 2.2, without requiring that the original S be
finite or normal. Completing the base at infinity does not change
this construction above Gamma.

The local-slice theorem gives R_f=A_f[r], so the complement of E
is the required product over Spec(A) minus Gamma. Remove finitely
many base points to obtain smooth curves and an unramified map
on the remaining open set. Here E is already the product with A1.
The ambient X=Spec(R)=A3 is smooth and has H_3(X)=0. Thus the
notation and assumptions of Kaliman Proposition 3.2(i) hold for
this chosen factor, and theta is finite. Equivalently,

    B is a finite C-algebra.                            (4)

This is the sole finiteness conclusion imported from that result.

## 4. Finite flatness recovers a monic equation

The map A->R is flat. Indeed at a closed point of Spec(R) the
regular source has dimension three, the regular base has dimension
two, and the fiber has local dimension one. The upper bound follows
from Kaliman Lemma 2.1; the lower bound follows because the fiber
is cut out by two functions in a regular three-dimensional local
ring. Miracle flatness applies.[^flat] Flatness then holds at every
point, by localization (or the open flat locus for this finite-type
map). Empty fibers require no additional assumption.

Base change makes R/fR=B[Z] flat over C. Evaluation at Z=0
exhibits B as a C-module direct summand of B[Z], hence B is flat.
By (4) and noetherianness it is finite locally free. Since C is a
domain and C embeds in B, its constant rank is an integer d>=1.

Moreover S->B is surjective, even though it need not be injective.
To see this, the finite C-generating set for B also generates it
over S, so ubar^(-1) is integral over S. A monic equation for
this inverse, multiplied by ubar^(n-1), expresses ubar^(-1) as
the image of an element of S. Every element of S_ubar is then
in the image of S. This does NOT prove ubar is a unit of S.

Thus B is generated as a C-algebra by the image of T. Let G1bar
be the characteristic polynomial of multiplication by T on the
finite locally free C-module B. Characteristic polynomials on
local free charts agree, and Cayley-Hamilton holds after localization,
so globally G1bar is monic of degree d and G1bar(T)=0 in B.
There is a surjection

    C[T]/(G1bar) -> B.                                  (5)

Both sides are locally free of rank d. Localizing at each prime
makes the surjection a square surjective matrix over a local ring,
which is invertible. Hence (5) is an isomorphism. In particular
B is actually free with the monic power basis; freeness was not
assumed and no condition on higher D-image ideals was used.

Because Gbar vanishes in B, monic division gives

    Gbar=G1bar G2bar.                                   (6)

Also G1bar maps to zero in S_ubar, so ubar^N G1bar belongs to
(Gbar) in C[T] for some N>=0. Cancellation of the nonzero monic
G1bar in the domain C[T] gives

    ubar^N=G2bar h                                      (7)

for some h in C[T]. In B the element ubar is a unit. Equation
(7) makes G2bar, and therefore ubar G2bar, a unit of B as well.

## 5. Polynomial elimination inside the actual ring

Lift G1bar to a monic G1 in A[T], lift G2bar to G2, and write

    G=G1 G2+fJ.

Since G1(r) vanishes in R/fR, the actual element

    y1=G1(r)/f

belongs to R. Cancelling f in the original first relation yields

    y=G2(r)y1+J(r),   R=A[r,y1,z].                     (8)

Put U=uG2 and K1=uJ+K. The exact identities in R are

    fy1=G1(r),    fz=U(r)y1+K1(r).                     (9)

No new unsaturated quotient presentation is presumed here. The
unit of B=C[T]/G1bar supplies v,alpha,beta in A[T] such that

    vU+f alpha+G1 beta=1.

With all coefficients evaluated at r, set

    W=vz+alpha y1+beta y1^2.                            (10)

The same direct calculation as626 gives

    fW=y1+vK1,
    y1=fW-vK1,
    z=UW+alpha K1+beta y1 K1.                          (11)

These are polynomial identities in the actual R. Equations
(8) and (11) prove R=A[r,W]. They also give

    f^2 W=G1(r)+f v(r)K1(r).

The one-generator rank obstruction621 now applies with the actual
kernel and local slice, and proves rank(D)<=2. Its source is KVZ
Theorems 3.21 and 4.23, with the relative quotient calculation
in proof 4.26, not an unproved general embedding assertion.[^kvz]

## 6. A polynomial control where a component really disappears

The distinction between S and B is essential. Take A=C[x,b],
f=x and

    R=A[r,y,z]/(xy-r(r-1), xz-ry-1).

Define the entire elements

    k=z(r-1)-y^2,    w=z-2k^2-xk^3.

The relations give xk=r-1, y=rk, and xw=k+1. The full inverse is

    k=-1+xw,    r=1+xk,    y=rk,
    z=w+2k^2+xk^3.

These formulas verify R=C[x,b,w]. With D=partial_w its actual
kernel is A and Dr=x^2. However

    S=C[b,T]/(T(T-1)),   ubar=T,
    B=S_T=C[b],          G1bar=T-1,  G2bar=T.

The element T is not a unit of S. The selected component makes
T a unit in B, precisely as the proof requires. Here the action
has unit plinth, so this is a proof control, not a primitive
prime-square-plinth or rank-three example.

## 7. Scope and verification

General proposed the component-selection and characteristic-polynomial
argument. Root and Jet separately reconstructed the finite-factor
application using Zariski Main and the exact product compactification.
Jet independently checked the finite-flat and direct elimination
steps. Root read the cited primary statements and complete proof
of Kaliman Proposition 3.2(i), plus the entire saved621 and626.

Fresh unsaved algebra checks the universal unit-center identities;
the proof above, not any bounded symbolic test, establishes the
claim for every G,u,K. General also checked both complete inverse
directions of the control in Section 6. A full independent review
of this saved file is required before canonical acceptance.

The genuinely nonlinear H(T,Y) case is still outside this result.
A monic H makes R a finite normalization of A[r,z], but need not
give equality with that subring, as the published control in622 shows.
An arbitrary global presentation, arbitrary modification recognition,
and the four-variable entry to cancellation remain unresolved.
No frozen checker was executed, imported, compiled, or modified.
No human expert review, Lean certification, or novelty clearance
has occurred. This note is not a solution of cancellation.

[^kaliman]: S. Kaliman, [*Free C+-actions on C3 are translations*](https://www.math.miami.edu/~kaliman/library/Ka.invent.2004.c%2B.pdf), Lemmas 2.1--2.2, Notation 2.3, and Proposition 3.2(i). The chosen curve factor and its compactification are identified in Section 3.

[^zmt]: [Stacks Project, Section 37.43, Lemma 37.43.3](https://stacks.math.columbia.edu/tag/02LQ), the separated quasi-finite form of Zariski's Main Theorem.

[^flat]: [Stacks Project, Lemma 10.128.1, tag 00R4](https://stacks.math.columbia.edu/tag/00R4), miracle flatness. Its dimension equality is checked in Section 4.

[^kvz]: S. Kaliman, S. Venereau and M. Zaidenberg, [*Simple birational extensions of the polynomial ring C^[3]*](https://arxiv.org/pdf/math/0104204), Theorems 3.21 and 4.23, proof 4.26. See [621](global-one-generator-rank-obstruction-pass621-working.md) for the actual embedded-kernel coordinate deduction.
