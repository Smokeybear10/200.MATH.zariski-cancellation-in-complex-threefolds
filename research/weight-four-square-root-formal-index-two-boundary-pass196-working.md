# A square-root chart with constant Jacobian and exact field index two

Status: bounded working negative example. The following rational chart
satisfies every universal coefficient potential, has the expected full
scalar determinant and projected field return, and has the formal leading
relation \(Z^2-X^3Y\). Nevertheless its original four-entry map has field
degree two. It is not an actual polynomial frame and is not a
counterexample to cancellation.

The distinction is important: a coefficient-field parameter or projected
inverse does not supply an original-ring inverse. This example belongs
to the surviving \(f=q\) family of
[two-gate195](weight-four-square-root-two-gate-classification-pass195-working.md).
It is kept separate from that classification and from the195 packet.

## 1. Independent variables and the complete chart

Let \(x,y,q,\rho\) be algebraically independent over \(\mathbb C\), and put
\[
\mathcal F=\mathbb C(x,y,q,\rho),\qquad
t=q^2,\quad L=\mathbb C(q,\rho),\quad K=\mathbb C(q),
\qquad h=y/2+\rho.
\tag{1}
\]
The coefficient derivatives are
\(\partial_t=(2q)^{-1}\partial_q\) and \(\partial_\rho\), initially
fixing \(y\). Define elements of \(\mathcal F\) by
\[
\begin{aligned}
X&=x,&Y&=y+q^2x,\\
Z&=q+\frac hq x+qx^2,&
W&=h+\left(\frac{h^2}{2q^2}+q^2\right)x+\rho x^2.
\end{aligned}
\tag{2}
\]
These are polynomials in the time variable \(x\), but some coefficients
have poles at \(q=0\). They are not being asserted to be polynomial
coordinates of \(\mathbb C[x,y,q,\rho]\).

The projected entries and coefficient potentials are
\[
\begin{gathered}
z=q,\qquad w=h,\qquad
\sigma=h/q,\qquad
\vartheta=P(y)+q^2,\qquad
P(U)=\frac{(U+2\rho)^2}{8q^2},\\
k=\rho/q,\qquad
n=-\frac{\rho^2}{2q^3},\qquad
\ell=-\frac{\rho^3}{2q^5},\qquad
m=\frac{5\rho^4}{8q^7}-\frac q2 .
\end{gathered}
\tag{3}
\]
In particular \(R=k_\rho=1/q\), so \(f=1/R=q\).
The element \(h\) is only an abbreviation; it is not an additional
independent variable in (1).

## 2. All four universal potentials hold

We check the identities of
[universal184](weight-four-universal-chart-potentials-pass184-working.md)
directly. Since \(q_\rho=0\), the first two take the form
\[
\sigma=q'y+k,\qquad
z=Qy^2+k_ty+R\vartheta+n,\qquad Q=q''/2=-\frac1{8q^3}.
\tag{4}
\]
The first expression is \((y+2\rho)/(2q)=h/q\).
For independent \(U,V\), set
\[
M=U+2\rho,\qquad \zeta=V-P(U).
\]
Then the right side of the second expression, before evaluation, is
\(V/q-M^2/(8q^3)=\zeta/q\). At \(U=y,V=\vartheta\) one has
\(\zeta=q^2\), giving \(z=q\).

Write the third and fourth formal potentials as
\[
\begin{aligned}
S&=\frac{q'''}6U^3+\frac{k_{tt}}2U^2+R'UV+n_tU+n_\rho V,\\
T&=\frac{q''''}{24}U^4+\frac{k_{ttt}}6U^3+\frac{R''}2U^2V
       +\frac{n_{tt}}2U^2+n_{t\rho}UV+\frac{n_{\rho\rho}}2V^2.
\end{aligned}
\tag{5}
\]
Here \(q'''/6=1/(16q^5)\) and \(q''''/24=-5/(128q^7)\).
Substitution of (3), with coefficient derivatives before evaluation,
gives the useful completed expressions
\[
\begin{aligned}
S&=\frac{M^3}{16q^5}-\frac{\rho^3}{2q^5}
                    -\frac{MV}{2q^3},\\
T-\ell_tU-\ell_\rho V
 &=-\frac{5M^4}{128q^7}+\frac{5\rho^4}{8q^7}
                 +\frac{3M^2V}{8q^5}-\frac{V^2}{2q^3}.
\end{aligned}
\tag{6}
\]
Thus the polynomial obtained from the third potential is
\[
w(U,V)=\frac{\ell-S}{R}=\frac{M\zeta}{2q^2}.
\]
At \(\zeta=q^2\), it is \(M/2=h\), and \(Rw+S=\ell\).
Also \(R'U+n_\rho=-M/(2q^3)\). Substituting \(V=P(U)+\zeta\)
in (6) therefore yields
\[
(R'U+n_\rho)w(U,V)+T-\ell_tU-\ell_\rho V
 =\frac{5\rho^4}{8q^7}-\frac{\zeta^2}{2q^3}.
\tag{7}
\]
At the selected branch \(\zeta=q^2\), this is precisely \(m\).
The fourth universal potential, including its coefficient derivatives,
is verified. The \(q_{\rho\rho}w^2/2\) term is zero here because
\(q_\rho=0\), not because it was omitted from the universal identity.

Equivalently the undivided eliminant is
\[
\begin{aligned}
\mathcal H(U,V)
&=R(T-\ell_tU-\ell_\rho V-m)
                    +(R'U+n_\rho)(\ell-S)\\
&=-\frac{(V-P(U))^2}{2q^4}+\frac12.
\end{aligned}
\tag{8}
\]
The selected factor \(V-P(U)-q^2\) is simple. Its evaluated cofactor
is \(-1/q^2\in L^*\); the other factor differs by \(2q^2\).
These are exact identities of rational functions, not numerical tests.

## 3. Full determinant and projected field return

At fixed \(x\), use independent variables \(y,q,h\) in place of
\(y,q,\rho\). The change \(h=y/2+\rho\) has determinant one.
The Jacobian matrix of \((Y,Z,W)\) is
\[
\begin{pmatrix}
1&2qx&0\\
0&1+x^2-hx/q^2&x/q\\
-x^2/2&(-h^2/q^3+2q)x&1+hx/q^2+x^2
\end{pmatrix}.
\tag{9}
\]
Its determinant is
\[
(1+x^2-hx/q^2)(1+x^2+hx/q^2)
 -(x/q)(-h^2/q^3+2q)x-x^4=1.
\]
Consequently the full four-variable rational map (2) has
\[
\det\frac{\partial(X,Y,Z,W)}{\partial(x,y,q,\rho)}=1.
\tag{10}
\]
This is not a polynomial Jacobian example: the map has the poles
already displayed in (2).

For the coefficient calibration use
\[
v=-\frac{y}{2q},\qquad N=\partial_v=-2q\partial_y.
\]
Thus \(L[v]=L[y]\), \(Nv=1\), and \(\Gamma=Ny=-2q\).
The change from \((t,\rho,y)\) to \((y,q,\rho)\) has determinant
\(1/(2q)\), and \(y_v=-2q\). Equation (10) gives, for every \(x\),
\[
\det\frac{\partial(Y,Z,W)}{\partial(t,\rho,y)}=\frac1{2q},
\qquad
\det\frac{\partial(Y,Z,W)}{\partial(t,\rho,v)}=-1.
\tag{11}
\]
Both the sign and the affine-parameter factor are retained.
The formal speed is \(E X=1\), for \(E=\partial_x\) on \(\mathcal F\).
Thus (11) has exactly the numerical shape of the calibrated actual
identity \(-a_E^3\), even though actualness has not been established.

At \(x=0\), the projected map has the polynomial inverse
\[
(y,z,w)=(y,q,y/2+\rho),\qquad q=z,\quad \rho=w-y/2.
\tag{12}
\]
It follows that
\[
L[y,z,w]=L[v],\qquad
\mathbb C(y,z,w)=\mathbb C(y,q,\rho)=L(v).
\]
These are the whole-line and exact projected-field equalities.
They do not say that the original map (2) is birational.

## 4. The invariant identity and exact original field degree

Direct expansion of (2) gives
\[
I:=Z^2-X^3Y-2XW=q^2.
\tag{13}
\]
For completeness, the constant coefficient of \(Z^2-X^3Y\) in \(x\)
is \(q^2\). Its coefficients of \(x,x^2,x^3\) are respectively
\(2h,\ h^2/q^2+2q^2,\ 2\rho\); its \(x^4\) coefficient is zero.
These are exactly the positive-degree coefficients of \(2XW\).
Thus (13) is the full identity, not only a leading cancellation.
It is killed by \(E=\partial_x\) in the ambient rational field.

Set \(B_0=\mathbb C[X,Y,Z,W]\subset\mathcal F\) and
\(M_0=\operatorname{Frac}B_0\). The notation is initially for the
subalgebra generated by the four displayed elements; independence
will now be justified. Equation (13) makes \(q\) algebraic over
\(M_0\), while
\[
x=X,\qquad
y=Y-q^2X,\qquad
h=\frac{qZ-q^2(1+X^2)}{X},\qquad
\rho=h-y/2
\tag{14}
\]
recovers every generator of \(\mathcal F\) over \(M_0(q)\).
The divisions in (14) are field operations, not polynomial inverses.
Therefore
\[
\mathcal F=M_0(q),\qquad [\mathcal F:M_0]\le2.
\tag{15}
\]
Since \(\mathcal F\) has transcendence degree four, so does \(M_0\).
The four generators of \(B_0\) are consequently algebraically
independent. Thus \(B_0\) really is a polynomial four-ring in these
generators.

In that polynomial ring, \(I=Z^2-X^3Y-2XW\) is irreducible.
As a polynomial of degree one in \(W\), its two coefficients
\(-2X\) and \(Z^2-X^3Y\) are coprime in \(\mathbb C[X,Y,Z]\):
the second is not divisible by \(X\).
It is primitive and irreducible over the fraction field, so Gauss's
lemma proves irreducibility in \(B_0\).
Its prime valuation in \(M_0\) is one, whereas every square has even
valuation. In particular \(I\) is not a square in \(M_0\).
Using (13)--(15), we obtain the exact conclusion
\[
q\notin M_0,\qquad
[\mathcal F:M_0]=2.
\tag{16}
\]
No step asserted \(q\in M_0\) before proving this opposite conclusion.

## 5. Why this is not an actual sliced frame

The derivation \(E=\partial_x\) is defined on the ambient field, and
the four entries have exact time degrees \(1,1,2,2\) there, with
leading coefficients
\[
(EX,EY,E^2Z/2,E^2W/2)=(1,q^2,q,\rho).
\tag{17}
\]
It cannot preserve \(B_0\): preservation would put
\(q=E^2Z/2\) in \(B_0\), contradicting (16).
Thus it does not define the actual locally nilpotent derivation on
the polynomial ring generated by \(X,Y,Z,W\) required by the
cancellation setup.

Even the formal leading map with the coefficients in (17) has full
kernel \((\mathsf Z^2-\mathsf X^3\mathsf Y)\).
Its image field contains \(\eta\), \(q\), and \(\rho\), so has
transcendence degree three. Its kernel has height one and contains
the irreducible polynomial \(\mathsf Z^2-\mathsf X^3\mathsf Y\).
The latter is primitive and linear in \(\mathsf Y\), with coprime
coefficients, which proves irreducibility. The height-one prime is
therefore exactly its principal ideal. This is a formal coefficient
statement, not an initial algebra for an LND of \(B_0\).

One can also formulate the obstruction under the missing actual
hypothesis. If an actual realization of these exact identities put
the leading ratio \(q\) in \(\operatorname{Frac}B_0\), then (13)
would make it integral over \(B_0\). Normality would imply
\(q\in B_0\), contradicting the irreducibility and nonsquare property
of \(I\). In the formal fixture itself, that fraction-field membership
is false; the correct obstruction is already the index two in (16).

This example excludes only the displayed exact fixture from actual
realization. It does not exclude other lower potentials in the
\(f=q\) family, any other family in195, or all positive bad-rank
initial forms. It establishes precisely that the universal potentials,
formal full leading relation, whole projected line, projected field
return, and constant full Jacobian do not by themselves imply an
original polynomial inverse or even original-map birationality.

No195 or earlier source was changed. The proof consists of the explicit
identities and field arguments above; no saved checker was executed,
imported, or compiled. No cancellation counterexample, unrestricted
solution, novelty certification, or formal verification is claimed.

