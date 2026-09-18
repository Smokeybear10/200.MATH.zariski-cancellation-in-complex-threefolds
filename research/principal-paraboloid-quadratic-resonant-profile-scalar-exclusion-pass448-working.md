# Excluding the quadratic equal-degree resonance profile by the original scalar

Working exclusion: under the full actual264 moving-slope chart, the
resonant quadric profile (deg p,deg x,deg q)=(2,2,2) cannot occur.
The quadratic relation space and the genuine fourth coefficients
first force a complex shift j. Specializing the ORIGINAL calibrated
scalar at X=-j then gives incompatible coefficient equations.

The proof uses the actual scalar, not a classification of formal
coefficient families. It does not assume that the coefficient field
is rational, promote a field-valued shear to an ambient coordinate,
or claim recognition of another surviving profile.

## 1. Entire actual input and the exact profile

Retain EVERY hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md) and the
moving-slope assumptions of
[438](principal-paraboloid-moving-transverse-slope-fourth-potential-pass438-working.md):
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad
a_0=EX\ne0,\quad \deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the entire weighted initial kernel},\\
N=[u^4]\partial_Z|_A\ne0,\quad
L=\operatorname{Frac}\ker_A N,\quad
[L:\mathbb C(t,s)]<\infty,\quad Na_0=Nt=Ns=0,\\
Nv=1,\quad O=L[v]=L[y,z,w]=L[y,\sigma,\theta],\quad
\operatorname{Frac}A=L(v)=\mathbb C(y,z,w),\\
F=\ker_L\partial_s,\quad
k=s+f,\quad n=\nu s+n_0,\quad
f,\nu,n_0\in F,\quad b=\nu'\ne0.
\end{gathered}
\tag{1}
\]
The exact coefficient partials commute and have joint constants C.
F is finite over C(t), but is not assumed to equal C(t).
Primes on its elements are exact t-derivatives.

Use the polynomial quadric transformation of
[441](principal-paraboloid-arbitrary-longitudinal-moving-slope-quadric-degrees-pass441-working.md).
It gives actual elements x,p,q of O, satisfying
\[
\mathcal H=x^2+bpq-d=0,\qquad O=L[x,p,q],\qquad d\in L.
\tag{2}
\]
Add the resonance and the specific degree profile
\[
f'''=6b,\qquad
(\deg_vp,\deg_vx,\deg_vq)=(2,2,2).
\tag{3}
\]
All degrees in this note refer to the original generic-line
polynomial variable v, until an affine replacement is explicitly
introduced.

The transformed genuine fourth level is441(10), not an arbitrary
quadric chosen to contain the curve. By441 and
[442](principal-paraboloid-moving-slope-resonance-degree-profiles-pass442-working.md),
its full support under the resonance is
\[
\begin{aligned}
\Phi={}&b xq+u_1px+\delta p^4+\kappa p^3+\epsilon p^2q+F_2q^2\\
&+c_{20}p^2+c_{11}pq+c_{10}p+c_{01}q+c_{00},
\end{aligned}
\tag{4}
\]
where
\[
\delta=-(b'+2\ell_{ss})/4,\qquad
\epsilon=-2\delta,\qquad F_2=-\ell_{ss}/2.
\tag{5}
\]
There are no x^2 or constant-times-x terms in (4).
The two evaluated gradients of Hcal and Phi have two-by-two
minors generating O. These are consequences of the actual scalar
and the polynomial intrinsic transformation, not assumptions about
normality of a projection.

In the profile(3), p^4 is uniquely highest until delta=0.
This also gives epsilon=0. Then p^3 is uniquely highest until
kappa=0. Therefore the FULL Phi is quadratic and
\[
\delta=\epsilon=\kappa=0,\qquad
\ell_{ss}=-b'/2,\qquad F_2=b'/4.
\tag{6}
\]

## 2. The quadratic relation space, with its unit cofactor

Put
\[
\lambda=\frac{[v^2]x}{[v^2]p}\in L^*,\qquad
v_1=x-\lambda p,\qquad
q_1=q+\frac{2\lambda}{b}x-\frac{\lambda^2}{b}p.
\tag{7}
\]
The leading quadric coefficient makes both v1 and q1 have degree
at most one, and
\[
v_1^2+bpq_1=d,\qquad O=L[v_1,p,q_1].
\]
If q1=0, then v1 is constant and O=L[p], impossible because
deg p=2. If v1 is constant and q1 nonzero, then p*q1 would be
constant, also impossible. Thus v1 is affine nonconstant, and
the degree equation forces
\[
q_1=q_c\in L^*,\qquad
p=\frac{d-v_1^2}{bq_c},\qquad
O=L[v_1].
\tag{8}
\]
No square root of d is used, and d=0 is retained.

In the formal polynomial ring L[x,p,q], define
\[
G=q+\frac{2\lambda}{b}x-\frac{\lambda^2}{b}p-q_c.
\tag{9}
\]
The complete evaluated curve ideal is (Hcal,G). Indeed the
invertible affine variables (v1,p,G) make Hcal equal
v1^2+bp(G+qc)-d. Quotienting by G and Hcal solves p linearly,
with nonzero coefficient b*qc, and leaves the polynomial ring
L[v1]. This verifies the whole ideal without localization or
saturation.

Every quadratic polynomial in this ideal has the form
\[
\Phi=A_0\mathcal H+G L_1,
\tag{10}
\]
where A0 lies in L and L1 is affine linear. To see this directly,
set G=0. A polynomial of total degree at most two in v1,p,
vanishing at p=(d-v1^2)/(b*qc), is a scalar multiple of
v1^2+b*qc*p-d. Subtract that scalar multiple of Hcal; the
remaining quadratic is divisible by the linear G.

Upon evaluation, the gradient wedge of Hcal and Phi is L1_ev
times that of Hcal and G. The unit minor ideal therefore forces
L1_ev in L*. Write this value as zeta_c. Since the only affine
linear polynomials vanishing on this parabola are multiples of G,
\[
L_1=\gamma G+\zeta_c,\qquad \zeta_c\in L^*,\qquad
\Phi=A_0\mathcal H+\gamma G^2+\zeta_c G.
\tag{11}
\]
This is where the genuine full minor condition enters. Mere
quadratic vanishing would not force a constant evaluated cofactor.

Compare the xq,x^2,x coefficients in (4),(11). Since b and
lambda are nonzero, they give respectively
\[
\gamma=\frac{b^2}{4\lambda},\qquad
A_0=-\lambda,\qquad
\zeta_c=2\gamma q_c.
\tag{12}
\]
The complete coefficient comparison, including the constant level, is
\[
\begin{gathered}
u_1=-\lambda^2,\qquad F_2=\gamma,\qquad
c_{20}=\lambda^3/4,\qquad c_{11}=-3b\lambda/2,\\
c_{10}=c_{01}=0,\qquad
c_{00}=\lambda d-\gamma q_c^2 .
\end{gathered}
\tag{13}
\]
In particular the d term has not been dropped.

## 3. Genuine coefficient identities force exact constants

Equations(6),(12),(13) imply
\[
b'\ne0,\qquad \lambda=\frac{b^2}{b'}\in F.
\tag{14}
\]
For completeness, the exact lower coefficient identities needed
next can be reconstructed from the full Q of438, including its
moving levels. Put
\[
g=f',\qquad h_c=f''/2,\qquad
\chi=h_c-\nu,\qquad E_0=\ell_s+\nu^2,\qquad
a=n_t,\qquad c=n_{tt}.
\]
The quotient T2 in441 has the form P^2+t1*P+t0. Comparing its
P^2 coefficient and using the x coefficient of Phi gives
\[
t_1=\frac{c/2-\nu h_c-\chi^2+E_0}{b},\qquad
u_1=b(t_1-g)=c/2-\chi h_c+\ell_s-bg .
\tag{15}
\]
The genuine pq coefficient is
\[
c_{11}=-bf''-\ell_{ts}-\frac{b'}2t_1.
\tag{16}
\]
One can read (16) without expanding all lower levels. Differentiate
Q-f''(H-h)/2 with respect to the formal V, use438(8), and substitute
\[
U=x-\chi P-(a-\nu g)/2,\qquad
V=q-P^2-t_1P-t_0,\qquad \ell_{ss}=-b'/2.
\]
Its P^2 terms cancel, and its P coefficient is precisely (16).
The final translation P=p+E0/b leaves that pq coefficient unchanged.

From (13),(15), t1=g-lambda^2/b belongs to F. Equation(16) and
c11=-3b*lambda/2 therefore show ell_ts belongs to F. Taking its
s derivative and using (6) proves
\[
b''=0,\qquad \beta:=b'\in\mathbb C^*,\qquad
\lambda=b^2/\beta,\qquad \lambda_t=2b.
\tag{17}
\]
The complex-constant assertion uses the exact joint constant field:
beta is in F and its t derivative is zero. There is no rational
function ansatz or assumed integration into C[t].

Resonance gives chi_t=f'''/2-b=2b. Consequently
\[
j:=\lambda-\chi\in\mathbb C,\qquad
r:=\frac{2\lambda}{b}=\frac{2b}{\beta},\qquad
r_t=2,\qquad r_0:=2t-r\in\mathbb C.
\tag{18}
\]
Both j and r0 have zero s derivative as well as zero t derivative.

## 4. Exact intercepts and the second complex constant

Write P=sigma. By(8) and the inverse441 transformation,
\[
P=A v_1^2+C,\qquad
A=-\frac1{bq_c}\ne0,\qquad
C=\frac{E_0}{b}+\frac{d}{bq_c}\in L.
\tag{19}
\]
The original intercepts have the form
\[
\begin{aligned}
y&=jP+v_1+\eta,&
\eta&=-\frac{rE_0+a-\nu g}{2},\\
\theta&=-P^2-gP-rv_1-T,&
T&=t_0-q_c-\lambda^2E_0/b^2\in L.
\end{aligned}
\tag{20}
\]
These identities follow from x=v1+lambda*p and
q=qc-2lambda*v1/b-lambda^2*p/b; all coefficient-field shifts
are retained.

The remaining derivatives needed for the specialization are also
forced, rather than chosen. First E0_s=-beta/2 by(6).
Equations(13),(15) give
\[
\ell_s=bg-c/2+\chi h_c-\lambda^2.
\]
Using t1=g-lambda^2/b in(16), with (17), gives
\[
\ell_{ts}=2b(j-\nu)-\beta g/2,\qquad
(E_0)_t=2bj-\beta g/2.
\tag{21}
\]
It follows directly from(20) that eta_s=0. For its t derivative,
differentiate rE0+a-nu*g, using r_t=2, g_t=2h_c, a_t=c.
Substitute (21) and the displayed ell_s identity. The result is
\[
(rE_0+a-\nu g)_t
=2\chi^2-2\lambda^2+4\lambda j=2j^2.
\]
Thus
\[
\boxed{\eta_t=-j^2,\qquad \eta_s=0,\qquad
\eta_0:=\eta+j^2t\in\mathbb C.}
\tag{22}
\]
No division by eta, j, d or a derivative of either is used.
In particular all zero values of these quantities remain covered.

## 5. A licensed specialization of the ORIGINAL scalar

Since v1 is affine in the original v over L,
rho=Nv1 belongs to L*. The original calibration becomes
\[
J(X)=\det\frac{\partial(Y,Z,W)}{\partial(t,s,v_1)}
=-a_0^4/\rho\in L^*.
\tag{23}
\]
Coefficient derivatives now fix v1 and X. The parameter change
has full chain determinant rho; its moving t,s coefficients do
not alter (23).

Crucially, j in(18) is a COMPLEX constant. Therefore differentiating
at fixed X commutes with the specialization X=-j. This is not
evaluation at a moving coefficient-field root.

Use the complete original rows438(4). Equations(18),(20),(22)
give exactly
\[
Y|_{X=-j}=v_1+\eta_0,\qquad
Z|_{X=-j}=r_0(v_1+\eta_0)+\zeta,
\tag{24}
\]
where
\[
\zeta=n-T-j(s+f)-j^2t^2+r\eta_0\in L.
\]
Since r0 is also complex, subtracting r0 times the first row from
the second introduces no coefficient derivative.

For the third ORIGINAL row, write Wj=W|X=-j. Its full expression is
\[
\begin{aligned}
W_j={}&-\lambda P^2-2v_1P+rE_0P+
 \{r(\nu+j)-g\}v_1+C_0,\\
C_0={}&\ell-g\eta+(\nu+j)T+j^2s.
\end{aligned}
\tag{25}
\]
In particular no coefficient-field modification of W was made.
Substitute P=A*v1^2+C to obtain all five coefficients
\[
W_j=\sum_{i=0}^4D_i v_1^i,\qquad
\begin{cases}
D_4=-\lambda A^2,\\
D_3=-2A,\\
D_2=A(-2\lambda C+rE_0),\\
D_1=-2C+r(\nu+j)-g,\\
D_0=-\lambda C^2+rE_0C+C_0.
\end{cases}
\tag{26}
\]

For coefficient functions in L, set
\(\{\zeta,h\}=\zeta_t h_s-\zeta_s h_t\).
The first row in(24) has coefficient derivatives (0,0,1),
so the entire specialized determinant is
\[
J(-j)=\{\zeta,W_j\}
=\sum_{i=0}^4\{\zeta,D_i\}v_1^i\in L^*.
\tag{27}
\]
This retains the whole constant term. Its precise value is not
needed, but its nonvanishing is essential.

## 6. Four scalar coefficients give the contradiction

The cubic coefficient in(27) first gives {zeta,A}=0.
The quartic coefficient then gives
\[
0=\{\zeta,\lambda A^2\}=A^2\{\zeta,\lambda\}.
\]
Since A is nonzero, lambda_s=0 and lambda_t=2b nonzero, this
forces zeta_s=0. If zeta_t were zero as well, the whole scalar
in(27) would vanish. Hence
\[
\zeta_s=0,\qquad \zeta_t\ne0.
\tag{28}
\]
The cubic coefficient now forces A_s=0. The linear coefficient,
using r,nu,j,g in F, forces C_s=0. But the quadratic coefficient
then becomes
\[
\begin{aligned}
\{\zeta,D_2\}
&=\zeta_t A r(E_0)_s\\
&=\zeta_t A\,\frac{2b}{\beta}
                 \left(-\frac{\beta}{2}\right)
=-A b\zeta_t\ne0.
\end{aligned}
\tag{29}
\]
This contradicts the scalar condition in(27). The profile(3) is
therefore excluded.

## 7. Scope and reconstruction boundary

The proof covers only the moving-slope resonance profile(2,2,2)
under the complete actual hypotheses(1). The formal quadratic
relation-space argument alone is not claimed to be an actual
obstruction. Its role is to force the exact coefficient conditions
that make X=-j a legitimate complex specialization of the original
nonzero scalar.

The proof neither needs a polynomial-in-t classification of the
lower potentials nor uses a field-valued ambient coordinate change.
It leaves all other degree profiles separate. No exclusion is
inferred merely from a generic projection or from a formal family
that satisfies a few high coefficients.

The complete438 source was freshly read through EOF and rehashed;
441's exact transformation and support were read completely in this
workstream. Fresh unsaved cb40d7 reconstructed (15),(16) from the
FULL438 fourth polynomial after the polynomial quadric substitution,
and verified every coefficient in(12),(13). Fresh9e6dd4 retained the
original rows and checked eta_s, eta_t+j^2, both identities(24),
the whole third row(25), all displayed nonconstant coefficients
of(26), and the final coefficient in(29). All residuals were zero.
The unit-cofactor, exact constants and parameter-calibration steps
are the written algebraic arguments, not consequences of sampling.

No saved checker was executed, imported, compiled or rerun. No
earlier source or canonical index was edited. No unrestricted
recognition, cancellation, historical novelty, external expert
review or formal certification is claimed.
