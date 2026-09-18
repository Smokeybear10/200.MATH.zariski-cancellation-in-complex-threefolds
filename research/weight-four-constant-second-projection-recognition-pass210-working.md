# Recognition with constant second projection and t-independent leading ratio

Status: bounded working recognition theorem. In the actual weight-four
chart, the conditions \(q_t=0\), \(q_{\rho\rho}\ne0\), and
\(\vartheta\in L\) imply that the original derivation fixes an ambient
polynomial coordinate. The nonzero-\(R\) case is proved here; the
zero-\(R\) case is the retained theorem205. No assumption that the
projected plane is already the whole line is needed.

In particular this recognizes the constant-\(\vartheta\) part of the
nonzero-return radical chart. It does not recognize its nonconstant
affine-\(\vartheta\) part or all whole projected planes.

## 1. Actual hypotheses and complete relevant potentials

Retain the supplied actual hypotheses of
[universal184](weight-four-universal-chart-potentials-pass184-working.md):
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\\
\deg_E(X,Y,Z,W)=(1,1,2,2),\qquad a=EX\ne0,\\
\ker\theta_0=(F),\qquad F\text{ irreducible of weight four},
\qquad F_{\mathsf Z}\ne0,\\
\theta_0(\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
 =(a\tau,(EY)\tau,(E^2Z/2)\tau^2,(E^2W/2)\tau^2).
\end{gathered}
\tag{1}
\]
Weights are \((1,1,2,2)\). The displayed ideal is the full initial
kernel and the named four entries are actual polynomial coordinates.
The pivot is the literal original partial \(\partial_Z\).

The exact selected derivation and coefficient field are
\[
\begin{gathered}
0\ne N=[u^3](\partial_Z|_A)\in\operatorname{LND}(A),\qquad
Na=N(EY)=N(E^2Z/2)=N(E^2W/2)=0,\\
L=\operatorname{Frac}\ker_A N,\qquad A_L=L[v],\qquad Nv=1,\\
t=EY/a,\quad \rho=(E^2W/2)/a^2,\quad q=(E^2Z/2)/a^2,\quad
[L:\mathbb C(t,\rho)]<\infty.
\end{gathered}
\tag{2}
\]
The independent coefficient partials on \(L\) extend those on
\(\mathbb C(t,\rho)\), commute, and fix \(v\) on \(L[v]\).
Their joint constants are \(\mathbb C\). No rationality of \(L\)
is imposed.

The actual Taylor chart gives
\[
\begin{gathered}
B_a=A_a[X],\quad
Y=y+tX,\quad Z=z+\sigma X+qX^2,\quad
W=w+\vartheta X+\rho X^2,\\
y,z,w,\sigma,\vartheta\in L[v],\qquad
L[y,z,w]=L[v],\qquad \mathbb C(y,z,w)=L(v),\\
J(X)=J_0=-a^3\in L^*.
\end{gathered}
\tag{3}
\]
These are the actual projection and calibration, not formal
coefficient hypotheses offered in place of an original frame.

Assume additionally
\[
q_t=0,\qquad q_{\rho\rho}\ne0,\qquad \vartheta\in L.
\tag{4}
\]
For independent formal \(U,V\), put
\(H_j(c)=\sum_{i=0}^j c_{t^i\rho^{j-i}}U^iV^{j-i}/(i!(j-i)!)\).
The full relevant universal potentials specialize to
\[
\begin{gathered}
\sigma=q_\rho\vartheta+k,\qquad
z=q_\rho w+\frac{q_{\rho\rho}}2\vartheta^2+k_ty+k_\rho\vartheta+n,\\
Rw+g_3(y,\vartheta)=\ell,\qquad
R=q_{\rho\rho}\vartheta+k_\rho,\\
\frac{q_{\rho\rho}}2w^2+f_\rho(y,\vartheta)w
 +g_4(y,\vartheta)-\ell_t y-\ell_\rho\vartheta=m,\\
f_\rho(U,V)=\frac{q_{\rho\rho\rho}}2V^2
                +k_{t\rho}U+k_{\rho\rho}V+n_\rho,\\
g_3(U,V)=\frac{q_{\rho\rho\rho}}6V^3+H_2(k)+H_1(n),\\
g_4(U,V)=\frac{q_{\rho\rho\rho\rho}}{24}V^4+H_3(k)+H_2(n),
\qquad k,n,\ell,m\in L.
\end{gathered}
\tag{5}
\]
The higher \(\rho\)-derivatives of \(q\) and the quadratic \(w\)
term have not been dropped. All coefficient partials in (5) are
formed before evaluating \(U=y,V=\vartheta\).

## 2. A constant second projection forces an affine projected line

If \(R=0\), the complete
[t-independent zero-return theorem205](weight-four-t-independent-zero-r-recognition-pass205-working.md)
already proves the assertion. For the new part, assume \(R\ne0\).
By (4), \(R\) is now a scalar in \(L^*\), not an asserted unit of
the original ring.

If \(y\in L\), the third potential in (5) makes \(w\in L\).
The second then makes \(z\in L\), contradicting (3).
Thus \(y\) is nonconstant in \(v\), and hence transcendental over
\(L\). Solving the third potential gives
\[
w=A_2y^2+A_1y+A_0,\qquad
A_i\in L,\qquad A_2=-\frac{k_{tt}}{2R}.
\tag{6}
\]
The second potential makes \(z\in L[y]\) as well. Consequently
\[
L[y]=L[y,z,w]=L[v],
\qquad \deg_v y=1.
\tag{7}
\]
No original-ring coordinate conclusion follows from (7) alone.

Substitute (6) into the fourth potential, treating \(y\) as an
independent polynomial variable over \(L\). Since \(\vartheta\in L\),
\(f_\rho(y,\vartheta)\) has degree at most one in \(y\),
and \(g_4(y,\vartheta)\) has degree at most three in \(y\).
The coefficient of \(y^4\) is therefore exactly
\[
\frac{q_{\rho\rho}}2 A_2^2=0.
\tag{8}
\]
The nonzero hypothesis on \(q_{\rho\rho}\) gives \(A_2=0\) and
\(k_{tt}=0\). Thus \(w\), and then \(z\), are affine in \(y\).
Together with (7) this proves
\[
Ny\ne0,\qquad N^2y=N^2z=N^2w=0,\qquad
N\vartheta=N\sigma=0.
\tag{9}
\]
The last identity uses \(\sigma=q_\rho\vartheta+k\in L\).

## 3. The original-ring nice derivation and recognition

Extend \(N\) from \(A\) to \(B=A[u]\) by \(Nu=0\), and define
\[
P=aN-(NX)E .
\tag{10}
\]
This is an original polynomial derivation. It is not a merely
generic derivative. The extension of \(N\) is locally nilpotent
and commutes with \(E\). Writing \(X=x_0+au\), with \(x_0\in A\),
gives \(NX=Nx_0\in A\), since \(Na=0\). Hence
\[
PX=0,\qquad P|_A=aN,\qquad [E,P]=0,\qquad Pa=0.
\tag{11}
\]

Local nilpotence of \(P\) follows in the actual presentation
\(B_a=A_a[X]\): it fixes \(X\), and its restriction \(aN\) to
\(A_a\) is locally nilpotent because \(Na=0\).
Its restriction to the preserved subring \(B\) is therefore an
LND. This does not rely on a general assertion about sums of LNDs.

Equation (9) and the actual expansions (3) give
\[
PY=aNy\ne0,\qquad PZ=aNz,\qquad PW=aNw,
\qquad P^2X=P^2Y=P^2Z=P^2W=0.
\tag{12}
\]
These equalities can first be calculated in \(B_a\) and then hold
in \(B\). In particular each right side in the first three
equalities, although expressed in the invariant fraction field,
is an actual polynomial. Therefore
\[
E(PY)=E(PZ)=E(PW)=0.
\tag{13}
\]
Every hypothesis of the fully read
[invariant-coefficient criterion205](nice-commuting-invariant-coefficients-recognition-pass205-working.md)
is now verified for the original pair \(E,P\). That criterion
constructs a primitive auxiliary slice, obtains a polynomial
three-variable kernel, and applies the stated Daigle and
Bhatwadekar--Gupta--Lokhande endpoints. It proves that \(E\)
annihilates an ambient polynomial coordinate of \(B\) and that
\[
\boxed{A\simeq\mathbb C^{[3]}.}
\tag{14}
\]
This use includes the regularity supplied by the original global
slice. It does not assume that the original slice belongs to
the auxiliary kernel or that \(a\) is an original-ring unit.

## 4. Radical specialization and the nonconstant boundary

For the supplied full initial kernel
\(\mathsf X^2\mathsf Z-\mathsf W^2\), the literal selected
\(\partial_Z\) chart has \(q=\rho^2\).
Hence (4)'s coefficient conditions hold, and every branch with
\(\vartheta\in L\) is recognized. In the nonzero-\(R\) case the
plane is whole by (7), so this closes one whole-plane boundary.
The full kernel \(\mathsf Z\mathsf W-\mathsf X^4\), with the
same stated pivot, gives \(q=1/\rho\) and is another conditional
specialization. Its nonconstant-\(\vartheta\) branches are not
included.

There is an exact limitation on reusing this auxiliary derivation.
Without assuming \(N\vartheta=0\), the same actual definition (10)
and the t-independent chart give
\[
\begin{gathered}
PY=aNy,\qquad
PW=a(Nw+X N\vartheta),\qquad
PZ=a(Nz+q_\rho X N\vartheta),\\
E(PY)=0,\qquad E(PW)=a^2N\vartheta,\qquad
E(PZ)=a^2q_\rho N\vartheta .
\end{gathered}
\tag{15}
\]
All these identities hold in the original fraction field, and the
left sides are original polynomials. Thus whenever \(\vartheta\)
is nonconstant in \(v\), in particular when it is an affine
generic parameter, \(E(PW)\ne0\). Criterion205 cannot be invoked
for this \(P\) without a new argument or a different actual
derivation. This is an applicability boundary, not a failure of
recognition or a nonexistence statement about other derivations.

No generic parameter is declared an ambient coordinate, and no
coefficient-field scalar is promoted to an original unit. This
note does not settle all whole-plane branches, arbitrary entry,
minimum time profiles, or unrestricted cancellation. Universal184,
both retained205 sources, and the radical eliminant206 were fully
read before the argument. No saved checker was executed, imported
or compiled; no earlier proof or index was edited. The result is
working mathematics, not expert or proof-assistant certification
or historical novelty clearance.
