# Recognition of the constant-slope projected lines

Working result: every selected projected line in the actual principal
branch271 is recognized if its parameter potential has the form
\(H=hn+c\) with \(h\in\mathbb C^*\). This closes the constant-slope
cubic-coefficient mode left open in288. It does not recognize the
nonconstant-slope lines or establish entry into this chart.

The proof below derives its line identities directly from271. In
particular it does not apply the nonlinear component theorem280 to a
line. It reconstructs the original-ring descent used in287, rather
than treating a coefficient-field variable as an actual coordinate.

## 1. Actual hypotheses and the two possible line directions

Retain all actual hypotheses of
[271](principal-paraboloid-nonconstant-intercept-plane-reduction-pass271-working.md):
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad A=\ker E,
\quad \deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\mathrm{initial}}=(X^2Z-Y^2)\text{ is the full initial kernel},
\quad\operatorname{shift}(\partial_Z)=4,\quad k_s=0,\quad n_s\ne0,\\
K=\operatorname{Frac}A=\mathbb C(y,z,w)=L(v),\quad Nv=1,
\quad L[y,\sigma]=L[v],\\
F=\ker_L\partial_n,\quad [F:\mathbb C(t)]<\infty,
\quad[L:F(n)]<\infty,\quad\ker(\partial_t|_F)=\mathbb C.
\end{gathered}
\tag{1}
\]
The coefficient partials commute and initially fix \(v\). Primes
on elements of \(F\) mean the exact extended t-derivative. Assume
in addition
\[
H=hn+c,\qquad h\in\mathbb C^*,\quad c,k\in F,
\qquad\deg G=1,
\tag{2}
\]
where \(G\) is the full selected plane relation of271.
The potential \(T\), and the integration term \(\omega\), initially
belong only to \(L\).

If \(\sigma\in L\), the retained actual-coordinate theorem
[278](principal-paraboloid-constant-second-line-recognition-pass278-working.md)
already recognizes \(A\). Its hypotheses include this case and
do not require the first projection to be constant. Hence assume
\(\sigma\notin L\). Whole-line generation then gives
\[
G=U-AP-C,\quad y=A\sigma+C,\quad A,C\in L,
\qquad L[\sigma]=L[v],\quad\sigma_v\in L^*.
\tag{3}
\]
The capital \(A\) in the line coefficient is a scalar in \(L\),
distinct from the kernel ring \(A=\ker E\); below it occurs only
in formulas for the line. Put \(a=EX\ne0\) for the slice speed.

The actual expansions, including every lower term, are
\[
\begin{aligned}
Y&=y+\sigma X+tX^2,\\
Z&=z+(2t\sigma+k)X+t^2X^2,
&z&=2ty+\sigma^2+k'\sigma+n,\\
W&=w+\theta X+HX^2,
&\det\frac{\partial(Y,Z,W)}{\partial(t,n,v)}&=-a^4h\in L^*.
\end{aligned}
\tag{4}
\]
For independent formal variables \(U,P\), write
\[
\begin{aligned}
\mathscr A&=(2P+k')U+k''P^2/2,
&\mathscr C&=U^2+k''PU+k'''P^3/6,\\
g&=T+c'P-h\mathscr A,
&\mathscr W&=\omega-T_n\mathscr A-h\mathscr C
                  +c'U+c''P^2/2+T_tP,\\
Q_U&=(2P+k')\mathscr W_n-\mathscr W_P,
&Q_P&=(2U+k''P)\mathscr W_n-\mathscr W_t.
\end{aligned}
\tag{5}
\]
Then \(\theta=g(y,\sigma)\), \(w=\mathscr W(y,\sigma)\), and
all derivatives in (5) are taken before evaluating the line.
The unit selected cofactor of271 states
\[
Q-q_0=\eta G+G^2R,\quad\eta\in L^*,\quad
Q_U(AP+C,P)=\eta,\quad Q_P(AP+C,P)=-A\eta.
\tag{6}
\]

## 2. The full scalar and the canonical direction

Use \(\sigma\) as the independent generic-line parameter. This
changes the calibrated determinant by the factor \(\sigma_v\),
including the moving coefficients of its affine change from \(v\).
The full wedge identity of271, with (6), gives
\[
\begin{aligned}
\delta:=\frac{J_\sigma}{\eta}
&=(4A+k'')A_n P^2\\
&\quad+\bigl((4A+k'')C_n+(2C+Ak')A_n-A_t\bigr)P\\
&\quad+(2C+Ak')C_n-C_t-A^2\in L^*.
\end{aligned}
\tag{7}
\]
Here \(P\) stands for the new independent parameter and
\(J_\sigma=-a^4h/\sigma_v\). In these derivatives \(P\) is
fixed. Formula (7) also follows directly from
\(-y_t+(2y+k''P)y_n-A\{y_P-(2P+k')y_n\}\).
It is not obtained by holding the old \(v\) fixed after changing
the parameter without a chain rule.

Set \(\ell=4A+k''\). If \(\ell=0\), then
\(A=-k''/4\in F\), and the coefficient of \(P\) in (7) forces
\(A'=0\). Thus \(k'''=0\), and
\(k=\kappa t^2/2+\alpha t+\beta\) with complex constants.
The literal normalization272, with \(d=\kappa/4\), is
\[
X_*=X-d,\quad Y_*=Y+\alpha X_*/2,
\quad Z_*=Z-\beta X_*,\quad W_*=W.
\tag{8}
\]
Its inverse adds \(d\) to \(X_*\), subtracts \(\alpha X_*/2\)
from \(Y_*\), and adds \(\beta X_*\) to \(Z_*\).
It has \(k_*=0\),
\(y_*=y+d\sigma+td^2=C+td^2\in L\), and
\[
n_*=n-3d^2t^2-\alpha dt+\beta d-\alpha^2/4.
\tag{9}
\]
As proved by literal substitution in the fully read
[272](principal-paraboloid-high-derivative-line-normalization-pass272-working.md),
the actual degrees, full initial kernel, selected partial, fields,
whole-line return and calibration are retained. Its Section4 uses
only the quadratic form of \(k\), not the high-derivative hypothesis
that led to that form in272. The canonical-line recognition theorem
[275](principal-paraboloid-canonical-line-recognition-pass275-working.md)
therefore applies. This disposes of \(\ell=0\).

Assume from now on \(\ell\ne0\). The positive coefficients in
(7) imply
\[
A\in F,\qquad C_n=A'/\ell.
\tag{10}
\]

## 3. The literal primitive becomes quadratic

The two highest line-gradient coefficients from (5) are
\[
[P^3]Q_U(AP+C,P)=-\ell T_{nn},
\qquad
[P^3]Q_P(AP+C,P)\bigm|_{T_{nn}=0}=hk''''/6.
\tag{11}
\]
They vanish by (6). Hence
\[
T=pn+q,\quad p,q\in F,
\qquad k''''=0,\quad k\in\mathbb C[t]_{\le3}.
\tag{12}
\]
The integrations use the exact constants of the two partials in
(1), not an assumption that \(F=\mathbb C(t)\).

Termwise integration of (5), with \(Q(0,0)=0\), now yields
\[
\begin{aligned}
Q&=BU^2+(a_2P^2+a_1P+a_0)U+D_3P^3+D_2P^2+D_1P,\\
B&=hk''/2+p,&a_2&=hk'''/2+2p',\\
a_1&=pk''-c''+k'p'+2\omega_n,
&a_0&=-np'+k'\omega_n-q',\\
D_3&=(pk'''-c'''+3k''p')/6,
&D_2&=-np''/2+k''\omega_n/2-q''/2,
&D_1&=-\omega_t.
\end{aligned}
\tag{13}
\]
The \(P^2\)-coefficient of \(Q_U(AP+C,P)\) is \(a_2\), so
\[
a_2=0,\qquad r:=p'=-hk'''/4\in\mathbb C,
\qquad B'=-r.
\tag{14}
\]
No nonlinear selected-component assumption enters this identity.

Since \(\deg Q\le3\), (6) makes \(R\) affine if it is nonzero.
Write \(R=\rho U+\lambda P+\mu\). The absent \(U^3\) term in
(13) forces \(\rho=0\), and the absent \(U^2P\) term forces
\(\lambda=0\). Comparison of \(U^2\) gives \(\mu=B\).
This also covers \(R=0\), when \(B=0\). Consequently
\[
\boxed{Q-q_0=\eta G+BG^2,\quad\deg Q\le2,
\quad D_3=0,\quad c'''=pk'''+3k''r.}
\tag{15}
\]
In particular the coefficient of \(UP\) is
\[
a_1=-2BA.
\tag{16}
\]

## 4. The zero r branch has an actual degree-lowering correction

If \(r=0\), then (14),(15) imply \(k'''=c'''=0\).
Both \(k\) and \(c\) are complex quadratics, and \(p\) is complex.
Apply the actual map (8), using the coefficients of \(k\), whether
or not the projected direction is canonical. The same literal
substitution gives \(k_*=0\) and (9), and the original-ring gates
in272 are preserved. Since \(H=hn+c\) with complex \(h\), the
rebuilt \(c\) is still a complex quadratic in \(t\).

Relabel this actual chart and write
\(c=c_2t^2/2+c_1t+c_0\), with \(c_i\in\mathbb C\). Define
\[
W_*=W-h(X^2Z-Y^2)-c_2Z/2-c_1Y-c_0X^2.
\tag{17}
\]
It fixes \(X,Y,Z\); adding the displayed correction is its
polynomial inverse. In the rebuilt \(k=0\) chart,
\[
X^2Z-Y^2=-y^2-2y\sigma X+nX^2.
\]
Thus every summand in (17) has time degree at most two, and
its \(X^2\)-coefficient is exactly
\(hn+c-hn-c_2t^2/2-c_1t-c_0=0\).
Therefore \(\deg_EW_*\le1\).

If its degree is zero, \(W_*\) is an actual invariant coordinate,
and Bhatwadekar--Gupta--Lokhande Theorem3.5 recognizes the regular
sliced kernel. If its degree is one, the actual frame
\((X,W_*,Y,Z)\) has exact time degrees1122. The retained
[recognition synthesis257](full-exact1122-recognition-synthesis-pass257-working.md)
recognizes its kernel, without imposing the old initial ideal on
the rebuilt frame. The proof of this case requires no assertion
that the remaining linear coefficient is nonzero.

## 5. The nonzero r branch removes the coefficient extension

Suppose \(r\in\mathbb C^*\). Then \(B'=-r\) ensures
\(B\ne0\). Equations (10),(16) give \(a_1\in F\), so (13)
forces \(\omega_n\in F\). Exact integration yields
\[
\omega=v_1n+v_0,\quad v_1,v_0\in F,
\qquad a_0=-rn+k'v_1-q'.
\tag{18}
\]
Completing the square in (15) gives the constant discriminant
\[
(a_1P+a_0)^2-4B(D_2P^2+D_1P-q_0)=\eta^2.
\tag{19}
\]
Its linear coefficient vanishes:
\(2a_1a_0+4B\omega_t=0\). The coefficient of \(n\) implies
\[
v_1'=a_1r/(2B)=-Ar.
\tag{20}
\]
On the other hand differentiating \(a_1\) in (13) and using
(15) yields
\(a_1'=-rk''+2v_1'=-rk''+a_1r/B\).
Differentiating (16) and comparing therefore gives
\[
2BA'=r(4A+k'')=r\ell,
\qquad C_n=A'/\ell=r/(2B).
\tag{21}
\]
Define the completed-square value
\[
\chi=2By+a_1\sigma+a_0=2BC+a_0=\eta\in L^*.
\tag{22}
\]
It is a coefficient-field element, not a new line parameter.
Equation (21) gives \(\chi_n=2BC_n-r=0\), so
\[
\boxed{\chi\in F^*,\qquad
y=\frac{\chi-a_1\sigma+rn-k'v_1+q'}{2B}.}
\tag{23}
\]
All coefficients of the full raw potentials in (5) are now
polynomial in \(n\) over \(F\). Hence \(y,z,w\in F[n,\sigma]\).
The actual return in (1), and the fact that \(F,n,\sigma\subset K\),
give both inclusions
\[
K=\mathbb C(y,z,w)\subset F(n,\sigma)\subset K.
\]
Taking \(N\)-constants, with \(N\sigma=\sigma_v\ne0\) and
\(N\) zero on \(F(n)\), proves
\[
\boxed{K=F(n,\sigma),\qquad L=F(n).}
\tag{24}
\]
No rationality of \(F\) or original-ring polynomiality of \(n\)
is inferred.

## 6. A complex triangular correction preserves a polynomial three-ring

Since \(B'=-r\), there is \(\tau\in\mathbb C\) with
\(B=r(\tau-t)\). Make the actual weighted change
\[
X_*=X,\quad Y_*=Y-\tau X^2,\quad
Z_*=Z-2\tau Y+\tau^2X^2,\quad W_*=W.
\tag{25}
\]
The inverse is \(Y=Y_*+\tau X_*^2\),
\(Z=Z_*+2\tau Y_*+\tau^2X_*^2\), with \(X,W\) fixed.
It preserves the full initial relation, actual degree profile and
literal selected partial. The coefficient changes are
\(t_*=t-\tau\), \(y_*=y,\sigma_*=\sigma,n_*=n\),
\(z_*=z-2\tau y\). Thus the exact fields, derivatives,
calibration and strong return survive, as does the scalar slope
\(h\). Relabel so that
\[
B=-tr,\qquad
\kappa:=hk'+2tp\in\mathbb C.
\tag{26}
\]
The last assertion follows from
\((hk'+2tp)'=2B+2tr=0\).
There is a second complex scalar:
\[
\begin{aligned}
\Lambda&:=c'-pk'-2tv_1,\\
\Lambda'&=c''-rk'-pk''-2v_1-2tv_1'
          =-a_1-2tv_1'
          =-a_1(1+tr/B)=0.
\end{aligned}
\tag{27}
\]
Therefore \(\Lambda\in\mathbb C\). This step is what licenses
the complex-coordinate correction below.

Equation (23) now solves
\[
n=-2ty+\frac{a_1\sigma+k'v_1-q'-\chi}{r}.
\tag{28}
\]
In view of (24), this gives \(K=F(y,\sigma)\), with
\(y,\sigma\) algebraically independent over \(F\).
Substitution in the complete raw potentials yields
\[
z\in F[\sigma],\qquad
w=-hy^2+\Lambda y+\Omega(\sigma),\quad\Omega\in F[\sigma].
\tag{29}
\]
Indeed \(z\)'s y-coefficient is \(2t-2t=0\).
In \(w\), the coefficient of \(\sigma y\) is
\(-2p-hk''-2tr=-2B-2tr=0\), and its remaining linear
y-coefficient is exactly \(\Lambda\).

Use the actual monic triangular coordinate
\[
J=W+hY^2+\kappa XY-\Lambda Y,
\qquad W=J-hY^2-\kappa XY+\Lambda Y.
\tag{30}
\]
Set \(M=F(X,\sigma)\). Then the full expansion, not just the
intercepts, satisfies
\[
Z,J\in F[X,\sigma],\qquad
\operatorname{Frac}\mathcal B=M(Y).
\tag{31}
\]
For the full \(J\), differentiate while fixing \(F,X,\sigma\).
Equations (5),(28) give
\(n_y=-2t\), \(\theta_y=-\kappa-2h\sigma\),
\(H_y=-2ht\). With (29) and
\(Y=y+\sigma X+tX^2\), every coefficient in \(J_y\)
vanishes. Its raw expression is polynomial in \(y\), which proves
the first assertion of (31) without an ambient field-valued shear.

Let \(S=\mathbb C[X,Z,J]\). The actual inverse in (30) gives
\(\mathcal B=S[Y]\). Equation (31) gives
\(\operatorname{Frac}S\subset M\) and
\(\operatorname{Frac}S(Y)=M(Y)\), with \(Y\) transcendental over
\(M\). The constant coefficients of rational functions in this
independent variable show that
\[
\operatorname{Frac}S=M.
\tag{32}
\]
Moreover \(E/a\) is the \(X\)-partial holding \(K\) fixed, so
all four ratios
\[
(EX,EZ,EJ,EY)/a=(1,EZ/a,EJ/a,\sigma+2tX)
\]
lie in \(\operatorname{Frac}S\).

Here is the necessary original-ring divisibility argument. Choose
a proportional vector \(b\in S^4\) with gcd one. The actual
coefficient vector of \(E\) is \(g b\) with
\(g\in\operatorname{Frac}S[Y]\). At every irreducible of the
UFD \(S\), at least one \(b_i\) is a local unit. Since every
\(gb_i\) belongs to \(S[Y]\), coefficientwise valuations show
\(g\in S[Y]\). The polynomial identity \(Eu=1\) then makes
\(g\) divide \(1\), so \(g\in\mathbb C^*\). Consequently
\[
E(S)\subset S.
\tag{33}
\]
This argument uses the actual global slice; it does not assume
that \(a\) or any coefficient-field scalar is a polynomial unit.

## 7. Recognition and the exact remaining frontier

The restriction \(E_0=E|_S\) is a nonzero LND and
\(E_0X\ne0,E_0^2X=0\). Let \(\Delta\) be the gcd of its
three polynomial coefficients. It divides \(E_0\Delta\).
If that derivative were nonzero, additivity of LND degree would
contradict \(\deg_{E_0}(E_0\Delta)=\deg_{E_0}\Delta-1\).
Thus \(E_0\Delta=0\), and \(D=E_0/\Delta\) is an irreducible
LND on \(S\) with the same kernel and \(DX\ne0,D^2X=0\).

[Dasgupta--Gupta Theorem4.8, restating Daigle](https://arxiv.org/html/1701.03635v1)
supplies an actual invariant coordinate \(I\) of the polynomial
three-ring \(S\). It remains an invariant coordinate in
\(\mathcal B=S[Y]\). The kernel \(A\) is affine and regular
because \(\mathcal B=A[u]\) is regular. Hence
[Bhatwadekar--Gupta--Lokhande Theorem3.5](https://arxiv.org/html/1501.01438v1)
gives
\[
\boxed{A\cong\mathbb C[I]^{[2]}\cong\mathbb C^{[3]}.}
\tag{34}
\]

This proves the claimed constant-slope line endpoint, subject to
the retained actual-chart and recognition results explicitly used
for the other line branches. It closes neither the nonconstant
complex-affine slope mode of288 nor the three-projection sector
\(k_s\ne0\) of264. It establishes no arbitrary-coordinate entry
theorem and therefore does not solve unrestricted cancellation.

The raw coefficient argument is independent of280 and of288's
nonconstant-slope elimination. The exact-field, full-X transport,
primitive coefficient and published preslice steps are written
above. No historical novelty, human review or proof-assistant
certification is claimed. Separate review and finite identity
checks are recorded in the research ledger when completed.
