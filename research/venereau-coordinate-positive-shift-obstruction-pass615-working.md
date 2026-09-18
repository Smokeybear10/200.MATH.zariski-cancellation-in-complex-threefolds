# A specified coordinate can exclude every zero-shift completion

Date: 2026-09-17. Private working proof; novelty UNKNOWN.
General complex-threefold cancellation remains UNSOLVED.

## 1. Exact conclusion and its limitation

Work in B=C[x,y,z,u] with the already rectified derivation E=partial_u.
Let

\[
 v=y+x^3\bigl(xz+y(yu+z^2)\bigr)=au+b,
\]
\[
 a=x^3y^2,\qquad b=y+x^4z+x^3yz^2.
\]

Then v is an ACTUAL polynomial coordinate and E^2v=0, but no locally
nilpotent derivation D of B can satisfy both [E,D]=0 and Dv=1.
Consequently EVERY coordinate partial obtained by completing this
specified v has strictly positive E-degree shift. An explicit completion
below has exact shift 10. This is not asserted to be the minimum shift.

The counterstatement concerns preserving this particular coordinate v.
The original E is a translation and has other coordinates, including u,
that give zero shift. This is not a cancellation counterexample, and
does not exclude recognition after changing the chosen coordinate.

The polynomial v is the classical third Vénéreau polynomial. Its
coordinate status is already published, for example in
[Kaliman--Zaidenberg, Corollary1](https://arxiv.org/pdf/math/0308191)
and [Lewis, Section3](https://arxiv.org/html/1007.2230).
The following whole polynomial construction is included to make the
ambient-coordinate premise inspectable without relying on a localized
completion or on an unproved embedding conjecture.

## 2. A whole polynomial completion with its inverse

Set

\[
 p=yu+z^2,\qquad V=xz+yp,\qquad
 W=x^2u-2xzp-yp^2.
\]

Define a polynomial derivation K by

\[
 Kx=0,\quad Ky=x^3V,\quad
 Kz=-x^2Vp-yVW,\quad Ku=2zVW-xVp^2.
\]

Direct polynomial differentiation gives

\[
 Kp=xVW,\qquad KV=KW=0.
\]

It also gives

\[
 K^2y=0,\quad K^2z=-2x^3V^2W,\quad K^3z=0,
\]
\[
 K^2u=-4x^2V^2Wp-2yV^2W^2,\qquad
 K^3u=-6x^3V^3W^2,\qquad K^4u=0.
\]

Thus K is locally nilpotent on the original polynomial ring: it kills
a sufficiently high iterate of each generator. Its finite exponential
F_tau=exp(tau K), for an independent scalar parameter tau, fixes x and
has the following complete polynomial components. Put q=tau VW and

\[
 Y=y+\tau x^3V,\qquad
 Z=z-\tau x^2Vp-Yq,
\]
\[
 U=u+2zq-yq^2-\tau xV(p+xq)^2.
\]

The preceding derivatives give these formulas by the finite exponential
series, coefficient by coefficient. In particular there are no omitted
terms. The exact transformed invariants are

\[
 p(Y,Z,U)=p+xq,\quad V(x,Y,Z,U)=V,\quad W(x,Y,Z,U)=W.
\]

The finite polynomial flow identity proves BOTH whole inverse orders:
F_tau F_(-tau)=F_(-tau) F_tau=id. Explicitly, to recover the old variables
from independent (x,Y,Z,U), form

\[
 p_0=YU+Z^2,\quad V_0=xZ+Yp_0,\quad
 W_0=x^2U-2xZp_0-Yp_0^2,\quad q_0=\tau V_0W_0.
\]

Then the inverse is

\[
 y=Y-\tau x^3V_0,\qquad
 z=Z+\tau x^2V_0p_0+yq_0,
\]
\[
 u=U-2Zq_0-Yq_0^2+\tau xV_0(p_0-xq_0)^2.
\]

All these are polynomials. At tau=1, Y=v, so (x,v,Z,U) is an actual
completion of v. The derivative degrees in the old u are (0,1,4,7)
on these four coordinates.

## 3. No commuting slice derivation for this coordinate

Suppose D were locally nilpotent, [E,D]=0, and Dv=1. Commutation with
E=partial_u forces D to preserve A=kerE=C[x,y,z] and Du=beta in A.
Its restriction N to A is locally nilpotent. Hence

\[
 D=N+\beta\partial_u,\qquad
 1=D(au+b)=N(a)u+a\beta+N(b).
\]

Comparison of the whole u-coefficients gives

\[
 N(a)=0,\qquad N(b)+a\beta=1.
\]

The kernel of a locally nilpotent derivation on a characteristic-zero
domain is factorially closed. This follows, for example, from the
additivity of its nonnegative degree function on nonzero products.
Since a=x^3y^2, the first identity therefore forces Nx=Ny=0. It follows
that

\[
 N(b)=x^3(x+2yz)N(z),\qquad
 N(b)+a\beta\in x^3A.
\]

This contradicts the second identity, since 1 is not in x^3A.
The proof even rules out commuting LNDs with Dv=1 that are not known
to be coordinate partials.

For the all-completion shift conclusion, apply
[614](nonunit-speed-coordinate-induced-action-pass614-working.md).
Every actual coordinate partial for v has nonnegative shift because
a is a nonzero nonunit. Zero shift would imply [E,D]=0, just excluded.
Thus the shift is positive for every completion of this specified v.

## 4. Exact positive shift for the displayed completion

For precision, fix tau=1 in Section2 and keep its complete Y,Z,U.
Set q=VW, P=p+xq and define the following old-coordinate polynomials:

\[
 F=P+YU,\qquad G=-P^2-2VU,\qquad S=FW+VG.
\]

Differentiating the whole inverse at fixed x,Z,U and substituting the
forward map gives its coordinate partial D=partial_Y exactly as

\[
 Dx=0,\qquad Dy=1-x^3F,
\]
\[
 Dz=x^2(Fp+VU)+q+yS,
\]
\[
 Du=-2zS-q^2+x(Fp^2+2VpU).
\]

These equations are polynomial identities, not leading-term definitions.
Direct substitution gives DY=1 and DZ=DU=0.
The exact u-degrees and nonzero leading coefficients are

| Polynomial | u-degree | Leading coefficient |
|---|---:|---|
| Dy | 8 | x^9 y^14 |
| Dz | 10 | x^6 y^18 |
| Du | 10 | -x^6 y^16(x+2yz) |

One can check the degree bound before expanding the entire equations:
deg_u(p,V,W,q,Y,P,U,F,G,S)=(1,1,2,3,1,3,7,8,8,10).
The displayed formulas then bound deg_u(Dy,Dz,Du) by (8,10,10).
Their leading coefficients follow from the same formulas and are
nonzero in C[x,y,z]. Since x,y,z have E-degree zero and u has degree
one, the exact derivation shift is

\[
 \delta(D)=\max\{8,10,10-1\}=10,
 \qquad N=x^6y^{18}\partial_z\quad\text{on }A.
\]

This illustrates the positive-shift branch of614 and its condition
N(a)=0. Dividing this N by its invariant common factor gives partial_z;
no obstruction to a primitive auxiliary slice is claimed here.

## 5. Verification and research consequence

The finite exponential proof supplies the entire automorphism and its
inverse, including x=0. Fresh unsaved algebra separately checked the
original K identities, every finite flow coefficient, both whole inverse
orders, the entire coordinate-partial identities, and the printed degrees.
No saved checker was executed, imported, or compiled.

The consequence is specific: a proof strategy cannot preserve an
arbitrary actual coordinate in ker(E^2) and assume a zero-shift partial
can then be chosen. It must allow changing that coordinate or genuinely
handle the positive-shift case. Existence of an appropriate first
coordinate for an arbitrary cancellation candidate is itself still
unproved. This note establishes neither a terminating coordinate change
nor a general polynomial-kernel theorem.

No new coordinate-status theorem, literature priority, human expert
review, or formal-assistant certification is claimed. Author review and
independent saved-source review are distinct gates.
