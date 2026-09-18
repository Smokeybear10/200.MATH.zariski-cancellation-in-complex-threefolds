# The constant determinant excludes the nongraph cusp quartic

**Status: working exclusion of one actual generic-chart branch.**

In the actual cusp chart159, the branch \(r=k_\rho\ne0\)
cannot have \(\deg_v y\ge2\). The preceding restriction160
reduces that putative branch to a nested quartic and a
reciprocal shifted fifth-power coefficient. The full constant
Jacobian then imposes an additional even-parity identity.
Its highest \(\rho\) coefficient contradicts the explicit
fifth-power functions, for every value of the remaining
complex constants.

This excludes only the indicated nongraph branch over the
generic field. It does not construct a polynomial invariant
correction, descend a generic parameter, recognize all cusp
frames, or settle arbitrary coordinate entry or cancellation.
No160 or earlier artifact is edited.

## 1. Actual inputs and the surviving quartic description

Retain all actual hypotheses of the cusp chart159, and suppose
for contradiction that \(r\ne0\) and \(\deg_v y\ge2\).
The exact-field restriction160, including its prior
selected-factor reduction, supplies
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,
\quad \ker\theta_0=(\mathsf X\mathsf Z-\mathsf Y^3),\\
N=[u^3]\partial_Z|_A,\quad
L=\operatorname{Frac}(\ker_A N),\quad A_L=L[v],\quad Nv=1,\\
L/\mathbb C(\tau,\rho)\text{ finite separable},\qquad
L[y,\vartheta]=L[v],\qquad
(\deg_v y,\deg_v\vartheta)=(2,4),\\
\Phi=\kappa\{V-Q(U)\}^2+\lambda U+\nu,
\quad \Phi(y,\vartheta)=m\in L,\quad
\kappa\lambda\ne0,\quad Q\in L[U],\quad\deg Q=2 .
\end{gathered}
\tag{1}
\]
Here \(U,V\) are independent formal variables, and the
whole polynomial \(\Phi-m\), not just one chosen factor,
generates the implicit kernel up to \(L^*\).[^1]
The description is in the fixed projected axes, derived
over \(L\) before the present argument.

Use \(k,n,\ell\in L\) and the exact potential from159:
\[
\begin{gathered}
r=k_\rho,\quad r_\rho=0,\quad r'\ne0,\quad
\Delta=r''/2-r'^2/r\ne0,\quad
\mathcal N=n_{\rho\rho}=2\kappa
 =-r\Delta^2/(2r')\ne0,\quad \mathcal N_\rho=0,\\
f=U^3+H_2(k;U,V)+H_1(n;U,V),\quad
A_1=f_V=r'U+n_\rho,\quad
B_1=f_U=3U^2+k''U+r'V+n_\tau,\\
\Phi=A_1(\ell-f)/r+H_3(k;U,V)+H_2(n;U,V)
 -\ell_\tau U-\ell_\rho V,\qquad
w=(\ell-f(y,\vartheta))/r.
\end{gathered}
\tag{2}
\]
A prime denotes the coefficient derivative \(\partial_\tau\).
Both coefficient partials commute and hold \(U,V\) fixed.
The notation \(H_j\) is the homogeneous directional Taylor
polynomial with the factorial convention of159/160.
All nonzero denominators in (2) were established in160,
not imposed as unexplained genericity assumptions.

For later substitution, put \(t=\tau-C_2\). The same theorem
gives constants and functions
\[
F=C_0+C_1t^5,\qquad
r=F^{-1},\qquad
\mathcal N=10C_1t^2/F^3,
\qquad C_0,C_2\in\mathbb C,\quad C_1\in\mathbb C^* .
\tag{3}
\]
In particular \(r,\mathcal N\in\mathbb C(\tau)\).
No claim that the remaining coefficients of \(L\) are
rational in \(\tau\) or \(\rho\) is made.

## 2. Changing only the generic parameter preserves a constant determinant

Set \(\zeta=\vartheta-Q(y)\).
The exact quadratic extraction in160 shows that \(\zeta\)
is an affine linear parameter in \(v\), with
\(\zeta_v\in L^*\). Equation (1) gives
\[
y=A_0\zeta^2+B_0,\qquad
\vartheta=Q(y)+\zeta,\qquad
A_0=-\kappa/\lambda\ne0,\qquad B_0=(m-\nu)/\lambda .
\tag{4}
\]
For this section extend the coefficient partials to fix
\(\zeta\), rather than \(v\). Their restrictions to \(L\)
are unchanged. This is a generic parameter description,
not an original-ring coordinate change.

The actual chart determinant at \(X=0\) was
\(\det\partial(y,z,w)/\partial(\tau,\rho,v)=-a^3\),
where \(a=EX\in L^*\). The chain rule therefore gives
\[
\mathcal J:=\det\frac{\partial(y,z,w)}{\partial(\tau,\rho,\zeta)}
 =-a^3/\zeta_v\in L^* .
\tag{5}
\]
It is essential that this is constant in the genuine line
parameter \(\zeta\). The value need not be a complex constant
or equal to the old normalized value.

The constant differential-wedge identity proved in159 is
unchanged by this parameter description. Taking its
\(d\tau\wedge d\rho\wedge d\zeta\) coefficient yields
\[
\begin{gathered}
\mathcal J=C_U\Phi_U(y,\vartheta)+C_V\Phi_V(y,\vartheta),\\
C_U=(\vartheta_\rho+A_1(y,\vartheta)/r)y_\zeta-y_\rho\vartheta_\zeta,
\qquad
C_V=y_\tau\vartheta_\zeta-(\vartheta_\tau+B_1(y,\vartheta)/r)y_\zeta .
\end{gathered}
\tag{6}
\]
Thus coefficient derivatives of the moving parametrization
are retained. No coefficient-dependent substitution has
silently been treated as constant.

## 3. The even part forces one more polynomial identity

Define the following polynomial over \(L\), with derivatives
of \(Q\) holding its formal variable fixed:
\[
\mathcal S(U)=Q_\tau+Q_U Q_\rho
 +Q_U(r'U+n_\rho)/r
 +(3U^2+k''U+r'Q+n_\tau)/r .
\tag{7}
\]
Substitute (4) in (6). One has
\(\Phi_U=\lambda-2\kappa\zeta Q_U(y)\),
\(\Phi_V=2\kappa\zeta\), \(y_\zeta=2A_0\zeta\), and
\(\vartheta_\zeta=Q_U(y)y_\zeta+1\).
The remaining derivatives are
\(y_i=(A_0)_i\zeta^2+(B_0)_i\) and
\(\vartheta_i=Q_i(y)+Q_U(y)y_i\), for \(i=\tau,\rho\).
With \(\kappa=-\lambda A_0\), expansion gives
\[
\begin{aligned}
\mathcal J={}&-\lambda(B_0)_\rho
 +\lambda\zeta^2\{- (A_0)_\rho+4A_0^2\mathcal S(y)\}\\
&+2\lambda A_0\zeta\bigl[
 Q_\rho(y)+(r'y+n_\rho)/r
 -Q_U(y)\{(A_0)_\rho\zeta^2+(B_0)_\rho\}\\
&\hspace{41mm}-(A_0)_\tau\zeta^2-(B_0)_\tau
 +2A_0(r'/r)\zeta^2\bigr].
\end{aligned}
\tag{8}
\]
Every term in square brackets is a polynomial in \(\zeta^2\),
since \(y=A_0\zeta^2+B_0\). Thus the last two displayed
lines form an odd polynomial in \(\zeta\); the first line
is its even part.

Since \(\mathcal J\in L^*\), the nonconstant even part
vanishes. Substitution \(U\mapsto A_0\zeta^2+B_0\) is
injective on \(L[U]\). Hence
\[
\mathcal S(U)=\frac{(A_0)_\rho}{4A_0^2}
 =\frac{\lambda_\rho}{4\kappa}
 =\frac{\lambda_\rho}{2\mathcal N}
 \quad\text{in }L[U].
\tag{9}
\]
The middle equality uses \(\kappa_\rho=\mathcal N_\rho/2=0\).
Only this necessary even identity will be used below.
The odd identity and the value
\(\mathcal J=-\lambda(B_0)_\rho\) impose additional
conditions, but are not needed for the contradiction.

## 4. Coefficients are polynomial in rho over its exact constant field

Let \(K_0=\ker_L\partial_\rho\).
Then \(\rho\) is transcendental over \(K_0\):
differentiating a monic algebraic relation of least positive
degree, using \(\partial_\rho\rho=1\), would give a
nonzero relation of smaller degree in characteristic zero.
Also \(\partial_\tau\) preserves \(K_0\), by commutation.
Elements of \(K_0\) need not be rational functions of \(\tau\).

As \(r,\mathcal N\in K_0\), their defining derivative
equations integrate without any antiderivative in an
algebraic coefficient field:
\[
k=r\rho+k_0,\qquad
n=\tfrac12\mathcal N\rho^2+n_1\rho+n_0,
\qquad k_0,n_1,n_0\in K_0.
\tag{10}
\]
For example, take \(k_0=k-r\rho\),
\(n_1=n_\rho-\mathcal N\rho\), and then the corresponding
\(n_0\); each has zero \(\rho\) derivative.
Thus coefficient extraction in the polynomial variable
\(\rho\) over \(K_0\) is legitimate.

Write the fixed-axis potential as
\[
\begin{gathered}
\Phi=\tfrac12\mathcal N V^2+b(U)V+c(U),\\
b(U)=\Delta U^2+b_1U+b_0,\qquad
b_1=n_{\tau\rho}-2r'n_\rho/r,\quad b_0=-n_\rho^2/r-\ell_\rho,\\
c_2=[U^2]c=\tfrac12 n_{\tau\tau}
 -(r'n_\tau+n_\rho k''/2)/r,\qquad
c_1=[U]c=(r'\ell-n_\rho n_\tau)/r-\ell_\tau,\\
Q(U)=-b(U)/\mathcal N,\qquad
\lambda=c_1-b_1b_0/\mathcal N .
\end{gathered}
\tag{11}
\]
All formulas come by expanding (2) and completing the square
in \(V\). The remaining vanishing coefficient of \(U^2\)
in that square completion gives
\(b_0=(2\mathcal N c_2-b_1^2)/(2\Delta)\).
By (10), \(b_1\) has \(\rho\)-degree at most one and
\(c_2\) degree at most two. Thus \(b_0\) has degree at
most two, and \(\ell_\rho=-b_0-n_\rho^2/r\) has degree
at most two.
Termwise integration in the polynomial variable \(\rho\),
whose coefficients lie in \(K_0\), proves
\(\ell\in K_0[\rho]\) with degree at most three.
The remaining difference is in \(K_0\) by its zero derivative.
There is no assumption that its \(\tau\) antiderivative is
algebraic or rational.

## 5. The highest rho coefficients are independent of the integration constants

The following expressions depend only on \(r\) and \(\mathcal N\):
\[
\begin{gathered}
\mathsf B=\mathcal N'-2r'\mathcal N/r,\qquad
\mathsf C=\mathcal N''/4-(r'\mathcal N'+\mathcal N r'')/(2r),\\
\mathsf H=(2\mathcal N\mathsf C-\mathsf B^2)/(2\Delta),\qquad
\mathsf E=-(\mathsf H+\mathcal N^2/r)/3,\\
[\rho]b_1=\mathsf B,\quad [\rho^2]c_2=\mathsf C,\quad
[\rho^2]b_0=\mathsf H,\quad [\rho^3]\ell=\mathsf E .
\end{gathered}
\tag{12}
\]
These are ordinary polynomial coefficients, with the factor
three in the last integration explicitly included.
They are unaffected by \(k_0,n_1,n_0\) or the other integration
constants in \(K_0\).

Write \(Q=q_2U^2+q_1U+q_0\), and put
\(P=[\rho]q_1\), \(R=[\rho^2]q_0\).
Equation (11) gives \(q_2=-\Delta/\mathcal N\),
\(P=-\mathsf B/\mathcal N\), \(R=-\mathsf H/\mathcal N\).
Their degree bounds are \(\deg_\rho q_1\le1\),
\(\deg_\rho q_0\le2\); similarly \(\deg_\rho\lambda\le3\).
The coefficients needed in (9) are exactly
\[
\begin{gathered}
L_3:=[\rho^3]\lambda
 =r'\mathsf E/r-\mathcal N\mathcal N'/(2r)
   -\mathsf E'-\mathsf B\mathsf H/\mathcal N,\\
S_2:=[\rho^2][U^0]\mathcal S
 =R'+2PR+P\mathcal N/r+r'R/r+\mathcal N'/(2r),\\
S_2=\frac{3L_3}{2\mathcal N} .
\end{gathered}
\tag{13}
\]
For the first formula use the expression for \(c_1\) in
(11) and the leading \(\rho\) terms in (10), (12).
For the second take the constant term in \(U\) in (7):
it is \(q_0'+q_1(q_0)_\rho+q_1n_\rho/r
+r'q_0/r+n_\tau/r\).
Its \(\rho^2\) coefficient is the displayed expression.
The last equality is the necessary identity (9).
Lower \(\rho\) coefficients, however complicated in \(K_0\),
cannot modify it.

## 6. The exact fifth-power substitution contradicts even parity

Use (3), put \(c=C_1\ne0\), \(d=C_0\), and write
\(z_5=ct^5\), so \(F=d+z_5\).
Differentiation is in \(t\), since \(t=\tau-C_2\).
The expressions in (12) give
\[
\begin{gathered}
\Delta=-10ct^3/F^2,\qquad \mathcal N=10ct^2/F^3,\qquad
\mathsf B=10ct(2d-3z_5)/F^4,\\
\mathsf C=5c(d^2-28dz_5-4z_5^2)/F^5,\\
\mathsf H=\frac{5c(3d+13z_5)}{tF^5},\qquad
\mathsf E=-\frac{5c(d+11z_5)}{tF^5},\\
q_2=tF,\qquad
P=\frac{-2d+3z_5}{tF},\qquad
R=-\frac{3d+13z_5}{2t^3F^2} .
\end{gathered}
\tag{14}
\]
For an explicit intermediate check,
\(\mathcal N'=20ct/F^3-150c^2t^6/F^4\) and
\(\mathcal N''=20c/F^3-1200c^2t^5/F^4+3000c^3t^{10}/F^5\).
They give \(\mathsf C\) as displayed.
Also
\(2\mathcal N\mathsf C-\mathsf B^2
=-100c^2t^2(3d+13z_5)/F^7\), which verifies
\(\mathsf H\) after division by \(2\Delta\).
The formula for \(\mathsf E\) follows since
\(\mathcal N^2/r=100c^2t^4/F^5\).

Substitute (14) into the two expressions in (13).
They simplify to
\[
L_3=-\frac{35c}{t^2F^4},\qquad
S_2=\frac{21}{2t^4F},\qquad
S_2-\frac{3L_3}{2\mathcal N}
 =\frac{63}{4t^4F}\ne0 .
\tag{15}
\]
These are rational identities, not asymptotic estimates.
For a direct numerator verification of the first one,
factor \(5c/(t^2F^6)\) out of its defining expression.
The remaining numerator is
\[
5z_5(3d-7z_5)-(d+11z_5)F-(2d-3z_5)(3d+13z_5)
=-7F^2.
\]
For the second, put its terms over \(2t^4F^3\).
The numerator is
\[
(3d+13z_5)(7d+12z_5)-85dz_5-135z_5^2=21F^2.
\]
Finally \(3L_3/(2\mathcal N)=-21/(4t^4F)\),
giving the last formula in (15).

The rational function in (15) is nonzero because
\(\tau\) is transcendental, \(c\ne0\), and
\(F=d+ct^5\ne0\). The value \(d=0\) is included.
This is an identity in the coefficient field, not evaluation
at a pole or removal of any actual divisor.
It contradicts the necessary last equality of (13).

## 7. Exact conclusion and remaining scope

The assumed \(r\ne0\), \(\deg_v y\ge2\) branch of the
actual cusp chart cannot occur. Thus in the nonzero-\(r\)
branch \(y\) is either constant in \(L\) or an affine
linear parameter for \(L[v]\).

Combining this conclusion with the separate zero-\(r\)
reduction160 gives, for every actual cusp chart159,
\[
y\in L\quad\text{or}\quad y=\alpha v+\beta
\ (\alpha\in L^*,\ \beta\in L),\qquad N^2y=0
\quad\text{in }A_L=L[v].
\tag{16}
\]
In the zero-\(r\) branch, that source makes \(y\) affine
when \(n_\rho\ne0\), and constant otherwise.
If \(r\ne0\) and \(y\in L\), the whole-line equality
\(L[y,\vartheta]=L[v]\) also makes \(\vartheta\) an affine
parameter. Equation (16) concerns the projected coordinate
\(y\in A_a\); it does not remove its denominator or assert
the corresponding statement for an original ambient coordinate.

The proof uses the whole quartic conclusion160, the full
actual constant determinant159, and coefficient polynomiality
over \(\ker_L\partial_\rho\). It allows arbitrary finite
algebraic coefficient extensions throughout; no unproved
coefficient fixing or antiderivative assertion replaces them.
Only an auxiliary generic parameter description is used.

The remaining graph or constant-coordinate cases still
require an actual integral argument. The zero-\(r\) result
is used only in the corollary (16), not in the exclusion proof.
No automatic low-weight invariant lift, polynomial primitive
slice, global recognition, arbitrary-entry theorem or full
cancellation conclusion is asserted.

## Sources and verification scope

1. [Nongraph quartic restriction160](cusp-nongraph-quartic-restriction-pass160-working.md),
   including its exact-field AMS degree step, selected-factor
   prerequisite, fixed-axis extraction and fifth-power ODE.
   These inputs are retained as working proofs, not recursively
   re-audited primary classifications here.
2. [Actual cusp chart159](cusp-generic-chart-first-reductions-pass159-working.md),
   Sections 2--5, supplies the actual determinant and its
   tensorial constant-wedge identity used in (5)--(6).
3. [Zero-r generic reduction160](cusp-zero-r-generic-graph-pass160-working.md),
   a separate result, not an input to the contradiction.

The even-parity calculation, polynomial coefficient extraction
and nonzero rational discrepancy are proved explicitly above.
Finite symbolic controls cannot replace these universal steps.
No historical novelty clearance, human expert review or
proof-assistant certification is claimed.

[^1]: Sources 1--2 with all their actual-frame and generic-field hypotheses.
