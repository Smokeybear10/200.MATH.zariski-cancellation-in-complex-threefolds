# Foundational audit of the intrinsic affine-plane quotient

The inherited quotient claim survives this adversarial audit. If
\(A\) is a complex affine domain, \(A[s_*]\simeq\mathbb C^{[4]}\), and
\(0\ne D\in\operatorname{LND}_{\mathbb C}(A)\), then
\[
C:=\ker D\simeq\mathbb C^{[2]},\qquad
C\longrightarrow A\text{ is faithfully flat}.
\tag{1}
\]
The leading frame is needed to produce a nonzero global intrinsic
LND, not as an extra hypothesis of this quotient theorem.

This audits [the inherited proof](intrinsic-quotient-surface-pass.md).
Its \(K,d,A\) correspond to the present \(A,D,C\). It is neither a
new quotient theorem nor a resolution of cancellation.

## 1. Primary statement and version boundary

Kaliman and Saveliev's
[*C+-actions on contractible threefolds*](https://www.math.miami.edu/~kaliman/library/KaSa.michigan.2004.quotient.pdf)
starts with a smooth contractible affine complex threefold carrying a
nontrivial algebraic additive action.

| Passage in the author PDF | Applicable content |
| --- | --- |
| Lemma 2.1(1), p. 2 | An affine factorial surface quotient with nonempty curve fibers. |
| Theorem 2.7, pp. 4–5 | The quotient is smooth and contractible. |
| Corollary 2.8(2), p. 6 | Domination by a curve times affine two-space makes the quotient an affine plane. |
| Corollary 2.8(1),(3), p. 6 | Freeness is an additional premise for a translation product. |
| Section 3, pp. 6–8 | An independent logarithmic-form proof covers the dominated case without the Taubes step. |

The [arXiv record](https://arxiv.org/abs/math/0209306) lists only v1,
dated 23 September 2002. The relevant statements agree with the
author-hosted manuscript, whose proof wording and pagination differ.
The author's [publication list](https://www.math.miami.edu/~kaliman/)
identifies *Michigan Mathematical Journal* 52 (2004), no. 3, 619–625.

This audit directly read the author-hosted theorem proofs and compared
the relevant arXiv passages. Project Euclid's article and PDF endpoints
were inaccessible in this run. This is an author-primary and arXiv
comparison, not a newly observed typeset-journal comparison.

## 2. Cylinder hypotheses, before any cancellation conclusion

Put \(X=\operatorname{Spec}A\). The given isomorphism yields
\[
X\times\mathbb A^1\simeq\mathbb A^4.
\tag{2}
\]
It gives \(\dim X=3\). Even if affineness of \(A\) were not separately
stated, evaluation at \(s_*=0\) makes it a quotient of the finitely
generated algebra \(A[s_*]\).

For a closed maximal ideal \(\mathfrak m\subset A\), put
\(\mathfrak n=(\mathfrak m,s_*)\subset A[s_*]\). Then
\[
\dim A[s_*]_{\mathfrak n}=\dim A_{\mathfrak m}+1,\qquad
\operatorname{edim}A[s_*]_{\mathfrak n}
=\operatorname{edim}A_{\mathfrak m}+1.
\tag{3}
\]
The first local ring is regular, so \(A_{\mathfrak m}\) is regular.
Over the perfect field \(\mathbb C\), regularity at these closed
points gives smoothness of \(X\).

The homotopy \((x,z,t)\mapsto(x,(1-t)z)\) retracts
\(X\times\mathbb C\) onto \(X\times\{0\}\). Equation (2) therefore
makes \(X\) contractible. No assertion that arbitrary additive
quotients preserve contractibility is used.

Also \(A\) is a UFD with \(A^*=\mathbb C^*\). An irreducible of
\(A\) stays irreducible in \(A[s_*]\), since factors of an
\(s_*\)-constant element have degree zero in \(s_*\). It is then
prime in that UFD, and hence in \(A\). Noetherianity gives
factorizations. The same degree argument gives the units assertion.

### The dimension-three domination gate

Transport the product projection to a smooth surjective morphism
\[
P:\mathbb A^4\longrightarrow X.
\tag{4}
\]
Its differential has rank three everywhere. At a complex point \(v\),
choose a three-dimensional constant tangent subspace complementary
to \(\ker dP_v\), and translate it through \(v\) to an affine plane
\(L\simeq\mathbb A^3\). The differential of \(P|_L\) is an
isomorphism at \(v\). The complex inverse-function theorem gives a
Euclidean open subset in its local image. That subset is Zariski
dense in the irreducible smooth variety \(X\). Consequently
\[
P|_L:\mathbb A^3\simeq\mathbb A^1\times\mathbb A^2
\longrightarrow X
\quad\text{is dominant}.
\tag{5}
\]
Thus the source has exactly the dimension and product form required
by Corollary 2.8(2). Neither surjectivity nor birationality of this
restriction is needed. It is not assumed that \(s_*\) is an ambient
polynomial coordinate, or that the projection has a polynomial
three-space section.

### Action and finite generation

A nonzero complex LND of the affine algebra \(A\) exponentiates
to the required nontrivial algebraic action. Neither primitivity
nor a slice for \(D\) is required.

Finite generation of \(C\) is not deduced from being a subring of a
polynomial algebra. It is part of the affine-quotient conclusion in
the cited lemma. The underlying source input is explicit in Kaliman,
[*Free C+-actions on C3 are translations*](https://www.math.miami.edu/~kaliman/library/Ka.invent.2004.c%2B.pdf),
Introduction and Lemma 2.1, author PDF pp. 1–3: a factorial affine
threefold with a nontrivial additive action has an affine surface
quotient. That source invokes Zariski's theorem. Its Proposition 3.2
and Remark 3.3, pp. 5–8, supply surjectivity under the homological
hypotheses available here.

The actual \(X\) satisfies all these requirements. Apply
Corollary 2.8(2) using (5) to get \(C\simeq\mathbb C^{[2]}\).
This does not apply a theorem for LNDs on \(\mathbb C^{[3]}\) to
the unknown \(A\). The optional Miyanishi regular-subring alternative
in the inherited note is not needed for this audit.

## 3. Faithful flatness of the actual inclusion

Write \(C=\mathbb C[u,v]\). This is a coordinate choice in the
abstract quotient, not in the ambient \(A[s_*]\).

For a closed base point \(q=(u-\alpha,v-\beta)\), the fiber is a
nonempty curve. At a closed fiber point \(x\), the regular local
ring \(T=\mathcal O_{X,x}\) has dimension three. The ideal
\((u-\alpha,v-\beta)T\) has height two: two generators bound its
height above, and a height-one minimal component would be a surface
component of the fiber. Hence
\[
\dim T=3=2+1
=\dim C_q+\dim T/(u-\alpha,v-\beta)T.
\tag{6}
\]
The two equations are a regular sequence. Reducedness or smoothness
of the fiber has not been assumed.

[Miracle flatness, Stacks 00R4](https://stacks.math.columbia.edu/tag/00R4),
applies: \(C_q\) is regular, \(T\) is Cohen–Macaulay, and (6) is
the required dimension equality. Thus \(T\) is flat over \(C_q\),
and over \(C\).

The inherited passage from closed points to every point is also
valid. The map \(C\to A\) is finitely presented. By
[Stacks 00RC](https://stacks.math.columbia.edu/tag/00RC), its flat
locus is open. A nonempty closed subset of an affine complex variety
has a closed point, so the nonflat locus is empty. Both Stacks
statements and their complete displayed proofs were read directly.

Alternatively, for any prime \(\mathfrak p\subset A\), choose a
maximal ideal \(\mathfrak n\supset\mathfrak p\).
The already flat \(C\)-algebra \(A_{\mathfrak n}\) localizes to
\(A_{\mathfrak p}\), proving all-point flatness without an openness
citation.

Nonempty closed fibers imply \(\mathfrak mA\ne A\) for every
maximal ideal \(\mathfrak m\subset C\). A flat algebra satisfying
this is faithfully flat. This also gives surjectivity on all scheme
points, without silently upgrading a statement about complex points
at the start of the argument.

Closed fibers are purely one-dimensional by the height-two argument.
For a height-one base point, its prime generator remains prime in
\(A\) by factorial closure, and the domain fiber has transcendence
degree one over the residue field. The generic fiber is a line by
the local-slice theorem. No assertion of smoothness, reducedness,
or connectedness of all closed fibers follows.

## 4. The actual leading frame supplies a global nonzero action

The primary theorem does not manufacture an intrinsic LND from the
cylinder alone. In the degree-two branch the required action comes
from the already proved actual fields in
[pass42, Section 3](two-quadratic-degree-two-pass42.md).

Let \(E\) be the original sliced LND of
\(B=\mathbb C[x_1,x_2,x_3,x_4]=A[s_*]\). The two independent highest
bad-column fields \(V_3,V_4\) commute with \(E\) and are global
polynomial LNDs. Consequently \(V_i|_A\) are global LNDs of \(A\),
not just derivations of an invariant localization.

Highest-column local nilpotence has a direct uniform justification.
The conjugate
\(\exp(tE)T_i\exp(-tE)\) is an LND of \(B[t]\) fixing \(t\).
For each polynomial input, \(\exp(-tE)\) produces a polynomial of
finite \(x_i\)-degree, so a single power of \(T_i\) kills it before
conjugating back. If the conjugate has highest \(t\)-coefficient
\(V\), the highest coefficient in its \(N\)-fold iterate is
\(V^N\). Its local nilpotence thus proves local nilpotence of \(V\).
This is not an inference from separate LNDs at each numerical value
of \(t\).

If both restrictions vanished on \(A\), the two fields over
\(\operatorname{Frac}A(s_*)\) would be multiples of
\(E=\partial_{s_*}\), contrary to their independence. At least one
restriction \(D'\) is therefore nonzero. The established rank-one
restriction statement gives the same kernel for every nonzero
leading restriction. Thus the common ring used in
[the generic bad-pair proof](generic-bad-pair-pass44.md)
is exactly \(\ker D'\), so (1) applies.

Primitivity can be imposed without assuming a free tangent module.
Choose finite algebra generators \(a_i\) of the UFD \(A\), and let
\(\delta\) be the gcd of the nonzero values \(D'(a_i)\).
Then \(D'(A)\subseteq\delta A\), so \(\delta\mid D'(\delta)\).
The LND divisibility lemma gives \(D'(\delta)=0\). Therefore
\[
D=D'/\delta\in\operatorname{LND}(A),\qquad \ker D=\ker D'.
\tag{7}
\]
Indeed \((D')^n(a)=\delta^nD^n(a)\), and \(A\) is a domain.
The values of \(D\) on the generators have gcd one. This division
does not change the quotient inclusion or assume (1) in advance.

## 5. Downstream consequences and remaining limits

No downstream claim needs withdrawal because of this foundational
gate. The actual base is a Noetherian regular factorial surface;
ideals contract under \(C\subset A\), and regular sequences remain
regular after this faithfully flat base change. These are the inputs
used in the intrinsic plinth, image-module, divisor, and conic work.
Those later arguments still require their own separately stated
premises and proofs. This is not a new full audit of all of them.

The following stronger statements are not obtained:

- The cylinder alone does not supply this special leading frame.
  A nonzero intrinsic LND is nevertheless guaranteed by the general
  leading-extraction argument in [23](leading-derivation-pass23.md).
- Abstract polynomiality of the quotient does not make its generators
  ambient coordinates or split the actual invariant inclusion by
  an algebra retraction.
- Faithful flatness gives neither a global slice nor freeness.
  The inherited control \(x\partial_y+2y\partial_z\) has quotient
  \(\mathbb C[x,xz-y^2]\), double and disconnected fibers, and no
  retraction of that actual inclusion.
- Primitivity excludes a divisorial common factor of the vector field,
  not its entire fixed scheme.
- The theorem concerns the global affine \(X\), not arbitrary
  invariant localizations whose contractibility is unproved.

No mathematical correction to (1) was found. The publisher-access
limit in Section 1 is a source-record qualification only. No frozen
file, test, claim registry, or hash record was changed. No new checker
or regression run is claimed.

September 18 clarification: the first bullet formerly denied existence
of a nonzero intrinsic LND from the cylinder hypothesis. That clause
was too broad and contradicted the established general extraction.
The correction changes no quotient or flatness argument above; the
special leading-frame hypothesis remains additional.
