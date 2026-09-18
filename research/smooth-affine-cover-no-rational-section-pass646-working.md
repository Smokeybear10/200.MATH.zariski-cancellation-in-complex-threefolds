# Smooth affine-space covers without rational sections

Date: September 18, 2026. Private working proof. Novelty: UNKNOWN.

The smooth cover in645 has no rational section, even after adding any
number of affine variables, except for the exponent pair (2,2). This
does NOT obstruct cancellation: the same section failure occurs for
an explicit smooth surjection A5 -> A3 between actual affine spaces.
The source and target dimensions match645 exactly.

Everything below is over C. Integers p,q are at least two. A rational
section means a rational map defined on a dense open subset of the
base whose composition with the stated morphism is the identity.
Stabilization means BASE CHANGE along the projection Y x Ak -> Y,
equivalently the morphism g x id: Z x Ak -> Y x Ak. It does not mean
an arbitrary alteration of the base or a different covering map.

## 1. A rational-function obstruction

Let x,w1,...,wk be algebraically independent. If (p,q)!=(2,2), then
there are NO b,c in C(x,w1,...,wk) with

    b^p+c^q=-x.                                      (1)

Here k may be zero. This statement is about affine points. A smooth
projective completion may have rational points at infinity.

First consider the smooth affine curve

    C0={B^p+C^q=-1}.

It is integral: viewed as B^p+(1+C^q), its polynomial is Eisenstein
at any simple root of 1+C^q in C[C]. Its two partial derivatives
cannot vanish simultaneously on the curve. Its smooth projective
completion has genus

    g=(pq-p-q-d+2)/2,    d=gcd(p,q).                  (2)

For completeness, projection to C has degree p. Each of the q simple
zeros of 1+C^q is totally ramified, contributing p-1. At infinity
write C=z^(-1); locally B^p=-z^(-q)(1+z^q). The unit has a p-th root
in C[[z]], so normalization has d branches, each of ramification
index p/d. There is no other ramification. Riemann-Hurwitz gives

    2g-2=-2p+q(p-1)+(p-d),

which proves (2). The characteristic-zero formula used here is
[Stacks, Section53.12](https://stacks.math.columbia.edu/tag/0C1B).
Its displayed derivation was checked; the branch calculation above
is specific to this curve. If p<=q and p=2, then 2g=q-gcd(2,q),
which is positive for q>=3. If 3<=p<=q, using d<=p gives
2g>=(p-1)(q-2)>=2. Thus g>=1 except for (p,q)=(2,2).

A rational map from an affine space to a positive-genus smooth
projective curve is constant. To see this, restrict it to any affine
line through two points of its domain. It defines a rational map
from P1, which extends over the missing points because the curve is
proper and P1 is smooth. A nonconstant resulting morphism contradicts
Riemann-Hurwitz: -2=degree*(2g-2)+nonnegative ramification. Therefore
the two original points have the same image, proving constancy.

Suppose (1) holds. Put l=lcm(p,q) and embed its field into
C(s,w1,...,wk) by x=s^l. In the latter field define

    B=b/s^(l/p),    C=c/s^(l/q).

Then B^p+C^q=-1, so this pair gives a rational map from affine space
to C0 and then to its projective completion. By the preceding argument
B and C are constants in C. On the other hand, b and c are invariant
under s -> zeta*s for every l-th root of unity. Taking zeta primitive
forces B=zeta^(l/p) B and C=zeta^(l/q) C. Both multipliers are
nontrivial, of orders p and q. Consequently B=C=0, contradicting
B^p+C^q=-1. This proves (1) for every number of passive variables.

## 2. Exact section classification for the cover in645

Let m>=2 and

    X={x+x^m y+z^p+t^q=0}.

The map H:A5 -> X in645 has x=-b^p-c^q. On x!=0, the coordinate y
is determined by x,z,t, so C(X)=C(x,z,t). A rational section after
X x Ak would give (1) in C(x,z,t,w1,...,wk). Section1 excludes it
for every (p,q)!=(2,2). In particular, no regular section exists.

For (p,q)=(2,2), the exception is real. On x!=0 choose

    b=(1-x)/2,    c=(1+x)/(2i),    a=0,
    sigma=(z-b)/x^m,    tau=(t-c)/x^m.                (3)

Then b^2+c^2=-x, the h of645 equals one, and its two flow parameters
give the required z and t. Its y is forced by the defining equation.
Thus (3) is a rational section. The same section works after any
affine stabilization. This classifies rational sections of this
particular H for all the parameters of645.

## 3. A three-variable polynomial comparator

Use independent source coordinates a,v,tau and define

    u=1+av,
    C=a-v*tau*u,
    B=u-C.                                          (4)

These polynomials never vanish simultaneously: if B=C=0, then u=0,
av=-1 and C=a!=0, a contradiction. Hence (4) defines a morphism

    R:A3 -> A2 minus {(0,0)}.

It is surjective. For a prescribed pair (B0,C0)!=(0,0), write
u0=B0+C0 and use the following explicit preimages:

    u0!=0,1:  a=1, v=u0-1, tau=(1-C0)/((u0-1)*u0);
    u0=1:     a=0, v=1,    tau=-C0;
    u0=0:     a=C0, v=-1/C0, tau=0.                 (5)

In the third case C0!=0. Each denominator is nonzero in its stated
case. Direct substitution recovers both target coordinates.

The two-by-two Jacobian minors, with rows ordered (B,C), are

    J_(a,v)   =-a-v*tau*u,
    J_(a,tau) =-v^2*u,
    J_(v,tau) =-av*u.                               (6)

If v*u!=0, the second is nonzero. If u=0, then a!=0 and the first
is -a. If v=0, then u=1 and the first is again -a. Thus R has rank
two except exactly at a=v=0. There its image is (1,0), and

    partial_a(B,C)=(-1,1).                          (7)

Now define the single polynomial

    f_pq:A3 -> A1,    f_pq=-B^p-C^q.                (8)

The map g_pq:(A2 minus0)->A1, (B,C)->-B^p-C^q, has nonzero
differential everywhere because p,q>=2 and (B,C)!=(0,0). It is
surjective: for a nonzero value use C=0 and a suitable nonzero B;
for zero use C=1 and B^p=-1. By (5), f_pq is therefore surjective.
Where R has rank two, f_pq has rank one. On its exceptional locus
a=v=0, (7) gives

    partial_a(f_pq)=p!=0.                           (9)

Thus (8) is a smooth surjective morphism of relative dimension two
for EVERY p,q>=2. This is an everywhere assertion, not generic
smoothness or a numerical gradient test.

There is also a direct polynomial-ideal certificate. Let J be the
ideal of the row minors (6). Up to sign its generators are

    j1=a+v*tau*u,    j2=v^2*u,    j3=av*u.

The identity u-1=v*j1-tau*j2 gives

    J=(v^2,a+v*tau).                                (9a)

Indeed u=1 modulo J, so v^2 and a+v*tau lie in J. Conversely all
three j's vanish modulo the ideal on the right. The row is explicitly
unimodular, not just nowhere zero:

    B*(1-v^2*tau)-C*(v-1+v^2*tau)=1.                (9b)

Put P=p*B^(p-1), Q=q*C^(q-1), and I=(f_a,f_v,f_tau). Equation (9b)
implies (P,Q)=(1). Since df=-P*dB-Q*dC, wedging with dB and dC
shows Q*J and P*J lie in I; hence J is contained in I. Modulo J,

    u=1,    a=-v*tau,    B=1+2v*tau,    C=-2v*tau,
    f_a=p+v*(p*(2*(p-1)*tau-1)+4*tau*1_(q=2)).      (9c)

This last element is a unit because v^2=0 and p!=0. Thus I=(1).
This proves exact unit generation of the gradient ideal uniformly
in p,q, without a finite-degree Groebner search.

## 4. Section failure even between affine spaces of the same dimensions

For (p,q)!=(2,2), a rational section of f_pq after any base
stabilization would yield b=B(a,v,tau), c=C(a,v,tau) satisfying (1)
in the base rational function field. Section1 proves impossibility.
In particular, with p=2,q=3,

    f_23 x id_A2: A5 -> A3                          (10)

is a smooth surjection with no rational section, and remains so
after every further affine stabilization. This has exactly the
source dimension, target dimension and relative dimension of645.
Both its source AND its target are affine spaces by construction.

The exponent exception is sharp for this comparator too. When p=q=2,
put B0=(1-x)/2 and C0=(1+x)/(2i). Their sum is generically different
from zero and one, so the first formula in (5) gives a rational
section of f_22. No everywhere regular extension is asserted.

## 5. The actual cylinder supplies a different kind of splitting

An actual isomorphism X x A1 = A4 supplies i:X -> A4 and r:A4 -> X
with r*i=id_X. Such a retraction yields the global algebraic spray

    S(x,w)=r(i(x)+w),    w in A4.

It equals x at w=0, and its w-differential there is surjective since
dr*di=id. This formula does not assert an additive group law, a
family of invertible self-maps, or locally nilpotent derivatives.

It also yields an extension property: every regular map Z -> X
extends to Y for every closed immersion Z -> Y of affine varieties.
Indeed, extend the finitely many coordinates of its composite with
i using O(Y)->O(Z), then compose that extension with r. Conversely,
apply the property to id_X and any closed embedding X -> AN to
obtain a retraction. Thus it characterizes affine-space retracts,
not affine spaces themselves. In particular, if the standard KR
embedding X -> A4 has ANY affine-space retract presentation, it
already has a retraction in that standard embedding, by the same
coordinate-extension argument.

This lifting across CLOSED embeddings is not a section principle
for SMOOTH surjections. Equation (10) is a counterexample even when
the base is A3 and so has every extension property just described.
It follows that lack of a section for645 cannot itself contradict
an affine-space or actual-cylinder hypothesis on its base.

The distinction agrees with [Lárusson and Truong, introduction and
Theorem1](https://arxiv.org/html/1706.00519v3): algebraic subellipticity,
relative ellipticity and homotopy Runge are equivalent there, whereas
the algebraic interpolation property is a different requirement.
For a contractible affine manifold the latter is equivalent to
being a regular affine-space retract. No reverse upgrade from the
smooth covers here to a retract, a global spray, or cancellation
is proved.

## 6. Verification and status

General independently derived the root-of-unity obstruction, genus
formula, sharp (2,2) exception and all-stabilization conclusion.
Jet independently reconstructed those proofs. Jet supplied a smooth
four-parameter cover of SL2 that led to the comparator; root reduced
its top row to the three-variable map (4), and General independently
checked this reduction and all three surjectivity cases. The proof
above uses only the direct minors (6), not that auxiliary SL2 map.
Jet independently reconstructed the reduced map and supplied the
exact ideal certificate (9a)--(9c).

Root's fresh unsaved checks6bc3a4 verified the auxiliary determinant
and tangent formulas; c91e75 verified the row minors, all three
preimage formulas, and exceptional derivative for five exponent
pairs. Jet's fresh530b33 checked the same complete formulas, the
unimodular row, and the ideal-certificate identities, including six
exponent controls for (9c). These finite checks supplement the
uniform proof, not replace it. No saved checker was run, imported,
compiled or modified.

General and Jet then independently read all 255 saved lines at SHA256
3566a2720a0a1c06767c6bef767226741c0300a1a0751743a1557bffc56a664b
and reported CLEAN. General's EOF read was72a581, final hash/count
d1b7e3; Jet's EOF read was7c3c96, final count438b24 and hash a02833.
Both also checked the stated primary-source hypotheses. Root's fresh
15ec26 independently checked the complete unimodular and minor-ideal
identities and six exact residue/unit controls. This final paragraph
updates verification provenance only; the mathematical proof is
unchanged. No formal proof-assistant certification or human expert
review has occurred. A complete novelty audit has not been performed.
General cancellation remains UNSOLVED; novelty remains UNKNOWN.
