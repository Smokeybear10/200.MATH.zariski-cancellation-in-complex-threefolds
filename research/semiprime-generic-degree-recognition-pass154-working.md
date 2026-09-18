# Semiprime generic degree forces the graph case

This working corollary concerns the supplied actual dense three-good
frame only. If its generic embedded-line degree \(d=\mu+1\) is a
product of two primes, counted with multiplicity, its normalized
generic curve must already be a graph in the fixed axes.
The retained graph-recognition theorem therefore gives
\(A\simeq\mathbb C^{[3]}\). In particular this recognizes
minimum \(\mu=5\) through \(d=6\).

The argument uses degree divisibility over the exact coefficient
field and an explicit leading-term subtraction. It does not
assert that a plane-coordinate change over that field is an
allowed original-coordinate change. This new154 corollary is
outside frozen checkpoint153 and is not a solution to arbitrary
coordinate entry or the full cancellation problem.

## 1. Actual inputs and the statement

Use leading normalization153 and the actual generic chart139/145:
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad
E^2X=E^2Y=E^2Z=0,\\
\text{the good speeds have rank two and dense homogeneous cone},
\qquad m=\mu\ge2,\qquad d=m+1,\\
\deg_EW=m,\qquad s=EX\ne0,\quad \tau=EY/s,\quad \rho=EZ/s,\\
L/\mathbb C(\tau,\rho)\text{ finite separable},\qquad
L[y,z]=L[v],\qquad \Phi\in L^*g,\quad
\ker(L[U,V]\longrightarrow L[v])=(g),\\
\deg g=\deg\Phi=d,\qquad \Phi_d=-\gamma U^d,\quad
\gamma\in\mathbb C^*,\qquad f_m=\gamma\tau^d .
\end{gathered}
\tag{1}
\]
Every original coordinate change supplying (1) is one of the
actual changes allowed in the retained normalization proof.
All canonical tail and derivative hypotheses required by the
two-stage exclusion154 are included in these retained inputs.[^1]

Assume \(d=pq\) for primes \(p,q\), possibly equal.
The claim is \(\deg_v y=1\), followed by graph recognition.

## 2. Degree divisibility in the exact field

The polynomial parametrization's unique point at infinity is
\([0:1:0]\), because the whole implicit leading form is
\(-\gamma U^d\). The exact degree equality139 then gives
\[
\deg_v z=d,\qquad 0<e:=\deg_v y<d.
\tag{2}
\]
If \(y\) were constant, \(L[y,z]=L[v]\) would give an implicit
line rather than degree \(d\ge4\). These are the same fixed-axis
degree conclusions used in graph-recognition153.

The Abhyankar--Moh--Suzuki degree theorem states, in characteristic
zero, that one of the two degrees divides the other when the
polynomials generate a one-variable polynomial ring. It applies over the exact
field \(L\), without assuming that \(L\) is algebraically closed.[^2]
Thus \(e\mid d\). If \(e=1\), the conclusion is already established.
Otherwise \(e\) is a proper nontrivial divisor of a semiprime,
so \(e=p\) or \(e=q\), and in either case \(e\) is prime.

## 3. Leading subtraction exposes a fixed-axis two-stage equation

Keep \(y\) fixed and start with the polynomial \(z\in L[v]\).
Throughout the following procedure the current residual \(w\)
satisfies \(L[y,w]=L[v]\).
If \(D=\deg_v w\ge e\), the same AMS theorem gives \(e\mid D\).
Choose the quotient of the leading coefficients of \(w\) and
\(y^{D/e}\), which is an element of \(L\), and subtract that
scalar multiple of \(y^{D/e}\). This strictly lowers \(D\).

The residual cannot become constant: that would imply
\(L[y,z]=L[y]\), impossible when \(\deg y=e>1\).
Since degrees strictly decrease, eventually a positive residual
degree \(D<e\) occurs. AMS now gives \(D\mid e\).
The primality of \(e\) forces \(D=1\). Consequently
\[
w=z-\mathcal A(y),\qquad
\mathcal A\in L[T],\quad \deg\mathcal A=d/e,\qquad
\deg_v w=1,\qquad y=P_e(w),\quad \deg P_e=e .
\tag{3}
\]
The initial leading subtraction has power \(d/e\), with a
nonzero coefficient. Later subtractions have smaller powers,
so the displayed degree of \(\mathcal A\) is exact.
Since \(w\) is affine-linear in \(v\), writing \(y=P_e(w)\)
uses coefficients in \(L\) and takes no field extension or root.

This constructs the following equation in the unchanged formal
axes \(U,V\):
\[
g\in L^*\{U-P_e(V-\mathcal A(U))\},\qquad
\Phi=\mathcal B(V-\mathcal A(U))+\ell U+n,\qquad
\deg\mathcal A=d/e\ge2,\quad \deg\mathcal B=e\ge2,\quad \ell\ne0.
\tag{4}
\]
For example, take \(\Phi=\lambda\{U-P_e(V-\mathcal A(U))\}\),
\(\ell=\lambda\), \(\mathcal B=-\lambda P_e\), and \(n=0\);
the scalar \(\lambda\in L^*\) exists by the whole-kernel
association145.

Equation (4) is exactly the additional placement hypothesis of
the two-stage exclusion154. That theorem rules it out under
the actual inputs (1). Therefore \(e>1\) is impossible.
The only remaining degree is \(e=1\), and graph-recognition153
gives the claimed polynomial kernel.

This generic leading subtraction is used only to describe the
literal first-tail equation in the original formal axes.
No polynomial automorphism over \(L\) is transported to the
original four-coordinate ring without proof. All such actual
changes are instead supplied inside the two-stage and graph
proofs already cited.

## 4. Consequences and limits

The semiprime case includes \(d=6\), hence minimum \(\mu=5\).
It also includes repeated primes, for example \(d=9\).
Prime generic degrees were already handled by153.
The proof does not state that these are the only recognized
degrees, and it does not classify longer coordinate compositions.

All conclusions retain the actual sliced dense three-good
hypotheses. There is no assertion about arbitrary coordinate
entry, other general profiles, the full cancellation conjecture,
historical priority, human expert review, or formal verification.
Finite examples cannot replace the degree theorem or the
universal conditional exclusions.

## Sources

1. [Leading normalization153](dense-all-degree-leading-normalization-pass153-working.md),
   [actual chart139](dense-all-degree-taylor-chart-pass139-working.md),
   [exact generic degree139](dense-generic-embedded-line-pass139-working.md),
   and [first-tail primitivity145](common-gauss-integrality-tail-primitivity-pass145-working.md).
   These provide (1)--(2) and the exact generic ring, not merely
   a chosen irreducible component after scalar extension.
2. Leonid Makar-Limanov,
   [*A new proof of the Abhyankar-Moh-Suzuki Theorem*](https://arxiv.org/pdf/1212.0163v1),
   AMS Theorem, printed p. 1. The exact characteristic-zero
   field statement was freshly read for this argument.
   Only degree divisibility is imported; the finite leading
   subtraction and fixed-axis consequence are proved here.
3. [Two-stage nongraph exclusion154](two-stage-nongraph-continuation-pass154-working.md),
   Sections 1--6, with the explicit fixed-axis hypothesis.
4. [Graph recognition153](dense-all-degree-graph-correction-pass153-working.md),
   including its [normalized-suspension endpoint](normalized-suspension-recognition-pass153-working.md).
   This supplies actual polynomial generators once \(\deg_v y=1\).

[^1]: Sources 1, 3 and their stated actual inputs.
[^2]: Source 2, applied repeatedly to the unchanged generating
    ring \(L[y,w]=L[v]\).
