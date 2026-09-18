# A quadratic ratio excludes the constant-second projected line

Status: working actual-chart exclusion. For a quadratic polynomial
\(f(t)\) with nonzero leading coefficient, the chart \(q=f(t)/\rho\)
cannot have \(\vartheta\) constant and \(y\) affine nonconstant in the
selected line parameter. The full scalar Jacobian gives the
contradiction directly; no Wang theorem or generic coordinate descent
is used.

This note is separate from220 and221. It does not assert exclusion
of all repeated-root quartic frames.

## 1. Exact chart and hypotheses

Keep the supplied actual exact1122 and full initial-kernel hypotheses
of [general quartic220](rank-two-binary-quartic-leading-sextic-pass220-working.md).
In particular the original polynomial ring is
\(B=\mathbb C[X,Y,Z,W]=A[u]\), \(E=\partial_u\), and its actual
chart from [universal184](weight-four-universal-chart-potentials-pass184-working.md)
satisfies
\[
\begin{gathered}
Y=y+tX,\qquad Z=z+\sigma X+qX^2,\qquad
W=w+\vartheta X+\rho X^2,\\
[L:\mathbb C(t,\rho)]<\infty,\qquad
y,z,w,\vartheta,\sigma\in L[v],\qquad L[y,z,w]=L[v],\\
\det\frac{\partial(Y,Z,W)}{\partial(t,\rho,v)}
=J_0=-a^3\in L^*,\qquad a=EX.
\end{gathered}
\tag{1}
\]
The variable \(X\) is held fixed in this determinant and is
transcendental over \(L(v)\). The ratios \(t,\rho\) are algebraically
independent. Coefficient derivatives on the finite field \(L\)
are the exact extensions of \(\partial_t,\partial_\rho\).

Assume the additional conditions
\[
q=\frac{f(t)}{\rho},\qquad
f(t)=\alpha t^2+\beta t+\gamma,\quad
\alpha\in\mathbb C^*,\quad \beta,\gamma\in\mathbb C,
\qquad
\vartheta\in L,\quad \deg_vy=1.
\tag{2}
\]
There is no assumption on \(\beta^2-4\alpha\gamma\). Since \(y\)
is affine nonconstant, \(L[y]=L[v]\). It may therefore replace
\(v\) as a parameter for this calculation. This is not an original
polynomial coordinate assertion. The corresponding determinant is
\[
j=\det\frac{\partial(Y,Z,W)}{\partial(t,\rho,y)}
=J_0/y_v\in L^*.
\tag{3}
\]
Its coefficient derivatives agree with the original ones on \(L\),
but now hold \(y\), rather than \(v\), fixed.

## 2. The actual potentials determine the required shapes

For \(c\in L\) use the Taylor notation
\[
H_i(c;U,V)=
\sum_{j=0}^i\frac{c_{t^j\rho^{i-j}}}{j!(i-j)!}U^jV^{i-j}.
\tag{4}
\]
The first three universal potentials, with \(k,n,\ell\in L\), are
\[
\begin{gathered}
\sigma=q_ty+q_\rho\vartheta+k,\\
z=q_\rho w+H_2(q;y,\vartheta)+k_ty+k_\rho\vartheta+n,\\
Rw+H_3(q;y,\vartheta)+H_2(k;y,\vartheta)+H_1(n;y,\vartheta)=\ell,\\
R=q_{t\rho}y+q_{\rho\rho}\vartheta+k_\rho .
\end{gathered}
\tag{5}
\]
All coefficient derivatives in these polynomials are taken before
evaluation.

Because \(\vartheta\in L\),
\[
R=-\frac{f'(t)}{\rho^2}y+\frac{2f(t)}{\rho^3}\vartheta+k_\rho
\tag{6}
\]
has degree one in \(y\). Its leading coefficient is nonzero because
\(f'=2\alpha t+\beta\ne0\) in the exact field. The cubic coefficient
of \(H_3(q;y,\vartheta)\) is \(q_{ttt}/6=0\). Thus solving the third
potential for \(Rw\) gives a right side of degree at most two.
Since \(w\) is a polynomial in \(y\), it is affine.
The second potential and \(q_{tt}/2=\alpha/\rho\) now give
\[
\begin{gathered}
w=\lambda y+\omega,\qquad
z=\frac{\alpha}{\rho}y^2+\kappa y+\zeta,\qquad
\lambda,\omega,\kappa,\zeta\in L,\\
\kappa=k_t+q_{t\rho}\vartheta+q_\rho\lambda,\qquad
\sigma=q_ty+q_\rho\vartheta+k .
\end{gathered}
\tag{7}
\]
Zero values of \(\lambda\) are allowed. No rationality of any lower
coefficient, or constancy of \(\lambda\), has been presumed.

## 3. A two-factor form of the full Jacobian

Insert (7) into the original coordinate map, retaining every term:
\[
\begin{aligned}
Y&=y+tX,\\
Z&=\frac{\alpha}{\rho}y^2+\kappa y+\zeta
 +(q_ty+q_\rho\vartheta+k)X+qX^2,\\
W&=\lambda y+\omega+\vartheta X+\rho X^2 .
\end{aligned}
\tag{8}
\]
Set
\[
H=q_{t\rho}\vartheta+q_\rho\vartheta_t+k_t-\kappa,
\qquad \eta=\lambda-\vartheta_t .
\tag{9}
\]
These are coefficients in \(L\), independent of \(X,y\).
Expanding the determinant along the first row
\((Y_t,Y_\rho,Y_y)=(X,0,1)\) yields
\[
\begin{aligned}
j&=(Z_t-XZ_y)W_\rho+Z_\rho(XW_y-W_t)\\
&=(\kappa_t y+\zeta_t+HX)
       (\lambda_\rho y+\omega_\rho+\vartheta_\rho X+X^2)\\
&\quad+Z_\rho(\eta X-\lambda_t y-\omega_t),\\
Z_\rho&=-\frac{\alpha}{\rho^2}y^2+\kappa_\rho y+\zeta_\rho
 +(q_{t\rho}y+q_{\rho\rho}\vartheta
                     +q_\rho\vartheta_\rho+k_\rho)X+q_\rho X^2 .
\end{aligned}
\tag{10}
\]
The equality \(q_{tt}=2\alpha/\rho\) is exactly what cancels
the term linear in \(yX\) from \(Z_t-XZ_y\).

For clarity, the following are coefficients of the full polynomial
on the right of (10), before imposing any coefficient equation.
Notation \([X^iy^j]\) extracts both exponents at once.
\[
\begin{array}{c|l}
\text{monomial}&\text{coefficient}\\ \hline
y^3&\alpha\lambda_t/\rho^2\\
Xy^2&-\alpha\eta/\rho^2-q_{t\rho}\lambda_t\\
X^2y&\kappa_t-q_\rho\lambda_t+q_{t\rho}\eta\\
y^2&\kappa_t\lambda_\rho-\kappa_\rho\lambda_t+
                                  \alpha\omega_t/\rho^2\\
X^3&H+q_\rho\eta\\
X^2&\zeta_t+H\vartheta_\rho-q_\rho\omega_t+
 (q_{\rho\rho}\vartheta+q_\rho\vartheta_\rho+k_\rho)\eta .
\end{array}
\tag{11}
\]
Each coefficient must vanish because (3) is a scalar in \(L^*\).
Reading the six rows successively, using \(\alpha\ne0\), gives
\[
\lambda_t=0,\qquad
\eta=0,\qquad
\kappa_t=0,\qquad
\omega_t=0,\qquad
H=0,\qquad
\zeta_t=0.
\tag{12}
\]
After these substitutions both factors
\(\kappa_t y+\zeta_t+HX\) and
\(\eta X-\lambda_t y-\omega_t\) in (10) vanish.
Therefore \(j=0\), contradicting (3).

Equivalently, after the first five gates the entire determinant
already has the transparent form
\[
j=\zeta_t\bigl(X^2+\vartheta_\rho X+
                        \lambda_\rho y+\omega_\rho\bigr).
\tag{13}
\]
Its coefficient of \(X^2\) forces \(\zeta_t=0\), while the actual
calibration requires a nonzero determinant. This comparison does not
divide by \(\lambda\), \(\lambda_\rho\), \(\omega_\rho\), or any
projected polynomial.

## 4. Bounded consequences

We have proved that the actual hypotheses (1)--(2) are inconsistent.
In particular this directly excludes the constant-second line for
the mixed specialization \(q=t^2/\rho\). The earlier217 and220
arguments and their saved sources are unchanged.

There is also an immediate use for the root partition \(2+1+1\).
Choose the pair consisting of the two copies of the repeated root.
Its sextic factor has multiplicity one, so if it is the selected
pure leading factor, the theorem220 forces a plane line.
Use an actual constant \(\operatorname{GL}_2(\mathbb C)\) change
whose first good coordinate is this repeated root form.
The normalized binary quartic is
\[
F_4(X,Y)=X^2(\alpha Y^2+\beta XY+\gamma X^2),\qquad
\alpha\ne0,\qquad \beta^2-4\alpha\gamma\ne0.
\tag{14}
\]
For completeness, if the chosen first root form is
\(l(X,Y)=a_1X+b_1Y\), put \(l(t)=a_1+b_1t\).
The actual projection formula in Section2 of
[squarefree line221](rank-two-squarefree-quartic-line-exclusion-pass221-working.md)
gives
\(\vartheta_*=\vartheta/l-2\rho b_1y/l^2\).
The old repeated-pair factor is
\(l^2\vartheta-2\rho l b_1y=l^3\vartheta_*\).
Thus its affine line relation becomes \(\vartheta_*\in L\).
The invertible projected linear transformation preserves the
whole line, so \(y_*\) is affine nonconstant. The unchanged
quadratic pivot, preserved exact degrees, and transformed full
initial ideal provide precisely (1)--(2). This particular selected
pair is consequently excluded by (10)--(12).

The other selected pair types in partition \(2+1+1\), including
their possible conic components, are not handled here.
No conclusion about arbitrary initial-frame entry or unrestricted
complex-threefold cancellation is asserted.

The full universal potentials and retained sources were read before
use. Fresh unsaved algebra independently verified all six raw
coefficients in (11), the two-factor identity (10), and the collapsed
identity (13). No saved checker was executed, imported or compiled.
No earlier proof, checker, index or packet was edited.
The written proof is not human expert review or proof-assistant
certification, and no historical novelty claim is made.
