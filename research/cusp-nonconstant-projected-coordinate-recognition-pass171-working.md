# Recognition of the nonconstant-y, nonzero-r cusp branch

Status: synthesis of retained working proofs, pending saved-source review.
This note records the exact case split closed by the new three-good
coordinate change. It does not solve all cusp charts or unrestricted
complex-threefold cancellation. In particular the remaining constant-y
and zero-r cases cannot be dropped.

## Statement and actual hypotheses

Retain the full actual cusp setup159:
\[
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad
(\deg_E X,\deg_E Y,\deg_E Z,\deg_E W)=(1,1,2,2),
\qquad \ker\theta_0=(XZ-Y^3).
\]
Here the last equality is the full weighted initial kernel, not merely
one relation among leading coefficients. Use exactly the selected
derivation \(N=[u^3](\partial_Z|_A)\), the field
\(L=\operatorname{Frac}(\ker_A N)\), and the whole line \(A_L=L[v]\)
with \(Nv=1\). The projected coordinates and chart coefficients are
those of159, including
\[
L[y,\vartheta]=L[v],\qquad
r=k_\rho,\qquad
0\ne \Phi-m\in L[U,V],\qquad \deg\Phi\le4.
\]

Under the retained working results below, the additional hypotheses
\[
r\ne0,\qquad y\notin L
\]
imply \(A\simeq\mathbb C^{[3]}\).
These are hypotheses on the specified actual chart; no arbitrary
coordinate frame is asserted to satisfy them.

## Exhaustive case split

The nongraph exclusion161, using its restriction160, rules out
\(\deg_v y\ge2\) when \(r\ne0\). Since \(y\notin L\), it follows that
\(y\) is an affine parameter for \(L[v]\). Thus
\[
\vartheta=P(y),\qquad P\in L[U],\qquad
G=V-P(U)
\]
generates the entire evaluation kernel in \(L[U,V]\).
The zero polynomial \(P\) is permitted in the first row below.
Because \(G\mid\Phi-m\), one has \(\deg G\le4\); thus \(P\) has
degree at most four, with no assumption about its coefficients'
dependence on \(\rho\).

The selected-factor result159 gives
\(\Phi-m=\lambda G+G^2H\), where \(\lambda\in L^*\).
If \(H\ne0\), its exact case split allows only constant \(y\), or
a quadratic graph in the fixed axes. The former is excluded by our
hypothesis; the latter is excluded by169. Therefore \(H=0\) in
every case here. This uses169 as a theorem input, not a consequence
of the new coordinate change.

| Degree of \(P\) | Working resolution |
| --- | --- |
| At most two, including \(P=0\) | The new pure-graph three-good reframe171 has a global polynomial inverse and places three actual coordinates in \(\ker E^2\). Retained recognition156 applies. |
| Three | The cubic field-forcing result167 and the global invariant coordinate168 recognize the branch. |
| Four | The quartic field-return theorem166 forces the condition in165, whose global invariant coordinate recognizes the branch. |

The last two rows retain their actual coefficient-forcing arguments.
Their rationality and integration conclusions are not assumptions
transferred to the first row. The first row does not require
\(p_0\in K[\rho]\) to have degree at most one, which was the extra
condition in170.

The table is exhaustive because the degree bound came from the
nonzero relation and the full selected kernel. The recognition
endpoints in its last two rows use the retained published
regular-kernel theorem. The first row uses the separately recorded
three-good working theorem, including its stated dependencies.
Agreement of these routes is not an independent proof of all their
historical inputs.

## What remains

Within the actual cusp setup159, any unrecognized branch must now
satisfy
\[
r=0\quad\text{or}\quad y\in L.
\]
This is a necessary restriction on the remaining cases, not proof
that they occur or that they are counterexamples. The zero-r reduction160
already provides generic affine parameters, but does not by itself
give integral recognition. The nonzero-r constant-y case can have
extra factors and was excluded from the argument above.

The other initial configurations and higher possible minimum E-time
profiles remain separate. No theorem here bounds an arbitrary
action's minimum profile by \((1,1,2,2)\), and no theorem supplies
this cusp initial form for every action.

## Sources and evidence

1. [Actual cusp chart159](cusp-generic-chart-first-reductions-pass159-working.md) and [selected-factor reduction159](cusp-generic-selected-factor-reduction-pass159-working.md).
2. [Nongraph restriction160](cusp-nongraph-quartic-restriction-pass160-working.md) and [nongraph exclusion161](cusp-nongraph-quartic-exclusion-pass161-working.md).
3. [Quadratic extra-factor exclusion169](cusp-quadratic-extra-factor-exclusion-pass169-working.md).
4. [Pure-graph three-good reframe171](cusp-pure-quadratic-three-good-recognition-pass171-working.md), with [three-good recognition156](three-good-all-degree-recognition-pass156-working.md).
5. [Cubic field forcing167](cusp-cubic-field-forcing-pass167-working.md) and [global cubic coordinate168](cusp-cubic-global-coordinate-pass168-working.md).
6. [Quartic criterion165](cusp-quartic-weight-four-sufficiency-pass165-working.md) and [actual field forcing166](cusp-quartic-actual-field-recognition-pass166-working.md).
7. [Zero-r generic reduction160](cusp-zero-r-generic-graph-pass160-working.md).

This synthesis has no new checker or test execution. The171 finite
checks concern the new pure-graph shear, not every row of this table.
The saved source statements and hashes were checked for the case split;
this is not a recursive audit of every dependency. There is no human
expert review, proof-assistant certification, or novelty clearance.
No frozen170 or earlier mathematical artifact is changed.
