# An affine intercept forces reciprocal coupling in the degree-drop chart

Working bounded result: retain the FULL actual principal chart264,
the genuine potentials and unit minors of296, and the unrestricted
unit-multiplier lemma494. Suppose
\[
\begin{gathered}
P=\sigma,\qquad \deg_v\sigma=1,\qquad
\theta=-P^2/m+bP+c,\\
m=k_s\ne0,\qquad m_s=0,\qquad m\notin\mathbb C,\qquad
y=lP+r.
\end{gathered}
\tag{1}
\]
Thus the quadratic coefficient e of y is zero, and
\(\delta=1+m[P^2]\theta=0\). Then
\[
\boxed{\frac1m=Bt+D,\qquad B\in\mathbb C^*,\quad
D\in\mathbb C,\quad l\in\mathbb C.}
\tag{2}
\]
An explicit actual complex polynomial reframe consequently gives
\[
\boxed{m^*=1/t^*,\qquad y^*\in L,\qquad
\theta^*=-t^*(P^*)^2+b^*P^*+c^*.}
\tag{3}
\]
This is a necessary coefficient reduction and an actual normalization,
not an exclusion or recognition theorem for the remaining lower
equations. It asserts no result for the e nonzero branch, arbitrary
projected curves, or unrestricted cancellation.

## 1. Full actual hypotheses and exact coefficient fields

Retain EVERY actual hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md) and
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md).
In particular,
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u_{\rm glob}],\qquad
E=\partial_{u_{\rm glob}},\quad X=a_0u_{\rm glob}+x_0,\quad a_0\ne0,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\qquad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the ENTIRE initial kernel},\\
0\ne N=[u_{\rm glob}^4]\partial_Z|_A,\qquad
L=\operatorname{Frac}\ker_A N,\qquad [L:\mathbb C(t,s)]<\infty,\\
Na_0=Nt=Ns=0,\quad Nv=1,\quad
O=L[v]=L[y,z_0,w]=L[y,\sigma,\theta],\\
\operatorname{Frac}A=L(v)=\mathbb C(y,z_0,w).
\end{gathered}
\tag{4}
\]
The original slice, literal selected partial and both actual returns
are retained. The coefficient partials commute and have joint
constants C. The original intercept w in (4) is distinct from the
cubic leader denoted omega below.

Set \(F_0=\ker_L\partial_s\). This is a finite extension of C(t),
not necessarily C(t). Indeed an element of F0 has a monic minimal
polynomial over C(t,s). Differentiating it in s gives a relation of
smaller degree, so all its coefficients lie in C(t). The degrees of
the resulting constant subextensions are bounded by
\([L:\mathbb C(t,s)]\); the finite primitive-element argument then
gives finiteness of F0. The exact t derivative on F0 has constants C
by the joint-constant statement. Primes below denote this derivative.

Because m belongs to F0 and is not complex,
\[
p=m'\ne0,\qquad q=m'',\qquad j=m'''
\tag{5}
\]
are legitimate coefficient elements; q and j may vanish.
Affine sigma gives
\[
O=L[P],\qquad NP=\rho\in L^*,\qquad
J_{t,s,P}(X)=-a_0^4/\rho\in L^*.
\tag{6}
\]
The coefficient derivatives are extended to fix P in the literal
determinant. No assertion \(NP=1\) or that the scalar is a complex
constant is made.

The literal rows needed throughout are
\[
\begin{aligned}
Y&=y+PX+tX^2,\\
Z&=2ty+P^2+k_tP+m\theta+n+(2tP+k)X+t^2X^2,\\
W&=w+\theta X+sX^2,\\
mw&=\ell-(2P+k_t)y-F(P,\theta),\\
F(P,V)&=k_{tt}P^2/2+pPV+n_tP+n_sV.
\end{aligned}
\tag{7}
\]
All lower functions and their moving derivatives remain present.

## 2. Raw genuine-H and scalar coefficients

The held surrounding reduction
[512](principal-paraboloid-degree-drop-univariate-coupling-reduction-pass512-working.md)
has been read through EOF. We nevertheless print and independently
verify the exact raw identities needed for this branch.

For independent formal U,P,V, the genuine monic polynomial is
\[
\begin{aligned}
G&=\{\ell-(2P+k_t)U-F(P,V)\}/m,\\
H&=U^2+F_PU+F_VG+k_{ttt}P^3/6+qP^2V/2\\
 &\hspace{12mm}+n_{tt}P^2/2+n_{ts}PV+n_{ss}V^2/2
                       -\ell_tP-\ell_sV.
\end{aligned}
\tag{8}
\]
Both levels \(H(y,P,\theta)=h_0\) and
\(Q(y,P,\theta)=q_0\) of296 are retained in L.
The monic coefficients of H after quadratic theta have P degrees
at most two and four. Thus y has degree at most two without using
327's inapplicable quadratic-level parity. Assumption (1) selects
exactly its zero-quadratic-coefficient branch.

The coefficient of \(P^4\) in the actual H level is
\((n_{ss}-mq+2p^2)/(2m^2)\). Hence, by exact subtraction in s,
\[
\begin{aligned}
N_2&=mq-2p^2,\qquad
k=ms+f_0,\qquad n=N_2s^2/2+n_1s+n_0,\\
f_0,n_1,n_0&\in F_0.
\end{aligned}
\tag{9}
\]
No rationality is used in these integrations.

Use only Sections1--3 of
[494](principal-paraboloid-unit-tangent-multiplier-pass494-working.md).
Put \(f_H=H_U^{\rm ev}\), \(g_H=H_V^{\rm ev}\), and
\[
\begin{aligned}
\nu&=(pP+n_s)/m,\quad
\beta_f=(2y+F_P(P,\theta))/m,\quad D_f=(2P+k_t)/m,\\
\mathcal A&=y_t+\theta_Py_s+y_P^2,\\
\mathcal B_1&=\theta_t+
\theta_P(y_P+\theta_s+\nu)+\beta_f+D_fy_P.
\end{aligned}
\tag{10}
\]
That unrestricted lemma gives \(\mathcal A=\kappa g_H\) and
\(\mathcal B_1=-\kappa f_H\), where \(\kappa\in L^*\).
The unit uses the entire constant scalar and the genuine unit
tangent minor, not merely a highest-degree formal relation.

Direct extraction from (8)--(10), retaining all lower jets, gives
\[
\begin{aligned}
F_2:=[P^2]f_H&=-3p/m,\qquad
G_2:=[P^2]g_H=p^2/m-q/2,\\
[P^2]\mathcal A&=-2l_s/m=\kappa G_2,\\
[P^2]\mathcal B_1&=-2(p+mb_s)/m^2=-\kappa F_2.
\end{aligned}
\tag{11}
\]
Consequently the EXISTING coefficient
\(\epsilon=k_t+mb\) satisfies
\[
\epsilon_s=-3\kappa mp/2\ne0,\qquad
l_s=\kappa(mq/4-p^2/2).
\tag{12}
\]
The zero possibility for epsilon was not divided away: its
nonzero derivative is now a consequence of the full scalar.

For completeness the ENTIRE cubic H coefficient after (9) is
\[
\begin{aligned}
[P^3]H(y,P,\theta)&=F_2l+G_2b+E_0s+C_0=0,\\
E_0&=-5j/6+9pq/(2m)-4p^3/m^2,\\
C_0&=-pf_0''/(2m)+2pn_1/m^2-n_1'/m+f_0'''/6\in F_0.
\end{aligned}
\tag{13}
\]
Differentiate (13) in s. Substitute both equations (11), so the
terms containing kappa cancel exactly. The full resulting identity is
\[
0=-\frac5{6m^2}(m^2j-6mpq+6p^3),\qquad
\boxed{(1/m)'''=0.}
\tag{14}
\]
The last equality uses
\(m^2j-6mpq+6p^3=-m^4(1/m)'''\). No value of q, G2 or a
lower coefficient was divided in this calculation.

## 3. A separating lower coefficient and actual Delta leaders

Dividing the two equations (12) by the known nonzero factors gives
\[
l=\alpha\epsilon+L_0,\qquad
\alpha=\frac{2p^2-mq}{6mp}\in F_0,\qquad L_0\in F_0.
\tag{15}
\]
Here exact subtraction proves the assertion about L0. Since
epsilon_s is nonzero, epsilon is transcendental over F0 and
\((t,\epsilon)\) is a separating coefficient basis. Explicitly,
\[
\partial_\epsilon|_t=\epsilon_s^{-1}\partial_s,\qquad
\partial_t|_\epsilon=\partial_t|_s-
                         (\epsilon_t/\epsilon_s)\partial_s.
\tag{16}
\]
These commute on the exact finite extension
\(L/\mathbb C(t,\epsilon)\). The new t derivative restricts to the
original t derivative on F0, while the epsilon derivative kills F0.
There is no assertion \(L=F_0(\epsilon)\).

Extend the original N to the actual \(A[u_{\rm glob}]\) by
\(Nu_{\rm glob}=0\), and define
\[
\Delta=a_0N-(NX)E.
\tag{17}
\]
This is polynomial on the actual four-ring and fixes X.
Indeed \(NX=Nx_0\in A\). On its literal polynomial overring
\(L[X,P]\), it kills L and equals
\(a_0\rho\,\partial_P|_X\). Thus Delta is locally nilpotent
on the actual ring; this does not assume that an arbitrary
difference of LNDs is locally nilpotent.

Because X is an actual fixed coordinate, localize to the actual
polynomial three-ring
\[
R_X=\mathbb C(X)[Y,Z,W]=\mathbb C(X)^{[3]}.
\tag{18}
\]
Directly from (7),(1), its exact Delta-degree profile is (1,1,3),
with ordinary P leaders
\[
\Lambda=X+l=X+\alpha\epsilon+L_0,\qquad
2t\Lambda+\epsilon,\qquad \omega=p/m^2\ne0.
\tag{19}
\]
The first two are nonzero as polynomials in the independent actual
X: their X coefficients are 1 and \(2t\ne0\). The cubic W
leader follows from the \(pP\theta\) term in F, including its sign.
The term theta X in W does not change it.

For later comparison, this nonzero LND has kernel fraction field
of transcendence degree two over \(k_X=\mathbb C(X)\).
One can see this without classification: \(\Delta Y\ne0\) is
invariant and \(\Delta^2Y=0\). After inverting Delta Y, the
element \(Y/(\Delta Y)\) is a slice, and finite Taylor projection
writes the localization as a polynomial ring over its kernel.

## 4. The initial map forces a zero wedge

The two weight-zero initial ratios in profile (1,1,3) are
\[
\mathscr R=2t+\epsilon/\Lambda,\qquad
\mathscr S=\omega/\Lambda^3.
\tag{20}
\]
The speed factors \((a_0\rho)^d\) cancel in both ratios.
If these two elements were algebraically independent over kX,
the weighted initial map
\[
k_X[\mathsf Y,\mathsf Z,\mathsf W]\longrightarrow L(X)[\Xi],
\qquad
(\mathsf Y,\mathsf Z,\mathsf W)\longmapsto
(g\Lambda\Xi,\ g(2t\Lambda+\epsilon)\Xi,
                                    g^3\omega\Xi^3),
\quad g=a_0\rho
\tag{21}
\]
would be injective. Indeed its image fraction field is generated
by the two ratios and \(g\Lambda\Xi\), the last element being
transcendental over L(X). Every nonconstant polynomial in the
actual coordinates Y,Z,W would then retain a nonzero top component
of positive weight, and hence have positive Delta-degree. This
would give \(\ker_{R_X}\Delta=k_X\), contradicting the local-slice
conclusion above. This argument concerns an actual polynomial
three-ring, not an arbitrary coefficient-field parametrization.

Therefore the ratios are algebraically dependent. Differentiating
in the exact basis (16), fixing X, forces their Jacobian to be zero.
The complete quotient calculation is
\[
\det\frac{\partial(\mathscr R,\mathscr S)}{\partial(t,\epsilon)}
 =\frac{-6\omega\alpha\Lambda-(X+L_0)\omega'
                 +3\omega(\alpha'\epsilon+L_0')}{\Lambda^5}=0.
\tag{22}
\]
All lower-coefficient derivatives are retained. The existing omega
in (19) satisfies
\[
\alpha=-\omega'/(6\omega).
\tag{23}
\]
Substitution reduces the numerator in (22) exactly to
\(3\omega\{(\alpha'-2\alpha^2)\epsilon+L_0'\}\).
Epsilon is transcendental over F0, so
\[
\alpha'=2\alpha^2,\qquad L_0'=0.
\tag{24}
\]
In particular \(L_0\in\mathbb C\). There is no differentiation
or specialization at a root of Lambda.

## 5. The nonzero-alpha alternative contradicts the full H gate

Suppose first \(\alpha\ne0\). The existing element
\(T=-1/(2\alpha)\in F_0\) satisfies T'=1 by (24), so
\(T=t-\tau\) with \(\tau\in\mathbb C\). Equations (23),(24)
give \(\omega'/\omega=3/T\), hence
\[
\omega=C T^3,\qquad C\in\mathbb C^*.
\tag{25}
\]
This integration is exact subtraction or division inside F0:
\((\omega/T^3)'=0\). No rationality is assumed. But
\((1/m)'=-\omega\), so (14) requires \(\omega''=0\), whereas
(25) gives \(\omega''=6CT\ne0\). This is impossible.

Thus alpha=0. Equations (23),(24) give omega in C* and L0 in C.
Equation (15) gives l=L0, and exact integration of
\((1/m)'=-\omega\) gives (2), with \(B=-\omega\ne0\).
The zero-alpha case was not discarded or inferred by division.

## 6. A verified actual complex normalization

Now set \(\tau=D/B\) and denote the proved complex number l by
\(c_l\). Use the actual composite polynomial map
\[
\begin{aligned}
X^*&=X+c_l,\\
Y^*&=Y+\tau X^2,\\
Z^*&=Z+2\tau Y+\tau^2X^2,\\
W^*&=W/B.
\end{aligned}
\tag{26}
\]
The W scaling and time shift can be performed first, followed by
the X translation. Every coefficient is complex. Its full inverse is
\[
\begin{aligned}
X&=X^*-c_l,\\
Y&=Y^*-\tau(X^*-c_l)^2,\\
Z&=Z^*-2\tau Y^*+\tau^2(X^*-c_l)^2,\\
W&=B W^*.
\end{aligned}
\tag{27}
\]
Both compositions are polynomial identities.

These maps belong to the fully licensed filtered class of
[426](general-coupling-normalization-obstruction-pass426-working.md).
For explicit transport in this case, expanding the original rows gives
\[
\begin{aligned}
t^*&=t+\tau,\qquad s^*=s/B,\qquad a_0^*=a_0,\\
P^*&=P-2c_l(t+\tau),\qquad \rho^*=NP^*=\rho,\\
y^*&=r+c_l^2(t+\tau)\in L,\\
\theta^*&=\theta/B-2c_ls/B,\\
k^*&=k+2c_l(t+\tau)^2,\qquad m^*=Bm=1/t^*.
\end{aligned}
\tag{28}
\]
The theta formula is first a pullback in the old P; substituting
\(P=P^*+2c_lt^*\) shows its quadratic coefficient is
\((-1/m)/B=-t^*\). Therefore delta remains zero, while both the
quadratic and linear intrinsic coefficients of y* vanish. No
coefficient-field element was used as an ambient map parameter.

Here are all retained actual-chart licenses. The time shift obeys
\(X^2Z_1-Y_1^2=X^2Z-Y^2\) exactly. The final X translation has
the same leading X, and the W scaling is invertible. Thus the
invertible weighted leading map preserves the ENTIRE initial
kernel, not just one relation. Exact E-degrees remain (1,2,2,2):
the transformed coefficient ratios \(t+\tau,s/B\) are independent.
The original global slice and kernel A are unchanged.

The inverse (27) has Z*-column exactly \((0,0,1,0)\), so
\(\partial_{Z^*}=\partial_Z\) and the selected N and exact field L
are unchanged. Since P* differs from P by an element of L,
\(L[P^*]=O\). For the strong actual return,426's actual quotient
argument applies: \(\mathcal B_{a_0}=A_{a_0}[X^*]\), and evaluating
the actual starred frame at X*=0 gives both
\(\operatorname{Frac}A=\mathbb C(y^*,z_0^*,w^*)\) and
\(L[y^*,z_0^*,w^*]=O\). The denominator a0 after evaluation is
itself a polynomial in the starred intercepts. This is not merely
an affine change over L offered as proof of the complex-field return.

Finally the bad-row determinant at fixed X* is 1/B, and the exact
parameter determinant of \((t^*,s^*,P^*)\) with respect to
\((t,s,P)\) is also 1/B. Thus the entire scalar is transported as
\[
J^*_{t^*,s^*,P^*}(X^*)
 =J_{t,s,P}(X^*-c_l)=-a_0^4/\rho.
\tag{29}
\]
The genuine new levels and potentials come from this actual new
chart; they are not independently prescribed formal functions.
This completes the normalization (3), with every actual264 gate
preserved.

## 7. Verification and exact scope

Fresh unsaved a4ecb7 reconstructed the full H4 and H3 coefficients,
both formal-gradient leaders, both scalar leaders, the cubic W
leader and the reciprocal-third-derivative identity. All final
residuals were zero. Fresh482d29 reconstructed the full quotient
wedge and its reduction. The actual initial-map and local-slice
argument was independently checked against the complete source495,
without importing that note's nonzero-delta hypotheses or conclusion.

Fresh f0fc08 verified both complete inverse compositions of
(26),(27), the full time-shift initial relation, the transported
Y/coupling/theta coefficients, the selected-partial inverse column,
and both determinant factors. The complete source426 was reread
through EOF for its actual-return and filtered-frame licenses.
No saved checker was executed, imported, compiled or modified.

The dependencies264/296 and universal494 Sections1--3 remain
retained inputs, not recursively certified results. The necessary
raw coefficient chain of the now-held512 investigation is
proved explicitly here. Neither327 parity nor any reducible-H
constraint is used. No later two-quasi classification, exclusion
of this normalized family, or ambient recognition is claimed.
