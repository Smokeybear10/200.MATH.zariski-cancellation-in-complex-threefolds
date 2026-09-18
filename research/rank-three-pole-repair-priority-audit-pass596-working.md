# Priority audit for the rank-three sliced-extension pole repair

The coordinate construction in pass 594 uses an established rank-three
base and classical localization and invertibility principles. A definite
subfamily of the proposed pass-595 extension was also recognized in this
project's old pass 22. The bounded primary comparison below does not
identify a published theorem that supplies the specific whole-family
pole correction automatically. It does not establish its novelty or
absence from the literature.

This note records statement-level matches and missing premises. It is
not another proof of the full proposed family, a review of unfinished
pass 595, or a general cancellation result. The concrete
[pass-594 proof](rank-three-sliced-extension-pole-repair-recognition-pass594-working.md)
was held at SHA256
`1f842ca6cd427576c34bbe21c2453b04b2c29bfd790daa1489712c4c2cf33cb3`.
No unfinished pass-595 source was read for this audit.

## 1. Exact comparison target and published base

Work in \(B=\mathbb C[x,y,z,t]\). The communicated family is
\[
\begin{gathered}
f=xz-y^m,\qquad r=xF(x,f)+yf^n,\qquad
g=\frac{f^{mn+1}+r^m}{x},\\
H=\operatorname{Jac}(f,g,\cdot),\qquad
m\ge2,\quad n\ge2,\quad F(x,0)\notin\mathbb C.
\end{gathered}
\tag{1}
\]
The expression for \(g\) is polynomial. Indeed, modulo \(x\),
\(f=-y^m\) and \(r=yf^n\), so \(f^{mn+1}+r^m=0\).
Dasgupta--Gaifullin's Theorem 5.7 and its preceding construction
contain precisely this base, with their new invariant named \(h\)
instead of \(g\). Their proof supplies the rank-three LND, its
irreducibility, the minimal local slice \(r\), and
\[
Hf=Hg=0,\qquad Hr=-gf^n,\qquad
Hx=-m r^{m-1}f^n.
\tag{2}
\]
Their Theorem 2.17 recalls the underlying local-slice construction.
These are published base results, not new ingredients of the repair.[^DG]

Set
\[
b=-gf^{n-2},\qquad E=H+(1+fbr)\partial_t,\qquad
v=ft-r^2/2,
\tag{3}
\]
and take the supplied slice
\[
u=t-brv+\frac{fb^2}{2}v^2.
\tag{4}
\]
Here \(Hb=0\), \(Hr=f^2b\), and \(E(v)=f\). Direct differentiation
gives \(Eu=1\). The recognition target is stronger than this slice
identity: it is that \(u\) can be completed to an actual polynomial
coordinate system of \(B\). Pass 594 proves this for
\((m,n,F)=(2,2,x^4)\). The communicated pass-595 claim covers (1).
The DG theorem concerns the three-variable base and does not itself
state this four-variable coordinate conclusion.

## 2. Definite earlier internal coverage, with signs retained

The whole old
[pass-22 theorem and proof](radical-noninvariant-pass22.md) were read
through EOF for this comparison. Its convention, for every \(n\ge1\), is
\[
\begin{gathered}
f=xz-y^2,\qquad r=x^3+yf^n,\qquad
h=zf^{2n}+2x^2yf^n+x^5,\\
D=-\operatorname{Jac}(f,h,\cdot),\qquad
E_{22}=D+(1+q_{22}r)\partial_t.
\end{gathered}
\tag{5}
\]
It states that \(E_{22}\) has a slice exactly when
\(f\mid q_{22}\in\mathbb C[f,h]\), and that every positive case has
kernel \(\mathbb C^{[3]}\) and a full polynomial translation frame.
Its positive proof already uses a finite correction and a
minimal-denominator argument, followed by physical-coordinate lifting.

For (1) with \(m=2\) and \(F(x,f)=x^2\), the old \(h\) is the new \(g\).
Thus \(D=-H\), and choose
\[
q_{22}=fb=-gf^{n-1}.
\tag{6}
\]
Let \(S\in\operatorname{Aut}_{\mathbb C}B\) fix \(x,y,z\) and send
\(t\mapsto-t\). As derivations,
\[
-S E S^{-1}=D+(1-gf^{n-1}r)\partial_t=E_{22}.
\tag{7}
\]
The coefficient in (6) is divisible by \(f\) for every \(n\ge2\).
Consequently pass 22 already recognizes this entire subfamily.
Conjugation transports its kernel, and multiplying a derivation by
\(-1\) does not change its kernel.

This also recognizes the particular supplied slice (4), not merely
some other slice: if \(A=\ker E\cong\mathbb C^{[3]}\), then \(Eu=1\)
gives \(B=A[u]\) by the slice theorem. Choosing three polynomial
generators of \(A\) completes this \(u\) to a coordinate system.
There is no assertion that the old displayed slice equals (4).

The old pass-23 theorem further classifies coefficients in
\(\mathbb C[f,h,r]\) for the same canonical base. The general base
in (1) also appears in the older pass-18 base discussion, but its
invariant-extension result is not a direct treatment of the
noninvariant coefficient in (3). These observations do not constitute
an exhaustive audit of every old source. In particular, neither all
of pass 595 nor its method should be labeled entirely new internally.
The concrete \(F=x^4\) is not the \(F=x^2\) specialization just matched.

The checked old pass-22 source has SHA256
`2dd1e002c0e773cab2b06df785d126b6409fd25d8953131c1d9a0af8a8556285`.
Its [separate priority audit](priority-comparison-pass22.md), also read
in full, retains unresolved external priority rather than asserting it.

## 3. Classical final-step recognition and the exact Jacobian licenses

Bass--Connell--Wright, Chapter I, Theorem (2.1), implication (b) to
(a), states that a birational polynomial map with invertible Jacobian
is a polynomial automorphism. This is the birational case credited
there to Keller. The statement and its relevant proof were read in
the author-uploaded primary text.[^BCW]

This theorem applies directly after the specific repair has made all
four coordinate images polynomial. No coefficient-ring presentation
with \(f\) as an ambient coordinate is needed. Here are the licenses
for the Jacobian premise, independently of the quotient-injectivity
proof used in pass 594.

On \(B_f\), extend \(H\) by \(H(t)=0\), and put
\[
L=H/f+br\partial_t.
\tag{8}
\]
It is locally nilpotent: its restriction to
\(\mathbb C[x,y,z]_f\) is the LND \(H/f\), and its value on \(t\)
belongs to that ring and has a finite derivative sequence. Moreover,
\[
Lr=fb,\qquad Lt=br,\qquad Lv=0.
\tag{9}
\]
Thus \(-vL\) is an invariant replica and
\(\Phi=\exp(-vL)\in\operatorname{Aut}(B_f)\). Its \(t\)-image is
exactly (4), since \(L^2t=fb^2\) and \(L^3t=0\).

Use divergence relative to the original ordered coordinates
\((x,y,z,t)\), extended by the quotient rule to \(B_f\).
A Jacobian derivation has divergence zero; \(Hf=0\), and \(br\)
is independent of \(t\). Therefore
\[
\operatorname{div}L=0,\qquad
\operatorname{div}(-vL)=-v\operatorname{div}L-Lv=0.
\tag{10}
\]
The correction has the form
\[
\delta_0=x\partial_y+m y^{m-1}\partial_z,\qquad
\Gamma=\exp\left(-\frac{p(x)}f\delta_0\right),
\quad p(x)\in\mathbb C[x].
\tag{11}
\]
The coefficient \(p(x)/f\) is killed by \(\delta_0\), which also
kills \(t\); its divergence is zero. Hence the derivation in (11)
is a divergence-zero LND of \(B_f\). In pass 594,
\(p(x)=9x^{18}/2\). For the general-family comparison, the statement
here applies to any correction of form (11); it does not replace
the proof that a particular \(p\) cancels all the poles.

For completeness, if \(T\) is either divergence-zero LND above, its
finite parameter flow \(\sigma_s=\exp(sT)\) satisfies the formal
Jacobian differential identity
\[
\frac{d}{ds}\det J(\sigma_s)
=\sigma_s(\operatorname{div}T)\det J(\sigma_s)=0.
\tag{12}
\]
The determinant at \(s=0\) is one. The identity holds in the
localization with the independent parameter \(s\), so both factors
have Jacobian one. Composition gives
\[
\Psi=\Phi\circ\Gamma\in\operatorname{Aut}(B_f),
\qquad \det J(\Psi)=1.
\tag{13}
\]
Once the repair proves \(\Psi(B)\subset B\), it is a polynomial
map and remains birational because its localized inverse is known.
BCW then makes it an automorphism of \(B\). Its image of \(t\) is
\(u\), since \(\Gamma(t)=t\).

This is a positive theorem match for the final invertibility step,
not a published construction of the required regular images. In
particular, one polynomial component of a localized automorphism
is not enough to invoke BCW. The unrepaired map in pass 593 has
a genuine pole in its \(y\)-image. Pass 594's alternative proof,
using injectivity modulo \(f\) to clear inverse denominators, remains
valid and self-contained. No new general invertibility principle is
claimed here.

## 4. Nearby primary coordinate theorems and their missing premises

Lewis's *Strongly residual coordinates over A[x]* explicitly describes
the classical technique of composing localized elementary maps until
their poles cancel. Its numbered Theorems 3 and 4 require elementary
factorizations with specified scaled-subalgebra and congruence
conditions over \(R=A[x]\), \(S=A[x,x^{-1}]\). Their more technical
versions are labeled **Main Theorems 1 and 2** in Section 3.2; these
use "Main" as part of the theorem name. Numbered Theorem 1 in the
preliminary section separately treats two relative variables. Corollary 5
gives one-stability of the specified Vénéreau-type polynomials.[^L13]

The method deserves prior credit. A direct application to (1)--(4)
would still need an actual polynomial-ring presentation and the
stated factorization conditions. In the natural attempted
presentation over \(\mathbb C[f]\), the special fiber
\[
B/(f)=\mathbb C[x,y,z,t]/(xz-y^m)
\tag{14}
\]
is singular along \(x=y=z=0\) for \(m\ge2\). It is not a
three-variable polynomial ring, so this does not make \(B\) a
polynomial three-ring over \(\mathbb C[f]\). The displayed slice
has not been identified here with Lewis's Vénéreau-type formula.
No assertion of inequivalence under every possible automorphism is
being made.

Lewis's earlier *Vénéreau-type polynomials as potential
counterexamples*, Theorem 3, is a coefficient-ring overring principle:
for reduced \(A\), a non-zero-divisor \(x\in A\), and a polynomial
map over \(A\) with unit Jacobian, invertibility over \(A_x\) implies
invertibility over \(A\). Its Theorems 4 and 13 construct coordinates
under additional explicit polynomial-presentation conditions.[^L10]
The theorem cannot literally be applied by moving the noncoordinate
\(f\) into a fictitious coefficient ring. BCW in Section 3 avoids
that problem once all actual coordinate images are polynomial.

Freudenburg's Proposition 7.1 in *Actions of SL2(k) on Affine
k-Domains and Fundamental Pairs* concerns extensions whose added
coefficient lies in the old kernel, with image-ideal compatibility.
Theorem 7.6 further assumes a fundamental pair and an invariant
coefficient of weight zero. Here, instead,
\[
H(1+fbr)=f^3b^2\ne0.
\tag{15}
\]
Thus those statements do not apply directly to the supplied
extension over its original three-ring. This is a missing premise,
not a theorem forbidding a different presentation.[^F]

Kaliman--Zaidenberg, Proposition 2.1, lifts maps between affine
modifications when the denominator and full center-ideal conditions
hold; its surjectivity statement requires the corresponding equalities.
It supplies established lifting machinery, not automatic preservation
of a center by an arbitrary localized map. The family-specific
regularity or center calculations cannot be omitted.[^KZ]

## 5. Search limits and disposition

The bounded comparison examined the precise DG family and local-slice
construction; Lewis's stated coordinate, overring, and factorization
results; Freudenburg's extension statements; KZ's lifting proposition;
and BCW's birational criterion. Relevant statements and their displayed
proofs were read. This is not a recursive recertification of every
lemma those papers cite, or an exhaustive citation-tree, thesis,
MathSciNet, or zbMATH search.

The AMS PDF endpoint for BCW returned HTTP 403. The public full text
uploaded by coauthor David Wright was read instead; no access control
was bypassed. The old pass-22 priority note records an unresolved
comparison with the full example section of Freudenburg's 2009
*Derivations of R[X,Y,Z] with a slice*. This audit does not silently
claim to have obtained or settled that missing comparison.

Accordingly, the retained conclusions are: definite published credit
for the base and general machinery, definite internal overlap, and
an explicit bounded non-match for the particular theorem statements
checked. The specific coordinate proof can be correct without its
priority having been resolved. Neither unsuccessful searches nor this
list of missing premises proves that the result is absent from all
literature. Novelty remains **UNKNOWN**.

No saved checker was executed, imported, or compiled. Only this new
audit file was written; no prior source or canonical record was changed,
and no git commands were performed. There was no outreach, submission,
or claim of human or formal verification.

## Primary sources

[^DG]: N. Dasgupta and S. A. Gaifullin, [*On locally nilpotent derivations of polynomial algebra in three variables*](https://www.mathnet.ru/php/archive.phtml?jrnid=sm&option_lang=eng&paperid=10094&wshow=paper), *Sbornik: Mathematics* 216(4) (2025), 456--484, Theorems 2.17 and 5.7 with the preceding construction and proof. [Author version](https://arxiv.org/html/2306.00510v2).

[^BCW]: H. Bass, E. H. Connell, and D. Wright, [*The Jacobian conjecture: reduction of degree and formal expansion of the inverse*](https://www.researchgate.net/publication/38390367_The_Jacobian_conjecture_Reduction_of_degree_and_formal_expansion_of_the_inverse), *Bulletin of the American Mathematical Society* 7(2) (1982), 287--330, Chapter I, Theorem (2.1), particularly (b) implies (a), pages 294--296. The link supplies the coauthor-uploaded full primary text. [Publisher DOI](https://doi.org/10.1090/S0273-0979-1982-15032-7).

[^L13]: D. Lewis, [*Strongly residual coordinates over A[x]*](https://arxiv.org/pdf/1304.1765), arXiv:1304.1765v2, introduction, Theorems 1, 3 and 4, Corollary 5, and Main Theorems 1 and 2 in Section 3.2. The arXiv header identifies the version as 14 May 2013; this audit does not use a later PDF typesetting date to claim a later theorem.

[^L10]: D. Lewis, [*Vénéreau-type polynomials as potential counterexamples*](https://arxiv.org/pdf/1007.2230), arXiv:1007.2230v3, Theorems 3, 4 and 13. Theorem 3 explicitly credits the overring principle.

[^F]: G. Freudenburg, [*Actions of SL2(k) on Affine k-Domains and Fundamental Pairs*](https://arxiv.org/pdf/2108.12021), Section 7.1, Proposition 7.1, and Section 7.3, Theorem 7.6.

[^KZ]: S. Kaliman and M. Zaidenberg, [*Affine modifications and affine hypersurfaces with a very transitive automorphism group*](https://arxiv.org/pdf/math/9801076), Section 2, Proposition 2.1 and its proof. Published in *Transformation Groups* 4 (1999), 53--95.
