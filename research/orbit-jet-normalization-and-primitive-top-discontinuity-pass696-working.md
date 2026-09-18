# Orbit jets can be normalized, but do not control primitive leading actions

## 1. The actual-cylinder consequence and its limit

Work over C. Suppose B=A[u]=C^[4], with E=partial_u and
A=ker E. For every closed point p of Spec A and every integer
k>=2 there is an ACTUAL ambient polynomial coordinate system
(X1,X2,X3,U) such that, for I=m_p B,

    I=(X1,X2,X3),
    E(Xi) belongs to I^k for i=1,2,3,
    E(U)-1 belongs to I^k.                           (1)

The coordinate change takes the entire orbit {p} x A1 to the
standard coordinate line. This is a source-dependent consequence
of the published extension theorem of Kaliman and Udumyan, not
a new orbit-embedding or jet-extension theorem.[^ku]

It does NOT provide a single coordinate change satisfying (1)
for all k. Nor does it imply that the highest u-coefficients of
the corresponding coordinate partials move p in Spec A.

The second result below makes this last distinction exact.
For any prescribed primitive nonzero LND D on a POLYNOMIAL
three-ring that vanishes at p, and any finite normal order,
one can choose a whole polynomial frame agreeing to that order
with the standard frame along {p} x A1, while EVERY nonzero
constant frame direction has primitive intrinsic top D.

These are compatible statements about the available data, not a
solution of the original cancellation problem. The second one
does not produce a point fixed by every intrinsic LND. General
cancellation remains UNSOLVED; novelty is UNKNOWN.

## 2. Formal volume coordinates along an arbitrary slice orbit

The algebra A is smooth of dimension three: regularity descends
from its polynomial extension B. Choose elements x1,x2,x3 in
m_p whose residues are a basis of m_p/m_p^2. Formal smooth
coordinates give

    completion_I B = C[u][[x1,x2,x3]].               (2)

Here the notation means the inverse limit of
C[u,x1,x2,x3]/(x1,x2,x3)^j. The u-degree may increase with
the normal order; no uniform polynomial bound in u is implied.
On this completion E is exactly partial_u, and all xi are
E-invariant. These are local parameters in A, not assumed
global coordinates of A.

Let omega be the standard nowhere-vanishing four-form on B.
Every exponential exp(tE) preserves omega. Its Jacobian is a
unit in C[t,X1_old,...,X4_old], hence a nonzero constant, and
at t=0 it equals one. In completed coordinates write

    omega=g(x,u) dx1 wedge dx2 wedge dx3 wedge du.

The coefficient g is a unit. E-invariance of omega gives
partial_u g=0, hence g=g(x) is independent of u. Over C one
can integrate its formal power series term by term in x1.
Put

    eta1=integral from0 to x1 of g(v,x2,x3) dv,
    eta2=x2, eta3=x3.

The linear coefficient of eta1 in x1 is g(0)!=0, so these
are formal parameters. They all lie in the completed maximal
ideal, are E-invariant, and satisfy

    omega=deta1 wedge deta2 wedge deta3 wedge du.    (3)

For each k, truncating these formal parameters gives an
isomorphism between B/I^k and the k-th infinitesimal neighborhood
of a standard line in A4. It is E-equivariant with respect to
translation in u, and has Jacobian one. Its restriction to the
reduced line uses the coordinate u itself. Each eta truncation
can be represented by an element of A; no formal coefficient
is asserted to be globally polynomial to all orders.

## 3. The precise published extension step

Kaliman--Udumyan Theorem0.1 states that on a complex linear
algebraic group of dimension at least four with no nontrivial
characters, every Jacobian-one isomorphism between finite
infinitesimal neighborhoods of smooth polynomial curves extends
to an automorphism. Apply this to the additive group A4 and
the two lines in Section2. The source's Definition8.2 and
Theorem8.3/Corollary8.6 specify the normal-Jacobian convention;
(3) gives a volume-preserving formal isomorphism, hence meets
that finite-order condition.

The resulting global coordinate functions agree modulo I^k
with eta1,eta2,eta3,u. Since E(I) is contained in I, applying
E preserves the same ideal order. This proves (1), without
losing an order through an arbitrary transverse derivative.
The equality I=(X1,X2,X3) follows from the reduced orbit map.

We use the published extension theorem with its hypotheses;
we do not reconstruct all of its auxiliary group-theoretic
results. It extends one finite jet at a time. Their restrictions
to common lower thickenings ARE compatible, because they lift
the same formal system. What is not supplied is one polynomial
automorphism realizing all orders, or a uniform degree bound
on the finite-order extensions. Global translation does not follow.

### 3.1. A precise sufficient degree bound

Fix the ORIGINAL ambient polynomial coordinates z1,...,z4 of B.
Let e=max_i deg(E(zi))>=0, ignoring zero coefficients, and let
d>=1 be the maximum total degree of an ACTUAL coordinate frame
(X1,X2,X3,U) satisfying (1). If

    k>e+d-1,                                          (3a)

then that frame already makes E an exact global translation.
Indeed each polynomial E(Xi) and E(U)-1 has total degree at most
e+d-1. For any closed point q on the orbit, I^k is contained
in m_q^k. A nonzero polynomial of total degree at most e+d-1
cannot vanish to order k>e+d-1 at q: translating q to the
origin preserves the total degree, whereas every surviving
monomial in m_q^k has degree at least k. The four residuals
are therefore zero. In these actual coordinates E=partial_U,
so A=C[X1,X2,X3]. Also u-U lies in A, and a triangular shear
recovers a coordinate system containing the originally supplied u.

Only forward degree is needed here. The frame must already be
an automorphism; a constant Jacobian alone is not substituted
for that hypothesis. Nor is any estimate for d asserted.

For precision, let mu(k) be the least forward degree among ALL
frames satisfying (1), with this orbit and original ambient
degree fixed. Section3 makes this a finite positive integer.
The admissible sets shrink with k, so mu(k) is nondecreasing.
If an exact adapted frame exists, let d_* be its least degree.
Then mu(k)<=d_*, and (3a) shows mu(k)=d_* for k>e+d_*-1.
If no exact adapted frame exists, (3a) instead forces

    mu(k)>=k-e+1 for every k>=2.                       (3b)

Thus bounded mu(k), or even a bound mu(k)<=alpha*k+C with
alpha<1 along unbounded orders, would suffice. None is proved
from the cylinder assumption. This reformulates a genuine
global obligation; it does not discharge it.

### 3.2. Even an algebraic formal choice can force degree growth

One must not replace the minimum over ALL frames by extensions
of one preselected formal coordinate system. Already for
B=C[x,y,z,u], E=partial_u and I=(x,y,z), consider

    H=(x/(1+x), (1+x)^2*y, z, u).

This is a formal I-adic automorphism, with inverse

    (X/(1-X), (1-X)^2*Y, Z, U).

Its determinant is one and it commutes with E. Each component
is algebraic over the polynomial ring. Every finite truncation
therefore satisfies the extension hypotheses in Section3.
But no single polynomial map realizes all truncations: its first
coordinate P would satisfy (1+x)P=x, impossible in C[x,y,z,u].
Equality in the completion implies this polynomial equality
because the polynomial ring embeds in its I-adic completion.

Every order-k polynomial lift of this chosen system has degree
at least k-1, since its first coordinate must contain the nonzero
monomial (-1)^(k-2)*x^(k-1). This lower bound concerns those
prescribed jets, not mu(k). Here mu(k)=1, since the original
standard frame already works exactly. Compatibility, algebraicity
of the formal coefficients, and extendability at every finite
order consequently do not supply the uniform-degree choice.

## 4. A fixed prescribed primitive top at every finite normal order

Now use the explicit polynomial base A0=C[y1,y2,y3] and
B0=A0[u], E=partial_u. Fix a nonzero primitive LND D of A0
with a fixed point p, meaning D(m_p) is contained in m_p.
Choose 0!=h in ker D with h(p)=0. Such h exists: ker D is
a polynomial two-ring, and a nonconstant invariant minus its
value at p is nonzero and vanishes there.

After a fixed affine-linear coordinate change centered at p,
assume all three yi vanish there and have the same D-degree
N>=1. Indeed a linear coordinate span has some positive maximal
D-degree N; over the infinite field C, a basis can be chosen
outside the proper subspace killed by D^N.

For an arbitrary M>=1 set

    Delta=h^M D,
    ci=exp(-u Delta)yi,
    F(c1,c2,c3)=sum_i ci^(r_i), U=u+F(c),            (4)

where the three integers r_i are distinct and
r_i>=max(4,M+1). The exponential in (4) is finite. Since
h is invariant, Delta is LND and fixes u. The map (y,u) to
(c,U) is the composition of an actual C[u]-automorphism and
an ordinary last-coordinate shear.

For a fully specified inverse let Phi_i(t;Y) denote the finite
constant-parameter Delta-flow polynomial in independent variables
Y=(Y1,Y2,Y3). Then the inverse is

    u=U-F(c), yi=Phi_i(U-F(c);c1,c2,c3).             (5)

Both compositions first undo the shear, then compose opposite
flows with u held fixed. Polynomiality is not inferred merely
from a constant Jacobian.

Put I=m_p B0. Because D(I^j) is contained in I^j and h is
in I, one has

    Delta(I^j) subset I^(j+M),
    Delta^l(yi)=h^(Ml)D^l(yi) belongs to I^(Ml+1).

Therefore ci-yi belongs to I^(M+1), and each ci belongs to I.
The shear term F also belongs to I^(M+1). The full map and
its inverse are identity modulo I^(M+1). This is along the
ENTIRE line Spec(B0/I)=Spec C[u], not only at one value of u.

Differentiation in yi lowers this ideal order by at most one;
differentiation in u does not lower it. The coordinate partials
of the new frame thus differ coefficientwise from those of the
original frame by elements of I^M. One can see this directly
from the inverse polynomial map (5). In addition,

    E(ci) belongs to I^(M+1), E(U)-1 belongs to I^(M+1).

Hence E itself has translation form to arbitrarily prescribed
finite normal order in these actual coordinates. If the original
linear coordinate frame before the preliminary change is wanted,
apply its inverse linear change to the c outputs. All constant-
direction and ideal-order conclusions below are unchanged.

## 5. All constant directions have the same primitive top

The exact u-degree of each ci in (4) is N, with nonzero leader

    ell_i=h^(MN)(-1)^N D^N(yi)/N! in ker D.          (6)

Let J=(partial ci/partial yj), with u fixed. Its entries have
u-degree at most N. Since the flow is a polynomial automorphism
and is identity at u=0, det J=1. Entries of J inverse are
two-by-two cofactors, so have u-degree at most2N.

Let Ti0 denote the pre-shear partial in ci, fixing u, and put
T=Delta+E. This field kills all ci and sends u to one. The
actual coordinate partials after the U shear are

    Ti=Ti0-r_i ci^(r_i-1) T, i=1,2,3,
    TU=T.                                          (7)

Their horizontal u-degrees and highest coefficients on A0 are

    Ti: (r_i-1)N, -r_i ell_i^(r_i-1) h^M D;
    TU: 0, h^M D.                                  (8)

All three positive degrees exceed2N and are distinct. Thus
the old Ti0 terms cannot cancel a displayed leading term.
For EVERY nonzero constant linear combination of the four
partials, the greatest degree among its nonzero summands occurs
exactly once. Its horizontal top is a nonzero invariant multiple
of D. As D is primitive, dividing the gcd of that top's
coordinate coefficients gives D up to a nonzero scalar.

Every such primitive top vanishes at p. Meanwhile for M>=1
the actual four coordinate partials restrict to the standard
tangent frame along the entire orbit. Their determinant is
one. Taking a primitive highest coefficient is not controlled
by these arbitrarily accurate normal-jet data.

## 6. Explicit fixed-direction example

For all M>=1 keep the SAME primitive direction

    D=a partial_b+b partial_c, h=a, p=(0,0,0).

The raw replica is Delta=a^M D. Its inverse-flow coordinates are

    eta1=a,
    eta2=b-a^(M+1)u,
    eta3=c-a^M b u+a^(2M+1)u^2/2.

Set c1=eta3,c2=eta1+eta3,c3=eta2+eta3 and use exponents
(M+3,M+4,M+5) in F. All three ci have u-degree2 with
common leader a^(2M+1)/2. Use the final frame
(eta1,eta2,eta3,U=u+F(c)). It agrees with (a,b,c,u) modulo
I^(M+1), and the preceding constant-direction assertion holds
after this fixed linear recombination.

For proposed outputs (A,B,C,U), define

    tau=U-F(C,A+C,B+C),
    a=A, b=B+A^(M+1)tau,
    c=C+A^M B tau+A^(2M+1)tau^2/2, u=tau.           (9)

These are the whole inverse formulas. Both orders are checked
by substituting the opposite triangular flow and then the shear.
The primitive top is always D, not the raw high-order replica.
The example therefore does not change the chosen primitive
fixed-point behavior when the jet order is increased.

## 7. Deduplication and the remaining general gap

The old43 control makes augmentation jets arbitrarily accurate
while adjoint height grows. It does not prescribe all primitive
tops or use normal jets along the entire orbit. The old643
constructs one frame with arbitrary prescribed primitive top;
the present invariant replica and high-order shear additionally
place that construction in every finite normal-jet neighborhood
of the standard frame. The flow/cofactor mechanism is inherited
from643 and is not presented as a new general construction.

The formal nonalgebraization examples31/642 concern selected
compatible actions on all thickenings. Here every constructed
frame is already a global polynomial automorphism. The obstruction
is in what finite jets certify about its highest coefficients.

Neither Section1 nor this control shows that all intrinsic LNDs
of an arbitrary stably polynomial A fix a point. The control
base A0 is polynomial and has the usual transverse translations;
its standard frame is a successful global choice. No minimality
of the bad frames is asserted. A theorem selecting a globally
useful frame could still work, but must use more than the finite
normal-jet agreement established here.

The unresolved task remains a global action or coordinate
construction from arbitrary A[u]=C^[4], with proof of its
existence and polynomial inverse. This note does not provide it.

[^ku]: Shulim Kaliman and David Udumyan, [On automorphisms of flexible varieties](https://arxiv.org/pdf/2008.02221), version2, April2021, Theorem0.1; Definition8.2, Theorem8.3 and its proof, Example8.5(2), Corollary8.6. These precise primary passages were directly read. The theorem is used with X equal to the additive algebraic group A4. No novelty is claimed for orbit or finite-neighborhood extension.

## 8. Completed review and verification record

The first held source had262 lines and SHA256
e5822bc4941ad9d1b7580c632a63c11aa5d48065e35ac5228e57140b5c7bcc59.
All three complete saved-source reviews found the same sole wording
defect: finite restrictions ARE compatible. The correction in Section3
was made before acceptance. Sections3.1 and3.2 were then added to make
the missing degree condition and the prescribed-jet distinction exact.

The revised mathematical source has331 lines and SHA256
51a97d124fd25ce973d5f642f152850087758442d4823d999d1c996598e45fd5.
Root read all of it through EOF in be1b7b and63f979. Independent
full-source AI reviews were CLEAN: General7cdbef with final hash6fed3f;
Geometry4e9292; and Jet d2e6f3 with final hash cb5d40. This record
is appended after those reviews; the mathematical prefix is unchanged.

Root freshly read the primary KU statement and the complete displayed
Definition8.2/Theorem8.3 proof/Example8.5(2)/Corollary8.6 in
turn6357view0 and turn6359view0. Each reviewer also read these precise
primary passages. No claim to reconstruct all auxiliary KU results
is made. The source is used for extension, not for a degree estimate.

Fresh unsaved checks support the explicit formulas: earlier root493cf0
checked flow inverses, determinant, normal orders and leading terms
for M=1,2,3,5; Jet75cbb6 and bd1d96 independently checked the explicit
construction. Current root b3a0bb checked both rational-H inverse
orders, determinant, equivariance and jet coefficients for k=2 through20;
Jet cb5d40 separately checked that example for k=2 through9. Finite
checks are supplementary; the uniform claims use the written proofs.

The ordinary residual degree bound was already in43, and73 gave a
different conditional degree statement for finite-complexity families.
The finite-normal-order criterion here adds no proof that suitable
low-degree frames exist. The flow/cofactor method is credited to643.
No mathematical priority claim follows from the bounded archive check.

No saved checker was executed, imported, compiled or edited. No git
mutation, scheduler change, contact, publication or submission occurred.
These AI reviews are not human expert review, formal certification or
novelty clearance. The original cancellation target remains UNSOLVED.
