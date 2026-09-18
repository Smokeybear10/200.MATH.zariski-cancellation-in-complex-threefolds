# A possible radical projection defect is only a node or a cusp

Status: working restriction on the generic projected plane ring,
not original-ring recognition. In the nonzero-R radical chart206,
if the plane ring is proper, its normalization defect has dimension
one. Explicit polynomial changes of the two projected generators,
over the exact coefficient field, put it in the form
\[
C=L[x^2,x^3+c x]\subsetneq L[x]=O,\qquad c\in L.
\tag{1}
\]
Its conductor is \((x^2+c)O\). When \(c=0\) this is a cusp; when
\(c\ne0\) it is a node after algebraic closure. These are descriptions
of a possible defect, not examples satisfying the actual chart.

The proof uses the actual conductor element and degree bounds from
[the nonzero-R eliminant206](weight-four-radical-nonzero-r-eliminant-pass206-working.md).
No genus formula, assumed normality, or coordinate lift is used.

## 1. Exact inputs and the conductor bound

Retain the actual hypotheses of that note. Its conclusions give
\[
\begin{gathered}
O=L[v],\qquad C=L[y,\vartheta]\subset O,\qquad
\operatorname{Frac}C=L(v),\\
O=C+Cw,\qquad R=2\vartheta+k_\rho\ne0,\qquad Rw\in C,\\
RO\subset C,\qquad
d:=\deg_v y\le5,\qquad e:=\deg_v\vartheta\le4.
\end{gathered}
\tag{2}
\]
The field \(L\) is the exact finite coefficient field; it need not
be rational or algebraically closed. The module equality in (2)
does not mean that \(1,w\) are a free basis.

If \(\vartheta\) is constant, then \(R\in L^*\) and \(C=O\).
If either nonconstant generator has degree one, \(C=O\) directly.
If \(y\) is constant, the fraction-field equality makes
\([L(v):L(\vartheta)]=1\), so \(e=1\) and again \(C=O\).
Consequently a proper \(C\) has \(d,e\ge2\).

For \(e>0\), \(\deg_vR=e\). The inclusion \(RO\subset C\)
implies finite codimension, with
\[
\delta:=\dim_L(O/C)
=e-\dim_L(C/RO)\le e-1.
\tag{3}
\]
Indeed \(O/RO\) has dimension \(e\), and the nonzero class of
one lies in \(C/RO\). We next prove a sharper restriction when
the two degrees are coprime.

## 2. An elementary degree-semigroup computation

Suppose \(d,e>0\) and \(\gcd(d,e)=1\), retaining the birational
field equality in (2). First, \(O\) is free over \(L[y]\) with
basis \(1,v,\ldots,v^{d-1}\). The degree-d polynomial expression
for \(y\) reduces every \(v^n\) to such a combination. Independence
follows from the distinct leading degrees \(kd+j\), with
\(0\le j<d\). Thus \([L(v):L(y)]=d\).

Multiplication by \(\vartheta\) is an endomorphism of this free
module. Its characteristic polynomial is a monic degree-d
polynomial in \(L[y][T]\), and annihilates \(\vartheta\).
Since \(L(y,\vartheta)=L(v)\), the minimal polynomial of
\(\vartheta\) over \(L(y)\) also has degree \(d\). The two monic
polynomials coincide. This proves the coefficient assertion
without an unproved descent from \(L(y)\).

It follows that
\[
C=\bigoplus_{j=0}^{d-1}L[y]\vartheta^j.
\tag{4}
\]
For nonzero summands, their leading degrees are \(kd+je\),
where \(k\ge0\) and \(0\le j<d\). These degrees are distinct
between different \(j\), because \(d,e\) are coprime. Consequently
no cancellation between summands changes the leading degree.
The set of degrees of nonzero elements of \(C\) is exactly
\[
\Gamma=\{kd+je:k\ge0,\ 0\le j<d\}
       =\langle d,e\rangle.
\tag{5}
\]

The monomials \(v^n\) for \(n\notin\Gamma\) form a basis of
\(O/C\). Spanning follows by cancelling a highest degree in
\(\Gamma\) using an element of \(C\), successively decreasing
degree. Independence follows because a nonzero combination of
missing-degree monomials cannot have its leading degree in
\(\Gamma\).

For completeness, write \(r_j\in\{0,\ldots,d-1\}\) for the
residue of \(je\) modulo \(d\). The least element of \(\Gamma\)
in that residue class is \(je\). Its missing values number
\((je-r_j)/d\). The \(r_j\) permute all residues, so
\[
\delta=\sum_{j=0}^{d-1}\frac{je-r_j}{d}
       =\frac{(d-1)(e-1)}2.
\tag{6}
\]
When \(d,e>1\), the largest missing integer is
\((d-1)e-d=de-d-e\): in residue \(r_j\) the last missing
value, if nonnegative, is \(je-d\), maximized at \(j=d-1\).
Thus the least integer from which all degrees belong to
\(\Gamma\) is \((d-1)(e-1)\).

The actual conductor supplies more than the codimension bound.
For every \(n\ge0\), the polynomial \(Rv^n\) lies in \(C\)
and has degree \(e+n\). Hence every integer at least \(e\)
belongs to \(\Gamma\). Therefore
\[
(d-1)(e-1)\le e
\quad\text{if }\gcd(d,e)=1,\quad d,e>1.
\tag{7}
\]
If \(d=2\), this allows odd \(e\). If \(d\ge3\), the inequality
forces \(d=3,e=2\); for \(d\ge4\) it is impossible.
Under the bounds \(d\le5,e\le4\), the only coprime pairs for
a proper plane ring are
\[
(d,e)=(2,3)\quad\text{or}\quad(3,2).
\tag{8}
\]
In particular \(d=5\) is impossible for a proper plane ring.

## 3. All remaining small-degree pairs reduce to a quadratic and cubic

If the original pair is noncoprime, the only possibilities with
\(d,e\ge2\), \(d\le5\), \(e\le4\) are
\[
(2,2),\ (2,4),\ (3,3),\ (4,2),\ (4,4).
\tag{9}
\]
All changes below are polynomial automorphisms of a plane over
\(L\), applied to its two generators. They preserve \(C\), its
fraction field, and \(O\). Their coefficients lie in \(L\);
no descent to the original four-ring is asserted.

For equal degrees, replace \(y\) by \(y-\lambda\vartheta\)
using the nonzero ratio of leading coefficients. The new degree
is smaller. A generator of degree one gives \(C=O\); a constant
leaves one generator of degree greater than one, contradicting
the birational field equality.

Thus \((2,2)\) cannot be proper. The case \((3,3)\) reduces to
\((2,3)\). In \((4,4)\), the new first degree is at most three.
Degree three is excluded by (7) for the new pair \((3,4)\):
at this step \(\vartheta\) is unchanged, so the same actual
conductor \(R=2\vartheta+k_\rho\) still has degree four.
The only proper possibility reduces to \((2,4)\).

For \((4,2)\), replace \(y\) by \(y-\lambda\vartheta^2\).
The first degree is now at most three. Degree three gives
\((3,2)\); degree two is reduced by one further linear
subtraction to degree at most one, which is not proper.

For \((2,4)\), replace \(\vartheta\) by
\(\vartheta-\lambda y^2\). Degree three gives \((2,3)\).
Degree two reduces by subtracting a multiple of \(y\), and
again degree at most one is not proper. We do not reuse (7)
after this change of \(\vartheta\): the original conductor
need no longer be linear in the new second generator.

This exhausts (9). Therefore every proper ring in (2) admits
two polynomial generators of degrees two and three.

## 4. Explicit cubic form and its exact conductor

Let \(f,g\) be the resulting quadratic and cubic generators.
Divide \(f\) by its leading coefficient and complete the square,
using an affine parameter \(x=v+\lambda\) with \(\lambda\in L\).
Subtracting a constant makes the first generator \(x^2\).
From \(g\), subtract a multiple of \(x^2\) and a constant to
remove its quadratic and constant terms. Dividing by the cubic
coefficient then gives \(x^3+c x\), proving (1).
These operations require only division by nonzero elements of
\(L\) and by two, not extraction of roots in \(L\).

Every polynomial in \(O\) has a unique even/odd decomposition
\(A(x^2)+xB(x^2)\). Set \(z=x^2\). The cubic generator is
\(x(z+c)\), and its square is \(z(z+c)^2\). Thus
\[
C=L[z]\oplus x(z+c)L[z],\qquad
\dim_L(O/C)=1.
\tag{10}
\]
In particular the missing class is represented by \(x\).

The conductor ideal is exactly
\[
\mathfrak c=\{h\in O:hO\subset C\}=(x^2+c)O.
\tag{11}
\]
The right-hand side is contained in \(C\) by (10), so it is
contained in the conductor. Conversely, write
\(h=A(z)+xB(z)\) in the conductor. Since \(h,hx\in C\),
(10) implies that both \(A\) and \(B\) are divisible by
\(z+c\). Therefore \(h\in(z+c)O\), proving equality.

Writing the plane generators as \(U=x^2,V=x^3+c x\), their
entire relation ideal is generated by
\[
V^2-U(U+c)^2.
\tag{12}
\]
The equation is irreducible over \(L\): \(U(U+c)^2\) is not
a square in \(L(U)\). Its evaluation kernel has height one,
so that irreducibility gives the entire ideal.

For \(c=0\), (12) is the cuspidal cubic \(V^2=U^3\).
For \(c\ne0\), its singular point is \((U,V)=(-c,0)\).
Putting \(u=U+c\), the lowest nonzero homogeneous part of
\(V^2-(u-c)u^2\) is \(V^2+c u^2\), which has two distinct
lines over an algebraic closure. This is a node. Equivalently,
the normalization identifies the two distinct roots of
\(x^2+c\). No assertion that these roots belong to \(L\) is made.

## 5. Consequences and the remaining actual-ring gate

The original conductor \(R\) belongs to \(\mathfrak c\).
Since \(2\le e\le4\) for a proper plane ring, (11) gives
\[
R=(x^2+c)h(x),\qquad h\in L[x],\qquad \deg h=e-2\le2.
\tag{13}
\]
Also, both original projected entries have degree at most four:
\(\vartheta\) does by (2), and degree five for \(y\) was excluded
in Section2. Formula (10) therefore writes either original
entry as an \(L\)-linear combination of
\[
1,\qquad x^2,\qquad x^3+c x,\qquad x^4.
\tag{14}
\]
These are finite-degree necessary restrictions on a possible
remaining defect.

The eliminant206 already proves that a defect requires a
nonconstant squarefree center polynomial \(p\) of degree one
or two. The present reduction does not show that the cusp or
node is compatible with the actual differential potentials,
scalar determinant, field return, or an original polynomial
frame. Nor does it yet exclude either type using those extra
identities.

If \(C=O\), that is only equality of generic projected rings.
If \(C\ne O\), (1) describes that generic ring after changes over
\(L\). Neither conclusion is an invariant coordinate of
\(\mathbb C[X,Y,Z,W]\). The full cancellation conjecture and
arbitrary coordinate entry remain unsolved.

The eliminant source and its exact hypotheses were fully read.
The semigroup argument was independently reconstructed before
this source was written; a saved-source review remains required.
No saved checker has been executed for this note. This is a
working proof, not human expert certification, proof-assistant
verification, or a historical novelty claim.
