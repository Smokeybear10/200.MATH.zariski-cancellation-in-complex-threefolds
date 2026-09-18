# A higher-degree bound with transverse coupling

Working result: retain the FULL actual principal chart264, with
nonzero coupling, affine nonconstant intrinsic sigma, and
\(m_s\ne0\). Then
\[
\boxed{\deg_P\theta\ge3\quad\Longrightarrow\quad
       \deg_P\theta\in\{3,4\},\qquad \deg_Py\le\deg_P\theta.}
\tag{1}
\]
Here \(P=\sigma\); the degree of the zero polynomial is minus
infinity. The second inequality is the accepted result521. The
new bound follows from the full monic level and the universal
unit multiplier and minor from494, after a coefficient-field
shear that retains the derivatives of its moving coefficient.

This is only a necessary degree reduction. Neither residual
cubic nor residual quartic theta is excluded or recognized.
No assumption on the leading coefficient of the actual Z row
is made, and no coefficient-field shear is promoted to an
ambient coordinate change.

## 1. Actual inputs and exact derivatives

Retain EVERY actual hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
the genuine levels and unit evaluated gradient ideals from
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md),
and the universal conclusions of Sections1--3 of
[494](principal-paraboloid-unit-tangent-multiplier-pass494-working.md).
In particular,
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u_{\rm glob}],\quad
E=\partial_{u_{\rm glob}},\quad X=a_0u_{\rm glob}+x_0,\quad a_0\ne0,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\quad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the ENTIRE initial kernel},\\
N=[u_{\rm glob}^4]\partial_Z|_A\ne0,\quad
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,\\
Na_0=Nt=Ns=0,\quad m=k_s\ne0,\quad h=m_s\ne0,\quad p=m_t,\\
\deg_v\sigma=1,\quad P=\sigma,\quad NP=\rho\in L^*,\\
O=L[P]=L[y,\sigma,\theta],\quad
L[X,Y,Z,W]=L[X,P],\\
\operatorname{Frac}A=L(P)=\mathbb C(y,z_{\rm int},w),\quad
L[y,z_{\rm int},w]=L[P].
\end{gathered}
\tag{2}
\]
The symbol \(z_{\rm int}\) denotes the literal original
Z-intercept \(Z|_{X=0}\), not the later corrected expression
obtained by subtracting \(2ty\). Both actual returns, the original
global slice and the selected literal partial remain required.
The original slice is not assumed equal to \(X/a_0\).

The exact coefficient partials on L are the commuting extensions
from \(\mathbb C(t,s)\). In \(L[P]\) they fix P. This intrinsic
affine reparameterization is not an actual coordinate assertion.
The literal rows and original scalar are
\[
\begin{aligned}
Y&=y+PX+tX^2,\\
Z&=2ty+P^2+k_tP+m\theta+n+(2tP+k)X+t^2X^2,\\
W&=w+\theta X+sX^2,\\
mw&=\ell-(2P+k_t)y-\mathcal F(P,\theta),\\
\mathcal F(P,V)&=\frac{k_{tt}}2P^2+pPV+\frac h2V^2+n_tP+n_sV,\\
J_{t,s,P}(Y,Z,W)&=-a_0^4/\rho\in L^*.
\end{aligned}
\tag{3}
\]
The potential n is unrelated to the integer degree used below.
No rationality of L or of its exact constant subfields is assumed.
The scalar is independent of X and P, but may depend on t,s.

Write
\[
N_\theta=\deg_P\theta\ge3,\qquad
\theta=aP^{N_\theta}+\text{lower terms},\qquad a\in L^*.
\tag{4}
\]
The accepted
[521](principal-paraboloid-higher-slope-intercept-degree-bound-pass521-working.md)
gives \(\deg_Py\le N_\theta\). Below the letter \(d=N_\theta\)
is an integer, never the selected derivation N from (2).
All arguments apply uniformly to every integer \(d\ge3\);
the finite degree window from299 is not needed.

## 2. Complete formal support and universal equations

Use independent formal variables U,P,V. Set
\[
B=pP+n_s,\qquad F_{\rm base}=\frac{k_{tt}}2P^2+n_tP,
\qquad \gamma=2P+k_t.
\]
The complete off-level decomposition from521 is
\[
H-h_0=U^2+(C_1+C_2V)U+C_3V^3+C_4V^2+C_5V+C_6,
\tag{5}
\]
where
\[
\begin{aligned}
C_1&=k_{tt}P+n_t-\gamma B/m,&
C_2&=p-\gamma h/m,\\
C_3&=h_s/6-h^2/(2m),&
C_4&=h_tP/2+n_{ss}/2-3hB/(2m),\\
C_5&=m_{tt}P^2/2+n_{ts}P-\ell_s+
                   (h\ell-B^2-hF_{\rm base})/m,\\
C_6&=k_{ttt}P^3/6+n_{tt}P^2/2-\ell_tP-h_0+
                   B(\ell-F_{\rm base})/m.
\end{aligned}
\tag{6}
\]
Their formal degrees are bounded by \(2,1,0,1,2,3\),
respectively. The genuine actual level is
\(H(y,P,\theta)=h_0\). Every lower coefficient, including the
moving level, is retained. In particular the formal gradients,
taken BEFORE evaluation, are
\[
H_U=2U+C_1+C_2V,\qquad
H_V=C_2U+3C_3V^2+2C_4V+C_5.
\tag{7}
\]

Put
\[
\begin{aligned}
f&=H_U(y,P,\theta),&g&=H_V(y,P,\theta),\\
\nu&=(B+h\theta)/m,&
\beta_f&=(2y+k_{tt}P+p\theta+n_t)/m,&D_f&=\gamma/m,\\
\mathcal A&=y_t+\theta_Py_s+y_P^2,\\
\mathcal B_1&=\theta_t+
          \theta_P(y_P+\theta_s+\nu)+\beta_f+D_fy_P.
\end{aligned}
\tag{8}
\]
The FULL scalar and evaluated unit-minor identities of494 give
\[
\begin{gathered}
\mathcal A=\kappa g,\qquad
\mathcal B_1=-\kappa f,\qquad \kappa\in L^*,\\
\mathcal W=(\theta_P+D_f)g^2+
        (y_P-\theta_s-\nu)fg-y_sf^2\in L^*,\\
J_{t,s,P}=\kappa\mathcal W,\qquad (f,g)L[P]=L[P].
\end{gathered}
\tag{9}
\]
The evaluated full H-gradient also generates the unit ideal.
These are universal affine-sigma identities, not the later
conic specialization in494. In particular \(\kappa\) has no P
dependence, but is not assumed constant in t,s.

## 3. Leading gates, including unequal or zero y

Recall \(d=\deg_P\theta\ge3\) and \(\deg_Py\le d\).
In (5), a nonzero \(C_3\theta^3\) has degree \(3d\).
Every other term has degree at most \(2d+1<3d\).
Thus the full level gives
\[
h_s=3h^2/m,\qquad C_3=0.
\tag{10}
\]
This is a formal coefficient identity: the ENTIRE \(C_3V^3\)
term vanishes, not just its evaluated highest monomial.
Consequently \(\deg_Pg\le d+1\), whereas
\[
\deg_Pf=d+1,\qquad [P^{d+1}]f=-2ha/m\ne0.
\tag{11}
\]

In \(\mathcal B_1\), degree \(2d-1>d+1\) has coefficient
\[
da(a_s+ha/m).
\]
Indeed \(\theta_Py_P\) has degree at most \(2d-2\);
all terms outside \(\theta_P(\theta_s+\nu)\) have smaller
degree. Equation (9) therefore forces
\[
a_s=-ha/m.
\tag{12}
\]
If \(\deg_Py=d\), put \(r=[P^d]y\in L^*\). The coefficient
of \(P^{2d-1}\) in \(\mathcal A\) is \(da r_s\).
The term \(y_P^2\) has degree at most \(2d-2\), while
\(\deg_Pg\le d+1<2d-1\). Hence \(r_s=0\).
Define the unified moving shear coefficient by
\[
q=\begin{cases}
r/a,&\deg_Py=d,\\
0,&\deg_Py<d,
\end{cases}
\qquad R=y-q\theta.
\tag{13}
\]
This includes zero and constant y without dividing by either.
It gives \(\deg_PR<d\) and, in both branches,
\[
q_s=hq/m.
\tag{14}
\]
The coefficient of \(P^{2d+1}\) in the actual H level is now
\[
a^2\left(\frac{h_t}2-\frac{3hp}{2m}
                         -\frac{2hq}{m}\right).
\]
Thus
\[
h_t-\frac{3hp}{m}=\frac{4hq}{m}.
\tag{15}
\]
For \(\deg_Py<d\), the same computation uses \(q=0\).
No coefficient of the actual Z row was divided by.

For orientation, the exact \(s\)-constant field
\(F_0=\ker_L\partial_s\) is finite over \(\mathbb C(t)\), and
(10),(12),(14),(15) imply
\[
ma\in F_0^*,\qquad q/m\in F_0,\qquad
\lambda:=h/m^3\in F_0^*,\qquad
\lambda_t=4(q/m)\lambda.
\tag{16}
\]
These are identities in the existing field, not rational
parametrizations or ambient maps. In the unequal-degree branch,
\(q=0\) and \(\lambda\in\mathbb C^*\). In the equal-degree
branch the original Z leading coefficient is \((2tq+m)a\),
which may vanish. Nothing below assumes that it does not.

## 4. Exact moving shear, including its coefficient derivatives

Set
\[
\begin{aligned}
K&=C_4+qC_2+q^2\\
 &=q^2+pq-\frac{hk_tq}{m}
                  +\frac{n_{ss}}2-\frac{3hn_s}{2m}\in L,\\
A_R&=(2q+C_2)R+qC_1+C_5.
\end{aligned}
\tag{17}
\]
The equality in the first two lines uses precisely (15) to
cancel the P coefficient of K. Direct substitution in the
ENTIRE formal polynomial gives
\[
\begin{aligned}
(H-h_0)(qV+R,P,V)
 &=R^2+C_1R+C_6+A_RV+KV^2,\\
0&=R^2+C_1R+C_6+A_R\theta+K\theta^2,\\
f&=(2q+C_2)\theta+2R+C_1,\qquad
G:=g+qf=2K\theta+A_R.
\end{aligned}
\tag{18}
\]
Only polynomial identities over L are asserted here.

For the derivative equations define
\[
\begin{aligned}
K_\theta&=y_P+\theta_s+\nu,\\
L_R&=R_s+qR_P-\frac{q(B+q\gamma)}m,\\
J_R&=\frac{2R+k_{tt}P+n_t+\gamma R_P}{m},\\
\eta_q&=q_t-\frac{q(2q+p)}m.
\end{aligned}
\tag{19}
\]
The symbol \(J_R\) is an auxiliary polynomial, not the original
Jacobian scalar. Expansion of the COMPLETE expressions (8),(9),
using (14) and no vanishing of \(q_t\), gives
\[
\boxed{\mathcal A-q\mathcal B_1
=R_t+R_P^2+\eta_q\theta+\theta_PL_R-qJ_R
=\kappa G.}
\tag{20}
\]
For example, before (14) the additional term is
\((q_s-qh/m)\theta\theta_P\). Its cancellation is licensed by
(14), whereas the full \(\eta_q\theta\) term is retained.
The complete transformed minor is
\[
\boxed{\mathcal W=-L_Rf^2+
 (2R_P-K_\theta-2qD_f)fG+(\theta_P+D_f)G^2\in L^*.}
\tag{21}
\]
One obtains this by writing \(g=G-qf\) in (9). It retains
every moving coefficient and lower gradient contribution.

The original \(\mathcal B_1\) equation also gives the useful
bound
\[
\deg_PK_\theta\le2.
\tag{22}
\]
If its degree were greater than two, then
\(\theta_PK_\theta\) would have degree greater than \(d+1\).
All other terms of \(\mathcal B_1\) have degree at most d,
whereas \(-\kappa f\) has degree \(d+1\). This is impossible.
The zero polynomial \(K_\theta\) causes no division or exception.

## 5. Remainders of degree at most d minus two

Suppose first \(\deg_PR\le d-2\), including \(R=0\).
In the actual equation (18), \(K\theta^2\), if nonzero, would
be the unique term of degree \(2d\). Indeed
\(\deg_P A_R\le\max(\deg_PR+1,2)\le d-1\), and the remaining
free terms have degree strictly less than \(2d\). Hence \(K=0\).

If \(c=\deg_PR\ge2\), then \(A_R\) has exact degree \(c+1\),
with nonzero leading coefficient \(-2h[P^c]R/m\). The other
summand \(qC_1+C_5\) has degree at most two. Thus \(A_R\theta\)
has degree \(d+c+1\), strictly exceeding the degrees
\(2c,c+2,3\) of \(R^2,C_1R,C_6\). This contradicts (18).
Therefore
\[
\deg_PR\le1,\qquad K=0
\tag{23}
\]
in this branch; the zero polynomial is still included.

The possibility \(A_R=0\) is ruled out by the FULL evaluated
gradient ideal, not by assuming irreducibility. If \(A_R=0\),
the actual equation (18) gives \(R^2+C_1R+C_6=0\) as a
polynomial identity. The entire formal polynomial then factors:
\[
H-h_0=(U-qV-R)
       \big(U+(q+C_2)V+C_1+R\big).
\tag{24}
\]
The first factor evaluates to zero and the complementary factor
evaluates to f, of exact degree \(d+1\) by (11). In the formal
variable order U,P,V, all evaluated H-gradient components are
\[
f\,(1,-R_P,-q).
\]
Thus their ideal is contained in the proper ideal \((f)\),
contrary to296. In particular no zero or constant R boundary
escapes this argument.

Consequently \(A_R\ne0\), and (18),(23) imply
\[
d+\deg_PA_R\le3.
\tag{25}
\]
Since \(d\ge3\), this branch has exactly
\[
d=3,\qquad \deg_PR\le1,\qquad K=0,\qquad A_R\in L^*.
\tag{26}
\]
The last assertion allows a nonzero constant coefficient A_R;
it does not assert any realization or recognition.

## 6. The top remainder cannot occur in degree at least five

The only other possibility is
\[
\deg_PR=d-1,\qquad b=[P^{d-1}]R\in L^*.
\tag{27}
\]
Degree \(2d\) in the complete equation (18) gives
\[
Ka^2-\frac{2hab}{m}=0,\qquad
K=\frac{2hb}{ma}\ne0.
\tag{28}
\]
The terms \(R^2,C_1R,C_6\) have smaller degree for every
\(d\ge3\). Moreover,
\[
\begin{gathered}
\deg_Pf=d+1,\qquad F:=[P^{d+1}]f=-2ha/m,\\
\deg_PG=d,\qquad G_0:=[P^d]G=2hb/m.
\end{gathered}
\tag{29}
\]
For G, the leading coefficients of \(2K\theta\) and \(A_R\)
are \(4hb/m\) and \(-2hb/m\), so their difference is nonzero.

Assume now \(d\ge5\). In (20), every term other than
\(R_P^2\) and \(\theta_PL_R\) has degree at most d:
\(\deg R_t\le d-1\), \(\deg J_R\le d-1\),
\(\deg(\eta_q\theta)\le d\), and \(\deg(\kappa G)=d\).
But \(R_P^2\) has degree \(2d-4>d\), with coefficient
\((d-1)^2b^2\). If \(\deg L_R>d-3\), its product with
\(\theta_P\) would be uniquely highest. Comparing the
coefficient of \(P^{2d-4}\) therefore gives
\[
\deg_PL_R\le d-3,\qquad
\ell_R:=[P^{d-3}]L_R=-\frac{(d-1)^2b^2}{da}.
\tag{30}
\]
All denominators here are nonzero field elements or positive
integers. No coefficient derivative was set to zero.

Because \(d-2\ge3\), (22) shows that
\(2R_P-K_\theta-2qD_f\) has exact degree \(d-2\), with
leading coefficient \(2(d-1)b\). Thus all three summands in
(21) have degree at most \(3d-1\), whose complete coefficient is
\[
\begin{aligned}
[P^{3d-1}]\mathcal W
 &=-\ell_RF^2+2(d-1)bFG_0+daG_0^2\\
 &=\frac{F^2b^2}{da}
   =\frac{4h^2ab^2}{dm^2}\ne0.
\end{aligned}
\tag{31}
\]
This contradicts \(\mathcal W\in L^*\). Hence (27) requires
\(d\le4\).

The threshold \(d\ge5\) is essential to this particular
comparison. At \(d=4\), \(2d-4=d\), so the retained
\(\eta_q\theta\) and other degree-d terms can contribute in
(20); also \(R_P\) has degree two and can tie \(K_\theta\).
They have not been discarded or used to exclude the quartic
case. At \(d=3\) the same high-degree comparison is not invoked.

## 7. Conclusion, verification and unresolved scope

Equations (26)--(31) prove (1). More precisely, with q and R
defined by (13), the remaining possibilities satisfy
\[
\begin{cases}
d=3,\ \deg_PR\le1,\ K=0,\ A_R\in L^*,\\
\text{or}\\
d\in\{3,4\},\ \deg_PR=d-1,\
K=2h[P^{d-1}]R/(ma)\ne0.
\end{cases}
\tag{32}
\]
In particular a quartic theta forces a cubic R. This includes
the unequal-degree case \(q=0\), the equal-degree case with
nonconstant q, all zero and constant lower remainders, and the
possible drop of the original Z leading coefficient. It does
not require \(p=m_t\ne0\), a nonzero \(q_t\), or a choice of
an algebraic root.

Fresh unsaved inline computation219fcb reconstructed the entire
formal H from its original potential definition, all six
coefficients (6), K's P cancellation, the whole substitution
(18), the complete moving identity (20) and full minor (21).
Every residual was zero. It separately checked the unrestricted
lower-coefficient leading gates for \(d=3,4,5,6\), with
\(\deg y=d,d-1,0,-\infty\), and the symbolic all-d expression
(31), again with zero residuals. These checks supplement the
uniform degree proof; they are not a finite-degree surrogate.

Root independently reconstructed the full moving identities and
all terms at the threshold \(d=5\). General's independent fresh
e21972 reconstructed the full formal support, shear, derivative
terms and all-d coefficient, including arbitrary lower-support
checks in degrees five and six. These were outline checks; a
complete independent saved-source review is separate from the
author hold of this note.

The result is conditional on the supplied actual chart and all
its retained hypotheses. It neither arranges affine sigma in an
arbitrary chart nor solves the remaining cubic and quartic
systems. There is no claim of arbitrary chart entry, ambient
recognition, unrestricted cancellation, novelty or external
certification. No saved checker was executed, imported, compiled
or rerun, and no earlier source or canonical record was edited.
