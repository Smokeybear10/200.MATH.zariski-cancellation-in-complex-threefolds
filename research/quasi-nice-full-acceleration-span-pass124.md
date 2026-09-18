# An actual quadratic-time frame with no affine-linear good direction

There is an actual polynomial coordinate frame on complex affine four-space
for a translation derivation in which every coordinate has exact time degree
two, and no nonconstant affine-linear combination has time degree at most
one. Thus quadratic time dependence does not even supply one good direction
by a constant affine change of the given frame. It cannot by itself give the
three good directions needed by the
[constant-acceleration recognition statement123](cubic-exclusion-frontier-pass123.md).

This is an explicitly recognized translation, not a cancellation
counterexample. The claim concerns constant affine changes of this particular
frame, not arbitrary polynomial coordinate changes.

## 1. A polynomial automorphism and its inverse

Work in B=C[u,v,z,w] with E=partial_u. Define successively

\[
\begin{aligned}
r&=u+v^2, &Y&=v+r^2,\\
Z&=z+vY, &W&=w+v^2Y,\\
X&=r+YW-Z^2.
\end{aligned}
\tag{1}
\]

Each replacement is elementary: replace u by r, then v by Y, then z by Z,
then w by W, and finally r by X. During the third and fourth replacements,
the old v is the polynomial Y-r squared in the unchanged coordinates r,Y.
Consequently these are actual coordinate changes, not generic changes over
an invariant fraction field. Their inverse is explicitly

\[
\begin{aligned}
r&=X-YW+Z^2, &v&=Y-r^2,\\
u&=r-v^2, &z&=Z-vY, &w&=W-v^2Y.
\end{aligned}
\tag{2}
\]

The formulas prove both compositions directly, and every elementary step has
Jacobian determinant one. In particular B=C[X,Y,Z,W]. The polynomial r is a
coordinate slice, Er=1, and ker E=C[v,z,w]. The inverse already supplies a
nonlinear recognition of the action.

## 2. Exact quadratic time dependence

The cancellation responsible for the time-degree bound is

\[
YW-Z^2=Y(w-2vz)-z^2,\qquad
(EX,EY,EZ,EW)
 =\bigl(1+2r(w-2vz),\ 2r,\ 2vr,\ 2v^2r\bigr).
\tag{3}
\]

Here v,z,w are E-invariant. Hence

\[
\bigl(E^2X,E^2Y,E^2Z,E^2W\bigr)
 =2\bigl(w-2vz,\ 1,\ v,\ v^2\bigr),\qquad
E^3X=E^3Y=E^3Z=E^3W=0.
\tag{4}
\]

Each displayed second derivative is a nonzero polynomial. All four given
coordinates therefore have exact E-degree two. The acceleration ideal is
the unit ideal, since E squared Y equals two. This does not make the
acceleration functions constant or reduce their complex linear span.

## 3. The full affine-linear obstruction

For constants c0,c1,c2,c3,c4 and F=c0+c1X+c2Y+c3Z+c4W,

\[
E^2F=2\bigl(c_1(w-2vz)+c_2+c_3v+c_4v^2\bigr).
\tag{5}
\]

The coefficient of w first forces c1=0 whenever this expression is constant.
Then the coefficients of v and v squared force c3=c4=0. It follows that
the affine-linear polynomials with constant acceleration are exactly
C+CY. Their acceleration vanishes only when c2=0. Equivalently, the four
acceleration functions in (4) are complex-linearly independent, the maximum
possible dimension for a four-coordinate frame.

Thus there is no nonconstant affine-linear F with E squared F=0, and in
particular no affine-linear slice. Every coordinate in every constant affine
change of (X,Y,Z,W) still has exact E-degree two. No such change can put the
whole acceleration vector in C to the fourth power: the space of eligible
linear parts has dimension one, not four. It also cannot put three second
derivatives equal to zero and the fourth equal to a nonzero constant.

This disproves the specific reduction shortcut that E cubed killing an
actual coordinate frame forces at least one constant-linear good direction.
It does not disprove the existence of a better polynomial frame. Indeed,
(2) gives the nice frame (r,v,z,w), and replacing w there by w+r squared
gives a frame with exactly three zero accelerations and one nonzero constant
acceleration. Any such improvement from the displayed frame must therefore
be genuinely nonlinear.

## 4. Scope and finite verification

The [earlier acceleration-field controls81](acceleration-field-obstruction-pass81.md)
already separate quadratic time dependence from shortcuts involving the
acceleration derivation. The present control addresses the stronger and
different affine-linear issue: its acceleration functions have full complex
span four. No historical novelty claim is made. Root supplied the explicit
construction; this note supplies its reconstruction and bounded verification.

The separate
[checker](quasi_nice_full_acceleration_checks_pass124.py)
checks both polynomial inverse orders, the Jacobian determinant, the full
translation flow, the second and third derivatives, and the exact
coefficient identity (5). It is one finite algebraic example, not a test of
all quadratic-time frames or a proof of arbitrary sliced-derivation recognition.
No file through123 or live index is changed by this note.

The author's run dca807 passed its one method in 0.351 seconds reported by
unittest, with 0.6217931248247623 seconds measured around import and execution.
The proof of the affine-linear obstruction is the coefficient argument in
Section3, not an inference from a sample of numerical values.
