# Invariant slice kernels as principal affine modifications

Private bounded pass 18. The exact reduction below is proved algebraically.
It does not establish that every resulting modification is polynomial.
No novelty claim, human expert review, or Lean verification is asserted.
The extension from affine slices to arbitrary slices inherits the
source-dependent [pass-17 affine-replacement proof](general-invariant-affine-pass17.md).

## 1. Exact two-way reduction

Let
\[
R=\mathbb C^{[3]},\quad 0\ne D\in\operatorname{LND}(R),\quad
C=\ker D,\quad P_D=pC,\quad Dr=p.
\]
Here \(C\cong\mathbb C^{[2]}\) and the plinth ideal is principal by
the three-variable results collected in Freudenburg's Theorem 2.4.[^1]
The choice of \(r\) is a minimal local slice. For \(A,B\in C\), put
\(E=AD+B\partial_t\). If \(E\) has an affine slice, its coefficient
comparison, followed by the choice of the generator \(p\), supplies
\(U,V\in C\) with
\[
ApU+BV=1,\qquad s=Ur+Vt,\qquad E(s)=1.                 \tag{1}
\]
This step is elementary for affine slices; using it for an arbitrary
slice invokes pass 17. Invariant summands commute, so \(E\) is locally
nilpotent. Assume first \(V\ne0\).

**Proposition.** There is an isomorphism fixing \(C\)
\[
\ker E\ \cong\ R[t]/(Ur+Vt)\ \cong\ R[r/V]
\subset\operatorname{Frac}(R).                         \tag{2}
\]
The last ring contains a copy of \(R\) coming from the quotient map;
this is not a claim that the original \(R\subset R[t]\) is invariant.

**Proof.** The slice theorem identifies the first two rings and makes
the quotient a domain. The ideal \((Ur+Vt)\) meets \(R\) in zero:
a nonzero multiple of this polynomial has positive degree in \(t\).
Thus the quotient embeds into its localization over \(\operatorname{Frac}(R)\),
where \(t=-Ur/V\). Its image is \(R[Ur/V]\).
Equation (1) gives
\[
\frac rV=Ap\frac{Ur}{V}+Br,
\]
so that image equals \(R[r/V]\). Also (1) gives both
\((U,V)C=C\) and \((p,V)C=C\). This proves (2).

For completeness, the modification has the exact hypersurface presentation
\[
R[r/V]\cong R[w]/(Vw-r).                              \tag{3}
\]
Indeed, a common irreducible divisor \(d\) of \(V\) and \(r\) in
the UFD \(R\) belongs to \(C\), since LND kernels are factorially
closed. It would divide \(Dr=p\), contradicting \((p,V)C=C\).
Thus \(Vw-r\) is primitive and irreducible over \(R\), and Gauss's
lemma identifies the kernel of evaluation \(w\mapsto r/V\).

**Converse.** Start with any such \(D,r,p\), and any nonzero
\(V\in C\) with \((p,V)C=C\). Choose \(U,B\in C\) satisfying
\(pU+BV=1\). Then \(D+B\partial_t\) has slice \(Ur+Vt\), and
(2) identifies its kernel with \(R[r/V]\). In particular,
\[
R[r/V]^{[1]}\cong\mathbb C^{[4]}.                     \tag{4}
\]
Consequently the arbitrary-invariant-extension affine-slice kernel
question is *equivalent* to polynomial recognition for these specific
principal modifications. The coefficient \(A\) is unnecessary for this
recognition problem. This is not an equivalence with full cancellation:
no reduction of an arbitrary slice derivation on \(\mathbb C^{[4]}\)
to an invariant extension has been established.

Boundary cases are explicit. If \(V\) is a nonzero constant, (2) is
\(R\). If \(p\) is a nonzero constant, the slice theorem gives
\(R=C[r]\), hence \(R[r/V]=C[w]\) for every nonzero \(V\).
If \(V=0\) in (1), then \(ApU=1\), so \(A,p,U\) are nonzero
constants. Again \(R=C[r]\), and the determinant-one matrix with
rows \((B,-Ap)\), \((U,V)\) gives polynomial kernel
\(C[Br-Apt]\). The case \(A=0\) simply forces \(B\) to be a unit
and also has polynomial kernel. A zero original derivation, excluded
from the notation, reduces to that same elementary case.

For an invariant replica \(D=hD_0\), the plinth ideals satisfy
\(P_D=hP_{D_0}\). The same \(r\) satisfies \(D_0r=p/h\), and
\((p/h,V)C=C\). Thus this modification problem can be restricted to
primitive bases after the usual invariant-replica factorization.

## 2. The exact charts and the failed relative patching shortcut

Set \(M=R[r/V]\), with \(w=r/V\). The comaximality of \(p,V\)
gives a two-open cover of \(\operatorname{Spec}C\), on which
\[
M_V=R_V,\qquad R_p=C_p[r],\qquad M_p=C_p[w].             \tag{5}
\]
The transition on the overlap is exactly \(r=Vw\).
In affine-modification terminology, this replaces the divisor \(V=0\)
by the exceptional divisor over the center \((V,r)\).[^2]
The entire center is outside the plinth support, and even for nonreduced
\(V\) one has
\[
R/(V)=(C/(V))[r],\quad R/(V,r)=C/(V),\quad
M/(V)=(C/(V))[w].                                      \tag{6}
\]
To verify (6), invert \(p\), which is already a unit modulo \(V\),
and use (3) and (5).

This does not exhibit a line bundle over \(\operatorname{Spec}C\).
The chart \(R_V\) can include the entire plinth support and need not
be \(C_V[r]\). The overlap scaling need not extend to an automorphism
of that chart. Picard-group triviality of the affine plane is therefore
not a proof of polynomiality.

There is a concrete obstruction to demanding an isomorphism fixing
the invariant ring. In the pass-17 example with
\(C=\mathbb C[f,h]\), \(p=f^nh\), \(n\ge2\), take
\[
B=1+fh,\qquad U=(-1)^nh^{n-1},\qquad
V=\sum_{j=0}^{n-1}(-fh)^j.
\]
Then \(pU+BV=1\), so its kernel is precisely a modification of (2).
The [relative Danielewski calculation](danielewski-relative-pass17.md),
using Poloni's Corollary 3.3(1), proves that it is **not** isomorphic
to \(R\) over \(\mathbb C[f,h]\).[^3] Nevertheless the
[finite-jet construction](nonreduced-coordinate-lift-pass17.md)
proves that it is abstractly \(\mathbb C^{[3]}\). Any general argument
must allow the embedding of the invariant plane to change. This is a
negative result for the stronger relative statement, not a counterexample
to the requested absolute statement.

## 3. Exact primary results and their scope

Derksen, van den Essen, and van Rossum, Theorem 4.4, prove that a slice
LND on \(S[X,Y,Z]\), with \(S\) a Dedekind domain containing
\(\mathbb Q\), has kernel \(S^{[2]}\). Their Corollary 4.5 therefore
settles slice derivations on four-space having an ambient coordinate
\(q\) with derivative in \(\mathbb C[q]\). Local nilpotence makes
that derivative zero or constant. This settles our rank-at-most-two
bases, since they have an invariant ambient coordinate. An abstract
generator of \(C=\mathbb C^{[2]}\) is not a substitute for that
ambient-coordinate hypothesis.[^4]

Kaliman, Vénéreau, and Zaidenberg's main simple-extension results study
\(a(x,y)w+g(x,y,z)\) in an **ambient coordinate system** \(x,y,z\).
Knowing only \(V\in\ker D\) does not put \(Vw-r\) in that form.
Their Theorem 1.7 gives a separate useful criterion: a smooth acyclic
affine threefold is affine three-space if it has a regular function all
of whose fibers are affine planes. Our \(\operatorname{Spec}M\) is
smooth and contractible by (4), but no such function is supplied by
the two charts (5).[^2] Only the stated all-fibers criterion is
invoked here, not the preceding manuscript remark about general fibers.

Ghosh and Gupta's Theorem B, numbered Theorem 3.10 in the body, treats
coefficient \(\prod X_i^{r_i}\), \(r_i>1\), and numerator
\(F=f(Z,T)+(\prod X_i)g\), with \(f\ne0\). Its equivalent
polynomiality and coordinate conclusions depend on that ambient
monomial presentation. Their Theorem A records the one-coordinate-power
case. Neither statement directly covers a general invariant \(V\).[^5]

These are verified hypothesis comparisons, not evidence from failure
to find a paper. This bounded audit does not establish priority, nor
does it assert that no other theorem settles a larger subcase.

## 4. Precise remaining lemma

The unrestricted target is now:

> For every primitive LND \(D\) of \(R=\mathbb C^{[3]}\), every
> minimal local slice \(Dr=p\), and every nonzero \(V\in\ker D\)
> with \((p,V)=1\), the ring \(R[r/V]\) is abstractly
> \(\mathbb C^{[3]}\).

This target remains unproved here. A strictly bounded next case is the
**radical-congruence lift**: prove that assertion when the primitive
plinth support is connected and \(V=c+p_{\mathrm{red}}Q\),
\(c\ne0\), without assuming an invariant ambient coordinate or a
specific local-slice equation. The
[independently audited plinth-unit argument](plinth-units-pass18.md)
forces exactly this congruence for connected support and already settles
the squarefree-plinth case. The missing part is the higher-order
thickening, not coprimality on the reduced curve. Disconnected support
is a separate case and has not been excluded.

One exact sufficient geometric sublemma is to construct a regular
function on this modification with every fiber \(\mathbb A^2\),
without requiring it to lie in the original \(C\). Theorem 1.7 then
finishes recognition. No construction of that function is asserted.

A separate algebraic reconstruction checked the primitive linear
relation, lack of denominator torsion, both local charts, and the
converse construction. It found no gap. The main agent also read the
exact Derksen--van den Essen--van Rossum statements and proof and the
KVZ and Ghosh--Gupta theorem statements; no broader consequence was
inferred from their titles.

## Sources

[^1]: G. Freudenburg, *Actions of SL2(k) on affine k-domains and fundamental pairs*, [arXiv:2108.12021v2, Theorem 2.4](https://arxiv.org/pdf/2108.12021v2). The general affine-replacement inference is the separately linked project proof, not a claim quoted from this theorem.

[^2]: S. Kaliman, S. Vénéreau, M. Zaidenberg, *Simple birational extensions of the polynomial algebra C[3]*, *Transactions of the AMS* **356** (2004), 509–555; [primary manuscript, arXiv:math/0104204v2](https://arxiv.org/pdf/math/0104204). Directly read the introduction, Notation 1.1, and Theorem 1.7. The theorem is used as a conditional criterion only.

[^3]: P.-M. Poloni, *Classification(s) of Danielewski hypersurfaces*, *Transformation Groups* **16** (2011), 579–597; [arXiv:0912.3241, Corollary 3.3(1)](https://arxiv.org/pdf/0912.3241). The explicit specialization and first-order contradiction are written in the linked local proof.

[^4]: H. Derksen, A. van den Essen, P. van Rossum, *The Cancellation Problem in Dimension Four*, University of Nijmegen report 0022, October 2000, Theorem 4.4 and Corollary 4.5. Directly read [author-uploaded primary manuscript](https://www.researchgate.net/publication/228571174_The_cancellation_problem_in_dimension_four), including the complete statements and proofs. No account or paid access used.

[^5]: P. Ghosh and N. Gupta, *On the triviality of a family of linear hyperplanes*, [arXiv:2206.15210v5, Theorems A and B](https://arxiv.org/pdf/2206.15210). Exact forms read in the introduction; Theorem B is identified there as Theorem 3.10.
