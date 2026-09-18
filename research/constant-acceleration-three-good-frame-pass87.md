# Three good coordinates give a cubic bad adjoint, not the nice rank cap

For a sliced action whose three original companion coordinates are
E-affine and whose remaining coordinate has nonzero constant
acceleration, the velocity Jacobian satisfies the same differential
identity as in the nice case. The acceleration column has one extra
vanishing power. The nice-case rank bound nevertheless fails, even
for an explicit triangular action with a polynomial inverse.

## 1. General actual-frame identities

Work in original polynomial coordinates, and retain the original
globally sliced LND:
\[
B=\mathbb C[x_1,x_2,x_3,z]=A[u],\qquad A=\ker E,
\qquad E(x_i)=b_i\in A\ (i\le3),\qquad
E(z)=qu,\qquad E(u)=1,\qquad q\in\mathbb C^*.
\tag{1}
\]
For an initial supplied slice one obtains this centered u by setting
u=E(z)/q. Write P=(b_1,b_2,b_3,qu) transposed, J=Jac(P), and e_i
for the four constant standard columns. The actual exponential and
its actual inverse give
\[
\Phi_\tau(x)=x+\tau P(x)+\frac q2\tau^2e_4,
\qquad D\Phi_\tau=I+\tau J,
\qquad \det(I+\tau J)=1.
\tag{2}
\]
The inverse is Phi at negative tau, as maps over C[tau]. Thus the
determinant is a unit in B[tau], hence a complex constant, and its
value at tau=0 is one. Comparing the characteristic polynomial and
applying Cayley--Hamilton gives J to the fourth equal to zero.
Differentiating the constant identity E(P)=q e_4 entrywise gives
\[
JP=qe_4,\qquad E(J)=-J^2,\qquad J^4=0.
\tag{3}
\]
All of these are identities in the original polynomial ring. There
is no assumption that formal nilpotent matrix data integrate to an
action. In particular JP is not zero, unlike the nice-action setting.

Let T_i be the actual original coordinate partial. Its first adjoint
has coefficient column -J e_i. Since E(J to the j)=-j J to the j+1,
the derivation bracket product rule proves by induction that
\[
\operatorname{ad}_E^j(T_i)(x)
 =(-1)^j j!J^j e_i\quad(j\ge0),\qquad
J^3e_4=q^{-1}J^4P=0,
\qquad \operatorname{ad}_E^3(T_z)=0.
\tag{4}
\]
For the induction, a field with coefficient column C has bracket
coefficient E(C)-JC. This supplies the extra factor j+1 and the
sign. Every original partial has fourth adjoint zero, whereas the
bad partial T_z has third adjoint zero. These are adjoint statements;
they must not be replaced by or identified with coordinate flow
degrees. The identity J cubed e_4=0 does not say J cubed=0.

There is also a useful exact rank reduction over K=Frac(B):
\[
\operatorname{rank}_K J
 =1+\operatorname{rank}_K d(b_1,b_2,b_3)\le3.
\tag{5}
\]
The covector du is independent of the span of the db_i, since
evaluation on E gives one on the former and zero on the latter.
The last row of J is q du. The rank bound follows from nilpotence
of J. Hence rank three corresponds to a two-dimensional good-speed
image, and rank two to a curve image, in the sense of transcendence
degree of C(b_1,b_2,b_3) in characteristic zero. This does not say
that the coordinate algebra of either image is polynomial or regular.

The rank-one branch is elementary: (5) makes each b_i a complex
constant. They cannot all vanish. Otherwise E=qu partial_z with
the x_i fixed, and E squared z would be (qu) partial_z(qu)=q.
A polynomial v in z over C[x_1,x_2,x_3] cannot satisfy v v_z=q:
degree zero gives zero, and positive degree gives positive degree
2 deg(v)-1. Some original x_i therefore has nonzero constant
E-velocity. Dividing it by that constant gives an actual coordinate
slice, and A is B modulo that coordinate, hence C cubed. This
recognizes only the rank-one branch of (1).

## 2. An actual regular-nilpotent Jacobian

Use canonical polynomial coordinates (u,r,t,c), set E=partial_u,
and define the original frame and its inverse by
\[
\begin{gathered}
x_1=u,\qquad x_2=t+ur,\qquad x_3=c+ut,
\qquad z=r+u^2,\\
u=x_1,\qquad r=z-x_1^2,\qquad
t=x_2-x_1r,\qquad c=x_3-x_1t.
\end{gathered}
\tag{6}
\]
Direct substitution proves both polynomial inverse orders, each
with Jacobian determinant one in the displayed variable orders.
In particular this is an actual sliced action, not a hypothetical
coefficient table. Its flow degrees in the original frame are
(1,1,1,2), with q=2. In those original coordinates the velocity and
its Jacobian are
\[
P=\begin{pmatrix}1\\z-x_1^2\\x_2-x_1(z-x_1^2)\\2x_1\end{pmatrix},
\qquad
J=\begin{pmatrix}
0&0&0&0\\
-2x_1&0&0&1\\
3x_1^2-z&1&0&-x_1\\
2&0&0&0
\end{pmatrix}.
\tag{7}
\]
Multiplication gives
\[
\operatorname{rank}(J,J^2,J^3)=(3,2,1),\qquad
J^3=2e_3e_1^{\mathsf T}\ne0,\qquad
J^4=0,\qquad JP=2e_4,\qquad J^2e_4=e_3.
\tag{8}
\]
Thus neither J cubed=0 nor rank J at most two can be transferred
from the nice case to (1). The actual adjoint heights of the four
partials are (4,2,1,3): the fourth and third bounds in (4) are
attained. This action is already recognized by the actual coordinate
slice x_1. It is not a counterexample to a global u-coordinate or
recognition assertion, and it does not exhibit an unresolved frame.

## 3. A genuine highest LND, but no forced critical-value slice

The bad-partial bound in (4) has a useful direct expression in the
actual slice presentation. Since E=partial_u, its third adjoint
annihilates every coefficient of T=T_z. Extracting coefficients on
a finite set of generators of A gives complex derivations D_j of A,
and initially T(u) also has degree at most two in u. Write
r=z-q u squared/2 in A. The equality T(z)=1 has no cubic contribution
from T(r), so its cubic coefficient kills the quadratic term of T(u).
The exact resulting system is
\[
T|_A=D_0+uD_1+u^2D_2,\qquad T(u)=h_0+uh_1,
\qquad D_0r=1,\quad D_1r=-qh_0,\quad D_2r=-qh_1,
\qquad h_0,h_1\in A.
\tag{9}
\]
The field D_2 on A, extended by D_2(u)=0, is locally nilpotent
(possibly zero). Here is the actual-ring justification. Over
B[epsilon,epsilon inverse], conjugate the original LND T by the
automorphism alpha which fixes A and epsilon and sends u to
u+epsilon inverse. Multiply this conjugate by epsilon squared.
It remains an LND, since epsilon is in its kernel. Formula (9)
shows that the resulting field preserves B[epsilon], and its value
at epsilon=0 is exactly D_2. The restriction is locally nilpotent
because this polynomial ring injects into its localization, where
each element is killed by a finite iterate. Specialization is
therefore locally nilpotent as well. In particular
\[
V=\operatorname{ad}_E^2(T)=2D_2,\qquad
V(u)=0,\qquad [E,V]=0,\qquad V(r)=-2q h_1.
\tag{10}
\]
This is the same highest-coefficient degeneration mechanism used
in the retained [vertical-top proof](vertical-top-exclusion-pass69.md),
not a new general existence theorem for LNDs. The quadratic
coordinate equation gives the especially direct splitting (9).
It is different from averaging T with an involution: there is a
specific localization, invariant scaling, and specialization here.

Nonzero V need not move r, even when J has rank three. In the actual
control (6), the bad partial in canonical coordinates is
partial_r-u partial_t+u squared partial_c. Thus D_2=partial_c,
V=2 partial_c, and h_0=h_1=0. Consequently V is nonzero but V(r)=0.
No slice for the critical-value function follows from (10).

## 4. Verification scope

The standalone
[one-method checker](constant_acceleration_frame_checks_pass87.py)
imports only unittest and SymPy. It checks the actual inverse and
flow inverse in both orders, the Jacobian determinants and transport,
the coordinate slice, (3), all four exact adjoint columns through
order four using polynomial derivation brackets, the ranks and powers
in (8), and the distinction between the four flow degrees and four
adjoint heights. It also checks the actual bad-partial transport in
(9) for this control and the nonzero highest field fixing r. The
general statements (2)--(5), (9)--(10), the degeneration argument,
and the rank-one argument are written proofs, not claims certified
by the example.

Root identified the general constant-acceleration Jacobian identities
and suggested the velocity-image reduction. Jet reconstructed the
adjoint-column consequence, rank-one branch, and this explicit rank
three control. An initial inline exact calculation agreed with (8),
chunk f81af7; it was not a unittest suite. The first standalone run
passed one method in 0.067 seconds, exit zero, with full output in
chunk 4f4074. The later highest-field checks were added within that
same method. The final one-method run passed in 0.063 seconds,
exit zero, chunk a5d052; the final checker SHA-256 is
0efa132db7c269a46869aa7714304e76f15daa4a68bb73c52d22f75ddf99925f.
No mathematical assertion failed. The proof and checker received complete author
reads through EOF. This adds only a separate
new pass87 note and one-method checker; all earlier artifacts remain
unchanged. No full regression, general linearization theorem, or
unrestricted recognition is asserted.
