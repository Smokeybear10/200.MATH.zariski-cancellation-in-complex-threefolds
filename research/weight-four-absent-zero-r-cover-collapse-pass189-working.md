# The absent-variable zero-R coefficient cover is linear with constant slope

**Status: working exact-field reduction, not original-ring recognition.**

Under the actual hypotheses of the absent-variable zero-R reduction187,
the quadratic coefficient cover cannot be genuinely quadratic. Its remaining
linear slope is a nonzero complex constant. In particular
\[
L=K(n),\qquad \rho=b n+c,\qquad b\in\mathbb C^*,\quad c\in K .
\]
This uses the actual inverse through its exact function-field equality.
Formal determinant solutions alone do not imply the conclusion.

## 1. Inputs and exact coefficient derivatives

Retain all actual hypotheses and conclusions of
[zero-R187](weight-four-absent-variable-zero-r-reduction-pass187-working.md).
In particular the full initial kernel is \((X^2Z-Y^4)\), the actual
time profile is \((1,1,2,2)\), the action has a global slice, and
\[
\begin{gathered}
K=\ker_L\partial_\rho,\quad [K:\mathbb C(t)]<\infty,\quad K'=\partial_tK,
\quad \ker_K\partial_t=\mathbb C,\\
L[y]=L[v],\qquad \mathbb C(y,z,w)=L(y),\\
z=n+6t^2y^2+k'y,\quad k\in K,\quad s=n_\rho\ne0,\\
\rho=a n^2+b n+c,\qquad
\eta:=1/s=2an+b\ne0,\qquad a,b,c\in K.
\end{gathered}
\tag{1}
\]
Here \(a\) is the quadratic cover coefficient, not the original speed
\(EX\). The latter will not be divided out in the original ring.
The element \(n\) is transcendental over \(K\), since
\(\partial_n:=\eta\partial_\rho\) kills \(K\) and takes \(n\) to one.
The field \(L/K(n)\) is finite separable, not yet assumed trivial.

Extend the derivative on \(K\) to \(K(n)\) fixing \(n\), and then
uniquely to \(L\). Denote it by \(\nabla\), or by a prime on coefficients.
It commutes with \(\partial_n\), since their commutator vanishes on
the finite separable base \(K(n)\). They satisfy
\[
\partial_\rho=\eta^{-1}\partial_n,\qquad
\partial_t^{\mathrm{old}}
 =\nabla-\frac{\rho'}{\eta}\partial_n,\qquad
\ker_L\partial_n=K .
\tag{2}
\]
This is a change of derivations on the given field, not a rationality
assumption about it.

For an independent formal \(U\), set
\[
d=4t,\quad h=k''/2,\quad F(U)=dU^3+hU^2,\quad M=\eta\ell,\qquad
\delta=\nabla-F_U\partial_n .
\tag{3}
\]
The polynomials \(P,\mathcal W\) from187 obey exactly
\[
P=\rho' U-\eta F+M,\qquad
\mathcal W_U=\delta P,\qquad \delta\mathcal W\in L^*,
\qquad w=\mathcal W(y).
\tag{4}
\]
Indeed \(P_U=\rho'-\eta F_U\), so the old differential operator
\(\partial_t^{\mathrm{old}}+P_U\partial_\rho\) is precisely \(\delta\).
The nonzero scalar in (4) retains the calibration from187; no
normalization of \(Ny\) is made or needed here.

## 2. Three coefficients remove the residual algebraic extension

Integrating only in the formal polynomial variable \(U\) gives
\[
\mathcal W
=aF^2-\eta'UF
 -\eta\left(\frac{d'}4U^4+\frac{h'}3U^3\right)
 +\frac{\rho''}2U^2+M'U-M_nF+W_0,\qquad W_0\in L .
\tag{5}
\]
Differentiating this expression in \(U\) gives
\[
\rho''U-\eta'F-\eta(d'U^3+h'U^2)+M'
 -F_U(\eta'U-2aF+M_n)=\delta P .
\]
Thus no unspecified coefficient-field integral was adjoined in (5).
The term involving \(d'\) is essential: unlike the earlier cusp
calculation, \(d=4t\) is not a constant.

For any coefficients \(\mathcal W_j=[U^j]\mathcal W\), the recurrence is
\[
[U^j]\delta\mathcal W
 =\mathcal W_j'-3d\,\partial_n\mathcal W_{j-2}
                  -2h\,\partial_n\mathcal W_{j-1}.
\tag{6}
\]
Missing coefficients are zero. Its two highest potentially nonzero
terms are
\[
\begin{aligned}
[U^6]\delta\mathcal W
 &=\frac72d(ad'+2da'),\\
[U^5]\delta\mathcal W
 &=12a'dh+3ad'h+4adh'+3d^2M_{nn}.
\end{aligned}
\tag{7}
\]
Since (4) is scalar and \(d\ne0\), these give
\[
2da'+ad'=0,\qquad
M_{nn}=\mu:=\frac{ahd'}{d^2}-\frac{4ah'}{3d}\in K,\qquad
M=\frac{\mu}{2}n^2+M_1n+M_0,\quad M_1,M_0\in K .
\tag{8}
\]
The last conclusion follows by two explicit primitive subtractions
with \(\partial_n\), whose kernel is exactly \(K\).

The \(U^2\) coefficient of (4), after (8), is
\[
3d(W_0)_n
 =\frac{a'''}2n^2
   +\left(\frac{b'''}2-h'\mu-3h\mu'\right)n
   +\frac{c'''}2-h'M_1-3hM_1' .
\tag{9}
\]
Consequently
\[
W_0=\frac{a'''}{18d}n^3
 +\frac{b'''/2-h'\mu-3h\mu'}{6d}n^2
 +\frac{c'''/2-h'M_1-3hM_1'}{3d}n+W_{00},
\qquad W_{00}\in K .
\tag{10}
\]
Equations (5), (8), and (10) show \(\mathcal W,P\in K[n,U]\);
in particular every coefficient of the actual \(z,w\) belongs to
\(K[n]\). Actual field return in (1) therefore gives
\[
L(y)=\mathbb C(y,z,w)\subset K(n)(y)\subset L(y).
\]
All inclusions are equalities. Intersecting with \(L\), and using
that \(y\) is transcendental over \(L\), proves
\[
L=K(n),\qquad \mathbb C(y,z,w)=K(y)(z).
\tag{11}
\]
For the intersection statement, clear the denominator of a rational
expression in \(y\) over \(K(n)\), and compare one nonzero denominator
coefficient. The second equality uses
\(n=z-6t^2y^2-k'y\), so \(z\) is transcendental over \(K(y)\).
This field argument used the actual inverse, not merely a Jacobian.

## 3. A polynomial-pencil degree bound

We use the following standard curve-degree consequence, with its
application-specific proof included. Let \(K/\mathbb C\) be a
one-variable function field, let \(y,z\) be independent over \(K\),
and suppose
\[
w=\sum_{i=0}^r f_i(y)z^i,\qquad f_i(y)\in K(y).
\]
If one coefficient is \(\gamma\in K\setminus\mathbb C\), then
\[
[K(y,z):\mathbb C(y,z,w)]\ \ge\ [K:\mathbb C(\gamma)].
\tag{12}
\]
The left extension is finite whenever \(w\) is nonconstant on the
coefficient curve, as it is under the stated coefficient assumption.

Take the nonsingular projective complex curve with function field \(K\).
After adjoining the independent parameters \(y,z\), it remains a
smooth integral curve. At a pole of \(\gamma\), extend the valuation
first to the coefficient curve over \(\mathbb C(y)\), then adjoining
\(z\). The valuation of \(w\) is the minimum of those of its
coefficients: after dividing by that minimum valuation, their
nonzero residues form a nonzero polynomial in the transcendental
\(z\), so no cancellation is possible. Thus the pole divisor of
\(w\) contains at least the base extension of the pole divisor
of \(\gamma\), with each multiplicity retained.

On a smooth proper curve, the degree of the pole divisor of a
nonconstant rational function equals the degree of its function-field
map to \(\mathbb P^1\). The latter equals the field extension degree.
Applying this first to \(w\), then to \(\gamma\), proves (12).
Purely transcendental base extension preserves the degree of the
finite map defined by \(\gamma\). Any additional poles of \(w\)
only strengthen the inequality.

The standard inputs can be located precisely in the Stacks Project:
[Theorem 53.2.6](https://stacks.math.columbia.edu/tag/0BY1) supplies the
nonsingular projective model and maps, and
[Lemma 33.44.11](https://stacks.math.columbia.edu/tag/0AYZ), applied to
the degree-one divisor at infinity, gives the pullback-degree formula.
[Definition 29.52.8](https://stacks.math.columbia.edu/tag/02NY) identifies
the map degree with the function-field degree.
These are retained standard inputs, not new claims about curves.

In particular, under the exact equality in (11), any nonconstant
coefficient \(\gamma\in K\) of the polynomial in \(z\) must satisfy
\[
K=\mathbb C(\gamma).
\tag{13}
\]
This conclusion is not obtained by assuming \(K\) rational in advance.

## 4. The genuine quadratic cover is impossible

Assume \(a\ne0\). Equation (8), with \(d=4t\), gives
\[
2ta'+a=0,\qquad a^2t=\kappa\in\mathbb C^* .
\tag{14}
\]
The constancy follows by differentiation and the constant field of \(K\).
Successive derivatives give \(a'''=-15a/(8t^3)\).
In (5), all terms other than \(W_0\) have \(n\)-degree at most two.
By (10), \(\mathcal W\) has \(n\)-degree exactly three, with coefficient
\[
\gamma=\frac{a'''}{18d}=-\frac{5a}{192t^4},\qquad
\gamma'=-\frac{9}{2t}\gamma,\qquad
\gamma^2t^9=\frac{25\kappa}{36864}\in\mathbb C^* .
\tag{15}
\]
The shift \(n=z-6t^2y^2-k'y\) preserves the coefficient of \(z^3\),
so \(\gamma\) is a coefficient to which (13) applies.
It is nonconstant by its displayed nonzero derivative.
Hence \(K=\mathbb C(\gamma)\), and \(t\) is a rational function of
\(\gamma\). At the discrete valuation of this rational function field
given by \(\gamma=0\), (15) would give
\[
2+9\,\operatorname{ord}_{\gamma=0}(t)=0,
\]
which is impossible for an integer valuation. Therefore \(a=0\).
In the notation of187, the quadratic cover coefficient \(A_c=2a\)
is zero.

## 5. The linear cover slope is constant

We now have \(\rho=bn+c\), with \(b\in K^*\). Equation (8) gives
\(\mu=0\), so \(M=M_1n+M_0\). From (5),
\[
\mathcal W_4=-b'd-\frac{bd'}4,\qquad
\mathcal W_2=\frac{b''n+c''}{2}-hM_1 .
\]
The coefficient \(\mathcal W_3\) is independent of \(n\).
Thus the \(U^4\) coefficient in (6) vanishes precisely when
\[
10db''+5d'b'+d''b=0,
\qquad\text{hence}\qquad 2tb''+b'=0 .
\tag{16}
\]
Also (10) now makes the coefficient of \(n^2\) in \(\mathcal W\)
equal to
\[
\gamma=\frac{b'''}{12d}.
\tag{17}
\]
No other term of (5) has \(n\)-degree two.

If \(b'\ne0\), put \(j=b'\). Then \(2tj'+j=0\),
\(j^2t=\lambda\in\mathbb C^*\), and
\[
b'''=j''=\frac{3j}{4t^2},\qquad
\gamma=\frac{j}{64t^3},\quad
\gamma'=-\frac{7}{2t}\gamma,\qquad
\gamma^2t^7=\frac{\lambda}{4096}\in\mathbb C^* .
\tag{18}
\]
Again \(\gamma\ne0\) is nonconstant. It is the leading coefficient
of the polynomial in \(z\) obtained by the same shift, now of degree
two. Equations (11)--(13) force \(K=\mathbb C(\gamma)\). Taking
the valuation at \(\gamma=0\) in (18) would require
\(2+7\operatorname{ord}(t)=0\), again impossible.
Thus \(b'=0\), and the constant field of \(K\) gives \(b\in\mathbb C^*\).

## Conclusion and remaining work

The exact new necessary conclusion under the full actual187 hypotheses is
\[
\boxed{a=0,\qquad b\in\mathbb C^*,\qquad
       \rho=bn+c,\quad c\in K,\qquad L=K(n),\qquad n_\rho=1/b.}
\tag{19}
\]
The remaining scalar equations still constrain \(h,M_1,M_0,c,W_{00}\).
They have not been solved or converted here into an invariant coordinate
of the original four-ring. In particular (11) is a field equality;
it is not a polynomial-ring identification over \(\mathbb C\).

The proof excludes formal quadratic and nonconstant-linear covers only
because of the actual field return. It must not be applied to formal
solutions that lack the polynomial inverse. This is not recognition
of every absent-variable chart, a proof of arbitrary entry, unrestricted
cancellation, historical novelty clearance, or expert/formal certification.
No earlier source has been changed.
