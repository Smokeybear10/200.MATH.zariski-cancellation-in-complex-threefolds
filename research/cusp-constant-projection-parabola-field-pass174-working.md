# The constant-projection cusp chart has a rational parabola coefficient field

**Status: complete working field and localization reduction.**

In the actual cusp chart159 with \(r=k_\rho\ne0\) and \(y\in L\),
the other projected original coordinate \(z\) is a parameter for
the whole generic line. Write \(w\) as a quadratic polynomial in
\(z\) over \(L\). Actual field return, together with the single
actual localization at \(EX\), forces its two nonconstant-z
coefficients to lie in \(\mathbb C(y)\). Its constant coefficient
then generates the entire remaining coefficient field.

The result is
\(w=\alpha(y)z^2+\beta(y)z+g\),
\(L=\mathbb C(y,g)\). The rational functions \(\alpha,\beta\)
are not yet declared polynomial in the original ring. An integral
coordinate construction and recognition are separate steps.

## 1. The exact actual chart and the selected vertical line

Retain all hypotheses of
[the actual cusp chart159](cusp-generic-chart-first-reductions-pass159-working.md):
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\\
(\deg_E X,\deg_E Y,\deg_E Z,\deg_E W)=(1,1,2,2),\qquad
\ker\theta_0=(\mathsf X\mathsf Z-\mathsf Y^3),\\
a=EX\ne0,\qquad N=[u^3](\partial_Z|_A),\qquad
L=\operatorname{Frac}(\ker_A N),\qquad A_L=L[v],\qquad Nv=1.
\end{gathered}
\tag{1}
\]
The initial ideal is the full weighted initial kernel. Set
\(t=EY/a\) and \(\rho=(E^2W/2)/a^2\). They are algebraically
independent over \(\mathbb C\), and \(L/\mathbb C(t,\rho)\)
is finite separable. The coefficient partials on this exact
field commute.

The original inverse supplies
\[
\begin{gathered}
B_a=A_a[X],\qquad
A_a=\mathbb C[y,z,w]_{a_0},\qquad a=a_0(y,z,w)\in L^*,\\
\operatorname{Frac}A=\mathbb C(y,z,w)=L(v),\qquad
L[y,\vartheta]=L[v],\\
Y=y+tX,\qquad
Z=z+(3t^2y+k)X+t^3X^2,\qquad
W=w+\vartheta X+\rho X^2,\\
z=3ty^2+k_t y+r\vartheta+n,\qquad r=k_\rho,\qquad k,n\in L .
\end{gathered}
\tag{2}
\]
Here \(a_0\) is a nonzero polynomial, and \(y,z,w\) are
algebraically independent over \(\mathbb C\). The single
localization in (2), not just the equality of fraction fields,
will be essential below. In particular \(t,\rho\in A_a\cap L\).

Assume \(r\ne0\) and \(y\in L\). Then (2) gives
\(L[\vartheta]=L[v]\), so \(\vartheta\) is affine in \(v\)
with nonzero slope. Consequently \(z\) is also affine with
nonzero slope, and
\[
L[z]=L[v],\qquad \operatorname{Frac}A=L(z),\qquad
\ker\{L[U,V]\longrightarrow L[v]\}=(U-y).
\tag{3}
\]
No coefficient has been replaced by a complex constant in this
step.

The calibrated actual determinant also proves \(y_\rho\ne0\).
If it vanished, its first row would be \((X+y_t,0,0)\), since
\(y_v=0\). The determinant would be divisible by \(X+y_t\)
in \(L[v][X]\), contradicting its nonzero constant value
\(-a^3\). It follows that \(t,y\) are algebraically independent:
the rho derivation kills \(\mathbb C(t)\), so it kills any
separable algebraic element over that field. Hence
\[
y_\rho\ne0,\qquad
L/\mathbb C(t,y)\text{ is finite separable}.
\tag{4}
\]
Finiteness follows because \(L\) is a finitely generated field
of transcendence degree two and \(t,y\) are a transcendence basis.

The selected-factor issue is not discarded. The unit-gradient
statement in159 and the full kernel (3) give exactly
\[
\Phi-m=c_*(U-y)+(U-y)^2H_*,\qquad
c_*\in L^*,\quad H_*\in L[U,V].
\tag{5}
\]
Indeed the evaluated cofactor is a unit of \(L[v]\), hence lies
in \(L^*\); subtracting it leaves an element of \((U-y)\).
We do not assume \(H_*=0\), and the argument below does not
need that assertion.

## 2. Literal coefficients of the projected parabola

For this section all subscripts \(t,\rho\) mean the original
coefficient partials, not partials holding \(y\) fixed. Define
\[
\begin{gathered}
\zeta=3ty^2+k_t y+n,\qquad
C_0=y^3+\tfrac12 k_{tt}y^2+n_t y,\qquad
C_1=r_t y+n_\rho,\\
z=\zeta+r\vartheta,\qquad
rw=\ell-C_0-C_1\vartheta-\tfrac12 r_\rho\vartheta^2 .
\end{gathered}
\tag{6}
\]
The second identity is precisely the actual \(X^2\)-potential159
evaluated at \((y,\vartheta)\). Substitution of
\(\vartheta=(z-\zeta)/r\) gives
\[
\begin{gathered}
w=p_2z^2+p_1z+p_0,\qquad p_2,p_1,p_0\in L,\\
p_2=-\frac{r_\rho}{2r^3},\qquad
p_1=\frac{r_\rho\zeta}{r^3}-\frac{C_1}{r^2},\\
p_0=\frac{\ell-C_0}{r}+\frac{C_1\zeta}{r^2}
                         -\frac{r_\rho\zeta^2}{2r^3} .
\end{gathered}
\tag{7}
\]
Degree drops are allowed. In particular neither \(p_2\ne0\)
nor \(p_1\ne0\) is presumed.

Put \(k_b=\mathbb C(y)\). The actual equality to be used is
\[
k_b(z,w)=L(z),\qquad
\operatorname{trdeg}_{k_b}L=1,\qquad
z\text{ transcendental over }L .
\tag{8}
\]
The base field \(k_b\) is not algebraically closed. Nevertheless
it is relatively algebraically closed in \(L\), by (8): any
element of \(L\) algebraic over \(k_b\) lies in the purely
transcendental field \(k_b(z,w)\), whose algebraic constants
are exactly \(k_b\). One elementary justification is that such
an element is integral over the integrally closed ring
\(k_b[z,w]\), hence polynomial in \(z,w\). A nonconstant
polynomial is transcendental over \(k_b\), by its total degree.
Here \(z,w\) are independent over \(k_b\), as follows also
from the actual independent triple \(y,z,w\).

## 3. A quadratic pencil with exact field return

We prove an elementary consequence of (7)--(8). If a positive-z
coefficient is outside \(k_b\), there is an element \(T\)
transcendental over \(k_b\) such that
\[
L=k_b(T),\qquad w=A(z)T+B(z),\qquad
A,B\in k_b[z],\qquad \deg A\in\{1,2\} .
\tag{9}
\]

First suppose \(p_2\notin k_b\). Relative algebraic closure
proved above makes \(p_2\) transcendental over \(k_b\).
Use the degree-at-z-infinity valuation of \(L(z)\), with
\(\operatorname{val}(z)=-1\). Every nonzero polynomial
\(P(z,w)\) over \(k_b\) has the weighted degree predicted by
weights \((1,2)\). Its highest coefficient after substitution
is a nonzero polynomial in \(p_2\), so it cannot cancel.
For a ratio of two such polynomials with valuation zero, the
residue is a ratio of their highest coefficients and lies in
\(k_b(p_2)\). Conversely \(w/z^2\) has residue \(p_2\).
Thus the restricted residue field is exactly \(k_b(p_2)\).
The full field \(L(z)\) has residue field \(L\). Equality
(8) therefore gives \(L=k_b(p_2)\).

Set \(T=p_2\). We next show \(p_1,p_0\in k_b+k_bT\).
Write these two rational functions with a common polynomial
denominator:
\(p_1=A_1(T)/D(T)\), \(p_0=A_0(T)/D(T)\), where
\(D,A_1,A_0\in k_b[T]\), \(D\ne0\), and their common gcd
is one. As a rational function of \(T\) over \(k_b(z)\),
\[
w=\frac{T D(T)z^2+A_1(T)z+A_0(T)}{D(T)} .
\tag{10}
\]
Numerator and denominator are coprime over \(k_b(z)\): a
factor of \(D\) dividing the numerator must divide both
\(A_1\) and \(A_0\), since \(z\) is independent.
The numerator has T-degree at least \(\deg D+1\), because
its \(z^2\) coefficient is \(TD\).

For relatively prime polynomials \(P(T),Q(T)\) over a field,
the rational function \(P(T)/Q(T)\) has function-field degree
\(\max(\deg P,\deg Q)\). This follows directly from
\(P(T)-VQ(T)\): it is primitive and irreducible, being linear
in the independent \(V\) after passage to the fraction field
in \(T\), and its T-degree is that maximum. Gauss's lemma
then gives the asserted field degree.
Apply this to (10). Equation (8) makes that degree one.
Consequently \(D\) is constant, and both \(A_1,A_0\) have
degree at most one. This proves (9) with \(\deg A=2\).

Now suppose \(p_2\in k_b\) and \(p_1\notin k_b\). Replace
\(w\) by \(w-p_2z^2\) in (8). Weights \((1,1)\) and the
same highest-coefficient argument give \(L=k_b(p_1)\).
Set \(T=p_1\) and write \(p_0=A_0(T)/D(T)\) in lowest terms.
The numerator of \(Tz+p_0\) is \(TDz+A_0\), again of
T-degree at least \(\deg D+1\) and coprime to \(D\).
Degree one forces \(D\) constant and \(\deg A_0\le1\).
This proves (9) with \(\deg A=1\).

If instead \(p_2,p_1\in k_b\), subtraction in (7) and (8)
already gives \(k_b(p_0)(z)=L(z)\). Intersecting with \(L\)
then gives \(L=k_b(p_0)\). For this elementary intersection,
write an element of \(L\cap k_b(p_0)(z)\) as a rational
function in the independent \(z\), clear its denominator and
compare a nonzero coefficient. No assumption about rationality
of \(L\) was made in any of these cases.

## 4. The actual localization excludes both nonconstant leading cases

Suppose (9) holds. We first claim
\[
k_b[z,w]\cap L=k_b .
\tag{11}
\]
To prove it, let a nonzero polynomial \(P(z,w)\) lie in
\(L=k_b(T)\), and write \(m=\deg_w P\). Substitution of
\(w=A(z)T+B(z)\) makes it a polynomial in \(z,T\).
Its membership in \(k_b(T)\) then makes it a polynomial in
\(T\) alone, by coefficient comparison in the independent \(z\).
If \(m>0\), its highest T-coefficient is
\(P_m(z)A(z)^m\), where \(P_m\ne0\) is the highest
w-coefficient of \(P\). This cannot be constant in \(z\),
since \(A\) has positive degree. If \(m=0\), membership in
\(k_b(T)\) forces \(P(z)\in k_b\). This proves (11).

Return now to the actual speed \(a=a_0(y,z,w)\) in (2).
It belongs both to \(\mathbb C[y,z,w]\subset k_b[z,w]\)
and to \(L\). Equation (11) therefore puts it in \(k_b\).
Independence of \(y,z,w\) shows
\(\mathbb C[y,z,w]\cap\mathbb C(y)=\mathbb C[y]\), so
\(a\in\mathbb C[y]\setminus\{0\}\). In particular,
\[
A_a=\mathbb C[y,z,w]_{a_0}\subset k_b[z,w],\qquad
t,\rho\in A_a\cap L\subset k_b=\mathbb C(y).
\tag{12}
\]
The final inclusion contradicts algebraic independence of the
two actual ratios \(t,\rho\). Thus (9) is impossible in the
actual cusp chart. This step does not make \(a\) a global
unit. It uses its actual polynomial representative and precisely
the permitted localization at that representative.

## 5. Exact conclusion and the next integral step

Both positive-degree cases have been excluded. The remaining
case of Section 3 proves
\[
w=\alpha(y)z^2+\beta(y)z+g,\qquad
\alpha,\beta\in\mathbb C(y),\qquad
L=\mathbb C(y,g).
\tag{13}
\]
Here \(g\) is transcendental over \(\mathbb C(y)\), since
\(L\) has transcendence degree two over \(\mathbb C\).
The explicit formulas in (7) identify
\(\alpha=p_2\), \(\beta=p_1\), and \(g=p_0\).
Together with (4), this permits coefficient differentiation in
the exact independent variables \((t,y)\) in the same field.

The proof has not declared \(y\), \(g\), \(\alpha(y)\), or
\(\beta(y)\) integral in the original four-ring. It does not
replace the selected relation (5) by its linear factor alone.
The remaining determinant coefficients and any original-ring
coordinate correction must still be proved. Other initial
configurations and unrestricted entry are outside this result.

The actual chart and selected-factor premises were fully read
for this proof. The residue and rational-map arguments are
supplied here; they use the same elementary mechanisms as the
[nonconstant-ratio supplement171](cusp-pure-quadratic-nonconstant-ratio-exclusion-pass171-working.md)
without importing its different coefficient hypotheses.
No new external theorem is invoked. There is no claim of
unrestricted cancellation, historical novelty, human expert
review, proof-assistant certification, or recursive audit of
all earlier dependencies. No frozen source or earlier checker
is edited or rerun.
