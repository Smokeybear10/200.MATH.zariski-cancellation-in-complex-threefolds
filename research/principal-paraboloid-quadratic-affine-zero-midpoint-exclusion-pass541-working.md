# The zero-midpoint quadratic-affine branch is impossible

Working bounded exclusion: retain the FULL actual264/296/535 hypotheses
and the variable-coupling quadratic-sigma, affine-theta sector of537.
After the actual normalization of539, its branch
\[
C_0=0,\qquad \nu_0\ne0
\tag{1}
\]
is impossible. The proof works in the ORIGINAL coefficient and fraction
fields. No square root of the leading coefficient of sigma is adjoined
or assumed to descend.

This does not exclude the other branch of539, identify its lower
coefficients, or establish a general nonlinear-sigma recognition theorem.

## 1. Actual hypotheses and the normalized branch

Retain every actual hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
the genuine potentials, their moving levels and the unit ideals of
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md),
and the denominator-free unit multiplier of
[535](principal-paraboloid-nonlinear-sigma-unit-multiplier-pass535-working.md).
In particular,
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,
\qquad X=a_0u+x_0,\quad a_0\ne0,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\qquad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the ENTIRE original initial kernel},\\
0\ne N=[u^4]\partial_Z|_A,\qquad Na_0=Nt=Ns=0,\\
L=\operatorname{Frac}\ker_A N,\qquad
[L:\mathbb C(t,s)]<\infty,\qquad L[A]=L[v],\quad Nv=1,\\
\operatorname{Frac}A=L(v)=\mathbb C(y,z_{\rm int},w),\qquad
L[y,z_{\rm int},w]=L[v],\\
J_{t,s,v}(X)=-a_0^4\in L^*.
\end{gathered}
\tag{2}
\]
Here \(z_{\rm int}\) is the literal Z-intercept. It is not the intrinsic
parameter introduced below. The whole all-X return, not merely a
birational projection, remains part of the supplied actual chart.

Assume \(m=k_s\notin\mathbb C\), \(\deg_v\sigma=2\), and
\(\deg_v\theta=1\). Result
[537](principal-paraboloid-quadratic-sigma-affine-theta-longitudinal-exclusion-pass537-working.md)
gives \(m_t=0\), \(k_{tt}\in\mathbb C\), and
\(y+(k_{tt}/4)\sigma\in L\).
The complete actual transport in
[539](principal-paraboloid-quadratic-affine-transverse-normal-form-pass539-working.md)
therefore applies. More explicitly, write
\(q=k_{tt}/4\in\mathbb C\) and
\(b_0=k_t-4qt\in\mathbb C\). Its actual map and inverse are
\[
\begin{aligned}
X^*&=X-q,&Y^*&=Y+(b_0/2)X^*,& Z^*&=Z,&W^*&=W,\\
X&=X^*+q,&Y&=Y^*-(b_0/2)X^*,& Z&=Z^*,&W&=W^*.
\end{aligned}
\tag{3}
\]
This is a complex polynomial automorphism of determinant one, including
\(q=0\) or \(b_0=0\). It adds only smaller E-degree terms, so preserves
all four initial forms, their entire kernel, and t,s. It also preserves
the literal selected partial \(\partial_{Z^*}=\partial_Z\), hence the
ORIGINAL N, L, v and a0. In its full rows,
\[
\begin{aligned}
\sigma^*&=\sigma+2qt+b_0/2,&\theta^*&=\theta+2qs,\\
y^*&=y+q\sigma+q^2t,&k^*&=k-2qt^2-b_0t,\\
z_{\rm int}^*&=z_{\rm int}+q(2t\sigma+k)+q^2t^2,
&w^*&=w+q\theta+q^2s.
\end{aligned}
\tag{4}
\]
The full scalar is the old one evaluated at \(X=X^*+q\), so remains
\(-a_0^4\). The return statements in (2) for the new intercepts follow
from the actual fiber as proved in539: the coordinate prime X* cannot
divide a0 by E-degree, and
\(\mathcal B_{a_0}=A_{a_0}[X^*]\). Taking the X*=0 fiber and then
fractions or adjoining L gives precisely those returns, not just an
affine coefficient-field map. The new genuine potentials are those
of the transported actual chart.

Drop stars. Thus throughout the rest of the proof,
\[
k_t=0,\qquad m_t=0,\qquad h=m_s\ne0,\qquad y=r\in L.
\tag{5}
\]
The nonvanishing of h follows from noncomplex m and the joint constant
field \(\mathbb C\). No normalization of h has yet been made.

## 2. An original-field affine intrinsic parameter

In the ORIGINAL field write
\[
\sigma=A_\sigma(v-v_0)^2+c,\qquad
\theta=D(v-v_0)+e,
\quad A_\sigma,D\in L^*,\quad v_0,c,e\in L.
\]
Define
\[
z=\theta-e=D(v-v_0),\qquad
a=A_\sigma/D^2\in L^*,\qquad
\sigma=az^2+c,\qquad \theta=z+e.
\tag{6}
\]
In particular \(L[z]=L[v]\) and \(Nz=D\in L^*\).
This z is not the symbol used for the coefficient \(d^2\) in539.
All expressions in (6) belong to the original \(L[v]\).

The exact coefficient partials are now extended to fix z. Their
restrictions to L are unchanged. The speed, scalar and multiplier are
\[
J_{t,s,z}(X)=-a_0^4/D,\qquad
\kappa_z=\kappa_v/D^2\in L^*.
\tag{7}
\]
Indeed the affine intrinsic substitution has Jacobian D, while the
primitive cross-product multiplier changes by D. This is the full
affine covariance of535, including moving coefficient terms. Neither
\(Nz=1\) nor a constant scalar value after changing parameters is assumed.

Put \(\lambda=n_t\) and
\[
\nu=\frac{he+n_s}{m},\qquad
C_0=2r+\lambda+\frac{h}{2a}.
\tag{8}
\]
These are the same two coefficient-field quantities as in539. The
branch considered here is \(C_0=0\), \(\nu\ne0\). In particular,
\[
r=-\lambda/2-h/(4a).
\tag{9}
\]
The full second potential and actual rows, without any lower truncation,
give
\[
\begin{aligned}
w&=-\nu z+w_0,&
w_0&=\frac{\ell+h c/(2a)-he^2/2-n_se}{m},\\
Y&=r+X(az^2+c)+tX^2,\\
Z&=2tr+(az^2+c)^2+m(z+e)+n
                   +\{2t(az^2+c)+k\}X+t^2X^2,\\
W&=-\nu z+w_0+(z+e)X+sX^2.
\end{aligned}
\tag{10}
\]
Thus \(L[w]=L[z]\) here, but w and r are NOT promoted to actual ambient
coordinates. That equality alone is not the argument below.

## 3. Original-field potential gates and the nonzero r derivative

For completeness the branch restrictions needed from539 are rederived
in (6), with no square-root extension. The full formal third potential,
up to its moving coefficient-field level, is
\[
\begin{aligned}
H(U,P,V)={}&U^2+\lambda U+(hV+n_s)
 \frac{\ell-2PU-\lambda P-hV^2/2-n_sV}{m}\\
&+\frac{h_s}{6}V^3+\frac{n_{tt}}2P^2+
 \lambda_sPV+\frac{n_{ss}}2V^2-\ell_tP-\ell_sV.
\end{aligned}
\tag{11}
\]
At \((U,P,V)=(r,az^2+c,z+e)\), its level is in L. Its complete
coefficients of z4 and z3 are respectively
\[
\frac{a^2n_{tt}}2,\qquad \frac{h_s}{6}+a\lambda_s.
\tag{12}
\]
The first gives \(\lambda_t=0\). The second gives
\(\lambda_s+h_s/(6a)=0\).

Let \(f=H_U^{\rm ev}\) and \(\beta=\sigma_z=2az\). In the full535
identity \(\mathcal B_\beta=-\kappa_z f\), the exact cubic coefficients
are
\[
[z^3]f=-2ah/m,\qquad
[z^3]\mathcal B_\beta=-2aa_t.
\]
For example, with \(\nu_F=(h(z+e)+n_s)/m\), the entire expression is
\[
\mathcal B_\beta
=4a^2z^2\left(e_t+\frac{2r+\lambda}{m}\right)
 +2az(e_s+\nu_F-a_tz^2-c_t)-a_sz^2-c_s.
\tag{13}
\]
No coefficient of \(\mathcal B_\beta\) or f above its displayed degree
has been suppressed. Since a,h,m and the multiplier are nonzero,
\[
a_t=-\kappa_z h/m\ne0.
\tag{14}
\]
Now \(h_t=0\) follows from \(m_t=0\), and \(\lambda_t=0\) was proved
from H. Differentiate \(\lambda_s+h_s/(6a)=0\) in t. The result
\(-h_sa_t/(6a^2)=0\) forces \(h_s=0\), and then \(\lambda_s=0\).
The joint constants of L are \(\mathbb C\), so
\[
h\in\mathbb C^*,\quad \lambda\in\mathbb C,\quad
m=hs+\mu\ (\mu\in\mathbb C),\quad
r_t=\frac{h a_t}{4a^2}\ne0.
\tag{15}
\]
In particular r is noncomplex and nonzero. Equation (9) also gives
\[
a=-\frac{h}{4(r+\lambda/2)}\in\mathbb C(r)^*,
\qquad r+\lambda/2\ne0.
\tag{16}
\]
The conclusions allow \(\lambda=0\), \(\mu=0\), and all vanishing lower
coefficients compatible with (1). No rationality of L or of any of its
one-variable constant fields was used.

## 4. The actual three-ring forces dependence of r and nu

Work in the ACTUAL localized polynomial ring
\[
\mathbb K=\mathbb C(X),\qquad
\mathcal R=\mathbb K[Y,Z,W],\qquad
\operatorname{Frac}\mathcal R=L(X)(z).
\tag{17}
\]
Extend N to \(A[u]\) by \(Nu=0\), and put
\(\Delta=a_0N-(NX)E\). It preserves the actual polynomial ring, fixes
X, and is locally nilpotent. For the latter assertion, in
\(A_{a_0}[X]\) it is just a0N with X fixed; \(Na_0=0\), so this is an
LND, and its restriction to the preserved original ring is an LND.
On \(L(X)[z]\) it is \(a_0D\partial_z\), hence nonzero.

The kernel of a nonzero LND on the three-dimensional polynomial ring
\(\mathcal R\) has transcendence degree two over \(\mathbb K\).
One elementary justification is to choose a degree-one local-slice
element by repeated differentiation. After inverting its nonzero
invariant derivative, its quotient by that derivative is a slice;
the fraction field is a one-variable rational extension of the
invariant fraction field. Consequently there exists a nonconstant
polynomial \(F\in\ker_{\mathcal R}\Delta\). As a polynomial in z,
F has degree zero.

Only over \(\mathbb K\), use the invertible triangular coordinate shear
\[
V=Z-Y^2/X^2
 =m(z+e)+n+kX-\frac{2r(az^2+c)}X-\frac{r^2}{X^2}.
\tag{18}
\]
Its inverse is \(Z=V+Y^2/X^2\). This is not asserted to be an ambient
complex polynomial automorphism. The exact intrinsic degrees of
\((Y,V,W)\) are \((2,2,1)\), with initials
\[
Y_{\rm top}=XaT^2,\qquad
V_{\rm top}=-2raT^2/X,\qquad
W_{\rm top}=(X-\nu)T.
\tag{19}
\]
The independent degree variable T is not the original slice. None of
these initials vanishes: r is nonzero by (15), and X is transcendental
over L, so \(X-\nu\ne0\), including when nu is complex.

Suppose r and nu were algebraically independent over \(\mathbb C\).
The field generated by the initials contains
\[
r=-\frac{X^2V_{\rm top}}{2Y_{\rm top}},\qquad
b=\frac{XW_{\rm top}^2}{Y_{\rm top}}=\frac{(X-\nu)^2}{a}.
\tag{20}
\]
By (16), nu is algebraic over \(\mathbb K(r,b)\), since
\((X-\nu)^2=ab\). Thus r,b are independent over \(\mathbb K\).
Also \(Y_{\rm top}\), which has positive T-degree, is transcendental
over the coefficient field. The three initials therefore generate a
field of transcendence degree three and are algebraically independent
over \(\mathbb K\).

But express the nonconstant invariant F above in the actual coordinates
Y,V,W, with positive weights 2,2,1. Its positive highest weighted part
is nonzero. Independence of the initials would make its evaluated
highest intrinsic part nonzero of positive degree, contradicting
\(\deg_z F=0\). This proves that r and nu are algebraically dependent.
Since r is noncomplex, it follows specifically that
\[
\nu\text{ is algebraic over }\mathbb C(r).
\tag{21}
\]
This is not a claim that nu is rational in r.

## 5. The full scalar in the exact (r,m) coefficient basis

Equation (15) gives
\[
\det\frac{\partial(r,m)}{\partial(t,s)}=h r_t\ne0.
\]
Hence r,m are a separating transcendence basis, and L is finite
separable over \(\mathbb C(r,m)\). Extend its commuting exact partials
uniquely to L and then fix z. From (16),(21) and characteristic zero,
\[
\partial_m a=0,\qquad \partial_m\nu=0
\quad\text{at fixed r}.
\tag{22}
\]
For the second assertion, differentiate the separable minimal polynomial
of nu over \(\mathbb C(r)\). No identification of L with a rational
function field, or of an exact constant field with \(\mathbb C(r)\),
is needed.

The combined change from \((t,s,v)\) to \((r,m,z)\) has determinant
\(h r_tD\). Thus the ORIGINAL actual rows, in this coefficient basis,
have scalar
\[
J_{r,m,z}(X)=-\frac{a_0^4}{h r_tD}\in L^*.
\tag{23}
\]
It is independent of both X and z, but not asserted to be a complex
constant. Neither r nor m is made an ambient coordinate.

Set X=0 only in this polynomial scalar. Formula (10) becomes
\[
Y=r,\quad
Z=a^2z^4+2ac z^2+mz+G,\quad
W=-\nu z+w_0,\qquad
G=c^2+me+n+2tr\in L.
\tag{24}
\]
Subscripts m in the rest of the proof mean the NEW exact partial at
fixed r. The first row of the Jacobian is \((1,0,0)\), so the ENTIRE
constant-X scalar is
\[
\begin{aligned}
J_{r,m,z}(0)
&=Z_mW_z-Z_zW_m\\
&=-4a^2(w_0)_m z^3-2a\nu c_m z^2
 -(\nu+4ac(w_0)_m)z-\nu G_m-m(w_0)_m.
\end{aligned}
\tag{25}
\]
All lower functions c,e,n,t,w0, including their moving derivatives,
remain in this identity. In particular no value of its constant
coefficient has been prescribed or discarded.

The nonzero coefficient-field scalar (23) has no positive z-powers.
Since \(a\ne0\), the z3 coefficient gives \((w_0)_m=0\). Its z1
coefficient is then \(-\nu\), contradicting \(\nu\ne0\).
Even the z2 equation is unnecessary. This finishes the exclusion.

## 6. Verification and scope

The held539 dependency was read completely through EOF before this
source was authored. Its exact actual normalization and the original
selected-N, full-initial-kernel, return and scalar licenses are retained.
The branch gates were nevertheless reconstructed in the original
theta-based parameter in Sections2--3.

Fresh unsaved72a758 rebuilt the full original second potential and
formal H/H_U, the cubic cleared-multiplier gate, the entire localized
shear, all three initials and the complete constant-X determinant with
arbitrary lower jets. Every residual was zero. Fresh012ba6 independently
checked the unrestricted original-field H4/H3 coefficients and all
three transported literal rows of the actual normalization. No saved
checker was executed, imported, compiled or rerun.

The argument excludes exactly the C0=0, nu0-nonzero branch of539 under
the retained full actual hypotheses. It neither assumes that the
original sigma leader is a square nor obtains a contradiction from a
square visible only after a coefficient extension. It uses an actual
localized three-ring for initial independence and only an exact
coefficient basis for the final scalar.

The other midpoint branch, general nonlinear-sigma recognition,
arbitrary chart entry, unrestricted cancellation, novelty and external
certification are not conclusions here. No earlier source or canonical
file was edited. Complete independent saved-source review remains a
separate step.
