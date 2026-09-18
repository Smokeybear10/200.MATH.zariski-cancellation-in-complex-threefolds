# Fence plinths, commuting directions and the unresolved rank-three sector

The non-fence hypothesis in the previous homotopy obstruction covers
every primitive rank-three derivation of the original polynomial
three-ring. This is a consequence of an explicitly published rank
criterion, not a new rank theorem.

The same local-slice argument gives a useful intrinsic dichotomy
without assuming that the threefold is already affine space.
It distinguishes the availability of a second commuting direction
from the much stronger existence of a coordinate or slice.

## 1. The exact published rank criterion

Let \(R=\mathbb C^{[3]}\), let \(D\) be a nonzero primitive LND,
and let its nonzero nonunit full plinth be \(pC\), where
\(C=\ker D=\mathbb C^{[2]}\). Primitive means no nonunit common
divisor of its values.

Stampfli, Lemma 5.3.1, says that if \(\operatorname{div}(p)\)
is a fence, an adapted plane coordinate \(u\) with \(p\in\mathbb C[u]\)
is an ambient coordinate of \(R\). Remark 5.3.1 states exactly

\[
\operatorname{div}(p)\text{ is a fence}
\quad\Longleftrightarrow\quad
\operatorname{rank}(D)\leq2.
\tag{1}
\]

Both the lemma's proof and the following remark were read in the
primary manuscript.[^1] The reverse implication uses the established
two-variable-over-a-UFD derivation theory cited there.
Primitivity is necessary in (1): an invariant multiple of a translation
may have an arbitrary non-fence plinth while retaining rank one.

Under the nonunit plinth assumption a primitive rank-one derivation
is impossible, because its coefficient would be a unit. Thus the
fence and non-fence cases here correspond to rank two and rank three.

A later primary treatment records the equivalent minimal-local-slice
test: for a rank-three derivation, its minimal local-slice derivative
cannot be a polynomial in any coordinate of its invariant plane.
It also records the non-equivalent commuting-LND coordinate theorem.[^2]
These statements reinforce the attribution and do not enlarge the
ambient hypothesis from \(R=\mathbb C^{[3]}\) to an unknown threefold.

## 2. Consequence for the polynomial-base homotopy

Choose \(Dr=p\), take \(d\in\sqrt{pC}\), and form

\[
\mathcal B=R[\lambda,w]/((1+\lambda d)w-r),\qquad
\mathcal A=C[\lambda].
\tag{2}
\]

The [pass-25 normalizer theorem](nonfence-plane-rigidity-pass25.md)
and (1) give, for every primitive rank-three base,

\[
\begin{gathered}
\exists\,\delta\in\operatorname{LND}(\mathcal B),\
\delta(\lambda)=1,\
\delta(\mathcal A)\subseteq\mathcal A\\
\Longleftrightarrow\quad d\in pC .
\end{gathered}
\tag{3}
\]

There is no remaining factor-field or irreducibility exception
to (3) within rank three. It includes disconnected reduced support
because the prior relative theorem uses common residue one, not
a connectedness premise.

If \(p\) is squarefree, then \(\sqrt{pC}=pC\), and every \(d\)
in (2) is already in the explicit positive regime.
Hence a radical-only rank-three input not settled by that
plane-preserving construction necessarily has nonreduced plinth.
This is a search-space restriction, not a polynomiality theorem
for that remaining sector.

The fence case is already known to settle the individual
three-dimensional modifications. To be precise, fix
\(\lambda=c\in\mathbb C\), put \(v=1+cd\), and choose
\(pU+vG=1\). Then \(D+G\partial_t\) on \(R[t]\) has slice
\(Ur+vt\). An adapted fence coordinate \(u\) from Section 1
is an ambient coordinate of \(R\) and is fixed by this LND.
The Dedekind-base slice theorem with base \(\mathbb C[u]\)
therefore makes its kernel \(\mathbb C[u]^{[2]}\), hence

\[
R[r/v]\simeq\mathbb C^{[3]}.
\tag{4}
\]

The actual theorem and proof, including Corollary 4.5, were
checked in the author-uploaded primary text.[^3]

This statement is deliberately fiberwise. Applying the same
theorem uniformly to base \(\mathbb C[u,\lambda]\) would be
invalid because this base has dimension two and is not Dedekind.
No claim that all fence homotopies are parameter-preservingly
trivial follows from (4). An individual modified threefold,
the four-dimensional homotopy, and a trivialization preserving
its old invariant subalgebra are different targets.

## 3. An intrinsic commuting-direction dichotomy

The following direct argument isolates which parts do not need
the ambient threefold to be polynomial.

Let \(A\) be a finitely generated \(\mathbb C\)-domain that is a UFD.
Let \(D\) be a nonzero primitive LND such that

\[
C=\ker D=\mathbb C[u,h],\qquad
D(A)\cap C=pC,\qquad p\ne0,\quad p\notin C^*.
\tag{5}
\]

A minimal local slice \(r\) satisfies \(Dr=p\), and
\(A_p=C_p[r]\). Let \(\mathfrak L_D\) denote the LNDs of \(A\)
commuting with \(D\), including zero.

**Proposition.**

If \(\operatorname{div}(p)\) is not a fence, then

\[
\mathfrak L_D=CD.
\tag{6}
\]

If it is a fence, choose adapted plane coordinates with
\(p\in\mathbb C[u]\). There is an \(N\in\mathfrak L_D\)
independent of \(D\) over \(\operatorname{Frac}(A)\), and

\[
\ker D\cap\ker N=\mathbb C[u].
\tag{7}
\]

Every member of \(\mathfrak L_D\) kills \(u\) in this case.
Consequently its rational span has dimension exactly two,
whereas in (6) it has dimension one.

**Proof.** If \(L\) commutes with \(D\), it preserves \(C\)
and its restriction there is locally nilpotent.
It also preserves the plinth ideal: for \(f=Da\in C\),
\(L(f)=D(L(a))\in D(A)\cap C\).
Thus \(L(p)\in pC\). The LND divisibility lemma gives \(L(p)=0\).

If the restriction of \(L\) to \(C\) were nonzero,
the plane LND theorem would place \(p\) in a polynomial ring
in one coordinate of \(C\); equivalently its divisor would
be a fence. The same implication follows from the published
plane-divisor stabilizer result.[^1]
Thus in the non-fence case \(L|_C=0\).

On \(A_p=C_p[r]\), a \(C_p\)-linear LND is
\(a\partial_r\) with \(a\in C_p\).
Indeed a coefficient with positive degree in \(r\) has
nonvanishing iterates on \(r\). Hence \(L=(a/p)D\) on
the fraction field. The
[primitive UFD saturation lemma](commuting-leading-pass25.md)
makes the regular multiplier a polynomial in \(A\), and local
nilpotence makes it invariant. Therefore \(L\in CD\).
The converse follows from the invariant-multiple rule.

For the fence case, work first on \(A_p=C_p[r]\) and define
\(N_0=\partial_h\), killing \(u,r\).
Since \(p\in\mathbb C[u]\), this is an LND and commutes with
\(D=p\partial_r\). Choose finitely many algebra generators of \(A\).
Each \(N_0\)-image has a denominator that is a power of \(p\).
For a single sufficiently large integer \(m\),

\[
N=p^mN_0
\tag{8}
\]

sends all these generators into \(A\).
It therefore restricts to a derivation of \(A\); local nilpotence
descends from the localization because \(A\hookrightarrow A_p\)
is injective. Since \(N_0(p)=0\), the multiple remains LND and
commutes with \(D\). It is independent of \(D\), as
\(N(h)=p^m\ne0\) while \(D(h)=0\).
Their common kernel is precisely \(\mathbb C[u]\).

For any other commuting \(L\), the equality
\(0=L(p)=p'(u)L(u)\) and characteristic zero give \(L(u)=0\).
The space of derivations of the fraction field fixing
\(\mathbb C(u)\) has dimension two.
Together with the independent \(D,N\), this proves the final
dimension statement. \(\square\)

This is a direct application of local-slice, plane-action and UFD
mechanisms. Stampfli's Section 5.3 gives a stronger, primitive
admissible-complement construction when \(A=\mathbb C^{[3]}\).[^1]
The elementary denominator-cleared \(N\) in (8) is not claimed
primitive, fixed-point-free or sliced.

## 4. Why the intrinsic version does not finish cancellation

For a threefold \(A\) with \(A[s]=\mathbb C^{[4]}\), the
previous [quotient-plane proof](intrinsic-quotient-surface-pass.md)
and its flatness argument give the relevant invariant-plane
geometry for nonzero intrinsic LNDs. The existing leading
construction supplies a nonzero intrinsic action.

Applying the proposition to a primitive such action, when its
full plinth is principal as in (5), determines whether a second
commuting direction exists. It does not turn \(u\) in (7) into
an ambient coordinate of \(A[s]\), nor an affine-plane-fiber
coordinate of \(A\). Stampfli's coordinate conclusion and the
commuting-LND coordinate theorem used above require the
three-dimensional ambient ring to be polynomial already.

In the non-fence case, a new useful intrinsic action must fail
to commute with \(D\) or must be reached through a genuinely
different orbit direction. In the fence case, the pair \(D,N\)
is available, but it need not be free or provide a slice.
A pair of commuting directions with generic rank two is not
a replacement for the missing global recognition hypothesis.

The [moving-plane control](moving-plane-lie-pass26.md)
tests a separate danger: an unrestricted horizontal action
need not leave even one common nonconstant invariant with the
vertical action. Hence a strategy demanding a new joint
invariant plane would require an additional theorem.

## Sources

[^1]: I. Stampfli, [*Automorphisms of C^3 Commuting with a C+-Action*](https://arxiv.org/pdf/1406.6246v2), arXiv:1406.6246v2, Lemma 5.3.1, Remark 5.3.1, Lemma 5.3.2 and its proof, printed pp. 9-10; also Proposition 3.0.3 and Lemma 4.1.1 for the inherited plane-action and UFD facts. Section 5.3 was read completely through Remark 5.3.4. Equation (1) is explicitly published.
[^2]: N. Dasgupta and S. Gaifullin, [*On locally nilpotent derivations of polynomial algebra in three variables*](https://arxiv.org/pdf/2306.00510), primary manuscript, Proposition 2.14, Lemma 2.15 and Proposition 5.3. These precise statements were read directly. The published article is in *Sbornik: Mathematics* 216(4) (2025), 456-484. The polynomial ambient hypothesis is essential.
[^3]: H. Derksen, A. van den Essen and P. van Rossum, [*The Cancellation Problem in Dimension Four*, author-uploaded primary manuscript](https://www.researchgate.net/publication/228571174_The_cancellation_problem_in_dimension_four), Nijmegen Report 0022 (October 2000), Theorem 4.4 and Corollary 4.5, printed pp. 8-9, both statements and proofs read directly. The invocation uses the Dedekind base \(\mathbb C[u]\), not the two-dimensional base \(\mathbb C[u,\lambda]\).
