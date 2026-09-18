# Independent audit of the polynomial local-slice coefficient classification

Date: 2026-09-13.

## Verdict and assumptions

I read the complete [classification note](polynomial-local-slice-coefficients-pass23.md)
and independently reconstructed both necessity arguments, the polynomial
gauge, the nonlinear variable-time inverse, and both directions of the
physical coordinate lift. I found no mathematical defect in the stated
criterion under its exact assumptions: the displayed canonical derivation
over C, n >= 1, and b in the specified subring C[f,h,r].

The proof gives a slice if and only if the nonzero constant and both monic
remainder tests hold. Every positive case has polynomial kernel. The
necessity arguments exclude slices of every degree, not just the degrees
tested computationally. The proof does not classify arbitrary b in
C[x,y,z], arbitrary primitive rank-three derivations, or arbitrary sliced
derivations on C^[4]. Priority, expert review, and Lean verification remain
unresolved.

## 1. Both divisors give genuine all-degree obstructions

The printed formulas for D(x), D(y), and D(z) are consistent with
-Jac(f,h,.), including n=1. They show that D vanishes on x=y=0,
where f=h=r=0. Hence c=b(0,0,0)=0 gives an actual fixed point of E
and precludes a slice.

For c nonzero, write P(u)=F(0,u^5,u^3). Because F has zero r-constant
term, its unique lowest term is c*u^3. The substitution kernel is
(r^5-h^3), and the five remainder powers r^i, 0 <= i < 5, occupy
distinct exponent classes modulo five. Thus the first remainder test is
exactly P(u)=c*u^3 plus a polynomial in u^5.

If it fails, every nontrivial fifth root epsilon detects a term of degree
greater than three whose exponent is not divisible by five. Consequently

\[
(P(u)-P(\epsilon u))/u^3
\]

has a nonzero constant and positive degree. It has a nonzero complex
root. No simple-root hypothesis is needed. At the selected point in the
f,x_1,x_2 chart, the equation x_1^5=x_2^5 has distinct local branches,
and the second equation restricts to a nonzero polynomial on the chosen
branch. The zero-f fiber is therefore locally zero-dimensional, even
when that polynomial has a multiple root.

Two equations in the regular three-dimensional chart have local
dimension at least one. Quotienting by f and using the zero-dimensional
fiber bounds that dimension above by one. A curve component through
the point is therefore not contained in f=0. Normalization gives a DVR
in which f has positive valuation and x_1,x_2,h,r_2-r_1 are units.
The displayed endpoints are actual integral points of the original
affine four-space. The E-orbit parameter
(r_2-r_1)/(f^n h) has negative valuation, whereas the defining equation
on the curve makes the t-displacement zero.

For the second divisor, the odd remainder coefficient B(f) satisfies
B(0)=c. If it is not constant, it has a nonzero root f_0. The polynomial
Gamma(f,h) is well defined because the odd part divided by r is a
polynomial in r^2. Its restriction at h=0 is precisely B(f). The
two-equation chart in f,h,r again has a zero-dimensional special fiber
and a horizontal curve component. Normalization gives h of positive
valuation and f,r units. The endpoints with x=1 and local-slice values
r,-r are integral because a=f^n is now a unit. Their parameter
-2r/(ah) has a pole and their t-displacement is zero.

In both constructions the exact flow identity is

\[
r_2=r_1+p\tau,\qquad
x_2-x_1=(r_2^2-r_1^2)/h,
\qquad
t_2-t_1=(F(r_2)-F(r_1))/p.
\]

These identities determine the remaining physical coordinates after
localizing f. A polynomial slice would have integral endpoint difference
equal to tau. This is the required contradiction in every degree.

The dimension and normalization hypotheses match those reconstructed
in the [preceding audit](radical-noninvariant-audit-pass22.md), Section 3:
[Stacks Lemma 10.60.12](https://stacks.math.columbia.edu/tag/0BBZ),
[Lemma 10.60.13](https://stacks.math.columbia.edu/tag/00KW),
[Lemma 33.27.1](https://stacks.math.columbia.edu/tag/0BXR), and
[Lemma 33.43.8](https://stacks.math.columbia.edu/tag/0B8Y).
The present argument adds the explicit second-divisor curve, not a
stronger normalization or dimension theorem.

## 2. The intersection and gauge take place in the correct ring

The hypersurface S_0 embeds in R and becomes R_f after localizing f.
The two displayed quotient rings S_0/(f) and S_0/(h) are domains.
For the latter, r^2+f^(2n+1) is irreducible because an odd power of f
is not a square in C(f). In particular f and h are distinct prime
elements. This does not assert that S_0 is a UFD.

The constants H_f(0)=H_h(0)=0 ensure that subtracting
H_f(h)+H_h(f) respects both remainder conditions. The key identity is

\[
G_0=r^5-h^3-f^{2\nu}r
 =h^2(x^2r-h)-2xh f^\nu r
 =p\bigl[-h(x^2y+az)-2x f^{n+1}r\bigr].
\]

It also has the expression
G_0=h[xr(r^2-f^nu)-h^2] in S_0. Thus, although g=J*g_0 need
not belong to S_0, the element pg=J*G_0 does belong to S_0. This is
essential to the intersection argument and is satisfied here.

The difference DeltaF-pg belongs to fS_0 by the first test and to
hS_0 by the second test. If f*q belongs to hS_0, reducing modulo h
and using the nonzero image of f in the domain S_0/(h) proves that
q belongs to hS_0. Hence (f) intersect (h)=(fh), with no factoriality
assumption. This produces ell in fS_0 such that

\[
F-cr-H-pg=h\ell.
\]

The independent polynomial representative required in Section 6 exists:
write ell=f*q in S_0, choose any polynomial representative of q in
C[f,h][x,r], and multiply it by f. This produces an f-divisible
representative before imposing the quadratic relation. It does not
identify S_0 with a polynomial ring.

On S_0, D=a*delta_0 and delta_0=2r*partial_x+h*partial_r.
Differentiating the displayed identity and cancelling the nonzero
element p gives b-Dg=c+delta_0(ell). The change t'=(t-g)/c is a
genuine polynomial automorphism of R[t], with inverse t=g+c*t'.
It yields the asserted form with ell/c. Any chosen representative
works, since delta_0 preserves xh-r^2-f^nu.

## 3. The nonlinear variable-time map has a finite global inverse

Work first in the independent polynomial ring C[f,h][x,r,t] with
the chosen f-divisible ell. Direct differentiation gives

\[
E(\ell-at)=-a,
\qquad E\bigl(r+h(\ell-at)\bigr)=0,
\]

and the claimed invariance of X and quadratic-level identity. The
localized inverse formulas reconstruct r and x polynomially from
X,rho,sigma_0; substituting them into
t=sigma_0+ell(x,r)/a then reconstructs t. Both compositions are
identities. In particular this inverse does not assume that a nonlinear
equation involving ell has an implicit polynomial solution.

Modulo a=f^n, let Delta=phi_0-id. Since phi_0 fixes f,h and is the
identity modulo f, Delta sends f^j times the whole polynomial ring
into f^(j+1) times that ring. Therefore Delta^n=0 on the entire
quotient. The finite geometric sum is a two-sided additive inverse
of the ring map phi_0 and hence its ring inverse. The quotient may
have nilpotents; that is the reason the argument is finite, not a gap.

The correct orientation of the correction is
K=phi_0^-1(-ell) modulo a. Then -ell-K(X,rho) is divisible by a,
so sigma is polynomial. Modulo a, E is
(1+delta_0 ell)*partial_t with a unit coefficient. From E(sigma)=1,
characteristic zero implies that sigma is affine in t with unit slope
there. Together with phi_0, this gives an automorphism of the complete
polynomial ring modulo a, not only of the surface quotient.

The localized inverse and the injective reduced map suffice to remove
denominators. Explicitly, write a preimage as H/a^m with m minimal.
If m>0, its defining equality reduces to phi_bar(H_bar)=0 modulo a.
Injectivity forces H=aH_1, contradicting minimality. This is a finite
domain argument, not formal algebraization. The resulting automorphism
fixes f,h and the quadratic level, so its inverse does also and both
descend to S_0[t].

## 4. Both physical coordinate directions are polynomial

On the universal old curve (x,h,r)=(u,u^5,u^3), the map is exactly

\[
X=u(1+u^2v)^2=uU,\qquad
\rho=u^3(1+u^2v)=uW,\qquad h=u^5.
\]

All computations here are in (C[f]/(f^n))[u]. The factors U and
1+u^2v are units, and psi=uU is the identity modulo the nilpotent
ideal (f). Its inverse is a finite polynomial. The definition of
Ptilde therefore gives both rho=X*Ptilde and h=X*Ptilde^2 on the
universal image curve. These are full congruences, not statements only
about its closed points. Any cancellation of u occurs in this universal
polynomial ring, where u is a non-zero-divisor, before specialization.

The first congruence clears the Y denominator in the physical ring.
Multiplying the Z numerator by X gives exactly a^2*(Y^2+f).
The polynomial f=xz-y^2 is prime, X=x modulo f, and f does not divide
X. Therefore cancellation of f^(2n) is valid and Z is polynomial.
The same identity proves f=XZ-Y^2.

For the independent inverse, start with independent variables
X,Y,Z,sigma, define f=XZ-Y^2, and reconstruct rho and h from the
new physical presentation. Apply the universal polynomial inverse from
Section 3. The inverse curve congruence makes r-x^3 divisible by f^n,
so the old y is polynomial. The quadratic identity then gives x times
the old z numerator equal to f^(2n)*(y^2+f). Here f=XZ-Y^2 is prime
in the new independent polynomial ring and old x=X modulo f, so
the same prime cancellation makes old z polynomial. Undoing the gauge
then makes old t polynomial as well.

The two maps are inverse after localizing f. Both rings are domains,
so their polynomial compositions are already identities globally. This
checks the claimed coordinates in the physical R[t], not merely in
S_0[t] or on a formal neighborhood.

The prior-work scope is unchanged: the general full-ideal lifting
principle is Kaliman--Zaidenberg's, as documented in the
[two-stage modification audit](priority-boundary-pass20.md). The present
proof supplies the particular curve congruences. No new universal
lifting principle or mathematical priority is inferred.

## 5. Exact controls and proper-subring boundary

Independent inline SymPy controls supplied 34 exact scalar assertions
for the G_0 factorization, nonlinear variable-time invariants, preserved
quadratic level, and both localized inverse directions for several
nonlinear f-divisible ell. A further 16 exact scalar assertions checked
the expanded physical G_0 identity, all three printed derivation
coefficients and D(r)=f^n*h for n=1,2,3, and the higher-r negative
example for those n. All 50 assertions passed. These are inline controls,
not 50 test methods or a proof of the universal claims.

The example b=1+f*r^2 is correctly negative: the first test passes,
while the second odd coefficient is 1-f^(nu+1)/3, which is nonconstant.
The reductions to the preceding 1+q*r and invariant-coefficient
classifications are also correct.

The proper-subring limitation is substantive. Modulo f, the image of
C[f,h,r] is C[x^5,x^3]. To make the role of y precise, localize
R/(f) at x; the result is C[x,x^-1,y]. Its element y is algebraically
independent of x and cannot lie in the image C[x^5,x^3]. Therefore y
does not belong to C[f,h,r] in R. Nothing in this proof shows that
arbitrary coefficients can be moved into that subring modulo D(R).
That remaining reduction and the general coordinate-frame problem
must remain separate from this completed family classification.
