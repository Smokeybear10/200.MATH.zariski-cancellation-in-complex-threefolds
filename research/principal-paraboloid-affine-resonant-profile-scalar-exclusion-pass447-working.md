# Excluding the affine resonant quadric profile by the full scalar

Working result: retain the entire actual264 chart and the moving-slope
assumptions of438. In the resonance f'''=6nu', the normalized quadric
profile (deg p,deg x,deg q)=(1,1,1) is impossible. Both factors of the
relevant scalar coefficient are treated. One branch is excluded directly
by lower genuine-potential and scalar coefficients. The other requires
an actual polynomial return over the exact coefficient field before its
last scalar contradiction.

No coefficient-field transformation below is an original complex
coordinate change. This is only a profile exclusion, not a recognition
theorem for the remaining moving-slope profiles.

## 1. Full actual input and the affine parametrization

Retain every hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
[438](principal-paraboloid-moving-transverse-slope-fourth-potential-pass438-working.md)
and the quadric construction of
[441](principal-paraboloid-arbitrary-longitudinal-moving-slope-quadric-degrees-pass441-working.md).
In particular
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,
\quad a_0=EX\ne0,\quad X=a_0u+x_0,\quad x_0\in A,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\quad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the full initial kernel},\\
N=[u^4]\partial_Z|_A\ne0,\quad
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,
\quad Na_0=Nt=Ns=0,\\
Nv=1,\quad O=L[A]=L[v]=L[y,z,w]=L[y,\sigma,\theta],\\
K=\operatorname{Frac}A=L(v)=\mathbb C(y,z,w),\quad
\det\frac{\partial(Y,Z,W)}{\partial(t,s,v)}=-a_0^4\in L^*.
\end{gathered}
\tag{1}
\]
Put F=ker_L(partial_s). It is finite over C(t), not assumed rational.
The exact coefficient partials commute and have joint constants C.
Primes on F mean exact t-derivatives. Assume
\[
k=s+f,\quad n=\nu s+n_0,\quad f,\nu,n_0\in F,
\quad b=\nu'\ne0,\quad f'''=6b.
\tag{2}
\]
Use the entire genuine H,Q of438, including their moving levels h,q0
and both h_t,h_s. Their evaluated gradient minors generate O.

Suppose the normalized quadric of441 has profile (1,1,1). Its coordinate
p differs from sigma by an element of L. Thus P=sigma is an affine
intrinsic parameter and O=L[P]. Since the polynomial T2 of441 is monic
quadratic under(2), write the actual intercepts as
\[
y=aP+c,\qquad \theta=-P^2+B P+D,\qquad
A_1=f''-2\nu,\quad \lambda=a+A_1/2\ne0.
\tag{3}
\]
Initially a,c,B,D,lambda belong to L. Capital B in(3) is a coefficient,
not the ring mathcal B. Changing the coefficient partials to hold P fixed
changes the calibrated scalar to
\[
\mathcal J(X)=\det\frac{\partial(Y,Z,W)}{\partial(t,s,P)}
             =-\frac{a_0^4}{NP}\in L^*.
\tag{4}
\]
The triangular parameter Jacobian has determinant P_v=NP in L*.
All coefficient derivatives below hold P fixed. Positive X- or P-degree
coefficients of this determinant must vanish.

The complete literal rows are
\[
\begin{aligned}
Y&=y+PX+tX^2,\\
Z&=2ty+P^2+f'P+\theta+n+(2tP+s+f)X+t^2X^2,\\
W&=\ell-(2P+f')y-\frac{f''}{2}P^2-n_tP-\nu\theta
                         +\theta X+sX^2.
\end{aligned}
\tag{5}
\]
Actual E-stability and a0 in L* recover P=EY/a0-2tX, y=Y-PX-tX^2
and theta=EW/a0-2sX. Together with the whole return, this proves
\[
L[\mathcal B]=L[X,P].
\tag{6}
\]
Set M=f'+B. At the formal specialization X=-a, Y is constant in P
and the P coefficient of Z is M. If M=0, both are constant, whereas
the P^2 coefficient of W is -lambda, nonzero. They cannot generate L[P].
Thus M is nonzero. This is coefficient specialization, not an ambient map.

Put E0=ell_s+nu^2 and zeta=lambda/b. The centered function is
x=lambda P+c+(n_t-nu f')/2. In the normalized parameter p=P-E0/b,
\[
x=\lambda p+\rho,\qquad
\rho=c+\frac{n_t-\nu f'}2+\frac{\lambda}{b}E_0.
\tag{7}
\]
The quadric forces d=rho^2 and q=-lambda^2 p/b-2lambda rho/b.
If rho=0, its entire gradient vanishes at p=0, contradicting the
evaluated minor-unit ideal. Therefore rho is nonzero. This argument
does not assume d nonzero in advance.

## 2. The highest genuine-Q coefficients and T

Substitute(3) in the complete Q of438. Its highest coefficients are
\[
[P^4]Q=-\frac{b'+2\ell_{ss}}4,\qquad
[P^3]Q=\ell_{ts}+\frac{n_{ttt}}6-\frac{b(f''-2\nu)}2
\quad\text{after }[P^4]Q=0.
\tag{8}
\]
Since n_ttt=b''s+n0''', commuting partials applied to(8) give
-b''/2=-b''/6, hence b''=0. Exact integration yields
\[
\begin{gathered}
b'=\beta\in\mathbb C,\quad b=\beta t+b_0,\quad
\nu=\beta t^2/2+b_0t+\nu_0,\quad C=f''-6\nu\in\mathbb C,\\
\ell=-\beta s^2/4+L_1s+L_0,\quad
L_1=\nu^2+C\nu/2-n_0''/6+\ell_{10},\quad L_0\in F,\\
b_0,\nu_0,\ell_{10}\in\mathbb C.
\end{gathered}
\tag{9}
\]
These statements follow by subtracting the displayed primitives and
using the exact constant fields. In particular beta may be zero.

Define Ebar=L1+nu^2 in F and
\[
T=\frac{n_{tt}-\nu f''}{2}-\frac{(f''-2\nu)^2}{4}+E_0
 =\frac{n_0''}{3}-5\nu^2-2C\nu-\frac{C^2}{4}+\ell_{10}\in F.
\tag{10}
\]
The P^2 and P coefficients of H-h give
\[
B=-\frac{\lambda^2+T}{b},\qquad
D=\frac{-2\lambda c-(n_t-\nu f')a+\nu n_t+\ell_t+E_0B}{b}.
\tag{11}
\]
For reconstruction, the exact coefficient and level ledger is
\[
\begin{aligned}
&E_0=\bar E-\beta s/2,\quad L_1'=-(T'+bf'')/2,\quad
\bar E'=-(T'+b(f''-4\nu))/2,\\
&n_0''=2T+\nu f''+(f''-2\nu)^2/2-2\bar E,\quad
n_0'''=3(T'+2bf''-2b\nu),\\
&h=c^2+(n_t-\nu f')c+\nu\ell-E_0D.
\end{aligned}
\tag{12}
\]
In all lower-Q computations h_t,h_s are the actual derivatives of
the last expression, not independent levels set to zero.

## 3. The first full-scalar gates

Form the determinant of(5), using(9)--(12), while lambda and c may still
depend on t and s. Define the nonzero polynomial
\[
\mathcal F(Z)=-\beta Z^3+3b^2Z^2
 +(bT'-\beta T-b^2f'')Z-b^2T+b^3f'\in F[Z].
\tag{13}
\]
Direct expansion of the literal determinant gives
\[
[P^3]\mathcal J=-\frac{2\lambda_s}{b^2}\mathcal F(\lambda),
\qquad
[P^2]\mathcal J=-\frac{2c_s+2b-\lambda'}{b^2}\mathcal F(\lambda)
\quad\text{after }\lambda_s=0.
\tag{14}
\]
These are whole polynomials in X with no remaining X terms.
The Z^2 coefficient of(13) is 3b^2, even if beta=0. If lambda_s
were nonzero, (14) would make lambda algebraic over F. Differentiating
its separable minimal polynomial over F would then give lambda_s=0.
Consequently
\[
\lambda,a,B\in F,\qquad M=f'+B\in F^*.
\tag{15}
\]
Set zeta=lambda/b, nonzero. Then
\[
\zeta'=\frac{a'+2b-\beta\zeta}{b},\qquad
\mathcal F(\lambda)=b^3\{M-\zeta M'-2\zeta^2a'\}.
\tag{16}
\]
Both factors of the second equation in(14) are retained below.

## 4. The branch mathcal F(lambda) nonzero

Here c_s=a'/2, so c=a's/2+c0 with c0 in F. Complete genuine-Q expansion,
including both derivatives of h in(12), gives
\[
\begin{aligned}
[P^2s]Q&=\frac{b^2T''-2b\beta T'+2\beta^2T+2I^2}{4b^2},
\quad I=b^2-b\lambda'+\beta\lambda,\\
[Ps^2]Q&=-\frac{(2\beta-\lambda'')I}{2b}
\quad\text{after }[P^2s]Q=0.
\end{aligned}
\tag{17}
\]
Before the first substitution, the numerator for the second coefficient,
multiplied by -1/(4b^3), is
\[
\begin{aligned}
&-\beta(b^2T''-2b\beta T'+2\beta^2T)
+2b^4\beta-2b^4\lambda''+2b^3\lambda'\lambda''\\
&\hspace{8mm}-2b^2\beta\lambda\lambda''-2b^2\beta(\lambda')^2
+4b\beta^2\lambda\lambda'-2\beta^3\lambda^2.
\end{aligned}
\]
This provides a short direct check on the elimination in(17).

If I is nonzero, (17) gives lambda''=2beta. If I=0, differentiate
I to get I'=b(2beta-lambda'')=0 and the same result. Thus
\[
a''=0,\qquad a=a_1t+a_0^\flat,\qquad a_1,a_0^\flat\in\mathbb C.
\tag{18}
\]
Here a0-flat is not the actual speed a0 of(1). The first equation
of(17) is (T/b)''=-2I^2/b^3. Using T/b=-M+f'-b*zeta^2 and(16),
together with lambda''=2beta, gives
\[
M''=-4a'.
\tag{19}
\]
No division by I or beta occurs. The second equation of(11) now reads
\[
c=a's/2+c_0,\qquad D=(a-\nu+M'/2)s+K_0,\qquad c_0,K_0\in F.
\tag{20}
\]
For the determinant calculations one also has
\[
L_0'=bK_0+2b\zeta c_0+n_0'(a-\nu)-a\nu f'-\bar E(M-f').
\tag{21}
\]

Expand(5) using(18)--(21). The determinant has support only XP,P,X,1.
Its XP coefficient is
\[
-\frac b2\{2K_0'+MM'+4Ma+2Ma'\zeta-M'f'+2n_0'
 +4a^2\zeta-2af'-2a'f'\zeta+4c_0+4c_0'\zeta\}.
\tag{22}
\]
Its K0' coefficient is -b, so its zero equation eliminates K0'.
Write R1 for this exact substitution and put S0=Ma'+2a^2-a'f'+2c0'.
The remaining determinant ledger is
\[
\begin{aligned}
R_1([P]\mathcal J)&=-\frac b2(-M+\zeta M'+2a'\zeta^2)S_0,\\
R_1([X]\mathcal J)&=-\rho S_0,\\
R_1([1]\mathcal J)\big|_{S_0=0}&=0.
\end{aligned}
\tag{23}
\]
The last substitution solves uniquely for c0', whose coefficient in S0
is two. These are identities of the full literal rows. By(16), the first
factor in(23) is nonzero, so S0=0. Every determinant coefficient,
including the constant coefficient, vanishes, contradicting(4).

## 5. The branch mathcal F(lambda) zero

Here
\[
M-\zeta M'-2\zeta^2a'=0.
\tag{24}
\]
Do not impose a''=0. Equation(11) becomes
\[
D=-2\zeta c+(a-\nu+M/(2\zeta))s+d_0,\qquad d_0\in F.
\tag{25}
\]
Indeed, before(24), its coefficient of s is
B'/2-lambda+lambda*lambda'/b and its constant part is an F-combination
of L0',n0',Ebar,lambda,T,f',nu. Equations(16),(24) give(25).
At this stage c is still an arbitrary element of L.

For a reproducible literal determinant ledger, put v1=n0' and use
\[
\begin{gathered}
f''=2(b\zeta-a+\nu),\quad T=-b(M-f')-b^2\zeta^2,\quad
\bar E'=-(T'+b(f''-4\nu))/2,\\
n_0''=2T+\nu f''+(f''-2\nu)^2/2-2\bar E,\\
L_0'=bd_0+v_1(a-\nu)-a\nu f'-\bar E(M-f'),\quad
M'=M/\zeta-2\zeta a'.
\end{gathered}
\tag{26}
\]
The determinant again has support XP,P,X,1. Its XP coefficient is
\[
\begin{aligned}
C_{11}={1\over2\zeta^2}\{&
-4\bar E a'\zeta^3+8\bar E c_s\zeta^3-M^2b\zeta-4Mab\zeta^2\\
&+Ma's+Mbf'\zeta+Mbs-M\beta s\zeta
-2v_1a'\zeta^2-2v_1b\zeta^2+4v_1c_s\zeta^2\\
&-4a^2b\zeta^3+2abf'\zeta^2-2a'bs\zeta^2
+2a'\beta s\zeta^3+2a'f'\nu\zeta^2\\
&+4bc\zeta^2+4bc_s s\zeta^2-2bd_0'\zeta^2
-4\beta c\zeta^3-4\beta c_s s\zeta^3\\
&+8cc_s\zeta^2-4c_sf'\nu\zeta^2\}.
\end{aligned}
\tag{27}
\]
Its d0' coefficient is -b. Let R1 now mean the forced substitution
d0'=C11|_(d0'=0)/b. Define
\[
\begin{aligned}
V_0&=-2\rho=-2\bar E\zeta-v_1-bs+\beta s\zeta-2c+\nu f',\\
K_1&=(2c_s-a')(2\bar E-\beta s)+2bc_s(f'-M)-2ba^2-2bc_t.
\end{aligned}
\tag{28}
\]
The exact remaining identities are
\[
\begin{aligned}
R_1([P]\mathcal J)&=-\frac{\rho}{\zeta}(M+4\zeta^2c_s)(a'-2c_s),\\
R_1([X]\mathcal J)&=\frac{\rho}{b}K_1,\\
R_1([1]\mathcal J)\big|_{K_1=0}
 &=\frac{(a'-2c_s)\rho}{b\zeta}
       \{E_0(M+4\zeta^2c_s)-4c_s\zeta\rho\}.
\end{aligned}
\tag{29}
\]
The substitution K1=0 solves uniquely for c_t, with coefficient -2b.
Since rho is nonzero, no scalar equation is lost in imposing it.

The first equation in(29) gives c_s=a'/2 or c_s=-M/(4zeta^2).
The first choice makes the last coefficient zero, contradicting(4).
The remaining possibility is
\[
c_s=-\frac{M}{4\zeta^2}\in F,\quad
c=-\frac{M}{4\zeta^2}s+c_0,\quad c_0\in F,\qquad
\mathcal J=\frac{M(M+2a'\zeta^2)}{2b\zeta^4}\rho^2\ne0.
\tag{30}
\]
In particular M+2a'zeta^2 is nonzero, by the full nonzero scalar.
It was not divided out earlier.

## 6. Actual polynomial return and the exact speeds

At this point every intercept y,z,w is polynomial in s,P over F,
by(3),(5),(9),(25),(30). The strong return K=C(y,z,w) and the inclusions
F,s,P contained in K therefore give
\[
K=F(s,P).
\tag{31}
\]
The field L is algebraic over F(s) and is contained in this rational
one-variable extension. Since F(s) is relatively algebraically closed
in F(s)(P), one has L=F(s). This does not assert F=C(t).

Put mathcal T=F[X,s,P] and mathcal B_F=F[mathcal B]. The literal rows give
mathcal B_F contained in mathcal T. Since a0 belongs both to mathcal B_F
and L=F(s), polynomial intersection gives a0 in F[s]. The ORIGINAL
polynomial slice u belongs to mathcal B and hence to mathcal T; no claim
that X/a0 is this slice or belongs to mathcal B is made. The derivation
E kills F,s,P and has EX=a0, so its restriction to mathcal T is
a0(s)*partial_X. Thus Eu=1 gives a0(s)*u_X=1 in F[X,s,P]. The units of
this polynomial ring are F*, so a0 belongs to F*. This uses the original
slice, with X=a0*u+x0 and x0 in A, without assuming x0=0.

E kills F and preserves mathcal B_F. Actual derivatives recover
\[
P=EY/a_0-2tX\in\mathcal B_F,\qquad
s=E^2W/(2a_0^2)\in\mathcal B_F.
\tag{32}
\]
Consequently
\[
\mathcal B_F=F[X,s,P],\qquad F[A]=F[s,P],\qquad a_0\in F^*.
\tag{33}
\]
For the second equality, the actual slice gives F[mathcal B]=F[A][u];
taking E-invariants of this polynomial extension gives exactly F[A].
No assertion that s or P is an original complex coordinate is made.

N kills F and preserves F[A]. Since P is affine in the original
intrinsic v, NP belongs to L* and F[s,P], hence to F[s].
The determinant of the literal polynomial rows belongs to F[s,P,X],
and by(4) it belongs to L, hence to F[s]. Calibration now gives
\[
(NP)\mathcal J=-a_0^4\in F^*.
\tag{34}
\]
Units of F[s] are F*, so NP and mathcal J belong to F*. The prefactor
of rho^2 in(30) is a nonzero element of F. Also rho is affine in s over
F by(7),(30). Thus rho belongs to F*, and in particular rho_s=0.

## 7. Final contradiction without dividing beta

Equations(7),(30) turn rho_s=0 into
\[
M=2\zeta^2(b-\beta\zeta).
\tag{35}
\]
M is nonzero, so b-beta*zeta is nonzero. Differentiating(35), using
beta'=0 and(16), gives the exact identity
\[
M-\zeta M'-2\zeta^2a'
 =6\zeta^2(b-\beta\zeta)(1-\zeta').
\tag{36}
\]
Equation(24) forces zeta'=1. The first equation of(16) then gives
a'=beta*zeta-b. Together with(35), this makes M+2a'zeta^2 zero,
contrary to(30). The second branch is excluded as well.

The case beta=0, both I alternatives, both factors in(14), and both
factors in(29) have been retained. There is no rationality assumption
on the finite exact field F and no coefficient-field coordinate promotion.

## 8. Verification and scope

The complete438 and441 sources and the writing guide were read before
this writeup. Fresh unsaved f3dfce, terminal f156dd, rebuilt the full
literal determinant with lambda_s retained and verified both identities
(14). Fresh c0d016, terminal0a2cef, rebuilt the complete Q with both
derivatives of the actual level in(12), giving(17);796546 verified the
short elimination. Fresh99f857 rebuilt all four determinant coefficients
in the first branch, including its zero constant coefficient.

Fresh8645c3, terminal060320, rebuilt the second literal determinant.
Freshcc0649, terminal0f6b67, and7fa87b, terminal6fb81b, verified
(27)--(30) with c_t,c_s independent. Fresh0e3f49 verified the conversion
to(19), differential identity(36), and the final zero scalar factor.
The field intersections, actual slice, polynomial return and unit
arguments are the written algebraic arguments above, not consequences
of symbolic sampling.

No saved checker was executed, imported, compiled or rerun. No earlier
proof or canonical index was edited. This note excludes only the
resonant affine normalized-quadric profile under the entire supplied
actual264 hypotheses. It makes no arbitrary-entry, unrestricted
cancellation, actual-existence, novelty or formal-certification claim.
