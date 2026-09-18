# Quartic excess forces an impossible even polynomial return

## 1. Conditional statement and full actual inputs

Retain EVERY actual hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md)
and
[535](principal-paraboloid-nonlinear-sigma-unit-multiplier-pass535-working.md).
The conclusion of this note is that the intrinsic degree profile

\[
 (\deg\sigma,\deg\theta,\deg y)=(2,4,6)
 \tag{1}
\]

is impossible. In particular this excludes the quartic excess exception
in the noncomplex-coupling degree bound553. It supplies no entry to the
chart from arbitrary cancellation data and no recognition of other
intrinsic profiles.

Here the actual ambient ring, original slice and selected derivation are

\[
 \begin{gathered}
 B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad
 X=a_0u+x_0,\quad a_0\ne0,\\
 \deg_E(X,Y,Z,W)=(1,2,2,2),\qquad
 I_{\rm original}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
       \text{ is the entire original initial kernel},\\
 0\ne N=[u^4]\partial_Z|_A\in\operatorname{LND}(A),\qquad
 Na_0=Nt=Ns=0,\qquad Nv=1,\\
 L=\operatorname{Frac}\ker_A N,\qquad [L:\mathbb C(t,s)]<\infty,\\
 L[A]=L[v]=L[y,\sigma,\theta],\qquad
 \operatorname{Frac}A=L(v)=\mathbb C(y,z_{\rm int},w),\qquad
 L[y,z_{\rm int},w]=L[v].
 \end{gathered}
 \tag{2}
\]

The intercept \(z_{\rm int}\) is the literal original Z-intercept.
Both returns, all moving levels, the original slice and the full scalar
are retained. In particular \(t,s\) are algebraically independent.

Use553's finite coefficient extension and affine intrinsic normalization,
not a transformation of the actual coordinates. For a finite field
\(L'\supset L\), write \(x=\rho v+\zeta\), with \(\rho\in L'^*\).
The coefficient partials are the exact commuting extensions of the
\(t,s\) partials to \(L'\), extended to fix \(x\). Then

\[
 \begin{split}
 \sigma&=x^2+c,\\
 \theta&=ax^4+bx^3+dx^2+ex+f,\\
 y&=rx^6+qx^5+y_4x^4+y_3x^3+y_2x^2+y_1x+y_0,
             \qquad ar\ne0,\\
 Nx&=\rho,\qquad L'[y,\sigma,\theta]=L'[x].
 \end{split}
 \tag{3}
\]

The last equality follows by extending the exact polynomial return (2);
it is not a rational inverse assertion. All displayed coefficients lie
in \(L'\). No rationality of this finite field is assumed. Put
\(m=k_s\ne0\), \(p=m_t\) and \(h=m_s\). We initially allow \(h=0\).

## 2. Entire potentials and equations used

The complete literal rows are

\[
 \begin{split}
 Y&=y+\sigma X+tX^2,\\
 Z&=2ty+\sigma^2+k_t\sigma+m\theta+n
                         +(2t\sigma+k)X+t^2X^2,\\
 W&=w+\theta X+sX^2.
 \end{split}
 \tag{4}
\]

For independent formal variables \(U,P,V\), define

\[
 \begin{split}
 F(P,V)&=\frac{k_{tt}}2P^2+pPV+\frac h2V^2+n_tP+n_sV,\\
 G(U,P,V)&=\frac{\ell-(2P+k_t)U-F(P,V)}m,\\
 H(U,P,V)&=U^2+F_PU+F_VG
       +\frac{k_{ttt}}6P^3+\frac{p_t}2P^2V
       +\frac{h_t}2PV^2+\frac{h_s}6V^3\\
   &\hspace{12mm}+\frac{n_{tt}}2P^2+n_{ts}PV
                   +\frac{n_{ss}}2V^2-\ell_tP-\ell_sV.
 \end{split}
 \tag{5}
\]

Thus \(w=G(y,\sigma,\theta)\) and
\(H(y,\sigma,\theta)=h_0\in L'\). Formal derivatives are taken
BEFORE evaluation. Write \(H_U^{\rm ev},H_V^{\rm ev}\) for them, and set

\[
 \begin{gathered}
 B_f=\frac{2y+k_{tt}\sigma+p\theta+n_t}{m},\quad
 D_f=\frac{2\sigma+k_t}{m},\quad
 \nu=\frac{p\sigma+h\theta+n_s}{m},\\
 A_\beta=4x^2y_t+2x\theta_xy_s+y_x^2
                         -2xc_ty_x-c_sy_x\theta_x,\\
 B_\beta=4x^2(\theta_t+B_f)+2xD_fy_x+y_x\theta_x
               +2x(\theta_s+\nu-c_t)\theta_x-c_s\theta_x^2,\\
 A_\beta=\kappa H_V^{\rm ev},\qquad
 B_\beta=-\kappa H_U^{\rm ev},\qquad \kappa\in L'^*,\\
 J_{t,s,x}(Y,Z,W)=-a_0^4/\rho\in L'^*.
 \end{gathered}
 \tag{6}
\]

These are the full535 multiplier identities after the licensed intrinsic
change. Both multiplier polynomials scale by \(\rho^{-2}\); the genuine
moving-center and moving-scale terms cancel by the full chain rule.
No division by \(2x\) or an evaluated gradient component is made.
The scalar is independent of \(x,X\), not assumed complex constant.

## 3. The entire initial kernel forces two leading cancellations

The full second potential in (5) gives

\[
 w_8=[x^8]w=-\frac{ha^2+4r}{2m},\qquad
 w_7=[x^7]w=-\frac{2q+hab}{m},\qquad \deg_x w\le8.
 \tag{7}
\]

We prove both coefficients are zero using the actual ring, rather than
postulating cancellation. Put \(K=\mathbb C(X)\) and
\(R=K[Y,Z,W]\), the actual polynomial three-ring. Extend \(N\) to
\(A[u]\) by \(Nu=0\), and define

\[
 \Delta=a_0N-(NX)E.
 \tag{8}
\]

This fixes X and restricts to \(a_0N\) on A. It is locally nilpotent:
\(\Delta^j u=-a_0^{j-1}N^jx_0\) for \(j\ge1\), and these derivatives
eventually vanish. Localization at nonzero polynomials in the invariant
X preserves local nilpotence. The resulting derivation on R is nonzero;
on the finite overfield \(L'(X)(x)\) it is
\(a_0\rho\partial_x\), killing \(L'(X)\).
The local-slice argument gives
\(\operatorname{trdeg}_K\ker_R\Delta=2\), so R has a nonconstant
polynomial invariant of intrinsic x-degree zero.

The exact return in (2) identifies \(\operatorname{Frac}R\) with
\(L(v)(X)\). Its finite separable overfield \(L'(X)(x)\) is used only
for coefficient derivatives and degree calculations. Actual coordinate
partials extend uniquely; no equality with the overfield is asserted.

The Y and Z rows in (4) have exact degrees six and six, with initials
\(r\eta^6\) and \(2tr\eta^6\). These are algebraically independent
over K: their ratio is \(2t\), and the coefficient variable t and the
grading variable \(\eta\) are independent of the actual X.
Suppose W has positive intrinsic degree D. All three generator degrees
are then positive. The highest source-weight part of a nonconstant
\(\Delta\)-invariant supplies a nonzero initial relation. Therefore
the ENTIRE initial kernel in \(K[\widehat Y,\widehat Z,\widehat W]\)
is a height-one prime, generated by a weighted homogeneous irreducible
\(H_{\rm in}\) involving \(\widehat W\).

Let \(T_W\) be the actual partial fixing X,Y,Z. Cramer's rule in
\((t,s,x)\), together with (6), gives coefficient degree bounds eleven
for its t and s components, and twelve for its x component. Hence for
every nonzero polynomial in \(L'(X)[x]\),

\[
 \deg_x T_W f\le \deg_x f+11.
 \tag{9}
\]

The denominator is the coefficient-field unit in (6). All iterates
remain polynomials over this field, so the same bound applies repeatedly.
For a nonconstant invariant f, write its source-weight top as
\(H_{\rm in}^{\ell}G_0\), where \(H_{\rm in}\nmid G_0\), of weight M.
Since \(H_{\rm in}\) involves W, its W derivative is nonzero modulo
the full initial prime. Exactly \(\ell\) derivatives therefore give
a surviving initial polynomial, while lower source-weight parts remain
strictly lower. Consequently

\[
 \deg_x T_W^\ell f=M-D\ell\le11\ell,
 \qquad \operatorname{wt}H_{\rm in}\le D+11.
 \tag{10}
\]

Independence of the Y,Z initials requires at least two W blocks in a
homogeneous relation. Their W exponents differ by a positive multiple
of \(6/\gcd(6,D)\). Thus

\[
 \operatorname{wt}H_{\rm in}\ge\operatorname{lcm}(6,D).
 \tag{11}
\]

If \(w_8\ne0\), the literal W row has D=8. Equations (10)--(11)
would give \(24\le19\), impossible. If \(w_8=0\) but \(w_7\ne0\),
it has D=7, giving \(42\le18\), also impossible. The additions
\(\theta X+sX^2\) have degree at most four and cannot affect these
two conclusions. Therefore

\[
 w_8=w_7=0,\qquad
 r=-\frac{ha^2}{4},\qquad q=-\frac{hab}{2},\qquad h\ne0.
 \tag{12}
\]

The last nonvanishing follows from r nonzero, so the h=0 boundary is
excluded without dividing by h prematurely. No relation coefficients
were assumed complex rather than in K, and no lower W profile is
discarded or classified in this argument.

## 4. Whole high coefficients kill the first odd terms

Expansion of the complete expressions (5)--(6), with ALL lower
coefficients present, gives

\[
 \begin{split}
 [x^{12}]H^{\rm ev}
    &=r^2-\frac{2har}{m}
                +a^3\left(\frac{h_s}{6}-\frac{h^2}{2m}\right)=0,\\
 [x^8](B_\beta+\kappa H_U^{\rm ev})
    &=24ar+8aa_s+\frac{8ha^2}{m}+\frac{32r}{m}=0,\\
 [x^{10}](A_\beta-\kappa H_V^{\rm ev})&=8ar_s+36r^2=0.
 \end{split}
 \tag{13}
\]

These are553's full quartic excess coefficients, independently expanded
here. Substituting (12) in the first two gives

\[
 a_s=\frac34ha^2,\qquad h_s=-\frac38h^2a,
 \qquad r_s=-\frac9{32}h^2a^3.
 \tag{14}
\]

The formula for r_s is also the genuine derivative of (12); it agrees
with the last equation of (13). In particular no leading derivative is
treated as an independent jet after these identities are imposed.

The complete next H coefficient, after (12)--(14), is

\[
 [x^{11}]H^{\rm ev}=\frac1{16}a^3bh^2=0.
 \tag{15}
\]

Thus b=0 and q=0 as coefficient-field identities. Their genuine partials
are now zero. This is a proved consequence, not an evenness assumption.

## 5. Genuine compatibility kills every remaining odd term

Keep c,d,f,y4,y2,y0 and every lower potential unrestricted. Define

\[
 \begin{split}
 \mathcal O&=ahe(3am+16)+8(am+4)y_3,\\
 \mathcal J&=5aeh+4am e_s+(6am+10)y_3,\\
 \mathcal K&=9a^2eh^2+144ah y_3-128(y_3)_s.
 \end{split}
 \tag{16}
\]

After precisely (12)--(15), three coefficients of the ENTIRE equations
are

\[
 [x^9]H^{\rm ev}=-\frac{ah}{16m}\mathcal O,
 \qquad [x^5](B_\beta+\kappa H_U^{\rm ev})=\frac2m\mathcal J,
 \qquad [x^7](A_\beta-\kappa H_V^{\rm ev})=-\frac a{16}\mathcal K.
 \tag{17}
\]

All three vanish. No term containing a lower potential or an optional
coefficient has been removed by an extra hypothesis in this collection.

First, \(am+4\ne0\). Otherwise its genuine s derivative, using
\(m_s=h\) and (14), would be

\[
 0=(am)_s=\frac{ah}{4}(3am+4)=-2ah\ne0.
 \tag{18}
\]

We may therefore solve the three zero equations in (17) as

\[
 y_3=-\frac{ahe(3am+16)}{8(am+4)},\qquad
 e_s=-\frac{5aeh+(6am+10)y_3}{4am},\qquad
 (y_3)_s=\frac{9a^2eh^2+144ah y_3}{128}.
 \tag{19}
\]

Differentiate the full first polynomial \(\mathcal O\) in (16).
Before substitution this derivative is

\[
 \begin{split}
 \mathcal O_s={}&(a_she+ah_se+ah e_s)(3am+16)
     +3ahe(a_sm+ah)\\
 &+8(a_sm+ah)y_3+8(am+4)(y_3)_s.
 \end{split}
 \tag{20}
\]

Using (14), \(m_s=h\), and all of (19), exact collection gives

\[
 0=\mathcal O_s=-\frac{39a^3eh^2m}{16(am+4)}.
 \tag{21}
\]

Every factor other than e is already nonzero. Hence e=0, and (19)
gives y3=0, without dividing by either of them or by \(3am+16\).
The entire next needed H coefficient then simplifies to

\[
 [x^7]H^{\rm ev}=-\frac{ah(am+4)}{2m}y_1=0.
 \tag{22}
\]

It follows that y1=0. The independent zero boundary \(p=m_t=0\) and
all zero optional coefficients remain covered; none was divided out.

## 6. The actual polynomial return gives the contradiction

Equations (15), (21) and (22) have proved that

\[
 \sigma=x^2+c,\qquad
 \theta=ax^4+dx^2+f,\qquad
 y=rx^6+y_4x^4+y_2x^2+y_0.
 \tag{23}
\]

Thus all three generators lie in the proper subring \(L'[x^2]\) of
\(L'[x]\). The subring is proper because x is a transcendental variable
over the characteristic-zero coefficient field: no polynomial in x²
equals x. This contradicts the exact return in (3). The profile (1)
is impossible.

## 7. Verification and scope

The complete direct sources264,296,535 and553 were read through EOF.
The actual-ring initial-kernel and finite-overfield licenses were also
checked against the complete held571, but its cubic exclusion is not
a dependency of this quartic proof.

Fresh unsaved28b214, completed inbd7470, reconstructed the entire formal
H before both gradients, the full second potential and both multiplier
polynomials, retaining all lower coefficients. Freshf45a4c checked the
genuine compatibility (20)--(21) and the boundary (18). The separate
fresh reconstruction14fbfb used unrestricted formal symbols throughout
and verified thirteen exact zero residuals covering (7), (13)--(15),
(17)--(22), and the genuine derivative of r. The first reconstruction's
symbol-assumption choices were not used as mathematical hypotheses.

An independent AI outline review reconstructed the whole high system
and cofactor bounds in93e83f, and the entire odd-coefficient elimination
and genuine derivative in723cdc. Its conceptual review checked the
ENTIRE initial prime, exact relation multiplicity, actual LND and finite
coefficient extension. This outline review is not substituted for a
separate complete saved-source review of this file after author hold.

The proof does not specialize a moving root, discard the critical point
of sigma, promote the intrinsic x to an actual coordinate, or replace
the full initial kernel by a chosen relation. It retains the original
selected literal partial and original global slice. All historical
inputs remain explicit rather than being recursively recertified.

This result is conditional on the supplied actual chart. Lower-y
quartic cases, the other intrinsic profiles, arbitrary chart entry and
unrestricted cancellation are not solved by it. No historical novelty,
human expert review or proof-assistant certification is claimed.
No saved checker was executed, imported, compiled or rerun. No external
contact, publication or submission occurred.
