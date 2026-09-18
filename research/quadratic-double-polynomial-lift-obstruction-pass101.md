# A full polynomial obstruction to the nilpotent slice correction

In the primitive triangular family below, the quadratic coefficient
permitted by the whole-fiber calculation100 does not lift to an element
of full N-degree at most two. This rules out all polynomial corrections,
not just a finite jet ansatz, by an exact free-module computation.

These are smooth polynomial threefolds with a genuine canonical base
Jacobian. They are not supplied with the original four-coordinate frame
or its highest-adjoint kernel. This result does not eliminate the
remaining actual sector in100.

## 1. The intrinsic family and the exact degree-two module

For an integer m at least one, set
\[
\begin{gathered}
A_0=\mathbb C[x,y,c],\qquad f=y^2+x^m c,\qquad S_0=\mathbb C[x,f],\\
N=-x^m\partial_y+2y\partial_c
 =\det\frac{\partial(x,f,\,\cdot\,)}{\partial(x,y,c)},\\
\mathfrak m_0=(x,f)S_0,\qquad \mathfrak p=(x,y)A_0,\qquad
A_0/\mathfrak m_0A_0=\mathbb C[c,y]/(y^2),\\
\boxed{\quad \ker(N^3)=S_0\oplus S_0y\oplus S_0c.\quad}
\end{gathered}
\tag{1}
\]
Here the kernel of N cubed is the vector-space kernel of the third
iterate, not the invariant ring. The direct sum is as an S0-module.
We prove both the equality and its freeness.

N kills x,f. Giving x weight zero, y weight one and c weight two
makes N decrease weight, so N is locally nilpotent on A0. The functions
x,f are algebraically independent, as also follows from the exact
localized presentation
\[
\begin{gathered}
(A_0)_x=\mathbb C[x,x^{-1},f,y]=(S_0)_x[y],
\qquad c=(f-y^2)/x^m,\\
N=-x^m\partial_y\text{ with }x,f\text{ fixed},\\
\ker\bigl(N^3|(A_0)_x\bigr)
 =(S_0)_x\oplus(S_0)_x y\oplus(S_0)_x c.
\end{gathered}
\tag{2}
\]
In characteristic zero a polynomial has third derivative zero exactly
when its degree is at most two. Replace y squared by f minus x to the
m times c. The change from the basis 1,y,y squared to 1,y,c is invertible
after inverting x. Thus 1,y,c are also S0-linearly independent.

There are no hidden x-denominators in this module. For h in A0 and in
the last module of (2), choose the smallest nonnegative k clearing a
common denominator:
\[
\begin{gathered}
x^k h=A_0(x,f)+A_1(x,f)y+A_2(x,f)c,\qquad A_i\in\mathbb C[x,f],\\
k>0\quad\Longrightarrow\quad
A_0(0,y^2)+A_1(0,y^2)y+A_2(0,y^2)c=0
\quad\text{in }\mathbb C[y,c],\\
\Longrightarrow\quad x\mid A_0,\quad x\mid A_1,\quad x\mid A_2.
\end{gathered}
\tag{3}
\]
Independence of c first forces A2(0,y squared) to vanish. Substitution
from C[f] to C[y], sending f to y squared, is injective. The two
remaining terms have opposite parity in y, so each vanishes separately.
This proves the last line. Dividing by x contradicts minimality of k.
Therefore k is zero. Conversely each of 1,y,c has third iterate zero.
This proves (1) for arbitrary coefficient degrees and arbitrary h.

## 2. Kernel, quotient and first normal action

Applying N to the unique expression in (1) gives
\[
\begin{gathered}
N(A_0+A_1y+A_2c)=-x^m A_1+2A_2y,\qquad \ker N=S_0,\\
\gcd(x^m,2y)=1,\qquad N^3x=N^3y=N^3c=0,\\
m\ge2\quad\Longrightarrow\quad N(\mathfrak p)\subset\mathfrak p^2,\\
m=1\quad\Longrightarrow\quad
Nx=0,\quad Ny\equiv-x\not\equiv0\pmod{\mathfrak p^2}.
\end{gathered}
\tag{4}
\]
Independence forces A1 and A2 to vanish when the first line is zero.
Conversely S0 is invariant. The coefficient gcd proves primitivity.
The fixed scheme is defined by (x to the m,y), with the entire c-line
as its reduced support.

The base map is faithfully flat directly: A0 is free over S0[c],
with basis 1,y, by its monic equation y squared plus x to the m times
c minus f. Consequently it is a nonzero free, faithfully flat module
over S0. Its origin whole fiber is the double line in (1), free of
rank two over the specified C[c]. The standard polynomial volume
gives the canonical Jacobian in (1). Thus the family has considerably
more structure than an Artin-only control, but no original
constant-acceleration frame is being inferred.

## 3. The nilpotent coefficient cannot vary in c

Suppose N cubed h is zero and h has constant reduced restriction eta
on p. Its unique expression in (1), reduced first on the reduced
curve and then on the whole double fiber, yields
\[
\begin{gathered}
A_2(0,0)=0,\qquad A_0(0,0)=\eta,\qquad d=A_1(0,0)\in\mathbb C,\\
\boxed{\quad h\equiv\eta+d y\pmod{\mathfrak m_0A_0}.\quad}
\end{gathered}
\tag{5}
\]
The reduced restriction is A0(0,0) plus A2(0,0)c, and c is
transcendental on the reduced line. On the whole fiber x and f
vanish, proving the exact equality (5), including its nilpotent term.

For the more precise first normal expression, let subscripts on Ai
denote partial derivatives with respect to their formal variables
x,f, evaluated at (0,0). Then
\[
\begin{array}{ll}
m\ge2:&
h\equiv\eta+(A_{0,x}+cA_{2,x})x+d y\pmod{\mathfrak p^2},\\[2pt]
m=1:&
h\equiv\eta+
\bigl(A_{0,x}+cA_{0,f}+cA_{2,x}+c^2A_{2,f}\bigr)x
+d y\pmod{\mathfrak p^2}.
\end{array}
\tag{6}
\]
For m at least two, f belongs to p squared. For m equal to one its
first normal class is xc, which explains the additional terms.
The x-coefficient bounds are sharp: xc has an affine coefficient
for m at least two, and fc has a quadratic coefficient for m equal
to one.

In every case the y coefficient is the constant d. Therefore no
polynomial h with third iterate zero can have first normal form
eta plus alpha(c)x plus cy, or with c squared y in place of cy.
Arbitrary terms in p squared cannot repair either candidate.
This uses the full module equality, not the leading cubic100.

The uncorrected candidates and their localized repairs illustrate
the distinction:
\[
\begin{gathered}
N^3(yc)=6x^{2m},\qquad
N^3(yc^2)=12x^{2m}c-48x^m y^2,\\
\widetilde h_1=yc+\frac{y^3}{x^m}
 =\frac{yf}{x^m},\qquad N^3\widetilde h_1=0,\\
\widetilde h_2=yc^2+\frac{2y^3c}{x^m}
 +\frac{y^5}{x^{2m}}=\frac{yf^2}{x^{2m}},
\qquad N^3\widetilde h_2=0.
\end{gathered}
\tag{7}
\]
The repairs exist after inverting x but are not polynomial at the
fixed curve. Equation (3), not the failure of these particular
repairs, rules out all polynomial repairs with the specified
first normal coefficient.

## 4. An explicit base-preserving polynomial shear

One elementary deformation is only a change of coordinates. For
P in C[x,y], put
\[
\begin{gathered}
C=c+P(x,y),\qquad c=C-P(x,y),\qquad
f_P=y^2+x^m(c+P(x,y)),\\
N_P=-x^m\partial_y+(2y+x^mP_y)\partial_c,\qquad
N_PC=2y,\qquad N_Py=-x^m,\\
S_P=\mathbb C[x,f_P],\qquad
\ker(N_P^3)=S_P\oplus S_Py\oplus S_PC.
\end{gathered}
\tag{8}
\]
Both inverse orders in the first line are polynomial and the
coordinate determinant is one. Thus (8) is exact transport of (1),
not a new classification. The normal generators x,y are unchanged.
On their reduced curve C equals c plus the constant P(0,0). For a
constant reduced residue the whole-fiber form is still eta plus d y;
this stated shear cannot introduce a nonconstant beta.

For example take \(P=y^4+xy+1\). Then
\(N_P^3c=24x^{3m}y\ne0\) and \(N_P^5c=0\), while
\(N_P^3C=0\). Thus the constant-beta obstruction also holds in
this explicit sheared model where the specified c has degree four,
not two, for N. This is not a silent renaming of that specified c.

We do not identify C with a different specified component parameter
in an arbitrary actual frame. More general base maps and changes of
the normal generators require their own argument. In particular
nothing here says every zero-first-normal field is conjugate to
this family.

## Scope and dependencies

The motivation is the remaining nilpotent coefficient in
[whole-fiber actions100](quadratic-whole-fiber-actions-pass100.md).
The intrinsic m equal to two family was already retained as a
square-versus-full-square boundary in
[zero-normal-row98](quadratic-zero-normal-row-pass98.md).
The new result is the exact all-polynomial degree-two module and
its obstruction to the prescribed lift, with the m equal to one
distinction and the explicitly transported shear.

All equalities and saturation steps are proved above. No new
primary-source theorem, completion-localized LND assertion,
original four-coordinate frame, or recognition claim is used.
All files through100 remain unchanged.

The [standalone checker](quadratic_polynomial_lift_checks_pass101.py)
now has two methods. Its first method has m equal to one, two and
three as subtests. It checks sample module coefficients and their exact first normal
and whole-fiber residues, the two nonzero cubic iterates, their
localized repairs, both inverse orders of the stated polynomial
shear, and its actual degree-four c. A twelve-column parity table
is only a finite control of the all-degree argument in (3).
It does not certify the universal module theorem or an original
four-coordinate frame. No older solver or checker is imported.
The second method is a distinct intrinsic base-order noniteration
control supplied by Geometry; it is not an additional verification
of the module theorem here.

The historical first author execution passed one method in 0.333 seconds,
exit zero, with full output in chunk aa922a (wall time
0.585151042 seconds). After adding the second method, the final
two-method author run passed in 0.340 seconds, exit zero, with
full output in chunk bd5e73 (wall time 0.592544750 seconds).
No assertion failed and no full regression was run.
An initial patch-formatting attempt to create this note
was rejected before file creation; the successful saved proof
was read through EOF with all displayed signs checked.
