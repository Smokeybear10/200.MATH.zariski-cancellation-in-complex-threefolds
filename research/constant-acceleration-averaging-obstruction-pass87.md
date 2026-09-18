# Averaging the actual coordinate partial need not preserve local nilpotence

The Reynolds average fails even when the quadratic coordinate has
nonzero constant acceleration and the derivation being averaged is
its actual coordinate partial. The construction below reuses the
SL2 coordinate change in Section 5 of the retained
[monic quadratic note](quartic-quadratic-variable-pass.md), with its
inessential fourth-power term removed. It is not a new family or a
counterexample to recognition. The point is to verify all the original
coordinate and constant-acceleration hypotheses simultaneously.

## 1. Two explicit polynomial coordinate systems

Start in canonical polynomial coordinates and set
\[
B=\mathbb C[u,x,y,c],\qquad E=\partial_u,
\qquad A=\ker E=\mathbb C[x,y,c],\qquad
z=x+u^2,\qquad E(z)=2u,\qquad E^2(z)=2.
\tag{1}
\]
The variables (z,u,y,c) also form polynomial coordinates, with
x=z-u squared. Make the following determinant-one change in the
pair (u,y), over C[z]:
\[
\begin{gathered}
a=(1+z^2)u-zy,\qquad b=-zu+y,\\
u=a+zb,\qquad y=za+(1+z^2)b,\qquad
x=z-(a+zb)^2.
\end{gathered}
\tag{2}
\]
The last line, together with the unchanged c, is a polynomial inverse
from (z,a,b,c) to (u,x,y,c). Substitution in either direction verifies
every coordinate. Consequently (z,a,b,c) is an actual original
four-coordinate frame. In this frame E is still a globally sliced
LND, with the polynomial slice u=a+zb. The E-degrees of these four
coordinates are respectively (2,5,3,0). Thus this example concerns
the one-quadratic-coordinate scope, not an asserted three-nice,
one-quadratic frame.

Let T be the actual partial with T(z)=1 and T(a)=T(b)=T(c)=0.
Differentiating the inverse (2) proves its expression in the
intermediate coordinates (z,u,y,c):
\[
T=\partial_z+(-zu+y)\partial_u
       +\bigl((1-z^2)u+zy\bigr)\partial_y,
\qquad T(c)=0.
\tag{3}
\]
Here the partial symbols in the displayed formula refer to that
intermediate coordinate system. In particular T is locally nilpotent
because it is the actual partial with respect to z in (z,a,b,c),
not because an abstract vector-field expression has been declared
locally nilpotent. For example T(u)=b, T squared(u)=0, and
T cubed kills each of u,x,y,c.

## 2. The exact average and its infinite sequence of nonzero iterates

Use the involution iota of the
[constant-acceleration reduction](constant-acceleration-involution-boundary-pass87.md):
it fixes x,y,c and negates u. Equivalently it fixes z,y,c and
negates u in the intermediate chart. Conjugating the actual T in
(3) and averaging gives
\[
V:=\frac{T+\iota T\iota}{2}
 =\partial_z-zu\partial_u+zy\partial_y,
\qquad V(z)=1,\qquad V\iota=\iota V.
\tag{4}
\]
The signs in the u component include the sign from applying T to
iota(u), not just substitution into the coefficient of partial_u.
In canonical coordinates the components of V are
(-zu, 1+2zu squared, zy, 0), where z=x+u squared.

For every integer n at least zero,
\[
V^n(y)=P_n(z)y,\qquad
P_0(t)=1,\qquad P_{n+1}(t)=P_n'(t)+tP_n(t),
\qquad \deg P_n=n,\quad \operatorname{lc}(P_n)=1.
\tag{5}
\]
The recurrence follows from V(z)=1 and V(y)=zy. The degree and
leading-coefficient assertions follow by induction: the product
t P_n has degree n+1 and leading coefficient one, whereas the
derivative has lower degree. Hence no iterate V to the n of y is
zero. This proves that V is not locally nilpotent. It also follows
from the nonzero self-divisibility V(u)=-zu: a characteristic-zero
LND on a domain cannot send a nonzero element into its own principal
ideal nontrivially, by additivity of LND-degree.

The failure remains visible on the fixed hypersurface. Since V(u)
is divisible by u, it descends modulo (u) to a derivation of A:
\[
\overline V=\partial_x+xy\partial_y,
\qquad \overline V(x)=1,
\qquad \overline V\text{ is not locally nilpotent}.
\tag{6}
\]
Here r=z-u squared=x is the critical-value function. Thus evaluation
at the critical section can produce a splitting derivation for dr
without producing an LND, even globally and with q=2 a unit. This
does not contradict the existence of a different equivariant LND:
the canonical partial partial_x fixes u,y,c, commutes with iota,
and sends z to one. The original kernel A is already polynomial.
Moreover every z-fiber has coordinates (u,y,c), in which its
involution is already a linear reflection. Averaging the specified
original partial nevertheless fails.

## 3. Exact finite verification and provenance

The standalone
[one-method checker](constant_acceleration_average_checks_pass87.py)
uses unittest and SymPy only. It checks both polynomial inverse
orders, both constant Jacobian determinants, the actual E-transport
and slice, all four stated E-degrees, the inverse-derived original
partial T, its coordinate values and bounded iterates, the conjugation
signs, V(z)=1, equivariance, the quotient derivation, and six exact
instances of (5). The all-n obstruction is the written degree
induction, not a conclusion extrapolated from those six instances.
No prior checker or solver code is imported.

The first author run passed the single method in 0.152 seconds,
exit zero, with complete tool output in chunk a0988d. The checker
SHA-256 is
f9259e459b3d933336055355c0f005290e74deea1e5b4ac722060d55a516dbfc.
The author then read the entire saved checker and proof through EOF.
No mathematical assertion failed, and no additional suite or full
regression was run. This note and checker are separate new pass87
artifacts. The preceding pass87 involution note and every file through
pass86 are unchanged. Root owns any canonical capture and integration.
