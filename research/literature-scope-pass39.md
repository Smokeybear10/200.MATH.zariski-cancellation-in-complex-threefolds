# Quasi-translations, frame height, and the actual remaining scope

## 1. The previous closure must be retained

The whole adjoint-height-one condition is **already closed more strongly**
in [the height-eight algebra proof](height-eight-algebra-pass.md):
for an LND \(E\) on \(\mathbb C^{[4]}\),
\[
[E,[E,\partial_{x_i}]]=0\quad(1\le i\le4)
\]
forces an ambient polynomial coordinate in \(\ker E\), even without a
slice. With a slice, the kernel is polynomial. I reread that complete
proof, including its highest-iterate cases and cone-preserving
homogenization. The [pass-38 argument](actual-frame-pass38.md) is a
weaker alternate argument under the same whole-frame assumption, not
new progress in the recognition threshold. Its direct construction
of commuting restrictions does not undo the earlier stronger closure.

The [completed mixed proof, Section 10](../deep-pass-13.md), already
gives \(H\le9\Rightarrow\ker E\simeq\mathbb C^{[3]}\) for an actual
sliced cylinder. Here \(q_i\) is the filtration shift of the coordinate
partial and \(H=\sum_i(q_i+1)\). There is no established universal
upper bound on the minimum height over genuine coordinate frames.

After the previously closed negative, double-zero, and zero/one cases,
the first height-ten profiles still requiring treatment are
\[
(0,2,2,2),\qquad(1,1,1,3),\qquad(1,1,2,2).
\]
These are filtration shifts, not ordinary degrees of polynomial
coefficients. Neither a new search over the height-eight cases nor
another proof of their low-rank branch advances this remaining gate.

## 2. Three different assertions about sliced quasi-translations

Write \(E=v\cdot\partial\) and \(J=\operatorname{Jac}v\). A displayed
quasi-translation is characterized by
\[
Jv=0,\qquad v(x+tv(x))=v(x),
\]
so its flow is \(x+tv(x)\). This is also called a nice derivation in
the displayed coordinates. Niceness is not the whole-frame condition:
differentiating \(Jv=0\) gives \(E(J)=-J^2\), whereas the whole-frame
condition gives \(E(J)=J^2\). Their intersection therefore has
\(J^2=0\), in characteristic zero.

The targeted primary audit does not supply a theorem that **every**
nonhomogeneous sliced quasi-translation of \(\mathbb A^4\) is
polynomially conjugate to a translation. That remains an unproved
subproblem in this project. This statement describes the boundary of
the sources actually checked; it is not an exhaustive assertion about
every publication or a novelty inference from search results.

By contrast, the assertion that all such actions have a nonzero
**linear invariant in the displayed frame is false**. The known
control, already recorded in [nice-route.md](nice-route.md), is
\[
a=xz-y^2+w,\qquad
v=(1,a,a^2,-a^2x+2ay-z).
\tag{1}
\]
It is de Bondt's Example 1.3(b), specialized at its fixed fifth
coordinate equal to one.[^five] One has \(E(x)=1\) and \(E(a)=0\).
Moreover
\[
(x,a,Y,Z)=(x,a,y-xa,z-xa^2)
\]
are actual polynomial coordinates. Their inverse is
\[
y=Y+xa,\quad z=Z+xa^2,\quad
w=a-xZ+Y^2+2xaY.
\]
Thus this action is a translation, although no nonzero constant row
annihilates \(v\). To check the latter directly, use the independent
coordinates \((x,a,y,z)\): the coefficient of \(z\) in a constant
linear relation first kills the fourth coefficient, and the remaining
relation among \(1,a,a^2\) is zero only trivially.

The exact matrix controls are
\[
Jv=0,\quad\operatorname{rank}J=2,\quad
\operatorname{rank}[v\mid J]=3,\quad J^2\ne0,\quad J^3=0.
\tag{2}
\]
These identities were recalculated over SymPy with exact arithmetic.
This is a reuse of an established control, not a new family or new
test-suite count. It cannot contradict either whole-frame theorem,
because its displayed frame fails that condition.

## 3. What the primary classifications actually say

De Bondt's *Quasi-translations and singular Hessians* gives the
nonhomogeneous Jacobian-rank-one description in Theorem 5.5, and
classifies all quasi-translations in dimension at most three and
homogeneous ones in dimension at most four through Corollaries
5.6, 5.8, and 5.9. Its Section 6 explicitly leaves general
nonhomogeneous dimension four outside that classification. The
homogeneous four-variable conclusion must not be applied after
introducing a fifth variable. I directly read these statements, the
rank-one proof, the proof of Corollary 5.6, and the surrounding
classification and question sections.[^hess]

Dasgupta and Gupta's Theorem 3.6 is an irreducible nice-derivation
theorem for \(R[X,Y,Z]\) over a PID containing \(\mathbb Q\).
Corollary 3.8 assumes an actual common coordinate system with
\(DX_1=0\) and \(D^2X_i=0\) for \(i=2,3,4\), and concludes a
polynomial kernel. I directly read the complete Theorem 3.6 proof
and Corollary 3.8. The theorem does not produce the initially fixed
coordinate for an arbitrary four-variable nice derivation.[^nice]

If a sliced action fixes any actual ambient coordinate, the
fixed-coordinate regular-kernel theorem already closes it. This
recognition gate and its exact hypotheses are recorded in
[the pass-38 literature note](literature-scope-pass38.md). No new
invariant-coordinate existence conclusion is supplied here.

## 4. The fifth zero component is not a second invariant

For \(d\ge\max\{1,\deg v\}\), de Bondt's homogenization produces
\[
\widetilde v(x,z)=\bigl(z^dv(x/z),0\bigr).
\]
With \(u=x/z\), its complete Jacobian after inverting \(z\) is
\[
z^{d-1}\begin{pmatrix}J(u)&d v(u)-J(u)u\\0&0\end{pmatrix},
\]
and consequently its rank is \(\operatorname{rank}[J\mid v]\).
This is the same explicit column calculation as pass 38.

A theorem promising one linear invariant in dimension five may
produce only the already invariant \(z\). Example (1) has augmented
rank three and no old linear invariant, so its homogenization has
exactly one independent linear invariant. This is an explicit
failure control for inferring a second invariant from the zero
component or from niceness and a slice alone.

The rank-at-most-two theorem is different: Theorem 3.6(i),(iii) in
de Bondt's five-dimensional paper supplies at least two linear
invariants, without the gcd-one hypothesis of part (ii). Its exact
positive-degree homogeneous assumptions were directly checked.
That is valid input in the old height-eight proof and pass 38,
but does not apply to the rank-three homogenization in (2).[^five]

The ordinary square-zero identity must also be distinguished from
\[
J(x)J(y)=0\quad\text{with independent variable tuples }x,y.
\tag{3}
\]
De Bondt's strong-nilpotency Theorem 4.1 gives a linear block form
for a quasi-translation under (3). I read the complete theorem
and proof. Substitution \(y=x\) loses information; it is not a
proof of the converse. The paper's four-dimensional square-zero
matrix control has a coefficient map that is **not** a
quasi-translation, as the old height-eight note already verifies.
It must not be promoted into a sliced counterexample.[^strong]

There is no need for this stronger matrix condition in the
whole-height-one nice branch. In dimension four, \(J^2=0\) and
\(Jv=0\) already imply augmented rank at most two: at rank two,
\(\ker J=\operatorname{im}J\); at lower rank, adjoining \(v\)
increases the rank by at most one. This merely recovers the
already closed conical/homogenized branch.

## 5. Coordinate-preserving degree reduction remains a separate gate

De Bondt's Proposition 2.4 gives an exact criterion for a polynomial
conjugation to preserve quasi-translation form. If \(F\) is an
automorphism with inverse \(G\), then
\(G\circ(x+v)\circ F\) is a quasi-translation precisely when
each \(G_i(x+tv)\) has degree at most one in \(t\). I read the
complete proof. This checks an already supplied coordinate change;
it does not construct a degree-lowering one.[^five]

Kuroda's weighted reduction Theorem 2.1 assumes **three variables
and a tame automorphism**. Its conclusion allows either an
elementary or a Shestakov–Umirbaev reduction. I read the full
statement, definitions, introductory scope, and the displayed
Nagata application, not its entire long proof. Neither the
dimension nor the tameness hypothesis can be dropped to obtain
a reduction algorithm for arbitrary four-variable frames. Nor
does reduction of ordinary coordinate degree automatically
decrease an \(E\)-filtration height.[^reduction]

Accordingly the concrete next obligation is a proved operation on
an actual height-ten frame, with a polynomial inverse and an
explicitly decreasing invariant, or a direct proof covering one
of its three surviving profiles. Merely choosing a degree-minimal
frame supplies none of those steps.

## Source inventory and verification boundary

This audit reread the established nice-route and height-eight
arguments before distinguishing them from the current pass. The
primary searches covered nice derivations, sliced
quasi-translations, independent-point strong nilpotence,
double commutators, and polynomial degree reduction. Nearby
recent image-ideal results did not supply an unrestricted
four-variable recognition theorem; no inference of novelty is
made from that bounded search.

There is no new universal theorem, proof-assistant verification,
expert review, or new unittest count in this literature note.
Its main correction is preservation of the stronger earlier
closure and the exact height-ten boundary.

[^five]: Michiel de Bondt, [*Homogeneous quasi-translations in dimension 5*](https://arxiv.org/pdf/1501.04845v3), Example 1.3(b), PDF p. 5; Propositions 2.4–2.5, PDF pp. 8–9; Theorem 3.6(i),(iii), PDF p. 13. [Published version](https://doi.org/10.1007/s13366-017-0358-2). The complete statements and relevant proofs were directly read; the theorem explicitly credits Gordan and Nöther.

[^hess]: Michiel de Bondt, [*Quasi-translations and singular Hessians*](https://arxiv.org/pdf/1501.05168), Theorem 5.5, Corollaries 5.6, 5.8–5.9, and Section 6, PDF pp. 19–23. [Published DOI](https://doi.org/10.4064/cm6915-3-2017), *Colloquium Mathematicum* 152 (2018), 175–198. The historical unclassified statement is not advertised as an exhaustive September 2026 status certification.

[^nice]: Nikhilesh Dasgupta and Neena Gupta, [*Nice derivations over principal ideal domains*](https://arxiv.org/pdf/1701.03635), Theorem 3.6 and Corollary 3.8, PDF pp. 6–8. [Published DOI](https://doi.org/10.1016/j.jpaa.2018.02.025), *Journal of Pure and Applied Algebra* 222 (2018), 4161–4172.

[^strong]: Michiel de Bondt, [*The strong nilpotency index of a matrix*](https://arxiv.org/pdf/1203.6615v3), Section 2 after Proposition 2.3, PDF p. 7, and Theorem 4.1 with complete proof, PDF pp. 11–12. [Published DOI](https://doi.org/10.1080/03081087.2013.784282), *Linear and Multilinear Algebra* 62 (2014), 486–497.

[^reduction]: Shigeru Kuroda, [*Shestakov–Umirbaev reductions and Nagata's conjecture on a polynomial automorphism*](https://arxiv.org/pdf/0801.0117v2), Section 1 and Theorem 2.1 with its scope definitions and immediate application, PDF pp. 1–7. [Published version](https://doi.org/10.2748/tmj/1270041028), *Tohoku Mathematical Journal* 62 (2010), 75–115. The full proof of this external theorem was not independently reconstructed in this bounded audit.
