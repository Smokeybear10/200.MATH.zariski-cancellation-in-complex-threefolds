# Recovering weighted Euler shifts by exact commutators

Working bounded result: for a sliced locally nilpotent derivation E,
the exact E-degree shift of ANY nonzero polynomial derivation D is
determined by its last nonzero iterated commutator with E, together
with a polynomial collinearity test. No generators of ker(E) are
needed for that test. In the all-positive weighted Euler case,
zero shift is equivalent to the exact identity [E,D]=E. At positive
shift, the final commutator recovers the leading locally nilpotent
derivation on ker(E), with an explicit vertical correction.

The companion
[576](weighted-euler-positive-shift-and-homogeneous-initial-rank-pass576-working.md)
is pending independent complete saved-source review at this note's
authoring. Its positive-shift input is proved directly below to make
the present argument self-contained. No zero-shift recognition
conclusion from576 is used or certified here.

These are computable identities and structural restrictions, not
a new coordinate-descent theorem or an entry theorem for arbitrary
cancellation data. The actual controls below are not globally
degree-minimizing frames and are not counterexamples to a theorem
about such frames. No novelty is claimed.

## 1. Actual ring, slice and exact derivation shift

Let
\[
B=\mathbb C[X_1,\ldots,X_n]=A[u],\qquad
0\ne E\in\operatorname{LND}(B),\qquad Eu=1,
\qquad A=\ker_B E.
\tag{1}
\]
Thus E=partial_u in this presentation. The Xi are actual polynomial
coordinates; no coefficient-field generators are promoted to such
coordinates. The slice u is an actual polynomial but need not be
one of the displayed Xi. The arguments work for n at least one;
the positive-shift alternative is empty if A=C.

For nonzero f in B put deg_E f=deg_u f, and give zero degree minus
infinity. For a nonzero C-derivation D of B define its exact shift
\[
\delta(D)=\sup_{Df\ne0}\{\deg_E(Df)-\deg_E f\}.
\tag{2}
\]
This integer can be negative for a general D. In particular a
nonzero A-multiple of E has shift -1. We do not initially assume
that D is locally nilpotent, homogeneous, or an Euler derivation.

For the proof only, restrict D to A and take its u coefficients:
\[
D=\sum_{j\ge0}u^jN_j+b(u)E,\qquad
N_j\in\operatorname{Der}_{\mathbb C}(A),\quad N_j(u)=0,
\qquad b(u)=D(u)\in A[u].
\tag{3}
\]
The sum is finite. Indeed A is finitely generated, since evaluation
at u=0 identifies A with B/(u); taking a finite generating set of A
bounds all the coefficient degrees in its D images. The Leibniz
rule shows that each coefficient map Nj is a derivation of A.
This argument does not presume that such generators are known
to perform the computation below.

Let nu be the largest j with Nj nonzero, or minus infinity if all
vanish, and let beta=deg_u b, also allowing minus infinity. Then
\[
\boxed{\delta(D)=\max\{\nu,\beta-1\}.}
\tag{4}
\]
The upper bound follows by applying (3) to every polynomial
sum of a_k u to the k. The horizontal bound nu is attained on an
element of A on which Nnu is nonzero. The vertical bound beta-1
is attained on u. Thus this is an exact all-ring shift, not only
a bound checked on the displayed Xi.

## 2. A finite calculation in the original actual coordinates

Use the commutator convention [E,D]=E composed with D minus
D composed with E, and set
\[
C_0=D,\qquad C_j=(\operatorname{ad}_E)^jD,
\qquad r=\max\{j:C_j\ne0\}.
\tag{5}
\]
This maximum exists without a known presentation of A. Introduce
an independent parameter z fixed by all derivations. The map
exp(zE) is a polynomial automorphism of B[z], with inverse
exp(-zE), because E is locally nilpotent. For each of the finitely
many actual Xi, the expression
\[
\exp(zE)\,D\,\exp(-zE)(X_i)
\tag{6}
\]
is a polynomial in z: first expand exp(-zE)(Xi), apply D to its
finitely many coefficients, and apply exp(zE) to those finitely
many resulting polynomials. Its Taylor coefficients are
Cj(Xi)/j!. The degrees in z for the finite coordinate set therefore
bound j uniformly. Vanishing on all Xi is vanishing as a derivation,
so Cj=0 for all sufficiently large j.

Since E kills the coefficients in (3), the commutators simply
differentiate its u-polynomial coefficients. Hence
\[
r=\max\{\nu,\beta\},\qquad
C_r=r!\{N_r+b_rE\},\quad b_r=[u^r]b,
\qquad [E,C_r]=0.
\tag{7}
\]
Missing coefficients are interpreted as zero. In particular the
following formula determines the exact shift from actual
polynomial derivations alone:
\[
\boxed{
\delta(D)=
\begin{cases}
r,& C_r\wedge E\ne0,\\
r-1,& C_r\wedge E=0.
\end{cases}}
\tag{8}
\]
The wedge is zero precisely when every polynomial minor
\[
C_r(X_i)E(X_j)-C_r(X_j)E(X_i)
\tag{9}
\]
vanishes. This test needs no kernel generators and no coordinate
presentation of A. If the wedge is zero, C_r is a rational multiple
of E; applying it to the actual slice shows that the multiplier is
C_r(u), a polynomial. Commutation with E then places it in A.
Equivalently N_r=0. In that case beta=r and nu is at most r-1,
so (4) gives r-1. If the wedge is nonzero, N_r is nonzero and
(4) gives r. This proves both directions of (8).

The endpoints are part of the statement. If r=0 and the wedge
is nonzero, the shift is zero. If r=0 and the wedge is zero,
D is a nonzero A-multiple of E and its shift is -1. Thus simply
identifying the final nonzero commutator order with the shift
would already be false for general derivations. The zero derivation
is excluded from (2),(5), rather than assigned a fictitious r.

## 3. Positive weighted Euler shift and its recovered LND

Now impose the actual all-positive hypotheses
\[
d_i=\deg_E X_i>0,\qquad
D=\sum_{i=1}^n d_iX_i\partial_{X_i}.
\tag{10}
\]
This D defines the connected positive source grading with weights
di. Every source-weight component is finite dimensional and D acts
on it by its weight. In particular D is locally finite. Since
D(Xi)=di Xi, equation (2) gives delta at least zero.

Suppose delta is positive. The leading derivation gr_E(D) is
a nonzero homogeneous derivation of degree delta on
gr_E(B)=A[eta]. It is locally nilpotent. Indeed the D iterates of
each f belong to a finite-dimensional source-weight space, so
their E degrees are bounded. A nonzero k-th iterate of gr_E(D)
on the initial form of f would imply degree
deg_E f+k delta for D to the k of f. This cannot continue
indefinitely. The conclusion extends from homogeneous initials
to finite sums of them.

The possible value of gr_E(D)(eta) is a coefficient of A times
eta to the delta+1, hence is divisible by eta. A locally nilpotent
derivation on a characteristic-zero domain cannot take a nonzero
element to a nonzero multiple of itself: its own degree function
would give deg(derivative f)=deg(f)-1, while the nonzero product
f times g has degree deg(f)+deg(g). Consequently
\[
\operatorname{gr}_E(D)(\eta)=0,\qquad
\operatorname{gr}_E(D)=\eta^\delta N,
\qquad 0\ne N\in\operatorname{LND}(A),
\qquad \deg_E D(u)\le\delta.
\tag{11}
\]
The nonzero horizontal coefficient N is necessary because the
whole leading derivation is nonzero. Its local nilpotence follows
also from (eta to the delta*N) to the k of a being
eta to the k delta times N to the k of a, for a in A.

It follows from (7),(8) that r=delta, the terminal wedge is nonzero,
and the precise recovery formula is
\[
\boxed{\begin{aligned}
C_\delta&=\delta!\{N+\beta_\delta E\},
&\beta_\delta&=[u^\delta]D(u)\in A,\\
N&=\frac1{\delta!}C_\delta\big|_A,
&\widetilde N&=\frac{C_\delta-C_\delta(u)E}{\delta!}
\quad\text{on }B.
\end{aligned}}
\tag{12}
\]
Here the occurrence of N in the first line means its extension
killing the supplied slice u. The corrected derivation N-tilde is
an actual polynomial LND, kills u, restricts to N on A, and
commutes with E. The terminal commutator Cdelta itself is also an
LND: after division by delta!, it acts as N on A and sends u to
beta_delta in A, so repeated application to u gives the successive
N derivatives of beta_delta and eventually vanishes. This proves
local nilpotence on B=A[u]. Both derivations are nonzero, and
Cdelta is independent of E over Frac(B) by its nonzero horizontal
part. No common-kernel coordinate theorem follows from that fact.

The restriction N on A is independent of the slice chosen to
write (12). Replacing u by u+a with a in A changes its extension
killing that slice by -N(a)E, not its restriction to A. The terminal
commutator is intrinsic to E,D. The correction in (12) is therefore
essential bookkeeping, not a claim that Cdelta automatically
kills every slice. If a slice polynomial is supplied, every entry
of (12) is computable without generators of A; the wedge test (8)
does not even require its explicit formula.

For completeness, if P(X1,...,Xn) is source-weight homogeneous of
weight w, then D(P)=wP. At positive delta the leading derivation
must kill its E-initial form. Thus N kills the leading coefficient
of EVERY such homogeneous polynomial, not merely the finitely
many coordinate leaders. These initials belong to (ker_A N)[eta],
so their transcendence rank is at most n-1. The dimension count
uses trdeg_C ker_A N=n-2, obtained from a local slice of the
nonzero LND N. This reproduces only the positive-shift part of
the companion576 argument, without its separate recognition claim.

## 4. Zero Euler shift is exactly [E,D]=E

Under (10), the stronger exact test is
\[
\boxed{\delta(D)=0\quad\Longleftrightarrow\quad [E,D]=E.}
\tag{13}
\]
Here the particular equality of the source weights and the actual
E degrees matters. The claim is not made for an arbitrary choice
of positive source weights.

Assume first that delta=0. By (3),(4), D preserves A and
\[
D|_A=N_0,\qquad D(u)=b_1u+b_0,
\qquad b_0,b_1\in A.
\tag{14}
\]
Allow b1 to be zero initially. Write the exact coordinate leaders
Xi=ci u to the di plus lower terms, with ci nonzero in A. Comparing
the top u coefficients in D(Xi)=di Xi gives
\[
D(c_i)=d_i(1-b_1)c_i.
\tag{15}
\]
The source-weight degree of D(ci) is at most that of ci. If b1
were nonconstant, its source-weight degree would be positive, and
the nonzero right side would have degree wt(b1)+wt(ci), strictly
larger. The polynomial ring is a domain and its positive grading
makes the degree of a product additive. Therefore b1 belongs to C.
This argument also covers constant ci, when its left side is zero.

Because D is diagonal and locally finite and A is D-stable, A is
a graded subalgebra: each homogeneous component of any element of
A is recovered by a polynomial in D on its finite spectral span.
Equivalently B/A is a graded VECTOR-SPACE quotient here, not a
quotient ring; no ideal property of A is being asserted.
The actual slice u is not in A. At least one of its homogeneous
components u_w is therefore outside A. Taking the weight-w part
of D(u)-b1u=b0 in A yields (w-b1)u_w in A. Consequently
b1=w. Weight zero consists only of constants, so this w is a
strictly positive integer. Equation (15) now says that the nonzero
ci is a D eigenvector of weight di(1-b1). Polynomial weights are
nonnegative, and di is positive, so b1 is at most one. Hence
\[
b_1=1,\qquad D(c_i)=0,\qquad c_i\in\mathbb C^*.
\tag{16}
\]
Equation (14) gives [E,D]=E, proving the forward implication.
Conversely this identity gives C1=E nonzero and C2=0. The last
commutator is vertical, so (8) gives delta=1-1=0. This proves (13)
and shows that the terminal order is exactly one in the zero-shift
Euler case, never zero.

Equation (16) has an immediate rank consequence: zero Euler shift
forces the full coordinate-initial algebra
C[c1 eta to the d1,...,cn eta to the dn] to have rank one. Thus
coordinate-initial rank at least two forces positive shift, and
then Section 3 bounds even the larger algebra of all homogeneous
initials by rank n-1. Rank one alone does not imply zero shift,
as the next actual controls show.

One can summarize the safe Euler computation as follows. Form the
successive actual commutators until the first zero; test the last
one by the minors (9). A vertical terminal commutator occurs
exactly in the zero-shift case, where it equals E and occurs at
order one. Otherwise its order is the positive shift, and (12)
recovers the additional LND. This is an exact test, not an a priori
bound on the number of iterations in a globally minimizing frame.

## 5. Actual controls for arbitrary positive order and its boundary

For every integer d at least two take B=C[a,b,c,u], E=partial_u,
and the actual polynomial coordinates
\[
X_1=a+u^d+u^{d-1},\qquad
X_2=b+u,\qquad X_3=c+u,\qquad X_4=u.
\tag{17}
\]
Their entire inverse is
\[
u=X_4,\qquad a=X_1-X_4^d-X_4^{d-1},\qquad
b=X_2-X_4,\qquad c=X_3-X_4.
\tag{18}
\]
Both compositions are identities, so these are actual coordinates,
not an abstract polynomial curve or a prescribed degree tuple.
Their positive E degrees are (d,1,1,1), with all leading
coefficients one and initial rank one. Their weighted Euler field is
\[
D=(da+u^{d-1})\partial_a+b\partial_b+c\partial_c+u\partial_u.
\tag{19}
\]
For example this follows directly by applying the Euler derivation
in Xi to every inverse coordinate in (18). On A=C[a,b,c] the exact
maximum coefficient degree is d-1, while deg D(u)-1=0. Hence
delta=d-1. Its complete positive-order commutators are
\[
C_k=\frac{(d-1)!}{(d-1-k)!}u^{d-1-k}\partial_a
                       +\mathbf1_{k=1}E\quad(1\le k\le d-1),
\qquad C_d=0.
\tag{20}
\]
At d=2 this says C1=partial_a+E. The vertical correction is
already nonzero for the original displayed slice: subtracting
C1(u)E recovers N=partial_a. At d at least three, the terminal
commutator is (d-1)! partial_a. Thus the positive shift and the
terminal order can be arbitrarily large even for explicit polynomial
kernels and an actual coordinate slice visible in the same frame.

For a separate zero-shift control take
\[
(X_1,X_2,X_3,X_4)=(a+u,b+u,c+u,u),\qquad
D=a\partial_a+b\partial_b+c\partial_c+u\partial_u.
\tag{21}
\]
The inverse subtracts X4 from the first three entries. Its degree
tuple is (1,1,1,1), delta=0, but C1=E is nonzero and C2=0.
Together with d=2 in (17), this shows why terminal order one by
itself cannot distinguish shifts zero and one. The wedge test
and the correction cannot simply be omitted.

These controls do not assert global degree minimality. They have
obvious polynomial shears back to the invariant coordinates a,b,c
and the slice u. They establish the stated algebraic boundaries:
positive shift is compatible with an already polynomial kernel;
rank-one initials do not force zero shift; terminal order alone
does not always equal shift; and the raw last commutator can have
a vertical component. They do not refute or prove a stronger
descent theorem for a genuinely globally minimizing positive frame.

## 6. What becomes computable and what does not

The required inputs are the actual polynomial fields E,D, and an
actual slice only if the extension killing that particular slice
is wanted. Iterated brackets, zero tests and the minors (9) take
place in the actual polynomial coordinate ring. Thus the formulas
do not hide a requirement to first compute generators of A.

At positive Euler shift they construct the explicit commuting pair
E,Cdelta, or alternatively the commuting pair E,N-tilde, and determine
a nonzero LND of A by restriction. Each pair's common kernel is
exactly ker_A N. No commutation of Cdelta with N-tilde is asserted.
No conclusion that this common kernel
is a polynomial ring, contains an actual coordinate, or supplies
a coordinate-completable cancellation remainder has been proved.
In particular there is no implication here that a displayed
coordinate can be lowered by a polynomial shear. The delta-zero
test is a computable reformulation of that branch of the Euler
argument, not a proof that a globally minimum frame attains it.

Fresh unsaved 0a649b inverted the ENTIRE coordinate Jacobian of
(17), reconstructed (19), checked every commutator through its
first zero for d=2,3,6, and checked the full coordinate inverses.
It also checked (21), including the nonzero vertical C1. The
uniform proofs (17)--(20), not those finitely many checks, give
the arbitrary-d statement. The general finite-conjugation,
all-ring degree, local-nilpotence and grading arguments are
proved in Sections 1--4 without a saved checker.

No saved checker was executed, imported, compiled or rerun.
No earlier source or canonical record was edited. The companion576
still requires its own complete independent saved-source review;
this note makes no certification of its separate recognition step.
This author-held note likewise requires independent full review.
No novelty, coordinate-entry, globally minimizing-frame descent,
or unrestricted cancellation conclusion is asserted.
