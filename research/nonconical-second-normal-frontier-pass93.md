# Double-fiber conormal rigidity and the remaining cubic configurations

The quadratic degree bound now supplies information beyond the
first normal layer. For a collapsed rank-one double fiber, it forces
a constant row or column direction in the quotient conormal matrix,
including the zero-transverse-speed-derivative case left open by the
first-layer calculation. In the cubic branch, saturated multiplicity
gives a finite free local normalization, while the support lattice
forces additional source gluing and, in specified cases, singular
base branches. These results narrow restricted cases without
excluding all fixed fibers.

The working cancellation question remains
\[
A[s]\simeq\mathbb C^{[4]}
\quad\Longrightarrow\quad A\simeq\mathbb C^{[3]}.
\tag{1}
\]
It is not solved here. The professor has not confirmed that this
complex-threefold formulation is the intended correction of the
email. The literal conclusion \(X\simeq\mathbb A^1\) has the wrong
dimension when r is greater than one. None of the restricted results
below supplies the missing arbitrary-action reduction.

## 1. The precise restricted setting

The inherited setting is an actual polynomial four-ring
\(B=A[u]=\mathbb C[x_1,x_2,x_3,z]\), with a sliced locally nilpotent
derivation E. The first three coordinates have vanishing second
E-derivatives, while \(E^2z=q\in\mathbb C^*\), and \(u=Ez/q\).
The retained original velocity Jacobian is nilpotent. The actual
highest-adjoint kernel is the specified polynomial plane
\(S=\mathbb C[s_1,s_2]\); it is not an arbitrary subring with the
same transcendence degree.

In the nonconical branch the good speeds are b in S cubed and
\(\Omega=\det[b,b_{s_1},b_{s_2}]\ne0\). The unresolved case has
nonconstant \(\Omega\). The actual coordinate completion gives
\(A=S[A_1,A_2,c]\), \(A_K=K[v]\), and relative degree d equal to
two or three. The function c has degree at most 2d. The quotient
to S is faithfully flat, and the primitive intrinsic Jacobian LND
N has kernel S. These conclusions and their assumptions are
established in [frontier92](nonconical-fixed-fiber-frontier-pass92.md)
and its linked original-coordinate proofs.

The unrestricted problem has not been reduced to this setting.
Even inside it, isolated rank drops and generically rank-one fixed
curves remain possible in the current argument.

## 2. Equality supplies local finiteness

The [flat-rank proof](nonconical-saturated-flat-rank-pass93.md)
establishes a general algebraic implication. For a Noetherian local
domain T with residue field k and fraction field F, and a flat
T-module M,
\[
\dim_k(M/mM)=\dim_F(M\otimes_TF)=n<\infty
\quad\Longrightarrow\quad M\simeq T^n.
\tag{2}
\]
Finite generation is a conclusion, not a hypothesis. Residue-basis
lifts give isomorphisms modulo every power of m. Generic coordinates
then lift compatibly to the completion of T, and faithful-flat ideal
contraction returns them to T. Krull intersection is used only in
the finite source module, not in M.[^completion]

For a common function U nonconstant on all components of a closed
fiber, the actual semilocal ring O' is flat over
\(T=(S[U])_{mS[U]}\). Its special dimension is
\(\sum_i\mu_i f_i\), with residue degrees
\(f_i=[\kappa(\mathfrak q_i):\mathbb C(\bar U_i)]\); its generic
dimension is \(\deg_vU\le2d\). Equality makes O' finite free.
Since O' is normal with fraction field K(v), it is exactly the
full integral closure of T in that field.

Every cubic profile of total multiplicity six saturates the bound:
all residue degrees equal one and the local model has rank six.
This includes (6), (5,1), (4,2), and (4,1,1). For the single
rank-zero multiplicity-six component, U can be c itself, and both
local residue fields are \(\mathbb C(\bar c)\). The profile (4,1)
has a separate weighted-degree condition explained in the proof.
None of these statements implies global finiteness of A over S[U]
or impossibility of the local extension.

## 3. Rank-one Artinian fibers and their normal action

The [curvilinear proof](nonconical-curvilinear-fiber-action-pass93.md)
uses actual local differential coordinates, with one base parameter
x and a second parameter y. The other base function has order
\(\mu\) in the DVR obtained by setting x to zero. Its Jacobian
field acts on the whole generic Artinian fiber T by
\[
0\ne\bar N(T)\subset\operatorname{Soc}(T),\qquad
\bar N(\mathfrak m_T)=0,\qquad \bar N^2=0.
\tag{3}
\]
The socle is the one-dimensional subspace annihilated by the
maximal ideal. This nonzero action is compatible with a zero
action on the reduced fiber. It can also coexist with a nonzero
first action on the normal space of the reduced component:
these are different quotients.

When both relative generators collapse, the reduced component is
an affine line and its cylinder is the actual linear plane
\(\mathfrak qB=(X,Y)\). Retraction at u=0 gives the global ideal
\(\mathfrak q=(F,G)\), where \(F=X-uEX\), \(G=Y-uEY\).
In degree two, \(N^3F=N^3G=0\) exactly. The
[first-layer proof](nonconical-collapsed-conormal-layer-pass93.md)
gives a constant good normal L with \(EL\in(X,Y)^2\), but its
extra second-order N-conclusion originally needed a nonzero
transverse speed derivative.

## 4. Double fibers remove the first-layer exception

The [second-normal-order proof](nonconical-double-fiber-normal-order-pass93.md)
uses the degree identities one order further when \(\mu=2\).
Choose local parameters x,y and actual coefficient parameter c,
so \(Nx=0\), \(Ny\equiv\gamma x\), and
\(Nc\equiv\delta x+\lambda y\) modulo the square of the normal
ideal. Multiplicity two makes \(\lambda\ne0\). If the y-coefficients
of F,G are b(c),e(c), the third-derivative product rule modulo the
cube of the ideal yields
\[
\gamma\ne0\quad\Longrightarrow\quad be'-eb'=0,
\qquad
C=\ell(c)\rho_0\ \text{or}\ C=\ell_0\rho(c).
\tag{4}
\]
Here C is the polynomial conormal matrix, and the indicated row
or column is constant. If \(\gamma\ne0\), the zero Wronskian
makes its kernel line constant. If \(\gamma=0\), the Jacobian
formula makes its column direction constant. The normal quadratic
remainder contributes nothing because the induced operator
\(\gamma x\partial_y\) has cube zero on homogeneous quadratics.

Some constant affine-linear good normal L consequently satisfies
both \(EL\in\mathfrak P^2\) and \(N(L-uEL)\in\mathfrak q^2\),
with no transverse speed-matrix rank assumption. The actual linear
plane makes \(\mathfrak q^2\) primary, justifying passage from
generic local to global ideal membership. At higher multiplicities,
the coefficient \(\lambda\) vanishes in this calculation, so the
same conclusion has not been established by this proof.

This does not produce an invariant coordinate. The polynomial
control \(D=p\partial_y-2y\partial_c\), \(f=p+y^2\) satisfies
\(Df=2py\ne0\), although \(Df\in(p,y)^2\) and \(D^3f=0\).
Further original-frame information is still needed to exclude
the fixed component or recognize A.

## 5. Cubic source gluing and singular-base restrictions

The [support proof](nonconical-reducible-ramification-support-pass93.md)
keeps the actual component Thom columns, their nonnegative entries,
and their support at a single point of the intermediate finite
curve Z. Its exact lattice equates the gcd of fiber multiplicities
with the lcm of normalized branch gcds. The underlying integral
topological diagram is the retained Kaliman argument, whose
general-cylinder applicability was checked previously.[^kaliman]

For (4,1) and (5,1), there is exactly one normalized base branch
and two source points, with indices (1,1) or (1,2). Both source
points must map to the same actual point of Z. For (4,2), the
only branch pattern is one split degree-two or degree-three cover
and one fully ramified degree-two branch. The support constraints
also narrow (4,1,1).

Two conditional exclusions identify missing geometric inputs.
If source normalization is injective over the fiber, every
component has multiplicity at most three. Separately, at a
rank-zero component a smooth analytic base branch cannot support
an unramified Thom entry one. Pullback of a base parameter has
order at least two by rank zero, while that entry gives order one.
Thus the (4,1)/(5,1) patterns with split-cover degree two and
the one-base-branch (4,1,1) pattern with cover degree three
require a singular base branch.

Finite reduced curve pinchings realize the required source gluing.
Replacing the base by a cusp preserves the normalized indices and
avoids the smooth-branch restriction. Exact integer bases also
satisfy the required multiplicities. These controls realize only
finite curves and integer data, not an exceptional surface, actual
Thom classes, an action, or a polynomial inverse frame. The tested
necessary conditions therefore do not yet give a contradiction.

## 6. Verification and the next proof obligation

The [canonical capture](verification-pass93-working.json) passes
two suites and three methods in 0.969877917 wall seconds and
0.563 unittest seconds. The standard-library checker tests finite
curve products, whole integer bases, gluing support, and negative
controls. The symbolic checker tests the third-derivative normal
identity, including rejection of an incorrect product-rule
coefficient. Neither checker proves the geometric lemmas.

The [proof audit](proof-audits-pass93-working.md) records separate
AI reconstructions and their scope. No human review, Lean
formalization, novelty certification, submission, or external
contact has occurred. Historical full regression and registry
counts are not current verification.

The next proof tasks are to exploit the constant conormal direction
using the complete original coordinate equations, or constrain
singular source-gluing configurations with more than lattice data.
The rank-six finite-free description may permit exact local algebra
analysis, but no classification has yet been proved. Arbitrary
sliced-action reduction remains a separate unsatisfied requirement.
See the [checkpoint](checkpoint-pass93-working.json) for the
retained state.

## Sources

[^completion]: The Stacks Project,
    [Noetherian local completion, 00MC](https://stacks.math.columbia.edu/tag/00MC),
    [flatness of completion, 00MB](https://stacks.math.columbia.edu/tag/00MB),
    and [Krull intersection, 00IP](https://stacks.math.columbia.edu/tag/00IP).
    The full displayed statements and proofs were read on September 14,
    2026. The linked algebraic proof specifies the finiteness distinctions.

[^kaliman]: Shulim Kaliman,
    [*Free C+-actions on C3 are translations*, final author PDF](https://www.math.miami.edu/~kaliman/library/Ka.invent.2004.c%2B.pdf),
    Notation 2.3, Proposition 3.2 and the related hypotheses and
    support arguments retained in
    [ramification92](nonconical-irreducible-fiber-ramification-pass92.md).
    The current support proof rereads that saved reconstruction.
    It does not claim a fresh complete audit of every primary
    analytic or topological dependency.
