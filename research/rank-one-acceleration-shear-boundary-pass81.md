# A rank-one acceleration shear criterion and its actual obstruction

If only one actual coordinate has nonzero acceleration, subtracting a
polynomial in the other three coordinates can sometimes make the action
nice. The exact criterion below is sufficient, but is not automatic even
for a sliced triangular translation with an explicit polynomial inverse.
The obstruction excludes every coordinate change fixing those three
coordinates pointwise, not arbitrary polynomial changes.

The older [time-degree statement audit](mixed-time-degree-literature-addendum.md)
already identifies this as the 3-quasi case and records the missing
invariant-coordinate or actual fixed-base hypotheses of the retained
relative theorems. This note does not replace those hypotheses or establish
historical novelty. Its positive endpoint uses the completed
[nice sliced recognition80](nice-slice-recognition-pass80.md).

## 1. Exact sufficient condition

Let B=C[x_1,x_2,x_3,z], let E be an actual locally nilpotent derivation
with a polynomial slice, and suppose
\[
E^2x_i=0\ (1\le i\le3),\qquad E^2z=q,\qquad Eq=0.
\tag{1}
\]
These hypotheses include the rank-one nonzero constant-vector span of
the full acceleration column, after an actual constant linear change.
They do not assert that E fixes any of the first three coordinates.
Put a_i=Ex_i and let I=(a_1,a_2,a_3)B.

For every F in the actual polynomial subring C[x_1,x_2,x_3], the
ordinary chain rule gives
\[
E^2F=\sum_{i,j=1}^3 a_i a_j F_{x_ix_j}\in I^2.
\tag{2}
\]
The coefficients a_i need not belong to that subring; the identity
holds in the original B and uses E(a_i)=0.

Consequently, if such an F satisfies E^2F=q, the actual triangular
coordinate z'=z-F has E^2z'=0. Its inverse is z=z'+F, fixing the
other three coordinates. The resulting action is nice in an actual
polynomial frame and has the same original slice, so recognition80
gives ker E=C^[3]. In particular the sufficient condition
\[
q=\sum_{i,j=1}^3 m_{ij}a_i a_j,\qquad
M=(m_{ij})\in\operatorname{Mat}_3(\mathbb C),\quad M=M^t
\tag{3}
\]
is handled by F=(x^t M x)/2. This elementary constant-quadratic
specialization does not claim that every q in I^2 solves (2).

There is a necessary obstruction for the entire pointwise fixed-base
automorphism group. Every C[x_1,x_2,x_3]-algebra automorphism of B
sends z to lambda z+F, with lambda in C* and F in that subring:
degrees in z of an automorphism and its polynomial inverse multiply,
so both have degree one, and the leading coefficient must be a unit
of the base. Therefore
\[
q\notin I^2\quad\Longrightarrow\quad
\text{no such coordinate change makes E nice.}
\tag{4}
\]
This is a necessary condition only for this specified group of changes.

The actual slice does impose the weaker necessary condition
\(q\in\sqrt I\). Indeed, let p be a closed point at which every
a_i vanishes. Along its actual E-orbit the a_i remain zero, while
the remaining velocity is
\(Ez(\Phi_t(p))=Ez(p)+tq(p)\). If q(p) were nonzero, choosing
\(t=-Ez(p)/q(p)\) would make all four velocities zero at an actual
point, contradicting Es_*=1. Thus q vanishes on V(I), and the
Nullstellensatz gives the claimed radical membership. This does not
give membership in I^2; the example below explicitly prevents that
upgrade.

## 2. An actual sliced translation which violates the necessary condition

Use original coordinates (a,x,y,c) and the polynomial derivation
\[
E=a^2\partial_x+(1+ax)\partial_y.
\tag{5}
\]
It is triangular and locally nilpotent. Its original coordinate
accelerations are (0,0,a^3,0), and E cubed kills all four coordinates.
The three good-coordinate speeds are (0,a^2,0). Thus
\[
I=(a^2),\qquad q=a^3\notin(a^4)=I^2.
\tag{6}
\]
The repeated power in (6) is essential: a radical or a gcd is not
a substitute for the exact ideal square.

Here is an explicit polynomial slice and both-sided coordinate inverse.
Set
\[
v=x+\frac a2x^2-a^2y,\qquad
s=y+\frac{v^2-x^2}{2a}.
\tag{7}
\]
Although displayed with a denominator, s is polynomial: v-x is
divisible by a in C[a,x,y,c], hence so is v^2-x^2. Direct
differentiation gives Ev=0 and
Es=(1+ax)-xa^2/a=1. This calculation is an equality of polynomials,
not merely a slice on the principal open where a is nonzero.

Conversely, in the independent polynomial variables (a,v,s,c), set
\[
x=v-\frac a2v^2+a^2s,\qquad
y=s+\frac{x^2-v^2}{2a}.
\tag{8}
\]
Again x-v is divisible by a, so y is a polynomial. Substituting
(7) into (8), or (8) into (7), gives every input variable. For example,
the relation defining v becomes v=x+(a/2)v^2-a^2s after the
substitution for y, which is exactly the first equation of (8);
the equation for s is the second. Thus (a,v,s,c) are actual polynomial
coordinates, E is their derivative with respect to s, and
ker E=C[a,v,c]. No division on a deleted fiber is used.

Nevertheless (4) and (6) show that no polynomial change fixing the
three original good coordinates (a,x,c) pointwise can make this E
nice. In particular no polynomial F(a,x,c) has E^2F=a^3:
the left side is a^4 F_xx. The known adapted inverse changes x as
well as y, so it is outside the excluded group, as it must be.

## 3. Scope and verification

The construction in Section 2 was independently proposed by Root and
fully reconstructed here. It is a simple recognized triangular family,
not an asserted novel action. Its role is to disprove automatic
single-direction shear reduction under exactly the original sliced,
quadratic-time, rank-one-acceleration hypotheses.

The companion [acceleration-field control](acceleration-field-obstruction-pass81.md)
shows a separate failure: even rank-one acceleration need not define
an LND. That failure is not used to prove (4).

Neither obstruction disproves recognition of all rank-one-acceleration
actions. A reduction which changes the good coordinates, establishes
an actual invariant coordinate, or constructs a different nice frame
is not excluded. No fixed-base theorem is applied without its actual
base premise, and unrestricted cancellation remains unresolved.

The proof uses exact differentiation and the written two-sided inverses.
An inline symbolic calculation separately checked both inverse orders,
polynomial denominator cancellation, the slice, and the acceleration.
No new standalone suite, full regression, or frozen-file edit belongs
to this note.
