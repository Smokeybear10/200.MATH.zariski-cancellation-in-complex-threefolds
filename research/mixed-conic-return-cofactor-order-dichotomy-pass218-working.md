# The radial determinant factor determines the return-cofactor order

Status: bounded working necessary condition for the normalized actual
mixed conic. The scalar \(M\) from the next Jacobian coefficient
distinguishes exactly the simple and double evaluated cofactors:
\(M\ne0\) gives a scalar multiple of \(R\), while \(M=0\) gives
a scalar multiple of \(R^2\). The scalars are units of the exact
coefficient field, not asserted to be units of the original ring.
Neither branch is recognized or excluded here.

## 1. Supplied actual setup and normalized coefficients

Retain the actual case-II conic of
[quadratic reduction217](rank-two-mixed-ratio-quadratic-graph-reduction-pass217-working.md)
and the complete hypotheses of
[radial constants218](mixed-conic-radial-constant-leading-ratios-pass218-working.md)
and [the next Jacobian coefficient218](mixed-conic-next-jacobian-constant-pass218-working.md).
In particular
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\\
\deg_E(X,Y,Z,W)=(1,1,2,2),\qquad
\ker\theta_0=(\mathsf Z\mathsf W-\mathsf X^2\mathsf Y^2),\\
0\ne N=[u^3](\partial_Z|_A),\quad
L=\operatorname{Frac}\ker_A N,\quad A_L=L[v],\quad Nv=1,\\
t=b_0/a,\quad \rho=h_0/a^2,\quad h=t/\rho,\quad
[L:\mathbb C(h,\rho)]<\infty,\qquad a=EX\ne0,\\
\xi=y-h\vartheta,\quad \deg_v\xi=1,\quad
\vartheta=P(\xi),\quad P(T)=\frac{\rho}{C}T^2+bT+c,\quad
y=\xi+hP(\xi).
\end{gathered}
\tag{1}
\]
Here \(b_0=EY\) and \(h_0=E^2W/2\); the symbol \(b\) is instead
the linear coefficient of \(P\). The initial ideal in (1) is the
full weighted evaluation kernel. The selected pivot is the literal
original \(\partial_Z\), and \(t,\rho\) are algebraically independent.
In particular \(h,\rho\ne0\).

The commuting exact coefficient derivatives are
\(\mathcal D=h\partial_t+\partial_\rho\) and
\(\partial_h=\rho\partial_t\). Put \(L_0=\ker_L\mathcal D\).
The retained218 results give
\[
\begin{gathered}
C\in\mathbb C^*,\qquad F,G,\delta\in L_0,\qquad
k=C/\rho+F\rho+G,\\
b=\frac{G_h\rho+2h\delta\rho^2}{C},\qquad
M=hF_h-F-2h^2\delta\in L_0,\\
R=-\frac{2h}{\rho}\xi+k_\rho\in L[\xi],\qquad
\deg_\xi R=1.
\end{gathered}
\tag{2}
\]
Subscripts \(h\) refer to \(\partial_h\), whereas \(k_\rho\)
in the return polynomial is the original partial at fixed \(t\).
No equality \(L_0=\mathbb C(h)\) or rationality of \(L\) is used.

## 2. The exact relation between M and the plane gradient

At fixed original \(t\), the derivative is
\(\partial_\rho=\mathcal D-(h/\rho)\partial_h\).
Applying it to (2), with \(C\) complex, yields
\[
\begin{aligned}
k_\rho
 &=-C/\rho^2+F-hF_h-hG_h/\rho\\
 &=-M-\frac{C}{\rho^2}(1+hb).
\end{aligned}
\tag{3}
\]
Thus no radial derivative has been substituted for the original
coefficient partial.

In the original independent formal variables \(U,V\), the selected
plane equation can be normalized to
\(\Gamma(U,V)=V-P(U-hV)\).
Put \(p=P'(\xi)\). Its evaluated gradient is
\[
\Gamma_U(y,\vartheta)=-p,\qquad
\Gamma_V(y,\vartheta)=1+hp
 =-\frac{\rho^2}{C}(R+M).
\tag{4}
\]
The last equality follows from
\(p=2\rho\xi/C+b\), (2), and (3). It is an identity in
\(L[\xi]\), with no ambient coordinate change.

## 3. Actual gradient identities and the two possible orders

Let \(\mathcal H(U,V)\) be the literal sextic eliminant in
[mixed projection217](rank-two-mixed-ratio-projection-reduction-pass217-working.md),
equation (6), including all lower potentials. Set
\[
\widetilde{\mathcal H}(T,V)=\mathcal H(T+hV,V),\qquad
q_1=\widetilde{\mathcal H}_V(\xi,P(\xi)).
\tag{5}
\]
The affine-\(\xi\) argument in quadratic reduction217 proves
\(0\ne q_1\mid R^2\) in \(O=L[v]=L[\xi]\). Its hypotheses
include the actual calibration, both universal potentials, and
the already proved nonzero \(\xi_v\in L^*\); none is replaced
by a formal graph assumption here.

For explicit sign and derivative conventions, let
\[
\begin{gathered}
B_1=f_t(y,\vartheta)+q_{t\rho}w,\qquad
C_1=f_\rho(y,\vartheta)+q_{\rho\rho}w,
\qquad q=t^2/\rho,\\
S=H_3(q)+H_2(k)+H_1(n),\qquad
\Lambda_i=\ell_i-S_i(y,\vartheta)-\mathcal R_i(y,\vartheta)w,
\quad i=t,\rho,\\
\mathcal R=f_V,\qquad R=\mathcal R(y,\vartheta).
\end{gathered}
\tag{6}
\]
Here \(f=H_2(q)+H_1(k)+n\), and the Taylor polynomials \(H_j\)
are those of universal184. All derivatives of formal polynomials
fix \(U,V\) before evaluation. In particular \(B_1\) retains
the mixed term \(q_{t\rho}w\).

The two potentials, their formal gradients, and the selected factor
give the following polynomial identities in \(O\):
\[
\begin{gathered}
B_1(1+hp)+C_1p+Rw_\xi=0,\qquad w_\xi=w_v/\xi_v,\\
\mathcal H_U(y,\vartheta)=-R(C_1B_1+R\Lambda_t)=-p q_1,\\
\mathcal H_V(y,\vartheta)=-R(C_1^2+R\Lambda_\rho)=(1+hp)q_1,\\
q_1=h\mathcal H_U(y,\vartheta)+\mathcal H_V(y,\vartheta).
\end{gathered}
\tag{7}
\]
The last line is only the formal chain rule in (5); it does not
hold \(h\) constant under coefficient differentiation. The first
line follows by differentiating the third potential in \(v\)
and dividing by the proved scalar \(\xi_v\ne0\).

Every gradient on the last line of (7) is divisible by \(R\).
Together with the retained upper bound, this proves
\[
R\mid q_1\mid R^2,\qquad
q_1=\kappa R^j\quad\hbox{for some }\kappa\in L^*,\quad j\in\{1,2\}.
\tag{8}
\]
Indeed \(R\) is a nonconstant linear polynomial over \(L\).
It has the single simple root
\(\xi_* =\rho k_\rho/(2h)\in L\), so no splitting-field or
normality assumption is required for this divisibility argument.

We will also use the original calibrated wedge identity
\[
J_0=
\left[dy\wedge(R\,d\vartheta+B_1dt+C_1d\rho)\wedge dw\right]
 _{dt\wedge d\rho\wedge dv}
=-a^3\in L^*.
\tag{9}
\]
All coefficient entries of this determinant lie in \(L[v]\).
Since \(\xi\) is affine in \(v\), evaluating at \(\xi=\xi_*\)
is an \(L\)-algebra map on that polynomial ring. We evaluate the
already formed identity (9); we never differentiate the moving
root \(\xi_*\) as if it were constant. In particular if
\(R,B_1,C_1\) all vanished there, the middle wedge would vanish,
contradicting (9).

## 4. Distinguishing the simple and double cofactors

Suppose first \(M\ne0\). Equation (4) gives
\(\Gamma_V(\xi_*)=-\rho^2M/C\ne0\).
If \(C_1(\xi_*)=0\), the first line of (7), with
\(R(\xi_*)=0\), forces \(B_1(\xi_*)=0\). This contradicts
(9). Hence \(C_1(\xi_*)\ne0\).
The second gradient in (7) now has exactly order one at the
simple root of \(R\): its factor
\(C_1^2+R\Lambda_\rho\) is nonzero there. Since
\(\Gamma_V\) is also nonzero there, \(q_1\) has order one.
Equation (8) gives \(q_1\in L^*R\).

Suppose next \(M=0\). Equation (4) makes \(1+hp\)
proportional to \(R\). Thus \(p(\xi_*)=-1/h\ne0\).
The first line of (7) then forces \(C_1(\xi_*)=0\), so
\(R\mid C_1\) in \(O\). The first gradient in (7) is
therefore divisible by \(R^2\). Its other factor
\(\Gamma_U(\xi_*)=-p(\xi_*)=1/h\ne0\) is a unit at the
root, so \(q_1\) has order at least two. The upper bound in (8)
makes that order exactly two. We have proved
\[
\boxed{
M\ne0\ \Longleftrightarrow\ q_1\in L^*R,\qquad
M=0\ \Longleftrightarrow\ q_1\in L^*R^2.}
\tag{10}
\]
The converses follow because the two cases of \(M\) exhaust the
field \(L\), and the two orders are distinct.

## 5. Scope

This result identifies a local order in the exact generic line
ring, using the actual scalar determinant to distinguish the
cases. It does not make \(\xi\), the cofactor scalar \(\kappa\),
or any radial-constant function regular or invertible in the
original polynomial ring. No branch is asserted to be realized,
excluded, or recognized by this dichotomy alone.

In particular it does not by itself remove the square-root mode
allowed by the preceding218 determinant coefficient. Further
lower-potential equations are separate inputs, not assumptions
of the proof above. No original coordinate, slice, minimum-profile
theorem, arbitrary-entry theorem, or unrestricted cancellation
result is supplied here.

The retained218 notes and complete217 conic proof were independently
read before this argument; the exact coefficient and gradient
identities were reconstructed above. No saved checker was executed,
imported, or compiled. No217 or earlier source, packet, or index
was changed. This is not human expert review, proof-assistant
certification, or a claim of historical novelty.
