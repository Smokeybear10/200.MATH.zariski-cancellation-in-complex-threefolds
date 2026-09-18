# Divergence zero over a nonreduced base

A relative-plane recognition theorem cannot currently
remove the residual nilpotent acceleration. Its hypotheses include
exactly a divergence condition that is still unproved in the relevant
quotient coordinates. Ambient zero divergence and quotient relative
zero divergence are different assertions.

## 1. The primary statement and its scope

Berson, van den Essen and Maubach's April 1999 report defines B(R)
for a commutative Q-algebra R: an R-linear locally nilpotent derivation
on R[X,Y], with zero divergence and unit coefficient ideal, has a
slice and invariant algebra R[P(D)]. Theorem 3.7 proves B(R) for
arbitrary R, including nonreduced rings. The proof reduces to a
Noetherian coefficient algebra and patches through products of ideals;
nilpotents are not simply discarded. The domain case appears in
Theorems 3.3 and 3.4. [1]

The entire eight-page author-hosted report was read. This is a
statement-level applicability check, not a complete comparison with
all related literature or a historical novelty conclusion. The
[source record](../tmp/pdfs/berson-essen-maubach-divergence-pass82-source.md)
retains the report version and local hashes.

## 2. The exact gate in the current action

Use the actual rank-one hypotheses and notation of the
[speed-quotient proof](rank-one-speed-quotient-pass82.md). In particular
the quotient retains nilpotents and is the actual polynomial line
over its invariant subring:
\[
C=B/I=R[z],\qquad \overline E=\overline b(z)\partial_z,
\qquad \overline b\in C^*,\qquad
\overline q=\overline b\,\partial_z\overline b.
\tag{1}
\]
Its relative divergence is therefore partial_z bar(b), not the full
ambient divergence of E. Since bar(b) is a unit, the exact equivalence is
\[
\operatorname{div}_R(\overline E)=0
\quad\Longleftrightarrow\quad \overline q=0
\quad\Longleftrightarrow\quad q\in I.
\tag{2}
\]
Adding a new invariant polynomial variable w would provide a formal
relative plane R[z,w], with the same coefficient ideal and divergence.
It would not establish the missing equality in (2), and it would not
identify the original invariant threefold as a polynomial ring.

The source theorem is consequently not a way to assume (2) for free.
Even after checking a genuine relative-plane presentation, its
zero-divergence premise must still be verified in those coordinates.
In particular, changing the coefficient ring from the ground field to
a possibly nonreduced quotient does not preserve the domain argument
about units of polynomial rings.

## 3. An explicit control for the distinction

Over R=C[epsilon]/(epsilon squared), consider
\[
\delta=(1+\varepsilon z)\partial_z,\qquad
s=z-\frac{\varepsilon}{2}z^2,
\qquad z=s+\frac{\varepsilon}{2}s^2.
\tag{3}
\]
The two inverse orders are polynomial identities, delta(s)=1,
and delta is conjugate to partial_s. Nevertheless its relative
divergence in z is epsilon, which is nonzero. Its coefficient is a
unit. On R[z,w] with delta(w)=0 it still has a global slice and a
unit coefficient ideal, but does not meet the zero-divergence premise.
This is the quotient control from the divisorial note, not an actual
four-variable domain action or a cancellation counterexample.

For the original action, the ambient determinant identity instead
proves the valid additional restriction q to the fourth power lies in
I. It does not establish (2). The next mathematical task must exploit
further original-coordinate or ideal-embedding constraints, or supply
an actual counterexample to membership. Reapplying the relative-plane
theorem without its divergence hypothesis would be circular.

## Sources

1. Joost Berson, Arno van den Essen and Stefan Maubach.
   [Derivations having divergence zero on R[X,Y]](https://www.math.ru.nl/~maubach/Papers/DerivHavingDivZero.pdf).
   University of Nijmegen Report 9918, April 1999, Section 3,
   especially property B(R) and Theorem 3.7. The report version is
   the inspected primary source; later publication metadata was not
   independently verified in this check.
