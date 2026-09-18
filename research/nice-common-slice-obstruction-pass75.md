# Two sliced commuting actions need not admit an invariant slice for the first

There is an explicit nice sliced action on complex four-space whose
sole constant good partial produces a second, also globally sliced,
commuting LND. No slice for the first action is invariant under that
particular second action. Both actions and the original quotient are
nevertheless completely recognized by actual polynomial coordinates.

This strengthens the preceding supplied-slice countercontrol: replacing
the first slice cannot repair this pair. It does not prevent replacing
or adjusting the second action. It is not a cancellation counterexample
or a historical novelty claim.

## 1. Actual polynomial fields and invariant

In B=C[x,y,z,w], set
\[
a=xz-y^2+w,\qquad u=a,\qquad v=a^2+1,
\]
\[
f_0=u^2=a^2,\quad f_1=uv=a^3+a,\quad
f_2=v^2=a^4+2a^2+1.
\tag{1}
\]
Primes on the f_i below mean ordinary differentiation as polynomials
in the one indeterminate a. Define the actual polynomial velocity and
derivations
\[
P=(f_0,f_1,f_2,-f_2x+2f_1y-f_0z)^t,
\qquad E=P\cdot\partial,
\]
\[
T=\partial_w,\qquad Q=(TP)\cdot\partial.
\tag{2}
\]
The letters E,Q denote derivations, and Q(x,y,z,w) denotes its
coefficient column when used in a matrix formula. This Q is not an
arbitrarily chosen centralizer: it is exactly the derivative along an
original actual coordinate partial.

Directly from (1)--(2), Ea=0. Also f_1^2=f_0f_2, so
\[
E(P)=0.
\tag{3}
\]
For the fourth component this is the equality
-f_2f_0+2f_1^2-f_0f_2=0. The first three components are
functions of the invariant a. Thus E is nice and locally nilpotent;
its actual flow is x_vec+tP with polynomial inverse x_vec-tP.
The explicit coordinates below also independently establish this.

## 2. Complete polynomial coordinates, not just a Jacobian test

Define
\[
U=v^2x-2uvy+u^2z,
\]
\[
V=-avx+(v+au)y-uz,\qquad S=a^2x-2ay+z.
\tag{4}
\]
The four polynomials (a,U,V,S) are actual coordinates. Their inverse,
with a,U,V,S now independent target variables, is
\[
x=U+2uV+u^2S,
\]
\[
y=aU+(v+au)V+uvS,\qquad
z=a^2U+2avV+v^2S,
\]
\[
w=a-US+V^2.
\tag{5}
\]
In (5), u=a and v=a^2+1 as before. To check both inverse orders,
first replace the original w by a-xz+y^2. This identifies the
original ring exactly with C[a,x,y,z]. Over C[a], the transformation
of (x,y,z) in (4) is the symmetric-square transformation associated
with the matrix
\[
L=\begin{pmatrix}v&-u\\-a&1\end{pmatrix},\qquad
L^{-1}=\begin{pmatrix}1&u\\a&v\end{pmatrix},\qquad
\det L=v-au=1.
\tag{6}
\]
Indeed, if (x,y,z) are the entries of a symmetric two-by-two matrix,
its transformation is L times that matrix times L^t. Multiplication
by L^{-1} on both sides gives the first three equations of (5),
and determinants give US-V^2=xz-y^2. The fourth equation of (5)
then recovers the original a and w in both orders. This verifies
global polynomial inverses, not merely local invertibility.

In these actual coordinates, direct evaluation gives
\[
Ea=EU=EV=0,\qquad ES=1,
\qquad E=\partial_S.
\tag{7}
\]
Consequently the original action has a global slice S and
kerE=C[a,U,V]. This construction is an elementary member of the
conic-velocity family f_1^2=f_0f_2, rather than an unknown kernel.

## 3. The second action is globally sliced as well

Since Ta=1, the second velocity in (2) is
\[
Q(x,y,z,w)=(f_0',f_1',f_2',-f_2'x+2f_1'y-f_0'z)^t.
\tag{8}
\]
It kills a. Evaluation in (4) gives the exact simpler description
\[
Qa=QU=0,\quad QV=1-a^2,\quad QS=2a,
\qquad Q=(1-a^2)\partial_V+2a\partial_S.
\tag{9}
\]
This makes Q a polynomial LND commuting with E. Their generic
rank is two. Moreover
\[
\rho=V+\frac a2S,\qquad Q\rho=(1-a^2)+a^2=1.
\tag{10}
\]
Thus Q has an actual polynomial slice and no fixed point, not merely
coefficient gcd one. Both original E and derived Q are globally sliced.
The pair becomes dependent on the nonempty divisors a=1 and a=-1,
where Q=2E and Q=-2E respectively. Having no fixed points individually
does not make the joint action pointwise independent.

The simple target form also gives Q(P)=0. In the original frame,
Q^2x=Q^2y=Q^2z=0 but
\[
Q^2w=2(1-a^2)^2\ne0,\qquad Q^3(x,y,z,w)=0.
\tag{11}
\]
For example, use w=a-US+V^2 and (9). Thus Q is not nice in the
original displayed frame, though it is nice in (a,U,V,S).

## 4. The sole constant good direction is the one used above

Let J=Jac P, let r=(z,-2y,x,1), and put
\(\ell=(-f_2,2f_1,-f_0,0)\). Write q_col=Q(x,y,z,w).
Differentiating the actual coefficients, including the explicit
x,y,z terms in P_4, gives
\[
J=q_{\rm col}r+e_w\ell,\qquad
rq_{\rm col}=0,\quad\ell q_{\rm col}=0,
\quad re_w=1,\quad\ell e_w=0.
\tag{12}
\]
The second zero follows from differentiating f_1^2=f_0f_2.
Therefore
\[
J^2=q_{\rm col}\ell,\qquad J^3=0,\qquad
\operatorname{rank}J=2,\qquad\operatorname{rank}J^2=1.
\tag{13}
\]
For rankJ=2, q_col and e_w are independent, and r and ell are
independent since their fourth entries are respectively one and zero.
All ranks here are over FracB.

If a constant column c belongs to kerJ^2, (13) gives
-c_1(a^2+1)^2+2c_2a(a^2+1)-c_3a^2=0. Comparing powers of
the transcendental polynomial a gives c_1=c_2=c_3=0. Hence
G_2=C e_w. As Je_w=q_col is nonzero, G_1=0. The exact
adjoint formula in [pass74](nice-slice-adjoint-rank-pass74.md)
now gives ad_E^2 T=0, [E,T]=-Q, and displayed profile(2,2,2,1).
There is no assertion that its minimum over nonlinear frames is eleven:
the actual translation frame (7) already disproves that.

There is not even an affine-linear invariant or slice for E in the
original frame. A constant relation among 1 and the four P_i has zero
coefficient on P_4 by independence of x,y,z over C[a]. Comparing the
degrees four, three and two then makes the other coefficients zero.
Recognition in this example genuinely uses nonlinear coordinates.

## 5. No choice of E-slice can be fixed by this Q

Every polynomial E-slice in the actual coordinates (7) is
F=S+h(a,U,V), since EF=1. Equation (9) then gives
\[
QF=2a+(1-a^2)\partial_Vh.
\tag{14}
\]
It cannot vanish: in the nonzero quotient B/(a-1), its value is
the nonzero constant two. Equivalently, on that divisor Q=2E,
so EF=1 would force QF=2. This proves nonexistence for every
polynomial F, not failure of a bounded-degree slice search.

The obstruction concerns selection of a slice while holding Q fixed.
It does not contradict the general [slice-fixing adjustment](good-partial-slice-adjustment-scope-pass75.md).
For the chosen S, that adjustment is
\[
Q_0=Q-(QS)E=Q-2aE=(1-a^2)\partial_V.
\tag{15}
\]
It is a polynomial LND fixing S, but now vanishes on a=±1.
Its restriction to kerE has image contained in the proper principal
ideal(1-a^2), so that restriction has no slice. In this recognized
example primitive division removes the factor and gives the actual
coordinate partial ∂V. This positive repair uses the supplied inverse
coordinates; it is not a general primitive-division recognition theorem.

## 6. What changes in the unresolved investigation

The [earlier boundary](nice-good-partial-boundary-pass75.md) showed
that the original supplied slice need not be fixed, but that example
had a different slice fixed by Q. Here there is no such replacement.
The older [centralizer control](nice-centralizer-bridge-pass40.md)
already distinguished an auxiliary kernel from the original kernel
and warned against slice transfer. The present construction additionally
retains all of the one-good-partial hypotheses and global slices for
both actions. It disproves common-slice selection under those stronger
conditions, not existence of some other recognizing action or frame.

The standalone [exact checker](nice_common_slice_checks_pass75.py)
tests actual coordinate inverses, fields, matrix decomposition, the
constant good space, both slice identities and the divisor obstruction.
The universal nonexistence statement follows from (14), not finite
sampling. All mathematical ingredients used for this construction are
displayed above; no external classification or novelty claim is needed.
General cancellation and arbitrary one-good-partial recognition remain
unproved. Frozen passes through74 are unchanged.
