# A globally solved quadratic extension with nonisomorphic old-divisor localizations

## 1. Result and purpose

For every integer m>=3 let

    R=C[x,y,z], g=x^2 z-y^m, C0=C[x,g],
    D=x^2 partial_y+m y^(m-1)partial_z,
    O=(C0)_(x), K=Frac(O)=C(x,g), kappa=O/(x)=C(g).

Take the quadratic extension of688 with a=x,b=1,w=y:

    B=R[t], E=D+(1+xy)partial_t,
    v=xt-y^2/2, q=xv-y, u=t-yv+xv^2/2.

Its sliced quotient is the polynomial ring

    A=C[x,W,Z], y=W-xW^2/2,
    g=x^2 Z-(W-xW^2/2)^m,                             (1)

where C0 is embedded by these particular x,g. Define
R_O=R tensor_(C0) O and A_O=A tensor_(C0) O.

**Theorem.** R_O and A_O are NOT isomorphic as C-algebras.
No O-linearity, fixed invariant generators, or prescribed action
on the residue field is assumed of a prospective isomorphism.

Nevertheless R and A are both polynomial three-rings, and u is
a whole coordinate of the actual polynomial four-ring B. Thus
this is NOT a cancellation counterexample. It disproves the
proposed intermediate requirement that every quadratic construction
can first be rectified on every old-invariant height-one localization
and then glued. Those local rectifications need not exist at all.

The earlier whole-plane-normalizer obstruction689 did not exclude
arbitrary C-isomorphisms after this localization. Here units recover
the entire DVR O intrinsically, and its possible reparametrizations
are handled without a restricted form for its automorphism group.
General cancellation remains UNSOLVED; novelty is UNKNOWN.

## 2. Whole positive control and the two kernels

The coordinate assertion has a complete polynomial inverse. For
proposed new coordinates (x,Q,z,U), set

    V'=xU-Q^2/2,
    y=xV'-Q, t=U-QV'+x(V')^2/2.                       (2)

Substitution gives v=V', q=Q and u=U, and the reverse composition
also fixes the original x,y,z,t. Thus (x,q,z,u) are coordinates.
Setting U=0 and W=-Q gives exactly (1).

The kernel of D is C0. Indeed R_x=C[x,x^(-1),g,y] with
D=x^2 partial_y. A nonzero f-pole, here f=x, in a prospective
invariant cannot contract to R: reducing its least numerator
modulo x would give a nonzero polynomial in -y^m equal to zero.
Thus the contraction of C[x,x^(-1),g] is C[x,g].

On A there is the whole nonzero LND

    delta x=0, delta W=x^2,
    delta Z=m(1-xW)(W-xW^2/2)^(m-1).                  (3)

It is triangular, preserves g from (1), and its kernel is also
the embedded C0. The same x-localization and contraction prove
this, now reducing prospective numerators to polynomials in -W^m.
Consequently C0 is factorially closed in BOTH R and A.

## 3. The units intrinsically recover the old DVR

Let S=C0 minus the prime ideal (x), so R_O=S^(-1)R,
A_O=S^(-1)A, O=S^(-1)C0. Both original polynomial rings have
unit group C*. If r/s is a unit in R_O, with r in R,s in S,
there exist r' in R and s' in S such that rr'=ss'. Since
ss' is in C0 minus zero, factorial closure puts r,r' in C0.
Their product is outside (x), so both belong to S. Therefore

    R_O^*=O^*, A_O^*=O^*.                             (4)

The identical proof applies in A. Furthermore

    O=C[O^*].                                        (5)

Indeed every element of a local ring is either a unit or belongs
to its maximal ideal; in the latter case it equals (1+h)-1, a
difference of units. Equations (4)-(5) show that ANY C-isomorphism
psi:R_O to A_O must restrict to a C-automorphism zeta of O.
It therefore preserves (x) and its valuation. This conclusion is
intrinsic to the localized rings; it was not imposed on psi.

## 4. Generic affine-line form and two-sided valuation saturation

The exact generic and special presentations are

    R_K=K[y], A_K=K[W],
    R_O/(x)=kappa[y,z]/(y^m+g),
    A_O/(x)=kappa[W,Z]/(W^m+g).                       (6)

The polynomial T^m+g is irreducible over kappa=C(g), by Eisenstein
at g over C[g]. Each special fiber is therefore a polynomial line
over a degree-m field extension of kappa. In particular 1,W are
linearly independent over kappa, and so are 1,y in the other fiber.

Suppose psi exists. Its extension to the generic fibers is a
zeta-semilinear isomorphism of polynomial one-rings over K, hence

    psi(y)=alpha W+beta, alpha in K^*, beta in K.       (7)

We claim alpha is in O^* and beta is in O. If the minimum of
their x-valuations is negative, multiply (7) by the smallest
positive x-power making both coefficients integral. Its left
side is then in x A_O, whereas reduction of the right side is
a nonzero kappa-linear combination of 1,W. This contradicts (6).
Thus both coefficients are integral. Apply the same argument to
psi inverse. Its leading coefficient is zeta^(-1)(alpha^(-1)),
whose valuation is the negative of alpha's because zeta preserves
the DVR valuation. It must also be integral. Therefore v_x(alpha)=0,
proving the claim. No coefficient was assumed constant in g.

Every element of O has a unique first-order expansion with
coefficients in the natural field kappa=C(g) inside O. Write

    alpha=alpha0+x alpha1 mod x^2,
    beta=beta0+x beta1 mod x^2,
    alpha0 in kappa^*, alpha1,beta0,beta1 in kappa.

## 5. The impossible first-order identity

Apply psi to g=x^2 z-y^m. Since zeta(x) belongs to x O,
zeta(x)^2 psi(z) belongs to x^2 A_O. Hence

    zeta(g)+(alpha W+beta)^m=0 mod x^2 A_O.             (8)

Modulo x, equation (8) lies in the degree-m field kappa[W]/(W^m+g).
The coefficient of W^(m-1) is m alpha0^(m-1) beta0, so beta0=0.
The constant term then gives

    zeta(g)=alpha0(g)^m g+x gamma(g) mod x^2 O         (9)

for some gamma in kappa. This conclusion allows every DVR
automorphism consistent with the residue relation, not only
the polynomial-plane normalizers considered in689.

From (1) one has

    W^m=-g+(m x/2)W^(m+1) mod x^2 A_O.                (10)

Substitute (9)-(10) in (8), divide by x in the domain A_O,
then reduce modulo x. The resulting identity in
L=kappa[W]/(W^m+g) is

    m alpha0^(m-1)W^(m-1)(alpha1 W+beta1)
       +(m/2)alpha0^m W^(m+1)+gamma=0.                (11)

The alpha1 term is in kappa, the beta1 term is in
kappa*W^(m-1), and the middle term is
-(m/2)alpha0^m g W. Since m>=3, the three elements
1,W,W^(m-1) are linearly independent over kappa. The W coefficient
is nonzero, as alpha0 and g are nonzero. This is a contradiction.
It proves the stated absolute C-nonisomorphism of R_O and A_O.

## 6. Exact consequences and limits

There is no automorphism of B_O taking t to u: quotienting such
an automorphism would give an isomorphism R_O to B_O/(u)=A_O,
contrary to the theorem. Likewise a rectification of E on B_O
to partial_t would identify their kernels and give the same
contradiction. Invariant localization commutes with ker E here.

This does not contradict (2). The whole global coordinate
completion does not extend as an automorphism of the PARTICULAR
localization B_O on both sides. It moves the old invariant
denominators to a different multiplicative set. Nor does the
theorem say the localizations are nonisomorphic after every
further localization or after forgetting fewer old divisors.

The right research obligation is therefore not merely to glue
already-available old-base divisor rectifications. A successful
general construction must be allowed to change the invariant
localization itself, or use another global recognition principle.
This obstruction narrows a proof strategy; it does not prove or
disprove the general cancellation conjecture.

## 7. Completed internal reconstruction

The mathematical source held for review had182 lines and SHA256
69436fd1e934cc824306c2d0688949f0e75792432b62430dc27f2609d67fc573.
Root read the full source in36020c and revalidated it in552a08.
Three independent full-source AI reviews reported CLEAN:
General e7708d/2fee15, Jet db378b/d23709, and Geometry510b6a.
Fresh unsaved root computation7ee0ca checked both universal inverse
orders and the first-jet remainder for m=3 through13. The theorem
for every m>=3 rests on the written independence argument, not on
those finite checks. Only this provenance was appended afterward.
No saved checker was executed, imported, compiled or edited.
These reviews are not human expert review, formal verification,
or confirmation of novelty.
