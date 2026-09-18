# A degree-profile restriction in the transverse cubic excess branch

Working necessary reduction: retain the FULL actual264/296/535
chart and the h nonzero, v1=0 cubic-excess family554. In the exact
intrinsic parameter below, put
\[
T_0=2t+1/r,\qquad w_i=[x^i]w.
\]
Then
\[
\boxed{T_0\notin\mathbb C\quad\Longrightarrow\quad
                         w_5=0\ \text{and}\ w_4\ne0.}
\tag{1}
\]
Thus the remaining noncomplex-T0 case has actual intrinsic degrees
(4,4,4) in the polynomial three-ring over C(X). This note does not
exclude that case. Every complex-T0 case, including T0=0 and the
resulting possible drop of the Z degree, is left separate.

The full H coefficient also forces w5 to lie in the exact
s-constant coefficient field. No coefficient-field rationality,
global slice for an auxiliary derivation, or actual coordinate
promotion of the intrinsic parameter is used.

## 1. Full actual input and the precise coefficient family

Retain EVERY actual hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md)
and
[535](principal-paraboloid-nonlinear-sigma-unit-multiplier-pass535-working.md),
including the original globally sliced four-ring
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
Here z_int is the literal original Z-intercept. Both actual returns,
the selected literal partial, genuine moving levels and full scalar
remain required. The original slice is not replaced by X/a0.

Use the finite intrinsic normalization and the necessary family
[554, Section 3.2](principal-paraboloid-cubic-excess-leading-families-pass554-working.md).
Thus L'=L(rho) is a finite coefficient extension, x is affine in v,
and
\[
\begin{gathered}
\sigma=x^2+c,\qquad Nx=\rho\in(L')^*,\\
\theta=ax^3+b_2x^2+d x+e,\qquad
y=rx^4+q_3x^3+y_2x^2+y_1x+y_0,\\
a,r\in F_0^*,\quad F_0=\ker_{L'}\partial_s,\quad
h=m_s=-4r/a^2\in F_0^*,\quad m=hs+m_0,\quad m_0\in F_0.
\end{gathered}
\tag{3}
\]
The field F0 is finite over C(t), not assumed rational. In particular
a_s=r_s=h_s=0. Put p=m_t; its genuine s derivative is p_s=h_t.
All partials are the exact commuting coefficient partials, extended
to fix x. No condition is imposed here on any other lower coefficient.

The original rows and second potential, using mathfrak n for the
potential n, remain
\[
\begin{aligned}
Y&=y+\sigma X+tX^2,\\
Z&=2ty+\sigma^2+k_t\sigma+m\theta+\mathfrak n
                              +(2t\sigma+k)X+t^2X^2,\\
W&=w+\theta X+sX^2,\\
mw&=\ell-(2\sigma+k_t)y-\mathcal F(\sigma,\theta),\\
\mathcal F(P,V)&=\frac{k_{tt}}2P^2+pPV+\frac h2V^2
                              +\mathfrak n_tP+\mathfrak n_sV,\\
J_{t,s,x}(Y,Z,W)&=-a_0^4/\rho\in(L')^*.
\end{aligned}
\tag{4}
\]
The scalar is independent of both x and X. It may depend on t,s;
none of its coefficient derivatives is assumed to vanish.

## 2. The entire second potential and the full H coefficient

The whole second potential in (4) has degree at most six in x.
Its two highest coefficients are exactly
\[
w_6=-\frac{2r+ha^2/2}{m}=0,\qquad
w_5=-\frac{2q_3+ap+ha b_2}{m}.
\tag{5}
\]
The first equality uses h=-4r/a squared. The contributions to w5
are respectively 2sigma*y, p*sigma*theta and h*theta squared/2.
Every remaining term of the full potential has lower degree.
Hence deg_x(w)<=5, including the possibility that w5 vanishes.

For clarity the genuine formal third level is
\[
\begin{aligned}
H-h_0={}&U^2+\mathcal F_PU+
\mathcal F_V\frac{\ell-(2P+k_t)U-\mathcal F}{m}
 +H_3(k;P,V)+H_2(\mathfrak n;P,V)\\
&-\ell_tP-\ell_sV-h_0,\qquad
H(y,\sigma,\theta)=h_0.
\end{aligned}
\tag{6}
\]
Its complete formal support is printed in553. Before substituting
h=-4r/a squared, its degree-eight coefficient in the present
profile is
\[
\begin{aligned}
[x^8](H-h_0)={}&r^2-\frac{2pr}{m}
 -\frac{2h(aq_3+b_2r)}m+3a^2b_2C_3
 +\frac{a^2}{2}\left(h_t-\frac{3hp}{m}\right),\\
C_3={}&\frac{h_s}{6}-\frac{h^2}{2m}=-\frac{h^2}{2m}.
\end{aligned}
\tag{7}
\]
This is an entire-level coefficient with all lower functions and
genuine coefficient derivatives retained. Using (3),(5), it becomes
\[
0=\frac{a^4h^2}{16}+ahw_5+\frac{a^2h_t}{2}.
\tag{8}
\]
Since a,h are nonzero, the resulting identity is
\[
\boxed{w_5=-\frac{a^3h}{16}-\frac{ah_t}{2h}
              =a_t-\frac{ar_t}{2r}+\frac{ar}{4}\in F_0.}
\tag{9}
\]
The second expression differentiates the genuine relation
h=-4r/a squared. Membership in F0 follows from a,r,h in F0 and
commutation of the two coefficient partials. It holds whether or
not T0 is complex, and includes w5=0. No initial-form independence
argument is needed for this particular coefficient-field conclusion.

## 3. The actual three-ring and its finite coefficient overfield

Put K=C(X) and work with the ACTUAL polynomial three-ring
\[
R=K[Y,Z,W]=K^{[3]}.
\tag{10}
\]
This uses that X,Y,Z,W are the original polynomial coordinates,
not an intrinsic or coefficient-field coordinate system. Set
F=L'(X). The rows (4) give an injection R into F[x]. Moreover
\[
\operatorname{Frac}R=L(v)(X),\qquad
F(x)=L'(v)(X)
\text{ is finite separable over }\operatorname{Frac}R,
\quad [F:K(t,s)]<\infty.
\tag{11}
\]
Indeed u=(X-x0)/a0 in the original fraction field. We do not
identify Frac(R) with the larger field F(x) when rho was adjoined.
Every actual partial derivation of R extends uniquely to this
finite separable overfield.

Extend N from A to B by Nu=0 and set
\[
\Delta=a_0N-(NX)E.
\tag{12}
\]
It preserves the actual polynomial ring and fixes X. On F[x] it
acts as g0*partial_x with g0=a0*rho in F*. It kills F and g0.
Thus its restriction to R is a nonzero K-LND, and its degree
filtration agrees with x degree. Local nilpotence follows from
this polynomial overring; it is not inferred merely from taking
a difference of two locally nilpotent derivations.

The kernel of Delta contains a nonconstant polynomial over K.
Here is the local-slice justification, without a global slice
assumption for Delta. Choose b in R with Delta squared b=0 and
a:=Delta b nonzero. After localizing at a, b/a is a slice, and
the finite Taylor projection gives
\[
R_a=(\ker_R\Delta)_a[b/a],\qquad
\operatorname{trdeg}_K\ker_R\Delta=2.
\tag{13}
\]
Such a b exists by local nilpotence and nonzeroness. The letters
a,b in this local-slice paragraph are temporary ring elements,
not the coefficient a in (3). No assertion of finite generation
of the kernel is needed.

## 4. The two profiles to be excluded when T0 is noncomplex

Assume from now on T0=2t+1/r is noncomplex. Its value is
transcendental over C and also over K=C(X), since X is
transcendental over L'. In particular T0 is nonzero. The original
Y and Z rows have exact degrees and leaders
\[
\deg_xY=\deg_xZ=4,\qquad
Y_4=r,\quad Z_4=1+2tr=rT_0.
\tag{14}
\]
The contributions of m*theta and the X-dependent terms of Z have
degree at most three. Thus (14) uses the full rows, not a chosen
leading model for a different ring.

There are two positive-degree profiles to rule out:
\[
\begin{array}{c|c|c}
\text{coefficient condition}&(\deg Y,\deg Z,\deg W)&[x^{\deg W}]W\\ \hline
w_5\ne0&(4,4,5)&w_5\\
w_5=w_4=0&(4,4,3)&aX+w_3.
\end{array}
\tag{15}
\]
In the second row aX+w3 is nonzero in F because a is nonzero
and X is transcendental over L'. This retains w3=0 and every
lower coefficient. In particular we do not specialize X to a
coefficient-field root that could lower this degree.

Write d=5 or 3 for the last degree and l_d for its nonzero leader.
For an independent eta define the source initial map
\[
\begin{aligned}
\phi:K[\mathsf Y,\mathsf Z,\mathsf W]&\longrightarrow F[\eta],\\
(\mathsf Y,\mathsf Z,\mathsf W)&\longmapsto
(r\eta^4,rT_0\eta^4,l_d\eta^d),\\
\operatorname{wt}(\mathsf Y,\mathsf Z,\mathsf W)&=(4,4,d).
\end{aligned}
\tag{16}
\]
The first two images are algebraically independent over K:
their ratio is the transcendental T0, while r*eta to the fourth
is transcendental over F. On the other hand the nonconstant
polynomial invariant from (13) has x degree zero. Its unique
source expression has positive weighted degree, so its top
belongs to ker(phi). The full initial kernel is therefore nonzero.
These two facts force it to be a height-one prime in the source UFD:
\[
\ker\phi=(H),\qquad H\text{ irreducible and weighted homogeneous},
\qquad D=\operatorname{wt}H>0.
\tag{17}
\]
The kernel is graded because distinct source weights map to distinct
eta degrees; a generator of this graded principal prime can be
chosen homogeneous. First-two independence forces H to involve W,
and characteristic zero gives H_W not in (H).
No constant-field statement about l_d is used here. In particular
the degree-three leader aX+w3 need not be killed by partial_s.
The kernel (17) is not the original four-variable initial kernel
in (2), nor is its image asserted to be the entire associated graded
ring of R.

## 5. The full cofactor bound and exact derivative multiplicity

Let T=partial_W on the actual R, fixing K,Y,Z, and extend it to
F(x) as in (11). Invert the full coefficient matrix in (4).
The cofactors for T(t) and T(s) use the Y,Z rows, one horizontal
column and one x column. Their degrees are at most 4+4-1=7.
The cofactor for T(x) uses both horizontal columns and has degree
at most eight. Division by the full scalar in (4) introduces no
x denominator. Consequently
\[
T(t),T(s)\in F[x]_{\le7},\qquad T(x)\in F[x]_{\le8}.
\tag{18}
\]
For every coefficient c in F, separability over K(t,s) gives
T(c)=c_t*T(t)+c_s*T(s). This is an identity of derivations into
F(x), not a claim that T preserves F. Differentiating any polynomial
sum(c_i*x to the i) therefore shows
\[
\deg_x T(f)\le\deg_x f+7\quad(T(f)\ne0).
\tag{19}
\]
Indeed the coefficient term has degree at most i+7, and the
x-derivative term has degree at most i-1+8. The bound applies to
every polynomial in F[x], hence to every element of the actual R.
Its iterations on R are licensed by the actual partial T.

Choose a nonconstant invariant f in ker_R(Delta). Let Q be its
unique source polynomial, of positive weighted degree M. Since
deg_x(f)=0, its top Q_M lies in (H). Write its exact multiplicity
as Q_M=H to the ell times G, with ell>=1 and H not dividing G.
Repeated source differentiation gives the nonzero residue
\[
\partial_{\mathsf W}^{\ell}(H^\ell G)
   \equiv \ell!G(H_{\mathsf W})^\ell\pmod H.
\tag{20}
\]
It is nonzero in the domain modulo H. Its weight is M-d*ell,
and all differentiated lower source components have smaller
weight or vanish. The FULL kernel identity (17) thus gives the
exact, not merely bounded, degree
\[
\deg_xT^\ell f=M-d\ell.
\tag{21}
\]
Meanwhile (19) gives deg_x(T to the ell f)<=7ell. Also M>=ell*D
because the weights are positive. Therefore
\[
\boxed{D\le d+7.}
\tag{22}
\]
This rederives the needed multiplicity argument from the actual
matrix. It does not import519's profile-specific theorem or its
strict growth refinement. No global slice or polynomial-coordinate
assertion for x has entered the proof.

## 6. The modular lower bound contradicts both profiles

Write a nonzero weighted-homogeneous relation as
\[
H=\sum_j\mathsf W^jH_j(\mathsf Y,\mathsf Z).
\tag{23}
\]
Every nonzero H_j has ordinary degree (D-dj)/4, a nonnegative
integer. There must be at least two distinct W-exponent blocks:
a single block evaluates to a product of a nonzero power of the
third initial and a nonzero polynomial in the independent first
two initials, so cannot be a relation.

For two exponents j1<j2, homogeneity gives 4 dividing d(j2-j1).
As d is odd, 4 divides j2-j1, so j2>=4. Hence
\[
D\ge dj_2\ge4d.
\tag{24}
\]
For d=5 this says D>=20, contradicting D<=12 from (22).
For d=3 it says D>=12, contradicting D<=10. Both rows of (15)
are impossible. Thus w5=0, and w4 cannot vanish as well. This
proves precisely (1).

If T0 is complex, first-two independence fails. If T0=0, the
leading Z coefficient in (14) vanishes too. Neither case is
covered by this argument. When T0 is noncomplex and w4 is
nonzero, the resulting degree-(4,4,4) case has different possible
initial relations and is not excluded or recognized here.

## 7. Verification and scope

The complete553/554 inputs were read before this continuation.
The full saved519 was read through EOF in1e06ce+367291 to check
the scope of its cofactor method. Sections 3--6 supply the needed
argument afresh, including finite coefficient extension, actual
partial iteration, full initial kernel and all positive weights.

Fresh unsaved6a86c0 and f8084b reconstructed the entire original
second potential and formal H with arbitrary lower coefficients.
They verified (5),(7),(8), with every residual zero. The latter
also checked directly that no weight at most twelve for (4,4,5),
or at most ten for (4,4,3), has two distinct W-exponent blocks.
The modular argument in Section 6 is the proof, not that finite
enumeration. A separate independent reconstruction9288ce checked
the complete W/H8 identities, genuine coefficient derivatives and
the full cofactor bounds (7,7,8), after a complete519 read.

Every lower coefficient, the full scalar and both actual returns
remain required. There is no assertion that the formal leading
data alone are realized by an actual chart. No saved checker was
executed, imported, compiled or rerun; no earlier source or
canonical file was edited. Separate saved-source review remains
required after the author hold. No novelty, general chart entry,
recognition or unrestricted cancellation claim is made.
