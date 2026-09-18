# Degree-one canonical tops can have arbitrary extra fixed divisors

Date: 2026-09-13.

Even the location of the original nonunit plinth does not control the
primitive top of a globally degree-minimal horizontal. For the fixed
canonical action from passes 28--32, the construction below realizes
every prescribed effective divisor on the punctured \(x\)-line as the
full plinth and fixed-fiber divisor of a primitive degree-one top.
The horizontal and both coordinate maps are actual polynomial objects.

In particular, a bad top can be free along the original divisor \(x=0\)
and fail to have a slice only at other fibers. This disproves the proposed
restriction of bad tops to \(x=0\). All these tops still have rank at most
two, since the horizontal fixes the actual coordinate \(x\).

This is a scoped explicit construction, not a classification of all
degree-one horizontals, a solution of cancellation, or a novelty claim.
The replica flow and pole-contraction mechanisms are standard. The
specific canonical compatibility and its exact consequences are proved
here, with no Jacobian-only inverse assertion.

## 1. Fixed canonical input and the theorem

Retain, without changing the input,
\[
R=\mathbb C[x,y,z],\qquad
D=x^2\partial_y+2y\partial_z,\qquad r=y,\quad p_{\rm in}=x^2,\quad d=x,
\]
\[
B=R[\lambda,w]/((1+\lambda x)w-y)
 =\mathbb C[x,\lambda,w,z],\qquad v=1+\lambda x,
\]
\[
\Delta x=\Delta\lambda=0,\qquad
\Delta w=x^2,\qquad \Delta z=2v^2w.
\tag{1}
\]
The input \(D\) is primitive and has full plinth \(x^2\ker D\).
Thus \(p_{\rm in}\) is nonunit and \(d\) is in its radical but not in
its ideal. These unchanged canonical hypotheses were proved in
[pass 28](canonical-top-pass28.md).

For the full class
\[
\mathcal H_x=\{\delta\in\operatorname{LND}(B):
                   \delta x=0,\ \delta\lambda=1\},
\]
let \(q(\delta)\) be the largest nonzero adjoint order of \(\Delta\)
under \(\operatorname{ad}\delta\). In genuine \(\delta\)-slice coordinates,
this is exactly the degree in \(\lambda\) of the vertical derivation.
[Pass 31](minimal-horizontal-pass31.md) proves on this full class that
\[
\min_{\delta\in\mathcal H_x}q(\delta)=1.
\tag{2}
\]
Its zero-degree exclusion does not impose a triangular-preservation
condition.

Choose any polynomial
\[
p=p(x)\in\mathbb C[x],\qquad p(0)=1.
\tag{3}
\]
The symbol \(p\) below is the chosen *top* plinth, not the fixed input
plinth \(p_{\rm in}=x^2\).
In a second polynomial ring \(\mathbb C[x,\lambda,b,c]\), put
\[
h=x^2c-b^2,\qquad F=p b+x^2h^2,
\]
\[
L=2x^4h\,\partial_b+(-p+4x^2b h)\,\partial_c.
\tag{4}
\]

**Theorem.** There is an actual polynomial horizontal
\(\delta_p\in\mathcal H_x\), given by the two-sided coordinate maps
in Section 2, such that its relative expression for the fixed action is
\[
\widetilde\Delta=D_0-4\lambda x pF L,\qquad
D_0=x^2\partial_b+2b\partial_c.
\tag{5}
\]
Consequently \(q(\delta_p)=1\), so every \(\delta_p\) is a global
degree minimizer in the full class.
The primitive top is \(L\), up to a nonzero scalar, and
\[
\ker L=\mathbb C[x,F],\qquad
\operatorname{pl}(L)=p\,\mathbb C[x,F].
\tag{6}
\]
Its entire coefficient ideal, not just its reduced zero set, is
\[
L(\mathbb C[x,b,c])\,\mathbb C[x,b,c]=(p,h).
\tag{7}
\]
Thus for nonconstant \(p\), \(L\) is primitive, has rank exactly two,
and has no slice. Its reduced fixed locus is the disjoint union
\[
\coprod_{\alpha:\,p(\alpha)=0}
\{x=\alpha,\ c=b^2/\alpha^2\}\simeq
\coprod_{\alpha:\,p(\alpha)=0}\mathbb A^1.
\tag{8}
\]
No such \(\alpha\) is zero. Multiplicities of \(p\) are retained in
both (6) and (7).

Every effective divisor supported away from zero is given by a
polynomial satisfying (3), after scalar normalization. The theorem
therefore permits arbitrary locations and multiplicities away from
the original bad fiber. It does not claim that these are all possible
primitive tops.

## 2. Actual polynomial coordinate maps

We use the sign convention
\[
J_G=G_c\partial_b-G_b\partial_c.
\tag{9}
\]
Then \(D_0=J_h\), \(L=J_F\). Define
\[
H=h-2\lambda x pF^2,\qquad
W=b+4\lambda x^3hF^2-4\lambda^2x^4pF^4,
\]
\[
Z=\frac{H+v^2W^2}{x^2}.
\tag{10}
\]
There are no divisions by \(p\).

### 2.1 Polynomiality of the forward quotient

Modulo \(x^2\), condition (3) gives
\[
W\equiv b,\qquad H\equiv h-2\lambda x b^2,\qquad
v^2\equiv1+2\lambda x.
\]
Since \(h+b^2=x^2c\), it follows that
\[
H+v^2W^2\equiv0\pmod{x^2}.
\tag{11}
\]
Thus \(Z\) is a polynomial in the full ring. The map fixing
\(x,\lambda\) and sending physical \((w,z)\) to \((W,Z)\) is
well defined everywhere, including \(x=0\) and \(p=0\).

### 2.2 The polynomial inverse

In the physical ring of (1), set
\[
I=x^2z-v^2w^2,\qquad F_*=p w+x^2I^2,
\]
\[
h_*=I+2\lambda x pF_*^2,
\]
\[
b_*=w-4\lambda x^3I F_*^2-4\lambda^2x^4pF_*^4,
\qquad
c_*=\frac{h_*+b_*^2}{x^2}.
\tag{12}
\]
Again no inverse of \(p\) occurs. Modulo \(x^2\),
\[
b_*\equiv w,\quad
I\equiv-w^2-2\lambda xw^2,\quad
h_*\equiv I+2\lambda xw^2.
\]
Hence
\[
h_*+b_*^2\equiv0\pmod{x^2},
\tag{13}
\]
so \(c_*\) is a polynomial.

### 2.3 Both inverse compositions, not just the determinant

First treat \(b,h\) as independent variables over \(\mathbb C[x,\lambda]\).
Direct expansion of (10) gives
\[
pW+x^2H^2=p b+x^2h^2=F.
\tag{14}
\]
Using this unchanged \(F\), the inverse identities are
\[
h=H+2\lambda xpF^2,\qquad
b=W-4\lambda x^3H F^2-4\lambda^2x^4pF^4.
\tag{15}
\]
For example, substituting \(H=h-2\lambda xpF^2\) into the
right side of the second identity cancels the two terms of order
\(\lambda\) and the three terms of order \(\lambda^2\).
Conversely the formulas in (15), substituted into (10), recover
\(W,H\). The analogous expansion also gives
\[
p b_*+x^2h_*^2=F_*.
\tag{16}
\]

These identities prove two-sided polynomial inversion on the
independent \((b,h)\)-plane. They can also be viewed as the standard
replica flow preserving \(F\): after inverting \(x\), \(Lh=-x^2p\)
and \(Lb=2x^4h\), and time \(2\lambda F^2/x\) yields exactly (10).
The displayed identities, rather than this localized interpretation,
prove the global inverse.

For the physical maps, (10) makes \(I\) equal to \(H\), so (14)
makes \(F_*\) equal to \(F\). Equations (15)--(16) therefore recover
\(b,h\), after which \(x^2c=h+b^2\) recovers \(c\).
In the other direction they recover \(w,I\), after which
\(x^2z=I+v^2w^2\) recovers \(z\).
Cancellation of \(x^2\) is legitimate in polynomial domains because
both quotients have already been proved polynomial in (11) and (13).
The maps are the identity at \(\lambda=0\).

## 3. Exact intertwining with the canonical action

On the independent \((b,h)\)-plane, the maps (10), (15) have
Jacobian determinant one. This follows either by differentiating
their explicit flow formulas, or directly from (14) and (15).
Under \(h=x^2c-b^2\), the determinant of \((b,h)\) with respect
to \((b,c)\) is \(x^2\). Therefore
\[
J_H(W)=x^2,\qquad J_H(H)=0.
\tag{17}
\]
The sign in (17) agrees with (9):
\(J_H(W)=W_bH_c-W_cH_b\).

Differentiating the numerator in (10) gives
\[
J_H(Z)=2v^2W.
\tag{18}
\]
The independent polynomial inverse from Section 2 and
(17)--(18) show that \(J_H\) is precisely the fixed physical action
(1), not an unrelated action with a similar plinth.

Finally \(p\) and \(x\) are constants for the Jacobian in (9), so
\[
J_H=J_h-2\lambda xp J_{F^2}
   =D_0-4\lambda xpF L.
\tag{19}
\]
All factors in the coefficient of \(\lambda\) are nonzero.
No term of order two or higher occurs.

Transport the actual coordinate partial \(\partial_\lambda\)
through the verified polynomial maps of Section 2. This defines an
actual LND \(\delta_p\) on the physical ring, with
\(\delta_p\lambda=1\), \(\delta_p x=0\), and quotient
\(\mathbb C[x,b,c]\). Equation (19) gives
\[
[\partial_\lambda,\widetilde\Delta]=-4xpF L\ne0,\qquad
[\partial_\lambda,[\partial_\lambda,\widetilde\Delta]]=0.
\tag{20}
\]
Together with (2), this proves genuine global degree minimality.

## 4. Primitive top and its exact kernel

The elementary identities
\[
LF=0,\qquad Lh=-x^2p,\qquad Lb=2x^4h
\tag{21}
\]
show local nilpotence after inverting \(x\): in the actual relative
coordinates \(b,h\), it is triangular. Since \(L\) is already a
polynomial derivation and localization is injective, local
nilpotence descends to the original ring.

The two coefficients in (4) have gcd one. A common irreducible
factor would divide \(x^4h\). It cannot be \(x\), since the other
coefficient is \(-1\) modulo \(x\). If it divides \(h\), the other
coefficient makes it divide \(p\); but \(\gcd(h,p)=1\).
Thus the gcd of the coefficients of the top in (19) is
\(-4xpF\), up to a nonzero scalar, and its primitive part is \(L\).

Let \(K=\mathbb C(x)\). Over \(K\), the pair \(F,h\) is an actual
polynomial coordinate pair: \(b=(F-x^2h^2)/p\) and
\(c=(h+b^2)/x^2\). By (21),
\[
\ker L_K=K[F].
\tag{22}
\]
The stronger pole-contraction calculation below proves the exact
global kernel and the entire second degree module, not just (22).

## 5. Full plinth in every degree and for repeated roots

Write \(p_1=p'(0)\) and put
\[
g(x)=1-2p_1x,\qquad
S=\frac{h+gF^2}{x^2}.
\tag{23}
\]
Since \(F\equiv p b\pmod{x^2}\) and \(gp^2\equiv1\pmod{x^2}\),
the numerator is divisible by \(x^2\). Thus \(S\) is polynomial,
and (21) gives
\[
LS=-p.
\tag{24}
\]
Over \(K\), equations (21)--(23) give
\[
\ker L_K^2=K[F]\oplus K[F]S.
\tag{25}
\]
Here \(\ker L^2\) denotes the kernel of the second iterate, not the
square of the invariant ring.

We claim the precise contraction
\[
\ker L^2=\mathbb C[x,F]\oplus\mathbb C[x,F]S.
\tag{26}
\]
Take an element \(A(x,F)+B(x,F)S\) of (25) that is polynomial in
\(x,b,c\), where the coefficients of \(A,B\) are rational functions
of \(x\). Suppose a coefficient has a pole at \(x=\alpha\).
Multiply by the highest necessary power of \(x-\alpha\) and
reduce modulo that prime. This gives a relation
\[
A_0(F_\alpha)+B_0(F_\alpha)S_\alpha=0,
\tag{27}
\]
with \(A_0,B_0\in\mathbb C[T]\) not both zero.
There are exactly three cases.

If \(\alpha=0\), then
\[
F_0=b,\qquad
S_0=c+\bigl(p''(0)-3p'(0)^2\bigr)b^2+2b^5.
\tag{28}
\]
They are actual plane coordinates, so (27) is impossible.

If \(\alpha\ne0\) and \(p(\alpha)\ne0\), they are again actual
plane coordinates. Indeed from \(F_\alpha,S_\alpha\) recover
\[
h_\alpha=\alpha^2S_\alpha-g(\alpha)F_\alpha^2,\qquad
b=\frac{F_\alpha-\alpha^2h_\alpha^2}{p(\alpha)},\qquad
c=\frac{h_\alpha+b^2}{\alpha^2}.
\tag{29}
\]
All denominators here are nonzero complex scalars.

If \(p(\alpha)=0\), then \(\alpha\ne0\), and
\[
F_\alpha=\alpha^2h_\alpha^2,\qquad
S_\alpha=\frac{h_\alpha}{\alpha^2}
              +\frac{g(\alpha)}{\alpha^2}F_\alpha^2.
\tag{30}
\]
The even part of (27), as a polynomial in the transcendental
coordinate \(h_\alpha=\alpha^2c-b^2\), contains \(A_0\) and the
last term of (30). Its odd part is
\[
\frac{h_\alpha}{\alpha^2}B_0(\alpha^2h_\alpha^2).
\]
It forces \(B_0=0\), then \(A_0=0\), again impossible.

Every possible pole is excluded. This argument does not assume
simple roots of \(p\): at a repeated root it excludes the highest
pole order in exactly the same way. It proves (26), and applying
\(L\) gives both assertions in (6):
\[
\ker L=\mathbb C[x,F],\qquad
L(\ker L^2)=p\,\mathbb C[x,F].
\tag{31}
\]
The second equality is exactly the definition
\(\operatorname{pl}(L)=L(\mathbb C[x,b,c])\cap\ker L\).
No finite jet, bounded-degree search, or fixed-support-only inference
is being used to establish the full plinth.

## 6. Entire fixed scheme and sharp selection consequences

Let \(I_L=(2x^4h,-p+4x^2bh)\).
Its two generators lie in \((p,h)\).
Conversely (24) puts \(p\) in \(I_L\), since every derivative is
a combination of the coefficients of the derivation.
As \(\gcd(p,x^4)=1\), a polynomial Bezout identity and
\(x^4h\in I_L\) then give \(h\in I_L\).
Thus \(I_L=(p,h)\), proving (7).

Modulo \(p\), \(x\) is a unit, so the fixed-scheme ring is precisely
\[
\mathbb C[x,b,c]/(p,x^2c-b^2)
\simeq(\mathbb C[x]/(p))[b].
\tag{32}
\]
This records the multiplicity of each nonzero root of \(p\), not
only the reduced union (8).
On \(x=0\), by contrast, \(L=-\partial_c\).

If \(p\) is nonconstant, a nonzero root exists and the corresponding
fixed points prevent a slice. Since \(x\) is an actual invariant
coordinate, its rank is at most two. A primitive rank-one LND would
be a nonzero constant coordinate partial: in rank-one coordinates
its only coefficient is its coefficient gcd. Such a field has a
slice. Hence this nonsliced primitive \(L\) has rank exactly two.

The constant case permitted by (3) is \(p=1\). It supplies a good
degree-one top in the same family: \(LS=-1\), and there are explicit
relative coordinates, not merely a Jacobian pair. With \(g=1\),
recover
\[
h=x^2S-F^2,\qquad
b=F-x^2h^2,\qquad
c=S-h^2(F+b).
\tag{33}
\]
These polynomial formulas invert \((b,c)\mapsto(F,S)\), so
\(L=-\partial_S\) in actual \(\mathbb C[x]\)-coordinates.

There is also a simple full-class bound independent of this
construction: every horizontal in \(\mathcal H_x\) has an actual
quotient frame \(\mathbb C[x,b,c]\), by the supplied-coordinate
slice projection in [pass 30](horizontal-gauge-pass30.md).
Every coefficient of its relative \(\Delta\), and therefore the
primitive top, kills \(x\). Rank-three primitive tops are impossible
throughout this class, not just at degree one.
This elementary retained-coordinate fact does not force a slice.

For a *supplied* primitive top on this actual relative plane, the
coefficient-ideal test \(I_L=(1)\) is an invariant success test.
Its implication to actual relative coordinates is the already
published comaximal case of Bhatwadekar--Dutta, Theorem 4.7,
applied in [pass 27](relative-completion-pass27.md).[^relative]
It does not prescribe how to find a suitable horizontal on an
unknown quotient. The present family shows that neither minimal
degree, the rank bound, nor testing only the original fiber \(x=0\)
can replace that condition.

## 7. Verification and scope

The companion
[exact checker](minimum_top_structure_checks_pass33.py) checks the
independent-plane forward and inverse identities, the actual physical
quotient remainders, the canonical intertwining, the primitive
coefficients, and the local-slice and residue formulas. Its finite
tests do not quantify over arbitrary \(p\) or prove the pole
contraction. Those assertions are proved in Sections 2--6.

The standalone run passed all eight methods in 2.905 seconds.
The initial run had one assertion-format failure: an expanded residue
was compared with the same polynomial in factored form. Expanding the
expected expression fixed that comparison; no mathematical formula
was changed. Independent full proof reconstructions also checked the
global inverse and all three pole cases.

The local-slice input and global minimum are inherited from the
linked passes. The present construction is an explicit nonlinear
coordinate loop on the auxiliary \((b,h)\)-plane with the necessary
physical divisibility checked in both directions. Nothing here
asserts that an arbitrary stable polynomial threefold admits
\(x\), an appropriate horizontal, or this canonical presentation.
No public priority or novelty claim is made.

[^relative]: Bhatwadekar and Dutta, [*Kernel of Locally Nilpotent R-Derivations of R[X,Y]*](https://repository.ias.ac.in/3203/1/311.pdf), Trans. AMS 349 (1997), Theorem 4.7 and its full proof, pp. 3315--3316, directly reread for this pass. Only the comaximal case gives the additional polynomial-variable conclusion. This criterion is inherited, not proved by a determinant-one assumption.
