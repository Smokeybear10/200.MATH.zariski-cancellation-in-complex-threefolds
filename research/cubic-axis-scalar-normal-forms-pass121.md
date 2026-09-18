# Two scalar normal forms for the constant cubic axis

The constant ambient axis supplied by120 puts the remaining actual cubic
metric into one of two explicit forms by a constant complex change of
the three original good coordinates. In either form the remaining
two-by-two block is determined by a single element D of the rational
first-integral field and its derivatives with respect to a nonconstant
normal ratio h. The field may be a proper finite extension of C(h).

These are necessary normal forms, not an exclusion or a construction of
an original frame. In particular, the argument does not make h a field
generator or a polynomial coordinate.

## 1. Actual setting and the constant-axis input

Retain the full supplied actual constant-acceleration hypotheses of
[potential90](nonconical-quadratic-potential-pass90.md) and
[cubic-relation90](nonconical-cubic-relation-pass90.md), in the exact
relative degree-three branch. The exclusions120 and the
[constant-axis theorem120](cubic-nondegenerate-conic-axis-pass120.md)
give the following data:

\[
\begin{gathered}
B=\mathbb C[x_1,x_2,x_3,z]=A[u],\quad A=\ker E,\quad
Eu=1,\quad Ez=q_0u,\quad q_0\in\mathbb C^*,\\
S=\mathbb C[s_1,s_2],\quad K=\operatorname{Frac}(S),\quad
b=E(x_1,x_2,x_3)^t\in S^3,\quad
\Omega=\det[b,b_{s_1},b_{s_2}]\ne0,\\
L=\ker(V|K)=\mathbb C(H),\quad
Q\in\operatorname{Sym}_3(L),\quad n\in L^3\setminus\{0\},\quad
Q_H=\kappa nn^t\ne0,\quad\kappa\in L^*,\\
Q(b,b)=-1,\quad n^tb=0,\quad
\operatorname{rank}Q=3,\quad
\operatorname{rank}(Q|_{\ker n^t})=2,\\
v_0\in\mathbb C^3\setminus\{0\},\quad n^tv_0=0,\quad
\ell_0:=Qv_0\in\mathbb C^3\setminus\{0\} .
\end{gathered}
\tag{1}
\]

Here Q(v,w) means v transposed Qw, subscript H denotes d/dH on L,
and V is the nonzero rational cubic direction. The derivation E and
the four original coordinates are actual. The vector v0 and covector
ell0 are constant in the original ambient complex vector space, not
merely constant along V. This is precisely the conclusion requiring
the full cubic volume argument120.

The lower-rank metric cases are excluded by
[degenerate-metric120](cubic-general-degenerate-metric-exclusion-pass120.md),
and the rank-one plane restriction by
[general-ruled120](cubic-general-ruled-exclusion-pass120.md).
The scalar alpha=ell0 transposed v0 is a complex constant. We separate
the two possibilities alpha nonzero and alpha zero. This separation
is relative to the selected axis; it does not assert uniqueness of
that axis or disjointness under all possible axis choices.

## 2. The two bases are constant ambient bases

If alpha is nonzero, rescale v0 by a nonzero complex scalar so that
Q(v0,v0)=-1. Its orthogonal complement is the fixed complex plane
ker(ell0 transposed), because ell0 is constant. Choose a constant
basis of that plane and use it after e1=v0. The resulting matrix
has first row and column (-1,0,0).

If alpha is zero, take e1=v0. Choose a constant e2 in ker(ell0
transposed) independent of e1 and a constant e3 with ell0 transposed
e3=1. These three vectors form a basis, since e3 is outside that
plane. The first row and column of Q in this basis are (0,0,1).
Thus, with a symmetric block M over L,

\[
\begin{array}{ll}
\text{non-null axis:}&
Q=\begin{pmatrix}-1&0&0\\0&M_{11}&M_{12}\\0&M_{12}&M_{22}\end{pmatrix},\\[8pt]
\text{null axis:}&
Q=\begin{pmatrix}0&0&1\\0&M_{11}&M_{12}\\1&M_{12}&M_{22}\end{pmatrix} .
\end{array}
\tag{2}
\]

To specify the coordinate change, let C have the chosen constant basis
vectors as columns. Replace the actual good-coordinate column by
C inverse x, its velocity by C inverse b, the metric by C transposed
QC, and the normal by C transposed n. Since C belongs to GL3(C),
this is a genuine linear automorphism of the original polynomial
four-ring, fixing z. It preserves the constant-acceleration conditions
and changes Omega only by a nonzero constant. We now suppress these
coordinate-change decorations. No matrix over L or S has been used
as an ambient coordinate change.

## 3. The normal ratio is nonconstant, but need not generate L

The new first component of n is zero because e1 is the axis. Write
n=(0,n2,n3) transposed. The entry n2 cannot vanish identically: otherwise
n transposed b=0 makes the third speed identically zero, and b and its
two base derivatives lie in a fixed plane, contradicting Omega nonzero.
Normalize n by n2 and write it as (0,1,-h) transposed.

If h were a complex constant, the same equation would put the entire
velocity in a fixed complex plane, again contradicting Omega. Therefore
h is nonconstant. Since h belongs to the one-variable rational field
L=C(H), it has nonzero H derivative and makes L a finite separable
extension of C(h). Define

\[
\begin{gathered}
n=(0,1,-h)^t,\qquad h\in L\setminus\mathbb C,\qquad
L/\mathbb C(h)\text{ finite separable},\\
\delta=(h_H)^{-1}d/dH,\qquad \delta h=1,\qquad L^\delta=\mathbb C,\\
\delta Q=\nu nn^t,\quad \nu\in L^*,\qquad
b=(g,hy,y)^t,\quad g,y,hy\in S,\quad y\ne0 .
\end{gathered}
\tag{3}
\]

For the finite-extension assertion, write h as a nonconstant reduced
rational function of H. Its numerator minus h times its denominator
is a nonzero polynomial over C(h) satisfied by H. Characteristic zero
gives separability. The derivation delta is exactly the unique extension
of d/dh from C(h) to L. Its constant field is C since it is a nonzero
L-multiple of d/dH. The rescaling of n and of the derivative only
multiplies kappa by nonzero elements of L, giving nu nonzero.

The last line of (3) follows from n transposed b=0 in the actual
transformed polynomial speed. If y were zero, its second component
would also vanish and Omega would be zero. Both y and hy are
polynomials, but their ratio h is not asserted to be polynomial.
Subsequent primes in this note mean delta, not ordinary differentiation
of a rational function assumed to lie in C(h).

## 4. One scalar reconstructs the varying block

The constant first row and column of (2) have zero derivative. The
remaining derivative and the defining scalar D are

\[
\begin{gathered}
M'=\nu\begin{pmatrix}1&-h\\-h&h^2\end{pmatrix},\qquad
v=(h,1)^t,\qquad M'v=0,\\
D:=v^tMv=h^2M_{11}+2hM_{12}+M_{22}\in L,\\
D'=2(hM_{11}+M_{12}),\qquad D''=2M_{11} .
\end{gathered}
\tag{4}
\]

Indeed v'=(1,0) transposed and the term v transposed M'v vanishes.
Differentiating once more gives
D''=2(M11+hM11'+M12')=2M11, since M11'=nu and M12'=-hnu.
Solving these identities for all three matrix entries yields

\[
M_{11}=\frac{D''}{2},\qquad
M_{12}=\frac{D'-hD''}{2},\qquad
M_{22}=D-hD'+\frac{h^2D''}{2},\qquad
\nu=\frac{D'''}2\ne0 .
\tag{5}
\]

Every operation takes place in the differential field (L,delta).
The formulas hold equally when D is algebraic but not rational over
C(h). Conversely, differentiating the three expressions in (5)
recovers the matrix derivative in (4). This converse is a coefficient
identity only, not an actual-frame realization criterion.

## 5. Determinants and whole polynomial speed identities

For a non-null axis, substituting b=(g,hy,y) into Q(b,b)=-1 and
expanding the determinant gives

\[
\begin{gathered}
g^2-Dy^2=1,\qquad Dy^2=g^2-1\in S,\\
\det Q=\frac{(D')^2-2DD''}{4}\ne0,\qquad
D\ne0,\qquad D'''\ne0,\\
(\det Q)'=-\frac12DD'''\ne0 .
\end{gathered}
\tag{6}
\]

For the condition D nonzero, the plane ker n has basis e1 and
(0,h,1) transposed. Its restricted matrix is diag(-1,D), so its
rank-two hypothesis in (1) is exactly D nonzero. Formula (5) gives
the nonzero third derivative. The determinant follows from
det Q=-det M and cancellation of the h-dependent terms. Its
derivative is then the last line of (6).

For a null axis the corresponding formulas are

\[
\begin{gathered}
2gy+Dy^2=-1,\qquad Dy^2=-1-2gy\in S,\\
\det Q=-\frac{D''}{2}\ne0,\qquad
D''\ne0,\qquad D'''\ne0,\\
(\det Q)'=-\frac{D'''}2\ne0 .
\end{gathered}
\tag{7}
\]

Here expansion along the first row gives det Q=-M11. The restricted
matrix on the same plane basis is [[0,1],[1,D]], whose determinant
is -1; its nondegeneracy does not require an additional scalar
condition on D. Ambient rank three gives D'' nonzero, and (5)
gives D''' nonzero. Both polynomial identities (6) and (7) are
identities of the actual global speed entries, not just of a
formal parametrization after a field extension.

## 6. Exact scope

The identities put D times y squared in S. They do not put D or
D times y in S. In the null case it would therefore be invalid to
read y(2g+Dy)=-1 as a product of two polynomials and conclude that
y is a unit. Likewise, g squared minus D times y squared equal to
one does not supply a polynomial factorization over S without
further coefficient information.

The ratio h may generate a proper subfield of L, so the proof does
not replace D by a rational function of h. The derivatives in (5)--(7)
must retain the extended derivation delta. There is no assertion that
(h,y) or any other rational pair is a polynomial coordinate system
on the invariant plane.

This proof uses the constant-axis theorem120 as a prerequisite and
adds constant-basis and differential-field algebra. Its entire saved
proof was freshly read, and the distinction between the two actual
axis norms was checked directly. No new primary source, test execution,
global recognition, or original-frame construction is claimed. All
files through120 remain unchanged.
