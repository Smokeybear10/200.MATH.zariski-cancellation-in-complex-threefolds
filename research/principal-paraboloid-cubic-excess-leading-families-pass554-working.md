# Necessary leading families in the cubic excess profile

Working bounded reduction: in the FULL actual264/296/535 chart,
retain noncomplex coupling m and the excess profile
\[
\deg\sigma=2,\qquad \deg\theta=3,\qquad \deg y=4.
\tag{1}
\]
The necessary leading system553 has three explicit coefficient
families, separated by h=m_s and then by one exact first integral.
The h=0 family is retained, not excluded. In that family additional
coefficients of the full H level and full multiplier force
\[
m^5=c_1t+c_0,\qquad c_1\in\mathbb C^*,\quad c_0\in\mathbb C.
\tag{2}
\]
All statements below are necessary conditions. They do not assert
that any family satisfies the lower genuine levels, full scalar,
actual returns, or original polynomial-ring hypotheses.

## 1. Retained chart, exact coefficient field and notation

Retain EVERY actual hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md),
[535](principal-paraboloid-nonlinear-sigma-unit-multiplier-pass535-working.md)
and the scoped degree reduction
[553](principal-paraboloid-quadratic-sigma-higher-theta-degree-bound-pass553-working.md).
In particular the original four-ring is
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=\mathcal A[u],\quad
E=\partial_u,\quad X=a_0u+x_0,\quad a_0\ne0,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\quad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the ENTIRE initial kernel},\\
0\ne N=[u^4]\partial_Z|_{\mathcal A},\quad
Na_0=Nt=Ns=0,\quad Nv=1,\\
L=\operatorname{Frac}\ker_{\mathcal A}N,\quad
[L:\mathbb C(t,s)]<\infty,\quad
L[\mathcal A]=L[v]=L[y,\sigma,\theta],\\
\operatorname{Frac}\mathcal A=L(v)=\mathbb C(y,z_{\rm int},w),
\qquad m=k_s\notin\mathbb C.
\end{gathered}
\tag{3}
\]
The intercept z_int is the literal original Z-intercept. Both
actual returns, the full calibrated scalar, the genuine moving
levels and the selected literal partial remain required.

Use553's intrinsic normalization only: in a finite extension L'
of L there is an affine intrinsic parameter x with
\[
\begin{gathered}
\sigma=x^2+c,\quad Nx=\rho\in(L')^*,\quad
J_{t,s,x}(Y,Z,W)=-a_0^4/\rho,\\
\theta=ax^3+\text{lower terms},\qquad
y=rx^4+q_3x^3+\text{lower terms},\qquad a,r\ne0,\\
p=m_t,\quad h=m_s,\qquad
F_0=\ker_{L'}\partial_s.
\end{gathered}
\tag{4}
\]
All coefficient partials are the exact commuting extensions from
C(t,s), extended to fix x. Thus moving-center and moving-scale
derivatives have already been retained. The multiplier in this
parameter is the unit kappa=kappa_v/rho squared from535.
The intrinsic x is not an actual polynomial coordinate.

The field F0 is finite over C(t), but need not equal C(t).
For example, the monic minimal polynomial over C(t,s) of an element
killed by partial_s has coefficients killed by partial_s: differentiating
would otherwise give a relation of lower degree. Its coefficients
therefore belong to C(t). The finite degree of L' then bounds the
constant-field extension. The common constants of the two exact
partials in L' are C by the same argument and algebraic closedness
of C. These facts justify all constant descents below.

## 2. The complete leading equations, without a transverse assumption

The cubic excess case of553 gives
\[
\begin{aligned}
a^3\left(\frac{h_s}{6}-\frac{h^2}{2m}\right)
                                      -\frac{2har}{m}&=0,\\
6a\left(a_s+\frac{ha}{m}\right)+\frac{24r}{m}&=0,\\
r_s&=0.
\end{aligned}
\tag{5}
\]
These are respectively the full H coefficient of degree nine,
the full cleared B multiplier coefficient of degree six, and
the full cleared A multiplier coefficient of degree seven.
They hold with all lower coefficients present, and with no
division by sigma_x=2x. The full equations used are
\[
\mathcal A_\beta=\kappa H_V^{\rm ev},\qquad
\mathcal B_\beta=-\kappa H_U^{\rm ev},\qquad
\kappa\in(L')^*.
\tag{6}
\]
Their explicit complete polynomials, formal H support and finite
intrinsic covariance are printed in553. In particular the first
equation of (5) does not force h nonzero. A vanishing h is an
identity in the coefficient field, and then h_s=h_t=0 as well.

## 3. The h nonzero families

Assume h is nonzero. Equations (5) become
\[
h_s=\frac{3h^2}{m}+\frac{12hr}{ma^2},\qquad
a_s=-\frac{ha}{m}-\frac{4r}{ma},\qquad r_s=0.
\tag{7}
\]
Define existing coefficient elements
\[
b=ha^3\ne0,\qquad
v_1=\frac{b/a+4r}{m}=\frac{ha^2+4r}{m}.
\tag{8}
\]
The symbol v1 is a coefficient, not the original intrinsic parameter v.
Differentiating (8) with (7), including m_s=h, gives
\[
b_s=0,\qquad (v_1)_s=0,\qquad aa_s=-v_1.
\tag{9}
\]
For the second equality one may write
\((v_1)_s=-b a_s/(ma^2)-v_1h/m\) after b_s=r_s=0;
then aa_s=-v1 and b=ha cubed cancel the two terms.
Consequently
\[
\gamma:=a^2+2v_1s\in F_0,\qquad r,b,v_1\in F_0.
\tag{10}
\]

### 3.1. Nonzero v1

If v1 is nonzero, the necessary family is
\[
\boxed{\begin{gathered}
r,b,v_1\in F_0^*,\quad \gamma\in F_0,\quad
a^2=\gamma-2v_1s,\\
m=\frac{4r+b/a}{v_1}\ne0,\qquad h=\frac b{a^3}\ne0.
\end{gathered}}
\tag{11}
\]
The element a already belongs to L'. Equation (11) does not adjoin
a new square root or normalize one as an actual coordinate.
The displayed nonzero m is the original coupling restriction.
These identities keep arbitrary t dependence of r,b,v1,gamma
inside the exact finite field F0.

### 3.2. Zero v1

If v1=0, (9) forces a_s=0 since a is nonzero. Equation (8) gives
b=-4ra and hence h=-4r/a squared, all in F0. The necessary family is
\[
\boxed{\begin{gathered}
a,r\in F_0^*,\quad h=-4r/a^2\in F_0^*,\quad b=-4ra,\\
m=hs+m_0,\qquad m_0\in F_0.
\end{gathered}}
\tag{12}
\]
The last integration is exact subtraction: partial_s(m-hs)=0.
No value of p=m_t is assumed in either (11) or (12).
No claim that their coefficient functions are complex or rational
is made. The lower coefficients, including q3, remain subject to
the unused genuine equations.

## 4. The h=0 family requires the next genuine coefficients

Now assume h=0. Then m,p belong to F0, p_s=0, and every derivative
of h vanishes. Use mathfrak n for the potential n, so that
\[
\mathcal F(P,V)=\frac{k_{tt}}2P^2+pPV+
                        \mathfrak n_tP+\mathfrak n_sV.
\tag{13}
\]
The entire formal level is still
\[
\begin{aligned}
H-h_0={}&U^2+\mathcal F_PU+
\mathcal F_V\frac{\ell-(2P+k_t)U-\mathcal F}{m}
       +\frac{k_{ttt}}6P^3+\frac{p_t}{2}P^2V\\
&+\frac{\mathfrak n_{tt}}2P^2+\mathfrak n_{ts}PV
       +\frac{\mathfrak n_{ss}}2V^2-\ell_tP-\ell_sV-h_0.
\end{aligned}
\tag{14}
\]
It is differentiated formally before evaluating U=y, P=x squared+c,
V=theta. In particular the complete evaluated gradient is
\[
g=py+\mathfrak n_{ss}\theta+C_5(x^2+c),\qquad
C_5(P)=\frac{p_t}{2}P^2+\mathfrak n_{ts}P-\ell_s
                                  -\frac{(pP+\mathfrak n_s)^2}{m}.
\tag{15}
\]
Thus deg_x(g)<=4, with no assumption on its leading coefficient.

The degree-eight coefficient of (14) is
\[
r^2-2pr/m=0,\qquad r=2p/m.
\tag{16}
\]
As r is nonzero by (1), this proves p nonzero, without assuming it
beforehand. The full degree-seven coefficient, after (16), is
\[
rq_3+a\left(\frac{p^2}{m}+\frac{p_t}{2}\right)=0.
\tag{17}
\]
For clarity, before (16) that coefficient is
\((2r-2p/m)q_3+a(pr+p_t/2-p^2/m)\). It retains all
contributions of y squared, the formal U coefficient and C5*theta.
Neither an h nonzero formula nor a normalized coupling is used.

Put
\[
\lambda=-p/2-mp_t/(4p)\in F_0.
\tag{18}
\]
Equation (17) is q3=lambda*a. The second equation of (5) gives
aa_s=-8p/m squared. With r_s=0, the COMPLETE degree-six
coefficient of A_beta is
\[
[x^6]\mathcal A_\beta=4r_t+6a(q_3)_s+16r^2.
\tag{19}
\]
Here the first term comes from 4x squared*y_t, the second from
2x*theta_x*y_s, and the third from y_x squared. The remaining
terms have degree at most five. Since lambda is in F0,
(q3)_s=lambda*a_s. Substituting this, (16) and aa_s=-8p/m squared
into (19) gives
\[
\boxed{[x^6]\mathcal A_\beta
             =20\frac{mp_t+4p^2}{m^2}=0.}
\tag{20}
\]
Its vanishing follows from (6),(15), not from a freely imposed
leading relation. All t derivatives here are genuine: in particular
r_t=2(mp_t-p squared)/m squared.

## 5. Exact integration of the h=0 branch

Equation (20) gives partial_t(m to the fourth*p)=0. This expression
is already killed by partial_s, so it is a complex constant.
Since m,p are nonzero, define
\[
c_1=5m^4p\in\mathbb C^*,\qquad
c_0=m^5-c_1t\in\mathbb C.
\tag{21}
\]
This proves (2) in the existing field. No new fifth root, rational
field assumption, or actual change of time is used.

After p_t=-4p squared/m, equation (18) simplifies to lambda=p/2.
Integrating the exact s derivative of a squared by subtraction
gives the complete necessary leading family obtained here:
\[
\boxed{\begin{gathered}
h=0,\quad m\in F_0^*,\quad m^5=c_1t+c_0,\quad
p=\frac{c_1}{5m^4}\ne0,\\
r=2p/m,\qquad q_3=pa/2,\qquad
a^2=\gamma-\frac{16p}{m^2}s,\quad \gamma\in F_0.
\end{gathered}}
\tag{22}
\]
The nonzero a is the existing leading coefficient of theta in L'.
The coefficient gamma may be noncomplex. No remaining coefficient
of theta, y, the potentials or the moving levels has been assigned
independently or deleted.

## 6. Verification and limits

The complete553 source was read before this continuation. Its full
actual inputs and finite intrinsic covariance are retained. Fresh
unsaved calculation53b421 rebuilt (14) with arbitrary lower
coefficients of theta and y and all their coefficient jets. It
differentiated H_V before evaluation and verified (15)--(20),
including the degree bound for g, the entire H coefficients and
the full cleared A and B coefficients. Six residuals were zero.
The same fresh calculation separately checked b_s, (v1)_s and
partial_s(a squared+2v1*s) from the entire system (5); all three
residuals were zero.

The cases h=0, h nonzero with v1=0, and h nonzero with v1 nonzero
are all retained. Divisions by p occur only after (16) proves it
nonzero. Divisions by v1 occur only in (11), and divisions by h
only after the transverse case is selected. Neither sigma_x nor
the intrinsic parameter is inverted. All exact-field dependencies
such as m_s=h, p=m_t and p_s=h_t remain in force.

The three families describe only necessary leading data at the
stated degree profile. Checking the three top equations alone is
not an actual264 realization and does not bypass the next genuine
coefficients used in the h=0 branch. The unused lower H and Q
levels, all lower multiplier coefficients, full calibrated scalar
and both actual returns may impose further restrictions.

No saved checker was executed, imported, compiled or rerun. No
other source or canonical file was edited. A separate complete
saved-source audit remains required after the author hold. There
is no exclusion, recognition, arbitrary-entry, novelty or general
cancellation claim here.
