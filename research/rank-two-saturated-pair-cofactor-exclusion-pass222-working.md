# Saturated pair directions and the double-simple-simple quartic

Status: bounded working exclusion for supplied actual rank-two quartic
frames. A universal differentiated eliminant bounds its evaluated
cofactor by the cube of the return polynomial. If the projected curve
uses the entire multiplicity of a simple or double leading pair factor,
the exact degree of that cofactor contradicts this bound.

This supplies another squarefree-sector exclusion and, with an actual
normalization of the remaining pair lines, excludes the root partition
2+1+1. It does not exclude the partition 3+1 or arbitrary initial kernels.
No projected coordinate is asserted to descend merely because it is a
variable over the coefficient field.

## 1. Exact actual inputs

Assume an actual globally sliced frame
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad A=\ker E,\\
\deg_E(X,Y,Z,W)=(1,1,2,2),\qquad
a=EX,\ b=EY,\ e_0=E^2Z/2,\ h_0=E^2W/2,\\
\ker\bigl((\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
 \mapsto(aT,bT,e_0T^2,h_0T^2)\bigr)
=(\mathsf Z\mathsf W-F_4(\mathsf X,\mathsf Y)),
\end{gathered}
\tag{1}
\]
where T is independent and F4 is a nonzero complex binary quartic.
The initial ideal is full, and the capital letters are actual polynomial
coordinates. The time profile is not an assumption about ordinary
coefficient degrees or a global minimum.

The literal Z pivot and the actual construction in
[universal184](weight-four-universal-chart-potentials-pass184-working.md)
give
\[
\begin{gathered}
N=[u^3](\partial_Z|_A)\ne0,\quad
L=\operatorname{Frac}(\ker_A N),\quad A_L=L[v],\quad Nv=1,\\
t=b/a,\quad \rho=h_0/a^2,\quad s(t)=F_4(1,t),\quad
q=e_0/a^2=s(t)/\rho,\quad [L:\mathbb C(t,\rho)]<\infty,\\
Y=y+tX,\quad Z=z+\sigma X+qX^2,\quad
W=w+\vartheta X+\rho X^2,\\
L[y,z,w]=L[v],\qquad J_0=-a^3\in L^* .
\end{gathered}
\tag{2}
\]
The ratios t,rho are algebraically independent. Coefficient partials
extend uniquely and commute on the exact finite field L, then fix v.
Neither rationality of L nor an original-ring unit speed is assumed.

Use independent formal variables U,V and the coefficient Taylor
polynomials H_j from universal184. Set
\[
\begin{gathered}
f=H_2(q)+H_1(k)+n,\quad \mathcal R=f_V,\quad c=f_\rho,
\quad A_2=q_{\rho\rho}/2=s(t)/\rho^3,\\
S=H_3(q)+H_2(k)+H_1(n),\quad T_0=\ell-S,\\
Q=H_4(q)+H_3(k)+H_2(n)-\ell_tU-\ell_\rho V-m,
\qquad k,n,\ell,m\in L .
\end{gathered}
\tag{3}
\]
The exact potentials are
\[
z=q_\rho w+f(y,\vartheta),\qquad
Rw=T_0(y,\vartheta),\qquad
A_2w^2+c(y,\vartheta)w+Q(y,\vartheta)=0,
\quad R=\mathcal R(y,\vartheta).
\tag{4}
\]
In Sections2--4 assume R is not identically zero in L[v]. This is not
a root-free assumption. As proved in
[general quartic220](rank-two-binary-quartic-leading-sextic-pass220-working.md),
the nonzero scalar A2 and the full return in (2) imply
\[
\begin{gathered}
\mathcal C=L[y,\vartheta]\subset\mathcal O=L[v],\quad
\mathcal O=\mathcal C[w]=\mathcal C+\mathcal Cw,\quad
R\mathcal O\subset\mathcal C,\\
\operatorname{Frac}\mathcal C=L(v).
\end{gathered}
\tag{5}
\]
In particular the evaluation kernel in L[U,V] has one irreducible
generator Gamma. Normality of C is not assumed.

## 2. The gradients are universal, not special to the mixed ratio

Define the formal eliminant
\[
\mathcal H=A_2T_0^2+\mathcal R cT_0+\mathcal R^2Q,
\qquad \mathcal H(y,\vartheta)=0.
\tag{6}
\]
All formal U,V derivatives below fix the coefficient field. Define the
evaluated expressions
\[
\begin{gathered}
B_1=f_t(y,\vartheta)+q_{t\rho}w,\qquad
C_1=c(y,\vartheta)+q_{\rho\rho}w,\\
\Lambda_i=\ell_i-S_i(y,\vartheta)-\mathcal R_i(y,\vartheta)w,
\qquad i=t,\rho .
\end{gathered}
\tag{7}
\]
In Lambda, each coefficient derivative is taken before evaluation;
it is not the total derivative of the evaluated polynomial.

For arbitrary q in the universal coefficient field, the definitions give
\[
\begin{gathered}
S_U=f_t,\quad S_V=c,\quad
\mathcal R_U=q_{t\rho},\quad \mathcal R_V=2A_2,\\
c_U=\mathcal R_t,\quad c_V=\mathcal R_\rho,\quad
Q_U=S_t-\ell_t,\quad Q_V=S_\rho-\ell_\rho .
\end{gathered}
\tag{8}
\]
Differentiate (6) formally, and only then substitute T0=Rw and
Q=-A2 w squared-cw from (4). Using (8), every term involving
R_t w or R_rho w cancels. The resulting polynomial identities are
\[
\boxed{
\mathcal H_U(y,\vartheta)
 =-R(C_1B_1+R\Lambda_t),\qquad
\mathcal H_V(y,\vartheta)
 =-R(C_1^2+R\Lambda_\rho).}
\tag{9}
\]
For example the U derivative, after substitution, is
\(-R(c+2A_2w)(f_t+\mathcal R_Uw)-R^2\Lambda_t\).
This is the first formula in (9); the V derivative uses
\(\mathcal R_V=2A_2\). No assumption q_t=0, special quadratic
Hessian, or mixed-quartic factorization enters this calculation.

## 3. Calibrated wedge and the evaluated cofactor divisor

The actual universal identities supply
\[
\begin{gathered}
R\,dw=-B_1dy-C_1d\vartheta+\Lambda_tdt+\Lambda_\rho d\rho,\\
J_0=\left[dy\wedge(Rd\vartheta+B_1dt+C_1d\rho)\wedge dw
     \right]_{dt\wedge d\rho\wedge dv}=-a^3.
\end{gathered}
\tag{10}
\]
Here differentials are total, unlike the formal derivatives in (8).
Put
\[
\begin{aligned}
D_U&=R(y_v\vartheta_\rho-y_\rho\vartheta_v)+C_1y_v,\\
D_V&=R(y_t\vartheta_v-y_v\vartheta_t)-B_1y_v.
\end{aligned}
\tag{11}
\]
An expansion of (10), followed by (9), gives the undivided identity
\[
\boxed{R^3J_0=D_U\mathcal H_U(y,\vartheta)
                   +D_V\mathcal H_V(y,\vartheta).}
\tag{12}
\]
For an explicit sign check, write
\(A=y_v\vartheta_\rho-y_\rho\vartheta_v\) and
\(B=y_t\vartheta_v-y_v\vartheta_t\) for this sentence only.
Expanding the first equality in (10) inside its wedge gives
\(RJ_0=-(R\Lambda_t+B_1C_1)A
 -(R\Lambda_\rho+C_1^2)B+y_v(B_1\Lambda_\rho-C_1\Lambda_t)\).
Substituting (9) and (11) on the right of (12) gives exactly
R squared times this expression. Thus the signs and the power R cubed
hold for arbitrary universal q.

For the specialization (2), general quartic220 proves that H has
nonzero total degree six. Since Gamma generates the evaluation kernel,
Gamma divides H. Its multiplicity in H is one: if it were at least
two, both evaluated formal gradients would vanish, contradicting (12)
and the nonzero elements R,J0. We can therefore write
\[
\mathcal H=\Gamma Q_1,\qquad
0\ne q_1:=Q_1(y,\vartheta),\qquad
q_1\mid R^3\quad\hbox{in }L[v].
\tag{13}
\]
Indeed the evaluated gradients are q1 times the corresponding gradients
of Gamma, so (12) proves the divisibility because J0 is a unit in L.
This is divisibility in the actual normalization ring O, not an assertion
that q1 is an original-ring polynomial unit.

## 4. Exact degree when the selected top factor is exhausted

Factor F4 into four complex linear root forms, with proportional copies
retained. Write ell_i(t)=ell_i(1,t). The established leading identity is
\[
\mathcal H_6=-\rho^{-11}\prod_{i<j}
 \{\ell_i\ell_jV-\rho(\ell_i'\ell_j+\ell_i\ell_j')U\}.
\tag{14}
\]
All six factors are nonzero; the only proportionalities correspond to
equal unordered multisets of two projective roots. The complete
characteristic-polynomial argument in general quartic220, using (5), gives
\[
g:=\deg\Gamma=\max(\deg_v y,\deg_v\vartheta),\qquad
\Gamma_g=c_0\ell(U,V)^g,
\tag{15}
\]
where c0 is a nonzero scalar in L and ell is one of the distinct pair
directions in (14). Let m be its multiplicity in H6. Necessarily g<=m.

Suppose g=m. The homogeneous top of Q1 has degree 6-g and is the quotient
of H6 by c0 ell to the power g. It consequently has no ell factor.
Let (u_g,v_g) be the two coefficients of the parameter v to degree g
in (y,vartheta); at least one is nonzero. The relation Gamma(y,vartheta)=0
forces ell(u_g,v_g)=0. Every other distinct linear pair factor is nonzero
on that vector, since two distinct lines through zero intersect only
at zero. Therefore the leading coefficient of the evaluated cofactor
does not vanish, and
\[
\deg_v q_1=(6-g)g,\qquad
\deg_vR\le g,\qquad
(6-g)g\le3\deg_vR\le3g.
\tag{16}
\]
The middle bound holds because the formal R=f_V is affine in U,V.
The leftmost degree is an equality, not a generic estimate. Lower
homogeneous terms of Q1 have evaluated degree at most (5-g)g and
cannot cancel it. Thus
\[
\boxed{g=m<3\quad\hbox{is impossible}.}
\tag{17}
\]
No normalization or nonsingularity of the plane ring C was needed.
For g=m=3, the inequality is an equality rather than a contradiction.
It would imply deg R=3 and q1 a scalar multiple of R cubed, but this
does not exclude that branch. In particular the partition 3+1 remains
outside the conclusions below.

## 5. Exhausting the partition 2+1+1

Suppose F4 has one double and two distinct simple projective roots.
It is not a square, so
[zero return221](rank-two-nonsquare-quartic-zero-return-exclusion-pass221-working.md)
forces R nonzero. The pair-factor multiplicities in (14) are 2,2,1,1.
The multiplicity-one directions come from the doubled root paired
with itself and from the two simple roots paired together. Their
possible components have g=1, and (17) excludes them.

Each multiplicity-two direction pairs the double root with one of
the simple roots. It permits g=1 or g=2. Equation (17) excludes
g=2. It remains to exclude a line in such a double/simple pair direction.

Choose the actual new first coordinate X' to be the simple root form
and Y' to be the double root form. More explicitly, write
\[
X'=\alpha X+\beta Y,\quad Y'=\gamma X+\delta Y,\quad
d=\alpha\delta-\beta\gamma\ne0,
\quad l=\alpha+\beta t,\quad m=\gamma+\delta t.
\tag{18}
\]
Keep Z,W fixed. The inverse is
\(X=(\delta X'-\beta Y')/d\),
\(Y=(-\gamma X'+\alpha Y')/d\). Both changed good degrees remain
one because t is transcendental. The full initial ideal transforms by
the same actual polynomial automorphism. The literal Z pivot, N and L
are unchanged, while all chart quantities and the auxiliary derivation
are rebuilt; we do not assert preservation of the old R or P.

The exact transport from squarefree-line221 uses only the independence
of these two root forms, not squarefreeness of all four roots:
\[
\begin{gathered}
t'=m/l,\quad \rho'=\rho/l^2,\quad
y'=d y/l,\quad \vartheta'=\vartheta/l-2\rho\beta y/l^2,\\
y'-(t'/\rho')\vartheta'
 =-\{lm\vartheta-\rho(\beta m+\delta l)y\}/(\rho l).
\end{gathered}
\tag{19}
\]
The numerator is constant in L along the selected line. The projected
linear transformation is invertible, so the new pair still generates
L[v]. Dropping stars yields exactly
\[
F_4=XY^2(\alpha_0Y+\beta_0X),\quad
\alpha_0\beta_0\ne0,\quad
q=(\alpha_0t^3+\beta_0t^2)/\rho,\quad
y=h\vartheta+\nu,\ h=t/\rho,\ \nu\in L,
\quad\deg_v\vartheta=1.
\tag{20}
\]
Here alpha0,beta0 are complex constants. They are nonzero because
the remaining simple root differs from both chosen roots.

## 6. The local Wang contradiction still applies when gamma0 is zero

The normalized calculation in
[squarefree-line221](rank-two-squarefree-quartic-line-exclusion-pass221-working.md)
was recorded with an additional term gamma0 t in the numerator of q.
The following direct calculation verifies the precise gamma0=0 extension,
without importing that note's squarefree global conclusion.

Put D_rad=h partial_t+partial_rho, so D_rad h=0. For (20),
D_rad squared q=2 alpha0 h cubed and D_rad cubed q=0. Also the
coefficient of vartheta in the new evaluated return is
\(-\alpha_0t^3/\rho^3\ne0\). The third potential therefore makes w
affine in vartheta, and the second gives
\[
\begin{gathered}
w=\lambda\vartheta+\omega,\quad
z=\alpha_0h^3\vartheta^2+\kappa\vartheta+\zeta,\\
\sigma=(2\alpha_0h^3\rho+\beta_0h^2)\vartheta+q_t\nu+k,
\qquad \lambda,\omega,\kappa,\zeta\in L.
\end{gathered}
\tag{21}
\]
Indeed the cubic directional term of H3(q) vanishes, whereas the
quadratic directional term of H2(q) is alpha0 h cubed. Since theta
is affine, the third potential has numerator of degree at most two
and denominator R of degree one in theta; its polynomial solution w
must have degree at most one.

The actual derivation P=aN-(NX)E fixes X and L and is locally nilpotent
by the same B_a=A_a[X] argument as in221. Put tau=aN vartheta in L*.
Its actual components have
\[
\mathcal PY=\tau h,\qquad
\mathcal PW=\tau(X+\lambda),\qquad
\mathcal P^2Z=2\alpha_0h^3\tau^2\ne0,\qquad
\mathcal P^2Y=\mathcal P^2W=\mathcal P^3Z=0.
\tag{22}
\]
Divide by the gcd Delta of its original polynomial components. The
LND-degree argument PDelta=Delta DDelta forces PDelta=DDelta=0.
Thus D=P/Delta is an irreducible LND with the displayed derivative
orders. Localization at C[X] preserves irreducibility by Gauss
factorization. Over K=C(X), it is an irreducible LND of K[Y,Z,W]
with the two good coordinates Y,W.

Apply exactly the alternatives of
[Dasgupta--Gupta Theorem4.1](https://arxiv.org/html/1701.03635v1#S4.Thm1),
their stated version of Wang's theorem. The first fixes a nonzero
K-linear form in Y,W; the second retains Y,W and supplies an invariant
coordinate. The ratio (DW)/(DY)=(X+lambda)/h is transcendental over K.
To see this, normalize it by X, clear a hypothetical polynomial
relation's denominators in C[X], and compare its highest Laurent power
at infinity. Its coefficient is a nonzero complex polynomial in 1/h,
impossible because h=t/rho is transcendental. This excludes the first
alternative.

In the second, the invariant coordinate has form uZ+Q2(Y,W) with
u in K*. This follows from degrees of the two inverse expressions
in the single polynomial variable Z over K[Y,W]. After scaling u,
use Z+Q2. A nonzero homogeneous polynomial of degree j in the good
variables has nonzero j-th derivative: it equals j factorial times
that polynomial evaluated at DY,DW. Transcendence of their ratio
prevents its vanishing. Hence the ordinary degree of Q2 is exactly
two, since Z has exact D-degree two. Taking D squared of the invariant
coordinate and dividing only in the fraction field gives
\[
\alpha_0h^3+A(X)h^2+B(X)h(X+\lambda)+C(X)(X+\lambda)^2=0,
\qquad A,B,C\in\mathbb C(X).
\tag{23}
\]
No tau or Delta is assumed to be an original-ring unit.

Let n be the maximum of the leading Laurent exponents at X infinity
of A, of B plus one, and of C plus two, ignoring zero terms. If n>0,
the coefficient at that power is a nonzero complex linear combination
of h squared,h,1, a contradiction. Terms involving lambda occur only
at lower powers. If n<=0, the constant Laurent coefficient is instead
alpha0 h cubed plus a complex polynomial in h of degree at most two,
again impossible. Thus both Wang alternatives fail for the actual
primitive derivation. Every remaining double/simple pair line is excluded.

## 7. Conclusions and boundaries

There is no supplied actual frame (1) when F4 has root partition 2+1+1.
The proof exhausts R=0 by221, both simple pair lines by (17), both
double pair conics by (17), and their remaining lines by Sections5--6.

For squarefree F4,221 also gives R nonzero, while220 gives g=1 and
every pair factor has multiplicity one. Equation (17) therefore gives
an independent squarefree-sector exclusion without Wang's theorem.
It does not depend on the separate quadratic-ratio constant-second222
argument.

The equality case g=m=3 is explicitly not excluded by the degree
argument. Root partition 3+1, other unresolved supplied sectors,
height-two initial kernels, arbitrary frame entry and unrestricted
complex-threefold cancellation are not settled here. No coefficient
field scalar has been used as an unauthorized ambient coordinate change.

Universal184, general quartic220, zero-return221 and the complete saved
squarefree-line221 proof were freshly read or retained as full source
reviews before use. The exact Wang statement was freshly checked.
The universal gradient and wedge identities and the exact cofactor-degree
gate were independently reconstructed by Root and General. These are
written AI checks, not expert or proof-assistant certification. No saved
checker was executed, imported, or compiled, and no prior source, index,
or verification packet was changed. No historical novelty claim is made.
