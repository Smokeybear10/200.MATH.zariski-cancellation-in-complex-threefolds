# A nonconstant leading ratio is impossible in the pure quadratic cusp graph

Status: working proof pending independent review of this saved artifact.
Retain the actual cusp chart and a pure quadratic graph relation.
The graph intercept is not assumed linear in rho. The determinant
forces it to be at most quadratic, and the resulting leading ratio
cannot be nonconstant in the coefficient field.

The proof uses the exact projected field equality twice: first at
rho-infinity, then as a degree-one rational map. It does not assume
the coefficient field is rational before deriving that conclusion.
The nonzero constant-ratio case is not settled here. No frozen170
or earlier source, checker, packet or index is changed.

## 1. Actual hypotheses and unrestricted quadratic intercept

Retain the actual chart159: \(B=A[u]=\mathbb C[X,Y,Z,W]\),
\(E=\partial_u\), exact E-time degrees \((1,1,2,2)\), and full
weighted initial ideal \((XZ-Y^3)\). Let
\(a=EX\ne0\), \(N=[u^3](\partial_Z|_A)\), and
\(L=\operatorname{Frac}(\ker_A N)\). Write \(t=\tau\).
All the exact-field, whole-line and actual projected-ring hypotheses
of159 remain in force:
\[
\begin{gathered}
A_L=L[v],\quad Nv=1,\quad L[y,\vartheta]=L[v],\qquad
\operatorname{Frac}A=\mathbb C(y,z,w)=L(v),\\
L/\mathbb C(t,\rho)\text{ finite separable},\qquad
z=3ty^2+k_t y+r\vartheta+n,\quad r=k_\rho\ne0,\\
rw+y^3+H_2(k;y,\vartheta)+H_1(n;y,\vartheta)=\ell .
\end{gathered}
\tag{1}
\]
The extended coefficient partials commute and have joint constants
\(\mathbb C\). The \(H_j\) are the ordinary homogeneous Taylor
coefficients with their factorials.

Assume a quadratic graph \(\vartheta=P(y)\),
\(P=p_2Y_0^2+p_1Y_0+p_0\in L[Y_0]\), \(p_2\ne0\), and
the pure whole relation
\[
\Phi-m=\lambda\{V_0-P(Y_0)\},\qquad \lambda\in L^* .
\tag{2}
\]
Here \(Y_0,V_0\) are independent formal plane variables.
The pure relation is an explicit hypothesis. No extra-factor
classification is needed for the conditional argument.
Also \(L[y]=L[v]\), so \(y\) is an affine parameter over \(L\).

Put \(K=\ker_L\partial_\rho\). Minimal-polynomial differentiation,
as reconstructed in170, gives
\([K:\mathbb C(t)]<\infty\),
\(\ker_K\partial_t=\mathbb C\), and the transcendence of rho over
\(K\). A prime denotes the extended derivative on \(K\).
No assertion \(K=\mathbb C(t)\) is made.

The literal degree-two potential gives, just as in170 before its
extra intercept assumption is used,
\[
\begin{gathered}
r\in\mathbb C^*,\quad k=r\rho+k_0,\qquad
n=s\rho+n_0,\quad s\in\mathbb C,\quad k_0,n_0\in K,\\
k_0'''=6s/r,\qquad
\lambda=-s^2/r-\ell_\rho,\\
p_2=\{s k_0''/(2r)-n_0''/2\}/\lambda,\qquad
p_1=\{s n_0'/r+\ell_t\}/\lambda .
\end{gathered}
\tag{3}
\]
Indeed the quartic part first forces both coefficient derivatives of
r to vanish; the \(V_0^2\) and \(Y_0V_0\) coefficients force
\(n_{\rho\rho}=n_{t\rho}=0\). The cubic coefficient gives the
displayed third derivative of \(k_0\).

Using \(y\) as the third separating parameter, the full determinant
is \(-\lambda\mathcal S=-a^3/y_v\in L^*\), where
\[
\mathcal S=P_t+P_{Y_0}P_\rho+(s/r)P_{Y_0}
                  +(3Y_0^2+k_0''Y_0+n_0')/r\in L^* .
\tag{4}
\]
The \(Y_0^3\) coefficient is \(2p_2(p_2)_\rho\). Hence
\((p_2)_\rho=0\), and the nonzero numerator in (3) gives
\(\lambda_\rho=0\). Write
\[
\begin{gathered}
\chi=1/\lambda\in K^*,\quad \alpha=\chi'/\chi,\qquad
\ell=(-1/\chi-s^2/r)\rho+\ell_0,\quad \ell_0\in K,\\
p_1=\alpha\rho+b,\qquad b=\chi(s n_0'/r+\ell_0')\in K,\\
p_2'+2\alpha p_2+3/r=0,\qquad
p_0=d_2\rho^2+e\rho+d_0,\quad e,d_0\in K,\qquad
d_2=-\frac{\alpha'+\alpha^2}{4p_2}
    =-\frac{\chi''}{4\chi p_2}.
\end{gathered}
\tag{5}
\]
The last line follows from the \(Y_0^2\) and \(Y_0\) coefficients
of (4). More explicitly the latter says
\[
2p_2(p_0)_\rho
=-(\alpha'+\alpha^2)\rho-b'-\alpha b-2sp_2/r-k_0''/r .
\]
Subtract the explicit quadratic primitive in rho; its residual lies
in \(K\). This proves (5) over the exact field without arbitrary
algebraic antiderivatives and without assuming \(d_2=0\).

## 2. A polynomial projected coordinate and a quadratic pencil

Define
\[
\begin{gathered}
c=sk_0-rn_0,\quad d=r\ell_0+sn_0,\quad
J=(st^3-rk_0)''/2\in\mathbb C,\qquad H=\chi(e+s/r)\in K,\\
c''=2rp_2/\chi\ne0,\qquad
\chi c'''+3\chi'c''+6=0,\qquad
\Gamma=-\frac{\chi''}{2c''}=\frac{\chi^2d_2}{r}.
\end{gathered}
\tag{6}
\]
The assertion about \(J\) uses \(k_0'''=6s/r\). The differential
identity follows by substituting \(p_2=\chi c''/(2r)\) in (5).
We seek a contradiction from \(\Gamma\notin\mathbb C\).
In particular this assumption makes \(d_2\ne0\).

Introduce an actual polynomial in the projected coordinates,
\(\mathcal U=r^2w+sz+ry^3-Jy^2\). Substitution in (1) gives
\[
\begin{gathered}
\mathcal U=c'y+d-r\rho/\chi,\qquad
C=c'y+d,\qquad
Z_0=(3t+rp_2)y^2+(k_0'+rb)y+n_0+rd_0,\\
z=Z_0+(r\alpha y+re+s)\rho+rd_2\rho^2\\
\phantom{z}
=\Gamma(\mathcal U-C)^2-(\chi'y+H)(\mathcal U-C)+Z_0\\
\phantom{z}
=\Gamma\mathcal U^2+A_1(y)\mathcal U+A_0(y),\\
A_1=-2\Gamma(c'y+d)-\chi'y-H,\qquad
A_0=\Gamma C^2+(\chi'y+H)C+Z_0,\qquad A_1,A_0\in K[y].
\end{gathered}
\tag{7}
\]
This construction is integral in the projected polynomial ring:
\(r,s,J\) are complex constants, and
\(w=(\mathcal U-sz-ry^3+Jy^2)/r^2\).
It is not a coefficient-dependent original coordinate change.
Since the rho coefficient of \(\mathcal U\) is \(-r/\chi\ne0\),
\(\mathcal U\) is transcendental over \(K(y)\).

All coefficients in (1) now belong to \(K[\rho]\). The actual field
equality and intersection with \(L\) therefore give
\[
L=K(\rho),\qquad
\mathbb C(y,z,\mathcal U)=K(y)(\mathcal U).
\tag{8}
\]
This is where the original polynomial inverse is used. A proper
projected subfield would not give (8).

## 3. The first field use makes Gamma a rational parameter

Put \(k_*=\mathbb C(y)\), \(M=K(y)\), and use the valuation at
\(\mathcal U=\infty\) on \(M(\mathcal U)\). Its residue field is
\(M\). Since \(\Gamma\notin\mathbb C\) and \(y\) is transcendental
over \(K\), \(\Gamma\) is transcendental over \(k_*\).

Give \(z,\mathcal U\) weights two and one. A nonzero highest weighted
part over \(k_*\), evaluated through (7), has leading coefficient
a nonzero polynomial in \(\Gamma\): its monomials of fixed weight
have distinct powers of \(\Gamma\). Thus leading cancellation
cannot occur. The residue of an equal-weight quotient belongs to
\(k_*(\Gamma)\), and conversely \(z/\mathcal U^2\) has residue
\(\Gamma\). The residue field of \(k_*(z,\mathcal U)\) is exactly
\(k_*(\Gamma)\). Equation (8) proves
\[
K(y)=\mathbb C(y,\Gamma),\qquad K=\mathbb C(\Gamma).
\tag{9}
\]
The second equality is intersection with \(K\). This rationality
is a consequence of actual field return, not an assumption on \(K\).
It is not itself a contradiction.

## 4. A second degree-one field use forces affine coefficients

The needed elementary statement is the following. Let \(k\) be a
field, \(T\) and \(U\) independent transcendental elements, and
\(a,b\in k(T)\). If
\[
k(U,T)=k(U,TU^2+a(T)U+b(T)),
\]
then \(a,b\in k+kT\).

Choose a common polynomial denominator \(D\in k[T]\setminus\{0\}\)
and write \(a=B/D,\ b=C_0/D\) with
\(\gcd(D,B,C_0)=1\). The numerator
\[
Q(T,U)=TD(T)U^2+B(T)U+C_0(T)
\tag{10}
\]
is coprime to \(D(T)\) in \(k(U)[T]\). Indeed, an irreducible
divisor of \(D\) would have to divide both \(B\) and \(C_0\):
reduce modulo that divisor and compare the coefficients of the
transcendental \(U\). Irreducibility of that divisor persists
under the purely transcendental extension \(k(U)/k\).

For coprime polynomials \(Q,D\), the degree of the rational map
\(T\mapsto Q/D\) equals \(\max(\deg_T Q,\deg_T D)\). One elementary
proof applies Gauss's lemma to \(Q(T,U)-Z D(T)\), which is primitive
and irreducible because it is linear in the independent \(Z\) and
its two coefficients are coprime. Its \(T\)-degree is the stated
maximum. This gives the same field extension degree over
\(k(U,Z)\).

The \(U^2\) coefficient in (10) has \(T\)-degree \(\deg D+1\)
and cannot be cancelled by terms with \(U\)-degree at most one.
Consequently degree-one field return forces \(\deg D=0\).
Now the numerator degree is
\(\max(1,\deg B,\deg C_0)\), by the same independence of \(U\).
It must be one. This proves the elementary statement, including
cases where either lower coefficient is zero.

Apply it using \(k=k_*\), \(T=\Gamma\), \(U=\mathcal U\), and
(7)--(9). It gives \(A_1,A_0\in k_*+k_*\Gamma\). In particular
\[
A_1\in K[y]\cap\{\mathbb C(y)+\Gamma\mathbb C(y)\},\qquad
[y]A_1=u_0+u_1\Gamma,\quad u_0,u_1\in\mathbb C .
\tag{11}
\]
For the coefficient assertion, choose a finite complex basis for
the span of \(1,\Gamma\) and the coefficients of \(A_1\), starting
with \(1,\Gamma\). Its members remain independent over
\(\mathbb C(y)\): clear a denominator and compare powers of \(y\).
Comparison in this basis proves that each coefficient lies in the
complex span of \(1,\Gamma\).

## 5. The coefficient derivative gives the contradiction

Equation (7) identifies \([y]A_1=-2\Gamma c'-\chi'\).
Using the definition of \(\Gamma\) in (6), differentiate inside
the exact field \(K\):
\[
(-2\Gamma c'-\chi')'
 =-2\Gamma'c'-2\Gamma c''-\chi''
 =-2\Gamma'c'.
\tag{12}
\]
Differentiating (11) therefore yields
\((-2c'-u_1)\Gamma'=0\). The assumed nonconstancy of \(\Gamma\)
implies \(\Gamma'\ne0\), since the constants of \(K\) are
\(\mathbb C\). Thus \(c'=-u_1/2\) and \(c''=0\), contrary to (6).
This excludes every nonconstant \(\Gamma\).

The remaining alternatives are \(\Gamma=0\), equivalently \(d_2=0\),
and \(\Gamma\in\mathbb C^*\). The first is the additional intercept
case recognized in170. This note does not settle the second, infer
that a nonzero constant ratio is impossible, or construct a new
global invariant in that case.

## Dependencies and verification scope

1. [Actual cusp chart159](cusp-generic-chart-first-reductions-pass159-working.md) supplies the actual projected ring and field, finite coefficient extension, whole line, potential and determinant.
2. [Conditional pure quadratic proof170](cusp-pure-quadratic-linear-intercept-pass170-working.md) supplies the coefficient mechanism before its extra intercept condition; the unrestricted rho integration and the two field arguments are proved here.
3. [Weighted residue proof169](cusp-quadratic-extra-factor-exclusion-pass169-working.md), Section4, gives the related weights-two-and-three mechanism. The weights-two-and-one version needed here is reconstructed in Section3 and does not use169's exclusion theorem.

No external classification or fresh regular-kernel theorem is needed
for this exclusion. No finite checker execution is claimed. The note
is a working proof pending saved-source review, not expert verification,
proof-assistant certification, a recursive source audit or novelty
clearance. Other graph degrees, zero-r charts, other initial forms and
unrestricted cancellation remain outside the conclusion.
