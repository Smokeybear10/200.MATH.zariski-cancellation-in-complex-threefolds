# Actual local restrictions on a proper radical projection

Status: working necessary restrictions, not recognition or a unit-speed
theorem. In the actual nonzero-return radical branch, a proper projected
plane ring has second-generator degree at most three. In particular,
none of the degree-four second-generator cases allowed by the initial
algebraic bounds occurs. Degree three requires a genuinely quadratic
center with two roots in the exact coefficient field. Further explicit
coefficient relations are given for both the cusp and the node.

The actual examples207 show that projection defects themselves cannot
be excluded. Nothing below asserts that the speed \(EX\) is a unit,
that an invariant ambient coordinate exists in every such frame, or
that the changes over the coefficient field descend to the original ring.

## 1. Exact inputs, potentials and the moving parameter

Retain the full actual hypotheses of
[eliminant206](weight-four-radical-nonzero-r-eliminant-pass206-working.md):
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad A=\ker E,\\
\deg_E(X,Y,Z,W)=(1,1,2,2),\quad
\ker\theta_0=(\mathsf X^2\mathsf Z-\mathsf W^2),\\
a=EX\ne0,\quad q=\rho^2,\quad
L=\operatorname{Frac}\ker_A N,\quad A_L=L[v],\quad Nv=1,\\
O=L[v],\quad C=L[y,\vartheta]\subsetneq O,\quad
O=C+Cw,\quad R=2\vartheta+k_\rho\ne0,\quad RO\subset C.
\end{gathered}
\tag{1}
\]
Here \(t,\rho\) are independent, \(L/\mathbb C(t,\rho)\) is
finite, and the exact coefficient partials extend to \(L\).
The calibrated scalar is \(J_0=-a^3\in L^*\).

Use the formal polynomials \(S,b_0,Q\) and the evaluated
\(B_1,C_1,\Lambda_t,\Lambda_\rho\) defined explicitly in
eliminant206. The particular identities needed here are
\[
\begin{gathered}
\mathcal P(U,V,W_0)=(2V+k_\rho)W_0+S(U,V)-\ell,\\
\mathcal K(U,V,W_0)=W_0^2+b_0(U,V)W_0+Q(U,V),\\
\mathcal P(y,\vartheta,w)=\mathcal K(y,\vartheta,w)=0,\\
(\mathcal P_U,\mathcal P_V,\mathcal P_{W_0})=(B_1,C_1,R),\qquad
(\mathcal K_U,\mathcal K_V,\mathcal K_{W_0})
 =(-\Lambda_t,-\Lambda_\rho,C_1),\\
B_1=S_U(y,\vartheta),\quad C_1=2w+b_0(y,\vartheta),\quad
b_0=S_V,\quad [U^2]S=k_{tt}/2,\\
J_0=\left[dy\wedge(R\,d\vartheta+B_1dt+C_1d\rho)\wedge dw
\right]_{dt\wedge d\rho\wedge dv}.
\end{gathered}
\tag{2}
\]
Every gradient is formed before evaluation. In particular
\(\Lambda_\rho=\ell_\rho-S_\rho(y,\vartheta)-k_{\rho\rho}w\).

The exact center polynomial is
\[
V_c=-k_\rho/2,\qquad p(U)=S(U,V_c)-\ell.
\tag{3}
\]
Since the plane ring is proper, eliminant206 proves that \(p\)
is nonconstant and squarefree, with degree one or two. At every
zero of \(R\), therefore,
\[
\vartheta=V_c,\quad p(y)=0,\quad B_1=p'(y)\ne0.
\tag{4}
\]
The final inequality can be evaluated after algebraic closure of
\(L\); it does not assert that every zero of \(R\) belongs to \(L\).

The fully read
[conductor reduction206](radical-projection-conductor-cubic-reduction-pass206-working.md)
gives an affine parameter \(x=v+\lambda\), \(\lambda\in L\), with
\[
C=L[x^2,x^3+c x],\quad c\in L,\quad
\mathfrak c=(x^2+c)O,\quad
2\le d:=\deg_vy\le4,\quad 2\le e:=\deg_v\vartheta\le4.
\tag{5}
\]
The original generators belong to the span of
\(1,x^2,x^3+cx,x^4\). The parameter change fixes \(t,\rho\)
and has Jacobian determinant one. Thus
\(dt\wedge d\rho\wedge dv=dt\wedge d\rho\wedge dx\),
and the calibrated determinant remains \(-a^3\) in these variables.
Coefficient partials on \(L\) are unchanged; total derivatives of
polynomials in \(x\) must still account for the moving shift.

## 2. The exact cusp jets

Suppose \(c=0\). Write the original entries as
\[
\begin{gathered}
y=y_c+a_2x^2+a_3x^3+a_4x^4,\qquad
\vartheta=V_c+b_2x^2+b_3x^3+b_4x^4,\\
w=w_0+w_1x+w_2x^2+\cdots.
\end{gathered}
\tag{6}
\]
The constant term of \(\vartheta\) is \(V_c\), since
\(R\in x^2O\). All displayed coefficients lie in \(L\).
In the cusp ring, the missing class in \(O/C\) is the coefficient
of \(x\). The equality \(O=C+Cw\) consequently forces
\(w_1\ne0\).

At \(x=0\), both \(y_x\) and \(\vartheta_x\) vanish. The
\(x\)-derivative of the fourth potential in (2) gives
\(C_1(0)w_1=0\), hence \(C_1(0)=0\). Let
\(B=p'(y_c)\in L^*\). The coefficient of \(x^2\) in the
third potential is then \(B a_2\), so \(a_2=0\).
If also \(b_2=0\), every polynomial in the centered generators
would vanish to order at least three unless it had a nonzero
constant. This contradicts \(x^2\in C\). Thus \(b_2\ne0\).

The next third-potential coefficient and the second
fourth-potential coefficient are respectively
\[
B a_3+2b_2w_1=0,\qquad
w_1^2=\Lambda_\rho(0)b_2.
\tag{7}
\]
For the first equality, the only new mixed contribution is
\(\mathcal P_{VW_0}b_2w_1=2b_2w_1\).
For the second, \(\mathcal K_{W_0W_0}/2=1\),
\(a_2=0\), and \(C_1(0)=0\). In particular \(a_3\ne0\).

Differentiate \(p(y_c)=0\) in the exact coefficient field.
At the cusp, \(S_V=-2w_0\) and
\((V_c)_\rho=-k_{\rho\rho}/2\). It follows that
\[
0=B(y_c)_\rho+S_\rho(y_c,V_c)
       +k_{\rho\rho}w_0-\ell_\rho,
\qquad \Lambda_\rho(0)=B(y_c)_\rho.
\tag{8}
\]
At \(x=0\), the shift contributions to total \(y_t,y_\rho\)
vanish because \(y_x=0\). Thus the wedge in (2) gives
\[
J_0=-B(y_c)_\rho w_1=-\frac{w_1^3}{b_2}=-a^3,
\qquad w_1^3=a^3b_2,
\qquad (y_c)_\rho\ne0.
\tag{9}
\]
Shift contributions to derivatives of \(w\) do not change this
coefficient, which uses only \(w_x=w_1\) after wedging with
\(dt,d\rho\). Equations (6)--(9) prove, in particular,
\(\operatorname{ord}_{x=0}R=2\). This exact order is a consequence
of the potentials, not merely of the conductor inclusion.

## 3. The return divisor has degree at most three

Differentiate the third potential with respect to \(x\):
\[
B_1 y_x+C_1\vartheta_x+Rw_x=0.
\tag{10}
\]
At a repeated zero of \(R\), one has \(\vartheta_x=R_x/2=0\).
Equations (4) and (10) then give \(y_x=0\).

In the node case \(c\ne0\), these two derivatives never vanish
together. Otherwise, differentiating polynomial expressions for
\(x^2,x^3+cx\) in \(y,\vartheta\) would give simultaneously
\(2x=0\) and \(3x^2+c=0\), which is impossible. Thus every
zero of \(R\) is simple in the node case.

The two roots of \(x^2+c\) are distinct and lie above the same
plane point. They are zeros of \(R\) by the conductor inclusion.
Every other fiber of the plane parametrization is a singleton:
equality of squares makes two parameters equal or opposite, and
at opposite nonzero parameters equality of \(x(x^2+c)\) forces
\(x^2+c=0\). Since every zero of \(R\) maps to
\((y,V_c)\) with \(p(y)=0\), and \(p\) has at most two roots,
there is at most one further zero of \(R\). All are simple, so
\(e\le3\).

In the cusp case, the same derivative argument excludes repeated
zeros away from zero, since \(2x\ne0\) there. The cusp
parametrization is injective: equality of both \(x^2,x^3\)
forces equality of the parameters. The zero at the cusp has
order exactly two by Section2. At most one additional root of
\(p\) is available, and it has at most one preimage. Thus here
also \(e\le3\). We have proved
\[
\boxed{\deg_v\vartheta\le3\quad\text{whenever }C\ne O.}
\tag{11}
\]

If \(e=3\), both types require a genuinely quadratic center,
so \(k_{tt}\ne0\). There is exactly one further simple zero
of \(R\), away from the conductor divisor, and its plane point
is the other center root. The conductor point itself has a
\(y\)-value in \(L\): it is \(y_c\) for a cusp, and the
common even-part value at \(x^2=-c\) for a node. Therefore
the quadratic center splits into two distinct linear factors
over \(L\), not merely over an algebraic closure.

The coprime-degree bound of conductor206 excludes \((d,e)=(4,3)\).
Thus \(e=3\) permits only \(d=2,3\). If instead \(d=4\),
then \(e=2\). The simple selected factor \(G\) has
\(\deg G=4\) and \(\deg_U G=e=2\); since
\(\mathcal H=GQ_1\) and \(\deg\mathcal H\le5\), one has
\(\deg_U\mathcal H\le3\). The exact coefficient
\([U^4]\mathcal H=k_{tt}^2/4\) from eliminant206 proves
\[
d=4\quad\Longrightarrow\quad e=2,\quad k_{tt}=0,
\quad\deg p=1.
\tag{12}
\]

## 4. Additional degree-three coefficient constraints

### 4.1. Cusp

In the cusp case with \(e=3\), equations (6)--(7) and the exclusion
of \((4,3)\) put the original entries in the exact form
\[
y=y_c+a_3x^3,\qquad
\vartheta=V_c+b_2x^2+b_3x^3,\qquad a_3b_2b_3\ne0.
\tag{13}
\]
The additional simple zero of \(R\) is
\(x_*=-b_2/b_3\in L^*\), with
\(y_*=y_c-a_3b_2^3/b_3^3\). The two distinct center roots give
\[
p(U)=\frac{k_{tt}}2(U-y_c)(U-y_*),\qquad
k_{tt}=\frac{2p'(y_c)b_3^3}{a_3b_2^3}\ne0.
\tag{14}
\]
This is an exact coefficient constraint, not a contradiction.

### 4.2. Node

For \(c\ne0\) and \(e=3\), the degree bounds and conductor
write the original entries as
\[
\begin{gathered}
y=y_0+A_2x^2+A_3x(x^2+c),\qquad
R=(x^2+c)(r_1x+r_0),\qquad r_1\ne0,\\
\vartheta=(R-k_\rho)/2,\qquad
A_2r_1-A_3r_0\ne0.
\end{gathered}
\tag{15}
\]
For the last inequality, these two centered generators are linear
combinations of \(x^2,x^3+cx\). A zero coefficient determinant
would make their ring a single-generator ring of degree at least
two, contrary to the exact birational field equality.

Work temporarily over an algebraic closure and choose \(s^2=-c\).
The two node parameters \(s,-s\) have common plane point
\((y_D,V_c)\), where \(y_D=y_0-A_2c\in L\). Put
\(B_D=p'(y_D)\ne0\). At either of these points,
\[
y_x=2x(A_2+A_3x),\qquad
\vartheta_x=x(r_0+r_1x),\qquad
C_1(x)=-\frac{2B_D(A_2+A_3x)}{r_0+r_1x}.
\tag{16}
\]
The denominators are nonzero because \(R\) is squarefree.
The two \(w\)-values are distinct: otherwise all of
\(y,\vartheta,w\) would coincide, contradicting their generation
of \(O\). They are the two roots of the same monic quadratic
\(\mathcal K(y_D,V_c,W_0)\). Their sum is \(-b_0(y_D,V_c)\),
so their two values of \(C_1=2w+b_0\) are opposite.
Adding (16) at \(s,-s\) consequently gives
\[
\boxed{A_2r_0+cA_3r_1=0.}
\tag{17}
\]
The computation is an identity among elements of \(L\), so it
descends without any assumption that \(s\in L\).
Equations (15)--(17) force
\[
\begin{gathered}
A_2\ne0,\quad r_0=-\frac{cA_3r_1}{A_2},\quad
x_*=-r_0/r_1=\frac{cA_3}{A_2}\in L,\\
A_2^2+cA_3^2\ne0,\qquad x_*^2+c\ne0.
\end{gathered}
\tag{18}
\]
The additional center value is \(y_*=y(x_*)\in L\), distinct
from \(y_D\). In particular if \(d=2\), then \(A_3=0\)
and the additional return zero is \(x_*=0\). If \(d=3\),
both \(A_2,A_3\) are nonzero. Again these are necessary
constraints, not a proof of realization or exclusion.

## 5. Scope and the original-ring gap

The node and cusp examples in
[actual207](radical-nodal-cuspidal-actual-frame-pass207-working.md)
have \(e=2\) and satisfy the local conditions above. In its
cuspidal specialization, the calibrated parameter \(v=2x\)
gives \(y=2\rho-v^3/8\), \(\vartheta=v^2/8\), \(w=v/2\).
Thus \(a=1\), \(w_1=1/2\), \(b_2=1/8\) satisfy (9).
The cubic relation in (9) is compatible with an actual frame;
it is not a denominator contradiction.

All generator changes, roots and coefficients used here live in
the exact coefficient field or its explicitly identified algebraic
closure. Nothing makes them regular in \(A\) or supplies a
polynomial inverse in the original four-ring. No step infers
that the nonzero scalar \(a\in L\) is a unit of \(B\), or
that generic conductor geometry alone returns an invariant
ambient coordinate. Those are still separate original-ring gates.

The conclusion is a strict degree and local-coefficient refinement
of the proper-plane alternatives. It is not recognition of all
radical frames, an entry or minimality theorem, or unrestricted
cancellation. No saved checker was executed, imported or compiled;
no earlier proof, packet or index was edited. No human expert
certification, proof-assistant verification or historical novelty
clearance is claimed.
