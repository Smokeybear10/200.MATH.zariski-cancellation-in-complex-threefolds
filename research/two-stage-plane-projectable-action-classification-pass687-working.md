# The full class of actions projectable to the (y,z)-plane

Date: September 18, 2026.

General complex-threefold cancellation is UNSOLVED; novelty is UNKNOWN.
This is a classification under an explicit subalgebra-preservation
hypothesis, not a classification of every action on the test cylinder.

## 1. Result, including every polynomial stabilization

Let

    R=C[a,b,r,y,z]/(a(y-1)-r^2-b^3, az-y^2+r),
    B_ell=R[u1,...,u_ell], ell>=1, K=C[y,z].

Every automorphism phi of B_ell with phi(K)=K fixes K POINTWISE. It
also preserves R and L_ell=V(a,b,r,y), and sends a to a nonzero scalar
multiple of itself. Every locally nilpotent derivation (LND) delta of
B_ell with delta(K) contained in K annihilates R. In other words,

    {delta in LND(B_ell): delta(K) contained in K}
       ={R-linear LNDs of B_ell}.                          (1)

For ell=1 this class is exactly R*partial_u. For larger ell it is not
being identified with translations having coefficients only in R.
The normalizer conclusion does not assert phi(K)=K for arbitrary phi.

## 2. Every fiber of the supplied plane map

Consider q:Spec R -> A^2, q=(y,z), and let (c,d) be a scalar base point.
If d!=0, eliminating a and setting w=2*d*r+c-1 gives the complete fiber

    w^2+4*d^2*b^3=(c-1)(4*d*c^2+c-1).                    (2)

The inverse is r=(w-c+1)/(2*d), a=(c^2-r)/d. For nonzero right-hand
side, (2) is a smooth elliptic curve minus its unique point at infinity,
and has compact-support Euler characteristic -1. For zero right-hand
side it is a reduced irreducible (2,3)-cusp, with Euler characteristic1.
Indeed its finite bijective normalization is A^1; no multiplicity is
inserted into this topological Euler value.

If d=0, the equations give r=c^2 and a(c-1)=c^4+b^3. For c!=1 this
fiber is A^1_b. At (c,d)=(1,0), the three distinct roots of b^3=-1
give three disjoint copies of A^1_a. Thus q is surjective and all its
fibers are nonempty reduced curves. In particular y,z are algebraically
independent, justifying the notation K=C[y,z].

Put Q=4*z*y^2+y-1 and E=V(z*(y-1)*Q) in the base plane. The full
Euler stratification is

    chi_c(q^(-1)(c,d)) = -1 off E,
                         1 on E minus {(1,0)},
                         3 at (1,0).                     (3)

All three components of E meet only at (1,0): Q at z=0 forces y=1,
and Q at y=1 forces z=0. Multiplication by an affine ell-space leaves
all these Euler values unchanged. Therefore (3) is also the profile
of the map Spec B_ell -> A^2 induced by K.

## 3. The discriminant configuration has trivial plane stabilizer

An automorphism preserving K induces a polynomial plane automorphism
and isomorphisms of the corresponding fibers of q. It must preserve
E, since E is exactly the set where (3) is not -1.

There are two affine-line components, z=0 and y=1. The third component
Q=0 is isomorphic to G_m: its coordinate ring satisfies

    y*(1+4*z*y)=1, z=(1-y)/(4*y^2),

and is exactly C[y,y^(-1)]. Its nonconstant units distinguish it from
either affine line. Consequently any plane automorphism preserving E
fixes the prime ideal (Q) and permutes (z) and (y-1).

Suppose first that it fixes the two line ideals separately. Since the
units in C[y,z] are scalars, it has

    phi(z)=c*z, phi(y)=1+d*(y-1), phi(Q)=e*Q,
    c,d,e in C*.

Comparing coefficients of y, z, and y^2*z in the last identity gives

    d=e, c*(d-1)^2=0, c*d^2=e.

These force d=e=c=1. Thus the plane automorphism is the identity.
If the line ideals are exchanged, its formulas instead have the form

    phi(y)=1+c*z, phi(z)=d*(y-1), c,d in C*.

Then phi(Q) has y*z^2 coefficient4*d*c^2, whereas e*Q has no such
monomial. The required equality is impossible. This proves that the
entire plane stabilizer of E is trivial, with no degree bound on the
original automorphism.

## 4. Lifting the conclusion back to the cylinder

If delta is an LND of B_ell preserving K, its restriction to K is an
LND and its finite exponentials preserve K setwise. Sections2-3 force
each induced plane automorphism to be the identity. Differentiating
the exponential identities gives delta(y)=delta(z)=0. The all-ell
y-fixed theorem685 then implies delta(R)=0. Conversely an R-linear
LND certainly preserves K. This proves (1). For ell=1, an R-linear
LND of R[u] is h*partial_u with h in R, giving the stated exact class.

If phi is an automorphism preserving K, it fixes y by Section3.
Conjugation therefore permutes the ENTIRE set of y-fixed LNDs of
B_ell. The intersection of their kernels is exactly R by685, so
phi(R)=R. This step uses685's all-stabilization statement, not the
one-variable z-rigidity statement of686.

The established equality ML(R)=C[a] in671 gives phi(a)=lambda*a+mu.
The a=0 fiber is the singular cusp y^4+b^3=0 times A^1_z, and each
nonzero a-fiber is A^2. Thus mu=0. The singular locus of a=0 after
stabilization is precisely L_ell, which is consequently preserved.
For ell=1, degree comparison also gives phi(u)=d*u+h with d in C*
and h in R. No such affine-in-free-variables formula is claimed for
ell>1.

## 5. Meaning and verification boundary

The result handles all actions allowing coupled motion of y,z whose
formulas remain in C[y,z]. It proves that no such nonvertical motion
exists. It does not handle formulas involving a,b,r or the added
variables and returning to the full ring rather than to K. The known
nonvertical actions therefore fall outside this projectable class.

The explicit dependencies are the complete proofs671 and685; the
plane-fiber and stabilizer arguments are given here in full. Fresh
root3f9fa5 and independent Jet f01417 verified the coefficient identities
and the latter also checked the full fiber identity and unit formula.
Earlier scratch checks b03537 and e7d200 used structural comparison of
expanded and factored expressions and failed. Replacing it with the
exact test expand(lhs-rhs)=0 passed; the mathematical formulas did not
change. These are supporting checks, not substitutes for the proofs.

No saved checker was executed, imported, compiled or edited. There is
no human peer review, formal certification or novelty clearance. Neither
polynomiality of B_ell nor general cancellation is concluded.

The complete138-line source was held at SHA256
1623ec1e6693467dcc047779736315e4abc2c50cd2010280659547979a2b4829.
Root read it through EOF in e573eb. General(7d3ea5, hash800499),
Geometry(9c919b, hash5e7feb), and Jet(51b6fc/c48434) each read the whole
held source and independently reconstructed the proof. All returned
CLEAN and confirmed the unchanged hash before this provenance-only
addition. These are internal AI reviews, not human or formal review.
