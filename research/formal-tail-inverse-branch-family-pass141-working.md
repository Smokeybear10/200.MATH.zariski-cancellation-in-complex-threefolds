# Formal tail factors and inverse branches in every degree

The full formal dense Taylor system permits a first tail of arbitrarily
large degree even when its selected generic line is linear. In the
family below, the first-tail degree equals the degree of the finite
inverse-field extension of the displayed polynomial tuple.

That equality is proved only for this explicit family. It is not a
general correspondence between extra tail factors and inverse branches.
The tuple is not a polynomial coordinate frame: its Jacobian is a
nonunit, and the selected field derivation does not return coefficients
to the underlying polynomial ring. This extends the quadratic formal
control140, not the actual-frame theorem.[^1]

## 1. A uniform polynomial tuple and its coefficient field

Fix
\(F(T_0)=\sum_{j=0}^{n}c_jT_0^j\in\mathbb C[T_0]\),
where \(n\ge2\) and \(c_n\ne0\).
Let \(X,k,\rho,v\) be algebraically independent over \(\mathbb C\).
On \(B_*=\mathbb C[X,k,\rho,v]\), use the translation
\(E=\partial_X\), fixing \(k,\rho,v\), and set
\[
\begin{gathered}
\tau=F(k),\qquad L=\mathbb C(k,\rho),\qquad
K=\mathbb C(\tau,\rho),\qquad [L:K]=n,\\
y=v,\qquad z=k,\qquad
Y=v+F(k)X,\qquad Z=k+\rho X,\\
W=\frac{F(k+\rho X)-F(k)}{X}
 =\sum_{j=1}^{n}c_j\sum_{i=1}^{j}
   \binom ji k^{j-i}\rho^iX^{i-1}.
\end{gathered}
\tag{1}
\]
The quotient in (1) is the displayed polynomial divided difference,
including on \(X=0\). Its time degree is \(m=n-1\), with leading
coefficient \(c_n\rho^n\ne0\).

For the field degree, \(\tau,\rho\) are independent. The polynomial
\(F(T_0)-Q_0\), where \(Q_0\) is an independent variable, is irreducible
over \(\mathbb C(\rho,Q_0)\): its ideal in
\(\mathbb C(\rho)[T_0,Q_0]\) is prime, since the quotient eliminates
\(Q_0\), and it is primitive over \(\mathbb C(\rho)[Q_0]\).
Gauss's lemma gives the field assertion. Substituting \(Q_0=\tau\)
proves \([L:K]=n\). Characteristic zero makes this extension separable.

The three good speeds are \((1,F(k),\rho)\); their second derivatives
vanish, their rank is two, and their homogeneous cone is dense.
Indeed dehomogenization at the entry \(1\) gives a polynomial in the
independent functions \(F(k),\rho\). The underlying action has the
actual slice \(X\). These facts do not make the displayed tuple a
polynomial coordinate system.

## 2. Exact relative Jacobian and field derivation

The coefficient derivations on \(L\) are
\(\partial_\tau=F'(k)^{-1}\partial_k\) and \(\partial_\rho\).
They commute and extend to \(L(v)\) by fixing \(v\). Because
\(F'(k)\ne0\) in \(L\), the following expressions are well-defined:
\[
\begin{gathered}
T=-\frac{X}{F'(k)}\partial_k+
       \frac1{F'(k)}\partial_\rho+X^2\partial_v,\\
TX=TY=TZ=0,\qquad TW=1,\qquad
[X^2]T|_{L(v)}=\partial_v,\\
\det\frac{\partial(Y,Z,W)}{\partial(\tau,\rho,v)}
=
\det\begin{pmatrix}
X&0&1\\
1/F'(k)&X&0\\
\bigl(F'(Z)-F'(k)\bigr)/(XF'(k))&F'(Z)&0
\end{pmatrix}
=1.
\end{gathered}
\tag{2}
\]
The apparent numerator quotient in the last matrix is polynomial in
\(X\) over \(L\). The determinant is computed at fixed \(X\).

Direct differentiation gives the four values of \(T\). In particular,
applying \(T\) to \(XW=F(Z)-F(k)\) gives \(XTW=X\).
The highest coefficient \(\partial_v\) is a genuine LND of \(L[v]\),
and \(L[y,z]=L[v]\). The uniform coefficient shift at most two extends
\(T\) continuously to \(L(v)((X^{-1}))\), with \(TX=0\).
No local nilpotence of \(T\) on \(B_*\) is asserted.

## 3. Full Taylor annihilation and exact negative tails

Use the positive Taylor embedding from139, not a truncated jet:[^2]
\[
\begin{gathered}
\Theta(f)=\sum_{a,b\ge0}
 \frac{\partial_\tau^a\partial_\rho^b f}{a!\,b!}
 v^ak^bX^{-a-b},\\
\Theta(\tau)=\tau+v/X=Y/X,\qquad
\Theta(\rho)=\rho+k/X=Z/X,\qquad
F(\Theta(k))=\tau+v/X,\\
T\Theta(f)=0\qquad(f\in L).
\end{gathered}
\tag{3}
\]
The commuting coefficient partials give a multiplicative Taylor
embedding. Its constant term is \(f\), so nonzero elements are units
of the Laurent field. Equivalently, \(\Theta(k)\) is the unique root
of the displayed equation with constant term \(k\), since
\(F'(k)\ne0\).

Both displayed shifted base parameters are killed by \(T\).
Differentiating \(F(\Theta(k))=\Theta(\tau)\) then gives
\(F'(\Theta(k))T\Theta(k)=0\).
The first factor has nonzero constant term \(F'(k)\), proving
annihilation on \(L=\mathbb C(k,\rho)\).

The entire peeling and its first two negative stages are
\[
\begin{gathered}
f_j=c_{j+1}\rho^{j+1}\quad(0\le j\le n-1),\qquad
\mathscr S=\sum_{j=0}^{n-1}X^j\Theta(f_j)
          =\frac{F(Z)-F(0)}{X},\\
W=(\mathscr S)_{\ge0},\qquad
\mathscr R=W-\mathscr S=\frac{F(0)-\tau}{X},\qquad
T\mathscr R=1,\qquad f_{-1}=F(0)-\tau,\\
\mathscr R-X^{-1}\Theta(f_{-1})=v/X^2,\qquad
T(v/X^2)=1 .
\end{gathered}
\tag{4}
\]
These are exact rational identities, interpreted at \(X=\infty\).
They identify the peeling coefficients without fitting finite data.

## 4. The first tail, its geometric components, and the shear minimum

For independent formal \(U,V\), the homogeneous Taylor terms of
\(\rho^{j+1}\) terminate at order \(j+1\). The signed definitions139
therefore give[^3]
\[
\begin{gathered}
R_1(U,V)=F(0)-F(V),\qquad
\Phi(U,V)=\tau-F(V),\qquad \Psi(U,V)=U,\\
g(U,V)=V-k,\qquad
\ker\bigl(L[U,V]\longrightarrow L[v],\ (U,V)\mapsto(v,k)\bigr)=(g),\\
\Phi=gH,\qquad
H=-\frac{F(V)-F(k)}{V-k},\qquad H(v,k)=-F'(k)\in L^*,\\
\deg g=1,\qquad \deg\Phi=n=m+1,\qquad \deg H=n-1 .
\end{gathered}
\tag{5}
\]
The quotient defining \(H\) is a polynomial. The evaluated gradient
is \((0,-F'(k))\), which generates the unit ideal over \(L[v]\).
Also \((\Psi_U,\Psi_V)=(\Phi_\tau,\Phi_\rho)=(1,0)\), and
\(\partial_v\Psi(v,k)=1\).

The polynomial \(F(V)-F(k)\) is squarefree over \(L\). Any common root
with \(F'(V)\) would be a complex critical point \(\alpha\) of \(F\)
and satisfy \(F(k)=F(\alpha)\), contradicting transcendence of \(k\).
It has \(n\) distinct roots over an algebraic closure of \(L\).
It need not split into \(n\) factors over \(L\) itself.
In particular, \(g\) occurs once and \(H\) is nonconstant.
Thus \(\Phi\) is not a plane coordinate.

There is an elementary minimum-degree statement even for this
noninvertible tuple:
\[
\mu_*:=\min_{P\in\mathbb C[X,Y,Z]}\deg_E(W+P)=n-1,
\qquad \deg g=1<\mu_*+1=\deg\Phi .
\tag{6}
\]
Here the good polynomials are algebraically independent, as also
follows from the nonzero Jacobian below. A nonzero good polynomial
of total degree \(d\) has time degree \(d\), by the dense speed row.
If \(d>m\) it cannot lower \(m\); if \(d<m\) it cannot cancel the
highest coefficient of \(W\). For \(d=m=n-1\), cancellation would
require
\(P_m(1,\tau,\rho)=-c_n\rho^n\).
The left side has total degree at most \(n-1\) in the independent
variables \(\tau,\rho\), which is impossible. Taking \(P=0\) proves
(6). This direct argument does not apply an actual-frame theorem to
the formal tuple.

## 5. Exact inverse-field degree and the actual failures

The actual polynomial Jacobian and the generic reconstruction are
\[
\begin{gathered}
\det\frac{\partial(X,Y,Z,W)}{\partial(X,k,\rho,v)}=F'(k),\\
Q:=F(Z)-XW=F(k),\qquad
\rho=(Z-k)/X,\qquad v=Y-XQ,\\
M:=\mathbb C(X,Y,Z,W)=\mathbb C(X,Y,Z,Q),\\
\mathbb C(X,k,\rho,v)=M(k),\qquad [M(k):M]=n .
\end{gathered}
\tag{7}
\]
The first determinant equals the relative determinant in (2) times
the change-of-parameter factor \(F'(k)\).
It is nonzero, so the target polynomials are algebraically independent.
Replacing \(W\) by \(Q=F(Z)-XW\) is a rational field change, with
inverse \(W=(F(Z)-Q)/X\).

Thus \(Q\) is independent over \(\mathbb C(X,Y,Z)\).
The same linear-in-\(Q\) irreducibility argument used after (1), now
over \(\mathbb C(X,Y,Z)\), proves that \(F(T_0)-Q\) has degree \(n\)
and is irreducible over \(M\). The recovery formulas then prove the
last field equality and exact degree in (7).
The tuple is generically \(n\)-to-one, not birational.

Since \(n\ge2\), the Jacobian \(F'(k)\) is a nonunit of \(B_*\).
Moreover \(T\rho=1/F'(k)\notin B_*\), so the field derivation is not
an actual polynomial coordinate partial there. At \(X=0\), the
projected-ring inclusion is
\[
\mathbb C[y,z,w_0]
 =\mathbb C[v,k,F'(k)\rho]\varsubsetneqq
 \mathbb C[v,k,\rho],\qquad w_0=F'(k)\rho .
\tag{8}
\]
For example, choose a complex root \(\alpha\) of \(F'\).
Reducing modulo \(k-\alpha\), the smaller ring has image
\(\mathbb C[v]\), whereas \(\rho\) remains independent in the larger
ring. The first good speed is one, so localizing at that speed
does not repair this strict inclusion.

This family identifies a concrete source of extra first-tail components:
here the number of geometric components equals the inverse-field
degree, and the nontrivial coefficient-field degree also equals \(n\).
Neither equality has been proved for an arbitrary formal chart.
In particular, a factor of a first-tail polynomial must not be counted
as an actual inverse branch without checking all later constraints.

The actual-frame question remains whether polynomial invertibility
or the full coefficient-return and LND conditions rule out every
extra factor. No member of this family is a counterexample to that
claim, and no global descent or cancellation conclusion follows.

## Sources

1. [The full formal Taylor system does not force a coordinate relation140](dense-tail-coordinate-obstruction-pass140-working.md),
   Sections 1--5. The quadratic formal example is generalized here;
   its actual-versus-relative Jacobian distinction is retained.
2. [A dense all-degree chart and its formal Taylor peeling139](dense-all-degree-taylor-chart-pass139-working.md),
   Sections 5--6. The exact positive Taylor embedding and continuous
   Laurent derivation provide the conventions, not an actual-frame
   realization of this tuple.
3. [The first two negative Taylor coefficients in a dense chart139](dense-negative-tail-relations-pass139-working.md),
   Sections 2--4. Signed tail formulas and the unit restriction of a
   complementary factor.

All constructions and degree assertions (1)--(8) are proved directly
above. No new external theorem or historical novelty claim is used.

[^1]: Source 1.
[^2]: Source 2.
[^3]: Source 3.
