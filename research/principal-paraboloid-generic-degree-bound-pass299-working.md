# A uniform generic-line degree bound in the coupled principal chart

Working result: under the complete actual hypotheses of264 and nonzero
coupling, each of the three generic-line polynomials y, sigma and theta
has degree at most twelve. This follows from296's cubic and quartic
levels and its independent-gradient conclusion. The argument keeps the
exact coefficient field and all three generators.

The bound is proved below by polynomial gcds and a dimension count.
It does not presume that the two level equations generate the full
curve ideal, that their intersection is irreducible, or that the plane
projection is smooth. It is not a recognition theorem.

## 1. The precise inputs

Retain the entire actual setup of the completely read
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
[290](principal-paraboloid-nonzero-coupling-projection-pass290-working.md),
and the new
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md).
In particular the original globally sliced polynomial four-ring has
exact time degrees1222 and full initial kernel X^2 Z-Y^2; the literal
Z-partial has exact intrinsic shift four. Its exact coefficient field
L is finite over C(t,s), and
\[
O=L[v]=L[y,\sigma,\theta],\qquad Nv=1,\qquad k_s\ne0.
\tag{1}
\]
The cubic and quartic levels are polynomials in independent variables
U,P,V over L:
\[
H_0=H-h_0,\quad Q_0=Q-q_0,\quad
\deg H_0\le3,\quad \deg Q_0\le4,
\qquad H_0(y,\sigma,\theta)=Q_0(y,\sigma,\theta)=0.
\tag{2}
\]
The first level is monic quadratic in U. By296, the evaluated
two-by-two minors of the two formal gradients generate the unit ideal
of O. In particular both polynomials in (2) are nonzero and their
evaluated gradients are independent at every point of the line.

For the proof of the bound, only (1),(2) and that minor ideal are used.
The original-ring and selected-derivation assumptions are retained
because they are needed to establish these inputs for this problem.

## 2. Removing common factors without removing the actual curve

Let D be a gcd of H_0 and Q_0 in the UFD L[U,P,V], and write
\[
H_0=Df,\qquad Q_0=Dg,\qquad \gcd(f,g)=1.
\tag{3}
\]
Suppose first that D evaluates to zero on the actual curve.
The product rule would make the two evaluated gradients scalar
multiples of the evaluated gradient of D. All their minors would
then be zero, contrary to the unit ideal. Therefore D has nonzero
evaluation in the domain O. Equations (2),(3) imply
\[
f(y,\sigma,\theta)=g(y,\sigma,\theta)=0.
\tag{4}
\]
The evaluated product rules now read grad(H_0)=D grad(f) and
grad(Q_0)=D grad(g). Every original minor is D^2 times the corresponding
reduced minor. Since the original minors generate O, evaluation of D
is a unit:
\[
D(y,\sigma,\theta)\in L^*.
\tag{5}
\]
Thus the removed factor is disjoint from the actual affine curve,
including after extending L. No assumption that D itself is constant
is made.

Neither f nor g is a nonzero constant, because of (4). Write
\[
a=\deg f\ge1,\qquad b=\deg g\ge1.
\tag{6}
\]
These letters refer only to total polynomial degrees in this note,
not the slice speed EX. We have a<=3, b<=4.

## 3. An elementary dimension bound for two coprime equations

Homogenize f,g to their own exact degrees in the ring
\(S=L[T,U,P,V]\), giving f^h,g^h of degrees a,b.
They are coprime. Indeed neither is divisible by T; any other
homogeneous common factor would dehomogenize at T=1 to a
nonconstant common divisor of f,g. A homogeneous polynomial with
constant dehomogenization is a scalar power of T, already excluded.

Multiplication by f^h is injective in S. Multiplication by g^h is
injective in S/(f^h): in the UFD S, f^h dividing g^h times a
polynomial and gcd(f^h,g^h)=1 force f^h to divide that polynomial.
The two exact multiplication sequences therefore give
\[
\begin{aligned}
\dim_L(S/(f^h,g^h))_n
={}&\binom{n+3}{3}-\binom{n-a+3}{3}
       -\binom{n-b+3}{3}+\binom{n-a-b+3}{3}\\
={}&ab\,n+\frac{ab(4-a-b)}2\qquad(n\ge a+b).
\end{aligned}
\tag{7}
\]
The first equality follows by counting degree-n monomials in four
variables and subtracting the two shifted exact sequences. The
second is an identity of polynomials in n,a,b. No global
complete-intersection claim about the actual curve is used.

Let V_n be the subspace of L[v] obtained by evaluating polynomials
of total degree at most n in U,P,V at y,sigma,theta. Dehomogenization
at T=1 followed by evaluation maps S_n onto V_n. Both f^h and g^h
evaluate to zero by (4), so this is also a surjection
\[
(S/(f^h,g^h))_n\longrightarrow V_n.
\tag{8}
\]
Consequently (7) is an upper bound on dim_L V_n. Extra components
of the intersection, whether affine or at infinity, do not invalidate
this inequality.

## 4. Whole-line return supplies the matching growth rate

Put
\[
d=\max\{\deg_v y,\deg_v\sigma,\deg_v\theta\}\ge1,
\tag{9}
\]
ignoring zero polynomials when taking the maximum. Choose one of
the three generators p(v) with degree d. Since they generate L[v],
each of 1,v,...,v^(d-1) has a polynomial expression in the three
generators. Let C be a common upper bound on the total degrees
of these finitely many expressions. This is an existence argument;
no effective or uniform bound on C is needed.

For every n>=C the d(n-C+1) polynomials
\[
p(v)^jv^i,\qquad 0\le i<d,\quad 0\le j\le n-C,
\tag{10}
\]
belong to V_n. Their v-degrees are dj+i, all distinct, so they
are linearly independent over L. Conversely every element of V_n
has v-degree at most dn. Thus
\[
d(n-C+1)\le\dim_L V_n\le dn+1.
\tag{11}
\]
Combining the lower bound with (7),(8), dividing by n, and taking
arbitrarily large integers n gives
\[
\boxed{d\le ab\le12.}
\tag{12}
\]
This proves the claimed uniform bound over the exact field L.
In particular it does not require L to be a rational function field,
an algebraically closed field, or a field of numerically sampled
coefficients. The argument remains valid under an affine change
of the line variable over L, since such changes preserve degrees.

## 5. A precise plane-degree consequence

Let C_0=L[sigma,theta], let Gamma be its projective plane closure,
and write
\[
e=[L(v):\operatorname{Frac}C_0]\in\{1,2\},\qquad
d_0=\max\{\deg_v\sigma,\deg_v\theta\}\ge1.
\tag{13}
\]
Finiteness, the alternatives for e, and d_0>=1 were proved in290.
Homogenizing (1,sigma(v),theta(v)) to degree d_0 defines a morphism
P^1_L to Gamma. At finite points the first coordinate is nonzero;
at infinity at least one leading coefficient of sigma or theta
is nonzero. Hence there is no base point. The map is nonconstant,
has function-field degree e, and pulls O_Gamma(1) back to
O_P^1(d_0).

The degree formula for proper curves, directly checked in
[Stacks, Lemma33.44.11](https://stacks.math.columbia.edu/tag/0AYZ),
therefore yields
\[
d_0=e\deg\Gamma,\qquad
\boxed{\deg\Gamma\le\lfloor12/e\rfloor.}
\tag{14}
\]
This allows plane degree at most twelve in the birational case,
and at most six in the quadratic case. Separate coefficient
arguments can improve the second bound. Equation (14) asserts
neither projected-plane smoothness in the birational case nor
an ambient polynomial change of coordinates.

## 6. Boundary and scope

For the abstract two-equation lemma, the constant twelve cannot
be improved without using additional structure. The embedding
\[
v\longmapsto(v,v^3,v^{12})
\]
has equations P-U^3=0 and V-P^4=0, whose degrees are three and
four and whose gradient minor in the P,V columns is 1.
This is only a control for the abstract lemma: it does not have
the prescribed monic-U form, projection degree, full actual
Jacobian identities or original sliced-ring entry of264. It is
not an actual example showing sharpness within the cancellation
problem.

Conversely the common-factor obstruction cannot simply be
ignored. The two equations V=0 and V^2=0 contain the embeddings
(v,v^r,0) for arbitrarily large r, and their evaluated gradient
minors vanish. This explains why a pair of low-degree equations
alone does not prove (12).

The result bounds the degrees in the generic polynomial variable v
for every actual nonzero-coupling frame in this one supplied chart.
It does not bound the degrees or field extensions of coefficient
functions in t,s, turn the remaining problem into a finite list
of numerical models, recognize every degree<=12 possibility,
or prove arbitrary-coordinate entry. Other full initial kernels
and time-degree profiles are not covered.

The full cancellation conjecture remains unsolved. The argument
uses the newly reviewed296 as a working input and has no human
expert, proof-assistant or novelty certification. Finite checks
and a separate source review are recorded only after completion.
