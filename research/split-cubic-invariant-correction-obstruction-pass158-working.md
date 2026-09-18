# A split-cubic initial relation has no weight-three invariant lift

**Status: working proof of a correction obstruction, not recognition.**

In an actual sliced E-time \((1,1,2,2)\) frame whose full initial
kernel is \((XZ+YW)\), every nonconstant invariant has original
weighted degree at least four. In particular the split-cubic
initial relation cannot be corrected by lower-weight terms
to an invariant.

The obstruction is elementary: every proposed lift has a unique
nondegenerate critical point, and invariance would make the
derivation vanish at that point, contradicting its global slice.
This rules out a particular correction strategy, not the actual
split-cubic frame. The retained157 example realizes that frame
and has an affine-in-time, noninvariant lift.

## 1. A critical-point lemma in the original polynomial ring

Let \(B=\mathbb C[X,Y,Z,W]\) be an actual polynomial four-ring.
Suppose a polynomial derivation \(E\) has a global polynomial
slice \(u\), so \(Eu=1\). Local nilpotence is not needed for
the following lemma.
For constants \(\lambda\ne0,\alpha,\beta\in\mathbb C\)
and any \(Q\in\mathbb C[X,Y]\), set
\[
H=\lambda(XZ+YW)+\alpha Z+\beta W+Q(X,Y).
\tag{1}
\]
Then \(EH\ne0\).

Indeed \(H_Z=\lambda X+\alpha\) and
\(H_W=\lambda Y+\beta\), so a critical point must have
\[
X_*=-\alpha/\lambda,\qquad Y_*=-\beta/\lambda,\qquad
Z_*=-Q_X(X_*,Y_*)/\lambda,\qquad
W_*=-Q_Y(X_*,Y_*)/\lambda .
\tag{2}
\]
Conversely these four values make every first partial of \(H\)
zero. Thus \(q_*=(X_*,Y_*,Z_*,W_*)\) is a unique complex
point, not merely a point over a coefficient-field extension.

In the coordinate order \(X,Y,Z,W\), its Hessian is
\[
\operatorname{Hess}H(q_*)
=
\begin{pmatrix}
Q_{XX}&Q_{XY}&\lambda&0\\
Q_{XY}&Q_{YY}&0&\lambda\\
\lambda&0&0&0\\
0&\lambda&0&0
\end{pmatrix}_{(X_*,Y_*)},
\qquad
\det\operatorname{Hess}H(q_*)=\lambda^4\ne0 .
\tag{3}
\]
The determinant does not depend on the entries in the upper
left block. The lemma therefore permits arbitrary \(Q\),
not just a polynomial of degree at most two.
In the low-weight application below, \(Q\) has degree at most
two and the entire Hessian is constant.

Write \(E=\sum_{i=1}^4p_i\partial_{x_i}\) with
\((x_1,x_2,x_3,x_4)=(X,Y,Z,W)\).
If \(EH=\sum_i p_iH_{x_i}=0\), differentiate this polynomial
identity in each original coordinate and evaluate at \(q_*\).
Every term differentiating \(p_i\) is multiplied by a first
partial of \(H\), which is zero there. The remaining terms give
\[
\operatorname{Hess}H(q_*)\,
 (p_1(q_*),p_2(q_*),p_3(q_*),p_4(q_*))^{\mathsf T}=0 .
\tag{4}
\]
Invertibility in (3) forces the whole polynomial vector field
to vanish at \(q_*\). Evaluating the slice identity now yields
\(1=(Eu)(q_*)=\sum_i p_i(q_*)u_{x_i}(q_*)=0\), a contradiction.
This proves the lemma directly, without treating a critical
point over a moving coefficient field as an original point.

## 2. Exact weighted scope of the no-lift conclusion

Assume the actual slice and time-degree hypotheses of157:
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\\
(\deg_E X,\deg_E Y,\deg_E Z,\deg_E W)=(1,1,2,2),\\
X=x_0+au,\quad Y=y_0+bu,\quad
Z=z_0+z_1u+eu^2,\quad W=w_0+w_1u+hu^2,\\
\theta:\mathbb C[\mathsf X,\mathsf Y,\mathsf Z,\mathsf W]\longrightarrow A[\eta],
\quad
(\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
\longmapsto(a\eta,b\eta,e\eta^2,h\eta^2),\\
\ker\theta=(\mathsf X\mathsf Z+\mathsf Y\mathsf W).
\end{gathered}
\tag{5}
\]
Here \(\eta\) is independent over \(A\), and the formal source
weights are \((1,1,2,2)\). The coefficients \(e,h\) are the
ordinary \(u^2\) coefficients. The principal ideal in (5) is
the full initial kernel, not only a relation known to vanish.
The actual normalization157 explains when this split form
arises from an independent cubic coefficient row.[^1]

Let \(\mathcal F_MA\) denote invariants whose representing
polynomial in the actual four coordinates has source weighted
degree at most \(M\). Then
\[
\mathcal F_3A=\mathbb C .
\tag{6}
\]
For if \(f\in A\setminus\mathbb C\) had weighted degree
\(0<M\le3\), its top weighted polynomial \(P_M\) would
evaluate to zero under \(\theta\): that evaluation is its
\(u^M\) coefficient multiplied by \(\eta^M\), whereas \(f\)
has E-degree zero.
Since the full kernel is generated in weight three, necessarily
\(M=3\) and
\(P_3=\lambda(\mathsf X\mathsf Z+\mathsf Y\mathsf W)\)
for some nonzero complex \(\lambda\).

All terms of smaller weight form a polynomial
\(\alpha Z+\beta W+Q(X,Y)\) with
\(\alpha,\beta\in\mathbb C\) and \(\deg Q\le2\).
Thus the actual invariant \(f\) has exactly the form (1),
contradicting the lemma.
This also proves directly that no polynomial with nonzero
top part \(\lambda(XZ+YW)\) and lower-weight correction can
be invariant.

The nonzero top-part condition matters. The statement does
not allow a weight-three correction that cancels the entire
displayed relation and leaves a constant. Nor, without the
full initial-kernel hypothesis, does it exclude every other
polynomial of weight at most three.
The elementary lemma separately excludes the larger family
(1), even when the good-coordinate polynomial \(Q\) has
higher degree; this does not identify every possible
higher-weight invariant.

## 3. The actual split-cubic boundary is consistent with the obstruction

The retained157 construction starts in the actual ring
\(\mathbb C[u,a,b,c]\) with \(E=\partial_u\), and uses
\[
\begin{gathered}
X=u,\quad Y=a+bu,\quad Z_0=c-bu,\quad W_0=b+u,\quad
p=c+a+b^2,\\
H_0=XZ_0+YW_0=ab+up,\qquad
Z=Z_0+YH_0,\quad W=W_0-XH_0,\\
XZ+YW=H_0,\qquad EH_0=p\ne0,\qquad E^2H_0=0 .
\end{gathered}
\tag{7}
\]
Its two inverse stages recover
\(H_0=XZ+YW,\ Z_0=Z-YH_0,\ W_0=W+XH_0\), then
\(u=X,\ b=W_0-X,\ a=Y-bX,\ c=Z_0+bX\).
Both inverse orders and the full height-one initial kernel
were proved in157.[^1]
Thus (5) is actually realizable, and (7) does not contradict
(6): \(H_0\) is E-affine, not invariant.
The kernel of this example is already polynomial, since
\(X=u\) is a coordinate slice.

Even the literal affine property can depend on lower-weight
terms. Replacing the good coordinate \(X\) by \(X+s\), with
a nonzero complex constant \(s\), leaves its leading
coefficient and the normalized initial relation unchanged.
The new displayed split polynomial is \(H_0+sZ\), and
\(E^2(H_0+sZ)=2s\,bp\ne0\).
Subtracting the lower-weight linear bad term \(sZ\) restores
the affine lift. This does not create an invariant lift.

## 4. An affine lift still needs a compatible actual shear

For clarity, an exact sufficient straightening condition
is different from an invariant correction.
In a normalized frame let \(F=XZ+YW\) and
\(\delta=Y\partial_Z-X\partial_W\).
Suppose there is a polynomial
\(P\in\mathbb C[X,Y,F]\) such that
\[
E^2P=0,\qquad e=b\,EP,\qquad h=-a\,EP .
\tag{8}
\]
These are additional hypotheses, not consequences of the
initial identity \(ae+bh=0\).
Because \(\delta\) kills \(X,Y,F\), it kills \(P\), so
\[
Z'=Z-YP,\qquad W'=W+XP,\qquad X'=X,\quad Y'=Y
\tag{9}
\]
is an actual polynomial change with inverse
\(Z=Z'+Y'P,\ W=W'-X'P\).
In the inverse formula \(P\) is evaluated using
\(F=X'Z'+Y'W'\), which equals \(XZ+YW\).
This verifies both inverse orders without division by a
coordinate or by a speed.

Using \(E^2X=E^2Y=0\), equation (8) gives
\(E^2Z'=2e-2b\,EP-YE^2P=0\) and
\(E^2W'=2h+2a\,EP+XE^2P=0\).
The transformed frame is nice, so the retained three-good
recognition156, or its nice endpoint80, recognizes \(A\).[^2]
The example (7) satisfies this gate with \(P=F=H_0\).

This sufficient gate asserts neither existence of \(P\) nor
that every E-affine correction belongs to
\(\mathbb C[X,Y,F]\). A lower-weight correction involving
linear bad terms may require a different translated
H-preserving shear; its polynomial inverse and the matching
acceleration identities would still need to be checked.
The no-lift theorem identifies which invariant strategy fails.
It does not solve this affine-correction problem or recognize
every split-cubic frame.

## Sources and scope

1. [Cubic normal forms and the actual split boundary157](two-linear-cubic-normal-forms-pass157-working.md),
   Sections 1--5, together with
   [the actual initial bound157](two-linear-two-quadratic-initial-bound-pass157-working.md).
   These provide the stated actual profile, full principal
   initial ideal, and inverse-verified example.
2. [All-degree three-good recognition156](three-good-all-degree-recognition-pass156-working.md).
   Only the explicit conditional shear (8)--(9) supplies its
   hypotheses here. No general correction existence is imported.

The critical-point and differentiated-invariance arguments
are written in full and require no external classification
theorem. They are not claimed as historically new.
This is a private working obstruction with the stated
recognition dependencies, not human expert review,
proof-assistant certification, or a conclusion from finite
tests. No157 or earlier file is changed.
The remaining split-cubic, weight-four, lower-initial-rank,
and arbitrary-entry questions are not settled by this note.

[^1]: Source 1.
[^2]: Source 2.
