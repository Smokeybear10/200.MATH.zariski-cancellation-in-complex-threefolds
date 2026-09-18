# Exact classification for all polynomial local-slice coefficients

The canonical primitive rank-three family admits a complete slice and
polynomial-kernel classification for every added coefficient in
C[f,h,r], not only coefficients linear in r. The criterion consists
of two polynomial remainder tests, one for each component of the
reduced plinth. Both are necessary in every possible slice degree.

This is a complete working argument over the complex numbers,
subject to independent checking and unresolved mathematical priority.
It does not treat every coefficient in C[x,y,z] or every sliced
derivation on C^[4].

## 1. Statement and exact remainder tests

Fix n>=1 and put
\[
R=\mathbb C[x,y,z],\quad f=xz-y^2,\quad a=f^n,\quad \nu=2n+1,
\]
\[
r=x^3+ay,\quad h=a^2z+2ax^2y+x^5,\quad
D=-\operatorname{Jac}(f,h,\cdot),\quad p=ah.
\tag{1}
\]
The established base facts are
\[
\ker D=\mathbb C[f,h],\quad Dr=p,\quad Dx=2ar,\quad
xh=r^2+f^\nu.
\tag{2}
\]
The derivation is primitive of rank three, with plinth ideal (p).
These are inherited from the canonical local-slice construction.[^1]
The [full base proof](polynomial-curve-lift-pass18.md) includes n=1.

Let b belong to C[f,h,r]. Write
\[
F(f,h,r)=\int_0^r b(f,h,v)\,dv,\qquad c=b(0,0,0),
\qquad E=D+b\partial_t.
\tag{3}
\]
This is a polynomial antiderivative, with zero r-constant term.
The derivation E is locally nilpotent, since its added coefficient
belongs to the base and D is locally nilpotent.

**Theorem.** E has a polynomial slice if and only if c is nonzero
and both of the following exact remainders have the indicated form:
\[
\begin{aligned}
F(0,h,r)\bmod(r^5-h^3)&=cr+H_f(h),\\
F(f,0,r)\bmod(r^2+f^\nu)&=cr+H_h(f).
\end{aligned}
\tag{4}
\]
Every positive case has global polynomial coordinates with E a
coordinate partial and hence has kernel C^[3].

The remainders are uniquely defined by monic division in r, of
degrees less than five and two respectively. The coefficient c
in both tests is the same constant from (3), not a freely selected
function of the surviving invariant. The constant terms satisfy
H_f(0)=H_h(0)=0 automatically.

For b=1+qr, (4) reduces exactly to f|q, recovering the
[previous classification](radical-noninvariant-pass22.md).
For invariant b=b(f,h), it reduces to b=c modulo fh, with c nonzero,
as required by the earlier invariant-extension criterion.
For b=1+f*r^2 the first test passes but the second fails:
its odd remainder coefficient is 1-f^(nu+1)/3.
Thus vanishing of a perturbation along f alone is not a general
slice criterion once higher powers of r are admitted.

## 2. Fixed points force the nonzero constant

On the line x=y=0, all of f,h,r vanish and D vanishes.
For clarity, direct differentiation gives
\[
Dy=h-6x^2r,\qquad
Dz=-10x^4y-8axy^2-2ax^2z.
\tag{5}
\]
Consequently E vanishes there when c=0. A derivation vanishing
at a point cannot send a polynomial to one. Hence a slice
forces c nonzero.

## 3. Necessity of the f-divisor condition

Assume c nonzero. Define P(u)=F(0,u^5,u^3).
Its lowest-degree term is c*u^3. The first condition in (4)
is equivalent to
\[
P(u)=cu^3+\text{a polynomial in }u^5.
\tag{6}
\]
Indeed the substitution h=u^5,r=u^3 has kernel (r^5-h^3);
the five monic remainder powers r^0,...,r^4 have distinct
exponent classes modulo five.

If (6) fails, choose a nontrivial fifth root epsilon. The polynomial
\[
\frac{P(u)-P(\epsilon u)}{u^3}
\tag{7}
\]
has nonzero constant c*(1-epsilon^3) and positive degree.
It therefore has a nonzero complex root u_0. The root is not
assumed simple.

In the smooth chart with coordinates f,x_1,x_2 and x_1*x_2 inverted,
put h_i=x_i^5+f^nu/x_i, r_i=x_i^3 and impose
\[
h_1=h_2,\qquad
F(f,h_1,r_1)=F(f,h_1,r_2).
\tag{8}
\]
The point (0,u_0,epsilon*u_0) satisfies these equations.
Its zero-f fiber is locally zero-dimensional: the first equation
has distinct fifth-root branches, and on the selected branch the
second is the nonzero polynomial used in (7).

The dimension bounds for two equations in a regular local
threefold therefore provide a curve component through the point
not contained in f=0. Its normalized local ring V is a DVR.[^2]
In V, f has positive valuation, while x_1,x_2,h=h_1 and
r_2-r_1 are units.

Use the actual integral endpoints
\[
P_i=(x_i,0,f/x_i,0)\in\mathbb A^4(V),\qquad
\tau=(r_2-r_1)/(ah).
\tag{9}
\]
The parameter tau has negative valuation. Over the fraction field,
the E-flow carries r_1,x_1 to r_2,x_2. Its t-displacement is
\[
\frac{F(f,h,r_2)-F(f,h,r_1)}{ah}=0.
\tag{10}
\]
The remaining base coordinates follow from the f-localized
presentation. Thus both endpoints lie on the same orbit with
nonintegral parameter tau. A polynomial slice would have integral
endpoint difference equal to tau, a contradiction.
This proves the first condition in every degree.

## 4. Necessity of the h-divisor condition

Write the second monic remainder as
\[
F(f,0,r)\bmod(r^2+f^\nu)=A(f)+rB(f).
\tag{11}
\]
Its coefficient B satisfies B(0)=c. If B is not the constant c,
it has a nonzero root f_0. Choose r_0 with r_0^2=-f_0^nu,
so r_0 is nonzero.

The odd part of F, divided by r, is polynomial in r^2. Define
\[
\Gamma(f,h)=
\left.\frac{F(f,h,r)-F(f,h,-r)}{2r}
\right|_{r^2=h-f^\nu}.
\tag{12}
\]
This is polynomial and Gamma(f,0)=B(f).
Near (f_0,0,r_0), impose the two equations
\[
r^2=h-f^\nu,\qquad \Gamma(f,h)=0.
\tag{13}
\]
The zero-h fiber is locally zero-dimensional, because B is a
nonzero polynomial with a root at f_0. The same dimension and
normalization argument gives a DVR V with h of positive valuation
and f,r units. This again allows multiple roots.

Take r_1=r,r_2=-r and the integral physical points
\[
x_i=1,\quad y_i=(r_i-1)/a,\quad z_i=f+y_i^2,\quad t_i=0.
\tag{14}
\]
Their canonical invariants are f,h and their local-slice values r_i.
The parameter tau=-2r/(ah) has negative valuation.
The r and x flow formulas connect the endpoints; x is unchanged
because r_1^2=r_2^2. Equation (13) and (12) make (10) zero.
A slice again contradicts integrality of its endpoint difference.
Therefore B(f)=c, which is the second condition in (4).

## 5. A polynomial gauge removes the non-nilpotent part

Assume both tests hold. Use the embedded surface ring
\[
S_0=
\mathbb C[f,h,x,r]/(xh-r^2-f^\nu)\ \subset R.
\tag{15}
\]
It is a domain and its f-localization is exactly R_f.
Both S_0/(f)=C[h,x,r]/(xh-r^2) and
S_0/(h)=C[f,x,r]/(r^2+f^nu) are domains.
The latter follows because nu is odd. In particular f and h
are distinct prime elements of S_0.

Let H=H_f(h)+H_h(f) and DeltaF=F-cr-H.
By the first test, for a polynomial J(h,r),
\[
\Delta F=J(h,r)(r^5-h^3)+fK(f,h,r).
\tag{16}
\]
By the second test, DeltaF belongs to hS_0: its reduction modulo h
is divisible by r^2+f^nu, which equals xh in S_0.

The essential exact polynomial identity is
\[
G_0=r^5-h^3-f^{2\nu}r=p\,g_0,
\qquad
g_0=-h(x^2y+az)-2x f^{n+1}r\in R.
\tag{17}
\]
To check it, expand
G_0=h^2(x^2r-h)-2xh f^nu r and use
x^2r-h=-a(x^2y+az). Also
G_0=h[xr(r^2-f^nu)-h^2] belongs to hS_0.

Set g=J*g_0. Equations (16)-(17) show that
DeltaF-pg belongs to fS_0 and hS_0. Their intersection is fhS_0:
for example, reduce f times a quotient modulo the prime h.
Consequently there is an actual polynomial element ell in fS_0 with
\[
F-cr-H-pg=h\ell.
\tag{18}
\]
All operations are finite polynomial division and reduction in the
monic presentation (15). In particular ell can be represented by
a polynomial in f,h,x,r whose coefficients are divisible by f.

Define delta_0=D/a on S_0. This is the polynomial derivation
delta_0(x)=2r, delta_0(r)=h, fixing f,h. Differentiating (18) gives
\[
b-Dg=c+\delta_0\ell.
\tag{19}
\]
The genuine polynomial change t'=(t-g)/c therefore puts E into
the form
\[
E=a\delta_0+(1+\delta_0\ell')\partial_{t'},
\qquad \ell'=\ell/c\in fS_0.
\tag{20}
\]
This change preserves the original base R and preserves degree
in the added variable. It does not assert that the original
coefficient was invariant or linearly gaugeable to a constant.

## 6. Universal finite variable-time correction

For readability write ell in place of ell' and t in place of t'.
Represent ell by a polynomial divisible by f in the full coefficient
polynomial ring C[f,h][x,r]. Work there first, with
delta_0=2r*partial_x+h*partial_r and a=f^n.
The derivation in (20) preserves the quadratic level.

Put
\[
L=\ell-at,\quad \rho=r+hL,\quad
X=x+2rL+hL^2,\quad \sigma_0=-L/a=t-\ell/a.
\tag{21}
\]
Directly EL=-a, E(rho)=E(X)=0, E(sigma_0)=1, and
Xh-rho^2=xh-r^2. After inverting a this is an automorphism:
\[
r=\rho+ah\sigma_0,\quad
x=X+2a\rho\sigma_0+a^2h\sigma_0^2,\quad
t=\sigma_0+\ell(f,h,x,r)/a.
\tag{22}
\]
These formulas prove both inverse directions without solving a
high-degree polynomial for r.

Modulo a, the first pair induces
\[
\phi_0(x)=x+2r\ell+h\ell^2,\qquad
\phi_0(r)=r+h\ell.
\tag{23}
\]
It is the identity modulo f, and f is nilpotent modulo a.
The finite geometric inverse of phi_0-id therefore gives a
polynomial automorphism on the full quotient ring, before imposing
the surface equation.

Choose a polynomial lift K of phi_0^-1(-ell) modulo a and set
\[
\sigma=\sigma_0-K(X,\rho)/a.
\tag{24}
\]
The numerator vanishes modulo a, so sigma is polynomial, and
E(sigma)=1. Modulo a, the coefficient 1+delta_0(ell) is a unit:
delta_0(ell) is divisible by f. Thus sigma is affine in t with
unit leading coefficient there, and the whole coordinate map
is an automorphism modulo a.

After inverting a, (24) is an invariant shear of (21).
The [minimal-denominator lemma](radical-noninvariant-pass22.md)
now proves that its inverse is polynomial globally. The entire
map fixes f,h and preserves xh-r^2. It therefore descends to
S_0[t] and to its specified quadratic level.

## 7. Both physical coordinate directions

The reduced surface map and its inverse are independent of t on
the surface variables modulo f^n, preserve the vertex ideal
(x,h,r), and are the identity modulo f. The finite physical lift
from the preceding proof therefore applies, with the following
explicit curve calculation.

In (C[f]/(f^n))[u], put
\[
v(u)=\ell(f,u^5,u,u^3),\quad
U=(1+u^2v)^2,\quad W=u^2(1+u^2v),\quad\psi(u)=uU.
\tag{25}
\]
The order of arguments in ell is f,h,x,r.
Since v is divisible by f, U is a unit and psi has a finite
polynomial inverse. On the old physical curve,
X=uU, rho=uW and h=u^5. Define
\[
\widetilde P=(W/U)\circ\psi^{-1}\pmod{f^n},\quad
Y=(\rho-X\widetilde P)/f^n,
\]
\[
Z=(h-2\widetilde P Yf^n-X\widetilde P^2)/f^{2n}.
\tag{26}
\]
The forward curve identities clear Y. Multiplication of the
Z numerator by X gives f^(2n)(Y^2+f); primality of f and
X=x modulo f clear Z and prove f=XZ-Y^2.

For the independent inverse, start in C[X,Y,Z,sigma], reconstruct
f,rho,h from (26), and use the polynomial inverse from Section 6.
The inverse curve congruence clears the old y denominator.
The same prime-cancellation identity clears the old z denominator.
Both maps are inverse after f-localization and hence globally.
Finally undo the polynomial gauge in Section 5.
This proves the claimed polynomial kernel in every positive case.

The physical lifting principle remains the established full-ideal
affine-modification framework, with explicit curve conditions.[^3]
No new abstract algebraization or cancellation principle is asserted.

## 8. Verification and exact scope

The companion exact checks verify both residue tests in positive
and negative cases, the polynomial G_0 identity, the gauge remainder
construction, variable-time invariants, finite nilpotent inverses,
and both exceptional-divisor orbit formulas.
The universal dimension and inverse arguments are written proofs,
not claims extrapolated from those examples.

The classifier treats b in C[f,h,r]. This is a proper subring of R:
modulo f its elements depend on x through h=x^5 and r=x^3,
whereas y remains a free varying coordinate on the reduced surface.
Thus y is not in that subring. No reduction of an arbitrary
b in R to this class modulo D(R) has been proved here.
The further arbitrary-coordinate-frame gap also remains.

The previous exact affine/quadratic/cubic minimum-degree assertions
for b=1+qr remain valid. No new all-degree minimum formula for the
larger class is claimed. Priority and human expert review remain
unresolved, and the unrestricted cancellation conjecture is not solved.

## Sources

[^1]: N. Dasgupta and S. A. Gaifullin, [*On locally nilpotent derivations of polynomial algebra in three variables*](https://arxiv.org/html/2306.00510v2), Theorem 5.7; G. Freudenburg, [*Canonical factorization of the quotient morphism for a Ga-action on an affine variety*](https://arxiv.org/pdf/1602.08786), Section 8.2. Canonical base and n=1 degree-module credit are unchanged.

[^2]: The Stacks Project, [dimension and principal ideal bounds](https://stacks.math.columbia.edu/tag/00KD), [finite normalization](https://stacks.math.columbia.edu/tag/0BXR), and [normal curve local rings](https://stacks.math.columbia.edu/tag/0B8Y). The same hypotheses checked in the preceding all-q proof apply to each explicit two-equation curve.

[^3]: S. Kaliman and M. Zaidenberg, [*Affine modifications and affine hypersurfaces with a very transitive automorphism group*](https://arxiv.org/pdf/math/9801076), Proposition 2.1 and Corollary 2.2; see the [full-ideal application audit](priority-boundary-pass20.md).
