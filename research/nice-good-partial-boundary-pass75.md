# A good partial need not produce a nice symmetry or preserve the supplied slice

In a nice sliced four-variable action with exactly one constant good
direction, differentiating the velocity in that direction can give
an actual commuting LND that is not nice in the displayed frame.
It can also move the supplied slice. Both failures occur in the
same already retained, completely recognized action.

This is a countercontrol to two proposed next steps, not a new
action or a counterexample to cancellation. It belongs to the
separate pass75 draft and is not part of the pass74 capture.

## 1. The reused actual action and its sole good direction

In the actual polynomial coordinates \((x,y,z,w)\), set
\[
a=xz-y^2+w,\qquad
P=(1,a,a^2,-a^2x+2ay-z)^t,\qquad E=P\cdot\partial.
\tag{1}
\]
This is the de Bondt example already recorded in
[pass39](literature-scope-pass39.md), Section2, and used in
[the pass74 rank-control proof](nice-slice-adjoint-rank-pass74.md).
In particular, no new historical provenance is claimed.
The identities \(EP=0\) and \(Ex=1\) give a nice sliced
action. Its actual polynomial inverse coordinates are
\[
(x,a,Y,Z)=(x,a,y-xa,z-xa^2),
\]
\[
y=Y+xa,\qquad z=Z+xa^2,
\qquad w=a-xZ+Y^2+2xaY.
\tag{2}
\]
Both compositions are the identity, and \(E=\partial_x\)
in (2). Thus the action and its kernel are already recognized.

Let \(J=\operatorname{Jac}P\). The retained exact calculation
gives \(J^3=0\), \(\operatorname{rank}J=2\), and
\[
(J^2)_{2,*}=(-a^2,2a,-1,0),\qquad J^2e_w=0,
\qquad Je_w\ne0.
\tag{3}
\]
Since \(a\) is transcendental over \(\mathbb C\), the
second row forces any constant vector in \(\ker J^2\)
to be a multiple of \(e_w\). The nonzero last column of
\(J\) then gives
\(G_2=\mathbb Ce_w\) and \(G_1=0\), in the notation
of the [frontier summary](nonlinear-frontier-pass74.md).
Consequently \(T=\partial_w\) is the unique constant good
line: \(\operatorname{ad}_E^2T=0\), but \([E,T]\ne0\).
This is an original coordinate partial, not a rationally
rescaled field or an arbitrary selected centralizer.

## 2. The derived field is a commuting LND but not nice

Differentiating the actual velocity gives
\[
Q=(\partial_wP)\cdot\partial
=\partial_y+2a\partial_z+(-2ax+2y)\partial_w.
\tag{4}
\]
Thus \([E,T]=-Q\). Direct calculation, or the actual
coordinates (2), gives
\[
Qx=Qa=0,\qquad QY=1,\qquad QZ=2a.
\tag{5}
\]
In (2), therefore, \(Q=\partial_Y+2a\partial_Z\) is an
actual polynomial LND. It commutes with \(E=\partial_x\),
and the pair is independent over the original fraction field.
These facts do not require a slice to descend to an auxiliary
kernel. They are supplied by the actual inverse pair.

Nevertheless, in the original displayed coordinates,
\[
Q(P)=0,
\qquad Q^2(x,y,z,w)=(0,0,0,2),
\qquad Q^3(x,y,z,w)=0.
\tag{6}
\]
For example, \(Q(-2ax+2y)=2\). Thus \(Q\) is not nice
in that original frame, even though it kills all four coefficients
of \(E\). Commutation, \(Q(P)=0\), and the fact that \(Q\)
comes from a good coordinate partial do not establish \(Q^2x_i=0\).
Niceness is coordinate-dependent; (5) does make \(Q\) nice
in the different actual frame (2). That does not justify inserting
niceness into an argument about the original partials.

## 3. The supplied slice need not be fixed

Keep the same actual action and good partial, but supply the
polynomial slice
\[
s=x+Y=x+y-xa.
\tag{7}
\]
The invariant \(Y\) satisfies \(EY=0\), while (5) gives
\(QY=1\). Therefore
\[
Es=1,\qquad Qs=1.
\tag{8}
\]
The originally supplied slice is not automatically killed by
the derived commuting LND. Of course this particular action also
has the different slice \(x\), which \(Q\) does kill.
The control disproves the assertion about an arbitrary supplied
slice, not existence of a suitable replacement in all instances.
It does not show that a common invariant slice selection theorem
is impossible or prove such a theorem.

## 4. Deduplication and bounded verification

The [old nice-centralizer analysis](nice-centralizer-bridge-pass40.md)
already distinguishes auxiliary-kernel recognition from the original
kernel, and disproves automatic slice transfer or preservation of
one chosen invariant plane. Its complete saved proof was reread
before this calculation. The present control checks a narrower
new proposed inference: the auxiliary field is exactly the
derivative of a nice velocity along its sole constant good
direction, and still has the failures (6) and (8).

The [standalone checker](nice_good_partial_checks_pass75.py) has
one method and imports only `unittest` and SymPy. It computes
\(Q\) from \(P\), verifies actual partial/adjoint identities,
\(Q(P)=E(Q)=0\), independence, both orders of (2), the
transported actions, and (6)--(8). It also verifies both inverse
orders and the differential equations for the actual polynomial
flows of \(E\) and \(Q\). No generic centralizer classification
or solver is imported.

The first standalone run passed **one method in 0.436 seconds**,
exit zero. An earlier exploratory inline check initially compared
algebraically equal expressions by structural equality. Expanded
differences fixed that harness issue; no mathematical formula was
changed. Its corrected identities passed before the standalone
method was written. These are not additional reusable methods.

The finite checks support exact identities for this known action,
not a universal recognition result, historical novelty claim,
proof-assistant certificate, or human expert audit. The note and
checker are new pass75 artifacts only. No pass74-or-earlier file,
shared metadata, full regression, or frozen checkpoint was changed.
