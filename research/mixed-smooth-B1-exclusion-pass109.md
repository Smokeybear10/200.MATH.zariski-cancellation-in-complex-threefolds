# The first conic constant cannot be a smooth base parameter

In the remaining actual collapsed mixed quadratic branch, the conic
constant B1 must belong to the square of the base maximal ideal.
This excludes more than the smooth-a case: the proof allows the
coefficient of G in the first-degree generator to have higher order.
It yields fourth-order vanishing of the whole first-image ideal, but
does not exclude the higher-order branch or solve cancellation.

## 1. Actual hypotheses and the sharp conic constraint

Retain the actual faithfully flat domain A_R over the regular local
invariant surface (R,m), its canonical LND N, and its finite free
modules F_j=ker N^(j+1) of rank j+1. The whole fiber is
D[c], with D=C[G]/(G^2(G-1)). The remaining second-degree
module has a basis 1,G,H, with H having zero whole-fiber residue,
and the following actual conic data:[^proper]
\[
\begin{gathered}
r=aG+bH,\quad Nr=P,\quad
NG=\epsilon br+B_1,\quad NH=-\epsilon ar+B_2,\\
P=aB_1+bB_2\ne0,\qquad
Q=\epsilon r^2-2B_2G+2B_1H\in R,\\
\epsilon\in R^*,\quad J_2=(a,b)\subset\mathfrak m,
\quad \gcd(a,b)=1,\quad \gcd(B_1,b)=1,\\
Q,B_2,a^2\in
\mathfrak m(B_1)+\mathfrak m(ab)+\mathfrak m^2(b^2).
\end{gathered}
\tag{1}
\]
In particular B1 is nonzero and belongs to m. The last membership
uses purity only of the piece R{1,G,G^2}, not of all F2.
Every invariant height-one localization has the exact degree-one
slice or degree-two conic model proved in107.[^divisor]

## 2. A smooth B1 permits an exact shear without dividing by a unit u

Suppose h=B1 belongs to m but not m^2. Then C=R/(h) is a DVR,
and b has nonzero image there. Reduce the a^2 membership in (1)
modulo h, and divide by b^2 in Frac(C). The element z=a/b
satisfies a monic equation z^2-v0 z-w0=0, with v0 in mC
and w0 in (mC)^2. Normality puts z in C, and reduction of the
equation puts z in mC. Thus there are u in R and v in m with
a=hu+bv. The element u need not be a unit. Define
\[
H'=H+vG,\quad a'=a-bv=hu,\quad
B_2'=B_2+vh,\quad G'=G.
\tag{2}
\]
This basis change has determinant one. It preserves r, N, P,
epsilon, Q, and the conic identities, with B1=h unchanged.
It also preserves the zero whole residue of H. In the actual
coprime case u is nonzero, since u=0 would give b|a; no unit
assumption on u is made or used.

From a=hu+bv, with v in m, the sharp ideal in (1) is contained
in m(h)+m^2(b^2). Adding vh preserves that containment for B2'.
Drop the primes and write
\[
\begin{gathered}
a=hu,\qquad B_2=h\beta+b^2\delta,
\qquad Q=h\zeta+b^2q,\\
\beta,\zeta\in\mathfrak m,
\qquad\delta,q\in\mathfrak m^2,\\
h(\epsilon hu^2G^2+2\epsilon ubGH-2\beta G+2H-\zeta)
 +b^2(\epsilon H^2-2\delta G-q)=0.
\end{gathered}
\tag{3}
\]
This is an identity in the actual algebra, obtained by expanding
the conic. No quotient or completed presentation replaces A_R.

## 3. The actual divided element has zero whole-fiber residue

The elements h,b^2 form a regular sequence in R. Flatness makes
b^2 a nonzerodivisor modulo h in A_R. Equation (3) therefore
proves existence of the actual element
\[
\begin{gathered}
U=(\epsilon H^2-2\delta G-q)/h\in A_R,\qquad U\in F_4,\\
hU\in\mathfrak m^2A_R,\qquad
(\mathfrak m^2A_R:h)=\mathfrak mA_R,
\qquad \boxed{\bar U=0.}
\end{gathered}
\tag{4}
\]
The degree assertion follows by applying N^5 to hU and cancelling
the nonzero invariant h. No exact degree of U is required.
Its numerator lies in m^2 A_R because H belongs to mA_R and
delta,q belong to m^2. For the colon assertion, multiplication
by h gives an injection R/m into R/m^2. Tensoring with the flat
module A_R gives exactly the displayed identity. This argument
uses h of order one, not a of order one.

## 4. A generic determinant with no missing point factor

In the generic polynomial line K[r], with K=Frac(R), use the
ordered monomial basis 1,r,r^2,r^3,r^4. Integrating NG gives
G=A2 r^2+A1 r+A0, where A2=epsilon b/(2P), A1=h/P,
and A0 is an invariant in K. Also H=(r-aG)/b. Column operations
and the formula for U give
\[
\begin{aligned}
\det(1,G,G^2,GH,U)
 &=\frac{\epsilon}{hb^3}
       \det(1,G,G^2,rG,r^2)\\
 &=-\frac{\epsilon}{hb^3}A_1 A_2^3
 =\boxed{-\frac{\epsilon^4}{8P^4}}.
\end{aligned}
\tag{5}
\]
Here determinants mean coefficient matrices in the specified
monomial basis. For the first equality, replace U by
(epsilon/h)H^2 modulo 1,G, then replace GH and H^2 using
H=(r-aG)/b. The two column factors are 1/b and 1/b^2.
For the second equality, discard degree-zero coefficients using
the first column, then expand along the r^2 column. The remaining
three-by-three matrix has first column (A1,0,0) and lower-right
block with rows (2A1A2,A2) and (A2^2,0), giving -A1 A2^3.
Thus the formula
does not assume a zero conic constant Q or u invertible.

Let B be any R-basis of the actual free F4. The five elements
in (5) belong to F4, so their coefficient matrix relative to B
has entries in R. At a degree-one invariant divisor, P is a
unit and the actual r is an affine coordinate with unit leading
coefficient relative to a local slice. The monomial-basis
determinant of B therefore has valuation zero there.

At a degree-two invariant divisor with e=ord(P), the actual
alternating DVR basis is 1,r0,t,r0t,t^2. In the powers of r0,
its determinant has valuation -4e. The global r and the minimal
local r0 are affine related with unit leading coefficient, since
both derivatives generate I1 at that divisor. Hence the same
valuation -4e holds in powers of r. Equation (5) has exactly
that valuation at every divisor.

The determinant of the R-matrix relative to B consequently has
valuation zero at every height-one prime. Since R is a UFD it
is a unit. The five elements in (5) are therefore an actual
R-basis of F4. This finite matrix argument does not assume
that divisorwise equality alone identifies arbitrary modules.

## 5. The whole-fiber contradiction and resulting orders

But GH and U both have zero whole residue. Such a basis would
make the image W4 have dimension at most three, spanned by
1,G,G^2. The actual c in F4 has residue independent of those
three elements. This is a contradiction. Therefore, in the
original proper-ideal coordinates of (1),
\[
\boxed{\quad B_1\in\mathfrak m^2,\qquad
a\in\mathfrak m^2,\qquad B_2,Q\in\mathfrak m^3,
\qquad P\in\mathfrak m^4.\quad}
\tag{6}
\]
For the second assertion, if a had order one then all three
summands of the sharp ideal in (1) would have order at least
three, while a^2 has order two. Once a and B1 have order at
least two, the same ideal lies in m^3. This gives B2,Q in m^3,
and P=aB1+bB2 then lies in m^4. These conclusions return to
the original coefficients; the contrary-assumption shear was
used only to exclude a smooth B1.

The exact normalized second image and divisor valuations,
together with actual fourth-image nonprincipality, also give
\[
\boxed{\quad I_1\subseteq\mathfrak m^4,
\quad I_2\subseteq\mathfrak m^5,
\quad I_3\subseteq\mathfrak m^8,
\quad I_4\subseteq\mathfrak m^9.\quad}
\tag{7}
\]
Indeed I1=(P), I2=PJ2 with J2 in m, I3 is contained in P^2R
by the height-one UFD intersection, and I4=P^2J4 with J4 proper.
No equality of these orders or indefinite iteration is asserted.
In particular, higher-order B1 does not supply the colon argument
in (4). For example, in the flat module R=C[x,y]_(x,y), h=x^2
and U=1 satisfy hU in m^2 but U not in m. This is a control
for that failed colon implication, not an actual-frame example.
Also J2 cannot equal m: a in m^2 and the single class of b cannot
span the two-dimensional cotangent space. Thus length(R/J2)>=2.
The entire mixed branch is not excluded.

## Scope and sources

The determinant mechanism independently sharpens the earlier
[smooth-a determinant argument109](mixed-smooth-quartic-determinant-exclusion-pass109.md).
It needs neither the selected c's sharp fourth-image valuation,
the equality W3=D, the narrower cubic-image calculation109,
nor generation of A_R by F4. It only uses the existence of c
in F4 with its stated independent whole residue.

The standard quotient/DVR facts were checked in Stacks Project
[00NQ](https://stacks.math.columbia.edu/tag/00NQ) and
[00PD](https://stacks.math.columbia.edu/tag/00PD). The actual
division, coefficient determinant and scalar valuation argument
are written out above. Exact symbolic determinant calculations
support the coefficient identity, not the actual flatness,
divisor classification, or universal existence assertions.
Separate AI reconstructions are not human or formal verification.
All files through108 remain unchanged. Global cancellation and
the arbitrary-frame entry problem remain unresolved.

[^proper]: [Sharp proper second-image proof108](mixed-proper-second-image-jets-pass108.md) and [unit-case exclusion108](mixed-unit-second-image-exclusion-pass108.md), in the supplied collapsed mixed quadratic sector with nonzero speed normal. These include nonzero b and B1, their coprimality, and the whole-residue hypotheses.

[^divisor]: [Exact quadratic divisor filtration107](quadratic-constant-divisor-filtration-pass107.md), Sections 4–5; and [degree-one DVR slice105](mixed-cubic-rank-defect-pass105.md), Section 2. The localized global r is an actual first-degree basis element, not a generic polynomial coordinate arbitrarily rescaled by a prime.
