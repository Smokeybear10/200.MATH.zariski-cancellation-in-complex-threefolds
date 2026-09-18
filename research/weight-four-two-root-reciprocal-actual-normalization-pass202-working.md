# Actual lower-potential normalization for the two reciprocal two-root families

Status: bounded working normalization lemma. In the supplied actual
two-root square-completion configuration, the two necessary families
\(f=cq/t\) and \(f=cq/(t-1)\) admit the same actual lower-potential
normal form. The proof solves a linear differential system inside
the exact finite field and realizes its modes by polynomial coordinate
changes. It does not recognize or exclude the resulting alternatives.

## 1. Actual input and the symmetry between the two families

Retain the actual chart and nondegenerate square alternatives from
[universal184](weight-four-universal-chart-potentials-pass184-working.md),
[double-cover reduction195](weight-four-double-cover-nonzero-r-reduction-pass195-working.md)
and [classification201](weight-four-two-root-two-gate-classification-pass201-working.md).
In particular, assume
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=\mathcal A[u],\quad E=\partial_u,\quad
\deg_E(X,Y,Z,W)=(1,1,2,2),\\
\ker\theta_0=(\mathsf Z^2-\mathsf X^2\mathsf Y(\mathsf X-\mathsf Y)),
\qquad q^2=t(1-t),\\
L=\operatorname{Frac}(\ker_{\mathcal A}N),\quad
\mathcal A_L=L[v],\quad Nv=1,\quad
K=\ker_L\partial_\rho,\quad [K:\mathbb C(t,q)]<\infty,\\
f=1/R=cq/t\quad\hbox{or}\quad cq/(t-1),\qquad c\in\mathbb C^* .
\end{gathered}
\tag{1}
\]
The initial kernel is the entire ideal, not one leading relation.
The selected derivation is \(N=[u^3](\partial_Z|_{\mathcal A})\).
All full-line, calibrated scalar-Jacobian and exact field-return
conditions are retained. No original coordinate equal to \(q\) is assumed.

The actual involution
\[
X_*=X,\qquad Y_*=X-Y,\qquad Z_*=Z,\qquad W_*=W
\tag{2}
\]
has the same formula as inverse. It sends
\(t_*=1-t,\ q_*=q,\ y_*=-y,\ \rho_* =\rho\), and leaves
\(\vartheta,k,n\) unchanged as coefficient elements in the reexpressed
field. For example \((q_*)_{t_*}y_*=q_ty\), while the second
derivative of \(q\) is unchanged and \(k_{t_*}y_*=k_ty\).
Thus the actual first and second potentials are preserved.
It carries \(cq/(t-1)\) to \(-cq_*/t_*\).
Write the resulting nonzero complex constant again as \(c\).
After this optional involution, the actual change \(W_*=W/c\)
reduces the remaining \(f=cq/t\) to \(f_*=q/t\), since
\(\rho_* =\rho/c\), \(R_*=cR\). Its inverse is \(W=cW_*\).
Both changes leave the selected partial \(\partial_Z\) literally unchanged.

Drop the stars and put
\[
\begin{gathered}
r=t/q,\qquad t=\frac{r^2}{1+r^2},\qquad q=\frac r{1+r^2},\qquad
\omega=1+r^2,\qquad
\partial_t=\frac{\omega^2}{2r}\partial_r,\\
R=r,\qquad \nu=n_{\rho\rho}=-r\omega,\qquad
\Delta=RR_{tt}/2-R_t^2=\frac{(r^2-3)\omega^3}{8r^2},\\
p_2=-\frac{\Delta}{R\nu}=\frac{(r^2-3)\omega^2}{8r^4},\qquad
k=R\rho+k_0,\qquad n=\nu\rho^2/2+s_0\rho+n_0 .
\end{gathered}
\tag{3}
\]
Here \(k_0,s_0,n_0\in K\). The exact field is finite over
\(\mathbb C(r)\), but need not equal it. The constants of its
\(r\)-derivative are \(\mathbb C\). The element \(r\) is transcendental,
so every displayed nonzero polynomial denominator is a nonzero field
element. None is asserted to be a unit of the original ring.

For a direct check from the general formulas195, if
\(d=q_{ttt}/6\) and \(D=d_t f/4+df_t\), then
\[
d=-\frac{(r^2-1)\omega^4}{16r^5},\qquad
D=-\frac{(r^2-3)^2\omega^5}{128r^8},\qquad
\nu=\frac{f_{tt}^2}{8f^3D}=-r\omega .
\tag{4}
\]

## 2. Raw coefficient comparisons give a linear six-state system

For independent \(U,V\), write the literal coefficient polynomials
\[
\begin{aligned}
S&=dU^3+k_{tt}U^2/2+R_tUV+n_tU+n_\rho V,\\
T&=q_{tttt}U^4/24+k_{ttt}U^3/6+R_{tt}U^2V/2
                  +n_{tt}U^2/2+n_{t\rho}UV+\nu V^2/2,\\
\mathcal H&=R(T-\ell_tU-\ell_\rho V-m)
                        +(R_tU+n_\rho)(\ell-S).
\end{aligned}
\tag{5}
\]
The actual square alternatives have
\(\mathcal H=(R\nu/2)(V-P(U))^2+B_1U+B_0\), with
\(P=p_2U^2+p_1U+p_0\). The
[general scalar-Jacobian gate193](weight-four-split-square-candidate-jacobian-obstruction-pass193-working.md)
gives \((B_1)_\rho=0\) in either alternative, including the graph
\(B_1=0\). The exact lower coefficient formulas are
\[
\begin{gathered}
\mathcal B=Rn_{t\rho}-2R_tn_\rho,\qquad
\mathcal C_2=Rn_{tt}/2-R_tn_t-n_\rho k_{tt}/2,\\
\ell_\rho=\frac{\mathcal B^2}{2\Delta R}
       -\frac{\nu\mathcal C_2}{\Delta}-\frac{n_\rho^2}{R},\qquad
\mathcal C=-R\ell_\rho-n_\rho^2,\\
B_1=-R\ell_t+R_t\ell-n_\rho n_t-\frac{\mathcal B\mathcal C}{R\nu}.
\end{gathered}
\tag{6}
\]
Since the right side for \(\ell_\rho\) is polynomial in \(\rho\)
of degree at most two, explicit primitive subtraction gives
\(\ell\in K[\rho]\) of degree at most three. This remains true
when \(L/K(\rho)\) is initially a proper finite extension.

In the remainder of the calculation a prime denotes \(\partial_r\),
not \(\partial_t\). Define the two linear expressions
\[
\begin{aligned}
\mathscr U(k_0,s_0)={}&r^3\omega^2k_0'''
 +6r^2(r^2-1)\omega k_0''+6r(r^2-1)^2k_0'\\
 &+3r(r^2-3)s_0'+3(5-r^2)s_0,\\
\mathscr V(k_0,s_0)={}&r^2(r^2-3)s_0'''-6rs_0''+6s_0'\\
 &+r^2(r^2-3)\omega k_0'''
   +6r(r^4-4r^2-1)k_0''+6(r^4-6r^2+1)k_0'.
\end{aligned}
\tag{7}
\]
Literal substitution of (3) into (5)--(6) gives
\[
\begin{gathered}
[U^3V^0]\left\{\mathcal H-\frac{R\nu}{2}(V-P)^2\right\}
   =\frac{\omega^4}{48r^5}\mathscr U(k_0,s_0),\\
[\rho^3]B_1=0,\qquad
[\rho^2]B_1=-\frac{\omega^4}{4(r^2-3)^2}\mathscr V(k_0,s_0).
\end{gathered}
\tag{8}
\]
These identities are taken before evaluating \(U,V\).
The first expression before substitution is
\(Rk_{ttt}/6-R_tk_{tt}/2-dn_\rho-\Delta\mathcal B/(R\nu)\).
Its positive \(\rho\)-coefficient cancels.
For independently reconstructing the second identity, write
\(\mathcal B=b_1\rho+b_0\), \(\mathcal C_2=c_2\rho^2+c_1\rho+c_0\).
Then
\[
\begin{gathered}
b_1=R\nu_t-2R_t\nu,\quad b_0=R(s_0)_t-2R_ts_0,\\
c_2=R\nu_{tt}/4-R_t\nu_t/2-\nu R_{tt}/2,\\
c_1=R(s_0)_{tt}/2-R_t(s_0)_t-(\nu(k_0)_{tt}+s_0R_{tt})/2,\\
[\rho^2]\ell_\rho=b_1^2/(2\Delta R)-\nu c_2/\Delta-\nu^2/R,\\
[\rho]\ell_\rho=b_1b_0/(\Delta R)-\nu c_1/\Delta-2\nu s_0/R.
\end{gathered}
\tag{9}
\]
Substitute these two entries into (6). Neither \(n_0\), \(\ell_0\)
nor \(m\) can change the coefficient in (8).
Thus every actual branch here satisfies \(\mathscr U=\mathscr V=0\).

## 3. Complete solution inside the exact finite field

The following six pairs solve both equations (7):
\[
(1,0),\quad(t,0),\quad(R,\nu),\quad(Rt,\nu t),\quad
(Rt^2,\nu t^2),\quad(r^{-1},\omega/r).
\tag{10}
\]
These are identities obtained by differentiation, not numerical fits.
Form the six-by-six matrix whose columns are their state vectors
\((k_0,k_0',k_0'',s_0,s_0',s_0'')^T\). Its determinant is
\[
-\frac{64r^4(r^2-3)}{\omega^6}\ne0.
\tag{11}
\]
For completeness, (7) solves first for \(k_0'''\), since
\(r^3\omega^2\ne0\), and then for \(s_0'''\), since
\(r^2(r^2-3)\ne0\). It therefore gives a homogeneous first-order
system on the six state entries, with coefficients in \(\mathbb C(r)\).
Every solution state in \(K^6\) is a linear combination of the six
columns using coefficients in \(K\), by (11). Differentiate that
coefficient vector and use the common first-order system. Its derivative
is zero, so every coefficient is complex. This proves completeness over
the exact field, not just among rational functions.

The final pair can be replaced by an actual-translation pair:
\[
q_t=\frac{1-r^2}{2r},\qquad R_t=\frac{\omega^2}{2r},\qquad
2(q_t,R_t)=(r^{-1},\omega/r)-(R,\nu).
\]
Consequently the complete solution may be written
\[
\begin{gathered}
k_0=\kappa_0+\kappa_1t+RP(t)+\lambda q_t,\qquad
s_0=\nu P(t)+\lambda R_t,\\
P(t)=p_0+p_1t+p_2^*t^2,\qquad
\kappa_0,\kappa_1,\lambda,p_0,p_1,p_2^*\in\mathbb C.
\end{gathered}
\tag{12}
\]

## 4. Actual coordinate changes remove k0 and s0

First translate only the original \(Y\) coordinate:
\[
X_1=X,\quad Y_1=Y+\lambda,\quad Z_1=Z,\quad W_1=W.
\tag{13}
\]
The inverse subtracts \(\lambda\). The coefficient change is
\(y_1=y+\lambda\), with \(t,q,\rho,\vartheta,z,w\) unchanged.
The first potential gives \((k_0)_1=k_0-\lambda q_t\).
Writing \(Q=q_{tt}/2=-\omega^3/(8r^3)\), the second gives
\[
(s_0)_1=s_0-\lambda R_t,\qquad
(n_0)_1=n_0-\lambda(k_0)_t+\lambda^2Q.
\tag{14}
\]
Indeed insert \(y=y_1-\lambda\) into
\(z=Qy^2+(R_t\rho+(k_0)_t)y+R\vartheta+n\).
Both formulas include the fixed-coefficient derivative change; this
is an original polynomial translation, not a free change of a potential.

Next set \(P_2(X_1,Y_1)=p_0X_1^2+p_1X_1Y_1+p_2^*Y_1^2\) and make
\[
X_2=X_1,\quad Y_2=Y_1,\quad
Z_2=Z_1-\kappa_0X_1-\kappa_1Y_1,\quad
W_2=W_1+P_2(X_1,Y_1).
\tag{15}
\]
The inverse adds the same linear polynomial to \(Z_2\) and subtracts
the displayed quadratic from \(W_2\), with unchanged \(X_2,Y_2\).
Both inverse orders cancel literally.
Here \(\rho_2=\rho+P(t)\), \(\vartheta_2=\vartheta+P_t(t)y_1\),
\(z_2=z-\kappa_1y_1\) and \(w_2=w+p_2^*y_1^2\).
The new first potential is \(k_2=R\rho_2\). The second is
\(n_2=n_1(\rho_2-P(t))\), because
\(((k_0)_1-RP)_t-\kappa_1=0\).
Its linear \(\rho_2\)-coefficient vanishes by (12)--(14).
Drop the subscripts: now \(k=R\rho\) and
\(n=\nu\rho^2/2+n_0\), with \(n_0\in K\).

## 5. The last lower coefficient has three removable modes

Reapply the actual coefficient gate (6) after (15). It becomes
\[
[\rho]B_1=-\frac{r\omega^3}{2(r^2-3)^2}
 \left\{r(r^2-3)\omega n_0'''
                    +3(r^4-6r^2+1)n_0''\right\}=0.
\tag{16}
\]
The functions \(1,r,rt\) solve the bracketed equation, with ordinary
three-by-three derivative Wronskian
\(-2r(r^2-3)/\omega^3\ne0\). Its highest coefficient is nonzero.
The same state-vector argument as in Section3 proves completeness:
\[
n_0=N_0+R(N_1+N_2t),\qquad N_0,N_1,N_2\in\mathbb C.
\tag{17}
\]
Thus make one more actual triangular change
\[
X_3=X_2,\quad Y_3=Y_2,\quad
Z_3=Z_2-N_0,\qquad W_3=W_2+N_1X_2+N_2Y_2.
\tag{18}
\]
Its inverse uses the opposite additions. It changes \(\vartheta\)
by \(N_1+N_2t\), so it subtracts precisely
\(N_0+R(N_1+N_2t)\) from the second potential.
The canonical lower-potential conclusion is therefore
\[
\boxed{\quad k=r\rho,\qquad
n=-\frac{r(1+r^2)}2\rho^2.\quad}
\tag{19}
\]

## 6. Remaining scalar and preservation of every actual input

Formula (6) in the final coordinates gives
\[
\ell=-\frac{r(1+r^2)^2}{2}\rho^3+\ell_0,\qquad
\ell_0\in K,\qquad B_1=-R(\ell_0)_t+R_t\ell_0.
\tag{20}
\]
Only in the graph alternative \(B_1=0\) does this imply
\(\ell_0=C R\) for \(C\in\mathbb C\). The actual constant translation
\(W\mapsto W-C\), with opposite translation as inverse, then subtracts
\(CR\) from the third potential. The quadratic-projection alternative
retains unrestricted \(\ell_0\); no graph-only normalization is used there.

Every original map has complex polynomial coefficients and an explicit
polynomial inverse. Each inverse keeps old \(X,Y,W\) independent of
new \(Z\), with old \(Z=\) new \(Z+\) a polynomial in new \(X,Y\).
Thus the selected partial \(\partial_Z\), and consequently \(N\),
its exact field \(L\) and the full generic line, are literally preserved.
The \(\rho\)-changes are nonzero complex scalings or additions of
polynomials in \(t\); hence the exact field \(K\) is preserved too.
The optional involution changes \(t\) to \(1-t\), not the field itself.
The generic \(y\) changes by a sign and translations in \(L\).
The generic \(\vartheta\) changes by a nonzero complex scaling and an
affine polynomial in \(y\), with coefficients in \(L\).
Both generic square alternatives are therefore preserved.

The involution preserves the entire binary leading relation, and the
remaining changes preserve the leading \(X,Y,Z\) slots. Only the absent
\(W\) slot is scaled or shifted by a binary quadratic. Its time-leading
coefficient stays nonzero because \(\rho\) is independent of \(t\).
Likewise \(1-t\ne0\), so the involution does not lower the degree of \(Y\).
These are invertible filtered changes of the polynomial coordinate ring;
they preserve exact1122 and the whole initial kernel, not merely a relation.
The original slice \(u\) and derivation \(E\) are unchanged.

This result solves the lower-potential normalization for the two
reciprocal two-root families. It does not solve the remaining scalar
Jacobian, exact projected field return or original-coordinate problem
after (19)--(20). It neither proves actual realization nor excludes either
square alternative, and it does not settle the separate \(f=cq\) family,
arbitrary coordinate entry or unrestricted cancellation.
New inline rational arithmetic checked the displayed identities and
Wronskians. No saved checker was executed, imported or compiled; no201
or earlier artifact was edited. This is not expert certification,
proof-assistant verification or a novelty claim.
