# Second independent audit of the odd-coefficient criterion

Date: 2026-09-13.

## Verdict and corrected transcription

I read the complete [odd-coefficient note](odd-coefficient-gauge-pass24.md)
and independently reconstructed its two necessity arguments, both polynomial
gauges, its use of the finite variable-time inverse, and the all-degree
nongauge obstruction. The substantive argument is correct under the stated
canonical hypotheses, n >= 1, c in C[f,h], and B in C[f,h,x].

I reported one consequential transcription error: equation (11) originally
omitted the plus sign between its two terms. The author restored that sign,
and I reread the corrected equation. The sum, not the product, equals the
orbit-primitive difference. No further correction is requested.

This is a working mathematical audit, not expert review, Lean verification,
a priority determination, or a result about every coefficient in S_0 or R.

## 1. The criterion is necessary in every slice degree

The monic r^2 presentation gives S_0 a free basis 1,r over
C[f,h,x], so the specified decomposition c+rB is unambiguous.
The chosen ell has zero x-constant term and delta_0(ell)=rB.
Thus mathcal F=cr+h*ell is a genuine element of S_0 satisfying
D(mathcal F)=ah*b. It is not being assumed to belong to C[f,h,r].
Over the invariant fraction field its difference divided by ah is
the exact t-displacement of the E-flow.

The fixed line x=y=0 forces c_0 nonzero. If c(f,0) is not constant,
its nonzero constant term c_0 gives a nonzero complex root f_0.
The curve defined by c(f,h)=0 and r^2=h-f^(2n+1) has an isolated
zero-h fiber at the selected point. The regular-local dimension bounds
give a horizontal curve component. Its normalization supplies a DVR
with h of positive valuation and f,r units. Both physical endpoints
have x=1, so their ell-values agree. The c term vanishes exactly,
and the primitive difference is zero. Their orbit parameter has a
pole. Multiple roots cause no problem in this argument.

For the f divisor, the physical substitution h=u^5,x=u,r=u^3
gives P(u) in the note. Its lowest term is c_0*u^3, because the
ell contribution starts at degree at least six. Monic reduction by
x^5-h makes the five powers of x independent over C[h], or,
equivalently, gives distinct exponent classes modulo five after
substitution. Failure of the stated remainder form therefore supplies
a term of degree above three whose exponent is not divisible by five.
Every nontrivial fifth root detects it. The divided difference in
the note is nonconstant with nonzero constant term and has a nonzero
root, without requiring that root to be simple.

The corrected sum in (11) is exactly mathcal F_2-mathcal F_1.
Its restriction to the selected fifth-root branch is a nonzero
one-variable polynomial, so the same dimension argument gives a
horizontal DVR with the required units. The actual integral endpoints
have zero t-displacement and a nonintegral orbit parameter. A polynomial
slice would have integral endpoint difference equal to that parameter.
Both negative arguments therefore apply to every hypothetical polynomial
slice, not just to the bounded examples in the checker.

These are the same precise dimension and normalization hypotheses
already reconstructed in the [pass-23 independent audit](polynomial-coefficients-audit-pass23.md),
Section 1. No new geometric existence theorem is being assumed.

## 2. Both gauges are genuine polynomials

The h test gives a polynomial C_1=(c-c_0)/h. Since
Dy=h-6x^2r=h+delta_0(-x^3), direct subtraction gives

\[
b-D(C_1y)=c_0+\delta_0(\ell_1),\qquad
\ell_1=\ell+C_1x^3.
\]

The f test then says that h times the remainder of ell_1 modulo
x^5-h belongs to C[h]. Write that remainder as
sum_{i=0}^4 L_i(h)x^i. The free monic basis forces h*L_i=0
for i>0, hence L_i=0. This spells out the monic-basis justification
behind the note's non-zero-divisor sentence; non-zero-divisibility
alone in an unrelated ring would not imply the same conclusion.

Consequently ell_1=L(h)+(h-x^5)J(h,x)+fK(f,h,x).
The identity h-x^5=a(2x^2y+az) proves that
g_1=(2x^2y+az)J is in the actual physical R. Its derivative is
delta_0((h-x^5)J), since D=a*delta_0 on S_0 and D(a)=0.
Thus (t-C_1y-g_1)/c_0 is an actual polynomial coordinate change
fixing R. Its inverse is t=c_0*t'+C_1y+g_1. The resulting
coefficient is exactly 1+delta_0(fK/c_0).

## 3. The pass-23 inverse applies to this larger input

The required ell_2=fK/c_0 lies in the literal independent polynomial
ring C[f,h,x], and is divisible by f there. No lift out of the
surface quotient or choice of a rational representative is necessary.
The universal argument in Sections 6-7 of the
[pass-23 theorem](polynomial-local-slice-coefficients-pass23.md)
was proved for every f-divisible polynomial representative in
C[f,h][x,r]. It was not restricted to coefficients polynomial in r
over the invariant plane.

Accordingly L=ell_2-a*t' satisfies E(L)=-a, while rho=r+hL
and X=x+2rL+hL^2 are invariant. The displayed localized inverse is explicit, not an
implicit nonlinear inversion. Modulo a=f^n the first pair is the
identity modulo the nilpotent ideal (f), so the finite additive
geometric sum supplies an actual inverse on the full quotient.
The corrected slice is affine with unit slope in t' modulo a;
the minimal-denominator argument then clears the inverse globally.

On the universal physical curve, ell_2 specializes to an f-divisible
polynomial in u. The same finite parameter inverse clears both curve
congruences. Primality of f and X=x modulo f clear the new Z
denominator; the independently reconstructed old-coordinate direction
uses the inverse curve congruence and the same prime cancellation.
The gauges above are undone only after those physical maps are
polynomial. Thus the proof yields coordinates in R[t], not merely
in the independent five-variable ring or S_0[t]. Its general
modification-lifting principle retains the established attribution.

## 4. The nongauge obstruction is genuinely all-polynomial

For b_*=1+2fxr the criterion passes. For n>=2, suppose instead that
b_*=A_0(f,h,r)+Dg with arbitrary polynomials A_0 and g. In R/(f^n),
x is a non-zero-divisor because f is prime and does not divide x.
The reduced formulas r=x^3,h=x^5 and
D=-5x^4*(x*partial_y+2y*partial_z) are exact.

The only exponents below five in the semigroup generated by 3 and 5
are zero and three. Grouping the invariant-ring image accordingly is
therefore exhaustive, regardless of the degree of A_0. Modulo x,
the independent powers 1,(-y^2),...,(-y^2)^(n-1) force q_0=1.
After cancelling x^3, the same independence forces q_3=0.
Further cancellation of the remaining x leaves

\[
2f=xQ(f,x)-5\delta g\quad\hbox{in }R/(f^n).
\]

The ideal (f^n) is homogeneous with no degree-two component when
n>=2. Since delta preserves ordinary degree, the degree-two part of
delta g depends only on the degree-two part of g, whatever its total
degree. The degree-two part of xQ(f,x) is a multiple of x^2.
Directly the degree-two image of delta has basis
x^2, xy, xz+2y^2, yz. The functional twice the xz coefficient
minus the y^2 coefficient kills this entire span, including x^2,
but takes value six on 2f. This contradicts the displayed equation.

The proof therefore excludes g of every polynomial degree. The
quadratic matrix is a complete obstruction after the justified
homogeneous reduction, not a search cutoff. A base-fixing automorphism
of R[t] sends t to a nonzero scalar times t plus an element of R;
such a change would contradict the same linear-subspace obstruction.

For n=1, the degree-two ideal does contain f, and the contradiction
is unavailable. Correctly, b_*=1+D(x^2/2). For n=2, the supplied
slice t+(X^2-x^2)/(2f) is polynomial since X=x modulo f, and its
derivative is exactly one. No minimum slice degree is inferred.

## 5. Independent executable controls

The companion [standalone checker](reduction_controls_pass24.py) imports
only unittest and sympy. It independently reconstructs remainder tests,
gauges, representative finite-inverse inputs, the n=1 and n=2 examples,
the complete degree-two obstruction matrix, and the stable horizontal
family and recurrence. It imports no solver or project proof module.
Its finite examples do not certify all universal algebraic or geometric
claims; the preceding deductions are the all-degree reconstruction.

Verification command:

```text
/opt/anaconda3/bin/python research/reduction_controls_pass24.py
```

Result: 22 unittest methods passed in 1.000 seconds on the recorded run.
Subtests, recurrence iterates, and scalar assertions are not counted as
additional methods. Both localized inverse compositions and finite
nilpotent slice repairs are included explicitly.
