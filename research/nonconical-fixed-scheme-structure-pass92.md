# The exact primitive field has a Cohen--Macaulay fixed curve

If the global primitive Jacobian field from pass91 has fixed points,
its fixed scheme is pure one-dimensional and Cohen--Macaulay. In
particular there are no isolated or embedded point components. Each
reduced component is an entire component of an exceptional quotient
fiber, and that fiber is generically nonreduced along it. These
conclusions do not exclude the fixed curve or bound its thickness.

## 1. The actual field and its local Jacobian ideal

Retain the actual original nonconical constant-acceleration frame of
[global-Jacobian91](nonconical-global-jacobian-field-pass91.md). In
particular,
\[
\begin{gathered}
B=A[u]=\mathbb C[x_1,x_2,x_3,z],\qquad E=\partial_u,\\
S=\mathbb C[s_1,s_2]\subset A,\qquad
N(f)=\det\frac{\partial(s_1,s_2,u,f)}
 {\partial(x_1,x_2,x_3,z)},\\
Nu=0,\quad [E,N]=0,\quad
0\ne N|_A\in\operatorname{LND}(A),\quad\ker(N|_A)=S,\\
I=N(A)A,\qquad \mathcal Z=\operatorname{Spec}(A/I).
\end{gathered}
\tag{1}
\]
The ring A is a smooth affine complex threefold and a UFD. The
restriction of N to A is primitive: no height-one prime of A contains
I. Its fixed set maps to finitely many closed points of
\(\operatorname{Spec}S\), all in \(V(\Omega)\). The inclusion
\(S\subset A\) is faithfully flat with nonempty purely
one-dimensional fibers. These are the precise actual-ring conclusions
of the linked proof, not hypotheses deduced from an arbitrary
polynomial vector field.

Fix a closed point \(x\in\mathcal Z\) and write \(R=A_x\).
Choose local functions \(y_1,y_2,y_3\) whose differentials form a
basis of \(\Omega_{R/\mathbb C}\). Such functions exist because A
is smooth and the residue field at x is \(\mathbb C\). Write
\[
\begin{gathered}
ds_1=\sum_i r_i\,dy_i,\qquad
ds_2=\sum_i t_i\,dy_i,\qquad r,t\in R^3,\\
c=r\times t,\qquad
IR=(c_1,c_2,c_3)R.
\end{gathered}
\tag{2}
\]
Here is the unit-factor gate in (2). Localize to \(R[u]\), and
reduce the rank-four cotangent module modulo u. This module is
\(\Omega_{R/\mathbb C}\oplus R\,du\); in particular du is
retained. The original volume generator reduces to a unit multiple
of \(dy_1\wedge dy_2\wedge dy_3\wedge du\).
This is coefficient evaluation, not pullback of a four-form to the
three-dimensional slice, which would discard du.
For \(f\in A\), the determinant in (1), evaluated at \(u=0\),
therefore equals a common unit times the three-dimensional Jacobian
of \(s_1,s_2,f\) in the y basis, with a sign depending only on
orientation. Since \(Nf\in A\), this is already its actual value.
The values on the \(y_i\) generate the localized value ideal,
because every differential in \(\Omega_{R/\mathbb C}\) is an
R-linear combination of the \(dy_i\). This proves (2); no
ambient coordinate status is assigned to the local y functions.

The rows r and t are independent over \(\operatorname{Frac}R\),
since \(s_1,s_2\) are algebraically independent in characteristic
zero. Primitivity in (1) says that at every height-one prime of R
at least one entry of c is a unit after localization.

## 2. An explicit resolution, without a determinantal height shortcut

Consider a vector \(w\in R^3\) with \(c\cdot w=0\).
Over the fraction field, the kernel of this nonzero row is the
span of r and t. Thus there are unique rational coefficients
\(\alpha,\beta\) with \(w=\alpha r+\beta t\).
At a height-one prime, choose the unit two-by-two minor furnished
by (2). Cramer's rule using its two coordinates puts
\(\alpha,\beta\) in that localization. The local UFD R is the
intersection of its height-one localizations inside its fraction
field: any nonunit reduced denominator has an irreducible prime
factor. Hence \(\alpha,\beta\in R\).

This proves every syzygy, including those not visible after choosing
a single nonunit minor. With r,t regarded as columns, it gives the
exact sequence
\[
0\longrightarrow R^2
 \xrightarrow{\ [r\ t]\ }R^3
 \xrightarrow{\ c\cdot\ }R
 \longrightarrow R/IR\longrightarrow0.
\tag{3}
\]
Injectivity on the left follows from fraction-field independence.
The middle image is the ideal in (2). Thus (3) is proved in the
actual local ring, not inferred from a rank computation over its
fraction field. It is the specific two-row determinantal resolution
needed here; no unverified general Hilbert--Burch theorem is imported.

The regular local ring R has dimension and depth three.
Apply the depth lemma to the two short exact sequences obtained
from (3). First \(\operatorname{depth}(IR)\ge2\), and then
\(\operatorname{depth}(R/IR)\ge1\). The absence of height-one
primes containing I bounds its support dimension at x by one.
Depth cannot exceed support dimension, so both are exactly one.[^depth]
This works at every closed point of the fixed scheme. At its
nonclosed generic points the local rings are zero-dimensional and
therefore Cohen--Macaulay. Consequently, if \(I\ne A\),
\[
\boxed{\quad
\mathcal Z\text{ is a pure one-dimensional Cohen--Macaulay scheme};
\quad \operatorname{Ass}_A(A/I)\text{ consists only of height-two primes}.
\quad}
\tag{4}
\]
Indeed an isolated point or an embedded closed associated point
would give depth zero at that point, contradicting the calculation.
No reduction of I was taken. The conclusion permits nonreduced
curve components.

## 3. A local Hamiltonian form where the quotient differential has rank one

At a fixed point the two quotient differentials have rank at most
one. Suppose this rank is one. After an invertible constant change
of the two base coordinates, take \(y_1=s_1-s_1(x)\), and extend
it to a local differential basis \(dy_1,dy_2,dy_3\).
Put \(f=s_2-s_2(x)\in R\), and let \(f_i\) denote its
coefficients in this basis. Formula (2) becomes
\[
IR=(f_2,f_3)R,\qquad
N|_R=\epsilon\bigl(f_3\partial_{y_2}-f_2\partial_{y_3}\bigr),
\qquad \epsilon\in R^* .
\tag{5}
\]
The partials mean the R-dual derivations to the specified differential
basis. They are not derivatives in an assumed global polynomial
presentation. The unit may absorb the orientation sign.
Since the ideal has height two in the regular local ring, its two
generators form a regular sequence. Thus the fixed curve is locally
a complete intersection on this rank-one stratum. Formula (5)
does not assert that the unit multiple is locally nilpotent on a
completion, that f is a polynomial coordinate, or that rank one
holds at every fixed point.

## 4. Entire fiber components and unavoidable generic nilpotents

By pass91, every irreducible fixed component maps to one closed
point m of the invariant plane. Its dimension is one by (4), so
it is an entire irreducible component of the purely one-dimensional
fiber over m, rather than an isolated subset of that component.

Let \(\mathfrak q\subset A\) be its height-two generic prime.
The faithful-flat base parameters form a regular sequence in
\(A_{\mathfrak q}\). The whole generic scheme of this fiber
is the nonzero Artinian complete intersection
\[
T=A_{\mathfrak q}/mA_{\mathfrak q},\qquad
\mu=\operatorname{length}_{A_{\mathfrak q}}T\ge2.
\tag{6}
\]
To justify the inequality, if \(\mu=1\) then T would be its
residue field. Since \(I\subset\mathfrak q\), the induced N
would vanish on T. The precise primitive-fiber theorem54 instead
proves nonzero action at the generic scheme of each component,
using the transverse complete-intersection socle. This gives a
contradiction.[^fiber]

The conclusion concerns the whole scheme fiber, not just its reduced
curve. It also does not make \(\mathcal Z\) a scheme-theoretic
subscheme of a reduced base fiber: functions in m may remain
nilpotent on the fixed scheme.

## 5. Degree two or three does not bound fixed-scheme thickness

The following polynomial control isolates that distinction. For any
\(m\ge1\) and \(e\in\{2,3\}\), set
\[
\begin{gathered}
A_0=\mathbb C[p,y,z],\qquad
S_0=\mathbb C[p,\eta],\qquad \eta=p^m z-y^e,\\
D_0=p^m\partial_y+e y^{e-1}\partial_z,\qquad
\ker D_0=S_0,\qquad I_0=(p^m,y^{e-1})A_0,\\
A_0=S_0[y,z]=S_0[Y,Z]/(p^mZ-Y^e-\eta).
\end{gathered}
\tag{7}
\]
This is the retained triangular plinth family, not a new action
construction. Directly, \(D_0\eta=0\), the coefficient gcd is
one, and local nilpotence follows from the triangular form.
After inverting p the kernel is \((S_0)_p\); contraction to
\(S_0\) follows from the injective substitution
\(\mathbb C[\eta]\to\mathbb C[y,z]\), \(\eta\mapsto-y^e\),
and repeated cancellation of powers of p.

The quotient has nonempty pure curve fibers and is faithfully flat,
by the same smooth-source and regular-base argument as the retained
Weitzenbock family. The origin fiber and the generic p-divisor fiber
are respectively \(\mathbb C[y,z]/(y^e)\) and
\(\mathbb C(\eta)[y]/(y^e+\eta)[z]\). The latter constant
extension has degree e: \(Y^e+\eta\) is Eisenstein at \(\eta\)
over \(\mathbb C[\eta]\). At the generic prime \((p,y)\),
using the coefficient field \(\mathbb C(z)\), the lengths are
\[
\operatorname{length}(A_{0,(p,y)}/(p,\eta))=e,
\qquad
\operatorname{length}(A_{0,(p,y)}/I_0)=m(e-1).
\tag{8}
\]
The monomial bases of the two quotients prove these equalities.
Thus the generic fiber multiplicity stays two or three while the
fixed-scheme thickness is unbounded. For \(m>1\), p itself is
nonzero nilpotent modulo \(I_0\), exhibiting the base-direction
warning after (6).

The total space \(A_0\) and its polynomial cylinder are polynomial.
The relative equation has degree e and the primitive action has a
single closed-base fixed support. None of this identifies the chosen
field, plane, or relative generators with the special original
nonconical highest-adjoint construction. Accordingly (7)--(8) do not
provide an actual-frame counterexample or rule out recognition by
another action.

## 6. Source and bridge limits

The principal-plinth and boundary-field results of passes27,33,36
and56 were reread for deduplication. Masuda's selected primary
Theorem 3.8 constructs a modification presentation after inverting
an element outside a chosen base prime. That element is not
guaranteed nonzero at one of the finitely supported fixed base
points. Theorem 3.9 and Corollary 3.10 give generic boundary and
additional derivative-unit criteria; they do not remove that
localization at those points.[^masuda] The direct argument (2)--(5)
therefore works on the actual local rings instead.

This proof still requires the exact N supplied by the special frame.
It constructs neither that frame nor an intrinsic nonzero LND of
the kernel of an arbitrary sliced action. The fresh check of the
quasi-nice source definitions and selected hypotheses does not supply
such a bridge: existence of suitable coordinates is part of its
definition, and the stated image-ideal theorems retain a polynomial
two-variable presentation over a specified base.[^quasi]

Geometry supplied the local resolution and depth argument. Root
supplied the whole-fiber-component consequence and the unbounded
thickness comparison. All calculations above are written algebra;
no numerical method, general cancellation claim, or edit to pass91
and earlier files is made.

[^depth]: The Stacks Project, [Lemma 10.72.6, 00LX](https://stacks.math.columbia.edu/tag/00LX),
    [Lemma 10.72.3, 00LK](https://stacks.math.columbia.edu/tag/00LK),
    and [Lemma 10.106.3, 00NQ](https://stacks.math.columbia.edu/tag/00NQ).
    The complete displayed statements and proofs were freshly read.
    They give the depth inequalities, depth bounded by support
    dimension, and regular local rings being Cohen--Macaulay.
    Their deeper Ext, dimension and regular-local dependencies were
    not all freshly re-audited. The exact resolution (3) is proved here.

[^fiber]: [Primitive-fiber54](primitive-fiber-nonvanishing-pass54.md),
    Sections 1--5, including the local generic-component nonvanishing
    argument, were reread completely. The source-socle proof cited
    there was not freshly re-audited in this pass. Its nilpotent
    whole-scheme conclusion is used exactly, not replaced by a
    statement about the reduction.

[^masuda]: Kayo Masuda,
    [*Factorial affine Ga-varieties with principal plinth ideals*, v1](https://arxiv.org/html/2312.05455v1),
    Section 3 hypotheses, complete displayed Theorem 3.9 and
    Corollary 3.10 statements/proofs, and the adjacent Theorem 3.8
    statement and formulas (15)--(17) were freshly read. The long
    preceding construction proving Theorem 3.8 was not freshly
    reconstructed in full. No claim to classify the exceptional
    closed-point germs is extracted from its generic localization.

[^quasi]: Dasgupta--Lahiri,
    [*On image ideals of nice and quasi-nice derivations on R[X1,X2]*, v6](https://arxiv.org/html/2302.13787v6),
    Definitions 2.2--2.3 and the exact hypotheses of Theorems 5.2
    and 5.9 were freshly checked against the retained source85/90
    notes. Their earlier proof reads are not claimed as new pass92
    reads. No absence of a search match is used as evidence of
    impossibility or historical novelty.
