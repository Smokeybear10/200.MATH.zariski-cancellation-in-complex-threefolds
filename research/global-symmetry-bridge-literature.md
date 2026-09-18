# Global symmetry bridges: centralizers, normalizers, and quotient actions

The exact source match for restriction up to a noninvariant multiplier
is the known quasi-extension lemma. It gives an all-degree sufficient
criterion when a slice LND is projectable, up to a factor, to an actual
coordinate plane. The full derivation centralizer also has maximal
generic rank, but this does not produce a maximal-rank family of LNDs.
A separate elementary reduction turns a rationally normalized LND
direction into a commuting primitive LND. These statements do not
force the required coordinate plane for an arbitrary slice.

## 1. A large centralizer does not imply many additive actions

[Bedratyuk, Chapovskyi and Petravchuk, *Centralizers of linear and
locally nilpotent derivations*, Proposition 2 and Theorem 4](https://arxiv.org/pdf/2302.02441),
give the following statements. In Section 4 the field has characteristic
zero and the algebra is a finitely generated domain.

If a nonzero LND \(D\) has a slice and \(C=\ker D\), Proposition 2
identifies its Lie-algebra centralizer as
\[
C_{\operatorname{Der}_k A}(D)\cong C\rtimes\operatorname{Der}_k C,
\]
where the first summand is abelian. Concretely, for \(A=C[s]\), a
commuting derivation is \(a\partial_s+\delta\), with \(a\in C\),
\(\delta\in\operatorname{Der}_k C\), and \(\delta(s)=0\).

Theorem 4 does not require a slice: the generic rank of the full
centralizer is \(\operatorname{trdeg}_k A\). Its proof extends
partials from a transcendence basis to a function field and clears
denominators. It does not show those resulting derivations are LNDs,
nor that they commute with each other. Thus the theorem applies to our
four-variable slice setup, but supplies neither four additive actions
nor a polynomial coordinate frame. The local nilpotence needed by a
commuting-actions recognition theorem remains an additional condition.

## 2. An explicit quotient-action guardrail, even with two slices

The following direct example is not attributed to a source. On
\(B=\mathbb C[s,x,y,z]\), put
\[
E=\partial_s,\qquad U=\partial_s+x\partial_y.
\]
They commute, are generically independent, and both have slice \(s\).
Both are nice in the displayed frame. Moreover \(U\) is a coordinate
LND: in coordinates \((s,x,y-xs,z)\), it is \(\partial_s\).

Nevertheless, on \(\ker E=\mathbb C[x,y,z]\), the induced action is
\[
U|_{\ker E}=x\partial_y.
\]
It fixes the divisor \(x=0\), has no slice, and is not proper: at a
fixed point its stabilizer is the nonproper algebraic group
\(\mathbb G_a\). Hence a commuting nice coordinate LND with a slice
does not automatically descend to a proper or slice action on the
original quotient. This blocks that inference, not cancellation; the
kernel in this example is already polynomial.

## 3. A published four-variable example keeps the slice hypothesis essential

[Deveney and Finston, *Additive group actions with finitely generated
invariants*, Osaka J. Math. 44 (2007), 91–98](https://doi.org/10.18910/6947),
was read in its [original university-hosted PDF](https://ocu-omu.repo.nii.ac.jp/record/2010092/files/111F0000002-04401-4.pdf).
Example 1, page 96, uses
\[
D=x\partial_y+y\partial_z+(y^2-2xz-1)\partial_w.
\]
It is fixed-point-free and commutes with the coordinate LND
\(\partial_w\). The paper gives its invariant algebra and identifies
an isolated singular point. Thus its kernel is not a polynomial
three-ring, and the derivation cannot have a slice on smooth
four-space. A direct fixed-point check is that simultaneous vanishing
of \(x,y\) leaves the last coefficient equal to \(-1\).

This example rules out replacing the slice by fixed-point-freeness in
a proposed recognition argument based only on a commuting coordinate
action. Theorem 3.1 of the same paper assumes a GICO action on
\(\mathbb C^4\), finitely generated regular invariants, and a smooth
complement of the quotient image whose components are disjoint. Its
conclusion is equivariant triviality, meaning existence of a slice.
It is not a theorem recognizing an already existing slice's kernel as
\(\mathbb C^{[3]}\).

## 4. Rational normalization reduces to primitive commutation

This is a self-contained algebraic observation, not a theorem located
in the source search. Let \(B=k[x_1,\ldots,x_n]\), characteristic
zero, and let \(E,U\) be LNDs, with \(U\ne0\). Suppose
\[
[E,U]=hU,\qquad h\in\operatorname{Frac}B.
\]
Divide the coefficients of \(U\) by their gcd \(g\), obtaining
\(U=gU_0\) with primitive polynomial coefficients. Since
\(g\mid U(g)\), LND degree gives \(U(g)=0\). Thus \(U_0(g)=0\),
and \(U^j(f)=g^jU_0^j(f)\) shows that \(U_0\) is an LND with the
same kernel. If \(U\) was nice, \(U_0\) remains nice.

Now
\[
[E,U_0]=qU_0,\qquad q=h-\frac{E(g)}g.
\]
The left side is polynomial. Any prime in a reduced denominator of
\(q\) would divide all coefficients of \(U_0\); primitivity therefore
gives \(q\in B\). No unit-ideal hypothesis is needed.

The conjugate
\[
U_t=\exp(tE)U_0\exp(-tE)
\]
has coefficients polynomial in \(t\), since both exponential maps
are polynomial on the finitely many generators. Differentiation gives
\[
\frac{dU_t}{dt}=\exp(tE)(q)U_t.
\]
For any coefficient \(p(t)\ne0\) of \(U_t\), this implies
\(p'(t)=\exp(tE)(q)p(t)\). Over \(\operatorname{Frac}B[t]\), the
degree of a nonzero derivative is smaller than that of \(p\); it
cannot equal the degree of a nonzero polynomial multiple of \(p\).
Consequently \(\exp(tE)(q)=0\), so \(q=0\) and
\[
[E,U_0]=0.
\]
This needs neither the slice hypothesis nor a dimension bound. It
reduces rational normalization of one LND direction to the commuting
case; it does not bound the coordinate rank of that direction or
identify its quotient.

## 5. Exact overlap: quasi-extensions require no invariant multiplier

[Freudenburg and Moser-Jauslin, *Locally nilpotent derivations of rings
with roots adjoined*, Section 2.1, Lemma 2.1](https://moser.perso.math.cnrs.fr/adjoinedroots.pdf),
states precisely the multiplier lemma needed here. The author preprint
is dated July 28, 2010; the article appeared in Michigan Math. J. 62
(2013), 227–258, [DOI 10.1307/mmj/1370870372](https://doi.org/10.1307/mmj/1370870372).

Let \(B\) be an integral domain containing \(\mathbb Q\), let
\(R\subset B\) be a subring, and suppose a derivation \(E\) of
\(B\) satisfies
\[
E(f)=hD(f)\quad(f\in R),\qquad 0\ne h\in B,
\]
where \(D\) is a derivation of \(R\). This is a quasi-extension.
If \(E\) is locally nilpotent, so is \(D\). There is no assumption
\(E(h)=0\), nor a finite-generation or coordinate-ring assumption.
The paper cites Freudenburg's first-edition monograph, Lemma 5.38.
The second edition uses Lemma 2.35.

Source-access qualification: the original author PDF's complete
Section 2.1, including the definition and lemma, was readable in its
indexed text. Direct downloads of that PDF timed out, and the published
PDF was not successfully fetched. The source statement is verified;
the published PDF's numbering was not separately compared.

For completeness, our independent elementary proof is short. Give
nonzero elements their nonnegative \(E\)-degree \(\nu\). Whenever
\(D(f)\ne0\), multiplicativity and the LND degree rule yield
\[
\nu(Df)=\nu(f)-\nu(h)-1.
\]
Successive nonzero \(D\)-iterates would strictly decrease a
nonnegative integer, which is impossible. This proof never
differentiates \(h\), so no invariance hypothesis is hidden in it.

## 6. Coordinate-plane consequences and the known intersection theorem

If a polynomial LND \(E\) of \(\mathbb C[a,b,z,w]\) preserves the
function field \(\mathbb C(a,b)\), then it preserves the polynomial
plane \(\mathbb C[a,b]\):
\[
E(a),E(b)\in\mathbb C(a,b)\cap\mathbb C[a,b,z,w]
=\mathbb C[a,b].
\]
The restriction is an LND. If nonzero, Rentschler supplies an invariant
plane coordinate; if zero, both plane coordinates are invariant.
Either way there is an ambient invariant coordinate. In the slice
setup, the existing regular-kernel theorem finishes recognition.

There is a stronger consequence of the quasi-extension lemma. Assume
\(E(b)\ne0\) and
\[
\frac{E(a)}{E(b)}\in\mathbb C(a,b).
\]
Write this ratio \(P/Q\) with coprime \(P,Q\in R=\mathbb C[a,b]\).
The identity \(Q E(a)=P E(b)\), unique factorization, and the
polynomial extension \(B=R[z,w]\) give
\(E(a)=hP\), \(E(b)=hQ\), with \(h\in B\). Thus
\(E|_R=h(P\partial_a+Q\partial_b)\). Quasi-extension descent and
Rentschler provide an invariant coordinate of \(R\), hence of \(B\).
If either image vanishes, that coordinate is already invariant.
This is a consequence of known results, not a new multiplier theorem.
The factor need not be invariant, and coprimality is used through prime
divisibility, not an invalid two-variable Bezout identity.

There is also an exact published intersection result.
[Freudenburg, *Algebraic Theory of Locally Nilpotent Derivations*,
second edition, Appendix to Chapter 5, Theorem 5.41 and Corollary 5.42](https://doi.org/10.1007/978-3-662-55350-3_5)
has the following hypotheses: \(U\) is a UFD over a characteristic-zero
field \(k\); \(0\ne D\in\operatorname{LND}(U)\); \(A=\ker D\);
\(S=R[u,v]\cong R^{[2]}\subset U\) is factorially closed; and
\(R\subsetneq S\cap A\subsetneq S\). Its conclusion is
\(S\cap A=R[w]\) and
\(\operatorname{Frac}(R)[u,v]=\operatorname{Frac}(R)[w]^{[1]}\).
When \(R\) is a field, Corollary 5.42 gives \(S=R[w]^{[1]}\).
The appendix explicitly credits its theorem and proof to Daigle and
Freudenburg. The displayed proof uses quasi-extension descent.

Corollary 5.43 applies this to any polynomial \(n\)-ring: if a
nonconstant invariant belongs to an actual coordinate plane, an
invariant coordinate of that plane exists, unless the whole plane is
already fixed. It identifies the earlier source as Theorem 2 of
Freudenburg's [*A note on the kernel of a locally nilpotent derivation*,
Proc. AMS 124 (1996), 27–29](https://doi.org/10.1090/S0002-9939-96-03003-1).
The appendix statement and proof were read in full; the earlier
three-page PDF was not fetched, so the appendix is the directly
inspected source for this implication.

All these criteria require an actual polynomial coordinate plane,
which may be nonlinear in the displayed coordinates. An abstract
rational subfield or a plane defined only by linear forms does not
substitute for that requirement. None of the inspected statements
forces such a plane for every four-variable slice LND.

## 7. Other source hit and coverage limits

[Finston and Walcher, *Centralizers of locally nilpotent derivations*,
JPAA 120 (1997), 39–49](https://doi.org/10.1016/S0022-4049(96)00064-3),
advertises a triangulability criterion from polynomial centralizers.
Only the original publisher abstract was recovered here. Its exact
criterion is not asserted or used. This remains a precise source lead,
not a theorem with presumed applicability.

Queries covered commuting actions on four-space, commuting slice
LNDs, nice centralizers, rational normalizers, and coordinate-frame
reduction. No automatic rank-two quotient theorem or global
low-commutator-height theorem was verified. The already checked
three-variable commuting-pair, regular invariant-coordinate, and
proper triangular four-space theorems retain their explicit
dimensional and presentation assumptions.

The outcome is an exact known quasi-extension lemma and coordinate-plane
recognition result, a normalizer-to-commutator reduction, a centralizer
structure theorem with a crucial non-LND boundary, and two guardrails
against stronger quotient-action inferences. There is no novelty or
exhaustive-coverage claim.

## 8. Dated status and an excluded inconsistent survey

[Huang, Nazemian, Wang and Zhang, *Relative Cancellation*, November 9,
2025 revision](https://arxiv.org/html/2503.10083v3), Introduction,
explicitly states that characteristic-zero polynomial-ring cancellation
remains open in dimensions at least three. Its exact author list is
Hongdi Huang, Zahra Nazemian, Yanhua Wang and James J. Zhang. This
original research source supports a dated status statement, not an
exhaustive verification of every later manuscript.

The February 17, 2026 revision of [Venegas and Venegas,
*Cancellation problem via locally nilpotent derivations*](https://arxiv.org/html/2512.15590v2)
is excluded as an authority here. Its introduction calls the classical
characteristic-zero problem open, but Example 2.6 claims that complex
Russell–Koras threefolds have affine-four-space cylinders and refute
cancellation. These statements are internally incompatible. The
manuscript also states an unconditional Makar-Limanov stability theorem;
no theorem from it is used in this investigation. Detecting the
contradiction does not require treating a search-result summary as a
proof or resolving all its other claims.

The [2026 Brieskorn–Pham cancellation paper](https://arxiv.org/abs/2606.26890)
concerns the singular varieties specified in its abstract and does not
claim the unrestricted smooth affine-three-space theorem. A restricted
cancellation theorem in a recent title does not establish (1) of the
main report. The exact quasi-extension source overlap and the actual
nonlinear coordinate-construction gap remain the conclusions of this
bounded audit.
