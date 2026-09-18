# A linear rank-two center with quadratic second projection is a node or cusp

Status: bounded working description of the generic projected plane.
Under the actual rank-two hypotheses, a linear center and a quadratic
second projection force a proper plane ring with defect dimension one.
The exact conductor is the return polynomial times the line ring.
All normalizing coefficients below belong to the exact field \(L\);
no ambient polynomial coordinate change or original-ring recognition
is asserted.

## 1. Exact hypotheses and division by the return polynomial

Retain the supplied globally sliced exact1122 frame with full initial
kernel \((\mathsf Z\mathsf W-\mathsf X^4)\), original pivot
\(\partial_Z\), and exact chart of
[sextic reduction212](rank-two-t-independent-sextic-reduction-pass212-working.md).
In particular
\[
\begin{gathered}
O=L[v],\quad Nv=1,\quad C=L[y,\vartheta]\subset O,\quad
[L:\mathbb C(t,\rho)]<\infty,\\
R=2\rho^{-3}\vartheta+k_\rho\ne0,\quad
L[y,\vartheta,w]=O,\quad \operatorname{Frac}C=L(v),\\
Rw+S(y,\vartheta)-\ell=0,\qquad \deg_v\vartheta=2,\\
S(U,V)=-\rho^{-4}V^3+\tfrac12k_{tt}U^2+k_{t\rho}UV
       +\tfrac12k_{\rho\rho}V^2+n_tU+n_\rho V .
\end{gathered}
\tag{1}
\]
These ring equalities and potentials come from the actual frame.
They are not assumptions imposed on an arbitrary parametrized curve.
The coefficient partials keep formal \(U,V\) fixed.

Assume the center is linear:
\[
V_c=-\rho^3k_\rho/2,\qquad
p(U)=S(U,V_c)-\ell=B_1(U-U_0),\qquad
B_1\in L^*,\quad U_0\in L.
\tag{2}
\]
The U-quadratic coefficient is \(k_{tt}/2\), so \(k_{tt}=0\).
The coefficient of \(U\) gives \(B_1=k_{t\rho}V_c+n_t\).
Writing
\(\phi(V)=-\rho^{-4}V^3+k_{\rho\rho}V^2/2+n_\rho V\),
exact polynomial division gives
\[
\begin{gathered}
S-\ell=p(U)-\mathcal R D(U,V),\qquad
\mathcal R=2\rho^{-3}(V-V_c),\\
D(U,V)=\alpha U+D_0(V),\qquad
\alpha=-\rho^3 k_{t\rho}/2,\qquad
D_0(V)=-\frac{\phi(V)-\phi(V_c)}
                   {2\rho^{-3}(V-V_c)}\in L[V],\quad \deg D_0\le2.
\end{gathered}
\tag{3}
\]
The quotient in (3) is polynomial because its numerator vanishes
at \(V=V_c\).

Define the projected polynomial
\[
\widetilde w=w-\alpha y-D_0(\vartheta).
\tag{4}
\]
The third potential is now
\[
y=U_0-\frac{R}{B_1}\widetilde w,\qquad
O=L[\vartheta,\widetilde w].
\tag{5}
\]
For the ring equality, the right side recovers \(y\) by (5), then
recovers \(w=\widetilde w+\alpha y+D_0(\vartheta)\).
Conversely \(\widetilde w\in O\); these two inclusions use the full
triple ring in (1), not merely its fraction field.
Only nonzero scalars of \(L\) are inverted.

## 2. The exact-field odd-part argument

Complete the square of \(\vartheta\) over \(L\):
\[
\vartheta=A_2x^2+c_0,\qquad
x=v-v_0,\quad v_0,c_0\in L,\quad A_2\in L^* .
\tag{6}
\]
No square root of \(A_2\) is taken. Since \(N\) kills \(L\),
\(Nx=1\). Unique even/odd decomposition over \(L\) gives
\(\widetilde w=P(\vartheta)+xH(\vartheta)\), with
\(P,H\in L[T]\).

We claim \(H=b_1\in L^*\).
Extend scalars to an algebraic closure \(\overline L\).
If \(H=0\), both entries in (5) have zero derivative at \(x=0\).
They therefore cannot generate \(x\), by the chain rule.
If \(H\) were nonconstant, choose a root \(\xi\) of \(H\).
When \(\xi\ne c_0\), the two distinct points with
\(A_2x^2+c_0=\xi\) have equal values of both
\(\vartheta,\widetilde w\), contradicting generation in (5).
When \(\xi=c_0\), their derivatives at zero both vanish:
\(\vartheta_x(0)=0\) and \(\widetilde w_x(0)=H(c_0)=0\).
This again contradicts generation.
Thus \(H\) is a nonzero constant over \(\overline L\).
Its original coefficients belong to \(L\), so that constant is in
\(L^*\), and the original \(P\) also remains in \(L[T]\).
We have proved
\[
\widetilde w=P(\vartheta)+b_1x,\qquad
P\in L[T],\quad b_1\in L^*.
\tag{7}
\]
The argument uses point separation and the chain rule only as
necessary consequences of ring generation; neither is used as a
converse criterion.

## 3. Both plane rings and the exact conductor

Set
\[
r=2\rho^{-3}A_2\in L^*,\qquad
c_1=\frac{2\rho^{-3}c_0+k_\rho}{r}\in L .
\tag{8}
\]
Then \(R=r(x^2+c_1)\). Equations (5) and (7) give the equality
of plane subrings
\[
C=L[y,\vartheta]
 =L[\vartheta,Rx]
 =L[x^2,x^3+c_1x]\subsetneq L[x]=O .
\tag{9}
\]
Explicitly,
\(y=U_0-RP(\vartheta)/B_1-b_1Rx/B_1\), and conversely
\(Rx=-(B_1/b_1)(y-U_0)-RP(\vartheta)/b_1\).
These are identities over \(L\). They are not maps of the original
four-variable polynomial ring over \(\mathbb C\).

Write \(z_0=x^2\). The square of the odd generator is
\(z_0(z_0+c_1)^2\). Reduction of its powers and parity give the
direct vector-space and \(L[z_0]\)-module decomposition
\[
C=L[z_0]\oplus x(z_0+c_1)L[z_0],\qquad
\dim_L(O/C)=1 .
\tag{10}
\]
In particular \(x\notin C\), including when \(c_1=0\).
Every class in the quotient is a scalar multiple of the class of
\(x\), by division of its odd coefficient by \(z_0+c_1\).

The conductor is exactly
\[
\mathfrak c=\{h\in O:hO\subset C\}
 =(x^2+c_1)O=RO .
\tag{11}
\]
The displayed ideal is contained in \(C\) by (10), and multiplying
it by any element of \(O\) keeps it in that ideal, proving one
inclusion. Conversely write \(h=A(z_0)+xB(z_0)\) in the conductor.
Both \(h\) and \(xh\) belong to \(C\). Their odd parts show that
both \(B\) and \(A\) are divisible by \(z_0+c_1\).
Hence \(h\in(x^2+c_1)O\), proving equality.

The entire relation of the two normalized generators is
\(V^2-U(U+c_1)^2\): it is irreducible because \(U\) is not a
square in \(L(U)\), and the evaluation kernel has height one.
For \(c_1=0\) this is the cusp \(V^2=U^3\).
For \(c_1\ne0\), at \(U=-c_1,V=0\) its lowest nonzero homogeneous
part is \(V^2+c_1(U+c_1)^2\), two distinct lines after extending
scalars. Thus it is geometrically a node.
No assertion that the two identified parameter values belong to
\(L\) is needed.

## 4. Degree bookkeeping and the original-ring boundary

If \(P=0\) or \(P\) is constant, (5) and (7) give
\(\deg_v y=3\): the nonzero term \(-b_1Rx/B_1\) has degree three
and cannot cancel an even polynomial.
If \(j=\deg P\ge1\), its even contribution \(RP(\vartheta)\)
has degree \(2j+2\), distinct from three. Consequently
\[
\begin{array}{c|c|c}
P&\deg_vy&\deg_v\widetilde w\\ \hline
\text{zero or constant}&3&1\\
\deg P=1&4&2\\
\deg P=2&6&4
\end{array}
\tag{12}
\]
The bound \(d=\deg_v y\le6\) in212 rules out \(j\ge3\).
Thus this reproduces exactly the \(e=2\), linear-center possibilities
\((d,e)=(3,2),(4,2),(6,2)\) in
[degree pruning213](rank-two-squarefree-center-degree-pruning-pass213-working.md).
In each case \(\deg_v\widetilde w=d-2\).

This is a stronger generic ring description than a degree list:
the plane is necessarily proper and its conductor is exactly the
actual return polynomial ideal. It does not show that any listed
case satisfies all actual differential identities, nor that it is
impossible. The coefficient-field transformations (4), (6), and
(9) have not been descended to ambient coordinates.
No invariant coordinate or recognition of the original ring follows
from this note alone.

The retained212 proof and213 degree-pruning note were fully read.
No saved checker was executed, imported or compiled, and no earlier
source, checkpoint or index was changed. The full cancellation goal,
arbitrary entry and novelty questions remain outside this working
projected-ring result.
