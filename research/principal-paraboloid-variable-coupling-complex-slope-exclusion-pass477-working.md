# Complex slopes are excluded in the variable-coupling affine-line branch

Working theorem: retain every actual hypothesis of264. Suppose
\(m=k_s\notin\mathbb C\), the projected curve is a line with
function-field projection degree one, and sigma is nonconstant.
Write its affine intrinsic data as
\[
y=\lambda P+r,\qquad \theta=\mu P+h,\qquad
w_{\rm int}=\omega P^2+bP+c,\qquad P=\sigma.
\tag{1}
\]
Then \(\lambda,\omega\) cannot both be complex constants.
In particular the normalized branch \(\lambda=\omega=0\) is empty.

The result has no additional condition on
\(\mathcal Dr=(\partial_t+\mu\partial_s)r\). Its zero branch is
the held exclusion476; the nonzero branch is proved here by the
entire original scalar. This does not exclude other affine slopes,
constant sigma, nonlinear projected curves, or arbitrary chart entry.

## 1. Full actual hypotheses and the normalized branch

Retain the actual entry of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
the genuine levels and evaluated minor units of
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md),
and the affine reduction of
[325](principal-paraboloid-all-specializations-affine-line-profile-pass325-working.md).
In particular,
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad
\deg_E(X,Y,Z,W)=(1,2,2,2),\quad a_0=EX\ne0,\\
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the entire initial kernel},\\
N=[u^4]\partial_Z|_A\ne0,\quad Na_0=Nt=Ns=0,\quad
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,\\
O=L[v]=L[y,\sigma,\theta]=L[y,z,w_{\rm int}],\quad Nv=1,\\
K=\operatorname{Frac}A=L(v)=\mathbb C(y,z,w_{\rm int}),\qquad
J_{t,s,v}(X)=-a_0^4\in L^*.
\end{gathered}
\tag{2}
\]
The original global slice, literal selected partial and both returns
are retained. The coefficient partials commute and their joint
constant field is \(\mathbb C\). No rationality of L is assumed.
There is no hypothesis about reducibility of the third surface.

By325 the birational projected-line assumption makes all three
intrinsic functions affine. Since sigma is nonconstant, \(P=\sigma\)
is a polynomial parameter, with \(NP=\rho\in L^*\). The coefficient
partials on O will fix P. Their restrictions to L are unchanged,
and the full calibrated scalar in this parameter is
\[
J_{t,s,P}(X)=-a_0^4/\rho.
\tag{3}
\]
Neither \(NP=1\) nor \(P=u\) is imposed. The original relation
\(X=a_0u+x_0\) retains its intercept.

First assume the normalized data
\[
y=r\in L,\qquad \theta=\mu P+h,\qquad w_{\rm int}=bP+c.
\tag{4}
\]
The case \(\mathcal Dr=0\) is excluded by the fully read held
[476](principal-paraboloid-variable-coupling-invariant-intercept-exclusion-pass476-working.md).
That source integrates the full scalar to
\(s=\epsilon k+\mu_0t+\chi_0\), with complex constants, and
then obtains \(1=\epsilon m\), impossible for variable m.
It requires no published recognition endpoint. For the rest of
Sections2--5 assume
\[
\mathcal Dr\ne0.
\tag{5}
\]

## 2. A nontrivial characteristic constant field exists

For clarity the required high-potential argument does not use (5).
Let \(\mathcal K_j\) denote the frozen sums
\(\sum_{i=0}^j\binom ji\mu^i k_{t^{j-i}s^i}\), and put
\[
\beta=m_t+\mu m_s,\quad
\mathcal M_2=m_{tt}+2\mu m_{ts}+\mu^2m_{ss},\quad
\kappa=\mathcal D\mu.
\tag{6}
\]
The exact second potential makes the quadratic W-intercept
coefficient \(-(2\lambda+\mathcal K_2/2)/m\).
The two zero coefficients in (4) therefore force \(\mathcal K_2=0\).
The complete genuine third and fourth leaders in
[474, Sections2--3](principal-paraboloid-variable-coupling-affine-line-high-gates-pass474-working.md)
then give \(\mathcal K_3=\mathcal K_4=0\).
Both moving levels and all lower coefficients remain part of the
actual equations; none contributes to these particular leaders.

Frozen sums are not iterates of \(\mathcal D\). Their exact
derivative identities are
\[
\mathcal D\mathcal K_2=\mathcal K_3+2\kappa\beta,\qquad
\mathcal D\mathcal K_3=\mathcal K_4+3\kappa\mathcal M_2,\qquad
\mathcal D\beta=\mathcal M_2+\kappa m_s.
\tag{7}
\]
If \(\kappa\ne0\), these identities force
\(\beta=\mathcal M_2=m_s=m_t=0\), which would make m complex.
Thus, without division by beta or either coefficient derivative of m,
\[
\mathcal D\mu=0,\quad a:=\mathcal Dk=k_t+\mu m,\quad
\mathcal Da=0,\quad
\chi:=s-\mu t\in\mathscr F,\quad
\phi:=k-at\in\mathscr F,\qquad
\mathscr F=\ker_L\mathcal D.
\tag{8}
\]
Here \(\mathcal Da=\mathcal K_2+m\kappa\). In particular
\(\mu,a,\chi,\phi\in\mathscr F\).

At least one of \(\mu,\chi\) is noncomplex, since otherwise
\(s=\mu t+\chi\) contradicts the algebraic independence of t,s.
Choose such an element and call it q. Then \(\mathcal Dq=0\)
and \(q_s\ne0\), since \(q_s=0\) would also give \(q_t=0\).
Therefore \((t,q)\) is a separating coefficient basis, with
\(\mathcal D=\partial_t|_q\). The field
\(\mathscr F\) is a finite extension of \(\mathbb C(q)\):
differentiating the monic minimal polynomial over \(\mathbb C(t,q)\)
of an element killed by \(\mathcal D\) shows that its coefficients are in
\(\mathbb C(q)\), and degrees of finite constant subextensions
are bounded by \([L:\mathbb C(t,q)]\). No equality of these
fields is inferred.

Assumption (5) now licenses the different separating basis
\((r,q)\). Indeed
\[
\det\frac{\partial(r,q)}{\partial(t,s)}
=q_s\mathcal Dr\ne0,\qquad
\partial_r|_q=\frac{\mathcal D}{\mathcal Dr},\qquad
\mathscr F=\ker_L\partial_r.
\tag{9}
\]
The unique extended partials \(\partial_r,\partial_q\) commute,
have joint constants \(\mathbb C\), and \(\partial_q\) preserves
\(\mathscr F\). The field \(L/\mathbb C(r,q)\) is finite;
neither \(L=\mathscr F(r)\) nor a rational constant field is
assumed. Every subscript r or q below refers to this exact basis.

## 3. Literal rows and the complete nine-coefficient scalar

Put
\[
\zeta=P+tX,\qquad G=2tr+mh+n,\qquad H_1=h-bt.
\tag{10}
\]
These are functions in the original fraction field, not proposed
complex polynomial coordinates. The complete original rows are
\[
Y=r+X\zeta,\qquad
Z=\zeta^2+a\zeta+G+\phi X,\qquad
W=b\zeta+c+H_1X+\mu X\zeta+\chi X^2.
\tag{11}
\]
The variables X and zeta are algebraically independent over L:
the original slice makes X transcendental over \(L(P)\), and
\(\zeta=P+tX\) is an invertible polynomial change over L.
At fixed X the total parameter determinant in passing from
\((t,s,P)\) to \((r,q,\zeta)\) is still \(q_s\mathcal Dr\).
The moving term tX in zeta is included in that chain rule. Thus
\[
J:=J_{r,q,\zeta}(X)=-\frac{a_0^4}{\rho q_s\mathcal Dr}
\in L^*,
\tag{12}
\]
independent of X and zeta. The full derivative matrix of (11) is
\[
\begin{pmatrix}
1&0&X\\
G_r&a_q\zeta+G_q+\phi_qX&2\zeta+a\\
b_r\zeta+c_r+(H_1)_rX&
b_q\zeta+c_q+(H_1)_qX+\mu_qX\zeta+\chi_qX^2&b+\mu X
\end{pmatrix}.
\tag{13}
\]
The fact that \(a,\mu,\chi,\phi\) have zero r derivative is
already proved in (8),(9), not imposed on arbitrary coefficients.
Its entire nonzero possible support is the following ledger:
\[
\begin{array}{c|l}
\text{monomial}&\text{coefficient in }J\\ \hline
\zeta^2&-2b_q\\
\zeta&a_qb-2c_q-ab_q\\
1&bG_q-ac_q\\
X\zeta^2&-2\mu_q-a_qb_r\\
X\zeta&a_q\mu-2(H_1)_q-a\mu_q+G_rb_q-a_qc_r-G_qb_r\\
X&b\phi_q+\mu G_q-a(H_1)_q+G_rc_q-G_qc_r\\
X^2\zeta&-2\chi_q+G_r\mu_q-a_q(H_1)_r-\phi_qb_r\\
X^2&\mu\phi_q-a\chi_q+G_r(H_1)_q-G_q(H_1)_r-\phi_qc_r\\
X^3&G_r\chi_q-\phi_q(H_1)_r.
\end{array}
\tag{14}
\]
All rows except the constant row must vanish. No lower scalar
coefficient is omitted.

## 4. The slope integration and its zero case

The first two rows of (14) give
\[
b_q=0,\qquad c_q=a_qb/2.
\tag{15}
\]
In particular \((b_r)_q=0\) by commuting partials. If
\(a_q\ne0\), the \(X\zeta^2\) row gives
\(b_r=-2\mu_q/a_q\in\mathscr F\). Since it is killed by
both r and q partials, \(b_r\in\mathbb C\).

If \(a_q=0\), that same row gives \(\mu_q=0\), and the
\(X^2\zeta\) row reduces to
\(\phi_qb_r=-2\chi_q\). In this case \(\phi_q\ne0\):
otherwise a and phi, being in \(\mathscr F\) and q-constant,
would both be complex. Then \(k=at+\phi\) would give
\(m=k_s=0\), contrary to the entry. Consequently here too
\(b_r\in\mathscr F\cap\ker\partial_q=\mathbb C\).
This treats the zero \(a_q\) case without dividing by it.

Write \(b_r=-2\epsilon\), where \(\epsilon\in\mathbb C\).
Integration inside the exact field gives
\[
b=-2\epsilon r+b_0,\qquad
\mu=\epsilon a+\mu_0,\qquad
c=ab/2+c_0,
\quad b_0,\mu_0\in\mathbb C,\quad c_0\in\ker_L\partial_q.
\tag{16}
\]
The first two constants are complex because the indicated
remainders are killed by both partials. The last remainder is
only q-constant. In particular it is not asserted to be a
rational function of r or a complex constant.

## 5. All remaining scalar coefficients force constant coupling

Define the exact coefficient functions
\[
\begin{aligned}
T&=H_1-\epsilon G,&\delta&=\chi-\epsilon\phi,\\
V_0&=\mu_0-(c_0)_r+\epsilon a,&
D_0&=G-a^2/4,\qquad \Delta=(D_0)_q,\\
A_0&=\phi_q+a_qG_r/2.
\end{aligned}
\tag{17}
\]
No nonvanishing is assumed for these functions. Substitution in
the \(X\zeta\) and \(X^2\zeta\) rows of (14) gives
\[
2T_q=a_qV_0,\qquad a_qT_r=-2\delta_q.
\tag{18}
\]
The constant row is \(b\Delta\), so (12) proves
\[
b\Delta\ne0.
\tag{19}
\]
After using (18), every remaining coefficient of (14) is exactly
recorded by
\[
J=b\Delta
 +X(bA_0+V_0\Delta)
 +X^2(V_0A_0-\Delta T_r)
 -X^3T_rA_0.
\tag{20}
\]
For example the X row before applying (18) is
\(b\phi_q+V_0G_q-aT_q+ba_qG_r/2\), giving the displayed
coefficient. The \(X^2\) row is
\(V_0A_0-a\delta_q-G_qT_r\), and its last two terms combine
to \(-\Delta T_r\). The \(X^3\) row is
\(\delta_qG_r-\phi_qT_r=-T_rA_0\).
Thus no coefficient was removed by an unlicensed division.

The X, \(X^2\), \(X^3\) coefficients now give
\[
bA_0+V_0\Delta=0,\qquad
V_0A_0-\Delta T_r=0,\qquad T_rA_0=0.
\tag{21}
\]
If \(A_0=0\), the first equation and \(\Delta\ne0\) force
\(V_0=0\), then the second forces \(T_r=0\).
If \(A_0\ne0\), the third forces \(T_r=0\), the second
forces \(V_0=0\), and the first contradicts \(b\ne0\).
Consequently
\[
A_0=V_0=T_r=0,\qquad \delta_q=0.
\tag{22}
\]
The last equality uses (18), with no division by \(a_q\).
Since \(\delta\in\mathscr F=\ker\partial_r\), it follows
that \(\delta=\delta_0\in\mathbb C\). Equations (8),(16) yield
\[
s=\mu t+\chi=(\epsilon a+\mu_0)t
                 +\epsilon\phi+\delta_0
 =\epsilon k+\mu_0t+\delta_0.
\tag{23}
\]
Apply the ORIGINAL coefficient partial \(\partial_s\) at fixed t
to this identity in L. Its displayed constants are complex, so
\[
1=\epsilon m.
\tag{24}
\]
The case \(\epsilon=0\) is impossible directly. Otherwise m is
the complex constant \(1/\epsilon\), again impossible. This
excludes (5); together with476 it excludes the entire normalized
branch (4).

## 6. The actual complex-slope normalization

Now suppose both coefficients \(\lambda,\omega\) in (1) are
complex, including either zero. Use the actual polynomial map
\[
X_*=X+\lambda,\qquad Y_*=Y,\qquad Z_*=Z,\qquad
W_*=W-\omega Z.
\tag{25}
\]
Its inverse is \(X=X_*-\lambda\), \(Y=Y_*\), \(Z=Z_*\),
\(W=W_*+\omega Z_*\). The fully read
[426](general-coupling-normalization-obstruction-pass426-working.md)
and [476, Section6](principal-paraboloid-variable-coupling-invariant-intercept-exclusion-pass476-working.md)
give its complete actual licenses. Specifically it and its inverse
preserve the original weights; its leading map preserves the entire
initial ideal, not only its displayed relation. The new normalized time
leader of W is \(s-\omega t^2\ne0\), and the coefficient parameter
change is invertible over \(\mathbb C\). The literal selected partial
is \(\partial_{Z_*}=\partial_Z+\omega\partial_W\); the retained
shift bound for the omitted W-partial gives \(N_*=N\).
The original global slice and kernel do not change, and426's actual
quotient argument preserves both polynomial and strong field returns
and the full scalar. This is not an arbitrary L-valued reframe.

For clarity the relevant exact coefficient transport is
\[
\begin{gathered}
t_*=t,\qquad s_*=s-\omega t^2,\qquad m_*=m,\qquad
k_*=k+2\lambda t^2,\\
P_*=P-2\lambda t,\qquad y_*=r+\lambda^2t,\qquad
\mu_* =\mu-2\omega t,\qquad \lambda_*=\omega_*=0,\\
\partial_{t_*}=\partial_t+2\omega t\partial_s,\qquad
\partial_{s_*}=\partial_s,\qquad
\mathcal D_* =\mathcal D.
\end{gathered}
\tag{26}
\]
The new theta is affine in \(P_*\), and the new W-intercept is
affine as well. Nonconstant sigma and the birational projected-line
condition therefore persist. There is no condition on
\(\mathcal D_*y_*=\mathcal Dr+\lambda^2\): if zero,476 applies;
if nonzero, Sections2--5 apply. Both alternatives are impossible.
This proves the theorem stated in (1).

## 7. A narrow consequence and the remaining scope

In the beta-zero family of474, the exact relation
\(2\lambda'+m\omega'=0\) shows
\(\lambda\in\mathbb C\) if and only if
\(\omega\in\mathbb C\). Thus any surviving actual beta-zero
chart in that particular family must have both coefficients
noncomplex. This does not assume beta zero in general and does
not exclude that remaining family.

The proof uses the supplied full actual chart and affine reduction.
It does not produce an actual chart with noncomplex slopes, solve
the constant-sigma case, promote a coefficient basis to ambient
coordinates, assume normality of a projected plane, or invoke a
published recognition theorem. General variable-coupling and
arbitrary-entry questions remain outside the conclusion.

The strengthened held476 and full426 sources were read through EOF
before authoring. The complete scalar matrix and all nine support
coefficients were reconstructed in fresh unsaved algebra; every
reduced coefficient in (18)--(21), the final zero-case elimination
and the moving parameter determinant were independently checked.
The argument above, rather than numerical samples, supplies the
exact-field and all zero-division justifications. No saved checker
was executed, imported, compiled or rerun. No earlier source or
canonical file was edited. No proof-assistant certificate, human
expert review, historical novelty, or unrestricted cancellation
claim is made.
