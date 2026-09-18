# A saturated cubic projection has no two-point fiber

Status: bounded working necessary condition for an actual supplied
rank-two quartic frame. If its projected component has degree three
and uses all three copies of its selected leading pair factor, its
normalization map is injective on geometric points.

This excludes a nodal cubic projection, or any other two-point
normalization fiber, in this precise branch. It does not exclude a
cusp, prove normality, recognize an original invariant coordinate,
or settle a smooth cubic graph.

## 1. Actual hypotheses and the saturated cubic condition

Assume the supplied globally sliced frame of
[general quartic220](rank-two-binary-quartic-leading-sextic-pass220-working.md):
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\\
\deg_E(X,Y,Z,W)=(1,1,2,2),\\
a=EX,\quad b=EY,\quad e_0=E^2Z/2,\quad h_0=E^2W/2,\\
\ker\bigl((\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
 \longmapsto(aT,bT,e_0T^2,h_0T^2)\bigr)
 =(\mathsf Z\mathsf W-F_4(\mathsf X,\mathsf Y)).
\end{gathered}
\tag{1}
\]
The symbol \(T\) is independent, the four capital letters are actual
coordinates, and the initial ideal is the entire displayed principal
ideal. The binary quartic \(F_4\) is nonzero.

The literal selected pivot and actual chart give
\[
\begin{gathered}
L=\operatorname{Frac}(\ker_A N),\qquad A_L=L[v],\qquad Nv=1,\\
t=b/a,\quad \rho=h_0/a^2,\quad q=e_0/a^2=F_4(1,t)/\rho,\qquad
[L:\mathbb C(t,\rho)]<\infty,\\
y,\vartheta,z,w\in L[v],\qquad L[y,z,w]=L[v],\qquad
J_0=-a^3\in L^* .
\end{gathered}
\tag{2}
\]
The ratios \(t,\rho\) are algebraically independent. Coefficient
partials on \(L\) are extended from these ratios and hold \(v\) fixed.
No rationality of \(L\) is assumed.

Suppose that the evaluated return \(R\) is nonzero. Then the actual
potentials and whole-line return, as proved in220, imply
\[
\begin{gathered}
\mathcal C=L[y,\vartheta]\subset\mathcal O=L[v],\qquad
\operatorname{Frac}\mathcal C=L(v),\\
\mathcal O=\mathcal C+\mathcal Cw,\qquad
R\mathcal O\subset\mathcal C .
\end{gathered}
\tag{3}
\]
In particular \(\mathcal O\) is the finite normalization of
\(\mathcal C\), not an assumed equality with it.

Let \(G\in L[U,V]\) generate the projected evaluation kernel.
The pure-leading-line theorem220 gives
\[
g=\deg G=\max(\deg_vy,\deg_v\vartheta),\qquad
G_g=c_0\ell(U,V)^g,\quad c_0\in L^* .
\tag{4}
\]
Here \(\ell\) is one of the distinct linear factors of the leading
sextic \(\mathcal H_6\). Let \(m\) be its multiplicity there.
The additional condition of this note is precisely
\[
g=m=3 .
\tag{5}
\]
It does not cover a degree-three component supported on a pair
factor of higher multiplicity.

## 2. The exact cofactor is a scalar times \(R^3\)

We retain the formal definitions from the universal potentials:
\[
\begin{gathered}
f=H_2(q)+H_1(k)+n,\quad \mathcal R=f_V,\quad R=\mathcal R(y,\vartheta),\\
S=H_3(q)+H_2(k)+H_1(n),\quad T_0=\ell_0-S,\\
Q=H_4(q)+H_3(k)+H_2(n)-(\ell_0)_tU-(\ell_0)_\rho V-m_0,\\
\mathcal H=(q_{\rho\rho}/2)T_0^2+
                         \mathcal R f_\rho T_0+\mathcal R^2Q .
\end{gathered}
\tag{6}
\]
Here \(k,n,\ell_0,m_0\in L\), while \(U,V\) are independent formal
variables and \(H_i\) are the coefficient Taylor polynomials.
The letters \(\ell_0,m_0\) are lower potentials, distinct from
the leading linear factor \(\ell\) and its multiplicity \(m\).

The full undivided gradient and calibrated wedge identities in
[universal cofactor222](rank-two-saturated-pair-cofactor-exclusion-pass222-working.md)
prove that \(G\) occurs simply in \(\mathcal H\), and that
\[
\mathcal H=GQ_1,\qquad
0\ne q_1:=Q_1(y,\vartheta)\mid R^3
\quad\hbox{in }L[v].
\tag{7}
\]
To recall the degree gate explicitly, the leading sextic is
\[
\mathcal H_6=-\rho^{-11}\prod_{i<j}
\left\{\ell_i(t)\ell_j(t)V
 -\rho\bigl(\ell_i'(t)\ell_j(t)+\ell_i(t)\ell_j'(t)\bigr)U\right\},
\tag{8}
\]
where \(F_4=\prod_i\ell_i(X,Y)\) with repeated root forms retained.
Since \(g=m=3\), the top homogeneous part of \(Q_1\) has degree
three and contains no copy of the selected factor \(\ell\).
The nonzero leading coefficient vector \((y_3,\vartheta_3)\)
of the projected pair lies on \(\ell=0\). Every other distinct
linear factor in (8) is nonzero on this vector. Thus
\[
\deg_vq_1=9,\qquad \deg_vR\le3 .
\tag{9}
\]
The first degree is exact: lower homogeneous terms of \(Q_1\)
evaluate to degree at most six and cannot cancel it.
The second bound follows because \(\mathcal R\) is affine in \(U,V\).
Divisibility (7) now forces
\[
\deg_vR=3,\qquad q_1=cR^3\quad\hbox{for some }c\in L^* .
\tag{10}
\]
This is a statement in the exact normalization ring. Neither \(R\)
nor \(q_1\) is asserted to be an ambient coordinate.

Every factor in (8) has nonzero coefficient of \(V\), namely
\(\ell_i(t)\ell_j(t)\in L^*\). Consequently \(y_3\ne0\): if
\(y_3=0\), then \(\ell(y_3,\vartheta_3)=0\) would force
\(\vartheta_3=0\) as well, contrary to \(g=3\). Hence
\[
\deg_v y=3.
\tag{11}
\]
This observation avoids needing a special normalization of the
chosen pair direction.

## 3. Every return root is a critical point of \(y\)

Use the exact evaluated coefficients
\[
\begin{gathered}
B_1=f_t(y,\vartheta)+q_{t\rho}w,\qquad
C_1=f_\rho(y,\vartheta)+q_{\rho\rho}w,\\
\Lambda_i=(\ell_0)_i-S_i(y,\vartheta)
                       -\mathcal R_i(y,\vartheta)w,\qquad i=t,\rho .
\end{gathered}
\tag{12}
\]
Each subscript on a formal polynomial differentiates its coefficients
before evaluation. The universal identities needed are
\[
\begin{gathered}
\mathcal H_V(y,\vartheta)=-R(C_1^2+R\Lambda_\rho),\\
R\,dw=-B_1dy-C_1d\vartheta+\Lambda_tdt+\Lambda_\rho d\rho,\\
J_0=\left[dy\wedge(Rd\vartheta+B_1dt+C_1d\rho)\wedge dw
       \right]_{dt\wedge d\rho\wedge dv}\in L^* .
\end{gathered}
\tag{13}
\]
These hold for the full \(q\), including its mixed derivatives;
they are not specialized radical or \(t\)-independent formulas.

Since \(\mathcal H=GQ_1\), evaluation of its formal derivative gives
\(\mathcal H_V(y,\vartheta)=q_1G_V(y,\vartheta)\).
Combine (10) and (13) and cancel the nonzero polynomial \(R\)
in the domain \(L[v]\):
\[
C_1^2+R\Lambda_\rho=-cR^2G_V(y,\vartheta).
\tag{14}
\]

Let \(\Omega\) be an algebraic closure of \(L\), and let
\(r\in\Omega\) be any root of \(R\). Evaluation of (14) gives
\(C_1(r)=0\), regardless of the multiplicity of that root.
The third line of (13) is a polynomial determinant identity with
coefficients in \(L\), so it can also be evaluated at \(v=r\).
If \(B_1(r)=0\), its entire middle row would vanish because
\(R(r)=C_1(r)=0\). This would give \(J_0=0\), impossible.
Thus \(B_1(r)\ne0\).

Taking the \(dv\) coefficient in the second line of (13), before
any evaluation, gives
\(Rw_v=-B_1y_v-C_1\vartheta_v\).
At the same root it follows that
\[
R(r)=0\quad\Longrightarrow\quad
C_1(r)=0,\quad B_1(r)\ne0,\quad y_v(r)=0.
\tag{15}
\]
All derivatives here were formed while fixing \(v\) as specified
in (2). No derivative of a moving algebraic root \(r\) has been
taken or omitted. Scalar extension and point evaluation are used
only after the polynomial differential identities are established.

As a small necessary consequence, \(R\) has at most two distinct
geometric roots, because the cubic \(y\) has quadratic derivative.
This is not by itself an exclusion of the cubic component.

## 4. The conductor detects every two-point fiber

The inclusion \(R\mathcal O\subset\mathcal C\) remains true after
extending scalars:
\[
R\,\Omega[v]\subset\Omega[y,\vartheta].
\tag{16}
\]
Indeed \(Rv^n\in L[y,\vartheta]\) for every \(n\ge0\), and
\(\Omega\)-linear combinations give (16).
The fraction-field and finite-normalization identities in (3)
also persist: a rational expression for \(v\) in \(y,\vartheta\)
and a monic integral equation for \(v\) retain their identities
after this extension.

Suppose distinct \(r,s\in\Omega\) belong to one projected fiber:
\[
y(r)=y(s),\qquad \vartheta(r)=\vartheta(s),\qquad r\ne s.
\tag{17}
\]
Every polynomial in \(\Omega[y,\vartheta]\) has equal values
at \(r,s\). Apply this to
\[
R(v)\frac{v-s}{r-s}\in\Omega[y,\vartheta].
\tag{18}
\]
Its value is \(R(r)\) at \(r\), and zero at \(s\), so \(R(r)=0\).
Interchanging the two points gives \(R(s)=0\).
Equation (15) therefore implies
\(y_v(r)=y_v(s)=0\).
This proves the conductor-to-critical-point implication without
assuming a particular equation for the projected cubic or its node.

## 5. A cubic has different values at distinct critical points

Write \(y(v)=a_3v^3+a_2v^2+a_1v+a_0\) over \(\Omega\),
with \(a_3\ne0\) by (11). Since \(r,s\) are distinct critical
points, its quadratic derivative is
\[
y_v(v)=3a_3(v-r)(v-s).
\tag{19}
\]
Taking a polynomial antiderivative, or comparing coefficients
in (19) and substituting the two values, gives
\[
y(s)-y(r)=-\frac{a_3}{2}(s-r)^3\ne0 .
\tag{20}
\]
This contradicts (17). Characteristic zero justifies division by
two and three; no analytic integration is involved.

We have proved the bounded theorem
\[
\boxed{g=m=3\quad\Longrightarrow\quad
v\longmapsto(y(v),\vartheta(v))
\text{ is injective on }\Omega\text{-points}.}
\tag{21}
\]
In particular an ordinary node, whose normalization has two
distinct points over the node, cannot occur.

## 6. Scope for the triple-root quartic

For root partition \(3+1\), the leading sextic has two distinct
pair factors, each of multiplicity three. Thus any selected cubic
component satisfies (5), and (21) applies in either direction.
In the normalized same-root direction \(q=t/\rho\), a projected
degree pair \((3,2)\) is included, but was not needed for the proof.

This result excludes geometric two-point fibers only. The cuspidal
case can have an injective normalization map and is not excluded.
A smooth cubic graph is also not excluded. Injectivity alone has
not been promoted to equality \(L[y,\vartheta]=L[v]\), smoothness,
or an original polynomial coordinate.

The projected line exclusions223 and this cubic necessary condition
do not settle all components for partition \(3+1\).
Degree-two components and injective cubic components still require
their own actual arguments. Arbitrary frame entry, other initial
ideals and unrestricted complex-threefold cancellation remain outside
this note.

The complete universal-cofactor222 source and the relevant actual
identities were freshly read and reconstructed before use.
New unsaved algebra checked the critical-value identity and
interpolation values; the conductor, cofactor and field-extension
arguments above are written proofs, not finite-test conclusions.
No saved checker was executed, imported or compiled. No frozen
source, index or packet was edited, and no expert review,
formal certification or historical novelty is asserted.
