# The null cubic axis forces a rational scalar coefficient

In the supplied actual exact cubic framework, the null-axis scalar
D must lie in C(h), even if the full coefficient field is only known
to be finite over C(h). More precisely, D is either a cubic polynomial
with nonzero cubic coefficient or a polynomial of degree at most two
plus a nonzero reciprocal affine-linear term. This follows from the
first three lower coefficients of the actual volume determinant.

These necessary forms do not exclude the null-axis case. An explicit
rational coefficient control satisfies the complete generic potential
and unit-volume identities below. It is not an original polynomial
four-space frame and does not settle the remaining global conditions.

## 1. Actual hypotheses and the rational differential frame

Retain the full original-coordinate and generation hypotheses of
[cubic-relation90](nonconical-cubic-relation-pass90.md) and the null-axis
case of [the scalar normal forms121](cubic-axis-scalar-normal-forms-pass121.md).
Use q0 for the nonzero constant original acceleration. In particular,
\[
\begin{gathered}
S=\mathbb C[s,t],\quad K=\operatorname{Frac}S,\quad
L=\ker(V|K),\quad L/\mathbb C(h)\text{ finite separable},\\
\delta h=1,\quad L^\delta=\mathbb C,\quad D\in L,
\quad D''\ne0,\quad D'''\ne0,\\
b=(g,hy,y)^t\in S^3,\qquad
g=-\frac{1+Dy^2}{2y},\qquad
\det[b,b_s,b_t]\ne0,\qquad
A_K=K[y_1,y_2]=K[v],\quad \deg_YF=3 .
\end{gathered}
\tag{1}
\]
Primes denote the extension delta of d/dh to L. The field L is
relatively algebraically closed in K. If y were algebraic over L,
it would belong to L, and all three entries of b would lie in L.
Then V(b)=0 would contradict the actual frame determinant. Thus y
is transcendental over L and K is finite separable over L(y).

Extend delta by fixing y and extend partial_y by killing L. Their
unique extensions to K commute, and the full partial_y kernel is L,
by the argument in [rational transfer120, Section3](cubic-general-ruled-exclusion-pass120.md).
These rational derivatives replace the original base derivatives by
an invertible matrix over K. The actual generic ring stays K[v,u]
and the original Jacobian changes only by a member of K*. No function
of v is inverted. In particular h and y are not being declared
polynomial coordinates of S. Write partial_y as a subscript y below.

## 2. The null connection is explicit

Put f=D''/2. Direct differentiation of the displayed b in (1), followed
by expansion in the actual frame (b,b_h,b_y), gives
\[
\begin{gathered}
\Omega_{h,y}=\det[b,b_h,b_y]=-1,\qquad
G=\begin{pmatrix}fy^2&0\\0&y^{-2}\end{pmatrix},\\
C^1_{11}=C^2_{12}=C^1_{22}=0,\quad
C^1_{12}=1/y,\quad C^2_{11}=-fy^3,\quad C^2_{22}=-1/y,\\
T_{111}=\tau=-f'y^2\ne0,\qquad
T_{112}=T_{122}=T_{222}=0 .
\end{gathered}
\tag{2}
\]
For example, b_hh=(-D''y/2,0,0) transposed, b_hy=b_h/y,
and b_yy=b/y squared-b_y/y. These three identities give every
connection entry in (2). The tensor follows either from its exact
definition90 or from -b_j transposed Q_i b_k in120. Thus these are
the actual connection and tensor, not independent proposed arrays.

The only cubic monomial in the potential is q0 tau Y1 cubed/6.
The generating-curve argument90 forces y1 to have generic degree one,
as in120. Put v=y1 and y2=R with generic degree three. The sixth and
fourth powers of v in the potential give B22=B12=0. From (2), these
two equations read
\[
\begin{gathered}
\rho/y^2-\rho_{yy}-\rho_y/y=0,
\qquad -\rho_{hy}+\rho_h/y=0,\\
\rho=A y+B/y,\qquad A\in L,\quad B\in\mathbb C,\\
\mathsf B_{11}=(2Bf-A'')y,\qquad
L_i=D_i(\chi+q_0\rho^2/2),\qquad (L_1)_y=L_2',\\
R=\frac{\zeta-L_1v-(q_0/2)\mathsf B_{11}v^2
                         +(q_0/6)f'y^2v^3}{L_2},\quad L_2\ne0 .
\end{gathered}
\tag{3}
\]
There is no unproved integration in the expression for rho. The first
equation makes (rho+y rho_y)/(2y) and y(rho-y rho_y)/2 members of
ker partial_y=L. The second equation makes the derivative of the
latter member zero, so it is the complex constant B. Substitution
then gives B11. The base element zeta may lie anywhere in K at this
stage; it has not been assumed constant along y.

## 3. The highest coefficients and exactness determine the linear term

Write R=sum from i=0 to3 of r_i v to the power i. Its cubic coefficient
is nonzero. The actual three-by-three volume determinant90 reduces to
\[
\begin{gathered}
\mathcal V:=\frac{\mathcal J}{\Omega_{h,y}L_2}
=R_h+R_vR_y-fy^3v-\frac{2}{y}RR_v-\frac1y vR_v^2\ \in K^*,\\
(r_3)_y=5r_3/y,\qquad (r_2)_y=4r_2/y,\\
r_3=ky^5,\quad r_2=jy^4,\quad
L_2=ly^{-3},\qquad
k=\frac{q_0f'}{6l}\in L^*,\quad
j=\frac{q_0(A''-2Bf)}{2l}\in L,\quad l\in L^* .
\end{gathered}
\tag{4}
\]
The two differential equations are respectively the fifth and fourth
coefficients in v. For example partial_y(r3/y to the power5)=0
puts k in L. Formula (3) then gives L2 and j. All these statements
hold even when the r_i initially belong to the finite extension K.

Put Psi0=chi+q0 rho squared/2. Since (Psi0)_y=l/y cubed,
the element Psi0+l/(2y squared) belongs to L; call it C. Exactness
of the linear coefficient now gives
\[
\begin{gathered}
\Psi_0=-l/(2y^2)+C,\quad C\in L,\qquad
L_1=-l'/(2y^2)+C',\\
r_1=\alpha y+\beta y^3,\qquad
\alpha=\frac{l'}{2l},\quad \beta=-\frac{C'}l,\\
k'/k=6\alpha=3l'/l,\qquad
(f'/l^4)'=0,\qquad f'=c_*l^4,\quad c_*\in\mathbb C^* .
\end{gathered}
\tag{5}
\]
The third coefficient in v gives the equality for k. Its last two
reformulations use k=q0 f'/(6l) and L^delta=C. Neither the existence
of an arbitrary logarithmic primitive nor a choice of a fourth root
inside L is being presumed.

## 4. Two lower coefficients force the scalar classification

Before determining r0, the second coefficient in v is
(j'-4 alpha j)y to the power4 plus
3k y to the power5 times ((r0)_y-2r0/y). Hence it forces
r0=m y squared+n, where m belongs to L and
n=(j'-4 alpha j)/(6k). The first and constant coefficients then give
\[
\begin{gathered}
r_0=my^2+n,\quad m\in L,\quad
n=\frac{j'-4\alpha j}{6k},\\
[v]\mathcal V=(\alpha'-2\alpha^2)y
       +(\beta'-2\alpha\beta-4jn-f)y^3=0,\\
\alpha'=2\alpha^2,\qquad
\beta'=2\alpha\beta+4jn+f,\qquad (1/l)''=0,\\
\mathcal V=(m'-2\beta n)y^2+(n'-2\alpha n)\ne0 .
\end{gathered}
\tag{6}
\]
For the first assertion, subtract the specified n and differentiate
(r0-n)/y squared; its derivative vanishes, so its value m lies in L.
The two distinct powers of y in the next line are independent over L.
This is exactly where its transcendence, rather than just y nonzero,
is used. The final nonzero assertion retains the original volume
unit condition; it does not require that volume be a complex constant.

Since the constants of delta are C, the equation (1/l)''=0 says
1/l=lambda h+mu with complex lambda,mu not both zero. Combine this
with D'''=2c_*l to the power4 from (5). Integrating inside L now
has only complex constants and gives exactly the two possibilities
\[
\begin{array}{ll}
\lambda=0:&
D=a_3h^3+a_2h^2+a_1h+a_0,
\quad a_i\in\mathbb C,\quad a_3\ne0,\\[4pt]
\lambda\ne0:&
D=a_2h^2+a_1h+a_0+\displaystyle\frac{c}{\lambda h+\mu},
\quad a_i,c\in\mathbb C,\quad c\ne0 .
\end{array}
\tag{7}
\]
In the second case, c=-c_*/(3 lambda cubed). Subtracting this
explicit reciprocal function makes the third derivative zero;
successive subtraction of complex multiples of h squared, h and
one then accounts for every integration constant. Thus (7) proves
D belongs to C(h) rather than assuming it. The retained condition
D'' nonzero is consistent with both cases, since D''' is nonzero.

## 5. A generic compatibility control, not an original global frame

The lower constraints are consistent. Over the rational field
K=C(h,y), set q0=1 and
\[
\begin{gathered}
D=h^3,\quad \rho=0,\quad
\chi=-\frac1{2y^2}-\frac{h^3}{2},\qquad
R=hy^2+\frac32h^2y^3v+\frac12y^5v^3,\\
L_1=-\frac32h^2,\quad L_2=y^{-3},\quad
\tau=-3y^2,\qquad
\Phi(v,R)=h/y,\quad \mathcal V=y^2,\quad
\mathcal J=-1/y\in K^* .
\end{gathered}
\tag{8}
\]
These are exact instances of (2)--(6), not merely solutions of the
last scalar ODE. In particular the relative generators v,R generate
K[v] and have exact plane relation of degree three. Define the four
rational expressions prescribed by the actual reconstruction90:
x_tr=b u+b_h v+b_y R and
z=chi+u squared/2-(3hy squared v squared+R squared/y squared)/2.
Their Jacobian in the order (u,h,y,v) is the displayed nonzero
base-valued scalar. This verifies generic compatibility of the
potential and volume conditions used here.

The first velocity entry is -(1+h cubed y squared)/(2y), which is
not a polynomial over C[h,y]. No global polynomial velocity or
four-variable original inverse is supplied. In particular the
control does not realize the full actual hypotheses (1) and is
not a counterexample to recognition or cancellation. The original
global polynomial data must still restrict the forms in (7).

## Verification scope

The classification (7) is a differential-field proof using the
actual potential and volume. It is not inferred from finite
choices of D or from a classification source.
[The one-method checker121](cubic_null_axis_checks_pass121.py)
independently derives the connection from b, checks every tensor
slot and the upper and lower volume coefficients, and checks the
particular rational model (8), including its four-expression
Jacobian. It cannot certify the actual framework, the full constant
field, the differential-field integrations, or a global inverse.
All files through120 are preserved.

The author ran that method once in execution `7b32ea`: it passed in
0.786 seconds of unittest time and 0.905025792 seconds of command
wall time, exit zero. The complete saved proof read was `7fb279`;
the complete code read and hash/AST/whitespace check were `0663f0`.
The earlier inline coefficient reconstruction `12af45` is not a
second test method or independent geometric certificate.
