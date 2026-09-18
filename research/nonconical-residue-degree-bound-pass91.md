# The relative degree bounds every generic divisor residue extension

In the actual nonconical frame, a whole generic divisor fiber is a
polynomial line over a finite extension of the base residue field.
The degree of that extension, multiplied by the degree of any surviving
relative generator, is at most the generic relative plane degree.
Consequently the extension degree is at most three. This is a bound
on the remaining obstruction, not an assertion that the extension is
trivial or that cancellation is proved.

## 1. Actual input

Retain the actual nonconical constant-acceleration hypotheses of
[quadratic-potential90](nonconical-quadratic-potential-pass90.md),
the exact degree and generic-embedding conclusions of
[cubic-relation90](nonconical-cubic-relation-pass90.md), and the
[whole-divisor noncollapse theorem90](nonconical-cyclic-fiber-omission-pass90.md).
Write
\[
\begin{gathered}
S=\mathbb C[s_1,s_2]\subset A,\qquad
R=S[A_1,A_2]\subset A=R[c],\qquad A_\Omega=R_\Omega,\\
K=\operatorname{Frac}S,\qquad A_K=K[v]=K[A_1,A_2],\\
R=S[T_1,T_2]/(F_0),\qquad
1\le d=\deg_{T_1,T_2}F_0\le3.
\end{gathered}
\tag{1}
\]
The ring A is a smooth affine UFD with an actual polynomial cylinder.
The invariant inclusion S is factorially closed and faithfully flat.
Every irreducible element p of S remains prime in A. These are
inherited actual-ring properties, not assumptions on an arbitrary
plane equation.

The exact primitive Jacobian field constructed in
[global-Jacobian91](nonconical-global-jacobian-field-pass91.md) is a nonzero
S-LND N on A with kernel S and coefficient gcd one. For such a prime p,
put
\[
\begin{gathered}
D=S_{(p)},\qquad k=\operatorname{Frac}(S/(p)),\qquad
C=A_D/pA_D,\\
C\text{ is a nonzero one-dimensional affine }k\text{-domain},\qquad
\overline N\ne0,\qquad
\operatorname{trdeg}_k k[\overline A_1,\overline A_2]=1.
\end{gathered}
\tag{2}
\]
Primitivity gives the nonzero derivation on this whole fiber; the
stronger general whole-scheme nonvanishing statement is already
proved in [primitive-fiber54](primitive-fiber-nonvanishing-pass54.md).
The final assertion in (2) is the separate actual-frame theorem90.

## 2. The curve field and its constants

A nonzero locally nilpotent derivation on a one-dimensional affine
domain in characteristic zero has a polynomial-line description
over its constant field. Here is the full elementary argument needed
for C, so no geometric integrality is tacitly assumed.

Choose a local slice a with \(\overline N^2a=0\) and
\(b=\overline N a\ne0\). The local slice expansion gives
\(C_b=(\ker\overline N)_b[a/b]\). Its kernel has transcendence
degree zero over k. Every nonzero element of that kernel is algebraic
over k and has its inverse as a polynomial in itself with coefficients
in k. The kernel is therefore a field, denoted k', and b is already
a unit in C. Thus
\[
C=k'[t],\qquad \overline N(t)=1,\qquad [k':k]<\infty.
\tag{3}
\]
The finite extension follows without a finite-generation assertion
about a general invariant ring: evaluation at t=0 identifies k' with
a quotient of the finitely generated k-algebra C. Zariski's lemma
then applies. Equivalently, k' is the algebraic-constant subfield of
the one-variable function field \(\operatorname{Frac}C\).

## 3. Restriction to a Gauss valuation

Choose \(U\in\{A_1,A_2\}\) with \(\overline U\) transcendental
over k. Such a choice exists by (2). The exact generic plane
embedding used in cubic-relation90 gives
\[
1\le n=\deg_v U\le d,\qquad
[\operatorname{Frac}A:K(U)]=[K(v):K(U)]=n.
\tag{4}
\]
The degree bound here is for the actual polynomial parametrization
with \(K[A_1,A_2]=K[v]\), not an arbitrary rational parametrization.

Let V be the DVR \(A_{(pA)}\), with valuation \(\nu\), normalized
by \(\nu(p)=1\). Its residue field is \(\operatorname{Frac}C\).
Every element of \(S\setminus(p)\) is a unit in V, and factorial
closure shows that the restriction of \(\nu\) to K is the ordinary
p-adic valuation on D.

For a nonzero polynomial \(g(T)=\sum g_iT^i\in K[T]\), scale by
a power of p until the smallest coefficient valuation is zero.
Reduction then gives a nonzero polynomial over k. It cannot vanish
at the transcendental \(\overline U\). Consequently
\[
\nu(g(U))=\min_i\nu(g_i),\qquad
\text{the residue field of }V\cap K(U)\text{ is }k(\overline U).
\tag{5}
\]
For the second statement, express a rational function as a quotient
of two polynomials and scale both. Valuation-zero functions reduce
to rational functions in \(\overline U\); all such rational
functions occur. This also proves that p remains a uniformizer of
the restricted valuation. No finiteness or normality statement for
R is involved.

## 4. An elementary residue-dimension inequality

Take any finite collection of elements of \(\operatorname{Frac}C\)
linearly independent over \(k(\overline U)\). Lift them to V, with
nonzero residues. Their lifts are linearly independent over K(U).
Indeed, otherwise scale the coefficients in a nontrivial dependence
by a power of p so they all have nonnegative valuation and at least
one has valuation zero. Reducing the dependence in the residue
field gives a nontrivial dependence over \(k(\overline U)\), by
(5), a contradiction.

The K(U)-dimension in (4) is n. Hence every such collection of
residues has size at most n, proving finiteness and the bound
\[
\boxed{\quad
[\operatorname{Frac}C:k(\overline U)]
 =[k':k]\,\deg_t\overline U
 \le n\le d\le3.
\quad}
\tag{6}
\]
The equality follows from the tower
\(k(\overline U)\subset k'(\overline U)\subset k'(t)\):
the first degree is \([k':k]\), since \(\overline U\) is
transcendental over k', and the second is the degree of the
nonconstant polynomial \(\overline U\in k'[t]\).
The proof is the residue-independence form of the usual valuation
degree inequality, written out here in the precise rings needed.

## 5. Consequences and limits

Every generic divisor constant extension has degree one, two or
three. A degree-three extension forces every chosen surviving
relative generator to have degree one over k' and generic degree
three. A degree-two extension also forces its surviving generator
to have degree one over k', although its generic degree can be
two or three. These deductions follow from the integer product
in (6); no geometric descent is being substituted for it.

If a surviving U already has generic degree one, then (6) gives
\(k'=k\) and \(C=k[\overline U]\). One can also prove
\(A_D=D[U]\) directly: every member of a finite generating set of
A lies in \(K[U]\), and a coefficient pole would, after minimal
denominator clearing, give a nonzero polynomial over k vanishing
at \(\overline U\). Thus all coefficients lie in D. This is a
local recognition conclusion only for that specified surviving
generic coordinate.

The argument does not say that such a degree-one generator survives
at every p, that \(k'=k\) always, that \(R_D\to A_D\) is finite,
or that the smaller relative ring has a prime p-fiber. A quadratic
constant extension already occurs in the retained Weitzenbock
control, which is polynomial as an absolute algebra but has no
section for its specified invariant inclusion. The new bound
does not exclude that mechanism in the remaining actual frame.

## Proof and source scope

Root supplied the valuation restriction and independent-residue
proof; General independently reconstructed the outline before this
note was saved. The exact degree input and whole-fiber noncollapse
are proved in the linked pass90 notes. The primitive field and its
extension are addressed separately in the linked pass91 note.
The foundational quotient geometry uses Kaliman--Saveliev,
[*C+-actions on contractible threefolds*](https://www.math.miami.edu/~kaliman/library/KaSa.michigan.2004.quotient.pdf),
Lemma 2.1, Theorem 2.7 and Corollary 2.8, with the exact cylinder
application written in [intrinsic-quotient](intrinsic-quotient-surface-pass.md).
No new classification theorem, numerical test, formal verification,
human expert review or novelty claim is part of this argument.
