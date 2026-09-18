# Two-stage modification: the second-center shear and a polynomial control

Private bounded proof, September 17, 2026. An exact global two-stage
presentation gives an exact polynomial formula for the changed second
center after an invariant local-slice modification. In a separate
invariant-coordinate class, one finite change of the embedded base gives
explicit polynomial coordinates and their entire inverse for arbitrary
modifying polynomial Q.

Rank-at-most-two recognition is already known in the relevant LND
setting. This note supplies an explicit coordinate certificate for the
displayed class, not a new rank-two recognition theorem. It does not
recognize arbitrary rank-three modifications or prove cancellation.
Novelty is not asserted. All rings below are over k=C.

## 1. Exact presentation and the two covering charts

Let A=k[a,b], let f be an irreducible element of A, and suppose

\[
B=A[r,y,z]/(fy-G(r),\ fz-H(r,y))
\tag{1}
\]

is a domain in which the indicated copy of A embeds. Here G belongs
to A[r] and H to A[r,y]. Equation (1) means the entire quotient,
without an additional saturation. Let Q belong to A and put

\[
V=1+fQ,\qquad M=B[r/V]\subset\operatorname{Frac}B.
\tag{2}
\]

The element V is nonzero and (f,V)=A. Define the raw substituted ring

\[
S=A[w,y,z]/(fy-G(Vw),\ fz-H(Vw,y)).
\tag{3}
\]

There is a surjection S to M, taking w to r/V and fixing A,y,z.
The whole equations give

\[
S_V\cong B_V,\qquad S_f\cong A_f[w].
\tag{4}
\]

The first isomorphism uses r=Vw, and the second eliminates y,z.
These principal opens cover Spec S. To see directly that S injects
into S_f, suppose f^n h=0 in S. In the domain S_V=B_V, the image of
f is nonzero, so h vanishes there and V^m h=0 for some m. The ideals
(f^n,V^m) generate S, hence h=0. Thus S is a domain. Since the map
S to M becomes injective after inverting V, it is already injective.
Consequently (3) is an exact presentation of M, not merely one of a
larger unsaturated algebra.

If B is smooth, then M is smooth: both charts in (4) are smooth,
the second because A is a polynomial ring. Moreover

\[
M/fM\cong
(A/fA)[w,y,z]/(\overline G(w),\overline H(w,y))
\cong B/fB.
\tag{5}
\]

This is an equality of entire quotient presentations, with r renamed
w. It does not assert that the fiber is reduced or that its geometry
recognizes the whole ring. None of these arguments promotes a merely
localized two-stage description to (1).

## 2. The exact second-center shear

All the following quotients first denote polynomial divided differences:

\[
C(w)=\frac{G(Vw)-G(w)}f,\qquad
C_0(w)=QwG_r(w),\qquad \eta=y-C(w).
\tag{6}
\]

Taylor expansion in the independent polynomial variable w gives
C-C_0 in fA[w], including when G or Q is constant or zero. Define

\[
J(w,\eta)=
\frac{H(Vw,\eta+C(w))-H(w,\eta+C_0(w))}{f},
\qquad \zeta=z-J(w,\eta).
\tag{7}
\]

The numerator in (7) is divisible by f in A[w,eta]: its two arguments
are congruent modulo f. Thus (6)-(7) are triangular polynomial changes
of the three presentation variables, with entire inverse

\[
y=\eta+C(w),\qquad z=\zeta+J(w,\eta).
\tag{8}
\]

They identify the defining ideals, giving

\[
\boxed{
M\cong_A
\frac{A[w,\eta,\zeta]}
 {(f\eta-G(w),\ f\zeta-H(w,\eta+C_0(w)))}.}
\tag{9}
\]

In particular, normalizing the first center need not normalize the
second one. The factor 1/f in (6) leaves the generally nonzero residue
QwG_r(w), which must not be discarded.

For completeness, the compatible derivation on (1) is

\[
D|_A=0,\quad Dr=f^2,\quad Dy=fG_r,\quad
Dz=fH_r+H_yG_r.
\tag{10}
\]

It is locally nilpotent: after inverting f the ring is A_f[r] and
D=f^2 partial_r, and (10) preserves the entire original ring. On M,
Delta=VD satisfies Delta(w)=f^2. With
H_Q(w,eta)=H(w,eta+C_0(w)), its transported formulas are

\[
\Delta\eta=fG_r(w),\qquad
\Delta\zeta=f(H_Q)_w+(H_Q)_\eta G_r(w).
\tag{11}
\]

These follow either by differentiating (6)-(7), or by differentiating
both relations in (9) and cancelling nonzero f in the domain. No
primitivity, full-kernel equality, or exact plinth assertion follows
from the presentation alone. Those are separate hypotheses when this
calculation is applied to a primitive local-slice problem.

## 3. What a further last-variable translation can remove

Put T=A[w,eta]/(f eta-G(w)). The following is an exact criterion for
making the second displayed equation in (9) equal to
f zeta-H(w,eta), over T, by a translation of zeta by a polynomial in
w,eta:

\[
\boxed{
H(w,\eta+C_0)-H(w,\eta)\in(f,G(w))\subset A[w,\eta].}
\tag{12}
\]

Indeed such a translation exists exactly when the difference is in
fT. Its preimage in A[w,eta] is
(f,f eta-G(w))=(f,G(w)). If the difference equals fL in T, set the
new last variable equal to zeta-L. This also proves sufficiency as
an isomorphism of the whole two-equation presentations. Equivalently,
the difference must vanish in
((A/fA)[w]/(Gbar(w)))[eta]. In particular Q in fA is sufficient.

The criterion concerns this specified translation, fixing A,w,eta.
It does not classify arbitrary relative isomorphisms, which might
change the other variables. The stronger local-slice relative
isomorphism theorem is already proved in
[pass19](relative-modification-classification-pass19.md), including
the common-residue case V=1+rad(p)Q. No new version of that theorem
is claimed here.

For a concrete failed translation, use the published control recorded
in [pass622, Section 4](global-triangular-presentation-cylinder-obstruction-pass622-working.md):

\[
A=k[x,s],\quad f=x,\quad G(w)=w^2-s,\quad
H(w,\eta)=w+\eta^2,\quad Q=1.
\tag{13}
\]

Then C_0=2w^2 and the residue difference in (12) is

\[
4w^2\eta+4w^4\ne0
\quad\text{in }k[s,w,\eta]/(w^2-s).
\tag{14}
\]

Thus the last-variable translation does not undo the center shear.
The next section nevertheless gives abstract polynomial coordinates,
including this example and every Q(x,s).

## 4. A polynomial class with an explicit change of embedded base

Now f,s are independent polynomial variables. Choose arbitrary

\[
g\in k[f,R],\qquad F\in k[f,Y],\qquad Q\in k[f,s],
\tag{15}
\]

and take G(r)=g(f,r)-s and H(r,y)=r+F(f,y). The exact presentation
eliminates r and s with coefficient one:

\[
B=k[f,y,z],\qquad r=fz-F(f,y),\qquad
s=g(f,r)-fy.
\tag{16}
\]

The indicated A=k[f,s] really embeds. If g has positive R-degree,
then s has positive z-degree over k(f,y), and so is transcendental
over k(f). If g has R-degree zero, then s=g(f)-fy is nonconstant
linear in y over k(f), with the same conclusion. This includes g=0.
Thus no lower-degree boundary silently invalidates the base embedding.

These data lie in the invariant-coordinate, rank-at-most-two setting
for the compatible LND (10), since f is an ambient coordinate.
The following coordinate construction is valid without assuming that
(10) is primitive, has kernel A, or has plinth f^2 A. For example,
if g is independent of R, then D=f partial_z and its kernel is
k[f,y], not the indicated A. Such a boundary is not a primitive
prime-square-plinth example.

Set q=Q(f,s), V=1+fq, and work in M with w=r/V. Define

\[
g_0=g(f,w),\quad g_1=g_R(f,w),\quad
q_*=Q(f,g_0),\quad S=s-fq_*wg_1,
\tag{17}
\]

\[
Y=\frac{g_0-S}{f},\qquad
Z=\frac{w+F(f,Y)}f.
\tag{18}
\]

The symbol S is a changed base element, not an assertion that the
old subring k[f,s] is preserved. On the polynomial plane with
coordinates s,w over k[f], the map (s,w) to (S,w) in (17) is an
entire triangular automorphism: q_* and g_1 depend only on f,w.

## 5. Clearing both forward denominators uniformly

The polynomial divided difference and Taylor remainder

\[
L=\frac{Q(f,s)-Q(f,g_0)}{s-g_0},\qquad
C=\frac{g(f,Vw)-g_0}{f},\qquad
R_2=\frac{C-qwg_1}{f}
\tag{19}
\]

belong to k[f,s,w]. They are interpreted polynomially at equal
arguments, so no nonzero value of s-g_0 is assumed. In particular,

\[
C=qwg_1+fR_2,\qquad
s-g_0=f(C-y),\qquad q-q_*=L(s-g_0).
\tag{20}
\]

The middle equality is precisely the first relation of M. Put

\[
T=L(C-y)wg_1+R_2.
\tag{21}
\]

Then (18) has the denominator-free form

\[
Y=y-fT,\qquad
Z=z-qw-T\,F^{[1]}(f;Y,y),
\tag{22}
\]

where F^{[1]}(f;U,W)=(F(f,U)-F(f,W))/(U-W) is a polynomial.
Indeed (20) gives C-q_*wg_1=fT, proving the first formula. The
second follows from fz=Vw+F(f,y). In particular Y=y modulo fM.
This proves polynomiality of both coordinates for every finite
degree of g,F,Q, not from bounded symbolic examples.

## 6. The entire polynomial inverse and both compositions

Start with independent polynomial variables f,Y,Z. Recover, in order,

\[
w=fZ-F(f,Y),\quad g_0=g(f,w),\quad g_1=g_R(f,w),\quad
q_*=Q(f,g_0),
\tag{23}
\]

\[
K_1=q_*wg_1-Y,\qquad s=g_0+fK_1,\qquad q=Q(f,s),
\qquad V=1+fq.
\tag{24}
\]

Evaluate the same polynomial L,R_2 from (19) at these recovered
arguments and define

\[
T_b=LK_1wg_1+R_2,\qquad
y=Y+fT_b,\qquad
z=Z+qw+T_b F^{[1]}(f;y,Y).
\tag{25}
\]

Every expression is polynomial in the independent f,Y,Z. The
identities s-g_0=fK_1 and q-q_*=fLK_1 give
C-q_*wg_1=fT_b. Therefore the inverse satisfies the entire equations

\[
fy=g(f,Vw)-s,\qquad fz=Vw+F(f,y).
\tag{26}
\]

It defines a homomorphism from M to k[f,Y,Z]. No implicit equation
for s or q is being solved: s is recovered explicitly before q.

For the forward-then-inverse composition inside M, equations (18)
recover w from fZ-F(f,Y), then S from g_0-fY, and then the original
s from S+fq_*wg_1. Thus q and V are recovered. Equation (26),
compared with the original defining equations, recovers y and z
after cancelling nonzero f in the domain M.

Conversely, begin with the independent variables in (23). Equations
(24)-(26) give C-y=K_1, so the forward T in (21) equals T_b.
The first formula in (22) recovers Y. The second recovers Z because
the polynomial divided difference is symmetric in its last two
arguments. This proves the other entire composition and yields

\[
\boxed{M=k[f,Y,Z].}
\tag{27}
\]

When Q=0, the formulas reduce to w=r,Y=y,Z=z. Constant or zero
g and F are retained by the same polynomial divided differences.
Primitivity and a minimal local slice have not been inferred in
these boundary cases.

## 7. Provenance, deduplication, and limits

The general two-chart presentation and the second-center shear were
derived independently by the main agent and the author of this note.
The author found the arbitrary-Q coordinate certificate for (13);
the main agent and author independently extended it to (15)-(16).
The published origin of (13) is Dasgupta--Gaifullin Example 4.15,
as directly recorded and checked in pass622. That base example is
not new.

The full relative theorem and its finite-iterate proof in pass19
already rule out many isomorphisms fixing the old invariant plane.
The full [iterated-local-slice proof](iterated-local-slice-bridge-pass19.md)
handles a different controlled rank-three, two-prime surface-mutation
class. A bounded archive search found no identical formula (17)-(25).
This is an archive-deduplication observation, not a priority claim.

Fresh unsaved checks e7357e through d551ce verified whole forward and
inverse certificates with generic quadratic Q in the example (13).
Fresh d85cde verified the universal Taylor first-relation certificate
and inverse identities, together with the whole second-relation
identity for a cubic F. Fresh 2f4bee checked the printed center shear
and entire derivation transport with cubic G,H, and reconstructed the
printed universal forward and inverse Taylor identities. The
all-polynomial proofs above, rather than these finite tests, establish
the stated arbitrary-degree claims.
No saved checker was executed, imported, compiled, or changed.

Equation (9) is a changed-family normal form for a general exact
two-stage presentation. Equation (27) is recognition only for the
explicit invariant-coordinate class (15)-(16). No theorem putting
an arbitrary rank-three input into that class is supplied. General
modification recognition, cancellation, and mathematical novelty
remain unresolved by this note. Independent saved-source review is
required before acceptance.
