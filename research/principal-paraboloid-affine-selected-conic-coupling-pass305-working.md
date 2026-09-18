# A reciprocal coupling constraint for an affine selected surface factor

Working result: in the actual reducible-surface conic sector of302,
suppose the surface factor that vanishes on the actual line is affine
in the two projected variables. Then the coupling has the exact form

\[
m=k_s=d+\frac{c}{t-\tau},\qquad d,c,\tau\in\mathbb C,\quad c\ne0.
\tag{1}
\]

This is a necessary coefficient restriction, not recognition of the
kernel or existence of these data. The other selection, where the
quadratic factor vanishes, is not covered by this argument.

## 1. Exact scope and factor conventions

Retain the complete actual nonzero-coupling chart of264, the fourth
potential and minor-unit theorem of
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md),
and the genuine-conic alternative of
[302](principal-paraboloid-reducible-surface-conic-reduction-pass302-working.md).
In particular the ambient ring is
\(\mathcal B=\mathbb C[X,Y,Z,W]=A[u]\), with original sliced
derivation \(E=\partial_u\), actual degree profile \((1,2,2,2)\),
and full initial kernel \((X^2Z-Y^2)\). Its coefficient field L is
finite over \(\mathbb C(t,s)\); the commuting coefficient partials
have joint constants exactly \(\mathbb C\).

The actual full scalar gives a generic polynomial line
\(O=L[v]\), two levels \(H_0=H-h_0\), \(Q_0=Q-q_0\), and a
unit ideal of their evaluated two-by-two gradient minors. In the
present conic case302 proves

\[
\begin{gathered}
H_0=(U+A)(U+B),\quad A,B\in L[P,V],\quad
A+B=A_1,\quad AB=A_0,\\
\deg A_1\le2,\quad\deg A_0\le3,\qquad
m_s=0,\quad m_t\ne0,\\
O=L[\sigma],\quad\deg_v\sigma=1,\quad
\theta\in L[\sigma],\quad\deg_\sigma\theta=2.
\end{gathered}
\tag{2}
\]

Fix the additional selection assumption explicitly:

\[
B=b_P P+b_V V+b_0,\quad y=-B(\sigma,\theta),\quad
(A-B)(\sigma,\theta)=\eta\in L^*.
\tag{3}
\]

The other factor A is quadratic. Let G be the full irreducible
projected equation. Since it is a genuine conic, equal-degree
divisibility gives \(A-B-\eta=\rho G\), \(\rho\in L^*\).
Its quadratic top is a nonzero multiple of \(P^2\), and its
V-coefficient is a nonzero element of L. Thus, after a scalar
normalization, G has the form \(V-g_2(P)\) with \(\deg g_2=2\).

All coefficient derivatives below hold U,P,V fixed. In particular
\(B_s\) is not the derivative of the evaluated polynomial.

## 2. The cubic terms determine the selected affine slopes

When \(m_s=0\), the formal surface coefficients are

\[
\begin{aligned}
F&=k_{tt}P^2/2+m_tPV+n_tP+n_sV,\\
D&=(2P+k_t)/m,\quad\lambda=(m_tP+n_s)/m,\\
A_1&=F_P-DF_V,\\
A_0&=F_V(\ell-F)/m+H_3(k)+H_2(n)
       -\ell_tP-\ell_sV-h_0.
\end{aligned}
\tag{4}
\]

The top parts needed here are

\[
\begin{aligned}
(A_1)_2&=-2m_tP^2/m,\\
(A_0)_3&=\left(k_{ttt}/6-m_tk_{tt}/(2m)\right)P^3
       +\left(m_{tt}/2-m_t^2/m\right)P^2V.
\end{aligned}
\tag{5}
\]

Since \(A=A_1-B\), the cubic part of \(AB\) is
\((A_1)_2(b_PP+b_VV)\). Comparing its two coefficients with
(5), using \(m_t\ne0\), yields

\[
\boxed{b_P=k_{tt}/4-\frac{m k_{ttt}}{12m_t},\qquad
b_V=m_t/2-\frac{m m_{tt}}{4m_t}.}
\tag{6}
\]

The formal V-coefficient of \(A-B=A_1-2B\) is consequently

\[
m_t-2b_V=\frac{m m_{tt}}{2m_t}.
\tag{7}
\]

It cannot vanish because G has nonzero V-coefficient. Thus
\(m_{tt}\ne0\). Also \((b_V)_s=0\), since every s-derivative
of m and its t-derivatives vanishes.

## 3. The fourth gradient forces a coefficient differential equation

Set \(q(P,V)=Q_0(-B(P,V),P,V)\). This polynomial vanishes on
the projected curve, so \(q=GT\) for some T. It is nonzero:
otherwise \(U+B\) would divide both levels, contradicting the
minor-unit theorem.

On the actual curve the first gradient is
\(\eta(1,b_P,b_V)\). The chain rule gives

\[
q_P^{\rm ev}=Q_P^{\rm ev}-b_PQ_U^{\rm ev},\qquad
q_V^{\rm ev}=Q_V^{\rm ev}-b_VQ_U^{\rm ev}.
\tag{8}
\]

The two minors involving U are eta times these expressions; the
third is their O-linear combination. Therefore their ideal is O.
Since \(q=GT\), both derivatives are divisible after evaluation
by \(T^{\rm ev}\), which must be a unit in \(O=L[v]\).
Since \(G_V\in L^*\), this proves

\[
q_V^{\rm ev}=T^{\rm ev}G_V\in L^*.
\tag{9}
\]

The formal fourth-gradient identities296 are
\(Q_V=(H_0)_s\) and
\(Q_U=(H_0)_P-D(H_0)_V+\lambda(H_0)_U\).
Differentiating the factorization before evaluation gives
\((H_0)_s^{\rm ev}=\eta B_s^{\rm ev}\). Equations (8),(9)
therefore imply

\[
q_V^{\rm ev}
=\eta\{B_s-b_V(b_P-Db_V+\lambda)\}^{\rm ev}\in L^*.
\tag{10}
\]

The expression in braces is affine in P and has no V-term,
because \((b_V)_s=0\). Its evaluation is constant, while sigma
is an affine nonconstant parameter. Its P-coefficient must be zero:

\[
0=(b_P)_s-\frac{b_V(m_t-2b_V)}m
  =-\frac{m m_{ttt}}{12m_t}
    +\frac{m m_{tt}^2}{8m_t^2}.
\tag{11}
\]

Here \(k_{tts}=m_{tt}\) and \(k_{ttts}=m_{ttt}\) follow by
commuting the exact coefficient partials. Clearing nonzero
denominators gives the necessary equation

\[
\boxed{2m_t m_{ttt}-3m_{tt}^2=0,
       \qquad m_s=0,\quad m_t m_{tt}\ne0.}
\tag{12}
\]

## 4. Exact integration, without a rational-field ansatz

Define \(r=m_{tt}/(2m_t)\in L^*\). Equation (12) gives
\(r_t=r^2\), and \(r_s=0\). Hence

\[
\tau=t+1/r,\qquad \tau_t=\tau_s=0,
\]

so \(\tau\in\mathbb C\) by the joint-constant theorem.
Put \(T=t-\tau\). Then \(r=-1/T\), and
\(a:=T^2m_t\) satisfies \(a_t=a_s=0\). It is a nonzero
complex constant. Finally \(d:=m+a/T\) has both derivatives
zero. Thus \(d\in\mathbb C\) and

\[
m=d-a/T=d+c/(t-\tau),\qquad c=-a\in\mathbb C^*,
\]

as claimed in (1). This does not identify L with \(\mathbb C(t,s)\).
It proves only that this particular coefficient belongs to that
rational subfield. Substitution in (6) also gives
\(b_V=d/(2(t-\tau))\), including the possible case d=0.

## 5. Remaining obligations

No division by \(t-\tau\) is made in the ambient polynomial ring.
There is no claim that the field-valued parameter normalization is
an actual coordinate change. The other coefficients, the finite
extension L, and the actual scalar still impose further constraints.
The branch where the quadratic surface factor is selected needs
its own derivative calculation; swapping factor names does not
preserve assumption (3).

This is a scoped working restriction toward the same unrestricted
cancellation goal. It does not finish that goal, establish existence
of an actual frame, or provide novelty, human-expert, or formal
proof-assistant verification.
