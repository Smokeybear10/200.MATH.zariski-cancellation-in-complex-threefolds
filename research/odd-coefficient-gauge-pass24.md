# Odd coefficients and an obstruction to gauge reduction

The canonical family admits an exact slice criterion for coefficients
c(f,h)+rB(f,h,x). This includes positive cases that cannot be changed
into coefficients in C[f,h,r] by any polynomial change of the added
variable fixing the original three-ring. Thus that proposed reduction
of positive cases is false, although the exhibited kernels are polynomial.

The assertions below are working proofs over C, not a solution to
unrestricted cancellation or a claim of mathematical priority.

## 1. Canonical data and statement

Let R=C[x,y,z], n>=1, a=f^n, nu=2n+1, and
\[
f=xz-y^2,\qquad r=x^3+ay,\qquad
h=a^2z+2ax^2y+x^5,\qquad D=-\operatorname{Jac}(f,h,\cdot).
\tag{1}
\]
The canonical base has
\[
\ker D=\mathbb C[f,h],\quad Dr=ah,\quad Dx=2ar,\quad
Dy=h-6x^2r,\quad xh=r^2+f^\nu.
\tag{2}
\]
These data are inherited from the established local-slice construction.[^1]
On the embedded ring
\[
S_0=\mathbb C[f,h,x,r]/(xh-r^2-f^\nu)
\tag{3}
\]
write delta_0=D/a=2r*partial_x+h*partial_r.

Take c in C[f,h] and B in C[f,h,x], and define
\[
b=c+rB,\qquad
\ell(f,h,x)=\frac12\int_0^x B(f,h,v)\,dv,\qquad c_0=c(0,0).
\tag{4}
\]
Then b=c+delta_0(ell). The decomposition is unique in S_0,
by its monic r^2 presentation. Let E=D+b*partial_t.

**Theorem.** E has a polynomial slice if and only if all three
conditions hold:
\[
\begin{gathered}
c_0\ne0,\qquad c(f,0)=c_0,\\
\bigl(x^3c(0,h)+h\ell(0,h,x)\bigr)\bmod(x^5-h)
=c_0x^3+H(h)
\end{gathered}
\tag{5}
\]
for a polynomial H in C[h]. Every positive case has explicit
finite global polynomial coordinates and kernel C^[3].

The last remainder is monic division in x, of degree less than five.
Its coefficient c_0 is prescribed by (4), not chosen separately.
There is no bound on the degrees of B,c or of a hypothetical slice.
The proof does not treat every coefficient in S_0 or every coefficient
in the physical ring R.

## 2. A polynomial primitive on the auxiliary surface

The element
\[
\mathcal F=c\,r+h\ell\in S_0
\tag{6}
\]
satisfies D(mathcal F)=ah*b. It need not be polynomial in r over
C[f,h] without invariant denominators. It is nevertheless a genuine
element of S_0 and a polynomial on physical R.

Over the fraction field of C[f,h], the ring is a polynomial line
with D=ah*partial_r, so the t-displacement along an E-orbit is
\[
\Delta t=\frac{\mathcal F(r_2,x_2)-\mathcal F(r_1,x_1)}{ah}.
\tag{7}
\]
Here x_i=(r_i^2+f^nu)/h. The invariant integration constant is
irrelevant to this difference.

On x=y=0, all of f,h,r vanish and D vanishes. Thus c_0=0
gives fixed points and precludes a slice.

## 3. The h-divisor condition is necessary

Assume c_0 nonzero. If c(f,0) is nonconstant, it has a nonzero
root f_0. Choose r_0^2=-f_0^nu, with r_0 nonzero.
In the three-dimensional chart f,h,r near this point impose
\[
r^2=h-f^\nu,\qquad c(f,h)=0.
\tag{8}
\]
The zero-h fiber is locally zero-dimensional because c(f,0)
is a nonzero polynomial with an isolated root. Two equations in
a regular local threefold therefore give a curve component through
the point not contained in h=0. Normalizing provides a DVR V with
h of positive valuation and f,r units. Multiple roots are allowed.

The two actual integral physical points are
\[
x_i=1,\qquad r_1=r,\quad r_2=-r,\qquad
y_i=(r_i-1)/a,\qquad z_i=f+y_i^2,\qquad t_i=0.
\tag{9}
\]
Their invariants are the common f,h. Since their x-values agree,
their ell-values agree. The c term vanishes on (8), so (7) is zero.
The parameter tau=-2r/(ah) has negative valuation and connects
the two endpoints, with no x-displacement.

A polynomial slice would have integral endpoint difference equal
to tau, a contradiction. Therefore c(f,0) must be the constant c_0.
The standard local dimension and normalization facts are the same
as those used in the preceding two-divisor proof.[^2]

## 4. The f-divisor remainder is necessary

On the physical zero-f curve put
\[
P(u)=u^3c(0,u^5)+u^5\ell(0,u^5,u).
\tag{10}
\]
Its unique lowest term is c_0*u^3, since ell has zero x-constant
term and therefore its second summand has degree at least six.
The monic condition in (5) is equivalent to
P(u)=c_0*u^3 plus a polynomial in u^5.

If that condition fails, for any nontrivial fifth root epsilon
the polynomial (P(u)-P(epsilon*u))/u^3 has nonzero constant
and positive degree. Choose a nonzero root u_0. In the chart
f,x_1,x_2 with x_1*x_2 inverted, impose
\[
\begin{gathered}
h_1=h_2,\qquad h_i=x_i^5+f^\nu/x_i,\\
c(f,h_1)(x_2^3-x_1^3)
{}+h_1\bigl(\ell(f,h_1,x_2)-\ell(f,h_1,x_1)\bigr)=0.
\end{gathered}
\tag{11}
\]
These equations contain (0,u_0,epsilon*u_0). The zero-f fiber
is locally zero-dimensional: the first equation has distinct
fifth-root branches and the second restricts to a nonzero
one-variable polynomial on the chosen branch.

The same dimension and normalization argument gives a DVR V
in which f has positive valuation and x_1,x_2,h_1 and
x_2^3-x_1^3 are units. The integral points
(x_i,0,f/x_i,0) have the same invariants. Equation (11)
makes (7) zero, while their orbit parameter
(x_2^3-x_1^3)/(ah) has a pole. This contradicts any polynomial
slice, in every possible degree.

## 5. Passing the tests gives an actual polynomial gauge

Assume (5). The h condition makes
\[
C(f,h)=(c-c_0)/h
\tag{12}
\]
a polynomial. Since Dy=h+delta_0(-x^3), subtracting
D(C*y) from b gives
\[
b-D(Cy)=c_0+\delta_0(\ell_1),\qquad
\ell_1=\ell+Cx^3\in\mathbb C[f,h,x].
\tag{13}
\]
The first remainder test now says that the reduction of
h*ell_1(0,h,x) modulo x^5-h lies in C[h]. Comparing coefficients
in the free monic remainder basis 1,x,...,x^4 over C[h], and
cancelling the nonzero coefficient h, shows that the remainder
of ell_1 itself lies in C[h]. Thus there are polynomials
L(h), J(h,x), and K(f,h,x) with
\[
\ell_1=L(h)+(h-x^5)J(h,x)+fK(f,h,x).
\tag{14}
\]

The physical identity
\[
(h-x^5)/a=2x^2y+az
\tag{15}
\]
shows that
g_1=((h-x^5)/a)J is an actual polynomial in R.
Also Dg_1=delta_0((h-x^5)J). Hence the genuine base-fixing
polynomial change
\[
t'=\frac{t-Cy-g_1}{c_0}
\tag{16}
\]
puts E into
\[
a\delta_0+
\left(1+\delta_0(fK/c_0)\right)\partial_{t'}.
\tag{17}
\]
No rational gauge has been silently declared polynomial.

The finite variable-time lemma from the preceding proof applies
to every f-divisible ell in S_0, not only the coefficients for
which its first classification was stated. For completeness, with
ell_2=fK/c_0 and L_2=ell_2-a*t', its invariants are
rho=r+hL_2 and X=x+2rL_2+hL_2^2. Its localized slice is
t'-ell_2/a. The invariant correction is computed by the finite
inverse modulo a of a map congruent to the identity modulo f.
The corrected full map is polynomial and has a polynomial inverse
by the minimal-denominator argument.

On the physical curve, v=ell_2(f,u^5,u,u^3) gives
X=u(1+u^2v)^2 and rho=u^3(1+u^2v) modulo a.
The inverse curve parameter supplies the new P, and both old and
new physical denominators clear by primality of f. The
[complete two-sided lemma](polynomial-local-slice-coefficients-pass23.md),
Sections 6-7, proves these steps for arbitrary f-divisible ell
before restricting the coefficient class. Its full-ideal lifting
framework is inherited.[^3]
Undoing (16) finishes the positive proof of (5).

## 6. A positive case cannot be gauged into the earlier coefficient ring

For every n>=1 consider
\[
b_*=1+2fxr,\qquad \ell_*=fx^2/2.
\tag{18}
\]
The criterion (5) passes, so E_*=D+b_*partial_t has polynomial
kernel and global translation coordinates.

**Obstruction.** If n>=2, then
\[
b_*\notin\mathbb C[f,h,r]+D(R).
\tag{19}
\]
This is an all-polynomial statement, not a finite-degree search.

Let A=R/(f^n). Multiplication by x is injective on A, since
f=xz-y^2 is prime in R and does not divide x. Modulo f^n,
\[
r=x^3,\quad h=x^5,\quad
\overline D=-5x^4\delta,\qquad
\delta=x\partial_y+2y\partial_z,\qquad \delta f=0.
\tag{20}
\]
The image of C[f,h,r] is C[f,x^3,x^5], with f^n=0.

Suppose b_*=A_0(f,h,r)+Dg for a polynomial g in R. Reduce
the coefficients of its image in powers of f below n. In the
semigroup of x-exponents generated by 3 and 5, the only
nonnegative exponents less than five are zero and three.
Write that image as
q_0(f)+x^3q_3(f)+x^5Q(f,x).

Reduction modulo x identifies A/(x) with C[y,z]/(y^(2n)).
The monomials 1,f,...,f^(n-1) there are independent.
The proposed equality thus forces q_0=1. After subtracting one
and cancelling x^3, reduction modulo x similarly forces q_3=0.
Cancelling the remaining x^4 gives in A
\[
2f=xQ(f,x)-5\delta g.
\tag{21}
\]

Use ordinary total degree in x,y,z. The polynomial f has degree
two and delta preserves degree. Since n>=2, the homogeneous ideal
(f^n) has no degree-two part. The degree-two part of xQ(f,x)
is a scalar multiple of x^2. But delta on all degree-two
polynomials has image exactly
\[
\operatorname{span}_{\mathbb C}
\{x^2,\ xy,\ xz+2y^2,\ yz\}.
\tag{22}
\]
This span does not contain f=xz-y^2: the coefficients of xz
and y^2 in its elements have ratio 1:2, not 1:-1.
Equivalently, the functional twice the xz coefficient minus the
y^2 coefficient kills the span and takes value six on 2f.
Equation (21) is impossible. This proves (19).

Every automorphism of R[t] fixing R sends t to lambda*t+g
for lambda in C* and g in R. Such a change would place the new
coefficient in C[f,h,r] only if (19) failed, after dividing by
lambda. Thus no such base-fixing coordinate change reduces this
positive case to the preceding coefficient class.

The n=1 boundary is different and explicit:
b_*=1+D(x^2/2), so t-x^2/2 is an affine slice.
For n=2 one convenient polynomial slice is
\[
\sigma=t+\frac{X^2-x^2}{2f},\qquad
X=x+2rL+hL^2,\quad L=fx^2/2-f^2t.
\tag{23}
\]
The quotient is polynomial because X=x modulo f, and directly
E_*(sigma)=1. This formula does not assert a minimum t-degree.

The obstruction forbids only changes fixing the original base R.
It does not exclude a nonlinear change of the entire four-variable
frame. Indeed the constructive proof supplies such coordinates.
It therefore identifies a genuine failure of a general-reduction
shortcut, not a counterexample to cancellation.

## Sources

[^1]: N. Dasgupta and S. A. Gaifullin, [*On locally nilpotent derivations of polynomial algebra in three variables*](https://arxiv.org/html/2306.00510v2), Theorem 5.7; G. Freudenburg, [*Canonical Factorization of the Quotient Morphism for an Affine Ga-Variety*](https://arxiv.org/html/1602.08786v3), Section 8.2 for the n=1 base. The [uniform image reconstruction](nonreduced-rank-three-images-pass17.md) records the sign and parameter conventions.

[^2]: The Stacks Project, [local dimension bounds](https://stacks.math.columbia.edu/tag/00KW) and [finite normalization](https://stacks.math.columbia.edu/tag/0BXR). The explicit two-equation charts satisfy the hypotheses checked in the [preceding independent audit](polynomial-coefficients-audit-pass23.md).

[^3]: S. Kaliman and M. Zaidenberg, [*Affine modifications and affine hypersurfaces with a very transitive automorphism group*](https://arxiv.org/pdf/math/9801076), Proposition 2.1 and Corollary 2.2; see the [full-ideal application record](priority-boundary-pass20.md). No new universal lifting principle or novelty is asserted.
