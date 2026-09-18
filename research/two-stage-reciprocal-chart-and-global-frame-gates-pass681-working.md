# A reciprocal chart and exact limits on global coordinate completion

Date: September 18, 2026.

Complex-threefold cancellation remains UNSOLVED and novelty UNKNOWN.
This note concerns the test cylinder from671, not an arbitrary cylinder
known to be affine four-space. It gives an explicit control for the volume
calculation and proves two relative completion obstructions. Neither is
an obstruction to every possible global coordinate system.

## 1. An involution of an ordinary polynomial principal open

Put P0=C[v,b,s,T] and

    h=1+v+v²T+b³s.

The following map is an automorphism of Spec(P0_h):

    iota(v,b,s,T)=(-v/h, b, -s/h, -hT).                  (1)

Indeed substitution gives

    h after iota = 1-(v+v²T+b³s)/h = 1/h.              (2)

Applying (1) twice therefore fixes each of the four coordinates. The map
and its inverse are regular on exactly the stated principal open; no
claim of extension over h=0 is made.

In coordinate order (v,b,s,T), its Jacobian is

    det Jac(iota)=-1/h².                                (3)

Here is a short all-degree calculation. Since b is fixed, use the 3-by-3
minor for (v,s,T). Holding h temporarily constant gives diagonal entries
(-1/h,-1/h,-h), with determinant -1/h. The remaining derivative is a
rank-one correction. With E=v partial_v+s partial_s-T partial_T,
we have E(h)=h-1. The determinant correction is therefore
1-E(h)/h=1/h, proving (3).

Consequently a reciprocal distinguished unit and a polar Jacobian can
occur in a self-isomorphism of a principal open of ordinary affine space.
Those properties alone cannot distinguish a nonpolynomial ambient ring.

## 2. The volume form becomes constant, but one coordinate still has a pole

Use the entire cylinder presentation from676:

    B=C[a,b,V,k,S]/F,
    F=a²S+2aV²k+V⁴+a(1-V)+b³,
    A=1-V+2V²k+aS,  aA+V⁴+b³=0.                       (4)

Here A is a function, not the unknown base ring in the cancellation problem.
By679, B_A=P0_h under

    v=V/A, s=S/A², T=V²S-2Ak, A=1/h.

Apply (1), naming its output coordinates (x,b,y,z). We obtain

    x=-V, y=-S/A, z=-T/A,
    K=z-x²y=2k.                                        (5)

In particular x,b,K are global functions in B, although y and z are
initially functions on D(A). In these variables (4) is exactly

    B=C[a,b,x,K,S]/(a²S+a c+P),
    c=1+x+x²K, P=x⁴+b³, A=c+aS.                       (6)

The new chart polynomial is

    1+x+x²z+b³y = c+P y = A.                           (7)

The ring B is smooth by671 and its polynomial extension. The hypersurface
residue gives a global nowhere-zero top form whose expression on D(a) is

    omega=(da wedge db wedge dV wedge dk)/a².            (8)

This expression uses F_S=a². At other points, the usual expressions
using a nonzero partial derivative of F glue to the same form. Thus (8)
specifies a global form, not a claim that a is everywhere invertible.

On D(aP), (6) gives

    A=-P/a, S=-c/a-P/a², y=-c/P-1/a.

Holding x,b,K fixed, partial_a(y)=1/a². With x=-V and K=2k this yields

    dx wedge db wedge dy wedge dK = 2 omega.

Since K=z-x²y, replacing dK by dz in this wedge changes nothing. Using
(3) now gives, with signs fixed in the indicated coordinate orders,

    omega=(1/2) dx wedge db wedge dy wedge dz
         =-(dv wedge db wedge ds wedge dT)/(2h²).       (9)

Equality on the dense open D(aP) proves equality of rational forms, hence
on their stated domains of regularity. The apparent polar volume factor
in one polynomial ambient chart disappears in the other.

Nevertheless y is not globally regular on B. By679, A=0 is a prime divisor;
on its dense V-invertible chart the residue of S is a free variable, hence
nonzero. Thus -S/A has a genuine pole along this divisor. Likewise T has
residue V²S there, so z has a genuine pole. Equation (9) therefore does
not supply global polynomial coordinates or global coordinate translations.

For perspective, every global LND of B preserves omega. Its flow pulls
omega back to a unit multiple in B[t]; since B*=C*, that unit is constant
and equals 1 at t=0. On the chart, a vector field with coefficients f_i
must therefore satisfy

    sum_i partial_i(f_i)-2 delta(h)/h=0.                (10)

This is only a necessary differential equation. It proves neither global
regularity nor local nilpotence. Four global derivations forming a B-basis
would have chart determinant a nonzero constant times h², since their
evaluation under omega is a unit. The reciprocal chart demonstrates why
the corresponding rational Jacobian condition is not a contradiction.

## 3. No repair preserving the three global functions can work

Let C0=C[x,b,K] inside B and let L=C(x,b,K). This is a polynomial
three-subalgebra: on D(a), (6) eliminates S and identifies B_a with
C[a,a^(-1),x,b,K], so x,b,K are algebraically independent.

There is an exact generic-fiber isomorphism

    B tensor_(C0) L = L[a,a^(-1)].                      (11)

Indeed P is a nonzero element of L, and the defining relation gives

    a^(-1)=-(aS+c)/P, S=-c/a-P/a².

These formulas define both inverse homomorphisms in (11). In particular
this generic fiber is a multiplicative line, not an affine line.

Every C0-linear LND of B is zero. Such a derivation localizes to an LND
over L because it kills every localization denominator. Every LND of
L[a,a^(-1)] kills the unit a, and hence the entire ring. Injectivity of
localization of the domain B then forces the original derivation to vanish.

It follows that there is no w in B with B=C0[w]. Such an equality would
make w transcendental over C0 by dimension and would supply the nonzero
C0-linear LND partial_w. In fact no choice of polynomial generators of
this SAME embedded C0 can be part of a four-variable coordinate system
for B. Any change of B preserving C0 setwise leaves this obstruction
intact. This excludes all such repairs, not just bounded-degree formulas.

The conclusion is strictly relative to the selected subalgebra. For an
explicit control, in the ordinary polynomial ring C[X,B,Y,Z], choose
C1=C[X,B,YZ]. Over L1=C(X,B,YZ), its generic fiber is
L1[Y,Y^(-1)] because Z=(YZ)/Y and YZ is a nonzero unit in L1. Thus it
also has no nonzero C1-linear LND, even though its ambient ring is plainly
polynomial. A different global three-subalgebra is not excluded by (11).

### 3.1. Even retaining only the pair x,b prevents completion

Put H=C[x,b], F1=C(x,b). Equation (6) gives

    B tensor_H F1 = F1[a,a^(-1),K].                     (12)

Its nonconstant unit a proves this ring is not F1^[2]. Consequently
x,b cannot simultaneously belong to a polynomial coordinate system on B,
even after arbitrary changes involving a,K,S. This strictly enlarges the
fixed-triple exclusion. It is still a relative obstruction: the pair
(X,YZ) in ordinary C[X,B,Y,Z] has the same type of generic fiber.

One can classify all attempts to obtain merely an affine-line generic
fiber while retaining this pair. Define

    U=H[a,A]/(aA+P) inside B,
    delta=a partial_K-x² partial_S.

The derivation delta is locally nilpotent on B, since it kills its two
coefficients and preserves (6). Its kernel is exactly U. After inverting
a, its kernel is H[a,a^(-1)]. Moreover U/(a)=(H/(P))[A] embeds in
B/(a)=(H/(P))[K,S] by A=1+x+x²K: H/(P) is a domain and x is nonzero
there, so distinct A-degrees stay independent. Hence U intersect aB=aU.
Clearing powers of a and descending this equality proves ker_B(delta)=U.
It also proves B intersect F1(a)=U. The ring U has H-basis

    1, a^i, A^j for i,j>=1,                              (13)

by aA=-P and independence of distinct Laurent a-degrees after localization.

Suppose f in B is algebraically independent from x,b. The generic fiber
over H[f] is an affine line if and only if

    f=alpha(x,b)*a+beta(x,b), or
    f=gamma(x,b)*A+beta(x,b),                            (14)

with alpha or gamma a nonzero polynomial in H. To prove necessity, in
an affine-line generic fiber the unit a belongs to its coefficient field
F1(f). Thus F1(a) is contained in F1(f), an algebraic extension since both
have transcendence degree one over F1. But F1(a) is algebraically closed
in F1(a,K), so f belongs to F1(a) and F1(f)=F1(a). Now f lies in U. A
Laurent polynomial in a generates F1(a) only if its rational-map degree
is one, so it is alpha*a+beta or alpha'/a+beta over F1. This last statement
also follows by counting its poles at zero and infinity: their total
order is the rational-map degree. Basis (13) gives exactly (14) over H.
Conversely (14) gives F1(f)=F1(a), and (12) then has generic fiber F1(f)[K].

Every projection in (14) is nevertheless nonsurjective. In the first case
choose (x0,b0) with P*alpha nonzero and prescribe f=beta(x0,b0). This
would force a=0, contradicting aA=-P. In the second case use P*gamma
nonzero to force A=0, giving the same contradiction. Thus even all of
these affine-line generic fibers leave missing fibers in the whole map.

### 3.2. Neither x nor b individually can be a global coordinate

For every nonzero lambda, the fiber x=lambda has the presentation

    B/(x-lambda)=C[a,b,W,S]/(aW+b³+lambda⁴),
    W=aS+1+lambda+lambda²K.                             (15)

This substitution is invertible because lambda² is nonzero. The ring
is smooth: off a=0 its S-independent equation eliminates W, and on a=0
the three roots of b³+lambda⁴ are distinct, so the b-partial is nonzero.
Its a-localization is C[a,a^(-1),b,S]. The divisor a=0 has three reduced
prime components, each with multiplicity one. Its divisor class group
is Z³/Z(1,1,1), hence Z².

Here is the exact class-group argument, also used for the next fiber.
Any divisor becomes principal after inverting a, since that localization
is a UFD. Its remaining class is therefore supported on the prime
components of a=0. A relation among these components must be the divisor
of a rational function invertible on D(a). The only units of that
localization are c*a^n, so the sole relation is n times div(a). This
proves both generation and the complete relation lattice.

For every nonzero mu, the fiber b=mu is also smooth: on a=0 its x-values
are the four distinct nonzero roots of x⁴+mu³, so the x-partial is
nonzero; off a=0 eliminate S. Its a-localization is
C[a,a^(-1),x,K]. The four reduced components (a,x-root) have multiplicity
one, giving class group Z⁴/Z(1,1,1,1)=Z³ by the same argument.
Both fiber rings are domains: their equations are primitive and linear
in the eliminated variable, with coefficient a or a² coprime to the
constant term. Their smoothness therefore also identifies these class
groups with their Picard groups.

A polynomial coordinate on B would have every scalar fiber isomorphic
to affine three-space, with zero divisor class group. Thus neither x
nor b is such a coordinate. This does not exclude a different function
mixing either of them with the remaining variables.

## 4. Normalizing the known rank-three action distribution cannot complete it

For this section return to the original671 presentation B=R[u], with

    R=C[a,b,r,y0,z0]/(a y0-r²-b³-a, a z0-y0²+r).

The subscripted names distinguish these coordinates from the chart in (5).
The known commuting LNDs are E=partial_u and

    D(a)=D(b)=0, D(r)=a², D(y0)=2ar, D(z0)=4y0r-a;
    Delta(a)=Delta(r)=0, Delta(b)=a²,
    Delta(y0)=3ab², Delta(z0)=6y0b².

On B_a=C[a,a^(-1),b,r,u] they are a² partial_r,
a² partial_b, and partial_u. Their common kernel in B is exactly C[a]:
the localized common kernel is C[a,a^(-1)], and negative a powers cannot
belong to B because a is a nonunit prime and C embeds in B/(a).

Let K0=Frac(B), M=B D+B Delta+B E, and let

    F0=(K0 M) intersect Der_C(B).

The rational span K0 M consists exactly of rational derivations killing
a, so F0=Der_C[a](B). This is the saturated rank-three distribution.

CLAIM. If W is a global LND of B and [W,F0] is contained in F0, then
W(a)=0. The same conclusion holds if W normalizes only the K0-span,
the module M, or the C-linear span of D,Delta,E.

For each H in {D,Delta,E}, normalization implies [W,H](a)=0. Since
H(a)=0, this says H(W(a))=0. The common-kernel calculation gives
W(a) in C[a]. Restricting the LND W to this subring then shows W(a) is
a constant: a nonconstant polynomial coefficient f(a) partial_a is not
locally nilpotent in characteristic zero, by its iterated degrees.

At every point with a=b=r=y0=0, the differential of the first defining
relation is -da=0 in the cotangent space. Therefore every global
derivation evaluated there sends a to zero. The constant W(a) is zero,
proving the claim. These points exist, with z0,u arbitrary.

In particular no fourth generically independent LND can be appended
while normalizing any of these specified spaces, even without commuting.
Conversely any derivation killing a normalizes F0 by the bracket rule.
Thus for LNDs the normalizer of F0 consists exactly of those killing a.
The whole-cylinder a-moving LND from672 must leave this distribution.
Other rank-three distributions and entirely different global commuting
frames remain possible. This is not a classification of all LNDs of B.

## 5. Evidence, novelty status, and the remaining obligation

The involution and Laurent generic fiber were derived by root and
independently checked by General and Jet before drafting. Jet checked
the volume comparison before drafting; General reconstructed it during
the complete saved-source review below.
Fresh unsaved root calculation b7c3d7 rechecked both involution compositions,
the reciprocal h identity, the exact Jacobian, both Laurent formulas,
the equation in (6), and the residue sign. The symbolic calculation uses
no numerical sampling. Earlier independent checks d13e2b and be78e4
give separate exact evidence for the same identities.
Fresh root78fd75 additionally checked the full delta flow, the first
fiber coordinate replacement, both nonzero discriminants, the original
action relations and brackets, and the critical cotangent calculation.

The all-LND and normalization conclusions use the proofs in Sections3--4,
not finite searches. They depend on the explicitly retained671 domain,
smoothness, units and localization calculations, and679's boundary proof.
General supplied the pair obstruction and complete generic-line
classification in Section3.1; root supplied the single-function fiber
tests in Section3.2. Jet independently strengthened the commuting-frame
obstruction to normalization of the saturated distribution.
The complete320-line source was held at SHA256
bc87485602af10fbeefcedfb351c6c6b3382771ea302138f7f41eb36e2dfe6fd.
General's full EOF reads were f3c9da/2dbe79/be6281, with final hash6b1ec1;
Geometry's were c6d2ba/9abf80, with hash/counta9dd11; Jet's were
f61b70/12fcf1, with final hash86e465. All three returned CLEAN on every
section before this provenance-only and line-wrap update. No mathematical
correction was requested. Jet's independent fresh05fc3f passed the full
involution, determinant, chart, delta, Laurent and first-fiber inverse
checks. An earlier scratch742a2a compared two equal expressions
structurally and failed; replacing that test with exact subtraction gave
the reported pass. It was not a failed mathematical identity.

These deductions have no novelty clearance. Internal AI checking is not
human expert review or formal certification. No saved checker was
executed, imported, compiled or edited.

The active target is still A[u]=C^[4] implies A=C^[3] for the corrected
complex-threefold question. For this test cylinder, neither polynomiality
nor nonpolynomiality has been proved. A successful global construction
must avoid x and b as individual coordinates and change the selected
action distribution. An argument for arbitrary candidates must use their actual polynomial
cylinder hypothesis. The local volume calculation cannot replace it.
