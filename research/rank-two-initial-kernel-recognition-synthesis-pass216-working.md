# Recognition for a supplied rank-two initial-kernel frame

Status: working restricted recognition theorem. The normalized linear-center
exclusion216 closes the last nonconstant second-projection case of the
supplied rank-two frame. The original-ring conclusion comes from the retained
zero-return and constant-second recognition theorems, not from a coordinate
over a coefficient field. A final corollary combines this result with the
radical theorem211 and the actual normal forms206.

Neither statement supplies a frame for an arbitrary cancellation instance.
The unrestricted complex-threefold cancellation problem remains unsolved.

## 1. The actual frame and the conclusion

Let the four named elements be polynomial coordinates, with
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\\
\deg_E(X,Y,Z,W)=(1,1,2,2),\\
a=EX,\quad b=EY,\quad e_0=E^2Z/2,\quad h_0=E^2W/2.
\end{gathered}
\tag{1}
\]
Here the degrees are degrees in the actual slice variable, not ordinary
degrees of the polynomial coefficients of the derivation. For an independent
indeterminate \(s\), assume the entire initial evaluation kernel is
\[
\begin{gathered}
\theta_0:\mathbb C[\mathsf X,\mathsf Y,\mathsf Z,\mathsf W]
\longrightarrow A[s],\\
(\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
\longmapsto(as,bs,e_0s^2,h_0s^2),\qquad
\ker\theta_0=(\mathsf Z\mathsf W-\mathsf X^4).
\end{gathered}
\tag{2}
\]
The source weights are \((1,1,2,2)\). Merely assuming the scalar
identity \(e_0h_0=a^4\) does not replace the full-kernel condition (2).
No minimality of the frame or unit-speed hypothesis is imposed.

**Working theorem.** Under (1)--(2), the original action fixes an ambient
polynomial coordinate, and
\[
\boxed{A\simeq\mathbb C^{[3]}.}
\tag{3}
\]
In fact (2) forces the speed \(a\) of this particular coordinate to be
nonunit. If \(a\) were a unit, it would be complex; the product
\(e_0h_0=a^4\) would then make both factors complex units, giving a
nonzero weight-two initial relation. This contradicts (2). Thus (3)
is not obtained by assuming that the supplied \(X\) is a global slice.

## 2. The chart is derived from the original ring

Use the literal original pivot \(\partial_Z\). The actual construction in
[universal184](weight-four-universal-chart-potentials-pass184-working.md),
as specialized in
[sextic reduction212](rank-two-t-independent-sextic-reduction-pass212-working.md),
gives
\[
\begin{gathered}
N=[u^3](\partial_Z|_A)\ne0,\qquad L=\operatorname{Frac}\ker_A N,
\qquad A_L=L[v],\qquad Nv=1,\\
t=b/a,\qquad \rho=h_0/a^2,\qquad q=e_0/a^2=1/\rho,
\qquad [L:\mathbb C(t,\rho)]<\infty,\\
Y=y+tX,\quad W=w+\vartheta X+\rho X^2,\quad
Z=z+\sigma X+\rho^{-1}X^2,\\
L[y,z,w]=L[v],\qquad \mathbb C(y,z,w)=L(v),\qquad J_0=-a^3\in L^*.
\end{gathered}
\tag{4}
\]
Here \(A_L\) is the localization by the nonzero elements of \(\ker_A N\).
The ratios \(t,\rho\) are algebraically independent. Their partials
extend uniquely to the finite separable field \(L\), commute, and have
joint constants \(\mathbb C\). No rationality of \(L\) is assumed.
All displayed projected entries lie in \(L[v]\).

The universal potentials supply \(k,n,\ell,m\in L\). In particular
\(\sigma=-\rho^{-2}\vartheta+k\), and the evaluated return coefficient is
\(R=2\rho^{-3}\vartheta+k_\rho\). Since
\(q_t=0\) and \(q_{\rho\rho}=2\rho^{-3}\ne0\), the hypotheses of
[zero-return recognition205](weight-four-t-independent-zero-r-recognition-pass205-working.md)
apply whenever \(R=0\). If \(\vartheta\in L\),
[constant-second recognition210](weight-four-constant-second-projection-recognition-pass210-working.md)
applies, including its retained zero-return case.

It remains to exclude \(\vartheta\notin L\). In that case \(R\ne0\)
automatically, because its coefficient of \(\vartheta\) is a nonzero
element of \(L\). This does not make \(R\) a unit of \(L[v]\).

## 3. Exhausting the center polynomials and degree pairs

For the remaining branch,212 constructs the nonzero sextic eliminant
\(\mathcal H\), its selected irreducible plane factor \(G\), and a
cofactor \(Q_1\), with
\[
\begin{gathered}
\mathcal H=GQ_1,\quad \mathcal H_6=-\rho^{-11}V^6,\quad
0\ne Q_1(y,\vartheta)\mid R^3\text{ in }L[v],\\
C=L[y,\vartheta]\subset O=L[v],\quad
\operatorname{Frac}C=L(v),\quad O=C+Cw,\quad RO\subset C,\\
V_c=-\rho^3k_\rho/2,\qquad
p(U)=S(U,V_c)-\ell,\qquad \deg p\le2,\qquad
\mathcal H(U,V_c)=\rho^{-3}p(U)^2,\\
d:=\deg_vy=\deg G>e:=\deg_v\vartheta=\deg_U G\ge1,
\qquad d\le6,\quad e\le4.
\end{gathered}
\tag{5}
\]
The polynomial \(S\) here is the third-potential coefficient polynomial
specified completely in212. Its coefficient derivatives are taken before
evaluation. The cofactor and conductor statements in (5) use the actual
nonzero calibrated determinant and the full potential identities.
Neither normality of \(C\) nor a formal parametrization is substituted
for those hypotheses.

The center analysis in212 is exhaustive for polynomials of degree at most
two. A nonzero constant center forces \(R\) to be a unit. If the center
is zero, the divided third potential and calibrated determinant again
force \(R\) to be a unit. Both contradict nonconstant \(\vartheta\).
A repeated quadratic center is excluded by the vertex-free cone argument,
its resulting whole-plane equality, and the cubic/quadratic degree
contradiction. The cone lemma used there has \(\deg R\le4\) and does not
assume an unproved bound on the other cone coordinate.

Consequently \(p\) is nonconstant and squarefree. The monic fiber and
conductor arguments in
[degree pruning213](rank-two-squarefree-center-degree-pruning-pass213-working.md)
leave exactly
\[
\begin{aligned}
\deg p=1:&\quad (d,e)=(2,1),(3,1),(4,1),(3,2),(4,2),(6,2),\\
\deg p=2:&\quad (d,e)=(2,1),(3,2),(6,4).
\end{aligned}
\tag{6}
\]
In particular this list does not assume that the center fiber is reduced
or that \(C=O\). Each remaining pair has the following disposition.

| Center degree | Projected degrees \((d,e)\) | Complete retained argument |
| --- | --- | --- |
| 1 | \((3,2),(4,2),(6,2)\) | [Linear-center quadratic-projection exclusion214](rank-two-linear-center-quadratic-projection-exclusion-pass214-working.md), using the exact ring description in [linear-center213](rank-two-linear-center-quadratic-projection-pass213-working.md). |
| 1 | \((3,1),(4,1)\) | [Affine-second high-degree exclusion214](rank-two-affine-second-high-degree-exclusion-pass214-working.md). |
| 2 | \((6,4)\) | [Quadratic-center six-four exclusion214](rank-two-quadratic-center-six-four-exclusion-pass214-working.md). |
| 2 | \((2,1)\) | [Quadratic-center affine-second exclusion215](rank-two-quadratic-center-affine-second-exclusion-pass215-working.md). |
| 2 | \((3,2)\) | [Quadratic-center cubic-quadratic exclusion215](rank-two-quadratic-center-cubic-quadratic-exclusion-pass215-working.md). |
| 1 | \((2,1)\) | [Actual affine reduction215](rank-two-linear-center-affine-reduction-pass215-working.md), followed by [normalized Wang exclusion216](rank-two-normalized-linear-center-wang-exclusion-pass216-working.md). |

The three214 arguments retain the required finite-field hypotheses in
their norm/residue steps. The six-four proof obtains the squared weighted
initial form from the monic characteristic polynomial and its four formal
branches, not from an unjustified polynomial-cancellation estimate.
The two quadratic-center215 exclusions use respectively the exact evaluated
cofactor degree and the exact center-fiber comparison. Thus all five rows
before the final row are exclusions under (1)--(2), not conditional
realization claims or generic coefficient normalizations.

## 4. Why the final row is an original-frame contradiction

The remaining linear pair \((2,1)\) satisfies the hypotheses of215.
Its local cofactor order and calibrated scalar identity first yield a
finite-field differential equation. Its proved complex-coefficient
\(W\)- and \(Z\)-shears then give
\[
\begin{gathered}
k_t=-c/\rho,\quad n_{tt}=0,\quad c\in\mathbb C^*,\quad
\deg_v\vartheta=1,\\
y=\frac{\vartheta^2}{c\rho^2}+p_1\vartheta+p_0,\qquad
w=\lambda\vartheta+\omega,\qquad
z=\kappa\vartheta+\zeta,
\end{gathered}
\tag{7}
\]
with coefficients in the exact \(L\). Those actual shears preserve
the full initial kernel, exact degrees, literal \(\partial_Z\), selected
\(N\), and coefficient field. Equation (7) does not presume that any
nonconstant coefficient in \(L\) belongs to the original polynomial ring.

The complete216 endpoint starts from precisely (7). The actual LND
\(\mathcal P=aN-(NX)E\) fixes \(X\) and has coordinate degrees
\((0,2,1,1)\). After primitive division, Wang's theorem over
\(\mathbb C(X)\) applies to the good pair \(Z,W\). Their derivative
ratio is genuinely transcendental over that field, so the first alternative
is impossible and the second yields an invariant of the form
\(Y+Q(Z,W)\) with ordinary degree \(\deg Q=2\).

The resulting exact quadratic identity, combined with lower coefficients
of both full potentials, forces
\(\lambda\in\mathbb C\) and \(\kappa=-\rho^{-2}\lambda\).
The Laurent comparison retains all three coefficient modes and eliminates
the two extreme modes with the complete identity, not just its leading
terms. The proof never needs a global slice for the primitive
auxiliary derivation or a lift of Wang's coefficient-field coordinate.

The final map is the actual translation \(X_*=X+\lambda\), fixing
\(Y,Z,W\), with inverse \(X=X_*-\lambda\). It leaves the full initial
kernel, literal selected partial, \(N,L,t,\rho\), and exact degrees unchanged.
Its new intercepts satisfy
\[
\begin{gathered}
\vartheta_* =\vartheta-2\rho\lambda,\qquad y_*=y-\lambda t,\\
w_* =\omega+\rho\lambda^2\in L,\qquad
z_* =\zeta-\lambda k+\rho^{-1}\lambda^2\in L,\qquad
\deg_vy_*=2,\\
L[X_*,Y,Z,W]=L[v][X_*]
\quad\Longrightarrow\quad L[y_*,z_*,w_*]=L[v].
\end{gathered}
\tag{8}
\]
The last implication is quotienting the equality of actual localized rings
by \(X_*\). It is valid because \(a\in L^*\) makes \(X_*\) an affine
slice variable over \(L[v]\). But its left-hand projected ring is
\(L[y_*]\), which cannot contain \(v\) when \(\deg_vy_*=2\).
This excludes the final row of the table, including \(\lambda=0\).

## 5. Completing the rank-two recognition theorem

Every nonconstant-second branch of (4) has now been excluded. The remaining
possibilities are exactly the zero-return or constant-second cases already
recognized in Section2. Those proofs construct an actual nice commuting
LND with E-invariant original coefficients and apply the
[original-ring criterion205](nice-commuting-invariant-coefficients-recognition-pass205-working.md).
That criterion checks primitive division, a complex linear fixed direction,
the polynomial auxiliary kernel and slice, and the precise three-variable
endpoint before concluding that \(E\) fixes an ambient coordinate.

The final regular-kernel implication is
[Bhatwadekar--Gupta--Lokhande Theorem3.5](https://arxiv.org/html/1501.01438v1).
Its regularity hypothesis holds here: \(A\simeq B/(u)\), and \(Eu=1\)
makes this hypersurface smooth. Applied over the polynomial ring generated
by the actual invariant coordinate, the theorem gives (3).
The auxiliary nice-derivation and three-variable results used in205, and
Wang's alternatives used in216, are checked against the precise statements
in [Dasgupta--Gupta](https://arxiv.org/html/1701.03635v1).
This is reliance on the authors' Wang restatement, not a claim to have read
Wang's original paper.

## 6. Corollary for every supplied full quartic kernel independent of Y

Keep (1), but replace (2) by
\[
\ker\theta_0=(F),\qquad
F\text{ irreducible weighted homogeneous of weight four},\qquad
F_{\mathsf Y}=0.
\tag{9}
\]
Then the same conclusion (3) holds, and \(E\) fixes an ambient coordinate.
This corollary concerns independence of this supplied linear slot, not the
existence of some coordinate system in which the condition holds.

Indeed, the fully read
[classification206](weight-four-t-independent-leading-kernel-classification-pass206-working.md)
uses actual invertible complex linear changes of \(Z,W\), followed by
additions of complex multiples of \(X^2\), to put the entire equation
into one of
\[
\mathsf Z^2-\mathsf X^2\mathsf W,\qquad
\mathsf Z\mathsf W-\mathsf X^4.
\tag{10}
\]
For completeness, independence of \(\mathsf Y\) writes the equation as
\(Q_2(\mathsf Z,\mathsf W)+\mathsf X^2L_1(\mathsf Z,\mathsf W)
+c\mathsf X^4\). Irreducibility excludes \(Q_2=0\). A rank-one
quadratic form is reduced by completing the square; a rank-two form is
reduced by completing the product. In each case irreducibility ensures
that the remaining coefficient used in the inverse is nonzero, giving
exactly (10). The explicit forward and inverse maps are recorded in206.

These are actual weighted polynomial automorphisms. Every new bad-coordinate
leading form is a nonzero weight-two polynomial. It cannot vanish under
\(\theta_0\), since the full ideal (9) contains no such polynomial.
Thus both transformed bad coordinates still have E-degree exactly two,
and the unchanged good coordinates have degree one. The weighted
automorphism transports the full initial ideal, not just a chosen relation.

For the second normal form apply the rank-two theorem proved above.
For the first, an actual interchange of \(Z,W\) gives the radical kernel
\((\mathsf X^2\mathsf Z-\mathsf W^2)\), up to a nonzero scalar.
The [complete radical recognition211](radical-initial-kernel-recognition-synthesis-pass211-working.md)
then applies.

These changes need not preserve the old pivot, selected derivation,
coefficient field, or zero/nonzero status of its return coefficient.
A fresh selected chart is built from each transformed actual frame before
applying its complete recognition theorem. No old chart branch is carried
through a change merely because the coordinate map is polynomial.

The same corollary applies if \(F\) depends on the good variables only
through one nonzero complex linear combination of \(\mathsf X,\mathsf Y\).
Take that combination as the new first good coordinate and choose a
constant linear complement. This actual \(\mathrm{GL}_2(\mathbb C)\)
change cannot lower either good degree: a vanishing new leading form
would be a nonzero weight-one member of the full ideal \((F)\).
It therefore reduces this condition to (9), after which the same
normalization and fresh-chart argument applies.

## 7. Verification and the remaining scope boundary

All retained recognition, center, degree-pruning and exclusion sources used
above were fully reread before this composition. The complete saved216
endpoint,206 normal-form proof and211 radical synthesis were read through
EOF. This note is a written synthesis, not a replacement for those proofs
and not a claim that finite checks prove field descent or the published
theorems. No saved checker was executed, imported or compiled during its
authorship; no earlier source, index or packet was changed.

The theorem and corollary assume a supplied actual global slice, exact time
profile \((1,1,2,2)\), and an entire principal irreducible weight-four
initial ideal of the stated kind. They do not establish arbitrary entry,
address all kernels with genuine dependence on both good directions, or recognize
every height-two initial ideal or higher time profile. No global-minimum,
historical-novelty, formal-certification or human-expert-review claim is made.
The unrestricted cancellation goal remains open.
