# Curvature evolution in every remaining higher-degree profile

Working necessary reduction under the complete supplied actual264
chart with k=s and n_ss nonzero. For every one of the six remaining
profiles in417, the coefficient beta is nonzero and the quadratic
curvature divided by beta squared is not constant along the
characteristic derivation.

The proof uses the two highest relevant coefficients of the genuine
fourth potential. It retains all lower intrinsic functions and does
not apply a degree-one scalar calculation to them. No remaining
profile is excluded by this note alone.

## 1. Complete actual input and the remaining degree balance

Retain EVERY actual hypothesis in
[264](principal-one-affine-paraboloid-chart-pass264-working.md)
and the reviewed necessary frontier in
[417](principal-paraboloid-equal-quadratic-exclusion-synthesis-pass417-working.md).
In particular,
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A_0[u_0],\qquad
E=\partial_{u_0},\qquad \deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(X^2Z-Y^2)\text{ is the full initial kernel},\qquad
0\ne N=[u_0^4]\partial_Z|_{A_0},\\
L=\operatorname{Frac}\ker_{A_0}N,\quad [L:\mathbb C(t,s)]<\infty,
\quad Nv_0=1,\quad a_0=EX\in L^*,\\
O=L[v_0]=L[y,\sigma,\theta]=L[y,z,w],\qquad
K=L(v_0)=\mathbb C(y,z,w),\\
J_{t,s,v_0}(X)=-a_0^4\in L^*,\qquad k=s,\quad e=n_{ss}\ne0 .
\end{gathered}
\tag{1}
\]
The global slice, original localization, literal selected partial,
both actual returns, complete genuine levels and their evaluated
unit ideals remain imposed. The exact coefficient partials commute
and have joint constants C.

Use
\[
\begin{gathered}
d=\deg\sigma=\deg\theta,\qquad
\lambda=[v_0^d]y/[v_0^d]\sigma,\qquad
\mu=[v_0^d]\theta/[v_0^d]\sigma,\\
a=n_t,\quad \nu=n_s,\quad b=n_{ts},\quad c=n_{tt},\quad
\delta=\lambda-\nu,\quad \beta=b+e\mu,\\
\mathscr D=\partial_t+\mu\partial_s,\qquad
\mathcal C=\beta^2+2e\delta^2,\\
u_1=y-\lambda\sigma,\qquad v_1=\theta-\mu\sigma,\qquad
j=\delta a-\ell_t-(\ell_s+\nu^2)\mu,\\
R=2\delta u_1+\beta v_1+j,\qquad
r=\deg R,\quad m=\max(\deg u_1,\deg v_1).
\end{gathered}
\tag{2}
\]
All degrees are intrinsic degrees in the original v0 over L.
The symbol R denotes a function on that line, not an original
coordinate. The coefficient lambda is allowed to be zero.

The inputs417 and
[413](principal-paraboloid-higher-degree-characteristic-zero-reduction-pass413-working.md)
give
\[
\begin{gathered}
\delta\ne0,\quad \mathcal C\ne0,\quad
1\le r<m<d,\quad d+r=2m,\quad
\mu\notin\mathbb C+\mathbb C t,\\
\mathscr D\lambda=0,\qquad \mathscr D\mu=-4\lambda,\qquad
\mathscr D\delta=-\beta,\\
(r,m,d)\in\{(1,2,3),(1,3,5),(2,3,4),
                 (2,4,6),(3,4,5),(4,5,6)\}.
\end{gathered}
\tag{3}
\]
The result below uses the inequalities and degree balance, rather
than a separate numerical argument for each entry.

We prove the necessary differential system and its nonzero-ratio
consequence
\[
\boxed{\begin{gathered}
\beta\ne0,\qquad
\delta\,\mathscr D\beta+2\beta^2=0,\\
\mathscr De+\frac{3e\beta}{\delta}
               +\frac{\beta^3}{2\delta^3}=0,\\
\kappa:=\frac{\mathcal C}{\beta^2}\ne0,\qquad
\mathscr D\kappa=-\frac{\beta}{\delta}\kappa\ne0 .
\end{gathered}}
\tag{4}
\]
In particular kappa is not a complex constant. No assertion that
a necessary family is realized is made.

## 2. Leading terms of the complete third level

The full third level, after the invertible formal substitution
U=lambda*P+U1, V=mu*P+V1, is the identity proved in
[407](principal-paraboloid-equal-degree-higher-rank-split-pass407-working.md):
\[
H-h_0=P(2\delta U_1+\beta V_1+j)
       +U_1^2+aU_1+\frac e2V_1^2
       -(\ell_s+\nu^2)V_1+\nu\ell-h_0.
\tag{5}
\]
It evaluates to zero at(P,U1,V1)=(sigma,u1,v1).

The function v1 has exact degree m. Indeed, otherwise R of degree
r<m and delta nonzero would imply deg u1<m from its definition,
contrary to the definition of m. Put
\[
\rho=[v_0^r]R,\qquad h_m=[v_0^m]v_1,\qquad
p_d=[v_0^d]\sigma,\qquad \rho,h_m,p_d\in L^* .
\]
The leading coefficient of u1 at degree m is
-beta*h_m/(2delta), which can be zero if beta=0. The full leading
equation in(5) is therefore
\[
\boxed{\qquad
p_d\rho=-\frac{\mathcal C}{4\delta^2}h_m^2 .
\qquad}
\tag{6}
\]
This includes beta=0: in that case u1 has lower degree and the
term e*v1^2/2 alone supplies the right side. No division by beta
has occurred.

## 3. The exact cubic tensor of the genuine fourth potential

Use the complete fourth polynomial of
[365, equation(7)](principal-paraboloid-nonlinear-intercept-unequal-degree-gate-pass365-working.md).
Its homogeneous cubic part in the ORIGINAL formal variables is
\[
Q_3=-2bP^2U-2ePVU+\frac{n_{ttt}}6P^3
 +\frac{n_{tts}}2P^2V+\frac{n_{tss}}2PV^2
 +\frac{n_{sss}}6V^3 .
\tag{7}
\]
All remaining terms form a polynomial of total degree at most two.
In particular the actual h0_t,h0_s terms remain present there.
The complete evaluated Q is a coefficient constant.

The third leading equation and(3) imply
\[
\mathscr D^2n=-2\lambda^2,\qquad
n_{ttt}+3\mu n_{tts}+3\mu^2n_{tss}+\mu^3n_{sss}
      =12\lambda\beta .
\tag{8}
\]
For the second identity differentiate the first. The product
rule contributes 3*Dscript(mu)*beta and
Dscript squared(mu)*nu to the third total derivative.
These are -12lambda*beta and zero respectively. Also
\[
\mathscr D\beta=n_{tts}+2\mu n_{tss}+\mu^2n_{sss}-4\lambda e,
\qquad
\mathscr De=n_{tss}+\mu n_{sss}.
\tag{9}
\]
These are identities of the original coefficient derivatives.
They do not require lambda to be a separating parameter or even
to be noncomplex.

Substituting U=lambda*P+U1, V=mu*P+V1 into(7), and using
(8),(9), gives the ENTIRE cubic part
\[
\boxed{\quad
Q_3^{\rm shifted}
=-2\beta P^2U_1+\frac{\mathscr D\beta}{2}P^2V_1
 -2ePU_1V_1+\frac{\mathscr De}{2}PV_1^2
 +\frac{e_s}{6}V_1^3 .
\quad}
\tag{10}
\]
In particular the P-cubed coefficient vanishes exactly. This is
not an omission based on a guessed intrinsic degree.

Now use the invertible affine formal change
U1=(R-beta*V1-j)/(2delta). The complete polynomial has the form
\[
\begin{aligned}
Q={}&
\left(\frac{\beta^2}{\delta}+\frac{\mathscr D\beta}{2}\right)P^2V_1
 -\frac{\beta}{\delta}P^2R\\
&+\left(\frac{e\beta}{\delta}+\frac{\mathscr De}{2}\right)PV_1^2
 -\frac e\delta PV_1R+\frac{e_s}{6}V_1^3
 +Q_{\le2}(P,R,V_1).
\end{aligned}
\tag{11}
\]
Here Q<=2 has total degree at most two and includes all j terms,
the transformed lower coefficients, and the actual level
derivatives. It has not been set to zero. The changes in this
section are formal coefficient-field changes, not ambient maps.

## 4. Two strict degree comparisons give the differential gates

Evaluate(11) on the original line. The degree 2d+m is strictly
larger than 2d+r, d+2m, d+m+r, 3m and 2d. Thus the P^2*V1
term uniquely has the highest possible degree unless its
coefficient vanishes. Since Q evaluates to a constant and
p_d,h_m are nonzero,
\[
\frac{\beta^2}{\delta}+\frac{\mathscr D\beta}{2}=0.
\tag{12}
\]
This is the first differential gate in(4), without dividing beta.

After(12), the two next leading terms have the common degree
2d+r=d+2m. They are P^2*R and P*V1^2. All other terms have
strictly smaller degree:
d+m+r<d+2m, 3m<d+2m, and every term of Q<=2 has degree at
most 2d<2d+r. The positivity r>=1 is essential for that last
strict inequality. The coefficient equation is
\[
-\frac{\beta}{\delta}p_d^2\rho
 +\left(\frac{e\beta}{\delta}+\frac{\mathscr De}{2}\right)
       p_dh_m^2=0 .
\tag{13}
\]
Substitute(6) and divide only by p_d*h_m^2 and delta, which
are nonzero. The resulting identity is
\[
\boxed{\qquad
\mathscr De+\frac{3e\beta}{\delta}
                 +\frac{\beta^3}{2\delta^3}=0 .
\qquad}
\tag{14}
\]
No leading coefficient of a lower intrinsic function has been
assumed constant under a coefficient partial. The argument
compares powers in an evaluated polynomial, so it requires no
differentiation of those leading coefficients at all.

## 5. The zero-beta boundary is excluded separately

Suppose beta=0. Since Dscript(delta)=-beta, delta is a nonzero
element of F:=ker(Dscript). Equation(14) gives Dscript(e)=0.
The following two alternatives exhaust the slope lambda.

If lambda is noncomplex, Dscript(lambda)=0 implies lambda_s
nonzero. Use the separating basis(t,xi=lambda); Dscript is its
exact t partial. The characteristic family from413 gives
\[
\begin{gathered}
s=-2\xi t^2+\zeta t+S_0,\qquad
n=-\xi^2t^2+Ut+V,\qquad \zeta,S_0,U,V\in F,\\
s'=-2t^2+\zeta't+S_0'\ne0,\\
\delta s'=(\xi\zeta'-U')t+\xi S_0'-V' .
\end{gathered}
\tag{15}
\]
Here primes denote the exact xi partial. The left side of the
last equation has t-squared coefficient -2delta in F*, whereas
the right side has degree at most one in t. Since t is
transcendental over F, this is impossible.

If lambda is complex, use instead(t,xi=nu). This is a separating
basis since e is nonzero, and Dscript fixes xi because beta=0.
Let primes denote its xi partial and F=ker(Dscript). The same
exact Legendre calculation written in413, Section2 gives
\[
\begin{gathered}
n-\xi s=(2\lambda\xi-\lambda^2)t^2+Ut+V,
\qquad U,V\in F,\\
s=-2\lambda t^2-U't-V',\qquad
\mu=-4\lambda t-U',\qquad
e=-\frac1{U''t+V''}.
\end{gathered}
\tag{16}
\]
The denominator is nonzero because s'=1/e. Since Dscript(e)=0,
equation(16) forces U''=0. The element U' is killed by both
exact partials, hence is complex. It follows that
mu belongs to C+C*t, contradicting(3). This covers lambda=0
as well as nonzero complex lambda.

Thus beta is nonzero in every retained profile. Neither argument
used an original-coordinate normalization, a rational ansatz for
the coefficient field, or the degree-one exclusions.

## 6. Curvature evolution and an exact optional primitive

From(12),(14) and Dscript(delta)=-beta, direct differentiation
gives
\[
\mathscr D\mathcal C=-5\frac{\beta}{\delta}\mathcal C,\qquad
\mathscr D(\beta^2)=-4\frac{\beta}{\delta}\beta^2.
\tag{17}
\]
Therefore
\[
\boxed{\qquad
\mathscr D\left(\frac{\mathcal C}{\beta^2}\right)
 =-\frac{\beta}{\delta}\frac{\mathcal C}{\beta^2}\ne0 .
\qquad}
\tag{18}
\]
All three factors on the right are nonzero by(3) and Section5.
In particular any independent argument making this ratio
algebraic over C would be incompatible with these necessary
conditions, since C is algebraically closed.

For clarity, these equations also have an internal exact
integration. With F=ker(Dscript), define existing elements
\[
c_0=\frac{\delta^2}{\beta},\qquad
T=\frac{c_0}{\delta},\qquad
\tau=T-t,\qquad H_0=T^3e+T/2 .
\]
The first gate gives Dscript(c0)=0 and Dscript(T)=1;
the second gives Dscript(H0)=0. Thus
\[
\boxed{\begin{gathered}
c_0\in F^*,\qquad \tau\in F,\qquad
T=t+\tau,\qquad
\delta=\frac{c_0}{T},\quad \beta=\frac{c_0}{T^2},\\
e=\frac{H_0}{T^3}-\frac1{2T^2},\qquad
\mathcal C=\frac{2c_0^2H_0}{T^5},\qquad
H_0\in F^*,\qquad \kappa=\frac{2H_0}{T}.
\end{gathered}}
\tag{19}
\]
The last nonzero assertion follows from the already nonzero
curvature. Here F means only the exact constant field of the
indicated derivation. No rationality of F, equality L=F(t), or
complexity of tau,c0,H0 is asserted. These definitions avoid any
assumption that arbitrary antiderivatives exist inside L.

## 7. Scope and verification

The two high-Q gates apply to all six profiles in(3), not only
the cubic profile. Their validity depends on r>=1, r<m<d and
d+r=2m. In particular this proof does not apply unchanged to
the former r=0 quadratic cases, where lower quadratic terms
can tie with the second comparison.

This note supplies no collision theorem, no full-profile
exclusion, no original-coordinate recognition and no entry
theorem for an arbitrary cancellation candidate. Any later
composition with an all-X polynomial-generation obstruction
must separately establish its exact hypotheses. The genuine
levels, full scalar and both actual returns remain imposed,
not converses to the necessary coefficient equations.

Current417 was completely read in5bfd00 and rehashed in985590
at8dcb3d8d462fc9e551f44df192a989147f92d67251221287ea1465a47772dc4f.
Current413 was completely reread in69850a and its unchanged
hash checked in60a5c3. The complete365 source was freshly read
inaca0ba;407 was fully read ineed0ec+5a4c1a and its unchanged
hash revalidated in60a5c3. The writing guide was read through
865fe0 before authoring.

Fresh unsaveddb4dd1 rebuilt(10) from the original cubic tensor,
using precisely(8),(9). It then checked the complete degree-eight
and degree-seven coefficients in the cubic profile while retaining
all lower polynomial coefficients; every residual was zero.
The symbol xi in that calculation was simply a formal name for
lambda, not a choice of coefficient basis. The proof of the
all-profile extension is the strict degree comparison above.
Fresh13f25a independently verified both differential identities
in(17),(18) and the strict degree gaps in every listed profile.

No saved checker was executed, imported, compiled or rerun.
No earlier source or canonical index was edited. This is a
scoped necessary reduction, not unrestricted cancellation,
novelty, human-expert review or formal certification.
