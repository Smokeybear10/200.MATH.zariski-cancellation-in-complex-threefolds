# Exclusion of the remaining transverse cubic-excess branch

Working exclusion in a supplied actual chart: retain the FULL
264/296/535 hypotheses and the transverse h nonzero, v1=0
cubic-excess family554. Its noncomplex-T0 sector557 is impossible.
The proof is an exact identity between two complete multiplier
coefficients, the genuine second-potential coefficient, its genuine
s derivative, and the complete H7 equation. It forces
\[
\boxed{0=r\kappa\ne0.}
\tag{1}
\]

No condition on the quartic pair coefficient U4 or on either delta
branch is used. In particular the conic-field classification563,
actual normalization564 and pair-boundary restriction567 are not
dependencies.
Combined with the separately held complex-T0 exclusion558, this
excludes the specified ENTIRE v1=0 transverse cubic-excess family.
It does not exclude v1 nonzero, h=0, other intrinsic degrees, or
an arbitrary actual chart, and it supplies no general entry theorem.

## 1. Full actual input and precise intrinsic sector

Retain every hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md)
and
[535](principal-paraboloid-nonlinear-sigma-unit-multiplier-pass535-working.md).
In particular
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=\mathcal A[u_{\rm glob}],\qquad
E=\partial_{u_{\rm glob}},\qquad
X=a_0u_{\rm glob}+x_0,\quad a_0\ne0,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\qquad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the ENTIRE original initial kernel},\\
0\ne N=[u_{\rm glob}^4]\partial_Z|_{\mathcal A},\qquad
Na_0=Nt=Ns=0,\qquad Nv=1,\\
L=\operatorname{Frac}\ker_{\mathcal A}N,\qquad
[L:\mathbb C(t,s)]<\infty,\qquad
L[\mathcal A]=L[v]=L[y,\sigma,\theta],\\
\operatorname{Frac}\mathcal A=L(v)=\mathbb C(y,z_{\rm int},w),
\qquad L[y,z_{\rm int},w]=L[v],\qquad m=k_s\notin\mathbb C .
\end{gathered}
\tag{2}
\]
The intercept z_int is the literal original Z-intercept.
The original global slice, selected actual partial, both returns,
genuine third and fourth levels and FULL scalar remain required.

Use precisely the finite intrinsic normalization and v1=0
transverse branch of
[554](principal-paraboloid-cubic-excess-leading-families-pass554-working.md).
In L'=L(rho), with x affine in the original v, write
\[
\begin{gathered}
Nx=\rho\in(L')^*,\qquad \sigma=x^2+c,\qquad
\theta=ax^3+bx^2+dx+e,\\
y=rx^4+qx^3+y_2x^2+y_1x+y_0,\qquad
F_0=\ker_{L'}\partial_s,\\
a,r,h\in F_0^*,\qquad h=m_s=-4r/a^2,\qquad
m=hs+m_0,\quad m_0\in F_0,\quad p=m_t,\\
v_1=(ha^2+4r)/m=0,\qquad T_0=2t+1/r\notin\mathbb C .
\end{gathered}
\tag{3}
\]
The symbols b and q here are b2 and q3 in554/557, not constant
normalization parameters. Every lower coefficient c,d,e,y2,y1,y0
is retained. None is assumed zero or nonzero.

F0 is finite over C(t), not assumed rational. The coefficient
partials are the exact commuting extensions from C(t,s), extended
to fix x. They include the original moving-center and moving-scale
effects. In particular h_s=a_s=r_s=0, and p_s=h_t.
The intrinsic parameter x is not promoted to an ambient coordinate.

### Direct moving-parameter license

For clarity, let x=rho*v+mu in the finite coefficient extension,
and put chi_t=(partial_t x)|v and chi_s=(partial_s x)|v. For each
intrinsic polynomial f the exact chain rule is
\[
f_t|_v=f_t|_x+f_x\chi_t,\qquad
f_s|_v=f_s|_x+f_x\chi_s,\qquad f_v=\rho f_x .
\tag{4}
\]
Substitute these into the ENTIRE535 expressions for A_beta and
B_beta printed in (8) below. Every chi_t and chi_s term cancels.
For example beta squared*y_t and minus beta*sigma_t*y_v cancel
their chi_t contributions in A_beta; its two s terms cancel
their chi_s contributions. The same paired cancellations hold in
B_beta. Thus
\[
(\mathcal A_\beta)_{\rm old}=\rho^2(\mathcal A_\beta)_x,\qquad
(\mathcal B_\beta)_{\rm old}=\rho^2(\mathcal B_\beta)_x,\qquad
\kappa=\kappa_{\rm old}/\rho^2\in(L')^* .
\tag{5}
\]
The formal H derivatives are taken before evaluation and are the
same field expressions. The scalar becomes -a0 to the fourth/rho.
This directly licenses fixed-x differentiation; no constant-speed
assumption on rho or discarded moving derivative is used.

## 2. Whole rows, formal H and the two unit-multiplier equations

The actual rows and entire second potential are
\[
\begin{aligned}
Y&=y+\sigma X+tX^2,\\
Z&=2ty+\sigma^2+k_t\sigma+m\theta+\mathfrak n
                                  +(2t\sigma+k)X+t^2X^2,\\
W&=w+\theta X+sX^2,\\
mw&=\ell-(2\sigma+k_t)y-\mathcal F(\sigma,\theta),\\
\mathcal F(P,V)&=k_2P^2/2+pPV+hV^2/2
                         +\mathfrak n_tP+\mathfrak n_sV,\qquad
 k_1=k_t,\quad k_2=k_{tt},\\
J_{t,s,x}(Y,Z,W)&=-a_0^4/\rho\in(L')^* .
\end{aligned}
\tag{6}
\]
The scalar has no X or x dependence, but is not assumed constant
under coefficient differentiation.

For independent formal U,P,V, retain the genuine third polynomial
\[
\begin{aligned}
\mathcal G&=\{\ell-(2P+k_1)U-\mathcal F(P,V)\}/m,\\
H={}&U^2+\mathcal F_PU+\mathcal F_V\mathcal G
 +k_{ttt}P^3/6+p_tP^2V/2+h_tPV^2/2+h_sV^3/6\\
&+\mathfrak n_{tt}P^2/2+\mathfrak n_{ts}PV
                  +\mathfrak n_{ss}V^2/2-\ell_tP-\ell_sV,\\
H(y,\sigma,\theta)&=h_0\in L',\qquad
f=H_U^{\rm ev},\quad g=H_V^{\rm ev}.
\end{aligned}
\tag{7}
\]
Every formal derivative is taken BEFORE substituting(y,sigma,theta).
The genuine fourth level and the full minor-unit hypotheses of296
are retained through535, not replaced by assumed coprimality of f,g.

Set beta=2x, nu=(p*sigma+h*theta+n_s)/m,
B_f=(2y+k2*sigma+p*theta+n_t)/m and D_f=(2sigma+k1)/m.
The entire cleared equations of535, with the convention (5), are
\[
\begin{aligned}
\mathcal A_\beta&=4x^2y_t+2x\theta_xy_s+y_x^2
                              -2xc_ty_x-c_sy_x\theta_x=\kappa g,\\
\mathcal B_\beta&=4x^2(\theta_t+B_f)+2xD_fy_x+y_x\theta_x
                   +2x(\theta_s+\nu-c_t)\theta_x-c_s\theta_x^2
                   =-\kappa f .
\end{aligned}
\tag{8}
\]
Define residuals Ares=A_beta-kappa*g and
Bres=B_beta+kappa*f. They vanish as ENTIRE polynomials.
No division by beta occurs, so its critical point x=0 is retained.

## 3. Retained complete high gates and genuine derivative ledger

Let wi=[x^i]w and put o=w4. The noncomplex-T0 hypothesis in (3)
licenses exactly the conclusions of
[556](principal-paraboloid-cubic-transverse-degree-profile-restriction-pass556-working.md)
and
[557](principal-paraboloid-cubic-transverse-conic-and-differential-restriction-pass557-working.md):
\[
w_5=0,\qquad o\ne0,\qquad o_s=0 .
\tag{9}
\]
In particular o_s=0 comes from the FULL actual initial-kernel
argument, not from a rationality assumption or a formal leading-data
ansatz.

For reference, expansion of the entire second potential in (6)
gives
\[
\begin{aligned}
w_6&=-\{2r+ha^2/2\}/m=0,\\
w_5&=-\{2q+a(p+hb)\}/m=0,\\
mo&=-\{2y_2+(2c+k_1)r+pb+h(ad+b^2/2)+k_2/2\}.
\end{aligned}
\tag{10}
\]
The complete H8 and H7 expressions from557 are
\[
\begin{aligned}
0&=a^4h^2/16+ahw_5+a^2h_t/2,\\
[x^7](H-h_0)
 &=aho+ab(h_t+a^2h^2/4)
          +w_5(a^2hm/4+hb+p)+ap_t/2 .
\end{aligned}
\tag{11}
\]
With w5=0 these give
\[
h_t=rh/2\ne0,\qquad
q=-a(p+hb)/2,\qquad o=rb/2-p_t/(2h).
\tag{12}
\]
This retains arbitrary p_t. In particular no assumption m_tt=0
has been made.

Put j=h_tt/h_t, a well-defined element of F0. Differentiating
the exact relations r=2h_t/h and a squared=-4r/h in t gives
r_t=rj-r squared/2 and a_t=a(j-r)/2. Differentiating the last
identity in (12) by s, using o_s=h_s=r_s=0 and (p_t)_s=h_tt,
gives b_s=j/2. The full fifth multiplier coefficient557(22) is
4a_t+6ab_s-3a cubed*h-2kappa*h*a/m=0. Therefore the complete
ledger needed below is
\[
\begin{gathered}
a^2h=-4r,\quad h_s=a_s=r_s=0,\quad
h_t=p_s=rh/2,\quad k_{1,s}=p,\quad k_{2,s}=p_t,\\
r_t=rj-r^2/2,\qquad a_t=a(j-r)/2,\qquad b_s=j/2,\\
q=-a(p+hb)/2,\qquad
q_s=-ah(r+j)/4,\\
q_t=-\{a_t(p+hb)+a(p_t+h_tb+hb_t)\}/2,\\
\kappa=\frac{5m}{2h}(j+2r)\ne0 .
\end{gathered}
\tag{13}
\]
Thus j+2r is nonzero, but j, b, b_t, q and p_t are not
individually divided by or assumed nonzero. The derivative b_t
remains free subject to the genuine full equations. No U4, delta,
conic-field classification or normalizing shear has been used.

## 4. Universal raw coefficients A5 and B4

Write A5=[x5]Ares and B4=[x4]Bres. To make their full pedigree
explicit, differentiating (7) formally gives
\[
\begin{aligned}
H_U={}&2U+k_2P+pV+\mathfrak n_t
                 -(2P+k_1)(pP+hV+\mathfrak n_s)/m,\\
H_V={}&\{p-h(2P+k_1)/m\}U
                  +C_1(P)+2C_2(P)V-\frac{3h^2}{2m}V^2,\\
C_2(P)={}&(h_t-3hp/m)P/2
                       +(\mathfrak n_{ss}-3h\mathfrak n_s/m)/2,\\
C_1(P)={}&(p_t/2-hk_2/(2m)-p^2/m)P^2\\
 &+(\mathfrak n_{ts}-h\mathfrak n_t/m
                       -2p\mathfrak n_s/m)P\\
 &+h\ell/m-\mathfrak n_s^2/m-\ell_s .
\end{aligned}
\tag{14}
\]
Only the proved h_s=0 was used in the last term of H_V.
All lower potential coefficients remain visible. In particular
\[
f_4:= [x^4]f=2r-\frac{2(p+hb)}m,\qquad
g_5:= [x^5]g=\frac{ahr}{2}-\frac{2ah(p+hb)}m .
\tag{15}
\]
For example g5 before using q in (13) is
-2hq/m-3h squared*a*b/m+a*h_t-3ahp/m;
substituting q and h_t gives (15).

The ENTIRE coefficients of (8), before eliminating y2 or its
derivative, are
\[
\begin{aligned}
A_5={}&4q_t+6a(y_2)_s+4bq_s+24rq-12arc_s-\kappa g_5,\\
B_4={}&4b_t+
 \{16y_2+4k_2+8r(2c+k_1)+8pb+8ahd+4hb^2\}/m\\
 &+8rb+9aq+4bb_s+6ad_s-9a^2c_s+\kappa f_4 .
\end{aligned}
\tag{16}
\]
Each term can be read directly from (8). In A5, respectively,
the five non-multiplier contributions are
4q_t, 6a(y2)_s+4bq_s, 24rq, zero, and -12ar*c_s.
For B4, the fractional terms combine the full B_f, D_f and nu
contributions. Their complete sum is printed in (16);
no n_s, e or y1 term contributes at this exact degree.
Their absence in (16) is a degree computation from the whole
polynomials, not an assumption that those functions or their jets
vanish. There is no finite-degree sampling argument.

One useful expanded check on (16), using (13),(15), is
\[
\frac{A_5}{a}
 =6(y_2)_s-12rc_s-2p_t-2hb_t
      +(4j-r)p+3hb(j-r)-\frac{\kappa hr}{2}.
\tag{17}
\]
Every derivative in this formula is genuine and holds x fixed.

## 5. A single exact coefficient certificate

Define
\[
\begin{aligned}
E_W&=mo+2y_2+(2c+k_1)r+pb+h(ad+b^2/2)+k_2/2,\\
E_s&=\partial_s E_W,\\
E_7&=o-rb/2+p_t/(2h).
\end{aligned}
\tag{18}
\]
Equations (10),(12) imply EW=E7=0, and the derivative of the
identically zero EW is zero. It is essential that Es is taken
with o_s=0 from (9) and with the genuine dependencies in (13);
neither the potential coefficients nor b are frozen.

For an explicit full derivative, put zeta=p+hb. Then
\[
\begin{aligned}
E_s={}&ho+2(y_2)_s+2rc_s+rp+h_tb+pb_s
                                      +ha d_s+hb b_s+p_t/2\\
 ={}&2(y_2)_s+2rc_s+ha d_s+hE_7+(r+j/2)\zeta .
\end{aligned}
\tag{19}
\]
The whole B4 formula in (16) also reads
\[
B_4=\frac{8E_W}{m}+4b_t-8o
                 +(8r+4b_s)b+9aq+6ad_s-9a^2c_s+\kappa f_4 .
\tag{20}
\]
Substitute (13),(15),(17),(19) into (20).
The coefficients of(y2)_s, c_s, d_s, b_t, p_t, b and p all
cancel in the following EXACT identity:
\[
\boxed{
B_4-\frac{8E_W}{m}+\frac{2A_5}{ah}
          -\frac{6E_s}{h}+14E_7
 =r\kappa
 =\frac{5mr(j+2r)}{2h}
 =-\frac{5a^2m(j+2r)}8 .}
\tag{21}
\]
This is an algebraic identity in the full unsolved coefficient
ledger, not a substitution into a proposed leading-data example.

If desired, its denominators involving a,h,m can be cleared:
\[
\boxed{
2mah B_4-16ah E_W+4m A_5-12ma E_s+28mah E_7
                           =2mah\,r\kappa .}
\tag{22}
\]
Every multiplier of a residual here is an existing coefficient
field element. All the divisions in (21) are already licensed
by a,h,m nonzero. Neither formula divides by j, q, a lower
coefficient, a pair discriminant, U4 or a conic coefficient.

The five residuals B4, EW, A5, Es, E7 vanish in every retained
actual chart: two are coefficients of the complete multiplier
equations, two come from the genuine second potential and its
actual s derivative, and one is the full H7 consequence.
The left side of (21) is therefore zero. Its right side is nonzero
because r and the535 multiplier kappa are nonzero.
This proves (1) and excludes the noncomplex-T0 sector557.

## 6. Boundaries, combination and verification

The proof keeps all c,d,e,y2,y1,y0, n and ell, including every
zero lower-coefficient case. It assumes neither rationality of
the finite coefficient field nor an algebraic presentation by the
displayed coefficients. The intrinsic critical point beta=0 has
not been removed. No actual coordinate specialization, root
promotion, ambient normalization or asserted realization is used.

There is NO U4 condition in (13)--(22). Consequently the excluded
sector includes U4 nonzero and U4 zero, both delta branches of559,
and every zero/nonzero choice of the homogeneous integration
constant in the later conic-field restrictions.
The proof does not depend on559,563,564 or567 for its contradiction:
their previously investigated cases simply lie inside the
specified noncomplex-T0 input. The earlier proposed degenerate-
quartic-only filename was never created.

The complementary T0 complex case of this SAME full554 transverse
v1=0 cubic-excess family is excluded in
[558](principal-paraboloid-cubic-transverse-complex-ratio-exclusion-pass558-working.md),
with its actual-map, selected-partial, full-return and lower-profile
hypotheses retained. T0 is an element of F0, so complex and
noncomplex exhaust its possibilities. Thus (1) combined with558
excludes the whole specified h nonzero, v1=0 family.
This combination makes no statement about v1 nonzero, the separate
h=0 family554, lower theta/y degrees, other sigma degrees or
arbitrary entry into264.

The target and the superseded target were checked absent before
creation. The writing guide was read. Complete557 and558 were
previously read through EOF; their held hashes were rechecked in
f4225a and caf57c:
b7767894ef7915ca4dcd3ee2ada71720be2a99d4cdd33bb4c546a1eb5bbd6c5b
and
0eb506f2a08af38de774460f2c068cf85144df076834419eb55e638851719ca9.
The source557 high formulas and full535 definitions were freshly
rechecked in fe2ae2 and f4225a. The full scalar and moving-x
licenses are explicitly retained above.

Fresh unsaved40c417 constructs the ENTIRE formal H with arbitrary
lower coefficients, differentiates H_U,H_V before evaluation,
builds both entire residuals in (8), and checks (15)--(21).
It keeps b and b_t arbitrary and all unused potential jets.
The complete A6 and B5 checks vanish as well. Its evaluation of
the entire certificate is exactly r*kappa. Earlier fresh3bdcd4,
6b86fb and6c7b09 verify the narrower U4=0 specialization; that
specialization is not needed in the final proof.

Parent's independent full-generic68c7db and Geometry's separate
full-generic1dc75f reconstruct the same universal coefficient
certificate. Their earlier whole-polynomial6ff0bb,0bd8fe and
aa477a checks agree on the specialization. Geometry's e1f8c5
separately checks the compact residual combination. These are
fresh unsaved expansions, not executions of saved checkers.
The direct printed coefficient calculation proves the identity
universally rather than inferring it from a grid of examples.
Post-writing fresh522862 independently checks the ENTIRE moving-x
covariance of both535 polynomials and the printed identities
(17),(19),(20),(21), with six zero residuals.

Only this new source was written. No saved checker was executed,
imported, compiled or rerun. No earlier source or canonical record
was edited. The initial complete author read reached EOF in
31f4b3+0d306c; a final complete reread follows this verification
update. Independent saved-source review remains required before
acceptance. No novelty, unrestricted
recognition, general entry or cancellation conclusion is claimed.
