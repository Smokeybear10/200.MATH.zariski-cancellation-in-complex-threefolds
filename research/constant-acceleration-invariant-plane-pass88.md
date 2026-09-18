# A highest adjoint gives an actual invariant plane and a unit velocity row

The three-good-coordinate constant-acceleration setting supplies a
nonzero LND of the original kernel which fixes all three good speeds.
The retained intrinsic-quotient theorem then places those speeds in
an actual polynomial invariant plane, where they generate the unit
ideal. This gives an exact relative generating set, but neither a
coordinate change from a module completion nor a free intrinsic
action is asserted.

## 1. An actual highest field on the original kernel

Retain the hypotheses of the
[stronger-frame proof](constant-acceleration-three-good-frame-pass87.md):
\[
B=\mathbb C[x_1,x_2,x_3,z]=A[u],\qquad A=\ker E,
\qquad E(x_i)=b_i\in A\ (i\le3),\qquad
E(z)=qu,\qquad E(u)=1,\qquad q\in\mathbb C^*.
\tag{1}
\]
Here E is an actual globally sliced LND and all four displayed
coordinates are original polynomial coordinates. Write
P=(b_1,b_2,b_3,qu) transposed and J=Jac(P). The actual flow inverse
and differentiation of E(P)=q e_4 give
\[
J^4=0,\qquad JP=qe_4,\qquad E(J)=-J^2,
\qquad \operatorname{ad}_E^j(T_i)(x)=(-1)^j j!J^j e_i.
\tag{2}
\]
The complete derivation is in the stronger-frame proof; it uses the
actual identity det(I+tau J)=1, not merely a formal nilpotent matrix.

Choose n maximal with J to the n nonzero. Since JP is nonzero,
n is one of 1,2,3. Choose i with J to the n e_i nonzero, and take
the actual highest adjoint W=ad_E to the n of T_i. Then
\[
W(x)=(-1)^n n!J^n e_i\ne0,\qquad
[E,W]=0,\qquad W(P)=0,\qquad
W(u)=0,\qquad W(b_i)=0\ (i\le3).
\tag{3}
\]
Indeed the coefficient column of W(P) is J W(x), which is zero
by maximality of n. Its fourth component is q W(u), and q is a
nonzero constant. The commutator follows either from the next
adjoint or directly from E(J to the n)=-n J to the n+1.

The local nilpotence of W requires the actual partial T_i. Extend
E and T_i to kill an indeterminate epsilon. In the Laurent ring
B[epsilon,epsilon inverse] form
\[
\mathcal T_\epsilon
 =\epsilon^n\exp(\epsilon^{-1}E)T_i\exp(-\epsilon^{-1}E)
 =\sum_{j=0}^n\frac{\epsilon^{n-j}}{j!}
       \operatorname{ad}_E^j(T_i),
\qquad \mathcal T_0=W/n!.
\tag{4}
\]
Conjugation preserves local nilpotence. Multiplication by epsilon
to the n also preserves it because epsilon is invariant. The finite
right side shows that this derivation preserves B[epsilon]. That
restriction is an LND: every element is killed by a finite iterate
in the Laurent ring, and the polynomial ring injects into it.
Specializing epsilon to zero gives an LND, proving the claim for W.
This is the retained highest-coefficient degeneration mechanism,
not a new general theorem about arbitrary polynomial vector fields.

Commutation with E makes W preserve A. Its restriction to A is a
nonzero LND, since otherwise W would kill both A and u and hence
all of B=A[u], contrary to (3). No primitive division is required.

## 2. The exact intrinsic quotient theorem applies

Set S=ker(W|A). The
[intrinsic-quotient-surface proof](intrinsic-quotient-surface-pass.md)
applies to the actual affine domain A, its cylinder A[u]=C to the
fourth, and its nonzero intrinsic LND W|A. It gives
\[
S\simeq\mathbb C^{[2]},\qquad
S\longrightarrow A\longrightarrow B=A[u]
\text{ are faithfully flat},\qquad
\ker(W|B)=S[u],\qquad b_1,b_2,b_3\in S.
\tag{5}
\]
For the last kernel equality, expand a polynomial in u and use
W(u)=0. The speed membership follows from (3) and b_i in A.

The source hypotheses are substantive. The cylinder makes Spec A
a smooth contractible affine threefold. Projection of its cylinder
restricts dominantly to a suitable affine linear three-plane,
verifying the domination hypothesis of Kaliman--Saveliev
Corollary 2.8(2). Their quotient conclusions, together with Lemma
2.1(1), yield the affine plane and nonempty curve fibers. The
retained proof obtains faithful flatness from those purely
one-dimensional fibers and miracle flatness for the smooth source
and smooth plane. Neither freeness of W nor reducedness, smoothness,
or connectedness of every fiber is assumed. The whole retained
written proof was read through EOF for this application; no fresh
full Kaliman--Saveliev paper-proof audit is claimed here.

## 3. The good-speed row is a unit row in this same plane

There is a direct proof which avoids the acceleration-integrality
results. If a closed point p of the original four-space satisfied
b_1(p)=b_2(p)=b_3(p)=0, its actual E-orbit would have constant
three good coordinates and last coordinate
z(p)+q u(p) tau+q tau squared/2. The distinct values
tau=-u(p)+1 and tau=-u(p)-1 give the same four coordinates.
This is impossible because u on that orbit has respective values
1 and -1, by E(u)=1. Thus no closed common zero exists. The
Nullstellensatz and faithful-flat ideal contraction in (5) prove
\[
(b_1,b_2,b_3)B=B,
\qquad (b_1,b_2,b_3)S=S.
\tag{6}
\]
This is a unit-ideal conclusion in the actual invariant plane,
not only a gcd conclusion. The orbit argument uses E and its
original slice; it says nothing about freeness of W|A.

## 4. Three relative generators, with a module completion only

Choose ell_i in S with sum ell_i b_i=1 and put
\[
y=\sum_{i=1}^3\ell_i x_i,\qquad E(y)=1,\qquad
h=u-y\in A,\qquad
a_i=x_i-b_i y\in A,\qquad
w=z-quy+\frac q2y^2\in A.
\tag{7}
\]
This y is another actual polynomial slice, not an asserted ambient
coordinate. Evaluation at y=0 in B=A[y] fixes A and S. Equivalently
it is the finite slice projection sum (-y) to the j E to the j/j!.
Applying it to the original four algebra generators proves the
exact relative generation statement
\[
A=S[a_1,a_2,a_3,w],\qquad
\sum_{i=1}^3\ell_i a_i=0,\qquad
w=\left(z-\frac q2u^2\right)+\frac q2h^2.
\tag{8}
\]
This does not assume that the displayed generators are independent.
At every closed point of Spec S, at least one ell_i remains nonzero,
by its scalar product with b. Thus its curve fiber is generated by
at most three elements after eliminating one a_i from (8). It is
still allowed to be a nonreduced or disconnected curve.

There is also a global three-generator conclusion. The split map
ell:S cubed to S has kernel a rank-two finitely generated projective
S-module. The Quillen--Suslin theorem applies because S is an actual
polynomial ring over C. Choose a basis v_2,v_3 of that kernel.
The matrix with columns b,v_2,v_3 is invertible; its inverse M has
first row ell. Define actual polynomials by
\[
M\in\operatorname{GL}_3(S),\qquad Mb=e_1,\qquad
\begin{pmatrix}\sigma\\A_1\\A_2\end{pmatrix}
 =M\begin{pmatrix}x_1\\x_2\\x_3\end{pmatrix},\qquad
E(\sigma)=1,\quad E(A_1)=E(A_2)=0.
\tag{9}
\]
The inverse matrix proves B=S[sigma,A_1,A_2,z] as an equality of
subalgebras, not a free polynomial presentation over S. The original
x_i are recovered over S, and S is already a subring of B, so this
algebra equality does not require an ambient matrix automorphism.
Evaluation at sigma=0 in the actual slice presentation A[sigma]
therefore gives
\[
c=z-qu\sigma+\frac q2\sigma^2\in A,\qquad
A=S[A_1,A_2,c].
\tag{10}
\]
This is the stronger relative generation observation independently
supplied by Geometry. The notation c here is a new invariant
generator, not a claim that sigma equals the original centered u.

For the module theorem, the original reference is
[Quillen, *Projective modules over polynomial rings*](https://doi.org/10.1007/BF01390008),
Inventiones Mathematicae 36 (1976), 167--171; its publisher metadata
was directly checked, but the original proof was subscription-only
in this access. The field case needed here is stated in the opening
paragraph and follows from Theorem 6, page 6, of
[Dicks, *Seminar on Quillen's proof of the Quillen--Suslin theorem*](https://arxiv.org/pdf/2112.02272).
That author proof write-up explicitly attributes the result to
Quillen's Theorem 4-prime and Suslin's Theorem 3. The complete
terminal statement and proof were read here; no full audit of the
original 1976 papers or all intermediate dependencies is claimed.
The only imported consequence is freeness of the displayed
finitely generated projective module over S=C to the second.

An invertible S-matrix is an invertible operation on a free module,
or on independent formal variables over S. It does not by that fact
give an ambient automorphism of B: the original x_i satisfy relations
over the embedded S, and the entries of the matrix are functions in
that same original ring. Its action on formal variables need not
preserve those relations while fixing S. The retained
[fiber-row control](constant-acceleration-fiber-row-pass87.md)
illustrates the general failure of this inference; it is not claimed
to be a counterexample satisfying every stronger hypothesis (1).
The valid outcome here is (7)--(10), not automatic coordinates or
freeness of the new intrinsic LND. Additional control of the actual
quotient fibers or their defining relations would still be needed
for such an endpoint.

## 5. A parallel highest column is already a recognized branch

There is one useful field-level dichotomy, also supplied by Geometry.
Suppose the first three coefficient entries of this nonzero W are
proportional to b over K=Frac(B). Write the full column as
\[
W(x)=\alpha P+\beta e_4,\qquad
0=J W(x)=\alpha q e_4+\beta J e_4.
\tag{11}
\]
If beta were zero, then alpha would be zero, contradicting W nonzero.
Otherwise e_4 is an eigenvector of J over K with eigenvalue
-alpha q/beta. Nilpotence forces that eigenvalue to vanish. Hence
alpha=0 and J e_4=0. In particular all b_i and u are independent
of the original z, and the actual good-coordinate three-ring
C[x_1,x_2,x_3] is stable under E.

The recognition gate is then exactly the one in Section 2 of the
[three-quasi-nice source audit](rank-one-quasi-nice-source-scope-pass85.md).
Its actual three-variable restriction is nice. The cited
Dasgupta--Gupta Theorem 3.1(i) supplies an invariant nonzero constant
linear form when the restriction is nonzero. If the restriction
were zero, any good coordinate would suffice. In either case the
form is an actual ambient invariant coordinate. The original slice
supplies regularity of A, so the cited Bhatwadekar--Gupta--Lokhande
Theorem 3.5 recognizes A as C cubed. This paragraph uses that
retained source-backed gate, which was reread for this application;
it is not a new primary-paper proof audit or an assumption that
the unknown base was polynomial.

Consequently, outside this already recognized branch, the transverse
highest column and the good-speed column are K-linearly independent.
This is a necessary distinction for further quotient-fiber work,
not freeness of W or a conclusion about the remaining fibers.

Root proposed the common-highest-field refinement and the invariant
plane application. Jet independently reconstructed the actual-ring
degeneration, the quotient hypotheses, the elementary orbit proof
of (6), and the relative slice projection (8). Geometry supplied
the stronger completion consequence (9)--(10) and dichotomy (11),
both independently reconstructed here. This note adds no
test method or run, does not edit pass87 or older artifacts, and
makes no unrestricted recognition or novelty claim.
