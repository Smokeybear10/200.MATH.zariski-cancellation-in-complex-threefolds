# Priority comparison for the all-coefficient slice criterion

The family-level priority comparison remains unresolved. Primary statements
confirm substantial inherited material, but this bounded comparison does not
establish that the complete classification is either already published or
new. In particular, the inaccessible example section of Freudenburg's 2009
paper remains an explicit comparison gap. Checked on 2026-09-13.

## Exact comparison target

The [current theorem](radical-noninvariant-pass22.md) concerns, for every
n >= 1,

\[
f=xz-y^2,\quad r=x^3+yf^n,\quad
h=zf^{2n}+2x^2yf^n+x^5,\quad D=-\operatorname{Jac}(f,h,\cdot).
\]

For every q in C[f,h], it classifies E=D+(1+qr) partial_t on
C[x,y,z,t]. The separate statements to compare are:

1. A slice exists exactly when f divides q, with polynomial kernel in
   every positive case.
2. A slice of t-degree at most one exists exactly when f^n divides q;
   degree at most two exists exactly when f^n divides q^2.
3. For nonzero q, f^n | q^3 and f^n not dividing q^2 give exact minimum
   degree three. Beyond that region, only finite construction and
   existence, not an exact minimum-degree formula, are claimed.

The negative direction in the first statement is an all-degree orbit
obstruction. Neither a degree-two calculation nor the general slice
theorem alone establishes it. The distinguished original subalgebra and
added variable t matter for the degree statements.

## Definite prior coverage

Dasgupta and Gaifullin, Theorem 5.7 and its proof, contain the entire
canonical base through the substitution m=2 and F(t_1,t_2)=t_1^2.
Their displayed local slice, invariant relation, irreducibility, and
rank-three conclusion are the base input, up to the chosen sign of the
Jacobian derivation. The statement is about derivations on k[x,y,z],
not the asserted all-q classification on the four-variable extension.
This distinction is a statement comparison, not a claim about every
possible consequence of their paper.[^1]

Freudenburg's *Canonical factorization* Section 8.2 is exactly the n=1
base, with its F,G,R corresponding to f,h,r. Theorem 8.3 and the
subsequent list explicitly give the first degree modules, including
A+Ar+Ax+Axr+Ax^2. Those formulas must retain their published credit.
Section 9 supplies a different explicit sliced extension on a
five-variable polynomial ring, with added coefficient 1+f+f^2 for an
invariant f. It invokes the 2009 fibration result and poses its own
relative kernel question. That displayed coefficient is invariant under
the original derivation, whereas E^2(t)=qf^n h here. Thus it is not a
literal instance of the displayed noninvariant classification. This does
not rule out conjugacy or a more elaborate specialization.[^2]

The physical coordinate proof also retains the previously audited
Kaliman-Zaidenberg full-ideal affine-modification framework. Its exact
application and inherited cylinder constructions are documented in the
[pass-20 priority reduction](priority-boundary-pass20.md). A general
lifting principle should not be presented as newly proved merely because
the current curve conditions have been checked explicitly.

## Closest general translation theorem and the missing hypothesis

Dubouloz, Finston, and Jaradat prove that a proper locally triangulable
additive action on a Zariski locally trivial affine-three-space bundle
over a Noetherian normal characteristic-zero base has an affine-plane-bundle
quotient away from codimension at least two. Their Dedekind-base
corollaries give global translations for proper triangular actions on
relative affine three-space, in particular on ordinary affine
four-space. I read the main statement and these corollaries in the
published paper, pages 1962-1963.[^3]

These statements do not directly supply the current physical coordinate
construction. The abstract ring C[f,h][x,r,t] is a polynomial ring in
five variables, while in the physical ring the extra equation
xh-r^2=f^(2n+1) already holds. Passing through that equation and the
weighted overring is additional work. Nor is the physical map to
Spec C[f] an affine-three-space bundle: its zero fiber is
Spec C[x,y,z,t]/(xz-y^2), which is singular. Therefore f cannot simply
be declared its required ambient base coordinate. An alternative
coordinate and a proper triangular presentation could conceivably
provide another proof, but they must be constructed, not inferred from
these theorem statements. The present polynomial coordinate proof
provides such a presentation only after its substantive work is done.

## Freudenburg 2009: what is and is not accessible

The publisher abstract reports an affine-plane-fibration theorem for
kernels of sliced R-derivations on R[X,Y,Z], where R is a polynomial
coefficient ring over a characteristic-zero field. It also reports a family theta_n whose relative
kernel question was unsettled there. The author's one-page CMS abstract
specifies R=C[a,b], relates the examples to Vénéreau polynomials, and
discusses replacing the slice equation by a lower-degree equation with
isomorphic quotient. Neither accessible abstract prints the theta_n
coefficients or provides a fixed-added-variable minimum-degree
classification.[^4][^5]

The fresh bounded retrieval repeated exact-title, DOI, theta_n, author,
and institutional manuscript searches. The ordinary publisher PDF route
returned HTTP 403. No full 2009 article was obtained, and no access-control
workaround, paid access, credential use, or external contact was attempted.
The more detailed earlier access record remains in the
[pass-21 comparison](priority-comparison-pass21.md).

Accordingly, no claim is made that the 2009 example family is disjoint
from, equivalent to, or sufficient to prove the current theorem. The
specific outstanding task is to read those coefficients and proofs in a
lawfully available full copy, test exact parameter substitutions into
the universal model, and then check the invariant equation and physical
modification compatibility. A match only in the abstract five-variable
model would not by itself settle those last checks or the t-degree
claims.

## Search boundary and disposition

The targeted searches combined the exact 2009 title and DOI with
Freudenburg, rank three, canonical local slice, noninvariant extension,
radical, 1+qr, and nilpotent modulo; they also checked the closest
triangular-action result and the cited canonical example. The primary
passages actually read for this comparison were Dasgupta-Gaifullin's
family and Theorem 5.7; Freudenburg's Section 8.2 formulas, Theorem 8.3,
degree-module list, and Section 9 extension; the 2014 main theorem and
corollaries; and the two 2009 abstracts. Search snippets and tertiary
pages were not used as proof evidence.

This was not a comprehensive MathSciNet, zbMATH, thesis, or citation-tree
audit. Unsuccessful formula searches establish no absence theorem.
The appropriate packet label is therefore **priority unresolved**, with
the above inherited results explicitly credited and the complete working
proof presented for expert checking, not as a cleared novelty claim.
No registry or earlier proof was modified.

## Sources

[^1]: N. Dasgupta and S. A. Gaifullin, [*On locally nilpotent derivations of polynomial algebra in three variables*](https://arxiv.org/html/2306.00510v2), Theorem 5.7 and preceding construction; published in *Sbornik: Mathematics* 216(4) (2025), 456-484, [journal record](https://www.mathnet.ru/eng/sm10094).

[^2]: G. Freudenburg, [*Canonical factorization of the quotient morphism for a Ga-action on an affine variety*](https://arxiv.org/pdf/1602.08786), author preprint, Sections 8.2 and 9, particularly Theorem 8.3 and Question 9.3.

[^3]: A. Dubouloz, D. R. Finston, and I. Jaradat, [*Proper triangular Ga-actions on A4 are translations*](https://msp.org/ant/2014/8-8/ant-v8-n8-p06-s.pdf), *Algebra & Number Theory* 8(8) (2014), 1959-1984, main theorem and corollaries, pages 1962-1963.

[^4]: G. Freudenburg, [*Derivations of R[X,Y,Z] with a slice*](https://www.sciencedirect.com/science/article/pii/S0021869308002627), *Journal of Algebra* 322 (2009), 3078-3087, [DOI](https://doi.org/10.1016/j.jalgebra.2008.05.007). Publisher abstract only in this comparison; full example section unavailable.

[^5]: G. Freudenburg, [*Additive group actions associated to derivations of R[X,Y,Z] with a slice*](https://www2.cms.math.ca/Events/summer09/abs/pdf/aga-gf.pdf), complete one-page author abstract, CMS Summer Meeting 2009.
