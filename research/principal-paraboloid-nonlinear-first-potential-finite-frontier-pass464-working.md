# Nine necessary degree pairs in the nonlinear first-potential branch

This is a scoped synthesis, not a recognition theorem. Under EVERY
actual hypothesis of264, assume k=s+f, f_s=0, n_ss nonzero and f'''
nonzero. Then n is quadratic in s over the exact coefficient field,
sigma is neither constant nor affine, and only the nine degree pairs
listed below remain possible. The list is necessary, not a list of
realized charts or a finite list of coefficient functions.

## 1. Full actual scope

Retain the complete supplied chart
[264](principal-one-affine-paraboloid-chart-pass264-working.md), including
the original globally sliced ring
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\qquad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the entire weighted initial kernel},\\
X=a_0u+x_0,\quad a_0\ne0,\quad x_0\in A,\qquad
N=[u^4]\partial_Z|_A\ne0,\\
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,
\quad Nv=1,\\
O=L[A]=L[v]=L[y,\sigma,\theta],\qquad
\operatorname{Frac}A=L(v)=\mathbb C(y,z,w),\\
J_{t,s,v}(X)=-a_0^4\in L^*.
\end{gathered}
\tag{1}
\]
The selected partial, localization and all other original264 hypotheses
remain required. The displayed equations are not a replacement by
formal polynomial data. The coefficient partials commute and have
joint constants C. Write
\[
\mathbb F=\ker_L\partial_s,\quad [\mathbb F:\mathbb C(t)]<\infty,
\qquad k=s+f,\quad f\in\mathbb F,\quad e=n_{ss}\ne0,
\quad f'''\ne0.
\tag{2}
\]
Primes on f mean exact t-derivatives. No rationality of either field
is assumed. Intrinsic degrees below are degrees in v over L.

## 2. Statement

Under (1),(2),
\[
n=\frac e2s^2+\nu_0s+n_0,\qquad e,\nu_0,n_0\in\mathbb F,
\qquad e_s=0.
\tag{3}
\]
Put a=deg(sigma) and r=deg(y)=deg(theta). These are positive and
a is at least two. The necessary pairs are exactly the following
remaining entries of the degree bounds; this does not assert their
existence:

| Alternative | Remaining necessary pairs (a,r) |
| --- | --- |
| Strict: r=2a | (2,4), (3,6), (4,8), (5,10), (6,12) |
| Balanced: 2r=3a | (2,3), (4,6), (6,9), (8,12) |

Let x,q be the affine centerings of460 and
eta=lc(x)/lc(q). In the strict alternative,
\[
\eta=-\frac1{2(t-\tau)},\qquad
e=-\frac1{2(t-\tau)^2},\qquad \tau\in\mathbb C.
\tag{4}
\]
In the balanced alternative,
\[
\begin{gathered}
f''''\ne0,\qquad \eta=-\frac{4ef'''}{f''''}\in\mathbb F^*,
\qquad \eta^2+e/2\ne0,\\
4f'''f''''e_t=e(f'''')^2-32e^2(f''')^2.
\end{gathered}
\tag{5}
\]
These are additional necessary coefficient conditions. They are not
claimed to suffice for the scalar, minor unit or actual realization.

## 3. Proof of the degree and boundary coverage

The complete arbitrary-n equations in
[458](principal-paraboloid-arbitrary-first-potential-birational-projection-pass458-working.md)
give a cubic H-h, monic quadratic in its first formal variable, and
the genuine Q-q0 of total degree at most four. Both vanish on the whole
polynomial line O, and their evaluated
gradient minors generate O. These are the296 inputs retained by458.

The elementary argument of
[299, Sections1--4](principal-paraboloid-generic-degree-bound-pass299-working.md)
therefore applies directly. No plane-projection conclusion from its
Section5 or its earlier290 dependency is needed here. To keep the
logical step explicit, let D be a polynomial gcd of the two equations.
If D evaluated to zero, the two evaluated gradients would be multiples
of grad(D), contrary to the minor unit. Hence their quotients both
vanish. The original minors are D_ev squared times the reduced minors,
so D_ev is a unit of O. The coprime quotients have total degrees
alpha<=3 and beta<=4, both positive.

Their exact homogenizations in four variables are coprime. The two
nonzerodivisor multiplication sequences give degree-N quotient
dimension
\[
\alpha\beta N+\frac{\alpha\beta(4-\alpha-\beta)}2
\quad\text{for all sufficiently large }N.
\tag{6}
\]
It surjects onto the evaluated polynomials of total degree at most N.
Let d be the maximum of the three intrinsic generator degrees and
choose a generator p of degree d. Whole generation expresses each of
1,v,...,v^(d-1) in the generators, with some fixed total-degree bound C.
The d(N-C+1) polynomials p^j v^i, for 0<=i<d and 0<=j<=N-C, lie
in that image and have distinct intrinsic degrees. Comparison with
(6) for arbitrarily large N gives d<=alpha*beta<=12. Extra components
of the two-equation intersection do not alter this surjection argument.

Next,
[462](principal-paraboloid-constant-sigma-nonlinear-first-slope-exclusion-pass462-working.md)
excludes constant sigma, including sigma zero. This uses the original
scalar and an actual-coordinate prime-square contradiction, not a
gradient assertion for a sliced conic. It even holds without f'''
nonzero, although (2) is retained in this synthesis.

For nonconstant sigma,
[460](principal-paraboloid-nonlinear-first-slope-tangent-degree-reduction-pass460-working.md)
proves (3), deg(x)=deg(q)=deg(y)=deg(theta)=r and 2r>=3a. In particular
r>a, so the affine centerings do not cancel the original leading terms.
It also proves the coefficient gates (4),(5).

If 2r>3a,
[461](principal-paraboloid-strict-nonlinear-degree-ratio-pass461-working.md)
proves r=2a. Its complete interval argument includes r=5a/3, r=7a/4,
r=5a/2 and the r=3a endpoint; none is being silently omitted. The
endpoint uses the all-parameter collision lemma of
[459](principal-paraboloid-affine-sigma-arbitrary-first-potential-reduction-pass459-working.md).
If 2r=3a, the balanced alternative remains.

Finally,
[463](principal-paraboloid-affine-sigma-irrational-residue-exclusion-pass463-working.md)
excludes a=1. Its own459 input first forces the degree pair (1,2),
and the actual scalar and minor then give the irrational-residue
contradiction in the finite field mathbb F. This is not an extension
of that argument to higher intrinsic degrees.

Thus a>=2, r<=12 and either r=2a or 2r=3a. In the first case the
integers a are 2 through6. In the second case a is even and at most8,
so a is 2,4,6 or8. This proves the complete displayed table and covers
constant, zero and affine sigma separately.

## 4. Verification and the remaining problem

Root read the complete current459--463 sources and freshly reread264.
The full299 source was read, but only its Sections1--4 are invoked.
Geometry independently reconstructed the gcd, homogenization and
whole-line dimension argument and the degree-table composition.
Fresh unsaved521cbd checked the binomial dimension identity and
enumerated its integer bounds. The preceding written inequalities,
not enumeration software, prove that no degree pair is missed.

The new component arguments have separate AI source reviews and
fresh unsaved identity checks recorded in the research ledger.
The earlier actual264/296/458 inputs retain their previous pedigree;
this synthesis is not a recursive re-certification of the entire
project. A separate held-source audit of this synthesis is recorded
only after completion.

The nine entries are degree patterns, not nine numerical cases.
Their coefficient functions still belong to finite algebraic function
fields of unbounded unspecified complexity. No entry is asserted to
occur, and no all-entry exclusion or original-ring recognition follows.
Arbitrary varieties are not known to satisfy (1),(2). Variable or zero
coupling, other initial kernels and time-degree frames, and arbitrary
actual-frame entry are not resolved by this note.

The full cancellation conjecture remains unsolved. No saved checker
was executed, imported, compiled or rerun. No external expert review,
Lean certification, historical novelty, publication or outreach is
claimed or authorized by this synthesis.
