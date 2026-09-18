# The next mixed-conic Jacobian coefficient makes C complex

Status: bounded working necessary condition for the normalized actual
mixed conic. The coefficient of \(X\xi^4\) in the full calibrated
Jacobian forces the radial constant \(C\) of the preceding218 note
to be a nonzero complex constant. The remaining fourth-degree equation
is retained, including its possible algebraic square-root mode.
No original invariant coordinate is produced here.

## 1. Exact retained hypotheses

Assume the normalized actual case-II conic of
[quadratic reduction217](rank-two-mixed-ratio-quadratic-graph-reduction-pass217-working.md)
and the fully read
[radial-constant note218](mixed-conic-radial-constant-leading-ratios-pass218-working.md).
In particular the original polynomial ring has a global slice and the
supplied exact time profile and full initial kernel
\[
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad
\deg_E(X,Y,Z,W)=(1,1,2,2),\qquad
\ker\theta_0=(ZW-X^2Y^2).
\tag{1}
\]
All four displayed generators are actual polynomial coordinates.
The selected field \(L\) is finite over
\(\mathbb C(t,\rho)=\mathbb C(h,\rho)\), where \(h=t/\rho\).
Use the commuting exact coefficient derivatives
\(\mathcal D=h\partial_t+\partial_\rho\) and
\(\partial_h=\rho\partial_t\), and put \(L_0=\ker_L\mathcal D\).
Thus \(\mathcal D\) is differentiation in \(\rho\) at fixed \(h\).
Joint constants are \(\mathbb C\); neither \(L_0=\mathbb C(h)\)
nor rationality of \(L\) is assumed.

The affine line parameter \(\xi\), quadratic second projection, and
intercepts are
\[
\begin{gathered}
\deg_v\xi=1,\qquad
\vartheta=\alpha\xi^2+b\xi+c,\qquad y=h\vartheta+\xi,\\
w=d\xi^2+e\xi+f,\qquad \deg_v z\le2,\qquad
L[y,z,w]=L[v],\\
k=C/\rho+F\rho+G,\qquad
C\in L_0^*,\quad F,G,\delta\in L_0,\qquad
\alpha=\rho/C,\quad d=\alpha\delta,\\
b=\frac{2C_h+G_h\rho+2h\delta\rho^2}{C}.
\end{gathered}
\tag{2}
\]
All other coefficients lie in the exact \(L\).
Subscripts \(h\) denote \(\partial_h\). The factor \(\rho^2\)
in the final summand of \(b\) is retained.
These are proved conditions of the preceding note, not a rational
ansatz or permission to use field-dependent ambient shears.

The actual original coordinates are
\[
\begin{gathered}
Y=y+tX,\qquad W=w+\vartheta X+\rho X^2,\\
Z=z+\sigma X+(t^2/\rho)X^2,\qquad
\sigma=h^2\vartheta+2h\xi+k,\\
z=-h^2w+\xi^2/\rho+k_t\xi+(\mathcal Dk)\vartheta+n.
\end{gathered}
\tag{3}
\]
The scalar \(n\in L\) affects the constant column but not the
quadratic or linear columns used below.

## 2. The full quadratic and linear columns

View the column \((Y,Z,W)^{\mathsf T}\) as
\(A_2(X)\xi^2+A_1(X)\xi+A_0(X)\), with entries in \(L[X]\).
Let
\[
\mathbf c=
\begin{pmatrix}
h\\ F+h^2(X-\delta)\\ X+\delta
\end{pmatrix},
\qquad
\epsilon=e-b\delta,\qquad
\mathbf d=
\begin{pmatrix}0\\-h^2\\1\end{pmatrix},
\qquad
\mathbf e_Z=
\begin{pmatrix}0\\1\\0\end{pmatrix}.
\tag{4}
\]
The earlier218 calculation gives \(A_2=\alpha\mathbf c\).
The complete linear column, directly from (3), is
\[
A_1=
\begin{pmatrix}
1+hb\\
k_t+(\mathcal Dk)b-h^2e+(h^2b+2h)X\\
e+bX
\end{pmatrix}.
\tag{5}
\]
In particular the terms \(2hX\), \(k_t\), and the full \(b\)
cannot be omitted.

The exact derivative identities of the preceding note are
\[
\mathcal Dk=-C/\rho^2+F,\qquad
k_t=C_h/\rho^2+F_h+G_h/\rho,\qquad
k_t-Cb/\rho^2=F_h-C_h/\rho^2-2h\delta.
\tag{6}
\]
Using \(e=b\delta+\epsilon\), equations (5)--(6) give the useful
decomposition
\[
\boxed{
A_1=b\mathbf c+\mathbf c_h
       +(\epsilon-\delta_h)\mathbf d
       -\frac{C_h}{\rho^2}\mathbf e_Z .}
\tag{7}
\]
For example its middle component is
\(b\{F+h^2(X-\delta)\}
+F_h+2h(X-\delta)-h^2\epsilon-C_h/\rho^2\),
which is exactly the middle entry in (5).
The \(G_h\) terms have canceled in this decomposition only through
the proved formula for \(b\); \(G\) has not been normalized away.

## 3. The complete fourth-degree determinant coefficient

The actual calibration, after the parameter change to
\((h,\rho,\xi)\), is
\[
\det\frac{\partial(Y,Z,W)}{\partial(h,\rho,\xi)}
 =-a^3\,\frac{\rho}{\xi_v}\in L^*.
\tag{8}
\]
The dependence of \(\xi\)'s affine coefficients on \(h,\rho\)
does not change this scalar conclusion, as proved in the preceding
note by the chain rule. Derivatives of the coefficient columns
below hold the parameter \(\xi\) and the original \(X\) fixed.

Write \(J_4=[\xi^4]\) of the determinant on the left of (8).
There are exactly three contributions:
\[
\begin{aligned}
J_4={}&\det((A_2)_h,\mathcal D A_2,A_1)\\
 &+2\det((A_2)_h,\mathcal D A_1,A_2)
 +2\det((A_1)_h,\mathcal D A_2,A_2).
\end{aligned}
\tag{9}
\]
Terms containing \(A_0\) or one of its derivatives have degree at
most three in \(\xi\), so (9) is the full coefficient, not a
selected leading contribution.

Because \(\mathcal D\mathbf c=0\),
\(\mathcal D A_2=A_2/\rho\). The last determinant in (9) vanishes.
Terms involving \(\alpha_h\) in the other two determinants also
have proportional columns. Keeping the signs gives
\[
J_4=\alpha^2
\left\{2\det(\mathbf c_h,\mathcal D A_1,\mathbf c)
             -\rho^{-1}\det(\mathbf c_h,A_1,\mathbf c)\right\}.
\tag{10}
\]
Define the exact expressions
\[
M=hF_h-F-2h^2\delta\in L_0,\qquad
T=X+\delta-h\delta_h\in L_0[X].
\tag{11}
\]
Direct expansion yields
\(\det(\mathbf c_h,\mathbf d,\mathbf c)=M\) and
\(\det(\mathbf c_h,\mathbf e_Z,\mathbf c)=T\).
Equation (7), commutation of the two coefficient partials, and
\(\mathcal D C_h=\mathcal D\delta_h=0\) therefore give
\[
\begin{aligned}
\det(\mathbf c_h,A_1,\mathbf c)
   &=M(\epsilon-\delta_h)-C_hT/\rho^2,\\
\det(\mathbf c_h,\mathcal D A_1,\mathbf c)
   &=M\mathcal D\epsilon+2C_hT/\rho^3,\\
\boxed{J_4}
   &=\boxed{\left(\frac{\rho}{C}\right)^2
       \left\{M\left(2\mathcal D\epsilon-\frac{\epsilon}{\rho}
                         +\frac{\delta_h}{\rho}\right)
                       +\frac{5C_hT}{\rho^3}\right\}.}
\end{aligned}
\tag{12}
\]
The radial derivative of the \(b\mathbf c\) term in (7) is a
multiple of \(\mathbf c\) and drops out of both determinants.
Thus all of its lower-field data have been accounted for.

## 4. The complex constant and the retained residual equation

Equation (8) makes \(J_4=0\) as a polynomial in the independent
original \(X\) over \(L\). Since \(M,\epsilon,\delta_h\) do not
depend on \(X\) and \([X]T=1\), (12) implies
\[
[X]J_4=\frac{5C_h}{\rho C^2}=0.
\tag{13}
\]
Consequently \(C_h=0\). Combined with \(\mathcal DC=0\), this
makes \(C\) a joint constant of the original coefficient field.
It remains nonzero by (2). Removing the now-vanishing final term
of (12) gives the complete conclusion at this degree:
\[
\boxed{C\in\mathbb C^*,\qquad
M\bigl(2\rho\,\mathcal D\epsilon-\epsilon+\delta_h\bigr)=0.}
\tag{14}
\]
No division by \(M\) has been made.

If \(M=0\), this coefficient places no further restriction on
\(\epsilon\). If \(M\ne0\), set \(\eta=\epsilon-\delta_h\).
Then \(2\rho\,\mathcal D\eta=\eta\), hence
\(\mathcal D(\eta^2/\rho)=0\).
This is compatible with a nonzero algebraic square-root mode over
a finite radial extension. It neither forces \(\eta=0\) nor
identifies that extension with a rational field. The remaining
lower potentials and determinant coefficients must decide whether
such a mode occurs in an actual frame.

## 5. Verification and scope

The preceding218 source and the complete217 conic source were read
through EOF before this argument. New independent inline calculations
reconstructed all three determinants in (9), confirmed (12), and
returned precisely the coefficient in (13). These check finite
identities; the actual calibration and exact-field hypotheses are
retained written inputs, not consequences of those calculations.

Only \(C\) has been proved complex here. The functions \(F,G,\delta\)
remain in \(L_0\), and the lower coefficients remain subject to the
unsolved equations. No arbitrary function of \(h\) has been removed
by an actual shear. This is a new separate218 necessary condition,
not an expansion of the217 conclusions or a coordinate-recognition
theorem. No saved checker was executed, imported or compiled, and
no earlier proof, verification packet or index was changed.
