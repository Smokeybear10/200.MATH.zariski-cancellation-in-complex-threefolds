# Recognition of the supplied two-quadratic frame and height ten

Every sliced action in the actual two-quadratic coordinate frame is
recognized by the written conditional proof chain. Combined with the
other previously recognized profiles, this raises the all-profile
slice-filtration height threshold from nine to ten. It does not
produce such a frame for an arbitrary action.

## 1. Complete supplied-frame statement

Let
\[
B=\mathbb C[x_1,x_2,x_3,x_4],\qquad
E\in\operatorname{LND}_{\mathbb C}(B),\qquad E(s_*)=1.
\]
The displayed generators are actual polynomial coordinates, with
genuine partials \(T_i=\partial_{x_i}\). Suppose
\[
\operatorname{ad}_E^2T_1=\operatorname{ad}_E^2T_2=0,\qquad
\operatorname{ad}_E^3T_3=\operatorname{ad}_E^3T_4=0.
\tag{1}
\]
Then
\[
\boxed{\ker E\simeq\mathbb C^{[3]}.}
\tag{2}
\]

Put \(V_i=\operatorname{ad}_E^2T_i\) for \(i=3,4\),
and take ranks over \(K=\operatorname{Frac}B\).
The [dependent-frame theorem](dependent-frame-closure-pass71.md)
proves (2) whenever the pair has rank at most one. This includes
vanishing defects and constant relations.

Otherwise the pair has rank two, so the span of
\(E,V_3,V_4\) has rank either two or three. The rank-two case
is the complete [joint-rank-two synthesis](joint-rank-two-frame-closure-pass72.md).
For rank three, let \(m\) be the greatest nonzero coordinate
flow index, so \(E^m x\ne0\) and \(E^{m+1}x=0\).
The remaining cases are exhausted as follows.

| Original flow case | Complete conditional input |
| --- | --- |
| \(m\le3\) | [Cubic frame recognition](cubic-frame-closure-pass70.md), for every defect rank. |
| \(m\ge4\) and \(E^m x\) is constant | The original six-dimensional companion gives \(m\le6\); [higher constant-top recognition](independent-higher-constant-closure-pass68.md) covers all three possibilities. |
| \(m\ge4\) and \(E^m x\) is nonconstant | The [highest-vector theorem](two-quadratic-top-line-pass42.md) gives \(m\le5\); the [original joint-rank-three transfer](independent-higher-joint-rank-closure-pass73.md) covers both \(m=4,5\). |

The last transfer preserves normalized defect rank two and retains
both auxiliary rows of the companion. It then checks the exact
original-ring quartic and quintic endpoint hypotheses. It does not
assume that invariant localization remains a polynomial four-ring.
These alternatives prove (2) for every action satisfying (1).

## 2. The resulting all-profile threshold

Let \(A=\ker E\), so the supplied slice gives \(B=A[s_*]\).
For any actual polynomial coordinate frame, use the intrinsic
slice-filtration derivation degrees
\[
q_i=\sup_{f\ne0}\bigl(\deg_{s_*}T_i f-\deg_{s_*}f\bigr),
\qquad H=\sum_{i=1}^4(q_i+1).
\tag{3}
\]
These degrees are finite integers at least minus one. For nonnegative
degrees they equal the actual partials' adjoint heights, as in the
[filtration definition and low-profile proof](coordinate-frame-minimization-pass.md),
Sections 1 and 2. They are not degrees of the coefficients of \(E\).

**Height-ten consequence.** Under the original sliced hypotheses,
\[
H\le10\quad\Longrightarrow\quad A\simeq\mathbb C^{[3]}.
\tag{4}
\]

First, a partial of degree minus one has the form \(T_i=fE\)
with \(f\in A\). An actual coordinate partial has a polynomial
slice, so \(f\) is a unit of \(B\), hence a nonzero complex
constant. Then \(A=\ker T_i\) is polynomial. This branch must
be separated before sorting nonnegative profiles.

Otherwise sort \(0\le q_1\le q_2\le q_3\le q_4\).
Equation (3) gives \(\sum q_i\le6\). If at least two are zero,
two actual partials commute with \(E\); their common actual
polynomial plane is preserved by \(E\). The established planar
and regular-original-kernel argument recognizes \(A\).
If exactly one is zero and another is one, restriction to the
commuting partial's actual polynomial three-ring invokes the
slice-free single-partial lemma. These are precisely the two
low-profile gates in the linked Section 2; no slice on a restricted
derivation is being assumed.

If there is exactly one zero but no one, the sum bound forces
\[
(q_1,q_2,q_3,q_4)=(0,2,2,2).
\tag{5}
\]
This is recognized by the [three-variable quadratic-frame theorem](three-variable-quadratic-frame-pass42.md),
Section 6, on the actual four-ring with its original slice.

Finally suppose all four degrees are positive. If \(q_3=1\),
the profile is bounded componentwise by \((1,1,1,3)\), the complete
[one-cubic-column theorem](../deep-pass-41.md), Sections 1 and 2.
If \(q_3\ge2\), the sum bound instead forces
\[
(q_1,q_2,q_3,q_4)=(1,1,2,2),
\tag{6}
\]
which is (1). This proves (4) without omitting any sorted profile.

## 3. The universal obligation is unchanged

The minimum over actual coordinate frames exists as an integer,
but existence does not bound its value. The adapted frame of a
polynomial kernel has minimum height three. Consequently the
earlier exact characterization and (4) give
\[
H_{\min}(E)\le10
\quad\Longleftrightarrow\quad H_{\min}(E)=3
\quad\Longleftrightarrow\quad A\simeq\mathbb C^{[3]}.
\tag{7}
\]
A hypothetical nonpolynomial cancellation kernel must therefore
have \(H_{\min}\ge11\). This is a conditional lower bound on
a hypothetical counterexample, not its construction or exclusion.
Proving a universal height-ten bound would still solve the working
cancellation problem; no such bound is supplied here.

The [bounded-family degree note](universal-family-degree-boundary-pass73.md)
addresses a separate quantifier: pointwise witness existence would
imply uniform degree bounds within each fixed finite-complexity
family. It does not establish pointwise existence and is not an
input to (2) or (4).

## Review and source scope

Root wrote this synthesis after reading the complete new transfer,
its actual42/68/71/72 hypotheses, the precise other-profile theorem
statements and the low-profile filtration gates. General independently
checked the entire sorted-profile exhaustion and its original-slice
requirements before this note was written. Full saved-file reviews
must be recorded separately, not inferred from that outline check.

The source theorems and earlier complete arguments are the linked
dependencies. This note adds no external classification theorem or
numerical method. The [audit](proof-audits-pass73-working.md) records
the separate AI reviews and actual full finite regression. Neither
tests nor these reviews are human expert approval, a formal proof,
historical novelty certification, or a general cancellation solution.
Frozen passes through72 are unchanged.
