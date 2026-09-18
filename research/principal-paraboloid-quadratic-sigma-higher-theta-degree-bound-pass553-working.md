# A degree bound for quadratic sigma and higher theta

Working necessary result: retain the FULL actual264/296/535 chart,
with noncomplex coupling m, intrinsic sigma of degree two, and
theta of degree n at least three. Then
\[
\boxed{\deg y\le n\quad\text{unless}\quad
       (n,\deg y)=(3,4)\ \text{or}\ (4,6).}
\tag{1}
\]
Equivalently, theta degree three permits y degree at most four;
theta degree four permits y degree at most four or exactly six;
and theta degree at least five permits y degree at most theta's.
The zero polynomial y has degree minus infinity and is included.
The two exceptional profiles satisfy the explicit leading systems
in Section 6. Neither profile is asserted to exist or excluded here.

The proof uses complete polynomial support and the unit multiplier
of535, not a finite degree search. It gives no arbitrary chart entry,
recognition, coefficient-field rationality or cancellation claim.

## 1. Full actual hypotheses and the intrinsic normalization

Retain EVERY actual hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md)
and
[535](principal-paraboloid-nonlinear-sigma-unit-multiplier-pass535-working.md).
In particular retain
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=\mathcal A[u],\quad
E=\partial_u,\quad X=a_0u+x_0,\quad a_0\ne0,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\quad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the ENTIRE initial kernel},\\
0\ne N=[u^4]\partial_Z|_{\mathcal A},\quad
Na_0=Nt=Ns=0,\quad Nv=1,\\
L=\operatorname{Frac}\ker_{\mathcal A}N,\quad
[L:\mathbb C(t,s)]<\infty,\quad
L[\mathcal A]=L[v]=L[y,\sigma,\theta],\\
\operatorname{Frac}\mathcal A=L(v)=\mathbb C(y,z_{\rm int},w),
\qquad m=k_s\notin\mathbb C.
\end{gathered}
\tag{2}
\]
Here z_int is the literal original Z-intercept, not its difference
with 2ty. Both polynomial returns, the genuine moving levels, the
selected literal partial and the full calibrated scalar remain
required. In particular m is nonzero. The original global slice
is not assumed equal to X/a0.

Use the notation mathfrak n for the potential usually called n,
to distinguish it from the integer degree of theta. The full rows
and first two potentials are
\[
\begin{aligned}
Y&=y+\sigma X+tX^2,\\
Z&=2ty+\sigma^2+k_t\sigma+m\theta+\mathfrak n
                          +(2t\sigma+k)X+t^2X^2,\\
W&=w+\theta X+sX^2,\\
mw&=\ell-(2\sigma+k_t)y-\mathcal F(\sigma,\theta),\\
\mathcal F(P,V)&=\frac{k_{tt}}2P^2+pPV+\frac h2V^2
                              +\mathfrak n_tP+\mathfrak n_sV,
\qquad p=m_t,\quad h=m_s.
\end{aligned}
\tag{3}
\]

Write the original quadratic sigma as
sigma=a2*v squared+a1*v+a0c, with a2 nonzero. Set
v0=-a1/(2a2), choose rho squared=a2 in the finite coefficient
extension L'=L(rho), and put x=rho(v-v0). Thus
\[
\sigma=x^2+c,\quad c\in L',\quad Nx=\rho\ne0,\qquad
J_{t,s,x}(Y,Z,W)=-a_0^4/\rho\in(L')^*.
\tag{4}
\]
No actual coordinate is changed. This is a finite scalar extension
and an affine intrinsic reparameterization only. The coefficient
partials on L' are the exact commuting extensions of partial_t and
partial_s. Extend them to fix x. Derivatives of y and theta then
include every moving-center and moving-scale contribution.
No rationality of L' is assumed.

Put beta=sigma_x=2x, and define
\[
\begin{aligned}
f&=H_U(y,\sigma,\theta),\quad g=H_V(y,\sigma,\theta),\\
\nu&=\frac{p\sigma+h\theta+\mathfrak n_s}{m},\quad
D_f=\frac{2\sigma+k_t}{m},\quad
B_f=\frac{2y+k_{tt}\sigma+p\theta+\mathfrak n_t}{m},\\
\mathcal A_\beta&=4x^2y_t+2x\theta_xy_s+y_x^2
                             -2xc_ty_x-c_sy_x\theta_x,\\
\mathcal B_\beta&=4x^2(\theta_t+B_f)+2xD_fy_x+y_x\theta_x
                         +2x(\theta_s+\nu-c_t)\theta_x-c_s\theta_x^2,\\
\mathcal A_\beta&=\kappa g,\qquad
\mathcal B_\beta=-\kappa f,\qquad \kappa\in(L')^*.
\end{aligned}
\tag{5}
\]
The last line is the complete multiplier conclusion of535.
Under the intrinsic affine change it has kappa=kappa_v/rho squared:
the moving-center terms in each expression cancel by the chain
rule, and both expressions scale by rho to the power minus two.
Thus (5) holds at x=0 as well. No division by beta, f or g is made,
and no coprimality of f and g is assumed.

## 2. Complete formal support, before evaluation

With U,P,V independent, define
\[
\begin{aligned}
\mathfrak w&=\{\ell-(2P+k_t)U-\mathcal F(P,V)\}/m,\\
H-h_0&=U^2+\mathcal F_PU+\mathcal F_V\mathfrak w
       +H_3(k;P,V)+H_2(\mathfrak n;P,V)
       -\ell_tP-\ell_sV-h_0,\\
H(y,\sigma,\theta)&=h_0\in L'.
\end{aligned}
\tag{6}
\]
The Taylor polynomials are the genuine ones of264/296.
Expand the entire formal polynomial as
\[
H-h_0=U^2+(C_1+C_2V)U+C_3V^3+C_4V^2+C_5V+C_6.
\tag{7}
\]
For B=pP+mathfrak n_s, F0=k_tt*P squared/2+mathfrak n_t*P,
and gamma=2P+k_t, its exact coefficients are
\[
\begin{aligned}
C_1&=k_{tt}P+\mathfrak n_t-\gamma B/m,&
C_2&=p-\gamma h/m,\\
C_3&=h_s/6-h^2/(2m),&
C_4&=h_tP/2+\mathfrak n_{ss}/2-3hB/(2m),\\
C_5&=m_{tt}P^2/2+\mathfrak n_{ts}P-\ell_s
                              +(h\ell-B^2-hF_0)/m,\\
C_6&=k_{ttt}P^3/6+\mathfrak n_{tt}P^2/2-\ell_tP-h_0
                              +B(\ell-F_0)/m.
\end{aligned}
\tag{8}
\]
Their P-degrees are at most 2,1,0,1,2,3, respectively.
This is the formal expansion also printed in521, now evaluated
at quadratic sigma rather than using sigma as a line coordinate.
Differentiating BEFORE evaluation gives
\[
H_U=2U+C_1+C_2V,\qquad
H_V=C_2U+3C_3V^2+2C_4V+C_5.
\tag{9}
\]
In particular no derivative of an evaluated constant level is
substituted for either formal gradient.

Let theta=a*x to the n+lower terms, with n>=3 and a nonzero.
If y is nonconstant, let j=deg_x(y), y=r*x to the j+lower terms,
with r nonzero. Substituting P=x squared+c in (7)--(9) gives
\[
\begin{array}{c|c}
\text{term in the complete H level}&\text{degree bound in x}\\ \hline
y^2&2j\\
C_1y&j+4\\
C_2\theta y&j+n+2\\
C_3\theta^3&3n\\
C_4\theta^2&2n+2\\
C_5\theta&n+4\\
C_6&6
\end{array}
\qquad
\begin{aligned}
\deg f&\le\max(j,n+2,4),\\
\deg g&\le\max(j+2,2n,n+2,4).
\end{aligned}
\tag{10}
\]
These are support bounds, not assertions of nonzero leading terms.
Vanishing coefficients and all lower coefficients are retained.
Coefficient derivatives at fixed x do not increase polynomial degree.

## 3. A uniform first bound and the h=0 boundary

If y is zero or constant, (1) already holds. Henceforth j>0.
Suppose j>n+2. In A_beta the term y_x squared has degree 2j-2
and nonzero coefficient j squared*r squared. The other four
terms have degree at most
\[
j+2,\quad n+j,\quad j,\quad n+j-2,
\tag{11}
\]
respectively. Since n>=3 and j>n+2, their degrees and every
bound for g in (10) are strictly less than 2j-2. The equation
A_beta=kappa*g is impossible. Thus j<=n+2 for every n>=3.

We will also use the following exact boundary. If h=0 as a field
element, then h_s=h_t=0, C2=p, C3=0 and C4=mathfrak n_ss/2.
The U coefficient and free coefficient of the evaluated monic H
then have degrees at most
\[
\max(4,n),\qquad \max(2n,n+4,6).
\tag{12}
\]
For n>=4 and j>n, y squared is uniquely highest: 2j exceeds
j+max(4,n) and max(2n,n+4,6). Hence h=0 implies j<=n when
n>=4. This uses no division by p and includes p=0.

## 4. Removing j=n+1 and the cubic j=5 boundary

Suppose n>=4 and j=n+1. If C3 were nonzero, C3*theta cubed
would have degree 3n, while all other terms in (10) have degree
at most 2n+3<3n. Therefore C3=0. The entire theta-cubed term
disappears, not merely its leading monomial. The next coefficient is
\[
[x^{2n+3}](H-h_0)=-2har/m=0.
\tag{13}
\]
All other terms have smaller degree, including y squared of
degree 2n+2. Since a,r,m are nonzero, h=0, which contradicts
(12). Thus j=n+1 is excluded for every n>=4.

For n=3 the uniform bound gives j<=5. If j=5, the two terms
4x squared*B_f and 2x*D_f*y_x in B_beta have combined leading
coefficient
\[
[x^7]\mathcal B_\beta=(8+4\cdot5)r/m=28r/m\ne0.
\tag{14}
\]
Every other term has degree at most six, while deg f<=5.
Equation (5) excludes j=5, leaving j<=4 when n=3.

## 5. Removing j=n+2 for every n>=5

Suppose n>=5 and j=n+2. First (12) shows h is nonzero.
The bound 3n>2n+4 and (10) give
\[
C_3=0,\qquad h_s=3h^2/m.
\tag{15}
\]
After this entire term is removed, the degree 2n+4 coefficient
of H comes only from y squared and C2*theta*y:
\[
r^2-2har/m=0,\qquad r=2ha/m.
\tag{16}
\]
The division by r is licensed by j=deg y.

In B_beta, the degree 2n terms are precisely y_x*theta_x and
2x*(theta_s+h*theta/m)*theta_x. All other contributions have
degree at most max(n+4,2n-2), which is strictly less than 2n.
Also deg f<=n+2<2n. Therefore
\[
na\{(n+2)r+2a_s+2ha/m\}=0,
\qquad a_s=-(n+3)ha/m.
\tag{17}
\]
These are genuine coefficient identities in L'. Differentiating
(16) by its exact s partial, using m_s=h and (15),(17), gives
\[
r_s=2\{(h_sa+ha_s)/m-h^2a/m^2\}
                   =-2(n+1)h^2a/m^2.
\tag{18}
\]
Thus r_s is not treated as an independent jet after (16).

Once C3=0, (9) gives deg g<=n+4. But the full A_beta coefficient
of degree 2n+2 is
\[
\begin{aligned}
[x^{2n+2}]\mathcal A_\beta
 &=2na r_s+(n+2)^2r^2\\
 &=4(3n+4)h^2a^2/m^2\ne0.
\end{aligned}
\tag{19}
\]
Only 2x*theta_x*y_s and y_x squared contribute at this degree.
Since 2n+2>n+4, this contradicts A_beta=kappa*g. The case
j=n+2 is excluded for all n>=5. Together with Sections 3--4,
this proves (1), including all zero and lower-degree cases.

## 6. The two remaining excess-degree leading systems

For (n,j)=(3,4), let a and r again denote the exact nonzero
leading coefficients of theta and y. The full H degree-nine,
B_beta degree-six and A_beta degree-seven coefficients give
\[
\boxed{
a^3C_3-2har/m=0,\qquad
6a(a_s+ha/m)+24r/m=0,\qquad r_s=0.}
\tag{20}
\]
Here deg f<=5 and deg g<=6. In the last equation the full
coefficient is 6a*r_s. The first equality has two possibly
cancelling contributions, so it does NOT imply C3=0 or h=0.
The h=0 boundary is not excluded or divided away in (20).

For (n,j)=(4,6), the full H degree-twelve, B_beta degree-eight
and A_beta degree-ten coefficients give
\[
\boxed{\begin{aligned}
r^2-2har/m+a^3C_3&=0,\\
24ar+8aa_s+8ha^2/m+32r/m&=0,\\
8ar_s+36r^2&=0.
\end{aligned}}
\tag{21}
\]
In this case deg f<=6 and deg g<=8. In the middle equality the
term 32r/m is the combined contribution of 4x squared*B_f and
2x*D_f*y_x. It must be retained at this degree. The first equality
retains the theta-cubed contribution, so the argument of Section 5
cannot be applied at n=4. Equation (12), or (21) with h=h_s=0,
does imply h nonzero in this exceptional profile.

All these derivatives are the genuine exact coefficient partials.
In particular p_s=h_t, m_s=h and the definition of C3 remain in
force; h_s is not a freely adjustable coefficient. Lower coefficients
of y and theta, all lower potentials and their moving levels remain
subject to the full H, Q, scalar and return conditions. Equations
(20),(21) are necessary leading systems only, not sufficient data
for a realization. No claim about their solvability is made here.

## 7. Verification, prior scope and limits

The complete535 and the formal-support input521 were read through
EOF before writing. The earlier strict quadratic-sigma parity note466
and its461 input were also read: their assumption k=s+f has constant
coupling and does not provide this noncomplex-coupling degree bound.
No theorem from that constant-coupling sector is imported here.

Fresh unsaved calculation6233e1, completed in39a4cf, reconstructed
the full formal H from (6), differentiated H_U and H_V before
evaluation, and retained every lower coefficient and t/s jet of y
and theta. Thirty exact residuals were zero. They cover the uniform
excess-degree coefficient, the n>=5 endpoint chain, the j=n+1
chain, the cubic j=5 boundary, and both exceptional systems.
The explicit degree instances used for reconstruction were
(n,j)=(3,5),(3,4),(4,6),(4,5),(5,7),(6,8),(7,9),(5,6),(6,7),
(3,6),(4,7). These checks supplement the uniform inequalities and
complete coefficient formulas above; they are not the proof for
unbounded n.

All divisions in the proof are by nonzero coefficient-field elements
m,a,r,h when explicitly licensed, or nonzero integers. Neither x nor
beta is inverted, so the unique critical point of quadratic sigma is
retained. The coefficient extension and derivative conventions are
kept separate from actual polynomial coordinate transformations.
No constant-coupling normalization is used.

No saved checker was executed, imported, compiled or rerun. No
earlier source or canonical file was edited. A complete independent
saved-source review remains required after the author hold. This
note asserts only the supplied-chart necessary degree restriction
and its two exceptional leading systems, not novelty, arbitrary
entry, recognition, realization or unrestricted cancellation.
