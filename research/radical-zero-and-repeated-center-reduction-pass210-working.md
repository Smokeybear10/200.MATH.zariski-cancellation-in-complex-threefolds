# Zero and repeated centers in the actual radical chart

Status: working restricted recognition and exclusion. Under the supplied
actual radical hypotheses, an identically zero center forces a constant
second projection and is recognized by the constant-projection theorem210.
A nonzero repeated-quadratic center cannot occur. The latter conclusion
uses an irreducible polynomial in the original four-ring, not merely
the equality of a generic projected ring with its normalization.

## 1. Exact setup and center identities

Retain the actual hypotheses of
[universal184](weight-four-universal-chart-potentials-pass184-working.md)
and [eliminant206](weight-four-radical-nonzero-r-eliminant-pass206-working.md):
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad A=\ker E,\quad
\deg_E(X,Y,Z,W)=(1,1,2,2),\\
a=EX\ne0,\qquad
\ker\theta_0=(\mathsf X^2\mathsf Z-\mathsf W^2),\qquad q=\rho^2,\\
0\ne N=[u^3](\partial_Z|_A),\quad
L=\operatorname{Frac}\ker_A N,\quad A_L=L[v],\quad Nv=1,\\
[L:\mathbb C(t,\rho)]<\infty,\qquad
Y=y+tX,\quad Z=z+(2\rho\vartheta+k)X+\rho^2X^2,\quad
W=w+\vartheta X+\rho X^2,\\
L[y,z,w]=L[v],\quad \mathbb C(y,z,w)=L(v),\quad
R=2\vartheta+k_\rho\ne0,\quad J_0=-a^3\in L^* .
\end{gathered}
\tag{1}
\]
The initial ideal is the entire kernel, not one identity. The bad-slot
names specify the actual selected partial. The independent coefficient
partials commute; no rationality of \(L\) is assumed.

For formal \(U,V\), set
\[
\begin{gathered}
\mathcal R=2V+k_\rho,\qquad
S=\frac{k_{tt}}2U^2+k_{t\rho}UV+\frac{k_{\rho\rho}}2V^2
       +n_tU+n_\rho V,\qquad b_0=S_V,\\
T=\ell-S,\qquad Q_0=H_3(k)+H_2(n)-\ell_tU-\ell_\rho V-m,\\
\mathcal P=\mathcal R W_0+S-\ell,\qquad
\mathcal K=W_0^2+b_0W_0+Q_0,\qquad
\mathcal H=T^2+\mathcal R b_0T+\mathcal R^2Q_0 .
\end{gathered}
\tag{2}
\]
Here \(k,n,\ell,m\in L\), and \(H_j\) denotes the divided Taylor
polynomial of degree \(j\) from universal184. The actual third and
fourth potentials are \(\mathcal P(y,\vartheta,w)=
\mathcal K(y,\vartheta,w)=0\). The second is
\[
z=2\rho w+\vartheta^2+k_ty+k_\rho\vartheta+n .
\tag{3}
\]
Define the center and its linear quotient by
\[
V_c=-k_\rho/2,\qquad p(U)=S(U,V_c)-\ell,\qquad
S-\ell=p(U)-\mathcal R D(U,V),\quad \deg D\le1 .
\tag{4}
\]
Thus \(R\{w-D(y,\vartheta)\}+p(y)=0\).
The exact gradient and determinant identities needed below are
\[
\begin{gathered}
B_1=-R D_U(y,\vartheta)+p'(y),\qquad
C_1=2(w-D(y,\vartheta))-R D_V(y,\vartheta),\\
J_0=\left[dy\wedge(R\,d\vartheta+B_1dt+C_1d\rho)
                   \wedge dw\right]_{dt\wedge d\rho\wedge dv},\\
\mathcal H_V(y,\vartheta)=-R(C_1^2+R\Lambda_\rho),\qquad
\Lambda_\rho=\ell_\rho-S_\rho(y,\vartheta)-k_{\rho\rho}w .
\end{gathered}
\tag{5}
\]
All formal gradients precede evaluation. In \(S_\rho\), only
coefficients are differentiated before evaluation.

Write \(O=L[v]\) and \(C=L[y,\vartheta]\). Eliminant206 proves
\[
\begin{gathered}
O=C+Cw,\quad \operatorname{Frac}C=L(v),\quad RO\subset C,\\
0\ne\mathcal H=GQ,\quad
\ker(L[U,V]\longrightarrow O)=(G),\quad
G\text{ simple in }\mathcal H,\quad 0\ne Q(y,\vartheta)\mid R^3,\\
\deg\mathcal H\le5,\quad
\deg G=\max(\deg_vy,\deg_v\vartheta),\quad
\deg_U G=\deg_v\vartheta\ \text{if }\vartheta\notin L,\\
[U^4]\mathcal H=k_{tt}^2/4,\quad
\mathcal H_5=4V^2H_3(k),\quad
H_3(k)=0\ \Longrightarrow\
\mathcal H_4=H_2(k)^2-2VH_1(k_\rho)H_2(k)+4V^2H_2(n).
\end{gathered}
\tag{6}
\]

## 2. Zero center: the actual determinant forces constant projection

Assume \(p=0\) in \(L[U]\). Since \(R\ne0\), (4) gives
\(w=D(y,\vartheta)\). Consequently
\[
B_1=-R D_U(y,\vartheta),\quad C_1=-R D_V(y,\vartheta),\qquad
J_0=R\left[dy\wedge
 (d\vartheta-D_Udt-D_Vd\rho)\wedge dw\right]_{dt\wedge d\rho\wedge dv}.
\tag{7}
\]
The bracket is in \(L[v]\). Since \(J_0\in L^*\), both factors
are units of \(L[v]\). Therefore \(R\in L^*\) and
\(\vartheta\in L\). This is stronger than generic whole-plane return.

The candidate coefficient formulas also hold over the exact field.
Put \(K=\ker_L\partial_t\), and let primes mean \(\partial_\rho\).
The coefficients of \(p=0\) give successively
\[
\begin{gathered}
k=tA+B,\quad A,B\in K,\qquad
b=k_\rho=tA'+B',\quad c=k_{\rho\rho}=tA''+B'',\\
n=b^2/4+n_0,\quad n_0\in K,\qquad
\ell=-cb^2/8-bn_0'/2,\\
\xi=\vartheta+b/2,\qquad
w=-\frac{A'}2y-\frac c4\xi-\frac{n_0'}2,\\
z=\xi^2+(A-\rho A')y+n_0-\rho n_0'-\frac{\rho c}{2}\xi .
\end{gathered}
\tag{8}
\]
Indeed \(k_{tt}=0\); the coefficient of \(U\) says
\(n_t-bk_{t\rho}/2=0\), giving \(n_0\); the constant coefficient
gives \(\ell\). Dividing \(S-\ell\) by \(2V+b\) gives \(w\),
and (3) gives \(z\). None of \(A,B,n_0\) is assumed complex or
rational in \(\rho\).

The fully read
[constant-second-projection theorem210](weight-four-constant-second-projection-recognition-pass210-working.md)
now applies, since \(q_t=0\) and \(q_{\rho\rho}=2\ne0\).
It proves that all three projected entries are affine on the line,
then constructs the actual nice commuting derivation
\(P=aN-(NX)E\) with E-invariant coordinate coefficients.
Criterion205 supplies an ambient E-invariant coordinate and
\[
p=0\quad\Longrightarrow\quad A\simeq\mathbb C^{[3]} .
\tag{9}
\]
The original-ring endpoint, not a claim of regularity for the
coefficients in (8), is the recognition step.

## 3. Repeated center: a single double return root

Suppose
\[
p(U)=\kappa(U-U_0)^2,\qquad
\kappa=k_{tt}/2\in L^*,\quad U_0\in L .
\tag{10}
\]
If \(\vartheta\in L\), theorem210 forces \(k_{tt}=0\),
a contradiction. Thus \(R\) is nonconstant in this hypothetical branch.

The cone entries \(R,y-U_0,-(w-D)/\kappa\) have product relation
\(R[-(w-D)/\kappa]=(y-U_0)^2\) and generate \(O\).
Their first two degrees are at most five. If all three vanished
at one point, the middle-row coefficients \(B_1,C_1,R\) in (5)
would vanish there, contradicting \(J_0\in L^*\).
The fully read
[vertex-free degree-five cone lemma184](vertex-free-quintic-cone-projection-pass184-working.md)
therefore gives \(L[R,y-U_0]=O\), equivalently \(C=O\).

At a root of \(R\) over an algebraic closure, \(y=U_0\) and
\(w-D\ne0\). Hence
\(\operatorname{ord}R=2\operatorname{ord}(y-U_0)\), so
\(\vartheta_v=R_v/2=0\). The equality \(L[y,\vartheta]=L[v]\)
implies immersion: differentiate a polynomial expression for \(v\).
Thus \(y_v\ne0\) there, and every root of \(R\) has order two.
That same ring equality implies injectivity after algebraic closure.
All roots map to \((U_0,V_c)\), so there is only one distinct root.
It is in \(L\), by the coefficient of one degree below the leading
term of \(R\). For an affine shift \(x=v-s\) over \(L\),
\[
R=r x^2,\quad r\in L^*,\qquad \deg_v\vartheta=2,\qquad
y(0)=U_0,\quad y_x(0)\ne0 .
\tag{11}
\]

## 4. The finite fiber and gradient force a quadratic k

Normalize \(G\) to be monic in \(U\). The free
\(L[\vartheta]\)-module \(O\), with basis \(1,x\), has multiplication
by \(y\) as an endomorphism. Its characteristic polynomial has
degree two, equal to the minimal degree by \(L(y,\vartheta)=L(x)\);
it is \(G\). At \(V=V_c\) this is multiplication in \(L[x]/(x^2)\).
Both eigenvalues are \(U_0\), including the nilpotent part, so
\[
G(U,V_c)=(U-U_0)^2,\qquad
Q(U,V_c)=\kappa^2(U-U_0)^2 .
\tag{12}
\]
No reduced-fiber assumption is made. Thus \(\deg Q\ge2\);
(6) implies \(\deg G\le3\), hence \(\deg_vy\le3\).

Write \(y=U_0+b x+a_2x^2+a_3x^3\), \(b\ne0\).
Then \(L[x^2,y]=L[x^2]\oplus x(b+a_3x^2)L[x^2]\).
Equality with \(L[x]\) forces \(a_3=0\). Consequently
\[
\begin{gathered}
y=U_0+b x+a_2x^2,\quad b\in L^*,\qquad
\vartheta=V_c+r x^2/2,\\
G=(U-U_0-s_0(V-V_c))^2-\mu(V-V_c),\qquad
s_0=2a_2/r,\quad \mu=2b^2/r\ne0 .
\end{gathered}
\tag{13}
\]
This monic relation is irreducible and is the exact plane equation.
At \(x=0\), \(G_V=-\mu\ne0\) and \(C_1=2(w-D)\ne0\).
The evaluated gradient in (5) has order exactly two there.
Using \(\mathcal H_V(y,\vartheta)=Q(y,\vartheta)G_V(y,\vartheta)\)
shows that \(Q(y,\vartheta)\) also has order exactly two.
Its only possible roots lie at zero, since it divides \(R^3\).
Thus \(Q(y,\vartheta)=\eta R\), with \(\eta\in L^*\).

The polynomial \(Q-\eta\mathcal R\) lies in \((G)\).
Because \(\deg G=2\) and \(\deg Q\le3\), it equals \(GF_1\)
with \(\deg F_1\le1\). Restricting to (12) gives
\[
Q=\eta\mathcal R+GF_1,\qquad
F_1=\kappa^2+d_0(V-V_c),\qquad
\mathcal H=\eta\mathcal R G+F_1G^2 .
\tag{14}
\]
If \(d_0\ne0\), its degree-five part is
\(d_0V(U-s_0V)^4\), with nonzero \(U^4V\) coefficient.
But \(\mathcal H_5=4V^2H_3(k)\) is divisible by \(V^2\).
Therefore
\[
d_0=0,\qquad \mathcal H=\eta\mathcal R G+\kappa^2G^2,\qquad H_3(k)=0 .
\tag{15}
\]

## 5. Actual normalization preserves the center multiplicity

The joint constants of the coefficient partials in \(L\) are
\(\mathbb C\): \(dt,d\rho\) form a basis of
\(\Omega_{L/\mathbb C}\), and a zero differential in a finitely
generated characteristic-zero field implies algebraicity over
the base field. All third partials of \(k\) vanish, so
\[
k=\kappa t^2+A_1t\rho+\frac{A_2}{2}\rho^2+A_3t+A_4\rho+A_5,
\qquad \kappa,A_i\in\mathbb C,\quad\kappa\ne0 .
\tag{16}
\]
Remove the unwanted terms sequentially by the actual changes:
translate \(X\) by \(-A_2/4\); add
\((A_1/2)Y+(A_4/2)X\) to \(W\); subtract \(A_3Y+A_5X\)
from \(Z\). Each inverse is the opposite elementary change.

Here is explicit coefficient transport, including the center gate.
For \(X'=X+s\), comparing full chart expansions gives
\[
\begin{gathered}
y'=y-st,\quad\vartheta'=\vartheta-2s\rho,\quad
w'=w-s\vartheta+s^2\rho,\quad k'=k+2s\rho^2,\\
n'=n+s(tk_t+2\rho k_\rho-k)+3s^2\rho^2 .
\end{gathered}
\tag{17}
\]
Substitution of these formulas in the third potential shows that
its new polynomial, evaluated at
\((U-st,V-2s\rho,W_0-sV+s^2\rho)\), equals the old one:
the difference before subtracting \(\ell'\) is a scalar in \(L\),
and its evaluation is absorbed by the uniquely determined \(\ell'\).
Thus \(R'=R\) and \(p'(U-st)=p(U)\), where the prime on \(p\)
means the new polynomial, not a derivative.

For \(W'=W+\alpha Y+\beta X\), put \(l=\alpha t+\beta\).
The transport is
\[
y'=y,\quad\vartheta'=\vartheta+l,\quad w'=w+\alpha y,\quad
k'=k-2\rho l,\quad n'=n-k_\rho l+l^2 .
\tag{18}
\]
The same direct third-potential substitution gives \(R'=R\)
and \(p'=p\). For \(Z'=Z-CY-FX\), one has
\(k'=k-Ct-F\), \(n'=n\), with \(S,\ell,R,p\) unchanged.
Equations (17)--(18) verify that the repeated center remains repeated,
rather than assuming that any change of chart preserves this property.

All these maps have complex coefficients and preserve the exact
profile and full initial map by adding lower-time-degree terms.
Their inverses keep old \(X,Y,W\) independent of new \(Z\),
with old \(Z\) equal to new \(Z\) plus a polynomial in \(X,Y\).
Thus the literal \(\partial_Z\), selected \(N\), \(L,t,\rho,a\)
remain unchanged. The projected generators change only by scalars
in \(L\), preserving \(C=O\) and their degrees.
Relabel the resulting actual coordinates and take \(k=\kappa t^2\).

Repeat the preceding cofactor argument in this chart.
The quartic part of (15) is \(\kappa^2(U-s_0V)^4\).
On the other hand the literal identity (6) gives
\[
\mathcal H_4=\kappa^2U^4+2n_{tt}U^2V^2+
4n_{t\rho}UV^3+2n_{\rho\rho}V^4 .
\tag{19}
\]
The zero \(U^3V\) coefficient forces \(s_0=0\), so \(y\) is affine.
The other coefficients force all second partials of \(n\) to vanish.
Joint constants now give
\[
n=\alpha t+\beta\rho+\gamma,\quad
\alpha,\beta,\gamma\in\mathbb C,\qquad
p(U)=\kappa U^2+\alpha U-\ell .
\tag{20}
\]
Its repeated root forces
\(\ell=-\alpha^2/(4\kappa)\in\mathbb C\) and
\(U_0=-\alpha/(2\kappa)\).

## 6. A square identity contradicts the original polynomial ring

The fourth potential is now \(w^2+\beta w=m\in L\).
It forces \(w\in L\), since otherwise the square has uniquely
highest positive \(v\)-degree. The third and second give
\[
c_0=2w+\beta\in L,\quad y_1=y+\frac{\alpha}{2\kappa},\qquad
c_0\vartheta=-\kappa y_1^2,\qquad
z=\vartheta^2+2\kappa t y_1+c_0\rho+\gamma .
\tag{21}
\]
Here \(c_0\ne0\), since \(y_1\) is nonconstant.

Use actual affine translates
\(Y_1=Y+\alpha/(2\kappa)\), \(W_1=2W+\beta\), \(Z_1=Z-\gamma\).
The full chart, not only its projection at \(X=0\), becomes
\[
\begin{gathered}
Y_1=y_1+tX,\qquad W_1=c_0+2\vartheta X+2\rho X^2,\\
Z_1=(\vartheta+\rho X)^2+2\kappa t y_1+\kappa t^2X+c_0\rho,\\
\boxed{c_0^2=W_1^2+4\kappa XY_1^2-4X^2Z_1}.
\end{gathered}
\tag{22}
\]
Expanding the right side cancels its terms of degrees two through
four in \(X\). Its linear term is
\(4X(c_0\vartheta+\kappa y_1^2)=0\) by (21).
This is an identity in the original fraction field.

The polynomial on the right is irreducible in
\(\mathbb C[X,Y_1,Z_1,W_1]\). It is linear in \(Z_1\) and primitive
over the UFD \(\mathbb C[X,Y_1,W_1]\): its coefficient \(-4X^2\)
is coprime to \(W_1^2+4\kappa XY_1^2\), since \(X\) does not divide
the latter. Gauss's lemma proves irreducibility.
But \(c_0\in L\subset\operatorname{Frac}A\subset\operatorname{Frac}B\).
Equation (22) makes it integral over the normal polynomial ring
\(B\), hence an element of \(B\). A nonconstant irreducible element
of the UFD \(B\) cannot be its square. Equivalently, the prime
valuation of that polynomial is one, while a rational square has
even prime valuation. This contradiction excludes (10).

## Scope and provenance

Under the full actual hypotheses (1), a zero center is recognized,
and a nonzero repeated-quadratic center is excluded. A nonzero
constant center or a squarefree center is not settled by this note.
This is not recognition of every whole projected plane, an
arbitrary-entry or minimum-profile theorem, or unrestricted cancellation.

The field coefficients in (8) are not assumed complex. Complex
constants in the repeated branch arise only after the cofactor
argument and joint-constant proof. Its final exclusion uses the
actual four-coordinate identity (22); a formal line model without
original fraction-field return would not justify it.

Universal184, eliminant206, the degree-five cone lemma, both205
recognition sources and the constant-projection theorem210 were
fully read. New unsaved calculations checked the zero-center fourth
potential and the third-potential transport in (17)--(18); they were
not saved checkers or substitutes for the written proof.
No saved checker was executed, imported or compiled, and no
earlier source or index was edited. This is
private working mathematics, not expert or proof-assistant
certification or historical novelty clearance.
