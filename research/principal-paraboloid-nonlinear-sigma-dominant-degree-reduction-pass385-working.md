# The strict sigma-dominant nonlinear profiles reduce to three pairs

Working result: retain the full actual principal chart264 with k=s
and n_ss nonzero, and assume theta is nonconstant but has strictly
smaller intrinsic degree than sigma. An exact affine change over L
puts the third surface in rank-three quadric form. Whole return and
the genuine cubic with its unit minors leave only
(deg theta,deg sigma)=(1,2),(2,3),(4,6).

The proof also gives necessary differential equations for the leading
ratio of y to sigma, including its possible zero value. None of the
changes over L is promoted to an actual polynomial reframe. This is
a necessary reduction, not recognition or exclusion of these last
three pairs. Theta constant and equal degrees are outside the claim.

## 1. Complete actual entry and the two genuine levels

Retain every actual hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md)
and the gradient/minor conclusion of
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md).
Use the complete k=s specialization in the fully read
[365](principal-paraboloid-nonlinear-intercept-unequal-degree-gate-pass365-working.md):
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A_0[u],\quad E=\partial_u,\quad
\deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(X^2Z-Y^2)\text{ is the full initial kernel},\quad
a_0=EX\ne0,\quad N=[u^4]\partial_Z|_{A_0}\ne0,\\
L=\operatorname{Frac}\ker_{A_0}N,\quad [L:\mathbb C(t,s)]<\infty,\quad
Nv=1,\quad O=L[v]=L[y,\sigma,\theta]=L[y,z,w],\\
K=\operatorname{Frac}A_0=L(v)=\mathbb C(y,z,w).
\end{gathered}
\tag{1}
\]
In particular the selected partial is the literal actual Z-partial.
The coefficient partials commute and fix the original v. The full map is
\[
\begin{aligned}
Y&=y+\sigma X+tX^2,&
Z&=z+(2t\sigma+s)X+t^2X^2,&
W&=w+\theta X+sX^2,\\
z&=2ty+\sigma^2+\theta+n,&
w&=\ell-2\sigma y-n_t\sigma-n_s\theta,\\
\det\frac{\partial(Y,Z,W)}{\partial(t,s,v)}&=-a_0^4\in L^*.
\end{aligned}
\tag{2}
\]
Here k=s is an assumption already satisfied by this frame, not an
asserted normalization of arbitrary k.

Let U,P,V be independent formal variables, and put
\[
\nu=n_s,\quad b=n_{ts},\quad e=n_{ss}\ne0,\quad
C=\ell_s+\nu^2,\quad J=\ell_t.
\tag{3}
\]
The full third polynomial and its level are
\[
\begin{aligned}
H={}&U^2+(n_t-2\nu P)U+\frac{n_{tt}}2P^2+bPV+\frac e2V^2\\
&-(\ell_t+\nu n_t)P-CV+\nu\ell,\qquad
H(y,\sigma,\theta)=h_0\in L.
\end{aligned}
\tag{4}
\]
The complete fourth polynomial, normalized by its formal constant, is
\[
\begin{aligned}
Q={}&[(n_{tt}+2\ell_s)P+bV-2bP^2-2ePV-\ell_t]U\\
&+\frac{n_{ttt}}6P^3+\frac{n_{tts}}2P^2V
 +\frac{n_{tss}}2PV^2+\frac{n_{sss}}6V^3\\
&-\frac{\ell_{tt}+2bn_t}{2}P^2
 -(\ell_{ts}+\nu b+en_t)PV-\frac{\ell_{ss}+2\nu e}{2}V^2\\
&+(b\ell+n_t\ell_s-(h_0)_t)P
 +(e\ell+\nu\ell_s-(h_0)_s)V,\qquad
Q(y,\sigma,\theta)=q_0\in L.
\end{aligned}
\tag{5}
\]
Its corrected formal gradients are those of296, so both
\[
(H_U,H_P,H_V)O=O,\qquad
(H_iQ_j-H_jQ_i:i<j)O=O.
\tag{6}
\]
All formal gradients are taken before evaluation.

The exact degrees of H-h0 and Q-q0 are two and three; the latter
has nonzero P V U coefficient -2e. The coprime-equation dimension
argument299, as specialized in365 Section3, consequently gives
\[
\max(\deg_v y,\deg_v\sigma,\deg_v\theta)\le6.
\tag{7}
\]
That section of365 is independent of the orientation of the degrees.
It uses the full minor identity to remove any common equation factor
and whole polynomial return to compare filtered dimensions. In
particular no irreducibility or plane-projection assumption is needed.

## 2. The leading ratio and its nonzero difference

Assume throughout the remainder of this note
\[
a:=\deg_v\sigma>h:=\deg_v\theta\ge1.
\tag{8}
\]
The symbols a,h here are degrees, not a0 or h0. Monicity of H in U
shows that deg y is at most a: otherwise y^2 has uniquely highest
degree after evaluation in (4). Define the exact coefficient
\[
\lambda=\frac{[v^a]y}{[v^a]\sigma}\in L,\qquad
\Delta=\lambda-\nu.
\tag{9}
\]
This definition allows lambda=0, when deg y<a.

The unique terms possibly of degree 2a in (4), and of degree 3a in
(5), give respectively
\[
\lambda^2-2\nu\lambda+\frac{n_{tt}}2=0,
\qquad n_{ttt}=12b\lambda.
\tag{10}
\]
For the second assertion, every cubic term involving V has degree
at most 2a+h<3a and every lower term degree at most 2a.

The difference Delta cannot vanish. If it did, (10) would give
n_tt=2nu^2. Its t derivative compared with the second equation
would give 8nu b=0. Since nu_s=e is nonzero, nu is a nonzero
field element, so b=0. But then n_tts=b_t=0, whereas the s derivative
of n_tt=2nu^2 is 4nu e, a nonzero element. This is a contradiction.
Thus
\[
\Delta\ne0,\qquad
\Delta\lambda_t=-2b\lambda,\qquad
b_t=4e\lambda-4\Delta\lambda_s.
\tag{11}
\]
The last two identities are the t and s derivatives of the first
equation in (10). No division by lambda or b has occurred.

## 3. A global affine remainder and the exact degree relation

Introduce coefficients and a formal affine remainder
\[
\begin{gathered}
d_1=\frac b{2\Delta},\qquad j=\frac J{2\Delta},\qquad
\bar h=h_0-\nu\ell+\frac{n_t^2}{4},\\
\mathcal R=U-\lambda P+d_1V+n_t/2-j,\\
\Omega=\frac e2+d_1^2,\qquad
\Lambda=C+2d_1j,\qquad \Gamma=j^2-\bar h.
\end{gathered}
\tag{12}
\]
The change from U,P,V to R,P,V is affine over L with determinant one.
An exact completion of the square, using (10), is
\[
H-h_0
=2\Delta P\mathcal R+\mathcal R^2-2d_1\mathcal RV+2j\mathcal R
 +\Omega V^2-\Lambda V+\Gamma.
\tag{13}
\]
This is a formal identity, not just an identity on the line.

The evaluated remainder initially has degree less than a, because
y-lambda*sigma does and h<a. If its degree r were at least h,
then 2Delta*sigma*R would have degree a+r, strictly larger than
2r, r+h and 2h. It would uniquely dominate (13). Consequently
either the evaluation of R is zero or its degree is less than h.

The zero case is impossible. If R evaluates to zero, (13) gives
Omega*theta^2-Lambda*theta+Gamma=0. The polynomial theta is
nonconstant and therefore transcendental over L, so
Omega=Lambda=Gamma=0 as coefficient identities. Thus the FULL
three-variable surface, not just a sliced equation, factors as
\[
H-h_0=\mathcal R(2\Delta P+\mathcal R-2d_1V+2j).
\tag{14}
\]
On the actual line every gradient entry is divisible by the
evaluation of the second factor. The first identity in (6) makes
that evaluation a unit of O, hence an element of L*. Yet its
degree is a, since 2Delta*sigma has degree a>h and R evaluates
to zero. This contradiction proves R^ev is nonzero.

Write r=deg_v R^ev, so 0<=r<h. If Omega=0, the term
2Delta*sigma*R again uniquely dominates (13): its degree a+r
exceeds 2r, r+h and h. Hence Omega is nonzero. Then the remaining
unique candidate of highest degree is Omega*theta^2, giving
\[
\boxed{\Omega\ne0,\qquad
a+r=2h,\qquad 0\le r<h.}
\tag{15}
\]
The determinant of the homogeneous quadratic part of H is
\[
\det(H_2)=-\Delta^2\Omega\ne0.
\tag{16}
\]
Thus its rank is three, even though no projective smoothness at a
possibly zero centered level is assumed.

If r=0, equation (13) solves sigma as a quadratic polynomial in
theta over L, because the coefficient 2Delta*R^ev is a unit.
Equation (12) then expresses y as a polynomial in theta. Whole
return in (1) gives O=L[theta], forcing h=1, and (15) gives a=2.
For r>0, a<2h. The bound (7) therefore leaves exactly
\[
(h,a)\in\{(1,2),(2,3),(3,4),(3,5),(4,5),(4,6),(5,6)\}.
\tag{17}
\]

## 4. A further necessary equation from the genuine cubic

There is a derivative gate not supplied by an abstract cubic.
Substitute U=lambda*P-d1*V-n_t/2+j+R in the complete (5).
Using (10),(11), its homogeneous degree-three part is exactly
\[
\begin{aligned}
Q_3^{\rm new}={}&-2bP^2\mathcal R
 +\left(\frac{b^2}{\Delta}-2\Delta\lambda_s\right)P^2V
 -2eP\mathcal RV\\
&+\left(\frac{eb}{\Delta}+\frac{e_t}{2}\right)PV^2
 +\frac{e_s}{6}V^3.
\end{aligned}
\tag{18}
\]
For example, the P^2 V coefficient before substituting b_t is
b^2/Delta-2e*lambda+b_t/2, giving the displayed expression.

The evaluated P^2 V has degree 2a+h. The other cubic terms have
degrees at most a+2h or 3h, by a+r=2h. Every term of total degree
at most two in the new variables has intrinsic degree at most 2a.
All these degrees are strictly below 2a+h, since a>h>=1.
Thus its coefficient must vanish:
\[
\boxed{\lambda_s=\frac{b^2}{2\Delta^2},\qquad
\Delta\lambda_t=-2b\lambda.}
\tag{19}
\]
Both equations retain lambda=0 and b=0. They are exact identities in
L with its original coefficient partials, not derivatives in a
newly normalized rational coefficient field.

## 5. Explicit transport to the retained quadric/cubic geometry

Define a further affine L-change, with all symbols still formal:
\[
\begin{gathered}
p=\mathcal R,\qquad
x=V-\frac{d_1}{\Omega}p-\frac{\Lambda}{2\Omega},\\
q=P+\frac{e}{4\Delta\Omega}p+\frac j\Delta
       -\frac{d_1\Lambda}{2\Delta\Omega},\\
\beta=\frac{2\Delta}{\Omega}\ne0,\qquad
d=\frac{\Lambda^2}{4\Omega^2}-\frac{\Gamma}{\Omega}.
\end{gathered}
\tag{20}
\]
The inverse is polynomial and affine over L:
\[
\begin{aligned}
V&=x+\frac{d_1}{\Omega}p+\frac{\Lambda}{2\Omega},\\
P&=q-\frac{e}{4\Delta\Omega}p-\frac j\Delta
       +\frac{d_1\Lambda}{2\Delta\Omega},\\
U&=\lambda P-d_1V-n_t/2+j+p .
\end{aligned}
\tag{21}
\]
The determinant from (R,P,V) to (p,x,q) is -1, and
\[
\frac{H-h_0}{\Omega}=x^2+\beta pq-d=:H_0.
\tag{22}
\]
After evaluation,
\[
O=L[p,x,q],\qquad
(\deg p,\deg x,\deg q)=(r,h,a),\qquad
(2x,\beta q,\beta p)O=O.
\tag{23}
\]
The degree assertions follow from r<h<a, so the lower affine
terms in (20) cannot cancel the leading terms of theta or sigma.

Substitute (21) into Q-q0 and call the resulting polynomial Phi.
It has exact total degree three, since the change is invertible
and affine. Formal gradients and their exterior products transform
by invertible coefficient matrices; no coefficient partial is taken
in that calculation. Thus
\[
\Phi(p(v),x(v),q(v))=0,\qquad
\bigl((H_0)_i\Phi_j-(H_0)_j\Phi_i:i<j\bigr)O=O.
\tag{24}
\]
These are precisely the abstract hypotheses used in Sections2--6
of the fully read
[367](principal-paraboloid-nonlinear-intercept-geometric-degree-exclusions-pass367-working.md).
They do not use its reciprocal formula for n after these hypotheses
have been established. Therefore the transfer is through explicit
identical algebraic and geometric inputs, not through an interchange
of the original coordinates sigma and theta.

For clarity, the exclusions being transferred are summarized here.
At d=0, the unit gradient forces gcd(p,q)=1, and exact UFD
factorization gives
p=c0*R1^2, x=c0*R1*S1, q=-c0*S1^2/beta.
The degree-five cases have odd degree p and are impossible. For
degrees (2,3,4), R1,S1 have degrees one and two; after using R1 as
parameter xi, the whole generated ring has odd module
xi(A*xi^2+C)L[xi^2] with A,C nonzero, and misses xi. For degrees
(4,5,6), R1,S1 have degrees two and three. Whole return would
force L[R1,S1]=L[v], contradicted by the same quadratic/cubic odd
module calculation. This treats every zero-level case being excluded.

At d nonzero, extend to the algebraic closure of L. Whole return
gives a smooth embedded affine line on the smooth projective quadric,
whose normalization is P1. The projective degree is a, and its
single point at infinity has local normalization orders
a, a-r and a-h for z/q, p/q and x/q. The genuine cubic cuts an
effective divisor of class (3,3). Unit minors give multiplicity one
along the line and prohibit affine intersections with the residual
divisor. The degree-four curve is smooth at infinity, has class
(1,3) or (3,1), and leaves two ruling fibers. Each requires
intersection number three, but its only possible intersection at
infinity has order one. The degree-five curves leave one ruling
fiber with required intersection number three, whereas the order
at infinity is respectively two or one. The degree-six curve with
degrees (4,5,6) is smooth rational but would be the whole (3,3)
divisor, of genus four. All are contradictions.

The normalization degree and additive Cartier intersections are
[Stacks, Section33.45](https://stacks.math.columbia.edu/tag/0BEL).
The Segre quadric and ruling description is given in
[Vakil, Foundations, Section5.1](https://virtualmath1.stanford.edu/~vakil/0708-216/216fall0708.pdf).
The genus formula follows from the divisor exact sequence on
P1 x P1 and chi(O(i,j))=(i+1)(j+1); see also
[Chao Li, Intersection Theory, Example15](https://www.math.columbia.edu/~chaoli/docs/IntersectionTheory.html).
The full local intersection-length argument and the exact odd-module
proofs are retained in367,355,356 and351, freshly read for this transfer.

Consequently the four pairs (3,4),(3,5),(4,5),(5,6) in (17) are
impossible, and the scoped conclusion is
\[
\boxed{\deg_v\sigma>\deg_v\theta\ge1,\quad k=s,\quad n_{ss}\ne0
\quad\Longrightarrow\quad
(\deg_v\theta,\deg_v\sigma)\in\{(1,2),(2,3),(4,6)\}.}
\tag{25}
\]

## 6. Boundaries and evidence

No part of the nonconstant-theta proof is applied when theta lies
in L. Its transcendence in the global factor argument and its
positive degree in (18) are explicit hypotheses. Equal degrees are
also outside (25). The leading ratio lambda is allowed to vanish;
no nonvanishing of b is assumed or inferred without its equation.

The surviving centered degree-(2,4,6) pattern is not excluded by the
abstract quadric/cubic geometry:351 and367 give exact whole-line
formal controls with unit minors at both zero and nonzero centered
levels. Such controls are not asserted to satisfy the literal
coefficient formulas, full scalar calibration, or strong complex
return of the actual chart. Further work must keep those distinctions.

All affine changes above occur only in the formal/intrinsic
coefficient-field polynomial rings. No coordinate of the original
four-ring, invariant polynomial, rationality of L, or recognition
theorem is asserted. The actual hypotheses (1),(2) remain in force.

The complete365,367,355,356 and351 sources were freshly read.
Fresh unsaved symbolic algebra independently checked (13),
(20)--(22), both affine inverse substitutions, the determinant -1,
and every cubic coefficient in (18), with zero residuals.
The degree comparisons, full factor argument, and geometric
transfer are the written proofs, not finite-test certificates.
No saved checker was executed, imported, compiled or rerun.
No held source, canonical index or ledger was changed.
No unrestricted cancellation, arbitrary normalization, novelty,
human-expert review or proof-assistant certification is claimed.

