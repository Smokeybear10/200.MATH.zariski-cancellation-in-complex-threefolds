# The product-radical rank-one chart has a nonzero sextic

Status: bounded working degree reduction for a supplied actual full
initial kernel \(Z^2-XYW\). The algebraic relation \(q^2=t\rho\)
does not cancel the leading sextic. Its two leading factors have
multiplicities two and four.

In the nonzero-return branch, the actual cofactor and conductor
identities exclude projected degrees three and four, as well as the
conic in the multiplicity-two direction. What remains is a projected
line or a conic whose linear transverse parameter already generates
the coefficient-field line. Neither statement supplies an original
invariant coordinate. The zero-return branch remains outside this note.

## 1. Actual hypotheses and exact coefficient field

Assume
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
Here \(T\) is independent, the displayed ideal is the entire initial
kernel, and the capital letters are actual polynomial coordinates.
No globally minimal frame is assumed.

The literal \(Z\) pivot in
[universal184](weight-four-universal-chart-potentials-pass184-working.md),
with the ratio-field gates of
[normal forms184](weight-four-positive-bad-rank-normal-forms-pass184-working.md),
supplies
\[
\begin{gathered}
0\ne N=[u^3](\partial_Z|_A),\qquad
L=\operatorname{Frac}(\ker_A N),\qquad A_L=L[v],\quad Nv=1,\\
t=b/a,\qquad \rho=h/a^2,\qquad q=e/a^2,\qquad q^2=t\rho,\\
[L:\mathbb C(t,\rho)]<\infty,\qquad
Y=y+tX,\quad Z=z+\sigma X+qX^2,\quad
W=w+\vartheta X+\rho X^2,\\
y,z,w,\sigma,\vartheta\in L[v],\qquad L[y,z,w]=L[v],
\qquad J_0=-a^3\in L^* .
\end{gathered}
\tag{2}
\]
The ratios \(t,\rho\) are algebraically independent. Their partials
extend uniquely and commute on the finite separable field \(L\), and
then hold \(v\) fixed. In particular
\[
q_t=\frac{q}{2t},\qquad q_\rho=\frac{q}{2\rho},\qquad
q_{\rho\rho}=-\frac{q}{4\rho^2}\ne0.
\tag{3}
\]
These are derivatives in the exact field, not a choice of an analytic
square-root branch or an assumption that \(L\) is rational.

## 2. All lower potentials are retained

For \(c\in L\), let
\[
H_j(c;U,V)=\sum_{i=0}^j
\frac{c_{t^i\rho^{j-i}}}{i!(j-i)!}U^iV^{j-i}.
\tag{4}
\]
The formal variables \(U,V\) are independent and fixed by coefficient
partials. With arbitrary actual lower potentials \(k,n,\ell,m\in L\),
put
\[
\begin{gathered}
f=H_2(q)+H_1(k)+n,\qquad \mathcal R=f_V,\qquad c=f_\rho,\\
S=H_3(q)+H_2(k)+H_1(n),\qquad T_0=\ell-S,\\
Q=H_4(q)+H_3(k)+H_2(n)-\ell_tU-\ell_\rho V-m,\\
\mathcal H=\frac{q_{\rho\rho}}2T_0^2+
                 \mathcal R cT_0+\mathcal R^2Q .
\end{gathered}
\tag{5}
\]
The universal potentials give
\[
z=q_\rho w+f(y,\vartheta),\qquad
Rw=T_0(y,\vartheta),\qquad
\frac{q_{\rho\rho}}2w^2+c(y,\vartheta)w+Q(y,\vartheta)=0,
\quad R=\mathcal R(y,\vartheta).
\tag{6}
\]
Thus \(\mathcal H(y,\vartheta)=0\). Its total degree is at most six.
No lower potential has been normalized or set to zero.

For the remainder of the note assume \(R\ne0\) in \(L[v]\).
Set \(\mathcal C=L[y,\vartheta]\), \(\mathcal O=L[v]\).
The first equation of (6) and the whole-line equality in (2) give
\(\mathcal O=\mathcal C[w]\). Since \(q_{\rho\rho}/2\in L^*\),
the last equation is monic after scalar division. Consequently
\[
\mathcal O=\mathcal C+\mathcal Cw,\qquad
R\mathcal O\subset\mathcal C,\qquad
\operatorname{Frac}\mathcal C=L(v).
\tag{7}
\]
The last assertion uses \(Rw\in\mathcal C\) and \(R\ne0\).
This is not a claim that \(\mathcal C\) is normal.

## 3. Exact leading sextic

Write \(\Xi=\rho U-tV\). Repeated differentiation using (3) gives
\[
\begin{aligned}
H_2(q)&=-\frac{\Xi^2}{8q^3},\\
H_3(q)&=\frac{\Xi^2(\rho U+tV)}{16q^5},\\
H_4(q)&=-\frac{\Xi^2(5\rho^2U^2+6t\rho UV+5t^2V^2)}
                    {128q^7},\\
R_1:=\partial_VH_2(q)&=\frac{\Xi}{4q\rho},\qquad
(H_2(q))_\rho=-\frac{\Xi(\rho U+3tV)}{16\rho q^3}.
\end{aligned}
\tag{8}
\]
For example all mixed derivatives can be computed as
\(q\,(\tfrac12)_i(\tfrac12)_j t^{-i}\rho^{-j}\),
where the parentheses denote falling factorials. This calculation
takes place in the field defined by \(q^2=t\rho\).

Only the displayed highest parts can contribute to degree six:
\[
\mathcal H_6=\frac{q_{\rho\rho}}2H_3(q)^2
           -R_1(H_2(q))_\rho H_3(q)+R_1^2H_4(q).
\tag{9}
\]
Substitution of (8) reduces the bracket, after factoring
\(\Xi^4/(2048\rho^2q^9)\), to
\[
-(\rho U+tV)^2
+2(\rho U+3tV)(\rho U+tV)
-(5\rho^2U^2+6t\rho UV+5t^2V^2)
=-4\rho^2U^2.
\]
Therefore
\[
\boxed{\mathcal H_6=-\frac{U^2(\rho U-tV)^4}{512q^9}\ne0,
\qquad
\mathcal R=\frac{\rho U-tV}{4q\rho}+k_\rho.}
\tag{10}
\]
In particular \(\deg\mathcal H=6\), independently of every lower
potential. There is no lower-degree eliminant obtained by cancellation
of this sextic.

## 4. The universal strict cofactor mechanism still applies

Let \(G\) generate the height-one evaluation kernel of
\(L[U,V]\longrightarrow L[v]\). For clarity, the arbitrary-\(q\)
identities from
[cofactor222](rank-two-saturated-pair-cofactor-exclusion-pass222-working.md)
are rebuilt here; its special ratio \(F_4(1,t)/\rho\) is not imported.
Define
\[
\begin{gathered}
B_1=f_t(y,\vartheta)+q_{t\rho}w,\qquad
C_1=f_\rho(y,\vartheta)+q_{\rho\rho}w,\\
\Lambda_i=\ell_i-S_i(y,\vartheta)-\mathcal R_i(y,\vartheta)w,
\quad i=t,\rho,\\
D_U=R(y_v\vartheta_\rho-y_\rho\vartheta_v)+C_1y_v,\qquad
D_V=R(y_t\vartheta_v-y_v\vartheta_t)-B_1y_v.
\end{gathered}
\tag{11}
\]
Coefficient derivatives in \(\Lambda_i\) precede evaluation. The formal
identities \(S_U=f_t,S_V=f_\rho,\mathcal R_U=q_{t\rho}\),
\(\mathcal R_V=q_{\rho\rho}\), \(c_U=\mathcal R_t\),
\(c_V=\mathcal R_\rho\), \(Q_U=S_t-\ell_t\), and
\(Q_V=S_\rho-\ell_\rho\) follow directly from (4).
Differentiating (5), then using (6), gives
\[
\begin{gathered}
\mathcal H_U(y,\vartheta)=-R(C_1B_1+R\Lambda_t),\qquad
\mathcal H_V(y,\vartheta)=-R(C_1^2+R\Lambda_\rho),\\
Rw_v=-B_1y_v-C_1\vartheta_v,\qquad
R^3J_0=D_U\mathcal H_U(y,\vartheta)+D_V\mathcal H_V(y,\vartheta).
\end{gathered}
\tag{12}
\]
The last equality is the universal calibrated wedge. These derivations
use no rationality of \(q\). Since \(R,J_0\ne0\), both evaluated
gradients cannot vanish. Thus \(G\) occurs simply and
\[
\mathcal H=GQ_1,\qquad 0\ne q_1:=Q_1(y,\vartheta)\mid R^3.
\tag{13}
\]

The stronger conclusion of
[strict225](rank-two-strict-return-cofactor-obstruction-pass225-working.md)
uses only these same identities. Indeed put \(W_0=R^3/q_1\).
Polynomial cancellation gives
\[
W_0J_0=D_UG_U(y,\vartheta)+D_VG_V(y,\vartheta),\qquad
W_0(C_1^2+R\Lambda_\rho)=-R^2G_V(y,\vartheta).
\tag{14}
\]
At any geometric root \(r\) of \(R\), if \(W_0(r)\ne0\), the second
identity forces \(C_1(r)=0\). Then \(D_U(r)=0\); the third identity
of (12) gives \(B_1(r)y_v(r)=0\), so \(D_V(r)=0\).
The first identity of (14) contradicts \(J_0\in L^*\).
Descent of the monic squarefree divisor from an algebraic closure
therefore proves
\[
\boxed{q_1\mid R^3/\operatorname{rad}R.}
\tag{15}
\]
Here \(\operatorname{rad}R=1\) when \(R\) is constant. The proof never
calls \(R\), \(q\), or a coefficient-field unit an original-ring unit.

## 5. Excluding the larger projected components

By (7), the elementary plane-degree argument in
[leading-sextic220](rank-two-binary-quartic-leading-sextic-pass220-working.md)
applies over the exact field \(L\): writing
\[
g=\deg G=\max(\deg_vy,\deg_v\vartheta),
\tag{16}
\]
the top part of \(G\) is a scalar times a pure \(g\)-th power of
one linear form. To recall why, make a linear change over \(L\)
so the two generator degrees are \(i<j\). The characteristic
polynomial of the first on the free rank-\(j\) module \(L[v]\)
over the second generator's polynomial ring equals its minimal
polynomial by birationality. Its coefficient of first-variable
degree \(j-r\) has second-variable degree at most
\(\lfloor ir/j\rfloor<r\), by the pole orders of the \(j\) roots
over infinity. Thus its pure top is the first variable to power
\(j\). Constant first generator forces \(j=1\).
This argument proves a relation over \(L\); it makes no ambient change.

By (10), the selected top is consequently \(U^g\), with \(g\le2\),
or \(\Xi^g\), with \(g\le4\).

If it is \(U^2\), then \(\vartheta\) has degree two and \(y\)
has smaller degree. The degree-four top of \(Q_1\) is a nonzero
multiple of \(\Xi^4\), which evaluates to degree eight.
All lower terms evaluate to degree at most six. But \(R\) has
degree at most two, contradicting (13).

Suppose instead that the selected top is \(\Xi^g\), with \(g=3\)
or \(4\). Put \(\xi=\rho y-t\vartheta\). Both \(y,\vartheta\)
have degree \(g\), while \(d=\deg_v\xi<g\).
The polynomial \(\xi\) cannot be constant: otherwise
\(\mathcal C=L[y]\), contradicting
\([L(v):L(y)]=g>1\). Thus
\[
1\le d<g,\qquad
\mathcal C=L[y,\xi],\qquad
R=\xi/(4q\rho)+k_\rho,\qquad \deg_vR=d.
\tag{17}
\]

For \(g=3\), the degree-three top of \(Q_1\) is a nonzero
multiple of \(U^2\Xi\). It evaluates to degree \(6+d>6\).
Every lower term has evaluated degree at most six, so
\(\deg_vq_1=6+d\). Divisibility (13) would require
\(6+d\le3d\), impossible for \(d=1,2\).

For \(g=4\), the degree-two top of \(Q_1\) is a nonzero
multiple of \(U^2\). Thus \(\deg_vq_1=8\), since lower terms
evaluate to degree at most four. The same divisibility forces
\(8\le3d\); by (17), \(d=3\).

This last pair is excluded by an elementary conductor argument.
The ring \(L[v]\) is free of rank four over \(L[y]\).
Multiplication by \(\xi\) has a monic characteristic polynomial
over \(L[y]\). Since \(L(y,\xi)=L(v)\), its minimal polynomial
has degree four and equals that characteristic polynomial.
Therefore
\[
\mathcal C=\bigoplus_{j=0}^3 L[y]\xi^j.
\tag{18}
\]
A nonzero summand has degree \(4i+3j\), with \(i\ge0\).
These degrees have distinct residues modulo four for different
\(j\), so leading cancellation between summands is impossible.
None equals five. But \(Rv^2\in\mathcal C\) by (7), and
\(\deg_v(Rv^2)=3+2=5\), a contradiction.
This is the exact-field degree argument underlying
[conductor206](radical-projection-conductor-cubic-reduction-pass206-working.md),
not a genus formula or assumed classification of singularities.

The coarse divisor (13) already suffices for these degree exclusions.
The strict improvement (15) remains an additional restriction on the
surviving cases.

## 6. Exact remaining possibilities and boundaries

Under (1) and \(R\ne0\), the only possibilities left by this note are
\[
\begin{array}{c|c|c}
\text{selected component}&\text{projected degrees}&\text{return}\\ \hline
G_1\text{ has top }U
&y\in L,\ \deg_v\vartheta=1&\deg_vR=1\\
G_1\text{ has top }\Xi
&\xi\in L,\ \deg_vy=\deg_v\vartheta=1&R\in L^*\\
G_2\text{ has top }\Xi^2
&\deg_vy=\deg_v\vartheta=2,\ \deg_v\xi=1&\deg_vR=1 .
\end{array}
\tag{19}
\]
For the conic, constancy of \(\xi\) is ruled out by birationality,
so it is affine nonconstant. Each row therefore gives
\(\mathcal C=L[v]\). In the first and third rows, (15) further
gives \(\deg_vq_1\le2\); in the second \(q_1\in L^*\).
These are necessary conditions, not realizability claims.

No result here treats \(R=0\), recognizes \(A\), or constructs an
actual invariant coordinate. In particular the \(L\)-linear change
from \((y,\vartheta)\) to \((y,\xi)\) is only a calculation in the
projected coefficient-field ring. The task is not reduced by an
unjustified ambient rational coordinate change.

The README and retained positive-rank normal forms were inspected to
avoid duplicating a previously treated supplied kernel. The universal
potentials, arbitrary-\(q\) cofactor derivation, strict root argument,
plane-degree proof, and elementary conductor-degree proof were fully
reread before this composition. Fresh unsaved symbolic arithmetic
independently reconstructed (8)--(10), keeping all lower potentials
available in (5). No saved checker was executed, imported, or compiled.
No previous proof, index, JSON, or packet was changed.

This is a bounded supplied-frame working reduction, not arbitrary
entry, unrestricted cancellation, a historical novelty claim,
human expert review, or proof-assistant certification.
