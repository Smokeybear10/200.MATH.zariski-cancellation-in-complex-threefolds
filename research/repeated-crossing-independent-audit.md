# Independent audit of repeated crossing coefficients

The integral residue calculation, the nonconstant-axis coordinate theorem,
and the two positive subfamilies in
[repeated-crossing-pass.md](repeated-crossing-pass.md) survive this audit.
The torsion calculation is an ordinary integral cohomology calculation:
for the stated nonzero fibers it gives \(H^3=\mathbb Z/q\).

One scope error was identified and corrected in the source note during
the audit. Rational acyclicity was initially stated for all fibers, while
the argument only covered nonzero fibers. The source now makes the
restricted assertion and proves the Euler characteristic of the zero
fiber separately. The change matters because the zero fiber has
intersecting boundary components and a divisor with multiplicity \(q\).

## 1. Why the Gysin sequence is integral and applicable

Fix a smooth fiber \(X\) and a reduced closed subset
\(E=E_x\sqcup E_y\) consisting of disjoint smooth complex divisors.
Put \(U=X\setminus E\). A tubular neighborhood identifies the relative
cohomology \(H^k(X,U;\mathbb Z)\) with the relative cohomology of the
normal bundle and its deleted zero section. The complex normal line
bundle has a canonical real orientation. Excision and the integral
Thom isomorphism therefore give

\[
 H^k(X,U;\mathbb Z)\simeq H^{k-2}(E;\mathbb Z).
\]

The long exact sequence of the pair becomes

\[
 \cdots\longrightarrow H^k(X;\mathbb Z)
 \longrightarrow H^k(U;\mathbb Z)
 \xrightarrow{\operatorname{res}}H^{k-1}(E;\mathbb Z)
 \longrightarrow H^{k+1}(X;\mathbb Z)\longrightarrow\cdots.
 \tag{1}
\]

Neither compactness of \(X\) nor compactness of \(E\) is required.
The relevant Thom and Gysin construction, including its orientation
local system, is recorded in Appendix A.4 of
[*Loop coproduct in Morse and Floer homology*](https://link.springer.com/article/10.1007/s11784-023-01061-z).
Here the complex orientation trivializes that local system. The passage
from the normal bundle to (1) is the tubular-neighborhood argument just
given.

Suppose \(x\) and \(y\) vanish simply on \(E_x\) and \(E_y\),
respectively, and are units along the opposite component. Let
\(\alpha=x^*\eta\), \(\beta=y^*\eta\), where \(\eta\) is the
integral generator of \(H^1(\mathbb C^*;\mathbb Z)\), normalized to
evaluate to one on a positive circle. Then

\[
 \operatorname{res}(\alpha\smile\beta)
 =\left(\beta|_{E_x},-\alpha|_{E_y}\right)
 \tag{2}
\]

with consistent orientation conventions. This is an integral formula:
over a loop in \(E_x\), take its product with a positive normal
meridian. The cup product evaluates on this torus as the winding number
of \(y\) along the loop. Interchanging the two degree-one classes for
\(E_y\) gives the minus sign. This computation determines the integer
map, rather than merely its scalar extension to de Rham cohomology.

The coefficient multiplicities \(r,s\) in \(x^ry^s u\) do not enter
(2). The vanishing orders in the actual fiber do enter it. At a generic
regular value, the quotients by \((x)\) and \((y)\) are reduced smooth
curve cylinders. Since the fiber is smooth, its local ring at each
generic divisor point is a DVR; a reduced quotient forces valuation one.
The source note makes this check correctly before using (2).

## 2. Independent reconstruction of the torsion example

For

\[
 F_{r,s,q}=x^ry^su+y+xz^q,\qquad
 r\ge1,\quad s\ge2,\quad q\ge2,
\]

every fiber is smooth: off \(xy=0\), \(F_u\ne0\), while on either
coordinate plane \(F_y=1\). Fix \(\lambda\ne0\). Then

\[
 \begin{aligned}
 E_x&=\{x=0,y=\lambda\}\simeq\mathbb A^2,\\
 E_y&=\{y=0,xz^q=\lambda\}
       \simeq\mathbb C^*_z\times\mathbb A^1_u,\\
 U&\simeq(\mathbb C^*)^2\times\mathbb A^1.
 \end{aligned}
\]

The two divisors are disjoint. Their defining quotient rings are
\(\mathbb C[z,u]\) and \(\mathbb C[z,z^{-1},u]\), respectively,
so the order-one premise of (2) holds.

The map \(H^1(U)\to H^0(E)\) in (1) is the identity matrix on the
two meridian generators, up to signs. On \(E_y\), however,

\[
 x=\lambda z^{-q},\qquad
 \alpha|_{E_y}=-q\eta_z.
\]

Since \(H^1(E_x)=0\), equation (2) makes
\(H^2(U)=\mathbb Z\to H^1(E)=\mathbb Z\) multiplication by
\(\pm q\). The relevant exact sequence is therefore

\[
 0\longrightarrow H^1(X)\longrightarrow\mathbb Z^2
 \xrightarrow{\cong}\mathbb Z^2
 \longrightarrow H^2(X)\longrightarrow\mathbb Z
 \xrightarrow{\times q}\mathbb Z
 \longrightarrow H^3(X)\longrightarrow0.
\]

Thus \(H^1(X)=H^2(X)=0\) and \(H^3(X)=\mathbb Z/q\).
The remaining terms of (1) give \(H^j(X)=0\) for \(j\ge4\).
The open set \(U\) is irreducible and dense in the smooth pure
three-dimensional fiber: the closed strata have dimension two, so they
cannot contain an irreducible component. Hence \(H^0(X)=\mathbb Z\).
This proves the full integral cohomology assertion in the source note.

For \(r=1,s=2,q=2\), this is exactly

\[
 F=xy^2u+y+xz^2,\qquad
 H^3(F^{-1}(\lambda);\mathbb Z)=\mathbb Z/2
 \quad(\lambda\ne0).
\]

The factor two is the degree of the map \(z\mapsto\lambda z^{-2}\)
on the punctured-line stratum. It is not the multiplicity of the divisor
\(y=0\) on a nonzero fiber. Rational coefficients would turn this
map into an isomorphism and erase the obstruction.

At \(\lambda=0\), the reduced boundary instead consists of the two
planes \(\{x=y=0\}\) and \(\{y=z=0\}\), meeting in the
\(u\)-line. Near the generic point of the second plane with \(x\ne0\),

\[
 y\left(1+x^ry^{s-1}u\right)=-xz^q.
\]

The parenthesized factor is a unit there, so \(y\) has order \(q\)
along that component. The nonzero-fiber Gysin calculation cannot simply
be copied to this value. The separate Euler calculation is valid:
the reduced boundary has Euler characteristic \(1+1-1=1\), and
the open set contributes zero. This proves \(\chi_c=1\) for the
zero fiber without claiming its rational acyclicity.

## 3. The generic constant-axis residue deduction is valid

For a stable coordinate \(x^ry^su+H\) with \(H(0,0,z)=b\),
the reduced-stratum cohomology argument forces, for generic values
\(\lambda\ne b\), one plane curve to be \(\mathbb A^1\) and the
other to be \(\mathbb C^*\). The pigeonhole and vertical-line argument
correctly makes one plane restriction \(ay+b\), after choosing the
orientation, where \(a\ne0\).

On the other curve, the unit \(x\) has the form \(dt^m\) in a
punctured-line coordinate, with \(m\ne0\). Contractibility of the
fiber makes the map in (2) an integral isomorphism, forcing
\(|m|=1\). Therefore projection to \(x\) is an isomorphism onto
\(\mathbb C^*\), not merely an étale map of unspecified degree.

This forces \(g(x,z)=H(x,0,z)\) to be linear in \(z\). A precise
way to justify the degree step is to use the chosen reduced regular
fiber: over general \(x\), its defining polynomial has one simple
root because projection is an isomorphism. A higher \(z\)-degree
would give more roots at general \(x\), counted with multiplicity.
Writing \(g=A(x)z+B(x)\), the same isomorphism forces
\(A(x)\ne0\) on \(\mathbb C^*\). Consequently
\(A=cx^k\), and the constant-axis restriction gives \(k\ge1\).

This proof only needs generic smooth plane fibers, which are available
in characteristic zero. It successfully avoids the invalid assertion
that an arbitrary critical point on the repeated plane restriction can
be made a critical point of the four-variable polynomial by choosing
\(u\). The resulting forms remain necessary conditions; the source
does not claim their sufficiency for arbitrary multiplicities.

## 4. The nonconstant-axis lifting theorem is valid

The reduced-divisor compact-support calculation is independent of
\(r,s\), including its finite intersection on the axis. It therefore
forces the exact same restriction

\[
 H=az+D(x,y)+xyR(x,y,z),\qquad a\ne0,
\]

as in the simple-crossing nonconstant-axis proof. Its use of plane-line
rectification is legitimate because the selected plane levels are
smooth and irreducible; their equations are not powers.

The new issue is lifting from the reduced crossing to the repeated
coefficient. Put \(p=x^ry^s\), \(n=xy\), and
\(N=\max(r,s)\), so \(n^N\in(p)\). The recurrence in the source
has initial error in \((n)\) and increases the error's divisibility
by one power at each step. For \(I=I_{N-1}\), both identities

\[
 H(I(T))-T\in(p),\qquad I(H(z))-z\in(p)
\]

hold. The proof of each identity is supplied separately. This is
important: the inverse formula uses both compositional directions.

For \(F=pu+H(z)\), the polynomial companion and inverse are

\[
 V=\frac{z-I(F)}p,\qquad
 z=I(S)+pV,\qquad
 u=\frac{S-H(I(S)+pV)}p.
\]

The two congruences prove polynomial divisibility of the two numerators;
the displayed identities then verify both compositions exactly. No
unproved residual-coordinate lifting theorem is required. Equivalently,
\(H\) is an affine automorphism modulo the nilpotent ideal
\((xy)/(p)\), and the second variable absorbs the lifting error.

An additional exact symbolic check used
\(p=x^2y^3\), \(H=z+x+y+xyz^2\), and the inverse modulo \(p\)

\[
 I(T)=(T-x-y)-xy(T-x-y)^2+2x^2y^2(T-x-y)^3.
\]

Both required numerators were divisible by \(x^2y^3\). This is a
check of the signs and divisibility in a case with unequal exponents;
the all-exponent proof is the recurrence and exact inverse above.

The two positive subfamilies in Section 3 also pass. For orientation A
with \(k=1\), apply this construction to
\(T=cz+yR_0+y^2u\) over \(\mathbb C[x,y]\), then solve
\(F=ay+B(x)+xT\) for \(y\). When \(R_0\) is independent of
\(z\), the cited univariate-coefficient criterion applies after
taking \(z\) as the linear variable. Neither argument extends by
formal division to all remaining jets.
