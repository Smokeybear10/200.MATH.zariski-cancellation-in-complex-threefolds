# Exact coefficient normal forms in the zero-r, nonzero-s cusp branch

**Status: complete working necessary-condition argument.**

The unrestricted intercept is polynomial in the auxiliary coefficient
parameter \(n\). In the actual chart, this also removes any further
coefficient-field extension beyond \(K(n)\). Neither conclusion assumes
that the intercept is linear in rho, that \(K=\mathbb C(t)\), or that
the normalized generic parameter is integral.

This note records the coefficient reduction only. The existence of a
global invariant coordinate is not inferred from these normal forms.

## 1. Actual hypotheses and the retained quadratic coefficient relation

Retain the actual frame and notation of
[the cusp chart159](cusp-generic-chart-first-reductions-pass159-working.md)
and the branch \(r=k_\rho=0\), \(s=n_\rho\ne0\) of
[the zero-r reduction160](cusp-zero-r-generic-graph-pass160-working.md).
Thus \(B=\mathbb C[X,Y,Z,W]=A[u]\), \(E=\partial_u\), the exact
E-time degrees are \((1,1,2,2)\), and the full weighted initial
kernel is the cusp prime \((\mathsf X\mathsf Z-\mathsf Y^3)\).
Write \(a_E=EX\ne0\), to distinguish this original speed from the
quadratic coefficient \(a\) below.

Put \(t=\tau\), \(L=\operatorname{Frac}\ker_A N\), and
\(K=\ker_L\partial_\rho\). The retained coefficient fields satisfy
\(L/\mathbb C(t,\rho)\) finite separable and \(K/\mathbb C(t)\)
finite. The two original coefficient partials commute. Their common
constant field is \(\mathbb C\). The actual projection and the
zero-r calculation give
\[
\begin{gathered}
\operatorname{Frac}A=\mathbb C(y,z,w)=L(y),\qquad L[y]=L[v],\\
Y=y+tX,\qquad
Z=z+(3t^2y+k)X+t^3X^2,\qquad
z=3ty^2+k_t y+n,\\
W=R(y)+P(y)X+\rho X^2,\qquad k\in K,\quad P,R\in L[U],\\
P(U)=\frac{\ell-U^3-k_{tt}U^2/2-n_tU}{s},\qquad
R_U=P_t+P_UP_\rho,\qquad R_t+P_UR_\rho\in L^* .
\end{gathered}
\tag{1}
\]
The subscripts \(t,\rho\) in (1) are the original coefficient
partials, and formal \(U\) is held fixed.

The proved highest-coefficient restriction
\(\partial_\rho^2(1/s^2)=0\) has the exact interpretation in
[the square-root boundary171, Section 2](cusp-zero-r-square-root-actual-boundary-pass171-working.md):
\[
\rho=a n^2+b n+c,\qquad
q:=1/s=2an+b\ne0,\qquad a,b,c\in K.
\tag{2}
\]
Initially \(a\) need not be a complex constant and may be zero.
Also \(L/K(n)\) is finite separable, not initially assumed trivial.
The element \(n\) is transcendental over \(K\): the derivation
\(D_n=q\partial_\rho\) kills \(K\) and takes \(n\) to one.

## 2. Commuting coefficient derivatives at fixed n

Extend the derivation of \(K\) induced by the old \(t\)-partial to
\(K(n)\) by fixing \(n\), and then uniquely to the finite separable
extension \(L\). Call it \(\nabla\), and write primes for this
derivative. The derivation \(D_n\) extends the ordinary derivative
in \(n\) on \(K(n)\), and has kernel \(K\). The two extensions
commute: their commutator vanishes on \(K(n)\), hence on its
separable algebraic extension. In particular,
\[
\partial_\rho=q^{-1}D_n,\qquad
\partial_t^{\rm old}=\nabla-\frac{\rho'}qD_n,\qquad
\rho'=a'n^2+b'n+c'.
\tag{3}
\]
These are identities on the exact field \(L\), not a replacement
of that field by a rational subfield.

Set
\[
\begin{gathered}
h=k''/2\in K,\qquad F(U)=U^3+hU^2,\qquad m=q\ell\in L,\\
P=\rho' U-qF+m,\qquad
\delta=\nabla-F_U D_n,\qquad
R_U=\delta P,\qquad \delta R\in L^* .
\end{gathered}
\tag{4}
\]
Indeed the old \(n_t\) is \(-\rho'/q\), which gives the formula
for \(P\). Also \(P_U=\rho'-qF_U\), so that
\(\partial_t^{\rm old}+P_U\partial_\rho=\delta\).

Direct integration in the formal polynomial variable \(U\), with
an unrestricted constant \(R_0\in L\), now gives
\[
R=aF^2-q'UF-\frac{qh'}3U^3
       +\frac{\rho''}2U^2+m'U-(D_nm)F+R_0.
\tag{5}
\]
For verification, differentiating (5) in \(U\) yields
\(\rho''U-q'F-qh'U^2+m'-F_U(q'U-2aF+D_nm)\),
which is exactly \(\delta P\). No coefficient-field
antiderivative is being adjoined in (5).

## 3. The top four coefficients

Before making \(a\) constant, the top two coefficients of
\(\delta R\) are
\[
[U^6]\delta R=7a',\qquad
[U^5]\delta R=12a'h+4ah'+3D_n^2m.
\tag{6}
\]
They vanish by (4). Therefore \(a\in\mathbb C\) and
\(D_n^2m=-4ah'/3\). Two primitive subtractions inside \(L\)
give
\[
m=-\frac{2a}{3}h'n^2+M_1n+M_0,\qquad M_1,M_0\in K.
\tag{7}
\]
This argument does not require \(a\ne0\).

Write \(R=\sum_{j=0}^6 R_jU^j\). Substitution in (5) gives the
following exact coefficient list, still with arbitrary \(R_0\):
\[
\begin{aligned}
R_6&=a,& R_5&=2ah,& R_4&=ah^2-b',\\
R_3&=\frac{2a}{3}h'n-b'h-\frac b3h'-M_1,\\
R_2&=\left(\frac{b''}2+\frac{4a}{3}hh'\right)n
                  +\frac{c''}2-hM_1,\\
R_1&=-\frac{2a}{3}h''n^2+M_1'n+M_0'.
\end{aligned}
\tag{8}
\]
For every \(j\), including the lower terms, coefficient
extraction can be checked by the single recurrence
\([U^j]\delta R=R_j'-3D_nR_{j-2}-2hD_nR_{j-1}\),
where missing coefficients are zero.

In particular the \(U^4\) coefficient gives
\(b''=-4ahh'/3\). Its first integral is
\(b'=\beta-2ah^2/3\), with \(\beta\in\mathbb C\).
After that substitution the \(U^3\) coefficient is
\(14ah''n/3-4b'h'/3-bh''/3-4M_1'\).
Since \(n\) is transcendental over \(K\), this proves
\[
b''=-\frac{4a}{3}hh',\qquad
ah''=0,\qquad
M_1'=-\frac{b'h'}3-\frac{bh''}{12}.
\tag{9}
\]

## 4. The unrestricted intercept and the lower compatibility

Using \(ah''=0\), the \(U^2\) coefficient reads
\[
3D_nR_0=
\left(\frac{b'''}2+\frac{4a}{3}(h'^2+hh'')\right)n
       +\frac{c'''}2-h'M_1-3hM_1'.
\]
Differentiate the first identity of (9) and use \(ah''=0\).
Subtracting an explicit polynomial primitive in \(n\) gives
\[
\begin{gathered}
R_0=\gamma n^2+D n+R_{00},\qquad
\gamma=\frac a9(h')^2,\qquad R_{00}\in K,\\
D=\frac{c'''}6-\frac{h'M_1}3-hM_1'\in K .
\end{gathered}
\tag{10}
\]
In particular \(\gamma'=2ah'h''/9=0\). The letter \(D\)
here denotes a coefficient, not a derivation.

The \(U^1\) and \(U^0\) coefficients now give
\[
\begin{gathered}
M_1''=\frac{4a}{9}h(h')^2,\qquad M_0''=2hD,\\
\delta R=D'n+R_{00}'\ne0.
\end{gathered}
\tag{11}
\]
The right side need not yet be a complex constant, or a unit in
an unlocalized polynomial ring. Only its nonzero value in \(L\)
is used here, exactly as in (1).

One lower compatibility must not be discarded. Differentiating
the last identity of (9) and substituting its first identity
shows
\[
M_1''=\frac{4a}{9}h(h')^2
        -\frac5{12}b'h''-\frac1{12}bh''',\qquad
bh'''+5b'h''=0.
\tag{12}
\]
For \(a\ne0\), this follows already from \(h''=0\).
For \(a=0\), however, \(q=b\ne0\), \(b''=0\), and the
remaining condition is genuinely required. Equivalently in that
case, \((b^5h'')'=0\). The coefficient calculation alone does
not justify deleting this condition.

## 5. Actual field return removes the residual extension

Equations (7), (8), and (10) prove that every coefficient of
\(P\) and \(R\) belongs to \(K[n]\). Also \(k\in K\) and
\(\rho=an^2+bn+c\in K[n]\). Consequently the actual projected
coordinates in (1) satisfy
\[
y,z,w\in K(n)[y],\qquad
L(y)=\mathbb C(y,z,w)\subseteq K(n)(y)\subseteq L(y).
\tag{13}
\]
Both inclusions are equalities. Intersect with \(L\): since
\(y\) is transcendental over \(L\),
\(L\cap K(n)(y)=K(n)\). For example, if an element of \(L\)
equals a rational function in \(y\) with coefficients in
\(K(n)\), compare the coefficients of its cleared numerator and
denominator as polynomials in \(y\). Thus
\[
L=K(n).
\tag{14}
\]
This use of actual field return is essential. The earlier
coefficient integration was carried out on the original finite
extension and did not assume (14).

## 6. A chart derivation identity and exact scope

On the field \(L(y,X)\), keep \(X\) fixed and define
\(\mathcal T=\nabla-X\partial_y-F_yD_n\). The chart in (1)
and (4) gives, without any additional realization assumption,
\[
\mathcal T X=\mathcal T Y=\mathcal T Z=0,\qquad
\mathcal T W=\delta R=D'n+R_{00}'.
\tag{15}
\]
Indeed the \(X\) coefficient of \(\mathcal T W\) is
\(\delta P-R_U\), and its \(X^2\) coefficient is
\(\delta\rho-P_U\); both vanish. Direct differentiation of
\(Z\) uses \(F_y=3y^2+k''y\). This is a rational-field
identity. By itself it does not prove that \(\mathcal T\) is
a polynomial derivation of the original ring, locally nilpotent,
or normalized to the original coordinate partial.

The result is a list of necessary coefficient identities and
the exact actual coefficient field (14). It does not prove
\(K=\mathbb C(t)\), force \(D'=0\), or construct a global
invariant coordinate. Those are additional questions requiring
an additional argument. A formal solution of the displayed
identities need not be an actual polynomial frame. No arbitrary
entry theorem, full cancellation theorem, historical novelty,
or formal proof certification is claimed.

The companion finite checker is
[cusp_zero_r_coefficient_normal_form_controls_pass173.py](cusp_zero_r_coefficient_normal_form_controls_pass173.py).
It is independent source arithmetic, not a proof of the field
or universal necessary-condition arguments. Earlier proofs and
their canonical executions are unchanged.
