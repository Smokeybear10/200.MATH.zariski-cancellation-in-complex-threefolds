# An original polynomial shear recognizes the constant-y cusp branch

Status: complete working proof with separate saved-source AI reviews of
this note and its new projected-field input. The theorem concerns the
actual nonzero-r, constant-y branch of the sliced cusp chart159.
It is not an entry theorem for arbitrary sliced four-variable actions.

## 1. Actual hypotheses and the projected-field input

Retain the complete actual setup159:
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\\
(\deg_E X,\deg_E Y,\deg_E Z,\deg_E W)=(1,1,2,2),\\
\ker\theta_0=(\mathsf X\mathsf Z-\mathsf Y^3),\qquad
a=EX\ne0,\qquad t=EY/a,\qquad \rho=(E^2W/2)/a^2 .
\end{gathered}
\tag{1}
\]
The kernel in (1) is the full initial kernel in weights
\((1,1,2,2)\). With the actual selected intrinsic LND
\(N=[u^3](\partial_Z|_A)\), put \(L=\operatorname{Frac}\ker_A N\).
The retained conclusions include \(a\in L^*\),
\(L/\mathbb C(t,\rho)\) finite separable, independence of \(t,\rho\),
and the whole generic line \(A_L=L[v]\), \(Nv=1\).

Assume precisely \(r=k_\rho\ne0\) and \(y\in L\). The actual
chart and its field return are
\[
\begin{gathered}
Y=y+tX,\quad Z=z+\sigma X+t^3X^2,\quad
W=w+\vartheta X+\rho X^2,\quad \sigma=3t^2y+k,\\
z=3ty^2+k_t^{\rm old}y+r\vartheta+n,\qquad
L[y,\vartheta]=L[v],\qquad
\operatorname{Frac}A=\mathbb C(y,z,w)=L(v),\\
A_a=\mathbb C[y,z,w]_{a_0},\qquad a=a_0(y,z,w)\in L^* .
\end{gathered}
\tag{2}
\]
The old derivative holds rho fixed. All three projected entries
are algebraically independent over \(\mathbb C\).
Since \(y\in L\), the whole-line equality makes \(\vartheta\)
affine in \(v\), with nonzero coefficient. Thus \(z\) too is an
affine whole-line parameter.

Use the new
[parabola field-return proof174](cusp-constant-projection-parabola-field-pass174-working.md).
Its conclusion, obtained using the actual single localization in
(2), is
\[
w=\alpha(y)z^2+\beta(y)z+g,\qquad
\alpha,\beta\in\mathbb C(y),\qquad L=\mathbb C(y,g).
\tag{3}
\]
This is an explicit input to the present note. Field equality
alone does not imply that its first two coefficients belong to
\(\mathbb C(y)\). Neither \(y\), \(g\), nor a rational function
of \(y\) is being assumed integral in \(B\).

## 2. Legitimate coefficient derivatives in t and y

The actual159 determinant, with \(X\) fixed, is
\[
\det\frac{\partial(Y,Z,W)}{\partial(t,\rho,v)}=-a^3\in L^*.
\tag{4}
\]
If the old coefficient derivative \(y_\rho\) were zero, its
first row would be \((X+y_t^{\rm old},0,0)\), since \(y_v=0\).
The determinant would be divisible by the nonconstant monic
polynomial \(X+y_t^{\rm old}\) in \(L[v][X]\), contradicting (4).
Consequently \(y_\rho\ne0\).

As \(\partial_\rho\) kills \(t\), in characteristic zero this
also shows that \(y\) is not algebraic over \(\mathbb C(t)\).
Thus \(t,y\) are algebraically independent and form a separating
transcendence basis for \(L/\mathbb C\).
Extend their two partials uniquely to the finite separable
extension \(L/\mathbb C(t,y)\). They commute and their common
constant field is \(\mathbb C\). For the latter assertion,
differentiate a monic minimal polynomial over \(\mathbb C(t,y)\)
of a joint constant: minimality makes both coefficient derivatives
zero, so its coefficients lie in \(\mathbb C\), which is
algebraically closed.

In the remainder, subscripts \(t,y\) denote these new partials,
not the old fixed-rho derivative. Extend them to fix \(X,z\).
Set
\[
H=1/r,\qquad \vartheta=Hz+J,\quad J\in L,\qquad
\sigma=3t^2y+k .
\tag{5}
\]
The change of separating triples has determinant
\[
\det\frac{\partial(t,y,z)}{\partial(t,\rho,v)}
=y_\rho z_v\in L^*.
\tag{6}
\]
It is independent of \(X\). Therefore the Jacobian of
\((Y,Z,W)\) in \((t,y,z)\) is a nonzero scalar in \(L\),
independent of \(X\). At \(X=0\), using (3), it is \(g_t\).
In particular \(g_t\ne0\). This assertion does not normalize
that scalar to a global unit of a polynomial ring.

## 3. Two determinant coefficients remove the quadratic term

Write \(w_z=2\alpha z+\beta\), and keep \(z\) fixed in coefficient
derivatives. Direct expansion of the actual determinant gives
\[
\begin{aligned}
\det\frac{\partial(Y,Z,W)}{\partial(t,y,z)}
={}&g_t\\
&+X\{\vartheta_t-\sigma_t w_z-w_y\}\\
&+X^2\{\rho_t+k_yw_z-H\sigma_t-\vartheta_y\}\\
&+X^3\{Hk_y-\rho_y\}.
\end{aligned}
\tag{7}
\]
For example its matrix is
\[
\begin{pmatrix}
X&1&0\\
\sigma_tX+3t^2X^2&\sigma_yX&1\\
g_t+\vartheta_tX+\rho_tX^2&
w_y+\vartheta_yX+\rho_yX^2&
w_z+HX
\end{pmatrix},
\]
and \(\sigma_y=3t^2+k_y\). This establishes both the signs
and the derivative convention in (7).

Every positive \(X\) coefficient vanishes. Compare coefficients
in the independent parameter \(z\) in the \(X\) and \(X^2\)
coefficients. They give
\[
\alpha_y=0,\qquad
H_t=2\alpha\sigma_t+\beta_y,\qquad
H_y=2\alpha k_y .
\tag{8}
\]
Since \(\alpha\in\mathbb C(y)\), the first identity says
\(\alpha\in\mathbb C\). Commuting the two partials in (8), and
using \(\sigma_{ty}=6t+k_{ty}\), now gives
\[
\beta_{yy}=-12\alpha t .
\tag{9}
\]
The left side belongs to \(\mathbb C(y)\) and is killed by
\(\partial_t\); differentiating (9) in \(t\) yields
\(\alpha=0\). A rational function of \(y\) with zero second
derivative is affine. Hence
\[
\beta=\lambda y+\nu,\qquad
H=\lambda t+\mu,\qquad \lambda,\nu,\mu\in\mathbb C .
\tag{10}
\]
Indeed (8) now gives \(H_t=\lambda\), \(H_y=0\), so
\(H-\lambda t\) is a joint constant of the exact field \(L\).
At least one of \(\lambda,\mu\) is nonzero since \(H=1/r\ne0\).
No division by \(\lambda\), \(\mu\), or \(a\) in \(B\) has
occurred.

## 4. An original polynomial shear creates a commuting partial

The crucial coefficient from (10) is already polynomial in the
original coordinates:
\[
\beta(y)+H(t)X=\lambda Y+\nu+\mu X=:C(X,Y).
\tag{11}
\]
Define
\[
V=W-C(X,Y)Z,\qquad
W=V+C(X,Y)Z,\qquad B=\mathbb C[X,Y,Z,V].
\tag{12}
\]
These displayed maps are polynomial inverses in both orders,
fixing \(X,Y,Z\). Thus \(V\) is an actual coordinate, regardless
of the rational status of the projected coefficients.

In the chart (2), after (3) and (10), this coordinate has no
dependence on \(z\):
\[
V=g+(J-\beta\sigma)X+
  (\rho-H\sigma-\beta t^3)X^2-Ht^3X^3\in L[X].
\tag{13}
\]
Also \(X,Y\in L[X]\) and \(Z=z+\sigma X+t^3X^2\).
On the common fraction field \(L(X,z)\), let \(T_0=\partial_z\)
fix \(L,X\). Then
\[
T_0X=T_0Y=T_0V=0,\qquad T_0Z=1.
\tag{14}
\]
Since (12) is an actual coordinate system, these values identify
\(T_0\) with its actual polynomial coordinate partial
\(\partial_Z\), now holding \(X,Y,V\) fixed. This is not the
old selected partial holding \(W\) fixed.

The sliced action on this same field is \(E=a\partial_X\),
fixing \(L,z\), with \(a\in L\). It follows that
\[
[E,T_0]=0 .
\tag{15}
\]
In the actual frame (12), commutation says that all polynomial
coefficients of \(E\) are independent of \(Z\). Therefore the
three-ring \(R=\mathbb C[X,Y,V]\) is stable under \(E\), and
\[
E=D+f\partial_Z,\qquad
0\ne D\in\operatorname{LND}_{\mathbb C}(R),\quad f\in R,\qquad
DX\ne0,\quad D^2X=D^2Y=0 .
\tag{16}
\]
No slice on \(D\), or unit condition on \(f\), is inferred.

## 5. Published three-variable classification and recognition

For clarity, the passage to an irreducible derivation in Wang's
theorem is elementary here. Let \(\delta\ne0\) be the polynomial
gcd of \(DX,DY,DV\), and write \(D=\delta D_0\).
If \(D\delta=\delta D_0\delta\ne0\), additivity of LND degree
on products gives degree at least \(\deg_D\delta\) on the right,
but \(\deg_D(D\delta)=\deg_D\delta-1\) on the left.
Thus \(D\delta=D_0\delta=0\). By induction
\[
D^j h=\delta^jD_0^j h,\qquad
0\ne D_0\in\operatorname{LND}_{\mathbb C}(R),\qquad
D_0^2X=D_0^2Y=0,\qquad \ker D_0=\ker D .
\tag{17}
\]
Its coefficient gcd is one, as required by the published
irreducibility hypothesis.

Apply Wang's two-coordinate theorem, as reproduced in
Dasgupta--Gupta Theorem 4.1, to \(R=\mathbb C[X,Y,V]\).
In its first alternative an invariant nonzero complex linear
form in \(X,Y\) would make \(t=EY/EX\) complex, contrary to
the retained independence. In its second alternative there
is an actual coordinate \(\xi\) such that
\[
R=\mathbb C[\xi,X,Y],\qquad D_0\xi=0 .
\tag{18}
\]
Since \(\xi\) is in \(R\), equations (16)--(17) give \(E\xi=0\).
In particular \(B=\mathbb C[\xi,X,Y,Z]\) has an actual invariant
ambient coordinate.

Finally \(A=\ker E\) is regular. Indeed \(Eu=1\) expresses one
as a polynomial combination of the ordinary partial derivatives
of \(u\); consequently \(B/(u)\simeq A\) is smooth over
\(\mathbb C\). Bhatwadekar--Gupta--Lokhande Theorem 3.5 applies
to the nonzero \(\mathbb C[\xi]\)-linear LND \(E\) and gives
\[
A=\mathbb C[\xi]^{[2]}\simeq\mathbb C^{[3]} .
\tag{19}
\]
Both classification statements are imported published theorems.
The coordinate furnished by Wang is not being claimed as an
explicit computed polynomial formula here.

## Scope and sources

The recognition covers the retained actual branch \(r\ne0\),
\(y\in L\), conditional on the separately proved projected-field
input174. It does not assume that the selected plane relation is
pure: extra factors in that relation were not discarded.
Together with the nonconstant-y recognition171 and the zero-r
arguments172--173, a completed review would cover the entire
actual cusp setup159. Other initial profiles and arbitrary
coordinate entry remain independent obligations.

1. [Actual cusp chart159](cusp-generic-chart-first-reductions-pass159-working.md),
   for the actual inverse, whole generic line, coefficient field,
   and calibrated determinant.
2. [Parabola field-return174](cusp-constant-projection-parabola-field-pass174-working.md),
   for precisely (3). Its single-localization argument is essential.
3. [Zero-r exclusion172](cusp-zero-r-constant-projection-exclusion-pass172-working.md),
   for a separate earlier commuting-partial mechanism. The
   primitive-content and classification steps needed here are
   stated above, without importing that branch's contradiction.
4. Nikhilesh Dasgupta and Neena Gupta,
   [Nice derivations over principal ideal domains](https://arxiv.org/pdf/1701.03635v1),
   Theorem 4.1, printed p. 9, reproducing Wang's Theorem 4.7
   and Remark 5. The exact two alternatives were freshly read.
5. S. M. Bhatwadekar, Neena Gupta and Swapnil A. Lokhande,
   [Some K-theoretic properties of the kernel of a locally nilpotent derivation on k[X1,...,X4]](https://arxiv.org/html/1501.01438v1),
   Theorem 3.5; the exact statement and displayed proof were
   freshly read, not the whole historical dependency chain.

This is a human-readable algebraic proof draft. AI reconstruction
and finite symbolic controls are not expert review, formal
certification, or historical novelty clearance. No unrestricted
cancellation theorem, publication, or external contact is claimed.
All173 and earlier mathematical artifacts are unchanged.
