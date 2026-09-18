# Weight-four forms with zero quadratic rank in the bad coordinates

**Status: working algebraic classification, pending independent saved-source review.**

Let the weights of \(X,Y,Z,W\) be \((1,1,2,2)\). An irreducible
weight-four polynomial with no term quadratic in \(Z,W\), and with
at least one of those variables occurring, has exactly one of four
normal forms under constant good and bad linear changes and binary
quadratic translations of the bad coordinates:
\[
\begin{array}{c|c|l}
\dim\langle P_2,Q_2\rangle&\gcd(P_2,Q_2)&\text{normal form}\\ \hline
2&1&X^2Z+Y^2W\\
2&\text{one linear factor}&X^2Z+XYW-Y^4\\
1&\text{a doubled linear factor}&X^2Z-Y^4\\
1&\text{two distinct linear factors}&XYZ+X^4+Y^4 .
\end{array}
\tag{1}
\]
Here a generator can also be multiplied by a nonzero complex constant.
There is no continuous modulus under this specified group. This is
an algebraic classification, not a realization or recognition theorem.
In particular it does not prove that a true minimum time-degree frame
can or cannot have any one of these forms.

## 1. Allowed actual transformations and irreducibility

Write
\[
F=P_2(X,Y)Z+Q_2(X,Y)W+H_4(X,Y),
\qquad (P_2,Q_2)\ne(0,0),
\tag{2}
\]
with the subscripts indicating ordinary homogeneous degrees.
The specified transformations have the form
\[
\begin{gathered}
\binom{X'}{Y'}=M\binom XY,\qquad
\binom{Z'}{W'}=N\binom ZW+
 \binom{S_2(X',Y')}{T_2(X',Y')},\qquad M,N\in\mathrm{GL}_2(\mathbb C),\\
\binom XY=M^{-1}\binom{X'}{Y'},\qquad
\binom ZW=N^{-1}\left(\binom{Z'}{W'}-
 \binom{S_2(X',Y')}{T_2(X',Y')}\right).
\end{gathered}
\tag{3}
\]
The displayed formulas verify both inverse orders: the good inverse
returns the same good arguments in the quadratic translations, after
which the two translations cancel and the constant matrices invert.
All these operations are therefore genuine polynomial coordinate
changes in an original four-ring, not just operations on leading
coefficients. Their compositions have the same form. All denominators
below are nonzero complex constants.

Let \(R=\mathbb C[X,Y]\). Viewed in \(R[Z,W]\), the polynomial
in (2) is primitive exactly when
\[
\gcd(P_2,Q_2,H_4)=1.
\tag{4}
\]
Over \(\mathbb C(X,Y)\) it is a nonconstant affine linear
polynomial in \(Z,W\), hence irreducible. Gauss's lemma consequently
makes (4) equivalent to irreducibility of \(F\). If the gcd is
nonconstant, factoring it is a genuine nontrivial factorization:
the remaining factor still involves a bad variable.

If both bad coefficients were zero, a nonzero homogeneous binary
quartic would split into four linear factors over \(\mathbb C\).
It could not be an irreducible weight-four relation. In an actual
height-one setting it is also excluded by the independence of the
two good initials. Thus the only coefficient-span ranks are one
and two.

The rank of \(\langle P_2,Q_2\rangle\), the degree of its common
factor, and the multiplicities of that factor's roots are invariant
under (3). Quadratic translations only replace \(H_4\) by an element
of its coset modulo
\[
P_2 R_2+Q_2 R_2\subset R_4.
\tag{5}
\]
This gives the invariants separating the four rows of (1).

## 2. Independent coefficients with no common factor

Suppose \(P_2,Q_2\) are independent and coprime. Their pencil
contains two distinct square members \(L_1^2,L_2^2\), with
independent linear forms \(L_1,L_2\). Here is an elementary
justification that also separates the common-factor case.

The discriminant of \(sP_2+tQ_2\) is a homogeneous quadratic in
\(s,t\). It cannot vanish identically: if every member were a
square, two independent square members \(L^2,M^2\) would have
independent \(L,M\), but a general linear combination of their
squares has rank two. This is a contradiction.
Choose one discriminant root and set its linear factor equal to
\(X\). In a complementary pencil member write
\(aX^2+bXY+cY^2\). The determinant of the matrix of
\(sX^2+t(aX^2+bXY+cY^2)\) is
\[
t\{cs+t(ac-b^2/4)\}.
\tag{6}
\]
If that root were double, then \(c=0\), and both members would
be divisible by \(X\), contrary to coprimality. Thus there are
two distinct square members. Their linear factors cannot be
proportional because their pencil members are independent.

Use those factors as the good coordinates and the independent
pencil rows as a bad linear change. The bad-linear part becomes
\(X^2Z+Y^2W\). Every binary quartic is in
\(X^2R_2+Y^2R_2\): assign the monomials \(X^4,X^3Y,X^2Y^2\)
to the first summand and \(XY^3,Y^4\) to the second. Hence write
\(H_4=X^2S_2+Y^2T_2\), and set
\(Z'=Z+S_2, W'=W+T_2\). The inverse subtracts these polynomials.
This gives the first normal form in (1). It is irreducible by (4).

## 3. Independent coefficients with a common linear factor

For an independent quadratic pair, a common factor has degree at
most one. Choose it as \(X\) and choose an independent good
coordinate \(Y\). The two remaining linear factors are independent,
so an invertible bad linear change gives
\[
F=X^2Z+XYW+H_4.
\]
For example, if the coefficients are \(X(aX+bY)\) and
\(X(cX+dY)\), use \(Z_0=aZ+cW\), \(W_0=bZ+dW\);
the determinant \(ad-bc\) is nonzero.

Every degree-four monomial other than \(Y^4\) is in
\(X^2R_2+XYR_2\). Therefore
\[
H_4=X^2S_2+XYT_2+\lambda Y^4.
\tag{7}
\]
Irreducibility is exactly \(\lambda\ne0\), because the gcd of
the bad coefficients is \(X\). Define
\(Z'=-(Z+S_2)/\lambda\), \(W'=-(W+T_2)/\lambda\).
Then \(F=-\lambda(X^2Z'+XYW'-Y^4)\). The inverse is
\(Z=-\lambda Z'-S_2\), \(W=-\lambda W'-T_2\), composed
with the inverse of the earlier constant matrices. Thus the
second row has no remaining parameter and is irreducible.

## 4. One-dimensional coefficient span with a double root

An invertible bad linear change first writes
\(F=q_2(X,Y)Z+H_4(X,Y)\); the other bad coordinate is absent.
Suppose \(q_2\) is a square. A good linear change and a nonzero
bad scaling make \(q_2=X^2\). Write
\[
H_4=X^2S_2+\mu XY^3+\lambda Y^4.
\tag{8}
\]
Condition (4) is exactly \(\lambda\ne0\). After setting
\(Z_0=Z+S_2\), put \(c=\mu/(4\lambda)\) and
\(Y_1=Y+cX\). In terms of \(Y_1\), the remaining quartic is
\[
\begin{gathered}
\lambda(Y_1-cX)^4+\mu X(Y_1-cX)^3
 =\lambda Y_1^4+X^2B_2(X,Y_1),\\
B_2=-6\lambda c^2Y_1^2+8\lambda c^3XY_1-3\lambda c^4X^2.
\end{gathered}
\tag{9}
\]
The formula is polynomial, including at \(X=0\); it makes no
division by \(X\). Set \(Z_1=Z_0+B_2(X,Y_1)\), then
\(Z'=-Z_1/\lambda\). This gives
\(F=-\lambda(X^2Z'-Y_1^4)\).

The explicit inverse of these three stages is
\[
Y=Y_1-cX,\qquad
Z=-\lambda Z'-B_2(X,Y_1)-S_2(X,Y_1-cX),
\tag{10}
\]
with \(X,W\) fixed. Substitution in either order returns the
same \(Y_1\) and cancels both quadratic translations. This proves
the third normal form and the absence of a residual parameter.

## 5. One-dimensional coefficient span with two distinct roots

If \(q_2\) has two distinct linear factors, an actual good change
and bad scaling make it \(XY\). Modulo \(XYR_2\), write
\[
H_4=XY S_2+\alpha X^4+\beta Y^4.
\tag{11}
\]
Irreducibility is exactly \(\alpha\beta\ne0\): otherwise a factor
\(X\) or \(Y\) divides all three coefficients in (4).
Set \(Z_0=Z+S_2\). Choose complex nonzero constants \(a,b\)
with \(a^4=\alpha\), \(b^4=\beta\), and define
\[
X'=aX,\quad Y'=bY,\quad Z'=Z_0/(ab),\quad W'=W.
\tag{12}
\]
Then \(F=X'Y'Z'+X'^4+Y'^4\). The full inverse is
\(X=X'/a\), \(Y=Y'/b\),
\(Z=abZ'-S_2(X'/a,Y'/b)\), and \(W=W'\).
Both compositions cancel the same translation and scalings.
The choices of fourth roots are only choices of complex constants;
there is no extension of an actual coefficient field.

The four cases exhaust all nonzero quadratic coefficient pairs.
Each displayed normal form satisfies (4), and the invariants in
Section 1 distinguish their orbits. In particular the zero bad-rank
classification has no binary-quartic cross-ratio parameter.

## 6. What the actual time profile does and does not imply

Now additionally assume the actual hypotheses of
[the initial-bound proof157](two-linear-two-quadratic-initial-bound-pass157-working.md):
\(B=A[u]=\mathbb C[X,Y,Z,W]\), \(E=\partial_u\), exact
time degrees \((1,1,2,2)\), and full generated-initial kernel
\((F)\), with \(F\) irreducible of weight four. The coefficients
in the initial map are ordinary time coefficients, so the two
quadratic coefficients are \(E^2Z/2\) and \(E^2W/2\).

Every transformation (3) is weight-preserving, with a
weight-preserving inverse. Moreover, every new good or bad slot
retains its exact time degree one or two. Otherwise its nonzero
homogeneous coordinate polynomial, of weight one or two, would
belong to \((F)\). A nonzero homogeneous multiple of a weight-four
polynomial in this positive grading has weight at least four.
This is impossible. Thus the transformed initial map has the
same image and the transformed full principal kernel, and none
of the displayed normalizations hides a third good coordinate.

The exact-shift refinement157 consequently gives necessary
conditions in the normal forms: both bad partials have shift
three in the two rank-two rows. In the two rank-one rows,
\(\partial_Z\) has shift three and the omitted \(\partial_W\)
has shift at most two. These facts do not give an inverse or a
degree reduction outside the transformations already displayed.

If the sum of time degrees is additionally assumed to be a true
minimum among all polynomial coordinate frames, that is a
strictly stronger assertion than having the displayed exact
profile. The transformations used here preserve the degree sum
six. They neither contradict that minimum nor prove it is
attained globally. An unrelated, non-weight-preserving polynomial
automorphism could lower the sum; its existence requires a
separate argument. No arbitrary-coordinate entry assertion is
made.

Finally, the formal relation only implies
\(\deg_E F(X,Y,Z,W)\le3\). It does not say that the displayed
original polynomial is invariant, or that it has a lower-weight
invariant correction. None of the four forms itself is an ambient
coordinate: its gradient vanishes on \(X=Y=0\). This last
observation is not an obstruction to an invariant correction,
whose lower-weight terms may change the critical locus.

## Verification and scope

Both proof157 and its companion cubic-normal-form note157 were
read in full before this derivation. Their distinction between
an actual polynomial frame, a generated initial algebra, and a
true minimum profile is retained. The algebraic classification
and its inverses are proved here; no finite checker was written,
run, imported, or compiled. No prior artifact was edited.

This does not establish actual realization of any row, recognize
the remaining weight-four profile, exclude height-two initial
kernels, or solve unrestricted cancellation. It is not a novelty
claim, human expert review, or proof-assistant certification.
