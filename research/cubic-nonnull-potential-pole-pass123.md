# The non-null cubic potential has a fixed reciprocal term

In the supplied actual non-null cubic framework, the scalar potential
has the exact form Psi0=lambda g/Y+c, with lambda a nonzero complex
constant and c in the full first-integral field L. The constant is
forced by the lower volume equations121, not by choosing a normalization
of a generic relative Jacobian.

Combining this with the original-coordinate reconstruction gives a
rational identity involving z and the actual good coordinates. The
identity is valid without assuming h generates L or is a polynomial
coordinate. It does not by itself assert that its individual rational
terms are regular or that its reciprocal term cannot cancel.

## 1. Actual hypotheses and the retained potential

Retain the full original-coordinate framework90 and the surviving
non-null cubic form of
[scalar classification121](cubic-nonnull-axis-scalar-constraint-pass121.md),
using [constant reciprocal equivalence122](cubic-nonnull-reciprocal-equivalence-pass122.md)
if necessary. Write q for the original constant acceleration and a
for the coefficient occurring in
[the non-null reconstruction122](cubic-nonnull-divisor-restriction-pass122.md).
Thus

\[
\begin{gathered}
B=\mathbb C[x_1,x_2,x_3,z]=A[u],\quad A=\ker E,\quad
Eu=1,\quad Ez=qu,\quad q\in\mathbb C^*,\\
S=\ker(N|A)=\mathbb C[s,t],\quad K=\operatorname{Frac}S,\quad
L/\mathbb C(h)\text{ finite},\quad L\text{ relatively algebraically closed in }K,\\
b=(g,P,Y)^t\in S^3,\quad h=P/Y\notin\mathbb C,\quad
g^2-DY^2=1,\quad
D=a_3h^3+a_2h^2+a_1h+a_0,\quad a_i\in\mathbb C,\quad a_3\ne0,\\
Q=\operatorname{diag}(-1,M),\quad
M=\begin{pmatrix}
D''/2&(D'-hD'')/2\\
(D'-hD'')/2&D-hD'+h^2D''/2
\end{pmatrix},\\
\Delta=\det Q=(D'^2-2DD'')/4\ne0,\quad
D\ne0,\quad \Delta'=-DD'''/2,\quad D'''=6a_3,\\
\rho=C_0g+aY,\quad C_0\in\mathbb C,\quad a\in L,\qquad
x_{\rm tr}=b(u+\rho)+b_hv+b_YR,\\
z=\frac q2u^2+\chi-q\Psi,\qquad
\Psi=\rho_hv+\rho_YR+\frac12G_{ij}y_i y_j,\quad
(y_1,y_2)=(v,R),\quad
\Psi_0=\chi+\frac q2\rho^2\in K .
\end{gathered}
\tag{1}
\]

Here and below a prime denotes the unique extension of d/dh to L,
or its specified finite algebraic extension, unless a normalized
derivative is named. The two derivatives b_h,b_Y in (1) are the
commuting rational derivatives with the other variable held fixed.
The element Y is transcendental over L, the full Y-constant field
in K is L, and the two relative generators are actual elements of
A_K. The original-coordinate inverse, exact relative degree three
and actual base-only unit-volume property are retained hypotheses.

The last line is the exact potential of
[quadratic potential90](nonconical-quadratic-potential-pass90.md),
transported to this rational base frame. The matrix G is the radial
coefficient matrix in the second derivatives of b. No equality
L=C(h), global relative slice or constant relative Jacobian is assumed.

## 2. The conic normalization and its two derivative conventions

As in121, take a finite extension L' of L containing d=sqrt(D) and
sqrt(Delta), and form the field K'=KL'. Regularity of K/L gives
this field with L' relatively algebraically closed in K'. Its
coefficient h-derivative has constants C. Set

\[
\begin{gathered}
w=i(g+dY),\quad Z=w+w^{-1}=2idY,\quad
W=w-w^{-1}=2ig,\quad
\kappa=\frac{\sqrt\Delta}{2D},\quad
e_0=-\frac{\Delta'}{2\Delta},\quad e=e_0/\kappa,\\
w_h\big|_Y=\frac{D'Yw}{2dg},\qquad
w_Y\big|_h=\frac{dw}{g},\\
\partial_w=\frac{g}{dw}\partial_Y,\qquad
\partial=\kappa^{-1}
 \left(\partial_h\big|_Y-\frac{D'Y}{2D}\partial_Y\right),\\
\partial w=0,\qquad [\partial,\partial_w]=0,\qquad
\partial|_{L'}=\kappa^{-1}d/dh .
\end{gathered}
\tag{2}
\]

The inverse of g+dY is g-dY, by the norm identity. This gives Z
and W and proves the two derivative formulas by differentiation.
All denominators are nonzero in K'. The normalized derivative
partial fixes w, not Y. Its restriction to L' is the scaled
h-derivative, which is the convention used for the scalar equations
below. No algebraic primitive of partial is required.

This rational change of base derivatives does not change rho or
Psi0. Indeed, the tangent span of the two derivatives of b is
unchanged, so the coefficient of b in the original reconstruction
is unchanged. Under an invertible change of the derivative pair,
the radial part of the second derivatives transforms as a symmetric
two-tensor: derivatives of the change-of-frame coefficients multiply
first derivatives of b and contribute no radial term. The relative
generator column transforms contragrediently. Consequently both
rho_i y_i and G_ij y_i y_j are unchanged. Thus Psi, and then
chi=z-qu squared/2+qPsi and Psi0, are the same scalar elements
before and after this coefficient-field normalization.

## 3. The cubic case forces a constant reciprocal coefficient

The actual normalized-frame volume calculation121, equations(4)--(7),
supplies ell in L' nonzero and c_* in L' with

\[
\begin{gathered}
\Psi_0=\frac{\ell W}{4Z}+c_*,\qquad z_0=1/\ell\in L'^*,\\
\partial^2z_0-e\,\partial z_0-4z_0=0,\qquad
\frac{\partial e}{e}+4\frac{\partial z_0}{z_0}-3e=0,\\
(z_0)''+\frac{D'}D(z_0)'-\frac{\Delta}{D^2}z_0=0,
\qquad (d z_0)''=0,\\
z_0=\frac{\beta_1h+\beta_0}{d},\quad
\beta_0,\beta_1\in\mathbb C,\quad(\beta_0,\beta_1)\ne(0,0),\\
\bigl(D'''(\beta_1h+\beta_0)^4\bigr)'=0 .
\end{gathered}
\tag{3}
\]

These are retained consequences of the actual potential and all
required lower volume coefficients, not additional choices of ell.
To check the conversion explicitly, on L' equation(2) gives
partial squared z0=kappa to the power minus two times
[z0''-(kappa'/kappa)z0']. Moreover
kappa'/kappa+e0=-D'/D and 4kappa squared=Delta/D squared.
Multiplying the first normalized equation by kappa squared therefore
gives the third line of (3). Differentiating d z0 twice verifies
the equivalent equation there. Since the coefficient derivative has
constant field C, its solutions have the fourth displayed form.

For the last line, the second normalized equation says
(e z0 to the fourth power)'/(e z0 to the fourth power)=3e0.
The exact identity
e=D squared D'''/(2Delta to the power three halves)
gives
e z0 to the fourth power=
D'''(beta1 h+beta0) to the fourth power/(2Delta to the power three halves).
Its logarithmic derivative cancels 3e0, proving the last line.
This uses only derivatives and field identities, not analytic logarithms.

In the present cubic case D''' is the nonzero complex constant 6a3.
The last line forces beta1=0, and beta0 is nonzero. Substituting
ell=d/beta0 and W/Z=g/(dY) in the first line gives

\[
\boxed{\qquad
\Psi_0=\lambda\,\frac gY+c,\qquad
\lambda=\frac1{4\beta_0}\in\mathbb C^*,\qquad c\in L .
\qquad}
\tag{4}
\]

To justify the last membership, initially the remaining term is c_*
in L'. But Psi0 and lambda g/Y lie in K. Their difference is killed
by the Y-derivative, since c_* is a coefficient-field element.
The full Y-constant field of K is L, so it belongs to L already.
Neither the square roots nor the normalized derivative enlarge the
constant coefficient lambda beyond C.

Differentiating (4) in the original rational h,Y frame also gives
the exact potential-gradient identities

\[
(\Psi_0)_h=\lambda\frac{D'Y}{2g}+c',\qquad
(\Psi_0)_Y=-\frac{\lambda}{gY^2}\ne0 .
\tag{5}
\]

Thus the coefficient of the second relative generator is prescribed
and nonzero. The signs use g_Y=DY/g and g squared-DY squared=1.

## 4. Return to the actual original coordinates

Let x denote the three-column (x1,x2,x3). By the definition of the
canonical metric and its radial coefficients,

\[
\begin{gathered}
Q(b,b)=-1,\qquad Q(b,b_i)=0,\qquad Q(b_i,b_j)=G_{ij},\\
x^tQx=-(u+\rho)^2+G_{ij}y_i y_j,\\
z+\frac q2x^tQx
 =\Psi_0-q\bigl[\rho(u+\rho)+\rho_hv+\rho_YR\bigr],\\
\rho(u+\rho)+\rho_hv+\rho_YR
 =C_0x_1+a'x_2+(a-ha')x_3 .
\end{gathered}
\tag{6}
\]

For the third line substitute the potential identity in (1) and
cancel its radial quadratic term. The fourth line follows directly
from rho=C0g+aY and the original reconstruction:
the C0 terms combine to C0x1, the a terms to ax3, and the
a' term is a'Yv=a'(x2-hx3). C0 has zero h and Y derivatives.

Combining (4) and (6) proves the proposed rational identity:

\[
\boxed{\quad
z+\frac q2x^tQx+qC_0x_1
 =\lambda\frac gY+c-q a'x_2-q(a-ha')x_3 .
\quad}
\tag{7}
\]

This is an identity in the actual fraction field of B, with all four
displayed original coordinates still the actual polynomial generators.
The matrix Q and a,a',c belong to the indicated base field, so their
individual terms are not asserted to be polynomial.

## 5. The remaining lower-volume equation constrains a and c

The two coefficient-field functions in (4) and (7) are not arbitrary.
Retain the normalized coefficients from121, now decorating the first
linear coefficient as alpha and the second as beta to distinguish
them from the actual function a and the cubic coefficients a_i.
Let a hat on a relative element denote the normalized partial,w frame.
The normalized rho coefficient is Ahat=a/(2id); its constant W
coefficient is C0/(2i). The exact coefficient formulas are

\[
\begin{gathered}
\ell=4\lambda d,\qquad
\alpha=-\frac{\partial\ell}{4\ell}=-\frac{D'}{8D\kappa},\quad
\beta=-\frac{\partial c}{\ell}=-\frac{c'}{4\lambda d\kappa},\qquad
k=-\frac{qe}{3\ell},\\
j=-\frac{q(4\widehat A-\partial^2\widehat A
                        +e\partial\widehat A)}{2\ell}
  =-\frac{iqD a''}{4\lambda\Delta},\qquad
\widehat A=\frac{a}{2id},\\
n=\frac{\partial j+8\alpha j-2ej}{6k}
 =\frac{2id\,a'''}{D'''},\qquad
\partial\beta+4\alpha\beta-e\beta-4jn=0 .
\end{gathered}
\tag{8}
\]

For the j formula, substitute Ahat and the exact derivative in (2)
on coefficient-field elements. Equivalently, transform the quadratic
coefficient of the original potential, where B11=-a''Y, into the
normalized relative frame. The latter equality follows directly from
G11=g g_hh and rho-Yrho_Y=C0/g, so the C0 terms in
rho G11-rho_hh-YG11rho_Y cancel.

To check the n simplification, write
j=(-iq/(4lambda))D a''/Delta. Multiplying its numerator in (8)
by kappa gives j'-(D'/D)j-2e0j. Since 2e0=-Delta'/Delta,
the derivatives of its D/Delta coefficient cancel and this is
(-iq/(4lambda))(D/Delta)a'''. The displayed k and
e0=D D'''/(4Delta) then give n exactly.

For the last equation multiply by kappa. Its first three terms
become beta'-(d'/d+e0)beta. In the coefficient of c', the identity
2d'/d+kappa'/kappa+e0=0 cancels every first derivative of D.
Substituting j and n and using kappa squared=Delta/(4D squared)
therefore gives

\[
\boxed{\quad
c''=-\frac{2q}{D'''}a''a''',\qquad
c'+\frac{q}{D'''}(a'')^2=\eta\in\mathbb C .
\quad}
\qquad
R\big|_{v=0}=M_0 gY+\frac{2a'''}{D'''}g^2,\quad M_0\in L .
\tag{9}
\]

The second equality in the box follows by differentiation and the
constant field of L, because D''' is constant and nonzero. No
primitive of (a'') squared is asserted: the actual c exists, and
(9) is the constraint it satisfies.

For the constant coefficient of R, the normalized calculation121
gives Rhat at vhat=0 equal to m(w squared+1)+n with m in L'.
Equation(2) gives vhat=kappa v and
R=-(D'Y/(2D))v+g Rhat/(dw). Hence at v=0 the normalized constant
coefficient becomes i(2m+n)gY-in g squared/d. The n formula in
(8) proves (9) with M0=i(2m+n). This coefficient lies in K and
has zero Y-derivative, so the full constant-field property puts M0
in L. The unused nonzero constant volume condition121 still applies;
M0 and the functions in (9) are not declared freely realizable.

The author separately checked three exact finite identities by an
inline symbolic calculation: the displayed j, the n simplification,
and the conversion of the last normalized scalar equation to the
first boxed equation in (9). The command started in7bad3b and
completed with all three certificates passing and exit zero in
fcd3d6. This was not a new unittest suite, a field-constant proof,
or an original-frame realization test.

## 6. Exact scope

The new conclusions are (4), (5), their original-coordinate
combination (7), and the further coefficient restrictions (9).
They use the supplied actual potential and volume
equations; speed or metric identities alone do not prove them.
The prior global contraction aY squared in S from122 remains
available, but is not silently strengthened to a in S or c in S.

In particular the summand lambda g/Y is distinguished and has
nonzero complex coefficient. The statement does not assert that
Psi0 has an uncancellable pole at every divisor of Y. Other
coefficient-field terms in (7) can have poles and must be analyzed
at the chosen divisor before taking residues. No claim that h
is a polynomial coordinate, generates L, or has only simple poles
is used. No polynomial shear by x transposed Qx is asserted.

No new recognition theorem or general cancellation conclusion follows
from this calculation alone. All files through122 remain unchanged.
