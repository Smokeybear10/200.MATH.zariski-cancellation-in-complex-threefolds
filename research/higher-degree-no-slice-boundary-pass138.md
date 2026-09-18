# Arbitrarily high last-coordinate degree without a slice

The actual conical example137 extends to every last-coordinate time
degree at least three by a single elementary shear. The good speeds,
their nonlinear rank-two cone, and the proper derivative ideal stay
unchanged. Thus increasing the allowed last-coordinate degree does not
remove the need for the slice hypothesis.

This is an explicit omitted-hypothesis boundary. Its kernel is already
polynomial, so it is not a cancellation counterexample.

## 1. An actual polynomial family and its inverse

Use the polynomial ring \(B=\mathbb C[x,\tau,\xi,v]\) and the
coordinates from the no-slice example137.[^1]
For any integer \(\ell\ge3\), put
\[
\begin{gathered}
X=x,\qquad Y=2v+\tau x,\qquad
Z=4\tau v+\xi+\tau^2x,\\
W=-\tau/2+vx+\tau x^2/2,\qquad
W_\ell=W+Y^\ell .
\end{gathered}
\tag{1}
\]
The last change is an elementary shear fixing \(X,Y,Z\), with inverse
\(W=W_\ell-Y^\ell\). Composing it with the exact137 inverse gives
\[
x=X,\qquad
\tau=XY-2(W_\ell-Y^\ell),\qquad
v=(Y-\tau X)/2,\qquad
\xi=Z-2\tau Y+\tau^2X .
\tag{2}
\]
Both orders of composition return the four generators, by first
undoing the shear and then using the137 inverse. These are polynomial
identities on the whole affine space, not rational or principal-open
inverses.

## 2. Exact time degree and the missing slice

Let \(E=\xi\partial_x\), fixing \(\tau,\xi,v\).
It is locally nilpotent because it lowers \(x\)-degree. The good speeds
and last-coordinate degree are
\[
\begin{gathered}
(EX,EY,EZ)=(\xi,\xi\tau,\xi\tau^2),\qquad
E^2X=E^2Y=E^2Z=0,\\
E^\ell W_\ell=\ell!\,\xi^\ell\tau^\ell\ne0,\qquad
E^{\ell+1}W_\ell=0 .
\end{gathered}
\tag{3}
\]
For the last line, the old \(W\) has time degree two and
\(E(Y)=\xi\tau\) is invariant. Thus only \(Y^\ell\) contributes
to its \(\ell\)-th derivative.
The speed field remains \(\mathbb C(\xi,\tau)\), with irreducible
homogeneous relation \(SR-T^2\) and no homogeneous linear relation.

Every derivative is divisible by the nonunit coordinate \(\xi\), and
\(EX=\xi\). Consequently
\[
(E(B))B=(\xi)\ne B,\qquad
\ker E=\mathbb C[\tau,\xi,v].
\tag{4}
\]
In particular no polynomial slice exists. The higher-degree shears
have not changed this ideal or the action.

## 3. Invariant correction and the same selected partial

There is an actual invariant coordinate even in this nonsliced family:
\[
\begin{gathered}
I=W_\ell-Y^\ell-\tfrac12XY=-\tfrac12\tau,\qquad
B=\mathbb C[I,X,Y,Z],\\
T_\ell=\partial_{W_\ell}\big|_{X,Y,Z}
      =-2\partial_\tau+8v\partial_\xi+x\partial_v .
\end{gathered}
\tag{5}
\]
The first inverse is \(W_\ell=I+Y^\ell+XY/2\).
For the second identity, the bad shear fixes the goods, so the
original partial in the new bad coordinate equals the old partial.
It kills \(Y^\ell\), hence has value one on \(W_\ell\).

The primitive speed row over \(\mathbb C[I]\) still has the nonunit
common factor \(\xi\). Thus the slice-dependent unit argument cannot
be replaced merely by existence of the invariant coordinate.
The coefficient of \(x\) in \(T_\ell\) on
\(\mathbb C[\tau,\xi,v]\) is \(\partial_v\), while
\(T_\ell(\xi)=8v\notin\mathbb C(\tau,\xi)\), just as in137.

## Verification and scope

The [independent exact checker138](all_degree_conical_controls_pass138.py)
contains finite controls at \(\ell=3,4,5\), including both inverse
orders, the Jacobian, exact derivative degrees, invariant correction
and selected partial. The proof for arbitrary \(\ell\) is the
elementary composition and derivative calculation above, not an
inference from those finite cases.

The other methods in that checker use formal determinant or coefficient
data. They are separate from this actual polynomial family and do not
certify the universal all-degree theorem or its field dependencies.
This note is a direct extension of137, not a historical novelty claim.

## Sources

[^1]: [Conical no-slice boundary137](conical-no-slice-boundary-pass137.md),
    Sections 1–4: the actual polynomial coordinates, both inverse orders,
    derivative ideal and selected partial. The new step here is the
    elementary shear in (1); no fresh external source audit is claimed.
