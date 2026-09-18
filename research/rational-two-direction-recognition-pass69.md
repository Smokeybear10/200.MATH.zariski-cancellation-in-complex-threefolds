# Rational two-direction symmetries and original-kernel recognition

A rational two-direction field need not be locally nilpotent on a
localization merely because its second iterates kill the polynomial
coordinates. Nevertheless, a compatible original sliced action permits
a complete alternative: the rational field is either a parallel
translation with an invariant denominator, or a radial field whose
polynomial invariants force the original action to preserve an actual
coordinate plane. Both alternatives recognize the original kernel.

This theorem concerns a supplied rational symmetry and a genuine good
coordinate partial. It does not assert that an arbitrary sliced action
admits either one, and it does not solve unrestricted cancellation.

## 1. Precise original-ring hypotheses

Let
\[
B=\mathbb C[u,v,a,b],\qquad E\in\operatorname{LND}(B),
\qquad E(s_*)=1,\qquad 0\ne g\in\ker E.
\]
All four displayed generators are actual polynomial coordinates.
Put \(\delta=E/g\) on \(\operatorname{Frac}B\). Assume that
\[
\operatorname{ad}_E^2\partial_a=0.
\tag{1}
\]
Suppose \(\beta\in\operatorname{Frac}B\) and
\[
S=\partial_b+\beta\partial_a,\qquad
[\delta,S]=0,\qquad S\beta=0,\qquad
\delta\beta=\kappa\in\mathbb C.
\tag{2}
\]
No local nilpotence of \(S\), invariant denominator of \(\beta\),
or inclusion \(\beta\in B_g\) is assumed.

**Theorem.** Under (1)--(2), \(E\) fixes an actual ambient
coordinate of \(B\), and
\[
\ker E\simeq\mathbb C^{[3]}.
\tag{3}
\]
The original polynomial slice is used essentially below. The statement
does not transfer a slice to the rational field \(S\).

## 2. The original slice forces the inverted factor to be fixed

Equation (2) gives \(S^2u=S^2v=S^2a=S^2b=0\). Consequently every
polynomial in the original generators has a finite sequence of
nonzero \(S\)-iterates, even though its intermediate images may
only be rational functions. This follows directly by repeated use
of the Leibniz rule on a polynomial expression in the generators.
In particular \(\exp(tS)g\) and \(\exp(tS)s_*\) are polynomials
in \(t\) with coefficients in \(\operatorname{Frac}B\).

Commutation and \(\delta s_*=1/g\) give
\[
\exp(tS)(1/g)=\delta\bigl(\exp(tS)s_*\bigr)
\in\operatorname{Frac}(B)[t].
\tag{4}
\]
The formal exponential of a derivation preserves products in the
formal power-series ring. Thus the two polynomial expressions
\(\exp(tS)g\) and \(\exp(tS)(1/g)\) multiply to one.
The only units of \(\operatorname{Frac}(B)[t]\) are its nonzero
constant polynomials. Taking the coefficient of \(t\) proves
\[
Sg=0,\qquad [E,S]=[g\delta,S]=0.
\tag{5}
\]
This is the original-slice unit argument of the
[degree-five reduction](cubic-degree-five-pass40.md), Section 4.
Its first conclusion requires no assumption that the coefficients
of \(S\) have only powers of \(g\) as denominators. It still
does not make \(S\) locally nilpotent on an arbitrary localization.

## 3. Classification of the rational coefficient over the fixed plane

Set \(K=\mathbb C(u,v)\). Write \(\beta=N/D\) in reduced form
over the UFD \(K[a,b]\), with \(D\ne0\). The equation
\(S\beta=0\) is
\[
D^2N_b-ND D_b+ND N_a-N^2D_a=0.
\tag{6}
\]
Reduction modulo \(D\), together with coprimality, gives
\(D\mid D_a\). A nonzero derivative in \(a\) has strictly
smaller \(a\)-degree, so \(D_a=0\), and \(D\in K[b]\).
After division by \(D\), equation (6) becomes
\[
D N_b-ND_b+N N_a=0.
\tag{7}
\]
If \(n=\deg_aN\ge2\), the last summand has degree \(2n-1\)
with nonzero leading coefficient, whereas the first two have
degree at most \(n\). This is impossible. The zero numerator
belongs to the constant alternative directly.

If \(\deg_aN=0\), (7) says \(\beta_b=0\), so \(\beta\in K\).
Otherwise write \(\beta=p(b)a+q(b)\), with \(p,q\in K(b)\)
and \(p\ne0\). The two coefficients in the differential equation
are
\[
p'+p^2=0,\qquad q'+pq=0.
\tag{8}
\]
Hence \((1/p)'=1\) and \((q/p)'=0\). Constants of ordinary
differentiation on \(K(b)\) are precisely \(K\). There are
\(A_0,B_0\in K\) such that
\[
\boxed{\quad \beta\in K\quad\text{or}\quad
\beta=\frac{a+A_0}{b+B_0}.\quad}
\tag{9}
\]
The second expression is an identity in the rational function field.
It is not a claimed polynomial coordinate change over \(\mathbb C[u,v]\).

## 4. Parallel case: the original denominator is invariant

Suppose \(\beta\in K\). Choose coprime
\(N_0,D_0\in\mathbb C[u,v]\), with \(D_0\ne0\), representing
\(\beta=N_0/D_0\). They remain coprime in the polynomial
extension \(B\). For \(\beta=0\), take \(N_0=0,D_0=1\).
By (2), \(E\beta=\kappa g\in B\), so
\[
D_0 E N_0-N_0 E D_0=\kappa gD_0^2.
\tag{10}
\]
Reduction modulo \(D_0\) gives \(D_0\mid E D_0\).
For a polynomial LND in characteristic zero, this implies
\(E D_0=0\): if \(E D_0=H D_0\ne0\), the additive LND
degree of the product contradicts the strict drop in the degree
of a nonzero derivative. Thus
\[
E D_0=S D_0=0,\qquad
S\in\operatorname{LND}(B_{D_0}),\qquad
D_0S(B)\subset B.
\tag{11}
\]
Here local nilpotence is now justified: \(S\) fixes the denominator
and the two actual base coordinates, and is a translation with
coefficients in that localized base ring on the other two.
Equations (1), (5) and (11), together with the original slice,
are exactly the hypotheses of the
[one-good-output recognition lemma](three-output-cubic-closure-pass41.md),
Section 1. That lemma gives (3) and an original invariant coordinate.

## 5. Radial case: polynomial invariants force an actual plane restriction

Suppose the second alternative of (9) holds. In \(K[a,b]\), make
the translations \(a'=a+A_0\), \(b'=b+B_0\). They are valid
polynomial changes over the field \(K\). Since \(S\) kills \(K\),
\[
(b+B_0)S=a'\partial_{a'}+b'\partial_{b'}.
\tag{12}
\]
The right side acts on each homogeneous component of positive
total degree as multiplication by that positive integer.
Consequently its polynomial kernel over \(K\) is \(K\), and
\[
K[a,b]\cap\ker S=K,\qquad B\cap\ker S=\mathbb C[u,v].
\tag{13}
\]
The second equality also uses \(B\cap K=\mathbb C[u,v]\)
in the actual polynomial coordinate ring.

By (5), \(S(Eu)=E(Su)=0\) and \(S(Ev)=0\). Polynomiality of
the original \(E\), followed by (13), gives
\[
E\bigl(\mathbb C[u,v]\bigr)\subseteq\mathbb C[u,v].
\tag{14}
\]
The restriction is an LND because \(E\) is one on \(B\).
If it is zero, \(u\) is an original invariant coordinate.
If it is nonzero, Rentschler's plane theorem supplies a coordinate
\(p\) of the actual plane \(\mathbb C[u,v]\) killed by that
restriction.[^plane] It is therefore an invariant coordinate of
the original \(B\), not just of a field extension.

Finally \(B=(\ker E)[s_*]\) makes the original kernel regular.
The invariant-coordinate regular-kernel theorem of Bhatwadekar,
Gupta and Lokhande gives (3), with the same precise original-ring
endpoint used in Section 1 of the linked recognition lemma.[^regular]
This radial alternative does not use the good-partial hypothesis;
that hypothesis is retained to cover the parallel alternative.

## 6. Boundary control and scope

The rational field \(S=\partial_b+(a/b)\partial_a\) has
\(S^2a=S^2b=0\), yet \(S(b^{-1})=-b^{-2}\) and no positive
iterate of \(b^{-1}\) vanishes. It is the radial alternative,
not an LND on \(B_b\). Taking \(E=\partial_u\), \(g=1\)
and \(s_*=u\) meets the theorem's compatibility assumptions
with \(\kappa=0\), and its conclusion holds through the actual
plane restriction. Thus the proof has not silently upgraded the
rational field to an LND in this alternative.

The theorem is a written conditional deduction. The rational
classification in Section 3 is proved here directly. The slice-unit
argument and complete one-good-output lemma were reread in the
retained working proof chain. The source statements below were
checked at their stated scope; no fresh reconstruction of every
historical source proof is claimed. Independent AI review and
finite coefficient checks, when recorded separately, do not amount
to human expert review or proof-assistant verification.

## Sources

[^plane]: Nikhilesh Dasgupta and Sergey Gaifullin, [*On locally nilpotent derivations of polynomial algebra in three variables*](https://arxiv.org/html/2306.00510v2), arXiv:2306.00510v2, December 9, 2023, Theorem 2.7, stating Rentschler's theorem. The complete statement was directly checked for this argument; it applies here to an actual complex polynomial plane.

[^regular]: S. M. Bhatwadekar, Neena Gupta and Swapnil A. Lokhande, [*Some K-theoretic properties of the kernel of a locally nilpotent derivation on k[X1,...,X4]*](https://arxiv.org/pdf/1501.01438v1), Theorem 3.5. Its precise invariant-coordinate and regular-original-kernel hypotheses, and the retained proof/source audit, are documented in [the one-good-output lemma](three-output-cubic-closure-pass41.md). This argument reuses that source gate; it does not claim a fresh full-paper review.
