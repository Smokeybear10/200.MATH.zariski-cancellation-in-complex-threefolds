# The normalized square-root graph is incompatible with an actual frame

Status: bounded working conditional exclusion. In the actual
\(Z^2-X^3Y\) chart, the normalized family below cannot occur for any
nonzero \(g\) in the exact coefficient field, whether or not that field
is rational. The obstruction is an original polynomial equal to
\(g^2\): normality would make \(g\) polynomial, but that polynomial is
irreducible.

This is not an exclusion of every surviving family in
[two-gate195](weight-four-square-root-two-gate-classification-pass195-working.md).
The normalization of arbitrary lower potentials to this family is
not proved here.

## 1. Exact conditional hypotheses

Retain the actual supplied-frame hypotheses of
[universal184](weight-four-universal-chart-potentials-pass184-working.md):
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\\
\deg_E(X,Y,Z,W)=(1,1,2,2),\qquad
\ker\theta_0=(\mathsf Z^2-\mathsf X^3\mathsf Y),\\
L=\operatorname{Frac}(\ker_A N),\qquad A_L=L[v],\qquad
t=(EY)/(EX),\quad \rho=(E^2W/2)/(EX)^2,\quad
q=(E^2Z/2)/(EX)^2,\quad q^2=t,\\
[L:\mathbb C(t,\rho)]<\infty,\qquad
K=\ker_L\partial_\rho,\qquad [K:\mathbb C(t)]<\infty .
\end{gathered}
\tag{1}
\]
The initial ideal is the full kernel, and the four original generators
are polynomial coordinates. Their actual projection has
\[
\begin{gathered}
Y=y+tX,\qquad Z=z+(q'y+k)X+qX^2,\qquad
W=w+\vartheta X+\rho X^2,\\
L[y,z,w]=L[v],\qquad \mathbb C(y,z,w)=L(v).
\end{gathered}
\tag{2}
\]
The coefficient partials commute. Primes on \(K\) denote the extension
of \(d/dt\), with constant field \(\mathbb C\).

Impose the following additional normalization, as a hypothesis:
\[
k=\frac{\rho}{q},\qquad
n=-\frac{\rho^2}{2q^3},\qquad
z=g\in L^* .
\tag{3}
\]
Thus \(R=k_\rho=1/q\), so \(f=1/R=q\), and the lower coefficients
\(k_0,s_0,n_0\) vanish. We do not assume \(K=\mathbb C(q)\).
Membership \(g\in K\) is not assumed; it will follow from the scalar
Jacobian. No proof that a general \(f=q\) square graph reaches (3)
is included.

## 2. The potentials determine the harmless additive constant

Put \(Q=q''/2=-1/(8q^3)\). The second universal potential in this
\(q_\rho=0\) chart is
\[
z=Qy^2+k_ty+R\vartheta+n .
\]
Using (3) it gives
\[
\vartheta=P(y)+qg,\qquad
P(U)=\frac{(U+2\rho)^2}{8q^2}.
\tag{4}
\]
For the next two potentials use independent \(U,V\), and let
\[
\begin{aligned}
S&=\frac{q'''}6U^3+\frac{k_{tt}}2U^2+R'UV+n_tU+n_\rho V,\\
T&=\frac{q''''}{24}U^4+\frac{k_{ttt}}6U^3+\frac{R''}2U^2V
 +\frac{n_{tt}}2U^2+n_{t\rho}UV+\frac{n_{\rho\rho}}2V^2.
\end{aligned}
\]
Write
\[
\ell_*=-\frac{\rho^3}{2q^5},\qquad
\varepsilon=\ell-\ell_*\in L,\qquad h=y/2+\rho.
\]
The exact completed expressions checked in Section 2 of
[index-two196](weight-four-square-root-formal-index-two-boundary-pass196-working.md)
give, with \(M=U+2\rho\),
\[
S=\frac{M^3}{16q^5}-\frac{\rho^3}{2q^5}
                    -\frac{MV}{2q^3}.
\]
Consequently \(Rw+S(y,\vartheta)=\ell\) implies
\[
w=\frac{hg}{q}+q\varepsilon .
\tag{5}
\]
Equations (4)--(5) show that if \(y\in L\), then \(y,z,w\in L\),
contradicting \(L[y,z,w]=L[v]\). Thus \(y\) is nonconstant in \(L[v]\)
and is transcendental over \(L\). In fact all three projected entries
are in \(L[y]\), so the whole-line equality makes \(y\) affine in \(v\).
Only transcendence is needed for the following comparison.

The fourth universal potential is
\[
(R'y+n_\rho)w+T(y,\vartheta)-\ell_t y-\ell_\rho\vartheta=m,\qquad m\in L.
\]
The completed calculation before evaluating \(V\) gives
\[
\begin{aligned}
&(R'U+n_\rho)\frac{(U+2\rho)(V-P(U))}{2q^2}
       +T-\ell_{*,t}U-\ell_{*,\rho}V\\
&\hspace{35mm}
=\frac{5\rho^4}{8q^7}-\frac{(V-P(U))^2}{2q^3}.
\end{aligned}
\]
Use \(V=P(U)+qg\) and add the terms coming from \(\varepsilon\).
The fourth potential becomes the following polynomial identity in
the transcendental \(y\):
\[
m=\frac{5\rho^4}{8q^7}-\frac{g^2}{2q}
 -\frac{(y+2\rho)\varepsilon}{2q^2}
 -\varepsilon_t y-\varepsilon_\rho\bigl(P(y)+qg\bigr).
\tag{6}
\]
Its \(y^2\) coefficient is \(-\varepsilon_\rho/(8q^2)\), so
\(\varepsilon_\rho=0\). Thus \(\varepsilon\in K\). The \(y\)
coefficient then gives
\[
\varepsilon'+\frac{\varepsilon}{2q^2}=0,\qquad
(q\varepsilon)'=0.
\]
The exact constant field yields a complex constant \(C\) with
\[
q\varepsilon=C,\qquad
w=\frac{hg}{q}+C,\qquad
m=\frac{5\rho^4}{8q^7}-\frac{g^2}{2q}-\frac{C\rho}{q^3}.
\tag{7}
\]
In particular \(k_0=s_0=n_0=0\) alone should not silently be used
to set \(\ell-\ell_*=0\). The potential equations leave precisely
the additive constant \(C\) in (7). The actual constant translation
\(W\mapsto W-C\), whose inverse is \(W\mapsto W+C\), removes it.

## 3. The full original polynomial identity

The actual chart entries now read
\[
\begin{aligned}
Y&=y+q^2X,\\
Z&=g+\frac hq X+qX^2,\\
W&=\frac{hg}{q}+C+
       \left(\frac{h^2}{2q^2}+qg\right)X+\rho X^2.
\end{aligned}
\tag{8}
\]
These identities are in the actual localized ring and its fraction
field, not a replacement of the original polynomial coordinates.
Direct expansion gives
\[
\boxed{\,Z^2-X^3Y-2X(W-C)=g^2.\,}
\tag{9}
\]
Indeed \(Z^2-X^3Y\), as a polynomial in \(X\), has coefficients
\[
g^2,\quad 2gh/q,\quad h^2/q^2+2qg,\quad 2h-y=2\rho,\quad 0.
\]
The last four are exactly the coefficients canceled by
\(2X(W-C)\). No derivative of \(g\) and no representation of \(g\)
as a rational function of \(q\) is used in this identity.

The actual scalar determinant now places \(g\) in the smaller exact
field \(K\). We already proved that \(y\) is affine in \(v\); put
\(\Gamma=Ny\in L^*\). The change of coefficient parameter gives
\[
\det\frac{\partial(Y,Z,W)}{\partial(t,\rho,y)}
 =-\frac{(EX)^3}{\Gamma}\in L^*.
\]
This identity is independent of \(X\). Evaluate it at \(X=0\),
where \((Y,Z,W)=(y,g,hg/q+C)\), and take coefficient partials
fixing \(y\). Direct expansion, with \(h=y/2+\rho\), gives
\[
\begin{aligned}
\det\frac{\partial(y,g,hg/q+C)}{\partial(t,\rho,y)}
 &=g_t\left(\frac gq+\frac{hg_\rho}q\right)
   -g_\rho h\left(\frac{g_t}q-\frac{gq_t}{q^2}\right)\\
 &=\frac{g g_t}q+\frac{h g g_\rho q_t}{q^2}.
\end{aligned}
\tag{10}
\]
Its \(y\) coefficient is \(gg_\rho q_t/(2q^2)\).
The determinant is in \(L^*\), whereas \(y\) is transcendental over
\(L\). Since \(g\ne0\) and \(q_t=1/(2q)\ne0\), we obtain
\[
g_\rho=0,\qquad g\in K,\qquad
\Gamma\,\frac{gg'}q=-(EX)^3\ne0.
\]
Thus \(g'\ne0\) as well. The speed and affine-parameter factor have
both been retained. These are the uniquely extended coefficient
derivations on \(L\), not an assumption that the coefficient field is
rational or that \(q\) is a global coordinate.

## 4. Normality contradicts the square

The actual hypothesis in (1) is essential at this point. It gives
\[
g\in K\subset L\subset\operatorname{Frac}A
 \subset\operatorname{Frac}B.
\]
By (9), \(g\) satisfies a monic polynomial over \(B\), namely
\[
T^2-I_C,\qquad I_C=Z^2-X^3Y-2X(W-C)\in B.
\]
The polynomial ring \(B\) is integrally closed, so \(g\in B\).
Hence \(I_C\) would be a square in \(B\).

On the other hand \(I_C\) is irreducible in that polynomial ring.
As a polynomial in \(W\) over \(\mathbb C[X,Y,Z]\), it has degree
one, and its coefficients are
\[
-2X,\qquad Z^2-X^3Y+2CX.
\]
They are coprime, since the second coefficient reduces to \(Z^2\)
modulo \(X\). Thus \(I_C\) is primitive and is irreducible over the
fraction field as a nonconstant linear polynomial. Gauss's lemma
proves irreducibility in \(B\). It is a nonunit, and no nonunit
irreducible in a polynomial UFD is a square. This contradicts (9)
and proves the conditional exclusion.

The same contradiction can be expressed using the prime valuation
of \(I_C\), which is one on \(I_C\) and even on every square in
\(\operatorname{Frac}B\). The normality proof above makes explicit
why the coefficient-field element \(g\) descends under the actual
hypotheses. This membership must not be inferred for a formal
rational chart: the exact formal fixture196 instead has an
original field extension of degree two.

## Scope

The conclusion is only that the actual normalized family (3) is
impossible. It starts with arbitrary \(g\in L^*\), derives \(g\in K\)
from the scalar determinant, and retains the additive constant in (7).
It does not assume a rational coefficient field or make a generic
parameter into a coordinate. A proof that more general
lower potentials admit the required actual normalization remains
a separate task. This note does not exclude all the surviving
two-gate families, other positive-rank initial forms, or arbitrary
entry, and it does not settle unrestricted cancellation.

No195 or earlier file was edited. No saved checker was executed,
imported, or compiled. The identity and irreducibility arguments
are elementary and explicit; no external classification theorem,
formal verification, human expert certification, or novelty claim
is asserted.
