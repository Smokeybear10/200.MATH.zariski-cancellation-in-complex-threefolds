# Exact divisor multiplicities and the remaining point ideals

In the full second-degree Artin branch of the collapsed mixed fiber,
the degree-two divisor classification determines the divisorial parts
of all four initial derivative-image ideals. The two previously
undetermined matrix coefficients are units. The residual second and
fourth image ideals are genuine point-supported complete intersections,
not necessarily reduced points.

These are deductions under a branch assumption. The separate
[quartic argument](mixed-full-artin-quartic-exclusion-pass107.md)
now excludes that branch. None of
the statements below extends the supplied quadratic frame to an
arbitrary cancellation problem.

## 1. Local hypotheses

Let R=S_m be the regular local invariant plane, with maximal ideal n,
in the actual collapsed mixed sector with nonzero speed normal. Write
A_R for the faithfully flat domain, N for its locally nilpotent
derivation with full kernel R, and
\[
F_j=\ker(N^{j+1}|A_R),\qquad I_j=N^j(F_j),\qquad
F_j\simeq R^{j+1},\qquad
A_R/\mathfrak nA_R=\mathcal D[c],\quad
\mathcal D=\mathbb C[G]/(G^2(G-1)).
\tag{1}
\]
Assume the image W2 of F2 in this whole fiber is D. The actual
fiber derivation kills D. The retained full-Artin result106 gives
W3=D, a principal I3, a nonprincipal I4, and compatible free
complements to F2 in F3 and F4.[^modules]

Every height-one base prime has residue constant-field degree one
or two. In degree one the actual local slice gives every Ij the
unit ideal. In degree two, the surviving good generator and the
new exact DVR classification give
\[
\operatorname{ord}_{\mathfrak p}I_j
=\left\lceil j/2\right\rceil
  \operatorname{ord}_{\mathfrak p}I_1.
\tag{2}
\]
This is equality of image-ideal valuations. It uses the entire
DVR degree modules, not the derivative of one selected element.[^dvr]

## 2. The second-degree matrix coefficient is a unit

Faithful flatness makes 1 unimodular in the free module F1.
Choose a basis 1,r and put P=Nr, so I1=PR and P is nonzero.
Choose a basis 1,z,w of F2. An invariant shift of r gives
r=az+bw. Torsion freeness of F2/F1=I2 shows gcd(a,b)=1:
a common nonunit divisor would produce a nonzero torsion class
in R²/R(a,b).

The conic calculation, reconstructed in module102, then gives
\[
\begin{gathered}
Nz=\epsilon b r+B_1,\qquad Nw=-\epsilon a r+B_2,
\qquad P=aB_1+bB_2,\\
Q=\epsilon r^2-2B_2z+2B_1w\in R,\qquad
I_2=\epsilon P(a,b),\qquad \epsilon\in R\setminus\{0\}.
\end{gathered}
\tag{3}
\]
At every height-one prime the coprime ideal (a,b) becomes the
unit ideal, while (2) makes the valuations of I2 and P equal.
Thus epsilon has valuation zero at every height-one prime of R.
Since R is a local UFD, epsilon is a unit.

The map F2/nF2 into the whole fiber is injective by the assumption
W2=D and rank three. Since N kills D, its matrix in 1,z,w is
zero modulo n. In particular epsilon a² and epsilon b² belong
to n. The unit epsilon makes a,b belong to n. Neither is zero:
coprimality and properness would otherwise force the other to be
a unit. Consequently
\[
\boxed{\quad I_1=PR,\qquad I_2=PJ_2,\qquad
J_2=(a,b)\subsetneq R,\qquad \sqrt{J_2}=\mathfrak n.\quad}
\tag{4}
\]
The coprime nonzero pair a,b is a regular sequence. This gives
a maximal-primary complete intersection, not J2=n.

## 3. Normalizing the third and fourth images

The retained full-Artin matrix gives I3=gR and
I4=theta gJ4, where g and theta are nonzero elements of R and
J4 is a proper two-generated maximal-primary complete intersection.
Applying (2) with j=3, and using the principal ideal I3, shows
that g/P² has zero valuation at every height-one prime. It is
therefore a unit of R. Applying (2) with j=4 then shows theta
is a unit as well, since J4 becomes the unit ideal at height one.
Thus the equalities of ideals in the actual closed-point ring are
\[
\boxed{\quad I_3=P^2R,\qquad I_4=P^2J_4.\quad}
\tag{5}
\]
Units are absorbed only into generators, not into ideals or
unproved coordinate changes. This argument fixes the multiplicities
left open in106; it does not discard either residual point ideal.

The compatibility g in J4 I2 from that same matrix and the
Leibniz inclusion I2² contained in I4 now give, by cancellation
of the nonzero P,
\[
\boxed{\quad P\in J_2J_4,\qquad J_2^2\subseteq J_4.\quad}
\tag{6}
\]
These containments by themselves do not imply either ideal is
the maximal ideal or that the branch is impossible.

## 4. Purity gives the correct ideal square, including multiplicities

The residue-basis purity lemma says that a finite free submodule
with independent closed residues in a flat module is universally
injective. In the present setting it gives
F2 intersect HA_R = HF2 for every ideal H of R.[^purity]
Apply it to H=J2². Since r=az+bw, the element epsilon r²
belongs to J2²A_R. Equation (3) makes it also equal to the
F2 element Q+2B2z-2B1w. Comparing its coordinates in the pure
basis 1,z,w proves
\[
\boxed{\quad B_1,B_2,Q\in J_2^2,\qquad P\in J_2^3.\quad}
\tag{7}
\]
No replacement of J2 by its radical occurs. In particular this
is stronger than the first-base-jet conclusion B1,B2,Q in n².
It supplies coherent quadratic expressions in a,b even when
the residual point scheme is nonreduced.

Since J2 and J4 are proper, equations (4), (5), and (7) imply
\[
I_1\subseteq\mathfrak n^3,\qquad
I_2\subseteq\mathfrak n^4,\qquad
I_3\subseteq\mathfrak n^6,\qquad
I_4\subseteq\mathfrak n^7.
\tag{8}
\]
These are necessary containments within the assumed branch, not
a claim of exact orders or an argument that a finite-order zero
is identically zero.

## 5. Scope

The proof does not use the older reduced-second-image assumption,
trace inequalities on normalized curves, or a completion of A_R.
It uses the exact local divisor models now established for the
supplied original quadratic frame, the separate full-Artin module
argument106, and the general purity lemma. The lower-dimensional
W2 branch does not satisfy the residue-basis premise and does not
inherit these conclusions.

The separate actual quartic construction from the coefficients
in J2² supplies the fiber-dimension contradiction. The ideal
identities alone are not that contradiction. General and Root independently
reconstructed the normalizations. Separate AI reviews are not
human expert or formal proof certification, and no novelty claim
is made.

## Sources

[^modules]: [Full-Artin module106](mixed-full-artin-two-generator-pass106.md), Sections 1–6, and [degree-module102](quadratic-degree-module-fiber-rigidity-pass102.md), Sections 2 and 4. The latter's local conic computation is used with the current full residue basis, not its contradiction-specific basis.

[^dvr]: [Quadratic constant divisor107](quadratic-constant-divisor-filtration-pass107.md), all-degree basis and image formula; [independent normal-form proof107](quadratic-divisor-normal-form-gates-pass107.md); and [degree-one slice105](mixed-cubic-rank-defect-pass105.md), Section 2. The actual divisor input is [divisor91](nonconical-residue-degree-bound-pass91.md).

[^purity]: [Residue-basis purity107](residue-basis-purity-pass107.md), using the Stacks Project's [Lazard theorem, tag 058G](https://stacks.math.columbia.edu/tag/058G) and its [finite-factorization proof, tag 058C](https://stacks.math.columbia.edu/tag/058C), consulted September 14, 2026. The application needs flatness of A_R, not finiteness as an R-module.
