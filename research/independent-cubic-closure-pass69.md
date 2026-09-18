# Independent-defect cubic recognition under an actual coordinate frame

Every independent-defect cubic case in the supplied two-quadratic
coordinate frame is now recognized by the written proof chain.
The new step closes the original joint-rank-two alternative left
by the preceding pass. Nonconstant normalized transverse speed
produces a rational two-direction symmetry with a proved recognition
alternative. Nonzero constant speed instead admits an explicit
polynomial coordinate shear to the already recognized mixed frame.

This is not a solution of unrestricted complex-threefold cancellation.
Dependent-defect moving cubics remain separate, as do higher moving
flows and the existence of a suitable frame for an arbitrary action.

## 1. Exact theorem and interpretation

Let
\[
B=\mathbb C[Q_1,Q_2,X,Y],\qquad E\in\operatorname{LND}(B),
\qquad E(s_*)=1,\qquad A=\ker E.
\]
The four displayed generators are actual polynomial coordinates,
with genuine partials satisfying
\[
\operatorname{ad}_E^2T_1=\operatorname{ad}_E^2T_2=0,
\qquad \operatorname{ad}_E^3T_X=\operatorname{ad}_E^3T_Y=0.
\tag{1}
\]
Write \(V_X=\operatorname{ad}_E^2T_X\) and
\(V_Y=\operatorname{ad}_E^2T_Y\). Ranks below are dimensions
over \(\operatorname{Frac}B\), not coordinate ranks of individual
derivations.

**Independent cubic theorem.** Under (1),
\[
\operatorname{rank}(V_X,V_Y)=2,\qquad E^4(Q_1,Q_2,X,Y)=0
\quad\Longrightarrow\quad A\simeq\mathbb C^{[3]}.
\tag{2}
\]
The iterate bound concerns degree in the flow parameter on the
given coordinate generators. It does not bound the ordinary
polynomial degree of the coefficients of \(E\).

The underlying working target remains the unconfirmed interpretation
\(A[s_*]\simeq\mathbb C^{[4]}\Rightarrow A\simeq\mathbb C^{[3]}\).
The professor has not confirmed the intended field and dimension.
Neither this interpretation nor the frame hypothesis is silently
removed from the statement.

## 2. Exhaustion of the independent cubic alternatives

| Actual case under (1)--(2) | Written recognition source |
| --- | --- |
| Flow degree at most two | The complete frozen [low-flow theorem](low-flow-closure-pass66.md). |
| Nonzero constant cubic highest vector | The frozen [constant cubic theorem](constant-cubic-closure-pass67.md). |
| Nonconstant highest vector with zero preceding bad vector | The commuting constant-partial branch of [the full highest-vector theorem](two-quadratic-top-line-pass42.md). |
| Nonconstant highest vector, nonzero preceding bad vector, original joint rank three | The complete [rank-three moving cubic proof](constant-and-moving-closure-pass68.md). |
| The same moving alternative, original joint rank two | The two new rank-drop proofs summarized below. |

Independent original defects make their joint rank with \(E\)
either two or three. In the final two rows, actual constant changes
within the good and bad coordinate pairs put the highest data in
the form
\[
E^3x=e_1g^3,\qquad E^2(X,Y)=(g^2,0),\qquad
g\in\ker E\setminus\mathbb C.
\tag{3}
\]
The zero preceding-vector case is kept outside this normalization.
The exact rank formula then shows that \(\delta=E/g\) on \(B_g\)
has two normalized defects of rank one in the remaining original
joint-rank-two case. Neither the localization nor its coordinate
partials are assumed to be polynomial objects of the same kind as
the original ring and partials.

## 3. Rank drop with nonconstant speed: a rational symmetry is enough

The [first rank-drop proof](cubic-rank-drop-nonconstant-speed-pass69.md)
uses the actual five-dimensional normalized companion over the
fraction field. It has cube zero and rank-one square, forcing
\(\delta^2x=e_1\sigma+e\), with \(e\) a genuine complex constant
vector and \(e_B=(1,0)\). The full auxiliary row yields
\(\delta X=\sigma+F\), \(\delta Y=G\), and the ordinary
differential identity \(dF+r\,dG=0\).

If the first normalized defect vanishes, a genuine constant good
partial commutes with \(\delta\). The original-slice unit argument
makes it commute with the original \(E\), giving recognition.
If \(G=0\), the original coordinate \(Y\) is invariant.

For \(G\) nonconstant, full velocity identities give
\(S=T_e+\beta T_1\), where
\(\beta=(\sigma-F-rG)/2\), \([\delta,S]=0\), and
\(\delta\beta=1/2\). Commutation first gives
\(S\sigma=SF=SG=0\). Taking the Lie derivative of the full
ordinary differential relation gives \((Sr)dG=0\), hence
\(Sr=S\beta=0\). This proves niceness on the actual coordinates
without guessing a denominator or a polynomial curve parameter.

The separate [rational two-direction theorem](rational-two-direction-recognition-pass69.md)
handles arbitrary rational coefficients at this stage. In actual
coordinates \((u,v,a,b)\) with \(S=\partial_b+\beta\partial_a\),
its elementary rational differential-equation classification is
\[
\beta\in\mathbb C(u,v)\quad\text{or}\quad
\beta=\frac{a+A_0(u,v)}{b+B_0(u,v)}.
\tag{4}
\]
The original slice proves \(Sg=0\) before original commutation
is used. In the first alternative a reduced denominator is proved
\(E\)-invariant and an actual localized translation meets the
existing one-good-output theorem. In the second, the rational
field need not be an LND on its denominator localization. Its
polynomial kernel over \(\mathbb C(u,v)\) instead forces the
original \(E\) to preserve the actual plane \(\mathbb C[u,v]\).
Planar LND recognition and the regular-original-kernel endpoint
then finish the argument.[^recognition]

## 4. Constant nonzero speed: a global polynomial shear

The [constant-speed proof](cubic-rank-drop-constant-speed-closure-pass69.md)
uses \(G\in\mathbb C^*\), so \(EY=Gg\) is an original
polynomial identity. Crucially, the original full top coefficient
gives \(g[E,T_1]=-V_X\), before any localization is used.

The coordinate replacement is explicit:
\[
q_1=Q_1-\frac{XY}{2G}+\frac{Y^3}{12G^3},\qquad
(q_2,x_3,x_4)=(Q_2,X,Y).
\tag{5}
\]
Its inverse changes the two correction signs. The new
\(X\)-partial is \(T_X+Y T_1/(2G)\); its original second
adjoint is exactly \(V_X+g[E,T_1]=0\).
The new \(Y\)-partial is
\(T_Y+(X/(2G)-Y^2/(4G^3))T_1\). The coefficient has zero
second \(E\)-derivative, so this partial's third adjoint vanishes.
The original two good partials are unchanged.

Thus (5) is an actual polynomial frame of bound \((1,1,1,2)\).
Its coordinate third flow derivative also vanishes identically:
the changed first component is \(g^3-3g^3/2+g^3/2=0\).
The established mixed slice theorem applies to the original
action and slice. This closes the constant-speed branch without
promoting a merely divided-good partial to an original-good one.

## 5. Two auxiliary deductions and their limits

The [normalized-defect projection lemma](projected-cubic-defects-pass69.md)
proves that the normalized defects are genuine LNDs on \(B_g\).
With \(\sigma_0=EX/g\), projection of an original commuting
defect \(V\) to the kernel of \(\delta\) is
\(N=V-(V\sigma_0)\delta\). It is locally nilpotent on the
actual extension \((\ker\delta)[\sigma_0]\).
The full column identity makes \(gN\) polynomial on \(B\).
Its restriction to \(A\) is only the replica \(gV|_A\);
this does not create another independent intrinsic direction.
The rank-drop proof above does not require this additional
local-nilpotence result for its rational companion calculation.

The separate [vertical-top exclusion](vertical-top-exclusion-pass69.md)
proves that, for a sliced LND \(E\) and an actual LND \(T\),
a highest \(\operatorname{ad}_E^nT\) parallel to \(E\) must
vanish. An actual Laurent-parameter conjugation, restriction and
specialization supply an LND before its self-divisibility property
is used. This gives an independent divided-good descent criterion.
The simpler original identity used in Section 4 means that the
constant-speed closure does not depend on this lemma.

## 6. Verification and current evidence

The new proofs have separate author self-review and independent
through-EOF AI reconstructions. The [audit record](proof-audits-pass69-working.md)
states the completed reviews, source-read limits and exact finite
checks. These are not human referee reports or proof-assistant
verification.

Three new standalone suites contain eight methods. They check
actual coordinate inverses, projection and denominator controls,
rational differential identities, the shear's formal coefficient
cancellations, and Laurent-dilation coefficient bounds.
The projection example explicitly fails the target full frame;
the radial example explicitly fails localized local nilpotence.
Neither is presented as a realization of a still-unknown kernel.

The [captured combined regression](verification-pass69-working.json)
passed 1,021 methods in 136 suites, with every process exiting
zero. Its actual UTC interval was 2026-09-14 02:03:29.218741
through 02:05:03.238131. The command set contains the exact 132
frozen67 suites, the two-method68 addition, and the three new69
suites. Only eight methods in three suites are new in this pass.
The [runner](run_regression_pass69.py) reuses the frozen67
subprocess helper, hashes full captured output before omission,
and retains the three new suite outputs. This is a finite
regression, not a machine verification of the written theorems.

~~~sh
/opt/anaconda3/bin/python research/run_regression_pass69.py
/opt/anaconda3/bin/python research/normalized_defect_projection_checks_pass69.py
/opt/anaconda3/bin/python research/rational_two_direction_checks_pass69.py
/opt/anaconda3/bin/python research/cubic_shear_vertical_checks_pass69.py
~~~

## 7. Remaining obligations

The constant-highest theorem from pass68 remains valid for both
defect ranks. Together with (2), the remaining supplied-frame
sectors have nonconstant highest vectors and are:

- Independent defects with flow degree four or five, after the
  inherited individual recognition criteria.
- Dependent defects without a complex constant relation, with
  flow degree three or four, after their existing recognition
  criteria.

The entire two-quadratic profile is not closed. The all-profile
height threshold is not raised to ten. Even closure of the
remaining sectors would leave the separate universal-coordinate-
frame implication unresolved.

The historical central registry and manifest remain at their
full60 integration state. A new proof packet is not silently
represented as a completed reintegration of those records.
There is no general solution, confirmed novelty, human expert
review, proof-assistant certificate, external contact, public
posting or submission.

## Sources

[^recognition]: The complete source gate is stated and applied in [the rational two-direction theorem](rational-two-direction-recognition-pass69.md), Sections 4--5. Its plane input is Rentschler's theorem, stated as Theorem 2.7 in Dasgupta and Gaifullin, [*On locally nilpotent derivations of polynomial algebra in three variables*](https://arxiv.org/html/2306.00510v2). Its original invariant-coordinate and regular-kernel endpoint is Bhatwadekar, Gupta and Lokhande, [*Some K-theoretic properties of the kernel of a locally nilpotent derivation on k[X1,...,X4]*](https://arxiv.org/abs/1501.01438), Theorem 3.5. Exact source statements and retained proof dependencies are distinguished from fresh full-source reconstructions in the linked notes.
