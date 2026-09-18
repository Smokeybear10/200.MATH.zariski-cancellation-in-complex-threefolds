# Targeted source screen: do not import the claimed general ML statements

A targeted literature check found elementary problems in specific
statements of *Cancellation problem via locally nilpotent derivations*,
[arXiv:2512.15590v1](https://arxiv.org/html/2512.15590v1).
The selected passages were read on September16,2026. This is a
statement-level check, not a review of the entire paper or its
noncommutative sections.

The source is not being used as a theorem input in this investigation.
In particular its claimed unrestricted ML-stability statement and
its purported characteristic-zero cancellation counterexample are
not adopted. No claim about authorship, intent or the production
process of the source is made.

## 1. The displayed derivation does not descend for the displayed family

Example1.12 considers the polynomial family
\[
f_n=x+x^n y+z^2+t^3
\]
and the derivation D=x^2 partial_z-2z partial_y. For the asserted
descent to the quotient by f_n, one needs D(f_n) in the ideal (f_n).
Direct differentiation gives
\[
D(f_n)=2z(x^2-x^n).
\tag{1}
\]
For n=3 this is nonzero. It has degree zero in y, whereas f_3
has degree one in y over the domain C[x,z,t]. Every nonzero
polynomial multiple of f_3 has y-degree at least one. Therefore
\[
D(f_3)\notin(f_3).
\tag{2}
\]
The displayed derivation does not induce a derivation of that
quotient. This is an algebraic error in the stated family, not
merely a missing citation. Replacing x^2 by x^n corrects this
particular differentiation, but does not justify other claims.

## 2. The stated surface dichotomy needs additional hypotheses

Theorem2.2 asserts a dichotomy for affine two-dimensional UFDs
over an algebraically closed field of characteristic zero. As
stated, it excludes intermediate Makar-Limanov invariant rings.
Consider instead
\[
R=\mathbb C[x,x^{-1},y].
\tag{3}
\]
This is an affine domain, a UFD, and has Krull dimension two.
Every locally nilpotent derivation on a characteristic-zero domain
kills every unit. Indeed its additive degree function satisfies
deg_D(ab)=deg_D(a)+deg_D(b) for nonzero a,b; applying this to
xx^{-1}=1 forces both degrees to be zero. Thus every such
derivation on R kills C[x,x^{-1}].

The ordinary derivation partial_y is locally nilpotent on R
and its kernel is precisely C[x,x^{-1}]. Consequently
\[
\operatorname{ML}(R)=\mathbb C[x,x^{-1}],
\tag{4}
\]
which is neither R nor C. Also R is not the complex polynomial
two-ring, since it has a nonconstant unit. This contradicts the
theorem with its displayed hypotheses. No cancellation assertion
about R is needed for this counterexample.

## 3. Consequence for the research workflow

The same source's introduction says characteristic-zero affine
cancellation in dimension at least three remains open, while its
Example2.6 asserts a characteristic-zero threefold counterexample.
That internal inconsistency is an additional reason to check any
purported cancellation shortcut against original statements.

The two exact errors above are sufficient to exclude this source
as support for the proposed general commutative arguments. They
do not prove that every statement in the paper is false. They do
not establish or refute the actual cancellation target, nor affect
the primary theorems independently used in the working proofs.

No external comment, report, message or contact was made. This
private note records why a search result was not promoted into
mathematical evidence. It is not a novelty audit or a publishable
new result.
