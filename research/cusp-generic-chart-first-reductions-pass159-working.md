# First actual generic-chart reductions for the cusp initial relation

**Status: working chart and coefficient reductions, not cusp recognition.**

An actual sliced four-ring with E-time degrees \((1,1,2,2)\)
and full initial kernel \((XZ-Y^3)\) has the generic chart below.
Its relative Jacobian is exactly \(-a^3\) when the selected
intrinsic derivation satisfies \(Nv=1\).
The three highest determinant coefficients integrate over the
exact coefficient field. In the main branch the next coefficient
gives a plane relation of degree at most four, with unit gradient
on the selected whole affine line.

These statements do not identify every factor of that relation
with the selected line. Nor do they construct an integral
low-weight invariant correction in the original polynomial ring.
All158 and earlier artifacts remain unchanged.

## 1. Actual hypotheses and the selected intrinsic line

Assume
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\\
(\deg_E X,\deg_E Y,\deg_E Z,\deg_E W)=(1,1,2,2),\\
a=EX,\quad b=EY,\quad e=E^2Z/2,\quad d=E^2W/2,\\
\theta_0:(\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
 \longmapsto(a\eta,b\eta,e\eta^2,d\eta^2),\qquad
\ker\theta_0=(\mathsf X\mathsf Z-\mathsf Y^3).
\end{gathered}
\tag{1}
\]
The four displayed generators of \(B\) are actual polynomial
coordinates. The source of \(\theta_0\) is a formal polynomial
four-ring with weights \((1,1,2,2)\), and \(\eta\) is independent
over \(A\). All four ordinary leading coefficients are nonzero.
In particular \(ae=b^3\); the factors of two in (1) are essential.
The ideal assertion is the full initial kernel, not one vanishing
leading equation.

Take the actual partial \(T=\partial_Z\), holding \(X,Y,W\)
fixed. The exact cofactor and initial-projection result157 gives[^1]
\[
\begin{gathered}
T(A)\subset A[u]_{\le3},\qquad T(u)\in A[u]_{\le3},\\
0\ne N=[u^3]T|_A\in\operatorname{LND}_{\mathbb C}(A),\qquad
N(a)=N(b)=N(e)=N(d)=0 .
\end{gathered}
\tag{2}
\]
Its exact shift is three because the full initial relation
involves \(Z\). Equivalently the other three initials
\(a\eta,b\eta,d\eta^2\) are algebraically independent.
This input comes from the actual volume and a specialization
of an actual Laurent conjugate of \(T\), not from asserting
local nilpotence after arbitrary localization.

Set \(S=\ker_A N\), \(L=\operatorname{Frac}S\), and
\(F=\operatorname{Frac}A\). An intrinsic local slice gives
\(q\in A\), \(Nq=h\ne0\), \(Nh=0\). Put \(v=q/h\).
The finite local-slice expansion implies
\(A_h=S_h[v]\), hence
\[
\begin{gathered}
A_L:=S^{-1}A=L[v],\qquad F=L(v),\qquad Nv=1,\\
\tau=b/a,\qquad \rho=d/a^2,\qquad
\tau,\rho\text{ algebraically independent over }\mathbb C,\\
L/\mathbb C(\tau,\rho)\text{ finite and separable}.
\end{gathered}
\tag{3}
\]
Here \(S^{-1}\) means localization at all nonzero elements of
\(S\). No polynomial-plane theorem for \(S\) is needed.

For the field assertions, the other triple's initial field is
\(\mathbb C(a\eta,\tau,\rho)\). The first element is
transcendental over \(F\), so the triple's rank three proves
independence of the two ratios. They lie in \(L\) by (2).
The local slice gives \(\operatorname{trdeg}_{\mathbb C}L=2\).
Also \(F\) is finitely generated because \(A\simeq B/(u)\),
so \(F\) is finite over \(\mathbb C(\tau,\rho)(v)\).
Any finite set linearly independent over \(\mathbb C(\tau,\rho)\)
in \(L\) stays independent after adjoining the transcendental
\(v\). This proves finiteness in (3); characteristic zero gives
separability. Thus no unproved finite generation of \(S\)
is being used in that step.

Extend \(\partial_\tau,\partial_\rho\) uniquely from the rational
base field to \(L\), and then to \(L[v]\) by fixing \(v\).
They commute with each other and with \(\partial_v=N\).
All coefficient derivatives below use precisely these extensions.

## 2. The actual fixed-X presentation and its determinant

Since \(Ea=0\), \(E/a\) is an LND of \(B_a\) with slice \(X\).
Its finite Taylor projection gives
\[
\begin{gathered}
B_a=A_a[X],\qquad A_a=\mathbb C[y,z,w]_{a_0},
\qquad a=a_0(y,z,w),\\
Y=y+\tau X,\qquad
Z=z+\sigma X+\tau^3X^2,\qquad
W=w+\vartheta X+\rho X^2,\\
y,z,w,\sigma,\vartheta\in A_a\subset L[v],
\qquad L[y,z,w]=L[v].
\end{gathered}
\tag{4}
\]
Indeed quotienting \(B_a=A_a[X]\) by \(X\) identifies \(A_a\)
with \(\mathbb C[Y,Z,W]_{a(0,Y,Z,W)}\). This ring is nonzero,
so the displayed denominator \(a_0\) is nonzero and the three
projected coordinates are algebraically independent over
\(\mathbb C\). The coefficient of \(X^2\) in \(Z\) is
\(e/a^2=b^3/a^3=\tau^3\), and that in \(W\) is \(\rho\).
After localization at \(S\setminus\{0\}\), the sole denominator
\(a_0=a\in L^*\) disappears, proving the whole-line equality
in (4). In particular it is not an assertion about only an
open subset of that line.

Both the Taylor map and its inverse in (4) are actual localized
polynomial-ring maps. Their Jacobians with respect to
\((X,y,z,w)\) and \((X,Y,Z,W)\) are inverse units.
After pullback, such a unit of \(A_a[X]\) is independent of
\(X\), and evaluation at \(X=0\) makes it one.
Thus the determinant in \((y,z,w)\) is one for every \(X\).
The chain rule over the finite separable extension now shows
that the following determinant is independent of \(X\):
\[
\begin{gathered}
J(X)=\det
\begin{pmatrix}
X+y_\tau&y_\rho&y_v\\
3\tau^2X^2+\sigma_\tau X+z_\tau&\sigma_\rho X+z_\rho&\sigma_vX+z_v\\
\vartheta_\tau X+w_\tau&X^2+\vartheta_\rho X+w_\rho&\vartheta_vX+w_v
\end{pmatrix}
=J_0,\\
T(v)=-\frac{(X+y_\tau)(X^2+\vartheta_\rho X+w_\rho)
 -y_\rho(\vartheta_\tau X+w_\tau)}{J_0},\qquad
J_0=-a^3\in L^* .
\end{gathered}
\tag{5}
\]
The matrix rows are \((Y,Z,W)\), columns \((\tau,\rho,v)\),
with \(X\) fixed. This specifies the sign convention.
The determinant is nonzero because both triples are separating
coordinates for \(F/\mathbb C\).

For the last equality, write \(X=x_0+au\), \(x_0\in A\).
The quotient rule extends (2) to \(F\), with leading
coefficient \(N\). Re-expanding in \(X\) therefore gives
\([X^3]T(v)=Nv/a^3=1/a^3\).
The displayed cofactor has leading coefficient \(-1/J_0\).
Comparison proves the stated normalization. Neither a guessed
relative determinant nor a formally chosen frame supplies (5).

## 3. The X-four and X-three coefficients integrate

The determinant in (5) has degree at most four. Direct expansion
gives \([X^4]J=3\tau^2y_v-\sigma_v\). Thus there is \(k\in L\)
with \(\sigma=3\tau^2y+k\).
After this substitution its degree-three coefficient is
\((6\tau y+k_\tau)y_v+k_\rho\vartheta_v-z_v\).
Since all positive coefficients vanish, integration in \(L[v]\)
gives \(n\in L\) and
\[
\begin{gathered}
\sigma=3\tau^2y+k,\qquad
z=3\tau y^2+k_\tau y+k_\rho\vartheta+n,\qquad k,n\in L,\\
XZ-Y^3=-y^3+
 (k_\tau y+k_\rho\vartheta+n)X+kX^2 .
\end{gathered}
\tag{6}
\]
The final identity is a literal equality in \(L[v][X]\).
It bounds the time degree of the original cusp polynomial by
two, not by zero. No invariant correction is inferred from it.
Integration used only \(\ker_{L[v]}\partial_v=L\), without
division by \(y_v\) or \(\vartheta_v\).

## 4. The X-two coefficient has an exact potential

For a coefficient \(c\in L\), use formal, independent variables
\(U,V\) and put
\(H_j(c;U,V)=\sum_{i=0}^j
c_{\tau^i\rho^{j-i}}U^iV^{j-i}/(i!(j-i)!)\).
Define
\[
\begin{gathered}
r=k_\rho,\qquad
f(U,V)=U^3+H_2(k;U,V)+H_1(n;U,V),\\
B_1=f_U=3U^2+k_{\tau\tau}U+k_{\tau\rho}V+n_\tau,\qquad
A_1=f_V=k_{\tau\rho}U+k_{\rho\rho}V+n_\rho,\\
r w+f(y,\vartheta)=\ell,\qquad \ell\in L .
\end{gathered}
\tag{7}
\]
The subscripts on \(A_1,B_1\) are labels for these formal
polynomials, not coefficient derivatives or elements of the
original ring \(A\).

Here is a differential verification that also controls the
lower determinant coefficients. Take total differentials over
\(\mathbb C\) in \(F\), treating \(X\) as fixed, and write
\(q=d\vartheta+X\,d\rho\).
Using (6), subtract
\((3\tau^2X+6\tau y+k_\tau)dY\) from \(dZ\).
The three wedge rows become
\[
dY=dy+X\,d\tau,\qquad
dZ_{\rm red}=r q+B_1(y,\vartheta)d\tau+A_1(y,\vartheta)d\rho,
\qquad dW=dw+Xq .
\tag{8}
\]
This row subtraction preserves their wedge and determinant.
Its \(X^2\) coefficient is
\(d\tau\wedge d\rho\wedge
(r\,dw+B_1\,dy+A_1\,d\vartheta)\).
Its scalar coefficient in \(d\tau\wedge d\rho\wedge dv\)
is \(r w_v+f_U y_v+f_V\vartheta_v\), precisely
\(\partial_v(rw+f(y,\vartheta))\). Vanishing and integration
prove (7), including when \(r=0\).

## 5. When r is nonzero, X-one gives a nonzero quartic relation

Assume \(r\ne0\), and define formal polynomials over \(L\):
\[
\begin{gathered}
\omega(U,V)=\frac{\ell-f(U,V)}r,\qquad
g_3(U,V)=H_3(k;U,V)+H_2(n;U,V),\\
\Phi(U,V)=A_1(U,V)\omega(U,V)+g_3(U,V)
 -\ell_\tau U-\ell_\rho V,\\
\Phi_U=f_\tau-\ell_\tau+r_\tau\omega-A_1B_1/r,\qquad
\Phi_V=f_\rho-\ell_\rho+r_\rho\omega-A_1^2/r,\\
[X]J=\partial_v\Phi(y,\vartheta)=0,\qquad
\Phi(y,\vartheta)=m\in L,\qquad \deg_{U,V}\Phi\le4,\\
\Phi_4(U,V)=-\frac{(r_\tau U+r_\rho V)U^3}{r} .
\end{gathered}
\tag{9}
\]
Coefficient partials \(f_\tau,f_\rho\) in (9) hold formal
\(U,V\) fixed. The homogeneous component \(\Phi_4\) may be
zero. No assertion that the actual relation has degree four
is included.

For the derivative identities, \((g_3)_U=f_\tau\) and
\((g_3)_V=f_\rho\); the coefficient derivative of \(U^3\)
is zero. Also \((A_1)_U=r_\tau\), \((A_1)_V=r_\rho\),
\(\omega_U=-B_1/r\), and \(\omega_V=-A_1/r\).
These give both formulas by the product rule.

For the determinant coefficient, differentiate (7) totally:
\[
r\,dw=-B_1\,dy-A_1\,d\vartheta+L_\tau\,d\tau+L_\rho\,d\rho,
\qquad L_i=\ell_i-f_i-r_iw\quad(i=\tau,\rho),
\]
with formal polynomials evaluated at \((y,\vartheta)\).
Insert this expression in the \(X\) coefficient of (8).
The terms involving \(dy\wedge d\rho\wedge d\vartheta\)
and \(dy\wedge d\tau\wedge d\vartheta\) cancel. The remainder is
\(d\tau\wedge d\rho\wedge
(\Phi_U\,dy+\Phi_V\,d\vartheta)\), proving (9).
This proves closedness by an explicit potential, not by a
formal integration assumption about the coefficient field.

Equations (6)--(7) imply
\(L[y,z,w]\subset L[y,\vartheta]\). The reverse containment
in \(L[v]\) follows from (4), so
\(L[y,\vartheta]=L[v]\). In particular the evaluation kernel
\(L[U,V]\to L[v]\) is a principal prime \((G)\), with
\(G\) irreducible.

The constant determinant gives the stronger evaluated identity
\[
\begin{gathered}
C_U\Phi_U(y,\vartheta)+C_V\Phi_V(y,\vartheta)=-a^3,\\
C_U=(\vartheta_\rho+A_1(y,\vartheta)/r)y_v-y_\rho\vartheta_v,\qquad
C_V=y_\tau\vartheta_v-(\vartheta_\tau+B_1(y,\vartheta)/r)y_v,
\qquad C_U,C_V\in L[v].
\end{gathered}
\tag{10}
\]
Indeed the constant wedge after the same substitution is
\[
-\Phi_U\,dy\wedge d\vartheta\wedge d\tau
-\Phi_V\,dy\wedge d\vartheta\wedge d\rho
+(A_1\Phi_U-B_1\Phi_V)dy\wedge d\tau\wedge d\rho/r.
\]
Taking its \(d\tau\wedge d\rho\wedge dv\) coefficient yields
(10) with the sign convention in (5).

It follows that \(\Phi-m\) is a nonzero formal polynomial,
that \(G\mid\Phi-m\), and that the selected factor \(G\)
has multiplicity one. If \(\Phi-m=GH\), both evaluated
gradient entries have the factor \(H(y,\vartheta)\).
Equation (10) therefore forces
\(H(y,\vartheta)\in L[v]^*=L^*\).
This is not the statement that \(H\) is constant in
\(L[U,V]\): a nonconstant cofactor can restrict to a unit
on the selected line. Thus (9)--(10) do not prove
\(\Phi-m\sim G\).

## 6. The two branches when r is zero

If \(r=k_\rho=0\), its mixed and second \(\rho\) derivatives
also vanish. Equations (6)--(7) read
\[
\begin{gathered}
z=3\tau y^2+k_\tau y+n,\\
y^3+\tfrac12k_{\tau\tau}y^2+n_\tau y+n_\rho\vartheta=\ell .
\end{gathered}
\tag{11}
\]
If \(n_\rho\ne0\), this makes \(\vartheta\) a polynomial
in \(y\) over \(L\). The first equation does the same for
\(z\), so the whole-line equality is \(L[y,w]=L[v]\).
No degree bound for this embedding follows from (11) alone.

If \(n_\rho=0\), the monic cubic equation in (11) makes
\(y\) algebraic over \(L\), hence \(y\in L\), since it
belongs to \(L[v]\). Then \(z,\sigma\in L\) by (6).
The determinant (5) reduces to the product
\[
J(X)=M(X)(w_v+\vartheta_vX)=-a^3,\qquad
M(X)=\det\begin{pmatrix}Y_\tau&Y_\rho\\Z_\tau&Z_\rho\end{pmatrix}
\in L[X].
\tag{12}
\]
Both factors are nonzero polynomials in the domain \(L[v][X]\).
Their product is a unit, so each has \(X\)-degree zero.
Thus \(\vartheta_v=0\), \(M\in L^*\), and
\(w_v=-a^3/M\in L^*\).
Consequently \(y,z,\sigma,\vartheta\in L\), while
\(w\) is an affine linear parameter for \(L[v]\).
This is a generic-fiber conclusion only; it does not descend
that parameter to a polynomial slice on \(A\).

## Scope and sources

The whole-line presentation, determinant calibration and potentials
above use the original polynomial inverse through (4)--(5).
They are not consequences of an arbitrary formal determinant-one
system. They retain the exact field \(L\), including its possibly
nontrivial finite extension of \(\mathbb C(\tau,\rho)\).

The first reductions leave additional coefficient constraints
and the actual integral correction problem open. In the branch
\(r\ne0\), even the nonzero plane relation with selected unit
gradient has a possible extra-factor issue. The existence gate
for a low-weight cusp invariant in158 is not being supplied by
any of these identities.[^3]
No arbitrary entry, unrestricted cancellation, historical novelty,
human expert review or proof-assistant certification is claimed.

1. [Two-linear/two-quadratic initial bound157](two-linear-two-quadratic-initial-bound-pass157-working.md),
   Sections 1--3 and 8, supplies (2) and the exact occurring-pivot
   shift. [Cubic actual normal forms157](two-linear-cubic-normal-forms-pass157-working.md),
   Section 3, supplies the normalized hypothesis (1) when its
   surviving cusp case applies.
2. [Actual dense Taylor chart139](dense-all-degree-taylor-chart-pass139-working.md),
   Sections 1--3, contains the local-slice, finite-field and
   actual Jacobian mechanisms. Those mechanisms are reconstructed
   here with two quadratic slots and a cubic cofactor. Its
   three-good theorem is not being applied to this two-good frame.
3. [Cusp low-weight invariant gate158](cusp-cubic-low-weight-invariant-gate-pass158-working.md).
   That gate assumes the existence of a nonconstant invariant
   of source weight at most three; this note does not prove it.

The new coefficient identities and their orientations are proved
above. No finite checker execution is used as proof, and no
recursive re-audit of retained source dependencies is claimed.

[^1]: Source 1. The related actual chart mechanism is Source 2.
[^3]: Source 3.
