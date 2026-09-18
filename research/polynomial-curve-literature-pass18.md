# Statement audit: polynomial-curve lifts and canonical rescaling

Private bounded pass 18, with primary statements checked online. This
audit separates established construction machinery, the project's
explicit coordinate deduction, and the scope of nearby automorphism
theorems. It does not establish priority from missing search matches.

## 1. The arbitrary monic polynomial is covered by general local-slice machinery

In [the polynomial-curve note](polynomial-curve-lift-pass18.md), write
\(F(Y)\) for a monic polynomial of degree \(d\ge2\), to distinguish
it from the two-variable polynomial called \(F\) in Dasgupta--Gaifullin.
The latter is denoted \(P(x,f)\) here.

The **displayed family** in Dasgupta--Gaifullin, Theorem 5.7, uses
\(f=xz-y^m\), \(r=xP(x,f)+yf^n\), and
\(xh=r^m+f^{mn+1}\). Its hypothesis allowing an arbitrary
two-variable polynomial concerns \(P\), not replacing \(y^m\)
by an arbitrary curve polynomial.[^1]

However, their Theorem 2.17 recalls Freudenburg's general local-slice
theorem, and Corollary 5.6 gives rank three once the constructed
derivation is primitive and its chosen local slice is minimal.
These results are not restricted to the monomial presentation.[^1]
Freudenburg's original Section 2, Theorem 2, constructs the new LND
from a minimal irreducible relation modulo an invariant generator;
the discussion and kernel criterion following it do not impose
homogeneity.[^2]

Here is an explicit application, rather than an inference based only
on similar terminology. Begin with the triangular LND
\[
D_0=x\partial_y+F'(y)\partial_z,
\quad f=xz-F(y),\quad g=x,
\quad r=xP(x,f)+yf^n.
\]
It is primitive, has kernel \(\mathbb C[x,f]\), and
\(D_0r=xf^n\). The kernel assertion follows by localizing at
\(x\) and contracting; the map \(\mathbb C[f]\to R/(x)\)
sends \(f\) to the nonconstant polynomial \(-F(y)\) and is
injective. Also \(r\notin xR\).

Let \(G(R,S)=S^dF(R/S)\) and
\[
K(f,r)=G(r,f^n)+f^{nd+1}.
\]
Modulo \(x\), the relations are \(f=-F(y)\), \(r=yf^n\),
so \(K=0\). After inverting \(f\), put \(T=r/f^n\).
The relation becomes \(F(T)+f=0\), irreducible over
\(\mathbb C(f)\): the field extension
\(\mathbb C(y)/\mathbb C(F(y))\) has degree \(d\).
Since \(K\) is monic in \(r\), it is irreducible in
\(\mathbb C[f,r]\) and is the minimal relation required by the
local-slice construction. Thus that existing theorem gives
\(-\operatorname{Jac}(f,K/x,\cdot)\) as an LND, up to its
harmless sign convention.

The project's direct primitivity and minimal-slice calculations
then verify the hypotheses of the existing rank-three corollary.
Consequently **existence through local-slice construction and the
rank criterion must be credited to the prior general machinery**.
The new note provides an explicit application and independent algebraic
checks, not a new general local-slice principle.

The arbitrary \(F\) does enlarge the displayed formula in a meaningful
fixed-invariant sense. For example, \(xz-F(y)=0\) is smooth when
\(F\) has only simple roots, while \(xz-y^d=0\) is singular for
\(d\ge2\). This excludes identifying these two presentations by
an ambient automorphism carrying the specified \(f\) to the specified
monomial invariant. It does **not** classify the derivations up to
conjugacy when their invariant generators may change.

The four-variable claim is separate: neither cited local-slice statement
asserts that every slice extension \(A\delta+B\partial_t\) of these
rank-three bases has polynomial coordinates. The project's finite-jet
construction and inverse are the evidence for that claim. Their
mathematical priority remains unestablished.

Daigle's *Homogeneous locally nilpotent derivations of k[X,Y,Z]*,
Section 4.1, explicitly develops a grading-compatible version and
credits Freudenburg. Its stated local-slice graph results require a
positive grading. The remark after 4.1 also points to broader
characteristic-zero local-slice constructions. This is additional
evidence that local-slice methodology is established, not a theorem
about the present invariant extensions.[^3]

## 2. The rescaling question is not a centralizer question

The [scaling obstruction](radical-modification-attack-pass18.md)
concerns an automorphism of \(C_{pV}[r]\) fixing \(C_{pV}\),
with \(r\mapsto\lambda r\). Its direct conjugation formula is
\[
\sigma_\lambda D\sigma_\lambda^{-1}=\lambda^{-1}D.
\]
Unless \(\lambda=1\), this does not commute with \(D\).
For nonconstant \(\lambda\), it does not even normalize the fixed
one-parameter subgroup with constant time parameters. It preserves
the invariant kernel and the invariant-coefficient rank-one module
of derivations instead. Conflating those objects would make a
centralizer theorem appear stronger than its statement.

Stampfli's Proposition 5.1.1 and Lemma 5.1.2 identify the
kernel-fixing part **inside the centralizer** as exponentials of
invariant replicas of the primitive derivation. The lemma applies
to a UFD, not only polynomial three-space. Its proof extends an
integer translation to all scalar parameters by a density argument
and differentiates at zero.[^4] This is a precise predecessor for
the iterate-and-infinitesimal method. The project's multiplicative
rescaling argument needs the additional finite valuation extraction
to distinguish \(p\) from its radical; it is not obtained by
dropping the commutation assumption in that lemma.

The 2025 paper of El Kahoui, Essamaoui, and Ouali studies centralizers
on \(S^{[2]}\) over a domain \(S\), with stronger descriptions for
UFD bases and principal plinth ideals. The publisher's abstract and
introduction were accessible, but not a reliably rendered complete
theorem text. Its fixed two-variable presentation and commutation
conditions do not directly match the present localized rank-three
kernel-fixing rescaling problem. No uninspected theorem from it is
being used.[^5]

## 3. A closer predecessor: Kuroda's kernel-fixing automorphism announcement

Kuroda's symposium report studies \(\operatorname{Aut}(A/A^\delta)\)
for a UFD and an LND. Proposition 2.1 supplies the affine action on
a local slice and a multiplicative character; Proposition 2.2 places
that character in the unit group. Theorem 2.4(iii) says that a
nontorsion multiplier gives a relative polynomial extension after
inverting all its nontrivial power differences. Theorem 3.5 treats
finite-order multipliers for a specified triangular derivation by
an exact polynomial congruence.[^6]

This is the correct nearby group-theoretic framework. It also shows
why treating every kernel-fixing automorphism as an exponential of
an LND is false. Nevertheless, the stated general localization
criterion inverts elements such as \(\lambda^i-1\); it does not
record their individual valuations along plinth components. The
project's condition
\[
\lambda\equiv1\pmod{\operatorname{rad}(p)}
\quad\Longrightarrow\quad
\bigl(\sigma_\lambda\text{ extends over }R_V
\iff\lambda\equiv1\pmod p\bigr)
\]
is a full-multiplicity extension criterion for one specified scaling.
It is not a theorem quoted from that report.

The source itself labels its results an announcement and says a
detailed version is intended. The symposium program dates the talk
to December 2013.[^7] This audit has not verified a subsequently
published complete proof of those exact statements. The report is
therefore recorded as a primary announced predecessor, not silently
upgraded to a fully inspected journal proof. Conversely, its existence
prevents presenting the general kernel-fixing multiplier framework as
new project machinery.

## 4. Audit conclusions and proof status

The base family is an application of established local-slice theory,
beyond the displayed monomial subfamily. The invariant-extension
coordinate theorem is a distinct explicit deduction. The scaling
obstruction belongs near existing kernel-fixing automorphism results;
its iterate differentiation method has a verified centralizer analogue.
No exact prior full-multiplicity criterion has been used to replace the
project proof, and no absence-based novelty conclusion follows.

A quick independent algebra audit of Sections 1–3 of
[the polynomial-curve note](polynomial-curve-lift-pass18.md) found
no gap in its inverse chart, degree basis, invariant contraction,
primitivity calculation, or minimal-slice argument. This is a
cross-check, not external expert review. The scaling proof has a
separate finite reconstruction by the main investigation that removes
the need for completion and logarithms; this literature note does not
modify either proof or any claim registry.

## Sources

[^1]: N. Dasgupta and S. Gaifullin, *On locally nilpotent derivations of polynomial algebra in three variables*, *Sbornik: Mathematics* **216** (2025), 456–484. [Primary arXiv v2, Theorem 2.17, Corollary 5.6, and the definition preceding Theorem 5.7](https://arxiv.org/html/2306.00510v2); [published record](https://www.mathnet.ru/eng/sm10094). The arXiv displays contain known typographical errors already recorded in pass 17; the present calculation does not copy the erroneous displayed derivative of y.

[^2]: G. Freudenburg, *Local slice constructions in k[X,Y,Z]*, *Osaka Journal of Mathematics* **34** (1997), 757–767. [Primary journal scan, Section 2, Theorem 2 and the following kernel criterion](https://ir.library.osaka-u.ac.jp/repo/ouka/all/4752/ojm34_04_02.pdf). Some OCR notation is damaged; its general statement was cross-read with the exact recall in source 1.

[^3]: D. Daigle, *Homogeneous locally nilpotent derivations of k[X,Y,Z]*, [author manuscript, Section 4.1 and its following remark](https://aix3.uottawa.ca/~ddaigle/articles/part1.pdf). Only the grading hypotheses and local-slice scope are used here.

[^4]: I. Stampfli, *Automorphisms of C3 Commuting with a C+-Action*, *International Mathematics Research Notices* **2015**(19), 9832–9856, [DOI 10.1093/imrn/rnu232](https://doi.org/10.1093/imrn/rnu232). Directly read [arXiv:1406.6246v2, Proposition 5.1.1 and Lemma 5.1.2 including its proof](https://arxiv.org/pdf/1406.6246).

[^5]: M. El Kahoui, N. Essamaoui, M. Ouali, *The centralizer of a locally nilpotent R-derivation of the polynomial R-algebra in two variables*, *Journal of Pure and Applied Algebra* **229**(1) (2025), 107828. [Publisher abstract and introduction](https://www.sciencedirect.com/science/article/abs/pii/S0022404924002251). Access limitation is stated in the text.

[^6]: S. Kuroda, [*The automorphism group of a UFD over the kernel of a locally nilpotent derivation*](https://www.math.okayama-u.ac.jp/~hashimoto/paper/Comm-Alg/35/jsca35kurodas.pdf), eight-page primary symposium announcement, Propositions 2.1–2.2 and Theorems 2.4 and 3.5. The entire report was read; it is not represented here as a full journal proof.

[^7]: [35th Japan Symposium on Commutative Algebra, December 2013 program](https://www.math.okayama-u.ac.jp/~hashimoto/paper/Comm-Alg/35/program_e_CommAlg2013.pdf), for the dated Kuroda talk. This dates the announcement context, not a later publication.
