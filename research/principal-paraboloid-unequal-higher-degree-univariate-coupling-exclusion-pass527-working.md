# Unequal higher intrinsic degrees with moving univariate coupling

Working conditional exclusion. Retain every actual hypothesis and
return of264, the genuine levels and unit gradients of296, and
the universal multiplier identities in Sections1--3 of494.
Suppose

\[
 \sigma=P,\qquad m=k_s\ne0,\qquad m_s=0,\qquad
 p=m_t\ne0,\qquad N=\deg_P\theta\ge3,\qquad \deg_Py<N.
\tag{1}
\]

Then (1) is impossible. The degree of the zero polynomial is
minus infinity, so y=0 is included. This is not a recognition
claim for p=0, equal degrees, nonzero m_s, nonlinear sigma or
arbitrary cancellation data. No general entry theorem is assumed.

## 1. Actual inputs and full formal identities

The original actual ring is B=C[X,Y,Z,W]=A[u_glob], with
E=partial_(u_glob), actual E degrees (1,2,2,2), and ENTIRE
initial kernel (mathsf X^2 mathsf Z-mathsf Y^2). The original
global slice need not be X/(EX). Retain the selected derivation
N_sel=[u_glob^4]partial_Z|A, its exact coefficient field
L=Frac(ker_A N_sel), and both the literal-intercept and all-X
returns from264. The field L is finite over C(t,s). Its
commuting coefficient partials hold P fixed. In particular

\[
 \begin{gathered}
 L[X,Y,Z,W]=L[X,P],\qquad
 \operatorname{Frac}A=L(P)=\mathbb C(y,z_{\rm int},w),\qquad
 L[y,z_{\rm int},w]=L[P],\\
 Y=y+PX+tX^2,\\
 Z=2ty+P^2+k_tP+m\theta+n+(2tP+k)X+t^2X^2,\\
 mW=[mX-pP-n_s]\theta+
       \ell-(2P+k_t)y-\frac{k_{tt}}2P^2-n_tP+msX^2.
 \end{gathered}
\tag{2}
\]

Here z_int is the literal Z intercept, not its difference with
2ty. The symbol N in (1) is a polynomial degree and is not
the selected derivation or the potential n. No field parameter
is declared an ambient polynomial coordinate.

For independent formal variables U,P,V, the COMPLETE third
level H_0=H-h_0 under m_s=0 is

\[
 H_0=U^2+pUV+L_2U+\frac{n_{ss}}2V^2+M_2V+N_3,
\tag{3}
\]

where

\[
 \begin{aligned}
 L_2&=k_{tt}P+n_t-\frac{(2P+k_t)(pP+n_s)}m,\\
 M_2&=\frac{m_{tt}}2P^2+n_{ts}P-\ell_s
                                  -\frac{(pP+n_s)^2}m,\\
 N_3&=\frac{(pP+n_s)(\ell-k_{tt}P^2/2-n_tP)}m
       +\frac{k_{ttt}}6P^3+\frac{n_{tt}}2P^2-\ell_tP-h_0.
 \end{aligned}
\tag{4}
\]

Their degrees are at most two, two and three. The full actual
level is H_0(y,P,theta)=0, and the ideal of the three evaluated
FORMAL U,P,V derivatives is the unit ideal in L[P]. Formula
(3) is the full formal expansion recorded in522, not a claim
that the three-variable curve has only one defining equation.

Write theta=aP^N+lower terms, a in L*. The universal B identity is

\[
 \theta_t+\theta_P\left(y_P+\theta_s+\frac{pP+n_s}{m}\right)
 +\frac{2y+k_{tt}P+p\theta+n_t}{m}
 +\frac{2P+k_t}{m}y_P=-\kappa H_U(y,P,\theta),\quad\kappa\in L^*.
\tag{5}
\]

Its unique possible coefficient of degree 2N-1 is Naa_s;
the right side has degree at most N, and every other term
on the left has smaller degree. Thus a_s=0. In (3), the
unique degree-2N contribution is n_ss*a^2/2: all others
have degree at most max(2deg y,N+deg y,N+2,3)<2N.
Consequently

\[
 a_s=0,\qquad n_{ss}=0.
\tag{6}
\]

No lower coefficient is assumed to be s-constant. In particular
the argument does not restrict the arbitrary lower potentials.

## 2. Reduction to degree-three and degree-four theta

Using (6), the exact actual level is

\[
 (py+M_2)\theta+y^2+L_2y+N_3=0.
\tag{7}
\]

If d=deg y>2, the coefficient A_theta=py+M_2 has exact
degree d because p is nonzero. Its product with theta has
degree N+d, strictly larger than 2d,d+2 and three because
d<N. It cannot cancel in (7). Therefore deg y<=2, allowing
the zero polynomial.

Also A_theta cannot be the zero polynomial. If it were zero,
(7) would give y^2+L_2y+N_3=0, and the ENTIRE formal
polynomial would factor as

\[
 H_0=(U-y(P))\bigl(U+y(P)+pV+L_2(P)\bigr).
\tag{8}
\]

The first factor vanishes on the actual line. The second
evaluates to 2y+p theta+L_2, which has exact degree N>=3.
It therefore divides every evaluated formal derivative of H_0
and is a nonunit in L[P]. This contradicts the retained unit
gradient. No factor-recognition theorem is needed here.

The remaining terms in (7) have degree at most four. Hence

\[
 y=eP^2+vP+f_0,\qquad
 A_\theta=py+M_2\ne0,\qquad
 N+\deg A_\theta\le4,
 \qquad N\in\{3,4\}.
\tag{9}
\]

All three coefficients e,v,f_0 belong to L, and e may be zero.
The field element p need not be complex or constant in t.

## 3. The full odd-part obstruction

Let lambda be an auxiliary indeterminate and put

\[
 X_\lambda=-2e\lambda-v,\qquad
 P=\lambda+\xi,\quad z=\xi^2,\qquad
 \theta(\lambda+\xi)=E(\lambda,z)+\xi O(\lambda,z).
\tag{10}
\]

This is coefficient-field base change and substitution, not an
ambient polynomial coordinate change. No division by e occurs.
Put k_1=k_t and k_2=k_tt, and define

\[
 \begin{aligned}
 F&=mO+2\lambda+k_1,\\
 c_\lambda&=-(2me+p)\lambda-mv-n_s,\\
 L_{\rm low}&=2ez+6e\lambda^2
       +(4v+2k_1e+k_2)\lambda+k_1v+2f_0+n_t,\\
 g&=c_\lambda O-pE-L_{\rm low},\\
 G&=c_\lambda(2\lambda+k_1)+mpE+mL_{\rm low}.
 \end{aligned}
\tag{11}
\]

By an odd part we mean the coefficient of xi in the unique
decomposition L[z] direct-sum xi L[z]. Substitution in the
COMPLETE rows (2) gives

\[
 \operatorname{odd}(Y)=0,\qquad
 \operatorname{odd}(Z)=F,\qquad
 \operatorname{odd}(mW)=g,
 \qquad G=c_\lambda F-mg.
\tag{12}
\]

For example, Y's odd part is 2e lambda+v+X_lambda=0.
Z's remaining odd part is
mO+4te lambda+2tv+2lambda+k_1+2tX_lambda=F.
In mW, the coefficient of theta is
c_lambda-p xi. The remaining lower odd part is exactly
-L_low, including all potential and lower-y contributions.

These are the same two F,G polynomials as in523, Section4,
with its nonzero parameter u replaced by p. This use does NOT
import523's equal-degree hypothesis or its normalization:
(10)--(12) have just been derived directly from (1),(2).
The resultant calculations are purely polynomial identities.
Explicitly,

\[
 \begin{array}{c|c|c}
 N&\deg_\lambda\operatorname{Res}_z(F,G)&
       \text{leading coefficient in }\lambda\\ \hline
 3&3&-8m^2pa^2\\
 4&6&-64m^3pa^3
 \end{array}
\tag{13}
\]

Both leaders are nonzero. For N=3, F is linear in z with
constant nonzero z coefficient ma. For N=4, G is quadratic
in z with constant nonzero leading coefficient mpa. These
observations ensure that a zero of the resultant supplies a
FINITE common root, including specialization at a vanishing
linear coefficient of F: then resultant vanishing forces
F's constant coefficient to vanish also, while G stays
quadratic. The explicit cubic and quartic even/odd formulas
and resultant expansions are given in523, equations12--15.

For completeness, let M be an algebraic closure of L. Since
the resultant in (13) is nonconstant, it has a root lambda_0
in M, and the finite-root argument gives z_0 in M with
F(lambda_0,z_0)=G(lambda_0,z_0)=g(lambda_0,z_0)=0. Therefore
I=(F(lambda_0,z),g(lambda_0,z)) is a proper ideal of M[z].

The all-X return from (2) survives scalar extension to M,
then specialization X=X_(lambda_0) and translation of P.
It would give M[Y_0,Z_0,W_0]=M[xi]. But (12) puts its
left side in the proper subring

\[
 M[z]\mathbin{\oplus}\xi I\subsetneq M[\xi],\qquad z=\xi^2.
\tag{14}
\]

Closure follows because odd times odd is even, while even
times odd preserves I. Properness follows because 1 is not
in I, so xi is not in this subring. This is the contradiction.
It includes z_0=0 and e=0, and does not require two distinct
points, a plane-embedding theorem, or nonvanishing of any
unrestricted lower coefficient.

## 4. Evidence and exact scope

Root's fresh unsaved inline8f10bc reconstructs all three
COMPLETE original row odd parts, the zero-e specialization,
both resultants and their nonzero leaders, and the complete
formal factorization (8). Every residual was zero. The
uniform degree arguments, unit-gradient contradiction and
base-change/parity-ring proof are written above; they are
not assertions drawn from finite grids or floating-point data.

The full held522 and523 sources were read and separately
reviewed before this argument. The formal expansion (3),(4)
is used independently of522's equal-degree conclusion; the
resultant formulas are used independently of523's different
actual normalization. A complete saved-source review remains
a separate gate after this author's hold.

This excludes exactly (1). Under m_s=0, the excluded p=0
boundary means m is a nonzero complex constant, because
both coefficient partials then kill m. That boundary is
not called impossible by this note. No conclusion is made
for equal degrees or m_s nonzero here. Any composition with
other degree bounds must state those separate dependencies.

The general cancellation conjecture remains unsolved. The
intended field and dimension of the professor's email remain
unconfirmed. No saved checker was executed, imported or
compiled. No earlier source, canonical record, external
message or submission was changed. There is no novelty or
external-certification claim.
