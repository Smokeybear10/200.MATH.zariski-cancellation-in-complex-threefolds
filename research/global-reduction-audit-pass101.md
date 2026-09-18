# The global entry gate has no dimension-only spatial-degree cutoff

Even a tame translation on actual complex four-space can require
arbitrarily high ordinary degree before any nonconstant invariant,
slice, or flow-linear polynomial appears in the supplied coordinates.
The exact construction below proves this simultaneously for every
polynomial below the chosen degree, not only for linear combinations
of a specified retraction's generators.

This sharpens the search boundary without disproving frame existence.
Its kernels are explicitly polynomial. The largest remaining global
obligation is still to produce an actual recognized frame for an
arbitrary polynomial cylinder, or to recognize its factor without
that frame. Finishing the current quadratic fiber calculations does
not supply this entry theorem.

## 1. Trace the actual assumptions, not just the word quadratic

The unrestricted working target gives only
\[
B=A[u]\simeq\mathbb C[x_1,x_2,x_3,x_4],\qquad
E=\partial_u,\qquad A=\ker E.
\tag{1}
\]
Here u is a polynomial slice, not a known ambient coordinate.
The retraction makes A finitely generated and regular. It does not
bound the E-degrees of the supplied original coordinates.

The [current frontier100](quadratic-action-frontier-pass100.md)
uses a substantially narrower chain of actual hypotheses:

| Stage | Extra entry condition or established conditional output |
| --- | --- |
| Original constant-acceleration frame | Actual polynomial coordinates with \(E^2x_i=0\) for three generators and \(E^2z=q\in\mathbb C^*\). Existence for arbitrary (1) is unproved. |
| Nonconical speed branch | The [homogeneous-speed branch89](homogeneous-speed-recognition-frontier-pass89.md) is recognized. In the remaining branch, the actual intrinsic plane S and nonzero determinant Omega are constructed from the supplied frame. |
| Relative quadratic branch | The [actual relative plane relation90](nonconical-cubic-relation-pass90.md) has degree at most three. [Degree one91](nonconical-linear-relation-recognition-pass91.md) is recognized; the current quadratic program takes degree two. This is not an ordinary degree bound on E or on its coordinates. |
| Whole-fiber calculation100 | A collapsed fixed double, possibly with a simple companion, and nonzero speed normal L(m). Other quadratic sectors and the relative cubic sector are not covered by these fiber formulas. |

The exact first entry condition is
\[
E^2x_1=E^2x_2=E^2x_3=0,\qquad E^2z=q\in\mathbb C^*.
\tag{2}
\]
It supplies its own canonical slice Ez/q, but no argument here or
in100 produces such coordinates from arbitrary (1).
Even a complete solution of all the current degree-two sectors
would leave the relative cubic branch before reaching the full
constant-acceleration theorem. Even that full theorem would still
leave the entry from (1) to (2), or to a recognized alternative.

The [universal audit52](universal-frame-reduction-audit-pass52.md)
and [degree-scope audit58](coordinate-slice-degree-scope-pass58.md)
already separate these types of hypotheses. Their historical
height thresholds are superseded by
[height-ten closure73](height-ten-closure-pass73.md): the supplied
adjoint-frame recognition through height ten is complete, but a
universal minimizing-frame bound is not. Adjoint height, orbit
degree, relative degree, and ordinary spatial degree are distinct.

## 2. An actual translation with an arbitrarily late first witness

Fix any integer k at least two. Start with genuine independent
coordinates u,a,b,c and perform four successive polynomial shears:
\[
\begin{gathered}
x_1=a+u^k,\qquad x_2=b+x_1^k,\qquad
x_3=c+x_2^k,\qquad x_4=u+x_3^k,\\
u=x_4-x_3^k,\qquad a=x_1-(x_4-x_3^k)^k,\\
b=x_2-x_1^k,\qquad c=x_3-x_2^k,\\
B=\mathbb C[x_1,x_2,x_3,x_4]=\mathbb C[u,a,b,c],
\qquad E=\partial_u,\qquad A=\mathbb C[a,b,c].
\end{gathered}
\tag{3}
\]
Substituting the forward equations in the inverse recovers u first,
then a,b,c. Conversely the inverse identities give x_1, then x_2,
then x_3, and finally x_4. Thus both inverse orders are proved;
a unit-Jacobian implication is not being used.

In particular E is an actual sliced polynomial LND. If desired its
original coefficients can be read without expanding the powers:
put U=x_4-x_3^k and successively use
\(Ex_1=kU^{k-1}\), \(Ex_2=kx_1^{k-1}Ex_1\),
\(Ex_3=kx_2^{k-1}Ex_2\), and
\(Ex_4=1+kx_3^{k-1}Ex_3\).
The polynomial inverse proves all their claimed LND identities.

Restrict to the actual E-orbit a=b=c=0, with parameter t=u:
\[
\begin{gathered}
(x_1,x_2,x_3,x_4)|_{a=b=c=0}
 =(t^k,t^{k^2},t^{k^3},t+t^{k^4}),\\
w(\alpha)=\alpha_1k+\alpha_2k^2+\alpha_3k^3+\alpha_4k^4,\\
|\alpha|<k\quad\Longrightarrow\quad
\deg_t(x^\alpha|_{a=b=c=0})=w(\alpha),
\quad\text{with leading coefficient one}.
\end{gathered}
\tag{4}
\]
For distinct exponent vectors of total degree less than k, these
weights are distinct. Divide by k: the four entries are digits
between zero and k-1 in a base-k expansion. Uniqueness follows
successively by reduction modulo k and division by k.

Now take any nonconstant P in the original polynomial ring with
ordinary total degree less than k. Its distinct monomials have
distinct leading orbit degrees. The monomial with largest weight
cannot be canceled by any of the others, including their lower
terms arising from x_4. Its weight is at least k. Therefore the
restriction of P to this one orbit has degree at least k.

For a polynomial in A[u], its degree after setting a=b=c=0 is
at most its degree in u before specializing. In characteristic
zero the latter degree is exactly its E-degree. We obtain the
all-polynomial statement
\[
\boxed{\quad
P\notin\mathbb C,\quad \deg_x P<k
\quad\Longrightarrow\quad \deg_E P\ge k.
\quad}
\tag{5}
\]
This includes arbitrary complex coefficients and every cancellation
within P. It is not inferred from finitely many sample polynomials.

## 3. Exact minima and the quantifiers this control rules out

For k at least two, (5) excludes below degree k every nonconstant
invariant, every E-slice, and even every nonconstant element killed
by E squared. The inverse (3) supplies a slice u of degree exactly k
and an invariant ambient coordinate b of degree exactly k. Hence
\[
\begin{gathered}
\min_{Ev=1}\deg_x v=k,\qquad
\min_{f\in\ker E\setminus\mathbb C}\deg_x f=k,\\
\min_{\substack{f\text{ ambient coordinate}\\Ef=0}}\deg_x f=k,
\qquad
\min_{\substack{f\notin\mathbb C\\E^2f=0}}\deg_x f=k.
\end{gathered}
\tag{6}
\]
All minima concern the fixed actual derivation expressed in its
specified x-coordinates. They allow every polynomial slice and
every polynomial invariant, not just the supplied u or a linear
extraction from a projected generating list.

Thus no cutoff depending only on dimension four and existence of
a slice can bound the first invariant-coordinate witness, the
first coordinate slice, or the forward degree of a frame satisfying
(2). Any such frame has nonconstant E-good generators and therefore
has forward degree at least k. The all-inverse-pairs search43 must
likewise have no successful invariant-coordinate level below k
on this example, regardless of the permitted inverse degree.

The conclusion does not concern a bound depending on the actual
input complexity. Here the least slice degree k and original orbit
degrees \(k,k^2,k^3,k^4\) grow with k. This is
consistent with the conditional uniform bound inside each fixed
finite-complexity family in
[bounded-family73](universal-family-degree-boundary-pass73.md).

Nor does the construction obstruct nonlinear frame existence.
The adapted coordinates (a,b,c,u) already recognize its kernel and
have minimum slice-filtration height three. The actual frame
\((a,b,u,c+u^2)\) satisfies (2) with q=2 and constant speeds.
Its explicit inverse recovers c by subtraction. Thus (3) is not an
exceptional factor, an unrecognized action, or a counterexample to
either cancellation or a universal orbit-height bound.

## 4. The primary recognition endpoint and the priority consequence

Bhatwadekar, Gupta and Lokhande, Theorem 3.5, assumes a nonzero
LND on an actual polynomial four-ring, fixes an actual ambient
coordinate, and requires a regular kernel. It concludes polynomiality
over that coordinate ring. Its short proof localizes at primes of
the coordinate PID and applies its Proposition 3.3(ii) and patching
Theorem 2.2.[^bgl]

For (1), regularity is already present. The ambient invariant
coordinate is the missing premise. The theorem recognizes a
witness; it does not manufacture one. This is the retained
endpoint from21/43, freshly checked here, not a new source result.
The earlier time-degree and relative-fibration source gates remain
those of52/58. This bounded check supplies no primary theorem
producing (2) or an invariant coordinate for every sliced action,
and is not a claim that none exists in the literature.

The priority consequence is concrete. A fixed spatial-degree
ansatz cannot stand in for the unrestricted bridge, even on tame
positive examples. A universal lane must instead prove a degree-
adaptive witness theorem, a valid terminating frame change, or an
argument recognizing A without that coordinate search. Advancing
the quadratic fiber lane can remain useful, but it must not be
counted as progress on that entry gate unless an actual transfer
is supplied.

The new obstruction differs from projection95, which fixes a slice
and rejects constant linear combinations of four projected generators.
Here every polynomial below an arbitrarily large degree is excluded,
and the minima range over every slice and every invariant. It also
differs from the scalar-filter obstruction81 and the finite-jet
control43. No general frame nonexistence is asserted in any of these
comparisons.

## Verification and source scope

The inverse, unique-leading-degree proof and exact minima above are
elementary all-k arguments. No finite numerical method is added or
used as their proof. Deduplication included complete reads of52,58,
search43, scalar-filter81, projection95 and bounded-family73, and
the relevant exact definitions and current conditional frontiers.
The current joint100 proof was separately audited through EOF.

For the primary input, the complete displayed Theorem 3.5 and its
short proof were freshly read in the original arXiv HTML. Its cited
DVR proposition, PID patching theorem and deeper dependencies were
not newly reconstructed in this pass. The rest of this note does
not invoke an external classification theorem. Any later independent
review is an AI reconstruction, not expert or formal certification.
No file through100, registry, checkpoint or execution record is edited.

[^bgl]: S. M. Bhatwadekar, Neena Gupta and Swapnil A. Lokhande,
    [*Some K-theoretic properties of the kernel of a locally nilpotent derivation on k[X1,...,X4]*](https://arxiv.org/html/1501.01438v1),
    arXiv:1501.01438v1, Theorem 3.5 and complete displayed proof.
