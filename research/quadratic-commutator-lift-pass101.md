# One additional base order, without an iterative lift

At a collapsed double component with nonzero first normal action,
the actual slice difference satisfies N squared h in the base square.
The original-volume normal has its second N-derivative in the base
cube. These strengthen the retained conclusions for h and for that
normal, but do not yet lift the whole-fiber commutation to higher
normal orders.

An exact intrinsic polynomial control shows why the finite-order
argument cannot simply be iterated. It is not a control satisfying
the entire supplied four-coordinate frame.

## 1. Retained actual hypotheses and the new square bound

Use the actual nonconical quadratic frame of
[volume-normal splitting99](quadratic-volume-normal-splitting-pass99.md).
Thus B=A[u] is the original polynomial fourfold, E is partial u,
the original good coordinates have E-degree at most one, and the
original z has nonzero constant acceleration. Let N be the actual
canonical field, with kernel S on A. At a collapsed fixed double
component C, retain the following exact notation:
\[
\begin{gathered}
S=\mathbb C[s_1,s_2],\qquad
\mathfrak q=I(C)=(F,G),\qquad
\mathfrak m=\mathfrak q\cap S,\qquad A/\mathfrak q=\mathbb C[c],\\
\mathbf a=x_{\rm tr}-u\mathbf b,\qquad
\mathbf a|_C=o\in\mathbb C^3,\qquad h|_C=\eta\in\mathbb C,\\
L=\mathbf b_{s_1}\times\mathbf b_{s_2},\qquad
L_0=L(\mathfrak m)\ne0,\qquad L\cdot\mathbf a=\kappa\in S,\\
F=L_0\cdot\mathbf a-\kappa(\mathfrak m),\qquad
NF\equiv0,\quad NG\equiv-\nu\alpha_1F\pmod{\mathfrak q^2},
\qquad \nu,\alpha_1\in\mathbb C^*.
\end{gathered}
\tag{1}
\]
The last line is the nonzero-first-normal case of the affine
quotient column (1,alpha0+alpha1 c). This note concerns that case,
not the constant column or L0 equal to zero. The argument is
componentwise; the whole collapsed double and mixed (2,1) cases
are among its applications.

Since C is fixed, N acts as zero on A/q. Its endomorphism of
q/q squared is consequently C[c]-linear, and (1) makes its square
zero. Hence N squared sends every element of q into q squared.
The all-power contraction
S intersect q to the r equals m to the r is already proved in
[base-normal order94](nonconical-base-normal-order-contraction-pass94.md).
Also N cubed kills every entry of the centered good column.
The resulting base-square statement for the good generators was
already used in
[component compatibility96](quadratic-component-compatibility-pass96.md),
Section 6. It is not a new assertion here.

For h, the global volume equation expresses Omega times h as an
S-linear combination of the two relative good generators and an
element of S. N kills S and the third iterates of those generators.
Since Omega is nonzero in the domain A, this proves N cubed h
equals zero globally, as in
[whole-fiber actions100](quadratic-whole-fiber-actions-pass100.md).
Now h minus eta belongs to q, so the same normal-square argument
and contraction give
\[
\begin{gathered}
N^2\mathbf a\in\mathfrak m^2S^3
\quad\text{(retained good-center argument)},\\
N^2h\in S\cap\mathfrak q^2,
\qquad\boxed{\quad N^2h\in\mathfrak m^2S.\quad}
\end{gathered}
\tag{2}
\]
Membership in S here follows from the third-iterate identities,
not merely from vanishing on the reduced component. No division
by Omega at the fixed base point is used.

## 2. The volume normal gains one further base factor

Subtract the exact global volume identity from the definition of F:
\[
\begin{gathered}
F=(L_0-L)\cdot\mathbf a+\kappa-\kappa(\mathfrak m),\\
N^2F=(L_0-L)\cdot N^2\mathbf a,
\qquad\boxed{\quad N^2F\in\mathfrak m^3S.\quad}
\end{gathered}
\tag{3}
\]
Every entry of L0 minus L belongs to m, and every entry of the
second derivative belongs to m squared by (2). The derivation
kills all these invariant coefficients. This improves the
base-square bound in volume-normal99 in the nonzero-first-normal
case. It does not state that N squared F vanishes.

## 3. Exact boundary to another iteration

Consider the separate intrinsic polynomial threefold
\[
\begin{gathered}
A_0=\mathbb C[x,y,c],\qquad f=xc+y^2,\qquad
S_0=\mathbb C[x,f],\qquad N_0=-x\partial_y+2y\partial_c,\\
\mathfrak q_0=(x,y),\qquad \mathfrak m_0=(x,f)S_0,\qquad
a_0=y^2,\quad F_0=x+f y^2,\quad G_0=y,\quad h_0=xc,\\
(F_0,G_0)=\mathfrak q_0,\qquad
(F_0,G_0^2)=(x,y^2)=\mathfrak m_0A_0,\\
\binom{x}{f}\equiv\binom{1}{c}F_0\pmod{\mathfrak q_0^2},
\qquad N_0^3a_0=N_0^3F_0=N_0^3G_0=N_0^3h_0=0,\\
N_0^2a_0=2x^2,\qquad
N_0^2h_0=-2x^2\in\mathfrak m_0^2\setminus\mathfrak m_0^3,
\qquad
N_0^2F_0=2x^2f\in\mathfrak m_0^3\setminus\mathfrak m_0^4.
\end{gathered}
\tag{4}
\]
N0 is a polynomial locally nilpotent derivation: weights zero,one,two
on x,y,c decrease under N0. Its kernel is S0. Indeed, after inverting
x the ring is (S0)x[y] and the derivation is minus x partial y.
If a polynomial invariant had an x-denominator in S0, reduction
modulo x would contradict injectivity of C[f] into C[y] by f to
y squared. This also follows from the separate full module proof
in [polynomial lift101](quadratic-double-polynomial-lift-obstruction-pass101.md).

The ideal equalities in (4) are literal: F0 minus x is f times y
squared, and f minus xc is y squared. Thus the whole fiber is
C[y,c]/(y squared), and the displayed column has nonzero first
normal action. Its coefficient differentiation is retained,
since N0 c equals 2y. Directly N0 F0 is minus 2xfy and N0 h0
is 2xy, giving the displayed second and third derivatives.
Algebraic independence of x,f makes the stated base orders exact.

The relation F0=x+f a0 realizes an invariant coefficient in m0
multiplying a center whose second derivative has exact order two.
It shows that the normal-square, cubic-iterate and one-extra-factor
argument does not force order three for the second derivative of h,
or order four for that of F. This control does not provide original
four coordinates with the prescribed acceleration, the specified
speed normal L, or all the original J identities. It therefore
does not refute a stronger deduction using those additional data.

## 4. The attempted full commutator lift remains inconclusive

The actual identities J to the fourth equals zero and
J cubed equals q times N of the original coordinate column times
(L,0) impose further original-frame constraints. They have not
produced another base-order increase in this bounded argument.
In particular the intrinsic control (4) is not asserted to satisfy
them.

For the original T=partial z, put Q=[E,T]. The exact identity
[E,Q]=2 Omega N permits the decomposition Q=Q0+2u Omega N,
where [E,Q0]=0, since E(u)=1 and E commutes with N and kills Omega.
The whole-fiber commutation from100 says Q has coefficients in mB;
Omega is already in m. Thus Q0 also has coefficients in mB.
This alone provides no additional base factor for Q0. Nor does
the decomposition justify dividing by Omega at m or treating T
as preserving the intrinsic ring A. The attempted use of the full
commutator and J identities beyond (2)--(3) is inconclusive, rather
than a proof that those identities cannot give further information.

The new conclusions are precisely the square bound for N squared h
and the cubic bound for N squared F. The contraction theorem, the
good-center bound and whole-fiber commutation retain their earlier
provenance. No new primary-source theorem, higher-normal induction,
original-frame realization or cancellation conclusion is claimed.
All files through100 remain unchanged.

The second method of the shared
[polynomial checker101](quadratic_polynomial_lift_checks_pass101.py)
tests the finite intrinsic control (4), including explicit polynomial
ideal transitions and its exact base orders. Its first method belongs
to the separate polynomial-lift proof. Neither method certifies the
actual geometric hypotheses or the all-power contraction used here.
This note's author read the final two-method code through EOF without
executing it; execution evidence is recorded separately.
