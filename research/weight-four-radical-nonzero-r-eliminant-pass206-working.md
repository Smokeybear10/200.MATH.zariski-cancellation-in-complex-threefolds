# The radical pivot with nonzero return coefficient

**Status: working necessary restrictions, not recognition.**

For the actual radical pivot, the two last universal potentials give
an explicit eliminant that is at most quartic in its first variable but can
have total degree five. The actual scalar determinant proves that
this eliminant is nonzero, even when its displayed top part vanishes.
The selected component is simple, its evaluated cofactor is supported
on the return divisor, and its normalization is generated as a module
by two elements. These statements do not assume that the projected
plane ring is normal.

The zero, nonzero constant and repeated quadratic centers do give
the entire plane ring. A nonconstant squarefree
center remains a genuine unclosed case of this note.

## 1. Exact actual hypotheses and all lower terms

Start with a supplied actual globally sliced frame whose entire
initial kernel is the radical form. Interchanging the two bad
coordinate names puts it in the form
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad A=\ker E,\\
\deg_E(X,Y,Z,W)=(1,1,2,2),\qquad
\ker\theta_0=(\mathsf X^2\mathsf Z-\mathsf W^2),\\
a=EX\ne0,\quad t=EY/a,\quad
\rho=(E^2W/2)/a^2,\quad q=(E^2Z/2)/a^2=\rho^2.
\end{gathered}
\tag{1}
\]
Thus the selected original partial is the old \(\partial_W\), not
the old \(\partial_Z\). Retain the actual constructions of
[universal184](weight-four-universal-chart-potentials-pass184-working.md):
\[
\begin{gathered}
0\ne N=[u^3](\partial_Z|_A),\quad
L=\operatorname{Frac}\ker_A N,\quad A_L=L[v],\quad Nv=1,\\
[L:\mathbb C(t,\rho)]<\infty,\qquad
Y=y+tX,\quad Z=z+\sigma X+\rho^2X^2,\quad
W=w+\vartheta X+\rho X^2,\\
y,z,w,\sigma,\vartheta\in L[v],\quad
L[y,z,w]=L[v],\quad \mathbb C(y,z,w)=L(v),\quad
J_0=-a^3\in L^*.
\end{gathered}
\tag{2}
\]
The independent coefficient partials \(\partial_t,\partial_\rho\)
extend uniquely to \(L\), commute, and fix \(v\). No equality
\(L=\mathbb C(t,\rho)\) is assumed.

Use independent formal variables \(U,V\). The divided Taylor
polynomials in universal184 specialize as follows:
\[
\begin{aligned}
f&=V^2+k_tU+k_\rho V+n,&
\mathcal R&=2V+k_\rho,\\
S&=\frac{k_{tt}}2U^2+k_{t\rho}UV
  +\frac{k_{\rho\rho}}2V^2+n_tU+n_\rho V,&
b_0&=k_{t\rho}U+k_{\rho\rho}V+n_\rho,\\
Q&=\frac{k_{ttt}}6U^3+\frac{k_{tt\rho}}2U^2V
 +\frac{k_{t\rho\rho}}2UV^2+\frac{k_{\rho\rho\rho}}6V^3\\
 &\quad+\frac{n_{tt}}2U^2+n_{t\rho}UV
 +\frac{n_{\rho\rho}}2V^2-\ell_tU-\ell_\rho V-m,
 &T&=\ell-S,
\end{aligned}
\tag{3}
\]
where \(k,n,\ell,m\in L\). In particular \(b_0=f_\rho=S_V\),
where these are coefficient or formal derivatives, respectively.
Every lower term is included in (3). The actual identities are
\[
\begin{gathered}
\sigma=2\rho\vartheta+k,\qquad z=2\rho w+f(y,\vartheta),\\
Rw=T(y,\vartheta),\qquad
w^2+b_0(y,\vartheta)w+Q(y,\vartheta)=0,\qquad
R=\mathcal R(y,\vartheta)\ne0\text{ in }L[v].
\end{gathered}
\tag{4}
\]
The last condition is the branch assumption. It allows zeros of
\(R\), and does not make \(R\) an original-ring or line-ring unit.
The identically zero branch is separate in
[the t-independent recognition205](weight-four-t-independent-zero-r-recognition-pass205-working.md).

## 2. Elimination, degrees and the calibrated gradient

Eliminating \(w\) without dividing in a ring gives
\[
\boxed{\mathcal H=T^2+\mathcal R b_0T+\mathcal R^2Q,
\qquad \mathcal H(y,\vartheta)=0.}
\tag{5}
\]
Equivalently, in the fraction field of the formal polynomial ring,
\(\mathcal H=\mathcal R^2 K(U,V,T/\mathcal R)\), where
\(K(U,V,W_0)=W_0^2+b_0W_0+Q\). Formula (5) itself is polynomial.

Writing \(H_j(c)\) for the divided Taylor polynomial of degree \(j\),
one obtains
\[
\begin{gathered}
\deg\mathcal H\le5,\qquad
\mathcal H_5=4V^2H_3(k),\qquad
\deg_U\mathcal H\le4,\qquad [U^4]\mathcal H=k_{tt}^2/4,\\
H_3(k)=0\ \Longrightarrow\
\mathcal H_4=H_2(k)^2-2V H_1(k_\rho)H_2(k)+4V^2H_2(n),\\
k_{tt}=0\ \Longrightarrow\ \deg_U\mathcal H\le2.
\end{gathered}
\tag{6}
\]
For the final implication, \(k_{ttt}=k_{tt\rho}=0\) as well.
Only \(\mathcal R^2H_3(k)\) can contribute total degree five.
Thus one may not call the eliminant a total-degree quartic without
an additional vanishing argument.

For the determinant calculation define evaluated quantities
\[
\begin{gathered}
B_1=S_U(y,\vartheta)=k_{tt}y+k_{t\rho}\vartheta+n_t,\qquad
C_1=2w+b_0(y,\vartheta),\\
\Lambda_i=\ell_i-S_i(y,\vartheta)-\mathcal R_i(y,\vartheta)w,
\qquad i=t,\rho,\\
R\,dw=-B_1dy-C_1d\vartheta+\Lambda_tdt+\Lambda_\rho d\rho,\\
J_0=\left[dy\wedge(R\,d\vartheta+B_1dt+C_1d\rho)\wedge dw
\right]_{dt\wedge d\rho\wedge dv}.
\end{gathered}
\tag{7}
\]
The partials \(S_i,\mathcal R_i\) differentiate their coefficients
before evaluating, not the evaluated functions. Explicitly
\(\mathcal R_t=k_{t\rho}\) and
\(\mathcal R_\rho=k_{\rho\rho}\).

The two formal potential gradients, evaluated only after
differentiation, are
\[
\begin{gathered}
(\mathcal R W_0+S-\ell)_{U,V,W_0}=(B_1,C_1,R),\qquad
K_{U,V,W_0}=(-\Lambda_t,-\Lambda_\rho,C_1),\\
\mathcal H_U(y,\vartheta)=-R(C_1B_1+R\Lambda_t),\qquad
\mathcal H_V(y,\vartheta)=-R(C_1^2+R\Lambda_\rho).
\end{gathered}
\tag{8}
\]
For example, the formal derivatives of \(T/\mathcal R\) at the
curve are \(-B_1/R,-C_1/R\). Differentiating the rational identity
following (5) yields (8); the term from differentiating
\(\mathcal R^2\) vanishes because \(K=0\). Clearing denominators
gives identities in \(L[v]\).

Substitute (7) in its wedge and expand. The result is
\[
\begin{gathered}
R^3J_0=D_U\mathcal H_U(y,\vartheta)
             +D_V\mathcal H_V(y,\vartheta),\\
D_U=R(y_v\vartheta_\rho-y_\rho\vartheta_v)+C_1y_v,\qquad
D_V=R(y_t\vartheta_v-y_v\vartheta_t)-B_1y_v.
\end{gathered}
\tag{9}
\]
To check both signs directly, before using (8) the expression
\(R J_0\) is the coefficient of
\[
dy\wedge\{(R\Lambda_t+B_1C_1)d\vartheta\wedge dt
 +(R\Lambda_\rho+C_1^2)d\vartheta\wedge d\rho
 +(B_1\Lambda_\rho-C_1\Lambda_t)dt\wedge d\rho\}.
\]
Using
\(C_1\mathcal H_U-B_1\mathcal H_V
 =R^2(B_1\Lambda_\rho-C_1\Lambda_t)\)
gives (9).
Since \(R\ne0\) and \(J_0\in L^*\), equation (9) proves
\(\mathcal H\ne0\). This argument also covers every degeneration
of the displayed degree-five and degree-four parts.

## 3. The exact projected ring and selected component

Put \(C=L[y,\vartheta]\) and \(O=L[v]\). From (2)--(4),
\[
\begin{gathered}
O=C[w]=C+Cw,\qquad \operatorname{Frac}C=L(v),\qquad
C_R=O_R,\qquad RO\subset C.
\end{gathered}
\tag{10}
\]
The first equality follows from \(z=2\rho w+f(y,\vartheta)\)
and the actual whole-line equality. The monic quadratic in (4)
reduces every power of \(w\) to a \(C\)-linear combination of
\(1,w\). These are module generators, not a claim of a free
rank-two basis. The fraction-field equality follows from
\(w=T/R\). That formula also gives the last two assertions.
In particular \(R\) lies in the conductor from \(O\) to \(C\).

Thus \(O\) is finite integral over \(C\), birational to it, and
is exactly its integral closure in that field. Indeed any element
of \(L(v)\) integral over \(C\) is also integral over \(O\), and
\(O=L[v]\) is integrally closed. This proof does not assume that
\(C\) is integrally closed.

Let \(G\) generate the height-one prime kernel of
\(L[U,V]\to L[v]\). Equation (5) and the nonzero conclusion give
\(G\mid\mathcal H\). If \(G\) had multiplicity at least two in
\(\mathcal H\), both evaluated partials in (9) would vanish.
Consequently, writing \(\mathcal H=GQ_1\), one has
\[
\begin{gathered}
G\text{ is a simple factor of }\mathcal H,\qquad
0\ne Q_1(y,\vartheta)\mid R^3\quad\text{in }L[v],\\
\deg G=\max(\deg_v y,\deg_v\vartheta)\le5,\qquad
\deg_v\vartheta\le4,\\
k_{tt}=0\ \Longrightarrow\ \deg_v\vartheta\le2.
\end{gathered}
\tag{11}
\]
The divisibility follows from (9), since \(J_0\) is a scalar unit.
The cofactor need not be a unit at a zero of \(R\).

Here is an exact-field degree proof. For a transcendental \(s\),
the polynomial \(sy+\vartheta\) in \(v\) has degree
\(d=\max(\deg_vy,\deg_v\vartheta)>0\). Over \(L(s)\), a
polynomial of degree \(d\) gives a function-field extension of
degree \(d\): the polynomial \(p(v)-Z_0\) is irreducible, being
linear in \(Z_0\), and Gauss's lemma applies. On the other hand,
the irreducible polynomial \(G(U,Z_0-sU)\) has degree \(\deg G\)
in \(U\), with nonzero leading coefficient \(G_{\deg G}(1,-s)\).
The birational equality in (10) identifies these two extensions.
This proves \(d=\deg G\). If \(\vartheta\) is nonconstant, the
same argument without a generic linear combination gives
\([L(v):L(\vartheta)]=\deg_v\vartheta=\deg_U G\).
Equation (6) then proves the final bounds in (11). If
\(\vartheta\in L\), those bounds hold directly and \(R\in L^*\),
so (10) already gives \(C=O\).

## 4. The exact center and two whole-plane cases

Define
\[
V_0=-k_\rho/2,\qquad p(U)=S(U,V_0)-\ell,
\qquad S-\ell=p(U)-\mathcal R D(U,V),\quad \deg D\le1.
\tag{12}
\]
Polynomial division by \(V-V_0\) gives \(D\) over the exact
field \(L\). In particular \(\deg p\le2\), and the first
potential is
\[
R\{w-D(y,\vartheta)\}+p(y)=0.
\tag{13}
\]
Also \(\mathcal H(U,V_0)=p(U)^2\). If \(p=0\), equation (13)
and the domain give \(w=D(y,\vartheta)\in C\), hence \(C=O\).
If \(p\in L^*\), the two polynomial factors on the left of
\(R(w-D)=-p\) are units in \(L[v]\); thus \(R\in L^*\) and
again \(C=O\).

Suppose next that \(p=\kappa(U-U_0)^2\), with
\(\kappa\in L^*\). The repeated root \(U_0\) belongs to \(L\).
Set
\[
P_c=R,\qquad Q_c=y-U_0,\qquad
S_c=-\{w-D(y,\vartheta)\}/\kappa.
\tag{14}
\]
Then \(P_cS_c=Q_c^2\), and
\(L[P_c,Q_c,S_c]=O\): these entries recover
\(\vartheta=V_0+P_c/2\), \(y=U_0+Q_c\), and \(w\).
Equation (11) gives \(\deg_vP_c,\deg_vQ_c\le5\).

The vertex condition must be checked with the actual determinant.
The gradient of the first potential (13) has evaluated entries
\[
B_1=-R D_U+2\kappa Q_c,\qquad
C_1=2(w-D)-R D_V,\qquad P_{W_0}=R.
\tag{15}
\]
At a common zero of \(P_c,Q_c,S_c\) over an algebraic closure of
\(L\), all three vanish. The middle row in the wedge (7) would
be zero, contradicting \(J_0=-a^3\in L^*\). Thus the triple is
vertex-free. The freshly read
[degree-five cone lemma184](vertex-free-quintic-cone-projection-pass184-working.md)
applies with every hypothesis verified and gives
\(L[P_c,Q_c]=L[v]\). Since this is \(C\),
\[
p=0,\quad p\in L^*,\quad\text{or }p=\kappa(U-U_0)^2
\quad\Longrightarrow\quad L[y,\vartheta]=L[v].
\tag{16}
\]
Therefore a projection defect, if one occurs in this actual branch,
requires a nonconstant squarefree center of degree one or two.
In that remaining case, any point above \(R=0\) has
\(\vartheta=V_0\) and \(p(y)=0\). For each such pair \((y,V_0)\),
the monic quadratic for \(w\) has at most two roots. Since the
three entries generate \(O\), distinct parameter values cannot
have the same triple. Hence, over an algebraic closure of \(L\),
there are at most \(2\deg p\) distinct points above \(R=0\).
This is a bound on distinct points, not on ramification multiplicity.

## 5. A boundary and the remaining gate

The finite-module and conductor conclusions alone do not imply
normality. For a purely formal example over any characteristic-zero
field, take
\[
y=v(v^2-1),\qquad \vartheta=(v^2-1)/2,\qquad w=v,
\qquad R=2\vartheta.
\tag{17}
\]
Then \(Rw=y\), \(w^2=2\vartheta+1\), and the triple generates
the whole line, but the two plane entries agree at \(v=1,-1\).
Thus \(L[y,\vartheta]\ne L[v]\), with plane relation
\[
U^2-4V^2(2V+1)=0.
\tag{18}
\]
Its restriction to \(V=0\) is \(p(U)^2\), with the squarefree
linear center \(p(U)=-U\). This example illustrates why the ring
structure and low degree are insufficient. It is not asserted to
satisfy the Taylor coefficient identities (3), the calibrated
determinant, any actual fourfold frame, or the full initial kernel.

The unresolved gate is to use the remaining actual differential
identities at a squarefree center, or to produce an original-ring
coordinate by another argument. This note proves neither that a
projection defect exists in an actual frame nor that it is impossible.
Even the whole-plane cases (16) are not ambient-coordinate recognition.
There is no claim about the other nonzero-return pivots, arbitrary
entry into exact1122, higher minimum profiles, height-two kernels, or
unrestricted cancellation.

The universal source and the exact degree-five cone lemma were fully
read before this derivation. No saved checker was executed, imported
or compiled, and no earlier source or index was changed. The written
proof and independent source review are not human expert certification,
proof-assistant verification, or historical novelty clearance.
