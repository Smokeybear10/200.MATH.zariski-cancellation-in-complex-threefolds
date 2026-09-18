# A Legendre reduction and rational-entry boundary for one projected-line branch

Working result: in the reducible projected-line case309 with
\(\sigma_v\ne0\) and \(m_s=0\), an actual normalization gives \(k=s\).
An exact Legendre change of coefficient variables and the full
X-coefficient of the calibrated determinant then yield
\[
L=\mathcal F(\eta),\qquad
[\mathcal F:\mathbb C(r)]<\infty,\qquad r=n_s,\qquad
\eta\in L^*.
\tag{1}
\]
Here \(\mathcal F\) is an exact coefficient constant field, not an
asserted ambient polynomial ring. The full original map has a
polynomial presentation over this curve field whose normalization is
a polynomial three-ring.

This does not give the polynomial entry criterion266. For this same
curve field, W has degree two over \(\mathcal F(X,Y,Z)\). After the
actual shear \(\mathcal V=W-2XZ\), the last slot Z is rational over
\(\mathcal F(X,Y,\mathcal V)\), with an explicit nonconstant
denominator \(D_{X,Y}^2\), of exact degree two in Y. No recognition or exclusion is
claimed in this note.

## 1. Retained actual branch and normalization

Retain the full actual chart264 and the exact surface and fourth
potential of
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md).
Assume the surface level is reducible, the projected equation is a
line, and retain the whole-return and factor-unit statements302.
By the fully read
[309](principal-paraboloid-reducible-line-affine-generators-pass309-working.md),
\[
y,\sigma,\theta\in L[v]\text{ are affine},\qquad
L[\sigma,\theta]=L[v].
\tag{2}
\]
The ambient slice is denoted u, as in the retained sources. No new
line parameter below is called u.

For this note assume additionally
\(\beta:=\sigma_v\ne0\) and \(m_s=0\). We first justify the
normalization rather than assuming it. Write the three intrinsic
slopes as \(\alpha=y_v,\beta=\sigma_v,\gamma=\theta_v\).
The evaluated \(H_U\) is the unit difference of the two factors,
so belongs to \(L^*\). Its quadratic coefficient in v is
\[
-\frac{2\beta(m_t\beta+m_s\gamma)}m.
\tag{3}
\]
Thus \(m_t=0\), and the exact joint constants give \(m\in\mathbb C^*\).
The cubic coefficient of the evaluated H is then
\(k_{ttt}\beta^3/6\), so \(k_{ttt}=0\). Exact integration gives
\[
k=ms+\frac{\kappa}{2}t^2+b_0t+d_0,\qquad
\kappa,b_0,d_0\in\mathbb C.
\tag{4}
\]
Use the actual polynomial reframe
\[
W_*=mW+\frac{\kappa}{2}Z+b_0Y+d_0X^2,\qquad
W=\frac{W_*-\kappa Z/2-b_0Y-d_0X^2}{m}.
\tag{5}
\]
The full arbitrary-n transport and monic surface-level identity of302,
Section3 apply. They preserve the selected derivation, calibration,
whole return, strong intercept-field return, projected degree and
reducibility, and give \(k_*=s_*\).
The affine intercept transformation leaves \(\sigma_v\ne0\).
Drop stars only after this actual reframe. Henceforth \(k=s,m=1\).
No constraint on n or ell was inserted during the reframe.

## 2. The square discriminant and its nonzero transverse slope

In this normalized chart H has total degree at most two. Its reducible
monic level has affine factor coefficients, so its entire discriminant
is a square of an affine polynomial:
\[
\begin{aligned}
\Delta={}&(4n_s^2-2n_{tt})P^2-4n_{ts}PV-2n_{ss}V^2\\
 &+4\ell_tP+4(\ell_s+n_s^2)V+n_t^2-4n_s\ell+4h_0\\
={}&(a_1P+b_1V+d_1)^2.
\end{aligned}
\tag{6}
\]
This is the literal normalized discriminant302, with its full lower
coefficients. By308 the formal difference is not constant.
Along the projected line the affine square root evaluates to a
nonzero coefficient constant. Its slope condition is
\(a_1\beta+b_1\gamma=0\).
If \(b_1=0\), then \(\beta\ne0\) would give \(a_1=0\), contrary
to the nonconstant difference. Therefore \(b_1\ne0\).

Choose the sign of the square root to agree on the line with
\(\eta:=H_U^{\rm ev}\in L^*\). The surface equation and affine
square-root relation are then
\[
2y+n_t-2n_s\sigma=\eta,\qquad
a_1\sigma+b_1\theta+d_1=\eta.
\tag{7}
\]
No field-valued coefficient is asserted to be an ambient polynomial.

The quadratic and linear discriminant coefficients give
\[
\begin{gathered}
n_{ss}=-b_1^2/2\ne0,\qquad
n_{ts}=-a_1b_1/2,\qquad
n_{tt}=2n_s^2-a_1^2/2,\\
\ell_t=a_1d_1/2,\qquad
\ell_s+n_s^2=b_1d_1/2.
\end{gathered}
\tag{8}
\]
In particular
\(n_{tt}-n_{ts}^2/n_{ss}=2n_s^2\).

## 3. Exact Legendre change, with its derivative conventions

Put \(r=n_s\). Since \(n_{ss}\ne0\), r is nonconstant under the
old s-partial. Thus t,r are algebraically independent, L is finite
over \(\mathbb C(t,r)\), and the exact new coefficient partials are
\[
\partial_{t,\mathrm{new}}
 =\partial_{t,\mathrm{old}}
  -\frac{n_{ts}}{n_{ss}}\partial_{s,\mathrm{old}},
\qquad
\partial_r=\frac1{n_{ss}}\partial_{s,\mathrm{old}}.
\tag{9}
\]
They commute by uniqueness of extensions from \(\mathbb C(t,r)\)
to the finite separable field L. In formulas involving n, ell and
their old derivatives through (8), old subscripts retain their old
meaning. From now on plain t-derivatives hold r fixed.

Let \(\mathcal F=\ker_L\partial_{t,\mathrm{new}}\).
It is finite over \(\mathbb C(r)\). For example, differentiating the
monic minimal polynomial over \(\mathbb C(t,r)\) of an element killed
by the new t-partial shows that its coefficients belong to
\(\mathbb C(r)\); the algebraic closure of that field in the
finitely generated L is finite. The commuting r-partial preserves
\(\mathcal F\), and its constants there are exactly \(\mathbb C\).

Define the coefficient Legendre transform
\(\mathscr F=n-rs\). The chain rule gives
\[
\mathscr F_t=n_{t,\mathrm{old}},\qquad
\mathscr F_r=-s,\qquad
\mathscr F_{tt}
 =n_{tt,\mathrm{old}}-\frac{n_{ts,\mathrm{old}}^2}
                                  {n_{ss,\mathrm{old}}}
 =2r^2.
\tag{10}
\]
Consequently there are \(f,g\in\mathcal F\) such that
\[
\begin{aligned}
\mathscr F&=r^2t^2+f t+g,\\
s&=-2rt^2-f't-g',\\
n&=-r^2t^2+(f-rf')t+g-rg'.
\end{aligned}
\tag{11}
\]
Primes mean the extended r-partial, not an assumption that
\(\mathcal F=\mathbb C(r)\).

The two linear equations in (8) imply
\(\ell_{t,\mathrm{old}}
 =(n_{ts}/n_{ss})(\ell_{s,\mathrm{old}}+r^2)\).
Using (9),(11), this becomes
\(\ell_{t,\mathrm{new}}=r^2(4rt+f')\).
Thus, for some \(e\in\mathcal F\),
\[
\ell=2r^3t^2+r^2f't+e.
\tag{12}
\]

## 4. Recover the full original map before using its scalar

Set \(\xi=1/b_1\ne0\). Since \(s_r=1/n_{ss}=-2\xi^2\),
equations (8),(11) imply
\[
\xi^2=t^2+\frac{f''}{2}t+\frac{g''}{2},\qquad
\frac{a_1}{b_1}=4rt+f'.
\tag{13}
\]
Define a new intrinsic line parameter and one full-map expression by
\[
\omega=\sigma-rt,\qquad S=\omega+tX,\qquad
T=t+\xi.
\tag{14}
\]
Then \(L[\omega]=L[v]\), with \(\omega_v=\beta\ne0\).
The change from \((t,s,v)\) to \((t,r,\omega)\) is only a
coefficient-and-line chart change; S is not declared ambient.

The two relations (7), together with
\(d_1/b_1=-\ell_r+2r^2\xi^2\), give
\[
\begin{aligned}
y&=r\omega+(\eta-f)/2,\\
\theta&=\eta\xi-(4rt+f')\sigma
                   +4r^2t^2+2rf't+e'-r^2g''.
\end{aligned}
\tag{15}
\]
Introduce the curve-field coefficients
\[
d=e+rg-r^2g',\qquad c=d'=e'+g-rg'-r^2g''.
\tag{16}
\]
Substitution into the literal first and second potentials264, followed
by the full fixed-X map, gives the exact identities
\[
\begin{aligned}
Y&=(X+r)S+(\eta-f)/2,\\
Z&=S^2-f'S-g'X+c+\eta T,\\
W&=(X-r)Z-(X+r)S^2-\eta S-gX+d.
\end{aligned}
\tag{17}
\]
In particular the last identity is also
\[
W=(X-r)Z+(X+r)S^2-(2Y+f)S-gX+d.
\tag{18}
\]
These are full original-coordinate identities after (5), not
identities only at X=0.

## 5. The full X-coefficient forces a constant sheet

Let \(J_{\mathrm{new}}\) be the full determinant with respect to
\((t,r,\omega)\) at fixed X. The retained calibration becomes
\[
J_{\mathrm{new}}
 =(-a^4)\frac{s_r}{\beta}
 =\frac{2a^4\xi^2}{\beta}\in L^*,
\tag{19}
\]
still independent of X and the line parameter. Moving coefficient
derivatives in the change of \(\omega\) do not change its triangular
Jacobian factor.

Since \(d'=c\), the literal rows of (17) satisfy
\[
dW-(X-r)dZ+2S\,dY=-\eta(dS+T\,dr).
\tag{20}
\]
Use the basis \(dt,dr,dS\), whose determinant relative to
\(dt,dr,d\omega\) is one at fixed X. The resulting three rows are
\[
\begin{pmatrix}
\eta_t/2&\eta_r/2+S-f'/2&X+r\\
\eta_tT+\eta T_t&
 \eta_rT+\eta T_r+c'-f''S-g''X&2S-f'\\
0&-\eta T&-\eta
\end{pmatrix}.
\tag{21}
\]
All coefficient derivatives here are the new ones.

For a compact exact coefficient check put \(q=2T+f''/2\).
Equation (13) gives
\[
T^2-g''/2=tq,\qquad 2\xi T_t=q,\qquad \xi=T-t\ne0.
\tag{22}
\]
Expanding (21), first in S and X, and then replacing
\(S=\omega+tX\), gives
\[
[\omega]J_{\mathrm{new}}
 =\eta(\eta_t q+\eta T_t),\qquad
[X]J_{\mathrm{new}}=-\frac{\eta^2q}{2}.
\tag{23}
\]
There are no terms of total degree greater than one in X,omega.
One direct way to verify the second coefficient is to write the
determinant as \(-\eta\) times the two-by-two determinant obtained
after imposing \(dS=-Tdr\). If its S and X coefficients are A and B,
then
\[
A=-\eta_tq-\eta T_t,\quad
B=\eta_t(T^2-g''/2)+\eta T_tT,\quad
B+tA=\eta\xi T_t=\eta q/2.
\]
This proves (23) without dividing by q or discarding its zero case.

Since eta is nonzero, the full-X calibration forces
\[
T=-f''/4\in\mathcal F,\qquad
g''=f''^{\,2}/8,\qquad
\xi=T-t.
\tag{24}
\]
The constant-sheet possibility in (24) is essential. An argument
that divided by q would incorrectly exclude it.

After this specialization the entire determinant is
\[
J_{\mathrm{new}}
 =-\frac{\eta\eta_t}{2}
       \bigl(\eta T'+c'+2Tf'+2rT^2\bigr)\ne0.
\tag{25}
\]
In particular \(\eta_t\ne0\). No further differential equation or
recognition conclusion is inferred from its nonzero value alone.

## 6. Strong return gives the exact remaining coefficient field

At X=0 the three expressions (17) lie in
\(\mathcal F[\omega,\eta]\), because T now belongs to
\(\mathcal F\). The actual strong return is
\(K=\mathbb C(y,z,w)\), and both \(\mathcal F\) and
\(\omega,\eta\) already belong to K. Therefore
\[
K=\mathcal F(\omega,\eta)=L(\omega).
\tag{26}
\]
Since omega is transcendental over L, intersection with L in (26)
gives \(L=\mathcal F(\eta)\). This is an exact field equality,
not merely an algebraic inclusion or a polynomial-ring assertion.
It is also consistent with \(\eta_t\ne0\); eta is not algebraic
over \(\mathcal F\).

The passage between the two polynomial parameters at fixed X has
the field inverse
\[
S=\omega+tX,\qquad \omega=S-tX.
\tag{27}
\]
Here \(t\in\mathcal F(\eta)\) by (26), not necessarily
\(\mathcal F[\eta]\). Thus (27) is not asserted to be an
ambient polynomial change. Nevertheless
\(\operatorname{Frac}\mathcal B=\mathcal F(X,S,\eta)\), and
X,S,eta are algebraically independent over \(\mathcal F\).

## 7. Polynomial normalization is not polynomial entry

Eliminate eta from (17) by the exact polynomial inverse
\[
\eta=2Y-2(X+r)S+f,\qquad
Y=(X+r)S+(\eta-f)/2.
\tag{28}
\]
Define polynomials over the curve field
\[
\begin{aligned}
A_X&=f'+2T(X+r),\\
B_{X,Y}&=2TY+Tf-g'X+c,\\
D_{X,Y}&=(X+r)A_X-(2Y+f),\\
E_{X,Y}&=-(X+r)B_{X,Y}-gX+d.
\end{aligned}
\tag{29}
\]
Use the actual complex triangular shear
\[
\mathcal V=W-2XZ,\qquad W=\mathcal V+2XZ.
\tag{30}
\]
Equations (17),(18) become
\[
Z=S^2-A_XS+B_{X,Y},\qquad
\mathcal V=D_{X,Y}S+E_{X,Y}.
\tag{31}
\]
The coefficient \(D_{X,Y}\) has exact Y-coefficient \(-2\).
It is a nonzero nonunit of \(\mathcal F[X,Y]\), even though all
operations defining (30) itself are actual polynomial operations.

Let \(\mathcal R=\mathcal F[X,Y,Z,W]\), the subring of the
actual fraction field generated by these displayed elements.
Equations (28),(31) show
\[
\mathcal R\subset \mathcal F[X,Y,S]
                 =\mathcal F[X,S,\eta].
\tag{32}
\]
The right-hand polynomial ring is finite and birational over
\(\mathcal R\): S satisfies the monic equation (31), and
\(S=(\mathcal V-E_{X,Y})/D_{X,Y}\) lies in its fraction field.
Being integrally closed, it is the normalization of \(\mathcal R\).
No normality of \(\mathcal R\) itself is supplied by this argument.

There is a precise obstruction to using the slot W in266 with this
same curve field. Over \(\mathcal F(X,Y,Z)\), the first equation
of (31) is irreducible of degree two in S. Its discriminant
\(A_X^2-4B_{X,Y}+4Z\) has degree one in the independent variable Z
and cannot be a rational square. The nonzero linear S-coefficient
in the second equation gives
\[
[\mathcal F(X,Y,Z,W):\mathcal F(X,Y,Z)]=2.
\tag{33}
\]
In particular W is not in \(\mathcal F[X,Y,Z]\), or even in that
fraction field.

With the sheared slot, rational entry does hold, but its denominator
is genuine:
\[
Z=\frac{(\mathcal V-E_{X,Y})^2
       -A_XD_{X,Y}(\mathcal V-E_{X,Y})
       +B_{X,Y}D_{X,Y}^2}{D_{X,Y}^2}.
\tag{34}
\]
The numerator is not divisible by the irreducible polynomial
\(D_{X,Y}\): modulo D its coefficient of \(\mathcal V^2\) is one.
Thus (34) is reduced, with exact nonconstant denominator \(D^2\).
This does not satisfy266's polynomial-entry hypothesis either.
The coefficients are in the curve field; none has silently been
declared regular in the original ring.

## 8. Scope and verification boundary

The result treats only the beta-nonzero, m_s-zero subcase of the
actual reducible projected line. It gives the exact Legendre and
constant-field reduction (11),(12),(24),(26), the full original map,
and a finite birational polynomial normalization. The actual
recognition problem, other line directions, and irreducible surfaces
remain outside its conclusion. In particular (32) cannot be promoted
to equality without another original-ring argument.

The held264,296,302,308 and309 inputs were read before use.
Fresh unsaved raw algebra checked the initial affine-slope
coefficients, the full-X relation (18), the exterior row replacement,
both coefficients (23), and the complete specialized determinant
(25). These identities support the written argument; finite algebra
does not prove the exact constant fields, actual returns or normality
statements. No saved checker was executed, imported, compiled or
rerun, and no held source, checker, index or packet was changed.
