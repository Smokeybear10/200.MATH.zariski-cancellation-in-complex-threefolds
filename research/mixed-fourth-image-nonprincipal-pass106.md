# The actual mixed fourth-derivative image is not principal

In the supplied actual collapsed mixed quadratic sector with
nonzero speed normal, the fourth derivative-image ideal is
nonprincipal. It requires either two or three generators, and
exactly two if the third-degree residue image has dimension three.
Thus the fourth degree-module quotient is not a free rank-one
module, despite freeness of both degree modules themselves.

The obstruction uses an admissible parameter that also generates
the proposed image ideal. Its actual normalization boundary
contradicts a polynomial slice over the corresponding base DVR.
No parity assertion about specialized polynomial degrees is used.

## 1. The exact ideal and actual hypotheses

Retain the full actual mixed hypotheses of
[boundary106](mixed-admissible-quartic-boundary-pass106.md)
and [rank-defect105](mixed-cubic-rank-defect-pass105.md).
In particular A is a smooth affine complex domain, the original
three-good constant-acceleration frame is supplied, N is its
primitive canonical LND, and S into A is faithfully flat. Put
\[
\begin{gathered}
S=\ker(N|_A)=\mathbb C[s_1,s_2],\qquad
R=S_{\mathfrak m},\qquad\mathfrak n=\mathfrak mR,\qquad
K=\operatorname{Frac}S,\qquad A_K=K[v],\\
F_j=\ker N^{j+1},\qquad M_j=(F_j)_R\simeq R^{j+1},\qquad
I_4=N^4(M_4)\subset R,\\
0\longrightarrow M_3\longrightarrow M_4
\xrightarrow{\ N^4\ }I_4\longrightarrow0,\\
A/\mathfrak mA=\mathcal D[c],\qquad
\mathcal D=\mathbb C[G]/(G^2(G-1)),\qquad
\epsilon=G-G^2,\quad e_1=G^2,\\
\bar N=(\lambda\epsilon+\rho e_1)\partial_c,
\quad\lambda,\rho\in\mathbb C^*,\qquad
c\in F_4,\quad N^4c\ne0.
\end{gathered}
\tag{1}
\]
The fiber is the whole nonreduced mixed fiber, and L(m) is nonzero.
Write W_j for the image of M_j in A/mA. Then W_2 is either
C1+CG or D, and dim W_3 is at most three by105. Freeness of M_j
does not assert freeness of I_4 or injectivity of every module
fiber into A/mA. Equation (1) is the exact sequence of actual
modules, not a sequence obtained by assuming either property.

## 2. Generic perturbation and ideal-wide base order

For any V in M_4, the reduced values of V+alpha c are nonconstant
on both component lines for all but at most two alpha in C.
On either line at most one alpha can make a fixed polynomial
plus alpha c constant. For an admissible alpha, the any-function
strict inequality97 gives
2d_2+d_1 < deg_N(V+alpha c) <= 4, with d_i positive integers.
It follows that both component degrees are one. Subtracting
alpha c shows that both reduced values of every V in M_4
are affine. This is also proved in boundary106, Section 2.

Thus its whole residue has the form
(a_2c+b_2+epsilon beta(c), a_1c+b_1), now allowing zero slopes.
The second whole-fiber N-iterate is zero: the double factor
contributes epsilon squared, while the second derivative of
the affine simple value is zero. Consequently
\[
\begin{gathered}
N^2(M_4)\subseteq\mathfrak nA_R\cap M_2,\qquad
\boxed{\ I_4\subseteq\mathfrak n.\ }\\
\boxed{\quad
\mathcal W_2=\mathcal D\quad\Longrightarrow\quad
I_4\subseteq\mathfrak n^3.
\quad}
\end{gathered}
\tag{2}
\]
For the first ideal membership, further N-iterates preserve
nA_R because N kills the base, and faithful flatness contracts
the invariant result to n. In the rank-three W_2 case,
[mixed-image104](mixed-degree-module-artin-image-pass104.md)
gives M_2 intersect nA_R=nM_2 and N^2(M_2) contained in n squared.
Applying N squared to N^2(M_4) contained in nM_2 proves the
last membership. It concerns the entire ideal, not just N^4c.

Localized coefficients cause no extra issue here or below.
Each finite list of elements of A_R has a common denominator
in S outside m. Clearing it preserves N-degree and all component
degrees, since its residue at m is a nonzero complex number.

## 3. A putative principal image has an admissible generator

Suppose I_4 were principal, say I_4=gR. It is nonzero by (1).
By the definition of the image there is U in M_4 with N^4U=g.
Write N^4c=gh with h in R. Choose alpha in C avoiding the
at most two nonadmissible values for U+alpha c, and also
avoiding the at most one value satisfying 1+alpha h(m)=0.
Then
\[
\begin{gathered}
V=U+\alpha c\in M_4\text{ is admissible},\qquad
e=1+\alpha h\in R^*,\\
N^4V=ge,\qquad I_4=R\,N^4V,\qquad \deg_NV=4.
\end{gathered}
\tag{3}
\]
The finite avoidance is possible over C. If h(m) is zero,
there is no forbidden value from the unit condition. Thus
admissibility has not been imposed by a perturbation that
loses the ideal-generator property. No assertion puts the
chosen U or V among the specified original generators.

## 4. The parameter's own boundary gives the contradiction

Apply the fully proved arbitrary-admissible boundary106 theorem
to V. There exists an irreducible p in S contained in m for
which the actual generic divisor has constant-field degree one
and V specializes to degree three. Hence
\[
\begin{gathered}
A_{S\setminus(p)}/pA_{S\setminus(p)}=k_p[w],\qquad
\bar N\ne0,\qquad\deg_w\bar V=3,\\
N^4V\in pS_{(p)},\qquad
I_4S_{(p)}=S_{(p)},\\
\boxed{\qquad I_4\text{ is not principal.}\qquad}
\end{gathered}
\tag{4}
\]
Here k_p=Frac(S/(p)) is the full residue constant field.
The first membership follows by differentiating the cubic
residue four times under its nonzero translation. Its invariant
value contracts from pA_(S minus (p)) to pS_(p).

For the unit-ideal statement, use the elementary DVR slice
lift in rank-defect105, Section 2. In the actual ring over
S_(p), choose a local slice t with Nt=p^a after invariant-unit
scaling. If a>0, the residue of t is in ker(bar N)=k_p.
Lift that constant from S_(p), subtract it, and divide by p
inside the actual ring. Repeating lowers a to zero and gives
Nt_*=1. Then N^4(t_*^4/24)=1. Invariant localization commutes
with the kernels and images in (1), proving I_4S_(p)=S_(p).

But (3) makes I_4S_(p) generated by N^4V, which lies in its
maximal ideal. This is impossible. The boundary prime may
depend on V; no fixed prime is required for the contradiction.
The proof uses actual boundary geometry, not an assumption
that an arbitrary quasi-finite parameter map is finite.

## 5. Generator counts and the internal module reduction

Let r be the minimal number of generators of I_4 as an R-module.
Reduce the exact sequence (1) modulo n. Right exactness gives
the exact rank identity
\[
\begin{gathered}
\dim_{\mathbb C}\operatorname{im}
 \big(M_3/\mathfrak nM_3\longrightarrow M_4/\mathfrak nM_4\big)
 =5-r,\\
\boxed{\quad 2\le r\le3,\qquad
\dim\mathcal W_3=3\ \Longrightarrow\ r=2.\quad}
\end{gathered}
\tag{5}
\]
Nonprincipality gives r at least two. The image of the displayed
internal map surjects onto W_3 under the further map into A/mA.
That space contains the independent residues 1,G, so 5-r is
at least two. This proves r at most three. If W_3 has dimension
three, the same inequality gives r at most two, hence equality.
In particular W_2=D implies r=2 by the rank-defect105 conclusion.

There is no assertion that the internal image in (5) equals W_3.
It can have an additional kernel when mapped into the algebra's
fiber. Nor does reduction preserve the injectivity on the left
of (1). The nonprincipal rank-one quotient I_4 is not free over
the local ring R, so (1) does not split as a sequence of R-modules.

## 6. The residual defect is genuinely at the closed base point

The regular local plane R is a UFD. Choose a greatest common
divisor d of a finite generating set of I_4, and divide every
generator by d. Then
\[
\boxed{\quad
I_4=dJ,\qquad J\subsetneq R\text{ is }\mathfrak n\text{-primary},
\qquad \mu_R(J)=\mu_R(I_4)\in\{2,3\}.
\quad}
\tag{6}
\]
The ideal J has no common prime divisor among its generators.
It is nonzero and proper, since otherwise I_4 would be principal.
No height-one prime can contain J. In the two-dimensional local
domain R this forces its radical to be n, hence J is n-primary.
Multiplication by the nonzero d is an R-module isomorphism
from J to I_4, proving the generator-count equality.

At every height-one base prime with constant-field degree one,
the same finite DVR slice lift gives I_4 localized there equal
to the unit ideal. Therefore every prime factor of d must be
a constant-field-degree-two divisor. Divisor valuations detect
only d: J becomes the unit ideal at every height-one prime.
The proof does not assert that d is a unit, that I_4 itself
is n-primary, or that J equals n or any specified power of it.

In the W_2=D branch, the separate
[two-generator matrix refinement106](mixed-full-artin-two-generator-pass106.md)
identifies I_3=(g), I_4=theta g(a,b), with (a,b) a proper
n-primary complete intersection, and improves (2) to I_4
contained in n to the fourth. Its exact matrix uses the
nonprincipality proved here; none of those stronger conclusions
is an input to this proof.

## Scope and provenance

This is nonprincipality of the actual fourth derivative-image
ideal at the mixed closed base point. It is not nonfreeness of
the degree modules, an exclusion of the mixed fiber, or a
global coordinate theorem. The original frame, faithful-flat
full kernel, divisor constant-field bound, and entire mixed
fiber are retained throughout. No reduction from an arbitrary
sliced action to this setting is supplied.

The complete saved admissible-boundary106 proof was independently
read before applying its parameter-dependent conclusion. The
frozen105 boundary, rank and module arguments, checkpoint and
frontier were also consulted; the DVR slice lift is reproduced
above to keep its exact constant-field gate visible. The
original perturbation proposal was supplied by Root. No new
primary-source theorem, numerical method, or test execution is
claimed. All files through105 remain unchanged.
