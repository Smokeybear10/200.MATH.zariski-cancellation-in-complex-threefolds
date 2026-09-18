# The scalar Jacobian excludes the rational split square-completion candidate

Status: bounded working obstruction. The rational function
\(f=t^5+3t\) satisfies the necessary ODE in
[counterexample192](weight-four-split-nonzero-r-ode-counterexample-pass192-working.md),
but it cannot occur in the actual square-completion branch considered there.
The obstruction is a second differential gate, obtained from the scalar
Jacobian rather than from the coefficient comparisons used in192.

This does not exclude every nonaffine solution of the first ODE or every
remaining split-quartic branch. No original coordinate or unrestricted
cancellation theorem is claimed.

## 1. Exact conditional setup

Retain the actual coefficient chart of
[universal184](weight-four-universal-chart-potentials-pass184-working.md).
In particular the projected entries lie in \(L[v]\), generate that entire
ring, and have nonzero scalar Jacobian:
\[
L[y,z,w]=L[v],\qquad
\det\frac{\partial(y,z,w)}{\partial(t,\rho,v)}
 =-\mathfrak a^3\in L^*.
\tag{1}
\]
Here \(t,\rho\) are algebraically independent, \(L/\mathbb C(t,\rho)\)
is finite, its coefficient partials commute, and
\(K=\ker_L\partial_\rho\) is finite over \(\mathbb C(t)\).
The derivative constants of \(K\) are exactly \(\mathbb C\).
Primes below denote its \(t\)-derivative. Rationality of \(K\) is not assumed.

Suppose \(q\in K\), \(R=k_\rho\in K^*\), and the nondegenerate
square-completion comparison of192 applies. Put
\[
\begin{gathered}
Q=q''/2,\quad d=q'''/6,\quad e=q''''/24,\qquad
k=R\rho+k_0,\\
\nu=n_{\rho\rho}\in K^*,\qquad
n=\frac{\nu}{2}\rho^2+s_0\rho+n_0,\quad k_0,s_0,n_0\in K,\\
\Delta=\frac{RR''}{2}-(R')^2\ne0.
\end{gathered}
\tag{2}
\]
The symbol \(\nu\) is a coefficient, not the selected locally nilpotent
derivation. All divisions here and below are in the exact coefficient
field. They are not claims about units in the original polynomial ring.

With independent variables \(U,V\), write
\[
\begin{aligned}
S&=dU^3+\frac{k_{tt}}2U^2+R'UV+n_tU+n_\rho V,\\
T&=eU^4+\frac{k_{ttt}}6U^3+\frac{R''}2U^2V
   +\frac{n_{tt}}2U^2+n_{t\rho}UV+\frac{\nu}{2}V^2,\\
\mathcal H&=R(T-\ell_tU-\ell_\rho V-m)
 +(R'U+n_\rho)(\ell-S).
\end{aligned}
\tag{3}
\]
Assume the polynomial identity
\[
\mathcal H=A(V-P(U))^2+B_1U+B_0,\qquad
P=p_2U^2+p_1U+p_0,\qquad A,p_2\ne0.
\tag{4}
\]
The coefficients \(B_1,B_0,p_1,p_0\) initially belong to \(L\).
The already necessary comparisons give
\[
A=\frac{R\nu}{2}\in K^*,\qquad
p_2=-\frac{\Delta}{R\nu}\in K^*.
\tag{5}
\]
Evaluation at \((y,\vartheta)\) gives \(\mathcal H(y,\vartheta)=0\), and
the other two projected entries are
\[
z=Qy^2+k_ty+R\vartheta+n,\qquad
w=\frac{\ell-S(y,\vartheta)}R.
\tag{6}
\]
These are identities in the retained actual chart. Formal solutions of
(3)--(6) without (1) do not meet the hypotheses of the obstruction.

## 2. The linear remainder must be rho-constant

We prove that every actual configuration satisfying these hypotheses has
\[
(B_1)_\rho=0.
\tag{7}
\]
If \(B_1=0\), this is immediate. Suppose henceforth \(B_1\ne0\).
Set
\[
\zeta=\vartheta-P(y),\qquad
y=a\zeta^2+b,\qquad
a=-\frac{R\nu}{2B_1}\ne0,\quad b=-\frac{B_0}{B_1}.
\tag{8}
\]
By (6), \(L[y,z,w]\subseteq L[y,\vartheta]\subseteq L[v]\), so (1)
gives \(L[y,\vartheta]=L[v]\). Equation (8) and
\(\vartheta=P(y)+\zeta\) then give \(L[\zeta]=L[v]\).
Thus \(\zeta\) is affine in \(v\) over \(L\). Changing from \(v\) to
\(\zeta\) multiplies the Jacobian by a nonzero element of \(L\);
the new determinant is still in \(L^*\).

For the calculation use independent \(U,\zeta\) and put
\(V=P(U)+\zeta\). Coefficient partials in the next formulas fix both
\(U,\zeta\). The expressions in (6) become
\[
\begin{gathered}
z=Z_2U^2+Z_1U+Z_0+R\zeta,\qquad
Z_2=Q+Rp_2\in K,\\
Z_1=k_t+Rp_1,\quad Z_0=n+Rp_0,\qquad
w=w_{\mathrm{pol}}(U)-l(U)\zeta,\quad
l(U)=\frac{R'U+n_\rho}{R}.
\end{gathered}
\tag{9}
\]
Here \(w_{\mathrm{pol}}\in L[U]\). Define
\(F_i=Rw_i+l z_i\) for \(i=t,\rho\).
The terms from differentiating \(P\) cancel in \(F_i\), because
\(z_V=R\) and \(w_V=-l\) before the substitution.

The identities \(S_t=T_U\), \(S_\rho=T_V\),
\(z_t=S_U\), and \(z_\rho=S_V=Rl\), taken before that substitution,
give
\[
\mathcal H_U=-R(Rw_t+l z_t),\qquad
\mathcal H_V=-R(Rw_\rho+l z_\rho).
\]
Differentiating the right side of (4) in \(U,V\), and then substituting,
therefore gives
\[
F_t=\nu P_U(U)\zeta-\frac{B_1}{R},\qquad
F_\rho=-\nu\zeta.
\tag{10}
\]
These are exact gradient identities; no derivative of an evaluated
coefficient has been substituted for a coefficient derivative.

After \(U=y=a\zeta^2+b\), expand \(dy\wedge dz\wedge dw\).
In the order \(dt,d\rho,d\zeta\), the determinant is
\[
\begin{aligned}
J&=y_\rho F_t-y_t F_\rho
 +\frac{y_\zeta}{R}(z_tF_\rho-z_\rho F_t)\\
 &=-\frac{B_1}{R}y_\rho
   +\nu\zeta\left(P_U(y)y_\rho+y_t-\frac{z_\rho}{R}\right)
   +\frac{\nu^2}{B_1}\zeta^2
                    \left(z_t+P_U(y)z_\rho\right).
\end{aligned}
\tag{11}
\]
The symbols \(z_i\) on the right mean the coefficient partials in (9),
followed by substitution \(U=y\); the symbols \(y_i\) differentiate
(8), fixing \(\zeta\). The sign and final coefficient use
\(y_\zeta=2a\zeta=-R\nu\zeta/B_1\).

Because \(Z_2,R\in K\),
\[
z_\rho=(Z_1)_\rho y+(Z_0)_\rho,\qquad
z_t=Z_2'y^2+(Z_1)_t y+(Z_0)_t+R'\zeta.
\]
In (11), the final summand has only even powers of \(\zeta\),
apart from its possible cubic term from \(R'\zeta\).
The first summand has degree at most two.
In the middle summand, only \(P_U(y)y_\rho\) can contribute degree
five. Consequently
\[
[\zeta^5]J=2\nu p_2 a\,a_\rho.
\tag{12}
\]
The Jacobian lies in \(L^*\), so (12) vanishes. All of
\(\nu,p_2,a\) are nonzero. Hence \(a_\rho=0\).
Since \(R\nu\in K^*\), equation (8) proves (7).
This conclusion does not depend on \(B_0\), \(m\), or on a choice of
the constant term of the quadratic parametrization.

## 3. A reusable highest-rho differential gate

The remaining coefficient equations make (7) a condition purely on
\(R,\nu\). Define
\[
\mathscr B=R\nu'-2R'\nu,\qquad
\mathscr C=\frac{R\nu''}{4}-\frac{R'\nu'}2-\frac{\nu R''}2.
\tag{13}
\]
For the full coefficients, not just their highest terms, set
\[
B=Rn_{t\rho}-2R'n_\rho,\qquad
C_2=\frac{Rn_{tt}}2-R'n_t-\frac{n_\rho k_{tt}}2,\qquad
C=-R\ell_\rho-n_\rho^2.
\]
The \(V\)-coefficient is \(\Delta U^2+BU+C\).
Comparison of \(U^2V^0\) in (4) gives
\[
C_2=\frac{B^2+2\Delta C}{2R\nu},\qquad
\ell_\rho=\frac{B^2}{2\Delta R}
          -\frac{\nu C_2}{\Delta}-\frac{n_\rho^2}{R}.
\tag{14}
\]
The right side is a polynomial in \(\rho\) of degree at most two.
Subtracting its explicit polynomial primitive leaves an element of
\(\ker_L\partial_\rho=K\). Thus \(\ell\in K[\rho]\), of degree at most
three, even if \(L\) was initially a proper finite extension of \(K(\rho)\).

The coefficient of \(\rho\) in \(B\) is \(\mathscr B\), and that of
\(\rho^2\) in \(C_2\) is \(\mathscr C\). Therefore
\[
\mathscr L:=[\rho^3]\ell
 =\frac13\left(
       \frac{\mathscr B^2}{2\Delta R}
       -\frac{\nu\mathscr C}{\Delta}
       -\frac{\nu^2}{R}\right).
\tag{15}
\]
It does not depend on \(k_0,s_0,n_0\) or on the integration constant
in \(\ell\).

The \(UV^0\) coefficient of \(\mathcal H\) is
\(-R\ell_t+R'\ell-n_\rho n_t\); the corresponding coefficient of
\(A(V-P)^2\) at \(V=0\) is \(BC/(R\nu)\). Hence
\[
B_1=-R\ell_t+R'\ell-n_\rho n_t-\frac{BC}{R\nu}
 \in K[\rho],\qquad \deg_\rho B_1\le3.
\tag{16}
\]
Taking its cubic coefficient gives the second differential gate
\[
\boxed{\;
\mathscr M:=
 -R\mathscr L'+R'\mathscr L-\frac{\nu\nu'}2
 +\frac{\mathscr B(3R\mathscr L+\nu^2)}{R\nu}=0.
\;}
\tag{17}
\]
If \(B_1\ne0\), this follows from (7). If \(B_1=0\), it follows directly
from (16). Thus (17) is necessary in either case of (4).
The polynomial constant remainder \(B_0\), and therefore \(m\), cannot
alter this coefficient. It is a necessary condition, not a sufficiency
criterion for an actual frame.

## 4. Applying the gate to the rational candidate

Now specialize to the split form and candidate of192:
\[
\begin{gathered}
q=-t^3-t^{-1},\qquad
R=\frac1{t(t^4+3)},\qquad
\nu=\frac{50t^3}{(t^4+3)^3(1-5t^4)},\\
\Delta=-\frac{10}{(t^4+3)^3},\qquad
p_2=\frac{(1-5t^4)(t^4+3)}{5t^2}.
\end{gathered}
\tag{18}
\]
Every displayed denominator is a nonzero element of the coefficient
field, and \(t\) is transcendental over \(\mathbb C\).
Direct substitution into (13) and (15) gives
\[
\mathscr L=
-\frac{125t^3(5t^4+3)(11t^4-7)}
       {(t^4+3)^5(5t^4-1)^3}.
\tag{19}
\]
Substitution into (17) then gives
\[
\mathscr M=
-\frac{875t(5t^4-11)}
       {(t^4+3)^5(5t^4-1)^3}\ne0.
\tag{20}
\]
Equations (19)--(20) are rational identities in the transcendental
\(t\), not conclusions from selected numerical evaluations.

Thus no choices of \(k_0,s_0,n_0\in K\), no integration constant in
\(\ell\), and no \(m\in L\) make this candidate satisfy the full actual
square-completion hypotheses. It violates the scalar Jacobian gate.

For comparison, the bare coefficient identity (4) has no such
obstruction. Set \(k_0=s_0=n_0=0\), choose
\(\ell=\mathscr L\rho^3\), and choose \(m\) to prescribe any desired
constant remainder \(B_0\). Equations (5), (14), and the first ODE of192
then supply all coefficients of (4), with
\(B_1=\mathscr M\rho^3\ne0\).
This is a surviving formal potential system, but (12) prevents it
from being the actual constant-Jacobian chart. The distinction explains
why the first ODE is necessary but insufficient.

## 5. Scope and evidence

The first ODE in192 remains valid, and \(t^5+3t\) remains its nonaffine
rational solution. The new result excludes that solution from the
specified actual square-completion branch. It does not classify solutions
of the simultaneous first ODE and (17), exclude every square branch,
or settle unrestricted cancellation.

The general gate (17) retains \(\nu=\Delta^2/(2R(eR-dR'))\) from192
when that nonzero comparison is imposed. It can be studied together
with the first ODE without assuming \(K=\mathbb C(t)\).
No global unit speed, original polynomial inverse, or recognition
theorem has been inferred from a formal coefficient calculation.

Exploratory read-only rational calculations checked (19)--(20) and a
specific formal determinant. They are not canonical test suites or a
replacement for the coefficient and wedge proof above. No saved checker
was executed, imported, or compiled, and no192 or earlier file was
modified. This is a working proof, not human expert review,
proof-assistant certification, or a historical novelty claim.

