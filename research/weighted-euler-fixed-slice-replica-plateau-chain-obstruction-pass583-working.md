# A fixed-slice replica plateau chain can stall in an actual translation frame

## 1. Statement and the exact permitted moves

There is an actual polynomial coordinate frame of
\[
 B=\mathbf C[a,b,c,u]=A[u],\qquad A=\mathbf C[a,b,c],
 \qquad E=\partial_u,
\tag{1}
\]
with positive coordinate degrees and weighted Euler complexity
\[
 \mathcal C=\left(\sum_i\deg_E X_i,\ \deg_E D\right)=(13,1),
\tag{2}
\]
for which the following fixed-slice procedure cannot reach a
strictly smaller pair by any finite nonincreasing chain.

At each step, recompute the weighted Euler derivation from the
actual coordinate degrees, recover its leading LND on \(A\),
extend that derivation to kill the same supplied slice \(u\),
and apply a polynomial replica of that extension. Every coefficient
in the full invariant ring with polynomial dependence on \(u\)
is allowed. Compare the pairs lexicographically after each move,
using the actual new degrees and the exact new Euler shift.

In this example the recovered extension is always
\[
 N=a\partial_b+b^2\partial_c,
\tag{3}
\]
for every permitted nonincreasing intermediate frame. It is
primitive and nonsliced. Every nonincreasing move is exactly
\(\exp(F_0N)\) for some \(F_0\in\ker_A N\), independent
of \(u\). Such moves leave the pair unchanged, and their
composition leaves the same obstruction in place.

The fixed slice, fixed rule for choosing the recovered direction,
and nonincrease at every step are essential restrictions. Arbitrary
slice changes, other LND directions, or steps that temporarily
increase the pair are not excluded. Indeed the example has a
visible homogeneous coordinate slice \(u\), an already polynomial
kernel, and an explicit escape using other directions. It does
not refute a strategy that first tests for a homogeneous slice,
nor a general coordinate-entry or cancellation statement. No
global minimality or novelty claim is made.

## 2. Whole actual frame and inverse

Take
\[
 \begin{split}
 X&=u,\qquad Y=a+u^2,\qquad Z=b+au+u^4,\\
 W&=c-\frac13b^2u+\frac13ab u^2-\frac13a^2u^3+u^6.
 \end{split}
\tag{4}
\]
An entire polynomial inverse is given successively by
\[
 \begin{split}
 U&=X,\qquad a_*=Y-U^2,\qquad b_*=Z-a_*U-U^4,\\
 u&=U,\qquad a=a_*,\qquad b=b_*,\\
 c&=W+\frac13b_*^2U-\frac13a_*b_*U^2
                   +\frac13a_*^2U^3-U^6.
 \end{split}
\tag{5}
\]
The forward composition first recovers \(U=u\), then \(a,b\),
then \(c\). The reverse composition recovers \(X,Y,Z,W\)
in the same order. Both are identities on the whole fourfold,
with no localization. The coordinate Jacobian in the ordered
variables \((a,b,c,u)\) is \(-1\).

The exact \(E\)-degrees of (4) are \((1,2,4,6)\), all with
leader one. The weighted Euler derivation of this actual frame is
\[
 D=X\partial_X+2Y\partial_Y+4Z\partial_Z+6W\partial_W.
\tag{6}
\]
Differentiating the full inverse, or checking the four entire
Euler eigen-equations, gives
\[
 D=D_A+uE+uN,\qquad
 D_A=2a\partial_a+4b\partial_b+6c\partial_c,
 \qquad N=a\partial_b+b^2\partial_c.
\tag{7}
\]
In particular \(D(a)=2a\), \(D(b)=4b+au\),
\(D(c)=6c+b^2u\), and \(D(u)=u\). The terms of degrees
two and three appearing in the last row of (4) are retained
in these identities.

The product rule proves the all-ring shift bound
\(\deg_E Df\le\deg_E f+1\), and equality occurs on \(b\).
Thus \(\delta=1\), and on the entire graded ring \(A[\eta]\)
the induced derivation is \(\eta N\). Equivalently,
\[
 [E,D]=E+N,\qquad [E,[E,D]]=0.
\tag{8}
\]
The commutator convention is \([P,Q]=PQ-QP\). Subtracting
\([E,D](u)E=E\) recovers exactly (3), extended to kill \(u\).
Thus the direction used below is the genuine recovered direction,
not an arbitrary choice from the LNDs of the known polynomial ring.

## 3. Primitivity, absence of a slice, and the full replica flow

The derivation \(N\) is locally nilpotent: assign weights zero,
one, and three to \(a,b,c\). Every nonzero image under \(N\)
has strictly smaller weight. Its component gcd is
\(\gcd(a,b^2)=1\), so no nonconstant polynomial factor can
be removed by primitive normalization. Every image satisfies
\[
 N(f)=a f_b+b^2 f_c\in(a,b^2)\subset A.
\tag{9}
\]
This is a proper ideal, so \(N(f)=1\) has no polynomial
solution. The common-zero locus is the line \(a=b=0\), with
\(c\) arbitrary. Hence the recovered direction is primitive
and has no slice.

Write \(S=\ker_A N\). No finite generating set for \(S\)
is needed: throughout, every element of the full kernel is
allowed. For example \(a\) and \(3ac-b^3\) belong to \(S\).
For any \(F\in S[u]\), the multiplier is killed by \(N\),
so \(FN\) is locally nilpotent. The entire automorphism
\(\alpha_F=\exp(FN)\) is
\[
 \begin{split}
 \alpha_F(a)&=a,\qquad \alpha_F(u)=u,\\
 \alpha_F(b)&=b+aF,\\
 \alpha_F(c)&=c+b^2F+abF^2+\frac13a^2F^3.
 \end{split}
\tag{10}
\]
Its inverse is \(\alpha_{-F}\). These statements follow from
\(N(F)=0\), \(N^2(c)=2ab\), \(N^3(c)=2a^2\), and
\(N^4(c)=0\). In particular the entire inverse is polynomial
even when the invariant coefficients of \(F\) depend on \(c\).
The flow fixes \(F\), so no substitution ambiguity is involved.

On the full coordinate frame, (10) gives
\[
 \begin{split}
 \alpha_F(X)&=X,\qquad \alpha_F(Y)=Y,\\
 \alpha_F(Z)&=Z+aF,\\
 \alpha_F(W)&=W+
 F\left(b^2-\frac23ab u+\frac13a^2u^2\right)
 +F^2\left(ab-\frac13a^2u\right)+\frac13a^2F^3.
 \end{split}
\tag{11}
\]
Thus every replica under consideration is an actual polynomial
coordinate change with a full inverse, not just a change of the
coordinate initials.

## 4. Every degree-sum-nonincreasing replica has degree at most two

Let \(I=(a,b)\subset A\). All components of \(N\) lie in
\(I\), and \(N(I)\subseteq I\). Therefore every replica
\(\alpha_F\) acts as the identity modulo \(I[u]\). The
entire frame (4) modulo that ideal is
\[
 (X,Y,Z,W)\bmod I[u]=(u,u^2,u^4,c+u^6).
\tag{12}
\]
Every original coordinate degree survives in this quotient.
Consequently no replica can reduce any one of the four global
\(E\)-degrees. This argument uses the whole frame and does
not assume anything about the invariant coefficients of \(F\).

If \(F\ne0\), let \(k=\deg_u F\) and let \(F_k\in S\)
be its nonzero leader. For \(k>2\), the term
\(a^2F^3/3\) in (11) has degree \(3k>6\). Every other
added term has degree at most \(k+2\) or \(2k+1\), both
strictly smaller than \(3k\). Its leader \(a^2F_k^3/3\)
is nonzero in the domain \(A\). Hence the new \(W\)-degree
is \(3k>6\); together with (12), the degree sum strictly
increases.

For \(k\le2\), the degree of \(Z+aF\) is exactly four.
The degree of the last row is at most six, and at \(k=2\)
its leading coefficient is
\[
 1+\frac13a^2F_2^3\ne0.
\tag{13}
\]
Equality to zero would make the nonunit \(a\) a unit in
\(A\). At \(k<2\), the leader is one. Thus, with \(F=0\)
included separately, the degree tuple is unchanged exactly
in the sum-nonincreasing range:
\[
 \deg_uF\le2\quad\Longrightarrow\quad
 (\deg_E\alpha_F(X_i))=(1,2,4,6).
\tag{14}
\]
Conversely, every \(\deg_uF>2\) increases the sum. In
particular a lexicographic improvement cannot occur through
a degree decrease that offsets an increase of another coordinate.

## 5. Constant coefficients are filtered equivariances

Write \(F=F_0+G\), with \(F_0\in S\) and \(G\in uS[u]\).
The two invariant-multiple derivations commute, giving
\[
 \alpha_F=\beta\alpha_G,\qquad \beta=\exp(F_0N).
\tag{15}
\]
The automorphism \(\beta\) restricts to an automorphism of
\(A\), fixes \(u\), and commutes with both \(E\) and \(N\).
It fixes every element of \(S\). It therefore preserves the
exact \(E\)-degree of every nonzero polynomial, and preserves
the exact filtration shift of every derivation by conjugation.

Consequently the degree tuples for \(\alpha_F(X_i)\) and
\(\alpha_G(X_i)\) agree. Their actual Euler fields are
conjugate by \(\beta\), because their actual weights agree,
so their exact Euler shifts agree as well. This reasoning is
valid even when a replica changes the original degree tuple.
Thus the entire pair is unaffected by removing \(F_0\).

For the only remaining nonincreasing candidates, we may therefore
write
\[
 F=uF_1+u^2F_2,\qquad F_1,F_2\in S,
\tag{16}
\]
including either coefficient being zero. The actual weights
are still \((1,2,4,6)\), so their true new Euler derivation is
\(D_F=\alpha_FD\alpha_F^{-1}\). We do not use this old-weight
conjugation as the recomputed Euler field when the degrees change.

## 6. The entire second-order obstruction

Define the full horizontal commutators
\[
 K=[N,D_A]=2a\partial_b-2b^2\partial_c,
 \qquad J=[N,K]=-8ab\partial_c.
\tag{17}
\]
Since \(N\) kills \(u\), the derivation \(FN\) for (16)
raises \(u\)-adic order by at least one; \(D\) preserves
that order. Thus commutators of order at least three cannot
contribute to the coefficient of \(u^2\) in \(D_F|_A\).
The first two commutators give exactly
\[
 \begin{split}
 T_2:=[u^2]D_F|_A
 &=F_2K-(D_AF_2+2F_2)N
             +\frac12F_1^2J-F_1K(F_1)N.
 \end{split}
\tag{18}
\]
Here \(D_AF_i\) and \(K(F_i)\) need not be in \(S\).
To verify the quadratic term directly, the first-order
commutator is
\(u\{F_1K-(D_AF_1+F_1)N\}\). Commuting once more with
\(uF_1N\), using \(N(F_1)=0\) and
\(N(D_AF_1)=K(F_1)\), gives
\(u^2\{F_1^2J-2F_1K(F_1)N\}\). Its factor one-half
in the exponential yields the last two terms of (18).
The \(-2F_2N\) term comes from the vertical Euler field
\(uE\). No moving coefficient has been dropped.

Put \(Q=D_AF_2+F_1K(F_1)\). The two complete components
of (18) are
\[
 T_2(b)=-aQ,\qquad
 T_2(c)=-b^2Q-4b^2F_2-4abF_1^2.
\tag{19}
\]
If the new exact Euler shift is at most one, then every
element of \(A\) has image of \(u\)-degree at most one,
so \(T_2=0\). Since \(A\) is a domain and \(a,b\) are
nonzero elements of it, (19) successively gives
\[
 Q=0,\qquad bF_2+aF_1^2=0.
\tag{20}
\]
Apply \(N\) to the second identity. Both \(F_i\) are in
\(S\), \(N(a)=0\), and \(N(b)=a\), so it gives
\(aF_2=0\). Hence \(F_2=0\), and then \(F_1=0\).
No division by a value of \(a\) or \(b\) at a point, and
no division by a potentially zero \(F_i\), has been used.

It follows that every replica with any nonzero coefficient of
positive \(u\)-degree either increases the degree sum or
keeps that sum at 13 and increases the exact shift above one.
Conversely, every \(F\in S\) independent of \(u\) preserves
the pair by Section 5. We have proved the exact classification
\[
 \mathcal C\bigl(\alpha_F(X_i)\bigr)\le_{\rm lex}(13,1)
 \quad\Longleftrightarrow\quad F\in S.
\tag{21}
\]
In the latter case the pair is equal to \((13,1)\), never
strictly smaller.

## 7. Why recomputing the direction cannot escape this plateau

The classification (21) alone would only be a one-step result.
Here it persists along every allowed chain. For \(H\in S\)
write \(\beta_H=\exp(HN)\). Its changed Euler field is
\[
 D_H=\beta_HD\beta_H^{-1}
     =\beta_HD_A\beta_H^{-1}+uE+uN.
\tag{22}
\]
The first summand preserves \(A\) and kills \(u\), since
\(\beta_H\) is an automorphism of \(A\) fixing \(u\).
Thus this full field still has exact shift one and induced
derivation \(\eta N\). Its corrected recovery using the
same supplied slice \(u\) is exactly \(N\), not a new
direction. It remains primitive; allowing a nonzero complex
rescaling does not change its replica family.

For every \(F\in S[u]\), the automorphisms \(\alpha_F\)
and \(\beta_H\) commute. The pair of the frame
\(\alpha_F\beta_H(X_i)=\beta_H\alpha_F(X_i)\) equals
the pair of \(\alpha_F(X_i)\), by the filtered equivariance
of Section 5. Therefore a nonincreasing step from the frame
\(\beta_H(X_i)\) is again possible only when \(F\in S\).
It then leads to \(\beta_{H+F}(X_i)\).

Induction proves that every finite nonincreasing chain has this
form at every stage and has constant complexity \((13,1)\).
No such chain can reach a strictly smaller pair. This proves
the statement for recomputed recovered directions, not merely
for repeated use of an unexamined original vector field.

The fixed slice is important. If it were replaced by
\(u+q\), \(q\in A\), the extension of the recovered
derivation killing that new slice would be \(N-N(q)E\).
That is outside the fixed-\(u\) family proved obstructed here.
The argument also does not address chains that allow a temporary
increase of the pair.

## 8. Explicit escape outside the restricted procedure

The example is not a coordinate-entry obstruction. The visible
coordinate \(u=X\) is already a homogeneous slice of weight
one. A strategy that tests for a homogeneous slice first
recognizes this example immediately, before any replica chain.
The kernel is the known polynomial ring \(A\), and the old
coordinate frame has degrees \((0,0,0,1)\). An all-positive
frame \((u,a+u,b+u,c+u)\) has sum four. Both are linked to
(4) by the complete inverse (5).

For a more specific escape, let
\[
 L=a\partial_b=\frac12N+\frac14[N,D],
 \qquad P=b^2\partial_c=N-L.
\tag{23}
\]
These are LNDs in the complex Lie algebra generated by \(E,D\),
because \(N=[E,D]-E\) and \([N,D]=K\). So are
\[
 [L,P]=2ab\partial_c,\qquad
 [L,[L,P]]=2a^2\partial_c.
\tag{24}
\]
The first actual automorphism \(\exp(-uL)\) sends (4) to
\[
 \left(u,\ a+u^2,\ b+u^4,
       c-\frac13b^2u+ab u^2-a^2u^3+u^6\right).
\tag{25}
\]
Next translate \(c\) by
\(b^2u/3-ab u^2+a^2u^3\), fixing \(a,b,u\). This is a
polynomial automorphism with the opposite translation as its
inverse. It can also be written as commuting replica flows
of the three vertical LND directions in (23),(24), since its
generator is
\[
 \frac u3P-\frac{u^2}{2}[L,P]
                   +\frac{u^3}{2}[L,[L,P]].
\tag{26}
\]
The resulting whole frame is
\[
 (u,\ a+u^2,\ b+u^4,\ c+u^6),
\tag{27}
\]
whose Euler field is \(D_A+uE\), of exact shift zero.
Every displayed map has a polynomial inverse. These steps use
directions other than the fixed-slice recovered direction, and
no nonincrease claim is made for their intermediate pair.
The example does not show that Lie-generated directions fail
to escape, or that they always succeed.

## 9. Verification and status

Fresh unsaved algebra reconstructs both entire inverse orders,
the Jacobian, all Euler eigen-equations, the full replica flow,
the commutators (17), both complete components (19) with generic
invariant coefficients, and the explicit escape (25)--(27).
The proof of (21) and its finite-chain extension covers all
\(F\in S[u]\); it is not inferred from sampled coefficient
values or a bounded search through chains.

No saved checker was executed, imported, compiled or rerun,
and no canonical record was edited. Author verification is
not an independent saved-source audit. The conclusion concerns
the explicit fixed-slice, nonincreasing replica-only procedure.
It is not a claim about globally minimizing frames, arbitrary
slice rechoice, an eigen-slice-first strategy, unrestricted Lie
directions, or general cancellation. No novelty is asserted.
