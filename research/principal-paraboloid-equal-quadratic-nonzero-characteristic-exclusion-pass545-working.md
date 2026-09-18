# Equal quadratic slopes force zero characteristic coupling derivative

Working conditional result: retain the FULL actual chart264, the genuine
potentials and gradient-unit hypotheses of296, and the denominator-free
multiplier of535. Suppose
\[
\deg_v\sigma=\deg_v\theta=2,\qquad m=k_s\ne0.
\]
Let \(\mu=\operatorname{lc}_v(\theta)/\operatorname{lc}_v(\sigma)\in L^*\).
Then
\[
\boxed{m_t+\mu m_s=0.}
\tag{1}
\]
The proof excludes only the nonzero left side. It does not recognize the
remaining zero-characteristic branch, force \(\mu\) to be complex, or
provide entry into this chart for arbitrary cancellation data.

## 1. Actual hypotheses and intrinsic normalization

Retain every hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md)
and [535](principal-paraboloid-nonlinear-sigma-unit-multiplier-pass535-working.md).
In particular,
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u_{\rm glob}],\quad
E=\partial_{u_{\rm glob}},\quad X=a_0u_{\rm glob}+x_0,\quad a_0\ne0,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\qquad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the ENTIRE original initial kernel},\\
0\ne N=[u_{\rm glob}^4]\partial_Z|_A\in\operatorname{LND}(A),\quad
Na_0=Nt=Ns=0,\quad Nv=1,\\
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,\quad
O=L[A]=L[v]=L[y,\sigma,\theta],\\
\operatorname{Frac}A=L(v)=\mathbb C(y,z_{\rm int},w),\quad
L[y,z_{\rm int},w]=L[v],\quad
J_{t,s,v}(X)=-a_0^4\in L^*.
\end{gathered}
\tag{2}
\]
Here \(z_{\rm int}\) is the literal Z-intercept. The original global
slice, original coordinate frame, selected literal partial and both
returns are required. No projected-plane normality or irreducibility of
the level surface is assumed.

Write the quadratic sigma as \(a_\sigma(v-v_0)^2+c\), with
\(a_\sigma\in L^*\). In the finite coefficient extension
\(L'=L(\rho)\), \(\rho^2=a_\sigma\), put \(x=\rho(v-v_0)\).
This is an intrinsic affine change only, not an actual coordinate map.
It gives
\[
\sigma=x^2+c,\qquad \theta=\mu x^2+d x+e.
\tag{3}
\]
The exact coefficient partials now fix x. They commute, extend the
partials of \(\mathbb C(t,s)\), and have joint constants \(\mathbb C\).
There is no assumption that L or L' is rational. In particular
\(Nx=\rho\), not necessarily one.

For a general affine intrinsic change \(x=\rho v+\zeta\), the scalar,
primitive-cross multiplier and535 multiplier transform as
\[
J_x=J_v/\rho,\qquad \tau_x=\rho\tau_v,\qquad
\kappa_x=\kappa_v/\rho^2\in (L')^*.
\tag{4}
\]
Indeed the primitive tangent transforms by \(1/\rho\), whereas its
formal gradient cross product is unchanged. The chain rule in535's
two cleared expressions makes each transform by \(1/\rho^2\).
Thus its polynomial identities remain valid at every zero of
\(\beta=\sigma_x=2x\); no division by the value of beta is made.
Below \(\kappa=\kappa_x\). Since \(\rho^2\in L\), this multiplier
actually lies in \(L^*\).

The case \(d=0\) is already incompatible with the branch to be
excluded. Indeed then \(L(\sigma,\theta)=L(\sigma)\), and the
original projected map has degree two. The retained double-cover
calculation [303, Section 3](principal-paraboloid-double-cover-line-obstruction-pass303-working.md)
forces \(m_s=m_t=0\) under precisely this full actual input and
nonconstant sigma. Consequently (1) holds in that case. We may assume
\(d\ne0\). This uses only that retained necessary calculation, not an
upgraded recognition theorem or a classification of all projections.

## 2. Full rows, potentials and a quadratic bound for y

Put \(p=m_t\), \(h=m_s\), \(k_j=\partial_t^j k\). The literal rows are
\[
\begin{aligned}
Y&=y+\sigma X+tX^2,\\
Z&=2ty+\sigma^2+k_1\sigma+m\theta+n
                         +(2t\sigma+k)X+t^2X^2,\\
W&=w+\theta X+sX^2,\\
mw&=\ell-(2\sigma+k_1)y-F(\sigma,\theta),\\
F(P,V)&=k_2P^2/2+pPV+hV^2/2+n_tP+n_sV.
\end{aligned}
\tag{5}
\]
The complete formal H used in this note is
\[
\begin{aligned}
H(U,P,V)={}&U^2+F_PU+
 \frac{F_V}{m}\{\ell-(2P+k_1)U-F\}\\
&+\frac{k_3}{6}P^3+\frac{p_t}{2}P^2V
 +\frac{h_t}{2}PV^2+\frac{h_s}{6}V^3\\
&+\frac{n_{tt}}2P^2+n_{ts}PV+\frac{n_{ss}}2V^2
 -\ell_tP-\ell_sV,\qquad H(y,\sigma,\theta)=h_0\in L.
\end{aligned}
\tag{6}
\]
Formal differentiation precedes evaluation. Write
\(f=H_U^{\rm ev}\), \(g=H_V^{\rm ev}\), and
\[
D_f=(2\sigma+k_1)/m,\qquad
\nu=F_V^{\rm ev}/m,\qquad B_f=(2y+F_P^{\rm ev})/m.
\]
The full cleared polynomials from535 are
\[
\begin{aligned}
\mathcal A_\beta={}&\beta^2y_t+\beta\theta_xy_s+y_x^2
             -\beta\sigma_ty_x-\sigma_sy_x\theta_x,\\
\mathcal B_\beta={}&\beta^2(\theta_t+B_f)+D_f\beta y_x+y_x\theta_x
       +\beta(\theta_s+\nu-\sigma_t)\theta_x-\sigma_s\theta_x^2,\\
\mathcal A_\beta={}&\kappa g,\qquad
\mathcal B_\beta=-\kappa f,\qquad \kappa\in L^*.
\end{aligned}
\tag{7}
\]
These are consequences of the entire calibrated scalar, not selected
leading equations imposed on arbitrary polynomials.

If \(D_y=\deg_x y\ge3\), the two terms
\(\beta^2(2y/m)\) and \(D_f\beta y_x\) have combined coefficient
\(4(D_y+2)\operatorname{lc}(y)/m\) at degree \(D_y+2\).
Every remaining term in \(\mathcal B_\beta\) has degree at most
\(\max(D_y,4)\); the term \(y_x\theta_x\) is included in that bound.
Also \(\deg_x f\le\max(D_y,4)\). Equation (7) is impossible.
Therefore, including zero and constant y,
\[
y=A x^2+B x+C,\qquad A,B,C\in L'.
\tag{8}
\]
The normalized coefficient A and the ratio mu belong to the original
L: they are the original leading-coefficient ratios. No nonzero A or
B has been assumed.

## 3. Entire all-X divided-pair identity

Extend scalars to L'. The actual polynomial return gives
\(L'[X,Y,Z,W]=L'[X,x]\). Hence the divided differences of the three
rows generate the unit ideal in \(L'[X,x_1,x_2]\): apply a polynomial
inverse for x and telescope its difference. This includes diagonal
pairs, where divided differences are derivatives.

Let \(u=x_1+x_2\), use subscripts for evaluation, and write brackets
for divided differences. Define
\[
\mathcal P=u(\sigma_1+\sigma_2+k_1)+m(\mu u+d).
\tag{9}
\]
After \(Y[x_1,x_2]=y[x_1,x_2]+Xu=0\), the Z divided difference
is exactly \(\mathcal P\). Define
\[
\begin{aligned}
G={}&u\{y_1+y_2+k_2(\sigma_1+\sigma_2)/2
                     +p(\theta_1+\theta_2)/2+n_t\}\\
&+(\mu u+d)\{p(\sigma_1+\sigma_2)/2
                     +h(\theta_1+\theta_2)/2+n_s\}.
\end{aligned}
\]
The entire third row, including every lower coefficient, satisfies
\[
mW[x_1,x_2]+G+(\sigma_1+\sigma_2+k_1)
                  (y[x_1,x_2]+Xu)-X\mathcal P=0.
\tag{10}
\]

On \(\mathcal P=0\), u is nonzero because \(md\ne0\). For every
\(u\in\overline{L'}^*\), a finite pair exists: take the roots of
\[
T^2-uT+\frac{u^2+2c+k_1+m\mu+md/u}{2}=0.
\tag{11}
\]
Repeated roots are allowed. Set \(X=-y[x_1,x_2]/u\) only AFTER
forming all divided differences. Put
\[
\begin{gathered}
q=p+h\mu,\quad \Phi=k_2+2p\mu+h\mu^2,\quad
K_1=k_1+m\mu,\quad \nu_0=\{h(e-\mu c)+n_s\}/m,\\
S_\sigma=-K_1-md/u,\quad
S_\theta=\mu(S_\sigma-2c)+du+2e,\quad
S_y=A(S_\sigma-2c)+Bu+2C.
\end{gathered}
\tag{12}
\]
The full Laurent polynomial \(\mathcal L=G/u\) is
\[
\begin{aligned}
\mathcal L={}&S_y+k_2S_\sigma/2+pS_\theta/2+n_t
 +(\mu+d/u)(pS_\sigma/2+hS_\theta/2+n_s)\\
={}&(B+qd/2)u+\Lambda_0
 +\frac{md}{u}\left(\nu_0-A-\frac{qK_1}{2m}-\frac\Phi2\right)
 -\frac{md^2q}{2u^2},\\
\Lambda_0={}&2C-A(2c+K_1)-\Phi K_1/2
                  +q(e-\mu c)+\mu n_s+n_t+hd^2/2.
\end{aligned}
\tag{13}
\]
By (10), any nonzero root of this Laurent polynomial would annihilate
all three divided rows, contradicting the unit ideal. Thus it is a
nonzero Laurent monomial. This assertion neither deletes critical
points nor specializes an actual ambient coordinate over L'.

Assume henceforth \(q\ne0\). Its \(u^{-2}\) coefficient is nonzero,
so every other coefficient in (13) vanishes:
\[
B=-qd/2,\qquad
A=\nu_0-\frac{qK_1}{2m}-\frac\Phi2,\qquad \Lambda_0=0.
\tag{14}
\]
Neither p nor h has been divided by. All zero choices of lower
coefficients remain available subject to these equations.

## 4. Complete high coefficients and characteristic identities

Define the coefficient derivation and three coefficient functions
\[
\begin{gathered}
\mathcal D=\partial_t+\mu\partial_s,\qquad
\chi=(4A+\Phi)/m,\qquad \delta=\mathcal D\mu,\\
M_2=p_t+2\mu h_t+\mu^2h_s,\qquad
K_3=k_3+3\mu p_t+3\mu^2h_t+\mu^3h_s.
\end{gathered}
\tag{15}
\]
Direct expansion of the FULL (6),(7), without dropping any lower
coefficients, gives
\[
\begin{aligned}
[x^6]H^{\rm ev}&=(K_3-3q\chi)/6,\\
[x^5]H^{\rm ev}&=d(M_2-h\chi)/2
                           -2q(B+qd/2)/m,\\
[x^4]g&=(M_2-h\chi)/2-q^2/m,\\
[x^4]\mathcal A_\beta&=4\mathcal DA,\\
[x^4](\mathcal B_\beta+\kappa f)
                       &=4(\delta+\chi)-2\kappa q/m.
\end{aligned}
\tag{16}
\]
Equations (14),(16), the genuine level and (7) imply
\[
M_2=h\chi,\quad K_3=3q\chi,\quad
\mathcal DA=-\frac{\kappa q^2}{4m}\ne0,\quad
\delta+\chi=\frac{\kappa q}{2m}.
\tag{17}
\]
In particular A is noncomplex. The mixed derivatives of the original
k give \(\mathcal Dm=q\), and direct differentiation gives
\[
\mathcal Dq=M_2+h\delta=\frac{\kappa hq}{2m},\qquad
\mathcal D\Phi=K_3+2q\delta.
\]
Differentiate \(m\chi=4A+\Phi\) and substitute (17). The resulting
identity is \(q\chi+m\mathcal D\chi=q\chi\). Thus
\[
\boxed{\mathcal D\chi=0.}
\tag{18}
\]
No rationality of a characteristic constant field is used here.

## 5. Actual invariant relation and complex descent of chi

Here is the actual derivation used for both initial arguments. Extend
N to \(A[u_{\rm glob}]\) by \(Nu_{\rm glob}=0\), and put
\[
\Delta=a_0N-(NX)E.
\tag{19}
\]
It preserves the original polynomial ring and fixes X. In
\(A_{a_0}[X]\) it is \(a_0N\) with X fixed, hence is locally
nilpotent. It is nonzero because N is. Consequently it restricts to
a nonzero LND of the ACTUAL ring
\[
R=\mathbb C(X)[Y,Z,W],\qquad
\operatorname{Frac}R=L(v)(X).
\tag{20}
\]
A local slice gives \(\operatorname{trdeg}_{\mathbb C(X)}\ker_R\Delta=2\):
if \(\Delta b=a\ne0\), \(\Delta a=0\), localization at a gives
the slice b/a and the usual polynomial slice decomposition. In
particular a nonconstant actual polynomial invariant exists.

The finite extension \(L'(X)(x)\) contains this fraction field;
they are NOT asserted equal. On that extension
\(\Delta=a_0\rho\partial_x\). Thus every actual invariant has
intrinsic degree zero. Whenever the three actual coordinates have
positive intrinsic degrees, a nonconstant invariant supplies a
nonzero relation among their weighted initials, by taking its top
positive-weight part.

From (5),(14), the complete leading intercept coefficients are
\[
w_4=-\chi/2,\qquad w_3=0,\qquad
w_2=\mu A-\chi(2c+k_1+m\mu)/2.
\tag{21}
\]
Suppose \(\chi\notin\mathbb C\), so \(\chi\ne0\). The actual
degree profile is \((2,4,4)\), with initials
\[
(X+A)\xi^2,\qquad \xi^4,\qquad -\chi\xi^4/2.
\tag{22}
\]
If A and chi were algebraically independent over C, these three
initials would be algebraically independent over \(\mathbb C(X)\),
as is seen from the ratios \((X+A)^2\) and \(-\chi/2\) and the
independent symbol xi. That contradicts (20). Thus A is algebraic
over \(\mathbb C(\chi)\). Separability and (18) then force
\(\mathcal DA=0\), contradicting (17). This also accounts for all
finite coefficient extensions. We conclude
\[
\chi\in\mathbb C,
\tag{23}
\]
including the case chi equals zero from the outset.

## 6. A licensed actual shear, not a coefficient-field reframe

Set \(c_*=\chi/2\in\mathbb C\), and make the ACTUAL change
\[
X^*=X,\quad Y^*=Y,\quad Z^*=Z,\quad W^*=W+c_*Z.
\tag{24}
\]
Its polynomial inverse subtracts \(c_*Z^*\). It is a member of the
fully checked actual family426. More explicitly,
\[
t^*=t,\quad s^*=s+c_*t^2,\quad a_0^*=a_0,\quad
\sigma^*=\sigma,\quad y^*=y,\quad
\theta^*=\theta+2c_*t\sigma+c_*k,\quad k^*=k.
\tag{25}
\]
The last equality is a pullback identity; starred derivatives fix
\(s^*\), so \(\partial_{t^*}=\partial_t-\chi t\partial_s\) and
\(\partial_{s^*}=\partial_s\). The full original initial relation
is preserved by the invertible weighted leading map. The exact
time degrees remain \((1,2,2,2)\), since \(t,s+c_*t^2\) are
algebraically independent.

The selected literal coordinate partial is
\(\partial_{Z^*}=\partial_Z-c_*\partial_W\). The retained
omitted-W bound from264/158, explicitly used in426, is
\([u_{\rm glob}^4]\partial_W|_A=0\). Hence \(N^*=N\), with the
same original slice v, coefficient field L, a0 and global slice.
The original strong return follows from
\(\mathcal B_{a_0}=A_{a_0}[X^*]\) by evaluating at \(X^*=0\)
in the actual starred frame; its intercept is again the literal
Z*-intercept. The L-polynomial return follows as well. Alternatively
the map of \((y,\sigma,\theta)\) in (25) is invertible affine over L.
The row determinant and coefficient-parameter determinant are both
one, so the full scalar remains \(-a_0^4\), and remains
\(-a_0^4/\rho\) in the centered x parameter. These statements use
the actual inverse and quotient, not an L-valued ambient shear.

The quadratic ratio and characteristic data transform by
\[
\mu^*=\mu+\chi t,\quad p^*=p-\chi th,\quad h^*=h,
\quad q^*=q,\quad A^*=A,\quad \Phi^*=\Phi-\chi m,\quad
\chi^*=0,\quad \mathcal D^*=\mathcal D.
\tag{26}
\]
These identities include the moving-parameter derivatives of k.
In particular \(\mathcal D\mu^*=\kappa q/(2m)\ne0\), so the
new ratio is nonzero and noncomplex. Reapply (13)--(21) in this
actual new chart and drop stars. Then
\[
\chi=0,\qquad w_4=w_3=0,\qquad w_2=\mu A,
\qquad w_1=d(A-\mu q/2).
\tag{27}
\]
Thus the exact actual intrinsic profile is \((2,4,2)\), with
initials \((X+A)\xi^2,\xi^4,\mu(X+A)\xi^2\). In particular
the intrinsic Z leader never drops in this argument.

## 7. A complete weak initial-relation bound for this actual ring

Use weights \((2,4,2)\) in the actual variables \((Y,Z,W)\), and
let \(\mathfrak p\) be the full kernel of their initial map over
\(K=\mathbb C(X)\). Since mu is noncomplex, the Y and W initials
are algebraically independent: homogeneous polynomials in them
reduce to nonzero polynomials in mu. Section 5 supplies a nonzero
relation, so \(\mathfrak p\) has height one. The polynomial UFD
gives \(\mathfrak p=(H)\) with H irreducible and weighted
homogeneous. It necessarily depends on Z.

Consider the ACTUAL coordinate partial \(\partial_Z\) of R holding
Y and W fixed. Extend it uniquely through the finite separable
extension \(L'(X)(x)/\operatorname{Frac}R\). Cramer's rule applied
to the full scalar matrix in \((t,s,x)\) gives coefficients of
\(\partial_t,\partial_s\) of intrinsic degree at most three and
a coefficient of \(\partial_x\) of degree at most four: the two
other rows have intrinsic degree two, their x derivatives degree
at most one, and the full determinant is \(-a_0^4/\rho\in(L')^*\).
Consequently this extended partial sends any polynomial of
intrinsic degree j to one of degree at most \(j+3\).

Take a nonconstant actual invariant F, and let its highest weighted
part have weight M and equal \(H^\ell G\), where \(\ell\ge1\)
and \(H\nmid G\). Such a factor exists because the intrinsic
degree of F is zero. Since H depends on Z, characteristic zero
gives \(H_Z\notin(H)\). Modulo H, the \(\ell\)-th coordinate
partial of the top part is
\(\ell!H_Z^\ell G\ne0\). Therefore
\[
\deg_x(\partial_Z^\ell F)=M-4\ell.
\]
On the other hand F starts with intrinsic degree zero, and the
cofactor bound gives \(\deg_x(\partial_Z^\ell F)\le3\ell\).
It follows that
\[
\boxed{\operatorname{wt}H\le7.}
\tag{28}
\]
All three weights are positive, so M is positive for a nonconstant
F. This proof needs neither a global Delta slice nor a strict
filtered-growth refinement of (28). The extension of the partial
does not identify the actual ring with a polynomial ring over L'.

## 8. Low support and the rational-square contradiction

All weights are even, so (28) gives \(\operatorname{wt}H\le6\).
A relation in Y,W alone is impossible. Thus H has exactly one
power of Z. Writing its homogeneous terms and evaluating yields
\[
(X+A)^2 Q(\mu)+L(\mu)=0,
\qquad 0\ne Q,L\in\mathbb C(X)[T],\quad
\deg Q\le3,\quad \deg L\le1.
\tag{29}
\]
For weight four the Z coefficient is constant and the other part
has degree two; weight six gives a linear Z coefficient and a
cubic other part. Weight two cannot involve Z. A missing side of
(29) would again be a nonzero polynomial relation for mu over
\(\mathbb C(X)\), and is impossible.

Regard X now as the independent transcendental over L'. Equation
(29) says \((X+A)^2\in\mathbb C(X,\mu)\). The formal derivation
\(\partial_X\), fixing L', shows
\(2(X+A)\in\mathbb C(X,\mu)\), hence
\[
A\in\mathbb C(X,\mu)\cap L'=\mathbb C(\mu).
\tag{30}
\]
The intersection is the elementary pure-transcendental intersection;
it does not assume beforehand that A is rational in mu. Write
\(A=a(\mu)/b(\mu)\) with coprime \(a,b\in\mathbb C[T]\),
\(b\ne0\). Since \(\mathcal DA\ne0\), this function is
nonconstant, and \(e_0=\max(\deg a,\deg b)\ge1\).

Clear b squared in (29), using a new formal variable T:
\[
(Xb+a)^2Q+b^2L=0\quad\hbox{in }\mathbb C(X)[T].
\tag{31}
\]
The polynomials \(Xb+a\) and b are coprime. Thus
\((Xb+a)^2\) divides L. Its degree in T is \(2e_0\ge2\):
there is no leading cancellation with the independent X. This
contradicts \(\deg L\le1\). The contradiction proves (1).

## 9. Exact remaining scope and verification

If m is complex, (1) is automatic. For noncomplex m, the conclusion
is the necessary equation \(p+h\mu=0\); then \(h\ne0\) and
\(\mu=-p/h\). This note gives no recognition or exclusion of that
remaining branch, and makes no assertion that its coefficient-field
shear is an actual complex coordinate change. Constant or vanishing
A, B, p or h were not divided away; (17) itself excludes constant A
only under the contradictory assumption q nonzero.

The full current535 and426 sources were reread through EOF for this
writeup. The full303 double-cover scope had been read before the
outline calculation. The actual264/296 hypotheses are retained in
full. No historical recognition ancestor is recursively recertified.
Fresh unsaved193422 and b4ab6f reconstruct the entire formal (6),
the entire cleared (7), all five unrestricted coefficients in (16),
and every coefficient in (21),(27); all residuals are zero. Fresh
6c9877 reconstructs the entire divided-row identity (10), and 16afec
checks the full Laurent ledger (13), with all lower terms retained.
Fresh b4ab6f also checks the moving-star identities for q and Phi.
The actual-LND, finite-extension, initial-kernel, exact derivative
multiplicity and polynomial divisibility arguments are given above.

No saved checker was executed, imported, compiled or rerun. No earlier
source or canonical file was edited. This is a bounded conditional
exclusion, not unrestricted cancellation, an arbitrary-chart entry
theorem, novelty, external review or formal certification. Complete
independent saved-source review remains separate from this author
verification.
