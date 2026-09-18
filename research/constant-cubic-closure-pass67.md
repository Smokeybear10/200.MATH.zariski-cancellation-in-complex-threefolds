# Cancellation under a constant third flow derivative

The supplied two-quadratic coordinate frame is now recognized whenever
the third flow derivative of its coordinate vector is constant. This
includes the already recognized flow-degree-at-most-two sector and
both newly closed constant-top cubic sectors. The proof does not
cover a nonconstant cubic top or establish a frame for every sliced
action.

## 1. Precise conditional theorem

Let
\[
B=\mathbb C[x_1,x_2,x_3,x_4],\qquad
E\in\operatorname{LND}_{\mathbb C}(B),\qquad E(s_*)=1,
\qquad A=\ker E.
\]
The displayed generators must be actual polynomial coordinates.
Let \(T_i=\partial_{x_i}\). Assume
\[
\operatorname{ad}_E^2T_1=\operatorname{ad}_E^2T_2=0,
\qquad
\operatorname{ad}_E^3T_3=\operatorname{ad}_E^3T_4=0,
\qquad E^3x\in\mathbb C^4.
\tag{1}
\]
Then the working proof chain gives
\[
\boxed{A\simeq\mathbb C^{[3]}.}
\tag{2}
\]

Here \(x=(x_1,x_2,x_3,x_4)^t\), and the last condition allows
the zero vector. It implies \(E^4x=0\), but its converse is not
assumed. Flow degree is degree in the additive-action parameter,
not spatial degree of a polynomial coefficient. This distinction
is essential to the remaining cubic problem.

This is a written conditional theorem with independent AI proof
reconstructions and separately stated source dependencies. It is
not a proof-assistant certificate, a human-reviewed theorem, a
historical novelty claim, or a solution of general cancellation.

## 2. Exhaustion of the hypotheses

Put \(V_i=\operatorname{ad}_E^2T_i\), \(i=3,4\), and measure
their rank over \(\operatorname{Frac}B\).

| Actual alternative | Recognition argument |
| --- | --- |
| A nonzero complex constant relation between \(V_3,V_4\), including rank zero | A genuine constant coordinate recombination gives a third good partial. The inherited mixed-height-nine theorem applies. |
| \(E^3x=0\), with either defect rank | The complete [low-flow theorem](low-flow-closure-pass66.md), including its full five-dimensional rank cap. |
| \(E^3x=c\ne0\), defects dependent but with no complex constant relation | The new [dependent cubic closure](dependent-constant-cubic-closure-pass67.md), after the complete frozen dependent reduction. |
| \(E^3x=c\ne0\), defects independent | The new [actual graph closure](independent-cubic-graph-closure-pass67.md), after the complete frozen independent normal form and its already recognized endpoints. |

These alternatives exhaust (1). A relation with nonconstant
rational coefficients does not count as a constant coordinate
recombination. The rank-one case is handled separately for precisely
that reason.

## 3. Independent defects: an explicit coordinate slice

The retained independent cubic normal form supplies actual
polynomials \(t,f\), with \(Et=0\), \(Ef=1\), and exact joint
kernels \(\mathbb C[t,f]\) and \(\mathbb C[t]\). The normalized
bad velocities are \(EX=f\), \(EY=G(t)\), while
\[
E^2(Q_1,Q_2,X,Y)^t=(f-F(t),U(t),1,0)^t.
\tag{3}
\]
The retained branch has nonconstant \(U,G\). Those properties
are normal-form conclusions with their own proof dependencies,
not hypotheses silently inferred from a formal matrix.

The two actual good fields first determine the good velocities.
Integrating their exact joint-invariant potentials then expresses
both \(Q_1,Q_2\) as polynomials in \(X,Y\) over
\(K=\mathbb C(t,f)\). Since the original four coordinates
generate the ring, this proves
\[
B\otimes_{\mathbb C[t,f]}K=K[X,Y].
\tag{4}
\]
Only after (4) is established are \(X,Y\) known to be independent
over \(K\). Their independence is not obtained by assuming the
bad projections of the defect fields are invertible.

The true partial derivatives provide a polynomial inverse to the
two-by-two graph derivative matrix \(\mathcal K\), hence
\(\det\mathcal K\in K^*\). Its \(X^2\), \(XY\), and \(X\)
coefficients successively force
\[
U=b_0+\kappa G^2,\quad l=a_2G+l_0,\quad
n=2l_0d+n_0,\quad l_0\ne0,
\qquad d=\frac{F'G}{2G'}-F.
\tag{5}
\]
All \(b_0,\kappa,a_2,l_0,n_0\) are complex constants. The resulting
polynomial
\[
S=\frac{Q_2-b_0X-\kappa Y^2/2-a_2Y-n_0}{l_0}
=f+2d(t)
\tag{6}
\]
is a genuine ambient coordinate by its explicit triangular inverse,
and \(ES=1\). Thus
\(A\simeq B/(S)\simeq\mathbb C[Q_1,X,Y]\).
The final step uses the slice theorem directly. In particular it
does not need a new classification theorem or a Jacobian-conjecture
implication.

## 4. Dependent defects: an actual localized symmetry

Write the primitive defect as \(D\), with
\(V_3=aD,V_4=bD\) and jointly invariant polynomial multipliers.
The frozen reduction supplies
\[
E^2x=c\sigma+e,\quad E\sigma=1,\quad
(EX,EY)=e_B\sigma+(p(u),q(u)),\quad Eu=Du=0,
\tag{7}
\]
where \(c,e\) are constant, \(c_B=0\), and the residual curve
has nonconstant tangent direction. The zero bad-acceleration and
constant residual-curve alternatives were already recognized.

In the remaining branch, set
\[
\Delta=e_3q'-e_4p',\qquad
\beta=\frac12\left(\sigma-
\frac{pq'-qp'}{\Delta}(u)\right),\qquad
Z=T_e+\beta T_c.
\tag{8}
\]
The full velocity identities prove \(\Delta(u)\ne0\),
\(E\beta=1/2\), and \([E,Z]=0\). Applying this commutation
to the acceleration and bad velocities forces
\(Z\sigma=Zu=0\). Consequently \(Z\beta=Z\Delta(u)=0\).
Every original coordinate has \(Z\)-degree at most one, and the
denominator is fixed. This proves actual local nilpotence on
\(B_{\Delta(u)}\); it was not inferred from commutation alone.

The genuine constant directions \(c,e\) are independent. In a
constant ambient coordinate frame the field is
\(Z=\partial_b+\beta\partial_a\), with the one required good
partial \(\partial_a=T_c\). These are the exact hypotheses of
the [one-good-output lemma](three-output-cubic-closure-pass41.md#1-a-recognition-lemma-requiring-only-one-good-partial).
That lemma's denominator contraction, commuting-derivation, plane
classification, relative cancellation and regular-kernel inputs
recognize the original \(A\).[^recognition]

Repeated factors in \(\Delta\) are retained. The proof does not
invert the potentially larger multiplier \(ae_3+be_4\), assume
that \(u\) is a coordinate, or transfer the original slice to
the defect derivation.

## 5. An actual control against stronger unsupported claims

The [nonomission family](constant-cubic-nonomission-control-pass67.md)
starts with actual coordinates \((t,y,z,s)\), \(E=\partial_s\),
and any nonconstant polynomial \(G(t)\). It gives a polynomial
coordinate presentation with exact adjoint heights \((1,1,2,2)\),
constant cubic top, and independent defects. All four ordinary
derivatives of its common curve parameter are complex-linearly
independent.

Thus no constant ambient direction has to omit that parameter.
One good partial also fails to preserve the common two-variable
kernel, although a unique constant good line does preserve it.
The example has an explicit polynomial original kernel. It is a
control against two overstrong intermediate claims, not a
cancellation counterexample. The graph proof works without either
overstrong claim.

## 6. Verification and source boundaries

Each new closure note received independent full-file proof reviews,
with author self-review recorded separately. Root also reconstructed
both complete arguments and reread the full one-good-output note.
The [audit record](proof-audits-pass67-working.md) distinguishes
these AI reviews from human and formal verification.

The two new standalone checkers contain three test methods in total.
Two verify an actual polynomial family and its two inverse orders;
one checks the exact formal graph coefficients and slice formula.
They do not machine-verify the all-instance generation theorem,
the external classification results, or cancellation. Commands:

~~~sh
/opt/anaconda3/bin/python research/constant_cubic_nonomission_checks_pass67.py
/opt/anaconda3/bin/python research/constant_cubic_graph_checks_pass67.py
/opt/anaconda3/bin/python research/run_regression_pass67.py
~~~

The [captured full regression](verification-pass67-working.json)
and [working integrity packet](checkpoint-pass67-working.json)
record only actual runs and file checks. Repeated test runs do not
increase distinct counts. The central claim registry and experiment
manifest remain at their historical full60 state; working proofs
and later suites are explicitly separate from that integration.

The earlier normal forms retain their polynomial-curve source
dependencies. This round reread the local written dependencies;
it does not claim a new full audit of every original classification
paper. A fresh web check of the dated primary survey records is
not a statement-level novelty audit of (1).[^landscape]

## 7. Remaining obligations toward the original question

The corrected working question remains
\(A[s_*]\simeq\mathbb C^{[4]}\Rightarrow A\simeq\mathbb C^{[3]}\).
The professor has not confirmed this field and dimension. The
pasted statement with conclusion \(X\simeq\mathbb A^1\) has a
dimension error when \(r>1\).

The supplied frame still has unrecognized nonconstant cubic tops
and higher-flow sectors. Independently of recognizing that entire
frame, a universal theorem supplying such a frame is unproved.
The minimization equivalence and finite inverse-pair search do not
establish that universal existence statement. Closing (1) therefore
does not close either larger obligation.

No human expert review, proof-assistant verification, historical
novelty certification, external communication or submission has
occurred. These boundaries apply even when all finite checks pass.

## Sources

[^recognition]: The full [one-good-output proof and primary-source inventory](three-output-cubic-closure-pass41.md), Section 1 and its four source footnotes. Its final external endpoint is Bhatwadekar, Gupta and Lokhande, [*Some K-theoretic properties of the kernel of a locally nilpotent derivation on k[X1,...,X4]*](https://arxiv.org/pdf/1501.01438v1), Theorem 3.5. Current use is through the explicit inherited source gates, not a new unsupported classification assertion.

[^landscape]: Neena Gupta, [*The Zariski Cancellation Problem and related problems in Affine Algebraic Geometry*](https://arxiv.org/abs/2208.14736), submitted August 31, 2022; César F. Venegas R. and Helbert J. Venegas R., [*Cancellation problem via locally nilpotent derivations*](https://arxiv.org/abs/2512.15590), version 2 dated February 17, 2026. This round directly checked the arXiv title, version and abstract records. Neither abstract was used to verify the new conditional theorem or its novelty.
