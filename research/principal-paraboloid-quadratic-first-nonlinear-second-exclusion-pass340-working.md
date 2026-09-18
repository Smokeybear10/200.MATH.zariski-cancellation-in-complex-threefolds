# Exclusion of the nonlinear-second-potential quadratic-first line

Working result: the actual principal chart with `k=s`, a nonzero complex
quadratic first potential, and `ell_s ell_ss != 0` cannot occur. The full
plane primitive and its unit cofactor force four coefficient equations.
Their mixed-derivative compatibility makes the complete actual Jacobian
zero. No intrinsic coefficient is promoted to an ambient coordinate.

This is a bounded exclusion in the supplied chart, not a normalization of
arbitrary first potentials or recognition of arbitrary time profiles.

## 1. Exact retained branch and scalar conversion

Retain all actual hypotheses of264 and the complete saved reductions
[333](principal-paraboloid-one-variable-first-potential-plane-reduction-pass333-working.md)
and
[336](principal-quadratic-first-affine-line-specialization-gate-pass336-working.md).
In particular,
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,
\qquad a_0=EX\ne0,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\qquad
I_{\mathrm{initial}}=(\mathsf X^2\mathsf Z-\mathsf Y^2),\\
[L:\mathbb C(t,s)]<\infty,\quad Nv=1,\quad
K=\operatorname{Frac}A=L(v)=\mathbb C(y,z,w),\\
L[y,z,w]=L[y,\sigma,\theta]=L[v],\qquad
J_{t,s,v}(X)=-a_0^4\in L^* .
\end{gathered}
\tag{1}
\]
Here N is the retained leading part of the literal Z-partial. The exact
coefficient partials commute. All coefficient fields and intercepts are
killed by the original E.

Assume
\[
k=s,\qquad n=g t^2,\qquad g\in\mathbb C^*,\qquad
\ell_s\ne0,\quad\ell_{ss}\ne0.
\tag{2}
\]
The same conclusion applies to `n=g t^2+f_1 t+f_0` with complex affine
terms, by333's actual translations `Y*=Y+f_1/2`, `Z*=Z-f_0`, with X,W
fixed. These are genuine constant translations and preserve the stated
chart hypotheses. They do not remove g.

Use333's exact coefficient parameters and centered first function:
\[
r=\ell,\qquad s=H(t,r),\qquad H_r\ne0,\quad H_{rr}\ne0,
\qquad x=y+gt,\qquad \mathcal L=H_r\bar h.
\tag{3}
\]
The nonzero H_rr follows from `ell_ss=-H_rr/H_r^3`. Derivatives from now
on are the commuting exact derivatives in t,r. No rationality of L is
assumed.

The quartic-top argument and whole polynomial return in333 give
\[
x=\alpha\sigma+\beta,\qquad
\alpha\in\mathbb C^*,\quad\alpha^2=-g,\quad\beta\in L,
\qquad O=L[\sigma]=L[v].
\tag{4}
\]
Thus sigma is affine in v, and `q_sigma=N sigma=partial_v sigma` is an
element of L*. The exact change from `(t,s,v)` to `(t,r,sigma)` has
Jacobian `H_r/q_sigma` in the inverse direction. Although sigma's affine
coefficients may depend on t,r, those derivatives lie off the diagonal
of this parameter Jacobian. Consequently the complete actual scalar is
\[
\boxed{J_{t,r,\sigma}(X)
       =-\frac{a_0^4 H_r}{q_\sigma}\in L^*.}
\tag{5}
\]
This conversion uses the original actual determinant, not only a formal
plane equation. It is the contradiction target below.

## 2. The full primitive and unit normal derivative

For formal U,P,333 gives the complete plane primitive
\[
\begin{aligned}
\Phi={}&\frac{H_{rr}}2(U^2-\alpha^2P^2)^2
 +H_{tr}(U^2-\alpha^2P^2)P+\frac{H_{tt}}2P^2\\
&+2(1-\alpha^2H_r)UP+H_tU
 -\mathcal L_r(U^2-\alpha^2P^2)-\mathcal L_tP.
\end{aligned}
\tag{6}
\]
The `g'` term is zero because g is complex. With
`G=U-alpha P-beta`, the whole line and unit-gradient conclusion give
\[
\Phi-q_1=\eta G+G^2R,\qquad
q_1\in L,\quad\eta\in L^*,\quad R\in L[U,P].
\tag{7}
\]
In particular `Phi(alpha P+beta,P)` is constant in P, and
`Phi_U(alpha P+beta,P)=eta` is also constant in P. These are formal
polynomial identities over the exact field L.

Write `c=1-alpha^2 H_r`. The P-squared and P coefficients of the normal
derivative are, respectively,
\[
4\alpha^2\beta H_{rr}+2\alpha H_{tr},\qquad
2c+6\alpha\beta^2H_{rr}-2\alpha\mathcal L_r+2\beta H_{tr}.
\tag{8}
\]
They vanish. Substituting their consequences into the P-squared and P
coefficients of the restricted primitive gives the exact four equations
\[
\boxed{\begin{aligned}
H_{tr}&=-2\alpha\beta H_{rr},&
\mathcal L_r&=\beta^2H_{rr}+c/\alpha,\\
H_{tt}&=4\alpha^2\beta^2H_{rr}-4\alpha c,&
\mathcal L_t&=\alpha H_t-2\alpha\beta^3H_{rr}.
\end{aligned}}
\tag{9}
\]
Only the nonzero complex alpha is divided out. The constant normal
coefficient is
\[
\boxed{\eta=H_t-\frac{2\beta c}{\alpha}\ne0.}
\tag{10}
\]
For comparison with336, the intrinsic theta coefficient below is
`d=2 alpha beta H_r+H_t`, and `alpha d-2 beta=alpha eta`.
Thus the cofactor already implies336's necessary specialization gate;
no additional actual-coordinate conclusion is inferred from this fact.

## 3. Mixed compatibility

The two H-equations in(9), differentiated using the commuting exact
coefficient partials, give
\[
\begin{aligned}
H_{rrt}&=-2\alpha\beta_rH_{rr}-2\alpha\beta H_{rrr},\\
(H_{tt})_r-(H_{tr})_t
 &=2\alpha H_{rr}
   (\beta_t+2\alpha\beta\beta_r+2\alpha^2).
\end{aligned}
\tag{11}
\]
The left side is zero. Since both alpha and H_rr are nonzero, this forces
\[
\boxed{\beta_t+2\alpha\beta\beta_r+2\alpha^2=0.}
\tag{12}
\]
Equivalently the first two terms sum to `2g`. There is no division by
beta, beta_r, c, or any derivative whose nonvanishing has not been shown.

## 4. The complete literal actual determinant

Here P denotes the actual intrinsic parameter sigma. Define
\[
d=2\alpha\beta H_r+H_t,\qquad
e=\beta^2H_r-\mathcal L,\qquad x=\alpha P+\beta.
\tag{13}
\]
The first two potentials, the solved third relation, and the original
actual expansions give the full formulas
\[
\begin{aligned}
y&=\alpha P+\beta+\alpha^2t,&\theta&=dP+e,\\
z&=P^2+(2\alpha t+d)P+2t\beta+\alpha^2t^2+e,&
w&=r-2\alpha P^2-2\beta P,\\
Y&=y+PX+tX^2,&
Z&=z+(2tP+H)X+t^2X^2,\\
W&=w+(dP+e)X+HX^2.
\end{aligned}
\tag{14}
\]
In particular these are not merely intercept identities used in place
of the full actual map.

Let `mathrm d` below mean differential in `(t,r,P)` with X fixed. Equations
(9) give, without using(12),
\[
\begin{aligned}
\mathrm d d&=2\alpha H_r\,\mathrm d\beta-4\alpha c\,\mathrm dt,\\
\mathrm d e&=2\beta H_r\,\mathrm d\beta
                 -\alpha H_t\,\mathrm dt-(c/\alpha)\,\mathrm dr,\\
\mathrm d\theta&=d\,\mathrm dP+2H_rx\,\mathrm d\beta
 -(4\alpha cP+\alpha H_t)\,\mathrm dt-(c/\alpha)\,\mathrm dr.
\end{aligned}
\tag{15}
\]
These equalities keep all moving coefficient derivatives.

Start with determinant rows
\[
\mathsf A=\mathrm dY,
\qquad\mathsf B=\mathrm dZ-2t\,\mathrm dY,
\qquad\mathsf C=\mathrm dW.
\tag{16}
\]
The initial row subtraction preserves the actual determinant. Direct
substitution of(14),(15) gives
\[
\begin{aligned}
\mathsf A&=(\alpha+X)\,\mathrm dP+\mathrm d\beta
                      +(\alpha^2+X^2)\,\mathrm dt,\\
\mathsf C_1:=\mathsf C-X\mathsf B+2P\mathsf A
 &=\mathrm dr-2x\,\mathrm dP
                       +(2\alpha^2P-2Xx)\,\mathrm dt,\\
\mathsf B_1:=\mathsf B-2H_rx\mathsf A,\qquad
\mathsf B_2:=\mathsf B_1-(XH_r-c/\alpha)\mathsf C_1
 &=\eta\bigl(\mathrm dP+(X-\alpha)\,\mathrm dt\bigr).
\end{aligned}
\tag{17}
\]
The transformation from `(A,B,C)` to `(A,B_2,C_1)` has determinant one.
Set `Q=dP+(X-alpha)dt`. After extracting the nonzero coefficient eta
from the middle row, the further row operations are
\[
\mathsf A-(\alpha+X)Q=\mathrm d\beta+2\alpha^2\,\mathrm dt,
\qquad
\mathsf C_1+2xQ=\mathrm dr-2\alpha\beta\,\mathrm dt.
\tag{18}
\]
Thus, in the ordered variables `(t,r,P)`, the complete determinant is
\[
\begin{aligned}
J_{t,r,P}(X)
 &=\eta\det\begin{pmatrix}
 \beta_t+2\alpha^2&\beta_r&0\\
 X-\alpha&0&1\\
 -2\alpha\beta&1&0
 \end{pmatrix}\\
 &\boxed{=-\eta(\beta_t+2\alpha\beta\beta_r+2\alpha^2).}
\end{aligned}
\tag{19}
\]
This proves the whole polynomial-in-X identity, not only its highest
coefficient. Equation(12) makes(19) identically zero, contradicting the
specific nonzero calibration(5).

## 5. Scope and relation to the retained frontier

The contradiction excludes exactly the actual branch(2), including
complex affine terms in n removed by the stated translations. It uses
the full primitive, its unit normal derivative, commuting coefficient
partials, and the complete actual scalar. A formal solution of only the
plane equations is not an actual counterexample to any recognition or
cancellation statement.

The `ell_ss=0` quadratic-plane alternatives of333 remain outside this
argument: the division by H_rr in(11) is essential and explicitly
confines the result. Arbitrary nonconstant `g=f''/2` is also outside the
claim. The `ell_s=0` one-variable-pair theorem337 is a different branch.

This is not merely an application of reducible-surface synthesis324.
Here the third relation is linear in its formal V-variable with a
nonzero coefficient and is irreducible, as333 explains. Nor is the
1123 transfer in336 used as a recognition theorem. Its all-X gate is
consistent with(10), but the new contradiction already follows from the
full actual determinant.

The complete held sources333 and336 were read before this derivation.
Fresh unsaved symbolic calculations independently reconstructed the
primitive and normal coefficients, the full actual determinant, and
every row identity in(17),(18). The written row proof and exact parameter
conversion provide the argument; these finite calculations are only
controls. No saved checker was executed, imported, compiled, or rerun by
this author. No earlier source, checker, canonical index, or ledger was
edited.
