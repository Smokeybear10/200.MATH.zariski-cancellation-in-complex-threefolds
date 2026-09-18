# A log-form obstruction to polynomial parametrization of the nontriple cubic surface

Let D be a complex cubic polynomial with nonzero leading coefficient,
not the cube of an affine-linear polynomial times a constant. There
are no polynomials g,P,Y on the affine plane, with Y nonzero, satisfying
g squared minus D(P/Y) times Y squared equal to one and having a
nonzero moving-frame determinant det[b,b_s,b_t], where b=(g,P,Y).

This is a polynomial-speed obstruction. It does not require the
actual invariant ring, the divisor bounds122/123, a scalar potential,
or an original-coordinate inverse. In the supplied actual cubic
framework it excludes the squarefree and double-root non-null scalar
cases. It does not cover the triple-root cubic. The separate actual
triple-root argument and arbitrary-frame entry are not proved here.

The proof resolves the relevant cubic surface explicitly and pulls
back a nonzero logarithmic two-form. It does not invoke a general
monotonicity or subadditivity theorem for logarithmic Kodaira dimension.

## 1. The projective cubic and dominance

Write D(T)=a3 T^3+a2 T^2+a1 T+a0, with a3 nonzero, and let
F3(P,Y) be its degree-three homogenization. Use projective coordinates
[P:Y:G:W], reserving lowercase g for its polynomial pullback. Set

\[
\begin{gathered}
\overline X=V\bigl(YG^2-F_3(P,Y)-YW^2\bigr)\subset\mathbb P^3,
\qquad C=\overline X\cap V(W),\\
X=\overline X\setminus C
 =V\bigl(Y(G^2-1)-F_3(P,Y)\bigr)\subset\mathbb A^3,\\
\varphi:\mathbb A^2\longrightarrow X,\qquad
(s,t)\longmapsto(P(s,t),Y(s,t),g(s,t)).
\end{gathered}
\tag{1}
\]

The projective equation is irreducible. For example, after the
invertible constant change U=G-W,V=G+W, it becomes YUV-F3(P,Y).
Regard this as a polynomial in V over C[P,Y,U]. Its two coefficients
YU and -F3 are coprime: F3 is independent of U and is not divisible
by Y because its P cubed coefficient is a3. The primitive linear
polynomial is irreducible by Gauss's lemma. Thus the projective and
affine surfaces are integral.

If det[b,b_s,b_t] is nonzero, b_s and b_t are independent over
C(s,t). The map in (1) therefore has generic differential rank two.
Its image is dense in the integral surface X, and the induced
function-field extension is finite and separable. Separability uses
characteristic zero. In particular a nonzero rational two-form on
X pulls back to a nonzero rational two-form on the affine plane.

## 2. All singular points are explicit

The four derivatives of the projective equation are

\[
\begin{gathered}
F_G=2YG,\qquad F_W=-2YW,\\
F_P=-(3a_3P^2+2a_2PY+a_1Y^2),\\
F_Y=G^2-W^2-a_2P^2-2a_1PY-3a_0Y^2.
\end{gathered}
\tag{2}
\]

On Y=0 the equation gives P=0. The last derivative then gives
G=plus or minus W, so the only singular points there are
[0:0:1:1] and [0:0:-1:1], both in the affine open X.
If Y is nonzero, normalize Y=1. The first two derivatives give
G=W=0; the remaining conditions are D(P)=D'(P)=0.
Thus squarefree D gives no further singularity. A cubic with a
double but not triple root alpha gives exactly one more point,
[alpha:1:0:0], on C. There are no other singular points.

In particular the surface is normal: an integral hypersurface is
Cohen--Macaulay, and the isolated singularities give regularity in
codimension one. The hypersurface canonical sheaf is invertible.

## 3. One blowup resolves each affine singularity

Work near either affine singular point, where W=1 and G=plus or
minus one. Define the local function
u=G^2-1-a2 P^2-a1 PY-a0 Y^2. Its derivative with respect to G
is 2G, a unit there. Therefore (P,Y,u) are etale local coordinates
in the ambient smooth threefold, and the equation is exactly
Yu=a3 P^3. The blowup of the point has the following strict-transform
charts, writing p for P and y for Y:

\[
\begin{array}{c|c|c}
\text{chart}&\text{substitution}&\text{strict-transform equation}\\ \hline
p&y=p y_1,\ u=p u_1&y_1u_1=a_3p\\
y&p=y p_1,\ u=y u_1&u_1=a_3y p_1^3\\
u&p=u p_1,\ y=u y_1&y_1=a_3u p_1^3.
\end{array}
\tag{3}
\]

All three charts are smooth. In the first chart the exceptional
set is y1 u1=0, and the two components meet transversely. The
other charts complete them to the usual two exceptional rational
curves. The computations apply to the original surface because
blowing up and these smoothness checks commute with the displayed
etale change of coordinates.

This resolution is crepant, with no classification theorem needed.
A local generator of the hypersurface canonical sheaf is
dp wedge dy divided by y. In the p-chart it becomes
du1 wedge dy1 divided by a3; in the y-chart it becomes
dp1 wedge dy. Using the equivalent expression du wedge dp divided
by u gives du wedge dp1 in the u-chart. Each is regular and
nowhere zero. The etale coordinate change only contributes a unit.
Thus pulling back a local canonical generator introduces neither
a zero nor a pole along either exceptional component.

The boundary W=0 is disjoint from both centers, so these exceptional
curves are not boundary components.

## 4. The double-root boundary point and its resolution

When D has a double root alpha and a distinct simple root, set
x=P/Y-alpha, G0=G/Y and w=W/Y near the additional singular point.
Then D(alpha+x)=c0 x^2+a3 x^3 with c0 nonzero, and the local
surface is G0 squared minus w squared minus c0 x squared minus
a3 x cubed equal to zero. Its point blowup has charts

\[
\begin{array}{c|c}
\text{chart}&\text{strict-transform equation}\\ \hline
x&G_1^2-w_1^2-c_0-a_3x=0,
\quad G_0=xG_1,\ w=xw_1\\
G_0&1-w_1^2-c_0x_1^2-a_3G_0x_1^3=0,
\quad x=G_0x_1,\ w=G_0w_1\\
w&G_1^2-1-c_0x_1^2-a_3wx_1^3=0,
\quad x=wx_1,\ G_0=wG_1.
\end{array}
\tag{4}
\]

The first chart is smooth. On the exceptional locus in the second
and third charts, the derivatives in x1 and the other ratio cannot
both vanish, because c0 is nonzero and the displayed equations
would then contradict their constant terms. Away from the exceptional
locus the original surface was smooth. The exceptional curve is the
smooth conic G0 squared minus w squared minus c0 x squared in the
exceptional projective plane.

The blowup is again crepant. In each ambient threefold chart, the
pullback of a volume form has a square of the exceptional coordinate
as its Jacobian factor, and the surface equation has exactly that
same square as its total-transform factor. Taking hypersurface
residues cancels the two factors. The strict surface is smooth by
(4), so its resulting canonical generator has no exceptional zero
or pole. This is also the multiplicity-two hypersurface adjunction
calculation: the ambient discrepancy is two and the equation has
multiplicity two.

Crucially, the reduced inverse image of the boundary is its strict
transform plus this exceptional conic. In the x-chart the old boundary
function is w=xw1. The two components are therefore x=0 and w1=0,
each with multiplicity one. Their intersections have
G1=plus or minus sqrt(c0), so they are two distinct points. At each
point G1 is a unit, and x,w1 are regular parameters on the resolved
surface. Thus the components intersect transversely. The boundary
was smooth elsewhere: its only singularity is the double-root node,
as is seen from G squared Y=F3(P,Y). Its strict transform is smooth.

## 5. A global logarithmic two-form survives

Let pi:V to Xbar be the projective surface obtained by the point
blowups above. It is smooth. If D is squarefree, the boundary is
already a smooth plane cubic and its inverse image is unchanged.
If D has a double root, Section4 gives a simple normal crossing
reduced boundary Delta consisting of the strict transform and one
exceptional curve. In either case Delta is the entire reduced
inverse image of C.

Hypersurface adjunction on a cubic in projective three-space gives
omega_Xbar=O_Xbar(-1); C is a hyperplane Cartier divisor. The
canonical calculation in Sections3--4 is crepant, and the boundary
total transform has precisely the reduced multiplicities just checked.
Consequently

\[
K_V=\pi^*K_{\overline X},\qquad
\Delta=\pi^*C,\qquad
K_V+\Delta\sim0,\qquad
0\ne\omega\in H^0\bigl(V,\Omega_V^2(\Delta)\bigr).
\tag{5}
\]

The equalities of divisors use compatible canonical choices; the
line-bundle statement is independent of those choices. For the
double-root case it is essential to include the exceptional boundary
curve in Delta. Omitting it would give the wrong log-canonical class.
The Cartier adjunction calculation is the standard local two-term
resolution recorded in Stacks0B4B.[^adjunction]

Because Delta has simple normal crossings, omega is logarithmic:
locally it is a regular coefficient times dz1 wedge dz2, or
(dz1/z1) wedge dz2, or (dz1/z1) wedge (dz2/z2), according to
whether the point is off the boundary, on one component, or at a
crossing.

## 6. Pullback to the affine plane gives a contradiction

A dominant map in (1) induces a dominant rational map
f:P2 to V, because pi is birational. The properness of V extends
f to a neighborhood of the generic point of every irreducible
divisor of P2: its local ring is a discrete valuation ring.
This is exactly the situation of Stacks0BX7.[^extension]
No assertion that f is globally a morphism on P2 is necessary.

For a divisor whose generic point is in A2, the composition pi f
agrees with the original morphism phi there. Separatedness makes
the two maps agree on the local valuation ring. Since phi lands in
X=Xbar minus C, the lifted center is outside Delta. Therefore
f pullback omega is regular at every affine divisor.

At the line at infinity, let t be a local uniformizer. A boundary
parameter that pulls back to a nonzero function has the form
t to the power m times a unit u, with m nonnegative. Hence
dlog(t^m u)=m dt/t+du/u. In the wedge of two such expressions,
the term with two copies of dt vanishes. With one logarithmic
factor the same simple-pole bound is immediate. Thus even if the
generic point at infinity maps to a boundary crossing, the pullback
two-form has pole order at most one at that line.

The pullback is nonzero by separability and dominance. The preceding
codimension-one statements imply that it is a global section of
the indicated line bundle on the smooth projective plane:

\[
0\ne f^*\omega\in
H^0\bigl(\mathbb P^2,\Omega_{\mathbb P^2}^2(L_\infty)\bigr)
=H^0\bigl(\mathbb P^2,\mathcal O_{\mathbb P^2}(-2)\bigr)=0.
\tag{6}
\]

For clarity, no hidden codimension-two extension theorem is needed
here: on each affine polynomial chart of P2, a rational coefficient
with nonnegative order at every irreducible divisor is a polynomial.
The same observation after trivializing the line bundle gives the
extension asserted in (6). The contradiction proves the theorem.

## 7. Scope and sources

The surface and pullback proof uses only the polynomial norm relation,
the degree-three nontriple scalar and the nonzero differential rank.
In particular it does not use Y squared dividing P cubed, factorial
closure of an embedded invariant plane, or a global scalar potential.
For a triple root, the boundary is cuspidal and Section4 is no longer
the node calculation above. No conclusion for that case is extracted
from this log-form argument.

The six numbered displays and explicit blowup charts are written
arguments, not certified by a finite checker. No test execution is
claimed. An initial search for log-Kodaira monotonicity was not used
as a proof input; the elementary logarithmic top-form calculation
replaces it. This note adds no general cancellation or arbitrary-frame
entry theorem. Files through122 are unchanged.

[^extension]: The Stacks Project, [Lemma29.43.5, tag0BX7](https://stacks.math.columbia.edu/tag/0BX7).
    Its displayed statement and full proof were freshly read, together
    with the displayed valuative criterion and neighborhood-extension
    proof in Section29.43, in turn3801view0 and turn3802view0. The target
    is proper and the source local rings at divisor generic points are
    valuation rings. Deeper references inside those proofs were not
    independently reread here.

[^adjunction]: The Stacks Project, [Lemma48.14.1, tag0B4B](https://stacks.math.columbia.edu/tag/0B4B),
    and the tensor form in [Section48.14](https://stacks.math.columbia.edu/tag/0B4A).
    The full displayed two-term Cartier-divisor calculation and its
    tensor version were freshly read in turn3801view1 and turn3802view1.
    Their canonical-sheaf specialization supplies the hypersurface
    adjunction formula. The exceptional discrepancy and the boundary
    multiplicities are separately checked by the explicit charts above,
    not asserted to follow from a classification of surface singularities.
    No deeper derived-duality references were independently reread.
