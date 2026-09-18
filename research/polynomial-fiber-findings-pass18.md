# Replacing a pure power by a monic polynomial

This is an exact algebraic exploration, not a rank-three classification or
an assertion of novelty. The physical identities were first checked in
the eight requested cases, then reconstructed symbolically below. The
initial six-method checker passed in 4.040 seconds. The current
[standalone checker](polynomial_fiber_checks_pass18.py) has eight methods,
including actual forward and inverse finite-jet tests. Its complete
regression execution is recorded in
[verification-pass-18.json](../verification-pass-18.json). It imports
no solver or other research checker.

This exploration's original scope is preserved below. The subsequent
[complete polynomial-curve proof](polynomial-curve-lift-pass18.md)
also establishes universal primitivity, the exact plinth and rank three
when \(P(x,0)\) is nonconstant, and constructs coordinates for the
specified invariant slice extensions. Those statements rest on that
written proof, not on the physical parameter grid.

## 1. General identities

Let \(F(y)\in\mathbb C[y]\) be monic of degree \(d\ge2\), let
\(n\ge1\), and put
\[
G(R,S)=S^dF(R/S),\qquad f=xz-F(y),\qquad
r=xP(x,f)+yf^n.
\]
The homogeneous expression \(G\) is polynomial. Define
\[
T_F(x,y,P,f)=\sum_{k=1}^d\frac{F^{(k)}(y)}{k!}
 x^{k-1}P^k f^{n(d-k)},\qquad
h=T_F(x,y,P,f)+zf^{nd}.
\tag{1}
\]
Taylor's polynomial identity gives
\[
xh=G(r,f^n)+f^{nd+1}.
\tag{2}
\]
Thus this \(h\) is exactly the quotient in the proposed definition,
and is polynomial before any localization.

Let \(\delta=-\operatorname{Jac}(f,h,\cdot)\). Direct differentiation
and (2) give
\[
\delta f=\delta h=0,\qquad
\delta r=f^nh,\qquad
\delta x=f^nG_R(r,f^n),
\tag{3}
\]
and
\[
\delta y=h-(P+xP_x)G_R(r,f^n).
\tag{4}
\]
Here \(P_x\) means differentiation with \(f\) held fixed. For an
independent derivation of the sign in (3), the derivation
\(x\partial_y+F'(y)\partial_z\) kills \(f\) and sends \(r\) to
\(xf^n\). Consequently \(\operatorname{Jac}(f,x,r)=xf^n\).
Taking \(\operatorname{Jac}(f,\cdot,r)\) in (2) then gives
\(x\operatorname{Jac}(f,h,r)=-hxf^n\), as required.

For the two requested polynomials, (3) reads
\[
\begin{array}{c|c|c}
F(y)&G(r,f^n)&\delta x\\ \hline
y^2+y+1&r^2+rf^n+f^{2n}&2f^nr+f^{2n}\\
y^3-y&r^3-rf^{2n}&3f^nr^2-f^{3n}
\end{array}
\]
The extra coefficients change lower powers of \(r\), not the leading
degree \(d-1\) of \(G_R\).

## 2. Local nilpotence is proved, not just suggested by the examples

Write \(R_0=\mathbb C[x,y,z]\) and \(A=\mathbb C[f,f^{-1},h]\).
There is an exact presentation
\[
(R_0)_f\cong
A[x,r]/\bigl(xh-G(r,f^n)-f^{nd+1}\bigr).
\tag{5}
\]
The polynomial inverse reconstructs
\[
y=(r-xP(x,f))/f^n,\qquad
z=\bigl(h-T_F(x,y,P(x,f),f)\bigr)/f^{nd}.
\]
These are valid over \(A\). Taylor's identity verifies
\(xz-F(y)=f\), and the remaining inverse identities follow from the
definitions. No division by \(x\) is used in this verification.

On the generators of (5), \(\delta\) kills \(f^{\pm1},h\), sends
\(r\) to \(f^nh\), and sends \(x\) to a polynomial of degree
\(d-1\) in \(r\) with invariant coefficients. Hence
\(\delta^2r=0\) and \(\delta^{d+1}x=0\). The derivation is locally
nilpotent on the localized ring and therefore on its stable subring
\(R_0\). The lower coefficients of \(F\) introduce no obstruction to
this argument.

## 3. Exact kernel calculation

Because the defining relation in (5) is monic of degree \(d\) in
\(r\), the monomials
\[
x^a r^i,\qquad a\ge0,\quad 0\le i<d,
\]
form an \(A\)-basis. After additionally inverting \(h\), one has
\[
x=\frac{G(r,f^n)+f^{nd+1}}{h},\qquad
\delta=f^nh\,\partial_r.
\]
The displayed basis monomial has \(r\)-degree \(da+i\) and leading
coefficient \(h^{-a}\). All these degrees are distinct. Thus a
nonconstant linear combination cannot lose its top derivative degree,
and
\[
\ker\bigl(\delta|(R_0)_f\bigr)=\mathbb C[f,f^{-1},h].
\tag{6}
\]

Assume now \(P(x,0)\ne0\), as in every requested example. Formula (1)
gives
\[
h\equiv x^{d-1}P(x,0)^d\pmod f.
\tag{7}
\]
This is a nonconstant polynomial in \(x\). The ring
\(R_0/(f)=\mathbb C[x,y,z]/(xz-F(y))\) is a domain and contains
\(\mathbb C[x]\) injectively. Indeed, the relation is primitive and
linear in \(z\), and localization at \(x\) identifies the quotient
with a subring of \(\mathbb C[x,x^{-1},y]\).

If an invariant required a positive minimal power of \(f\) in its
denominator in (6), reducing its numerator modulo \(f\) would give a
polynomial relation over \(\mathbb C\) for the nonconstant expression
in (7). That relation is zero only when the numerator was already
divisible by \(f\) in \(\mathbb C[f,h]\), contradicting minimality.
Consequently
\[
\ker\delta=\mathbb C[f,h].
\tag{8}
\]
This proves the proposed kernel statement under the stated nonzero
residue hypothesis. It does not identify the exact plinth ideal or
establish the rank of \(\delta\).

## 4. Exact lower-coefficient coordinate identities

For arbitrary symbols \(a,b\), the polynomial
\[
\mathcal D_G(a,b,S)=
\sum_{k=1}^d c_k S^{d-k}
 \sum_{j=0}^{k-1}a^{k-1-j}b^j,
\qquad F(y)=\sum_{k=0}^dc_ky^k,
\]
satisfies
\((a-b)\mathcal D_G(a,b,S)=G(a,S)-G(b,S)\).
Thus the proposed inverse formula
\[
x=X+W\mathcal D_G(r,\rho,f^n),\qquad hW=r-\rho,
\]
satisfies
\(hx-G(r,f^n)=hX-G(\rho,f^n)\). This identity retains all lower
coefficients of \(F\), not only its leading monomial.

Likewise, if \(\rho=XH+Yf^n\), then polynomial Taylor expansion gives
\[
G(\rho,f^n)-XT_F(X,Y,H,f)=f^{nd}F(Y).
\]
Combining this with \(Xh=G(\rho,f^n)+f^{nd+1}\) gives exactly
\[
X\bigl(h-T_F(X,Y,H,f)\bigr)=f^{nd}\bigl(F(Y)+f\bigr).
\tag{9}
\]
Thus the proposed new coordinate relation is \(f=XZ-F(Y)\).
The checker tests (9), the reconstructed relation, and both divided
difference directions for each requested \(F\) and \(n=1,2,3\).
It also checks the congruences for \(X\) modulo \(f^n\) without
canceling \(h\) in that nonreduced quotient. Full coordinate
generation requires the separate finite-jet and inverse arguments.

## 5. Bounded physical results and limits

For each row below, both \(n=1\) and \(n=2\) were checked with exact
rational polynomial arithmetic. Every physical Jacobian identity, chart
inverse, and coefficient-gcd test passed.

| \(F(y)\) | \(P(x,f)\) | \(\delta\)-degrees of \((x,y,z)\) | Coefficient gcd |
|---|---|---|---|
| \(y^2+y+1\) | \(x\) | \((2,4,6)\) | \(1\) |
| \(y^2+y+1\) | \(x^2+f+1\) | \((2,6,10)\) | \(1\) |
| \(y^3-y\) | \(x\) | \((3,6,15)\) | \(1\) |
| \(y^3-y\) | \(x^2+f+1\) | \((3,9,24)\) | \(1\) |

The gcd calculation proves primitivity for these eight derivations only.
No exact plinth-generator, universal primitivity, rank-three, novelty,
or cancellation conclusion is inferred from it. The independent command is

```sh
/opt/anaconda3/bin/python research/polynomial_fiber_checks_pass18.py
```

The initial finite run passed six methods in 4.040 seconds. Two later
methods test the actual finite-jet numerators in both directions for
three monic polynomials, two choices of \(P\), and \(n=1,2,3\),
including a deliberately uncorrected negative control. The general
statements in Sections 1-3 are separate elementary proofs; they are not
consequences of a finite parameter grid or proof-assistant certificates.
