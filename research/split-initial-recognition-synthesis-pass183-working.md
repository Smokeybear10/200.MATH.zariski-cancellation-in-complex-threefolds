# Working recognition under the full split cubic initial-kernel hypothesis

**Status: synthesis of restricted written proofs, not unrestricted cancellation.**

The supplied split configuration now has a working proof covering every
projected graph degree. In each remaining case, the proof constructs an
invariant coordinate of the original polynomial four-ring, with a
polynomial inverse. A published regular-kernel theorem then identifies
the invariant ring with complex affine three-space.

This combines the actual projection results175--177, the low-graph
argument181, and the nonlinear arguments178--182. It inherits their
explicit assumptions and source dependencies. AI review and symbolic
identity tests do not constitute expert review or formal verification.

## 1. Exact theorem under investigation

Let
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W],\qquad E\in\operatorname{LND}_{\mathbb C}(B),
\qquad Eu=1,\qquad A=\ker E,\qquad B=A[u],\\
(\deg_E X,\deg_E Y,\deg_E Z,\deg_E W)=(1,1,2,2),\\
a=EX,\quad b=EY,\quad e=E^2Z/2,\quad f=E^2W/2 .
\end{gathered}
\tag{1}
\]
The four displayed generators must be actual polynomial coordinates.
The degree is degree in the slice parameter, not ordinary polynomial
degree or an adjoint-height measurement.

For an indeterminate \(\tau\) over \(A\), assume the full kernel of
\[
\theta_0:\mathbb C[\mathsf X,\mathsf Y,\mathsf Z,\mathsf W]
\longrightarrow A[\tau],\qquad
(\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
\longmapsto(a\tau,b\tau,e\tau^2,f\tau^2)
\]
is exactly
\[
\ker\theta_0=(\mathsf X\mathsf Z+\mathsf Y\mathsf W).
\tag{2}
\]
One vanishing relation \(ae+bf=0\) is not sufficient in place of
this full-kernel hypothesis.

Under (1)--(2), the combined working conclusion is
\[
\boxed{A\simeq\mathbb C^{[3]}.}
\tag{3}
\]
Consequently the given slice \(u\) belongs to a polynomial coordinate
system of \(B\), by the slice theorem. The proof does not presume that
fact at any intermediate generic-coordinate step.

## 2. Why the case split is exhaustive

The actual bad-coordinate partial in175 has nonzero cubic coefficient
\(N=[u^3](\partial_Z|_A)\), a locally nilpotent derivation of \(A\).
Its exact coefficient field is
\(L=\operatorname{Frac}(\ker_A N)\), and \(A_L=L[v]\) with \(Nv=1\).
The original polynomial inverse gives projected elements \(y,z,w\)
with \(\mathbb C(y,z,w)=L(v)\).

The whole-plane argument175, constant-projection exclusion176 and
quadratic-projection exclusion177 prove
\[
L[y]=L[v],\qquad y=\gamma v+\eta,\quad\gamma\in L^*,\qquad
\vartheta=P(y),\quad P\in L[U],\quad \deg P\le4 .
\tag{4}
\]
This is a statement over the exact field \(L\), not an original-ring
coordinate assertion.

There are two exhaustive graph ranges:

| Range | Original-ring construction | Written proof |
| --- | --- | --- |
| Degree at most one | A constant graph is excluded. In the linear case an actual split-preserving shear followed by a complex linear subtraction gives an invariant coordinate. | [Low graph181](split-low-degree-graph-three-good-recognition-pass181-working.md). |
| Degrees two through four, \(m_\rho=0\) after actual normalization | A polynomial equal to the coefficient \(m\) is an invariant coordinate; a companion gives both polynomial inverse orders. | [Normalization178](split-affine-graph-coefficient-normal-form-pass178-working.md) and [zero-slope construction179](split-rho-constant-potential-coordinate-pass179-working.md). |
| Degrees two through four, \(m_\rho\ne0\) after actual normalization | Exact field return forces \(m_\rho=d^2/(t+\nu)\); an actual linear reframe and a polynomial correction give an invariant coordinate with both inverse orders. | [Reciprocal rigidity180](split-nonzero-rho-slope-reciprocal-rigidity-pass180-working.md) and [reciprocal construction182](split-reciprocal-slope-invariant-coordinate-pass182-working.md). |

The last two rows are complementary cases of a coefficient in a field.
The revised180 proof explicitly supplies the coefficient-field gate
also when the graph has degree two. Its reciprocal argument uses all
three positive-degree pencil coefficients, not just the two highest
ones. The [nonlinear synthesis182](split-nonlinear-graph-recognition-synthesis-pass182-working.md)
records these details.

The first row does not assume the pure-eliminant conclusion proved
only for nonlinear graphs. It uses just the nonzero evaluated cofactor
and its two evaluated gradients. Its key exclusion uses the full
actual equality \(\mathbb C(y,z,w)=L(y)\), not a Jacobian alone.

## 3. The common recognition endpoint

Every row constructs an actual invariant coordinate \(I\in B\):
the coordinate map and its inverse are polynomial over \(\mathbb C\).
No inverse divides by the possibly nonunit original speed \(a\).
The nonzero scalar \(d\) used in the nonlinear coordinate formulas
and the low-graph shear is proved to lie in \(\mathbb C^*\).

The slice makes \(A\simeq B/(u)\) regular: \(Eu=1\) makes the
partial derivatives of \(u\) generate the unit ideal. Since \(EI=0\),
the nonzero derivation \(E\) is \(\mathbb C[I]\)-linear on
\(B=\mathbb C[I]^{[3]}\). The exact hypotheses of
[Bhatwadekar--Gupta--Lokhande, Theorem 3.5](https://arxiv.org/html/1501.01438v1)
therefore hold, giving \(A=\mathbb C[I]^{[2]}\).

These final recognition steps no longer require the general
three-good working theorem156. The earlier degree-two nice shear
remains a valid separate construction, but the revised argument uses
the direct invariant-coordinate endpoint instead.

## 4. Remaining obligations and verification limits

The full complex-threefold cancellation question is still unsolved
in this project. This result does not show that an arbitrary
presentation \(A[u]\simeq\mathbb C^{[4]}\) admits a frame satisfying
(1), let alone (2).

Within the two-linear/two-quadratic investigation157, a full
weight-four initial relation and a height-two initial kernel remain
separate unresolved configurations. The true minimum of total
\(E\)-degree may also exceed six; no upper bound of six has been proved.
The earlier supplied cusp configuration has its separate synthesis174,
not an unstated role in the present split proof.

The determinant factor \(Ny\) is retained throughout. Finite controls
check polynomial identities and include a formal degree-eight
field-extension example: nonzero Jacobian and the displayed differential
equations alone do not force the actual field equality needed here.
Such controls do not prove the universal field-degree lemma or certify
every retained hypothesis.

This synthesis does not add a new argument beyond the cited proofs.
No historical novelty clearance, expert certification, proof-assistant
verification, public claim, submission, or external contact is asserted.
The professor has not confirmed the corrected complex-threefold
interpretation of the original email.
