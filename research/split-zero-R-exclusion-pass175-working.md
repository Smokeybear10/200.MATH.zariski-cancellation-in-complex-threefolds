# The split chart cannot have identically zero projection denominator

**Status: working algebraic exclusion under the actual chart175 hypotheses.**

In the actual split-cubic chart, the polynomial
\(R=k_\rho-y\in L[v]\) is not identically zero. The proof uses
the original calibrated Jacobian and the whole generic line. It
does not assume that a nonzero \(R\) is a unit, and does not
exclude zeros of \(R\) on that line.

## 1. Actual hypotheses and the denominator-free input

Retain the complete hypotheses of
[the split-cubic chart175](split-cubic-generic-chart-pass175-working.md):
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\\
(\deg_E X,\deg_E Y,\deg_E Z,\deg_E W)=(1,1,2,2),\\
\ker\theta_0=(\mathsf X\mathsf Z+\mathsf Y\mathsf W),\qquad
a=EX\ne0,\qquad N=[u^3](\partial_Z|_A)\ne0,\\
L=\operatorname{Frac}(\ker_A N),\qquad A_L=L[v],\qquad Nv=1.
\end{gathered}
\tag{1}
\]
The formal weights are \((1,1,2,2)\), and the displayed ideal
is the full initial kernel. The original partial holds \(X,Y,W\)
fixed. Put \(t=EY/a\) and \(\rho=(E^2W/2)/a^2\). These
ratios are independent, and \(L/\mathbb C(t,\rho)\) is finite
separable. Their partials extend to \(L[v]\) fixing \(v\).

The actual inverse and the first two coefficient identities give
\[
\begin{gathered}
Y=y+tX,\qquad Z=z+\sigma X-t\rho X^2,\qquad
W=w+\vartheta X+\rho X^2,\\
y,z,w,\sigma,\vartheta\in L[v],\qquad
L[y,z,w]=L[v],\\
\sigma=-t\vartheta-\rho y+k,\qquad
z+tw=k_t y+(k_\rho-y)\vartheta+n,\qquad k,n\in L,\\
J(X):=\det\frac{\partial(Y,Z,W)}{\partial(t,\rho,v)}
=-a^3\in L^* .
\end{gathered}
\tag{2}
\]
Here \(X\) is held fixed in the determinant. All identities
in (2) were proved without dividing by \(k_\rho-y\). In
particular they remain available in the branch considered below.
The scalar calibration in (2) is an actual-chart conclusion,
not a condition imposed on arbitrary formal coefficient data.

## 2. A constant projected y has a nonzero rho derivative

We first record a consequence of (2) whenever \(y\in L\):
\[
y_\rho\ne0.
\tag{3}
\]
Indeed \(y_v=0\). If also \(y_\rho=0\), the first row of
the determinant in (2) would be \((X+y_t,0,0)\).
Its determinant would be a multiple of the monic positive-degree
polynomial \(X+y_t\) in the domain \(L[v][X]\). It could
not equal the nonzero scalar \(-a^3\).
This argument does not divide by any derivative of a projected
coordinate.

## 3. The zero-R branch contradicts the constant determinant

Suppose for contradiction that \(R=k_\rho-y=0\) in \(L[v]\).
Then
\[
y=k_\rho\in L,\qquad
A_0:=k_t y+n\in L,\qquad z=A_0-tw .
\tag{4}
\]
By (3), \(y_\rho\ne0\). The polynomial \(w\in L[v]\)
is nonconstant: otherwise (4) and \(y\in L\) would make
\(L[y,z,w]=L\), contrary to the whole-line equality in (2).
In fact that equality gives \(L[w]=L[v]\), so \(w\) is
affine in \(v\) with nonzero slope. The following degree
argument needs only its positive degree.

Evaluate the actual determinant at \(X=0\). Its rows are
the coefficient derivatives of \(y,z,w\). Add \(t\) times
its last row to its middle row. Equation (4) makes the latter
row \((A_{0,t}-w,A_{0,\rho},0)\), not
\((A_{0,t},A_{0,\rho},0)\): differentiating \(-tw\)
contributes the essential term \(-w\). Consequently
\[
\begin{aligned}
J(0)
&=\det
\begin{pmatrix}
y_t&y_\rho&0\\
A_{0,t}-w&A_{0,\rho}&0\\
w_t&w_\rho&w_v
\end{pmatrix}\\
&=w_v\bigl(y_tA_{0,\rho}-y_\rho A_{0,t}+y_\rho w\bigr).
\end{aligned}
\tag{5}
\]
Write \(w=c_m v^m+\cdots\), with \(m\ge1\) and
\(c_m\in L^*\). The two terms not containing \(w\) in
the parentheses belong to \(L\). Characteristic zero and (3)
therefore give the exact leading term
\[
\deg_v J(0)=2m-1\ge1,\qquad
[v^{2m-1}]J(0)=m\,y_\rho c_m^2\ne0.
\tag{6}
\]
This contradicts \(J(0)=-a^3\in L^*\) in (2).
The contradiction proves
\[
k_\rho-y\ne0\quad\text{as an element of }L[v].
\tag{7}
\]

## 4. What the exclusion does not prove

Equation (7) permits division by \(R\) in the fraction field
\(L(v)\). It does not permit division by \(R\) in the whole
line ring \(L[v]\): a nonconstant nonzero polynomial can still
vanish at points after extending the coefficient field. In
particular this argument has not removed any exceptional
projection locus or proved that the coefficient potentials
generate the full evaluation ideal.

No invariant correction or original-ring coordinate change
has been constructed, and the split-cubic case is not recognized
by this note. The proof does not transfer any cusp-specific
recognition statement from174 to the split chart.

The full saved chart175 was read before this proof was written.
Only its actual polynomial parameter ring, calibrated determinant,
and denominator-free first coefficient identity are used here;
the later quadratic and cubic potentials are not needed.
No new external theorem or checker is invoked. There is no
checker execution, frozen-source edit, unrestricted cancellation
claim, historical novelty clearance, human expert review, or
proof-assistant certification.
