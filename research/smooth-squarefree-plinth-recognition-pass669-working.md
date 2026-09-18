# Smooth squarefree full plinth: recognition without a degree restriction

General complex-threefold cancellation remains UNSOLVED. The result here is
conditional on a primitive intrinsic additive action whose FULL plinth divisor
is reduced and smooth. Existence of such an action is not proved. Novelty is
UNKNOWN; the recognition endpoint uses published theorems.

## 1. Statement and separation of hypotheses

Throughout, k=C. Let A be a finite-type factorial k-domain of dimension three,
D a primitive nonzero locally nilpotent derivation, and assume

    C=ker D=k[a,b],       pl(D)=D(A) intersect C=pC,       Dr=p.

Primitive means that D(A) is contained in no nonunit principal ideal of A.
The notation r denotes this actual minimal local slice, not a new coordinate.

**Global presentation lemma.** If, in actual coordinates of C,

    p=P(a)=product_(i=1)^s (a-c_i),       c_i distinct,

then there exists G in k[a,b,T] and an actual element y in A such that

    y=G(a,b,r)/P(a),
    A=C[r,y] = k[a,b,T,Y]/(P(a)Y-G(a,b,T)).                    (1)

The displayed equality with a quotient means the evaluation map is an
isomorphism. Neither stable polynomiality, monicity in T, a quadratic degree
bound, nor principality of higher image ideals is an input to this lemma.

**Conditional recognition theorem.** In addition to the initial hypotheses,
suppose A[u]=k^[4], p is squarefree and V_C(p) is smooth. Then

    A=k[a]^[2]=k^[3]

for a suitable coordinate a of C. No bound on residual degrees is needed.
The established intrinsic quotient and plinth reductions supply the initial
kernel and principality hypotheses for an actual cylinder and a supplied
nonzero intrinsic action; see [27](intrinsic-plinth-boundary-pass27.md).
They do not supply an action with the additional divisor properties.

If p is a unit, the slice theorem already gives A=C[r]. Hence the proof below
concerns nonconstant p. A scalar unit multiplying P can be absorbed by
rescaling r and p together.

## 2. Global presentation over a squarefree fence

Write f_i=a-c_i. The kernel C is factorially closed in A. Its units, and
therefore all units of A, are k*. Every f_i is consequently prime in the UFD A,
and f_i A intersect C=f_i C. Thus k[b] injects into A/f_i A.

Primitivity makes the induced derivation delta_i on A/f_i A nonzero. It stays
nonzero after localizing at k[b] minus zero, since A/f_i A is a domain. The
result is a one-dimensional affine domain over k(b) with a nonzero LND. Its
invariants are algebraic over k(b): an invariant transcendental over k(b)
would make its fraction field algebraic over a field killed by the derivation,
forcing the whole derivation to vanish in characteristic zero. In particular
the image rbar is algebraic over k(b).

The kernel of

    k[b,T] -> A/f_i A,       T -> rbar

is therefore a height-one prime ideal (G_i). Here G_i is irreducible, primitive
as a polynomial over k[b], and has positive T-degree. Gauss's lemma and
characteristic zero imply that G_i is separable over k(b), so

    (G_i)_T(b,rbar) != 0 in A/f_i A.                              (2)

Choose G(a,b,T) by coefficientwise Chinese remainders, with
G(c_i,b,T)=G_i(b,T) for every i. It can have a-degree less than s. Since the
f_i are pairwise comaximal in A, G(a,b,r) belongs to their product ideal PA.
This defines y=G(a,b,r)/P in A, with

    Dy=G_T(a,b,r).                                                (3)

Let H=C[r,y] inside A. The polynomial PY-G is primitive and irreducible in
C[T,Y]: P and G have no common factor, and over Frac(C[T]) it is linear in Y.
Inverting P identifies its quotient with C_P[T]. Since r is transcendental
over Frac(C), evaluation has exactly this kernel. Hence H has precisely the
presentation in (1), prior to proving H=A.

For each i,

    H/f_i H = (k[b,T]/(G_i))[Y].                                  (4)

The coefficient ring in (4) injects into A/f_i A by construction. The map on
the entire ring is injective as well. Indeed, delta_i kills that coefficient
ring, whereas (2)--(3) give delta_i(ybar) nonzero. Thus ybar is transcendental
over its fraction field; any algebraic element would be killed by the
derivation in characteristic zero.

Chinese remainders now give H/PH -> A/PA injective, or

    H intersect PA=PH.                                           (5)

The local-slice theorem gives A_P=C_P[r]=H_P. For z in A choose the least
N>=0 with P^N z in H. If N>0, that element belongs to H intersect PA=PH;
canceling P in A lowers N, a contradiction. Therefore N=0 and A=H. This
proves the global presentation, including its saturation and surjectivity.

## 3. Why the smooth squarefree support becomes a fence

For an actual polynomial cylinder, X=Spec A is smooth and contractible, and A
is factorial. Kaliman's boundary theorem applies to a smooth factorial affine
threefold with H_2(X;Z)=H_3(X;Z)=0. It supplies a quotient-product complement
and a retained boundary curve whose components have normalization A1.[^kal]

Every full-plinth component belongs to this retained curve. At its generic
point, [668, Sections 2--3](squarefree-plinth-divisor-envelope-pass668-working.md)
give the residual fiber L[t], with [L:kappa]>=2. Equivalently its geometric
generic fiber has at least two affine-line components. If the plinth component
were absent from the retained curve, the quotient-product complement would
instead give a single affine line there. This is a contradiction. No equality
between the entire retained boundary and V(p) is needed.

Since V(p) is smooth and reduced, its irreducible components are disjoint and
each equals its normalization. Thus each is A1. The characteristic-zero plane
embedding theorem of Abhyankar-Moh and Suzuki makes one such component a=0 in
actual coordinates C=k[a,b]. On another component, a is a nowhere-zero regular
function on A1 and is therefore a nonzero constant c_i. That component is a
closed irreducible curve in the line a=c_i, hence the entire line. Distinct
components have distinct constants. Consequently p is a scalar times P(a)
with distinct roots, as required in Section 2.

This step has no quadratic-cover hypothesis. It uses the whole boundary theorem
and the full-plinth generic-degree obstruction, not the earlier degree-two
monodromy argument of [47](smooth-plinth-recognition-pass47.md).

## 4. Recognition from the resulting actual presentation

Apply (1). Ghosh, Gupta and Pal's Theorem 4.1(ii) states that stable polynomiality
of this hypersurface makes every residual curve at a simple root an affine
line. Its simple-root clause has no intrinsic Makar-Limanov or Derksen
hypothesis. Abhyankar-Moh-Suzuki then makes each G_i a plane coordinate, and
their Lemma 4.3 yields A=k[a]^[2].[^ggp]

This uses the actual stable-polynomial premise. It does not infer intrinsic
ML(A)=k or DK(A)=A from those invariants of A[u]. Their repeated-root clause
has additional invariant hypotheses and is not silently imported here.

### 4.1. Independent topological reconstruction of the residual-curve step

Once (1) holds, smoothness of X and H_3(X;Q)=0 suffice for this alternative.
Put Sigma_i=Spec k[b,T]/(G_i), E=V_X(P), and U=X minus E. Each Sigma_i is
integral, and

    E = disjoint union_i (Sigma_i x A1),
    U = (A1 minus {c_1,...,c_s}) x A2.                            (6)

These are actual scheme descriptions: the f_i are comaximal and each G_i is
prime. The closed scheme E is reduced.

Each Sigma_i is smooth. Otherwise, at a point where G_i and both of its
partials vanish, choose Y=G_a(c_i,b,T)/P'(c_i). That point annihilates the
equation PY-G and all its partial derivatives, contradicting smoothness of X.

All following cohomology has rational coefficients. Poincare duality on the
smooth real six-manifold X gives H_c^3(X)=H_3(X)=0. Kunneth and (6) give
H_c^4(U)=0, because the punctured affine line has H_c^0=0. The closed-open
compact-support exact sequence therefore implies

    0=H_c^3(X) -> H_c^3(E) -> H_c^4(U)=0,
    H_c^3(E)=direct sum_i H_c^1(Sigma_i)=0.                       (7)

For a smooth connected affine complex curve of completion genus g and q>=1
punctures, dim H_c^1=2g+q-1. Thus every Sigma_i has genus zero and one puncture,
and is A1. Apply the plane embedding theorem and the same Lemma 4.3 to finish.

Equivalently, all a-fibers, including the generic fiber, are A2, and A is flat
over k[a] because it is torsion-free over this PID. The A2-fibration endpoint
requires the local Sathaye theorem together with polynomial-bundle patching;
it is not merely an unqualified assertion that a generic A2-fiber suffices.
The cited Lemma 4.3 avoids adding that separate source dependency here.

## 5. Consequence for every image ideal in this conditional case

After Sigma_i=A1, b is a nonconstant polynomial on that line, so its coordinate
ring is integral and finite over k[b]. Therefore rbar is integral and G_i can
be chosen monic in T. Repeat the interpolation of Section 2 with these monic
generators. Put d_i=deg_T G_i, Q_i=(G-G_i)/f_i, and

    y_i=(P/f_i)y-Q_i(a,b,r).

On D(P/f_i) this gives the exact monic presentation f_i y_i=G_i(b,r).
These opens cover the invariant plane: at a point on f_i=0, P/f_i is nonzero;
off all the components every P/f_i is nonzero. The distinct-degree monic
bases of 668 now give, in every degree n,

    D^n(A) intersect C = product_i f_i^(n-floor(n/d_i)) C.        (8)

Thus the finite point defects of 668 disappear in this smooth-squarefree
recognized case. This consequence can be derived before using the final
recognition theorem. It is not an argument that all squarefree plinths have
principal higher images or polynomial total space.

## 6. Controls and the exact unresolved boundary

A polynomial degree-four control is obtained in k[x,y,z] by setting

    r=xz+y^2,    g=y+r^2/4,
    D=-(xr/2) partial_y + (1+yr) partial_z.

Then Dr=x, Dg=0, and the exact global presentation is

    xz = r-(g-r^2/4)^2.

Conversely y=g-r^2/4 recovers the original variables and relation. This is
an explicit control outside a quadratic-residue restriction, not a new family.
The supplied derivation has gcd of its coefficients equal to one.

The homology/stable-polynomial input is essential. The known hypersurface

    R=k[a,b,r,Y]/(aY-r^2-b^3-1),
    D=a partial_r+2r partial_Y

is smooth and factorial, with kernel k[a,b] and full plinth a. Its exceptional
curve is a smooth elliptic curve with one point removed. In the exact sequence
above H_c^3(U)=H_c^4(U)=0, so H_c^3(Spec R)=Q^2. In particular it is neither
affine three-space nor stably polynomial. Smoothness follows from the gradient
criterion; a is prime and R_a is a Laurent polynomial ring, so factoriality
follows from Nagata's criterion. This is also the hypersurface of GGP's
Example 4.9, not a proposed novel counterexample.[^ggp]

Repeated plinth factors genuinely break Section 2 even on affine three-space.
For example, the published DG control retained in
[622](global-triangular-presentation-cylinder-obstruction-pass622-working.md) has
r=xz-y^2, s=r^2-xy, Dr=x^2, C=k[x,s]. The first modification adds
y=(r^2-s)/x. Its residue map is NOT injective: r+y^2 is nonzero modulo x in
that intermediate ring but equals xz in the actual polynomial ring. The
second modification must add z. This is a failure of the proof mechanism,
not a counterexample to cancellation.

For an unknown nonpolynomial cylinder candidate, every primitive intrinsic
action must therefore have either a repeated full-plinth factor or singular
(including intersecting) reduced support. This is conditional exclusion, not
proof that such candidates cannot exist. A universal existence theorem for
an action avoiding both problems remains missing. The full goal stays open.

## 7. Status, provenance and source licenses

The global presentation and the topology argument were independently
reconstructed by General, Geometry and Jet before this source was assembled.
The complete 256-line source was then held at SHA256
fe5deffca57ba11a91c38764bca4d822534a00dd93188473e7904b76141b965f.
General (30a113/43f42f), Geometry (791e36/183a66), and Jet
(9a2360/b316dc) each personally read the full saved source through EOF and
returned CLEAN. This paragraph is a provenance-only update after all three
reviews; the reviewed mathematical text is unchanged. AI agreement is neither
formal certification nor human expert review.

Compared with retained47, the scope improvement is removing the quadratic and
second-image hypotheses. The rootwise recognition endpoint is published and
was already discussed in retained79 and cubic-literature-pass. No statement
here has a completed novelty audit. No expert contact or submission occurred.
Saved checker scripts remain frozen; any computational controls are fresh,
unsaved identities and do not replace the general proof.

[^kal]: S. Kaliman, [Free C+-actions on C3 are translations](https://www.math.miami.edu/~kaliman/library/Ka.invent.2004.c%2B.pdf), Lemma 2.2 and Theorem 5.2(i). Their hypotheses concern a factorial affine threefold with the indicated smoothness and homology, not an already polynomial threefold. Root reopened both exact statements on September 18, 2026; three independent AI source checks agreed on that scope.

[^ggp]: P. Ghosh, N. Gupta and A. Pal, [On the family of affine threefolds a(x)y=F(x,z,t)](https://arxiv.org/html/2403.17397v2), Theorem 4.1(ii), Theorem 2.8, Lemma 4.3 and Example 4.9. Theorem 4.1(iii), unlike (ii), needs ML(A)=k or DK(A)=A at repeated roots. Root reread the exact clauses and relevant proof text on September 18, 2026.
