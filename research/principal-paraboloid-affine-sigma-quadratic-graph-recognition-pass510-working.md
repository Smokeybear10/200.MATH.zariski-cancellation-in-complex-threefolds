# Recognition of the supplied affine-sigma, nondegenerate quadratic graph

Working scoped synthesis. Retain EVERY actual hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
including its entire initial kernel, original global slice, literal
selected nonzero derivation, genuine potentials and both actual
returns. Suppose the intrinsic parameter sigma is affine and
nonconstant, and, in the existing parameter P=sigma,

\[
\theta=aP^2+bP+c,\qquad a\ne0,\qquad
m=k_s,\qquad \delta=1+ma\ne0.
\tag{1}
\]

Then the accepted variable-coupling exclusions give

\[
\boxed{m\in\mathbb C.}
\tag{2}
\]

Retaining the earlier recognition dependencies of
[473](principal-paraboloid-complete-constant-coupling-recognition-pass473-working.md),
including its separate zero-coupling proof, it follows that

\[
\boxed{A\simeq\mathbb C^{[3]}.}
\tag{3}
\]

This is recognition of one supplied, oriented quadratic-graph
sector. It is NOT recognition of all projected conics, all charts
of264, or arbitrary cancellation candidates. It is a synthesis of
internal working proofs, not a newly independent recertification of
all historical dependencies. No novelty, human expert review or
proof-assistant verification is claimed.

## 1. Actual scope and the parameters that are not coordinates

The retained setup includes

\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad
X=a_0u+x_0,\quad a_0\ne0,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\qquad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the ENTIRE initial kernel},\\
0\ne N=[u^4]\partial_Z|_A,\qquad
L=\operatorname{Frac}\ker_A N,\qquad [L:\mathbb C(t,s)]<\infty,\\
O=L[A]=L[v],\qquad Nv=1,\qquad
\operatorname{Frac}A=L(v)=\mathbb C(y,z_0,w_{\rm int}).
\end{gathered}
\tag{4}
\]

All exact coefficient partials and actual-return licenses of264
remain. Their joint constants are C. None of (4) is inferred merely
from knowing that A[u] is a polynomial ring. Establishing such chart
entry is still an unresolved part of the general research objective.

The assumption deg_v(sigma)=1 makes P=sigma a parameter of O over L,
with NP=rho in L*. It does not make P an actual complex polynomial
coordinate. In that parameter the complete scalar is

\[
J_{t,s,P}(X)=-a_0^4/\rho\in L^*.
\tag{5}
\]

Its coefficient-field value need not be constant in t or s. The
second nondegeneracy condition in (1) means that

\[
S(P)=P^2+k_tP+m\theta(P)
\tag{6}
\]

has degree exactly two. The degree-drop boundary delta=0 is not
included. Whenever m is nonzero, all genuine-level and parity inputs
of296 and327 are retained; they are not replaced by arbitrary formal
polynomials with similar degrees.

## 2. Variable coupling with nonzero s derivative is impossible

Assume m is not complex. It is then nonzero as a field element.
First suppose m_s is nonzero. The complete reduction
[498](principal-paraboloid-transverse-coupling-conic-reduction-pass498-working.md)
and initial-form argument
[500](principal-paraboloid-transverse-conic-initial-rigidity-pass500-working.md)
give, with F0=ker_L(partial_s), exactly two alternatives:

\[
\gamma=\frac{m_s}{m^3}\in\mathbb C^*
\quad\text{or}\quad
\gamma=\frac{C}{(t-\tau)^2},\qquad C\in\mathbb C^*,\ \tau\in\mathbb C.
\tag{7}
\]

The constant alternative is impossible by501, the actual normal
form504, and the full mixed-derivative contradiction
[506](principal-paraboloid-constant-transverse-conic-mixed-derivative-exclusion-pass506-working.md).
It retains and separately excludes the beta-zero boundary of504.

The inverse-square alternative is impossible by the slope reduction
502 and the complete exclusion
[505](principal-paraboloid-inverse-square-transverse-conic-exclusion-pass505-working.md).
That proof treats both values of its auxiliary cstar. Its final
identity makes an ACTUAL coordinate minus a complex constant a
square in the fraction field of the polynomial ring, contradicting
the valuation at that prime.

Thus m_s must vanish in every remaining variable-coupling case.

## 3. Variable coupling with zero s derivative is also impossible

Now m_s=0. Since m is not complex and the joint exact constants
are C, m_t is nonzero. The full fifth-root exclusion
[495](principal-paraboloid-fifth-root-conic-initial-exclusion-pass495-working.md)
rules out m_tt nonzero. Exact subtraction therefore gives

\[
m=pt+d,\qquad p\in\mathbb C^*,\quad d\in\mathbb C.
\tag{8}
\]

The genuine unit-multiplier argument
[494](principal-paraboloid-unit-tangent-multiplier-pass494-working.md)
gives a_s=0. The complete moving-frame reduction
[496](principal-paraboloid-affine-coupling-conic-moving-frame-pass496-working.md)
is now applicable, including its exact moving connection and
unrestricted lower functions. Its existing f,h in F0 satisfy

\[
k=ms+f,\qquad
n=p^2s^2/4+(pf'/2-h)s+n_0,\qquad f''''=6ah''.
\tag{9}
\]

There are no remaining unexamined zero branches in the following
split. A prime denotes the exact t derivative on F0.

| Condition in the full496 chart | Complete exclusion |
| --- | --- |
| a'=0 | [499](principal-paraboloid-constant-conic-leader-two-quasi-exclusion-pass499-working.md), retaining both alternatives of the two-quasi theorem and all actual lower terms |
| a' nonzero, b_s-pa=0 | [503](principal-paraboloid-moving-conic-leader-zero-transverse-exclusion-pass503-working.md), including both root alternatives and their zero cases |
| a' and b_s-pa nonzero, h'' nonzero | [508](principal-paraboloid-moving-conic-curvature-exclusion-pass508-working.md), using both exact first integrals and a rational-function pole argument |
| a' and b_s-pa nonzero, h''=0, normalized H=0 | [507](principal-paraboloid-moving-conic-zero-normalized-offset-exclusion-pass507-working.md), using the entire constant-intrinsic scalar |
| a' and b_s-pa nonzero, h''=0, normalized H nonzero | [509](principal-paraboloid-moving-conic-nonzero-normalized-offset-exclusion-pass509-working.md), treating both values of its auxiliary determinant |

For precision, the last two rows are an exhaustive split only AFTER
h''=0. Equation (9) then makes f complex cubic or lower degree and
h complex affine. The licensed actual maps in503 and507 normalize
to m=t,k=ts,h=H in C, while preserving a' and b_s-pa nonzero,
the entire initial kernel, selected N, actual returns and calibrated
scalar. No field-valued ambient transformation is used to erase
a nonzero h''.

508 and the nonzero-determinant branch of509 contradict the genuine
nonzero multiplier from494, not an assumed nonzero ansatz coefficient.
The zero-determinant branch of509 contradicts the calibrated scalar
directly. Their comparison equations retain every lower function and the
moving-frame correction.508 handles repeated or moving denominator
roots by a coefficient-field pole argument, not by deleting actual
fibers.509 treats its zero determinant at a fixed complex X and
never specializes a rational expression at a pole.

The table exhausts every field-element alternative under (8),(9).
Hence the m_s=0, noncomplex-m case is impossible as well. Together
with Section2 this proves (2).

## 4. Constant coupling and the retained recognition endpoint

Apply the complete scoped synthesis473, whose full current source
was reread for this composition. It recognizes every complex m
under all actual264 hypotheses, without restrictions on k_ttt or
the lower potentials. Its m=0 proof retains the exhaustive268/294
union; no formula dividing by m is extended to that case here.

The nonzero-constant proof in473 retains its original published and
internal recognition endpoints, described in its Section5. This
note does not recursively reprove those historical sources or
upgrade their verification status. Subject to precisely those
retained working dependencies, (2) therefore proves (3).

## 5. Verification and what is still unresolved

Sources505,506,507,508,509 have complete separate saved-source AI
reviews and fresh independent exact coefficient reconstructions,
recorded in the research ledger. The earlier accepted sources in
the case split retain their recorded reviews. Root reread473
through EOF dc746d and revalidated its hash in d975e9. Jet separately
read473 through EOF dd0fc1 and checked the exact scope of the case
split and its boundaries before this synthesis was authored.

This composition requires no new numerical experiment. Its key
verification obligation is that the hypotheses match at every
case transition and that the alternatives are exhaustive. A complete
saved-source review of this synthesis is recorded separately.

The following are NOT supplied by the result:

- An actual allowable coordinate change making sigma affine for
  every projected conic. Both displayed projected functions may be
  quadratic even when their image is a birational conic.
- The delta-zero degree-drop boundary, or affine sigma with theta
  of degree at least three, apart from overlaps with older results.
- Recognition of all other nonlinear projected curves, other entire
  initial kernels, or other time-degree profiles.
- A reduction of arbitrary cancellation data to264, or confirmation
  of the intended field and dimension in Luo's email.

Thus the general cancellation objective remains active and unsolved.
All saved checkers remain frozen; none was executed, imported,
compiled or rerun. No public contact, submission, historical novelty
claim, human expert review or proof-assistant certification occurred.
