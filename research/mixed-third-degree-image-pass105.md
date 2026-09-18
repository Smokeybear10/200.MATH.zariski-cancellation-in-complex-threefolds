# Third-degree residues on the actual mixed fiber

In the actual collapsed mixed quadratic sector with nonzero speed
normal, a third-degree element can vary on at most one reduced
component. In fact no element of any N-degree can make the whole
localized algebra finite over its polynomial parameter ring.
The conditional full-rank calculations give exact degree-module
splittings, but not the missing cubic algebra presentation.

The nilpotent residue coefficients also satisfy actual weighted
degree bounds. In the full-rank case with constant reduced values,
the residue space is exactly the four-dimensional space consisting
of the Artin coefficient ring and epsilon times c. The normal
coefficient argument alone does not exclude that fourth direction.
The separate [boundary rank-defect theorem105](mixed-cubic-rank-defect-pass105.md)
now excludes full third-degree residue rank using additional
actual divisor geometry.

## 1. Standing actual data and the two reduced slopes

Use the precise setting of
[mixed-image104](mixed-degree-module-artin-image-pass104.md).
In particular, with R=S_m and n=mR,
\[
\begin{gathered}
S=\ker(N|_A)=\mathbb C[s_1,s_2],\quad A_K=K[v],\quad
N|_{A_K}=\lambda_K\partial_v,\quad\lambda_K\ne0,\\
A/\mathfrak mA=\mathcal D[c],\quad
\mathcal D=\mathbb C[G]/(G^2(G-1)),\quad
\epsilon=G-G^2,\quad e_1=G^2,\\
\bar N=(\lambda\epsilon+\rho e_1)\partial_c,
\quad\lambda,\rho\in\mathbb C^*,\quad
F_j=\ker N^{j+1},\quad (F_j)_R\simeq R^{j+1},\\
\mathcal W_j=\operatorname{im}(F_j\longrightarrow A/\mathfrak mA),
\quad\mathcal W_2=\mathbb C1+\mathbb CG
\text{ or }\mathcal D,\quad c\in F_4,\\
U\in F_3\quad\Longrightarrow\quad
\bar U=(a_1c+a_0+\epsilon\beta(c),\ b_1c+b_0),
\quad a_i,b_i\in\mathbb C,\quad\beta\in\mathbb C[c].
\end{gathered}
\tag{1}
\]
The two entries of the last line refer to the double and simple
factors. Indeed NU lies in F2, whose residue belongs to D by104.
Applying the displayed whole-fiber derivation to an arbitrary
residue shows that both reduced derivatives are constants.
This proves their asserted affine forms. It imposes no bound
on beta by itself.

The hypotheses include the actual original three-good frame,
canonical E-slice, faithful-flat full kernel plane, actual
whole-fiber presentation, and L(m) nonzero. The normalized
volume chart99 and strict source-balance inequality97 will be
used below. None is inferred from module ranks alone.

## 2. Only one component can carry a third-degree parameter

The strict inequality in
[weighted-defect97, Section 2](quadratic-weighted-rank-defect-pass97.md)
applies to every actual function nonconstant on every component,
not only to linear combinations of the original generators.
If a1 and b1 in (1) were both nonzero, the special component
degrees would both equal one, whereas the generic degree of U
is at most three. It would give the contradiction
\[
3=2\cdot1+1\cdot1<\deg_vU\le3.
\qquad\boxed{\quad a_1b_1=0.\quad}
\tag{2}
\]
Since the slope map on F3 is complex linear, its entire image
lies in one coordinate axis, or is zero. If it contained nonzero
vectors on both axes, their sum would contradict (2).

There is a stronger generation consequence, with no degree cutoff:
for no U in A_R is A_R finite over R[U]. Suppose otherwise.
Finiteness descends to each reduced component. A constant value
of U there would make C[c] finite over C, which is impossible.
Thus U is nonconstant on both components and is transcendental
over K. Put T=(R[U])_(nR[U]) and D_U=A_R tensor_(R[U]) T.
The ring T is regular local of dimension two, with residue field
C(U); D_U is finite over T by the contrary assumption.

All maximal ideals of D_U lie over the maximal ideal of T.
Its reduced closed fiber consists exactly of the two generic
component points: each component is C[c], and inverting the
nonzero polynomials in its nonconstant U-residue gives the
finite field extension C(c)/C(U). No other points survive.
At each of these maximal ideals, the target local ring is the
actual regular local ring A_(q_i), of dimension two, and its
closed T-fiber is zero-dimensional. The exact local
[flatness argument92](nonconical-closed-fiber-multiplicity-pass92.md)
therefore applies. Flatness is local on the target, so D_U is
flat over T. Being finite over a local ring, it is free.

Its generic rank is n=deg_v U, while its closed-fiber dimension
over C(U) is 2d_2+d_1, where d_i is the positive component
residue degree. Freeness forces n=2d_2+d_1, contradicting the
any-degree strict inequality97. This also proves directly that
D_U is not finite for any admissible U, even without assuming
A_R finite. For a localized U, clearing its single base
denominator outside m preserves both generic degree and the
component degrees, so the same strict inequality applies.

This excludes a finite parameter presentation of the whole
localized algebra at every N-degree. It does not rule out
quasi-finite parameter maps, infer a finite map from finite
fibers, or exclude every presentation involving a cubic equation
with different degree assignments or generators.

## 3. What the two-dimensional F2 image forces

If U has a nonzero double slope, its N-residue is a nonzero
multiple of epsilon. If it has a nonzero simple slope, that
residue is a nonzero multiple of e1. By (2) these cases do not
occur together. Both epsilon and e1 are independent of 1,G
in the three-dimensional algebra D. Since NU lies in F2,
\[
\boxed{\quad
\dim\mathcal W_2=2\ \Longrightarrow\
a_1=b_1=0\text{ for every }U\in F_3,
\qquad \mathcal W_1=\mathbb C1.
\quad}
\tag{3}
\]
For the last assertion, a first-degree element has residue
alpha+delta G by104. Its square belongs to F2 and has G-squared
coefficient delta squared. If delta were nonzero, that would
enlarge W2 to D. Hence delta is zero.

Thus freeness of F1 does not here justify an injective F1 fiber
map: its rank is two, while its whole-fiber image in this branch
has dimension one. The unresolved image defect is explicit.

## 4. Bounds on the nilpotent coefficient use the actual normal chart

In the generic double chart99, use weights two and one on x and
y=G. The actual leading operator has constant coefficients
\(D_*=\gamma x\partial_y+\delta y\partial_c\), with delta
nonzero; gamma is zero exactly when the first normal action is
zero. Put
\(W=U-a_1c-a_0-(b_0-a_0)G\). On the double its residue is
epsilon times a polynomial beta0 differing from beta by a
constant. In the local generic double ring,
\(W-\beta_0(c)G\in\mathfrak mA_{\mathfrak q_2}\).
Consequently W has weight-one part beta0(c)y. This is a local
membership; the same difference need not lie in the global
whole mixed ideal because of its simple-component residue.

If a1=0 then W is in F3, so N to the fourth of W is zero.
In general W belongs to F4, so N to the fifth of W is zero.
The exact leading expressions are
\[
\begin{aligned}
D_*^4(\beta_0y)
 &=15\gamma^2\delta^2\beta_0''x^2y
   +10\gamma\delta^3\beta_0'''xy^3
   +\delta^4\beta_0^{(4)}y^5,\\
D_*^5(\beta_0y)
 &=15\gamma^3\delta^2\beta_0''x^3
   +45\gamma^2\delta^3\beta_0'''x^2y^2
   +15\gamma\delta^4\beta_0^{(4)}xy^4
   +\delta^5\beta_0^{(5)}y^6.
\end{aligned}
\tag{4}
\]
These follow by applying the displayed derivation four and five
times and collecting coefficients. Each application raises weight
by one. The strict higher-order actual derivation terms and
the terms of W of weight at least two cannot change these
lowest possible weights.

For gamma nonzero, either applicable equation forces beta0
to be affine. For gamma zero, beta0 has degree at most three
if a1=0, and at most four in general. The same bounds hold
for beta. No claim makes these bounds sharp or asserts an
actual example attaining them.

## 5. Full F3 rank with zero reduced slopes

Suppose every F3 reduced slope is zero and dim W3 equals four.
Its residue map is then injective, since F3_R has rank four.
The whole N-action on all those residues is zero, so
\[
\boxed{\quad
N((F_3)_R)\subseteq\mathfrak n(F_3)_R,
\qquad \mathcal W_3=\mathcal D\oplus\mathbb C\epsilon c.
\quad}
\tag{5}
\]
To justify the exact second equality, choose a basis with
independent residues and subtract constant combinations of 1,G
so its remaining vectors have zero reduced values on both
components. They have double residues epsilon times polynomials.
For any such vector W, the preceding inclusion writes NW as
a sum of base-maximal-ideal coefficients times these basis
vectors. The basis vectors have constant reduced values on
the double. Hence the weight-two part of the right side only
uses those constants and the first base coefficients.

The retained invariant base parameters have leading forms x
and \((a_0+a_1c)x+b y^2\), with b a nonzero constant. Thus the
coefficient of y squared in that weight-two part is a complex
constant. On the other hand, the actual leading derivative of
epsilon beta(c) is \(\gamma\beta(c)x+\delta\beta'(c)y^2\).
Its y-squared coefficient makes beta prime constant. Every
nilpotent coefficient is therefore affine, in either normal
case. The residue space is contained in
\(\mathcal D+\mathbb C\epsilon c\), which has dimension four,
so full rank gives equality.

In particular the fourth residue direction is possible in this
argument. Epsilon itself is independent of 1,G; an affine
nilpotent coefficient does not reduce the residue dimension
to three. No such invalid dimension reduction is used.

## 6. Actual module splittings, not cubic algebra generation

Suppose now W2=D and dim W3 equals four. Choose an actual U
in F3 with residue outside D. The residues of D,U,c are
independent. If U has a nonzero reduced slope, it has one
on exactly one component, while c varies on both. If U has
zero reduced slopes, its nonconstant nilpotent coefficient
cannot be canceled by D and c. Thus in both cases
\[
\begin{gathered}
(F_3)_R=(F_2)_R\oplus RU,\qquad
(F_4)_R=(F_2)_R\oplus RU\oplus Rc,\\
Nc=aU+V_0,\qquad a\in\mathfrak n\setminus\{0\},
\quad V_0\in(F_2)_R,\\
\boxed{\quad N^4c=aN^3U.\quad}
\end{gathered}
\tag{6}
\]
Independence first gives bases by the ranks four and five and
Nakayama. Since Nc belongs to F3, it has the displayed unique
expression. Its whole residue lies in D by100. The U residue
is outside D, so a vanishes at m. Also c has generic N-degree
exactly four: it is admissible on both actual component lines,
and97 gives 3<deg c<=4. If a were zero, Nc would belong to
F2 and c would have degree at most three. Thus a is nonzero.
Applying N three times yields the boxed equality.

The actual finite generating set A=S[A1,A2,c] places A1,A2
in F2 and c in F4. This does not identify the module bases
in (6) with a power basis over R[U]. In particular Gc is only
known to be in F6. The no-finiteness conclusion in Section 2
rules out the attempted finite cubic parameter algebra, rather
than supplying it from these module splittings.

## 7. Order consequences of the full residue ranks

When W2=D,104 already gives N(F2_R) inside nF2_R. Since
N squared of U in (6) lies in F2 and vanishes on the whole
fiber, its injective reduction gives
\[
\begin{gathered}
N^3U\in\mathfrak m^2S,\qquad N^4c\in\mathfrak m^3S
\quad\text{in the setting of (6)}.\\
\text{If (5) holds, then}\quad
N^2((F_2)_R)\subseteq\mathfrak n^2,
\quad N^3((F_3)_R)\subseteq\mathfrak n^3,
\quad N^4c\in\mathfrak m^3S.
\end{gathered}
\tag{7}
\]
For the first line, N squared of U is in nF2_R, and applying
N once more puts its invariant third derivative in n squared;
use (6) for c. For the second line, iterate (5), and use
invariance of the indicated highest derivatives. N squared
of c belongs to F2 and has zero whole residue, so injectivity
of the full F3 fiber map puts it in nF3_R. Two further
iterations give its last membership.

Contraction of invariant memberships uses faithful flatness
and \(\mathfrak m^jS_m\cap S=\mathfrak m^j\), exactly as104.
Thus the second line applies even if W2 has dimension two,
provided the four-dimensional zero-slope F3 alternative is
present. The original-volume formula for F then also gives
N squared of F in m cubed, without claiming it vanishes.

## Scope

The new restrictions concern actual F3 residues, their common
one-component slope direction, full-rank module splittings and
the exact obstruction to a finite parameter of any degree.
No argument asserts existence of a nonconstant F3 residue,
excludes the mixed fiber, or recognizes A. The intrinsic mixed
family103 lacks the actual source-balance premise that yields
(2), so it is not a counterexample to this conditional theorem.
Its independent warning against a module-only hidden-parameter
argument remains valid.

The proof uses the retained actual normal chart99, full-fiber
action100, finite free modules102, any-function strict balance97
and residue theorem104. No new primary-source theorem, numerical
method, or actual-frame realization is claimed. All files
through104 remain unchanged.

The later [rank-defect theorem105](mixed-cubic-rank-defect-pass105.md)
uses the independent actual normalization boundary and an elementary
DVR slice lift to prove dim W3 at most three. Consequently the
full-rank alternatives in Sections 5--7 are now excluded in this
actual setting. Their conditional algebra remains correctly
stated and records why neither the affine-beta dimension argument
nor the module splitting alone supplied that exclusion. In
particular this forward result is not an input to (1)--(7).
