# FISI and the remaining coordinate-recognition gap

For a critical-point-free polynomial
\(G:\mathbb C^3\to\mathbb C\) with reduced leading homogeneous
part and general rationally acyclic fiber, the checked results prove
contractible fibers and topological triviality. They do not provide
the additional algebraic conclusion that \(G\) is a coordinate.

There is a precise historical reason to preserve that gap: the
original Siersma–Tibăr paper explicitly asks the corresponding
coordinate question for its larger isolated-singularity-at-infinity
class. This is evidence about what those results prove, not a claim
that the narrower FISI case remains open today.

## 1. The FISI source proves the topological reduction

[Siersma and Tibăr, *Deformations of polynomials, boundary
singularities and monodromy*](https://arxiv.org/pdf/math/0207076),
Definition 2.1 and the statement following (3.1), characterize FISI
by

\[
\dim\{\partial G_d=0\text{ in }\mathbb P^2\}\le0,
\qquad \dim\operatorname{Sing}G\le0.
\]

The reduced plane curve \(V(G_d)\) has only finitely many
singularities. Together with the empty affine critical locus, this
verifies FISI. Section 2 gives the general fiber the homotopy type
of a bouquet of two-spheres, with count

\[
b_2=\mu+\lambda.
\]

Rational acyclicity makes both nonnegative terms zero and makes
the fiber contractible. The atypical-value description following
(2.2) then removes every bifurcation value. All fibers share that
topology. These statements concern homotopy type and topological
fibrations, not algebraic trivializations.

Thus the hypotheses fit this theorem without a mismatch. The
missing step is in its conclusion: contractible surface is not the
stated algebraic conclusion \(\mathbb A^2\).

## 2. The original theorem expressly separates the coordinate question

[Siersma and Tibăr, *Singularities at infinity and their vanishing
cycles*, author preprint](https://webspace.science.uu.nl/~siers101/inftyST.pdf)
is the primary source for the wider isolated \(W\)-singularity
framework. Theorem 3.1 is the bouquet theorem; Corollary 3.5 gives
the sphere count \(\mu+\lambda\). Theorem 5.6 detects atypical
or nonsmooth fibers by their Euler-characteristic difference from a
general fiber. Corollary 5.8 relates \(\lambda=0\) to
\(t\)-regularity and \(M\)-tameness, and identifies topological
triviality when also \(\mu=0\).

The unnumbered question immediately after Remark 5.7, on preprint
page 10, asks whether

\[
\text{isolated }W\text{-singularities at infinity},\qquad
\mu=\lambda=0
\quad\Longrightarrow\quad G\text{ is a coordinate}.
\]

It notes the affirmative two-variable case. FISI is a subclass of
this framework, so our zero-cycle case is a special case of that
historical question. A question is not a theorem, and the theorem
on \(M\)-tameness cannot be cited as algebraic linearization.

The linked author preprint was directly checked. The publication is
Duke Mathematical Journal 80 (1995), 771–783; the available scanned
publication did not yield readable text in this pass, so the exact
question locator above intentionally refers to the preprint.

## 3. The available algebraic bridge requires an actual plane fiber

[Kaliman, *Polynomials with general C2-fibers are variables*,
Pacific Journal of Mathematics 203 (2002), 161–190](https://msp.org/pjm/2002/203-1/pjm-v203-n1-p08-p.pdf),
proves the conclusion in its title with \(\mathbb C^2\) meaning
the algebraic affine plane. The Main Theorem, page 162, requires a
Zariski open part of a smooth factorial affine threefold, with
\(H_3=0\) and constant units, mapped to a curve with all fibers
isomorphic to \(\mathbb A^2\), plus a condition on the excluded
components. For ambient \(\mathbb A^3\), this yields

\[
\text{general algebraic fiber }\simeq\mathbb A^2
\quad\Longrightarrow\quad G\text{ is a coordinate}.
\]

The precise mismatch is the fiber-isomorphism premise. The FISI
bouquet theorem verifies contractibility, not that premise. Its
topological trivialization also does not produce the Zariski-local
algebraic plane cylinder used in Kaliman's argument.

## Bounded conclusion

The valid chain stops at

\[
\text{reduced leading form and no affine critical points}
\Longrightarrow\text{FISI}
\Longrightarrow
\bigl(\text{general rational acyclicity}
\Longrightarrow\mu=\lambda=0\bigr)
\Longrightarrow\text{topologically trivial contractible fibers}.
\]

An additional theorem identifying the general algebraic fiber with
\(\mathbb A^2\), or directly proving coordinatehood in this
FISI subclass, is still needed for the proposed deduction. The
three sources above do not supply it. This pass checked exact FISI,
reduced-leading, zero-vanishing-cycle, and coordinate formulations;
it did not audit every later reference or establish a present-day
open-problem status. A degree bound, such as degree at most four,
would be an additional restriction not settled by the historical
question alone.
