# A higher commutator need not be locally nilpotent in an actual nonconical frame

The original last partial and its highest E-adjoint are locally
nilpotent, but their bracket need not be. The following polynomial
inverse pair realizes that failure under all three-good-coordinate,
nonzero-constant-acceleration hypotheses. Its good-speed image is
nonconical. The example is already recognized by a coordinate slice,
so it is not a model of the remaining branch without an affine linear
speed relation.

## 1. An actual frame, not a coefficient prescription

Start with canonical polynomial coordinates \(u,r,\ell,t\), and let
\(E=\partial_u\). Set
\[
x_1=u,\qquad x_2=t+u\ell,\qquad
x_3=r(t+u\ell)-\ell,\qquad z=r+u^2.
\tag{1}
\]
The actual inverse is
\[
u=x_1,\qquad r=z-x_1^2,\qquad
\ell=r x_2-x_3,\qquad t=x_2-x_1\ell .
\tag{2}
\]
Substituting either tuple into the other gives the identity. The
Jacobian determinant in the displayed variable orders is one.
In particular \(B=\mathbb C[x_1,x_2,x_3,z]\) is the original
polynomial ring, not an assumed presentation.

The kernel is \(A=\mathbb C[r,\ell,t]\), and the good-speed row and
acceleration are
\[
b=(1,\ell,r\ell)^t,\qquad E^2x_i=0\ (i\leq3),\qquad
E^2z=2,\qquad
\Omega=\det[b,b_r,b_\ell]=-\ell\ne0 .
\tag{3}
\]
Thus the good-speed map has rank two. The first speed is one, so
\(x_1\) is already an original coordinate slice. This recognized
case is sufficient to disprove a claimed consequence of the stated
frame hypotheses, but says nothing about existence in the narrower
remaining no-affine-relation class.

## 2. The actual partial and its highest adjoint

Transport the original \(T=\partial_z\) through (2), holding the
three \(x_i\) fixed. In canonical coordinates the resulting fields are
\[
\begin{aligned}
T&=\partial_r+(t+u\ell)\partial_\ell
       -u(t+u\ell)\partial_t,\\
Q:=[E,T]&=\ell\partial_\ell-(t+2u\ell)\partial_t,\\
H:=[E,Q]&=-2\ell\partial_t,\qquad [E,H]=0 .
\end{aligned}
\tag{4}
\]
This proves that \(T\) is an actual LND by coordinate conjugation,
and that \(H\ne0\) is an actual LND by its displayed triangular
formula. The latter fixes \(u\), all \(b_i\), and the centered
invariant \(z-u^2=r\). Its restriction to \(A\) has kernel
\(S=\mathbb C[r,\ell]\), and \(H\) vanishes on the divisor
\(\ell=0\). Primitive division gives \(-2\partial_t\), which has a
global slice in this example. Thus this is not a primitive fixed-point
counterexample.

The coefficient splitting from the retained
[three-good-frame proof87](constant-acceleration-three-good-frame-pass87.md)
is exact here:
\(D_0=\partial_r+t\partial_\ell\),
\(D_1=\ell\partial_\ell-t\partial_t\),
\(D_2=-\ell\partial_t\), and \(h_0=h_1=0\).
In particular the middle coefficient \(D_1\) need not be an LND.
If \(J\) denotes the velocity Jacobian in the original coordinates,
the retained adjoint formula identifies \(H(x)=2J^2e_4\).
The original Jacobian has ranks \(3,2,1\) in its first three powers
and fourth power zero, so this is genuinely the highest bad adjoint
in the regular-nilpotent case.

## 3. The next brackets do not supply another intrinsic LND

Direct polynomial derivation brackets give
\[
[T,H]=2Q,\qquad [Q,H]=2H,\qquad
Q(\ell)=\ell,\qquad
Q^n(\ell)=\ell,\qquad [T,H]^n(\ell)=2^n\ell\quad(n\geq1).
\tag{5}
\]
The last two formulas follow by induction and characteristic zero.
Consequently neither \(Q\) nor \([T,H]\) is locally nilpotent.
The failure is for an actual coordinate partial \(T\) and an actual
highest-adjoint LND \(H\), not an arbitrary pair of vector fields.

There is another actual LND among the brackets, but it does not
restrict to the original kernel:
\[
R:=[T,Q]=-2x_2\partial_{x_3},\qquad
[E,R]=2Q,\qquad
R(\ell)=2(t+u\ell)\notin A.
\tag{6}
\]
Here the expression for \(R\) is in the original coordinates.
It proves local nilpotence directly. Since \(\ell\in A\) but its
image depends on \(u\), \(R\) does not preserve \(A\).
Thus merely producing this additional LND is not an intrinsic
relative-slice argument.

The four fields \(E,T,Q,H\) do span the tangent space generically:
their determinant is \(-2\ell^2\), in either displayed coordinate
system. It is not a unit. This agrees with the nonconical cyclic
Jacobian observation; it does not strengthen generic spanning to
spanning at every point.

## 4. Exact verification and scope

The standalone
[checker](nonconical_higher_commutator_checks_pass90.py) contains one
unittest method and imports only unittest and SymPy. It checks both
polynomial inverse orders, both Jacobian determinants, the actual
partial transport, all coordinate velocities, the original-J
highest-adjoint identity and ranks, the brackets in (4)--(6), the
generic determinant, and finitely many instances of the iterates
in (5). The displayed induction, not those finitely many instances,
proves failure of local nilpotence.

Jet derived this bounded inverse-frame control while investigating
Root's nonconical higher-commutator question. An initial inline
calculation checked the inverse and bracket formulas in tool chunk
4d53a5; it was not a unittest method. The first standalone run passed
one method in 0.309 seconds, exit zero, with the complete output in
tool chunk 903b9c. No assertion failed. The complete saved proof and
checker received author reads through EOF; the final provenance
paragraph was then checked separately.
There is no novelty claim, new source theorem, recognition claim
for the unresolved branch, runner, integration capture, or full
regression. Pass89 and earlier files remain unchanged.
