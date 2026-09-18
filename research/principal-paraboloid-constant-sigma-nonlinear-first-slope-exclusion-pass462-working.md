# Constant sigma is excluded for an arbitrary longitudinal potential

Working exclusion: retain the full actual chart264 and suppose
\(k=s+f\), \(f_s=0\), and \(n_{ss}\ne0\). Then \(\sigma\notin L\).
There is no assumption on \(f'''\), on \(n_{ts}\), or on the second
potential \(\ell\). The proof starts from the sliced third level,
then uses the complete actual scalar. It does not apply a surface
gradient-unit statement to a sliced factorization.

The argument extends the constant-sigma proof of
[366](principal-paraboloid-nonlinear-first-constant-sigma-exclusion-pass366-working.md)
from \(f=0\) to arbitrary \(f\). All longitudinal terms are retained
below. No coefficient-field change is declared an ambient polynomial
automorphism.

## 1. Full actual input and all derivative conventions

Retain every hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md) and the
full scalar calibration of
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md):
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad
\deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\quad\hbox{is the entire weighted initial kernel},\\
a_0=EX\ne0,\qquad X=a_0u+x_0,\quad x_0\in A,\qquad
N=[u^4]\partial_Z|_A\ne0,\\
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,\quad
a_0\in L^*,\quad Nv=1,\\
O=L[A]=L[v]=L[y,z,w]=L[y,\sigma,\theta],\qquad
\operatorname{Frac}A=L(v)=\mathbb C(y,z,w),\\
J_{t,s,v}(X)=
\det\frac{\partial(Y,Z,W)}{\partial(t,s,v)}=-a_0^4.
\end{gathered}
\tag{1}
\]
In particular the original slice is \(u\), not an assumed \(X/a_0\).
The selected \(N\) kills \(a_0,t,s\). The exact coefficient partials
on \(L\) commute and have joint constants \(\mathbb C\). Initially
their extensions fix \(v\). Let
\[
F=\ker_L\partial_s,\qquad k=s+f,\quad f\in F,\qquad
\nu=n_s,\quad b=n_{ts},\quad e=n_{ss}\ne0.
\tag{2}
\]
The field \(F\) is finite over \(\mathbb C(t)\), and the constants
of its exact \(t\)-derivative are \(\mathbb C\). It is not assumed
equal to \(\mathbb C(t)\). Write \(f_i=\partial_t^i f\) and
\(n_i=\partial_t^i n\). Thus \(\nu_t=b,\nu_s=e,b_s=e_t\).
No nonvanishing of \(b\) or any \(f_i\) is assumed.

Suppose, for a contradiction, that \(p=\sigma\in L\). The full literal
rows and the first two potentials are
\[
\begin{aligned}
Y&=y+pX+tX^2,\\
Z&=2ty+p^2+f_1p+\theta+n+(2tp+s+f)X+t^2X^2,\\
W&=\ell-(2p+f_1)y-\frac{f_2}2p^2-n_1p-\nu\theta
       +\theta X+sX^2.
\end{aligned}
\tag{3}
\]
Every coefficient in these expressions may move under the exact
coefficient derivatives.

## 2. The sliced conic gives an actual intrinsic affine parameter

The complete third potential, independently valid for arbitrary \(f\)
and \(n\), is
\[
\begin{aligned}
H={}&U^2+\{(f_2-2\nu)P+n_1-\nu f_1\}U
 +\frac{f_3}6P^3+\frac{n_2-\nu f_2}2P^2\\
&-(\nu n_1+\ell_t)P+\nu\ell
 +(bP-\ell_s-\nu^2)V+\frac e2V^2,\qquad
H(y,p,\theta)=h\in L .
\end{aligned}
\tag{4}
\]
This is the complete formula from
[458, Sections 1--3](principal-paraboloid-arbitrary-first-potential-birational-projection-pass458-working.md),
not its later nonzero-\(f_3\) projection specialization.

At \(P=p\), completing squares in \(U,V\) changes (4) into
\(\widetilde U^2+(e/2)\widetilde V^2=d_0\), with \(d_0\in L\).
After a temporary algebraic closure \(M/L\), this factors as
\((\widetilde U+a\widetilde V)(\widetilde U-a\widetilde V)=d_0\),
where \(a^2=-e/2\ne0\). If \(d_0\ne0\), both factors in \(M[v]\)
are units, hence constant. That would make \(y,\theta\) constant,
contradicting the whole return \(O=L[y,\theta]=L[v]\).
Thus \(d_0=0\), and one factor vanishes.

It follows that \(\theta\) is nonconstant and \(y\) is affine in
\(\theta\). The slope descends to \(L\) as the ratio of their leading
\(v\)-coefficients; the intercept then descends too. Write
\[
y=A V+B,\qquad V=\theta,\qquad A,B\in L,\qquad
A^2=-e/2\ne0,\qquad O=L[V],\qquad \rho=NV\in L^*.
\tag{5}
\]
The equality \(O=L[V]\) forces \(V\) to have degree one in the
original \(v\). No square root was adjoined to the retained field.
Only the conic factorization used a temporary scalar extension.

The coefficient derivatives now fix \(V\), still agree with the
original derivatives on \(L\), and commute. The triangular change
from \((t,s,v)\) to \((t,s,V)\) has determinant \(\rho\), including
all moving coefficients. Therefore
\[
J:=J_{t,s,V}(X)=-a_0^4/\rho\in L^*.
\tag{6}
\]
The full determinant is independent of both \(V\) and \(X\).

For completeness, set \(A_1=f_2-2\nu\), \(B_1=n_1-\nu f_1\).
The three coefficients of the sliced third level are exactly
\[
\begin{aligned}
&A^2+e/2=0,\\
&\ell_s=A(2B+A_1p+B_1)+bp-\nu^2,\\
&h=B^2+(A_1p+B_1)B+\frac{f_3}6p^3
 +\frac{n_2-\nu f_2}2p^2-(\nu n_1+\ell_t)p+\nu\ell .
\end{aligned}
\tag{7}
\]
Nothing here asserts that the full \(H_P\) vanishes.

## 3. Complete fourth-level ledger and the first scalar split

All fourth-level coefficients can be kept without imposing extra
conditions. Define formal polynomials over \(L\):
\[
\begin{aligned}
L_2(P)&=(f_3/2-2b)P^2+(n_2+2\ell_s-bf_1)P
                              +f_1\ell_s-\ell_t,\\
D_1(P)&=b-ef_1-2eP,\\
F_0(P)&=\frac{f_4}{24}P^4+\frac{n_3-3bf_2}{6}P^3
 +\frac{f_2\ell_s-\ell_{tt}-2bn_1}{2}P^2
 +(b\ell+n_1\ell_s-h_t)P,\\
F_1(P)&=\frac{b_t-ef_2}{2}P^2
 -(\nu b+en_1+\ell_{ts})P+e\ell+\nu\ell_s-h_s,\\
F_2(P)&=\frac{e_tP-\ell_{ss}-2\nu e}{2}.
\end{aligned}
\tag{8}
\]
The genuine polynomial from296 and458 is
\[
Q=\frac{f_2}{2}U^2+\{L_2(P)+D_1(P)V\}U+
 F_0(P)+F_1(P)V+F_2(P)V^2+\frac{e_s}{6}V^3.
\tag{9}
\]
It satisfies \(Q(y,p,V)=q_0\in L\). Its entire evaluated coefficient
ledger is therefore
\[
\begin{aligned}
&[V^3]Q=e_s/6=0,\\
&[V^2]Q=f_2A^2/2+D_1(p)A+F_2(p)=0,\\
&[V]Q=f_2AB+L_2(p)A+D_1(p)B+F_1(p)=0,\\
&[1]Q=f_2B^2/2+L_2(p)B+F_0(p)=q_0.
\end{aligned}
\tag{10}
\]
In particular both actual derivatives \(h_t,h_s\) are retained.
These identities are necessary conditions, not a sufficiency claim
for realizing an actual chart.

The exclusion below needs only the third level and the full scalar,
and obtains \(A_s=0\) directly before using any fourth-level equation.
The vector of \(V\)-coefficients in the three literal rows is
\[
\mathcal V=(A,\ 2tA+1,\ X-(2p+f_1)A-\nu).
\tag{11}
\]
Thus the \(V^2\) coefficient of \(J\) is
\(\det(\mathcal V_t,\mathcal V_s,\mathcal V)\).
Using \(e=-2A^2\), with \(A_s\) still arbitrary, gives
\[
[XV^2]J=-2AA_s .
\tag{12}
\]
Since \(A\ne0\) and (6) is a scalar, \(A_s=0\). Consequently
\(e_s=0\), in agreement with (10), and exact subtraction gives
\[
A,e\in F,\qquad n=\frac e2s^2+\nu_0s+n_0,\qquad
\nu_0,n_0\in F .
\tag{13}
\]
For example \(\nu_0=n_s-es\) has zero \(s\)-derivative, as does
the remainder defining \(n_0\). This is not a rational ansatz.

Here is the complete Jacobian matrix after \(A_s=0\). Its rows are
\(Y,Z,W\), its columns \(t,s,V\), and \(y=AV+B\):
\[
\begin{pmatrix}
 A_tV+B_t+p_tX+X^2 & B_s+p_sX & A\\
 2y+2t(A_tV+B_t)+(2p+f_1)p_t+f_2p+n_1
 +(2p+2tp_t+f_1)X+2tX^2
 &2tB_s+(2p+f_1)p_s+\nu+(2tp_s+1)X&2tA+1\\
 \ell_t-(2p_t+f_2)y-(2p+f_1)(A_tV+B_t)
 -f_3p^2/2-f_2pp_t-n_2p-n_1p_t-bV
 &\ell_s-2p_sy-(2p+f_1)B_s-f_2pp_s-bp-n_1p_s-eV+X^2
 &X-(2p+f_1)A-\nu
\end{pmatrix}.
\tag{14}
\]
In particular this is not a determinant of intercept rows alone.
Its necessary coefficients are
\[
\begin{aligned}
[X^2]J&=A(2B+A_1p+B_1)+bp-\ell_s-\nu^2,\\
[V^2]J&=2A(p_s-A)(A_t-2A^2),\\
[XV]J&=2A\{A^2(2p+f_1)+\nu p_s-B_s\}
                          +(A-p_s)(Af_2+b).
\end{aligned}
\tag{15}
\]
The first is zero by (7). The last two vanish by (6).

## 4. One alternative has proportional columns

Suppose \(p_s=A\), allowing also \(A_t=2A^2\).
Set \(C_p=A(2p+f_1)+\nu\). The last coefficient in (15) forces
\(B_s=AC_p\). Substitute this and the complete second identity in
(7) into (14). The entire \(s\)-column becomes
\[
\begin{pmatrix}Y_s\\Z_s\\W_s\end{pmatrix}
=(X+C_p)
\begin{pmatrix}A\\2tA+1\\X-C_p\end{pmatrix}
=(X+C_p)
\begin{pmatrix}Y_V\\Z_V\\W_V\end{pmatrix}.
\tag{16}
\]
The terms involving \(V\) in \(W_s\) cancel because \(e=-2A^2\).
Its constant term is \(-C_p^2\), by (7).
Thus \(J=0\), contradicting (6). No division by \(b,f_i,C_p\), or
\(A_t-2A^2\) has been made.

We have proved
\[
p_s\ne A,\qquad A_t=2A^2 .
\tag{17}
\]
Since \(A\in F^*\), the element \(t+1/(2A)\) has both coefficient
derivatives zero. The exact joint constants give
\[
A=-\frac1{2(t-\tau)},\qquad e=-\frac1{2(t-\tau)^2},
\qquad \tau\in\mathbb C .
\tag{18}
\]

## 5. Normalize only the complex constant by an actual map

Use the actual complex polynomial automorphism
\[
X_*=X,\quad Y_*=Y-\tau X^2,\quad
Z_*=Z-2\tau Y+\tau^2X^2,\quad W_*=W .
\tag{19}
\]
Its inverse is
\(Y=Y_*+\tau X_*^2\),
\(Z=Z_*+2\tau Y_*+\tau^2X_*^2\), with \(X=X_*,W=W_*\).
Both Jacobians are one, and
\(X_*^2Z_*-Y_*^2=X^2Z-Y^2\).
This is an invertible weighted polynomial change, so it transports
the entire initial kernel, not just one vanishing relation.

The new leading ratios and intercepts are
\[
t_*=t-\tau,\quad s_*=s,\quad
p_*=p,\quad \theta_*=\theta,\quad y_*=y,\quad
z_*=z-2\tau y,\quad w_*=w .
\tag{20}
\]
The ratios \(t-\tau,s\) remain algebraically independent; their
nonzero leading coefficients retain the exact degree frame
\((1,2,2,2)\). The literal \(\partial_{Z_*}\) is exactly
\(\partial_Z\). Hence the selected coefficient \(N=[u^4]\partial_Z|_A\),
the original slice \(u\), \(L\), and \(a_0\) are unchanged.
The whole return is unchanged because \(y,p,\theta\) are unchanged.
The strong return is
\(\mathbb C(y_*,z_*,w_*)=\mathbb C(y,z,w)=\operatorname{Frac}A\),
by the displayed complex linear intercept change.

Moreover \(k_*=s_*+f(t_*+\tau)\), and \(n,\ell\) are the same
coefficient elements expressed in the new parameters. The coefficient
parameter determinant and the actual bad-row determinant are both one,
so (6) is retained. Drop the stars:
\[
A=-1/(2t),\qquad e=-1/(2t^2),\qquad
n=-s^2/(4t^2)+\nu_0s+n_0,\quad \nu_0,n_0,f\in F .
\tag{21}
\]
Here \(t\ne0\) as an element of the coefficient field.
No element of \(F\setminus\mathbb C\) was used as an ambient translation.

## 6. A separating coefficient parameter and the exact moving scalar

Define
\[
\xi=2tp+s+f,\qquad
\beta=\nu_0+\frac{f-tf_1}{2t^2}\in F,\qquad
z=2tB+p^2+f_1p+n\in L .
\tag{22}
\]
By (17),
\(\xi_s=2tp_s+1=2t(p_s-A)\ne0\).
Thus \(t,\xi\) are algebraically independent and form a separating
transcendence basis; \(L\) is finite over \(\mathbb C(t,\xi)\).
The new exact partials are
\[
\partial_\xi=\xi_s^{-1}\partial_s,\qquad
\partial_t\big|_\xi=
\partial_t\big|_s-\frac{\xi_t|_s}{\xi_s}\partial_s .
\tag{23}
\]
They commute. The kernel of \(\partial_\xi\) is still \(F\), and
the new \(t\)-derivative restricts to the original derivative on \(F\).
Joint constants are still \(\mathbb C\). We do not assert
\(L=F(\xi)\), nor that \(\xi\) is an original polynomial coordinate.

Using actual \(Y\) as a further field parameter at fixed actual \(X\),
the exact rows (3) become
\[
Z=z+\xi X+t^2X^2,\qquad
W=(C_Y-2tX)Y+I(t,\xi,X),
\qquad C_Y=-\xi/t+2t\beta ,
\tag{24}
\]
where the entire lower expression is
\[
I=\ell-\frac{f_2}2p^2-n_1p-2t\nu B+2tBX+sX^2
            -(C_Y-2tX)(pX+tX^2)\in L[X].
\tag{25}
\]
Indeed \(V=-2t(y-B)\), \(y=Y-pX-tX^2\), and
\(-(2p+f_1)+2t\nu=C_Y\). This proves (24),(25) without imposing
any unrecorded condition on \(B,\ell,p\).

The determinant of the parameter change
\((t,s,V)\mapsto(t,\xi,Y)\), with \(X\) fixed, is
\(\xi_sY_V=\xi_sA\ne0\), regardless of the moving lower terms.
The complete calibration is therefore
\[
J_{\rm new}:=J_{t,\xi,Y}(X)
       =-\frac{a_0^4}{\rho\,\xi_s A}\in L^* .
\tag{26}
\]
In particular it has no \(X\) or \(Y\) dependence. The factor is
\(\rho=N\theta\), not \(N\sigma\), which is zero in this branch.

All \(t\)-derivatives in the remainder of the proof hold \(\xi\)
fixed. Put \(D=(C_Y)_t=\xi/t^2+2\beta+2t\beta'\).
The full Jacobian matrix of (24) is
\[
\begin{pmatrix}
0&0&1\\
z_t+2tX^2&z_\xi+X&0\\
(D-2X)Y+I_t&-Y/t+I_\xi&C_Y-2tX
\end{pmatrix}.
\]
Thus its entire determinant is
\[
J_{\rm new}
=(z_t+2tX^2)I_\xi-(z_\xi+X)I_t
 +Y\{(2z_\xi-D)X-Dz_\xi-z_t/t\}.
\tag{27}
\]
All lower scalar conditions remain present in the first two terms.
We use only the necessary vanishing of the \(Y\)-coefficient.
The elements \(X,Y\) are algebraically independent over \(L\):
\(X,V\) are independent, and \(Y=AV+B+pX+tX^2\) with \(A\ne0\).
Consequently (26),(27) imply
\[
z_\xi=\frac{\xi}{2t^2}+\beta+t\beta',
\qquad z_t=-2t z_\xi^2 .
\tag{28}
\]

## 7. Exact integration forces an impossible original-coordinate square

Put \(C_1=\beta+t\beta'\in F\). The first equation in (28) gives
by exact subtraction
\[
z=\frac{\xi^2}{4t^2}+C_1\xi+Z_0,\qquad Z_0\in F.
\tag{29}
\]
The element \(\xi\) is transcendental over \(F\), since \(F\) is
finite over \(\mathbb C(t)\) and \(t,\xi\) are algebraically independent.
Substitute (29) into the second equation of (28) and compare its
polynomial coefficients in \(\xi\):
\[
C_1'=-2C_1/t,\qquad Z_0'=-2tC_1^2 .
\tag{30}
\]
Since the derivative constants of \(F\) are \(\mathbb C\),
\(t^2C_1\) is complex. Write \(C_1=-b_2/t^2\), with
\(b_2\in\mathbb C\). As \((t\beta)'=C_1\), exact subtraction again
gives
\[
\beta=b_1/t+b_2/t^2,\qquad
Z_0=b_2^2/t^2+z_0,\qquad b_1,b_2,z_0\in\mathbb C,
\qquad
z=\frac{(\xi-2b_2)^2}{4t^2}+z_0.
\tag{31}
\]
No rational-function ansatz was used. Neither \(C_1\), \(\beta\),
nor \(b_2\) was divided by, so their zero cases are included.

Combining (24) and (31) yields in \(\operatorname{Frac}\mathcal B\)
\[
\boxed{
Z-2b_2X-z_0=
\left(tX+\frac{\xi-2b_2}{2t}\right)^2 .}
\tag{32}
\]
The element on the left is an irreducible coordinate polynomial of
the actual UFD \(\mathbb C[X,Y,Z,W]\), since \(b_2,z_0\) are complex.
Its valuation at its own prime factor is one. Every square in the
fraction field has even valuation there, contradicting (32).
The putative square root was never declared an original coordinate;
the contradiction occurs in the fraction field itself.

This proves the bounded exclusion
\[
\boxed{\text{full actual264},\quad k=s+f,\ f_s=0,\ n_{ss}\ne0
                 \quad\Longrightarrow\quad \sigma\notin L.}
\tag{33}
\]
There is no hypothesis on \(f'''\). The conclusion excludes this
constant-sigma branch only; it does not recognize or exclude every
nonlinear-first-potential chart.

## 8. Dependencies, verification, and retained boundaries

The complete366 source was freshly read. We retain its conic descent,
the actual complex-\(\tau\) normalization, and the final prime-valuation
principle, but rederive every intervening row and scalar with arbitrary
\(f\). The essential changes are the full \(f_i\) terms in (3),(7)--(16),
the separating parameter \(\xi=2tp+s+f\), and the adjusted
\(\beta=\nu_0+(f-tf_1)/(2t^2)\). The strict-degree Riccati statement
of460 is not used. In particular its nonconstant-sigma hypotheses
are not imported into this boundary case.

The complete458 source was also freshly read, including the arbitrary
potential formulas before its additional projection assumptions.
The full264/296 actual inputs remain dependencies. No surface-gradient
unit statement is applied after slicing \(P=p\), and no formal solution
of the displayed necessary equations is asserted to realize the chart.

Fresh unsaved6730a7 reconstructed the complete matrix (14) and its
coefficients (15). Fresh9743f4 checked the full evaluated H/Q ledger,
all three proportional-column identities, the entire row (25), the
full new determinant (27), and the square identity (32), with zero
residuals. Freshb0fc75 kept \(A_s\) arbitrary and verified (12), the
remaining \(V^2\) factor, both actual normalization inverse identities,
the full initial relation, the exact integrations, and (32). These
algebraic controls supplement the written field and UFD arguments;
they are not numerical sampling or substitutes for those arguments.

No saved checker was executed, imported, compiled, or rerun. No earlier
source or canonical index was edited. No unrestricted cancellation,
historical novelty, external expert review, or formal certification
is claimed.

