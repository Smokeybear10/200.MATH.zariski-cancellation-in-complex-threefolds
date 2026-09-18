# A monic first stage and linear last stage collapse globally

Private source-dependent proof. General cancellation remains UNSOLVED.
This note excludes a specified global two-stage presentation for rank-three
actions. It does not assert that every action has this presentation, that
every intermediate ring is polynomial, or that a singular cylinder can
be rectified by an ambient automorphism. Novelty is not established.

## 1. Exact hypothesis and conclusion

Work over C. Let R=C^[3], let D be a nonzero LND, and let
A=ker(D)=C[a,b] be its actual embedded kernel. Suppose there are
elements r,y,z of R and an irreducible nonconstant f in A with

    Dr=f^2,
    R = A[r,y,z]
      = A[T,Y,Z]/(fY-G(T), fZ-u(T)Y-K(T))                 (1)

as A-algebras, with T,Y,Z mapping to r,y,z. Here G,u,K belong
to A[T], G is monic of positive degree, and the displayed ideal
is the full defining ideal, not an ideal to be saturated later.
Assume also that

    S = (A/fA)[T]/(Gbar(T))                              (2)

is an integral domain. For example, irreducibility of Gbar over
Frac(A/fA) suffices because Gbar is monic. Irreducibility merely
as an element of the possibly nonnormal ring (A/fA)[T] is not
used as a substitute for the domain assumption.

Then ubar is a unit of S. There are v,alpha,beta in A[T] with

    vu+f alpha+G beta=1.                                (3)

The explicit element

    W=v(r)z+alpha(r)y+beta(r)y^2                         (4)

gives R=A[r,W]. Consequently rank(D)<=2.

If D is additionally primitive with exact plinth f^2 A, its rank
is exactly two and f is a coordinate of R. In particular there
is no primitive rank-three example satisfying all these premises.

## 2. The first exceptional curve cannot have a deleted point

Factorial closure of A in R makes f prime in R, so E=Spec(R/fR)
is a nonempty integral surface. Put Gamma=Spec(A/fA). The quotient
pi:Spec(R)->Spec(A) has no two-dimensional fiber. This is the
polynomial-threefold instance of Kaliman's Lemma 2.1.[^kaliman]

The elements ubar and Kbar generate the unit ideal of S. Indeed,
if they vanished at a closed point of Spec(S), that point would
give values (a0,b0,r0) satisfying f=G=u=K=0. In the presentation
(1), y and z could then take arbitrary independent values.
This would put a closed affine plane in pi^(-1)(a0,b0), contrary
to the fiber-dimension statement. The Nullstellensatz proves

    (ubar,Kbar)S=S.                                     (5)

Reducing (1) modulo f and using (5) now gives exactly

    R/fR = S[Y,Z]/(ubar Y+Kbar) = S_ubar[Z].             (6)

For example, if c ubar+d Kbar=1 in S, then ubar(c-dY)=1
in the quotient, proving that no further localization is being
silently imposed in (6). Conversely Y=-Kbar/ubar in S_ubar.
This also shows ubar is nonzero, since E is nonempty.

Monicity makes Spec(S)->Gamma finite. The map

    theta: Z0=Spec(S_ubar) -> Gamma                     (7)

is therefore quasi-finite. Projection onto the first factor in
E=Z0 x A1 gives a surjective kappa with pi|E=theta composed
with kappa. Away from Gamma, (1), or the local slice theorem,
gives R_f=A_f[r]. Thus the complement is the required A1-product.

This is a legitimate factorization for Kaliman's Proposition 3.2(i),
not a conclusion drawn from an arbitrary normalization. To see it
directly in the construction of his Lemma 2.2, use the proper
extension Spec(S) x P1 -> Gamma. Its projection to Spec(S)
has connected P1 fibers and pushforward of the structure sheaf
equal to O_S; the next map is finite. The image of E in this
Stein curve is exactly Z0. One may complete the base curves at
infinity without changing this factorization above Gamma.

For the remaining notation in that proposition, remove finitely
many points of Gamma to make both curves smooth and the finite
curve map unramified there. This is possible in characteristic
zero. The product description (6) holds over that open set.
The ambient X=Spec(R)=A3 is smooth and H_3(X)=0. All hypotheses
of Proposition 3.2(i) are satisfied, so theta is FINITE.

Hence S_ubar is finite over A/fA, and therefore finite over S.
In particular 1/ubar is integral over S. An integral inverse
already lies in S: multiplying a monic equation of degree n for
1/ubar by ubar^(n-1) explicitly expresses 1/ubar as an element
of S. Thus ubar is a unit of S, as asserted.

No normality of S or E was needed. The crucial global restriction
was finiteness of (7), which forbids deleting part of the finite
first-stage curve. Smoothness of an unrelated ambient threefold
alone would not justify that restriction.

## 3. Exact polynomial collapse

Lift the inverse of ubar in S to v in A[T]. This gives (3) for
some alpha,beta in A[T]. Define W by (4). All coefficients below
are evaluated at r. The defining relations give

    fW = v(uy+K)+f alpha y+beta(fy)y
       = (vu+f alpha+G beta)y+vK
       = y+vK.                                         (8)

Consequently

    y=fW-vK,
    z=uW+alpha K+beta yK.                               (9)

For the second identity, multiply (4) by u and add alpha K+
beta yK; its value becomes (uv+f alpha+beta fy)z=z.
Equations (9) are polynomial formulas, so R=A[r,W] globally.
In particular

    f^2 W=G(r)+f v(r)K(r).                              (10)

There is also an exact one-relation presentation

    R = A[T,W]/(f^2 W-G(T)-f v(T)K(T)).                 (11)

To check exactness, r is transcendental over A because Dr=f^2
is nonzero. The surjection in (11) therefore has a height-one
prime kernel. Its displayed linear polynomial in W is primitive
and irreducible: f does not divide G, since G is monic. Gauss's
lemma and the height count identify the full kernel. This step
does not replace a nonnormal subring by its normalization.

## 4. Where the polynomial ambient hypothesis enters

The already retained [one-generator obstruction621](global-one-generator-rank-obstruction-pass621-working.md)
applies to R=A[r,W] with this actual local slice. It uses KVZ
Theorem 3.21 and Theorem 4.23, including the relative quotient
calculation in proof 4.26.[^kvz] These results supply an actual
ambient coordinate in A, not merely an abstract polynomial-ring
isomorphism. Therefore rank(D)<=2.

For the stated primitive exact-plinth case, rank one would force
a slice and unit plinth. Thus the rank is two. The rank criterion
and coordinate transfer in [624](single-prime-plinth-normality-rank-gate-pass624-working.md)
then make the sole plinth prime f itself an ambient coordinate.

The finite-factor argument and the polynomial-recognition argument
have separate roles. In particular, the first does not claim to
recognize arbitrary smooth contractible threefolds as A3. The known
Koras-Russell control625 has a one-stage presentation and is not
polynomial; KVZ cannot be applied to that nonpolynomial input.

## 5. Boundary of the result

The theorem leaves the following cases untouched:

- A genuinely nonlinear second-stage polynomial H(T,Y).
- A first relation not monic, or whose residual curve is not integral.
- Presentations valid only after localization or saturation.
- General modifications or arbitrary slice actions on A4.

Monicity of nonlinear H cannot simply replace the linear hypothesis.
If H has Y-degree m and is monic, eliminating y instead gives
the subring A[r,z] with relation

    f^(m+1)z=f^m H(r,G(r)/f).                           (12)

The original R is integral over this subring, not automatically
equal to it. The published example retained in622 has

    A=C[x,s], f=x, G=r^2-s, H=r+y^2,
    x^3 z=x^2 r+(r^2-s)^2.

Its actual R=C[x,y,z] is the normalization of A[r,z], while
the latter has a nonreduced quotient modulo x. Thus applying
KVZ to that intermediate ring as if it were polynomial is
invalid. The linear collapse above avoids this exact problem.

This is a source-dependent restriction on a proposed presentation,
not a classification of rank-three actions. The search for a
general coordinate construction must still handle genuinely
nonlinear centers or different global presentations.

## 6. Check and provenance boundary

General and Geometry independently reconstructed the finite-factor
application and the unit-to-generator argument before this note was
written. Root freshly checked the universal polynomial identities
(8)--(10) modulo exactly the two defining relations and (3), using
unsaved exact algebra. No finite computation proves the imported
topological or polynomial-recognition theorem.

The note extends the global-generator boundary of621 and the
terminal-denominator boundary of622. It does not repackage the
already retained full relative-isomorphism classification19 as a
new result. A complete saved-source review is required before
canonical acceptance. No frozen checker was executed, imported or
compiled. No expert review, formal certification or novelty claim
has occurred.

[^kaliman]: Shulim Kaliman, [*Free C+-actions on C3 are translations*, final author version](https://www.math.miami.edu/~kaliman/library/Ka.invent.2004.c%2B.pdf), Lemmas 2.1--2.2, Notation 2.3, and Proposition 3.2(i). The actual curve factorization and its proper completion are identified above; the proof does not infer finiteness from quasi-finiteness alone.

[^kvz]: Shulim Kaliman, Stephane Venereau and Mikhail Zaidenberg, [*Simple birational extensions of the polynomial ring C^[3]*](https://arxiv.org/pdf/math/0104204), Theorem 3.21, Theorem 4.23 and proof 4.26. The exact one-generator/rank deduction, including the retained kernel coordinate, is written in621.
