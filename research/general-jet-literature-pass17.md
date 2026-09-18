# Literature boundary for the full-family finite-jet lift

The relevant construction has clear predecessors: local-slice constructions
of rank-three derivations, finite congruence corrections for Danielewski
surfaces, and explicit cylinder isomorphisms obtained from slices. The
precise theorems inspected here do not directly identify the kernel of
every invariant-coefficient slice extension in the entire
Dasgupta-Gaifullin family with a polynomial three-ring. That is a statement
about the scope of these particular sources, not a finding that the
full-family conclusion is new.

The finite-jet mechanism must not be described as the first use of
nilpotent corrections or finite interpolation in this subject. In
particular, Moser-Jauslin and Poloni's explicit cylinder construction is a
close mathematical predecessor that should be cited in any future note.
The more specific point requiring a statement-level priority check is the
uniform translation theorem for all parameters and invariant coefficients
in Section 1 below.

## 1. Exact statement being compared

Fix \(m\ge2\), \(n\ge1\), and
\(P\in\mathbb C[x,f]\) with \(P(x,0)\notin\mathbb C\).
Write

\[
f=xz-y^m,\qquad r=xP(x,f)+yf^n,\qquad
h=\frac{r^m+f^{mn+1}}x,
\qquad \delta=-\operatorname{Jac}(f,h,\cdot).
\tag{1}
\]

The family theorem and its proof give
\(C=\ker\delta=\mathbb C[f,h]\),
\(\delta r=f^nh\), primitive rank three, and plinth ideal
\(f^nhC\). These are known inputs, credited to
Dasgupta-Gaifullin, Theorem 5.7.[^1]

The [full-family coordinate construction](general-local-slice-lift-pass17.md)
proves that

\[
E=A\delta+B\partial_t,\qquad A,B\in C,
\qquad (A,B)C=C,
\qquad B=1+fhQ(f,h)
\tag{2}
\]

admits polynomial coordinates \((X,Y,Z,s)\) with
\(EX=EY=EZ=0\), \(Es=1\), and \(f=XZ-Y^m\).
A nonzero scalar residue of \(B\) is handled by scaling both
coefficients and the derivation. Necessity of these conditions from an
arbitrary slice is a separate implication supplied by the
[general affine-replacement deduction](general-invariant-affine-pass17.md),
with its stated geometric dependencies.

The correction is a polynomial \(H(X,f)\) determined modulo \(f^n\)
by

\[
b_H=B(f,X^{m-1}H^m),\qquad
H=b_H^{1-m}P(b_H^{-m}X,f).
\tag{3}
\]

The fact \(B\equiv1\pmod f\) makes each inverse power a finite
expression in the nilpotent quotient. The resulting polynomial inverse
works on the entire four-space, including \(f=h=0\). It preserves
the displayed form of \(f\), while changing the polynomial used to
present \(h\). The comparison target is this global statement, not a
generic-fiber isomorphism or an isomorphism after adjoining another
independent variable.

## 2. Local-slice construction is established prior work

Freudenburg introduced the local-slice construction in 1997. Starting
with kernel \(k[f,g]\) and suitable local slice \(r\), it replaces
\(g\) by \(h=\phi(f,r)/g\) and produces another locally nilpotent
Jacobian derivation. Its original examples include the homogeneous
rank-three series of type \((2,4n+1)\), not just the first
\((2,5)\) example.[^2]

The modern statement recalled as Dasgupta-Gaifullin Theorem 2.17 gives
the new derivation, its value on \(r\), and its kernel when irreducible.
Their Theorem 5.7 verifies rank three for (1), including nonhomogeneous
choices. It proves neither a classification of extensions on
\(k^{[4]}\) nor the coordinate conclusion in (2). The introduction
and the proof of the family theorem were inspected, not merely its title.

Thus the proposed result cannot claim discovery of this family or of
the operation that creates it. Its specific mathematical content begins
with the invariant extension and the polynomial inverse.

## 3. The closest finite-jet predecessor: explicit cylinders

Moser-Jauslin and Poloni's Theorem 4.0.1 considers a special Danielewski
surface \(S\) over a line with \(d\ge2\) origins and a surface
\(W=\{xy=F(z)\}\), with \(F\) having \(d\) simple roots.
It constructs an explicit isomorphism
\(S\times\mathbb A^1\simeq W\times\mathbb A^1\).[^3]

Its proof chooses a finite polynomial satisfying congruences of the form

\[
g(x,r_i+xt)\equiv\sigma_i(x)\pmod{x^n}
\]

by Hermite interpolation, making \((u-g(x,z))/x^n\) polynomial and
a slice for an extended LND. Proposition 5.2.1 specializes the method
to classical Danielewski cylinders. These are explicit finite-jet
predecessors, but their conclusions retain a surface cylinder.
Application to (2) would require a compatible global identification
with the prescribed data, including at \(f=h=0\).

## 4. Stable equivalence already uses matrix corrections

For

\[
P_r=x^2y-z^2-xr(z^2),
\]

Moser-Jauslin and Poloni's Theorem 2.5 proves stable polynomial
equivalence of \(P_r,P_s\) in four variables exactly when their
constant terms are both zero or both nonzero. The proof of Theorem 2.5'
uses a two-by-two polynomial change in the \(z,w\) variables and
divisibility modulo \(x^2\) to obtain polynomial inverse maps.[^4]

Poloni's later Lemma 3.4 treats

\[
P_q=(x_1\cdots x_ell)^2y+z^2+
(x_1\cdots x_ell)q(z^2).
\]

It proves that \(P_q\) and \(P_{q(0)}\) become equivalent after
adding one variable. The displayed maps fix all \(x_i\), correct
the remaining variables by a unimodular matrix, and cancel the apparent
denominator using a finite congruence.[^5]

These are precedents for matrix-plus-congruence lifting, not the
kernel conclusion (2). Poloni's integer \(\ell\) counts coordinate
factors; it is not the arbitrary thickening exponent \(n\) in (1).

## 5. The general extension theorem has a different hypothesis

Freudenburg's Theorem 7.6 begins with a fundamental pair \((D,U)\)
on an affine domain, hence an underlying \(SL_2\) structure, and
extends \(D\) by an invariant in the degree-zero part of its kernel.
It describes the extension kernel through weighted degree modules;
over an algebraically closed field its quotient map is surjective only
when that coefficient is a nonzero constant.[^6]

Its Theorem 6.4 places fundamental derivations on polynomial
three-space in linear models of rank at most two. Thus our primitive
rank-three \(\delta\) cannot satisfy this hypothesis. Theorem 6.6
also proves cancellation when the threefold factor has a nontrivial
\(SL_2\)-action. Such an action on the extension kernel is additional
structure, not a consequence of (1)-(2).

## 6. Generalized Danielewski models do not supply automatic descent

The May 2026 primary abstract of El Kahoui, Labtaini and Ouali assumes
an affine factorial domain, an irreducible LND with the freeness
property, affine kernel, and plinth generated by a power of one prime.
It identifies that differential algebra with a generalized Danielewski
model.[^7]

Globally, the plinth \(f^nh\) in (1) contains two distinct prime
factors in \(\mathbb C[f,h]\), so the prime-power hypothesis
fails. Localizing away from one factor changes the problem and does
not prove the needed global compatibility. Freeness is also an input
to the published statement, not its conclusion. Only the primary
abstract and bibliography were accessible; no full-text theorem beyond
that abstract is attributed to this source.

There is a concrete reason to preserve the distinction between relative
and abstract isomorphism. Poloni's Corollary 3.3(1) forces an
isomorphism between Danielewski surfaces \(x^ny=Q(x,z)\),
\(n\ge2\), to send \(x\) to a constant multiple and \(z\)
to a constant affine scaling plus a polynomial in \(x\).[^8]
Applied in [the exact relative chart](danielewski-relative-pass17.md),
this excludes a \(\mathbb C[f,h]\)-linear isomorphism between
the original three-ring and the extension kernel for
\(m=2,P=x^2,B=1+fh,n\ge2\), despite the polynomial coordinates
constructed in this project. The lift must be allowed to change the
presentation of \(h\).

## 7. Citation and priority conclusions

The supported attribution is narrow and useful. The rank-three family
and its plinth belong to prior work. Finite congruences, interpolation,
matrix corrections, and polynomial denominator cancellation also have
explicit precedents. The exact full-family coordinate statement should
be presented as a working deduction with those predecessors cited,
not as an unprecedented technique.

Within the named primary statements above, three additional steps would
be needed to replace the new proof by a citation: a matching global
model for (2), compatibility across \(f=h=0\), and a conclusion
that identifies the quotient kernel itself as a polynomial three-ring.
The source conclusions on surface cylinders or stable hypersurface
equivalence do not supply those steps. This is the precise boundary
established by the comparison, not proof of novelty elsewhere in the
literature.

Coverage was bounded to the original local-slice article, the exact
family theorem, the invariant-extension theorem, explicit Danielewski
cylinder and stable-equivalence constructions, the relevant isomorphism
restriction, and the recent generalized-model abstract. The full-family
note and its inverse were also read. There was no author contact,
purchase, submission, or exhaustive bibliographic-database audit.
Priority remains unestablished, and the full cancellation conjecture
is not resolved by these comparisons.

## Sources

[^1]: Nikhilesh Dasgupta and Sergey Gaifullin, [*On locally nilpotent derivations of polynomial algebra in three variables*](https://www.mathnet.ru/eng/sm10094), *Sbornik: Mathematics* 216(4) (2025), 456-484, Theorems 2.17 and 5.7, with the family definition and proof. The condition \(n\ge1\) is explicit in [arXiv:2306.00510v2](https://arxiv.org/html/2306.00510v2).

[^2]: Gene Freudenburg, [*Local slice constructions in k[X,Y,Z]*](https://ir.library.osaka-u.ac.jp/repo/ouka/all/4752/ojm34_04_02.pdf), *Osaka Journal of Mathematics* 34(4) (1997), 757-767, Sections 2 and 4.1. Original institutional version of record.

[^3]: Lucy Moser-Jauslin and Pierre-Marie Poloni, [*Isomorphisms between cylinders over Danielewski surfaces*](https://arxiv.org/pdf/2002.12202v1), arXiv:2002.12202v1, February 27, 2020, Section 4, Theorem 4.0.1, and Proposition 5.2.1. Exact finite congruences and the resulting slice construction were read.

[^4]: Lucy Moser-Jauslin and Pierre-Marie Poloni, [*Embeddings of a family of Danielewski hypersurfaces and certain C+-actions on C3*](https://numdam.org/item/10.5802/aif.2220.pdf), *Annales de l'Institut Fourier* 56(5) (2006), 1567-1581, Theorem 2.5 and its reformulation and proof in Section 5.

[^5]: Pierre-Marie Poloni, [*A note on the stable equivalence problem*](https://arxiv.org/pdf/1308.2652), Lemma 3.4 and its explicit inverse. Published in [*Journal of the Mathematical Society of Japan* 67(2) (2015), 753-761](https://www.jstage.jst.go.jp/article/jmath/67/2/67_753/_article/-char/en), DOI 10.2969/jmsj/06720753.

[^6]: Gene Freudenburg, [*Actions of SL2(k) on affine k-domains and fundamental pairs*](https://arxiv.org/pdf/2108.12021v2), arXiv:2108.12021v2, June 7, 2022, Theorems 6.4, 6.6, and 7.6. The fundamental-pair and degree-zero hypotheses are essential to the statement audited here.

[^7]: M'hammed El Kahoui, Hatim Labtaini and Mustapha Ouali, [*The Freeness Property for Locally Nilpotent Derivations of Factorial Domains*](https://link.springer.com/article/10.1007/s00031-026-09969-9), *Transformation Groups*, published May 15, 2026, DOI 10.1007/s00031-026-09969-9. Primary abstract only; subscription full text not accessed.

[^8]: Pierre-Marie Poloni, [*Classification(s) of Danielewski hypersurfaces*](https://arxiv.org/pdf/0912.3241v1), arXiv:0912.3241v1, Corollary 3.3(1). Published in *Transformation Groups* 16(2) (2011), 579-597. The exact isomorphism restriction, not an ambient-equivalence substitute, is the input used in the relative obstruction.
