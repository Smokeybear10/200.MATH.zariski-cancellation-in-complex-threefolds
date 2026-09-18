# Polynomial coefficients over a one-variable field in the conical mismatch branch

The actual tangent-graph reduction forces its remaining coefficients to
be polynomial in a reparameterized field variable. Their degrees give a
monic relation \(W-G_K(X,Y,Z)=0\), with \(\deg G_K\le4\), over a
transcendence-degree-one invariant field \(K\).

This note starts from the separately proved actual-chart reduction.
It does not assume that arbitrary formal jets are realizable, that
\(L=K(\kappa)\), or that \(K\) has a polynomial generator. Descent from
this coefficient-field relation to a complex polynomial invariant is a
separate step and is not used here.

## 1. The proved actual-chart input

Use the nonlinear conical, nonradial hypotheses and notation of the
tangent-graph reduction136.[^1] In particular the original generators
are actual coordinates in \(B=\mathbb C[X,Y,Z,W]=A[u]\), the derivation
\(E=\partial_u\) has the given global slice, and \(s=EX\ne0\).
The coefficient field \(L\subset\operatorname{Frac}A\) is finite and
separable over \(\mathbb C(\tau,\sigma)\). The element \(\rho\) is
algebraic over \(\mathbb C(\tau)\). The proved formulas are
\[
\begin{gathered}
B_s=A_s[X],\qquad A_L=L[v]=L[y],\qquad y_v\in L^*,\\
Y=y+\tau X,\qquad Z=z+\rho X,\qquad
W=w+dX+\tfrac12\sigma X^2,\\
z=\rho' y+k,\qquad k,\ell,m\in L,\qquad k_\sigma\ne0,\qquad
r:=\rho''\ne0,\\
d=-\frac{r}{4k_\sigma}y^2-\frac{k_\tau}{2k_\sigma}y+\ell,\\
w_y=d_\tau-\frac{r y+k_\tau}{k_\sigma}d_\sigma,\qquad
1=y_v\left(\frac{r y+k_\tau}{k_\sigma}w_\sigma-w_\tau\right).
\end{gathered}
\tag{1}
\]
Here \(d,w\) are first viewed as polynomials in the formal variable
\(y\) over \(L\), and their coefficient derivatives hold that variable
fixed. The initial subscripts \(\tau,\sigma\) are the uniquely extended
partials in the original coefficient field. Primes on \(\rho\) mean
\(\partial_\tau\). The proof of (1) establishes \(y_v\in L^*\), rather
than assuming a linear generic parameter at the outset.

Nonlinearity gives \(r\ne0\): if \(\rho''=0\), the constant-field
argument in the chart proof makes \(\rho\) an affine function of
\(\tau\) with complex coefficients, giving a forbidden homogeneous
linear speed relation. No conclusion that \(r\) must vanish will be
drawn from the residual scalar equations.

## 2. An exact reparameterization and its constant field

Put \(\kappa=k\). Since \(k_\sigma\ne0\), separability implies that
\(\kappa\) is not algebraic over \(\mathbb C(\tau)\). Thus
\(\tau,\kappa\) are algebraically independent, and
\(L/\mathbb C(\tau,\kappa)\) is finite and separable.

Write \(\partial_\tau^{\rm old},\partial_\sigma^{\rm old}\) for the
old coefficient derivatives. The unique new coordinate derivatives are
\[
\partial_\kappa=\frac{1}{k_\sigma}\partial_\sigma^{\rm old},
\qquad
\partial_\tau=\partial_\tau^{\rm old}
             -\frac{k_\tau}{k_\sigma}\partial_\sigma^{\rm old},
\qquad
\sigma_\kappa=\frac1{k_\sigma},\qquad
\sigma_\tau=-\frac{k_\tau}{k_\sigma}.
\tag{2}
\]
They have the displayed values on \(\tau,\kappa\), hence are precisely
the extensions of the rational coordinate partials and commute.
The new derivative of \(\rho\) is the old one, since
\(\partial_\sigma^{\rm old}\rho=0\).
All subscripts from now on use the new derivatives, with \(\kappa\)
fixed under \(\partial_\tau\).

Define
\[
K=\ker(\partial_\kappa:L\longrightarrow L).
\quad\text{Then}\quad
K=\overline{\mathbb C(\tau)}^{\,L},\qquad
[K:\mathbb C(\tau)]<\infty,\qquad
\partial_\tau K\subset K,\qquad \rho,r\in K.
\tag{3}
\]
The bar denotes relative algebraic closure, not an algebraic closure
of the whole field. Here is the exact justification. If \(f\in K\),
differentiate its monic minimal polynomial over
\(\mathbb C(\tau,\kappa)\) by \(\partial_\kappa\).
The differentiated coefficients give a polynomial of smaller degree
annihilating \(f\), so all those coefficients vanish. The original
coefficients therefore belong to \(\mathbb C(\tau)\), proving
algebraicity. Conversely, separable algebraicity over
\(\mathbb C(\tau)\) makes \(\partial_\kappa f=0\).

The element \(\kappa\) is transcendental over \(K\), since its
derivative is one. Elements linearly independent in \(K\) over
\(\mathbb C(\tau)\) remain independent after adjoining \(\kappa\).
Their number is bounded by
\([L:\mathbb C(\tau,\kappa)]\), proving the finiteness in (3).
Commutation of the new partials proves stability under
\(\partial_\tau\). Thus \(K\) is a transcendence-degree-one subfield
of \(\operatorname{Frac}A\). None of these arguments asserts
\(L=K(\kappa)\).

## 3. Explicit integration in the line variable

On \(L[y]\), define \(\mathcal D=\partial_\tau-r y\partial_\kappa\),
where both coefficient derivatives kill the formal \(y\). Equations
(1)--(2) become
\[
d=-\tfrac14r\sigma_\kappa y^2+\tfrac12\sigma_\tau y+\ell,
\qquad w_y=\mathcal Dd,\qquad
\mathcal Dw=-1/y_v\in L^*.
\tag{4}
\]
In particular, \(\mathcal Dw\) has no positive power of \(y\).
The identity for the operator follows by substituting (2) into the
old expression
\(\partial_\tau^{\rm old}-(r y+k_\tau)\partial_\sigma^{\rm old}/k_\sigma\).
The \(k_\tau\) terms cancel.

Integrating \(w_y=\mathcal Dd\) only in the polynomial variable \(y\)
gives
\[
\begin{aligned}
w={}&\frac{r^2\sigma_{\kappa\kappa}}{16}y^4
-\left(\frac{r'\sigma_\kappa}{12}
       +\frac{r\sigma_{\tau\kappa}}4\right)y^3\\
&+\left(\frac{\sigma_{\tau\tau}}4
        -\frac{r\ell_\kappa}{2}\right)y^2
 +\ell_\tau y+m,\qquad m\in L.
\end{aligned}
\tag{5}
\]
The constant \(m\) is the actual constant coefficient of \(w\) in
this polynomial expression. No integration of algebraic coefficient
functions in \(\tau\) or \(\kappa\) has been assumed.

Three coefficients of the last equation in (4) now give
\[
\begin{aligned}
0=[y^5]\mathcal Dw
   &=-\frac{r^3}{16}\sigma_{\kappa\kappa\kappa},\\
0=[y^3]\mathcal Dw
   &=-\frac{r''}{12}\sigma_\kappa
     -\frac{r'}3\sigma_{\tau\kappa}
     -\frac r2\sigma_{\tau\tau\kappa}
     +\frac{r^2}{2}\ell_{\kappa\kappa},\\
0=[y]\mathcal Dw
   &=\ell_{\tau\tau}-r m_\kappa.
\end{aligned}
\tag{6}
\]
Primes on \(r\) use the new \(\partial_\tau\).
The omitted coefficients of \(y^4,y^2\), and the constant coefficient
are further necessary conditions on actual solutions; they are not
claimed to follow from (6). They are unnecessary for the polynomial
degree conclusions below.

## 4. Polynomial descent without assuming a rational larger field

An elementary differential fact suffices. In any characteristic-zero
field with a derivation \(\partial_\kappa\) satisfying
\(\partial_\kappa\kappa=1\) and constant field \(K\),
if \(\partial_\kappa^{\,n+1}f=0\), then \(f\in K[\kappa]\) has
degree at most \(n\). Indeed
\((\partial_\kappa^n f)/n!\in K\); subtract its multiple of
\(\kappa^n\), then argue by induction. More generally, if
\(\partial_\kappa f\in K[\kappa]\), subtract the explicit polynomial
primitive, whose coefficients are divided only by nonzero integers.
The remainder belongs to \(K\).

As \(r\ne0\), the first line of (6) proves
\(\sigma\in K[\kappa]\) with degree at most two.
Since \(\partial_\tau K\subset K\) and \(\partial_\tau\kappa=0\),
all its \(\tau\)-derivatives have the same degree bound. The second
line of (6) is equivalently
\[
\begin{gathered}
\ell_{\kappa\kappa}
 =\frac{r''}{6r^2}\sigma_\kappa
  +\frac{2r'}{3r^2}\sigma_{\tau\kappa}
  +\frac1r\sigma_{\tau\tau\kappa}\in K[\kappa]_{\le1},\\
m_\kappa=\ell_{\tau\tau}/r,\qquad
\sigma\in K[\kappa]_{\le2},\qquad
\ell\in K[\kappa]_{\le3},\qquad m\in K[\kappa]_{\le4},\\
d\in K[\kappa,y]_{\text{total degree}\le3},\qquad
w\in K[\kappa,y]_{\text{total degree}\le4}.
\end{gathered}
\tag{7}
\]
Two polynomial primitives give the bound on \(\ell\), and one then
gives the bound on \(m\). Their integration constants belong to the
exact field \(K\), even if \(L/K(\kappa)\) is a nontrivial extension.
This is a consequence of the actual differentiated elements, not
assumed existence of arbitrary algebraic antiderivatives.

The total-degree bounds in (7) follow term by term from (4)--(5).
For example \(\sigma_\kappa y^2\) has total degree at most three,
\(\sigma_{\kappa\kappa}y^4\) at most four, and
\(\ell_\tau y\) at most four. Coefficients in \(K\) have degree zero;
this is ordinary degree in the displayed polynomial variables, not
a new assertion about original invariant-field coefficients.

## 5. A monic equation over the exact one-variable field

The original-coordinate substitutions in (1) are
\[
\begin{gathered}
y=Y-\tau X,\qquad
\kappa=Z-\rho'Y+(\tau\rho'-\rho)X,\\
W=w(\kappa,y)+d(\kappa,y)X+\tfrac12\sigma(\kappa)X^2
   =G_K(X,Y,Z),\\
G_K\in K[X,Y,Z],\qquad \deg G_K\le4,\qquad
\mathcal F=W-G_K(X,Y,Z)\in K[X,Y,Z,W].
\end{gathered}
\tag{8}
\]
The first two expressions are linear in the actual goods, with
coefficients in \(K\). Equations (7) give degree at most four in
each term of the second line, including its powers of \(X\).
Thus (8) is an identity in the actual fraction field
\(\operatorname{Frac}B\).

In the formal polynomial ring over \(K\), \(\mathcal F\) is monic
linear in \(W\), hence irreducible. This conclusion has not replaced
the coefficient field by an algebraic extension or selected one
component of an older pencil.

The coefficients of \(G_K\) are so far in \(K\), not asserted to
be complex numbers. In particular (8) alone is not being called an
actual polynomial invariant, an elementary coordinate change over
\(\mathbb C\), or recognition of \(\ker E\). Those conclusions need
the separate exact-field rational-pencil descent. The result here
is the polynomial coefficient bound and monic relation that feed
that descent. The resonant branch and arbitrary coordinate entry
are outside these hypotheses.

## Sources

1. [A tangent-graph reduction for nonradial conical speeds](conical-mismatch-tangent-graph-reduction-pass136.md),
   Sections 1--4, equations (1)--(10), and Section 5 for
   \(\rho''\ne0\). This supplies the actual localized ring, finite
   coefficient field, whole generic affine line, \(y_v\in L^*\),
   and the scalar compatibility identity. The present note derives
   the new reparameterized polynomiality from those proved inputs.

[^1]: [Tangent-graph reduction136](conical-mismatch-tangent-graph-reduction-pass136.md), Sections 1--5.
