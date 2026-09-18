# Original volume splits a constant normal row

At a collapsed double component of the supplied quadratic frame,
a nonzero speed normal forces one original normal coordinate into
the whole fiber ideal. Its centered conormal class has a constant
left inverse from the base. Consequently the quotient conormal row
is constant, and its normalized column is affine in the actual
component parameter. Zero first normal action makes the entire
conormal matrix constant.

In particular the nonconstant zero-normal row sector considered
in98 and in the conditional companion calculation99 is impossible
when the speed normal is nonzero. This does not exclude the
remaining constant case, recognize A, or treat points where that
normal vanishes.

## 1. The exact global identity, before specialization

Retain the actual nonconical quadratic frame through
[checkpoint98](checkpoint-pass98-working.json). Write the original
good-coordinate column as x_tr. The actual centered column and
the original-volume identity are
\[
\begin{gathered}
B=\mathbb C[x_1,x_2,x_3,z]=A[u],\qquad E=\partial_u,
\quad E^2x_i=0,\quad E^2z=q_0\in\mathbb C^*,\\
S=\ker(N|_A)=\mathbb C[s_1,s_2],\qquad
\mathbf b=Ex_{\rm tr}\in S^3,\qquad
L=\mathbf b_{s_1}\times\mathbf b_{s_2},\qquad
\Omega=L\cdot\mathbf b\ne0,\\
\mathbf a=x_{\rm tr}-u\mathbf b
 =-\mathbf b h+v_2A_1+v_3A_2\in A^3,\\
\boxed{\quad L(s)\cdot\mathbf a=\kappa(s)\in S.\quad}
\end{gathered}
\tag{1}
\]
The last equality is global, as proved in
[volume88](constant-acceleration-volume-descent-pass88.md).
Its sign also follows from
\(\Omega h=(L\cdot v_2)A_1+(L\cdot v_3)A_2-\kappa\).
No denominator or localization has been introduced.

Let C be a collapsed fixed double component over a closed point
\(\mathfrak m\subset S\), with ideal \(\mathfrak q\).
The [actual plane theorem92](nonconical-collapsed-component-plane-pass92.md)
gives \(A/\mathfrak q=\mathbb C[\bar c]\), constant residues of
A_1,A_2 and h, and therefore
\(\mathbf a|_C=o\in\mathbb C^3\). Also
\(\Omega(\mathfrak m)=0\). Suppose
\(L_0=L(\mathfrak m)\ne0\), and put
\(\kappa_0=\kappa(\mathfrak m)=L_0\cdot o\).

Since \(L_0\cdot\mathbf b(\mathfrak m)=0\), the nonzero
constant row L_0 is an original good normal to the component plane.
Complete it by a second constant good normal Y and a good tangent
coordinate W. With an affine shift of Y, the exact equations and
their canonical centers are
\[
\begin{gathered}
\ell=L_0\cdot x_{\rm tr}-\kappa_0,\qquad
B=\mathbb C[\ell,Y,W,z],\qquad \mathfrak qB=(\ell,Y),\\
F=\ell-uE\ell=L_0\cdot\mathbf a-\kappa_0,\qquad
G=Y-uEY,\qquad \mathfrak q=(F,G),\\
\mathfrak q/\mathfrak q^2=
\mathbb C[c]\bar F\oplus\mathbb C[c]\bar G,
\qquad N^3F=N^3G=0.
\end{gathered}
\tag{2}
\]
The ideal equality follows by evaluating the actual polynomial
extension B=A[u] at u=0. The free conormal basis follows from the
smooth component in the smooth threefold and these two generators.
In particular F has a nonzero conormal class at every component
point. It is not being inferred to be an ambient coordinate.

## 2. Membership in the whole fiber and a constant left inverse

Subtract the exact identity (1) from the expression for F:
\[
\begin{gathered}
\boxed{\quad
F=(L_0-L(s))\cdot\mathbf a+\kappa(s)-\kappa_0
 \in\mathfrak mA.\quad}\\
E\ell=L_0\cdot\mathbf b(s)\in\mathfrak m^2\setminus\{0\},
\qquad \boxed{\quad\ell\in\mathfrak mB.\quad}
\end{gathered}
\tag{3}
\]
The speed has zero value and zero first base derivatives at
\(\mathfrak m\). It cannot be identically zero: then L_0 would
annihilate \(\mathbf b,\mathbf b_{s_1},\mathbf b_{s_2}\) globally,
contradicting \(\Omega\ne0\). Finally
\(\ell=F+uE\ell\) gives the actual-coordinate membership in (3).

Put \(t_j=s_j-s_j(\mathfrak m)\). As
\(\mathbf a-o\in\mathfrak q A^3\) and
\(\mathfrak mA\subset\mathfrak q\), Taylor expansion of (3)
modulo \(\mathfrak q^2\) gives
\[
\begin{gathered}
F\equiv d_1t_1+d_2t_2\pmod{\mathfrak q^2},\qquad
d_j=\kappa_{s_j}(\mathfrak m)-L_{s_j}(\mathfrak m)\cdot o
 \in\mathbb C,\\
\binom{t_1}{t_2}\equiv C(c)\binom F G\pmod{\mathfrak q^2},
\qquad d C(c)=(1,0),\qquad d\ne0,\\
\boxed{\quad
\binom{x}{f}\equiv
\begin{pmatrix}1&0\\a(c)&0\end{pmatrix}
\binom F G\pmod{\mathfrak q^2},\qquad
\mathfrak m=(x,f),\qquad x=d_1t_1+d_2t_2.
\quad}
\end{gathered}
\tag{4}
\]
Here C(c) is the polynomial quotient conormal matrix. It has
generic rank one because the component is double; the retained
quotient-rank theorem95 rules out rank zero. The relation dC=(1,0)
itself also makes its rank nonzero everywhere.

For the Taylor step, the product
\((L_0-L)\cdot(\mathbf a-o)\) belongs to \(\mathfrak q^2\),
and every base Taylor remainder belongs to
\(\mathfrak m^2A\subset\mathfrak q^2\). Thus d is genuinely
constant, not a rational row depending on c.
Complete d to a constant invertible base matrix, whose second
coordinate is f. Its transformed C has first row (1,0).
Its determinant vanishes, so its second row has second entry
zero. This proves the constant normal row in (4), without any
first-normal-action assumption. Only a constant base change and
a constant affine original-coordinate change have been used.

## 3. The transverse coefficient is constant on the entire line

The polynomial a(c) in (4) is lifted using the specified c in A.
Let \(g=f-a(c)x\in\mathfrak q^2\). Its quadratic normal class
has polynomial coefficients in the free associated graded ring
\(\mathbb C[c][\bar F,\bar G]\). Define its transverse coefficient by
\[
\begin{gathered}
g\equiv Q_2(c;F,G)\pmod{\mathfrak q^3},\qquad
b(c)=Q_2(c;0,1),\qquad
\boxed{\quad b(c)=b\in\mathbb C^*.\quad}
\end{gathered}
\tag{5}
\]
At every c_0 the entire component thickening is free of rank two
over the actual \(\mathbb C[c]\), by
[the whole-thickening proof95](quadratic-quotient-rank-everywhere-pass95.md).
Thus its transverse section c=c_0 has length two. On the regular
surface defined by that section, x has nonzero linear normal term F.
Quotienting by x leaves a regular local curve with parameter G.
The equation f=g there has order exactly two, forcing
b(c_0) nonzero. Nonlinear terms of x do not alter this quadratic
coefficient, because g has no linear normal term.

It follows that b has no complex zero and is constant. The use of
g here does not require N-invariance of g. The actual derivation
below is computed from the invariant base parameters x,f, not x,g.

## 4. The actual cubic identity makes the column affine

At the generic point of C, complete with the actual coefficient
field \(\mathbb C(c)\), parameters x,y=G and weights two,one.
The retained actual volume ratio is a constant \(\nu\in\mathbb C^*\)
along the component, since x has the same linear normal class as F.
The weighted leading formula is therefore
\[
\begin{gathered}
f_*=a(c)x+b y^2,\qquad
D_* =\nu\bigl(-a'(c)x\partial_y+2b y\partial_c\bigr),\\
D_*y=-\nu a'x,\qquad
D_*^2y=-2\nu^2b a''xy,\\
D_*^3y=2\nu^3b a'a''x^2-4\nu^3b^2a'''xy^2=0,\\
\boxed{\quad a(c)=a_0+a_1c,\qquad a_0,a_1\in\mathbb C.\quad}
\end{gathered}
\tag{6}
\]
The zero in the third line is the weight-four part of the actual
identity N^3G=0. Strictly higher terms have greater operator weight
and cannot cancel either displayed coefficient. Since b and nu are
nonzero, \(a'a''=0\). In the polynomial domain either a' is zero,
which already makes a constant, or a'' is zero. Thus a is affine
in both cases. No N^5c identity or local nilpotence on the completed
ring is used.

The ordinary first normal action is
\(NF\equiv0\), \(NG\equiv-\nu a_1F\pmod{\mathfrak q^2}\).
Consequently zero first normal action is exactly a_1=0. In that
case both entries of the quotient column in (4) are constant.
When a_1 is nonzero, its column span is \(\{1,c\}\). These remain
conormal statements: (6) does not imply N^2G=0 in A.

## 5. A stronger common second-order inclusion

The exact identity (3) has additional consequences independent of
the first normal action. N kills S, and it preserves each reduced
fiber component. Since \(\mathbf a\) restricts to constants on a
collapsed component, \(N\mathbf a\in\mathfrak q A^3\).
Differentiation yields
\[
\begin{gathered}
NF=(L_0-L)\cdot N\mathbf a\in\mathfrak mA\,\mathfrak q,\\
N^2\mathbf a\in\mathfrak m S^3,\qquad
\boxed{\quad N^2F\in\mathfrak m^2S.\quad}\\
I=\sqrt{\mathfrak mA},\quad
\text{all components collapsed}\quad\Longrightarrow\quad
\boxed{\quad NF\in\mathfrak mA\,I\subset I^2.\quad}
\end{gathered}
\tag{7}
\]
For the second line, every entry of \(N^2\mathbf a\) lies in S
because N^3 kills every centered good coordinate. It also vanishes
on C, since N preserves its ideal. Its entries therefore belong
to \(S\cap\mathfrak q=\mathfrak m\). The same two-factor argument
as for NF now gives N^2F in the base square.

In a mixed (2,1) fiber with L_0 nonzero, both components are
collapsed by98, and the same F from (3) is common to them. Hence
the final line applies without a zero-normal or nonconstant-row
assumption. It also applies to a whole collapsed double fiber.
These ideal containments are stronger than vanishing on the
reduced fiber, but weaker than the identities NF=0 or N^2F=0.

## 6. Whole-fiber consequence and remaining cases

The actual-coordinate membership \(\ell\in\mathfrak mB\) now
allows the [whole-plane-fiber proof99](quadratic-whole-plane-fiber-pass99.md)
to identify the entire scheme ideal, not merely its radical:
\[
\begin{array}{c|c|c}
\text{collapsed profile}&\mathfrak mB&\mathfrak mA\\ \hline
(2)&(\ell,Y^2)&(F,G^2)\\
(2,1)&(\ell,Y^2(Y-1))&(F,G^2(G-1)).
\end{array}
\tag{8}
\]
Its separate proof uses Cohen--Macaulayness of the whole fiber,
height-one primary contraction in B/(ell), and the actual
multiplicity lengths. It does not replace a nilpotent thickening
by its reduction.

The previous
[nonconstant zero-normal compatibility calculation99](quadratic-zero-normal-companion-compatibility-pass99.md)
is a valid conditional deduction in a now-empty actual sector
when L_0 is nonzero. Its second-order NF inclusion is replaced
by the stronger unconditional-in-first-normal-action statement (7).
For zero first normal action, the nonconstant row forms of98 can
now occur only in the still-untreated sector L(m)=0. This is a
necessary condition, not an assertion that those forms occur.

Whole double fibers and mixed fibers with constant conormal data
have not been excluded. Nor does the original hyperplane lying in
the fiber ideal make it invariant: its E-speed in (3) is nonzero.
No coordinate recognition or arbitrary-frame reduction follows.

## Scope and proof provenance

Root derived the exact whole-fiber membership, constant left inverse,
affine-column refinement, and base-square second derivative.
Geometry, Jet and General independently reconstructed the volume
sign, constant residue, conormal basis, left-inverse and zero-normal
exclusion before this note was saved. Jet independently checked
the all-point transverse coefficient and weighted cubic refinement.
Geometry proposed the whole-scheme corollary; General independently
checked its global primary-contraction and multiplicity gates.

Root reread volume88, collapsed-plane92 and global-Jacobian91
through EOF for their exact identities. The completion, volume
factor and whole-thickening dependencies retain their audited
93--98 scope. The separate
[finite symbolic checker](quadratic_volume_normal_checks_pass99.py)
tests only the displayed coefficient algebra, not those universal
geometric hypotheses. Saved-file reviews and execution evidence
must be recorded separately before integrating this working99 note.
No file through98, source novelty claim, human review, Lean proof,
external message or general cancellation conclusion is changed.
