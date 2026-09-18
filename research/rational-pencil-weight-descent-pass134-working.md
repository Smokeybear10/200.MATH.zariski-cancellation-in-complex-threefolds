# The weight of a rational pencil's generic equation

This elementary algebra lemma concerns the exact coefficient field of a
rational pencil. It does not assert that a geometric construction supplies
that field, or that a rational invariant generator is polynomial.

## 1. Statement and ambient coprimality

Let \(B=\mathbb C[x_1,\ldots,x_n]\), with strictly positive integer
weights on its actual polynomial coordinates. Let \(E\) be a locally
nilpotent derivation, \(A=\ker E\), and suppose
\[
a=p/q\notin\mathbb C,\qquad p,q\in A,\quad q\ne0,
\qquad p,q\text{ have no common nonunit divisor in }A.
\tag{1}
\]
Put \(K=\mathbb C(a)\). In a separate polynomial ring over this
coefficient field, give each formal \(\xi_i\) the weight of \(x_i\),
and all elements of \(K\) weight zero. The evaluation homomorphism is
\[
\operatorname{ev}:K[\xi_1,\ldots,\xi_n]\longrightarrow
\operatorname{Frac}B,\qquad \xi_i\longmapsto x_i.
\tag{2}
\]
If \(F\) generates its kernel, then
\[
\operatorname{wt}F
=\max\{\operatorname{wt}p,\operatorname{wt}q\}.
\tag{3}
\]
In particular both numerator and denominator have weight at most that
of the generic equation. At least one is a nonconstant invariant.

First, the coprimality in (1) is also coprimality in \(B\). Indeed the
kernel of an LND on a characteristic-zero domain is factorially closed:
for nonzero factors, their finite \(E\)-degrees add, since the top
Leibniz term has a nonzero binomial coefficient. Any divisor of a
nonzero invariant therefore belongs to \(A\), as does its complementary
factor. A common irreducible divisor of \(p,q\) in the UFD \(B\) would
thus be a common nonunit divisor in \(A\). Units in either ring are
exactly the nonzero complex constants.

## 2. The exact generic kernel, without deleting the base locus

Use an indeterminate \(T\), independent of the formal coordinates, and
write \(p(\xi),q(\xi)\) for the original polynomials with their variable
names changed. Consider
\[
P(T,\xi)=p(\xi)-Tq(\xi)\in\mathbb C[\xi][T].
\tag{4}
\]
It is primitive as a polynomial in \(T\) over the UFD
\(\mathbb C[\xi]\), and is linear and irreducible over its fraction
field. Gauss's lemma makes \(P\) irreducible in
\(\mathbb C[T,\xi]\), hence prime there.

In fact the map \(\mathbb C[T,\xi]\to\operatorname{Frac}B\), sending
\(T\mapsto p/q\) and \(\xi\mapsto x\), has kernel exactly \((P)\).
To verify this directly, regard an element of the kernel as a polynomial
in \(T\) over \(\mathbb C[\xi]\). Over its fraction field it is divisible
by \(T-p(\xi)/q(\xi)\), and hence by \(P\). Primitivity and Gauss's
lemma give divisibility already in \(\mathbb C[T,\xi]\).

Because \(a\) is nonconstant, it is transcendental over \(\mathbb C\).
No nonzero element of \(\mathbb C[T]\) belongs to this kernel.
Localizing by those elements therefore preserves a proper prime and
gives exactly the kernel in (2), under \(\mathbb C(T)\simeq K\).
In particular \(P\) does not become a unit or split merely because
the coefficient ring was localized to \(\mathbb C(T)\).

There is no hidden assumption that the base locus \(p=q=0\) is empty.
If one instead first describes the pencil on \(q\ne0\), its ideal
contracts to the same ideal: \(q\notin(P)\), and primality gives
\((P):q^\infty=(P)\). Thus deleting that open-set denominator adds no
equation to the generic kernel.

Any two generators of this kernel differ by a unit of
\(K[\xi]\), necessarily an element of \(K^*\). Such multiplication
does not change the coordinate weight. Moreover each coefficient of
\(P\), in the formal coordinate monomial basis, is \(c-Td\) with
\(c,d\in\mathbb C\). This vanishes only when \(c=d=0\).
The coordinate support of \(P\) is therefore the union of the supports
of \(p\) and \(q\), proving (3).

## 3. The coefficient field cannot silently be enlarged

It matters that \(F\) generates the kernel over exactly \(K=\mathbb C(a)\).
A selected component after algebraic extension can have lower weight.
For example take \(E=\partial_u\) on \(\mathbb C[x,y,z,u]\) and
\[
a=x^2/y^2,\quad K=\mathbb C(a),\qquad
P=x^2-Ty^2.
\tag{5}
\]
Over \(K\), this is the irreducible generic equation for the reduced
numerator \(x^2\) and denominator \(y^2\). Over the larger field
\(\mathbb C(x/y)\), write \(\lambda=x/y\). The actual selected
component is \(x-\lambda y\), and
\(P=(x-\lambda y)(x+\lambda y)\) after \(T=\lambda^2\).
With ordinary weights its degree is one, while both original pencil
members have degree two. Using that selected component to bound the
original numerator and denominator would be invalid.

Thus an application to a generic cubic relation must establish its
coefficient field and kernel before applying this lemma. The lemma
itself neither supplies that geometric identification nor proves either
mixed-cubic correction gate. It uses no polynomial Luroth-generator
assertion and no relative algebraic closedness assumption on \(K\).

## Exact-control scope

The separate [rational-pencil controls](rational_pencil_weight_controls_pass134.py)
check a pencil with nonconstant numerator and denominator, coefficient-field
unit scaling, finite division and base-locus identities, and the displayed
algebraic-extension boundary. They do not computationally certify the
universal kernel or irreducibility argument above.
