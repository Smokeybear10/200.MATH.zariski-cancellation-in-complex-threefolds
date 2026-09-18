# The zero-M branch contradicts the actual conic Jacobian

Status: new restricted working exclusion. In the normalized actual mixed
conic, the coefficient M cannot vanish. The proof evaluates an existing
polynomial determinant identity over the exact coefficient field. It
does not replace an original coordinate by a field-dependent expression.
The nonzero-M conic and unrestricted cancellation are not solved here.

## 1. Retained actual chart and exact coefficients

Assume the supplied actual globally sliced exact1122 frame with entire
initial kernel (ZW-X^2Y^2), normalized as in
[quadratic reduction217](rank-two-mixed-ratio-quadratic-graph-reduction-pass217-working.md).
Use the exact radial field and conclusions of
[radial ratios218](mixed-conic-radial-constant-leading-ratios-pass218-working.md)
and [the next Jacobian coefficient218](mixed-conic-next-jacobian-constant-pass218-working.md).
In particular
\[
\begin{gathered}
L/\mathbb C(h,\rho)\text{ is finite},\qquad
\mathcal D h=0,\quad\mathcal D\rho=1,\qquad
L_0=\ker_L\mathcal D,\\
C\in\mathbb C^*,\quad F,G,\delta\in L_0,\qquad
k=C/\rho+F\rho+G,\\
\alpha=\rho/C,\qquad
b=(G_h\rho+2h\delta\rho^2)/C .
\end{gathered}
\tag{1}
\]
The subscripts h are exact coefficient derivatives. The nonzero
elements h and rho are independent transcendentals over the complex
numbers. Neither L nor L0 is assumed rational.

The affine line parameter xi and the intercepts have the form
\[
\begin{gathered}
\vartheta=\alpha\xi^2+b\xi+c,\qquad
y=h\vartheta+\xi,\qquad
w=\alpha\delta\xi^2+e\xi+f,\qquad
\epsilon=e-b\delta,\\
z=-h^2w+\xi^2/\rho+k_t\xi+(\mathcal Dk)\vartheta+n,\\
k_t=F_h+G_h/\rho,\qquad
\mathcal Dk=F-C/\rho^2,\qquad
\sigma=h^2\vartheta+2h\xi+k.
\end{gathered}
\tag{2}
\]
All undisplayed restrictions on c,e,f,n remain in force; none is
needed in this argument. The original polynomial coordinates are
\[
Y=y+h\rho X,\qquad
Z=z+\sigma X+h^2\rho X^2,\qquad
W=w+\vartheta X+\rho X^2 .
\tag{3}
\]
The original X is independent of L. Equations (2)--(3) are identities
in L[X,xi], not definitions of a new polynomial coordinate system.

Write Q=(Y,Z,W) as a column. The actual calibration is
\[
\det(Q_h,\mathcal DQ,Q_\xi)
 =j,\qquad j=-a^3\rho/\xi_v\in L^* .
\tag{4}
\]
Here the three derivatives hold the original X fixed and use
(h,rho,xi) as independent chart parameters. Since xi is affine in v,
the right side has no dependence on X or xi. This is the retained
actual determinant, not an assumed generic nonvanishing condition.

## 2. Exact linear and quadratic columns

Put
\[
\mathbf c=
\begin{pmatrix}
h\\F+h^2(X-\delta)\\X+\delta
\end{pmatrix},\qquad
\mathbf d=
\begin{pmatrix}0\\-h^2\\1\end{pmatrix},\qquad
M=hF_h-F-2h^2\delta\in L_0.
\tag{5}
\]
Directly expanding (2)--(3), or using the proved decomposition in
the preceding218 note with C_h=0, gives
\[
Q=A_2\xi^2+A_1\xi+A_0,\qquad
A_2=\alpha\mathbf c,\qquad
A_1=b\mathbf c+\mathbf c_h+(\epsilon-\delta_h)\mathbf d .
\tag{6}
\]
The unspecified A0 is in L[X]^3 and disappears on differentiating
with respect to xi. Equation (6) therefore yields
\[
Q_\xi=(2\alpha\xi+b)\mathbf c+
             \mathbf c_h+(\epsilon-\delta_h)\mathbf d .
\tag{7}
\]
All coefficient-field dependence is retained in these derivatives.

## 3. One legal evaluation of the polynomial determinant

Choose the following two elements of L:
\[
\xi_*=-\frac{C}{2h\rho}-\frac{b}{2\alpha}
      =-\frac{C}{2h\rho}-\frac{G_h}{2}-h\delta\rho,
\qquad
X_*=h\epsilon-\delta .
\tag{8}
\]
The denominators are legitimate nonzero elements of L. In particular
2 alpha xi_*+b=-1/h. Before making the X substitution, (7) becomes
\[
\left.Q_\xi\right|_{\xi=\xi_*}
=-\mathbf c/h+\mathbf c_h+(\epsilon-\delta_h)\mathbf d
=
\begin{pmatrix}
0\\
F_h-F/h+h(X-\delta)-h^2\epsilon\\
\epsilon-(X+\delta)/h
\end{pmatrix}.
\tag{9}
\]
Substitute X=X_* into (9). The result is exactly
\[
\boxed{\left.Q_\xi\right|_{X=X_*,\,\xi=\xi_*}
       =\begin{pmatrix}0\\M/h\\0\end{pmatrix}.}
\tag{10}
\]
For example the middle component becomes
F_h-F/h+h(h epsilon-2 delta)-h^2 epsilon=M/h.

If M=0, the evaluated third column of the determinant in (4) is
zero. Evaluation at (X_*,xi_*) is an L-algebra homomorphism
L[X,xi] to L, so it commutes with taking this already-computed
determinant. Its left side would vanish, while its right side
remains the nonzero element j. This contradiction proves
\[
\boxed{M\ne0.}
\tag{11}
\]

It is essential to differentiate first and then evaluate. Differentiating
the substituted coordinates would introduce derivatives of X_* and
xi_* and would not be the column identity used here. No such operation
occurs. The point is an algebraic evaluation over L, not an original
complex point or an authorized ambient coordinate change. Regularity
of the individual field coefficients in the original ring is unnecessary.

Equivalently, one can center only the chart parameter by
s=xi+b/(2 alpha). That parameter change has determinant one in
(h,rho,xi), and the point has s_*=-C/(2h rho). The unshifted proof
above avoids needing even that parameter change.

## 4. Scope and finite evidence

The three retained input notes were read before this proof. A fresh
inline symbolic computation af4f16 differentiated the raw coordinates
in (2)--(3), without importing the column decomposition, and obtained
(0,M/h,0) with all residuals zero. Two other AI reconstructions
checked the same unshifted substitution. These are algebra checks
and written reviews, not formal verification or human expert review.

No saved checker has yet executed this new result, and no217 or
earlier frozen record was changed. The result supplies permission
to divide by M only in subsequent arguments under these same actual
conic hypotheses. The previously retained radial equation becomes
\[
2\rho\,\mathcal D\epsilon-\epsilon+\delta_h=0.
\tag{12}
\]
It still permits an algebraic square-root term by itself. The lower
potentials must be used to exclude such a term. Even their resolution
would not automatically produce an original invariant coordinate,
establish arbitrary frame entry, or solve unrestricted cancellation.
