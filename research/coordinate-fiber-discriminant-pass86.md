# Coordinate fibers impose exact quadratic discriminant constraints

Every fiber of an original coordinate of quadratic slice degree embeds
the invariant base into an actual polynomial three-ring and gives a
quadratic extension of its fraction field. The field discriminant is therefore
nonsquare at every complex coordinate value. Primitivity of each
coordinate equation also constrains the common factor of the speed
and acceleration. On the reduced-denominator open set, the separate
critical-value theorem gives a smooth discriminant hypersurface.

These are necessary conditions, not a recognition theorem. In
particular, the raw field discriminant need not be squarefree: an
actual sliced polynomial frame with a repeated common factor provides
that boundary. All files through pass85 remain unchanged.

## 1. Retain the actual coordinate and invariant normalization

Let E be a locally nilpotent derivation of the actual polynomial
four-ring, with its original polynomial slice s. Assume only that
the original coordinate z has slice degree two. No degree bound on
the other three original coordinates is required. The normalization
from the [centered-return proof](rank-one-centered-return-quotient-pass85.md)
then gives
\[
\begin{gathered}
B=A[s]=\mathbb C[x_1,x_2,x_3,z],\quad A=\ker E,\quad E(s)=1,\\
b=E(z),\quad q=E^2(z)\ne0,\quad E(q)=0,\quad
g=\gcd(q,b),\quad h=q/g,\\
v=b/g-hs\in A,\quad w=z-bs+qs^2/2\in A,\quad
\gcd_A(h,v)=1,\\
z=w+gvs+(gh/2)s^2,\qquad g,h\ne0.
\end{gathered}
\tag{1}
\]
Here z is an original polynomial coordinate of B. The base A is
smooth and factorial, but it is not assumed to be a polynomial
three-ring. The slice gives its actual polynomial extension A[s].

For each complex number lambda put
\[
B_\lambda=B/(z-\lambda)B\simeq\mathbb C^{[3]},\qquad
F_\lambda(S)=\frac{gh}{2}S^2+gvS+w-\lambda\in A[S].
\tag{2}
\]
The polynomial F_lambda is the actual coordinate equation after the
slice presentation, not an unrelated relative polynomial.

## 2. The base embedding and nonsquare field discriminant

The map A to B_lambda is injective. Indeed, a nonzero element of A
has s-degree zero. If it equaled (z-lambda)f for a nonzero f in
A[s], degree additivity in the domain would give degree
2+deg_s(f)>0. Thus the intersection of A with (z-lambda)B is zero.

Let K=Frac(A). Since B_lambda is a domain and the localization at
A minus zero is nonzero, it follows that
\[
K\otimes_A B_\lambda\simeq K[S]/(F_\lambda(S))
\text{ is a field of degree two over }K.
\tag{3}
\]
In particular F_lambda remains irreducible over K. The embedding
part is an elementary degree fact: any nonconstant polynomial of
slice degree d gives zero intersection with A by the same argument,
and a coordinate fiber gives a degree-d domain extension. It is
not a new cancellation or descent theorem.

Define the normalized discriminant numerator L_lambda. The usual
quadratic discriminant is then
\[
L_\lambda=2h(w-\lambda)-gv^2,\qquad
\operatorname{disc}_S(F_\lambda)=-gL_\lambda,
\qquad -gL_\lambda\notin K^2
\quad(\lambda\in\mathbb C).
\tag{4}
\]
This follows from (3) in characteristic zero. In particular neither
L_lambda nor the discriminant is zero. A nonsquare in a field is
not the same assertion as a squarefree polynomial in A or A_h.

## 3. Primitivity and the smooth discriminant on D(h)

Because z-lambda is a coordinate polynomial, F_lambda is prime in
A[S]. If an irreducible p of A divided both g and w-lambda, it
would divide every coefficient of F_lambda. Dividing F_lambda by p
would leave positive S-degree, so this would factor the prime
F_lambda into two nonunits. Thus
\[
\gcd_A(g,w-\lambda)=1
\qquad\text{for every }\lambda\in\mathbb C.
\tag{5}
\]
Equivalently, on no irreducible component of g=0 is the restriction
of w identically a complex constant. This does not say that the
divisor g=0 is smooth, reduced, or disjoint from the fibers of w.
The common coefficient gcd of F_lambda is exactly the gcd in (5),
since gcd(h,v)=1.

The independently proved
[critical-value theorem](coordinate-critical-value-constraints-pass86.md)
applies to the same original coordinate and slice. On A_h it gives
r=w-gv squared/(2h) and an actual complex derivation D_* of A_h
with D_*(r)=1. No local nilpotence of D_* is asserted. Since
L_lambda=2h(r-lambda), one has
\[
\begin{gathered}
D_*(L_\lambda)\equiv2h\pmod{L_\lambda},\qquad
(L_\lambda,D_*(L_\lambda))A_h=A_h,\\
L_\lambda\text{ is squarefree in }A_h,
\qquad \gcd_{A_h}(g,L_\lambda)=1.
\end{gathered}
\tag{6}
\]
The unit ideal gives the smooth or empty hypersurface in D(h).
It also proves squarefreeness directly in the UFD A_h: an
irreducible square dividing L_lambda would divide both entries of
that unit ideal. For the last assertion, reduce L_lambda modulo any
common irreducible factor of g; the remaining expression is
2h(w-lambda), and h is a unit on this open set. Equation (5)
excludes that common factor.

With y=hs+v, the actual coordinate fiber has the presentation
\[
(B_\lambda)_h
\simeq A_h[y]/(g y^2+L_\lambda),\qquad
(B_\lambda)_{gh}
\simeq A_{gh}[y]/(y^2+L_\lambda/g).
\tag{7}
\]
The second is a free rank-two algebra over A_gh. The first need
not be finite over A_h. Finiteness on D(gh) does not establish
global finiteness, and no normalization claim is made for (7).
These rings come from actual coordinate fibers,
not from a presumed polynomial presentation of A.

## 4. A repeated common factor in an actual polynomial frame

The following variation of the
[retained triangular control](return-denominator-cancellation-control-pass85.md)
has a repeated common factor. In the actual ring C[a,x,c,z], set
\[
\begin{gathered}
f(a)=(a-1)^2,\qquad
E=a^2\partial_x+f(a)(1+ax)\partial_z,\\
V=f(a)(x+ax^2/2)-a^2z,\qquad
H_a(V)=V+a(2V-V^2/2),\qquad
\sigma=(x-H_a(V))/a^2.
\end{gathered}
\tag{8}
\]
This is a global polynomial slice with a polynomial coordinate
inverse, not a localization construction. Modulo a squared,
V=x+a(x squared/2-2x); the polynomial H is its two-sided inverse
modulo a squared. Thus sigma is polynomial, and the inverse map is
x=H_A(V)+A squared sigma and
z=[f(A)(x+A x squared/2)-V]/A squared, with a=A and c unchanged.
The same congruence makes the inverse quotient polynomial. The
formulas recover x, V and z in both composition orders.

Direct differentiation gives E(V)=0 and E(sigma)=1, while a and c
are fixed. These actual coordinate identities prove that E is
translation in sigma. Its good-speed ideal is the proper principal
ideal (a squared), and q=a cubed f(a). In its invariant ring
C[a,V,c], the normalized coefficients satisfy
\[
\begin{gathered}
g=f(a),\quad h=a^3,\quad v=1+aH_a(V),\quad
w=\frac{f(a)(H_a(V)+aH_a(V)^2/2)-V}{a^2},\\
w\big|_{a=1}=-V,\qquad
L_\lambda\big|_{a=1}=-2(V+\lambda).
\end{gathered}
\tag{9}
\]
The formula for w is polynomial by the same inverse congruence.
The original gcd is indeed f(a), since gcd(a cubed,1+ax)=1.
For every lambda the factor a-1 does not divide L_lambda, whereas
the raw discriminant -gL_lambda contains (a-1) squared. This gives
an actual failure of squarefreeness of that raw discriminant, even
on D(h), while retaining (4)--(6).

Here q already belongs to the speed ideal; no acceleration
membership counterexample is claimed. The repeated-g construction
is a bounded explicit control, not a historical novelty claim.
Any separate numerical verification is recorded with its checker,
not treated as an additional proof method here.

Geometry derived the all-coordinate-fiber field and primitivity
constraints and the repeated-factor control. Root highlighted the
discriminant interpretation and the distinction between a relative
finite cover and the actual coordinate fiber. Jet's separate
critical-value proof is the input to (6) and was read through EOF
before use. Root also noted that the proofs require only the
quadratic slice degree of z, not niceness of the other coordinates.
The speed-ideal conclusions of pass85 are not asserted in this
broader class. No new external source theorem, cancellation step,
kernel recognition or edit to the frozen passes is asserted.
