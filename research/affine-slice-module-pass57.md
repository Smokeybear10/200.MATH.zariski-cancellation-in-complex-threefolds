# The finite module that detects actual affine generic slices

The actual determinant fields define a finite rank-three module of
affine generic functions. Over a closed-point local invariant base,
this module is free with a basis containing \(1\). The derivatives
of its other two basis elements generate an exact ideal whose
unitness is equivalent to existence of an actual affine generic
slice.

This replaces the radial sufficient condition by a direct
slice-selection condition. It does not prove that the ideal is
the unit ideal. The supplied slice may lie outside the finite
module, and no universal bound for its generic degree is inferred.

## 1. Actual frame and the degree-one module

Retain the entire supplied independent degree-two frame of
[the generic bad-pair theorem](generic-bad-pair-pass44.md).
Write
\[
B=\mathbb C[x_1,x_2,x_3,x_4]=A[s_*],\qquad Es_*=1,
\]
\[
C=\ker D\simeq\mathbb C^{[2]},\quad
R=C_{\mathfrak m},\quad L=\operatorname{Frac}R,\quad
\mathcal B=B_R,\quad\mathcal A=A_R.
\tag{1}
\]
Here \(D\) is the actual primitive intrinsic LND and
\(C\subset A\) is faithfully flat. The inherited identities are
\[
\mathcal B_L=L[x_3,x_4],\quad
x_i=\mathcal Q_i(x_3,x_4),\quad
\deg\mathcal Q_i\leq2\quad(i=1,2),
\]
\[
E=f\partial_{x_3}+g\partial_{x_4},\qquad
f,g,h_i=E^2x_i\in R,\qquad \mathcal B\cap L=R.
\tag{2}
\]
The four \(x_i\) are the actual original polynomial coordinates,
not four abstract generators substituted into a generic model.

There are actual \(R\)-derivations with
\[
K_3=-\Delta\partial_{x_4},\qquad
K_4=\Delta\partial_{x_3},\qquad 0\ne\Delta\in R.
\tag{3}
\]
Define the actual \(R\)-submodule
\[
V=\mathcal B\cap L[x_3,x_4]_{\leq1}.
\tag{4}
\]
The subscript is total degree in the actual generic bad pair.
It is not the intrinsic \(D\)-degree of arbitrary elements of
\(\mathcal B\).

Since \(K_3,K_4\) kill \(\Delta\) and commute, characteristic
zero gives the exact description
\[
V=\ker K_3^2\cap\ker(K_3K_4)\cap\ker K_4^2
\quad\hbox{inside }\mathcal B.
\tag{5}
\]
Indeed the three operators are nonzero scalar multiples of
the three second partial derivatives on the generic polynomial
plane. Their simultaneous kernel is exactly its affine-linear
part. Injectivity into \(\mathcal B_L\) gives (5) in the actual
ring.

## 2. An exact coefficient lattice and finiteness

For \(F\in V\), set
\[
\alpha=K_4F,\qquad \beta=-K_3F.
\]
These derivatives are generic constants and actual elements,
so \(\alpha,\beta\in\mathcal B\cap L=R\). The remaining
coefficient
\[
\gamma=\Delta F-\alpha x_3-\beta x_4
\]
is also actual and generically constant, hence belongs to \(R\).
Thus
\[
\Delta V\subseteq R+Rx_3+Rx_4.
\tag{6}
\]
In particular this is a bound on all coefficients, not just
the two derivative coefficients.

The exact coefficient lattice is
\[
\Gamma=
\{(\gamma,\alpha,\beta)\in R^3:
 \gamma+\alpha x_3+\beta x_4\in\Delta\mathcal B\}.
\tag{7}
\]
The map
\[
(\gamma,\alpha,\beta)\longmapsto
\frac{\gamma+\alpha x_3+\beta x_4}{\Delta}
\tag{8}
\]
is an \(R\)-module isomorphism \(\Gamma\simeq V\).
Uniqueness follows from the linear independence of
\(1,x_3,x_4\) over \(L\). Conversely membership in (7)
makes (8) actual and affine generic, so it belongs to \(V\).

Because \(R\) is Noetherian, \(\Gamma\subset R^3\) is finite.
It contains \(\Delta R^3\), and hence has rank three.
This proves that \(V\) is finite torsion free of rank three.
The full denominator \(\Delta\) is retained in (7), including
its prime multiplicities.

Equivalently, the derivative map gives an exact sequence
\[
0\longrightarrow R\longrightarrow V
\xrightarrow{\,F\mapsto(K_4F,-K_3F)\,}\Lambda
\longrightarrow0,
\qquad \Lambda\subset R^2.
\tag{9}
\]
The derivative kernel is \(V\cap L=R\), and
\(\Delta R^2\subseteq\Lambda\). Finiteness does not mean
that all relations defining this actual coefficient lattice
have already been computed.

## 3. Local freeness and a basis containing the constant

Invariant localization commutes with (5): the operators are
\(R\)-linear, and localization preserves the kernels and
their finite intersection. Consequently, for every height-one
prime \(\pi\) of \(R\),
\[
V_{(\pi)}
=\mathcal B_{(\pi)}\cap L[x_3,x_4]_{\leq1}.
\tag{10}
\]
Use the inherited actual embedded intersection
\[
\mathcal B=\bigcap_{\operatorname{ht}\pi=1}
\mathcal B_{(\pi)}
\quad\hbox{inside }\mathcal B_L.
\]
This follows coefficientwise from \(\mathcal B=\mathcal A[s_*]\)
and [the invariant-ring intersection](minimal-quadratic-slice-pass46.md),
or by factoring invariant denominators in the actual factorial
ring. Equation (10) gives
\[
V=\bigcap_{\operatorname{ht}\pi=1}V_{(\pi)}
\quad\hbox{inside }V_L=L+Lx_3+Lx_4.
\tag{11}
\]

A finite torsion-free module over a Noetherian normal domain
is reflexive when it has the embedded intersection (11).
Over the regular local ring \(R\) of dimension two, a finite
reflexive module is free. These are precisely the hypotheses
of the two cited primary module lemmas.[^intersection][^free]
Therefore \(V\) is free of rank three.

Faithful flatness gives
\(\mathfrak mR\,\mathcal B\ne\mathcal B\). Since \(V\subset
\mathcal B\), it follows that \(1\notin\mathfrak mR\,V\).
In a finite free module over a local ring, such an element
has at least one unit coefficient and can be extended to a
basis by invertible elementary basis operations. Thus there
exist actual affine generic functions \(u,v\in V\) with
\[
V=R\cdot1\oplus Ru\oplus Rv.
\tag{12}
\]
This uses nonemptiness of the actual closed fiber. No
unimodularity conclusion is drawn from generic rank alone.

## 4. The exact affine-slice ideal

For \(F\in V\), \(EF\) is a generic constant and an actual
element, so it belongs to \(R\). Define
\[
\mathfrak s_{\mathrm{aff}}=E(V)\subset R.
\tag{13}
\]
This is a finite ideal. In the basis (12),
\[
\mathfrak s_{\mathrm{aff}}=(Eu,Ev)R.
\tag{14}
\]
In terms of the exact coefficient lattice (7),
\[
\mathfrak s_{\mathrm{aff}}
=\left\{\frac{f\alpha+g\beta}{\Delta}:
(\gamma,\alpha,\beta)\in\Gamma\right\}\subset R.
\tag{15}
\]
The displayed quotient lies in \(R\) because it is the
actual derivative of (8). This does not assume that arbitrary
coefficient pairs satisfy a divisibility condition in the base.

The selection criterion is exactly
\[
\boxed{\text{an actual affine generic \(E\)-slice exists}
\iff 1\in\mathfrak s_{\mathrm{aff}}
\iff\mathfrak s_{\mathrm{aff}}=R.}
\tag{16}
\]
If \(1=A(Eu)+B(Ev)\) with \(A,B\in R\), then \(Au+Bv\)
is such a slice. The converse follows by applying \(E\).

The original bad coordinates and the derivatives of the good
coordinates all belong to \(V\):
\[
x_3,x_4,Ex_1,Ex_2\in V.
\]
For the last two, differentiate the actual generic quadratics
in (2). Hence
\[
(f,g,h_1,h_2)R\subseteq\mathfrak s_{\mathrm{aff}}.
\tag{17}
\]
No coprimality or unit-ideal premise for the original speeds
is being added.

There is also an intrinsic kernel identification. Put
\(F_1(\mathcal A)=\ker(D^2:\mathcal A\to\mathcal A)\).
Since \(\mathcal A_L=L[j]\), \(j=gx_3-fx_4\), and
\(Dj\in L^*\), the actual \(E\)-invariant affine generic
functions are exactly \(F_1(\mathcal A)\). Thus
\[
0\longrightarrow F_1(\mathcal A)\longrightarrow V
\xrightarrow{E}\mathfrak s_{\mathrm{aff}}\longrightarrow0
\tag{18}
\]
is exact. A free middle module does not force the final ideal
to be the unit ideal.

## 5. What this adds, and what remains

The earlier [generation proof](frame-filtration-generation-pass49.md)
already showed that an actual affine generic slice projects
the four true generators into \(F_2(\mathcal A)\) and gives
\(\mathcal A=R[F_2(\mathcal A)]\). The
[invariant-open proof](fiber-invariant-opens-pass50.md)
already established the relevant bounded-slice descent and
the equivalence between an affine slice and its projected
original list lying in \(F_3\), equivalently \(F_2\), in the
genuine degree-two case.

The additional formulation here is the exact finite
coefficient lattice, its local free rank-three structure, and
the two-generated ideal (13)--(16). It tests affine slice
selection directly, without demanding a radial derivation or
an algebra retraction to the invariant base.

At a genuine second-image obstruction point, the cited
generation and fiber arguments already exclude any affine
generic slice. Therefore the actual ideal
\(\mathfrak s_{\mathrm{aff}}\) is proper there. A future
positive selection theorem would have to use additional
actual-frame information to prove unitness, thereby excluding
the point. Neither the supplied arbitrary slice nor the
freeness in (12) establishes that missing implication.

This note gives no universal generic-degree bound, no
generation theorem for an arbitrary chosen filtration layer,
and no identification of the original bad speeds with
parameters of an intrinsic image ideal. The elementary
calculations and the primary module lemmas require no new
numerical test suite.

[^intersection]: The Stacks Project, [Tag 0AVB](https://stacks.math.columbia.edu/tag/0AVB),
  complete statement and proof: the finite torsion-free
  height-one intersection criterion for reflexivity. This
  source was already used for the intrinsic \(F_2\) module in
  [pass 47](second-image-vector-bundle-pass47.md); it is
  applied here to the different module \(V\).
[^free]: The Stacks Project, [Tag 0B3N](https://stacks.math.columbia.edu/tag/0B3N),
  complete statement and proof: a coherent reflexive module
  on a regular scheme of dimension at most two is locally
  free. The local rank-three conclusion follows over the
  actual regular local invariant surface.
