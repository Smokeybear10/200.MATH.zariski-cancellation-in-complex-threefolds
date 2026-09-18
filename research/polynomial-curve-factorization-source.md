# Polynomial factorization through a curve

Yes. If
\[
R=\mathbb C[h_1,\ldots,h_m,\ell]
\subset B=\mathbb C[x_1,x_2,x_3,x_4],
\qquad \operatorname{trdeg}_{\mathbb C}R=1,
\]
then there is a nonconstant polynomial \(a\in B\) and univariate
polynomials \(f_1,\ldots,f_m,g\in\mathbb C[T]\) such that
\[
h_i=f_i(a),\qquad \ell=g(a).
\tag{1}
\]
The parameter \(a\) is genuinely polynomial. No ambient-coordinate
conclusion about \(a\) follows just from this statement.

## 1. An exact primary-source statement

[De Bondt, *Rational maps \(H\) for which \(K(tH)\) has transcendence
degree 2 over \(K\)*, Corollary 3.2, PDF pp. 20–21](https://arxiv.org/pdf/1501.06046)
states the following for an arbitrary field \(K\). Let \(R\) be a
\(K\)-subalgebra of \(K[x_1,\ldots,x_n]\), with fraction field \(L\)
of transcendence degree one. There exists \(p\in K[x]\) with
\(L=K(p)\); moreover,
\[
R\subseteq K[p]=K(p)\cap K[x],
\]
and \(K[p]\) is the integral closure of \(R\) in \(L\).
Neither finite generation nor normality of \(R\) is a stated
hypothesis. The proof and the polynomial-intersection Lemma 3.3
are present immediately below the corollary.

Taking \(K=\mathbb C\) and \(R\) as above gives (1) directly.
The paper appeared in *Journal of Pure and Applied Algebra* 222
(2018), 3595–3620,
[DOI 10.1016/j.jpaa.2018.01.003](https://doi.org/10.1016/j.jpaa.2018.01.003).

## 2. Independent normalization proof over \(\mathbb C\)

This proof uses finite normalization of an affine curve, the classical
one-variable Lüroth theorem, and the description of a smooth rational
affine curve as an open subset of \(\mathbb P^1\). It does not assume
that a rational parameter is polynomial.

Let \(L=\operatorname{Frac}R\), and let \(\overline R\) denote the
integral closure of \(R\) in \(L\).

First, \(\overline R\subseteq B\). Indeed, an element of \(\overline R\)
belongs to \(L\subseteq\operatorname{Frac}B\) and satisfies a monic
equation with coefficients in \(R\subseteq B\). Normality of the
polynomial ring \(B\) places that element in \(B\). Since \(R\) is a
finitely generated complex curve algebra, \(\overline R\) is also
finitely generated.

Choose an affine line in \(\mathbb A^4\) on which some nonconstant
member of \(R\) stays nonconstant. Such a line exists: if a polynomial
has highest homogeneous part \(q_d\neq0\), choose a vector \(v\)
with \(q_d(v)\neq0\) and restrict to \(x=tv\).
Restriction induces
\[
\rho:\overline R\longrightarrow\mathbb C[t].
\]
This map is injective. Otherwise its nonzero prime kernel in the
one-dimensional domain \(\overline R\) would make the image
zero-dimensional. A zero-dimensional finitely generated complex
domain is \(\mathbb C\), contradicting the selected nonconstant
restriction.

Consequently \(L\) embeds in \(\mathbb C(t)\). Classical Lüroth gives
\(L\cong\mathbb C(u)\). Thus the smooth projective completion of
\(\operatorname{Spec}\overline R\) is \(\mathbb P^1\), and
\[
\operatorname{Spec}\overline R\cong\mathbb P^1\setminus S
\]
for a finite, nonempty set \(S\). The set is nonempty because this
is a positive-dimensional affine curve.

Now \(\overline R^\times=\mathbb C^\times\): a unit and its inverse
both lie in \(B\), whose only units are nonzero constants.
If \(S\) contained two distinct points \(P,Q\), a rational function
with divisor \(P-Q\) on \(\mathbb P^1\) would restrict to a
nonconstant unit on its complement. Hence \(S\) consists of one
point.

It follows that \(\overline R=\mathbb C[a]\) for an element
\(a\in\overline R\subseteq B\). Since every \(h_i\) and \(\ell\)
belongs to \(R\), formula (1) follows. This proof also identifies
the generator inside the original ambient polynomial ring, not
merely in an abstractly isomorphic field.

## 3. Consequences and limits needed in the coefficient-curve branch

All components must be included in the same transcendence-degree-one
algebra. Knowing that the \(h_i\) alone have one-dimensional image
does not permit adding an unrelated \(\ell\).

If a derivation \(D\) annihilates every generator of \(R\), then it
also annihilates \(a\). Choose a nonconstant generator \(f(a)\).
In characteristic zero,
\[
0=D(f(a))=f'(a)D(a),
\]
where \(f'(a)\neq0\). Since \(B\) is a domain, \(D(a)=0\).
This applies simultaneously to any collection of derivations
annihilating \(R\). Local nilpotence is not needed for this deduction.

Containment \(R\subseteq\mathbb C[a]\) is not equality in general:
\(\mathbb C[x_1^2,x_1^3]\) is a basic example. Nor is \(a\)
necessarily an ambient coordinate. For example,
\(R=\mathbb C[x_1x_2]\) is already normal, but its generator
\(x_1x_2\) is not a coordinate, as its zero fiber is reducible.
Polynomial factorization therefore licenses polynomial chain rules
and coefficient comparison; coordinate recognition remains a
separate step.

## 4. The Formanek reference and its numbering

[De Bondt, *The strong nilpotency index of a matrix*, proof of
Theorem 4.2](https://arxiv.org/pdf/1203.6615)
explicitly invokes Formanek's Lemma 3 to obtain
\(H_i\in K[p]\) with \(p\in K[x]\).
Its reference is Formanek's
[*Two notes on the Jacobian Conjecture*](https://doi.org/10.1007/BF01210711),
*Archiv der Mathematik* 49 (1987), 286–291.

The later rational-maps paper instead attributes the weaker
containment statement to Formanek's Lemma 2. The original Formanek
paper was located on the publisher and author's upload pages, but
the lemma text was not recovered in this bounded pass. The
unambiguous citation for the present argument is therefore the
directly inspected Corollary 3.2 above, not an unverified lemma
number.
