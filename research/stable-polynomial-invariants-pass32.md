# Cross-frame certificates for the intrinsic Makar-Limanov invariant

Date: 2026-09-13.

Work throughout with the full hypothesis
\[
B=A[s]=\mathbb C[x_1,x_2,x_3,x_4],\qquad E=\partial_s.
\tag{1}
\]
This note does not prove that ML(A)=C. It gives a finite sufficient
certificate using coordinate translations from different ambient
frames, and tests two proposed ways of finding it. Both negative
controls have an actual polynomial cylinder, not merely a contractible
base with a cylinder of unknown isomorphism type.

The old leading-symbol theorem, rank-loss examples and constant-term
projection failures are inherited. The new scope here is the
cross-frame invariant test, target-specific height minimization over
the entire affine-linear frame orbit, and the precise loss of local
nilpotence when a coefficient is chosen by its action on one function.
No novelty or universal cancellation claim is made.

## 1. What the known invariant results actually imply

The [intrinsic-action note](intrinsic-actions-pass.md) already proves
that A admits a nonzero LND. Its subsequent quotient and plinth notes
identify each nonzero intrinsic kernel with C^[2], with a faithfully
flat quotient and principal plinth. None of those statements says
that all the intrinsic kernels have constant intersection.

In particular, the polynomiality of B gives ML(B)=ML*(B)=C, where
ML* intersects only the kernels of sliced LNDs. The published
one-variable comparison is
\[
\operatorname{ML}^*(A[s])\subseteq\operatorname{ML}(A),
\tag{2}
\]
not the reverse inclusion. Dasgupta and Gupta prove (2) by extending
each intrinsic D to D+partial_s and intersecting also with ker E.
Their threefold characterization requires both ML(A)=C and the
existence of an intrinsic sliced LND. The ambient slice s is not
that extra intrinsic slice.[^ml]

The associated-graded LND input is likewise inherited: Alhajjar's
Proposition 2.2, attributed to Daigle, and Proposition 3.4 give the
filtration mechanism used here.[^filtration] No primary statement
read in this bounded audit supplies ML(A)=C from (1) alone. This
reports the scope of the statements checked, not an absence-based
claim about the whole literature.

## 2. A finite certificate from different ambient frames

Choose three actual coordinate LNDs T_1,T_2,T_3 on B. Each must
come with a genuine polynomial coordinate presentation, including
an inverse; a unit Jacobian by itself is not a coordinate proof.
They may come from different frames and need not commute.

For each i, choose q_i>=0 such that
\[
(\operatorname{ad}E)^{q_i+1}T_i=0,
\qquad
K_i=\frac{1}{q_i!}(\operatorname{ad}E)^{q_i}T_i\ne0.
\tag{3}
\]
Such a largest adjoint order exists. Indeed the actual conjugate
\[
\exp(tE)T_i\exp(-tE)
=\sum_{j\ge0}\frac{t^j}{j!}(\operatorname{ad}E)^jT_i
\tag{4}
\]
has polynomial coefficients in the independent parameter t.
Polynomiality follows by applying the finite exponential maps to
the finitely many ambient generators, not from a formal series
being presumed convergent or algebraic.

Each K_i is an LND and commutes with E. For the first assertion,
(4) is an LND on B[t]. In a sufficiently high iterate applied to
any fixed b in B, its highest t-coefficient is K_i^N(b), which
therefore vanishes. The second assertion is immediate from (3).
Consequently
\[
D_i=K_i|_A\in\operatorname{LND}(A),\qquad
h_i=K_i(s)\in A,
\qquad S_i=K_i-h_iE
\tag{5}
\]
is the coefficientwise extension of D_i that fixes s. In particular
S_i is an LND. This is not a general rule that subtracting two LNDs
preserves local nilpotence: (5) is justified by the preserved
polynomial decomposition A[s]. A restriction D_i could be zero.

Form the polynomial determinant in the actual coordinates of (1):
\[
g=\det\bigl(E(x_j),K_1(x_j),K_2(x_j),K_3(x_j)\bigr)_{j=1}^4.
\tag{6}
\]
Subtracting h_i times the first column replaces K_i by S_i and
does not change g.

**Cross-frame certificate.** If g is not the zero polynomial, then
\[
\operatorname{ML}(A)=\mathbb C.
\tag{7}
\]

**Proof.** If f belongs to ML(A), then E(f)=0 and all S_i(f)=0,
so all K_i(f)=0. The coefficient matrix in (6) is invertible over
Frac(B). Thus every ambient coordinate partial kills f. A complex
polynomial killed by all four partials is constant. This proves (7).

The determinant actually belongs to A. The four columns commute
with E. Applying E to their coefficient matrix differentiates each
column by the Jacobian matrix of E, so
E(g)=(div E)g=0. An ambient LND has divergence zero: the Jacobian
of its polynomial additive flow is a unit in B[t], hence constant
and equal to one at t=0.

The certificate gives generic rank three on Spec(A), and hence an
open special-automorphism orbit. It need not give three commuting
intrinsic LNDs, a free individual action, a unit determinant, or a
slice. The former same-frame rank-three argument did have commuting
fields and obtained cancellation through a transitive vector-group
action. That stronger group argument must not be used here.

Thus (3) and the nonzero determinant in (6) are finitely checkable
sufficient data for ML triviality. Existence of such data for every
(1) has not been proved. Nor is this criterion asserted necessary
when ML(A)=C; that would require additional access to enough
intrinsic directions through coordinate LNDs on B.

## 3. Target-specific minimization within all affine-linear frames can fail

Here A=C[a,b,c] and B=A[s] really are polynomial. Fix integers
N>=2, M>=1 and k>=2 and take the actual coordinates
\[
x_1=a,\qquad x_2=b+a^ks^N,\qquad
x_3=c+bs^M,\qquad x_4=s.
\tag{8}
\]
Their inverse is
\[
a=x_1,\quad s=x_4,\quad b=x_2-x_1^kx_4^N,
\quad c=x_3-(x_2-x_1^kx_4^N)x_4^M.
\]
The four coordinate partials are
\[
\begin{aligned}
T_1&=\partial_a-ka^{k-1}s^N\partial_b
                     +ka^{k-1}s^{N+M}\partial_c,\\
T_2&=\partial_b-s^M\partial_c,\\
T_3&=\partial_c,\\
T_4&=\partial_s-Na^ks^{N-1}\partial_b
       +(Na^ks^{N+M-1}-Mb s^{M-1})\partial_c.
\end{aligned}
\tag{9}
\]
Their s-filtration degrees are, respectively,
N+M, M, 0, N+M-1. These four degrees are distinct. Hence for
every nonzero constant linear combination T=sum alpha_i T_i,
its intrinsic leading direction is a nonzero multiple of partial_c.
There is no hidden cancellation between equal highest degrees.

Every such T is itself a coordinate partial after a linear change
of the x-frame. Thus this statement covers every coordinate
translation in every affine-linear re-framing of (8), not just
the four displayed partials.

For the particular target f=a, T(f)=alpha_1. Whenever T moves f,
\[
q(T)=N+M,\qquad \deg_s T(f)=0,
\qquad D_{q(T)}(f)=0.
\tag{10}
\]
Every height minimizer among the entire constant translation space
that moves f has the same failure. The loss N+M is arbitrarily
large. Thus selecting a minimum-height translation that moves f
does not make its intrinsic top move f, even in an actual
polynomial cylinder.

All invariant replicas of these translations have the same
limitation. If h is nonzero with T(h)=0, then hT is an ambient
LND. Write h=s^r h_r+lower terms. Its intrinsic top is
h_r D_{q(T)}, so it still kills a. When T(a) is nonzero, the
degrees of (hT)(a) and of hT both increase by r, leaving the
same loss (10). This covers each such replica, not arbitrary
sums of replicas from different directions or their conjugates.

The underlying triangular rank-loss mechanism is inherited from
the earlier intrinsic-action and frame-minimization notes. The
additional assertion proved here is the entire affine-linear
orbit and target-minimum quantifier. It does not obstruct general
nonlinear changes: the inverse in (8) reaches the adapted frame.
The target a is not claimed to belong to the true ML(A), which
is C in this example. It is a false candidate surviving the
specified extraction procedure.

## 4. Different bad frames can nevertheless supply the certificate

In (8), set k=3, N=2, M=1. Its leading directions all span
partial_c. Cyclically permute (a,b,c) to obtain two further
frames whose directions all span partial_a and partial_b.
The T_1 from the respective frames gives the three intrinsic
LNDs
\[
3a^2\partial_c,\qquad 3b^2\partial_a,
\qquad 3c^2\partial_b.
\tag{11}
\]
Their coefficient determinant in (a,b,c) is
27a^2b^2c^2, which is nonzero. They therefore supply (6), up
to the harmless sign from placing E in the first column.

Each of the three input frames has leading rank one. No
single one of them supplies the earlier same-frame rank-three
certificate. Moreover the three displayed fields do not
commute, and all vanish at the origin. The computation gives
the ML conclusion using their combined generic rank; it does
not infer a free action from those particular fields.

## 5. Selecting the highest coefficient that moves f is not LND extraction

There is a different attempted repair of (10): retain the largest
coefficient D_j that actually moves f, discarding higher
coefficients that kill it. Even with T(f)=1 this can cease to
be locally nilpotent.

On the same genuine B=C[a,b,c,s], put
\[
u=a-s,\qquad \beta=b-sc,\qquad
\gamma=-sb+(1+s^2)c.
\tag{12}
\]
These and s are coordinates, with full inverse
\[
a=u+s,\qquad
b=(1+s^2)\beta+s\gamma,\qquad
c=s\beta+\gamma.
\tag{13}
\]
The matrix of the last two substitutions has determinant one;
(13), rather than that determinant alone, proves the coordinates.
Their actual partial T=partial_s, holding u,beta,gamma fixed, is
\[
T=\partial_s+\partial_a+
       (sb+(1-s^2)c)\partial_b+(b-sc)\partial_c.
\tag{14}
\]
Its intrinsic expansion has
\[
D_0=\partial_a+c\partial_b+b\partial_c,\quad
D_1=b\partial_b-c\partial_c,\quad D_2=-c\partial_b.
\tag{15}
\]
For f=a the largest index that moves f is zero, with D_0(f)=1.
But D_0^{2r}(b)=b and D_0^{2r+1}(b)=c for every r>=0.
It is not an LND. D_1 is not an LND either. The genuine top
D_2 is an LND but kills f. This is a failure of the proposed
function-targeted selection rule, not a failure of the inherited
highest-derivation-degree theorem.

## 6. Exact remaining hypothesis and verification

The main unresolved assertion is still that every (1) has enough
intrinsic LNDs to move every nonconstant candidate invariant.
For the concrete cross-frame route, a sufficient next result
would produce three actual coordinate LNDs satisfying (6).
Neither height minimization within one affine-linear orbit nor
function-targeted coefficient selection proves that result.

The two-sided inverses, the matrix derivative underlying (14),
the coordinate-partial identities, the nonzero determinant in
(11), and six instances of the recurrence in (15) were checked
with exact SymPy arithmetic. The all-degree and all-frame claims
use the written proofs above. These inline controls are not
additional unittest methods or a standalone suite.

A separate auditor subsequently reconstructed these identities in
the standalone [stable_polynomial_invariants_checks_pass32.py](stable_polynomial_invariants_checks_pass32.py).
Its six methods verify the cyclic full coordinate inverses, actual
coordinate partials, target-degree and replica controls, highest
adjoints and nonzero cross-frame determinant, noncommutation, and
the two-shear lower-coefficient recurrence. It imports only unittest
and SymPy. The author run passed in 0.147 seconds; a separate full-file
audit and run passed the same six methods in 0.137 seconds. These are
six new methods, not the sum of repeated runs or the inline controls.

```
/opt/anaconda3/bin/python research/stable_polynomial_invariants_checks_pass32.py
```

This note does not reuse a cylinder whose polynomiality is
unknown as a counterexample to (1), infer a worldwide literature
absence, or claim expert or proof-assistant verification.

[^ml]: Nikhilesh Dasgupta and Neena Gupta, [*An algebraic characterization of the affine three space*](https://arxiv.org/pdf/1709.00169), arXiv version 2, Lemma 3.1 and proof, PDF p. 5; Lemma 4.5 and Theorem 4.6 with proofs, PDF p. 9. The hypotheses in Theorem 4.6 are an affine three-dimensional UFD over an algebraically closed characteristic-zero field, plus ML(A)=C and ML*(A) different from A. The latter requires an intrinsic sliced LND. These exact statements were read directly; they do not assert descent of ML triviality from a polynomial cylinder.

[^filtration]: Bachar Alhajjar, [*LND-Filtrations and Semi-Rigid Domains*](https://arxiv.org/pdf/1501.00445), Proposition 2.2, PDF p. 4, and Proposition 3.4 with proof, PDF p. 7. The associated-graded mechanism and one-cylinder rigidity theorem were already used in [intrinsic-actions-pass.md](intrinsic-actions-pass.md). The highest-adjoint proof (3)-(5) is also written explicitly here so that no arbitrary lower coefficient is silently treated as an LND.
