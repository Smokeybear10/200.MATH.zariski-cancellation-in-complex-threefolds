# Independent audit of the all-q local-slice-linear bridge

The proof in [the main note](radical-noninvariant-pass22.md) passes this
independent algebraic audit. I reconstructed the finite nilpotent repair,
the physical inverse, the algebraic orbit obstruction, and both sharp
low-degree criteria. In particular, the cubic conclusion is a minimum
degree statement in its specified regime, not merely an example of a
cubic slice.

This audit does not establish priority, formal verification, expert
review, or a reduction of arbitrary slice derivations to this family.
The ambient complex cancellation question remains open in this project.

## 1. Exact scope checked

Use the main note's canonical family with n>=1, a=f^n,
C=ker D=C[f,h], Dr=ah, Dx=2ar and
xh=r^2+f^(2n+1). For every q in C, the audited assertions are:

- D+(1+qr)*partial_t has a polynomial slice exactly when f divides q.
- Every positive case has polynomial kernel, via a finite coordinate
  construction with a polynomial inverse.
- A slice of t-degree at most one exists exactly when a divides q.
- A slice of t-degree at most two exists exactly when a divides q^2.
- If q is nonzero and a divides q^3 but not q^2, the minimum t-degree
  is exactly three.

The q=0 case is included: t is a slice, and no degree-zero slice exists
because D has no slice. No minimum-degree formula is asserted in the
remaining positive range a not dividing q^3. The construction still
terminates there.

## 2. The nilpotent repair really is a polynomial automorphism

Work first over the Q-domain Lambda in Section 2. The forward invariant
pair X,rho preserves xh-r^2, and the known rational slice sigma_0 gives
an automorphism after inverting a. These statements concern the full
polynomial ring Lambda[x,r,t], before imposing a surface relation.

Modulo a the first two coordinates give an endomorphism phi_0 that is
the identity modulo the nilpotent principal ideal (q). Because phi_0
fixes the coefficient ring, the additive operator Delta=phi_0-id raises
the q-adic filtration. Its finite geometric inverse is valid even
though Delta is not a derivation. A bijective unital ring homomorphism
has a ring-homomorphism inverse, so the finite additive calculation
proves an actual ring automorphism.

The polynomial H is chosen from phi_0 inverse applied to the residue K
of a*sigma_0. Consequently H(X,rho) and a*sigma_0 agree modulo a in the
full polynomial ring. The corrected sigma is therefore polynomial,
not just regular on a dense open set. Since H is invariant, E(sigma)=1.

The reduction of sigma is affine in t: modulo a,
E=(1+qr)*partial_t, and 1+qr is a unit. The coefficient ring is a
Q-algebra, so the derivative equation eliminates every higher t-term,
including over its possibly nonreduced quotient. Together with phi_0,
this gives the full reduced automorphism.

The denominator lemma then applies exactly as stated. If a localized
inverse has minimal denominator a^m with m>0, injectivity modulo a
forces its numerator into (a), reducing m. This does not require a to
be prime or a nonreduced center to be replaced by its support. It uses
a domain and the fact that the endomorphism fixes a. The polynomial
automorphism preserves xh-r^2 and hence descends to the specified level.

## 3. Both physical directions retain the necessary thickening

The quotient modulo f^n is essential here. On the universal curve
(x,h,r)=(u,u^5,u^3), direct substitution gives
X=uU, rho=uW with the U and W of the main note. Since f divides q,
U is a unit and psi(u)=uU is the identity modulo f. Its inverse is
finite over (C[f]/(f^n))[u]. The resulting Ptilde satisfies both
rho=X*Ptilde and h=X*Ptilde^2.

Cancellation in the second identity occurs by the independent
indeterminate u and a unit in that universal polynomial ring. The
inverse curve identities are established there before base change.
They do not divide by a specialized X or x that may be a zero divisor
in a nonreduced quotient.

For the physical forward map, the first curve identity clears the
f^n denominator of Y. Multiplying the numerator of Z by X gives
f^(2n)(Y^2+f). In the physical four-variable polynomial ring f is prime,
and X=x modulo f is not divisible by f. Thus the entire f^(2n)
denominator clears. This is stronger than checking the reduced curve.

The independent inverse starts in C[X,Y,Z,sigma] with f=XZ-Y^2.
It uses the already polynomial surface inverse, then the inverse curve
congruence to clear the old y denominator. The same prime-cancellation
identity clears the old z denominator. The maps agree with mutually
inverse maps after inverting f, so they are inverse polynomial maps
globally. This verifies the claimed polynomial kernel, rather than
only a polynomial slice.

## 4. The nonsimple-root orbit obstruction is valid

When q(0,H) is nonzero, the one-variable polynomial in Section 4 is
nonconstant and has nonzero constant term. It has a nonzero complex
root; no simplicity assumption is needed. At the selected point,
x_1, x_2 and h are units, and the residue of r_2-r_1 is nonzero.

The equations defining the algebraic curve have a zero-dimensional
local fiber over f=0. The distinct fifth-root branches of the first
equation separate near the chosen point, and the second equation is
a nonzero one-variable polynomial on the selected branch. The
principal ideal height bound in a regular three-dimensional ambient
local ring supplies a component of dimension at least one. Since its
zero fiber is zero-dimensional, a one-dimensional component through
the point is not contained in f=0. Normalizing that algebraic curve
supplies the stated DVR. Multiple roots only allow ramification; they
do not invalidate the construction.

The two endpoints are actual V-points of the original four-space.
The displayed flow sends their r and x coordinates to each other.
Their y and z coordinates then agree by the defining identities,
using f nonzero in the fraction field and the endpoint x-coordinates
being units. The second curve equation makes the t displacement zero.
The resulting orbit parameter has negative valuation, whereas any
polynomial slice would give that parameter as the difference of its
two integral endpoint values. This is a contradiction in the DVR.

Thus the argument excludes slices of every degree when f does not
divide q. It is not merely a failure of the proposed positive formula,
a formal arc calculation, or a finite numerical search.

## 5. Quadratic sharpness and cubic minimality

I independently reconstructed the degree-four invariant module used
in Section 5. In the f-localized monic presentation, the five basis
elements 1,r,x,xr,x^2 have D-degrees 0,1,2,3,4. Their residues have
distinct exponents modulo five over C[h]=C[x^5]. A highest f-pole
therefore cannot cancel. This justifies the exact module description,
not just a spanning statement after localization.

For an affine slice A*t+v, coefficient comparison puts A in C and
v in C+Cr+Cx. The resulting equations imply A=1 modulo a and a
divides A*q. Hence a divides q. The displayed affine slice proves
sufficiency.

For a quadratic slice A*t^2+B*t+C_0, the coefficient equations force
A=ahU and B=b_0-2Ur-hqUx with U,b_0 in C. Comparing the r and x
coefficients in the final derivative equation gives

\[
ac_3=qU,\qquad 2ac_2=2U-b_0q.
\]

Multiplying the second equation by q and using the first shows that
a divides b_0*q^2. Comparing constants after the same substitution
gives ah*c_1=1-b_0, so b_0=1 modulo a. Therefore a divides q^2.
This includes A=0 and does not assume the putative slice has exact
degree two. When a divides q^2, sigma_0 is polynomial, proving the
reverse implication.

If a divides q^3, the choice H=q^2*X*rho/2 has the required residue:
all corrections in phi_0(H)-K contain q^3. Its corrected slice is
the displayed equation (22). I checked independently that the
displayed expansion equals sigma_0-q^2*X*rho/(2a) and that its exact
derivative is one. For q nonzero, its t^3 coefficient is nonzero.
When a does not divide q^2, the preceding necessity proof excludes
all lower degrees. This establishes exact minimum degree three in
the stated adjacent regime.

## 6. Exact controls and editorial precision

Separate inline SymPy controls were actually run, without importing
project solvers:

- Four cases n=3,4 and q=f or f*(1+h) checked an independently built
  finite inverse modulo f^n, polynomiality of the repaired slice,
  derivative one, and the reduced affine t-slope. Both n=3 cases had
  exact t-degree three. This run completed in 0.941 seconds.
- A universal rational-identity check compared equation (22) with
  sigma_0-q^2*X*rho/(2a) and independently differentiated the displayed
  equation. Both identities passed in 0.393 seconds.

These are inline controls, not additional unittest methods or a new
regression suite. The written all-parameter arguments carry the
universal claims. The main agent maintains the separate regression
counts and results.

No mathematical correction was required by this audit. Two minor
precision suggestions were sent to the main author:

- Link the base proof for n=1 directly, since the immediately
  preceding pass21 note states n>=2. The wider
  [polynomial-curve proof](polynomial-curve-lift-pass18.md) covers n=1.
- Beside the orbit endpoint reconstruction, z=(f+y^2)/x uses the
  invertibility of the endpoint x-coordinate in addition to f.
  Either state that explicitly or use the fully f-localized identity
  z=(h-2x^2*y*f^n-x^5)/f^(2n). The endpoint argument itself is valid.

This audit intentionally does not infer family-level novelty from
the lack of an immediate literature match. It also does not prove
that arbitrary noninvariant coefficients can be put in the form 1+qr,
or that arbitrary slice derivations admit the required base frame.
