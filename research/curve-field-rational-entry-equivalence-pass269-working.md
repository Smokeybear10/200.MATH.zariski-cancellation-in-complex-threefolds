# Rational curve-field entry and an invariant Bezout criterion

For a fixed actual polynomial frame, rational entry over an invariant
curve field is equivalent to the existence of an invariant polynomial
of degree one in the last coordinate. The coefficient of that coordinate
need not be a unit. This is weaker than the polynomial-entry hypothesis
of266, and does not by itself supply an invariant ambient coordinate.

An explicit invariant Bezout identity for the leading coefficients of
the reduced fractional-linear pair does supply such a coordinate.
The coefficient ring in that identity matters: its coefficients must
be invariant, not merely polynomials in the first three coordinates.

## 1. Fixed actual frame and exact statement

Suppose
\[
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,
\qquad R_0=\mathbb C[X,Y,Z],\quad K_0=\operatorname{Frac}R_0 .
\tag{1}
\]
All four displayed variables are actual polynomial coordinates.
The global slice is needed for the recognition endpoint below, not
for the elementary rational-entry equivalence.

For this fixed frame, the following conditions are equivalent:

1. There is a finitely generated field
   \[
   \mathbb C\subset F\subset\operatorname{Frac}A,\qquad
   \operatorname{trdeg}_{\mathbb C}F=1,\qquad
   \operatorname{Frac}B=F(X,Y,Z).
   \tag{2}
   \]
2. There are \(a,b\in R_0\), with \(a\ne0\), for which
   \[
   I=aW+b\in A .
   \tag{3}
   \]

Condition (3) means exactly \(\deg_W I=1\); it does not require
\(a\in\mathbb C^*\), \(Ea=0\), or \(I\) to be a coordinate.
In the implication from (2) to (3), replacing the originally
supplied field \(F\) is allowed. In general \(I\) need not lie
in that original field.

## 2. The curve field is rational, and its generator is fractional-linear

We use the generalized Luroth theorem in its precise subfield form:
a transcendence-degree-one subfield over \(k\) of a rational function
field \(k(x_1,\ldots,x_n)\) is \(k(h)\) for some element \(h\).
An explicitly read primary statement is
[Ollivier--Sadik, Theorem 2, arXiv:2201.11733v1](https://arxiv.org/html/2201.11733v1).
Only the case \(k=\mathbb C\) is used here. The cited source identifies
this as an established generalization of Luroth's theorem; no new
field-rationality theorem is claimed in this note.

Apply it to the actual inclusion
\(F\subset\operatorname{Frac}B=\mathbb C(X,Y,Z,W)\).
It gives \(F=\mathbb C(h)\). Equation (2) then reads
\[
K_0(h)=K_0(W).
\tag{4}
\]
In particular \(h\) is transcendental over \(K_0\), and the
independence of \(X,Y,Z\) over \(F\) also follows by transcendence
degree. No equality \(F=\mathbb C(h)\) is inferred merely from
the existence of one nonconstant element of \(F\).

For completeness, equality (4) forces a fractional-linear expression.
For coprime \(A(T),B(T)\in K_0[T]\), with \(A/B\) nonconstant,
the polynomial \(A(T)-H B(T)\) is irreducible in \(K_0(H)[T]\).
Indeed it is primitive and linear in \(H\) over \(K_0[T]\);
Gauss's lemma first applies over \(K_0(T)\), and then over
\(K_0[H]\). Its \(T\)-degree is
\(\max(\deg A,\deg B)\), because \(H\) is transcendental.
Therefore the field degree of a rational function is that maximum.
Applied to (4), this degree is one, so
\[
h=\frac{aW+b}{cW+d},\qquad
a,b,c,d\in K_0,\qquad ad-bc\ne0 .
\tag{5}
\]

Clear the coefficient denominators to put all four coefficients in
\(R_0\), and cancel their common polynomial factor. Put
\[
P=aW+b,\qquad Q=cW+d,\qquad
a,b,c,d\in R_0,\quad ad-bc\ne0,\quad \gcd_B(P,Q)=1 .
\tag{6}
\]
The cancellation preserves degree at most one in \(W\).
To justify the last gcd assertion, a common factor of positive
\(W\)-degree would remain a common factor over \(K_0[W]\),
contrary to \(ad-bc\ne0\). A remaining common factor in \(R_0\)
divides all four coefficients and has already been removed.
The gcd assertion is not a claim that the ideal \((P,Q)B\) is
the unit ideal.

## 3. Reduced numerator and denominator are individually invariant

Since \(h\in\operatorname{Frac}A\), differentiating \(h=P/Q\) gives
\[
Q\,E(P)=P\,E(Q).
\tag{7}
\]
Unique factorization and \(\gcd(P,Q)=1\) imply
\(P\mid E(P)\) and \(Q\mid E(Q)\).

If \(f\ne0\) is a polynomial and \(E(f)=fg\ne0\), the degree
function of a locally nilpotent derivation gives
\[
\deg_E f-1=\deg_E(Ef)=\deg_E f+\deg_E g,
\]
which is impossible. Thus a polynomial dividing its own derivative
under an LND has derivative zero. Applying this separately to (7)
proves
\[
E(P)=E(Q)=0 .
\tag{8}
\]
This argument applies to actual polynomials in \(B\), not to
arbitrary elements of a localization where local nilpotence might fail.

At least one of \(a,c\) is nonzero by (6). Choose the corresponding
member of \(P,Q\). It is an invariant of \(W\)-degree one,
which proves (2) implies (3).
It need not generate the originally supplied curve field.

Conversely, given (3), set \(F'=\mathbb C(I)\).
The polynomial \(I=aW+b\) is transcendental over \(K_0\), since
\(a\ne0\) and \(W\) is transcendental over \(K_0\). Hence \(F'\)
is a finitely generated invariant curve field and
\[
W=\frac{I-b}{a},\qquad
\operatorname{Frac}B=F'(X,Y,Z).
\tag{9}
\]
This proves the equivalence, with its stated permission to replace \(F\).

## 4. A sufficient invariant Bezout condition for recognition

Retain a reduced pair (6),(8). Suppose there are explicit polynomials
\[
\alpha,\beta\in A\cap R_0,\qquad
\alpha a+\beta c=1 .
\tag{10}
\]
There is no automatic existence assertion in (10).
The coefficients \(a,c\) themselves are not assumed invariant.
Define
\[
J=\alpha P+\beta Q
  =W+\alpha b+\beta d .
\tag{11}
\]
Every factor used in the first expression is invariant, so \(EJ=0\).
The second expression proves that \(J\) is an actual coordinate:
the map fixing \(X,Y,Z\) and replacing \(W\) by \(J\) has the
polynomial inverse \(W=J-\alpha b-\beta d\).
Both compositions are the identity, because the correction lies in
\(R_0\). No coefficient-field coordinate change has been descended.

By the slice hypothesis \(A[u]=B\), the kernel \(A\) is finitely
generated and regular. The nonzero derivation \(E\) now annihilates
the actual coordinate \(J\). The precise
[Bhatwadekar--Gupta--Lokhande Theorem 3.5](https://arxiv.org/html/1501.01438v1)
therefore applies to \(B=\mathbb C[J,X,Y,Z]\), giving
\[
A=\mathbb C[J]^{[2]}\simeq\mathbb C^{[3]} .
\tag{12}
\]

A particularly simple verifiable case is a constant linear
combination \(ra+sc\in\mathbb C^*\), with \(r,s\in\mathbb C\);
normalize that nonzero constant to obtain (10).
This includes either \(a\in\mathbb C^*\) or \(c\in\mathbb C^*\).
In the latter case the reduced denominator \(Q\) itself is an
invariant coordinate with nonzero constant \(W\)-coefficient.
More generally a constant fractional-linear rechoice of \(h\)
can make such an invariant linear combination the denominator.

The phrase "unit denominator" must not be substituted for this
condition: \(Q=1\) has zero \(W\)-coefficient and supplies no
nonconstant coordinate. Nor does an identity
\(\alpha a+\beta c=1\) with merely \(\alpha,\beta\in R_0\)
make (11) invariant. Its derivative then includes
\(E(\alpha)P+E(\beta)Q\). Invariance of the Bezout coefficients
is an explicit hypothesis, not a consequence of coprimality.

## 5. Actual rational boundary and precise scope

The fully read
[actual boundary in266, Section 4](curve-field-polynomial-entry-criterion-pass266-working.md)
has
\[
I=XW-Y^2\in A,\qquad F=\mathbb C(I),\qquad
W=\frac{I+Y^2}{X},\qquad \operatorname{Frac}B=F(X,Y,Z).
\tag{13}
\]
Its explicitly defined derivation is globally sliced, with an ordinary
polynomial kernel. The same source proves that no
\(P_0\in R_0\) makes \(W-P_0\) invariant: the coefficient of \(W^2\)
in \(E(W-P_0)\) would force
\(X^2(P_0)_Y=2XY+2\), impossible at \(X=0\).
Thus that example has rational entry and an invariant affine in \(W\),
but not the particular invariant monic-linear coordinate concluded
by266 or by (10).

For its generator \(h=I\), the reduced pair is \(P=I,Q=1\),
so \(a=X,c=0\). Condition (10) would require \(\alpha X=1\)
in \(R_0\), which is impossible even without imposing invariance.
This is an actual countercontrol to treating a nonzero leading
coefficient as a unit. It is not a cancellation counterexample.

Consequently the equivalence in Section 1 is not an equivalence
with the polynomial-entry hypothesis of266 for the fixed actual frame.
No implication from rational entry alone to rank at most three,
to an invariant ambient coordinate, or to recognition is proved.
The rank drop and recognition in Section 4 use the additional
invariant Bezout condition. The note also does not establish
rational entry in any arbitrary globally sliced four-ring.

The generalized Luroth statement is an explicitly identified primary
input. Fractional-linear degree, UFD cancellation, the LND divisibility
argument, and both triangular inverse orders are given above.
The full266 proof and its held boundary were read; no saved checker
was executed, imported, compiled, or rerun. No earlier source,
packet, or mutable index was changed. No new checker is needed for
these elementary algebraic implications, and none was created.
This is a bounded working argument, not a novelty claim, independent
human certification, or an unrestricted cancellation solution.
