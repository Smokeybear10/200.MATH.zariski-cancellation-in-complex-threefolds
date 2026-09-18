# The constant Laurent branch is excluded after reflection rigidity

Working bounded exclusion: retain the FULL actual264/296/535 chart
and the noncomplex-leading-coefficient necessary family547. After
the actual normalization proved below, the branch B=nu0=0 is
impossible. In particular the constant Laurent alternative cannot
occur. The proof uses the entire scalar of the actual X=0 fiber,
not only point separation or a formal intrinsic change of variables.

This note also proves two shared necessary facts before specializing
that branch: the quadratic coefficient of U=Y squared+alpha W is
D-constant, and Dd is nonzero whenever B=0. No exclusion of the
other two Laurent alternatives is claimed here.

## 1. Full input and the required necessary family

Retain every actual hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md)
and [535](principal-paraboloid-nonlinear-sigma-unit-multiplier-pass535-working.md).
In particular, use the original global-slice equality
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=\mathcal A[u],\quad E=\partial_u,
\quad X=a_0u+x_0,\quad a_0\ne0,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\quad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the entire initial kernel},\\
0\ne N=[u^4]\partial_Z|_{\mathcal A},\quad
Na_0=Nt=Ns=0,\quad Nv=1,\\
L=\operatorname{Frac}\ker_{\mathcal A}N,\quad
[L:\mathbb C(t,s)]<\infty,\quad L[\mathcal A]=L[v],\\
\operatorname{Frac}\mathcal A=L(v)=\mathbb C(y,z_{\rm int},w),\quad
L[y,z_{\rm int},w]=L[v],\quad J_{t,s,v}(X)=-a_0^4.
\end{gathered}
\tag{1}
\]
The intercept z_int is literal. Both returns, the selected original
partial and the full genuine levels remain required.

The complete source
[547](principal-paraboloid-equal-quadratic-zero-characteristic-reflection-rigidity-pass547-working.md)
has been read through EOF. Its finite intrinsic normalization is
\[
\sigma=x^2+c,\quad \theta=\mu x^2+d x+e,\quad
y=A x^2+B x+C,\qquad d\ne0,
\tag{2}
\]
where x=rho*(v-v0), rho squared belongs to L*, and the coefficients
may be considered in L'=L(rho). A and mu belong to original L.
Coefficient partials fix x. The exact covariance is
\[
Nx=\rho,\qquad J_{t,s,x}=-a_0^4/\rho,
\qquad\kappa=\kappa_v/\rho^2\in(L')^*.
\tag{3}
\]
No root is promoted to an ambient coordinate or presumed to descend.

Write p=m_t, h=m_s and D=partial_t+mu*partial_s. The current
branch has noncomplex m=k_s and q=p+h*mu=0. Hence h is nonzero.
The full high identities of547 give
\[
Dm=DA=D\chi=0,\quad D\mu=-\chi,\quad
\chi=\frac{4A+\Phi}{m},\quad
\Phi=k_{tt}+2p\mu+h\mu^2.
\tag{4}
\]
For the noncomplex-A branch, its necessary reflection conclusion is
\[
A=\frac\alpha m+\beta,\qquad
\chi=\frac{2\alpha}{m^2}+\delta,
\quad\alpha\in\mathbb C^*,\quad\beta,\delta\in\mathbb C.
\tag{5}
\]
This input is only a necessary family, not a realization assertion.

## 2. Actual normalization of the two additive constants

First use the ACTUAL complex translation
X1=X+beta, leaving Y,Z,W unchanged. Direct expansion gives
\[
\begin{aligned}
\sigma_1&=\sigma-2\beta t,&\theta_1&=\theta-2\beta s,\\
y_1&=y-\beta\sigma+\beta^2t,&k_1^{\rm pot}&=k+2\beta t^2,\\
n_1&=n-\beta k+2\beta t k_t+3\beta^2t^2+2\beta sm,&
w_1&=w-\beta\theta+\beta^2s.
\end{aligned}
\tag{6}
\]
The superscript on k1 distinguishes the new potential from k_t.
The functions t,s,m,h,q do not change. The quadratic y coefficient
becomes A-beta, whereas chi is unchanged. The intrinsic x, rho,
linear coefficient B and residual d are unchanged.

Next replace W1 by W1+(delta/2)Z1, leaving X1,Y1,Z1 fixed.
For this shear, in the current notation,
\[
\begin{gathered}
t^*=t,\quad s^*=s+\delta t^2/2,\quad k^*=k,\quad
\theta^*=\theta+\delta t\sigma+(\delta/2)k,\\
\partial_{t^*}=\partial_t-\delta t\partial_s,\quad
\partial_{s^*}=\partial_s,\quad
\mu^*=\mu+\delta t,\quad D^*=D,\quad q^*=q,\\
m^*=m,\quad h^*=h,\quad A^*=A,\quad B^*=B,\quad d^*=d,
\quad\chi^*=\chi-\delta.
\end{gathered}
\tag{7}
\]
In particular Phi*=Phi-delta*m. Both beta and delta may vanish;
no division by either is used. After these two actual maps, drop
subscripts and stars. We have
\[
\boxed{A=\alpha/m,\qquad\chi=2\alpha/m^2,\qquad\Phi=-2A.}
\tag{8}
\]

These are members of the fully read actual filtered class
[426](general-coupling-normalization-obstruction-pass426-working.md).
Their complex polynomial inverses subtract the translation and
the indicated multiple of Z. They retain the original E, global
slice and kernel. Their leading weighted maps preserve the entire
paraboloid initial kernel and exact time profile. The translation
fixes the literal selected Z partial. The shear changes it to
partial_Z-(delta/2)partial_W; the retained omitted-partial bound
[u^4]partial_W restricted to the original kernel is zero. Thus
N,L,v and a0 stay unchanged. The parameter and row determinants
are one, so the full scalar in the original v basis remains -a0^4.
The actual localized X1 fiber argument of426 preserves both returns.
No potentials were independently reassigned. Their new values are
the genuine potentials of this actual frame.

In (8), (t,m) is a separating coefficient basis because m_s=h is
nonzero. Its t derivative is D. Use a dot for D and a prime for
partial_m at fixed t. The constant field F0=ker_D L' is finite
over C(m), not assumed rational. In this basis the full scalar is
\[
J_{t,m,x}(X)=-a_0^4/(h\rho)\in(L')^*.
\tag{9}
\]
In particular it is independent of x, not necessarily complex.

## 3. The actual zero fiber and its entire degree-two row

The polynomial identity
\(\mathcal B_{a_0}=\mathcal A_{a_0}[X]\) holds in the new actual
frame. The coordinate prime X does not divide a0, since E-degree
would otherwise give deg_E a0 at least one. Therefore
\[
\mathcal B/(X)=\mathbb C[Y,Z,W]\hookrightarrow\mathcal A_{a_0},
\qquad (\mathcal B/(X))_{a_0}\simeq\mathcal A_{a_0}.
\tag{10}
\]
The contraction is exact because (X) is prime and a0 is not in it.
Thus the actual fiber fraction field is \(\operatorname{Frac}\mathcal A\), and the literal
intercepts below really are independent polynomial coordinates of
an actual three-ring. No coefficient-field root was substituted
for an actual coordinate in forming this fiber.

The complete second potential, still before specialization, is
\[
mw=\ell-(2\sigma+k_t)y-k_{tt}\sigma^2/2-p\sigma\theta
 -h\theta^2/2-n_t\sigma-n_s\theta.
\tag{11}
\]
Put
\[
H_0=hd^2/2+Dn,\quad r=C-Ac,\quad
\nu_0=\{h(e-\mu c)+n_s\}/m,\quad \overline C=2r+H_0.
\tag{12}
\]
Here H0 is merely this coefficient, not the formal fourth potential.
The all-X Laurent alternatives in this normalized family are the
nonzero monomials of B*u+Cbar+md*nu0/u. The constant one has
B=nu0=0 and Cbar nonzero. We will in fact exclude B=nu0=0 without
needing that additional nonvanishing of Cbar.

At actual X=0, expand the ENTIRE rows and set U=Y squared+alpha W.
This is an actual polynomial coordinate change of the three-ring,
with inverse W=(U-Y squared)/alpha. Write k1=k_t in the following
coefficient formulas. They are
\[
\begin{aligned}
Y&=Ax^2+Bx+C,\\
Z&=x^4+z_2x^2+z_1x+z_0,\\
z_2&=2tA+2c+k_1+m\mu,&z_1&=2tB+md,\\
z_0&=2tC+c^2+k_1c+me+n,\\
W&=-\alpha x^4/m^2-2Bx^3/m+w_2x^2+w_1x+w_0,\\
w_2&=-\{2C+Ak_1+hd^2/2+Dn\}/m,\\
w_1&=-(2c+k_1)B/m-d\nu_0,\\
w_0&=\{\ell-(2c+k_1)C-k_{tt}c^2/2-pce-he^2/2-n_tc-n_se\}/m.
\end{aligned}
\tag{13}
\]
No constant or linear term of W is omitted. Its quartic and cubic
terms cancel those of Y squared in U. Therefore
\[
\begin{aligned}
U&=Tx^2+U_1x+U_0,\\
T&=B^2-A^2k_1-AH_0,\\
U_1&=B(2r-Ak_1)-\alpha d\nu_0,\qquad U_0=C^2+\alpha w_0.
\end{aligned}
\tag{14}
\]
The scalar for the actual rows Y,Z,U is alpha times (9):
\[
\det\frac{\partial(Y,Z,U)}{\partial(t,m,x)}
       =-\alpha a_0^4/(h\rho)\in(L')^*.
\tag{15}
\]

We next prove the shared necessary gate DT=0, including T=0.
Extend N to the original \(\mathcal A[u]\) by Nu=0 and put
Delta=a0*N-(NX)E. This polynomial LND fixes X and descends to
the actual fiber (10). In its coefficient-field embedding it is
a0*rho*partial_x. It is nonzero, because the quadratic coefficient
A of Y is nonzero. Local nilpotence follows from this polynomial
overring and the invariant speed. A local slice shows that its
actual fiber kernel has transcendence degree two, so it contains a
nonconstant polynomial invariant. No global slice for Delta is used.

If T is nonzero and algebraically independent of m over C, the
three initial images
\[
A\eta^2,\quad\eta^4,\quad T\eta^2
\tag{16}
\]
are algebraically independent over C. Their fraction field, after
an algebraic extension, contains m by the ratio of the second to
the square of the first, then eta and T. Thus it has transcendence
degree three. Injectivity of the positive-weight initial map for
weights (2,4,2) would make every nonconstant actual polynomial in
Y,Z,U have positive x degree. This contradicts the invariant just
obtained. Consequently T is algebraic over C(m) and DT=0. If T=0,
the same derivative conclusion is immediate. In all cases,
\[
F:=T/A\in F_0,\qquad
U=FY+L_1x+R,
\quad L_1=B(\overline C-B^2/A)-\alpha d\nu_0,
\quad R=U_0-FC.
\tag{17}
\]
The symbol F here is not the second-potential polynomial of296.
These are exact expressions in the existing finite coefficient
field. In particular rationality of F is not asserted.

## 4. Whenever B=0, the residual slope has nonzero D derivative

This section assumes B=0 but does NOT yet assume nu0=0. The following
identities are coefficients of the full535 polynomials, independently
of whether A is complex. They were reconstructed with arbitrary A
and A_s in the fresh calculation97b625 accompanying
[546](principal-paraboloid-equal-quadratic-zero-characteristic-constant-intercept-exclusion-pass546-working.md):
\[
4DB+2dA_s=-\frac{\kappa h(2B+dm\mu_s)}m,
\qquad 2Dd+d\mu_s+6B/m=\kappa hd/m.
\tag{18}
\]
These are coefficients of the whole polynomials, not assigned
equations after suppressing their lower terms. Since A=alpha/m,
the first equation for B=0 gives
\[
\kappa\mu_s=2\alpha/m^2=\chi\ne0.
\tag{19}
\]
Suppose Dd=0. The second equation then gives mu_s=kappa*h/m.
Using mu_s=h*mu' and s'=1/h, these two identities imply
\[
(\mu')^2=(\chi/m)s'.
\tag{20}
\]
But the exact integrations from547 after the actual normalization are
\[
\mu=-2\alpha t/m^2+\mu_0,
\quad s=-\alpha t^2/m^2+\mu_0t+s_0,
\quad\mu_0,s_0\in F_0.
\tag{21}
\]
Therefore mu'=4alpha*t/m cubed+mu0' and
s'=2alpha*t squared/m cubed+mu0'*t+s0'. The t-squared coefficients
of the two sides of (20) are respectively 16alpha squared/m to
the sixth and 4alpha squared/m to the sixth. Their difference is
nonzero. Comparing them is legitimate because t is transcendental
over F0. This contradiction proves
\[
\boxed{Dd\ne0\quad\text{whenever }B=0.}
\tag{22}
\]
No comparison presumes L'=F0(t), and no root in d has been removed.

## 5. The constant Laurent branch contradicts the complete scalar

Now impose B=nu0=0. Equation (17) has L1=0, so the ENTIRE fiber
rows have the form
\[
Y=Ax^2+C,\quad Z=x^4+z_2x^2+mdx+z_0,\quad U=FY+R,
\qquad DF=0.
\tag{23}
\]
The nonzero linear term mdx is retained. Dots and primes below are
the exact commuting partials in (t,m). Subtract F times the Y
differential row from the U row. The full matrix is
\[
\begin{pmatrix}
\dot C&A'x^2+C'&2Ax\\
\dot z_2x^2+m\dot d x+\dot z_0&z_2'x^2+(md)'x+z_0'&4x^3+2z_2x+md\\
\dot R&YF'+R'&0
\end{pmatrix}.
\tag{24}
\]
Its determinant is still the coefficient-field unit (15).
The following coefficients of that ENTIRE determinant suffice:
\[
\begin{aligned}
[x^4]J&=2A^2m\dot d F',\\
[x^5]J\big|_{F'=0}&=4A'\dot R,\\
[x^2]J\big|_{F'=\dot R=0}&=2Am\dot d R'.
\end{aligned}
\tag{25}
\]
They are read in this order. The first forces F'=0 by (22) and
A,m nonzero. The second forces dot R=0 because A'=-alpha/m squared
is nonzero. The third forces R'=0, again by (22). The entire last
row of (24) is then zero. Its determinant vanishes, contradicting
(15). This proves the claimed branch exclusion.

No constant scalar coefficient was set to zero. The argument only
uses positive x coefficients and then the entire determinant. It
retains every lower z2,z0,C,R function and every one of their jets.
It also covers F=0 or R constant, rather than dividing by either.

## 6. Verification and limits

The full547 input was read through EOF before authoring; the full
actual426 transport and the constant-A source546 were also read.
Fresh383d5b starts from the COMPLETE second potential and verifies
all U coefficients, the residual linear coefficient in (17), the
three scalar gates (25), and the nonzero difference in (20).
Fresh a9ca94 verifies every full translated row in (6); the full
shear and its derivative transport were checked in fresh1877a4.
Root's independent aa5807 and634ad5 reproduce the same full fiber
scalar coefficients with arbitrary lower jets. These computations
supplement the actual-fiber, exact-field and invariant arguments.

The conclusion concerns only the necessary family547 after its
licensed actual normalization, with B=nu0=0. The shared results
DT=0 and (22) do not themselves exclude either remaining Laurent
alternative. No all-q-zero closure, original-square descent,
ambient root change or arbitrary chart entry is asserted. Earlier
recognition ancestors are not recursively recertified.

No saved checker was executed, imported, compiled or rerun. No
earlier source or canonical record was edited. The source requires
separate complete saved-source review before acceptance.
