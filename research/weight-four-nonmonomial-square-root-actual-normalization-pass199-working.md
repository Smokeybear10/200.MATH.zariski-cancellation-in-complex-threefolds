# Actual lower-potential normalization for the nonmonomial square-root family

Status: bounded working normalization lemma. In the supplied actual
square-root configuration, the surviving family \(f=at+bq\), with
\(a,b\in\mathbb C^*\) and \(q^2=t\), admits the actual polynomial
normalization below. The result is a canonical lower-potential system,
not recognition or exclusion of either remaining square alternative.
No rationality of the exact coefficient field is assumed.

## 1. Actual hypotheses and the initial constant scaling

Retain the actual chart and square alternatives of
[universal184](weight-four-universal-chart-potentials-pass184-working.md),
[nonzero-R195](weight-four-double-cover-nonzero-r-reduction-pass195-working.md)
and [classification195](weight-four-square-root-two-gate-classification-pass195-working.md).
In particular,
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=\mathcal A[u],\qquad E=\partial_u,\qquad
\deg_E(X,Y,Z,W)=(1,1,2,2),\\
\ker\theta_0=(\mathsf Z^2-\mathsf X^3\mathsf Y),\qquad q^2=t,\\
L=\operatorname{Frac}(\ker_{\mathcal A}N),\qquad
\mathcal A_L=L[v],\qquad Nv=1,\qquad
K=\ker_L\partial_\rho,\\
[K:\mathbb C(q)]<\infty,\qquad \ker_K\partial_q=\mathbb C,\qquad
f=1/R=at+bq,\quad a,b\in\mathbb C^* .
\end{gathered}
\tag{1}
\]
The initial kernel is the entire ideal, not just one relation.
The selected derivation is \(N=[u^3](\partial_Z|_{\mathcal A})\).
The full generic line and calibrated actual scalar Jacobian are
retained. No original polynomial coordinate equal to \(q\) is assumed.

Put \(c=a/b\) and \(e=a^2/b^3\), both nonzero complex numbers.
Make the actual diagonal change
\[
X_*=X,\qquad Y_*=c^2Y,\qquad Z_*=cZ,\qquad W_*=eW .
\tag{2}
\]
Its inverse divides the last three entries by \(c^2,c,e\), respectively.
The actual ratios and potentials transform by
\[
t_*=c^2t,\quad q_*=cq,\quad \rho_*=e\rho,\quad
y_*=c^2y,\quad \vartheta_*=e\vartheta,\quad
k_*=ck,\quad n_*=cn,\quad R_*=\frac ceR .
\]
Consequently
\[
f_*=\frac ec f(q_*/c)=q_*(q_*+1).
\tag{3}
\]
The new selected partial is \(\partial_{Z_*}=c^{-1}\partial_Z\);
thus \(N\) is multiplied by a nonzero complex number, and its constant
field and generic line are unchanged. All later maps below leave that
selected partial literally unchanged.

Drop the stars. The necessary coefficient values from195 become
\[
\begin{gathered}
R=\frac1{q(q+1)},\qquad
\nu=n_{\rho\rho}=\frac1{q^3(q+1)^3(3q-1)},\qquad
\Delta=\frac{RR''}{2}-(R')^2=\frac1{8q^6(q+1)^3},\\
k=R\rho+k_0,\qquad n=\frac{\nu}{2}\rho^2+s_0\rho+n_0,
\qquad k_0,s_0,n_0\in K .
\end{gathered}
\tag{4}
\]
A prime means the coefficient \(t\)-derivative, while a dot means
\(\partial_q=2q\partial_t\). All derivative constants are still
\(\mathbb C\). Denominators in (4) are nonzero field elements,
not asserted units in the original ring.

## 2. Raw square equations and two linear lower-coefficient gates

For independent \(U,V\), use the literal coefficient expressions
\[
\begin{aligned}
S&=dU^3+\frac{k_{tt}}2U^2+R'UV+n_tU+n_\rho V,\\
T&=e_4U^4+\frac{k_{ttt}}6U^3+\frac{R''}2U^2V
       +\frac{n_{tt}}2U^2+n_{t\rho}UV+\frac{\nu}{2}V^2,\\
\mathcal H&=R(T-\ell_tU-\ell_\rho V-m)
             +(R'U+n_\rho)(\ell-S),\\
d&=\frac1{16q^5},\qquad e_4=-\frac5{128q^7}.
\end{aligned}
\tag{5}
\]
The actual alternatives have
\(\mathcal H=A_2(V-P(U))^2+B_1U+B_0\), with
\(A_2=R\nu/2\), \(P=p_2U^2+p_1U+p_0\), and
\(p_2=-\Delta/(R\nu)\ne0\).
The [actual square-Jacobian gate193](weight-four-split-square-candidate-jacobian-obstruction-pass193-working.md)
gives \((B_1)_\rho=0\), including the graph case \(B_1=0\).

For exact coefficient extraction put
\[
\begin{gathered}
\mathcal B=Rn_{t\rho}-2R'n_\rho,\qquad
\mathcal C_2=\frac{Rn_{tt}}2-R'n_t-\frac{n_\rho k_{tt}}2,\qquad
\mathcal C=-R\ell_\rho-n_\rho^2,\\
\ell_\rho=\frac{\mathcal B^2}{2\Delta R}
           -\frac{\nu\mathcal C_2}{\Delta}-\frac{n_\rho^2}{R},
\qquad
B_1=-R\ell_t+R'\ell-n_\rho n_t-\frac{\mathcal B\mathcal C}{R\nu}.
\end{gathered}
\tag{6}
\]
The right side for \(\ell_\rho\) is polynomial in \(\rho\) of degree
at most two. Explicit primitive subtraction therefore gives
\(\ell\in K[\rho]\), of degree at most three, plus its unrestricted
constant term in \(K\). This holds even if \(L/K(\rho)\) was initially
a proper finite extension.

Define the rational polynomial
\[
A(q)=q(q+1)^2(3q-1).
\]
The raw \(U^3V^0\) residual, after completing the square, is
\[
\frac{q(q+1)\dddot k_0+3q\ddot k_0-3\dot k_0
                         -3(As_0)^{\boldsymbol\cdot}}
     {48q^5(q+1)^2}.
\tag{7}
\]
Indeed the unspecialized expression is
\(Rk_{ttt}/6-R'k_{tt}/2-dn_\rho-\Delta\mathcal B/(R\nu)\);
its positive-\(\rho\) coefficient cancels with the fixed values (4).
It must vanish. Independently, substitution in (6) gives
\[
[\rho^3]B_1=0,\qquad
[\rho^2]B_1=
 \frac{(qAs_0)^{(3)}-k_0^{(3)}}
 {4q^4(q+1)^4(3q-1)^2}.
\tag{8}
\]
Here parentheses denote \(q\)-derivatives.
Neither \(n_0\), the constant term of \(\ell\), nor \(m\) enters (8).

For a direct way to reconstruct these computations, write
\(\mathcal B=b_1\rho+b_0\) and
\(\mathcal C_2=c_2\rho^2+c_1\rho+c_0\). Then
\[
\begin{gathered}
b_1=R\nu'-2R'\nu,\quad b_0=Rs_0'-2R's_0,\\
c_2=R\nu''/4-R'\nu'/2-\nu R''/2,\\
c_1=Rs_0''/2-R's_0'-(\nu k_0''+s_0R'')/2,\qquad
c_0=Rn_0''/2-R'n_0'-s_0k_0''/2 .
\end{gathered}
\]
If \(\ell_\rho=a_2\rho^2+a_1\rho+a_0\), formula (6) gives
\(a_2=b_1^2/(2\Delta R)-\nu c_2/\Delta-\nu^2/R\),
\(a_1=b_1b_0/(\Delta R)-\nu c_1/\Delta-2\nu s_0/R\), and
\(a_0=b_0^2/(2\Delta R)-\nu c_0/\Delta-s_0^2/R\).
Using \([\rho^2]\ell=a_1/2\) in (6) gives (8) directly.

## 3. Exact-field integration and the complete k0 solution

Equations (7)--(8) integrate inside \(K\):
\[
\begin{gathered}
3As_0=q(q+1)\ddot k_0+(q-1)\dot k_0-4k_0+c_0^*,\\
qAs_0-k_0=C_2q^2+C_1q+C_0,\qquad
c_0^*,C_0,C_1,C_2\in\mathbb C .
\end{gathered}
\tag{9}
\]
Each step subtracts a displayed polynomial primitive; a function
with zero \(q\)-derivative is complex. Thus (9) does not presume
\(K=\mathbb C(q)\).

Eliminating \(s_0\), define
\[
\mathscr L(h)=q^2(q+1)\ddot h+q(q-1)\dot h-(4q+3)h .
\]
Then
\[
\mathscr L(k_0)=3C_2q^2+(3C_1-c_0^*)q+3C_0 .
\tag{10}
\]
This equation has a complete rational basis:
\[
\begin{gathered}
\mathscr L(R)=\mathscr L(q^4R)=0,\qquad
\mathscr L(1)=-4q-3,\qquad
\mathscr L(q^2)=-3q^2,\qquad
\mathscr L(q^2R)=-4q,\\
k_0=\kappa_0+\kappa_2q^2+
          R(p_0+p_1q^2+p_2^*q^4),
\qquad \kappa_0,\kappa_2,p_0,p_1,p_2^*\in\mathbb C .
\end{gathered}
\tag{11}
\]
The three displayed inhomogeneous images span all quadratic
polynomials. The two homogeneous solutions have nonzero Wronskian
\(R(q^4R)^{\boldsymbol\cdot}-\dot R(q^4R)=4q^3R^2\).
For any homogeneous solution \(h\in K\), solve for its two coefficients
using \(h,\dot h\) and this Wronskian. Differentiating those coefficients
and using the common second-order equation makes both derivatives zero.
They are therefore complex. This proves completeness of (11) in every
allowed finite \(K\), not only among rational trial functions.

## 4. Actual shear removes k0, and the remaining gate determines n0

Let
\(P_2(X,Y)=p_0X^2+p_1XY+p_2^*Y^2\) and
\(P(t)=p_0+p_1t+p_2^*t^2\). Make the actual change
\[
X_1=X,\quad Y_1=Y,\quad
Z_1=Z-\kappa_0X-\kappa_2Y,\qquad W_1=W+P_2(X,Y).
\tag{12}
\]
The inverse adds the same lower polynomial to \(Z_1\) and subtracts
\(P_2(X_1,Y_1)\) from \(W_1\); both composition orders cancel literally.
In the coefficient chart,
\(\rho_1=\rho+P(t)\), \(\vartheta_1=\vartheta+P'(t)y\),
\(z_1=z-\kappa_2y\), and \(w_1=w+p_2^*y^2\).
The new potentials satisfy \(k_1=R\rho_1\) and
\(n_1=n(\rho_1-P(t))\). The fixed-coefficient derivative change is
included: the possible residual \(y\)-coefficient is
\((k_0-RP)'-\kappa_2=0\).

Drop the subscript. Reapplying (7) with \(k_0=0\) gives
\[
s_0=\frac{C}{A(q)},\qquad C\in\mathbb C .
\tag{13}
\]
The next coefficient of (6) now simplifies to
\[
[\rho]B_1=
 \frac{(3q-1)^4\,[q(q+1)n_0]^{(3)}+9C^2}
      {2q^3(q+1)^3(3q-1)^5}.
\tag{14}
\]
For example its numerator before grouping has coefficients
\(q(q+1)(3q-1)^4\) on \(\dddot n_0\),
\(3(2q+1)(3q-1)^4\) on \(\ddot n_0\), and
\(6(3q-1)^4\) on \(\dot n_0\), plus \(9C^2\).
Its vanishing integrates exactly, since
\(((3q-1)^{-1})^{(3)}=-162(3q-1)^{-4}\):
\[
n_0=R\left\{\frac{C^2}{18(3q-1)}
                   +N_0+N_1q+N_2q^2\right\},
\qquad N_0,N_1,N_2\in\mathbb C .
\tag{15}
\]
The constant term of \(\ell\) still cannot alter this gate.

The three free modes in (15) are removable in the original ring:
\[
Z_2=Z_1-N_1,\qquad
W_2=W_1+N_0X_1+(N_2-N_1)Y_1,
\quad X_2=X_1,\ Y_2=Y_1.
\tag{16}
\]
Its inverse uses the opposite additions.
The resulting \(n_0\) is \(RC^2/[18(3q-1)]\), since
\(1=R(q^2+q)\). The \(k\)-potential, \(\rho,t,q\) are unchanged.

## 5. An actual X translation removes the last parameter

Starting from \(k=R\rho\) and the minimal (15), for any
\(\tau\in\mathbb C\) put
\[
\begin{aligned}
X_3&=X_2+\tau,\qquad Y_3=Y_2,\\
Z_3&=Z_2+\frac{3\tau}{2}Y_2,\qquad
W_3=W_2+\frac{3\tau}{2}(Y_2^2-X_3Y_2).
\end{aligned}
\tag{17}
\]
The inverse is
\(X_2=X_3-\tau\), \(Y_2=Y_3\),
\(Z_2=Z_3-(3\tau/2)Y_3\),
\(W_2=W_3-(3\tau/2)(Y_3^2-X_3Y_3)\).
This proves both inverse orders as polynomial identities.

Here are the coefficient changes, to distinguish (17) from a free
reparametrization. Write \(P_\tau(t)=3\tau(t^2-t)/2\), and use old
unsubscripted chart entries:
\[
\begin{gathered}
y_3=y-\tau q^2,\qquad
\rho_3=\rho+P_\tau(t),\qquad
\vartheta_3=\vartheta-2\tau\rho+P_\tau'(t)y_3,\\
z_3=z-\tau(q'y+R\rho)+\tau^2q+\frac{3\tau}{2}y_3,\qquad
w_3=w-\tau\vartheta+\tau^2\rho+\frac{3\tau}{2}y_3^2 .
\end{gathered}
\tag{18}
\]
The new \(k\) is again \(R\rho_3\).
For instance the identity
\(R P_\tau=-3\tau q/2+3\tau q^2/2\) cancels the \(k\)-change.
In the second potential, with \(Q=-1/(8q^3)\), take
\(n_3=z_3-Qy_3^2-R'\rho_3y_3-R\vartheta_3\).
Literal substitution gives
\[
\begin{gathered}
n_3=\frac{\nu}{2}\rho_3^2+\frac{C+\tau}{A}\rho_3
 +R\left\{\frac{(C+\tau)^2}{18(3q-1)}
                     +P_{\tau,C}(q)\right\},\\
P_{\tau,C}(q)=
 \frac{-9C\tau q^2+6C\tau q+2C\tau
                 +9\tau^2q^2+3\tau^2q+\tau^2}{18}.
\end{gathered}
\tag{19}
\]
Choose \(\tau=-C\). The new linear coefficient is zero and
\(P_{-C,C}=C^2(q^2-q/6-1/18)\).
One more instance of (16), explicitly
\[
Z_4=Z_3+\frac{C^2}{6},\qquad
W_4=W_3-\frac{C^2}{18}X_3+\frac{7C^2}{6}Y_3,
\quad X_4=X_3,\ Y_4=Y_3,
\tag{20}
\]
removes this polynomial as well. Its inverse again uses the opposite
constant and linear additions. The final canonical conclusion is
\[
\boxed{\quad k=R\rho,\qquad n=\frac{\nu}{2}\rho^2,\qquad
R=\frac1{q(q+1)},\quad
\nu=\frac1{q^3(q+1)^3(3q-1)}.\quad}
\tag{21}
\]

## 6. The remaining scalar and the precise scope

For (21), formula (6) also gives
\[
\begin{gathered}
\ell=L_3\rho^3+\ell_0,\qquad \ell_0\in K,\qquad
L_3=-\frac{q^2+4q-1}{2q^5(q+1)^5(3q-1)^3},\\
B_1=-R(\ell_0)_t+R'\ell_0 .
\end{gathered}
\tag{22}
\]
Thus in the graph alternative alone, \(B_1=0\) implies
\(\ell_0=\lambda R\), \(\lambda\in\mathbb C\).
The actual translation \(W\mapsto W-\lambda\), with its opposite
translation as inverse, subtracts \(R\lambda\) from the third potential.
It leaves \(k,n,\rho,\vartheta\) unchanged.
In the quadratic-projection alternative, \(\ell_0\) is not normalized
away by this argument.

Every original map above has complex polynomial coefficients, with
its inverse explicitly supplied. After the initial scaling, every
inverse keeps the old \(X,Y,W\) independent of the new \(Z\) and has
old \(Z=\) new \(Z+\) a polynomial in the new \(X,Y\).
The selected partial \(\partial_Z\), hence \(N\) and \(L\), is unchanged.
All changes of \(\rho\) are a nonzero complex scaling or an addition
of a polynomial in \(t\), so the exact derivative-constant field \(K\)
is preserved too. The generic \(y\)-coordinate changes only by a
nonzero complex scaling or an \(L\)-translation; \(\vartheta\) changes
by such a scaling and an affine polynomial in the old \(y\).
Therefore the graph/quadratic-projection distinction is preserved.

The initial diagonal map sends the full relation to a nonzero
constant multiple. The remaining filtered changes preserve the
leading \(X,Y,Z\) slots and change only the absent \(W\) slot by a
binary quadratic. Its leading ratio remains nonzero, because
\(\rho\) is independent of \(t\).
Thus the exact1122 profile and entire initial kernel persist.
These facts justify applying the same actual coefficient gates after
each stage; they are not assumptions that formal chart changes lift.

This lemma normalizes lower potentials for the nonmonomial family;
it does not solve the remaining scalar determinant, actual field
return or original-coordinate problem in either alternative.
It does not imply a rational ambient \(K\), realization of the bare
system, recognition of the family, or unrestricted cancellation.
The raw identities were independently expanded in new inline
arithmetic, separate from any saved checker. No saved checker was
executed, imported or compiled, and no197 or earlier source was edited.
