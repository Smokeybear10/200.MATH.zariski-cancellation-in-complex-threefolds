# Independent audit of the radical noninvariant slice criterion

Date: 2026-09-13.

## Verdict and scope

I read the complete [radical noninvariant note](radical-noninvariant-pass22.md)
and independently reconstructed its finite correction, physical inverse,
valuative obstruction, and low-degree coefficient comparisons. I found no
mathematical gap under its stated assumptions. In particular, the obstruction
does not require a simple root, and the positive proof does not infer
algebraization from a formal inverse.

The conclusion is restricted to the displayed canonical family over
the complex numbers, with n >= 1 and q in C[f,h]. The audited statement is
that D + (1+qr) partial_t has a slice exactly when f divides q, and that
each positive case has polynomial kernel. The affine, quadratic, and
specified cubic minimum-degree regimes are also justified. No exact minimum
degree is asserted in the remaining positive region.

This is an independent working mathematical reconstruction, supplemented
by exact symbolic controls. It is not expert review, Lean verification,
a priority determination, or a proof of general complex cancellation.

## 1. Finite repair and denominator removal

Let a be nonzero in a Q-domain Lambda and assume q is nilpotent modulo a.
For the abstract polynomial derivation in Section 2, put

\[
L=qx/2-at,\qquad \rho=r+hL,\qquad X=x+L(r+\rho).
\]

Direct differentiation gives E(X)=E(rho)=0 and
Xh-rho^2=xh-r^2. A useful independently checked identity is

\[
\sigma_0=t+\frac{q(X-x)}{2a}.
\]

It agrees with the expanded rational slice in the note, including every
sign. Over Lambda[a^-1], the cited polynomial formulas for its inverse
are exact rational identities. No assumption that h is invertible is
needed for that inverse.

Modulo a, the first two coordinates give the ring homomorphism phi_0
displayed in the note. If q^N=0 there, the additive operator
Delta=phi_0-id carries q^j Lambda_bar[x,r] into
q^(j+1) Lambda_bar[x,r]. Thus Delta^N=0 on the whole polynomial ring.
The finite geometric sum is a two-sided additive inverse of phi_0;
because phi_0 is a bijective ring homomorphism, that inverse is a ring
homomorphism. This proof works even if Lambda/(a) has zero divisors.

With K=q^2*x*r/2+q^3*x^2*h/8, the required orientation is
H=phi_0^-1(K), not phi_0(K). Then H(X,rho)=K modulo a, so
sigma=sigma_0-H(X,rho)/a belongs to the polynomial ring and E(sigma)=1.
An equivalent check on this orientation is

\[
H=\frac q2\bigl(x-\phi_0^{-1}(x)\bigr)\pmod a.
\]

The reduction of E is (1+qr) partial_t. Its coefficient is a unit,
since q is nilpotent. Therefore sigma modulo a has derivative
(1+qr)^-1 with respect to t. In a Q-algebra this forces sigma to be
affine in t with that unit slope. Together with the automorphism phi_0
on x,r, this proves that the complete coordinate map modulo a is an
automorphism.

The denominator lemma is sufficient as stated. If the localized inverse
of b has a denominator a^m with m minimal, reduction of F(H)=a^m b
modulo a and injectivity of the reduced map imply H=aH_1 when m>0.
That contradicts minimality. The domain assumption justifies the
localization and cancellation; no completeness assumption is used.

## 2. Physical weighted-overring lift

The universal coordinate map fixes f,h and the quadratic relation. Its
reduction modulo f^n has first coordinates independent of t, preserves
(x,h,r), and is the identity modulo f. The finite inverse has the same
properties. These are the hypotheses required in the previously audited
[weighted-overring argument](cylinder-comparison-pass20.md), Section 5,
and its [full-ideal modification reduction](priority-boundary-pass20.md).

On the universal old curve (x,h,r)=(u,u^5,u^3), the actual images are

\[
X=u(1+q_u u^3/2)^2,\qquad
\rho=u^3(1+q_u u^3/2),\qquad h=u^5.
\]

Consequently the U, W, and psi formulas in the note are exact. U is a
unit and psi is the identity modulo the nilpotent ideal (f), so its
inverse is an actual finite polynomial in the quotient. The construction
of Ptilde gives both required curve identities, not merely equality on
closed points.

The cancellation establishing h=X*Ptilde^2 takes place in the universal
ring (C[f]/(f^n))[u], where u is a non-zero-divisor. It does not cancel a
potentially nilpotent specialized x. In the physical ring, the later
cancellation is different: f is prime, X=x modulo f, and f does not
divide X. Hence X times the numerator being divisible by f^(2n) really
does imply that the numerator itself is divisible by f^(2n).

The independent inverse uses the inverse universal curve identity to
clear the old y denominator and the same prime-cancellation argument to
clear the old z denominator. After f-localization it is the already
established inverse. Injectivity of localization then proves both global
compositions. This verifies polynomial coordinates in the physical
four-variable ring, rather than merely in the larger abstract surface
presentation.

The framework remains an application of the previously cited full-ideal
affine-modification lifting principle. The audit does not claim that
the new coefficient classification is absent from prior work.

## 3. The all-degree negative direction

For q_0(H) nonzero and epsilon a nontrivial fifth root of unity,
1+epsilon^3 is nonzero and epsilon^3-1 is nonzero. Thus
2+(1+epsilon^3)x^3 q_0(x^5) is a nonconstant polynomial with constant
term 2. It has a nonzero complex root x_0, at which q_0(x_0^5) is also
nonzero. Root multiplicity does not enter the rest of the proof.

At the specified point in the smooth three-dimensional chart, the
f=0 fiber of the two defining equations is locally zero-dimensional:
the first equation has distinct fifth-root branches, and the second
restricts to a nonzero one-variable polynomial on the selected branch.
The generalized principal ideal bound gives local dimension at least
one, and the dimension inequality after quotienting by f gives dimension
at most one. Therefore a dimension-one irreducible component through
the point is not contained in f=0.

These uses match the exact primary statements of
[Stacks Lemma 10.60.12](https://stacks.math.columbia.edu/tag/0BBZ)
and [Lemma 10.60.13](https://stacks.math.columbia.edu/tag/00KW).
Normalization is finite and birational for this integral finite-type
curve by [Lemma 33.27.1](https://stacks.math.columbia.edu/tag/0BXR),
and the local ring at a point over the selected closed point is a DVR
by [Lemma 33.43.8](https://stacks.math.columbia.edu/tag/0B8Y).
The residue field is C. These statements allow ramification and singular
or multiple roots in the original curve.

In that DVR, f has positive valuation, while x_1, x_2, h, and
r_2-r_1 are units. Thus tau=(r_2-r_1)/(f^n h) has negative valuation.
The two displayed endpoints are genuine integral points of the original
physical affine four-space. The exact r and x flow formulas send one
endpoint to the other, using x_i h=r_i^2+f^(2n+1). The defining second
curve equation makes the t displacement

\[
\tau\left(1+q(r_1+r_2)/2\right)
\]

zero. The old y,z values follow from their rational reconstruction at
the endpoints. A polynomial slice would therefore have an integral
endpoint difference equal to the nonintegral element tau. This is a
contradiction in every possible polynomial degree.

## 4. Degree boundaries and exact controls

I also checked the additional low-degree conclusions in Sections 5-6.
After f-localization, the monic presentation has basis x^j r^epsilon
with epsilon in {0,1}. Their D-degrees 2j+epsilon are distinct. The first
five reductions are x^0,x^3,x^1,x^4,x^2 over C[x^5], so a highest f-pole
in their invariant coefficients cannot cancel. This proves the stated
description of ker D^5 without silently inverting h.

The affine comparison forces a to divide q. In the quadratic comparison,
the first two equations in (21) give a | b_0 q^2, and the third gives
b_0=1 modulo a, hence a | q^2. The converses use actual polynomial
slices. When a | q^3, the choice H=q^2*X*rho/2 satisfies the required
congruence and gives exactly the cubic formula (22). Its highest
t-coefficient is nonzero when q is nonzero. Together with the quadratic
obstruction, this proves the stated exact cubic regime, but not an
unclaimed formula in every higher-degree regime.

Independent inline SymPy controls passed for
(n,q)=(3,f), (4,f), (5,f(1+h)), and (2,f). For each case I checked the
finite inverse defining H, f^n-divisibility of the corrected numerator,
E(sigma)=1, preservation of Xh-rho^2, and the reduced unit-slope identity.
These are 20 exact controls. The constructed t-degrees were respectively
3, 4, 5, and 2; these observations alone are only upper bounds.

Five additional exact controls checked the compact sigma_0 identity,
the full cubic expansion, its derivative, the factored endpoint
t-displacement, and the quadratic coefficient expansion. All 25 controls
passed. They corroborate the written universal arguments; they are not
substitutes for them, and no finite set of examples establishes the
all-degree negative direction.
