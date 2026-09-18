# Actual normalization of the square-root monomial square branch

Status: bounded working normalization lemma. In the actual full
\(Z^2-X^3Y\) setup, the square-completion family \(f=\beta q\),
\(\beta\in\mathbb C^*\), admits the original polynomial coordinate changes
below. They remove all lower terms of \(k,n\). In the quadratic-graph
subbranch a final constant translation also normalizes \(\ell\).
This is not, by itself, an exclusion or recognition theorem.

## 1. Exact hypotheses and derivative conventions

Assume an actual supplied globally sliced frame
\[
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad
\deg_E(X,Y,Z,W)=(1,1,2,2),\qquad
\ker\theta_0=(\mathsf Z^2-\mathsf X^3\mathsf Y).
\tag{1}
\]
Retain the [universal chart184](weight-four-universal-chart-potentials-pass184-working.md)
and its exact fields \(L/\mathbb C(t,\rho)\) and
\(K=\ker_L\partial_\rho\), finite over \(\mathbb C(t)\).
Here \(q^2=t\), \(q\in K\), and the derivative constants of \(K\)
are exactly \(\mathbb C\).
A prime in the potential identities denotes \(\partial_t\).
A dot in the calculations below denotes
\(\partial_q=2q\partial_t\), so \(\dot q=1\).
The two derivatives have the same constants.
Neither \(K=\mathbb C(q)\) nor an original polynomial coordinate
equal to \(q\) is assumed.

Suppose the actual nonzero-\(R\) branch has the square form and
monomial reciprocal coefficient
\[
\begin{gathered}
\mathcal H=A_2(V-P(U))^2+B_1U+B_0,\qquad
P=p_2U^2+p_1U+p_0,\qquad A_2p_2\ne0,\\
f=1/R=\beta q,\qquad \beta\in\mathbb C^*.
\end{gathered}
\tag{2}
\]
The actual hypotheses include the whole-line and calibrated scalar
Jacobian used in the [general square gate193](weight-four-split-square-candidate-jacobian-obstruction-pass193-working.md).
In particular \((B_1)_\rho=0\).
The [classification195](weight-four-square-root-two-gate-classification-pass195-working.md)
does not exclude (2); it supplies its necessary coefficient values.

First make the actual constant scaling \(W_1=W/\beta\), fixing
\(X,Y,Z\), with inverse \(W=\beta W_1\).
It gives \(\rho_1=\rho/\beta\), \(\vartheta_1=\vartheta/\beta\) and
\(R_1=\beta R=1/q\).
The monomial formula \(\nu=-1/(\beta^2q^3)\) becomes
\(\nu_1=\beta^2\nu=-q^{-3}\).
Drop the subscript after this actual scaling. We therefore work with
\[
R=q^{-1},\quad \nu=-q^{-3},\quad
\Delta=RR''/2-(R')^2=\frac1{8q^6},\quad
k=\rho/q+k_0,\quad
n=-\frac{\rho^2}{2q^3}+s_0\rho+n_0,\qquad k_0,s_0,n_0\in K.
\tag{3}
\]
Only a nonzero complex number was divided out in the original ring.

## 2. Raw coefficient equations and exact integration of k and s

For independent \(U,V\), the universal coefficient identity is
\[
\begin{aligned}
S&=dU^3+\frac{k_{tt}}2U^2+R'UV+n_tU+n_\rho V,\\
T&=eU^4+\frac{k_{ttt}}6U^3+\frac{R''}2U^2V
 +\frac{n_{tt}}2U^2+n_{t\rho}UV+\frac{\nu}2V^2,\\
\mathcal H&=R(T-\ell_tU-\ell_\rho V-m)
 +(R'U+n_\rho)(\ell-S),\\
d&=\frac1{16q^5},\qquad e=-\frac5{128q^7}.
\end{aligned}
\tag{4}
\]
All coefficient derivatives precede evaluation at \(U=y,V=\vartheta\).
Define, with all primes still meaning \(\partial_t\),
\[
\begin{gathered}
\mathcal B=Rn_{t\rho}-2R'n_\rho,\qquad
\mathcal C_2=\frac{Rn_{tt}}2-R'n_t-\frac{n_\rho k_{tt}}2,\qquad
\mathcal C=-R\ell_\rho-n_\rho^2,\\
\ell_\rho=\frac{\mathcal B^2}{2\Delta R}
          -\frac{\nu\mathcal C_2}{\Delta}-\frac{n_\rho^2}{R},\\
B_1=-R\ell_t+R'\ell-n_\rho n_t-\frac{\mathcal B\mathcal C}{R\nu}.
\end{gathered}
\tag{5}
\]
The right side for \(\ell_\rho\) is polynomial in \(\rho\) of degree
at most two. Subtracting its explicit polynomial primitive shows
\(\ell\in K[\rho]\), of degree at most three, with one integration
constant in \(K\). No primitive is adjoined to the coefficient field.

The \(U^3V^0\) comparison in (2) is
\(Rk_{ttt}/6-R'k_{tt}/2-dn_\rho-\Delta\mathcal B/(R\nu)=0\).
Substituting (3) and \(\partial_t=(2q)^{-1}\partial_q\) gives exactly
\[
\frac{q\dddot k_0+3q\dot s_0+3s_0}{48q^5}=0,\qquad
s_0=\frac{\dot k_0-q\ddot k_0+c}{3q},\quad c\in\mathbb C.
\tag{6}
\]
For the integration, \((qs_0)^{\boldsymbol\cdot}
=-q\dddot k_0/3\), and an explicit primitive of
\(-q\dddot k_0\) is \(\dot k_0-q\ddot k_0\).
The remaining constant belongs to \(\ker\partial_q=\mathbb C\).

Using (6) in (5), coefficient extraction gives
\[
[\rho^3]B_1=0,\qquad
[\rho^2]B_1=\frac{q\,k_0^{(5)}+5k_0^{(4)}}{12q^3}.
\tag{7}
\]
Superscripts in parentheses mean repeated \(q\)-derivatives.
The integration constant in \(\ell\) does not enter (7).
Since \((B_1)_\rho=0\), the numerator in (7) vanishes.
Equivalently \((q^5k_0^{(4)})^{\boldsymbol\cdot}=0\).
The fourth derivative of \(q^{-1}\) is \(24q^{-5}\).
Subtract this explicit primitive and then four polynomial primitives.
The complete solution in the exact field is
\[
\begin{gathered}
k_0=\frac{\kappa_{-1}}{q}+\kappa_0+\kappa_1q+\kappa_2q^2+hq^3,\\
s_0=\frac{\sigma}{q}-hq-\frac{\kappa_{-1}}{q^3},\qquad
\sigma=\frac{\kappa_1+c}{3},
\end{gathered}
\tag{8}
\]
with every displayed coefficient complex. This does not assume
rationality of \(K\); the equations prove rationality of these particular
coefficients.

## 3. The remaining positive-rho coefficient determines n0

Substitute (8) in (5), leaving \(n_0\) and the constant term of \(\ell\)
unrestricted in \(K\). The next coefficient is
\[
[\rho]B_1
=-\frac{\dddot n_0+3\ddot n_0/q
                +60h^2q^2-24h\sigma-12\kappa_{-1}^2/q^6}{2q^2}.
\tag{9}
\]
It again cannot be altered by the constant term of \(\ell\), by \(m\),
or by the constant eliminant remainder \(B_0\).
Its vanishing is equivalent to
\[
(q^3\ddot n_0)^{\boldsymbol\cdot}
=-60h^2q^5+24h\sigma q^3+12\kappa_{-1}^2q^{-3}.
\]
Explicit integration three times yields
\[
n_0=-\frac{h^2q^5}{2}+h\sigma q^3-\frac{\kappa_{-1}^2}{2q^3}
       +\frac{v_-}{q}+v_0+v_+q,\qquad v_-,v_0,v_+\in\mathbb C.
\tag{10}
\]
For completeness, after the first integration one has
\(q^3\ddot n_0=-10h^2q^6+6h\sigma q^4-6\kappa_{-1}^2q^{-2}+C_0\).
The next two integrations give (10), with \(v_-=C_0/2\).
Every remainder after primitive subtraction is a derivative constant
in the same exact field. No logarithm or finite-field rationality
hypothesis is used.

## 4. First actual polynomial shear removes k0

Set
\[
P_2(X,Y)=\kappa_{-1}X^2+\kappa_1XY+hY^2,\qquad
P(t)=\kappa_{-1}+\kappa_1t+ht^2.
\]
Make the actual polynomial change
\[
X_1=X,\quad Y_1=Y,\quad
Z_1=Z-\kappa_0X-\kappa_2Y,\quad
W_1=W+P_2(X,Y).
\tag{11}
\]
Its inverse is
\(Z=Z_1+\kappa_0X_1+\kappa_2Y_1\),
\(W=W_1-P_2(X_1,Y_1)\), with \(X=X_1,Y=Y_1\).
Both compositions are literal polynomial cancellations.

The chart ratios \(t,q\) and \(y\) are unchanged, while
\[
\rho_1=\rho+P(t),\qquad
\vartheta_1=\vartheta+P'(t)y,\qquad
w_1=w+hy^2,\qquad z_1=z-\kappa_2y .
\]
Here \(P'(t)\) means its \(t\)-derivative.
The coefficient of \(X\) in \(Z_1\) gives
\(k_1=\rho_1/q\), since
\(k_0-P(t)/q=\kappa_0+\kappa_2t\).
The second universal potential gives exactly
\(n_1=n(\rho_1-P(t))\).
In verifying this assertion, the change in the fixed-\(\rho\)
\(t\)-derivative is included: the residual \(y\)-coefficient is
\((k_0-P/q)'-\kappa_2=0\).
Consequently
\[
\begin{gathered}
k_1=\rho_1/q,\qquad
n_1=-\frac{\rho_1^2}{2q^3}+\frac{C\rho_1}{q}
       +\frac{N_-}{q}+N_0+N_+q,\\
C=\sigma+\kappa_1,\quad N_-=v_--\sigma\kappa_{-1},\quad N_0=v_0,\quad
N_+=v_+-\sigma\kappa_1+h\kappa_{-1}-\kappa_1^2/2 .
\end{gathered}
\tag{12}
\]
All constants in (12) are complex.

## 5. Translate X and apply two lower-degree shears

For any complex \(a\), make the actual change
\[
X_2=X_1+a,\qquad Y_2=Y_1,\qquad Z_2=Z_1,\qquad
W_2=W_1-\frac{3a}{2}X_2Y_2 .
\tag{13}
\]
The inverse is \(X_1=X_2-a\), \(Y_1=Y_2\), \(Z_1=Z_2\),
\(W_1=W_2+(3a/2)X_2Y_2\).
Again both orders are polynomial identities.

Rewrite the old chart in the new time coordinate \(X_2\). Directly,
\[
\begin{gathered}
y_2=y_1-aq^2,\qquad
\rho_2=\rho_1-\frac{3a}{2}q^2,\qquad
\vartheta_2=\vartheta_1-2a\rho_1-\frac{3a}{2}y_2,\\
z_2=z_1-a(q'y_1+\rho_1/q)+a^2q,\qquad
w_2=w_1-a\vartheta_1+a^2\rho_1 .
\end{gathered}
\tag{14}
\]
The coefficient of \(X_2\) in \(Z_2\) gives \(k_2=\rho_2/q\).
Using \(Q=q''/2=-1/(8q^3)\) in the second potential gives
\[
n_2=n_1+\frac{a\rho_1}{2q}+\frac{3a^2q}{8}
=-\frac{\rho_2^2}{2q^3}+\frac{(C-a)\rho_2}{q}
  +\frac{N_-}{q}+N_0+\left(N_++\frac{3Ca}{2}\right)q .
\tag{15}
\]
Thus choose \(a=C\).
Put \(D_-=N_-\), \(D_0=N_0\), \(D_+=N_++3C^2/2\), and make
\[
X_3=X_2,\quad Y_3=Y_2,\quad
Z_3=Z_2-D_0,\qquad
W_3=W_2+D_-X_2+D_+Y_2 .
\tag{16}
\]
The inverse subtracts the displayed linear polynomial from \(W_3\)
and adds \(D_0\) to \(Z_3\). The chart has the same \(q,t,\rho_2\).
Its new \(\vartheta\) gains \(D_-+D_+t\), and its projected \(z\)
loses \(D_0\). Therefore \(n\) loses
\((D_-+D_+t)/q+D_0\). Relabeling the final coefficients gives
\[
k=\frac{\rho}{q},\qquad n=-\frac{\rho^2}{2q^3}.
\tag{17}
\]
This proves the actual normalization assertion, not merely a change
of coefficient-field variables.

## 6. The graph subbranch and the last constant translation

Suppose additionally that the selected projection is a quadratic graph,
rather than a quadratic projection: \(y\) is affine on the full generic
line and \(\vartheta\) is a degree-two polynomial in \(y\).
Apart from the initial nonzero complex scaling of \(\vartheta\), every
preceding change replaces \(y\) by an affine translation over \(L\)
and replaces \(\vartheta\) by its old value plus a polynomial of degree
at most one in the old \(y\).
Thus the quadratic graph property and its nonzero top coefficient
are preserved. Under the retained actual whole-plane and cofactor
gates, its completed square form has \(B_1=0\).

For the bare coefficients (17), equation (5) becomes
\[
\ell_\rho=-\frac{3\rho^2}{2q^5},\qquad
\ell=-\frac{\rho^3}{2q^5}+\ell_0,\quad \ell_0\in K,\qquad
B_1=-\frac{q\dot\ell_0+\ell_0}{2q^3}.
\tag{18}
\]
Since this is the graph subbranch, \(B_1=0\). The exact constant field
gives \(\ell_0=\lambda/q\), with \(\lambda\in\mathbb C\).
The actual final translation \(W_4=W_3-\lambda\), with inverse
\(W_3=W_4+\lambda\), subtracts \(R\lambda=\lambda/q\) from the cubic,
third potential. It leaves \(k,n,\vartheta,\rho\) unchanged and yields
\[
k=\rho/q,\qquad n=-\rho^2/(2q^3),\qquad
\ell=-\rho^3/(2q^5).
\tag{19}
\]
Nothing here asserts that the projected \(z\), initially in \(L\),
is in \(K\). Such membership needs a separate scalar-Jacobian gate.

## 7. Original-ring and scope checks

All maps above and their inverses have complex polynomial coefficients.
Their composition is therefore an actual polynomial automorphism.
They preserve the given global slice and the same derivation \(E\).
The ratios \(q,t\) and the speed \(EX\) are unchanged.
In every inverse map the old \(X,Y,W\) are independent of the new
\(Z\), and the old \(Z\) is the new \(Z\) plus a polynomial in the
new \(X,Y\). Thus the selected actual partial \(\partial_Z\) is
literally unchanged. Since the slice \(u\) is also unchanged, so is
\(N=[u^3]\partial_Z|_A\), its constant field \(L\), and the selected
generic line. The fields \(K\) agree as well: the displayed changes
of \(\rho\) are a nonzero complex scaling followed by functions of
\(t\), so they have the same \(\rho\)-derivative constants. This
justifies preserving the affine or quadratic generic degree of \(y\)
under the stated affine translations.
Every shift of \(\rho\) is by a function of \(t\) in the exact field;
it is the effect of an explicitly displayed original polynomial map.

The exact time degrees remain \((1,1,2,2)\).
The lower-degree changes in \(Z\) cannot cancel its nonzero quadratic
leader. The quadratic changes in \(W\) replace \(\rho\) by
\(\rho+P(t)\) or \(\rho-3at/2\), which are nonzero because \(t,\rho\)
are independent. Their full filtered initial maps are invertible;
they fix the leading \(X,Y,Z\) slots and change only the absent \(W\)
slot by a nonzero constant scaling and a binary quadratic polynomial.
Thus the entire initial ideal
\((\mathsf Z^2-\mathsf X^3\mathsf Y)\) is preserved, not just its
displayed relation.

The general square lemma stops at (17). The graph-specific conclusion
is (19). This note does not extend (17) to the general
\(f=at+bq\) family with \(a\ne0\) or the family \(f=b/q\).
It does not extend the extra conclusion (19) to the quadratic-projection
subbranch, although (17) does apply to that subbranch when \(f=\beta q\).
Nor does it claim recognition or exclusion solely from (19).
Any composition with the separate
[normalized-graph obstruction196](weight-four-normalized-square-root-graph-obstruction-pass196-working.md)
must justify that note's additional projected-\(g\) hypotheses; they
are not consequences of a coefficient normalization alone.

The formulas (6), (7), (9) and (18) were independently expanded from
the raw potentials in (4)--(5). A new read-only symbolic calculation
provided an arithmetic cross-check; no saved checker was executed,
imported or compiled. Exact integration and both orders of all original
coordinate changes are written above.
No195 or earlier source was edited, and no cancellation, minimum-profile,
entry, novelty or formal-certification claim is made.
