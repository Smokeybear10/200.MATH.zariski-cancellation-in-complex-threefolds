# A branch-count obstruction for every ambient additive extension

For the fixed conductor surface, the nonzero-conductor-speed
qualification in the preceding ambient theorem can be removed.
A topological branch count forces the ambient invariant curve to
have a node. Primitive ambient extensions then necessarily have
nonzero speed, so the exact residue theorem applies to them.

This is a conditional statement about a hypersurface presentation.
No such presentation is constructed or excluded. The original
complex threefold cancellation problem remains unresolved.

## 1. Ambient quotient branch counts

Let W=C[X,Y,Z], let E be a nonzero LND, and write
C=ker E=C[f,g]. Put X=Spec W and Y=Spec C.
Choose a reduced curve Gamma in Y so that
X minus pi^{-1}(Gamma) is a product with an affine line over
Y minus Gamma. Enlarge Gamma if needed to include a specified
invariant prime divisor.

Kaliman's Lemmas 2.1-2.2 give irreducible reduced exceptional
surfaces and the factorization
\[
\pi^{-1}(\Gamma)\xrightarrow{\kappa}Z
 \xrightarrow{\theta}\Gamma,
\tag{1}
\]
where theta is finite by Proposition 3.2(i). Choose a finite
set Sigma in Gamma containing its singularities and every
exceptional value needed so that Gamma*, Z*, and their product
exceptional surface are smooth, as in the source's Notation 2.3.[^1]

For b in Sigma, let:

- r_b be the number of analytic branches of the full Gamma at b.
- q_b be the number of points of the normalization of Z over b.
- c_b be the number of irreducible components of the reduced
  actual quotient fiber pi^{-1}(b).

These are not multiplicities. The curve fiber is pure
one-dimensional: the two invariant coordinate equations define
a height-two complete intersection in the regular threefold.
The assertion is
\[
c_b=q_b-r_b+1.
\tag{2}
\]

Here is a proof retaining the support decomposition. Use rational
coefficients for ranks. For an affine smooth curve N and a finite
set P, the small positively oriented loops around P are linearly
independent in H_1(N minus P). This follows from the exact
sequence of the pair and H_2(N)=0. Consequently the subspaces
V_b of H_1(Z*) spanned by the q_b normalized puncture loops,
and W_b of H_1(Gamma*) spanned by the r_b base branch loops,
have those exact dimensions. Their sums over b are direct,
even if the affine normalizations have positive genus or more
than one point at infinity.

The finite map theta induces on these subspaces
\[
\theta_{1,b}:V_b\longrightarrow W_b,
\qquad \beta_a\longmapsto e_a\gamma_{\theta(a)},
\tag{3}
\]
with positive integer ramification indices. It is surjective
over Q, since each normalized base branch has a preimage.
No unramified assumption is used.

Set X*=X minus pi^{-1}(Sigma), Y*=Y minus Sigma,
Xcheck=X minus pi^{-1}(Gamma), Ycheck=Y minus Gamma.
The diagram of pair sequences and Thom maps in Kaliman's
Proposition 3.2 gives
\[
0\longrightarrow H_3(X^*)\xrightarrow{\varphi'}
 H_1(Z^*)\xrightarrow{\psi'}H_2(X_{\rm check}),
\]
\[
0\longrightarrow H_3(Y^*)\xrightarrow{\varphi}
 H_1(\Gamma^*)\xrightarrow{\psi}H_2(Y_{\rm check}),
\tag{4}
\]
with theta_1 as the middle vertical map and an isomorphism
on the right, induced by the product complement.
The zero on the left uses H_3(Ycheck)=0 for a smooth affine
complex surface and the product identification for Xcheck.

By Lemma 3.1 the image of the small sphere about b under
varphi is the diagonal vector
\(\gamma_b=\sum_{j=1}^{r_b}\gamma_j\).
The sphere classes form a basis of H_3(Y*) since Y=C^2.
The direct puncture-loop decomposition therefore gives
\[
(\operatorname{im}\varphi)\cap W_b=\mathbb Q\gamma_b.
\tag{5}
\]
Commutativity, exactness, and the right-hand isomorphism give
\[
\ker\psi'\cap V_b
 =\theta_{1,b}^{-1}(\mathbb Q\gamma_b),
\quad
\dim(\ker\psi'\cap V_b)=q_b-r_b+1.
\tag{6}
\]

On the other side, X=C^3 has H_3(X)=H_4(X)=0. The pair sequence,
excision, and Thom isomorphism along the smooth parts of the
curve fibers give
\[
H_3(X^*)=H_4(X,X^*)
 \simeq\bigoplus_{b\in\Sigma}\mathbb Q^{c_b}.
\tag{7}
\]
Removing the finite singular and intersection points of the
fiber curves does not change relative degree four; the result
counts irreducible curve components, not connected components.

The b-summand of (7) maps under varphi' into V_b. Indeed its
cycle can be supported in a sufficiently small neighborhood of
pi^{-1}(b); the functorial Thom map followed by kappa then lies
in puncture neighborhoods over b. This is the excision-support
argument in the proof of Proposition 3.2, with base-point
support retained. Since varphi' is injective and the V_b sum
is direct, its image inside V_b has dimension exactly c_b.
Combining (4), (6), and (7) proves (2).

### An individual-component consequence

Fix one irreducible component Gamma_i through b.
Let r_{i,b} count its analytic branches there, and let q_{i,b}
count normalization points of its corresponding Z_i over b.
Every other normalized base branch has at least one source
preimage, so
\[
q_b-q_{i,b}\ge r_b-r_{i,b}.
\]
Therefore
\[
c_b\ge q_{i,b}-r_{i,b}+1.
\tag{8}
\]
Other plinth components passing through b cannot weaken this
lower bound. No assumption that Gamma_i is disjoint from the
rest of the exceptional curve is hidden in (8).

The branch count is a deduction from the cited quotient
homology diagram, not an asserted new topological principle.
Ramification and nonreduced quotient fibers are allowed.

## 2. Applying the count to the actual conductor surface

Use the complete fixed data of
[the preceding residue proof](ambient-residue-obstruction-pass32.md):
\[
B_0=\mathbb C[u,y,z]/((u-1)(u-i)z-y(y-1)),\quad d=u^4-1,
\]
\[
R=B_0\times_{\mathbb C[t]^6}\mathbb C[t]^3,\quad
M=\mathbb C u+d\mathbb C[u],\quad T=\mathbb C+d\mathbb C[u],
\quad\operatorname{LND}(R)=M\delta_0.
\tag{9}
\]
The actual root pairings and scaled parameters are unchanged.
The normalization has two split fibers over 1 and i, ordinary
fibers elsewhere, and precisely six conductor lines over
1,-1,i,-i. The pinch replaces those six lines by three disjoint
affine lines.

Suppose R=W/(F) and an ambient LND E induces a nonzero LND on R.
As before E(F)=0 and C=ker E=C[f,g].
Write F=P(f,g) and set S=C/(P), embedded in T.
The gcd argument of the preceding proof gives
\[
E=h(f,g)J,\qquad J=\operatorname{Jac}(f,g,\cdot)
\quad\text{primitive and locally nilpotent}.
\tag{10}
\]
A primitive J cannot vanish identically modulo F, since that
would make all its ambient coefficients divisible by F.

The normalization of S is C[t], with t=phi(u) polynomial,
by finiteness inside C[u], Lüroth's theorem, and constant units,
exactly as in the preceding proof. This argument does not
require nonzero conductor speed. All elements of S take the
same value at the four conductor roots. Thus all three
singular lines of R map to one point b of Gamma_i=Spec S.

The algebraic closure of Frac S in Frac R=C(u,y) is C(u).
Accordingly the normalization of the intermediate curve Z_i
in (1) is the u-line. This identifies its branch count with
the actual normalized invariant map, without presuming Z_i
itself is the full invariant curve Spec T.

Let n be the number of additional distinct u-values outside
{1,-1,i,-i} that map to b. The fibers there are ordinary
affine lines, because the only split fibers of B_0 lie at
conductor roots. The actual reduced quotient fiber is therefore
three conductor lines and n additional disjoint affine lines:
\[
q_{i,b}=4+n,\qquad c_b=3+n=q_{i,b}-1.
\tag{11}
\]
Nilpotent structure and ramification do not change these counts.
The actual ambient fiber equals this fiber of R over b,
because its two base-coordinate equations include F=0.

Combining (8) and (11) forces
\[
r_{i,b}\ge2.
\tag{12}
\]
In particular the plane curve Gamma_i is not smooth or unibranch
at b, irrespective of the conductor speed of E or J.

## 3. The node and primitive speed are now forced

At a point x of any conductor line, the actual hypersurface
F=0 has an ordinary double crossing. Its quadratic initial
form has rank two. Since P has at least two branches at b,
its multiplicity is at least two.

Writing F=P(f,g) in the ambient regular local ring shows that
P has multiplicity exactly two and that the linear parts of
f-f(x),g-g(x) are independent. Otherwise the quadratic initial
form of F would vanish or have rank at most one. The quadratic
part of P also has rank two. Thus Gamma_i has an ordinary node
at b, and (f,g) has differential rank two at every conductor
point. In particular J is nonzero at all these points.

Every singular point of Gamma_i pulls back to singular points
of R by the chain rule, while R maps surjectively to Gamma_i
and has no singular points outside its conductor. Therefore
b is the only singular point of Gamma_i.

The restriction of J belongs to M delta_0 by the complete
intrinsic classification. Since it is nonzero on the conductor,
its common translation speed is nonzero. The entire
pass-32 residue theorem can now be applied to J, giving
\[
S=\mathbb C+d\mathbb C[u^2],
\qquad J|_R=\kappa u\delta_0,\quad\kappa\ne0.
\tag{13}
\]
Finally h restricts to an element of S. Absorb kappa in it.
For every ambient E inducing a nonzero action, with no
conductor-speed restriction, one obtains
\[
E|_R=uH(u^2)\delta_0,\qquad
0\ne H(u^2)\in\mathbb C+d\mathbb C[u^2].
\tag{14}
\]
The conductor value of H is now allowed to be zero.
Every extendable multiplier is odd.

## 4. A conditional exact dichotomy for extendable actions

Fix a particular hypersurface presentation of R, without
asserting that any exists. If one nonzero surface LND has an
ambient LND extension, primitive normalization produces an
extension of u delta_0 by (13). Conversely every H in S
lifts to an ambient invariant, so an invariant replica of
that extension lifts uH delta_0.

Consequently, for that presentation, the set of surface LNDs
with ambient LND extensions is either {0} or exactly
\[
\{uH(u^2)\delta_0:H(u^2)\in\mathbb C+d\mathbb C[u^2]\}.
\tag{15}
\]
This is exactly the odd-multiplier subspace of M delta_0.
The proof does not choose between the two alternatives and
does not produce an embedding.

## 5. Divergence-free lifts at every finite order still do not suffice

Choose the actual invariant G=du in T. The Hamiltonian result
of [the divergence note](divergence-torsion-pass32.md) supplies,
in every hypothetical hypersurface presentation, a divergence-free
polynomial derivation K preserving F exactly and restricting to
\[
D_{\rm even}=dG'(u)\delta_0
 =(u^4-1)(5u^4-1)\delta_0.
\tag{16}
\]
The multiplier is nonzero and even, so (14) excludes every
ambient LND extension of this action. Yet K is an explicit
rescaled ambient Jacobian field, and the
[finite-thickening criterion](finite-thickening-algebraization-pass31.md)
makes K locally nilpotent on every W/(F^N).

Thus, conditional on the presentation, this particular action
has exact divergence-free lifts and compatible additive
actions at every finite order, but no additive ambient lift
at all. This is stronger than showing that one chosen
divergence-free lift is not an LND.

It is not an exhibited hypersurface counterexample, since
the presentation remains unknown. The compatible odd action
u delta_0, the three-generator question, and the full
cancellation problem remain unresolved. No novelty, expert
review, or proof-assistant certification is claimed.

## Finite exact controls and reconstruction scope

The standalone [all_speed_ambient_checks_pass33.py](all_speed_ambient_checks_pass33.py)
checks weighted branch matrices, the individual-component bound,
distinct-root component counts, quadratic-rank constraints, the even
Hamiltonian identities and the exact odd replica subspace. It imports
only unittest and SymPy. The initial targeted run passed six methods
in 0.059 seconds. A separate full-file audit reran all six successfully
in 0.061 seconds.

Two other agents independently reconstructed the full written argument,
including the support decomposition, other exceptional components,
normalization field identification, node forcing and fixed-presentation
dichotomy. Their agreement is AI review, not human expert review or
proof-assistant verification. The finite matrix controls do not prove
the universal homological assertions.

```
/opt/anaconda3/bin/python research/all_speed_ambient_checks_pass33.py
```

## Primary source and proof scope

[^1]: Shulim Kaliman, [*Free C+-actions on C3 are translations*, final author version](https://www.math.miami.edu/~kaliman/library/Ka.invent.2004.c%2B.pdf), Lemmas 2.1-2.2, Notation 2.3, Lemma 3.1 with proof, and Proposition 3.2(i) with its homology diagram and excision-support proof, printed pp. 2-6. The source statements were directly read. The ambient hypotheses are X=C^3 and Y=C^2; no freeness assumption is imported. Formula (2) is reconstructed above from the diagram, not quoted as the printed proposition. The separate three-variable polynomial-kernel, primitive Jacobian, dualizing-residue, and invariant-ring inputs are recorded with proofs and exact source scope in the linked pass-32 notes.
