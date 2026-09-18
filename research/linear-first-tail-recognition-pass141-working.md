# Linear first tails give an invariant coordinate and recognition

In the actual dense three-good setup, a linear first-tail polynomial
is equivalent to the existence of an invariant last coordinate obtained
by a polynomial shear fixing the other three coordinates. In that
case a published nice-derivation theorem identifies the invariant ring
with a polynomial three-ring.

This is a sufficient recognition criterion, with no bound on the
original last-coordinate time degree. It does not assert that every
actual first tail is linear, primitive, or reducible to this case.

## 1. Exact criterion

Assume the actual hypotheses and fixed normalization of the
shear-minimum theorem141.[^1] In particular,
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad A=\ker E,\\
E^2X=E^2Y=E^2Z=0,\quad
(EX,EY,EZ)\text{ has rank two and dense homogeneous cone},\\
m=\deg_E W,\quad \Phi\in L[U,V]\setminus\{0\},\quad
\mu=\min_{P\in\mathbb C[X,Y,Z]}\deg_E(W+P)=\deg\Phi-1 .
\end{gathered}
\tag{1}
\]
Here rank two means that the speed field has transcendence degree two.
The first tail \(\Phi\), including its exact finite coefficient field,
is the one specified in that theorem, not a freely chosen relation.

It follows that
\[
\deg\Phi=1
\quad\Longleftrightarrow\quad
\exists P\in\mathbb C[X,Y,Z]\text{ with }I=W+P\in A .
\tag{2}
\]
Indeed \(\deg_E I=0\) is exactly \(EI=0\) for the nonzero polynomial
\(I\). The minimum formula proves both implications. When (2) holds,
the explicit choice from141 is
\[
P_*=-\sum_{j=1}^{m}X^j f_j(Y/X,Z/X),\qquad
B=\mathbb C[I,X,Y,Z],\quad I=W+P_*,\quad EI=0 .
\tag{3}
\]
Every \(f_j\) in this sum belongs to
\(\mathbb C[\tau,\rho]_{\le j}\); the displayed homogenizations are
therefore complex polynomials, including at \(X=0\).
The coordinate inverse is \(W=I-P_*(X,Y,Z)\).
For \(m=0\), the sum is empty and \(I=W\).

There is no hidden claim that \(I\) is an ambient coordinate because it
is invariant. Its ambient coordinate status follows from the explicit
elementary shear. It is nonconstant since \(\partial_W I=1\).

## 2. Recognition with every published hypothesis checked

Dasgupta and Gupta's Corollary 3.8 states that an irreducible locally
nilpotent derivation of a characteristic-zero polynomial four-ring
has a polynomial three-ring as kernel if it kills one coordinate
and its square kills the other three.[^2]

Apply that result to the actual coordinate order \((I,X,Y,Z)\).
The derivation \(E\) is locally nilpotent because \(E=\partial_u\)
on \(A[u]\), and it is nonzero because \(Eu=1\).
It is irreducible: a nonunit dividing every value of \(E\) would
divide \(Eu=1\). Equation (3) gives \(EI=0\), while the other three
square-zero identities are retained from (1). The base field is
\(\mathbb C\), so the characteristic hypothesis holds.
Thus
\[
\deg\Phi=1\quad\Longrightarrow\quad A\simeq\mathbb C^{[3]} .
\tag{4}
\]

The classification in this step is an external theorem, not a new
proof of that classification. The new minimum-degree identity supplies
its actual invariant-coordinate hypothesis in the stated linear-tail
regime.

## 3. Scope and the unsolved step

The converse of (4) is not asserted. Already recognized polynomial
frames can have first tails of arbitrarily large degree, as the sharp
actual family140 shows.[^3] Consequently forcing every first tail to
be linear cannot be a valid general proof strategy.

If an actual first tail is primitive and its exact generic-line
equation is linear, then its degree is one and this criterion applies.
A linear generic-line equation alone does not prove that premise:
the formal inverse-branch family141 has a linear selected component
and arbitrarily high first-tail degree, although it fails the actual
polynomial-inverse assumptions.[^4]

Neither arbitrary actual first-tail primitivity nor recognition in
the remaining dense higher-degree regime is settled here. Supplying
three affine-in-time coordinates for an arbitrary sliced polynomial
fourfold remains a separate gap. Unrestricted cancellation and
historical novelty remain unproved.

## Sources

1. [Fixed-good shears preserve the tails and determine minimal time degree141](dense-shear-minimal-tail-pass141-working.md),
   Sections 1--4. Exact hypotheses, peeling coefficients, polynomial
   homogenizations and the minimum identity.
2. Nikhilesh Dasgupta and Neena Gupta.
   [*Nice derivations over principal ideal domains*](https://arxiv.org/pdf/1701.03635v1),
   arXiv:1701.03635v1, January 13, 2017, Corollary 3.8, printed p. 8.
   Published in *Journal of Pure and Applied Algebra* 222 (2018),
   4161--4172, [DOI](https://doi.org/10.1016/j.jpaa.2018.02.025).
3. [An actual sharp dense-tail family140](sharp-dense-tail-family-pass140-working.md).
   The explicit inverse-verified examples have \(\deg\Phi=m+1\).
4. [Formal tail factors and inverse branches in every degree141](formal-tail-inverse-branch-family-pass141-working.md),
   Sections 4--5. The linear component does not make the noninvertible
   polynomial tuple an actual coordinate frame.

[^1]: Source 1.
[^2]: Source 2. The precise coordinate and irreducibility assumptions
    are used, not just the phrase “nice derivation.”
[^3]: Source 3.
[^4]: Source 4.
