# Saturated fiber multiplicity gives a finite free local model

Equality in the flat-rank bound has a stronger consequence than the
inequality: it forces a module not initially assumed finite to be
finite free. Applied to the actual nonconical frame, a closed fiber
whose total multiplicity is six gives the full normalization of a
regular two-dimensional local base in a degree-six field extension.
This is a local description of the remaining cubic cases, not their
exclusion or a global cancellation theorem.

## 1. A finite-rank flat-module lemma

Let T be a Noetherian local domain with maximal ideal m, residue
field k, and fraction field F. Let M be a flat T-module. Suppose
\[
\dim_F(M\otimes_T F)=n<\infty,
\qquad \dim_k(M/mM)=n.
\tag{1}
\]
Then any lifts \(e_1,\ldots,e_n\) of a residue basis form a T-basis
of M. In particular M is finite free. There is no hypothesis that
M is finite, complete, or separated for its m-adic filtration.
The case n=0 follows immediately from flat torsion-freeness, so
assume n is positive.

Flatness identifies the successive quotients as
\[
m^jM/m^{j+1}M
 \simeq (m^j/m^{j+1})\otimes_k(M/mM).
\tag{2}
\]
Indeed tensor the inclusions of ideals and their quotient exact
sequences with M. Their images in M are the indicated ideal
products. This proof works for a non-finite flat module.

The lifts are F-linearly independent. Clear denominators in a
putative relation, obtaining \(\sum_i a_i e_i=0\) with coefficients
in T, not all zero. Krull intersection in the Noetherian local
domain T gives a finite least m-adic order j among its nonzero
coefficients. Equation (2) turns their nonzero initial vector
into a nonzero element of \(m^jM/m^{j+1}M\), a contradiction.
By (1) the lifts consequently form an F-basis after tensoring.
Flatness also embeds M in this generic vector space.

For every positive h the map induced by these same lifts is an
isomorphism
\[
\phi_h:(T/m^h)^n\xrightarrow{\ \sim\ }M/m^hM.
\tag{3}
\]
For surjectivity, the residue basis gives
\(M=\sum_iTe_i+mM\). Iterating this equality h times gives
\(M=\sum_iTe_i+m^hM\). This finite iteration is not an application
of Nakayama's lemma to a module of unproved finite type.
For injectivity, if a coefficient vector is not in \((m^h)^n\),
take its least order j, which is less than h. Equation (2) shows
its image is not in \(m^{j+1}M\), hence not in \(m^hM\).
The maps and their inverses are compatible with reduction in h.

For any z in M, its generic expansion permits clearing denominators:
choose nonzero a in T and \(b_i\in T\) with
\(az=\sum_i b_i e_i\). Apply the compatible inverses in (3) to
the classes of z. They define coefficients in the completion of T,
and the relation gives
\[
\widehat c_i\in\widehat T=\varprojlim_h T/m^h,
\qquad a\widehat c_i=b_i,
\qquad a\widehat T\cap T=aT.
\tag{4}
\]
The last equality follows from faithful flatness of the completion
of a Noetherian local ring.[^completion] Equivalently, the map from
T/aT to its scalar extension by \(\widehat T\) is injective.
Thus \(b_i=ad_i\) for some \(d_i\in T\). Torsion-freeness cancels
a in the original relation and gives \(z=\sum_i d_i e_i\).
This proves spanning and completes the proof.

Only T was completed. No injectivity of \(M\to\widehat M\),
identification of its completion with a tensor product, or prior
finite generation of M was used.

## 2. Application to every component of an actual fiber

Use exactly the rings of
[total-multiplicity92](nonconical-total-fiber-multiplicity-pass92.md).
Here \(S=\mathbb C[s_1,s_2]\), \(K=\operatorname{Frac}S\),
\(A_K=K[v]\), and \(A=S[A_1,A_2,c]\) is a smooth threefold.
Choose a complex linear combination U of \(A_1,A_2,c\) nonconstant
on every component of the fiber over a closed base point m. Let
\(\mathfrak q_i\) be those generic component primes, and set
\[
\begin{gathered}
T=(S[U])_{mS[U]},\qquad
O'=(A\setminus\bigcup_i\mathfrak q_i)^{-1}A,\qquad
F=K(U),\\
\dim_F(O'\otimes_T F)=n=\deg_vU\le2d,\qquad
\dim_{T/mT}(O'/mO')=\sum_i\mu_i f_i,\\
f_i=[\kappa(\mathfrak q_i):\mathbb C(\bar U_i)].
\end{gathered}
\tag{5}
\]
The retained proof establishes the actual contractions, regular
local source of dimension two, semilocal target, and flatness.
It does not assume a finite morphism. If
\(\sum_i\mu_i f_i=n\), the lemma supplies precisely that missing
finiteness: O' is free of rank n over T.

Moreover O' is then the full integral closure of T in K(v).
It is a normal domain because it is a localization of smooth A,
and its fraction field is K(v). Finite module type makes every
element of O' integral over T. Conversely, an element of K(v)
integral over T is also integral over O', using the same monic
equation, and hence belongs to the integrally closed ring O'.
This establishes equality of the rings, not just an embedding in
a normalization or an identification of their completions.

## 3. The saturated cubic profiles

In degree d=3, if \(\sum_i\mu_i=6\), the inequalities in (5)
and positivity of every \(f_i\) force
\[
\sum_i\mu_i=6
\quad\Longrightarrow\quad
n=6,\quad f_i=1\text{ for all }i,\quad
O'\text{ is finite free of rank six over }T.
\tag{6}
\]
This applies to every admissible common U chosen above. In
particular it applies to the remaining cubic profiles (6), (5,1),
(4,2), and (4,1,1), whenever such a fiber actually exists. These
lists record necessary numerical possibilities, not constructions.

For the single rank-zero component of multiplicity six, the
[actual-plane theorem92](nonconical-collapsed-component-plane-pass92.md)
gives \(A/\mathfrak q=\mathbb C[\bar c]\). Choose U=c itself.
Then \(f=1\), \(\deg_vc=6\), and the local ring
\(O=A_{\mathfrak q}\) is finite free of rank six over
\((S[c])_{mS[c]}\). Both residue fields are \(\mathbb C(\bar c)\).
It is a regular local integral closure with a length-six closed
fiber. The ramification argument92 still requires the retained
degree-two and degree-three branches. Neither that requirement
nor finite freeness is a contradiction.

The profile (4,1) has total multiplicity five. If its common U
has degree five, the same argument forces all residue degrees
one and finite freeness of rank five. If its degree is six, the
bound still forces every residue degree one except possibly the
multiplicity-one companion, whose residue degree may be two.
Finite freeness follows when the weighted sum is six, but is not
proved when the weighted sum is five and n is six.

## 4. Limits, controls, and sources

Equality is essential. For a nonzero nonunit a of a local domain
T, the flat module \(T\oplus T[1/a]\) has generic rank two but
special-fiber dimension one. Its second summand is not finite:
it equals its product by a, so finite generation would contradict
Nakayama while the summand is nonzero. This control prevents
replacing the equality hypothesis by the inequality alone.

The result concerns the specific semilocal ring O'. It does not
prove that A is finite over S[U], that the smaller ring
\(S[A_1,A_2]\) equals A, that the quotient is smooth at this
fiber, or that the intrinsic action has no fixed points. It also
does not supply the missing reduction of arbitrary sliced actions
to the nonconical frame.

The proof is a derived application of flatness, Krull intersection,
and faithfully flat completion, not a historical novelty claim.
Its outline was independently reconstructed before saving; final
saved-file review is recorded separately. No numerical test or
formal proof is presented as verification of this universal lemma.

## Sources

[^completion]: The Stacks Project,
    [Lemma 10.97.3, tag 00MC](https://stacks.math.columbia.edu/tag/00MC),
    faithful flatness of Noetherian local completion, and
    [Lemma 10.97.2, tag 00MB](https://stacks.math.columbia.edu/tag/00MB),
    flatness of completion. Both complete displayed statements
    and proofs were read on September 14, 2026. The ideal
    contraction in (4) follows by faithful flatness; no finiteness
    statement about M is imported from the source. For the source
    separation used above, the complete displayed statement and
    proof of [Krull intersection, tag 00IP](https://stacks.math.columbia.edu/tag/00IP)
    were also read on that date. It is applied to the finite
    module T itself, not to the initially non-finite module M.
