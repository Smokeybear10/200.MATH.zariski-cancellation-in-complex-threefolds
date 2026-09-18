# A degree-ten plane frontier and a genuine plane-return alternative

Working result: in the actual nonzero-coupling principal chart264,
the irreducible equation of the projected plane curve has degree at
most ten. If the cubic surface level is reducible, the two plane
functions already generate the whole generic polynomial line, and
the plane degree is at most four.

These conclusions use296's precise quadratic structure in the first
formal variable. They refine299's degree-twelve plane bound but do
not improve its bound on the three individual line polynomials.
They do not supply an original-ring coordinate change or recognition.

## 1. Exact input and plane equation

Retain the entire actual hypotheses of the fully read
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
[290](principal-paraboloid-nonzero-coupling-projection-pass290-working.md),
and [296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md).
Write
\[
O=L[v]=L[y,\sigma,\theta],\quad C=L[\sigma,\theta],\quad
e_0=[L(v):\operatorname{Frac}C]\in\{1,2\}.
\tag{1}
\]
There is an irreducible polynomial G in R=L[P,V] generating the
kernel of evaluation P=sigma,V=theta. Indeed this is a height-one
prime in the two-variable polynomial UFD. At least one projected
function is nonconstant, by290.

Keep the actual levels, including their constants:
\[
\begin{aligned}
H_0&=H-h_0=U^2+A_1(P,V)U+A_0(P,V),\\
Q_0&=Q-q_0=e(P)U^2+L_1(P,V)U+L_0(P,V),\\
\deg A_1&\le2,\quad\deg A_0\le3,\quad
\deg e\le2,\quad\deg L_1\le3,\quad\deg L_0\le4.
\end{aligned}
\tag{2}
\]
Both levels vanish at (y,sigma,theta). By296 their evaluated
gradient minors generate the unit ideal of O. In particular the
H_0-gradient is a unit ideal, and the levels cannot share a factor
that vanishes identically on the actual curve.

## 2. A reducible surface gives the whole plane ring

Suppose H_0 is reducible in R[U]. Since it is monic quadratic,
its factors can be chosen monic in U. It cannot have a nonconstant
factor in R alone. Thus
\[
H_0=(U+A)(U+B),\qquad A,B\in R,
\quad A+B=A_1,\quad AB=A_0.
\tag{3}
\]
We have deg A,deg B<=2. If one had degree greater than two,
the relation A+B=A_1 would force the other to have the same degree
and opposite leading form. Their product would then have degree
greater than four, contrary to deg A_0<=3. If either factor is
zero as an element of R, the other is A_1 and the claim is immediate.

Exactly one factor in (3) vanishes identically on the actual line.
At least one does because O is a domain. If both did, all evaluated
partials of H_0 would vanish. Relabel so y=-A(sigma,theta).
Then
\[
\boxed{O=C[y]=C=L[\sigma,\theta].}
\tag{4}
\]
This is a genuine polynomial-ring equality, not only equality
of fraction fields. In particular e_0=1 and the projected affine
curve is the affine line over L. This statement is still about
the exact coefficient-field ring, not an original ambient coordinate.

Substitute the selected factor into the fourth level:
\[
q(P,V)=Q_0(-A(P,V),P,V).
\tag{5}
\]
It has total degree at most six by (2) and deg A<=2. It is not
the zero polynomial: otherwise monic division in R[U] would make
U+A divide Q_0 as well as H_0, a common factor vanishing on the
actual curve. It is not a nonzero constant, because it evaluates
to zero. Hence G divides this nonzero q, and
\[
\boxed{\deg G\le6\quad\text{if H_0 is reducible}.}
\tag{6}
\]

One can also recover the smoothness gate directly from the minors.
The other factor U+B evaluates to a unit by the H_0-gradient
condition. On the selected component, the gradient minors reduce
to that unit times q_P,q_V and A_P q_V-A_V q_P. Thus the evaluated
gradient of q is a unit ideal. No assertion that q itself is
irreducible or the full plane equation is required.

There is a stronger bound using the selected factor's unit. Write
\(B(\sigma,\theta)-A(\sigma,\theta)=\eta\in L^*\),
as follows from the H_0-gradient condition. If B-A is a nonconstant
polynomial, G divides the nonzero polynomial B-A-eta of degree
at most two. If B-A is a constant polynomial, it is the nonzero
constant eta. Then B=A+eta. Unless A is constant, A and B have
the same degree, so deg(AB)<=3 forces deg A<=1. With this improved
substitution degree, (5) has degree at most four. Consequently
\[
\boxed{\deg G\le4\quad\text{if H_0 is reducible},\qquad
\deg G\le2\quad\text{if B-A is nonconstant}.}
\tag{6a}
\]
These are separate polynomial alternatives over L. A nonconstant
factor difference can evaluate to a scalar on the plane curve;
it must not be declared constant as a formal polynomial.

## 3. An irreducible surface gives an explicit nonzero eliminant

Suppose instead that H_0 is irreducible. It cannot divide Q_0,
by the common-factor obstruction. Its monicity also makes it
irreducible over the rational function field L(P,V).

Put
\[
r=L_1-eA_1,\qquad s=L_0-eA_0,
\qquad Q_0-eH_0=rU+s.
\tag{7}
\]
Use a new plane polynomial, not a coefficient-field parameter:
\[
\begin{aligned}
\mathcal R
&=s^2-A_1rs+A_0r^2\\
&=L_0^2-A_1L_1L_0+A_0L_1^2
  +e(A_1^2-2A_0)L_0-eA_0A_1L_1+e^2A_0^2.
\end{aligned}
\tag{8}
\]
The second expression has total degree at most ten by (2).
Using the unreduced degree bounds deg r<=4,deg s<=5 without
the cancellation in (8) would give a weaker estimate.

This eliminant is nonzero. If r=0 and the eliminant were zero,
then s=0 and H_0 would divide Q_0. If r!=0 and the eliminant
were zero, then -s/r would be a root of the irreducible monic
quadratic H_0 in L(P,V), again impossible.

For an explicit ideal-membership identity, direct multiplication gives
\[
\mathcal R=r^2H_0-(rU+A_1r-s)(Q_0-eH_0).
\tag{9}
\]
Therefore the nonzero polynomial in (8) evaluates to zero at
(sigma,theta); the plane equation G divides it. We obtain
\[
\boxed{\deg G\le10\quad\text{if H_0 is irreducible}.}
\tag{10}
\]
This does not assume that the eliminant is irreducible, reduced,
or equal to the selected plane equation. Extraneous projected
components and multiplicities are allowed.

If e_0=2, there is a further elementary divisibility. Equation
(7) after evaluation and the degree-two minimal polynomial of y
over Frac C force both r and s to vanish on the plane curve.
Thus G divides both, so G^2 divides the eliminant in (8) and
deg G<=5. This is only an intermediate bound; separate full
coefficient constraints may be stronger.

## 4. Consequences and remaining gap

Together the alternatives prove the uniform plane degree bound
\[
\boxed{\deg G\le10.}
\tag{11}
\]
A singular birational plane projection can occur only in the
irreducible-surface alternative. If H_0 is reducible, equation
(4) supplies exactly the polynomial plane return that cannot
be inferred from a generic cubic-surface equation alone.

The result retains arbitrary exact coefficient functions and
does not replace them by rational or polynomial ansatzes in t,s.
It does not make the reducible-surface factor A an original-ring
polynomial coordinate correction. It does not classify all plane
degrees up to ten, exclude the singular birational case, or prove
the remaining original-ring descent. Other initial kernels,
time-degree profiles, and arbitrary-coordinate entry remain
outside this chart. Full cancellation remains unsolved.

The elimination is supplied as the explicit identity (9), not
as a numerical resultant computation. Separate source review
and finite algebra controls are recorded after completion.
No historical novelty, human expert review or formal verification
is asserted.
