# Recognition under a homogeneous relation among the three good speeds

The investigation now has a complete written recognition argument for
a restricted class of four-variable additive actions. It combines a
unit-normal construction, a whole-divisor-fiber argument and a
critical-point contradiction using the original coordinate derivative.
The unrestricted complex-threefold cancellation conjecture is not solved.
Human expert review and a statement-level novelty determination remain
outstanding.

## 1. The precise result

Let \(E\) be a locally nilpotent complex derivation of the actual
polynomial ring \(B=\mathbb C[x_1,x_2,x_3,z]\). Suppose
\[
E^2x_1=E^2x_2=E^2x_3=0,\qquad E^2z=q\in\mathbb C^*,
\qquad F(Ex_1,Ex_2,Ex_3)=0
\tag{1}
\]
for some nonzero homogeneous polynomial
\(F\in\mathbb C[T_1,T_2,T_3]\). Then the working theorem concludes
\[
\ker E\simeq\mathbb C^{[3]}.
\tag{2}
\]
The slice is already supplied by the second assumption:
\(u=Ez/q\) has \(Eu=1\). There is no separate requirement to find
a slice, and no premise that this supplied slice is an ambient
coordinate. The proof establishes the polynomial kernel under (1).

The homogeneous relation is a genuine additional hypothesis.
Writing \(b=(Ex_1,Ex_2,Ex_3)\) and taking an independent \(t\), it
is equivalent to \(\operatorname{trdeg}_{\mathbb C}\mathbb C(tb)\leq2\).
It bounds the dimension of the projective speed image. It is not a
bound on the ordinary polynomial degrees of the four coefficients.

The full case proof is in
[the combined recognition note](constant-acceleration-relative-slice-descent-pass89.md).
Its conclusion is a working mathematical result supported by written
reconstructions, not a formal certificate or a verified novelty claim.

## 2. How the proof closes the previously missing steps

The retained [invariant-plane construction88](constant-acceleration-invariant-plane-pass88.md)
gives the actual plane \(S=\mathbb C[s_1,s_2]\), a common kernel of
the sliced action and an intrinsic highest-adjoint LND. The speed row
\(b\) generates the unit ideal in \(S\).

If the speed map has rank zero, a constant linear combination of the
original good coordinates is a slice. If there is an invariant
constant linear coordinate, the established regular-kernel recognition
theorem applies. These cases are handled before the remaining argument.

For a rank-one speed curve, a univariate primitive cross product
gives a unit normal. For a rank-two conical speed image, the
homogeneous binary parametrization theorem gives a unit normal after
removing the common factor of its derivative cross product.[^binary]
The [curve-speed note](constant-acceleration-curve-speed-pass89.md)
and [conical-normal note](constant-acceleration-conical-normal-pass89.md)
keep these two constructions separate.

The resulting actual matrix reconstruction has the form
\[
A=\ker E=S[Y,c],\quad h=u-\sigma,\quad
x_{\rm tr}=b(u-h)+VY+U_0c_0,\quad
z=c+\frac q2(u^2-h^2),\quad c_0\in S.
\tag{3}
\]
These are identities between actual subalgebras, not a claimed
polynomial automorphism arising from a matrix with invariant
coefficients. The universal generator pencil forces
\(h\in\operatorname{Frac}(S[Y])\) and makes its tensor difference
nilpotent. Normality alone would not give global membership.

If \(Y\) is algebraic over \(\operatorname{Frac}(S)\), the intrinsic
LND kills it, so \(Y\in S\) and \(A=S[c]\) is already polynomial.
The rest of the argument assumes \(Y\) is transcendental over that
field.

After passing to \(K=\operatorname{Frac}(S)\), the intrinsic line is
\(A_K=K[v]\). The generic integrality of \(K[v]\) over \(K[Y]\)
places \(h\) in \(K[Y]\), without global descent. The original
commutator \(Q=[E,\partial_z]\), in the nontrivial remaining cases,
is a nonzero LND with kernel \(S\) on \(A\). It becomes
\(\lambda\partial_v\) for \(\lambda\in K^*\).

The [critical-point proof](constant-acceleration-relative-degree-one-pass89.md)
then gives the decisive generic-degree step. If \(Y'(v_0)=0\),
the generation identity \(K[v]=K[Y,c]\) forces \(c'(v_0)\ne0\).
At that point (3) makes the original coefficient column of \(Q\)
a nonzero vertical vector. But its two original Jacobian identities
are incompatible with such a vector:
\[
Q(x)=-Je_4,\qquad JQ(x)=0,\qquad
Q(x)|_{v_0}=\mu e_4,\ \mu\ne0
\quad\Longrightarrow\quad 0=-\mu^2e_4.
\tag{4}
\]
Thus \(Y\) has generic degree one and \(A_K=K[Y]\).
All evaluations occur in \(\overline K[u]\); there is no
specialization through a \(v\)-dependent denominator.

It remains to descend the coefficients of \(c\in K[Y]\).
The [whole-fiber proof](constant-acceleration-pole-support-pass89.md)
shows that any coefficient pole would force its invariant-plane
divisor to lie in the original good-coordinate subring.
The tensor condition on \(h\), not global descent of \(h\), makes
the fiber argument work. In the remaining speed cases, the combined
note excludes every nonconstant invariant in that good-coordinate
subring. Consequently no coefficient pole exists:
\(c\in S[Y]\), so \(A=S[Y]\), proving (2).

## 3. A separate valuation result and its limits

The [valuation-gap note](universal-pencil-valuation-gap-pass89.md)
proves a reusable statement for domains with
\(A=R[c]\), \(h\in A\), and \(A[\tau]=R[\tau,c+\tau h]\).
For every valuation nonnegative on \(R\),
\[
\nu(h)<0\quad\Longrightarrow\quad \nu(c)<\nu(h)<0.
\tag{5}
\]
In characteristic zero over a normal Noetherian \(R\), a pole of
order \(n\) in \(h\) therefore forces order at least \(n+1\)
in the leading coefficient of every polynomial relation of \(c\)
over \(R\). A relation with squarefree divisorial leading coefficient
is sufficient for \(h\in R\). The standard inputs are extension
of DVR valuations and the height-one intersection description of
normal domains.[^dvr][^normal]

The [all-integer family](generator-pencil-pole-order-control-pass89.md)
shows this bound is sharp. The separate
[binary-normal control](binary-normal-unit-control-pass89.md)
shows why dividing the raw derivative cross product by its common
factor is essential. Neither control is an actual cancellation
example. The recognition proof does not assume the squarefree
leading-coefficient criterion holds automatically.

## 4. What remains outside the theorem

The remaining three-good-coordinate constant-acceleration case has
rank-two speed map and
\(\Omega=\det[b,b_{s_1},b_{s_2}]\ne0\). The existence of such
actual frames is not hypothetical. In the retained
[explicit frame87](constant-acceleration-three-good-frame-pass87.md),
\[
x_1=u,\quad x_2=t+ur,\quad x_3=c+ut,\quad z=r+u^2,
\qquad E=\partial_u,\quad b=(1,r,t),\quad \Omega=1.
\tag{6}
\]
Its polynomial inverse is written in that note. No nonzero
homogeneous polynomial vanishes on \((1,r,t)\): dehomogenizing
a fixed-degree homogeneous polynomial at its first variable equal
to one is injective. This example is already recognized by the
coordinate slice \(x_1\); its purpose is to show that the new
homogeneous-relation premise is not automatic.

An affine linear relation among the three speeds also gives an
established recognition route: a nonzero constant right-hand side
gives an actual linear coordinate slice, and a zero right-hand side
gives an invariant linear coordinate with regular kernel. A next
nonconical investigation must therefore retain genuinely nonlinear
speed geometry rather than treating (6) as an unresolved example.

Even a solution of that nonconical case would not supply the
three-good-coordinate, constant-acceleration frame for an arbitrary
sliced derivation. That separate reduction remains missing.
The interpretation of Luo's email as corrected complex-threefold
cancellation is still unconfirmed.

## 5. Verification and literature boundaries

The [targeted capture](verification-pass89-working.json) records
two standalone exact methods, four unchanged inputs and two complete
outputs. It is not a test of the quantified recognition theorem.
The [proof-review record](proof-audits-pass89-working.md) separates
full-file mathematical reviews, finite tests, and source access.
The [checkpoint](checkpoint-pass89-working.json) records the saved
artifact hashes and outstanding obligations.

The nearby published inputs retain their exact scope:
Dasgupta--Gupta Theorem 3.1(i) provides an invariant linear form for
a nice LND of an actual polynomial three-ring; Bhatwadekar--Gupta--Lokhande
Theorem 3.5 requires an actual invariant ambient coordinate and a
regular kernel.[^nice][^regular] The latter's complete displayed
short proof and the former's displayed theorem were checked again.
Their deeper cited proofs remain inherited theorem inputs.

A bounded additional search did not establish whether the exact
statement (1)--(2) is already known. Sparse or irrelevant search
results do not establish novelty. No claim of priority, submission,
external contact, expert approval, or formal verification is made.
The general goal remains active.

[^binary]: Michiel de Bondt, [*Rational maps \(H\) for which \(K(tH)\) has transcendence degree 2 over \(K\)*](https://arxiv.org/pdf/1501.06046v4), Theorem 2.7 and Corollary 3.2. The selected statements and displayed proofs were checked in the retained primary text.
[^dvr]: The Stacks Project, [tag 09E8](https://stacks.math.columbia.edu/tag/09E8), finite separable extensions of a DVR's fraction field.
[^normal]: The Stacks Project, [tag 0AVB](https://stacks.math.columbia.edu/tag/0AVB), height-one intersection applied to the module \(R\).
[^nice]: Nikhilesh Dasgupta and Neena Gupta, [*Nice derivations over principal ideal domains*](https://arxiv.org/pdf/1701.03635v1), Theorem 3.1(i), reproducing the stated theorem of Wang. No new reconstruction of Wang's original proof is claimed.
[^regular]: S. M. Bhatwadekar, Neena Gupta and Swapnil A. Lokhande, [*Some K-theoretic properties of the kernel of a locally nilpotent derivation on \(k[X_1,\ldots,X_4]\)*](https://arxiv.org/pdf/1501.01438v1), Theorem 3.5.
