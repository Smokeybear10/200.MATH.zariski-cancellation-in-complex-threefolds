# Recognition when the leading ratio is t-independent and R vanishes

Status: bounded working recognition theorem for a supplied actual
weight-four chart. If \(q_t=0\), \(q_{\rho\rho}\ne0\), and the
selected polynomial \(R\) is identically zero, the projected line
is affine in all three projected entries. An actual nice commuting
derivation then meets the invariant-coefficient criterion205.

This covers the zero-R branches with \(q=\rho^2\) and
\(q=1/\rho\), under their specified pivots and full initial kernels.
It neither proves that R vanishes nor recognizes their nonzero-R
branches.

## 1. Retained actual hypotheses

Use the actual setup of
[universal184](weight-four-universal-chart-potentials-pass184-working.md):
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\\
\deg_E(X,Y,Z,W)=(1,1,2,2),\\
a=EX,\quad b=EY,\quad e=E^2Z/2,\quad h=E^2W/2,\\
\ker\theta_0=(F),\qquad
\theta_0(\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
 =(a\tau,b\tau,e\tau^2,h\tau^2),\\
F\text{ irreducible of weight four},\qquad F_{\mathsf Z}\ne0.
\end{gathered}
\tag{1}
\]
Weights are \((1,1,2,2)\), the named generators are original
polynomial coordinates, and the displayed ideal is the entire
initial kernel. The choice of the quadratic-slot names matters
because it specifies the pivot.

The retained exact-shift and local-slice mechanisms give
\[
\begin{gathered}
0\ne N=[u^3](\partial_Z|_A)\in\operatorname{LND}_{\mathbb C}(A),
\qquad Na=Nb=Ne=Nh=0,\\
S=\ker_A N,\qquad L=\operatorname{Frac}S,\qquad A_L=L[v],\quad Nv=1,\\
t=b/a,\qquad \rho=h/a^2,\qquad q=e/a^2,\qquad
[L:\mathbb C(t,\rho)]<\infty.
\end{gathered}
\tag{2}
\]
The ratios \(t,\rho\) are algebraically independent. Their partials
extend uniquely and commute on the finite separable field \(L\),
then extend to \(L[v]\) fixing \(v\). No equality
\(L=\mathbb C(t,\rho)\) is assumed.

The actual Taylor projection and determinant calibration are
\[
\begin{gathered}
B_a=A_a[X],\qquad
Y=y+tX,\quad Z=z+\sigma X+qX^2,\quad
W=w+\vartheta X+\rho X^2,\\
y,z,w,\sigma,\vartheta\in L[v],\qquad
L[y,z,w]=L[v],\qquad \mathbb C(y,z,w)=L(v),\\
J(X)=J_0=-a^3\in L^*.
\end{gathered}
\tag{3}
\]
The determinant uses rows \(Y,Z,W\), columns \(t,\rho,v\), and
holds \(X\) fixed. In particular its scalar value is derived from
the actual selected partial. The element \(a\) need not be a unit
of the original ring.

The additional coefficient hypotheses are
\[
q_t=0,\qquad q_{\rho\rho}\ne0.
\tag{4}
\]
They are identities in the exact coefficient field. The first is
not a claim that \(q\) is rational in \(\rho\). It implies that
every mixed derivative of \(q\) involving \(t\) vanishes, because
the partials commute.

## 2. The complete specialized potentials

For \(c\in L\), set
\[
H_j(c;U,V)=\sum_{i=0}^j
\frac{c_{t^i\rho^{j-i}}}{i!(j-i)!}U^iV^{j-i}.
\tag{5}
\]
Coefficient partials keep \(U,V\) fixed before evaluation.
Universal184 supplies \(k,n,\ell,m\in L\) and the identities
\[
\begin{aligned}
\sigma&=q_\rho\vartheta+k,\\
z-q_\rho w&=f(y,\vartheta),
&f(U,V)&=\frac{q_{\rho\rho}}2V^2+k_tU+k_\rho V+n,\\
Rw+g_3(y,\vartheta)&=\ell,
&R&=q_{\rho\rho}\vartheta+k_\rho,\\
\frac{q_{\rho\rho}}2w^2+f_\rho(y,\vartheta)w
 +g_4(y,\vartheta)-\ell_t y-\ell_\rho\vartheta&=m,
\end{aligned}
\tag{6}
\]
where the full higher potentials are
\[
g_3(U,V)=\frac{q_{\rho\rho\rho}}6V^3+H_2(k;U,V)+H_1(n;U,V),
\qquad
g_4(U,V)=\frac{q_{\rho\rho\rho\rho}}{24}V^4
                  +H_3(k;U,V)+H_2(n;U,V).
\tag{7}
\]
The quadratic term in \(w\) in (6) has a nonzero coefficient.
It is essential below and is not replaced by an absent-W formula.

Write
\[
\begin{aligned}
\mathcal B&=k_{tt}y+k_{t\rho}\vartheta+n_t,\\
\mathcal C&=q_{\rho\rho}w
 +\frac{q_{\rho\rho\rho}}2\vartheta^2
 +k_{t\rho}y+k_{\rho\rho}\vartheta+n_\rho.
\end{aligned}
\tag{8}
\]
The remaining actual determinant identity is
\[
\left[dy\wedge
 (R\,d\vartheta+\mathcal B\,dt+\mathcal C\,d\rho)
 \wedge dw\right]_{dt\wedge d\rho\wedge dv}=-a^3.
\tag{9}
\]

## 3. The zero-R branch gives an affine projected line

Assume the additional branch condition
\[
R=0\quad\hbox{identically in }L[v].
\tag{10}
\]
Since \(q_{\rho\rho}\in L^*\), it follows that
\(\vartheta=-k_\rho/q_{\rho\rho}\in L\).
If \(y\) also belonged to \(L\), the last identity in (6) would
be a quadratic equation for \(w\in L[v]\) with coefficients in
\(L\) and nonzero leading coefficient. A polynomial of positive
\(v\)-degree cannot satisfy it: its squared term has uniquely
largest degree. Thus \(w\in L\), and the second identity of (6)
would imply \(z\in L\). This contradicts \(L[y,z,w]=L[v]\).
Hence \(y\) is nonconstant and therefore transcendental over \(L\).

The third identity of (6) now reads
\[
\frac{k_{tt}}2y^2+(k_{t\rho}\vartheta+n_t)y
 +\frac{q_{\rho\rho\rho}}6\vartheta^3
 +\frac{k_{\rho\rho}}2\vartheta^2+n_\rho\vartheta=\ell.
\tag{11}
\]
Its two positive-degree coefficients give \(k_{tt}=0\) and
\(k_{t\rho}\vartheta+n_t=0\). Consequently
\(\mathcal B=0\), and (9) factors as
\[
\mathcal C\,(y_t w_v-y_v w_t)=-a^3.
\tag{12}
\]
The two factors are elements of \(L[v]\). Their product lies in
\(L^*\), so \(\mathcal C\in L^*\). Solving (8) gives
\[
\begin{aligned}
w={}&-\frac{k_{t\rho}}{q_{\rho\rho}}y+
\frac{\mathcal C-(q_{\rho\rho\rho}/2)\vartheta^2
                  -k_{\rho\rho}\vartheta-n_\rho}{q_{\rho\rho}},\\
z={}&q_\rho w+\frac{q_{\rho\rho}}2\vartheta^2
                 +k_t y+k_\rho\vartheta+n.
\end{aligned}
\tag{13}
\]
Both are affine polynomials in \(y\) over \(L\). It follows that
\(L[y]=L[y,z,w]=L[v]\), so \(y\) has degree one in \(v\).
Thus all three projected entries are affine in the generic parameter,
and
\[
Ny\ne0,\qquad N^2y=N^2z=N^2w=0,
\qquad N\vartheta=N\sigma=0.
\tag{14}
\]
Here \(\sigma=q_\rho\vartheta+k\in L\). Division by
\(q_{\rho\rho}\) in (13) takes place only in the coefficient field.
It asserts no original-ring unit.

## 4. The actual derivation satisfies the recognition criterion

Extend \(N\) to \(B=A[u]\) by \(Nu=0\), so that it remains
locally nilpotent and commutes with \(E\). Define the actual
polynomial derivation
\[
P=aN-(NX)E.
\tag{15}
\]
There is no assumption that \(NX=0\). If \(X=x_0+au\), then
\(NX=Nx_0\in A\), because \(Na=0\). Direct computation gives
\(PX=0\), \(P|_A=aN\), and \([E,P]=0\); the latter uses
\(E(NX)=N(EX)=Na=0\).

To verify local nilpotence, pass to the actual presentation
\(B_a=A_a[X]\). There \(P\) fixes \(X\) and restricts to
\(aN\) on \(A_a\). Since \(Na=0\), this restriction is locally
nilpotent. Thus \(P\) is locally nilpotent on \(B_a\). It already
preserves \(B\) by (15), so its restriction is an LND of the
original ring. This argument does not assert that an arbitrary sum
of LNDs is locally nilpotent.

Use (3) and (14) to obtain
\[
\begin{gathered}
PY=aNy\ne0,\qquad PZ=aNz,\qquad PW=aNw,\\
P^2X=P^2Y=P^2Z=P^2W=0,\qquad
E(PY)=E(PZ)=E(PW)=0.
\end{gathered}
\tag{16}
\]
Indeed \(P\) fixes \(X\), and \(N\) annihilates
\(a,t,q,\rho,\sigma,\vartheta\). The three first-line values are
in \(\operatorname{Frac}A\) by their projected expressions and
are original polynomials because \(P\) preserves \(B\). They are
therefore E-invariant. The square-zero equalities follow from
\(Na=0\) and the second derivatives in (14), first on the
localization and hence in the original domain.

All hypotheses of
[the invariant-coefficient criterion205](nice-commuting-invariant-coefficients-recognition-pass205-working.md)
are now verified. It proves that \(E\) annihilates an ambient
polynomial coordinate and that \(A\simeq\mathbb C^{[3]}\).
Its argument supplies the primitive auxiliary slice and applies
the precise Dasgupta--Gupta, Daigle and Bhatwadekar--Gupta--Lokhande
endpoints. None of these gates is replaced here by a generic-line
coordinate or by regularity of an unexamined auxiliary kernel.

## 5. Two conditional specializations

For the supplied full initial kernel
\(\mathsf Z^2-\mathsf X^2\mathsf W\) in the original names,
interchange the bad-slot names to
\(\widehat Z=W\), \(\widehat W=Z\) before applying this note.
Then the pivot is the original \(\partial_W\), and
\[
\rho=e/a^2,\qquad q=h/a^2=\rho^2,
\qquad q_t=0,\quad q_{\rho\rho}=2,
\qquad R=2\vartheta+k_\rho.
\tag{17}
\]
Under the additional identity \(R=0\), this recovers and recognizes
the branch reduced in204. It does not replace (17)'s full initial
kernel assumption by its scalar leading relation.

For the supplied rank-two full initial kernel
\(\mathsf Z\mathsf W-\mathsf X^4\), use the original
\(\partial_Z\) pivot. The ratio relation gives
\[
q\rho=1,\qquad q=1/\rho,
\qquad q_t=0,\quad q_{\rho\rho}=2/\rho^3\ne0,
\qquad R=\frac{2\vartheta}{\rho^3}+k_\rho.
\tag{18}
\]
Again, the conclusion applies only if this selected \(R\) vanishes
identically. The field element \(\rho\) is nonzero; no polynomial
coordinate or original unit equal to \(\rho\) is assumed.

## 6. Scope

The theorem concerns supplied globally sliced exact1122 frames with
a full irreducible weight-four initial kernel and the additional
conditions (4) and (10). It does not classify which such frames have
\(R=0\), assert existence of either conditional subbranch above, or
address finite zeros of a nonzero \(R\).

The nonzero-R branches, other positive-rank kernels, height-two
initial kernels, higher minimum profiles and arbitrary entry remain
outside this note. There is no unrestricted cancellation conclusion.
The universal184 source and the complete criterion205 were freshly
read before this derivation. No saved checker was executed, imported
or compiled, and no older source or index was changed. The working
proof is not expert or proof-assistant certification and makes no
historical novelty claim.
