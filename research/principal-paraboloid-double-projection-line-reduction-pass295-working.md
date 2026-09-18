# The double-projection branch has a linear projected image

Working result: in the actual nonzero-coupling chart264, suppose
the finite projection to the last two intrinsic generators has
degree two. Its projected plane image is then a line. In the
exact parameter supplied by290, both projected generators have
degree at most two and the first generator has degree at most four.

This uses the remaining Jacobian coefficient through the fourth
potential and unit-minor theorem296. A monic cubic surface relation
alone does not give the result. No actual coordinate recognition,
exclusion of every double cover, or resolution of the birational
projection branch is claimed.

## 1. Actual entry and the double-cover normal form

Retain the complete actual assumptions and returns of the fully read
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
[290](principal-paraboloid-nonzero-coupling-projection-pass290-working.md),
and [296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md):
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad
\deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(X^2Z-Y^2)\text{ is the entire initial kernel},
\qquad a=EX\ne0,\\
L=\operatorname{Frac}\ker_A N,\qquad [L:\mathbb C(t,s)]<\infty,
\qquad O=L[v],\quad Nv=1,\quad K=\operatorname{Frac}A=L(v),\\
K=\mathbb C(y,z,w),\qquad L[y,z,w]=L[y,\sigma,\theta]=O,\qquad
m=k_s\ne0 .
\end{gathered}
\tag{1}
\]
The selected literal \(Z\)-partial has exact intrinsic shift four.
The coefficient partials in \(t,s\) extend uniquely to \(L\),
commute, and fix \(v\). Their common constant field is \(\mathbb C\):
an element killed by both has zero differential over \(\mathbb C\)
in the finite separable extension of \(\mathbb C(t,s)\), hence is
algebraic over the algebraically closed field \(\mathbb C\).

The complete actual expressions and scalar calibration are
\[
\begin{aligned}
Y&=y+\sigma X+tX^2,\\
Z&=z+(2t\sigma+k)X+t^2X^2,\\
W&=w+\theta X+sX^2,\qquad
\det\frac{\partial(Y,Z,W)}{\partial(t,s,v)}=-a^4\in L^* .
\end{aligned}
\tag{2}
\]
Set \(C=L[\sigma,\theta]\). The extra hypothesis of this note is
\[
[L(v):\operatorname{Frac}C]=2.
\tag{3}
\]
The exact odd-module argument of290, not a geometric splitting
assumption, gives
\[
\begin{gathered}
x=v-\beta/2,\quad Nx=1,\quad r=x^2,\quad
C=L[r],\\
y=A(r)+cx,\qquad c\in L^*,\quad A\in L[r],\\
\sigma=p(r),\qquad\theta=q(r),\qquad L[p,q]=L[r].
\end{gathered}
\tag{4}
\]
The parameter change in (4) is only within \(O\). It is not an
ambient coordinate change. In particular \(1,y\) are independent
over \(\operatorname{Frac}C\).

Let \(G(P,V)\) generate the kernel of
\(L[P,V]\longrightarrow L[r]\), \((P,V)\mapsto(p,q)\), and put
\(g_0=\deg G\). The exact-field plane-degree argument in
[271, Section5](principal-paraboloid-nonconstant-intercept-plane-reduction-pass271-working.md)
gives
\[
g_0=\max(\deg_r p,\deg_r q),\qquad
G_{g_0}=c_0\Lambda^{g_0},
\quad c_0\in L^*,\quad 0\ne\Lambda\in L[P,V]_1.
\tag{5}
\]
Briefly, after cancelling leading terms one entry has degree
\(i<d\). The characteristic polynomial over the degree-\(d\)
entry is minimal by the field return. Its coefficient of
first-variable degree \(d-j\) has other-variable degree at most
\(\lfloor ij/d\rfloor<j\), by the pole orders at infinity.
Thus its total degree is \(d\) and its top is a pure power.
This calculation descends to the exact field \(L\).

## 2. The two actual potentials and a strengthened plane cofactor

Use independent formal variables \(U,P,V\). Write
\[
\begin{aligned}
F&=\frac{k_{tt}}2P^2+m_tPV+\frac{m_s}2V^2+n_tP+n_sV,\\
\gamma&=2P+k_t,\qquad D=\gamma/m,\qquad \lambda=F_V/m,\\
g&=(\ell-\gamma U-F)/m .
\end{aligned}
\tag{6}
\]
The letter \(g\) in (6) is a polynomial, distinct from the plane
degree \(g_0\). We have \(w=g(y,\sigma,\theta)\).
Let \(H\) be264's surface polynomial and \(Q\) the corrected
fourth potential of296. Their full conclusions are
\[
\begin{gathered}
H(y,\sigma,\theta)=h_0,\qquad Q(y,\sigma,\theta)=q_0,\qquad
h_0,q_0\in L,\\
H-h_0=U^2+A_1(P,V)U+A_0(P,V),\qquad
\deg A_1\le2,\quad\deg A_0\le3,\quad\deg Q\le4,\\
\bigl(H_UQ_P-H_PQ_U,\ H_UQ_V-H_VQ_U,\
H_PQ_V-H_VQ_P\bigr)^{\rm ev}O=O .
\end{gathered}
\tag{7}
\]
Here and below “ev” means evaluation at \((y,\sigma,\theta)\).
In particular the last line comes from the actual nonzero
constant determinant, not from smoothness of the projected plane.
The formal coefficient partials in the following formulas hold
\(U,P,V\) fixed:
\[
\begin{aligned}
Q_U&=H_P-DH_V+\lambda H_U,\\
Q_P&=H_t-h_{0,t}-\frac{2U+F_P}{m}H_V+\lambda H_P,\\
Q_V&=H_s-h_{0,s}.
\end{aligned}
\tag{8}
\]

For later coefficient checks the exact expressions are
\[
\begin{aligned}
A_1&=F_P-DF_V,\\
A_0&=\frac{F_V(\ell-F)}m+H_3(k;P,V)+H_2(n;P,V)
                    -\ell_tP-\ell_sV-h_0,\\
e&=\frac{k_{tt}-2Dm_t+D^2m_s}{2},\\
R&=A_{0,P}-DA_{0,V}+(\lambda-e)A_1 .
\end{aligned}
\tag{9}
\]
The \(H_j\) are the homogeneous Taylor polynomials with factorial
denominators as in264. By296, division in the formal variable \(U\)
is exactly
\[
Q-q_0-e(H-h_0)=R(P,V)U+S(P,V),\qquad
\deg R\le4,\quad\deg S\le5 .
\tag{10}
\]
At the actual curve, independence of \(1,y\) over
\(\operatorname{Frac}C\) gives \(R(p,q)=S(p,q)=0\).
Write \(R=G r_1,\ S=G s_1\).
Differentiating (10) and evaluating gives
\[
\nabla Q^{\rm ev}
=e^{\rm ev}\nabla H^{\rm ev}
+z_1(0,G_P^{\rm ev},G_V^{\rm ev}),\qquad
z_1=r_1(p,q)y+s_1(p,q).
\tag{11}
\]
Every minor in (7) is divisible by \(z_1\) in \(O=L[x]\).
Hence \(z_1\in O^*=L^*\). Taking odd parts in (4) yields
\(c\,r_1(p,q)x=0\), so \(r_1\in(G)\). The even part gives
\(s_1(p,q)=\eta\in L^*\), so \(s_1-\eta\in(G)\). Therefore
\[
\boxed{R=G^2R_2,\qquad S=\eta G+G^2S_2,\qquad\eta\in L^*.}
\tag{12}
\]
Neither the independence in (3) nor the unit-minor input can be
replaced merely by a formal surface equation.

## 3. A nonlinear projected image forces zero remainder

Assume for contradiction that \(g_0\ge2\).
The degree-four part of (9) is
\[
R_4=\frac{4P^3m_s(m_tP+m_sV)}{m^3}.
\tag{13}
\]
Indeed \(A_{1,2}=-2P(m_tP+m_sV)/m\) and
\(e_2=2P^2m_s/m^2\); only \(-e_2A_{1,2}\) contributes degree four.

If \(m_s\ne0\), the two lines in (13) are distinct and have
multiplicities three and one. By (5),(12),
\(\Lambda^{2g_0}\) divides (13), impossible for \(g_0\ge2\).
Thus \(m_s=0\). Its \(t,s\) derivatives vanish too, and now
\(\deg R\le3\). Equation (12) with \(2g_0\ge4\) implies
\[
\boxed{m_s=0,\qquad R=0.}
\tag{14}
\]

## 4. Lower remainder coefficients force constant coupling

All coefficients below are obtained directly from (9), under
\(m_s=0\). No parameter of the projected curve is differentiated.
They retain all coefficient-field derivatives:
\[
\begin{aligned}
[P^3]R&=-\frac{m m_{tt}+4m_t^2}{m^2},\\
[PV]R&=\frac{m m_{tt}+m_t^2-2n_{ss}}m,\\
[P^2]R&=\frac{
-k_t m^2m_{tt}-8k_t m m_t^2+5k_{tt}m^2m_t+k_{ttt}m^3
-4m^2n_{ts}-8m m_t n_s}{2m^3}.
\end{aligned}
\tag{15}
\]
Since \(R=0\), the first two equations give
\[
m m_{tt}+4m_t^2=0,\qquad
n_{ss}=(m m_{tt}+m_t^2)/2 .
\tag{16}
\]
Differentiate the last equation of (15) in \(s\).
Use \(k_{ts}=m_t,\ k_{tts}=m_{tt},\
k_{ttts}=m_{ttt}\) and the \(t\)-derivative of the second
equation of (16). The result is
\[
0=-\frac{m^2m_{ttt}+6m m_t m_{tt}+12m_t^3}{2m^2}.
\tag{17}
\]
The first equation of (16) gives
\(m_{tt}=-4m_t^2/m\) and \(m_{ttt}=36m_t^3/m^2\).
Thus (17) is \(-12m_t^3/m^2=0\), so \(m_t=0\).
Together with \(m_s=0\) and the joint-constant gate in Section1,
\[
m\in\mathbb C^*,\qquad n_{ss}=0 .
\tag{18}
\]
With these vanishing derivatives the next two coefficients
of (9) are simply
\[
[V]R=n_{ts},\qquad [P^2]R=k_{ttt}/2-2n_{ts}/m.
\tag{19}
\]
They give \(n_{ts}=k_{ttt}=0\). Exact integration, without any
assumption that \(L\) is a rational field, yields
\[
\boxed{
k=m s+\frac{\kappa}{2}t^2+b t+d,\qquad
n=\nu s+f_0,\qquad
m,\kappa,b,d,\nu\in\mathbb C,\quad m\ne0,\quad (f_0)_s=0.}
\tag{20}
\]
For example \(k_{tt}\) is killed by both partials and is the
complex constant \(\kappa\); subtracting its quadratic
antiderivative successively gives \(b,d\). The same argument
makes \(n_s=\nu\) complex.

## 5. An actual reframe, with the exact chart gates preserved

Only now use the complex constants in (20). Make the actual
polynomial change
\[
W_*=mW+\frac{\kappa}{2}Z+bY+dX^2,\qquad
W=\frac{W_*-\kappa Z/2-bY-dX^2}{m}.
\tag{21}
\]
It fixes \(X,Y,Z\). Its new quadratic coefficient and intercept
data are
\[
\begin{aligned}
s_*&=m s+\kappa t^2/2+bt+d=k,\qquad k_*=s_*,\\
\theta_*&=m\theta+(\kappa t+b)\sigma+\kappa k/2,\\
w_*&=mw+\kappa z/2+by,\qquad n_*=n-\kappa k/2.
\end{aligned}
\tag{22}
\]
Substitution verifies both the full \(W_*\) expansion and
\(z=2ty+\sigma^2+\theta_*+n_*\).
In coefficient variables \((t,s_*)\),
\[
m_*=1,\qquad n_*=\nu_*s_*+f(t),\qquad
\nu_*=\nu/m-\kappa/2\in\mathbb C,\quad f_{s_*}=0.
\tag{23}
\]
The transformed second-potential constant is, explicitly,
\(\ell_*=\ell+\kappa n/2+\kappa\nu_* k/2\).
This follows by substituting (22) into
\(w_*+2\sigma y+(n_*)_t\sigma+\nu_*\theta_*\).

Here are the actual-field and selected-chart checks. The map
(21) is invertible over \(\mathbb C\), not over \(L\) alone.
Its weighted leading map is invertible and fixes the relation
\(X^2Z-Y^2\); hence the entire initial kernel is unchanged.
The new \(s_*=m s+\text{a polynomial in }t\) is independent
of \(t\), so \([L:\mathbb C(t,s_*)]<\infty\) and all four
time degrees remain exact. The intercept change in (22) is
invertible, giving both \(\mathbb C(y,z,w_*)=K\) and
\(L[y,z,w_*]=O\).

The new literal \(Z\)-partial is
\(\partial_Z-(\kappa/(2m))\partial_W\).
The old \(W\)-partial has shift at most three: its omitted
leading triple \(X,Y,Z\) is dependent, while the maximal
shift is four by the exact minor criterion of264's retained158
input. Therefore its addition cannot change the shift-four
intrinsic leading field \(N\). Thus \(L,O,Nv=1\) are retained.
Alternatively, the full determinant check is direct:
the actual row change multiplies it by \(m\), while replacing
\((t,s,v)\) by \((t,s_*,v)\) divides it by \(m\). Its value
remains exactly \(-a^4\).

Finally, \((\sigma,\theta_*)\) is an invertible affine
\(L\)-linear change of \((\sigma,\theta)\), so its generated
ring is still \(C=L[r]\), and the total degree \(g_0\ge2\)
of its plane equation is unchanged. This affine plane change
is justified separately from the actual coordinate change (21).

## 6. The normalized fourth potential is affine, a contradiction

Drop the stars, working in the actual frame just established.
We have \(k=s,\ m=1,\ n=\nu s+f(t)\).
The argument of Sections2 and3 applies afresh to this chart,
since the projected image is still assumed nonlinear.
In particular its new remainder is zero. Formula (9) reduces to
\[
R=(f''+2\ell_s)P-\ell_t=0.
\tag{24}
\]
Commutation of the partials gives \(f'''=0\). The exact
joint-constant integration is therefore
\[
f=\alpha t^2/2+\beta t+\delta,\qquad
\ell=-\alpha s/2+\ell_0,\qquad
\alpha,\beta,\delta,\ell_0\in\mathbb C.
\tag{25}
\]
In this frame the entire cubic surface polynomial, which now
has total degree at most two, is
\[
H=U^2+(f'-2\nu P)U-\nu f'P+\frac{\alpha}{2}P^2
       +\left(\frac{\alpha}{2}-\nu^2\right)V+\nu\ell.
\tag{26}
\]
Insert (26) in the full corrected gradients (8), not in a
formula differentiated after restriction to a plane curve.
The cancellations are exact:
\[
\boxed{
Q_U=0,\qquad
Q_P=-h_{0,t}-\alpha f'/2,\qquad
Q_V=-h_{0,s}-\nu\alpha/2.}
\tag{27}
\]
For instance the coefficient of \(U\) in \(Q_P\) is
\(\alpha-2(\alpha/2-\nu^2)-2\nu^2=0\), and its
coefficient of \(P\) cancels as well.
Thus \(Q-q_0\) is an affine polynomial in \(P,V\).
Its two linear coefficients cannot both vanish, because that
would make every two-gradient minor in (7) zero.
It is consequently a nonzero affine equation of the projected
plane curve. Its irreducible equation \(G\) must have degree one,
contrary to \(g_0\ge2\).

## 7. Exact conclusion and remaining boundary

The contradiction proves, in the original chart,
\[
\boxed{
[L(v):\operatorname{Frac}L[\sigma,\theta]]=2
\quad\Longrightarrow\quad
\deg G=1.}
\tag{28}
\]
Equations (4),(5) now make \(p(r),q(r)\) affine polynomials in
\(r\), with at least one nonconstant. Taking the trace of the
monic quadratic relation gives
\(2A(r)=-A_1(p(r),q(r))\), so \(\deg_r A\le2\). Hence
\[
\boxed{
\max(\deg_x\sigma,\deg_x\theta)=2,\qquad
y=A(x^2)+cx,\quad \deg_x y\le4,\quad c\in L^*.}
\tag{29}
\]
There is a useful refinement if the original \(m_s\ne0\).
Equations (12),(13) force the line's top to be \(P\);
thus \(\sigma\in L\), and then \(A_1(\sigma,V)\) is affine
in \(V\), giving \(\deg_x y\le2\).

The theorem does not identify the coefficient-field line with
an actual ambient coordinate. It leaves both the surviving
double-cover line case and the degree-one projection case open.
It does not assume that arbitrary coefficients can be normalized
to \(k=s,n=0,\ell=t\); the actual reframe (21) is used only after
its complex coefficients have been forced under the contradictory
nonlinear hypothesis.

Fresh unsaved algebra independently checked the complete
remainder's top terms and the differentiated lower-coefficient
identity (17). The proof is the exact coefficient and
unit-minor argument above, not a finite sampling claim.
All directly used296 source text was read through EOF before
writing this consequence. No saved checker was executed,
imported, compiled or rerun, and no retained file was changed.
No claim of arbitrary1222 recognition, unrestricted cancellation,
actual existence, historical novelty or proof-assistant certification
is made.
