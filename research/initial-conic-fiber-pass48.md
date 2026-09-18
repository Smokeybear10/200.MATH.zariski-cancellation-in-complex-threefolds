# Initial conic equations on the actual closed fiber

The plane fiber of the degree-two subalgebra does not embed
automatically into the full quotient fiber. Flatness nevertheless
forces its image to satisfy the lowest nonzero base-adic equations
of the conic. At a reduced obstruction point this gives an explicit
distinction between a line-valued image and a finite image.

These are restrictions on the image of two functions, not a
classification of the full fiber or a proof that higher generators
are unnecessary.

## 1. Lowest base-adic coefficients survive flat base change

Use the actual local setup in the
[cubic note](third-image-cubic-gate-pass48.md). Put
\(R=C_{\mathfrak m}\), \(\mathfrak n=\mathfrak mR\),
\(\mathcal A=A\otimes_C R\), and
\(\overline{\mathcal A}=\mathcal A/\mathfrak n\mathcal A\).
The latter is a nonzero finitely generated complex algebra.
Flatness gives, in each degree \(d\geq0\),
\[
\mathfrak n^d\mathcal A/\mathfrak n^{d+1}\mathcal A
\simeq
(\mathfrak n^d/\mathfrak n^{d+1})
\otimes_{\mathbb C}\overline{\mathcal A}.
\tag{1}
\]
Indeed tensor the inclusions of both ideals into \(R\) and their
short exact quotient sequence. Flatness makes the tensor injections
actual ideal inclusions and preserves the quotient sequence.
No finite-module assumption on \(\mathcal A\) is needed.

For any polynomial relation
\[
F(Z,W)=\sum_{i,j}c_{ij}Z^iW^j,\qquad F(z,w)=0,
\]
whose coefficients all lie in \(\mathfrak n^d\), (1) therefore gives
\[
\sum_{i,j}[c_{ij}]\otimes\bar z^i\bar w^j=0.
\tag{2}
\]
Taking coefficients in any complex basis of
\(\mathfrak n^d/\mathfrak n^{d+1}\) produces actual equations in
\(\overline{\mathcal A}\). These are equations on the image of
\(\mathbb C[Z,W]\), not equations asserted in the auxiliary
polynomial plane \(\mathbb C[Z,W]\) itself.

One cannot continue to higher homogeneous coefficients of the same
relation unless the lower coefficients vanish in the base ring.
Vanishing after evaluation at \(\bar z,\bar w\) does not suffice:
higher terms can contain information about the varying lifts of
\(z,w\). Only the indicated coefficient-wise filtration step is used.

## 2. First-jet equations at a reduced obstruction point

Suppose \(J_R=\mathfrak n\). Choose regular parameters \(a,b\)
so that the actual conic has the form
\[
F=\epsilon(aZ+bW)^2-2B_2Z+2B_1W-Q,\qquad
\epsilon\in R^*,\quad B_1,B_2,Q\in\mathfrak n.
\tag{3}
\]
An invariant translation of the local minimal slice has already
been made. Write
\[
B_1=ac+bd,\quad B_2=ae+bf,\quad Q=aq+bh.
\tag{4}
\]
Modulo \(\mathfrak n\), the six coefficients in (4) are the
corresponding first-jet coordinates and are independent of the
choice of decompositions.

The quadratic part of (3) has all coefficients in
\(\mathfrak n^2\). Applying (2) with \(d=1\) gives
\[
-2\bar e\,\bar z+2\bar c\,\bar w-\bar q=0,\qquad
-2\bar f\,\bar z+2\bar d\,\bar w-\bar h=0.
\tag{5}
\]
Their coefficient matrix has the same rank as
\[
M=\begin{pmatrix}\bar c&\bar d\\ \bar e&\bar f\end{pmatrix}.
\tag{6}
\]
The augmented affine system in (5) is consistent. Otherwise a
complex linear combination would give a nonzero constant equal
to zero in the nonzero complex algebra \(\overline{\mathcal A}\).
Thus its augmented matrix has the same rank as its coefficient
matrix.

If the rank is one, (5) confines the image of \((\bar z,\bar w)\)
to an affine line. The image algebra is a quotient of
\(\mathbb C[T]\); it need not be the whole coordinate ring of
the quotient fiber. The
[cubic rank exclusion](third-image-cubic-gate-pass48.md)
rules out rank two under the actual hypotheses.
That exclusion is not being reproved by these linear equations.

## 3. A rank-zero first jet leaves a finite image of length at most three

Suppose \(M=0\). Then \(B_1,B_2\in\mathfrak n^2\).
Equations (5) also force \(\bar q=\bar h=0\), hence
\(Q\in\mathfrak n^2\). Every coefficient of the actual conic
now lies in \(\mathfrak n^2\), so (2) applies with \(d=2\).

The classes of \(a^2,ab,b^2\) form a basis of
\(\mathfrak n^2/\mathfrak n^3\). The corresponding three
coefficients in (2) have quadratic terms, respectively,
\[
\bar\epsilon\,\bar z^2,\qquad
2\bar\epsilon\,\bar z\bar w,\qquad
\bar\epsilon\,\bar w^2.
\tag{7}
\]
All their other terms are affine-linear in
\(1,\bar z,\bar w\), coming from \(B_1,B_2,Q\).
Since \(\bar\epsilon\ne0\) and the characteristic is zero,
each quadratic monomial is a complex linear combination of
\(1,\bar z,\bar w\).

Multiplying and reducing one quadratic factor at a time shows
inductively that every monomial is in the same span. Thus
\[
\boxed{\quad
\dim_{\mathbb C}\mathbb C[\bar z,\bar w]\leq3.
\quad}
\tag{8}
\]
This is the dimension of the actual image subalgebra of
\(\overline{\mathcal A}\), including possible nilpotents.
It is not a dimension bound on \(\overline{\mathcal A}\).
Also \(p=aB_1+bB_2\in\mathfrak n^3\) in this case.

If the full fiber happens to be reduced, the finite image
subalgebra is reduced, hence a product of at most three copies
of \(\mathbb C\). If that fiber is also connected, its image
is one point and both functions are constant. Neither reducedness
nor connectedness of the full fiber is silently assumed here.

## Scope and provenance

The lowest-initial-form observation was identified in the parallel
cubic investigation; this note spells out its flat-module proof
and its exact image-algebra consequences. No additional numerical
test is counted for this elementary coefficient argument.
The cubic note supplies the separate topological rank-two exclusion.

Rank one, rank zero with a finite low-degree image, and the
nonreduced-obstruction case remain possible. Their higher-degree
fiber corrections are not eliminated. The original cancellation
question, the full frame reduction and historical novelty remain
unresolved.
