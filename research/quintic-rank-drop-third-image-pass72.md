# The third full image fixes the remaining normalized acceleration

In the independent moving-quintic rank-drop case, a constant
transverse first residual pair already forces the remaining good
coordinate to have constant normalized second derivative.
The second residual pair need not be constant for this conclusion.
The proof uses the full three-dimensional image of the companion
square, including its variable auxiliary entries.

This strengthens the earlier bound on the third derivative.
It does not force the resulting constant to vanish and does not
recognize the remaining quintic kernel.

## 1. Actual hypotheses and the established first two images

Let
\[
B=k[Q_1,Q_2,X,Y],\qquad k=\mathbb C,\qquad
E\in\operatorname{LND}_k(B),\qquad Es_*=1.
\]
The displayed generators are actual polynomial coordinates.
Assume their genuine partials have the supplied bounds
\[
\operatorname{ad}_E^2T_1=\operatorname{ad}_E^2T_2=0,\qquad
\operatorname{ad}_E^3T_X=\operatorname{ad}_E^3T_Y=0.
\]
Retain the independent moving-quintic rank-drop branch of
[the higher rank-drop proof](independent-higher-rank-drop-pass72.md):
\[
\operatorname{rank}_K(V_X,V_Y)
=\operatorname{rank}_K(E,V_X,V_Y)=2,\qquad K=\operatorname{Frac}B,
\]
\[
E^5x=cg^5,\qquad E^6x=0,\qquad
E^4(X,Y)=(g^4,0),\qquad c=e_1,\qquad
g\in\ker E\setminus k,
\tag{1}
\]
where \(V_i=\operatorname{ad}_E^2T_i\) and
\(x=(Q_1,Q_2,X,Y)^t\).
The original slice is retained, but the new linear-algebra
deduction below does not use it.

Put \(\delta=E/g\) on \(B_g\).
The normalized defects have rank one. The zero
\(\widetilde V_X\) branch is already recognized; in the
remaining branch write
\[
D=\widetilde V_X\ne0,\qquad
\widetilde V_Y=\eta D,\qquad [\delta,D]=0,\qquad
\delta\eta=0.
\]
Here \(D\) is a rational derivation, not an asserted primitive
polynomial LND of \(B\).
Set
\[
h_j=\delta^jx,\qquad P=h_1,\qquad
J=\operatorname{Jac}P,\qquad d=D(x),\qquad
\ell=(0,0,1,\eta),\qquad
M=\begin{pmatrix}J&-d/2\\ \ell&0\end{pmatrix}.
\tag{2}
\]
The actual divided flow and inverse matrices give
\[
M^5=0,\qquad \operatorname{Jordan}(M)=(5),\qquad
\operatorname{rank}M^2=3,\qquad
(M^j)_{\rm UL}=\frac{\operatorname{Jac}h_j}{j!},
\]
\[
j!M^j\binom P0
=\binom{h_{j+1}}{j\ell h_j}.
\tag{3}
\]
In particular \(M^4(P,0)^t\ne0\) because its upper component
is \(c/24\). This gives the asserted Jordan type in dimension
five. No derivative of the row \(\ell\) is inserted in (3).

Assume the first residual pair is constant and transverse.
The already established first and second image formulas are
\[
h_4=c\sigma+e,\qquad
h_3=c\tau+e\sigma+v_0,\qquad
\delta\sigma=1,\quad \delta\tau=\sigma,
\]
\[
e,v_0\in k^4,\qquad
e_B=(1,0),\qquad (v_0)_B=\mu=(\mu_1,\mu_2),\qquad
\mu_2\ne0.
\tag{4}
\]
The functions \(\sigma,\tau\) belong to \(B_g\).
These statements are equations (5) and (13) of the linked
rank-drop proof. They use the constant transverse first pair,
not a constant second pair.

## 2. Three vectors span the entire companion-square image

Put \(s_0=\mu_1+\eta\mu_2=\ell v_0\).
Since \(\ell c=0\) and \(\ell e=1\), equation (3) gives
the following vectors:
\[
\begin{aligned}
v&=24M^4\binom P0=\binom{c}{4},\\
w_1&=6M^3\binom P0-\sigma v
      =\binom{e}{3s_0-\sigma},\\
w_2&=2M^2\binom P0-\tau v-\sigma w_1
      =\binom{v_0}
        {2\ell h_2-4\tau-\sigma(3s_0-\sigma)}.
\end{aligned}
\tag{5}
\]
All three belong to \(\operatorname{im}M^2\).
This uses the inclusions
\(\operatorname{im}M^4\subseteq\operatorname{im}M^3
\subseteq\operatorname{im}M^2\), and linear combinations
over \(K\). Their auxiliary components may be variable
rational functions; no constancy is claimed for them.

The upper vectors \(c,e,v_0\) are independent over \(k\):
their bad projections are \(0,(1,0),\mu\), with
\(\mu_2\ne0\), and \(c\ne0\).
They remain independent over \(K\).
Thus \(v,w_1,w_2\) are independent and, by the rank in (3),
span the entire image:
\[
\operatorname{im}M^2=Kv+Kw_1+Kw_2,\qquad
\operatorname{pr}_{K^4}(\operatorname{im}M^2)
=Kc+Ke+Kv_0.
\tag{6}
\]
Only this image statement is needed. In particular no
rank-three assertion for the upper-left block alone is
inferred by discarding the auxiliary column.

## 3. An actual good coordinate has constant acceleration

Choose another original constant good direction \(c_2\)
independent of \(c\). The vectors \((c,e,v_0,c_2)\) form
a constant basis, since \(e_B,\mu\) span the bad plane.
Use its dual actual linear coordinates \((a,b,z,w)\).
Then \(\partial_w=T_{c_2}\) is still an original good partial,
and the constant differential row of \(w\) kills
\(c,e,v_0\).

Each upper part of a base column of \(M^2\) belongs to the
right side of (6). By (3) that upper-left block is
\(\operatorname{Jac}h_2/2\).
Consequently all four ordinary partial derivatives of
\[
\delta^2w=(dw)h_2
\]
vanish. The common constant field of the ordinary coordinate
partials on \(K=k(Q_1,Q_2,X,Y)\) is \(k\). Therefore
\[
\boxed{\delta^2w=\lambda\in k.}
\tag{7}
\]
This is an equality of actual rational functions, not a
specialization to a generic fiber or a coefficient-field
extension.

Because \(Eg=0\), the original polynomial action satisfies
\[
E^2w=\lambda g^2,\qquad E^3w=0.
\tag{8}
\]
The constant \(\lambda\) may be zero or nonzero.
In the former case \(Ew\) is invariant; the lemma does not
establish that former case.
In the latter case it gives an exact nonzero acceleration
along an actual surviving good coordinate.

## 4. Scope and verification

The first constant transverse residual pair suffices for
(7)--(8). No assumption about constancy of the second pair,
no global polynomiality or local nilpotence of the normalized
defect direction, and no polynomial presentation of \(B_g\)
has been added.

The conclusion improves the previously recorded
\(E^3w=0\) to the explicit identity \(E^2w=\lambda g^2\).
It does not remove the separate good-partial cancellation
failure recorded for the direct quintic analogue of the
terminal quartic shear. Nor does it itself supply
\(E^2w=0\), a global slice for the auxiliary symmetry, or
recognition of the remaining quintic action.

The proof is the displayed full-image calculation with its
actual-coordinate contraction. It adds no numerical method,
test suite, regression total, new external theorem, human
expert-review claim, formal certificate, or historical
novelty conclusion. Frozen pass71 and earlier files are
unchanged.
