# Exact nice-frame criterion for a triangular polynomial pencil

For the actual pair of sliced actions
\[
E=\partial_s,\qquad
T=\partial_A+s f(A)\partial_B+s g(A)B\partial_C
\quad\text{on }R=\mathbb C[A,B,C,s],
\tag{1}
\]
a polynomial coordinate frame making T a coordinate partial and E
nice exists if and only if f and g are linearly dependent over
\(\mathbb C\). This statement allows zero polynomials and arbitrary
degrees. Whenever the derived intrinsic field is nonzero and such
a frame exists, its primitive division has an explicit polynomial
coordinate slice.

This classifies this candidate construction, not every nice sliced
action. It extends the all-degree obstruction for the
[single triangular candidate in pass75](triangular-primitive-candidate-obstruction-pass75.md).
The purpose is to eliminate all nonfree members of this construction
from the simultaneous nice/good-partial search. There is no new
general cancellation or primitive-freeness theorem here.

## 1. The actual pair and a polynomial T-coordinate frame

Both fields in (1) are locally nilpotent. E has slice s, and T is
triangular with slice A. The derived field and the double-adjoint
identity are
\[
Q=[T,E]=-d,\qquad
d=f(A)\partial_B+g(A)B\partial_C,
\qquad [E,Q]=0.
\tag{2}
\]
The field d is a triangular LND on the actual invariant ring
\(\ker E=\mathbb C[A,B,C]\). In particular Q fixes s, so its
adjustment to this supplied E-slice is already Q itself.

Choose polynomial antiderivatives
\[
F'=f,\qquad G'=g,\qquad H'=Gf.
\tag{3}
\]
Their integration constants may be arbitrary. Put
\[
a=A,\qquad
b=B-sF(A),\qquad
c=C-sG(A)B+s^2H(A),
\tag{4}
\]
with s unchanged. The inverse is
\[
A=a,\qquad B=b+sF(a),\qquad
C=c+sG(a)b+s^2\bigl(G(a)F(a)-H(a)\bigr).
\tag{5}
\]
For the forward substitution into (5), the correction to C is
\(-sGB+s^2H+sG(B-sF)+s^2(GF-H)=0\).
For the reverse substitution into (4), the correction to c is
\(sGb+s^2(GF-H)-sG(b+sF)+s^2H=0\).
The A and B coordinates cancel directly in both orders.
Thus (4)--(5) are actual two-sided polynomial inverses.

Using (3) gives Tb=Tc=Ts=0 and Ta=1. Consequently
\[
R=\mathbb C[a,s,b,c],\qquad T=\partial_a,
\qquad \ker T=\mathbb C[s,b,c].
\tag{6}
\]
In these coordinates E takes the exact form
\[
E=\partial_s-F(a)\partial_b
 +\left[-G(a)b+s\bigl(2H(a)-G(a)F(a)\bigr)\right]\partial_c,
\qquad E^2c=2H(a).
\tag{7}
\]
The last identity uses Ea=0, Eb=-F(a) and Es=1. No polynomial
inverse, kernel presentation or localized slice is assumed in
this calculation.

## 2. A two-jet obstruction to every alternative frame

Assume f is not zero, so F is nonconstant. Suppose some polynomial
coordinate frame \((t_0,t_1,t_2,t_3)\) makes T=partial_(t0) and
makes E nice. The three T-invariant coordinates generate its entire
kernel, hence
\[
\mathbb C[t_1,t_2,t_3]=\mathbb C[s,b,c],\qquad
E^2t_i=0\quad(1\leq i\leq3).
\tag{8}
\]
They are therefore an actual polynomial coordinate system of
\(\mathbb C[s,b,c]\). Their Jacobian in s,b,c is invertible at
the origin. At least one of them, denoted r, must satisfy
\(r_c(0,0,0)\ne0\).

For any polynomial r(s,b,c), evaluate E^2r using (7) at s=b=c=0,
while retaining the independent polynomial variable a. The value
of E on (s,b,c) at that point is (1,-F(a),0), and the value of
E^2 on that triple is (0,0,2H(a)). Thus
\[
\left.E^2r\right|_{s=b=c=0}
=r_{ss}(0)-2F(a)r_{sb}(0)+F(a)^2r_{bb}(0)
 +2H(a)r_c(0).
\tag{9}
\]
All displayed derivatives of r are complex constants. Since E^2r=0
and rc(0) is nonzero, (9) proves
\[
H=h_0+h_1F+h_2F^2
\quad\text{for some }h_0,h_1,h_2\in\mathbb C.
\tag{10}
\]
Differentiate this polynomial identity in a. Equation (3) gives
\(Gf=(h_1+2h_2F)f\). Since f is a nonzero polynomial, cancellation
in the domain \(\mathbb C[a]\) gives G=h1+2h2F. Differentiating
again yields
\[
g=2h_2 f.
\tag{11}
\]
This proves the necessary constant-proportionality condition.
It uses no degree bound on the hypothetical coordinates. High-degree
terms in r cannot change the exact necessary identity (9).

The argument allows every T-slice, not only t0=a. Indeed every such
slice is a plus an element of \(\mathbb C[s,b,c]\), and in any
T-coordinate frame the three invariant coordinates must still
satisfy (8). A nonzero constant vector field can be made a partial
by a constant linear change of coordinates, which preserves niceness;
allowing that formulation of a good direction changes nothing.

## 3. Explicit positive frames and primitive division

Conversely, suppose f is nonzero and g=lambda f for a complex
constant lambda. Choose F'=f and use the simpler coordinates
\[
a=A,\qquad s=s,\qquad
b=B-sF(A),\qquad c_0=C-\frac{\lambda}{2}B^2.
\tag{12}
\]
Their inverse is
\[
A=a,\qquad B=b+sF(a),\qquad
C=c_0+\frac{\lambda}{2}\bigl(b+sF(a)\bigr)^2.
\tag{13}
\]
Both inverse orders cancel directly, first in B and then in C.
Direct application of the original fields gives
\[
T=\partial_a,\qquad E=\partial_s-F(a)\partial_b.
\tag{14}
\]
E is nice in this actual frame. In the original E-invariant ring,
\[
d=f(A)\left(\partial_B+\lambda B\partial_C\right),
\qquad
D=\partial_B+\lambda B\partial_C,
\qquad DB=1.
\tag{15}
\]
Here D is the primitive division up to a nonzero constant: the gcd
of f(A) and lambda f(A)B is f(A), including lambda=0.
The coordinates \((A,B,C-\lambda B^2/2)\) identify D with a
coordinate partial, so its fixed-locus ideal is the unit ideal.

It remains to handle f=0. For any g, choose G'=g and take
\[
a=A,\qquad b=B,\qquad c_0=C-sG(A)B,
\qquad
T=\partial_a,\quad E=\partial_s-G(a)b\partial_{c_0}.
\tag{16}
\]
The inverse is C=c0+sG(a)b with A=a and B=b. This is again an
actual nice frame. If g is nonzero, then d=g(A)B partial_C and its
primitive division is partial_C, with slice C in the original
E-invariant ring. If f=g=0, then Q=d=0 and there is no nonzero
primitive intrinsic direction to divide. These cases establish
the asserted criterion, including its zero boundaries.

## 4. What the classification excludes

The pass75 candidate has f(A)=A and g(A)=2, which are linearly
independent. It therefore cannot be repaired by any T-coordinate
change into a nice frame. More generally, every member of (1)
with a primitive intrinsic fixed point fails to admit a simultaneous
nice/partial frame, because every member that admits one has the
explicit primitive slice in Section 3.

The converse of that last implication is not asserted. For example,
f=1 and g=A already give d a slice B, but fail the constant-
proportionality criterion and hence admit no simultaneous nice frame
with this T. Primitive freeness is weaker than the frame condition
inside this candidate family.

The construction begins with the already recognized E=partial_s.
It does not furnish a new recognition theorem or cover every nice
sliced action and derived good partial. Its exact contribution is
a complete all-degree obstruction and converse for a larger
triangular candidate family. Different actions, different choices
of T and constructions outside (1) remain outside this proof.

## 5. Verification and preservation

An inline exact SymPy calculation checked (9) with an unspecified
function r(s,b,c), and separately checked both positive inverse
orders and niceness with F(A)=A^4+A and arbitrary constants
h0,h1,h2. These finite identities are not a proof of the universal
frame obstruction; Sections 1--3 give that written argument.
There is no new standalone numerical suite, method count or full
regression execution. The complete saved proof was self-read through
EOF. All pass75-or-earlier artifacts and shared metadata remain
unchanged.
