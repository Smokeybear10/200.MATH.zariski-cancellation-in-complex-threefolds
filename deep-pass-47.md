# Second-image basepoints and smooth-plinth cancellation

Under the established quadratic-divisor hypotheses, a smooth reduced
primitive plinth divisor now forces the unknown cylinder factor to be
affine three-space. The proof first confines the second-image obstruction
to the singular locus of the full plinth polynomial, then gives explicit
coordinates when that locus is empty.

This is a conditional recognition theorem, not the unrestricted
complex-threefold cancellation conjecture. The hypotheses concern the
still-unrecognized degree-two branch of a supplied coordinate frame.
Neither every cancellation candidate admitting that frame nor all
singular and nonreduced plinth cases has been proved.

## 1. The working problem and the exact quadratic assumptions

The working question is
\[
A[s_*]\simeq\mathbb C^{[4]}
\quad\Longrightarrow\quad
A\simeq\mathbb C^{[3]}.
\tag{1}
\]
It is the corrected complex-threefold interpretation of the supplied
conjecture, not a professor-confirmed interpretation of its dimensional
typo. Nothing here asserts a theorem in arbitrary dimension or over
arbitrary fields.

In the quadratic branch, a nonzero primitive intrinsic locally nilpotent
derivation \(D\) has polynomial invariant plane
\[
C=\ker D\simeq\mathbb C[U,V],\qquad
D(A)\cap C=pC,\qquad Dr=p.
\tag{2}
\]
The ring \(A\) is smooth and factorial, and \(C\subset A\) is faithfully
flat. These properties are established on the actual unknown ring.
The polynomial cylinder also makes its complex points contractible.

Write \(L=\operatorname{Frac}C\). The full generic algebra is \(A_L=L[r]\).
At every prime factor \(\pi\) of \(p\), the prior argument gives the
entire local algebra
\[
A_{C_{(\pi)}}=
C_{(\pi)}[T,Z]/(\pi^n Z-T^2+\eta),\qquad
DT=\pi^n,\quad DZ=2T,
\tag{3}
\]
after an invariant unit normalization. Here \(n=v_\pi(p)\), and the
residue of \(\eta\) is a nonzero nonsquare. At the other base divisors
the local algebra is a polynomial line.

The local rings in (3) are embedded in the same generic line. Their
intersection is exactly \(A\). The previous proof also establishes
\[
F_1=C\oplus Cr,\qquad
I_2:=D^2(A)\cap C=pJ,\qquad
p\in J,\qquad J_{(\pi)}=C_{(\pi)}
\tag{4}
\]
for all base prime elements. Thus a proper \(J\) has finite support.
The equality \(J=C\) is equivalent to one full global equation
\(pY=r^2+ar+b\), not merely a subalgebra with that relation.

The full assumptions, valuation correction and global equation
equivalence remain in the frozen
[local-model proof](research/minimal-quadratic-slice-pass46.md) and
[second-image proof](research/second-image-gluing-pass46.md).

## 2. A basepoint is exactly a scalar scheme-theoretic slice

For a closed point \(\mathfrak m\) of the invariant plane,
\[
J_{\mathfrak m}\ne C_{\mathfrak m}
\quad\Longleftrightarrow\quad
r\bmod\mathfrak m A\text{ is a scalar in }A/\mathfrak m A.
\tag{5}
\]
The entire scheme-theoretic fiber is essential. A nilpotent part of
the image of \(r\) counts as nonconstant.

Here is the mechanism. Work in the regular local ring
\(R=C_{\mathfrak m}\), with maximal ideal \((u,v)\). If \(JR\) is
proper, take a nonzero socle class \(z+JR\): both \(uz\) and \(vz\)
belong to \(JR\), but \(z\) does not. Choose actual \(a,b\in(F_2)_R\)
with \(D^2a=puz\) and \(D^2b=pvz\). Then
\[
va-ub=\alpha+\beta r,\qquad \alpha,\beta\in R.
\tag{6}
\]
If \(\beta\) were in the maximal ideal, faithful-flat contraction
would put \(\alpha\) there too. Subtracting elements of \(F_1\) would
make \(va'=ub'\). Flatness preserves the regular sequence \(u,v\),
so \(a'=ut\) and \(b'=vt\) for an actual \(t\). This gives
\(D^2t=pz\), a contradiction.

Therefore \(\beta\) is a unit, and (6) makes \(r\) scalar in the
closed fiber. Conversely, if \(JR=R\), the full localized quadratic
presentation is free over \(R\), with basis \(Y^k,rY^k\).
The images of \(1,r\) remain independent in every fiber.
The complete argument is in the
[closed-fiber criterion](research/second-image-closed-fiber-pass47.md).

This proof does not assume that a primitive derivation remains nonzero
on every closed fiber. The valid nonvanishing result at generic
divisor fibers is a different statement.

## 3. The obstruction is the zero scheme of a rank-two bundle section

The module \(F_2=\ker D^3\) is finite. For
\(z=a_2r^2+a_1r+a_0\in F_2\), differentiating and using \(F_1\)
puts \(pa_2,pa_1\) in \(C\), then \(pa_0\in A\cap L=C\). Hence
\[
F_2\subset p^{-1}(C+Cr+Cr^2).
\tag{7}
\]
The embedded height-one reconstruction of \(A\) gives the corresponding
intersection formula for \(F_2\). The standard normal-domain criterion
makes this finite module reflexive, and a reflexive module on a regular
surface is locally free.[^1]

Faithful flatness makes \(1\) a unimodular member of \(F_2\) at every
closed point. Constants therefore split off locally, and \(F_2/C\)
is a rank-two vector bundle. The class of \(r\) is a section whose
zero ideal is exactly \(J\), with multiplicities.

More explicitly, at a closed point, after an invariant translation
of the local minimal slice \(r\), choose
\[
(F_2)_R=R\oplus Rz\oplus Rw,\qquad r=az+bw.
\tag{8}
\]
The torsion-free quotient \(F_2/F_1\simeq pJ\) forces
\(\gcd(a,b)=1\). Wedge with \((a,b)\), followed by comparison at
height-one primes, gives \(JR=(a,b)\). Thus any proper local
obstruction is a zero-dimensional complete intersection, not an
arbitrary finite ideal.

The action has the exact form
\[
Dz=\epsilon br+B_1,\quad Dw=-\epsilon ar+B_2,\qquad
p=aB_1+bB_2,\qquad \epsilon\in R^*.
\tag{9}
\]
Consequently the subalgebra \(H=R[z,w]\) has the exact conic equation
\[
\epsilon(aZ+bW)^2-2B_2Z+2B_1W-Q=0,\qquad Q\in R.
\tag{10}
\]
The proof establishes equality \(H_{(\pi)}=A_{(\pi)}\), not automatic
global equality. The full construction and the distinction between a
free module and a section with no zeros are in the
[vector-bundle note](research/second-image-vector-bundle-pass47.md).

## 4. Cylinder topology excludes the unit-linear conic case

The complete pointwise plinth argument applies to the unknown \(A\).
A reduced single affine-line quotient fiber with nonzero induced
translation lies outside the primitive plinth support. The proof uses
the exact quotient factorization and peripheral-cycle diagram supplied
by Kaliman, together with smoothness, factoriality and the vanishing
of \(H_2,H_3,H_4\). All hold for the factor in (1). It does not require
that factor already to be a polynomial three-ring.[^2]

The [scope extension](research/intrinsic-pointwise-plinth-pass47.md)
retains the whole-fiber reached-branch argument. In particular,
surjectivity of an intermediate map is not replaced by surjectivity
after normalization.

At a point where \(J\) is proper, \(a,b\) in (8) vanish. If either
\(B_1\) or \(B_2\) is a unit, (10) has a unit linear coefficient.
Its coefficient ideal is therefore the unit ideal, making \(H\)
flat over \(R\). This is stronger than Gauss primitivity.

A flat module over a UFD is the intersection of its height-one
localizations inside its generic localization. Clearing a denominator
proves this directly: flatness preserves multiplication by a coprime
element modulo each prime power, and preserves the finite intersection
of those prime-power ideals. Thus \(H=A_R\) in this unit-linear case.

Its full closed fiber is a reduced line, and (9) induces a nonzero
translation there. The pointwise plinth theorem contradicts
\(p\in(a,b)\). We conclude that at every actual basepoint,
\[
B_1,B_2\in\mathfrak mR,\qquad
p\in\mathfrak mJR\subseteq\mathfrak m^2R.
\tag{11}
\]
In particular,
\[
\operatorname{Supp}(C/J)\subseteq
V(p,\partial_U p,\partial_V p).
\tag{12}
\]
This is the singular locus of the full polynomial \(p\), including
multiplicities. For example, \(p=U^n\) with \(n>1\) is singular along
its whole zero set even though the reduced support is a smooth line.

The [flat-conic proof](research/flat-conic-topology-gate-pass47.md)
also states exactly what survives: all coefficients of (10) vanish
at such a point, so \(H\) has a plane fiber there. This plane need not
inject into the one-dimensional full fiber of \(A\). It is a remaining
generation problem, not a dimension contradiction.

## 5. Explicit recognition for a smooth reduced plinth

Suppose \(p\) is squarefree and \(V(p)\) is smooth. Equation (12)
makes \(J=C\), hence gives the full global quadratic equation.
Every retained plinth component has affine-line normalization by the
existing quotient geometry. Being smooth, each is an actual embedded
affine line. The Suzuki–Abhyankar–Moh theorem makes one component a
coordinate line in the invariant plane.[^3]

Choose \(C=\mathbb C[u,v]\) so this line is \(u=0\). Any other
component is a disjoint affine line, on which \(u\) is a nowhere-zero
regular function, hence constant. All components are consequently
parallel coordinate lines. Up to a constant unit,
\[
p=P(u)=\prod_i(u-a_i),\qquad a_i\text{ distinct}.
\tag{13}
\]
After completing the square the whole ring is
\[
A=\mathbb C[u,v,r,Y]/(P(u)Y-r^2-d(u,v)).
\tag{14}
\]
At each root \(a_i\), a repeated root of \(d(a_i,v)\) would give a
singular point of (14): take \(r=0\) and
\(Y=d_u(a_i,v)/P'(a_i)\). Thus each residue polynomial is squarefree.
Its quadratic field cover has just one finite branch value by the
previous normalized-cover theorem, so it is a linear polynomial in
\(v\), with nonzero slope.

Interpolation now gives
\[
d(u,v)=A_0(u)v+B_0(u)+P(u)h(u,v),\qquad
\gcd(P,A_0)=1.
\tag{15}
\]
Set \(Y'=Y-h\) and choose
\(\alpha P+\beta A_0=1\). The determinant-one linear change
\[
W=P Y'-A_0v,\qquad Z=\beta Y'+\alpha v
\tag{16}
\]
has polynomial inverse
\[
Y'=\alpha W+A_0 Z,\qquad v=-\beta W+PZ.
\tag{17}
\]
The only relation is now \(W=r^2+B_0(u)\), so eliminating \(W\)
proves
\[
\boxed{A=\mathbb C[u,r,Z].}
\tag{18}
\]
The [recognition note](research/smooth-plinth-recognition-pass47.md)
contains the complete construction and boundary checks. Empty plinth
support is the ordinary slice case. No assumption that \(P\) has only
one root is needed.

The conclusion is conditional on the quadratic-divisor setup and
smooth reduced plinth. It does not cover singular reduced curves,
intersections of components, or repeated plinth factors.

## 6. A checked counterexample to the weaker algebraic shortcut

The following actual algebra shows that the cylinder topology is
doing necessary work:
\[
A_0=\mathbb C[u,v,z,w]/((uz+vw)^2+2w-v),\qquad
r_0=uz+vw,
\tag{19}
\]
\[
D_0u=D_0v=0,\quad
D_0z=1+vr_0,\quad D_0w=-ur_0,\quad D_0r_0=u.
\tag{20}
\]
It is a smooth factorial threefold with constant units, a primitive
LND, faithfully flat invariant plane \(C_0=\mathbb C[u,v]\), and
full plinth \(uC_0\). Inverting \(u\) gives a polynomial line over
\(C_0[1/u]\); the divisor at \(u=0\) is irreducible. Nagata's
criterion supplies factoriality.[^4]

Nevertheless,
\[
\ker D_0^3=C_0\oplus C_0z\oplus C_0w,\qquad
D_0^2(A_0)\cap C_0=u(u,v).
\tag{21}
\]
Thus both low-degree modules are free while their image quotient is
nonprincipal. At the origin, \(r_0\) is scalar in the full fiber
\(\mathbb C[z]\), where \(D_0z=1\).

The all-degree computation is also exact:
\[
D_0^n(A_0)\cap C_0
=u^{\lceil n/2\rceil}(u,v)^{\lfloor n/2\rfloor},\qquad n\ge0.
\tag{22}
\]
It follows from the actual associated graded domain
\(C_0[R,Z]/(2uZ-vR^2)\), with weights \(1,2\), not a pattern inferred
from finitely many derivatives.

The example cannot be a cancellation counterexample. The curve
\(\Sigma=\{vr_0^2+2r_0-v^2=0\}\) is a finite double cover of the
\(r_0\)-line with four simple branch points, since its discriminant
is \(r_0^4+8r_0\). Hence \(\chi_c(\Sigma)=-2\). The complement of
\(u=0\) is \(\mathbb C^*\times\mathbb A^2\), and its zero divisor is
\(\Sigma\times\mathbb A^1\). Additivity gives \(\chi(A_0)=-2\), so
\(A_0\) is not contractible and no polynomial extension of it is affine
space.[^5]

The [full control proof](research/second-image-countercontrol-pass47.md)
also exhibits a nonreduced fiber where \(r_0\) is scalar after reduction
but not before reduction. It rules out discarding nilpotents in (5).

## 7. Literature and remaining obligations

The current Dasgupta–Lahiri v6 treats specified nice or quasi-nice
derivations on actual relative polynomial planes. Its introduction
still formulates general three-variable image-ideal principality as
the Freeness Conjecture. Its positive results do not supply the missing
relative coordinates on the unknown \(A\).[^6] The previously announced
all-ranks proof by Daigle is withdrawn for an error and is not a valid
input.[^7]

The [statement-level source audit](research/image-ideal-source-scope-pass47.md)
also distinguishes published PID results from factorial-domain
classification statements which assume freeness. Finiteness of an
intermediate curve cover is not silently upgraded to a statement about
the full residue invariant ring or about a chosen minimal slice.

The next mathematical obligation in the quadratic branch is now more
specific: analyze a section-zero point where \(p\in\mathfrak mJ\),
the derivation vanishes on the second-degree module modulo
\(\mathfrak m\), and the conic subalgebra has a plane fiber. The actual
ring may need higher-degree generators there. Excluding or classifying
this correction requires more than the local quadratic models.

The genuinely moving higher branches of the supplied \((1,1,2,2)\)
profile and existence of a universal actual-frame reduction remain
separate obligations. The original unrestricted goal is unchanged.
No historical novelty, human expert approval or formal proof assistant
verification is claimed.

## Sources

[^1]: Stacks Project, [Lemma 15.24.18, tag 0AVB](https://stacks.math.columbia.edu/tag/0AVB) and [Lemma 31.13.15, tag 0B3N](https://stacks.math.columbia.edu/tag/0B3N). Finite reflexivity via height-one intersection and local freeness on regular surfaces.
[^2]: Shulim Kaliman, [*Free C+-actions on C3 are translations*](https://www.math.miami.edu/~kaliman/library/Ka.invent.2004.c%2B.pdf), final 2004 author version, Lemma 2.2, Proposition 3.2 and Theorem 5.2. The pointwise extension is a written deduction using the full published geometry, not a verbatim source theorem.
[^3]: Angelo Vistoli, [*On the minimal normal compactification of a polynomial in two variables*](https://arxiv.org/pdf/math/9904035v3), 2 August 1999, p. 2, Suzuki–Abhyankar–Moh theorem over \(\mathbb C\), with supporting Theorem 1 proof on pp. 3–4. Original embedding theorem credited there to Suzuki and Abhyankar–Moh.
[^4]: Stacks Project, [Lemma 10.120.7, tag 0AFU](https://stacks.math.columbia.edu/tag/0AFU), Nagata's criterion for factoriality.
[^5]: Sylvain E. Cappell, Laurentiu G. Maxim and Julius L. Shaneson, [*Euler Characteristics of Algebraic Varieties*](https://people.math.wisc.edu/~lmaxim/Euler.pdf), *Communications on Pure and Applied Mathematics* 61 (2008), 409–421, Section 2, p. 410. Standard additivity and multiplicativity; the example's calculation is given above.
[^6]: Nikhilesh Dasgupta and Animesh Lahiri, [*On image ideals of nice and quasi-nice derivations on R[X1,X2]*](https://arxiv.org/html/2302.13787v6), v6, 24 July 2026, Introduction and Theorems 4.1, 5.2, 5.9.
[^7]: Daniel Daigle, [*The freeness property for locally nilpotent derivations of k[x,y,z]*](https://arxiv.org/abs/2009.14800), v2, withdrawn 14 May 2021. Current record explicitly identifies the proof error.
