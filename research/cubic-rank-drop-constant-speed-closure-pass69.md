# An actual shear closes the cubic rank-drop constant-speed branch

The remaining nonzero constant normalized transverse speed supplies
an actual polynomial shear. One formerly bad coordinate partial
becomes good for the original action, not merely for its invariant
division. The new frame has three good partials and one quadratic
bad partial, with flow degree at most two. The previously proved
mixed slice theorem therefore recognizes the original kernel.

This closes the constant-speed alternative of the separate
[rank-drop reduction](cubic-rank-drop-nonconstant-speed-pass69.md).
It is conditional on the supplied actual frame. It does not provide
a universal frame for an arbitrary sliced action.

## 1. Original hypotheses and the remaining normalized alternative

Let
\[
B=k[Q_1,Q_2,X,Y],\qquad k=\mathbb C,\qquad
E\in\operatorname{LND}(B),\qquad E(s_*)=1,\qquad A=\ker E.
\]
The displayed four generators are actual polynomial coordinates.
Their partials satisfy
\[
\operatorname{ad}_E^2T_1=\operatorname{ad}_E^2T_2=0,\qquad
\operatorname{ad}_E^3T_X=\operatorname{ad}_E^3T_Y=0.
\tag{1}
\]
Write \(W_1=[E,T_1]\), \(V_i=\operatorname{ad}_E^2T_i\)
for \(i=X,Y\), and retain the actual normalized highest layers
\[
\operatorname{rank}(V_X,V_Y)=2,\qquad
\operatorname{rank}(E,V_X,V_Y)=2,
\]
\[
E^3x=e_1g^3,\qquad E^4x=0,\qquad
E^2X=g^2,\qquad E^2Y=0,\qquad
g\in\ker E\setminus k.
\tag{2}
\]
Here \(x=(Q_1,Q_2,X,Y)^t\). All ranks are over
\(K=\operatorname{Frac}B\).

The preceding rational companion argument concerns
\(\delta=E/g\) on \(B_g\). It gives
\[
\delta^2x=e_1\sigma+e,\quad e_B=(1,0),\quad
\delta\sigma=1,\quad
\delta X=\sigma+F,\quad \delta Y=G,
\tag{3}
\]
with the full ordinary differential relation \(dF+r\,dG=0\).
The case considered here is
\[
G\in k^*.
\tag{4}
\]
Then \(F\in k\), although the shear below does not need its value.
The first divided defect can be assumed nonzero because its zero
case was already recognized in the preceding note.

Most importantly, (4) gives the original polynomial identity
\(EY=Gg\). Thus
\[
S_0=Y/G\in B,\qquad ES_0=g,\qquad E^2S_0=0.
\tag{5}
\]
No claim that \(S_0\) is an original slice is made.

## 2. The full original highest identity

Put \(P=Ex\), \(J=\operatorname{Jac}P\), and
\(\mathcal V=(V_X(x),V_Y(x))\).
The full original companion coefficient in
[pass42, equation (9)](two-quadratic-top-line-pass42.md)
is
\[
Jh=\frac{m-1}{2}\mathcal V\ell,\qquad
h=E^mx,\quad \ell=L_0E^{m-1}x.
\]
For (2), \(m=3\), \(h=e_1g^3\), and
\(\ell=(g^2,0)^t\). Since \(J\) acts here as a matrix, rather
than differentiating the scalar multiplying its input, cancellation
of \(g^2\ne0\) yields
\[
gJe_1=V_X(x),\qquad
\boxed{gW_1=-V_X.}
\tag{6}
\]
This is an equality of original polynomial derivations. It is
valid along \(g=0\) because it was obtained from a polynomial
identity in the domain \(B\).

## 3. One actual polynomial shear reaches the mixed bound

Set
\[
q_1=Q_1-\frac{YX}{2G}+\frac{Y^3}{12G^3},\qquad q_2=Q_2,
\qquad x_3=X,\qquad x_4=Y.
\tag{7}
\]
Its polynomial inverse is
\(Q_1=q_1+YX/(2G)-Y^3/(12G^3)\), with the other three
coordinates unchanged. Thus
\(B=k[q_1,q_2,X,Y]\) is an actual coordinate presentation.
Its partials, expressed in the old frame, are
\[
T'_1=T_1,\quad T'_2=T_2,\quad
T'_X=T_X+\frac{S_0}{2}T_1,\quad
T'_Y=T_Y+\theta T_1,\qquad
\theta=\frac{X}{2G}-\frac{Y^2}{4G^3}.
\tag{8}
\]
The first two retain their original good bounds.
For a function \(a\) and a derivation \(T\), the ordinary
Leibniz commutator formula is
\[
\operatorname{ad}_E^n(aT)
=\sum_{j=0}^{n}\binom nj E^{n-j}(a)
       \operatorname{ad}_E^jT.
\]
Using \(E^2S_0=0\), \(\operatorname{ad}_E^2T_1=0\),
and (6), it gives
\[
\operatorname{ad}_E^2T'_X
=V_X+gW_1=0.
\tag{9}
\]
This is the decisive original-ring cancellation. In particular
the new \(X\)-partial is a genuine third good partial.

For the remaining partial, \(EY=Gg\), \(E^2Y=0\),
and \(E^2X=g^2\) give
\[
E^2\theta=\frac{g^2}{2G}
 -\frac{2G^2g^2}{4G^3}=0,\qquad E^3\theta=0.
\]
Its original third adjoint is therefore
\[
\operatorname{ad}_E^3T'_Y
=\operatorname{ad}_E^3T_Y+E^3\theta\,T_1
 +3E^2\theta\,W_1=0.
\tag{10}
\]
The omitted summands contain higher adjoints of the original
good \(T_1\) and are zero. Consequently the actual new profile
is bounded by \((1,1,1,2)\). Exact equality of the four heights is
not needed.

## 4. Flow degree and the inherited recognition endpoint

The product rule also gives
\[
E^3(YX)=3Gg^3,\qquad E^3(Y^3)=6G^3g^3.
\]
Therefore the actual new generators satisfy
\[
E^3(q_1,q_2,X,Y)^t=0,
\tag{11}
\]
because its first component is
\(g^3-3g^3/2+g^3/2=0\).

The complete mixed slice theorem in
[pass13, Section 1](../deep-pass-13.md) requires three actual
partials with second adjoint zero, one actual partial with
third adjoint zero, and the original polynomial slice.
Equations (8)--(10) establish precisely those hypotheses;
the original \(s_*\) has not changed. Thus
\[
\boxed{A=\ker E\simeq k^{[3]}.}
\tag{12}
\]
The use of that inherited theorem retains its proved recognition
and primary-source dependencies. The additional bound (11) is
consistent with its low-flow recognition branch. This argument
does not assert that \(B_g\) is a polynomial four-ring.

## 5. Divided-field crosscheck and scope

The first new partial also has zero divided second adjoint.
Indeed the preceding normalized companion gives
\(\widetilde V_X=D\) and \([\delta,T_1]=-D\), so
\[
\operatorname{ad}_\delta^2T'_X
=D+2\delta(S_0/2)[\delta,T_1]=0.
\tag{13}
\]
Together with its original third-adjoint bound, the separate
[vertical-top exclusion lemma](vertical-top-exclusion-pass69.md)
would upgrade this divided-good condition to (9). The direct
original identity (6) already supplies that upgrade here, so
the proof of (12) does not require a local-nilpotence assertion
for a coordinate partial on \(B_g\).

Combined with the preceding rank-drop note's zero-first-defect,
zero-speed and nonconstant-speed alternatives, (12) closes the
remaining independent moving cubic of original joint rank two.
The original joint-rank-three cubic was recognized separately
in pass68. This argument does not recognize the dependent-defect
nonconstant cubic, close the remaining higher moving-top branches,
or supply a universal actual frame.

The full algebraic proof is written above. This file adds no
checker, regression claim, metadata change, or historical-novelty
claim. Independent reconstruction is not human expert review
or formal verification.
