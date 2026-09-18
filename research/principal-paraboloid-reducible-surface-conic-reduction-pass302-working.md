# A conic bound for the reducible paraboloid surface

Working result: in the actual nonzero-coupling chart264, a reducible
cubic surface level forces the projected plane equation to have degree
at most two. All three intrinsic generators have degree at most two
in the original generic polynomial-line parameter. If the two monic
surface factors differ by a formal constant, the projected equation
is a line and all three generators are affine.

This strengthens the reducible-surface alternative of300. The actual
normalization below is used only after its coefficients have been
proved complex. It preserves the surface level, not just the projected
degree. No ambient recognition or exclusion of every reducible
surface is asserted.

## 1. Exact retained entry and the two alternatives

Retain the complete actual hypotheses of the fully read
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
[290](principal-paraboloid-nonzero-coupling-projection-pass290-working.md),
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md),
and the reducible-surface argument of the fully read
[300](principal-paraboloid-plane-degree-refinement-pass300-working.md).
In particular,
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,
\quad \deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(X^2Z-Y^2),\quad a=EX\ne0,
\quad [L:\mathbb C(t,s)]<\infty,\\
O=L[v]=L[y,\sigma,\theta],\quad Nv=1,\quad
K=\mathbb C(y,z,w)=L(v),\quad m=k_s\ne0,\\
\det\frac{\partial(Y,Z,W)}{\partial(t,s,v)}=-a^4\in L^*.
\end{gathered}
\tag{1}
\]
The coefficient partials commute, fix v, and have joint constants
\(\mathbb C\). The literal Z-partial supplies the exact selected
shift-four derivation N. All new coefficient parameters remain in L.

Use the formal polynomials of296:
\[
\begin{aligned}
F&=k_{tt}P^2/2+k_{ts}PV+k_{ss}V^2/2+n_tP+n_sV,\\
\gamma&=2P+k_t,\quad D=\gamma/m,\quad \lambda=F_V/m,
\quad g=(\ell-\gamma U-F)/m,\\
H&=U^2+F_PU+F_Vg+H_3(k)+H_2(n)-\ell_tP-\ell_sV,\\
H_0&=H-h_0=U^2+A_1U+A_0,\qquad
A_1=F_P-DF_V,\quad \deg A_1\le2,\quad\deg A_0\le3.
\end{aligned}
\tag{2}
\]
The Taylor polynomials have factorial denominators. The evaluated
gradients of H and the fourth potential Q have unit two-by-two
minor ideal in O, by296.

Assume H0 is reducible. Its monicity gives
\[
H_0=(U+A)(U+B),\qquad A,B\in L[P,V],\qquad
A+B=A_1,\quad AB=A_0,\quad \deg A,\deg B\le2.
\tag{3}
\]
The degree assertions and zero-factor cases follow as in300:
opposite terms of degree greater than two could cancel in A+B,
but their product could not cancel in AB. Relabel so the selected
factor is \(U+A\). Exactly one factor vanishes on the actual line,
because the first gradient is a unit ideal. Thus
\[
y=-A(\sigma,\theta),\qquad C:=L[\sigma,\theta]=O,\qquad
(B-A)(\sigma,\theta)=\eta\in L^*.
\tag{4}
\]
The unit follows since every evaluated derivative of H0 is
divisible by the other evaluated factor.

Let G generate the projected kernel in \(L[P,V]\), and put
\(d_G=\deg G\). The exact polynomial plane return gives
\[
d_G=\max(\deg_v\sigma,\deg_v\theta),\qquad
G_{d_G}=c\Lambda^{d_G},\quad c\in L^*,\quad
0\ne\Lambda\in L[P,V]_1.
\tag{5}
\]
This is the characteristic-polynomial and pole-order argument
fully supplied in271 Section5, not a rationality assumption on L.
If B-A is nonconstant, G divides the nonzero polynomial B-A-eta,
so300 already gives \(d_G\le2\). We sharpen the other alternative.

## 2. Constant factor difference forces constant coupling

Suppose the difference is formally constant:
\[
B-A=\eta\in L^*,\qquad
\Delta:=A_1^2-4A_0=\eta^2\quad\hbox{in }L[P,V].
\tag{6}
\]
Since deg A0 is at most three, the degree-four part of Delta
is the square of
\[
A_{1,2}=-\frac{2P(m_tP+m_sV)}m.
\tag{7}
\]
It vanishes only if \(m_t=m_s=0\). The joint-constant gate gives
\(m\in\mathbb C^*\).

Now deg A1 is at most one; (6) makes deg A0 at most two.
Thus H0 has no cubic part. With m constant, its only possible
cubic term is \(k_{ttt}P^3/6\): FV is the coefficient ns,
and all other terms in (2) have degree at most two.
Exact joint-constant integration therefore gives
\[
k=m s+\frac{\kappa}{2}t^2+b t+d,\qquad
m\in\mathbb C^*,\quad \kappa,b,d\in\mathbb C.
\tag{8}
\]
No condition on ns has yet been imposed. The normalization below
must retain arbitrary n and ell.

## 3. Actual normalization preserves the monic surface level

Use the actual polynomial reframe, with its inverse,
\[
W_*=mW+\frac{\kappa}{2}Z+bY+dX^2,\qquad
W=\frac{W_*-\kappa Z/2-bY-dX^2}{m}.
\tag{9}
\]
It fixes X,Y,Z. The complete fixed-X map gives
\[
\begin{aligned}
s_*&=k,\qquad k_*=s_*,\qquad m_*=1,\\
\theta_*&=m\theta+k_t\sigma+\kappa k/2,\\
w_*&=mw+\kappa z/2+by,\qquad n_*=n-\kappa k/2.
\end{aligned}
\tag{10}
\]
The new coefficient derivatives and second-potential coefficient are
\[
\begin{aligned}
\partial_{t,*}&=\partial_t-(k_t/m)\partial_s,\qquad
\partial_{s,*}=m^{-1}\partial_s,\qquad
\nu_*=n_s/m-\kappa/2,\\
\ell_*&=\ell+\kappa n/2+(\kappa k/2)\nu_*.
\end{aligned}
\tag{11}
\]
Here nu* can be nonconstant. Indeed
\((n_*)_{t,*}=n_t-k_tn_s/m\), \((n_*)_{s,*}=\nu_*\);
substitution into
\(w_*+2\sigma y+(n_*)_{t,*}\sigma+\nu_*\theta_*\)
cancels the sigma and theta terms and gives exactly ell*.

The surface level needs a separate check. Define H* by the literal
formula (2) using the new derivatives and k*,n*,ell*. Put
\(\Phi(P,V)=mV+k_tP+\kappa k/2\). Then
\[
H_*(U,P,\Phi(P,V))-H(U,P,V)=c_*\in L.
\tag{12}
\]
Here is a derivative-preserving proof. The first two potentials
transform exactly by (10),(11). The actual row change multiplies
the generic determinant by m, while the coefficient change divides
it by m. Before any surface level is imposed,296 identifies its
X-squared coefficient with the line derivative of H. Apply this
universal row identity to arbitrary formal intercept functions.
The line derivative of the difference in (12) is zero for every
independent first jet of the three intercepts. Therefore each of
its formal U,P,V derivatives is zero. The difference belongs to L.
This uses the raw coefficient identity, not just its evaluation
on the selected curve.

The constant is also explicit. With \(c_1=\kappa k/2\), evaluating
at U=P=V=0 gives
\[
c_*=\nu_*\ell_*-c_1\nu_*^2
 +\frac{c_1^2n_{ss}}{2m^2}
 -c_1\partial_{s,*}\ell_*-\frac{n_s\ell}{m}.
\tag{13}
\]
Consequently \(h_{0,*}=h_0+c_*\), and
\[
(H_*-h_{0,*})(U,P,\Phi(P,V))=H_0(U,P,V).
\tag{14}
\]
The formal constant factor difference and discriminant are genuinely
preserved. Preservation of the projected degree alone would not
justify this conclusion.

All actual chart gates survive (9), as in the fully read295
normalization, but here with arbitrary n. The complex invertible
weighted leading map fixes the entire initial ideal. The new s*
is independent of t, and the intercept change preserves both
strong K-return and whole O-return. The new literal Z-partial is
\(\partial_Z-\kappa\partial_W/(2m)\). The old W-partial has shift
at most three by264's retained minor criterion, since its omitted
leading triple X,Y,Z is dependent. It cannot alter the selected
shift-four N. Thus L,O,Nv=1 are retained. The two compensating
determinant factors above preserve the exact calibration \(-a^4\).
Finally Phi is an invertible affine L-plane map, preserving the
projected equation's total degree.

## 4. Constant discriminant forces a projected line

Drop the stars. Now k=s, m=1, n and ell are still arbitrary,
and the formal discriminant is constant in P,V. Its entire expansion is
\[
\begin{aligned}
\Delta={}&(4n_s^2-2n_{tt})P^2-4n_{ts}PV-2n_{ss}V^2\\
 &+4\ell_tP+4(\ell_s+n_s^2)V+n_t^2-4n_s\ell+4h_0.
\end{aligned}
\tag{15}
\]
Thus
\[
n_{ss}=n_{ts}=0,\quad n_{tt}=2n_s^2,\quad
\ell_t=0,\quad \ell_s=-n_s^2.
\tag{16}
\]
Both partials kill ns, so it is a complex constant nu. Further
exact integrations give
\[
n=\nu s+\nu^2t^2+b_1t+c_2,\qquad
\ell=-\nu^2s+\ell_0,\qquad
\nu,b_1,c_2,\ell_0\in\mathbb C.
\tag{17}
\]
This includes nu=0. Write \(f=\nu^2t^2+b_1t+c_2\). The surface
and full corrected fourth gradients are
\[
\begin{aligned}
H&=U^2+(f'-2\nu P)U-\nu f'P+\nu^2P^2+\nu\ell,\\
Q_U&=0,\qquad Q_P=-h_{0,t}-\nu^2f',\qquad
Q_V=-h_{0,s}-\nu^3.
\end{aligned}
\tag{18}
\]
Indeed \(H_V=0\),
\(H_P=-2\nu U-\nu f'+2\nu^2P\), and
\(H_U=2U+f'-2\nu P\), so \(Q_U=H_P+\nu H_U=0\).
The other identities follow from296's coefficient derivatives
with U,P,V held fixed.

The last two coefficients in (18) cannot both vanish, since all
evaluated two-gradient minors would then vanish. Hence Q-q0 is
a nonzero affine polynomial in P,V vanishing on the projected curve.
Its equation G has degree one. Transporting back preserves this:
\[
B-A\in L^*\text{ formally}\quad\Longrightarrow\quad d_G=1.
\tag{19}
\]
Moreover A,B have degree at most one in this case: B=A+eta
and a quadratic A would make AB quartic. Equations (4),(5)
make y,sigma,theta affine in v already in the original chart.

## 5. A genuine conic has a distinguished affine generator

Return to the original chart and suppose \(d_G=2\). The factor
difference is nonconstant by (19). Equal-degree divisibility gives
\[
B-A-\eta=cG,\qquad c\in L^*.
\tag{20}
\]
At least one of A,B has degree at most one, since otherwise AB
would have degree four. Thus the degree-two part of B-A is plus
or minus A1,2. By (5),(7),(20), the nonzero polynomial
\(-2P(m_tP+m_sV)/m\) is a pure square of a linear form. Therefore
\[
m_s=0,\qquad m_t\ne0,\qquad G_2=c_3P^2,\quad c_3\in L^*.
\tag{21}
\]
If ms were nonzero its two factors would be distinct; if mt
also vanished, the whole quadratic part would be zero.

The affine-linear part of G has a nonzero V coefficient.
Otherwise G would be a polynomial only in P. Its vanishing at
sigma in L[v] would make sigma a constant in L and give a
linear factor of G over L, contrary to irreducibility. Hence
theta is a quadratic polynomial in sigma over L. Whole return gives
\[
L[v]=L[\sigma],\qquad \deg_v\sigma=1,\qquad \deg_v\theta=2.
\tag{22}
\]
Finally (4) gives \(y=(\eta-A_1^{\rm ev})/2\). When ms=0,
the full coefficient is
\[
A_1=-\frac{2m_t}{m}P^2+m_tV
 +\left(k_{tt}-\frac{k_tm_t+2n_s}{m}\right)P
 +n_t-\frac{k_tn_s}{m}.
\tag{23}
\]
Its evaluation using (22) has degree at most two in v.
So does y. No coefficient is asserted to be an ambient polynomial.

## 6. Precise result and remaining boundary

Together with300's nonconstant-difference bound, the alternatives yield
\[
\boxed{H-h_0\text{ reducible in }L[U,P,V]
\ \Longrightarrow\
L[\sigma,\theta]=L[v],\quad d_G\le2,\quad
\max(\deg_vy,\deg_v\sigma,\deg_v\theta)\le2.}
\tag{24}
\]
For dG=1 the final degree bound follows from (3) and the affine
projected generators. For dG=2 the stronger description (21)--(23)
holds. For formally constant factor difference all three generators
are affine. In particular an original ms different from zero permits
only a projected line in this reducible-surface sector.

The note does not promote a projected generator or surface factor
to an ambient coordinate. It gives no recognition or realization
result, does not address300's irreducible-surface alternative, and
leaves unrestricted cancellation unsolved. The actual normalization
was justified only under the constant-discriminant coefficient gates,
not for arbitrary coupling.

The complete300 and295 sources and the directly used296 proof were
read before this argument. Fresh unsaved generic algebra checked both
potential transports with arbitrary n and ell, the formal surface
gradient difference in (12), and the entire normalized discriminant.
The exact-field and actual-ring conclusions are the written arguments,
not finite sampling assertions. No saved checker was executed,
imported, compiled or rerun; no retained proof, checker, index or
packet was edited. No novelty, human-expert review or proof-assistant
certification is claimed.
