# Equal degree one: the zero characteristic coefficient with nonconstant slope is excluded

Working exclusion inside the full actual264 chart. Retain the
degree-one presentation and high equations of401. This note treats
only the branch delta=lambda-n_s nonzero, lambda noncomplex, and
Dscript(mu)+4lambda=0. A legitimate coefficient basis gives exact
quadratic t integrations. The remaining full scalar equations then
force the entire calibrated determinant to vanish.

The proof retains every zero value of its later complex constants.
It does not impose a rationality ansatz on the coefficient field,
promote a field parameter to an ambient coordinate, or use the
strict-degree rank condition from385/387.

## 1. Actual input and the precisely selected branch

Retain every actual hypothesis and both genuine-potential levels in
[401](principal-paraboloid-equal-degree-one-delta-zero-necessary-family-pass401-working.md),
and hence the supplied actual
[264](principal-one-affine-paraboloid-chart-pass264-working.md)
entry. In particular,
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A_0[u],\qquad E=\partial_u,\qquad
\deg_E(X,Y,Z,W)=(1,2,2,2),\qquad a_0=EX\ne0,\\
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2),\qquad
0\ne N=[u^4]\partial_Z|_{A_0},\\
L=\operatorname{Frac}\ker_{A_0}N,\qquad
[L:\mathbb C(t,s)]<\infty,\qquad k=s,\qquad n_{ss}\ne0,\\
O=L[P],\quad P=\sigma,\quad \rho=NP\in L^*,\qquad
\operatorname{Frac}A_0=L(P)=\mathbb C(y,z,w).
\end{gathered}
\tag{1}
\]
The intrinsic presentation is
\[
y=\lambda P+r,\qquad \theta=\mu P+h,\qquad
\lambda,r,h\in L,\quad \mu\in L^*.
\tag{2}
\]
The intrinsic functions sigma and theta both have degree one.
Both whole polynomial returns, the strong complex-field return,
the original global slice, full initial kernel and literal selected
derivation remain required. None is replaced by an abstract curve.

Use the exact commuting coefficient partials in t,s, with joint
constant field C. Set
\[
\nu=n_s,\quad a=n_t,\quad b=n_{ts},\quad e=n_{ss}\ne0,\quad
\delta=\lambda-\nu,\qquad
\mathscr D=\partial_t+\mu\partial_s,
\tag{3}
\]
and write alpha=Dscript(lambda), beta=Dscript(nu) and
kappa=Dscript(mu). The high equations from401 include
\[
\begin{gathered}
n_{tt}+2\mu n_{ts}+\mu^2n_{ss}=4\nu\lambda-2\lambda^2,\\
2\delta\alpha+\beta(\kappa+4\lambda)=0.
\end{gathered}
\tag{4}
\]
The branch studied here is exactly
\[
\boxed{\delta\ne0,\qquad \lambda\notin\mathbb C,\qquad
             \kappa+4\lambda=0.}
\tag{5}
\]
In particular lambda is nonzero. No assertion about the
kappa+4lambda nonzero branch or a complex constant lambda is made
here. This is a specified branch of the full degree-one system,
and the other branches remain outside the present conclusion.

Equation (4) gives Dscript(lambda)=0. The full literal rows are
\[
\begin{aligned}
Y&=(X+\lambda)P+r+tX^2,\\
Z&=P^2+(2t\lambda+\mu+2tX)P+2tr+h+n+sX+t^2X^2,\\
W&=-2\lambda P^2+(\mu X-2r-a-\nu\mu)P
                    +\ell-\nu h+hX+sX^2.
\end{aligned}
\tag{6}
\]
Their required scalar is
\[
J=\det\frac{\partial(Y,Z,W)}{\partial(t,s,P)}
       =-a_0^4/\rho\in L^*,
\tag{7}
\]
independent of X and P. All determinant calculations below use
these complete rows, not just high homogeneous terms of a level.

## 2. A separating coefficient basis and exact integrations

Put xi=lambda. Then lambda_s is nonzero: otherwise Dscript(lambda)=0
would also give lambda_t=0, contrary to (5). Consequently t,xi
are algebraically independent and L is finite over C(t,xi).
For example, if xi were algebraic over C(t), applying partial_s
to its separable minimal polynomial would force lambda_s=0.

On L define
\[
\dot f=\mathscr D f,\qquad
f'=\lambda_s^{-1}\partial_s f,\qquad
\mathcal F=\ker_L\dot{\ },\qquad
\dot t=1,\ \dot\xi=0,\ t'=0,\ \xi'=1.
\tag{8}
\]
These are the unique extensions of the coordinate partials for
C(t,xi), so they commute. Their joint constants remain C.
The field F is stable under primes, and t is transcendental over F.
No equality F=C(xi) or L=F(t) is assumed.

Since dot mu=-4xi and dot s=mu, exact integrations inside L give
zeta,S0 in F with
\[
\mu=\zeta-4\xi t,\qquad s=-2\xi t^2+\zeta t+S_0.
\tag{9}
\]
Here S0 is an integration coefficient, not the original chart
function k, which remains s. Also
\[
\begin{aligned}
\dot n&=a+\mu\nu,\\
\ddot n
 &=n_{tt}+2\mu n_{ts}+\mu^2n_{ss}+\kappa\nu
   =-2\xi^2.
\end{aligned}
\tag{10}
\]
Thus there are A,B in F such that
\[
\boxed{n=-\xi^2t^2+At+B.}
\tag{11}
\]
For example A=dot n+2xi^2*t has zero dot derivative, and then
B=n+xi^2*t^2-A*t does as well. These integrations do not assume
that all elements of L are rational in t over F.

Set
\[
\begin{gathered}
d=s'=-2t^2+\zeta't+S_0'=1/\lambda_s\ne0,\\
\mathfrak u=\xi\zeta'-A'\in\mathcal F,\qquad
\mathfrak v=\xi S_0'-B'\in\mathcal F.
\end{gathered}
\tag{12}
\]
At fixed t, n'=nu*s'. Hence
\[
\nu=\frac{-2\xi t^2+A't+B'}d,\qquad
\delta=\frac{\mathfrak u t+\mathfrak v}d.
\tag{13}
\]
In particular ufrak and vfrak cannot both be zero.
The symbol ufrak is not the original slice u.

## 3. Full moving-parameter rows and calibrated determinant

Introduce only coefficient-field and intrinsic changes:
\[
\begin{aligned}
q&=P+t(X-\xi)+\zeta/2,\\
G&=r+\xi^2t,\\
H&=h+2tG-4\xi^2t^2+(A+\xi\zeta)t+B-\zeta^2/4,\\
V&=\ell-\nu h-\xi t(A+2G)+2\xi^3t^2
                      +A\zeta/2+G\zeta-\xi\zeta^2/2.
\end{aligned}
\tag{14}
\]
The element V here is a coefficient function in L, not the
intrinsic theta or an ambient coordinate. At fixed actual X the
change from P to q is affine over L. It is not asserted to be
a polynomial transformation of the original four-ring.

Substitution in (6), with a=dot n-mu*nu, gives the exact rows
\[
\boxed{
\begin{aligned}
Y={}&(X+\xi)q+G-\zeta(X+\xi)/2,\\
Z={}&q^2+S_0X+H,\\
W={}&-2\xi q^2+(\zeta X-A-2G+2\xi\zeta)q
          +S_0X^2+(H-B-\zeta^2/4)X+V.
\end{aligned}}
\tag{15}
\]
No coefficient derivative or explicit X term has been discarded.
The parameter Jacobian at fixed X is
\[
\det\frac{\partial(t,s,P)}{\partial(t,\xi,q)}=d.
\]
Consequently the full new determinant satisfies
\[
\widehat J
=\det\frac{\partial(Y,Z,W)}{\partial(t,\xi,q)}
=dJ=-d a_0^4/\rho\in L^*.
\tag{16}
\]
Dots and primes in this determinant fix q and X. In particular
the required determinant remains independent of both X and q.
The actual degree-one X is transcendental over Frac A0, since
X=a0*u+b0 with b0 in A0 and a0 nonzero. Thus X,P, and equivalently
X,q, are algebraically independent over L. The polynomial
coefficient comparisons are legitimate.

For a complete differentiation ledger, the first two rows are
\[
\begin{pmatrix}
\dot G&
 q-\zeta/2-(X+\xi)\zeta'/2+G'&X+\xi\\
\dot H&H'+S_0'X&2q
\end{pmatrix},
\]
and the third row is
\[
\begin{aligned}
W_t={}&-2\dot Gq+\dot HX+\dot V,\\
W_\xi={}&-2q^2+(\zeta'X-A'-2G'+2\zeta+2\xi\zeta')q\\
 &\quad+S_0'X^2+(H'-B'-\zeta\zeta'/2)X+V',\\
W_q={}&-4\xi q+\zeta X-A-2G+2\xi\zeta.
\end{aligned}
\tag{17}
\]
The determinant has support contained in X^2,Xq,X,q^2,q,1.

## 4. Nonzero gates and the first lower-coefficient integrations

The q^2 coefficient of (17) is
\[
[q^2]\widehat J
 =2[-(\mathfrak u+\zeta)\dot G+\xi\dot H+\dot V].
\]
Its required vanishing gives
\[
\dot V=(\mathfrak u+\zeta)\dot G-\xi\dot H.
\tag{18}
\]
After this substitution the Xq and X^2 coefficients respectively
give
\[
\begin{gathered}
\mathfrak u\dot H-(2\mathfrak v+\mathfrak u\zeta')\dot G=0,\\
\mathfrak v\dot H-\mathfrak u S_0'\dot G=0.
\end{gathered}
\tag{19}
\]
These equations involve no division by ufrak, vfrak or dot G yet.

If dot G=0, equations (19), together with the fact that ufrak and
vfrak are not both zero, force dot H=0. Equation (18) then gives
dot V=0. The entire t column of (17) vanishes, contradicting (16).
Thus dot G is nonzero. If ufrak=0, the first equation of (19)
now forces vfrak=0, again a contradiction. We have proved
\[
\boxed{\dot G\ne0,\qquad \mathfrak u\ne0.}
\tag{20}
\]
The value vfrak=0 remains allowed.

It is now legitimate to put
\[
\omega=\mathfrak v/\mathfrak u\in\mathcal F,\qquad
j=\zeta'+2\omega\in\mathcal F.
\]
Equations (18),(19) give, without dividing by omega or j,
\[
S_0'=\omega j,\qquad
\dot H=j\dot G,\qquad
\dot V=(\zeta-A'-2\xi\omega)\dot G.
\tag{21}
\]
Their exact integrations define H0,V0 in F:
\[
\boxed{H=jG+H_0,\qquad
V=(\zeta-A'-2\xi\omega)G+V_0.}
\tag{22}
\]
Also G is transcendental over F. If it were algebraic, its
separable minimal polynomial over F would imply dot G=0.

## 5. Coefficient comparison forces complex constants

Insert (22) into the complete determinant (17). The part of the
xi column proportional to G' is G'/dot G times the t column, so
it can be subtracted without changing the determinant. Every G'
term therefore cancels. After dividing by the proved nonzero dot G, the result
is a polynomial in X,q,G with coefficients in F. Put
\[
D_1=\mathfrak u'-(\zeta'+4\omega)
                =\mathfrak u'-(j+2\omega).
\]
The coefficients of qG and XG in that polynomial are, respectively,
\[
[qG](\widehat J/\dot G)=-2D_1,\qquad
[XG](\widehat J/\dot G)=jD_1-\mathfrak u j'.
\tag{23}
\]
The scalar condition first makes the full q and X coefficients
zero. Since G is transcendental over F, their G coefficients in
(23) are zero. Using (20) gives
\[
\mathfrak u'=\zeta'+4\omega,\qquad j'=0.
\]
The element j lies in F and has zero prime derivative, so the exact
joint-constant property yields j=c in C, including c=0. Since
zeta'=c-2omega, one has (ufrak+zeta)'=2c. Thus
\[
\mathfrak u+\zeta=2c\xi+c_0,\qquad c_0\in\mathbb C.
\]
Integrating the definitions in (12) and (21) now gives
\[
\boxed{
\begin{aligned}
\mathfrak u&=2c\xi+c_0-\zeta\ne0,\\
A&=\xi\zeta-c\xi^2-c_0\xi+a_c,\\
S_0&=c^2\xi/2-c\zeta/2+s_c,\\
B&=-(\zeta-c\xi-c_0)^2/4+b_c,
\end{aligned}
\qquad a_c,s_c,b_c\in\mathbb C.}
\tag{24}
\]
For clarity, A'=xi*zeta'-ufrak is the derivative of the displayed A.
Also S0'=omega*c and
B'=xi*S0'-omega*ufrak=omega*(zeta-c*xi-c0).
The last expression is the derivative of the displayed B because
(zeta-c*xi-c0)'=-2omega. Each integration constant belongs to F
and has zero prime derivative, hence belongs to C. No rationality
of zeta in xi and no nonzero condition on c,c0,ac,sc,bc is imposed.

Equations (22) simplify to
\[
H=cG+H_0,\qquad V=(c\xi+c_0)G+V_0.
\tag{25}
\]

## 6. The corrected complete scalar vanishes

Define the two remaining derivative errors, both elements of F,
by
\[
\begin{aligned}
D_H&=H_0'-\frac{c^2\xi-c\xi\zeta'-c\zeta}{2},\\
D_V&=V_0'-\frac{a_c c-
                   [(c\xi^2+c_0\xi)\zeta]'}2.
\end{aligned}
\tag{26}
\]
Substitute (24),(25) into the full differentiated rows (17),
retaining arbitrary G' and dot G. The complete determinant is
\[
\boxed{
\frac{\widehat J}{\dot G}
=X[(c\xi-\mathfrak u)D_H+cD_V]
 -2q[\xi D_H+D_V]
 +(-2G+\xi\zeta-a_c)D_H+c\xi D_V.
}
\tag{27}
\]
In particular the constant DH coefficient is
(-2G+xi*zeta-ac), not an expression obtained by replacing xi*zeta
with c*xi^2+c0*xi. Equation (27) includes every remaining scalar
coefficient, not only its X and q terms.

The q coefficient required by (16) gives DV=-xi*DH. The X
coefficient then becomes -ufrak*DH. By the proved ufrak nonzero
gate in (20), DH=0 and hence DV=0. The right side of (27) is
therefore identically zero. This contradicts the nonzero calibrated
scalar in (16) and proves the claimed exclusion.

No division by c, omega, zeta', H0' or V0' occurred. In particular
c=0 and vfrak=0 are fully retained. This proof also does not need
to identify the original invariant ring with any coefficient-field
extension or its normalization.

## 7. Optional separate integrated cross-check

This section is not needed for the contradiction from (27).
The equations DH=DV=0 can also be integrated exactly in F:
\[
H_0=c^2\xi^2/4-c\xi\zeta/2+h_c,\qquad
V_0=a_c c\xi/2-(c\xi^2+c_0\xi)\zeta/2+v_c,
\quad h_c,v_c\in\mathbb C.
\tag{28}
\]
Define T=q-c(X+xi)/2 as an element of the original fraction field.
Eliminate G using Y in (15). Direct substitution of (24),(25),(28)
then gives
\[
\begin{aligned}
Z={}&T^2-c^2X^2/4+s_cX+cY+h_c,\\
W={}&2XT^2+cX^2T-c_0XT-2YT-a_cT\\
 &+(s_c-cc_0/2)X^2+
       (h_c-a_c c/2-b_c+c_0^2/4)X+c_0Y+v_c.
\end{aligned}
\tag{29}
\]
All displayed coefficients are complex. Thus these necessary
identities would place the original four algebraically independent
coordinates in C[X,Y,T], a field-subring of transcendence degree
at most three. That is another contradiction. It does not assert
that T is polynomial in the original ring or is an ambient
coordinate; its fraction-field membership suffices for this
transcendence-degree comparison.

## 8. Scope and verification record

The excluded branch is (5), within the full actual degree-one
presentation of401. The proof keeps the precise coefficient field,
both actual returns and all original chart gates. It uses the high
equations and the complete calibrated scalar; it does not claim
that arbitrary formal solutions of a quadric admit the actual
entry. Complex constant lambda and nonzero kappa+4lambda remain
outside this note. No arbitrary entry theorem, unrestricted
cancellation conclusion or classification of all equal degrees
is asserted.

The complete held401 source was read through EOF in
d1317b+d7a30a before this derivation. Fresh unsaved90729f rebuilt
the moving literal rows. Fresh dc3bc1 and d6f6fe computed the
initial and intermediate scalar coefficients. Fresh38b59c checked
the final lower elimination, and 785724 checked the separate
integrated identities (29). A new independent literal reconstruction
a0ccdf retained arbitrary coefficient functions and checked all
three rows (15), the Jacobian d, and (18),(19), with zero residuals.

A separate full-matrix check02887e caught a transcription error
in the constant DH coefficient of an outline sent before this note
was saved. It was corrected to the coefficient in (27). Fresh
unsaved1b44e9 retained arbitrary G', dot G, H0 and V0 and checked
the complete corrected identity (27), with residual zero.
The X and q coefficient exhaustion was unaffected by that correction.

These finite symbolic identities support but do not replace the
written exact-field, nonzero-gate and coefficient-comparison
arguments. No saved checker was executed, imported, compiled or
rerun. No held earlier source or canonical index was edited.
Independent full saved-source review is still required. There is
no claim of novelty, human-expert review or formal certification.
