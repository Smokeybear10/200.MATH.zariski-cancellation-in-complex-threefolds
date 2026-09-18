# A moving-frame constraint for the exact cubic branch

An exact cubic relative relation forces a rank-one variation of the
quadratic velocity form. The coefficient vector of the cubic term
defines a rational direction on the invariant plane along which
that form is constant. This direction has a nonconstant rational
first integral. Over its invariant field, the velocity vector lies
in a fixed plane and a fixed quadratic level set.

These are necessary conditions under the supplied actual framework90.
They do not recognize the kernel, make the rational direction a
polynomial locally nilpotent derivation, or extend coordinates over
a missing divisor.

## 1. An affine graph without a base-coordinate change

Retain the full actual hypotheses and notation of
[cubic-relation90](nonconical-cubic-relation-pass90.md), now with
exact degree three for the relative evaluation kernel. Put
K=C(s1,s2). The elementary generic-coordinate argument there gives
a K-linear combination of y1,y2 that generates K[v].

The other generator is a degree-three polynomial in that coordinate.
An affine shift of v removes its quadratic term, and absorbing its
leading coefficient into a vector gives

\[
y=D+vX+v^3V,\qquad D,X,V\in K^2,\qquad
\delta=\det[X,V]\ne0 .
\tag{1}
\]

Only v has been changed. The vectors X and V need not be coordinate
vector fields on the base. We interpret their two components as
rational derivations of K in the original s1,s2 coordinates. In
particular their bracket must not be set to zero.

Let ell,m be the dual rows: ell(X)=m(V)=1 and ell(V)=m(X)=0.
The evaluation kernel has generator
F(Y)=m(Y-D)-ell(Y-D)^3. The potential has degree at most three,
so Phi-zeta=c0 F for c0 in K*. Comparing cubic terms gives

\[
T=\tau\,\ell^{\otimes3},\qquad \tau=-6c_0/q\ne0,
\qquad \ell(V)=0 .
\tag{2}
\]

The actual localized coordinate ring is still K[v,u]. A base-valued
affine change of its variable v changes the volume unit by an
element of K*, not by a v-dependent factor.

## 2. All positive volume coefficients

Use the torsion-free connection on the rational base vector fields
defined by the actual moving-frame coefficients C^j_ik of90:
( nabla_Z W )^j=Z(W^j)+sum C^j_ik Z^i W^k.
The nonzero constant term of the original volume and the full
gradient identity give

\[
w=X+3v^2V,\qquad
\frac{\mathcal J}{\Omega}
 =\frac{c_0}{\delta}\det(w,\nabla_w y),\qquad
\det(w,\nabla_w y)\in K^* .
\tag{3}
\]

Here nabla differentiates the coefficients in (1), holding v fixed.
For completeness, the three-by-three determinant90 equals
Z^t Kmat w because Z^t w=0 and
adj(uI+Kmat)=(u+tr Kmat)I-Kmat. The term rho I in Kmat
drops out. Since Z=c0(m-3v^2 ell), the remaining product is
exactly (3).

Expand before imposing any frame relations:

\[
\nabla_w y
 =\nabla_XD+v\nabla_XX+3v^2\nabla_VD
 +v^3(\nabla_XV+3\nabla_VX)+3v^5\nabla_VV .
\tag{4}
\]

The coefficients at v, v^7 and v^4 respectively show that
nabla_X X is proportional to X, nabla_V V to V, and
nabla_V D to V. The coefficients at v^3,v^5,v^2
give the remaining equalities below. The constant term is nonzero.
Thus there are a,c,d,e,f,h,j,k in K such that

\[
\begin{gathered}
\nabla_XX=aX,\qquad \nabla_XV=cX+dV,\qquad
\nabla_VX=eX+fV,\qquad \nabla_VV=hV,\\
d=3a-3f,\qquad h=c+3e,\qquad
\nabla_XD=jX+kV,\qquad \nabla_VD=jV,\qquad k\ne0,\\
[X,V]=(c-e)X+(d-f)V .
\end{gathered}
\tag{5}
\]

Conversely these coefficient conditions make the determinant in
(3) equal to k delta. This converse is only a formal volume
identity. It does not produce an actual original-coordinate inverse.

## 3. A rational first integral of the cubic direction

Return to the three-dimensional velocity moving frame
C=[b,b_s1,b_s2] and let G be its symmetric radial coefficient matrix.
As in117 define H=diag(-1,G), Q=C^(-t) H C^(-1).
No nondegeneracy assumption on G or Q is made. The unspecialized
derivative calculation, now retaining T, gives

\[
\begin{gathered}
n=C^{-t}(0,\ell_1,\ell_2)^t,\qquad
\partial_i Q=-\tau\ell_i\,n n^t,\qquad V(Q)=0,\\
b^tQb=-1,\qquad n^t b=0,\qquad
n^t b_X=1,\qquad n^t b_V=0 .
\end{gathered}
\tag{6}
\]

To check the sign, the lower-right block of
partial_i H-M_i^t H-H M_i is -T_ijk. Formula (2) gives
(6) after conjugating by C^(-1). Since tau and n are nonzero
and ell is a nonzero row, Q has at least one nonconstant entry.

The ambient derivative of n along V is -e n. Indeed differentiate
its three pairings with the basis b,b_X,b_V. The derivatives of b_X
and b_V have tangential parts b_(nabla_V X) and b_(nabla_V V);
their radial components do not contribute to n. Formula (5)
therefore gives pairings 0,-e,0 for V(n), as required.

Let L be the field of rational functions killed by V. A nonconstant
entry of Q lies in L, so trdeg_C L is at least one. It cannot
contain two algebraically independent elements: K would be
algebraic over their rational function field, and in characteristic
zero a derivation vanishing on that field vanishes on K as well.
That would contradict V being a nonzero rational vector field.
Consequently

\[
\operatorname{trdeg}_{\mathbb C}L=1,\qquad
Q\in\operatorname{Mat}_3(L),\qquad
\widehat n=n/n_j\in L^3,\qquad
\widehat n^t b=0,\qquad b^tQb=-1
\tag{7}
\]

for any nonzero component n_j. The ratios are invariant because
V(n)=-e n. No assertion that L already has a chosen global
polynomial generator is used.

The plane and quadratic equation in (7) are defined over L.
Their intersection need not be a smooth nondegenerate conic.
The conclusion does not identify the full coordinate ring of the
generic fiber or descend a coordinate to C[s1,s2].

## 4. Limits and literature comparison

Rank-one T does not imply constant Q in both base directions.
The explicit principal-open cubic example in
[local model118](cubic-principal-open-frame-control-pass118.md) tests
this boundary with actual polynomial-coordinate formulas after
localization. A local inverse cannot be promoted across its
excluded divisor without a separate argument.

The identities resemble centroaffine structure equations, but no
classification theorem is imported here. In particular Hildebrand's
classification concerns nondegenerate real immersions with cubic
form parallel for the Levi-Civita connection.[^hildebrand] Neither
nondegeneracy, that parallelism, nor its real geometric hypotheses
have been established in the present complex rational setting.
Rank one is not a substitute for parallelism.

The proof consists of exact algebra in the supplied actual frame.
It does not imply cubic-branch recognition or entry for an arbitrary
cylinder. Novelty, human expert review and formal verification are
unestablished.

[^hildebrand]: Roland Hildebrand, [*Centro-affine hypersurface immersions
with parallel cubic form*, arXiv:1208.1155v4](https://arxiv.org/abs/1208.1155v4),
revised January 4, 2013. The primary abstract and version history were
read for this exclusion of applicability, not the complete
classification proof.
