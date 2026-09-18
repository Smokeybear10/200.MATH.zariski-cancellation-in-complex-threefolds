# A constant velocity determinant gives global recognition

In the actual three-good-coordinate constant-acceleration setting,
a nonzero constant velocity determinant makes the intrinsic free
action constructed in pass90 global. The published Kaliman--Saveliev
translation theorem then recognizes the kernel. This is an application
of that theorem to the new actual field, not a new theorem about all
free additive actions.

## 1. Exact hypotheses and conclusion

Let E be an actual locally nilpotent derivation in the original frame
\[
\begin{gathered}
B=\mathbb C[x_1,x_2,x_3,z],\qquad
E^2x_i=0\ (i\le3),\qquad E^2z=q\in\mathbb C^*,\\
u=Ez/q,\qquad Eu=1,\qquad A=\ker E,\qquad B=A[u],\qquad
b=(Ex_1,Ex_2,Ex_3)^t.
\end{gathered}
\tag{1}
\]
Use an actual highest-adjoint LND W and its intrinsic invariant
plane from [invariant-plane88](constant-acceleration-invariant-plane-pass88.md).
Retain all actual-ring hypotheses of that construction, so
\[
Wu=0,\qquad 0\ne W|A,\qquad
S=\ker(W|A)=\mathbb C[s_1,s_2],\qquad b\in S^3,
\qquad \Omega=\det[b,b_{s_1},b_{s_2}]\in\mathbb C^*.
\tag{2}
\]
The last condition is stronger than \(\Omega\ne0\).
The generators \(s_1,s_2\) are coordinates of the actual intrinsic
plane S; they are not assumed to form part of an ambient coordinate
system of B. Nor is u assumed to be an ambient coordinate before
recognition.

Under (1)--(2), there is \(t\in A\) such that
\[
\boxed{\qquad
A=S[t]=\mathbb C[s_1,s_2,t],\qquad
B=\mathbb C[s_1,s_2,t,u],\qquad E=\partial_u.
\qquad}
\tag{3}
\]
Thus the original action is a global translation in polynomial
coordinates. No explicit degree bound for these coordinates is asserted.

## 2. The actual free field is global

The complete [open free-field proof90](nonconical-open-free-derivation-pass90.md),
equations (1)--(8), constructs an actual derivation of \(A_\Omega\)
from its actual two-generator presentation. Its coefficients form a
unit ideal, and its generic action on the intrinsic polynomial line
proves local nilpotence. It establishes
\[
0\ne D\in\operatorname{LND}_{S_\Omega}(A_\Omega),\qquad
\ker D=S_\Omega,\qquad D(A_\Omega)A_\Omega=A_\Omega.
\tag{4}
\]
The later smoothness/cofactor conclusions in that note are not needed
here. Since \(\Omega\in\mathbb C^*\), the localizations in (4)
are exactly A and S. No multiplication by a denominator-clearing
factor is necessary. Consequently D is a nonzero global LND on A,
its kernel is S, and its image ideal is the whole ring A.

The unit image ideal says its complex additive action has no fixed
point. Stabilizers are algebraic subgroups of the additive group;
in characteristic zero there are no nontrivial finite stabilizers.
Thus this action is free. This does not assert that fixed-point-freeness
alone supplies a slice on an arbitrary affine variety.

## 3. The global geometric hypotheses are supplied by the cylinder

Put \(X=\operatorname{Spec}A\). The actual slice in (1) makes A
a finitely generated complex domain and identifies
\(X\times\mathbb A^1\) with \(\mathbb A^4\).
The hypersurface \(u=0\) is smooth: \(Eu=1\) expresses 1 as
the pairing of the original polynomial vector field with \(du\),
so the four partial derivatives of u do not vanish simultaneously.
Its coordinate ring is \(B/(u)\simeq A\). Hence X is a smooth
affine threefold.

On complex points, the product with \(\mathbb C\) deformation
retracts onto \(X\times\{0\}\). The cylinder is contractible,
so X is contractible as well. These are properties of the entire
threefold, not of an unverified principal open.

Kaliman--Saveliev Corollary 2.8(1) now applies to D: a free additive
action on a smooth contractible affine complex threefold is the
translation product with its affine quotient.[^ks]
Here that quotient is already \(\operatorname{Spec}S=\mathbb A^2\).
The equivariant product isomorphism therefore gives \(A=S[t]\)
with \(Dt=1\), and adjoining the original u proves (3).
No prior properness, retraction, or fiber-irreducibility hypothesis
is required by the stated corollary.

For comparison, its domination hypothesis in parts (2)--(3) is also
available: the smooth projection \(\mathbb A^4\to X\) restricts
to a dominant morphism from an affine linear three-plane by choosing
its tangent space complementary to the one-dimensional differential
kernel at any point. The source is \(\mathbb A^1\times\mathbb A^2\).
That extra route to identifying the quotient is unnecessary here,
because the actual S has already been identified.

## 4. Exact scope and source access

The global free-action gate was already retained in
[intrinsic quotient recognition](intrinsic-quotient-surface-pass.md)
and [the pass44 application](heisenberg-common-base-pass44.md).
The new input is that the actual pass90 field satisfies the gate
without localization when the determinant is a nonzero constant.
This is an additional recognized nonconical subcase, not a claim
of novelty for the published criterion.

If \(\Omega\) is nonconstant, (4) only gives a free action on
\(\operatorname{Spec}A_\Omega\). Its contractibility has not been
proved. Clearing denominators can introduce fixed points on
\(\Omega=0\); neither step permits the application above. The
[localized Weitzenbock boundary](homogeneous-speed-recognition-source-scope-pass90.md)
also shows why the local free action does not itself supply a
relative polynomial line. No recognition of arbitrary nonzero
\(\Omega\), universal frame existence, or general cancellation
is asserted here.

The complete saved quadratic-potential90 and final ten-equation
open-free90 proofs were read through EOF, as were the two retained
global applicability notes. No numerical test or modification of
pass89 or earlier artifacts is part of this corollary.

[^ks]: Shulim Kaliman and Nikolai Saveliev,
    [*C+-actions on contractible threefolds*, author-hosted final text](https://www.math.miami.edu/~kaliman/library/KaSa.michigan.2004.quotient.pdf),
    Corollary 2.8, printed p.6. Its full displayed statement and proof
    were freshly read, together with the displayed Theorem 2.7 proof
    and the introduction's scope. Part (1) invokes Kaliman's earlier
    Theorem 5.4(ii) under the smooth-quotient hypothesis, supplied by
    Theorem 2.7. No fresh full proof audit of that earlier theorem,
    the invoked topology, or other deeper dependencies is claimed.
    Properness, a section and irreducible fibers are not additional
    assumptions in Corollary 2.8(1).
