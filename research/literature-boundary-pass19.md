# Pass 19: statement-level prior-work boundaries

Date: 2026-09-12. This bounded audit compares the two pass-19 statements
with primary texts, not with generic cancellation surveys. It establishes
several exact overlaps. It does not establish priority, exhaust the
literature, or supply external expert review.

## 1. Statements being compared

The [relative classification note](relative-modification-classification-pass19.md)
uses a primitive LND \(D\) on \(R=\mathbb C^{[3]}\),
\(C=\ker D\), a minimal local slice \(Dr=p\), and
\((p,V)C=C\). Its proposed classification is
\[
R\simeq_C R[r/V]
\quad\Longleftrightarrow\quad
V-c\in pC\text{ for some }c\in\mathbb C^*,
\]
when the reduced plinth support is connected. The intermediate affine
criterion on \(R_V\), under \(\lambda\equiv1\pmod{\sqrt{pC_V}}\), is
\[
r\longmapsto\lambda r+b\text{ preserves }R_V
\quad\Longleftrightarrow\quad
\lambda-1,b\in pC_V.
\]
Here preservation initially means endomorphism; the proof also gives
an automorphism. This is a relative statement, not a test for abstract
polynomiality. The disconnected-support example in the note is essential.

The [additive mutation note](iterated-local-slice-bridge-pass19.md) starts
with the explicit polynomial-curve family
\(f=xz-F(y)\), \(r=xP(x,f)+yf^n\), \(xh=K(f,r)\), and replaces
\[
r_2=r+hQ(f,h),\qquad k=K(f,r_2)/h.
\]
Its target is not merely that \(\operatorname{Jac}(f,k,\cdot)\) is an LND.
It claims explicit polynomial kernels for its invariant slice extensions,
using a corrected finite curve jet and a global polynomial inverse. Its
finite-chain continuation retains explicit kernel, local-slice, and plinth
hypotheses; it is not a generation theorem for all rank-three LNDs.

## 2. Kernel-fixing automorphisms: direct overlap and a remaining refinement

### Kuroda

Kuroda's eight-page symposium report, *The automorphism group of a UFD
over the kernel of a locally nilpotent derivation*, Proposition 2.1,
already makes a kernel-fixing automorphism affine on a local slice,
\(r\mapsto ur+b\). Its multiplier character has the exponential
subgroup as kernel. Proposition 2.2 identifies allowable plinth-preserving
multipliers with units in the UFD case. Theorems 2.4 and 2.5 constrain
torsion and non-torsion multipliers; the finite-cyclic conclusion uses
additional unit hypotheses.
[Primary report, pp. 2–3](https://www.math.okayama-u.ac.jp/~hashimoto/paper/Comm-Alg/35/jsca35kurodas.pdf).

This is a direct predecessor for the affine-multiplier reduction. One
must not apply the units-plus-zero-is-a-field hypothesis to \(R_V\): its
unit group can contain nonconstant factors of \(V\). Theorem 2.4(iii)
inverts multiplier power differences to obtain a slice; its stated
conclusion is not the pass-19 full-multiplicity congruence. This audit
has not settled whether that congruence is an existing consequence in
later treatments.

### Stampfli

Stampfli's Lemma 5.1.2 applies to complex UFDs, not only polynomial
three-space. An automorphism fixing the kernel and commuting with an LND
is an exponential of a kernel multiple of the associated irreducible
LND. Its proof uses integer iterates, polynomial dependence on the
iteration parameter, and differentiation at zero.
[Author version, Lemma 5.1.2 and proof](https://arxiv.org/pdf/1406.6246).

Consequently the \(\lambda=1\) **automorphism** case on \(R_V\) is
already a direct corollary: \(\sigma=\exp(gD)\) gives
\(b=gp\in pC_V\). Full plinth multiplicity in this translation case
must not be presented as a new discovery. The project separately proves
endomorphism-to-automorphism and allows the noncommuting case
\(\lambda\ne1\) with \(\lambda\equiv1\) on the reduced support.
The iteration/coefficient-extraction strategy also needs acknowledgment
as a refinement of an existing method, not an invented principle.

**Unresolved priority question A.** Does a published localized
kernel-automorphism theorem already imply the full affine criterion,
including its endomorphism direction? If so, does the relative
\(R[r/V]\) classification follow as a short corollary? The current
proof can be correct while its mathematical content is already known.

## 3. Local-slice mutation is established machinery

Freudenburg's *Local slice constructions in \(k[X,Y,Z]\)*, Section 2,
Proposition 2 and Theorem 2, establishes the local-slice replacement and
Jacobian construction used here. The paragraph immediately following
Theorem 2 explicitly warns that reuse of the same slice reverses the
construction; continued iteration requires changing the local slice or
interchanging invariant roles. Sections 3 and 4.2 develop chains and
rank-three examples.
[Journal scan, Osaka J. Math. 34 (1997), 757–767](https://ir.library.osaka-u.ac.jp/repo/ouka/all/4752/ojm34_04_02.pdf).

Thus \(r\mapsto r+hQ\), the divided-difference formula for \(k\),
and the reversal warning are prior constructions. The relevant
comparison starts after this step: preservation of the particular
polynomial overring across its \(f^n\) and \(f^{nd}\) denominator
ideals, with an explicit inverse for the resulting slice-extension
kernel. The cited theorem does not itself state that conclusion.

Dasgupta–Gaifullin restate the local-slice construction in Theorem 2.17,
including its local-slice derivative and the kernel conclusion under
irreducibility. Their Theorem 5.7 supplies the monomial predecessor of
the project's starting family.
[Primary author text, Sections 2 and 5](https://arxiv.org/html/2306.00510v2).
This corroborates the precise inherited inputs; it is not a theorem
about all four-variable invariant slice extensions.

Freudenburg–Moser-Jauslin define a quasi-extension by
\(E|_R=t\delta\). Their Lemma 2.1 says that, over a domain containing
\(\mathbb Q\), local nilpotence of \(E\) implies that of \(\delta\).
There is no additional assumption \(E(t)=0\) in that lemma.
[Primary author text, Section 2.1](https://moser.perso.math.cnrs.fr/adjoinedroots.pdf).
This is an exact predecessor for descent of local nilpotence, not for
polynomiality of an extension kernel.

## 4. Finite congruences and explicit cylinders also have close predecessors

Moser-Jauslin–Poloni, *Isomorphisms between cylinders over Danielewski
surfaces*, Section 4 and Theorem 4.0.1, construct an extension LND on a
fiber-product cylinder and obtain a slice through finite Hermite
congruences. Their polynomial \(g\) satisfies
\(g(x,r_i+xt)\equiv\sigma_i(x)\pmod{x^n}\). This yields explicit
cylinder isomorphisms for special Danielewski surfaces, with simple-root
and principal-bundle hypotheses.
[Primary author version, Section 4](https://arxiv.org/pdf/2002.12202).

The overlap is substantive: finite congruences, a regular quotient by
a power of the base parameter, an extension LND, and an explicit slice.
The project's singular nilpotent cone and its embedded curve jet do
not automatically satisfy this theorem's geometric hypotheses.
Conversely, a different presentation could make it applicable; that
possibility has not been ruled out.

A still closer general formula is Blanc–Poloni–Van Santen,
*Complements of hypersurfaces in projective spaces*, Lemma 3.1.
Over \(S=k[x_0,\ldots,x_s]\), it treats hypersurfaces
\(x_0^ny=P(z)\) and \(x_0^ny=Q(z)\). Approximate inverse
polynomials modulo \(x_0^m\), together with two ideal-inclusion
conditions, produce explicit inverse cylinder maps. The proof checks
regularity from these conditions and computes both compositions.
[Journal article, JEP 11 (2024), pp. 740–741](https://jep.centre-mersenne.org/item/10.5802/jep.264.pdf).

This is a serious priority comparison for the pass-19 reparametrization
and denominator argument. The project must either derive its theorem
from this lemma by displaying the required global hypersurface
presentation and ideal inclusions, or explain precisely which extra
overring compatibility it proves. An isomorphism after inverting
\(f\) does not supply that missing identification.

**Unresolved priority question B.** Is the global additive-mutation
lift a specialization or finite iteration of these published cylinder
constructions? The finite-jet technique alone is not a defensible
novelty claim. A possible distinct statement would have to specify
the exact uniform family, retained plinth data, and global polynomial
inverse, then survive this comparison.

## 5. Reading record and access limits

The two project notes were read for their full hypotheses and conclusions.
The primary sections stated above were actually read, including the
Stampfli proof, Freudenburg's post-Theorem-2 paragraph, the complete
Moser-Jauslin–Poloni Section 4 construction, and the complete JEP
Lemma 3.1 and proof.

Two access qualifications matter:

- Kuroda's report URL failed on direct retrieval during this pass.
  The indexed primary PDF supplied the complete targeted propositions
  and theorems on printed pp. 2–3, not a successfully downloaded full
  report. Kuroda's later author survey was also read at Theorems
  7.5–7.7 and reference 46, which identifies the eight-page symposium
  report. It does not establish the absence of a later publication.
  [Author survey](https://www.mathsoc.jp/section/algebra/algsymp_past/algsymp16_files/ring-theory/2-kuroda.pdf).
- The quasi-extension definition and Lemma 2.1 were read from the
  indexed primary author PDF's complete Section 2.1 excerpt. Direct
  retrieval failed; no claim of reading that entire paper is made.

One additional recent primary text was checked: Shakhmatov's
Theorem 2.6 and Corollaries 2.7–2.8 identify the plinth zero locus
through action-compatible principal cylinders. They detect support,
not the full-thickening relative classification above.
[Author preprint, 2026](https://arxiv.org/html/2605.00138v1).

Status: exact inherited machinery identified; two narrow priority
questions remain. No conclusion here upgrades either working proof
to established novelty, a cancellation solution, or a publishable
result without further comparison and expert review.
