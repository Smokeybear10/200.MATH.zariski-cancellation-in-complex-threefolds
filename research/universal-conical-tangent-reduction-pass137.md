# A speed-based tangent chart for nonlinear conical frames

The tangent-graph construction does not require nonradial acceleration.
Using a nonzero good speed as the second coefficient parameter, the
selected partial's linear coefficient forces the tangent relation
directly. This supplies the same polynomial-coefficient reduction for
every supplied nonlinear conical rank-two three-good quadratic frame.

The consequence, combined with the separately proved monic-pencil
descent and linear-invariant obstruction, is nonexistence of that
supplied nonlinear conical profile with a global slice. No assertion
about entry into this coordinate profile from an arbitrary cylinder
is made.

## 1. Hypotheses and a coefficient basis made from speeds

Suppose
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\\
E^2X=E^2Y=E^2Z=0,\qquad E^3W=0,\\
s=EX,\quad t=EY,\quad b=EZ,\quad q=E^2W,\\
\operatorname{trdeg}_{\mathbb C}\mathbb C(s,t,b)=2,\qquad
\ker\bigl(\mathbb C[S,T,B_0]\to A,\ (S,T,B_0)\mapsto(s,t,b)\bigr)=(H),
\end{gathered}
\tag{1}
\]
where \(H\) is irreducible homogeneous of degree at least two.
The four original generators are actual polynomial coordinates.
The slice \(u\) is not assumed to be an ambient coordinate.
The acceleration \(q\) may be zero, and no radial identity or
inequality is assumed.

Let \(T=\partial_W\), holding the three original goods fixed.
The selected-partial theorem135 gives exact adjoint degree one,
\[
T(A)\subset A[u]_{\le1},\qquad T(u)\in A[u]_{\le1},\qquad
N=[u]T|_A\in\operatorname{LND}(A)\setminus\{0\},\qquad
N(s)=N(t)=N(b)=N(q)=0 .
\tag{2}
\]
Its degree-zero alternative would give a homogeneous linear speed
relation, contrary to (1). These conclusions do not require
nonzero acceleration.[^1]

Put \(S_0=\ker_A N\) and \(L=\operatorname{Frac}S_0\).
An intrinsic local slice gives
\(\operatorname{Frac}A=L(v_0)\), and \(L\) has transcendence degree
two. The extension \(L/\mathbb C(s,t,b)\) is finite and separable:
adjoin \(v_0\) to two independent speeds, then use finite generation
of \(\operatorname{Frac}A\) and preservation of linear independence
under adjoining the transcendental \(v_0\).

There is no zero speed or constant ratio of two speeds, since either
would give a linear homogeneous relation. Define
\[
\tau=t/s,\qquad \rho=b/s,\qquad \xi=s,\qquad \sigma=q/s^2.
\quad
L/\mathbb C(\tau,\xi)\text{ is finite and separable},\qquad
\rho\text{ is algebraic over }\mathbb C(\tau).
\tag{3}
\]
To verify the field assertions, the nonzero dehomogenization
\(H(1,T,B_0)\) relates \(\tau,\rho\), while \(\tau\) is
nonconstant. Thus \(\mathbb C(\tau,\rho)\) has transcendence
degree one. If \(s\) were algebraic over \(\mathbb C(\tau)\),
then the whole speed field
\(\mathbb C(s,t,b)=\mathbb C(s,\tau,\rho)\) would have
transcendence degree one, contradicting (1).
Hence \(\tau,\xi\) are independent and give (3).

Extend \(\partial_\tau,\partial_\xi\) uniquely through the finite
separable extension \(L/\mathbb C(\tau,\xi)\). They commute,
and \(\partial_\xi\rho=0\). Write \(\rho'=\partial_\tau\rho\)
and \(r=\rho''\).
Nonlinearity implies \(r\ne0\): the constants of the derivative
in a finite algebraic extension of \(\mathbb C(\tau)\) are
\(\mathbb C\), as follows by differentiating a monic minimal
polynomial. Thus \(\rho''=0\) would imply
\(\rho=c_1\tau+c_0\), a forbidden linear speed relation.
In contrast, \(\sigma\) is just an arbitrary element of \(L\);
neither its independence nor a nonzero partial derivative is used.

## 2. Actual localization, the leading derivation, and the whole line

Localize at the invariant \(s\), and use \(D=E/s\), with \(DX=1\).
If \(b_X=X-su\in A\), the slice theorem and Taylor projection give
\[
\begin{gathered}
B_s=A_s[X],\qquad
A_s=\mathbb C[y,z,w]_{s_0(y,z,w)},\qquad s=s_0(y,z,w),\\
s_0(Y,Z,W)=s(0,Y,Z,W)\ne0,\\
Y=y+\tau X,\qquad Z=z+\rho X,\qquad
W=w+dX+\tfrac12\sigma X^2,\qquad d\in A_s .
\end{gathered}
\tag{4}
\]
Precisely, \(y,z,w\) are the Taylor projections of \(Y,Z,W\).
Quotienting \(B_s=A_s[X]\) by \(X\) identifies \(A_s\) with
\(\mathbb C[Y,Z,W]_{s_0}\), proves \(s_0\ne0\), and shows that
\(y,z,w\) are independent polynomial generators before localization.
Projecting the invariant \(s\) proves its displayed formula.

The forward transformation and Taylor inverse are isomorphisms of
these actual localized rings. Their Jacobian determinants are inverse
units. Pulling back to \(\mathbb C[y,z,w]_{s_0}[X]\), a unit is
independent of \(X\); evaluation at \(X=0\) gives determinant one.
Thus the Jacobian from \((X,y,z,w)\) to \((X,Y,Z,W)\) is exactly one.
This uses both actual inverse orders, not a converse to the
Jacobian condition.[^2]

Re-expanding \(u=(X-b_X)/s\) in (2), including the quotient rule
on fractions, gives \(N'=[X]T|_{A_s}=N/s\).
This is a nonzero LND on \(A_s\), since \(N(s)=0\).
No local nilpotence of the localized \(T\) is asserted.
Choose an intrinsic local slice \(a\) with \(Na=h\in S_0\setminus\{0\}\),
and set \(v=sa/h\). Then
\[
N'v=1,\qquad
A_L=(S_0\setminus\{0\})^{-1}A=L[v]=L[y,z,w],\qquad
N'\tau=N'\xi=N'\sigma=0 .
\tag{5}
\]
Indeed \(A_L=L[a/h]\), and \(s\in L^*\). Also the denominator
\(s_0=s\) in (4) lies in \(L^*\), so it disappears on this
generic fiber. The entire affine line is retained.
Extend the two coefficient derivatives to fix \(v\);
then \(N'=\partial_v\).

## 3. The tangent relation comes from the speed cofactor

Let \(J(X)\) be the Jacobian of \((Y,Z,W)\) with respect to
\((\tau,\xi,v)\), with \(X\) fixed. By Section 2,
\(J(X)=J_0\in L(v)^*\), independent of \(X\).
Coefficient subscripts in this section hold \(v\) fixed.
The matrix and the selected cofactors are
\[
\begin{gathered}
\begin{pmatrix}
y_\tau+X&y_\xi&y_v\\
z_\tau+\rho'X&z_\xi&z_v\\
w_\tau+d_\tau X+\sigma_\tau X^2/2&
w_\xi+d_\xi X+\sigma_\xi X^2/2&w_v+d_vX
\end{pmatrix},\\
T(\xi)=
\frac{y_vz_\tau-y_\tau z_v+X(\rho'y_v-z_v)}{J_0},\qquad
T(v)=
\frac{y_\tau z_\xi-y_\xi z_\tau+X(z_\xi-\rho'y_\xi)}{J_0}.
\end{gathered}
\tag{6}
\]
These are Cramer's formulas for the original partial \(T\) on
the actual fraction field, since \(T(X)=T(Y)=T(Z)=0\) and
\(T(W)=1\).

Now \(\xi=s\) is fixed by \(N'\). Comparing the \(X\) coefficient
of \(T(\xi)\) in (6) with (5) therefore gives
\(z_v=\rho'y_v\). Consequently
\[
z=\rho'y+k,\qquad k\in L,\qquad
\alpha(\zeta)=r\zeta+k_\tau,\quad \beta=k_\xi,\qquad
J_0=\beta\ne0 .
\tag{7}
\]
The first assertion follows by subtracting \(\rho'y\) and using
\(\ker\partial_v=L\). For the last assertion, the \(X\)
coefficient of \(T(v)\), together with \(N'v=1\), gives
\(1=(z_\xi-\rho'y_\xi)/J_0=k_\xi/J_0\).
This supplies the nonzero denominator; it is not a condition
imposed on \(k\).

This is the difference from the nonradial chart136. There the
third-degree Jacobian coefficient used an independent acceleration
parameter. Here the cofactor of the invariant speed \(\xi=s\)
forces tangency even when \(\sigma_\xi=0\).

Subtract \(\rho'\) times the first row of (6) from its second row.
With \(C=\beta y_\tau-\alpha(y)y_\xi\), the exact determinant becomes
\[
\begin{aligned}
J(X)={}&(C+\beta X)(w_v+d_vX)\\
&+y_v\left\{
\alpha(y)(w_\xi+d_\xi X+\sigma_\xi X^2/2)
-\beta(w_\tau+d_\tau X+\sigma_\tau X^2/2)
\right\}.
\end{aligned}
\tag{8}
\]
Its quadratic coefficient is
\(\beta d_v+y_v(\alpha(y)\sigma_\xi-\beta\sigma_\tau)/2\).
If \(y_v=0\), this coefficient gives \(d_v=0\), and then the
linear coefficient gives \(w_v=0\). Together with \(z_v=0\),
these contradict \(J_0\ne0\). Hence \(y_v\ne0\).

## 4. Polynomial graph and reparameterization

The quadratic coefficient of (8) integrates in \(v\) to
\[
\begin{gathered}
d=\mathfrak d(y),\qquad
\mathfrak d(\zeta)=
-\frac{r\sigma_\xi}{4\beta}\zeta^2
+\frac12\left(\sigma_\tau-\frac{k_\tau\sigma_\xi}{\beta}\right)
 \zeta+\ell,\qquad \ell\in L,\\
w=\mathfrak w(y),\qquad
\mathfrak w_\zeta(\zeta)
=\mathfrak d_\tau(\zeta)-\frac{\alpha(\zeta)}{\beta}
 \mathfrak d_\xi(\zeta),\qquad
\deg_\zeta\mathfrak w\le4,\quad \mathfrak w\in L[\zeta].
\end{gathered}
\tag{9}
\]
In the second line, coefficient derivatives hold \(\zeta\) fixed.
For clarity, after substituting the first line into the linear
coefficient of (8), the chain-rule terms containing \(y_\tau,y_\xi\)
cancel. What remains is
\(w_v=(\mathfrak d_\tau(y)-\alpha(y)\mathfrak d_\xi(y)/\beta)y_v\).
Polynomial integration in the formal variable \(\zeta\), followed
by subtraction in \(L[v]\), supplies the constant term in \(L\).
No algebraic antiderivative in a coefficient parameter is assumed.

Equations (5), (7), and (9) give
\(L[v]=L[y,z,w]=L[y]\). Comparing degrees in these polynomial
rings makes \(y\) linear in \(v\), so \(y_v\in L^*\).
Only now does the constant coefficient of (8) become an identity
whose right-hand side is independent of the formal line variable:
\[
\begin{gathered}
\mathcal D=\partial_\tau-\frac{r y+k_\tau}{k_\xi}\partial_\xi,
\qquad d_y=\tfrac12\mathcal D\sigma,\qquad
w_y=\mathcal Dd,\qquad \mathcal Dw=-1/y_v\in L^*,\\
\kappa=k,\qquad
\partial_\kappa=k_\xi^{-1}\partial_\xi,\qquad
\partial_\tau^{\mathrm{new}}
=\partial_\tau^{\mathrm{old}}-\frac{k_\tau}{k_\xi}\partial_\xi,\\
\mathcal D=\partial_\tau^{\mathrm{new}}-r y\partial_\kappa,\qquad
d=-\tfrac14r\sigma_\kappa y^2+\tfrac12\sigma_\tau y+\ell .
\end{gathered}
\tag{10}
\]
All derivatives in the last expression use the new basis
\((\tau,\kappa)\) and hold the formal \(y\) fixed.
Because \(k_\xi\ne0\), this is a separating transcendence basis
of \(L\). The reparameterization uses \(k_\xi\), not a derivative
of \(\sigma\).

## 5. The coefficient and monic-descent consequences

The coefficient-polynomiality calculation136 applies to exactly
the identities in the last line of (10), with arbitrary
\(\sigma\in L\). Its differentiated polynomial argument never
requires \(\sigma_\kappa\ne0\). For completeness, put
\(K=\ker(\partial_\kappa|_L)\).
Differentiation of minimal polynomials shows that \(K\) is the
relative algebraic closure of \(\mathbb C(\tau)\) in \(L\);
it is finite over \(\mathbb C(\tau)\), and is stable under
\(\partial_\tau\).
Integration of \(w_y=\mathcal Dd\) gives
\[
\begin{aligned}
w={}&\frac{r^2\sigma_{\kappa\kappa}}{16}y^4
-\left(\frac{r'\sigma_\kappa}{12}
       +\frac{r\sigma_{\tau\kappa}}4\right)y^3\\
&+\left(\frac{\sigma_{\tau\tau}}4-\frac{r\ell_\kappa}{2}\right)y^2
 +\ell_\tau y+m,\qquad m\in L .
\end{aligned}
\tag{11}
\]
The \(y^5,y^3,y\) coefficients of
\(\mathcal Dw=-1/y_v\) respectively yield
\[
\begin{gathered}
\sigma_{\kappa\kappa\kappa}=0,\qquad
\ell_{\kappa\kappa}
=\frac{r''}{6r^2}\sigma_\kappa
 +\frac{2r'}{3r^2}\sigma_{\tau\kappa}
 +\frac1r\sigma_{\tau\tau\kappa},\qquad
m_\kappa=\ell_{\tau\tau}/r,\\
\sigma\in K[\kappa]_{\le2},\qquad
\ell\in K[\kappa]_{\le3},\qquad
m\in K[\kappa]_{\le4},\\
d\in K[\kappa,y]_{\le3},\qquad w\in K[\kappa,y]_{\le4}.
\end{gathered}
\tag{12}
\]
The last two degrees are total degrees.
These polynomial conclusions follow by subtracting explicit
polynomial primitives in \(\kappa\); the remainders are in its
exact constant field \(K\). They do not assume \(L=K(\kappa)\)
or a polynomial generator for \(K\). The complete coefficient
calculation is reproduced in the stated input.[^3]

Finally \(\tau,\rho,\rho'\in K\), and
\[
y=Y-\tau X,\qquad
\kappa=Z-\rho'Y+(\tau\rho'-\rho)X,\qquad
W=w(\kappa,y)+d(\kappa,y)X+\tfrac12\sigma(\kappa)X^2
=G_K(X,Y,Z),\quad \deg G_K\le4 .
\tag{13}
\]
Thus the original bad coordinate has a monic polynomial relation
over a transcendence-degree-one subfield \(K\subset\operatorname{Frac}A\).

The exact monic-pencil lemma136, Section 3, requires precisely this
field and monicity conclusion and does not assume nonradiality.
It gives an actual invariant
\(I=W+P(X,Y,Z)\), with \(P\in\mathbb C[X,Y,Z]\) of degree at most
four. Its proof uses the classical rationality of a
transcendence-degree-one subfield of a complex rational function
field, then the exact generic kernel \(p-aq\) for a reduced rational
invariant \(a=p/q\). No selected component over a larger field is
substituted for that kernel.[^4]

The fixed-point-free linear-invariant obstruction in Section 5 of
the same note then applies without any acceleration assumption:
\(B=\mathbb C[I,X,Y,Z]\), \(EI=0\), and the other three coordinates
are still good. Over \(\mathbb C(I)\), the classical nice
three-variable theorem supplies a linear speed relation.
Intersecting that line with the irreducible nonlinear cone puts
the projective speed ratios in \(\mathbb C(I)\).
A primitive row over the PID \(\mathbb C[I]\), together with
fixed-point freeness from the slice, then makes all three speeds
belong to \(\mathbb C[I]\). Their transcendence degree is at most
one, contradicting (1).[^4]

Consequently the nonlinear homogeneous rank-two speed case in
the supplied three-good quadratic profile is impossible, including
the formerly separated radial case. Linear homogeneous speed
relations and dense homogeneous speed images are different cases;
no change to their assumptions or arbitrary coordinate entry is
asserted here.

## Sources

1. [Conical three-good speeds lower the selected adjoint degree](conical-three-good-adjoint-degree-pass135.md),
   Sections 2--4. Exact selected degree one, its intrinsic leading
   LND, and the degree-zero boundary.
2. [A tangent-graph reduction for nonradial conical speeds](conical-mismatch-tangent-graph-reduction-pass136.md),
   Section 2. Actual localization and whole generic line.
   Sections 3--4 are generalized here by changing the coefficient
   basis and using the speed cofactor.
3. [Polynomial coefficients over a one-variable field in the conical mismatch branch](conical-mismatch-coefficient-polynomiality-pass136.md),
   Sections 2--5. The conditional coefficient calculation after
   reparameterization, reproduced in (10)--(13).
4. [Nonradial conical speeds are incompatible with a slice](conical-nonradial-quartic-coordinate-pass136-working.md),
   Section 3 for the general exact monic-pencil lemma, and
   Section 5 for the general invariant-bad-coordinate obstruction.
   Those two arguments have no nonradial premise. They explicitly
   identify the classical rational-field theorem and the
   Dasgupta--Gupta statement of Wang's linear-invariant theorem.

[^1]: [Selected-partial135](conical-three-good-adjoint-degree-pass135.md), Sections 2--4.
[^2]: [Actual localized chart136](conical-mismatch-tangent-graph-reduction-pass136.md), Section 2.
[^3]: [Coefficient-polynomiality136](conical-mismatch-coefficient-polynomiality-pass136.md), Sections 2--5.
[^4]: [Monic-pencil and invariant-coordinate obstruction136](conical-nonradial-quartic-coordinate-pass136-working.md), Sections 3 and 5, including the classical sources stated there.
