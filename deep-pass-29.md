# Finite Lie closure, exact horizontal selection, and a global branch obstruction

Private research checkpoint, September 13, 2026.

The working target remains
\[
 X\times_{\mathbb C}\mathbb A^1\simeq\mathbb A^4
 \quad\Longrightarrow\quad X\simeq\mathbb A^3.
 \tag{1}
\]
Professor Luo has not confirmed this correction of the original dimension
or the choice of \(\mathbb C\). The unrestricted implication (1) is not solved.

## 1. What changed

The finite-symmetry criterion is stronger than in pass 28: solvability
is unnecessary. Finite-dimensional Lie closure with all partials of
an actual ambient coordinate frame suffices to triangularize an LND.
In dimension four, a genuine slice then gives a polynomial kernel.
The bridge is a published theorem on the unipotent radical of a
transitive algebraic group, not an assumption that the entire group
is unipotent.[^1]

The canonical nonunit-plinth example now has an all-parameter horizontal
selection criterion within a specified family. Its primitive highest
coefficient is sliced exactly when a particular coefficient is independent
of the second auxiliary invariant. Equal relative degrees can give
opposite outcomes, and a decrease in degree can destroy the slice property.

The actual conductor surface now has a global obstruction beyond the
complete fiber tests: no generating triple can contain any invariant of
its specified action. This includes the functions \(d\) and \(d(u^2-1)\)
that passed every closed-fiber planarity test. A hypothetical presentation
forces at least four branches in a plane base curve, incompatible with
the surface's quadratic double crossings.

The complete arguments and separate AI reconstructions are linked below.
None proves the missing universal existence step in (1), establishes
novelty, supplies human expert review, or formally verifies the source
theorems.

## 2. Finite-dimensional closure really is enough

Let \(B=\mathbb C[x_1,\ldots,x_n]\) and let \(\delta\) be an LND.
In this genuine coordinate frame form

\[
 \mathfrak g=\operatorname{Lie}_{\mathbb C}
 \langle\delta,\partial_{x_1},\ldots,\partial_{x_n}\rangle.
 \tag{2}
\]

**Recognition statement.** If \(\dim_{\mathbb C}\mathfrak g<\infty\),
then \(\delta\) is triangular in some polynomial coordinate system.

The proof is in [the radical-transitivity note](research/levi-bridge-pass29.md).
Finite dimension and the known LND generators integrate the actual
generated additive subgroups to an affine algebraic group \(G\).
Because it contains the full coordinate translation group, it acts
transitively, not merely with an open orbit.[^2]

The unipotent radical \(U=R_u(G)\) is itself transitive by
Bruce--du Plessis--Wall's Theorem 3.6.[^1] This does not imply that
\(\delta\) belongs to \(\operatorname{Lie}(U)\). To retain its subgroup
\(H=\exp(\mathbb C\delta)\), set

\[
 \pi:G\longrightarrow G/U,\qquad
 K=\pi^{-1}(\pi(H))=UH .
 \tag{3}
\]

The image of \(H\) is a closed unipotent algebraic subgroup. The exact
sequence
\[
 1\longrightarrow U\longrightarrow K
 \longrightarrow\pi(H)\longrightarrow1
 \tag{4}
\]
makes \(K\) unipotent, since that property is preserved by extensions.[^3]
It is transitive because it contains \(U\), and contains \(H\) by
construction. No normality of \(H\) is asserted.

The transitive-unipotent triangularization theorem gives actual
polynomial coordinates for \(K\), hence for \(\delta\).[^2]
This conclusion holds in every dimension. For \(n=4\), if
\(\delta(s)=1\), the action is proper by the slice decomposition
\(B=(\ker\delta)[s]\). The proper triangular fourfold theorem gives

\[
 \ker\delta\simeq\mathbb C^{[3]}.
 \tag{5}
\]

The four-dimensional restriction in (5) belongs to this last published
recognition input.[^4] Proper triangular actions in arbitrary dimensions
are not claimed to be translations.

### Why the previous nonsolvable control is not an obstruction

For
\[
 \delta=(1+4y(x+y^2))\partial_x-2(x+y^2)\partial_y,
 \qquad u=x+y^2,\quad v=y,
 \tag{6}
\]
with two passive variables, the closure is
\((\mathfrak{sl}_2\ltimes\mathbb C^2)\oplus\mathbb C^2\), of dimension seven.
It is not solvable, but the criterion applies.

In the coordinates \(u,v\), \(\delta=\partial_u-2u\partial_v\).
The integrating group's unipotent radical consists of all four
translations, whereas \(UH\) also contains the shear \(u\partial_v\).
The known invariant coordinate \(v+u^2\) independently confirms (5).
The example fails linear triangularization in its old frame, not
polynomial triangularization or cancellation.

The remaining quantifier is essential:
for a fixed cylinder \(B=A[s]=\mathbb C^{[4]}\),

\[
 A\simeq\mathbb C^{[3]}
 \quad\Longleftrightarrow\quad
 \text{some genuine polynomial frame has finite closure with }\partial_s.
 \tag{7}
\]

The forward implication uses the coordinates of \(A\) and \(s\).
The reverse is the proved criterion. No terminating search, universal
degree bound or construction of that frame for arbitrary \(A\) is known
from this work.

## 3. A reusable positive certificate verifier

A finite constant-coefficient bracket-closed spanning list is enough
to prove that (2) is finite-dimensional. It need not be a basis and its
members need not all be LNDs. The actual generators in (2) are the ones
whose local nilpotence matters.

[The independent premise verifier](research/finite_lie_certificate_checks_pass29.py)
checks all generator expressions, every pairwise bracket relation,
a polynomial slice and coordinatewise nilpotence identities
\[
 \delta^{n_i}(x_i)=0,\qquad \delta(s)=1.
 \tag{8}
\]
The iterated Leibniz rule promotes the four nilpotence identities to
local nilpotence on all polynomials. This implication and the precise
input contract are in [the certificate note](research/finite-lie-certificates-pass29.md).

The verifier accepts the nonsolvable seven-field certificate and an
ordinary translation certificate. It rejects a finite-closure field
having a slice equation but not local nilpotence. Constant structure
coefficients, all four translations and complete bracket tables are
mandatory.

Independent adversarial review found and repaired two input-validation
defects: relation objects could be coerced into polynomials, and float
or boolean indices could masquerade as integer table keys. Both now
have rejection controls. The final audit also checked dependent spanning
lists, which correctly return a dimension upper bound.

The verifier checks finite algebraic premises, not the published
integration and classification proofs. Its rational input and size
limits are implementation limits, not negative mathematical conclusions
for rejected candidates. It does not identify an unknown variety merely
from four supplied function names.

## 4. Exact horizontal selection in the canonical nonunit model

Retain the actual polynomial canonical homotopy
\[
 B=\mathbb C[\lambda,x,w,z],\qquad
 \Delta=x^2\partial_w+2(1+\lambda x)^2w\partial_z,
 \quad F=2xz-w^2,\quad L_0=x\partial_w+w\partial_z.
 \tag{9}
\]
Its original full plinth is \(x^2\), and the perturbation \(d=x\)
lies in its radical without being divisible by \(x^2\).

Consider exactly the horizontal LNDs satisfying
\(\delta(\lambda)=1,\ \delta(x)=\delta(F)=0\).
The complete classification is
\[
 \delta_G=\partial_\lambda+G(\lambda,x,F)L_0,
 \qquad G\in\mathbb C[\lambda,x,F].
 \tag{10}
\]
There are no other members of this stipulated family.

Necessity follows by differentiating \(F\), using \(\gcd(x,w)=1\),
and localizing over \(\mathbb C(x,F)\). A field
\(\partial_\lambda+P(\lambda,w)\partial_w\) is locally nilpotent
exactly when \(P\) is independent of \(w\): positive degree gives
nonvanishing iterates with controlled leading terms. A separate
pole-removal argument contracts the localized kernel correctly.

For sufficiency put \(J=\int_0^\lambda G\,d\lambda\). The polynomial
horizontal invariants and their full inverse are
\[
 a=x,\quad b=w-xJ,\quad c=z-Jw+\tfrac12xJ^2;
 \qquad
 x=a,\quad w=b+aJ,\quad z=c+bJ+\tfrac12aJ^2,
 \tag{11}
\]
where on the inverse side \(J\) is evaluated at
\((\lambda,a,\kappa)\), \(\kappa=2ac-b^2=F\).
Thus these are actual slice coordinates, even for time-dependent \(G\).

The exact primitive-top criterion is
\[
 \boxed{\text{primitive top of }\Delta\text{ is sliced}
        \quad\Longleftrightarrow\quad \partial_FG=0.}
 \tag{12}
\]
If \(J_\kappa\ne0\), writing \(s=\deg_\lambda J\),
\(r=\deg_\lambda J_\kappa\ge1\), the top has degree \(s+r+2\)
and primitive part \(a\partial_b+b\partial_c\), with a fixed line
and nonunit plinth. If \(J_\kappa=0\), its primitive part is
\(\partial_c\). The full formulas and all-degree proof are in
[the horizontal-selection note](research/horizontal-selection-pass29.md).

For every \(N\ge4\), choices
\(J_+=\lambda^{N-2}\) and \(J_-=\lambda^{N-3}+\lambda F\)
have the same relative degree \(N\) but opposite outcomes.
Also \(J=\lambda^3\) succeeds at degree five whereas \(J=\lambda F\)
fails at degree four. Degree is not a monotone proxy for this property.
The unique degree-two minimum within this family is the original
successful partial, so failure at the global minimum is not claimed.

## 5. A global obstruction that every fiber test missed

Let \(R_{\rm surf}\) be the unchanged conductor-glued surface, with
normalization
\[
 B_{\rm surf}=
 \mathbb C[u,y,z]/((u-1)(u-i)z-y(y-1)),
 \qquad
 T=\ker\partial=\mathbb C+(u^4-1)\mathbb C[u].
 \tag{13}
\]
All gluing parameters and the specified action are those already
proved in the preceding surface notes.

The completed local rings along its conductor lines are
\(\mathbb C[[\xi,\eta,t]]/(\xi\eta)\).
The new conclusion is
\[
 \boxed{R_{\rm surf}\ne\mathbb C[j,a,b]
        \text{ for every }j\in T\text{ and every }a,b\in R_{\rm surf}.}
 \tag{14}
\]

Here is the proof mechanism, with every global step detailed in
[the invariant-embedding note](research/global-invariant-embedding-pass29.md).

For nonconstant \(j\), let \(K=\mathbb C(j)\),
\(L=\mathbb C(u)\), and \(N=[L:K]=\deg_u j\).
The geometric generic fiber is a disjoint union of \(N\) reduced
affine lines. Suppose \(R_{\rm surf}=\mathbb C[j,a,b]\), and present
it as \(\mathbb C[J,X,Y]/(P)\) with \(J\) mapping to \(j\).

Over \(\overline K\), the zero set of \(P\) is a disjoint union of
embedded affine lines. Abhyankar--Moh rectifies one line. Disjointness
forces the coordinate of that line to restrict to a nonzero constant
on every other line, so all components are parallel coordinate fibers.[^5]

It follows that the actual ambient Hamiltonian
\(P_Y\partial_X-P_X\partial_Y\) is an LND, by descent of its vanishing
polynomial iterates. Dividing its coefficient gcd preserves local
nilpotence. The primitive relative-plane kernel theorem then gives
a **global** kernel \(\mathbb C[J,Q]\), so
\(P=\Phi(J,Q)\) globally, without inverting \(J-j_0\).[^6]
The regular-sequence case is sufficient; no slice is inferred there.

The induced action on the surface has the original full invariant
field \(L\). Flat kernel base change proves that the geometric
coordinate \(Q\) is affine in the parallel-line coordinate, so
\(\deg_Q\Phi=N\). Consequently the plane base curve
\(\mathbb C[j,\overline Q]\) has fraction field \(L\), not a smaller
subfield. Its finite normalization is exactly \(\mathbb C[u]\).

Every invariant takes the same value at \(u=1,i,-1,-i\).
Those four distinct normalization points therefore map to one point
of that plane base curve. They give at least four formal branches.[^7]
Its defining equation has order at least four at that point.

The global substitution \(P=\Phi(J,Q)\) forces the ambient equation
to have order at least four at a conductor point of the surface.
Such a hypersurface in smooth three-space has six independent quadratic
monomials in \(\mathfrak m^2/\mathfrak m^3\). The actual double crossing
has only five because of the nonzero quadratic relation \(\xi\eta=0\).
This is the contradiction. Constants are excluded separately by the
three-dimensional cotangent space.

Thus neither \(d\), \(d(u^2-1)\), nor any other invariant can have two
global companion generators. This does not contradict their planar
closed fibers: it is a global presentation obstruction.

The proof also gives the abstract quadratic-branch criterion recorded
in [the general branch-obstruction note](research/invariant-branch-obstruction-pass29.md):
three or more identified points in a rational invariant normalization
already suffice when the selected surface point has embedding dimension
three and a nonzero quadratic relation. No normality of the surface
or finite generation of its invariant ring is silently assumed.

A hypothetical three-generator presentation of this particular surface
must therefore use three noninvariant functions. An ambient extension
of the fixed action would have to be rank three, since an invariant
ambient coordinate would give a forbidden triple. Neither all-noninvariant
presentations nor rank-three ambient actions are excluded.

## 6. Verification and the next actual proof gap

The [saved complete regression](verification-pass-29.json) reruns
all 634 preceding methods and adds 10 certificate, 8 horizontal-selection
and 7 global-surface controls: 659 methods across 55 suites.
All three new checkers import only SymPy and unittest.
[The audit record](research/proof-audits-pass29.md) separates the full
proof reconstructions, source access limits, repaired input defects,
and finite symbolic controls.
[The consistency record](consistency-pass-29.json) checks artifact
integrity, not mathematical truth.

The next target is not another unrestricted search among invariant
companions or a claim that lower relative degree guarantees a slice.
The remaining substantive questions are universal construction of a
finite-closure frame, control of horizontal actions beyond the auxiliary
plane-fixing family, and genuinely all-noninvariant surface presentations
or ambient rank-three realization.

General cancellation, novelty determination, human specialist review and
proof-assistant verification remain unfinished. No contact, posting,
submission, payment, new user-owned task or automation occurred.

## Primary sources

[^1]: J. W. Bruce, A. A. du Plessis and C. T. C. Wall, [Determinacy and unipotency](https://doi.org/10.1007/BF01391830), Inventiones Mathematicae 88 (1987), 521-554, Theorem 3.6, printed pp. 535-536. The primary digitization's [statement](https://gdz.sub.uni-goettingen.de/fulltext/PPN356556735_0088/00000541?_format=xml) and [completion of the complex proof](https://gdz.sub.uni-goettingen.de/fulltext/PPN356556735_0088/00000542?_format=xml) were read directly. It concerns algebraic transitive actions, not only affine-linear ones.

[^2]: H. Kraft and M. Zaidenberg, [Algebraically generated groups and their Lie algebras](https://arxiv.org/pdf/2203.11356v4), Theorem 3.1.1(1) with proof and Theorem 5.2.2 with proof. Finite integration and transitive unipotent polynomial triangularization are separate inputs.

[^3]: J. S. Milne, [Algebraic Groups, 2017 edition](https://www.jmilne.org/math/Books/iAG2017.pdf), Corollary 14.7, unipotence under subgroups, quotients and extensions.

[^4]: A. Dubouloz, D. R. Finston and I. Jaradat, [Proper triangular Ga-actions on A4 are translations](https://msp.org/ant/2014/8-8/ant-v8-n8-p06-p.pdf), final unnumbered corollary on printed p. 1963 and its deduction.

[^5]: E. R. García Barroso and A. Płoski, [An approach to plane algebroid branches](https://arxiv.org/pdf/1208.0913), Theorems 6.6 and 6.9 with their proofs. Their algebraically closed characteristic-zero degree-divisibility result yields rectification by successive polynomial shears. The original Abhyankar--Moh publisher full text was not accessible in this pass; this primary proof reconstruction was inspected instead.

[^6]: S. M. Bhatwadekar and A. K. Dutta, [Kernel of Locally Nilpotent R-Derivations of R[X,Y]](https://repository.ias.ac.in/3203/1/311.pdf), Transactions of the AMS 349 (1997), 3303-3319, Theorem 4.7. The full selected argument was read in pass 27. Current direct proof-page refetches failed; the exact statement and assumptions were independently rechecked in the indexed primary text. Coprime polynomial coefficients give the required regular-sequence or comaximal alternatives globally.

[^7]: The Stacks Project, [Lemma 33.40.1, Tag 0C1S](https://stacks.math.columbia.edu/tag/0C1S), normalization preimages and branches. The note also supplies the finite-birational-conductor and completion argument needed to connect those points with formal plane branches.
