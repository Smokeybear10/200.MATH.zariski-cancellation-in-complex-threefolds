# Recognition of the full common-factor quartic configuration

**Status: synthesis of restricted working proofs. Unrestricted cancellation is not solved.**

The remaining branches for the supplied full initial relation
\(X^2Z+XYW-Y^4\) are excluded. The only surviving projected graph
has degree five, and the earlier construction gives an invariant
coordinate in the original polynomial ring. Consequently the
invariant ring is a polynomial three-ring under the hypotheses below.

Together with the coprime-pair exclusion185, this handles every
full weight-four initial relation that is linear in the two
quadratic-time variables with independent quadratic coefficients.
It does not handle all weight-four relations or supply an arbitrary
coordinate frame.

## 1. Exact conditional statement

Suppose
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad A=\ker E,\\
\deg_E(X,Y,Z,W)=(1,1,2,2),\\
a=EX,\quad b=EY,\quad e=E^2Z/2,\quad h=E^2W/2,\\
\theta_0:(\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
 \mapsto(a\tau,b\tau,e\tau^2,h\tau^2),\\
\ker\theta_0=(\mathsf X^2\mathsf Z+\mathsf X\mathsf Y\mathsf W-\mathsf Y^4).
\end{gathered}
\tag{1}
\]
The coordinates are actual polynomial coordinates, the slice is
global, and the ideal equality is the full initial-kernel hypothesis.
The working conclusion is
\[
\boxed{\text{There is an }I\in A\text{ with }
 B=\mathbb C[I]^{[3]},\qquad A=\mathbb C[I]^{[2]}.}
\tag{2}
\]
Neither one vanishing leading equation nor a height-two initial
kernel implies the hypotheses in (1). No minimum-degree or
arbitrary-entry assertion is being added.

## 2. The exhaustive branch argument

The [universal chart184](weight-four-universal-chart-potentials-pass184-working.md)
constructs the selected intrinsic derivation \(N\), its exact
coefficient field \(L\), and the whole generic line \(A_L=L[v]\).
Its determinant is obtained from the actual inverse.
For (1), the leading ratios satisfy
\(q=-t\rho+t^4\), with \(t,\rho\) algebraically independent.

The [whole-plane proof184](weight-four-bad-linear-whole-plane-projection-pass184-working.md)
and [selected-component proof184](weight-four-bad-linear-selected-component-pass184-working.md)
give
\[
\begin{gathered}
L[y,\vartheta]=L[v],\qquad
y\in L\quad\hbox{or}\quad y=\gamma v+\eta,\quad\gamma\in L^*,\\
\text{in the affine case }\vartheta=P(y),\quad \deg P\le5,
\quad G=V-P(U),\quad
\mathcal H=GQ,\quad Q(y,\vartheta)\in L^*,\\
\deg\mathcal H=5,\qquad\mathcal H_5=-U^5 .
\end{gathered}
\tag{3}
\]
The conclusion is a statement about the exact generic line, not yet
an original polynomial coordinate.

The new exclusions address every branch not recognized in185.

1. The [constant-projection proof186](weight-four-common-factor-constant-projection-exclusion-pass186-working.md)
   excludes \(y\in L\). It includes the extra \(t^4X^2\) term in
   the literal determinant. The resulting commuting original-ring
   derivation has kernel \(\mathbb C[X,Y,F]\), where
   \(F=(X+\mu)Z+(Y-\nu)W\). Wang's two-coordinate theorem gives
   either a forbidden invariant linear form or an invariant
   \(cF+Q(X,Y)\). The latter would require
   \(ct^4+Q_3(1,t)=0\), impossible for transcendental \(t\).
   This branch proof does not use whole-plane completion or
   the unit selected cofactor.
2. The [low-graph proof186](weight-four-common-factor-low-graph-exclusion-pass186-working.md)
   excludes constant and linear \(P\). Its graph's leading form
   \(V-p_1U\) cannot divide \(-U^5\). This also covers the zero
   polynomial, and does not require the stronger cofactor assertion.
3. The [quadratic-graph proof186](weight-four-common-factor-quadratic-graph-exclusion-pass186-working.md)
   excludes \(\deg P=2\). The evaluated unit cofactor, literal
   coefficient comparisons and actual constant translations force
   a nonzero complex \(\lambda\). The second potential then has
   coefficient \(-\lambda^3/4\) at \(\rho^2y\), contrary to its
   independence of \(y\). Transcendence over the exact constant
   field justifies the coefficient comparison; that field is not
   assumed rational.

Thus only the affine branch with \(\deg P\ge3\) remains. The
[high-graph proof185](weight-four-common-factor-high-graph-recognition-pass185-working.md)
forces degree five, derives its own actual translation normalization,
and constructs the invariant coordinate. Degrees three and four
do not constitute unexamined branches.

## 3. The original-ring endpoint

In the normalized actual frame of that surviving branch, the
construction produces complex coefficients and \(d\in\mathbb C^*\)
such that
\[
\begin{gathered}
I=dW-(X^2Z+XYW-Y^4)+K_3(X,Y)+N_2(X,Y)-\ell_1Y-\ell_0X\in A,\\
P_0=Y^4+K_3+N_2-\ell_1Y-\ell_0X,\qquad
J=(d+XY)Z+Y^2W,\\
Z=\frac{(d-XY)J-Y^2(I-P_0)}{d^2},\qquad
W=\frac{(d+XY)(I-P_0)+X^2J}{d^2}.
\end{gathered}
\tag{4}
\]
Here \(K_3,N_2\) are complex-coefficient homogeneous polynomials
of the indicated degrees. Both inverse orders hold in the original
polynomial ring, so \(B=\mathbb C[X,Y,I,J]\).
There is no inversion of an original variable or nonconstant
coefficient in (4). Undoing the actual translations preserves the
existence of this invariant coordinate.

The global slice makes \(A\) regular: \(B=A[u]\) is regular,
and regularity descends along this faithfully flat polynomial
extension. The nonzero \(E\) is now a \(\mathbb C[I]\)-linear LND
on \(\mathbb C[I]^{[3]}\). The published
[Bhatwadekar--Gupta--Lokhande Theorem 3.5](https://arxiv.org/html/1501.01438v1)
gives \(A=\mathbb C[I]^{[2]}\), proving the conditional conclusion (2).
The [normalized endpoint185](weight-four-normalized-common-factor-recognition-pass185-working.md)
records the construction and its precise hypotheses separately.

## 4. Consequence for independent bad-variable coefficients

Suppose instead that the full irreducible weight-four initial
generator in an actual exact1122 frame is
\[
F=P_2(X,Y)Z+Q_2(X,Y)W+H_4(X,Y),\qquad
\dim_{\mathbb C}\langle P_2,Q_2\rangle=2.
\tag{5}
\]
The [actual normal forms184](weight-four-zero-bad-rank-normal-forms-pass184-working.md)
give exactly two possibilities. If \(P_2,Q_2\) are coprime,
the form becomes \(X^2Z+Y^2W\), excluded by
[the complete coprime argument185](weight-four-frontier-synthesis-pass185-working.md).
Otherwise their common factor is linear, and the form becomes (1).
The latter now has the conclusion (2).

These changes are genuine homogeneous polynomial automorphisms.
Each new slot keeps exact time degree one or two: a degree drop
would put its nonzero weight-one or weight-two initial polynomial
in the principal weight-four kernel, which is impossible.
Thus (5) implies the working recognition conclusion, rather than
merely a formal normal-form reduction.

## 5. Verification and what is still unresolved

The proofs have separate saved-source AI reconstructions and bounded
symbolic controls. These support specific written identities and
their review, not human expert certification or a proof-assistant
check of every universal argument and retained dependency.
The constant-projection exclusion also retains Wang's classification
as stated in [Dasgupta--Gupta Theorem 4.1](https://arxiv.org/pdf/1701.03635v1).
Neither external theorem is being represented as newly proved here.

The one-dimensional bad-coefficient span, positive quadratic
bad-variable rank, height-two initial kernels, higher possible
minimum time profiles, and arbitrary coordinate entry are not settled.
The full corrected question \(A[u]\simeq\mathbb C^{[4]}\Rightarrow
A\simeq\mathbb C^{[3]}\) remains unsolved, and the professor has
not confirmed that field-and-dimension interpretation of the email.

The next bounded investigation is the remaining one-dimensional
coefficient-span quartics, keeping their absent-variable and lower
derivation-shift cases separate. The ultimate objective is unchanged.
No historical novelty clearance, expert review, public claim,
submission, external contact or new automation is asserted.
