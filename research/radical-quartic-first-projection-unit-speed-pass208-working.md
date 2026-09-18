# The quartic first-generator radical branch has unit speed

Status: working restricted recognition theorem with an actual polynomial
inverse. Under the full actual radical-chart hypotheses, if the projected
plane is proper and its original first generator has degree four, then
\(EX\) is a nonzero complex constant. Consequently its invariant ring is
a polynomial three-ring. The proof does not assume that any generic
parameter was originally a polynomial coordinate.

This is a branch theorem, not unrestricted cancellation. In particular,
it gives no entry into the supplied degree profile or leading kernel.

## 1. Exact hypotheses and the cofactor

Use the notation and full hypotheses of
[eliminant206](weight-four-radical-nonzero-r-eliminant-pass206-working.md):
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad A=\ker E,\\
\deg_E(X,Y,Z,W)=(1,1,2,2),\quad a=EX\ne0,\\
\ker\theta_0=(\mathsf X^2\mathsf Z-\mathsf W^2),\quad
q=\rho^2,\quad L/\mathbb C(t,\rho)\text{ finite},\\
A_L=L[v],\quad Nv=1,\quad C=L[y,\vartheta]\subsetneq L[v],\\
Y=y+tX,\quad Z=z+(2\rho\vartheta+k)X+\rho^2X^2,\quad
W=w+\vartheta X+\rho X^2,\quad \deg_vy=4 .
\end{gathered}
\tag{1}
\]
The exact coefficient partials commute. Their joint constants in \(L\)
are \(\mathbb C\): the differentials \(dt,d\rho\) form a basis of
\(\Omega_{L/\mathbb C}\), and an element with zero differential in a
finitely generated characteristic-zero field is algebraic over the
base field.

The fully written [local refinement208](radical-proper-projection-degree-refinement-pass208-working.md)
gives \(\deg_v\vartheta=2\) and \(k_{tt}=0\). Its proof uses the
actual potentials at the node or cusp, not plane normality. Let \(G\)
be the irreducible plane equation and \(\mathcal H\) the literal
eliminant206. Then
\[
\deg G=4,\quad \deg_U G=2,\quad
\mathcal H=GQ_1,\quad \deg Q_1\le1,\quad
\deg_U\mathcal H\le2,\quad 0\ne Q_1(y,\vartheta)\mid R^3,
\quad R=2\vartheta+k_\rho .
\tag{2}
\]
Degree in \(U\) in a polynomial domain shows \(Q_1\in L[V]\).
If \(Q_1\) is nonconstant, it is linear. Its evaluated linear
polynomial in \(\vartheta\) can divide \(R^3\) only when it is
proportional to \(2\vartheta+k_\rho\): two different translates of
the same nonconstant polynomial are coprime. Thus \(Q_1\) would
be proportional to \(2V+k_\rho\). This is impossible, since
\(\mathcal H(U,-k_\rho/2)=p(U)^2\) and the center \(p\) is
nonzero. Therefore \(Q_1\in L^*\), and \(\deg\mathcal H=4\).

The exact highest homogeneous term \(4V^2H_3(k)\) vanishes.
All third coefficient partials of \(k\) vanish. Together with
\(k_{tt}=0\) and the joint-constant fact this gives
\[
k=A_1t\rho+\frac{A_2}{2}\rho^2+A_3t+A_4\rho+A_5,
\qquad A_i\in\mathbb C .
\tag{3}
\]
For example \(k_{t\rho}\) and \(k_{\rho\rho}\) are joint constants;
subtracting their displayed quadratic primitive leaves constant
first partials and then a constant remainder.

## 2. Removing k in the actual polynomial ring

The following are actual elementary coordinate changes, not changes
with coefficients in \(L\). A constant translation \(X'=X+s\),
with the other coordinates unchanged, gives
\[
y'=y-st,\quad \vartheta'=\vartheta-2s\rho,\quad
\sigma'=\sigma-2s\rho^2,\quad k'=k+2s\rho^2 .
\tag{4}
\]
Thus \(s=-A_2/4\) removes the \(\rho^2\) term. In the resulting
coordinates, changing \(W\) to \(W+\alpha Y+\beta X\) replaces
\(\vartheta\) by \(\vartheta+\alpha t+\beta\), and hence replaces
\(k\) by \(k-2\alpha t\rho-2\beta\rho\). Take
\(\alpha=A_1/2,\ \beta=A_4/2\). Finally changing \(Z\) to
\(Z-A_3Y-A_5X\) removes the remaining terms.

These changes preserve the entire initial map and its kernel:
only lower-time-degree terms have been added. They preserve the
literal \(\partial_Z\), hence the selected \(N\), its field \(L\),
the ratios \(t,\rho\), and the speed \(a\). They preserve the
degrees four and two of \(y,\vartheta\), and the proper plane ring,
since the projected generators change only by elements of \(L\).
All changes have elementary polynomial inverses. Relabel the
resulting actual coordinates \(X,Y,Z,W\). From now on \(k=0\).

The same cofactor proof applies in this chart. Here the degree-four
part of the eliminant is
\[
2n_{tt}U^2V^2+4n_{t\rho}UV^3+2n_{\rho\rho}V^4 .
\tag{5}
\]
The top homogeneous part of \(G\) is proportional to \(V^4\).
One way to verify this precisely is to form the resultant of
\(y(v)-U\) and \(\vartheta(v)-V\), whose implicit irreducible
factor occurs once because the parametrization is birational.
Equivalently use its two sheets over the quadratic \(\vartheta\):
the terms \(U^2\) and the trace times \(U\) have ordinary degrees
at most three, and the norm has leading term proportional to
\(V^4\), since \(y\) has degree four. Therefore
\(n_{tt}=n_{t\rho}=0\). The center is \(p(U)=n_tU-\ell\);
its nonconstancy forces
\[
n=\gamma t+n_0,\quad
\gamma=n_t\in\mathbb C^*,\quad (n_0)_t=0 .
\tag{6}
\]
No rationality of \(n_0\) in \(\rho\) is assumed.

## 3. A conic produces an affine generic parameter

The undivided potentials become
\[
z=2\rho w+\vartheta^2+n,\qquad
2\vartheta w+\gamma y+n_\rho\vartheta=\ell,\qquad
w^2+n_\rho w+\frac{n_{\rho\rho}}2\vartheta^2
-\ell_ty-\ell_\rho\vartheta=m .
\tag{7}
\]
Set \(\eta=w+n_\rho/2\) and \(\lambda=\ell_t/\gamma\).
The second identity gives
\(y=(\ell-2\vartheta\eta)/\gamma\), so \(\deg_v\eta=2\).
It also gives \(L[\vartheta,\eta]=L[v]\), using the full
three-generator return in (1) and the first identity of (7).
Two quadratic polynomials generating \(L[v]\) have an affine,
nonconstant difference after cancelling their leading terms.
Write \(\eta=b\vartheta+\xi\) with \(b\in L^*\) and \(\xi\)
affine and nonconstant in \(v\).

Substituting the second identity in the third yields
\[
\eta^2+2\lambda\vartheta\eta
+\frac{n_{\rho\rho}}2\vartheta^2
-D\vartheta-K=0,\quad
D=\ell_\rho,\quad
K=m+\frac{n_\rho^2}{4}+\lambda\ell .
\tag{8}
\]
The quartic coefficient and then the cubic coefficient in \(v\)
force \(b=-\lambda\) and \(n_{\rho\rho}=2\lambda^2\).
In particular \(\lambda\ne0\). Thus
\[
x=\eta+\lambda\vartheta\text{ is affine and nonconstant in }v,
\qquad x^2=D\vartheta+K,\qquad D\ne0 .
\tag{9}
\]
The last assertion follows because \(x^2\notin L\).
Since \((n_{\rho\rho})_t=0\), one has \(\lambda_t=0\).
Writing \(\ell=\gamma\lambda t+f\) gives \(f_t=0\) and
\(D_t=\gamma\lambda_\rho\). At this stage all these are only
coefficient-field identities.

## 4. Calibration forces constant coefficients

Use \(t,\rho,x\) as differential coordinates. Although \(x\) was
obtained by an affine change with coefficients in \(L\), its
derivative \(x_v\) is a nonzero element of \(L\). The exact scalar
calibration therefore says
\[
J_x:=\det\frac{\partial(y,z,w)}{\partial(t,\rho,x)}
=-\frac{a^3}{x_v}\in L^* .
\tag{10}
\]
In these coordinates \(\vartheta=(x^2-K)/D\),
\(w=x-\lambda\vartheta-n_\rho/2\), and
\(y=(\ell-2\vartheta x+2\lambda\vartheta^2)/\gamma\).
For a transparent determinant calculation put
\(\omega=2\vartheta\,d\vartheta+\gamma\,dt+
2(x-\lambda\vartheta)d\rho\).
Direct differentiation of these expressions gives
\[
\begin{aligned}
dw&=dx-\lambda\,d\vartheta
-(\vartheta\lambda_\rho+\lambda^2)d\rho,\\
\gamma\,dy+2\vartheta\,dw-\lambda\omega
&=(D-2\lambda x)d\rho-2x\,d\vartheta,\\
D\,d\vartheta&=2x\,dx
-(K_t+\gamma\lambda_\rho\vartheta)dt
-(K_\rho+D_\rho\vartheta)d\rho .
\end{aligned}
\tag{11}
\]
The calibrated wedge is \(dy\wedge\omega\wedge dw\).
Expanding (11) and substituting \(\vartheta=(x^2-K)/D\),
the following sequential coefficients of \(\gamma D^3J_x\)
are sufficient:
\[
\begin{array}{c|c|c}
\text{coefficient}&\text{prior equalities used}&\text{value}\\ \hline
[x^4]&\text{none}&10\gamma D\lambda_\rho\\
[x^2]&\lambda_\rho=0&6D^2K_t\\
[x^3]&\lambda_\rho=K_t=0&-2\gamma D D_\rho\\
[x]&\lambda_\rho=K_t=D_\rho=0&
4\gamma D^3\lambda-2\gamma D^2K_\rho
\end{array}
\tag{12}
\]
Each must vanish by (10). Their nonzero denominators and the
joint-constant fact show successively
\[
\begin{gathered}
\lambda\in\mathbb C^*,\quad D=\delta\in\mathbb C^*,\quad
K=2\lambda\delta\rho+\kappa,\quad \kappa\in\mathbb C,\\
n=\gamma t+\lambda^2\rho^2+n_1\rho+n_2,\qquad
\ell=\gamma\lambda t+\delta\rho+\ell_0,\qquad
n_1,n_2,\ell_0\in\mathbb C .
\end{gathered}
\tag{13}
\]
Here \(D_t=\gamma\lambda_\rho=0\), \(K_t=0\), and
\(\lambda_t=0\) are essential to the joint-constant deductions.
The remaining constant determinant is \(J_x=-\delta\).
This alone does not make \(a\) a unit: it says
\(\delta x_v=a^3\). The actual inverse below is the missing step.

## 5. Explicit inverse in the original polynomial ring

All constants in (13) are complex, with
\(\gamma\delta\lambda\ne0\). The chart entries now read
\[
\begin{gathered}
\vartheta=\frac{x^2-2\lambda\delta\rho-\kappa}{\delta},
\quad w=x-\lambda\vartheta-\lambda^2\rho-\frac{n_1}{2},\\
y=\frac{\ell-2\vartheta x+2\lambda\vartheta^2}{\gamma},
\quad z=2\rho w+\vartheta^2+
\gamma t+\lambda^2\rho^2+n_1\rho+n_2 .
\end{gathered}
\tag{14}
\]
Make an invertible affine change of the actual original coordinates:
\[
U=X-\lambda,\quad W_0=W+n_1/2,\quad
V=\gamma Y-2\lambda Z-(\ell_0-2\lambda n_2),\quad
Z_0=Z-n_2 .
\tag{15}
\]
Set
\[
\begin{gathered}
\vartheta_0=(x^2-\kappa)/\delta,\quad
j=\vartheta_0+\rho U,\quad
T=\gamma t-4\lambda\rho\vartheta_0+4\lambda^2\rho^2 .
\end{gathered}
\tag{16}
\]
Substituting (14) and the full chart expansions (1), not just their
values at \(X=0\), gives
\[
\begin{aligned}
W_0&=x+Uj,\\
Z_0&=T+2\rho x+j^2-2\lambda\rho^2U,\\
V&=\delta\rho-2x\vartheta_0+TU-2\lambda\rho^2U^2 .
\end{aligned}
\tag{17}
\]
In particular \(W_0^2+UV-U^2Z_0=x^2+\delta\rho U\).

For independent \(U,V,Z_0,W_0\), define the following polynomials:
\[
\begin{gathered}
I=W_0^2+UV-U^2Z_0,\qquad J=(I-\kappa)/\delta,\\
\widehat x=W_0-UJ,\qquad
\widehat\rho=(V-UZ_0+2W_0J-UJ^2)/\delta,\\
\widehat T=Z_0-2\widehat\rho\widehat x-J^2
                 +2\lambda\widehat\rho^2U,\\
\widehat t=
(\widehat T+4\lambda\widehat\rho(\widehat x^2-\kappa)/\delta
                -4\lambda^2\widehat\rho^2)/\gamma .
\end{gathered}
\tag{18}
\]
Only nonzero complex constants are divided. In the forward order,
(17) gives \(J=j\), \(\widehat x=x\),
\(\widehat\rho=\rho\), \(\widehat T=T\), and
\(\widehat t=t\).

For the reverse order, direct expansion of (18) gives
\[
\delta(J-\widehat\rho U)=\widehat x^2-\kappa .
\tag{19}
\]
Thus the reconstructed \(\vartheta_0\) is
\(J-\widehat\rho U\), and the reconstructed \(j\) is \(J\).
The first two equations of (17) follow immediately from (18).
For the last one, substitute \(\widehat T\): the terms
in \(2\lambda\widehat\rho^2U^2\) cancel, leaving
\(\delta\widehat\rho+UZ_0-2\widehat xJ-UJ^2=V\),
which is exactly the definition of \(\widehat\rho\).
Then (16) recovers \(t\). These are both polynomial inverse orders.
The affine change (15) is also invertible, so
\[
B=\mathbb C[U,x,t,\rho] .
\tag{20}
\]
This equality has now been established in the actual original ring,
not merely its localization or fraction field.

## 6. Recognition and limits

The three recovered elements \(x,t,\rho\) belong to the invariant
fraction field of \(E\), and (18) proves that they are in \(B\).
Hence \(E\) kills them, while \(EU=EX=a\). On (20) this gives
\(E=a\partial_U\), and \(E^2U=0\) makes \(a\) independent of
\(U\). The global slice implies
\[
1=Eu=a\,\partial_Uu,\qquad
a\in B^*=\mathbb C^*,\qquad A=\mathbb C[x,t,\rho].
\tag{21}
\]
The actual changes in Section2 preserved the speed, so this is also
the speed of the supplied frame (1). In particular a nonunit-speed
proper radical frame cannot have first projected degree four.

This leaves the proper-plane degrees at most three, as well as the
whole-plane case and other leading-kernel sectors. No arbitrary-entry,
minimum-frame, unrestricted cancellation, or novelty theorem is claimed.
The coefficient-field conic and determinant calculations by themselves
are not recognition; the two polynomial inverse orders are essential.
Independent symbolic calculations of the determinant and its wedge
form support Section4, but are not a saved checker or a substitute for
the written degree, cofactor and coordinate arguments.
