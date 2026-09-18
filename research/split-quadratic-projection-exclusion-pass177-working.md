# The actual split chart cannot have quadratic projected y

**Status: working exclusion using the full actual projection conclusions175--176.**

The remaining quadratic possibility for \(y\) is impossible.
The whole plane embedding gives an elementary normal form for
its selected relation. The unit cofactor then makes the entire
eliminant a scalar multiple of that relation. Its cubic coefficient
in the second formal variable contradicts the required quadratic
center polynomial.

This is not recognition of the original invariant ring. Combined
with the separate constant-projection exclusion, it makes \(y\)
an affine parameter in the actual split chart.

## 1. Actual inputs and the contradiction hypothesis

Retain the actual setup of
[chart175](split-cubic-generic-chart-pass175-working.md):
\[
B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad
\deg_E(X,Y,Z,W)=(1,1,2,2),\quad
\ker\theta_0=(\mathsf X\mathsf Z+\mathsf Y\mathsf W).
\tag{1}
\]
This is the full weighted kernel. Use the selected nonzero
LND \(N=[u^3](\partial_Z|_A)\), the exact coefficient field
\(L=\operatorname{Frac}(\ker_A N)\), and \(A_L=L[v]\),
\(Nv=1\). The ratios \(t,\rho\) are independent, \(L\) is
finite separable over \(\mathbb C(t,\rho)\), and coefficient
partials are the original commuting extensions fixing \(v\).

The [whole-plane proof175](split-projection-exceptional-cone-pass175-working.md)
and [selected-component proof176](split-cubic-simple-selected-component-pass176-working.md)
give
\[
\begin{gathered}
L[y,\vartheta]=L[v],\qquad
\max(\deg_v y,\deg_v\vartheta)\le4,\\
r=k_\rho\in L,\qquad R=r-y\ne0,\qquad
q(V)=f(r,V)-\ell,\quad f=H_2(k;U,V)+H_1(n;U,V).
\end{gathered}
\tag{2}
\]
If \(y\) is nonconstant, the latter note proves
\[
R\text{ is squarefree},\qquad
1\le\deg_v y\le\deg q\le2 .
\tag{3}
\]
The quartic eliminant and its selected factor satisfy
\[
\begin{gathered}
\mathcal H=(r-U)\{g_3-\ell_tU-\ell_\rho V-m\}
                      +f_V(\ell-f),\qquad \deg\mathcal H\le4,\\
\mathcal H=GQ,\qquad Q(y,\vartheta)\in L^*,\qquad
g_3=H_3(k;U,V)+H_2(n;U,V).
\end{gathered}
\tag{4}
\]
Here \(G\) generates the prime plane evaluation kernel.
Its normalization may be changed by a nonzero element of \(L\).

Assume for contradiction that \(\deg_v y=2\).
Then (3) makes \(q\) quadratic, whose leading coefficient is
\[
[V^2]q=\frac{k_{\rho\rho}}2=\frac{r_\rho}2\ne0 .
\tag{5}
\]
Only the nonzero assertion in (5), not the full center formula,
will be needed for the final contradiction.

## 2. A quadratic first entry has an exact-field nested normal form

Write \(y=a_2v^2+a_1v+a_0\), with \(a_2\in L^*\).
An affine shift \(x=v+a_1/(2a_2)\) puts it in the form
\[
y=b+a_2x^2,\qquad
\vartheta=c_4x^4+c_3x^3+c_2x^2+c_1x+c_0,\qquad c_i\in L .
\tag{6}
\]
Coefficients of missing powers are zero.
The whole ring equality in (2) is now
\(L[x^2,\vartheta]=L[x]\).

One must have \(c_1\ne0\). Otherwise the two derivatives of
\(x^2,\vartheta\) both vanish at \(x=0\); differentiating a
polynomial expression for \(x\) in those generators gives
the contradiction \(1=0\) there.
Also \(c_3=0\): if not, choose \(x_*\) over an algebraic
closure with \(x_*^2=-c_1/c_3\). It is nonzero, so
\(x_*\) and \(-x_*\) are distinct. The odd part
\(x(c_1+c_3x^2)\) of \(\vartheta\) vanishes at both points.
Thus both generators have identical values there, contradicting
the polynomial expression for \(x\).

Set \(\zeta=c_1x\). There are \(a\in L^*\) and
\(P(U)\in L[U]\), \(\deg P\le2\), with
\[
y=b+a\zeta^2,\qquad
\vartheta=P(y)+\zeta,\qquad
a=a_2/c_1^2 .
\tag{7}
\]
Explicitly
\[
P(U)=\frac{c_4}{a_2^2}(U-b)^2
           +\frac{c_2}{a_2}(U-b)+c_0 .
\]
All these coefficients and the affine parameter lie in the
original exact field and ring. No square root was adjoined
to define \(\zeta\); the algebraic closure was used only to
rule out a two-point collision.

In these fixed formal axes choose
\[
G(U,V)=U-b-a\{V-P(U)\}^2 .
\tag{8}
\]
It is the selected irreducible relation. For example the pair
\((S,T)=(G,\ V-P(U))\) is a polynomial coordinate system over
\(L\), with explicit inverse in independent \(S,T\):
\[
U=S+b+aT^2,\qquad V=T+P(S+b+aT^2).
\]
This also directly identifies the evaluation kernel as \((G)\).

If \(\deg P=2\), then \(\deg G=4\), since its top term in
\(U\) has nonzero coefficient. If \(\deg P\le1\), including
zero and constant \(P\), then \(\deg G=2\): its \(V^2\)
coefficient is the nonzero \(-a\). In every case
\[
\deg G\in\{2,4\},\qquad \deg_VG=2,\qquad [V^2]G=-a .
\tag{9}
\]
The parameter \(\zeta\) may depend on \(t,\rho\). No coefficient
derivative is taken after this change; (8)--(9) are polynomial
identities over \(L\) in the original formal variables \(U,V\).

## 3. The unit cofactor and V-degree force a pure selected relation

If \(\deg G=4\), equation (4) immediately gives
\(\mathcal H=cG\) with \(c\in L^*\), by total degree.
If \(\deg G=2\), then \(\deg Q\le2\).
For \(c=Q(y,\vartheta)\in L^*\), the polynomial \(Q-c\)
belongs to the evaluation kernel \((G)\).
Degree additivity in \(L[U,V]\) therefore gives
\[
Q=c+\lambda G,\qquad
\mathcal H=cG+\lambda G^2,\qquad \lambda\in L .
\tag{10}
\]
The value \(\lambda=0\) is included.

On the other hand the explicit eliminant in (4) has
\(\deg_V\mathcal H\le3\). Indeed \(r-U\) is independent
of \(V\), \(g_3\) has \(V\)-degree at most three, and
\(f_V(\ell-f)\) has \(V\)-degree at most three.
The \(V^4\) coefficient in (10) is \(\lambda a^2\).
Thus \(\lambda=0\) also in the degree-two case. Both cases give
\[
\mathcal H=cG,\qquad c\in L^*,\qquad
[V^3]\mathcal H=0 .
\tag{11}
\]
An evaluated unit was not treated as a constant polynomial
without this explicit degree argument.

## 4. The cubic V coefficient gives the contradiction

Before any parameter change, the literal formula (4) gives
\[
[V^3]\mathcal H
 =\frac{r-U}{6}\,k_{\rho\rho\rho}
       -\frac{r_\rho^2}{2}.
\tag{12}
\]
For the first term, only \(H_3(k)\) contributes a \(V^3\)
term to \(g_3\). For the second, \([V]f_V=r_\rho\)
and \([V^2]f=r_\rho/2\); the part \(f_V\ell\)
has degree at most one in \(V\).
There is no omitted contribution from \(H_2(n)\) or the
linear \(\ell\) and \(m\) terms.

Equation (11) makes (12) the zero polynomial in \(L[U]\).
Its coefficient of \(U\) first gives
\(k_{\rho\rho\rho}=0\), and its constant coefficient then
gives \(r_\rho^2=0\). Since \(L\) is a field,
\[
r_\rho=0,
\tag{13}
\]
contrary to (5). This excludes \(\deg_v y=2\).

Combining this exclusion with (3) and the independent
[constant-projection exclusion176](split-constant-projection-exclusion-pass176-working.md)
proves
\[
y=\alpha v+\beta,\qquad
\alpha\in L^*,\quad\beta\in L,\qquad L[y]=L[v]
\tag{14}
\]
for the retained actual split chart.
Thus its generic second polynomial is a graph
\(\vartheta=P_*(y)\) with \(P_*\in L[y]\), \(\deg P_*\le4\).
No claim about the existence of an original-ring coordinate
or polynomial invariant correction follows yet.

## Scope and verification boundary

The quadratic exclusion itself does not use the constant-y
exclusion. That separate result is used only for the final
exhaustive conclusion (14). The whole-plane and unit-cofactor
inputs are essential and have not been replaced by fraction
field equality or a presumed irreducible eliminant.

The normal form was proved by polynomial derivatives and point
separation, not an external plane-embedding theorem. Its exact
coefficient field and the original formal axes are retained
through the final comparison. This is a proof-only note; no
new checker was executed or imported. It does not settle
split-case recognition, the other initial configurations,
arbitrary entry, or unrestricted cancellation. There is no
historical novelty, human expert review, proof-assistant
certification, publication or external-contact claim.
