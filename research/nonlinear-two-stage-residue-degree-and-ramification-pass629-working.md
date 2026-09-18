# Residual degree and ramification in a global nonlinear two-stage presentation

Private source-dependent note, September 17, 2026. General cancellation
remains UNSOLVED. The conclusions concern the exact presentation below,
not every rank-three action or every localized two-stage construction.
The control family is published. Novelty of the deductions is UNKNOWN.

## 1. Hypotheses and conclusions

Work over k=C. Let R=k^[3], let D be a nonzero locally nilpotent
derivation, and let A=ker(D)=k[a,b] be its actual embedded kernel.
Let f be irreducible and nonconstant in A. Suppose Dr=f^2 and
there is an exact A-algebra presentation

    R = A[r,y,z]
      = A[T,Y,Z]/(fY-G(T), fZ-H(T,Y)),                  (1)

where G belongs to A[T] and H to A[T,Y]. The displayed ideal is
the entire defining ideal. No subsequent saturation is permitted.
Neither primitivity of D nor exact equality pl(D)=f^2 A is assumed.
Set

    C=A/fA,
    B=C[T,Y]/(Gbar(T),Hbar(T,Y)).                       (2)

Bars denote reduction modulo f, followed by passage to B when needed.
Then B is an integral affine curve algebra, C injects into B, and

    R/fR=B[z].                                         (3)

The following statements hold.

1. B is finite locally free over C. No normality of either curve is
   asserted.
2. The induced derivation on (3) and the Kähler different are

       Dbar=q partial_z,  q=Gbar_T Hbar_Y != 0,
       Fitt_0^B(Omega_(B/C))=qB.                       (4)

   Consequently D is primitive, and its fixed subscheme on (3) is
   Spec(B/qB) x A1. This does not assert that q is a unit.
3. Suppose additionally that G is monic of positive degree and

       S=C[T]/(Gbar(T))                                (5)

   is a domain. Write h(Y) for the image of H in S[Y]. Its degree
   m is positive and its leading coefficient is a unit of S. Then

       m=[Frac(B):Frac(S)],
       R=A[r,W] for some W in R  if and only if  m=1.   (6)

The same actual r occurs on both sides of (6). The field statement
that rbar generates Frac(B) over Frac(C) is different from
primitivity of D, meaning that its ambient polynomial coefficients
have no nonunit common factor. The latter already follows from (1).

There are published actual polynomial examples with exact plinth
f^2 A and arbitrarily large m. Thus the exponent two does not bound
this residual extension degree or force the collapse in (6).

## 2. Why this particular residual curve is finite and flat

Factorial closure makes f prime in R. Also A intersect fR=fA:
if a=fh is invariant, then 0=D(a)=fD(h), so h belongs to A.
These observations prove the domain and injection claims in (2).
Equation (3) follows by reducing the full presentation, and dimension
gives dim(B)=1. Put X=Spec(R), Gamma=Spec(C), and Z0=Spec(B).

Let pi:X->Spec(A) be the actual quotient. Its nonempty fibers have
pure dimension one. In particular no fiber contains a surface;
this is the polynomial-threefold case of Kaliman's Lemma 2.1.
The quotient is also faithfully flat, as recorded in the polynomial
three-ring plinth theorem.[^dg] The factorization on E=Spec(R/fR) is

    E=Z0 x A1 -> Z0 --theta--> Gamma.                  (7)

Every closed fiber of theta has dimension zero, since adjoining the
free variable z raises its dimension by one and gives the corresponding
fiber of pi. Thus theta is quasi-finite and separated.

Apply Zariski's Main Theorem to theta.[^zmt] It realizes Z0 as an
open subscheme of a finite Gamma-scheme. Replace the latter by the
reduced closure of Z0, obtaining an integral curve S0 finite over
Gamma. The proper extension

    S0 x P1 -> S0 -> Gamma                              (8)

is a legitimate compactification for Kaliman's Lemma 2.2: its
first map has connected fibers and pushes its structure sheaf to
O_(S0), and its second map is finite. The image of E in its Stein
curve is exactly Z0, not an arbitrarily substituted normalization.
Completing at infinity does not change this factorization over Gamma.

Off Gamma, the local-slice theorem gives R_f=A_f[r]. After removing
finitely many points of Gamma, the curves in (8) are smooth and the
finite curve map is unramified. Such a removal is possible in
characteristic zero; the cylinder (7) already holds everywhere.
Thus the factor is precisely of the type in Kaliman's Notation 2.3.
Since X=A3 is smooth and H_3(X)=0, his Proposition 3.2(i) proves
that theta is finite.[^kaliman] This proves finiteness of B over C.
Quasi-finiteness alone was not used as finiteness.

Flatness is inherited from the original quotient, not deduced by
applying miracle flatness to the possibly singular curve C. One
can obtain flatness of A->R from the regular base, Cohen-Macaulay
source and pure one-dimensional fibers by miracle flatness; it is
also the faithful-flatness assertion cited above.[^flat] Base change
gives the flat C-module R/fR=B[z]. Evaluation at z=0 splits the
inclusion B->B[z] as C-modules. Hence B is C-flat. Since C is
Noetherian and B finite over C, B is finite locally free.[^flat]

This extends the chosen-factor argument in
[626](monic-linear-two-stage-rank-obstruction-pass626-working.md)
and the separately reviewed linear strengthening
[628](general-linear-two-stage-rank-obstruction-pass628-working.md).
The argument has been given here in full; no unreviewed strengthening
or normality of an intermediate curve is an input.

## 3. The residual derivation is the different coefficient

Differentiate both whole relations (1), using D(A)=0 and Dr=f^2.
Since R is a domain, cancellation of f gives

    Dy=f G_T(r),
    Dz=f H_T(r,y)+G_T(r)H_Y(r,y).                      (9)

Modulo f, D kills the images of A,r,y. Therefore its full restriction
to B[z] is q partial_z with q as in (4).

The relative differential module of (2) has the presentation with
generators dT,dY and relation matrix

    [ Gbar_T       0       ]
    [ Hbar_T       Hbar_Y   ].                         (10)

Its zeroth Fitting ideal is the determinant ideal qB. This is the
Kähler different, and its vanishing set is the locus where Z0->Gamma
is not unramified.[^different] No identification with an alternative
notion of different is required.

Let K=Frac(C) and L=Frac(B). Since B is a finite C-domain, localizing
at C minus zero gives the field L, a finite extension of K. It is
separable in characteristic zero. Hence Omega_(B/C) tensor_B L=0.
The square matrix (10) is then surjective over L, so its determinant
is nonzero. This proves q!=0 without a primitivity assumption.

It follows coefficientwise that ker(Dbar)=B. The ideal generated
by the images of D on B[z] is exactly qB[z]. Thus the scheme-theoretic
intersection of the fixed locus of D with E is Spec(B/qB) x A1,
including any multiplicities in q.

Finally, if an irreducible polynomial divided every ambient
coefficient of D on R=k[X1,X2,X3], it would divide every D(h),
and in particular Dr=f^2. It would therefore be associated to f.
But q!=0 shows that f does not divide Dz. This proves automatic
primitivity. It does not prove that r is a minimal local slice;
the exact plinth might be a proper divisor of f^2 A.

## 4. The same-r one-generator criterion

Assume now the extra hypotheses (5). The natural map S->B is
injective. Indeed its kernel contracts to zero in C. Localizing at
C minus zero turns the finite domain S into a field, and the kernel
then becomes a proper ideal of that field. It is zero there and
therefore zero in S. This is also the usual incomparability argument.

Since B is finite over C, it is finite over S. We have B=S[Y]/(h).
The polynomial h cannot be zero, since S[Y] is not finite over S.
It cannot be a nonzero constant, since S->B is injective, nor a
unit, since B is nonzero. Thus m=deg_Y(h)>=1.

The image of Y is integral over S, so the ideal (h) in S[Y] contains
a monic polynomial P(Y). Write P=hJ. As S is a domain, the leading
coefficients multiply to one. Therefore the leading coefficient
of h is a unit. Dividing by that unit makes h monic, without changing
its ideal. Polynomial division gives a free S-basis

    1, Y, ..., Y^(m-1)                                 (11)

of B. After passage to Frac(S), the quotient is a finite domain over
a field, hence a field. Its dimension is m. This proves the degree
formula in (6), without replacing B by a normalization.

Suppose first that R=A[r,W]. Reduction and localization give

    B[z]=S[Wbar],
    Frac(B)[z]=Frac(S)[Wbar].                          (12)

The element Wbar must be transcendental over Frac(S), because the
left side has transcendence degree one over this field. A field is
relatively algebraically closed in its rational function field in
one variable. But Frac(B) is a finite algebraic extension of Frac(S)
inside that field by (12). Hence the extension is trivial and m=1.
This is the constant-field obstruction already used in the m=n=2
control of [622](global-triangular-presentation-cylinder-obstruction-pass622-working.md).

Conversely, if m=1 then h=ubar Y+Kbar with ubar a unit of S.
Lift ubar,Kbar to u,K in A[T]. There exist P,Q in A[T,Y] such that

    H=uY+K+fQ+GP.                                     (13)

Replace the last presentation generator by

    z1=z-Q(r,y)-yP(r,y).                              (14)

The inverse substitution is polynomial. Since fy=G(r), the exact
new presentation is

    R=A[T,Y,Z1]/(fY-G(T), fZ1-u(T)Y-K(T)).             (15)

This is a change of the polynomial presentation before quotienting.
It does not claim that r,y,z are an ambient coordinate system.

Lift the inverse of ubar in S to v in A[T], and choose alpha,beta
in A[T] with vu+f alpha+G beta=1. With all coefficients evaluated
at r, set

    W=v z1+alpha y+beta y^2.                           (16)

The complete polynomial identities are

    fW=y+vK,
    y=fW-vK,
    z1=uW+alpha K+beta yK,
    f^2 W=G+fvK.                                      (17)

They follow from exactly the two relations (15) and the displayed
Bezout identity. Equations (14) and (17) put y,z in A[r,W], proving
R=A[r,W]. This completes both directions of (6).

The retained one-generator result
[621](global-one-generator-rank-obstruction-pass621-working.md)
then gives rank(D)<=2 when m=1. Its polynomial-ambient recognition
input is separate from the finite-curve argument. No rank bound
for m>=2 has been established here.

## 5. Published polynomial controls with unbounded residual degree

Fix arbitrary integers m,n>=2 and take the actual polynomial ring
R=k[x,y,z]. Define

    r=xz-y^m,  s=r^n-xy,
    Dx=0,
    Dy=nx r^(n-1),
    Dz=x+mn y^(m-1)r^(n-1).                           (18)

This is the specialization r1=r2=x, h1(T)=T^m, h2(T)=T^n of
Dasgupta--Gaifullin Example 4.14, not a new family. Their invariant
in that example has the opposite sign to our s. The hypotheses on
the common nonconstant divisor and the degrees of h1,h2 hold for
every pair m,n>=2. Their Example 4.15, retained in622, is m=n=2.
The following whole-ring checks also prove the facts needed here.

Direct differentiation gives Dr=x^2 and Ds=0. There is an exact
localization with both inverse formulas

    R_x=k[x,x^(-1),s,r],
    y=(r^n-s)/x,  z=(r+y^m)/x,
    r=xz-y^m,  s=r^n-xy.                              (19)

On this ring D=x^2 partial_r. The polynomial formulas (18) preserve
R, so their local nilpotence on R_x proves local nilpotence on R.
In fact the exact D-degrees of y and z are n and mn, respectively,
by (19). No check at finitely many exponents replaces this argument.

Let A0=k[x,s]. The reduction A0/xA0 -> R/xR sends

    s -> (-1)^n y^(mn)                                (20)

and is injective. Hence A0 intersect xR=xA0. Successive cancellation
of x proves (A0)_x intersect R=A0. Equation (19) now gives the exact
kernel A=ker(D)=A0, not just an exhibited invariant subring.

The coefficients in (18) have gcd one. Indeed any common irreducible
factor must divide x or r from Dy; r=xz-y^m is irreducible. Modulo x,
Dz becomes mn(-1)^(n-1)y^(mn-1), which is nonzero. Modulo r, Dz=x,
and r does not divide x. Thus D is primitive.

The polynomial-three-ring plinth theorem makes pl(D) principal.[^dg]
Its generator divides Dr=x^2, so, up to a scalar, it is 1, x or x^2.
If it were 1 or x, choose h with Dh=1 or Dh=x. Then r-x^2h or
r-xh, respectively, would be invariant. Reduction modulo x would
put -y^m in the image k[y^(mn)] of A/xA, impossible since n>=2.
Consequently

    pl(D)=x^2 A.                                      (21)

The exact global presentation is

    R=k[x,s,T,Y,Z]/(xY-T^n+s, xZ-T-Y^m).              (22)

It is verified in both directions simply by eliminating T=xZ-Y^m
and s=T^n-xY. Thus f=x, G=T^n-s, H=T+Y^m. Its curve algebras are

    C=k[s],
    S=C[T]/(T^n-s)=k[T],
    B=C[T,Y]/(T^n-s,T+Y^m)=k[Y].                      (23)

The maps are T->-Y^m and s->(-1)^nY^(mn). Hence B is free of
rank m over S and rank mn over C. In particular its residual
degree m can be arbitrarily large, even though both residual curves
are smooth and D is primitive with the exact square plinth (21).
Equation (6) excludes R=A[r,W] for every such pair, for this same r.

The full residual coefficient and different are

    q=mn(-1)^(n-1)Y^(mn-1),
    Fitt_0(Omega_(B/C))=(Y^(mn-1)).                    (24)

This agrees with differentiating s=(-1)^nY^(mn), up to a nonzero
scalar. The fixed subscheme on x=0 is its product with the z-line.
The action has rank two: x is an ambient invariant coordinate, while
primitivity and the nonunit plinth exclude rank one.

## 6. Scope, deduplication, and checking

The cylinder consequence of an exact final denominator and the
m=n=2 fixed-r obstruction were already retained in622. The warning
that finite residual data do not control a chosen primitive element
also appears in [pass47](image-ideal-source-scope-pass47.md). This
note records the degree-one equivalence under (5), the exact different
coefficient, and the uniform consequences of the published family.
It does not present that family or the earlier constant-field idea
as a discovery.

For m>=2 the remaining obstruction is concrete: rbar does not
generate the residual function field, so one generator cannot
reconstruct R over this A[r]. Neither finite flatness, normality of
B, nor Dr=f^2 removes it. The controls are rank two with a smooth
plinth curve. They are not rank-three or cuspidal-plinth examples.

Without (5), no field-degree criterion for the first-stage algebra
is asserted. Even with (5), nothing here rectifies an abstract
cylinder by an ambient automorphism, proves an intermediate ring
polynomial, or allows application of one-stage recognition to an
unproved normalization. Changing r or using another action is not
excluded. General cancellation and the arbitrary nonlinear
rank-three frontier remain unresolved.

The primary statements used above were read directly, including
Kaliman's complete finiteness proof, DG Example 4.14 and its displayed
derivation, DG Theorem 2.10, and the cited Stacks statements. Fresh
unsaved exact algebra in08d555 checked the universal generator-change
and collapse identities, and both full localization inverse orders,
gcd and residual formulas for (m,n)=(2,2),(3,2),(2,4),(4,3),(5,2).
The uniform arguments above, not those samples, prove the all-degree
claims. No saved checker was executed, imported or compiled.
A complete independent saved-source review is required before
canonical acceptance. No expert or formal-proof certification has
occurred, and no novelty claim is made.

[^kaliman]: Shulim Kaliman, [*Free C+-actions on C3 are translations*, final author version](https://www.math.miami.edu/~kaliman/library/Ka.invent.2004.c%2B.pdf), Lemmas 2.1--2.2, Notation 2.3, and Proposition 3.2(i). The chosen Stein factor and its image are identified in (7)--(8).

[^zmt]: [Stacks Project, Lemma 37.43.3, tag05K0](https://stacks.math.columbia.edu/tag/05K0), the quasi-finite separated form of Zariski's Main Theorem.

[^flat]: [Stacks Project, Lemma 10.128.1, tag00R4](https://stacks.math.columbia.edu/tag/00R4), miracle flatness over a regular local base; [Lemma 10.78.2, tag00NX](https://stacks.math.columbia.edu/tag/00NX), finite-presentation/flatness and finite-local-freeness equivalence. The regular base is A, not C.

[^different]: [Stacks Project, Section 49.7, tag0BVV](https://stacks.math.columbia.edu/tag/0BVV), Definition 49.7.1 and Lemmas 49.7.3--49.7.4. The calculation uses the full two-equation presentation, not a reduced-support approximation.

[^dg]: Nikhilesh Dasgupta and Sergey Gaifullin, [*On locally nilpotent derivations of polynomial algebra in three variables*, arXiv2306.00510v2](https://arxiv.org/html/2306.00510v2), Theorem 2.10 for faithful flatness and principal plinth; Example 4.14 for the family and Example 4.15 for m=n=2. The kernel and exact plinth of (18) are also proved directly above, using principality only for (21).
