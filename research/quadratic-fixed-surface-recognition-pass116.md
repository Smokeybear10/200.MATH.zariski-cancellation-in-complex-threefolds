# Recognition through the fixed surface of the quadratic conic

In the supplied quadratic frame, the conic has a smooth irreducible
fixed surface. Showing that this surface is an affine plane is
equivalent to several concrete coordinate and linearization criteria,
and any of them recognizes the threefold. The odd-row argument gives
an elementary coordinate implication if its good odd column vanishes.
A subsequent scope check shows that this vanishing is already excluded
in the exact relative-degree-two branch. That conditional implication
is not a newly recognized nonempty part of the unresolved branch.

## 1. Precise hypotheses

Retain the complete actual-frame hypotheses of
[the global conic theorem115](quadratic-global-conic-frontier-pass115.md).
Use different symbols for the surface and its coordinate ring:

\[
\begin{gathered}
S=\mathbb C[s,t],\quad 0\ne P\in S,\quad \eta\in S,\qquad
A=S[U,r]/(r^2-2PU+\eta),\\
B=A[u]\simeq\mathbb C^{[4]},\quad
C_0=S[U],\quad C=C_0[u],\quad F=2PU-\eta,\\
D_0=C_0/(F)=A/(r),\quad D=\operatorname{Spec}D_0,\\
N(U)=r,\quad N(r)=P,\quad N|_S=0,\qquad
N(\ker N^2)=PS.
\end{gathered}
\tag{1}
\]

Here C0 is a polynomial ring in three variables, not a formal
coefficient ring. The last image in (1) is taken inside A. Every
irreducible element of S remains prime in A, as retained in the
actual-frame divisor hypotheses. The cylinder implies that A is
smooth. No statement below puts an arbitrary cancellation input into
these additional hypotheses.

## 2. Primitivity, irreducibility and smoothness

Suppose an irreducible p of S divided both P and eta. Equation (1)
would give r squared in pA. Since pA is prime, r belongs to pA; hence
h=r/p is an actual element of A. Applying N twice gives

\[
N(h)=P/p\in S,\qquad N^2(h)=0,\qquad
P/p\in PS\quad\Longrightarrow\quad 1/p\in S,
\tag{2}
\]

which is impossible. Therefore gcd(P,eta)=1. This is a gcd statement,
not an assertion that the ideal (P,eta) is the unit ideal. In
particular it does not exclude their common closed zeros.

The polynomial F is primitive as a polynomial in U over the UFD S.
Over Frac(S) it has degree one, so Gauss's lemma makes it irreducible
in C0. Thus F is prime, D0 is a domain of dimension two, and r is
prime in both A and B. If eta is zero, the same gcd assertion makes
P a unit; the presentation then already gives A=S[r]. No separate
argument with a nonzero eta is needed in this boundary case.

If a closed point of D were singular, all three partial derivatives
of F would vanish there. Adjoining r=0 gives a point of A where
all four partial derivatives of r squared minus F vanish, contrary
to smoothness of A. Consequently D is a smooth irreducible affine
surface. It is nonempty, since F is a nonconstant nonunit polynomial.
None of these conclusions asserts that D is an affine plane.

## 3. The actual sign involution

There is a genuine automorphism sigma of B which fixes C and sends
r to minus r. Its construction needs only the monic presentation;
its interpretation as a polynomial automorphism of four-space uses
the supplied equality \(B\simeq\mathbb C^{[4]}\). The free decomposition gives

\[
B=C\oplus Cr,\qquad B^\sigma=C,\qquad
(a-\sigma(a):a\in B)=rB,\qquad
\operatorname{Fix}(\sigma)=D\times\mathbb A^1_u.
\tag{3}
\]

It commutes with E=partial_u and reverses N. In particular N does
not generally descend to D0: N(r)=P need not belong to (r). An
additive action on A cannot simply be assigned to its fixed surface.

The quotient map to Spec C is a finite flat double cover with branch
F=0. Having a polynomial quotient does not already provide a
polynomial conjugation of sigma to a linear map. The
[source gate116](quadratic-involution-recognition-source-gate-pass116.md)
separates this issue from local holomorphic linearization.

## 4. Equivalent sufficient criteria

Within (1), the following five statements are equivalent:

\[
\begin{array}{ll}
\mathrm{(a)}&D_0\simeq\mathbb C^{[2]},\\
\mathrm{(b)}&C_0=\mathbb C[F]^{[2]},\\
\mathrm{(c)}&C=\mathbb C[F]^{[3]},\\
\mathrm{(d)}&\sigma\text{ is polynomially linearizable on }B,\\
\mathrm{(e)}&B=\mathbb C[r]^{[3]}.
\end{array}
\qquad
\text{Each implies }A=\mathbb C[r]^{[2]}.
\tag{4}
\]

Here equality notation means actual polynomial coordinates over the
indicated subring. It is stronger than an abstract isomorphism that
forgets F or r. The implications are as follows.

For (a) to (b), apply the Sathaye--Russell linear-plane theorem to
F=2PU-eta in S[U]. Its coefficient of U is nonzero and S is a
polynomial plane. Thus a plane quotient makes this particular F an
actual coordinate of C0. The linearity in U is essential; no general
affine-plane embedding conjecture is used. The precise statement,
including its stronger simultaneous-coordinate version, is recorded
in the primary research restatement cited below.[^linear]

Statement (b) gives (c) just by adjoining u. If (c) holds, choose
\(C=\mathbb C[F,y_1,y_2,y_3]\). Eliminating F in B=C[r]/(r squared-F) gives
\(B=\mathbb C[r,y_1,y_2,y_3]\), with sigma fixing each yi and changing the sign
of r. This proves (d).

For (d) to (e), diagonalize the resulting linear involution. Its
fixed scheme has dimension three by (3), so exactly one eigenvalue
is negative. Call its eigen-coordinate w. The fixed ideal is then
(w), which equals (r). Since the only units of B are nonzero
complex constants, r is a constant multiple of w and is an actual
coordinate. This compares scheme-theoretic fixed ideals, not just
their closed-point sets.

Finally, (e) gives \(D_0[u]=B/(r)\simeq\mathbb C^{[3]}\). The affine-plane cancellation
theorem gives \(D_0\simeq\mathbb C^{[2]}\), proving (a). The theorem used is specifically
that the affine plane is a Zariski factor; no assertion that arbitrary
surfaces cancel is needed.[^surface]

To see the final recognition assertion directly, (b) gives actual
elements X,Y with \(C_0=\mathbb C[F,X,Y]\). Substitution in the original conic
gives the isomorphism, with inverse induced from these coordinates,

\[
A=\mathbb C[F,X,Y,r]/(r^2-F)=\mathbb C[r,X,Y].
\tag{5}
\]

No theorem about affine-plane fibrations over the r-line is needed
for this chain. We do not assert the converse that \(A\simeq\mathbb C^{[3]}\), without
preserving r, forces all five statements in (4).

## 5. A coordinate conditional and its exact scope

In the actual original coordinates, write the three good coordinates
as x_tr=bu+dU+er+f with b,d,e,f in S cubed, and use the fourth
coordinate from theorem115. The
[odd-row proof116, Section 4](quadratic-involution-odd-row-pass116.md)
proves that e=0 gives a nonzero complex constant k1 and a polynomial
H in the three actual x-coordinates such that

\[
r=(z-H(x_1,x_2,x_3)/2)/k_1,\qquad
z=k_1r+H(x_1,x_2,x_3)/2.
\tag{6}
\]

These are explicit inverse triangular substitutions, so (e) holds.
Equation (4) therefore recognizes A as affine three-space. The same
conclusion follows if b and e are generically proportional, since
the odd-row proof first shows that this forces e=0. At every closed
base point they are either independent or e vanishes; nonzero
proportionality is excluded.

However, the exact remaining quadratic branch has an additional
retained constraint. The [generic two-generator proof90](nonconical-cubic-relation-pass90.md)
gives \(A_K=K[y_1,y_2]=K[r]\), where y is an affine K-linear
reexpression of dU+er+f, and its defining plane relation has degree
exactly two in this branch. If d,e are dependent with d nonzero,
both y's belong to K[V] for a quadratic polynomial V in r. That
proper subring cannot contain r. If d=0, both y's have degree at
most one in r, so their plane relation is linear. These alternatives
show that d,e are generically independent in the exact quadratic
branch. With the retained volume restrictions, this also gives
\(\det[b,d,e]\ne0\).

In particular e=0 is already excluded in that branch. The coordinate
implication (6) is valid under the broader displayed conic/frame
hypotheses, but it must not be counted as a new nonempty solved case.
The [intrinsic-shift proof116](quadratic-intrinsic-shift-odd-row-pass116.md)
records the fuller scope check and the useful new restrictions at
closed points where the generic determinant drops rank.

The fixed-surface criterion is a conditional theorem, not a proof
that every supplied quadratic frame is recognized. Neither the
coefficient argument nor the surface criterion recognizes the
remaining generically independent-column case.
The relative cubic branch and an entry theorem for arbitrary sliced
actions are also still missing. These obligations remain part of
the original cancellation goal.

## Sources and confidence limits

[^linear]: P. Ghosh, N. Gupta and A. Pal, [*On the family of affine threefolds a(x)y=F(x,z,t)*, arXiv:2403.17397v2, Introduction](https://arxiv.org/html/2403.17397v2#S1), 3 August 2024. The two paragraphs following Question 3 restate the Sathaye--Russell linear-plane theorem. This use is a statement-level application, not a claimed new proof of that published theorem.

[^surface]: H. Flenner, S. Kaliman and M. Zaidenberg, [*Cancellation for surfaces revisited. I*, arXiv:1610.01805v2, Introduction, printed pp. 2--3](https://arxiv.org/pdf/1610.01805v2), 26 December 2017. The definition of a Zariski factor and the explicit affine-plane theorem immediately before Theorem 0.3 were checked. This is a primary research restatement, not a fresh reconstruction of the original surface-cancellation proof. The general non-cancellation examples later in that introduction do not contradict the plane-specific statement.

Equations (2), (3), the elementary implications in (4), and (5)--(6)
are written deductions under the stated hypotheses. Symbolic checks
of conjugation or triangular substitutions cannot certify these
global hypotheses or the two published theorems. Independent AI
reviews are not human expert review, formal verification or novelty
clearance. No public novelty claim or submission is made.
