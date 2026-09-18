# A singular coefficient curve blocks the smooth shear step

The higher-order coefficient restrictions allow a small tuple for
which a/b is integral over R/(B1) but does not belong to that ring.
Thus the shear used in the smooth-B1 proof cannot be inferred from
those restrictions alone. This is coefficient data, not an actual
flat algebra with a mixed fiber and not a cancellation counterexample.

## 1. Explicit coefficients with the required higher orders

Let R=C[x,y]_(x,y), with maximal ideal m=(x,y), and put
\[
\begin{gathered}
h=B_1=y^2-x^5,\qquad a=y(x+y),\qquad b=x^2,\qquad
\epsilon=1,\\
B_2=xh,\qquad Q=yh,\qquad
P=ah+bB_2=h(a+x^3)\ne0.
\end{gathered}
\tag{1}
\]
Both a and h have order exactly two, B2 and Q have order
exactly three, and P has order exactly four. Neither a nor h
has the prime factor x, so gcd(a,b)=gcd(h,b)=1. In particular
J=(a,b) is a proper maximal-primary complete intersection.
The nonzero condition on P is an identity in the polynomial
domain, not a specialization of a hypothetical derivation.

The exact polynomial identity
\[
\begin{gathered}
a^2=h\bigl((x+y)^2+x^5\bigr)
       +b^2\bigl(x^3+2x^2y+x^6\bigr),\\
a^2\in\mathfrak m^2(h)+\mathfrak m^3(b^2),\\
Q,B_2,a^2\in\mathfrak m(h)+\mathfrak m(ab)+\mathfrak m^2(b^2)
\end{gathered}
\tag{2}
\]
verifies the sharp coefficient condition108. Since J is
contained in m², J² is contained in m⁴, whereas h has order
two. Thus h does not belong to J² either. These coefficients
satisfy the specific order and gcd restrictions just obtained
in109; no algebra realization is being inferred.[^bounds]

## 2. Integral does not mean regular on this singular curve

The polynomial h is irreducible: it is monic quadratic in y,
and x^5 is not a square in C(x). Hence C=R/(h) is a domain.
Its element b is nonzero. In Frac(C) set z=bar(a)/bar(b).
Equation (2) gives the monic equation
\[
z^2=\bar x^3+2\bar x^2\bar y+\bar x^6
\in(\mathfrak m C)^3\subseteq(\mathfrak m C)^2.
\tag{3}
\]
Thus z is integral over C, with exactly the coefficient-order
property used by the smooth quotient argument. Nevertheless
\[
\begin{gathered}
(h,b)=(y^2,x^2)R,\qquad
a\bmod(h,b)=xy\ne0,\\
z\notin C,\qquad
\boxed{\quad a\notin(h,b),\quad
a\notin(h)+b\mathfrak m.\quad}
\end{gathered}
\tag{4}
\]
The Artin quotient R/(x²,y²) has C-basis 1,x,y,xy, so the
nonzero assertion is exact and persists after localization.
If z belonged to C, the equality a=bz modulo h would instead
put a in (h,b). This proves the failure without appealing to
an uncomputed normalization or an infinite power series.

In particular no u,v in R satisfy a=hu+bv, even without the
stronger requirement v in m. The step that failed is the
normality of the quotient curve: the smooth-B1 proof has a
DVR quotient, while C here is an explicitly nonnormal domain.

## 3. A second failed implication, and its precise limit

For a higher-order h the old smooth colon implication also
cannot be inferred from flatness alone. Already in the flat
R-module R itself,
\[
h\in\mathfrak m^2,\qquad h\cdot1\in\mathfrak m^2,
\qquad 1\notin\mathfrak m,
\qquad (\mathfrak m^2:h)=R.
\tag{5}
\]
This does not assert failure of actual quartic division in
some original frame. No such algebra or quartic was supplied
in (1). Moreover this colon observation is not a reason to
abandon a shear that is independently available: the next
identity gives a derivative-residue substitute for that step.

## 4. The exact derivative identity once a shear is supplied

For the separate general-shear calculation, use formal
invariant coefficients h,b,u,beta,delta,q and epsilon. Suppose
an actual conic calculation has reached r=huG+bH and the
usual derivative formulas. In a ring where h is invertible,
the following is an exact identity:
\[
\begin{gathered}
NG=\epsilon br+h,\qquad
NH=-\epsilon hu r+h\beta+b^2\delta,\\
U=(\epsilon H^2-2\delta G-q)/h,\\
NU=-2\epsilon^2uHr+2\epsilon\beta H
       -2\epsilon bu\delta G-2\delta.
\end{gathered}
\tag{6}
\]
Differentiate the numerator and use bH-r=-huG to cancel the
remaining h denominator. If an actual flat conic construction
has supplied U in its algebra, this same identity holds there
by injectivity into the h localization. With H and r zero in
the whole fiber, beta in m and delta in m², it gives NU zero
in that fiber without requiring U itself to vanish there.
The finite check of (6) does not prove existence of that U.

The tuple (1) is outside this shear premise by (4). The
calculation therefore neither supplies a missing shear for
the tuple nor asserts that it survives every further actual
frame identity. Its function is to isolate a genuine limit
of the coefficient-only argument.

For the separate calculation without a shear, write the sharp
coefficient identities as a²=hU0+abV0+b²W0,
B2=h beta+ab tau+b²delta and Q=h zeta+ab xi+b²q. Set
A=epsilon U0 G²-2beta G+2H-zeta. The exact conic gives
hA+bB=0 with
B=a(epsilon V0 G²+2epsilon GH-2tau G-xi)
+b(epsilon W0 G²+epsilon H²-2delta G-q).
The third finite control checks, conditional on these identities,
\[
\begin{gathered}
W=B/h=-A/b,\\
NW=-2\epsilon^2U_0Gr+2\epsilon\beta r
 +2\epsilon\bigl((aV_0+bW_0)G+aH\bigr)
 -2a\tau-2b\delta,\\
\det(1,G,G^2,GH,W)=-\epsilon^4b/(8P^4).
\end{gathered}
\tag{7}
\]
For the determinant, the generic line uses
G=epsilon b r²/(2P)+h r/P+g0 and H=(r-aG)/b.
These computations do not prove the existence of W in an
actual algebra, the valuation of its coefficient matrix over
R, or a resulting derivative-residue contraction. They are
explicit identities supporting those separately written steps.

## 5. The tuple fails the stronger actual necessary ideal condition

The [actual divided-W exclusion](mixed-proper-image-exclusion-pass110.md)
imposes a further condition
not contained in the original sharp coefficient inequalities:
b must belong to J=(h)+m(a)+m²(b). The tuple (1) fails this
condition explicitly:
\[
\boxed{\quad
J=(y^2,x^2y,x^4)R,\qquad b=x^2\notin J.
\quad}
\tag{8}
\]
Indeed x^4 is among the generators m²b, so h supplies y²;
then xa supplies x²y. The reverse ideal inclusion follows
by substituting (1). The monomial x² survives this local
Artin quotient. Thus the example does not challenge a proof
that derives the extra condition from an actual flat frame.
It isolates why sharp coefficients alone did not imply a
shear, while the new derivative-residue information is stronger.
The linked proof excludes the actual proper mixed sector without
assuming a shear. This coefficient tuple is therefore not a surviving
actual-frame candidate.

## Verification scope

The [companion checker](mixed_singular_coefficient_checks_pass110.py)
tests the polynomial identity, ideal
remainders and finite Artin basis behind (1)--(4), and the
formal conic/derivative identities (6)--(7), in three separate methods.
The first method also verifies (8); the third checks the
denominator-free identity used by the subsequent unit absorption.
It does not test actual flatness, a prescribed whole fiber,
the degree-module filtration, or a coordinate inverse for
this coefficient tuple. No numerical sample is used as a
proof of irreducibility or of a universal geometric theorem.
All files through109 remain unchanged.

The final author command was
`/opt/anaconda3/bin/python research/mixed_singular_coefficient_checks_pass110.py`.
All three methods passed in 0.404 unittest seconds, exit zero, with
complete output retained as fddfd0. The earlier author run b5d1fd
preceded the stronger-ideal and unit-absorption assertions and is not
counted as additional coverage. Independent code-only reviews are
distinct from execution; the canonical packet capture is recorded separately.

[^bounds]: [Sharp proper coefficients108](mixed-proper-second-image-jets-pass108.md) and [smooth-B1 exclusion109](mixed-smooth-B1-exclusion-pass109.md). Their coefficient restrictions are necessary in the actual frame, not sufficient to construct one.
