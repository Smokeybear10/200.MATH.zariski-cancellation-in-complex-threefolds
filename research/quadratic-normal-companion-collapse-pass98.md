# A nonzero speed normal collapses the simple companion

In a surviving quadratic fiber of profile (2,1), suppose the
speed-map normal L is nonzero at the base value. Then the simple
companion, as well as the fixed double component, is collapsed.
Their cylinders are two distinct parallel affine planes in the
original four-space. One original good hyperplane contains both,
and its nonzero speed vanishes to second order on the base.

These are necessary actual-frame restrictions. They neither
exclude the two components nor recognize the kernel. The sector
where L vanishes at the base point is not covered.

## 1. Actual hypotheses and retained fiber information

Retain the actual nonconical quadratic setup of
[checkpoint97](checkpoint-pass97-working.json),
[the invariant-plane proof88](constant-acceleration-invariant-plane-pass88.md),
and [the weighted defect proof97](quadratic-weighted-rank-defect-pass97.md):
\[
\begin{gathered}
B=\mathbb C[x_1,x_2,x_3,z]=A[u],\qquad E=\partial_u,
\qquad u=Ez/q,\qquad q=E^2z\in\mathbb C^*,\\
E^2x_i=0,\qquad S=\mathbb C[s_1,s_2]\subset A=\ker E,
\qquad \mathbf b=(Ex_1,Ex_2,Ex_3)^t\in S^3,\\
C=[\mathbf b,v_2,v_3]\in\operatorname{GL}_3(S),\qquad
A=S[A_1,A_2,c],\qquad h\in A,\\
x_{\rm tr}=\mathbf b(u-h)+v_2A_1+v_3A_2,
\qquad z=c+\frac q2(u^2-h^2),\\
L=\mathbf b_{s_1}\times\mathbf b_{s_2},\qquad
\Omega=L\cdot\mathbf b\ne0.
\end{gathered}
\tag{1}
\]
The displayed four coordinates of B are original polynomial
coordinates. An invertible S-matrix in (1) is used only for the
actual generating identities, not as an ambient automorphism.

Let \(\mathfrak m\) be a closed point of S whose whole fiber has
two components \(C_2,C_1\), with generic scheme multiplicities
two and one respectively. Assume \(C_2\) is fixed pointwise by
the actual canonical Jacobian LND N. Write their prime ideals
in A as \(\mathfrak q_2,\mathfrak q_1\).

The retained [compatibility theorem96](quadratic-component-compatibility-pass96.md)
makes \(C_2\) collapsed:
both A_i have constant residue on it. The affine-line theorem96
and weighted defect theorem97 say that the two reduced components
are disjoint entire affine lines and that A_1,A_2,c restrict
affinely to each. Since these generators generate A over S,
their relative three-space presentation is a closed embedding of
the whole fiber. In particular it preserves distinctness and
disjointness of the two reduced components. These are actual
fiber statements, not chosen line configurations.

## 2. The original volume forces collapse of the companion

The exact [global volume identity88](constant-acceleration-volume-descent-pass88.md) is
\[
\Omega h=(L\cdot v_2)A_1+(L\cdot v_3)A_2-\kappa,
\qquad \kappa\in S.
\tag{2}
\]
The canonical field N is fixed-point-free on \(A_\Omega\), by
the final paragraph of Section 4 of
[global-Jacobian91](nonconical-global-jacobian-field-pass91.md).
The fixed component therefore forces \(\Omega(\mathfrak m)=0\).
This uses freeness of the exact N on that open set, not merely
the existence of some rational multiple of N which is free.

Suppose now that \(L_0=L(\mathfrak m)\ne0\), and put
\(\mathbf b_0=\mathbf b(\mathfrak m)\). The latter is nonzero
because the speed row is unimodular. Define
\[
\begin{gathered}
\alpha=L_0\cdot v_2(\mathfrak m),\qquad
\beta=L_0\cdot v_3(\mathfrak m),\qquad
\kappa_0=\kappa(\mathfrak m),\\
(\alpha,\beta)\ne(0,0),\qquad
\alpha\bar A_1+\beta\bar A_2=\kappa_0
\quad\text{in }A/\mathfrak mA.
\end{gathered}
\tag{3}
\]
Indeed \(L_0\mathbf b_0=0\), and if the other two products
vanished then L_0 would annihilate the invertible matrix
\(C(\mathfrak m)\). The last equality is the specialization of
(2) in the whole, possibly nonreduced fiber.

Let p be the constant good point of C_2. Its relative image is
the entire vertical line \(\{p\}\times\mathbb A^1_c\). The
affine good-plane equation in (3) defines a line through p.
If C_1 were noncollapsed, its good projection would be a line:
the two good residues are affine in a parameter, with at least
one nonzero slope. Equation (3) would make that projected line
equal to the line through p. The projection would attain p,
and the corresponding point of the full relative line C_1
would meet the vertical line C_2 at its finite c-value.
This contradicts disjointness in the actual closed embedding.
Thus
\[
\boxed{\quad
L(\mathfrak m)\ne0
\ \Longrightarrow\ C_1\text{ and }C_2\text{ are both collapsed}.
\quad}
\tag{4}
\]
No finiteness of a projection or normalization of an intermediate
curve is used. In particular the exact rank defect97 remains
consistent with this argument.

## 3. Two actual parallel planes in one good hyperplane

For i equal to 1 or 2, write the good residues as
\(p_i=(p_{i1},p_{i2})\). They are different: otherwise their
relative vertical lines would coincide in the embedding.
The retained tensor-pencil argument in
[collapsed-plane92](nonconical-collapsed-component-plane-pass92.md)
also makes \(h|_{C_i}=\eta_i\in\mathbb C\). For clarity, its
nilpotent difference \(h\otimes1-1\otimes h\) maps to zero in
\(\mathbb C[c_1,c_2]\), because the image of S[A_1,A_2] on a
collapsed component is C. Hence h is constant on that component.

Set
\[
\begin{gathered}
o_i=-\eta_i\mathbf b_0+p_{i1}v_2(\mathfrak m)
                         +p_{i2}v_3(\mathfrak m),\\
B/\mathfrak q_iB=\mathbb C[c_i,u],\qquad
\bar x_{\rm tr}=\mathbf b_0u+o_i,\qquad
\bar z=c_i+\frac q2(u^2-\eta_i^2),\\
\ell=L_0\cdot x_{\rm tr}-\kappa_0,\qquad
\ell|_{\mathfrak q_iB}=0.
\end{gathered}
\tag{5}
\]
Thus both cylinders are actual affine planes with the same
direction space spanned by \((\mathbf b_0,0)\) and \(e_z\).
Their good lines are distinct, since their displacement modulo
\(\mathbb C\mathbf b_0\) is the nonzero combination of the last
two columns of \(C(\mathfrak m)\) determined by \(p_1-p_2\).
The last assertion in (5) follows from (3) and
\(L_0\mathbf b_0=0\).

Choose a constant row \(\xi\) independent of L_0 in the
annihilator of \(\mathbf b_0\). Since the two distinct good
lines lie in the same L_0-hyperplane, \(\xi(o_1-o_2)\ne0\).
Choose also a constant row \(\lambda\) with
\(\lambda\mathbf b_0=1\), and set
\[
\begin{gathered}
Y=\frac{\xi(x_{\rm tr}-o_2)}{\xi(o_1-o_2)},\qquad
W=\lambda(x_{\rm tr}-o_2),\qquad
B=\mathbb C[\ell,Y,W,z],\\
\boxed{\quad
\mathfrak q_2B=(\ell,Y),\qquad
\mathfrak q_1B=(\ell,Y-1).
\quad}
\end{gathered}
\tag{6}
\]
This is a constant affine coordinate change in the three original
good coordinates, so it genuinely is an ambient automorphism.
The ideal equalities follow directly from (5): W recovers u up
to a constant on either plane, and z then recovers c_i.
Equivalently both indicated inclusions are between height-two
prime ideals. The planes are stable under E and the original
\(\partial_z\), but that does not make their defining good
coordinates invariant.

The shared coordinate has a precise nonzero second-order speed:
\[
E\ell=L_0\cdot\mathbf b(s)\in\mathfrak m^2\setminus\{0\},
\qquad E^2\ell=0.
\tag{7}
\]
Its value at the base point is zero. Each first base partial is
\(L_0\cdot\mathbf b_{s_j}(\mathfrak m)=0\), which proves
membership in the square of the maximal ideal of the polynomial
base. If this speed were identically zero, differentiation would
make the same nonzero constant row L_0 annihilate all three
columns \(\mathbf b,\mathbf b_{s_1},\mathbf b_{s_2}\) globally.
Their determinant would vanish identically, contrary to (1).
In particular (7) is not an invariant-coordinate conclusion.

## 4. Exact component generators inside the original kernel

The evaluation homomorphism at u=0 in the actual polynomial
presentation B=A[u] fixes A. Since ell and Y are good affine
coordinates, their E-degree is at most one. Define
\[
\begin{gathered}
F=\ell-uE\ell\in A,\qquad G=Y-uEY\in A,\\
\boxed{\quad
\mathfrak q_2=(F,G),\qquad
\mathfrak q_1=(F,G-1),\qquad
\sqrt{\mathfrak mA}=(F,G(G-1)).
\quad}
\end{gathered}
\tag{8}
\]
Applying evaluation to the two exact extended ideals in (6)
gives the first two equalities. Their sum is A. Modulo F, the
ideals generated by G and G-1 are comaximal, so their intersection
is generated by G(G-1). This gives the third equality, since
there are exactly two reduced components of the fiber.

These are global component-ideal equalities in A, not a claim
that F and G are coordinates of A or B. In particular the last
ideal is the radical of the fiber ideal, not the whole nonreduced
ideal \(\mathfrak mA\). No first-normal-action assumption is
needed for any conclusion above.

## Scope and evidence

Root proposed applying the global volume relation to the two
relative lines. Geometry reconstructed the collapse proof and
the original parallel-plane, second-order-speed, and slice-evaluation
consequences. General independently checked the original-coordinate
outline. The listed invariant-plane88, volume88, global-Jacobian91,
collapsed-plane92, compatibility96 and weighted-defect97 files,
plus checkpoint97, were reread through EOF for their indicated
gates. This is not a new primary-source proof audit. The
affine-line and supported-source dependencies
remain exactly those recorded in the frozen proofs.

No numerical method or original-frame example is supplied here.
The theorem is conditional on the actual (2,1) fixed-containing
fiber and the nonzero value of L. It leaves the L=0 sector, the
existence of either profile, freeness, recognition of the supplied
frame, and unrestricted cancellation unresolved. All files
through97 are unchanged.
