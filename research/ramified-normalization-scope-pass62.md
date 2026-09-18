# Local monomial parameters and the limits of unit normalization

Exact monomial parameters need not be global coordinates of the
invariant plane. Positive weighted Euler homogeneity recovers their
rational invariant field inside the original local fraction field,
even when the parameters generate a proper subfield. This gives a
valid local extension of the square-speed exclusion.

Removing arbitrary unit factors is a different operation. Formal or
étale roots can lie outside the original fraction field. Their
existence alone does not preserve the actual coordinate-field
generation used in the exclusion proof.

## 1. Rational invariants of an actual local weighted Euler field

Let \(C=\mathbb C[a,b]\), let \(R=C_{\mathfrak m}\) at a closed
point, and put \(L=\operatorname{Frac}C\). Suppose \(u,v\in R\)
form a regular system of parameters. They need not generate \(C\),
or even generate \(L\) as a field.

Their Jacobian in the original base coordinates is a unit in \(R\).
The inverse Jacobian therefore defines derivations
\(\partial_u,\partial_v\) preserving \(R\). They agree with the
unique extensions to \(L\) of the corresponding field partials:
\(u,v\) are a transcendence basis and the intervening algebraic
extension is finite separable.

For positive integers \(p,q\), set
\[
\mathscr H=\frac{u}{p}\partial_u+\frac{v}{q}\partial_v,
\qquad d=\gcd(p,q),\qquad
\rho=\frac{v^{q/d}}{u^{p/d}}.
\tag{1}
\]
Then
\[
\boxed{\ker_L\mathscr H=\mathbb C(\rho),\qquad
       R\cap\ker_L\mathscr H=\mathbb C.}
\tag{2}
\]
These conclusions do not assume \(L=\mathbb C(u,v)\).

To prove them, use the coefficient-compatible identification
\(\widehat R=\mathbb C[[u,v]]\). It follows from the regular-parameter
power-series change theorem.[^parameters] The map from \(R\) to
this completion is injective, as can also be checked from the
finite ordinary order of a nonzero rational local germ.

Multiply \(\mathscr H\) by \(pq/d\). The resulting derivation has
positive coprime integer weights
\[
w(u)=q/d,\qquad w(v)=p/d.
\]
For a nonzero formal series, let its weighted order be the least
weight of a monomial with nonzero coefficient. Its initial form is
a finite weighted-homogeneous polynomial. Initial forms multiply
without cancellation in the polynomial domain, so order extends
additively to the fraction field of the completion.

If \(z=P/Q\in L^*\) and \(\mathscr Hz=0\), initial-form comparison
in the quotient rule gives \(w(P)=w(Q)=n\). Write their initial
polynomials as \(P_0(u,v),Q_0(u,v)\). The quotient \(P_0/Q_0\)
also has weight zero, and
\[
\frac P Q-\frac{P_0}{Q_0}
=\frac{P Q_0-P_0Q}{Q Q_0}
\tag{3}
\]
is either zero or has strictly positive weighted order. It is
still killed by \(\mathscr H\). A nonzero invariant rational
element has order zero by the same quotient-rule comparison.
Thus (3) vanishes exactly.

Finally, a quotient of two weighted-homogeneous polynomials of
the same weight belongs to \(\mathbb C(\rho)\). Indeed, two
monomials of equal weight have exponent difference an integer
multiple of \((p/d,-q/d)\). Factoring one monomial from each
polynomial reduces their quotient to a rational function of
\(\rho\). This proves the first equality in (2); the reverse
inclusion is immediate. A regular series of weight zero contains
only its constant term, proving the second equality.

The same argument for a regular eigenfunction yields
\[
F\in R,\quad \mathscr HF=\lambda F
\quad\Longrightarrow\quad
F=\sum_{i/p+j/q=\lambda}c_{ij}u^iv^j,\qquad c_{ij}\in\mathbb C.
\tag{4}
\]
The sum is finite because the weights are positive. If no such
nonnegative exponents exist, \(F=0\). This is an exact identity,
not an approximation of the germ by its leading term.

## 2. A local extension of the exact square-speed theorem

Retain all the actual frame, Schur determinant, and original
complex coordinate-field generation hypotheses of
[the square-speed theorem](square-speed-schur-generation-pass61.md).
It suffices that, at one closed invariant-base point,
\[
u,v\in R\text{ are regular parameters},\qquad
f=u^2,\quad g=v^2.
\tag{5}
\]
The conclusion is still exclusion of those actual data. No
assumption \(L=\mathbb C(u,v)\) is needed.

Here are the precise replacements for the global-coordinate uses
in that proof. Equation (4) makes every actual acceleration
\(h_i\in R\) a homogeneous binary quartic in \(u,v\). With
\(r=v/u\), (2) gives \(\ker_L\mathscr H=\mathbb C(r)\), and
every rational weight-one potential has
\[
k_i=u^2 d_i(r),\qquad d_i(r)\in\mathbb C(r).
\tag{6}
\]
All zero-weight Hessian and gradient coefficients are consequently
in that same rational field. The full determinant alignment, the
three odd-coefficient ranks, and the exact quadratic formulas of
pass61 are unchanged.

In its rank-two case, \(\mathscr HQ_1\ne0\) proves that \(Q_1\)
is transcendental over \(\mathbb C(r,X,Y)\): the derivation kills
that field and must kill any element algebraic over it in
characteristic zero. Thus \(K=\mathbb C(Q_1,X,Y)\) is still the
correct independent coefficient field. The two pole orders still
give \([K(r):K(Q_2)]\ge4\). But \(r\in L\) is actual, so original
coordinate-field generation gives exactly
\[
K(Q_2)\subseteq K(r)\subseteq L(X,Y)=K(Q_2),
\tag{7}
\]
the same contradiction.

In the lower odd-rank cases, the constant-coordinate conclusions
use \(B_R\cap L=R\) followed by the regular equality in (2).
When every varying term vanishes, actual generation gives
\(B_R=R[X,Y]\), and the original arbitrary slice contradicts the
proper speed ideal \((u^2,v^2)R\). No new affine-slice premise is
introduced.

All even quadratic shears and constant linear changes of good
outputs used here have complex coefficients in the original bad
coordinates. They remain genuine global coordinate changes. The
argument does not replace them by formal ambient coordinates.

For example,
\[
u=a+a^2,\qquad v=b
\tag{8}
\]
are regular parameters at the origin, but
\([\,\mathbb C(a,b):\mathbb C(u,v)\,]=2\): the polynomial
\(T^2+T-u\) has nonsquare discriminant \(1+4u\).
Nevertheless the local extension just proved applies to exact
speeds \((a+a^2)^2,b^2\). A proper parameter subfield is therefore
not, by itself, a surviving obstruction.

Also \(u=a,\ v=(1+a)b\) are local parameters with
\(L=\mathbb C(u,v)\) and \(b=v/(1+u)\), although the global
polynomial subring \(\mathbb C[u,v]\) is proper. This is another
harmless base reparametrization covered by (5).

## 3. What arbitrary unit factors actually permit

For this paragraph translate the original base coordinates so that
\(\mathfrak m=(a,b)\). Suppose that in this local ring
\[
f=a^p U,\qquad g=b^q V,\qquad U,V\in R^*.
\tag{9}
\]
In the completion one can choose roots of the nonzero complex
constant terms and then use the formal binomial series to obtain
\(U^{1/p}\) and \(V^{1/q}\). The parameters
\[
\widetilde u=aU^{1/p},\qquad
\widetilde v=bV^{1/q}
\tag{10}
\]
have invertible linear part, so they give a formal coordinate
change and make the speeds exact monomials.

Algebraically, adjoining roots of \(T^p-U\) and \(S^q-V\) gives
a finite free étale cover: the defining polynomials are monic,
the roots are units, and their derivatives are units in
characteristic zero.[^etale] Choosing points over the original
closed point gives the corresponding local root rings. This
operation need not leave the fraction field unchanged.

A decisive elementary example is
\[
R=\mathbb C[a,b]_{(a,b)},\qquad
f=a^2(1+a),\qquad g=b^2.
\tag{11}
\]
Its initial speed pair is \(a^2,b^2\), and the formal coordinates
\(\widetilde u=a\sqrt{1+a},\widetilde v=b\) normalize it.
But \(f\) is not a square in \(L=\mathbb C(a,b)\): its valuation
at the irreducible polynomial \(a+1\) is one. In particular it
has no square root in \(R\). This obstruction persists although
\(a+1\) is a unit at the chosen closed point.

Even a constant invertible mixing of these two speeds cannot
produce two squares in \(L\). If \(\alpha\ne0\), the polynomial
\(\alpha f+\beta g\) has total degree three and hence is not a
polynomial square. A polynomial that is a rational square in
the fraction field of the UFD \(\mathbb C[a,b]\) is already a
polynomial square. Thus the square members of this pencil lie
only in the one-dimensional span of \(g\).

The root cover \(R[w]/(w^2-1-a)\) in this example is genuinely
quadratic at the level of fraction fields, despite being étale
over this local ring. After any such proper field extension
\(L'/L\), the old four coordinate functions still generate
\(L(X,Y)\) over \(\mathbb C\), not \(L'(X,Y)\). The equality
required at the final step of (7) is not transported merely by
base change.

This example is a base-germ and field-normalization control. It
does not realize the actual sliced full-frame hypotheses and
does not show that unit-twisted square speeds can survive them.
A further argument forcing descent of the needed root ratio or
other coefficients would be a separate theorem.

## 4. Changes of the actual bad coordinates

A constant transformation \((X',Y')^{\mathsf t}=M(X,Y)^{\mathsf t}\),
with \(M\in\operatorname{GL}_2(\mathbb C)\), is legitimate. It
sends the speed column to \(M(f,g)^{\mathsf t}\); the true bad
partials transform by the inverse constant matrix. Their
adjoint bounds and independence are preserved, as are the ranks
of their bad-coordinate projections and the original coordinate
field. Thus the local square conclusion also applies when such
a constant transformation puts the speeds in (5).

Multiplication by a nonconstant invariant local unit is not the
same operation. For instance, even with the sliced \(E=\partial_X\)
on \(\mathbb C[a,b,X,Y]_{1+a}\), replacing \(X\) by \((1+a)X\)
has the true local dual field
\[
T=\partial_a-\frac{X}{1+a}\partial_X.
\tag{12}
\]
It satisfies \(T((1+a)X)=0\), but is not locally nilpotent on
that localization:
\[
T^n((1+a)^{-1})=(-1)^n n!(1+a)^{-n-1}\ne0.
\]
This does not prove failure of every particular adjoint identity.
It shows why local coordinate expressions cannot simply be
declared a new global polynomial coordinate-partial frame.

## 5. Exact remaining boundary

The rational weighted-Euler lemma is valid for every pair of
positive integer weights in actual regular parameters. The
specific exclusion proved here is the local extension of the
already established square theorem. No unproved all-exponent
classification is included.

Formal monomialization with units, equality of initial ideals,
and étale root extraction do not alone preserve the generation
step. Conversely, lack of global polynomial coordinates or a
proper parameter subfield does not obstruct the local proof
when the parameters themselves belong to the actual ring.
No general cancellation conclusion, actual ramified counterexample,
or historical novelty claim is made.

## Sources

[^parameters]: The Stacks Project,
[Lemma 15.40.2, Tag 07NM](https://stacks.math.columbia.edu/tag/07NM),
part (1), statement and complete proof. It permits the prescribed
regular-parameter change in the already existing power-series
completion. The rational weighted initial-form argument above is
proved directly.

[^etale]: The Stacks Project,
[Definition 10.144.1, Tag 00UB](https://stacks.math.columbia.edu/tag/00UB)
and [Section 59.26, Tag 03PA](https://stacks.math.columbia.edu/tag/03PA),
Definition 59.26.3 and its following complete proof that standard
étale algebras are étale. The proof was read directly, including
its finite-free and separable-fiber argument. Root extraction is
used here only to describe the permissible extension, not to
identify it with the original field.
