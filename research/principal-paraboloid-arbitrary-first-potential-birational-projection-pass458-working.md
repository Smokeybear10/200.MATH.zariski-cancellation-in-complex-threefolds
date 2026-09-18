# Arbitrary first potential: exact equations and a finite birational projection

Working result: retain the entire supplied actual264 chart and assume
k=s+f with f_s=0. For arbitrary n and ell the complete third and fourth
potentials acquire the additional n_ss terms displayed below. If
n_ss and f''' are both nonzero, the projection to L[sigma,theta] is
finite and birational. When sigma is nonconstant, the evaluated linear
remainder cannot vanish and supplies a conductor denominator. When
sigma is constant, theta is affine and L[theta] is already the whole
intrinsic polynomial line.

These are necessary projection statements, not recognition or an
exclusion of the arbitrary-n sector. The projected ring in the
nonconstant branch is not declared normal. The note also verifies that
the original all-parameter polynomial-ring return of439 needs no
assumption n_ss=0.

## 1. Entire actual input and derivative conventions

Retain EVERY hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md), including
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad
\deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the entire weighted initial kernel},\\
a_0=EX\ne0,\quad X=a_0u+x_0,\quad x_0\in A,\quad
N=[u^4]\partial_Z|_A\ne0,\\
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,
\quad a_0\in L^*,\quad Nv=1,\\
O=L[A]=L[v]=L[y,z,w]=L[y,\sigma,\theta],\qquad
\operatorname{Frac}A=L(v)=\mathbb C(y,z,w),\\
\det\frac{\partial(Y,Z,W)}{\partial(t,s,v)}=-a_0^4\in L^*.
\end{gathered}
\tag{1}
\]
The exact coefficient partials on L commute and have joint constants C.
They are initially extended to fix v. Put F=ker_L(partial_s), finite
over C(t) but not assumed rational, and assume
\[
k=s+f,\qquad f\in F,
\qquad n,\ell\in L\text{ arbitrary}.
\tag{2}
\]
Primes on f mean exact t-derivatives. For convenience write
\[
a=n_t,\quad \nu=n_s,\quad c=n_{tt},\quad b=n_{ts},\quad e=n_{ss}.
\tag{3}
\]
In particular a_s=b, nu_t=b, nu_s=e, c_s=b_t and b_s=e_t.
Neither nu nor b is assumed to belong to F, and b may be zero.

The exact literal rows and the first two potentials are
\[
\begin{aligned}
Y&=y+\sigma X+tX^2,\\
Z&=z+(2t\sigma+s+f)X+t^2X^2,\\
W&=w+\theta X+sX^2,\\
z&=2ty+\sigma^2+f'\sigma+\theta+n,\\
w&=\ell-(2\sigma+f')y-\frac{f''}{2}\sigma^2-a\sigma-\nu\theta.
\end{aligned}
\tag{4}
\]
All later formal variables U,P,V are independent over L. Coefficient
partials of a formal polynomial hold those variables fixed and are
not total derivatives after evaluation at (y,sigma,theta).

## 2. The complete third potential and its gradients

The general264 formula specializes exactly to
\[
\boxed{
\begin{aligned}
H={}&U^2+\{(f''-2\nu)P+a-\nu f'\}U
 +\frac{f'''}6P^3+\frac{c-\nu f''}{2}P^2\\
&-(\nu a+\ell_t)P+\nu\ell
 +(bP-\ell_s-\nu^2)V+\frac e2V^2,
\qquad H(y,\sigma,\theta)=h\in L.
\end{aligned}}
\tag{5}
\]
For a direct derivation, the formal polynomial from264(12) is
F0=f''P^2/2+aP+nu V, and its second-potential expression is
\[
w_f=\ell-(2P+f')U-\frac{f''}{2}P^2-aP-\nu V.
\tag{6}
\]
Then H=U^2+(F0)_P U+(F0)_V w_f+f'''P^3/6
+cP^2/2+bPV+eV^2/2-ell_tP-ell_sV, giving every term of(5).
The complete three formal derivatives are
\[
\begin{aligned}
H_U&=2U+(f''-2\nu)P+a-\nu f',\\
H_P&=(f''-2\nu)U+\frac{f'''}2P^2+(c-\nu f'')P
                            -\nu a-\ell_t+bV,\\
H_V&=eV+bP-\ell_s-\nu^2.
\end{aligned}
\tag{7}
\]
The new term eV in H_V is retained. In particular the moving-slope
formula H_V=bP-ell_s-nu^2 from438 is not used when e is nonzero.

## 3. The complete genuine fourth potential

The corrected general gradient construction of
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md),
with k_s=1, gives
\[
\boxed{
\begin{aligned}
Q_U&=H_P-(2P+f')H_V+\nu H_U,\\
Q_P&=H_t-h_t-(2U+f''P+a)H_V+\nu H_P,\\
Q_V&=H_s-h_s.
\end{aligned}}
\tag{8}
\]
There is no requirement nu_s=0 in this identity. The two derivatives
of the actual level h must be retained. A primitive normalized by
Q(0,0,0)=0 is the following entire polynomial:
\[
\boxed{
\begin{aligned}
Q={}&\frac{f''}{2}U^2\\
&+\left\{\left(\frac{f'''}2-2b\right)P^2
 +(c+2\ell_s-bf')P+(b-ef'-2eP)V+f'\ell_s-\ell_t\right\}U\\
&+\frac{f''''}{24}P^4+\frac{n_{ttt}-3bf''}{6}P^3
 +\frac{f''\ell_s-\ell_{tt}-2ba}{2}P^2
 +(b\ell+a\ell_s-h_t)P\\
&+\left\{\frac{b_t-ef''}{2}P^2
       -(\nu b+ea+\ell_{ts})P+e\ell+\nu\ell_s-h_s\right\}V\\
&+\frac{e_tP-\ell_{ss}-2\nu e}{2}V^2+\frac{e_s}{6}V^3.
\end{aligned}}
\tag{9}
\]
For an explicit coefficient check, its three complete gradients are
\[
\begin{aligned}
Q_U={}&f''U+\left(\frac{f'''}2-2b\right)P^2
 +(c+2\ell_s-bf')P+(b-ef'-2eP)V+f'\ell_s-\ell_t,\\
Q_P={}&\{(f'''-4b)P+c+2\ell_s-bf'-2eV\}U
 +\frac{f''''}{6}P^3+\frac{n_{ttt}-3bf''}{2}P^2\\
&+(f''\ell_s-\ell_{tt}-2ba)P+b\ell+a\ell_s-h_t
 +\{(b_t-ef'')P-\nu b-ea-\ell_{ts}\}V+\frac{e_t}{2}V^2,\\
Q_V={}&(b-ef'-2eP)U+\frac{b_t-ef''}{2}P^2
 -(\nu b+ea+\ell_{ts})P+e\ell+\nu\ell_s-h_s\\
&+(e_tP-\ell_{ss}-2\nu e)V+\frac{e_s}{2}V^2.
\end{aligned}
\tag{10}
\]
Using the coefficient identities after(3), direct differentiation
of(5) verifies that(10) equals(8) in all three components.

For precise comparison with438, let Qbase mean its displayed polynomial,
but interpret every n derivative arbitrarily and its b' as n_tts=b_t.
Then the difference is exactly
\[
Q-Q_{\rm base}=eVw_f+\frac{e_t}{2}PV^2+\frac{e_s}{6}V^3.
\tag{11}
\]
When e=0 identically, both e_t and e_s vanish, recovering438. For
arbitrary n the extra terms cannot be suppressed. Similarly (5)
differs from its438 expression by eV^2/2.

The genuine construction of296 and the actual full scalar give
\[
Q(y,\sigma,\theta)=q_0\in L,
\qquad
(H_UQ_P-H_PQ_U,\ H_UQ_V-H_VQ_U,\ H_PQ_V-H_VQ_P)O=O.
\tag{12}
\]
These are inherited actual conclusions, not assumptions that an
arbitrary formal polynomial tuple satisfying(5) realizes the chart.

## 4. The exact monic remainder and the projection

For the rest of the projection argument impose explicitly
\[
e=n_{ss}\ne0,\qquad f'''\ne0.
\tag{13}
\]
Neither b nor any coefficient derivative of e is assumed nonzero.
Set mathscr C=L[sigma,theta]. Because H-h is monic quadratic in U,
\[
O=\mathscr C[y]=\mathscr C+\mathscr C y,
\qquad [L(v):\operatorname{Frac}\mathscr C]\in\{1,2\}.
\tag{14}
\]
In particular C has transcendence degree one: integrality and the
whole return rule out both sigma and theta being in L.

The exact monic reduction has the polynomial identity
\[
Q-q_0-\frac{f''}{2}(H-h)=R(P,V)U+S(P,V),
\tag{15}
\]
where
\[
\begin{aligned}
R(P,V)&=A(P)V+B_2(P),\qquad A(P)=b-ef'-2eP,\\
B_2(P)&=r_2P^2+r_1P+r_0,\\
r_2&=f'''/2-2b,\\
r_1&=c+2\ell_s-bf'-f''(f''-2\nu)/2,\\
r_0&=f'\ell_s-\ell_t-f''(a-\nu f')/2,\\
S(P,V)&=Q(0,P,V)-q_0-\frac{f''}{2}\{H(0,P,V)-h\}.
\end{aligned}
\tag{16}
\]
Equations(5),(9),(16) specify every remainder coefficient, including
the two level derivatives. Unlike438, the coefficient A(P) of V is
not a field unit. No division by A(sigma) is licensed in O.

## 5. Nonconstant sigma: the evaluated remainder cannot vanish

Suppose sigma is nonconstant, and assume temporarily
R(sigma,theta)=0. Divide the quadratic-or-lower polynomial B2 by
the linear polynomial A in L[P]. Its leading coefficient -2e is
nonzero. There are psi(P) of degree at most one and r0-flat in L with
\[
B_2(P)=A(P)\psi(P)+r_0^\flat,
\qquad A(\sigma)\{\theta+\psi(\sigma)\}=-r_0^\flat.
\tag{17}
\]
Because sigma is nonconstant, A(sigma) is a nonzero nonunit of O.
If r0-flat were nonzero, the second identity would make this nonunit
a factor of a unit, impossible. Thus r0-flat=0 and, since O is a
domain, theta=-psi(sigma). This is a polynomial conclusion; it did
not invert A(sigma).

Consequently C=L[sigma] and O=L[sigma,y]. Center the first generator
by the affine expression
\[
x=y+\frac{(f''-2\nu)\sigma+a-\nu f'}2.
\tag{18}
\]
Since theta is affine in sigma, substituting it in(5) gives
\[
x^2=-\frac{f'''}6\sigma^3+J_2(\sigma),\qquad
J_2\in L[P],\quad \deg J_2\le2,
\qquad O=L[\sigma,x].
\tag{19}
\]
No other term can cancel the cubic coefficient in(19), which is
nonzero by(13).

Let d=deg_v(sigma)>0. Polynomial division by sigma(v), after scaling
its leading coefficient, shows that L[v] is free over L[sigma] with
basis 1,v,...,v^(d-1). Independence also follows from their distinct
degree classes modulo d. On the other hand (19) generates O over
L[sigma] by 1,x. Localizing at the fraction field therefore gives
d<=2. The degree equation from(19) is 2 deg_v(x)=3d, so d is even.
It follows that
\[
\deg_v\sigma=2,\qquad \deg_vx=3.
\tag{20}
\]

Here is the elementary whole-generation obstruction, without a
plane-embedding theorem. Center sigma by translating v over L, then
scale sigma to get L[sigma]=L[z^2]. Write the full cubic x in z and
subtract its even part, which belongs to L[z^2]. Its remaining odd
part is z(A2*z^2+A0), with A2 in L*. The generated ring is exactly
\[
L[z^2,x]=L[z^2]\mathbin{\oplus}z(A_2z^2+A_0)L[z^2].
\tag{21}
\]
The square of the odd generator belongs to L[z^2], which proves
this module description. Comparing odd parts shows that this ring
does not contain z, since A2*z^2+A0 is a nonunit. This contradicts
O=L[z]. No square root of the leading quadratic coefficient is needed.

We have proved the stronger statement
\[
\boxed{\sigma\notin L\quad\Longrightarrow\quad
             R(\sigma,\theta)\ne0.}
\tag{22}
\]
This did not assume that the field degree in(14) was two. If that
degree were two, the linear independence of 1,y over Frac(C) in
the evaluated identity(15) would force R(sigma,theta)=0. Thus the
nonconstant-sigma projection is birational.

## 6. Constant sigma and the exact descent from the conic

Suppose now sigma belongs to L. The monic relation(5) and whole
generation show theta is nonconstant: if theta also belonged to L,
then y would be algebraic over L in L[v], hence constant as well.

Complete the squares in the specialized binary conic. After affine
translations of y and theta by elements of L it has the form
\[
x^2+\frac e2 z^2=d_0,\qquad d_0\in L,
\qquad L[x,z]=L[y,\theta]=L[v].
\tag{23}
\]
Extend scalars to an algebraic closure M of L and choose a nonzero
q in M with q^2=-e/2. Then
(x+qz)(x-qz)=d0 in M[v]. If d0 is nonzero, both factors are units
and hence constant, contradicting nonconstant theta. If d0=0,
one factor is zero. Thus y is affine in theta over M, and
\[
M[v]=M[y,\theta]=M[\theta].
\tag{24}
\]
Equality(24) forces the polynomial theta to have degree one.
Scalar extension does not change the degree of a nonzero polynomial
with coefficients in L, so deg_v(theta)=1 over L too. Its affine
inverse has coefficients in L. Therefore
\[
\boxed{\sigma\in L\quad\Longrightarrow\quad
       O=\mathscr C=L[\theta],\qquad
       [L(v):L(\theta)]=1.}
\tag{25}
\]
This separates the scalar extension used to factor the conic from
the field-degree conclusion over L. No assertion about an actual
complex coordinate follows from theta being intrinsic-affine.

## 7. Normalization and the precise unresolved ring boundary

Both sigma cases prove
\[
\boxed{O\text{ is finite and birational over }\mathscr C=L[\sigma,\theta].}
\tag{26}
\]
Since O=L[v] is integrally closed, it is exactly the normalization
of C in their common fraction field. Indeed an element integral
over C is also integral over O and therefore belongs to O.

In the nonconstant-sigma case put r=R(sigma,theta) in C, nonzero
by(22). Evaluating(15) gives r*y=-S(sigma,theta) in C. Since
O=C+Cy, this proves
\[
rO\subset\mathscr C,\qquad
O[r^{-1}]=\mathscr C[r^{-1}].
\tag{27}
\]
Thus the conductor contains rO. This is not a claim that the conductor
equals rO, that r is a unit, or that C=O without localization. No
global plane-coordinate return or original invariant coordinate is
proved here. In particular the quadric-degree conclusions of441
are not transferred through the additional eV^2 term in(5).

## 8. The all-parameter return survives arbitrary n

This section uses only the actual input and k=s+f; it requires neither
condition in(13), nor b nonzero, nor sigma nonconstant. Define over L
\[
A_1=f''-2\nu,\qquad B_1=a-\nu f',\qquad
x=y+(A_1\sigma+B_1)/2,\qquad
\zeta=\theta+\sigma^2+f'\sigma.
\tag{28}
\]
The original slice in(1) gives
\[
L[\mathcal B]=O[u]=O[X]=L[X,v],
\tag{29}
\]
because X=a0*u+x0, a0 in L*, and x0 in A subset O. This uses the
original polynomial slice, not an assertion that X/a0 is that slice.

At fixed X make the following polynomial row change over L[X]:
\[
\begin{aligned}
Y_c&=Y-tX^2+B_1/2,\\
Z_c&=Z-2tY-n-(s+f)X+t^2X^2,\\
W_c&=\ell+sX^2+f'B_1/2+(X-\nu)Z_c-f'Y_c-W.
\end{aligned}
\tag{30}
\]
Its determinant in Y,Z,W is -1. The complete inverse is
\[
\begin{aligned}
Y&=Y_c+tX^2-B_1/2,\\
Z&=Z_c+2tY_c+t^2X^2-tB_1+n+(s+f)X,\\
W&=\ell+sX^2+f'B_1/2+(X-\nu)Z_c-f'Y_c-W_c.
\end{aligned}
\tag{31}
\]
Direct substitution of the full rows(4), without differentiating any
moving coefficient, gives, with T=X-A1/2,
\[
Y_c=x+T\sigma,\qquad Z_c=\zeta,\qquad
W_c=2\sigma x+T\sigma^2.
\tag{32}
\]
Equations(29)--(31) are a polynomial-ring equality before specializing
X. After any field extension M/L, quotient by X-(T0+A1/2), for ANY
T0 in M. The invertible row change remains valid at that value, giving
\[
\boxed{M[x+T_0\sigma,\ \zeta,\ 2\sigma x+T_0\sigma^2]=M[v]
       \quad\text{for every }M/L\text{ and every }T_0\in M.}
\tag{33}
\]
This extends exactly the all-parameter license in439, not its
moving-slope third-potential formula. It requires no generic-value
qualification, division by a root, or rationality of L. The row change
is over L[X], not an original complex polynomial automorphism.

## 9. Verification and limited conclusion

The current264 and296 sources were read completely for the general
potential construction, and438 for the comparison. The entire439
source was read before revalidating its actual return for arbitrary n.
Fresh unsaved6fa5ba rebuilt H, the complete Q in(9), all three exact
identities(8), and the monic coefficient R in(16), with zero residuals.
It retained arbitrary compatible n and ell jets and both moving level
derivatives. Fresh b129f0 reconstructed all three transformed actual
rows, both orders of the inverse(30),(31), and determinant -1, with
every identity residual zero.

The finite-ring, polynomial-rank, odd-module, scalar-extension and
normalization arguments are the written proofs above, not consequences
of symbolic sampling. The source makes no degree-bound extrapolation,
recognition claim, arbitrary-n exclusion or assertion that a formal
solution of selected equations realizes the actual chart. The earlier
k=s synthesis422 is not extended by setting the nonzero f''' term to
zero in a coefficient-field presentation.

All actual264 and296 dependency hypotheses remain retained. No saved
checker was executed, imported, compiled or rerun. No earlier source
or canonical index was edited, and no unrestricted cancellation,
historical novelty or formal-certification claim is made.
