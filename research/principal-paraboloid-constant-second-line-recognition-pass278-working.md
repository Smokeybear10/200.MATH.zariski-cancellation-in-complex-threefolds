# Recognition of the constant-second line in the paraboloid branch

Status: in the actual nonconstant-intercept branch271, suppose the
projected coefficient \(\sigma\) belongs to the intrinsic constant
field \(L\). Then the original kernel is a polynomial three-ring.
More precisely, after one explicitly invertible complex affine
change of \(X,Y,Z\), this note constructs an actual invariant
coordinate that is monic linear in \(W\).

The proof uses the affine-in-\(n\) restriction277, the full scalar
Jacobian, and a nice auxiliary derivation on an actual polynomial
three-ring over \(\mathbb C(X)\). Its fixed linear form is used only
to restrict coefficients. No coefficient-field coordinate is
declared to be an ambient coordinate.

## 1. Actual hypotheses, exact fields, and the line

Retain the actual hypotheses and exact construction of the fully read
[271](principal-paraboloid-nonconstant-intercept-plane-reduction-pass271-working.md):
\[
B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad A=\ker E,
\quad \deg_E(X,Y,Z,W)=(1,2,2,2),
\quad \operatorname{in}\ker=(X^2Z-Y^2).
\tag{1}
\]
The last expression denotes the full weighted initial kernel, not
a relation between the original coordinates. Write \(a=EX\ne0\).
The intrinsic nonzero LND \(N\) selected by the literal \(Z\)-partial
has shift four. Its exact generic line and coefficient fields satisfy
\[
\begin{gathered}
Na=Nt=0,\quad L=\operatorname{Frac}\ker_A N,\quad
A\otimes_{\ker N}L=L[v],\quad Nv=1,\quad
K=\operatorname{Frac}A=L(v),\\
F=\ker_L\partial_n,\quad [F:\mathbb C(t)]<\infty,\quad
[L:F(n)]<\infty,\quad \ker_F\partial_t=\mathbb C.
\end{gathered}
\tag{2}
\]
The two commuting coefficient partials fix \(v\); primes on elements
of \(F\) mean their \(t\)-derivative. The parameter \(n\) is
transcendental over \(F\). These are the fields obtained by replacing
the old coefficient parameter \(s\) by the nonconstant intercept
\(n\), under \(k_s=0,n_s\ne0\), not arbitrary algebraic enlargements.

The completely read restriction
[277](principal-paraboloid-affine-parameter-restriction-pass277-working.md)
gives
\[
H=s=h(t)n+j(t),\qquad h,j,k\in F,\qquad h\ne0.
\tag{3}
\]
It does not by itself say that \(h,j,k\) are complex polynomials.
The actual fixed-\(X\) map and returns are
\[
\begin{aligned}
Y&=y+\sigma X+tX^2,\\
Z&=z+(2t\sigma+k)X+t^2X^2,
&z&=2ty+\sigma^2+k'\sigma+n,\\
W&=w+\theta X+HX^2,\\
K&=\mathbb C(y,z,w),&
L[y,\sigma]&=L[v],\\
\mathcal J(X)&=\det\frac{\partial(Y,Z,W)}{\partial(t,n,v)}
=-a^4h\in L^*.
\end{aligned}
\tag{4}
\]
All projected coefficients belong to \(L[v]\).

Assume for this note that
\[
\sigma\in L.
\tag{5}
\]
Then (4) gives \(L[y]=L[v]\), so \(y\) is affine in \(v\) and
\(y_v\in L^*\). The selected plane equation is \(P-\sigma\).
The unit-cofactor statement of271 therefore gives
\[
Q_U(U,\sigma)=0,\qquad Q_P(U,\sigma)=\eta\in L^*.
\tag{6}
\]
Here \(U,P\) are independent formal variables. Coefficient
derivatives are taken before the moving substitution \(P=\sigma\).

For later explicit computations put
\[
\begin{aligned}
\gamma&=2P+k',& B_1&=2U+k''P,\\
\mathscr A&=\gamma U+k''P^2/2,&
\mathscr C&=U^2+k''PU+k'''P^3/6,\\
g&=T+H_tP-h\mathscr A,\\
\mathscr W&=\omega-(h'P+T_n)\mathscr A-h\mathscr C
 +(h'n+j')U+(h''n+j'')P^2/2+T_tP,\\
Q_U&=\gamma\mathscr W_n-\mathscr W_P,&
Q_P&=B_1\mathscr W_n-\mathscr W_t.
\end{aligned}
\tag{7}
\]
The retained potentials assert \(\theta=g(y,\sigma)\) and
\(w=\mathscr W(y,\sigma)\), with \(T,\omega\in L\).
All derivatives in (7) retain their full coefficient dependence.

## 2. The scalar Jacobian forces h to be complex

The indicated formal coefficients of (7) are
\[
\begin{aligned}
[U]Q_U&=-\gamma^2T_{nn}+(6P+2k')h'+2T_n+hk'',\\
[U^2]Q_P&=-2\gamma T_{nn}+3h'.
\end{aligned}
\tag{8}
\]
Both vanish after \(P=\sigma\), by (6). In this section abbreviate
\(\gamma(\sigma)=2\sigma+k'\) to \(\gamma_0\).

If \(\gamma_0=0\), the second equality immediately gives \(h'=0\).
Suppose \(\gamma_0\ne0\), and assume for contradiction \(h'\ne0\).
Solving (8) gives the exact identities in \(L\)
\[
T_{nn}=\frac{3h'}{2\gamma_0},\qquad
T_n=-\frac{hk''}{2}+\frac{h'k'}2-\frac{3h'\gamma_0}{4}.
\tag{9}
\]
Differentiating the second identity in \(n\), using that \(h,k\in F\),
and comparing with the first gives
\[
\gamma_0(\gamma_0)_n=-2,\qquad
1+\gamma_0\sigma_n=0.
\tag{10}
\]
This is a derivative of the evaluated identity, so the moving
\(\sigma_n\) is included.

The actual constant determinant identity from271, specialized only
using \(\sigma_v=0\) and (6), is
\[
-a^4h=\eta(1+\gamma_0\sigma_n)y_v.
\tag{11}
\]
Equation (10) contradicts its nonzero left side. Thus \(h'=0\) in
every case, and the constants assertion in (2) gives
\[
h\in\mathbb C^*.
\tag{12}
\]
If \(\gamma_0\ne0\), (8) now gives \(T_{nn}=0\) and
\(T_n=-hk''/2\). If \(\gamma_0=0\), the first equality in (8)
directly gives the same \(T_n\), hence again \(T_{nn}=0\).
Exact integration using \(F=\ker_L\partial_n\) yields
\[
T=-\frac{hk''}{2}n+q,\qquad q\in F.
\tag{13}
\]
There is no assertion here that \(L=F(n)\).

## 3. An actual nice derivation restricts k and j

Extend \(N\) from \(A\) to \(B=A[u]\) by \(Nu=0\), and define
\[
\mathcal P=aN-(NX)E,\qquad \tau=\mathcal P Y=aNy.
\tag{14}
\]
This is an actual derivation of \(B\), not merely a derivation of
the coefficient field. Since \(Na=0\), \(X=x+au\) has \(NX=Nx\in A\).
Thus \(\mathcal P X=0\), \([E,\mathcal P]=0\), and
\(\mathcal P|_A=aN\).

It is locally nilpotent: \(B_a=A_a[X]\), and on this ring
\(\mathcal P\) fixes \(X\) and restricts to the LND \(aN\) of \(A_a\).
The localization preserves local nilpotence because \(Na=0\).
Every element of \(B\) is therefore killed by a power of
\(\mathcal P\). Moreover \(Ny=y_v\in L^*\), so
\(\tau\ne0\), \(\tau\in B\), and \(\mathcal P\tau=0\).

The complex constant (12) permits the actual triangular coordinate
\[
\widehat W=W+hY^2,\qquad W=\widehat W-hY^2.
\tag{15}
\]
Use it only for the present auxiliary derivation, without changing the
underlying chart notation \(W\). Differentiating the literal map (4)
at fixed \(X,L\), using (7),(13), gives
\[
\begin{aligned}
\mathcal P Y&=\tau,&
\mathcal P Z&=2t\tau,\\
\mathcal P\widehat W
 &=\tau(2htX^2-hk'X+\Lambda),&
\Lambda&=\frac{hk'k''}{2}+j'\in F.
\end{aligned}
\tag{16}
\]
All coefficients on the right are killed by \(\mathcal P\).
Consequently the nonzero LND induced on the actual ring
\(\mathbb C(X)[Y,Z,\widehat W]\) kills the second iterate of each
of these three generators.

The precise external input is the fixed-linear-form part of
[Dasgupta--Gupta, Theorem 3.1(i)](https://arxiv.org/html/1701.03635v1),
which restates Wang's result: over a characteristic-zero field,
a nonzero LND whose second iterate kills all three polynomial
generators has a nonzero linear form in its kernel.
Irreducibility is not required for that part of the theorem.
We use the displayed restatement, not a claim to have checked the
original proof of Wang.

Applied over \(\mathbb C(X)\), it gives \(A_0,A_1,A_2\in\mathbb C(X)\),
not all zero, with
\[
A_0+2tA_1+A_2(2htX^2-hk'X+\Lambda)=0.
\tag{17}
\]
The element \(X\) is transcendental over \(K\), and \(t\) is
transcendental over \(\mathbb C\). Hence \(1,t\) are linearly
independent over \(\mathbb C(X)\), so \(A_2\ne0\).
It follows that
\[
-hk'X+\Lambda\in \mathbb C(X)+t\mathbb C(X).
\tag{18}
\]
Clear denominators in \(\mathbb C[X]\), and pass to the
\(\mathbb C\)-vector-space quotient \(F/(\mathbb C+\mathbb Ct)\).
Multiplication by a nonzero scalar polynomial in \(X\) is injective
on its vector-valued polynomial module. The degree-one polynomial
represented by the left side of (18) must therefore be zero.
Since \(h\in\mathbb C^*\), this proves
\[
k',\Lambda\in\mathbb C+\mathbb Ct.
\tag{19}
\]
Integrating in \(F\), whose derivative constants are exactly
\(\mathbb C\), shows that \(k\) is a complex quadratic.
Its contribution \(hk'k''/2\) to \(\Lambda\) is complex affine,
so \(j'\) is complex affine and \(j\) is also complex quadratic.

The fixed linear form in (17) has not been descended to a
coordinate over \(\mathbb C[X]\). Only the coefficient restrictions
(19) have been extracted from it.

## 4. A literal affine normalization and the remaining potentials

Write \(k=\kappa t^2/2+\alpha t+\beta\), with complex coefficients,
and put \(d=\kappa/4\). Use the actual map from the completely read
[272](principal-paraboloid-high-derivative-line-normalization-pass272-working.md):
\[
X_*=X-d,\quad Y_*=Y+\alpha X_*/2,\quad
Z_*=Z-\beta X_*,\quad W_*=W.
\tag{20}
\]
Its polynomial inverse is
\(X=X_*+d,\ Y=Y_*-\alpha X_*/2,\ Z=Z_*+\beta X_*,\ W=W_*\).
Both compositions are the identity.

For arbitrary projected \(y,\sigma\), literal substitution gives
\[
\begin{aligned}
\sigma_*&=\sigma+2dt+\alpha/2,&
y_*&=y+d\sigma+td^2,&k_*&=0,\\
n_*&=n-3d^2t^2-\alpha dt+\beta d-\alpha^2/4.
\end{aligned}
\tag{21}
\]
In particular \(\sigma_*\in L\) and \(y_*\) is still affine in \(v\).
The map preserves the literal selected \(Z\)-partial, \(N,L\), the
leaders and full initial kernel, and all actual chart returns.
Its change in \(n\) is a complex polynomial in \(t\), so
\(\partial_{n_*}=\partial_n\) and its constant field remains \(F\).
The old parameter \(H\) takes the form \(hn_*+j_*(t)\), with the
same \(h\in\mathbb C^*\) and another complex quadratic \(j_*\).
The coefficient \(t\)-partial is rebuilt at fixed \(n_*,v\);
no old moving-coordinate derivative is reused without this change.

Rename the rebuilt chart, so \(k=0\). Reapplying the line coefficient
calculation (8),(13) gives \(T=q(t)\in F\). Write
\[
j=j_2t^2/2+j_1t+j_0,\qquad j_2,j_1,j_0\in\mathbb C.
\tag{22}
\]
The complete formal polynomial and gradients now reduce to
\[
\begin{aligned}
\mathscr W&=-hU^2+j'U+j_2P^2/2+q'P+\omega,\\
Q_U&=2P\omega_n-j_2P-q',\\
Q_P&=(2\omega_n-j_2)U-q''P-\omega_t.
\end{aligned}
\tag{23}
\]
The coefficient of \(U\) in (6) forces
\(\omega_n=j_2/2\). The other identity in (6) then forces \(q'=0\).
Thus
\[
q\in\mathbb C,\qquad
\omega=j_2n/2+\omega_0,\quad \omega_0\in F,\qquad
-\omega_0'=\eta\ne0.
\tag{24}
\]
The last equality follows from \(Q_P(U,\sigma)=\eta\).
In particular the coefficient integrations introduce no unaccounted
\(n\)-dependent mode.

## 5. An explicit original-ring invariant coordinate

The rebuilt actual map now has
\[
\begin{aligned}
z&=2ty+\sigma^2+n,&
H&=hn+j,\\
\theta&=q+j'\sigma-2h\sigma y,&
w&=-hy^2+\frac{j_2}{2}z+j_1y+\omega_0 .
\end{aligned}
\tag{25}
\]
Here all coefficients used in the following ambient correction are
complex. In the actual coordinate ring set
\[
\boxed{
I=W-h(X^2Z-Y^2)-\frac{j_2}{2}Z-j_1Y-qX-j_0X^2.
}
\tag{26}
\]
The map \((X,Y,Z,W)\mapsto(X,Y,Z,I)\) has the polynomial inverse
\[
W=I+h(X^2Z-Y^2)+\frac{j_2}{2}Z+j_1Y+qX+j_0X^2.
\tag{27}
\]
Substituting either expression into the other gives the identity,
so \(I\) is an actual coordinate, not merely a rational invariant.

For completeness, direct substitution of (4),(25) uses
\[
X^2Z-Y^2=-y^2-2y\sigma X+nX^2
\]
and yields
\[
I=\omega_0(t)\in K=\operatorname{Frac}A,\qquad EI=0.
\tag{28}
\]
The equality is in the actual fraction field; since (26) is in \(B\),
it proves \(I\in A\). No assertion that arbitrary elements of \(F\)
are regular on the original ring is needed.

The sliced kernel \(A\) is affine and regular, because
\(B=A[u]\) is a polynomial four-ring. Apply
[Bhatwadekar--Gupta--Lokhande, Theorem 3.5](https://arxiv.org/html/1501.01438v1)
to the nonzero LND \(E\) on
\(B=\mathbb C[I]^{[3]}\): its invariant actual coordinate is \(I\),
and its kernel is regular. This gives
\[
\boxed{A=\mathbb C[I]^{[2]}\cong\mathbb C^{[3]}.}
\tag{29}
\]

## 6. Scope and independent finite evidence

This recognizes precisely the \(\sigma\in L\) line inside the
actual branch271 after the restriction277. The other projected
lines, nonlinear plane components, and the nonzero-coupling
three-generator branch264 are not settled by this note.
The proof neither removes every finite coefficient-field extension
nor infers an ambient coordinate from a coefficient-field change.

Fresh unsaved symbolic computations independently reconstructed
both coefficients (8), the full nice row (16), the rebuilt gradients
(23), and the actual identity (28), retaining all displayed
coefficients. They are finite algebra checks, not a substitute for
the exact-field, local-nilpotence, published-theorem, or actual
coordinate arguments above. No saved checker was executed,
imported, or compiled. No earlier source was edited.

