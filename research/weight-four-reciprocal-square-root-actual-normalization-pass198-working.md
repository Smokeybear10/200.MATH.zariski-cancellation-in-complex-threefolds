# Actual normalization of the reciprocal square-root square branch

Status: bounded working normalization lemma, pending independent review.
For the supplied actual full initial kernel \(Z^2-X^3Y\) and reciprocal
family \(f=\beta_0/q\), the polynomial changes below normalize
\(k=q\rho\) and \(n=-q\rho^2/2\). They preserve the selected intrinsic
derivation and both generic-degree alternatives. This is not a
recognition or exclusion theorem for either remaining alternative.

## 1. Actual setup and derivative conventions

Assume the actual supplied globally sliced frame and exact chart of
[universal184](weight-four-universal-chart-potentials-pass184-working.md):
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=\mathcal A[u],\qquad E=\partial_u,\qquad
\deg_E(X,Y,Z,W)=(1,1,2,2),\\
\ker\theta_0=(\mathsf Z^2-\mathsf X^3\mathsf Y),\qquad
q^2=t,\qquad N=[u^3](\partial_Z|_{\mathcal A})\ne0,\\
L=\operatorname{Frac}(\ker_{\mathcal A}N),\qquad
\mathcal A_L=L[v],\quad Nv=1,\qquad
K=\ker_L\partial_\rho,\quad [K:\mathbb C(q)]<\infty,\\
\ker_K\partial_q=\mathbb C,\qquad
Y=y+tX,\quad Z=z+(q_ty+k)X+qX^2,\quad
W=w+\vartheta X+\rho X^2 .
\end{gathered}
\tag{1}
\]
The ideal is the entire weighted initial kernel, and \(t,\rho\) are
independent. The actual whole-plane, projected field-return and scalar
Jacobian inputs are retained. The selected nonzero-R branch has
\[
\mathcal H=A_2(V-P(U))^2+B_1U+B_0,\qquad
P=p_2U^2+p_1U+p_0,\qquad A_2p_2\ne0,\qquad
f=1/R=\beta_0/q,\quad \beta_0\in\mathbb C^* .
\tag{2}
\]
These are the surviving square alternatives in
[reduction195](weight-four-double-cover-nonzero-r-reduction-pass195-working.md).
The actual square-Jacobian gate gives \((B_1)_\rho=0\); in the graph
case \(B_1=0\) this is immediate. In the quadratic-projection case
it is the retained odd-degree scalar-Jacobian argument, not an
assumption on freely chosen formal potentials.

Make the actual constant scaling \(W_1=W/\beta_0\), fixing \(X,Y,Z\).
Its inverse is \(W=\beta_0W_1\). It gives
\(\rho_1=\rho/\beta_0\), \(\vartheta_1=\vartheta/\beta_0\) and
\(R_1=\beta_0R=q\). Drop subscripts after this scaling.
The symbol \(\partial_t\) below differentiates at fixed \(\rho\);
a dot denotes \(\partial_q=2q\partial_t\).
Neither rationality of \(K\) nor polynomial membership of \(q\)
is assumed.

The exact leading and square-completion coefficients are
\[
\begin{gathered}
R=q,\qquad Q=q_{tt}/2=-\frac1{8q^3},\qquad
d=q_{ttt}/6=\frac1{16q^5},\qquad e=q_{tttt}/24=-\frac5{128q^7},\\
\Delta=RR_{tt}/2-R_t^2=-\frac3{8q^2},\qquad
C_4=Re-R_td=-\frac9{128q^6},\\
\nu:=n_{\rho\rho}=\frac{\Delta^2}{2RC_4}=-q,\qquad
p_2=-\frac{\Delta}{R\nu}=-\frac3{8q^4},\\
k=q\rho+k_0,\qquad
n=-\frac q2\rho^2+s_0\rho+n_0,\qquad k_0,s_0,n_0\in K.
\end{gathered}
\tag{3}
\]
For example \(C_4=(R\nu/2)p_2^2\) and the \(U^2V\) coefficient
\(-R\nu p_2=\Delta\) give the displayed \(\nu\).
The integrations in \(\rho\) in (3) follow by polynomial primitive
subtraction and the exact derivative-constant field \(K\).

## 2. Raw square coefficients before normalization

For independent \(U,V\), set
\[
\begin{aligned}
S&=dU^3+\frac{k_{tt}}2U^2+R_tUV+n_tU+n_\rho V,\\
T&=eU^4+\frac{k_{ttt}}6U^3+\frac{R_{tt}}2U^2V
       +\frac{n_{tt}}2U^2+n_{t\rho}UV+\frac{\nu}{2}V^2,\\
\mathcal H&=R(T-\ell_tU-\ell_\rho V-m)
                   +(R_tU+n_\rho)(\ell-S).
\end{aligned}
\tag{4}
\]
These are the literal third and fourth universal potentials. All
partials act on coefficients before evaluation at \(U=y,V=\vartheta\).
Introduce
\[
\begin{gathered}
\mathcal B=Rn_{t\rho}-2R_tn_\rho,\qquad
\mathcal C_2=\frac{Rn_{tt}}2-R_tn_t-\frac{n_\rho k_{tt}}2,\qquad
\mathcal C=-R\ell_\rho-n_\rho^2,\\
\ell_\rho=\frac{\mathcal B^2}{2\Delta R}
          -\frac{\nu\mathcal C_2}{\Delta}-\frac{n_\rho^2}{R},\\
B_1=-R\ell_t+R_t\ell-n_\rho n_t-\frac{\mathcal B\mathcal C}{R\nu}.
\end{gathered}
\tag{5}
\]
The formula for \(\ell_\rho\) is the constant \(U^2\) comparison
after completing the square: the coefficient linear in \(V\) is
\(\Delta U^2+\mathcal B U+\mathcal C=-R\nu P(U)\).
The formula for \(B_1\) is the remaining constant \(U\) coefficient.
The right side for \(\ell_\rho\) is polynomial in \(\rho\) of degree
at most two. Subtracting an explicit primitive gives
\(\ell\in K[\rho]\), with one integration constant in \(K\).

The constant \(U^3\) comparison is
\[
\frac{Rk_{ttt}}6-\frac{R_tk_{tt}}2-dn_\rho
                  -\frac{\Delta\mathcal B}{R\nu}
 =\frac{q^3\dddot k_0-6q^2\ddot k_0+6q\dot k_0
                   -9q\dot s_0+15s_0}{48q^5}=0.
\tag{6}
\]
Here and below dots are \(q\)-derivatives, not \(t\)-derivatives.
For example
\(\mathcal B=\rho/2+\dot s_0/2-s_0/q\), which fixes the signs
in this comparison.

Let \(h_0=k_0+s_0\). One useful intermediate coefficient obtained
from (5) is
\[
[\rho]\ell_\rho
 =3s_0+\frac{q\dot h_0-q^2\ddot h_0}{3}.
\tag{7}
\]
If this coefficient is denoted by \(e_1\), direct substitution into
the last line of (5) gives
\[
\begin{gathered}
[\rho^3]B_1=0,\\
[\rho^2]B_1
 =\frac{-\dot e_1-e_1/q+3\dot s_0+3s_0/q}{4}
 =\frac{q^2\dddot h_0+2q\ddot h_0-2\dot h_0}{12}.
\end{gathered}
\tag{8}
\]
This coefficient is independent of \(n_0\) and the integration
constant of \(\ell\). Since \((B_1)_\rho=0\), it vanishes.

## 3. Exact-field Euler equations and their complete solutions

Put \(\mathscr D=q\partial_q\). Equation (8) is
\(\mathscr D(\mathscr D-2)(\mathscr D+1)h_0=0\). Hence
\[
h_0=A_0+A_2q^2+\frac{a}{q},\qquad A_0,A_2,a\in\mathbb C .
\tag{9}
\]
For completeness, this does not follow from a rational-function
ansatz. For a product of distinct factors
\(\prod_i(\mathscr D-\lambda_i)\), polynomial spectral projections
decompose any solution in \(K\) into solutions of the individual
first-order equations. Each such solution here obeys
\((q^{-\lambda_i}h_i)^{\boldsymbol\cdot}=0\).
The integer exponents \(0,2,-1\) make those powers elements of \(K\),
and its exact constants give complex multiples of these powers.

Substituting \(s_0=h_0-k_0\) into (6) gives
\[
(\mathscr D-1)(\mathscr D-3)(\mathscr D-5)k_0
       =-15A_0+3A_2q^2-\frac{24a}{q}.
\tag{10}
\]
The displayed inhomogeneous terms have the particular solution
\(A_0+A_2q^2+a/(2q)\). Applying the same distinct-root argument
to the remainder gives the complete exact-field formulas
\[
\begin{gathered}
k_0=A_0+A_2q^2+\frac{a}{2q}
                  +K_1q+K_3q^3+K_5q^5,\\
s_0=\frac{a}{2q}-K_1q-K_3q^3-K_5q^5,\qquad
K_1,K_3,K_5\in\mathbb C .
\end{gathered}
\tag{11}
\]
No lower coefficient is silently set to zero, and no finite field
extension is identified with a rational field by these integrations.

## 4. First actual shear and the fixed-rho derivative correction

Define the complex polynomials
\[
P_2(X,Y)=K_1X^2+K_3XY+K_5Y^2,\qquad
P(t)=K_1+K_3t+K_5t^2.
\]
Make the actual original-ring change
\[
X_1=X,\quad Y_1=Y,\quad
Z_1=Z-A_0X-A_2Y,\qquad W_1=W+P_2(X,Y).
\tag{12}
\]
Its polynomial inverse is
\(Z=Z_1+A_0X_1+A_2Y_1\),
\(W=W_1-P_2(X_1,Y_1)\), with \(X=X_1,Y=Y_1\).
Both compositions cancel the displayed polynomials.

The chart changes are
\[
\begin{gathered}
t_1=t,\quad q_1=q,\quad y_1=y,\qquad
\rho_1=\rho+P(t),\\
\vartheta_1=\vartheta+P_t(t)y,\qquad
w_1=w+K_5y^2,\qquad z_1=z-A_2y,\\
k_1=q\rho_1+\frac{a}{2q}.
\end{gathered}
\tag{13}
\]
The last equality is the actual \(X\)-coefficient of \(Z_1\), using
\(k_0=A_0+A_2t+a/(2q)+qP(t)\).

In the second universal potential the coefficient partial at fixed
\(\rho_1\) differs from the old one. Explicitly,
\[
(k_1)_{t,\rho_1}+qP_t
 =q_t(\rho+P)+(a/(2q))_t+qP_t=k_t-A_2 .
\tag{14}
\]
Thus the entire residual term transforms as
\[
\begin{gathered}
n_1(t,\rho_1)=n(t,\rho_1-P(t))
     =-\frac q2\rho_1^2+\frac{a}{2q}\rho_1+\bar n_0,\\
\bar n_0=n_0-s_0P-\frac q2P^2\in K .
\end{gathered}
\tag{15}
\]
This verifies the transformation of \(n\), rather than inferring it
from its leading \(\rho\)-coefficient alone.

## 5. A constant Y-translation removes both remaining lower slopes

Make the actual translation
\[
X_2=X_1,\qquad Y_2=Y_1+a,\qquad Z_2=Z_1,\qquad W_2=W_1,
\tag{16}
\]
with inverse \(Y_1=Y_2-a\), fixing the other entries.
It leaves \(t,q,\rho_1,\vartheta_1,z_1,w_1\) unchanged as coefficient
elements, while \(y_2=y_1+a\).
In particular the leading ratio \(t=EY/EX\) is not translated.
The first universal potential gives
\[
k_2=k_1-aq_t=q\rho_1 .
\tag{17}
\]
For the second potential substitute \(y_1=y_2-a\) and
\((k_1)_t=q_t\rho_1-a/(4q^3)\).
Since \(Q=-1/(8q^3)\), the extra \(y_2\)-coefficient is
\(-2aQ-a/(4q^3)=0\), and the constant change is
\[
\begin{gathered}
n_2=n_1-\frac{a\rho_1}{2q}+\frac{a^2}{8q^3}
       =-\frac q2\rho_1^2+\widehat n_0,\\
\widehat n_0=\bar n_0+\frac{a^2}{8q^3}\in K .
\end{gathered}
\tag{18}
\]
This is the complete translation formula. The same translation
simultaneously removes the residual \(k_0=a/(2q)\) and
\(s_0=a/(2q)\); their cancellation is not an additional assumption.

The actual changes preserve the generic degree of \(y\), so the
new square alternative still has its \(\rho\)-constant linear
remainder. Apply the raw equations (4)--(5) to this new actual chart,
and relabel \(\rho_1\) as \(\rho\). Now \(k=q\rho\) and
\(n=-q\rho^2/2+\widehat n_0\).
They give, before using the next scalar gate,
\[
\begin{gathered}
\ell_\rho=-\frac{3q}{2}\rho^2+
           q\dot{\widehat n}_0-\frac{q^2}{3}\ddot{\widehat n}_0,\\
[\rho]B_1=\frac{q^2\dddot{\widehat n}_0-q\ddot{\widehat n}_0}{6}=0 .
\end{gathered}
\tag{19}
\]
For example write the \(\rho\)-constant term of \(\ell_\rho\) as
\(e_0=q\dot{\widehat n}_0-q^2\ddot{\widehat n}_0/3\).
The last expression in (5) gives
\([\rho]B_1=(-\dot e_0+\dot{\widehat n}_0)/2\), proving (19).
The remaining integration constant of \(\ell\) cannot affect this
coefficient.

The equation in (19) says
\((\ddot{\widehat n}_0/q)^{\boldsymbol\cdot}=0\).
Three explicit primitive subtractions in \(K\) therefore give
\[
\widehat n_0=N_3q^3+N_1q+N_0,\qquad N_3,N_1,N_0\in\mathbb C .
\tag{20}
\]

## 6. Final actual lower-degree shear and the bare potentials

Make the actual change
\[
X_3=X_2,\quad Y_3=Y_2,\quad
Z_3=Z_2-N_0,\qquad W_3=W_2+N_1X_2+N_3Y_2 .
\tag{21}
\]
The inverse adds \(N_0\) to \(Z_3\) and subtracts
\(N_1X_3+N_3Y_3\) from \(W_3\).
The chart has unchanged \(t,q,\rho\); its \(\vartheta\) gains
\(N_1+N_3t\), while its \(z\) loses \(N_0\).
Thus its second potential subtracts
\(q(N_1+N_3t)+N_0\) from \(n_2\).
Relabeling the final coefficients proves the actual normalization
\[
k=q\rho,\qquad n=-\frac q2\rho^2.
\tag{22}
\]

The raw formulas now yield
\[
\ell_\rho=-\frac{3q}{2}\rho^2,\qquad
\ell=-\frac q2\rho^3+l,\quad l\in K,\qquad
B_1=\frac{l-q\dot l}{2q}.
\tag{23}
\]
This statement leaves \(l\) unrestricted in the quadratic-projection
alternative. In the graph alternative \(B_1=0\) gives \(l=Cq\),
\(C\in\mathbb C\). If desired, the actual constant translation
\(W_4=W_3-C\), with inverse \(W_3=W_4+C\), subtracts \(RC=Cq\)
from the third potential and makes \(\ell=-q\rho^3/2\).
That final specialization is graph-only, not part of the common
normalization (22).

## 7. Selected derivation, initial ideal, and scope

Every displayed map is an original polynomial automorphism with
complex coefficients and a written inverse. The derivation \(E\)
and the given global slice \(u\) are unchanged.
In every inverse, old \(X,Y,W\) are independent of the new \(Z\),
and old \(Z\) is new \(Z\) plus a polynomial in the other coordinates.
Consequently the actual selected partial \(\partial_Z\) is unchanged.
So are \(N=[u^3](\partial_Z|_{\mathcal A})\), \(L\), and the selected
generic line. The changes of \(\rho\) are a nonzero complex scaling
and additions of functions of \(t\), preserving its derivative-constant
field \(K\).

All changes of \(y\) are affine translations over \(L\).
All changes of \(\vartheta\), apart from the initial nonzero complex
scaling, add polynomials of degree at most one in the old \(y\).
Thus the affine-versus-quadratic generic degree of \(y\), and the
quadratic-graph alternative when present, are preserved.
In particular one may legitimately reapply the actual square gate
\((B_1)_\rho=0\) in the chart used in (19).

The exact E-time degrees stay \((1,1,2,2)\).
The changes in \(Z\) have degree at most one in time, and the
translation in \(Y\) has degree zero, so their leading coefficients
do not change. The only quadratic alteration of \(W\) replaces its
ratio by \(\rho+P(t)\), nonzero by the independence of \(t,\rho\).
The associated filtered initial maps are invertible; they fix the
leading \(X,Y,Z\) slots and alter only the absent \(W\) slot by a
constant scaling and a binary quadratic. Hence the entire initial
ideal \((\mathsf Z^2-\mathsf X^3\mathsf Y)\) is preserved.

This note normalizes only the reciprocal monomial \(f=\beta_0/q\)
under the supplied actual full-kernel and square-alternative inputs.
It neither normalizes the nonmonomial family \(f=at+bq\), \(a\ne0\),
nor recognizes or excludes either bare reciprocal alternative.
No square root is asserted to be an original coordinate merely
because it belongs to the coefficient field.
There is no arbitrary-entry, higher-profile, or unrestricted
cancellation conclusion.

The raw coefficient comparisons, exact-field Euler integrations and
actual column changes were independently reconstructed before saving.
No saved checker was executed, imported or compiled; no197 or earlier
source was edited. This is a bounded working proof, not human expert
review, formal certification, historical novelty clearance, or public
submission.
