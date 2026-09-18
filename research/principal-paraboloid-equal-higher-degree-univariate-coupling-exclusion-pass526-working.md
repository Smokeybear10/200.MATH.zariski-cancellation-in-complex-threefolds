# Equal higher degrees with univariate coupling are impossible

Working conditional exclusion: under the FULL actual264 chart,
the genuine296 levels and universal494 multiplier, assume
\[
 m=k_s\ne0,\quad m_s=0,\quad \sigma=P,\qquad
 \deg_Py=\deg_P\theta\ge3.
\tag{1}
\]
These hypotheses are inconsistent. The nonzero leading-W case is
the retained exclusion523. This note proves the complementary
zero-leading-W case, including the exceptional cubic left after
the all-X odd-part test.

The final argument uses an ACTUAL polynomial three-ring over
C(X), its local-slice kernel dimension, and inverse-Jacobian
cofactors. It does not require a global slice for the auxiliary
three-ring derivation. There is no claim about unequal intrinsic
degrees, nonzero m_s, nonlinear sigma, or arbitrary chart entry.

## 1. Full actual hypotheses and retained bounded inputs

Retain every actual hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
the genuine levels and unit gradient-minor conclusions of
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md),
and Sections1--3 of
[494](principal-paraboloid-unit-tangent-multiplier-pass494-working.md).
Thus
\[
 \begin{gathered}
 \mathcal B=\mathbb C[X,Y,Z,W]=A[u_{\rm glob}],\quad
 E=\partial_{u_{\rm glob}},\quad X=a_0u_{\rm glob}+x_0,\quad a_0\ne0,\\
 \deg_E(X,Y,Z,W)=(1,2,2,2),\quad
 I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
 \text{ is the FULL initial kernel},\\
 N=[u_{\rm glob}^4]\partial_Z|_A\ne0,\quad
 L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,\\
 Na_0=Nt=Ns=0,\quad P=\sigma,\quad NP=\rho\in L^*,\quad
 O=L[P],\\
 \operatorname{Frac}A=L(P)=\mathbb C(y,z_{\rm int},w),\quad
 L[y,z_{\rm int},w]=L[P],\quad L[X,Y,Z,W]=L[X,P].
 \end{gathered}
\tag{2}
\]
The intercept z_int is the literal original Z-intercept, not its
difference with 2ty. The original slice need not equal X/a_0.
All coefficient derivatives are the exact commuting extensions
from C(t,s) to L, extended to fix P. Every field return and the
all-X polynomial return in (2) remain part of the hypotheses.

Write p=m_t. The complete literal rows are
\[
 \begin{aligned}
 Y&=y+PX+tX^2,\\
 Z&=2ty+P^2+k_tP+m\theta+n+(2tP+k)X+t^2X^2,\\
 W&=w+\theta X+sX^2,\\
 mw&=\ell-(2P+k_t)y-k_{tt}P^2/2-pP\theta-n_tP-n_s\theta,\\
 J_{t,s,P}(Y,Z,W)&=-a_0^4/\rho\in L^*.
 \end{aligned}
\tag{3}
\]
Let d be their common y,theta intrinsic degree, with nonzero
leaders r,a. If omega=-(2r+pa)/m is nonzero, the entire
specified branch is excluded by the retained
[523](principal-paraboloid-equal-higher-degree-nonzero-leading-row-exclusion-pass523-working.md).
We do not reapply that theorem to omega=0.

For omega=0, use the completely read necessary reduction
[524](principal-paraboloid-equal-degree-zero-leading-row-reduction-pass524-working.md).
It gives
\[
 \begin{gathered}
 p\in\mathbb C^*,\quad m=pt+b_0,\quad b_0\in\mathbb C,\quad
 y=-(p/2)\theta+R,\quad R=d_2P^2+d_1P+d_0,\\
 (\deg\theta,\deg R,\deg T)
   \in\{(3,\le1,0),(3,2,1),(4,2,0)\}.
 \end{gathered}
\tag{4}
\]
The first triple includes R=0. The nonzero polynomial T and
complete identities used later are recalled in Section4.
In both quadratic-R cases, 524 also gives d2!=0. No lower
coefficient or potential is assumed rational over C(t,s).

## 2. Normalize m=pt and retain the complete odd parts

The actual complex time translation with tau=b0/p is
\[
 X_*=X,\quad Y_*=Y+\tau X^2,\quad
 Z_*=Z+2\tau Y+\tau^2X^2,\quad W_*=W.
\tag{5}
\]
Its inverse replaces tau by -tau. It preserves the entire
initial relation, since X_*²Z_*-Y_*²=X²Z-Y². It sends
t to t+tau and fixes s,P,a0,rho and the literal selected partial.
The intercept change is complex linear. Therefore both strong
field and polynomial returns, the actual global slice, and the
all-X return survive. Its ambient and parameter determinants
are one. After renaming, m=pt and y=-m theta/(2t)+R.
No division by a coefficient-field expression is an ambient map.

Put k1=k_t, k2=k_tt and D=2td2+1. In the auxiliary coefficient
field extension L(lambda), make the formal substitution
\[
 X_\lambda=-\frac Dt\lambda-d_1-\frac{k_1}{2t},\qquad
 P=\lambda+\xi,\qquad z=\xi^2.
\tag{6}
\]
We never divide by D. Decompose
theta(lambda+xi)=E(lambda,z)+xi O(lambda,z). Define
\[
 \begin{aligned}
 F&=mO+2\lambda+k_1,\\
 c_\lambda&=-(2md_2+p)\lambda-md_1-n_s,\\
 L_{\rm low}&=2d_2z+6d_2\lambda^2
       +(4d_1+2k_1d_2+k_2)\lambda+k_1d_1+2d_0+n_t,\\
 G&=c_\lambda(2\lambda+k_1)+mL_{\rm low},\qquad
 g_{\rm odd}=c_\lambda O-L_{\rm low}.
 \end{aligned}
\tag{7}
\]
Direct substitution of the COMPLETE rows (3) gives
\[
 \operatorname{odd}(Y)=-F/(2t),\qquad
 \operatorname{odd}(Z)=0,\qquad
 \operatorname{odd}(mW)=g_{\rm odd},\qquad
 G=c_\lambda F-mg_{\rm odd}.
\tag{8}
\]
Odd means the coefficient of xi in the unique decomposition
L[z] direct-sum xi L[z]. These formulas are the directly
reconstructed zero-u identities underlying523, not an invocation
of its nonzero-u result. All lower coefficients are retained.

For example, the full Z polynomial is
2tR+P²+k1P+n+(2tP+k)X+t²X². Its odd coefficient vanishes
at (6), including D=0. The coefficient of theta in mW is
mX+(p/2)(2P+k1)-pP-ns; at (6) it is c_lambda, independent
of xi. The remaining odd coefficient is exactly -L_low.

## 3. Resultants and every finite-root case

For cubic theta=aP³+bP²+cP+e, one has
O=a(z+3lambda²)+2b lambda+c. Thus F is linear in z with
constant nonzero leader ma, whereas G has degree at most one
with leader 2md2. For Res_z(F,G)=F1G0-F0G1, including its
constant-polynomial specialization, direct expansion gives
\[
 [\lambda^2]\operatorname{Res}_z(F,G)
       =-2ma(2md_2+p).
\tag{9}
\]
If this is nonzero, the resultant is nonconstant. At any root
lambda0, F retains degree one, so there is a finite common
root in z even if G is constant or the zero polynomial.

For quartic theta=aP⁴+bP³+cP²+eP+h, its odd part is
4a lambda z+4a lambda³+b(z+3lambda²)+2c lambda+e. Both F
and G have degree at most one in z, and
\[
 [\lambda^3]\operatorname{Res}_z(F,G)=-8map\ne0.
\tag{10}
\]
Here d2!=0 by (4), so G has the constant nonzero z leader
2md2. If a resultant root makes F1=0, the identity
F1G0-F0G1=0 then forces F0=0. F is the zero polynomial
and G still has a finite root. Otherwise the usual linear
elimination gives a finite common root. Thus no root at
infinity is being substituted for the needed finite root.

Any such common root is impossible by the all-X return. Indeed,
over an algebraic closure M of L, specialize lambda=lambda0
and X=X_(lambda0) in (2). If z0 is a common root, the ideal
I=(F(lambda0,z),g_odd(lambda0,z)) in M[z] is proper by (8).
Every specialized generator lies in the proper subring
\[
 M[z]\mathbin{\oplus}\xi I\ \subsetneq\ M[\xi],\qquad z=\xi^2,
\tag{11}
\]
whereas the base-changed all-X return requires those generators
to generate M[xi]. The displayed sum is a ring because the
product of two odd terms lies in zI², in the unrestricted even
part. It is proper because xi has odd coefficient one, not in I.
This argument includes z0=0 and D=0. It is a coefficient-field
base change and specialization, not an actual noncomplex root
promoted to an ambient coordinate.

Consequently the quartic case and the cubic case deg R<=1
are excluded, since d2=0 makes (9) nonzero. The only remaining
possibility is
\[
 \deg\theta=3,\quad \deg R=2,\quad
 d_2=-p/(2m),\quad \deg T=1.
\tag{12}
\]
The cubic resultant must now be a nonzero constant in lambda.
It cannot vanish identically, since then any lambda would give
a finite common root. Its linear coefficient therefore vanishes:
\[
 2ad_1m^2-ak_1mp+ak_2m^2-2am n_s+2bmp+2p=0.
\tag{13}
\]
We do not need the value of its remaining nonzero constant.

## 4. Complete scalar gates in the exceptional cubic

Apply the actual complex map W_*=pW, with X,Y,Z fixed.
Its inverse divides W_* by the nonzero complex number p.
Now s_*=ps, theta_*=p theta, m_*=m/p=t and P_*=P. The
coupling p_* is one. The entire initial kernel and both returns
survive this constant scaling. Its ambient determinant and
coefficient parameter determinant are both p, so the scalar
in (3) is unchanged; the literal Z-partial, a0 and rho are
unchanged. All retained scalar identities may be reapplied in
this actual frame, with its transformed coefficients renamed.

Henceforth
\[
 \begin{gathered}
 m=t,\quad p=1,\quad
 \theta=aP^3+bP^2+cP+d,\quad
 R=-P^2/(2t)+eP+f_0,\quad y=-\theta/2+R,\\
 k=ts+f(t),\quad n=s^2/4+n_1(t)s+n_0(t),\quad
 a\in F_0^*,\quad F_0=\ker_L\partial_s,\quad [F_0:\mathbb C(t)]<\infty,\\
 \zeta=(n_s-k_t/2)/t=(n_1-f'/2)/t\in F_0.
 \end{gathered}
\tag{14}
\]
All functions written as functions of t belong to the exact finite
field F0, not necessarily C(t). The coefficients e,f0,c,d may
still move in L. In particular no lower scalar is suppressed.

For explicit use of524, put
\[
 \begin{aligned}
 B_0(P)&=P+n_s,\quad \gamma=2P+k_t,\\
 L_2&=k_{tt}P+n_t-\gamma B_0(P)/t,\\
 M_2&=n_{ts}P-\ell_s-B_0(P)^2/t,\quad
 T&=M_2-L_2/2=T_1P+T_0,\quad T_1=t\zeta_t\ne0,\\
 f_H&=2R+L_2,\qquad
 K=\theta_s-\theta_P/2+R_P+\zeta,\\
 L_R&=R_s-R_P/2+\zeta/2,\qquad
 J_R=(2R+k_{tt}P+n_t+\gamma R_P)/t.
 \end{aligned}
\tag{15}
\]
The complete identities are
\[
 \begin{aligned}
 \mathcal B_1&=\theta_t+\theta_PK+J_R=-\kappa f_H,\\
 \mathcal C&=R_t+R_P^2+\theta_PL_R+J_R/2=\kappa T,\\
 \mathcal W&=-L_Rf_H^2+
       (2R_P-K+D_f/2)f_HT+(\theta_P+D_f)T^2\in L^*,\qquad
 D_f=(2P+k_t)/t.
 \end{aligned}
\tag{16}
\]
The full H level is R²+L2R+N3+T theta=0, with deg N3<=3.
Its degree-four coefficient gives
\[
 aT_1=-5/(4t^2).
\tag{17}
\]
The first equation in (16) forces deg K<=1, as in524; write
K=K1P+K0. The second forces L_R to be constant in P. Its
degree-two coefficient is exactly
\[
 (1/(2t^2))+4(1/(4t^2))-3/(2t^2)+3aL_R=3aL_R.
\]
Thus L_R=0. In particular e_s=-1/(2t). The full minor in
(16), after (17), has degree-four coefficient
\[
 \frac{3T_1}{4t^2}(4tK_1-1)=0.
\tag{18}
\]
This uses the exact leader [P²]f_H=-3/t, and no lower term
can reach that coefficient. Consequently
\[
 K_1=1/(4t),\quad c_s=b+5/(4t),\quad
 a_t=-3a/(4t).
\tag{19}
\]
The last equation is the full degree-three coefficient
a_t+3aK1=0 of B1. The degree-two condition on K also says
b_s=3a/2. These are full scalar consequences, not formal
constant-coefficient assumptions.

Equations (17),(19) and T1=t*zeta_t give an existing-field
primitive:
\[
 \zeta_t=-5/(4at^3)
      =\left(1/(at^2)\right)_t,\qquad
 \zeta=1/(at^2)+\zeta_0,\quad \zeta_0\in\mathbb C.
\tag{20}
\]
Both summands are in F0, whose t-constants are C. No algebraic
root has been adjoined or promoted to an actual coordinate.

Finally (13), in this normalized frame, is the exact relation
\[
 e=\frac{k_t}{2t}-\frac{k_{tt}}2+\frac{n_s}{t}
                  -\frac{b}{at}-\frac1{at^2}.
\tag{21}
\]

## 5. An actual polynomial frame of degrees (1,2,3)

Make the actual triangular change
\[
 U=W+2(X-\zeta_0)Y,\qquad W=U-2(X-\zeta_0)Y.
\tag{22}
\]
It has determinant one. We do NOT assert that this later map
preserves the original time profile1222. That assertion is not
needed: it is an actual polynomial coordinate change, fixes X,
and supplies the same polynomial three-ring over C(X).

Define
\[
 A_X=2tX+B(t),\qquad B(t)=2te+k_t\in F_0.
\tag{23}
\]
The membership follows from e_s=-1/(2t) and (k_t)_s=1.
The entire literal Z row in (3) has P² coefficient zero
and P coefficient A_X. Since its X coefficient is 2t!=0,
this is an exact intrinsic degree one over L(X).

For clarity the full expression for U, before taking coefficients,
is
\[
 \begin{aligned}
 U={}&-\frac{\theta}{at^2}
       -\frac{(2P+k_t)R}{t}
       -\frac{k_{tt}P^2/2+n_tP-\ell}{t}
       +2(X-\zeta_0)R\\
    &+2(X-\zeta_0)PX+sX^2+2t(X-\zeta_0)X^2.
 \end{aligned}
\tag{24}
\]
Its cubic terms cancel. Using exactly (21), its quadratic
coefficient is -A_X/(2t²). Thus the actual ordered coordinates
(Z,U,Y), over K=C(X), have degrees and leaders
\[
 (1,2,3),\qquad
 \left(A_X,-\frac{A_X}{2t^2},-\frac a2\right).
\tag{25}
\]
No specialization of X or removal of a coefficient-field
denominator was used to assert these exact degrees.

Extend N from A to B=A[u_glob] by killing u_glob and define
Delta=a0N-(NX)E. It is an actual polynomial derivation that
kills X. On B_(a0)=A_(a0)[X] it acts as a0N on A_(a0),
so it is locally nilpotent there, hence on B. It remains a
nonzero LND after localizing in nonzero polynomials in X.
Therefore
\[
 \mathscr R=K[Z,U,Y]\subset F[P],\quad K=\mathbb C(X),\quad
 F=L(X),\quad \operatorname{Frac}\mathscr R=F(P),\quad
 \Delta=a_0\rho\partial_P.
\tag{26}
\]
The coefficient field F is finite separable over K(t,s).
The row transformation (22) and even cyclic permutation to
(Z,U,Y) preserve the scalar Jacobian in (3). The original
global slice is not a presumed global slice for Delta.

## 6. A complete cofactor bound for this actual three-ring

Let eta be independent over F and consider the full leading map
\[
 K[\mathsf Z,\mathsf U,\mathsf Y]\longrightarrow F[\eta],\quad
 (\mathsf Z,\mathsf U,\mathsf Y)\longmapsto
 \left(A_X\eta,-A_X\eta^2/(2t^2),-a\eta^3/2\right).
\tag{27}
\]
The first two images are algebraically independent over K. Their
degree-zero ratio is mu=-1/(2t² A_X). Its t derivative is
nonzero: the X coefficient of (t² A_X)_t is 6t². Any element
algebraic over K has zero t derivative, by differentiating its
separable minimal polynomial. Hence mu is transcendental over K.
The eta powers then prove the asserted independence, by grouping
a polynomial relation into its weighted homogeneous components.

The nonzero LND Delta has two algebraically independent polynomial
invariants over K. To recall the local argument, choose b with
Delta b!=0 and Delta²b=0, put h=Delta b, and localize at the
invariant h. Then b/h is a slice there; finite Taylor projection
gives R_h=(ker Delta)_h[b/h]. Thus the fraction field of the
kernel has transcendence degree two. No global slice or finite
generation of the kernel is required.

A nonconstant polynomial invariant has P degree zero, so its
positive source-weight top supplies a nonzero relation in (27).
Together with independence of the first two images, this shows
the FULL leading kernel is height one. The kernel is graded,
since different weighted components give distinct eta powers.
The source UFD therefore gives a generator H irreducible and
weighted homogeneous of weight D for weights(1,2,3).
H must involve mathsf Y.

Use the ACTUAL coordinate partial partial_Y at fixed Z,U over K.
Since the scalar Jacobian belongs to F*, inverse cofactors give
\[
 \deg_P(\partial_Yt),\deg_P(\partial_Ys)\le2,\qquad
 \deg_P(\partial_YP)\le3.
\tag{28}
\]
The first bound is 1+2-1: each cofactor contains a P derivative.
The last cofactor uses two coefficient derivatives. The exact
chain rule on F(P), using its finite separating presentation,
therefore gives for every f in F[P]
\[
 \deg_P(\partial_Y f)\le\deg_P f+2.
\tag{29}
\]
The P derivative of f lowers its degree by one, so (29) does
not require the stronger false estimate deg(partial_Y P)<=2.
Actual partial_Y preserves the polynomial three-ring, and its
iterates may be used in this bound.

Take any nonconstant polynomial invariant f, and let M>0 be its
source weight. Write its weighted top as H^ell G with ell>=1
and H not dividing G. In characteristic zero, H_Y is nonzero
modulo H. The ell-th actual Y derivative of that top is,
modulo H, exactly ell!*G*(H_Y)^ell, nonzero. Lower-weight
terms remain lower after differentiation. Consequently its
P degree is exactly M-3ell. On the other hand (29), starting
from degree_P f=0, bounds it by 2ell. Hence
\[
 D\ell\le M\le5\ell,\qquad D\le5.
\tag{30}
\]
If D=5, equality forces G to have weight zero, so to be a scalar
in K. Thus every nonconstant invariant has weighted top a scalar
power of H. Because all coordinate weights are positive, the
source-weight filtration of the invariant ring has dimension at
most 1+floor(N/5) through weight N. Two algebraically independent
polynomial invariants instead give (n+1)² independent monomials
through a weight growing only linearly with n. This contradiction
excludes equality. We have proved, for this actual three-ring,
\[
 D\le4.
\tag{31}
\]
This is a cofactor and kernel-growth proof, not an application
of a sliced four-ring theorem to an unsliced three-ring.

## 7. Both coefficient-field X-root cases contradict the scalar ODE

Since the first two initials in (27) are independent, D cannot
be one or two. A relation of weight three has a nonzero constant
coefficient on mathsf Y and a binary weighted cubic. A relation
of weight four has a nonzero scalar multiple of mathsf Z as
its Y coefficient and a binary weighted quartic. Normalizing
that nonzero scalar and evaluating either form gives
\[
 a=\alpha(X)A_X^3+\beta(X)A_X^2/t^2
                       +\gamma(X)A_X/t^4,\qquad
 \alpha,\beta,\gamma\in\mathbb C(X).
\tag{32}
\]
For weight three the last coefficient is zero. For weight four,
this identity follows after division by A_X in the fraction
field, where A_X is nonzero. No polynomial nonunit is inverted
to assert a ring-generation statement.

Set x0=-B(t)/(2t) in F0. If x0 is not complex, it is
transcendental over C. Every nonzero polynomial denominator
from C[X] in (32) stays nonzero at X=x0. Thus the rational
identity (32) may be evaluated in the coefficient field there.
Its right side vanishes because A_(x0)=0, contradicting a!=0.
This is evaluation of a proved rational identity in F0(X),
not an actual noncomplex ambient fiber claim.

Therefore x0 is complex and B(t)=c0*t for some c0 in C.
Then A_X=t(2X+c0). Choose a complex X value avoiding the
finitely many poles in (32) and the zero of 2X+c0. Evaluating
(32) gives constants alpha0,beta0,gamma0 in C such that
\[
 a=\alpha_0t^3+\beta_0+\gamma_0t^{-3}.
\tag{33}
\]
Apply t*partial_t+3/4, using the actual scalar consequence
a_t=-3a/(4t) in (19). The three coefficients become
15alpha0/4, 3beta0/4 and -9gamma0/4. Algebraic independence
of t over C forces all three to vanish. Equation (33) would
then give a=0, the final contradiction.

This excludes the exceptional cubic (12), and hence all three
zero-leading-row triples in524. Combining with retained523
proves exactly the conditional exclusion (1).

## 8. Verification and exact scope

The entire held523 source was read through EOF65ccef+ae55b1,
at SHA98ecbf667f65692c3b6bb7ace2ce38d64fef6e4506922df30ecd8f9df84afc68.
The entire524 input was authored and reread through EOFdb2b28+
292193 at its held SHA1102b922b21b8da44b9eaa11e1e6b3fcbceef827dcbbdad35423266a4298b173.
Their retained earlier dependencies are not recursively certified
by this note. The original264,296 and universal494 equations
were directly read for the full-row and exact-field licenses.

Fresh unsaved60f356 reconstructed all THREE complete odd parts
in (8), for cubic and quartic theta with unrestricted lower
coefficients, directly from the literal rows with m=pt. Every
residual was zero. Fresh da0513 checked the full zero-u resultants
(9),(10), the exceptional linear coefficient (13), both entire
Z/U leading cancellations, the complete C/W gates (17)--(19),
and the exact primitive (20), with all residuals zero. The
remaining argument is the explicit field, cofactor, derivative
and filtration proof above, not a finite numerical test.

The later shear (22) is used only as an actual three-ring frame;
no unchanged1222 profile is claimed after it. All finite algebraic
coefficient extensions, moving lower coefficients, zero resultant
degree cases, and finite-root guards are retained. No global
slice for Delta, rationality of F0 or L, or actual root-coordinate
change is presumed.

No saved checker was executed, imported, compiled or rerun. No
earlier source or canonical file was edited. This excludes only
the stated equal-degree, univariate-coupling, affine-sigma chart
sector. It is not arbitrary entry, unrestricted cancellation,
a novelty assertion or external certification.
