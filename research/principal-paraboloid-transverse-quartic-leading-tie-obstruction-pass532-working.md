# A quartic leading-coefficient obstruction with transverse coupling

Working conditional lemma: under the complete actual assumptions
of528, if \(\deg_P\theta=4\), then the moving leading shear
\(R=y-q\theta\) has a nonzero cubic coefficient b and satisfies
\[
\boxed{
a\left(q_t-\frac{q(2q+m_t)}m\right)=-b^2,\qquad
a=[P^4]\theta,\quad b=[P^3]R\ne0.
}
\tag{1}
\]
Consequently \(\deg_Py=4\), and the original Z row also has
exact intrinsic degree four. Neither conclusion is assumed
while deriving (1).

This lemma does not exclude the remaining equal-degree quartic
sector by itself. It is the quartic replacement for528's
degree-at-least-five comparison, retaining every term that ties
in degree four.

## 1. Complete actual input and the retained quartic reduction

Retain EVERY actual hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
the genuine296 levels and unit gradient-minor conclusions, and
the universal multiplier of Sections1--3 of
[494](principal-paraboloid-unit-tangent-multiplier-pass494-working.md).
Apply the accepted necessary reduction
[528](principal-paraboloid-transverse-coupling-higher-degree-bound-pass528-working.md)
only within precisely those hypotheses. In particular,
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u_{\rm glob}],\quad
E=\partial_{u_{\rm glob}},\quad X=a_0u_{\rm glob}+x_0,\quad a_0\ne0,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\quad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the ENTIRE initial kernel},\\
N=[u_{\rm glob}^4]\partial_Z|_A\ne0,\quad
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,\\
Na_0=Nt=Ns=0,\quad \deg_v\sigma=1,\quad P=\sigma,\quad
NP=\rho\in L^*,\quad O=L[P],\\
m=k_s\ne0,\quad h=m_s\ne0,\quad p=m_t,\quad
\chi=h/m\ne0,\\
\operatorname{Frac}A=L(P)=\mathbb C(y,z_{\rm int},w),\quad
L[y,z_{\rm int},w]=L[P],\quad L[X,Y,Z,W]=L[X,P].
\end{gathered}
\tag{2}
\]
The intercept \(z_{\rm int}\) is the literal original
Z-intercept, not \(z_{\rm int}-2ty\). The original global
slice need not be \(X/a_0\). The exact coefficient partials
commute and fix P; no rationality of L is assumed. The complete
literal rows and calibrated scalar remain
\[
\begin{aligned}
Y&=y+PX+tX^2,\\
Z&=2ty+P^2+k_tP+m\theta+n+(2tP+k)X+t^2X^2,\\
W&=w+\theta X+sX^2,\\
mw&=\ell-(2P+k_t)y-\frac{k_{tt}}2P^2-pP\theta
                         -\frac h2\theta^2-n_tP-n_s\theta,\\
J_{t,s,P}(Y,Z,W)&=-a_0^4/\rho\in L^*.
\end{aligned}
\tag{3}
\]
The scalar need not be constant in t,s.

Write the unrestricted lower polynomials as
\[
\begin{aligned}
\theta&=aP^4+A_3P^3+A_2P^2+A_1P+A_0,\qquad a\in L^*,\\
q&=\begin{cases}
[P^4]y/a,&\deg_Py=4,\\
0,&\deg_Py<4,
\end{cases}\\
R=y-q\theta&=bP^3+B_2P^2+B_1P+B_0.
\end{aligned}
\tag{4}
\]
Here \(A_j,B_j\in L\), and the \(A_0\) in this display is
only a lower theta coefficient, not the original \(a_0\).
Result521, retained through528, gives \(\deg_Py\le4\).
Result528 further proves that a quartic theta necessarily has
\(\deg_PR=3\), so \(b\ne0\). Its alternative with a remainder
of degree at most two would force theta to be cubic instead.
This also shows that zero or constant R is not silently
discarded here.

The full leading gates already proved in528 give
\[
h_s=3h^2/m,\qquad a_s=-\chi a,\qquad q_s=\chi q,\qquad
h_t-3hp/m=4hq/m.
\tag{5}
\]
They include \(q=0\); no nonzero y or Z leader is presumed.

## 2. Full moving identities and their polynomial support

Use the genuine formal gradients \(f=H_U^{\rm ev}\) and
\(g=H_V^{\rm ev}\), differentiated before evaluation. Set
\[
\begin{aligned}
B&=pP+n_s,\quad \gamma=2P+k_t,\quad
F_{\rm base}=k_{tt}P^2/2+n_tP,\\
C_1&=k_{tt}P+n_t-\gamma B/m,\qquad C_2=p-\chi\gamma,\\
C_5&=m_{tt}P^2/2+n_{ts}P-\ell_s+
                         (h\ell-B^2-hF_{\rm base})/m,\\
K&=q^2+pq-\chi k_tq+n_{ss}/2-3\chi n_s/2
                                      =2\chi b/a,\\
A_R&=(2q+C_2)R+qC_1+C_5,\\
f&=(2q+C_2)\theta+2R+C_1,\qquad
G:=g+qf=2K\theta+A_R.
\end{aligned}
\tag{6}
\]
These are the complete polynomials from528, not a homogeneous
truncation. In particular,
\[
\deg_Pf=5,\quad F:=[P^5]f=-2\chi a,\qquad
\deg_PG=4,\quad G_0:=[P^4]G=2\chi b.
\tag{7}
\]
Both leaders are nonzero. No assumption on the un-sheared
g leader is needed.

Define
\[
\begin{aligned}
\nu&=(B+h\theta)/m,\qquad D_f=\gamma/m,\qquad
\beta_f=(2y+k_{tt}P+p\theta+n_t)/m,\\
K_\theta&=y_P+\theta_s+\nu,\\
L_R&=R_s+qR_P-q(B+q\gamma)/m,\\
J_R&=(2R+k_{tt}P+n_t+\gamma R_P)/m,\\
\eta_q&=q_t-q(2q+p)/m,\\
\mathcal A&=y_t+\theta_Py_s+y_P^2,\qquad
\mathcal B_1=\theta_t+\theta_PK_\theta+\beta_f+D_fy_P.
\end{aligned}
\tag{8}
\]
The symbol \(J_R\) is auxiliary, not the original determinant.
The full494 equations and the exact moving shear from528 read
\[
\begin{aligned}
\mathcal A&=\kappa g,\qquad
\mathcal B_1=-\kappa f,\qquad \kappa\in L^*,\\
\mathcal C:=\mathcal A-q\mathcal B_1
 &=R_t+R_P^2+\eta_q\theta+\theta_PL_R-qJ_R
   =\kappa G,\\
\mathcal W&=-L_Rf^2+
 (2R_P-K_\theta-2qD_f)fG+(\theta_P+D_f)G^2\in L^*.
\end{aligned}
\tag{9}
\]
The coefficient \(\kappa\) has no P dependence, but may vary in
t,s. The term \(\eta_q\theta\), and in particular \(q_t\), has
not been removed. The only canceled moving-shear term is
\((q_s-qh/m)\theta\theta_P\), licensed by (5).

The support bound from the full \(\mathcal B_1\) equation is
\(\deg_PK_\theta\le2\): otherwise \(\theta_PK_\theta\)
would uniquely exceed degree five. Every other summand of
\(\mathcal B_1\) has degree at most four. Put
\[
k_2=[P^2]K_\theta
 =3qA_3+3b+(A_2)_s+\chi A_2.
\tag{10}
\]
The degree-four cancellation uses \(a_s=-\chi a\), and the
degree-three cancellation says
\((A_3)_s+\chi A_3+4qa=0\). No lower theta coefficient has
been fixed. Comparing degree five in the full first line of (9)
now gives
\[
4ak_2=-\kappa F=2\kappa\chi a,\qquad
k_2=\kappa\chi/2.
\tag{11}
\]
In particular \(k_2\ne0\) is a consequence, not an input.

## 3. The complete degree-six, degree-five and degree-four ties

Initially \(\deg_PL_R\le3\), with cubic coefficient \(b_s\).
All terms of \(\mathcal C\) in (9) other than
\(\theta_PL_R\) have degree at most four:
\(\deg R_t,\deg J_R\le3\), \(\deg R_P^2=4\), and
\(\deg(\eta_q\theta)\le4\). The right side has degree four.
Consequently the complete degree-six coefficient gives
\[
[P^6]\mathcal C=4ab_s=0,\qquad b_s=0.
\tag{12}
\]
After this substitution, degree five gives
\[
[P^5]\mathcal C=4a\big((B_2)_s+3qb\big)=0,\qquad
(B_2)_s=-3qb.
\tag{13}
\]
Thus \(\deg_PL_R\le1\). Its linear coefficient is
\[
\ell_1=[P]L_R=(B_1)_s+2qB_2-q(p+2q)/m.
\tag{14}
\]
The full degree-four equation is therefore
\[
4a\ell_1+9b^2+a\eta_q=\kappa G_0=2\kappa\chi b.
\tag{15}
\]
The three terms on the left arise from
\(\theta_PL_R\), \(R_P^2\), and \(\eta_q\theta\),
respectively. Neither \(R_t\) nor \(qJ_R\) can reach degree
four. The arbitrary lower coefficients do not enter (15);
they were not set to zero.

Now all summands of \(\mathcal W\) in (9) have degree at most
eleven. The coefficient of \(P^2\) in
\(2R_P-K_\theta-2qD_f\) is \(6b-k_2\), since \(D_f\)
is affine. Its complete degree-eleven coefficient is
\[
\begin{aligned}
0=[P^{11}]\mathcal W
 &=-\ell_1F^2+(6b-k_2)FG_0+4aG_0^2\\
 &=-4\chi^2a\big(a\ell_1+2b^2-bk_2\big).
\end{aligned}
\tag{16}
\]
This equation remains valid if \(6b-k_2=0\), or if
\(\ell_1=0\). No such coefficient is divided by.
As \(\chi a\ne0\), equations (11),(16) give
\[
a\ell_1=bk_2-2b^2=\kappa\chi b/2-2b^2.
\tag{17}
\]
Substitute (17) in (15). The \(\kappa\)-terms cancel, leaving
\(a\eta_q=-b^2\), which is exactly (1). This calculation
retains both quartic ties that prevent using528's
degree-at-least-five contradiction unchanged.

## 4. The two excluded boundaries and the remaining scope

If \(\deg_Py<4\), definition (4) gives \(q=0\) identically
in L, hence \(q_t=0\) and \(\eta_q=0\). Equation (1) would
give \(b=0\), contradicting (4). Thus
\[
\deg_Py=4,\qquad q\ne0.
\tag{18}
\]
This accounts for every unequal-degree y, including zero y,
without dividing by its leading coefficient.

By the literal Z row (3), its degree-four coefficient is
\((2tq+m)a\). Suppose it vanishes. Then
\[
q=-\frac m{2t},\qquad
q_t=-\frac p{2t}+\frac m{2t^2}
       =\frac{q(2q+p)}m.
\tag{19}
\]
The division by t is in the existing coefficient field: t is
one of its transcendental separating parameters. This gives
\(\eta_q=0\), again contradicting (1). Therefore the original,
unmodified Z row has exact intrinsic degree four. No Z leader
was assumed nonzero earlier in the proof.

For clarity, (1) alone is not a contradiction in the surviving
equal-degree branch. Put \(F_0=\ker_L\partial_s\), which is
finite over \(\mathbb C(t)\), and set
\(\mathfrak a=ma\), \(v=q/m\), \(\lambda=h/m^3\).
Equations (5),(12) and528 give
\[
\mathfrak a,b,\lambda\in F_0^*,\quad v\in F_0,\qquad
\lambda_t=4v\lambda,\qquad
v_t=2v^2-b^2/\mathfrak a.
\tag{20}
\]
These leader equations are compatible in finite coefficient
fields. For a compact control, take \(L=\mathbb C(t,z)\),
\(s=-z^2/2\), and
\[
m=\frac1{tz},\quad k=-\frac zt,\quad
a=t^3z,\quad q=\frac1{2t^2z},\quad b=1,\quad
\lambda=t^2,\quad \mathfrak a=t^2,\quad v=\frac1{2t}.
\tag{21}
\]
With \(\partial_s=-z^{-1}\partial_z\) and the fixed-s
t derivative, this satisfies (5), \(b_s=0\), (1), and (20).
The Z leading coefficient is \(2t^2\ne0\).
This is ONLY a control for the listed necessary leader
equations. It supplies no full theta or y, genuine H/Q level,
calibrated determinant, actual ring return or chart realization.
It is not a counterexample to any chart exclusion.

## 5. Verification and retained dependencies

The complete528 source was reread through EOF95d8f8+d1e56a,
with SHA31157bc68bd98ed7f39d3408136ea61a1c77f8ab988db9efbbb4c839dd3f73ef
confirmed in acaa07. Its complete actual pedigree and earlier
degree theorem remain retained; this note does not recertify
arbitrary chart entry.

Fresh unsaved cf9742 independently expanded the COMPLETE
\(\mathcal A,\mathcal B_1,\mathcal W\) with unrestricted lower
coefficients of quartic theta and cubic R. It verified
\(\mathcal B_1\)'s degree-five coefficient, the sequential
degree-six/five/four coefficients of \(\mathcal C\), the entire
degree-eleven expression (16), and its cancellation to (1),
with every residual zero. Fresh b33d55 checked the listed
finite-field control and its nonzero Z leader. These algebraic
checks supplement the exact support argument above.

No all-X resultant or pending quartic exclusion is a dependency
of this lemma. No coefficient-field operation is claimed to be
an ambient coordinate change. No saved checker was executed,
imported, compiled or rerun, and no earlier source or canonical
record was edited. The conclusion is the bounded obstruction
(1),(18),(19), not unrestricted cancellation, a realization,
novelty or external certification.
