# Degree-drop conics cannot have transversely variable coupling

Working bounded exclusion: retain the FULL actual principal chart264
and the genuine potentials and unit minors of296. Suppose intrinsic
sigma is affine and nonconstant, and, in the existing parameter
\(P=\sigma\),
\[
\theta=aP^2+bP+c,\qquad a\ne0,\qquad m=k_s\ne0,
\qquad 1+ma=0.
\tag{1}
\]
Then
\[
\boxed{m_s=0.}
\tag{2}
\]
Thus the degree-drop sector with \(m_s\ne0\) is empty. This includes
both zero and nonzero values of \(k_t+mb\). It does not settle the
remaining \(m_s=0\) degree-drop sector, arbitrary projected curves,
or the global entry problem.

The quadratic-level parity theorem327 does NOT apply to (1), and
none of its parity conclusions is used below. The degree bound is
proved directly from the genuine monic H. Only the unrestricted
Sections1--3 of494 are imported for the unit tangent multiplier.

## 1. Exact actual input and intrinsic parameter speed

Retain every actual hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md) and
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md).
In particular,
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u_{\rm glob}],\qquad
E=\partial_{u_{\rm glob}},\qquad X=a_0u_{\rm glob}+x_0,
\quad a_0\ne0,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\qquad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the ENTIRE initial kernel},\\
0\ne N=[u_{\rm glob}^4]\partial_Z|_A,\qquad
L=\operatorname{Frac}\ker_A N,\qquad [L:\mathbb C(t,s)]<\infty,\\
Na_0=Nt=Ns=0,\qquad Nv=1,\qquad
O=L[v]=L[y,z_0,w]=L[y,\sigma,\theta],\\
\operatorname{Frac}A=L(v)=\mathbb C(y,z_0,w).
\end{gathered}
\tag{3}
\]
The original slice, the literal selected partial and both actual
returns remain required. Coefficient partials on L commute and have
joint constants C. No rationality of L is assumed.

The affine nonconstant sigma hypothesis gives
\[
P=\sigma,\qquad O=L[P],\qquad NP=\rho\in L^*,\qquad
J_{t,s,P}(X)=-a_0^4/\rho\in L^*.
\tag{4}
\]
The coefficient partials are extended to fix P when taking the
literal determinant. In particular \(NP\) has not been set to one.
This is an intrinsic parameter change, not an ambient coordinate
change. The scalar in (4) need not be a complex constant or have
zero coefficient derivatives.

The original rows are
\[
\begin{aligned}
Y&=y+PX+tX^2,\\
Z&=2ty+P^2+k_tP+m\theta+n+(2tP+k)X+t^2X^2,\\
W&=w+\theta X+sX^2,\\
mw&=\ell-(2P+k_t)y-F(P,\theta).
\end{aligned}
\tag{5}
\]
All intercepts here are polynomials in P with coefficients in L.
Suppose for contradiction that \(h=m_s\ne0\). Equation (1) gives
\[
a=-1/m,\qquad a_s=h/m^2,\qquad \epsilon:=k_t+mb,
\qquad P^2+k_tP+m\theta=\epsilon P+mc.
\tag{6}
\]
The last expression is allowed to be constant. Neither its linear
coefficient nor any polynomial coordinate assertion is assumed.

## 2. The genuine monic level bounds y without quadratic parity

For independent formal variables U,P,V, use the full polynomials
\[
\begin{aligned}
F(P,V)&=\frac{k_{tt}}2P^2+m_tPV+\frac h2V^2+n_tP+n_sV,\\
G(U,P,V)&=\{\ell-(2P+k_t)U-F(P,V)\}/m,\\
H(U,P,V)&=U^2+F_PU+F_VG+H_3(k;P,V)+H_2(n;P,V)
                       -\ell_tP-\ell_sV,\\
H_3(k;P,V)&=\frac{k_{ttt}}6P^3+\frac{m_{tt}}2P^2V
                          +\frac{h_t}2PV^2+\frac{h_s}6V^3,\\
H_2(n;P,V)&=\frac{n_{tt}}2P^2+n_{ts}PV+\frac{n_{ss}}2V^2.
\end{aligned}
\tag{7}
\]
The levels \(H(y,P,\theta)=h_0\) and \(Q(y,P,\theta)=q_0\)
are the actual moving levels of296, with \(h_0,q_0\in L\).
No lower coefficient or derivative of these levels is discarded.

Write the monic polynomial \(H-h_0=U^2+A_1U+A_0\). Directly,
\[
\begin{aligned}
A_1&=F_P-(2P+k_t)F_V/m,\\
A_0&=F_V(\ell-F)/m+H_3(k)+H_2(n)-\ell_tP-\ell_sV-h_0.
\end{aligned}
\tag{8}
\]
After substituting any quadratic theta, their P degrees are at most
three and six respectively. If y had degree d greater than three,
its square would have degree 2d, strictly greater than both d+3
and six, so the monic level could not vanish. Consequently
\[
y=rP^3+eP^2+lP+j,\qquad r,e,l,j\in L.
\tag{9}
\]
The case r=0 is retained. This argument requires no assertion from
327 and no irreducibility or factorization hypothesis on H.

## 3. The full scalar and genuine minor give a unit multiplier

Apply only Sections1--3 of
[494](principal-paraboloid-unit-tangent-multiplier-pass494-working.md),
which have no degree restriction on y or theta and no assumption
\(m_s=0\) or \(1+ma\ne0\). In its notation set
\[
f=H_U^{\rm ev},\qquad g=H_V^{\rm ev},\qquad
\nu=F_V(P,\theta)/m,\quad
\beta_f=(2y+F_P(P,\theta))/m,\quad D_f=(2P+k_t)/m.
\tag{10}
\]
The complete polynomials needed here are
\[
\begin{aligned}
\mathcal A&=y_t+\theta_Py_s+y_P^2,\\
\mathcal B_1&=\theta_t+
       \theta_P(y_P+\theta_s+\nu)+\beta_f+D_fy_P,\\
\mathcal W&=(\theta_P+D_f)g^2+
       (y_P-\theta_s-\nu)fg-y_sf^2.
\end{aligned}
\tag{11}
\]
That universal result gives
\[
\mathcal A=\kappa g,\qquad \mathcal B_1=-\kappa f,
\qquad \kappa\in L^*,\qquad \mathcal W\in L^*.
\tag{12}
\]
For clarity, the unit statements use the whole actual scalar, not
just its highest terms. The P tangent is \((y_P,1,\theta_P)\).
The three genuine evaluated minors of296 are \(\mathcal W\) times its signed
components, so their unit ideal gives \(\mathcal W\in L^*\).
Likewise the H gradient gives \((f,g)O=O\). The entire linear-X
scalar is \(-f\mathcal A-g\mathcal B_1\), so its vanishing gives
a polynomial common multiplier, including f=0 or g=0. The entire
constant-X scalar is \(J_0=\kappa\mathcal W\). Equation (4) then
forces the multiplier to lie in \(L^*\). No moving coefficient
of kappa is assumed zero.

In particular the use of the genuine fourth potential Q in (12)
retains both moving levels. A formal solution of the cubic H alone
would not license these equations.

## 4. Six coefficients with unrestricted lower jets

All following coefficients are extracted from the full expressions
(7),(10),(11). Their respective degree bounds are
six, three, four, four, three and nine. Write
\(H_6=[P^6]H(y,P,\theta)\), \(f_3=[P^3]f\), and
\(g_4=[P^4]g\). With (6), the exact ledger is
\[
\begin{aligned}
H_6&=r^2+\frac{2hr}{m^2}-\frac{h_s}{6m^3}
                          +\frac{h^2}{2m^4}=0,\\
f_3&=2(r+h/m^2),\\
g_4&=-\frac{2hr}{m}+\frac{h_s}{2m^2}-\frac{3h^2}{2m^3},\\
[P^4]\mathcal A&=9r^2-2r_s/m=\kappa g_4,\\
[P^3]\mathcal B_1&=2r/m=-\kappa f_3,\\
[P^9]\mathcal W&=3rf_3g_4-r_sf_3^2=0.
\end{aligned}
\tag{13}
\]
These are coefficient identities even if one of the displayed
leaders vanishes. All lower coefficients b,c,e,l,j,n,ell and their
derivatives remain arbitrary in the extraction.

Some details guard against a false degree-drop simplification.
Formal differentiation gives
\(f=2y+F_P-(2P+k_t)F_V/m\). The evaluated G has quartic
leader \(-\{2r+ha^2/2\}/m\); this term is included in g4.
Before imposing (6), the last two relevant scalar leaders are
\[
\begin{aligned}
[P^3]\mathcal B_1
 &=6ar+2aa_s+2ha^2/m+8r/m,\\
[P^9]\mathcal W
 &=2(a+1/m)g_4^2+(3r-a_s-ha/m)f_3g_4-r_sf_3^2.
\end{aligned}
\tag{14}
\]
Under (6), \(a_s+ha/m=0\) and
\(\theta_P+D_f=(k_t+mb)/m\), which is constant in P and may
be zero. Thus its squared-gradient contribution has degree at
most eight. This explains both cancellations in (13), without
dividing \(k_t+mb\).

The first three entries also satisfy the exact off-level identity
\[
g_4+3mH_6=r(4h/m+3mr).
\tag{15}
\]
On the actual H level this reduces to
\(g_4=r(4h/m+3mr)\).

## 5. Zero cases and the derivative contradiction

If r=0, then \(f_3=2h/m^2\ne0\). The fifth entry of (13)
would give kappa=0, contrary to (12). Hence r is nonzero.

If f3=0, then \(r=-h/m^2\ne0\). The same entry of (13)
would require \(2r/m=0\), again impossible. Hence f3 is also
nonzero. Only now divide by these two coefficients. The last
two entries of (13) give
\[
\kappa=-\frac{2r}{mf_3},\qquad r_s=\frac{3rg_4}{f_3}.
\tag{16}
\]
Insert (16) in the fourth entry of (13). It becomes
\(9r^2-6rg_4/(mf_3)=-2rg_4/(mf_3)\), and therefore
\[
g_4=\frac94mr f_3,\qquad r_s=\frac{27}4mr^2.
\tag{17}
\]
Equating this formula for g4 with (15), using its on-level form
and \(f_3=2(r+h/m^2)\), gives
\[
r=-\frac{h}{3m^2}.
\tag{18}
\]
Substitution into H6=0 gives
\[
h_s=-\frac{h^2}{3m}.
\tag{19}
\]
Differentiate the existing coefficient (18) in the exact s
direction, retaining \(m_s=h\). Equations (18),(19) give
\[
r_s=-\frac{h_s}{3m^2}+\frac{2h^2}{3m^3}
    =\frac{7h^2}{9m^3}.
\tag{20}
\]
But the second identity in (17) gives
\[
r_s=\frac{3h^2}{4m^3}.
\tag{21}
\]
The difference of (20) and (21) is
\[
\frac{h^2}{36m^3}\ne0,
\tag{22}
\]
a contradiction. This proves (2).

No division by epsilon, g4, r_s, or any unspecified lower
coefficient occurred. The r=0 and f3=0 cases were disposed of
before dividing by them. No algebraic root was adjoined, no
coefficient field was assumed rational, and no field-valued
coordinate change was promoted to the actual four-ring.

## 6. Verification and retained boundary

Fresh unsaved author calculation57cd63 reconstructed the full
generic H, its two formal gradients, both scalar polynomials and
the primitive minor. All six generic coefficient residuals were
zero; specializing a=-1/m reproduced (13)--(22).
Root's independent184905 and Jet's independent5059cb/b31bd1
separately reconstructed the same complete ledger, monic degree
bounds, off-level identity and derivative mismatch. No saved
checker was executed, imported, compiled or modified.

This note retains the actual264/296 inputs and universal494
Sections1--3 as dependencies, not as recursively certified
results. The proof does not import327's quadratic-S parity or
498's nonzero-delta hypothesis. It excludes exactly the added
conditions (1) with m_s nonzero. The complementary degree-drop
case m_s=0 and the unrestricted cancellation problem remain
outside its conclusion.
