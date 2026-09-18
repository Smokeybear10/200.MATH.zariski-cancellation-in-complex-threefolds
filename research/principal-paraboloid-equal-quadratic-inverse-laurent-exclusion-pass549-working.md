# Exclusion of the inverse-Laurent noncomplex equal-quadratic branch

Working conditional result: retain the FULL actual264/296/535 chart,
noncomplex \(m=k_s\ne0\), and the q-zero equal-quadratic sector with
noncomplex quadratic y coefficient treated in547. After its licensed
complex normalizations, the inverse-Laurent alternative is impossible.

This note concerns ONLY the alternative with zero linear y coefficient
and a nonzero inverse-power Laurent coefficient. It does not transfer
any determinant calculation to the nonzero-linear-y branch. In
particular the linear Z term retained throughout is \(mdx\), because
the present branch has b zero; before that restriction the original
linear term would be \((2tb+md)x\).

## 1. Full actual input and normalization of the rigid leaders

Retain every hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md),
and [535](principal-paraboloid-nonlinear-sigma-unit-multiplier-pass535-working.md).
In particular
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u_{\rm glob}],\quad
E=\partial_{u_{\rm glob}},\quad X=a_0u_{\rm glob}+x_0,\quad a_0\ne0,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\quad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the ENTIRE original initial kernel},\\
0\ne N=[u_{\rm glob}^4]\partial_Z|_A\in\operatorname{LND}(A),
\quad Na_0=Nt=Ns=0,\quad Nv=1,\\
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,
\quad O=L[A]=L[v]=L[y,\sigma,\theta],\\
\operatorname{Frac}A=L(v)=\mathbb C(y,z_{\rm int},w),\quad
L[y,z_{\rm int},w]=L[v],\quad J_{t,s,v}(X)=-a_0^4\in L^*.
\end{gathered}
\tag{1}
\]
Here \(z_{\rm int}\) is the literal Z-intercept. The original slice,
selected partial, both returns, and complete genuine gradient-unit
conditions remain required.

Use the finite intrinsic affine normalization
\(x=\rho(v-v_0)\), \(\rho^2\in L^*\), of545/547. It is not an
actual coordinate map. Coefficient partials fix x; the full scalar is
\(-a_0^4/\rho\), \(Nx=\rho\), and535 has multiplier
\(\kappa=\kappa_v/\rho^2\in L^*\). Write
\[
\sigma=x^2+c,\quad \theta=\mu x^2+d x+e,\quad
y=a x^2+b x+C,
\quad \mu d\ne0.
\tag{2}
\]
The d-zero boundary was excluded for noncomplex m by the retained
double-cover calculation303. Put
\[
p=m_t,\quad h=m_s,\quad q=p+h\mu=0,\quad
\Phi=k_{tt}+2p\mu+h\mu^2,\quad \chi=(4a+\Phi)/m,
\quad \mathcal D=\partial_t+\mu\partial_s.
\tag{3}
\]
Here \(h\ne0\). The present input is the noncomplex-a conclusion of
[547](principal-paraboloid-equal-quadratic-zero-characteristic-reflection-rigidity-pass547-working.md):
\(a=\alpha/m+\beta\), \(\chi=2\alpha/m^2+\delta\), with
\(\alpha\in\mathbb C^*\), \(\beta,\delta\in\mathbb C\).

Both constant terms can be removed by ACTUAL maps of426. First use
\(X_1=X+\beta\), leaving Y,Z,W unchanged. Its transported quantities
satisfy
\[
\sigma_1=\sigma-2\beta t,\quad
\theta_1=\theta-2\beta s,\quad
y_1=y-\beta\sigma+\beta^2t,\quad k_1=k+2\beta t^2.
\]
Thus its quadratic y coefficient is \(a-\beta\), while m,q,mu and
chi are unchanged. Next use \(W_2=W_1+\delta Z_1/2\), fixing the
other three actual coordinates. Then \(s_2=s+\delta t^2/2\),
\(\mu_2=\mu+\delta t\), \(p_2=p-\delta th\),
\(q_2=q\), \(\chi_2=\chi-\delta\), and
\(\mathcal D_2=\mathcal D\).

These maps have complex coefficients and polynomial inverses. They
preserve the full initial kernel and exact time degrees. The first
preserves the selected Z partial literally. For the second,
\(\partial_{Z_2}=\partial_{Z_1}-(\delta/2)\partial_{W_1}\), and the
retained omitted-W shift bound gives the same selected leading N.
The original a0, global slice, original N-slice and field L are
unchanged. The actual localized quotient
\(\mathcal B_{a_0}=A_{a_0}[X_2]\) supplies both literal intercept
returns. Row and parameter determinants give the unchanged full
scalar. These are exactly the actual licenses of426, not coefficient-
field substitutions promoted to ambient maps.

Drop subscripts after this normalization. We have
\[
\boxed{a=\alpha/m,\qquad \chi=2\alpha/m^2,\qquad
       \Phi=-2a,\qquad q=0.}
\tag{4}
\]
In particular \(\mathcal D\mu=-\chi\ne0\), so theta remains
quadratic. The intrinsic affine center is still legitimate and d
remains nonzero. No full-chart property will be claimed after the
later unfiltered U shear solely on the basis of these maps.

## 2. The exact inverse-Laurent branch

The complete all-X ledger of545 uses
\(\nu_0=\{h(e-\mu c)+n_s\}/m\) and gives, when q zero,
\[
\mathscr L(u)=bu+\Lambda_0+
          \frac{md}{u}(\nu_0-a-\Phi/2),
\quad
\Lambda_0=2C-a(2c+k_t+m\mu)-\Phi(k_t+m\mu)/2
                         +\mu n_s+n_t+hd^2/2.
\tag{5}
\]
The full all-X divided-difference return forces this Laurent
polynomial to be a nonzero monomial, including diagonal pair roots.
Since (4) makes \(a+\Phi/2=0\), the inverse alternative is precisely
\[
\boxed{b=0,\qquad \Lambda_0=0,\qquad \nu_0\ne0.}
\tag{6}
\]
Thus \(y=ax^2+C\), and
\(n_t=-2C+2ac-\mu n_s-hd^2/2\). No constant or linear Laurent
branch is included in this note.

All subsequent calculations use the full literal rows
\[
\begin{aligned}
Y&=y+\sigma X+tX^2,\\
Z&=2ty+\sigma^2+k_t\sigma+m\theta+n
                         +(2t\sigma+k)X+t^2X^2,\\
W&=w+\theta X+sX^2,\\
mw&=\ell-(2\sigma+k_t)y-F(\sigma,\theta),\\
F(P,V)&=k_{tt}P^2/2+pPV+hV^2/2+n_tP+n_sV,
\end{aligned}
\tag{7}
\]
and the complete formal H and535 polynomials printed in547. Their
lower coefficients are not replaced by an arbitrary top-degree ansatz.

## 3. The nonzero derivative of the affine theta coefficient

The complete q-zero high identities from547 are
\(\mathcal Da=\mathcal Dm=\mathcal D\chi=0\) and
\(\mathcal D\mu=-\chi\). The third-degree coefficients of the
same full polynomials, now under b zero, are
\[
f_3=-2hd/m,\qquad g_3=-hd\mu_s,\qquad
(\mathcal A_{\sigma_x})_3=2d a_s,\qquad
(\mathcal B_{\sigma_x}+\kappa f)_3
          =4\mathcal Dd+2d\mu_s-2\kappa hd/m.
\tag{8}
\]
Here \(a_s=-\alpha h/m^2\), so the full multiplier gives
\[
\kappa\mu_s=\chi,\qquad
2\mathcal Dd=d(\kappa h/m-\mu_s).
\tag{9}
\]
In particular \(\mu_s\ne0\). We claim
\[
\boxed{\mathcal Dd\ne0.}
\tag{10}
\]
If it vanished, (9) would give \(\mu_s=\kappa h/m\).
The commutator \([\mathcal D,\partial_s]=-\mu_s\partial_s\)
and (4) give
\[
\mathcal Dh=-h\mu_s,\qquad
\mathcal D\mu_s=-\chi_s-\mu_s^2
                       =2\chi h/m-\mu_s^2=\mu_s^2.
\]
On the other hand the two equations in (9) now give
\(\mu_s^2=\chi h/m\). Its derivative is
\(2\mu_s\mathcal D\mu_s=-\mu_s^3\), so
\(\mathcal D\mu_s=-\mu_s^2/2\), a contradiction. All divisions
here are by the explicitly nonzero h,m,d,kappa,chi or mu_s; no
square-root descent is used.

## 4. The actual X-zero fiber and its entire quadratic U row

Make the ACTUAL polynomial coordinate shear
\[
U=Y^2+\alpha W,
\qquad (X,Y,Z,U)\text{ is a coordinate frame},\qquad
W=(U-Y^2)/\alpha.
\tag{11}
\]
It has row determinant alpha. It need not preserve the full1222
profile, and no such preservation is asserted or needed.
Evaluate only at the fixed actual coordinate value X zero, after
forming the full rows and their derivatives. The scalar there is
still a coefficient-field unit. Denote the resulting rows by Y,Z,U.

Since \(h\ne0\), exact coefficient coordinates \((t,m)\) are
licensed, and \(\mathcal D=\partial_t|_m\). Extend this basis to
\(L'=L(\rho)\); let \(F_0=\ker_{L'}\mathcal D\), finite algebraic
over \(\mathbb C(m)\). It is not assumed rational. The commuting
\(\partial_m|_t\) restricts to the unique m derivation of \(F_0\).
Coefficients carrying rho may belong only to this extended field.

The full potential in (7), with (4),(6), cancels the entire quartic
and cubic terms of U. Explicitly put
\[
\begin{gathered}
F_1=2C-a(2c+k_t),\qquad
L_1=-\alpha d\nu_0\ne0,\qquad
R_1=C^2+\alpha w_0-F_1C,\\
Z_2=2ta+2c+k_t+m\mu,\qquad
Z_0=2tC+c^2+k_tc+me+n.
\end{gathered}
\tag{12}
\]
Here \(w_0\) is the full constant coefficient of w, with ell and
all lower potentials retained. The entire fiber rows are
\[
\boxed{Y=ax^2+C,\quad
Z=x^4+Z_2x^2+mdx+Z_0,\quad
U=F_1Y+L_1x+R_1.}
\tag{13}
\]
In particular the term \(mdx\) is present. At this point
\(F_1,L_1,R_1\) may depend on both coefficient parameters.
The literal formulas imply
\[
\mathcal DZ_2=(2\mathcal DC-\mathcal DF_1)/a.
\tag{14}
\]
For example \(\mathcal Dk_t=\Phi=-2a\), so differentiating (12)
directly proves (14); it is not a selected scalar constraint.

The complete scalar in this basis is
\[
J_{t,m,x}(Y,Z,U)=-\frac{\alpha a_0^4}{h\rho}\in(L')^*.
\tag{15}
\]
It need not be complex constant. It is independent of the intrinsic
parameter x. This follows from the actual row factor alpha, the
exact parameter factor h and the intrinsic factor rho.

Subtract \(F_1\) times the Y row from the U row of the differential
matrix. A dot denotes \(\mathcal D\), and the m partial fixes t.
The entire determinant in (15) becomes
\[
\det\begin{pmatrix}
\dot C&a_mx^2+C_m&2ax\\
\dot Z_2x^2+m\dot d x+\dot Z_0&
 (Z_2)_mx^2+(d+md_m)x+(Z_0)_m&4x^3+2Z_2x+md\\
\dot F_1Y+\dot L_1x+\dot R_1&
 (F_1)_mY+(L_1)_mx+(R_1)_m&L_1
\end{pmatrix}.
\tag{16}
\]
This matrix retains every derivative of every lower coefficient.
Its successive high coefficients, using \(a=\alpha/m\), are
\[
\begin{aligned}
[x^7]J&=-4\alpha^2\dot F_1/m^3,\\
[x^6]J\big|_{\dot F_1=0}&=-4\alpha\dot L_1/m^2,\\
[x^5]J\big|_{\dot F_1=\dot L_1=0,\ (14)}
                         &=-4\alpha\dot R_1/m^2.
\end{aligned}
\tag{17}
\]
Thus
\[
F_1,L_1,R_1\in F_0,\qquad
\mathcal D(d\nu_0)=0,\qquad
\dot Z_2=2\dot C/a.
\tag{18}
\]
The quadratic coefficient of U is \(aF_1\) and is also a
\(\mathcal D\)-constant. Neither (17) nor (18) uses any B-nonzero
branch formula.

## 5. Zero-safe fourth coefficient and exact integrations

In the rest of the proof write \(F=F_1\), \(L_c=L_1\), \(R=R_1\)
to distinguish the scalar coefficient \(L_c\) from the original
field L. The complete fourth coefficient of (16) is
\[
[x^4]J=\frac2m\{L_c\dot C+\alpha^2F_m\dot d\}.
\tag{19}
\]
We must first rule out \(F_m=0\). In that case \(L_c\ne0\)
forces \(\dot C=0\), and (18) forces \(\dot Z_2=0\). Then the
ENTIRE determinant (16), not merely a high coefficient, factors as
\[
(m\dot d x+\dot Z_0)
\left\{Y_x((L_c)_mx+R_m)-L_c(a_mx^2+C_m)\right\}.
\tag{20}
\]
The first factor is a nonconstant polynomial because \(m\dot d\ne0\).
If the other factor vanishes, J is zero; otherwise the product has
positive intrinsic degree. Both contradict (15). Consequently
\[
F_m\ne0,\qquad
\lambda=-\alpha^2F_m/L_c\in F_0^*,\qquad
C=\lambda d+C_0,\quad C_0\in F_0.
\tag{21}
\]
The last equality integrates (19) by subtraction. In particular
\(\dot C\ne0\), with no division by an unproved nonzero quantity.

Equation (18) next gives
\(Z_2=2\lambda d/a+K\), \(K\in F_0\). The entire third coefficient
of (16), after (18), is
\[
[x^3]J=2a^2F_m\dot Z_0-2a\dot C F_mZ_2
                  +\alpha\dot d\{2(L_c)_m+L_c/m\}.
\tag{22}
\]
Therefore
\[
\begin{gathered}
Z_0=Z_2^2/4+\tau d+G_0,\qquad G_0\in F_0,\\
\tau=-\frac{m^2\{2(L_c)_m+L_c/m\}}{2\alpha F_m}\in F_0.
\end{gathered}
\tag{23}
\]
There is no requirement that tau, K, C0, G0 or their derivatives be
nonzero. These integrations require only the proved field-unit
denominators, and leave every other lower coefficient unrestricted.

## 6. The full determinant in the separating pair (d,m)

By (10), d is transcendental over \(F_0\), and \((d,m)\) is a
separating coefficient basis. The extended coefficient field is
finite over \(\mathbb C(d,m)\). Its new \(\partial_m|_d\) agrees
with the former m derivative on every element of \(F_0\), because
their difference is a multiple of \(\mathcal D\). Thus all m
derivatives of \(\lambda,F,L_c,R,C_0,K,\tau,G_0\) below are their
genuine exact derivatives, not formally frozen coefficients.

The complete rows are now
\[
\begin{aligned}
Y&=a x^2+\lambda d+C_0,\\
Z&=Q^2+mdx+\tau d+G_0,\qquad
Q=x^2+\lambda d/a+K/2,\\
U&=FY+L_cx+R,
\qquad a=\alpha/m.
\end{aligned}
\tag{24}
\]
The calibrated scalar is
\[
J_{d,m,x}=-\frac{\alpha a_0^4}{h\rho\dot d}\in(L')^*,
\tag{25}
\]
still allowed to depend on the coefficient parameters. The full
matrix after subtracting F times the first row is
\[
\det\begin{pmatrix}
\lambda&a_mx^2+\lambda_m d+(C_0)_m&2ax\\
2Q\lambda/a+mx+\tau&2QQ_m+dx+\tau_m d+(G_0)_m&4xQ+md\\
0&F_mY+(L_c)_mx+R_m&L_c
\end{pmatrix}.
\tag{26}
\]
In particular the derivative of the full \(mdx\) term contributes
both mx and dx in the indicated entries.

Expanding the whole (26), its x-squared coefficient is
\[
[x^2]J=
\left(\alpha\lambda F_m+\frac{4L_c\lambda^2}{\alpha}\right)d
 +J_{20},
\tag{27}
\]
where all lower terms are retained in
\[
\begin{aligned}
J_{20}={}&2\alpha C_0F_m+2\alpha R_m
 +\frac{2\alpha\tau(L_c)_m}{m}
 +\frac{\alpha L_c\tau}{m^2}\\
&+L_c\lambda K_m+\frac{KL_c\lambda}{m}
 -\frac{2mL_c\lambda(C_0)_m}{\alpha}\in F_0.
\end{aligned}
\tag{28}
\]
Substitute (21). The coefficient of d in (27) is exactly
\[
\boxed{[d][x^2]J=\frac{3\alpha^3F_m^2}{L_c}\ne0.}
\tag{29}
\]
Since d is transcendental over \(F_0\), the full x-squared
coefficient cannot vanish. This contradicts the x-independent
nonzero scalar (25). The contradiction never sets the allowed
constant-in-x scalar to zero. It proves the claimed inverse-Laurent
exclusion.

## 7. Verification and precise scope

This proof uses the HELD rigidity source547, its full actual inputs,
and the actual transformation family426. It does not use any
unfinished source or any determinant computed in the B-nonzero
branch. The original field and its finite intrinsic square-root
extension are kept distinct. In particular d and \(L_c\) need not
descend individually, although their paired occurrence in the actual
rows does. No rationality of \(F_0\), ambient inversion of m, or
ambient promotion of the intrinsic coefficient parameter is made.

Fresh unsaved23f3d2 reconstructs the complete U row from the full
potential (7), the f/g cubic coefficients and both full535 cubic
coefficients in (8); all residuals are zero. Fresh e1c1c4 reconstructs
the ENTIRE generic matrix (16), its successive coefficients (17),
and the fourth/third coefficients (19),(22). Fresh a06bf4 reconstructs
the whole determinant from (24), with every genuine m derivative,
and gives exactly (27),(28); final fresh c3955e checks the entire
printed x-squared coefficient and its substitution (29). All polynomial
identities checked have zero residual. The commutator argument,
finite-field licenses, zero-safe factor case and calibrated scalar
contradiction are the written proofs above.

Only this new bounded source was authored. No saved checker was
executed, imported, compiled or rerun, and no earlier source or
canonical file was edited. No broader equal-quadratic recognition,
nonlinear-sigma classification, arbitrary chart entry, cancellation,
novelty or external certification is claimed. Complete independent
saved-source review remains separate from author verification.
