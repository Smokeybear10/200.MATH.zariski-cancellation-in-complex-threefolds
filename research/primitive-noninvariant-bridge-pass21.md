# A primitive rank-three obstruction to fixed-base invariantization

An arbitrary sliced extension cannot be reduced to the invariant-coefficient
case merely by changing its added variable while preserving its original
three-variable coordinate ring. This failure occurs with a primitive
rank-three base, not only with a nonprimitive triangular base. The examples
below have polynomial kernels and explicit polynomial inverses, so they
are counterexamples to that proposed reduction, not to cancellation.

## 1. A universal polynomial transformation

Let K be a domain containing the rational numbers, and take
a,q,c in K[h], with a nonzero and ac=q^2. On K[h,x,r,t], let the
derivation fix K and h and satisfy
\[
\mathcal E=2ar\partial_x+ah\partial_r+(1+qr)\partial_t,
\qquad \mathcal E h=0.
\tag{1}
\]
The coefficient q may in particular be a polynomial in the invariant h,
with the other invariant parameters fixed. Put
\[
L=qx/2-at,\quad
\rho=r+hL,\quad X=x+L(r+\rho),
\tag{2}
\]
\[
\sigma=t-qrt-\frac{q^2xh}{2}t+\frac{ahq}{2}t^2
       +\frac{c}{2}xr+\frac{cq}{8}x^2h.
\tag{3}
\]
These are polynomial formulas. Direct differentiation, using ac=q^2,
gives
\[
\mathcal E\rho=\mathcal EX=0,\quad \mathcal E\sigma=1,
\quad Xh-\rho^2=xh-r^2.
\tag{4}
\]

There is an inverse on independent variables X,h,rho,sigma:
\[
L'=a\sigma-qX/2,\quad
r=\rho+hL',\quad x=X+L'(r+\rho),
\tag{5}
\]
\[
t=\sigma+\frac q2\sigma(r+\rho)-\frac c4X(r+\rho).
\tag{6}
\]
Both compositions are identities, before imposing any surface equation.
One can verify them by substituting (2)-(3) into (5)-(6), or by
checking them after inverting a and then using the domain property.
The identity (4) shows that the automorphism descends to every level
xh-r^2 equal to an invariant scalar polynomial.

The formula does not require a to be a unit. The exact divisibility
a|q^2 is what makes (3) and (6) polynomial. Nor does this universal
calculation identify a local slice r with an ambient coordinate of an
arbitrary ring containing it. The physical extension below requires
a separate overring argument.

## 2. The primitive rank-three base

For n>=2, in R=C[x,y,z] use the positive local-slice convention
\[
f=xz-y^2,\quad r=x^3+yf^n,\quad
h=zf^{2n}+2x^2yf^n+x^5,\quad
D=-\operatorname{Jac}(f,h,\cdot).
\tag{7}
\]
Then
\[
xh=r^2+f^{2n+1},\quad
Df=Dh=0,\quad Dr=f^nh,\quad Dx=2f^nr.
\tag{8}
\]
This is an established Freudenburg local-slice family; its primitive
rank-three property is included in the Dasgupta-Gaifullin formulation.[^1]
The [base proof](polynomial-curve-lift-pass18.md) verifies the exact
kernel C=C[f,h], plinth (f^n h), and primitivity. The older
[image calculation](nonreduced-rank-three-images-pass17.md) uses
the opposite sign for r and D. Changing both signs preserves the
kernel and all higher image ideals.

Choose
\[
q=f^\ell J(f,h),\qquad
\lceil n/2\rceil\le\ell<n,\qquad J(0,h)\ne0,
\quad a=f^n,\quad c=q^2/a.
\tag{9}
\]
In particular c is polynomial and q is nonzero. Define
\[
E=D+(1+qr)\partial_t\quad\hbox{on }R[t].
\tag{10}
\]
This is locally nilpotent: it is D on R, and E^3t=0.
The universal formula (3) supplies a polynomial slice of t-degree
exactly two.

The coefficient 1+qr is not invariant, since
E^2t= D(1+qr)=f^nhq is nonzero.
The fact that E nevertheless has a slice is central to the example.

## 3. The complete second image ideal

For the obstruction it is enough to reconstruct the second image,
without importing the all-degree image formula:
\[
\ker D^3=C\oplus Cr\oplus Cx,\qquad
D^2(R)\cap C=f^{2n}hC.
\tag{11}
\]
After inverting f, the exact monic chart is
\[
R_f=C[f^{-1}][x,r]/(xh-r^2-f^{2n+1}).
\]
Its free module basis consists of x^j r^epsilon, with epsilon=0,1.
Their distinct D-degrees are 2j+epsilon. Therefore degree at most
two is exactly the span of 1,r,x over C[f^{-1}].

To descend the coefficients, suppose a highest f-pole were present.
Multiplying by its power and reducing modulo f would give a nontrivial
relation
\[
A(x^5)+B(x^5)x^3+C_1(x^5)x=0.
\tag{12}
\]
The three possible monomial exponents are respectively 0,3,1 modulo
5, so cancellation between those summands is impossible. Hence no
coefficient has a pole. This proves the module equality in (11).
Finally D^2x=2f^{2n}h gives its exact image ideal.

This is a general proof for all n, rather than an extrapolation from
a degree-bounded primitive search.

## 4. No invariant coefficient in the same base

If 1+qr belonged to C+D(R), applying D would give
\[
f^nhq\in D^2(R)\cap C=f^{2n}hC.
\]
Thus f^n would divide q in C, contrary to (9). Therefore
\[
1+qr\notin C+D(R).
\tag{13}
\]
More generally, for arbitrary q in C the exact criterion is
\[
1+qr\in C+D(R)\quad\Longleftrightarrow\quad f^n\mid q.
\tag{14}
\]
The reverse implication follows from
D(qx/(2f^n))=qr when q/f^n is polynomial.

Every R-algebra automorphism of R[t] sends t to ut+H with
u in R*=C* and H in R. Such a change makes the new added coefficient
invariant exactly when u(1+qr)+D(H) belongs to C. Equation (13)
excludes it. Allowing an automorphism of R as well does not remove
the obstruction: it transports C, D(R), and the class of the
coefficient isomorphically.

Consequently no ambient polynomial automorphism preserving R as a
subalgebra can put (10) into invariant-coefficient form. This does
not exclude a new three-variable coordinate subring that mixes the
original t with base variables.

## 5. No affine slice in t

Suppose At+v were a slice, with A,v in R. Its t coefficient gives
DA=0, hence A in C, and
\[
Dv+A(1+qr)=1.
\tag{15}
\]
Applying D and using (11) forces A*f^nhq into f^(2n)hC.
Since q has exact f-valuation ell, f^(n-ell) divides A.

At the point x=y=z=0, all coefficients of D vanish and 1+qr=1.
Evaluation of (15) therefore gives A(0)=1. But f^(n-ell)|A,
with n-ell>0, gives A(0)=0. This is a contradiction.
Together with (3), it proves
\[
\min\{\deg_t s:\ s\in R[t],\ Es=1\}=2.
\tag{16}
\]
The base D is primitive and rank three throughout. In particular,
the earlier affine-replacement theorem for invariant added coefficients
cannot be applied to an arbitrary coefficient by forgetting that
hypothesis.

## 6. The kernel is nevertheless polynomial

The universal automorphism (2)-(6) preserves xh-r^2. It therefore
gives a polynomial automorphism of the abstract surface cylinder
\[
\mathscr A_0[t],\qquad
\mathscr A_0=C[f,x,h,r]/(xh-r^2-f^{2n+1}).
\tag{17}
\]
All three surface coordinates are E-invariant and sigma is a slice.

Modulo f^n, q^2=0, and the forward map is
\[
h\longmapsto h,\quad
r\longmapsto r+qxh/2,\quad
x\longmapsto x+qxr.
\tag{18}
\]
Its inverse has the corresponding minus signs. Both maps are independent
of the cylinder coordinate modulo f^n, preserve the vertex ideal
(x,h,r), and are the identity modulo f. These are the full hypotheses
of the [weighted-overring lemma](cylinder-comparison-pass20.md),
whose lifting principle is explicitly reduced to established
Kaliman-Zaidenberg modification theory in the
[priority note](priority-boundary-pass20.md).[^2]

The old physical curve is (x,h,r)=(u,u^5,u^3), corresponding to P=x^2.
Set q_curve(f,X)=q(f,X^5). The corrected curve polynomial is explicitly
\[
\widetilde P(X,f)=X^2-\frac52q_{\rm curve}(f,X)X^5
                    \pmod{f^n}.
\tag{19}
\]
Indeed on the old curve,
\[
X=u+q(f,u^5)u^4,\qquad
\rho=u^3+\tfrac12q(f,u^5)u^6.
\]
Since q^2 and q*q_h vanish modulo f^n, finite first-order substitution
gives rho=X*Ptilde(X,f) and h=X*Ptilde(X,f)^2. The inverse curve
identity follows from u=X-q(f,X^5)X^4. This calculation is made in
the universal parameter polynomial ring before any specialization.

Choose the remainder of (19) of f-degree less than n, and define
\[
Y=\frac{\rho-X\widetilde P(X,f)}{f^n},\qquad
Z=\frac{h-2\widetilde P(X,f)Yf^n-X\widetilde P(X,f)^2}{f^{2n}}.
\tag{20}
\]
The first numerator is f^n-divisible by the curve identity.
For the second, multiply its numerator by X and use
Xh=rho^2+f^(2n+1); the result is f^(2n)(Y^2+f).
Here f is prime in the physical polynomial ring and X=x modulo f,
so f does not divide X. Repeated prime cancellation makes Z polynomial,
and f=XZ-Y^2.

For the inverse, start with independent X,Y,Z,sigma, put
f=XZ-Y^2, rho=X*Ptilde+Y*f^n and
h=Z*f^(2n)+2*Ptilde*Y*f^n+X*Ptilde^2.
Apply (5)-(6). The inverse curve identity gives r-x^3 in (f^n);
the same quadratic identity clears the original z denominator.
The two polynomial maps are inverse after inverting f and hence
globally. It follows that
\[
R[t]=C[X,Y,Z,\sigma],\qquad
E=\partial_\sigma,\qquad
\ker E=C[X,Y,Z].
\tag{21}
\]

Thus (13) and (16) are genuine obstructions to a fixed-base reduction
inside a case with explicitly solved cancellation behavior.

## 7. A smaller primitive control

For comparison, take D=x^2*partial_y+y^m*partial_z on C[x,y,z],
with m>=2, and again use E=D+(1+xy)*partial_t.
The polynomial
\[
t+\frac{y^3}{2}+\frac{xy^4}{8}-xyt
-\frac{x^2y^2t}{2}+\frac{x^3t^2}{2}
\]
is a slice. The base is primitive, with
ker D=C[x,(m+1)x^2z-y^(m+1)]. Modulo (x^2,y^m), D(R) is zero
and the kernel maps into C[x]/(x^2), whereas xy survives. Thus
1+xy does not belong to ker D+D(R).

This easier control shows the same failure without relying on
rank-three image calculations. The main result above establishes
that restricting attention to primitive rank-three bases does not
repair the shortcut.

## 8. Scope, verification, and the next logical requirement

The [standalone checker](primitive_bridge_checks_pass21.py) uses exact
polynomial identities, independent inverse substitutions, residue
controls and finite curve jets. It imports no project solver.
Finite checks supplement Sections 1-6; they do not prove a universal
classification of arbitrary slices.

Independent reconstructions checked the universal polynomial
transformation, the complete second-image argument, both fixed-base
obstructions, the sign convention, and the two curve identities.
These are model audits, not human expert review. The constructions
use existing LND and modification machinery, and mathematical priority
for this family-level consequence is unestablished.

A universal cancellation proof along the invariant-extension route
must justify a change of the actual base subring, not merely a vertical
shear, even after a commuting coordinate partial has been found.
The [separate frame analysis](arbitrary-slice-frame-pass21.md) isolates
that existence question. No claim that every slice derivation admits
such a frame is made here.

## Sources

[^1]: N. Dasgupta and S. A. Gaifullin, [*On locally nilpotent derivations of polynomial algebra in three variables*](https://www.mathnet.ru/eng/sm10094), *Sbornik: Mathematics* 216(4) (2025), 456-484, Theorems 2.17 and 5.7. The base is the monomial specialization with quadratic F and P=x^2; the present positive-r convention negates the Jacobian convention in the older image note.

[^2]: S. Kaliman and M. Zaidenberg, [*Affine modifications and affine hypersurfaces with a very transitive automorphism group*](https://arxiv.org/pdf/math/9801076), *Transformation Groups* 4 (1999), 53-95, Proposition 2.1. The full center-ideal conditions and two-stage application are recorded in the linked priority note; preservation of reduced support alone is not sufficient.
