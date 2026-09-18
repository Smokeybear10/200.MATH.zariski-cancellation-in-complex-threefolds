# The exact linear-invariant source gate over a characteristic-zero field

The terminal-quartic proof needs only the following established
statement: a nonzero nice derivation of a polynomial three-ring
over a characteristic-zero field fixes a nonzero linear form.
The required field is \(\mathbb C(w)\), not just \(\mathbb C\).
This note records two source routes and proves the elementary
field-transfer step for the second route. No originality is claimed
for this historical result or its field transfer.

## 1. The directly applicable statement

Dasgupta and Gupta, Theorem 3.1(i), states the linear-invariant
conclusion for every characteristic-zero field \(K\) and every
nonzero LND \(D\) of \(K[X,Y,Z]\) with
\(D^2X=D^2Y=D^2Z=0\).[^dg]
Its separate part (iii) imposes irreducibility for a stronger
normal-form conclusion. That premise is not present in part (i).

The paper explicitly attributes Theorem 3.1 to Wang,
Proposition 4.6.[^wang] The theorem statement was read directly
in the retained Dasgupta--Gupta text. That paper does not give
a new proof of its Theorem 3.1. Attempts to retrieve Wang's
publisher article and PDF returned HTTP 403, so a fresh read
of Wang's complete proof is not claimed.

## 2. An accessible proof route over the complex numbers

De Bondt's Corollary 5.6(i) gives a complex linear relation among
the three components of any three-dimensional quasi-translation.
Corollary 5.8 states the stronger Wang normal form, but that
stronger form is unnecessary here.[^bondt]

The relevant accessible proof chain was read in the retained text:

1. Proposition 1.3 and Remark 1.4 identify nice derivations with
   quasi-translations. If \(H_i=Dx_i\) and \(D H_i=0\),
   their flow is \(x\mapsto x+tH\).
2. Proposition 5.1 homogenizes a quasi-translation in dimension
   three to a homogeneous one in dimension four.
3. Theorem 5.2 bounds the latter's Jacobian rank by two, unless
   its components already span a single constant direction.
4. Theorem 5.3, with its proved Lemma 5.4, bounds the linear
   span by two in the rank-two case.
5. Corollary 5.6 specializes the homogenization to recover the
   linear-dependence conclusion in dimension three.

A constant coefficient vector already has a linear relation,
so no positive-degree argument is needed for that boundary case.
This source route is a reading of the author's algebraic proof,
not a formal verification or a fresh independent proof of every
standard algebraic-geometry fact that proof cites.

## 3. Descent of the linear relation to any characteristic-zero field

Let \(K\) be any characteristic-zero field, and let
\(D\) be a \(K\)-derivation of \(K[x_1,x_2,x_3]\) with
\(D^2x_i=0\) for every \(i\). Put \(H_i=Dx_i\).
All coefficients of the three finite polynomials \(H_i\)
belong to a subfield \(K_0\subset K\) finitely generated
over \(\mathbb Q\).

The same polynomial formulas define a \(K_0\)-derivation
\(D_0\), and the identities \(D_0H_i=0\) hold over
\(K_0\). They are just coefficient identities among the
same finite polynomials. Local nilpotence follows by the
Leibniz rule from the second-iterate identities on the generators.

There is an embedding \(K_0\hookrightarrow\mathbb C\).
To construct one, choose a finite transcendence basis over
\(\mathbb Q\), send it to algebraically independent complex
numbers, and extend the embedding across the finite algebraic
extension using algebraic closedness of \(\mathbb C\).
The base-changed nice derivation therefore satisfies the
complex theorem from Section 2.

Let \(\mathcal M\) be the finite union of monomials occurring
in the \(H_i\), and let \(C_H\) be their coefficient matrix,
with one row for each monomial and three columns. Complex linear
dependence says
\[
\operatorname{rank}_{\mathbb C} C_H\le2.
\tag{1}
\]
If fewer than three rows occur, the corresponding rank bound
over \(K_0\) is immediate. Otherwise every three-by-three
minor is zero after the injective embedding. Each such minor
was an element of \(K_0\), so it was already zero there.
Thus \(C_H\) has a nonzero kernel vector
\((c_1,c_2,c_3)\in K_0^3\), and
\[
c_1H_1+c_2H_2+c_3H_3=0,
\qquad D(c_1x_1+c_2x_2+c_3x_3)=0.
\tag{2}
\]
The displayed linear form is nonzero because the generators
are algebraically independent and the coefficient vector is
nonzero. Extension from \(K_0\) to \(K\) proves precisely
the required field version.

This argument does not embed the entire possibly large field
\(K\) into \(\mathbb C\). Only a finitely generated
coefficient field is embedded, and the relation is then
descended by finite matrix rank. In particular it applies
without treating \(w\) as a complex constant when
\(K=\mathbb C(w)\).

## 4. Application and limits

In the [terminal proof](terminal-quartic-recognition-pass71.md),
the polynomial nice derivation is
\(T=(U/3)\partial_a+N\partial_b+g\partial_z\).
It fixes \(w\) and is nonzero because \(Tz=g\ne0\).
Apply the field theorem to \(K=\mathbb C(w)\), absorb
the constant factor \(1/3\), and clear denominators in
\(\mathbb C[w]\). This gives precisely the original-ring
relation used by the leading-speed argument.

Neither route supplies a global slice for \(T\). Neither
identifies the kernel of the original sliced derivation \(E\).
That endpoint is supplied by the separate polynomial shears
and the rational two-direction recognition theorem, with
their actual original-ring hypotheses checked independently.

## Sources

[^dg]: Nikhilesh Dasgupta and Neena Gupta, [*Nice derivations over principal ideal domains*](https://arxiv.org/pdf/1701.03635v1), arXiv:1701.03635v1, January 13, 2017, Theorem 3.1(i), PDF p. 5. Retained text: [dg-nice-1701.03635v1.txt](../tmp/pdfs/dg-nice-1701.03635v1.txt).

[^wang]: Zhiqing Wang, [*Homogenization of locally nilpotent derivations and an application to k[X,Y,Z]*](https://doi.org/10.1016/j.jpaa.2004.08.006), Journal of Pure and Applied Algebra 196 (2005), 323--337. Proposition 4.6 is attributed by Dasgupta--Gupta; the complete original proof was not retrieved in this pass.

[^bondt]: Michiel de Bondt, [*Quasi-translations and singular Hessians*](https://arxiv.org/pdf/1501.05168v1), arXiv:1501.05168v1, January 21, 2015. Proposition 1.3 and Remark 1.4, PDF pp. 4--5; Proposition 4.1, p. 12; Proposition 5.1, pp. 14--15; Theorem 5.2, pp. 15--16; Theorem 5.3 and Lemma 5.4, pp. 16--19; Corollary 5.6, pp. 19--20; Corollary 5.8, p. 21. Retained text: [bondt-1501.05168v1.txt](../tmp/pdfs/bondt-1501.05168v1.txt). The listed linear-dependence proof chain was read in full; no claim of full-paper reconstruction is made.
