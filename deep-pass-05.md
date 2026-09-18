# Global symmetries, failed shortcuts, and a fiber obstruction

September 12, 2026. Private continuation of the cancellation investigation.

## Executive summary

The full target remains unresolved:

\[
X\times_{\mathbb C}\mathbb A^1\simeq\mathbb A^4
\quad\Longrightarrow\quad X\simeq\mathbb A^3.
\]

This pass moves beyond the fixed derivation classified in
[the preceding report](deep-pass-04.md). It corrects an earlier global claim,
constructs a precise sufficient condition for cancellation, and gives exact
counterexamples to two attempted ways of proving that condition. It also
excludes an infinite family of tempting smooth polynomials from being slice
polynomials by comparing their fibers.

The main change is that a hypothetical cancellation counterexample cannot
be rigid: its coordinate ring must admit a nonzero locally nilpotent
derivation. What remains unproved is that these symmetries can be made strong
enough to produce polynomial coordinates. Nonrigidity alone is insufficient.

The earlier fixed-family theorem survived a fresh full-chain model audit.
This is a working proof with supporting exact checks, not a human-reviewed
result or a proof-assistant certificate. No novelty claim is made for the
global lemmas or explicit examples in this report.

## 1. The ring formulation and the filtration

Write

\[
B=\mathbb C[x_1,x_2,x_3,x_4]=K[s],\qquad E=\partial_s.
\]

Here \(K=\mathcal O(X)\), and the displayed equality is the product
decomposition supplied by the hypothesized isomorphism. It does not assume
that \(K\) is a polynomial ring. The function \(s\) is a slice, meaning
\(E(s)=1\). The question is whether \(K\cong\mathbb C^{[3]}\).

Give \(K\) degree zero and \(s\) degree one. If a nonzero locally nilpotent
derivation \(T\) moves an element of \(K\), its filtration degree \(q\) is
nonnegative. This degree is finite: take the maximum on a finite set of
algebra generators, subtracting the generator's degree. The leading
homogeneous derivation \(\widehat T\) is again locally nilpotent. To see this,
apply successive powers to an element's leading form: unless a leading
coefficient becomes zero, the result is the leading form of the corresponding
power of \(T\). Local nilpotence of \(T\) forces termination.

Homogeneity gives \(\widehat T(s)=h s^{q+1}\) for \(h\in K\). An LND on a
characteristic-zero domain cannot send an element to a nonzero multiple of
itself. Indeed, the degree function associated to the LND is additive on
products, but applying the derivation decreases that degree by one. Therefore
\(\widehat T(s)=0\), and

\[
\widehat T=s^q\delta,\qquad 0\ne\delta\in\operatorname{LND}(K).
\tag{1}
\]

Local nilpotence of \(\delta\) follows from
\(\widehat T^n(a)=s^{nq}\delta^n(a)\) for \(a\in K\).

This is the elementary mechanism behind the known one-variable rigidity
theorem.[^4] Precise primary-source versions and an independent reconstruction
are recorded in [the intrinsic-actions appendix](research/intrinsic-actions-pass.md).

## 2. Correcting the rigidity claim

If an affine characteristic-zero domain \(A\) is rigid, equation (1) shows
that every LND on \(A[s]\) kills \(A\). Since \(\partial_s\) has kernel
\(A\), the intersection of all LND kernels is exactly \(A\):

\[
\operatorname{ML}(A[s])=A.
\]

But the coordinate partials on \(\mathbb C^{[4]}\) have common kernel
\(\mathbb C\). Consequently \(K[s]\cong\mathbb C^{[4]}\) with
\(\dim K=3\) rules out rigid \(K\).

The earlier [global bridge note](research/global-bridge-pass.md) incorrectly
said that no theorem established this consequence. That statement must be
replaced by the stronger, correct restriction: intrinsic nonzero LNDs exist,
but their properness, slices, and adequate independence are not guaranteed.

Do not generalize one-variable rigidity to arbitrarily many added variables.
Dubouloz constructs rigid affine surfaces whose product with an affine plane
is flexible in codimension one.[^1]

## 3. A sufficient global condition

Apply the preceding construction to the four ambient coordinate partials
\(T_i=\partial_{x_i}\).

If some \(T_i\) has negative filtration degree, it kills \(K\). Then
\(K\subseteq\ker T_i\), both have transcendence degree three, and every
element of \(\ker T_i\) is algebraic over \(\operatorname{Frac}K\).
Differentiating its minimal polynomial with \(E\), using characteristic zero,
shows that it lies in \(\ker E=K\). Hence
\(K=\ker T_i\cong\mathbb C^{[3]}\).

Otherwise every leading symbol has the form
\(s^{q_i}\delta_i\) in (1). Since the original partials commute, their
highest-degree commutator vanishes. As all \(\delta_i\) kill \(s\), this says
\([\delta_i,\delta_j]=0\).

If three of the \(\delta_i\) are independent over \(\operatorname{Frac}K\),
their commuting flows define a \(\mathbb G_a^3\)-action with a
three-dimensional orbit on \(X\). This orbit is open. Orbits of a unipotent
algebraic group on an affine variety are closed, so this orbit is all of the
irreducible variety \(X\). Its stabilizer has dimension zero and is trivial
over \(\mathbb C\), since an additive group has no nontrivial finite algebraic
subgroups. Thus \(X\cong\mathbb G_a^3\cong\mathbb A^3\). The closed-orbit
fact is standard and is explicitly recalled by Arzhantsev.[^2]

This proves a sufficient condition, not a reduction to a condition already
known to hold. In particular, the independence assumption cannot be omitted.

## 4. Exact rank-loss counterexample

Even for the ordinary polynomial ring \(K=\mathbb C[a,b,c]\), choose the
ambient coordinates

\[
x_1=a,\quad x_2=b+as,\quad x_3=c+bs,\quad x_4=s.
\]

Their inverse is polynomial. Expressed in \((a,b,c,s)\), the partials are

\[
\begin{aligned}
T_1&=\partial_a-s\partial_b+s^2\partial_c,\\
T_2&=\partial_b-s\partial_c,\\
T_3&=\partial_c,\\
T_4&=\partial_s-a\partial_b+(as-b)\partial_c.
\end{aligned}
\]

The four fields are independent and commute, but their leading symbols are
\(s^2\partial_c,-s\partial_c,\partial_c,as\partial_c\). All induced
derivations of \(K\) span just one direction over its fraction field.

One can repair this particular example using
\(T_1+sT_2=\partial_a\) and \(T_2+sT_3=\partial_b\). However, this uses the
special fact that \(s\) is a common invariant of \(T_1,T_2,T_3\). The same
operation has not been justified for an arbitrary slice polynomial.

The independently implemented
[filtration checker](verify_global_filtration.py) verifies both inverse maps,
the coordinate-partial pairing, commutators, leading terms, rank loss, and
the special recovery formulas exactly.

There is a stronger control. Replace \(x_2\) by \(b+a^2s\), retaining
\(x_1=a,x_3=c+bs,x_4=s\). The leading term of the first partial is now
\(2as^2\partial_c\); the other partials have lower filtration degree.
The four constant linear combinations
\(U_1=T_1\), \(U_2=T_1+T_2\), \(U_3=T_1+T_3\),
\(U_4=T_1+T_4\) are again a coordinate-partial basis, since the mixing
matrix is invertible. All four top symbols are now \(2as^2\partial_c\).
Thus all induced intrinsic fields equal \(2a\partial_c\), vanish along
\(a=0\), and have no slice. Even a unit plinth ideal cannot be inferred
from the ambient coordinate translations by this leading-term operation.

## 5. Lower coefficients and commutators are not safe replacements

On \(\mathbb C[a,b,c,s]\), use the ambient coordinate pair

\[
u=a+s^2,\qquad v=s+u^2
\]

and retain \(b,c\). Its inverse is
\(s=v-u^2\), \(a=u-(v-u^2)^2\). The coordinate partial with respect to
\(u\) is

\[
T=(1+4as+4s^3)\partial_a-2(a+s^2)\partial_s.
\]

Its leading symbol is \(4s^3\partial_a\). Its lower horizontal
\(s\)-coefficient is \(4a\partial_a\), which is not locally nilpotent:
its \(n\)-th iterate on \(a\) equals \(4^n a\).

Moreover,

\[
[E,T]=(4a+12s^2)\partial_a-4s\partial_s
\]

is not locally nilpotent, because its successive iterates on \(s\) are
\((-4)^n s\). Thus taking a lower coefficient or a first commutator with
\(E\) is not a general mechanism for obtaining the missing intrinsic LNDs.
The [obstruction appendix](research/filtration-obstruction-pass.md) develops
these controls and checks their exact coordinate origins.

Nor is projection to \(s=0\) safe if \(T\) does not preserve the ideal
\((s)\). For the coordinate pair \(u=s+a^2\), \(v=a+u^2\), the partial
\(T=\partial_u\) satisfies
\(T(a)=-2(s+a^2)\) and \(T(s)=1+4a(s+a^2)\). Its projected horizontal
derivation on \(K\) is \(-2a^2\partial_a\), which is not locally nilpotent.
By contrast, if an LND actually kills \(s\), it descends to each quotient
\(B/(s-\lambda)\) as an LND. The missing ideal-invariance hypothesis is
precisely what makes the proposed general projection invalid.

## 6. Low-degree gates and a smooth family excluded by its fibers

There is a positive low-degree result: every slice polynomial of total degree
at most two is a coordinate. A quadratic \(f=\tfrac12x^TAx+b^Tx+c\)
without critical points has \(b\notin\operatorname{im}A\). Symmetry of
\(A\) supplies \(v\in\ker A\) with \(b^Tv\ne0\), so
\(\partial_v f\) is a nonzero constant. In linear coordinates with axis
\(v\), replacing that coordinate by \(f\) is triangular and invertible.

For a genuine cubic without critical points, its leading projective cubic
surface must be singular. Otherwise, homogenizing the four gradient
equations gives four quadrics in \(\mathbb P^4\) with a common zero by
the height theorem, but no common zero at infinity. Dehomogenizing then
produces a critical point, a contradiction. The
[stable-coordinate appendix](research/stable-coordinate-pass.md) supplies
the complete proofs and a constant-direction sufficient test. It also
shows why Kuroda's stable Newton-polytope obstruction imposes no restriction
on polynomials of degree at most three in four variables. No universal
cubic-coordinate theorem is claimed.

For integers \(m,r,q\ge2\), put

\[
P=x+x^m y+z^r+w^q\in\mathbb C[x,y,z,w].
\]

Every fiber is smooth: if \(x\ne0\), the derivative with respect to \(y\)
is nonzero; if \(x=0\), the derivative with respect to \(x\) equals one.
Nevertheless, \(P\) cannot satisfy \(D(P)=1\) for an LND \(D\).

Here is a direct proof. Use compactly supported topological Euler
characteristic, which is additive over constructible decompositions and
multiplicative for products and finite unramified covers. The part of a fiber
\(P^{-1}(\lambda)\) with \(x\ne0\) is
\(\mathbb C^*\times\mathbb A^2\), so contributes zero. Its \(x=0\) part is
\(\mathbb A^1\times C_\lambda\), where
\(C_\lambda=\{z^r+w^q=\lambda\}\).

For \(\lambda\ne0\), projection to \(w\) is an unramified degree-\(r\)
cover away from the \(q\) distinct roots of \(w^q=\lambda\). Each exceptional
fiber consists of one point. Therefore

\[
\chi_c(P^{-1}(\lambda))=r(1-q)+q
=1-(r-1)(q-1).
\]

For \(\lambda=0\), the curve has \(\gcd(r,q)\) irreducible branches.
Each branch minus the origin is isomorphic to \(\mathbb C^*\); all branches
meet only at the origin. Consequently
\(\chi_c(P^{-1}(0))=1\).

A slice would make \(\exp(tD)\) identify all fibers algebraically. Their
different Euler characteristics contradict this. The same calculation
excludes \(P\) from becoming a coordinate after any number of polynomial
stabilizations: its nonzero fibers times affine space still have Euler
characteristic different from one.

In particular, the Russell polynomial \(x+x^2y+z^2+w^3\) has fiber Euler
characteristics \(1\) and \(-1\). This does **not** decide whether the
abstract cylinder over its zero fiber is affine four-space. An isomorphism
of one abstract cylinder does not identify every fiber of this particular
polynomial. Further details and source checks are in
[the stable-coordinate appendix](research/stable-coordinate-pass.md).

## 7. Why the torus route does not finish the proof

The product presentation gives a dilation action
\(s\mapsto\lambda s\), fixing \(K\). Its fixed locus is \(X\), and its
invariant ring is \(K\). It is a parabolic one-dimensional torus action in
the terminology of Arzhantsev.[^2]

If this particular action could be linearized, its fixed locus would be a
linear three-space, giving the desired conclusion. Conversely, if
\(K\cong\mathbb C^{[3]}\), its coordinates together with \(s\) linearize the
action immediately. Linearizing this product-type dilation is therefore an
equivalent restatement of this cancellation instance, not an independent
argument.

The relevant complexity is \(4-1=3\). Liendo and Petitjean discuss positive
linearization results for complexity-two actions with a positive-dimensional
fixed locus. Those hypotheses do not cover the action here.[^3] Merely
noticing that its fixed locus has dimension three cannot justify applying
their result.

## 8. Verification and remaining task

The [fresh full-chain audit](research/full-chain-audit.md) reconstructed the
fixed-family proof from its ring presentations through its formal-branch
obstruction and positive coordinates. It found no mathematical defect and
corrected a dependency link. A noncircular argument for the needed primitive
obstruction is now explicit in the preceding report.

The global proof gap is now specific: manufacture enough appropriate
intrinsic additive actions from an arbitrary presentation
\(K[s]\cong\mathbb C^{[4]}\), or find a different route to polynomial
coordinates. Leading symbols guarantee existence but can lose independence;
lower coefficients and naive commutators need not remain LNDs. These failures
are proved negative results, not evidence that cancellation itself fails.

The restricted theorem and the global statements remain private working
mathematics. No expert review, external contact, publication, or submission
has occurred. Exact test totals and commands are recorded in the experiment
manifest; none of the finite tests verifies the universal conjecture.

## Sources

[^1]: Adrien Dubouloz, [*Flexible bundles over rigid affine surfaces*](https://arxiv.org/html/1304.4189v1), introduction and main construction. This is the primary counterexample to extrapolating one-variable rigidity to two added variables.

[^2]: Ivan Arzhantsev, [*Limit points and additive group actions*](https://arxiv.org/html/2102.11330v1), Introduction (closed unipotent orbits), Lemma 1 (parabolic actions), and Theorem 1. Its compatible additive action is along the torus fibers, not a conclusion that the fixed locus is affine space.

[^3]: Alvaro Liendo and Charlie Petitjean, [*Codimension two torus actions on the affine space*](https://arxiv.org/html/2411.14645v1), Introduction and Theorem 1. The complexity-two restriction is essential to the comparison made here.

[^4]: Anthony J. Crachiola and Leonid G. Makar-Limanov, [*An algebraic proof of a cancellation theorem for surfaces*](https://cds.cern.ch/record/905059/files/cer-002575268.pdf), Theorem 3.1; *Journal of Algebra* 320 (2008), 3113–3119, [DOI](https://doi.org/10.1016/j.jalgebra.2008.03.037). The theorem uses exponential maps; the present reconstruction only needs the characteristic-zero LND case. A further primary proof is [Alhajjar, *LND-Filtrations and Semi-Rigid Domains*](https://arxiv.org/html/1501.00445v1), Proposition 3.4. The CERN mirror presented a bot-check page during the main agent's final access attempt; the accessible Alhajjar proof and the derivation above provide separate verification.
