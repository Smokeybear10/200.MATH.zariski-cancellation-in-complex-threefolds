# All z-fixed actions and the exact z-fiber profile

Date: September 18, 2026.

General complex-threefold cancellation remains UNSOLVED and novelty UNKNOWN.
This note concerns the specific (n,m,q)=(2,2,3) member of671. Neither
polynomiality nor nonpolynomiality of its cylinder is established here.

## 1. Statements and scope

Work over C and set

    R=C[a,b,r,y,z]/(a(y-1)-r^2-b^3, az-y^2+r), B=R[u].

The smooth-domain and constant-unit assertions for R are proved in671.
For EVERY locally nilpotent derivation (LND) delta of B,

    delta(z)=0  iff  delta is in R*partial_u.                 (1)

For every nonconstant g in C[Z], write B_g=B[g(z)^(-1)] and similarly R_g.
Then

    LND(B_g)=R_g*partial_u, ML(B_g)=R_g,
    intersection_{delta(z)=0} ker(delta)=R.                  (2)

These action statements concern ONE added polynomial variable. Rigidity
of a surface alone does not justify their analogue with two or more.

In contrast, the following compact-support Euler profile holds for R and
EVERY polynomial stabilization. If f in C[Z] is nonconstant and N_lambda
counts DISTINCT roots of f(c)=lambda, then

    chi_c(V(f(z)-lambda))
      =5*N_lambda-2*1_{lambda=f(0)}-2*1_{lambda=f(-1/16)}.     (3)

Thus no nonconstant f(z) is a coordinate or an LND slice. On any
stabilization there is no automorphism sending y to a polynomial in z,
or z to a polynomial in y. A setwise stabilizer of C[y] fixes y, and a
setwise stabilizer of C[z] fixes z. On B=R[u], either stabilizer preserves
R, normalizes its vertical translation action, and preserves

    L=V(a,b,r,y), with B/I(L)=C[z,u].                        (4)

No assertion that every automorphism belongs to either stabilizer is made.

## 2. Whole z-fibers and their projective completion

Fix c!=0. In R/(z-c), put

    w=2*c*r+y-1, P_c(y)=(y-1)(4*c*y^2+y-1).

Eliminating a and completing the square gives the ENTIRE fiber

    S_c=Spec C[y,b,w]/(w^2+4*c^2*b^3-P_c(y)).               (5)

The inverse is r=(w-y+1)/(2*c), a=(y^2-r)/c. Both maps are polynomial
for the fixed nonzero scalar c; no open part of this fiber was deleted.
The exact discriminant is

    disc_y(P_c)=16*c^2*(1+16*c).                            (6)

For c!=0,-1/16, (5) is smooth. A singular affine point would have w=b=0
and P_c=P_c'=0, contradicting (6). In coordinates [W:B:Y:H], its ordinary
projective closure V_c has equation

    H*W^2+4*c^2*B^3-4*c*Y^3+(4*c-1)*Y^2*H
                   +2*Y*H^2-H^3=0.                       (7)

At infinity H=0 the B and Y derivatives force B=Y=0 at any proposed
singular point. The remaining point [1:0:0:0] has H-derivative1, so is
smooth. Hence V_c is a smooth cubic surface for these c.

Its boundary D_c is Y^3=c*B^3 in the plane H=0. It consists of three
distinct lines, all through p=[1:0:0:0]. The tangent plane of V_c at p
is H=0, so p is the required Eckardt point. Therefore (V_c,D_c) is exactly
a special pair in Dubouloz--Kishimoto, Section3.2.1. Their published
Proposition16(a) and Corollary17(a) imply

    Aut(S_c)=Aut(V_c,D_c), a finite group.                  (8)

In particular the affine coordinate ring of S_c is rigid: a nontrivial
Ga action would give a positive-dimensional family of automorphisms,
contradicting (8). This imports that published theorem, not a claim that
every affine cubic surface is rigid.

## 3. Why one cylinder variable does not destroy this rigidity

Here is the characteristic-zero lemma used in (1). If a finitely
generated domain C0 is rigid, then every LND of C0[u] kills C0.

Give C0 degree0 and u degree1. If an LND D moves C0, its filtration
degree q, computed on finitely many algebra generators and u, is at
least0. Its highest homogeneous derivation Dhat is nonzero and locally
nilpotent. Indeed whenever an iterated homogeneous derivative is nonzero,
it is the leading term of the corresponding iterate of D; local
nilpotence of D therefore gives local nilpotence of Dhat.

Homogeneity gives Dhat(u)=h*u^(q+1), h in C0. In a characteristic-zero
domain, v dividing an LND-image D(v) forces D(v)=0: the nonnegative
LND-degree satisfies deg_D(Dv)=deg_D(v)-1 and is additive on products,
which contradicts Dv=v*h!=0. Hence Dhat(u)=0. Nonzeroness then forces
Dhat|C0=u^q*d with a nonzero derivation d of C0. Iteration gives
Dhat^j(c)=u^(j*q)*d^j(c); thus d is LND, contradicting rigidity.

Consequently D kills C0 and is p(u)*partial_u. Over Frac(C0), if p has
positive degree, repeated derivatives of u do not vanish in characteristic
zero. Thus p is in C0. Conversely every such translation is LND. This
proves the full formula LND(C0[u])=C0*partial_u, including the zero action.
The retained intrinsic-actions-pass, Section2, supplies the same lemma.

Now delta(z)=0 induces an LND on every fiber of B over z. By Section2 and
this lemma, it kills the images of a,b,r,y on every c!=0,-1/16. Therefore
delta(a),delta(b),delta(r),delta(y) vanish on the dense open subset
z*(16*z+1)!=0 of Spec B. This uses all closed points of these fibers,
not merely their generic points. Since B is a reduced complex domain,
these functions are zero. No preservation of R was assumed beforehand.
The last part of the lemma now gives (1), and partial_u gives the kernel
intersection in (2).

On B_g every LND kills the unit g(z), so g'(z)*delta(z)=0. Since g is
nonconstant and the characteristic is zero, delta(z)=0. For every good
c with g(c)!=0, its specialized derivation again kills the surface
factor. These fibers remain dense. It follows that delta kills R_g and
is h*partial_u for h in R_g. Conversely these translations exist, proving
both localized assertions of (2). This proof is not a localization of an
arbitrary whole LND moving z; such a localization need not be LND.

## 4. Both exceptional fibers and the complete Euler profile

For c!=0, project (5) to the affine (y,w)-plane. It is a finite degree3
cover, etale away from the branch curve

    C_c: w^2=P_c(y).

Over this curve the underlying reduced preimage is C_c itself. Its
scheme fiber has equation b^3=0, which is NOT reduced; compact-support
Euler characteristic ignores this thickening. Additivity and the
degree3 covering formula therefore give

    chi_c(S_c)=3*(1-chi_c(C_c))+chi_c(C_c)
             =3-2*chi_c(C_c).                              (9)

For c!=0,-1/16 the curve C_c is a smooth double cover with a squarefree
cubic on the right. Its smooth completion is an elliptic curve, and
exactly one point lies at infinity. Hence chi_c(C_c)=-1 and chi_c(S_c)=5.

At c=-1/16 the cubic is

    P_c(y)=-(y-1)*(y-2)^2/4.

The normalization of C_c is A^1_v with

    y=1-4*v^2, w=-v-4*v^3.

Indeed v=w/(y-2) in the function field and satisfies v^2=(1-y)/4,
so is integral. These formulas are inverse off y=2. Precisely the two
points v=i/2,-i/2 map to the node (y,w)=(2,0); all other fibers contain
one point. Thus chi_c(C_c)=(1-2)+1=0, and (9) gives chi_c(S_c)=3.
No Milnor-number or smoothing assumption is used.

At c=0 the original equations give r=y^2 and a(y-1)=y^4+b^3. Put
a'=a-(y^3+y^2+y+1). The exact surface is

    a'*(y-1)=b^3+1.                                      (10)

It is smooth: simultaneous vanishing of the three partial derivatives
would require a'=0,y=1,b=0, contradicting the equation. Over y!=1 it
is G_m times A^1; over y=1 it has three disjoint affine lines, one for
each simple root of b^3=-1. Its Euler characteristic is therefore3.

All c!=0 surfaces in (5) are domains. The polynomial P_c(y)-w^2 is
irreducible in C[y,w], because the odd-degree P_c is not a square in
C(y). Its valuation1 makes it not a cube in C(y,w), proving irreducibility
of the cubic equation in b. Surface (10) is a domain as well, since its
linear polynomial in a' has coprime coefficients y-1 and b^3+1.

This proves that the z-fiber has Euler value3 at exactly 0,-1/16 and
value5 elsewhere. Decomposing V(f(z)-lambda) into its distinct underlying
scalar fibers proves (3). Multiple roots only cause nilpotent thickening.
If f(0)=f(-1/16), BOTH subtractions in (3) apply. Affine-space factors
have Euler characteristic1, proving the stabilization assertion.

For d=deg f the generic value is5*d. At lambda=f(0) it is at most
5*d-2, strictly smaller. A slice of an LND presents the ring as a
polynomial ring in that slice over its kernel, so all its scalar fibers
are isomorphic. This variation rules out a slice, and therefore a
polynomial coordinate, without assuming contractibility of the variety.

## 5. Consequences for specified automorphisms

By685, the generic Euler value for y is3 and for f(y) is3*deg f. Formula
(3) makes the generic value for f(z) equal5*deg f. An automorphism taking
y to f(z) would imply 3=5*deg f; one taking z to f(y) would imply
5=3*deg f. Neither is possible. These exclusions hold after any number
of polynomial variables has been added.

If phi preserves C[y] setwise, its restriction is y -> alpha*y+beta,
alpha!=0. The unique exceptional Euler value of the y-fibration occurs
at0, forcing beta=0. Its only singular fiber is at1, forcing alpha=1.
To check the latter assertion directly, for y=c!=1 the surface equation
is (r^2+b^3)z+(c-1)(r-c^2)=0. Vanishing of all partials on the surface
would require r=c^2, r^2+b^3=0, b^2*z=0, and 2*r*z+c-1=0.
For c=0 the last equation is impossible, while for c!=0 the first two
give b!=0, then z=0, again impossible. At y=1 the equations are
r^2+b^3=0 and az=1-r, singular along r=b=0,az=1.

If phi preserves C[z] setwise, write phi(z)=alpha*z+beta. Its affine
parameter map preserves the Euler-exception set {0,-1/16}. The only
singular scalar z-fiber is at -1/16: Sections2 and4 prove all the others
smooth, while (5) has its singular point at y=2,w=b=0 at this value.
Thus it cannot exchange the two exceptional values. It fixes both,
forcing alpha=1,beta=0. All these arguments survive stabilization.

For B=R[u], fixing y or z permutes by conjugation the respective entire
set of fixed-function LNDs. Its kernel intersection is R by685 or (2).
Therefore phi(R)=R. Degree comparison for an automorphism of one
polynomial variable over R then gives

    phi(u)=d*u+h, d in C*, h in R,                        (11)

using R*=C*. Hence phi normalizes R's vertical translation action.
Finally671 proves ML(R)=C[a], so phi|R sends a to lambda*a+mu. The
a=0 fiber is the singular cusp y^4+b^3=0 times A^1_z; all nonzero
a-fibers are A^2. Thus mu=0. Its singular locus is b=y=r=0, so its
stabilized singular locus is exactly L. This proves the preservation
claim in (4). The z-based kernel-intersection step is not asserted for
two or more added variables.

## 6. The unrestricted gap is still present

The polynomial curve

    (a,b,r,y,z,u)=(t^3,-t,t^2,t,0,0)

satisfies both relations, meets L at t=0, and leaves it for t!=0. Thus
an argument claiming that no affine-line curve can leave L is false.
This curve cannot be an orbit of a whole z-fixed action by (1), but an
action can move z globally while having z constant on a particular orbit.
The curve alone therefore neither supplies nor excludes an escaping LND.

Combined with685, a nonvertical whole LND on B must move BOTH y and z.
Such actions are not excluded by this note. Nor does a supplied fibration
become intrinsically invariant simply because its generic fiber is rigid.
The full cancellation problem still needs an unrestricted argument using
the actual polynomial-cylinder hypothesis, or a verified counterexample.

## 7. Sources and evidence status

The imported projective-completion theorem is
[Dubouloz--Kishimoto, Log-uniruled affine varieties without cylinder-like open subsets](https://www.numdam.org/item/10.24033/bsmf.2692.pdf),
Bulletin SMF143(2) (2015), Section3.2.1, Proposition16(a), Corollary17(a),
printed pp.395-398. Root read the special-pair definition and complete
Proposition16 and Corollary17 proofs in turn6250view0. The numbering here
is that of the published paper, not the older preprint. All hypotheses
used in its application are verified in Section2.

The one-variable lemma is reproduced in Section3, rather than importing
an unproved arbitrary-stabilization assertion. The prior proofs671 and685
are explicit dependencies for the stated properties of R and the y-route.
This is private working mathematics. Human peer review, formal
certification, and novelty clearance have not been obtained. No saved
checker was run, imported, compiled or edited.

The complete262-line source was held at SHA256
5c12387b9c2f04f75a2409744e6fefce7d1e1be8086d789189e36d7eb152ec7c.
Root read it through EOF in e3d54d. General(8e39be/9be2bd, hash9b9866),
Geometry(a67139, hash991ff3), and Jet(08ab3b, hash2e60a1) each read the
entire held source and independently reconstructed its proofs. All
returned CLEAN and confirmed the same hash before this provenance-only
addition. Fresh root a44ee5 checks the full square identity, discriminant,
projective equation, nodal normalization, exceptional shift, escaping
curve and representative Euler critical values. These finite checks do
not replace the all-parameter proof. The three reviews are internal AI
reviews, not human peer review or formal certification.
