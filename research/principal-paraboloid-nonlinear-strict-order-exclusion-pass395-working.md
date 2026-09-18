# Only equal degrees or a nonzero-slope affine boundary remain

Working synthesis in the complete supplied actual264 chart: assume
k=s and n_ss nonzero. If theta is nonconstant on the intrinsic line,
then theta and sigma have equal degree, between one and six. If theta
is constant on that line, sigma and y both have degree one and the
affine y/sigma slope is nonzero. In particular both strict orders with
theta and sigma nonconstant are excluded.

This does not prove n_ss=0, recognize the original invariant ring,
or establish entry of an arbitrary cancellation candidate into the
supplied chart. It is a composition of scoped working arguments,
not a new recursive certification of all earlier dependencies.

## 1. Complete actual entry and precise conclusion

Retain every hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
including the actual global slice and the full initial kernel:
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A_0[u],\quad E=\partial_u,
\quad a_0=EX\ne0,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\qquad
I_{\rm initial}=(X^2Z-Y^2),\\
N=[u^4]\partial_Z|_{A_0}\ne0,\qquad
L=\operatorname{Frac}\ker_{A_0}N,\quad [L:\mathbb C(t,s)]<\infty,\\
Nv=1,\qquad
O=L[v]=L[y,\sigma,\theta]=L[y,z,w],\quad
K=\operatorname{Frac}A_0=L(v)=\mathbb C(y,z,w).
\end{gathered}
\tag{1}
\]
The selected partial is the literal actual Z-partial. All exact
coefficient partials, actual potential identities, evaluated unit
gradient/minor conditions and both returns of264 remain in force.
In the already normalized coupling k=s, the complete literal rows are
\[
\begin{aligned}
Y&=y+\sigma X+tX^2,\\
Z&=z+(2t\sigma+s)X+t^2X^2,\\
W&=w+\theta X+sX^2,\\
z&=2ty+\sigma^2+\theta+n,\\
w&=\ell-2\sigma y-n_t\sigma-n_s\theta,\\
\det\frac{\partial(Y,Z,W)}{\partial(t,s,v)}&=-a_0^4\in L^*.
\end{aligned}
\tag{2}
\]
Assume n_ss is nonzero. Degrees below are intrinsic v degrees over
the exact field L, with zero polynomial degree minus infinity.

The necessary alternatives are
\[
\boxed{
\begin{array}{ll}
\theta\notin L:&1\le\deg\theta=\deg\sigma\le6,
\quad\deg y\le\deg\sigma;\\
\theta\in L:&\deg\sigma=\deg y=1,\quad
y=\lambda\sigma+r,\quad\lambda\in L^*,\ r\in L.
\end{array}}
\tag{3}
\]
The alternatives are not existence claims. Neither is excluded or
recognized by this synthesis.

## 2. Previously excluded orientation and the exact opposite-order list

The retained synthesis
[383](principal-paraboloid-nonlinear-theta-dominant-exclusion-pass383-working.md)
already proves
\[
1\le\deg\sigma\le6,\qquad
\deg\theta\le\deg\sigma,\qquad
\deg y\le\deg\sigma.
\tag{4}
\]
In particular sigma is nonconstant. Its proof treats constant sigma
and all theta-dominant pairs, including the two highest-Q branches
of its quadratic-cubic pair. No new symmetry is being used to
exchange the two orientations here.

Suppose now that theta is nonconstant and has strictly smaller degree
than sigma. The full actual reduction
[385](principal-paraboloid-nonlinear-sigma-dominant-degree-reduction-pass385-working.md)
leaves exactly
\[
(\deg\theta,\deg\sigma)\in\{(1,2),(2,3),(4,6)\}.
\tag{5}
\]
The compatibility argument
[387](principal-paraboloid-sigma-dominant-coefficient-integrability-pass387-working.md)
forces the leading y/sigma ratio to be zero, gives
n=gamma*t+f with gamma complex and f_t=0, and places deg y below
deg theta. Its proof retains the exact finite coefficient field.

The actual complex translation Y*=Y+gamma/2, fixing X,Z,W, removes
gamma*t from n. Each of388--392 verifies that it preserves the full
initial kernel, selected literal partial, exact time degrees, both
returns and calibration. Thus write
\[
n=f\in S=\ker_L\partial_t,\qquad
\nu=f_s\ne0,\quad e=f_{ss}\ne0.
\tag{6}
\]
This normalization is used only in the strict nonconstant-theta
case. It is not imported into the constant-theta boundary below.

## 3. Exclusion of each pair in the opposite-order list

For pair(1,2), y belongs to L. Its exact derivative y_t is either
zero or nonzero. The full-scalar argument
[388](principal-paraboloid-affine-theta-moving-intercept-exclusion-pass388-working.md)
excludes the nonzero case through incompatible coefficient partials.
The separate strong-return and scalar argument
[389](principal-paraboloid-affine-theta-constant-t-intercept-exclusion-pass389-working.md)
excludes the zero case. The derivative split is unchanged by the
constant Y translation, and no subcase is omitted.

For pair(4,6), the literal-cubic exclusion
[390](principal-paraboloid-sigma-dominant-four-six-cubic-exclusion-pass390-working.md)
matches the abstract degree-(2,4,6) line classification370 explicitly,
computes the entire line ideal and applies the finite filtered-degree
lemma373. Its genuinely rebuilt cubic has a mandatory PRV term
incompatible with that ideal. It includes zero centered quadric
level and does not infer the cubic by swapping sigma and theta.

For pair(2,3), the intrinsic remainder r=y+ell_t/(2nu) has degree
one, so O=L[r]. Define the exact coefficient gate
\[
\mathcal E=e_s/6-e^2/(2\nu)\in S.
\tag{7}
\]
The zero-gate proof
[391](principal-paraboloid-sigma-dominant-quadratic-cubic-zero-gate-exclusion-pass391-working.md)
uses the complete lower fourth-potential coefficients and one actual
scalar coefficient. Its derived rationality followed by integrality
excludes the nonzero auxiliary factor; its complementary zero factor
forces the actual nonzero scalar to vanish. It retains all zero
slopes and does not assume L=S(t) in this branch.

If Ecal is nonzero, the exact normal form
[392](principal-paraboloid-sigma-cubic-nonzero-gate-normal-form-pass392-working.md)
forces polynomial coefficients in t over S, with
ell=F*t^2/2+B*t+D, F in S*, and Ecal/F^4 complex nonzero. It also
derives L=S(t) from the actual strong return. The actual original
slice and selected derivation then give
[393](principal-paraboloid-sigma-dominant-polynomial-return-degree-gate-pass393-working.md)
\[
S[\mathcal B]=S[X,t,r],\quad S[A_0]=S[t,r],\quad
S[y,z,w]=S[t,y],\quad a_0,Nr,J\in S^*.
\tag{8}
\]
Its line-embedding degree argument forces deg_t sigma at most two
after fixing y. These ring equalities are proved by reverse polynomial
inclusion, not assumed from field equality.

Finally the complete lower-potential exclusion
[394](principal-paraboloid-sigma-dominant-nonzero-gate-lower-potential-exclusion-pass394-working.md)
combines that degree bound with the actual r3 coefficient, including
the derivative of its evaluated third level. Two necessary modes
reduce to one without discarding their zero overlap. Its next two
coefficients force k1=nu*Ecal/e^2=1/2 while also requiring
\[
\frac\nu e\partial_s k_1=-k_1(1+4k_1).
\tag{9}
\]
The two sides are then zero and -3/2, a contradiction. Every lower
coefficient function remains present until it cancels by an explicit
coefficient equation.

Both Ecal alternatives and therefore every pair in(5) are impossible.
Combined with(4), this proves the first line of(3).

## 4. The constant-theta boundary is affine with nonzero slope

When theta belongs to L, the separate sliced-quadric argument
[386](principal-paraboloid-nonlinear-constant-theta-line-gates-pass386-working.md)
proves O=L[sigma], deg sigma=1 and y=lambda*sigma+r with lambda,r
in L. This case did not satisfy the nonconstant-theta hypothesis of385
or387, and those later derivative conclusions are not imported.

The direct full-scalar proof
[396](principal-paraboloid-constant-theta-zero-slope-exclusion-pass396-working.md)
excludes lambda=0 without assuming n_ts=0 or replacing n by f(s).
Its P-squared and XP coefficients first force r_t=0, and the next
P coefficient then forces the constant scalar coefficient to vanish.
This contradicts the actual nonzero calibration. Thus lambda is
nonzero, y has degree one, and the second line of(3) follows.

## 5. Remaining scope and verification boundary

The next genuinely unresolved cases in this supplied nonlinear chart
are equal positive degrees and the nonzero-slope affine constant-theta
boundary. The still broader gaps are general coupling k, other full
initial ideals, and arbitrary-chart entry. None of(3)--(9) supplies
an original coordinate of A0 or proves A0 is a polynomial ring.

Root freshly read383 in f755dc,388 in38d68d,389 in16d5aa,390 in
d05b88,391 in6f7b3e,392 in3ecddb,393 in574673,394 in db946a,
386 in8a3fce and396 in a7a15b. The earlier385/387 full reads and
independent audits remain recorded in the ledger. Source hashes and
separate reviews of the new notes are recorded there; this synthesis
requires its own independent read before canonical acceptance.

Fresh exact identities include Root9621aa for391's complete lower Q
and scalar, Root8a9d03/3c4936 for394's complete r3 and final elimination,
and Root15c784 for396's unnormalized full scalar. Their zero residuals
support the written proofs, not the unverified assertion of any
original-coordinate descent or unrestricted theorem.

No saved checker was executed, imported, compiled or rerun. There is
no claim of recursive formalization, human-expert certification,
novelty, submission or a solution of the unrestricted conjecture.
