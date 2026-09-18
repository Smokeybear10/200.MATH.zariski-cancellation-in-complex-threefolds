# An invariant-intercept exclusion in the variable-coupling affine-line branch

Working theorem: retain EVERY actual hypothesis of264. In the
birational projected-line branch with nonconstant sigma and
\(m=k_s\notin\mathbb C\), suppose the normalized intrinsic data are
\[
y=r\in L,\qquad \theta=\mu P+h,\qquad
w_{\rm int}=bP+c,\qquad P=\sigma,
\qquad (\partial_t+\mu\partial_s)r=0.
\tag{1}
\]
Then the full scalar equations force \(m\in\mathbb C\), a
contradiction. Thus no actual chart with these hypotheses exists.
Equivalently, in the normalized variable-coupling branch with both
specified slopes zero, the necessary condition is \(\mathcal Dr\ne0\).

The zero y-slope, zero quadratic W-intercept coefficient and final
directional condition in(1) are extra assumptions. They are not
deduced for the whole variable-coupling branch. Section6 gives their
precise transport from a larger-looking but equivalent constant-slope
formulation. No irreducibility hypothesis on the third surface or
published recognition endpoint is used. This is not a solution of
unrestricted cancellation.

## 1. Actual chart, exact field and genuine high identities

Retain the full entry of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
including the entire initial ideal, original global slice, literal
selected partial, both returns and full scalar:
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad
\deg_E(X,Y,Z,W)=(1,2,2,2),\quad a_0=EX\ne0,\\
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2),\quad
N=[u^4]\partial_Z|_A\ne0,\quad Na_0=Nt=Ns=0,\\
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,
\quad O=L[v],\quad Nv=1,\\
K=\operatorname{Frac}A=L(v)=\mathbb C(y,z,w_{\rm int}),\quad
L[y,z,w_{\rm int}]=L[y,\sigma,\theta]=O,\\
J_{t,s,v}(X)=-a_0^4\in L^*.
\end{gathered}
\tag{2}
\]
The last three-generator equality is licensed by \(m=k_s\ne0\).
The coefficient partials commute and have joint constants \(\mathbb C\).
Neither the exact field L nor its constant subfields are presumed
rational. The original intercept in \(X=a_0u+x_0\) is retained.

Assume the projected plane curve is a line and its function-field
projection is birational. By
[325](principal-paraboloid-all-specializations-affine-line-profile-pass325-working.md)
all three intrinsic functions are affine. Nonconstant sigma makes
\(P=\sigma\) a polynomial parameter of O, with \(NP=\rho\in L^*\).
Coefficient derivatives from now on fix P and agree with the old
derivatives on L. The scalar in this basis is \(-a_0^4/\rho\).

For \(\mathcal D=\partial_t+\mu\partial_s\), distinguish its
iterates from the frozen directional sums
\[
\begin{aligned}
\mathcal K_j&=\sum_{i=0}^j\binom ji\mu^i k_{t^{j-i}s^i},\qquad j=2,3,4,\\
\beta&=m_t+\mu m_s,\qquad
\mathcal M_2=m_{tt}+2\mu m_{ts}+\mu^2m_{ss},\quad
\kappa=\mathcal D\mu.
\end{aligned}
\tag{3}
\]
The full second potential gives the quadratic W-intercept coefficient
\(-(2\lambda+\mathcal K_2/2)/m\), where \(\lambda\) is the y-slope.
Both coefficients are zero in(1), hence \(\mathcal K_2=0\).
The complete third and corrected fourth potentials of264/296 give
\(\mathcal K_3/6=0\) and \(\mathcal K_4/24=0\), respectively.
These are the specialization \(\lambda=\omega=0\) of the exact
leaders in
[474, Sections2--3](principal-paraboloid-variable-coupling-affine-line-high-gates-pass474-working.md).
All lower coefficients and both moving levels are retained; they
cannot contribute to these highest powers of P.

## 2. The characteristic slope is constant along its own direction

Commuting the exact coefficient partials gives
\[
\begin{aligned}
\mathcal D\mathcal K_2&=\mathcal K_3+2\kappa\beta,\\
\mathcal D\mathcal K_3&=\mathcal K_4+3\kappa\mathcal M_2,\\
\mathcal D\beta&=\mathcal M_2+\kappa m_s.
\end{aligned}
\tag{4}
\]
Thus \(\kappa\beta=\kappa\mathcal M_2=0\). If \(\kappa\ne0\),
then \(\beta=\mathcal M_2=0\), and the last identity forces
\(m_s=0\). The definition of beta then forces \(m_t=0\), contrary
to \(m\notin\mathbb C\). Therefore
\[
\mathcal D\mu=0,\qquad
a_1:=\mathcal Dk=k_t+\mu m,\qquad
\mathcal Da_1=\mathcal K_2+m\kappa=0.
\tag{5}
\]
Set \(\mathscr F=\ker_L\mathcal D\). In addition to \(\mu,a_1\),
\[
\chi=s-\mu t\in\mathscr F,\qquad
\phi=k-a_1t\in\mathscr F.
\tag{6}
\]
No division by beta, \(m_s\), \(\mu\), or \(a_1\) was made.

The strong return in(2) forces \(r\notin\mathbb C\): if r were
complex, K would be generated over \(\mathbb C\) by only z and
\(w_{\rm int}\), contrary to its transcendence degree three.
The extra assumption \(\mathcal Dr=0\) then gives \(r_s\ne0\).
Indeed \(r_s=0\) would also give \(r_t=0\) and make r complex.
Thus \((t,r)\) is a separating coefficient basis and
\[
[L:\mathbb C(t,r)]<\infty,\qquad
\mathcal D=\partial_t|_r,\qquad
\partial_r|_t=r_s^{-1}\partial_s.
\tag{7}
\]
The two derivations commute by uniqueness through the finite
separable extension. In particular the r derivative preserves
\(\mathscr F\), whose r constants are exactly \(\mathbb C\).

For completeness \(\mathscr F\) is finite over \(\mathbb C(r)\).
Differentiate the monic minimal polynomial over \(\mathbb C(t,r)\)
of an element killed by \(\partial_t|_r\). Its differentiated
polynomial has smaller degree and vanishes on that element, so
all original coefficients are t-constant. It is therefore algebraic
over \(\mathbb C(r)\). Finite subextensions of this algebraic
constant field have degrees bounded by \([L:\mathbb C(t,r)]\),
since t is transcendental over them; their union is finite as well.
Neither \(\mathscr F=\mathbb C(r)\) nor \(L=\mathscr F(t)\)
is needed below.

## 3. Complete literal rows in the separating basis

Use the rational function \(\zeta=P+tX\). This is not yet
an original polynomial coordinate or the original global slice u.
Define
\[
G=2tr+mh+n,\qquad H_1=h-bt.
\tag{8}
\]
The full original expansions become
\[
\begin{aligned}
Y&=r+X\zeta,\\
Z&=\zeta^2+a_1\zeta+G+\phi X,\\
W&=b\zeta+c+H_1X+\mu X\zeta+\chi X^2.
\end{aligned}
\tag{9}
\]
This follows directly from
\(z=2tr+P^2+k_tP+m(\mu P+h)+n\),
the original Z-linear coefficient \(2tP+k\), and(1).
In(9), \(\mu,a_1,\chi,\phi\in\mathscr F\); the other
coefficients may still vary with t.

At fixed X the change \((t,s,P)\mapsto(t,r,\zeta)\)
has determinant \(r_s\). Hence the exact full calibration is
\[
J_{t,r,\zeta}(X)=-\frac{a_0^4}{\rho r_s}\in L^*.
\tag{10}
\]
It is independent of both X and zeta. All t and r subscripts
in the rest of the proof refer to the exact basis(7).
The complete derivative matrix of(9) is
\[
\begin{pmatrix}
0&1&X\\
G_t&(a_1)_r\zeta+G_r+\phi_rX&2\zeta+a_1\\
b_t\zeta+c_t+(H_1)_tX&
b_r\zeta+c_r+(H_1)_rX+\mu_rX\zeta+\chi_rX^2&b+\mu X
\end{pmatrix}.
\tag{11}
\]
Its \(X^0\zeta^2\) and \(X^0\zeta\) coefficients are
\(2b_t\) and \(a_1b_t+2c_t\). Therefore \(b_t=c_t=0\),
so \(b,c\in\mathscr F\). After these gates, the ENTIRE determinant is
\[
\begin{aligned}
J={}&-bG_t\\
&+\{G_tb_r+2(H_1)_t\}X\zeta\\
&+\{a_1(H_1)_t+G_t(c_r-\mu)\}X\\
&+\{G_t\mu_r-(a_1)_r(H_1)_t\}X^2\zeta\\
&+\{G_t(H_1)_r-G_r(H_1)_t\}X^2\\
&+\{G_t\chi_r-(H_1)_t\phi_r\}X^3.
\end{aligned}
\tag{12}
\]
In particular \(bG_t\ne0\) by(10), so \(G\notin\mathscr F\).
No lower scalar equation has been silently discarded.

## 4. Every surviving integration constant is complex

Put \(\epsilon=-b_r/2\in\mathscr F\). The \(X\zeta\)
coefficient in(12) gives \((H_1)_t=\epsilon G_t\), whence
\(H_1=\epsilon G+h_0\), with \(h_0\in\mathscr F\).
Here \(h_0\) is a new integration constant in this section,
not the moving third-potential level.
The \(X^2\) coefficient becomes
\[
G_t(\epsilon_rG+(h_0)_r)=0.
\tag{13}
\]
Since \(G\notin\mathscr F\) and both coefficients in parentheses
belong to \(\mathscr F\), each coefficient is zero. Thus
\(\epsilon,h_0\in\mathbb C\). Integrating the remaining
identities inside the exact field gives
\[
\begin{aligned}
b&=-2\epsilon r+b_0,& H_1&=\epsilon G+h_0,\\
\mu&=\epsilon a_1+\mu_0,&
\chi&=\epsilon\phi+\chi_0,&
c&=\mu_0r+c_0,\\
\epsilon,b_0,h_0,\mu_0,\chi_0,c_0&\in\mathbb C.
\end{aligned}
\tag{14}
\]
Specifically the \(X^2\zeta\), \(X^3\), then X coefficients
give the last three r-derivative identities. Subtracting the
displayed expressions leaves elements killed by both exact
partials, so the constants are complex. Only the already-nonzero
\(G_t\) was divided out. Zero values of epsilon, \(a_1\),
phi and the optional constants are all permitted.

## 5. The coefficient coupling is forced to be complex

The relations \(s=\mu t+\chi\) and \(k=a_1t+\phi\) in(6),
together with the complex constants in(14), give
\[
s=(\epsilon a_1+\mu_0)t+\epsilon\phi+\chi_0
 =\epsilon k+\mu_0t+\chi_0.
\tag{15}
\]
Apply the ORIGINAL partial \(\partial_s\) at fixed t. This
is an identity in L, so the earlier switch to the exact basis
\((t,r)\) does not prevent doing so. Since the three constants
in(15) are complex and \(k_s=m\),
\[
1=\epsilon m.
\tag{16}
\]
If epsilon is zero this is already impossible. Otherwise it
forces \(m=1/\epsilon\in\mathbb C\), contradicting the
standing hypothesis. This exhausts the zero branch without
dividing by epsilon in advance and proves the exclusion.

The contradiction is entirely within the full scalar and exact
coefficient system. No coefficient-field expression is promoted
to a polynomial coordinate. In particular no normality argument,
invariant-coordinate recognition theorem, or hypothesis about
the factorization of the third surface is needed at the endpoint.

## 6. Optional complex-slope transport, with the extra condition preserved

Start instead with the actual affine data
\[
y=\lambda P+r_{\rm old},\quad
\theta=\mu_{\rm old}P+h,\quad
w_{\rm int}=\omega P^2+bP+c,
\qquad \lambda,\omega\in\mathbb C.
\tag{17}
\]
The ACTUAL polynomial reframe
\[
X_*=X+\lambda,\quad Y_*=Y,\quad Z_*=Z,\quad W_*=W-\omega Z
\tag{18}
\]
has an explicit polynomial inverse. It belongs to the filtered
class in
[426](general-coupling-normalization-obstruction-pass426-working.md),
so retains the full initial ideal, selected leading derivation,
exact field, original slice, both returns and scalar. Its precise
coefficient transport is
\[
\begin{gathered}
t_*=t,\quad s_*=s-\omega t^2,\quad m_*=m,\quad
k_*=k+2\lambda t^2,\quad P_*=P-2\lambda t,\\
r_*=r_{\rm old}+\lambda^2t,\quad
\mu_* =\mu_{\rm old}-2\omega t,\quad
\lambda_*=\omega_*=0,\quad
\mathcal D_* =\mathcal D_{\rm old}.
\end{gathered}
\tag{19}
\]
Here the last equality uses the exact starred partials, not
differentiation at fixed old s. Consequently the excluded
directional condition in this original frame is
\[
\mathcal D_{\rm old}r_{\rm old}=-\lambda^2.
\tag{20}
\]
Complex slopes alone do NOT imply(20). Instead the proved
necessary condition for any actual variable-coupling chart with
these complex slopes is
\(\mathcal D_{\rm old}r_{\rm old}\ne-\lambda^2\).
Neither this section nor Section2 claims that the excluded
directional intercept condition is automatic.

## 7. Verification and scope

The full264,296,325,426 and held474 sources were read before
authoring. Fresh unsaved root algebra4bcd05 reconstructed(4),
the entire post-gate determinant(12) and additional identities
from a provisional longer recognition argument, with all
residuals zero. Separate fresh reconstruction173a3e checked the
normalization and full raw determinant. Review of the provisional
source noticed that the presumed recognition family is empty;
the direct contradiction(15),(16) replaces that unnecessary
endpoint. Independent full-source review of this strengthened
exclusion version is recorded separately after handoff.

This proof retains the actual chart-entry dependencies of264
and the affine reduction325; they are not recursively recertified
here. It excludes only(1), or equivalently the specified
transported conditions(17),(20). Other affine-line
data, nonlinear projected curves, other initial kernels and
arbitrary entry into this chart remain outside the conclusion.
No saved checker was executed, imported, compiled or rerun.
No human expert review, Lean certification, historical novelty,
public submission or unrestricted cancellation result is claimed.
