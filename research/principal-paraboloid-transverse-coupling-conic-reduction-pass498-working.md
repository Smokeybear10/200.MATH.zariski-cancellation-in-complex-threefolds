# Transversely variable conic coupling has a reciprocal-square-root form

Working necessary result: retain the FULL actual principal chart264,
nonzero coupling \(m=k_s\), affine nonconstant intrinsic sigma,
quadratic theta, and a quadratic
\(S=\sigma^2+k_t\sigma+m\theta\). If \(m_s\ne0\), then
\[
\boxed{\deg_\sigma y\le2,\qquad m_{ss}=\frac{3m_s^2}{m}.}
\tag{1}
\]
Consequently in the exact field \(F_0=\ker_L\partial_s\), finite
over \(\mathbb C(t)\), there exist \(\gamma\in F_0^*\) and
\(B,K\in F_0\) such that
\[
\boxed{
\frac1{m^2}=B-2\gamma s,\qquad
k=K-\frac1{\gamma m}.
}
\tag{2}
\]
No root is adjoined and none of these coefficient functions is
promoted to an actual polynomial coordinate. This is a necessary
family, not a solution of its remaining lower equations or a
recognition theorem. It is separate from the \(m_s=0\) family493.

## 1. Exact actual hypotheses and the common multiplier

Retain every actual assumption of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
the genuine cubic/quartic levels and unit minors of
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md),
and the degree sector of
[327](principal-paraboloid-affine-sigma-quadratic-level-parity-pass327-working.md).
In particular the original polynomial four-ring
\(\mathcal B=A[u_{\rm glob}]=\mathbb C[X,Y,Z,W]\), its slice
\(E=\partial_{u_{\rm glob}}\), time degrees \((1,2,2,2)\),
ENTIRE initial kernel \((\mathsf X^2\mathsf Z-\mathsf Y^2)\),
literal selected partial and nonzero leading N, both actual returns
and exact finite field \(L/\mathbb C(t,s)\) remain required.
Put
\[
P=\sigma,\quad O=L[P],\quad NP=\rho\in L^*,\qquad
\theta=aP^2+bP+c,\quad a\ne0,\quad\delta=1+ma\ne0.
\tag{3}
\]
The original scalar in these parameters is
\(-a_0^4/\rho\in L^*\). The coefficient partials on L commute
and have joint constants C. They extend to fix P for the moving
parameter determinant. This intrinsic change is not an ambient
complex coordinate change.

Assume \(h=m_s\ne0\).327's monic-surface degree bound gives
\[
y=y_3P^3+y_2P^2+y_1P+y_0,\qquad y_i\in L.
\tag{4}
\]
We do not assume \(y_3=0\); proving it is the new step.
The condition delta nonzero is the exact quadratic-S hypothesis,
not a field-valued normalization.

Use the complete held common-multiplier lemma
[494](principal-paraboloid-unit-tangent-multiplier-pass494-working.md),
Sections1--3. These sections apply without the later \(m_s=0\)
conic restriction. With evaluated genuine gradients
\[
f=H_U^{\rm ev},\qquad g=H_V^{\rm ev},\qquad
\nu=F_V(P,\theta)/m,\quad
\beta_f=(2y+F_P(P,\theta))/m,\quad D_f=(2P+k_t)/m,
\]
that lemma supplies
\[
\begin{aligned}
\mathcal A&=y_t+\theta_Py_s+y_P^2=\kappa g,\\
\mathcal B_1&=\theta_t+\theta_P(y_P+\theta_s+\nu)
                            +\beta_f+D_fy_P=-\kappa f,\\
\kappa&\in L^*,\\
\mathcal W&=(\theta_P+D_f)g^2+
             (y_P-\theta_s-\nu)fg-y_sf^2\in L^*.
\end{aligned}
\tag{5}
\]
The nonzero coefficient-field multiplier follows from BOTH full
scalar coefficients and the genuine unit tangent minor. It is not
an arbitrary polynomial multiplier introduced just at highest degree.
No rationality of the coefficient field is assumed.

## 2. Leading coefficients from the literal cubic and full scalar

For clarity the full formal polynomial whose coefficients are used is
\[
\begin{aligned}
F(P,V)&=\frac{k_{tt}}2P^2+m_tPV+\frac h2V^2+n_tP+n_sV,\\
G(U,P,V)&=\{\ell-(2P+k_t)U-F(P,V)\}/m,\\
H(U,P,V)&=U^2+F_PU+F_VG
       +H_3(k;P,V)+H_2(n;P,V)-\ell_tP-\ell_sV.
\end{aligned}
\tag{6}
\]
Here \(H_j\) are264's factorial-denominator Taylor polynomials,
and \(H(y,P,\theta)=h_0\in L\) is the ACTUAL moving level.
Lower coefficients n,ell,h0 and their derivatives remain unrestricted.

The coefficient of \(P^6\) in that level is
\[
y_3^2-\frac{2ha}{m}y_3
          +a^3\left(\frac{h_s}{6}-\frac{h^2}{2m}\right)=0.
\tag{7}
\]
It is also327's leading monic condition, now with intrinsic
coordinate P. Direct formal differentiation of (6) gives
\[
\begin{aligned}
f_3:=[P^3]f&=2(y_3-ha/m),\\
g_4:=[P^4]g&=-2hy_3/m+
                     a^2\left(h_s/2-3h^2/(2m)\right).
\end{aligned}
\tag{8}
\]
The full f and g have degrees at most three and four respectively.
In particular the leading term of G after evaluation is
\(-\{2y_3+ha^2/2\}P^4/m\); its contribution to \(H_V\) must
be retained. Eliminating only \(h_s\) by (7), using \(a\ne0\),
rewrites (8) as
\[
g_4=y_3(4h/m-3y_3/a).
\tag{9}
\]
Neither f3 nor g4 is assumed nonzero.

The complete polynomials A and B1 in (5) have degrees at most
four and three. Their respective highest coefficients give
\[
\begin{aligned}
9y_3^2+2a(y_3)_s&=\kappa g_4,\\
6ay_3+2aa_s+2ha^2/m+8y_3/m&=-\kappa f_3.
\end{aligned}
\tag{10}
\]
For example the last \(8y_3/m\) is the sum of the cubic terms
of beta_f and D_f*y_P, not a discarded lower-potential term.
These equations also hold when a displayed top coefficient is zero.

The COMPLETE coefficient of \(P^9\) in W is
\[
2(a+1/m)g_4^2+
 (3y_3-a_s-ha/m)f_3g_4-(y_3)_sf_3^2.
\tag{11}
\]
Indeed each of its three summands has degree at most nine in the
full expression (5). There is no unprinted term of this degree.
Substitute the two identities (10) into (11), dividing only by
the known nonzero \(2a\), and use (9). Exact simplification gives
\[
[P^9]\mathcal W
=-\frac{2y_3^2}{a^2m^2}
       \left(-a^3h^2-4ahy_3+3my_3^2\right).
\tag{12}
\]
Since W is in \(L^*\), (12) vanishes.

## 3. A nonzero cubic coefficient contradicts the unit multiplier

Suppose \(y_3\ne0\). Equation (12) gives
\[
3my_3^2-4ahy_3-a^3h^2=0.
\tag{13}
\]
Define an EXISTING coefficient element
\[
r=\frac{my_3}{ah}\ne0.
\tag{14}
\]
There is no extraction of a root. Equations (7),(13) then give
\[
\begin{aligned}
a&=\frac{r(3r-4)}m,\qquad
y_3=\frac{h r^2(3r-4)}{m^2},\\
h_s&=\frac{3r h^2}{m(3r-4)},\qquad
\delta=(r-1)(3r-1).
\end{aligned}
\tag{15}
\]
Here \(3r-4\ne0\), since otherwise a would be zero.
The only denominators used in (15) are nonzero m,h,a,r,3r-4.
The delta hypothesis is retained but is not divided in the
following elimination.

Differentiate the first two formulas in (15) in s, using \(m_s=h\)
and the third formula. Substitute into (10). After removing only
the nonzero factors \(h r^2(3r-4)/m^4\) and
\(2r(3r-4)/m^3\), the two equations are exactly
\[
\begin{aligned}
G_1={}&h\kappa m(3r-4)+hr(27r^2-42r+16)
                             +2m r_s(9r-8)=0,\\
G_2={}&h\kappa m(r-1)+hr(9r^2-12r+4)
                             +2m r_s(3r-2)=0.
\end{aligned}
\tag{16}
\]
Their zero-safe elimination is
\[
(3r-2)G_1-(9r-8)G_2=-hmr\kappa=0.
\tag{17}
\]
All of h,m,r,kappa are nonzero. This contradiction excludes
\(y_3\ne0\).
No division by \(3r-2\), \(r-1\), \(9r-8\), f3, g4 or r_s
occurred, so no exceptional value of these factors was discarded.

Thus \(y_3=0\). Equation (7), with \(a\ne0\), immediately gives
\[
h_s=3h^2/m.
\tag{18}
\]
This proves (1). There is no conclusion yet that the remaining
quadratic y or conic theta can be realized in an actual chart.

## 4. Exact integration without changing the ambient ring

Set \(F_0=\ker_L\partial_s\). The usual exact finite-field argument
applies: differentiate a monic minimal polynomial over C(t,s);
minimality puts its coefficients in C(t). Degrees of these
constant subextensions are bounded by \([L:\mathbb C(t,s)]\).
Thus \(F_0/\mathbb C(t)\) is finite, and its exact t derivative
has constants C. The field is not assumed rational.

Equation (18) gives
\[
\gamma=\frac{h}{m^3}\in F_0^*.
\tag{19}
\]
Differentiating the following EXISTING elements in s gives zero:
\[
B=m^{-2}+2\gamma s,\qquad
K=k+\frac1{\gamma m}.
\tag{20}
\]
For the second identity use \(k_s=m\) and \(m_s=\gamma m^3\).
Thus \(B,K\in F_0\), proving (2). Either B or K may be zero.
The factor \(B-2\gamma s=m^{-2}\) is nonzero in the coefficient
field. None of these expressions is asserted to be a unit or
coordinate of the original polynomial ring.

The necessary family still has to satisfy the remaining genuine
H and Q levels, the full lower scalar, all-X polynomial generation,
the original-ring returns and actual entry. This note supplies no
converse and no coordinate recognition for that family.

## 5. Reconstruction and scope

The complete264,296,327 and held494 sources were read before this
argument. Fresh unsaved root4a57fa rebuilt the full formal H in
(6), its evaluated derivatives, both leading scalar polynomials
and the entire degree-nine expression. Every displayed leading
coefficient residual was zero. Earlier a281a4 checked the same
degree-nine elimination from independently written leading terms.
Fresh49a0e4 reconstructs the complete substituted two-equation
system (16). Fresh917307 verifies the division-free combination
(17) and all exact integration derivatives in (19),(20).
The scalar/unit and field licenses are the written proofs, not
claims inferred from numerical sampling.

This is a necessary conic reduction in the transverse-coupling
branch \(m_s\ne0\). The zero-\(m_s\) branches, delta-zero degree
drop, nonlinear sigma, other projected curves and arbitrary
actual-chart entry remain separate. The general cancellation
problem is not solved. No historical novelty, human expert review
or proof-assistant certification is claimed. All saved checkers
remain frozen; none was executed, imported, compiled or rerun.
No earlier source or canonical record was edited while writing
this note.
