# What quotient rank and a unit speed row do not supply

Even the full elementary quadratic quotient geometry, an actual polynomial
cylinder, a nonconstant nonconical determinant, and the exact relative
generator pencil do not force a constant linear combination of the proposed
good speeds to be a nonzero constant. The example below retains those
properties, and its proposed bad function is an actual coordinate with
constant nonzero acceleration.

The proposed four functions are **not** an original coordinate system:
their Jacobian has an explicit zero even on the open set where the
intrinsic quotient action is free. This is a sharp obstruction to omitting
the original-coordinate hypothesis, not a counterexample to the actual-frame
theorem or to cancellation. The invariant ring in this example is already
polynomial.

## 1. An actual quadratic quotient with no rank-zero point

Take the literal polynomial rings and derivations
\[
\begin{gathered}
A=\mathbb C[a,y,v],\qquad B=A[u],\qquad E=\partial_u,\\
N=a\partial_y+y\partial_v,\qquad
t=2av-y^2,\qquad S=\mathbb C[a,t].
\end{gathered}
\tag{1}
\]
The derivation N is locally nilpotent by its triangular formula. It has
coefficient gcd one, commutes with E, and kills u. Its kernel on A is
exactly S. Indeed,
\(A_a=\mathbb C[a,a^{-1},t,y]\) and \(N=a\partial_y\) there. If a minimal
denominator expression \(a^{-n}f(a,t)\), with \(n>0\) and a not dividing f,
belonged to A, reduction of \(a^n(a^{-n}f)=f\) modulo a would give
\(f(0,-y^2)=0\). Since \(-y^2\) is transcendental over \(\mathbb C\), this
would imply \(f(0,T)=0\), a contradiction. This proves the contraction.

With respect to the actual coordinate volume in the order \(u,a,y,v\),
the Jacobian derivation \(\operatorname{Jac}(a,t,u,-)\) is \(-2N\).
Thus N is an actual primitive Jacobian quotient field, up to a nonzero
complex scalar. It is not being asserted to be the highest adjoint of E
for the later, noncoordinate tuple.

There is an exact presentation and generic degree-two graph:
\[
\begin{gathered}
A=S[y,v]/(y^2-2av+t),\qquad
A\text{ is free over }S[v]\text{ with basis }1,y,\\
K=\operatorname{Frac}S,\qquad
A_K=K[y],\qquad v=\frac{y^2+t}{2a},\\
N^2y=0,\qquad N^3v=0,\qquad
\operatorname{rank}(da,dt)_p\ge1\quad\text{for every }p\in\operatorname{Spec}A.
\end{gathered}
\tag{2}
\]
In particular S embeds faithfully flatly into A. The rank assertion follows
from the everywhere nonzero differential da.

The closed fibers can be read from the same presentation. If \(a\ne0\),
the fiber is an affine line. If \(a=0\) and \(t\ne0\), it is two disjoint
reduced affine lines. At \((a,t)=(0,0)\), the whole fiber is
\(\mathbb C[y,v]/(y^2)\). It is free of rank two over the actual parameter
ring \(\mathbb C[v]\). These are exactly the relevant smooth reduced
components, disjointness, and finite-thickening phenomena; the double
fiber is retained rather than replaced by its reduction. N has fixed locus
\(V(a,y)\), with image the single base point \((0,0)\).

## 2. A unit speed row without a constant linear slice

On the actual plane S set
\[
b=\begin{pmatrix}a\\at-1\\t^2\end{pmatrix},\qquad
(t,-1,0)b=1,\qquad
\Omega=\det[b,b_a,b_t]=t(at+2)\ne0.
\tag{3}
\]
The speed map has generic rank two: the derivative minor of its first two entries
is a. The determinant is nonconstant. The row b has no nonzero complex
linear combination that is constant. Explicitly,
\[
\alpha a+\beta(at-1)+\gamma t^2\in\mathbb C
\]
forces \(\beta=\gamma=\alpha=0\), by the coefficients of \(at,t^2,a\).
This proves an all-coefficient statement, not a finite sample.

The field N is also free on \(A_\Omega\). Its image ideal is \((a,y)A\);
this contains \(t=2av-y^2\), which is a unit after inverting \(\Omega\).
Thus retaining freeness on this specified open set does not fix the
constant-linear-speed issue.

The row admits a particularly simple determinant-one completion over S:
\[
C=
\begin{pmatrix}
a&1&0\\ at-1&t&0\\ t^2&0&1
\end{pmatrix}\in\operatorname{SL}_3(S),\qquad
\begin{pmatrix}X_1\\X_2\\X_3\end{pmatrix}
=C\begin{pmatrix}u\\y\\v\end{pmatrix},\qquad Z=a+u^2.
\tag{4}
\]
Thus \(X_1=au+y\), \(X_2=(at-1)u+ty\), and \(X_3=t^2u+v\).
All these expressions are actual polynomials in B.

## 3. The exact relative inverse and pencil still hold

Over S the completion has the exact inverse
\[
\begin{gathered}
\sigma=tX_1-X_2=u,\qquad
A_1=X_1-a\sigma=y,\qquad A_2=X_3-t^2\sigma=v,\\
c=Z-\sigma^2=a,\qquad h=u-\sigma=0,\qquad
R=S[A_1,A_2]=A=R[c],\\
B=S[X_1,X_2,X_3,Z],\qquad
A[\tau]=R[\tau,c+\tau h].
\end{gathered}
\tag{5}
\]
Both the displayed relative generation and the universal pencil are
literal equalities here. In particular \(A_\Omega=R_\Omega\) and
\(\operatorname{Frac}A=\operatorname{Frac}R\); there is no hidden
normalization or coefficient-pole issue in this example. Every divisor
fiber also has noncollapsed image under R, since R is A itself.

However, (5) is an inverse **over S**. It does not express the elements
a and t as polynomials in \(X_1,X_2,X_3,Z\) over \(\mathbb C\).
Treating a determinant-one S-matrix as an ambient coordinate change
would incorrectly delete this distinction.

The bad function Z is independently a true coordinate: the map
\((u,a,y,v)\mapsto(u,Z,y,v)\) has polynomial inverse
\(a=Z-u^2\). Moreover
\[
EX_i=b_i,\qquad E^2X_i=0,\qquad EZ=2u,\qquad E^2Z=2,\qquad
u=EZ/2.
\tag{6}
\]
So the slice is exactly the canonical slice supplied by this coordinate's
constant acceleration. For an affine linear expression
\(L=\alpha X_1+\beta X_2+\gamma X_3+\delta Z+\epsilon\),
the equation \(EL\in\mathbb C\) first forces \(\delta=0\), by its u
coefficient, and then forces \(\alpha=\beta=\gamma=0\) by (3).
In particular none of the nonconstant affine linear expressions in the
proposed tuple is a slice or an invariant.

The nonlinear relative recovery \(\sigma=tX_1-X_2=u\) remains valid.
It is not an ambient recovery from the proposed tuple alone.

## 4. Exactly where the original-coordinate gate fails

Let \(\Delta\) be the Jacobian determinant of
\((X_1,X_2,X_3,Z)\) with respect to the actual variables \((u,a,y,v)\).
Direct differentiation gives, with \(t=2av-y^2\),
\[
\begin{aligned}
\Delta={}&1+2ay(t^2-y)\\
&+\bigl(2a^2t^2-2a^2y+4at+4yv\bigr)u\\
&+4(av+y^2)u^2+4ayu^3.
\end{aligned}
\tag{7}
\]
In particular there is an explicit singular point on the free open set:
\[
\begin{gathered}
\Delta(u,0,1,0)=1+4u^2,\qquad
p=(u,a,y,v)=(i/2,0,1,0),\\
t(p)=-1,\qquad \Omega(p)=-2,\qquad \Delta(p)=0.
\end{gathered}
\tag{8}
\]
A polynomial coordinate system would have a polynomial inverse, and its
Jacobian determinant would therefore be a nonzero complex constant.
Equation (8) rules this out. It also shows that removing \(V(\Omega)\)
does not repair the proposed coordinate map at every point.

One can verify the missing recovery directly, not only through the
determinant. At p, the nonzero tangent vector
\(k=(1,-i,-1/2,-1+i)\), in the order \((u,a,y,v)\), annihilates
all four differentials \(dX_1,dX_2,dX_3,dZ\), whereas
\(du(k)=1\), \(da(k)=-i\), and \(dt(k)=1\).
Consequently none of u, a, t belongs to
\(\mathbb C[X_1,X_2,X_3,Z]\): a polynomial in the four proposed
functions would have differential annihilating k. In particular the
coefficient t used in (5) cannot silently be recovered from that tuple.

Thus the example does not satisfy the full actual-frame hypotheses:
this tuple does not supply an original coordinate derivation
\(\partial_Z\) fixing the three X_i, and none of its original-coordinate
Jacobian or adjoint identities is being assumed. The actual identity
that the four-coordinate volume is constant fails visibly in (7).

## 5. The remaining bridge and bounded provenance

The result isolates a necessary obligation for a speed-row approach.
The rank-at-least-one theorem, the unit row, the quadratic relative
presentation, the actual coordinate Z, freeness on \(D(\Omega)\), and
even the exact relative inverse and pencil do not by themselves produce
a constant linear speed. Any such inference for the supplied frame must
also use its actual four-coordinate inverse or the volume and original
partial-derivation identities that depend on that inverse.

This does not exclude a nonlinear slice change in the actual frame,
prove that a constant linear slice is necessary for recognition, or
supply a reduction from an arbitrary sliced action. Here A is visibly
polynomial and u is visibly a coordinate. The failure concerns the
proposed shortcut and tuple, not existence of a coordinate slice.

The construction is distinct from the specified-slice
[projected-generator obstruction95](projected-generator-linear-extraction-obstruction-pass95.md):
that note has a genuine original coordinate tuple and obstructs all
constant linear combinations of its projected invariant generators.
Here the obstruction concerns speeds in a proposed three-good,
constant-acceleration tuple, and the failed original-coordinate premise
is identified explicitly. The elementary unit pair underlying (3) also
appears in [the binary control89](binary-normal-unit-control-pass89.md),
but that earlier parameter-only control does not contain this actual
quadratic quotient, cylinder, relative inverse, or Jacobian failure.

All kernel, flatness, fiber, inverse, and derivative claims above have
elementary proofs in the displayed rings. No external classification
theorem, historical novelty claim, action recognition, or frozen-file
edit is added. The separate
[one-method symbolic control](quadratic_global_bridge_checks_pass96.py) verifies the
finite polynomial identities, not the universal coefficient comparison
or an arbitrary-frame theorem.
