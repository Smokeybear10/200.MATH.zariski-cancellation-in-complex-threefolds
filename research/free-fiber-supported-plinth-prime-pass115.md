# Supported ramification at one or two reduced simple fiber components

In the actual quadratic quotient, a whole reduced fiber consisting of
one multiplicity-one component has a slice after localizing at its base
point. If the whole fiber has two multiplicity-one components, the first
derivative image has exactly one analytically irreducible base prime in
its support. The associated quadratic constant cover splits at that
closed point. Its splitting does not contradict primeness of the base
curve germ.

This extends only the supported-base-prime part of
[descent113](whole-double-ramified-completion-descent-pass113.md).
Its primeness and scalar-contraction conclusions for the completed
threefold divisor are not transferred to the split case.

## 1. Exact actual hypotheses and the first image

Retain the supplied quadratic frame and its actual quotient. In
particular, write
\[
\begin{gathered}
X=\operatorname{Spec}A,\quad A[u]=\mathbb C^{[4]},\quad
0\ne N\in\operatorname{LND}(A),\quad S=\ker N=\mathbb C[s_1,s_2],\\
A\text{ faithfully flat over }S,\quad A_K=K[v],\quad K=\operatorname{Frac}S,\\
A_{S_{(p)}}/pA_{S_{(p)}}=k'_p[w],\quad
k_p=\operatorname{Frac}(S/p),\quad [k'_p:k_p]\in\{1,2\},\quad
\bar N\ne0.
\end{gathered}
\tag{1}
\]
Every irreducible p in S remains prime in A. At every degree-two
constant divisor, one actual good generator survives nonconstantly
and has N-degree at most two. These are the whole-divisor hypotheses
of [divisor91](nonconical-residue-degree-bound-pass91.md), not a claim
about a selected subring only. They supply exactly the inputs of
[DVR classification107](quadratic-constant-divisor-filtration-pass107.md).

Fix a closed base point m. Put R=S_m and A_R=A tensor_S R. Let F_j
be ker N^(j+1) on A_R. By [module102, Section 2](quadratic-degree-module-fiber-rigidity-pass102.md),
F_1 is finite free of rank two. Its element 1 is unimodular: otherwise
1 belongs to mF_1 and hence mA_R, contrary to faithful flatness.
Extend 1 to a basis 1,r. The full kernel is R, so
\[
F_1=R\oplus Rr,\qquad Nr=P\ne0,\qquad I_1=N(F_1)=PR.
\tag{2}
\]
This principality needs neither a closed-fiber injection of all F_1 nor
a polynomial coordinate on A_R.

At a degree-one generic divisor, bar N is a nonzero translation on
k_p[w]. Choose a local slice z with Nz=p^d, after absorbing a DVR
unit. If d>0, bar z is killed by bar N and belongs to k_p. Lift its
constant value to the base DVR. Then (z minus the lift)/p is an actual
element of the localized algebra with derivative p^(d-1). Finitely
many repetitions give a slice. At a degree-two divisor, classification107
gives I_1=(p^e) with e>0. Localization commutes with the invariant
kernels, and therefore
\[
p\mid P\quad\Longleftrightarrow\quad [k'_p:k_p]=2
\qquad(p\text{ an irreducible base equation through }m).
\tag{3}
\]

## 2. The supported lattice does not require an irreducible whole fiber

X is smooth, factorial and contractible by the polynomial cylinder.
Choose the product-complement curve Gamma and finite factorization
E to Z to Gamma supplied by the
[repaired support argument96, Sections 1--4](irreducible-fiber-dependency-audit-pass96.md).
Every degree-two divisor belongs to Gamma: outside Gamma its generic
point would lie in a polynomial-line product, whose constant field has
degree one. Additional degree-one components of Gamma are permitted.
The chosen exceptional finite set may include m.

Let r_b count the normalized base branches of Gamma through m. Above
branch j let q_j count the normalized source points, with positive
indices e_ja. The normalized cover degree is N_j=sum_a e_ja, equal to
the actual divisor constant degree in (1). Put q_b=sum_j q_j. If the
entire reduced fiber has d components of whole-fiber multiplicities
mu_i, the actual component Thom classes satisfy
\[
\begin{gathered}
T:\mathbb Z^{q_b}\longrightarrow\mathbb Z^{r_b},\qquad
T(e_{ja}^{\rm std})=e_{ja}e_j^{\rm std},\\
(v_1,\ldots,v_d)\text{ is a full integral basis of }
T^{-1}(\mathbb Z\mathbf1),\qquad Tv_i=\mu_i\mathbf1,\\
d=q_b-r_b+1,\qquad q_j\ge1,\quad N_j\le2.
\end{gathered}
\tag{4}
\]
The rank and full support statement is96(5); the componentwise linking
coefficient is written explicitly in
[supported97(1)](quadratic-supported-lattice-pass97.md).
It is the generic whole-fiber length along each component. It remains
valid for a reducible whole fiber. No multiplicity formula for one
component of a reducible fiber is substituted for (4).

The source facts behind (4) are Kaliman's Lemmas 2.1--2.2, Lemma 3.1
and Proposition 3.2, with the integral normalization-homology and support
repair given in96. They require the actual reduced prime divisor
pullbacks, product complement, and homology vanishings. They do not
require that Z be normal, that all its normalized components be affine
lines, or that the normalized source points have distinct images in Z.
The finite curve map is proper; the additive quotient need not be.
[Author-hosted primary source](https://www.math.miami.edu/~kaliman/library/Ka.invent.2004.c%2B.pdf).

## 3. A one-component simple fiber has a local slice

Assume d=1 and mu_1=1. If m is outside Gamma, it is in the product
complement and no degree-two divisor passes through it. Otherwise (4)
gives q_b=r_b, so every q_j is one. Its singleton index is N_j.
The corresponding row of Tv_1=1 reads N_j(v_1)_j=1 in integers.
Thus every N_j is one. In either case (3) shows that P has no prime
factor in the local UFD R. It is a unit, and r/P is a slice. The
finite Taylor slice formula gives
\[
\boxed{\quad
d=1,\ \mu_1=1\quad\Longrightarrow\quad
I_1=R,\qquad A_R=R[r/P],\qquad N(r/P)=1.
\quad}
\tag{5}
\]
For completeness, successive subtraction of powers of the slice,
starting from an element's highest nonzero N-iterate, expresses every
element of A_R as a polynomial in the slice with invariant coefficients.
This uses local nilpotence on actual A_R, not on a completion.

## 4. Two simple components force one unibranch base prime

Assume d=2 and mu_1=mu_2=1. Such a fiber cannot be in the product
complement. Equation (4) gives sum_j(q_j-1)=1. Exactly one base branch
has q_j=2, and all others have q_j=1. The split branch has degree two
with indices (1,1), since N_j<=2. A singleton branch of degree two
would give 2(v_i)_j=1, impossible. Every remaining branch has degree
one. Thus there is exactly one degree-two normalized base branch.

By (3), P is nonunit and its prime factors are exactly the degree-two
divisors through m. Each such prime has at least one normalized branch
there. The unique degree-two normalized branch consequently belongs to
one prime p, and that prime has only one normalized branch at m:
\[
\boxed{\quad
d=2,\ \mu_1=\mu_2=1\quad\Longrightarrow\quad
P=v p^e,\quad v\in R^*,\quad e\ge1,\quad
p=0\text{ is unibranch at }m.
\quad}
\tag{6}
\]
Notice that the two-component calculation uses only the integer row
equations and the supported rank. Positivity of the columns would give
their split restrictions as (1,0) and (0,1), in some order, but is not
needed to prove (6).

## 5. Base completion and the split-cover warning

Let C0=R/pR. Its normalization V is finite, and (6) makes V local with
one maximal ideal over m. It is a DVR with residue field C. Its completion
is C[[t]]. The finite inclusion C0 into V stays injective on completion,
and mV and the DVR maximal ideal define equivalent topologies. Thus
\[
\boxed{\quad \widehat R/(p)\hookrightarrow\widehat V
       =\mathbb C[[t]],\qquad p\widehat R\text{ is prime}.\quad}
\tag{7}
\]
This is the base-curve completion argument from113, Section 3. It uses
finite normalization of a curve and exactness of completion for finite
modules, not normality of the original curve. Authoritative references
are [Stacks 0C44, curve normalization](https://stacks.math.columbia.edu/tag/0C44)
and [Stacks 00MA, finite-module completion](https://stacks.math.columbia.edu/tag/00MA).

A nonzero conductor element d satisfies dV contained in C0. Completing
and then inverting d shows that C0hat and Vhat have the same fraction
field. This is the scalar field used in the following cover comparison.

The degree-two constant cover now has two normalized points above the
one base branch, each of index one. Completing its finite normalization
there gives the product of the two local DVR completions, each rank one
over Vhat. After passing to the completed base fraction field, the
quadratic constant algebra is a product of two copies of that field,
not a quadratic field. This is opposite to the ramified whole-double
situation in113. Formula (7) is all that transfers. In particular this
note does not assert that p remains prime in A_R tensor_R Rhat or that
its powers contract from the whole-fiber completion.

## Proof scope

The complete retained96 support proof, its97 component-linking statement,
the91 actual divisor inputs, the107 local classification, and113's
finite curve completion argument were reread for this application.
The source URLs identify the established dependencies, not additional
fresh full primary-proof reviews in this note. Only the one-component
slice and two-component analytic-base-prime consequences are new here.
No assumption about the speed normal L(m), selected c, original plane
ideal, or purity of a higher degree module enters the proof. No numerical
method or global cancellation assertion is added. Files through114 stay
unchanged.
