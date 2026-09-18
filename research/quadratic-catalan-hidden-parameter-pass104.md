# Catalan truncation recovers a hidden quadratic parameter

The apparent quartic term in y does not obstruct a hidden element
of N-degree two in this intrinsic polynomial family. For every
integer m at least one, a finite Catalan truncation gives such an
element globally, with exact whole-fiber residue minus c. It gives
a conic presentation over the full invariant plane.

The residue modulo x alone is not minus c: it has an additional
even power of y. That power vanishes on the whole double fiber,
including its nilpotents. The construction is an intrinsic
threefold calculation, not an original four-coordinate E-frame.

## 1. The polynomial family

Work with
\[
\begin{gathered}
A=\mathbb C[x,y,c],\qquad
f=y^2+xy^4+x^m c,\qquad S=\mathbb C[x,f],\qquad m\ge1,\\
N=-x^m\partial_y+(2y+4xy^3)\partial_c
 =\det\frac{\partial(x,f,\,\cdot\,)}{\partial(x,y,c)},\\
Nx=Nf=0,\qquad
\mathfrak m=(x,f)S,\qquad \mathfrak p=(x,y)A,\qquad
A/\mathfrak mA=\mathbb C[y,c]/(y^2).
\end{gathered}
\tag{1}
\]
The variables x,f are algebraically independent: after inverting x,
the equation for f solves for c and gives \(A_x=S_x[y]\).
The coefficient gcd of N is one, because x does not divide
\(2y+4xy^3\). Thus N is the primitive polynomial base Jacobian.
Give x weight zero, y weight one and c weight four. Every term
of N decreases this weight, proving local nilpotence on A.

## 2. A finite polynomial inverse modulo x to the m

Let \(C_j=(j+1)^{-1}\binom{2j}{j}\) be the Catalan integers, and
use an independent variable t when defining
\[
\begin{gathered}
P_m(x,t)=\sum_{j=0}^{m-1}(-1)^j C_j x^j t^{j+1},\\
Z(x,t)=\frac{(1+4xt)^{1/2}-1}{2x}
 =\sum_{j\ge0}(-1)^j C_j x^j t^{j+1}
 \quad\text{in }\mathbb C[t][[x]],\\
Z+xZ^2=t,\qquad
P_m+xP_m^2\equiv t\pmod{x^m}.
\end{gathered}
\tag{2}
\]
The displayed series is purely formal. Expanding the binomial
series, its coefficient of x to the j is
\(2^{2j+1}\binom{1/2}{j+1}t^{j+1}=(-1)^j C_jt^{j+1}\).
Squaring the formal square root verifies the quadratic identity.
Truncation then proves the last congruence as a polynomial
identity, without any convergence assertion.

Define
\[
\begin{gathered}
R_m(x,t)=\frac{t-P_m(x,t)-xP_m(x,t)^2}{x^m}
 \in\mathbb C[x,t],\qquad t\mid R_m,\\
P=P_m(x,f),\qquad R=R_m(x,f),\qquad
U=\frac{y^2-P}{x^m}\in A.
\end{gathered}
\tag{3}
\]
The divisibility for Rm follows from (2). Its numerator is
divisible by t, and x and t are coprime in C[x,t], so the
quotient Rm is also divisible by t.

Here is the full polynomial gate for U. In A modulo x to the m,
both \(y^2\) and \(P_m(x,f)\) solve \(Z+xZ^2=f\):
the first follows from (1) and the second from (2). Any two
solutions Z1,Z2 in this quotient satisfy
\((Z_1-Z_2)(1+x(Z_1+Z_2))=0\).
The second factor is a unit, with a finite geometric-series
inverse since x is nilpotent. Thus the solutions are equal.
It follows that x to the m divides \(y^2-P\) in the polynomial
ring A. No rational or completed lift is being substituted
for the asserted polynomial U.

Since P is invariant and A is a domain, differentiating the
polynomial equality \(x^mU=y^2-P\) gives
\[
\begin{gathered}
NU=-2y,\qquad N^2U=2x^m,\qquad N^3U=0,\\
N^2c=-2x^m-12x^{m+1}y^2,\qquad
N^3c=24x^{2m+1}y,\qquad
N^4c=-24x^{3m+1}\ne0,\qquad N^5c=0.
\end{gathered}
\tag{4}
\]
In particular U has N-degree exactly two, whereas the specified
original c has N-degree four. This is not a renaming of c.

## 3. Exact algebra generation and the relative conic

Substitute \(y^2=P+x^mU\) into (1). Using (3) yields
\[
\begin{gathered}
c=R-(1+2xP)U-x^{m+1}U^2,\qquad
\boxed{\quad A=S[y,U].\quad}\\
\boxed{\quad
A\simeq S[\mathsf Y,\mathsf U]/
\bigl(\mathsf Y^2-x^m\mathsf U-P_m(x,f)\bigr),
\quad \mathsf Y\mapsto y,\quad\mathsf U\mapsto U.
\quad}
\end{gathered}
\tag{5}
\]
The displayed recovery of c proves surjectivity of the proposed
presentation. Its source is free over S[\(\mathsf U\)] with
basis 1,\(\mathsf Y\), because the relation is monic in
\(\mathsf Y\). It is therefore S-torsion-free. After inverting x,
the relation solves for \(\mathsf U\), and the map becomes the
isomorphism \(S_x[\mathsf Y]\simeq A_x=S_x[y]\).
Its original kernel is x-torsion and hence zero. This proves the
exact conic, not just equality of fraction fields or completions.

The same presentation makes S into A faithfully flat: the source
is a nonzero free S-module. It is a genuine smooth polynomial
threefold A, not a formal conic coefficient prescription.

## 4. Residues before and after taking the whole fiber

The next Catalan coefficient in (2) gives
\[
\begin{gathered}
R_m(0,t)=(-1)^m C_m t^{m+1},\\
U\bmod x=-c+(-1)^m C_m y^{2m+2}
 \quad\text{in }\mathbb C[y,c],\\
\boxed{\quad
U\bmod(x,f)=-c
 \quad\text{in }\mathbb C[y,c]/(y^2).
\quad}
\end{gathered}
\tag{6}
\]
For the first equality, compare Pm with
\(P_{m+1}=P_m+(-1)^m C_mx^mt^{m+1}\) in its quadratic identity
modulo \(x^{m+1}\). This gives the coefficient of x to the m in
the numerator defining Rm. Reducing the recovery formula (5)
modulo x then gives the second line, since \(f\bmod x=y^2\).
Finally \(2m+2\ge4\), so the extra term vanishes modulo y squared.

Alternatively, the exact last line follows immediately from (5):
R belongs to fS by (3), while x=f=0 on the whole fiber.
Both arguments retain nilpotents. The reduction of NU is minus
twice y, a nonzero square-zero class on this fiber. Thus U is
a nonconstant surviving degree-two element, even though y alone
has zero reduced residue.

For m at least two, \(N(\mathfrak p)\subset\mathfrak p^2\).
For m equal to one, the class \(Ny=-x\) gives nonzero first
normal action. The hidden parameter exists in both cases.

## 5. The full degree-two module is also explicit

The same polynomial gate determines all degree-two elements:
\[
\boxed{\quad
\ker(N^3)=S\oplus Sy\oplus SU,\qquad \ker N=S.
\quad}
\tag{7}
\]
After inverting x, N is minus x to the m times the derivative
in y with x,f fixed. The degree-two module has basis 1,y,U,
since \(U=(y^2-P)/x^m\), and these elements are S-linearly
independent. Suppose a minimal denominator expression for an
element of A is
\(x^kh=A_0(x,f)+A_1(x,f)y+A_2(x,f)U\) with k positive.
Modulo x, equation (6) makes the coefficient of c equal to
minus \(A_2(0,y^2)\), so A2 is divisible by x. The remaining
even and odd polynomials in y separately force the same
divisibility for A0 and A1. This contradicts minimality of k.
It proves the module equality for every polynomial, with no
bound on coefficient degrees.

For an invariant element in this module, its derivative is
\(-x^mA_1-2yA_2\). Independence of 1,y over S forces A1=A2=0.
This proves the full kernel assertion. The argument is the
parity-saturation method of
[polynomial lift101](quadratic-double-polynomial-lift-obstruction-pass101.md),
applied to the new polynomial U and its exact residue.

The cyclic invariant associated with this hidden element is
\(2(N^2U)U-(NU)^2=-4P_m(x,f)\).
Thus the conic also has the exact cyclic form discussed in
[cyclic degree-module103](noncollapsed-cyclic-degree-module-pass103.md).
Here it has been proved directly for the stated intrinsic family;
no original E-frame is inferred from that comparison.

## 6. A relative parameter is not an ambient coordinate system

The coordinate determinant of the proposed triple x,y,U is
\[
\det\frac{\partial(x,y,U)}{\partial(x,y,c)}
 =U_c=-\partial_tP_m(x,f)
 =
 \begin{cases}
 -1,&m=1,\\
 \text{a nonconstant polynomial},&m\ge2.
 \end{cases}
\tag{8}
\]
For m at least two, the coefficient polynomial in S contains
the nonzero term \(2xf\), and algebraic independence of x,f
prevents its cancellation by terms of larger x,f degree.
Consequently (x,y,U) is not a polynomial coordinate system in
those cases. This does not contradict (5): that presentation
retains the invariant generator f. It also does not assert that
U alone cannot be an ambient coordinate in some other tuple.

When m equals one the formula is especially transparent:
\(P_1=f\) and \(U=-c-y^4\). For m at least two the apparent
replacement \(c\mapsto c+x^{1-m}y^4\) is not a polynomial shear.
The finite Catalan construction supplies a polynomial hidden
parameter without silently using that nonpolynomial replacement.

## Scope

All assertions concern the displayed intrinsic family. The high
apparent defining degree does not obstruct its hidden quadratic
parameter, but no classification of actual frames or general
existence theorem for hidden parameters is supplied. A is already
a polynomial threefold. No counterexample to recognition or
cancellation is claimed, and no new primary-source theorem is
used. All files through103 remain unchanged.

The standalone [finite Catalan checker](quadratic_catalan_checks_pass104.py)
has one method, with exact symbolic subtests for m=1 through5. It checks
the polynomial divisions, recovery and conic identities, derivative
orders, both residue levels, the coordinate determinant, and finite
module/parity samples. These finite instances do not verify the
all-m polynomial or saturation proofs above. The first assertion-bearing
author run passed one method in 0.576 seconds, exit zero, tool chunk
72e191; its wall time was 0.847100917 seconds. No full regression was run.
