# Bounded comparison with Freudenburg's 2009 sliced derivations

Date: 2026-09-13. Scope: [the pass-21 primitive noninvariant bridge](primitive-noninvariant-bridge-pass21.md),
especially its universal polynomial transformation and physical
rank-three realization.

Conclusion: a definite overlap of problem setting is established, but
the exact family-level priority comparison remains unresolved. The full
example formulas in Freudenburg's 2009 paper were not obtained. Neither
a collision nor a distinction between its examples and the pass-21
family is proved by this audit. Unavailable text supplies no evidence
of novelty.

## 1. What the primary material actually establishes

The reference is Gene Freudenburg, *Derivations of R[X,Y,Z] with a
slice*, Journal of Algebra **322** (2009), 3078–3087,
[DOI 10.1016/j.jalgebra.2008.05.007](https://doi.org/10.1016/j.jalgebra.2008.05.007).
The [publisher's abstract](https://www.sciencedirect.com/science/article/pii/S0021869308002627)
describes the question whether a sliced locally nilpotent derivation
over a polynomial coefficient ring has a two-generated kernel over
that ring. It reports that Theorem 1.1 gives an affine-plane fibration,
and that the last section introduces examples \(\theta_n\) whose
kernel question was unresolved there. These are abstract-level reports,
not a reading of the full theorem hypotheses or the example section.

The author's complete one-page
[2009 CMS conference abstract](https://www2.cms.math.ca/Events/summer09/abs/pdf/aga-gf.pdf)
specifies the coefficient ring \(\mathbb C[a,b]\), a sliced action
on affine five-space, and a method replacing the slice equation by a
lower-degree equation defining an isomorphic fibration. It connects
those examples to Vénéreau polynomials. It prints no derivation or
slice formula, so it cannot identify the present family.

This bounded retrieval checked the publisher landing page and PDF
routes, the author's institutional page, exact-title manuscript
searches, and the OpenAlex location record. The latter listed only
the publisher PDF. That PDF returned HTTP 403 here. The public Elsevier
metadata endpoint confirmed the article and an open-archive flag, but
returned no full text; its full-text view required an API key. OpenAlex's
content download also required a key. No credentials, access-control
workaround, purchase, account creation, or author contact was used.
These are access observations on this date, not a claim that no lawful
public or library copy exists.

## 2. Exact algebraic comparison target

Use \(S=\mathbb C[f,h]\) for the coefficient ring, to avoid
confusing it with the physical three-variable ring. The pass-21
universal calculation concerns
\[
\mathcal E\in\operatorname{LND}_S S[x,r,t],\qquad
\mathcal E(r)=ah,\quad
\mathcal E(x)=2ar,\quad
\mathcal E(t)=1+qr,
\qquad 0\ne a,\quad ac=q^2,
\tag{1}
\]
where \(a,q,c\in S\). This is a triangular derivation in the
order \(r,x,t\). Its displayed coefficient ideal is the unit ideal:
\[
(1-qr)\mathcal E(t)+\frac{cr}{2}\mathcal E(x)=1.
\tag{2}
\]
The pass-21 note gives the stronger result of an explicit polynomial
coordinate system \((X,\rho,\sigma)\) over \(S\) such that
\(\mathcal E\sigma=1\), \(\mathcal EX=\mathcal E\rho=0\),
and
\[
S[x,r,t]=S[X,\rho,\sigma],\qquad
Xh-\rho^2=xh-r^2.
\tag{3}
\]
Thus this abstract model lies in the problem setting described by
Freudenburg's abstract. The reported affine-plane-fibration conclusion
alone is weaker than (3); it neither supplies these coordinates nor
identifies the 2009 examples with (1).

The missing comparison is concrete. One must read the coefficients
and slices of \(\theta_n\), then exhibit, or rule out by a stated
invariant, a coefficient specialization and polynomial change of
variables giving (1), including the exact divisibility
\(a\mid q^2\). Names, number of parameters, triangular appearance,
and the mere existence of a slice do not settle that calculation.
Specialization could also identify only a proper subfamily, so an
unrestricted equivalence should not be inferred from one example.

## 3. The physical rank-three passage is a separate comparison

For the actual pass-21 family,
\[
R=\mathbb C[x,y,z],\quad f=xz-y^2,\quad
r=x^3+yf^n,\quad
h=zf^{2n}+2x^2yf^n+x^5,
\]
and
\[
D=-\operatorname{Jac}(f,h,\cdot),\qquad
E=D+(1+qr)\partial_t,
\quad n\ge2,\quad a=f^n,\quad q=f^\ell J(f,h),
\quad \lceil n/2\rceil\le\ell<n,
\quad J(0,h)\ne0.
\tag{4}
\]
There are two distinct operations after the universal polynomial
calculation. First impose the invariant relation
\[
xh-r^2=f^{2n+1}
\]
to obtain the surface cylinder
\(\mathscr A_0[t]\), where
\(\mathscr A_0=S[x,r]/(xh-r^2-f^{2n+1})\).
Then pass from this proper subring to \(R[t]\) by adjoining the
divided expressions defining \(y\) and \(z\). The pass-21 proof
checks the thickened curve and both polynomial inverse maps at this
second step. This is not substitution of three freely independent
variables into another three-variable polynomial algebra over \(S\).

Indeed \(\dim R[t]=4\), whereas \(\dim S[x,r,t]=5\), and
the displayed nonzero relation already holds in \(R[t]\). Thus
the assertion that the physical ring is itself \(S^{[3]}\), needed
for a direct application of a theorem with that hypothesis, is false.
Even a proven prior identity for the universal model would still
require comparison of the relation and the physical modification
centers. Conversely, the dimension distinction does not exclude an
existing theorem that expressly passes through such quotients and
modifications.

The other two pass-21 conclusions depend on that original embedded
base, not just on the abstract isomorphism type of \(\ker E\):
\[
1+qr\notin\ker D+D(R),\qquad
\min_{Es=1}\deg_t(s)=2.
\tag{5}
\]
The proof uses the exact second image ideal
\(D^2(R)\cap\ker D=f^{2n}h\mathbb C[f,h]\).
An abstract translation conjugacy does not by itself establish or
exclude these fixed-base statements. A full collision comparison
must track the distinguished subalgebra \(R\) and added variable
\(t\), rather than only the existence of polynomial kernel coordinates.

## 4. Present credit and next action

The local-slice base and the affine-modification lifting principle
retain their existing Freudenburg, Dasgupta–Gaifullin, and
Kaliman–Zaidenberg attribution in the linked notes. This audit does
not alter that attribution or supply priority for the new conjunction
of formulas and fixed-base conclusions.

The precise next priority task is to obtain and inspect the full 2009
example section and its proofs, preferably from an existing lawful
library copy or author manuscript, then perform the substitution test
in Section 2 and the additional compatibility checks in Section 3.
Until then the appropriate label is **family-level priority unresolved**,
not “new,” “not covered,” or “already implied.” No main registry was
changed by this bounded audit.
