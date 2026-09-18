# The rank-two Euler matrix in the independent-parameter branch

The original nice action gives an exact two-by-two nilpotent matrix
after its velocity is expressed in the two invariant parameters.
Its radial defect and its parameter Wronskian are both nonzero.
This identifies the square of the original Jacobian with the derived
good-partial field, but only as a fraction-field factorization.
It does not justify evaluating a denominator at a parameter zero.

## 1. The actual action and its independent parameters

Retain the nonlinear ternary-cone branch of the
[binary descent proof](nice-binary-parameter-descent-pass77.md):
\[
\begin{gathered}
B=\mathbb C[x_1,x_2,x_3,w]=A[s],\quad A=\ker E,\quad Es=1,\\
E=P\cdot\partial,\quad E(P_i)=0,\quad
J=\operatorname{Jac}P,\quad J^2\ne0,\quad
T=\partial_w,\quad [E,[T,E]]=0,\\
P_i=h_i(p,q)\quad(i\le3),\qquad
p,q\in A,\quad \deg h_i=e\ge2.
\end{gathered}
\tag{1}
\]
The h_i are coprime homogeneous binary forms and linearly independent
over C. Assume p,q are algebraically independent. This is necessary
if their ideal is proper, by the complete
[finite-pair argument](binary-conormal-obstruction-pass77.md).
No coordinate status for either parameter is assumed.

Set K=Frac B and Q=[T,E]. The inherited sliced rank and
highest-vertical-adjoint arguments give
\[
J^3=0,\qquad \operatorname{rank}_KJ=2,\qquad
P\notin\operatorname{im}_KJ,\qquad
Q(x)=Je_4\ne0,\qquad P,Q(x)\text{ are independent over }K.
\tag{2}
\]
For the third assertion, the Jordan type is (3,1), so
im J intersect ker J=im J^2. Since JP=0, membership of P in
im J would make a nonzero second adjoint of an original partial
parallel to E, which is excluded by the original slice.
These are the actual gates of the
[leading-boundary proof](nice-leading-boundary-pass76.md), Section1.

If Je4 were zero, all four velocity polynomials would be independent
of w. At least one is nonconstant, since J has rank two.
It would be an E-invariant killed by the nonzero constant partial T,
contradicting the supplied-good nonlinear
[invariant-omission theorem](nice-good-direction-invariant-omission-pass76.md).
Thus Q is nonzero. Its column lies in im J, while P does not, proving
the final assertion in (2). In particular delta=Q|A is nonzero:
if it vanished, Q would be Q(s)E on the actual extension B=A[s].

## 2. Algebraic-coordinate differentiation and the exact factorization

The finite binary parametrization gives
trdeg C(P1,P2,P3)=2. Since rank J=2 in characteristic zero,
trdeg C(P1,P2,P3,P4)=2 as well. Therefore P4 is algebraic over
C(p,q). Put L=C(p,q,P4), a finite separable field extension
of C(p,q).

The two ordinary derivations of C(p,q) extend uniquely to L.
Explicitly, if F(Z) is the separable minimal polynomial of P4,
\[
(P_4)_p=-\frac{(\partial_p F)(P_4)}{F'(P_4)},\qquad
(P_4)_q=-\frac{(\partial_q F)(P_4)}{F'(P_4)}.
\tag{3}
\]
The denominator is nonzero in the field, not necessarily a unit
in a local polynomial ring. Differentiating the same relation by
each original coordinate partial proves the chain rule for P4.
This also explains why T need not preserve L for the chain rule
to hold: its values Tp,Tq can lie outside L.

Define the matrices and vectors over K
\[
\begin{gathered}
U=\frac{\partial P}{\partial(p,q)}\in\operatorname{Mat}_{4,2}(L),
\quad V=\operatorname{Jac}(p,q)\in\operatorname{Mat}_{2,4}(B),
\quad C=VU,\quad J=UV,\\
\tau=\binom{a}{b}:=\binom{Tp}{Tq}=Ve_4,\quad
r=\binom p q,\quad Q(x)=U\tau.
\end{gathered}
\tag{4}
\]
Both U and V have rank two. The rank of V follows from the
independence of p,q. The first three rows of U already have
rank two: the finite separable binary map has two independent
differentials. Equivalently, differentiating a separable relation
for each parameter shows dp,dq are in the span of the transverse
velocity differentials. Thus im J=im U, and left and right
inverses over K can be used in the calculations below.

## 3. The radial defect and the nonzero Wronskian

Put gamma=eP4-p(P4)_p-q(P4)_q. Euler's identity applies to each
homogeneous h_i in the first three rows of U. Niceness gives VP=0.
The exact resulting identities are
\[
\begin{gathered}
C^2=0,\quad C\ne0,\quad C\tau=0,\quad
Ur=eP-\gamma e_4,\quad Cr=-\gamma\tau,\\
\gamma\ne0,\qquad
\omega:=pb-qa\ne0.
\end{gathered}
\tag{5}
\]
Indeed J^3=U C^2 V=0 implies C^2=0 by the rank-two inverses,
while J^2=U C V is nonzero. Goodness gives J^2e4=0, hence
C tau=0. If gamma were zero, Ur=eP would put P in im U=im J,
contrary to (2). Also tau is nonzero because U tau=Q(x) is nonzero.
Consequently Cr is nonzero whereas C tau=0, so r and tau are
independent and their determinant omega is nonzero.

The action of C on the basis (r,tau) now determines every entry:
\[
\boxed{\quad C=-\frac{\gamma}{\omega}
\binom a b (b,-a).\quad}
\tag{6}
\]
The sign is fixed by (b,-a)r=omega. This formula uses the
original niceness, good-direction and slice gates through (2)
and (5). An arbitrary nilpotent matrix with two formal parameters
is not a realization of those gates.

## 4. The original Jacobian square and an invariant coefficient row

Let eta=b dp-a dq denote its coefficient row in the original
coordinates, so eta=(b,-a)V. It is nonzero because V has rank two.
Equation (6) gives
\[
\begin{gathered}
J^2=-\frac{\gamma}{\omega}Q(x)\eta,\qquad
\operatorname{im}_KJ^2=KQ(x),\\
\eta e_4=0,\quad \eta P=0,\quad \eta Q(x)=0,\qquad
\ker_K\eta=\operatorname{span}_K\{P,e_4,Q(x)\}.
\end{gathered}
\tag{7}
\]
The last three columns are independent: P,Q(x) are independent
in ker J and J e4=Q(x) is nonzero. Thus their three-dimensional
span is precisely the kernel of the nonzero row eta.

In fact all four coefficients of eta belong to A. The
[common-invariant argument](binary-conormal-obstruction-pass77.md)
gives Ea=Eb=0. Differentiating Ep=Eq=0 gives E(V)=-VJ,
where E acts entrywise on the coefficient matrix.
Also eta U=(b,-a)C=0 by (6). Consequently
\[
E(\eta)=-\eta J=0,\qquad
\eta\in A^{1\times4},\qquad
a,b\in(p,q)^e A,\qquad \omega\in(p,q)^{e+1}A.
\tag{8}
\]
The two ideal orders are exactly the original-slice restrictions
from pass77, not new unit assertions. The entrywise identity
E(eta)=0 is distinguished from the Lie derivative of a one-form.

## 5. Regularity and remaining scope

Neither (3) nor (6) permits evaluation of gamma/omega at p=q=0.
The new nonzero omega has positive order in that ideal.
Moreover gamma itself can acquire poles when p,q ramify as
functions on the actual common invariant ring S=ker delta.
The separate ramification argument is needed before using any
local initial form or a unit claim.

The factorization concerns the supplied-good nice branch with an
independent binary pair. It does not establish the existence of
that pair's zero set, exclude every such zero, prove primitive
freeness, bound all Q-orbits by a particular degree, or produce a
nice frame for an arbitrary sliced action.
The earlier constant-direction and rank inputs remain conditional
and source-dependent. No historical novelty or formal verification
is claimed. Frozen files through77 are unchanged.
