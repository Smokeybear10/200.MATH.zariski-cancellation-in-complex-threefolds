# Constant acceleration, fiber symmetries and the remaining coordinate problem

A nonzero constant acceleration produces an actual involution on every
original affine-three-space coordinate fiber. Its invariant ring is the
unknown threefold ring. This gives a precise conditional route to
cancellation, but the natural averaging and module-completion shortcuts
do not supply the needed coordinate change.

The unrestricted corrected complex-threefold cancellation problem is
not solved. The professor has not confirmed the correction, field or
dimension. The results below are private, AI-reviewed working mathematics,
without formal verification, expert review or an established novelty claim.

## 1. The actual reduction

Let E be a locally nilpotent derivation of an actual polynomial four-ring
with a global slice. Suppose one original coordinate z satisfies
E squared z=q, a nonzero complex constant. Set
\[
B=A[u]=\mathbb C^{[4]},\qquad A=\ker E,\qquad
u=E(z)/q,\qquad r=z-(q/2)u^2\in A.
\tag{1}
\]
The [complete reduction](constant-acceleration-involution-boundary-pass87.md)
does not bound the E-degrees of the other three coordinates. For each
complex lambda the coordinate fiber and its involution are
\[
\begin{gathered}
C_\lambda=B/(z-\lambda)=A\oplus Au\simeq\mathbb C^{[3]},\qquad
u^2=2(\lambda-r)/q,\\
\iota|_A=\operatorname{id},\qquad\iota(u)=-u,\qquad
C_\lambda^\iota=A.
\end{gathered}
\tag{2}
\]
All rings in (2) are actual global rings. The fixed scheme is the
nonempty smooth surface Spec A/(r-lambda). The original coordinate
partial, evaluated at u=0, gives a derivation D of A with D(r)=1.
This proves smoothness, not that D is locally nilpotent or that the
surface is an affine plane.

## 2. An exact recognition gate, not an automatic solution

For one fixed fiber, the
[odd-generator theorem](coordinate-odd-generator-recognition-pass87.md)
proves the following equivalence and implication:
\[
u\text{ is a coordinate of }C_\lambda
\quad\Longleftrightarrow\quad
\iota\text{ is linearizable}
\quad\Longrightarrow\quad A\simeq\mathbb C^{[3]}.
\tag{3}
\]
Here coordinate means that u can be completed to actual polynomial
generators, not merely that u generates a free odd module.

If u is a coordinate, set t=u squared. The presentation
C_lambda=A[U]/(U squared-t) gives A/(t-c)=C squared for every complex c,
including c=0. The generic fiber becomes a polynomial plane after
the separable extension adjoining a square root of t. Kambayashi's
affine-plane-form theorem descends that generic plane. The affine-plane-
fibration theorem over the PID C[t] then gives A=C[t,p,q_0] and
C_lambda=C[u,p,q_0]. Exact theorem statements and read limits are
recorded in the linked proof.[^forms] [^fibration]

Conversely, a linearization must be a reflection because the fixed
scheme has dimension two. In reflection coordinates its odd generator
and u differ by a unit of the invariant ring, hence by a nonzero
constant. Thus (3) is an equivalent formulation of the missing
linearization premise, not a proof of that premise.

Conjugacy of one fiber involution into the tame automorphism group
also suffices, by Lamy--Przytycki's finite-subgroup theorem.[^tame]
The common cylinder does not automatically supply that conjugacy.
Its dilation u to a scalar times u does not preserve a fixed z-fiber
except at the appropriate roots of unity.

## 3. Exact obstructions to the tempting shortcuts

The [fiber-row proof](constant-acceleration-fiber-row-pass87.md) writes
any actual fiber coordinates as x_i=P_i+uQ_i with coefficients in A.
Their odd row satisfies
\[
(Q_1,Q_2,Q_3)A=A,\qquad
du(Q)\equiv1\pmod u,\qquad (JQ)Q\equiv0\pmod u.
\tag{4}
\]
These follow from the full difference ideal (u) and the involution
identities. They do not turn a matrix completion over A into an
ambient polynomial coordinate change.

An actual frame with E=partial_u is
x=u, y=(1+u squared)a+ub, z_0=ua+b, W=c+u squared.
Both polynomial inverse orders are known. On W=lambda its standard
Reynolds map, which is also a particular invariant-matrix completion,
is (u,(1+u squared)a,b), with Jacobian 1+u squared. It is not invertible.
The original involution is nevertheless tame and linearizable.
The associated row derivation is not locally nilpotent either.

The [primary-source audit](involution-reynolds-source-gate-pass87.md)
checks Jurkiewicz's exact sufficient condition: after fixing the origin,
all nonlinear homogeneous degrees must lie between d and 2d-2 for
some d at least two.[^band] This control has degrees 2, 3 and 4,
so it does not satisfy that condition in its supplied frame. Finite
polynomial degree alone is not the condition.

A separate [actual averaging control](constant-acceleration-averaging-obstruction-pass87.md)
reuses an earlier SL2 frame. Averaging the actual coordinate partial
with its conjugate gives
\[
V=\partial_z-zu\partial_u+zy\partial_y,\qquad
V^n(y)=P_n(z)y,\qquad P_{n+1}=P_n'+zP_n.
\tag{5}
\]
The monic degree of P_n is n, so V is not locally nilpotent. It
still sends z to one. Both controls have additional coordinates
of E-degree greater than one. They do not refute a theorem requiring
three E-affine companion coordinates.

## 4. Stronger frame and the next proof obligation

With the additional hypotheses E squared x_i=0 for all three
companions, put P=E(x_1,x_2,x_3,z) and J=Jac P. The flow is
x+tP+(q/2)t squared e_4, so its Jacobian is I+tJ. This gives
J to the fourth=0, E(J)=-J squared and the exact adjoint-column
formula (-1)^j j! J^j e_i. In particular J cubed e_4=0 and the
third adjoint of the original z-partial vanishes.

These stronger assumptions do not restore the nice-action rank
bound. The actual triangular frame
(u,t+ur,c+ut,r+u squared) has Jacobian rank three, with J cubed
nonzero. Thus the all-nice recognition theorem cannot be applied
through an unproved rank reduction. The
[stronger-frame proof](constant-acceleration-three-good-frame-pass87.md)
and its exact checker record the valid identities and this counterexample.

The original z-partial has the exact expansion
T restricted to A=D_0+uD_1+u squared D_2 and T(u)=h_0+uh_1.
An actual conjugation, invariant scaling and specialization prove
that D_2 is an LND of A, possibly zero, with D_2(r)=-qh_1.
This uses the retained highest-coefficient mechanism, not averaging.
In the rank-three control it is nonzero but kills r. Consequently
this construction does not automatically give the critical-value
function an LND slice.

The rank of J is one more than the rank of the differentials of
the three invariant velocities: contraction with E separates du
from those differentials. Their image therefore has dimension at
most two. A useful next proof task is to determine whether that
actual invariant image provides polynomial coordinates or a
controlled quotient, retaining its global fiber and generation
hypotheses. Its low dimension alone is not a recognition theorem.

## 5. Verification and status

The [print-only targeted runner](run_targeted_pass87.py) executes three
independent exact checkers, one method each. They cover actual inverse
pairs and the specified averaging, row and stronger-frame controls.
Finite checks do not establish the universal assertions or the
external fibration theorems. The [capture](verification-pass87-working.json)
and [proof audit](proof-audits-pass87-working.md) distinguish those scopes.
The [checkpoint](checkpoint-pass87-working.json) records immutable evidence.

The remaining obligation is still the full cancellation implication.
Even unconditional recognition of the constant-acceleration subclass
would require a further argument, and would not produce such a
coordinate for an arbitrary sliced action. No external contact,
submission, public posting or novelty certification is included.

## Sources

[^forms]: Dutta, Gupta and Lahiri, [*On Separable A2 and A3-forms*, Theorem 2.8](https://arxiv.org/html/1802.03777v2), quoting Kambayashi's separable affine-plane-form theorem. The quoted statement was checked, not the original 1975 proof.

[^fibration]: Babu and Das, [*Structure of A2-fibrations having fixed point free locally nilpotent derivations*](https://arxiv.org/pdf/2001.07632v5), definition on page 1 and PID consequence of Sathaye and Bass--Connell--Wright on page 9 before Theorem 4.7. No relative LND premise is used from their separate Theorem 4.7.

[^tame]: Lamy and Przytycki, [*Almost a building for the tame automorphism group*](https://www.math.univ-toulouse.fr/~slamy/stock/translation_immeuble.pdf), Corollary B, statement page 2 and short proof page 30; author translation of the 2021 paper. Finite tame subgroups, not all polynomial involutions.

[^band]: Jurkiewicz, [*Linearizing some Z/2Z actions on affine space*](https://www.numdam.org/item/CM_1990__76_1-2_243_0.pdf), Compositio Mathematica 76 (1990), 243--245, theorem case 3. All three pages were visually checked; the original paper also gives a noninvertible Reynolds-map example for a linearizable action.
