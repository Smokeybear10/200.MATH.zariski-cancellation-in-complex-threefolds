# Conic and differential restrictions in the surviving transverse profile

Working necessary reduction: retain the FULL actual264/296/535
chart, the h nonzero, v1=0 cubic-excess family554, and the
noncomplex-T0 branch of556. The remaining degree-(4,4,4) profile
has a FULL coordinate-initial kernel generated over C by an
irreducible homogeneous quadratic. In particular
\[
(w_4)_s=0.
\tag{1}
\]
The genuine next coefficients also force
\[
h_t=-a^2h^2/8\ne0,\qquad
(b_2)_s=\frac{h_{tt}}{2h_t},\qquad
\kappa=\frac{5m}{2h}
               \left(\frac{h_{tt}}{h_t}+\frac{4h_t}{h}\right)\ne0.
\tag{2}
\]
These are restrictions on the remaining conic case, not an exclusion
or realization. The complex-T0 boundary remains outside the claim.
No rationality of the conic parametrization or coefficient field is
asserted.

## 1. Retained actual chart and coefficient conventions

Retain EVERY actual hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md)
and
[535](principal-paraboloid-nonlinear-sigma-unit-multiplier-pass535-working.md),
including the original global slice, exact time profile, ENTIRE
initial kernel, selected literal partial, both actual returns,
genuine moving levels and full calibrated scalar. Explicitly,
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=\mathcal A[u],\quad
E=\partial_u,\quad X=a_0u+x_0,\quad a_0\ne0,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\qquad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2),\\
0\ne N=[u^4]\partial_Z|_{\mathcal A},\quad
Na_0=Nt=Ns=0,\quad Nv=1,\\
L=\operatorname{Frac}\ker_{\mathcal A}N,\quad
[L:\mathbb C(t,s)]<\infty,\quad
L[\mathcal A]=L[v]=L[y,\sigma,\theta],\\
\operatorname{Frac}\mathcal A=L(v)=\mathbb C(y,z_{\rm int},w),
\qquad m=k_s\notin\mathbb C.
\end{gathered}
\tag{3}
\]
The intercept z_int is the literal original Z-intercept. No original
global slice is replaced by X/a0.

Use the finite intrinsic normalization and necessary coefficient
family of
[554, Section 3.2](principal-paraboloid-cubic-excess-leading-families-pass554-working.md).
In L'=L(rho), with x affine in the original v, write
\[
\begin{gathered}
\sigma=x^2+c,\quad Nx=\rho\in(L')^*,\quad
\theta=ax^3+b_2x^2+d x+e,\\
y=rx^4+q_3x^3+y_2x^2+y_1x+y_0,\qquad
F_0=\ker_{L'}\partial_s,\\
a,r\in F_0^*,\quad h=m_s=-4r/a^2\in F_0^*,\quad
m=hs+m_0,\quad m_0\in F_0,\quad p=m_t.
\end{gathered}
\tag{4}
\]
All coefficient partials are the exact commuting extensions from
C(t,s), extended to fix x. They retain moving-center and moving-scale
terms. F0 is finite over C(t), not assumed rational; its t constants
are C. In particular h_s=a_s=r_s=0 and p_s=h_t.

Let w_i=[x^i]w and assume
\[
T_0=2t+1/r\notin\mathbb C.
\tag{5}
\]
The independently derived restriction
[556](principal-paraboloid-cubic-transverse-degree-profile-restriction-pass556-working.md)
gives w5=0 and w4 nonzero. The full original rows remain
\[
\begin{aligned}
Y&=y+\sigma X+tX^2,\\
Z&=2ty+\sigma^2+k_t\sigma+m\theta+\mathfrak n
                               +(2t\sigma+k)X+t^2X^2,\\
W&=w+\theta X+sX^2,\\
mw&=\ell-(2\sigma+k_t)y-\mathcal F(\sigma,\theta),\\
\mathcal F(P,V)&=k_{tt}P^2/2+pPV+hV^2/2
                                 +\mathfrak n_tP+\mathfrak n_sV,\\
J_{t,s,x}(Y,Z,W)&=-a_0^4/\rho\in(L')^*.
\end{aligned}
\tag{6}
\]
Here mathfrak n is the potential n. The scalar is independent of
x and X, not assumed constant under coefficient differentiation.

## 2. The full initial kernel descends to complex coefficients

Work in the actual polynomial three-ring R=K[Y,Z,W], K=C(X).
It embeds in F[x], F=L'(X). Its fraction field is L(v)(X), while
F(x)=L'(v)(X) is only a finite separable overfield of that fraction
field. This distinction is retained throughout.

As in556, the actual derivation
\(\Delta=a_0N-(NX)E\), extending N by Nu=0, fixes X and is
a nonzero K-LND on R. In F[x] it is a0*rho*partial_x and kills
F. Its filtration is x degree. The usual local-slice argument
gives trdeg_K(ker_R Delta)=2: choose b with Delta squared b=0
and Delta b nonzero, localize at Delta b, and apply the finite
Taylor projection to the slice b/(Delta b). Thus there is a
nonconstant polynomial invariant, without assuming a global
slice for Delta.

The full coordinate degrees and leaders are
\[
(\deg_xY,\deg_xZ,\deg_xW)=(4,4,4),\qquad
(Y_4,Z_4,W_4)=(r,1+2tr,w_4)=(r,rT_0,w_4).
\tag{7}
\]
They are independent of X. The first two coordinate-initial images
are algebraically independent: their ratio T0 is transcendental
over K, and r*eta to the fourth is transcendental over F, for an
independent eta. Define
\[
\begin{aligned}
\phi_{\mathbb C}:\mathbb C[\mathsf Y,\mathsf Z,\mathsf W]
   &\longrightarrow L'[\eta],\\
(\mathsf Y,\mathsf Z,\mathsf W)
   &\longmapsto(r\eta^4,rT_0\eta^4,w_4\eta^4),
\end{aligned}
\tag{8}
\]
and let phi_K be the same map with source coefficients in K and
target F[eta]. A relation for phi_K can be multiplied by a
nonzero complex polynomial in X to clear its denominators. Expand
the result in powers of X. Since X is transcendental over L',
each coefficient is a relation for phi_C. Conversely every such
complex relation remains a relation over K. Therefore
\[
\ker\phi_K=(\ker\phi_{\mathbb C})K[\mathsf Y,\mathsf Z,\mathsf W].
\tag{9}
\]
This argument descends the FULL kernel, not just one chosen relation.

The top of a nonconstant Delta-invariant belongs to ker(phi_K),
because the invariant has x degree zero and all source weights
are positive. Thus this kernel is nonzero. First-two independence
then gives height one. Equation (9) implies the complex kernel is
also a nonzero height-one prime. Hence
\[
\ker\phi_{\mathbb C}=(H),\qquad
\ker\phi_K=(H),\qquad
H\in\mathbb C[\mathsf Y,\mathsf Z,\mathsf W]
\text{ irreducible homogeneous}.
\tag{10}
\]
The second ideal in (10) is taken in the K-polynomial ring.
The kernel is graded, and all three weights equal four, so weighted
homogeneity is ordinary homogeneity. H necessarily involves W.
The image of this coordinate-initial map is not identified with
the entire associated graded ring of R.

## 3. The actual partial bounds the relation degree by two

Let T=partial_W on R, fixing K,Y,Z, and extend it uniquely to the
finite separable overfield F(x). Inverting the ENTIRE Jacobian
matrix in (6), the cofactors from the Y,Z rows give
\[
\deg_x T(t),\deg_x T(s)\le7,\qquad \deg_x T(x)\le8.
\tag{11}
\]
The scalar denominator has no x dependence. Exact separability
over K(t,s) gives T(c)=c_t*T(t)+c_s*T(s) for every c in F.
It follows by differentiating coefficients and x powers that
deg_x(Tf)<=deg_x(f)+7 for every polynomial f in F[x] when Tf
is nonzero. Every iteration on R is licensed by the actual partial.

For a nonconstant invariant f, let Q be its unique source expression
of positive weight M. Write the exact multiplicity of the weighted
top as Q_M=H to the ell times G, ell>=1, H not dividing G. Because
H involves W, H_W is not in (H). The exact source residue is
\[
\partial_{\mathsf W}^{\ell}(H^\ell G)
       \equiv\ell!G(H_{\mathsf W})^\ell\pmod H\ne0.
\tag{12}
\]
All lower source components remain of smaller weight after those
derivatives. The full kernel (10) therefore gives
deg_x(T to the ell f)=M-4ell, whereas the cofactor bound gives
at most 7ell. If D is the weight of H, then
\[
\ell D\le M\le11\ell,\qquad
D\le11,\qquad \deg H\le2.
\tag{13}
\]
Here D=4*deg(H). No strict-growth refinement or profile-specific
theorem is imported from519.

Suppose H were linear. Its W coefficient is nonzero, by first-two
independence. For some complex lambda,mu it would give
\[
w_4=\lambda r+\mu(1+2tr).
\tag{14}
\]
Make the ACTUAL complex shear W*=W-lambda*Y-mu*Z, with X,Y,Z
unchanged. It is a polynomial automorphism with row determinant
one and polynomial inverse. In the same actual R, with the same
Delta, the new W* has exact x degree three: its leading coefficient is
\[
aX+w_3-\lambda q_3-\mu(2tq_3+ma)\ne0.
\tag{15}
\]
This uses the full original rows. The x cubed coefficient of Z
is 2t*q3+ma, while the X-dependent parts of Y and Z have degree
at most two in x. Nonzeroness follows from a nonzero and X
transcendental over L'. No intrinsic root is specialized.

For this actual degree-(4,4,3) triple, the same nonconstant invariant
and first-two independence give a full height-one initial kernel.
The unchanged Y,Z cofactors still give shift seven. The exact
multiplicity argument now bounds the relation weight by 3+7=10.
But a relation must have two different W*-exponent blocks, since
a single block cannot vanish on the independent Y,Z initials.
Homogeneity with weights (4,4,3) makes their exponents differ by
a positive multiple of four, so its weight is at least twelve.
This contradiction excludes (14).

Thus the full generator H in (10) is an irreducible homogeneous
quadratic over C. This shear argument uses the unchanged actual
ring and full scalar; it makes no new chart-entry or selected-partial
normalization claim.

## 4. Dehomogenization forces w4 to be s-constant

Since r is nonzero, put T0=(1+2tr)/r and U0=w4/r. The relation is
\[
H(1,T_0,U_0)=0.
\tag{16}
\]
The dehomogenized polynomial is nonzero and depends on U. Its
coefficients in C[T] cannot all vanish at T0, since T0 is
transcendental over C. Therefore U0 is algebraic over C(T0).
Both r and T0 are killed by partial_s. Characteristic-zero
separability of the minimal polynomial of U0 then gives
(U0)_s=0, hence (w4)_s=0.

This proof does not divide by the W squared coefficient of H.
That coefficient is allowed to vanish; the resulting dependence
on U can be linear after dehomogenization. No conclusion that
U0 or r is rational in T0 is drawn.

## 5. Full H8, H7 and B5 give differential restrictions

In this section H denotes the genuine formal third potential of
264/296, not the coordinate-initial generator of Sections 2--4.
The complete second potential gives
\[
\begin{aligned}
w_5&=-\{2q_3+a(p+hb_2)\}/m=0,\\
w_4&=-\frac{2y_2+(2c+k_t)r+pb_2+h(ad+b_2^2/2)+k_{tt}/2}{m}.
\end{aligned}
\tag{17}
\]
The full coefficient of degree eight in the genuine H level is,
by556,
\[
0=a^4h^2/16+ahw_5+a^2h_t/2.
\tag{18}
\]
Consequently h_t=-a squared*h squared/8 is nonzero, and
r=2h_t/h. Before imposing w5=0, the ENTIRE degree-seven coefficient
of the same H level, using only (4) and (17), is
\[
\begin{aligned}
[x^7](H-h_0)={}&ahw_4+ab_2(h_t+a^2h^2/4)\\
&+w_5(a^2hm/4+hb_2+p)+ap_t/2.
\end{aligned}
\tag{19}
\]
Thus after (18) and w5=0 it becomes
\[
0=ah\{w_4-rb_2/2+p_t/(2h)\},\qquad
w_4=rb_2/2-p_t/(2h).
\tag{20}
\]
Formula (17) retains every lower contribution to w4; (19) is not
a relation for freely chosen replacement potentials. Differentiating
(20) by s, and using (1), r_s=h_s=0 and (p_t)_s=h_tt, gives
(b2)_s=h_tt/(hr)=h_tt/(2h_t).

For the next multiplier coefficient, use the full535 polynomials
in the normalized x parameter. In particular f is the formal
U derivative of H evaluated afterward, and
\[
\begin{aligned}
\mathcal B_\beta={}&4x^2(\theta_t+B_f)+2xD_fy_x+y_x\theta_x
 +2x(\theta_s+\nu-c_t)\theta_x-c_s\theta_x^2,\\
B_f={}&(2y+k_{tt}\sigma+p\theta+\mathfrak n_t)/m,\quad
D_f=(2\sigma+k_t)/m,\quad
\nu=(p\sigma+h\theta+\mathfrak n_s)/m.
\end{aligned}
\tag{21}
\]
The full coefficient of x to the fifth in B_beta+kappa*f is
\[
4a_t+6a(b_2)_s-3a^3h-10w_5-2\kappa ha/m=0.
\tag{22}
\]
All lower theta and y coefficients are present when this coefficient
is taken. No supposition on m_tt is made.

Differentiate a squared=-8h_t/h squared genuinely in t. Then
a_t/a=h_tt/(2h_t)-h_t/h. Substituting this, w5=0 and
(b2)_s=h_tt/(2h_t) into (22) proves (2). In particular
\[
\boxed{hh_{tt}+4h_t^2\ne0.}
\tag{23}
\]
All factors divided by here, namely m,h,a and h_t, have been
proved nonzero. Kappa is the coefficient-field unit from535,
not assumed constant under t or s differentiation.

The noncomplex-T0 condition separately gives
\[
(T_0)_t=\frac{5h_t^2-hh_{tt}}{2h_t^2}\ne0.
\tag{24}
\]
Indeed T0 belongs to F0, whose exact t constants are C. Neither
inequality (23) nor (24) is an exclusion of the remaining family.

## 6. A formal leading-data control, not an actual chart

The displayed leading restrictions are compatible as coefficient
data. To make the limitation explicit, in an auxiliary algebraic
field with a squared=-16/t cubed, take
\[
\begin{gathered}
h=t^2,\quad m=t^2s,\quad r=4/t,\quad
b_2=s/(2t)+81t^2/8,\quad w_4=81t/4,\\
T_0=9t/4,\quad \kappa=45s/(2t),\qquad
H_{\rm init}=\mathsf Y\mathsf W-\mathsf Z^2.
\end{gathered}
\tag{25}
\]
These give r*w4=(1+2tr) squared, the irreducible conic above,
and satisfy (1),(2),(20),(23),(24). For a full check of the
displayed high coefficients, choose the formal potentials
k=t squared*s squared/2, mathfrak n=ell=0 and c=d=e=0. Put
\[
\begin{gathered}
q_3=-a(p+hb_2)/2,\qquad y_1=y_0=0,\\
2y_2=-mw_4-k_t r-pb_2-hb_2^2/2-k_{tt}/2,\qquad
\theta=ax^3+b_2x^2.
\end{gathered}
\tag{26}
\]
Here p=2ts, k_t=ts squared, k_tt=s squared, and a_t=-3a/(2t).
The entire formal expressions then have W6=W5=0 and the required
W4, and satisfy H9,H8,H7, B6,B5 and A7,A6 with the indicated
unit kappa. But the UNUSED degree-six H coefficient at t=s=1,
a=4i equals -30603/64, which is nonzero. Thus this particular
control fails the full genuine H level. It is not an actual264
chart, a realization of the remaining conic, or a counterexample
to any retained hypothesis.

## 7. Verification and remaining scope

The complete556 source and its actual-ring, finite-overfield and
cofactor licenses were read before this continuation. The proof
above descends the full kernel and rederives every weight bound
needed for this profile. It does not assume an initial relation
over C before proving the scalar-extension identity (9).

Fresh f8084b rebuilt the entire original second potential and H,
including (17)--(20). Fresh da9406 rebuilt the complete B expression
and its coefficient (22), the kappa simplification and (24), with
zero residuals. Fresh c7818b reconstructed the full formal control
(25),(26): all ten listed high-coefficient residuals were zero,
and the unused H6 value was exactly -30603/64. These calculations
were fresh inline algebra, not saved checker executions.
A separate independent reconstruction b66e31 verified the complete
H/W coefficients after a full556 read; independent278a43 rebuilt
the whole B/f coefficient used in (22).

The result leaves the irreducible conic case open. No linear or
quadratic coefficient of H is silently assumed nonzero except
where first-two independence forces dependence on W. The original
critical point x=0, finite coefficient extension and all lower
functions remain in scope. The complex-T0 cases are not treated.

No earlier source or canonical file was edited. No saved checker
was executed, imported, compiled or rerun. Separate saved-source
review remains required after the author hold. There is no
recognition, realization, general chart-entry, novelty or
unrestricted cancellation claim.
