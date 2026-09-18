# Proper radical projected planes force unit speed

Status: working restricted recognition synthesis. This completes the
proper-plane part of the supplied radical chart, not the whole radical
chart and not the cancellation conjecture.

## 1. Statement with the actual hypotheses

Let
\[
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,
\qquad \deg_E(X,Y,Z,W)=(1,1,2,2).
\tag{1}
\]
Write \(a=EX,\ b=EY,\ e=E^2Z/2,\ h=E^2W/2\).
Assume the entire kernel of the weighted initial evaluation is
\[
\ker\!\left(
\mathbb C[\mathsf X,\mathsf Y,\mathsf Z,\mathsf W]
\longrightarrow A[\tau]\right)
=(\mathsf X^2\mathsf Z-\mathsf W^2),
\quad
(\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
\longmapsto(a\tau,b\tau,e\tau^2,h\tau^2).
\tag{2}
\]
The requirement is the full kernel, not just one vanishing identity.
Use the actual selected partial \(\partial_Z\) and the constructions
of [universal184](weight-four-universal-chart-potentials-pass184-working.md)
and [eliminant206](weight-four-radical-nonzero-r-eliminant-pass206-working.md):
\[
\begin{gathered}
N=[u^3](\partial_Z|_A),\quad L=\operatorname{Frac}\ker_A N,
\quad A_L=L[v],\quad Nv=1,\\
t=b/a,\quad \rho=h/a^2,\quad
Y=y+tX,\quad Z=z+(2\rho\vartheta+k)X+\rho^2X^2,\quad
W=w+\vartheta X+\rho X^2,\\
R=2\vartheta+k_\rho\ne0,\qquad
C=L[y,\vartheta]\subset O=L[v].
\end{gathered}
\tag{3}
\]
In particular the exact coefficient field is finite over
\(\mathbb C(t,\rho)\); its rationality is not an assumption.

**Restricted theorem.** Under (1)--(3),
\[
C\subsetneq O
\quad\Longrightarrow\quad
\deg_v\vartheta=2,\quad
\deg_vy\in\{3,4\},\quad
a\in\mathbb C^*,\quad A\simeq\mathbb C^{[3]}.
\tag{4}
\]
The inverse-coordinate conclusions used to obtain \(a\in\mathbb C^*\)
hold in the original polynomial ring. In particular the theorem
does not infer unit speed from a nonzero element of \(L\).

## 2. Complete branch coverage

The [conductor reduction206](radical-projection-conductor-cubic-reduction-pass206-working.md)
first shows that a proper plane in this actual chart is
\(L[s^2,s^3+cs]\), with normalization defect one and conductor
\((s^2+c)L[s]\). The original generator degrees have the stated
finite bounds. The [local refinement208](radical-proper-projection-degree-refinement-pass208-working.md)
uses the actual potential equations to sharpen the second degree
to at most three.

The [cubic-second exclusion209](radical-cubic-second-projection-exclusion-pass209-working.md)
then rules out second degree three. Its crucial steps are:

- A finite free multiplication matrix specializes the monic cubic
  plane equation at the center. This includes the length-two cusp
  fiber and makes no unramifiedness assumption.
- The evaluated cofactor is supported only at the one remaining
  simple return root and is a power of degree at most three.
  Exact membership in the cusp or node ring eliminates the cusp
  and reduces the node to two cases.
- The cubic node power contradicts the calibrated gradient
  identity. The quadratic node power admits an actual normalization,
  after which its Jacobian is divisible by an affine generic
  parameter and so cannot be a nonzero scalar.

Therefore only second degree two remains. Equal first and second
degrees two cannot give a proper birational plane ring: cancelling
their quadratic leading terms either gives an affine parameter,
making the plane whole, or makes its fraction field quadratic.
The conductor degree restrictions leave first degrees three and four.

The [cubic/quadratic theorem209](radical-cubic-first-quadratic-second-unit-speed-pass209-working.md)
handles \((\deg y,\deg\vartheta)=(3,2)\), and the
[quartic-first theorem208](radical-quartic-first-projection-unit-speed-pass208-working.md)
handles \((4,2)\). Both prove constant-parameter normal forms and
both orders of their actual polynomial inverse. They recover
\[
B=\mathbb C[U,x,t,\rho],\qquad
Ex=Et=E\rho=0,\qquad EU=a .
\tag{5}
\]
Thus \(E=a\partial_U\), and \(E^2U=0\) makes \(a\) independent
of \(U\). The original global slice gives
\[
1=Eu=a\partial_Uu .
\tag{6}
\]
Only here does it follow that \(a\) is a unit of \(B\), namely
a nonzero complex constant, and that \(A=\mathbb C[x,t,\rho]\).
The actual normalizations preserved the original \(a\).
This proves every conclusion of (4).

## 3. A unified normal form and the remaining task

After the stated actual elementary normalizations, both recognized
families can be written with complex constants
\(\gamma,\delta\ne0\), \(\lambda,\kappa,n_1,n_2,\ell_0\):
\[
\begin{gathered}
k=0,\quad n=\gamma t+\lambda^2\rho^2+n_1\rho+n_2,\quad
\ell=\gamma\lambda t+\delta\rho+\ell_0,\\
K=2\lambda\delta\rho+\kappa,\qquad
\vartheta=(x^2-K)/\delta,\qquad
w=x-\lambda\vartheta-\lambda^2\rho-n_1/2,\\
y=(\ell-2\vartheta x+2\lambda\vartheta^2)/\gamma,\qquad
z=2\rho w+\vartheta^2+n .
\end{gathered}
\tag{7}
\]
Here \(\lambda=0\) gives first degree three, and
\(\lambda\ne0\) gives first degree four. These formulas are
necessary normal forms proved in the two branch notes, not
an assertion that arbitrary coefficients can be normalized
over the original ring.

The plane ring in this form is
\[
C=L[x^2,x(x^2-K)] .
\tag{8}
\]
It is cuspidal when \(K=0\) and geometrically nodal otherwise.
Since \(\rho\) is transcendental over \(\mathbb C\), first degree
four has \(K\ne0\), hence is nodal. The examples207 are compatible
with these unit-speed conclusions. There is no contradiction
between a proper generic plane and an actual invariant coordinate.

Equivalently, within exactly (1)--(3),
\[
a\notin\mathbb C^*
\quad\Longrightarrow\quad L[y,\vartheta]=L[v].
\tag{9}
\]
This is the next restriction, not the end of the cancellation proof.
A whole projected plane is still not an invariant coordinate of
the original four-ring. Recognizing that whole-plane branch,
other leading kernels and higher or lower initial ranks, and
placing an arbitrary globally sliced action in a recognized frame
all remain separate unresolved requirements.

## Verification status

The degree-four branch has its recorded written reviews and the
five-method finite checker in
[verification208](verification-pass208-working.json). The two new209
branch notes and this synthesis are separate from that frozen packet.
No saved209 checker has run, and no finite test is represented as
a proof of the field, cofactor or exhaustive branch arguments.

This synthesis and its underlying proofs are private working
mathematics with independent AI reconstruction, not human expert
review, proof-assistant certification, or novelty clearance.
The unconfirmed corrected complex-threefold cancellation target
remains unsolved. No external contact, public posting or submission
has occurred.
