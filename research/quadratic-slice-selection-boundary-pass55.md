# A cubic slice gauge in a quadratic intermediate algebra

Quadratic generation, stability under a constant-coefficient translation,
and existence of a slice do not by themselves force a slice of transverse
generic degree at most two. The intermediate algebra below has minimum
slice-gauge degree exactly three. It is smooth and flat over the local
base, but not faithfully flat: it misses the closed base point.

Thus the example does not realize the actual cancellation residual.
It identifies the precise missing nonempty-fiber premise in this
weaker proposed slice-selection theorem. It is an existential
countercontrol, not a large replica of a slice that already has a
smaller representative.

## 1. The weaker algebra and its four quadratic generators

Let
\[
k=\mathbb C,\qquad R=k[a,b]_{(a,b)},\qquad L=\operatorname{Frac}R.
\]
In the polynomial ring \(L[X,Y]\), put
\[
j=bX-aY,\qquad
Z=\frac{j^2-b}{a},\qquad
W=\frac{1-j^2+b}{b}.
\tag{1}
\]
Define the actual subalgebras of these specified fraction rings
\[
\mathcal A_0=R[j,Z,W]\subset L[j],\qquad
\mathcal B_0=R[X,Y,Z,W]\subset L[X,Y].
\tag{2}
\]
Both extra generators in (1) have total degree at most two in
\(X,Y\), with coefficients in \(L\). They satisfy
\[
aZ+bW=1,\qquad j^2=aZ+b.
\tag{3}
\]

The \(R\)-derivation
\[
E=a\partial_X+b\partial_Y
\tag{4}
\]
preserves \(\mathcal B_0\), kills \(j,Z,W\), and is locally nilpotent.
The element
\[
s=ZX+WY\in\mathcal B_0
\tag{5}
\]
has \(Es=1\). There are exact inverse formulas
\[
X=as+Wj,\qquad Y=bs-Zj.
\tag{6}
\]
They follow directly from \(aZ+bW=1\) and \(j=bX-aY\).
Consequently
\[
\mathcal B_0=\mathcal A_0[s],\qquad
\ker(E:\mathcal B_0\to\mathcal B_0)=\mathcal A_0.
\tag{7}
\]
Algebraic independence of \(s\) over \(\mathcal A_0\) can also be
checked in \(L[X,Y]\): the explicit inverse (6), with \(Z,W\)
polynomials in \(j\) over \(L\), proves that \((j,s)\) is a
polynomial coordinate pair over \(L\).

If nonzero accelerations of the two displayed good generators are
desired, replace them by
\[
Q_1=Z+X^2,\qquad Q_2=W+Y^2.
\tag{8}
\]
The ring is unchanged:
\(\mathcal B_0=R[X,Y,Q_1,Q_2]\). These remain quadratic over \(L\), and
\[
EQ_1=2aX,\quad E^2Q_1=2a^2,\qquad
EQ_2=2bY,\quad E^2Q_2=2b^2.
\tag{9}
\]
In particular the bad speeds \(a,b\) are algebraically independent,
and the flow has genuine degree two on this four-generator list.
These generators are not asserted to be an ambient polynomial
coordinate frame, and no adjoint bounds on hypothetical coordinate
partials are asserted.

## 2. Exact presentation, smoothness, and the missing fiber

The invariant algebra in (2) has the exact presentation
\[
\mathcal A_0=
R[J,Z,W]/(aZ+bW-1,\ J^2-aZ-b),
\tag{10}
\]
where \(J\) maps to \(j\).
To verify exactness without a saturation assumption, the abstract
ring on the right is covered by the opens \(D(a),D(b)\), by its first
relation. Its two charts are
\[
\begin{split}
(\mathcal A_0)_a
&=R_a[J,W]/(J^2+bW-b-1),\\
(\mathcal A_0)_b
&=R_b[J,Z]/(J^2-aZ-b).
\end{split}
\tag{11}
\]
Each polynomial is monic in \(J\); over \(L\) its quotient is the
domain \(L[j]\), with \(W\) or \(Z\) eliminated. Freeness over
\(R_a[W]\) or \(R_b[Z]\) makes the map to that generic domain
injective. Thus both charts inject into the algebra in (2).
They cover (10), so the entire presentation injects as well.

These charts also prove flatness over \(R\). The first is free
with basis \(1,J\) over the flat \(R\)-algebra \(R_a[W]\); the
second is free with the same basis over \(R_b[Z]\). Flatness is
local on the source, and these two opens cover the source.

They are smooth complex charts. In the second equation of (11)
the derivative with respect to \(b\) is \(-1\). In the first,
simultaneous vanishing of its derivatives with respect to
\(J,W,b\) would require
\[
J=0,\qquad b=0,\qquad W=1,
\]
which contradicts the equation's constant term \(-1\).
Equivalently its Jacobian ideal is the unit ideal. All coefficient
localizations are open restrictions of these smooth affine charts.
Thus \(\mathcal A_0\), and hence \(\mathcal B_0=\mathcal A_0[s]\),
are regular domains essentially smooth over \(k\).

The crucial failure is explicit:
\[
(a,b)\mathcal A_0=\mathcal A_0,\qquad
(a,b)\mathcal B_0=\mathcal B_0.
\tag{12}
\]
Their closed fibers over the local base are empty. The flat maps
are not faithfully flat. In particular smoothness and flatness
alone are not replacements for the actual nonempty-fiber hypothesis.

## 3. Every slice has gauge degree at least three

Use the affine generic slice \(\sigma_0=X/a\). Equation (5) gives
\[
s=\sigma_0+H(j),\qquad
H(j)=\frac{j^3-(1+b)j}{ab}.
\tag{13}
\]
Every other slice in \(\mathcal B_0\) is \(s+A\) with
\(A\in\mathcal A_0\), by (7).

Suppose that some slice had the form
\(\sigma_0+P(j)\), where \(P\in L[j]\) has degree at most two.
Then \(H-P\in\mathcal A_0\). The involution \(j\mapsto-j\)
preserves \(\mathcal A_0\), since it fixes \(Z,W\).
Taking odd parts, and using characteristic zero, would give
\[
H-\ell j\in\mathcal A_0
\quad\text{for some }\ell\in L.
\tag{14}
\]
We show that no such \(\ell\) exists.

At the height-one base prime \((a)\), \(b\) is a unit and the
second presentation of (11), now over \(R_{(a)}\), is free over
\(R_{(a)}[Z]\) with basis \(1,j\). Since \(j^2=aZ+b\),
\[
H=\frac{jZ}{b}-\frac{j}{ab}.
\]
Uniqueness of this basis expansion in the generic ring shows
that (14) requires
\[
\ell+\frac1{ab}\in R_{(a)}.
\tag{15}
\]

At \((b)\), \(a\) is a unit. The first presentation in (11)
is free over \(R_{(b)}[W]\) with basis \(1,j\), and
\[
H=-\frac{jW}{a}\in(\mathcal A_0)_{(b)}.
\]
Thus (14) requires \(\ell j\in(\mathcal A_0)_{(b)}\), and
uniqueness of the basis gives \(\ell\in R_{(b)}\).
At every other height-one prime \((\pi)\) of \(R\), both \(a,b\)
are units and \((\mathcal A_0)_{(\pi)}=R_{(\pi)}[j]\).
There (14) again requires \(\ell\in R_{(\pi)}\).
Therefore
\[
\ell\in\bigcap_{\pi\not\sim a}R_{(\pi)}=R[1/a].
\tag{16}
\]
The equality uses only unique factorization in the local ring \(R\).

Write \(\ell=q/a^N\) with \(q\in R\). Condition (15) rules out
\(N=0\), so take \(N\ge1\). The same condition implies
\[
a^N\mid bq+a^{N-1}\quad\text{in }R.
\tag{17}
\]
Indeed divisibility at \((a)\) contracts to this divisibility in
the UFD \(R\). Reducing (17) modulo \(b\) would make
\(a^{N-1}\) divisible by \(a^N\) in the DVR
\(R/(b)=k[a]_{(a)}\), which is impossible.
This contradicts (14).

Thus no slice has gauge degree at most two. The explicit slice
(13) has degree three, so
\[
\boxed{\min_{Es'=1}\deg_j(s'-X/a)=3.}
\tag{18}
\]
The minimum is over all slices belonging to \(\mathcal B_0\).
Changing an affine generic slice or the polynomial generator
of \(L[j]\) does not change this conclusion.
The argument excludes every low-degree representative, rather
than exhibiting only a particular high-degree slice.

For the quadratic list (8), its two nonzero coefficients in (9)
give the same degree comparison as in pass54: a gauge of degree
\(n\ge2\) has maximum projected-list degree \(2n\).
Its minimum maximum projected generic degree is consequently six.
This statement concerns generic polynomial degree; no additional
primitive intrinsic derivation is needed for this control.

## 4. The actual faithful-flat question remains separate

The [actual pass54 slice-coset criterion](profile-generation-gap-pass54.md)
requires a representative in
\[
H_*+\mathcal A\subset L[j].
\]
The control above disproves the degree-two selection implication
for smooth flat quadratic intermediate algebras when the closed
fiber may be empty. It does not decide that implication for the
actual faithfully flat algebra
\[
B_R=R[x_3,x_4,\mathcal Q_1(x_3,x_4),\mathcal Q_2(x_3,x_4)]
\]
with its four genuine ambient coordinate generators, full adjoint
identities, nonempty closed fiber, and polynomial-cylinder origin.
It also does not disprove a uniform bound of three or a larger
bound under the weaker premises.

The [invariant-open argument in pass50](fiber-invariant-opens-pass50.md)
does not supply the missing low-degree representative. In the
actual setting its nonempty fiber opens have denominators whose
moving prime factors cannot occur in a finite-degree polynomial.
Consequently a bounded slice constructed on any one such nonempty
open descends to \(B_R\) with its bound unchanged. That is a
descent theorem conditional on constructing the bounded slice.
The square-root normalization gives slices in an algebraic
extension whose intrinsic derivative degree need not be finite.

Here the two opens \(D(a),D(b)\) instead cover the entire source
because the closed base fiber is missing. The incompatible
conditions (15)--(17) occur precisely over the omitted base point.
They cannot be promoted to an obstruction at an actual fiber.
In particular this example neither invalidates the pass50 descent
theorem nor satisfies its nonempty-fiber hypotheses.

## Verification scope

The inverse formulas, two monic chart presentations, and all-slices
valuation argument are explicit algebra. No image-ideal freeness,
associated-graded generation, or cancellation theorem is used.
This is a boundary for a stated weaker lemma, not a novelty claim
or a counterexample to cancellation. Files from pass54 and earlier
remain unchanged; no registry or regression count is changed here.
