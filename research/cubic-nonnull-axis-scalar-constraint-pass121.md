# The non-null cubic axis has the same scalar classification

Under the supplied actual exact cubic hypotheses, a non-null constant
axis forces the scalar D of the normal forms121 to be either a cubic
polynomial or a quadratic polynomial plus a nonzero reciprocal
affine-linear term. In particular D belongs to C(h), although that
rationality is not assumed. The remaining potential and volume
coefficients supply the restriction.

This is a necessary condition within the actual constant-acceleration
framework. It does not establish that an arbitrary cancellation
instance has such a frame, exclude either scalar form globally, or
construct an original polynomial inverse.

## 1. The coefficient fields and a normalized conic frame

Retain the actual generation and volume hypotheses of
[potential90](nonconical-quadratic-potential-pass90.md),
[cubic-relation90](nonconical-cubic-relation-pass90.md), and the
non-null case of [scalar normal forms121](cubic-axis-scalar-normal-forms-pass121.md).
Write Y for the third polynomial velocity entry, to distinguish it
from the relative curve generators. Thus

\[
\begin{gathered}
b=(g,hY,Y)^t\in S^3,\quad S=\mathbb C[s,t],\quad K=\operatorname{Frac}S,
\quad g^2-DY^2=1,\\
L\subset K,\quad L/\mathbb C(h)\text{ finite separable},\quad
L\text{ relatively algebraically closed in }K,\\
Q=\operatorname{diag}(-1,M),\quad
M=\begin{pmatrix}D_{hh}/2&(D_h-hD_{hh})/2\\
(D_h-hD_{hh})/2&D-hD_h+h^2D_{hh}/2\end{pmatrix},\\
\Delta=\det Q=(D_h^2-2DD_{hh})/4\ne0,\quad
D\ne0,\quad D_{hhh}\ne0,\quad \Delta_h=-DD_{hhh}/2.
\end{gathered}
\tag{1}
\]

Subscript h means the unique extension of d/dh. Adjoin square roots
of D and Delta to obtain a finite field L' over L. Its h-derivative
has constants C. Indeed, for a constant algebraic element, differentiating
its monic minimal polynomial shows that every coefficient is constant;
C is algebraically closed. The regular extension K/L permits the
field compositum K'=KL', with L' relatively algebraically closed in K'.
The same base-extension argument is recorded in
[the conic-axis proof120](cubic-nondegenerate-conic-axis-pass120.md).
For the underlying irreducibility statement see Stacks, Lemma
10.47.8; characteristic zero also makes these algebraic base changes
reduced.[^1]

Set

\[
\begin{gathered}
p_0=\tfrac12(1,h/\sqrt D,1/\sqrt D)^t,\quad
q_0^{\mathrm{vec}}=\tfrac12(1,-h/\sqrt D,-1/\sqrt D)^t,\\
P=-i p_0,\quad U=i q_0^{\mathrm{vec}},\quad
w=i(g+\sqrt D\,Y),\quad
\kappa=\frac{\sqrt\Delta}{2D},\quad r=P_h/\kappa,\\
b=Pw+U/w,\quad Q(P,P)=Q(U,U)=0,\quad Q(P,U)=-1/2,\\
Q(r,r)=1,\quad Q(P,r)=Q(U,r)=0,\\
P_h=U_h=\kappa r,\quad
r_h=2\kappa(P+U)+e_0r,\quad e_0=-\Delta_h/(2\Delta),\\
\partial=\kappa^{-1}\partial_h,\quad e=e_0/\kappa\ne0,\qquad
\partial P=\partial U=r,\quad \partial r=2P+2U+er.
\end{gathered}
\tag{2}
\]

These identities follow by differentiating the displayed vectors and
using (1). For example Q((p0)h,(p0)h)=-Delta/(4D squared), so the
factor -i makes the displayed r have norm one. Differentiating that
norm with Qh gives e0. The two coefficients of P and U in rh are
then determined by differentiating their orthogonality to r. The
relation g squared minus D Y squared equal to one gives the inverse
of g+sqrt(D)Y and verifies b=Pw+U/w.

The variable w is transcendental over L': otherwise b would lie in
a one-variable algebraic coefficient field, contradicting the actual
nonzero frame determinant. Therefore K' is finite separable over
L'(w). Extend the h-derivative by fixing w, and the w-derivative by
killing L'. Their extensions to K' commute and the full w-constant
field is L'. The derivative partial in (2) also commutes with the
w-derivative, since kappa belongs to L'. Its constants on L' are C.

The derivative partial need not have an algebraic primitive. No
coordinate with derivative one is asserted. All subsequent prime
symbols mean partial, unless an h subscript is displayed explicitly.
This is an invertible rational change of the two commuting base
derivations. The relative ring is still K'[v,u]; no v-dependent
element is inverted. The reconstruction, potential, and volume
identities can be derived in this frame by the product rule and
commutation alone. Its volume determinant differs from the original
one only by a member of K'*. This is not an ambient polynomial
coordinate change.

## 2. Actual connection and potential in the normalized frame

Put Z=w+1/w, W=w-1/w, and ell=Zw/Z. Differentiating b in (2)
and expanding in (b,partial b,bw) gives

\[
\begin{gathered}
G=\operatorname{diag}(Z^2,w^{-2}),\quad
C^1_{11}=e,\quad C^1_{12}=\ell,\quad C^1_{22}=0,\\
C^2_{11}=-w^2ZZ_w,\quad C^2_{12}=0,\quad C^2_{22}=-1/w,\\
T_{111}=2eZ^2\ne0,\quad T_{112}=T_{122}=T_{222}=0,\\
\rho=A Z+B W,\quad A\in L',\quad B\in\mathbb C,\qquad
\mathsf B_{11}=Z(4A-A''+eA').
\end{gathered}
\tag{3}
\]

The first three lines also specialize the independently derived
moving-frame formulas120. For the last line, the potential's pure
cubic term forces the first relative generator to be linear; put
v=y1 and y2=R of degree three. Its sixth and fourth coefficients give
B22=B12=0. The first is the Euler equation
rho/w squared-rho_ww-rho_w/w=0, whose two algebraic first integrals
give rho=A1 w+B1/w with A1,B1 in L'. The second is
-rho'_w+ell rho'=0, which gives A1'=B1'. Thus (A1-B1)/2 is the
complex constant B and (A1+B1)/2 is A. Substitution gives B11.

Write Li for the derivatives of Psi0=chi+q rho squared/2, where
q in C* denotes the original scalar acceleration. The potential
then reads L1 v+L2 R+(q/2)B11 v squared+(q/3)eZ squared v cubed=zeta.
Here L2 is nonzero, as follows already from the nonzero cubic term
and the linearity of v.

## 3. Exactness and lower volume coefficients

The full volume identity in this frame, with Omega the actual
frame determinant, is

\[
\begin{gathered}
\mathcal V:=\mathcal J/(\Omega L_2)
=R'+R_vR_w-w^2ZZ_wv-evR_v
          +(-1/w-\ell)RR_v-\ell vR_v^2\in K'^*,\\
R=r_0+r_1v+r_2v^2+r_3v^3,\quad
r_3=k wZ^4,\quad r_2=j wZ^3,\quad k\in L'^*,\ j\in L',\\
L_2=\frac{l}{wZ^2},\quad l\in L'^*,\quad
k=-\frac{qe}{3l},\quad
j=-\frac{q(4A-A''+eA')}{2l},\\
\Psi_0=\frac{lW}{4Z}+C,\quad C\in L',\qquad
r_1=a wZW+b_1 wZ^2,\quad a=-\frac{l'}{4l},\quad b_1=-\frac{C'}l.
\end{gathered}
\tag{4}
\]

The fifth and fourth coefficients in v give the respective
w-derivative equations for r3 and r2, as in120. Dividing them by
wZ to the appropriate powers puts k and j in the full constant
field L'. The cubic potential coefficient gives L2. Since
(W/Z)w=4/(wZ squared), integrating the exact derivative of Psi0
gives the displayed expression, with its remaining term C in L'.
The formula for r1 is -L1/L2.

Expand the remaining coefficients in (4). The third coefficient,
then the second, then the first and constant ones give

\[
\begin{gathered}
k'/k+12a-3e=0,\\
r_0=m(w^2+1)+n,\quad m\in L',\quad
n=\frac{j'+8aj-2ej}{6k},\\
[v]\mathcal V=wZ\bigl[(a'+4a^2-ae-1)W
                    +(b_1'+4ab_1-b_1e-4jn)Z\bigr]=0,\\
a'+4a^2-ae-1=0,\qquad b_1'+4ab_1-b_1e-4jn=0,\\
\mathcal V=m'(w^2+1)+n'-2an(w^2-1)-2b_1n(w^2+1)\ne0.
\end{gathered}
\tag{5}
\]

For the second assertion, its coefficient equation is exactly
r0w-2w r0/(w squared+1)=-2n w/(w squared+1). The derivative of
(r0-n)/(w squared+1) vanishes, so m lies in L'. For the third line,
W and Z are independent over L' because w is transcendental. Thus
both displayed scalar equations are necessary. The remaining
nonzero constant coefficient is kept as a constraint, not discarded
as an automatically realizable unit.

Put z0=1/l. Combining the equation for a with the equation for k,
and using k=-qe z0/3, gives two necessary scalar equations:

\[
z_0''-e z_0'-4z_0=0,\qquad
\frac{e'}e+4\frac{z_0'}{z_0}-3e=0,\qquad z_0\in L'^*.
\tag{6}
\]

## 4. Returning to h removes the apparent differential complexity

In this section use only h subscripts. By (2), partial is
kappa inverse times the h-derivative and e=e0/kappa. Consequently
the first equation (6), multiplied by kappa squared, becomes
z0_hh-(kappa_h/kappa+e0)z0_h-4kappa squared z0=0.
But kappa_h/kappa+e0=-Dh/D and 4kappa squared=Delta/D squared.
It follows that

\[
\begin{gathered}
(z_0)_{hh}+\frac{D_h}{D}(z_0)_h-\frac{\Delta}{D^2}z_0=0,
\qquad (\sqrt D\,z_0)_{hh}=0,\\
z_0=\frac{a_1h+a_0}{\sqrt D},\quad a_1,a_0\in\mathbb C,
\quad (a_1,a_0)\ne(0,0),\\
e=\frac{D^2D_{hhh}}{2\Delta^{3/2}},\qquad
e z_0^4=\frac{D_{hhh}(a_1h+a_0)^4}{2\Delta^{3/2}},\\
\left(D_{hhh}(a_1h+a_0)^4\right)_h=0,\qquad
D_{hhh}=\frac{c_*}{(a_1h+a_0)^4},\quad c_*\in\mathbb C^*.
\end{gathered}
\tag{7}
\]

The equivalence in the first line follows by differentiating
sqrt(D)z0 twice and using (1). The constants in its solutions are
complex because the h-constant field of L' is C. For the third
line use Delta_h=-D Dhhh/2. The second equation (6), multiplied
by kappa, says that the h-logarithmic derivative of e z0 to the
fourth power is 3e0=-3Delta_h/(2Delta). Substituting the third
line cancels that Delta term and gives the last line. No logarithm
or antiderivative outside the algebraic coefficient field is used.

Integrating that explicit third derivative within L' now gives

\[
\begin{array}{ll}
a_1=0:&D=d_3h^3+d_2h^2+d_1h+d_0,
\quad d_i\in\mathbb C,\ d_3\ne0,\\[4pt]
a_1\ne0:&D=d_2h^2+d_1h+d_0+\displaystyle\frac{c}{a_1h+a_0},
\quad d_i,c\in\mathbb C,\ c\ne0.
\end{array}
\tag{8}
\]

In the second case c=-c*/(6a1 cubed). Subtracting the displayed
reciprocal term leaves an element with zero third derivative.
Successive subtraction of quadratic, linear, and constant complex
terms proves the assertion without assuming rationality. Thus D
lies in C(h) already in the original coefficient field L. The
nonzero determinant condition (1) remains imposed.

## 5. Scope of the classification

Together with [the null-axis calculation121](cubic-null-axis-scalar-constraint-pass121.md),
this proves the same two scalar types for either constant axis.
The proof does not identify h as a polynomial coordinate or as the
full generator of L. The extra square roots and the normalized
derivative occur only in the coefficient-field reconstruction.
Neither is claimed to define a polynomial automorphism.

The classification does not supply the unused potential data,
their global regularity, or a polynomial inverse for the four
original coordinates. Even eliminating this entire cubic branch
would leave the unrestricted frame-entry problem. It is therefore
not a proof of cancellation or a novelty-cleared theorem.

The identities admit exact symbolic checks of the finite frame,
potential, and volume calculations. Such checks do not establish
the actual framework or replace the differential-field and global
hypotheses. Files through120 remain unchanged.

## Sources

[^1]: The Stacks Project, [Lemma 10.47.8, tag 037P](https://stacks.math.columbia.edu/tag/037P),
    geometric irreducibility from relative algebraic closedness.
    The lemma and proof were freshly read for this coefficient-field
    step. It is not a source for the new scalar classification or
    a cancellation result.
