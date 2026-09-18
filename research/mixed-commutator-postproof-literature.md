# Mixed commutators and rational Burgers: post-proof overlap check

There is a published predecessor for the rational Burgers classification
sublemma: Saleeby's Theorem 1(ii). The bounded search did not locate an
identical four-variable mixed-commutator recognition theorem. These are
separate findings. Neither the search result nor the present proof is a
claim of novelty or exhaustive literature coverage.

## 1. The statement compared

The project statement concerns a slice LND \(E\) of
\(\mathbb C[x_1,x_2,x_3,x_4]\) satisfying
\[
\operatorname{ad}_E^2(\partial_{x_i})=0\quad(i\le3),
\qquad \operatorname{ad}_E^3(\partial_{x_4})=0.
\]
Its conclusion is a polynomial three-ring kernel. This check read
[deep-pass-13.md, Section 8](../deep-pass-13.md) and the full subsequent
[rational-rescaling proof](height-nine-rational-rescale-pass.md).
The quadratic power-law branch is already handled by the explicit
shear; the higher branches use rational classification, a
positive-weight contradiction to the slice, and invariant denominator
clearing. The literature comparison does not replace those arguments.

## 2. Exact overlap: Saleeby's Burgers classification

Elias G. Saleeby, *Meromorphic solutions of generalized inviscid Burgers'
equations and a family of quadratic PDEs*, J. Math. Anal. Appl. 425
(2015), 508–519, [DOI](https://doi.org/10.1016/j.jmaa.2014.12.046).
The [author-uploaded original article](https://www.researchgate.net/publication/270961773_Meromorphic_solutions_of_generalized_inviscid_Burgers%27_equations_and_a_family_of_quadratic_PDEs)
was inspected.

Theorem 1(ii), page 510, gives the nonconstant meromorphic solutions on
\(\mathbb C^2\) of
\[
u_x+u u_y=0
\]
as \(u=(y+A)/(x+B)\), with complex constants \(A,B\). The printed
clause omits the additional, evident constant solutions. For the
project equation \(r\sigma_b+\sigma\sigma_a=0\), set
\(x=b/r\), \(y=a\). This matches the nonzero-slope formula
\[
\sigma=\frac{\alpha a+\beta}{\alpha b/r+\gamma};
\]
constant solutions give the zero-slope case.

An inspection concern affects use of the source proof: page 511
equates coprimality of bivariate polynomials with a polynomial Bézout
identity equal to one. Coprimality alone does not imply that assertion,
as \(x,y\) demonstrate. This identifies a proof step needing scrutiny,
not a disproof of the classification. Retain the independent UFD proof.

## 3. Why the parameter-ring proof remains necessary

The project works over \(R=\mathbb C[z_1,z_2]\), not just complex
constant coefficients. Its numerator and denominator lie in
\(R[a,b]\), and the resulting \(\alpha,\beta,\gamma\) belong to
\(R\). The derivation \(E\) need not initially kill this coefficient
ring. A classification over \(\mathbb C^2\) by itself does not justify
the needed global parameter dependence or extension across poles.

The written algebraic argument addresses this directly: reduced
\(\sigma=N/D\) and the Burgers identity give
\(D\mid D_a\), then \(N\mid N_b\), by prime-factor divisibility
with multiplicities. Degree forces \(D_a=N_b=0\), and the remaining
identity is \(N_a=rD_b\). It uses no multivariable unit-ideal claim.

The further assertions \(E(D)=0\), \(D\mid g^{m-2}\), and the
invariance of a common denominator for the induced rational plane
field are action-specific steps. They do not follow from merely
recognizing the rational Burgers formula. Likewise, ruling out the
nonzero-slope branch uses the slice and a positive grading, not a
meromorphic-solution theorem. These distinctions preserve the content
of the proof after acknowledging the older classification statement.

## 4. A nearby analytic extension does not add the missing action step

Feng Lü, *Meromorphic solutions of generalized inviscid Burgers'
equations and related PDES*, Comptes Rendus Mathématique 358 (2020),
1169–1178, published online January 25, 2021,
[original publication](https://comptes-rendus.academie-sciences.fr/mathematique/articles/10.5802/crmath.136/).
The [original article text](https://www.researchgate.net/publication/348753669_Meromorphic_solutions_of_generalized_inviscid_Burgers%27_equations_and_related_PDES)
was inspected.

Its Theorem 9 treats meromorphic solutions on \(\mathbb C^2\) of
\(u_t-Cu^m u_x=Q\), with \(C\ne0\) constant and \(Q\) polynomial.
For \(m=1\), the conclusion allows an implicit rational expression
in \(u\). Remark 10 explicitly notes that this may be the identity
\(u=u\), and does not give a useful classification in that case.
The paper points back to Saleeby for zero forcing. It is not a
coordinate-recognition or algebraic-action descent theorem.

## 5. Search formulations and bounded outcome

The actual search formulations included:

- `"locally nilpotent" "Burgers"`
- `"rational Burgers" polynomial derivation`
- `"locally nilpotent" "commutator" "partial" four`
- `"locally nilpotent" "ad" "quadratic" derivation slice`
- `"locally nilpotent" "inverse Jacobian"`
- `"inviscid Burgers" "rational solutions" classification`
- `"Burgers equation" "rational" "linear fractional"`
- The exact Saleeby and Lü article titles and theorem searches.

No matching mixed-commutator theorem was identified in this small pass.
The earlier [time-degree audit](mixed-time-degree-literature-addendum.md)
records the distinct premises of nice, quasi-nice, and ordinary
quadratic-map results. The published Burgers formula is an actual
overlap at the sublemma level. The coefficient-ring classification and
the polynomial-action descent remain explicitly proved in the project
notes rather than attributed to those analytic papers.

Search results from automated mathematics repositories were not used.
No further broad classification search was undertaken.
