# A constant odd part in the remaining degree-(2,4,6) quadric line

Working result: the whole polynomial-line return and a nontrivial
cubic relation on the normalized quadric force a precise coefficient
normal form for the intrinsic degree pattern (2,4,6).
After an affine parameter translation and constant rescalings over
the exact field L, its odd part has degree one:
p=v^2-delta and x=p(ap+b)+epsilon v, with a,epsilon nonzero.

The proof first classifies the two possible whole-line forms.
The other form has ruling degrees two and four on a smooth quadric,
so cannot lie on a cubic section of bidegree (3,3).
This is a normal form over L, not an actual polynomial change of
X,Y,Z,W, and it is not recognition or exclusion of the remaining
actual degree pair.

## 1. Precise intrinsic inputs and the actual application

Let L be a characteristic-zero field and suppose
\[
\begin{gathered}
p_{\rm old},x_{\rm old},q_{\rm old}\in L[v_0],\qquad
L[p_{\rm old},x_{\rm old},q_{\rm old}]=L[v_0],\\
x_{\rm old}^2+\beta p_{\rm old}q_{\rm old}=d,\qquad
\beta\in L^*,\ d\in L,\\
(\deg p_{\rm old},\deg x_{\rm old},\deg q_{\rm old})=(2,4,6).
\end{gathered}
\tag{1}
\]
Assume also that a polynomial Phi of total degree at most three
vanishes on the line and is not a multiple of the quadric equation.
In the actual application, this is the transformed genuine fourth
potential, whose evaluated gradient minors with the quadric generate
the unit ideal. That unit ideal implies the required nonmultiple
condition.

These inputs apply to the remaining (deg sigma,deg theta)=(4,6)
case of the complete actual chart in
[365](principal-paraboloid-nonlinear-intercept-unequal-degree-gate-pass365-working.md)
and
[367](principal-paraboloid-nonlinear-intercept-geometric-degree-exclusions-pass367-working.md).
Their invertible affine L change gives exactly (1) and transports
the genuine cubic and unit minors. All their actual assumptions
are retained: a globally sliced C-polynomial four-ring, exact
time profile (1,2,2,2), full initial kernel X^2Z-Y^2, literal
selected Z-partial, exact finite coefficient field, strong complex
intercept field return, and full scalar calibration.

The actual normalization of
[369](principal-paraboloid-nonlinear-intercept-linear-coefficient-normalization-pass369-working.md)
can additionally arrange n=-s^2/(4t^2)+f(t) in that sector.
The abstract proof below does not need that extra coefficient gate.
It will not promote any transformation over L to an original
complex polynomial automorphism.

## 2. Exact normalization of the quadratic generator

Write
p_old=alpha v0^2+alpha1 v0+alpha0 with alpha nonzero, and set
\[
v=v_0+\frac{\alpha_1}{2\alpha},\qquad
\delta=\frac{\alpha_1^2-4\alpha\alpha_0}{4\alpha^2},\qquad
p=p_{\rm old}/\alpha,\quad x=x_{\rm old},\quad
q=\alpha\beta q_{\rm old}.
\tag{2}
\]
Then, with no coefficient-field square root,
\[
p=v^2-\delta,\qquad x^2+pq=d,\qquad
L[p,x,q]=L[v],\qquad (\deg p,\deg x,\deg q)=(2,4,6).
\tag{3}
\]
The transformed Phi still has total degree at most three and is
not divisible by the transformed quadric. If the original Nv0=1,
then Nv=1 as well, since the translating coefficient belongs to L.

The free parity decomposition
L[v]=L[p] direct-sum v L[p] gives unique polynomials
\[
x=E(p)+vF(p),\qquad
E(p)=ap^2+bp+c,\quad a\in L^*,\quad
F(p)=Dp+\varepsilon,\quad b,c,D,\varepsilon\in L.
\tag{4}
\]
The nonvanishing of a follows from deg x=4; the odd part has
degree at most three. If F were zero, both x and
q=(d-x^2)/p would be even polynomials in v, contradicting whole
return. Thus F is nonzero.

Reduction modulo p uses the free basis 1,v of L[v]/(v^2-delta).
It does not require delta to be nonsquare or nonzero. The condition
p divides x^2-d gives exactly
\[
2c\varepsilon=0,\qquad d=c^2+\delta\varepsilon^2.
\tag{5}
\]
Every repeated-root and split-quadratic boundary is retained.

## 3. Whole return gives exactly two forms

First suppose c=0. Write K=ap+b, so E=pK. Formula (5) gives
d=delta epsilon^2. Direct division gives
\[
q=-pK^2-2vKF-F^2-\delta\frac{F^2-\varepsilon^2}{p}.
\tag{6}
\]
The last quotient is polynomial because F=epsilon+Dp.
Since x-pK=vF, equations (4),(6) prove the exact ring equality
\[
L[p,x,q]=L[p,vF]
=L[p]\oplus vF\,L[p].
\tag{7}
\]
Indeed (vF)^2=(p+delta)F^2 lies in L[p], so every polynomial
reduces to this even/odd form. Equality with L[v] forces v to
lie in the odd module, which is equivalent to F being a unit
of L[p]. Thus D=0 and epsilon is nonzero.
This yields the first possible whole-line form:
\[
\begin{aligned}
\mathrm{I}:\quad&
p=v^2-\delta,\qquad x=p(ap+b)+\varepsilon v,\\
&q=-p(ap+b)^2-2\varepsilon v(ap+b)-\varepsilon^2,\qquad
d=\varepsilon^2\delta,\qquad a,\varepsilon\in L^*.
\end{aligned}
\tag{8}
\]
In particular the simultaneous case c=epsilon=0 is impossible.

Now suppose c is nonzero. Equation (5) gives epsilon=0 and
d=c^2. Since F is nonzero, D is nonzero. Put E=c+pK. Then
\[
\begin{aligned}
\mathrm{II}:\quad&
p=v^2-\delta,\qquad x=c+p(ap+b)+Dpv,\qquad d=c^2,\\
&q=q_{\rm ev}-2DEv,\qquad
q_{\rm ev}=-\frac{E^2-c^2}{p}-D^2p(p+\delta),\\
&a,c,D\in L^* .
\end{aligned}
\tag{9}
\]
The displayed even part is polynomial. This second form really
does satisfy whole return before the cubic input is used:
\[
pv=\frac{x-E}{D},\qquad
Ev=-\frac{q-q_{\rm ev}}{2D},\qquad
v=\frac{Ev-K(pv)}c .
\tag{10}
\]
Thus the classification has not discarded it by an unsupported
parity argument. Conversely both (8),(9) satisfy the quadric and
have the three degrees (2,4,6). These exhaust all possibilities
from (3) alone.

## 4. The second form has ruling degrees two and four

Assume form II. Since c is nonzero, the projective quadric
\[
\mathcal S:\quad x^2+pq-c^2z^2=0
\quad\subset\mathbb P^3_L
\tag{11}
\]
is smooth. Let C0 be the projective closure of the polynomial line,
and extend coefficients to an algebraic closure of L if needed.
The whole-ring equality in (3) persists and makes P1_v the
normalization of C0, with function field L(v) before base change.

The two rational functions on S
\[
u_-=\frac{x-cz}{p},\qquad
u_+=\frac{x+cz}{p}
\tag{12}
\]
are affine expressions for its two ruling projections. One can
check this globally using the rank-one matrix
\[
\begin{pmatrix}
p&x+cz\\
x-cz&-q
\end{pmatrix}.
\tag{13}
\]
Its determinant is the negative of the quadric equation.
At a projective point the matrix is nonzero and has rank one;
its row and column lines give the two globally defined maps to P1.
On p nonzero these are precisely the two ratios in (12).
The Segre identification and ruling maps are the standard primary
description in
[Vakil, Foundations, Section5.1](https://virtualmath1.stanford.edu/~vakil/0708-216/216fall0708.pdf).

On the normalization, (9) gives
\[
u_-=ap+b+Dv,\qquad
u_+=\frac{ap^2+bp+Dpv+2c}{p}.
\tag{14}
\]
The first is a polynomial of exact degree two in v because a
is nonzero. In the second, the numerator has exact degree four,
the denominator has degree two, and they are coprime: reduction
of the numerator modulo p is the nonzero constant 2c.
This includes delta=0, when p has a repeated root.
Their exact degrees as maps P1 to P1 are therefore two and four.
For example, a generic fiber is cut out by numerator minus a
transcendental multiple of denominator, of the indicated degree;
coprimality prevents lost base points.

Degree under normalization, equivalently the pullback degree of
O_P1(1), is given by
[Stacks, Lemma33.44.11](https://stacks.math.columbia.edu/tag/0AYZ).
Because C0 is birationally parametrized by v, the two projection
degrees give its bidegree as
\[
[C_0]=(2,4)\quad\text{or}\quad(4,2)
\tag{15}
\]
depending only on the ordering of the two rulings. No smoothness
at infinity is assumed or needed.

## 5. A genuine cubic cannot contain the second form

Homogenize the transformed Phi to its exact total degree j<=3.
It is not identically zero on S. Indeed vanishing on the quadric
would make its affine polynomial a multiple of x^2+pq-c^2,
contrary to the input following (1). In the actual application
this would also annihilate all evaluated two-gradient minors.

Thus its restriction gives an effective divisor of class (j,j)
on S=P1 x P1, containing the integral curve C0. The residual
effective divisor would have class
(j-2,j-4) or (j-4,j-2), with at least one negative entry.
This is impossible: an effective divisor on P1 x P1 has
nonnegative degrees against the two general ruling fibers.
Equivalently its two bidegrees are nonnegative.
The intersection and effective-divisor degree facts are the same
ones used in367, directly recorded in
[Stacks, Section33.45](https://stacks.math.columbia.edu/tag/0BEL).

Therefore form II is excluded by the cubic input, and (8) is the
only remaining exact-field normal form:
\[
\boxed{
p=v^2-\delta,\quad x=p(ap+b)+\varepsilon v,\quad
q=-p(ap+b)^2-2\varepsilon v(ap+b)-\varepsilon^2,\quad
a,\varepsilon\in L^* .
}
\tag{16}
\]
This includes d=0 exactly when delta=0.

## 6. The surviving form is an intrinsic boundary, not recognition

The formal polynomial change over L
\[
p_1=p,\qquad x_1=x-pK,\qquad q_1=q+2Kx-pK^2,
\qquad K=ap+b
\tag{17}
\]
has inverse
\[
p=p_1,\quad x=x_1+p_1K,\quad
q=q_1-2Kx_1-p_1K^2,
\tag{18}
\]
where K=ap1+b in the inverse. Both compositions are identities
and x1^2+p1q1=x^2+pq.
On (16), x1=epsilon v and q1=-epsilon^2.
Consequently the cubic
\[
\Phi_0=q+2Kx-pK^2+\varepsilon^2
\tag{19}
\]
vanishes and has unit evaluated gradient minors with the quadric:
in the new formal coordinates one such minor is q1=-epsilon^2.
Thus the whole-ring, quadric, cubic, and unit-minor properties
really do permit the surviving form, for zero or nonzero d.

The map (17) is only over L. Its coefficients have not been
proved complex or polynomial in the original four-ring, and its
new generators are not asserted to be actual coordinates.
Moreover the auxiliary cubic (19) is not identified with the
genuine fourth potential except for the shared property of vanishing
on this intrinsic line. Further use of its literal coefficients
and the full actual scalar remains necessary.

The normal form uses neither a rationality assumption on L nor
a square root of a coefficient. Fresh primary geometry was checked.
Fresh unsaved algebra verified both forms of the quadric, the
second-form recovery of v, both ruling ratios, the rank-one
determinant, the quadratic-form preservation in (17), and the
surviving cubic identity. The exact ring and divisor arguments
above are not consequences of finite sampling.
No saved checker was executed, imported or compiled, and no
retained source or index was changed. No actual realization,
ambient normalization, unrestricted cancellation, novelty,
human-expert or proof-assistant certification is claimed.
