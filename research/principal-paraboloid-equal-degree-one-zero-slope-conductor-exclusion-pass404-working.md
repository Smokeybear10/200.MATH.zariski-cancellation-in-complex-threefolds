# Equal intrinsic degree one: exclusion of the zero y-slope

Working exclusion in the complete actual264 chart with k=s and
n_ss nonzero. Suppose sigma and theta both have intrinsic degree
one and y belongs to the coefficient field. The exact scalar
forces a coefficient presentation whose original-coordinate ring
has an explicitly computed conductor in a polynomial overring.
The original derivation preserves both rings, contradicting the
computed conductor.

This note treats only lambda=0. It does not normalize a nonzero
slope, classify the higher-degree cases, or assert unrestricted
cancellation. All coefficient-field changes below remain
coefficient-field changes, not original polynomial automorphisms.

## 1. Actual input and the zero-safe high equations

Retain all hypotheses of
[264](principal-one-affine-paraboloid-chart-pass264-working.md)
and the genuine potentials of
[365](principal-paraboloid-nonlinear-intercept-unequal-degree-gate-pass365-working.md).
In particular,
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A_0[u],\qquad E=\partial_u,\qquad
a_0=EX\ne0,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\qquad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2),\\
0\ne N=[u^4]\partial_Z|_{A_0},\qquad
L=\operatorname{Frac}\ker_{A_0}N,\qquad
[L:\mathbb C(t,s)]<\infty,\\
Nv=1,\qquad O=L[v]=L[y,\sigma,\theta]=L[y,z,w],\\
K=\operatorname{Frac}A_0=L(v)=\mathbb C(y,z,w),\qquad
k=s,\qquad e=n_{ss}\ne0.
\end{gathered}
\tag{1}
\]
Thus the original global slice, full initial kernel, literal
selected partial, whole polynomial return, strong complex-field
return, and nonzero calibrated scalar are all retained.

Assume the equal intrinsic degree-one case and its zero y-slope:
\[
P=\sigma,\qquad O=L[P],\qquad \rho=NP\in L^*,\qquad
y=r\in L,\qquad \theta=\mu P+h,\quad \mu\in L^*.
\tag{2}
\]
The necessary leading-ratio result
[400](principal-paraboloid-equal-degree-leading-ratio-obstruction-pass400-working.md)
gives
\[
\mu\notin\mathbb C+\mathbb C t.
\tag{3}
\]
Only its consequence that mu is not complex is needed here.
No strict-degree rank condition from385 or387 is imported.

Coefficient subscripts initially mean the commuting extensions of
the coordinate partials on C(t,s) to L. Their joint constants are
C. Extend them to fix P and the actual X. Set
\[
a=n_t,\quad \nu=n_s,\quad c=n_{tt},\quad b=n_{ts},\quad
e=n_{ss}\ne0,\quad \beta=b+e\mu.
\tag{4}
\]
Here a is not a0. Since nu_s=e is nonzero, nu is nonzero.

The literal original-coordinate rows and calibrated scalar are
\[
\begin{aligned}
Y&=PX+r+tX^2,\\
Z&=P^2+(\mu+2tX)P+2tr+h+n+sX+t^2X^2,\\
W&=(\mu X-2r-a-\nu\mu)P+\ell-\nu h+hX+sX^2,\\
J_{\rm old}
&=\det\frac{\partial(Y,Z,W)}{\partial(t,s,P)}
=-a_0^4/\rho\in L^*.
\end{aligned}
\tag{5}
\]
For example z=2tr+P^2+theta+n and
w=ell-2Pr-aP-nu*theta give these rows.

The quadratic and linear coefficients of the third potential,
equivalently [401, (7)](principal-paraboloid-equal-degree-one-delta-zero-necessary-family-pass401-working.md)
with lambda=0, are
\[
c+2b\mu+e\mu^2=0,\qquad
\ell_t=-\nu(2r+a)+\beta h-\mu(\ell_s+\nu^2).
\tag{6}
\]
Let \(\mathscr D=\partial_t+\mu\partial_s\) and
\(\kappa=\mathscr D\mu\). The zero-safe high scalar equation
[401, (14)](principal-paraboloid-equal-degree-one-delta-zero-necessary-family-pass401-working.md)
gives
\[
\beta\kappa=0.
\tag{7}
\]
Indeed its general coefficient is
\([XP^2]J=-\{2(\lambda-\nu)\mathscr D\lambda+
\beta(\kappa+4\lambda)\}\). At lambda=0 it gives (7)
without dividing by beta.

## 2. The characteristic direction is constant on mu

If beta is nonzero, (7) immediately gives kappa=0.
It remains to prove the same statement when beta=0.

In that case mu=-b/e and (6) gives c=b^2/e.
Since nu_s=e is nonzero, t,nu are algebraically independent and
L is finite over C(t,nu). To justify independence directly, if
nu were algebraic over C(t), differentiating its separable minimal
polynomial in s would force nu_s=0. Finiteness then follows from
finite generation and equality of transcendence degrees.

In this temporary basis the exact coordinate partials are
\(\mathscr D\) and \(e^{-1}\partial_s\). They commute: they take
t,nu to the two coordinate basis vectors and extend uniquely
over the finite separable field extension. Write a temporary
prime for the second partial. The Legendre coefficient satisfies
\[
\mathscr D(n-\nu s)=a,\qquad
(n-\nu s)'=-s,\qquad
\mathscr Da=c+\mu b=0.
\tag{8}
\]
Consequently there are exact \(\mathscr D\)-constants \(A_1,B_1\)
with \(n-\nu s=A_1t+B_1\). Applying the prime gives
\(s=-A_1't-B_1'\), hence
\(\mu=\mathscr Ds=-A_1'\). Commutation shows
\(\mathscr D\mu=0\). This integration uses only subtraction of
an exact primitive inside L, not rationality of the constants.

Both alternatives in (7) have therefore proved
\[
\kappa=0.
\tag{9}
\]
If mu_s were zero, then mu_t=kappa-mu*mu_s would also be zero.
The joint-constant property would put mu in C, contrary to (3).
Thus mu_s is nonzero. None of this divides by lambda, beta or b.

## 3. A legitimate new coefficient basis and exact integrations

Put \(q=\mu\). The pair t,q is separating, by the same minimal-
polynomial argument used above, and L is finite over C(t,q).
From now on dots and primes mean
\[
\dot{\ }=\partial_t+q\partial_s,\qquad
{}'=\mu_s^{-1}\partial_s,\qquad
F=\ker_L(\dot{\ }),\qquad
\dot t=1,\quad \dot q=0,\quad t'=0,\quad q'=1.
\tag{10}
\]
These exact partials commute. Their joint constants remain C;
F is stable under primes. The element t is transcendental over F.
No equality F=C(q), L=F(t), or polynomial description of L is
assumed.

Since dot s=q, there is f in F such that
\[
s=qt+f,\qquad D:=s'=t+f'=\mu_s^{-1}\ne0.
\tag{11}
\]
Equation (6) and kappa=0 give
\[
\ddot n=c+2qb+q^2e+\kappa\nu=0.
\]
Exact integration therefore gives A,B in F with
\[
n=At+B,\qquad a+q\nu=A,\qquad
M:=A't+B',\qquad \nu=M/D\ne0.
\tag{12}
\]
Here A,B need not initially be complex.

Define
\[
g=2r+A,\qquad w_0=\ell-\nu h,\qquad H_c=g+\dot h.
\tag{13}
\]
The linear third-potential equation in (6) yields
\[
\dot\ell=-\nu g+\beta h,\qquad
\dot\nu=\beta,\qquad
\dot w_0=-\nu H_c.
\tag{14}
\]
For the first equality, use a+q*nu=A in (6) after adding
q*ell_s. Thus every holding-variable change in (14) is explicit.

The complete literal rows (5), now expressed in this basis, are
\[
\begin{aligned}
Y&=PX+(g-A)/2+tX^2,\\
Z&=P^2+(q+2tX)P+tg+h+B+(qt+f)X+t^2X^2,\\
W&=(qX-g)P+w_0+hX+(qt+f)X^2.
\end{aligned}
\tag{15}
\]
The coefficient-basis change has Jacobian
\(\det\partial(t,s)/\partial(t,q)=D\), so
\[
\widehat J=
\det\frac{\partial(Y,Z,W)}{\partial(t,q,P)}
=D J_{\rm old}=-D a_0^4/\rho\in L^*.
\tag{16}
\]
The dots and primes in this determinant fix P and X.

## 4. The complete scalar ledger and the dot-g gate

For direct reconstruction, the derivative matrix of (15) is
\[
\begin{pmatrix}
\dot g/2+X^2 &(g'-A')/2&X\\
2XP+g+t\dot g+\dot h+qX+2tX^2
 &P+tg'+h'+B'+DX&2P+q+2tX\\
-\dot gP+\dot w_0+\dot hX+qX^2
 &(X-g')P+w_0'+h'X+DX^2&qX-g
\end{pmatrix}.
\tag{17}
\]
Its entire determinant has just the following possible support:
\[
\widehat J=C_{20}X^2+C_{11}XP+C_{10}X+
             C_{02}P^2+C_{01}P+C_{00},
\tag{18}
\]
where
\[
\begin{aligned}
C_{20}&=-M H_c-D\dot w_0,\\
C_{11}&=-A'H_c+M\dot g-\dot w_0,\\
C_{10}&=(qM-Dg)\dot g/2-(M+h')\dot w_0+H_cw_0',\\
C_{02}&=A'\dot g,\\
C_{01}&=(qA'-g-2w_0')\dot g/2+(g'-A')\dot w_0,\\
C_{00}&=\bigl\{(g'-A')(gH_c+q\dot w_0)
       -\dot g\,[g(M+h')+qw_0']\bigr\}/2.
\end{aligned}
\tag{19}
\]
This is a full literal scalar ledger, not an expansion of only a
surface equation. The relation (14) makes C20 zero. Calibration
requires every other positive-degree coefficient in (18) to vanish,
while C00 is nonzero.

Suppose dot g were zero. Then (19) gives
\[
C_{01}=(g'-A')\dot w_0,\qquad
C_{00}=(g'-A')(gH_c+q\dot w_0)/2.
\]
If dot w0 is nonzero, C01=0 forces g'=A', so C00=0.
If dot w0 is zero, (14) and nu nonzero force Hc=0,
again giving C00=0. Both contradict (16). Hence
\[
\dot g\ne0.
\tag{20}
\]
In particular g is transcendental over F. Otherwise differentiating
its separable minimal polynomial over F would force dot g=0.

Now C02=0 gives A'=0. Since A belongs to F and the joint
constants of the two partials are C, A is complex, including
the possibility A=0. Equation (12) becomes
\(\nu=B'/D\), so B' is nonzero. Then C11=0 and (14) give
\[
0=B'\bigl(\dot g+H_c/D\bigr).
\]
Thus Hc=-D*dot g. Since dot D=1, this integrates exactly to
\[
A\in\mathbb C,\qquad B'\ne0,\qquad
h=-Dg+H_0,\qquad w_0=B'g+\omega,
\quad H_0,\omega\in F.
\tag{21}
\]
Indeed dot h=-D*dot g-g=-dot(Dg), and
dot w0=-nu*Hc=B'*dot g. No division by g or by any
lower integration constant was needed. The still-imposed C10,
C01 and C00 equations are not dropped; the following contradiction
already holds for the larger family (21).

## 5. Strong field return and the polynomial overring

At X=0, (15) and (21) give the exact intercepts
\[
y=(g-A)/2,\qquad
z=P^2+qP-f'g+H_0+B,\qquad
w=-gP+B'g+\omega.
\tag{22}
\]
They all belong to F[g,P]. Using the actual strong complex-field
return, not just whole return over L, yields
\[
L(P)=K=\mathbb C(y,z,w)\ \subseteq\ F(g,P)
       \subseteq\ L(P).
\tag{23}
\]
Consequently L=F(g). For completeness, intersect (23) with L:
P is transcendental over L, and comparison of coefficients in
any rational expression in P proves
\(F(g,P)\cap L=F(g)\).

Introduce the formal moving intrinsic variable
\[
R=P+tX.
\]
It is not declared an original polynomial coordinate. The actual
X is transcendental over K, since E kills K but EX is nonzero.
Together with the transcendence of g over F and P over L, this
shows that X,g,R are algebraically independent over F.
The full original rows become
\[
\begin{aligned}
Y&=XR+(g-A)/2,\\
Z&=R^2+qR-f'g+H_0+B+fX,\\
W&=(qX-g)R+B'g+\omega-f'gX+H_0X+fX^2.
\end{aligned}
\tag{24}
\]
All t dependence has canceled in these literal expressions.

Define
\[
\mathcal T=F[X,g,R],\qquad
\mathcal B_F=F[\mathcal B]=F[X,Y,Z,W]\subseteq\mathcal T.
\tag{25}
\]
These are rings in the actual common fraction field. The elements
of F, g, t and P are E-invariant. Also a0 belongs to L=F(g).
Since EX=a0 lies in B_F and hence in T, the polynomial intersection
\[
F[X,g,R]\cap F(g)=F[g]
\]
shows that \(d_0:=a_0\in F[g]\setminus\{0\}\).
Likewise \(d_1:=a_0t\in F(g)\) and
\[
EY=d_0R+Xd_1\in\mathcal T.
\]
Coefficient comparison in the independent variables X,R gives
\(d_1\in F[g]\). In detail, regard the last expression in
F(g)[X,R]; its coefficient of X must belong to F[g] because the
whole expression lies in F[g][X,R]. Therefore
\[
E|_{\mathcal T}
=d_0(g)\partial_X+d_1(g)\partial_R.
\tag{26}
\]
This explicitly proves E(T) is contained in T. The ring B_F is
also E-stable, since B is and E kills F. No general extension
theorem for derivations, normality assertion about B_F, or slice
on a smaller invariant ring is used. The original slice from
(1) remains part of the actual input, but no stronger slice
consequence is needed here.

## 6. A free quadratic extension and the complete W remainder

The first equation in (24) gives
\(g=2Y-2XR+A\), so
\[
\mathcal T=F[X,Y,R].
\]
Put \(S=F[X,Y,Z]\). The second row in (24) is equivalent to
\[
R^2+\mathfrak aR+\mathfrak b=0,\qquad
\mathfrak a=q+2f'X,\qquad
\mathfrak b=H_0+B+fX-2f'Y-f'A-Z.
\tag{27}
\]
In particular X,Y,Z are algebraically independent: substitution
of Z, a monic quadratic in the independent R over F[X,Y],
cannot kill a nonzero polynomial in Z.

Equation (27) gives the free quadratic module decomposition
\[
\mathcal T=S\oplus SR.
\tag{28}
\]
Spanning is monic division. Independence follows from the parity
of highest R-degree after substitution: a nonzero polynomial
in Z has even R-degree, whereas R times such a polynomial
has odd R-degree. This is a ring-theoretic equality without
localization or division by f'.

Substitute \(g=2Y-2XR+A\) in the last row of (24) and divide by
the monic polynomial in (27). The quotient is exactly 2X,
and the complete remainder is
\[
\begin{aligned}
W&=\mathfrak C+\mathfrak D R,\\
\mathfrak D&=-2Y-A-(q+2B')X-2f'X^2,\\
\mathfrak C&=(2Y+A)(B'+f'X)+\omega
                -(H_0+2B)X-fX^2+2XZ.
\end{aligned}
\tag{29}
\]
Thus every lower term is explicit. The coefficient of Y in
Dfrak is -2, so Dfrak is nonzero. From (28),(29),
\[
\mathcal B_F=S[\mathfrak D R]
             =S\oplus \mathfrak D SR.
\tag{30}
\]
For closure, use
\((\mathfrak D R)^2
=-\mathfrak a\mathfrak D(\mathfrak D R)
 -\mathfrak b\mathfrak D^2\). The directness in (30) follows
from (28).

The conductor of B_F in T is exactly
\[
\mathfrak c=\{c\in\mathcal T:c\mathcal T\subseteq\mathcal B_F\}
             =\mathfrak D\mathcal T.
\tag{31}
\]
Here is the full membership check. Write c=u+vR with u,v in S.
The condition c in B_F gives v in Dfrak*S. The further condition
cR in B_F gives
\(cR=-\mathfrak b v+(u-\mathfrak a v)R\), hence
\(u-\mathfrak a v\) in Dfrak*S and therefore u in Dfrak*S.
These two conditions are also sufficient, since T is generated
as an S-module by 1,R. Thus c belongs to Dfrak*T precisely when
it belongs to the conductor. This proof does not assume B_F
is normal or confuse a gcd with a principal coefficient ideal.

## 7. Original-derivation stability contradicts the conductor

Both rings in (31) are stable under the original E. Consequently
their conductor is E-stable: for c in the conductor and z in T,
\[
E(c)z=E(cz)-cE(z)\in\mathcal B_F.
\]
The first term is in B_F because cz is; the second is in B_F
because E(z) belongs to T. Hence
\(E(\mathfrak D)\in\mathfrak D\mathcal T\).

Rewrite (29) using the independent variables X,g,R of T:
\[
\begin{aligned}
\mathfrak D&=-g-2XR-(q+2B')X-2f'X^2,\\
E(\mathfrak D)&=-2d_0R-(q+2B')d_0
                     -4f'Xd_0-2Xd_1.
\end{aligned}
\tag{32}
\]
All q,B',f' coefficients belong to F, so are killed by E.

Both polynomials in (32) have exact R-degree one, with leading
coefficients -2X and -2d0 respectively. The second leading
coefficient is nonzero. If E(Dfrak)=Dfrak*Q in T, degree in R
over the domain F[g,X] gives Q in F[g,X]. Comparison of the
R coefficients then gives
\[
XQ=d_0(g).
\tag{33}
\]
Evaluating at X=0 contradicts d0 nonzero. This contradiction is
independent of whether f', A, H0, omega or any unused lower
coefficient vanishes.

It follows that the complete actual equal-degree-one chart
(1),(2) cannot have lambda=0. The proof uses the strong
complex-field return essentially in (23), and the actual
derivation essentially in (26),(31)--(33). Abstract coefficient
families without those actual gates are not excluded by this
argument.

## 8. Verification and scope boundary

The direct inputs264,365,400,401 and the conductor argument in403
were read in full during this work. Fresh unsaved reconstruction
f76402 gave the complete six-term determinant support.
The separate reconstruction c711d8 verified both branches of the
dot-g-zero contradiction, the integrations used in (21), and all
three literal polynomial rows (24). A fresh final independent
expansion d40b20 reproduced every coefficient in (19), the
quotient 2X and complete remainder (29), and both formulas (32),
with zero residuals.

These finite identities support the displayed algebra. They do
not independently prove the exact-field integrations, original
strong return, conductor calculation, or contradiction; those
arguments are written above. No saved checker was executed,
imported, compiled or rerun, and no earlier held source or
canonical index was edited.

This note is held for independent source review. It makes no
claim about nonconstant or constant nonzero lambda, higher
equal intrinsic degrees, arbitrary coupling k, entry of a general
cancellation candidate into the chart, unrestricted cancellation,
novelty, human-expert verification or formal proof certification.
