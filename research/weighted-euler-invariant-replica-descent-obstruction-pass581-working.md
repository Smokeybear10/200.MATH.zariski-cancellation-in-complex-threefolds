# Every invariant-coefficient replica can fail to lower the Euler degree pair

## 1. Exact bounded conclusion

There is an actual polynomial translation frame with all coordinate
degrees positive for which the recovered Euler-induced derivation
\(N\) is primitive and has no slice, and no automorphism
\[
 \alpha_F=\exp(F\widetilde N),\qquad
 F\in(\ker_A N)[u],
\tag{1}
\]
lowers the lexicographic pair
\[
 \left(\sum_i\deg_E X_i,\ \deg_E D\right).
\tag{2}
\]
Here \(E=\partial_u\), \(A=\ker E\), \(\widetilde N\) is the
extension of \(N\) killing \(u\), and \(D\) is the weighted Euler
derivation whose weights are the actual coordinate \(E\)-degrees.
After every coordinate change, the weights and the exact shift
in (2) are recomputed in the changed actual frame.

The coefficient \(F\) in (1) is an arbitrary invariant-coefficient
polynomial, not merely an element of \(\mathbf C[u]\). The failure
is therefore not removed by allowing all polynomial replicas of
this particular recovered direction. A different, explicitly
Lie-generated LND does lower the pair in the same example.

The invariant ring in this control is a known polynomial ring;
the displayed frame is not globally degree-minimizing. The result
does not obstruct arbitrary polynomial coordinate changes or a
sequence using new directions. It asserts no cancellation or
coordinate-entry theorem and makes no novelty claim. Sources576,
577, and578 provide the context; the whole control and its
obstruction are proved directly below.

## 2. Actual frame, full inverse, and entire Euler derivation

Work in
\[
 B=\mathbf C[a,b,c,u]=A[u],\qquad A=\mathbf C[a,b,c],
 \qquad E=\partial_u.
\tag{3}
\]
Define the four actual polynomials
\[
 X=u,\qquad Y=a+u^2,\qquad Z=b+au+u^4,\qquad
 W=c+\left(b+\frac15\right)u+\frac12au^2+u^6.
\tag{4}
\]
Their entire polynomial inverse is
\[
 \begin{split}
 u&=X,\qquad a=Y-X^2,\\
 b&=Z-(Y-X^2)X-X^4,\\
 c&=W-\left(Z-(Y-X^2)X-X^4+\frac15\right)X
             -\frac12(Y-X^2)X^2-X^6.
 \end{split}
\tag{5}
\]
Substituting (4) in (5) recovers \(u,a,b,c\), and substituting
(5) in (4) recovers \(X,Y,Z,W\). Both compositions are polynomial
identities on the whole fourfold. The Jacobian of (4) in the
ordered variables \((a,b,c,u)\) is \(-1\).

The exact degrees and their leaders are
\[
 (d_X,d_Y,d_Z,d_W)=(1,2,4,6),\qquad
 (\operatorname{lc}_uX,\operatorname{lc}_uY,
   \operatorname{lc}_uZ,\operatorname{lc}_uW)=(1,1,1,1).
\tag{6}
\]
The corresponding actual weighted Euler derivation is
\[
 D=X\partial_X+2Y\partial_Y+4Z\partial_Z+6W\partial_W.
\tag{7}
\]
Applying it to the complete inverse gives
\[
 D(a)=2a,\qquad D(b)=4b+au,\qquad
 D(c)=6c+(b+1)u,\qquad D(u)=u.
\tag{8}
\]
For example, the last nontrivial equation follows from
\(D(W)=6W\): after the known \(D(a),D(b),D(u)\) terms
are collected, it reads
\(6W=D(c)+(5b+1/5)u+3au^2+6u^6\).
Comparing with (4) gives the asserted \(D(c)\).

Consequently the entire polynomial field is
\[
 D=D_A+uE+uN,\qquad
 D_A=2a\partial_a+4b\partial_b+6c\partial_c,
 \qquad N=a\partial_b+(b+1)\partial_c.
\tag{9}
\]
We use \(N\) for its extension killing \(u\) as well. Formula
(9) proves the all-ring bound \(\deg_E Df\le\deg_E f+1\).
Equality occurs for \(b\), so the exact shift is one. Thus
the pair in (2) is initially \((13,1)\).

The full commutators, with \([P,Q]=PQ-QP\), are
\[
 [E,D]=E+N,\qquad [E,[E,D]]=0.
\tag{10}
\]
Subtracting \([E,D](u)E=E\) recovers precisely the extension
of \(N\) killing the given slice. This is the actual recovery
operation of577, not a separately chosen leading vector field.
Equivalently, the induced derivation on
\(\operatorname{gr}_E B=A[\eta]\) is \(\eta N\).

## 3. A primitive nonsliced direction and its complete replica family

The derivation \(N\) satisfies
\[
 N(a)=0,\qquad N(b)=a,\qquad N(c)=b+1.
\tag{11}
\]
It is nonzero and locally nilpotent: assigning weights zero,
one, and two to \(a,b+1,c\), respectively, makes every nonzero
image have strictly smaller weight. Its component gcd is
\(\gcd(a,b+1)=1\), so no nonconstant polynomial factor can
be removed by primitive normalization. But every image satisfies
\[
 N(f)=a f_b+(b+1)f_c\in I:=(a,b+1)\subset A.
\tag{12}
\]
The ideal \(I\) is proper. Therefore \(N\) has no slice,
and its common-zero locus is the line \(a=0,b=-1\), with
\(c\) arbitrary. Set
\[
 S=\ker_A N,\qquad a,\ 2ac-(b+1)^2\in S.
\tag{13}
\]
No description of generators of \(S\) is needed below; every
element of this full kernel is allowed as a replica coefficient.

For every \(F\in S[u]\), \(N(F)=0\), so \(FN\) is locally
nilpotent and \(\alpha_F=\exp(FN)\) is a polynomial automorphism
with inverse \(\alpha_{-F}\). Its exact action on the actual
frame is
\[
 \alpha_F(X)=X,\qquad \alpha_F(Y)=Y,\qquad
 \alpha_F(Z)=Z+aF,\qquad
 \alpha_F(W)=W+(b+1)F+auF+\frac12aF^2.
\tag{14}
\]
Here \(N^2(Z)=0\), \(N(W)=b+1+au\), \(N^2(W)=a\),
and \(N^3(W)=0\). Thus (14) is the whole exponential, including
its quadratic term. It describes every replica in (1), with
arbitrary coefficient functions in the full invariant ring.

## 4. Exact degree control for every invariant polynomial coefficient

The case \(F=0\) changes nothing. Otherwise write
\(F=\sum_{j=0}^k F_j u^j\), with \(F_j\in S\),
\(F_k\ne0\). Since \(a\) is a nonunit of the polynomial
ring \(A\), neither
\[
 1+aF_k=0\qquad\hbox{nor}\qquad 1+\frac12aF_k^2=0
\tag{15}
\]
can hold in \(A\). Either equation would make \(a\) a unit.
This retains all special polynomial coefficients in \(S\),
not just constants.

Using (14), the exact degrees of the changed \((Z,W)\) are
\[
 \begin{array}{c|c|c}
  k & (\deg_E\alpha_F(Z),\deg_E\alpha_F(W))
       &\sum_i\deg_E\alpha_F(X_i)\\ \hline
  0\le k\le3 &(4,6)&13\\
  k=4 &(4,8)&15\\
  k>4 &(k,2k)&3+3k.
 \end{array}
\tag{16}
\]
At \(k=3\), the possible leader \(1+aF_3^2/2\) of the
changed \(W\) is nonzero by (15). At \(k=4\), the leader
\(1+aF_4\) of the changed \(Z\) is also nonzero, and
\(aF_4^2/2\ne0\) is the degree-eight leader of the changed
\(W\). The remaining cases follow from the distinct powers
in (14) and the domain property.

There is also a useful whole-quotient check: the replicas act
as the identity modulo \(I[u]\), because all components of
\(N\) lie in \(I\) and \(N(I)\subseteq I\). The original
frame modulo this ideal is
\((u,u^2,u^4-1,c+u^6-4u/5)\), retaining all four original
degrees. Thus no replica can lower any of them.

In particular no replica reduces any coordinate degree. A strict
lexicographic improvement of (2) can only occur when \(k\le3\)
and the new Euler shift becomes zero. All degrees remain positive
in every case.

## 5. Removing the constant coefficient does not change the test

Write \(F=F_0+G\), where \(G\in uS[u]\). The derivations
\(F_0N\) and \(GN\) commute, so
\[
 \alpha_F=\beta\gamma,\qquad
 \beta=\exp(F_0N),\quad \gamma=\exp(GN).
\tag{17}
\]
The automorphism \(\beta\) restricts to an automorphism of
\(A\) and fixes \(u\), hence it commutes with \(E\) and
preserves the exact \(E\)-degree of every nonzero polynomial.
It therefore preserves both coordinate degrees and the exact
filtration shift of a derivation under conjugation.

More explicitly, when the coordinate weights are unchanged,
the Euler derivations of the frames \(\alpha_F(X_i)\) and
\(\gamma(X_i)\) are respectively
\(\beta\gamma D\gamma^{-1}\beta^{-1}\) and
\(\gamma D\gamma^{-1}\). Their shifts are equal because
\(\beta\) is a filtration-preserving automorphism with a
filtration-preserving inverse. Thus a constant coefficient
\(F_0\), however complicated in \(S\), cannot affect the
descent question. We may assume \(F_0=0\).

## 6. A first-order Lie obstruction to shift zero

Assume now \(\deg_uF\le3\) and \(F_0=0\). By (16) the
weights remain \((1,2,4,6)\), so the actual new Euler field is
\[
 D_F=\alpha_FD\alpha_F^{-1}.
\tag{18}
\]
Write \(F=uF_1+O(u^2)\), with \(F_1\in S\); \(F_1=0\)
is allowed. Direct computation from (9) gives
\[
 [N,D_A]=2N+4\partial_c.
\tag{19}
\]
Modulo \(u^2\), the conjugation in (18) is exactly its first
commutator. Indeed \(FN\) raises \(u\)-adic order by at least
one, kills \(u\), and \(D\) preserves \(u\)-adic order.
All second and later commutators applied to \(A\) have order
at least two. Therefore the coefficient of \(u\) in
\(D_F|_A\) is
\[
 \begin{split}
 M_1
 &=N+F_1[N,D_A]-(D_AF_1+F_1)N\\
 &=(1-D_AF_1+F_1)N+4F_1\partial_c.
 \end{split}
\tag{20}
\]
The term \(-F_1N\) in the first line comes from the vertical
Euler field \(uE\). No assumption that \(D_AF_1\) belongs to
\(S\) is made; all identities in (20) are identities in \(A\).

If the new exact shift were zero, then \(D_F(A)\subseteq A\),
so \(M_1\) would vanish. Put \(Q=1-D_AF_1+F_1\). Its
components would give
\[
 0=M_1(b)=aQ,\qquad
 0=M_1(c)=(b+1)Q+4F_1.
\tag{21}
\]
Since \(A\) is a domain and \(a\ne0\) as an element of it,
the first identity gives \(Q=0\), and the second gives
\(F_1=0\). But then \(Q=1\), a contradiction. There was
no division by a value of \(a\) at a point.

Thus the new shift is not zero. The Euler field of an
all-positive frame has nonnegative exact shift, since each
coordinate is a nonzero eigenvector of unchanged degree.
Consequently \(\deg_E D_F\ge1\), which finishes the proof
that no replica (1) lowers the pair \((13,1)\).

The first-order obstruction is a failure of collinearity:
\(N\wedge[N,D_A]=4a\,\partial_b\wedge\partial_c\ne0\).
The scalar multiplication and the \(D_AF_1\) term in (20)
cannot cancel this independent direction. This calculation
does not assert that the same obstruction occurs for every
Euler-induced LND.

## 7. A different Lie-generated direction does lower the shift

The example also separates the failed fixed-direction procedure
from arbitrary Lie-generated coordinate changes. Equations
(9),(19) give the entire identity
\[
 [N,D]=2N+4\partial_c.
\tag{22}
\]
By (10), the complex Lie algebra generated by \(E,D\) contains
\(N\), hence contains \(\partial_c\), and therefore contains
the nonzero LND
\[
 M=N-\frac45\partial_c
   =a\partial_b+\left(b+\frac15\right)\partial_c.
\tag{23}
\]
It is triangular and locally nilpotent: it fixes \(a\),
sends \(b\) to \(a\), and sends \(c\) to \(b+1/5\).
It kills \(u\). The actual
polynomial automorphism \(\exp(-uM)\), with inverse
\(\exp(uM)\), sends the entire frame (4) to
\[
 (u,\ a+u^2,\ b+u^4,\ c+u^6).
\tag{24}
\]
The coordinate degrees and their sum are unchanged, but the
new Euler field is \(D_A+uE\), of exact shift zero. Thus this
different direction does lower \((13,1)\) to \((13,0)\).
It is not a replica of \(N\): comparison of the \(b\) and
\(c\) components shows that \(M\) is not even a rational
multiple of \(N\).

There are still lower frames, such as
\((u,a+u,b+u,c+u)\), with all degrees one. Their inverses and
the inverse (5) supply actual polynomial coordinate changes.
The example is therefore explicitly nonminimal, with the known
polynomial kernel \(A=\ker E\) throughout. No conclusion that
Lie closure always supplies a successful direction is drawn.

## 8. Recomputing the direction after a plateau move also escapes

The obstruction is to strict improvement by one replica of the
original recovered direction. It does not even obstruct a
two-step sequence that recomputes the direction after a move
leaving (2) unchanged. This can be verified exactly here.

First use \(F=-u\) and the original \(N\). The full flow
formula (14) gives
\[
 \exp(-uN)(X,Y,Z,W)
   =(u,\ a+u^2,\ b+u^4,\ c-4u/5+u^6).
\tag{25}
\]
The exact degree tuple is still \((1,2,4,6)\). The entire
Euler field of this intermediate frame is
\[
 D_1=D_A+uE-4u\partial_c,\qquad
 \delta(D_1)=1,\qquad N_1=-4\partial_c.
\tag{26}
\]
Indeed its last eigen-equation forces \(D_1(c)=6c-4u\);
the other three inverse equations give \(D_1(a)=2a\),
\(D_1(b)=4b\), and \(D_1(u)=u\). The recovered horizontal
derivation is therefore \(N_1\), not the original \(N\).
The first step leaves \((13,1)\) unchanged, in agreement
with the obstruction proved above.

Now the coefficient \(-u/5\) is allowed for the new direction
\(N_1\). Its replica adds \(4u/5\) to \(c\) and takes (25)
to the zero-shift frame (24). Since \([N,\partial_c]=0\),
the two exact polynomial automorphisms satisfy
\[
 \exp\!\left(-\frac{u}{5}N_1\right)\exp(-uN)
 =\exp\!\left(\frac45u\partial_c\right)\exp(-uN)
 =\exp(-uM).
\tag{27}
\]
Thus a plateau step followed by recovery and a second replica
does succeed in this example. No assertion that plateau moves
always escape, or that they admit a well-founded secondary
measure, is proved. The exact failed shortcut is a guaranteed
strict one-step decrease using replicas of the currently
recovered direction.

## 9. Verification and status

Fresh unsaved algebra checked both complete inverse compositions
in (4)--(5), the Jacobian, the full degree tuple, the entire
Euler pullback (8), the gcd, fixed ideal, full replica flow, the brackets
(19),(22), and the universal first-order formula (20) with an
arbitrary symbolic function \(F_1(a,b,c)\). The whole untwisted
frame (24) and both entire intermediate Euler fields in
(25)--(26) were checked separately. The all-coefficient degree
classification (16), constant-term normalization, and full
replica obstruction are proved above, not inferred from a
finite parameter search.

Sources576,577,578 were read completely. No saved checker was
executed, imported, compiled, or rerun. No canonical file was
edited. Author checking is not an independent saved-source
review. The conclusion is a bounded obstruction for one full
replica orbit, together with a successful different direction
in that same actual control, not a general descent theorem.
