# The constant-return projected line is impossible

Status: bounded working exclusion for the supplied full initial kernel
\(Z^2-XYW\). In the nonzero-return line with
\(\rho y-t\vartheta\in L\), one exact Jacobian coefficient removes
the apparent quadratic auxiliary terms. The resulting actual nice
derivation has an impossible fixed-linear-form identity.

The proof changes parameters only in the exact coefficient field.
It does not regard those parameters or their linear combinations
as original polynomial coordinates. The remaining conic from227
is outside this note.

## 1. Actual input and the specified line

Assume the actual globally sliced frame
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\\
\deg_E(X,Y,Z,W)=(1,1,2,2),\\
a=EX,\quad b=EY,\quad e=E^2Z/2,\quad h=E^2W/2,\\
\ker\bigl((\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
\longmapsto(aT,bT,eT^2,hT^2)\bigr)
=(\mathsf Z^2-\mathsf X\mathsf Y\mathsf W).
\end{gathered}
\tag{1}
\]
Here \(T\) is independent, the ideal is the entire initial kernel,
and the four capital letters are original polynomial coordinates.

The literal \(Z\) pivot and
[universal184](weight-four-universal-chart-potentials-pass184-working.md),
as rebuilt in
[sextic227](rank-one-product-radical-sextic-pruning-pass227-working.md),
give
\[
\begin{gathered}
N=[u^3](\partial_Z|_A)\ne0,\qquad
L=\operatorname{Frac}(\ker_A N),\qquad A_L=L[v],\quad Nv=1,\\
t=b/a,\quad \rho=h/a^2,\quad q=e/a^2,\quad q^2=t\rho,
\qquad [L:\mathbb C(t,\rho)]<\infty,\\
Y=y+tX,\quad Z=z+\sigma X+qX^2,\quad
W=w+\vartheta X+\rho X^2,\\
y,z,w,\sigma,\vartheta\in L[v],\qquad L[y,z,w]=L[v],\qquad
J_{(t,\rho,v)}(Y,Z,W)=-a^3\in L^* .
\end{gathered}
\tag{2}
\]
The determinant holds \(X\) fixed and is independent of \(X,v\).
The ratios \(t,\rho\) are algebraically independent, and their
coefficient partials extend uniquely to \(L\).

Consider exactly the second line row in227:
\[
\deg_vy=\deg_v\vartheta=1,\qquad
\xi:=\rho y-t\vartheta\in L,\qquad
R=\frac{\xi}{4q\rho}+k_\rho\in L^*.
\tag{3}
\]
The subscript on \(k_\rho\) here is the original coefficient
partial at fixed \(t\). No condition that \(R\) be a complex
constant is imposed.

## 2. Exact field parameters and the lower potentials

Set
\[
s=q/t,\qquad \rho=s^2t,\qquad q=st,\qquad
c=-\xi/t,\qquad \vartheta=s^2y+c.
\tag{4}
\]
The elements \(t,s\) are algebraically independent and
\([L:\mathbb C(t,s)]<\infty\). Indeed \(L\) contains
\(\mathbb C(t,\rho,q)=\mathbb C(t,s)\), which is a degree-two
extension of \(\mathbb C(t,\rho)\).

From now on, a dot means the coefficient partial in \(t\) with
\(s\) fixed, and a subscript \(s\) means the coefficient partial
in \(s\) with \(t\) fixed. On the exact field these are
\[
\dot{\ }=\partial_t+\frac{\rho}{t}\partial_\rho,\qquad
\partial_s=2st\,\partial_\rho .
\tag{5}
\]
They extend uniquely to \(L\), commute, and hold the chosen
line parameter fixed when acting on its coefficient ring.
This is not a change of the original coordinates.

The universal second and third leading polynomials are
\[
H_2(q;U,V)=-\frac{(\rho U-tV)^2}{8q^3},\qquad
H_3(q;U,V)=
\frac{(\rho U-tV)^2(\rho U+tV)}{16q^5}.
\tag{6}
\]
On \(U=y,V=s^2y+c\), the first is constant in \(y\), and the
second has degree at most one in \(y\).
The third potential
\[
Rw=\ell-\{H_3(q)+H_2(k)+H_1(n)\}(y,\vartheta)
\]
therefore has right side of degree at most two in \(y\).
Because \(y\) is affine nonconstant in \(v\),
\(L[y]=L[v]\); because \(R\in L^*\), this proves
\[
w=A_2y^2+\lambda y+\omega,\qquad A_2,\lambda,\omega\in L.
\tag{7}
\]
The notation \(A_2\) is a coefficient, not the invariant ring \(A\).

The first and second potentials become exactly
\[
\sigma=sy+\frac{c}{2s}+k,\qquad
z=\frac{w}{2s}+\dot k\,y+f_0,\qquad
f_0=n+\frac{c\,k_s}{2st}-\frac{c^2}{8s^3t}\in L.
\tag{8}
\]
For the coefficient of \(y\), the original combination
\(k_t+(\rho/t)k_\rho\) is \(\dot k\), not the old partial
\(k_t\) at fixed \(\rho\). This distinction is essential.
No equation for the remaining lower potentials is discarded or
replaced by rationality of \(L\).

## 3. A literal Jacobian coefficient forces \(A_2=0\)

The actual map now has the form
\[
\begin{aligned}
Y&=y+tX,\\
W&=w+(s^2y+c)X+s^2tX^2,\\
Z&=\frac{w}{2s}+\dot k\,y+f_0+
                  \left(sy+\frac{c}{2s}+k\right)X+stX^2 .
\end{aligned}
\tag{9}
\]
Replace the line parameter \(v\) by the affine parameter \(y\)
only when computing the determinant. The chain rule gives
\[
J:=J_{(t,s,y)}(Y,Z,W)
=-\frac{2st\,a^3}{y_v}\in L^*,
\tag{10}
\]
since \(\partial\rho/\partial s=2st\) and \(y_v\in L^*\).
The coefficient dependence of \(y=y_1v+y_0\) causes no omitted
terms: the triangular determinant of this parameter change is
exactly \(2st/y_v\). In particular \(J\) is independent of both
the actual coordinate \(X\) and the affine parameter \(y\).

Here is a complete coefficient calculation from (9).
While differentiating, \(X\) is fixed. Put
\[
\mathcal T=\partial_t-X\partial_y,\qquad
U_0=Z-\frac{W}{2s}
    =\dot k\,y+f_0+kX+\frac{s}{2}XY .
\tag{11}
\]
The operator \(\partial_t\) in (11) is at fixed \(s,y\).
Eliminating the \(t\)-entry in the first Jacobian row gives
\[
J=(\mathcal T U_0)W_s
           -\left((U_0)_s-\frac{W}{2s^2}\right)\mathcal TW .
\tag{12}
\]
The derivative of \(1/(2s)\) is retained in the second bracket.
Using (7) and (9), the four required expressions are
\[
\begin{aligned}
\mathcal T U_0&=\ddot k\,y+\dot f_0,\\
W_s&=(A_2)_s y^2+\lambda_s y+\omega_s
                         +(2sy+c_s)X+2stX^2,\\
\mathcal TW&=\dot A_2 y^2+\dot\lambda y+\dot\omega
                         +(\dot c-\lambda-2A_2y)X,\\
(U_0)_s-\frac{W}{2s^2}
&=-\frac{A_2}{2s^2}y^2+
       \left((\dot k)_s-\frac{\lambda}{2s^2}\right)y
       +(f_0)_s-\frac{\omega}{2s^2}
       +\left(k_s-\frac{c}{2s^2}\right)X .
\end{aligned}
\tag{13}
\]
The first product in (12) has \(X\)-coefficient of \(y\)-degree
at most two. In the second product, the only contribution to
\(Xy^3\) multiplies \(-A_2y^2/(2s^2)\) by \(-2A_2yX\).
The minus sign in (12) consequently gives
\[
[Xy^3]J=-\frac{A_2^2}{s^2}.
\tag{14}
\]
Equation (10) forces \(A_2=0\). In particular (8) gives
\[
w=\lambda y+\omega,\qquad
z=\kappa y+\zeta,\qquad
\kappa=\dot k+\frac{\lambda}{2s},\quad
\zeta=f_0+\frac{\omega}{2s}.
\tag{15}
\]
The conclusion uses the full calibrated determinant, not just
the polynomial degree bounds on \(w,z\).

## 4. The auxiliary derivation is actual and nice

Extend \(N\) to \(B=A[u]\) by \(Nu=0\), and define
\(\mathcal P=aN-(NX)E\). This is an original polynomial derivation.
It fixes \(X\), kills \(L\), and on \(A\) equals \(aN\).
On \(B_a=A_a[X]\) it therefore fixes \(X\) and is locally
nilpotent, since \(Na=0\). Its restriction to \(B\) is locally
nilpotent as well. This argument does not presume \(NX=0\).

Put \(\tau=aNy\in L^*\). Equations (9),(15) give the exact row
\[
\mathcal PX=0,\qquad
\mathcal PY=\tau,\qquad
\mathcal PZ=\tau(sX+\kappa),\qquad
\mathcal PW=\tau(s^2X+\lambda).
\tag{16}
\]
The displayed products are original polynomials because
\(\mathcal P\) was constructed on \(B\). Their field factors
are not separately declared regular. As \(\mathcal P\) fixes
\(L\) and \(X\), it squares to zero on all four original
coordinates.

Localizing the original fixed coordinate \(X\) at the nonzero
elements of \(\mathbb C[X]\) gives a nonzero nice derivation of
\(\mathbb C(X)[Y,Z,W]\). Theorem3.1(i) in
[Dasgupta--Gupta, *Nice derivations over principal ideal domains*](https://arxiv.org/html/1701.03635v1)
states that such a derivation fixes a nonzero linear form in
the three polynomial variables over the coefficient field.
This part of the theorem does not require primitive division.
Only its fixed-linear-form conclusion is used.

Clear the \(X\)-denominators of that form. Equation (16), divided
by the nonzero \(\tau\) in the fraction field, gives
\[
l(X)+m(X)(sX+\kappa)+n(X)(s^2X+\lambda)=0,
\qquad l,m,n\in\mathbb C[X],
\tag{17}
\]
with the three polynomials not all zero.
Let \(d=\max(\deg l,\deg m+1,\deg n+1)\), assigning zero
polynomials degree \(-\infty\). The terms \(m\kappa+n\lambda\)
have \(X\)-degree at most \(d-1\). The coefficient of \(X^d\)
in (17) is thus a nonzero complex polynomial of degree at most
two in \(s\). This is impossible, because
\(s^2=\rho/t\) and the algebraic independence of \(t,\rho\)
make \(s\) transcendental over \(\mathbb C\).
Therefore the line (3) cannot occur.

## 5. Scope and verification

The nonzero-return condition in (3) is used to bound the degree
of \(w\) in (7). This is a different argument from the separately
saved [zero-return229](rank-one-product-radical-zero-return-exclusion-pass229-working.md),
which was independently read in full but is not an input here.
The constant-first line is separately excluded in
[228](rank-one-product-radical-constant-first-line-exclusion-pass228-working.md).
The conic left by227 requires a separate argument.

The exact field change (4)--(5) and the parameter replacement
in (10) are never promoted to polynomial automorphisms of \(B\).
The original selected partial, derivation \(N\), and field \(L\)
are unchanged. There is no assertion that \(a\) is an original
unit, that a hypothetical frame is globally minimal, or that
an arbitrary sliced action enters this supplied profile.

The original universal potentials were freshly read. New unsaved
symbolic arithmetic independently expanded the raw map (9) with
all six coefficient functions in (7),(8) arbitrary, and verified
the exact coefficient (14). A separate AI reconstruction obtained
the same coefficient and checked the chain-rule calibration.
The exact nice-field theorem was freshly read in the primary
Dasgupta--Gupta restatement; this is not a claim of having read
Wang's original article.

No saved checker was executed, imported, or compiled. No previous
source, index, JSON, or packet was changed. This is working
mathematics, not human expert review, proof-assistant certification,
historical novelty clearance, or unrestricted cancellation.
