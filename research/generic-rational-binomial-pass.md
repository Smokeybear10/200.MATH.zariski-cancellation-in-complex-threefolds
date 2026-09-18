# General rationally acyclic fibers of a binomial polynomial

The proposed strengthening is valid. Let

\[
G(x,y,z)=f(x,y)z^q+g(x,y),\qquad
0\ne f\in\mathbb C[x,y],\quad q\ge1.
\]

If a general fiber of \(G\) is smooth and rationally acyclic, then
\(G\) is a coordinate of \(\mathbb C[x,y,z]\). No total-degree
bound and no assumption on every special fiber is needed.

Here general means on a nonempty Zariski open subset of the parameter
line, equivalently the topological generic fiber. It does not mean an
arbitrarily chosen single smooth fiber.

This is a deduction from the cited results with a genericity argument,
not a claim that the deduction is new. The audit did not identify a
gap in it.

## 1. Exact inputs

Put \(X_n=\{f z^n+h=0\}\), with \(f,h\) nonconstant and
coprime. [Kaliman and Zaidenberg, *Affine modifications and affine
hypersurfaces with a very transitive automorphism group*, Section
7](https://arxiv.org/pdf/math/9801076) supplies these inputs:

- Lemma 7.4(a): smoothness, irreducibility and rational acyclicity
  descend from \(X_n\) to \(X_1\).
- Lemma 7.5(a): for smooth irreducible rationally acyclic \(X_n\),
  \(\chi(D_h)=1\) when \(n>1\).
- Lemma 7.5(b): under those same hypotheses the reduced irreducible
  components of \(D_f\) are disjoint simply connected curves, smooth
  outside \(D_h\), and each meets \(D_h\) at exactly one point.
- Lemma 7.6(b) and Proposition 7.1: for \(n=1\), rational
  acyclicity together with transverse intersection of the supports of
  \(D_f,D_h\) gives rectifiability.

The extra integral-homology assumptions in other parts of these
lemmas are not being imported into the above statements. In
particular, the smoothness of \(D_f\) at its intersection with
\(D_h\) will be supplied below by the choice of level.

## 2. A general level supplies the missing transversality

Assume first that \(f\) and \(g\) are nonconstant. Write
\(D=V(f)_{\rm red}\). Its singular set is finite. Exclude the
values of \(g\) at that finite set. On every irreducible component
of \(D\) where \(g\) is nonconstant, exclude the finite set of
critical values of its restriction to the smooth locus. On every
component where \(g\) is constant, exclude that constant value.

Also exclude the finitely many nongeneric values of \(G\) and
\(g\). Choose \(\lambda\) outside the resulting finite set and
put \(h=g-\lambda\).

Then \(V(h)\) is smooth and reduced; it avoids every singular
point of \(D\), has no common component with \(D\), and meets
\(D\) transversely wherever it meets it. If some component of
\(D\) were disjoint from \(V(h)\), KZ Lemma 7.5(b) would
contradict the assumed rational acyclicity of \(G^{-1}(\lambda)\).
Thus no such disjoint component occurs.

That lemma now makes every component of \(D\) smooth everywhere:
it is smooth outside \(V(h)\) by the lemma, and the chosen
intersections avoid its singularities. These components are therefore
affine lines. This is the step that fails at a specially selected
tangent level such as the rationally acyclic Bertin surface.

## 3. The case \(q=1\)

Apply KZ Lemma 7.6(b) followed by Proposition 7.1 to the selected
fiber. Their transverse-intersection hypothesis was verified in
Section 2, and their rational-acyclic hypothesis is exactly the one
assumed here. Thus an automorphism of \(\mathbb A^3\) takes
\(V(G-\lambda)\) to a coordinate plane.

The fiber is smooth and connected, hence its equation is reduced and
irreducible. Equality of its principal prime ideal with the transported
coordinate-plane ideal means that \(G-\lambda\) becomes a nonzero
constant times a coordinate. Therefore \(G\) is itself a coordinate.

There is also a coefficient-only conclusion, needed independently
of this absolute coordinatehood: a base automorphism makes
\(f=p(a)\) for a univariate polynomial \(p\). Indeed, Section 2
makes the reduced components of \(V(f)\) disjoint affine lines.
Rectify the first component to \(a=0\). The restriction of \(a\)
to every other component is nowhere zero, hence a nonzero constant
because the units on \(\mathbb A^1\) are constant. Each other
component is consequently the full line \(a=\alpha\). Its
irreducible equation is associated to \(a-\alpha\); including
multiplicities in the factorization of \(f\) gives \(f=p(a)\).
Constant \(f\) satisfies the same conclusion trivially.

This coefficient-only conclusion does not assert that \((f,g)\) becomes a pair
\((p(a),b)\). For example \(xz+y+xy^2\) is a coordinate while
\(y+xy^2\) is not a plane coordinate.

## 4. The case \(q>1\)

KZ Lemma 7.5(a) gives \(\chi(V(g-\lambda))=1\). Because
\(\lambda\) was also chosen as a generic value of \(g\), this
forces its fiber to be connected, as follows.

A polynomial has a finite bifurcation set and is a smooth locally
trivial fibration outside it, as recalled in [Dimca and Némethi,
*On the monodromy of complex polynomials*, Section
2.1](https://arxiv.org/pdf/math/9912072). For \(g\), the inverse
image of this regular-value open subset is a nonempty Zariski open
subset of \(\mathbb A^2\), hence connected. Its monodromy acts
transitively on the connected components of the fiber. Consequently
all \(r\) components have the same integral Euler characteristic
\(e\). The equation \(re=1\) gives \(r=e=1\).

A connected smooth affine curve of Euler characteristic one is
\(\mathbb A^1\). Plane-line rectification then makes
\(h=g-\lambda\) a plane coordinate.

Rectify one component of \(D\) to the line \(a=0\). Every other
component is disjoint from it, so the restriction of \(a\) to that
affine line is an invertible regular function and thus a nonzero
constant. The components of \(D\) are therefore parallel lines,
and \(f=p(a)\) for a univariate polynomial \(p\), including the
original multiplicities.

The coordinate \(h\) restricts to an affine-linear polynomial on
\(a=0\): it has exactly one zero there, which is simple by
transversality. The following elementary relative-coordinate argument
therefore applies. Choose a companion \(w\) to \(h\). In the
coordinates \((h,w)\), the old line \(a=0\) is a polynomial
graph \(w=r(h)\). Its irreducible equation is associated to
\(w-r(h)\). Thus \((a,h)\) is a coordinate pair.

In that pair of base coordinates,

\[
G=p(a)z^q+h+\lambda.
\]

Replacing \(h\) by \(G\) is an elementary triangular
automorphism of \(\mathbb C[a,h,z]\). This proves coordinatehood
and, in this branch, the stronger simultaneous base-coordinate
normal form.

## 5. Constants and degenerate cases

If \(f\in\mathbb C^*\) and \(q=1\), coordinatehood is
immediate.

If \(f=c\in\mathbb C^*\), \(q>1\), and \(g\) is
nonconstant, projection of the selected fiber to \(\mathbb A^2\)
is a cyclic cover branched along \(C=V(g-\lambda)\). Stratifying
along that curve gives

\[
1=\chi(G^{-1}(\lambda))
=q-(q-1)\chi(C),
\]

so \(\chi(C)=1\). The generic-component argument of Section 4
makes \(C\) an affine line. Hence \(g\) is a coordinate and
\(cz^q+g\) is a coordinate. This Euler calculation and the
irreducible-branch conclusion also appear in [Alok Maharana,
*Q-homology planes as cyclic covers of A2*, Lemmas 3.1 and
3.2](https://www.jstage.jst.go.jp/article/jmath/61/2/61_2_393/_pdf).

If \(g\) is constant, choose a different level. Projection of
\(fz^q=\lambda-g\) to \(\{f\ne0\}\) is an unramified
\(q\)-sheeted cover. Its Euler characteristic is divisible by
\(q\), so rational acyclicity forces \(q=1\). In that case the
fiber is \(\mathbb A^2\setminus V(f)\). For nonconstant \(f\)
this complement has nonzero \(H_1\), generated by meridians of its
reduced irreducible components, contradicting rational acyclicity.
Thus only constant nonzero \(f\), \(q=1\) survives here.

## 6. Scope for the ongoing slice argument

The result upgrades the previously used binomial surface criterion
when acyclicity is known for a general level: rational coefficients
suffice. A single special rationally acyclic level still does not.

No particular ambient coordinate, including the original \(x\), is
claimed to be preserved. Applying this result to a branch polynomial
therefore proves absolute coordinatehood, not a residual-coordinate
statement over a previously chosen coefficient ring. Any subsequent
slice descent must use precisely the conclusion established here.
