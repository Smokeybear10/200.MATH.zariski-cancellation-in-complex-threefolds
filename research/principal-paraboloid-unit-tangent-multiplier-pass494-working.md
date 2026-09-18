# A unit tangent multiplier and a transverse conic parameter

Working result: in the FULL actual principal chart264 with nonzero
coupling and affine nonconstant intrinsic sigma, the two remaining
scalar equations have a common multiplier in the exact coefficient
field \(L^*\), not merely in the intrinsic polynomial ring.
The conclusion includes the zero-gradient-component cases.

In the nonlinear conic sector with variable \(m=k_s\), \(m_s=0\),
\(\theta=aP^2+bP+c\), \(P=\sigma\), and
\(a(1+ma)\ne0\), this forces
\[
\boxed{a_s=0.}
\tag{1}
\]
There is NO restriction on \(m_{tt}\). In particular this proves (1)
in the zero-second-derivative branch not covered by493.
With \(p=m_t\), an existing transverse coefficient is
\[
\boxed{
z_{\rm tr}=b-\left(pa-\frac{a_t}{2a}\right)s,\qquad
(z_{\rm tr})_s\ne0.
}
\tag{2}
\]
Thus \((t,z_{\rm tr})\) is an exact separating coefficient basis.
This is a necessary reduction, not an actual ambient coordinate
change, a conic exclusion or unrestricted cancellation.

## 1. Actual chart and reparameterization license

Retain EVERY actual hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md) and
the genuine levels and unit-minor result of
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md).
In particular,
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u_{\rm glob}],\quad
E=\partial_{u_{\rm glob}},\quad X=a_0u_{\rm glob}+x_0,\quad a_0\ne0,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\qquad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the ENTIRE initial kernel},\\
0\ne N=[u_{\rm glob}^4]\partial_Z|_A,\qquad
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,\\
Na_0=Nt=Ns=0,\quad Nv=1,\quad
O=L[v]=L[y,z_0,w]=L[y,\sigma,\theta],\\
\operatorname{Frac}A=L(v)=\mathbb C(y,z_0,w),\qquad m=k_s\ne0.
\end{gathered}
\tag{3}
\]
Here \(z_0\) denotes the original Z intercept, not the transverse
coefficient in (2). The original slice, both returns and selected
literal partial remain required. The coefficient partials commute,
with joint constants C.

Assume \(\deg_v\sigma=1\). Then
\[
P=\sigma,\qquad O=L[P],\qquad NP=\rho\in L^*.
\tag{4}
\]
The exact coefficient partials on L are unchanged and are extended
to fix P when differentiating the literal rows. This is an intrinsic
affine reparameterization, not an original polynomial coordinate
assertion. Its parameter Jacobian divides the original scalar by rho.
The full map is
\[
\begin{aligned}
Y&=y+PX+tX^2,\\
Z&=2ty+P^2+k_tP+m\theta+n+(2tP+k)X+t^2X^2,\\
W&=w+\theta X+sX^2,\\
mw&=\ell-(2P+k_t)y-F(P,\theta),\\
F(P,V)&=\frac{k_{tt}}2P^2+m_tPV+\frac{m_s}2V^2+n_tP+n_sV,\\
J(X,P)&=J_{t,s,P}(X)=-a_0^4/\rho\in L^*.
\end{aligned}
\tag{5}
\]
All y,theta,w are polynomials in P with coefficients in L.
Their moving coefficient derivatives are not discarded.

The genuine formal H and Q of296 satisfy
\(H(y,P,\theta)=h_0\), \(Q(y,P,\theta)=q_0\), with both levels
in L. Denote evaluated derivatives by
\[
f=H_U^{\rm ev},\quad g=H_V^{\rm ev},\quad h_P=H_P^{\rm ev},
\qquad Q_U^{\rm ev},Q_P^{\rm ev},Q_V^{\rm ev}\in O.
\]
To avoid confusing the slope of y with a formal coefficient, set
\[
\nu=\frac{F_V(P,\theta)}m,\qquad
\beta_f=\frac{2y+F_P(P,\theta)}m,\qquad
D_f=\frac{2P+k_t}{m}.
\tag{6}
\]
Formal coefficient derivatives used to construct H,Q hold their
independent formal variables fixed; derivatives of evaluated
functions below are total derivatives at fixed P.

## 2. The primitive tangent minor is a coefficient-field unit

Differentiate the two actual levels in P. Their tangent is
\((y_P,1,\theta_P)\), and hence
\[
h_P=-fy_P-g\theta_P,\qquad
Q_P^{\rm ev}=-Q_U^{\rm ev}y_P-Q_V^{\rm ev}\theta_P.
\tag{7}
\]
Put
\[
\mathcal W=fQ_V^{\rm ev}-gQ_U^{\rm ev}.
\tag{8}
\]
The three evaluated minors from296 are exactly
\[
M_{UP}=-\theta_P\mathcal W,\qquad
M_{UV}=\mathcal W,\qquad
M_{PV}=-y_P\mathcal W.
\tag{9}
\]
Their ideal is the unit ideal by the full actual scalar argument
in296. Thus
\[
\mathcal W\in L^*.
\tag{10}
\]
This is a polynomial-ideal conclusion in \(O=L[P]\), not just a
nonzero rational-function assertion.
Likewise296's evaluated H-gradient ideal is the unit ideal.
Equation (7) therefore gives
\[
(f,g)O=O.
\tag{11}
\]
In particular f and g are coprime, even when one is zero. They
cannot both be zero.

The full corrected-gradient identities of296, including the moving
level derivative \(h_{0,s}\), give
\[
\begin{aligned}
Q_U^{\rm ev}&=h_P-D_fg+\nu f
                 =f(\nu-y_P)-g(\theta_P+D_f),\\
Q_V^{\rm ev}&=H_s^{\rm ev}-h_{0,s}=-fy_s-g\theta_s.
\end{aligned}
\tag{12}
\]
The second identity follows by differentiating the actual H level
at fixed P. Substitution in (8) gives the entire polynomial
\[
\mathcal W=(\theta_P+D_f)g^2
            +(y_P-\theta_s-\nu)fg-y_sf^2.
\tag{13}
\]
No lower gradient term or moving level was removed.

## 3. The two complete scalar coefficients force a unit multiplier

Define polynomials in \(O\) by
\[
\begin{aligned}
\mathcal A&=y_t+\theta_Py_s+y_P^2,\\
\mathcal B_1&=\theta_t+
       \theta_P(y_P+\theta_s+\nu)+\beta_f+D_fy_P.
\end{aligned}
\tag{14}
\]
The symbol \(\mathcal B_1\) is not the ambient polynomial ring.
After the literal potential substitutions,296 supplies
\(J=J_0+XJ_1+X^2J_2\). The H level makes \(J_2=0\).
Its COMPLETE linear coefficient, after (7), is
\[
J_1=-f\mathcal A-g\mathcal B_1.
\tag{15}
\]
For direct reconstruction before cancellation, it is
\[
f\{(\theta_s+\nu)y_P-y_t-y_s\theta_P\}
 +h_P\{y_P+\theta_s+\nu\}
 +g\{-\theta_t-\beta_f-D_fy_P\}.
\]
Its vanishing and (11) imply a polynomial multiplier
\[
\mathcal A=\kappa(P)g,\qquad
\mathcal B_1=-\kappa(P)f,\qquad\kappa(P)\in O.
\tag{16}
\]
To include all zero cases: if \(g\ne0\), coprimeness makes g divide
the polynomial A, after which (15) gives the second identity.
This includes f=0, when g is a unit and B1=0. If g=0, f is a unit,
A=0, and one takes \(\kappa=-\mathcal B_1/f\).
No common root or leading coefficient has been divided away.

The FULL constant-X coefficient is equally important.296 gives
\[
\begin{aligned}
J_0={}&f\{y_s(\theta_t+\beta_f)-y_t(\theta_s+\nu)\}\\
 &+h_P\{y_P(\theta_s+\nu)-y_s(\theta_P+D_f)\}\\
 &+g\{y_t(\theta_P+D_f)-y_P(\theta_t+\beta_f)\}.
\end{aligned}
\tag{17}
\]
Use only (7),(14) to rewrite this entire polynomial as
\[
\begin{aligned}
J_0={}&f\{y_s\mathcal B_1-(\theta_s+\nu)\mathcal A\}\\
 &+g\{(\theta_P+D_f)\mathcal A-y_P\mathcal B_1\}.
\end{aligned}
\tag{18}
\]
Now (13),(16) give the complete identity
\[
J_0=\kappa(P)\mathcal W.
\tag{19}
\]
Both \(J_0=-a_0^4/\rho\) and W are nonzero elements of L by the
actual scalar and (10). Consequently
\[
\boxed{\kappa=-\frac{a_0^4}{\rho\mathcal W}\in L^*.}
\tag{20}
\]
Thus the multiplier has no intrinsic P dependence. It need NOT
be a complex constant, or be independent of t or s. Equations
(14),(16),(20) are necessary conditions for every actual affine-sigma
chart under (3), with no restriction on the degrees of y or theta.
They are not a converse construction of an actual chart.

## 4. Consequence for quadratic theta with m_s=0

Now add exactly the conic hypotheses
\[
m_s=0,\quad m\notin\mathbb C,\quad
p=m_t\ne0,\qquad
\theta=aP^2+bP+c,\quad a\ne0,\quad\delta=1+ma\ne0.
\tag{21}
\]
The nonzero p follows from the joint-constant field, not from a
condition on \(q=m_{tt}\), which may be zero.
Retain the all-X polynomial return and parity/degree result
[327](principal-paraboloid-affine-sigma-quadratic-level-parity-pass327-working.md).
The condition delta nonzero says that
\(S=P^2+k_tP+m\theta\) has exact degree two.327 first eliminates
the cubic y coefficient using \(m_s=m_{ss}=0\), then fixes its
quadratic coefficient. Therefore
\[
y=-\frac p2\theta+\lambda P+r,\qquad\lambda,r\in L.
\tag{22}
\]
No surface factorization or irreducibility equation is used.
This is not an application of327 to the separate delta-zero case.

The formal derivatives in (6) now give
\[
\begin{aligned}
\beta_f&=\frac{(2\lambda+k_{tt})P+2r+n_t}{m},\\
f&=2\lambda P+2r+k_{tt}P+n_t
                   -\frac{(2P+k_t)(pP+n_s)}m .
\end{aligned}
\tag{23}
\]
In particular beta_f is affine in P, and f has exact degree two,
with leading coefficient \(-2p/m\ne0\).
Before imposing any equation on \(a_s\), every term in B1 has
degree at most two except \(\theta_P\theta_s\). Thus
\[
[P^3]\mathcal B_1=2a a_s.
\tag{24}
\]
But (16),(20),(23) imply that B1 has degree at most two. Since
a is nonzero, (24) proves \(a_s=0\). This conclusion required
neither a division by q nor the fifth-root reduction493.

## 5. An exact transverse parameter valid also when q=0

After \(a_s=0\), direct expansion of the full B1 in (14) gives
\[
[P^2]\mathcal B_1=a_t-2pa^2+2ab_s.
\tag{25}
\]
The two terms involving \(2ap/m\) cancel between
\(\theta_P\nu\) and \(D_fy_P\); beta_f contributes no quadratic
term. Compare (25) with \(\mathcal B_1=-\kappa f\) and (23):
\[
\kappa=\frac{m}{2p}(a_t-2pa^2+2ab_s)
       =\frac{ma}{p}\left(b_s-pa+\frac{a_t}{2a}\right).
\tag{26}
\]
All denominators in (26) were proved nonzero under (21).

Let \(F_0=\ker_L\partial_s\). It is finite over C(t), with exact
t-derivative constants C: differentiating a monic minimal polynomial
over C(t,s) puts every s-constant's coefficients in C(t), and the
degrees of these constant subextensions are bounded by
\([L:\mathbb C(t,s)]\). Neither \(F_0=\mathbb C(t)\) nor
\(L=F_0(s)\) is asserted.
The elements \(m,p,a,a_t\) all belong to \(F_0\).
Set \(z_{\rm tr}\) as in (2). Then (26) gives
\[
(z_{\rm tr})_s=\frac{p\kappa}{ma}\ne0,\qquad
dt\wedge dz_{\rm tr}=(z_{\rm tr})_s\,dt\wedge ds.
\tag{27}
\]
It follows that \(L/\mathbb C(t,z_{\rm tr})\) is finite and that
the exact commuting partials in this basis are
\[
\partial_{z_{\rm tr}}|_t=(z_{\rm tr})_s^{-1}\partial_s|_t,\qquad
\partial_t|_{z_{\rm tr}}=
 \partial_t|_s-\frac{(z_{\rm tr})_t}{(z_{\rm tr})_s}\partial_s|_t.
\tag{28}
\]
These formulas rebase coefficient derivatives only.
The complete scalar in the new parameter basis is
\[
J_{t,z_{\rm tr},P}=-\frac{a_0^4}{\rho(z_{\rm tr})_s}\ne0.
\tag{29}
\]
One must retain this factor and the moving-parameter derivatives in
any further calculation. The existence of this basis does not
make the remaining lower coefficients rational or polynomial in it.

## 6. Verification and unresolved scope

The entire source296 was read before reconstructing (7)--(19).
The complete264 and327 inputs and their actual return hypotheses
were also read. Fresh unsaved root758ded verifies the entire
J1 syzygy, the entire J0 decomposition, the complete kappa-W
identity and all four leading-coefficient cancellations used in
the conic argument. No coefficient of a parameter-dependent
scalar was artificially set to zero.
Separate outline and saved-source audits are recorded in the ledger.

This supplies new necessary information for the stated conic sector,
especially its q=0 alternative. It does not exclude that sector,
solve its full lower equations, or recognize arbitrary nonlinear
projected curves. The delta-zero boundary and arbitrary chart entry
remain separate problems. All saved checkers remain frozen; none
was executed, imported, compiled or rerun. No earlier source or
canonical record was edited while authoring this note.
