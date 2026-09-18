# The normalized nonmonomial square-root graph is impossible

Status: bounded working proof, pending independent saved-source review.
The actual graph alternative for the nonmonomial family
\(f=at+bq\), \(ab\ne0\), is excluded after the actual normalization199.
The quadratic-projection alternative is not treated here.
The obstruction is an exact degree-three failure of projected field
return, not an assertion that a scalar Jacobian supplies an inverse.

## 1. Actual hypotheses and the normalized graph

Retain the supplied actual configuration of
[universal184](weight-four-universal-chart-potentials-pass184-working.md),
[reduction195](weight-four-double-cover-nonzero-r-reduction-pass195-working.md),
and the actual maps in
[normalization199](weight-four-nonmonomial-square-root-actual-normalization-pass199-working.md).
Thus
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=\mathcal A[u],\qquad E=\partial_u,\qquad
\deg_E(X,Y,Z,W)=(1,1,2,2),\\
\ker\theta_0=(\mathsf Z^2-\mathsf X^3\mathsf Y),\qquad
a_E=EX,\quad t=EY/a_E,\quad q=E^2Z/(2a_E^2),\quad q^2=t,\\
\rho=E^2W/(2a_E^2),\qquad
N=[u^3](\partial_Z|_{\mathcal A})\ne0,\qquad
L=\operatorname{Frac}(\ker_{\mathcal A}N),\qquad
\mathcal A_L=L[v],\quad Nv=1,\\
K=\ker_L\partial_\rho,\qquad [K:\mathbb C(q)]<\infty,\qquad
\ker_K\partial_q=\mathbb C .
\end{gathered}
\tag{1}
\]
The entire initial kernel is prescribed. The ratios \(t,\rho\) are
independent, \(a_E\in L^*\), and the coefficient partials commute on
the exact finite fields. Subscripts \(q\) hold \(\rho\) fixed;
\(\partial_t=(2q)^{-1}\partial_q\). No rationality of \(K\) is assumed.

The actual projected chart and return are
\[
\begin{gathered}
Y=y+q^2X,\qquad Z=z+\left(\frac{y}{2q}+k\right)X+qX^2,\qquad
W=w+\vartheta X+\rho X^2,\\
L[y,z,w]=L[v],\qquad \mathbb C(y,z,w)=L(v),\qquad
\det\frac{\partial(Y,Z,W)}{\partial(t,\rho,v)}
       =-a_E^3\in L^* .
\end{gathered}
\tag{2}
\]
In particular \(y,z,w\) are algebraically independent over
\(\mathbb C\). These are consequences of actual polynomial coordinates
and the fixed-\(X\) projection, not formal coefficient assumptions.

Normalization199 supplies actual polynomial changes, with polynomial
inverses and preservation of the selected fields and alternatives,
which make
\[
\begin{gathered}
f=q(q+1),\qquad R=k_\rho=\frac1{q(q+1)},\qquad
\nu=n_{\rho\rho}=\frac1{q^3(q+1)^3(3q-1)},\\
k=R\rho,\qquad n=\frac{\nu\rho^2}{2},\qquad
\ell=L_3\rho^3+l,\quad l\in K,\\
L_3=-\frac{q^2+4q-1}{2q^5(q+1)^5(3q-1)^3}.
\end{gathered}
\tag{3}
\]
All denominators here are nonzero elements of the coefficient field.
They are not declared units in \(B\).

Assume the selected component is a graph in the nonconstant coordinate
\(y\), so \(\vartheta\in L[y]\). Since \(R\in L^*\), the second and
third universal potentials express \(z,w\) in \(L[y,\vartheta]\).
Equation (2) therefore gives
\[
L[y]=L[v],\qquad \Gamma:=Ny\in L^*,\qquad
\mathbb C(y,z,w)=L(y).
\tag{4}
\]
This proves that \(y\) is affine in \(v\); it does not set \(\Gamma=1\).

## 2. Literal square completion and simplified projected entries

Use independent \(U,V\). The second potential has quadratic term
\(Q=-1/(8q^3)\). For the third and fourth potentials write
\[
\begin{aligned}
S&=\frac{U^3}{16q^5}+\frac{R_{tt}\rho}{2}U^2
       +R_tUV+\frac{\nu_t\rho^2}{2}U+\nu\rho V,\\
T&=-\frac{5U^4}{128q^7}+\frac{R_{ttt}\rho}{6}U^3
       +\frac{R_{tt}}2U^2V+\frac{\nu_{tt}\rho^2}{4}U^2
       +\nu_t\rho UV+\frac{\nu}{2}V^2,\\
\mathcal H&=R(T-\ell_tU-\ell_\rho V-m)
                    +(R_tU+\nu\rho)(\ell-S),\qquad m\in L .
\end{aligned}
\tag{5}
\]
Every derivative in (5) is a coefficient derivative before evaluation.
The actual identities are
\(z=Qy^2+R_t\rho y+R\vartheta+\nu\rho^2/2\),
\(Rw+S(y,\vartheta)=\ell\), and
\(\mathcal H(y,\vartheta)=0\).

Put
\[
\begin{aligned}
P(U)&=p_2U^2+p_1\rho U+p_0\rho^2,\\
p_2&=-\frac{(q+1)(3q-1)}{8q^2},\\
p_1&=\frac{9q^2+4q-1}{2q^2(q+1)(3q-1)},\\
p_0&=-\frac{3q^2+6q-1}{2q^2(q+1)^2(3q-1)^2},
\qquad A_2=\frac{R\nu}{2},\qquad g=\frac lR .
\end{aligned}
\tag{6}
\]
Direct coefficient comparison in (5) gives the exact square completion
\[
\begin{gathered}
\mathcal H=A_2(V-P(U))^2-\frac{R^2}{2q}g_q\,U+B_0,\\
B_0=-Rm+\nu\rho l+
          \left(\nu L_3-\frac{R\nu p_0^2}{2}\right)\rho^4 .
\end{gathered}
\tag{7}
\]
For example, the \(V^2\), \(U^2V\), \(UV\), and \(V\) coefficients
give \(A_2\) and the three entries of (6); the \(U\) coefficient is
\(-Rl_t+R_tl=-R^2g_q/(2q)\).
The coefficients of \(U^4,U^3,U^2\) in the residual vanish.
The formula for \(B_0\) follows simply by setting \(U=V=0\)
before subtracting \(A_2P(0)^2\).

Let \(\zeta=\vartheta-P(y)\in L[y]\). Since \(y\) is
transcendental over \(L\), equation (7) makes \(\zeta^2\) a
polynomial of degree at most one in \(y\). A nonconstant polynomial
square has positive even degree. Consequently
\[
\zeta=\gamma\in L,\qquad g_q=0,\qquad g=C\in\mathbb C,\qquad l=CR .
\tag{8}
\]
This does not assume \(\gamma\ne0\) or \(\gamma\in K\).
The actual constant translation \(W\mapsto W-C\) would remove \(C\),
but retaining it makes the identities explicit.

Define
\[
D=q(q+1)(3q-1),\qquad
h=\frac{y}{2q}-\frac{\rho}{D},\qquad
\xi=R\gamma .
\tag{9}
\]
These are elements of \(L[y]\), not declared original polynomial
coordinates. Substituting \(\vartheta=P(y)+\gamma\) in the second
and third potentials gives
\[
\boxed{\quad
z=\xi-\frac32h^2,\qquad
w=(h+y)z+\frac12h^3+C .
\quad}
\tag{10}
\]
One can verify (10) without a field or geometric argument:
substitute (6) into
\(Qy^2+R_t\rho y+R(P(y)+\gamma)+\nu\rho^2/2\) and into
\((L_3\rho^3+CR-S(y,P(y)+\gamma))/R\), respectively.
Their coefficients in the independent symbols \(y,\rho,\gamma,C\)
give the two expressions in (10).

## 3. The calibrated scalar Jacobian, with its parameter factor

Set
\[
\omega=w-yz-C=h\xi-h^3=hz+\frac12h^3.
\tag{11}
\]
At fixed \(y\), subtracting \(y\,dz\) from \(dw\) shows that the
Jacobian of \(y,z,w\) equals that of \(y,z,\omega\).
Differentiating the first expression in (10) and (11) gives
\[
dz=d\xi-3h\,dh,\qquad
d\omega=h\,d\xi+(\xi-3h^2)\,dh,\qquad
dz\wedge d\omega=\xi\,d\xi\wedge dh .
\]
Thus in columns \((q,\rho,y)\),
\[
\begin{aligned}
J_y
&=\xi(\xi_qh_\rho-\xi_\rho h_q)\\
&=\xi\left\{-\frac{\xi_q}{D}
       +\frac{y\,\xi_\rho}{2q^2}
       -\frac{\rho D_q\,\xi_\rho}{D^2}\right\}
 =-\frac{2q\,a_E^3}{\Gamma}\in L^* .
\end{aligned}
\tag{12}
\]
The last factor is obtained from \(dt=2q\,dq\) and
\(dy=\Gamma\,dv\) along the generic line.
No original-ring unit conclusion about \(a_E\) is used.

Nonvanishing first forces \(\xi\ne0\). Independence of \(y\)
then gives \(\xi_\rho=0\), hence \(\xi\in K^*\), and the remaining
constant coefficient gives \(\xi_q\ne0\).
In particular \(\xi\) is transcendental over \(\mathbb C\).
These are necessary scalar-Jacobian restrictions. They are consistent
as coefficient identities and are not themselves the contradiction.

## 4. Exact projected field return contradicts a cubic degree

Here the actual return in (4), not a formal nonzero Jacobian, is decisive.
Because \(C\) is complex, (11) gives
\(\mathbb C(y,z,w)=\mathbb C(y,z,\omega)\).
The two inclusions from (10) and \(h,\xi\in L(y)\) are
\[
L(y)=\mathbb C(y,z,\omega)
       \ \subseteq\ \mathbb C(y,h,\xi)
       \ \subseteq\ L(y).
\tag{13}
\]
Hence both are equalities. The field \(L(y)\) has transcendence
degree three over \(\mathbb C\), so its three displayed generators
\(y,h,\xi\) are algebraically independent.
Replacing \(\xi\) by \(z=\xi-3h^2/2\) gives
\[
\mathbb C(y,z,h)=\mathbb C(y,z,\omega),\qquad
\omega=zh+\frac12h^3,
\tag{14}
\]
where \(y,z,h\) are algebraically independent.

For completeness, take \(F=\mathbb C(y,z)\). For independent symbols
\(H,S\), the polynomial
\[
H^3+2zH-2S\in F[H,S]
\tag{15}
\]
is irreducible: the quotient by it is \(F[H]\), since its coefficient
of \(S\) is the nonzero scalar \(-2\), and this is a domain.
As a polynomial in \(H\) over \(F[S]\) it is primitive.
Gauss's lemma therefore makes it irreducible over \(F(S)\).
The element \(\omega=zh+h^3/2\) is transcendental over \(F\);
otherwise \(h\) would be algebraic over \(F\).
Specializing the coefficient-field isomorphism \(F(S)\simeq F(\omega)\)
shows
\[
[\,F(h):F(\omega)\,]=3 .
\tag{16}
\]
This contradicts (14).

In fact (13)--(16) do not require the additional descent
\(\xi\in K\) established in Section 3. The exact actual return itself
already ensures the independence needed for the cubic argument.
Thus there is no hidden inference \(K=\mathbb C(q)\), no assumed
descent \(L=K(\rho)\), and no use of a rational inverse as an original
polynomial coordinate change.

## Scope

This excludes the actual nonmonomial graph branch after the complete
actual normalization199. It does not exclude or recognize the
nonmonomial quadratic-projection branch. It does not treat the
two-root cover's nonzero-\(R\) alternatives, other initial forms,
higher profiles, arbitrary entry, or unrestricted cancellation.

The universal184 source, the differential classification195, the
normalized reciprocal graph198, and the complete actual normalization199
were read before this proof was saved. New inline coefficient arithmetic
independently confirmed (6)--(7) and (10); the determinant and cubic
field argument are reconstructed in full above. No saved checker was
executed, imported, compiled, or edited. Earlier artifacts are unchanged.
This is a bounded working proof, not a historical novelty claim,
human expert certification, or proof-assistant verification.
