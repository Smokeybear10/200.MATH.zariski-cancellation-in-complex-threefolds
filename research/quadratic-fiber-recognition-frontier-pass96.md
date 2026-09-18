# Quadratic fiber restrictions and the global recognition boundary

The actual quadratic case now has two stronger restrictions:
every reduced closed-fiber component is an entire affine
line, and any noncollapsed fixed component is the whole
reduced fiber. A separate dependency argument retains the
needed multiplicity exclusion with fewer topological
source assumptions.

These results do not recognize the threefold. An explicit
polynomial-ring control shows why even the improved
quotient geometry, a unit speed row, and a relative
inverse cannot replace the original-coordinate hypothesis.

## 1. The target and the conditional result

The working target is still the unconfirmed interpretation
of the professor's question as
\[
A[u]\simeq\mathbb C^{[4]}
\quad\Longrightarrow\quad A\simeq\mathbb C^{[3]}.
\tag{1}
\]
It remains unsolved. The present deductions require the
supplied actual nonconical constant-acceleration frame
and its quadratic relative-degree branch. Cancellation
alone has not been shown to provide that frame.

Use the notation of
[the previous synthesis](nonconical-quadratic-rank-frontier-pass95.md):
the canonical primitive LND N has actual kernel
\(S=\mathbb C[s_1,s_2]\), the quotient is faithfully flat,
and \(A=S[A_1,A_2,c]\). The good relative functions have
generic degree at most two and c has degree at most four.
A component is collapsed if both good functions become
constants on it.

For every closed base value, write \(C=A/mA\) and let
\(\mu_i\) be the whole-fiber multiplicities at its
generic components. The combined restrictions are
\[
\begin{gathered}
C_{\rm red}=\coprod_i\mathbb A^1,\qquad
1\le\mu_i\le3,\qquad \sum_i\mu_i\le4,\\
C_{\rm red}\text{ irreducible}\ \Longrightarrow\
\mu_1\in\{1,2\},\\
\text{a noncollapsed fixed component exists}
\ \Longrightarrow\
C_{\rm red}\simeq\mathbb A^1,\quad \mu_1=2.
\end{gathered}
\tag{2}
\]
Every fixed component in a reducible fiber is therefore
collapsed. The remaining irreducible fixed fibers have
multiplicity two. Neither class has been excluded.
The earlier everywhere quotient-rank bound remains
at least one, not two.

## 2. Why the affine-line components have no missing points

The [affine-line proof](quadratic-fiber-affine-lines-pass96.md)
starts from theorem95's smooth disjoint open-line
components. Take the standard quotient product strata,
with a finite set of bad base values removed, and
write \(L\) for their full reduced inverse image,
\(X^*=X\setminus L\), and \(\check X\) for the
product complement of the exceptional curve.

The intervening smooth divisor is a product of a
noncompact curve with an affine line. Ordinary
homological Thom therefore gives
\(H_4(X^*,\check X)=0\). The product complement of
an affine surface has zero fourth homology, so
\(H_4(X^*)=0\). Contractibility of X and a second
ordinary Thom isomorphism give
\[
0=H_4(X^*)\simeq H_5(X,X^*)
\simeq H_1(L).
\tag{3}
\]
Here L is a closed smooth, possibly disconnected and
noncompact, complex curve in a smooth threefold.
Ordinary homology is the correct version of Thom for
the tubular-neighborhood pair; no compactness or
trivial normal bundle is assumed.

An affine line with k missing points has first homology
\(\mathbb Z^k\). Equation (3) forces k=0 for each
component. The choice of the removed finite set can
include any chosen closed base value.

## 3. Why a noncollapsed fixed component cannot have companions

The [compatibility proof](quadratic-component-compatibility-pass96.md)
has an independent algebraic route. It does not use
the new topological puncture-removal result.

Suppose a noncollapsed fixed component had a companion.
A surviving good generator U has generic degree two
and the fixed component has multiplicity two. Its
reduced field is \(\mathbb C(\bar U)\), and its third
residue is a rational function \(a(\bar U)/b(\bar U)\).
A generic projection \(U+t c\) survives on every
component. Twice its positive residue degree on the
chosen component, plus the positive companion
contribution, is at most four. That residue degree
must equal one. Hence b is constant and a is affine,
so the chosen component is already an entire U-line
under this contradiction premise.

Choose a point on a companion and the point of that
line with the same U-value. The whole thickening95
gives transverse length two at the latter point.
The actual map from the regular local three-ring
\(T=(S[U])_{(m,U-\alpha)}\) to the regular local
ring \(A_p\) is flat by the dimension equality.
Its generic field degree and special length are
both two. Equality in the retained flat-rank lemma
forces \(A_p\) to be finite free over T.

The intermediate actual base change
\(D=A\otimes_{S[U]}T\) then equals \(A_p\), since
an integral localization of a domain cannot invert
a new element. But the two different points survive
as distinct maximal ideals of D. That contradicts
the locality of \(A_p\).

This rules out every companion, not just a second
fixed component and not just the (2,2) profile. In
particular a (2,2) fiber, if it exists, consists of
two collapsed components. No nonzero-first-normal
action premise is needed.

## 4. The narrower multiplicity dependency

The [dependency audit](irreducible-fiber-dependency-audit-pass96.md)
reconstructs the whole-irreducible multiplicity
exclusion. It uses the finite exceptional-curve
factorization and equality of the normalization
first-Betti numbers. A finite-cover transfer makes
the map on normalization first homology rationally
surjective. Equal ranks and torsion-free integral
homology then make it integrally injective.

That injectivity prevents handle or infinity classes
from hiding an integral puncture obstruction. The
full supported Thom lattice, rather than only its
rational span, identifies an irreducible fiber's
multiplicity with the least common multiple of its
branch degrees. The actual divisor degree bound is
two, so the multiplicity is one or two.

This avoids the later theorem that removes bijective
exceptional components and does not require all their
normalizations to be affine lines. Exact controls
show why the homology premise and reduced prime
divisor pullbacks still cannot be dropped. The
replacement argument supports the stated use of92;
it does not retroactively certify every dependency
in the research collection.

## 5. The original-coordinate condition is still essential

The [global-bridge control](quadratic-global-bridge-pass96.md)
uses the literal ring \(A=\mathbb C[a,y,v]\), its
cylinder, and the primitive field
\(N=a\partial_y+y\partial_v\) with invariant plane
\(S=\mathbb C[a,t]\), \(t=2av-y^2\).
Its closed quotient fibers have exactly the smooth
reduced-line and double-thickening behavior relevant
above.

The speed row and proposed tuple are
\[
\begin{gathered}
b=(a,at-1,t^2),\qquad (t,-1,0)b^t=1,\qquad
\Omega=t(at+2),\\
X_1=au+y,\quad X_2=(at-1)u+ty,\quad
X_3=t^2u+v,\quad Z=a+u^2 .
\end{gathered}
\tag{4}
\]
The row has generic rank two, has no nonzero constant
linear combination that is constant, and is a unit
row. N is free on \(D(\Omega)\). The bad function Z
is a genuine coordinate with \(E^2Z=2\), for
\(E=\partial_u\), and the good functions satisfy
\(E^2X_i=0\). The determinant-one relative frame
gives an exact inverse over S and the exact
relative generator pencil.

Nevertheless the four proposed functions are not
an original coordinate tuple. Their Jacobian vanishes
at \((u,a,y,v)=(i/2,0,1,0)\), where \(\Omega=-2\).
A displayed tangent vector also proves that u, a
and t are not polynomials in that tuple alone.
Thus the relative inverse cannot be converted into
an ambient inverse by silently recovering its
coefficients.

This is not a counterexample to the actual-frame
theorem or cancellation: A is already polynomial,
and the original-coordinate premise fails. It
isolates the global hypothesis that a successful
recognition argument still must use.

## 6. Evidence and the next unresolved step

The [canonical symbolic capture](verification-pass96-working.json)
passes one method for the explicit bridge control.
It checks polynomial identities, the singular
point and the tangent obstruction. It does not
test the universal topology or finite-flat arguments.
The [audit](proof-audits-pass96-working.md) records
saved-proof AI reviews and the precise source limits;
the [checkpoint](checkpoint-pass96-working.json)
records the saved state.

The next mathematical targets are the remaining
collapsed fixed components in reducible fibers and
the irreducible double fibers. Their intrinsic
quotient models alone permit fixed curves. Progress
toward recognition must therefore add restrictions
from the original four-coordinate inverse, volume,
or partial-derivation identities.

The separate reduction from arbitrary sliced actions
to the studied frame remains missing. No external
expert review, proof-assistant verification, historical
novelty clearance, public claim, outreach or submission
is represented by these results.

## Sources

The linked proofs contain the full assumptions,
derivations, countercontrols and source scopes.
The primary external inputs checked for this pass are:

- Shulim Kaliman,
  [*Free C+-actions on C3 are translations*](https://www.math.miami.edu/~kaliman/library/Ka.invent.2004.c%2B.pdf),
  Lemmas 2.1--2.2, Notation 2.3 and Proposition 3.2.
  The source-dependent deductions use these quotient
  strata and homological inputs, not a freeness
  assumption on the present action.
- The Stacks Project,
  [miracle flatness, tag 00R4](https://stacks.math.columbia.edu/tag/00R4),
  and [faithfully flat completion, tag 00MC](https://stacks.math.columbia.edu/tag/00MC).
  Their complete displayed statements and proofs were
  checked; the retained finite-rank lemma supplies
  the separate finite-generation step.
- The Stacks Project,
  [Nagata's criterion, tag 0AFU](https://stacks.math.columbia.edu/tag/0AFU),
  used only for the factorial quadric control in
  the dependency audit.
