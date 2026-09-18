# An actual degree-lowering map in an affine-potential coupling sector

Working result: in the actual principal chart264, the additional
conditions \(k=s\), \(n=0\), and
\(\ell=\lambda t+\mu\), with \(\lambda,\mu\in\mathbb C\),
have an explicit resolution. If \(\lambda=0\), no such actual
frame exists. If \(\lambda\ne0\), a polynomial automorphism
produces three coordinates affine in the slice parameter. The
retained three-good theorem156 then recognizes the kernel.

This is a sufficient actual sector, not a normalization of arbitrary
\(k_s\ne0\) data. No existence claim for this sector is made.
The coordinate change is checked in the original four-ring, not
only over a coefficient field.

## 1. Precise actual entry and the full identities

Retain the actual setup, entire initial kernel, selected derivation,
exact fields, returns and calibrated determinant of the completely read
[264](principal-one-affine-paraboloid-chart-pass264-working.md):
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,
\quad A=\ker E,\quad\deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(X^2Z-Y^2),\quad a=EX\ne0,
\quad K=\operatorname{Frac}A=L(v),\quad Nv=1,\\
t,s\in L\text{ algebraically independent over }\mathbb C,
\qquad [L:\mathbb C(t,s)]<\infty .
\end{gathered}
\tag{1}
\]
All fixed-X coefficient expressions below lie in \(K[X]\).
Neither \(t,s\) nor an intrinsic line parameter is assumed to
be an ambient coordinate.

Assume exactly
\[
k=s,\qquad n=0,\qquad
\ell=\lambda t+\mu,\qquad\lambda,\mu\in\mathbb C.
\tag{2}
\]
In particular \(m=k_s=1\), so this is a nonzero-coupling sector.
The formal polynomial \(F\) in264 is zero: all second derivatives
of \(k=s\) and all first derivatives of \(n=0\) vanish.
The two literal potentials and the monic surface relation become
\[
\begin{aligned}
z&=2ty+\sigma^2+\theta,\\
w&=\lambda t+\mu-2\sigma y,\\
y^2-\lambda\sigma&=h_0,\qquad h_0\in L.
\end{aligned}
\tag{3}
\]
Indeed the surface polynomial in264 is
\(\mathcal H(U,P,V)=U^2-\lambda P\), not a plane relation
asserted from three-generator return.
The complete actual expressions remain
\[
\begin{aligned}
Y&=y+\sigma X+tX^2,\\
Z&=z+(2t\sigma+s)X+t^2X^2,\\
W&=w+\theta X+sX^2.
\end{aligned}
\tag{4}
\]

First make the actual triangular shear
\[
U_1=W-\mu-XZ,\qquad W=U_1+\mu+XZ,
\qquad R=Y^2+XU_1.
\tag{5}
\]
Here \((X,Y,Z,U_1)\) is a polynomial coordinate frame, whereas
\(R\) is only a polynomial, not an asserted coordinate.
Substitution of (3),(4) gives the exact full-X identity
\[
\boxed{R=y^2+\lambda tX.}
\tag{6}
\]
For an explicit coefficient check, before imposing (3) the
coefficients of \(X,X^2,X^3,X^4\) in (5) are respectively
\[
2y\sigma+w-\mu,\quad
\sigma^2+2ty+\theta-z,\quad
2t\sigma+s-(2t\sigma+s),\quad t^2-t^2.
\]
Thus (6) uses the entire expansion, not the initial relation as
an equality of original coordinates.

## 2. A constant potential is impossible

If \(\lambda=0\), (6) says \(y^2=R\in\mathcal B\).
The element \(y\in K\subset\operatorname{Frac}\mathcal B\)
is integral over \(\mathcal B\), being a root of \(T^2-R\).
The polynomial ring is integrally closed, so \(y\in\mathcal B\).

But, in the original independent coordinates,
\[
R=Y^2+X(W-\mu)-X^2Z
\]
has exact degree one in \(Z\) over \(\mathbb C[X,Y,W]\).
The square of a nonzero polynomial has even degree in \(Z\).
This contradicts \(R=y^2\). Hence no actual frame in (1),(2)
can have \(\lambda=0\).

The integrality step matters: a square in a fraction field is not
initially a polynomial square by definition. No claim about the
singularities of a projected curve enters this obstruction.

## 3. The nonzero slope gives an explicit polynomial automorphism

Suppose \(\lambda\in\mathbb C^*\). Fix \(X,Z\) and define
\[
\boxed{
V=Y-\frac{X R}{\lambda},\qquad
U_2=U_1+\frac{2YR}{\lambda}-\frac{X R^2}{\lambda^2}.}
\tag{7}
\]
Every denominator here is a nonzero complex scalar.
Direct multiplication gives the preserved quadratic polynomial
\[
V^2+XU_2=Y^2+XU_1=R.
\tag{8}
\]
Put \(R_*=V^2+XU_2\). The polynomial inverse is
\[
\boxed{
Y=V+\frac{XR_*}{\lambda},\quad
U_1=U_2-\frac{2VR_*}{\lambda}-\frac{X R_*^2}{\lambda^2},
\quad W=U_1+\mu+XZ.}
\tag{9}
\]
The preservation identity (8) verifies both compositions of
(5),(7),(9). In particular
\[
\mathcal B=\mathbb C[X,V,U_2,Z]
\tag{10}
\]
is an actual polynomial coordinate presentation. This map has
the usual quadratic-preserving triangular-exponential form;
no external automorphism classification is used to establish it.

Use (3),(4),(6) in the first equation of (7):
\[
\begin{aligned}
V&=y+\left(\sigma-\frac{y^2}{\lambda}\right)X
     +\left(t-\frac{\lambda t}{\lambda}\right)X^2\\
 &=y-\frac{h_0}{\lambda}X.
\end{aligned}
\tag{11}
\]
Then (8),(6) give
\[
\boxed{
U_2=\lambda t+\frac{2h_0y}{\lambda}
                       -\frac{h_0^2}{\lambda^2}X.}
\tag{12}
\]
To obtain (12), subtract the square of (11) from (6) and cancel
the nonzero element \(X\) in the domain \(K[X]\). Polynomiality
of \(U_2\) was already established by (7); this cancellation
is not used to declare an arbitrary quotient polynomial.

Since \(y,t,h_0\in K=\ker(E|_{\operatorname{Frac}\mathcal B})\)
and \(E^2X=0\), equations (11),(12) prove
\[
E^2X=E^2V=E^2U_2=0.
\tag{13}
\]
If \(h_0\ne0\), both new derivatives are nonzero:
\(EV=-ah_0/\lambda\) and
\(EU_2=-ah_0^2/\lambda^2\). The actual frame then has exact
time degrees1112, with \(Z\) still of degree two.
If \(h_0=0\), \(V\) and \(U_2\) are invariant actual coordinates.
More generally if \(h_0\in\mathbb C\), the complex shear
\(V+(h_0/\lambda)X\) is an invariant actual coordinate.
The proof does not assume this last coefficient is complex in
the general case.

## 4. Recognition and scope

The completely read retained
[three-good recognition theorem156](three-good-all-degree-recognition-pass156-working.md)
applies to (10),(13): the ring is the original globally sliced
complex polynomial four-ring, and three displayed actual
coordinates have zero second derivative. Therefore, subject to
that retained working theorem and its stated dependencies,
\[
\boxed{A\cong\mathbb C^{[3]}.}
\tag{14}
\]
In the special \(h_0\in\mathbb C\) case the explicit invariant
coordinate above instead permits the direct
[Bhatwadekar--Gupta--Lokhande Theorem3.5 endpoint](https://arxiv.org/html/1501.01438v1),
since the slice makes \(A\) affine and regular.

The new contribution is the actual automorphism with the full
degree reduction (11),(12). It uses only retained actual-chart
identities before the known working recognition endpoint.
It does not deduce a two-generator plane return from the
three-generator surface relation, and it requires neither the
degree-two projection case of290 nor \(Ny\ne0\).

Conditions (2) are extra hypotheses. No argument here transforms
an arbitrary \(k_s\ne0\) chart to them. The degree-lowering map
does not prove all1222 recognition, a bound on arbitrary coordinate
profiles, or unrestricted cancellation. No realized example of
(2), historical novelty, human-expert review, or proof-assistant
certification is claimed. The older dependencies of156 have not
been recursively rechecked in this note.

Finite raw-map checks and separate saved-source reviews are
recorded in the ledger after completion. No earlier proof or
completed checker is changed by this argument.
