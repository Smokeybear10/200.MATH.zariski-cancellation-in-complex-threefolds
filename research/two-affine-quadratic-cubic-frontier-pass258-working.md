# Structural frontier for an actual two-affine quadratic-cubic frame

For a supplied globally sliced time profile \((1,1,2,3)\), the
general initial-bound158 gives principal initial relation weight at
most five. A zero selected shift recognizes the kernel. In the
height-two case, a quadratic-slot partial of exact shift three gives
an exact coefficient-field chart with three successive determinant
identities. Its nonzero coupling branch has a whole polynomial-line
plane presentation satisfying a nonzero equation of degree at most
four. Its zero coupling branch is either recognized or has affine
first projection and a graph of degree at most six.

These are bounded reductions, not recognition of every1123 frame.
In particular, an actual initial ideal and a polynomial plane equation
over a coefficient field are different objects. No coefficient-field
shear below is asserted to be an ambient polynomial automorphism.

## 1. Actual entry, retained bounds, and elementary reductions

Assume
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad A=\ker E,
\quad K=\operatorname{Frac}A,\\
\deg_E(X,Y,Z,W)=(1,1,2,3),\quad
a=EX,\quad b=EY,\quad e=E^2Z/2,\quad h=E^3W/6.
\end{gathered}                                                     \tag{1}
\]
All four leaders are nonzero. The slice is not assumed to be an
ambient coordinate. If \(a,b\) are proportional over \(\mathbb C\),
a constant linear combination of \(X,Y\) is an invariant actual
coordinate and the regular-kernel endpoint recognizes \(A\).
Hence assume \(t=b/a\notin\mathbb C\).

For an independent \(T\), use the full weighted initial kernel
\[
I=\ker\{\mathbb C[\mathsf X,\mathsf Y,\mathsf Z,\mathsf W]
 \longrightarrow A[T],\quad
(\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
 \mapsto(aT,bT,eT^2,hT^3)\} .                                    \tag{2}
\]
The fully read [general theorem158](arbitrary-positive-weight-initial-bound-pass158-working.md)
applies with degree sum seven. In particular, the literal actual
partials \(T_Z=\partial_Z,T_W=\partial_W\) have exact shifts
and nonzero intrinsic LNDs satisfying
\[
\begin{gathered}
0\le k_Z\le4,\quad0\le k_W\le3,\qquad
N_i=[u^{k_i}]T_i|_A\ne0,\quad N_i\in\operatorname{LND}(A),\\
\deg_uT_i(u)\le k_i,\qquad N_i(a)=N_i(b)=N_i(e)=N_i(h)=0,\\
\operatorname{ht}I\in\{1,2\}.
\end{gathered}                                                     \tag{3}
\]
The final assertion uses independence of \(aT,bT\) and the
nonzero intrinsic LND fixing all leaders, exactly as in157/158.
The generated initial algebra is not the full associated graded ring.

If \(I=(F)\) is principal, \(F\) is irreducible and weighted
homogeneous, with \(2\le\operatorname{wt}F\le5\). An occurring
\(Z\)-pivot has shift four and an occurring \(W\)-pivot has
shift three. If \(\operatorname{ht}I=2\), both omitted triples
are dependent, and the strict versions of the cofactor bounds are
\[
\boxed{k_Z\le3,\qquad k_W\le2.}                                 \tag{4}
\]
These are applications of158, not a new argument replacing its
full-prime-kernel and exact-multiplicity hypotheses.

Two elementary recognition gates need only membership in \(I\),
not its principality. A weight-two relation must be
\(c\mathsf Z+Q_2(\mathsf X,\mathsf Y)\), with \(c\ne0\).
Replacing \(Z\) by \(cZ+Q_2(X,Y)\) has the inverse obtained by
solving for \(Z\), and gives three coordinates killed by \(E^2\).
The retained all-last-degree theorem156 recognizes that case.
A weight-three relation with nonzero \(\mathsf W\)-coefficient is
\(c\mathsf W+L_1(\mathsf X,\mathsf Y)\mathsf Z+Q_3(\mathsf X,\mathsf Y)\).
Replacing \(W\) by that actual polynomial, with the inverse again
obtained by solving for \(W\), lowers its time degree to at most two.
The resulting frame is recognized by an invariant-coordinate gate,
156, or the fully read [exact1122 synthesis257](full-exact1122-recognition-synthesis-pass257-working.md).

Consequently neither relation can occur in a hypothetical
nonpolynomial kernel, or in a genuinely minimizing degree-sum-seven
frame. This does not show that some such relation must occur.
In principal height one the residual forms, before further analysis,
are the absent-\(W\) cubic and the following weights four and five:
\[
\begin{aligned}
F_3&=L_1Z+Q_3,\\
F_4&=cZ^2+Q_2Z+L_1W+Q_4,\\
F_5&=L_1Z^2+cZW+Q_3Z+Q_2W+Q_5.
\end{aligned}                                                     \tag{5}
\]
Here the other coefficients are homogeneous in the formal good
variables, and the relation remains irreducible. Equation (5) is
only a weight decomposition, not a recognition classification.

## 2. The selected-partial wedge and the actual three-ring endpoint

The wedge mechanism in the fully read
[249](height-two-selected-partial-wedge-rank-pass249-working.md)
does not require equal degrees for the two bad slots. Here is the
needed argument with the actual present degrees.
Use the fixed-\(X\) expansions
\[
Y=y+tX,\quad Z=z+\sigma X+qX^2,\quad
W=w+\theta X+\rho X^2+rX^3,
\quad q=e/a^2,\quad r=h/a^3.                                    \tag{6}
\]
Notice that \(\rho\) is now the second coefficient of \(W\),
not its leading ratio. Localization at the invariant \(a\) gives
\(B_a=A_a[X]\). Quotienting by \(X\) gives the actual return
\[
K=\mathbb C(y,z,w).
\tag{7}
\]
The fixed-\(X\) coordinate Jacobian is independent of \(X\),
by the invariant volume argument of158. For a separating volume
\(\omega\) on \(K\), write it as \(J\omega\), \(J\in K^*\).
Contracting by the two literal partials gives
\[
\iota_{T_W}\iota_{T_Z}\omega=J^{-1}(dy+Xdt).
\tag{8}
\]
Since \(dt\ne0\), their horizontal wedge has exact \(X\)-degree
one. Their leading terms are \(a^{-k_i}N_iX^{k_i}\). Thus
\(k_Z+k_W\ge1\), and \(N_Z\wedge N_W\ne0\) exactly when that
sum is one. The top coefficient of their commuting bracket is
\(a^{-(k_Z+k_W)}[N_Z,N_W]\), since both kill \(a\). Hence the
intrinsic LNDs always commute. If both shifts are positive, they
are proportional over their common exact constant field
\(L=\operatorname{Frac}\ker_A N_Z\), of transcendence degree two.
No descent of that proportionality to \(\mathbb C(t)\) is inferred.

If one shift is zero, it preserves \(A\) and takes \(u\) into
\(A\), hence commutes with \(E\). Its actual polynomial kernel
is a three-variable polynomial ring \(S\), containing \(X\),
which is \(E\)-stable. More generally the same endpoint applies
whenever an actual nonzero derivation \(P\), commuting with \(E\),
has kernel \(S=\mathbb C[X,Y,Z]\) or \(\mathbb C[X,Y,W]\).

Indeed \(\delta=E|_S\ne0\), \(\delta X=a\ne0\), and
\(\delta^2X=0\). Divide its three coefficients by their gcd
\(g\). Since \(g\mid\delta X\in\ker\delta\), factorial closure
makes \(\delta g=0\). The resulting irreducible LND on \(S\)
still has actual coordinate \(X\) of derivation degree one.
Daigle's theorem, in the freshly read
[Dasgupta--Gupta Theorem 4.8](https://arxiv.org/html/1701.03635v1),
then supplies an invariant coordinate of \(S\). It remains an
actual coordinate after adjoining the omitted original variable.
The slice makes \(A\) regular, so
[Bhatwadekar--Gupta--Lokhande Theorem 3.5](https://arxiv.org/html/1501.01438v1)
gives \(A\simeq\mathbb C^{[3]}\).
This endpoint does not use three-good recognition156.

## 3. The maximal height-two quadratic pivot

For the rest of the new chart, assume explicitly
\[
\operatorname{ht}I=2,\qquad k_Z=3,
\quad N=N_Z.
\tag{9}
\]
The ratio field \(\mathbb C(t,q,r)\) is finite over
\(\mathbb C(t)\), because the initial fraction field is
\(\mathbb C(t,q,r)(aT)\) of transcendence degree two.
Primes on \(q,r\) denote the unique extended \(t\)-derivative.

In a separating coefficient basis \(t,r_1,r_2\) of \(K\), put
\(S=\sigma-q'y\), \(H=\rho-r'y\). The coefficient of \(X^4\)
in the literal determinant of (6) is
\(S_{r_1}H_{r_2}-S_{r_2}H_{r_1}\), so it vanishes.
The degree-three horizontal cofactor for \(T_Z\) is
\[
N=\frac{a^3}{J}
       (H_{r_2}\partial_{r_1}-H_{r_1}\partial_{r_2}).
\tag{10}
\]
This follows by using the rows of \(Y,W\); their top minors
are those of \(dt\) and \(d\rho-r'dy\).
The \(t\)-cofactor has no degree-three term. Thus
\(N(t)=N(H)=N(S)=0\), and \(N\ne0\) makes \(t,H\) independent.

Set \(\lambda=H\), \(k=S\), and
\(L=\operatorname{Frac}\ker_A N\). A local slice supplies
\(Nv=1\), \(K=L(v)\), and the exact finite field extension
\([L:\mathbb C(t,\lambda)]<\infty\). Its commuting coefficient
partials initially fix \(v\). The literal chart becomes
\[
\begin{aligned}
Y&=y+tX,\\
Z&=z+(q'y+k)X+qX^2,\\
W&=w+\theta X+(r'y+\lambda)X^2+rX^3,
\end{aligned}
\quad L[y,z,w]=L[v].
\tag{11}
\]
All displayed intercept coefficients also lie in \(L[v]\),
since \(a\in\ker N\) and they lie in \(A_a\).
The leading \(X^3\) cofactor of \(T_Z(v)\) is \(-1/J\),
whereas \(Nv=1\) makes it \(a^{-3}\). Therefore
\[
\boxed{\det\frac{\partial(Y,Z,W)}{\partial(t,\lambda,v)}=-a^3\in L^*.}
\tag{12}
\]
This cubic speed calibration must not be replaced by the \(-a^2\)
of the exact1122 chart.

## 4. The first two potential identities

Put \(d=r''\), \(m=k_\lambda\). With \(X\) fixed, subtract
\(q'X\,dY\) from the middle differential row and
\(r'X^2\,dY\) from the last one. The determinant becomes
\[
(dy+Xdt)\wedge
\bigl(dz+X\{(q''y+k_t)dt+m\,d\lambda\}\bigr)\wedge
\bigl(dw+X\,d\theta+X^2\{dy\,dt+d\lambda\}\bigr).
\tag{13}
\]
The symbol \(dy\,dt\) inside braces denotes the product
\(d\cdot y\cdot dt\); other occurrences of \(dy\) are the
differential of the first projection.

The coefficient of \(X^3\), in orientation
\(dt\wedge d\lambda\wedge dv\), is
\(-z_v+m\theta_v+\{(q''-dm)y+k_t\}y_v\).
Integration in the polynomial variable \(v\) gives
\[
z=m\theta+f(y),\qquad
f(U)=\frac{q''-dm}{2}U^2+k_tU+n,\quad n\in L.
\tag{14}
\]
Set \(B_1=m_t\theta+f_t(y)\), \(C_1=m_\lambda\theta+f_\lambda(y)\).
After subtracting \(f_U(y)\) times the first row in (13), the
middle row is \(m\{d\theta+X(dy\,dt+d\lambda)\}+B_1dt+C_1d\lambda\).
Its degree-two determinant coefficient is
\(m w_v+(B_1-dyC_1)y_v+C_1\theta_v\).
Because \(f_{\lambda U}=m_t-dU m_\lambda\), it integrates to
\[
m w+\frac{m_\lambda}{2}\theta^2+f_\lambda(y)\theta+P(y)=\ell,
\qquad \ell\in L,
\tag{15}
\]
where the complete polynomial is
\[
P(U)=\frac{d^2m_\lambda}{8}U^4
 +\frac{q'''-r'''m-3dm_t}{6}U^3
 +\frac{k_{tt}-dn_\lambda}{2}U^2+n_tU .
\tag{16}
\]
In particular \(P_U=f_t-dU f_\lambda\).
There has been no integration in a presumed rational coefficient field.

The cofactor of \(T_W(v)\) has degree-two coefficient \(m/J\).
Its other horizontal top coefficients vanish. Thus in this chart
\[
k_W=2\ \Longleftrightarrow\ m\ne0,
\qquad m\ne0\ \Longrightarrow\ N_W=-\frac m aN_Z.
\tag{17}
\]
When \(m=0\), the exact remaining shift is at most one.

## 5. Nonzero coupling gives a nonzero quartic whole-plane equation

Assume \(m\ne0\). Equations (14),(15) give \(z,w\in L[y,\theta]\),
while (14) gives \(\theta\in L[y,z,w]\). Therefore
\[
\boxed{L[y,\theta]=L[y,z,w]=L[v].}
\tag{18}
\]
Let \(U,V\) be formal plane variables, and put
\[
g(U,V)=\frac{\ell-P(U)-m_\lambda V^2/2-f_\lambda(U)V}{m},
\qquad C=m_\lambda V+f_\lambda(U).
\tag{19}
\]
Thus \(w=g(y,\theta)\), \(g_V=-C/m\), and
\(g_U=-(m_tV+f_t-dUC)/m\).
The coefficient of \(X\) in (13), after (14),(15), is
\[
\mathcal A(y,\theta)y_v+\mathcal B(y,\theta)\theta_v,
\quad
\mathcal A=-mg_t+mdU g_\lambda+Cg_U,
\quad \mathcal B=-mg_\lambda+Cg_V.
\tag{20}
\]
The two formal coefficients satisfy
\(\mathcal A_V=\mathcal B_U\). A complete polynomial primitive
can be defined without appealing to an implicit integrability claim:
\[
\begin{aligned}
\mathcal T(U,V)={}&
 \left(\frac{m_{\lambda\lambda}}6-\frac{m_\lambda^2}{2m}\right)V^3
 +\left(\frac{f_{\lambda\lambda}}2-\frac{3m_\lambda f_\lambda}{2m}\right)V^2\\
&+\left(P_\lambda-\ell_\lambda
       -\frac{m_\lambda(P-\ell)+f_\lambda^2}{m}\right)V+Q(U),\\
Q(U)={}&\int_0^U\left[-m(g_0)_t+mdT(g_0)_\lambda
                       -\frac{f_\lambda P_T}{m}\right]dT,
\quad g_0=(\ell-P)/m .
\end{aligned}
\tag{21}
\]
The integral is just polynomial integration in the formal variable
\(T\), with coefficients in \(L\). Differentiating (21), using
\(P_U=f_t-dUf_\lambda\) and \(f_{\lambda U}=m_t-dUm_\lambda\),
gives exactly \(\mathcal T_U=\mathcal A\),
\(\mathcal T_V=\mathcal B\). Hence
\(\mathcal T(y,\theta)=s\) for some \(s\in L\).

Make only the coefficient-field shear \(\psi=\theta-dy^2/2\).
The polynomial \(\mathcal H(U,V)=\mathcal T(U,V+dU^2/2)-s\)
has total degree at most four. For an explicit audit of all higher
cancellations, its nonconstant coefficients are the following:

| Monomial | Coefficient in \(\mathcal H\) |
| --- | --- |
| \(U^4\) | \((q''''-mr''''-4q'''m_t/m)/24\) |
| \(U^3V\) | \(-q'''m_\lambda/(6m)\) |
| \(U^3\) | \((mk_{ttt}-3k_{tt}m_t-n_\lambda q''')/(6m)\) |
| \(U^2V\) | \((mm_{tt}-m_\lambda k_{tt}-2m_t^2)/(2m)\) |
| \(U^2\) | \((mn_{tt}-k_{tt}n_\lambda-2n_tm_t)/(2m)\) |
| \(UV^2\) | \(m_{t\lambda}/2-3m_\lambda m_t/(2m)\) |
| \(UV\) | \((mn_{t\lambda}-m_\lambda n_t-2n_\lambda m_t)/m\) |
| \(U\) | \((\ell m_t-m\ell_t-n_\lambda n_t)/m\) |
| \(V^3\) | \(m_{\lambda\lambda}/6-m_\lambda^2/(2m)\) |
| \(V^2\) | \(n_{\lambda\lambda}/2-3m_\lambda n_\lambda/(2m)\) |
| \(V\) | \((\ell m_\lambda-m\ell_\lambda-n_\lambda^2)/m\) |

Its constant coefficient is \(-s\). These formulas follow by
expanding the explicit primitive (21), not by imposing a quartic
ansatz on the original map.

The polynomial \(\mathcal H\) is nonzero. To check this necessary
point, before the shear the constant determinant form is
\(dU\wedge\{m\,dV+B\,dt+C\,d\lambda\}\wedge dg\), with
\(B=m_tV+f_t\). Its coefficients on
\(dU\wedge dt\wedge d\lambda\),
\(dU\wedge dt\wedge dV\), and
\(dU\wedge d\lambda\wedge dV\) are, respectively,
\[
\frac C m\mathcal A+g_U\mathcal B,
\qquad \mathcal A+dU\mathcal B,
\qquad \mathcal B.
\tag{22}
\]
If \(\mathcal H\) vanished formally, its formal derivatives,
and hence \(\mathcal A,\mathcal B\), would vanish. Equation (22)
would make the actual scalar determinant zero, contrary to (12).
Thus this branch has the proved whole-plane conclusion
\[
\boxed{L[y,\psi]=L[v],\quad
0\ne\mathcal H\in L[U,V],\quad\deg\mathcal H\le4,
\quad\mathcal H(y,\psi)=0.}
\tag{23}
\]
The polynomial need not be irreducible or reduced. Its selected
irreducible plane component has degree at most four. This is not
an assertion about degrees of generators of the full original \(I\).

## 6. Zero coupling: recognition or an affine graph

Assume \(m=0\), and put \(\nu=n_\lambda\).
Equation (14) gives \(z=f(y)\), so \(L[y,w]=L[v]\).
Equation (15) becomes
\[
\nu\theta+P(y)=\ell,\qquad
P(U)=\frac{q'''}6U^3+\frac{k_{tt}-d\nu}{2}U^2+n_tU .
\tag{24}
\]
If \(\nu=0\) and \(y\notin L\), the nonconstant polynomial
\(y\in L[v]\) is transcendental over \(L\). Thus (24) forces
\(q'''=k_{tt}=n_t=0\). This makes \(f_t=f_\lambda=0\),
and the reduced middle differential row in (13), after subtracting
\(f_U(y)\) times the first, is zero. That contradicts (12).
Hence \(\nu=0\) forces \(y,z\in L\).

This last case has an actual endpoint. Extend \(N\) to \(A[u]\)
by \(Nu=0\), and define \(P_0=aN-(NX)E\). It preserves \(B\),
commutes with \(E\), and fixes \(X,Y,Z\). It is nonzero on
\(K\), since its restriction there is \(aN\). Thus its kernel
in the original polynomial ring is exactly \(\mathbb C[X,Y,Z]\):
as a derivation fixing those three coordinates it is a nonzero
multiple of \(\partial_W\). The actual three-ring endpoint of
Section 2 applies. No assertion that this multiple is \(E\)-fixed,
or that \(E\) commutes with \(\partial_W\), is needed.

If \(\nu\ne0\), set
\[
G(U)=\frac{\ell-P(U)}\nu,
\qquad\theta=G(y),\qquad \deg_U G\le3.
\tag{25}
\]
The remaining degree-one determinant coefficient is
\[
\nu w_v+\{f_t(y)G_\lambda(y)-\nu G_t(y)\}y_v=0.
\tag{26}
\]
All coefficient partials in this formula hold \(U\) fixed.
Polynomial integration in \(U\) gives
\[
w=J(y)+w_0,\quad w_0\in L,\qquad
J_U=G_t-(f_t/\nu)G_\lambda,
\qquad\deg J\le6.
\tag{27}
\]
Indeed \(f_t\) has degree at most two and \(G_\lambda\) at most
three. The difference in (27) has zero \(v\)-derivative, so its
constant belongs to \(L\). Whole-line return now gives
\(L[v]=L[y,w]=L[y]\), which forces
\(y=\alpha v+\beta\), \(\alpha\in L^*\).
This is an affine graph reduction, not yet recognition of its
remaining scalar determinant or actual-coordinate endpoint.

## 7. Precise remaining boundary

Under the retained recognition inputs, the new unresolved1123
cases can be separated without assuming an entry theorem:

- Principal full initial kernels of weights three through five
  not removed by the actual elementary gates in Section 1.
- Height-two frames with positive selected shifts and \(k_Z\le2\).
- The maximal height-two pivot \(k_Z=3\): the quartic whole-plane
  problem (23), or the affine graph (25)--(27) with \(\nu\ne0\).

This is not a claim that any remaining case is realizable or that
a minimizing frame must have the maximal pivot. Equal-bad-degree
arguments from257 cannot be imported by numerically relabeling the
last slot. An invariant of small original weighted complexity and
a small bound on all generators of the initial ideal are also
different claims.

The complete157,158,249,250 and257 sources were read. The new
potential formulas, their exact gradients and the quartic coefficient
table were independently reconstructed by unsaved algebra; they
remain ordinary mathematical identities, not finite certificates
of field descent or recognition. The actual endpoint in Section 2
uses the explicitly stated primary theorems. No source or frozen
packet was changed, and no saved checker was executed, imported
or compiled. No historical novelty, human expert certification,
arbitrary entry or unrestricted cancellation theorem is claimed.
