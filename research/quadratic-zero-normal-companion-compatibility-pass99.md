# The two conormal layers share a constrained constant base frame

Suppose an actual quadratic (2,1) fiber has nonzero speed normal at
its base value. If the double component has zero first normal
N-action and a nonconstant conormal row, both planes admit one
constant base frame in which their quotient conormal matrices have
the forms below. The shared centered normal has N-image in the
square of the radical of the entire fiber.

These are compatibility restrictions on actual components. They do
not make that normal invariant or exclude the fiber. No coefficient
calculation is promoted from a leading derivation to the full action.

Current status: the independent
[volume-normal splitting99](quadratic-volume-normal-splitting-pass99.md)
excludes this actual nonconstant zero-normal row sector when
L(m) is nonzero. The deductions below remain conditional diagnostics.
Their NF inclusion is superseded by the stronger
\(NF\in\mathfrak mA\sqrt{\mathfrak mA}\), which needs no
first-normal-action hypothesis when all components are collapsed.

## 1. The actual common planes and the speed derivative

Retain the actual frame and conclusions of
[companion-collapse98](quadratic-normal-companion-collapse-pass98.md).
Write C2 for the fixed double component and C1 for the simple one.
The assumption is \(L(\mathfrak m)\ne0\). The common original good
coordinates and their canonical centers satisfy
\[
\begin{gathered}
B=\mathbb C[\ell,Y,W,z]=A[u],\qquad
\mathfrak q_2B=(\ell,Y),\quad
\mathfrak q_1B=(\ell,Y-1),\\
F=\ell-uE\ell,\quad G=Y-uEY,\quad
\mathfrak q_2=(F,G),\quad \mathfrak q_1=(F,G-1),\\
A/\mathfrak q_i=\mathbb C[\bar c],\qquad
N^3F=N^3G=0,\qquad E\ell\in\mathfrak m^2\setminus\{0\}.
\end{gathered}
\tag{1}
\]
The two uses of \(\mathbb C[\bar c]\) are the restrictions of the
same actual polynomial c to two different component rings.

Put \(h=EY\in S\). Both planes are E-stable, so \(h(\mathfrak m)=0\).
In any constant coordinates of the invariant plane, the two normal
speed derivatives form a constant matrix B0. It has first row zero.
It has rank exactly one: the two vectors
\(\mathbf b_{s_1}(\mathfrak m),\mathbf b_{s_2}(\mathfrak m)\)
are independent because L is nonzero, while their span contains
the nonzero vector \(\mathbf b(\mathfrak m)\) because Omega vanishes.
Projection to the normal two-space modulo that vector therefore
has rank one. In particular \(dh(\mathfrak m)\ne0\).

Choose a constant affine base-coordinate change x,f centered at
\(\mathfrak m\) so that \(dx(\mathfrak m)=dh(\mathfrak m)\).
Then
\[
\begin{gathered}
\mathfrak m=(x,f),\qquad h=x\pmod{\mathfrak m^2},\qquad
B_0=\begin{pmatrix}0&0\\1&0\end{pmatrix},\\
\binom{x}{f}\equiv C_2(c)\binom F G\pmod{\mathfrak q_2^2},
\qquad
\binom{x}{f}\equiv C_1(c)\binom F{G-1}\pmod{\mathfrak q_1^2},\\
\operatorname{tr}(B_0 C_i(c))=0.
\end{gathered}
\tag{2}
\]
Both matrices have polynomial entries in the actual c.

Here the trace is an original-coordinate identity, not a nonlinear
Jacobian transformation rule. On either plane the trace of the
original velocity Jacobian is the trace of its normal 2-by-2
block. The W-speed is constant along the plane, and the last
diagonal derivative is \(q u_z=0\) there. The original Jacobian
has zero trace. At the canonical section u=0, the original normal
generators and their centered versions agree to first order:
the correction \(uE(\ell,Y)\) has zero normal differential at
that section because both speeds vanish on the plane. Thus
the normal block there is exactly B0 times the displayed C_i.
This proves the last identity for every value of c.

## 2. A nonconstant zero-normal row kills the double speed layer

Assume \(N(\mathfrak q_2)\subset\mathfrak q_2^2\), and assume its
unimodular conormal row is nonconstant. Precisely, its two polynomial
entries span a two-dimensional complex space, equivalently its
projective row direction is nonconstant: a one-dimensional
unimodular span could only have constant entries.

The [zero-normal-row theorem98](quadratic-zero-normal-row-pass98.md)
gives \(C_2=\ell_0\rho(c)\), with \(\ell_0\) a nonzero constant
column and \(\rho(c)\) a unimodular polynomial row of degree at
most two. Equation (2) says
\(\rho(c)B_0\ell_0=0\). The entries of rho are complex-linearly
independent, so \(B_0\ell_0=0\). Rescaling the row puts
\[
\boxed{\quad
C_2(c)=\begin{pmatrix}0&0\\p(c)&q(c)\end{pmatrix},
\qquad (p,q)=\mathbb C[c],\qquad \deg p,\deg q\le2,
\qquad B_0C_2=0.
\quad}
\tag{3}
\]
Thus x and h have no linear conormal term along the double
component. This conclusion uses both the nonconstant row and
the nonzero speed normal. It need not hold merely from zero
first normal action with a constant row.

## 3. The simple layer is invertible and has a quadratic shear

On C1 the actual canonical N induces a nonzero LND of
\(\mathbb C[\bar c]\), hence a constant translation
\(N\bar c=\delta\in\mathbb C^*\). This is the retained
multiplicity-one component theorem95. In particular the
quotient differential has rank two at every point of C1.
The differentials \(dF,d(G-1)\) are a normal basis, so C1(c)
is invertible at every complex value of c.

By (2) its top-right entry is zero. Its diagonal entries
are polynomials whose product has no zero, so each is a
nonzero complex constant. Write
\[
\begin{gathered}
C_1(c)=\begin{pmatrix}k&0\\a(c)&b\end{pmatrix},
\qquad k,b,\delta\in\mathbb C^*,\qquad a\in\mathbb C[c],\\
NF\equiv0,\qquad
NG\equiv-\frac{\delta}{b}a'(c)F\pmod{\mathfrak q_1^2},\\
N^j(G-1)\equiv-\frac{\delta^j}{b}a^{(j)}(c)F
\pmod{\mathfrak q_1^2}\quad(j\ge1),\qquad
\boxed{\quad\deg a\le2.\quad}
\end{gathered}
\tag{4}
\]
Indeed x is invariant and \(x\equiv kF\), giving the first
N-congruence. Apply N to the invariant congruence
\(f\equiv a(c)F+b(G-1)\) for the second. The component ideal
and its square are N-stable. On its coefficient ring N acts
as the specific constant derivation \(\delta\,d/dc\), so
induction proves the third line. Finally \(N^3G=0\), the
nonzero constants and the free normal class of F force
\(a'''=0\).

This argument uses c as the actual affine coordinate on the
collapsed simple component. Merely having a rational parameter
with a nonconstant induced speed would not justify the displayed
ordinary derivatives or the degree bound.

## 4. The common second-order N-vanishing and different E-orders

Combining (3)--(4) with the hypothesis on the double component gives
\[
\begin{gathered}
I=\sqrt{\mathfrak mA}
 =\mathfrak q_2\cap\mathfrak q_1=(F,G(G-1)),\\
\boxed{\quad NF\in I^2,\qquad N^3F=0,\quad}\\
E\ell\in\mathfrak m^2\setminus\{0\},\qquad
h=EY\in\mathfrak q_2^2,\qquad
h\equiv kF\pmod{\mathfrak q_1^2},\qquad
h\notin\mathfrak q_1^2.
\end{gathered}
\tag{5}
\]
For the square identity, \(\mathfrak q_1+\mathfrak q_2=A\)
because their generators include G and G-1. Consequently their
squares are comaximal, and
\(\mathfrak q_1^2\cap\mathfrak q_2^2
=(\mathfrak q_1\mathfrak q_2)^2=I^2\).
This is a global ideal calculation, not generic ideal membership.
Also \(h-x\in\mathfrak m^2\) maps into either component-ideal
square. Equations (3)--(4) therefore give its two stated first
normal orders. The final nonmembership uses the nonzero normal
class kF on the simple component.

For reference, the shared scalar coordinate can be expressed in
the original ring with the same second-order conclusion:
\[
NF=N\ell,\qquad
N\ell\in
\bigl((\ell,Y)\cap(\ell,Y-1)\bigr)^2B.
\tag{6}
\]
Here \(Nu=0\) and \(N(E\ell)=0\) because the good speeds lie in S;
extending (5) along \(B=A[u]\) proves the inclusion.

Nothing above proves \(NF=0\), \(E\ell=0\), a global slice for N,
or impossibility of the two components. The relations are
compatible at the displayed first normal orders; a contradiction
would require another actual higher-order or global constraint.
They are not constructions of an original frame.

## Scope and provenance

The common original planes, nonzero second-order speed and
canonical centers are the actual statements of companion-collapse98.
The degree-two row theorem supplies precisely the zero-normal
hypotheses used here. The multiplicity-one translation and normal
bases are retained from95. No fresh primary-source theorem,
completion-LND assertion, numerical method, or change to a file
through98 is made. This compact compatibility result is separate
from Geometry's original \(J^3\) plane-matrix calculation.
