# A line-family construction criterion and an elementary-shear obstruction

No example with zero constant good-direction space is constructed here,
and existence of a constant good direction for every nice sliced action
is not proved. The bounded conclusions instead identify an exact
construction target and rule out a natural attempt to reach it from
the retained example.

For an actual affine slice, nice actions are exactly polynomially
invertible line families. Their constant good directions can be tested
on one actual three-dimensional slice by an explicit polynomial matrix.
For the familiar de Bondt specialization, every single elementary
coordinate shear preserving niceness retains a constant good direction.
Two elementary shears with different targets cannot conceal a nonnice
intermediate frame if the final frame is nice.

## 1. The exact affine-slice construction criterion

Work over \(\mathbb C\). Let \(E\) be a nice LND on the actual
polynomial ring \(B=\mathbb C[t,x_1,x_2,x_3]\), and suppose
\(Et=1\). This is an additional affine-coordinate-slice hypothesis,
not a consequence of an arbitrary supplied polynomial slice. Put
\[
H(y)=\bigl(Ex_1,Ex_2,Ex_3\bigr)(0,y),\qquad
K(y)=\operatorname{Jac}_yH.
\tag{1}
\]
Niceness means \(E^2(t,x)=0\), so the actual flow from the plane
\(t=0\) gives the polynomial map
\[
\Psi(t,y)=(t,y+tH(y)).
\tag{2}
\]
It is an actual polynomial automorphism: its inverse sends \((t,x)\)
to \((t,\pi_x(t,x))\), where
\(\pi=\exp(-tE)(t,x)\) is the original slice projection.
Both inverse orders follow by flowing back to \(t=0\).

Conversely, suppose a polynomial map \(H\in\mathbb C[y]^3\)
is given and (2) has a polynomial inverse over \(\mathbb C\).
Transport \(\partial_t\) through this actual inverse pair.
The resulting original-frame derivation is a polynomial LND, with
\(Et=1\), and its other coordinate images are
\(H(\pi_x(t,x))\). Since each coordinate of (2) is affine in
\(t\), this LND is nice. Thus the converse requires actual
polynomial invertibility of (2), not just its Jacobian determinant.

The determinant of the Jacobian of (2) is \(\det(I+tK)\).
It is a polynomial unit, and is one at \(t=0\). Consequently
\(K\) is nilpotent and \(K^3=0\). At \((t,x)=\Psi(t,y)\),
write the velocity and its original-frame Jacobian as \(P,J\).
Differentiating the actual inverse pair gives
\[
P(\Psi(t,y))=\binom{1}{H(y)},\qquad
J(\Psi(t,y))=
\begin{pmatrix}
0&0\\
-K(I+tK)^{-1}H&K(I+tK)^{-1}
\end{pmatrix}.
\tag{3}
\]
Here \((I+tK)^{-1}=I-tK+t^2K^2\) is a genuine polynomial
matrix. Squaring (3) and using \(K^3=0\) gives
\[
J^2(\Psi(t,y))=
\begin{pmatrix}0&0\\-K^2H&K^2\end{pmatrix}.
\tag{4}
\]
In particular the coefficient matrix is independent of flow time
when expressed in the actual invariant slice coordinates.

For a constant vector \((c,v)\in\mathbb C\oplus\mathbb C^3\),
the exact tests are therefore
\[
\begin{aligned}
G_1&=\{(c,v):K(v-cH)=0\},\\
G_2&=\{(c,v):K^2(v-cH)=0\}.
\end{aligned}
\tag{5}
\]
These are kernels over \(\mathbb C\) of the full polynomial
coefficient matrices, not kernels over \(\mathbb C(y)\).
The definitions agree with
[the pass74 nice-rank note](nice-slice-adjoint-rank-pass74.md):
\(G_1=\{v:Jv=0\}\) and \(G_2=\{v:J^2v=0\}\).
The nice adjoint identity \(\operatorname{ad}_E^2T_v=2J^2v\)
makes \(G_2\) the constant good-direction space.

Thus an explicit countercontrol with a linear slice and \(G_2=0\)
would result from an actual polynomial inverse for (2) together with
a trivial constant kernel of \([-K^2H\mid K^2]\).
Neither requirement is inferred here solely from \(K^3=0\)
or fraction-field rank one of \(K^2\). Nothing here asserts that
all nilpotent Jacobian matrices integrate to such polynomial inverses.

## 2. The retained seed and the exact single-shear question

Use the actual polynomial coordinates \((x,y,z,w)\) and set
\[
a=xz-y^2+w,\qquad
P=(1,a,a^2,b)^t,\qquad b=-xa^2+2ya-z,
\qquad E=P\cdot\partial.
\tag{6}
\]
This is the already retained de Bondt specialization from
[pass39](literature-scope-pass39.md), Section2, and
[the nice-route inventory](nice-route.md).
Its actual inverse coordinates and exact constant spaces were
rechecked in [pass74](nice-slice-adjoint-rank-pass74.md):
\[
(x,a,Y,Z)=(x,a,y-xa,z-xa^2),\qquad
G_1=0,\qquad G_2=\mathbb Ce_w.
\tag{7}
\]
In these coordinates \(E=\partial_x\). In particular it is a
completely recognized sliced action, not a candidate counterexample
to cancellation.

An elementary coordinate shear replaces one displayed coordinate
\(x_i\) by \(x_i+F\), where \(F\) is a polynomial in the other
three coordinates, and retains those other coordinates. Its inverse
is obtained by subtraction, so it is an actual automorphism for
every such \(F\). The new frame is nice exactly when \(E^2F=0\).
Since \(EP=0\), this last condition is the polynomial identity
\[
E^2F=P^t(\operatorname{Hess}F)P=0.
\tag{8}
\]

**Single-shear statement.** For (6), if \(F\) omits \(x\),
\(y\), or \(z\), respectively, equation (8) forces \(F\)
to be affine. If \(F\) omits \(w\), it forces
\[
F=L(x,y,z)+k(xz-y^2),\qquad \deg L\le1,
\qquad k\in\mathbb C,
\tag{9}
\]
In every case the new nice frame has a nonzero constant good direction.

The following coefficient proof does not impose a bound on
\(\deg F\).

### 2.1. A shear of \(w\)

Here \(F\in\mathbb C[x,y,z]\), while \(a\) is an independent
polynomial coordinate over that ring. Expanding (8) in powers of
\(a\) gives
\[
F_{xx}+2aF_{xy}+a^2(2F_{xz}+F_{yy})
 +2a^3F_{yz}+a^4F_{zz}=0.
\tag{10}
\]
Thus \(F_{xx}=F_{xy}=F_{yz}=F_{zz}=0\) and
\(F_{yy}=-2F_{xz}\). Integrating these elementary polynomial
identities gives exactly (9).

### 2.2. A shear of \(x\)

Let \(F\in\mathbb C[y,z,w]\). Work temporarily over
\(\mathbb C(y,z,w)\), where \(z\ne0\); this is only a
coefficient calculation, not a localization of the original action.
Substitution \(x=(a+y^2-w)/z\) makes \(a\) transcendental
over that field and gives
\[
b=-a^3/z+(w-y^2)a^2/z+2ya-z.
\tag{11}
\]
In
\(a^2F_{yy}+2a^3F_{yz}+2abF_{yw}
+a^4F_{zz}+2a^2bF_{zw}+b^2F_{ww}=0\),
the degree-six and degree-five coefficients give
\(F_{ww}=F_{zw}=0\). The degree-one coefficient then gives
\(F_{yw}=0\). The remaining coefficients give
\(F_{yy}=F_{yz}=F_{zz}=0\). The Hessian is zero, so
\(F\) is affine in \(y,z,w\).

### 2.3. A shear of \(y\)

Let \(F\in\mathbb C[x,z,w]\). Write
\(b=b_0+2ay\), where \(b_0=-xa^2-z\), and separate
the odd and even parts in \(y\). Since \(a=xz+w-y^2\),
it is transcendental over \(\mathbb C(x,z,w)\); comparison
of polynomials in \(a\) is legitimate.
After division of the odd part by the nonzero \(4ay\), it is
\[
F_{xw}-zF_{ww}+a^2(F_{zw}-xF_{ww})=0.
\tag{12}
\]
Consequently \(F_{xw}=zF_{ww}\) and \(F_{zw}=xF_{ww}\).
Put \(W=F_{ww}\). Substitution in the even part yields
\[
F_{xx}-z^2W
+a^2(2F_{xz}+2xzW+4wW)-4a^3W
+a^4(F_{zz}-x^2W)=0.
\tag{13}
\]
Its cubic coefficient gives \(W=0\), and all remaining
second derivatives of \(F\) then vanish. Thus \(F\) is affine.

### 2.4. A shear of \(z\)

Let \(F\in\mathbb C[x,y,w]\). Over \(\mathbb C(x,y,w)\),
substitute \(z=(a+y^2-w)/x\); then
\[
b=-xa^2+(2y-1/x)a+(w-y^2)/x.
\tag{14}
\]
Expanding
\(F_{xx}+2aF_{xy}+2bF_{xw}+a^2F_{yy}
+2abF_{yw}+b^2F_{ww}=0\), the fourth and third coefficients
give \(F_{ww}=F_{yw}=0\). The others give
\[
F_{yy}=2xF_{xw},\qquad
F_{xy}=-(2y-1/x)F_{xw},\qquad
F_{xx}=-2(w-y^2)F_{xw}/x.
\tag{15}
\]
The first two vanishing derivatives imply \(F_w=L(x)\).
Using the first identity in (15), write
\(F=wL(x)+xL'(x)y^2+M(x)y+N(x)\).
The second identity then gives
\(xL''+2L'=0\) and \(M'=L'/x\).
As \(L\) is polynomial in characteristic zero,
\(xL''+2L'=0\) forces \(L'=0\). Thus \(M'=0\),
and the last identity in (15) forces \(N''=0\).
Again \(F\) is affine.

## 3. The permitted shear retains a constant good direction

Affine frame changes preserve the dimensions of the constant spaces
\(G_1,G_2\). After removing the affine part of the only
nonlinear possibility (9), it remains to consider
\(w'=w+k(xz-y^2)\). In the resulting actual frame,
\[
a=w'+(1-k)(xz-y^2),\qquad
E(x,y,z,w')=(1,a,a^2,(1-k)b).
\tag{16}
\]
The velocity derivative along \(\partial_{w'}\) is
\((0,1,2a,(1-k)(-2ax+2y))\).
The original \(E\) kills all its components, since
\(Ea=0\), \(Ex=1\), and \(Ey=a\). Therefore
\(\operatorname{ad}_E^2\partial_{w'}=0\).
This proves the last assertion of the single-shear statement.
When \(k=1\), the coordinate \(w'=a\) is even invariant.

## 4. Two shears cannot hide a nonnice intermediate frame

The following observation applies to any original nice coordinate
frame, not only (6). Apply two elementary shears successively in
that fixed list of coordinate positions. If the targets are
different positions \(i\ne j\), the second shear leaves the
first changed coordinate unchanged. If the final frame is nice,
the second \(E\)-derivative of that first changed coordinate
must already vanish. All the other coordinates in the first
intermediate frame were original nice coordinates. Hence that
entire intermediate frame was nice.

If both shears target the same position, they depend on the same
three unchanged coordinates and their composition is one elementary
shear, obtained by adding the two shear polynomials. The preceding
single-shear statement applies to that composite for (6), even if
the intermediate frame was not nice.

This rules out the proposed two-elementary-shear construction that
would leave niceness temporarily and restore it at the end while
removing the good direction. It does not classify a second nice
shear after an arbitrary affine first change, longer sequences that
revisit coordinate positions, or other nonlinear automorphisms.
In particular it does not prove that the entire nice-preserving
coordinate orbit of (6) has \(G_2\ne0\).

## 5. Deduplication, verification, and the remaining question

The old nice-route and normalizer notes distinguish actual frames
from arbitrary centralizers and already recognize (6).
[The pass74 rank theorem](nice-slice-adjoint-rank-pass74.md)
proves \(J^3=0\) and \(\operatorname{rank}J\le2\) for
nice sliced four-variable actions, but does not produce a constant
element of \(\ker J^2\). The present contribution is the exact
line-family constant-kernel test and a proved obstruction to the
single-shear and nonnice-intermediate two-shear construction routes.
Neither supplies the missing constant direction in general.

The derivations and coefficient arguments above are written proofs,
not finite-degree searches. No new external classification theorem
is used: the seed's attribution is inherited, and each new claim is
proved here. No new reusable numerical method, full regression,
formal proof-assistant verification, or human expert audit is claimed.
All pass74-or-earlier files and shared metadata are unchanged.

The unresolved question is still whether an actual nice sliced
\(E\) on \(\mathbb C^{[4]}\) can have \(G_2=0\).
Even in the affine-slice construction (2), this note does not prove
that the constant kernel in (5) is nonzero or construct an actual
invertible line family for which it is zero.
