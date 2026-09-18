# The selected conic of a quartic paraboloid primitive

Status: the selected degree-two plane component is recognized when the
literal primitive of the actual branch271 has degree four. Its
\(p'=0\) subcase is impossible; its \(p'\ne0\) subcase admits an
actual invariant coordinate after restriction to a polynomial
three-ring.

The completed-square expression in this note is a nonzero element of
the coefficient field. It is not the affine generic-line parameter
of the genuine quartic component281. We rebuild its scalar
determinant before using actual field return.

## 1. Actual entry and the constant discriminant

Retain every actual hypothesis of the fully read
[271](principal-paraboloid-nonconstant-intercept-plane-reduction-pass271-working.md)
and its nonlinear reduction
[280](principal-paraboloid-nonlinear-constant-slope-pass280-working.md).
Thus
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad
K=\operatorname{Frac}A,\quad\deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(X^2Z-Y^2)\text{ is the full initial kernel},\quad
\operatorname{shift}(\partial_Z)=4,\quad k_s=0,\quad n_s\ne0,\\
K=\mathbb C(y,z,w)=L(v),\quad Nv=1,\quad L[y,\sigma]=L[v],\\
F=\ker_L\partial_n,\quad [F:\mathbb C(t)]<\infty,\quad
[L:F(n)]<\infty,\quad\ker_F\partial_t=\mathbb C .
\end{gathered}
\tag{1}
\]
The coefficient partials commute and initially fix \(v\).
Primes on \(F\) mean the exact extended \(t\)-derivative.
The nonlinear reduction gives
\[
H=hn+c,\quad h\in\mathbb C^*,\quad T=pn+q,
\qquad c,k,p,q\in F .
\tag{2}
\]

Assume precisely that the selected full irreducible plane relation
has degree two, while the normalized primitive \(Q\) has degree four.
Its pure top is a multiple of \(P^2\); whole-line generation and
irreducibility give
\[
G=U-P_2(P),\quad \deg P_2=2,\qquad
L[\sigma]=L[v],\quad \sigma_v\in L^*.
\tag{3}
\]
The evaluated-unit cofactor in271 has the exact form
\[
Q-q_0=\eta G+BG^2,\qquad \eta\in L^*,\quad B\in L^*.
\tag{4}
\]
Indeed the square cofactor is constant by degree, and comparison of
the U-squared coefficient identifies it with \(B=hk''/2+p\in F^*\).

For independent formal \(U,P\), write the complete coefficient table
from280 as
\[
\begin{aligned}
Q&=BU^2+C(P)U+D(P),&
C(P)&=a_2P^2+a_1P+a_0,&D(P)&=\sum_{i=1}^4D_iP^i,\\
B&=hk''/2+p,&a_2&=hk'''/2+2p',\\
a_1&=pk''-c''+k'p'+2\omega_n,&
a_0&=-np'+k'\omega_n-q',\\
D_4&=hk''''/24,&
D_3&=(pk'''-c'''+3k''p')/6,\\
D_2&=-np''/2+k''\omega_n/2-q''/2,&D_1&=-\omega_t .
\end{aligned}
\tag{5}
\]
All coefficient derivatives are taken before any projected-variable
substitution. Completing the square in (4) gives
\[
\begin{gathered}
C(P)^2-4B(D(P)-q_0)=\chi^2,\qquad
\chi:=2By+C(\sigma)=\eta\in L^*,\\
a_2^2=4BD_4\ne0,\qquad a_1=2BD_3/a_2\in F.
\end{gathered}
\tag{6}
\]
In particular \(a_2\ne0\), and (5) shows \(\omega_n\in F\).
Exact integration gives
\[
\omega=v_1n+v_0,\qquad v_1,v_0\in F.
\tag{7}
\]
This does not yet imply \(L=F(n)\).

Put \(r=p'\), so \(a_2=B'+r\). The vanishing P-squared and
P-linear coefficients of the discriminant give, respectively,
\[
Br'=a_2r,\qquad 2a_1a_0+4B\omega_t=0.
\tag{8}
\]
The n-coefficient of the second identity is
\(-2a_1r+4Bv_1'=0\); hence
\[
v_1'=a_1r/(2B).
\tag{9}
\]
These identities do not use an affine discriminant parameter or a
nonzero discriminant slope.

## 2. The complete scalar makes chi a curve-field element

The actual map remains
\[
\begin{aligned}
Y&=y+\sigma X+tX^2,\\
Z&=z+(2t\sigma+k)X+t^2X^2,\qquad
z=2ty+\sigma^2+k'\sigma+n,\\
W&=w+\theta X+HX^2,\\
\theta&=pn+q+c'\sigma-h\{(2\sigma+k')y+k''\sigma^2/2\},\\
w&=v_1n+v_0-p\{(2\sigma+k')y+k''\sigma^2/2\}\\
 &\quad-h\{y^2+k''\sigma y+k'''\sigma^3/6\}
       +c'y+c''\sigma^2/2+(rn+q')\sigma .
\end{aligned}
\tag{10}
\]
The calibrated determinant is \(-a^4h\), where \(a=EX\ne0\).
Use \(\sigma\) as the line parameter, holding it fixed in the new
coefficient derivatives. The exact determinant is
\[
J_\sigma=\det\frac{\partial(y,z,w)}{\partial(t,n,\sigma)}
                       =-a^4h/\sigma_v\in L^*.
\tag{11}
\]
Moving coefficients of the affine change from \(v\) do not alter
its determinant factor \(\sigma_v\).

To reconstruct this scalar, temporarily put \(P=\sigma\) but treat
it as the independent line parameter. The identities (6) give
\[
\begin{aligned}
y&=(\chi-C(P))/(2B),&
y_n&=(\chi_n+r)/(2B),\\
y_t&=(\chi_t-C_t-2B'y)/(2B),&
y_P&=-C_P/(2B),\\
Q_U(y,P)&=\chi,& Q_P(y,P)&=\chi C_P/(2B).
\end{aligned}
\tag{12}
\]
The last formula follows from
\(2CC_P-4BD_P=0\). The full gradient determinant identity of271 is
therefore
\[
J_\sigma=
\chi\{-y_t+(2y+k''P)y_n\}
+\frac{\chi C_P}{2B}\{y_P-(2P+k')y_n\}.
\tag{13}
\]
No derivative of a moving root has been substituted for a formal
gradient.

The coefficient identities required for simplifying (13) follow
directly from (5),(6),(8),(9):
\[
\begin{aligned}
B'&=a_2-r,&r'&=a_2r/B,\\
a_2'&=(3a_2^2+2a_2r)/B,\\
a_1'&=-k''r+k'a_2r/B+3a_2a_1/B+a_1r/B,\\
(a_0)_t&=(a_1^2+2a_2a_0)/(2B)+k'a_1r/(2B).
\end{aligned}
\tag{14}
\]
For the third identity use
\(a_2^2=Bh k''''/6\) and \(hk''''=2(B''-r')\).
For the fourth differentiate the definition of \(a_1\), then use
\(a_1=2BD_3/a_2\) and (9). The last follows from
\((a_0)_t=2D_2+k'v_1'\) and the vanishing quadratic
discriminant coefficient.

Substitution in the complete expression (13) gives
\[
[P^2]\left(\frac{4B^2J_\sigma}{\chi}\right)=-6a_2\chi_n.
\]
Since \(\sigma\) is affine in \(v\), the scalar (11) is independent
of \(P\). Thus \(a_2\ne0\) forces \(\chi_n=0\), or \(\chi\in F^*\).
After imposing this, every positive P-coefficient in (13) cancels;
the exact constant is
\[
\boxed{
\chi\in F^*,\qquad
J_\sigma=\frac{\chi(a_2\chi-B\chi')}{2B^2}\ne0.}
\tag{15}
\]
This is the constant-discriminant scalar, not the nonzero-slope
formula of281.

Now (12) puts \(y\) in \(F[n,\sigma]\), and the literal formulas
(10) put \(z,w\) there as well. Strong actual field return supplies
\[
K=\mathbb C(y,z,w)\subset F(n,\sigma)\subset K.
\]
Taking \(N\)-constants, with \(N\sigma=\sigma_v\ne0\), gives
\[
\boxed{K=F(n,\sigma),\qquad L=F(n).}
\tag{16}
\]
The second inclusion uses that all displayed field elements are
already in \(K\); no rationality of \(F\) is assumed.

## 3. The subcase p'=0 is impossible

Suppose \(p'=0\). Then \(p,v_1\in\mathbb C\) by (9),
\(a_2=B'\ne0\), and the leading relation in (6) gives
\[
B^{-2}=\alpha t+\kappa_0,\qquad
\alpha\in\mathbb C^*,\quad\kappa_0\in\mathbb C,\qquad
B'=-\alpha B^3/2 .
\tag{17}
\]
The remaining integrations are the zero-linear-discriminant
specialization of the coefficient identities in (14),(8):
\[
\begin{aligned}
a_1&=\beta B^3,&
a_0&=\gamma B-\beta^2B^3/(2\alpha),\\
c'-pk'-2tv_1&=2\beta B/\alpha+\ell_0,\\
v_0&=\beta\gamma B/\alpha-\beta^3B^3/(6\alpha^2)+\omega_0,
\end{aligned}
\tag{18}
\]
with \(\beta,\gamma,\ell_0,\omega_0\in\mathbb C\).
For clarity \(a_1'=3B'a_1/B\) and
\((a_0/B)'=\beta^2B^4/2\) give the first line.
The definition of \(a_1\) gives the next.
Finally (8) gives \(v_0'=-a_1a_0/(2B)\), whose integral is
the last displayed expression. These computations include all
their exact integration constants.

Define elements of the actual intercept field by
\[
S_0=B(\sigma-\beta/\alpha),\quad
Y_0=y+\gamma/2,\quad
W_0=w-v_1z+hy^2-\ell_0y-\omega_0 .
\tag{19}
\]
They are not asserted to be ambient coordinates.
The completion (6) and the literal \(w\) in (10), using (18),
give
\[
Y_0=\frac{\chi}{2B}+\frac{\alpha S_0^2}{4},
\qquad W_0=-2S_0Y_0+\frac{\alpha S_0^3}{6}.
\tag{20}
\]
To check the second identity, the coefficient of \(y\) in the
corrected \(w\) is \(-2S_0\). Its remaining terms before the shift
\(\sigma=S_0/B+\beta/\alpha\) are
\[
\frac{\alpha B^3}{6}\sigma^3-\frac{\beta B^3}{2}\sigma^2
+\left(-\gamma B+\frac{\beta^2B^3}{2\alpha}\right)\sigma
+v_0-\omega_0 .
\]
Substitution cancels the \(\beta\gamma B\) and \(\beta^3B^3\)
terms and proves (20).

In particular \(S_0\in K\) satisfies
\[
\alpha S_0^3-12Y_0S_0-6W_0=0.
\tag{21}
\]
The formal polynomial \(\alpha T^3-12UT-6V\) is irreducible in
\(\mathbb C[U,V,T]\), being primitive linear in \(V\) over
\(\mathbb C[U,T]\). As a primitive polynomial in \(T\), it remains
irreducible of degree three over \(\mathbb C(U,V)\), and then over
\(\mathbb C(U,Z_0,V)\) for an independent \(Z_0\).

The complex triangular intercept change (19) has inverse
\[
y=Y_0-\gamma/2,\qquad
w=W_0+v_1z-h(Y_0-\gamma/2)^2+\ell_0(Y_0-\gamma/2)+\omega_0.
\]
Thus strong return gives \(K=\mathbb C(Y_0,z,W_0)\).
These three generators are algebraically independent, since
\(\operatorname{trdeg}_{\mathbb C}K=3\).
Equation (21) would therefore be a root in \(K\) of an irreducible
cubic over \(K\), a contradiction. The entire \(p'=0\) subcase
is excluded.

## 4. The nonzero p-derivative has a complex slope directly

Suppose \(r=p'\ne0\). Equations (8),(14) give
\((B/r)'=-1\). Exact constants in \(F\) therefore yield
\(B=(\tau-t)r\) for a complex \(\tau\). The actual weighted map
\[
X_*=X,\quad Y_*=Y-\tau X^2,\quad
Z_*=Z-2\tau Y+\tau^2X^2,\quad W_*=W
\tag{22}
\]
has inverse
\(Y=Y_*+\tau X_*^2,\ Z=Z_*+2\tau Y_*+\tau^2X_*^2\),
with \(X,W\) unchanged. It preserves \(X^2Z-Y^2\), the literal
selected partial, intrinsic derivation and exact fields.
Its new \(t_*=t-\tau\) is still transcendental, with
\(y_*=y,\sigma_*=\sigma,n_*=n,z_*=z-2\tau y\).
After relabeling,
\[
B=-tr,\qquad hk'+2tp=\kappa\in\mathbb C.
\tag{23}
\]
The last equality follows by differentiating, using \(B=hk''/2+p\).

Define
\[
\Lambda=c'-pk'-2tv_1\in F.
\]
There is a particularly useful shortcut:
\[
\begin{aligned}
\Lambda'&=c''-rk'-pk''-2v_1-2tv_1'\\
&=-a_1-2tv_1'
=-a_1\left(1+\frac{tr}{B}\right)=0 .
\end{aligned}
\tag{24}
\]
Here the definition of \(a_1\) and the exact identity (9) are both
used. Hence \(\Lambda\in\mathbb C\). There is no need for a
curve-pencil pole bound or a distinction among radical ODE modes.

This shortcut also applies under the corrected genuine-quartic
identities281 after the same \(B=-tp'\) normalization, since its
vanishing derivative of the discriminant slope yields the same (9).
The held proof285 remains a valid independent recognition route;
no earlier source is changed by this observation.

The completed-square equation now solves
\[
n=-2ty+
 \frac{a_2\sigma^2+a_1\sigma+k'v_1-q'-\chi}{r}.
\tag{25}
\]
Together with (16), this gives \(K=F(y,\sigma)\), with \(y,\sigma\)
algebraically independent over \(F\). Substitution in the literal
potentials gives
\[
z\in F[\sigma],\qquad
w=-hy^2+\Lambda y+\Omega(\sigma),\quad \Omega\in F[\sigma].
\tag{26}
\]
The y-cancellation in \(z\) uses (25); the coefficient of
\(\sigma y\) in \(w\) is \(-2p-hk''-2tr=0\).
Every remaining coefficient belongs to the exact field \(F\).

Use the actual triangular coordinate
\[
J=W+hY^2+\kappa XY-\Lambda Y,
\qquad W=J-hY^2-\kappa XY+\Lambda Y.
\tag{27}
\]
All its coefficients are complex, and the inverse is literal.
Set \(M=F(X,\sigma)\). Then
\[
\operatorname{Frac}\mathcal B=M(Y),\qquad
Z,J\in F[X,\sigma].
\tag{28}
\]
For \(J\), the full raw-map check, holding \(F,X,\sigma\) fixed,
uses
\(n_y=-2t,\theta_y=-\kappa-2h\sigma,H_y=-2ht\).
Together with (26), these make \(J_y=0\).
The raw expression is polynomial in \(y\), so it belongs to
\(F[X,\sigma]\). No field-dependent ambient change is made.

## 5. Actual three-ring preservation and recognition

The coordinate change (27) gives the actual polynomial ring
\[
S=\mathbb C[X,Z,J],\qquad \mathcal B=S[Y].
\]
From (28), \(\operatorname{Frac}(S)\subset M\) and
\(\operatorname{Frac}(S)(Y)=M(Y)\), with \(Y\) transcendental over
\(M\). Comparing rational functions in this independent variable
therefore yields
\[
M=\operatorname{Frac}(S).
\tag{29}
\]
Since \(E/a\) is the \(X\)-partial holding \(K\) fixed, (28) and
the raw \(Y\) show that all four ratios
\[
(EX,EZ,EJ,EY)/a=(1,EZ/a,EJ/a,\sigma+2tX)
\]
belong to \(\operatorname{Frac}(S)\).

Choose a proportional primitive vector \(b\in S^4\) of gcd one.
The actual coefficient vector of \(E\) is \(g b\), initially with
\(g\in\operatorname{Frac}(S)[Y]\).
Because every entry lies in \(S[Y]\), and at every prime of the
UFD \(S\) some entry of \(b\) is not divisible by that prime,
coefficientwise valuations give \(g\in S[Y]\).
The actual slice \(u\) is polynomial in \(X,Z,J,Y\), and \(Eu=1\)
makes \(g\) a divisor of \(1\). Thus \(g\in\mathbb C^*\), proving
\[
E(S)\subset S.
\tag{30}
\]
This is the actual primitivity argument, not the assumption that
a coefficient-field scalar is an original-ring unit.

The restriction \(E_0=E|_S\) is a nonzero LND with
\(E_0X\ne0,E_0^2X=0\). Divide it by the gcd \(\Delta\) of its
three coefficients. Since \(\Delta\mid E_0\Delta\), local
nilpotence gives \(E_0\Delta=0\), by additivity of LND degree.
Thus \(D=E_0/\Delta\) is an irreducible LND with the same kernel
and \(DX\ne0,D^2X=0\).

The precise three-variable preslice theorem
[Dasgupta--Gupta, Theorem 4.8, restating Daigle](https://arxiv.org/html/1701.03635v1)
supplies an actual coordinate \(I\) of \(S\) with \(DI=0\).
It remains a coordinate after adjoining \(Y\), and \(EI=0\).
The sliced kernel \(A\) is affine and regular because
\(\mathcal B=A[u]\) is regular. Applying
[Bhatwadekar--Gupta--Lokhande, Theorem 3.5](https://arxiv.org/html/1501.01438v1)
to this actual invariant coordinate gives
\[
\boxed{A=\mathbb C[I]^{[2]}\cong\mathbb C^{[3]}.}
\tag{31}
\]

## 6. Exact scope and verification

This treats the degree-two selected plane relation when its literal
primitive has degree four. It does not conflate that component with
the genuine degree-four component281 or the degree-two primitive
components. In the \(p'=0\) subcase it proves nonrealizability.
In the \(p'\ne0\) subcase it proves recognition, not existence.

The constant-discriminant scalar, exact coefficient-field return,
complex slope identity, literal n-elimination and actual three-ring
descent are all included above. Fresh unsaved algebra independently
reconstructed (13)--(15), the slope derivative (24), and the literal
cubic identity (20),(21). The source279 was fully read for comparison,
but its different quadratic-cubic chart is not used as an imported
hypothesis. The actual content and preslice argument is reconstructed
here from the already fully read285.
No saved checker was executed, imported, or compiled, and no
earlier proof was changed. No unrestricted result or novelty
claim is asserted.

