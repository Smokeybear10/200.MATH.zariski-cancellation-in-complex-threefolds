# Variable coupling with zero quadratic W-slope: a scalar exclusion and a quadratic coupling form

Working result: retain the full actual264 hypotheses, variable
coupling \(m=k_s\notin\mathbb C\), a birational projected line,
and nonconstant sigma. Suppose the quadratic coefficient omega
of the intrinsic W-intercept is complex. After the actual shear
\(W_*=W-\omega Z\), use the normalized data
\[
y=\lambda P+r,\quad \theta=\mu P+h,\quad
w_{\rm int}=bP+c,\quad P=\sigma.
\tag{1}
\]
Then \(\lambda\notin\mathbb C\),
\(\beta=(\partial_t+\mu\partial_s)m\ne0\), and
\(\kappa=(\partial_t+\mu\partial_s)\mu\ne0\).
There are complex constants \(A,B,C,D,E,\lambda_0\), with
\((A,B)\ne(0,0)\), for which
\[
\boxed{\begin{aligned}
m&=At+Bs+C,\\
k&=-2\lambda_0t^2+Ats+\frac B2s^2+Cs+Dt+E,\\
\lambda&=\lambda_0-\frac A2\mu-\frac B4\mu^2.
\end{aligned}}
\tag{2}
\]
These formulas concern the normalized coefficient variables.
For the original frame, substitute \(s_*=s-\omega t^2\);
the original k need not be quadratic in the original t,s.

The note excludes the \(\kappa=0\) alternative by the complete
original scalar, including a separate zero moving-intercept case.
It does not exclude or realize the remaining family (2), solve its
lower potentials or returns, or give a recognition theorem.

## 1. Actual scope and the licensed normalization

Retain every actual hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
the full genuine fourth potential and minor units of
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md),
and the birational projected-line reduction of
[325](principal-paraboloid-all-specializations-affine-line-profile-pass325-working.md).
In particular,
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad
\deg_E(X,Y,Z,W)=(1,2,2,2),\quad a_0=EX\ne0,\\
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the entire initial kernel},\\
N=[u^4]\partial_Z|_A\ne0,\quad Na_0=Nt=Ns=0,\quad
L=\operatorname{Frac}\ker_A N,\quad[L:\mathbb C(t,s)]<\infty,\\
O=L[v]=L[y,\sigma,\theta]=L[y,z,w_{\rm int}],\quad Nv=1,\quad
K=L(v)=\mathbb C(y,z,w_{\rm int}),\quad
J_{t,s,v}(X)=-a_0^4\in L^*.
\end{gathered}
\tag{3}
\]
The exact coefficient partials commute, with joint constant field
\(\mathbb C\). Both returns, the original slice, and the literal
selected partial are retained. No rationality of L, reducibility
of a surface, or plane-normality assumption is imposed.

By325 all three intrinsic generators are affine. Nonconstant
sigma makes \(P=\sigma\) a parameter of O, with \(NP=\rho\in L^*\).
Coefficient derivatives on O now fix P; their restrictions to L
are the same exact coefficient derivatives. The calibrated scalar is
\[
J_{t,s,P}(X)=-a_0^4/\rho\in L^*.
\tag{4}
\]
This does not set \(NP=1\) or identify P with the original slice.

If the original quadratic W-intercept coefficient is
\(\omega\in\mathbb C\), use the ACTUAL map
\[
X_*=X,\quad Y_*=Y,\quad Z_*=Z,\quad W_*=W-\omega Z.
\tag{5}
\]
Its inverse adds \(\omega Z_*\) to \(W_*\). The filtered
transport of the fully read
[426](general-coupling-normalization-obstruction-pass426-working.md)
preserves every actual gate in (3), including the full initial
ideal, both returns and scalar. In particular
\(\partial_{Z_*}=\partial_Z+\omega\partial_W\), whose leading
shift-four derivation is still N by the retained omitted-partial bound.
The exact coefficient transport is
\[
\begin{gathered}
t_*=t,\quad s_*=s-\omega t^2,\quad k_*=k,\quad m_*=m,\quad
P_*=P,\quad \lambda_* =\lambda,\quad \omega_*=0,\\
\mu_* =\mu-2\omega t,\quad
\partial_{t_*}=\partial_t+2\omega t\partial_s,\quad
\partial_{s_*}=\partial_s,\quad \mathcal D_* =\mathcal D_{\rm old}.
\end{gathered}
\tag{6}
\]
The new W-intercept is affine in P, and theta remains affine.
The birational projected-line condition and nonconstant sigma persist.
By the held
[477](principal-paraboloid-variable-coupling-complex-slope-exclusion-pass477-working.md),
the two original slopes cannot both be complex. Hence lambda is
noncomplex. From now on drop stars and work in (1), so all t,s
derivatives and the conclusion (2) refer to this normalized frame.

## 2. Zero-safe consequences of the entire high system

Let \(\mathcal D=\partial_t+\mu\partial_s\). As in
[474](principal-paraboloid-variable-coupling-affine-line-high-gates-pass474-working.md),
write frozen Taylor sums
\[
\begin{aligned}
\mathcal K_j&=\sum_{i=0}^j\binom ji\mu^i k_{t^{j-i}s^i}
                                                    &&(j=2,3,4),\\
\beta&=m_t+\mu m_s,\quad
\mathcal M_2=m_{tt}+2\mu m_{ts}+\mu^2m_{ss},\\
\mathcal M_3&=m_{ttt}+3\mu m_{tts}+3\mu^2m_{tss}+\mu^3m_{sss},\quad
B_2=\mathcal M_2/2,\quad C_3=\mathcal M_3/6.
\end{aligned}
\tag{7}
\]
These are not iterates of the derivation \(\mathcal D\).
The zero quadratic W-slope gives \(\mathcal K_2=-4\lambda\),
and the complete genuine third and fourth leaders give
\(\mathcal K_3=\mathcal K_4=0\). The exact high one-forms and
minor identity specialize to
\[
\begin{aligned}
2d\lambda+\beta\,d\mu+B_2(ds-\mu\,dt)&=0,\\
B_2\,d\mu+C_3(ds-\mu\,dt)&=0,\qquad B_2^2=\beta C_3,\\
2B_2\,d\lambda&=0.
\end{aligned}
\tag{8}
\]
Here d is the coefficient differential. These identities come
from the full corrected fourth potential, with both moving levels
retained, and not from an arbitrary quartic containing the line.

Since lambda is noncomplex, \(d\lambda\ne0\). The last
identity forces \(B_2=0\). If beta were zero, the first form
would force \(d\lambda=0\), impossible. Thus beta is nonzero,
and the minor identity forces \(C_3=0\). We have proved
\[
\boxed{\mathcal K_2=-4\lambda,\quad
\mathcal K_3=\mathcal K_4=\mathcal M_2=\mathcal M_3=0,\quad
\beta\ne0,\quad 2d\lambda+\beta\,d\mu=0.}
\tag{9}
\]
In particular mu is noncomplex too. None of these deductions
assumes beta nonzero in advance, divides by lambda, or uses
the redundant highest constant scalar coefficient from474.

## 3. The coefficient family when kappa vanishes

Suppose first that \(\kappa=\mathcal D\mu=0\). Then
\(\mu_s\ne0\), since otherwise \(\mu_t=0\) and mu would be
complex. The exact coefficient basis \((t,q)\), with \(q=\mu\),
is separating, and
\[
\dot{\ }=\partial_t|_q=\mathcal D,\qquad
{}'=\partial_q|_t=\mu_s^{-1}\partial_s,\qquad
\mathscr F=\ker_L\mathcal D.
\tag{10}
\]
The commuting extensions have joint constants \(\mathbb C\).
The field \(\mathscr F\) is finite over \(\mathbb C(q)\), by
the exact minimal-polynomial argument of474 Section6: differentiating
the monic minimal polynomial of a dot-constant makes its coefficients
t-constant, and their finite extension degrees are bounded by
\([L:\mathbb C(t,q)]\). No equality \(\mathscr F=\mathbb C(q)\)
or \(L=\mathscr F(t)\) is used.

Equation (9) gives \(\lambda\in\mathscr F\) and
\(\beta=-2\lambda'\ne0\). Also
\(\mathcal D\beta=\mathcal M_2+m_s\kappa=0\).
Integrating existing coefficient functions by subtracting explicit
polynomials in t gives elements \(\chi,M,A_1,\Phi\in\mathscr F\)
such that
\[
\begin{aligned}
s&=qt+\chi,\qquad m=\beta t+M,\qquad
k=-2\lambda t^2+A_1t+\Phi,\\
\beta&=-2\lambda',\qquad
A_1'=\beta\chi'+M,\qquad \Phi'=M\chi'.
\end{aligned}
\tag{11}
\]
For k the second dot derivative is
\(\mathcal D^2k=\mathcal K_2+m\kappa=-4\lambda\).
The last two identities in (11) follow by comparing the q
derivative of k with \(k_s s_q=m(t+\chi')\).
The coefficient basis has \(s_q=t+\chi'=1/\mu_s\ne0\).
All integrations take place in the exact field; no new primitives
are adjoined.

## 4. The moving center and the zero intercept-derivative case

In this section t and q partials mean (10), with the intrinsic
parameter fixed as specified. Define
\[
\begin{aligned}
\zeta&=P+t(X-\lambda),&R&=r+\lambda^2t,\\
G&=2tr+mh+n-\lambda^2t^2+A_1\lambda t,\\
C_0^{\rm mov}&=c+b\lambda t,&
H_0^{\rm mov}&=h-bt+q\lambda t.
\end{aligned}
\tag{12}
\]
For shorter matrix notation write the two last functions as C,H
in Sections4--5. They are not yet constant-field elements.
The ORIGINAL literal rows become exactly
\[
Y=R+(X+\lambda)\zeta,\qquad
Z=\zeta^2+A_1\zeta+G+\Phi X,\qquad
W=(b+qX)\zeta+C+HX+\chi X^2.
\tag{13}
\]
For example \(k_t+qm=\mathcal Dk=-4\lambda t+A_1\)
gives the P coefficient \(2t(X-\lambda)+A_1\) in Z;
substituting (12) then gives its entire constant part in (13).
No L-valued change of actual polynomial coordinates is made.

The change from \((t,s,P)\) to \((t,q,\zeta)\) at fixed X
has determinant \(\mu_s\), including the moving center.
Thus the full scalar remains a nonzero element of L. Its exact
derivative matrix is
\[
\begin{pmatrix}
R_t&R_q+\lambda'\zeta&X+\lambda\\
G_t&A_1'\zeta+G_q+\Phi'X&2\zeta+A_1\\
b_t\zeta+C_t+H_tX&(b_q+X)\zeta+C_q+H_qX+\chi'X^2&b+qX
\end{pmatrix}.
\tag{14}
\]
In particular its \(\zeta^3\) coefficient is
\(2\lambda'b_t\). Since \(\lambda'\ne0\), it forces
\(b_t=0\), so \(b\in\mathscr F\). After this gate, the
ENTIRE \(\zeta^2\) coefficient is
\[
2\{-R_t(b'+X)+\lambda'(C_t+H_tX)\}.
\tag{15}
\]
The X term inside \(b'+X\) is essential: it is the q derivative
of the coefficient \(qX\) in W and cannot be omitted.

If \(R_t=0\), equation (15) gives \(C_t=H_t=0\).
The only possibly nonzero entry in the first column of (14)
is now \(G_t\). Its determinant has \(X^2\zeta\) coefficient
exactly \(G_t\), so calibration forces \(G_t=0\) as well.
The entire determinant is then zero, a contradiction. Therefore
\[
R_t\ne0,
\qquad H_t=R_t/\lambda',\qquad C_t=R_tb'/\lambda'.
\tag{16}
\]
This proves the necessary nonzero gate before changing coefficient
basis or dividing by the moving intercept derivative.

## 5. The complete remaining determinant has a quadratic factor

Use the separating coefficient basis \((R,q)\). Its exact
partials commute, with joint constants \(\mathbb C\), and
\(\mathscr F=\ker\partial_R\). Derivatives of elements of
\(\mathscr F\) with respect to q agree with the primes in (10).
The complete scalar in \((R,q,\zeta)\) is
\[
J=-\frac{a_0^4}{\rho\mu_sR_t}\in L^*.
\tag{17}
\]
Set
\[
\eta=1/\lambda'\in\mathscr F^*,\qquad
\epsilon=b'/\lambda'\in\mathscr F.
\]
Integrating (16) inside the exact field gives
\(H=\eta R+H_0\), \(C=\epsilon R+C_0\), with
\(H_0,C_0\in\mathscr F\). These are coefficient expressions,
not actual coordinate replacements. The exact derivative matrix is
\[
\begin{pmatrix}
1&\lambda'\zeta&X+\lambda\\
G_R&A_1'\zeta+G_q+\Phi'X&2\zeta+A_1\\
\epsilon+\eta X&(b'+X)\zeta+\epsilon'R+C_0'
                          +(\eta'R+H_0')X+\chi'X^2&b+qX
\end{pmatrix}.
\tag{18}
\]
Its quadratic and cubic zeta coefficients are already zero by
construction. Put
\[
\mathcal Z=G_R-A_1'/\lambda',\qquad
\mathcal P(X)=(X+\lambda)(b'+X)-\lambda'(b+qX).
\tag{19}
\]
The ENTIRE remaining zeta coefficient is
\[
\mathcal Z\mathcal P(X)
 -2\{\epsilon'R+C_0'+(\eta'R+H_0')X+\chi'X^2\}.
\tag{20}
\]
Since \(\mathcal P\) is monic quadratic, its \(X^2\)
coefficient gives \(\mathcal Z=2\chi'\in\mathscr F\).
The other two coefficients become
\[
\begin{aligned}
\eta'R+H_0'&=\chi'(\lambda+b'-\lambda'q),\\
\epsilon'R+C_0'&=\chi'(\lambda b'-\lambda'b).
\end{aligned}
\tag{21}
\]
Their right sides belong to \(\mathscr F\), whereas
\(R\notin\mathscr F\) by (16). Therefore
\(\eta'=\epsilon'=0\). The joint constant field now gives
complex constants \(\alpha,\lambda_0,b_1,b_0\), with
\(\alpha\ne0\), such that
\[
\lambda=\alpha q+\lambda_0,\qquad
b=b_1q+b_0,
\quad
H_0'=(\lambda_0+b_1)\chi',\qquad
C_0'=(\lambda_0b_1-\alpha b_0)\chi'.
\tag{22}
\]
Here \(\alpha=\lambda'=1/\eta\) and
\(b_1=\alpha\epsilon\); no nonvanishing of b or epsilon
has been assumed. Also (11) and \(\mathcal Z=2\chi'\) give
\[
G_R=A_1'/\alpha+2\chi'=M/\alpha,
\qquad G=MR/\alpha+G_0,\quad G_0\in\mathscr F.
\tag{23}
\]

After (22),(23) and \(\Phi'=M\chi'\), the ENTIRE determinant
of (18), not merely its top part, is
\[
\boxed{
J=\frac{F(X)}{\alpha}
 \{-G_q+\chi'(\lambda M-\alpha A_1)\},\qquad
F(X)=X^2+(\lambda_0+b_1)X+\lambda_0b_1-\alpha b_0.
}
\tag{24}
\]
Here \(G_q\) is taken at fixed R, and the expression in braces
belongs to L and is independent of X. To check the complete
factorization directly, the constant zeta part of (18) is
\[
-\frac{\mathcal P(X)}{\alpha}(G_q+\Phi'X)
 +(C_0'+H_0'X+\chi'X^2)
       \{(X+\lambda)G_R-A_1\}.
\tag{25}
\]
Equations (22) make its parenthesized coefficient
\(\chi'F(X)\), while \(\mathcal P=F\); equations (23)
and \(\Phi'=M\chi'\) then give (24).

If the braces in (24) vanish, J is zero. Otherwise J has exact
X-degree two because F is monic. Both alternatives contradict
(17). No division by \(\chi',M,b,\epsilon\), or either
remaining scalar factor was used. This excludes every
\(\kappa=0\) case.

## 6. The remaining kappa-nonzero case forces a complex quadratic coupling

Now assume \(\kappa\ne0\). Define
\[
\mathcal N_1=m_{ts}+\mu m_{ss},\qquad
\mathcal N_2=m_{tts}+2\mu m_{tss}+\mu^2m_{sss}.
\tag{26}
\]
The exact jet identities are
\[
\mathcal D\mathcal M_2=\mathcal M_3+2\mathcal N_1\kappa,
\qquad (\mathcal M_2)_s=\mathcal N_2+2\mathcal N_1\mu_s,
\qquad \mathcal D\mathcal N_1=\mathcal N_2+m_{ss}\kappa.
\tag{27}
\]
By (9), their successive implications are
\(\mathcal N_1=0\), then \(\mathcal N_2=0\), then
\(m_{ss}=0\). The definitions of \(\mathcal N_1\) and
\(\mathcal M_2\) give \(m_{ts}=m_{tt}=0\).
Thus both coefficient derivatives of \(m_t,m_s\) vanish,
and exact joint constants give
\[
m=At+Bs+C,\qquad A,B,C\in\mathbb C,
\qquad (A,B)\ne(0,0).
\tag{28}
\]
The last condition uses variable m. In particular
\(\beta=A+B\mu\ne0\). The last one-form in (9) integrates
without dividing by a derivative of mu:
\[
d\left(\lambda+\frac A2\mu+\frac B4\mu^2\right)=0.
\tag{29}
\]
Its value is a complex constant \(\lambda_0\).
Subtracting \(Ats+Bs^2/2+Cs\) from k leaves an element f
killed by \(\partial_s\). The equation
\(\mathcal K_2=-4\lambda\) is then
\[
f_{tt}+2A\mu+B\mu^2=-4\lambda,
\qquad f_{tt}=-4\lambda_0.
\tag{30}
\]
Subtract the explicit quadratic \(-2\lambda_0t^2\), then
use joint constants on its first derivative and constant
remainder. This gives \(f=-2\lambda_0t^2+Dt+E\) with
\(D,E\in\mathbb C\), and proves (2) in the normalized frame.

This high-compatibility family is not empty as a purely formal
coefficient system: \(k=ts\), \(m=t\), \(\mu=s\),
\(\lambda=-s/2\) gives \(\beta=1\), \(\kappa=s\ne0\)
and every identity (9). This is not an actual chart or a control
for the lower scalar, potentials, initial ideal, or strong return.
It only prevents interpreting the high-jet reduction itself
as an exclusion of (2).

## 7. Scope, frame distinction, and verification

The complete conclusion is a necessary form after the actual
normalization (5), together with exclusion of its zero-kappa
alternative. If the original omega is nonzero complex, then
\(\kappa_* =\kappa_{\rm old}-2\omega\); the proved nonzero
condition is the normalized one. Formula (2) pulls back using
\(s_*=s-\omega t^2\), not by silently declaring that the original
coupling is quadratic. The coefficient changes in Sections3--5
are separating field bases only, not ambient coordinate maps.

The lower genuine levels, full original return, and remaining
scalar constraints on the family (2) are not solved here. No
realization, recognition, exclusion of that family, or statement
about the noncomplex-omega branch is made.

The complete sources474,477 and the actual transport426 were
read before use. Fresh unsaved calculations reconstructed the
compatibility chain (27), forward identities of both coefficient
families, all three original-row identities (13), both highest
scalar coefficients, the zero \(R_t\) case, the full remaining
zeta coefficient (20), and the complete determinant (24).
The proof includes the finite exact-field and zero-division
arguments; it does not infer an identity from numerical samples.
No saved checker was executed, imported, compiled or rerun.
No earlier source or canonical file was edited. No unrestricted
cancellation or historical-novelty claim is made.
