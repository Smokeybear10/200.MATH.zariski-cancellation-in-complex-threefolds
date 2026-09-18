# The remaining mixed branch has a proper second-image ideal

The unit second-image case is excluded in the supplied collapsed
mixed quadratic sector. The remaining ideal is a proper closed-point
complete intersection. Purity of a different, degree-four piece
gives sharper coefficient restrictions in that remaining case.
If one specified coefficient has first base order one, an actual
quartic gives a full fourth-degree basis, a full cubic Artin image,
and a strictly bounded two-generator fourth-image ideal.

These results concern the stated local branch. They do not solve
complex-threefold cancellation, justify entry into this quadratic
frame from an arbitrary sliced action, or establish novelty.

## The setting and the obligations that remain separate

The intended working target is A[u] isomorphic to C^[4] implies
A isomorphic to C^[3]. The original email instead has A^1 as its
conclusion for a general r, which is dimensionally incompatible
when r is greater than one. The complex-threefold interpretation
has not been confirmed by the professor.

Within the supplied original quadratic frame, write R for the
regular local invariant surface, m for its maximal ideal, A_R
for the faithfully flat actual domain, and N for its canonical
locally nilpotent derivation. Put F_j=ker N^(j+1) and I_j=N^jF_j.
The modules F_j are free of rank j+1. The branch under study has
whole fiber D[c], with D=C[G]/(G^2(G-1)), and a nonzero speed
normal. Pass107 excludes W2=D, so W2=span(1,G) and W1=C.
Here Wj is the image in the entire nonreduced fiber.

These hypotheses are not free consequences of cancellation.
The [global-entry audit108](global-entry-audit-pass108.md) identifies
the first missing reduction and distinguishes it from the local
branches. A result in this local sector cannot be promoted to
an unrestricted theorem by omitting that entry hypothesis.

## Why the unit case is impossible

The [unit-case proof108](mixed-unit-second-image-exclusion-pass108.md)
starts from I1=(P) and I2=P J2. Suppose J2=R. Freeness of the
image then splits F2 over F1. Since G has nonconstant residue,
it can be used in a basis 1,r,G with

\[
NG=r,\qquad Nr=P,\qquad r^2=2PG-\eta,\qquad
\eta\in R,\qquad \bar r=0.
\]

The monic equation proves an exact embedded algebra
H=R[r,G] with free R-basis G^j,rG^j, for all j>=0.
At every invariant height-one prime the retained exact divisor
model says A_R and H are equal. Any actual element has a unique
finite expansion in this basis over Frac(R). Every coefficient
lies in every height-one localization, hence in the UFD R.
Therefore A_R=H, an equality of entire algebras.

But r is then a free basis element and cannot belong to mH,
whereas its actual whole-fiber residue is zero. This is the
contradiction. It does not rely on normality of the conic,
completion, an unspecified extension principle, the selected
quartic's valuation, or generation by F4. Consequently J2 is
a proper maximal-primary two-generated complete intersection.

## Sharp restrictions in the proper case

Choose F2=R{1,G,H}, with H having zero whole residue, and set
r=aG+bH, J2=(a,b), with coprime a,b in m. The exact conic is

\[
NG=\epsilon br+B_1,\quad NH=-\epsilon ar+B_2,\quad
P=aB_1+bB_2,\quad
Q=\epsilon r^2-2B_2G+2B_1H\in R,
\]

where epsilon is a unit. The full F2 is not pure. Instead,
1,G,G^2 have independent whole residues and span a pure piece
inside F4. Contracting the rearranged conic through that piece
gives the sharper ideal membership

\[
Q,B_2,a^2\in\mathfrak m(B_1)+\mathfrak m(ab)
                         +\mathfrak m^2(b^2).
\]

The [proper-ideal proof108](mixed-proper-second-image-jets-pass108.md)
deduces B1 nonzero, gcd(B1,b)=1, and B1 not in J2^2. The last
fact explains exactly why the two-quartic argument used to
exclude the full-Artin branch cannot be reused here.

If ord(a)<=ord(b), the same identity gives
ord(B1)<=2ord(a)-1. In particular ord(a)=1 makes B1 a smooth
parameter. Writing a=B1 u+bv with u a unit and v in m gives
J2=(B1,b), and the initial form of P is a nonzero scalar
multiple of the square of the initial form of B1.
Writing k=length R/J2, the intersection length of P and B1,
when finite, is at least 3k+2. Divisibility B1|P is not
excluded by that conditional contact bound.

## One actual quartic and a strict fourth-image bound

Assume ord(a)=1. The
[smooth-generator construction108](mixed-smooth-generator-quartic-pass108.md)
changes the basis while preserving G so that B1=a. Then
B2=a beta+b^2 delta and Q=a zeta+b^2 q, with beta,zeta in m
and delta,q in m^2. Flat regular-sequence division proves that

\[
U=(\epsilon H^2-2\delta G-q)/a\in F_4,
\qquad N^4U=6\epsilon^3aP^2.
\]

Existence inside the actual algebra is part of the proof,
not a consequence of verifying the rational expression.
The cancelled conic also gives H in mF4. Since I4=P^2J4
is nonprincipal, a and b^2 in J4 initially give J4=(a,t^n),
with m=(a,t) and 1<=n<=2k.

The [quartic-residue argument108](mixed-smooth-quartic-residue-pass108.md)
sharpens this. The numerator of aU belongs to m^2 A_R;
flatness and the first-order parameter a imply U in mA_R.
Nevertheless U is not in mF4, since its fourth derivative
is a minimal image generator. Consequently

\[
F_4=R\{1,G,G^2,c,U\},\qquad
\mathcal W_4=\mathcal D+\mathbb Cc,\qquad
\mathcal W_3=\mathcal D.
\]

For the last equality, the internal F3 image has dimension
three and does not contain the sole whole-residue kernel
direction U. Its zero reduced slopes remove the c direction.
Lifting G^2 through that image then forces b^2 into mJ4.
Writing L=N^4c/P^2, the exact conclusions are

\[
J_4=(a,L)=(a,t^n),\qquad 1\le n<2k.
\]

Thus k=1 forces J4=m. Conversely, a remaining branch with
dim W3=2 cannot have ord(a)=1. The rank-two cubic branch
must be sought in higher base order. This is a necessary
condition, not an existence or nonexistence theorem there.

## An independent row constraint beyond the smooth case

The [pure quartic row108](mixed-pure-quartic-row-pass108.md)
uses only the independent residues of 1,G,G^2,c to extend
them to an F4 basis. Put d=N^2G, k4=N^4c, and
g0=gcd(6d^2,k4). Then

\[
A_0=6d^2/g_0,\quad B_0=k_4/g_0,\qquad
F_3\cap R\{1,G,G^2,c\}
 =R\{1,G,B_0G^2-A_0c\}.
\]

Zero reduced slopes force A0 into m. If dim W3=2, B0 is
also in m, and the two component translation constants must
agree. The converse is not claimed. These constraints do
not suppose a smooth coefficient and do not assume equal
speeds in the other cases.

The sharper expression k4=P^2L and gcd(P,L)=1 uses the
selected-c boundary valuation at every quadratic constant
divisor. Generic fourth degree alone would not justify it.

## Verification and what the checks do not prove

The [canonical capture108](verification-pass108-working.json)
passes three suites and six methods: two new finite checks
and four retained controls. The new checker covers gcd rows,
mixed-Artin identities, the sharp conic rearrangement, and
general-epsilon divided-quartic derivatives. The retained
controls cover the divisor filtration and actual-division
hypothesis boundaries in explicit examples.

The execution took 1.876345709 seconds, with unittest reporting
1.429 seconds. Input hashes stayed unchanged. The complete
output hash is
`30c95b4e560badd88715a13bc7ac98da57a72212bed22bf7b3ba3608d39d9d15`.
The command is

~~~sh
/opt/anaconda3/bin/python -m unittest -v research.mixed_pure_quartic_checks_pass108 research.quadratic_divisor_filtration_checks_pass107 research.triple_point_quartic_checks_pass51
~~~

These checks do not prove the universal purity, divisibility,
rank or global-entry arguments. Those have written derivations
and separate AI reconstructions, not formal certification or
human expert review. The historical full75 run remains 146
suites and 1047 methods; it was not rerun here. The historical
claim registry remains 544 and is not a count of new108 claims.

The [checkpoint108](checkpoint-pass108-working.json) records
the exact proof versions, verification scope and predecessor
integrity. All 663 predecessor records through107 were rehashed
without a mismatch. README and the ledger remain live.

## Next proof obligations

The smooth-coefficient branch now has the concrete actual
generators G,c,U, with U zero in the whole fiber and a
two-generator image ideal. A next step must use their exact
relations or additional original-frame identities; formal
division by 1+epsilon bG is not available. In the higher-order
branch the sharp ideal and the pure quartic row remain valid,
but the smooth-parameter division and residue-rank proof do not.

Whole-double fibers, zero speed normal, relative cubic frames,
global recognition and the arbitrary-action entry theorem
remain separate open obligations in this investigation.
No public novelty claim, external contact, submission, paid
resource use or new automation has occurred in this pass.

## Sources

The linked proof notes give complete local derivations and
their exact frozen dependencies. The standard source facts
used in the new smooth-parameter step are Stacks Project
[00NQ](https://stacks.math.columbia.edu/tag/00NQ), regular-parameter
quotients, and [00PD](https://stacks.math.columbia.edu/tag/00PD),
one-dimensional regular local rings and DVRs. The purity
input is the separately proved and sourced
[residue-basis lemma107](residue-basis-purity-pass107.md).
These source facts are not claims of novel cancellation results.
