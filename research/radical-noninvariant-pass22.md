# Exact slice criterion for local-slice-linear noninvariant coefficients

For the canonical primitive rank-three family, the added coefficient
1+qr has a slice exactly when q vanishes along f=0. Every positive case
has an explicit finite polynomial coordinate algorithm and polynomial
kernel. This extends the previous q^2-divisibility construction; that
condition is exactly the boundary for a slice of degree at most two,
not the boundary for existence of a slice.

All statements are over C. They are complete working arguments,
not a universal cancellation theorem, a novelty claim, or a Lean proof.

## 1. Exact statement

For n>=1 put
\[
R=\mathbb C[x,y,z],\quad f=xz-y^2,\quad r=x^3+yf^n,\quad
h=zf^{2n}+2x^2yf^n+x^5,\quad D=-\operatorname{Jac}(f,h,\cdot).
\tag{1}
\]
Use C=ker D=C[f,h] and a=f^n. The base is primitive rank three,
with plinth (ah), and
\[
Df=Dh=0,\quad Dr=ah,\quad Dx=2ar,\quad xh=r^2+f^{2n+1}.
\tag{2}
\]
The base, including n=1, is established in the
[polynomial-curve proof](polynomial-curve-lift-pass18.md), with
F(Y)=Y^2 and P(X,f)=X^2. The
[preceding noninvariant proof](primitive-noninvariant-bridge-pass21.md)
uses the same positive-r sign convention and credits the published
local-slice family.[^1]

**Theorem.** For every q in C, let E=D+(1+qr)*partial_t on R[t].
Then:
\[
E\text{ has a slice}\quad\Longleftrightarrow\quad f\mid q.
\tag{3}
\]
In every positive case, there are global polynomial coordinates
X,Y,Z,sigma with E=partial_sigma and ker E=C[X,Y,Z].
For every q, the exact low-degree criteria are
\[
\begin{split}
E\text{ has a slice of t-degree at most 1}
 &\Longleftrightarrow a\mid q,\\
E\text{ has a slice of t-degree at most 2}
 &\Longleftrightarrow a\mid q^2.
\end{split}
\tag{4}
\]
There is no t-degree-zero slice, because D has no slice.
If q is nonzero, write ell=v_f(q). Consequently the minimum degree
is one for ell>=n, two for 2ell>=n>ell, and three for
3ell>=n>2ell. The theorem does not claim an exact minimum degree
when n>3ell>0. It still proves existence and polynomial kernel there.

## 2. A finite nilpotent repair on the abstract polynomial ring

This section works over any Q-domain Lambda containing invariant
coefficients a,q,h, with a nonzero. Suppose q is nilpotent modulo a,
equivalently q^N belongs to a*Lambda for some N>=1.
The case a a unit is immediate from the old rational formulas,
so assume otherwise. On Lambda[x,r,t] use
\[
\mathcal E=2ar\partial_x+ah\partial_r+(1+qr)\partial_t.
\]
Set
\[
L=qx/2-at,\quad \rho=r+hL,\quad X=x+L(r+\rho).
\tag{5}
\]
These are polynomial invariants for arbitrary a,q. Over Lambda[a^-1],
the rational slice and inverse from the preceding proof apply:
\[
\sigma_0=t-qrt-\frac{q^2xh}{2}t+\frac{ahq}{2}t^2
          +\frac{q^2}{2a}xr+\frac{q^3}{8a}x^2h.
\tag{6}
\]
The map (x,r,t)->(X,rho,sigma_0) is an automorphism after inverting a,
fixes Lambda, and preserves xh-r^2.

Let bar Lambda=Lambda/(a). The first two coordinates induce
\[
\phi_0(x)=x+qxr+q^2x^2h/4,\qquad
\phi_0(r)=r+qxh/2
\quad\text{on }\overline\Lambda[x,r].
\tag{7}
\]
This is an automorphism. Indeed it fixes the coefficient ring and is
the identity modulo (q). As an additive operator, Delta=phi_0-id
sends (q)^j*bar Lambda[x,r] into (q)^(j+1)*bar Lambda[x,r].
Thus Delta^N=0, and its inverse is the finite sum
id-Delta+Delta^2-...+(-Delta)^(N-1). This additive inverse of a
unital ring homomorphism is necessarily a ring homomorphism.

Put
\[
K=q^2xr/2+q^3x^2h/8.
\tag{8}
\]
Choose any polynomial lift H(X,rho) of phi_0^-1(K), where the
coefficients also lie in Lambda, and define
\[
\sigma=\sigma_0-H(X,\rho)/a.
\tag{9}
\]
The numerator a*sigma_0 has residue K modulo a. By the definition
of H, H(X,rho) has the same residue. Therefore sigma is polynomial,
and E(sigma)=1 because H is invariant.
This uses a finite quotient and an actual polynomial correction,
not a formal power series asserted to algebraize.

The map F=(X,rho,sigma) is an automorphism modulo a as well.
There E=(1+qr)*partial_t, with 1+qr a unit since q is nilpotent.
From E(sigma)=1, differentiation with respect to t gives
partial_t(sigma)=(1+qr)^-1. The quotient is a Q-algebra, so
sigma is affine in t, with that unit leading coefficient.
The first two coordinates are the automorphism phi_0.

For completeness, the following elementary denominator lemma now
proves that F is a global polynomial automorphism.

**Denominator lemma.** Let B be a domain and let F:B->B fix a nonzero
element a. If F becomes an automorphism after inverting a and its
reduction modulo a is injective, then F is an automorphism.
For b in B, write its inverse image after localization as H/a^m,
with m as small as possible. The equality F(H)=a^m b, reduced
modulo a when m>0, forces H in (a), contradicting minimality.
Thus m=0 for every b. Injectivity follows from the localized map.

Here F becomes an automorphism after inverting a because (9) is
an invariant shear of sigma_0. The lemma therefore applies.
The coordinate pair X,rho is unchanged, so the global map still
preserves xh-r^2. It descends to any specified invariant level
of that polynomial.

## 3. The physical polynomial coordinate algorithm

Return to (1), and assume f divides q. Then q is nilpotent modulo
a=f^n, so Section 2 constructs a polynomial surface-cylinder
automorphism with sigma a slice. Its reduction on the surface
coordinates modulo f^n is independent of t, preserves the vertex
ideal (x,h,r), and is the identity modulo f.
The inverse has the same properties by the finite nilpotent inverse.

Here is the explicit finite curve construction. In
(C[f]/(f^n))[u], set q_u=q(f,u^5) and
\[
U=(1+q_u u^3/2)^2,\qquad W=u^2(1+q_u u^3/2),\qquad
\psi(u)=uU.
\tag{10}
\]
The old physical curve is (x,h,r)=(u,u^5,u^3).
On that curve the forward surface map is
\[
X=uU,\qquad \rho=uW,\qquad h=u^5.
\]
The parameter map psi is the identity modulo f, so it has a finite
polynomial inverse in this quotient. Define
\[
\widetilde P(X,f)=(W/U)\big(\psi^{-1}(X)\big)\pmod{f^n},
\tag{11}
\]
choosing its unique f-degree-less-than-n remainder.
The displayed U is a unit. These are finite polynomial operations
in a coefficient ring with a nilpotent ideal.

The curve identities are rho=X*Ptilde and h=X*Ptilde^2.
The first is immediate from (11); the second follows either directly
from (10) or from Xh=rho^2 on this universal curve, cancelling
the non-zero-divisor u and the unit U. The inverse curve identities
follow from psi^-1, not from inversion of a possibly vanishing point
coordinate after specialization.

Define
\[
Y=(\rho-X\widetilde P)/f^n,\qquad
Z=(h-2\widetilde P Yf^n-X\widetilde P^2)/f^{2n}.
\tag{12}
\]
The first identity makes Y polynomial. Multiplication of the second
numerator by X gives f^(2n)(Y^2+f); f is prime and X=x modulo f,
so Z is polynomial and f=XZ-Y^2.

For the independent inverse, use X,Y,Z,sigma as variables, put
f=XZ-Y^2, rho=X*Ptilde+Y*f^n and
h=Z*f^(2n)+2*Ptilde*Y*f^n+X*Ptilde^2.
Apply the polynomial inverse of Section 2, including its chosen H.
The inverse curve congruence first clears (r-x^3)/f^n; the same
prime-cancellation identity clears the old z denominator.
The two maps are inverse after inverting f and hence globally.
This proves the positive kernel statement in (3).

This physical lifting argument is the established two-stage
affine-modification framework with the explicitly verified curve
conditions, as detailed in the
[full-ideal priority reduction](priority-boundary-pass20.md).[^2]
Neither a new general lifting principle nor novelty of the resulting
family classification is asserted.

## 4. A normalized algebraic curve excludes every q not divisible by f

Suppose q_0(H)=q(0,H) is nonzero. Choose a nontrivial fifth root
of unity epsilon. Then epsilon^3 is neither 1 nor -1.
The polynomial
\[
2+(1+\epsilon^3)x^3q_0(x^5)
\tag{13}
\]
is nonconstant and has constant term 2, so it has a nonzero root x_0.
At that root q_0(x_0^5) is also nonzero.
No assertion that this root is simple is needed.

Let s=2n+1. In the smooth three-dimensional affine chart with
coordinates f,x_1,x_2 and x_1*x_2 inverted, set
\[
h_i=x_i^5+f^s/x_i,\qquad r_i=x_i^3,
\]
and impose the two equations
\[
h_1=h_2,\qquad
2+q(f,h_1)(x_1^3+x_2^3)=0.
\tag{14}
\]
The point P=(0,x_0,epsilon*x_0) satisfies them.
Modulo f, the first equation is x_1^5=x_2^5.
Its five branches are distinct on this chart. Near P the branch
is x_2=epsilon*x_1, and the second equation is the nonzero
one-variable polynomial (13). Thus the local fiber over f=0
is zero-dimensional, even when x_0 is a multiple root.

Two equations in a regular local ring of dimension three have
local dimension at least one. Consequently some irreducible curve
component through P is not contained in f=0; otherwise the local
zero fiber would have positive dimension. Equivalently, the local
dimension is exactly one, and every dimension-one component needed
here dominates the f-line. Choose one such component, normalize it,
and choose a point over P. Its local ring V is a discrete valuation
ring with fraction field K and residue field C.

In V, f has positive valuation, while x_1,x_2 and h=h_1=h_2
are units. Also r_2-r_1 is a unit, since its residue is
(epsilon^3-1)*x_0^3. Define two actual points of A^4(V) by
\[
P_i=(x_i,\ 0,\ f/x_i,\ 0),
\quad\text{in the order }(x,y,z,t).
\tag{15}
\]
Their values of f,h,r are exactly f,h_i,r_i.
The parameter
\[
\tau=(r_2-r_1)/(f^n h)
\tag{16}
\]
has strictly negative valuation.

The E-flow preserves f,h and has the exact formulas
\[
r\mapsto r+f^nh\tau,\quad
x\mapsto x+2f^nr\tau+f^{2n}h\tau^2,
\]
\[
t\mapsto t+\tau(1+qr)+qf^nh\tau^2/2.
\tag{17}
\]
The first two formulas carry r_1,x_1 to r_2,x_2, using
x_i h=r_i^2+f^s. The other two base coordinates then agree
by the exact f-localized presentation
y=(r-x^3)/f^n and z=(h-2x^2yf^n-x^5)/f^(2n).
At these endpoints one may also use z=(f+y^2)/x, since x_i are units.
The t-displacement is
\[
\tau\left(1+\frac{q(r_1+r_2)}2\right)=0
\]
by (14). Hence exp(tau E)(P_1)=P_2 as points over K.

If a polynomial slice S existed, its finite flow identity would give
S(P_2)-S(P_1)=tau. The left side lies in V because both endpoints
are V-points. The right side has negative valuation, a contradiction.
This proves the negative direction of (3) in every degree.
It is an actual algebraic orbit obstruction, not a finite search
or a claim based on a missing polynomial expression.

The only curve facts used are the principal ideal height bound,
normalization of an algebraic curve, and the DVR local ring of a
normal curve. Their hypotheses hold for the explicit finite-type
curve above. Formal roots or an unproved simple-root condition
are unnecessary. The precise statements are Stacks Lemmas 10.60.12
and 10.60.13 for the dimensions, 33.27.1 for finite normalization,
and 33.43.8 for the DVR local ring.[^3]

## 5. Sharp affine and quadratic degree boundaries

For the low-degree argument, the monic f-localized chart and
the five distinct exponent classes modulo five prove
\[
\ker D^5=C\oplus Cr\oplus Cx\oplus Cxr\oplus Cx^2.
\tag{18}
\]
Indeed the corresponding degrees are 0,1,2,3,4 and their reductions
are x^0,x^3,x^1,x^4,x^2 over C[h]=C[x^5]. A highest f-pole
would give a relation between distinct residue classes, which is
impossible. In particular the earlier spans for ker D^2 and
ker D^3 are retained.

Suppose A*t+v is a slice. Then A is invariant and
Dv=1-A-Aqr. Write v=v_0+v_1r+v_2x. Coefficient comparison gives
1-A=ah*v_1 and -Aq=2a*v_2. Thus A=1 modulo a, and a divides q.
Conversely t-qx/(2a) is a polynomial slice when a divides q.
This proves the first line of (4).

For a putative quadratic slice A*t^2+B*t+C_0, coefficient comparison
gives
\[
DA=0,\quad DB=-2A(1+qr),\quad DC_0=1-B(1+qr).
\tag{19}
\]
The first equations put B in ker D^3 and C_0 in ker D^5.
Comparing DB shows, for some U,b_0 in C,
\[
A=ahU,\qquad B=b_0-2Ur-hqUx.
\tag{20}
\]
Write C_0=c_0+c_1r+c_2x+c_3xr+c_4x^2.
Using r^2=xh-f^s, its remaining equation becomes
\[
\begin{split}
DC_0={}&1-b_0-2Uqf^s+(2U-b_0q)r\\
 &+3hqUx+hq^2Uxr.
\end{split}
\]
Since D(xr)=3ahx-2af^s and D(x^2)=4axr, comparison gives
\[
ac_3=qU,\quad 2ac_2=2U-b_0q,\quad
ahc_1=1-b_0,\quad 4ac_4=hq^2U.
\tag{21}
\]
The first two imply a divides b_0q^2. The third gives b_0=1
modulo a. Thus a divides q^2. Conversely (6) is polynomial
when a divides q^2 and supplies a slice of degree at most two.
This proves the second line of (4), including affine slices.

## 6. Explicit cubic slices below the quadratic threshold

If a divides q^3, choose H=q^2*X*rho/2 in (9).
Modulo a, q^3=0, so phi_0(H)=K and this choice is valid.
Direct expansion gives
\[
\begin{split}
\sigma_3={}&\frac{a^2h^2q^2}{2}t^3
+\left(-\frac{3ah^2q^3x}{4}
        -\frac{3ahq^2r}{2}+\frac{ahq}{2}\right)t^2\\
&+\left(\frac{3h^2q^4x^2}{8}
         +\frac{3hq^3rx}{2}+q^2r^2-qr+1\right)t\\
&-\frac{h^2q^5x^3}{16a}
 -\frac{3hq^4rx^2}{8a}
 -\frac{hq^3x^2}{8a}
 -\frac{q^3r^2x}{2a}.
\end{split}
\tag{22}
\]
Every displayed coefficient is polynomial when a divides q^3,
and E(sigma_3)=1. For nonzero q its cubic coefficient is nonzero.
When a does not divide q^2, Section 5 rules out every quadratic
or affine slice, so the minimum degree is exactly three.

This provides a sharp adjacent degree regime, not an asserted
all-degree formula. In the remaining positive region f divides q
but a does not divide q^3, the finite algorithm in Sections 2-3
still terminates and constructs a slice and polynomial kernel.

## 7. Verification and scope

The [standalone controls](radical_nonlinear_checks_pass22.py) check
the cubic derivative identity, independent finite nilpotent inversions,
global denominator clearings in small exact cases, both physical
curve directions, low-degree coefficient equations, and the orbit
endpoint identities. They import no project solver.
The universal ring and curve arguments are written proofs, not
conclusions extrapolated from these controls.

The [independent audit](radical-noninvariant-audit-pass22.md) reconstructs
the finite inverse and all-degree DVR obstruction. No claim that
arbitrary noninvariant coefficients or arbitrary slice LNDs reduce
to this family is made. The full complex cancellation problem remains
unresolved, and family-level priority still requires further comparison.

## Sources

[^1]: N. Dasgupta and S. A. Gaifullin, [*On locally nilpotent derivations of polynomial algebra in three variables*](https://www.mathnet.ru/eng/sm10094), *Sbornik: Mathematics* 216(4) (2025), 456-484, Theorem 5.7; [author text](https://arxiv.org/html/2306.00510v2). The canonical degree modules for n=1 also occur in G. Freudenburg, [*Canonical factorization of the quotient morphism for a Ga-action on an affine variety*](https://arxiv.org/pdf/1602.08786), Section 8.2.

[^2]: S. Kaliman and M. Zaidenberg, [*Affine modifications and affine hypersurfaces with a very transitive automorphism group*](https://arxiv.org/pdf/math/9801076), *Transformation Groups* 4 (1999), 53-95, Proposition 2.1. The linked prior reduction states the actual full-ideal conditions.

[^3]: The Stacks Project, [dimension lemmas](https://stacks.math.columbia.edu/tag/00KD), [normalization of varieties](https://stacks.math.columbia.edu/tag/0BXR), and [normal curve local rings](https://stacks.math.columbia.edu/tag/0B8Y). These standard inputs were checked directly; no new curve-normalization theorem is claimed.
