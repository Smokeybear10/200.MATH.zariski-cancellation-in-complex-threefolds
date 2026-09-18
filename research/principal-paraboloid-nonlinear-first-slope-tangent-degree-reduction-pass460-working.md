# Nonlinear first slope: a tangent minor forces quadratic transverse dependence

Working necessary result: retain the entire actual264 chart, and assume
\[
k=s+f,\qquad f_s=0,\qquad e=n_{ss}\ne0,\qquad f'''\ne0.
\tag{1}
\]
Then
\[
\boxed{n_{sss}=0,\qquad
n=\frac{e(t)}2s^2+\nu_0(t)s+n_0(t),\quad e,\nu_0,n_0\in F=\ker_L\partial_s.}
\tag{2}
\]
The notation e(t),nu0(t),n0(t) denotes membership in the EXACT field F,
not rationality in t.

If sigma is nonconstant, put a=deg_v sigma. The centered first and
third generators defined below have equal degrees r, and
\[
\boxed{\deg_v y=\deg_v\theta=r,\qquad 2r\ge3a>0.}
\tag{3}
\]
The strict and balanced alternatives have additional necessary coefficient
identities proved in Sections6--7. If sigma is constant, y and theta are
both intrinsic-affine and(2) still holds.

No finite upper degree bound, realization, exclusion of all remaining
data or original-ring recognition is asserted. The argument uses the
full genuine fourth potential and its minor UNIT, not a finite search.

## 1. Entire actual hypotheses and the complete centered cubic

Retain EVERY hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md)
and the arbitrary-n formulas of
[458](principal-paraboloid-arbitrary-first-potential-birational-projection-pass458-working.md).
In particular
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad
\deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the ENTIRE weighted initial kernel},\\
a_0=EX\ne0,\qquad X=a_0u+x_0,\quad x_0\in A,\qquad
N=[u^4]\partial_Z|_A\ne0,\\
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,\quad
Nv=1,\quad O=L[A]=L[v]=L[y,\sigma,\theta],\\
\operatorname{Frac}A=L(v)=\mathbb C(y,z,w),\qquad
\det\frac{\partial(Y,Z,W)}{\partial(t,s,v)}=-a_0^4\in L^*.
\end{gathered}
\tag{4}
\]
Every original slice, localization, selected-partial and return hypothesis
remains in force. The original slice u is not replaced by X/a0.
The coefficient partials on L commute and have joint constants C.
The field F=ker_L(partial_s) is finite over C(t), not assumed rational.

Use the arbitrary first potential n and write
\[
\nu=n_s,\quad b=n_{ts},\quad e=n_{ss},\quad
A_1=f''-2\nu,\quad B_1=n_t-\nu f',\quad C=\ell_s+\nu^2.
\tag{5}
\]
Neither b nor nu is assumed to belong to F, and b may be zero.
Primes on f mean exact coefficient t-derivatives.

The complete third polynomial of458 is
\[
\begin{aligned}
H={}&U^2+(A_1P+B_1)U+\frac{f'''}6P^3
 +\frac{n_{tt}-\nu f''}{2}P^2\\
&-(\nu n_t+\ell_t)P+\nu\ell+(bP-C)V+\frac e2V^2,
\qquad H(y,\sigma,\theta)=h\in L.
\end{aligned}
\tag{6}
\]
All formal variables U,P,V are independent over L. Make the invertible
AFFINE change of formal variables over L
\[
x=U+(A_1P+B_1)/2,\qquad q=V+(bP-C)/e,\qquad P=P.
\tag{7}
\]
Its inverse subtracts the same two affine expressions. Its determinant
is one and its only new coefficient denominator is e in L*. No evaluated
polynomial is inverted. It is not an ambient complex coordinate map.

Write
\[
\begin{aligned}
T(P)={}&\frac{f'''}6P^3+\frac{n_{tt}-\nu f''}{2}P^2
 -(\nu n_t+\ell_t)P+\nu\ell-h\\
&-\frac{(A_1P+B_1)^2}{4}-\frac{(bP-C)^2}{2e}.
\end{aligned}
\tag{8}
\]
Then the transformed third equation is exactly
\[
\boxed{\mathcal H=x^2+\frac e2q^2+T(P),\qquad
\deg_P T=3,\quad [P^3]T=f'''/6\ne0.}
\tag{9}
\]
After evaluation P=sigma and the symbols x,q denote the corresponding
elements of O. In particular O=L[x,P,q].

## 2. The full centered fourth support

Let Q be the ENTIRE genuine fourth potential458(9), retaining both
h_t and h_s, and let Q(y,sigma,theta)=q0 in L. If tau denotes the
inverse substitution in(7), define
\[
\Phi=\tau\{Q-q_0-f''(H-h)/2\}.
\tag{10}
\]
The two evaluated levels Hcal and Phi vanish. Their evaluated gradient
minors generate O by296/458: subtracting the multiple of H-h and
applying the invertible affine Jacobian preserve that component ideal.

Define
\[
D(P)=b-ef'-2eP.
\]
The complete support has the following exact form:
\[
\boxed{\Phi=x\{T'(P)+D(P)q\}+K(P,q),}
\tag{11}
\]
\[
\begin{aligned}
K(P,q)={}&\frac{f''''}{24}P^4+K_3(P)+J_2(P)q\\
&+\left\{\frac12\left(e_t-\frac{be_s}{e}\right)P+c_0\right\}q^2
 +\frac{e_s}{6}q^3,\\
&\deg K_3\le3,\qquad\deg J_2\le2,\\
c_0={}&-\frac{ef''}{4}-e\nu-\frac{\ell_{ss}}2+\frac{e_sC}{2e}.
\end{aligned}
\tag{12}
\]
The prime on T in(11) is its FORMAL P-derivative, not a coefficient
t-derivative. K3,J2 and c0 are exact coefficient polynomials determined
by(10), not new free parameters. Equations(6),(8),(10) together with
the complete458 Q define every lower coefficient and moving level.

Here is a direct verification of the structure. In the new variables,
the old formal partials of H are
\[
H_U=2x,\qquad H_V=eq,\qquad H_P=T'(P)+A_1x+bq.
\]
The corrected identity Q_U=H_P-(2P+f')H_V+nu H_U therefore gives
Q_U=f''x+T'+Dq. Subtracting f''(H-h)/2 gives exactly(11).
There is no x^2 term left.

All terms of Q other than f''''P^4/24 have total degree at most three.
The affine substitution(7) preserves this fact, so the only quartic
term of K is the one displayed. The only original V^3 term is
e_s V^3/6, so its q^3 coefficient is e_s/6. Its q^2 contribution
is -e_s(bP-C)/(2e). Combining this with the original
(e_tP-ell_ss-2nu e)V^2/2 and the subtracted f''e q^2/4 gives all
of the q^2 coefficient in(12). All other q-dependent terms have
exactly the remaining support in(12).

## 3. The genuine minor is a primitive tangent component

Differentiate only in the intrinsic variable v, fixing L. In this
section write a dot for that derivative, to separate it from all
coefficient partials. Whole generation O=L[x,P,q] gives
\[
a_1\dot x+a_2\dot P+a_3\dot q=1
\quad\text{for some }a_i\in O.
\tag{13}
\]
Indeed differentiate a polynomial expression for v in x,P,q.

The two evaluated formal gradients annihilate this tangent vector.
Their cross product is nonzero by its unit ideal. Linear algebra over
L(v), followed by(13), writes the cross product as
psi*(dot x,dot P,dot q) with psi in O. Since the cross-product
components generate O, psi is a unit. Thus, in variable order(x,P,q),
\[
\psi\in L^*,\qquad
W:=(2x\Phi_q-eq\Phi_x)_{\rm ev}=-\psi\dot P.
\tag{14}
\]
The minus sign is the second cross-product component. In particular,
if a=deg_v P>0, then
\[
\boxed{\deg_v W=a-1.}
\tag{15}
\]
When P is constant, W=0 instead. The positive-degree assertion(15)
is not used on that boundary.

Differentiating the FULL expression(11) gives the exact minor ledger
\[
\boxed{W=2D(P)x^2-eD(P)q^2+2xK_q(P,q)-eqT'(P).}
\tag{16}
\]
This is an identity before using Hcal=0. It keeps all lower coefficients
of K. In particular
\[
K_q=J_2(P)+
\left\{\left(e_t-\frac{be_s}{e}\right)P+2c_0\right\}q
+\frac{e_s}{2}q^2.
\tag{17}
\]

## 4. Nonconstant sigma forces equal centered degrees

Assume a=deg_v P>0. Put c=deg_v x and d=deg_v q, assigning degree
minus infinity to a zero polynomial. The nonzero cubic term of T
makes at least one of x,q nonconstant. If c and d are unequal,
the higher of 2c,2d must equal 3a by the third level(9).

### 4.1. The alternative d>c is impossible

Here d=3a/2. If e_s were nonzero, the q^3 term of Phi would have
degree 3d=9a/2, uniquely highest. All other terms in(11),(12)
have degree at most 4a: in particular xPq has degree c+a+d<4a,
Pq^2 has degree4a, and xP^2 has degree less than7a/2.
Thus e_s=0.

With e_s=0, the term -eDq^2 in(16) has degree4a, with leading
coefficient
\[
2e^2 P_*Q_*^2\ne0,\qquad
P_*=\operatorname{lc}_v P,\quad Q_*=\operatorname{lc}_v q.
\tag{18}
\]
It is uniquely highest. Indeed 2Dx^2 has degree at most a+2c<4a,
2xK_q has degree at most max(c+2a,c+a+d)<4a, and eqT' has
degree d+2a=7a/2. This contradicts(15).
The same inequalities cover x constant or zero; its terms then
have still smaller degree or vanish.

### 4.2. The alternative c>d is impossible

Now c=3a/2. In(16), the term 2Dx^2 has the nonzero leading term
-4ePx^2 of degree4a. Every other term has degree strictly less
than4a, except possibly e_s*x*q^2 from(17). In detail, -eDq^2
has degree at most a+2d<4a, xJ2 has degree at most c+2a=7a/2,
the xPq term has degree c+a+d<4a, and eqT' has degree d+2a<7a/2.

If q is zero or constant, the possible competitor e_s*x*q^2
is also strictly lower, so a contradiction is immediate.
Otherwise the only possible leading cancellation requires
\[
e_s\ne0,\qquad c+2d=4a,\qquad d=5a/4.
\tag{19}
\]
These are necessary equalities, not an enumeration of integer triples.

Under(19), the P^4 term is uniquely highest in the full Phi, of
degree4a. It follows that f''''=0. The next top degree is15a/4,
and its only terms are -2ePxq and e_s*q^3/6. Therefore
\[
e_s Q_*^2=12eP_*X_*,
\qquad X_*=\operatorname{lc}_v x\ne0.
\tag{20}
\]
The degree4a coefficient of W is now
\[
-4eP_*X_*^2+e_sX_*Q_*^2
=8eP_*X_*^2\ne0.
\tag{21}
\]
Again this contradicts(15). We divided by Q* only after q had
positive degree and nonzero leading coefficient. No division by
an evaluated polynomial or moving level occurred.

### 4.3. The equal alternative forces e_s=0

The preceding two cases leave
\[
c=d=r>0,\qquad 2r\ge3a.
\tag{22}
\]
If 2r<3a the cubic in T would be uniquely highest, so that
inequality is impossible. In particular r>a.

If e_s were nonzero, e_s*q^3/6 would be the unique highest term
of Phi. Its degree3r is greater than4a because 3r>=9a/2,
and is also greater than a+2r and 2a+r because r>a.
These bound all the other terms in(11),(12). Consequently
\[
\boxed{e_s=0\quad\text{when sigma is nonconstant}.}
\tag{23}
\]
The affine corrections in(7) have intrinsic degree at most a.
Since r>a, they cannot cancel the leading terms of x or q.
Thus deg_v y=deg_v theta=r, proving(3).

## 5. Constant sigma and exact transverse subtraction

Suppose P=sigma belongs to L. The whole return is O=L[x,q].
The centered equation specializes to x^2+(e/2)q^2=-T(P).
For completeness, extend scalars to an algebraic closure M of L
and choose eta in M* with eta^2=-e/2. Then
\[
(x-\eta q)(x+\eta q)=-T(P).
\]
If T(P) is nonzero, both factors are units in M[v], hence constant.
This would make x,q constant and contradict whole generation.
Therefore T(P)=0, and one factor vanishes. The other data then give
M[x,q]=M[q]=M[v], so q has exact degree one. The same holds for x,
because eta is nonzero. Degrees do not change under scalar extension.
Thus x,q,y,theta are all intrinsic-affine over L.

At constant P, every term of(11),(12) now has intrinsic degree
at most two except e_s*q^3/6. The fourth level therefore forces
e_s=0 also in this boundary. This uses a polynomial factorization
and the complete fourth level, not a gradient-unit assertion for
a sliced conic factor.

Combining with(23), e_s=0 throughout the hypotheses(1).
Define by exact subtraction in L
\[
\nu_0=n_s-es,\qquad n_0=n-\frac e2s^2-\nu_0s.
\tag{24}
\]
Their s-derivatives vanish, as does e_s. Hence e,nu0,n0 belong to F,
which proves(2). No integration ansatz or choice of a rational
coefficient-field parameter was made. In particular
b=e_t s+(nu0)_t may still be nonzero or zero.

## 6. Common leading gate and strict-degree alternative

Return to nonconstant P and(22). Let
\[
\eta=\frac{X_*}{Q_*}\in L^*,\qquad
X_*=\operatorname{lc}_v x,\quad Q_*=\operatorname{lc}_v q.
\tag{25}
\]
With e_s=0, the highest possible degree in W is a+2r.
Its coefficient comes precisely from -4ePx^2, 2e^2Pq^2 and
2e_tPxq. Since a+2r>a-1, (15) forces
\[
\boxed{e_t\eta-2e\eta^2+e^2=0.}
\tag{26}
\]
All other terms of W have degree at most max(2r,2a+r), strictly
less than a+2r. Thus no lower coefficient is omitted from this gate.

If 2r>3a, the top third level gives
\[
\eta^2=-e/2,\qquad e_t=4e\eta.
\tag{27}
\]
The second equality follows from(26) by dividing only by eta in L*.
Differentiate the first equality with the EXACT coefficient partials.
Since e_s=0, eta_s=0. Its t-derivative and(27) give
\[
\eta_t=2\eta^2,\qquad
\partial_t\left(t+\frac1{2\eta}\right)=
\partial_s\left(t+\frac1{2\eta}\right)=0.
\]
Joint constants in L are C. Therefore
\[
\boxed{
\eta=-\frac1{2(t-\tau)},\qquad
e=-\frac1{2(t-\tau)^2},\qquad \tau\in\mathbb C
\quad\text{if }2r>3a.}
\tag{28}
\]
The denominator t-tau is nonzero because eta is a nonzero element
of the field. This integration uses the derivative of 1/eta and
joint constants. It does not assume F=C(t), adjoin a square root
to integrate an arbitrary coefficient, or make t-tau an ambient
coordinate. It is a necessary formula for these specific elements.

## 7. Balanced-degree coefficient identities

Suppose instead 2r=3a. The leading third equation says
\[
X_*^2+\frac e2Q_*^2+\frac{f'''}6P_*^3=0.
\tag{29}
\]
Since f''' and P* are nonzero, this gives
\[
\eta^2+e/2\ne0,\qquad
\frac{P_*^3}{Q_*^2}=-\frac{6(\eta^2+e/2)}{f'''}.
\tag{30}
\]
Here a is even and r=3a/2 is integral, but no finite degree list
is inferred.

The top fourth level, of degree4a, is
f''''P_*^4/24-2eP_*X_*Q_*+e_tP_*Q_*^2/2=0.
Divide by nonzero P*Q*^2 and use(30):
\[
-\frac{f''''}{4f'''}(\eta^2+e/2)-2e\eta+e_t/2=0.
\tag{31}
\]
Equation(26) expresses e_t=2e eta-e^2/eta. Substituting it in(31)
factors the entire expression as
\[
-\frac{(\eta^2+e/2)(f''''\eta+4ef''')}{4f'''\eta}=0.
\tag{32}
\]
The first numerator factor is nonzero by(30). Consequently
f''''*eta+4e*f'''=0. In particular f'''' cannot be zero, and
\[
\boxed{
\eta=-\frac{4ef'''}{f''''}\in F^*,\qquad
4f'''f''''\,e_t=e(f'''')^2-32e^2(f''')^2
\quad\text{if }2r=3a.}
\tag{33}
\]
Every division in this step is by a coefficient proved nonzero.
These identities do not classify all algebraic functions satisfying
the differential equation, nor assert that any such functions give
an actual chart.

## 8. Verification and scope

The complete current296,438 and458 sources and the writing guide
were read through EOF before this writeup. Fresh unsaved99f498
reconstructed the complete double centering from the genuine458 H,Q,
with arbitrary compatible coefficient jets and both h derivatives.
It verified(8)--(12), every monomial of K, and the exact minor(16),
with zero residuals.

Fresh5a3bab reconstructed the unequal-degree top forms and(20),(21),
the balanced top levels, the full factorization(32), and the identity
in(33). The written inequalities in Section4, not a bounded numerical
grid, supply the degree argument. The primitive tangent proof uses
whole polynomial-ring generation and the genuine minor UNIT.
The strict integration is the exact joint-constant argument in Section6.

The result proves transverse quadratic dependence(2), the degree
restriction(3), and the necessary strict/balanced gates(28),(33).
It neither assumes nor proves a finite degree frontier by these
arguments alone. It does not use the separate affine-sigma collision
result459, make an original complex coordinate change, exclude all
remaining functions, or recognize the original kernel.

All actual264/296 dependency hypotheses remain retained. A separate
full saved-source review and final held hash belong in the ledger.
No saved checker was executed, imported, compiled or rerun. No
earlier source or canonical index was edited. No unrestricted
cancellation, arbitrary chart entry, actual realization, historical
novelty, external expert review or formal-certification claim is made.

