# Cubic intrinsic slope with transverse coupling is impossible

Working conditional exclusion: retain the FULL actual chart264,
its genuine296 consequences and universal494 identities. If sigma
is affine nonconstant in the intrinsic line parameter, then
\[
\boxed{m=k_s\ne0,\quad h=m_s\ne0,\quad P=\sigma,
       \quad\deg_P\theta=3\quad\text{are inconsistent}.}
\tag{1}
\]
The accepted degree bound521 first gives deg_P(y)<=3. The direct
argument below then uses only the complete first two potential
rows and the all-X polynomial return. It does not use another H
level, scalar coefficient, gradient minor or recognition theorem.

The key specialization is chosen AFTER a common root is found.
No expression X=-O_y(lambda,z) is used as an actual coordinate
change, or as a fixed-X polynomial frame before choosing that root.
Zero, constant, linear, quadratic and cubic y are all included.

## 1. Actual pedigree and the direct algebraic proposition

Retain every hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
with the genuine levels and unit ideals of
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md)
and Sections1--3 of
[494](principal-paraboloid-unit-tangent-multiplier-pass494-working.md).
In particular,
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u_{\rm glob}],\quad
E=\partial_{u_{\rm glob}},\quad X=a_0u_{\rm glob}+x_0,\quad a_0\ne0,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\quad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the ENTIRE initial kernel},\\
N=[u_{\rm glob}^4]\partial_Z|_A\ne0,\quad
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,\\
Na_0=Nt=Ns=0,\quad P=\sigma,\quad NP=\rho\in L^*,\quad
O=L[A]=L[P],\\
\operatorname{Frac}A=L(P)=\mathbb C(y,z_{\rm int},w),\quad
L[y,z_{\rm int},w]=L[P],\quad
L[X,Y,Z,W]=L[X,P].
\end{gathered}
\tag{2}
\]
The intercept z_int is the literal original Z-intercept, not
z_int-2ty. The original global slice is not assumed to be X/a0.
The last return also follows directly from
L[mathcal B]=L[P,u_glob] and X=a0*u_glob+x0: a0 is a unit
of L and x0 belongs to L[P]. This uses no new ambient coordinate.

The coefficient partials on L are the exact commuting extensions
from C(t,s), extended to fix P. Write
\[
m=k_s,\quad h=m_s,\quad p=m_t,\quad k_1=k_t,\quad k_2=k_{tt}.
\tag{3}
\]
The first two full potentials in264 give the literal rows
\[
\begin{aligned}
Y={}&y+PX+tX^2,\\
Z={}&2ty+P^2+k_1P+m\theta+n+(2tP+k)X+t^2X^2,\\
mW={}&(mX-pP-n_s)\theta-\frac h2\theta^2
       +\ell-(2P+k_1)y-\frac{k_2}2P^2-n_tP+msX^2.
\end{aligned}
\tag{4}
\]
These follow from z_int=2ty+P^2+k1*P+m*theta+n and
mw+(2P+k1)y+F(P,theta)=ell, where
F=k2*P^2/2+p*P*V+h*V^2/2+n_t*P+n_s*V.
In particular the ENTIRE quadratic-in-theta contribution to W
has been retained. All lower potentials and coefficients move
freely unless one of the actual hypotheses already restricts them.

The original calibrated determinant in this parameter is
J_(t,s,P)=-a0^4/rho in L*. Its speed rho is not set to one.
That scalar and all actual conditions remain part of the chart
even though the direct contradiction below needs no further
coefficient of this determinant. No rationality of L is presumed.

For precision, the direct algebraic proposition is stronger in
its required inputs: over any characteristic-zero coefficient
field L, rows (4), the equality L[X,Y,Z,W]=L[X,P], and
\[
mh\ne0,\qquad
\theta=aP^3+bP^2+cP+d,\quad a\ne0,\qquad
y=r_3P^3+r_2P^2+r_1P+r_0
\tag{5}
\]
are inconsistent. The coefficients other than m,h,a may be zero.
The proof of this proposition treats every displayed coefficient
as an element of L; it requires no differential equation among
them. In the actual chart, the accepted
[521](principal-paraboloid-higher-slope-intercept-degree-bound-pass521-working.md)
supplies deg_P(y)<=3 and therefore (5). Its full hypotheses are
retained, not inferred from arbitrary formal rows.

## 2. Complete odd parts with X still independent

Introduce an auxiliary indeterminate lambda and translate
P=lambda+xi. Put z=xi^2 and write the unique parity decompositions
\[
\theta(\lambda+\xi)=E(\lambda,z)+\xi O(\lambda,z),\qquad
y(\lambda+\xi)=E_y(\lambda,z)+\xi O_y(\lambda,z).
\tag{6}
\]
Their full expressions are
\[
\begin{aligned}
E&=a(\lambda^3+3\lambda z)+b(\lambda^2+z)+c\lambda+d,\\
O&=a(z+3\lambda^2)+2b\lambda+c,\\
E_y&=r_3(\lambda^3+3\lambda z)+r_2(\lambda^2+z)
                      +r_1\lambda+r_0,\\
O_y&=r_3(z+3\lambda^2)+2r_2\lambda+r_1.
\end{aligned}
\tag{7}
\]
Here an odd part means the coefficient of xi in
L[lambda,X,z] direct-sum xi L[lambda,X,z]. X is still an
independent variable, held fixed in this decomposition.
Set gamma0=2lambda+k1 and
\[
\begin{aligned}
F&=mO+\gamma_0,\\
G&=(mp-h\gamma_0)E+2mE_y+mk_2\lambda+mn_t
                            -(p\lambda+n_s)\gamma_0.
\end{aligned}
\tag{8}
\]
Substitution in the COMPLETE rows (4) gives
\[
\begin{aligned}
\operatorname{odd}(Y)&=O_y+X,\\
\operatorname{odd}(Z)&=2t(O_y+X)+F,\\
\Omega:=\operatorname{odd}(mW)
  &=(mX-p\lambda-n_s)O-pE-hEO
       -\gamma_0O_y-2E_y-k_2\lambda-n_t.
\end{aligned}
\tag{9}
\]
For example, the odd part of -(h/2)theta^2 is -hEO,
and that of -(2P+k1)y is -gamma0*Oy-2Ey. The terms ell
and msX^2 are even. No lower contribution has been omitted.

The useful pre-elimination identity is
\[
\boxed{m\Omega-m^2O(X+O_y)
       +(mO_y+p\lambda+n_s+hE)F+G=0.}
\tag{10}
\]
It is a polynomial identity in L[lambda,z,X]. In particular it
holds BEFORE any value of X has been selected. Equivalently,
substitution X=-Oy in this algebraic identity would give
m*Omega+(m*Oy+p*lambda+n_s+hE)F+G=0. That substitution is
only elimination in an identity, not an ambient map or a
claim that an X depending on z is a fixed coordinate value.

## 3. A finite common root from the entire resultant

Both F and G are linear in z over L[lambda]. To show the
resultant and every possible specialization directly, write
F=f1*z+f0 and G=g1*z+g0. Then
\[
\begin{aligned}
f_1&=ma,\\
f_0&=m(3a\lambda^2+2b\lambda+c)+2\lambda+k_1,\\
g_1&=(mp-h\gamma_0)(3a\lambda+b)+2m(3r_3\lambda+r_2),\\
g_0&=(mp-h\gamma_0)(a\lambda^3+b\lambda^2+c\lambda+d)\\
   &\quad+2m(r_3\lambda^3+r_2\lambda^2+r_1\lambda+r_0)
       +mk_2\lambda+mn_t-(p\lambda+n_s)\gamma_0.
\end{aligned}
\tag{11}
\]
The resultant, computed at these degree-one bounds, is
\[
\mathscr R(\lambda)=\operatorname{Res}_z(F,G)=f_1g_0-f_0g_1.
\tag{12}
\]
One has deg_lambda(f0)=2, deg_lambda(g1)=2 and
deg_lambda(g0)=4, with respective leaders 3ma,-6ha,-2ha.
Thus deg_lambda(mathscr R)<=4, and its degree-four coefficient is
\[
(ma)(-2ha)-(3ma)(-6ha)=16mha^2\ne0.
\tag{13}
\]
Consequently mathscr R has exact degree four. This calculation
retains arbitrary r3,r2,r1,r0: none can contribute to its
degree-four coefficient. In particular no degree of y is divided
by or assumed positive.

Let M be an algebraic closure of L. Choose a root lambda0 of
the nonconstant polynomial (12), and set
\[
z_0=-f_0(\lambda_0)/(ma)\in M.
\tag{14}
\]
The coefficient f1=ma never vanishes. Therefore F(lambda0,z0)=0,
and (12) gives G(lambda0,z0)=0. This is a FINITE common root.
It remains valid if g1(lambda0)=0, if G(lambda0,z) is constant
or zero, and if z0=0. No common point at infinity is used.

## 4. Choose a field constant X0 and use the actual return

Only now define the single element
\[
X_0=-O_y(\lambda_0,z_0)\in M.
\tag{15}
\]
It is independent of the remaining variable xi. Specialize the
ORIGINAL rows (4) at this fixed X0, then translate P=lambda0+xi.
Call the resulting polynomials Y0,Z0,W0 in M[xi], and write
their odd parts as Y_o(z),Z_o(z),W_o(z) in M[z]. Equations
(9),(10),(14),(15) give
\[
Y_o(z_0)=Z_o(z_0)=W_o(z_0)=0.
\tag{16}
\]
For W, equation (10) at (lambda0,z0,X0) yields m*Omega=0,
so Omega=0 and W_o=Omega/m=0. Both uses of m are legitimate
because m is a nonzero coefficient-field element.

The ideal of these THREE FIXED-X0 odd polynomials,
\[
I=(Y_o,Z_o,W_o)\subset M[z],
\tag{17}
\]
is proper, since it is contained in (z-z0). All three full
specialized generators therefore belong to
\[
\mathscr S=M[z]\mathbin{\oplus}\xi I\subsetneq M[\xi],
\qquad z=\xi^2.
\tag{18}
\]
This is a subring: an even polynomial preserves I upon
multiplication, and the product of two odd terms belongs to
zI^2, in the unrestricted even part. It is proper because xi
has odd coefficient one whereas 1 is not in I. This proof
includes z0=0 and does not require two distinct points.

On the other hand, extend the equality in (2) from L to M,
then quotient by X-X0. This gives
\[
M[Y(X_0),Z(X_0),W(X_0)]=M[P].
\tag{19}
\]
Translation P=lambda0+xi is a polynomial automorphism over M,
so (19) says M[Y0,Z0,W0]=M[xi], contradicting (18).
All these operations are on the coefficient-extended polynomial
return. Neither lambda0, z0 nor X0 is promoted to an actual
complex ambient coordinate or an original geometric fiber.

This proves the direct proposition (5). Using521 only to obtain
deg_P(y)<=3 proves exactly the conditional chart exclusion (1).

## 5. Verification and scope

The complete264 source was freshly read through EOF before
authoring. The final notation-corrected521 was previously
independently read and reviewed through EOF at
SHA6e292e83a069137d6b73e2d3e4d8b9998c1627ce3ddc50d52b0ad31f2860691f;
its retained degree theorem, not an assumption on arbitrary y,
is the sole additional input to the chart corollary.

Fresh unsaved85eeba reconstructs the complete original rows,
both parity decompositions, the fixed-X identity (10), the
whole resultant (12), its exact degree and leader (13), and
the quadratic/linear/constant/zero-y specializations. Every
residual was zero. Root independently reconstructed the same
complete generic-cubic identities in fresha34a49. These are
outline computations; an independent full saved-source review
remains a separate gate after this author hold.

The proof does not require529, the monic third level, the fourth
potential or another coefficient of the calibrated scalar once
(4),(5) and the all-X return are supplied. It makes no claim
about m=0, h=0, a quartic theta, nonlinear sigma, or arbitrary
entry into the actual principal chart. It is not unrestricted
cancellation, recognition, a novelty assertion or external
certification. No saved checker was executed, imported or
compiled. No earlier source or canonical record was changed.
