# Integral vanishing cycles leave finite torsion models

The vanishing-cycle decomposition and exact sequence (E) give stronger
local restrictions than the earlier Gysin--Leray order formula. They do
not, by themselves, eliminate finite torsion. Explicit nonzero finite
groups satisfy the checked identities, including change-of-coefficient
constraints. None of these formal data is asserted to come from a
polynomial with all fibers smooth and rationally acyclic.

Let \(G:\mathbb C^3\to\mathbb C\) be nonconstant, and assume every fiber
is smooth and rationally acyclic. For a general fiber \(Y\), set
\[
A=H_1(Y;\mathbb Z),\qquad
A_i=H_1(G^{-1}(b_i);\mathbb Z),
\]
where \(b_1,\ldots,b_s\) are the bifurcation values. If there are no
bifurcation values, the locally trivial fibration over the contractible
base \(\mathbb C\) already makes \(Y\) contractible. Assume \(s\geq1\).

All these groups are finite. A smooth affine surface has a finite CW
model of dimension at most two, so rational acyclicity gives
\[
H_0=\mathbb Z,\quad H_1\text{ finite},\quad H_j=0\quad(j\geq2).
\tag{1}
\]
Integral Poincaré duality consequently gives
\[
H_c^3(G^{-1}(b_i);\mathbb Z)=A_i,
\qquad H_c^2(G^{-1}(b_i);\mathbb Z)=0.
\tag{2}
\]
In particular, ordinary \(H^1=0\) must not be substituted for the
possibly nonzero group \(H_c^3\).

## 1. The exact local identities

Choose a star of paths to the bifurcation values and let \(m_i\) denote
the resulting monodromy on \(A\). Dimca--Némethi supply a direct sum
and the weak Picard relation
\[
A=\bigoplus_{i=1}^s V_i,
\qquad \operatorname{im}(m_i-1)\subseteq V_i.
\tag{3}
\]
Here \(V_i=V_{1,i}\) is the degree-one vanishing-cycle group.[^dn]

Their exact sequence (E), in general homological degree \(q\), is
\[
0\longrightarrow\operatorname{im}(m_{q,i}-1)
\longrightarrow V_{q,i}
\longrightarrow\widetilde H_c^{5-q}(G^{-1}(b_i);\mathbb Z)
\longrightarrow\ker(m_{q-1,i}-1)\longrightarrow0.
\tag{4}
\]
Use \(q=2\). By (1), \(H_2(Y)=0\), so both \(V_{2,i}\) and the first
group vanish. The compact-support degree is three, where no reduced-top
convention is involved. Equation (2) therefore proves
\[
\boxed{A_i\cong\ker(m_i-1).}
\tag{5}
\]

The earlier [Gysin--Leray calculation](all-fiber-torsion-constraint.md)
gives, in homological group orders,
\[
\prod_i|A_i|=|A|^{s-1}.
\tag{6}
\]
That calculation originally uses \(H^2(Y;\mathbb Z)\). Since
\(H_1(Y;\mathbb Z)=A\) is finite and \(H_2(Y;\mathbb Z)=0\),
the universal coefficient theorem identifies this cohomology group
with \(\operatorname{Ext}^1(A,\mathbb Z)=
A^\vee=\operatorname{Hom}(A,\mathbb Q/\mathbb Z)\). In particular
its order is \(|A|\), so the orders in (6) are unchanged.

By (5),
\[
\prod_i|\operatorname{im}(m_i-1)|
=\prod_i\frac{|A|}{|A_i|}=|A|.
\]
The direct sum in (3) also gives \(\prod_i|V_i|=|A|\). Each image is a
subgroup of its corresponding \(V_i\), so equality of these products
forces equality in every component. Hence
\[
\boxed{\operatorname{im}(m_i-1)=V_i,
\qquad 0\longrightarrow A_i\longrightarrow A
\xrightarrow{\ m_i-1\ }V_i\longrightarrow0.}
\tag{7}
\]
The kernel identification depends on the chosen transport paths, as
does (3). These are finite-group identities, not just rank equalities.
The argument uses (4) only in degree two, avoiding the source's
reduced-top compact-support notation in degree one.

## 2. The global constraint is compatible with these local sequences

Define
\[
d:A^s\longrightarrow A,
\qquad d(a_1,\ldots,a_s)=\sum_i(m_i-1)a_i.
\]
The images are the independent direct summands \(V_i\), so (7) gives
\[
0\longrightarrow\bigoplus_i A_i
\longrightarrow A^s\xrightarrow{d}A\longrightarrow0.
\tag{8}
\]
Taking the exact character dual yields
\[
0\longrightarrow A^\vee
\longrightarrow(A^\vee)^s
\longrightarrow\bigoplus_iA_i^\vee\longrightarrow0.
\tag{9}
\]
The first map agrees, up to invertible changes in its components,
with the graph cochain differential for the cohomology monodromy
\(M_i=(m_i^{-1})^\vee\). Indeed, replacing \(m_i^\vee-1\) by
\((m_i^{-1})^\vee-1\) multiplies that component by an automorphism.
Thus (9) reproduces both the zero invariant subgroup and the full
cokernel group in the earlier Gysin--Leray constraint.

This also explains why zero invariants in cohomology do not automatically
mean zero common fixed points in homology. Cohomological invariants
annihilate the sum of the images \(\operatorname{im}(m_i-1)\); they
need not be the dual of the intersection of the kernels.

There is a further tube calculation. With \(E_i=G^{-1}(D_i)\), the star
excision construction identifies \(H_2(E_i,Y)\) with \(V_i\), with its
boundary map the inclusion in (3); the other reduced relative degrees
vanish. The pair sequence gives
\[
H_1(E_i;\mathbb Z)\cong A/V_i,\qquad
H_j(E_i;\mathbb Z)=0\quad(j\geq2).
\tag{10}
\]
The special-fiber group in (5) and the tube group in (10) have the same
order. A canonical isomorphism between them has not been established
here. Smoothness of an affine polynomial map does not make its tubes
proper fibrations; a deformation retraction of the tube onto the
special fiber must not be assumed.

## 3. One exceptional value still permits nonzero torsion

Take the formal data
\[
s=1,\qquad A=\mathbb Z/3,\qquad V_1=A,
\qquad m_1=-1,\qquad A_1=0.
\tag{11}
\]
Then \(m_1-1=-2\) is an automorphism. Equations (3), (5), (7),
(8), and (9) all hold. The tube group (10) is zero. The monodromy at
infinity is \(-1\), and its fixed subgroup is zero, agreeing with
the common-invariant identity of Dimca--Némethi Theorem 3.1.

The model also respects Corollary B in each relevant degree. In degree
one, its premise of identity monodromy fails, as does the conclusion
that \(A=0\). In degree two, the generic second homology and special
\(H_c^3\) both vanish, and \(m_1-1\) has zero kernel. The higher
groups involved vanish.

The same construction works with \(A=\mathbb Z/d\) for every odd
\(d>1\). Even torsion is not automatically excluded by the abstract
identities either. For example, on \(A=(\mathbb Z/2^e)^2\), take
\[
m_1=\begin{pmatrix}0&-1\\1&-1\end{pmatrix}.
\]
It has order three, and both its determinant and
\(\det(m_1-1)=3\) are units modulo \(2^e\). Again set \(V_1=A\)
and \(A_1=0\).

## 4. A compatible two-value model

The constraints are not restricted to a one-value pattern. Over
\(\mathbb F_3\), take
\[
A=\mathbb F_3^2=V_1\oplus V_2,
\qquad V_1=\mathbb F_3e_1,\quad V_2=\mathbb F_3e_2,
\]
and
\[
m_1=\begin{pmatrix}2&1\\0&1\end{pmatrix},\qquad
m_2=\begin{pmatrix}1&0\\1&2\end{pmatrix}.
\tag{12}
\]
Both are involutions. Their differences from the identity have images
\(V_1,V_2\), respectively, and both have kernel
\(L=\{(t,-t):t\in\mathbb F_3\}\). Set \(A_1=A_2=L\).
All local exact sequences hold, and \(|A_1||A_2|=9=|A|\).

The global monodromy is
\[
M_\infty=m_2m_1=\begin{pmatrix}2&1\\2&0\end{pmatrix},
\qquad\ker(M_\infty-1)=L.
\]
Thus its fixed subgroup is exactly the common homology invariant
subgroup, as required by Theorem 3.1. The cohomology invariant subgroup
is zero, and the graph cohomology cokernel is \(\mathbb F_3^2\),
matching \(A_1^\vee\oplus A_2^\vee\). In Corollary B's degree-two
test, both the special-group vanishing condition and the global
kernel-vanishing condition fail; there is no contradiction.

This example illustrates why one must not infer zero homology
invariants from the previously proved zero cohomology invariants.

## 5. Changing coefficients does not remove these examples

Integral \(H_2(Y)=0\) does not mean that its mod-\(p\) version is zero.
The universal coefficient theorem gives
\[
H_1(Y;\mathbb F_p)=A\otimes\mathbb F_p,
\qquad H_2(Y;\mathbb F_p)=A[p].
\tag{13}
\]
The same formulas hold for each \(A_i\). Thus the degree-two Tor
contribution must be retained when changing coefficients in the
vanishing-cycle decomposition or in (4).

For the one-value model (11), the only prime to check is three.
Both positive mod-three groups in (13) are \(\mathbb F_3\), and
monodromy acts by \(-1\) on both. Their difference operators remain
invertible. The special fiber has zero reduced mod-three groups, so
the degree-one and degree-two image terms in (4) are isomorphisms,
and the subsequent kernel terms vanish. At other primes all reduced
fiber groups vanish. The even-torsion model works the same way at two.

For (12), in characteristic three both groups in (13) are
\(\mathbb F_3^2\) with the displayed matrices. The degree-two
vanishing groups are copies of the respective lines \(V_i\), coming
from Tor. The degree-three specialization term is
\(H_c^2(G^{-1}(b_i);\mathbb F_3)=A_i[3]\), matching the kernel of the
degree-two monodromy difference. The remaining terms of (4) also have
the specified images and kernels. At other primes the reduced groups
vanish. Thus the formal examples are not defeated by simply repeating
the exact sequence with prime-field coefficients.

## 6. What has and has not been settled

The established new restrictions are the local identities (5)--(7),
their relation to the global cochain complex, and the tube group (10).
The examples satisfy these identities and the checked monodromy
conditions, while having \(A\ne0\). They are formal homological data.
No smooth algebraic surface fibration, polynomial map, or geometric
specialization realizing them has been constructed.

Exact finite enumeration checked the odd cyclic models for orders
\(3,5,7,9,15,25\), the even models for \(e=1,\ldots,6\), and the
two-value matrices, their kernels, images, global fixed subgroup, and
dual graph differential. Those checks validate the finite examples,
not the applicability of the geometric theorems to an unrealized map.

Consequently these methods do not settle whether all-fiber smooth
rational acyclicity forces integral acyclicity. An additional geometric
constraint on torsion specialization or monodromy at infinity would
be needed to exclude the surviving data. No claim that the implication
is false, or that a particular polynomial realizes the models, is made.

## Source

[^dn]: Alexandru Dimca and András Némethi,
[*On the monodromy of complex polynomials*](https://arxiv.org/html/math/9912072),
Section 2.3 for the star decomposition, Lemma 2.4 and Section 2.5 for
the block form, Theorem 3.1 for global invariants, and equation (E)
in Section 3.3. The original PDF was also checked. All applications
above keep integral homology distinct from its cohomological dual.
