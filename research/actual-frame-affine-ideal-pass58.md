# An actual Jacobian condition on the affine-slice ideal

The genuine ambient coordinate Jacobian gives a necessary ideal
containment for the affine-slice module. Its normalized four-function
Jacobian belongs to the actual affine-slice ideal, with full
multiplicities. In particular, a unit normalized Jacobian supplies
an actual affine generic slice.

This is a differential subcase, not a proof that the normalized
Jacobian is a unit. The faithful control from pass57 satisfies the
new necessary containment while its affine-slice ideal remains
proper. The missing full-frame argument is not replaced by an
assumption that four generators over the invariant base are
ambient coordinates.

## 1. Actual hypotheses and the invariant base Jacobian

Retain the full independent-defect degree-two hypotheses of
[the actual generic graph](generic-bad-pair-pass44.md):
\[
B=\mathbb C[x_1,x_2,x_3,x_4]=A[s_*],\qquad Es_*=1,
\]
\[
C=\ker D=\mathbb C[a,b],\qquad
R=C_{\mathfrak m},\qquad L=\operatorname{Frac}R,\qquad
\mathcal B=B_R.
\tag{1}
\]
The letters \(a,b\) here are actual polynomial coordinates
of the invariant plane, not the original bad speeds and
not coordinates of the ambient four-space. Their shifts
by their values at \(\mathfrak m\) are regular parameters.

The inherited bad pair and fields satisfy
\[
\mathcal B_L=L[x_3,x_4],\qquad
E=f\partial_{x_3}+g\partial_{x_4},\qquad
K_3=-\Delta\partial_{x_4},\quad
K_4=\Delta\partial_{x_3},\quad 0\ne\Delta\in C.
\tag{2}
\]
The speeds \(f,g\) are algebraically independent.
Put
\[
\delta_C=
\det\frac{\partial(a,b,x_3,x_4)}
          {\partial(x_1,x_2,x_3,x_4)}
=\det
\begin{pmatrix}
T_1a&T_2a\\
T_1b&T_2b
\end{pmatrix},
\qquad T_i=\partial_{x_i}.
\tag{3}
\]
This is an actual polynomial determinant.

The actual good-partial calculation in pass44, equations
(18)--(19), gives
\[
U=\frac{\partial(f,g)}{\partial(x_1,x_2)},\qquad
\det U\in L^*.
\]
The two field derivations with respect to \(f,g\) extend
uniquely to \(L\), because characteristic is zero and
\(L/\mathbb C(f,g)\) is finite algebraic. The chain rule
therefore gives
\[
\delta_C=
\det\frac{\partial(a,b)}{\partial(f,g)}\,\det U
\in L^*.
\]
Both coordinate pairs are transcendence bases, so the
first determinant is nonzero. Since \(B\cap L=C\),
\[
0\ne\delta_C\in C.
\tag{4}
\]
This invariance is an inherited consequence of the actual
good partials, not a generic determinant assumption for
an arbitrary quadratic-generator model.

## 2. The normalized Jacobian of the affine module

By [the finite affine-module theorem](affine-slice-module-pass57.md),
\[
V=\mathcal B\cap L[x_3,x_4]_{\le1}
  =R\cdot1\oplus Ru\oplus Rv,
\qquad
\mathfrak s_{\mathrm{aff}}=E(V)=(Eu,Ev)R.
\tag{5}
\]
The elements \(u,v\) are actual functions, not asserted
to be ambient coordinates. Set
\[
\alpha_u=K_4u,\quad\beta_u=-K_3u,\qquad
\alpha_v=K_4v,\quad\beta_v=-K_3v.
\]
All four coefficients are in \(R\). Define
\[
\kappa=\alpha_u\beta_v-\beta_u\alpha_v\ne0.
\]
Then the actual Jacobian
\[
\delta_V=
\det\frac{\partial(a,b,u,v)}
          {\partial(x_1,x_2,x_3,x_4)}
\]
has the exact generic formula
\[
\delta_V=\delta_C\,\frac{\kappa}{\Delta^2}.
\tag{6}
\]
To see it, hold \(a,b\) fixed and differentiate the
affine expressions for \(u,v\) in the bad pair. Their
two-by-two coefficient determinant is
\(\kappa/\Delta^2\). In the full four-by-four chain
rule, derivatives of their base-dependent coefficients
do not change this block determinant.

The determinant on the left is actual: the true ambient
partials preserve \(\mathcal B\), including its inverted
invariant denominators. Equation (6) also puts it in \(L\).
Consequently
\[
0\ne\delta_V\in\mathcal B\cap L=R.
\tag{7}
\]
Changing the basis \(1,u,v\) of \(V\) while retaining \(1\)
changes \(\delta_V\) by a unit of \(R\). In fact the
induced change on \(V/R\) is an invertible two-by-two
matrix over \(R\); all derivatives of its coefficients
disappear after wedging with \(da\wedge db\).
Thus the principal ideal \(\delta_VR\) is well-defined
for the selected affine module and invariant coordinates.

## 3. The true ambient adjugate and the original slice

Let \(J\) be the four-by-four Jacobian matrix in (6), with
rows corresponding to \(a,b,u,v\), and let
\(P=(Ex_1,\ldots,Ex_4)^{\mathsf t}\).
Because \(E\) kills the invariant base,
\[
JP=(0,0,Eu,Ev)^{\mathsf t}.
\]
The polynomial adjugate identity gives
\[
\delta_VP
=\operatorname{adj}(J)(0,0,Eu,Ev)^{\mathsf t}.
\tag{8}
\]
All cofactors belong to \(\mathcal B\), even when the
determinant is a nonunit or vanishes on a divisor.

Multiply (8) by the actual row
\((T_1s_*,\ldots,T_4s_*)\). Since \(Es_*=1\), this proves
\[
\delta_V\in(Eu,Ev)\mathcal B.
\]
Faithful flatness contracts every extended ideal:
\((Eu,Ev)\mathcal B\cap R=(Eu,Ev)R\).
Together with (7), this gives the exact condition
\[
\boxed{\delta_V\in\mathfrak s_{\mathrm{aff}}.}
\tag{9}
\]
This is membership in the full ideal, not just in its
radical. No primitive rescaling of \(E\), transfer of its
slice, or inverse of \(J\) was used.

The same calculation with the actual four functions
\(a,b,x_3,x_4\) instead yields
\[
\delta_C\in(f,g)R.
\tag{10}
\]
It is essential that the cofactors in this argument are
taken with respect to the original ambient polynomial
coordinates, whose derivations actually act on the ring.
A four-generator presentation over \(R\) is not a
substitute for such a frame.

In particular,
\[
\delta_V\in R^*
\quad\Longrightarrow\quad
\mathfrak s_{\mathrm{aff}}=R
\quad\Longrightarrow\quad
\text{an actual affine generic \(E\)-slice exists}.
\tag{11}
\]
The projection theorem from pass49 then gives
\(\mathcal A=R[F_2(\mathcal A)]\). Its separate recognition
hypotheses are not being discarded.

## 4. An equivalent full-multiplicity condition on \(\Gamma\)

Write the exact coefficient lattice from pass57 as
\[
\Gamma=
\{(\gamma,\alpha,\beta)\in R^3:
 \gamma+\alpha x_3+\beta x_4\in\Delta\mathcal B\}.
\]
The basis \(1,u,v\) corresponds to the lattice basis matrix
\[
G=
\begin{pmatrix}
\Delta&\gamma_u&\gamma_v\\
0&\alpha_u&\alpha_v\\
0&\beta_u&\beta_v
\end{pmatrix},
\qquad \det G=\Delta\kappa.
\]
Equations (6) and (9) give
\[
\Delta^3\delta_V=\delta_C\det G,\qquad
\boxed{\delta_C\det G\in
       \Delta^3\mathfrak s_{\mathrm{aff}}.}
\tag{12}
\]
The determinant of a different lattice basis changes
by a unit. Thus (12) is an intrinsic determinant-ideal
condition on this fixed affine lattice, not a choice of
generic coefficient representatives.

For every height-one prime \(\pi\), (12) implies
\[
v_\pi(\delta_C)+v_\pi(\det G)
\ge 3v_\pi(\Delta)+v_\pi(\mathfrak s_{\mathrm{aff}}).
\tag{13}
\]
Here the valuation of an ideal is the minimum valuation
of its elements. The statement retains every divisor
multiplicity. It does not assert that height-one
inequalities settle possible closed-point ideal defects.

## 5. Exact limitation and deduplication

The [faithful control from pass57](faithful-quadratic-slice-boundary-pass57.md)
has invariant coordinates \(a,b=t^2-az\), localizing where
\(b\) is a unit, and affine-module basis \(1,t,w\), where
\(w=as+tz\). Directly in the true ambient coordinates
\((a,t,z,s)\),
\[
\det\frac{\partial(a,t^2-az,t,w)}
          {\partial(a,t,z,s)}=a^2,
\qquad
\mathfrak s_{\mathrm{aff}}=aR.
\tag{14}
\]
Thus it satisfies (9) while the affine-slice ideal remains
proper. The cofactor multiplying \(Ew=a\) when applying
(8) to its actual slice \(s\) is \(a\).
The Jacobian criterion above therefore does not by itself
exclude that weaker model. Its displayed four quadratic
generators still fail the actual-coordinate requirement
proved in the linked note.

The invariant determinant (4), the generic quadratic graph,
and the good-partial identities are inherited from pass44.
Pass49 supplies generation after an affine slice has been
found. The full cubic-generation obstruction in pass51 is
not used or weakened here. The added statement is the
normalized affine-lattice determinant condition (9)--(13)
and its unit-Jacobian subcase.

An exact inline SymPy check on the reused control verified
(14), the indicated cofactor, and every component of (8).
No new standalone test suite is counted. The general
adjugate and ideal-contraction arguments are proved above.

What remains is an actual-frame argument forcing the
normalized determinant to be a unit, or otherwise forcing
\(\mathfrak s_{\mathrm{aff}}=R\), in a genuinely relevant
subcase. The present identities do not establish either
conclusion at an arbitrary obstruction point.

