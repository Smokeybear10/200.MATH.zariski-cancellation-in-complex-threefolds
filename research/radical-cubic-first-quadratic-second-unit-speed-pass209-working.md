# The proper radical branch of projected degrees three and two has unit speed

Status: working restricted recognition theorem, with an original-ring
polynomial inverse. Under the supplied actual radical-chart hypotheses,
if the proper projected plane has original generator degrees \((3,2)\),
then \(EX\in\mathbb C^*\) and its invariant ring is a polynomial
three-ring. This is a companion to the
[degree-four first-generator theorem208](radical-quartic-first-projection-unit-speed-pass208-working.md),
not a change to that source or a general entry theorem.

## 1. Exact setup and the conductor fiber

Retain the full actual hypotheses of
[eliminant206](weight-four-radical-nonzero-r-eliminant-pass206-working.md):
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad A=\ker E,
\quad \deg_E(X,Y,Z,W)=(1,1,2,2),\\
a=EX\ne0,\quad \ker\theta_0=(\mathsf X^2\mathsf Z-\mathsf W^2),
\quad t=EY/a,\quad q=\rho^2,\\
Y=y+tX,\quad Z=z+(2\rho\vartheta+k)X+\rho^2X^2,
\quad W=w+\vartheta X+\rho X^2,\\
L/\mathbb C(t,\rho)\text{ finite},\quad A_L=L[v],\quad Nv=1,
\quad C=L[y,\vartheta]\subsetneq O=L[v],\\
\deg_vy=3,\quad\deg_v\vartheta=2,\quad
R=2\vartheta+k_\rho\ne0,\quad RO\subset C.
\end{gathered}
\tag{1}
\]
Both actual projected returns and \(J_v=-a^3\in L^*\) are retained.
The coefficient partials extend uniquely, commute, and have joint
constants \(\mathbb C\). Indeed \(dt,d\rho\) form a basis of
\(\Omega_{L/\mathbb C}\); an element killed by both partials is
algebraic over \(\mathbb C\), hence complex.

The exact-field conductor reduction206 gives a parameter \(s\)
with \(L[s]=O\) and \(C=L[s^2,s^3+c_0s]\), where \(c_0\in L\).
The original generator degrees give the more precise form
\[
\begin{gathered}
D_0=s^2+c_0,\quad V_c=-k_\rho/2,\quad
\vartheta=V_c+bD_0,\quad y=y_c+D_0(A_2+A_3s),\\
b,A_3\in L^*,\quad A_2,y_c\in L,\qquad R=2bD_0.
\end{gathered}
\tag{2}
\]
Indeed the original entries belong to the span of
\(1,s^2,s^3+c_0s,s^4\), and their conductor is \(D_0O\).
Degree two for \(\vartheta\) and conductor divisibility of \(R\)
give its displayed form. Degree three for \(y\) gives \(A_3\ne0\).
These changes occur over \(L\), not in the original four-ring.

## 2. The cofactor is constant

Let \(G\) be the irreducible plane equation and \(\mathcal H\)
the literal eliminant206. That note proves
\[
\mathcal H=GQ_1,\quad \deg G=3,\quad \deg Q_1\le2,\quad
0\ne Q_1(y,\vartheta)\mid R^3,\qquad
\mathcal H(U,V_c)=p(U)^2.
\tag{3}
\]
The center \(p(U)=S(U,V_c)-\ell\) is nonconstant and squarefree.
In particular \(p(y_c)=0\), since every root of \(R\) lies over
\((y_c,V_c)\).

Writing \(S_0=V-V_c\), formula (2) gives the explicit equation
\[
\bigl(b(U-y_c)-A_2S_0\bigr)^2
-A_3^2S_0^2(S_0/b-c_0)=0.
\tag{4}
\]
It is irreducible over \(L\): as a quadratic in \(U\), its
discriminant has the nonsquare linear factor \(S_0/b-c_0\).
When \(c_0=0\), the remaining odd power of \(S_0\) gives the
same conclusion. Its height-one evaluation kernel is therefore
exactly this principal ideal. For any scalar choice of \(G\),
\[
G(U,V_c)=g(U-y_c)^2\quad\text{with }g\in L^*.
\tag{5}
\]

Factor \(p=(U-y_c)p_1\). Squarefreeness gives \(p_1(y_c)\ne0\).
Restrict (3) to \(V=V_c\) and cancel \((U-y_c)^2\) in \(L[U]\):
\[
Q_1(U,V_c)=g^{-1}p_1(U)^2,\qquad Q_1(y_c,V_c)\ne0.
\tag{6}
\]
Every zero of \(R\), after algebraic closure if needed, has that
same plane image. Thus \(Q_1(y,\vartheta)\) has no common zero
with \(R\). Its divisibility in (3) makes it a unit of \(L[v]\),
say \(q_1\in L^*\). Hence \(Q_1-q_1\in(G)\), but its degree is
at most two, less than \(\deg G=3\). Therefore \(Q_1=q_1\).
We have proved \(\mathcal H=q_1G\) and \(\deg\mathcal H=3\).
This includes both the node and the double conductor root of a cusp.

## 3. Actual normalization and the remaining coefficients

The exact coefficients from eliminant206 are
\([U^4]\mathcal H=k_{tt}^2/4\) and
\(\mathcal H_5=4V^2H_3(k)\). Consequently \(k_{tt}=0\) and
every third partial of \(k\) vanishes. Joint constants give
\[
k=A_1t\rho+\frac{A_2'}2\rho^2+A_3't+A_4\rho+A_5,
\qquad A_1,A_2',A_3',A_4,A_5\in\mathbb C.
\tag{7}
\]
These constants are unrelated to the coefficients in (2).

The removal of (7) occurs in the actual ring. Apply the following
changes sequentially, relabeling after each: translate \(X\) by
\(-A_2'/4\), add \((A_1/2)Y+(A_4/2)X\) to \(W\), and subtract
\(A_3'Y+A_5X\) from \(Z\). A translation \(X'=X+s\) changes
\(k\) to \(k+2s\rho^2\). The \(W\)-change then changes \(k\)
by \(-A_1t\rho-A_4\rho\); the \(Z\)-change removes the rest.
Each has an elementary polynomial inverse with complex coefficients.

As in the fully read actual normalization208, these changes preserve
the entire initial map, the literal \(\partial_Z\), the selected
\(N\), \(L,t,\rho,a\), and the projected generator degrees and ring.
They also preserve \(R\): the changes in \(2\vartheta\) and
\(k_\rho\) cancel. Only lower-time-degree terms are added.
Relabel the resulting actual coordinates and assume \(k=0\).

The cofactor argument applies again. The quartic part of the now
cubic eliminant is
\(2n_{tt}U^2V^2+4n_{t\rho}UV^3+2n_{\rho\rho}V^4\).
It vanishes, so every second partial of \(n\) vanishes. The
nonconstant center is \(p(U)=n_tU-\ell\). Therefore
\[
n=\gamma t+n_1\rho+n_2,\qquad
\gamma\in\mathbb C^*,\quad n_1,n_2\in\mathbb C.
\tag{8}
\]

## 4. An affine generic parameter and the scalar determinant

The undivided potentials become
\[
\begin{gathered}
z=2\rho w+\vartheta^2+n,\qquad
2\vartheta(w+n_1/2)+\gamma y=\ell,\\
w^2+n_1w-\ell_ty-\ell_\rho\vartheta=m.
\end{gathered}
\tag{9}
\]
Set \(x=w+n_1/2\). The degrees of \(y,\vartheta\) in the middle
identity are three and two, so \(\deg_vx=1\). In the last identity
the only possible degree-three term is \(-\ell_ty\). Hence
\(\ell_t=0\). Put \(D=\ell_\rho\) and \(K=m+n_1^2/4\). Then
\[
x^2=D\vartheta+K,\qquad D\ne0,\qquad D_t=0,\qquad
\vartheta=(x^2-K)/D.
\tag{10}
\]
Nonconstancy of \(x\) proves \(D\ne0\). Here \(x\) is only an
affine generic parameter; original-ring regularity is not assumed.

In the differential coordinates \((t,\rho,x)\), calibration gives
\(J_x=-a^3/x_v\in L^*\), with \(x_v\in L^*\).
Use \(w=x-n_1/2\), \(y=(\ell-2\vartheta x)/\gamma\), and
\(z=2\rho x+\vartheta^2+\gamma t+n_2\). At fixed \(x\),
\(\vartheta_t=-K_t/D\) and
\(\vartheta_\rho=-(K_\rho+D_\rho\vartheta)/D\).
The last Jacobian row is \((0,0,1)\), and direct expansion gives
\[
J_x=-D+\frac{2(3x^2-K)K_t}{\gamma D}
       -\frac{2xK_\rho}{D}
       -\frac{2x(x^2-K)D_\rho}{D^2}.
\tag{11}
\]
The coefficient partials on \(L\) are unchanged. The displayed
derivatives of \(\vartheta,y,z,w\) hold \(x\) fixed, not \(v\).

The cubic, quadratic, and then linear coefficients in (11) force
\(D_\rho=0\), \(K_t=0\), and \(K_\rho=0\). Joint constants give
\[
D=\delta\in\mathbb C^*,\quad K=\kappa\in\mathbb C,\quad
\ell=\delta\rho+\ell_0,\quad \ell_0\in\mathbb C,\quad J_x=-\delta.
\tag{12}
\]
The relation \(\delta x_v=a^3\) alone does not make \(a\) a unit
of the original ring. The polynomial inverse is still necessary.

## 5. Both actual polynomial inverse orders

In the normalized original coordinates set
\[
U=X,\quad V=\gamma Y-\ell_0,\quad
Z_0=Z-n_2,\quad W_0=W+n_1/2.
\tag{13}
\]
This is an invertible affine change with complex coefficients.
Let \(\vartheta=(x^2-\kappa)/\delta\) and \(j=\vartheta+\rho U\).
The full original chart, not just its projection, becomes
\[
W_0=x+Uj,\quad Z_0=\gamma t+2\rho x+j^2,\quad
V=\delta\rho-2x\vartheta+\gamma tU.
\tag{14}
\]
For independent \(U,V,Z_0,W_0\), define
\[
\begin{gathered}
I=W_0^2+UV-U^2Z_0,\qquad J=(I-\kappa)/\delta,\\
\widehat x=W_0-UJ,\qquad
\widehat\rho=(V-UZ_0+2W_0J-UJ^2)/\delta,\\
\widehat t=(Z_0-2\widehat\rho\widehat x-J^2)/\gamma.
\end{gathered}
\tag{15}
\]
These are polynomials, dividing only the nonzero complex constants
\(\gamma,\delta\). Substituting (14) gives
\(I=x^2+\delta\rho U\), hence \(J=j\), then
\(\widehat x=x\), \(\widehat\rho=\rho\), and \(\widehat t=t\).
This is the first inverse order.

Conversely, (15) gives
\(\delta(J-\widehat\rho U)=\widehat x^2-\kappa\).
Thus the reconstructed \(\vartheta\) is \(J-\widehat\rho U\)
and the reconstructed \(j\) is \(J\). The \(W_0,Z_0\) identities
in (14) follow directly. For its last identity, substitution gives
\[
\delta\widehat\rho-2\widehat x(J-\widehat\rho U)
 +\gamma\widehat tU
=\delta\widehat\rho+UZ_0-2\widehat xJ-UJ^2=V.
\tag{16}
\]
This proves the reverse inverse order, and
\(B=\mathbb C[U,x,t,\rho]\) in the actual original polynomial ring.

The recovered \(x,t,\rho\) already belong to the invariant fraction
field of \(E\), and (15) makes them elements of \(B\). Hence
\(E\) kills them and \(EU=a\). Thus \(E=a\partial_U\), with
\(a\) independent of \(U\) because \(E^2U=0\). The global slice
now proves
\[
1=Eu=a\partial_Uu,\qquad
a\in B^*=\mathbb C^*,\qquad A=\mathbb C[x,t,\rho].
\tag{17}
\]
The actual normalizations preserved \(a\), so this is the speed
of the supplied frame, not an auxiliary generic model.

## Scope

Together with the degree-four companion208, this recognizes all
proper radical projected planes with \(\deg_v\vartheta=2\):
the conductor reduction206 excludes \(\deg_vy=2\), and the remaining
first-generator degrees are three and four. This leaves the
degree-three second-generator branches, the whole-plane case,
other leading sectors, and arbitrary entry.

No field rationality or coefficient-field coordinate lift was assumed.
The original inverse is the recognition step; neither cofactor purity
nor the scalar determinant alone supplies it. This note does not assert
unrestricted cancellation, global minimality, novelty, expert
certification, or formal proof-assistant verification. No saved checker
was executed, imported or compiled, and no earlier source, packet or
index was edited.
