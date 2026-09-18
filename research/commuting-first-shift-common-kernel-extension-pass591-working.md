# Actual first-shift common-kernel extensions need not have an affine slice

## 1. The exact obstruction and its scope

Consider a sliced LND \(E\) of an actual polynomial fourfold, with
an all-positive coordinate frame and its Euler field weighted by the
actual \(E\)-degrees. Even if the homogeneous components of \(E\)
commute and the Euler shift is exactly one, the following proposed
reduction is false. After selecting a negative component with an
actual coordinate slice \(t\), write
\[
 B=R[t],\qquad R\cong\mathbb C^{[3]},\qquad
 E=\delta+g\partial_t,
 \qquad \delta\in\operatorname{LND}_{\mathbb C}(R),\quad g\in R.
\tag{1}
\]
Sliceness and the actual degree condition
\(\deg_\delta g=\deg_Et-1\) do not force
\(g\in\mathbb C^*+\delta(R)\). There need not even be any
\(E\)-slice affine in \(t\), allowing arbitrary polynomial
coefficients in \(R\).

The example below has minimum \(t\)-degree of a slice exactly two.
It has an explicit polynomial kernel and an actual invariant
coordinate. It therefore obstructs this same-frame scalar-gauge
reduction, not recognition, cancellation, or a theorem restricted
to a rank-three base derivation.

The underlying non-affine-slice example was already recorded in
`commuting-coordinate-partial-pass.md`, Section 2. That whole source
was read before this construction. The point checked here is its
applicability to the additional actual-weight, first-shift and
commuting-component requirements. No novelty is claimed for the
older example, and no new recognition theorem is inferred from it.

## 2. Actual frame, full slice and full inverse

In the actual polynomial ring \(B=\mathbb C[x,y,z,t]\), set
\[
 E=x^2\partial_y+(1+xy)\partial_t.
\tag{2}
\]
This is a locally nilpotent derivation. It kills \(x,z\), and on
the other generators its full nonzero iterates are
\[
 E(y)=x^2,\qquad E(t)=1+xy,\qquad E^2(t)=x^3.
\tag{3}
\]
The next respective iterates vanish. Local nilpotence on generators
implies local nilpotence on their polynomial ring by the iterated
product rule.

Use the actual linear coordinate frame
\[
 X_1=t,\quad X_2=x+t,\quad X_3=y+t,\quad X_4=z+t.
\tag{4}
\]
Its entire inverse is
\(t=X_1,x=X_2-X_1,y=X_3-X_1,z=X_4-X_1\).
For every \(i\), \(E^2X_i=x^3\ne0\) and \(E^3X_i=0\).
Thus every actual degree is exactly two, and the actual Euler field is
\[
 d=(2,2,2,2),\qquad
 D=2\sum_iX_i\partial_{X_i}
  =2(x\partial_x+y\partial_y+z\partial_z+t\partial_t).
\tag{5}
\]
This equality uses the complex linear coordinate map (4). The weights
are not a separately assigned convenient grading.

Here are a whole invariant and a whole slice:
\[
 \begin{aligned}
 q&=x^2t-y-\frac12xy^2,\\
 u&=t+\frac12y^3+\frac18xy^4-xyt
      -\frac12x^2y^2t+\frac12x^3t^2.
 \end{aligned}
\tag{6}
\]
Direct application of (2) gives \(Eq=0\) and \(Eu=1\).
These identities retain every term in (6), including the quadratic
term in \(t\).

The full inverse of \((x,y,z,t)\mapsto(x,q,z,u)\) is polynomial.
Define \(v=xu-q^2/2\) in the target ring. Then
\[
 x=x,\qquad z=z,\qquad
 y=xv-q,\qquad t=u-qv+\frac12xv^2,
 \qquad v=xu-q^2/2.
\tag{7}
\]
Substitution in both directions gives the identity. One way to verify
the cancellation is to expand (6) and obtain
\(2xu=2xt+q^2-y^2\), then use the first equation of (6).
The displayed inverse (7) contains no division by \(x\), so it
remains an identity on \(x=0\). The Jacobian of (6), in the ordered
coordinates \((x,y,z,t)\) and \((x,q,z,u)\), is \(-1\).

Consequently the actual whole-ring statements are
\[
 B=\mathbb C[x,q,z,u],\qquad E=\partial_u,
 \qquad A=\ker E=\mathbb C[x,q,z].
\tag{8}
\]
Neither the polynomial kernel nor the coordinateness of this slice
is inferred from an embedding of a single orbit.

## 3. Exact first shift and commuting homogeneous components

Transporting the entire Euler derivation (5) through (6)--(7) gives
\[
 \begin{aligned}
 D(x)&=2x,&D(z)&=2z,\\
 D(q)&=2q-2xq^2+4x^2u,&
 D(u)&=(2+4xq)u-2q^3.
 \end{aligned}
\tag{9}
\]
These identities can also be checked by the four complete Euler
eigen-equations for the inverse coordinates in (7).
For the \(E\)-filtration \(\deg_E=\deg_u\) on \(A[u]\),
horizontal coefficients in (9) have degree at most one and the
vertical coefficient has degree one. The whole derivation therefore
raises degree by at most one. Equality holds on \(q\), since
\(q\in A\) and \([u]D(q)=4x^2\ne0\). Its exact shift is one.

In particular, the full commutator and the corrected recovery killing
the supplied slice \(u\) are
\[
 [E,D]=4x^2\partial_q+(2+4xq)\partial_u,
 \qquad [E,[E,D]]=0,
 \qquad \widetilde N=4x^2\partial_q.
\tag{10}
\]
This is a direct whole-ring calculation. No general first-shift
recognition theorem is used.

In the original coordinates, define
\[
 L=\partial_t,\qquad
 P=x^2\partial_y+xy\partial_t,
 \qquad E=L+P.
\tag{11}
\]
Both fields are LNDs: \(L\) is a coordinate partial, and
\(P(x)=P(z)=0,P(y)=x^2,P(t)=xy,P^2(t)=x^3,P^3(t)=0\).
The exact brackets for (5) are
\[
 [L,P]=0,\qquad [D,L]=-2L,\qquad [D,P]=2P,
 \qquad [E,D]=2L-2P.
\tag{12}
\]
Thus (11) is the complete homogeneous decomposition of this same
actual \(E\), not a decomposition from an unrelated grading.
The two components commute, have distinct weights, and generate a
commutative additive action normalized by the actual Euler torus.
The complex Lie algebra generated with \(D\) is the three-dimensional
span of \(D,L,P\).

The negative component \(L\) has the actual source-coordinate slice
\(t=X_1\). Its quotient and the other restriction are exactly
\[
 R=\ker L=\mathbb C[x,y,z],\qquad
 \delta=P|_R=x^2\partial_y,
 \qquad g=E(t)=1+xy.
\tag{13}
\]
There is just one nonzero restricted derivation, so the common-kernel
alternative is genuine. Its primitive factor is \(H=\partial_y\),
with \(\delta=x^2H\) and \(x^2\in\ker H=\mathbb C[x,z]\).
All the required component commutation conditions hold, including
\(\delta(L(t))=\delta(1)=0\). Finally
\[
 \delta(g)=x^3\ne0,\qquad \delta^2(g)=0,
 \qquad \deg_\delta(g)=1=\deg_E(t)-1.
\tag{14}
\]
This checks the particular actual-weight constraint that an arbitrary
extension with a freely assigned weight need not satisfy.

## 4. No scalar gauge and no affine-in-t slice

For any \(Q\in R\), the condition
\(E(t-Q)\in\mathbb C^*\) is equivalent to
\[
 1+xy-c=x^2\partial_y Q\qquad\text{for some }c\in\mathbb C^*.
\tag{15}
\]
Reducing modulo \(x\) forces \(c=1\). Reducing the resulting
identity modulo \(x^2\) would give \(xy=0\) in
\(\mathbb C[x,y,z]/(x^2)\), which is false. Hence no such
\(Q,c\) exist. This proves in particular that
\(g\notin\mathbb C^*+\delta(R)\).

The stronger affine assertion allows both coefficients to be arbitrary
elements of \(R\). Suppose \(s=\alpha t+\beta\),
\(\alpha,\beta\in R\), satisfied \(E(s)=1\). Comparing
coefficients of \(t\) gives \(x^2\partial_y\alpha=0\), hence
\(\alpha\in\mathbb C[x,z]\). The remaining equation is
\[
 x^2\partial_y\beta+\alpha(1+xy)=1.
\tag{16}
\]
Modulo \(x\), \(\alpha(0,z)=1\). Write
\(\alpha=1+x\alpha_1(z)\pmod{x^2}\). Equation (16) modulo
\(x^2\) now forces \(\alpha_1(z)+y=0\), impossible because
\(y\) is independent of \(z\). This proof includes \(\alpha=0\),
which was already excluded by reduction modulo \(x\).

The slice (6) has exact \(t\)-degree two, since its leading
coefficient is the nonzero polynomial \(x^3/2\). The failure of
(16) for every affine polynomial therefore proves that the minimum
\(t\)-degree of a slice is exactly two. This is a polynomial-ring
claim, not an assertion after deleting the fiber \(x=0\).

## 5. What the example leaves open

This example satisfies the actual positive-degree presentation,
the exact first-shift condition, pairwise commuting homogeneous LND
components, the actual negative-component coordinate quotient, and
the relation (14). It disproves an automatic scalar-gauge or
affine-in-the-selected-coordinate slice conclusion under those
hypotheses, even with arbitrary coefficients allowed in the proposed
affine slice.

It does not obstruct recognition. The full invariant-coordinate
inverse (7)--(8) recognizes the kernel directly. Also \(x\) is an
actual invariant coordinate in the source frame (4), namely
\(x=X_2-X_1\). Thus the common-coordinate alternative of589 applies
independently. The base derivation in (13) has rank one, not rank
three. No claim concerning all rank-three common-kernel extensions
follows from this countercontrol.

The prohibition is tied to the selected \(R[t]\) presentation.
Replacing \(t\) by the actual slice \(u\) in (6) is a valid
polynomial coordinate change, but it mixes the base and extension
variables and has \(t\)-degree two. The example does not forbid
such changes, other recognition methods, a finite algorithm allowing
them, or cancellation. It does not assert that a failure of the
affine test implies a nonpolynomial kernel.

Fresh unsaved algebra reconstructs both full inverse orders, the
Jacobian, the complete slice and invariant equations, every original
coordinate's exact \(E\)-degree, the whole transported Euler field,
and all spectral and recovery brackets. The obstruction in Section 4
is an exact coefficient argument for arbitrary \(\alpha,\beta,Q\),
not a finite coefficient search. Earlier scratch comparisons were
replaced by fully expanded polynomial residual checks before the
final verification.

No external classification theorem is required for this explicit
control. No saved checker was executed, imported or compiled; no
canonical file was edited, and no unfinished source was read. Final
hold is reported separately only after a complete author EOF reread
and exact hash.
