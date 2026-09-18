# Three polynomial open charts cover the entire two-stage cylinder

Date: September 18, 2026.

Complex-threefold cancellation remains UNSOLVED and novelty UNKNOWN.
This note strengthens679's one-chart calculation to an explicit finite
atlas of the WHOLE test cylinder. It does not identify that cylinder with
affine four-space, nor produce a counterexample to cancellation.

## 1. Whole translation and the three-chart theorem

Keep the exact presentation from676:

    B=C[a,b,V,k,S]/F,
    F=a²S+2aV²k+V⁴+a(1-V)+b³,
    A=1-V+2V²k+aS, so F=aA+V⁴+b³.                       (1)

It is the cylinder R[u] with

    u=S-k², y=V-au, r=V²+ak, z=-k-2Vu+au².

Translation u -> u+lambda, with the original R coordinates fixed,
induces the WHOLE automorphism tau_lambda of B given by

    a_lambda=a, b_lambda=b,
    V_lambda=V+a*lambda,
    k_lambda=k-2V*lambda-a*lambda²,
    S_lambda=S-k²+lambda+k_lambda².                      (2)

These are polynomial formulas, including at a=0. Their group law is
tau_lambda*tau_mu=tau_(lambda+mu), with inverse tau_(-lambda), because
they are obtained from the stated whole inverse presentation and translation.
The same statements follow by expanding (2). In particular they preserve F.

The translate of A is

    A_lambda=A-4V³*lambda-6aV²*lambda²
                 -4a²V*lambda³-a³*lambda⁴.              (3)

For example this follows from a*A_lambda=-(V+a*lambda)⁴-b³,
after subtracting aA=-V⁴-b³ and canceling the nonzero element a in
the domain B. Alternatively substitution into (1) proves (3) identically
in the ambient polynomial ring, so the formula involves no localization.

THEOREM. The three principal opens

    D(A_(-1)), D(A_0), D(A_1)                             (4)

cover Spec(B), and every one is isomorphic to a principal open subset of
ordinary affine four-space. Thus Spec(B) is uniformly rational: every
point has a Zariski open neighborhood isomorphic to an open subset of A4.

Proof of the cover. Write A_+=A_1 and A_-=A_(-1). Formula (3) gives

    A_++A_--2A=-2a(a²+6V²),
    A_+-A_-=-8V(a²+V²).                                  (5)

Suppose a prime ideal contains all three functions in (4). In the resulting
domain quotient, (5) gives

    a(a²+6V²)=0, V(a²+V²)=0.

If a=0 then V³=0, so V=0. If a is nonzero, a²+6V²=0;
V=0 would contradict a nonzero, while V nonzero also gives a²+V²=0.
Subtracting gives 5V²=0, again a contradiction. Therefore a=V=0.
But (1) then gives A=1, contradicting membership of A in the prime.
There is no such prime, so (A_-,A,A_+)=B. This proves the scheme cover,
not merely a numerical or closed-point test.

An explicit certificate even holds before quotienting by F. Put

    e=a³+6aV²=(2A-A_+-A_-)/2,
    o=V³+a²V=(A_--A_+)/8,
    L=1-2Vk, t=VL-aS=1-A,
    M_a=sum_(j=5)^9 binom(9,j)*(-S)^j*a^(j-5)*(VL)^(9-j),
    M_V=sum_(j=0)^4 binom(9,j)*(-aS)^j*V^(4-j)*L^(9-j),
    C_e=(a²+6V²/5)*M_a-aV*M_V/5,
    C_o=-36aV*M_a/5+(V²+a²/5)*M_V,
    G=sum_(i=0)^8 t^i.

Then the whole polynomial identity is

    1=(G+C_e)*A+(-C_e/2-C_o/8)*A_+
                   +(-C_e/2+C_o/8)*A_-.                 (7)

Indeed a⁵=(a²+6V²/5)e-36aVo/5 and
V⁵=(V²+a²/5)o-aVe/5. The binomial expansion splits as
t⁹=a⁵M_a+V⁵M_V=eC_e+oC_o. Substitution into
1=A*G+t⁹ proves (7). All denominators are nonzero rational constants.

Proof of the chart claim. Each tau_lambda gives an isomorphism
B_A -> B_(A_lambda). Apply679's exact chart to these translated variables:

    T_lambda=V_lambda²*S_lambda-2A_lambda*k_lambda,
    v_lambda=V_lambda/A_lambda,
    s_lambda=S_lambda/A_lambda²,
    h_lambda=1+v_lambda+v_lambda²*T_lambda+b³*s_lambda.

Then

    B_(A_lambda)=C[v_lambda,b,s_lambda,T_lambda]_(h_lambda),
    A_lambda=h_lambda^(-1).                              (6)

No additional subset is removed. The inverse formulas are those in679
applied to the lambda variables, followed by tau_(-lambda). This proves
the theorem, including all points of the previously omitted divisor A=0.

For comparison, D(A_0) and D(A_1) alone do not cover: the point

    (a,b,V,k,S)=(2,-1,-1,-1,0)

satisfies F=A_0=A_1=0. No claim that three is a minimal atlas among
arbitrary choices of charts is made.

## 2. The atlas is not a global polynomial coordinate system

The charts in (6) are principal OPENS in affine four-space, not copies
of all of affine four-space. The transition maps follow from (2) and (6)
and are regular on their overlaps. Their existence does not give four
global functions generating B with a polynomial inverse.

In fact the original679 identification extends in NEITHER direction
as a morphism between its two whole ambient varieties. Along the prime
divisor A=0, the functions V and S have nonzero residues. This follows
from the chart D_V of its boundary ring computed in679, where V is a unit
and S is a free coordinate. Hence v0=V/A and s0=S/A² have genuine poles
of orders one and two. Conversely A=h^(-1) has a pole on the nonempty
h=0 divisor in C[v0,b,s0,T]. Thus this identification gives neither a
polynomial subring inclusion in B nor the reverse whole-ring inclusion.

This does not exclude some DIFFERENT global isomorphism. Also the known
projection forgetting S in (1) already presents B as an affine modification
of C[a,b,V,k]. Kaliman--Zaidenberg, Theorem1.1, describes an already-given
birational morphism as an affine modification; it is not a recognition
theorem making its source polynomial.
[Primary text, Theorem1.1 and proof](https://arxiv.org/pdf/math/9801076).

## 3. A known boundary-normality countercontrol

Boundary singularity alone cannot repair that inference. Poloni gives
smooth and singular hypersurfaces in the SAME polynomial ambient space
with isomorphic complements. For a direct check, put

    P=x²y+z²+xz², Q=x²y+z²+x.

His Lemma3.1 specializes to the following inverse complement maps:

    D(Q) -> D(P): (x,y,z) -> (x/Q, yQ²+Q(xy+1), z),
    D(P) -> D(Q): (x,y,z) -> (Px, (y-xy-z²)/P², z).

Substitution gives P after the first map equal to Q and Q after the second
equal to P; both compositions are the identity. Both hypersurfaces are
irreducible by primitivity and degree one in y. Q=0 is smooth by its
partials. P=0 is singular along x=z=0, a codimension-one line in that
surface, so it is nonnormal. Taking products with A1 gives the same
countercontrol in affine four-space. This is published, not a new result.
[Poloni, Lemma3.1 and Proposition3.4](https://arxiv.org/pdf/1605.05169).

No isomorphism between these particular hypersurfaces or their complements
and our boundary/complement pair is asserted. They disprove only the
proposed general rule that a smooth versus nonnormal boundary must
distinguish polynomial ambient spaces from isomorphic complements.

## 4. Verification, prior scope, and remaining target

Root's fresh unsaved86ff16 checked the WHOLE translation, its inverse,
preservation of F, both identities (5), and the unit ideal using exact
polynomial arithmetic. The elementary prime-ideal argument above is the
all-point proof; the Groebner check is supplementary. Fresh416bfc checked
both complete Poloni maps, their inverse compositions, and the displayed
point omitted by the two-chart subcover. No saved checker was executed,
imported, compiled, or edited.

General independently reconstructed the whole cover and supplied the
finite Bezout certificate (7), checked in fresh unsaved sparse-polynomial
run dbd8d5. Root independently checked that complete identity with exact
symbolic arithmetic in9e79fa. Geometry independently reconstructed the translation
and all-point cover proof before the complete saved-source review.

Uniform rationality is an established notion, not proposed here as a
new invariant. Petitjean's work includes uniform-rationality results for
Koras-Russell threefolds; this explicit cylinder atlas is not claimed to
be absent from prior literature.
[Primary reference](https://arxiv.org/pdf/1505.03108).

The complete193-line source was held at SHA256
f8ab0c120ba87a333336804a0b2388ba59128da052c56cf73ccf319fde71c2ac.
General read through EOF inaaa5b3/675c59 and confirmed the hash in30d048.
Jet read through EOF ind58ce9 and confirmed hash/count in5d0690/55a1d6.
Geometry read through EOF inef6036 and repeated the full read and hash
in5dc607, also rechecking679 in964d91. All three complete reviews returned
CLEAN before this provenance-only update. Jet's fresh exact run c052ee
independently verified the group law, inverse, complete Bezout identity,
omitted point, and both Poloni complement maps. The reviewers also reopened
the relevant primary statements and proofs. No mathematical correction was
required. These are internal AI reviews, not formal or human expert
verification. Novelty clearance remains absent.

The remaining problem is global. A failure of local affine-space charts
cannot obstruct this test cylinder, since (4) covers every point. But no
global polynomial coordinates, no proof of nonpolynomiality of B, and no
resolution of arbitrary complex-threefold cancellation have been obtained.
The original goal remains active and has not been replaced by the atlas.
