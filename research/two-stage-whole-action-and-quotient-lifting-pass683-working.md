# A whole cylinder action, its exact quotient, and a boundary lifting gate

Date: September 18, 2026.

Complex-threefold cancellation remains UNSOLVED and novelty UNKNOWN.
This note completes the denominator calculation left open in672 and tests
one concrete route to an action escaping the exceptional plane. It does
not classify all actions and does not decide polynomiality of the cylinder.

## 1. The entire ring and the action

Use the special case (n,m,q)=(2,2,3) of671:

    R=C[a,b,r,y,z]/(ay-r²-b³-a, az-y²+r), B=R[u].

The whole change of variables of676 is

    V=y+au, k=-z-2yu-au², S=k²+u,
    B=C[a,b,V,k,S]/(F),
    F=a²S+2aV²k+V⁴+a(1-V)+b³.                          (1)

The inverse is u=S-k², y=V-au, r=V²+ak,
z=-k-2Vu+au². Define whole functions, not new independent variables,

    A=1-V+2V²k+aS, T=V²S-2Ak, J=A+2VT.

Thus aA+V⁴+b³=0. The critical plane is

    L=V(a,b,V), B/I(L)=C[k,S]=C[z,u],
    A|L=1, T|L=-2k=2z, S|L=z²+u.                        (2)

Define

    Theta(a)=4b³V³, Theta(b)=0, Theta(V)=-b³A,
    Theta(k)=-b³VS+V²J/2, Theta(S)=AJ.                   (3)

These are polynomial expressions on the WHOLE ring. In the ambient
polynomial ring their derivatives satisfy

    Theta(F)=aJF, Theta(A)=JF, Theta(T)=-2kJF.            (4)

Therefore (3) descends to B and fixes A,T. It is locally nilpotent:
on the redundant generating sequence b,A,T; V; S; a,k, each image depends
only on earlier entries. More explicitly,

    Theta²(V)=0, Theta³(S)=0, Theta⁵(a)=Theta⁵(k)=0.

Finite nilpotence on a finite generating set implies local nilpotence
on every polynomial in that set by the iterated Leibniz rule.

## 2. The clearing exponent is exactly three, with no removable content

In672's b-inverted comparison let sigma denote its auxiliary cylinder
coordinate, to distinguish it from S here. Its functions are

    W=-A, sigma=T/(2b³), delta(V)=W, delta(a)=4V³,
    delta(b)=delta(W)=delta(sigma)=0.

Indeed, with r=V²+ak and

    G=V²+(V⁴+b³)V²/(2b³)-a(V-1)V²/(2b³),

the ambient identity is

    2b³(r-G)-a²T=(2ak-V²)F.

It follows, either on the a-chart and then by injection, or by
differentiating these coordinates, that Theta=b³ delta on B_b.

On L, in the original coordinate order (a,b,r,y,z,u),

    Theta|L=(0,0,0,0,0,1).                              (5)

In particular Theta(u) is not divisible by b. Thus b^e delta cannot
preserve B for any integer 0<=e<3: its u-image would require divisibility
of Theta(u) by b^(3-e). This proves the exact minimal exponent.

The derivation is also primitive, meaning that its images have no common
nonunit divisor. B is a UFD by671 and polynomial extension. The elements
b and V are prime: their quotients have primitive linear equations in S
over C[a,V,k] and C[a,b,k], respectively. Their leading coefficients are
a²; the constant terms are not divisible by a. Also V does not divide A,
since at a=b=V=0 its image is1. Hence

    gcd(Theta(a),Theta(V))=b³

up to a nonzero scalar, while b does not divide Theta(S), whose restriction
to L is1. Dividing common content cannot improve (5).

## 3. The exact whole kernel is a polynomial three-ring

One has

    ker Theta=C[b,A,T].                                  (6)

First compute the localized kernel. In672's comparison

    B_b=C[b,b^(-1),a,V,W,sigma]/(aW-V⁴-b³),

inverting W makes delta=W partial_V, with kernel
C[b,b^(-1),W,W^(-1),sigma]. Removing W-denominators gives
C[b,b^(-1),W,sigma]: the coefficient ring C[b,b^(-1),sigma]
injects into the W=0 quotient, so a minimal negative W-denominator is
impossible. Replacing W,sigma gives C[b,b^(-1),A,T].

It remains to remove b-denominators. B/bB is a domain by Section2.
In its fraction field,

    a=-V⁴/A, T=A(1-V-A)/V²,
    Frac(B/bB)=C(A,V,k).

Here A,V,k are independent, since a,V,k were independent before the
invertible rational substitution a=-V⁴/A. The expression for T is a
nonconstant rational function of V over C(A), so A,T are algebraically
independent in this quotient. Thus C[A,T] injects into B/bB.
If b^(-e)h(b,A,T) belongs to B with e>0 minimal, reduction of h modulo b
must vanish in B/bB, forcing h(0,A,T)=0 as a polynomial. This contradicts
minimality. This proves (6), including its polynomial algebra structure.

The associated morphism pi=(b,A,T):Spec B->A³ has exact closed-point image

    A³ minus {b=A=0, T!=0}.                              (7)

For b!=0, the comparison gives every (A,T). For b=0,A!=0, choose a root
V of TV²+AV+A(A-1)=0, choose any S, and set
a=-V⁴/A, k=(V²S-T)/(2A). These are whole points by676.
For b=A=0, the relation forces V=0 and then T=0. The remaining target
point (0,0,0) occurs at (a,b,V,k,S)=(1,0,0,0,-1).
Consequently this polynomial invariant ring does not give a polynomial
product decomposition of B. In particular Theta has no slice: a slice
would make B=(ker Theta)[s] and pi would be surjective.

## 4. Exact lifting criterion for translations of the third invariant

For ANY q in C[b,A], the derivation q(b,A) partial_T of (6) admits a
regular C-derivation lift to B fixing b,A if and only if

    b³ divides q in C[b,A].                              (8)

Whenever a lift exists, one exists that is locally nilpotent. The
necessity assertion concerns all regular derivations, not just LNDs.

For necessity use the whole identity

    V²T+b³S+AV+A(A-1)=0.

For a proposed lift D, differentiating gives

    b³D(S)+J D(V)+V²q=0.                                (9)

For every lambda in C other than0,1 there are whole B-points with

    b=0, A=lambda, V=2(1-lambda), T=lambda/[4(lambda-1)],
    a=-V⁴/lambda, k=(V²S-T)/(2lambda),

where S is arbitrary. Substitution verifies J=0, and V!=0. Evaluating
(9) therefore gives q(0,lambda)=0 for all such lambda, hence b divides q.
Since B/bB is a domain and J modulo b is nonzero (it is1 on L), reducing
(9) also shows b divides D(V). Write q=bq1 and D(V)=bv1. Division of
(9) by b gives b²D(S)+Jv1+V²q1=0. The identical evaluation and domain
argument gives b|q1 and b|v1. A second division and repetition yields
q=b³q3 and D(V) in b³B, proving necessity. No localization of D is used.

For sufficiency define the whole triangular LND

    Xi(a)=Xi(b)=Xi(V)=0, Xi(k)=a/2, Xi(S)=-V².

It preserves F, kills A, and satisfies Xi(T)=-V⁴-aA=b³. Therefore
(q/b³)Xi is an LND lift when (8) holds, since q/b³ is in its kernel.

Every regular lift in (8) preserves L. Indeed D(b)=0, D(V) belongs to
b³B, and differentiating aA+V⁴+b³=0 gives A D(a)=-4V³D(V).
Since A=1 on L, D(a) vanishes there. Also D(T)|L=0, so the induced
derivation on L fixes z=T/2. In particular neither partial_T itself
nor another translation of this precise form supplies the desired escape.
Actions moving b or A, or not preserving the invariant subring, are not
covered by (8).

## 4a. Classification of every LND preserving this invariant subring

The preceding gate extends to a complete classification under the single
extra hypothesis D(H) contained in H, where H=ker Theta=C[b,A,T]:

    {D in LND(B):D(H) contained in H}
        = {q(b,A) Xi+h(b,A,T) Theta:q in C[b,A], h in H}. (11)

Include the zero derivation on both sides. In particular EVERY such
projectable action preserves L and fixes z there. This hypothesis is not
automatic for a whole action of B.

First the fibers of pi force D(b)=D(A)=0. Off bA=0, the comparison gives
a literal A¹ fiber. On A=0,b!=0 it gives four disjoint reduced A¹ fibers,
one for each root of V⁴=-b³. On the dense open subset of b=0 defined by

    A*T*(A²-4TA(A-1)) != 0,

the chart equation gives two disjoint reduced A¹ components, corresponding
to the two roots of TV²+AV+A(A-1). Thus the closure of the set of base
points with fiber not isomorphic to A¹ is exactly V(bA). Empty or
nonreduced special fibers do not change this closure.

The hypothesis makes exp(tD) preserve H in both directions, so pi is
equivariant for the induced action. Consequently the radical principal
ideal (bA) of this closed locus is stable and D(bA) is divisible by bA.
For an LND on a domain, D(f) in fB implies D(f)=0: otherwise D-degree
of D(f) is deg_D(f)-1 whereas degree of its nonzero multiple f*g is
deg_D(f)+deg_D(g). Additivity of D-degree also shows that D(bA)=0 forces
D(b)=D(A)=0. On C(b,A)[T], a locally nilpotent derivation therefore has
D(T) independent of T. Since D(T) belongs to H, it is in C[b,A].
Section4 now implies D(T)=b³q(b,A) and preservation of L and z.

For the full classification, such a D commutes with Theta. To justify
this, conjugation by exp(tD) takes Theta to a primitive LND with the SAME
kernel H. Any two such LNDs are scalar associates: over Frac H they are
constant multiples of partial_V on the generic polynomial line, and
primitivity in the UFD B forces their ratio to have valuation0 at every
prime. Thus the ratio belongs to B*=C*. For the polynomial conjugation
family the scalar is a polynomial function of t, never zero, hence is
constant; at t=0 it is1. Differentiating proves [D,Theta]=0.

The explicit formulas give [Xi,Theta]=0 on B. Put K=D-qXi. This regular
derivation kills H; over Frac B its space of such derivations is one-
dimensional, so K=hTheta for h in Frac B. Primitivity and regularity imply
h belongs to B: at every prime some Theta-image is a unit in the
corresponding local DVR, forbidding a negative valuation of h. Commutation
then gives Theta(h)=0, hence h belongs to H. This proves necessity in(11).

Conversely every displayed derivation is whole and, on the injective
localization

    B_(bA)=C[b,b^(-1),A,A^(-1),T,V],

has the triangular form

    b³q(b,A) partial_T - b³A h(b,A,T) partial_V.

It is locally nilpotent there and therefore on the stable subring B.
Its restriction to L is h(0,1,2z) partial_u, as also follows from(5).

## 5. All orbits of the explicitly generated action group

Let E=partial_u, and use the two whole LNDs D,Delta of671:

    D(a)=D(b)=0, D(r)=a², D(y)=2ar, D(z)=4yr-a;
    Delta(a)=Delta(r)=0, Delta(b)=a²,
    Delta(y)=3ab², Delta(z)=6yb².

Both kill u. Let G be the subgroup generated by the complete flows of
D,Delta,E,Theta. Then G has one orbit Spec B minus L, and its orbits in
L are exactly the u-lines with z fixed.

For a=xi!=0, the literal coordinates b,r,u identify the fiber with A³.
D,Delta,E give its translations, so the subgroup is transitive there.
The whole polynomial curve

    (a,b,V,k,S)=(-v⁴-1,1,v,-v³/2,-v)

has A=1,T=0, and Theta translates v with speed -1. Its a-coordinate
takes every complex value, connecting all nonzero a-fibers. At a=0
outside L, both b and y=V are nonzero, so Theta(a)=4b³V³!=0; a suitable
flow parameter moves such a point to a!=0. This proves the single orbit.
On L, D and Delta vanish, while E and Theta are partial_u. Thus all
words preserve z there, and E reaches the entire claimed line.

At the curve point v=1, D,Delta,E span ker(da), and Theta(a)=4.
Transporting this frame by G shows that tangent spaces on the open orbit
are spanned by LNDs conjugate to the displayed ones. No assertion about
the full special automorphism group or its orbits follows.

## 6. Replicas and conjugated sliced kernels still miss the cylinder variable

Enlarge G to G_rep by including the flows of u^jD and u^jDelta for every
integer j>=0. These are LNDs because D and Delta kill u. Define

    H_G=C[g(R):g in G_rep],
    C_G={h in B:hB is contained in H_G}.

Each g(R) is the kernel of the sliced LND g E g^(-1). Thus H_G is
contained in the algebra generated by ALL sliced LND kernels, but need
not equal it. Every generator of G_rep preserves L and fixes z there.
Consequently the restriction of H_G to L is exactly C[z], so u is not
in H_G. This exclusion concerns every finite word, with no degree bound.

The exact support of its conductor is

    sqrt(C_G)=I(L).                                      (10)

To prove it, put I=(a²,ar,4yr-a,ab²,yb²) in R. The algebra H_G is
G_rep-stable. For f in R, expansion of exp(t u^jD)(f) and interpolation
in finitely many distinct scalar t give u^jD(f) in H_G; the same holds
for Delta. The displayed coordinate images, multiplication by R, and
summing over j give IB contained in H_G. Since IB is an ideal of B,
it is contained in C_G. Its radical is I(L): a² forces a=0, then r=y²,
4yr-a forces y=r=0, and b³=-y⁴ forces b=0. Conversely I vanishes on L.
If h is in C_G, both h|L and (hu)|L lie in C[z]. Their equality
(hu)|L=u(h|L) in C[z,u] forces h|L=0. Hence

    IB contained in C_G contained in I(L),

which proves (10). The replica hypothesis is essential to the inclusion
IB contained in H_G; it is not silently asserted for the smaller G.
Neither (10) nor the orbit result proves that all sliced kernels miss u.
Both conclusions remain true if G_rep is enlarged by the flows of ALL
actions in(11): those flows still preserve L and fix z there, and the
replicas establishing the lower conductor inclusion are still present.

## 7. Evidence, scope, and remaining obligation

Root's fresh unsaved aa9d56 verifies (4), the comparison identity, every
original-coordinate residue in (5), the whole invariant curve and its
translation speed, and the nilpotence bounds. The preceding attempt
09203e stopped on a Python integer's missing .subs method; the harness
was corrected and the full rerun passed, with no mathematical assertion
failure. Fresh root1986d2 verifies the entire Xi flow, the branch-point
family, and all required identities. Jet independently checked the action
in157a57 and General in116f5e. The all-q divisibility, kernel descent,
orbit and conductor arguments are proofs, not finite-sample inferences.

The original259-line source passed full independent reviews before the
addition of Section4a. Its held SHA256 was
2d4e210b11de2a4ac2e0ec621ddbc66cb1ce4f048e176e072db5d295752ce932.
General read ebd2fb/74e09a, Geometry6cba6c and Jet a74a01 through EOF;
all returned CLEAN with unchanged hashes. The expanded328-line source
was then held at SHA256
02baefc7d347ae449ac6ee4d36b4e71c4c3249157687b65e74131618a2cdd83b.
General(4dbe92,935173,cbaf29), Geometry(718d1d), and Jet(00c9fb,19e640)
each read it through EOF and returned CLEAN, including the classification.
Their final hash receipts f603f1,d563a2,55b5b5 confirm unchanged source.
Root read the added complete tail inbafe4c and unchanged opening indb4fb9.
Fresh rootdb4fb9, Geometry239e98, and Jet7911b4 independently checked the
whole Xi/Theta commutator; root also verified the explicit bA-chart used
for triangular sufficiency. All reviews finished before this provenance-
only update. Saved checkers remain frozen. No
novelty, human expert verification, or formal proof certification is
claimed. The next action search must leave the bounded groups and the
quotient-translation lifting mechanism above. The actual polynomial-
cylinder premise of cancellation has still not been established for R.
