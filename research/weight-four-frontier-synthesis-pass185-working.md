# Weight-four frontier: one full exclusion and a second recognized branch

**Status: synthesis of restricted working proofs. The cancellation
conjecture is not solved.**

The new investigation excludes the full coprime quadratic-pair initial
kernel \(X^2Z+Y^2W\) in the supplied actual two-linear/two-quadratic
setup. This is a universal conditional exclusion, not a failed search
for examples. A different quartic, \(X^2Z+XYW-Y^4\), has an explicit
invariant-coordinate construction in its high-graph branch. Its other
branches remain open in this packet.

Separately, an elementary rational-differential argument excludes the
absent-\(W\) double cover \(Z^2+H_4(X,Y)\) when the binary quartic is
squarefree. A complete algebraic normal-form list identifies the
remaining weight-four families without asserting that they occur.

## 1. Exact assumptions of the main exclusion

Suppose
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\\
(\deg_E X,\deg_E Y,\deg_E Z,\deg_E W)=(1,1,2,2),\\
a=EX,\quad b=EY,\quad e=E^2Z/2,\quad h=E^2W/2,\\
\theta_0:(\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
 \longmapsto(a\tau,b\tau,e\tau^2,h\tau^2).
\end{gathered}
\tag{1}
\]
The generators are actual polynomial coordinates and the slice is
global. The working conclusion is that
\[
\boxed{\ker\theta_0
\ne(\mathsf X^2\mathsf Z+\mathsf Y^2\mathsf W).}
\tag{2}
\]
The single identity \(a^2e+b^2h=0\) is not enough for this conclusion:
the proof assumes this polynomial would generate the full initial
kernel. A larger, height-two kernel is outside its hypotheses.
There is no assumption that (1) is a minimum-degree frame, and no
claim that an arbitrary sliced action can be put into that frame.

## 2. Why every case in this supplied configuration is covered

The proof has the following actual-ring and exact-field steps.

1. [Universal chart184](weight-four-universal-chart-potentials-pass184-working.md)
   derives a selected intrinsic derivation \(N\), its exact field \(L\),
   and the entire generic line \(L[v]\). The determinant is calibrated
   from the original polynomial inverse, not postulated.
2. The same proof obtains two polynomial potentials and a nonzero
   plane eliminant of exact degree five, with top part \(-U^4V\).
   The return coefficient \(R=k_\rho-2ty\) is proved nonzero, but is
   not presumed to be a unit.
3. [Whole-plane completion184](weight-four-bad-linear-whole-plane-projection-pass184-working.md)
   proves \(L[y,\vartheta]=L[v]\), including every zero of \(R\).
   Its repeated-center case uses the separately proved
   [degree-five cone lemma184](vertex-free-quintic-cone-projection-pass184-working.md).
   The lemma's explicit degree-six failure records the limit of that
   argument; the example is not a cancellation counterexample.
4. [Selected-component184](weight-four-bad-linear-selected-component-pass184-working.md)
   proves a unit evaluated cofactor and reduces \(y\) to a constant
   or a nonconstant affine parameter. It excludes the intermediate
   quadratic possibility by a polynomial inverse and coefficient
   comparisons, without a plane-embedding classification theorem.
5. [Affine-projection exclusion185](weight-four-coprime-graph-degree-obstruction-pass185-working.md)
   excludes every graph degree in the affine case. A quadratic graph
   would force an algebraic function of \(t\) to have the irrational
   Euler exponent \(3/2\pm\sqrt2\); the exact-field obstruction is
   proved using its minimal polynomial.
6. [Constant-projection exclusion185](weight-four-coprime-constant-projection-exclusion-pass185-working.md)
   independently excludes the constant case. The actual determinant
   forces a rational expression whose vanishing would give a
   polynomial in a transcendental \(R\) with nonzero leading
   coefficient \(-3/(8t^3)\).

The two alternatives in step4 are exhaustive and both are contradicted.
This proves (2) subject to the retained written working inputs.
The constant-projection proof does not depend on the whole-plane
or graph-degree exclusions, so it is not a circular case elimination.

There is an immediate normal-form consequence. For a full irreducible
weight-four relation
\[
F=P_2(X,Y)Z+Q_2(X,Y)W+H_4(X,Y)
\tag{3}
\]
with independent coprime binary quadratics \(P_2,Q_2\), the
[zero-bad-rank classification184](weight-four-zero-bad-rank-normal-forms-pass184-working.md)
uses actual homogeneous polynomial automorphisms to obtain (2).
Each slot retains its exact time degree, since no nonzero relation
of weight one or two lies in a principal weight-four initial ideal.
Thus this entire coefficient-pair class is excluded, not just a
chosen literal generator.

## 3. The other completed reductions and their limits

| Configuration under the actual setup | Result in this packet |
| --- | --- |
| Zero quadratic bad rank, independent coprime quadratic coefficients | Excluded by (2)--(3). |
| \(X^2Z+XYW-Y^4\), affine \(y\), graph degree at least three | Recognized; the graph is forced to have degree five and an actual invariant coordinate is constructed. |
| \(Z^2+H_4(X,Y)\), absent \(W\), squarefree binary quartic | Excluded by a rational-function obstruction. |
| Other degree-four forms | Classified under the stated homogeneous automorphism group, not generally excluded or recognized. |

For the second row,
[high-graph recognition185](weight-four-common-factor-high-graph-recognition-pass185-working.md)
derives the requisite normalization through actual constant
translations. The
[normalized endpoint185](weight-four-normalized-common-factor-recognition-pass185-working.md)
then returns the coefficient \(m\) to an original polynomial:
\[
I=dW-(X^2Z+XYW-Y^4)+K_3(X,Y)+N_2(X,Y)-\ell_1Y-\ell_0X,
\quad d\in\mathbb C^* .
\tag{4}
\]
A companion has a two-sided polynomial inverse with determinant
\(-d^2\). Thus \(I\) is an actual invariant coordinate, not only a
generic line parameter. The slice supplies regularity, and the
published Bhatwadekar--Gupta--Lokhande Theorem3.5 supplies the final
polynomial-kernel conclusion. The constant-\(y\) and graph-degree
at-most-two branches are not disposed of here.

The [squarefree exclusion184](weight-four-squarefree-double-cover-exclusion-pass184-working.md)
uses a two-point affine-line restriction and the impossibility of a
nonzero pole-free rational differential on \(\mathbb P^1\). It does
not assume rationality of \(A\). Its conclusion does not transfer
to \(ZW+H_4\), where the leading surface is a different object.
The [positive-bad-rank classification184](weight-four-positive-bad-rank-normal-forms-pass184-working.md)
retains that distinction, including the cross-ratio family at rank two.

## 4. Verification and remaining goal

The packet contains complete written arguments and independent
saved-source AI reviews. Its separate symbolic controls check raw
determinants, coefficient identities, algebraic-coefficient terms,
actual translations, and both coordinate inverse orders. They do
not prove universal field arguments, actual chart entry, or every
historical source dependency. A passing finite test suite is not
being called a proof of cancellation.

The full corrected complex-threefold question
\(A[u]\simeq\mathbb C^{[4]}\Rightarrow A\simeq\mathbb C^{[3]}\)
remains unsolved in this project. Other quartic families, height-two
initial kernels, higher minimum time profiles and arbitrary entry
are still unresolved. The professor has not confirmed this corrected
field-and-dimension interpretation of the original email.

The next bounded proof task is the remaining branches for
\(X^2Z+XYW-Y^4\), beginning with constant \(y\) and a quadratic graph.
That task is a continuation toward the full objective, not a
redefinition of success.
No expert review, proof-assistant certification, historical novelty
clearance, public claim, submission or external contact has occurred.
The full goal remains active.
