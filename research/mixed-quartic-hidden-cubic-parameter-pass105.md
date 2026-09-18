# A mixed quartic perturbation has a hidden degree-three parameter

Every member of this intrinsic mixed-fiber family has a polynomial
element of N-degree three whose reduced values are nonconstant on
both components. Finite monic preparation recovers it without
inverting x. The resulting cubic presentation and the full
degree-three module hold over the original invariant plane.

This is not an original four-coordinate E-frame. It tests a
specific intrinsic obstruction: the specified parameter c has
N-degree four, but that does not prevent a hidden degree-three
parameter from varying on both mixed components.

## 1. The polynomial family and its whole mixed fiber

For an integer m at least one, put
\[
\begin{gathered}
\mathcal A=\mathbb C[x,y,c],\qquad H(y)=y^2(y-1),\\
f=H(y)+xy^4+x^m c,\qquad S=\mathbb C[x,f],\\
N=-x^m\partial_y+(3y^2-2y+4xy^3)\partial_c
 =\det\frac{\partial(x,f,\,\cdot\,)}{\partial(x,y,c)},\\
Nx=Nf=0,\qquad
\mathfrak m=(x,f)S,\qquad
\mathcal A/\mathfrak m\mathcal A
 =\mathbb C[y,c]/(y^2(y-1))
 \simeq\mathbb C[\epsilon,c]/(\epsilon^2)\times\mathbb C[c].
\end{gathered}
\tag{1}
\]
The double component is y=0 and the simple component is y=1.
The variables x,f are algebraically independent, since solving
for c after inverting x gives \(\mathcal A_x=S_x[y]\).
The coefficients of N have gcd one: x does not divide
\(3y^2-2y+4xy^3\). N is therefore the primitive polynomial
base Jacobian. Weight x by zero, y by one and c by four.
Every term of N strictly lowers this nonnegative weight, proving
local nilpotence on the actual polynomial ring.

The full kernel and faithful flatness over S are proved below.
They are not inferred from the displayed coefficient prescription.

## 2. Constructive monic preparation in the x-adic ring

Use an independent variable t. There is a unique formal series
\(\alpha\in\mathbb C[t][[x]]\) with constant coefficient -1 satisfying
\[
\begin{gathered}
\alpha=-1+x\alpha^2-\frac{x^2t}{(1-x\alpha)^2},\qquad
q=1-x\alpha,\qquad
\beta=\frac{xt}{q^2},\qquad \gamma=-\frac{t}{q},\\
g=y^3+\alpha y^2+\beta y+\gamma,\\
xy^4+y^3-y^2-t=(xy+q)g.
\end{gathered}
\tag{2}
\]
All divisions in this formula are by formal units with constant
coefficient one. For each positive n, the coefficient of x to
the n on the right side of the first equation depends only on
earlier coefficients of alpha. This determines alpha uniquely,
with polynomial coefficients in t, by ordinary recursion.

For the factorization, the coefficients of y to the fourth and
third are x and \(x\alpha+q=1\). The coefficient of y squared
is \(x\beta+q\alpha=-1\) by the recursion. The coefficient of y
is \(x\gamma+q\beta=0\), and the constant term is \(q\gamma=-t\).
This proves the identity directly, without invoking a preparation
theorem or assuming an algebraic global change of coordinates.

Let \(\alpha_{<m},\beta_{<m},\gamma_{<m}\) be the truncations
through x-degree m-1, and set
\[
\begin{gathered}
g_m(x,t,y)=y^3+\alpha_{<m}y^2+\beta_{<m}y+\gamma_{<m}
 \in\mathbb C[x,t,y],\\
xy^4+y^3-y^2-t
 =q_m(x,t,y)g_m(x,t,y)+x^m R_m(x,t,y),\\
q_m=xy+1-x\alpha_{<m},\qquad
R_m\in\mathbb C[x,t,y],\qquad \deg_y R_m\le2,\\
\boxed{\quad U=\frac{g_m(x,f,y)}{x^m}\in\mathcal A.\quad}
\end{gathered}
\tag{3}
\]
Here the second line is ordinary polynomial division by the
monic cubic gm. Its quotient is the indicated qm by comparison
of the two leading coefficients. Its remainder is divisible by
x to the m: modulo that power, equation (2) factors the quartic
by gm, with quotient \(xy+q\). Thus Rm is a polynomial.

To prove the boxed polynomial assertion, work in the actual ring
\(\mathcal A/(x^m)\). There f equals \(H(y)+xy^4\), so the
left side of the second line vanishes after t=f. The quotient
qm has residue one modulo x, hence is a unit modulo x to the m.
Consequently \(g_m(x,f,y)=0\) in this quotient. This proves
divisibility in the polynomial ring itself, not merely in a
completion or a rational extension.

## 3. Exact degrees and a cubic presentation

The coefficients of gm belong to S after t=f and are invariant.
Differentiating the polynomial identity \(x^mU=g_m(x,f,y)\)
in the domain gives
\[
\begin{gathered}
NU=-(3y^2+2\alpha_{<m}(x,f)y+\beta_{<m}(x,f)),\\
N^2U=x^m(6y+2\alpha_{<m}(x,f)),\qquad
N^3U=-6x^{2m}\ne0,\qquad N^4U=0,\\
N^2c=-x^m(6y-2+12xy^2),\qquad
N^3c=x^{2m}(6+24xy),\\
N^4c=-24x^{3m+1}\ne0,\qquad N^5c=0.
\end{gathered}
\tag{4}
\]
Thus U has degree exactly three and the specified c has degree
exactly four for every m.

After t=f, the quartic on the left side of (3) equals
\(-x^m c\). Cancelling x to the m gives
\[
\begin{gathered}
c=-q_m(x,f,y)U-R_m(x,f,y),\qquad
\boxed{\quad\mathcal A=S[y,U].\quad}\\
\boxed{\quad
\mathcal A\simeq
S[Y,W]/\bigl(g_m(x,f,Y)-x^mW\bigr),
\qquad Y\longmapsto y,\quad W\longmapsto U.
\quad}
\end{gathered}
\tag{5}
\]
The first formula proves surjectivity. The proposed source is
free over S[W] with basis 1,Y,Y squared, since the relation is
monic in Y. In particular it is x-torsion-free. After inverting
x its map to \(\mathcal A_x=S_x[y]\) is an isomorphism, with W
solved for by the relation. Its original kernel is therefore
zero. This proves the exact presentation.

The same source is a nonzero free S-module, so \(S\to\mathcal A\)
is faithfully flat. In particular this is a flat quotient of
an actual smooth polynomial threefold, not just a formal cubic
relation with arbitrary coefficient data.

## 4. The parameter survives on both components

Let \(\alpha_m(t),\beta_m(t),\gamma_m(t)\) denote the coefficients
of x to the m in the full series of (2), and put
\(d_m(t,y)=\alpha_m(t)y^2+\beta_m(t)y+\gamma_m(t)\).
Then
\[
\begin{gathered}
U\bmod x=-c-d_m(H(y),y)
 \quad\text{in }\mathbb C[y,c],\\
\boxed{\quad
U\bmod(x,f)=-c+(-1)^m C_m y^2
 \quad\text{in }\mathbb C[y,c]/(y^2(y-1)),\quad}\\
C_m=\frac{1}{m+1}\binom{2m}{m},\\
U|_{\text{double, reduced}}=-c,\qquad
U|_{\text{simple}}=-c+(-1)^m C_m.
\end{gathered}
\tag{6}
\]
For the first equality, substitute the polynomial f into the
formal factorization. This substitution is well defined in the
x-adic topology because each series coefficient is polynomial
in t. It gives \(g(x,f,y)=-x^m c/(xy+q(x,f))\).
Moreover \(g-g_m=x^m d_m+O(x^{m+1})\). The unit factor has
residue one, and f modulo x is H(y), proving the first line.

At t=0 the recursion reduces to \(\alpha=-1+x\alpha^2\),
while beta and gamma vanish. Its coefficients are
\(\alpha_m(0)=(-1)^{m+1}C_m\), as follows by the formal quadratic
formula or the Catalan convolution recursion. On the whole
fiber H(y)=0, so the first line becomes the boxed formula.
The nilpotent structure is retained: y squared is zero in the
double factor and one in the simple factor.

The induced derivation is \(H'(y)\partial_c\). Its values on
the two factors are \(-2\epsilon\partial_c\) and \(\partial_c\).
The residue of NU is \(-H'(y)\), nonzero on both factors.
Thus the surviving parameter is genuinely nonconstant on both
reduced components; this is not a statement only about a generic
localization of one of them.

For m at least two the first normal action on the double prime
\(\mathfrak p=(x,y)\) is zero, since \(N\mathfrak p\subset\mathfrak p^2\).
For m equal to one, \(Ny=-x\) gives nonzero first normal action.
The hidden degree-three parameter exists in both cases.

## 5. Full kernel and low-degree modules

There is no denominator or bounded coefficient-degree restriction:
\[
\boxed{\quad
\ker N=S,\qquad
\ker N^3=S\oplus Sy\oplus Sy^2,\qquad
\ker N^4=S\oplus Sy\oplus Sy^2\oplus SU.
\quad}
\tag{7}
\]
After inverting x, N equals \(-x^m\partial_y\) with S fixed.
The localized modules therefore have the indicated bases.
For the cubic module, monicity of gm gives the basis change
between 1,y,y squared,y cubed and 1,y,y squared,U.

For any proposed polynomial element with an x denominator,
choose the denominator exponent positive and minimal. Reduce
its numerator modulo x. Equation (6) says that the coefficient
of c in the U term is minus its coefficient evaluated at
\(f=H(y)\). Thus that coefficient is divisible by x. The
remaining relation has the form
\(A_0(H(y))+A_1(H(y))y+A_2(H(y))y^2=0\).
The monic cubic H makes \(\mathbb C[y]\) free over
\(\mathbb C[H(y)]\) with basis 1,y,y squared, so all three
coefficients vanish. All numerator coefficients are therefore
divisible by x, contradicting minimality.

The same argument without the U term proves the degree-two
module, and with only its scalar term proves the kernel.
This is the complete polynomial saturation argument. It does
not infer freeness or saturation from finitely many examples.

Every degree-two residue is consequently an element of the
constant Artin algebra \(\mathbb C[y]/(H(y))\), while U in
degree three supplies the missing parameter. This matches a
possible intrinsic mixed-module pattern without asserting that
an original E-frame realizes it.

## 6. Small exact instances

The first two polynomial hidden parameters are
\[
\begin{gathered}
m=1:\quad U=-c-y^4,\\
m=2:\quad U=-c+y^4(y+1)+xc(y+1).
\end{gathered}
\tag{8}
\]
These formulas follow directly from the truncations
\(g_1=y^3-y^2-t\) and
\(g_2=y^3-y^2-t+x(y^2+ty+t)\).
For m equal to two, the extra x times c term illustrates why
one must retain actual polynomial corrections rather than
merely guess a residue-class lift.

## 7. An exact failure of the actual quadratic-frame hypothesis

The obstruction to treating this family as the supplied actual
quadratic frame is explicit, not merely a missing inverse check.
The invariant prime x remains prime in the polynomial threefold.
Its whole generic divisor has
\[
\begin{gathered}
k_x=\mathbb C(f)=\mathbb C(H(y)),\qquad
\operatorname{Frac}(\mathcal A/(x))=\mathbb C(y)(c),\\
(\mathcal A/(x))\otimes_{\mathbb C[f]}k_x=\mathbb C(y)[c],\\
\operatorname{AlgCl}_{\,\mathbb C(y)(c)}(k_x)=\mathbb C(y),
\qquad [\mathbb C(y):\mathbb C(H(y))]=3.
\end{gathered}
\tag{9}
\]
Here AlgCl means the relative algebraic closure, namely the
subfield of elements algebraic over the indicated base field.
To prove the degree, \(H(Y)-t\) is irreducible in
\(\mathbb C[t,Y]\): its quotient is the domain \(\mathbb C[Y]\),
and its principal ideal is prime. It is primitive over
\(\mathbb C[t]\), so Gauss's lemma makes it irreducible of
degree three in \(\mathbb C(t)[Y]\). Consequently
\(k_x[y]=\mathbb C(y)\), proving the generic-divisor ring
description as well.

Write \(K'=\mathbb C(y)\). Every element of K' is algebraic
over kx. Conversely K' is relatively algebraically closed in
the rational extension K'(c). Indeed any rational function in
c not belonging to K' makes c algebraic over the field it
generates with K', by its numerator-denominator equation. If
that function were algebraic over K', this would contradict
the transcendence of c. Thus an element of K'(c) algebraic
over kx must belong to K'. This proves the exact relative
closure, not only the inclusion of a cubic subextension.
The induced derivation is \(H'(y)\partial_c\); its coefficient
is nonzero in K', and its kernel is exactly K'.

The supplied actual quadratic frame requires each such divisor
constant extension to have degree at most two, as stated in
[source balance97, Section 1](quadratic-saturated-source-balance-pass97.md)
and proved from the actual relative degree and whole-divisor
noncollapse in
[residue degree91](nonconical-residue-degree-bound-pass91.md).
Equation (9) violates that requirement. Therefore this exact
invariant inclusion S into the displayed polynomial threefold
cannot instantiate the supplied actual quadratic frame.
It does not exclude other actions or different invariant
inclusions on the same polynomial threefold.

## Scope

The construction extends the mixed cubic model by a genuine
quartic perturbation; it does not reuse the whole-double
Catalan family of104 as a mixed-fiber conclusion. The
finite recursion, unit-modulo-x gate, exact cubic presentation,
whole-fiber residues and full modules are proved here for the
displayed family only.

No universal hidden-parameter existence, recognition or
cancellation assertion is supplied. The ambient threefold is
already polynomial. The constructive argument is source-free;
the exact actual-frame failure uses the linked retained
hypothesis, whose proofs were reread, not a fresh primary-source
audit. All files through104 remain unchanged.

The standalone [finite mixed-quartic checker](mixed_quartic_cubic_checks_pass105.py)
has one method with m=1 through5 subtests. It constructs the
truncated factors by successive monic polynomial division,
independently compares the formal recurrence, and checks actual
polynomial recovery, derivative orders, both mixed residues,
and finite module samples. Its rank-twelve coefficient check
does not establish the all-polynomial saturation theorem.
The first assertion-bearing author run passed one method in
0.981 seconds, exit zero; tool chunk 5a3125 began the run and
aab7e1 contains its completion. No full regression was run.
