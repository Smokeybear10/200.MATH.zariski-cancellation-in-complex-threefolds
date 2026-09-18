# Recognition of the height-two shift-one pair by a curve pencil

Status: bounded recognition of the actual height-two exact1122 branch
whose two literal bad-coordinate partials both have exact shift one.
The shift-one chart253 reduces the only unrecognized coefficient case
to a finite curve field. The actual projected field return then makes
a particular generic curve function have degree one. Its pole divisor
forces an actual weight-two relation and a polynomial shear to three
good coordinates.

The pole-degree input and the complete no-cancellation argument are
stated below. The rational curve parameter obtained in that argument
is not lifted to an ambient coordinate. Recognition uses only the
resulting complex-coefficient shear and the retained theorem156.
No arbitrary-entry or unrestricted cancellation claim is made.

## 1. Exact retained chart and the finite curve field

Use the assumptions and notation of the fully read
[shift-one chart253](height-two-shift-one-affine-chart-pass253-working.md):
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\quad Eu=1,\quad A=\ker E,\quad
K=\operatorname{Frac}A,\\
(\deg_E X,\deg_E Y,\deg_E Z,\deg_E W)=(1,1,2,2),\quad
k_{\partial_Z}=k_{\partial_W}=1,\\
a=EX,\quad b=EY,\quad e=E^2Z/2,\quad h=E^2W/2,\quad
t=b/a\notin\mathbb C,\quad q=e/a^2,\quad\rho=h/a^2 .
\end{gathered}
\tag{1}
\]
The full weighted initial kernel has height two. The actual
localization and projection at \(X=0\) give
\[
K=\mathbb C(y,z,w).
\tag{2}
\]
For the selected intrinsic LND, the chart supplies an exact field
\(L\), finite over \(\mathbb C(t,\lambda)\), and a generic parameter
\(y\) with \(K=L(y)\). Its coefficient formulas are
\[
\begin{gathered}
z=n+\frac{q''}{2}y^2+S'y,\qquad
w=\lambda+\frac{\rho''}{2}y^2+H'y,\\
q'''=n_\lambda\rho''',\qquad S''=n_\lambda H'',\qquad
n_t\ne0,\qquad n_\lambda\ne0 .
\end{gathered}
\tag{3}
\]
Here \(q,\rho,S,H\) are algebraic over \(\mathbb C(t)\); primes are
the unique extended \(t\)-derivative. The two extended partials on
\(L\) commute. They are not derivatives on a presumed rational
coefficient field.

If \(n_{\lambda\lambda}\ne0\), chart253 already gives complex
quadratic \(q,\rho\), an actual weight-two shear, and recognition.
It remains to handle
\[
\begin{gathered}
n=m\lambda+n_0,\qquad
F=\mathbb C(t,q,\rho,S,H,m,n_0),\qquad
[F:\mathbb C(t)]<\infty,\quad m\ne0,\\
q'''=m\rho''',\qquad S''=mH'',\qquad m'\lambda+n_0'\ne0 .
\end{gathered}
\tag{4}
\]
These are precisely the remaining conclusions of253, not an
additional rationality assumption. In particular \(F\subset L\subset K\)
and \(F\) is a finitely generated one-variable field over \(\mathbb C\).
Every derivative of an element of \(F\) still belongs to \(F\), by
uniqueness of the derivative on a finite separable extension.

Put
\[
C=\frac{q''-m\rho''}{2},\qquad D=S'-mH' .
\]
Eliminating \(\lambda\) in (3) yields the exact projected formula
\[
\boxed{z=mw+Cy^2+Dy+n_0,\qquad m,C,D,n_0\in F.}
\tag{5}
\]
Equations (2),(5) give both field inclusions
\[
\mathbb C(y,z,w)\subseteq F(y,w)\subseteq K,
\quad\text{hence}\quad
\boxed{K=F(y,w)=\mathbb C(y,w)(z).}
\tag{6}
\]
There is no descent step in these inclusions: every generator is
already in \(K\). Moreover \(y,w\) are algebraically independent
over \(F\). Indeed \(F\) has transcendence degree one, while the
field in (6) has transcendence degree three.

## 2. The exact degree-pole fact used here

We use the following precise curve facts. A finitely generated
one-variable field has a nonsingular projective curve model, and
an inclusion of such function fields corresponds to a nonconstant
morphism of their models. This is
[Stacks, Theorem 53.2.6, tag 0BY1](https://stacks.math.columbia.edu/tag/0BY1).
For a nonconstant function \(f\) on a nonsingular projective curve
over a field \(k\), its pole divisor is the pullback of the degree-one
point \(\infty\) under \(f:C\to\mathbb P^1_k\). The pullback-degree
formula in
[Stacks, Lemma 33.44.11, tag 0AYZ](https://stacks.math.columbia.edu/tag/0AYZ),
together with the field-degree definition
[tag 02NY](https://stacks.math.columbia.edu/tag/02NY), therefore gives
\[
\deg\operatorname{Pole}(f)=[k(C):k(f)] .
\tag{7}
\]
This application has proper nonsingular integral curves and a
nonconstant function; it does not use a degree formula for a
nonproper affine parametrization.

All three cited statements were freshly read. The further argument
below proves the needed pole divisor itself rather than assuming
that a generic pencil has no cancellation.

## 3. A degree-one generic polynomial pencil

Here is the field lemma needed for (5).
Let \(F/\mathbb C\) be a finitely generated field of transcendence
degree one. Let \(Y_0,W_0\) be independent over \(F\), and let
\(f_1,f_2,f_3,f_0\in F\). If
\[
F(Y_0,W_0)=\mathbb C(Y_0,W_0)(f),\qquad
f=f_1W_0+f_2Y_0^2+f_3Y_0+f_0,
\tag{8}
\]
then there is a single point \(P\) on the nonsingular projective
complex curve of \(F\) such that each coefficient has pole divisor
bounded by \(P\). In particular \(F=\mathbb C(\alpha)\) for a
parameter \(\alpha\), and every \(f_i\) is affine in \(\alpha\)
with complex coefficients. Any nonconstant one of the \(f_i\)
can itself be used as \(\alpha\).

To prove this, let \(\mathcal C\) be the nonsingular projective
curve of \(F\). All its closed points are \(\mathbb C\)-rational.
Define an effective divisor by taking the maximum pole order of
the four coefficients at each point:
\[
\mathcal D=\sum_{P\in\mathcal C}
d_P P,\qquad
d_P=\max\{0,-\operatorname{ord}_P f_0,
                 -\operatorname{ord}_P f_1,
                 -\operatorname{ord}_P f_2,
                 -\operatorname{ord}_P f_3\}.
\tag{9}
\]
Only finitely many terms are nonzero.
Base change from \(\mathbb C\) to
\(k_0=\mathbb C(Y_0,W_0)\). This is a purely transcendental field
extension. The curve remains integral and nonsingular, with function
field \(F(Y_0,W_0)\); each original point \(P\) gives a
\(k_0\)-rational point with the same local parameter.
No algebraic closure of \(F\) or of \(k_0\) is taken.

At a point with \(d_P>0\), choose a local parameter \(\pi\).
The coefficient of \(\pi^{-d_P}\) in \(f\) is
\[
c_1W_0+c_2Y_0^2+c_3Y_0+c_0,\qquad c_i\in\mathbb C,
\tag{10}
\]
where at least one \(c_i\) is nonzero by definition of \(d_P\).
The four monomials are complex-linearly independent, so (10)
is nonzero in \(k_0\). Hence the pole order of \(f\) there is
exactly \(d_P\). Away from the coefficient poles all coefficients
are regular, so \(f\) has no other pole. Thus
\(\operatorname{Pole}(f)=\mathcal D_{k_0}\).

The function in (8) is nonconstant over \(k_0\), since its generated
field has transcendence degree one over \(k_0\). Applying (7) gives
\[
\deg\mathcal D
=\deg\mathcal D_{k_0}
=[F(Y_0,W_0):k_0(f)]=1 .
\tag{11}
\]
Because the points in (9) are complex-rational and the
multiplicities are nonnegative integers, \(\mathcal D\) is one
point with multiplicity one.

At least one coefficient is nonconstant. Any such coefficient
\(\alpha\) has exactly one simple pole. A second application of
(7), now over \(\mathbb C\), gives \(F=\mathbb C(\alpha)\).
Every \(f_i\) has no pole except possibly the simple pole of
\(\alpha\). In the rational field \(\mathbb C(\alpha)\), write it
as a reduced quotient of complex polynomials in \(\alpha\).
The absence of finite poles makes the denominator constant;
the bound at infinity makes the numerator degree at most one.
This proves the lemma without a Riemann--Roch dimension argument.

The purely transcendental base extension is essential to the
argument's use of (10). Substituting numerical values for the
two parameters could cancel a polar coefficient and would not
prove the lemma.

## 4. Applying the pencil lemma to the remaining chart

Apply Section 3 to (5),(6), with coefficients \(m,C,D,n_0\).
All of them are affine in a single curve parameter.
The differential identity needed for the endpoint follows directly
from (4):
\[
C'=\frac{q'''-m'\rho''-m\rho'''}2
   =-\frac{m'\rho''}{2}.
\tag{12}
\]
There are two cases.

If \(m\notin\mathbb C\), the lemma permits \(m\) itself as
parameter and gives \(C=c_1m+c_0\), \(c_0,c_1\in\mathbb C\).
The derivative \(m'\ne0\): the constants of the extended
derivative on the finite field \(F/\mathbb C(t)\) are exactly
\(\mathbb C\), by the differential criterion in253.
Therefore (12) implies
\[
\rho''=-2c_1\in\mathbb C,\qquad
\rho'''=0,\qquad q'''=m\rho'''=0 .
\tag{13}
\]
Successive integration with that same constant-field check makes
\(q\) a complex polynomial in \(t\) of degree at most two.
No parameter \(m\) is being made an ambient coordinate.

If instead \(m=m_0\in\mathbb C\), equation (4) gives
\[
(q-m_0\rho)'''=0 .
\tag{14}
\]
Again the exact constant-field argument makes \(q-m_0\rho\)
a complex polynomial of degree at most two.
This case does not require choosing a rational parameter of \(F\).

Thus both cases give a complex constant \(c\) and complex constants
\(r_0,r_1,r_2\) such that
\[
q-c\rho=r_2t^2+r_1t+r_0.
\tag{15}
\]
Use \(c=0\) in the first case, and \(c=m_0\) in the second.

## 5. The resulting transformation is actual and polynomial

Multiplying (15) by \(a^2\) gives
\(e-ch=r_2b^2+r_1ab+r_0a^2\) in the original invariant ring.
Define an actual coordinate and its inverse by
\[
\begin{aligned}
Z_1&=Z-cW-(r_2Y^2+r_1XY+r_0X^2),\\
Z&=Z_1+cW+(r_2Y^2+r_1XY+r_0X^2),
\end{aligned}
\qquad X_1=X,\quad Y_1=Y,\quad W_1=W .
\tag{16}
\]
The two compositions are the identity polynomial maps.
The ordinary \(u^2\) coefficient of \(Z_1\) is zero by (15).
Since all terms on the first line have \(E\)-degree at most two,
\[
E^2X_1=E^2Y_1=E^2Z_1=0 .
\tag{17}
\]
This gives the actual three-good frame required by the fully read
[recognition theorem156](three-good-all-degree-recognition-pass156-working.md).
With its explicitly retained working dependencies,
\[
\boxed{A\simeq\mathbb C^{[3]}}
\tag{18}
\]
for the case (4). The complementary
\(n_{\lambda\lambda}\ne0\) case was already recognized in253.
Hence the entire supplied height-two shift pair \((1,1)\)
is recognized under those dependencies.

No clearing of denominators from a generic coordinate change is used:
all coefficients in (16) have been proved complex constants before
the ambient map is written.

## 6. Scope and provenance

The complete253 chart was read before using it. Its exact
localization, full field return, intrinsic affine parameter and
calibrated determinant are inputs, not consequences of the pencil
alone. The complete156 recognition synthesis was also read.
The three Stacks statements in Section 2 were freshly read in their
stated forms. The local pole computation, finite-field inclusions,
two differential cases and both polynomial inverse directions
are established above.

This note closes only the selected shift pair \((1,1)\) within the
supplied exact1122 height-two entry. It is separate from the
shift-two chart and its further endpoints. It makes no claim that
every globally sliced action admits this profile, and no historical
novelty or unrestricted cancellation assertion.
No earlier source or frozen packet was edited. No saved checker
was executed, imported or compiled.
