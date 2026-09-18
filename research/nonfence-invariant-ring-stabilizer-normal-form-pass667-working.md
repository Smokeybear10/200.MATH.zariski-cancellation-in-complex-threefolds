# All automorphisms preserving a non-fence invariant three-ring

Status: complete private proof, two full-source internal reviews passed.
The cancellation conjecture remains UNSOLVED. Novelty is UNKNOWN.

## 1. Hypotheses and the exact normal form

Let k=C and let A be a finitely generated k-domain that is a UFD.
Let D be a nonzero primitive LND of A, with

    C=ker_A D=k[a,b],    pl_A(D)=pC,    p!=0,
    p not in k[g] for any plane coordinate g of C.       (1)

Here primitive means no common nonunit divisor of all its values;
it does not mean that its image ideal is the unit ideal. These are
the explicit non-fence hypotheses of665. In particular p is nonconstant.
Put B=A[u], extend D by D(u)=0, and put E=partial_u and S=C[u].
Assume additionally B*=k*. The actual polynomial cylinder B=k^[4]
has this unit property, but polynomiality is not otherwise needed.

Write N_A(D) for the automorphisms alpha of A with
alpha D alpha^(-1)=cD for some c in k*. Define a lift by

    psi_(alpha,lambda,h)|A=alpha,
    psi_(alpha,lambda,h)(u)=lambda u+h,                  (2)

where alpha belongs to N_A(D), lambda belongs to k*, and h belongs
to C. Its inverse on A is alpha^(-1), and its value on u is
lambda^(-1)(u-alpha^(-1)(h)), so this is an actual automorphism.

**Theorem.** The automorphisms phi of B satisfying phi(S)=S are
exactly the maps

    phi=exp(P(u)D) o psi_(alpha,lambda,h),               (3)

with alpha,lambda,h as above and P in uC[u]. These normalized
parameters are unique. Composition is composition of algebra maps.

No condition LND(A)=CD is assumed. The preservation premise is
SETWISE EQUALITY, not mere inclusion. There is no degree bound on
phi, its inverse, or P. The theorem does not classify automorphisms
that move S to a different embedded subring.

## 2. The inherited inputs and their scope

The full centralizer calculation of
[665](rank-one-abelian-vertical-kernel-rigidity-pass665-working.md)
under (1) gives

    {W in LND(B): [W,D]=0}=C[u]D+CE.                    (4)

Its proof preserves the full plinth pC[u], uses LND divisibility
to kill p, and then applies its non-fence plane lemma. That lemma
says: in any finite-type complex domain containing C, every LND
killing p must kill C. It does not require preservation of C.
The lemma uses the classical Abhyankar--Moh--Suzuki plane-embedding
theorem, with its exact source and orbit-to-smooth-fiber argument
in665. Those are imported dependencies, not new facts established
by this note.

Two more elementary ingredients are recorded to make their use
inspectable. With a local slice r satisfying Dr=p, one has

    A_p=C_p[r],    B_p=C_p[r,u],    Frac(B)=Frac(S)(r).
                                                               (5)

Also, if a rational multiple fD is a regular derivation on B,
then f belongs to B. In reduced UFD form f=h/k, regularity forces
k to divide every D-value on algebra generators, so k is a unit.
Primitivity persists under adjoining u and under automorphisms.
If fD is also primitive, the polynomial f must itself be a unit.

## 3. An S-preserver rescales D and preserves C

Let phi(S)=S and put D'=phi D phi^(-1). It is a primitive LND
with the same kernel S as D. The field description (5) makes
D'=fD on Frac(B), for some nonzero f in that field. The preceding
saturation argument gives f in B. Primitivity of D' makes f a unit,
and B*=k* therefore gives

    phi D phi^(-1)=cD,    c in k*.                      (6)

No claim that phi itself is an exponential is made.

Coefficientwise extension of the full plinth gives pl_B(D)=pS.
Conjugation transports it to pl_B(D')=pl_B(cD)=pS. Hence
phi(p)S=pS, so

    phi(p)=mu p,    mu in k*.                          (7)

The embedded plane C has an intrinsic description inside S:

    C = intersection of ker delta over all
        delta in LND(S) satisfying delta(p)=0.         (8)

Indeed the plane lemma in Section 2 puts C inside every such kernel,
and E|S is among these LNDs with kernel exactly C. Thus the reverse
inclusion follows too. Since (7) rescales p by a nonzero constant,
phi conjugates the set of derivations in (8) to itself. Consequently

    phi(C)=C.                                         (9)

This is not an initial premise. It is the role of the non-fence
condition in upgrading preservation of the three-ring S to preservation
of the original plane.

An automorphism of C[u] that preserves C setwise has the form

    phi(u)=lambda u+h,    lambda in k*, h in C.         (10)

To verify this, untwist the induced automorphism of C and compare
u-degrees of the map and inverse. Both degrees must be one, and
the leading coefficient must be a unit of C. Such units are in k*.

## 4. Removing the entire mixing by one replica exponential

Set E'=phi E phi^(-1). Equation (6) implies [E',D]=0, so (4) gives

    E'=q(u)D+beta E,    q in C[u], beta in C.           (11)

In fact beta=lambda^(-1). Apply E' to (10):
E'(phi(u))=phi(E(u))=1. Since (11) kills C, the left side is
lambda beta, proving the assertion.

There is a unique polynomial P in uC[u] with

    partial_u P=-lambda q.                            (12)

Existence is termwise integration in characteristic zero; the
zero-constant-term condition gives uniqueness. D(P)=0. Thus PD
is LND, and

    tau=exp(PD),    tau^(-1)=exp(-PD)                   (13)

are polynomial automorphisms of the whole B. They fix S pointwise.
No localized exponential or analytic flow is used. Commutation gives

    [PD,E]=-P_u D,    [PD,P_u D]=0,
    tau E tau^(-1)=E-P_u D.

Together with (11)--(12), this reads

    E'=lambda^(-1) tau E tau^(-1).                     (14)

Set psi=tau^(-1) phi. It follows that

    psi E psi^(-1)=lambda^(-1)E.                       (15)

Hence psi preserves ker E=A setwise; let its restriction be alpha.
Since tau fixes u and C, (10) gives psi(u)=lambda u+h. Further,
tau commutes with D, so (6) implies alpha D alpha^(-1)=cD on A.
This proves (3).

For uniqueness, phi fixes the data lambda,h in (10), and E' fixes
q in (11), since D,E are independent over Frac(B). Equation (12)
then fixes normalized P, and alpha is the restriction of tau^(-1)phi.
The normalization is essential: a constant-in-u replica exponential
can otherwise be absorbed into alpha.

## 5. Converse, group caution, and exact construction boundary

Conversely choose the data in Section 1. The lift (2) is an
automorphism and preserves S because alpha preserves C. It also
normalizes D, since D(h)=0. The exponential in (13) fixes S pointwise.
Their composition therefore preserves S, as required.

This is a unique factorization, not an asserted naive semidirect
product with the normalized subgroup exp(uC[u]D). Translating
u by h can create a nonzero constant term in P(u+h); that constant
replica must be absorbed into alpha when normalizing the product.
The larger replica subgroup exp(C[u]D) intersects the lifted intrinsic
normalizer in exp(CD).

The full conjugacy orbit of E under these S-preserving maps is exactly

    { beta E+q(u)D : beta in k*, q in C[u] }.           (16)

The forward inclusion is (11). For the converse take lambda=beta^(-1),
alpha the identity, h=0, and integrate (12). Every field in (16)
has slice beta^(-1)u. Its quotient is isomorphic to A by (14), and

    phi(A)=tau(A).                                    (17)

Thus all polynomial S-preserving changes of the cylinder translation
supply only D as a horizontal direction: subtracting beta E gives
q(u)D, whose u-coefficients and specialization at u=0 are all
C-multiples of D. This excludes obtaining a second independent
intrinsic direction by THAT conjugation-and-coefficient operation.
It does not exclude arbitrary frame repairs, transformations moving S,
other LNDs outside this conjugacy orbit, or cancellation itself.

## 6. A whole-coordinate control showing why non-fence is essential

Take A=k[x,y,z], D=x partial_y+y partial_z, and B=A[u]. This D
is primitive; Section 4.2 of666 proves

    C=k[x,h],    h=2xz-y^2,    pl_A(D)=xC.

The plinth is a fence, so (1) fails. The actual automorphism

    phi(x)=x, phi(y)=y, phi(z)=z+u, phi(u)=u             (18)

has inverse z -> z-u. It centralizes D and preserves
S=k[x,h,u], but phi(h)=h+2xu, so it does NOT preserve C.
Consequently (9) and the theorem's normal form cannot be extended
by merely deleting the non-fence hypothesis.

Directly, if (18) had the normalized form (3), its lambda,h from
(10) would be 1,0. Evaluation at u=0 forces alpha to be the identity,
because P(0)=0. But exp(PD)(y)=y+Px, so (18) would force P=0,
contradicting its nontrivial value on z. This example has polynomial
base and is not a counterexample to cancellation.

## 7. Provenance and unresolved existence

The primitive normalizer argument is inherited. It is already in
[the global-symmetry audit, Section 4](global-symmetry-bridge-literature.md)
for LND flows, and the same-kernel saturation is used in
[coupled25, Section 2](coupled-homotopy-pass25.md). The affine slice
normalizer calculation is the elementary extension of
[intrinsic30, Section 1](intrinsic-symmetry-pass30.md).
[The earlier source audit18, Sections 2--3](polynomial-curve-literature-pass18.md)
records Stampfli and Kuroda predecessors for kernel-fixing automorphisms.
This note does not claim those tools, or all normalizer theory, are new.

The additional assembled conclusion is (3) for ALL setwise S-preserving
automorphisms, obtained using665's intrinsic plane recovery (8). A
bounded archive check found no identical retained statement. This is
not a literature-priority determination or evidence of publishability.

Root reconstructed the proof; General and Jet independently checked
the argument before this complete source was held, including the
converse, normalization sign, uniqueness, and group caution.
Full saved-source review is recorded below. No saved checker has been
executed, imported, compiled, or edited.

This classifies a broad restricted class of coordinate changes. It
does not prove that a useful intrinsic action is supplied by every
actual cylinder. The general existence gap remains open here.

## 8. Completed reviews and exact controls

The complete 240-line held proof had SHA256
cf1be3244b697a47ab9cefa309d54ab9b9733adf3932890779f933c5007f62c9.
Root read it through EOF in01d0d9. General read through EOF and
checked its hash in43bf96, with final hash in8cce12. Jet read through
EOF in6804d8 and rechecked the hash in387bc9. Both separate full-source
reviews were CLEAN. No mathematical changes were requested. Only
status and provenance text changed afterward.

Root fresh unsaved014928, session6735, completed successfully infcca24.
It checked a nonconstant-coefficient replica polynomial, a nontrivial
intrinsic scaling and affine slice change, both whole inverse identities,
D scaling, E conjugation and reconstruction of P by integration. It also
checked the entire fence control (18). General8cce12 and Jetbfb166
independently passed replica and fence-control inverse/conjugation checks.
These are finite exact controls, not tests proving the theorem's universal
quantifiers or verifying a non-fence hypothesis on an unknown cylinder.

Internal AI reviews are not human expert reviews or formal certificates.
