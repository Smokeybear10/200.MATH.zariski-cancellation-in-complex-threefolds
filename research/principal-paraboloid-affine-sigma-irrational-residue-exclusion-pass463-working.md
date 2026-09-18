# Affine sigma: the scalar and a minor force an impossible algebraic residue

Working exclusion: in the entire supplied actual264 chart with
k=s+f, f_s=0, n_ss nonzero and f''' nonzero, sigma cannot have
intrinsic degree one.

The proof uses the necessary affine-sigma reduction459 and the strict
coefficient formula460. The genuine fourth-potential minor gives a
quadratic equation for one coefficient ratio. Two complete coefficients
of the ORIGINAL calibrated scalar then force an irrational logarithmic
residue for a nonzero element of a finite extension of C(t). The field
norm makes that impossible.

No other intrinsic degree, arbitrary chart-entry problem or recognition
endpoint is settled here. In particular no coefficient-field change
below is promoted to an original complex polynomial automorphism.

## 1. Entire actual input and the moving intrinsic parameter

Retain EVERY hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md)
and the arbitrary-n equations of
[458](principal-paraboloid-arbitrary-first-potential-birational-projection-pass458-working.md).
Write the original invariant ring as mathcal A in this note, reserving
A without decoration for a scalar coefficient. The actual data include
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=\mathcal A[u],\qquad E=\partial_u,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\qquad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the ENTIRE weighted initial kernel},\\
X=a_0u+x_0,\quad a_0\in L^*,\quad x_0\in\mathcal A,\qquad
N=[u^4]\partial_Z|_{\mathcal A}\ne0,\\
L=\operatorname{Frac}\ker_{\mathcal A}N,\quad
[L:\mathbb C(t,s)]<\infty,\quad Nv_0=1,\\
O=L[\mathcal A]=L[v_0]=L[y,\sigma,\theta],\qquad
\operatorname{Frac}\mathcal A=L(v_0)=\mathbb C(y,z,w),\\
\det\frac{\partial(Y,Z,W)}{\partial(t,s,v_0)}=-a_0^4\in L^*.
\end{gathered}
\tag{1}
\]
All other original slice, localization, selected-partial and return
conditions are retained, not replaced by the displayed formal data.
The exact coefficient partials on L commute and have joint constants C.
The field
\[
\mathbb F=\ker_L\partial_s,\qquad [\mathbb F:\mathbb C(t)]<\infty
\tag{2}
\]
is not assumed rational. Primes on a member of mathbb F mean its
exact t-derivatives.

Assume for contradiction
\[
k=s+f,\quad f\in\mathbb F,\qquad
e=n_{ss}\ne0,\quad f'''\ne0,\qquad \deg_{v_0}\sigma=1.
\tag{3}
\]
By
[459](principal-paraboloid-affine-sigma-arbitrary-first-potential-reduction-pass459-working.md),
the centered x has degree two and
zeta=theta+sigma^2+f' sigma has degree one. Apply the STRICT case of
[460](principal-paraboloid-nonlinear-first-slope-tangent-degree-reduction-pass460-working.md):
here the common centered degree is two and 2*2>3*1. The leading
coefficient of the centered q is -1 because zeta is affine. Therefore
the ratio called eta in460 is minus the leading coefficient of y.
Its exact formula gives
\[
A=\frac1{2(t-\tau)},\qquad \tau\in\mathbb C,\qquad
A_t=-2A^2,\quad A_s=0,\qquad
e=-2A^2,\qquad
n=-A^2s^2+\nu_0s+n_0,\quad \nu_0,n_0\in\mathbb F.
\tag{4}
\]
In particular A is nonzero. The element t-tau is a coefficient-field
element; no ambient time translation is performed.

Put P=sigma. This is an affine change of intrinsic polynomial
parameter over L, with
\[
\rho=NP\in L^*,\qquad
O=L[P],\qquad
\mathcal J:=\det\frac{\partial(Y,Z,W)}{\partial(t,s,P)}
             =-\frac{a_0^4}{\rho}\in L^*.
\tag{5}
\]
The coefficient partials in this determinant fix P and X. Indeed the
change from (t,s,v0) to (t,s,P) has determinant rho, even when the
two coefficients of P in v0 move with t,s. We neither set rho=1
nor identify P with the original slice u.

The full intrinsic forms are
\[
y=AP^2+aP+c,\qquad
\theta=-P^2+dP+g,\qquad
M=d+f'\ne0,\qquad a,c,d,g\in L.
\tag{6}
\]
Their derivatives below always retain the moving coefficients.
For compact notation set
\[
f_j=\partial_t^j f,\quad
\nu=n_s,\quad b=n_{ts},\quad
\chi=f_2/2-\nu,\quad B_1=n_t-\nu f_1,\quad
E_0=\ell_s+\nu^2,\quad r=f_3/6\in\mathbb F^*.
\tag{7}
\]
Thus r is a scalar, distinct from the coefficient field mathbb F.
From(4),
\[
\nu=-2A^2s+\nu_0,\quad b=8A^3s+\nu_0',\quad
b_s=8A^3,\quad (b_t)_s=-48A^4,\quad \nu_s=-2A^2.
\tag{8}
\]
No condition b nonzero is imposed.

## 2. The genuine third and fourth gradients

The complete third polynomial is
\[
\begin{aligned}
H(U,P,V)={}&U^2+(2\chi P+B_1)U+rP^3
 +\frac{n_{tt}-\nu f_2}{2}P^2-(\nu n_t+\ell_t)P+\nu\ell\\
&+(bP-E_0)V+\frac e2V^2,\qquad
H(y,P,\theta)=h\in L.
\end{aligned}
\tag{9}
\]
The entire genuine Q is458(9), with Q(y,P,theta)=q0 in L.
In particular its exact gradients, with formal variables fixed in
coefficient derivatives, satisfy
\[
\begin{aligned}
Q_U&=H_P-(2P+f_1)H_V+\nu H_U,\\
Q_P&=H_t-h_t-(2U+f_2P+n_t)H_V+\nu H_P,\\
Q_V&=H_s-h_s.
\end{aligned}
\tag{10}
\]
Both actual level derivatives are retained. The following argument
uses(10), not a polynomial with freely chosen replacement coefficients.
The evaluated gradient minors of H,Q generate O, by296/458.

Write
\[
\mathcal U=H_U(y,P,\theta)=2y+2\chi P+B_1,\qquad
\mathcal V=H_V(y,P,\theta)=e\theta+bP-E_0.
\tag{11}
\]
Their leading coefficients are 2A and 2A^2, respectively.
The P^3 coefficient of(9) is
\[
2A^2d+2Aa+Af_2-2A\nu-b+r=0.
\tag{12}
\]
Consequently
\[
a=\nu-f_2/2-Ad+\frac{b-r}{2A},\qquad
\mathcal V=A\mathcal U+R,\qquad R=rP+R_0,\quad R_0\in L.
\tag{13}
\]
The same relation differentiated in s gives, using(8),
\[
a_s=2A^2-Ad_s.
\tag{14}
\]

The tangent in the parameter P is (y_P,1,theta_P). Both evaluated
formal gradients annihilate it. Their cross product is nonzero and
has component ideal O. Over L(P) it is a scalar multiple of that
tangent. Its middle component already shows that the multiplier
belongs to O; its component ideal then makes it a unit of O.
Thus
\[
\mathcal W:=(H_UQ_V-H_VQ_U)_{\rm ev}\in L^*.
\tag{15}
\]
This uses the full minor UNIT, not just a nonzero minor.

Differentiate the actual H level in P and in s, fixing P for the
latter derivative. Equation(10) then gives exactly
\[
Q_U|_{\rm ev}=\mathcal U(\nu-y_P)-\mathcal V M,\qquad
Q_V|_{\rm ev}=-\mathcal U y_s-\mathcal V\theta_s.
\tag{16}
\]
Therefore the entire relevant minor is
\[
\mathcal W=\mathcal V^2M+
 \mathcal U\mathcal V(y_P-\nu-\theta_s)-\mathcal U^2y_s.
\tag{17}
\]
Substitute(13), and use(14) to cancel the P coefficient in
A^2M+A(y_P-nu-theta_s)-y_s. The result is the complete identity
\[
\boxed{\mathcal W=D\mathcal U^2+
 R\mathcal U(\Lambda P+E)+MR^2,}
\tag{18}
\]
where
\[
\Lambda=2A-d_s,\qquad
D=A^2M+A(a-\nu-g_s)-c_s,\qquad
E=2AM+a-\nu-g_s.
\tag{19}
\]
No coefficient or moving derivative was dropped in this reduction.

## 3. Constant minor: the exact centered coefficient comparison

Since r is nonzero, there is a unique P0 in L with
R=r(P-P0). Put z=P-P0, so
\[
R=rz,\qquad
\mathcal U=2Az^2+h_1z+h_0,\qquad
E_*=E+\Lambda P_0.
\tag{20}
\]
For this paragraph only we compare polynomials over L, without taking
coefficient derivatives. Evaluating(18) at z=0 gives
W=D h0^2. Since W is a nonzero constant, both D and h0 are nonzero.
The degree-four coefficient gives
4A^2D+2ArLambda=0. Thus Lambda is also nonzero, and
D=-rLambda/(2A).
The degree-three and degree-two coefficients, in that order, give
\[
D=-\frac{r\Lambda}{2A},\qquad
E_*=\frac{\Lambda h_1}{2A},\qquad
M=\frac{\Lambda h_0}{r}.
\tag{21}
\]
For an exact check of all terms, substituting(21) into(18) leaves
\[
\mathcal W=-\frac{r\Lambda h_0}{2A}(h_0+h_1z).
\tag{22}
\]
The coefficient of z must vanish. Because r,Lambda,h0,A are all
nonzero, h1=0. Define eta=h0/2. We have proved
\[
\begin{gathered}
\mathcal U=2Az^2+2\eta,\qquad \mathcal V=A\mathcal U+rz,\\
\eta\ne0,\quad \Lambda\ne0,\quad E_*=0,\qquad
M=\frac{2\Lambda\eta}{r},\qquad
\mathcal W=-\frac{2r\Lambda\eta^2}{A}.
\end{gathered}
\tag{23}
\]
All divisions in this comparison are by coefficient elements already
proved nonzero. A zero constant or zero linear coefficient of any
unrelated polynomial was not excluded.

## 4. The moving center and its exact s-derivatives

Define the full cubic from the completion of(9):
\[
\begin{aligned}
\mathcal T(P)={}&rP^3+\frac{n_{tt}-\nu f_2}{2}P^2
 -(\nu n_t+\ell_t)P+\nu\ell-h\\
&-(\chi P+B_1/2)^2-\frac{(bP-E_0)^2}{2e}.
\end{aligned}
\tag{24}
\]
The exact H level can be written
\[
\frac{\mathcal U^2}{4}-\frac{\mathcal V^2}{4A^2}
                       +\mathcal T(P)=0.
\tag{25}
\]
Use(23) in(25). Every term is retained, and it gives
\[
\mathcal T(P_0+z)
 =rz^3+\frac{r^2}{4A^2}z^2+\frac{r\eta}{A}z.
\tag{26}
\]
In particular, if T2 denotes the P^2 coefficient of T,
\[
T_2=\frac{n_{tt}-\nu f_2}{2}-\chi^2+\frac{b^2}{4A^2},
\qquad
T_2+3rP_0=\frac{r^2}{4A^2}.
\tag{27}
\]

Formula(4) shows that T2 is in mathbb F[s] and has degree at most
one in s. Indeed its three possible s^2 coefficients are
-12A^4, -4A^4, +16A^4, which sum to zero. More explicitly,
\[
(T_2)_s=\frac{\nu_0''}{2}-A^2f_2+4A^2\nu_0+4A\nu_0'\in\mathbb F.
\tag{28}
\]
Since r and A belong to mathbb F, (27) proves P0_s belongs to
mathbb F. This is a statement about these particular elements, not
an assumption L=mathbb F(s).

In the moving parameter z the polynomials take the full form
\[
\begin{aligned}
y&=Az^2-\chi z+C,\qquad
C=\eta-\chi P_0-B_1/2,\\
\theta&=-z^2+mz+G,\qquad
m=\frac{b-r}{2A^2},\\
d&=m+2P_0,\qquad
M=m+2P_0+f_1,\qquad m_s=4A.
\end{aligned}
\tag{29}
\]
The formula for m follows either from(13) or from the linear
coefficient of V=e theta+bP-E0 in(23). Thus
\[
d_s=4A+2(P_0)_s,\qquad
\Lambda=-2\{A+(P_0)_s\}\in\mathbb F^*.
\tag{30}
\]

We now differentiate while FIXING P, not z. In particular
z_s=-(P0)_s, and the complete derivatives are
\[
\begin{aligned}
y_s&=A\Lambda z+C_s+\chi(P_0)_s,\\
\theta_s&=d_sz+G_s-m(P_0)_s,\\
y_P&=2Az-\chi.
\end{aligned}
\tag{31}
\]
The zero constant E* in(23), as read in the middle bracket of(18),
is precisely
2AM-f2/2-G_s+m(P0)_s=0. Therefore the constant D in that same
identity becomes
\[
D=-A^2M-\{C_s+\chi(P_0)_s\}.
\tag{32}
\]
Use C from(29), chi_s=2A^2 and (B1)_s=b+2A^2f1. Keeping every
moving-center term in(32) gives
\[
\begin{aligned}
D&=-A^2M-\eta_s+2A^2P_0+b/2+A^2f_1\\
 &=-A^2m+b/2-\eta_s
 =r/2-\eta_s.
\end{aligned}
\tag{33}
\]
Comparing with(21),
\[
\eta_s=\frac{r(A+\Lambda)}{2A}.
\tag{34}
\]
On the other hand differentiate M=2Lambda*eta/r in(23).
Both r and Lambda belong to mathbb F, while M_s=d_s=2A-Lambda.
Consequently
\[
\eta_s=\frac{r(2A-\Lambda)}{2\Lambda}.
\tag{35}
\]
Equating(34),(35) and dividing only by the nonzero A,Lambda,r gives
\[
\Lambda^2+2A\Lambda-2A^2=0,\qquad
\boxed{\lambda:=\Lambda/A=-1+\sqrt3\ \text{or}\ -1-\sqrt3.}
\tag{36}
\]
The displayed alternatives are actual complex constants: the
polynomial splits over C and L is a field. In particular lambda is
irrational over Q and is neither zero nor one.

## 5. Two complete coefficients of the original all-X scalar

The original literal rows, with no formal row substituted for an
actual generator, are
\[
\begin{aligned}
Y={}&AP^2+(a+X)P+c+tX^2,\\
Z={}&2tY+(d+f_1)P+g+n+(s+f)X-t^2X^2,\\
W={}&-2AP^3+(-2a-f_1A-f_2/2+\nu-X)P^2\\
 &+(-2c-f_1a-n_t-\nu d+dX)P
       +\ell-f_1c-\nu g+gX+sX^2.
\end{aligned}
\tag{37}
\]
These follow directly from264/458:
z=2ty+P^2+f1P+theta+n and
w=ell-(2P+f1)y-f2P^2/2-n_tP-nu theta.
They keep the original time coefficient t, including the constant
tau in(4). No specialization X to a moving coefficient is made.

For full reconstruction of the scalar, subtract 2t times its Y
derivative row from the Z derivative row. This is a row operation
on the Jacobian, not differentiation of Z-2tY without its product
term. If W_X denotes the entire last polynomial of(37), then
\[
\mathcal J=\det
\begin{pmatrix}
-2A^2P^2+a_tP+c_t+X^2 & a_sP+c_s & 2AP+a+X\\
B_t^* & B_s^* & M\\
(W_X)_t & (W_X)_s & (W_X)_P
\end{pmatrix},
\tag{38}
\]
where
\[
\begin{aligned}
B_t^*&=2AP^2+(2a+d_t+f_2+2X)P
                  +2c+g_t+n_t+f_1X,\\
B_s^*&=d_sP+g_s+\nu+X.
\end{aligned}
\tag{39}
\]
All coefficient derivatives in(38),(39) fix X,P. In particular
nu_t=b, nu_s=-2A^2, (n_t)_t=n_tt, (n_t)_s=b,
ell_t and ell_s remain actual derivatives, and
(f1)_t=f2,(f2)_t=f3. This determinant specifies the entire original
scalar, including all unused lower coefficients.

Differentiate the necessary identity(12) in t and s. Together with
(13),(14) the substitutions are exactly
\[
\begin{aligned}
a&=\nu-f_2/2-Ad+\frac{b}{2A}-\frac{f_3}{12A},\\
a_s&=2A^2-Ad_s,\\
a_t&=2b-\frac23f_3+2A^2d-Ad_t+\frac{b_t}{2A}-\frac{f_4}{12A}.
\end{aligned}
\tag{40}
\]
Define the coefficient
\[
\mathcal K=-12A^2f_2+48A^2\nu+48Ab-14Af_3+6b_t-f_4.
\tag{41}
\]
Using(8), its s-derivative is
-96A^4+384A^4-288A^4=0, so Kcal belongs to mathbb F.

Expanding(38) and applying only(40) gives the following COMPLETE
two coefficient identities:
\[
\begin{aligned}
C_{13}:=[XP^3]\mathcal J
={}&4Ac_s+4A^2g_s-4A^3f_1+4A^2f_2-8A^2\nu-10Ab\\
 &+2Af_3-b_t+\frac{f_3d_s}{3}+\frac{f_4}{6},\\
[X^0P^4]\mathcal J
={}&A C_{13}+\frac{(A-d_s)\mathcal K}{6}.
\end{aligned}
\tag{42}
\]
Neither identity suppresses a c_t,d_t,g_t contribution by assuming
it zero. Such terms cancel in these exact coefficients of the
original determinant. No H2 or H1 relation, lower Q coefficient,
or assumption on the value of the scalar was used to form(42).

The calibrated equality(5) makes both coefficients in(42) vanish.
But from(19),(36),
A-d_s=Lambda-A=(lambda-1)A is nonzero. Therefore
\[
\boxed{\mathcal K=0.}
\tag{43}
\]
The nonzero speed rho in(5) remains arbitrary throughout this
argument. Only the absence of positive X,P coefficients of that
coefficient-valued scalar is used here.

## 6. The forced residue and the finite-field norm contradiction

Differentiate the explicit T2 in(27), or use(28) and(8),(41).
The exact result is
\[
(T_2)_s=\frac{\mathcal K+14Af_3+f_4}{12}.
\tag{44}
\]
Differentiating the other equality in(27) gives
(P0)_s=-(T2)_s/(3r). Insert this into(30), use r=f3/6 and(43):
\[
\Lambda=\frac{8A+f_4/f_3}{3}.
\tag{45}
\]
Since Lambda=lambda A and A=1/[2(t-tau)],
\[
\boxed{\frac{f_4}{f_3}
 =\frac{\kappa}{t-\tau},\qquad
\kappa=\frac{3\lambda-8}{2}\in\mathbb C\setminus\mathbb Q.}
\tag{46}
\]
Here f3 is a nonzero element of the exact finite coefficient field
mathbb F. The irrationality follows directly from(36): rational
kappa would make lambda rational, but x^2+2x-2 has no rational root.

We give the elementary algebraic-field obstruction. Let
m=[mathbb F:C(t)] and put
G=Norm_{mathbb F/C(t)}(f3), a nonzero rational function of t.
The extension is separable because the characteristic is zero.
In a normal closure, write the norm as the product of the m
embeddings of f3 over C(t). The exact derivative on an algebraic
extension is unique: differentiating a separable minimal polynomial
determines the derivative of each algebraic element. Hence the
derivative commutes with those embeddings. Taking the logarithmic
derivative of the product, and using(46), gives
\[
\frac{G'}G
 =\sum_{\iota:\mathbb F\hookrightarrow\overline{\mathbb C(t)}}
       \iota\!\left(\frac{f_4}{f_3}\right)
 =\frac{m\kappa}{t-\tau}.
\tag{47}
\]
The residue of the logarithmic derivative of a nonzero rational
function at t=tau is an integer. Explicitly write
G=(t-tau)^j R(t), where j is an integer and R is regular and
nonzero at tau. Then G'/G=j/(t-tau)+R'/R and the second term is
regular there. Equation(47) therefore forces m*kappa=j in Z,
so kappa is rational, contradicting(46).

This proves that the affine-sigma hypothesis in(3) cannot occur.
The norm step does not assume mathbb F=C(t), integrate a chosen
rational ansatz, or promote t-tau to an original ambient coordinate.

## 7. Verification and the exact conclusion

The current459 and460 sources were read completely before using
their necessary reductions. Their full actual264/296/458 pedigree
is retained, not recursively certified here.

Fresh unsavedaf9b84 reconstructed every coefficient of the evaluated
third level; (12) is its exact P^3 coefficient. Fresh3f9972 and
e217e1 reconstructed the original all-X determinant and its high
coefficients while retaining every moving first derivative.
Fresh678211 independently rebuilt the determinant again directly
from all three literal rows and checked both COMPLETE identities
in(42), with zero residuals.

Fresh01c776 checked the entire polynomial comparison(21),(22), the
moving-center identity D=r/2-eta_s, the polynomial
2A^2-2A Lambda-Lambda^2 from(34),(35), the exact T2 derivative(44)
and the last reduction(45), all with zero residuals. The written
minor-unit, coefficient-field and norm arguments are the proofs,
not conclusions of a bounded numerical search.

Only this subcase is excluded: full actual264, k=s+f with f_s=0,
n_ss*f''' nonzero, and intrinsic degree sigma equal to one.
No other degree is declared impossible, no original invariant
coordinate is produced, and no formal coefficient solution is
declared an actual realization.

No saved checker was executed, imported, compiled or rerun.
Only this newly assigned source was created. No earlier source,
canonical README or ledger was changed, and no unrestricted
cancellation, historical novelty or formal-certification claim is made.
