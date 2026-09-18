# Total fiber multiplicity and exclusion of generically rank-zero quadratic components

The local multiplicity bound extends to the sum over all components
of a closed fiber. In the actual nonconical frame, that sum is at
most twice the relative degree. As a consequence, in relative
degree two no fiber component can have generically rank-zero
quotient differential. This removes the irreducibility assumption
from that particular exclusion, but does not exclude isolated
rank-zero points on components whose generic rank is one.

## 1. A common surviving function

Retain all hypotheses and notation of
[local-multiplicity92](nonconical-closed-fiber-multiplicity-pass92.md).
Fix a closed base point m, and let
\(\mathfrak q_1,\ldots,\mathfrak q_h\) be all minimal primes
of mA. These are the finitely many generic points of its reduced
curve components. For each i, some generator among \(A_1,A_2,c\)
has nonconstant residue in \(A/\mathfrak q_i\).

The triples \((\lambda_1,\lambda_2,\lambda_3)\in\mathbb C^3\)
for which \(U=\lambda_1 A_1+\lambda_2 A_2+\lambda_3 c\) has
constant residue on a given component form a proper complex linear
subspace. Avoid the finite union of these subspaces. Then
\[
\begin{gathered}
\bar U_i\text{ is transcendental on every }A/\mathfrak q_i,
\qquad 1\le n=\deg_v U\le2d,\\
\mu_i=\operatorname{length}_{A_{\mathfrak q_i}}
 (A_{\mathfrak q_i}/mA_{\mathfrak q_i}),\qquad
f_i=[\kappa(\mathfrak q_i):\mathbb C(\bar U_i)]<\infty.
\end{gathered}
\tag{1}
\]
The degree estimate is exactly the retained generic polynomial
bound on the three generators. This choice introduces no new
coordinate assertion or base reparametrization.

## 2. The semilocal flat extension

Let \(\mathcal M=A\setminus\bigcup_i\mathfrak q_i\), and put
\[
T=(S[U])_{mS[U]},\qquad O'=\mathcal M^{-1}A,
\qquad J=mO',\qquad k_0=T/mT,\qquad F=K(U).
\tag{2}
\]
The complement \(\mathcal M\) is multiplicatively closed.
The maximal ideals of O' are exactly the extensions of the
\(\mathfrak q_i\): finite prime avoidance puts any prime
disjoint from \(\mathcal M\) inside one of them, and these
height-two primes are incomparable.

For every i, \(\mathfrak q_i\cap S[U]=mS[U]\). Thus each
denominator defining T is already invertible in O', giving an
actual map \(T\to O'\). Its localization at each maximal ideal
of O' is the flat map \(T\to A_{\mathfrak q_i}\) proved in
local-multiplicity92, with regular local dimensions two and zero
dimensional closed fiber. Flatness can be checked at all maximal
ideals of the target, so O' is flat over T.[^flatlocal]

The Noetherian ring O'/J has exactly these finitely many primes,
all maximal, and is therefore Artinian. Its local factors are the
Artinian whole-fiber rings in (1). Hence its dimension over k0
is \(\sum_i\mu_i f_i\). Its generic localization is still
\(O'\otimes_T F=K(v)\), of F-dimension n.

Apply the same associated-graded independence proof as in
local-multiplicity92 to a k0-basis of O'/J. Flatness identifies
\(\operatorname{gr}_J(O')\) with
\(\operatorname{gr}_{mT}(T)\otimes_{k_0}(O'/J)\).
A nonzero relation among lifts has a least coefficient order in
the regular local source T, contradicting residue-basis independence.
The target being semilocal rather than local changes none of this
argument. It follows that
\[
\boxed{\qquad
\sum_{i=1}^h\mu_i f_i\le\deg_v U\le2d,
\qquad\sum_{i=1}^h\mu_i\le2d.
\qquad}
\tag{3}
\]
This proof neither assumes finiteness of O' over T nor counts only
fixed components. Every component of the closed fiber is included,
and each has positive multiplicity.

## 3. What the aggregate bound excludes

Suppose one component has both quotient differentials zero at its
generic point in the ambient cotangent module. The local proof
gives \(\mu_i\ge4\). If d=2, (3) forces \(h=1\) and
\(\mu_1=4\). The whole reduced fiber is therefore irreducible.
Its generic rank-zero condition makes N vanish along it, so it
lies over the retained exceptional curve. The independently
reconstructed [ramification proof92](nonconical-irreducible-fiber-ramification-pass92.md)
then forces \(\mu_1=2\), a contradiction. Consequently
\[
\boxed{\quad d=2\ \Longrightarrow\
\operatorname{rank}(ds_1,ds_2)_{\mathfrak q_i}\ge1
\text{ for every generic closed-fiber component.}\quad}
\tag{4}
\]
At a fixed component this generic rank is exactly one, since N
is the Jacobian field and vanishes there. Its fixed scheme is
generically a local complete intersection by fixed-scheme92.
The conclusion does not rule out a lower-rank closed point on
that curve or a rank-one fixed curve of multiplicity two.

For d=3, (3) permits at most one generically rank-zero component.
If its multiplicity is six, it is the only component and the
ramification proof forces retained branch degrees two and three.
If its multiplicity is five, at most one other component remains,
of multiplicity one. If it is four, the total multiplicity of all
other components is at most two. A sole component of multiplicity
four or five is excluded by the irreducible ramification list,
so those two cases would actually require other components.
These are necessary constraints, not constructions or a proof
that the cubic case is impossible.

## 4. Verification and sources

The semilocal sum is a new derived use of the local flat-rank
argument. The degree-two exclusion additionally uses the retained
topological hypotheses from the linked ramification proof, not an
uncited assertion that all fibers are irreducible. No generic
rank condition is upgraded to a condition at every point.
The unrestricted cancellation conjecture and the reduction from
an arbitrary sliced action to this frame remain open here.

[^flatlocal]: The Stacks Project,
    [Lemma 10.39.18(7), 00HT](https://stacks.math.columbia.edu/tag/00HT),
    complete statement and displayed proof freshly read on
    2026-09-14. It checks flatness of a module after localization
    at all maximal ideals of the target, over their contracted
    source primes. All those contractions here are mT. The proof
    tests injectivity of ideal tensor maps by target localization;
    it does not require a finite target module. The local miracle
    flatness and associated-graded steps are proved and sourced
    in local-multiplicity92.
