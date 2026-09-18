# Quadratic-affine first potentials: exact transport and an actual1123 transfer

Working result: in the actual principal chart264 with \(k=s\) and
\(n=Dt^2+At+Bs+C\), where all four coefficients are complex, an
explicit polynomial reframe gives \(k_*=s_*\) and
\(n_*=(D-B^2)t^2\), with the full actual chart retained.
Consequently the case \(D=B^2\) is recognized by330.

If \(D-B^2\ne0\), a different explicit polynomial map supplies an
invariant coordinate when \(\ell+Ds\) is complex, and otherwise an
actual frame of profile1123. This is a transfer, not recognition of all
nonzero-residual cases. In particular an affine n with nonzero s-slope
does not become zero under the first reframe.

## 1. Complete retained actual hypotheses

Retain the full actual hypotheses of
[264](principal-one-affine-paraboloid-chart-pass264-working.md):
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A_0[u],\qquad E=\partial_u,
\quad A_0=\ker E,\quad\deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the full weighted initial kernel},\qquad a_0=EX\ne0,\\
N=[u^4]\partial_Z|_{A_0}\ne0,\quad Na_0=Nt=Ns=0,\quad
L=\operatorname{Frac}\ker_{A_0}N,\quad[L:\mathbb C(t,s)]<\infty,\\
K=\operatorname{Frac}A_0=L(v),\quad Nv=1,\quad
K=\mathbb C(y,z,w),\quad L[y,z,w]=L[y,\sigma,\theta]=L[v],\\
\det\frac{\partial(Y,Z,W)}{\partial(t,s,v)}=-a_0^4\in L^*.
\end{gathered}
\tag{1}
\]
The coefficient partials commute and fix v. The coefficient field and
all intercepts are killed by E. Assume
\[
k=s,\qquad n=Dt^2+At+Bs+C,
\qquad A,B,C,D\in\mathbb C,
\qquad \Delta=D-B^2.
\tag{2}
\]
There is no restriction on the coefficient-field function ell.
The actual fixed-X map and first two potentials are
\[
\begin{aligned}
Y&=y+\sigma X+tX^2,\\
Z&=z+(2t\sigma+s)X+t^2X^2,\\
W&=w+\theta X+sX^2,\\
z&=2ty+\sigma^2+\theta+Dt^2+At+Bs+C,\\
w&=\ell-2\sigma y-(2Dt+A)\sigma-B\theta.
\end{aligned}
\tag{3}
\]
No surface factorization or projected-degree hypothesis is imposed.

## 2. An actual polynomial reframe and its coefficient transport

Make the constant-coefficient polynomial changes
\[
X_*=X+B,\qquad Y_*=Y+A/2,\qquad Z_*=Z-C,
\qquad W_*=W+2BZ.
\tag{4}
\]
Their inverse is
\[
X=X_*-B,\qquad Y=Y_*-A/2,\qquad Z=Z_*+C,
\qquad W=W_*-2B(Z_*+C).
\tag{5}
\]
Both compositions are polynomial identities in the original ring.
At fixed X*, full substitution in (3) gives
\[
\begin{aligned}
t_*&=t,&s_*&=s+2Bt^2,&k_*&=s_*,\\
y_*&=y-B\sigma+B^2t+A/2,&
\sigma_*&=\sigma-2Bt,\\
z_*&=z-2Bt\sigma-Bs+B^2t^2-C,\\
\theta_*&=\theta+4Bt\sigma-4B^2t^2,\\
w_*&=w+2Bz-B\theta-4B^2t\sigma-B^2s+2B^3t^2.
\end{aligned}
\tag{6}
\]
In particular the new expressions retain the literal shape
\[
Y_*=y_*+\sigma_*X_*+tX_*^2,\quad
Z_*=z_*+(2t\sigma_*+s_*)X_*+t^2X_*^2,\quad
W_*=w_*+\theta_*X_*+s_*X_*^2.
\tag{7}
\]
All expressions on the right side of (6) are initially in the old
coefficient field and polynomial line. The new coefficient partials are
\[
\partial_{t,*}=\partial_t-4Bt\partial_s,
\qquad\partial_{s,*}=\partial_s,
\tag{8}
\]
still fixing v. Literal calculation of the two new potentials gives
\[
\boxed{
\begin{aligned}
z_*&=2ty_*+\sigma_*^2+\theta_*+n_*,
&n_*&=\Delta t^2,\\
w_*+2\sigma_*y_*+2\Delta t\sigma_*&=\ell_*,
&\ell_*&=\ell+B^2s+2BC-2B\Delta t^2.
\end{aligned}}
\tag{9}
\]
The rightmost formula is an equality in the old field L; replacing
\(s\) by \(s_*-2Bt^2\) expresses the same function in the new
coefficient parameters. It does not replace old coefficient derivatives
by new ones silently. In particular \((n_*)_{s,*}=0\) and
\((n_*)_{t,*}=2\Delta t\), as used in (9).

## 3. Full initial kernel, selected partial, and actual returns

The weighted leading change fixes X,Y,Z and sends W to W+2BZ.
It is invertible and fixes the polynomial \(X^2Z-Y^2\), which is
independent of W. Therefore the **full** initial kernel remains the
same principal ideal. Since t,s are independent, so are t,s*, and
the new W leader does not vanish. All four time degrees remain1222,
and \(EX_*=a_0\).

The new literal Z-partial is
\[
\partial_{Z_*}=\partial_Z-2B\partial_W.
\tag{10}
\]
The old W-partial has shift at most three: its omitted leading triple
X,Y,Z is dependent, whereas the selected Z-partial has exact shift
four. This is the retained omitted-triple gate used explicitly in
[302](principal-paraboloid-reducible-surface-conic-reduction-pass302-working.md)
and [314](principal-paraboloid-variable-coupling-hodograph-reduction-pass314-working.md).
Hence (10) has the same shift-four leading derivation N. Its exact
constant field L, localization O and normalized parameter v are unchanged.

The intrinsic map \((y,\sigma,\theta)\mapsto(y_*,\sigma_*,\theta_*)\)
in (6) is invertible affine over L. Thus it preserves whole O-return.
For the actual intercept returns, use the polynomial quotient again:
\(\mathcal B_{a_0}=(A_0)_{a_0}[X_*]\), and evaluate at \(X_*=0\)
in the new actual polynomial frame. Exactly as in264 this gives
\[
K=\mathbb C(y_*,z_*,w_*),\qquad L[y_*,z_*,w_*]=O.
\tag{11}
\]
For the second equality, localize further at the same \(\ker N\);
the denominator a0 is already a unit in L. Neither equality is inferred
from an L-affine intrinsic change alone.

At fixed X*, the three actual row changes in (4) have determinant one.
The coefficient change \((t,s)\mapsto(t,s_*)\) has determinant one.
The full calibrated polynomial therefore satisfies
\[
J_*(X_*)=J(X_*-B)=-a_0^4.
\tag{12}
\]
All hypotheses needed to rebuild the actual chart264 are retained.
No claim about transporting an old surface factorization is necessary.

If \(\Delta=0\), equations (7),(9) put the new actual chart exactly
in \(k_*=s_*,n_*=0\), with arbitrary ell*. The completely read
[330](principal-paraboloid-normalized-potential-family-recognition-pass330-working.md)
therefore gives
\[
\boxed{D=B^2\quad\Longrightarrow\quad A_0\cong\mathbb C^{[3]}.}
\tag{13}
\]
This retains330's explicit dependencies on298 and mandatory-corrected301,
and their stated working recognition inputs.

## 4. What the residual means for this reframe family

More generally, take constants \(\delta,\varepsilon,\zeta\) and use
\(X_*=X+\delta,Y_*=Y+\varepsilon,Z_*=Z+\zeta,
W_*=W+2\delta Z\). The same literal computation gives
\[
n_*=(D+\delta^2-2B\delta)t^2+(A-2\varepsilon)t
       +(B-\delta)s_*+C+\zeta,
\qquad s_*=s+2\delta t^2.
\tag{14}
\]
Thus the combination of its quadratic and s-linear coefficients obeys
\(D_*-(B_*)^2=D-B^2\). This is an invariant of the specified
translation/shear family, not an invariant under all polynomial
automorphisms.

For the initially requested affine n, one has D=0. If B=0, the constant
changes \(Y_*=Y+A/2,Z_*=Z-C\) already give n*=0. If \(B\ne0\),
(4) leaves \(n_*=-B^2t^2\ne0\). No conclusion of330 can be applied
to that residual merely by dropping it.

## 5. A separate actual1123 transfer when the residual is nonzero

Return to the original frame (3), and suppose \(\Delta\ne0\).
Define actual polynomials
\[
R=Y^2+XW-X^2Z,\qquad
T=R+AY+BW+DZ+CX^2,\qquad
S=(X-B)Z-W.
\tag{15}
\]
With \(U_0=T-Y^2-AY-CX^2\), their coefficient matrix is
\[
\begin{pmatrix}U_0\\S\end{pmatrix}
=\begin{pmatrix}D-X^2&X+B\\X-B&-1\end{pmatrix}
\begin{pmatrix}Z\\W\end{pmatrix},
\qquad\det=B^2-D=-\Delta.
\tag{16}
\]
Consequently X,T,Y,S are actual polynomial coordinates, with inverse
\[
Z=\frac{U_0+(X+B)S}{\Delta},\qquad
W=\frac{(X-B)U_0+(X^2-D)S}{\Delta}.
\tag{17}
\]
Only the complex unit Delta is divided out. The literal potentials give
\[
\begin{aligned}
R&=y^2+\bigl(\ell-(2Dt+A)\sigma-B\theta\bigr)X-nX^2,\\
T&=y^2+Ay+Bw+Dz+(\ell+Ds)X,\\
S&=t^2X^3+(2t\sigma-Bt^2)X^2
     +\bigl(z-B(2t\sigma+s)-\theta\bigr)X-Bz-w.
\end{aligned}
\tag{18}
\]
Put \(\eta=\ell+Ds\in L\). Then \(ET=a_0\eta\), \(E^2T=0\),
and S has exact E-degree three with leading ratio t squared.
If \(\eta\in\mathbb C\), the actual coordinate \(T-\eta X\) is
invariant. The regular-kernel invariant-coordinate endpoint gives
\(A_0\cong\mathbb C^{[3]}\), since the original global slice makes
the kernel regular. The precise published input is
[Bhatwadekar--Gupta--Lokhande, Theorem3.5](https://arxiv.org/html/1501.01438v1),
applied to the nonzero original E fixing this actual coordinate.

Otherwise this actual frame has exact profile
\[
\deg_E(X,T,Y,S)=(1,1,2,3).
\tag{19}
\]
Its leaders are \(a_0,a_0\eta,a_0^2t,a_0^3t^2\), so its full
initial kernel contains
\(\mathsf X\mathsf S-\mathsf Y^2\). If t,eta are algebraically
independent over C, the initial fraction field is
\(\mathbb C(t,\eta)(a_0\tau)\), of transcendence degree three.
The full kernel is then exactly the principal ideal generated by that
irreducible polynomial. If t,eta are dependent, that initial fraction
field has transcendence degree two and the full kernel has height two.
In neither case is a mere relation substituted for the entire kernel.

The retained1123 frontier is not a recognition theorem for all such
frames. Equation (19) is therefore an actual profile transfer, not a
completed endpoint. Its total degree sum remains seven. In particular,
for affine n with B nonzero, nonconstant ell remains open here after
this transfer. No field parameter has been made an ambient coordinate.
The detailed258/263 quadratic-cubic branches require height two and
their selected shift hypothesis; they do not complete the principal
height-one alternative just displayed.

## 6. Scope and verification boundary

The proved recognition cases are Delta=0 and, separately, Delta nonzero
with ell+Ds complex. The nonzero residual is explicitly retained in all
other cases. There is no assertion that a general n is quadratic-affine,
that an arbitrary k can be made s, or that all supplied1222 frames are
recognized.

Complete264,302,314 and330 were read for their actual-entry and reframe
hypotheses. A new unsaved algebra calculation reconstructed both
potential transports, the direct T expansion, and the two coefficient
determinants. The inverse formulas and field-return gates are supplied
above; finite symbolic identities do not certify the retained recognition
theorems. No saved checker was executed, imported, compiled, or rerun.
No earlier proof, canonical index, or ledger was edited.
