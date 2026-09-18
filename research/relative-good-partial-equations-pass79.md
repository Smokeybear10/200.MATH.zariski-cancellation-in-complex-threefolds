# The original good partial on the relative hypersurface

The relative presentation from pass78 carries a complete polynomial
system for the original coordinate partial. Its restriction to the
slice section is a derivation of the original kernel, but it cannot
preserve the common invariant plane in the nonlinear supplied-good
branch. The primitive intrinsic fixed-locus ideal is exactly the
relative gradient of the hypersurface equation divided by its gcd.

These are constraints on the actual reconstructed presentation. They
do not turn an arbitrary abstract hypersurface or a rational vector
field into an original coordinate frame, and do not prove that the
divided gradient ideal is the unit ideal.

Subsequent arguments in this same pass strengthen these intermediate
conclusions: the [primitive Jacobian theorem](relative-jacobian-primitive-pass79.md)
removes the gcd, [actual quadratic generation](relative-quadratic-generation-pass79.md)
proves the original-coordinate cube bound, and the
[good-direction recognition endpoint](nice-good-direction-recognition-pass79.md)
proves a global primitive slice in the full stated branch. The
deliberately weaker scope of the calculation below is not a claim
that those completed consequences remain open.

## 1. The actual relative presentation

Retain every actual hypothesis of the
[relative hypersurface theorem78](binary-relative-hypersurface-pass78.md).
Write its two invariant generators as Y,Z and its new E-slice as
sigma. Thus
\[
\begin{gathered}
B=\mathbb C[x_1,x_2,x_3,w]=A[\sigma],\qquad E=\partial_\sigma,
\qquad S=\ker\delta\simeq\mathbb C[u,v],\\
A=S[Y,Z]\simeq S[\mathsf Y,\mathsf Z]/(F),\qquad
Q=[T,E],\quad T=\partial_w,\quad \delta=Q|_A\ne0,\\
x_{\rm tr}=H\sigma+R,\qquad R=VY+Wc,\qquad
w=Z+P_4\sigma,\qquad M=[H,V,W]\in\operatorname{SL}_3(S).
\end{gathered}
\tag{1}
\]
Here H,V,W,c,P4 all have their actual meanings from pass78;
in particular c,P4 lie in S, and H,V,W have entries in S.
The original coordinate reconstruction and both matrix inverse
identities have already been proved over S. The presentation is
not a constant linear change of the original four coordinates.

The polynomial F is irreducible and primitive over S, and depends
on at least one of its two displayed variables. When a derivative
of F is used below, it is evaluated at the actual Y,Z in A.
The capital letters Y,Z denote these generators, not a claim that
they are independent over S.

## 2. Unique transport of the actual fields

Since Q commutes with E, its restriction to A and its value on
sigma give Q=delta+a partial_sigma with a in A. The identity
[T,E]=Q says that, for r in A, partial_sigma(Tr)=-delta(r),
and partial_sigma(Tsigma)=-a. Characteristic zero and the genuine
polynomial extension A[sigma] therefore give unique a,b in A and
a complex derivation theta of A such that
\[
\begin{aligned}
Q&=\delta+a\partial_\sigma,\qquad a=Q\sigma,\\
T&=\theta-\sigma\delta+(b-\sigma a)\partial_\sigma,
\qquad \theta(r)=(Tr)|_{\sigma=0},\quad b=(T\sigma)|_{\sigma=0}.
\end{aligned}
\tag{2}
\]
The evaluation defining theta is an algebra homomorphism on
A[sigma], so the Leibniz identity for T proves that theta is
a derivation of A. It is not an S-linear derivation in general.
Local nilpotence of theta is not inferred from that of T.

Set d=delta(Y) and k=delta(Z). Applying (2) to all four
original coordinates in (1), and equating the constant and
linear coefficients of sigma, gives precisely
\[
\boxed{
\begin{aligned}
\theta H&=aH+dV,&\qquad \theta P_4&=aP_4+k,\\
\theta R&=-bH,&\qquad \theta Z&=1-P_4b.
\end{aligned}}
\tag{3}
\]
For example T(x_tr)=sigma(theta H-aH-dV)+theta R+bH.
The expression for T(w) is
sigma(theta P4-aP4-k)+theta Z+P4b.
Consequently (3) is also sufficient for Tx_tr=0 and Tw=1
when (1), (2), and the actual generation of B by x_tr,w
are retained. In that setting T is literally the original
partial, not merely a derivation with a proposed formal name.

This sufficiency does not omit the generation hypothesis.
If one starts with arbitrary abstract data in place of (1),
the equations alone do not prove that the four displayed
elements generate a polynomial ring.

The frame matrix records every coefficient in (3). Define
Omega=M^{-1}(theta M), with theta acting entrywise. Differentiating
det M=1 gives trace Omega=0, and (3) becomes
\[
\begin{gathered}
\Omega_{\bullet1}=(a,d,0)^t,\qquad
b=-\Omega_{12}Y-\Omega_{13}c,\\
\theta Y=-\Omega_{22}Y-\Omega_{23}c,\qquad
\theta c=-\Omega_{32}Y-\Omega_{33}c,\qquad
a+\Omega_{22}+\Omega_{33}=0.
\end{gathered}
\tag{4}
\]
The entries of Omega lie in A, not necessarily S. Formula (4)
includes differentiation of the S-valued coefficients of V,W,c;
none has been incorrectly held constant under theta.

The first line of (3) also reconstructs the two actual velocity
columns of Q and Q squared:
\[
\begin{aligned}
Q(x_{\rm tr},w)&=(aH+dV,\ aP_4+k),\\
Q^2(x_{\rm tr},w)&=((\delta a)H+(\delta d)V,
                         \ P_4\delta a+\delta k).
\end{aligned}
\tag{5}
\]
All these entries lie in A. In the binary notation of pass78,
the already proved identity gives
d=omega G(p,q)/e, which is nonzero. It is not declared a unit
or a delta-invariant.

## 3. The relation and the fourth direction

Put alpha=theta(u), beta=theta(v), r=theta(Y), and t=theta(Z),
all in A. The exact relation-preservation equations are
\[
dF_Y+kF_Z=0,\qquad
\alpha F_u+\beta F_v+rF_Y+tF_Z=0\quad\text{in }A.
\tag{6}
\]
These follow by differentiating F(u,v,Y,Z)=0. Conversely they
are the tangency conditions for the specified values to define
derivations of this quotient. Polynomial representatives in
S[mathsf Y,mathsf Z] may be chosen for the values in A; changing
those representatives does not change the two equations in A.
Equation (6) does not treat theta(u),theta(v) as elements of S.

There is also an exact bracket formula. With
eta=[theta,delta]+a delta and ell=theta(a)-delta(b)+a squared,
direct application to A and sigma gives
\[
[T,Q]=\eta+\ell\partial_\sigma,
\qquad
\eta=[\theta,\delta]+a\delta,\qquad
\ell=\theta a-\delta b+a^2.
\tag{7}
\]
The terms linear in sigma cancel on both A and sigma. In
particular this bracket commutes with E, as it must by Jacobi.

The full nonlinear-branch
[Wronskian theorem78](binary-wronskian-derived-rank-pass78.md)
states that E,T,Q,[T,Q] have rank four over Frac B.
Subtracting their partial_sigma components and the indicated
multiples of delta in (2), (7) yields
\[
\operatorname{rank}_{\operatorname{Frac}A}
  (\delta,\theta,[\theta,\delta])=3,
\qquad
\theta(u)\delta\theta(v)-\theta(v)\delta\theta(u)\ne0.
\tag{8}
\]
For the second assertion, u,v,Y are algebraically independent:
u,v generate S, and an element algebraic over Frac S is killed
by delta, whereas delta Y=d is nonzero. Their field has the
same transcendence degree as Frac A, so the latter is a finite
separable extension. Evaluating the three rows
(delta,theta,[theta,delta]) on (u,v,Y) gives determinant
-d times the second expression in (8). This proves its precise
sign and nonvanishing.

In particular theta(S) cannot be contained in S in this branch.
If it were, delta theta(u) and delta theta(v) would both vanish,
contradicting (8). This obstruction holds for every relative
slice and basis for which (1) is retained. It is not merely
a failure exhibited by one example.

## 4. The exact primitive ideal on the hypersurface

The generation A=S[Y,Z] and delta(S)=0 imply
\[
(\delta(A))A=(d,k)A.
\tag{9}
\]
The inclusion from left to right follows by differentiating
an arbitrary representing polynomial; the reverse inclusion
uses the actual values delta Y and delta Z. Thus no unspecified
set of intrinsic generators is needed for the image ideal.

A is a UFD with only complex units, by the actual cylinder
A[sigma]=B and factorial closure. At least one of F_Y,F_Z
is nonzero in A. Indeed F depends on Y or Z in characteristic
zero, and its nonzero corresponding partial has smaller degree
in that variable and cannot be divisible by F.
Let g_F be a gcd in A of the nonzero members of this pair.
Then the primitive intrinsic LND D is, up to one nonzero
complex constant kappa, given exactly by
\[
\boxed{
D|_S=0,\qquad
D(Y)=\kappa F_Z/g_F,\qquad D(Z)=-\kappa F_Y/g_F,
\qquad
(D(A))A=(F_Z/g_F,F_Y/g_F)A.}
\tag{10}
\]
Here is the full fraction-clearing argument. Equation (6)
and (d,k) not both zero make their pair a rational multiple
of (F_Z,-F_Y). Divide the latter pair by its gcd, obtaining
a primitive pair in the UFD A. A rational scalar whose
products with both entries lie in A must lie in A: a prime
in its reduced denominator would otherwise divide both
primitive entries. Therefore
(d,k)=r_0(F_Z/g_F,-F_Y/g_F) with r_0 in A.
The gcd of (d,k) is r_0 up to a complex unit. Dividing delta
by its actual content gives exactly (10), using the already
proved primitive-LND division in
[pass75](primitive-good-quotient-scope-pass75.md).
Since S,Y,Z generate A, equality on these values determines
the derivation, not just its field direction.

The pair in (10) defines an actual derivation of A because it
annihilates F. Its local nilpotence here follows from its equality
to the primitive part of the actual delta, not from a general
claim that Jacobian derivations are locally nilpotent.
No assertion that g_F is a unit or that the divided pair has
unit ideal is made. The displayed division is an exact gcd
division, not infinite saturation.

## 5. The actual conic check and the weaker fixed-line boundary

For the retained conic seed use independent coordinates
(sigma,t,Y,c). The original coordinates and their inverse are
\[
\begin{gathered}
x_1=\sigma,\qquad x_2=t\sigma+Y,\qquad
x_3=t^2\sigma+2tY+c,\qquad
w=t+Y^2-c\sigma,\\
t=x_1x_3-x_2^2+w,\qquad
Y=x_2-tx_1,\qquad c=x_3-2tx_2+t^2x_1,\qquad
\sigma=x_1.
\end{gathered}
\tag{11}
\]
Both substitutions directly recover all four entries. In these
coordinates E=partial_sigma, S=C[t,c], P4=-c,
H=(1,t,t squared), V=(0,1,2t), W=(0,0,1), and Z=t+Y squared.
The hypersurface equation is F=Z-t-Y squared. The fields are
\[
\begin{gathered}
Q=\partial_Y,\qquad
T=\partial_t-2Y\partial_c-\sigma\partial_Y,
\qquad a=b=0,\\
\delta Y=1,\quad \delta Z=2Y,\qquad
\theta t=1,\quad\theta c=-2Y,\quad\theta Y=0,\quad\theta Z=1.
\end{gathered}
\tag{12}
\]
Thus theta(S) is not contained in S; the base expression in
(8), in coordinates (t,c), equals -2. Equation (3) checks
directly, as do both tangency equations. The divided relative
gradient pair is (1,2Y), so its ideal is the unit ideal.
These are calculations on the already recognized action,
not a new family or a primitive fixed-point example.

For comparison, the retained weaker intrinsic model is
\[
A_0=\mathbb C[u,Y,Z],\qquad S_0=\mathbb C[u,v],\quad
v=uZ-Y^2,\quad F_0=uZ-Y^2-v,\qquad
D_0=u\partial_Y+2Y\partial_Z.
\tag{13}
\]
Its gcd g_F is one and the ideal in (10) is (u,Y), which is
proper. It has an actual polynomial cylinder and plane quotient,
but has not been supplied with the full original reconstruction
(1), the equations (3), and the nonlinear rank condition (8).
It therefore shows only why the relative hypersurface and its
primitive Jacobian formula alone are insufficient. No abstract
choice of theta is asserted to realize the missing actual partial.

## 6. Verification and scope

The complete relative hypersurface78, Euler78, Wronskian78 and
primitive quotient75 written notes were read for this derivation.
The independent-parameter Euler formula is not applied to a
dependent binary pair, and no algebraic parameter derivative is
assumed regular. The formulas here use actual polynomial values
and the one genuine slice extension A[sigma] throughout.

The author read this complete saved note through EOF and checked
whitespace. A separate inline exact SymPy calculation checked both
inverse orders in (11), the actual transported partial and bracket,
and the conic base Wronskian -2; it exited zero (tool chunk
`316035`). This is a scratch control on the retained example, not
a new unittest method or a proof of the general statements.

The new conclusions are the complete original-partial system,
the compulsory nonpreservation of S in (8), and the exact two-entry
primitive ideal. They do not prove primitive freeness, a universal
Q-cube bound, a coordinate property of F or sigma, or general
cancellation. No new numerical suite, full regression, historical
novelty, primary-paper reread, human expert review or formal proof
certificate is claimed. Frozen files through pass78 and shared
metadata are unchanged.
