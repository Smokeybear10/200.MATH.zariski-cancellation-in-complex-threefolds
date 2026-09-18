# Statement-level literature check for the double-bracket criterion

This bounded search did not locate a published statement identical to

\[
D\in\operatorname{LND}\mathbb C[x_1,x_2,x_3,x_4],
\qquad [D,[D,\partial_{x_i}]]=0\quad(1\leq i\leq4)
\quad\Longrightarrow\quad
\ker D\text{ contains an ambient coordinate}.
\tag{1}
\]

This is a search result, not a novelty or openness claim. In particular,
the statement in (1) does not assume a slice. Recognition of a polynomial
kernel from a slice is a subsequent application, not part of the
published hypotheses checked below.

The nearest precise primary-source statements are the following.

## 1. Lie algebras consisting entirely of locally nilpotent derivations

[Petravchuk and Sysak, *On Lie Algebras Consisting of Locally Nilpotent
Derivations*, Theorem 2.5, printed p. 1059](https://jolt.centre-mersenne.org/item/10.5802/jolt.982.pdf),
proves that a finite-dimensional Lie subalgebra of derivations of an
integral domain over an algebraically closed characteristic-zero field
is nilpotent if every member is locally nilpotent. Theorem 3.11,
printed p. 1067, simultaneously triangularizes a Lie subalgebra
consisting entirely of LNDs on the polynomial plane.

Neither statement is (1). Local nilpotence of generators does not
supply the all-members hypothesis. The abelian Lie algebra spanned by
\(D\) and \(W_i=[D,\partial_{x_i}]\) does satisfy that hypothesis, but
its nilpotence is already known from the double-bracket calculation.
The triangularization theorem is two-dimensional.

## 2. Polynomial flows and coordinate frames

[Van den Essen, *Locally finite and locally nilpotent derivations with
applications to polynomial flows and polynomial morphisms*, author-uploaded
original paper, pp. 861 and 865](https://www.researchgate.net/publication/238870234_Locally_finite_and_locally_nilpotent_derivations_with_applications_to_polynomial_flows_and_polynomial_morphisms)
uses “polynomial flow” for polynomial dependence on the initial point.
The introduction recalls the Coomes-Zurkowski equivalence with local
finiteness of the associated derivation. This does not bound the flow's
degree in its group parameter.

Lemma 3.6 and Corollary 3.7 give a relevant exact frame criterion:
if a polynomial map \(F\) has constant nonzero Jacobian determinant,
then \(F\) is an automorphism exactly when all derivations dual to
the differentials \(dF_i\) are locally nilpotent. This recognizes a
specified full coordinate frame, not an invariant coordinate for
one LND. The paper's polynomial-flow classification algorithm is planar.

For (1), the conjugated partial is actually linear in the parameter:
\[
e^{tD}\partial_{x_i}e^{-tD}
=\partial_{x_i}+tW_i.
\]
Calling this a quadratic flow or a quadratic polynomial vector field
would conflate different degree conditions.

## 3. Commuting LNDs in three variables

[Maubach, *The Commuting Derivations Conjecture*, Theorem 3.6](https://www.math.ru.nl/~maubach/Papers/The_Commuting_Dervations.pdf)
states that two commuting LNDs of \(\mathbb C[X,Y,Z]\), linearly
independent over that polynomial ring, have common kernel
\(\mathbb C[g]\) with \(g\) an ambient coordinate.

This is an exact ingredient for the three-variable reductions of the
height-eight argument. It neither concerns four variables nor asserts
that the first brackets of one derivation provide two independent
directions. The dependent-bracket cases require separate arguments.

## 4. Quasi-translations and homogeneous rank two

[De Bondt, *Quasi-translations and singular Hessians*, Proposition 1.3,
Proposition 5.1, Theorems 5.3 and 5.5](https://arxiv.org/pdf/1501.05168)
provides the closest structural results used in the proof: the
quasi-translation identity \(JH\,H=0\), preservation of that identity
under homogenization with an added coordinate, the homogeneous
Jacobian-rank-two image-span bound \(n-2\), and a normal form for
nonhomogeneous Jacobian-rank-one quasi-translations.

The Riccati relation \(D(J)=J^2\), by itself, is not the
quasi-translation identity. In the remaining square-zero rank-two
case, the separate image-cone argument is what keeps homogenization
at rank two in dimension five. Applying Theorem 5.3 after that argument
is a consequence assembled in this workspace, not the literal statement
of a published double-bracket theorem.

## Coverage and limits

The bounded search covered the exact double-commutator condition and
nearby terms involving Riccati Jacobians, commutators with coordinate
partials, conjugated translation frames, and low-degree polynomial
flows. Only original papers or author-uploaded original texts were
used for mathematical claims. No author was contacted.

The companion [height-eight literature note](height-eight-literature-pass.md)
also records the precise limits of strong-nilpotence, ordinary-quadratic,
and nice-derivation theorems. These hypotheses must not be replaced by
same-point Jacobian nilpotence, a bound on the flow parameter degree,
or a slice. The search supplies relevant published ingredients and
premise checks, but does not establish priority for (1).
