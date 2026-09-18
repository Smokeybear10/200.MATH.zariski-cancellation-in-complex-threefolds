# Exact controls for three quadratic-flow reduction boundaries

The separate [checker](quadratic_reduction_controls_pass81.py) contains
three methods using only unittest and SymPy. Each main example is an
actual polynomial action or an explicitly specified flow-box map. None
is a counterexample to cancellation. These checks do not modify the
separate three-method scalar-filter suite.

## 1. Unit acceleration does not supply an auxiliary LND

The first method reconstructs the actual inverse pair in
[the acceleration obstruction](acceleration-field-obstruction-pass81.md):
\[
(x,y,z,w)=(s,(1+s^2)a+sb,sa+b,c+s^2),\quad E=\partial_s.
\tag{1}
\]
It checks both polynomial inverse orders, the transported original
velocity and its invariant generators, then the actual acceleration
field H=(E squared x) dot partial. Its coefficients include the unit 2,
but H(a)=2a and H to the nth power takes y to 2 to the nth power times
a. The method checks this recurrence for n from 1 through 5; the
written all-n proof uses H(a)=2a. It also checks H(w/2)=1, the nonzero
commutator with E, H squared(x) nonzero, and H's failure to preserve
the original kernel. A unit coefficient or a polynomial sent to one
does not substitute for local nilpotence.

## 2. The actual transverse flow box need not be globally invertible

The second method checks the two maps from
[the flow-box boundary](quadratic-flow-box-source-boundary-pass81.md):
\[
\begin{aligned}
\Psi_2(t,a,b,c)&=(a+t,2at+t^2,b,c),&G_2&=y-2Tx+T^2,\\
\Psi_1(t,s_0,A,Z)&=(s_0+t,A,At,Z),&G_1&=Y-AT.
\end{aligned}
\tag{2}
\]
The first has determinant -2a in the first two variables and
discriminant 4(x squared-y). The latter factor is irreducible with
multiplicity one, so its odd valuation prevents a square in the
rational function field. This is the exact algebra underlying the
generic double cover, not an assertion deduced from numerical samples.
The checker verifies the relation, discriminant, multiplicity and
reverse-flow expression.

The second map has generic rational inverse using T=Y/A, checked
in both orders. Its Y entry vanishes whenever A=0, so it misses all
points A=0,Y nonzero. No polynomial inverse across that divisor is
asserted. The universal generic-degree and global-isomorphism
criteria are proved separately in the written source-scope note;
finite checks do not establish them or its published prerequisites.

## 3. A nonunit-speed rank-one action with an actual global slice

Root supplied the actual action on C[a,x,y,z]
\[
E=a^2\partial_x+(1+ax)\partial_y,\qquad
v=x+\tfrac a2x^2-a^2y,\quad
\sigma=y+\frac{v^2-x^2}{2a}.
\tag{3}
\]
The displayed quotient for sigma is a polynomial: v-x is divisible
by a. Its actual inverse coordinates are
\[
x=v-\tfrac a2v^2+a^2\sigma,\qquad
y=\sigma+\frac{x^2-v^2}{2a},
\tag{4}
\]
with a,z unchanged. The inverse y is polynomial for the same
divisibility reason. The third method first verifies polynomial
membership, then both full inverse orders and the unit Jacobian.
It directly computes E(v)=0,E(sigma)=1,E(a)=E(z)=0, establishing
the transported translation and hence local nilpotence. It also
checks all original velocity/acceleration entries and E cubed(x)=0.

The sole nonzero acceleration is E squared(y)=a cubed. With
f=E(x)=a squared, the acceleration q=a cubed does not belong to
(f squared)=(a to the fourth power). A polynomial remainder verifies
that specific nonmembership. The field nevertheless has a global
polynomial slice and explicit adapted coordinates, including on a=0.
Thus this square-speed divisibility cannot be inferred from the
stated actual hypotheses. No general rank-one classification is
inferred from the example.

## 4. Verification scope

The author independently read the complete acceleration and flow-box
notes through EOF and reconstructed their equations. This is a
written-proof audit, not a fresh full read of the cited source paper.
The scalar-filter checker remains a different suite with three
different methods. No combined execution or extra method count is
being manufactured from repeated runs.

The final author run passed all three methods in 0.105 seconds, exit
zero, with complete output in tool chunk `ce16ad`. The checker SHA-256
is `acd5a30dcd28367dc43241bc71b9f41673539e7f87ac8fb2066da2c28983b2d8`.
No test failed. The complete checker and scope note were read through
EOF by the author and whitespace checked. Root owns any canonical
runner or capture. No frozen file, shared
metadata or full regression is part of this bounded task. No human
expert review, formal proof certification or historical novelty
verification is claimed.
