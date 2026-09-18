# The zero-characteristic equal-quadratic branch has noncomplex first leader

Working bounded exclusion: retain the FULL actual264/296 chart and
the cleared unit multiplier535. Suppose sigma is quadratic, theta
has a nonzero linear residual after its quadratic part is removed,
and m is noncomplex. In the notation below, the two conditions
q=0 and A in C are incompatible with this actual chart.

Both B=0 and B nonzero are included. The first case reduces by an
actual complex shear to the already excluded variable-coupling
quadratic-sigma/affine-theta profile542. The second case contradicts
two complete multiplier coefficients after an actual three-ring
initial-independence argument. This note does not exclude q=0 with
noncomplex A and makes no claim of arbitrary chart entry.

## 1. Actual input, finite intrinsic normalization and exact units

Retain every hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
the genuine potentials and levels of
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md),
and the proved cleared multiplier of
[535](principal-paraboloid-nonlinear-sigma-unit-multiplier-pass535-working.md).
In particular,
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=\mathcal A[u],\quad
E=\partial_u,\quad X=a_0u+x_0,\quad a_0\ne0,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\quad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the entire original initial kernel},\\
0\ne N=[u^4]\partial_Z|_{\mathcal A},\quad
Na_0=Nt=Ns=0,\quad L=\operatorname{Frac}\ker_{\mathcal A}N,\\
[L:\mathbb C(t,s)]<\infty,\quad L[\mathcal A]=L[v],\quad Nv=1,\\
\operatorname{Frac}\mathcal A=L(v)=\mathbb C(y,z_{\rm int},w),\quad
L[y,z_{\rm int},w]=L[v],\quad J_{t,s,v}(X)=-a_0^4.
\end{gathered}
\tag{1}
\]
The symbol z_int denotes the literal Z-intercept. The original
global slice, both returns, the full scalar and the selected literal
partial remain part of the input.

Complete the square in sigma in the ORIGINAL intrinsic polynomial
ring. Write its nonzero quadratic coefficient as rho squared after
a finite separable coefficient extension L'/L, and put
x=rho*(v-v0). Then
\[
\sigma=x^2+c,\qquad \theta=\mu x^2+d x+e,\qquad d\ne0.
\tag{2}
\]
The ratio mu, the critical value e and c belong to L. The coefficients
rho,d and x may require L'. This normalization is intrinsic only.
No root is asserted to descend to L or to be an actual coordinate.
The theorem includes mu=0; its genuinely equal-quadratic application
has mu nonzero. The d=0 profile is outside this note.

Coefficient partials henceforth fix x, and extend uniquely to L'.
On original L they are the original commuting partials. Put
\[
p=m_t,\quad h=m_s,\quad q=p+h\mu,\quad
D=\partial_t+\mu\partial_s.
\tag{3}
\]
Assume m not in C and q=0. Thus m and h are nonzero: if h=0,
then q=0 gives p=0 and the joint exact constants make m complex.
Joint constants of L' are also C, by finite separability over C(t,s).

The precise parameter covariance is
\[
Nx=\rho,\qquad J_{t,s,x}=-a_0^4/\rho,\qquad
\kappa=\kappa_v/\rho^2\in(L')^*.
\tag{4}
\]
Indeed the parameter Jacobian is rho, the primitive tangent is
divided by rho, and its cross-product multiplier is multiplied by
rho. The identity kappa=-J0/tau of535 gives (4). We do not set
Nx=1 or replace the scalar by an independently chosen constant.

## 2. Complete potentials and the high coefficient pedigree

Use formal independent U,P,V and write
\[
\begin{aligned}
F(P,V)&=k_{tt}P^2/2+pPV+hV^2/2+n_tP+n_sV,\\
G(U,P,V)&=\{\ell-(2P+k_t)U-F(P,V)\}/m,\\
H(U,P,V)&=U^2+F_PU+F_VG
 +k_{ttt}P^3/6+p_tP^2V/2+h_tPV^2/2+h_sV^3/6\\
&\quad+n_{tt}P^2/2+n_{ts}PV+n_{ss}V^2/2-\ell_tP-\ell_sV.
\end{aligned}
\tag{5}
\]
The entire evaluation at (y,sigma,theta) is H=h0 in L'. The
formal derivatives f=H_U evaluated and g=H_V evaluated are taken
BEFORE this substitution. The original rows are exactly
\[
\begin{aligned}
Y&=y+\sigma X+tX^2,\\
Z&=2ty+\sigma^2+k_t\sigma+m\theta+n+(2t\sigma+k)X+t^2X^2,\\
W&=G(y,\sigma,\theta)+\theta X+sX^2.
\end{aligned}
\tag{6}
\]
All lower coefficients and moving levels are retained.

For inspection, put beta=sigma_x=2x, d_y=y_x and e_theta=theta_x.
Also put nu=F_V evaluated/m, D_f=(2sigma+k_t)/m and
B_f=(2y+F_P evaluated)/m. The ENTIRE multiplier equations are
\[
\begin{aligned}
\mathcal A_\beta&=\beta^2y_t+\beta e_\theta y_s+d_y^2
 -\beta\sigma_t d_y-\sigma_s d_y e_\theta=\kappa g,\\
\mathcal B_\beta&=\beta^2(\theta_t+B_f)+D_f\beta d_y+d_y e_\theta
 +\beta(\theta_s+\nu-\sigma_t)e_\theta-\sigma_s e_\theta^2
 =-\kappa f.
\end{aligned}
\tag{7}
\]
No coprimality of f and g is assumed.

These equations first force deg_x y<=2, including y=0. If its
degree j were greater than two with leader r_j, the two whole
groups beta squared*2y/m and (2sigma/m)*beta*y_x in B_beta
have combined highest coefficient 4(j+2)r_j/m at degree j+2.
Every term outside these groups has degree at most max(4,j),
whereas deg f<=max(j,3) because q=0. Thus the top cannot cancel.
Write
\[
y=A x^2+B x+C,\quad
\Phi=k_{tt}+2p\mu+h\mu^2,\quad
\chi=(4A+\Phi)/m.
\tag{8}
\]
Here A belongs to original L, since it is the ratio of the original
quadratic coefficients of y and sigma. B may belong only to L'.
We now impose the additional hypothesis of this note: A is complex.
Its value may be zero.

To derive all high identities needed below, define frozen-direction
expressions
\[
M_2=p_t+2\mu h_t+\mu^2h_s,\qquad
K_3=k_{ttt}+3\mu p_t+3\mu^2h_t+\mu^3h_s.
\tag{9}
\]
These are not obtained by silently treating mu as constant under D.
Direct expansion of the FULL polynomials (5),(7), with q=0, gives
\[
\begin{array}{c|c}
\text{coefficient}&\text{exact value}\\ \hline
[x^6]H&K_3/6\\
[x^5]H&d(M_2-h\chi)/2\\
[x^4]g&(M_2-h\chi)/2\\
[x^3]f&-2dh/m\\
[x^4]\mathcal A_\beta&4DA\\
[x^4](\mathcal B_\beta+\kappa f)&4(D\mu+\chi).
\end{array}
\tag{10}
\]
The last row first gives Dmu=-chi. Since q vanishes identically,
\(0=Dq=M_2+hD\mu\), so M2=h*chi and the g coefficient in
(10) vanishes. The first multiplier equation then gives DA=0,
also valid without the current complex-A hypothesis. The H level
gives K3=0. Differentiating Phi correctly gives
\(D\Phi=K_3+2qD\mu\); since Dm=q=0, it follows that Dchi=0.
Thus
\[
Dm=DA=D\chi=0,\qquad D\mu=-\chi.
\tag{11}
\]

For completeness, (t,m) is a legitimate separating coefficient
basis because its original Jacobian is h. Its t partial is D.
The field F=ker_D L' is finite over C(m), not presumed rational.
From Ds=mu and (11), and from
D squared k=k_tt+2mu*p+mu squared*h+mDmu=-4A, subtraction gives
\[
\begin{aligned}
s&=-\chi t^2/2+\mu_0t+s_0,\\
k&=-2At^2+\alpha_1t+\alpha_0,\qquad
\chi,\mu_0,s_0,A,\alpha_1,\alpha_0\in F.
\end{aligned}
\tag{12}
\]
Let partial_m denote the coefficient partial at fixed t. The identity
k_m=m*s_m follows from k_s=m. Comparing powers of the transcendental t yields
\[
4A_m=m\chi_m,\qquad (\alpha_1)_m=m(\mu_0)_m,
\qquad (\alpha_0)_m=m(s_0)_m.
\tag{13}
\]
Since A is complex, chi_m=0. Together with Dchi=0 this proves
\(\chi\in\mathbb C\), including chi=0. No identification L'=F(t)
or F=C(m) was made.

Two more FULL coefficient equations will finish the proof.
The s derivative of q=0 gives h_t+mu*h_s+h*mu_s=0. Substitution
in the evaluated g, without dropping any lower function, gives
\[
[x^3]g=-\frac{h(2B+dm\mu_s)}m.
\tag{14}
\]
Consequently the x cubed coefficients of both equations (7) are
\[
\boxed{4DB+2dA_s=-\frac{\kappa h(2B+dm\mu_s)}m,}\qquad
\boxed{2Dd+d\mu_s+6B/m=\kappa hd/m.}
\tag{15}
\]
Both equalities include B=0 and every lower C,c,e coefficient.

## 3. The actual complex shears retain the full chart

The only ambient maps used below have arbitrary complex b,gamma:
\[
X^*=X,\quad Y^*=Y,\quad Z^*=Z,\quad W^*=W+bY+\gamma Z.
\tag{16}
\]
Their polynomial inverse subtracts bY*+gamma Z*. These are actual
members of the completely read filtered class
[426](general-coupling-normalization-obstruction-pass426-working.md), not shears with
coefficients from L'. Their literal transport is
\[
\begin{gathered}
t^*=t,\quad s^*=s+bt+\gamma t^2,\quad
\sigma^*=\sigma,\quad y^*=y,\quad k^*=k,\\
\theta^*=\theta+(b+2\gamma t)\sigma+\gamma k,\quad
m^*=m,\quad h^*=h,\quad n^*=n-\gamma mk,\\
\partial_{t^*}=\partial_t-(b+2\gamma t)\partial_s,
\quad\partial_{s^*}=\partial_s,\quad
\mu^*=\mu+b+2\gamma t,\quad D^*=D,\quad q^*=q,\\
A^*=A,\quad B^*=B,\quad d^*=d,\quad \chi^*=\chi-2\gamma.
\end{gathered}
\tag{17}
\]
Starred coefficient functions are pullbacks before their derivatives
are taken. In particular Phi*=Phi-2gamma*m verifies the last entry.

The original E, global slice, kernel and a0 do not change. The
weighted linear map is invertible and preserves the entire initial
kernel X squared Z-Y squared, which omits W. The exact time
profile is retained, with s*=s+bt+gamma*t squared. The literal
inverse partial is partial_Z*=partial_Z-gamma*partial_W.
The retained omitted-partial bound [u^4]partial_W restricted to
the actual kernel \(\mathcal A\) is zero. It therefore gives N*=N.
Thus L and the original v remain valid, as do x and rho.

The parameter and row determinants are both one, so the original
full scalar stays -a0^4. Finally
\(\mathcal B_{a_0}=\mathcal A_{a_0}[X]\),
and the actual coordinate prime X is a0-saturated by E-degree.
Evaluating the actual frame at X=0 preserves the strong complex
intercept return and the polynomial return, exactly as426 Section4.
Thus every264 hypothesis, and the newly derived genuine potentials
and multipliers, is retained. No special lower potential is assigned
independently of this actual map.

## 4. B=0 reduces to the affine-theta exclusion

In this branch A_s=DB=0. The first equation (15) and the nonzero
factors kappa,h,d imply mu_s=0. Thus Dmu=mu_t=-chi, and joint
constants give
\[
\mu=-\chi t+\mu_0,\qquad \mu_0\in\mathbb C.
\tag{18}
\]
Take b=-mu0 and gamma=chi/2 in (16). Then mu*=0 and
\[
\theta^*=d x+e+(\chi t-\mu_0)c+(\chi/2)k.
\tag{19}
\]
This is affine nonconstant intrinsically, with coefficient d nonzero,
while sigma* is quadratic. These degrees also hold in the original
L[v]: the actual expressions belong there and coefficient extension
does not change their degree. The coupling m*=m remains noncomplex.

The completely read variable-coupling exclusion in
[542](principal-paraboloid-quadratic-affine-recognition-synthesis-pass542-working.md),
Section2, now contradicts this profile. Only its conclusion that m
must be complex is used. The retained recognition473 endpoint of542
is not needed. Neither chi nor mu0 was divided out; their zero cases
are included. This excludes B=0, independently of which all-X
Laurent monomial was possible.

## 5. B nonzero gives an actual initial-independence obstruction

First take b=0 and gamma=chi/2 in (16) and drop stars. We now have
chi=0, A in C, B nonzero and all the same q=0 hypotheses. In
particular Dmu=0. Use K=C(X) and the ACTUAL polynomial three-ring
\[
R=K[Y,V,W],\qquad V=Z-\frac{Y^2}{(X+A)^2}.
\tag{20}
\]
The denominator X+A is a nonzero element of K even if A=0.
This is a triangular coordinate change over K, with inverse
Z=V+Y squared/(X+A) squared. No specialization at X=-A occurs.

The entire original rows (5),(6) give the exact x degrees
\[
(\deg_xY,\deg_xV,\deg_xW)=(2,3,3),\qquad
(Y_2,V_3,W_3)=\left(X+A,-\frac{2B}{X+A},-\frac{2B}{m}\right).
\tag{21}
\]
For W, q=0 makes its quartic coefficient -chi/2=0 and its cubic
coefficient -2B/m. For V, Z has quartic coefficient one and cubic
coefficient zero, whereas the cubic coefficient of Y squared is
2(X+A)B. Thus (21) retains every lower term and has no hidden
leading-degree cancellation.

Extend N to \(\mathcal B=\mathcal A[u]\) by Nu=0 and set
\[
\Delta=a_0N-(NX)E.
\tag{22}
\]
This is a polynomial derivation fixing X. In L'(X)[x] it is
a0*rho*partial_x, so it is locally nilpotent on R, with degree
filtration equal to x degree. It is nonzero by (21). The speed
a0*rho is retained, not made complex. A nonzero LND on this actual
three-ring has polynomial invariants of transcendence degree two:
choose a local slice, localize its nonzero invariant derivative,
and use the finite Taylor projection to obtain a polynomial slice
ring after localization. In particular it has a nonconstant
polynomial invariant. No global slice for Delta is assumed.

Suppose B and m were algebraically independent over C. They remain
so over K because X is transcendental over L'. For a new independent
eta, the three initial images in (21), multiplied respectively by
eta squared, eta cubed and eta cubed, would be algebraically
independent over K. Indeed their fraction field contains
m/(X+A) as the ratio of the last two. After an algebraic extension
it also contains eta, using the first image, and then B, using the
second. Its transcendence degree would therefore be three.

The corresponding polynomial initial map would be injective.
Every nonconstant polynomial in the actual independent coordinates
Y,V,W has positive source weight for weights (2,3,3). Its top
would survive under that injective map, giving positive x degree.
This contradicts a nonconstant polynomial Delta-invariant, whose
x degree is zero. Thus B and m are algebraically dependent.
Since m is noncomplex, it is transcendental over C; hence
\[
B\text{ is algebraic over }\mathbb C(m),\qquad DB=0.
\tag{23}
\]
The derivative conclusion follows by differentiating its separable
minimal polynomial, since Dm=0. Rationality of B is not asserted.
This argument works entirely with the finite overfield L': it
does not descend rho, B or d to the original L, and it does not
identify Frac(R) with L'(X)(x).

## 6. The two exact coefficients contradict the remaining branch

With A_s=DB=0, the first equation (15) now gives
\[
2B+md\mu_s=0,\qquad \mu_s\ne0.
\tag{24}
\]
The last nonvanishing follows from B,m,d nonzero. Because Dmu=0,
the moving-direction commutator must be retained:
\[
D(\mu_s)=(D\mu)_s-\mu_s^2=-\mu_s^2.
\tag{25}
\]
Apply D to (24), using DB=Dm=0. It follows that
Dd=d*mu_s. Substitute both this equality and
B=-md*mu_s/2 in the ENTIRE second equation (15). Its left side is
2d*mu_s+d*mu_s-3d*mu_s=0, but its right side is
kappa*h*d/m, which is nonzero. This is the final contradiction.

## 7. Verification and exact boundary

The full426 and542 were read through EOF for this proof. The actual
three-ring argument uses no classification of LNDs and no cofactor
bound. The separate noncomplex-A reflection argument is not part
of this note, and the all-X Laurent alternatives need not be
discarded: the proof exhausts B=0 and B nonzero directly.

Fresh unsaved97b625 reconstructed the full formal H, differentiated
before evaluation, and both complete multiplier polynomials.
Every coefficient in (10),(14),(15) had zero residual. Fresh
cf697c independently expanded every coefficient of B_beta+kappa*f.
Fresh29920c rebuilt the whole original W and the actual localized
V, verified all leaders in (21), and checked the terminal nonzero
factor. Fresh1877a4 verifies the complete transported Z and W rows,
the changed Phi and q, with zero residuals. These computations
retain arbitrary lower jets and only supplement the written
exact-field and actual-ring proofs.

The theorem is precisely exclusion of q=0, A in C under (1),(2)
with m noncomplex. It includes A=0, chi=0, mu0=0, and both B cases.
The d=0 case, q nonzero, and noncomplex A are not silently included.
No arbitrary sliced four-space is asserted to enter this chart.
No saved checker was executed, imported, compiled or rerun, and no
earlier source or canonical file was edited. A separate complete
saved-source audit is still required before acceptance.
