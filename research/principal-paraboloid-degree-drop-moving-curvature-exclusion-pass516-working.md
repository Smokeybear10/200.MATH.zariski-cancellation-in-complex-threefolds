# Curvature vanishes in the quadratic-row degree-drop subcase

Working result: retain the FULL actual degree-drop entry of514,
including its original scalar, both returns, the genuine potentials
and unit tangent multiplier. Then
\[
\boxed{h''=0,\qquad f''''=0.}
\]
Both zero and nonzero transverse derivatives of the moving linear
slope are treated. The proof uses the literal degree-drop moving
rows. It does not apply a nonzero-delta theorem with its hypothesis
removed.

This is a necessary coefficient reduction. The remaining lower
scalar is not solved in this note, and no entire conic exclusion,
ambient recognition or unrestricted cancellation is claimed.

## 1. Exact retained entry and the two slope alternatives

Retain all actual assumptions of
[514](principal-paraboloid-degree-drop-quadratic-row-moving-frame-pass514-working.md),
which were derived directly from
[512](principal-paraboloid-degree-drop-univariate-coupling-reduction-pass512-working.md)
in its zero-cubic-fourth-row subcase. In particular the actual
normalization has already given
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u_{\rm glob}],\quad
X=a_0u_{\rm glob}+x_0,\quad a_0\ne0,\quad E=\partial_{u_{\rm glob}},\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\quad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the ENTIRE initial kernel},\\
0\ne N=[u_{\rm glob}^4]\partial_Z|_A,\quad
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,\\
Na_0=Nt=Ns=0,\quad P=\sigma,\quad NP=\rho\in L^*,\quad
O=L[P],\quad L[X,Y,Z,W]=L[X,P],\\
\operatorname{Frac}A=L(P)=\mathbb C(y,z_0,w_{\rm int}),\quad
L[y,z_0,w_{\rm int}]=O,\\
m=t,\quad k=ts+f,\quad a=-1/t,\quad A_1=a'=1/t^2\ne0,\\
\theta=aP^2+bP+c,\quad y=-\theta/2+\lambda P+r,\quad
J_{t,s,P}=-a_0^4/\rho\in L^*.
\end{gathered}
\tag{1}
\]
Both returns, the original slice and selected literal partial remain
required. Let \(F_0=\ker_L\partial_s\). It is finite over C(t);
its exact t derivative has constants C. No rationality of F_0 or L
is assumed. Primes below mean this exact derivative on F_0.

The complete coefficient integrations of514 are
\[
\begin{aligned}
n&=s^2/4+(f'/2-h)s+n_0,\\
H_c&=(h-th')/2,\qquad B_c=-f''/4+tf'''/12,\\
\lambda&=-H_c/t+B_c,\\
r&=H_cb+(H_c/(2t)+B_c/2+h'/2)s+r_0,\qquad
f''''=-6h''/t,
\end{aligned}
\tag{2}
\]
with \(f,h,n_0,r_0,H_c,\lambda\in F_0\) and arbitrary remaining
b,c,ell in L. The letters H_c and h are coefficient functions,
not the genuine cubic potential H or its moving level.

The literal moving rows of514 are
\[
\begin{gathered}
U=Z,\quad V=-2Y+U/t,\quad
T=W+2(X+h')Y+f'''U/6,\\
U=P^2+uP+U_0,\quad V=vP+V_0,\quad T=wP+T_0,\\
u=s+f'+2t(X+\lambda),\quad
v=b+(s+f')/t,\quad
w\in F_0[X],\quad [X^2]w=2.
\end{gathered}
\tag{3}
\]
Their exact inverse and all lower coefficients are retained from514.
Only U is asserted to be an actual complex coordinate here.
The moving connection is essential:
\[
J=\frac12\det\bigl(dU,\ dV+A_1U\,dt,\ dT+h''V\,dt\bigr)
  =-a_0^4/\rho.
\tag{4}
\]
All differentials hold the actual X fixed.

The unit multiplier and the integrated cubic coefficient are
\[
\kappa=\frac1{2t}-v_s\in L^*,\qquad
T_0=\frac w2s+\frac{w_t}{A_1}v+\frac{h''}{2A_1}v^2+C_0,
\qquad C_0\in F_0[X].
\tag{5}
\]
Also \(v=\epsilon/t\ne0\) by512. Formula (5) does NOT make v_s
nonzero. The following two sections treat its two possibilities.

For either case one may center the intrinsic parameter by
\[
\xi=P+u/2,\quad U=\xi^2+\overline U,\quad
V=v\xi+\overline V,\quad T=w\xi+\overline T.
\tag{6}
\]
The centering uses coefficients in L[X], and is only a horizontal
polynomial change at fixed actual X. Its parameter Jacobian is one,
so (4) remains calibrated. It is not a claim that xi belongs to the
actual invariant ring or that the original extended N fixes X.

## 2. Zero transverse slope forces h''=0

Assume \(v_s=0\), so \(v\in F_0^*\). Put
\[
\alpha=\frac{h''}{2A_1},\qquad \beta=\frac{w_t}{A_1},\qquad
\Lambda=2\alpha v+\beta.
\]
Because \(u=s+u_F\) with \(u_F\in F_0[X]\), (5) gives
\[
\overline T=\alpha v^2+\beta v+C,\qquad C\in F_0[X].
\tag{7}
\]
In particular its s derivative is zero. Define
\[
K_c=\alpha'v^2+\beta'v+C'+2A_1\alpha\overline V.
\tag{8}
\]
The COMPLETE corrected matrix in (4), now in (t,s,xi), is
\[
\begin{pmatrix}
\overline U_t&\overline U_s&2\xi\\
A_1\xi^2+v_t\xi+\overline V_t+A_1\overline U
 &\overline V_s&v\\
A_1\Lambda\xi+\Lambda v_t+K_c&0&w
\end{pmatrix}.
\tag{9}
\]
Its xi^2 coefficient, before the factor 1/2 in (4), is exactly
\[
-A_1(w\overline U_s+2\Lambda\overline V_s)=0.
\tag{10}
\]
If \(\overline V_s=0\), then (10) and the nonzero polynomial w
give \(\overline U_s=0\). The entire middle column of (9) is zero,
contradicting the nonzero scalar. Thus \(\overline V_s\ne0\).

Work temporarily in the coefficient field L(X), where w is nonzero
and invertible. Substituting
\(\overline U_s=-2\Lambda\overline V_s/w\) from (10), the COMPLETE
xi coefficient of (9) is
\[
-2\overline V_s\left(K_c+\frac{A_1\Lambda^2v}{w}\right)=0.
\tag{11}
\]
The second term in parentheses is in F_0(X). Therefore K_c has
zero s derivative. But its definition gives
\[
(K_c)_s=2A_1\alpha\overline V_s.
\]
Since \(A_1\overline V_s\ne0\), alpha vanishes. This proves
\[
v_s=0\quad\Longrightarrow\quad h''=0,\quad f''''=0.
\tag{12}
\]
The argument did not divide by h'', v_t or a possibly zero lower
intercept. The division by w was only in F_0(X), not in the actual
coordinate ring. No finite root of w was deleted or specialized.

## 3. Nonzero transverse slope: complete literal centered support

Now suppose \(v_s\ne0\). Define
\[
z=b+s/t=v-f'/t,\qquad S=s(t,z),\qquad q_*=S-tz.
\tag{13}
\]
Thus \(z_s=v_s\ne0\), the coefficient basis (t,z) is exact,
\([L:\mathbb C(t,z)]<\infty\), and its transverse constants are
exactly F_0. The rebased and centered scalar is
\[
J_{t,z,\xi}=-\frac{a_0^4S_z}{\rho}\in L^*,\qquad
S_z=1/z_s\ne0.
\tag{14}
\]
The factor S_z is not removed or declared complex.

Assume for contradiction \(h''\ne0\), and put
\[
\alpha=t^2h''/2\ne0,\qquad A_1=1/t^2.
\]
Since \(H_c'=-th''/2=-\alpha/t\), H_c is a nonzero field
element. This licenses divisions by H_c below, without assuming
that it is a unit on an actual ambient variety.

For explicit literal support define the following F_0 coefficients:
\[
\begin{aligned}
u_1&=f-tf'-2t^2\lambda,\\
u_0&=2tr_0+n_0-(f'+2t\lambda)^2/4,\\
v_0&=f'/t,\qquad v_{10}=f/t-f',\\
\omega_1&=2(\lambda+h')+tf'''/3,\\
\omega_0&=2h'\lambda+f'''f'/6+tf'''\lambda/3
 -(2r_0+f'\lambda+n_0')/t,\\
t_2&=-f'-4t\lambda-t^2f'''/6,\\
t_{10}&=2r_0+f'''f/6-\omega_1f'/2-t\lambda\omega_1-t\omega_0,\\
L_0&=2\alpha v_0+t^2\omega_0'.
\end{aligned}
\tag{15}
\]
Here omega_1 and omega_0 are the X coefficients of the polynomial w:
\(w=2X^2+\omega_1X+\omega_0\).
The original h,H_c are unrelated to these names.

Using (2) in the full original rows, and then centering as in (6),
gives EXACTLY
\[
\begin{aligned}
v&=z+v_0,\\
\overline U&=u_1X-2H_cq_*+u_0,\\
\overline V&=-tX^2+(q_*+v_{10})X+R_*,\\
\overline T&=t_2X^2+(2H_cz+t_{10})X+\alpha z^2+L_0z+t_{00}.
\end{aligned}
\tag{16}
\]
Here R_* is the full constant-X term of overline V, initially an
arbitrary element of L. The coefficient t_00 belongs to F_0: it
is the constant-X coefficient of the existing integration (5)
after centering and removing the displayed z dependence. The
original c and ell remain in R_* and t_00 and in the relations
that define them. Neither has been set to zero.

For clarity, the literal derivative identities used in this support
calculation are
\[
H_c'=-\alpha/t,\qquad
u_1'=2H_c,\qquad
\omega_1'=2H_c/t^2,\qquad
t_2'=2\alpha/t,\qquad
\omega_0'=(L_0-2\alpha v_0)/t^2.
\tag{17}
\]
They follow directly from (2),(15), including
\(\lambda'=H_c/t^2-f'''/6\). In particular u_1'=2H_c
is unconditional. It is NOT obtained by dividing a scalar
coefficient by \((q_*)_z\).

Equations (15)--(17) are a direct specialization of literal
polynomial identities also recorded in
[508](principal-paraboloid-moving-conic-curvature-exclusion-pass508-working.md).
Their validity here was reconstructed from514's original rows.
The theorem statement of508, whose entry came from a different
sector, is not being invoked.

## 4. Two complete scalar coefficients make q_* rational

Put
\[
\Lambda_z=2\alpha z+L_0,\qquad
\Lambda=2H_cX+\Lambda_z,\qquad
M=\overline T_t-\Lambda v_0'+2A_1\alpha\overline V.
\tag{18}
\]
The full corrected determinant, before its factor 1/2, is
\[
\mathcal D=\det
\begin{pmatrix}
\overline U_t&\overline U_z&2\xi\\
A_1\xi^2+v_0'\xi+\overline V_t+A_1\overline U
 &\xi+\overline V_z&v\\
A_1\Lambda\xi+\Lambda v_0'+M&\Lambda&w
\end{pmatrix}.
\tag{19}
\]
Every derivative now fixes z or t as indicated by this exact basis.
In particular the xi term in the middle column of the second row
is present. Calibration (14) says that D is independent of X,xi.

Its complete xi^2 coefficient is
\[
[\xi^2]\mathcal D=-A_1w\overline U_z
                 -2A_1\Lambda\overline V_z-2M.
\tag{20}
\]
Define
\[
M_{10}=t_{10}'-2H_cv_0'+2\alpha v_{10}/t^2
\]
and the polynomials over F_0
\[
\begin{aligned}
R_2(z)&=-\alpha t z^2+t^2M_{10}z+\iota_1,\\
R_3(z)&=\frac{t^2\alpha'}3z^3
+\frac{t^2(L_0'-2\alpha v_0')}2z^2
+t^2(t_{00}'-L_0v_0')z+\iota_0,
\qquad \iota_0,\iota_1\in F_0.
\end{aligned}
\tag{21}
\]
The X^2 coefficient of (20) vanishes identically using (17).
The X and constant coefficients are, respectively, \(2A_1\) times
the z derivative of the left side minus the right side of each
equation below, before choosing iota_1 and iota_0. Their vanishing
integrates to
\[
\begin{aligned}
(H_c\omega_1-\Lambda_z)q_*-2H_cR_*&=R_2(z),\\
H_c\omega_0q_*-\Lambda_zR_*&=R_3(z).
\end{aligned}
\tag{22}
\]
The constants iota_0,iota_1 are the existing zero-derivative
differences in L. Because the transverse constants are F_0, no
primitive or rationality assumption was used in obtaining them.

Eliminate R_*:
\[
\begin{gathered}
\Delta(z)q_*=2H_cR_3(z)-\Lambda_zR_2(z),\\
\Delta(z)=\Lambda_z^2-H_c\omega_1\Lambda_z+2H_c^2\omega_0,
\qquad [z^2]\Delta=4\alpha^2\ne0.
\end{gathered}
\tag{23}
\]
The numerator has degree at most three and the denominator has
exact degree two. Consequently \(q_*\in F_0(z)\), and the first
line of (22) also puts \(R_*\in F_0(z)\). This is only a statement
about these two existing elements. It does not assert L=F_0(z),
let alone an ambient coordinate presentation.

## 5. The complete constant-xi coefficient and all pole boundaries

The full constant-xi coefficient of (19) is
\[
\begin{aligned}
\mathcal D_0={}&w\{\overline U_t\overline V_z
-\overline U_z(\overline V_t+A_1\overline U)\}\\
&+v\overline U_z(\overline T_t+2A_1\alpha\overline V)
-\Lambda v\overline U_t.
\end{aligned}
\tag{24}
\]
Define
\[
\mathcal G=4H_cu_1/t^2+4H_cv_{10}'+2u_0'\in F_0.
\]
Substitution of the COMPLETE support (16) and literal identities
(17) gives
\[
\boxed{
[X^3]\mathcal D_0=
\frac{4\alpha}{t}q_*(q_*)_z+4H_c(R_*)_z
+\mathcal G(q_*)_z=0.
}
\tag{25}
\]
There is no \((q_*)_t\) or \((R_*)_t\) term in this identity.
Their coefficients cancel before applying (22) or rationality.
This is an identity for D=2J in the rebased, centered parameters;
the factor 1/2 is not silently interchanged.

Work over an algebraic closure of F_0, only for the rational-function
pole test. If q_* had a finite pole of order n>0 in z, then
\(q_*(q_*)_z\) would have exact pole order 2n+1, with a nonzero
leading coefficient in characteristic zero. The first equation
of (22) makes R_* have pole order at most n. Hence the other terms
in (25) have pole orders at most n+1, strictly smaller. The
coefficient \(4\alpha/t\) is nonzero, giving a contradiction.

Thus q_* has no finite pole. Equation (23) now implies
\[
q_*=q_1z+q_0,\qquad q_0,q_1\in F_0,
\tag{26}
\]
allowing q_1=0, a zero polynomial q_*, and all cancellations in
(23). No root of Delta was deleted. Repeated roots are included
by their actual pole orders. Roots may move with t: (25) uses
only z derivatives, and the potentially competing t-derivative
terms were already proved absent.

The first line of (22) makes R_* a polynomial of degree at most two.
Writing its z^2 coefficient as r_2, that identity gives
\[
r_2=\frac{\alpha(t-2q_1)}{2H_c}.
\tag{27}
\]
The z coefficient of (25) is therefore
\[
\frac{4\alpha}{t}q_1^2+8H_cr_2
=\frac{4\alpha}{t}(q_1-t)^2=0.
\tag{28}
\]
It follows that q_1=t. The constant and zero q_* cases were not
discarded; they simply cannot satisfy (28) since t and alpha
are nonzero.

From S=q_*+tz, we now obtain \(S_z=2t\). Since z_s=v_s,
the exact inverse Jacobian gives
\[
v_s=z_s=1/(2t),\qquad \kappa=1/(2t)-v_s=0.
\]
This contradicts the genuine unit multiplier. Hence the assumption
h'' nonzero was impossible also in the nonzero-slope branch.
Together with (12) and (2), this proves
\[
\boxed{\text{Under full514, }\quad h''=0,\qquad f''''=0.}
\tag{29}
\]

## 6. Verification and retained boundary

The complete514 input, including its actual normalization and all
moving coefficients, was read. The full508 source was read only
to locate the literal support and pole calculation; the specialized
identities (15)--(28) were rebuilt under a=-1/t and delta zero.
Fresh f5ba06 checks the full xi^2 polynomial against both derivative
identities in (22), its X^2 cancellation, the entire X^3 coefficient
(25), both missing t-derivative coefficients, and the terminal
square (28), with every residual zero.

Independent root f01873 and31bf42 reconstruct the entire zero-slope
centered matrix, both complete coefficients and K_c's s derivative,
including the zero-middle-column boundary. Independent peer
ae6c08 and522293 reconstruct the full nonzero-slope original rows,
connection, integrations, pole support and terminal square.
These checks do not replace the exact-field and zero-safe arguments
given above.

The conclusion is only the stated necessary curvature vanishing.
The lower coefficients and remaining full scalar must still be
examined after any further ACTUAL normalization. No entire
degree-drop exclusion, nonlinear-curve recognition, ambient chart
entry or unrestricted cancellation is claimed here. No earlier
source or canonical file was edited. All saved checkers remained
frozen and were not executed, imported, compiled or rerun.
