# A projected quartic bound in the nonzero-R split-cubic branch

**Status: working necessary-condition proof under the saved actual chart175.**

The condition \(R=k_\rho-y\ne0\) gives a birational polynomial
plane parametrization, not automatically a closed embedding.
Nevertheless the calibrated actual determinant forces a nonzero
plane relation of total degree at most four. Its selected irreducible
factor occurs with multiplicity one, and the evaluated remaining
factor divides \(R^2\) in the whole generic-line ring.

The proof does not invert \(R\) as a unit of that ring. The actual
split example157 has \(R=-y\), so such a unit assumption would be false.
No recognition of the general split-cubic branch is claimed here.

## 1. Actual hypotheses and the two polynomial potentials

Retain all hypotheses and constructions of the
[actual split chart175](split-cubic-generic-chart-pass175-working.md).
In particular,
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad
(\deg_E X,\deg_E Y,\deg_E Z,\deg_E W)=(1,1,2,2),\\
\ker\theta_0=(\mathsf X\mathsf Z+\mathsf Y\mathsf W),\qquad
a=EX\ne0,\quad t=EY/a,\quad \rho=(E^2W/2)/a^2,\\
N=[u^3](\partial_Z|_A)\ne0,\qquad
L=\operatorname{Frac}\ker_A N,\quad A_L=L[v],\quad Nv=1 .
\end{gathered}
\tag{1}
\]
The initial ideal is the full weighted kernel. The field \(L\)
is finite separable over \(\mathbb C(t,\rho)\); coefficient partials
commute and fix \(v\). Write \(y,z,w,\vartheta\in L[v]\) for
the actual projected entries. The same chart supplies
\(L[y,z,w]=L[v]\) and
\[
z=k_t y+(k_\rho-y)\vartheta+n-tw,\qquad
\mathbb C(y,z,w)=L(v),\qquad
J_0=\det\frac{\partial(y,z,w)}{\partial(t,\rho,v)}=-a^3\in L^* .
\]
These are actual inverse and determinant inputs, not conditions
imposed on an arbitrary formal parametrization.

Use independent formal variables \(U,V,S_0\) and put
\[
\begin{gathered}
r=k_\rho,\qquad \mathcal R(U)=r-U,\qquad R=r-y,\\
f=H_2(k;U,V)+H_1(n;U,V),\qquad
g_3=H_3(k;U,V)+H_2(n;U,V),\\
P=\mathcal R S_0+f-\ell,\qquad
\Psi=f_VS_0+g_3-\ell_tU-\ell_\rho V,\\
P(y,\vartheta,w)=0,\qquad \Psi(y,\vartheta,w)=m,\qquad
k,n,\ell,m\in L .
\end{gathered}
\tag{2}
\]
Here \(H_j\) is the homogeneous coefficient Taylor polynomial defined
in chart175. In particular \(\deg f\le2\) and \(\deg g_3\le3\).
Assume only \(R\ne0\) as an element of the domain \(L[v]\).
It need not be constant.

For evaluated coefficients write
\[
A=f_V(y,\vartheta),\qquad B=f_U(y,\vartheta)-w,\qquad
C_i=f_i(y,\vartheta)+r_iw-\ell_i\quad(i=t,\rho).
\]
The formal gradients of the two potentials give
\[
(P_U,P_V,P_{S_0})|_{(y,\vartheta,w)}=(B,A,R),\qquad
(\Psi_U,\Psi_V,\Psi_{S_0})|_{(y,\vartheta,w)}=(C_t,C_\rho,A).
\tag{3}
\]
Indeed \((g_3)_U=f_t\), \((g_3)_V=f_\rho\),
\((f_V)_U=r_t\), and \((f_V)_V=r_\rho\).
The coefficient derivatives hold the formal variables fixed.

## 2. Polynomial elimination and birational field equality

Eliminate \(S_0\) without dividing by \(\mathcal R\):
\[
\begin{aligned}
\mathcal H(U,V)
&=\mathcal R(U)\{g_3-\ell_tU-\ell_\rho V-m\}
       +f_V(\ell-f)\\
&=\mathcal R(\Psi-m)-f_VP\in L[U,V],\\
\deg\mathcal H&\le4,\qquad
\mathcal H(y,\vartheta)=0 .
\end{aligned}
\tag{4}
\]
The second equality is an identity in the three-variable polynomial
ring; its \(S_0\) terms cancel exactly. At the actual curve, (3) gives
\[
\mathcal H_U(y,\vartheta)=RC_t-AB,\qquad
\mathcal H_V(y,\vartheta)=RC_\rho-A^2.
\tag{5}
\]
Terms differentiating \(\mathcal R\) or \(f_V\) vanish there because
\(P=\Psi-m=0\). No inverse of \(R\) was used for (4)--(5).

One may solve (2) in a fraction field:
\(w=(\ell-f(y,\vartheta))/R\).
The formula for \(z\) then shows
\[
L(y,\vartheta)=L(y,z,w)=L(v).
\tag{6}
\]
This uses \(R\ne0\), but does not assert
\(L[y,\vartheta]=L[v]\). In particular at least one of \(y,\vartheta\)
is nonconstant. The evaluation homomorphism \(L[U,V]\to L[v]\)
has a height-one prime kernel \((G)\), where \(G\) is irreducible
and nonconstant, determined up to \(L^*\).

## 3. The calibrated determinant proves nonvanishing and simple selection

All following differential identities are on the exact field \(L(v)\).
Differentiating the evaluated first potential gives
\[
R\,dw=-B\,dy-A\,d\vartheta-C_t\,dt-C_\rho\,d\rho .
\]
Also the expression for \(z\) gives
\[
J_0=
\left[
dy\wedge(R\,d\vartheta+B\,dt+A\,d\rho)\wedge dw
\right]_{dt\wedge d\rho\wedge dv}.
\tag{7}
\]
The omitted terms \((k_t-\vartheta)dy\) and \(-t\,dw\) in \(dz\)
do not contribute to this wedge.

Expansion of (7), followed by the preceding differential identity,
gives
\[
\begin{gathered}
R^2J_0=C_U\,\mathcal H_U(y,\vartheta)
                  +C_V\,\mathcal H_V(y,\vartheta),\\
C_U=R(\vartheta_\rho y_v-y_\rho\vartheta_v)+Ay_v,\\
C_V=R(y_t\vartheta_v-\vartheta_t y_v)-By_v .
\end{gathered}
\tag{8}
\]
Every coefficient here lies in \(L[v]\). For an explicit sign check,
expanding the right side using (5) yields \(R\) times
\[
\begin{aligned}
&-(RC_t-AB)(y_\rho\vartheta_v-y_v\vartheta_\rho)\\
&+(RC_\rho-A^2)(y_t\vartheta_v-y_v\vartheta_t)
 +(AC_t-BC_\rho)y_v ,
\end{aligned}
\]
which equals \(R^2J_0\) by (7). The calculation can be performed
after inverting the nonzero \(R\) in the fraction field, then cleared
to the displayed polynomial identity. It asserts no regular inverse
at a zero of \(R\).

Since \(R\ne0\) and \(J_0=-a^3\ne0\), the left side of (8)
is nonzero. Thus \(\mathcal H\) cannot be the zero polynomial.
Its vanishing at the actual curve implies \(G\mid\mathcal H\).
If \(G^2\mid\mathcal H\), both evaluated partials would vanish,
contradicting (8). Hence
\[
\mathcal H=GQ,\quad G\nmid Q,\quad Q(y,\vartheta)\ne0,\qquad
Q(y,\vartheta)\mid R^2\quad\text{in }L[v].
\tag{9}
\]
For the last assertion substitute
\(\mathcal H_U=QG_U\), \(\mathcal H_V=QG_V\) along the curve
into (8), then divide only by \(J_0\in L^*\).
This does not say that \(Q(y,\vartheta)\) is a unit.

A little more support information is immediate. Over an algebraic
closure of \(L\), if \(Q(y,\vartheta)\) vanishes at a finite parameter
value, then (9) forces \(R=0\) there. At that value
\(\mathcal H_V=QG_V=0\), so (5) gives \(A=0\).
Thus a possible zero of the evaluated cofactor must lie over
\(R=A=0\). This statement is only about its zero support, not its
multiplicity or the normality of the plane curve.

If \(y\in L\), the present nonzero \(R\) is a field unit, and (9)
does make the evaluated cofactor a unit of \(L[v]\).
For nonconstant \(y\), it generally does not.

## 4. Exact total degree without a plane-embedding theorem

The birational equality (6) gives the exact degree identity
\[
\deg G=\max(\deg_v y,\deg_v\vartheta)\le4 .
\tag{10}
\]
Here a nonzero constant has degree zero and the zero polynomial
has degree \(-\infty\). At least one degree is positive by (6).
The inequality follows from (4) and \(G\mid\mathcal H\).

For completeness, the equality does not require an algebraically
closed coefficient field or a closed plane embedding.
Let \(T\) be independent over \(L(v)\), and put
\(\zeta=T y+\vartheta\). Its degree in \(v\) is
\(d=\max(\deg_v y,\deg_v\vartheta)\), since its leading coefficient
cannot cancel for an independent \(T\).
For a polynomial \(p(v)\) of positive degree \(d\) over a field \(K\),
\([K(v):K(p(v))]=d\). Indeed \(p(v)-Z_0\) is irreducible in
\(K[v,Z_0]\), being linear in \(Z_0\), and Gauss's lemma gives
degree \(d\) over \(K(Z_0)\). Applying this with \(K=L(T)\) gives
\[
[L(T)(v):L(T)(\zeta)]=d .
\tag{11}
\]

On the other hand the polynomial substitution
\(V=Z_0-TU\) preserves irreducibility of \(G\) after adjoining \(T\).
If \(D=\deg G\), its resulting degree in \(U\) is exactly \(D\):
the highest coefficient is \(G_D(1,-T)\ne0\).
It is primitive in \(U\), so it remains irreducible over
\(L(T,Z_0)\). The field equality
\(L(T)(y,\vartheta)=L(T)(v)\) in (6) identifies its root \(U=y\)
and \(Z_0=\zeta\). Its function-field degree is therefore \(D\).
Comparison with (11) proves \(D=d\).

This argument also covers a constant \(y\) or a constant
\(\vartheta\). It does not invoke polynomial-embedding degree
divisibility, conclude that \(G\) is a coordinate, or show
that \(L[y,\vartheta]\) is integrally closed.

## 5. Actual boundary and exact remaining obligations

The inverse-verified split example157, rewritten in the selected
chart in175, has
\[
\begin{gathered}
L=\mathbb C(t,\rho),\qquad v=-a_0,\qquad y=-v,\qquad
w=t,\qquad \vartheta=1-ty,\\
k=0,\qquad n=-\rho,\qquad \ell=-1,\qquad m=-t,\\
R=-y,\qquad f=-V,\qquad A=-1,\qquad
\mathcal H=1-Ut-V .
\end{gathered}
\tag{12}
\]
Its actual global polynomial inverse and full split initial kernel
are proved in157, not newly presumed here.
The factor \(R=-y\) has a zero on the whole generic line.
Nevertheless the selected plane relation is linear and its cofactor
is a unit. Thus both the nonunit warning and the bound above are
compatible with an actual recognized example.

In general (9) leaves exceptional cofactor zeros over \(R=A=0\).
Even away from that issue, a birational polynomial parametrization
need not be a closed embedding. The two potentials are not asserted
to generate the entire three-variable evaluation ideal.
No all-degree recognition theorem for split-cubic frames follows
from a plane degree bound alone.

The full saved inputs
[initial bound157](two-linear-two-quadratic-initial-bound-pass157-working.md),
[normal forms157](two-linear-cubic-normal-forms-pass157-working.md),
[split correction obstruction158](split-cubic-invariant-correction-obstruction-pass158-working.md),
and [actual chart175](split-cubic-generic-chart-pass175-working.md)
were read for this derivation. The new calibration and degree arguments
are written above without a new external theorem. The obstruction158
still rules out a weight-three invariant correction; it does not
supply a different global invariant or coordinate.

There is no unrestricted cancellation, arbitrary-entry, historical
novelty, human expert, or proof-assistant verification claim.
No checker was executed or imported for this note, and all174 and
earlier artifacts remain unchanged.
