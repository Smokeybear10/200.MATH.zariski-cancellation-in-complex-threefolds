# Actual lower-potential normalization for the two-root family f=cq

Status: bounded working normalization theorem, pending independent
saved-source review. For the supplied actual two-root initial kernel
and the coefficient family \(f=cq\), every lower term in \(k,n\)
can be removed by the actual polynomial maps below. The result retains
the unrestricted constant term of the third potential in the projection
branch. It is not a recognition or exclusion of either alternative.

## 1. Actual input and the coefficient parameter

Retain the actual chart and square-completion alternatives of
[universal184](weight-four-universal-chart-potentials-pass184-working.md),
[double-cover reduction195](weight-four-double-cover-nonzero-r-reduction-pass195-working.md)
and [two-gate classification201](weight-four-two-root-two-gate-classification-pass201-working.md).
Thus
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=\mathcal A[u],\qquad E=\partial_u,\qquad
\deg_E(X,Y,Z,W)=(1,1,2,2),\\
\ker\theta_0=(\mathsf Z^2-\mathsf X^2\mathsf Y(\mathsf X-\mathsf Y)),
\qquad q^2=t(1-t),\qquad f=1/R=cq,\quad c\in\mathbb C^*,\\
N=[u^3](\partial_Z|_{\mathcal A})\ne0,\quad
L=\operatorname{Frac}(\ker_{\mathcal A}N),\quad
\mathcal A_L=L[v],\ Nv=1,\quad
K=\ker_L\partial_\rho,\quad [K:\mathbb C(t)]<\infty .
\end{gathered}
\tag{1}
\]
The initial ideal is the entire kernel, not one necessary relation.
The original four entries are polynomial coordinates and the global
slice is actual. The exact constants of \(K\) are \(\mathbb C\).
The full generic line, projected field return and calibrated scalar
Jacobian are retained; they are not deduced from the formulas below.

The chart, with coefficient derivatives before evaluation, is
\[
Y=y+tX,\quad Z=z+(q_ty+k)X+qX^2,\quad
W=w+\vartheta X+\rho X^2,\qquad
z=\frac{q_{tt}}2y^2+k_ty+R\vartheta+n .
\tag{2}
\]
First make the actual change \(W_*=W/c\), fixing \(X,Y,Z\).
Its inverse is \(W=cW_*\). It has
\(\rho_*=\rho/c,\ \vartheta_*=\vartheta/c,\ k_*=k,\ R_*=cR\),
and hence \(f_*=q\). For \(f=cq\), the coefficient formula201 gives
\(n_{\rho\rho}=-1/(c^2q^3)\), so the new value is \(-q^{-3}\).
The original selected partial \(\partial_Z\), \(N\), and their
constant fields do not change.

Drop stars and put
\[
\begin{gathered}
r=t/q,\qquad t=\frac{r^2}{1+r^2},\qquad
q=\frac r{1+r^2},\qquad \Omega=1+r^2,\\
\partial_t=\frac{\Omega^2}{2r}\partial_r,\qquad
R=\frac1q,\quad \nu=n_{\rho\rho}=-\frac1{q^3},\\
k=R\rho+k_0,\qquad
n=\frac{\nu}{2}\rho^2+s_0\rho+n_0,\qquad k_0,s_0,n_0\in K .
\end{gathered}
\tag{3}
\]
Only \(\mathbb C(t,q)=\mathbb C(r)\) is proved rational here.
The ambient \(K\) can remain a proper finite extension of this field.
All divisions are by nonzero coefficient-field elements, not units
asserted in the original ring.

## 2. Raw coefficient identities

A subscript \(t\) always means the coefficient derivative holding
\(\rho\) fixed. In this section write \(k_i=\partial_r^ik_0\) and
\(s_i=\partial_r^is_0\). The symbol \(\Omega\) is not a polynomial
coordinate. For independent \(U,V\), set
\[
\begin{aligned}
S&=dU^3+\frac{k_{tt}}2U^2+R_tUV+n_tU+n_\rho V,\\
T&=e_4U^4+\frac{k_{ttt}}6U^3+\frac{R_{tt}}2U^2V
       +\frac{n_{tt}}2U^2+n_{t\rho}UV+\frac{\nu}{2}V^2,\\
\mathcal H&=R(T-\ell_tU-\ell_\rho V-m)
                   +(R_tU+n_\rho)(\ell-S),\\
d&=q_{ttt}/6=\frac{1-2t}{16q^5},\qquad e_4=d_t/4,\qquad
\Delta=\frac{RR_{tt}}2-R_t^2=\frac1{8q^6}.
\end{aligned}
\tag{4}
\]
The actual alternatives have
\(\mathcal H=A_2(V-P(U))^2+B_1U+B_0\), where
\(A_2=R\nu/2\) and \(P\) has nonzero quadratic coefficient.
The actual square-Jacobian gate of
[square-Jacobian193](weight-four-split-square-candidate-jacobian-obstruction-pass193-working.md)
gives \((B_1)_\rho=0\), including \(B_1=0\) in the graph case.

For explicit extraction define
\[
\begin{gathered}
\mathcal B=Rn_{t\rho}-2R_tn_\rho,\qquad
\mathcal C_2=Rn_{tt}/2-R_tn_t-n_\rho k_{tt}/2,\qquad
\mathcal C=-R\ell_\rho-n_\rho^2,\\
\ell_\rho=\frac{\mathcal B^2}{2\Delta R}
           -\frac{\nu\mathcal C_2}{\Delta}-\frac{n_\rho^2}{R},
\qquad
B_1=-R\ell_t+R_t\ell-n_\rho n_t
                         -\frac{\mathcal B\mathcal C}{R\nu}.
\end{gathered}
\tag{5}
\]
The displayed expression for \(\ell_\rho\) in (5) has
\(\rho\)-degree at most two.
Subtracting its explicit polynomial primitive gives
\(\ell\in K[\rho]\), of degree at most three, with arbitrary constant
term in \(K\). This uses \(\ker_L\partial_\rho=K\), not \(L=K(\rho)\).

The constant-in-\(\rho\) residual of the \(U^3V^0\) coefficient
after square completion is
\[
\mathcal U=
\frac{\Omega^4}{48r^5}
 \{r\Omega^3 k_3+6r^2\Omega^2 k_2+6r\Omega^2 k_1
                     +3r\Omega s_1+3(1-r^2)s_0\}=0 .
\tag{6}
\]
Its positive-\(\rho\) coefficient vanishes identically.
The coefficients of \(B_1\) satisfy
\[
\begin{aligned}
[\rho^3]B_1&=0,\\
[\rho^2]B_1&=-\frac{\Omega^2}{4r^4}
 \{\Omega^5 k_3+6r\Omega^4 k_2+6\Omega^4 k_1
       +r^2\Omega^3 s_3+6r\Omega^2 s_2\\
 &\hspace{39mm}-6\Omega(3r^2-1)s_1+24r(r^2-1)s_0\}=0 .
\end{aligned}
\tag{7}
\]
These are coefficient identities from (4)--(5). Neither \(n_0\),
\(m\), nor the constant term of \(\ell\) can alter them.

One way to check (6)--(7) without expanded eliminants is to write
\(\mathcal B=b_1\rho+b_0\) and
\(\mathcal C_2=c_2\rho^2+c_1\rho+c_0\), where
\[
\begin{gathered}
b_1=R\nu_t-2R_t\nu,\quad b_0=R(s_0)_t-2R_ts_0,\\
c_2=R\nu_{tt}/4-R_t\nu_t/2-\nu R_{tt}/2,\\
c_1=R(s_0)_{tt}/2-R_t(s_0)_t
                     -(\nu(k_0)_{tt}+s_0R_{tt})/2,\\
c_0=R(n_0)_{tt}/2-R_t(n_0)_t-s_0(k_0)_{tt}/2.
\end{gathered}
\]
Then, if \(\ell_\rho=a_2\rho^2+a_1\rho+a_0\), (5) gives
\(a_2=b_1^2/(2\Delta R)-\nu c_2/\Delta-\nu^2/R\),
\(a_1=b_1b_0/(\Delta R)-\nu c_1/\Delta-2\nu s_0/R\), and
\(a_0=b_0^2/(2\Delta R)-\nu c_0/\Delta-s_0^2/R\).
Insert \([\rho^3]\ell=a_2/3,\ [\rho^2]\ell=a_1/2\) in (5).
The unspecialized residual for (6) is
\(Rk_{ttt}/6-R_tk_{tt}/2-dn_\rho-\Delta\mathcal B/(R\nu)\).
These give a direct reconstruction of every derivative and sign.

## 3. Fifth-order equation and completeness over the exact field

Equation (6) solves for \(s_1\):
\[
s_1=\frac{r^2-1}{r\Omega}s_0
 -\frac{\Omega^2k_3+6r\Omega k_2+6\Omega k_1}{3}.
\tag{8}
\]
Differentiate (8) twice, substitute the resulting \(s_1,s_2,s_3\)
into (7), and collect. The exact result is
\[
[\rho^2]B_1=\frac{\Omega^6}{12r^3}\mathscr L_5(k_0),\qquad
\mathscr L_5(h)=r(r^2+1)h^{(5)}
       +5(3r^2+1)h^{(4)}+60rh^{(3)}+60h'' .
\tag{9}
\]
The derivatives in (9) are \(r\)-derivatives. No differentiation of
an evaluated generic-line variable is used.

The five rational functions
\[
1,\quad t,\quad R,\quad tR,\quad t^2R
\tag{10}
\]
solve \(\mathscr L_5(h)=0\). In this order their Wronskian is
\[
\det\bigl(\partial_r^i h_j\bigr)_{0\le i,j\le4}
=-\frac{288}{r^5(1+r^2)^5}\ne0 .
\tag{11}
\]
This proves completeness in \(K\), not just linear independence among
rational trials. Indeed, for any solution \(h\in K\), use the invertible
matrix in (11) to express \((h,h',\ldots,h^{(4)})\) in its five
solution columns, with coefficients in \(K\). Differentiating the
first four rows and using the fifth-order equation in the last row
shows that the vector of coefficient derivatives is zero. All five
coefficients are therefore complex. Consequently
\[
k_0=\kappa_0+\kappa_1t+R(p_0+p_1t+p_2t^2),
\qquad \kappa_0,\kappa_1,p_0,p_1,p_2\in\mathbb C .
\tag{12}
\]

## 4. First actual shear and the last lower differential equation

Put \(P(t)=p_0+p_1t+p_2t^2\) and
\(P_2(X,Y)=p_0X^2+p_1XY+p_2Y^2\).
Make the actual change
\[
X_1=X,\quad Y_1=Y,\quad
Z_1=Z-\kappa_0X-\kappa_1Y,\quad W_1=W+P_2(X,Y).
\tag{13}
\]
Its polynomial inverse adds the same linear term to \(Z_1\) and
subtracts \(P_2(X_1,Y_1)\) from \(W_1\). Both compositions cancel
literally. The exact chart transformation is
\[
\rho_1=\rho+P(t),\quad
\vartheta_1=\vartheta+P_t(t)y,\quad
z_1=z-\kappa_1y,\quad w_1=w+p_2y^2,\quad k_1=R\rho_1 .
\tag{14}
\]
The second potential gives \(n_1=n(t,\rho_1-P(t))\).
Its possible extra \(y\)-coefficient is
\((k_0-RP)_t-\kappa_1=0\); thus (14) includes the
fixed-\(\rho_1\) derivative correction.

Drop subscripts. Reapply (6) with \(k_0=0\).
Since \(R_r/R=(r^2-1)/(r\Omega)\), equation (8) gives
\[
s_0=CR,\qquad C\in\mathbb C .
\tag{15}
\]
The next raw coefficient of (5) now reads
\[
[\rho]B_1=-\frac{\Omega}{2r^3}
 \{\Omega^4(r(n_0)_{rrr}+3(n_0)_{rr})
                         +12C^2r(r^2-1)\}=0 .
\tag{16}
\]
The third-order inhomogeneous equation is solved inside \(K\) by
\[
n_0=-\frac{C^2r(2r^2+3)}{2(1+r^2)}
                      +N_0+N_+r+\frac{N_-}{r},
\qquad N_0,N_+,N_-\in\mathbb C .
\tag{17}
\]
Substitution verifies the displayed particular solution. After its
subtraction, \((r^3h'')'=0\), so \(r^3h''\) is complex.
Subtracting the rational primitive twice gives exactly the three
homogeneous modes in (17). No algebraic primitive has been adjoined
and no rationality of the ambient \(K\) has been assumed.

## 5. Actual X translation removes C

For any \(a\in\mathbb C\), starting from (15)--(17), make
\[
X_*=X+a,\quad Y_*=Y,\quad Z_*=Z,\quad
W_*=W+a\left(Y^2-\frac32X_*Y\right).
\tag{18}
\]
The inverse is
\[
X=X_*-a,\quad Y=Y_*,\quad Z=Z_*,\quad
W=W_*-a\left(Y_*^2-\frac32X_*Y_*\right).
\]
It is polynomial in the new entries and supplies both inverse orders.

Let \(P_a(t)=a(t^2-3t/2)\). Comparing powers of the new \(X_*\)
in the literal chart gives
\[
\begin{gathered}
y_*=y-at,\qquad \rho_*=\rho+P_a(t),\\
\vartheta_*=\vartheta-2a\rho+a(2t-3/2)y_*,\qquad
w_*=w-a\vartheta+a^2\rho+ay_*^2,\\
z_*=z-a(q_ty+R\rho)+a^2q,\qquad k_*=R\rho_* .
\end{gathered}
\tag{19}
\]
In particular
\(a(tq_t-2q)=RP_a(t)\) proves the last equality directly.

Subtracting \(q_{tt}y_*^2/2+(R\rho_*)_t y_*+R\vartheta_*\)
from \(z_*\), using the fixed-new-coefficient partial, yields
\[
n_*=\frac{\nu}{2}\rho_*^2+(C-a)R\rho_*+
 n_0+\frac{Ca r^3+3Ca r+a^2r^3}{2(1+r^2)} .
\tag{20}
\]
This is a literal identity in the independent \(y,\rho,\vartheta\)
slots. Thus it is not a freely chosen coefficient reparametrization.
Choose \(a=C\). The extra constant term in (20) cancels exactly the
particular solution in (17). The result is
\(k_*=R\rho_*,\ s_*=0,\ n_{0,*}=N_0+N_+r+N_-/r\).

Finally \(r=tR\) and \(r^{-1}=(1-t)R\).
The actual change
\[
Z_{**}=Z_*-N_0,\qquad
W_{**}=W_*+N_-X_*+(N_+-N_-)Y_*,
\quad X_{**}=X_*,\quad Y_{**}=Y_*
\tag{21}
\]
removes all three residual modes. Its inverse uses the opposite
constant and linear additions. The second potential verifies
\(n_{**}=n_*-N_0-R\{N_-+(N_+-N_-)t\}=\nu\rho_*^2/2\).

## 6. Remaining potential and preservation of every actual gate

The final normalized conclusion is
\[
\boxed{\quad
k=\frac{\rho}{q},\qquad n=-\frac{\rho^2}{2q^3},\qquad
\ell=-\frac{\rho^3}{2q^5}+\ell_0,\quad \ell_0\in K .
\quad}
\tag{22}
\]
The formula for \(\ell_\rho\) follows by substituting the bare \(k,n\)
in (5), then integrating in \(\rho\). The remaining linear coefficient is
\[
B_1=-R(\ell_0)_t+R_t\ell_0
             =-R^2(\ell_0/R)_t .
\tag{23}
\]
Only in the graph alternative, where \(B_1=0\), does this force
\(\ell_0=C_0R\) with \(C_0\in\mathbb C\).
There the actual translation \(W\mapsto W-C_0\), with the opposite
translation as inverse, removes it. In the projection alternative
\(\ell_0\) remains unrestricted at this stage.

Every displayed map has complex polynomial coefficients and a
polynomial inverse. Each inverse keeps the old \(X,Y,W\) independent
of the new \(Z\), and has old \(Z\) equal to new \(Z\) plus a
polynomial in the new \(X,Y\). Thus the selected original partial
\(\partial_Z\), and consequently \(N,L\), are literally unchanged,
including the initial \(W\)-scaling. The changes in \(\rho\) are a
nonzero constant scaling or addition of a polynomial in \(t\).
They preserve the exact constant field \(K\).

The leading \(X,Y,Z\) slots are unchanged; only the absent \(W\)
slot is scaled or translated by a binary quadratic. Independence
of \(t,\rho\) prevents the new leading \(W\) coefficient from
vanishing. Therefore every map preserves exact1122 and the entire
initial ideal in (1). The generic \(y\) changes only by an
\(L\)-translation, while \(\vartheta\) changes by a nonzero constant
scaling and an affine polynomial in \(y\) over \(L\).
The graph/quadratic-projection distinction persists. These facts
justify reapplying the actual coefficient gates after each stage.

This proof normalizes lower potentials only. It does not prove that
the remaining scalar equations and actual field-return conditions
are satisfied by arbitrary normalized data, or that either
alternative exists, is excluded, or is recognized. It makes no
claim about an original coordinate equal to \(q\), the other two-root
families, arbitrary entry or unrestricted cancellation.

The raw coefficient extraction, exact elimination multiplier,
Wronskian, final lower equation and actual translation were
independently reconstructed in new inline exact arithmetic before
saving this note. No saved checker was executed, imported or
compiled, and no201 or earlier artifact was edited.
This is a bounded working proof, not human expert certification,
proof-assistant verification, public submission or novelty clearance.
