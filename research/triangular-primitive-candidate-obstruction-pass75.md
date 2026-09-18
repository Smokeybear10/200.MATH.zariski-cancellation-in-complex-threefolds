# A triangular primitive candidate admits no compatible nice frame

The following concrete commuting-field construction has a primitive
intrinsic fixed line. Nevertheless no polynomial coordinate frame in
which its selected field T is a coordinate partial can make E nice.
This rules out every T-preserving repair of this candidate, including
changes of the chosen T-slice. It is not a theorem that primitive
intrinsic fields arising from actual nice frames are always free.

The candidate and the request to test all T-preserving repairs were
supplied by Root. The full polynomial-coefficient obstruction below
is the bounded additional calculation. No new numerical suite or
historical novelty claim is made.

## 1. Two actual sliced actions, but not a common nice/partial frame

Work in the polynomial ring
\(R=\mathbb C[A,B,C,s]\), and set
\[
E=\partial_s,\qquad
T=\partial_A+sA\partial_B+2sB\partial_C.
\tag{1}
\]
The field E is nice in this displayed frame and has slice s.
The field T fixes s, is triangular and locally nilpotent, and has
slice A. Its bracket with E is
\[
Q=[T,E]=-A\partial_B-2B\partial_C=-d,\qquad
d=A\partial_B+2B\partial_C.
\tag{2}
\]
Both Q and d are triangular LNDs and commute with E. In particular
\(\operatorname{ad}_E^2T=0\). Their restriction to
\(\ker E=\mathbb C[A,B,C]\) is already primitive: the nonzero
coordinate coefficients A and 2B have gcd one. The intrinsic
fixed-locus ideal is
\[
(d(\mathbb C[A,B,C]))=(A,B),
\tag{3}
\]
whose zero set is the nonempty line A=B=0. As Qs=0, adjusting Q
to fix this supplied E-slice changes nothing, and primitive division
changes it at most by a nonzero constant. E and Q are generically
independent, while their wedge ideal is \((A,B)R\).

These facts do not yet give the desired nice/good-partial control:
T is not a constant coordinate partial in the displayed frame (1).
Although it becomes a coordinate partial in an actual polynomial
frame, we will show that E cannot be nice in any such frame.
The distinction concerns a simultaneous frame, not whether T alone
is a coordinate derivation.

## 2. An actual T-coordinate frame and both inverse orders

Define
\[
a=A,\qquad
b=B-\frac{sA^2}{2},\qquad
c=C-2sAB+\frac23s^2A^3,
\tag{4}
\]
and retain s. The proposed inverse is
\[
A=a,\qquad
B=b+\frac{sa^2}{2},\qquad
C=c+2sab+\frac13s^2a^3,
\tag{5}
\]
with s unchanged. Substituting (5) into the right side of (4)
returns a and b immediately, and the last coordinate becomes
\[
c+2sab+\frac13s^2a^3
-2sa\left(b+\frac{sa^2}{2}\right)
+\frac23s^2a^3=c.
\tag{6}
\]
Conversely, substituting (4) into (5) returns A and B, and its
last coordinate is
\[
C-2sAB+\frac23s^2A^3
+2sA\left(B-\frac{sA^2}{2}\right)
+\frac13s^2A^3=C.
\tag{7}
\]
Thus these are two-sided polynomial inverse maps. Direct application
of T gives Ta=1 and Ts=Tb=Tc=0, so
\[
R=\mathbb C[a,s,b,c],\qquad T=\partial_a,
\qquad \ker T=\mathbb C[s,b,c].
\tag{8}
\]
There is no assumed kernel theorem or implicit inverse in this step.

In this actual frame, E fixes a and has the exact expression
\[
E=\partial_s-\frac{a^2}{2}\partial_b
  +\left(-2ab+\frac{sa^3}{3}\right)\partial_c.
\tag{9}
\]
Indeed Ea=0, Es=1 and Eb=-a^2/2 follow directly from (4).
Also
\(Ec=-2AB+\tfrac43sA^3=-2ab+\tfrac13sa^3\).
In particular \(E^2c=\tfrac43a^3\ne0\), so this particular
T-coordinate frame is not nice. The next section rules out all
other T-coordinate frames, not just this displayed choice of c.

## 3. Every T-invariant nice polynomial

Let \(F\in\mathbb C[s,b,c]=\ker T\), with no restriction on its
degree. Subscripts below denote the actual partial derivatives in
s,b,c. Since Ea=0, expansion of (9) twice gives an identity in
the polynomial ring \(\mathbb C[s,b,c][a]\):
\[
\begin{aligned}
E^2F={}&
 \frac{s^2}{9}F_{cc}a^6
 -\frac{s}{3}F_{bc}a^5
 +\left(\frac14F_{bb}-\frac43bsF_{cc}\right)a^4\\
&+\left(2bF_{bc}+\frac23sF_{cs}+\frac43F_c\right)a^3
 +\left(4b^2F_{cc}-F_{bs}\right)a^2\\
&-4bF_{cs}a+F_{ss}.
\end{aligned}
\tag{10}
\]
All seven coefficients must vanish if E^2F=0. The coefficient of
a^6 first gives Fcc=0 because the coefficient ring is a domain.
The coefficient of a^5 then gives Fbc=0. The coefficients of a^4,
a^2 and a give, respectively, Fbb=0, Fbs=0 and Fcs=0.
Now the coefficient of a^3 gives Fc=0, and the constant coefficient
gives Fss=0. Consequently F is independent of c. Since Fbb=0 it
has the form p(s)b+q(s); Fbs=0 makes p constant, and Fss=0 makes
q affine in s. The converse follows directly from Es=1 and
E^2b=0. We have proved the exact vector-space equality
\[
\ker T\cap\ker E^2
=\mathbb C\oplus\mathbb Cs\oplus\mathbb Cb.
\tag{11}
\]
The argument compares coefficients of an arbitrary polynomial F.
It is not a finite-degree enumeration or an extrapolation from the
displayed coordinate c.

## 4. No alternative T-slice or T-invariant generators repair it

Suppose that \((t_0,t_1,t_2,t_3)\) were polynomial coordinates of
R with T=partial_(t0), and that E were nice in this same frame.
Then Tti=0 for i=1,2,3, and polynomial coordinate generation gives
\[
\ker T=\mathbb C[t_1,t_2,t_3].
\tag{12}
\]
Niceness also requires E^2ti=0. By (11), each of t1,t2,t3 lies in
\(\mathbb C+\mathbb Cs+\mathbb Cb\). Thus their generated algebra
lies in \(\mathbb C[s,b]\), which has transcendence degree two,
contradicting (8) and (12), whose transcendence degree is three.

This argument does not require t0=a. Every other T-slice is
\(a+H(s,b,c)\), because T(t0-a)=0. Changing that slice cannot
alter the necessary three T-invariant coordinate generators or
the equality (11). A nonzero constant rescaling of a coordinate
partial does not change its kernel and gives the same contradiction.
Hence even allowing alternative T-slices cannot produce a common
nice/partial frame.

## 5. Exact scope and verification record

The pair (1) has actual polynomial inverses, two global slices,
the required double-adjoint vanishing, and a primitive intrinsic
fixed line. What it lacks is precisely the simultaneous frame in
which E is nice and T is a coordinate partial. The full-degree
calculation (11) shows that this missing premise cannot be repaired
while retaining this T. Therefore this candidate cannot decide the
remaining [primitive quotient question](primitive-good-quotient-scope-pass75.md).

The result does not exclude other actual nice-frame candidates,
different choices of T, or more general constructions. It does
not prove general freeness of the primitive adjusted field, a
general coordinate-degree bound, or a cancellation theorem.

An inline exact SymPy differentiation independently expanded (10)
with an unspecified function F(s,b,c), returning its seven a-power
coefficients. The proof here instead supplies the complete actual
coordinate inverses and the all-polynomial coefficient argument.
There is no new standalone checker, test method, full-regression
execution, or claim of formal verification. The author read the
complete saved proof through EOF. Frozen passes through 74 and
shared metadata are unchanged.
