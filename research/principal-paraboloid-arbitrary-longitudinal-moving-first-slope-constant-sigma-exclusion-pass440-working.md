# Moving first slope excludes constant sigma with arbitrary longitudinal coupling

Working necessary result: retain the full actual264 chart and assume
\[
k=s+f,\qquad n=\nu s+n_0,\qquad
f,\nu,n_0\in\mathbb F:=\ker_L\partial_s,\qquad \nu'\ne0.
\tag{1}
\]
Then sigma cannot belong to L. No bound on f''', on any derivative
of n0, or on the second potential ell is imposed.

This extends350's constant-sigma exclusion from k=s to k=s+f.
Both branches of the third potential's theta coefficient are handled
directly: the nonzero branch contradicts the genuine fourth level;
the zero branch contradicts the entire calibrated scalar. The proof
uses no degree-two projection recognition, no ambient transformation
with the variable coefficient nu, and no claim that this remaining
moving-slope family is itself recognized.

## 1. Actual hypotheses and exact derivatives

Retain EVERY actual hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md), including
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,
\quad A=\ker E,\quad\deg_E(X,Y,Z,W)=(1,2,2,2),\\
a_0=EX\ne0,\quad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the full weighted initial kernel},\\
N=[u^4]\partial_Z|_A\ne0,\quad
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,
\quad Na_0=Nt=Ns=0,\quad Nv=1,\\
O=L[v]=L[y,z,w]=L[y,\sigma,\theta],\quad
K=\operatorname{Frac}A=L(v)=\mathbb C(y,z,w),\\
J(X)=\det\frac{\partial(Y,Z,W)}{\partial(t,s,v)}
                      =-a_0^4\in L^*.
\end{gathered}
\tag{2}
\]
The original slice, actual localization, selected literal partial,
both returns and genuine potentials remain assumptions. The exact
coefficient partials commute and initially fix v, and their joint
constant field is C. The field F in(1) is finite over C(t), but is
not assumed rational. A prime on an element of F is its exact
t-derivative. Put b=nu' in F*, so
\[
n_s=\nu,\quad n_{ts}=b,\quad n_{ss}=0,\quad
n_t=bs+n_0',\quad n_{tt}=b's+n_0''.
\tag{3}
\]
All coefficient derivatives of formal potentials below hold their
independent formal variables fixed before evaluation.

The first two potentials and complete literal rows are
\[
\begin{aligned}
z&=2ty+\sigma^2+f'\sigma+\theta+n,\\
w&=\ell-(2\sigma+f')y-\frac{f''}{2}\sigma^2-n_t\sigma-\nu\theta,\\
Y&=y+\sigma X+tX^2,\\
Z&=z+(2t\sigma+s+f)X+t^2X^2,\\
W&=w+\theta X+sX^2.
\end{aligned}
\tag{4}
\]
In particular the theta coefficient -nu in w must be retained.

## 2. Full third relation and the two required fourth gradients

Use independent formal variables U,P,V over L.264's quadratic
polynomial and the expression for the second intercept are
\[
F(P,V)=\frac{f''}{2}P^2+n_tP+\nu V,\qquad
g=\ell-(2P+f')U-F(P,V).
\tag{5}
\]
Its full third polynomial is
\[
\boxed{\begin{aligned}
H(U,P,V)={}&U^2+\{(f''-2\nu)P+n_t-\nu f'\}U\\
&+\frac{f'''}6P^3+\frac{n_{tt}-\nu f''}{2}P^2
 -(\ell_t+\nu n_t)P+\nu\ell\\
&+(bP-\ell_s-\nu^2)V,
\end{aligned}}
\qquad H(y,\sigma,\theta)=h\in L.
\tag{6}
\]
To obtain(6), substitute(5) in the exact expression
U^2+F_P U+F_V g+H3(k)+H2(n)-ell_t P-ell_s V.
Here H3(k)=f'''P^3/6 and H2(n)=n_tt P^2/2+bPV.
Thus neither the longitudinal cubic nor the mixed bPV term is lost.

The genuine fourth potential from
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md)
satisfies Q(y,sigma,theta)=q in L. Its corrected gradient formulas,
with m=1 and F_V=nu, give
\[
Q_U=H_P-(2P+f')H_V+\nu H_U,\qquad
Q_V=H_s-h_s.
\tag{7}
\]
Direct differentiation of(6) gives the complete two components
\[
\boxed{\begin{aligned}
Q_U={}&f''U+\left(\frac{f'''}2-2b\right)P^2
 +(n_{tt}+2\ell_s-bf')P+bV+f'\ell_s-\ell_t,\\
Q_V={}&bU+\frac{b'}2P^2-(\ell_{ts}+\nu b)P
 -\ell_{ss}V+\nu\ell_s-h_s.
\end{aligned}}
\tag{8}
\]
For example H_s uses (n_t)_s=b and (n_tt)_s=b'; every derivative
of f or nu with respect to s is zero. The genuine level derivative
h_s is present. Q_P and the other fourth-level coefficients are
not needed here, but no replacement potential omitting them is
asserted.296 supplies the complete existing Q and its level.

## 3. Nonzero theta coefficient gives a nonzero quadratic term

Suppose, for contradiction, that sigma=p belongs to L. Define
\[
\chi=\frac{(f''-2\nu)p+n_t-\nu f'}2,\qquad x=y+\chi,
\qquad D=bp-\ell_s-\nu^2\in L.
\tag{9}
\]
The centering is over the coefficient field only. Let
\[
C_p=\frac{f'''}6p^3+\frac{n_{tt}-\nu f''}{2}p^2
          -(\ell_t+\nu n_t)p+\nu\ell\in L.
\tag{10}
\]
Then(6) becomes
\[
x^2+D\theta=h-C_p+\chi^2.
\tag{11}
\]

First assume D is nonzero. The relation solves theta polynomially:
\[
\theta=a_2x^2+d_0,\qquad
a_2=-1/D\in L^*,\qquad d_0=(h-C_p+\chi^2)/D\in L.
\tag{12}
\]
The whole return in(2) is therefore O=L[x,theta]=L[x]. In particular
x is an affine nonconstant polynomial in v. It is not a new ambient
coordinate. Differentiate the genuine fourth level in this polynomial
parameter while holding L fixed:
\[
0=Q_U(x-\chi,p,a_2x^2+d_0)
       +2a_2x\,Q_V(x-\chi,p,a_2x^2+d_0).
\tag{13}
\]
There is no Q_P term because p is fixed in L. Introduce coefficients
\[
\begin{aligned}
u_0&=-f''\chi+\left(\frac{f'''}2-2b\right)p^2
 +(n_{tt}+2\ell_s-bf')p+f'\ell_s-\ell_t,\\
v_0&=-b\chi+\frac{b'}2p^2-(\ell_{ts}+\nu b)p
                              +\nu\ell_s-h_s.
\end{aligned}
\tag{14}
\]
Using(8), the right side of(13) is exactly
\[
-2\ell_{ss}a_2^2x^3+3ba_2x^2
 +\{f''+2a_2(v_0-\ell_{ss}d_0)\}x+(u_0+bd_0).
\tag{15}
\]
Its x^2 coefficient is nonzero because b,a2 are nonzero and the
characteristic is zero. This contradicts the polynomial identity(13).
There is no need first to divide by, or force vanishing of, ell_ss.
The additional longitudinal terms only enter the other coefficients.

## 4. Zero theta coefficient contradicts the full all-X scalar

Now assume D=0, without dividing by D. Equation(11) makes x^2 an
element of L. Since x is a polynomial in v, it must have degree zero.
Thus y and sigma belong to L, while the whole return forces
\[
O=L[\theta]=L[v],\qquad \tau=N\theta\in L^*.
\tag{16}
\]
The second assertion follows because a generator of L[v] has degree
one in v. Use the separating field variables (t,s,theta). Their
coefficient derivatives restrict on L to the original exact partials
and are extended to fix theta. The triangular Jacobian from the old
(t,s,v) has determinant tau, even if theta's old t,s derivatives
were nonzero. Consequently the entire calibrated scalar is
\[
\widetilde J(X)=\det\frac{\partial(Y,Z,W)}{\partial(t,s,\theta)}
                       =-a_0^4/\tau\in L^*.
\tag{17}
\]
It is independent of both X and theta.

Write the literal rows(4) exactly as
\[
\begin{aligned}
Y&=y+\sigma X+tX^2,\\
Z&=\theta+Z_0(X),\\
Z_0&=2ty+\sigma^2+f'\sigma+n+(2t\sigma+s+f)X+t^2X^2,\\
W&=(X-\nu)\theta+W_0(X),\\
W_0&=\ell-(2\sigma+f')y-f''\sigma^2/2-n_t\sigma+sX^2.
\end{aligned}
\tag{18}
\]
Here Z0,W0 belong to L[X]. Define only for a row computation
\[
I=W-(X-\nu)Z=W_0-(X-\nu)Z_0\in L[X].
\tag{19}
\]
Because nu need not belong to the original polynomial ring, I is
NOT declared to be an original coordinate or even an element of B.
At fixed X, nu_s=0 and nu_t=b give the exact differential identity
\[
dW-(X-\nu)dZ=dI-bZ\,dt.
\tag{20}
\]
This retains the derivative of the variable coefficient nu.

The first row has no dtheta term. The second has dtheta coefficient
one, and the new third row in(20) has none. Expanding the determinant
in the ordered basis dt,ds,dtheta gives
\[
\boxed{\widetilde J=Y_s I_t-Y_t I_s-bZY_s.}
\tag{21}
\]
The terms involving I have no theta dependence. Since Z=theta+Z0,
the coefficient of theta in(21) is
\[
-bY_s=-b(y_s+\sigma_s X).
\tag{22}
\]
The scalar(17) has no such coefficient. As b is nonzero and X is
transcendental over L, this forces y_s=sigma_s=0. Thus(21) reduces to
\[
\widetilde J=-(X^2+\sigma_tX+y_t)I_s.
\tag{23}
\]
Both factors are polynomials in L[X]. The first is monic of degree
two. If Is=0, the determinant is zero; otherwise its degree in X is
at least two. Neither possibility equals the nonzero constant(17).
This excludes D=0 and completes the contradiction.

## 5. Conclusion, overlap and exact boundary

The two cases prove
\[
\boxed{\text{Under the full actual chart(2) and assumptions(1),}
                     \quad\sigma\notin L.}
\tag{24}
\]
Equivalently, within k=s+f and n_ss=0, a constant intrinsic sigma
forces n_ts=0. This is a necessary statement in the supplied chart,
not an actual realization or a recognition of nonconstant sigma.

When f=0 this is the already proved
[350](principal-paraboloid-moving-first-slope-constant-sigma-exclusion-pass350-working.md).
The present proof reconstructs its two mechanisms with every new
longitudinal term retained. It does not assume an actual map taking
arbitrary f to zero. The nonzero-D branch is indeed an intrinsic
double projection, but no theorem307 or303 is needed. The zero-D
branch never uses a claimed actual kernel C[X,Y,W-(X-nu)Z].
That expression would require a separate original-ring justification
when nu is variable; the row operation(19),(20) makes no such claim.

If b=0 the decisive coefficients in(15),(22) vanish, so that boundary
is not excluded by this argument. The values of f''', ell_ss, b',
sigma and either level may be zero wherever not explicitly ruled out.
Only the nonzero-D branch divides D; only the zero-D branch uses
the affine theta parameter. These cases exhaust the coefficient D.

The complete saved350 source was read through80a9c1 before extending
it. The current264 and296 sources were freshly read through EOF in
8cdb7a and b6cc24. The writing guide had been read fully in41c9bc
before this continuation's authored notes. Fresh unsaved e3d893
reconstructs the full raw H, both corrected fourth gradients, the
centered cubic and quadratic coefficients, and the complete scalar
row identity and its two consequences. Every residual is zero.
These checks supplement the exact polynomial-degree arguments.

No saved checker was executed, imported, compiled or rerun. No
earlier source or canonical record was edited. No ambient-coordinate
promotion, coefficient-field rationality, arbitrary chart entry,
unrestricted cancellation result, historical novelty, expert review,
proof-assistant certification or external contact is claimed.
