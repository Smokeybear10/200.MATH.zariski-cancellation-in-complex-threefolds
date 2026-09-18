# A graph parameter forces a conic in the nonlinear velocity-cone branch

An arbitrary polynomial curve of transverse velocities can be put
into the explicit graph-parameter construction below. The resulting
action has actual polynomial inverse coordinates, and the selected
original partial is good. However, if the original frame is nice
and its Jacobian square is nonzero, its nonlinear ternary velocity
cone cannot have degree greater than two.

This is an all-degree obstruction for a specified actual inverse
family, not a conic theorem for every nice sliced action with a
good direction. In particular, no unit derivative of a source
binary parameter is assumed to exist in the general case.

## 1. The actual family and its slice criterion

Let R be any polynomial in three independent variables x1,x2,x3,
and let h1,h2,h3 belong to C[t], not all zero. In the original
polynomial ring B=C[x1,x2,x3,w], put
\[
a=w+R(x_1,x_2,x_3),\qquad
E x_i=h_i(a),\qquad
Ew=-\sum_{i=1}^3h_i(a)R_i,
\qquad T=\partial_w.
\tag{1}
\]
Here Ri denotes the ordinary partial derivative of R. The maps
(x,w) to (x,a) and (x,a) to (x,w=a-R(x)) are two-sided
polynomial inverses. They give
\[
B=C[a,x_1,x_2,x_3],\qquad
E=\sum_{i=1}^3h_i(a)\partial_{x_i},\qquad
T=\partial_a
\tag{2}
\]
in these actual coordinates. Hence E is a global LND. It has
a polynomial slice exactly when gcd(h1,h2,h3)=1 in C[a].
Necessity follows by evaluating an equation Es=1 at x=0;
sufficiency is a polynomial Bezout combination of the xi.

More explicitly, the Euclidean algorithm completes the unimodular
speed column to a matrix M(a) in GL3(C[a]) taking it to (1,0,0).
Thus (a,S,Y,Z), with (S,Y,Z)^t=M(a)x, are actual translation
coordinates, with inverse x=M(a)^{-1}(S,Y,Z)^t followed by
w=a-R(x). The determinant of M is a nonzero constant, so
its inverse has polynomial entries. The elementary two-entry
matrix used in this completion is displayed in
[pass76, Section2.1](triangular-nice-primitive-freeness-pass76.md).
This is an inverse construction, not an inference from the
Jacobian of (1).

The original selected partial is always good in this family:
\[
Q=[T,E]=\sum_{i=1}^3h_i'(a)\partial_{x_i}
\quad\text{in (2)},\qquad [E,Q]=0.
\tag{3}
\]
This assertion concerns the original T=partial_w under the
displayed exact coordinate identification. It does not require
that E already be nice in the original frame. Q is also a
polynomial LND in (2).

## 2. Niceness is a full quadratic-relation identity

The first three original coordinate images are E-invariant,
because Ea=0. Applying E a second time to the fourth gives
\[
E^2w=-\sum_{i,j=1}^3h_i(a)h_j(a)R_{ij}(x).
\tag{4}
\]
Since a and the three xi are independent coordinates, E is
nice in the original frame if and only if
\[
h(t)^t\operatorname{Hess}R(x)h(t)=0
\quad\text{in }C[x_1,x_2,x_3,t].
\tag{5}
\]
No degree bound on R or the hi is imposed. Write the polynomial
matrix Hess R as a finite sum of monomials in x with constant
symmetric coefficient matrices. If this Hessian is nonzero,
at least one such coefficient matrix C is nonzero. Comparing
that monomial in (5) gives
\[
q(h_1(t),h_2(t),h_3(t))=0,
\qquad q(Y)=Y^tCY\ne0.
\tag{6}
\]
The nonvanishing uses characteristic zero and symmetry of C:
a nonzero symmetric matrix defines a nonzero quadratic form.
Thus non-affine R requires a genuine homogeneous quadratic
relation on the entire transverse velocity curve.

If Hess R=0, R is affine-linear. In that case all four
original velocity entries are polynomials in a alone, while
da is a constant row. Let P be the original velocity column.
Then J=Jac P=P'(a)da. The identity da P=Ea=0 and constancy
of da imply da P'=0, whence J^2=0. Consequently
\[
J^2\ne0\quad\Longrightarrow\quad
\text{a nonzero homogeneous quadratic relation (6) exists.}
\tag{7}
\]
This rules out a higher-degree transverse curve before any
attempt to infer a coordinate from a rational parametrization.

## 3. Consequence for the ternary cone

Assume now that the hi have gcd one, the original frame is nice,
and J^2 is nonzero. Suppose its distinguished velocity-cone
polynomial F is nonlinear. The original T is good by (3), so
[the apex theorem](nice-leading-apex-pass76.md) makes F independent
of the fourth velocity coordinate. The projection of the full
velocity cone onto its first three coordinates is exactly the
cone over the curve h(t). It is an irreducible hypersurface
with prime ideal (F) in C[Y1,Y2,Y3].

For this identification, the original polynomial map a=w+R(x)
is surjective onto C. Its transverse velocity values are thus
all h(t), and their scalar multiples are dense in that projected
cone. Also the full velocity cone is V(F) times the fourth
coordinate line, by the good-direction identification. There
is no assumption that h(t) alone dominates a surface.

Relation (6) vanishes on this cone, so F divides q. Since q
has degree two and F is nonlinear and irreducible, deg F=2.
We have proved the conditional conclusion
\[
\boxed{\text{In the family (1), the nonlinear ternary
velocity cone in the nice sliced }J^2\ne0\text{ branch is a conic.}}
\tag{8}
\]
Equivalently, if the projective curve parametrized by the hi
has degree greater than two, (5) forces Hess R=0 and hence
J^2=0. If that projective image is not a curve, the nonlinear
ternary-cone premise in (8) is not being asserted.

## 4. Exact positive and negative boundary controls

The retained conic action is obtained by taking
R=x1 x3-x2^2 and h=(1,t,t^2). Its nonzero Hessian supplies
the relation Y1 Y3-Y2^2=0, and its original Jacobian square
is nonzero. Its actual inverse and sole constant good
direction were already checked in the pass74--76 notes.
Thus the quadratic possibility in (8) is attained.

Higher-degree transverse curves alone are easy to obtain and
do not refute (8). For any integer m>=3, take R=0 and
h=(1,t,t^m). The action is
E=partial_x1+w partial_x2+w^m partial_x3, with Ew=0.
It is nice, has actual slice x1, and has inverse translation
coordinates (x1,w,x2-wx1,x3-w^m x1). Its transverse projective
curve has irreducible equation Y1^(m-1)Y3-Y2^m=0 of degree m.
But J^2=0 and every constant direction is good. Its full
velocity cone has dimension two, not the three-dimensional
hypersurface required by the remaining branch. This boundary
cannot be promoted to the requested higher-degree example.

## 5. What remains outside the obstruction

The family is intrinsically recognized from the explicit
coordinates in Section1. If Q is independent of E, its
restriction to the polynomial kernel is a translation row
over C[a]; dividing its gcd gives a primitive polynomial
slice by the same PID argument as pass76. The current
additional deduction is the degree restriction (8), not
another recognition claim for this already explicit family.

The general binary-form source supplies invariant coprime
parameters, not necessarily a polynomial parameter a with
T a=1 or even one parameter that generates their algebra.
No such additional premise is proved here. Different polynomial
inverse constructions, nonunit T-derivatives and genuinely
two-parameter transverse velocities remain outside this note.
Existence of an actual higher-degree ternary cone, or a
general theorem forcing a conic, remains unresolved.

The proof is an exact all-degree coefficient argument with
explicit original actions and inverse coordinates. No new
numerical suite, full regression, external classification,
historical novelty, human expert review or formal proof
certificate is claimed. Frozen passes through76 and shared
metadata are unchanged.
