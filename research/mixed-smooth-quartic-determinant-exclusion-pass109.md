# The actual quartic determinant excludes a smooth a

The smooth-a subcase of the remaining proper second-image branch is
impossible. Five actual degree-four elements have the full determinant
valuation at every invariant divisor, so they form a basis over the
local invariant surface. Their whole-fiber residues, however, span only
the three-dimensional Artin algebra and cannot contain the actual
parameter c.

This proof uses the actual divided quartic and the full DVR degree
modules. It does not use a putative finite parameter map, a polynomial
inverse over the invariant base, or purity of the entire F4.

## 1. Actual smooth-a setting

Let R=S_m, with maximal ideal n and fraction field K, be the regular
local invariant surface in the actual collapsed mixed (2,1), L(m)
nonzero sector. Retain the faithfully flat domain A_R, its LND N
with full kernel R and generic polynomial line, and the finite free
degree modules Fj=ker N^(j+1). The normalized smooth-a data from108
are
\[
\begin{gathered}
F_1=R\oplus Rr,\quad Nr=P\ne0,\quad
F_2=R\oplus RG\oplus RH,\quad r=aG+bH,\\
NG=\epsilon br+a,\qquad NH=-\epsilon ar+B_2,
\qquad P=a^2+bB_2,\qquad \epsilon\in R^*,\\
a\in\mathfrak n\setminus\mathfrak n^2,\quad
J_2=(a,b),\quad \gcd(a,b)=1,\quad b\ne0,\\
Q=\epsilon r^2-2B_2G+2aH,\quad
B_2=a\beta+b^2\delta,\quad Q=a\zeta+b^2q,\\
\beta,\zeta\in\mathfrak n,\quad\delta,q\in\mathfrak n^2,
\quad H\in\mathfrak nA_R,\quad F_4\simeq R^5,\\
A_R/\mathfrak nA_R=\mathcal D[c],\qquad
\mathcal D=\mathbb C[G]/(G^2(G-1)),\qquad c\in F_4.
\end{gathered}
\tag{1}
\]
The element G is unchanged by the normalization. The original r and
its derivative generator may be multiplied by invariant units; N is
not rescaled. These exact data are supplied by the sharp-purity and
one-quartic108 proofs.[^normalization]

At every height-one prime of R, the actual degree modules have the
full presentations107. For constant-field degree one the algebra has
a DVR slice. For degree two it has the monic conic and alternating
degree-module basis. The existence of a surviving degree-two element
at every such divisor is a substantive actual-frame input.[^divisors]

## 2. The divided quartic is an actual element with zero whole residue

The normalized conic is the exact identity
\[
\begin{gathered}
a\bigl(\epsilon aG^2+2\epsilon bGH-2\beta G+2H-\zeta\bigr)
{}+b^2\bigl(\epsilon H^2-2\delta G-q\bigr)=0,\\
U=(\epsilon H^2-2\delta G-q)/a\in F_4,
\qquad \boxed{\quad U\in\mathfrak nA_R.\quad}
\end{gathered}
\tag{2}
\]
Since a is a regular parameter and b is nonzero modulo a, (a,b²)
is an R-regular sequence. Flatness makes b² a nonzerodivisor on
A_R/aA_R. Reducing the first identity modulo a proves that its
second parenthesis belongs to aA_R. This supplies the actual U.
Its numerator has N-degree at most four, and division by a nonzero
invariant retains that bound.

The numerator also belongs to n²A_R, because H is in nA_R and
delta,q are in n². Multiplication by a gives an injection R/n into
R/n². Tensoring with the flat A_R proves (n²A_R:a)=nA_R,
and hence the boxed whole-fiber membership. In particular both GH
and U have zero whole-fiber residue. This includes the double
nilpotents, not merely the reduced components.

No division by 1+epsilon bG is performed. The additional image-ideal
and W3 conclusions of108 are not needed in this proof.

## 3. A determinant identity in the generic line

The first-degree element r is a coordinate on the generic line,
with N=P times differentiation in r. Therefore
\[
G=A_2r^2+A_1r+A_0,\qquad
A_2=\frac{\epsilon b}{2P},\quad A_1=\frac aP,
\quad A_0\in K,\qquad H=\frac{r-aG}{b}.
\tag{3}
\]
For a list of five polynomials in r of degree at most four, let
Delta denote the determinant of their coefficient columns in the
ordered basis (1,r,r²,r³,r⁴). Consider the five actual elements
M=(1,G,G²,GH,U).

In the generic field, replace GH by rG/b using its earlier G²
column. Expressing H²=(r−aG)²/b² then replaces U by
epsilon r²/(ab²), modulo the columns 1,G,G²,GH. Consequently
\[
\begin{aligned}
\Delta(1,G,G^2,GH,U)
&=\frac{\epsilon}{ab^3}\,
  \Delta(1,G,G^2,rG,r^2)\\
&=-\frac{\epsilon A_1A_2^3}{ab^3}
=\boxed{-\frac{\epsilon^4}{8P^4}}.
\end{aligned}
\tag{4}
\]
For the middle equality, move the last r² column to the third
position, changing the sign by interchanging it with G². Subtract
A2 r²+A0 from the G column. The reordered degrees are then
0,1,2,3,4, with leading coefficients 1,A1,1,A2,A2². This
gives the stated sign and product. Thus the arbitrary integration
constant A0 and all beta,delta,zeta,q terms disappear by explicit
column operations, not by specializing them to zero.

The calculation takes place over K solely to compute a determinant.
All five original columns M belong to the actual free R-module F4.

## 4. Every divisor has exactly this determinant valuation

Fix an R-basis E of F4 and let C be the matrix of the five actual
columns M in that basis. Its entries belong to R. Write Delta_E
for the generic coefficient determinant of E in powers of r. We
claim, for every height-one prime p of R,
\[
\operatorname{ord}_{\mathfrak p}(\Delta_E)
 =-4\operatorname{ord}_{\mathfrak p}(P)
 =\operatorname{ord}_{\mathfrak p}(\Delta_M),
\qquad \operatorname{ord}_{\mathfrak p}(\det C)=0.
\tag{5}
\]
Here Delta_M is the nonzero determinant (4), and
Delta_M=Delta_E det(C).

For degree-one constants, put V=R_p. The actual DVR slice makes
P a unit and A_V=V[r]. Its fourth degree module has basis
1,r,r²,r³,r⁴. The localized basis E differs by a V-invertible
matrix, proving (5) in this case.

For degree-two constants, choose a uniformizer p0 of V. The actual
classification gives Nr0=p0^e and
p0^e t0=r0²+alpha r0+beta0, with e=ord_p(P). Its full F4 basis
is 1,r0,t0,r0t0,t0². The global r satisfies r=v r0+w, with
v=P/p0^e a V-unit and w in V: subtracting v r0 is invariant in
the actual localized algebra, whose full kernel is V.

In powers of r, the alternating basis has consecutive degrees
0,1,2,3,4. Its leading coefficients have valuations
0,0,−e,−e,−2e, respectively. Their product has valuation −4e.
Any other V-basis, including E localized at p, changes this by a
unit. This proves (5) for every degree-two divisor as well. There
are no other constant-field degrees in the actual quadratic frame.

## 5. The actual basis contradicts the whole fiber

The determinant det(C) is a nonzero element of the local UFD R.
By (5) it has no height-one prime factor, so it is a unit. Thus
\[
\boxed{\quad F_4=R\{1,G,G^2,GH,U\}.\quad}
\qquad
\operatorname{im}(F_4\longrightarrow A_R/\mathfrak nA_R)
=\mathcal D.
\tag{6}
\]
The equality of the image follows from (2): GH and U vanish
on the whole fiber, while 1,G,G² span D. But the actual c belongs
to F4 and its residue is the polynomial parameter of D[c], not
an element of D. This is a contradiction.

Therefore a cannot have first base order one in the remaining
proper second-image branch. Its nonzero coefficient a belongs to
n². This conclusion excludes the smooth-a subcase, not the entire
remaining mixed fiber or the higher-order coefficient cases.

The separate [smooth-B1 extension109](mixed-smooth-B1-exclusion-pass109.md)
applies the same determinant mechanism after a shear whose invariant
coefficient need not be a unit. It excludes a smooth B1 even when a
already has higher order. That stronger saved proof was independently
read through EOF; it is not an input to the narrower argument here.

## 6. Dependencies and the failed shortcut

Agreement of algebras at divisors alone would not justify a global
presentation. What works here is more specific: five actual elements
of one finite free degree module have an explicitly computed determinant,
and the exact local bases determine its valuation at every divisor.
The scalar determinant can then be tested in the UFD R. There is
no claim that the whole algebra is finite over R[G,c].

The proof does not use A_R=R[F4], the nonprincipality of I4, the
strict bound on its point ideal, W3=D, or a defining ideal for
R[G,c,U]. It needs only the actual element c in F4 with its independent
whole residue. Thus the determinant argument bypasses those additional
module conclusions rather than assuming they yield a polynomial inverse.

Root, General, Jet, and the author independently reconstructed the
generic determinant and DVR comparison. The exact determinant was
also checked once by an inline SymPy calculation with general invariant
integration constant; this finite calculation is not a proof of actual
division, local classification, or the all-divisor assertion. No new
standalone numerical method is claimed here. The complete retained
smooth-generator108 proof was freshly read before this deduction; the
full divisor and module proofs are the frozen dependencies listed below.
No new primary-source theorem or novelty claim is used. Independent AI
review is not human expert or formal proof certification.

The first method of the shared
[determinant checker109](mixed_divisor_determinant_checks_pass109.py)
checks the general-B1 determinant, its column reductions and shear,
and finite unit-affine DVR basis examples. The complete two-method
code was read here through EOF without execution. Its other method
concerns a separate actual-frame strong-nilpotence control. These
finite checks do not prove the division or all-divisor descent above;
the earlier inline determinant calculation remains a separate check.

Files through108 remain unchanged. The arbitrary-frame entry problem,
other remaining fiber sectors, and general cancellation remain open.

[^normalization]: [Proper second-image jets108](mixed-proper-second-image-jets-pass108.md), the smooth-a coefficient normalization; [actual smooth-generator quartic108](mixed-smooth-generator-quartic-pass108.md), Sections 1–2; and the flat colon calculation in [smooth quartic residue108](mixed-smooth-quartic-residue-pass108.md), Section 2. Only the indicated construction and colon inputs are used, not the latter note's basis or W3 conclusions.

[^divisors]: [Actual quadratic divisor classification107](quadratic-constant-divisor-filtration-pass107.md) and [independent normal-form proof107](quadratic-divisor-normal-form-gates-pass107.md), all-degree alternating bases; [degree-one slice105](mixed-cubic-rank-defect-pass105.md), Section 2; and [actual divisor91](nonconical-residue-degree-bound-pass91.md), including surviving good-generator noncollapse and the constant-field degree bound. Invariant localization commutes with these degree kernels. The finite freeness of F4 over R is [degree-module102](quadratic-degree-module-fiber-rigidity-pass102.md), Section 2.
