# An exact horizontal-selection criterion in the canonical homotopy

For the actual canonical nonunit-plinth model of pass 28, there is a
complete criterion within a naturally specified family: all horizontal
LNDs fixing the auxiliary plane pointwise. Their primitive highest
coefficients have a slice exactly when the horizontal coefficient is
independent of the plane's second invariant.

The family includes arbitrary polynomial dependence on the original
slice parameter. As a result, equal relative degrees can give opposite
slice outcomes, and lowering the relative degree can destroy the slice
property. This is not a claim that the global minimum in this family
fails: its unique degree-two member is the successful original
horizontal coordinate partial.

No criterion for arbitrary horizontal actions, unknown rank-three
inputs, or cancellation is asserted.

## 1. The fixed canonical action and the selected family

Keep exactly the [pass-28 modification](canonical-top-pass28.md):
\[
R=\mathbb C[x,y,z],\qquad
D=x^2\partial_y+2y\partial_z,\qquad
r=y,\quad p=x^2,\quad d=x,
\]
\[
B=R[\lambda,w]/((1+\lambda x)w-y)
 =\mathbb C[\lambda,x,w,z],
\]
\[
\Delta\lambda=\Delta x=0,\quad
\Delta w=x^2,\quad
\Delta z=2(1+\lambda x)^2w.
\tag{1}
\]
The full input and canonical plinths, and all primitivity assertions,
are proved directly in the cited note. In particular the plinth is
nonunit, \(d\in\sqrt{p\ker D}\), and \(p\nmid d\).

Define the auxiliary invariant and linear LND
\[
F=2xz-w^2,\qquad L_0=x\partial_w+w\partial_z.
\tag{2}
\]
Thus \(L_0F=0\). The plane \(\mathbb C[x,F]\) is auxiliary:
it is not the canonical invariant plane, and \(\Delta F\ne0\).

We classify precisely the set
\[
\mathcal H=\{\delta\in\operatorname{LND}_{\mathbb C}(B):
       \delta\lambda=1,\ \delta x=\delta F=0\}.
\tag{3}
\]
The pointwise conditions in (3) are part of the theorem. Setwise
preservation of an invariant plane, or no prescribed plane, is a
different problem.

**Classification and top criterion.** Every member of \(\mathcal H\)
has a unique expression
\[
\delta_G=\partial_\lambda+G(\lambda,x,F)L_0,
\qquad G\in\mathbb C[\lambda,x,F].
\tag{4}
\]
Every displayed polynomial \(G\) does give a member. In its actual
horizontal slice coordinates, the primitive highest coefficient of
the fixed canonical \(\Delta\) is sliced if and only if
\[
\boxed{\partial_FG=0.}
\tag{5}
\]
The primitive coefficient is a coordinate partial when (5) holds.
When (5) fails it is \(a\partial_b+b\partial_c\), up to a
nonzero scalar, and has no slice.

## 2. Why (4) describes all the stipulated horizontal LNDs

Let \(\delta\) satisfy (3). Differentiating \(F\), using
\(\delta x=0\), gives
\[
x\delta z=w\delta w.
\]
The variables \(x,w\) are coprime in the original polynomial ring.
Consequently a unique polynomial \(G\in B\) satisfies
\[
\delta w=xG,\qquad \delta z=wG.
\tag{6}
\]
It remains to prove that this regular \(G\) belongs to the smaller
ring in (4). This conclusion uses actual local nilpotence.

Pass to \(K=\mathbb C(x,F)\). Since \(\delta\) kills \(x,F\),
it extends as an LND to
\[
K[\lambda,w],\qquad
\delta=\partial_\lambda+xG\partial_w.
\tag{7}
\]
Here \(z=(F+w^2)/(2x)\), so \(xG\) is a polynomial in
\(\lambda,w\) over the field \(K\).

We use an elementary exact gate. Over any characteristic-zero field,
\[
\partial_\lambda+P(\lambda,w)\partial_w
\text{ is locally nilpotent}
\quad\Longleftrightarrow\quad \deg_wP\le0.
\tag{8}
\]
For \(m=\deg_wP\ge2\), the \(w\)-degree of the \(j\)-th iterate
on \(w\) is \(1+j(m-1)\). Its leading coefficient is multiplied
at the next step by the current positive degree and by the nonzero
leading coefficient of \(P\). The \(\partial_\lambda\) term has
smaller \(w\)-degree, so no iterate vanishes.

If \(P=A(\lambda)w+B(\lambda)\) with \(A\ne0\), write the
coefficient of \(w\) in the \(j\)-th iterate as \(A_j\). It obeys
\[
A_0=1,\qquad A_{j+1}=A_j'+AA_j.
\tag{9}
\]
If \(\deg A=e\ge0\), then \(\deg A_j=je\), with leading
coefficient \(\operatorname{LC}(A)^j\). The derivative term
cannot cancel this coefficient, including when \(A\) is constant.
Again no iterate vanishes. If \(P\) is independent of \(w\), the
derivation is triangular, proving the other direction of (8).

Thus (7) forces \(G\) to be independent of the localized variable
\(w\), or equivalently \(L_0G=0\). The exact kernel on the
original ring is
\[
\ker L_0=\mathbb C[\lambda,x,F].
\tag{10}
\]
For completeness, localizing at \(x\) gives
\(B_x=\mathbb C[\lambda,x,x^{-1},F][w]\), with
\(L_0=x\partial_w\). A polynomial invariant with a putative
highest \(x\)-pole has numerator \(Q(\lambda,x,F)\); modulo
\(x\), substitution \(F=-w^2\) is injective, so the numerator
cannot acquire the divisibility needed to cancel that pole.
This proves (10) by removing poles, not by assuming a localization
identity contracts automatically. Equations (6) and (10) prove
the necessity in (4).

## 3. The full polynomial horizontal trivialization

For an arbitrary \(G\) as in (4), take its unique polynomial
antiderivative in \(\lambda\) with zero constant term:
\[
J(\lambda,x,F)=\int_0^\lambda G(s,x,F)\,ds,
\qquad J(0,x,F)=0.
\tag{11}
\]
No analytic integration is intended: divide each coefficient of
\(\lambda^k\) by \(k+1\). Define
\[
a=x,\quad b=w-xJ(\lambda,x,F),\quad
c=z-J(\lambda,x,F)w+\frac{xJ(\lambda,x,F)^2}{2}.
\tag{12}
\]
Set \(\kappa=2ac-b^2\), and abbreviate
\(J(\lambda,a,\kappa)\) by \(J\). The complete inverse is
\[
x=a,\qquad w=b+aJ,\qquad
z=c+bJ+\frac{aJ^2}{2}.
\tag{13}
\]
Both compositions give polynomial identities and preserve
\(F=\kappa\). Since \(\delta_G J=G\), direct differentiation
gives \(\delta_Ga=\delta_Gb=\delta_Gc=0\). Thus
\[
B=\mathbb C[a,b,c][\lambda],\qquad
\delta_G=\partial_\lambda
\]
in these coordinates. This proves sufficiency in (4) and local
nilpotence even when \(G\) depends on \(\lambda\), so the two
summands in (4) need not commute.

## 4. Exact leading degree and primitive part

Put
\[
V=1+\lambda a,\qquad W=b+aJ,\qquad
T=2aW(2V^2-a).
\tag{14}
\]
The actual canonical action satisfies \(\Delta\kappa=T\).
Differentiating (12) and then using (13) gives exactly
\[
\begin{split}
\Delta a&=0,\\
\Delta b&=a^2-aJ_\kappa T,\\
\Delta c&=2V^2W-Ja^2-bJ_\kappa T.
\end{split}
\tag{15}
\]
In particular these are not arbitrarily assigned relative
coefficient fields: they are the fixed canonical action expressed
through the verified horizontal coordinate inverse.

First suppose \(J_\kappa\ne0\). Write
\[
s=\deg_\lambda J,\qquad r=\deg_\lambda J_\kappa,\qquad
J_s=[\lambda^s]J,\quad K_r=[\lambda^r]J_\kappa.
\]
The normalization in (11) implies \(1\le r\le s\), even
when the highest coefficient of \(J\) is independent of \(\kappa\).
Equation (14) has degree \(s+2\) and leading coefficient
\(4a^4J_s\). Consequently the exact relative degree and top are
\[
q=s+r+2,\qquad
D_q=-4a^4J_sK_r\,(a\partial_b+b\partial_c).
\tag{16}
\]
The competing term \(2V^2W-Ja^2\) has degree at most \(s+2\),
strictly smaller. No cancellation of (16) is possible in the
polynomial domain. The common multiplier lies in
\(\mathbb C[a,\kappa]\), the kernel of
\(L=a\partial_b+b\partial_c\).

Since \(\gcd(a,b)=1\), the primitive part is \(L\). It
has the nonempty fixed locus \(a=b=0\), so every value lies
in the proper ideal \((a,b)\) and it cannot have a slice.
Its full plinth is \(a\mathbb C[a,\kappa]\), as proved by
the all-degree parity calculation in pass 28.

If \(J_\kappa=0\) but \(J\ne0\), then \(s\ge1\) and (15) gives
\[
q=s+2,\qquad D_q=2a^3J_s\partial_c.
\tag{17}
\]
Here \(J_s\in\mathbb C[a]\setminus\{0\}\), so the primitive
part is \(\partial_c\), with polynomial slice \(c\).
If \(J=0\), the original frame is unchanged and
\[
q=2,\qquad D_2=2a^2b\partial_c,
\tag{18}
\]
again with sliced primitive part \(\partial_c\).

Finally \(J_\kappa=0\) is equivalent to \(G_F=0\), because
\(J_\lambda=G\) and \(J(0)=0\). This proves (5).
The claim concerns primitive parts: the actual highest fields in
(16)–(18) have nonunit multipliers and do not themselves have slices.

## 5. Degree is not a substitute for the criterion

For every integer \(N\ge4\), consider the two legitimate choices
\[
J_+=\lambda^{N-2},\qquad
J_-=\lambda^{N-3}+\lambda F.
\tag{19}
\]
Their horizontal coefficients are
\[
G_+=(N-2)\lambda^{N-3},\qquad
G_-=(N-3)\lambda^{N-4}+F.
\]
Both have exact relative degree \(q=N\). The first has
sliced primitive top \(\partial_c\), while the second has
nonsliced primitive top \(a\partial_b+b\partial_c\).
For \(N=4\), the leading coefficient of \(J_-\) is
\(1+F\), so (16) still applies without cancellation.

Nor is lowering the relative degree automatically an improvement:
\(J=\lambda^3\) has degree five and a sliced primitive top,
whereas \(J=\lambda F\) has degree four and a nonsliced primitive
top. This is a failure of monotonicity, not a proof that attaining
the global minimum fails. Within \(\mathcal H\), the unique
degree-two member is \(G=0\), and it succeeds.

All these actions also have the same joint rational invariant
field with \(\Delta\), namely \(\mathbb C(a)\). The constant
coefficient in every frame is
\(D_0=a^2\partial_b+2b\partial_c\). In the successful case,
its common kernel with \(\partial_c\) is \(\mathbb C(a)\).
In the unsuccessful case, its determinant with
\(a\partial_b+b\partial_c\) in the \(b,c\) directions is
\(ab(a-2)\ne0\), giving the same conclusion.
The original joint polynomial kernel is \(\mathbb C[a]\).
Thus that joint-invariant dimension does not distinguish the two
outcomes either.

## 6. Verification and boundary

The standalone checker imports only unittest and SymPy. It checks
actual time-dependent horizontal frames in both inverse directions,
the original canonical action rather than a substitute derivation,
the exact conjugated values, both leading-degree branches including
\(r<s\), the elementary planar nonnilpotence gate, and equal-degree
positive and negative controls.

~~~sh
/opt/anaconda3/bin/python research/horizontal_selection_checks_pass29.py
~~~

The eight methods passed in 0.648 seconds in the final recorded run.

The necessity in (4), exact highest-degree formulas, and all-parameter
criterion are written proofs. Finite controls do not establish them
by extrapolation. A second agent independently reconstructed the
classification, strict highest-degree dominance, and both primitive
parts without finding a correction.

The underlying canonical homotopy, replica flow, localization/parity
argument, and leading-coefficient mechanism are inherited from
[pass 28](canonical-top-pass28.md). The elementary affine-ODE
degree obstruction also appeared in the earlier
[horizontal projection analysis](horizontal-lnd-pass24.md).
No new external classification theorem or novelty assertion is used.

This bounded result provides an exact selection rule only for the
pointwise auxiliary-plane-fixing family (3). It does not construct
that auxiliary plane for an arbitrary unknown kernel, classify
horizontal actions moving it, or supply a universal good-choice
algorithm. Cancellation, priority, expert review, and formal
proof-assistant verification remain unresolved. No old file or
metadata is changed.
