# Independent audit of the pointwise plinth argument

The argument in [the pointwise note](pointwise-plinth-pass17.md) survives
this audit. Under its stated hypotheses, a reduced scheme-theoretic
single-line fiber of a primitive additive-group quotient of
\(\mathbb A^3_{\mathbb C}\) lies outside the plinth support. The
normalization support step closes the escaping-branch issue; it does
not assume the quotient morphism is proper or that the normalized
intermediate map is surjective.

This is an independent proof reconstruction using the cited published
inputs, not human peer review, a formal proof-assistant certificate,
or an assertion of priority. It does not prove threefold cancellation.

## 1. Scope and source verification

I read the complete eight-section pointwise note and the primitive
support identification in the preceding
[whole-component note](whole-plinth-component-pass16.md). I checked
Kaliman's final author version directly, including Lemmas 2.1 and 2.2,
Lemma 3.1, the diagram and excision argument in Proposition 3.2,
Remark 3.3, Proposition 4.2, and Theorem 5.2(i).[^1]

The source supplies a retained exceptional curve, product outside it,
the actual finite intermediate curve factorization, and the homology
diagram. Its retained component maps are nonbijective. The explicit
invocation of Proposition 3.2 Step 1 in Proposition 4.2 upgrades this
to nonbirationality in this setting. No general assertion that a
nonbijective finite map of singular curves has degree greater than
one is being used.

The proposed pointwise statement is a deduction from those inputs,
not a theorem quoted from Kaliman. The support refinement and the
normalization calculation must therefore remain in the proof rather
than being replaced by a citation to Proposition 3.2 alone.

## 2. The local topological map has the required type

Write \(L=\pi^{-1}(F)\), \(X^*=X\setminus L\), and
\(\widehat X=X\setminus E\). For an arbitrary Euclidean open
neighborhood \(U\supset L\), excision gives

\[
H_4(U,U\setminus L;\mathbb Q)
\cong H_4(X,X^*;\mathbb Q).
\tag{A1}
\]

Since \(H_4(X)=H_3(X)=0\), every class in \(H_3(X^*)\) is the
boundary of a relative class on the right. Applying the boundary
map on the left gives a representative in \(H_3(U\setminus L)\).
The correctly typed local Thom calculation is

\[
\begin{aligned}
H_3(U\setminus L)
&\longrightarrow
H_3(U\setminus L,U\setminus E)\\
&\xrightarrow{\mathrm{Thom}}
H_1(E^*\cap U)
\longrightarrow H_1(E^*)
\xrightarrow{\kappa_*}H_1(Z^*).
\end{aligned}
\tag{A2}
\]

The Thom isomorphism applies because \(E^*\cap U\) is a closed
smooth real-codimension-two submanifold of \(U\setminus L\),
with its complex normal orientation. Its naturality for open
inclusions identifies (A2) with the image under \(\phi'\) of the
original class. Ordinary singular homology suffices, including for
noncompact \(U\) and \(L\). No compactness of the entire fiber
enters (A1) or (A2).

Consequently the image of \(\phi'\) is supported in the image of
\(H_1(E^*\cap U)\) for every such \(U\). This is the exact
strength needed later. It does not assert that the full homology of
an arbitrary neighborhood equals that of the fiber.

The middle vertical map in the global diagram is \(\theta_*\),
not a weighted transfer. The inverse-image divisor is reduced, so
the local normal degree is one; the finite covering degree along
the divisor is already accounted for by \(\theta_*\). Thus the
right vertical isomorphism gives

\[
\theta_*\beta\in\operatorname{im}\phi
\quad\Longrightarrow\quad
\beta\in\operatorname{im}\phi'.
\tag{A3}
\]

## 3. Exactly one reached branch over each base branch

Let \(Y=\pi^{-1}(p)\) be the reduced scheme-theoretic affine
line. The quotient is flat and finitely presented. The pointwise
smoothness criterion makes \(\pi\) smooth at every point of
\(Y\). The exact Stacks statement is Lemma 29.35.14, implication
(2) to (1), not merely the statement concerning all fibers.[^2]

On the resulting open smooth locus containing \(Y\), the map
\(E_i\to\Gamma_i\) is the base change of a smooth morphism.
Normalization commutes with this smooth base change.[^3] More
concretely, base changing by \(\Gamma_i^\nu\to\Gamma_i\)
produces a normal scheme, finite and birational over that open
part of \(E_i\). It is its normalization. This also explains
why the relative-normalization formulation of Stacks applies to
the absolute normalization used here.

For each normalization point \(p_j\) of \(\Gamma_i\) over
\(p\), the normalized exceptional surface therefore has exactly
one copy \(Y_j\cong Y\) in its fiber over \(p_j\). The lift
\(E_i^\nu\to Z_i^\nu\) exists by the universal property of
normalization and dominance. It maps connected \(Y_j\) to one
point \(\zeta_j\) in the finite set over \(p_j\).

The map \(\theta_i^\nu:Z_i^\nu\to\Gamma_i^\nu\) is finite:
on coordinate rings, the integral closure of \(\mathcal O(\Gamma_i)\)
in the finite function-field extension also contains
\(\mathcal O(Z_i^\nu)\), and the two coincide by integrality.
Equivalently, normalize a finite map of algebraic curves. Both
normalizations are smooth curves over \(\mathbb C\).

At a reached point \(\zeta_j\), take local parameters \(u,v\)
downstairs and upstairs. If
\(\theta_i^{\nu*}u=\varepsilon v^e\) with \(e>1\), its pullback
has zero differential on \(Y_j\). This contradicts the smooth
map \(E_i^\nu\to\Gamma_i^\nu\) along that fiber. Therefore
\(e=1\). Finite degree \(d_i\ge2\) supplies an additional
point over every \(p_j\), and that point is not reached by
\(Y_j\).

This argument deliberately allows the unreached point to lie over
the same singular point of \(Z\) as the reached point. Connectedness
of \(\kappa(Y)\) does not separate those normalization branches.

## 4. The whole-fiber neighborhood is valid

Let \(N=E^\nu\) and let \(\nu:N\to E\) be normalization.
Choose disjoint small disks in \(Z^\nu\) around the finitely
many points above \(p\), retaining only the disk about the one
reached point for each base branch. The inverse image \(O\subset N\)
of those disks is open and contains all of \(\nu^{-1}(Y)\).

The last assertion uses the smooth-base-change calculation, not
surjectivity after normalization: the entire inverse image consists
of the copies \(Y_j\), each sent to its selected point. Finite
normalization is proper and closed in the complex topology, so

\[
W=E\setminus\nu(N\setminus O)
\tag{A4}
\]

is open, contains all of \(Y\), and satisfies
\(\nu^{-1}(W)\subset O\). Since \(E\) is closed in \(X\),
there is an ambient Euclidean open \(U_p\supset Y\) with
\(E\cap U_p\subset W\).

Shrink \(U_p\) inside the inverse image of a base neighborhood
excluding \(F\setminus\{p\}\). On \(E^*\), normalization is
an isomorphism. Thus \(\kappa(E^*\cap U_p)\) lies in punctured
disks belonging only to reached points. For every other \(q\in F\),
choose analogous neighborhoods allowing all normalized branches
over \(q\). They can be disjoint by choosing disjoint base
neighborhoods first.

Apply (A2) to their union. The result is precisely

\[
\operatorname{im}\phi'
\subset V_p^{\rm reach}+
\sum_{q\in F\setminus\{p\}}V_q.
\tag{A5}
\]

Noncompactness of \(Y\) creates no missing uniformity assumption:
(A4) is a neighborhood of its entire inverse image at once. The
proper map used here is \(\nu\), not \(\pi\) or \(\kappa\).

## 5. Peripheral independence and the contradiction

Each connected component of \(Z^*\) is obtained from the smooth
projective completion of a normalization component by deleting a
finite nonempty set. All loops over \(F\) are finite puncture
loops; at least one additional puncture lies at infinity. In the
usual presentation of first homology, the sole relation among all
puncture loops includes that infinity loop. Therefore the finite
puncture loops alone are linearly independent over \(\mathbb Q\).

For each analytic base branch at \(p\), choose an upstairs
normalized point, choosing an unreached point for at least one
branch. Weight its small loop by the reciprocal of its positive
ramification index. Their sum \(\beta\) maps under \(\theta_*\)
to the sum of all branch loops at \(p\), which is the Thom image
of the small three-sphere about \(p\).

Equation (A3) puts \(\beta\) in \(\operatorname{im}\phi'\).
Equation (A5) gives zero coefficient at every unreached puncture.
The constructed \(\beta\) has a nonzero coefficient at one such
puncture. Independence yields the contradiction.

## 6. Boundaries and optional clarifications

No gap was found in the proposed pointwise implication. Three
clarifications would make later reuse safer:

- Cite Stacks Lemma 29.35.14 for smoothness at points of one fiber.
- Keep the typed local pair \((U\setminus L,U\setminus E)\)
  in the Thom argument, as in (A2).
- State that normalization commutes with smooth base change on the
  open smooth locus containing the entire fiber. Nothing asserts
  that \(\pi\) is smooth over a whole neighborhood in the base.

The translation assumption is not used after smoothness and the
primitive retained-curve identification are established. Keeping
it in the advertised implication is harmless, and avoids an
unnecessary strengthening of the stated downstream input.

The conductor observation in Section 7 of the pointwise note also
checks out. If \(I\) is the nonzero conductor in an equivariant
finite normalization, it is stable under the derivation. A last
nonzero derivative gives \(c\in I\cap\ker D\), \(c\ne0\).
The normalized invariant ring embeds as a submodule of
\(c^{-1}\ker D\), hence is finite when \(\ker D\) is Noetherian.
This does not identify the intermediate curve ring with that
invariant ring, and it is not needed by the cycle proof.

The criterion would fail if reducedness meant only the underlying
set, if the intermediate factorization were arbitrary, or if the
homology/product hypotheses were discarded. In particular, the
nodal escaping-branch control in the note does not have (A3), so
it does not contradict the audited statement.

## Sources

[^1]: Shulim Kaliman, [*Free C+-actions on C3 are translations*](https://www.math.miami.edu/~kaliman/library/Ka.invent.2004.c%2B.pdf), final author version, especially §§2-5. The source inputs are distinguished from the independently reconstructed support argument above.
[^2]: The Stacks Project, [Smooth morphisms, Lemma 29.35.14](https://stacks.math.columbia.edu/tag/01V9), the pointwise equivalence between smoothness and flatness plus smoothness of the fiber.
[^3]: The Stacks Project, [Lemma 37.19.2, normalization commutes with smooth base change](https://stacks.math.columbia.edu/tag/03GV).
