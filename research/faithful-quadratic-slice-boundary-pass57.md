# Faithful flatness does not force a quadratic slice gauge

There is a smooth faithfully flat quadratic-generator control with
a supplied slice, a nonempty closed fiber, algebraically independent
bad speeds, and two nonzero quadratic time accelerations, but no
actual slice with transverse generic gauge of degree at most two.
Its exact minimum is three.

The underlying four-ring is an invariant localization of actual
polynomial affine four-space. The displayed four generators are
not ambient polynomial coordinates, and fail even to be local
coordinates at a specified point. Thus this is a countercontrol
to a quadratic-generator selection inference, not to the supplied
full-adjoint-frame program or to cancellation.

## 1. A smooth faithful cylinder over a local invariant surface

Let
\[
C=\mathbb C[a,v],\qquad
R=C_{(a,v-1)},\qquad L=\operatorname{Frac}R.
\tag{1}
\]
In particular \(v\) is a unit of \(R\), while \(a\) is not.
Define
\[
\mathcal A=R[t,z]/(t^2-v-az),\qquad
\mathcal B=\mathcal A[s],\qquad E=\partial_s.
\tag{2}
\]
We use the same letters for the residue classes. These rings
are actual localizations of polynomial rings: start with
\(\mathbb C[a,t,z]\subset\mathbb C[a,t,z,s]\), embed \(C\)
by \(v=t^2-az\), and invert \(C\setminus(a,v-1)\).
The embedding of \(C\) is injective. For example, substituting
\(t=0\) sends a nonzero polynomial \(P(a,v)\) to the nonzero
polynomial \(P(a,-az)\).

The presentation (2) is free with basis \(1,t\) over \(R[z]\).
Consequently \(\mathcal A\), and then \(\mathcal B\), are
faithfully flat over \(R\). More explicitly, for every
\(R\)-module \(M\), \(M\otimes_R\mathcal A\) is the direct
sum of two copies of \(M[z]\), so tensoring detects a
nonzero module as well as preserving exactness.

The relative hypersurface partials \(2t,-a\) generate the
unit ideal in \(\mathcal A\): the ideal \((t,a)\) contains
the unit \(v=t^2-az\). Thus the finitely presented relative
hypersurface is smooth, as is its polynomial extension
\(\mathcal B\). This is the standard Jacobian criterion on
the covering opens \(D(t)\) and \(D(a)\).

The full closed fibers are
\[
\mathcal A/(a,v-1)\mathcal A
  =\mathbb C[t,z]/(t^2-1)
  \simeq\mathbb C[z]\times\mathbb C[z],
\]
\[
\mathcal B/(a,v-1)\mathcal B
  \simeq\mathbb C[z,s]\times\mathbb C[z,s].
\tag{3}
\]
They are nonempty, reduced, and smooth. This removes the
empty-fiber limitation of
[the earlier weak control](quadratic-slice-selection-boundary-pass55.md).

For comparison with the intrinsic notation, there is an actual
LND
\[
D=a\partial_t+2t\partial_z
\quad\hbox{on }\mathcal A,\qquad D(s)=0.
\tag{4}
\]
The relation in (2) is preserved. On \(\mathcal A_L=L[t]\),
where \(z=(t^2-v)/a\), it is \(a\partial_t\).
The monic basis \(1,t\) shows \(\mathcal A\cap L=R\):
in an expression \(P(z)+tQ(z)\), the two summands have
opposite parity in \(t\), so a generic constant forces
\(Q=0\) and \(P\) to be constant in \(R\).
Hence \(\ker D=R\).

The same parity argument identifies
\[
\ker D^2=R\oplus Rt.
\tag{5}
\]
Indeed a nonconstant \(P(z)\) has even generic \(t\)-degree
at least two, while a nonconstant \(Q(z)\) makes \(tQ(z)\)
have odd degree at least three. These highest terms cannot
cancel each other.

The full plinth is therefore \(aR\). The derivation is
primitive, since its values \(a,2t\) generate the unit
ideal in this localization. This does not give a
\(D\)-slice: the full plinth \(aR\) is not the unit ideal.
Also \(D^2z=2a\), so the second image is \(aR\): it is
contained in the plinth and contains \(a\).
The associated second-image correction ideal is the unit
ideal. This control is not a second-image obstruction point.

## 2. Four actual quadratic generators and the supplied slice

Inside \(\mathcal B\), set
\[
w=as+tz,\qquad q=ts+z^2.
\tag{6}
\]
The two exact identities are
\[
aq=tw-vz,\qquad vs=tq-zw.
\tag{7}
\]
Both follow by substituting \(t^2-az=v\). Since \(v\) is a
unit, the second equation gives the actual slice
\[
s=\frac{tq-zw}{v}\in R[t,w,z,q],\qquad Es=1.
\tag{8}
\]
Thus
\[
\mathcal B=R[t,w,z,q].
\tag{9}
\]
This is an actual ring equality, not just a generic
parametrization.

Over \(L\), the pair \((t,w)\) is a polynomial coordinate
pair, with inverse formulas
\[
z=\frac{t^2-v}{a},\qquad
s=\frac{w-t(t^2-v)/a}{a}.
\tag{10}
\]
These are polynomials in \(t,w\) over \(L\), so
\(\mathcal B_L=L[t,w]\). The denominators in (10) are not
asserted to be units of the actual ring.

Choose four actual generators:
\[
X=w,\qquad Y=vw+t,\qquad
Q_1=z+w^2,\qquad Q_2=q+w^2.
\tag{11}
\]
Their inverse as a generator change over \(R\) is
\[
t=Y-vX,\qquad w=X,\qquad
z=Q_1-X^2,\qquad q=Q_2-X^2.
\tag{12}
\]
Hence \(\mathcal B=R[X,Y,Q_1,Q_2]\). If \(T=Y-vX\),
the exact generic graph is
\[
Q_1=\frac{T^2-v}{a}+X^2,\qquad
Q_2=\frac{TX}{a}
       -\frac{v(T^2-v)}{a^2}+X^2.
\tag{13}
\]
Both good generators have total degree at most two in the
generic bad pair \(X,Y\).

The \(E\)-values are
\[
EX=a,\qquad EY=av,\qquad
EQ_1=2aX,\qquad EQ_2=t+2aX,
\]
\[
E^2Q_1=E^2Q_2=2a^2\ne0,\qquad E^3Q_i=0.
\tag{14}
\]
The speeds \(a,av\) are algebraically independent over
\(\mathbb C\). Substituting \(U=a,V=av\) into
\(\sum_j P_j(U)V^j\) gives
\(\sum_j a^jP_j(a)v^j\); independence of \(v\) and the
domain property force every \(P_j\) to vanish.
Their common factor \(a\) is retained, not canceled
from the actual action.

This supplies independent speeds, a time-degree-two
flow on the listed generators, and a smooth faithful
actual cylinder. It does not make (11) an ambient frame.

## 3. The all-slices minimum gauge is exactly three

Choose the affine generic \(E\)-slice
\[
\sigma_0=w/a.
\]
Since \(\ker E=\mathcal A\) in \(\mathcal B=\mathcal A[s]\),
every actual \(E\)-slice is \(s+H\), with \(H\in\mathcal A\).
Relative to \(\sigma_0\), the set of all transverse gauges is
\[
-\frac{tz}{a}+\mathcal A
=-\frac{t(t^2-v)}{a^2}+\mathcal A
\quad\subset L[t].
\tag{15}
\]
The supplied slice gives a degree-three gauge.

Suppose the coset contained \(P(t)\in L[t]\) of degree
at most two. The involution
\[
t\longmapsto-t,\qquad z\longmapsto z
\]
preserves \(\mathcal A\). Taking odd parts in
\(-tz/a-P(t)\in\mathcal A\) gives
\[
t\left(-\frac{z}{a}-\lambda\right)\in\mathcal A
\quad\hbox{for some }\lambda\in L.
\tag{16}
\]
But \(\mathcal A=R[z]\oplus tR[z]\), and this remains a
basis decomposition over \(L[z]\). Equation (16) requires
\(-z/a-\lambda\in R[z]\). Its coefficient of \(z\) is
\(-1/a\notin R\), an impossibility. Therefore
\[
\boxed{\min_{\sigma\in\mathcal B,\ E\sigma=1}
\deg_t(\sigma-\sigma_0)=3.}
\tag{17}
\]
This quantifies over every actual slice, not just replicas
of one supplied slice.

A different affine generic \(E\)-slice differs from
\(\sigma_0\) by an affine polynomial in \(t\), so it
preserves this minimum and the degree-at-most-two
nonexistence. The pair \((X,Y)=(w,vw+t)\) is an
invertible linear change over \(L\) from \((w,t)\).

For a slice with gauge \(H(t)\) of degree \(n\ge3\),
its projection of \(Q_1\) is
\[
\frac{t^2-v}{a}+a^2H(t)^2
\]
and has exact degree \(2n\). The other original
projections have degree at most \(2n\). Thus the
least possible maximum intrinsic degree of this
particular projected list is six. This is not a
minimum algebra-generation claim: \(\mathcal A\)
already has generators \(t,z\) of intrinsic degrees
one and two.

## 4. The affine-slice ideal is genuinely proper

The module in
[the affine-slice formulation](affine-slice-module-pass57.md)
is completely explicit here. Let
\[
V=\mathcal B\cap L[t,w]_{\le1}.
\]
For \(F=\lambda w+\mu t+c\in V\), with coefficients in
\(L\), substitution gives
\[
F=\lambda a\,s+t(\lambda z+\mu)+c.
\tag{18}
\]
Membership in \(\mathcal A[s]\) implies that its constant
coefficient \(t(\lambda z+\mu)+c\) belongs to \(\mathcal A\).
The monic \(1,t\) basis over \(R[z]\) then requires
\(c\in R\) and \(\lambda z+\mu\in R[z]\).
Consequently \(\lambda,\mu\in R\), which also plainly
suffices. Hence
\[
V=R\cdot1\oplus Rt\oplus Rw,\qquad E(V)=aR.
\tag{19}
\]
This free rank-three module contains \(1\) as a basis
element, but its exact affine-slice ideal is proper.
The supplied actual slice (8) lies in the ring
generated by the quadratic list, not in \(V\).
Thus neither faithful flatness nor the free module
alone forces the affine-slice ideal to be the unit ideal.

## 5. The missing ambient-coordinate hypothesis

Regard \((Q_1,Q_2,X,Y)\) as polynomials in the original
ambient coordinates \((a,t,z,s)\), with \(v=t^2-az\).
At the point
\[
(a,t,z,s)=(0,1,0,0),\qquad v=1,
\]
their Jacobian matrix is
\[
\begin{pmatrix}
0&0&1&0\\
0&0&0&1\\
0&0&1&0\\
0&1&1&0
\end{pmatrix},
\tag{20}
\]
which has rank three. The point survives the invariant
localization because its base image is \((a,v)=(0,1)\).
Thus the selected list is not even a local coordinate
system there, and is not a polynomial coordinate frame.

Generation over \(R\) in (9) and (12) does not contradict
(20): the invariant coefficient ring is already
available in that assertion. No actual ambient
translation frame dual to the four listed generators
exists at the displayed point. In particular the
full \((1,1,2,2)\) adjoint hypotheses have not been realized.

This rules out inference from smooth faithful quadratic
generation, a supplied slice, independent bad speeds,
and quadratic time bounds alone to a gauge of degree
at most two. It does not rule out a useful upper bound
of three or higher under those weaker hypotheses, nor
a positive theorem using the missing actual-coordinate
and full-adjoint equations.

## 6. Verification and attribution boundary

The family and its faithful strengthening were proposed
by the parent investigation and reconstructed independently
here. An exact inline SymPy calculation checked both
identities (7), the displayed Jacobian matrix and its rank.
The full Jacobian determinant matched the independent
parent calculation. No standalone suite or full
regression is added by that inline calculation.

The all-slices claim, module equality, flatness, and
scope distinction are proved above. The classical
triangular intrinsic action is reused. No action
classification, human expert review, unresolved-frame
realization, or cancellation counterexample is claimed.

