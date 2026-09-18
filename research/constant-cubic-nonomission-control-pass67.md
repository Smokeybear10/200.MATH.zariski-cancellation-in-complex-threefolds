# An actual cubic frame with no omitted constant direction

The independent constant-top cubic hypotheses do not force their
common curve parameter to omit a constant ambient direction.
The family below has an actual polynomial inverse, exact adjoint
profile \((1,1,2,2)\), independent quadratic defects, and four
complex-linearly independent ordinary derivatives of that parameter.

One good partial does not preserve the common two-variable kernel.
There is nevertheless exactly one preserving constant good line,
which already meets the pass66 recognition criterion. The original
kernel is also explicitly polynomial. Thus this is a countercontrol
to automatic omission and to preservation by every good partial,
not an unrecognized action or a cancellation counterexample.

## 1. Polynomial coordinates and the actual inverse

Let
\[
B=k[t,y,z,s],\qquad k=\mathbb C,\qquad
E=\partial_s,\qquad g=G(t),\quad G\in k[t]\setminus k.
\]
Write \(g'=G'(t)\). Set
\[
X=y+\frac{s^2}{2},\qquad Y=z+gs,
\]
\[
Q_1=\frac12\left(t+sX-\frac{s^3}{6}\right)
=\frac t2+\frac{sy}{2}+\frac{s^3}{6},\qquad
Q_2=s+\frac{Y^2}{2}.
\tag{1}
\]
The inverse is the following finite polynomial sequence:
\[
s=Q_2-\frac{Y^2}{2},\qquad
t=2Q_1-sX+\frac{s^3}{6},\qquad
y=X-\frac{s^2}{2},\qquad z=Y-G(t)s.
\tag{2}
\]
Substitution in either order gives the identity. In particular
\(B=k[Q_1,Q_2,X,Y]\) is an actual coordinate presentation, not
just equality of fraction fields or a nonzero Jacobian test.
Its Jacobian relative to the ordered variables \((t,y,z,s)\)
is \(1/2\).

The original derivation has the actual slice \(s\) and kernel
\[
\ker E=k[t,y,z].
\tag{3}
\]
No recognition theorem is needed for this equality.

## 2. All four actual partials and adjoint heights

Let \(T_1,T_2,T_3,T_4\) be the actual partials in the order
\((Q_1,Q_2,X,Y)\). In the original variables, differentiating (2)
gives
\[
\begin{aligned}
T_1&=2\partial_t-2sg'\partial_z,\\
T_2&=-y\partial_t-s\partial_y+(-g+syg')\partial_z+\partial_s,\\
T_3&=-s\partial_t+\partial_y+s^2g'\partial_z,\\
T_4&=yY\partial_t+sY\partial_y
 +(1+gY-syYg')\partial_z-Y\partial_s.
\end{aligned}
\tag{4}
\]
Here \(Y=z+gs\) in the original ring. These are polynomial
coordinate partials by the two-sided inverse, not fields selected
only to satisfy desired commutators.

Because \(E=\partial_s\), a bracket with \(E\) differentiates
each coefficient in (4) with respect to \(s\). The good tops are
\[
W_1=-2g'\partial_z,\qquad
W_2=-\partial_y+yg'\partial_z,\qquad
[E,W_1]=[E,W_2]=0.
\tag{5}
\]
The bad middle fields are
\[
W_3=-\partial_t+2sg'\partial_z,
\]
\[
W_4=yg\partial_t+(z+2gs)\partial_y
 +\bigl(g^2-y(z+2gs)g'\bigr)\partial_z-g\partial_s.
\tag{6}
\]
Their top fields are
\[
V_3=2g'\partial_z,\qquad
V_4=2g(\partial_y-yg'\partial_z),\qquad
[E,V_3]=[E,V_4]=0.
\tag{7}
\]
Since \(G\) is nonconstant in characteristic zero, \(g,g'\) are
nonzero polynomials. Both good tops and both bad tops are nonzero.
Thus the adjoint heights are exactly \((1,1,2,2)\).
The two defect fields are independent over \(\operatorname{Frac}B\):
their \((y,z)\) coefficient determinant is \(-4gg'\ne0\).
No uniform rank assertion on every fiber of \(t\) is made.

## 3. Exact normalized cubic data

The first three coordinate iterates are
\[
Ex=\left(\frac y2+\frac{s^2}{2},\
            1+gY,\ s,\ g\right)^{\mathsf t},
\]
\[
E^2x=(s,g^2,1,0)^{\mathsf t},\qquad
E^3x=(1,0,0,0)^{\mathsf t},\qquad E^4x=0.
\tag{8}
\]
This is the exact \(c=e_1\) normalization of the
[pass65 independent cubic form](constant-top-cubic-pass65.md), with
\[
f=s,\qquad F=0,\qquad U(t)=G(t)^2.
\]
In particular \(U\) and \(G\) are nonconstant.

The complete defect kernel is also explicit. The first defect
in (7) forces every polynomial in the common kernel to be
independent of \(z\). On that ring, the second forces independence
of \(y\). Therefore
\[
\ker(V_3,V_4)=k[t,s],\qquad
\ker(E,V_3,V_4)=k[t].
\tag{9}
\]
The leading joint rank is three. Equations (5),(7) give the exact
good-field identities
\[
W_1=-V_3,\qquad 2G\,W_2=-V_4,
\tag{10}
\]
consistent with the full pass66 relation
\(U'W_2+F'V_3+G'V_4=0\).
The displayed field identities are polynomial; no inverse of
\(G\) is required on the original ring.

The corrected Heisenberg construction has
\[
N=W_3+\frac12T_1=sg'\partial_z
=\frac f2 V_3,\qquad R=N-\frac f2 V_3=0.
\tag{11}
\]
Thus its rational curve coefficients \(\alpha,\beta\) are both
zero in this family. This is not a non-LND repair example.

## 4. No constant ambient direction omits the parameter

The four ordinary derivatives of the actual common-kernel
generator \(t\) are
\[
(T_1t,T_2t,T_3t,T_4t)=(2,-y,-s,yY).
\tag{12}
\]
They are complex-linearly independent. Indeed a constant relation
\[
2a-by-cs+d\,y(z+G(t)s)=0
\]
first has \(d=0\) by its \(yz\) coefficient. The independent
variables \(y,s\) then force \(b=c=0\), and finally \(a=0\).
Consequently no nonzero constant combination of the four actual
partials kills \(t\). Changing the generator of \(k[t]\) by an
affine linear polynomial does not change this conclusion.

This realizes the nonomission condition recorded as necessary
for the previously unrecognized cubic branch. It does not show
that the example escapes every other recognition criterion.

## 5. The preserving good line is unique

For a constant good direction \(T=aT_1+bT_2\), (4) gives
\[
Tt=2a-by,\qquad Ts=b.
\tag{13}
\]
Since \(t,y,z,s\) are independent coordinates,
\(y\notin k[t,s]\). Hence
\[
T(k[t,s])\subset k[t,s]\quad\Longleftrightarrow\quad b=0.
\tag{14}
\]
In particular \(T_2\) does not preserve the actual defect kernel,
whereas \(T_1\) does and satisfies \(T_1t=2\).
The sufficient preserving-direction criterion in
[pass66](constant-top-cubic-good-fields-pass66.md#4-the-actual-partial-preservation-gate)
already recognizes this action. The explicit inverse and (3)
establish the conclusion independently.

After the constant good-coordinate change
\(\widehat Q_1=Q_1+Q_2,\ \widehat Q_2=Q_1-Q_2\), both displayed
good partials fail preservation individually:
\[
\widehat T_1t=1-y/2,\qquad
\widehat T_2t=1+y/2.
\tag{15}
\]
The preserving line remains
\(k(\widehat T_1+\widehat T_2)=kT_1\).
Thus failure by both named good partials is not failure by every
constant good combination.

## Scope and exact verification

All formulas hold for every nonconstant polynomial \(G(t)\).
The standalone checker
[constant_cubic_nonomission_checks_pass67.py](constant_cubic_nonomission_checks_pass67.py)
separates symbolic \(G(t)\) identities from both polynomial
inverse orders for an explicit nonconstant choice. It checks the
actual four columns, adjoint bounds, cubic normalization, complete
gradient relation and zero correction.
Its first complete run passed both methods in 0.084 seconds, with
exit zero and no failed assertion. Repeated runs are not new methods.

The general common-kernel calculation and the coefficient proof
of (12)--(14) are written algebraic arguments, not inferred from
sampled ranks. The example was built as a polynomial automorphism
before any kernel or frame conclusion was drawn.
No source-classification theorem, frozen-file edit, new universal
frame theorem, complete cubic recognition or general cancellation
solution is asserted.
