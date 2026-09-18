# A rank split for equal intrinsic degrees at least two

Working necessary reduction in the complete actual264 chart with
k=s and n_ss nonzero. For equal intrinsic degree d>=2, either the
leading direction has nonzero quadratic curvature, with the precise
degree balance below, or its two directional coefficients both vanish.
The exceptional latter case has d=2 and an exact necessary coefficient
family. The nonexceptional frontier remains open.

No coefficient-field affine change below is asserted to be an original
coordinate transformation. This note proves neither realization of a
remaining family nor a general equal-degree exclusion.

## 1. Actual input and the full shifted quadric

Retain every actual hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
the genuine quadric and cubic with their evaluated unit ideals in
[365](principal-paraboloid-nonlinear-intercept-unequal-degree-gate-pass365-working.md),
and the remaining equal-degree scope of
[400](principal-paraboloid-equal-degree-leading-ratio-obstruction-pass400-working.md).
In particular,
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A_0[u_0],\quad E=\partial_{u_0},
\quad \deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(X^2Z-Y^2)\text{ is the full initial kernel},\quad
0\ne N=[u_0^4]\partial_Z|_{A_0},\\
L=\operatorname{Frac}\ker_{A_0}N,\quad [L:\mathbb C(t,s)]<\infty,
\quad Nv_0=1,\\
O=L[v_0]=L[y,\sigma,\theta]=L[y,z,w],\quad
K=L(v_0)=\mathbb C(y,z,w),\quad k=s,\\
J_{t,s,v_0}(X)=-a_0^4\in L^*,\qquad a_0=EX\ne0.
\end{gathered}
\tag{1}
\]
All original scalar and higher-potential conditions remain imposed.
The exact coefficient partials on L commute and have joint constants C.

Assume
\[
2\le d=\deg\sigma=\deg\theta\le6,\qquad \deg y\le d.
\tag{2}
\]
Degrees are intrinsic v0 degrees over L. Set
\[
\begin{gathered}
\lambda=\frac{[v_0^d]y}{[v_0^d]\sigma},\qquad
\mu=\frac{[v_0^d]\theta}{[v_0^d]\sigma}\in L^*,\\
u_1=y-\lambda\sigma,\quad v_1=\theta-\mu\sigma,
\quad m=\max(\deg u_1,\deg v_1)<d,\\
a=n_t,\quad\nu=n_s,\quad b=n_{ts},\quad c=n_{tt},
\quad e=n_{ss}\ne0,\quad C=\ell_s+\nu^2,\\
\delta=\lambda-\nu,\qquad\beta=b+e\mu,\qquad
j=\delta a-\ell_t-C\mu,\qquad
\mathcal K=\beta^2+2e\delta^2.
\end{gathered}
\tag{3}
\]
Here u1,v1 are lower intrinsic functions, not the original slice or
the intrinsic parameter v0. The slope lambda may be zero. The
separate necessary restriction mu not in C+C*t from400 remains in
force, but is not used to divide any coefficient below.

The highest third-potential coefficient gives
\[
\lambda^2-2\nu\lambda+c/2+b\mu+e\mu^2/2=0.
\tag{4}
\]
Use independent formal variables U1,V1,P and the invertible L-linear
substitution U=lambda*P+U1, V=mu*P+V1 in the full third level.
If h0 is its actual level, its exact expression becomes
\[
H-h_0=P R+q(U_1,V_1),
\quad R=2\delta U_1+\beta V_1+j,
\quad q=U_1^2+aU_1+\tfrac e2V_1^2-CV_1+\nu\ell-h_0.
\tag{5}
\]
It evaluates to zero at(P,U1,V1)=(sigma,u1,v1). All evaluated
gradient and two-gradient-minor unit ideals are preserved under
this invertible formal change. Coefficient derivatives of this
change are not being substituted for formal-variable gradients.
Whole return is exactly O=L[sigma,u1,v1]. Hence m>=1: if both
lower functions were constant, O=L[sigma] would force d=1.

## 2. A zero evaluated R is impossible

First suppose (delta,beta) is not (0,0). If delta=0 and evaluated
R is zero, v1 is constant; equation(5), monic quadratic in u1,
then makes u1 constant as well. This contradicts m>=1.

If delta is nonzero, solve formally U1=(R-beta*V1-j)/(2delta).
Writing k=nu*ell-h0, the complete identity is
\[
\begin{aligned}
H-h_0={}&R\left(P+\frac{R}{4\delta^2}
 -\frac{\beta V_1}{2\delta^2}-\frac j{2\delta^2}
 +\frac a{2\delta}\right)
 +\frac{\mathcal K}{4\delta^2}V_1^2\\
&+\left(\frac{\beta j}{2\delta^2}
             -\frac{a\beta}{2\delta}-C\right)V_1
 +\frac{j^2}{4\delta^2}-\frac{aj}{2\delta}+k.
\end{aligned}
\tag{6}
\]
If evaluated R is zero and Kcal is nonzero, this is a nonzero
quadratic equation over L for v1 in L[v0]. Thus v1 is constant,
and so is u1, a contradiction.

If evaluated R is zero and Kcal is zero, v1 cannot be constant,
again because u1 would also be constant. The remaining affine
polynomial in V1 in(6) must therefore vanish identically. The
ENTIRE formal H-h0 factors as R times the parenthesis in(6).
Along the actual line, every gradient of H is divisible by the
evaluated second factor. The unit-gradient ideal from365 forces
that factor to be a unit in O, hence in L*. But its evaluation
has degree d: its P term is sigma and every other term has degree
at most m<d. This is a contradiction.

It remains to consider delta=beta=0. Here R=j is a coefficient
constant. If j=0, complete the two squares in q:
\[
q=(U_1+a/2)^2+\tfrac e2(V_1-C/e)^2+k_0,
\qquad k_0\in L.
\tag{7}
\]
Over an algebraic closure of L the two square terms factor into
distinct linear factors, since e is nonzero. Their evaluated
product is the scalar -k0. If that scalar is nonzero, both factors
are units in the polynomial ring over the extended field; u1,v1
are constant. If it is zero, one factor evaluates to zero. The
evaluated gradient ideal is generated by the two centered linear
functions in(7). Its being a unit ideal forces the other factor
to be a unit as well, again making both functions constant.
Units and the gradient identity remain valid under the field
extension. Constancy of polynomials originally in L[v0] descends
by coefficient comparison. Both alternatives contradict m>=1.

We have proved in all cases
\[
\boxed{R^{\rm ev}=2\delta u_1+\beta v_1+j\ne0.}
\tag{8}
\]
The factor argument used the FULL formal H and its full gradient
ideal, not a gradient statement about a sliced polynomial.

## 3. Nonexceptional directions have nonzero curvature

Suppose (delta,beta) is not (0,0). If Kcal=0, both delta and beta
must be nonzero, because e is nonzero. In(6) the V1-squared term
vanishes. Put r=deg R^ev>=0. Its first product has degree d+r:
the parenthesis has degree d, whereas its other terms have degree
at most m. The remaining affine polynomial in v1 has degree at
most m<d+r. It cannot cancel that product. Thus Kcal=0 is
impossible, including its previously treated zero-R boundary.

Consequently Kcal is nonzero. Equation(5) gives d+r<=2m. Since
d>m, it follows that r<m. If delta=0, v1 has degree at most r
and u1 has degree m, so q has degree exactly 2m. If beta=0,
the same argument uses u1 of degree at most r and v1 of degree m.
If both are
nonzero, r<m forces both lower functions to have degree m and
their leaders satisfy 2delta*lc(u1)+beta*lc(v1)=0. Their quadratic
term has nonzero leader Kcal*lc(v1)^2/(4delta^2). Thus in every case
\[
\boxed{\mathcal K\ne0,\qquad 0\le r<m<d,\qquad d+r=2m.}
\tag{9}
\]
The homogeneous quadratic-part determinant of the original H is
-Kcal/4, by(4), so this is precisely the rank-three alternative.

If r=0, the nontrivial affine relation between u1,v1 makes both
affine polynomials in one of them, and(5) makes sigma quadratic
in that same function. Whole return then forces this function
to be an affine intrinsic parameter. Hence (r,m,d)=(0,1,2).
For r>=1, the coarse necessary list from(2),(9) is
\[
(r,m,d)\in\{(1,2,3),(1,3,5),(2,3,4),
                 (2,4,6),(3,4,5),(4,5,6)\}.
\tag{10}
\]
This list is not an existence claim or a fresh exclusion of any
entry. In particular no earlier orientation-specific cubic has
been imported by a presumed symmetry.

## 4. The exceptional direction gives a genuine plane quartic

Now suppose delta=beta=0. Then
\[
\lambda=\nu\ne0,\qquad \mu=-b/e,\qquad
c=2\nu^2+b^2/e,\qquad j\in L^*.
\tag{11}
\]
The last assertion follows from Section2. Equation(5) solves
P=-q(U1,V1)/j, and on the actual line proves the polynomial equality
\[
O=L[u_1,v_1].
\tag{12}
\]
Define dot=partial_t+mu*partial_s on L. The exact Legendre
coefficient argument from401 applies to(11), without its additional
degree-one scalar equations: xi=nu is a separating coefficient
parameter, and dot and prime=e^{-1}partial_s are the commuting
partials in(t,xi). With F=ker(dot), it gives A,B in F such that
\[
\begin{gathered}
n-\xi s=\xi^2t^2+At+B,\qquad
s=-2\xi t^2-A't-B',\quad \mu=-4\xi t-A',\\
D:=1/e=-2t^2-A''t-B'',\qquad \dot\mu=-4\xi.
\end{gathered}
\tag{13}
\]
For completeness, dot(n-xi*s)=a, (n-xi*s)'=-s, and dot a=2xi^2
follow directly from(11); their exact integrations yield(13).
This does not impose B''=(A'')^2/8 from401: that identity there
used additional hypotheses which are absent here. The field F is
stable under primes, t is transcendental over F, and L is not
identified with F(t).

Use the complete Q of365, with its actual h0 derivatives retained.
After U=nu*P+U1 and V=mu*P+V1, its P^3, P^2U1 and P^2V1
coefficients vanish. Its coefficients of P^2, PU1V1 and PV1^2 are
respectively
\[
\dot j/2,\qquad -2e,\qquad \dot e/2.
\tag{14}
\]
Here j=-dot ell-mu*nu^2. To check the cancellations directly,
differentiate beta=b+e*mu=0 by dot and use dot mu=-4nu:
b_t+2mu*e_t+mu^2*e_s=4e*nu. Differentiating the quadratic
coefficient relation in(11) gives
n_ttt+3mu*n_tts+3mu^2*n_tss+mu^3*n_sss=0.
Finally dot j=-ell_tt-2mu*ell_ts-mu^2*ell_ss+4nu*C,
which gives the first coefficient in(14). These equations retain
all coefficient derivatives.

Substitute P=-q/j in this FULL polynomial to obtain a plane
polynomial Phi(U1,V1) whose evaluation is a coefficient constant.
Its exact degree is four, with top
\[
\boxed{
\Phi_4=\frac{q_2}{j^2}S_2,\qquad
q_2=U_1^2+\tfrac e2V_1^2,\quad
S_2=\tfrac{\dot j}{2}q_2+2ejU_1V_1
                         -\tfrac{j\dot e}{2}V_1^2.}
\tag{15}
\]
The cross coefficient 2ej in S2 is nonzero, so this quartic is
not zero, including when dot j=0. Every other substituted term
has degree at most three. In particular the full h0_t,h0_s terms
have substituted degree at most two and have not been set to zero.

The plane gradient of Phi generates the unit ideal on O. Indeed
the formal P derivative of H-h0 in(5) is j in this branch. The
plane derivatives after eliminating P are Q_U1-Q_P*q_U1/j and
Q_V1-Q_P*q_V1/j. Multiplication by j identifies them with two
gradient minors; the third minor is their polynomial combination.
Thus the full minor-unit input of365 gives exactly this plane
unit-gradient assertion.

## 5. Whole plane return and the unit cofactor force d=2

Let G be the irreducible kernel equation for the surjection
L[U1,V1] to L[u1,v1]=L[v0]. Its degree is m and its top is a
power of a linear form over L. Here are the precise elementary
one-place facts used. Homogenizing the two generating polynomials
of maximal degree m gives a morphism from the projective parameter
line to their plane closure, with no common zero of its three
coordinates. It is birational onto that closure because the
affine coordinate rings are equal. A generic line pulls back with
degree m, so the image curve has degree m. The line at infinity
pulls back only at the parameter's point at infinity. The image
there is the L-rational leading-coefficient point. Consequently
the top homogeneous equation of the curve is a scalar times the
m-th power of its corresponding L-linear form.

Write Phi-q0=G*K0. The unit plane gradient forces K0(u1,v1) to
be a unit of L[v0], hence some eta0 in L*. Thus K0-eta0 belongs
to the kernel(G), proving
\[
\Phi-q_0=\eta_0G+G^2R_0,\qquad \eta_0\in L^*.
\tag{16}
\]
This is the same whole-plane/unit-cofactor mechanism explained in
[333, Section3](principal-paraboloid-one-variable-first-potential-plane-reduction-pass333-working.md),
now applied to a different fully derived primitive.

Because e is nonzero, q2 in(15) has two distinct linear factors
over an algebraic closure. Hence Phi4 is not a fourth power.
If m=4, (16) forces R0=0 and would give a fourth-power top.
If m=3, R0 nonzero would give degree at least six, while R0=0
would give degree three, not four. If m=2, (16) forces R0 to
be a nonzero constant, again making the quartic top a fourth power.
Larger m is impossible since G divides a quartic; m=0 cannot
generate the intrinsic polynomial line. Therefore m=1. Since
sigma=-q(u1,v1)/j has degree d>m and at most 2m, we have proved
\[
\boxed{\delta=\beta=0,\quad d\ge2
\quad\Longrightarrow\quad d=2,\quad m=1.}
\tag{17}
\]
In particular the exceptional branch is retained, not declared
excluded by the preceding rank-three argument.

## 6. A further exact necessary family in the exceptional branch

Now G is a line. Let its top be the linear form l. Since sigma
has degree two, q2 does not vanish at the leading direction of
(u1,v1), so l does not divide q2. Equation(16) says l^2 divides
Phi4. Formula(15) then forces S2 to be a nonzero scalar times l^2.
Its discriminant must vanish, which is exactly
\[
\boxed{e\dot j^2-2j\dot j\dot e-8e^2j^2=0.}
\tag{18}
\]
This also proves dot j nonzero; otherwise e,j nonzero contradict
(18). No division by dot j was used to obtain the equation.

Set z0=dot j/j, which is nonzero. Using D=1/e from(13), equation
(18) becomes D*z0^2+2*dot(D)*z0-8=0. Define the existing field
element omega=D*z0+dot(D). It satisfies
\[
\omega^2=(A'')^2-8B''\in F.
\tag{19}
\]
An element of L algebraic over its exact dot-constant field has
zero dot derivative: differentiate its separable minimal polynomial.
Thus omega belongs to F. This argument includes a repeated-root
case of(19) and does not adjoin a square root.

Put
\[
T_-=t+(A''-\omega)/4,\qquad
T_+=t+(A''+\omega)/4.
\tag{20}
\]
Both are nonzero because t is transcendental over F. Then
D=-2T_-T_+, z0=-2/T_-, and exact differentiation gives
\[
\boxed{e=-\frac1{2T_-T_+},\qquad
j=\frac{J_0}{T_-^2},\quad J_0\in F^*,\qquad
B''=((A'')^2-\omega^2)/8.}
\tag{21}
\]
These are conclusions about particular elements, not the equality
L=F(t).

There is one more essential zero boundary. The square S2 has
linear factor proportional to U1+V1/(2T_+), because its cross
coefficient and U1-squared coefficient give that ratio. On this
line q2 becomes
\[
q_2\bigl(-V_1/(2T_+),V_1\bigr)
             =-\frac{\omega}{8T_-T_+^2}V_1^2.
\tag{22}
\]
If omega were zero, l would divide q2, contradicting the degree-two
condition used before(18). Therefore omega belongs to F*, not just F.
This excludes that boundary by degree, without dividing it in the
integration. No original coordinate or actual realization has been
constructed from(21).

## 7. Evidence, retained cases and limits

The complete400,395,384 sources were read in29d57e/e8f68e; the
complete365 was freshly read in22518d. The complete401 was read
in2c8417 and independently reconstructed in048ecc/b7ca8c/3ca116.
For this argument the full333 plane-cofactor source was reread
through EOF in feafbb. No unexamined strict-degree Omega conclusion
is transferred to the equal-degree sector.

Fresh unsaved c517ec reconstructed(6), all three cancellations
preceding(14), its exact coefficients, the full quartic top(15)
and the discriminant(18), with zero residuals. The coefficient
relations used there were derived from(11),(13), not sampled
functions or a rational ansatz. Fresh unsaved8c6b33 additionally
verified every identity in(19)--(22), the squared line factor,
and the finite list(10), with zero residuals. The global factor, one-place and
unit-ideal arguments are written above and are not certified by
those finite calculations.

The nonexceptional necessary list(9),(10) remains open here.
The exceptional d=2 family(17)--(22) also remains open; lower
potential equations, the entire calibrated scalar and original
ring returns continue to constrain it. Lambda=0, delta=0 with
beta nonzero, beta=0 with delta nonzero, and both-zero branches
were separated explicitly. No general equality of coefficient
fields, arbitrary-chart entry or original-ring recognition follows.

No saved checker was executed, imported, compiled or rerun by this
author. No earlier source or canonical index was edited. This is
a bounded necessary split, not unrestricted cancellation, novelty,
human-expert verification or formal certification.
