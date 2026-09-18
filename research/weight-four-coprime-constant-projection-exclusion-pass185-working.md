# The coprime quadratic-pair quartic cannot have constant projected y

**Status: working exclusion under the actual full initial-kernel hypothesis.**

For the supplied initial relation
\(X^2Z+Y^2W\), the projected \(y\) cannot belong to the selected
coefficient field \(L\). The obstruction is a polynomial identity
forced by the actual constant determinant. Its leading coefficient
cannot vanish. No ambient invariant coordinate, external
three-variable classification, or rationality of \(L\) is used.

## 1. Actual hypotheses and change to a projected parameter

Retain the full actual setup of
[universal-chart184](weight-four-universal-chart-potentials-pass184-working.md):
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad
\deg_E(X,Y,Z,W)=(1,1,2,2),\\
\ker\theta_0=(\mathsf X^2\mathsf Z+\mathsf Y^2\mathsf W),\quad
a=EX\ne0,\quad N=[u^3](\partial_Z|_A)\ne0,\\
L=\operatorname{Frac}(\ker_A N),\quad A_L=L[v],\quad Nv=1,\quad
t=EY/a,\quad \rho=(E^2W/2)/a^2,\quad q=-t^2\rho .
\end{gathered}
\tag{1}
\]
The ideal is the full weighted initial kernel, not one relation.
The independent ratios \(t,\rho\) make \(L/\mathbb C(t,\rho)\)
finite separable. Initial coefficient partials fix \(v\).
The actual chart and its first coefficient identities are
\[
\begin{gathered}
Y=y+tX,\quad Z=z+\sigma X-t^2\rho X^2,\quad
W=w+\vartheta X+\rho X^2,\\
\sigma=-2t\rho y-t^2\vartheta+k,\\
z=-t^2w-\rho y^2+k_t^{\rm old}y+
                  (k_\rho^{\rm old}-2ty)\vartheta+n,\qquad k,n\in L,\\
L[y,z,w]=L[v],\qquad
\det\frac{\partial(Y,Z,W)}{\partial(t,\rho,v)}
     =-a^3\in L^* .
\end{gathered}
\tag{2}
\]
The determinant holds \(X\) fixed.

Assume \(y\in L\). Its old \(\rho\)-derivative is nonzero:
otherwise the first row of the determinant in (2) is
\((X+y_t^{\rm old},0,0)\), which would give a positive-degree
factor of a nonzero constant polynomial in \(X\).
It follows that \(t,y\) are algebraically independent and
\(L/\mathbb C(t,y)\) is finite separable.

The denominator exclusion184 gives
\[
R=k_\rho^{\rm old}-2ty\in L^* .
\tag{3}
\]
The first potential has the form
\(Rw+g_3(y,\vartheta)=\ell\), where
\(g_3(U,V)=-U^2V+H_2(k;U,V)+H_1(n;U,V)\).
For fixed \(y\in L\), it is quadratic in \(\vartheta\).
Therefore \(w\in L[\vartheta]\) has degree at most two,
and the formula for \(z\) in (2) puts it in the same ring.
Since \(L[y,z,w]=L[v]\), we obtain
\[
L[\vartheta]=L[v],\qquad
w=\alpha\vartheta^2+\beta\vartheta+g,\quad
\alpha,\beta,g\in L,\qquad \vartheta_v\in L^* .
\tag{4}
\]
This step does not require the later whole-plane theorem.

Use the commuting coefficient partials \(t,y\) on the finite
separable extension \(L/\mathbb C(t,y)\), extending them to
fix \(X,\vartheta\). From now on a subscript \(t\) or \(y\)
means these new partials. The parameter-change determinant is
\[
\det\frac{\partial(t,y,\vartheta)}{\partial(t,\rho,v)}
=y_\rho^{\rm old}\vartheta_v\in L^* .
\tag{5}
\]
Thus the new determinant is a nonzero element of \(L\),
independent of \(X,\vartheta\). It is not necessarily an
original-ring unit.

## 2. The exact literal determinant

Define the following coefficients in \(L\), retaining the
superscripts in their definitions only:
\[
A_0=-\rho y^2+k_t^{\rm old}y+n,\qquad
K_0=k-2t\rho y .
\tag{6}
\]
The identities in (2) yield
\[
Z+t^2W=R\vartheta+A_0+K_0X .
\tag{7}
\]
In the determinant, add \(t^2\) times the last row to the
middle row. The term \(-2tW\,dt\) in
\(dZ+t^2dW=d(Z+t^2W)-2tW\,dt\) must be retained.
The resulting matrix is
\[
\begin{pmatrix}
X&1&0\\
R_t\vartheta+(A_0)_t-2tw+
   ((K_0)_t-2t\vartheta)X-2t\rho X^2&
R_y\vartheta+(A_0)_y+(K_0)_yX&R\\
w_t+\rho_tX^2&w_y+\rho_yX^2&w_\vartheta+X
\end{pmatrix}.
\tag{8}
\]
Its determinant expands to
\[
\begin{aligned}
\mathcal J(X,\vartheta)
={}&(w_\vartheta+X)
\bigl\{2tw-R_t\vartheta-(A_0)_t\\
&\qquad+X[(R_y+2t)\vartheta+(A_0)_y-(K_0)_t]
       +X^2[(K_0)_y+2t\rho]\bigr\}\\
&+R(w_t-Xw_y+\rho_tX^2-\rho_yX^3)\in L^* .
\end{aligned}
\tag{9}
\]
This identity is in \(L[X,\vartheta]\), not just at a point
of the generic curve.

The coefficient of \(\vartheta^3\) at \(X=0\), using (4),
is \(4t\alpha^2\). The transcendental \(t\) is nonzero, so
\(\alpha=0\).
The coefficients of \(X^2\vartheta\), \(X\vartheta\), and
\(\vartheta\) at \(X=0\) now give, successively,
\[
R_y=-2t,\qquad
R\beta_y=2t\beta-R_t,\qquad
\beta(2t\beta-R_t)+R\beta_t=0 .
\tag{10}
\]
Since \(R\ne0\), the last two yield
\[
\beta_t+\beta\beta_y=0 .
\tag{11}
\]

## 3. The forced rational expression has an impossible leading term

Put \(K=\ker_L\partial_y\). It is stable under \(\partial_t\)
because the partials commute. The first identity of (10)
gives
\[
R=r-2ty,\qquad r\in K .
\tag{12}
\]
Primes now mean \(\partial_t\) on \(K\). In particular
\(R_t=r'-2y\).
The second identity of (10) can be rewritten
\[
\partial_y(R\beta)=-R_t=-r'+2y .
\tag{13}
\]
Subtracting the explicit primitive \(-r'y+y^2\) gives
\[
R\beta=-r'y+y^2+d,\qquad d\in K .
\tag{14}
\]
No assumption about arbitrary primitives in \(K\) has been made.
Substitute \(y=(r-R)/(2t)\). For
\[
B_0=\frac{r'}{2t}-\frac{r}{2t^2}\in K,\qquad
e_0=d-\frac{r'r}{2t}+\frac{r^2}{4t^2}\in K ,
\]
equation (14) is exactly
\[
\beta=\frac{R}{4t^2}+B_0+\frac{e_0}{R},\qquad
R_t=2tB_0+\frac Rt,\qquad R_y=-2t .
\tag{15}
\]
All inversions here are of nonzero elements of the field \(L\);
none is presented as an original-ring polynomial inverse.

Differentiate (15) at fixed \(y\) and at fixed \(t\), respectively.
The two expressions are
\[
\begin{aligned}
\beta_t&=-\frac{R}{4t^3}+\frac{B_0}{2t}+B_0'
 +\frac{e_0'}R-\frac{2tB_0e_0}{R^2}-\frac{e_0}{tR},\\
\beta\beta_y&=-\frac{R}{8t^3}-\frac{B_0}{2t}
 +\frac{2tB_0e_0}{R^2}+\frac{2te_0^2}{R^3}.
\end{aligned}
\tag{16}
\]
Substituting in (11) and multiplying by \(R^3\) gives
\[
-\frac{3}{8t^3}R^4+B_0'R^3+
       (e_0'-e_0/t)R^2+2te_0^2=0 .
\tag{17}
\]

But \(R\) is transcendental over \(K\). Otherwise differentiating
its separable minimal polynomial over \(K\) in the \(y\) direction
would force \(R_y=0\), contrary to (15). Every coefficient in
(17) is in \(K\), and its leading coefficient
\(-3/(8t^3)\) is nonzero in characteristic zero.
This contradiction excludes \(y\in L\).

## 4. Scope

The proof uses the actual inverse's determinant, the first
potential, and the nonzero-denominator lemma. It does not
assume the whole-plane completion, affine nonconstant projection,
or any graph-degree classification. It is therefore independent
of those subsequent exclusions.

This note alone does not exclude every projected \(y\) or the
entire quartic configuration. Combining it with other branch
arguments requires their own exact hypotheses and verification.
It does not address the common-factor quartic, the other
weight-four normal forms, height-two initial kernels, entry
into a chosen time profile, or unrestricted cancellation.

The determinant computation and rational-expression contradiction
are written proofs. Finite symbolic controls can check their
identities but not supply the actual inverse, the field extension,
or the universal conclusion. No historical novelty clearance,
human expert certification, formal verification, submission or
external contact is asserted. All183 and earlier artifacts remain
unchanged.
