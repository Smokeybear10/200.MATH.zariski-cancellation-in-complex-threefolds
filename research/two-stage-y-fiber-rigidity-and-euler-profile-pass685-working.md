# Rigidity of the y-fixed route, uniformly through polynomial stabilizations

Date: September 18, 2026.

General complex-threefold cancellation remains UNSOLVED and novelty UNKNOWN.
This is a proof about the test family671, not an assertion that its cylinder
is polynomial or that every action fixes y. The proof closes a specified
construction route without imposing a polynomial-degree bound.

## 1. Statements and hypotheses

Throughout k=C, n,m,q>=2 and gcd(q,n*m)=1. Set

    R=C[a,b,r,y,z]/(a(y-1)-r^n-b^q, az-y^m+r),
    B_ell=R[u1,...,u_ell], ell>=1, g=y-1.

The domain and smoothness proofs for R are in671. Every locally nilpotent
derivation (LND) delta of B_ell with delta(y)=0 annihilates R. Consequently

    intersection_{delta in LND(B_ell), delta(y)=0} ker(delta)=R,
    ML((B_ell)_g)=R_g.                                      (1)

For a single extra variable this is the complete formula

    {delta in LND(R[u]):delta(y)=0}=R*partial_u,
    LND(R[u,g^(-1)])=R_g*partial_u.                         (2)

For ell>1, the conclusion is that every such derivation is R-linear, not
that it is a sum of translations with coefficients in R.

There is also an exact compact-support Euler profile. For nonconstant
f in C[Y], let N_lambda be the number of DISTINCT complex roots of
f(c)=lambda. On R or any B_ell,

    chi_c(V(f(y)-lambda))
      =q*N_lambda-(q-1)*1_{lambda=f(0)}.                    (3)

In particular no nonconstant f(y) is a coordinate or a slice of any LND,
even after adjoining arbitrarily many polynomial variables. All these
claims concern the displayed function y and its polynomial subalgebra.
They do not classify arbitrary whole actions or arbitrary coordinates.

## 2. Every nonspecial y-fiber has the same affine surface

Fix c in C minus {0,1}. Eliminating a from y=c gives

    (r^n+b^q)z+(c-1)(r-c^m)=0.

Choose beta with beta^q=c^(m*n). The invertible changes

    r=c^m v, b=beta w, z=(c-1)c^(m*(1-n))*h

give the surface

    S=S_(n,q)=Spec C[v,w,h]/((v^n+w^q)h+v-1).              (4)

Conversely a=c^(m*n)(v^n+w^q)/(c-1), so this is an isomorphism
of the entire fiber, with no further localization. The y=c fiber of
B_ell is S times affine ell-space.

Write F=v^n+w^q and Gamma=V(F) in the affine (v,w)-plane.
The coefficients F and v-1 are coprime, so (4) is a domain. Away from
Gamma the projection to the plane is an isomorphism. Above Gamma it has
exactly q affine-line fibers, over the distinct points

    v=1, w^q=-1.                                          (5)

At these points dF and d(v-1) are independent, since w!=0. In particular
the centers are reduced smooth points of Gamma. Equation (4) is smooth:
off the centers this follows from the plane chart; at a center h=0 makes
the v-derivative 1, while h!=0 makes the w-derivative q*w^(q-1)*h nonzero.

More precisely S is the blowup of the plane at (5), with the strict
transform of Gamma deleted. Locally at each center, F and 1-v are regular
parameters. The F-chart of their blowup adjoins (1-v)/F=h. The omitted
chart portion is exactly the strict transform of F=0. This also proves
the global identification, since the blowup is unchanged off the centers.

## 3. The surface has logarithmic Kodaira dimension one

Put U=A^2 minus Gamma. First compute the logarithmic Kodaira dimension
of U. With N=n*q, the base change

    t^N=v^n+w^q, t!=0

is a finite etale surjective degree-N cover of U. Its explicit coordinates

    v=t^q V, w=t^n W

identify it with G_m times E, where E: V^n+W^q=1. This assertion concerns
the cover, not a decomposition of U itself.

The curve E is smooth. Its completion has exactly one point at infinity
and genus j=(n-1)(q-1)/2. For completeness, projection to W is a cyclic
degree-n cover of the projective line, fully ramified at the q simple
zeros of 1-W^q and at infinity; coprimality gives the latter assertion.
Riemann-Hurwitz yields 2j-2=-2n+(q+1)(n-1). Since n,q>=2 are coprime,
j>=1. Thus E is its smooth projective completion minus that one point.

Complete the product as P^1 times Ebar with boundary
({0,infinity} times Ebar) union (P^1 times {infinity_E}). Its log-canonical
line bundle is pulled back from K_Ebar+infinity_E, of degree 2j-1>0.
Riemann-Roch therefore gives linearly growing log plurigenera, so this
product has logarithmic Kodaira dimension one. Finite etale invariance
then gives the same value for U. This uses the standard Iitaka theorem,
not an assumed general subadditivity conjecture; see Section7.

Take a smooth projective SNC completion (Ubar,D) of U by resolving Gamma
and infinity, leaving neighborhoods of (5) unchanged. Blow up those q
points. The boundary of the resulting completion of S is the STRICT
transform D', not D' plus the new exceptional curves: the exceptional
curves minus their boundary points belong to S. For every center,

    K_new=pi^*K_old+E_i, D'=pi^*D-E_i,
    K_new+D'=pi^*(K_old+D).                               (6)

The cancellation in (6) uses that the old boundary is smooth of
multiplicity one at the center. Pullback preserves the spaces of global
sections of these log pluricanonical line bundles, by pi_*O=O and the
projection formula. Hence

    log_kappa(S)=log_kappa(U)=1.                          (7)

Neither the singular cusp point nor any infinity point is a modification
center. Blowing up those different points while retaining their exceptional
curves would not justify (6).

## 4. No stabilized action can move the surface factor

Suppose a Ga-action on S times A^ell moves a function from O(S). Its
projected velocity is nonzero on a nonempty open subset W of the product.
Product projection is smooth, hence open, so pr_S(W) is a dense open
subset of S. Through each of its points runs a nonconstant morphism
A^1 to S obtained by projecting the corresponding action orbit. Thus S
would be A^1-uniruled, which implies log_kappa(S)=-infinity, contradicting
(7). The precise standard implication is recorded in Section7.

This does NOT assume that the action preserves O(S). Equivalently, choose
a smooth curve through a point of W whose projected tangent is independent
of the projected action vector. Flowing this curve and projecting gives
a dominant generically finite morphism A^1 times curve to S. This is the
usual log-pluriform obstruction to A^1-uniruledness.

Now let delta be an LND of B_ell with delta(y)=0. It induces an LND on
every fiber y=c. Section2 and the preceding argument show that it kills
the images of a,b,r,z on every c!=0,1. Hence each of delta(a), delta(b),
delta(r), delta(z) vanishes on every closed point of the dense open
D(y(y-1)) of Spec B_ell. Since B_ell is a finitely generated reduced
complex domain, each is zero. Thus delta annihilates R.

The same argument works directly on (B_ell)_g. Every LND kills every unit
of a characteristic-zero domain, so it fixes g and y automatically. The
same dense fibers then imply it annihilates R_g. Conversely the coordinate
partials in all u_i have common kernel R or R_g. This proves (1).

When ell=1, an R-linear derivation of R[u] is p(u)*partial_u. Over Frac(R),
local nilpotence forces the polynomial p to have degree zero: positive
degree gives nonzero iterated derivatives of u in characteristic zero.
Its constant coefficient lies in R. The same argument holds over R_g,
and every displayed constant-coefficient translation is LND. This proves(2).

## 5. The exceptional fibers and the complete Euler profile

For c!=1 the projection of the y=c fiber to (r,b) is an isomorphism off
Gamma_0: r^n+b^q=0, and has affine-line fibers precisely at

    r=c^m, b^q=-c^(m*n).

The coprime cusp Gamma_0 has a finite bijective normalization A^1 to
Gamma_0, a homeomorphism on complex points. Thus chi_c(Gamma_0)=1 and
chi_c(A^2 minus Gamma_0)=0. When c!=0,1 there are q exceptional lines;
when c=0 there is one. Therefore these fibers have Euler values q and 1,
respectively. The c=0 surface is also reduced: its linear-in-z equation
has coprime coefficients r^n+b^q and -r.

At c=1 the exact ring is

    C[r,b,a,z]/(r^n+b^q,az-(1-r)).

It is a domain, as follows by embedding the standard az-(1-r) normal
form over the cusp domain into its fraction field with a and a^(-1).
Above Gamma_0 minus {r=1}, projection is the product with G_m, contributing
zero Euler characteristic. At r=1 there are q distinct points and each
fiber is az=0, two affine axes meeting once, of Euler characteristic one.
Thus the c=1 fiber also has value q. It need not be smooth or normal.

In summary, chi_c(V(y-c)) equals 1 for c=0 and q for every c!=0.
For f(y)-lambda, its distinct roots give a disjoint union of these
underlying fibers. Repeated roots only introduce scheme thickenings,
which do not affect chi_c. Affine-space factors have Euler characteristic
one. This proves (3), including every critical value of f.

If d=deg f, the generic value of (3) is q*d. At lambda=f(0), it is at most
q*d-(q-1), strictly smaller. A slice s of an LND gives B=ker(delta)[s],
so all scalar fibers of s are isomorphic. The varying Euler values rule
out every f(y) as a slice. A polynomial coordinate is a slice of a
coordinate partial, so it is ruled out as well. This proof does not need
the contractibility theorem imported in671.

## 6. What this changes, and what it does not

There is no unexamined chart action hiding in R[u,(y-1)^(-1)]: its entire
LND set is (2), and clearing invariant denominators cannot produce a
nonvertical whole action. The conclusion holds across the full parameter
family, not only (n,m,q)=(2,2,3).

A whole action with delta(y)!=0 need not stay locally nilpotent after
inverting y-1. Such actions are known already. Nothing above forces them
to preserve the critical plane or classifies their sliced kernels. No
claim that B_ell is polynomial or nonpolynomial follows from this note.
The main problem still requires a genuinely unrestricted argument using
the ACTUAL polynomial-cylinder hypothesis, or a verified counterexample.

## 7. Sources and verification scope

The finite-etale input is Iitaka's invariance theorem. Its exact use was
personally checked in [Park, Remark1.8 and the proof of Proposition5.4](https://msp.org/ant/2026/20-3/ant-v20-n3-p02-p.pdf),
Algebra & Number Theory20(3) (2026), pp.449,468-469, explicitly citing
Iitaka1977 Theorem3. Root also read [Conceicao, Remark6.3(1),(3), p.365](https://www.impan.pl/shop/en/publication/transaction/download/product/83814),
Acta Arithmetica161(4) (2013), which states product and etale-cover
invariance and identifies Iitaka's textbook Theorems11.3 and11.10.
Iitaka's access-limited original proof was not read and is not claimed
to have been reconstructed here.

The implication from smooth A^1-uniruledness to negative log Kodaira
dimension was personally checked in [Dubouloz--Kishimoto, Definition3 and Section1.2.2, p.387](https://www.numdam.org/item/10.24033/bsmf.2692.pdf),
Bulletin SMF143(2) (2015). Its hypotheses match the smooth affine surface
in(4). No stronger assertion about every rational or rigid surface is used.

The exact formulas and all-parameter geometric proofs above are the
mathematical evidence. Fresh unsaved root d1b36a additionally checks the
scaling, Kummer identity, reduced centers and genus arithmetic for five
parameter triples. Those finite checks do not replace the uniform proof.
No saved checker was run, imported, compiled or edited. This is private
working mathematics, without human peer review, formal certification,
or novelty clearance. The cancellation goal remains active.

The complete236-line source was held at SHA256
2997bfcfaab7c354073f775f71288a83efa03c9c718b7395fca51360534b6141.
Root read through EOF in3cd4b7. General(0b834f/56e58f, finalda974a),
Geometry(7664c0, final3e5ced), and Jet(6a0cc6, final0b9185) each read
the entire held source, independently reconstructed the proof, checked
the primary input scopes, and returned CLEAN. All reviews finished before
this provenance-only addition. Root's direct Park reads were8ed4ff/3293ee;
the Conceicao and Dubouloz--Kishimoto passages were read in turn6218view0
and turn6213view1. Fresh354be1 checks representative exact Euler critical
values, without substituting samples for the all-polynomial proof. These
are internal AI reviews, not human expert review or formal verification.
