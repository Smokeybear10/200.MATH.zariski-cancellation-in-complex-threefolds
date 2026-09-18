# Second independent audit of polynomial local-slice coefficients

The complete [polynomial-coefficient classification](polynomial-local-slice-coefficients-pass23.md)
passes this second independent audit. Both remainder conditions are
necessary in every slice degree, and their conjunction gives the
claimed polynomial gauge and global polynomial coordinate inverse.
I found no mathematical defect in the proof as written.

The scope is exactly b in C[f,h,r] for the stated canonical primitive
rank-three base, with n>=1 over C. This is not a classification for
arbitrary b in the full physical ring, an arbitrary slice derivation,
or general cancellation. No priority or expert-review conclusion is
part of this audit.

## 1. Statement and compatibility of the two remainders

Retain a=f^n, nu=2n+1, p=ah and
F(f,h,r)=integral from zero to r of b(f,h,v)dv. Because b belongs
to the polynomial ring C[f,h,r], F is an actual polynomial with no
r-constant term. The coefficient of its linear r-term at f=h=0
is c=b(0,0,0).

The two monic remainder tests are well-defined. The substitution
h=u^5, r=u^3 has kernel (r^5-h^3). For the monic remainder of
r-degree less than five, the powers r^j have distinct exponent
classes 3j modulo five. This proves the equivalence with the stated
one-variable restriction P(u)=cu^3 plus a polynomial in u^5.
The second quotient has unique form A(f)+rB(f).

The two constant remainder terms H_f and H_h vanish at zero,
because F itself has zero r-constant term. Thus H=H_f(h)+H_h(f)
has the correct restriction on both components; no compatibility
constant is silently discarded. The coefficient c is fixed by b,
not an adjustable unit function on either component.

At x=y=0 the base derivation vanishes and f,h,r are all zero.
Consequently c=0 supplies actual fixed points of E and excludes
every possible slice. This also verifies the constant boundary.

## 2. Necessity on f=0 is an all-degree orbit argument

If the first remainder condition fails, P(u)=F(0,u^5,u^3) has
lowest term cu^3 and an additional term with exponent not divisible
by five. Every nontrivial fifth root epsilon has order five. Hence
(P(u)-P(epsilon*u))/u^3 has nonzero constant term and positive
degree. It has a nonzero complex root, without any simplicity
assumption.

At the resulting selected point, the equations h_1=h_2 and
F(f,h_1,r_1)=F(f,h_1,r_2) have a zero-dimensional local fiber over
f=0. The distinct fifth-root branches separate locally, and the
second equation is a nonzero one-variable polynomial on the chosen
branch. Two equations in the regular local threefold then give a
curve component not contained in f=0. Normalization supplies the
DVR used in the proof, even when the selected root is multiple.

Both endpoints are actual integral points of the original physical
four-space. Their x-values and common h are units, while f has
positive valuation and r_2-r_1 is a unit. Thus
tau=(r_2-r_1)/(ah) has negative valuation. The base flow connects
the endpoints by Dr=ah, Dx=2ar and the quadratic level relation.
The polynomial antiderivative gives its t-displacement exactly as
(F(r_2)-F(r_1))/(ah), which is zero by the defining curve equation.

A polynomial slice would identify this nonintegral tau with a
difference of two integral endpoint values. This contradiction
excludes slices in every degree. It does not merely refute the
proposed constructive formula.

## 3. Necessity on h=0 uses a different valid pair of endpoints

For the second remainder, B(0)=c is nonzero. If B is not constant,
it has a nonzero root f_0 over C. A root r_0 of r_0^2=-f_0^nu
is also nonzero. The odd-part expression Gamma in the note is a
polynomial because the odd part divided by r is polynomial in r^2.
It specializes to B(f) at h=0.

The equations r^2=h-f^nu and Gamma(f,h)=0 again have a
zero-dimensional local zero-h fiber at the selected point. The
same curve and normalization argument gives a DVR with h of
positive valuation and f,r units. No simple-root assumption enters.

The endpoints x_i=1, y_i=(r_i-1)/a, z_i=f+y_i^2 and t_i=0,
with r_1=r and r_2=-r, are integral because a is a unit there.
Their physical f-values are f, and the identity xh=r^2+f^nu
recovers exactly the common h. The flow parameter -2r/(ah) has
negative valuation. Its x-displacement is zero, its r-displacement
switches the signs, and Gamma=0 makes its t-displacement zero.
The same slice-integrality contradiction proves B(f)=c.

The different endpoint constructions are necessary: f is small and
h is a unit in the first, while h is small and f is a unit in the
second. Neither proof assumes that the other divisor has a generic
reduced fiber or that a formal root algebraizes without explanation.

## 4. The polynomial gauge really removes the residual obstruction

The embedded surface ring
S_0=C[f,h,x,r]/(xh-r^2-f^nu) has the stated f-localized physical
presentation. Its two quotients by f and h are domains. For h this
uses the odd exponent nu, so r^2+f^nu is irreducible; for f it is
the integral quadratic cone. Thus f and h are distinct prime
elements and (f) intersect (h)=(fh) in S_0.

The key expression

\[
G_0=r^5-h^3-f^{2\nu}r
\]

has both required properties. Expanding r^2=xh-f^nu gives
G_0=h^2(x^2r-h)-2xh f^nu r. The physical identity
x^2r-h=-a(x^2y+az) then proves exactly G_0=p*g_0 with the
polynomial g_0 displayed in the note. Independently,
G_0=h[xr(r^2-f^nu)-h^2] belongs to hS_0. The fact that g_0
need not itself lie in S_0 does not cause a problem: its product
with p is precisely the element G_0 of S_0 used for subtraction.

The first remainder condition writes DeltaF as
J(h,r)(r^5-h^3)+fK. Subtracting p*Jg_0 leaves an element of
fS_0 because its additional term J*f^(2nu)*r is divisible by f.
The second test already places DeltaF in hS_0, and G_0 also lies
there. Hence the difference is in fhS_0. Dividing by h therefore
gives a genuine ell in fS_0, not just a rational element regular
at some points.

Differentiating the resulting equation is legitimate because
DF=pb, Dr=p and D fixes f,h,p. Cancellation of the nonzero p
gives b-Dg=c+delta_0(ell). Thus the polynomial shear and constant
rescaling t'=(t-g)/c yield the claimed canonical coefficient.
This is not an assertion that the original coefficient is invariant
or that every b in the full physical ring has such a gauge.

## 5. Nonlinear variable time has a genuine independent inverse

On the full coefficient polynomial ring, not only the surface,
E=a*delta_0+(1+delta_0(ell))*partial_t and L=ell-at satisfy
EL=-a. The pair rho=r+hL and X=x+2rL+hL^2 is invariant and
preserves xh-r^2. With sigma_0=-L/a, the displayed inverse formulas
recover r,x and then t after inverting a. These formulas substitute
the recovered r,x into ell. They do not solve an implicit polynomial
equation involving ell, so arbitrary nonlinear dependence on x,r
does not invalidate the inverse.

Modulo a, the first pair is the identity modulo the nilpotent ideal
(f). Its additive difference from the identity raises f-adic order,
so the finite geometric inverse is an actual ring automorphism.
Choosing K as a lift of its inverse applied to -ell makes
sigma=sigma_0-K(X,rho)/a polynomial in the full ring. The numerator
vanishes modulo a before any surface relation is imposed.

The derivative of sigma is one. Modulo a the t-coefficient of E
is a unit, and the Q-algebra derivative identity makes sigma affine
in t with unit slope. Thus the full reduced coordinate map is an
automorphism. After inverting a the correction is an invariant
shear. The previously proved minimal-denominator lemma therefore
gives a polynomial global inverse. There is no unproved formal
power-series algebraization at this step.

## 6. Both physical denominator clearings remain valid

The map and its inverse preserve the vertex modulo f^n, are
independent of t on the surface variables there, and are the identity
modulo f. The arbitrary value of ell at x=h=r=0 causes no issue:
its added terms in X,rho contain r or h, so the vertex is preserved.

On the universal physical curve, the formulas give exactly
X=u(1+u^2v)^2, rho=u^3(1+u^2v), h=u^5. Since v is divisible
by f, all inversions used to define Ptilde are finite polynomial
operations modulo f^n. Curve identities are established before
base change, including the inverse parameter identity.

The forward curve congruence clears Y. Multiplying the numerator
of Z by X gives f^(2n)(Y^2+f), and f is prime in the physical
polynomial ring while X=x modulo f is not divisible by f. This
clears the full f^(2n) denominator. In the independent coordinate
ring for the inverse, f=XZ-Y^2 is again prime, and recovered x is
X modulo f. The inverse curve identity clears old y, and the same
prime-cancellation argument clears old z. The two maps are inverse
after f-localization and therefore globally. Undoing the polynomial
gauge is then polynomial as well.

## 7. Independent exact controls and final boundary

Separate inline SymPy commands were actually run without importing
any project solver or companion checker:

- The physical identity p*g_0=G_0 and the derivative
  Dg_0=5r^4-f^(2nu) were checked using the independently constructed
  physical Jacobian derivation for n=1,2. Twelve positive and negative
  coefficient cases at n=1,2,4 independently reproduced both monic
  remainder tests. This run took 0.209 seconds of measured script time.
- For the nonlinear full-ring choice ell=f*(xr+r^3), both rational
  coordinate inverse compositions, invariance and level preservation
  were checked. Independently constructed finite corrections for
  n=2,3 were polynomial and had derivative one and the required
  unit affine t-slope modulo f^n. The produced slices had t-degrees
  three and five, without any minimality claim. This run took
  0.912 seconds of measured script time.

These are inline controls, not added regression methods. The
all-parameter statements rest on the written arguments audited above.
The base facts and earlier denominator and physical-lift lemmas were
retained with their exact hypotheses; no new external result was
substituted for a missing proof step.

The full physical coefficient ring is larger than C[f,h,r]. For
example, after f=0 and x=1, the values h=r=1 are fixed while y
can vary, so y does not belong to that subring. The note correctly
does not assert that an arbitrary physical coefficient is gauge
equivalent to this class. Nor does it settle the separate arbitrary
slice-frame problem. The audited advance is the complete stated
coefficient-class criterion and its positive polynomial kernels.
