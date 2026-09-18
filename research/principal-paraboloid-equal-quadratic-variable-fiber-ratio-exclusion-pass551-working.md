# The variable fiber-ratio part of the B-Laurent branch is impossible

Working bounded exclusion: retain the FULL actual264/296/535 chart,
the noncomplex-leading-coefficient reflection family547, and its
actual normalization548. In the B-Laurent alternative, the fiber
ratio F cannot have nonzero m derivative. This is complementary to
550, but its proof does not import the zero-F-prime conclusion.
The final contradiction uses the ENTIRE original X-dependent scalar.

## 1. Actual hypotheses, finite fields and notation

Retain every hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md)
and [535](principal-paraboloid-nonlinear-sigma-unit-multiplier-pass535-working.md).
In particular retain the original global slice, the entire initial
kernel, the selected literal partial, both returns, the genuine
potentials and moving levels, and the whole scalar. Thus
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=\mathcal A[u],\quad E=\partial_u,
\quad X=a_0u+x_0,\quad a_0\ne0,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\qquad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2),\\
N=[u^4]\partial_Z|_{\mathcal A}\ne0,\quad
Na_0=Nt=Ns=0,\quad Nv=1,\\
L=\operatorname{Frac}\ker_{\mathcal A}N,\quad
[L:\mathbb C(t,s)]<\infty,\quad L[\mathcal A]=L[v],\\
\operatorname{Frac}\mathcal A=L(v)=\mathbb C(y,z_{\rm int},w),
\quad L[y,z_{\rm int},w]=L[v],\quad J_{t,s,v}(X)=-a_0^4.
\end{gathered}
\tag{1}
\]
Here z_int is the literal Z intercept, not a later subtraction of
2ty. The entire initial kernel, rather than one initial relation,
is part of the input.

Use the intrinsic normalization of
[547](principal-paraboloid-equal-quadratic-zero-characteristic-reflection-rigidity-pass547-working.md)
and the ACTUAL complex translation and shear of
[548, Sections 1--3](principal-paraboloid-equal-quadratic-constant-laurent-exclusion-pass548-working.md).
The latter source and the complete
[550](principal-paraboloid-equal-quadratic-stationary-linear-fiber-exclusion-pass550-working.md)
have been read through EOF. In this frame write
\[
\begin{gathered}
\sigma=x^2+c,\quad\theta=\mu x^2+d x+e,\quad
y=A x^2+B x+C,\qquad d\ne0,\\
m=k_s\notin\mathbb C,\quad h=m_s\ne0,\quad
D=\partial_t+\mu\partial_s,\quad Dm=0,\\
A=\alpha/m,\quad\chi=2\alpha/m^2,\quad
DA=0,\quad D\mu=-\chi,\quad\alpha\in\mathbb C^*.
\end{gathered}
\tag{2}
\]
The letter A denotes this coefficient, not the invariant ring
\(\mathcal A\). The scalar normalization may use
x=rho(v-v0), with rho squared in L*, and L'=L(rho). All coefficient
partials now fix x. We retain Nx=rho; we do not set Nx=1 or assert
that rho descends to L. The exact covariance is
\[
J_{t,s,x}=-a_0^4/\rho,\qquad
\kappa=\kappa_v/\rho^2\in(L')^*,\qquad
J_{t,m,x}(X)=-a_0^4/(h\rho).
\tag{3}
\]
The coefficient basis (t,m) is separating because h is nonzero.
A dot denotes D, and a prime initially denotes the commuting
partial_m at fixed t. The field F0=ker_D L' is finite over C(m),
not assumed rational. Its prime constants, and the joint constants
of the two exact partials, are C.

Put p=m_t and k1=k_t, where these derivatives are in the original (t,s) basis,
and set
\[
H=hd^2/2,\qquad j=2c+k_1,\qquad
\nu_0=\{h(e-\mu c)+n_s\}/m,\qquad
\overline C=2(C-Ac)+H+Dn.
\tag{4}
\]
The B-Laurent branch means B nonzero and nu0=Cbar=0. These are the
necessary nonzero-monomial alternatives from the full all-X return,
not independently assigned equations for a formal family. The
bounded extra hypothesis here will be F' nonzero, with F defined
from the actual fiber below.

## 2. The entire actual fiber, its invariant and its generic matrix

In this actual frame \(\mathcal B_{a_0}=\mathcal A_{a_0}[X]\).
The prime coordinate X does not divide a0: additivity of E-degree
would otherwise contradict deg_E a0=0. Hence contraction of (X)
after localization is exact and
\[
\mathcal B/(X)=\mathbb C[Y,Z,W]\hookrightarrow\mathcal A_{a_0},
\qquad (\mathcal B/(X))_{a_0}\simeq\mathcal A_{a_0}.
\tag{5}
\]
Every fiber in this argument is this fixed actual X=0 fiber. It is
not obtained by substituting a coefficient-field root for X.

Extend N by Nu=0. The polynomial derivation
Delta=a0*N-(NX)E fixes X and descends to (5). It is a nonzero LND:
in the coefficient-field embedding it acts as
a0*rho*partial_x, with invariant speed, and the quadratic coefficient
A of Y is nonzero. Its kernel has transcendence degree two by the
local-slice argument, so it contains a nonconstant actual polynomial
invariant. This does not require a global slice for Delta or an
identification of its original fraction field with L'(x).

Use the actual fiber coordinate U=Y squared+alpha W, with inverse
W=(U-Y squared)/alpha. This shear need not preserve the time-degree
profile or the four-generator initial kernel; it is used here only
as an actual coordinate change and to compute its scalar. The full
second potential, including its constant term, is
\[
mw=\ell-(2\sigma+k_t)y-k_{tt}\sigma^2/2-m_t\sigma\theta
       -h\theta^2/2-n_t\sigma-n_s\theta.
\tag{6}
\]
Expanding it gives the entire fiber identities
\[
\begin{gathered}
Y=A x^2+B x+C,\quad
Z=x^4+z_2x^2+(2tB+md)x+z_0,\\
z_2=2tA+2c+k_1+m\mu,\qquad
z_0=2tC+c^2+k_1c+me+n,\\
T_2=[x^2]U=B^2-A^2k_1-A(H+Dn),\qquad
F=T_2/A,\qquad U=FY+L_1x+R,\qquad L_1=-B^3/A.
\end{gathered}
\tag{7}
\]
In particular the ORIGINAL linear coefficient 2tB+md is retained.
No lower coefficient of U, hence no ell term, has been deleted;
R is its exact remaining intercept after subtracting FC.

For completeness, DT2=0 follows from the actual invariant just
described. If T2 is nonzero and algebraically independent of m,
the positive initial images
\(A\eta^2,\eta^4,T_2\eta^2\) are algebraically independent over C.
Their field contains m algebraically by the ratio of the second to
the square of the first, and then eta and T2 algebraically. Thus an
injective positive-weight initial map would make every nonconstant
actual polynomial in Y,Z,U have positive intrinsic degree. This
contradicts the nonconstant Delta-invariant. Consequently T2 is
algebraic over C(m), and DT2=0 by separability. The case T2=0 has
the same derivative conclusion immediately. Thus F belongs to F0.

After subtracting F times the Y differential row, the ENTIRE fiber
matrix against (t,m,x) is
\[
\begin{pmatrix}
\dot Bx+\dot C&A'x^2+B'x+C'&2Ax+B\\
\dot z_2x^2+(2B+2t\dot B+m\dot d)x+\dot z_0&
z_2'x^2+(2tB+md)'x+z_0'&4x^3+2z_2x+2tB+md\\
\dot L_1x+\dot R&F'Y+L_1'x+R'&L_1
\end{pmatrix}.
\tag{8}
\]
Its determinant is \(-\alpha a_0^4/(h\rho)\), a nonzero
coefficient-field scalar independent of x. It need not be complex.
The sixth coefficient is
\[
[x^6]J={4\over m}(3B^2-\alpha F')\dot B.
\tag{9}
\]
It forces DB=0 even when the first factor vanishes: differentiating
3B squared=alpha F' by D then gives 6B DB=0, since DF=0 and the
partials commute. Hence DL1=0. The genuine branch identities give
\[
F=B^2/A+2C-Aj,\quad Dk_1=-2A,\quad
Dj=2\dot C/A,\quad Dc=A+\dot C/A,\quad
\dot z_2=2\dot C/A.
\tag{10}
\]
Now the fifth coefficient of (8) is 4A' dot R. Since
A'=-alpha/m squared is nonzero, DR=0.

Introduce the coefficient expression v1=d+2tB/m. This is not an
ambient coordinate. The next coefficient of the same full matrix is
\[
[x^4]J={2\over m}\{(mBF'+L_1)\dot C+
                                    \alpha^2F'\dot v_1\}.
\tag{11}
\]
In particular dot v1 is dot d+2B/m, not dot d alone.

## 3. A nonzero F prime forces a stationary residual slope

Assume F' nonzero. First dot C is nonzero. Otherwise (11) forces
dot v1=0, and (10) gives dot z2=0. The whole determinant (8) is then
\[
\dot z_0\{(2Ax+B)(F'Y+L_1'x+R')
                         -L_1(A'x^2+B'x+C')\}.
\tag{12}
\]
The bracket has degree three with nonzero leader 2A squared F'.
If dot z0=0 the determinant is zero, and otherwise it has positive
x degree. Both contradict its genuine nonzero scalar value.

The existing pair (C,m) is therefore another separating coefficient
basis. We continue to use the prime on F0, where it agrees with
partial_m at fixed C. The field L' remains finite over C(C,m),
and C is transcendental over F0. Integrating (11) and (10) by
subtraction gives existing eta,v0,K in F0 with
\[
\begin{gathered}
v_1=\eta C+v_0,\quad
\eta=-{mBF'+L_1\over\alpha^2F'},\qquad
z_2=2C/A+K.
\end{gathered}
\tag{13}
\]
Eta is allowed to vanish. No division by eta is used.

In the new basis the complete rows, still with arbitrary z0, are
Y=A x squared+B x+C,
Z=x to the fourth+(2C/A+K)x squared+m(eta C+v0)x+z0,
U=FY+L1 x+R. Their x-cubed scalar coefficient determines
\(\partial_Cz_0=2C/A^2+\zeta\), and hence
\(z_0=C^2/A^2+\zeta C+G\), with zeta,G in F0. Explicitly, if
f=F' and b'=B', the entire coefficient gives
\[
\zeta={m\over2\alpha^5 f^2}
\left(2\alpha^4Kf^2+\alpha^2m^2B^2f^2
-2\alpha m^3B^3b'f-4\alpha m^2B^4f
+6m^3B^5b'+3m^2B^6\right).
\tag{14}
\]
Only the already nonzero F' is divided in this formula.

For clarity, these integrations leave the following ENTIRE matrix,
not just selected leading rows:
\[
\begin{pmatrix}
1&A'x^2+B'x&2Ax+B\\
2x^2/A+m\eta x+2C/A^2+\zeta&
(2C/A+K)'x^2+\{m(\eta C+v_0)\}'x+
 (C^2/A^2+\zeta C+G)'&
4x^3+2(2C/A+K)x+m(\eta C+v_0)\\
0&F'Y+L_1'x+R'&L_1
\end{pmatrix}.
\tag{15}
\]
Primes in this matrix differentiate at fixed C. Its determinant is
the original fiber scalar divided by dot C, still a unit independent
of x. Substituting (13)--(14), its complete x-squared coefficient
is affine in C and has C coefficient
\[
[x^2C]J_{C,m,x}={3mB\over\alpha^2}(\alpha F'-B^2).
\tag{16}
\]
As C is transcendental over F0 and B is nonzero, it follows that
\[
F'=B^2/\alpha,\qquad\eta=0,\qquad Dv_1=0,
\qquad \zeta=K/A+2m^4BB'/\alpha^3.
\tag{17}
\]
No constant scalar coefficient has been set to zero.

## 4. Full high gates and genuine mixed derivatives force B complex

In this section dots and primes again mean the exact commuting
partials in (t,m), with primes fixing t. On F0 this agrees with the
fixed-C derivative in (15), but it is not that derivative on C,c,e
or n. This distinction is retained in the mixed-potential argument.

The two full535 cubic identities, with all lower terms retained
in their derivation, are
\[
4DB+2dA_s=-\kappa h(2B+dm\mu_s)/m,
\qquad2Dd+d\mu_s+6B/m=\kappa hd/m.
\tag{18}
\]
Set zeta0=2B/(md). Since DB=0 and A_s=-Ah/m, the first equation
gives chi=kappa(mu_s+zeta0). Because Dv1=0 gives
Dd=-2B/m=-zeta0*d, the second gives
mu_s+zeta0=kappa*h/m. Eliminating kappa yields
\[
(\mu'+\zeta_0s')^2=(\chi/m)s'.
\tag{19}
\]
This calculation divides only nonzero B,d,m,h and alpha, and keeps
v1=0 as an allowed case.

Exact characteristic integration from Dmu=-2alpha/m squared gives
mu=-2alpha*t/m squared+M and
s=-alpha*t squared/m squared+Mt+S, with M,S in F0. Put
tau=mv1/(2B) in F0, T0=t-tau and eta0=2alpha/m cubed. Then
d=-2BT0/m, zeta0=-1/T0, and DT0=1, so T0 is nonzero. Write
s'=eta0*T0 squared+b1*T0+c1, with b1,c1 in F0. Since mu'=D(s'),
(19) becomes
\((\eta_0T_0-c_1/T_0)^2=\eta_0(\eta_0T_0^2+b_1T_0+c_1)\).
After multiplying by T0 squared, polynomial comparison over F0
gives b1=c1=0. Therefore
\[
s'=2\alpha(t-\tau)^2/m^3,\qquad
H=hd^2/2=B^2/A.
\tag{20}
\]
Tau need not yet be complex, and no rationality of F0 was used.

The next step uses the genuine n potential, rather than independent
assignments of lower z0 and e functions. From nu0=Cbar=0,
\[
n'=\mu c-e,\quad Dn=-2C+2Ac-H,\quad k_1'=-\mu.
\tag{21}
\]
Differentiate the literal z0 in (7). Together with (10) this gives
the two whole identities
\[
z_0'-me'=2tC'+jc',\qquad
\dot z_0-m\dot e=Aj-H+(2t+j/A)\dot C.
\tag{22}
\]
For example the second uses the ORIGINAL 2tC and c squared terms
of z0. Differentiating the first by D and the second by the prime,
then subtracting with commuting partials, gives
\[
\dot e=F'-(B^2/A)'+A'j+H'+(\mu/A)\dot C.
\tag{23}
\]
This is a genuine mixed-potential condition. Insert (17),(20) and
Aj=2C-F+B squared/A. It reduces to
\[
\dot e=-(2C-F)/m+(\mu/A)\dot C,
\qquad \dot z_0=(z_2/A)\dot C.
\tag{24}
\]
Since dot C is nonzero, compare (24) with the entire integrated
z0 in (14)--(15): zeta=K/A. Equation (17) now forces B'=0.
Thus joint constants give
\[
B\in\mathbb C^*,\qquad F=B^2m/\alpha+f_0,
\qquad f_0\in\mathbb C.
\tag{25}
\]

## 5. The stationary time translation is also complex

The remaining positive coefficients of the same full matrix (15),
after (17) and B'=0, are
\[
\begin{aligned}
[x^2]J&=-{B\over\alpha^3}
 \{\alpha^3Bv_1+\alpha^2mB^2K'-2\alpha^2mR'\},\\
[x]J&=-{mB^3\over\alpha}(mv_1)'.
\end{aligned}
\tag{26}
\]
Consequently mv1=E0 is complex and
\[
\tau=E_0/(2B)\in\mathbb C,\qquad
R'=B^2K'/2+\alpha B^2\tau/m^2.
\tag{27}
\]
This permits E0=v1=tau=0. Neither K nor R nor their derivatives
have been divided away.

Now compare the exact characteristic polynomial in t with (20).
Integration by subtraction in F0 gives complex mu_c,s_c with
\[
s=-\alpha(t-\tau)^2/m^2+\mu_c t+s_c,
\qquad\mu=-2\alpha(t-\tau)/m^2+\mu_c.
\tag{28}
\]
Likewise k'=m s' and D squared k=-4A give
\[
k=-2\alpha(t-\tau)^2/m+u_1(t-\tau)+u_0,
\qquad u_1,u_0\in\mathbb C.
\tag{29}
\]
For the last descent the difference has m derivative zero and
second t derivative zero. Subtract its affine t polynomial and use
the joint constant field; no assumption F0=C(m) or L'=F0(t) enters.

## 6. Actual complex normalization, followed by reapplication

The constants just proved complex permit the following simultaneous
ACTUAL polynomial map, with OLD rows on the right:
\[
\begin{aligned}
X_1&=X,&Y_1&=Y-\tau X^2,\\
Z_1&=Z-2\tau Y+\tau^2X^2,&
W_1&=W-\mu_cY-s_cX^2.
\end{aligned}
\tag{30}
\]
Its inverse is Y=Y1+tau X squared,
Z=Z1+2tau Y1+tau squared X squared,
W=W1+mu_c Y1+(mu_c tau+s_c)X squared. Direct full-row expansion gives
\[
\begin{gathered}
t_1=t-\tau,\quad s_1=s-\mu_ct-s_c=-\alpha t_1^2/m^2,\\
\sigma_1=\sigma,\quad y_1=y,\quad\theta_1=\theta-\mu_c\sigma,
\quad k_1^{\rm pot}=k,\quad n_1=n.
\end{gathered}
\tag{31}
\]
Here k1pot is distinguished from the derivative k1 used earlier.
In the first new frame (29) is -2A t1 squared+u1 t1+u0. Next use
\[
Y_2=Y_1+(u_1/2)X,\qquad Z_2=Z_1-u_0X,\qquad W_2=W_1.
\tag{32}
\]
The inverse subtracts the indicated X terms. This gives
k2=k1pot-u1*t1-u0, sigma2=sigma1+u1/2, and
n2=n1-(u1/2)(k1pot)_{t1}+(u1/2) squared. The other intercepts
are obtained from the entire same rows, not freely reassigned.

These are actual members of the completely read class
[426](general-coupling-normalization-obstruction-pass426-working.md).
Both maps have complex coefficients and row determinant one; their
time-base determinant is one. The original E, global slice and
kernel remain unchanged. Their full weighted leading maps preserve
the entire paraboloid initial kernel and the exact time profile.
In particular X squared Z1-Y1 squared=X squared Z-Y squared for
(30), and (32) changes neither leading relation. The selected
literal Z partial is unchanged by both maps, so N,L,v,a0 and rho
remain the same. The actual localized fiber proof preserves both
the literal complex-field return and the whole polynomial return.
Their full calibration is still (3). No noncomplex coefficient is
used in an ambient map.

The coefficients A,B,alpha,m are unchanged. The identities nu0=0
and Cbar=0 are preserved, as follows by matching the full potentials
using q=0 and Dk1=-2A. For example under (32), with gamma=u1/2,
nu0 changes by -gamma(h mu+p)/m=0, whereas Dn changes by 2gamma A
and 2(C-Ac) by -2gamma A. After (30), d=-2Bt1/m.
On the actual zero fiber (30) replaces U by U-alpha*mu_c*Y,
so F is replaced by F-alpha*mu_c and its nonzero m derivative is
preserved. Map (32) changes none of those fiber rows. Thus the
variable-ratio hypothesis needed for the following reapplication
is itself retained, not inferred from a new unproved entry claim.

Drop all subscripts and REAPPLY (7)--(27) to this actual new frame.
This step does not identify its new f0 with the old one. It gives
fresh complex f0,H0 and existing coefficient functions C,e0,g with
\[
\begin{gathered}
s=-\alpha t^2/m^2,\quad\mu=-2\alpha t/m^2,\quad
k=-2\alpha t^2/m,\quad k_t=-2At,\quad d=-2Bt/m,\\
F=B^2/A+f_0,\quad c=(C-f_0/2)/A+At,
\quad z_2=(2C-f_0)/A,\quad K=-f_0/A,\\
R-B^2K/2=H_0\in\mathbb C.
\end{gathered}
\tag{33}
\]
The new residual v1 is zero. Formula (24), now in this frame,
integrates by subtraction to
\[
e=B^2t/\alpha-2t(C-f_0/2)/m+e_0(m),\qquad
z_0=(C-f_0/2)^2/A^2+g(m),\qquad e_0,g\in F_0.
\tag{34}
\]
They need not be rational functions of m. The coefficient C and
its derivatives have not been fixed or suppressed. Dot C remains
nonzero, either by the reapplied Section3 argument or directly by
the nonzero scalar below.

## 7. The entire X-dependent determinant gives the contradiction

Define auxiliary polynomial expressions
\[
T=x^2+(C-f_0/2)/A+tX,\qquad Q=AT+Bx,
\qquad h_0=H_0+f_0^2/4\in\mathbb C.
\tag{35}
\]
Neither T nor Q is asserted to be an actual coordinate, a
coefficient-field element, or an N-slice. Direct substitution of
the genuine potentials and (33)--(34) in ALL original rows gives
\[
\boxed{\begin{aligned}
Y&=(A+X)T+Bx+f_0/2,\\
Z&=T^2+g(m),\\
\alpha W&=B^2T-Q^2+h_0+\alpha e_0(m)X.
\end{aligned}}
\tag{36}
\]
These are entire identities, including every X power. To see the
W identity without discarding its lower terms, put S=T-tX. At the
actual zero fiber, alpha*w=B squared*S-(AS+Bx) squared+h0.
Furthermore alpha*theta=B squared*t-2At(AS+Bx)+alpha*e0 and
alpha*s=-A squared*t squared. Adding theta X+sX squared gives
the last line of (36). Similarly 2t sigma+k=2tS, so the entire Z
row is (S+tX) squared+g. Thus the original 2tB+md term was retained
until the LICENSED normalization made it zero.

Compute formally with T,m,x independent, keeping genuine m
derivatives of A and all coefficient functions. The ENTIRE
determinant of (36) is
\[
\det{\partial(Y,Z,W)\over\partial(T,m,x)}
={-B^3g'+2BX\{(\alpha e_0'-Ag')T-Bg'x\}\over\alpha}.
\tag{37}
\]
The chain rule, now substituting the full expression (35), gives
\[
J_{t,m,x}(X)=\left(\dot C/A+X\right)
 {-B^3g'+2BX\{(\alpha e_0'-Ag')T-Bg'x\}\over\alpha}.
\tag{38}
\]
This is a polynomial chain-rule identity; no division by the
moving factor dot C/A+X is used and no root of it is removed.

By the genuine scalar (3), the left side is a nonzero element of
L', independent of BOTH X and x. Its X=0 value and its Xx
coefficient from (38) are respectively
\[
J\big|_{X=0}=-{B^3m\dot C g'\over\alpha^2}\ne0,
\qquad [Xx]J=-{2B^2m\dot C g'\over\alpha^2}
             ={2\over B}J\big|_{X=0}\ne0.
\tag{39}
\]
This is impossible. It uses neither an e0-prime division nor an
extra x-squared coefficient. It allows every zero value of tau,
v1, eta, K, f0,H0,h0 and e0 consistent with earlier equations.
If g were constant or dot C zero, the first coefficient in (39)
would already contradict the actual scalar. All lower functions
and their exact derivatives remain present in (37)--(38).

## 8. Verification and precise scope

Complete548 and550 were read through EOF before use. Fresh d7dfb3
reconstructed the entire generic matrix (15), the unrestricted
eta/zeta integrations, (16), and both coefficients (26). Earlier
fresh daa9aa/f9bc02 and aa4cc3 independently retained the same lower
functions. The genuine mixed-potential identities were checked
directly from the original intercepts; General's independent
af3594 also reconstructs them, and fd776a reconstructs the full
variable-ratio fiber chain. The actual simultaneous maps and their
inverse were independently checked by General, including n2 and
the selected partial. Its fresh0670f9 checks the last stationary
fiber coefficients without omitting 2tB.

Fresh25043f reconstructs the ENTIRE determinant (37)--(38) and both
coefficients (39); Root's independent486e59 matches it. As an
additional full-row check, fresh0699bf/ed379e gives, before complex
normalization, the global U-row scalar coefficient
-4alpha/m cubed times
(alpha*h*d squared/2-m squared*B*Dd-3mB squared) at Xx to the fifth.
Together with Dv1=0 it reproduces H=B squared/A. The written proof
instead establishes that gate from the full cubic identities (18),
so it does not rely on a discarded or isolated scalar ansatz.

The conclusion is only the exclusion of F_m nonzero in the
B-Laurent branch under the full necessary family547 and its actual
normalization548. Source550 separately addresses F_m=0. No other
Laurent alternative, no arbitrary chart entry, and no global
cancellation theorem is claimed here. Earlier recognition ancestors
are retained, not recursively recertified. No finite-field element
is silently declared rational or promoted to an ambient coordinate.

No saved checker was executed, imported, compiled or rerun. No
earlier source or canonical record was edited. This source requires
separate complete saved-source review before acceptance.
