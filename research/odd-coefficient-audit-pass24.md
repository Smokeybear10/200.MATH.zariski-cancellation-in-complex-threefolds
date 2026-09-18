# Independent audit of the odd-coefficient criterion

This audits the complete [odd-coefficient proof](odd-coefficient-gauge-pass24.md),
including its two necessity curves, the polynomial gauge, the inherited global
inverse, and the all-degree obstruction in Section 6. The verdict is clean
after the equation (11) transcription correction recorded below. This is an
independent reconstruction of a scoped working proof, not expert review or a
priority claim.

## 1. Scope and transcription

The physical ring is R=C[x,y,z], with n>=1 and

\[
f=xz-y^2,\quad a=f^n,\quad \nu=2n+1,\quad
r=x^3+ay,\quad h=a^2z+2ax^2y+x^5.
\]

The derivation is D=-Jac(f,h,.). The coefficient class is exactly
b=c(f,h)+rB(f,h,x), with
ell=(1/2) integral from 0 to x of B(f,h,v) dv and c_0=c(0,0).
The theorem asserts a slice precisely when c_0 is nonzero,
c(f,0)=c_0, and the indicated monic remainder is c_0*x^3+H(h).
It also supplies polynomial kernels for these positive cases.

Equation (11) originally omitted the plus sign in the primitive-difference
equation. I reported this independently. The current equation correctly reads

\[
c(f,h_1)(x_2^3-x_1^3)
+h_1\bigl(\ell(f,h_1,x_2)-\ell(f,h_1,x_1)\bigr)=0.
\]

I reread the corrected display. I also reread the strengthened coefficient
comparison in Section 5; it now explicitly uses the free monic remainder basis.
No further transcription or mathematical correction is requested.

The audit takes the already reconstructed canonical kernel and local-slice
data as input. It does not reprove every assertion in their primary sources.
The independently checked physical derivatives are

\[
Dx=2ar,\qquad Dy=h-6x^2r,
\]
\[
Dz=-10x^4y-8axy^2-2ax^2z.
\]

These imply Dr=ah, Df=Dh=0 and xh=r^2+f^nu. The auxiliary derivation
delta_0=2r*partial_x+h*partial_r is used only on the embedded surface
S_0=C[f,h,x,r]/(xh-r^2-f^nu), not as a polynomial derivation D/a of
the whole physical ring.

## 2. Independent reconstruction of both necessity curves

The physical polynomial primitive is mathcal F=c*r+h*ell. Its derivative is
D(mathcal F)=ah*b. After inverting f and h, the physical ring is the
polynomial r-chart over the localized invariant ring, and D=ah*partial_r.
Thus the two endpoint formulas in the main proof give actual orbits, not
only equal values of some invariants.

If c_0=0, the line x=y=0 consists of fixed points for E=D+b*partial_t.
In particular, a slice is impossible. Suppose henceforth c_0 is nonzero.

### The h-divisor

If c(f,0) is nonconstant, it has a nonzero root f_0 over C. Choose a nonzero
r_0 with r_0^2=-f_0^nu. At (f_0,0,r_0), impose
r^2=h-f^nu and c(f,h)=0 in the regular three-dimensional chart.
The zero-h fiber is locally zero-dimensional. The local dimension bound
for two equations produces a positive-dimensional component through this
point, and no such component can be contained in h=0. Its normalization
at a point over the chosen point gives a DVR in which h has positive
valuation and f,r are units. This reasoning does not require a simple root
of c(f,0).

Both endpoints x=1, r_i=+/-r,
y_i=(r_i-1)/a, z_i=f+y_i^2, t_i=0 are integral in that DVR.
Their physical h-values agree by xh=r_i^2+f^nu. Their ell-values agree
because their x-values agree. Since c vanishes along the curve,
the primitive difference is zero. Their orbit parameter -2r/(ah)
has a pole, however. A polynomial slice evaluated at these two integral
points would have integral difference equal to this parameter. This is
the required contradiction, in every possible slice degree.

### The f-divisor

Let P(u)=u^3*c(0,u^5)+u^5*ell(0,u^5,u). Because ell has zero x-constant
term, P has unique lowest term c_0*u^3. The quotient by x^5-h is identified
with C[u] by x=u,h=u^5. Accordingly, the required remainder is equivalent
to P-c_0*u^3 belonging to C[u^5].

If the remainder condition fails, fix a nontrivial fifth root epsilon.
Every such root is primitive. The polynomial
(P(u)-P(epsilon*u))/u^3 has nonzero constant term and at least one
positive-degree term. It therefore has a nonzero root u_0. At
(f,x_1,x_2)=(0,u_0,epsilon*u_0), use the corrected two equations (11).
The first equation has distinct local fifth-root branches on f=0, and the
second restricts to a nonzero one-variable polynomial on the chosen branch.
The zero-f fiber is locally zero-dimensional. The same dimension and
normalization argument gives a DVR with f of positive valuation and
x_1,x_2,h_1,x_2^3-x_1^3 units. No simple-root hypothesis is needed.

The integral physical endpoints (x_i,0,f/x_i,0) have the specified common
f,h. The corrected second equation makes their primitive difference zero.
Their orbit parameter (x_2^3-x_1^3)/(ah) has a pole. The same slice
integrality contradiction proves necessity.

Both arguments use the algebraic closure and characteristic zero of C.
They neither infer properness from a finite test nor assume that a
hypothetical slice is affine in t.

## 3. Polynomial gauge and the scope of the global inverse

The h-condition gives the actual polynomial C=(c-c_0)/h. As
Dy=h+delta_0(-x^3), subtracting D(Cy) changes the coefficient to
c_0+delta_0(ell_1), where ell_1=ell+Cx^3.

The f-remainder condition says that the remainder of h*ell_1(0,h,x)
lies in C[h]. In the free C[h]-basis 1,x,...,x^4, its nonconstant
coefficients are h times those of the remainder of ell_1. Their vanishing
forces those coefficients to be zero. Consequently

\[
\ell_1=L(h)+(h-x^5)J(h,x)+fK(f,h,x).
\]

The physical identity (h-x^5)/a=2x^2y+az makes
g_1=((h-x^5)/a)J a polynomial in R. Since D fixes a,
Dg_1=delta_0((h-x^5)J). Hence
t'=(t-Cy-g_1)/c_0 is an actual base-fixing polynomial automorphism.
Its new coefficient is 1+delta_0(ell_2), with ell_2=fK/c_0 in fS_0.

I reread Sections 6-7 of the
[preceding full inverse proof](polynomial-local-slice-coefficients-pass23.md).
They are stated and proved for every ell in fS_0, represented by an
f-divisible polynomial in the full ring C[f,h][x,r]. The prior classifier's
restriction to C[f,h,r] is not a hypothesis of that lifting lemma.
Therefore applying it here is valid.

More explicitly, L=ell_2-at', rho=r+hL and X=x+2rL+hL^2 preserve
Xh-rho^2=xh-r^2. After inverting a, they and sigma_0=-L/a have the displayed
two-sided inverse. Modulo a, the first pair is congruent to the identity
modulo f. Its difference from the identity raises f-adic order as an
additive operator, so the inverse is a finite geometric sum. Correcting
sigma_0 by the corresponding invariant polynomial divided by a makes
the corrected slice polynomial. Modulo a its t-coefficient is the unit
(1+delta_0 ell_2)^(-1). Thus the full map is an automorphism both after
a-localization and modulo a. Injectivity modulo a clears every remaining
inverse denominator by the minimal-denominator argument.

For the physical lift, the surface variables and their inverse are
t-independent modulo a, preserve the vertex ideal, and are the identity
modulo f. On the old physical curve, with
v=ell_2(f,u^5,u,u^3), one has
X=u(1+u^2v)^2 and rho=u^3(1+u^2v). The finite inverse curve parameter
defines the new P. The numerator identities clear the two physical
denominators, using that f is prime and X=x modulo f. In the independent
inverse coordinate ring the same argument uses f=XZ-Y^2 and x=X modulo f.
The two polynomial maps agree with mutual inverses after f-localization,
and hence are mutual inverses globally.

This establishes the announced polynomial kernel in the stated coefficient
class. It introduces no universal lifting theorem for arbitrary sliced
four-variable derivations.

## 4. Audit of the all-degree quotient obstruction

For b_*=1+2fxr, ell_*=fx^2/2, the criterion passes for every n>=1.
Assume n>=2 and suppose b_*=A_0(f,h,r)+Dg.
Modulo f^n, x is a non-zero-divisor and
r=x^3, h=x^5, D=-5x^4*delta with delta=x*partial_y+2y*partial_z.
The semigroup generated by 3 and 5 has only 0 and 3 below 5. Thus the
image of A_0 has the form q_0(f)+x^3q_3(f)+x^5Q(f,x), with the
f-degrees of q_0,q_3 reduced below n.

Modulo x the ring is C[y,z]/(y^(2n)), and the residues of
1,f,...,f^(n-1) are linearly independent. The first reduction gives
q_0=1. Cancel x^3 from the remaining equality and reduce modulo x
again to obtain q_3=0. Cancelling the remaining factor x yields

\[
2f=xQ(f,x)-5\delta g\pmod{f^n}.
\]

The homogeneous ideal (f^n) has no degree-two part. In degree two,
xQ contributes only a multiple of x^2. The image of delta on all
quadratic polynomials is exactly
span{x^2,xy,xz+2y^2,yz}. The linear functional twice the xz coefficient
minus the y^2 coefficient annihilates this span and takes value six
on 2f. This is an all-degree contradiction: no degree bound on g
or A_0 was used.

## 5. A second reconstruction using ordinary degree six

This argument takes place directly in R and does not reduce modulo f^n.
For every n>=2 the degree-five coefficient part of D is

\[
D_5=-5x^4(x\partial_y+2y\partial_z)=-5x^4\delta.
\]

Every other coefficient term of D has total degree at least seven.
Indeed a has degree 2n, so Dx starts in degree 2n+3>=7,
Dy=-5x^5-4ax^2y+a^2z, and
Dz=-10x^4y-8axy^2-2ax^2z. Therefore the degree-six part of Dg
is exactly -5x^4*delta(g_2), where g_2 is the degree-two homogeneous
part of g. A coefficient of degree at least seven acting on a linear
term has degree at least seven, and acting on a constant gives zero.
Thus no omitted part of g or D can contribute in degree six.

The lowest degrees of f,r,h are 2,3,5. Every invariant monomial
of lowest degree at most six is one of

\[
1,\ f,\ r,\ f^2,\ h,\ fr,\ f^3,\ r^2.
\]

For n>=2 the next term of r has degree 2n+1>=5, and all corrections
to h have degree at least seven. When n=2, the correction of r alone
has degree five, not six; the correction of fr has degree seven, and
the first correction of r^2 has degree eight. For larger n these
corrections occur later. No monomial of lowest degree greater than six
can contribute in degree six, because all substitutions only increase
degree. This checks explicitly that no lower-degree monomial correction,
including the special n=2 correction of r, has been lost.

It follows that the degree-six part of any A_0(f,h,r) is
alpha*x^6+beta*f^3. Meanwhile the degree-six part of b_*-1 is 2fx^4;
the remaining term 2f^(n+1)xy has degree 2n+4>=8. The hypothesized
equality therefore gives

\[
2fx^4=\alpha x^6+\beta f^3-5x^4\delta(g_2).
\]

Set x=0. Since f=-y^2 there, beta=0. Cancel x^4 in the polynomial
domain to obtain 2f=alpha*x^2-5*delta(g_2). The same quadratic
functional gives the contradiction. This proves the nongauge assertion
independently of the main quotient argument.

Every R-algebra automorphism of R[t] is t->lambda*t+g with lambda in C*
and g in R. The assertion therefore excludes every such base-fixing
coordinate change into C[f,h,r]. It does not exclude a change of the
entire four-variable frame. The positive coordinate proof supplies one.

The boundary n=1 is correctly separated: D(x^2/2)=2fxr, so
t-x^2/2 is an affine slice. For n=2 the displayed sigma is polynomial
because X=x modulo f, and its derivative is exactly one. No minimum
degree of this particular slice is asserted.

## 6. Bounded exact controls and remaining limitations

An independent inline SymPy calculation ran 15 bounded algebra-control
groups in 1.894 seconds. It checked the physical Jacobian derivatives
at n=1,2,3; their degree-five leading part and absence of degree-six
coefficient terms at n=2,3; a nonconstant-c primitive and actual physical
gauge at n=1,2; the n=1 affine slice; exact polynomial division and the
derivative of the displayed n=2 slice; the complete quadratic image and
separating functional; and every invariant monomial of lowest degree
at most six at n=2,3,4.

Those controls used SymPy and the standard library, without solver imports.
They added no regression methods. The unbounded conclusions are the written
dimension, gauge, inverse and degree arguments above, not extrapolations
from the checked parameter values.

No mathematical defect remains in the audited scope. Unrestricted
coefficients in R, arbitrary nonlinear frames on a sliced C^[4], priority,
and external expert review remain outside this result.
