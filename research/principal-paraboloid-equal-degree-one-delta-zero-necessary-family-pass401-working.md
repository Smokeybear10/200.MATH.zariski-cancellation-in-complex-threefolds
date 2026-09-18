# Equal intrinsic degree one: high equations and a Delta-zero necessary family

Working necessary reduction in the complete actual264 chart with
k=s and n_ss nonzero. When sigma and theta both have intrinsic
degree one, the high genuine-potential and scalar equations give
the exact system below. In the subcase where the y/sigma slope
equals n_s, the full scalar further forces a coefficient family
with B''=(A'')^2/8 and the explicit nonzero scalar (32).

The remaining scalar is not proved zero. This is not an exclusion,
an actual realization, or recognition of an original coordinate.
The exact coefficient-field changes below are not promoted to
polynomial changes of the original four coordinates.

## 1. Full actual input, degree-one presentation and derivative conventions

Retain every actual hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md)
and the complete genuine levels in
[365](principal-paraboloid-nonlinear-intercept-unequal-degree-gate-pass365-working.md).
In particular,
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A_0[u],\quad E=\partial_u,\quad
\deg_E(X,Y,Z,W)=(1,2,2,2),\quad a_0=EX\ne0,\\
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2),\quad
0\ne N=[u^4]\partial_Z|_{A_0},\quad
L=\operatorname{Frac}\ker_{A_0}N,\\
[L:\mathbb C(t,s)]<\infty,\quad Nv=1,\quad
O=L[v]=L[y,\sigma,\theta]=L[y,z,w],\\
K=\operatorname{Frac}A_0=L(v)=\mathbb C(y,z,w),\qquad k=s.
\end{gathered}
\tag{1}
\]
The full initial kernel, literal selected partial, original global
slice, whole polynomial return and strong complex-field return are
retained, not replaced by an abstract parametrized line.

Assume deg_v sigma=deg_v theta=1. The monic-y third relation bounds
deg_v y by one. Use the affine intrinsic parameter P=sigma, giving
\[
O=L[P],\quad \rho=NP\in L^*,\qquad
y=\lambda P+r,\quad\theta=\mu P+h,
\quad\lambda,r,h\in L,\quad\mu\in L^*.
\tag{2}
\]
The slope lambda is allowed to be zero. All coefficient derivatives
on L are the exact commuting extensions of partial_t,partial_s;
they have joint constants C. Extend them to fix P and the actual X.
The moving intrinsic parameter has calibrated determinant
\[
J(X)=\det\frac{\partial(Y,Z,W)}{\partial(t,s,P)}
      =-a_0^4/\rho\in L^*.
\tag{3}
\]
No strict-degree conclusion or nonzero rank coefficient from385/387
is assumed in this equal-degree case.

Write
\[
a=n_t,\quad \nu=n_s,\quad c=n_{tt},\quad b=n_{ts},
\quad e=n_{ss}\ne0,\quad C=\ell_s+\nu^2,\quad
\delta=\lambda-\nu,\quad g=2r+a.
\tag{4}
\]
The letter a is not a0. Since nu_s=e is nonzero, nu is nonzero.
The letter h is the constant term of theta, not a potential level.

The complete actual rows are
\[
\begin{aligned}
Y&=(X+\lambda)P+r+tX^2,\\
Z&=P^2+(2t\lambda+\mu+2tX)P+2tr+h+n+sX+t^2X^2,\\
W&=-2\lambda P^2+(\mu X-g-\nu\mu)P
                         +\ell-\nu h+hX+sX^2.
\end{aligned}
\tag{5}
\]
They follow from z=2ty+P^2+theta+n and
w=ell-2Py-aP-nu*theta. All later scalar calculations use these
literal rows, not only the third surface equation.

## 2. High genuine-potential equations with no slope division

For independent formal U,P,V, the complete third potential is
\[
H=U^2+(a-2\nu P)U+\tfrac c2P^2+bPV+\tfrac e2V^2
       -(\ell_t+\nu a)P-CV+\nu\ell.
\tag{6}
\]
Its evaluation at (lambda*P+r,P,mu*P+h) is constant. The quadratic,
linear and constant coefficients respectively give
\[
\begin{gathered}
\lambda^2-2\nu\lambda+c/2+b\mu+e\mu^2/2=0,\\
\ell_t=\delta g+(b+e\mu)h-\mu C,\\
h_0=r^2+ar+\tfrac e2h^2-Ch+\nu\ell.
\end{gathered}
\tag{7}
\]
In particular h0 is an exact coefficient function. Its derivatives
cannot be treated as independent free constants.

The full fourth polynomial is
\[
\begin{aligned}
Q={}&[(c+2\ell_s)P+bV-2bP^2-2ePV-\ell_t]U\\
&+\tfrac16n_{ttt}P^3+\tfrac12n_{tts}P^2V
  +\tfrac12n_{tss}PV^2+\tfrac16n_{sss}V^3\\
&-\tfrac12(\ell_{tt}+2ba)P^2
  -(\ell_{ts}+\nu b+ea)PV-\tfrac12(\ell_{ss}+2\nu e)V^2\\
&+(b\ell+a\ell_s-(h_0)_t)P
  +(e\ell+\nu\ell_s-(h_0)_s)V.
\end{aligned}
\tag{8}
\]
It too evaluates to a coefficient constant. Its highest coefficient
is the exact equation
\[
n_{ttt}+3\mu n_{tts}+3\mu^2n_{tss}+\mu^3n_{sss}
          =12\lambda(b+e\mu).
\tag{9}
\]
For completeness, its quadratic coefficient is
\[
\begin{aligned}
0={}&\lambda(c+2\ell_s+b\mu-2eh)-2(b+e\mu)r\\
&+\tfrac h2(n_{tts}+2\mu n_{tss}+\mu^2n_{sss})
 -\tfrac12(\ell_{tt}+2ba)\\
&-\mu(\ell_{ts}+\nu b+ea)
 -\tfrac{\mu^2}{2}(\ell_{ss}+2\nu e).
\end{aligned}
\tag{10}
\]
The remaining linear coefficient still contains both derivatives
of h0 from (7). The argument below does not set either to zero.
The high equations (7),(9),(10) divide by neither lambda nor delta.

## 3. A compact high-scalar system

Define an operator and coefficient elements by
\[
\mathscr D=\partial_t+\mu\partial_s,\qquad
\beta=b+e\mu=\mathscr D\nu,\qquad
\alpha=\mathscr D\lambda,\qquad
\kappa=\mathscr D\mu.
\tag{11}
\]
At this stage this is only a coefficient-field derivation, not an
actual locally nilpotent derivation or a commuting coordinate partial.

Here is a complete row ledger for the scalar computation. In the
differential rows of (5), first replace the second row by dZ-2t*dY,
and then the third row by dW+2P*dY+nu*(dZ-2t*dY). These determinant-
preserving operations give, in columns t,s,P,
\[
\begin{pmatrix}
\lambda_tP+r_t+X^2&\lambda_sP+r_s&X+\lambda\\
(2\lambda+\mu_t+2X)P+g+h_t&\mu_sP+h_s+\nu+X&2P+\mu\\
T_3&S_3&2(X-\delta)P+\mu X-g
\end{pmatrix},
\tag{12}
\]
where
\[
\begin{aligned}
T_3={}&(-c-b\mu+2\nu\lambda+2X^2+2\nu X+X\mu_t)P
                  +\ell_t-bh+\nu g+Xh_t,\\
S_3={}&(-b-e\mu+X\mu_s)P+C-eh+X^2+\nu X+Xh_s.
\end{aligned}
\tag{13}
\]
Row multipliers are multiplied into differentials; they are not
themselves differentiated. Direct determinant expansion has support
contained in X^2P,X^2,XP^2,XP,X,P^3,P^2,P,1. Its first two coefficients
are c+2b*mu+e*mu^2+2lambda^2-4lambda*nu and
delta*g+(b+e*mu)h-mu*C-ell_t, which vanish by (7).
After these vanish,
\[
\begin{aligned}
[XP^2]J&=-\{2\delta\alpha+\beta(\kappa+4\lambda)\},\\
[P^3]J&=2\{(\beta-\delta\mu_s)\alpha
                    +\delta(\kappa+4\lambda)\lambda_s\}.
\end{aligned}
\tag{14}
\]
Both expressions must vanish by (3). These formulas preserve every
zero slope. For example lambda=0 gives only beta*kappa=0 at this
stage, not permission to divide by either factor.

There is a consistency check on the first equation in (14).
Apply Dscript to the first equation of (7), keeping the derivatives
of mu. The result is
2delta*alpha-2lambda*beta+beta*kappa plus one half of the
third-order tensor on the left of (9). Substitution of (9) gives
exactly 2delta*alpha+beta*(kappa+4lambda)=0. Thus this scalar equation
agrees with the differentiated genuine-potential equations.

## 4. Delta zero: legitimate coefficient basis and exact integrations

Assume from now on only the subcase
\[
\delta=0,\qquad\lambda=\nu\ne0.
\tag{15}
\]
Then alpha=beta, and the second coefficient in (14) becomes 2beta^2.
Consequently
\[
\beta=0,\qquad \mu=-b/e,\qquad
c=2\nu^2+b^2/e.
\tag{16}
\]
No division by delta was used. Division by e is allowed by (4).

Put xi=nu. Because partial_s nu=e is nonzero, t,xi are algebraically
independent and form a separating coefficient basis: if xi were
algebraic over C(t), differentiation of its separable minimal
polynomial in s would force e=0. The finitely generated field L is
therefore finite over C(t,xi). On L define
\[
\dot f=(\partial_t+\mu\partial_s)f,\qquad
f'=e^{-1}\partial_sf,\qquad
\mathcal F=\ker_L(\dot{\ }),
\quad\dot t=1,\quad\dot\xi=0,\quad t'=0,\quad\xi'=1.
\tag{17}
\]
These are the unique extensions of the two coordinate partials for
C(t,xi), so they commute. Their joint constants are still C.
Primes below mean this xi derivative at fixed t, not old partial_s.
The field F is stable under primes and t is transcendental over F.
No equality F=C(xi) or L=F(t) is assumed.

Take the Legendre coefficient f_leg=n-xi*s. From (16),
\[
\dot f_{\rm leg}=a,\qquad f_{\rm leg}'=-s,\qquad
\dot a=c+\mu b=2\xi^2.
\tag{18}
\]
For example dot n=a+mu*xi and dot s=mu give the first identity;
n'=xi/e and s'=1/e give the second. Exact integration inside L
therefore defines A,B in F with
\[
\begin{aligned}
f_{\rm leg}&=\xi^2t^2+At+B,\\
s&=-2\xi t^2-A't-B',\qquad
\mu=-4\xi t-A',\\
n&=-\xi^2t^2+(A-\xi A')t+B-\xi B',\qquad
a=2\xi^2t+A.
\end{aligned}
\tag{19}
\]
For instance A=a-2xi^2*t has zero dot derivative; subtracting its
linear term from f_leg similarly defines B. This is not a rational
ansatz for the coefficient field. It also gives
\[
D:=s'=-2t^2-A''t-B''=1/e\ne0,
\qquad\dot\mu=-4\xi.
\tag{20}
\]
The letter D in (20) is an element, not the operator Dscript.

The second equation of (7), now with delta=beta=0, says
ell_t=-mu*(ell_s+xi^2). Hence dot ell=-mu*xi^2. Integrating with
(19) gives another element Lambda of F such that
\[
\ell=2\xi^3t^2+\xi^2A't+\Lambda.
\tag{21}
\]
The constant of this integration belongs to the exact field F;
it is not asserted to be complex.

## 5. The complete Delta-zero scalar and its nonzero gates

Continue to use g=2r+a and introduce
\[
\begin{gathered}
H_b=h-4\xi^2t^2-2\xi A't-\Lambda'+\xi^2B'',\\
K=C-eh=-eH_b,\qquad
T_0=\dot r+\xi^2=\dot g/2,\qquad
L_0=\dot h+g+2\mu\xi=\dot H_b+g.
\end{gathered}
\tag{22}
\]
To check K=-e*Hb, differentiate (21) in xi and use ell_s=e*ell'.
The difference ell'-h is -xi^2*D-Hb, which gives the identity.
The other two identities follow from (19). No derivative of r or h
has been assumed zero.

Changing coefficient columns from (t,s) to (t,xi) multiplies the
scalar by D=s'. Thus
\[
\widehat J(X)=\det\frac{\partial(Y,Z,W)}{\partial(t,\xi,P)}
             =D J(X)=-D a_0^4/\rho\in L^*.
\tag{23}
\]
Use (19),(21),(22) in the literal rows (5). Equivalently, substitute
them in the row matrix (12). The entire determinant is
\[
\begin{aligned}
\widehat J(X)&=J_X X+J_P P+J_0,\\
J_X&=-H_bL_0-DgT_0,\\
J_P&=gL_0+(2H_b-g\dot D)T_0,\\
J_0&=(-\xi H_b+g r')L_0
          -(-\mu H_b+g h'+\xi Dg)T_0.
\end{aligned}
\tag{24}
\]
In particular all higher X and P coefficients cancel; (24) is not
only a selection of highest coefficients. Formula (23) requires
J_X=J_P=0 and J0 nonzero.

Every division in the next step needs a nonzero gate. If g=0 as a
field element, then T0=dot g/2=0. Equation J_X=0 gives Hb*L0=0,
and (24) makes J0=-xi*Hb*L0=0, a contradiction. Hence g is nonzero.
If L0=0, J_X=0 and nonzero D,g imply T0=0, again making J0=0.
If T0=0, J_P=0 and nonzero g imply L0=0. Finally if Hb=0,
J_X=0 forces T0=0. We have proved
\[
\boxed{g\ne0,\quad L_0\ne0,\quad T_0\ne0,
\quad\dot g\ne0,\quad H_b\ne0.}
\tag{25}
\]
Eliminate L0 between J_X=J_P=0 and use T0 nonzero. The result is
\[
Dg^2-2H_b^2+gH_b\dot D=0.
\tag{26}
\]
Set zeta=Hb/g and omega=zeta+t. Both are coefficient-field elements;
zeta is nonzero by (25). Equation (26) is equivalent to
\[
2\zeta^2-\dot D\zeta-D=0,
\qquad 2\omega^2+A''\omega+B''=0.
\tag{27}
\]
The second equality uses the full quadratic D in (20). Its
coefficients are in F, so omega is algebraic over F. In
characteristic zero its separable minimal polynomial over F shows
dot omega=0, including a repeated-root case of the displayed
quadratic. Thus omega belongs to F by its definition; no rationality
of omega was presumed and no root was adjoined.

Now Hb=g*(omega-t), so L0=dot g*zeta. Substitution into J_X=0,
followed by division only by the nonzero g*dot g, gives D=-2zeta^2.
Equation (27), using zeta nonzero, then gives dot D=4zeta.
Comparing with dot D=-4t-A'' and zeta=omega-t proves
\[
\boxed{\omega=-A''/4,\qquad
H_b=-g(t+A''/4),\qquad B''=(A'')^2/8.}
\tag{28}
\]
The last equation follows by comparing constant terms in
D=-2(t+A''/4)^2. This is valid because t is transcendental over F.
No division by A'', A''' or B'' occurs. Their zero values are retained.

## 6. Necessary family and the still nonzero scalar

The resulting coefficient data have the following explicit form,
with A,B,Lambda in the exact field F and g in L:
\[
\begin{gathered}
s=-2\xi t^2-A't-B',\quad B''=(A'')^2/8,
\quad e=-\frac1{2(t+A''/4)^2},\\
\lambda=\xi,\quad\mu=-4\xi t-A',\qquad
n=-\xi^2t^2+(A-\xi A')t+B-\xi B',\\
\ell=2\xi^3t^2+\xi^2A't+\Lambda,\qquad
r=g/2-\xi^2t-A/2,\\
h=-g(t+A''/4)+4\xi^2t^2+2\xi A't
                         +\Lambda'-\xi^2(A'')^2/8,\\
y=\xi P+r,\qquad\theta=(-4\xi t-A')P+h.
\end{gathered}
\tag{29}
\]
The denominators are nonzero: e was nonzero, and the displayed
t+A''/4 is nonzero because t is transcendental over F. Also xi is
nonzero by (4), so mu is nonzero, as required by degree one.

For an explicit verification of the last scalar, before replacing
B'' write Q0=Lambda'-xi^2*B'' and w0=-A''/4. Then
Hb=g*(w0-t), dot g nonzero, and (24) simplifies to
\[
\widehat J=-\frac{g\dot g}{2}
                   (g w_0'+Q_0'+2A'w_0).
\tag{30}
\]
One can check this directly in (24) using
r'=g'/2-2xi*t-A'/2 and the derivative of
h=g*(w0-t)+4xi^2*t^2+2xi*A'*t+Q0.
The g' terms cancel. The t terms cancel by 4w0=-A''.
Differentiate B''=(A'')^2/8 to get B'''=A''A'''/4. Then
\[
g w_0'+Q_0'+2A'w_0
=\Lambda''-\frac{\xi(A'')^2}{4}
 -\frac{\xi^2A''A'''}4-\frac{gA'''}4-\frac{A'A''}{2}.
\tag{31}
\]
Consequently the complete scalar, not only a highest coefficient, is
\[
\boxed{
\widehat J=
\frac{g\dot g}{8}
\left[A'''(g+\xi^2A'')+2A'A''+\xi(A'')^2-4\Lambda''\right]
=-D a_0^4/\rho\ne0.
}
\tag{32}
\]
Thus the bracket in (32) is an additional required nonzero field
element. This formula supplies no contradiction by itself.

## 7. Exact scope, remaining gap and verification record

Equations (7)--(14) are necessary high equations for all degree-one
equal profiles, retaining lambda=0 and delta=0. Equations (19),
(21),(25),(28),(29),(32) are the further necessary reduction only
for delta=0. The delta-nonzero sector has not been classified here.

All transformations after (15) are changes of coefficient-field
basis or field elements. None changes the actual coordinates
X,Y,Z,W. In particular P,xi,g and the formal completed square
P+tX+t*lambda+mu/2 have not been shown to be original coordinates.
No claim L=F(t), F=C(xi), or polynomiality of g over F[t] is made.

The actual returns K=C(y,z,w), O=L[P], original global slice and
selected literal derivation remain required. The displayed necessary
family has not been proved compatible or incompatible with all those
original-ring conditions. Equation (32) still has a potentially
nonzero scalar. Resolving that actual-return or coordinate-entry gap
requires an additional argument; setting the scalar to zero would
not be justified by the calculations in this note.

The complete264 and365 sources were read directly in211a1d and7aca1b.
Fresh unsaved3a6597 rebuilt the original full determinant, its exact
support and high coefficients. Fresh bf0517 independently checked
the row-reduced determinant and directional forms. Fresh876672
rebuilt the complete scalar in the (t,xi,P) basis, verified all of
(24), and checked the quadratic change in (27). Fresh76f19e then
verified the entire determinant after (28) equals (32), with zero
residual. These were inline symbolic reconstructions, not saved
checker executions, and do not certify the original-ring arguments.

Applicable local instructions and the writing guide were read in
558ba6 before this source was authored. No saved checker was
executed, imported, compiled or rerun. No earlier source, canonical
README or ledger was edited. This is a bounded necessary reduction,
not an exclusion, actual-realization theorem, cancellation result,
novelty claim, human-expert review or formal certification.

