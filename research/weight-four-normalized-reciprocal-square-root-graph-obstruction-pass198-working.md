# Normalized reciprocal square-root graph obstruction

Status: bounded working proof, pending independent saved-source review.
The actual normalized reciprocal monomial graph branch is impossible.
This note does not normalize arbitrary lower potentials; the normalization
is a separate input. All earlier sources and checkers are unchanged.

## 1. Actual hypotheses and exact fields

Retain the actual hypotheses of
[universal184](weight-four-universal-chart-potentials-pass184-working.md)
and the square-root reduction195:
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=\mathcal A[u],\qquad E=\partial_u,\qquad
\deg_E(X,Y,Z,W)=(1,1,2,2),\\
\ker\theta_0=(\mathsf Z^2-\mathsf X^3\mathsf Y),\qquad
a_E=EX,\quad t=EY/a_E,\quad q=E^2Z/(2a_E^2),\quad q^2=t,\\
\rho=E^2W/(2a_E^2),\qquad
N=[u^3](\partial_Z|_{\mathcal A})\ne0,\qquad
L=\operatorname{Frac}(\ker_{\mathcal A}N),\\
\mathcal A_L=L[v],\quad Nv=1,\quad
K=\ker_L\partial_\rho,\quad [K:\mathbb C(q)]<\infty,\quad
\ker_K\partial_q=\mathbb C .
\end{gathered}
\tag{1}
\]
The ratios \(t,\rho\) are independent, \(a_E\in L^*\), and the
commuting coefficient partials extend to the exact finite algebraic
fields. A subscript \(q\) below holds \(\rho\) fixed. Thus the old
coefficient derivative is \(\partial_t=(2q)^{-1}\partial_q\).
No rationality of \(K\) is assumed.

The actual projected chart and calibrated return are
\[
\begin{gathered}
Y=y+q^2X,\qquad Z=z+\left(\frac{y}{2q}+k\right)X+qX^2,
\qquad W=w+\vartheta X+\rho X^2,\\
L[y,z,w]=L[v],\qquad \mathbb C(y,z,w)=L(v),\qquad
\det\frac{\partial(Y,Z,W)}{\partial(t,\rho,v)}=-a_E^3\in L^*.
\end{gathered}
\tag{2}
\]
The determinant is independent of \(X\). These are actual consequences,
not proposed formal sufficiency conditions.

Assume the following normalized reciprocal data:
\[
R=k_\rho=q,\qquad k=q\rho,\qquad
n=-\frac{q\rho^2}{2},\qquad
\ell=-\frac{q\rho^3}{2}+l,\quad l\in K .
\tag{3}
\]
In particular \(f=1/R=1/q\). Assume the selected plane component
is a graph in \(y\), with \(y\) nonconstant. Equivalently for the
present use, \(\vartheta\in L[y]\). Since \(R=q\in L^*\), the
second and third potentials put \(z,w\in L[y,\vartheta]\).
Consequently (2) gives \(L[y]=L[v]\): \(y\) is affine in \(v\), and
\(\Gamma:=Ny\in L^*\). This proves the parameter gate rather than
normalizing \(\Gamma\) to one.

## 2. Literal potentials retain the arbitrary scalar term

For independent formal variables \(U,V\), put
\[
P(U)=-\frac{3U^2}{8q^4}+\frac{\rho U}{2q^2}+\frac{\rho^2}{2},
\qquad \zeta=\vartheta-P(y).
\tag{4}
\]
The second potential is
\[
z=-\frac{y^2}{8q^3}+\frac{\rho y}{2q}
       +q\vartheta-\frac{q\rho^2}{2}
 =-\frac{y^2}{2q^3}+\frac{\rho y}{q}+q\zeta .
\tag{5}
\]
The cubic polynomial in the third potential \(qw+S=\ell\) is
\[
S(U,V)=\frac{U^3}{16q^5}-\frac{\rho U^2}{8q^3}
       +\frac{UV}{2q}-\frac{\rho^2U}{4q}-q\rho V .
\tag{6}
\]
For completeness the quartic polynomial before subtracting the
derivatives of \(\ell\) is
\[
T(U,V)=-\frac{5U^4}{128q^7}+\frac{\rho U^3}{16q^5}
       -\frac{U^2V}{8q^3}+\frac{\rho^2U^2}{16q^3}
       -\frac{\rho UV}{2q}-\frac q2V^2 .
\]
Thus the fourth-potential eliminant, multiplied by \(R=q\), is
\[
\begin{aligned}
\mathcal H(U,V)
&=q\{T-\ell_tU-\ell_\rho V-m\}
  +\left(\frac U{2q}-q\rho\right)\{\ell-S\}\\
&=-\frac{q^2}{2}(V-P(U))^2
  +\frac{l/q-l_q}{2}U
  +\frac{5q^2\rho^4}{8}-q\rho l-qm .
\end{aligned}
\tag{7}
\]
Here \(m\in L\) and \(\mathcal H(y,\vartheta)=0\).
The \(V^2\) coefficient is \(-q^2/2\), the \(V\) coefficient is
\(q^2P(U)\), and completing this square gives the displayed constant
and linear terms. All derivatives in its first line are coefficient
partials before evaluation.

Since \(\zeta\in L[y]\) and \(y\) is transcendental over \(L\),
equation (7) makes the square \(\zeta^2\) a polynomial of degree at
most one in \(y\). Its degree must be even if positive. Therefore
\[
\zeta=\gamma\in L,\qquad l_q=l/q,\qquad l=Cq,\quad C\in\mathbb C .
\tag{8}
\]
The last inference uses \((l/q)_q=0\) in \(K\).
At this point neither \(\gamma\in K\) nor \(\gamma\ne0\) is assumed.
In particular the selected graph need not be assigned a rational
coefficient field.

Set \(a=y/(2q^2)-\rho\), a generic-line polynomial, not the speed
\(a_E\). Equations (5)--(6) become
\[
z=q\gamma-\frac{ya}{q},\qquad
w=C+\frac{ya^2}{2q^2}-a\gamma .
\tag{9}
\]
Equivalently
\[
w-C=\frac{(y-2q^2\rho)(-4q^4\gamma-2q^2\rho y+y^2)}{8q^6}.
\]
Equation (7) also fixes
\(m=q(5\rho^4/8-C\rho-\gamma^2/2)\). No further scalar is discarded.

## 3. The exact scalar Jacobian forces coefficient descent

At \(X=0\), take the determinant in columns \((q,\rho,y)\).
Its first row is \((0,0,1)\). Differentiating (9), with \(y\)
fixed in the first two columns, gives
\[
\begin{aligned}
J_y
&=z_qw_\rho-z_\rho w_q\\
&=\gamma\left(\gamma+q\gamma_q+\rho\gamma_\rho
                         -\frac{3y}{2q^2}\gamma_\rho\right)
 =-\frac{2q\,a_E^3}{\Gamma}\in L^* .
\end{aligned}
\tag{10}
\]
For a direct expansion one may use \(A=a+\rho=y/(2q^2)\):
\[
\begin{gathered}
z_q=\gamma+q\gamma_q+2A(3a+2\rho),\qquad
z_\rho=q(\gamma_\rho+2A),\\
w_\rho=\gamma-2aA-a\gamma_\rho,\qquad
w_q=\frac{2A}{q}\{\gamma-a(3a+2\rho)\}-a\gamma_q .
\end{gathered}
\]
These four terms cancel to (10). The calibration factor follows
from \(dt=2q\,dq\) and \(dy=\Gamma\,dv\) on the generic line.
The coefficient-field parts of \(dy\) do not affect this triangular
Jacobian change.

The nonzero determinant first gives \(\gamma\ne0\); its coefficient
of \(y\) then gives \(\gamma_\rho=0\). Hence
\[
\gamma\in K^*,\qquad b=q\gamma\in K^*,\qquad
J_y=\gamma b_q\ne0 .
\tag{11}
\]
In particular \(b_q\ne0\), so \(b\) is transcendental over
\(\mathbb C\). This step does not drop \(\Gamma\) or replace the
speed by a unit.

## 4. The actual projected field return is already impossible

From (9) one obtains, by direct expansion and rational inversion,
\[
z^2-2y(w-C)=b^2,\qquad
\rho=\frac{q(z-b)}{y}+\frac{y}{2q^2}.
\tag{12}
\]
Division by \(y\) is permitted here in the function field:
\(y\) is a nonconstant polynomial in the generic-line variable.
It is not an asserted original polynomial inverse.

The two independent variables \(\rho,y\) over \(K\) may therefore
be replaced by \(y,z\), so \(K(\rho,y)=K(y,z)\) and \(y,z\) are
independent over \(K\). Moreover every projected entry belongs to
\(K(\rho)[y]\). The exact actual return in (2) gives
\[
L(y)=\mathbb C(y,z,w)\subseteq K(\rho,y)\subseteq L(y).
\tag{13}
\]
Both inclusions are equalities. Since \(y\) is transcendental over
\(L\), intersecting \(K(\rho)(y)\) with \(L\) yields
\(L=K(\rho)\). This explicitly removes a possible proper algebraic
coefficient extension; it was not removed by assumption.

Equation (12) and the same equality now give
\[
K(y,z)=\mathbb C(y,z,w)=\mathbb C(y,z,b^2),
\qquad K=\mathbb C(b^2).
\tag{14}
\]
For the last equality, intersect with \(K\). For any fields
\(F\subseteq K\) and variables algebraically independent over \(K\),
one has \(K\cap F(y,z)=F\), by clearing a polynomial denominator
and comparing coefficients. Apply this with \(F=\mathbb C(b^2)\).

But \(b\in K\) is transcendental, so (14) would imply
\[
\mathbb C(b)\subseteq K=\mathbb C(b^2)\subseteq\mathbb C(b).
\]
This is impossible: the nontrivial automorphism \(b\mapsto-b\)
of \(\mathbb C(b)\) fixes \(b^2\). Equivalently
\([\mathbb C(b):\mathbb C(b^2)]=2\).
This proves exclusion using the calibrated scalar and actual field
return, without any assumption that \(K\) was initially rational.

## 5. Independent original-ring obstruction

There is also an obstruction which uses the original polynomial ring
directly and does not need the descent \(\gamma\in K\).
Using \(a=y/(2q^2)-\rho\) as in (9), all four actual entries are
\[
\begin{gathered}
Y=q^2(X+2a+2\rho),\\
Z=q\{X^2+(a+2\rho)X+\gamma-2a^2-2a\rho\},\\
W-C=\rho X^2+(\gamma-3a^2/2-2a\rho)X
                         +a^3+\rho a^2-a\gamma .
\end{gathered}
\tag{15}
\]
Their direct expansion gives the polynomial identity
\[
I_C:=Z^2-X^3Y-2Y(W-C)=q^2\gamma^2=(q\gamma)^2 .
\tag{16}
\]
The coefficients of \(X^3,X^2,X\) cancel in succession and the
constant coefficient is \(q^2\gamma^2\).

Under the actual hypotheses, \(q\gamma\in L\subseteq
\operatorname{Frac}\mathcal A\subseteq\operatorname{Frac}B\).
Equation (16) makes it integral over \(B\); the polynomial ring
\(B\) is normal, so \(q\gamma\in B\).
On the other hand \(I_C\), viewed in
\(\mathbb C[X,Y,Z][W]\), is primitive and linear in \(W\):
its coefficients \(-2Y\) and \(Z^2-X^3Y+2CY\) are coprime.
Gauss's lemma makes \(I_C\) irreducible and nonconstant in \(B\).
It cannot be a square. If \(\gamma=0\), (16) instead says this
nonzero polynomial is zero, also impossible.

This confirms the exclusion independently of the field argument.
Unlike a merely formal parametrization, the actual hypothesis really
does put \(q\gamma\) in the original fraction field. No such inclusion
is inferred for an unproved formal fixture.

## Scope

The result is conditional on the actual normalized reciprocal
monomial data (3) and a selected graph in \(y\).
It neither supplies the original-ring normalization nor treats
the reciprocal quadratic-projection alternative.
It does not settle the nonmonomial family \(f=\alpha t+\beta q\),
other initial forms, higher profiles, arbitrary entry, or unrestricted
cancellation. No generic coefficient or parameter was declared an
original coordinate.

The universal184 source was reread completely before this note was
written. The displayed identities and both exclusion arguments were
independently reconstructed here. No saved checker was executed,
imported, compiled, or edited. This is a bounded working proof,
not a novelty audit, human expert certification, or formal verification.
