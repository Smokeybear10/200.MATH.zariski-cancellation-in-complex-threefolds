# Two complete coefficient classifications for the fixed DG base

Date: 2026-09-17. Private working proof; novelty UNKNOWN.
General complex-threefold cancellation remains UNSOLVED.

This note combines the held necessary reduction611 with the separately
reviewed residual-family proof612. It also proves a classification of
all invariant coefficients, without a degree bound. These are statements
about one explicitly fixed three-variable derivation, not an entry
theorem for arbitrary sliced derivations on a polynomial four-ring.

## 1. Fixed notation and whole polynomial flow

In R=C[x,y,z], put

\[
 f=xz-y^2,\qquad r=x^3+yf,\qquad
 g=zf^2+2x^2yf+x^5,\qquad H=\operatorname{Jac}(f,g,\cdot).
\]

The polynomial identities and faithful localization used below are

\[
 Hf=Hg=0,\quad Hr=-fg,\quad Hx=-2fr,\quad Hy=6x^2r-g,
\]
\[
 Hz=2x(5x^3y+x^2z^2+3xy^2z-4y^4),\qquad
 R_{fg}=\mathbb C[f^{\pm1},g^{\pm1},r],\quad H=-fg\partial_r,
\]
\[
 x=(r^2+f^3)/g,\quad y=(r-x^3)/f,\quad
 z=(g-2x^2r+x^5)/f^2.
\]

In particular f,g are algebraically independent. The finite r-degrees
2,6,10 of x,y,z show that H is locally nilpotent on the original R.
Write Phi_v for its finite polynomial flow, not merely the localized
translation in r. A polynomial slice for a derivation E means a whole
polynomial U with EU=1. Rectification means an actual polynomial
coordinate system (Z_1,Z_2,Z_3,T) with EZ_i=0 and ET=1.

## 2. Every homogeneous degree-five coefficient

**Theorem.** For any psi in R_5, including zero, the following are
equivalent for E=H+(1+psi)partial_t on R[t]:

1. E has a polynomial slice.
2. psi=H(L) for a homogeneous linear polynomial L in R.
3. E is polynomially rectified.

Thus every sliced member has polynomial kernel C^[3]. The allowed
coefficient space is the three-dimensional space H(R_1), not the
four-dimensional space Cg+H(R_1) that passes the two return tests.

**Necessity.** The exact full-coefficient reduction in
[611](rank-three-dg-degree-five-joint-return-reduction-pass611-working.md)
gives psi=lambda*g+H(L). It includes all 21 complex coefficients and
all four primitive fifth roots; it is not a rational-grid result.
The actual shear T=t-L changes E to H+(1+lambda*g)partial_T.
The residual-family theorem in
[612](rank-three-dg-invariant-coefficient-slice-classification-pass612-working.md)
then forces lambda=0. Its two proofs exclude every whole slice for
nonzero lambda, not just slices of bounded degree.

**Sufficiency and inverse.** If psi=H(L), let T=t-L. This is a
polynomial coordinate change fixing R, and ET=1. In the coordinates
(x,y,z,T), extend H by HT=0. This is a new extension of the base H;
one must not instead extend H by Ht=0 in the old coordinates when
using the following exponential. Set

\[
 (Z_1,Z_2,Z_3)=\Phi_{-T}(x,y,z).
\]

These are whole finite polynomials, E=H+partial_T kills them, and
the inverse is

\[
 (x,y,z)=\Phi_T(Z_1,Z_2,Z_3),\qquad
 t=T+L\bigl(\Phi_T(Z_1,Z_2,Z_3)\bigr).
\]

The polynomial flow group law checks both substitution orders.
Rectification implies a slice by taking T. Finally Hx,Hy,Hz have
distinct H-degrees 1,5,9, so H(R_1) has dimension three. This proves
all equivalences, including psi=0.

## 3. All invariant coefficients, with no degree restriction

**Theorem.** Let h be any polynomial in the independent invariants
f,g, and E_h=H+h(f,g)partial_t. Then

\[
 E_h\text{ has a slice}\quad\Longleftrightarrow\quad
 E_h\text{ is rectified}\quad\Longleftrightarrow\quad
 h=c+fgP(f,g),\quad c\in\mathbb C^*,\ P\in\mathbb C[f,g].
\]

The proof uses both invariant axes. It does not substitute absence
of fixed points for the stronger slice condition.

### Necessity on the f=0 axis

Suppose h(0,b)=0 with b nonzero. Choose a^5=b and a primitive fifth
root omega. There are unique formal unit roots X_i(s) of

\[
 X^6-bX+s^3=0,\qquad X_1(0)=a,\quad X_2(0)=\omega a,
\]

because the X-derivative at each initial root is 5b. The points
p_i=(X_i,0,s/X_i) are integral formal base points with f=s,g=b,
r=X_i^3. Their connecting H-time is

\[
 \tau=-(X_2^3-X_1^3)/(sb),
\]

which has order -1 and nonzero leading coefficient. The localized
coordinate reconstruction proves that this time connects every base
coordinate. Since h(s,b) is divisible by s, the full E_h endpoints

\[
 (p_1,0),\qquad (p_2,h(s,b)\tau)
\]

both lie in C[[s]]^4. The t-displacement need not be zero; its
integrality suffices. A polynomial slice would have an integral
difference at these endpoints equal to the pole tau, a contradiction.

### Necessity on the g=0 axis and at the origin

Suppose h(a,0)=0 with a nonzero, and choose b with b^2=-a. The
integral base endpoints (0,b,s/a^2) and (0,-b,s/a^2) have
f=a,g=s and r=ab,-ab, respectively. Formula Hr=-as gives time

\[
 \tau=2b/s.
\]

Faithful localized reconstruction again connects all base coordinates.
The full endpoints with t-values 0 and h(a,s)*tau are integral,
because h(a,s) is divisible by s. The same pole contradiction applies.

If h(0,0)=0, the whole derivation E_h vanishes at every point with
x=y=0. A derivation vanishing at a point cannot send a polynomial to
one. Thus a sliced E_h has neither of the preceding axis zeros,
including their common origin.

Over C a univariate polynomial without a zero is a nonzero constant.
Consequently h(0,g) and h(f,0) are constants. They have the same
value c=h(0,0), which is nonzero. Since f,g are independent,

\[
 h-c\in(f)\cap(g)=(fg)\quad\text{in }\mathbb C[f,g].
\]

This is precisely the necessary form asserted in the theorem.

### Sufficiency as a whole coordinate change

For h=c+fgP, use the actual polynomial coordinate

\[
 T=(t+rP)/c,
\]

with inverse t=cT-rP. It satisfies ET=(h-fgP)/c=1. In this actual
frame extend the base H by HT=0, so E=H+partial_T. The same finite
flow as in Section2 gives full rectification and its polynomial inverse.
There is no localized-to-global inference here.

More generally a displayed coefficient h(f,g)+H(F), with arbitrary
F in R, can first be reduced to h by the actual shear t-F. The same
criterion therefore applies to any such supplied decomposition. This
does not assert that every coefficient admits that decomposition.

## 4. Scope, proof dependencies, and the unresolved entry step

Section2 depends on the complete saved proofs611 and612. Section3
has the direct proof above; its first formal return is the one in612,
now with possibly nonzero but integral t-displacement. All arguments
are over C. No extension to other base derivations or arbitrary
nonhomogeneous, noninvariant coefficients is established.

These classifications do not place an arbitrary sliced LND on C^[4]
in the specified fixed-base form. That remains an independent missing
step. In particular, proving entry into a triangularizable base would
already resolve cancellation: that base has an invariant ambient
coordinate, and the regular-kernel theorem of
[Bhatwadekar--Gupta--Lokhande, Theorem3.5](https://arxiv.org/html/1501.01438v1)
then applies. A slice makes the kernel regular because the slice
hypersurface has unimodular gradient. The coordinate-entry issue
cannot be assumed away by a normal-form choice.

No novelty, human expert review, or formal-assistant certification is
claimed. No saved checker was executed, imported, or compiled. Author
and independent saved-source reviews must be recorded separately in
the research ledger; a written proof is not its own review certificate.
