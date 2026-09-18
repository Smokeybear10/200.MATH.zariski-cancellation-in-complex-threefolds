# The constant-first projected line is impossible in the product-radical chart

Status: bounded working exclusion. For the supplied full initial kernel
\(Z^2-XYW\), the line with constant first projection cannot occur.
The proof uses an actual two-variable locally nilpotent derivation over
\(\mathbb C[X,Y]\), not a lift of a coefficient-field coordinate.
It leaves the other projected line, the conic and the zero-return branch
outside its scope.

## 1. Actual input and the projected line

Assume the globally sliced actual frame
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad A=\ker E,\\
\deg_E(X,Y,Z,W)=(1,1,2,2),\\
a=EX,\quad b=EY,\quad e=E^2Z/2,\quad h=E^2W/2,\\
\ker(\mathsf X,\mathsf Y,\mathsf Z,\mathsf W
 \longmapsto aT,bT,eT^2,hT^2)
 =(\mathsf Z^2-\mathsf X\mathsf Y\mathsf W).
\end{gathered}
\tag{1}
\]
The named capital letters are original polynomial coordinates, \(T\)
is independent, and the displayed ideal is the entire initial kernel.

Use the literal \(Z\) pivot and exact chart of
[universal184](weight-four-universal-chart-potentials-pass184-working.md),
as rebuilt in
[product-radical227](rank-one-product-radical-sextic-pruning-pass227-working.md):
\[
\begin{gathered}
N=[u^3](\partial_Z|_A)\ne0,\quad
L=\operatorname{Frac}(\ker_A N),\quad A_L=L[v],\quad Nv=1,\\
a,b,e,h\in\ker_A N,\quad t=b/a,\quad \rho=h/a^2,\quad
q=e/a^2,\quad q^2=t\rho,\\
Y=y+tX,\quad Z=z+\sigma X+qX^2,\quad
W=w+\vartheta X+\rho X^2,\qquad L[y,z,w]=L[v].
\end{gathered}
\tag{2}
\]
The ratios \(t,\rho\) are algebraically independent, and
\([L:\mathbb C(t,\rho)]<\infty\). Coefficient derivatives extend
uniquely to \(L\) and fix \(v\). The coordinate \(X\) is independent
over \(L(v)\).

Consider precisely the first line row of227:
\[
y\in L,\qquad \deg_v\vartheta=1.
\tag{3}
\]
The actual return \(R=q_{t\rho}y+q_{\rho\rho}\vartheta+k_\rho\)
is then nonzero and has degree one, since
\[
q_\rho=\frac q{2\rho},\qquad
q_{\rho\rho}=-\frac q{4\rho^2},\qquad
q_{\rho\rho\rho}=\frac{3q}{8\rho^3}.
\tag{4}
\]

## 2. The full potentials determine the auxiliary degrees

The third universal potential is
\[
Rw=\ell-\{H_3(q)+H_2(k)+H_1(n)\}(y,\vartheta).
\tag{5}
\]
Its right side is cubic in the affine parameter \(\vartheta\),
with leading coefficient \(-q_{\rho\rho\rho}/6\).
The left side has a linear factor \(R\), whose leading coefficient
is \(q_{\rho\rho}\). As \(w\in L[\vartheta]\), polynomial degree and
leading coefficient therefore give
\[
w=\frac{\vartheta^2}{4\rho}+\lambda\vartheta+\omega,
\qquad \lambda,\omega\in L .
\tag{6}
\]
No lower potential is set to zero.

The second potential is \(z=q_\rho w+H_2(q;y,\vartheta)
+H_1(k;y,\vartheta)+n\). Its quadratic coefficient is
\[
\frac{q_\rho}{4\rho}+\frac{q_{\rho\rho}}2
=\frac{q}{8\rho^2}-\frac{q}{8\rho^2}=0.
\]
Together with the first potential, this proves
\[
z=\kappa\vartheta+\zeta,\qquad
\sigma=q_\rho\vartheta+q_ty+k,\qquad
\kappa,\zeta\in L .
\tag{7}
\]

Extend \(N\) to \(B=A[u]\) by \(Nu=0\), and define
\[
\mathcal P=aN-(NX)E.
\tag{8}
\]
This is an original polynomial derivation. It fixes \(X\) and \(L\),
commutes with \(E\), and is locally nilpotent: on
\(B_a=A_a[X]\) it fixes \(X\) and acts on \(A_a\) as \(aN\),
with \(Na=0\). Restriction to \(B\) preserves local nilpotence.
Put \(\tau=aN\vartheta\in L^*\). Equations (2),(3),(6),(7) give
\[
\mathcal PX=\mathcal PY=0,\qquad
\mathcal PZ=\tau(q_\rho X+\kappa),\qquad
\mathcal P^2Z=0,\qquad
\mathcal P^2W=\frac{\tau^2}{2\rho}\ne0,\quad
\mathcal P^3W=0.
\tag{9}
\]

## 3. Primitive division preserves both actions

Let \(\Delta\) be the gcd in \(B\) of the nonzero original coordinate
components of \(\mathcal P\), and set \(D=\mathcal P/\Delta\).
For completeness, the two needed invariances can be proved directly.

First \(\mathcal P\Delta=0\). Otherwise
\(\mathcal P\Delta=\Delta D\Delta\) contradicts the degree function
of the locally nilpotent derivation \(\mathcal P\): the left side
has degree \(\deg_{\mathcal P}\Delta-1\), while the right side has
degree at least \(\deg_{\mathcal P}\Delta\).
Thus \(D\Delta=0\), and
\(\mathcal P^j f=\Delta^jD^jf\) proves that \(D\) is locally
nilpotent and irreducible.

Next write \(\mathcal PX_i=\Delta g_i\) for the four original
coordinates, with \(\gcd(g_i)=1\). Commutation gives
\[
E(\Delta g_i)=E(\mathcal PX_i)=\mathcal P(EX_i)
            =\Delta D(EX_i).
\tag{10}
\]
Hence \(\Delta\) divides \((E\Delta)g_i\) for every \(i\).
Unique factorization and the gcd condition imply
\(\Delta\mid E\Delta\). The same degree argument for \(E\)
forces \(E\Delta=0\). Consequently \([E,D]=0\).
This uses neither a slice for \(D\) nor coprimality of two selected
coefficients over a function field.

In \(B_L=L[v][X]\), the actions are \(E=a\partial_X\) and
\(\mathcal P=a\partial_v\). Their common kernel is \(L\).
Therefore \(\Delta\in L^*\), and
\[
\delta:=\tau/\Delta\in L^*,\qquad
DZ=\delta(q_\rho X+\kappa),\quad
D^2W=\frac{\delta^2}{2\rho}\ne0,\quad
D^2Z=D^3W=0.
\tag{11}
\]
The notation \(L^*\) here makes no claim that \(\Delta\) is a unit
of the original polynomial ring.

## 4. An original coefficient ring forces incompatible slopes

Set \(S=\mathbb C[X,Y]\), so \(B=S[Z,W]\), and \(D\) is an
irreducible \(S\)-linear LND. This is a UFD containing the rationals.
By [Dasgupta--Gupta, Lemma 2.3(i)](https://arxiv.org/html/1701.03635v1),
applied to the relative variables \(Z,W\),
\[
DZ\in S,\qquad DW\in S[Z].
\tag{12}
\]
Only the UFD conclusion is used, not the separate PID slice statement.
Since \(D^3W=0\) and \(DZ\ne0\), differentiating in \(Z\) twice
shows that \(DW\) has degree at most one in \(Z\). In particular
\[
D^2W\in S.
\tag{13}
\]

For any nonzero polynomial in \(S\), its E-degree equals its ordinary
total degree in \(X,Y\). Indeed if its top homogeneous part is \(p_n\),
its leading E-coefficient is \(a^n p_n(1,t)\ne0\), since \(t\)
is transcendental over \(\mathbb C\). Thus
\[
S\cap\ker E=\mathbb C.
\tag{14}
\]
By (11), the E-degree of \(DZ\) is exactly one. Equations (12)
and (14), also applied to the E-invariant polynomial \(D^2W\),
give constants \(c_0,c_1,c_2,d\in\mathbb C\) with \(d\ne0\) such that
\[
DZ=c_1X+c_2Y+c_0,\qquad
\frac{\delta^2}{2\rho}=d.
\tag{15}
\]
Compare the coefficients of the independent variable \(X\) after
substituting \(Y=y+tX\) in (11) and (15):
\[
\delta q_\rho=c_1+c_2t.
\tag{16}
\]
Square this equality and use \(q^2=t\rho\) and
\(\delta^2=2d\rho\). It follows that
\[
(c_1+c_2t)^2=\frac d2\,t .
\tag{17}
\]
This is impossible for the transcendental \(t\): its quadratic
coefficient forces \(c_2=0\), and then its linear coefficient forces
\(d=0\). This contradicts (15), and excludes (3).

## 5. Scope and verification

This is an exclusion of one supplied actual projected line.
It does not itself exclude \(R=0\), the line with constant
\(\rho y-t\vartheta\), or the conic left by227. It supplies no
entry theorem for arbitrary sliced actions.

The complete universal184 and227 sources were read. The leading
potential coefficients, common-kernel gcd argument, original UFD
application and final slope identity were independently reconstructed.
The exact primary Lemma 2.3(i) was freshly checked before use.
This note does not claim to reconstruct every earlier chart dependency.
No saved checker was executed during this proof's authorship, and no
previous proof or verification packet was edited. This is written
working mathematics, not a novelty claim, human expert review or
proof-assistant certification.
