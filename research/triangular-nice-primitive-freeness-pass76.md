# Primitive derived fields in a linearly triangular nice frame

Let E be a nice, sliced locally nilpotent derivation of a polynomial
four-ring over C. Suppose E is triangular in some actual affine-linear
coordinate frame. Then every constant good direction T for which
Q=[T,E] is independent of E has the following property: the primitive
part of Q restricted to ker E has a polynomial slice. In particular
its intrinsic fixed-locus ideal is the unit ideal.

The conclusion concerns this additional linear-triangularity hypothesis.
It is not assumed for arbitrary nice actions, and the statement does
not extend to an arbitrary nonlinear triangularization that sends T
to a nonconstant vector field. It rules out another construction route
for the primitive fixed-point target, not that target in general.

## 1. Hypotheses and the exact object being divided

Work in B=C[x1,x2,x3,x4]. After an actual affine-linear change,
assume
\[
\begin{aligned}
Ex_1&=c\in C,& Ex_2&=f(x_1),\\
Ex_3&=g(x_1,x_2),& Ex_4&=h(x_1,x_2,x_3),\\
E^2x_i&=0,& Es_*&=1\quad(s_*\in B).
\end{aligned}
\tag{1}
\]
Let T be any constant vector field in this same affine-linear
frame, and assume ad_E^2(T)=0. Set A=ker E and Q=[T,E].
The good-direction identity gives [E,Q]=0. We assume Q and E
are independent over Frac B, equivalently d=Q|A is nonzero.
Indeed, B=A[s_*]; if d=0, then Q=(Qs_*)E with Qs_* in A.

We will construct polynomial coordinates for A in every case.
In those coordinates let h_d be a greatest common divisor of
the values of d on the coordinate generators. Its primitive part
is D=d/h_d, up to a nonzero constant. The proof will give an
actual element of A on which D has value one. Thus it establishes
the unit ideal, not only absence of a common divisor.

Writing P=(Ex_i), niceness and constancy of T imply
\[
Qx_i=T(P_i),\qquad E(Qx_i)+Q(P_i)=0,
\qquad [E,Q]x_i=2E(Qx_i).
\tag{2}
\]
We will use (2) to test goodness by applying E to the displayed
coefficients of Q. No equivalence between a fraction-field rank
bound and a constant good direction is used.

## 2. Two elementary translation cases

### 2.1. A translation row over the polynomial line

Suppose, in actual affine-linear coordinates (a,y1,y2,y3), that
\[
E=p_1(a)\partial_{y_1}+p_2(a)\partial_{y_2}
  +p_3(a)\partial_{y_3},\qquad Ea=0.
\tag{3}
\]
The supplied slice forces (p1,p2,p3)=C[a]. To see this directly,
evaluate Es_*=1 at y1=y2=y3=0; its three partial derivatives
there supply a polynomial Bezout identity in a.

There is an actual invertible matrix M(a) over C[a] taking this
column of speeds to (1,0,0). This can be constructed by the
ordinary Euclidean algorithm, not by a coordinate-recognition
assumption. For two nonzero entries p,q with gcd r and Ap+Bq=r,
the matrix with rows (A,B) and (-q/r,p/r) has determinant one
and sends (p,q) to (r,0). Embed this operation in three variables,
combine with the third entry, and normalize the final unit.
Zero entries are handled by a coordinate permutation. Both M
and M^{-1} have polynomial entries.

The resulting actual coordinates (a,S,Y,Z) give E=partial_S
and A=C[a,Y,Z]. A constant T has a constant a-component t_a,
so its original derived coefficients are t_a p_i'(a). Since
Qa=0, applying Q to the new coordinates just multiplies this
column by M(a). Therefore
\[
d=q_1(a)\partial_Y+q_2(a)\partial_Z.
\tag{4}
\]
At least one qi is nonzero by the independence hypothesis.
After dividing by their gcd, the two coefficients generate the
unit ideal of the PID C[a]. A Bezout combination of Y and Z
is an actual polynomial slice for D. This includes the case
where just one coefficient is nonzero.

### 2.2. Two translation directions over an invariant plane

Suppose instead, in actual affine-linear coordinates (a,b,y,z),
that
\[
E=p(a,b)\partial_y+q(a,b)\partial_z,
\qquad Ea=Eb=0.
\tag{5}
\]
Evaluation of the supplied slice equation at y=z=0 gives
alpha p+beta q=1 with alpha,beta in R=C[a,b]. Thus the
following are actual polynomial coordinates and inverse formulas:
\[
\begin{aligned}
S&=\alpha y+\beta z,& V&=pz-qy,\\
y&=pS-\beta V,& z&=qS+\alpha V.
\end{aligned}
\qquad E=\partial_S,\quad A=R[V].
\tag{6}
\]
Both inverse orders follow by substitution and alpha p+beta q=1.
For a constant T let delta be its restriction to the base plane.
Then Q fixes a,b and has coefficients (delta p,delta q) along
(y,z). Applying Q to V gives
d=(p delta q-q delta p)partial_V. The coefficient is nonzero
when E,Q are independent. Since this is the only nonzero
coordinate value of d, its primitive division is partial_V,
with polynomial slice V. No coprime-to-Bezout inference over
the two-variable ring R is needed: the Bezout identity above
came from the original supplied slice.

## 3. The branch with an actual linear slice

Suppose c in (1) is nonzero. Niceness of x2 gives cf'=0,
so f is constant. An actual affine-linear change gives
s=x1/c and a=x2-fs, with Es=1 and Ea=0. Retain y=x3,z=x4.
Niceness of y implies its velocity is a polynomial g(a).
The lower three-variable invariant ring is then C[a,j], where
j=y-g(a)s: the actual inverse is y=j+g(a)s.
Niceness of z consequently gives the exact form
\[
E=\partial_s+g(a)\partial_y+h(a,j)\partial_z,
\qquad j=y-g(a)s.
\tag{7}
\]
For later use the full actual translation coordinates are
(a,j,k,s), with k=z-s h(a,j); their inverse is
y=j+g(a)s, z=k+s h(a,j). Hence A=C[a,j,k].

The preceding changes from (x1,x2,x3,x4) to (s,a,y,z) were
affine-linear, so T still has constant components
(t_s,t_a,t_y,t_z). Its coefficients from (2) are
\[
\begin{aligned}
Qs&=Qa=0,& Qy&=t_a g',\\
Qz&=t_a h_a+(t_y-t_sg-t_asg')h_j,&
E(Qz)&=-t_a g'h_j.
\end{aligned}
\tag{8}
\]
Here h_a holds j fixed. The other coefficients of Q are
E-invariant, so goodness forces t_a g'h_j=0 in the actual
polynomial domain.

If g' and h_j are both nonzero, t_a=0. Equation (8) then
shows that Q fixes a and j, and
\[
d=(t_y-t_sg)h_j\partial_k
\quad\text{on }A=C[a,j,k].
\tag{9}
\]
Its nonzero coefficient is its exact content; the primitive
division is partial_k with slice k.

If g'=0, the coordinate j=y-gs is affine-linear. In the
affine-linear frame (a,j,s,z), E is the two-direction
translation (5) with speeds 1 and h(a,j). All hypotheses
of Section 2.2, including constancy of T, therefore hold.
If h_j=0, equation (7) is a translation row over C[a]
with speeds (1,g(a),h(a)); Section 2.1 applies. These cases
are exhaustive, including all overlaps and zero derivatives.

## 4. The branch with a nonzero first polynomial speed

Now let c=0 and f in (1) be nonzero. Write a=x1, y=x2,
z=x3 and w=x4. Niceness of z says f g_y=0, hence g=g(a).
Let
\[
\rho=\gcd(f,g),\quad F=f/\rho,\quad G=g/\rho,
\quad rF+sG=1,\qquad
U=ry+sz,\quad I=Gy-Fz.
\tag{10}
\]
Here rho is nonzero, may be a nonunit, and F,G generate
the unit ideal in C[a]. Both zero and nonzero g are allowed.
The exact inverse is y=FU+sI, z=GU-rI. It gives
E U=rho and E I=0. Since the ring is a domain of
characteristic zero, the lower invariant ring is exactly
C[a,I]. Thus niceness of w yields h=h(a,I), and
\[
B=C[a,I,U,w],\qquad
E=\rho(a)\partial_U+h(a,I)\partial_w.
\tag{11}
\]
The supplied slice, expressed in these actual coordinates and
evaluated at U=w=0, gives alpha rho+beta h=1 in C[a,I].
The maps
\[
\begin{aligned}
S&=\alpha U+\beta w,& V&=\rho w-hU,\\
U&=\rho S-\beta V,& w&=hS+\alpha V
\end{aligned}
\tag{12}
\]
are actual polynomial inverse formulas over C[a,I]. In
particular A=C[a,I,V]. This proves the required coordinates
even where rho vanishes. It does not replace rho by a unit
or assert that the original bad-speed pair is coprime.

We now compute Q while T is still written in the original
affine-linear frame (a,y,z,w), with constant components
(t_a,t_y,t_z,t_w). Define W=F'G-FG'. Since
E(I_a)=G'f-F'g=-rho W, differentiation of the original
velocity h(a,I) gives
\[
\begin{aligned}
Qa&=0,& Qy&=t_a f',& Qz&=t_a g',\\
Qw&=t_a(h_a+h_I I_a)+(t_yG-t_zF)h_I,&
E(Qw)&=-t_a\rho W h_I.
\end{aligned}
\tag{13}
\]
All other coefficients are E-invariant. Hence goodness forces
t_a rho W h_I=0. This computation does not treat the
base-dependent coordinates U,I as constant directions.

If W and h_I are nonzero, then t_a=0. The resulting Q
fixes a,y,z and therefore fixes I and U. Equations (12)--(13)
give its exact intrinsic value
\[
d=\rho(t_yG-t_zF)h_I\partial_V
\quad\text{on }A=C[a,I,V].
\tag{14}
\]
Again its primitive part is partial_V. Independence ensures
that the displayed coefficient is not zero.

If h_I=0, all three speeds f,g,h lie in C[a], so
Section 2.1 applies in the original affine-linear frame.
If W=0, coprimality forces F and G to be constant:
when both are nonzero their rational quotient has zero
derivative and so is constant, and a proportional coprime
polynomial pair is a constant pair. The same conclusion
holds if one component is zero. We can then choose r,s
constant in (10); thus U,I are affine-linear coordinates.
Equation (11) is exactly the two-direction translation
of Section 2.2 with invariant plane (a,I). In particular
T is still constant in that frame. These branches exhaust
every possibility in (13).

## 5. The remaining zero-speed cases

Finally suppose c=f=0 in (1). Then a=x1 and b=x2
are invariant. If g(a,b) is nonzero, niceness of x4
forces h_x3=0. Consequently
E=g(a,b)partial_x3+h(a,b)partial_x4, exactly (5).
The original slice again gives its unimodular row and
the explicit primitive division of Section 2.2.

If g=0 as well, E=h(a,b,x3)partial_x4. Its coefficient
ideal is hB. The supplied slice makes this the unit
ideal, so h is a nonzero complex constant. E is a
constant vector field, and every constant T commutes
with it. Thus Q=0 and this case is excluded by the
independence premise, not left as an exception.

## 6. Exact scope of the construction exclusion

The cases above prove the stated result for every actual
linearly triangular nice sliced four-variable action and
every constant good direction with independent derived field.
For every supplied E-slice, the intrinsic restriction d
is the same derivation of A. Primitive division and its
fixed-locus ideal are therefore unchanged by choosing another
slice. Equivalently, the slice-independent wedge-ideal test
from [pass75](primitive-good-quotient-scope-pass75.md) succeeds:
\[
(J_{E\wedge Q}:h_d)=B.
\tag{15}
\]
The content h_d here also equals the gcd of the original
wedge coefficients up to a constant, by that exact intrinsic
ideal comparison. Equation (15) uses a single colon, not
infinite saturation.

The distinction from the separate
[triangular-pencil theorem](triangular-nice-pencil-classification-pass76.md)
is important. That theorem starts with a particular triangular
auxiliary field T and asks whether a simultaneous T-partial,
nice-E frame exists. Here E itself is assumed linearly
triangular in the already supplied nice frame, and the
constant good direction is arbitrary. Neither proof assumes
this additional structure for every nice sliced action.

In particular a desired countercontrol with proper primitive
ideal must use a nice action that is not linearly triangularizable.
The conic family of pass75 provides such nontriangular examples
but still has primitive coordinate slices. Indeed its nonconstant
members have G1=0, whereas every triangular frame (1) has the
commuting last partial partial_x4 in G1; an affine-linear change
preserves the dimension of that constant space. Its direct
[two-invariant extension](two-invariant-conic-inverse-obstruction-pass76.md)
also does not produce the countercontrol. Existence or
nonexistence outside these constructions remains unresolved.

Every coordinate, slice and gcd step used here was proved
explicitly. No new external classification theorem, numerical
suite, full regression, historical novelty, human review or
formal proof-assistant verification is claimed. The complete
saved proof was author-read through EOF. Frozen passes through75
and shared metadata are unchanged.
