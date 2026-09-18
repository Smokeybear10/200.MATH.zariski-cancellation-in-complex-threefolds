# What the quadratic graph theorem closes, and what it does not

Pass64 recognizes the entire supplied **independent-defect, flow-degree-two**
branch. It does not recognize the entire supplied adjoint profile
\((1,1,2,2)\), and it does not produce a recognized frame for an arbitrary
sliced derivation. The remaining supplied-profile obligations include
higher-flow independent defects and the genuinely rationally dependent
defect sector.

This is a read-only dependency audit of the saved proofs, not a new
recognition theorem. The mathematical conclusion of
[the graph theorem](actual-quadratic-graph-cancellation-pass64.md) is taken
with all its written hypotheses and established external inputs. The
shared registry and earlier reports are not edited here.

## 1. Fix the three distinct notions of degree and rank

Throughout this map,
\[
B=\mathbb C[x_1,x_2,x_3,x_4]=A[s_*],\qquad
E(s_*)=1,\quad A=\ker E,\quad T_i=\partial_{x_i}.
\]
The supplied two-quadratic bounds are
\[
\operatorname{ad}_E^2T_1=\operatorname{ad}_E^2T_2=0,
\qquad
\operatorname{ad}_E^3T_3=\operatorname{ad}_E^3T_4=0.
\]
They are upper bounds on the actual adjoint heights. Put
\[
V_i=\operatorname{ad}_E^2T_i\ (i=3,4),\qquad
d=\operatorname{rank}_{\operatorname{Frac}B}[V_3(x)\mid V_4(x)],
\qquad m=\max\{j:E^jx\ne0\}.
\]
Here \(m\) is degree in the flow parameter, not the spatial degree of
the coefficients of \(E\). The defect rank \(d\) is not the coordinate
rank of the individual derivation \(E\), nor the rank of all intrinsic
LNDs of \(A\).

For slice-filtration height, retain
\(H=\sum_i(q_i+1)\) from
[the frame-minimization definition](coordinate-frame-minimization-pass.md#1-a-well-defined-height-and-what-its-minimum-would-mean).
A partial with \(q_i=-1\) already recognizes the kernel. Otherwise
the filtration degrees agree with the corresponding adjoint heights.
The nonnegative adjoint statistic in
[the all-inverse-pairs search](universal-frame-search-pass43.md#1-what-the-previous-minima-do-and-do-not-establish)
is not itself the shifted statistic \(H\).

## 2. The exact chain which pass64 finishes

Assume \(d=2\). The
[six-dimensional companion proof, Sections 2--4](two-quadratic-defects-pass39.md)
gives \(m\le6\), excludes \(m=1\), and proves that when \(m=2\),
\(\operatorname{rank}\operatorname{Jac}(E^2x)=2\). In particular the
highest vector in this degree-two sector cannot be constant.

The complete degree-two recognition chain is:

| Gate | Proven result and evidence |
| --- | --- |
| Bad speeds \(f=Ex_3,g=Ex_4\) have Jacobian rank at most one | An invariant ambient linear coordinate, hence polynomial \(A\), by [pass42, Section 4](two-quadratic-degree-two-pass42.md#4-low-rank-of-the-bad-speeds-produces-an-ambient-coordinate). |
| The bad-speed Jacobian has rank two | The bad projection of the independent defect plane also has rank two, by [pass43, Sections 1--4](bad-projection-rank-closure-pass43.md). The rank-one projection alternative is excluded using the original action. |
| Both ranks are two | The actual good partials give the full generic quadratic graph, a polynomial-in-the-bad-variables Schur inverse, and genuine generic coordinate generation, by [pass44](generic-bad-pair-pass44.md). |
| That full actual graph | [Pass64](actual-quadratic-graph-cancellation-pass64.md) produces either an invariant ambient coordinate or an explicit relative affine slice, and proves \(A\simeq\mathbb C^{[3]}\). |

Thus the composition of the stated theorems proves
\[
\boxed{\ d=2\text{ and }E^3x=0\quad\Longrightarrow\quad
A\simeq\mathbb C^{[3]}\ }
\]
under the original slice and actual adjoint bounds above. This is not
limited to the monomial speed cases, transverse divisors, coprime
speeds, simple common zeros, or the speed/acceleration unit-ideal open.

The last gate requires more than a quadratic presentation. In its
notation it uses all of
\[
C\simeq\mathbb C^{[2]},\quad B\cap\operatorname{Frac}C=C,
\quad B_{\operatorname{Frac}C}=\operatorname{Frac}C[X,Y],
\]
together with the actual Euler graph, the full Schur determinant, and
\(\mathbb C(Q_1,Q_2,X,Y)=\operatorname{Frac}(C)(X,Y)\).
Those inputs were established for the independent degree-two branch.
No saved reduction supplies them for every remaining branch below.

## 3. The rest of the supplied profile

First remove the constant-recombination cases. If \(d=0\), all four
partials are good, an already recognized case. More generally, a
nontrivial **complex constant** relation between \(V_3,V_4\) gives a
constant polynomial coordinate change supplying a third good partial.
The mixed height-nine theorem applies. These statements, and their
precise converse for constant frame changes, are proved in
[dependent defects, Sections 1--2](dependent-quadratic-defects-pass42.md).

The remaining sector map is as follows. An entry marked unclosed means
that the audited proof chain has no full recognition theorem for that
sector, after any applicable previously recognized subcases. It does
not assert existence of an action realizing every formal alternative.

| Defect sector | What is already recognized | What pass64 does not finish |
| --- | --- | --- |
| \(d=2\), nonconstant highest vector, \(m\ge3\) | The full companion image forces \(3\le m\le5\), \(E^mx=cq\), with \(c\) a constant good vector. If the preceding bad pair \(\ell=0\), a genuine good constant partial commutes with \(E\), giving recognition. Otherwise \(q=g^m\), \(\ell=\lambda g^{m-1}\), \(g\) nonconstant invariant and \(\lambda\ne0\). [Pass42](two-quadratic-top-line-pass42.md) proves these alternatives. Zero motion \(T_cg=0\) is fully recognized by [pass45](independent-zero-motion-closure-pass45.md). | Nonconstant motion remains after the further good-direction and direct-coordinate criteria below. The quadratic graph theorem does not apply merely because the inverse-flow Jacobian has quadratic time dependence. |
| \(d=2\), nonzero constant highest vector | The companion bounds give \(3\le m\le6\). For \(m\ge4\), [pass42, Section 6](two-quadratic-top-line-pass42.md#6-a-separate-constant-top-full-row-refinement) gives an actual polynomial slice and affine preceding-layer formulas. Any already proved commuting-partial or invariant-coordinate criterion still applies. | The full constant-top sector is not recognized by that refinement. It does not make the new slice an ambient coordinate. The \(m=3\) boundary can have two longest companion blocks and is not even covered by that particular affine-layer refinement. The independent zero-motion theorem explicitly excludes constant highest vectors. |
| \(d=1\), no constant relation, nonconstant highest vector, \(m\ge3\) | [Pass43](dependent-defect-top-line-pass43.md) gives \(m\in\{3,4\}\), primitive \(D\), \(V_3=aD,V_4=bD\), \(E^mx=cq\), and \([E,T_c]=-(m-1)rD/2\) with polynomial jointly invariant \(r\). The \(r=0\) case is recognized. The nonzero case has independent \(E,D\). [Pass44](dependent-preceding-curve-pass44.md) gives \(q=Q(u)\) and exhaustive common-power/rotating preceding-layer alternatives. [Pass45](rotating-zero-motion-closure-pass45.md) recognizes \(T_cu=0\) in both alternatives. | The nonzero-motion sector remains after the further good-direction and ramification criteria below. A rational relation between defects is not a constant coordinate recombination. |
| \(d=1\), no constant relation, lower flow or constant highest vector | The weighted five-dimensional companion gives \(E^6x=0\). Existing commuting-partial, invariant-coordinate, or other independently met recognition criteria remain available. | The full low-flow \(m\le2\) and constant-highest sectors are expressly outside the nonconstant high-top proof. No transfer of the rank-two degree-two image condition, invariant-plane graph, or pass64 theorem has been established for them. |

Two distinctions prevent a stronger reading of this table.

First, the original constant highest vector is not the same object as
the constant highest vector of the divided action \(\delta=E/g\) on
\(B_g\). The latter can have defect rank one even when the original
defects have rank two. The
[exact rank formula and localization caveat](two-quadratic-top-line-pass42.md#5-exact-rescaling-boundary)
do not supply a new global polynomial coordinate frame.

Second, the degree-five and degree-six closures for the separate
one-cubic profile \((1,1,1,3)\) use three good partials. They are not
closures of the constant-top or moving sectors of \((1,1,2,2)\).

## 4. Keep the later moving-parameter reductions

The broader [good-direction theorem](good-direction-recognition-pass46.md)
requires only two actual good partials and a nonconstant polynomial
\(z\in\ker E\cap\ker[E,T_1]\cap\ker[E,T_2]\) omitted by some
nonzero constant good direction. It recognizes the original kernel.
It applies to \(z=g\) in the independent high-top branch and \(z=u\)
in the dependent branch. Consequently a still-unrecognized instance
in either branch must have \(T_1z,T_2z\) complex-linearly independent.
This is not a statement of algebraic independence.

The [localization-gate note, Section 4](two-quadratic-localization-gate-pass42.md#4-a-small-recognition-branch-and-the-remaining-gap)
also recognizes \(T_cg\in\mathbb C^*\), since then \(g\) is a
triangular ambient coordinate. More generally an already exhibited
invariant ambient coordinate always bypasses the residual analysis.
Thus “nonzero motion remains” is not a claim that every nonzero
derivative is unrecognized.

For the dependent rotating alternative, the final retained arithmetic
condition is the stronger [pass46 condition](dependent-motion-ramification-pass46.md#3-a-stronger-necessary-condition-for-parameter-motion)
\[
T_cu\ne0\quad\Longrightarrow\quad
R_1\mid\gcd(Q',K_1',K_2',K_3',K_4')
\quad\text{in }\mathbb C[U].
\]
Failure invokes zero-motion recognition. The converse, integrability
of arbitrary formal curve data, and local nilpotence of further
correctors are not asserted.

For the independent moving branch,
[pass46](moving-commuting-repair-pass46.md) constructs a global
polynomial correction commuting with \(E\) and the relevant leading
fields, with zero divergence. It does not prove that correction
locally nilpotent under the full moving hypotheses. Its weaker
non-LND control is not a counterexample to the full frame problem.

These later reductions narrow the open sectors in Section 3; none
converts them into the degree-two graph of Section 2.

## 5. The universal quantifier remains separate

The precise currently inherited profile theorems are:

- Every frame with \(H\le9\) is recognized, by
  [the height-nine conclusion](../deep-pass-13.md) and its earlier
  zero/low-height criteria.
- The supplied profile \((1,1,1,3)\), including lower heights, is
  recognized by [the complete pass41 theorem](../deep-pass-41.md#1-the-conditional-theorem).
- The supplied profile \((0,2,2,2)\), including lower heights, is
  recognized by [pass42, Sections 1--6](three-variable-quadratic-frame-pass42.md).
- Pass64 now adds the full independent-defect degree-two part of
  \((1,1,2,2)\), not the whole last profile.

Accordingly the all-profile threshold has not become \(H\le10\).
If the remaining sectors of \((1,1,2,2)\) were recognized, a further
universal assertion that every sliced \(E\) admits a frame with
\(H\le10\) would suffice. Neither assertion follows from pass64.
They are the two separate remaining implications identified in
[the earlier universal-frame audit](universal-frame-reduction-audit-pass52.md#1-three-different-remaining-implications),
after its first, independent degree-two recognition obligation is
replaced by the new graph theorem.

The minimization identity \(H_{\min}(E)=3\) if and only if
\(A\simeq\mathbb C^{[3]}\) is an equivalence, not an upper bound.
The exact [all-inverse-pairs finite levels](universal-frame-search-pass43.md)
give a positive semidecision and do not prove termination for every
sliced action. A rational distribution, a tangent-module basis,
formal roots, local polynomial coordinates, or a Jacobian inverse
without a genuine global coordinate inverse cannot supply the missing
frame. Alternatively, an unrestricted proof of an invariant ambient
coordinate would suffice, but no such theorem is established here.

## 6. Registry and verification provenance

The read-only registry agrees with these older dependencies: Z114 is
the height-nine theorem; Z387 and Z391 are the other two complete
height-ten profile theorems; Z392 distinguishes constant from rational
defect dependence; Z394--Z399 record the degree-two and high-top
independent reductions; Z412 records the restricted dependent high-top
theorem; Z440 and Z443 are the two zero-motion closures; Z453--Z456
record the omitted-direction and final ramification restrictions.
The shared checkpoint predates the new pass64 closure. Its historical
open wording is not silently rewritten as a new theorem, and its old
degree-two open obligation is not retained as a present mathematical
gap after Section 2.

Pass64 does not establish that a specified intrinsic action has unit
plinth, trivial second-image ideal, an affine slice in the original bad
pair, or low-degree generation by its chosen filtration. Recognition
of \(A\) must not be substituted for proofs of these extra statements.
Pass64 provides a different recognition route. Earlier
valid divisor and generation lemmas remain conditional statements;
they are not all converted into nonexistence theorems. The polynomial
intrinsic-action control in
[pass52, Section 4](universal-frame-reduction-audit-pass52.md#4-polynomial-countercontrol-to-an-overstrong-relative-claim)
already illustrates why polynomial original kernel and relative
triviality for a chosen quotient are different conclusions.

For this scope audit I reread the complete relevant pass39/42/43
two-defect proofs, both pass45 zero-motion proofs, the pass44 preceding
curve proof, both pass46 moving/good-direction proofs, the pass44
generic graph, the current pass64 theorem, and the pass42
three-variable theorem. I checked the cited height-nine and pass41
theorem/exhaustion passages, the minimization and finite-search
definitions, the pass52 relevance audit, and the listed registry
entries. This is a dependency and scope reconstruction, not a fresh
full primary-source audit of every inherited theorem. The pass64
Dedekind and generalized-Luroth inputs retain their own explicitly
recorded source-access boundaries.

No new test suite or method is added, no full regression is claimed,
and no shared metadata is changed. No claim of a general cancellation
solution, new published theorem, historical novelty, human expert
review, or proof-assistant verification follows from this map.
