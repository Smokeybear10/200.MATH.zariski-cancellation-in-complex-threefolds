# Explicit shear in the quadratic power-law branch

Subsequent closure: the higher cases outside this shear are now handled
under the slice hypothesis by
[the rational-rescale proof](height-nine-rational-rescale-pass.md).

The \(m=2\) power-law residual in
[height-nine-zero-top-pass.md](height-nine-zero-top-pass.md) closes by an
explicit polynomial coordinate shear. This does not require excluding
the residual by coefficient primitivity, and it preserves the three good
coordinate partials. The higher power-law degrees \(m=3,4\) are not
settled by this argument.

Let \(E\) be a slice LND on \(B=\mathbb C[x_1,x_2,x_3,x_4]\), and let
\(T_i=\partial_{x_i}\). Assume
\[
\operatorname{ad}_E^2(T_i)=0\ (i\le3),\qquad
\operatorname{ad}_E^3(T_4)=0,
\]
and the quadratic power-law equations
\[
E^2(x)=c g^2,\qquad E(x_4)=\lambda g,\qquad E(g)=0,
\quad c\in\mathbb C^4\setminus\{0\},\quad c_4=0,
\quad\lambda\in\mathbb C^*.
\tag{1}
\]
Here \(g\) may be nonconstant. Put \(P=E(x)\), \(J=\operatorname{Jac}P\),
\(V=\operatorname{ad}_E^2(T_4)\), and \(v=V(x)\).

## 1. Polynomial shear and exact inverse

Define
\[
y_i=x_i-\frac{c_i}{2\lambda^2}x_4^2\quad(1\le i\le4).
\tag{2}
\]
Since \(c_4=0\), one has \(y_4=x_4\), and the inverse is
\[
x_i=y_i+\frac{c_i}{2\lambda^2}y_4^2.
\]
Thus this is an actual polynomial coordinate change, not just a
replacement of vector fields.

Using \(E(x_4)=\lambda g\) and \(E(g)=0\), one has
\(E^2(x_4^2)=2\lambda^2g^2\). Therefore
\[
E^2(y_i)=c_ig^2-
\frac{c_i}{2\lambda^2}2\lambda^2g^2=0
\]
for every coordinate. The derivation is nice in the new frame.
For \(i\le3\), \(\partial_{y_i}=\partial_{x_i}\), because the shear
depends only on \(x_4\). Hence those three partials retain their
double-bracket identities. The nice-subcase theorem from
[height-nine-first-pass.md](height-nine-first-pass.md) already closes
the kernel at this point.

## 2. The fourth partial also becomes good

There is a direct verification that the new frame satisfies all four
double-bracket identities. Put \(A=c\cdot\partial_x\). Since
\(c_4=0\), \(A\) is a constant combination of the three good partials,
so \(\operatorname{ad}_E^2(A)=0\).

The uniform highest-coefficient identity gives
\[
J(cg^2)=\frac12\lambda g v,
\quad\text{hence}\quad 2gJc=\lambda v.
\tag{3}
\]
This last polynomial identity is the safe form of the calculation; it
does not divide a polynomial coefficient by \(g\).
The new fourth partial is
\[
T'_4=\partial_{y_4}
=T_4+\frac{x_4}{\lambda^2}A.
\]
The product rule for iterated commutators yields
\[
\operatorname{ad}_E^2(x_4 A)
=E^2(x_4)A+2E(x_4)[E,A]
+x_4\operatorname{ad}_E^2(A)
=-2\lambda g\,(Jc)\cdot\partial_x.
\]
By (3), this is \(-\lambda^2V\). Consequently
\[
\operatorname{ad}_E^2(T'_4)=V-V=0.
\tag{4}
\]
All new partials commute because they are the partials of the explicit
coordinate system (2). There is no missing frame-integrability check.
The height-eight theorem therefore gives an ambient invariant
coordinate. Since \(E\) has a slice, regular-kernel recognition gives
\(\ker E\cong\mathbb C^{[3]}\).

## 3. Primitive slice control

Use physical coordinates \((a,d,z,w)\), and set
\[
g=d-a^2/2,\qquad E=g(\partial_a+a\partial_d)+\partial_z.
\]
The frame
\[
(x_1,x_2,x_3,x_4)=(d-z-w,z,w,a)
\]
has the exact filtration profile \((1,1,1,2)\) for the slice \(z\).
In this frame \(c=(1,0,0,0)\), \(\lambda=1\), and (2) is simply
\[
y_1=x_1-x_4^2/2=g-z-w,\qquad y_2=z,\quad y_3=w,\quad y_4=a.
\]
Now \(g=y_1+y_2+y_3\), and the new coefficient vector is
\[
E(y)=(-1,1,0,g).
\]
Every generator image is invariant, and the new coefficient Jacobian
has square zero. Thus this genuine primitive slice example exhibits the
claimed repair explicitly. It does not require a common coefficient
factor or a free highest-iterate field.

## 4. Boundary of this shear

The exponent two in (2) is matched to
\(E(x_4)=\lambda g\) and \(E^2(x)=cg^2\). In the cubic branch one
only knows \(E^2(x_4)=\lambda g^2\), and in the quartic branch one
only knows \(E^3(x_4)=\lambda g^3\). The same shear cannot be applied
there without further identities. The justified consequence of this
pass is closure of \(m=2\), leaving \(m=3,4\) for separate work.
