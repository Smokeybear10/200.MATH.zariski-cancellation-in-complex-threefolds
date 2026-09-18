# All slice shifts still fail a direct LND-extraction test

Date: September 18, 2026. Private working proof. Novelty: UNKNOWN.

There is an actual coordinate frame on a polynomial four-ring such
that, for EVERY polynomial slice of a fixed translation and EVERY
constant ambient translation direction in that frame, the projected
derivation is locally nilpotent precisely when it is a scalar multiple
of one specified derivation with a fixed line. In particular, no such
projection gives a fixed-point-free additive action.

Every nonzero projected constant direction is also primitive, uniformly
over all slices. Dividing out common coefficient factors cannot repair
the failure. The base is already polynomial: this obstructs the stated
extraction procedure, not cancellation. Nonlinear recombination explicitly
repairs the frame.

## 1. The actual frame and its inverse

Set

    A=C[a,b,c], B=A[u], E=partial_u, D=a partial_b+b partial_c.

Reuse the full coordinate frame of
[643](primitive-leading-fixed-locus-frame-obstruction-pass643-working.md):

    alpha=a,
    beta=b-au,
    gamma=c-bu+a u^2/2,
    F=alpha gamma^2+beta gamma^3+gamma^5,
    U=u+F.

The entire inverse, in the displayed new variables, is

    u=U-F, a=alpha, b=beta+alpha u,
    c=gamma+beta u+alpha u^2/2.

Undoing the last shear and then the triangular flow verifies both
compositions. Both successive changes have determinant one; existence
of the displayed whole inverse, rather than the determinant alone,
establishes polynomial invertibility.

Write H=D+E and G=2 alpha gamma+3 beta gamma^2+5 gamma^4. The
actual coordinate partials are

    T_alpha=(partial_a+u partial_b+u^2 partial_c/2)-gamma^2 H,
    T_beta=(partial_b+u partial_c)-gamma^3 H,
    T_gamma=partial_c-G H,
    T_U=H.

These are commuting locally nilpotent derivations of B. Every constant
direction T_lambda=lambda_alpha T_alpha+lambda_beta T_beta+
lambda_gamma T_gamma+lambda_U T_U is covered below. In particular this
covers every coordinate direction obtained after any invertible constant
affine reframing, even when the chosen reframing depends on the slice.

## 2. All slices and their projected fields

Every polynomial slice of THIS E is exactly u+h, with h in A:
E(s)=1 is equivalent to E(s-u)=0. The associated retraction rho_h
fixes A and substitutes u=-h. Put

    beta_h=b+ah, gamma_h=c+bh+ah^2/2,
    G_h=2a gamma_h+3 beta_h gamma_h^2+5 gamma_h^4,
    K_h=lambda_U-lambda_alpha gamma_h^2
        -lambda_beta gamma_h^3-lambda_gamma G_h.

The projected derivation V_(lambda,h)=rho_h T_lambda|A is exactly

    V_(lambda,h)=P_h+K_h D,
    P_h=lambda_alpha partial_a
       +(lambda_beta-lambda_alpha h)partial_b
       +(lambda_gamma-lambda_beta h+lambda_alpha h^2/2)partial_c.

Projection is a derivation because rho_h is an algebra homomorphism
and acts identically on A. Projection need not preserve local
nilpotence, which is precisely the issue tested here.

**Theorem.** For every h in C[a,b,c] and every lambda in C^4,

    V_(lambda,h) is locally nilpotent
        iff lambda_alpha=lambda_beta=lambda_gamma=0.

In that case V_(lambda,h)=lambda_U D. Zero is included in the
classification. The quantifiers permit a separate lambda for each h.

## 3. Divergence gives a uniform proof

A locally nilpotent derivation L on a polynomial ring over C has
divergence zero. Indeed exp(tL) is a polynomial automorphism over
C[t]. Its Jacobian determinant is a unit in C[t,a,b,c], hence a
nonzero scalar, and specialization at t=0 makes it one. Its coefficient
of t is div(L). This is also
[Derksen, Lemma 5.11](https://sites.lsa.umich.edu/hderksen/wp-content/uploads/sites/614/2018/09/LND1.pdf).
Only the necessary implication is used; zero divergence by itself
does not imply local nilpotence.

Since div(D)=0, direct differentiation gives

    D(beta_h)=a(1+Dh),
    D(gamma_h)=beta_h(1+Dh),

and consequently

    div V_(lambda,h)
      =-lambda_alpha h_b+(-lambda_beta+lambda_alpha h)h_c
       -(1+Dh)(lambda_alpha Q1+lambda_beta Q2+lambda_gamma Q3),

where

    Q1=2 beta_h gamma_h,
    Q2=3 beta_h gamma_h^2,
    Q3=2a beta_h+3a gamma_h^2
       +6 beta_h^2 gamma_h+20 beta_h gamma_h^3.

The factor 1+Dh is NEVER zero as a polynomial: its restriction to
a=b=0 is one. This includes arbitrary dependence of h on c.

First suppose d=deg(h)>=1, and write h_d for its nonzero top
homogeneous form. The exact highest forms of beta_h and gamma_h are
a h_d and a h_d^2/2, of degrees d+1 and 2d+1. Thus the three Q's
have exact, distinct total degrees and highest forms:

| Polynomial | Degree | Highest form |
| --- | --- | --- |
| Q1 | 3d+2 | a^2 h_d^3 |
| Q2 | 5d+3 | (3/4)a^3 h_d^5 |
| Q3 | 7d+4 | (5/2)a^4 h_d^7 |

For Q3, the degrees of the first three summands are at most 4d+3;
the last summand has the strictly greater degree 7d+4. None of the
displayed highest forms vanishes in the polynomial domain.

If any of lambda_alpha,lambda_beta,lambda_gamma is nonzero, their
combination Q has degree at least 3d+2: distinct degrees prevent
cancellation of its largest nonzero term. The nonzero product
(1+Dh)Q has degree at least deg(Q). The remaining divergence terms
have degree at most 2d-1, with the zero polynomial allowed. Hence
the divergence cannot vanish.

If h is constant, including zero, (a,beta_h,gamma_h) is an
invertible linear coordinate system. All derivatives of h vanish.
In these coordinates Q1,Q2,Q3 have exact degrees 2,3,4 respectively,
with the degree-four part of Q3 equal to 20 beta_h gamma_h^3.
They are linearly independent over C. The same conclusion follows.

Every locally nilpotent V therefore has its first three lambda's
zero. Conversely D is locally nilpotent, with polynomial flow

    (a,b,c) -> (a,b+ta,c+tb+t^2a/2),

so every lambda_U D is locally nilpotent. This proves both directions
of the theorem for all h, not only bounded-degree or sampled slices.

## 4. Every nonzero projection is already primitive

Here primitive means the coefficients have gcd one, not that they
generate the unit ideal. The distinction matters: D itself is primitive
and nevertheless has a fixed line.

If lambda_alpha is nonzero, V(a) is a nonzero scalar, so V is
primitive. If lambda_alpha=lambda_beta=0 but lambda_gamma is nonzero,
write V(b)=aW and V(c)=lambda_gamma+bW. Any common irreducible
factor divides aV(c)-bV(b)=a lambda_gamma, hence would have to be a.
But V(c) at a=b=0 is lambda_gamma, excluding that factor. If only
lambda_U is nonzero, V=lambda_U D is primitive since gcd(a,b)=1.

It remains to treat lambda_alpha=0 and lambda_beta nonzero. Scale
lambda_beta to one and put m=lambda_gamma,n=lambda_U. For this
section only write B0=beta_h, C0=gamma_h and f=2ac-b^2. Then

    2a C0-B0^2=f,
    W=n-C0^3-m(2a C0+3 B0 C0^2+5 C0^4),
    V(b)=1+aW, V(c)=m-h+bW.

Let g be a gcd of these two coefficients. The ideal (g,a) is the
whole ring, since g divides 1+aW. Also g divides B0-am, because

    aV(c)-bV(b)=am-B0.

Thus in A/(g), a is invertible, B0=am, and 2a C0=f+a^2m^2.
For m nonzero put Z=f+a^2m^2. Substitution in V(b), followed by
multiplication by 16a^3, shows that g divides

    P=16a^3(1+an)-2a Z^3-16a^4m Z-12a^3m^2 Z^2-5m Z^4.

This is a polynomial in C[a,f] with nonzero scalar leading
f-coefficient -5m. For m=0, multiplying by 8a^2 instead shows
that g divides the polynomial

    P0=f^3-8a^2(1+an),

which is monic in f. These are exact polynomial divisibilities:
P-16a^3 V(b) belongs to (B0-am), and, when m=0,
P0+8a^2 V(b) belongs to (B0).

The elementary invariant identity is ker(D)=C[a,f]. After inverting
a, use A_a=C[a,a^-1,f,b] and D=a partial_b. To contract this kernel
back to A, a purported genuine denominator a in a polynomial in
a,f is excluded by the injective substitution C[f] -> C[b,c],
f -> -b^2, modulo a. Repeating removes every such denominator.

Kernels of locally nilpotent derivations in characteristic-zero domains
are factorially closed: the D-degree of a nonzero product is the sum
of the D-degrees of its factors. Hence, from P=g(P/g), both g and
P/g belong to C[a,f]. Use P0 in place of P when m=0.

Specializing the ideal equality (g,a)=A at a=0 makes
g(0,-b^2) a unit in C[b,c]. Injectivity of the preceding substitution
therefore gives g(0,f) in C*. The leading f-coefficients of g and
P/g in C[a] multiply to a nonzero scalar, so each is a nonzero
scalar. If g had positive f-degree, that degree would survive at
a=0, contradicting g(0,f) constant. If g has f-degree zero, its
leading coefficient is g itself, so g is again a nonzero scalar.
This proves primitivity in the remaining case.

Combining this result with Section 3, primitive division of ANY nonzero
raw projected constant direction cannot produce any additional LND.
The proof covers every polynomial h and every nonzero lambda.

## 5. Fixed locus, nonlinear repair, and the precise limitation

Every nonzero classified field has coefficient ideal (a,b). It is
primitive, since gcd(a,b)=1, but vanishes on the entire line a=b=0.
It cannot have a slice: its image lies in that proper ideal. Its
additive action is neither free nor proper. For properness, the
stabilizer of any fixed point is the nonproper group Ga, whereas
stabilizers of a proper action are proper by base change.

Section 4 also excludes a repair by dividing a non-LND projected
field by common coefficient factors. Neither statement excludes general
nonlinear ambient reframings or polynomial-coefficient combinations of
different projected directions.

In fact there is a whole, exact nonlinear repair, already recorded in
[644](slice-scaling-root-extraction-closure-pass644-working.md):

    T_gamma+G T_U=partial_c.

After ANY slice projection the same identity gives

    V_(e_gamma,h)+G_h V_(e_U,h)=partial_c.

Thus a polynomial combination immediately produces a fixed-point-free
intrinsic LND that moves points on the stated line. Other adapted
coordinate partials also exist, and alpha=a is already an invariant
ambient coordinate. There is no common fixed point for all intrinsic
LNDs here and no obstruction to polynomiality of A.

## 6. Antecedents, verification, and research consequence

Note643 supplies exactly this frame, its inverse, and its common
primitive LEADING direction for every constant ambient direction.
Note644 classifies locally nilpotent HOMOGENEOUS components and their
specified closure. Neither assertion alone classifies the raw
projected fields at all polynomial slices.

The ledger subsection "A fixed-frame shortcut also fails on actual
affine four-space" already uses independent divergences to exclude
constant projected LNDs at ONE specified slice of another actual
frame. Note658 excludes a full complementary commuting-basis
certificate at ALL slices in another family, but that family still
has a free projected partial. The added scope here is all slices
for the weaker, single free projection test, even with primitive
division. These are local attributions, not a literature-priority or
novelty claim. The kernel identity and factorial-closure fact used in
Section 4 are standard, not claimed as new.

Three independently performed fresh, unsaved exact calculations checked
the universal first-jet divergence identity. Root also checked both
entire inverse compositions, all sixteen coordinate-partial identities,
the three projected coefficients and the whole nonlinear repair.
General independently checked both inverse compositions; Jet independently
checked all coordinate-partial identities. General supplied Section 4's
gcd argument; root and Jet independently reconstructed it, and root and
General separately checked both clearing identities exactly. The degree
argument and constant-h case have separate mathematical reconstructions.
Their unrestricted quantifiers do not rely on supplemental sample checks.
Full saved-source review and exact evidence are recorded in the ledger.

The resulting decision is to stop treating arbitrary slice adjustment
and constant ambient directions as a universal way to obtain a free
intrinsic LND. Nonlinear extraction remains necessary for that proposed
strategy. No global existence theorem has been obtained. Corrected
complex-threefold cancellation remains UNSOLVED, and novelty UNKNOWN.
The working field/dimension interpretation still awaits Luo's confirmation.
No human expert review or proof-assistant certification is claimed.
No saved checker was executed, imported, compiled, or edited.
