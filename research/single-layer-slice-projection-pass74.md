# A single homogeneous projection layer gives an actual coordinate certificate

A slice projection with just one nonlinear homogeneous layer has a
polynomial graph as its image. For an actual sliced action on complex
four-space, this makes the supplied slice a coordinate and produces
three explicit invariant coordinates with a bounded polynomial inverse.
The nonlinear layer can have arbitrary degree.
The same homogeneous support restriction also forces a sharp dichotomy:
either the supplied slice is linear in this affine frame, or the action
is a constant translation. Thus this is a quantitative coordinate
certificate, not a new recognition family.

The missing universal statement is not removed: an arbitrary slice
projection can have many homogeneous layers, and no change of slice or
frame eliminating them is constructed here. This is an exact sufficient
certificate with a self-contained proof, not a novelty or unrestricted
cancellation claim.

## 1. Actual input and the additional projection hypothesis

Let
\[
B=\mathbb C[x_1,x_2,x_3,x_4],\qquad
E\in\operatorname{LND}(B),\qquad Es=1,
\qquad E^Nx=0,\qquad \deg(Ex_i)\le e,
\quad e\ge1.
\tag{1}
\]
Let \(\Phi_t\) be the actual polynomial flow and let
\[
\pi(x)=\Phi_{-s(x)}(x).
\tag{2}
\]
The independent time is substituted only after forming the finite
flow. As recalled in the [quadratic-projection note](quadratic-slice-projection-pass74.md),
\(\pi\) is an idempotent algebra retraction onto \(A=\ker E\),
with \(\ker\pi=sB\) and rank-three derivative at every point.
Those general retraction and tangent properties were already retained
in [pass22](nonlinear-frame-pass22.md), Section 1.

Assume that after an actual affine coordinate change centered at a
fixed point of \(\pi\), the complete projection has the form
\[
\pi(x)=Lx+H_m(x),\qquad m\ge2,
\tag{3}
\]
where \(H_m\) is homogeneous of degree \(m\).
There are no other nonlinear homogeneous pieces. The zero case
\(H_m=0\) is permitted, although a nonzero layer is the intended
application. This is a condition on the actual four coordinate
images of \(\pi\), not on a Jacobian rank or the abstract algebra
\(A\). Affine changes preserve the coefficient degree bound \(e\)
and the coordinate iterate bound \(N\).

**Proposition.** Under (1)--(3), there is an adapted polynomial
inverse pair \(F,G\) with
\[
F_4=s,\qquad E(F_1)=E(F_2)=E(F_3)=0,
\qquad G\circ F=\operatorname{id},\quad F\circ G=\operatorname{id},
\]
\[
\deg F\le m,\qquad
\deg G\le m+(N-1)\bigl(m(e-1)+1\bigr).
\tag{4}
\]
In particular \(A=\mathbb C[F_1,F_2,F_3]\). The stronger
degree-two/inverse-degree-four bound for \(m=2\) remains the
separate quantitative result in the linked quadratic note.

## 2. The full idempotence identity forces a graph

The derivative \(L\) at the fixed origin satisfies \(L^2=L\)
and has rank three. A constant invertible linear change therefore
puts \(L=\operatorname{diag}(I_3,0)\). This preserves homogeneity
of \(H_m\). Write the new coordinates as \((u,t)\), with three
entries in \(u\).

In the identity \(\pi(\pi(x))=\pi(x)\), its degree-\(m\)
part is exactly
\[
LH_m(x)+H_m(Lx)=H_m(x).
\tag{5}
\]
Indeed, in expanding \(H_m(Lx+H_m(x))\), every term containing
at least one occurrence of \(H_m(x)\) has degree at least
\(2m-1>m\). This is where the absence of other nonlinear
homogeneous layers is used.

The upper entries of (5) say that the upper part \(P(u,t)\)
of \(H_m\) vanishes when \(t=0\). Its lower entry says that
the lower part depends only on \(u\). Thus
\[
\pi(u,t)=(U(u,t),Q(u)),\qquad
U=u+P(u,t),\qquad P(u,0)=0,
\tag{6}
\]
where \(P\) and \(Q\) are homogeneous of degree \(m\),
possibly zero.

We now use full idempotence, not only its leading or tangent part.
Its lower entry gives
\[
Q(U(u,t))=Q(u).
\tag{7}
\]
Every value of \(\pi\) is consequently of the form
\((U,Q(U))\), and every point \((u,Q(u))\) occurs as
\(\pi(u,0)\). This proves the exact graph description.

It also proves the corresponding algebraic statements without
assuming any geometric image theorem:
\[
\operatorname{im}\pi=\mathbb C[U_1,U_2,U_3],\qquad
\ker\pi=(t-Q(u)).
\tag{8}
\]
For the image, use (7). The \(U_i\) are algebraically independent,
because restriction to \(t=0\) sends them to the independent
variables \(u_i\).
For the kernel, \(t-Q(u)\) is killed by (6)--(7). If
\(f\circ\pi=0\), restriction to \(t=0\) gives
\(f(u,Q(u))=0\), so division by the monic polynomial
\(t-Q(u)\) shows that it divides \(f\).

Comparison with the actual slice ideal \(\ker\pi=sB\) yields
\[
s=c(t-Q(u)),\qquad c\in\mathbb C^*.
\tag{9}
\]
Thus \(s\) is an actual triangular polynomial coordinate, of
degree at most \(m\). No conclusion has been inferred from a
unimodular row, a projective-module splitting, or a localized ring.

There is a further restriction on this particular certificate. Every
graph point is fixed by the idempotent map, so its upper coordinates give
\[
P(u,Q(u))=0.
\]
Replace \(u\) by \(\lambda u\), where \(\lambda\) is an
independent scalar variable. Homogeneity of both \(P\) and \(Q\)
then gives
\[
P(u,\lambda^{m-1}Q(u))=0.
\]
For complete coefficient justification, write
\(P(u,t)=\sum_{j=1}^{m}P_j(u)t^j\). The distinct powers
\(\lambda^{(m-1)j}\) imply
\(P_j(u)Q(u)^j=0\) for every \(j\). If \(Q\ne0\),
the polynomial ring is a domain, so \(P=0\). In this branch
\(\pi=(u,Q(u))\), hence \(Eu=0\); equation (9) and
\(Es=1\) yield \(Et=1/c\). The actual action is therefore
a constant translation in this affine frame. If \(Q=0\),
equation (9) instead says that the supplied slice \(s=ct\)
is linear. Both branches are already recognized elementary cases.
The content retained below is the explicit adapted inverse and its
uniform degree estimate under the stated projection certificate.

## 3. The explicit adapted inverse and its degree

The graph in (8) has the polynomial parametrization
\(\iota(V)=(V,Q(V))\), of degree at most \(m\).
Here \(V=(V_1,V_2,V_3)\) consists of independent target variables.
Returning to the original input frame, if needed, only composes
\(\iota\) with the inverse of an affine map and keeps that bound.
The parametrization lies in \(s=0\), and
\[
\pi(x)=\iota(U(x)).
\]
Set
\[
F(x)=(U(x),s(x)),\qquad
G(V,S)=\Phi_S(\iota(V)).
\tag{10}
\]
Every \(U_i\) lies in \(\ker E\) by (8), and \(Es=1\).
The flow identities give both inverse orders explicitly:
\[
G(F(x))=\Phi_{s(x)}\bigl(\Phi_{-s(x)}x\bigr)=x,
\]
\[
\pi(G(V,S))=\iota(V),\qquad s(G(V,S))=S,
\qquad F(G(V,S))=(V,S).
\tag{11}
\]
For the second line, the slice increases by its flow time and
\(\pi\) is invariant under that flow. The first three graph
coordinates recover \(V\). These identities prove actual global
coordinates adapted to the original supplied slice.

The forward bound in (4) follows from (6) and (9).
For the inverse, the \(i\)-th flow component is
\[
G_i(V,S)=\sum_{j=0}^{N-1}
 \frac{S^j}{j!}(E^jx_i)(\iota(V)).
\tag{12}
\]
For a nonzero summand, \(\deg E^jx_i\le1+j(e-1)\).
After substitution its total degree is at most
\[
j+m\bigl(1+j(e-1)\bigr)
=m+j\bigl(m(e-1)+1\bigr).
\]
The maximum is attained at the last permitted index in this safe
bound. This proves (4). No assertion of sharpness is needed.

## 4. What the certificate does and does not add

The criterion is not a bound on the degree of an arbitrary slice
projection. It instead tests a precise gap in its homogeneous support
after a specified actual affine change. The dichotomy proved after
(9) shows explicitly that it adds no new recognition family beyond
linear supplied slices and constant translations. A slice may have arbitrarily
large degree and still meet it: for \(E=\partial_t\) and
\(s=t-Q(u)\), with \(Q\) homogeneous of any degree \(m\),
one has \(\pi=(u,Q(u))\). These are standard translation
examples, not examples of an unknown kernel.

The graph-image step alone is not an ambient-coordinate conclusion
for an arbitrary retract. The quadratic control
\(\rho(u,v,w,t)=(u(1+t),v,w,0)\) already has a polynomial graph
as geometric image, but its embedded image generators together with
\(t\) are not coordinates. It cannot be the projection of an
actual sliced LND with that kernel ideal. Here (9) and the actual
flow supply the missing inverse step. The full control and its
factorial-closure obstruction are in the separate quadratic note.

The old sparse-retraction criteria in
[the pass38 source audit](literature-scope-pass38.md), Section 3,
concern numbers of monomials in coordinate images. They do not
automatically put an arbitrary projection into (3). The present
certificate uses a different explicit condition, one homogeneous
nonlinear degree, and proves every needed identity directly.
The related Liu--Sun paper on sparse homogeneous retracts was located
at its [publisher page](https://doi.org/10.1016/j.jpaa.2017.04.009),
but its complete statements and proofs were not retrieved in this
pass. No exact subsumption, novelty, or theorem application is inferred
from the available abstract.

This proof introduces no source-dependent classification, numerical
method, full regression, human expert review, or proof-assistant
certificate. No universal existence of (3), automatic nonlinear
coordinate repair, unrestricted cancellation, or global regular choice
over a parameter scheme follows. Frozen passes through73 and shared
metadata are unchanged.
