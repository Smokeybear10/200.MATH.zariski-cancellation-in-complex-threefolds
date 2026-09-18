# A whole height-one frame forces two intrinsic directions

There is a conditional improvement for the actual polynomial-cylinder
problem. If all four members of one genuine ambient coordinate-partial
frame have adjoint height at most one with respect to the slice action,
then the threefold has at least two independent intrinsic LNDs. In the
low-rank branch of the proof, its coordinate ring is already polynomial.

The existence of such a frame has **not** been proved from
\(A[s]\simeq\mathbb C^{[4]}\). The theorem therefore rules out one
precise configuration for a hypothetical intrinsic-rank-one candidate;
it does not rule out every such candidate or solve cancellation.
The homogeneous classification used below is an inherited primary
result, not a novelty claim for this investigation.

## 1. The conditional theorem uses an actual whole frame

Let
\[
B=A[s]=\mathbb C[x_1,x_2,x_3,x_4],\qquad E=\partial_s,
\qquad T_i=\partial_{x_i}.
\tag{1}
\]
The two displayed presentations are genuine polynomial-ring
presentations of the same ring. In particular \(E(s)=1\), while
the values \(T_i(s)\) are unrestricted.

**Theorem.** Suppose that
\[
[E,[E,T_i]]=0\qquad(1\le i\le4).
\tag{2}
\]
Then \(A\) admits two commuting LNDs independent over
\(\operatorname{Frac}A\). More precisely, put
\[
v=(E(x_1),\ldots,E(x_4))^{\mathsf t},\qquad
J=(\partial_{x_j}v_i)_{i,j},\qquad
q=\operatorname{rank}_{\operatorname{Frac}B}[\,v\mid J\,].
\tag{3}
\]
If \(q\le2\), then \(E\) kills a nonzero complex linear
form in the \(x_i\), and \(A\simeq\mathbb C^{[3]}\).
If \(q\ge3\), two of the first commutators restrict directly
to independent intrinsic LNDs.

Consequently, under the original cylinder hypothesis, an
intrinsic-rank-one candidate must satisfy
\[
\text{for every ambient polynomial coordinate frame, some }i
\text{ has }[E,[E,\partial_{x_i}]]\ne0.
\tag{4}
\]
This is a statement about every genuine frame in a hypothetical
rank-one candidate, not just an old invariant-plane embedding.

## 2. The first commutators descend directly

Set \(S_i=[E,T_i]\). Equation (2) gives \([E,S_i]=0\).
Applying \((\operatorname{ad}E)^2\) to
\([T_i,T_j]=0\) gives
\[
0=2[S_i,S_j],\qquad [S_i,S_j]=0.
\tag{5}
\]
Each \(S_i\) is locally nilpotent, including the possibility
\(S_i=0\). Here is a direct uniform-parameter proof, which avoids
assuming that arbitrary limits of LNDs are locally nilpotent.
For a fixed \(f\in B\), the polynomial
\(\exp(-tE)f\) has finitely many coefficients in \(B\).
Choose \(N\) so that \(T_i^N\) kills each coefficient.
Conjugation gives
\[
(T_i+tS_i)^Nf
=\exp(tE)T_i^N\exp(-tE)f=0.
\tag{6}
\]
Its coefficient of \(t^N\) is \(S_i^Nf\). This proves the
assertion for every \(f\), with a bound allowed to depend on \(f\).

Thus \(E,S_1,\ldots,S_4\) are commuting LNDs. Their complex
linear span is a finite-dimensional abelian Lie algebra consisting
entirely of LNDs. The commuting exponential flows give an actual
regular additive-group action. Its generic rank is exactly \(q\),
because the coefficient vector of \(S_i\) is the negative of the
\(i\)-th column of \(J\).

Because \([E,S_i]=0\), each \(S_i\) preserves
\(A=\ker E\). Its restriction \(\overline S_i\) is an LND,
and these restrictions commute. If \(q\ge3\), choose two
\(S_i,S_j\) which, together with \(E\), are independent over
\(\operatorname{Frac}B\). Their restrictions are independent
over \(\operatorname{Frac}A\). Indeed, a relation between the
restrictions would make the same fraction-field combination of
\(S_i,S_j\) kill \(A\). Any derivation of
\((\operatorname{Frac}A)(s)\) killing \(\operatorname{Frac}A\)
is a multiple of \(E\), contradicting the three-field
independence. This gives the required two intrinsic directions.

More generally, selecting \(q-1\) columns independent modulo
\(E\) gives \(q-1\) commuting independent restrictions when
\(q\ge2\). This direct descent is possible because every first
commutator centralizes \(E\). It needs neither a homogeneous-space
theorem nor the more general
[pass 35 group criterion](rank-one-cylinder-pass35.md).
No finite-closure claim for the original \(T_i\) is being used.

Here is an exact control on the strength of this descent. In the
actual coordinates \(x,y,z,w\), take
\[
E=\partial_w+x^2\partial_y+3x^2y\partial_z.
\]
Its slice is \(w\), and invariant coordinates are
\[
x,\qquad a=y-x^2w,\qquad
b=z-3x^2yw+\frac32x^4w^2.
\]
The inverse is \(y=a+x^2w\),
\(z=b+3x^2aw+\tfrac32x^4w^2\). Thus the example is a genuine
polynomial cylinder and \(\ker E=\mathbb C[x,a,b]\).
It satisfies (2), has \(q=3\), and its first commutators with
\(\partial_x,\partial_y\) restrict to
\[
-2x\partial_a-6xa\partial_b,\qquad -3x^2\partial_b.
\]
Their \((a,b)\)-coefficient determinant is \(6x^3\), so they
are generically independent and commute. Nevertheless both
vanish on \(x=0\), so neither has a slice and their values do
not form a tangent basis everywhere. The conclusion of the
high-rank branch concerns generic intrinsic rank, not global
freeness of these particular descended fields. The known
polynomial quotient in this control of course has other free
coordinate partials.

It remains to treat \(q\le2\). The next lemma is independent
of the intrinsic-rank-one hypothesis.

## 3. A low projective-rank lemma

**Lemma.** Let \(E\ne0\) be an LND on
\(\mathbb C[x_1,x_2,x_3,x_4]\), with coefficient vector \(v\)
and Jacobian \(J\). If
\[
E(J)=J^2,\qquad \operatorname{rank}[\,v\mid J\,]\le2,
\tag{7}
\]
then \(E\) kills a nonzero complex linear form in the \(x_i\).
The lemma does not require a slice.

First, differentiating the coordinate expressions for the double
commutators shows that (2) is precisely the first identity in (7):
\[
[E,[E,T_i]]=-E(J_{\bullet i})+J^2_{\bullet i}.
\tag{8}
\]
This identity does **not** assert \(J^2=0\).

The derivation acts entrywise on matrices, so induction gives
\[
E^m(J)=m!J^{m+1}\qquad(m\ge0).
\tag{9}
\]
Local nilpotence on the finitely many entries makes a common
power on the left zero. Hence \(J\) is nilpotent over
\(\operatorname{Frac}B\).

Also
\[
E(v)=Jv,\qquad E^2(v)=2J^2v.
\tag{10}
\]
If \(J^2v\ne0\), the vectors \(v,Jv,J^2v\) are linearly
independent over that field. Indeed, for a nilpotent linear
operator, the nonzero initial segment of a cyclic Jordan chain
is independent, as follows by applying its largest relevant power
to a putative relation, successively. All three vectors belong to
the span of the columns of \([\,v\mid J\,]\), contradicting (7).
Therefore
\[
J^2v=0,\qquad E^2(v)=0.
\tag{11}
\]

### 3.1 The non-quasi-translation branch

Suppose \(E(v)\ne0\). Nilpotence of \(J\) implies that
\(v\) and \(E(v)=Jv\) are independent over the fraction field:
a nonzero proportionality coefficient would be an eigenvalue of
a nilpotent matrix. Choose a complex point \(a\) where their
values remain independent.

Consider the rational projective coefficient map
\[
\psi:\mathbb A^4\dashrightarrow\mathbb P^3,
\qquad x\longmapsto[v(x)].
\tag{12}
\]
In a chart where one component of \(v\) is nonzero, its
differential has rank \(q-1\le1\): it is the image of \(J\)
modulo the line spanned by \(v\). Characteristic zero therefore
gives \(\dim\overline{\psi(\mathbb A^4)}\le1\).
The closure is irreducible.

By (11), the actual additive-group flow satisfies
\[
v(\exp(tE)\cdot a)=v(a)+tE(v)(a).
\tag{13}
\]
These vectors are nonzero for all \(t\), and their projective
classes are dense in a projective line. That line is contained in
the irreducible image closure of dimension at most one, so the
closure is exactly the line. It follows that all values of \(v\)
lie in a fixed two-dimensional complex vector subspace. Two
independent constant linear forms therefore annihilate \(v\),
and their corresponding ambient linear coordinates are killed
by \(E\).

This argument does not infer that every projective curve image
is a line. The particular line comes from the actual nonconstant
flow in (13).

### 3.2 The quasi-translation branch and legitimate homogenization

Now suppose \(E(v)=Jv=0\). Then
\(x\mapsto x+tv(x)\) is the flow of \(E\): its coefficients
are constant along every orbit. In particular \(x+v(x)\) is a
quasi-translation. Differentiating \(Jv=0\) also gives
\(E(J)+J^2=0\); together with (7), this implies \(J^2=0\).

Choose an integer \(d\ge\max\{1,\deg v\}\), add an independent
variable \(z\), and define
\[
\widetilde v(x,z)=\bigl(z^d v(x/z),0\bigr).
\tag{14}
\]
This is a nonzero homogeneous polynomial map of positive degree
on five-dimensional affine space. It is a quasi-translation
coefficient map: its Jacobian times \(\widetilde v\) is
\(z^{2d-1}(Jv)(x/z)=0\). This is exactly the homogenization in
de Bondt's Proposition 2.5, whose statement and proof were
directly checked.[^bondt]

The additional Jacobian column must not be discarded. Writing
\(u=x/z\), the complete Jacobian after inverting \(z\) is
\[
\operatorname{Jac}_{x,z}\widetilde v
=z^{d-1}
\begin{pmatrix}
J(u)&d\,v(u)-J(u)u\\
0&0
\end{pmatrix}.
\tag{15}
\]
Adding the appropriate linear combination of the first four
columns to the last one, and using \(d\ne0\), proves
\[
\operatorname{rank}\operatorname{Jac}\widetilde v
=\operatorname{rank}[\,J\mid v\,]\le2.
\tag{16}
\]
Thus it is the augmented, or projective, rank bound in (7) that
survives homogenization. A bound on \(\operatorname{rank}J\)
alone would not justify (16).

Theorem 3.6(i),(iii) of de Bondt's paper, credited there to
Gordan and Nöther, now supplies at least two independent linear
invariants of this homogeneous quasi-translation: four in the
rank-one case, and at least two in the rank-two case. Its
dimension-five proof applies directly. No gcd-one assumption is
needed for these parts of the theorem.[^bondt]

One invariant is already \(z\). Since the space of linear
invariants has dimension at least two, there is another with a
nonzero \(x\)-linear part, say \(\ell(x)+c z\). Its invariance
is \(\ell(z^dv(x/z))=0\). Setting \(z=1\) gives
\(\ell(v(x))=0\), so \(E(\ell(x))=0\). This completes the
lemma. Adding \(z\) was only a proof device for a polynomial
map; it was not a claim that a different stabilized candidate
satisfies the original one-cylinder hypothesis.

## 4. Returning to the regular quotient and the exact gap

Under (1), \(A=B/(s)\) is affine and regular: regularity
descends from its polynomial extension \(A[s]\). The linear
form supplied by the lemma is an ambient coordinate, after an
invertible complex linear change of variables. The fixed-coordinate
kernel theorem of Bhatwadekar, Gupta and Lokhande, Theorem 3.5,
then gives
\[
A=\ker E\simeq\mathbb C^{[3]}.
\tag{17}
\]
Its exact hypotheses are a nonzero LND of
\(k[T,X,Y,Z]\) fixing \(T\), characteristic zero, and a regular
kernel; each has now been checked.[^bgl]
Choosing two coordinate partials on this polynomial \(A\)
finishes the low-rank branch of the theorem.

The conclusion is stronger than the
[one-partial equivalence in pass 36](intrinsic-transfer-pass36.md):
simultaneous commutation of the actual four partials gives the
abelian first-commutator action and the low projective-rank
alternative. No claim is made that each opposite double
commutator is automatically locally nilpotent.

What is still missing is an operation on an arbitrary genuine
ambient coordinate frame which produces (2), or a different
argument when all frames have larger adjoint height. Existence
of a lexicographically degree-minimal frame does not supply a
coordinate-preserving degree-lowering move. No such move, no
automatic finite closure of \(E,T_1,\ldots,T_4\), and no proof
of \(\operatorname{ML}(A)=\mathbb C\) is established here.

Thus (4) is a necessary condition on a rank-one countercandidate,
not a verified contradiction in the full original problem.
There is no claim of novelty, expert review, Lean verification,
or general cancellation.

## Primary-source and finite-check boundaries

The two-directions branch uses only the direct restriction argument
in Section 2, not the source-dependent rank-three group theorem.
The low-rank branch uses precisely the homogeneous quasi-translation
and invariant-coordinate kernel statements cited below. The actual
whole-frame identities are proved here, rather than inferred from
local nilpotence of an arbitrary projected field.

The standalone [exact checker](actual_frame_checks_pass38.py) imports
only `unittest` and `sympy`. Its six methods passed in 0.150 seconds.
They check the double-commutator matrix identity, commuting first
commutators, the factorial derivative and nilpotent-chain controls,
an actual non-quasi-translation flow, the complete homogenized
Jacobian column, and a low-rank conic image. A high-rank control
satisfies \(E(J)=J^2\ne0\), rejecting the invalid shortcut that
the whole height-one identity alone forces \(J^2=0\).

The initial invocation caught an unparenthesized Python generator
expression before any test ran; that syntax was corrected before
the passing six-method run. These finite controls do not verify
the source classification or the still-missing existence of a
whole height-one frame.

An independent full-file reconstruction and primary-statement
cross-read found no correction, including the revised direct
restriction proof. That audit independently ran the same six
methods in 0.145 seconds. The displayed \(q=3\) coordinate
control is a written algebraic identity and is not counted as
an additional test method.

A second [independent written audit](actual-frame-audit-pass38.md)
reconstructed the full proof and the primary-source gates without
requesting a correction. Its independent run passed the same six
methods in 0.142 seconds.

[^bondt]: Michiel de Bondt, [*Homogeneous quasi-translations in dimension 5*](https://arxiv.org/pdf/1501.04845v3), Proposition 2.5, PDF p. 9, and Theorem 3.6(i),(iii), PDF p. 13. Both complete statements and the relevant proofs were directly read. Proposition 2.5 accepts a nonhomogeneous input. Theorem 3.6 requires homogeneous positive degree, which is supplied by (14), and parts (i),(iii) do not assume primitivity. The paper explicitly attributes Theorem 3.6 to Gordan and Nöther. The independent calculation (15) supplies the needed rank bound; it is not obtained by ignoring the homogenizing variable.

[^bgl]: S. M. Bhatwadekar, Neena Gupta and S. A. Lokhande, [*Some K-theoretic properties of the kernel of a locally nilpotent derivation on k[X1,...,X4]*](https://arxiv.org/html/1501.01438v1), Theorem 3.5, complete statement and proof directly read. The invariant-coordinate conclusion is published input, not a new recognition theorem claimed here.
