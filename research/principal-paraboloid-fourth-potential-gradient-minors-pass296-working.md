# A fourth potential and independent gradients in the paraboloid chart

Working result: in the nonzero-coupling actual chart264, the unused
linear Jacobian coefficient integrates to a polynomial potential of
total degree at most four. The evaluated two-by-two minors of the
gradients of this potential and the retained cubic potential generate
the unit ideal of the generic polynomial line.

The proof keeps all three projected generators. It assumes neither
a two-generator plane return nor smoothness of the projected plane.
It supplies no ambient recognition theorem or degree bound by itself.

## 1. Exact actual inputs and notation

Retain the complete actual entry of the fully read
[264](principal-one-affine-paraboloid-chart-pass264-working.md)
and [290](principal-paraboloid-nonzero-coupling-projection-pass290-working.md):
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad
\deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\mathrm{initial}}=(X^2Z-Y^2)\text{ is the full initial kernel},
\quad a=EX\ne0,\\
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,\quad
O=A\otimes_{\ker N}L=L[v],\quad Nv=1,\quad K=L(v),\\
K=\mathbb C(y,z,w),\quad L[y,z,w]=O,\quad
m=k_s\ne0 .
\end{gathered}
\tag{1}
\]
The coefficient partials \(\partial_t,\partial_s\) extend uniquely
to \(L\), commute, and fix \(v\). They preserve \(O=L[v]\).
The literal \(Z\)-partial has exact intrinsic shift four.

Use independent formal variables \(U,P,V\), and put
\[
\begin{aligned}
F(P,V)&=\frac{k_{tt}}2P^2+k_{ts}PV+\frac{k_{ss}}2V^2+n_tP+n_sV,\\
\gamma&=2P+k_t,\qquad
g=\frac{\ell-\gamma U-F}{m},\\
B&=2U+F_P,\quad \lambda=F_V/m,\quad D=\gamma/m,\quad
\beta=B/m .
\end{aligned}
\tag{2}
\]
The symbols \(B,\beta\) here are formal polynomials over \(L\), not
the ambient ring or a previously normalized parameter slope.
Every formal expression is evaluated at \((y,\sigma,\theta)\)
when used in a differential row over \(O\).

The first two potentials and actual map are
\[
\begin{aligned}
z&=2ty+\sigma^2+k_t\sigma+m\theta+n,\qquad
w=g(y,\sigma,\theta),\\
Y&=y+\sigma X+tX^2,\\
Z&=z+(2t\sigma+k)X+t^2X^2,\\
W&=w+\theta X+sX^2,\qquad
J(X)=\det\frac{\partial(Y,Z,W)}{\partial(t,s,v)}
       =-a^4\in L^* .
\end{aligned}
\tag{3}
\]
In particular \(O=L[y,\sigma,\theta]\). This does not say that
the last two functions generate \(O\).

Write \(H\) for264's cubic surface polynomial:
\[
\begin{aligned}
H&=U^2+F_PU+F_Vg+H_3(k;P,V)+H_2(n;P,V)-\ell_tP-\ell_sV,\\
H(y,\sigma,\theta)&=h_0\in L,\\
H_U&=B-\gamma\lambda,\quad
H_P=-m g_t-\lambda B,\quad
H_V=-m g_s-m\lambda^2 .
\end{aligned}
\tag{4}
\]
Here \(H_j\) is the exact homogeneous Taylor expression from264.
The coefficient partials \(g_t,g_s,H_t,H_s\) hold \(U,P,V\)
fixed. They are different from total derivatives after evaluation.

## 2. The all-X row identity and every remaining coefficient

After subtracting \(2t\) times the first actual row from the second,
the three differential rows at fixed \(X\) are
\[
\begin{aligned}
A_X&=dy+X\,d\sigma+X^2dt,\\
B_X&=\gamma\,d\sigma+m\,d\theta+B\,dt+m\lambda\,ds
                       +X(\gamma\,dt+m\,ds),\\
C_X&=dg+X\,d\theta+X^2ds .
\end{aligned}
\tag{5}
\]
Their determinant in the basis \(dt,ds,dv\) is still \(J(X)\).
The total chain rule is
\(dg=-D\,dy-\beta\,d\sigma-\lambda\,d\theta+g_tdt+g_sds\).
It gives the polynomial covector identity
\[
\boxed{
C_X+D A_X-\frac{X-\lambda}{m}B_X
=-\frac1m\{H_U(d\sigma+Xdt)+H_Pdt+H_Vds\}.}
\tag{6}
\]
For example its \(d\sigma\) coefficient is \(-H_U/m\);
its \(dt\) coefficient is \(-(XH_U+H_P)/m\);
and its \(ds\) coefficient is \(-H_V/m\).
No \(d\lambda\) occurs in this row operation. Polynomial evaluation
at \(X=\lambda\) is not differentiation of a moving replacement.

Let \(h_i\) denote the three evaluated partials \(H_U,H_P,H_V\).
Expansion of (6) gives
\[
J(X)=J_0+XJ_1+X^2J_2,\qquad
J_2=H_Uy_v+H_P\sigma_v+H_V\theta_v .
\tag{7}
\]
All higher coefficients cancel before using \(H=h_0\).
The full linear coefficient is
\[
\begin{aligned}
J_1={}&H_U\{(\sigma_t+\theta_s+\lambda)y_v
                         -y_t\sigma_v-y_s\theta_v\}\\
 &+H_P\{y_v+(\theta_s+\lambda)\sigma_v-\sigma_s\theta_v\}\\
 &+H_V\{\sigma_t\theta_v-\sigma_v\theta_t
                         -\beta\sigma_v-Dy_v\}.
\end{aligned}
\tag{8}
\]
Every derivative in (7),(8) fixes the original \(v\) when it is
a coefficient partial. No centered or moving line parameter is
being differentiated as though it were fixed.

There is also a complete constant coefficient. Put
\(\mathcal T=\det(dy,d\sigma,d\theta)\) in the same basis.
Then
\[
\begin{aligned}
J_0&=H_U K_U+H_P K_P+H_V K_V,\\
K_U&=\mathcal T+(\beta y_s-\lambda y_t)\sigma_v
                         +(\lambda\sigma_t-\beta\sigma_s)y_v,\\
K_P&=y_v(\theta_s+D\sigma_s+\lambda)
                         -y_s(\theta_v+D\sigma_v),\\
K_V&=y_t(\theta_v+D\sigma_v)
                         -y_v(\theta_t+D\sigma_t+\beta).
\end{aligned}
\tag{9}
\]
All these coefficients belong to \(O\). Thus the actual nonzero
constant \(J_0=-a^4\) already proves
\[
(H_U,H_P,H_V)\,O=O .
\tag{10}
\]
This recovers290's surface-gradient conclusion without assuming
anything about the projected plane.

To prepare the fourth potential, differentiate the actual level
\(H(y,\sigma,\theta)=h_0\) in \(t,s,v\). In particular \(J_2=0\),
and (8) becomes
\[
\begin{aligned}
J_1={}&(H_P-DH_V)y_v\\
 &+(H_t-h_{0,t}-\beta H_V)\sigma_v\\
 &+(H_s-h_{0,s}-\lambda H_V)\theta_v .
\end{aligned}
\tag{11}
\]
The partials \(H_t,H_s\) on the right remain formal coefficient
partials evaluated afterward. The terms \(h_{0,t},h_{0,s}\) cannot
be dropped.

## 3. The corrected polynomial one-form is closed

The three coefficients in (11) are not generally a closed formal
one-form. Add \(\lambda\,d_{\!f}H\), where \(d_{\!f}\) denotes
differentiation only in \(U,P,V\). This addition evaluates to zero
on the tangent of the actual line because \(J_2=0\).

Define the corrected components
\[
\boxed{
\begin{aligned}
R_U&=H_P-DH_V+\lambda H_U,\\
R_P&=H_t-h_{0,t}-\beta H_V+\lambda H_P,\\
R_V&=H_s-h_{0,s}.
\end{aligned}}
\tag{12}
\]
The last line uses \(g_V=-\lambda\); its two possible
\(\lambda H_V\) terms cancel. Each component lies in \(L[U,P,V]\)
and has total degree at most three.

Here is an exact integrability calculation. The basic formal
identities following from (2) are
\[
\begin{gathered}
g_U=-D,\quad g_P=-\beta,\quad g_V=-\lambda,\\
\gamma_P=B_U=2,\quad \gamma_t=B_P,\quad
\gamma_s=B_V=m_t,\quad
\lambda_P=m_t/m,\quad\lambda_V=m_s/m,\\
\varepsilon:=(F_V)_t-(F_P)_s=0,\qquad
m\lambda_t+m_t\lambda-B_s=\varepsilon .
\end{gathered}
\tag{13}
\]
For the last vanishing equality, both derivatives of \(F\) are
\(k_{tts}P+k_{tss}V+n_{ts}\).
Using (4),(13) and commuting the coefficient derivatives gives
\[
\begin{aligned}
\partial_P R_U-\partial_U R_P&=D\varepsilon=0,\\
\partial_V R_U-\partial_U R_V&=\varepsilon=0,\\
\partial_V R_P-\partial_P R_V&=-\lambda\varepsilon=0.
\end{aligned}
\tag{14}
\]
These are polynomial identities, not identities modulo the
parametrized curve.

For an explicit check of the middle line, (4) gives
\[
\begin{aligned}
H_{PV}&=m\lambda_t-(m_s/m)B-\lambda m_t,\\
H_{VV}&=m\lambda_s-2m_s\lambda,\\
H_{UV}&=m_t-\gamma m_s/m,\\
H_{Us}&=B_s-m_t\lambda-\gamma\lambda_s .
\end{aligned}
\]
Consequently
\(H_{PV}-D H_{VV}+(m_s/m)H_U+\lambda H_{UV}-H_{Us}
=m\lambda_t+m_t\lambda-B_s\).
The first and third lines of (14) follow by the same expansion;
the terms in \(g_{ts}-g_{st}\) cancel. The terms \(h_{0,t},h_{0,s}\)
have no formal \(U,P,V\) derivatives.

The correction is substantive. If \(\alpha\) denotes the
uncorrected form in (11), its first two formal curl entries are
\[
\partial_P\alpha_U-\partial_U\alpha_P=-(m_t/m)H_U,\qquad
\partial_V\alpha_U-\partial_U\alpha_V=-(m_s/m)H_U .
\tag{15}
\]
They need not vanish. The \(\lambda\,d_{\!f}H\) correction is
what cancels them; it does not assume \(m\) constant.

Since the coefficient field has characteristic zero, (14) has
a polynomial primitive. Normalize it by
\[
Q(U,P,V)=
 \int_0^U R_U(\xi,P,V)\,d\xi+
 \int_0^P R_P(0,\pi,V)\,d\pi+
 \int_0^V R_V(0,0,\nu)\,d\nu .
\tag{16}
\]
These are termwise polynomial integrals in independent formal
variables, not integrations in the algebraic field \(L\).
Closedness proves \(Q_U=R_U,Q_P=R_P,Q_V=R_V\), with
\[
Q(0,0,0)=0,\qquad Q\in L[U,P,V],\qquad \deg Q\le4.
\tag{17}
\]

## 4. The fourth level and its original-ring boundary

Under the third level, (11),(12) give exactly
\[
J_1=\frac{d}{dv}Q(y,\sigma,\theta).
\]
The actual full determinant (3) has \(J_1=0\). Since \(Nv=1\)
on \(O=L[v]\), this integrates to
\[
\boxed{Q(y,\sigma,\theta)=q_0,\qquad q_0\in L.}
\tag{18}
\]
Thus the actual curve has two polynomial relations, one of degree
at most three and one of degree at most four. The two relations
have not been identified with generators of the full height-two
kernel. Neither \(Q-q_0\) nor \(H-h_0\) is assumed irreducible.

All constants in (18) belong to the exact field \(L\). The
coefficient derivatives of those constants remain available in
future determinant or compatibility computations. No field-valued
coordinate correction of \(X,Y,Z,W\) is made.

## 5. The actual scalar makes the two gradients independent

All objects in this section are evaluated on the actual line.
Set
\[
\overline B=B_0/m=d\theta+D\,d\sigma+\beta\,dt+\lambda\,ds,
\quad
R_H=H_Ud\sigma+H_Pdt+H_Vds,\quad
R_Q=Q_Ud\sigma+Q_Pdt+Q_Vds.
\tag{19}
\]
Here \(B_0\) is the differential row (5) at \(X=0\), not its
formal polynomial coefficient \(B\).
The total identity \(dH(y,\sigma,\theta)=dh_0\), together with
(12), is precisely
\[
\boxed{H_U\,dy+H_V\,\overline B+R_Q-\lambda R_H=0.}
\tag{20}
\]
For instance its \(dt\) coefficient uses
\(Q_P=H_t-h_{0,t}-\beta H_V+\lambda H_P\);
its \(dv\) coefficient is the already-zero derivative of the
third level.

By (6) at \(X=0\),
\[
J_0=-\det(dy,\overline B,R_H).
\]
Wedging (20) with the indicated rows gives
\[
\boxed{
H_UJ_0=\det(R_H,R_Q,\overline B),\qquad
H_VJ_0=-\det(R_H,R_Q,dy).}
\tag{21}
\]
Both right sides are \(O\)-linear combinations of the three
evaluated minors
\[
M_{UP}=H_UQ_P-H_PQ_U,\quad
M_{UV}=H_UQ_V-H_VQ_U,\quad
M_{PV}=H_PQ_V-H_VQ_P .
\tag{22}
\]
Let \(I\) be their ideal in \(O\). Because \(J_0\in L^*\),
equations (21) give \(H_U,H_V\in I\).
The first equation of (12) also gives the exact algebraic identity
\[
H_P^2
 =H_U(Q_P-\lambda H_P)+D H_PH_V-M_{UP}\in I .
\tag{23}
\]
By (10), choose \(c_U,c_P,c_V\in O\) with
\(c_UH_U+c_PH_P+c_VH_V=1\). Modulo \(I\), this says
\(c_PH_P=1\), whose square is zero by (23).
Therefore
\[
\boxed{(M_{UP},M_{UV},M_{PV})\,O=O.}
\tag{24}
\]
No division by an evaluated gradient component is used.

There is an independent all-X version of the same argument.
Expanding (20) and the first equation of (12) proves
\[
\begin{aligned}
H_UA_X+(H_V/m)B_X
={}&((X+\lambda)H_U-Q_U)(d\sigma+Xdt)\\
 &+((X+\lambda)H_P-Q_P)dt\\
 &+((X+\lambda)H_V-Q_V)ds .
\end{aligned}
\tag{25}
\]
If all three minors vanished modulo an irreducible polynomial
of \(O=L[v]\), the nonzero first gradient in that residue field
would make the second a scalar multiple, say \(q=\rho h\).
Evaluate the polynomial identity (25) at \(X=\rho-\lambda\).
Its right side is zero. Moreover \(H_U,H_V\) cannot both vanish:
the first equation of (12) would then give \(Q_U=H_P\), contrary
to a nonzero first gradient and \(q=\rho h\).
Thus the first two determinant rows would be dependent, contradicting
\(J(X)=-a^4\). This argument needs no lift of \(\rho\) to \(O\);
it is polynomial evaluation after passing to the residue field.

In particular \(H-h_0\) and \(Q-q_0\) cannot share a polynomial
factor that vanishes identically on the actual line. If such a
factor \(G\) existed, both evaluated gradients would be scalar
multiples of the evaluated gradient of \(G\), making every
minor zero. This does not exclude common factors disjoint from
the actual curve, and does not assert a global complete-intersection
description of its entire ideal.

## 6. The quadratic U structure and precise scope

Write \(H=U^2+A_1(P,V)U+A_0(P,V)\), with
\(\deg A_1\le2,\deg A_0\le3\).
The first equation of (12) is at most linear in \(U\).
More explicitly,
\[
Q_{UU}=k_{tt}-2D m_t+D^2m_s,\qquad
Q=e(P)U^2+L_1(P,V)U+L_0(P,V),
\quad
e=\frac{k_{tt}-2D m_t+D^2m_s}{2}.
\tag{26}
\]
The coefficient \(e\) has degree at most two in \(P\).
This follows from
\(A_{1,P}=k_{tt}-2\lambda-\gamma m_t/m\) and
\(A_{1,V}=m_t-\gamma m_s/m\), with
\(Q_{UU}=A_{1,P}-D A_{1,V}+2\lambda\).

Division by the monic third relation therefore has the exact form
\[
Q-q_0-e(H-h_0)=R_1(P,V)U+R_0(P,V),\qquad
\deg R_1\le4,\quad \deg R_0\le5 .
\tag{27}
\]
No assertion about their projected-plane divisibility is needed
or made here. That depends on the separate projection-degree
cases of290.

The new conclusions are the complete remaining determinant
coefficients, the closed corrected form, the quartic level,
and the unit ideal of the two evaluated gradients' minors.
They keep the original three-generator return and exact finite
coefficient field. No plane-return equality, conductor bound,
Bezout degree bound, actual coordinate recognition, arbitrary
entry statement or unrestricted cancellation result is claimed.

The complete264 and290 sources were read before this reconstruction.
Fresh unsaved generic-jet algebra checked (6)--(11), all three
closedness identities, the covector and wedge identities, and the
quadratic-U coefficient. The human arguments above, not finite
samples, establish closedness and the minor-unit conclusion.
No saved checker was executed, imported, compiled or rerun.
No earlier source, index or packet was edited.
No novelty, human-expert or proof-assistant certification is asserted.

