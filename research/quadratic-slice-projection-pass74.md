# A quantitative certificate from a quadratic slice projection

If the actual slice projection of a sliced action on complex four-space
has ordinary degree at most two, there are coordinates adapted to that
same slice with forward degree at most two and inverse degree at most
four. The proof classifies the quadratic projection after an actual
affine change and supplies both polynomial inverse maps.

This is a modest quantitative certificate, not a new recognition
family: the retained elementary argument already recognizes every
slice of degree at most two, and a quadratic projection forces its
slice to have that degree bound. No small projection degree is proved
for an arbitrary sliced action.

## 1. General projection bounds and existing limitations

Let
\[
B=\mathbb C[x_1,x_2,x_3,x_4],\qquad
E\in\operatorname{LND}(B),\qquad Es=1,
\]
\[
P=Ex,\qquad \deg P_i\le e,\qquad \deg s\le d,
\qquad E^N x=0,
\quad e\ge1,\ d\ge1.
\tag{1}
\]
An upper coefficient-degree bound \(e=1\) includes constant
fields. Write \(A=\ker E\). The actual polynomial flow, first
with an independent parameter, gives the slice retraction
\[
\pi_i(x)=\sum_{j=0}^{N-1}\frac{(-s(x))^j}{j!}E^j(x_i),
\qquad \pi(f)=f(\pi_1,\ldots,\pi_4).
\tag{2}
\]
This notation does not mean exponentiating the derivation \(-sE\).
The slice theorem identifies (2) with evaluation at \(s=0\)
in \(B=A[s]\). In particular
\[
\pi^2=\pi,\qquad \operatorname{im}\pi=A
 =\mathbb C[\pi_1,\ldots,\pi_4],\qquad \ker\pi=sB.
\tag{3}
\]
These facts are already retained in
[the nonlinear-frame analysis](nonlinear-frame-pass22.md), Section 1,
and [the slice-filtration calculation](simultaneous-frame-pass26.md),
Section 6. A bounded generator list is not a coordinate list.

For every nonzero iterate, ordinary degree satisfies
\(\deg E^j x_i\le1+j(e-1)\). Therefore
\[
\deg\pi_i\le1+(N-1)(d+e-1).
\tag{4}
\]
Terms whose iterates vanish are omitted. This estimate is a bound
on the actual four generators in (3), not a bound on a polynomial
coordinate inverse for \(A\).

There is also the elementary reverse observation
\[
\deg s\le\max(1,\deg\pi).
\tag{5}
\]
Indeed, at least one \(x_i-\pi_i\) is nonzero, because \(\pi(s)=0\)
and \(s\ne0\). That polynomial is divisible by \(s\), by (3),
and its degree is at most \(\max(1,\deg\pi)\).

The general Jacobian rank does not supply a missing coordinate.
If \(\Phi_t\) is the actual flow and
\(J_t=\operatorname{Jac}_x\Phi_t\) before substituting its time,
the chain rule gives
\[
\operatorname{Jac}\pi
 =J_{-s}(I-P\,ds).
\tag{6}
\]
Here \(ds\) is the row of partial derivatives. The identity
\(\partial_t\Phi_t=J_tP\) follows from the flow group law.
The matrix \(J_{-s}\) is invertible over \(B\), since the
independent-time flow has a polynomial inverse and determinant one.
Also \(ds(P)=1\). Thus (6) has rank three at every complex
point and kernel \(BP\) as a module. Those properties are
automatic for every action in (1).
At \(s=0\), (6) is exactly the projector \(I-P\,ds\)
already studied in pass22. That note gives actual translation
controls with nonflat projected connection, and even a flat
projected connection with no polynomial horizontal frame.
Neither constant rank nor its module splitting is used as recognition.

## 2. Exact quadratic normal form

Assume now that \(\deg\pi\le2\). Choose a fixed point of
\(\pi\), for example \(\pi(0)\), and translate it to zero.
This is an actual affine coordinate change and preserves all ordinary
degree bounds. The derivative \(L=\operatorname{Jac}\pi(0)\)
has rank three by (6), and \(L^2=L\) by idempotence.
A further constant invertible linear change gives
\[
x=(u_1,u_2,u_3,t),\qquad L=\operatorname{diag}(I_3,0),
\qquad \pi(x)=Lx+H_2(x),
\tag{7}
\]
where \(H_2\) is homogeneous quadratic, possibly zero.
The action and slice are transported by these actual coordinate
changes; the labels in (7) are not assumed adapted to \(E\).

The degree-two part of \(\pi\circ\pi=\pi\) is
\(LH_2+H_2\circ L=H_2\). Its upper three entries show
that the upper part of \(H_2\) vanishes at \(t=0\).
Its lower entry is independent of \(t\). Consequently
\[
\pi(u,t)=(U(u,t),Q(u)),\qquad
U=(I+tM)u+t^2b,
\]
\[
M\in\operatorname{Mat}_3(\mathbb C),\quad b\in\mathbb C^3,
\qquad Q\in\mathbb C[u_1,u_2,u_3]_2,
\tag{8}
\]
where zero is allowed for the homogeneous quadratic \(Q\).

The full lower idempotence identity is \(Q(U)=Q(u)\).
Furthermore \(\pi(u,0)=(u,Q(u))\). Hence the image is exactly
the polynomial graph \((u,Q(u))\). Algebraically,
\[
\ker\pi=(t-Q(u)),\qquad
\operatorname{im}\pi=\mathbb C[U_1,U_2,U_3].
\tag{9}
\]
For the first assertion, \(t-Q(u)\) maps to zero. Conversely,
if \(f\circ\pi=0\), restricting to \(t=0\) gives
\(f(u,Q(u))=0\), which is precisely divisibility by
the monic polynomial \(t-Q(u)\).
For the second, \(Q(u)=Q(U)\) and the three \(U_i\) are
algebraically independent: restricting a relation among them to
\(t=0\) gives the same relation among the three independent \(u_i\).

Comparing (9) with (3) proves
\[
s=c(t-Q(u)),\qquad c\in\mathbb C^*.
\tag{10}
\]
The unit is a complex constant because the units of \(B\) are
exactly \(\mathbb C^*\). Thus the original supplied slice itself
is a quadratic or linear coordinate.

The older [low-degree-slice lemma](nice-route.md#low-degree-slices-close-by-elementary-linear-algebra)
already proves coordinatehood from \(\deg s\le2\) and \(Es=1\).
Equations (5) and that lemma would suffice for recognition here.
The remaining calculation provides the stronger explicit adapted
degree bound, rather than claiming this as a new recognized family.

## 3. Both adapted inverse maps and the degree-four bound

There are two cases in (8).

If \(Q\ne0\), the full upper idempotence identity becomes
\[
Q(u)\bigl(Mu+tM^2u+t^2Mb+Q(u)b\bigr)=0.
\tag{11}
\]
Setting \(t=0\) and separating homogeneous degrees gives
\(M=0\) and \(b=0\). Hence \(U=u\).
Since the \(U_i\) are invariant and \(Es=1\), (10) gives
\(Eu=0\), \(Et=1/c\). The original action is a constant
translation in this affine frame. Its adapted inverse pair is
\[
F(u,t)=(u,c(t-Q(u))),\qquad
G(U,S)=(U,S/c+Q(U)).
\tag{12}
\]
Both maps have degree at most two, and both inverse orders follow
by direct substitution.

If \(Q=0\), then \(s=ct\). By (9) and the original slice
theorem,
\[
B=A[s]=\mathbb C[U_1,U_2,U_3,t].
\]
Thus \((U,t)\) is already an actual polynomial coordinate
system. This is proved from the exact algebra equality and
independence, not inferred from a Jacobian determinant.
Its Jacobian determinant is therefore a unit. Using (8),
that determinant is \(\det(I+tM)\), which has value one
at \(t=0\). Hence \(\det(I+tM)=1\), so \(M\) is
nilpotent and \(M^3=0\).

With \(T=S/c\), the explicit adapted pair is now
\[
F(u,t)=((I+tM)u+t^2b,ct),
\]
\[
G(U,S)=\bigl((I-TM+T^2M^2)(U-T^2b),T\bigr).
\tag{13}
\]
The identity
\((I+TM)(I-TM+T^2M^2)=I\) proves both inverse orders.
The forward degree is at most two. The inverse terms have
degree at most four, including the possible term \(-T^4M^2b\).
Since (7) only used affine changes, these bounds hold in the
original input coordinates as well.

Combining (12)--(13) proves the promised certificate:
\[
\boxed{\ \deg\pi\le2\ \Longrightarrow\quad
\deg F\le2,\quad \deg F^{-1}\le4,\quad
F_4=s,\quad E(F_1)=E(F_2)=E(F_3)=0.\ }
\tag{14}
\]
It is not an optimal-degree claim for every input.

## 4. Controls and precise limits

The nilpotent case need not be an affine-linear action. Take
\[
U_1=u_1+t^2,\qquad U_2=u_2+tu_1,\qquad
U_3=u_3+tu_2,\qquad s=t.
\tag{15}
\]
The inverse is
\[
u_1=U_1-t^2,\quad
u_2=U_2-tU_1+t^3,\quad
u_3=U_3-tU_2+t^2U_1-t^4.
\]
Transporting \(\partial_s\) gives the actual sliced polynomial LND
\[
E=\partial_t-2t\partial_{u_1}
 +(2t^2-u_1)\partial_{u_2}
 +(-u_2+tu_1-2t^3)\partial_{u_3}.
\tag{16}
\]
Its projection is \((U_1,U_2,U_3,0)\), of degree two.
The formulas prove actual inverse coordinates and local nilpotence;
no claim that the particular inverse degree four is unavoidable
for every other possible invariant generating set is made.

The original LND and slice matter when promoting (9) to coordinates.
For example the quadratic idempotent endomorphism of
\(\mathbb C[u,v,w,t]\) defined by
\[
\rho(u)=u(1+t),\qquad \rho(v)=v,\qquad
\rho(w)=w,\qquad \rho(t)=0
\tag{17}
\]
has polynomial image abstractly, but \((u(1+t),v,w,t)\)
is not a coordinate system: its Jacobian is \(1+t\), a nonunit.
It cannot be a slice projection with kernel \(tB\), since that
would give \(E(t)\ne0\) constant while factorial closure of
\(\ker E\) applied to \(u(1+t)\) would give \(E(t)=0\).
Thus the graph-image argument alone is not an ambient-coordinate
criterion for an arbitrary retract.

Finally, even a constant translation can have arbitrarily large
projection degree when its supplied slice varies. For
\(E=\partial_t\) and \(s=t+u^d\), the projection is
\((u,v,w,-u^d)\). Its degree is \(d\), despite coefficient
degree zero and coordinate nilpotence order two. This is not a
cancellation counterexample. It shows why the slice-degree input
in (4) cannot simply be omitted for the displayed projection.

The universal missing step remains an actual coordinate certificate
for arbitrary projections of higher degree, or a justified change
of slice and frame placing them in a recognized class. Neither (4),
the retraction identity, the automatic rank-three Jacobian, nor
the quadratic classification supplies such a reduction.

## 5. Deduplication and evidence scope

The slice retraction, its four generators, and the on-slice tangent
projector are inherited from passes22 and26. The
[retained retract audit](literature-scope-pass38.md), Sections 2--3,
already distinguishes dimension restrictions and proves separate
single-image and binomial-image criteria. No sparse-image hypothesis
is assumed here. The older quadratic-slice recognition is explicitly
credited above; (14) adds an elementary quantitative normal form.

A bounded primary search located Liu and Sun's related
[*A class of retracts of polynomial algebras*](https://doi.org/10.1016/j.jpaa.2017.04.009),
whose publisher abstract concerns sparse homogeneous parts.
The complete theorem and proof were not retrieved in this pass,
so no precise comparison or theorem application is inferred from
that abstract. Every algebraic step used here is proved above.
No historical novelty claim is made.

This note records a written conditional certificate and exact
hand-verified controls. It introduces no numerical method, regression
claim, human expert review, proof-assistant certificate, shared metadata
edit, or change to frozen passes through73.
