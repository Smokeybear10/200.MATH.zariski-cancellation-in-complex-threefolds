# Excluding an affine second projection at a quadratic rank-two center

Status: bounded working exclusion. In the actual supplied rank-two
chart, a quadratic center cannot have projected degrees \((2,1)\).
The affine-parameter determinant bound and two leading coefficients
already give a contradiction. No generic parameter is treated as an
ambient coordinate, and no original-ring recognition is asserted.

## 1. Exact inputs

Retain the full actual hypotheses of
[sextic reduction212](rank-two-t-independent-sextic-reduction-pass212-working.md)
and [center pruning213](rank-two-squarefree-center-degree-pruning-pass213-working.md).
Thus the original coordinates give a globally sliced exact1122
frame with full initial kernel
\((\mathsf Z\mathsf W-\mathsf X^4)\), the exact coefficient field
\(L\) is finite over \(\mathbb C(t,\rho)\), and the chart has \(q=1/\rho\).
The full potentials and scalar determinant in212 are retained.

Assume a quadratic center and the projected degrees
\[
\begin{gathered}
p(U)=S(U,V_c)-\ell,\qquad \deg p=2,\qquad
h=k_{tt}=2[U^2]p\ne0,\\
\deg_vy=2,\qquad \deg_v\vartheta=1,\qquad
y=P(\vartheta),\quad P(V)=p_2V^2+p_1V+p_0,\quad p_2\in L^* .
\end{gathered}
\tag{1}
\]
All coefficients belong to the exact field \(L\). The identification
\(L[v]=L[\vartheta]\) is a coefficient-field parametrization, not an
ambient polynomial coordinate change.

The selected plane relation is \(G(U,V)=U-P(V)\).
The full-potential proof in Section 2 of
[affine-second bound214](rank-two-affine-second-high-degree-exclusion-pass214-working.md)
does not assume the center is linear. It therefore applies here:
\[
q_1(V)=\mathcal H_U(P(V),V)\ne0,\qquad
q_1\mid R^2,\qquad R=2\rho^{-3}V+k_\rho,\qquad \deg q_1\le2 .
\tag{2}
\]
Its proof uses the scalar determinant \(J_0/\vartheta_v\in L^*\)
and both exact potentials of212. Neither a formal graph identity
alone nor the weaker divisibility by \(R^3\) is substituted for it.

## 2. Two incompatible leading coefficients

Write the actual sextic by U-degree:
\[
\mathcal H=a_4U^4+B_3(V)U^3+B_2(V)U^2+B_1(V)U+B_0(V),
\quad a_4=\frac{h^2}{4\rho^3}\ne0 .
\tag{3}
\]
The exact coefficient bounds from212 are
\(\deg B_3\le2,\deg B_2\le3,\deg B_1\le4,\deg B_0\le6\).
The V-quadratic coefficient of \(B_3\) is
\[
b_{32}:=[U^3V^2]\mathcal H=\frac{2k_{ttt}}{3\rho^6}
                                       =\frac{2h_t}{3\rho^6}.
\tag{4}
\]
For a direct check, the \(k_{ttt}U^3/6\) term of \(Q\), multiplied
by the leading \(4\rho^{-6}V^2\) in \(\mathcal R^2\), gives (4).
The U-cubic contributions from \(T^2\) and \(\mathcal R cT\) have
V-degree at most one. No other term contributes to (4).

Assign weights \(\operatorname{wt}U=2,\operatorname{wt}V=1\).
The only possible weight-eight terms in \(\mathcal H\) are
\(a_4U^4+b_{32}U^3V^2\). All remaining terms have weight at most
seven. Consequently \(\mathcal H(P(V),V)=0\) implies
\[
0=[V^8]\mathcal H(P,V)
  =p_2^3(a_4p_2+b_{32}),\qquad b_{32}=-a_4p_2 .
\tag{5}
\]
This conclusion also deals with \(h_t=0\): in that case it is already
inconsistent with \(a_4p_2\ne0\).

Differentiate (3) formally with respect to \(U\), before substituting
\(P(V)\). The contributions \(2B_2P\) and \(B_1\) have degree at
most five and four, respectively. Thus (5) gives
\[
\begin{aligned}
[V^6]\mathcal H_U(P,V)
 &=p_2^2(4a_4p_2+3b_{32})\\
 &=a_4p_2^3\ne0 .
\end{aligned}
\tag{6}
\]
This contradicts the degree bound in (2). The assumed pair \((2,1)\)
is therefore impossible at a quadratic center.

## 3. Scope

Squarefreeness of the quadratic center was not needed in this
argument, although the only centers still open after212 are
squarefree. The proof says nothing by itself about the other
quadratic-center pairs, linear centers, or other full initial
ideals. It does not show that an arbitrary cancellation instance
admits this coordinate frame.

The complete retained sources were read, and the two coefficient
comparisons were independently reconstructed before this note was
saved. No saved checker was run, imported, or compiled for this
proof. The result remains a written working exclusion requiring
its separate review and verification record. The full cancellation
objective remains unsolved.
