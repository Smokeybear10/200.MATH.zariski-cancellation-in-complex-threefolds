# Excess cofactor order consumes critical points of the first projection

This note proves a local order bound in the actual polynomial-radical
chart \(q=\rho^2-g(t)\). If the evaluated cofactor vanishes to higher
order than the return polynomial at a point, that point consumes at
least the return multiplicity among the zeros of \(y_v\). Combined
with the retained strict and simple-root bounds, this excludes
projected degrees three and four for the rebuilt quartic model
\(X^2Z-W^2+Y^4\).

The degree-at-least-two part of that model is reduced to
\(\deg_vy=1,\deg_v\theta=2\). The remaining conic is not excluded here.
The constant-first line is a separate actual-derivation argument and
is not an input to the higher-degree exclusion.

## 1. Actual chart and cofactor identities

Assume the actual globally sliced exact1122 full-quartic hypotheses
of [universal184](weight-four-universal-chart-potentials-pass184-working.md)
in a literal selected chart, with
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad a_0=EX\ne0,\\
N=[u^3]\partial_Z|_A\ne0,\quad
L=\operatorname{Frac}(\ker_A N),\quad A_L=L[v],\quad Nv=1,\\
[L:\mathbb C(t,\rho)]<\infty,\quad t,\rho\text{ algebraically independent},\\
Y=y+tX,\quad Z=z+\sigma X+qX^2,\quad
W=w+\theta X+\rho X^2,\quad L[y,z,w]=L[v],\\
q=\rho^2-g(t),\quad g(t)\in\mathbb C(t),\qquad J_0=-a_0^3\in L^* .
\end{gathered}                                                    \tag{1}
\]
All projected entries belong to \(L[v]\); coefficient partials extend
uniquely and commute on \(L\), then fix \(v\). The statement below
requires this actual chart and its scalar determinant, not merely
polynomial identities imposed on freely chosen coefficients.

Use the universal Taylor polynomials and retain all lower potentials:
\[
\begin{gathered}
f=H_2(q)+H_1(k)+n,\quad \mathcal R=f_V=2V+k_\rho,\quad c=f_\rho,\\
S=H_3(q)+H_2(k)+H_1(n),\quad T_0=\ell-S,\\
Q=H_4(q)+H_3(k)+H_2(n)-\ell_tU-\ell_\rho V-m,\\
\mathcal H=T_0^2+\mathcal R cT_0+\mathcal R^2Q,\\
z=2\rho w+f(y,\theta),\quad
Rw=T_0(y,\theta),\quad
w^2+c(y,\theta)w+Q(y,\theta)=0,\quad
R=2\theta+k_\rho .
\end{gathered}                                                    \tag{2}
\]
The coefficient of \(w^2\) is one because \(q_{\rho\rho}=2\).
For the remainder of the local argument assume \(R\ne0\). The whole-line
return and (2) yield
\[
\mathcal C=L[y,\theta]\subset\mathcal O=L[v],\quad
\mathcal O=\mathcal C+\mathcal Cw,\quad
R\mathcal O\subset\mathcal C,\quad
\operatorname{Frac}\mathcal C=L(v).
\tag{3}
\]
In particular the evaluation kernel of \(L[U,V]\to L[v]\) is generated
by one irreducible polynomial \(G\). No normality of \(\mathcal C\)
is assumed.

Define, with coefficient derivatives taken before evaluation in
\(\Lambda_t,\Lambda_\rho\),
\[
\begin{gathered}
B_1=f_t(y,\theta)+q_{t\rho}w,\quad
C_1=f_\rho(y,\theta)+2w,\\
\Lambda_i=\ell_i-S_i(y,\theta)-\mathcal R_i(y,\theta)w
 \quad(i=t,\rho),\\
D_U=R(y_v\theta_\rho-y_\rho\theta_v)+C_1y_v,\quad
D_V=R(y_t\theta_v-y_v\theta_t)-B_1y_v .
\end{gathered}                                                    \tag{4}
\]
Here \(q_{t\rho}=0\), but keeping the universal notation helps track
the fixed derivative convention. The arbitrary-\(q\) identities are
\[
\begin{gathered}
\mathcal H_U(y,\theta)=-R(C_1B_1+R\Lambda_t),\qquad
\mathcal H_V(y,\theta)=-R(C_1^2+R\Lambda_\rho),\\
Rw_v=-B_1y_v-C_1\theta_v,\\
J_0=[dy\wedge(R\,d\theta+B_1dt+C_1d\rho)\wedge dw]
                                      _{dt\wedge d\rho\wedge dv},\\
R^3J_0=D_U\mathcal H_U(y,\theta)+D_V\mathcal H_V(y,\theta).
\end{gathered}                                                    \tag{5}
\]
They follow from the actual potentials and calibration, as reconstructed
in [cofactor222](rank-two-saturated-pair-cofactor-exclusion-pass222-working.md).
Thus \(G\) occurs simply in the nonzero \(\mathcal H\), and
\[
\mathcal H=GQ_1,\quad
0\ne q_1:=Q_1(y,\theta)\mid R^3,\quad
\mathcal H_i(y,\theta)=q_1G_i(y,\theta)\quad(i=U,V).
\tag{6}
\]

We also use two already established universal order bounds:
\[
q_1\mid\frac{R^3}{\operatorname{rad}R},\qquad
\operatorname{ord}_r q_1\le1
 \quad\text{if }\operatorname{ord}_rR=1 .
\tag{7}
\]
The first is [strict225](rank-two-strict-return-cofactor-obstruction-pass225-working.md),
and the second is
[simple-root231](universal-simple-return-root-cofactor-bound-pass231-working.md).
Their hypotheses are precisely (3)--(6) and \(J_0\in L^*\).
They do not require plane smoothness. To recall the strict bound, putting
\(W_0=R^3/q_1\) gives
\(W_0J_0=D_UG_U+D_VG_V\) and
\(W_0(C_1^2+R\Lambda_\rho)=-R^2G_V\), after evaluation.
At a return root where \(W_0\ne0\), these force \(C_1=D_U=D_V=0\)
and contradict the first identity. This proves the first assertion of (7).

## 2. A local excess-order lemma

Suppose \(y\) is nonconstant, and extend coefficients to an algebraic
closure \(\Omega\) of \(L\). At a root \(r\) of the nonconstant \(R\), put
\[
m_r=\operatorname{ord}_rR\ge1,\quad
\nu_r=\operatorname{ord}_r(y_v)\ge0,\quad
k_r=\operatorname{ord}_rq_1\ge0 .
\tag{8}
\]
The symbol \(k_r\) in this section is an integer order, not a derivative
of the lower potential \(k\). All orders refer to polynomials in
\(\Omega[v]_{(v-r)}\), with coefficients fixed.

Assume \(k_r>m_r\). From
\(\mathcal H_V=q_1G_V=-R(C_1^2+R\Lambda_\rho)\), divide by \(R\)
in the local fraction field and then evaluate. The quotient
\(q_1G_V/R\) has positive order, so
\[
C_1(r)=0 .
\tag{9}
\]
If the evaluated \(G_V\) vanishes identically, the same conclusion follows
immediately from the right-hand expression. At \(r\) the middle
one-form in the determinant (5) is now \(B_1(r)\,dt\).
Since \(J_0\ne0\), necessarily \(B_1(r)\ne0\).

The special return formula in (2) is essential here:
\(R_v=2\theta_v\), hence
\(\operatorname{ord}_r\theta_v=m_r-1\) in characteristic zero.
The two terms \(Rw_v\) and \(C_1\theta_v\) have orders at least \(m_r\).
The third identity in (5) therefore gives
\[
\operatorname{ord}_r(B_1y_v)\ge m_r.
\]
Because \(B_1(r)\ne0\), this proves the new local implication
\[
\boxed{\ k_r>m_r\quad\Longrightarrow\quad
             2\le m_r\le\nu_r.\ }
\tag{10}
\]
The inequality \(m_r\ge2\) uses the simple-root assertion of (7).
In particular an excess root requires a zero of \(y_v\) of order
at least two, not just a critical point of multiplicity one.

No coefficient derivative has been applied to \(r\).
The derivatives in (5) are formed with \(v\) fixed before scalar
extension and point evaluation. The argument does not presume a
smooth projected point or a nonvanishing gradient of \(G\).

## 3. Global degree cost of the excess

Let \(i=\deg_vy\ge1\), \(d=\deg_vR=\deg_v\theta\), and let
\(\mathcal E\) be the set of roots with \(k_r>m_r\).
The derivative \(y_v\) is nonzero and has degree \(i-1\).
Therefore (10) gives
\[
\sum_{r\in\mathcal E}m_r
 \le\sum_{r\in\mathcal E}\nu_r\le i-1 .
\tag{11}
\]
All roots of \(q_1\) are roots of \(R\) by (6).
The strict bound (7) gives \(k_r\le3m_r-1\).
Summing the positive excess, and bounding all other orders by \(m_r\),
proves
\[
\boxed{\deg_vq_1\le
d+2(i-1)-|\mathcal E|\quad\text{if }\mathcal E\ne\varnothing.}
\tag{12}
\]
If \(\mathcal E=\varnothing\), then \(q_1\mid R\) over \(\Omega[v]\),
and hence over \(L[v]\) by polynomial division. In particular
\[
\boxed{\ i\le2\ \Longrightarrow\ q_1\mid R,\qquad
i=3\ \Longrightarrow\ \deg_vq_1\le d+3.\ }
\tag{13}
\]
The first assertion holds because every excess root would contribute
at least two to the sum in (11). If \(R\) is a nonzero constant,
the same divisor conclusion follows directly from (6).
No algebraic closedness of \(L\) is assumed in these conclusions.

## 4. Application to the rebuilt quartic repeated-root model

Now assume the entire actual initial kernel is
\((X^2Z-W^2+Y^4)\), in the displayed literal \(Z\) pivot. Its chart
has \(q=\rho^2-t^4\). This is a rebuilt chart after an actual bad-slot
interchange from \(Z^2-X^2W-Y^4\); no old \(N,L,R\) is transported
without rebuilding.

The Taylor polynomials and the leading sextic are
\[
\begin{gathered}
H_2(q)=V^2-6t^2U^2,\quad H_3(q)=-4tU^3,\quad H_4(q)=-U^4,\\
R_1=2V,\quad (H_2(q))_\rho=0,\qquad
\mathcal H_6=16t^2U^6-4U^4V^2
             =4U^4(2tU-V)(2tU+V).
\end{gathered}                                                    \tag{14}
\]
Thus \(\mathcal H\) has degree exactly six with no restriction on the
lower potentials. Its three lines are distinct over \(L\), since
\(t\ne0\).

The exact-field characteristic-polynomial argument used in
[pass235](rank-one-distinct-root-residue-sextic-line-reduction-pass235-working.md)
depends only on the birationality in (3). It gives
\(\deg G=\max(\deg_vy,\deg_v\theta)\) and pure top equal to a scalar
times one linear form to that power. If \(G\) selects either simple
line in (14), it has degree one. The top of its cofactor then evaluates
to degree five, while \(\deg R^3\le3\), contrary to (6).

All remaining tops have the form \(G_d=c_0U^d\), with \(1\le d\le4\).
Consequently
\[
\deg_vy=i<d=\deg_v\theta=\deg_vR.
\tag{15}
\]
For \(d\ge2\), \(y\) cannot be constant: otherwise
\(\mathcal C=L[\theta]\) would have fraction field of degree \(d>1\)
inside \(L(v)\), contrary to (3). Thus \(i\ge1\), and (13) applies.

If \(d=3\), the top of \(Q_1\) is a nonzero scalar multiple of
\(U(16t^2U^2-4V^2)\). Its \(UV^2\) term evaluates to degree
\(i+6\), strictly greater than the \(U^3\) term and than every lower
total-degree term, whose evaluated degree is at most six. Hence
\(\deg_vq_1=i+6\). Since \(i=1\) or \(2\), (13) would give
\(\deg_vq_1\le3\), a contradiction.

If \(d=4\), the top of \(Q_1\) is a nonzero scalar multiple of
\(16t^2U^2-4V^2\). Its \(V^2\) term has degree eight; its other top
term and all lower terms have smaller degree. Thus
\(\deg_vq_1=8\). For \(i=1,2\), (13) gives degree at most four;
for \(i=3\), it gives degree at most seven. Again there is a contradiction.

Therefore the entire degree-at-least-two branch in this rebuilt chart
is reduced to
\[
\boxed{\deg_vy=1,\qquad \deg_v\theta=2,\qquad
       L[y,\theta]=L[v].}
\tag{16}
\]
This argument itself does not use an exclusion of the constant-first
line \(d=1\); that line is handled by a separate original-derivation
argument. Nor does this note use or assert an \(R=0\) exclusion.

## 5. A necessary cofactor condition on the remaining conic

In (16), use the actual affine polynomial \(y\) as coefficient-field
parameter. Then \(\theta=P(y)\), where \(P\in L[U]\) has degree two,
and one can choose \(G(U,V)=V-P(U)\).
In particular \(G_V=1\), so (5),(6) show \(R\mid q_1\).
Together with (13), this gives
\[
q_1=\eta R,\qquad \eta\in L^*.
\tag{17}
\]
At every root of \(R\), the identity
\(-R(C_1^2+R\Lambda_\rho)=\eta R\) further gives
\(C_1^2=-\eta\ne0\).
This is a necessary local condition, not a proof that \(R\) is squarefree
or that the conic exists. Multiple roots are not excluded by this step.

## 6. Scope

The new lemma is the actual local implication (10) and its exact-field
degree consequence. It uses the special formula \(R=2\theta+k_\rho\);
it has not been transferred to the preceding square-root pivot.
The quartic application excludes degrees three and four without
assuming normality or an intrinsic conductor classification.

The remaining quadratic graph has not been recognized or excluded.
No coefficient-field coordinate is claimed to be an ambient polynomial
coordinate, and no coefficient-field unit is declared an original-ring
unit. The full cancellation question and arbitrary initial-kernel entry
remain outside this result.

The universal strict and simple-root source arguments were reread before
composition. The new local order argument and the exact evaluated
cofactor degrees were independently challenged before this source was
saved. No saved checker was executed, imported, or compiled, and no
previous source, packet, or index was changed.
