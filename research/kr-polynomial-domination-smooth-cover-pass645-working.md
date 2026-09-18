# Polynomial domination and a smooth affine-space cover of KR-type threefolds

Date: September 18, 2026. Private working proof. Novelty: UNKNOWN.

For every m,p,q>=2 over C, this note constructs an explicit polynomial
map from A3 to the smooth hypersurface

    X={x+x^m y+z^p+t^q=0} in A4.

It is submersive at preimages of every point in a specified principal
open subset, including the entire exceptional fiber x=0. Composing
with two familiar additive flows gives an everywhere smooth surjection
A5 -> X. All its fibers are computed below. For the classical Russell
cubic they show explicitly why this map is not a product projection.

This is not a cancellation proof. No isomorphism X x A1=A4, retraction
onto X, dominating spray OVER X, or new publication claim is supplied.
For arbitrary p,q use the term KR-type hypersurface; the usual first-kind
Koras-Russell terminology includes gcd(p,q)=1.

## 1. A global polynomial map

Use source coordinates a,b,c and abbreviate

    r=m-1,    n=pq,    P=b^p+c^q,    h=1+aP^r,
    epsilon=(-1)^(m+1).

Define F:A3 -> A4 by

    x=-P,
    y=epsilon sum_(j=1)^n binom(n,j) a^j P^(r(j-1)),
    z=b h^q,
    t=c h^p.                                           (1)

The sum is polynomial, including along P=0. Its useful quotient
notation is y=(-1)^m(1-h^n)/P^r, with the quotient understood as
the displayed polynomial. Direct substitution gives

    x+x^m y+z^p+t^q
      =-P+P(1-h^n)+P h^n=0.                           (2)

Thus F maps to X globally; no denominator is inverted. If

    V=1+x^(m-1)y,

then F*(V)=h^n. The hypersurface X is smooth: when x!=0 its defining
equation has nonzero y-derivative x^m, and when x=0 its x-derivative
equals one. Its defining polynomial is irreducible, since as a
polynomial in y it is primitive and linear over C[x,z,t].

## 2. Full tangent rank wherever h is nonzero

On P!=0, the target coordinates x,z,t are local coordinates because
x=-P!=0. Their source Jacobian is exactly

    det d(x,z,t)/d(a,b,c)=pq P^m h^(p+q-1).             (3)

One direct proof uses differential forms. Since
dh=P^r da+arP^(r-1)dP, expanding dx wedge dz wedge dt leaves

    P^r h^(p+q-1)(qb P_b+pc P_c) da wedge db wedge dc.

Here qb P_b+pc P_c=pq P, proving (3). Consequently F has rank
three whenever P h!=0.

At P=0, h=1 and the image is

    (x,y,z,t)=(0,epsilon pq a,b,c).                    (4)

The target coordinates y,z,t are local coordinates here. The a-column
of their Jacobian is (epsilon pq,0,0). If m>2, their z,t rows have
the identity matrix in the b,c columns, because d(P^r)=0 along P=0.
If m=2, that two-by-two block is

    I_2+a (qb,pc)^T (P_b,P_c).

Its determinant is 1+a(qb P_b+pc P_c)=1+apqP, hence is one on P=0.
In both cases,

    det d(y,z,t)/d(a,b,c)=epsilon pq  on P=0.           (5)

Thus F has rank three at EVERY point with h!=0, including P=0.
Equivalently, F is etale at these source points. No claim of
finiteness or constant fiber cardinality is included.

For comparison with exact checks, the second full minor is

    det d(y,z,t)/d(a,b,c)
      =epsilon pq h^(p+q-1)(m h^n-(m-1)).              (6)

Formula (6) is not needed outside P=0 for the rank proof. Its extra
factor records when y,z,t fail to be target local coordinates.

## 3. Every point of X_V has an etale preimage

Let (x0,y0,z0,t0) be a point with V0!=0. If x0=0, its equation
gives z0^p+t0^q=0. Take b=z0,c=t0 and a=y0/(epsilon pq).
Then P=0 and (4) gives the desired point with full rank.

If x0!=0, choose a complex h0 with h0^n=V0. It is nonzero. Put

    b=z0/h0^q,    c=t0/h0^p,
    a=(h0-1)/(-x0)^r.

The target equation gives z0^p+t0^q=-x0 V0, so P=-x0 and
1+aP^r=h0. The formula for y follows from (2), since x0^m!=0.
This provides a preimage of full rank by (3).

## 4. Two flows give an everywhere smooth surjection from A5

On X consider the commuting LNDs

    L=x^m partial_z-p z^(p-1) partial_y,
    N=x^m partial_t-q t^(q-1) partial_y.               (7)

Both preserve the defining equation and are triangular on its
generators. They commute because L fixes x,t and N fixes x,z.
Their combined polynomial flow Phi_(s,v) sends

    x -> x,
    z -> z+s x^m,
    t -> t+v x^m,
    y -> y-((z+s x^m)^p-z^p)/x^m
          -((t+v x^m)^q-t^q)/x^m.                    (8)

Both quotients in (8) are polynomial by the binomial theorem. The
inverse is Phi_(-s,-v). Define

    H:A5 -> X,    H(a,b,c,s,v)=Phi_(s,v)(F(a,b,c)).    (9)

First, H is onto. Section3 handles V!=0 with s=v=0. For a target
point with x0!=0, applying L with time s replaces z0 by z0+s x0^m.
The polynomial (z0+s x0^m)^p+t0^q has degree p and nonzero leading
coefficient. Some s therefore makes it nonzero, equivalently V!=0.
Lift that moved point using Section3 and apply the inverse flow in
(9). Points with x0=0 already have V0=1 and were handled. In fact
one of the p+1 times 0,1,...,p always works.

Second, H has rank three at EVERY source point. If h!=0, dF already
has rank three, and the fixed flow is a target automorphism. If h=0,
then P!=0 and x=-P!=0. Also dP!=0: P_b=p b^(p-1) and P_c=q c^(q-1)
can both vanish only at b=c=0, where P=0. Thus dF has a vector whose
x-component is nonzero. The two flow-parameter derivatives of H are
L and N at its image. On x!=0 these are independent and span ker(dx),
as their z,t components form x^m I_2. They supply the other two
directions. The flow preserves x, so the nonzero x-component survives.

Both source and target are smooth complex varieties. The surjective
differential criterion therefore proves that H is a smooth surjective
morphism of relative dimension two, not merely a generically
submersive dominant map.

The preceding onto argument also shows strong algebraic dominability:
every point of X is reached by an A3 -> X morphism submersive at a
source point. Translate that source point to zero if desired. The
finite family Phi_(-j,0) F, j=0,...,p, suffices with suitable preimages.

## 5. Exact fibers, and why this is not a product

Fix a target point with x=x0!=0. Its preimages have P=-x0.
The coordinate a is free. Once a,b,c are chosen with b^p+c^q=-x0,
the two flow parameters are uniquely forced:

    s=(z0-bh^q)/x0^m,    v=(t0-ch^p)/x0^m.

The y-coordinate then follows from the defining equation. These
polynomial formulas and projection to a,b,c give inverse morphisms,
so the scheme fiber is

    H^(-1)(x0,y0,z0,t0) = A1 x {b^p+c^q=-x0}.        (10)

For a target with x0=0, one instead has P=0,h=1,b=z0,c=t0, and

    y0=epsilon pq a-p z0^(p-1)s-q t0^(q-1)v.

This equation uniquely determines a for each s,v. Hence this fiber
is A2, also scheme-theoretically.

For p=2,q=3 and x0!=0, the curve in (10) is a smooth affine
elliptic curve with one point removed from its smooth projective
cubic completion. It has nonzero first integral homology, whereas
A2 has zero first homology. Its product with A1 is therefore not
A2. In particular, for the Russell cubic H is neither a Ga2-torsor
nor a product projection. Smoothness does not force isotriviality
of a nonproper morphism.

## 6. Relation to the cancellation investigation and prior work

An actual polynomial cylinder would provide much more: a regular
retraction r:A4 -> X with a section i. It gives the global algebraic
spray s(x,v)=r(i(x)+v), whose parameter differential is onto because
dr composed with di is the identity. Map (9) supplies no such section
or spray over X. Neither does pointwise algebraic dominability.

The standard Russell cubic is known not to be A3. A close published
antecedent is [Kaliman and Zaidenberg, Examples1.5 and6.3 in the
1998 arXiv version](https://arxiv.org/html/math/9801076v2), which gives
birational domination of the cubic by A3 and credits P. Russell.
Its modification is centered over a smooth point of the cusp. That
particular map does not cover the singular cusp line. These examples
were read directly; the present note does not claim priority for
domination, strong domination, smooth covering, or the formulas above.
A complete novelty audit has not been performed.

The useful boundary is exact: even an everywhere smooth surjection
from affine space, with the fibers described here, does not replace
the distinguished product structure required by cancellation. This
does not decide algebraic Oka/subellipticity of the test hypersurfaces,
nor exclude a possible stronger use of global sprays or retractions.

## 7. Verification boundary

General and Jet independently reconstructed the uniform polynomiality,
rank, surjectivity and smoothness arguments before this note was saved.
Jet additionally derived the fiber descriptions. Root's fresh unsaved
session28651 completed with PASS in0d749d, checking (1)--(6) for tuples
(m,p,q)=(2,2,3),(3,2,3),(2,3,2),(2,2,2), and the full commuting flow
identities for (2,2,3). Jet's1c4cb9 checked unspecialized determinant
algebra, and147cb0 checked the entire cubic mapH, its flow derivatives
and the x=0 fiber equation. General's review was written proof only;
its attempted default/bundled Python environments lacked SymPy.

Finite checks supplement, not replace, the all-parameter proof. No
saved checker was executed, imported, compiled or edited. General and
Jet subsequently read all 226 saved lines at SHA256
b0996adaa4f08a2709a206625322269f992e4c8955d57225218491c92c893715
and reported CLEAN. General's complete read ended in94b9eb and its
final hash/count check was9a65d5; Jet's complete read was39ecf4, its
ending reread759306 and final hash checka23d85. Both also reopened
the cited primary antecedent. This paragraph is a provenance-only
update after those reviews; the mathematical argument is unchanged.
These are AI-assisted proof reviews, not human expert review or a
formal proof-assistant certificate. General cancellation remains
UNSOLVED; novelty remains UNKNOWN.
