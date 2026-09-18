# A complex leading y-slope is impossible in the equal quadratic case

Working scoped exclusion in the complete actual264 chart with k=s
and n_ss nonzero. Suppose sigma and theta both have intrinsic degree
two and the leading y/sigma slope is complex. A licensed actual
constant shear reduces that slope to zero. Whole original polynomial
return, specialized at a suitable X, then forces two further
coefficients to vanish. The literal scalar and genuine fourth
potential contradict the resulting exact coefficient family.

The argument does not import404's degree-one determinant or conductor.
It excludes neither noncomplex leading slopes nor higher equal degrees.
No coefficient-field change is promoted to an original coordinate.

## 1. Complete actual hypotheses and the permitted normalization

Retain every actual hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
the complete quadric/cubic and their unit conditions of
[365](principal-paraboloid-nonlinear-intercept-unequal-degree-gate-pass365-working.md),
and the equal-degree reductions400,407,412,413. In particular,
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A_0[u],\qquad E=\partial_u,\qquad
a_0=EX\ne0,\qquad \deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the full initial kernel},\qquad
0\ne N=[u^4]\partial_Z|_{A_0},\\
L=\operatorname{Frac}\ker_{A_0}N,\qquad
[L:\mathbb C(t,s)]<\infty,\qquad Nv=1,\\
O=L[v]=L[y,\sigma,\theta]=L[y,z,w],\qquad
K=\operatorname{Frac}A_0=L(v)=\mathbb C(y,z,w),\\
k=s,\qquad
J_{t,s,v}(X)=-a_0^4\in L^*,\qquad e=n_{ss}\ne0 .
\end{gathered}
\tag{1}
\]
The coefficient partials on L commute and have joint constants C.
The original global slice, actual polynomial ring, full initial
kernel, literal selected partial, both returns and all lower
potential/scalar conditions are retained.

Assume
\[
\deg_v\sigma=\deg_v\theta=2,\qquad \deg_vy\le2,\qquad
\lambda=[v^2]y/[v^2]\sigma
           \in\mathbb C.
\tag{2}
\]
Here lambda is zero when deg(y)<2. The leading ratio
mu=lc(theta)/lc(sigma) is nonzero and, by400, does not belong to
C+C*t.

The ACTUAL map of
[384, Sections3--4](principal-paraboloid-actual-filtered-symmetry-obstruction-pass384-working.md),
with c=2lambda, is
\[
X^*=X+c/2,\qquad Y^*=Y,\qquad Z^*=Z,\qquad W^*=W+cZ.
\tag{3}
\]
Its inverse is X=X*-c/2, Y=Y*, Z=Z*, W=W*-cZ*.
The exact transports include
\[
\begin{gathered}
t^*=t,\quad s^*=s+ct^2,\quad
\sigma^*=\sigma-ct,\quad
y^*=y-c\sigma/2+c^2t/4,\\
\theta^*=\theta+2ct\sigma-c^2t^2,\quad
n^*=n-cs/2-c^2t^2/4,\quad n^*_{s^*s^*}=n_{ss}.
\end{gathered}
\tag{4}
\]
They make the new leading y-slope zero. The new leading theta
ratio is mu+2ct, which cannot vanish by the400 restriction.
Both intrinsic degrees therefore remain two.

The complete384 license, not just (4), retains the full initial
kernel, exact time profile, actual quotient returns and scalar.
Its inverse gives partial_Z*=partial_Z-c*partial_W; the actual
omitted-partial shift bound makes its degree-four leading part
exactly N. Thus L and the intrinsic degree are unchanged.
Only complex c is used. Drop stars after this actual check and
work from now on with
\[
\lambda=0,\qquad \deg_vy<2.
\tag{5}
\]

## 2. An exact characteristic coefficient basis

Write
\[
\nu=n_s,\quad b=n_{ts},\quad c_2=n_{tt},\quad e=n_{ss}\ne0,
\quad \beta=b+e\mu,\quad
\mathscr D=\partial_t+\mu\partial_s.
\]
The higher-degree result
[413](principal-paraboloid-higher-degree-characteristic-zero-reduction-pass413-working.md)
gives \(\mathscr D\mu=0\) in the zero-slope frame. This is a
coefficient conclusion, not a transfer of any degree-one scalar
exclusion. It could also be obtained from the all-degree412
high gates: beta*Dscript(mu)=0; the beta-zero alternative is
handled by the exact Legendre integration of413, Section2.

Since mu is not complex, mu_s is nonzero. Otherwise
Dscript(mu)=0 would give mu_t=0 as well. Set q=mu and use the
separating coefficient basis (t,q). Its exact partials are
\[
\dot{\ }=\mathscr D,\qquad {}'=\mu_s^{-1}\partial_s,\qquad
F=\ker_L(\dot{\ }),\qquad
\dot t=1,\quad\dot q=0,\quad t'=0,\quad q'=1.
\tag{6}
\]
The two partials commute, F is stable under primes, and their
joint constants remain C. The field L is finite over C(t,q).
No equality F=C(q) or L=F(t) is assumed.

The leading H equation at lambda=0 is
\(c_2+2qb+q^2e=0\). Since dot(q)=0, it says ddot(n)=0.
Exact integration inside L, along with dot(s)=q, gives
\[
\begin{gathered}
s=qt+f,\qquad n=At+B,\qquad f,A,B\in F,\\
D:=t+f'=s'=\mu_s^{-1}\ne0,\qquad
M:=A't+B',\\
\nu=M/D\ne0,\qquad
\beta=\dot\nu=\frac{A'f'-B'}{D^2}.
\end{gathered}
\tag{7}
\]
For example A=dot(n), B=n-t*dot(n), and f=s-qt are defined
elements of F. Nonzero nu follows from nu_s=e nonzero.
Every prime below is the q derivative at fixed t.

## 3. The quadratic profile supplies an affine intrinsic parameter

In the notation of407, delta=-nu is nonzero, so this is the
nonexceptional branch. Its rank/profile result for d=2 forces
\[
m=1,\qquad \deg_v R^{\rm ev}=0,\qquad R^{\rm ev}\in L^*.
\tag{8}
\]
Put \(\eta=\theta-q\sigma\). The complete shifted third level is
\[
H-h_0=\sigma R^{\rm ev}
 +y^2+n_ty+\frac e2\eta^2-C\eta+\nu\ell-h_0,\qquad
C=\ell_s+\nu^2,
\tag{9}
\]
where
\[
R^{\rm ev}=-\nu(2y+A)+\beta\eta-\dot\ell.
\tag{10}
\]
For (10),407's constant term is
\(-\nu n_t-\ell_t-q(\ell_s+\nu^2)=-\nu A-\dot\ell\),
since n_t+q*nu=A.

The functions y,eta have maximum intrinsic degree one by (8).
As R is constant and nu is nonzero, (10) expresses y as an
affine polynomial in eta. If eta were constant, y would also
be constant, contradicting m=1. Hence eta is affine nonconstant
on the original line and
\[
\begin{gathered}
O=L[\eta],\qquad \rho_\eta=N\eta\in L^*,\\
g:=2y+A=k\eta+g_0,\qquad
k=\beta/\nu,\quad g_0\in L,\\
P:=\sigma=p_2\eta^2+p_1\eta+p_0,\qquad p_2\in L^*.
\end{gathered}
\tag{11}
\]
These are intrinsic and coefficient-field presentations only.
In particular eta has not been identified with an original coordinate.

The literal rows following from264 are
\[
\begin{aligned}
Y&=XP+(k\eta+g_0-A)/2+tX^2,\\
Z&=P^2+(q+2tX)P+(tk+1)\eta+tg_0+B
                                      +(qt+f)X+t^2X^2,\\
W&=-k\eta P+(qX-g_0)P+(X-\nu)\eta+\ell+(qt+f)X^2.
\end{aligned}
\tag{12}
\]
This uses n_t+q*nu=A but no condition on lower scalar coefficients.

## 4. The original global slice licenses all-X polynomial return

The next generation statement is stronger than the intercept
return alone. It follows directly from the original slice in (1).
Since X has E-time degree one, write
\[
X=a_0u+b_0,\qquad b_0\in A_0.
\]
By264, Section1, N kills a0, so a0 belongs to L*. Its local-slice
localization gives
\(L[A_0]=A_0\otimes_{\ker N}L=O\).
Adjoining these rings inside the actual common fraction field,
\[
\boxed{
L[\mathcal B]=L[A_0][u]=O[u]=O[X]=L[X,\eta].
}
\tag{13}
\]
The equality O[u]=O[X] uses the polynomial inverse
\(u=(X-b_0)/a_0\), with b0 in O and a0 a unit of L.
No normality, rational coefficient-field assumption, or inference
from merely L[y,z,w]=O is used here.

Let Omega be an algebraic closure of L. Base extension and
specialization of the independent variable X preserve (13).
Thus for every \(x_0\in\Omega\),
\[
\boxed{\Omega[Y(x_0,\eta),Z(x_0,\eta),W(x_0,\eta)]
                    =\Omega[\eta].}
\tag{14}
\]
The elements x0 and eta are not asserted to be original coordinates.
Equation (14) is only a consequence of a polynomial-ring equality.

## 5. A finite collision forces k=g0=0

Use formal sums/products
\[
S=\eta_1+\eta_2,\qquad T=\eta_1\eta_2,\qquad
L_S=p_2S+p_1,
\]
and
\[
P_\Sigma=p_2(S^2-2T)+p_1S+2p_0,\qquad
H_\Delta=p_2(S^2-T)+p_1S+p_0.
\]
The three polynomial divided differences of (12) are exactly
\[
\begin{aligned}
\frac{Y(X,\eta_1)-Y(X,\eta_2)}{\eta_1-\eta_2}
 &=XL_S+k/2,\\
\frac{Z(X,\eta_1)-Z(X,\eta_2)}{\eta_1-\eta_2}
 &=(P_\Sigma+q+2tX)L_S+tk+1,\\
\frac{W(X,\eta_1)-W(X,\eta_2)}{\eta_1-\eta_2}
 &=-kH_\Delta+(qX-g_0)L_S+X-\nu.
\end{aligned}
\tag{15}
\]
They are polynomial identities, so also specialize to derivatives
when the two arguments coincide.

Suppose k is nonzero, or k=0 but g0 is nonzero. The polynomial
\[
(p_2S+p_1)(kS/2+g_0)+\nu
\tag{16}
\]
is respectively quadratic with nonzero leading coefficient or
linear with nonzero leading coefficient. It has a root S in
Omega. At any such root LS is nonzero, since nu is nonzero.
Define the finite elements
\[
x_0=-\frac{k}{2L_S},\qquad
T=\frac{L_SS+2p_0+q+1/L_S}{2p_2}.
\tag{17}
\]
The first two divided differences in (15) are then zero.
The third reduces to
\(-L_S(kS/2+g_0)-\nu\), so is zero as well.

Choose the two roots of z^2-S*z+T in Omega. If they are distinct,
the three generators in (14) take the same values at two distinct
eta values. Every polynomial in those generators then does too,
whereas eta does not. This contradicts (14).

If the roots coincide at eta0, the polynomial identities (15)
show that all three derivatives in eta vanish at eta0.
Every polynomial in the generators then has derivative zero there,
but the derivative of eta is one. This also contradicts (14).
Thus the repeated-root boundary does not evade the argument.

Both alternatives in (16) are impossible. Consequently
\[
\boxed{k=0,\qquad g_0=0,\qquad
\beta=0,\qquad y=-A/2.}
\tag{18}
\]
No root at infinity or coefficient-dependent actual coordinate
change was used. The divisions in (17) are licensed by p2 and
LS nonzero, before any specialization.

## 6. The remaining coefficient family has a nonzero dot-e

By (7),(18), beta=0 gives B'=A'f' and
\[
\nu=A'\in F^*,\qquad
e=\frac{A''}{D}\ne0,\qquad A''\ne0,\qquad
\dot e=-\frac{A''}{D^2}\ne0.
\tag{19}
\]
Indeed e=old partial_s(nu)=nu'/D. Both A'' and f' belong
to F, while dot(D)=1. No zero value of f' has been excluded.

Equations (10),(18) make R=-dot(ell). The nonzero gate (8)
therefore gives
\(\dot\ell\ne0\).
The quadratic coefficient in eta of (9), with y=-A/2,
then says
\[
\boxed{e=2p_2\dot\ell.}
\tag{20}
\]
The other terms in (9) contribute at most degree one in eta,
because y is now a coefficient element and C belongs to L.
This uses the exact H level, not only its homogeneous part.

## 7. Independent scalar and genuine-cubic coefficients conflict

Changing the coefficient basis and intrinsic affine parameter gives
\[
\widehat J(X)
=\det\frac{\partial(Y,Z,W)}{\partial(t,q,\eta)}
=-\frac{D a_0^4}{\rho_\eta}\in L^*.
\tag{21}
\]
The factor D/rho_eta follows from the Jacobian of
(t,s,v) with respect to (t,q,eta). Dots and primes on coefficients
remain the exact partials in (6), extended to fix eta and X.

Set X=0 in the full literal rows. This is legitimate because
(21) is independent of X. After (18), the intercepts are
\[
y=-A/2,\qquad z=P^2+qP+\eta+B,\qquad w=\ell-\nu\eta.
\tag{22}
\]
Using dot(A)=dot(B)=dot(nu)=0 and A'=nu, their complete
determinant is
\[
\boxed{
\widehat J(0)
=-\frac{\nu}{2}
 \left[(2P+q)\bigl(\nu\dot P+\dot\ell\,P_\eta\bigr)
                                     +\dot\ell\right].
}
\tag{23}
\]
For example the first differential row is (0,-nu/2,0);
this displays the orientation explicitly. Its degree-four
coefficient is
\[
[\eta^4]\widehat J(0)=-\nu^2p_2\dot p_2.
\tag{24}
\]
Calibration and nonzero nu,p2 force \(\dot p_2=0\).

Now use the complete genuine Q of365:
\[
\begin{aligned}
Q={}&[(c_2+2\ell_s)P+bV-2bP^2-2ePV-\ell_t]U\\
&+\frac{n_{ttt}}6P^3+\frac{n_{tts}}2P^2V
  +\frac{n_{tss}}2PV^2+\frac{n_{sss}}6V^3\\
&-\frac{\ell_{tt}+2bn_t}{2}P^2
 -(\ell_{ts}+\nu b+en_t)PV
 -\frac{\ell_{ss}+2\nu e}{2}V^2\\
&+(b\ell+n_t\ell_s-(h_0)_t)P
 +(e\ell+\nu\ell_s-(h_0)_s)V .
\end{aligned}
\tag{25}
\]
All derivatives displayed in (25) are the original t,s coefficient
partials. Both actual level derivatives are retained.

Substitute U=-A/2 and V=qP+eta only after forming this polynomial.
The relations beta=0, dot(q)=0 and the H-top identity give
\[
\begin{gathered}
b=-qe,\qquad c_2=q^2e,\qquad n_t=A-q\nu,\\
n_{tts}+2q n_{tss}+q^2n_{sss}=0,\\
n_{ttt}+3q n_{tts}+3q^2n_{tss}+q^3n_{sss}=0,\\
\dot e=n_{tss}+q n_{sss},\qquad
\ddot\ell=\ell_{tt}+2q\ell_{ts}+q^2\ell_{ss}.
\end{gathered}
\tag{26}
\]
The second line follows by differentiating beta=0 by dot;
the third follows by differentiating
c2+2q*b+q^2e=0. The potential coefficient derivatives are
not being evaluated at a silently fixed old s.

Consequently the substituted Q has no P^3 or P^2*eta term.
Its P^2 coefficient is -ddot(ell)/2 and its P*eta^2
coefficient is dot(e)/2. Every other term has eta degree
at most three after P=p2*eta^2+p1*eta+p0. In particular
the two h0-derivative terms have degree at most two.
The exact degree-four coefficient is therefore
\[
[\eta^4]Q(-A/2,P,qP+\eta)
=\frac{p_2}{2}\bigl(\dot e-p_2\ddot\ell\bigr).
\tag{27}
\]
The genuine Q level is a coefficient constant, so (27) is zero.
Thus dot(e)=p2*ddot(ell).

On the other hand, differentiate (20) and use dot(p2)=0 from
(24). This gives dot(e)=2p2*ddot(ell). Comparing the two
equalities, with p2 nonzero, forces ddot(ell)=0 and dot(e)=0.
This contradicts (19). No trace, logarithmic-primitive argument,
normalization theorem or conductor calculation is needed.

## 8. Exact conclusion and verification boundary

The complete actual normalized zero-leading-slope profile
(r,m,d)=(0,1,2) is excluded. Because407 forces that profile for
every normalized lambda=0,d=2 case, and384 licenses the complex
constant shear (3), the conclusion applies to (2).

It does not exclude a noncomplex leading lambda, equal degree
three or higher, arbitrary coupling k, a different initial kernel,
or general chart entry. The all-X polynomial generation argument
is an actual-ring consequence proved in Section4; it has not
been inferred from a coefficient-field coordinate or merely
from intercept field return.

The complete413 source was read in a839fc, and384 was read
without truncation in fbc259. Direct264,365,296 and407 had been
read in4abd4f,142531,08e97c and66989e. The complete400 and401
inputs were read in87a5b1 and fe4a37+a78e8e. The writing guide
was reread in668490 before authoring this note.

Fresh unsaved32bc0f independently reconstructed all three
divided differences (15), their residual after (17), the entire
scalar (23), its coefficient (24), and the full genuine Q
coefficient (27), retaining both h0 derivatives. Every residual
was zero; both possible Q coefficients above degree four
were zero as well. These controls do not prove all-X return,
the repeated-root obstruction, or the exact-field integrations;
those proofs are written above.

No saved checker was executed, imported, compiled or rerun.
No earlier held source or canonical index was edited. This note
is held for independent review and asserts no unrestricted
cancellation, novelty, human-expert verification or formal
proof certification.
