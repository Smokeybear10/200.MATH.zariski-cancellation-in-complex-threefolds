# Exact coefficient field of the remaining paraboloid quartic

For the genuine quadratic-over-quadratic quartic remaining in280, the
complete scalar determinant removes both parameter derivatives from
its completed-square discriminant. Strong actual field return then
gives the exact equality \(L=F(n)\), with a polynomial presentation of
all three intercepts over \(F\). The remaining leading coefficients
have two explicitly integrated algebraic forms.

These are necessary restrictions on the supplied actual branch. They
do not make the completed-square parameter an ambient coordinate and
do not yet recognize or exclude this quartic branch.

## 1. Retained actual chart and quartic coefficients

Retain all actual hypotheses of the fully read
[280](principal-paraboloid-nonlinear-constant-slope-pass280-working.md)
and its exact chart
[271](principal-paraboloid-nonconstant-intercept-plane-reduction-pass271-working.md).
In particular
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad
K=\operatorname{Frac}A,\quad\deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(X^2Z-Y^2)\text{ is the full initial kernel},\quad
\operatorname{shift}(\partial_Z)=4,\quad k_s=0,\quad n_s\ne0,\\
K=\mathbb C(y,z,w)=L(v),\quad Nv=1,\quad L[y,\sigma]=L[v],\\
F=\ker_L\partial_n,\quad [F:\mathbb C(t)]<\infty,\quad
[L:F(n)]<\infty,\quad\ker(\partial_t|_F)=\mathbb C.
\end{gathered}
\tag{1}
\]
The coefficient derivatives commute and initially fix \(v\); primes
denote the extended derivative on \(F\). The symbol \(B\) below is
a coefficient, not the four-variable ring \(\mathcal B\).

The genuine quartic restriction of280 gives
\[
H=hn+c,\quad h\in\mathbb C^*,\quad T=pn+q,\quad
\omega=v_1n+v_0,\qquad c,k,p,q,v_1,v_0\in F.
\tag{2}
\]
We assume precisely its remaining genuine quartic component, with
\(\deg_v\sigma=2\), \(\deg_v y=4\), not any of its lower-degree
components. The actual formulas are
\[
\begin{aligned}
Y&=y+\sigma X+tX^2,\\
Z&=z+(2t\sigma+k)X+t^2X^2,\\
W&=w+\theta X+HX^2,\qquad
z=2ty+\sigma^2+k'\sigma+n,\\
\theta&=T+c'\sigma-h\{(2\sigma+k')y+k''\sigma^2/2\},\\
w&=\omega-p\{(2\sigma+k')y+k''\sigma^2/2\}
 -h\{y^2+k''\sigma y+k'''\sigma^3/6\}\\
&\hspace{9mm}+c'y+c''\sigma^2/2+(p'n+q')\sigma,\\
\det\frac{\partial(Y,Z,W)}{\partial(t,n,v)}&=-a^4h\in L^*,
\qquad a=EX.
\end{aligned}
\tag{3}
\]
All coefficient differentiations are performed before evaluating the
formal projected variables.

Write the normalized plane primitive from280 as
\[
Q(U,P)=BU^2+C(P)U+D(P),\quad
C(P)=a_2P^2+a_1P+a_0,\quad D(P)=\sum_{j=1}^4D_jP^j,
\tag{4}
\]
where the complete coefficients are
\[
\begin{aligned}
B&=hk''/2+p,& a_2&=hk'''/2+2p'=B'+p',\\
a_1&=pk''-c''+k'p'+2v_1,&
a_0&=-np'+k'v_1-q',\\
D_4&=hk''''/24,&
D_3&=(pk'''-c'''+3k''p')/6,\\
D_2&=-np''/2+k''v_1/2-q''/2,&
D_1&=-v_1'n-v_0'.
\end{aligned}
\tag{5}
\]
Here \(B,a_2\in F^*\). In this quartic component the unit cofactor
gives \(Q-q_0=\eta G\), and the exact quadratic whole-line
classification gives
\[
\Delta(P):=C(P)^2-4B\{D(P)-q_0\}=dP+f,
\quad d\in L^*,\ f\in L,\qquad
x:=2By+C(\sigma),\quad x^2=d\sigma+f.
\tag{6}
\]
The polynomial \(x\) is affine in the original line parameter \(v\),
with \(x_v\in L^*\). This is a conclusion about \(L[v]\), not about
ambient polynomial coordinates. The full discriminant coefficients
already give
\[
a_2^2=4BD_4=Bh k''''/6\ne0,\qquad
a_1=2BD_3/a_2,\qquad Bp''=a_2p'.
\tag{7}
\]
The remaining coefficients of (6), including \(q_0\), are not presumed
to be rational in \(n\).

## 2. A complete scalar calculation removes d_n and f_n

Put \(v_*:=p'\), and temporarily hold the displayed formal \(P\)
fixed. The defining equations in (6) give
\[
\begin{aligned}
y&=(x-C(P))/(2B),\qquad x^2=dP+f,\\
x_n&=(d_nP+f_n)/(2x),\quad x_t=(d_tP+f_t)/(2x),
\quad x_P=d/(2x),\\
y_n&=(x_n+v_*)/(2B),\quad
y_t=(x_t-C_t-2B'y)/(2B),\quad y_P=(x_P-C_P)/(2B).
\end{aligned}
\tag{8}
\]
These are intermediate rational identities; multiplying out below
removes their denominators in \(x\).
Since \(x\) is affine in \(v\), the calibrated scalar in its own
parameter is
\[
J_x:=\det\frac{\partial(y,z,w)}{\partial(t,n,x)}
             =-a^4h/x_v\in L^*.
\tag{9}
\]
The change from \(v\) has its exact determinant factor \(x_v\).
Its moving coefficient derivatives do not change this factor.

The raw gradients in271 give
\(Q_U=(2P+k')\mathscr W_n-\mathscr W_P\) and
\(Q_P=(2U+k''P)\mathscr W_n-\mathscr W_t\).
Subtracting \(\mathscr W_n\) times the middle differential row in (3)
from the last one therefore proves
\[
\begin{aligned}
Q_U(y,P)&=x,\qquad Q_P(y,P)=(2xC_P-d)/(4B),\\
J_x&=\frac{2x}{d}\left[
x\{-y_t+(2y+k''P)y_n\}
 +\frac{2xC_P-d}{4B}\{y_P-(2P+k')y_n\}\right].
\end{aligned}
\tag{10}
\]
The factor \(2x/d\) changes \((t,n,P)\) to \((t,n,x)\).
In deriving the displayed value of \(Q_P\), differentiate the formal
discriminant with respect to \(P\), not a moving root:
\(2CC_P-4BD_P=d\). Thus
\(C_Py+D_P=(2xC_P-d)/(4B)\); the factor four is essential.

Substitute (8) into (10) and reduce by \(x^2=dP+f\). The exact form is
\[
4B^2dJ_x=\mathcal E(P)+x\mathcal O(P),\qquad
\deg\mathcal E,\deg\mathcal O\le3.
\tag{11}
\]
The two highest odd coefficients are
\[
\begin{aligned}
[P^3]\mathcal O&=-6a_2d_n,\\
[P^2]\mathcal O&=2Bk''d_n-2a_2k'd_n-6a_2f_n-4a_1d_n.
\end{aligned}
\tag{12}
\]
Since \(P=(x^2-f)/d\), the odd summand in (11) is odd in \(x\),
while (9) is independent of \(x\). Substitution is injective on
\(L[P]\). The nonzero coefficient \(a_2\) makes (12) imply
\[
\boxed{d_n=f_n=0,\qquad d\in F^*,\quad f\in F.}
\tag{13}
\]
This uses the exact kernel \(F\) inside \(L\), not a prior equality
\(L=F(n)\).

For transparency the remaining odd coefficients, after (13), are
\[
\begin{aligned}
[P]\mathcal O&=-2Bd'+(4B'+4a_2+6v_*)d,\\
[1]\mathcal O&=-2Bf'+4B'f+2a_1d+dk'v_*+4fv_*.
\end{aligned}
\tag{14}
\]
Thus
\[
Bd'=(4B'+5v_*)d,\qquad
Bf'=2(B'+v_*)f+(a_1+k'v_*/2)d.
\tag{15}
\]

The even part is also needed to retain the calibration. The formula
\(d=2a_1a_0+4B\omega_t\) and (13) first give
\(v_1'=a_1v_* /(2B)\). The literal discriminant identities then give
\[
\begin{aligned}
B'&=a_2-v_*,& v_*'&=a_2v_*/B,\\
a_2'&=(3a_2^2+2a_2v_*)/B,\\
a_1'&=-k''v_*+k'a_2v_*/B+3a_2a_1/B+a_1v_*/B,\\
(a_0)_t&=(a_1^2+2a_2a_0)/(2B)+k'a_1v_* /(2B).
\end{aligned}
\tag{16}
\]
For the fourth line differentiate \(a_1\) in (5), eliminate \(c'''\)
using \(a_1=2BD_3/a_2\), and use \(v_1'\) above. For the last,
\((a_0)_t=2D_2+k'v_1'\) and
\(a_1^2+2a_2a_0=4BD_2\).
Direct expansion of (10) shows that (16) cancels every positive
coefficient of \(\mathcal E\), and its constant coefficient is
\(-d^2/2\). In detail, before this substitution the coefficients are
\[
\begin{aligned}
\mathcal E_3&=d A,\qquad
\mathcal E_2=f A+d B_*,\qquad
\mathcal E_1=f B_*+d C_*,\qquad
\mathcal E_0=f C_*-d^2/2,\\
A&=4Ba_2'-4B'a_2-8a_2^2-12a_2v_*,\\
B_*&=4Ba_1'+4Bk''v_*-4B'a_1-8a_2a_1
                         -4a_2k'v_*-8a_1v_*,\\
C_*&=4B(a_0)_t-4B'a_0-2a_1^2-2a_1k'v_*-4a_0v_*.
\end{aligned}
\tag{17}
\]
Each of \(A,B_*,C_*\) vanishes by (16). Therefore the complete scalar is
\[
\boxed{J_x=-d/(8B^2)\in F^*.}
\tag{18}
\]
No positive-degree scalar coefficient or independent calibration factor
has been dropped.

## 3. Exact polynomial presentation and coefficient-field equality

Equations (5),(6),(13) now express
\[
\sigma=(x^2-f)/d\in F[x],\qquad
y=\frac{x-a_2\sigma^2-a_1\sigma-k'v_1+q'+v_*n}{2B}
                                                      \in F[n,x].
\tag{19}
\]
The raw formulas (3) then put \(z,w\) in \(F[n,x]\) as well.
Strong actual field return supplies both inclusions
\[
K=\mathbb C(y,z,w)\ \subset\ F(n,x)\ \subset\ K.
\tag{20}
\]
The second uses only that \(F,n,x\) are elements of \(K\).
Taking \(N\)-constants yields
\[
\boxed{K=F(n,x),\qquad L=F(n).}
\tag{21}
\]
Indeed \(N\) kills \(F(n)\), and \(Nx=x_v\ne0\). On the rational
function field \(F(n)(x)\), the kernel of
\((Nx)\partial_x\) is exactly \(F(n)\), whether or not the multiplier
was initially known to belong to that smaller field.

If \(v_*\ne0\), (19) also solves \(n\) polynomially over \(F[y,x]\),
so \(K=F(y,x)\). If \(v_*=0\), then \(y,\sigma\in F[x]\), and
\(z=n+2ty+\sigma^2+k'\sigma\) instead gives \(K=F(z,x)\).
None of these field equalities makes \(x\) an actual polynomial in
the original four coordinates.

## 4. Both exact leading-coefficient integrations

The last identity of (7) permits the two cases established in280:
\(p'=0\), or \(B=(\tau-t)p'\) with \(\tau\in\mathbb C\).

### 4.1 The case p'=0

Here \(p\in\mathbb C\), \(a_2=B'\ne0\), and
\(B''=hk''''/2\). The first equation of (7) is exactly
\(BB''=3(B')^2\). It is equivalent to \((B^{-2})''=0\).
Consequently there are constants \(A_1\in\mathbb C^*\),
\(D_1^*\in\mathbb C\), and \(\zeta=B^{-1}\in F^*\) such that
\[
\zeta^2=A_1t+D_1^*,\qquad
k=\frac{8\zeta^3}{3hA_1^2}-\frac{p}{h}t^2+k_1t+k_0,
\quad k_1,k_0\in\mathbb C.
\tag{22}
\]
The slope \(A_1\) cannot vanish, because then \(B'=0\).
To check the integration, \(\zeta'=A_1/(2\zeta)\) and
\(k''=2(B-p)/h\); differentiating the expression twice gives exactly
this value. Every integration constant is complex by (1).
The first equation of (15) also integrates to
\(d=d_0B^4\), with \(d_0\in\mathbb C^*\).

### 4.2 The case p' nonzero and its actual translation

The normalization \(B=-tp'\) is available by an actual weighted
polynomial change, not a field-dependent shift. For the complex
\(\tau\) from280 use
\[
X_*=X,\quad Y_*=Y-\tau X^2,\quad
Z_*=Z-2\tau Y+\tau^2X^2,\quad W_*=W.
\tag{23}
\]
Its inverse is \(Y=Y_*+\tau X_*^2\),
\(Z=Z_*+2\tau Y_*+\tau^2X_*^2\), with \(X,W\) unchanged.
Both compositions are the identity. Moreover
\(X^2Z_*-Y_*^2=X^2Z-Y^2\) identically. The new leader ratio is
\(t_*=t-\tau\), which is still transcendental; hence both affected
time degrees remain two. The full weighted initial kernel is preserved
by this weighted automorphism. The literal \(\partial_{Z_*}\) is
\(\partial_Z\), so the selected shift, intrinsic derivation, and exact
field are retained. The intercepts satisfy
\(y_*=y,\sigma_*=\sigma,z_*=z-2\tau y,n_*=n\); the coefficient
derivative and calibration are unchanged. Relabel \(t_*\) as \(t\).

Now write \(v_*=p'\ne0\). The equation \(B=-tv_*\) integrates exactly to
\(hk'+2tp=\kappa\in\mathbb C\), and \(a_2=-tv_*'\ne0\).
The quartic identity (7) becomes
\[
tv_*v_*''-3t(v_*')^2+3v_*v_*'=0,
\quad (v_*^{-2})''+\frac3t(v_*^{-2})'=0.
\tag{24}
\]
Multiplying by \(t^3\) makes the latter a total derivative. Two
integrations with exact constants give
\[
v_*^{-2}=A_2+D_2^*/t^2,\qquad
A_2\in\mathbb C,\quad D_2^*\in\mathbb C^*,\qquad
\zeta:=t/v_*,\quad \zeta^2=A_2t^2+D_2^*.
\tag{25}
\]
Here \(D_2^*\ne0\) is equivalent to \(v_*'\ne0\); this is forced by
\(a_2\ne0\). In contrast, \(A_2=0\) is not excluded.
If \(A_2\ne0\), then \(\zeta'=A_2t/\zeta\), and
\[
p=\zeta/A_2+p_0,\qquad
k=-\frac{2\zeta^3}{3hA_2^2}-\frac{p_0}{h}t^2
                    +\frac{\kappa}{h}t+k_0,
\quad p_0,k_0\in\mathbb C.
\tag{26}
\]
If \(A_2=0\), then \(\zeta\in\mathbb C^*\), since \(\mathbb C\)
is algebraically closed. The valid degeneration is
\[
p=t^2/(2\zeta)+p_0,\qquad
k=-t^4/(4h\zeta)-p_0t^2/h+\kappa t/h+k_0.
\tag{27}
\]
It has \(a_2=-t/\zeta\ne0\), so it cannot be discarded on degree
grounds. Finally (15) integrates in this case to
\(d=d_0v_*^4/t\), with \(d_0\in\mathbb C^*\).

## 5. Exact remaining boundary and verification

The leading functions \(k,p\) in (22),(26),(27) lie in the indicated
quadratic curve subfield of \(F\). The full coefficient field \(F\)
has not thereby been proved equal to that subfield: the remaining
functions \(c,q,v_1,v_0,f\) and their literal lower equations remain.
Equations (19)--(21) do remove the finite extension over \(F(n)\),
and all actual coordinates belong to \(F[X,n,x]\). They do not show
that one of the original coordinates is polynomial over an actual
three-coordinate subring with coefficients in \(F\), nor that \(x\)
descends to an ambient coordinate. Thus no recognition or contradiction
is asserted for these genuine quartics.

The complete saved280 and271 sources were read before this derivation.
An independent saved-source review found a factor-of-two error in the
first version of (10): it used \((xC_P-d)/(2B)\) for \(Q_P\).
The correct value is \((2xC_P-d)/(4B)\), as derived explicitly above.
Independent recalculations agreed on the correction. Keeping the
denominator \(4B^2d\) in (11), the highest odd coefficients (12),
the field conclusions (13),(19)--(21), and the leading-function
integrations (22),(24)--(27) are unchanged. The lower odd equations
(14),(15), the constant even coefficient, and (18) have been corrected.
In particular the former formulas \(J_x=-d/(4B^2)\),
\(d\propto B^5\), and \(d\propto v_*^5/t^2\) are invalid and
must not be used. Their corrected values are (18),
\(d\propto B^4\), and \(d\propto v_*^4/t\), respectively.

Fresh corrected unsaved algebra expanded (10), retaining arbitrary
coefficient jets, reconstructed both odd coefficients (12) and all of
(14), and checked the complete even ledger (17), not just its vanishing
after restrictions. It verified every cancellation in (16)--(18).
The exact-field
integrations, strong field return, and actual inverse in (23) are
written arguments rather than conclusions of those finite controls.
No retained proof was changed and no saved checker was executed,
imported, or compiled. No unrestricted or historical novelty claim
is made.
