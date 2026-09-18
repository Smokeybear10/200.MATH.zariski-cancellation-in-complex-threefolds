# The triple-root quartic has only a projected cubic frontier

Status: bounded reduction for supplied actual globally sliced exact1122
frames with full initial kernel ZW minus a binary quartic of root
partition 3+1. The degree-two projected case is impossible. Combining
this with the separately proved line exclusions leaves only cubics.
No actual cubic is constructed or excluded here.

## 1. Exact inputs and the two leading directions

Assume the full actual hypotheses of
[general quartic220](rank-two-binary-quartic-leading-sextic-pass220-working.md):
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad
\deg_E(X,Y,Z,W)=(1,1,2,2),\\
\ker(\mathsf X,\mathsf Y,\mathsf Z,\mathsf W
 \mapsto aT,bT,e_0T^2,h_0T^2)
 =(\mathsf Z\mathsf W-F_4(\mathsf X,\mathsf Y)),\\
F_4=c\,l^3m,\qquad c\in\mathbb C^*,\quad
l,m\text{ independent complex linear forms}.
\end{gathered}
\tag{1}
\]
The displayed kernel is the entire initial kernel. All four capital
coordinates are original polynomial coordinates, and the global slice
is an actual hypothesis, not a formal time variable alone.

Use the original selected Z pivot and universal184 chart. In the exact
finite coefficient field and its selected affine line,
\[
\begin{gathered}
[L:\mathbb C(t,\rho)]<\infty,\qquad
q=F_4(1,t)/\rho,\qquad \mathcal O=L[v],\qquad
L[y,z,w]=\mathcal O,\\
\mathcal C=L[y,\vartheta],\qquad
\operatorname{Frac}\mathcal C=L(v),\qquad
R\mathcal O\subset\mathcal C .
\end{gathered}
\tag{2}
\]
Indeed F4 is not a square, so
[zero-return221](rank-two-nonsquare-quartic-zero-return-exclusion-pass221-working.md)
forces R nonzero, and the nonzero-return conclusions220 apply.
The last two assertions do not assume that C is normal or equals O.

The sextic eliminant and universal cofactor proof in
[saturated-pair222](rank-two-saturated-pair-cofactor-exclusion-pass222-working.md)
give
\[
\begin{gathered}
\mathcal H=\Gamma Q_1,\quad
0\ne q_1=Q_1(y,\vartheta),\quad q_1\mid R^3\text{ in }L[v],\\
g:=\deg\Gamma=\max(\deg_v y,\deg_v\vartheta),\qquad
\Gamma_g=c_0\ell^g,\\
\mathcal H_6=c_1\ell^3\widetilde\ell^3,
\qquad c_0,c_1\in L^*.
\end{gathered}
\tag{3}
\]
Here ell and tilde-ell are distinct homogeneous linear forms over L.
They are the directions obtained from the repeated-root pair l,l and
the distinct-root pair l,m, in either order. The factor identity220
proves that each has multiplicity three. Consequently 1<=g<=3.
The selected Gamma is irreducible and generates the exact evaluation
kernel in L[U,V]. Its multiplicity in H is one by the calibrated
universal gradient identity, so the cofactor divisor in (3) is valid.

## 2. A conic forces cofactor degree seven

Suppose g=2 and define only for this coefficient-field calculation
\[
\xi=\ell(y,\vartheta),\qquad
\eta=\widetilde\ell(y,\vartheta).
\tag{4}
\]
This invertible L-linear transformation is not asserted to be an
ambient polynomial coordinate change. It preserves the rings generated
by the two projected entries and their fraction fields.

The nonzero degree-two leading vector of (y,vartheta) lies on ell=0.
The other line is distinct, so it does not vanish on this vector.
Therefore deg eta=2 and deg xi<2. The polynomial xi cannot be constant:
otherwise C=L[eta] and its fraction field has index two in L(v), since
eta is a quadratic polynomial in v. This contradicts (2). Hence
\[
\deg_v\xi=1,\qquad \deg_v\eta=2.
\tag{5}
\]
This argument works over the exact field L. In particular, it does not
require a root of the leading coefficient, rationality of L, or
geometric smoothness of the projected curve.

Since Gamma has degree two, Q1 has total degree four. From (3), its
top homogeneous part in the new formal variables xi,eta is exactly a
nonzero scalar multiple of xi eta cubed. Every other term has total
degree at most three. On evaluation, the former has degree seven by
(5), while all the latter have degree at most six. Thus
\[
\deg_vq_1=7,
\qquad \deg_vR\le2,
\qquad \deg_vR^3\le6.
\tag{6}
\]
The middle bound holds because the universal return is affine in
y,vartheta. Equation (6) contradicts the cofactor divisibility (3).
Thus no supplied frame (1) has g=2. The argument neither assumes
C=O nor replaces evaluated cofactor degree by total degree.

## 3. The precise surviving frontier

The complete actual line proof
[triple-root-lines223](rank-two-triple-root-constant-second-line-exclusion-pass223-working.md)
excludes g=1 in both selected directions. Its repeated-pair argument
uses an actual constant-second chart, a scalar-Jacobian split and a
primitive two-variable derivation over C[X,U]. Its distinct-pair
argument uses the local cubic Wang/Laurent contradiction after an
actual root-form change. Those are original-ring exclusions, not
consequences of the coefficient-field transformation (4).

Combining those line exclusions, Section2 and the nonsquare zero-return
lemma, every supplied frame (1), if it exists, must satisfy
\[
g=3,\qquad \deg_vR=3,\qquad
q_1=\gamma R^3\quad\text{for some }\gamma\in L^*.
\tag{7}
\]
To obtain the last two assertions, use the saturated case g=m=3
of222: its exact evaluated cofactor degree is nine. Divisibility
q1|R cubed and deg R<=3 therefore force equality of degrees and a
nonzero scalar quotient. This is an equality case, not a contradiction.

The cubic may still require separate singularity, original-ring or
Jacobian arguments. None is supplied here. In particular this note
does not prove nonrealizability, recognition or nonvacuity for the
entire triple-root sector. Arbitrary frame entry, height-two initial
kernels and unrestricted complex-threefold cancellation remain outside
its scope.

The complete saved220,221,222 and triple-root-line223 inputs were read
before composition. The cofactor top-degree argument was independently
reconstructed by Root. No saved checker was executed, imported or
compiled; no prior source, index or verification packet was edited.
These written checks are not expert review, proof-assistant certification
or historical novelty clearance.
