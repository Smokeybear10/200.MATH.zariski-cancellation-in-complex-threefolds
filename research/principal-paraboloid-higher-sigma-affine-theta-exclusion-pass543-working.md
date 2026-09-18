# Higher-degree sigma with affine theta is impossible for variable coupling

Working exclusion: retain the FULL actual264/296 chart and the unit
multiplier of535. If the coupling m is noncomplex and theta has
intrinsic degree one, then sigma cannot have intrinsic degree at
least three. The proof first bounds the complete first intercept,
forces longitudinally constant coupling, and uses a complex ACTUAL
normalization. Degrees at least four then contradict strong return.
Degree three contradicts the arbitrary-field degree-(3,5) polynomial
generation lemma in529.

The theta-based parameter below belongs to the original intrinsic
polynomial ring. It is never promoted to an ambient coordinate.
No rationality of the coefficient field, classification of polynomial
embeddings, or claim of arbitrary chart entry is used.

## 1. Full actual input and an original-field theta parameter

Retain every actual hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
the genuine H/Q levels and unit ideals of
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md),
and the complete multiplier conclusion of
[535](principal-paraboloid-nonlinear-sigma-unit-multiplier-pass535-working.md).
In particular,
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u_{\rm glob}],\quad
E=\partial_{u_{\rm glob}},\quad X=a_0u_{\rm glob}+x_0,\quad a_0\ne0,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\quad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the entire original initial kernel},\\
0\ne N=[u_{\rm glob}^4]\partial_Z|_A,\quad Na_0=Nt=Ns=0,\\
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,
\quad L[A]=L[v],\quad Nv=1,\\
\operatorname{Frac}A=L(v)=\mathbb C(y,z_{\rm int},w),\quad
L[y,z_{\rm int},w]=L[v],\quad
J_{t,s,v}(X)=-a_0^4\in L^*.
\end{gathered}
\tag{1}
\]
Here z_int is the literal Z-intercept, not its difference with 2ty.
Assume
\[
m=k_s\notin\mathbb C,\qquad \deg_v\theta=1,
\qquad n:=\deg_v\sigma\ge3.
\tag{2}
\]
The degree n in (2) is distinguished from the first-potential function
n(t,s) by context; all appearances of n_t,n_s and their higher
partials refer to that potential.

Put z=theta. This is an affine intrinsic parameter over L, with
\[
L[z]=L[v],\qquad Nz=D_\theta\in L^*,\qquad
P(z):=\sigma,\quad \deg_zP=n,\quad a=[z^n]P\ne0.
\tag{3}
\]
No extension of L is needed. Coefficient partials now fix z. Their
moving terms have the exact scalar and multiplier transport
\[
J_{t,s,z}=-a_0^4/D_\theta\in L^*,\qquad
\kappa=\kappa_v/D_\theta^2\in L^*.
\tag{4}
\]
Indeed the parameter Jacobian is D_theta. The formal gradient cross
product is unchanged, while the primitive tangent is divided by
D_theta, so its unit multiplier is multiplied by D_theta;535's
formula kappa=-J0/tau gives (4). The coefficient partials on elements
of L themselves are unchanged. Neither (4) nor the following degree
arguments assume that theta is an actual coordinate.

Use the abbreviations
\[
k_1=k_t,\quad k_2=k_{tt},\quad k_3=k_{ttt},\quad
p=m_t,\quad h=m_s,\quad \beta=P_z.
\tag{5}
\]
The complete first two potentials are
\[
\begin{aligned}
Y&=y+PX+tX^2,\\
Z&=2ty+P^2+k_1P+mz+n+(2tP+k)X+t^2X^2,\\
W&=w+zX+sX^2,\\
mw&=\ell-(2P+k_1)y-k_2P^2/2-pPz-hz^2/2-n_tP-n_sz.
\end{aligned}
\tag{6}
\]
All lower coefficients and moving levels remain present.

## 2. The full multiplier bounds the first intercept

With theta=z, the denominator-free equations of535 become
\[
\begin{aligned}
\mathcal A_\beta
 &=\beta^2y_t+\beta y_s+y_z^2-\beta P_ty_z-P_sy_z
   =\kappa g,\\
m\mathcal B_\beta
 &=\beta^2(2y+k_2P+pz+n_t)
   +(2P+k_1)\beta y_z+\beta(pP+hz+n_s)\\
 &\hspace{8mm}+my_z-m\beta P_t-mP_s=-\kappa m f,\\
f&=2y+k_2P+pz+n_t
       -\frac{(2P+k_1)(pP+hz+n_s)}m,\qquad g=H_V^{\rm ev}.
\end{aligned}
\tag{7}
\]
All P_t,P_s partials fix z. In particular they have degree at most n.
The formal derivative H_V is always taken before evaluation.

If y has degree d>n with leader r_d, the terms
2 beta squared y and 2P beta y_z in mB have unique highest
degree d+2n-2 and combined leader
\[
2n(n+d)a^2r_d\ne0.
\tag{8}
\]
Every other term has degree at most max(3n-2,n+d-2,d-1,2n-1), and
the right side has degree at most max(d,2n). Thus d>n is impossible.
This argument only concerns positive d; it leaves y=0 and every
constant y included in the conclusion deg y at most n.

Write r_n=[z^n]y, allowing r_n=0. Since 3n-2>2n for n>=3,
the coefficient of degree 3n-2 in (7) gives
\[
n^2a^2(4r_n+k_2a)=0.
\tag{9}
\]
Set
\[
q=-k_2/4,\qquad R=y-qP=y+k_2P/4.
\tag{10}
\]
Then either R=0 or deg R<n. The entire second equation of (7)
rewrites as
\[
\begin{aligned}
m\mathcal B_\beta={}&\beta^2\mathcal L
 +(2P+k_1)\beta R_z
 +\beta(pP+hz+n_s+mq-mP_t)+mR_z-mP_s,\\
\mathcal L&=2R+qk_1+pz+n_t.
\end{aligned}
\tag{11}
\]
If j=deg R satisfies 3<=j<n, the unique top degree is 2n+j-2,
with coefficient 2n(n+j)a squared times the nonzero leader of R.
All terms outside the two groups 2 beta squared R and 2P beta R_z have
degree at most 2n-1, while deg f<=2n. This is impossible. Thus
\[
R=r_2z^2+r_1z+r_0,
\tag{12}
\]
with all three coefficients allowed to vanish. The coefficient of
degree 2n in (11) and -kappa m f is exactly
\[
\boxed{n(n+2)r_2=\kappa p.}
\tag{13}
\]
Here the two sides before cancellation are
2n(n+2)a squared r2 and 2 kappa p a squared. No division by p or
r2 has occurred.

## 3. Full H forces p=0 and a complex k_tt

For an inspectable formal identity, leave P and z independent and
substitute U=qP+R(z) in the genuine H, including its moving level.
Define
\[
\mathcal M=k_1R+hz^2/2+n_sz-\ell.
\]
The full second potential and full substituted H are
\[
w=-\frac{\mathcal LP+\mathcal M}{m},\qquad
H(qP+R,P,z)=C_3P^3+C_2P^2+C_1P+C_0,
\tag{14}
\]
where
\[
\begin{aligned}
C_3={}&k_3/6,\\
C_2={}&-3k_2^2/16-p\mathcal L/m+p_tz/2+n_{tt}/2,\\
C_1={}&k_2R/2-k_2(pz+n_t)/4
 -(hz+n_s)\mathcal L/m-p\mathcal M/m
 +p_sz^2/2+n_{ts}z-\ell_t,\\
C_0={}&R^2+(pz+n_t)R-(hz+n_s)\mathcal M/m
 +h_sz^3/6+n_{ss}z^2/2-\ell_sz.
\end{aligned}
\tag{15}
\]
This is the entire polynomial, not only its highest terms. It evaluates
to the coefficient-field level h0. In particular the degrees of C2,
C1,C0 in z are at most 2,3,4, respectively, using (12).

After evaluation at P(z), the term of degree 3n is uniquely
k3 a cubed/6: 3n>2n+2, n+3,4 for n>=3. Therefore k3=0.
Next the coefficient of degree 2n+2 is uniquely
\[
-\frac{2p r_2a^2}{m}=0.
\tag{16}
\]
The remaining terms have degrees at most 2n+1,n+3,4.
Combining (13),(16), with m,kappa,a nonzero in characteristic zero,
gives
\[
p=0,\qquad r_2=0,\qquad k_3=0.
\tag{17}
\]
Since (k2)_s=p_t=0 and (k2)_t=k3=0, the exact joint-constant
property gives k2 in C. This property follows from separability:
dt,ds form a differential basis, so an element killed by both
partials is algebraic over C, hence complex. Also
b0=k1-k2*t is complex, since its s derivative is p and its t
derivative is zero.

## 4. A licensed actual normalization for arbitrary n

Put q0=k2/4 and use the complex actual map
\[
X^*=X-q_0,\qquad Y^*=Y+(b_0/2)X^*,\qquad Z^*=Z,\qquad W^*=W.
\tag{18}
\]
Its inverse replaces X by X*+q0 and Y by Y*-(b0/2)X*, fixing Z,W.
Both q0 and b0 may vanish. This is the same type of map verified
in539, but its licenses here do not assume sigma quadratic.

The original E, its global slice and kernel are unchanged, as is a0.
Only terms of smaller E-degree were added. All four initial forms,
the entire original initial kernel, t and s are therefore unchanged.
The inverse X,Y do not involve Z*, so the literal partial
\(\partial_{Z^*}=\partial_Z\), and its selected coefficient is the
same N in the original slice. Thus the same L and v remain valid.

The complete row expansion gives
\[
\begin{aligned}
\sigma^*&=\sigma+2q_0t+b_0/2,&
\theta^*&=\theta+2q_0s,\\
y^*&=y+q_0\sigma+q_0^2t,&
k^*&=k-2q_0t^2-b_0t,\\
n^*&=n+q_0k-2q_0tk_t+3q_0^2t^2-2q_0sm-b_0^2/4,&
w^*&=w+q_0\theta+q_0^2s.
\end{aligned}
\tag{19}
\]
Consequently \(k_t^*=0\), m*=m, and m_t*=0. The intrinsic degrees
of sigma and theta remain n and one. By (10),(12),(17), y* is affine
in theta*, including a possible constant or zero intercept.

The returns in (1) must also be retained. The actual equality
\(\mathcal B_{a_0}=A_{a_0}[X^*]\) holds. The coordinate prime X*
does not divide a0, by additivity of E-degree and deg_E a0=0.
Thus evaluation at X*=0 of the actual frame identifies
\(A_{a_0}=\mathbb C[y^*,z_{\rm int}^*,w^*]_{a_0}\).
Here a0 is a polynomial in the new intercepts, obtained by evaluating
its actual polynomial expression. Taking fractions gives the strong
complex-field return; adjoining L removes the localization since
a0 is in L*. This also retains the polynomial return.
At fixed X*, the differential rows are the old ones evaluated at
X=X*+q0, with the added (b0/2)X* having zero coefficient differential.
The full scalar remains -a0^4 in the original v basis.

Hence every actual264 input is retained. The new genuine potentials
come from this actual frame, not from independently assigned lower
functions. Drop stars, and once again use the original-field
intrinsic parameter z=theta. Its speed and multiplier obey (4).
We have now proved
\[
k_t=m_t=0,\quad h=m_s\ne0,\quad
\sigma=P(z),\ \deg P=n\ge3,\quad y=lz+r.
\tag{20}
\]
Here h is nonzero because m is noncomplex and m_t=0.
No normalization of variable m itself was attempted.

## 5. The complete normalized H leaves only the cubic boundary

Put lambda=n_t. The entire H after (20) is
\[
H(lz+r,P,z)=\frac{n_{tt}}2P^2+A_2(z)P+B_3(z),
\tag{21}
\]
with
\[
\begin{aligned}
A_2(z)&=-\frac{(hz+n_s)(2lz+2r+\lambda)}m
                       +\lambda_sz-\ell_t,\\
B_3(z)&=(lz+r)^2+\lambda(lz+r)
 -\frac{(hz+n_s)(hz^2/2+n_sz-\ell)}m
 +\frac{h_s}{6}z^3+\frac{n_{ss}}2z^2-\ell_sz.
\end{aligned}
\tag{22}
\]
In particular deg A2<=2 and deg B3<=3. Because 2n>n+2,3,
the coefficient of degree 2n first forces n_tt=0. Thus lambda_t=0.
The coefficient of degree n+2 then gives
-2hl*a/m=0, hence l=0. The coefficient of degree n+1 next gives
\[
\lambda_s-\frac{h(2r+\lambda)}m=0,\qquad
r=\frac{m\lambda_s}{2h}-\frac\lambda2,\qquad r_t=0.
\tag{23}
\]
These comparisons apply also at n=3, because n+1>3.
They do not require that the constant term of A2 vanish.

Differentiate the genuine formal H in V BEFORE putting U=r,V=z.
Its complete evaluated V-gradient is
\[
\begin{aligned}
g={}&\left(\lambda_s-\frac{h(2r+\lambda)}m\right)P
 +\left(\frac{h_s}{2}-\frac{3h^2}{2m}\right)z^2\\
&+\left(n_{ss}-\frac{3hn_s}{m}\right)z
 +\frac{h\ell}{m}-\frac{n_s^2}{m}-\ell_s.
\end{aligned}
\tag{24}
\]
Equation (23) removes its entire P term, so deg g<=2, including
g=0. Meanwhile the first equation of (7) becomes exactly
\[
P_z r_s=\kappa g.
\tag{25}
\]
If n>=4, a nonzero r_s would give degree n-1>=3 on the left,
impossible on the right. Hence r_s=0. Together with r_t=0 this
makes r complex, contradicting the strong return
\(L(z)=\mathbb C(r,z_{\rm int},w)\) of transcendence degree three.
This treats every lower-degree drop of g. Only n=3 remains.

## 6. The cubic case gives a forbidden degree-(3,5) return

For n=3 the same strong return excludes r_s=0. Define
\[
u=\frac{2r+\lambda}{m}=\frac{\lambda_s}{h}.
\tag{26}
\]
This coefficient is nonzero. Indeed u=0 would make lambda_s=0;
then lambda_t=0 makes lambda complex, and r=-lambda/2 would be
complex as well. This again contradicts the retained field return.

The full all-X equality is
\(L[X,Y,Z,W]=L[X,z]\). It follows by localizing
\(\mathcal B=A[u_{\rm glob}]\) at the nonzero elements of ker N
and using X=a0*u_glob+x0 with a0 in L*. Evaluate this polynomial
equality at X=0. Since Y0=r is in L, it yields
\[
L[Z_0,W_0]=L[z],\qquad
Z_0=P^2+mz+2tr+n,\qquad W_0=-uP-T_2,
\tag{27}
\]
where the complete lower polynomial is
\[
T_2=\frac{h}{2m}z^2+\frac{n_s}{m}z-\frac\ell m.
\tag{28}
\]
In this coefficient-field return only, apply the invertible shear
\[
V_0=Z_0-W_0^2/u^2
 =-2PT_2/u-T_2^2/u^2+mz+2tr+n.
\tag{29}
\]
Its inverse is Z0=V0+W0 squared/u squared. The exact degrees and
leaders, with a=[z^3]P, are
\[
\deg W_0=3,\quad \deg V_0=5,\quad
\operatorname{lc}W_0=-ua\ne0,\quad
\operatorname{lc}V_0=-\frac{ah}{mu}\ne0,
\quad L[W_0,V_0]=L[z].
\tag{30}
\]
Every lower coefficient in (27)--(29) is retained. The shear is over
L after specialization, not an actual ambient-coordinate claim.

## 7. The exact arbitrary-field obstruction used from529

Section 3 of the completely read
[529](principal-paraboloid-transverse-cubic-low-intercept-exclusion-pass529-working.md)
proves that two polynomials of exact degrees three and five over
ANY characteristic-zero field cannot generate its polynomial ring
in one variable. That abstract lemma has no affine-sigma or coupling
hypothesis. We recall the full finite-root argument to identify the
precise input being used.

After extending a field F to its algebraic closure, equality
F[f,g]=F[z] would give a polynomial inverse. Telescoping that inverse
at independent variables P,Q gives the unit divided-difference ideal
\[
\left(\frac{f(P)-f(Q)}{P-Q},\frac{g(P)-g(Q)}{P-Q}\right)=(1).
\tag{31}
\]
Let a3,b5 be the nonzero leaders. The divided differences have
P-degrees two and four with those CONSTANT nonzero leaders, and
total highest parts
a3(P²+PQ+Q²) and b5(P⁴+P³Q+P²Q²+PQ³+Q⁴).
Their P-resultant has Q-degree eight with leader a3^4*b5^2,
because
\[
\operatorname{Res}_P(P^2+PQ+Q^2,
 P^4+P^3Q+P^2Q^2+PQ^3+Q^4)=Q^8.
\tag{32}
\]
Reduction of the second polynomial modulo the first gives Q³(P+Q),
which proves (32). To see that lower coefficients cannot affect the
degree-eight leader, substitute P=T/epsilon,Q=1/epsilon and multiply
the two polynomials by epsilon squared and epsilon to the fourth.
Their resultant becomes epsilon to the eighth times the original
resultant at 1/epsilon, with constant term a3^4*b5^2.

The nonconstant resultant has a root Q=q0. Both P-leading coefficients
remain nonzero there, so it supplies a common FINITE root P=p0.
This contradicts (31). The case p0=q0 is allowed: the divided
differences then evaluate to the two derivatives and still cannot
vanish together. Thus no injectivity-only or root-at-infinity shortcut
is being used. Applying this lemma to (30) is the final contradiction.

## 8. Verification, prior scope and limits

The full535 was freshly read through EOF before this proof. The
existing strict sigma-dominant result385 was also read completely;
it assumes the already normalized constant coupling k=s and
n_ss nonzero. That result is not an entry license for the variable
coupling treated here, and none of its theorem conclusions is imported.
The full529 was read through EOF before reusing only its abstract
degree-(3,5) lemma.

Fresh unsaved428147 to971961 rebuilt the complete B remainder,
the full H decomposition (14),(15), and the normalized full H and
formal H_V. All residuals were zero. Checks with unrestricted lower
polynomial coefficients at degrees three through six supplemented
the uniform degree inequalities above; those samples are not their
proof. Fresh eb67dd rebuilt all three full transported rows (19),
the entire shear (29), its quintic leader, and resultant (32), with
zero residuals.

The conclusion is exactly impossibility of (2) under the FULL retained
actual chart. The proof includes y=0, constant y, p=0 initially,
vanishing k_tt, every lower R coefficient, and all drops in g. The
nonzero h used after normalization follows from m noncomplex; a
constant-coupling case is not excluded by this proof. The quadratic
sigma sector and other theta degrees are not asserted here.
No arbitrary action is assumed to enter this chart. No original
slice or coefficient-field substitution was promoted to an actual
coordinate. No saved checker was executed, imported, compiled, or
rerun, and no earlier source or canonical record was edited.
Complete independent saved-source review is a separate step.
