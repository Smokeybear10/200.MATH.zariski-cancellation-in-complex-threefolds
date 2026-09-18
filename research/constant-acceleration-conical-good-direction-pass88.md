# The conical speed branch supplies the original good last partial

In the actual three-good-coordinate, constant-acceleration setting,
a rank-two conical good-speed map forces the original last coordinate
partial to be good. This follows from the original nilpotent Jacobian,
not from an abstract parametrization of the cone. It also gives an exact
normal identity over the actual invariant plane. Neither statement by
itself meets the retained one-good-direction recognition hypotheses.

## 1. The unchanged actual hypotheses

Use the [invariant-plane lemma](constant-acceleration-invariant-plane-pass88.md).
In its notation,
\[
B=\mathbb C[x_1,x_2,x_3,z]=A[u],\qquad
Ex_i=b_i\in S=\mathbb C[s_1,s_2],\qquad
Ez=qu,\quad Eu=1,\quad q\in\mathbb C^*,
\qquad (b_1,b_2,b_3)S=S.
\tag{1}
\]
Here \(S=\ker(W|A)\) for an actual nonzero highest-adjoint LND
\(W\) with \(Wu=0\). The maps \(S\to A\to B\) are faithfully flat.
Write \(P=(b_1,b_2,b_3,qu)^t\) and let \(J\) be its Jacobian in
the four original coordinates. The actual flow identities give
\(J^4=0\), \(JP=qe_4\), and
\(\operatorname{ad}_E^j(T_i)(x)=(-1)^j j!J^j e_i\).

Assume throughout the new branch argument that the two columns
\(b_{s_1},b_{s_2}\) are independent over \(K=\operatorname{Frac}(B)\).
The word conical here means precisely the determinant condition
in (3). No classification of all speed maps is asserted.

The chain rule in the original coordinates gives
\[
J=U L,\qquad
U=\begin{bmatrix}
b_{s_1}&b_{s_2}&0\\
0&0&q
\end{bmatrix},\qquad
L=\begin{bmatrix}ds_1\\ds_2\\du\end{bmatrix},\qquad
\operatorname{rank}_K J=3,\quad
\operatorname{im}_K J=\operatorname{im}_K U.
\tag{2}
\]
The upper block has three rows. Both \(U\) and \(L\) have rank three:
the former uses the independent good-speed derivatives and \(q\ne0\);
the latter uses algebraic independence of \(s_1,s_2,u\) in
characteristic zero. Thus \(U\) is injective and \(L\) is surjective
over \(K\), proving the final assertions. This factorization concerns
the original Jacobian. It does not claim that nilpotence is preserved
by a nonlinear coordinate change.

## 2. Conicality makes the actual last partial good

The lower speed ranks can be separated exactly. If the derivative
matrix of \(b\) has rank zero, the \(b_i\) are complex constants.
Their unit row contains a nonzero constant, so an original linear
good coordinate is an \(E\)-slice and \(A\) is a polynomial three-ring.
If that derivative matrix has rank one, the same factorization has
\(\operatorname{rank}J=2\). Nilpotence in dimension four then gives
\(J^3=0\), whence \(qJ^2e_4=J^3P=0\). Thus the original last
partial is good also in the rank-one case, without a conical argument.
No recognition conclusion for that whole rank-one case is asserted.

Return now to the rank-two hypothesis of (2).
Suppose
\[
\Omega:=\det[b,b_{s_1},b_{s_2}]=0.
\quad\text{Then}\quad
P\in\operatorname{im}_K J,\qquad
0=J^3P=qJ^2e_4,\qquad
\operatorname{ad}_E^2(\partial_z)=0.
\tag{3}
\]
Indeed \(b\) belongs to the span of its two independent derivative
columns. Equation (2) then puts \(P=(b,qu)^t\) in the image of \(J\).
If \(P=Jv\), nilpotence gives \(J^3P=J^4v=0\). The relation
\(JP=qe_4\) and the actual adjoint formula give the remaining
equalities. Division here is only by the nonzero complex number \(q\).

If \(Je_4=0\), all \(b_i\) and \(u\) are independent of the original
\(z\). The actual good-coordinate subring is then stable under \(E\),
and the final recognized branch of the invariant-plane lemma applies.

Otherwise put \(T=\partial_z\) and \(Q=[E,T]\). Then
\[
Q(x)=-Je_4\ne0,\qquad
[E,Q]=0,\qquad Q(P)=0,\qquad Qu=Qb_i=0,\qquad
Q\in\operatorname{LND}(B),\qquad
\ker(Q|A)=S.
\tag{4}
\]
For local nilpotence, use the actual conjugation
\(\epsilon\exp(\epsilon^{-1}E)T\exp(-\epsilon^{-1}E)
=\epsilon T+Q\).
It is an LND on the Laurent extension, preserves \(B[\epsilon]\),
and specializes to \(Q\), exactly as in the retained highest-field
proof. The equalities \(Q(P)=0\), \(Qu=0\), and \(Qb_i=0\)
follow from \(J^2e_4=0\).

A nilpotent four-by-four matrix of rank three has one Jordan block.
Hence \(\ker_KJ=\operatorname{im}_KJ^3\) is one-dimensional.
Both \(Q(x)\) and the previously chosen nonzero highest column \(W(x)\)
lie on that line. The two derivations are nonzero rational multiples,
so they have the same kernels on \(B\) and on \(A\). This proves the
last equality in (4); it does not identify their replica factors.

## 3. The actual localized determinant and normal identity

For clarity, the Jacobian unit used in the complementary generic-degree
argument is an actual unit, independent of both fiber variables.
Choose a local slice for \(W|A\): after inverting some nonzero \(f\in S\),
one has \(A_f=S_f[v]\). This is obtained by choosing an element with
nonzero invariant first \(W\)-image and dividing by that image.
Consequently \(B_f=S_f[u,v]\), while also being the localization of
the original polynomial four-ring.

Set \(a=x_{\rm tr}-bu\) and \(r=z-qu^2/2\), both in \(A_f\).
The two presentations give bases of the same module of differentials
over \(\mathbb C\). Therefore, with column order \(u,s_1,s_2,v\),
\[
\mathcal J=
\det\begin{bmatrix}
b& a_{s_1}+u b_{s_1}&a_{s_2}+u b_{s_2}&a_v\\
qu&r_{s_1}&r_{s_2}&r_v
\end{bmatrix}
\in B_f^*=S_f^*,\qquad
[u^3]\mathcal J=-q\det[b_{s_1},b_{s_2},a_v]=0.
\tag{5}
\]
This does not infer invertibility from a proposed determinant. It uses
the two already valid algebra presentations to obtain the unit first.
In particular its image in \(\operatorname{Frac}(S)\) is nonzero and
has no \(u\)- or \(v\)-dependence.

If, over an algebraic closure of \(\operatorname{Frac}(S)\), some
value \(v_0\) makes all three \(a_{i,v}\) vanish, the last column at
that value is \((0,0,0,r_v)^t\). The same nonzero unit forces
\(r_v(v_0)\ne0\). Its coefficient of \(u^2\) is then
\(r_v(v_0)\Omega\), so \(\Omega=0\).
No differentiation of the chosen root \(v_0\) is involved: the
already computed polynomial determinant identity is specialized.
This is the critical-point implication in Geometry's separate
generic-degree argument, not an additional polynomial Lüroth claim.

In the conical branch take the nonzero polynomial row
\(N=b_{s_1}\mathbin{\times}b_{s_2}\in S^3\). Then
\[
N\cdot b=0,\qquad
c_0:=N\cdot x_{\rm tr}\in S,\qquad
c_0\in(N_1,N_2,N_3)S,\qquad
N\cdot\bigl(x_{\rm tr}-\alpha(S)\bigr)=0
\quad\text{for some }\alpha\in S^3.
\tag{6}
\]
Indeed \(E(c_0)=0\). The highest column \(W(x)\) lies in
\(\operatorname{im}J\); by (2), its transverse column is a linear
combination of \(b_{s_1},b_{s_2}\). Hence \(W(c_0)=0\), which
places \(c_0\) in the actual common kernel \(S\).
It belongs to the extended ideal \((N_i)B\) by its displayed
expression. Faithful-flat contraction gives the ideal membership
in \(S\), and choosing its coefficients proves the last identity.
No unit-ideal property of this normal row is inferred.

## 4. A conditional two-generator consequence, and the exact remaining gates

If some polynomial normal row \(N\in S^3\) satisfying (6) additionally
generates the unit ideal, its kernel is a projective rank-two module.
The unit speed column \(b\) is a direct summand of that kernel:
restrict any row \(\ell\) with \(\ell b=1\). The complementary
rank-one projective module is free over the polynomial plane \(S\),
by the same Quillen--Suslin input already used in the invariant-plane
lemma. Choose a generator \(V\) and a column \(U_0\) with \(NU_0=1\).
The columns \(b,V,U_0\) form a basis of \(S^3\). Thus, conditionally,
\[
x_{\rm tr}=b\sigma+VY+U_0c_0,\qquad
E\sigma=1,\quad EY=0,\qquad
A=S[Y,c],\qquad
c=z-qu\sigma+\frac q2\sigma^2.
\tag{7}
\]
The first equality recovers actual elements by the inverse matrix.
It gives the subalgebra equality \(B=S[\sigma,Y,z]\), since
\(c_0\in S\). Applying the actual slice evaluation at \(\sigma=0\)
then gives the last algebra-generation equality. It is not an
assertion of algebraic independence over \(S\), an ambient coordinate
change, or a free intrinsic action. The unimodular-normal premise
has not been established in this note.

The [supplied-good recognition theorem79](nice-good-direction-recognition-pass79.md)
requires all four original coordinates to satisfy \(E^2x_i=0\).
It therefore cannot be applied here, since \(E^2z=q\ne0\).
The older [one-good-output theorem41](three-output-cubic-closure-pass41.md),
Section 1, and [rational two-direction theorem69](rational-two-direction-recognition-pass69.md)
instead require a particular two-output nice symmetry fixing an
actual coordinate plane. The present \(S\)-plane and the highest
field do not supply that actual-coordinate-plane premise.

Also, \(Q(P)=0\) does not by itself give \(Q^2(x_i)=0\),
\(T(S)\subset S\), a slice for \(Q\), or a unit normal ideal.
No such step is used above. The result is an exact branch reduction
and normal identity, with a separately labeled conditional generation
statement. It does not recognize the remaining conical branch or
prove unrestricted cancellation.

General supplied and independently reconstructed the original
\(J=UL\) implication and checked the precise older theorem gates.
Geometry supplied the cubic determinant coefficient and the normal
identity outline; General reconstructed both from the actual
localized coordinates. Root requested this bounded consequence.
The source inputs are the inherited invariant-plane and module
theorems, not newly audited primary-paper proofs. No numerical
method, integration capture, or modification of pass87 or older
files is added here.
