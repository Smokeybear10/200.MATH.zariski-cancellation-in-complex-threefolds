# Constant highest flow vectors and the rank-three moving cubic branch

Under the supplied two-quadratic coordinate frame, every constant
highest flow vector is now recognized. A separate argument recognizes
the independent-defect moving cubic branch when the original action
and its two defects have joint rank three. These are conditional
theorems about actual polynomial coordinate frames, not a solution
of unrestricted complex-threefold cancellation.

## 1. Exact statements

Let
\[
B=\mathbb C[x_1,x_2,x_3,x_4],\qquad
E\in\operatorname{LND}(B),\qquad E(s_*)=1,\qquad A=\ker E.
\]
Assume that the actual coordinate partials satisfy
\[
\operatorname{ad}_E^2T_1=\operatorname{ad}_E^2T_2=0,
\qquad
\operatorname{ad}_E^3T_3=\operatorname{ad}_E^3T_4=0.
\tag{1}
\]
Write \(V_j=\operatorname{ad}_E^2T_j\), \(j=3,4\), and let
\(m=\max\{j:E^jx\ne0\}\) be the coordinate flow degree.
This is not the spatial degree of a coefficient of \(E\).
All derivation ranks below are over \(\operatorname{Frac}B\).

**Constant-highest theorem.** If
\[
E^mx\in\mathbb C^4\setminus\{0\},
\tag{2}
\]
then the complete working proof chain gives
\(A\simeq\mathbb C^{[3]}\).

**Rank-three cubic theorem.** If
\[
m=3,\qquad \operatorname{rank}(V_3,V_4)=2,
\qquad \operatorname{rank}(E,V_3,V_4)=3,
\tag{3}
\]
then \(A\simeq\mathbb C^{[3]}\), whether or not its highest
vector is constant.

Both statements retain the original polynomial slice and actual
coordinate partials in (1). A constant top after dividing \(E\)
by an invariant does not satisfy (2) for the original action.
In particular the second theorem is a separate result, not a
formal application of the first to a localized ring.

## 2. Exhaustion of the constant-highest sectors

An actual complex constant relation between the two defects gives
a third good partial by a constant coordinate recombination. The
already recognized mixed-height-nine theorem handles that case.
This includes rank zero. If there is no constant relation, the
defects have rank one or two, with the following exact exhaustion.

| Remaining alternative | Flow bound and recognition |
| --- | --- |
| Flow degree at most two, either rank | The complete frozen [low-flow theorem](low-flow-closure-pass66.md). |
| Constant cubic top, either rank | The frozen [constant-third-derivative theorem](constant-cubic-closure-pass67.md). |
| Independent defects, constant higher top | The six-dimensional companion gives \(m\le6\); the new [higher constant proof](independent-higher-constant-closure-pass68.md) covers \(m=4,5,6\). |
| Dependent defects without a constant relation, constant higher top | The weighted five-dimensional companion gives \(m\le5\); the new [quartic](dependent-constant-quartic-closure-pass68.md) and [quintic](dependent-constant-quintic-closure-pass68.md) proofs cover both remaining values. |

The upper bounds are inherited actual inverse-flow identities:
\(M^6=0\) in the independent case, and \(M^5=0\) in the
weighted dependent case. Their upper Jacobian blocks make the
corresponding highest coordinate iterates constant and the next
iterates zero. They are not guessed cutoffs from an experiment.
The dependent calculation retains its variable auxiliary row.

Thus no higher constant-top alternative is left out of (2).
This exhaustion says nothing about existence of the frame (1)
for an arbitrary sliced action.

## 3. The new global coordinate-section argument

The higher constant proofs exploit two consecutive full companion
images. Their base and auxiliary rows produce actual polynomial
layers and genuine complex integration constants. In the independent
case, for example, the layers have the form
\[
h_{m-1}=c\sigma+d,\qquad
h_{m-2}=c\tau+d\sigma+e,
\quad E\sigma=1,\quad E\tau=\sigma.
\tag{4}
\]
Using both auxiliary rows then fixes the next bad-coordinate layer.
That identity supplies a three-direction polynomial correction
\(Z=T_e+\beta T_d+\gamma T_c\) commuting with \(E\).
Commutation proves \(Z\sigma=0\), and the next layer proves
global local nilpotence: \(Z^3x=0\) in the quartic case and
\(Z^2x=0\) in the higher cases. These properties are established
before the field is called an LND.

The constant directions are independent in the remaining branch.
A complex linear coordinate \(z\), dual to the last direction,
therefore satisfies \(Zz=1\). This gives the actual decomposition
\[
R=\ker Z\simeq B/(z)\simeq\mathbb C^{[3]},\qquad B=R[z].
\tag{5}
\]
The original action restricts to \(R\), and \(\sigma\in R\)
is its actual slice. The known complex surface cancellation theorem
makes \(\ker(E|_R)\) a polynomial two-ring. Integrating the
polynomial \(Ez\in R\) with respect to \(\sigma\) produces an
invariant replacement of \(z\), so the original kernel is a
polynomial three-ring.[^section]

The dependent quartic and quintic proofs need an extra distinction.
Their variable auxiliary row initially gives a differential relation
for a residual polynomial pair, not constant values of that pair.
If either of two successive residual pairs is nonconstant, its
actual curve parameter supplies the precise denominator fixed by
the provisional commuting correction. Only then does it become a
localized nice LND meeting the established one-good-output lemma.
If both pairs are constant, the global construction (5) applies.
Repeated denominator factors and the original slice are retained.

## 4. The moving cubic argument and its global endpoint

For independent defects, the existing highest-vector theorem handles
zero preceding bad vector by a commuting actual partial. In the
remaining nonconstant-top alternative, it gives
\[
E^3x=e_1g^3,\qquad L_0E^2x=(1,0)^tg^2,
\qquad g\in\ker E\setminus\mathbb C.
\tag{6}
\]
The changes giving (6) are only constant changes within the good
and bad coordinate pairs. Under the joint-rank-three condition,
division by \(g\) preserves defect rank two. On \(B_g\), put
\(\delta=E/g\) and \(\sigma=\delta X\).

The [coordinate-local-slice proof](moving-cubic-coordinate-local-slice-pass68.md)
reconstructs the exact rational kernels and constant-top graph on
that localization. It never applies a polynomial-four-ring theorem
directly to \(B_g\), nor presumes that a localized partial is an
LND. Its common curve parameter \(t\) is an actual original
polynomial. Let \(G(t)=\delta Y\) be the normalized transverse
speed. All three alternatives are now recognized.

| Normalized transverse speed | Actual recognition mechanism |
| --- | --- |
| \(G=0\) | The original bad coordinate \(Y\) is invariant. |
| \(G\) nonconstant | The [moving graph theorem](moving-cubic-graph-recognition-pass68.md) constructs an actual triangular coordinate local slice and uses the additional full field-generation equality to obtain an original invariant coordinate. |
| \(G\in\mathbb C^*\) | The [constant-speed theorem](moving-cubic-constant-speed-recognition-pass68.md) uses either a direct triangular invariant coordinate or an actual constant good direction omitting \(t\). |

In the nonconstant case, a coordinate \(S\) with \(ES=g\) is
not itself enough. The graph also gives
\(\operatorname{Frac}B=\mathbb C(t,S,X_0,Y)\) in actual
coordinates \((Q_1,S,X_0,Y)\). Since \(t\) is an actual
polynomial, equality of the one-variable rational function fields
forces
\[
t=A(S,X_0,Y)Q_1+B(S,X_0,Y).
\tag{7}
\]
The unchanged good partial proves \(EA=0\). The other three
velocities are polynomials only in \(t\). Their constant coefficient
vectors either span three directions, forcing \(A\) to be a
nonzero complex constant, or leave an invariant linear coordinate.
Both outcomes give a global invariant ambient coordinate.

For nonzero constant \(G\), the separate proof obtains
\(\sigma=Y/G-h(t)\). Constant \(h\) gives a triangular invariant
coordinate. Otherwise the good-field identities give
\(T_2t=r(t)T_1t\). If \(T_1t=0\), the omitted direction is
already present. If not, coprime one-variable numerator and
denominator substitution, followed by total degree in the actual
good coordinates, forces \(r\in\mathbb C\). The resulting
constant good direction meets the original-action recognition
theorem, with every hypothesis checked.[^moving]

One provisional outline incorrectly replaced a defect applied to
a velocity by the defect applied to a coordinate. The full review
identified that distinction. The saved constant-speed proof does
not use the inference; its direct \(T_1t=0\) recognition branch
handles the case. No earlier frozen proof was changed.

## 5. Verification and current evidence

The six new recognition/reduction notes have separately recorded
author self-review and independent full-file AI reconstructions.
The [audit record](proof-audits-pass68-working.md) lists the exact
reviewers, source-read boundaries, and corrected outline. These
are not human referee reports or proof-assistant verification.

The one new standalone checker contains two methods. It verifies
symbolic full-velocity and commutator coefficients, the collinear
correction, lower differential rows, and the degree-four/five/six
nilpotence split. It does not manufacture an actual action from
formal data or machine-verify the all-instance proofs. The
[targeted capture](verification-pass68-working.json) records an
actual successful run, separately from the preceding full regression.

~~~sh
/opt/anaconda3/bin/python research/independent_higher_constant_checks_pass68.py
/opt/anaconda3/bin/python research/consistency_checks_pass68.py
~~~

The last fresh full regression remains 1,011 methods in 132 suites
from [pass67](verification-pass67-working.json). The two new targeted
methods do not constitute a fresh combined full regression. The
[working68 integrity packet](checkpoint-pass68-working.json)
checks the new saved files and unchanged frozen predecessors.
The central registry and experiment manifest remain at their
historical full60 integration with 544 claims.

## 6. What remains toward the original conjecture

The complete low-flow theorem, the constant-highest theorem above,
and the rank-three cubic theorem leave these supplied-frame sectors:

- Independent defects with nonconstant cubic top and original
  joint rank two. Division by the invariant factor drops the
  defect rank; the present rank-two graph proof does not apply.
- Independent defects with nonconstant highest top in flow
  degrees four or five, after the existing individual recognition
  criteria.
- Dependent defects with no constant relation and nonconstant
  highest top in flow degrees three or four, after their existing
  curve, zero-motion and ramification criteria.

Those are residual obligations, not asserted examples of unknown
kernels. The universal existence of the actual frame (1) is a
separate unresolved problem even if every listed sector is closed.
The all-profile height threshold has not been increased to ten.

The working target is still the unconfirmed interpretation
\(A[s_*]\simeq\mathbb C^{[4]}\Rightarrow A\simeq\mathbb C^{[3]}\).
The professor has not confirmed the field and dimension. There
is no general solution, human expert review, proof-assistant
certificate, historical novelty certification, external contact,
public posting or submission. A passing artifact checker cannot
change any of those mathematical or review boundaries.

## Sources

[^section]: [Independent higher constant-top proof](independent-higher-constant-closure-pass68.md), Section 2 and its source footnote, contains the full commuting coordinate-section lemma. It uses the established complex surface cancellation theorem, cited to Takao Fujita, [*On Zariski problem*](https://doi.org/10.3792/pjaa.55.106), Proceedings of the Japan Academy, Series A 55 (1979), 106-110, through the retained complete statement in Maubach's author manuscript. No fresh full reconstruction of Fujita's proof is claimed.

[^moving]: [Moving graph recognition](moving-cubic-graph-recognition-pass68.md), Sections 2--4, retains Derksen, van den Essen and van Rossum's original-slice Dedekind-base theorem. [Constant-speed recognition](moving-cubic-constant-speed-recognition-pass68.md), Sections 2--4, applies the complete [omitted-good-direction theorem](good-direction-recognition-pass46.md), whose local proof was freshly reread. Its curve, planar and regular-kernel source gates remain explicitly inherited, not replaced by numerical checks or a new full-paper audit.
