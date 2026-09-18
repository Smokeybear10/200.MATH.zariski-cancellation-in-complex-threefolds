# The nonzero constant normalized speed in the moving cubic branch

The remaining nonzero constant normalized transverse speed is
recognized in the independent moving cubic branch of original
joint rank three. A rational relation between the two actual good
derivatives of an invariant polynomial has constant ratio by a
polynomial-degree argument. This supplies an omitted actual good
direction, to which the previously proved recognition theorem applies.

Together with the two earlier moving cubic notes, this recognizes
the whole original joint-rank-three branch under their power-law
hypotheses. The original joint-rank-two branch, in which division
by the invariant factor drops the defect rank, is not covered.

## 1. Retained actual and divided data

Retain all hypotheses of the
[moving coordinate-local-slice note](moving-cubic-coordinate-local-slice-pass68.md).
In particular
\[
B=k[Q_1,Q_2,X,Y],\qquad k=\mathbb C,\qquad
E\in\operatorname{LND}(B),\qquad Es_*=1,
\]
\[
\operatorname{ad}_E^2T_1=\operatorname{ad}_E^2T_2=0,\qquad
\operatorname{ad}_E^3T_X=\operatorname{ad}_E^3T_Y=0,
\]
and the independent original defects satisfy
\[
E^3x=e_1g^3,\quad L_0E^2x=(1,0)^tg^2,\quad
g\in\ker E\setminus k,\quad
\operatorname{rank}(E,V_X,V_Y)=3.
\tag{1}
\]
The original common kernel is \(k[t]\), where \(t\in B\) is an
actual nonconstant polynomial and \(g=g_0(t)\).
On the actual invariant localization \(B_g\), put
\(\delta=E/g\) and \(\sigma=\delta X\).
The previous note proves
\[
\delta\sigma=1,\quad
\delta^2x=(\sigma-F_0(t),U(t),1,0)^t,\quad
\delta Y=G(t),\qquad U'\ne0,
\tag{2}
\]
with \(F_0,U,G\in k(t)\). Its divided defects
\(\widetilde V_X,\widetilde V_Y\) are independent and have exact
rational joint kernel \(k(t,\sigma)\); their common kernel with
\(\delta\) is \(k(t)\).

Assume here that
\[
G\in k^*.
\tag{3}
\]
The case \(G=0\) already fixes the actual coordinate \(Y\).
The nonconstant \(G\) case is recognized in the separate
[moving graph proof](moving-cubic-graph-recognition-pass68.md).

Set \(S=Y/G\). This is an actual constant rescaling of a bad
coordinate, and \(\delta S=1\). The divided defects kill both
\(\sigma\) and \(Y\), the latter because their second
\(\delta\)-adjoint applied to \(Y\) is zero when \(\delta Y\)
is constant. Therefore
\[
\sigma=S-h(t),\qquad h\in k(t).
\tag{4}
\]
This is an identity in the fraction field. No global polynomial
slice for \(\delta\) on \(B\), nor polynomiality of \(\delta\)
on \(B\), is inferred.

The original highest identities, applied to \(g=g_0(t)\), give
\[
Et=W_1t=W_2t=0,\qquad W_i=[E,T_i].
\tag{5}
\]
Here \(g_0'\ne0\) in characteristic zero and \(B\) is a domain.
These are statements about the original fields.

## 2. A polynomial derivative-ratio lemma

Let \(L\) be any extension field of \(k\), and let
\(t\in L[q_1,q_2]\). Suppose
\[
\partial_{q_1}t\ne0,\qquad
\partial_{q_2}t=r(t)\partial_{q_1}t,\qquad r\in k(T)
\]
where substitution \(T=t\) is understood. Then \(r\in k\).

Indeed \(n=\deg_{q_1,q_2}t\ge1\). Write \(r=a/b\) with coprime
\(a,b\in k[T]\), \(b\ne0\). The substituted Bézout identity
shows that \(a(t),b(t)\) are comaximal in \(L[q_1,q_2]\).
The derivative relation therefore implies
\[
b(t)\mid\partial_{q_1}t.
\tag{6}
\]
If \(b\) were nonconstant, then
\[
\deg b(t)=n\deg b\ge n>
\deg\partial_{q_1}t,
\]
contradicting (6). Thus \(r\) is a polynomial in \(k[T]\).
If it were nonconstant, the nonzero product on the right in
\[
\partial_{q_2}t=r(t)\partial_{q_1}t
\]
would have degree at least \(n\), whereas a nonzero derivative
on the left has degree at most \(n-1\). A zero derivative on
the left is also impossible when that product is nonzero.
Hence \(r\in k\), including the allowed value zero.

This elementary argument uses the actual polynomial \(t\).
It is not valid after replacing \(t\) by an arbitrary formal
series or adjoining an algebraic root outside the original field.

## 3. The three actual branches

First suppose \(h'=0\). Then \(h\in k\), and
\[
I=X-\frac{S^2}{2}+hS
\tag{7}
\]
is an actual triangular ambient coordinate. Equations (4) and
\(\delta S=1\) give
\[
\delta I=(S-h)-S+h=0,
\]
so \(EI=0\) in the original polynomial ring. The existing
invariant-coordinate endpoint, retaining the original slice,
recognizes \(\ker E\simeq k^{[3]}\).

Now assume \(h'\ne0\). Write \(J=\operatorname{Jac}(\delta x)\).
The exact divided good-field identity, obtained from the full
inverse-Jacobian coefficient, is
\[
J e_1=\widetilde V_X(x),\qquad
U'[\delta,T_2]+F_0'\widetilde V_X=0.
\]
As \([\delta,T_2](x)=-J e_2\), this gives
\[
J e_2=r(t)J e_1,\qquad r=\frac{F_0'}{U'}.
\tag{8}
\]
Take the bad \(X\)-component of (8). Since the two original
good partials kill \(S=Y/G\), equation (4) gives
\[
T_2\sigma=r(t)T_1\sigma,\qquad
T_2t=r(t)T_1t.
\tag{9}
\]
The sign and ratio in (9) come from (8); no interchange of
the two good columns is made.

If \(T_1t=0\), a nonzero actual constant good direction already
kills \(t\). This is an immediate recognition branch using (5)
and the omitted-good-direction theorem cited below. There is
no need to prove that any divided defect vanishes.

Finally suppose \(T_1t\ne0\). Regard the actual polynomial \(t\)
as an element of \(L[Q_1,Q_2]\), where \(L=k(X,Y)\).
The derivative-ratio lemma applies to (9) and gives \(r=r_0\in k\).
Consequently
\[
(T_2-r_0T_1)t=0.
\tag{10}
\]
This is a genuine nonzero complex constant good direction:
\(T_1,T_2\) are the original independent good partials.

## 4. Apply only the original recognition theorem

In each branch with \(h'\ne0\), equations (5),(10), or
\(T_1t=0\), supply precisely the hypotheses of
[An omitted good direction recognizes the original kernel](good-direction-recognition-pass46.md):
two actual good coordinate partials, the original sliced LND
\(E\), an actual nonconstant common invariant \(t\), and one
nonzero constant combination of the good directions killing it.
That theorem gives an original invariant ambient coordinate
and hence
\[
\boxed{\ker E\simeq k^{[3]}.}
\tag{11}
\]
Its source obligations and original-slice endpoint are retained.
No local nilpotence of the divided defects or localized partials
is used in applying it. It is not applied to \(\delta\).

The good quadratic velocity identity is an identity for
\(\widetilde V_X(\delta Q_i)\), not automatically for
\(\widetilde V_X(Q_i)\). In particular, this proof does not
infer a zero divided defect from \(T_1t=0\). The direct
omitted-direction branch makes such an inference unnecessary.

## 5. Consolidated scope and verification

The three normalized transverse-speed alternatives are now accounted
for at original joint rank three: \(G=0\) supplies an invariant
coordinate; nonconstant \(G\) is recognized by the coordinate-field
graph proof; and this note handles \(G\in k^*\).
All retain (1), including the nonzero power-law bad vector and
the original independent defects.

The original joint-rank-two case has only one independent divided
defect and is not covered by these graph identities. No unrestricted
moving-top, full supplied-profile, or universal-frame theorem is
claimed here.

This is a new written proof beyond the two earlier moving68 notes.
Its three-branch structure corrects an unnecessary provisional
outline inference at \(T_1t=0\); the correction changes no frozen
or previously stable file. The complete omitted-good-direction
proof was reread through EOF before using it. Its inherited
primary-source gates are reused, without claiming a fresh full
primary-source audit of every cited recognition theorem.
No new numerical suite or method count is asserted.
