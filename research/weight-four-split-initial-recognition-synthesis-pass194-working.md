# Recognition of the supplied full split-quartic initial configuration

Status: working synthesis of the saved193--194 proofs and the zero-R
recognition192. Every supplied actual globally sliced frame satisfying
the full split initial-kernel hypothesis below has an invariant coordinate
of the original polynomial four-ring. The resulting kernel is a polynomial
three-ring. This is a restricted recognition theorem, not arbitrary
coordinate entry or unrestricted cancellation.
The normal-form corollary in Section 6 also closes the full irreducible
weight-four stratum with zero quadratic part in the two bad variables.

## 1. Exact statement and retained actual chart

Assume
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=\mathcal A[u],\qquad
E=\partial_u,\qquad \mathcal A=\ker E,\\
\deg_E(X,Y,Z,W)=(1,1,2,2),\qquad
\ker\theta_0=(\mathsf X\mathsf Y\mathsf Z+\mathsf X^4+\mathsf Y^4).
\end{gathered}
\tag{1}
\]
The displayed ideal is the entire weighted initial kernel, with weights
\((1,1,2,2)\), not merely one relation among leading coefficients.
The coordinates are actual polynomial coordinates and \(u\) is a global
slice. No existence of such a frame for an arbitrary cancellation
problem is asserted.

The [universal chart184](weight-four-universal-chart-potentials-pass184-working.md)
supplies the exact selected derivation, coefficient fields, and identities
\[
\begin{gathered}
q=-t^3-t^{-1},\qquad [L:\mathbb C(t,\rho)]<\infty,\qquad
K=\ker_L\partial_\rho,\quad [K:\mathbb C(t)]<\infty,\\
L[y,z,w]=L[v],\qquad \mathbb C(y,z,w)=L(v),\qquad
\det\frac{\partial(Y,Z,W)}{\partial(t,\rho,v)}
 =-\mathfrak a^3\in L^*,\\
Y=y+tX,\qquad Z=z+(q'y+k)X+qX^2,\qquad
W=w+\vartheta X+\rho X^2,\qquad R=k_\rho.
\end{gathered}
\tag{2}
\]
The last determinant holds for every \(X\). The variables \(t,\rho\)
are independent and the derivative constants of \(K\) are \(\mathbb C\).
Neither \(K=\mathbb C(t)\) nor an original-ring unit speed is assumed.

## 2. The zero-R branch already returns an original coordinate

If \(R=0\), the
[split zero-R recognition192](weight-four-split-zero-r-coordinate-recognition-pass192-working.md)
applies directly. Its general-d coefficient integral and exact field return
supply the hypotheses of the algebraic-cover lemmas191.
The quadratic cover is excluded, the linear cover has slope
\(\lambda t\) with \(\lambda\in\mathbb C^*\), and the residual exact
linear pencil forces the remaining coefficient slope to be complex.

The resulting coordinate is
\[
I=W-(\lambda XY+\beta X+\alpha Y+D)Z-Q_0(X,Y),\qquad
Q_0\in\mathbb C[X,Y],\quad \alpha,\beta,D\in\mathbb C,\qquad EI=0.
\tag{3}
\]
The coefficient of \(W\) is one; keeping \(X,Y,Z\) fixed gives its
polynomial inverse immediately. Thus this branch provides an original
ambient coordinate, not merely an element of the generic coefficient
field.

## 3. The nonzero-R branch has exactly three alternatives

If \(R\ne0\), the
[actual three-alternative reduction193](weight-four-split-nonzero-r-three-alternatives-pass193-working.md)
first excludes constant projected \(y\) by an actual commuting
derivation, kernel contraction, and the two-coordinate theorem.
It then gives \(R_\rho=0\), the whole projected plane ring
\(L[y,\vartheta]=L[v]\), a unit evaluated cofactor, and a nonvanishing
quartic top.

Its three alternatives are a pure quartic graph, a quadratic graph
with a nonzero square term, and a quadratic projection with quartic
selected plane relation. In the notation of that note, the last two
have the common form
\[
\mathcal H=A(V-P(U))^2+B_1U+B_0,\qquad
A,p_2\ne0,\qquad P=p_2U^2+p_1U+p_0.
\tag{4}
\]
For the quadratic graph
\(\mathcal H=\omega(V-P_2)+A_2(V-P_2)^2\), completing the square shifts
only the constant term of \(P_2\), and gives (4) with \(B_1=0\).
For the quadratic projection, (4) already holds with \(B_1\ne0\).
Thus neither alternative is omitted by using the common square form.

## 4. Both square alternatives are excluded by two separate gates

Set \(f=1/R\), \(d=t^{-4}-1\), and \(D_f=d'f/4+df'\).
The coefficient comparison of
[split ODE192](weight-four-split-nonzero-r-ode-counterexample-pass192-working.md)
makes every instance of (4) satisfy
\[
f,f'',D_f\ne0,\qquad
\nu=n_{\rho\rho}=\frac{(f'')^2}{8f^3D_f}\in K^*,\qquad
20D_f f'''-3d(f'')^2-12f''D_f'=0.
\tag{5}
\]
This equation alone is insufficient: \(f=t^5+3t\) is its exact
nonaffine rational solution.

The [general square-Jacobian gate193](weight-four-split-square-candidate-jacobian-obstruction-pass193-working.md)
adds a different requirement. If \(B_1\ne0\), let
\(\zeta=\vartheta-P(y)\) and \(y=a\zeta^2+b\), where
\(a=-R\nu/(2B_1)\). The coefficient of \(\zeta^5\) in the actual
scalar Jacobian is \(2\nu p_2a\,a_\rho\). It forces
\((B_1)_\rho=0\). If \(B_1=0\), that conclusion is already true.

The same note proves \(\ell\in K[\rho]\) with degree at most three,
and derives the exact expression \(J_3(R,\nu)\) for
\([\rho^3]B_1\), independent of all lower potentials. Hence
\[
J_3(R,\nu)=0
\tag{6}
\]
is necessary in both square alternatives, including the quadratic
graph with \(B_1=0\). No choice of \(m\) or of the constant remainder
in (4) can change this condition.

The [two-gate algebraic exclusion194](weight-four-split-two-gate-algebraic-exclusion-pass194-working.md)
proves that (5) and (6) are incompatible in any finite
\(K/\mathbb C(t)\) under their nonzero gates.
Its local expansion at a place over infinity leaves leading exponents
zero, one, or five. Exponent one forces \(f\) to be affine, violating
\(f''\ne0\). The two possible nonaffine leading types give nonzero
leading terms in \(J_3\), independent of every lower Puiseux term.
This is not a rational-function ansatz or a conclusion from finite
symbolic tests.

Both square alternatives are therefore impossible. The counterexample
to the first ODE's proposed affine-only extension remains valid;
it is the additional actual-Jacobian equation that removes it here.

## 5. The remaining quartic branch supplies an original invariant coordinate

The pure-quartic coefficient comparisons in the reduction193 supply
precisely the additional hypotheses of
[pure-quartic coordinate recognition193](weight-four-split-pure-quartic-coordinate-recognition-pass193-working.md):
\(R=1/(\alpha t+\beta)\), \(n_\rho=cR^2\) with complex constants,
and affine \(y\) on the full generic line.

That proof retains both reciprocal cases allowed by the split scalar
equations. Its exact field return and linear-pencil argument make
the remaining slope complex. Polynomial coefficient transport then
constructs original coordinates, fixing \(X,Y\), of the form
\[
\begin{aligned}
J&=W-\lambda_0(X,Y)Z,&
I&=Z-B_0(X,Y)J-Q_0(X,Y),\\
Z&=I+Q_0(X,Y)+B_0(X,Y)J,&
W&=J+\lambda_0(X,Y)\{I+Q_0(X,Y)+B_0(X,Y)J\},
\end{aligned}
\tag{7}
\]
where every displayed coefficient is in \(\mathbb C[X,Y]\) and
\(EI=0\). Both inverse compositions are polynomial identities.
The full \(X\)-independent determinant, including the coefficient
change and \(Ny\), is used before the transport step. A projected
parameter has not been declared an original coordinate without this
construction.

In either \(R\) branch an original invariant coordinate \(I\) exists.
The global slice gives \(\mathcal A\simeq B/(u)\); \(Eu=1\) makes
that hypersurface regular. The nonzero action is therefore a
\(\mathbb C[I]\)-linear locally nilpotent derivation of an actual
polynomial four-ring with regular kernel.
[Bhatwadekar--Gupta--Lokhande, Theorem 3.5](https://arxiv.org/html/1501.01438v1)
gives
\[
\mathcal A=\mathbb C[I]^{[2]}\cong\mathbb C^{[3]}.
\tag{8}
\]
The exact published statement is retained as an input; this synthesis
does not recursively verify its proof dependencies.

## 6. Corollary for the entire zero-bad-quadratic-part stratum

Suppose instead that the same actual globally sliced exact1122 setup has
full principal initial kernel \((F)\), where the irreducible weight-four
generator is
\[
F=P_2(\mathsf X,\mathsf Y)\mathsf Z
 +Q_2(\mathsf X,\mathsf Y)\mathsf W+H_4(\mathsf X,\mathsf Y).
\tag{9}
\]
The subscripts are ordinary homogeneous degrees. Thus the terms
quadratic in \(\mathsf Z,\mathsf W\) are zero. This is an additional
condition on a weight-four kernel, not a property of every such kernel.
If both \(P_2,Q_2\) vanished, a binary quartic over \(\mathbb C\)
would factor into linear forms, contrary to irreducibility.

The [zero-bad-rank normal forms184](weight-four-zero-bad-rank-normal-forms-pass184-working.md)
give exactly four normal forms using constant invertible linear changes
of the good and bad slots and binary quadratic translations of the bad
slots. Both the transformations and their inverses are actual polynomial
maps, homogeneous for the weights \((1,1,2,2)\).
Every slot keeps its exact time degree: otherwise its nonzero weight-one
or weight-two coordinate polynomial would belong to the full weight-four
ideal \((F)\), which is impossible in this positive grading. The full
initial kernel transforms with the same weighted automorphism, rather
than being replaced by a single necessary leading relation.

Consequently every normalization retains the global slice, the exact1122
profile, and all full-kernel hypotheses required in the following table.

| Normalized full initial generator | Retained conclusion |
| --- | --- |
| \(\mathsf X^2\mathsf Z+\mathsf Y^2\mathsf W\) | Excluded by the [complete coprime proof185](weight-four-frontier-synthesis-pass185-working.md). |
| \(\mathsf X^2\mathsf Z+\mathsf X\mathsf Y\mathsf W-\mathsf Y^4\) | Recognized by the [full common-factor synthesis186](weight-four-common-factor-recognition-synthesis-pass186-working.md). |
| \(\mathsf X^2\mathsf Z-\mathsf Y^4\) | Recognized by the [full absent-variable synthesis190](weight-four-absent-variable-recognition-synthesis-pass190-working.md). |
| \(\mathsf X\mathsf Y\mathsf Z+\mathsf X^4+\mathsf Y^4\) | Recognized by Sections 1--5 above. |

Each recognized row supplies an invariant ambient coordinate and a
polynomial three-ring kernel. Undoing the actual polynomial normalization
preserves both assertions; the invariant ring is the same \(\ker E\).
The excluded row cannot occur under the hypotheses. Therefore every
supplied actual frame satisfying (9) has
\(\mathcal A\cong\mathbb C^{[3]}\), and in fact an original invariant
coordinate \(I\) with \(\mathcal A=\mathbb C[I]^{[2]}\).

This corollary closes the zero-quadratic-part stratum in the two
bad variables. It does not convert any positive-rank bad quadratic
form to that stratum and does not assert a minimality or entry theorem.

## 7. Boundaries of the synthesis

The main theorem settles recognition under the supplied full split
configuration (1), using the saved actual chart and branch proofs.
Section 6 extends recognition to (9) by the stated actual normalizations
and the separately retained completed row theorems.
The theorem does not establish an entry procedure for an arbitrary
polynomial four-ring with a slice.

Positive bad quadratic rank, height-two initial kernels, higher minimum
time profiles, arbitrary coordinate entry, and the unrestricted
cancellation problem remain open in the present investigation.
No claim that every unsolved configuration is reducible to (1) is made.
The earlier absent-variable examples are not examples of this split form.

This synthesis records a written proof composition. Finite controls,
where separately executed and recorded, check only their stated
algebraic identities and do not certify field return, local-function
arguments, original-ring descent, or the published endpoint.
No new checker was executed, imported, or compiled for this synthesis,
and no192 or earlier source, index, or metadata packet was changed.
The result is not human expert review, proof-assistant certification,
historical novelty clearance, a public submission, or completion of the
unrestricted goal.
