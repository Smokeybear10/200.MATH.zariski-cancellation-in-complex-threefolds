# A birational test for principal retractions and a transfer countercontrol

Date: September 18, 2026. Private working proof. Novelty: UNKNOWN.

A retraction with nonzero principal kernel becomes the actual polynomial
product projection if its image is factorially closed and its kernel
generator also generates the relative function field. Neither an
existing cylinder elsewhere nor factorial closure alone supplies that
second condition. Explicit retractions of an actual affine space below
have factorially closed polynomial images but generic fibers of every
positive genus. They admit no compatible nonzero ambient additive action.

This is a recognition test for a SUPPLIED retraction and a counterexample
to automatic transfer of structure. It does not construct the required
retraction for an unknown cancellation candidate, make it birational,
or solve cancellation.

## 1. An elementary principal-kernel criterion

Let A be a subring of a domain B, with a ring retraction

    rho:B -> A,    rho|A=id,    ker(rho)=sB,    s!=0.

All rings are commutative and have identity; the maps preserve it.
Recall that A is factorially closed in B if bc in A minus{0}, for
b,c in B, implies b,c in A. Then the following are equivalent:

    (i)   B=A[s], a polynomial ring in the supplied s;
    (ii)  A is factorially closed in B and
          Frac(B)=Frac(A)(s).                         (1)

No UFD, normality, finite-generation or characteristic assumption
is needed for this assertion.

First s is transcendental over A. A relation sum a_i*s^i=0, a_i in A,
gives a_0=0 after applying rho. Cancel the nonzero s and repeat to
obtain every a_i=0. The same statement holds over K=Frac(A).

Assume(ii) and put C=(A minus{0})^(-1)B. Its units are exactly K^*.
Indeed a unit b/a with inverse c/d satisfies bc=ad in A minus{0}.
Factorial closure puts b,c in A, so b/a is in K^*. The reverse
inclusion is immediate.

By the field equality in(ii),

    K[s] contained in C contained in K(s).

For any element p(s)/q(s) of C in relatively prime form over K[s],
Bezout gives polynomials v,w in K[s] with vp+wq=1. Hence

    v*(p/q)+w=1/q belongs to C.

Thus q is a unit of C, so q belongs to K^*. It follows that every
element of C is a polynomial in s, and C=K[s]. This step uses the
field equality, not merely the fact that the relative field is
rational with some unspecified parameter.

Extend rho to C by rho(b/a)=rho(b)/a. On K[s] it is evaluation at
s=0. For b in B, considered now as a polynomial in s over K, its
constant coefficient rho(b) lies in A. Since

    b-rho(b) belongs to ker(rho)=sB,

the quotient b_1=(b-rho(b))/s lies in B and has strictly smaller
s-degree unless b is constant. Repeat. The process terminates at
the finite polynomial degree, and every coefficient of b lies in A.
This proves B=A[s]. Conversely, in a polynomial ring over a domain,
the degree of a nonzero product is the sum of the degrees. A is
therefore factorially closed, and the field equality is immediate.

Geometrically, when A and B are finitely generated over a field,
(1) tests whether the map (r,s):Spec(B) -> Spec(A) x A1 is an
isomorphism. Its birationality together with factorial closure is
sufficient. No birationality assumption is automatically supplied
by extending coordinate functions of a closed embedding.

## 2. Retractions with factorially closed image and positive-genus fibers

For each integer g>=1 work in

    B=C[x,y,z,t],    F_g=x+y+x^(2g)*y^2,
    A_g=C[F_g,z,t].

Define the ring endomorphism

    rho_g(x)=F_g,  rho_g(y)=0,  rho_g(z)=z,  rho_g(t)=t.  (2)

The corresponding point map is (x,y,z,t) -> (F_g,0,z,t).
Evaluating y=0 proves that F_g,z,t are algebraically independent.
Also rho_g(F_g)=F_g, so rho_g is idempotent with image A_g.
If rho_g(b)=0, let h(x,z,t)=b(x,0,z,t). Then h(F_g,z,t)=0, and
independence forces h=0. Thus

    A_g is a polynomial three-ring,    ker(rho_g)=yB.    (3)

This is literally a transfer from the trivial cylinder projection
p=(x,0,z,t) by the polynomial map

    G_g=(F_g,y,z,t),    rho_g=p composed with G_g

on points. The map G_g restricts to the identity on y=0. Its
Jacobian determinant is 1+2g*x^(2g-1)*y^2, which is one along the
whole hyperplane but is not a unit of B. Thus G_g is etale along
the hyperplane, but is not a polynomial coordinate automorphism.

## 3. Prime preservation and factorial closure

Fix ANY irreducible H(U,z,t) in C[U,z,t]. Put

    S=C[U,z,t]/(H),    K_H=Frac(S),    u=U mod H.

Then S is a domain and

    B/(H(F_g,z,t)) = S[x,y]/(x^(2g)*y^2+y+x-u).        (4)

In a degree-compatible monomial order on x,y, the relation in(4)
is monic with leading monomial x^(2g)*y^2. Division by this one
monic polynomial shows that the quotient is S-free on the monomials
not divisible by x^(2g)*y^2. Spanning is division; uniqueness follows
because every nonzero multiple of the relation has leading monomial
divisible by x^(2g)*y^2. In particular (4) injects into its
localization over K_H.

Over K_H[x], the same polynomial is a primitive quadratic in y,
whose discriminant is

    1-4*x^(2g+1)+4*u*x^(2g).                         (5)

It has odd x-degree 2g+1 with leading coefficient -4 for EVERY u.
Its valuation at infinity is odd, so it is not a square in K_H(x).
Quadratic irreducibility and Gauss's lemma show that the localized
quotient is a domain. Therefore (4) is a domain, and H(F_g,z,t)
is prime in B.

Every irreducible of A_g remains prime in B. Since A_g and B are
UFDs with the same units C^*, unique factorization of a nonzero
element of A_g proves that every factor of it in B lies in A_g.
Consequently A_g is factorially closed in B. This argument handles
every irreducible H, not only special fibers F_g=c.

## 4. The generic genus excludes every compatible ambient LND

Let K=C(U,z,t), identifying U with F_g. The generic fiber of
Spec(B) -> Spec(A_g) has function field

    K(x,y),    x^(2g)*y^2+y+x-U=0.

With W=2*x^(2g)*y+1 this becomes

    W^2=1-4*x^(2g+1)+4*U*x^(2g).                     (6)

The right side is squarefree over K. To see this uniformly, its
specialization at U=0 is 1-4*x^(2g+1), which has no common zero
with its derivative. The discriminant in U is therefore not the
zero polynomial. Over an algebraic closure of K the double cover
of P1_x is branched at its 2g+1 simple finite roots and at infinity.
Riemann-Hurwitz gives

    2*genus-2 = 2*(-2)+(2g+2),    genus=g.             (7)

Odd degree also shows geometric irreducibility. Thus its smooth
projective function-field model has positive genus.

Suppose a nonzero locally nilpotent derivation of B annihilates
A_g. It stays nonzero and locally nilpotent after localizing by
A_g minus{0}, and after extending constants to an algebraic closure
of K. It gives a nontrivial additive action on an integral curve,
and hence a nonconstant orbit A1 -> that curve. Extending to the
smooth projective model gives a nonconstant P1 map to a curve of
positive genus, contrary to Riemann-Hurwitz. Therefore

    no nonzero D in LND_C(B) annihilates A_g.          (8)

This concerns B itself and this image subring. No analogous rigidity
after adding extra polynomial variables is asserted; translations
in new variables would already contradict such a statement.

For g=1 there is an even simpler obstruction to a normal derivation.
Any polynomial derivation T killing F_1,z,t and satisfying T(y)=1
would give

    (1+2*x*y^2)*T(x)=-(1+2*x^2*y).

At x=-1/2,y=1 this reads 0=-3/2, impossible. Thus even an ordinary
polynomial derivation with these specified properties does not exist.

## 5. Exactly which hypothesis the transferred example loses

The map G_g is generically finite of degree 2g, not birational.
Indeed, over L=C(y,z,t), F_g is a degree-2g polynomial in x.
The polynomial y^2*X^(2g)+X+y-U is irreducible in L(U)[X]: its
ideal in L[X,U] gives the domain L[X], and Gauss's lemma applies.
Hence

    [C(x,y,z,t):C(F_g,y,z,t)]=2g.                     (9)

The image is factorially closed and the kernel is principal, but
Frac(B) does not equal Frac(A_g)(y). Section1's missing field
condition is therefore explicit, rather than an unspecified failure.
The ordinary projection p remains a perfectly good product
retraction of the same hyperplane. The example does not obstruct
choosing a DIFFERENT retraction; it refutes automatic preservation
by the chosen extension, even if factorial closure survives.

For the cancellation problem, a genuine cylinder has its own sliced
locally nilpotent derivation and product projection. Transferring
only the projection to a different hypersurface embedding does not
transfer those properties for free. Criterion(1) does not furnish
a method of choosing a successful extension, and must not be used
as a replacement for that missing existence argument.

## 6. Sources, deduplication and verification scope

The retained[74](quadratic-slice-projection-pass74.md) already shows
that a polynomial retract with principal kernel need not be a slice
projection, using a non-factorially-closed image. The family here
also has factorial closure and excludes EVERY compatible ambient
LND. The retained[38](literature-scope-pass38.md) records the distinct
invariant-kernel criterion from Chakraborty, Dasgupta, Dutta and
Gupta, [Proposition4.2 and Corollary4.3](https://arxiv.org/html/1910.11023).
Those statements require an actual additive action; factorial
closure does not replace it. Root reread the displayed proposition,
proof and corollary in the current primary HTML source. No priority
claim is inferred for either this family or the elementary criterion.

There is an exact antecedent for the last step of Section1: Das and
Dutta, [On codimension-one A1-fibration with retraction](https://arxiv.org/abs/1302.5223),
Lemma3.6 and Remark3.7, already prove that a generically polynomial
algebra with a principal retraction kernel is the polynomial ring
in that kernel generator. The repeated-division proof above
reconstructs that step. Our unit/Bezout argument supplies its
generic-polynomial premise from the stated field equality and
factorial closure. Geometry located the antecedent; root read the
whole displayed lemma, proof and remark in the author-uploaded
[full text](https://www.researchgate.net/publication/267127854_On_codimension-one_A1-fibration_with_retraction)
and again in the [primary arXiv PDF](https://arxiv.org/pdf/1302.5223),
printed p.8. This paper and lemma were already examined in the
retained[104 source audit](cyclic-conic-retraction-obstruction-pass104.md),
which emphasized the separate codimension-one patching criterion.
This is renewed application and attribution, not a newly discovered
paper. No claim that the combined criterion or comparator is
historically new has been established.

The characteristic-zero curve calculation uses the explicit
[Riemann-Hurwitz formula](https://stacks.math.columbia.edu/tag/0C1B),
whose statement and derivation were read directly. The necessary
branch count and genus in(7) are proved here for this particular
function field.

General constructed and proved the genus-one comparator; Jet
independently reviewed all its algebraic claims. Root's fresh21b11c
and Jet's fresh613e4a checked its whole identities and discriminants.
Root's fresh77cab8 checked six genus controls without running or
importing any saved checker. The uniform genus and all-prime claims
rest on the written proofs, not those finite controls. Root supplied
the arbitrary-genus extension and the elementary criterion in1.

General and Jet each read all242 saved lines through EOF at SHA256
e319c0ad60c5423e3aaa58fedc3403c3277b5de47c5df40c6dfb565ad715738d
and reported CLEAN. General's EOF2bfadf, count2077b4 and hash213cd8,
and Jet's EOFc7333f, count2e38c7 and hash24fa9f, cover every proof
and scope boundary. Root's complete saved-source read was469dc9.
The subsequent source-attribution and final-paragraph additions
change no mathematical assertion.

These are separate AI-assisted checks, not human expert review or
a formal proof-assistant certificate. The supplied-product criterion
is not a proof that an unknown base is affine three-space. The full
cancellation goal remains UNSOLVED; novelty remains UNKNOWN.
