# A unit chart and an elliptic obstruction to a specific action construction

Date: September 18, 2026.

General cancellation remains UNSOLVED and novelty UNKNOWN. This note tests
the new quadratic-cylinder symmetry method against the two-stage family671,
at (n,m,q)=(2,2,3). It constructs an exact chart meeting the entire critical
plane and rules out one specific choice of invariants for an escaping LND.
It does NOT rule out other escaping actions or determine polynomiality.

## 1. An exact whole adapted presentation

Write

    R=C[a,b,r,y,z]/(ay-r²-b³-a, az-y²+r), B=R[u].

The capital A below is an auxiliary regular FUNCTION, not this ring R.
Introduce whole polynomial expressions

    V=y+au,
    k=-z-2yu-au²,
    S=k²+u.                                              (1)

Then B has the presentation

    C[a,b,V,k,S]/(F),
    F=a²S+2aV²k+V⁴+a(1-V)+b³.                            (2)

The inverse map is polynomial everywhere:

    u=S-k², y=V-au,
    r=V²+ak, z=-k-2Vu+au².                              (3)

Indeed y²-az=r, and the other original relation becomes -F. Conversely,
r-V²=ak follows from the original relations and(1), without division by a.
The two maps undo one another by direct substitution, so(2) is an exact
presentation, including a=0. No chart has yet been localized.

Define

    A=1-V+2V²k+aS.                                       (4)

The equation is aA+V⁴+b³=0. Thus A is the negative of the regular W=P(V)/a
from672, with its whole expression provided by(4), not by division by a.
The critical plane L0={a=b=r=y=0} has A=1, so all of it lies in B_A.

## 2. The whole A-inverted chart and its inverse

Set

    T=V²S-2Ak.

There is an exact isomorphism

    B_A=C[A,A^(-1),V,b,S,T]/(G),
    G=V²T+b³S+AV+A(A-1).                                (5)

Starting from(2), substitute(4) and T into G: the result is S*F, hence zero.
The inverse formulas are

    a=-(V⁴+b³)/A, k=(V²S-T)/(2A),                        (6)

followed by(3). These use only the declared unit A. Substitution in(4)
gives 1-V+2V²k+aS-A=-G/A, hence recovers the same A on(5). The identity
F=a(1-V+2V²k+aS)+(V⁴+b³) now verifies F=0. Both compositions recover all
generators, proving the chart isomorphism without removing a=0 or V=0.

Precisely, L0 corresponds to

    A=1, V=b=0, T=2z, S=z²+u.                            (7)

Its inverse is z=T/2, u=S-T²/4. Thus no point of that plane is lost.

## 3. A regular escaping tangent field is not locally nilpotent

On the chart(5), define the derivation

    D_H(A)=D_H(S)=D_H(T)=0,
    D_H(V)=3b²S, D_H(b)=-(2VT+A).                         (8)

The two nonzero terms in D_H(G) cancel exactly, so this is a regular
derivation of the chart ring. On(7), D_H(b)=-1: it points out of the
critical plane. Nevertheless it is NOT an LND and does not define a
polynomial additive action.

For a short proof, specialize A=S=T=1. This is a D_H-stable ideal. The
quotient is the affine curve

    V²+V+b³=0, or (2V+1)²=1-4b³.                        (9)

The induced derivation is nonzero, with D_H(b)=-(2V+1). If D_H were locally
nilpotent, so would be that quotient derivation. But the smooth projective
completion of(9) has genus one, whereas a complex affine domain of dimension
one with a nonzero LND has rational function field. This is a contradiction.

Here are elementary reasons for the two curve facts. The right side of(9)
has three distinct roots. The double cover of the projective b-line has
those three branch points and a fourth at infinity. Riemann--Hurwitz gives
2g-2=2*(-2)+4=0, hence g=1. For the LND assertion, an invariant nonconstant
function would make the entire function field algebraic over its invariant
subfield, forcing the derivation to vanish in characteristic zero. Thus the
kernel is C. A last nonzero derivative of an element supplies a nonzero
constant; the preceding derivative divided by that constant is a slice.
The slice theorem makes the curve ring C[s], which has genus zero.

## 4. All LNDs with those three invariants are excluded

More generally, every LND of(5) that fixes A,S,T is zero. These three
functions are algebraically independent: (G) meets C[A,A^(-1),S,T] only in
zero, since every nonzero multiple of G has positive V-degree over the
domain C[A,A^(-1),S,T,b]. Over the fraction field K=C(A,S,T), the presentation
is the nonzero curve ring

    K[V,b]/(TV²+AV+Sb³+A(A-1)).                           (10)

After completing the square it becomes

    (2TV+A)²=A²-4TA(A-1)-4TSb³.                          (11)

Both coefficients on the right relevant to its cubic and constant terms
are nonzero elements of K. Over an algebraic closure of K the polynomial
has three distinct roots; the same branch calculation proves genus one.
It is geometrically integral. An LND fixing A,S,T extends to(10) by invariant
localization, and to its algebraic closure by scalar extension. If nonzero
before localization it remains nonzero, since the ring is a domain. The
curve argument in Section3 therefore forces it to be zero, a contradiction.

Consequently, a nonzero action preserving A must move at least one of S,T.
In fact every chart LND fixes the unit A, since units belong to the kernel
of an LND. Thus every nonzero chart LND must move S or T.
The smooth tangent field(8) cannot be promoted to an additive action merely
because it escapes the plane. Nor may it be multiplied by an arbitrary
non-invariant factor with local nilpotence taken for granted.

## 5. Scope and checks

This is an exact obstruction to the specified invariant choice, not an
all-automorphism invariant-plane theorem. Actions that move S or T have
not been excluded. Global LNDs of B that move A have not been excluded;
they need not extend to LNDs of B_A. The chart
does not extend an isomorphism with affine four-space, and the original
polynomial-cylinder hypothesis is still missing for R.

General derived the adapted variables, complete inverse, critical-plane
image, and genus-one obstruction. Root independently checked the whole
forward/inverse identities, both chart relations, and the tangent equation
in fresh unsaved run7dea87. These support the complete displayed algebra
and curve proof, not a grid-based conjecture. No saved checker was run.

The complete 147-line source was held at SHA256
b8e9bcc00061b3303ba36c29c8d8083e9dd80c61926b542e3d06276e3dfdbcb9.
General (181793/19f246), Geometry (7e883e/98b2c2), and Jet
(aea871/290513) each read it through EOF and reconstructed the proof.
General and Jet returned CLEAN. Geometry agreed with the proof and requested
the explicit global-versus-localized-action distinction now in Section5.
All reviews finished before that clarification and the added independence
explanation; neither changes the theorem. This bounded failed construction
is retained to prevent repeating it as though regularity implied local
nilpotence. It is not represented as an independently novel theorem.
