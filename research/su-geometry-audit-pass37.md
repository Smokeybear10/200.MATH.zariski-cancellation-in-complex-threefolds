# Rank-two coordinate slices in Su's cells

The selected walk is admissible. More importantly, its first braid
parameter is a coordinate slice for the actual additive action, not merely
an abstract slice supplied by stable polynomiality. The same argument
applies to all 80 threefold factors in the six-puncture rank-two example:
they are polynomial threefolds, using the action and coordinate
identifications stated in Su's paper. This is a source-dependent
deduction with an explicit geometric proof below. It is not a solution
of cancellation, a claim about higher rank, or a novelty claim.

The broader rank-two cancellation phenomenon is already explicit in
Anton Mellit's [*Toric stratifications of character varieties*, Section
1.4, journal p. 160](https://link.springer.com/content/pdf/10.1007/s10240-025-00158-0.pdf):
the affine-line factor can be cancelled compatibly with the
stratification in rank two. That published statement was directly
read. The purpose of this note is the exact identification of Su's
affine-factor quotients, including the 80 specified indices, with
coordinate hyperplanes. It does not claim priority for rank-two
compatible cancellation.

## 1. Exact source inputs

The initial source is Tao Su, [*Cell decomposition and dual boundary complexes
of character varieties*, arXiv:2307.16657v4](https://arxiv.org/pdf/2307.16657v4),
dated 30 August 2024. Unqualified numbering below refers to that version.
The corresponding gates were also checked directly in the
[2026 journal version, *Advances in Mathematics* 498, 111043](https://doi.org/10.1016/j.aim.2026.111043);
the version comparison appears in Section 6.

The relevant gates are specific. Definition 1.14 specifies the Borel
action on braid parameters. Proposition 1.16 and Appendix A supply
actual cell coordinates. Lemma 2.5(a) identifies the braid projection
from the character-variety prequotient as equivariant. Equations
(2.3.7), (2.4.3), and Proposition 2.9 describe its product coordinates.
Theorem 2.10, with Appendix B.8--B.15, makes the affine-factor quotient
an actual principal unipotent bundle with affine base, then trivializes
it. For rank two this group is the one-dimensional additive group.
Remark 2.12 calls the 80 factors potential counterexamples; their
nonpolynomiality is not a theorem.

The deduction below needs the equivariant projection, not an unproved
claim that all extra affine coordinates are fixed by the action.

## 2. A coordinate slice gives a polynomial quotient

Let an algebraic additive action on
\(X=\operatorname{Spec}k[q,z_2,\ldots,z_N]\) satisfy
\[
q(t\mathbin{\cdot}x)=q(x)-t.
\tag{1}
\]
Here \(q\) is stipulated to be an actual member of a polynomial
coordinate system. Set \(H=\{q=0\}\simeq\mathbb A^{N-1}\).
The two maps
\[
\Phi:\mathbb A^1\times H\longrightarrow X,
\qquad (a,h)\longmapsto(-a)\mathbin{\cdot}h,
\]
\[
\Psi:X\longrightarrow\mathbb A^1\times H,
\qquad x\longmapsto\bigl(q(x),q(x)\mathbin{\cdot}x\bigr)
\tag{2}
\]
are regular and inverse. Indeed (1) puts the second component of
\(\Psi\) in \(H\), and the group law verifies both compositions.
Thus the geometric quotient is \(H\), and its invariant ring is
polynomial in \(N-1\) variables.

If \(\partial\) is the infinitesimal derivation, its invariant
coordinates can equivalently be written as finite sums
\[
Z_j=\sum_{a\ge0}\frac{q^a}{a!}\partial^a(z_j),\qquad 2\le j\le N.
\tag{3}
\]
Local nilpotence makes each sum finite; \(\partial q=-1\) makes
adjacent terms cancel under \(\partial\). Formula (2) proves
algebraic independence and generation, not just invariance.

An arbitrary slice does not justify this conclusion: without the
coordinate hypothesis, its zero fiber need not be known polynomial.
It is precisely that extra hypothesis which the first braid parameter
will provide.

## 3. The rank-two action and the first up coordinate

Use the matrices
\[
H(t)=\begin{pmatrix}1&t\\0&1\end{pmatrix},\qquad
B(e)=\begin{pmatrix}0&1\\1&e\end{pmatrix}=sH(e).
\]
The defining identity is simply
\[
B(e_1)H(-t)=B(e_1-t).
\tag{4}
\]
There is no residual upper-triangular factor. Applying the precise
action rule of Definition 1.14 to a nonempty rank-two braid word
therefore gives, for raw braid parameters,
\[
H(t):\quad e_1\longmapsto e_1-t,\qquad
e_m\longmapsto e_m\quad(m>1).
\tag{5}
\]
This is an identity of the matrix diagrams as well as of matrices:
the adjacent two upper-root factors combine immediately. Thus it
does not rely on incorrectly inferring uniqueness of a long braid
factorization from its matrix product alone.

Every walk starts at the identity. Its first step is necessarily an
up step. Appendix A, equations (A.0.2)--(A.0.3), starts the recursive
coordinate construction with previous factor equal to the identity,
so its first affine coordinate is exactly
\[
e'_1=e_1.
\tag{6}
\]
In particular this is not a nonlinear function of all affine
coordinates that happens to have derivative one.

There is a useful stronger calculation on the braid coordinates.
Every rank-two up step has previous Weyl element equal to the identity.
Write the preceding product as
\[
M_{m-1}=\begin{pmatrix}a&b\\0&d\end{pmatrix}.
\]
Its diagonal entries are units on this cell. Right multiplication by
\(H(-t)\) changes \(b\) to \(b-ta\), leaving \(a,d\) fixed.
The recursive up coordinate is
\[
e'_m=(d/a)e_m+b/a.
\]
Consequently every up coordinate changes by \(-t\), not only the
first one. The stay coordinates are unchanged, as also follows from
the invariant torus projection. Hence on the braid affine factor
the action is simultaneous translation of its up coordinates.

## 4. Transfer to the actual character-variety affine factor

Fix an admissible cell and use the product coordinates
\[
X''=\widetilde T_p\times
       \mathbb A^{|U_p|}\times\mathbb A^{n_{\mathbf w}}.
\tag{7}
\]
The middle coordinates are precisely the recursively defined up
coordinates; the last coordinates are the additional unipotent
factors from (2.3.7). This is an isomorphism of varieties, not a
dimension count.

The projection to the braid factor is equivariant by Lemma 2.5(a).
It follows from (5)--(6) that the pullback of \(e'_1\) still obeys
\(e'_1(t\cdot x)=e'_1(x)-t\) on \(X''\), irrespective of the
motion of the last factor. The torus coordinate is invariant under
the additive subgroup, so any chosen closed torus fiber
\[
Y=\{\tau\}\times\mathbb A^{|U_p|+n_{\mathbf w}}
\tag{8}
\]
is an actual stable affine space. On it, \(e'_1\) is still one of
the displayed polynomial coordinates.

Apply (2) to this affine space. Its quotient is the hyperplane
\(e'_1=0\), hence
\[
Y/\mathbb G_a\simeq
\mathbb A^{|U_p|+n_{\mathbf w}-1}.
\tag{9}
\]
The factor called \(\mathcal A_\mu(\mathbf w,p)\) in Theorem 2.10
is exactly this geometric quotient, by its construction in the
second paragraph of part (1). Uniqueness of geometric quotient
identifies it with (9).

This closes the extra-factor gate. In particular, if some Bruhat
index is the identity, its additional affine coordinate must not be
discarded or assumed fixed. Formula (2) handles its actual polynomial
motion. No simultaneous triangularization of the whole action is
needed, and no cancellation theorem is inserted into this step.

For the selected all-\(s\) tuple, the extra factor is absent. If
the four up coordinates are \(a_1,a_5,a_7,a_9\), the quotient
coordinates are explicitly
\[
a_5-a_1,\qquad a_7-a_1,\qquad a_9-a_1.
\tag{10}
\]
The coordinate inverse appends \(a_1\) and adds it back to each
of these differences.

## 5. The selected walk and all 80 factors

Take five nontrivial Bruhat indices in \(S_2=\{1,s\}\). Their
word has length ten and is \(\sigma_1^{10}\). In chronological
order, the selected walk is
\[
(1,s,s,s,1,s,1,s,1,s,1).
\tag{11}
\]
Its up steps are \(1,5,7,9\), stays \(2,3\), and down steps
\(4,6,8,10\). These obey Definition 1.15 at every step. The
conjugates associated with either stay are \(s\), so they generate
\(S_2\); Definition 2.7's admissibility test is satisfied.

The selected cell has one torus coordinate before the diagonal
quotient and four affine coordinates before the additive quotient.
Thus (10) is a three-dimensional polynomial quotient, not a merely
stably polynomial one.

For completeness, all 80 threefold factors fall under the same
argument. Let \(r\) be the number of nontrivial entries among the
five Bruhat indices. Their braid length is \(2r\), and the
threefold factors have two stays. Hence
\[
|U_p|=r-1,\qquad n_{\mathbf w}=5-r,\qquad
|U_p|+n_{\mathbf w}=4.
\tag{12}
\]
Here \(2\le r\le5\), so there is always a first up coordinate.
For fixed \(r\), a rank-two walk is a sequence of \(r-1\)
up/down excursions, with the two stays distributed among them.
There are \(\binom r2\) such distributions. Selecting the
nontrivial Bruhat entries gives
\[
\sum_{r=2}^{5}\binom5r\binom r2=10+30+30+10=80.
\tag{13}
\]
Each quotient in (12) is therefore \(\mathbb A^3\) by (9).
The empty word is not an omitted exception in this family: it
cannot have an admissible stay, and its genus-zero admissibility
subgroup is trivial.

The same nonempty-word gate also holds if Section 4 is applied in
the general rank-two setup with handles. The positive-word formula
(1.3.15) gives
\[
\ell(\beta)=2\sum_{j=1}^{2g}\ell(\tau_j)
             +2\sum_{i=1}^{k-1}\ell(w_i).
\]
If it vanishes, every \(\tau_j,w_i\) is the identity and there
are no stays. Then \(J_p\) is trivial and does not act transitively
on two letters. Thus no admissible rank-two cell has an empty word.
This identifies the general gate explicitly; the concrete candidate
conclusion of this audit remains the 80 threefold factors above.

The rational eigenvalue choice recorded in pass 36 also meets the
rank-two genericity condition. Pair consecutively the list consisting
of the first eleven primes followed by their product's reciprocal.
A one-per-pair product not using
that reciprocal is greater than one. A product using it omits
positive prime factors and is less than one. Neither equals one,
while the total determinant product is one and each pair has
distinct eigenvalues. This verifies the chosen parameters; (9)
does not otherwise depend on their numerical values.

## 6. Audit and scope boundaries

Directly read source sections include Definition 1.1 and Assumption
1.4; Definitions 1.14--1.15 and Proposition 1.16; Lemma 2.5 and its
proof; Lemma 2.6, Definition 2.7, Corollary 2.8 and Proposition 2.9;
the complete Theorem 2.10 proof and Remark 2.12; Appendix A's
coordinate/action proof; and Appendix B's quotient, restriction,
subgroup and unipotent-trivialization arguments.

The journal source was subsequently read directly at the decisive
passages. Its Lemma 2.5(a), equation (2.3.11), Proposition 2.9 and
Theorem 2.10 retain the same equivariant projection, product coordinates,
and affine-factor quotient. The old action Definition 1.14 is now
Definition 1.15; the old walk Definition 1.15 is now Definition 1.17;
and Proposition 1.16 is now Proposition 1.18. The up-coordinate formula
is unchanged, now unnumbered immediately after (A.0.2), journal p. 64.
Added Example A.2, pp. 68--71, explicitly confirms the first-coordinate
translation and the four-crossing stay calculation used here. Journal
Remark 2.12, p. 50, still lists 80 potential candidates, not a
nonpolynomiality theorem. No change to the proof above is required.

The essential conclusion is a coordinate recognition statement for
these actual rank-two cells. It does not claim that an arbitrary
additive action on affine four-space has a coordinate slice, that
every character-variety factor in higher rank is polynomial, or
that the general threefold cancellation conjecture is settled.
Nor does it assert pairwise nonisomorphism of the 80 indexed cells.

Separate finite matrix checks can verify (4), the selected recursive
coordinates, and the polynomial inverse (10). They do not replace
the equivariance and product-coordinate gates in Section 4. No new
checker is duplicated here. The complete independent selected-cell
suite [su_cell_checks_pass37.py](su_cell_checks_pass37.py) was read
and run: eight methods passed in 0.229 seconds. Its checks concern
the selected matrix/action formulas, not the universal extra-factor
argument. No external contact,
submission, expert review, Lean formalization, or novelty declaration
has occurred.
