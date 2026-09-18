# An explicit nice frame for the quadratic relative branch

In the actual nonconical constant-acceleration setting, a quadratic
relative plane relation forces a constant quadratic form on the
velocity column. It supplies an explicit triangular change of the
fourth original coordinate after which every coordinate has zero
second derivative. This branch therefore reduces to the retained
nice-slice recognition theorem. The proof does not use the later
global conic presentation or exceptional-fiber analysis.

The general complex-threefold cancellation problem remains open in
this investigation. A cubic relative relation is not treated here,
and an arbitrary sliced action has not been put into the supplied
constant-acceleration frame.

## 1. Exact actual-frame input

Let B be the complex polynomial four-ring in actual original
coordinates x1,x2,x3,z, with a locally nilpotent derivation E and
canonical slice u. Retain the actual invariant plane and volume
construction of [potential90](nonconical-quadratic-potential-pass90.md)
and [cubic-relation90](nonconical-cubic-relation-pass90.md). With
i,j in {1,2}, the actual data include

\[
\begin{gathered}
B=\mathbb C[x_1,x_2,x_3,z]=A[u],\quad A=\ker E,\quad
Eu=1,\quad Ex_{\rm tr}=b,\quad Ez=qu,\quad q\in\mathbb C^*,\\
S=\mathbb C[s_1,s_2]\subset A,\quad b\in S^3,\quad
\mathcal C=[b,b_{s_1},b_{s_2}],\quad
\Omega=\det\mathcal C\ne0,\quad K=\operatorname{Frac}S,\\
A_\Omega=S_\Omega[y_1,y_2],\qquad A_K=K[v]=K[y_1,y_2],\\
b_{s_i s_j}=G_{ij}b+\sum_{l=1}^2 C^l_{ij}b_{s_l},
\qquad G_{ij},C^l_{ij}\in S_\Omega .
\end{gathered}
\tag{1}
\]

The arrays are symmetric in i,j. The intrinsic slice used in the
volume calculation is available after inverting only a nonzero
element of S, not a polynomial depending on v. After extension to
K its coordinate ring is K[v,u], without a further v-localization.
This distinction is essential below.

Let F in K[Y1,Y2] generate the kernel of evaluation Y to y.
The new hypothesis is deg F=2, the exact quadratic relative branch.
It concerns the two actual generators from (1), not an arbitrary
quadratic equation chosen on an isomorphic curve.

## 2. The unit Jacobian kills the cubic multiplier

The complete volume calculation90 gives a symmetric tensor,
a formal polynomial potential and its gradient:

\[
\begin{gathered}
T_{ijk}=-\partial_iG_{jk}
 +\sum_l\bigl(G_{lj}C^l_{ik}+G_{lk}C^l_{ij}\bigr),\\
\Phi(Y)=\Phi_{\le2}(Y)
 +\frac q6\sum_{i,j,k=1}^2T_{ijk}Y_iY_jY_k,\qquad
Z_i(Y)=\partial_{Y_i}\Phi(Y),\\
\Phi(y)=\zeta\in K,\qquad \Phi(Y)-\zeta\ne0,\\
\frac{\mathcal J}{\Omega}
=\det\begin{pmatrix}
u+K_{11}&K_{12}&(y_1)_v\\
K_{21}&u+K_{22}&(y_2)_v\\
Z_1(y)&Z_2(y)&0
\end{pmatrix}\in K^*.
\end{gathered}
\tag{2}
\]

Here K_ij are the entries defined in90, not fields; every matrix
entry belongs to K[v,u]. The nonzero constant on the last line
is the determinant of a change between actual differential bases.
It is not an assumed Jacobian conjecture conclusion.

Since F is the evaluation kernel, write Phi-zeta=H F with
H in K[Y1,Y2], H nonzero and deg H at most one. Differentiating
and evaluating on F=0 gives Z_i(y)=H(y)F_Yi(y). Factoring the
last row of (2) therefore gives

\[
\mathcal J/\Omega=H(y)D(v,u),\qquad D(v,u)\in K[v,u],
\qquad H(y)\in K[v,u]^*=K^*.
\tag{3}
\]

Write H(y)=c with c in K*. Then H-c belongs to (F) but has
total Y-degree at most one. A nonzero multiple of a degree-two
polynomial cannot have that degree over a field. Hence H=c as
a formal polynomial, not merely after evaluation. Therefore
Phi-zeta=cF has degree two.

Its displayed cubic part vanishes. Characteristic zero, q nonzero
and full symmetry of T imply every T_ijk=0. For example the
coefficients of Y1 cubed and Y1 squared Y2 are qT111/6 and
qT112/2. No extrapolation from finitely many values is involved.

## 3. A constant quadratic form from the moving frame

Set G=(G_ij) and introduce matrices over K:

\[
\begin{gathered}
\mathcal H=\begin{pmatrix}-1&0&0\\0&G_{11}&G_{12}\\0&G_{12}&G_{22}\end{pmatrix},
\qquad Q=\mathcal C^{-t}\mathcal H\mathcal C^{-1},\\
M_i=\mathcal C^{-1}\partial_i\mathcal C
=\begin{pmatrix}
0&G_{i1}&G_{i2}\\
\delta_{i1}&C^1_{i1}&C^1_{i2}\\
\delta_{i2}&C^2_{i1}&C^2_{i2}
\end{pmatrix}.
\end{gathered}
\tag{4}
\]

Neither G nor H is required to be invertible. Only C is inverted,
as permitted in K by Omega nonzero. Direct multiplication shows
that the first row and column of M_i transposed H+H M_i vanish:
the two G_ij terms cancel because H00=-1. Its lower-right entry
j,k is the sum in the formula for T_ijk in (2). Thus T=0 gives

\[
\partial_i\mathcal H=M_i^t\mathcal H+\mathcal H M_i,
\qquad
\partial_iQ=\mathcal C^{-t}
(\partial_i\mathcal H-M_i^t\mathcal H-\mathcal H M_i)
\mathcal C^{-1}=0\quad(i=1,2).
\tag{5}
\]

The joint constants of the usual partial derivatives in C(s1,s2)
are C. Vanishing of the s1 derivative first places a rational
function in C(s2), and the second derivative then makes it
constant. Apply this to every entry of Q. Hence Q is a constant
complex symmetric matrix, not merely a matrix on the Omega-open
set. Its defining pairings give b transposed Q b=-1. In particular
Q is nonzero, even if it has rank less than three.

## 4. The global polynomial shear

The new fourth coordinate and its inverse are

\[
\boxed{\quad
z'=z+\frac q2x_{\rm tr}^{t}Qx_{\rm tr},\qquad
z=z'-\frac q2x_{\rm tr}^{t}Qx_{\rm tr}.
\quad}
\qquad E^2z'=q+q\,b^tQb=0.
\tag{6}
\]

These are polynomial substitutions in the original coordinates,
fixing x1,x2,x3. Constancy of Q makes the change global, with no
base denominators. The second derivative uses Ex_tr=b and Eb=0.
The three unchanged coordinates still have zero second derivative.

Thus E is nice in an actual polynomial coordinate frame: E squared
kills all four new generators. The original polynomial slice u
still satisfies Eu=1; it need not be recovered as Ez'/q. The
derivation and its kernel have not changed. This proves the frame
reduction without a new classification theorem or conic patching.

## 5. Recognition endpoint and honest scope

The retained [nice-slice theorem80](nice-slice-recognition-pass80.md)
states that a locally nilpotent derivation of the actual complex
polynomial four-ring, nice in an actual coordinate frame and
possessing a global polynomial slice, has polynomial kernel.
Applying that working theorem to (6) gives A isomorphic to C^[3].

The reduction (6) and this endpoint must be distinguished:
theorem80 is a separately AI-audited written result, not a newly
invoked published universal theorem. Its proof dependencies and
confidence limits remain as recorded there. Neither step is
Lean-verified or human expert-reviewed.

The [earlier shear criterion81](rank-one-acceleration-shear-boundary-pass81.md)
already recorded that a constant quadratic velocity identity would
suffice. The advance is proving that such an identity is forced
by the exact quadratic relative branch, using the unit Jacobian
to remove its cubic multiplier. A matrix with rational base
entries would not suffice for the global shear.

The proof uses the actual invariant-plane/volume framework90
and, for kernel recognition, theorem80. It does not assume the
global conic115, the module/fiber arguments91--115, or the
involution restrictions116. Those remain earlier research but
are unnecessary premises for this reduction.

For a cubic relative relation, (3) only makes the multiplier of
the already cubic F constant; it does not force T to vanish.
The argument does not solve that branch. A general cylinder
presentation also does not supply the frame in (1). Luo's
intended field and dimension remain unconfirmed, and general
cancellation is not claimed.

## Verification scope

The tensor cancellation and shear are exact symbolic identities.
The companion [checker117](quadratic_velocity_shear_checks_pass117.py)
checks the block calculation and an explicit nonplanar coefficient
example. That example is not an actual cancellation input without
the original polynomial inverse. Finite checks do not prove the
unit-Jacobian premise, the degree argument, the invariant-plane
construction or theorem80. Independent written reconstructions
and execution evidence are separate from these obligations.
Historical novelty is not established.
