# Universal-frame relevance: the relative-fibration gate

The local divisor program does not yet imply unrestricted complex
threefold cancellation. Its polynomial intrinsic quotient is useful,
but it cannot be substituted for an invariant ambient coordinate or
for the base of an affine-space fibration. At every remaining primitive
plinth divisor, the actual residue field gives an explicit obstruction
to the latter substitution.

This is a bounded source/applicability audit and an elementary
consequence of the saved divisor theorem, not a new classification
theorem or a claim that the general problem is nearly solved.

## 1. Three different remaining implications

Write
\[
B=\mathbb C[x_1,x_2,x_3,x_4]=A[s_*],\qquad
E(s_*)=1,\quad A=\ker E.
\tag{1}
\]
The current README, [working pass51 checkpoint](checkpoint-pass51-working.json)
and [pass51 synthesis](../deep-pass-51.md) distinguish the following
obligations. The checkpoint's historical verification status is not used
as a claim about a later integrated regression.

1. In the supplied independent-defect, degree-two branch, finish the
   actual higher-degree fiber algebra and its global recognition. Full
   divisor models and failure of cubic generation at a reduced
   second-image point do not exclude that point. Even global quadratic
   generation is a presentation statement, not automatically polynomial
   recognition.
2. Finish the entire supplied adjoint profile \((1,1,2,2)\). The
   degree-two independent-defect branch is only part of this profile;
   moving higher-flow and dependent-defect branches have their own
   remaining hypotheses and reductions.
3. For arbitrary (1), produce an actual recognized coordinate frame or
   obtain an invariant ambient coordinate by a different argument.
   Neither of the first two tasks proves this existence statement.

Here an actual frame means polynomial coordinates with a polynomial
inverse, not a basis of the tangent module, a rationally independent
family of vector fields, or local coordinates after invariant inversion.

For precise height bookkeeping, retain
\(H=\sum_i(q_i+1)\) from the
[slice-filtration definition](coordinate-frame-minimization-pass.md).
A partial of degree \(-1\) already recognizes the kernel. Otherwise
the filtration degrees agree with the corresponding adjoint heights.
The all-profile recognition threshold remains \(H\le9\); the other
height-ten profiles \((1,1,1,3)\) and \((0,2,2,2)\) were separately
closed in passes 41 and 42.

Consequently, **if** full \((1,1,2,2)\) recognition is completed, then
an additional universal assertion
\[
\text{every sliced }E\text{ in (1) has }H_{\min}(E)\le10
\tag{2}
\]
would imply cancellation. This is a conditional implication, not an
established bound. Well-ordering gives a minimum without bounding it.
The exact all-inverse-pairs ideals in
[pass43](universal-frame-search-pass43.md) give a positive semidecision,
not termination or a finite rejection certificate for every degree.
Those earlier constructions are not new results of this audit.

## 2. The primary residual-rank theorem has a fiber hypothesis

Babu, Das and Lokhande define an affine \(n\)-fibration to have
polynomial fibers over **every** prime of its base. Their residual
systems and residual ranks are defined only after this premise.
Corollary 3.11 concerns relative dimension three: for a fixed-point-free
base-linear LND, a slice is equivalent to residual rank at most two.
Its proof uses two-dimensional cancellation on the fibers; Remark
3.10 explicitly identifies the higher-dimensional cancellation gap.
Over a field, Definition 3.1 reduces residual rank to coordinate rank,
not the fraction-field rank of a family of derivations.[^rank]

Thus using base \(\mathbb C\) in (1) gives relative dimension four.
Using base \(A\) gives the already known one-variable polynomial
extension \(A[s_*]\), which says nothing new about \(A\).
Using an unspecified \(\mathbb C[t]\) requires proving an invariant
base and the actual relative-fibration hypothesis.

The related affine-plane result is also conditional: Babu and Das,
Theorem 4.4, start with an \(\mathbb A^2\)-fibration over a
Noetherian \(\mathbb Q\)-algebra and a fixed-point-free base-linear
LND. They obtain an affine-line-fibration kernel and a slice. For a
seminormal base their kernel is the symmetric algebra of a rank-one
projective module.[^plane] This would recognize (1) over the intrinsic
polynomial plane **if the affine-plane-fibration premise held**.

## 3. Exact obstruction over the actual intrinsic quotient

In the remaining degree-two setup, let \(D\ne0\) be the chosen
primitive intrinsic LND of \(A\), and write
\[
C=\ker D\simeq\mathbb C^{[2]},\qquad
\operatorname{pl}(D)=pC,\quad Dr=p.
\tag{3}
\]
The quotient and faithful-flatness theorem is an inherited input;
this note does not repeat its pass51 foundational audit.

For a prime element \(\pi\in C\), set
\(\kappa=\operatorname{Frac}(C/\pi C)\). The
[full residue proof](quadratic-residue-degree-pass46.md) gives
\[
A\otimes_C\kappa=F_\pi[t],\qquad
B\otimes_C\kappa=F_\pi[t,s_*],\qquad
[F_\pi:\kappa]=1\ \Longleftrightarrow\ \pi\nmid p.
\tag{4}
\]
In a still-unrecognized case, every \(\pi\mid p\) has degree
exactly two. These are entire generic divisor fibers, not the image
of the bad-coordinate ring or the fiber of a chosen approximation.

**Relative-fibration obstruction.** Under these inherited hypotheses,
\[
B\text{ is an }\mathbb A^2\text{-fibration over }C
\quad\Longleftrightarrow\quad p\in C^*.
\tag{5}
\]

If \(p\) is a unit, \(r/p\) is an actual intrinsic slice, so
\(A=C[r/p]\) and \(B=C[r/p,s_*]\). Conversely, if \(p\) is
not a unit, choose a prime divisor \(\pi\). By (4), its residue
ring contains a proper finite algebraic extension \(F_\pi\) of
\(\kappa\). In \(\kappa[U,V]\), an element algebraic over
\(\kappa\) is constant: a nonconstant polynomial has positive
degree, and its powers have distinct leading degrees. Therefore
\(F_\pi[t,s_*]\) cannot be \(\kappa[U,V]\).

In the degree-two case the stronger geometric distinction is explicit:
\[
(B\otimes_C\kappa)\otimes_\kappa\bar\kappa
\simeq\bar\kappa[t,s_*]\times\bar\kappa[t,s_*].
\tag{6}
\]
It is a disjoint pair of affine planes, not one affine plane.
Characteristic zero supplies separability. Smoothness of the total
space and faithful flatness of \(C\subset B\) do not change (6).

Thus the source theorem's missing premise is not merely unverified
for the retained action: it fails at its nontrivial primitive plinth
divisors. Inverting \(p\) gives the correct relative polynomial
chart, but omits exactly these fibers. Passing to a splitting field
still gives two planes and does not trivialize the whole fiber.

## 4. Polynomial countercontrol to an overstrong relative claim

The distinction already occurs when the unknown ring is actually
polynomial. Reuse the classical control, already present in
[pass38](literature-scope-pass38.md):
\[
A_0=\mathbb C[x,y,z],\quad
D_0=x\partial_y+2y\partial_z,\quad
C_0=\mathbb C[x,h],\quad h=xz-y^2.
\tag{7}
\]
Its kernel is \(C_0\). Indeed, after inverting \(x\) the kernel
is \(\mathbb C[x,x^{-1},h]\); a smallest possible \(x\)-pole
cannot survive in \(A_0\), since evaluation at \(x=0\) sends a
nonzero polynomial in \(h\) to the nonzero polynomial in \(-y^2\).

For \(B_0=A_0[s_*]\) and \(E_0=\partial_{s_*}\), all of (1)
holds. Over the generic divisor \(x=0\) in \(C_0\),
\[
B_0\otimes_{C_0}\mathbb C(h)
=\mathbb C(h)[y,z,s_*]/(y^2+h)
=\mathbb C(h)(\sqrt{-h})[z,s_*].
\tag{8}
\]
The valuation of \(-h\) at \(h=0\) is odd, so it is not a square
in \(\mathbb C(h)\). This is exactly the obstruction in (6), in
an actual polynomial cylinder. No unresolved full-frame realization
or new counterexample to cancellation is claimed. It shows why
polynomiality of \(A\) does not itself force relative triviality
for a specified intrinsic action and quotient.

## 5. The safe recognition target remains an actual coordinate

If one proves that \(E\) fixes an ambient coordinate \(u\) of
\(B\), then the regular-kernel theorem of Bhatwadekar, Gupta and
Lokhande applies to the \(\mathbb C[u]\)-linear derivation on
\(\mathbb C[u]^{[3]}\). The slice makes \(A\) regular, so its
conclusion is \(A=\mathbb C[u]^{[2]}\).[^regular]

Neither a generator of the abstract polynomial plane \(C\), nor a
residue parameter in (4), is thereby an ambient coordinate. This
coordinate-recognition gate and the proposed universal bound (2)
remain unproved. The literature checked here supplies conditional
recognition, not either missing implication.

## 6. Scope and source record

Deduplication found the rank/fibration route already in
[the mixed-flow source audit](mixed-flow-literature-pass.md), and
the unrestricted coefficient search already in pass43. The fresh
application here is the exact failure of the relative-fibration
premise using the later full divisor fields. No new finite checker,
regression total, metadata update or novelty claim is made.

The primary rank paper's definitions, relevant theorem statements
and proofs through Corollary 3.11, the affine-plane theorem and its
complete proof, and the regular-kernel theorem and its complete proof
were directly read in this audit. The arXiv versions below, not an
unread comparison with the typeset versions, determine theorem
numbering. This is an independent AI source/proof review, not human
expert review or formal proof verification.

[^rank]: Janaki Raman Babu, Prosenjit Das and Swapnil A. Lokhande,
[*Rank and rigidity of locally nilpotent derivations of affine fibrations*](https://arxiv.org/pdf/2210.10285v1),
arXiv:2210.10285v1, October 19, 2022, Definition 3.1, Remark 3.4(4),
Theorem 3.6, Remark 3.10 and Corollary 3.11, PDF pp. 6-12.
The [primary arXiv record](https://arxiv.org/abs/2210.10285) lists the
2021 publication in *Communications in Algebra* 49(12), DOI
[10.1080/00927872.2021.1939360](https://doi.org/10.1080/00927872.2021.1939360).
The later deposit date is retained, not treated as a revised theorem.

[^plane]: Janaki Raman Babu and Prosenjit Das,
[*Structure of A2-fibrations having fixed point free locally nilpotent derivations*](https://arxiv.org/pdf/2001.07632v5),
arXiv:2001.07632v5, July 15, 2020, Theorem 4.4 and proof,
PDF pp. 7-8; published
in *Journal of Pure and Applied Algebra* 225 (2021), 106763,
DOI [10.1016/j.jpaa.2021.106763](https://doi.org/10.1016/j.jpaa.2021.106763).

[^regular]: S. M. Bhatwadekar, Neena Gupta and Swapnil A. Lokhande,
[*Some K-theoretic properties of the kernel of a locally nilpotent derivation on k[X1,...,X4]*](https://arxiv.org/html/1501.01438v1),
arXiv:1501.01438v1, Theorem 3.5 and proof; also directly read in
the retained PDF, printed p. 11. The theorem assumes characteristic
zero, a nonzero derivation fixing an actual ambient variable, and
a regular kernel.
