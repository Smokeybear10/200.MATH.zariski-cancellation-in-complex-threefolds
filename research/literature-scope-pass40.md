# Source gates for the cubic-column closures

The restricted proofs combine new deductions from the supplied frame
with established recognition theorems. The external theorems below
retain their published hypotheses. None asserts that an arbitrary
sliced action on a polynomial four-ring has the required frame.
This is a statement-level dependency audit, not a certification that
the restricted formulation is novel.

## 1. Slice and three-variable recognition

Dasgupta and Gaifullin's version 2 explicitly states the slice theorem
as Theorem 2.5, Miyanishi's polynomial three-variable kernel theorem
as Theorem 2.8, and the two-variable triangularization theorem as
Theorem 2.7.[^1] Their complete statements were directly checked.
The degree-five constant-factor and degree-six proofs first construct
a global polynomial three-ring with an inherited slice. They then
apply these known results in that ring. No corresponding conclusion
is drawn by substituting a localized three-ring.

The same source's Proposition 2.14 states the coordinate conclusion
for two commuting non-equivalent nonzero LNDs of a polynomial
three-ring. Maubach's primary paper proves the complex-field version
as Theorem 3.6.[^2] Its Proposition 3.5 and the short final proof were
read directly as well. Polynomial independence in the present proof
implies distinct kernels: two derivations annihilating the same
transcendence-degree-two field are fractionally dependent on the
remaining one-variable function field.

## 2. Nice derivations and relative coordinate descent

Dasgupta and Gupta's Theorem 3.6 applies over a PID, requires an
irreducible nice derivation, and gives its elementary form after a
linear change over that PID.[^3] The root bridge supplies the invariant
ambient linear coordinate, divides by the coefficient gcd, and checks
that this division preserves both local nilpotence and commutation.
The theorem therefore recognizes the auxiliary kernel. Its allowed
noncomaximal coefficient pair prevents an automatic global section.

The same paper's Theorem 2.6 recalls Hamann's relative cancellation:
if an algebra becomes a polynomial two-ring over a fixed base ring
containing Q after adjoining one variable, it is a polynomial one-ring over
that base. In the two-output argument the base is exactly C[p],
and p is proved to belong to the original coordinate plane before
the theorem is applied. This is not the unresolved threefold
cancellation assertion in another notation.

These papers were already present in earlier project notes. Their
application to the new corrected field is the change in this pass;
the source theorems themselves are not new discoveries.

## 3. The final four-variable gate

Bhatwadekar, Gupta and Lokhande's Theorem 3.5 requires a nonzero
LND of a polynomial four-ring, an invariant ambient coordinate,
and a regular kernel.[^4] Its entire statement and short final proof
were directly reread. The two-output argument obtains the actual
ambient coordinate first. Regularity follows from the original
polynomial-cylinder presentation. A coordinate of an abstract
auxiliary ring would not be enough.

## 4. Limits of the comparison

Searches on rational quasi-translations, commuting sliced derivations,
and nice derivations were followed to the primary papers above.
The recent version of the image-ideal paper arXiv:2302.13787 concerns
its stated relative two-variable setting; only its abstract was used
as a screening lead, not as a proof input. A locally-finite-endomorphism
lead did not supply a missing cancellation theorem. Search-result
crawl dates were not treated as publication dates.

The inspected classification statements do not themselves say that
every cubic-column residual has dependent constant directions or
that every sliced four-variable action admits a height-ten frame.
No comprehensive post-proof novelty audit, human expert review,
public announcement, or submission has occurred. The remaining
three-output branch must be treated as an unproved case.

## Sources

[^1]: Nikhilesh Dasgupta and Sergey Gaifullin,
[*On locally nilpotent derivations of polynomial algebra in three variables*](https://arxiv.org/pdf/2306.00510v2),
version 2, Theorems 2.5, 2.7, 2.8 and Proposition 2.14,
PDF pp. 5-7. The underlying classical results are credited there.

[^2]: Stefan Maubach,
[*The Commuting Derivations Conjecture*](https://www.math.ru.nl/~maubach/Papers/The_Commuting_Dervations.pdf),
author manuscript dated October 5, 2001, Proposition 3.5 and Theorem 3.6,
PDF pp. 4-5. The version actually retrieved is retained locally.

[^3]: Nikhilesh Dasgupta and Neena Gupta,
[*Nice derivations over principal ideal domains*](https://arxiv.org/pdf/1701.03635v1),
version 1, 2017, Lemma 2.3, Theorem 2.6, Theorem 3.6 and proof,
Corollary 3.8, PDF pp. 3-8. Theorem 2.6 explicitly credits Hamann.

[^4]: S. M. Bhatwadekar, Neena Gupta and Swapnil A. Lokhande,
[*Some K-theoretic properties of the kernel of a locally nilpotent derivation on k[X1,...,X4]*](https://arxiv.org/pdf/1501.01438v1),
version 1, 2015, Theorem 3.5 and proof, PDF p. 11.
