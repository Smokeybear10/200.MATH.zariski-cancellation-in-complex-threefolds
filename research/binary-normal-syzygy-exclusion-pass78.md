# The original tangent-plane invariant excludes a proper binary parameter ideal

In the nonlinear ternary-velocity-cone branch with a supplied
good partial, the actual binary parameters generate the unit ideal.
The proof uses an original polynomial common invariant obtained
from the binary tangent-plane normal. Faithful flatness contracts
its linear relation to the intrinsic plane. The complete
intersection associated graded then gives a contradiction on a
whole parameter component, without assuming that component is
reduced.

This removes the proper-parameter branch. It does not construct a
good partial or a nice frame for an arbitrary sliced action, and
it does not prove primitive fixed-point-freeness or cancellation.

## 1. Exact original-action inputs

Retain the actual nonlinear supplied-good branch of
[binary descent77](nice-binary-parameter-descent-pass77.md):
\[
\begin{gathered}
B=\mathbb C[x_1,x_2,x_3,w]=A[s],\qquad
E=P\cdot\partial\in\operatorname{LND}(B),\quad Es=1,\quad E(P)=0,\\
T=\partial_w,\qquad [E,[T,E]]=0,\qquad Q=[T,E],\\
P_i=h_i(p,q)\quad (i\le3),\qquad
p,q\in A\setminus\{0\},\qquad \gcd_B(p,q)=1.
\end{gathered}
\tag{1}
\]
The three binary forms \(h_i\) are linearly independent over
\(\mathbb C\), homogeneous of one degree \(e\ge2\), and have
no common binary factor. They and the parameters are actual
polynomials supplied by that theorem, not newly chosen rational
coordinates.

The common-invariant and intrinsic quotient inputs are
\[
\begin{gathered}
Qp=Qq=0,\qquad 0\ne\delta=Q|_A=hD,\\
S=\ker D=\ker\delta\simeq\mathbb C[u,v],\qquad
p,q\in S,\qquad S\subset B\text{ faithfully flat}.
\end{gathered}
\tag{2}
\]
Here D is the primitive intrinsic locally nilpotent derivation.
These are the already established actual hypotheses of the
[conormal77](binary-conormal-obstruction-pass77.md) and
[regular-derivative78](binary-regular-derivative-exclusion-pass78.md)
arguments. In particular, faithful flatness is not inferred from
coprimality. The essential global plane and faithful-flatness
input is the complete
[intrinsic quotient theorem](intrinsic-quotient-surface-pass.md),
applied to the actual primitive D on A with its supplied cylinder
\(A[s]=B\). It is not a hypothesis on an arbitrary rational
quotient or merely a localized field action.
Nonvanishing of delta throughout this nonlinear branch
is also proved in the
[Wronskian note](binary-wronskian-derived-rank-pass78.md).

Suppose for a contradiction that \(I=(p,q)B\ne B\).
The complete finite-pair argument of conormal77 then makes p,q
algebraically independent. Alternatively, that independence may
be included among the hypotheses of the proper-branch proof below.
There is no algebraic-independence assumption on all binary pairs
in the final conclusion.

## 2. An actual polynomial tangent-plane invariant

Use independent formal variables \(\xi,\eta\), and write
\(\mathcal H=(h_1,h_2,h_3)^t\). Define the polynomial normal
\[
N=\mathcal H_\xi\times\mathcal H_\eta
  =(K_{23},-K_{13},K_{12})^t,
\qquad K_{ij}=\det\operatorname{Jac}_{\xi,\eta}(h_i,h_j).
\tag{3}
\]
Its three components are homogeneous of the same positive degree
\(d=2e-2\), and are linearly independent over \(\mathbb C\).
Here is the full independence gate. A nonzero relation between
the three pairwise Jacobians is a nonzero element of
\(\bigwedge^2\mathbb C^3\). Every such element in dimension
three is decomposable, so the relation would give
\(\det\operatorname{Jac}(F,G)=0\) for two independent constant
linear combinations F,G of the \(h_i\). They are homogeneous
of degree e. Euler's identities show that both ordinary partials
of F/G vanish; characteristic zero gives \(F/G\in\mathbb C\),
a contradiction. This is the elementary argument of Section 2
of regular-derivative78, now used for the normal itself.

The cross product annihilates \(\mathcal H_\xi\) and
\(\mathcal H_\eta\). Euler's identity
\(e\mathcal H=\xi\mathcal H_\xi+\eta\mathcal H_\eta\)
therefore gives \(N\cdot\mathcal H=0\) as well.
Consider the original polynomial
\[
c=\sum_{i=1}^3N_i(p,q)x_i\in B.
\qquad Ec=Qc=0,\qquad c\in S.
\tag{4}
\]
Indeed E and Q kill every coefficient \(N_i(p,q)\) by
(1)--(2). Their values on the three original coordinates are
respectively \(\mathcal H(p,q)\) and
\(\mathcal H_\xi(p,q)Tp+\mathcal H_\eta(p,q)Tq\).
Both dot products with N vanish. Since \(Ec=0\), c belongs
to A; since \(Qc=hDc=0\) with h nonzero in a domain, it
belongs to S. No rational invariant is promoted to a polynomial
here: the expression defining c already lies in B.

Let \(\mathfrak a=(N_1(p,q),N_2(p,q),N_3(p,q))S\).
Equation (4) puts \(c\in\mathfrak a B\cap S\).
Faithful flatness contracts this ideal exactly to
\(\mathfrak a\). Thus there exist actual \(a_1,a_2,a_3\in S\)
such that
\[
c=\sum_iN_i(p,q)a_i,\qquad
\sum_iN_i(p,q)(x_i-a_i)=0\quad\text{in }B.
\tag{5}
\]
The three normal entries need not generate the unit ideal;
no greatest-common-divisor or Bezout inference is being made.
There is also no need to divide their common binary factor.

## 3. The whole associated graded forces three constant residues

Choose a minimal prime \(\mathfrak n\) of I. Coprimality
in the polynomial UFD B excludes height one, and the height
theorem gives \(\operatorname{ht}\mathfrak n=2\).
Set \(L=B_{\mathfrak n}\), \(I_L=(p,q)L\), and
\(R_0=L/I_L\ne0\). The regular local ring L has dimension
two, and p,q are a parameter regular sequence. They need not
be a regular system of parameters. The exact regular-sequence
associated graded is
\[
\operatorname{gr}_{I_L}L\simeq R_0[\xi,\eta],
\qquad \xi=\operatorname{in}(p),\quad
\eta=\operatorname{in}(q).
\tag{6}
\]
The coefficient algebra R0 retains all its possible nilpotents.
This is the same selected regular-sequence result used in
regular-derivative78, not a choice of a coefficient field.[^graded]

Take the degree-d part of (5) in (6). Since each normal entry
is homogeneous of degree d, it is exactly
\[
\sum_iN_i(\xi,\eta)\,\overline{x_i-a_i}=0
\quad\Longrightarrow\quad
x_i-a_i\in I_L\quad(i=1,2,3).
\tag{7}
\]
For the implication, the coefficient matrix of the three
independent complex polynomials \(N_i\) has a nonzero complex
three-by-three minor. That minor is a unit over R0, so their
linear independence persists over R0, even when it is nonreduced.
No determinant-nilpotence inference or generic reducedness is
used in this step.

The contraction \(\mathfrak m=\mathfrak n\cap S\) is a
maximal ideal of the actual plane S. To check this precisely,
any height-one prime of S containing p,q would be generated
by a common divisor. Faithful flatness keeps that divisor a
nonunit in B, contradicting \(\gcd_B(p,q)=1\). A prime
containing both independent parameters is nonzero, so the
contraction has height two and is maximal. Its residue field
is \(\mathbb C\).

Reduce (7) modulo the maximal ideal \(\mathfrak nL\).
The three original coordinates satisfy
\[
\overline{x_i}=a_i(\mathfrak m)\in\mathbb C\quad(i\le3),
\qquad
\kappa(\mathfrak n)=\operatorname{Frac}(B/\mathfrak n)
\text{ has transcendence degree at most one}.
\tag{8}
\]
The latter follows because B is generated by precisely these
three original coordinates and w. Once the three are constants,
the quotient is generated over \(\mathbb C\) by the residue
of w alone. However a height-two prime of the four-variable
polynomial ring has residue field of transcendence degree two.
This contradiction excludes the assumed proper ideal.
Equivalently, (7) contracts to \(x_i-a_i\in\mathfrak n\);
adding \(a_i-a_i(\mathfrak m)\in\mathfrak n\) shows
that the height-two prime contains the three independent actual
affine linear equations \(x_i-a_i(\mathfrak m)\). Their ideal
has height three, giving the same contradiction directly.

## 4. Exact conclusion and scope

The completed conclusion in this actual nonlinear supplied-good
branch is
\[
(p,q)S=S,\qquad (p,q)A=A,\qquad (p,q)B=B,
\qquad (P_1,P_2,P_3)S=S.
\tag{9}
\]
The first two equalities follow by faithful-flat contraction
from the proved equality in B. For the last, the binary ideal
inclusion from descent77 gives
\((p,q)^{2e-1}S\subset(h_1(p,q),h_2(p,q),h_3(p,q))S\).
Thus the transverse velocities also generate the unit ideal
over the common invariant plane, not merely a gcd-one ideal.

Dependent binary parameters were already known to have unit
ideal. The new proof excludes the independent proper case,
including all its ramified or nonreduced possibilities.
It does not assert that independent unit pairs are coordinates,
that their parameter map is globally finite, or that P4 belongs
to \(\mathbb C[p,q]\).

The earlier ramification and derivative-pole conclusions remain
valid as conditional obstructions; the present original
tangent-plane invariant now excludes their proper-parameter
premise in the full stated branch. No conclusion about arbitrary
flat intrinsic models or stationary parameter pairs follows.

This is not a primitive-freeness or cancellation endpoint and
does not resolve the existence of a good direction or a nice
frame for a general sliced derivation. No historical novelty,
numerical method, full regression, human expert review or formal
verification is claimed. Files through pass77 and stable earlier
pass78 notes are unchanged.

[^graded]: The Stacks Project, [Definition 10.69.1, 061M](https://stacks.math.columbia.edu/tag/061M), and [Lemma 10.69.2, 00LN](https://stacks.math.columbia.edu/tag/00LN), as selected and applied in regular-derivative78. The selected definition and complete displayed proof of that lemma were freshly read for this note, not the entire source chapter or all dependencies. Only the regular-sequence associated-graded statement is used. The discarded flat-syzygy route is unnecessary; no new miracle-flatness application is a premise of this proof.
