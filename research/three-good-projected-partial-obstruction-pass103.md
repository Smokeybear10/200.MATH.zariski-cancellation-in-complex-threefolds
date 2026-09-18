# The projected original partial can fail local nilpotence in a three-good frame

An actual polynomial four-coordinate frame with three E-affine good
coordinates, nonzero constant acceleration, and nonconstant Omega
need not have a locally nilpotent projected zeroth coefficient.
Both inverse orders below are polynomial. This improves the scope
of the broad one-quadratic-coordinate control87 for this particular
failure, but it is not a counterexample to the stable-fiber statement102.

In fact the frame below has no T-stable closed fiber of its actual
highest-field quotient. That distinction is important when comparing
it with a conclusion proved on every finite thickening of a specified
stable fiber.

## 1. An explicit actual frame and inverse

Begin with polynomial coordinates s,a,v,p and define
\[
\begin{gathered}
B=\mathbb C[s,a,v,p],\qquad E=\partial_s,\\
x_1=s,\qquad x_2=v+a^2s,\qquad x_3=a+v^2+ps,\\
z=2a^2v-p+a^4s+\frac{s^2}{2}.
\end{gathered}
\tag{1}
\]
The inverse is polynomial:
\[
\begin{gathered}
s=x_1,\qquad
a=x_1\left(z-\frac{x_1^2}{2}\right)-x_2^2+x_3,\\
v=x_2-a^2x_1,\qquad
p=2a^2x_2-a^4x_1-z+\frac{x_1^2}{2}.
\end{gathered}
\tag{2}
\]
Substitution in either order gives the identity; no division by a or
by a speed coefficient is used. In the orders (s,a,v,p) and
(x1,x2,x3,z) the determinant is one.

The canonical E-slice and the good-speed row are
\[
\begin{gathered}
u=Ez=s+a^4,\qquad Eu=1,\qquad E^2z=1,\qquad
E^2x_i=0\quad(i=1,2,3),\\
A=\ker E=\mathbb C[a,v,p],\qquad B=A[u],\qquad
\mathbf b=(1,a^2,p)^t,\\
S=\mathbb C[a,p],\qquad
\Omega=\det[\mathbf b,\mathbf b_a,\mathbf b_p]=2a\ne0.
\end{gathered}
\tag{3}
\]
The interpretation of S as the actual highest-field kernel is
verified next, not assumed from the speed coefficients alone.
The speed map has generic rank two; it drops rank where a is zero.
The polynomial Omega is nonconstant.

## 2. The actual original partial and its highest coefficient

Let T be the original partial in z, holding x1,x2,x3 fixed.
Differentiating (2), or applying the resulting field to (1), gives
\[
\begin{gathered}
Ts=0,\qquad Ta=s,\qquad Tv=-2as^2,\qquad Tp=4avs-1,\\
Tu=4a^3s,\qquad s=u-a^4,\\
T=4a^3(u-a^4)\partial_u+(u-a^4)\partial_a
 -2a(u-a^4)^2\partial_v+
 \bigl(4av(u-a^4)-1\bigr)\partial_p,\\
H=\operatorname{ad}_E^2T=-4a\partial_v,\qquad
N=-\partial_v,\qquad H=2\Omega N,\qquad \ker(N|_A)=S.
\end{gathered}
\tag{4}
\]
T is locally nilpotent because it is an actual coordinate partial,
not because the displayed coefficients are triangular in canonical
u. The primitive field N is exactly the canonical Jacobian
determinant of (a,p,u,.) in the original coordinates: its value on
v is minus one, and it kills a,p,u. Thus the highest field and its
primitive division have the asserted actual quotient, including
the sign. H is nonzero, while N is free everywhere.

Let pi_u denote the genuine slice evaluation u to zero, and put
D0 equal to pi_u composed with T on A. Then
\[
\begin{gathered}
D_0=-a^4\partial_a-2a^9\partial_v-(4a^5v+1)\partial_p,\\
D_0^n(a)=(-1)^n
 \left(\prod_{j=0}^{n-1}(1+3j)\right)a^{1+3n}\ne0
 \quad(n\ge0).
\end{gathered}
\tag{5}
\]
For n zero the product is one. The formula follows by induction:
on every polynomial in a alone D0 acts as minus a to the fourth
times the derivative in a. Characteristic zero makes all the
integer factors nonzero. This proves that D0 is not locally
nilpotent; it is not an inference from finitely many iterates.

Nevertheless D0 has the expected global slice:
\[
r=z-\frac{u^2}{2}=2a^2v-p-\frac{a^8}{2}\in A,
\qquad D_0r=1.
\tag{6}
\]
A derivation with a slice need not be locally nilpotent. Here even
its origin as the projection of an actual partial, under all three
good-coordinate hypotheses, does not force that property.

## 3. No stable fiber is being supplied

For every closed base point m=(a-a0,p-p0) of S,
\[
T(a-a_0)=s\notin\mathfrak mB,\qquad
[E,T](a)=1,\qquad T(a)=u-a^4\notin A.
\tag{7}
\]
The image of s in B/mB is a genuine polynomial variable, shifted
from u by a complex constant. Thus no such fiber is T-stable, and
the commutator cannot vanish on it. This example does not satisfy
the stable-whole-fiber premise of102, nor any assertion about all
its finite thickenings. In particular the hypotheses of the
[adic projected-translation theorem103](quadratic-adic-projected-translation-pass103.md)
are not satisfied by this frame. It does prove that global preservation
T(A) inside A and local nilpotence of D0 cannot be inferred merely
from the actual frame, the constant acceleration, or Omega nonzero.

The kernel A is already a polynomial three-ring and x1=s is an
original coordinate E-slice. In particular the example has the
affine speed relation b1=1. It is not a model of the unrecognized
no-affine-relation branch, a primitive fixed-point example, or a
counterexample to cancellation.

## Relation to the retained controls

The [averaging obstruction87](constant-acceleration-averaging-obstruction-pass87.md)
has an actual quadratic coordinate and a non-LND projected field,
but its other original coordinates do not all have E-degree at most
one. The [higher-commutator control90](nonconical-higher-commutator-control-pass90.md)
does satisfy the three-good hypotheses, but its displayed D0 is
locally nilpotent. Both notes were read through EOF before this
construction. The distinction established here is the simultaneous
three-good frame, nonconstant Omega, and non-LND D0, with the stable
fiber hypothesis explicitly absent.

All identities above have direct polynomial proofs. No new source
theorem, unknown actual frame, ambient-coordinate inference from
coefficient data, or global recognition claim is involved. All files
through102 remain unchanged.

## Finite verification and execution scope

The second method of the shared
[two-method checker](projected_derivation_thickening_checks_pass103.py)
tests both actual inverse orders, determinant one, the original
partial and E transports, the canonical N sign and highest field,
the D0 slice and eight finite instances of (5), and the absence of
a stable closed S-fiber. The all-n proof in (5) is the written
induction, not an extrapolation from those instances.

Its first method is the separate abstract finite-thickening control:
it checks compatible finite flows, formal invariant coordinate
inverses and their growing slice degrees. That method is not an
actual four-coordinate frame and does not certify the universal
associated-graded argument. The two distinct methods are not
combined into one assertion about a single example.

An initial two-method execution had a harness error in the k equal
to one subtest: an empty Python sum returned an integer without a
substitution method. The actual-frame method passed in that run
(chunk ca655d). Replacing the empty sum by symbolic zero corrected
the harness; both methods then passed in 0.513 seconds, exit zero,
chunk 1cd092. After adding the finite formal-invariant inverse
checks within the first method, the final two-method author run
passed in 0.299 seconds, exit zero, chunk ff7107 (wall time
0.558049416 seconds). No mathematical assertion failed. No older
solver or checker is imported and no full regression was run.
