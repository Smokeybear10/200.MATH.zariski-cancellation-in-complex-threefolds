# A direct moving-frame entry at the conic degree drop

Working result: retain the FULL actual degree-drop sector of512 and
assume its literal fourth row has zero cubic intrinsic coefficient.
The necessary equations already imply affine nonconstant coupling.
A complex polynomial normalization then gives
\[
m=t,\qquad \theta=-P^2/t+bP+c,\qquad
y=-\theta/2+\lambda P+r.
\]
Fresh expansion of the original scalar gives the coefficient
integrations and corrected moving frame below. In particular
\[
f''''=-6h''/t.
\]
Both zero and nonzero transverse derivatives of the moving linear
slope are retained. That slope derivative is NOT forced nonzero
by the unit multiplier.

This note supplies direct literal entry only. It does not apply
the nonzero-delta theorem of496 at delta zero, transfer any later
exclusion without checking its hypotheses, exclude this entire
boundary, or claim ambient recognition.

## 1. Retained actual hypotheses and the zero-cubic-row subcase

Retain all actual assumptions, both exact ring returns, the original
slice and selected literal partial of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
the genuine third and fourth levels of
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md),
the universal unit multiplier from
[494](principal-paraboloid-unit-tangent-multiplier-pass494-working.md),
and the proved degree-drop reduction
[512](principal-paraboloid-degree-drop-univariate-coupling-reduction-pass512-working.md).
In particular,
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u_{\rm glob}],\quad
X=a_0u_{\rm glob}+x_0,\quad a_0\ne0,\quad E=\partial_{u_{\rm glob}},\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\qquad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the ENTIRE initial kernel},\\
0\ne N=[u_{\rm glob}^4]\partial_Z|_A,\quad
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,\\
Na_0=Nt=Ns=0,\quad P=\sigma,\quad NP=\rho\in L^*,\quad
O=L[P],\quad L[X,Y,Z,W]=L[X,P],\\
\operatorname{Frac}A=L(P)=\mathbb C(y,z_0,w_{\rm int}),\qquad
L[y,z_0,w_{\rm int}]=O.
\end{gathered}
\tag{1}
\]
The exact coefficient partials commute and have joint constants C.
Let \(F_0=\ker_L\partial_s\), finite over C(t), with t-derivative
constants C. No rationality of F_0 or L is assumed.

The hypotheses specific to this note, before normalization, are
\[
\begin{gathered}
m=k_s,\quad m_s=0,\quad m\notin\mathbb C,\quad p=m_t\ne0,\\
\theta=-P^2/m+bP+c,\quad y=eP^2+lP+r_{\rm old},\qquad
g_3=[P^3]w_{\rm int}=(p-2me)/m^2=0.
\end{gathered}
\tag{2}
\]
By512, \(e=p/(2m)\), \(m_{tt}=0\), and hence
\[
p\in\mathbb C^*,\quad m=pt+d,\quad d\in\mathbb C,\qquad
y=-\frac p2\theta+\lambda P+r,
\quad \lambda=l+\frac p2b,\quad r=r_{\rm old}+\frac p2c.
\tag{3}
\]
The change in the intercept name in (3) retains c; it is not a
normalization of that coefficient. This entry to the displayed y
form comes from512's zero-cubic-row equation, not327's parity.

## 2. An actual complex normalization, with its exact calibration

Put \(\tau=d/p\in\mathbb C\). Use the special case of the actual
transport in
[426](general-coupling-normalization-obstruction-pass426-working.md)
given by
\[
X^*=X,\quad Y^*=Y+\tau X^2,\quad
Z^*=Z+2\tau Y+\tau^2X^2,\quad W^*=pW.
\tag{4}
\]
This is an actual complex polynomial automorphism. Its inverse is
\[
X=X^*,\quad Y=Y^*-\tau(X^*)^2,\quad
Z=Z^*-2\tau Y^*+\tau^2(X^*)^2,\quad W=W^*/p.
\tag{5}
\]
Its leading parameters and intrinsic coefficients transform as
\[
t^*=t+\tau,\quad s^*=ps,\quad P^*=P,\quad
\theta^*=p\theta,\quad y^*=y,\quad
m^*=m/p=t^*,\quad k^*=k,\quad n^*=n,\quad\ell^*=\ell.
\tag{6}
\]
Here functions on the right are reexpressed in the new exact
coefficient basis. In particular \(k^*=t^*s^*+f^*\), with
\(f^*(t^*)=f(t^*-\tau)\).

The full initial relation has the literal identity
\[
(X^*)^2Z^*-(Y^*)^2=X^2Z-Y^2.
\tag{7}
\]
Together with the invertible weighted linear-triangular map this
preserves the ENTIRE initial kernel, not just its displayed
generator's membership. The new quadratic leaders are nonzero:
t is transcendental over C, so t+tau does not vanish, and p is
nonzero. The actual localizations and both returns are preserved.
The original global slice is retained; it is not replaced by X/a_0.

The new literal Z partial equals the old literal Z partial, so the
selected N is unchanged. Also \(a_0^*=a_0\) and \(NP^*=\rho\).
The row determinant of (4) is p, and the parameter determinant
\(\partial(t^*,s^*,P^*)/\partial(t,s,P)\) is p. Consequently the
full calibrated scalar in the new basis remains
\[
J_{t^*,s^*,P^*}=-a_0^4/\rho\in L^*.
\tag{8}
\]
No division by a polynomial in X, or deletion of a fiber, occurs.

Drop stars from now on. Thus
\[
m=t,\quad k=ts+f,\quad a=-1/t,\quad a'=1/t^2\ne0,\qquad
\theta=aP^2+bP+c,\quad y=-\theta/2+\lambda P+r.
\tag{9}
\]
The coefficient field remains exact and \(F_0=\ker\partial_s\).
All subsequent primes mean its t derivative, with original actual
X fixed.

## 3. Direct high coefficients from the literal rows

Equation512(10), or direct expansion of H at (9), gives
\[
n=\frac{s^2}{4}+\left(\frac{f'}2-h\right)s+n_0,\qquad h,n_0\in F_0.
\tag{10}
\]
These are existing coefficient functions, integrated by subtraction.
The full original rows used below are
\[
\begin{aligned}
Y&=y+PX+tX^2,\\
Z&=2ty+P^2+(s+f')P+t\theta+n+(2tP+ts+f)X+t^2X^2,\\
W&=w_{\rm int}+\theta X+sX^2,\\
tw_{\rm int}
&=\ell-(2P+s+f')y-\frac{f''}{2}P^2-P\theta-n_tP-n_s\theta.
\end{aligned}
\tag{11}
\]
The fields containing b,c,r,ell are not restricted beyond L.

Define
\[
K=h-th',\qquad A_c=K/2,\qquad
B_c=-f''/4+tf'''/12.
\tag{12}
\]
The COMPLETE cubic coefficient of the genuine H level is
\[
[P^3]H^{\rm ev}=-\frac2t(\lambda-A_ca-B_c).
\]
Its vanishing proves
\[
\lambda=A_ca+B_c
=\frac{th'-h}{2t}-\frac{f''}{4}+\frac{tf'''}{12}\in F_0.
\tag{13}
\]
Direct comparison of the full P^2 coefficients in the universal
multiplier equation of494 gives
\[
\kappa=\frac t2(a'-2a^2+2ab_s)
       =-b_s-\frac1{2t}\in L^*.
\tag{14}
\]
This is the genuine scalar/minor unit multiplier. In particular no
inference about b_s alone follows from its being nonzero.

After (10),(13), the raw complete scalar coefficient is
\[
\begin{aligned}
[XP^3]J=\frac1{6t}\bigl(&6a^2K-12ab_sK+3af''-atf'''
-12ah'\\
&-6ath''+24ar_s+tf''''\bigr).
\end{aligned}
\tag{15}
\]
It solves for r_s since a and t are nonzero field elements. Substitute
that expression, and nothing else concerning the lower intercepts,
in the complete P^4 coefficient at X=0. The result is
\[
\left.[P^4]J\right|_{(15)=0}
=\frac{(6ah''-f'''')(2a^2-2ab_s-a')}{12a}
=-\frac{\kappa}{6at}(6ah''-f'''').
\tag{16}
\]
Because the scalar (8) is independent of P and kappa is nonzero,
\[
\boxed{f''''=6ah''=-6h''/t.}
\tag{17}
\]
Neither h'' nor f'''' was divided away.
Substituting this equation back into (15) gives exact integration
\[
\begin{gathered}
D_c=-aA_c/2+B_c/2+h'/2,\qquad
r_s=A_cb_s+D_c,\\
\boxed{r=A_cb+D_cs+r_0,\qquad r_0\in F_0.}
\end{gathered}
\tag{18}
\]
Two coefficient derivative identities that will be used, with no
frozen-jet interpretation, are
\[
A_c'=-th''/2,\qquad \lambda'=A_ca'-f'''/6.
\tag{19}
\]
All c,ell and their derivatives were present in (11) during the
coefficient calculations. Their cancellation from (13),(15),(16)
does not remove them from the remaining scalar.

## 4. Complete moving rows and their inverse

At fixed original X define
\[
U=Z,\qquad V=-2Y-aU,\qquad
T=W+2(X+h')Y+\frac{f'''}6U.
\tag{20}
\]
These have the exact inverse
\[
Y=-\frac{V+aU}{2},\qquad Z=U,\qquad
W=T-2(X+h')Y-\frac{f'''}6U.
\tag{21}
\]
These are polynomial identities over \(F_0[X]\); U is actual Z,
but V and T are generally NOT ambient polynomial coordinates over C.
In particular a=-1/t is noncomplex. No coordinate theorem for an
actual two-quasi frame is being applied to (20).

The complete intrinsic rows are
\[
U=P^2+uP+U_0,\qquad V=v_1P+V_0,\qquad T=w_1P+T_0,
\tag{22}
\]
with every coefficient given by
\[
\begin{aligned}
u&=s+f'+2t(X+\lambda),\qquad u_s=1,\\
U_0&=2tr+n+(ts+f)X+t^2X^2,\\
v_1&=b+\frac{s+f'}t=\frac{\epsilon}{t},\qquad
\epsilon=s+f'+tb,\\
V_0&=c-2r-2tX^2+U_0/t,\\
w_1&=2(X+h')(X+\lambda)+\frac{f'''f'}6
       +\frac{tf'''(X+\lambda)}3
       -\frac{2r_0+f'\lambda+n_0'}t,\\
T_0&=\frac{hc+\ell-(s+f')r}{t}+cX+sX^2\\
&\hspace{6mm}+2(X+h')(-c/2+r+tX^2)+\frac{f'''}6U_0.
\end{aligned}
\tag{23}
\]
The formula for T_0 includes its full term \(2tX^3\).
It must not be omitted in any later coefficient calculation.
Equations (13),(18) give
\[
w_1\in F_0[X],\qquad (w_1)_s=0,\qquad
\deg_Xw_1=2,\quad [X^2]w_1=2.
\tag{24}
\]
Thus w_1 is not the zero polynomial, but it is not asserted to be a
unit in C[X] or F_0[X]. Its roots, moving or constant, remain intact.

## 5. The full derivative connection and both transverse cases

Let
\[
e_c=\begin{pmatrix}-a/2\\1\\a(X+h')-f'''/6\end{pmatrix},\quad
f_c=\begin{pmatrix}-1/2\\0\\X+h'\end{pmatrix},\quad
g_c=\begin{pmatrix}0\\0\\1\end{pmatrix}.
\]
Equations (20),(21) say \((Y,U,W)^{\mathsf T}=e_cU+f_cV+g_cT\).
Their exact coefficient derivatives, using (17), are
\[
e_c'=a'f_c,\qquad f_c'=h''g_c,\qquad
\det(e_c,f_c,g_c)=1/2.
\]
Consequently the ENTIRE original scalar is
\[
\boxed{
J=\frac12\det\bigl(dU,\ dV+a'U\,dt,\ dT+h''V\,dt\bigr)
  =-\frac{a_0^4}{\rho}.
}
\tag{25}
\]
The determinant is in the original basis (dt,ds,dP), at fixed X.
The uncorrected determinant of dU,dV,dT would generally be wrong.
The full corrected matrix is
\[
\begin{pmatrix}
u_tP+(U_0)_t&P+(U_0)_s&2P+u\\
a'P^2+((v_1)_t+a'u)P+(V_0)_t+a'U_0
 &(v_1)_sP+(V_0)_s&v_1\\
((w_1)_t+h''v_1)P+(T_0)_t+h''V_0
 &(T_0)_s&w_1
\end{pmatrix}.
\tag{26}
\]
In particular its exact cubic-P coefficient, before the nonzero
factor 1/2, is
\[
-a'w_1+2a'(T_0)_s
-2(v_1)_s\bigl((w_1)_t+h''v_1\bigr)=0.
\tag{27}
\]
Since \(a'=1/t^2\ne0\), coefficient-by-coefficient integration
of this identity in s gives
\[
\boxed{
T_0=\frac{w_1}{2}s+t^2(w_1)_t v_1+\frac{t^2h''}{2}v_1^2+C_0,
\qquad C_0\in F_0[X].
}
\tag{28}
\]
No division by \((v_1)_s\), h'', v_1 or w_1 occurs in this
integration. The difference defining C_0 is an existing polynomial
in X with s-constant coefficients.

The precise transverse alternatives are
\[
v_1=\epsilon/t\ne0,\qquad
(v_1)_s=b_s+1/t,\qquad
\boxed{\kappa=\frac1{2t}-(v_1)_s\ne0.}
\tag{29}
\]
Here epsilon is nonzero by512. If \((v_1)_s=0\), then
\(v_1\in F_0^*\) and \(\kappa=1/(2t)\ne0\); (27) gives
\((T_0)_s=w_1/2\). This is an allowed boundary, not a contradiction.
If \((v_1)_s\ne0\), then v_1 is independent of X by (23), and
the coefficient basis (t,v_1) is exact:
\[
[L:\mathbb C(t,v_1)]<\infty,\qquad
J_{t,v_1,P}=-\frac{a_0^4}{\rho(v_1)_s}\ne0.
\tag{30}
\]
Changing to that basis requires rebasing every coefficient derivative.
In neither case is v_1 promoted to an ambient coordinate.

There is also a separating coefficient available in BOTH alternatives:
\[
z=b+\frac{s}{2t},\qquad z_s=-\kappa\ne0.
\tag{31}
\]
This is exactly512's coefficient in the current subcase, not a claim
that \((v_1)_s\) is nonzero. The original speed rho and the appropriate
coefficient Jacobian must remain in any subsequent scalar test.

## 6. Verification and bounded scope

The complete512 and the relevant full original264/296/494 sources
were read, as were full426 and496. The source496 was used as a
comparison for the displayed algebra, not as a theorem whose
nonzero-delta hypothesis was silently dropped.
Fresh f68966 and a2cec5 rebuild the full original high coefficient
identities (13)--(18), including arbitrary lower b,c,r,ell and their
derivatives. Fresh b232ea checks every complete row (23), the exact
connection, its determinant factor and the full cubic coefficient
(27). The independent peer reconstructions fc0ab3 and5d2f23 also
check the raw high ledger, entire rows and inverses, normalization
and derivative correction. No saved checker was executed.

This note establishes direct necessary entry and both transverse
branches only. The functions C_0,c,ell,r_0,n_0 and the complete
remaining scalar equations have not been solved here. Later
nonzero-delta exclusions require a separate hypothesis and proof
audit before any proposed application. No entire degree-drop
exclusion, actual recognition, generic chart entry or unrestricted
cancellation result is claimed. No earlier source or canonical
record was edited. All saved checkers remained frozen and were
neither executed, imported, compiled nor rerun.
