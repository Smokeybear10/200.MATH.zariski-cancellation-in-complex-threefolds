# The direct two-invariant conic extension collapses

The symmetric-square construction from pass75 cannot acquire a new
velocity parameter by allowing its matrix coefficients to depend on
the additional invariant U. If the resulting displayed polynomial
map has a polynomial inverse, its two velocity parameters must
already be independent of U. The remaining U-dependence is precisely
a harmless change of the Bezout pair.

This is an obstruction for one explicit construction, not an
assertion about every two-invariant nice action. It constructs neither
a primitive intrinsic fixed-point example nor a nice sliced action
with no constant good direction.

## 1. The proposed larger construction

Use independent variables (a,U,V,S). Let
u,v,r,s belong to R=C[a,U], with
\[
ru+sv=1,\qquad
N=\begin{pmatrix}s&u\\-r&v\end{pmatrix},\qquad
N^{-1}=\begin{pmatrix}v&-u\\r&s\end{pmatrix}.
\tag{1}
\]
Thus either velocity parameter may vanish, but the pair cannot
vanish simultaneously. Define the polynomial map Phi by
\[
\begin{aligned}
x&=s^2U+2suV+u^2S,\\
y&=-srU+(sv-ru)V+uvS,\\
z&=r^2U-2rvV+v^2S,\\
w&=a-US+V^2.
\end{aligned}
\tag{2}
\]
All four outputs are affine in S. Pointwise matrix multiplication
gives
\[
\begin{pmatrix}x&y\\y&z\end{pmatrix}
=N\begin{pmatrix}U&V\\V&S\end{pmatrix}N^t,
\qquad xz-y^2=US-V^2,
\qquad a=xz-y^2+w.
\tag{3}
\]
These identities alone do not prove that Phi has an inverse:
the coefficients of N now involve the input U that one would
need to recover from the output.

If Phi were an actual polynomial automorphism, transporting
partial_S through it would give a globally sliced nice action E.
Its output velocities would be (u^2,uv,v^2,-U), evaluated through
the actual inverse. This motivates the ansatz, but neither that
inverse nor the original good-partial condition is assumed to
follow merely from (1)--(3).

**Claim.** The map (2) is a polynomial automorphism if and only
if u and v lie in C[a]. In that case it gives exactly the same
original action as the one-variable conic construction of pass75.

## 2. A necessary full Jacobian identity

Replace the output coordinate w by a=xz-y^2+w, and order the
outputs as (a,x,y,z). This is an actual polynomial coordinate
change on the output space. Since a is preserved, polynomial
invertibility of Phi implies that the determinant in the remaining
three variables (U,V,S), with a fixed, is a nonzero complex
constant.

Let a subscript U denote the polynomial derivative holding a
fixed, and write
\[
K=N^{-1}N_U
=\begin{pmatrix}k_{11}&k_{12}\\k_{21}&-k_{11}\end{pmatrix},
\qquad
k_{11}=v s_U+u r_U,
\quad k_{12}=v u_U-u v_U.
\tag{4}
\]
The trace is zero by differentiating det N=1. Let M be the
symmetric matrix with entries (U,V,S). Differentiating N M N^t
and multiplying on the left and right by N^{-1} and N^{-t}
gives
\[
dM+(KM+MK^t)\,dU.
\]
The linear symmetric-square map given by N has determinant
(det N)^3=1. The remaining change is a rank-one update of the
identity on the three-dimensional space of symmetric matrices.
Its determinant is one plus the first entry of KM+MK^t.
Consequently the exact full determinant is
\[
\det\frac{\partial(x,y,z)}{\partial(U,V,S)}
=1+2U(vs_U+ur_U)+2V(vu_U-uv_U).
\tag{5}
\]
No matrix derivative in the independent input a contributes to
this determinant, because the first output is a itself.

If (2) is a polynomial automorphism, comparison of the coefficient
of V in (5) gives
\[
v u_U-u v_U=0.
\tag{6}
\]
This is a necessary condition obtained from actual invertibility.
We are not using a constant Jacobian as a sufficient inverse test.

## 3. The velocity cannot depend on the second invariant

Work temporarily in the PID C(a)[U]. Equation (1) keeps u,v
coprime in this ring. If both are nonzero, (6) says that their
rational quotient u/v has zero U-derivative. In characteristic
zero the constants of C(a)(U) for this derivative are C(a),
so u and v are proportional over C(a).

Since proportional polynomials that generate the unit ideal in
C(a)[U] must both be units in that ring, each is independent of
U. Their original polynomial membership then gives u,v in C[a].
If one is zero, (1) already forces the other to be a unit of
C[a,U], so the same conclusion holds. This proves necessity
in the claim, including both zero-axis cases.

For completeness, no differential-field classification is hidden
here. For a reduced fraction f/g in C(a)(U), the equation
(f/g)_U=0 implies g divides g_U. A nonconstant polynomial g
cannot divide its derivative. Thus g is constant; then f_U=0
forces f constant as well.

## 4. Every surviving map has an explicit inverse

Suppose conversely that u,v lie in C[a]. Evaluating (1) at
U=0 supplies r0,s0 in C[a] with r0 u+s0 v=1. Every solution
of (1) then has the form
\[
r=r_0+k v,\qquad s=s_0-k u,
\qquad k\in C[a,U].
\tag{7}
\]
Indeed k=s0(r-r0)-r0(s-s0) gives these two identities directly
from u(r-r0)+v(s-s0)=0. This proof includes zero components.

Write N0 for the matrix (1) formed from r0,s0. Then
N=N0 G with G=((1,0),(-k,1)). Thus (2) is the composition
of the following explicit polynomial automorphism with the
one-variable inverse map from pass75:
\[
\begin{aligned}
\mathcal G(a,U,V,S)
  &=(a,U,V-kU,S-2kV+k^2U),\\
\mathcal G^{-1}(a,U,V_0,S_0)
  &=(a,U,V_0+kU,S_0+2kV_0+k^2U).
\end{aligned}
\tag{8}
\]
Here k(a,U) is unchanged by both maps, so direct substitution
checks both inverse orders. Also U S0-V0^2=US-V^2.
The pass75 inverse first recovers a=xz-y^2+w and then applies
the symmetric-square matrix N0^{-1}; its two inverse orders are
proved in [the conic family note](conic-nice-pair-classification-pass75.md),
equations (2)--(4). Composing these actual inverses proves the
sufficiency assertion, rather than appealing to (5).

## 5. Consequence for the proposed primitive fixed-point control

The map G fixes a,U and changes S with coefficient one; its
other components are independent of S. Therefore it transports
partial_S to partial_S. The original action produced by every
surviving map (2) is exactly
\[
E=(u(a)^2,u(a)v(a),v(a)^2,
       -v(a)^2x+2u(a)v(a)y-u(a)^2z)\cdot\partial,
\quad a=xz-y^2+w.
\tag{9}
\]
In particular the original constant partial T=partial_w is good
for this actual action. In the nonconstant-pair branch, its
derived field is independent of E, and pass75 gives both
G2=C e_w and a primitive intrinsic coordinate partial. The
wedge ideal after dividing by its gcd is consequently the unit
ideal, for every supplied E-slice. In the constant-pair branch
the derived field is zero and is not a candidate for the required
independent auxiliary action.

Thus arbitrary polynomial U-dependence in the Bezout matrix does
not enlarge the class of original actions or evade the primitive
freeness conclusion in this ansatz. A genuine construction must
change some further feature, for example the invariant placement,
the determinant-preserving form, or the dependence on the other
slice coordinates. No such larger construction is classified or
excluded here.

## 6. Scope and verification

The pass75 family assumes u,v in C[a] from the outset, whereas
this note derives that restriction from actual invertibility for
the proposed two-invariant extension (2). The earlier elementary
shear obstruction does not supply the determinant calculation (5)
or this iff inverse criterion. The new result is the exact limitation
on this additional construction route, not a general recognition
theorem, a general existence theorem for a good direction, or a
historical novelty claim.

All arguments are polynomial matrix calculations or elementary
one-variable coefficient arguments. There is no new external
classification theorem, numerical suite, full regression, human
review, or proof-assistant certificate. The complete proof was
author-read through EOF. Frozen passes through75 and shared
metadata are unchanged.
