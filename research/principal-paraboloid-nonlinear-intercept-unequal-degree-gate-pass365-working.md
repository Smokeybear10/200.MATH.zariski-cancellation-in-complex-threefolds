# A reciprocal derivative gate for the nonlinear intercept sector

Working result: in the complete actual chart264 with k=s and n_ss
nonzero, the third and fourth levels have degrees two and three.
Consequently every intrinsic generator has degree at most six.
More specifically, if sigma is nonconstant and theta has strictly
larger intrinsic degree, then
n_ss=-1/(2(t-tau)^2), with tau complex. An exact coefficient-field
shear gives a sharper degree relation and forces the quadratic part
of the third level to have rank three.

This is a necessary reduction, not recognition, an actual
normalization, or an assertion that n_ss must vanish. Equal intrinsic
degrees and the reverse degree inequality are not classified here.
No earlier source, checker, index, or packet is changed.

## 1. Complete actual hypotheses

Retain the whole actual entry of the fully read
[264](principal-one-affine-paraboloid-chart-pass264-working.md)
and the fourth level and minor-unit theorem of the fully read
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md):
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad
\deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(X^2Z-Y^2)\text{ is the full initial kernel},\qquad
a_0=EX\ne0,\\
N=[u^4]\partial_Z|_A,\qquad
L=\operatorname{Frac}\ker_A N,\qquad [L:\mathbb C(t,s)]<\infty,\\
O=L[v]=L[y,\sigma,\theta]=L[y,z,w],\qquad Nv=1,\qquad
K=L(v)=\mathbb C(y,z,w).
\end{gathered}
\tag{1}
\]
The actual fixed-X map and calibration are
\[
\begin{aligned}
Y&=y+\sigma X+tX^2,\\
Z&=z+(2t\sigma+s)X+t^2X^2,\\
W&=w+\theta X+sX^2,\qquad
\det\frac{\partial(Y,Z,W)}{\partial(t,s,v)}=-a_0^4\in L^*.
\end{aligned}
\tag{2}
\]
Here we assume the already normalized coefficient k=s, not that an
arbitrary coupling can be put in that form. Its first potentials are
\[
z=2ty+\sigma^2+\theta+n,\qquad
w=\ell-2\sigma y-n_t\sigma-n_s\theta,\qquad n,\ell\in L.
\tag{3}
\]
Assume throughout that e:=n_ss is nonzero.

The coefficient partials on L are the unique extensions of the
partials on C(t,s), commute, and fix the original v. Their joint
constant field is C. Indeed a joint constant is algebraic over
C(t,s); differentiating its monic minimal polynomial shows that
every coefficient is a joint constant, hence lies in C. It is then
algebraic over the algebraically closed field C. We write
\(\mathcal F=\ker_L\partial_s\), a finite extension of C(t).
No equality L=F(s) is assumed.

Every subsequent formal derivative holds U,P,V fixed, before
evaluation at (y,sigma,theta).

## 2. The complete quadric and cubic

Use the coefficient abbreviations
\[
a=n_t,\qquad \nu=n_s,\qquad c=n_{tt},\qquad
b=n_{ts},\qquad e=n_{ss}\ne0.
\tag{4}
\]
These are not the slice speed a0 or ambient coordinates. Direct
specialization of264 gives
\[
\begin{aligned}
H={}&U^2+(a-2\nu P)U+\frac c2P^2+bPV+\frac e2V^2\\
&-(\ell_t+\nu a)P-(\ell_s+\nu^2)V+\nu\ell,\qquad
H(y,\sigma,\theta)=h\in L.
\end{aligned}
\tag{5}
\]
The corrected fourth gradients296 specialize to
\[
Q_U=H_P-2PH_V+\nu H_U,\quad
Q_P=H_t-h_t-(2U+a)H_V+\nu H_P,\quad Q_V=H_s-h_s.
\tag{6}
\]
Their primitive, normalized to have zero formal constant term, is
\[
\begin{aligned}
Q={}&\big[(c+2\ell_s)P+bV-2bP^2-2ePV-\ell_t\big]U\\
&+\frac{n_{ttt}}6P^3+\frac{n_{tts}}2P^2V
 +\frac{n_{tss}}2PV^2+\frac{n_{sss}}6V^3\\
&-\frac{\ell_{tt}+2ba}{2}P^2
 -(\ell_{ts}+\nu b+ea)PV-\frac{\ell_{ss}+2\nu e}{2}V^2\\
&+(b\ell+a\ell_s-h_t)P+(e\ell+\nu\ell_s-h_s)V .
\end{aligned}
\tag{7}
\]
Differentiating (7) in U,P,V gives all three expressions (6),
using the commuting mixed partials of n and ell. Thus this is the
genuine fourth potential, not an arbitrary cubic through the line:
\[
Q(y,\sigma,\theta)=q\in L.
\tag{8}
\]
Its exact total degree is three because its P V U coefficient is
-2e. The third level H-h has exact degree two.
The evaluated gradient ideal of H and the evaluated two-by-two
minor ideal of grad H, grad Q are both the unit ideal of O, by296.

Center only the formal and intrinsic variables:
\[
\begin{gathered}
x=U+a/2-\nu P,\quad A=c/2-\nu^2,\quad
C=\ell_s+\nu^2,\quad J=\ell_t,\quad
\bar h=h-\nu\ell+a^2/4,\\
H-h=x^2+AP^2+bPV+\frac e2V^2-JP-CV-\bar h.
\end{gathered}
\tag{9}
\]
The same x denotes its evaluation when an intrinsic degree is taken.
The determinant of the quadratic-part matrix is
\[
\det\begin{pmatrix}
1&0&0\\0&A&b/2\\0&b/2&e/2
\end{pmatrix}
=\frac{e(c-2\nu^2)-b^2}{4}.
\tag{10}
\]
Its rank is three when this determinant is nonzero, and exactly
two otherwise, since e is nonzero. This refers to the homogeneous
quadratic part, not to projective smoothness of the full surface.
The monic-U discriminant is
\[
\begin{aligned}
\Delta={}&(4\nu^2-2c)P^2-4bPV-2eV^2\\
&+4\ell_tP+4(\ell_s+\nu^2)V+a^2-4\nu\ell+4h.
\end{aligned}
\tag{11}
\]
No reducibility assumption is made. The previously read302/324
reducible-surface conclusions remain separate retained results.

## 3. The six-bound is an elementary specialization

The complete coprime-equation dimension argument of the fully read
[299](principal-paraboloid-generic-degree-bound-pass299-working.md)
applies to (5),(7), now with degrees two and three instead of three
and four. For precision, if D is the polynomial gcd of H-h and Q-q,
the minor-unit identity first shows that D does not vanish identically
on the line. The two reduced factors therefore do vanish there.
Their gradient minors are multiplied by the square of D on evaluation,
so D evaluates to a unit of O.

If the reduced factors have degrees r1,r2, their coprime
homogenizations have degree-N quotient dimension
\(r_1r_2N+O(1)\). Evaluation surjects onto the polynomials obtained
from expressions of total degree at most N in y,sigma,theta.
If d is the largest of their intrinsic degrees, whole return in (1)
gives d(N-C0+1) independent expressions, by multiplying a generator
of degree d by fixed expressions for 1,v,...,v^(d-1).
Comparison for arbitrarily large N gives
\[
\max\{\deg_v y,\deg_v\sigma,\deg_v\theta\}
\le r_1r_2\le 2\cdot3=6.
\tag{12}
\]
This argument does not require the surface to be irreducible, the
projection to be birational, or the two levels to generate the entire
curve ideal. The projected degree-six bound for a degree-two
projection in299 is a different assertion. Equation (12) bounds
all three intrinsic generators in this normalized sector.

## 4. A strict theta-dominant degree forces a reciprocal coefficient

Assume from now on that
\[
1\le a_P:=\deg_v\sigma<h_V:=\deg_v\theta .
\tag{13}
\]
The different symbol a_P is a degree, not the coefficient a in (4).
The quadric (9) forces deg_v x=h_V, because its e theta^2/2 term
has strictly greater degree than every term not involving x.
If alpha=lc_v(x)/lc_v(theta), its leading equation is
\[
\alpha^2=-e/2,\qquad \alpha\in L^*.
\tag{14}
\]
The original U evaluation y also has degree h_V and the same
leading ratio, since y=x-a/2+nu sigma.

In the complete cubic (7), the term n_sss theta^3/6 is the only
possible term of degree 3h_V. Every other term has degree at most
a_P+2h_V or 2h_V, both strictly smaller. Thus n_sss=0.
Once this term has vanished, the only terms of degree a_P+2h_V
are -2e sigma theta y and n_tss sigma theta^2/2.
All terms of degree 2h_V are smaller because a_P is positive.
Their leading coefficients give
\[
e_s=0,\qquad e_t=4e\alpha,\qquad e_t^2=-8e^3.
\tag{15}
\]
In particular e_t is nonzero. Centering U does not spoil this
comparison: its extra cubic terms have types P^3 and P^2V,
of strictly smaller intrinsic degree.

These differential equations integrate in the exact field, without
a rational ansatz or extraction of a coefficient-field square root.
Differentiate the last identity in t to obtain e_tt=-12e^2.
Then
\[
\tau:=t+\frac{2e}{e_t}
\quad\text{satisfies}\quad \tau_t=\tau_s=0.
\]
Thus tau is complex. Set T=t-tau. Since T=-2e/e_t, (15) gives
\[
\boxed{
e=-\frac1{2T^2},\qquad
\alpha=-\frac1{2T},\qquad
n=-\frac{s^2}{4T^2}+f_1s+f_0,\qquad f_1,f_0\in\mathcal F .
}
\tag{16}
\]
The last integration is internal to L: subtract e s^2/2, whose
second s derivative is e, then integrate the two exact constants
of partial_s. It does not identify L with F(s).
Also
\(b=n_{ts}=s/T^3+f_1'\ne0\), since its s derivative is 1/T^3.

## 5. Rank three and a sharper intrinsic profile

Use an invertible affine L-change of the formal variables,
not a change of the original polynomial coordinates:
\[
\zeta=x+\frac{V}{2T},\qquad
\mathcal R=\zeta-TbP+TC,\qquad
\mathcal N=\zeta^2+AP^2-JP-\bar h.
\]
The complete identity (9) becomes
\[
H-h=\mathcal N-\frac{V}{T}\mathcal R.
\tag{17}
\]
By (14),(16), the evaluation of zeta has degree less than h_V.
If its degree were larger than a_P, the term zeta theta in (17)
would uniquely dominate all other terms, which is impossible.
If its degree were smaller than a_P, the term b sigma theta
would uniquely dominate, since b is nonzero and h_V>a_P.
Consequently
\[
\deg_v\zeta=a_P,\qquad
\operatorname{lc}_v(\zeta)=Tb\operatorname{lc}_v(\sigma),
\qquad \deg_v\mathcal R^{\rm ev}<a_P
\tag{18}
\]
unless the last evaluation is zero.

That zero possibility is excluded using the full gradient ideal,
not a gradient ideal of a slice. If R evaluates to zero, then
zeta=Tb sigma-TC. Equation (17) says that
N(P,TbP-TC) vanishes at the nonconstant polynomial sigma.
Sigma is transcendental over L, so this is a zero polynomial in P.
Therefore the formal polynomial N is divisible by the monic affine
R in L[P,zeta]. Its quotient is affine. The entire three-variable
surface H-h thus factors globally as R times an affine polynomial
whose V coefficient is -1/T. Along the actual curve, every gradient
of H is divisible by the evaluation of that second factor.
The unit-gradient conclusion of296 forces that evaluation into L*.
But it has degree h_V, since its other variables have degree a_P.
This is a contradiction. Hence R^ev is nonzero.

Write r0=deg_v R^ev, so 0<=r0<a_P, and set
\(\Omega=A+T^2b^2\). Substitution of
zeta=TbP-TC+R gives
\[
\begin{aligned}
\mathcal N={}&\Omega P^2+2TbP\mathcal R+\mathcal R^2
 -(2T^2bC+J)P-2TC\mathcal R+T^2C^2-\bar h.
\end{aligned}
\tag{19}
\]
If Omega were zero, its evaluation would have degree at most
a_P+r0, whereas (17) makes that degree h_V+r0. This is impossible.
Thus Omega is nonzero, and the unique leading term in (19) has
degree 2a_P. Equations (10),(16),(17) now prove
\[
\boxed{
\Omega\ne0,\quad
\det(H_2)=-\frac{\Omega}{4T^2}\ne0,\quad
h_V+r_0=2a_P,\quad 0\le r_0<a_P .
}
\tag{20}
\]
In particular a_P<h_V<=2a_P.

If r0=0, R^ev is a nonzero coefficient-field constant.
Equations (17),(18) then express theta as a quadratic polynomial
in sigma, and x,y also as polynomials in sigma. Whole return gives
O=L[sigma], so a_P=1 and h_V=2. For a_P>=2 the upper inequality
is strict. Together with (12), the possible degree pairs in this
one branch are therefore
\[
(a_P,h_V)\in
\{(1,2),(2,3),(3,4),(3,5),(4,5),(4,6),(5,6)\}.
\tag{21}
\]
The list is necessary, not a realization or sufficiency statement.

## 6. Boundaries and evidence

The positive degree of sigma is essential for the second leading
comparison in (15). If sigma is constant, terms of degree 2h_V
can tie with other terms in the complete cubic. That case is not
excluded here. Nor does this argument classify theta of degree
at most sigma, or show that every rank-two quadric is reducible.
The coefficient-field shear in Section5 has not been promoted to
an actual automorphism or polynomial coordinate.

The principal new result is the reciprocal derivative and rank/profile
gate (16),(20). The six-bound is a specialization of299's retained
dimension lemma. Both use the genuine lower potentials and exact
whole-line/minor inputs, not just a formal quadric parametrization.

The complete264,296,299,302,303 and324 sources were read while
checking for overlap and establishing the direct inputs. Fresh
unsaved algebra reconstructed all three complete cubic gradients,
the centered quadric, its determinant, the identity (17), and the
expansion (19), with zero residuals. Exact-field integration,
degree comparisons, and the global factor argument are proved
above and are not certified by finite tests.
No saved checker was executed, imported or compiled.
No unrestricted cancellation, arbitrary normalization, novelty,
human-expert review, or proof-assistant certification is claimed.
