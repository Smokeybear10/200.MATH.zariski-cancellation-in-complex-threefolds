# Recognition when both retained potentials have one coefficient variable

Working result: retain the entire supplied actual principal chart264.
If \(k=s\) and \(n_s=\ell_s=0\), then its original sliced kernel is
\(\mathbb C^{[3]}\). Neither n nor ell is assumed rational in t, or
polynomial in t. They initially belong to the exact finite coefficient
constant field.

When \(n_{tt}\ne0\), the nonconstant first-projection alternative is
excluded by the fourth potential and actual polynomial divisibility.
The remaining alternative has an explicitly preserved actual three-ring,
so the published three-variable and regular-kernel theorems apply.
When \(n_{tt}=0\), an actual constant translation reduces to298.

This does not normalize arbitrary k, n, or ell, and it does not recognize
every principal1222 chart. The nonconstant alternative overlaps the
reducible-surface coverage324; the direct argument here excludes that
alternative rather than importing its recognition conclusion.

## 1. Actual chart and exact constants

Retain every hypothesis of the completely read
[264](principal-one-affine-paraboloid-chart-pass264-working.md), including
its full initial ideal, literal selected partial, whole polynomial return,
strong complex-field return, and calibrated determinant:
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,
\qquad A=\ker E,\qquad \deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2),\qquad
a_0=EX\ne0,\qquad
N=[u^4]\partial_Z|_A\in\operatorname{LND}(A),\\
Na_0=Nt=Ns=0,\quad
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,
\quad Nv=1,\\
K=\operatorname{Frac}A=L(v)=\mathbb C(y,z,w),\qquad
O=L[v]=L[y,z,w]=L[y,\sigma,\theta],\\
J(X)=\det\frac{\partial(Y,Z,W)}{\partial(t,s,v)}=-a_0^4\in L^*.
\end{gathered}
\tag{1}
\]
The exact coefficient partials commute and fix v. In particular
\(a_0\in L^*\), and all intrinsic coefficients are E-invariant.
As in264, every coefficient of the fixed-X expansions belongs to
\(A_{a_0}\subset O\).

Assume
\[
k=s,\qquad n_s=\ell_s=0,\qquad
\mathbb F=\ker_L\partial_s,\qquad n=f\in\mathbb F,
\quad \ell\in\mathbb F.
\tag{2}
\]
The field \(\mathbb F\) is finite over \(\mathbb C(t)\).
The restriction of the exact t-derivative has constant field
\(\mathbb C\): its constants are algebraic over the algebraically
closed base constant field. A prime below denotes this derivative,
not differentiation in a presumed rational parameterization.

The complete first two potentials and the actual map are
\[
\begin{aligned}
z&=2ty+\sigma^2+\theta+f,&
w&=\ell-2\sigma y-f'\sigma,\\
Y&=y+\sigma X+tX^2,&
Z&=z+(2t\sigma+s)X+t^2X^2,&
W&=w+\theta X+sX^2.
\end{aligned}
\tag{3}
\]
No ambient coordinate change with a coefficient from \(\mathbb F\)
is implicit in these formulas.

## 2. Centered third and fourth levels

Use the fully read exact identities of
[333](principal-paraboloid-one-variable-first-potential-plane-reduction-pass333-working.md),
which were derived from264 and296 before any division by \(\ell_s\).
Put
\[
p=f'/2,\qquad g=f''/2,\qquad x=y+p,\qquad
\bar h=h+p^2\in L.
\tag{4}
\]
The third level and the centered fourth primitive specialize to
\[
\begin{aligned}
x^2+g\sigma^2-\ell'\sigma&=\bar h,\\
Q_c(U,P,V)&=(2gP-\ell')U+\frac{g'}3P^3
 -\frac{\ell''}2P^2-\bar h_tP-\bar h_sV,\\
Q_c(x,\sigma,\theta)&\in L.
\end{aligned}
\tag{5}
\]
The first equation uses the full quadratic-X coefficient, and the
fourth level uses the full linear-X coefficient. The formal polynomial
is obtained before the substitution of the actual functions. All
coefficient derivatives in (5) therefore retain the original convention.
The affine change x=y+p is only over L and preserves the polynomial
line ring; it need not be an actual coordinate translation.

If \(g=0\), the exact constant field gives
\(f=f_1t+f_0\) with \(f_1,f_0\in\mathbb C\). The actual map
\[
Y_*=Y+f_1/2,\qquad Z_*=Z-f_0,\qquad X_*=X,\qquad W_*=W
\tag{6}
\]
has the inverse constant translations. Directly in (3), it gives
\(k_*=s,n_*=0,\ell_*=\ell\), retaining \((\ell_*)_s=0\).
It preserves the leaders, selected N, exact field, and actual returns.
The retained one-variable-potential recognition
[298](principal-paraboloid-one-variable-potential-recognition-pass298-working.md)
therefore applies. This is the only use of that result's complete
n=0 recognition theorem. Henceforth assume \(g\ne0\).

## 3. The nonconstant branch forces complex quadratic coefficients

If \(\sigma\in L\), the first equation of (5) gives \(x\in L\),
because a nonconstant polynomial in v cannot have a constant square.
Conversely, x in L and g nonzero force sigma in L by the same degree
argument. The complementary case is consequently
\(\sigma,x\notin L\).

In this case their v-degrees are equal. Indeed the nonconstant top
terms in \(x^2+g\sigma^2\) must cancel, since the remaining term
has degree at most \(\deg_v\sigma\). Their leading-coefficient ratio
defines an element of the exact field, not an extension of it:
\[
\alpha=\frac{\operatorname{lc}_v x}{\operatorname{lc}_v\sigma}\in L^*,
\qquad \alpha^2=-g.
\tag{7}
\]
Since \(g_s=0\), differentiating this identity gives
\(\alpha_s=0\), hence \(\alpha\in\mathbb F^*\).

Complete the square in (5):
\[
\left(x-\alpha\left(\sigma-\frac{\ell'}{2g}\right)\right)
\left(x+\alpha\left(\sigma-\frac{\ell'}{2g}\right)\right)
=\bar h+\frac{(\ell')^2}{4g}\in L.
\tag{8}
\]
If the right side were nonzero, both factors would be units in
\(L[v]\), hence would belong to L. Their difference would make
sigma constant, a contradiction. The right side is therefore zero.
The second factor has nonzero leading coefficient by (7), so the
first factor is identically zero. Thus
\[
x=\alpha\sigma+\beta,\qquad
\beta=\frac{\ell'}{2\alpha}\in\mathbb F,\qquad
\bar h=-\frac{(\ell')^2}{4g}\in\mathbb F.
\tag{9}
\]
In particular \(\bar h_s=0\); no theta term remains in the fourth
level in (5).

A nonconstant sigma is transcendental over L. Substitution of (9)
in the complete fourth primitive makes a polynomial in sigma constant.
Its cubic and quadratic coefficients are respectively
\[
[\sigma^3]Q_c=\frac{g'}3,\qquad
[\sigma^2]Q_c=2g\alpha-\frac{\ell''}2.
\tag{10}
\]
Consequently
\[
g\in\mathbb C^*,\qquad \alpha\in\mathbb C^*,\qquad
\ell''=4g\alpha,
\qquad
\begin{aligned}
f&=gt^2+f_1t+f_0,\\
\ell&=2g\alpha t^2+e_1t+e_0,
\end{aligned}
\quad f_i,e_i\in\mathbb C.
\tag{11}
\]
These integrations use the exact constant field of \(\mathbb F\),
not rationality of \(\mathbb F\). In particular, coefficient-field
algebraicity has not supplied any ambient coordinate.

Combining (4),(9),(11) gives
\[
y=\alpha\sigma+gt+b_0,\qquad
b_0=\frac{e_1}{2\alpha}-\frac{f_1}{2}\in\mathbb C.
\tag{12}
\]
The lower linear coefficient of the fourth level also vanishes under
(11): it is \(-2\alpha\ell'+\ell'\ell''/(2g)\).
The argument does not assume or need any further lower coefficient
equation to obtain (12).

## 4. Original-ring divisibility excludes that branch

Use only the actual constant translations
\[
X_*=X+\alpha,\qquad Y_*=Y-b_0,
\qquad Z_*=Z,\qquad W_*=W.
\tag{13}
\]
They have polynomial inverses over \(\mathbb C\). Since
\(g=-\alpha^2\), the literal first row of (3),(12) becomes
\[
Y_*=(X+\alpha)\bigl(\sigma+t(X-\alpha)\bigr)
=X_*\bigl(\sigma-2\alpha t+tX_*\bigr)
\quad\text{in }\mathcal B_{a_0}.
\tag{14}
\]
The last factor belongs to this localization: t and sigma belong to
\(A_{a_0}\) by the actual chart. Thus some power of \(a_0\)
times \(Y_*\) is divisible by \(X_*\) in the original ring.

The element \(X_*\) is prime in \(\mathcal B\) and cannot divide
\(a_0\). Indeed \(\deg_E X_*=1\) and \(\deg_E a_0=0\), whereas
E-degree is additive on nonzero products in a characteristic-zero
domain. Primeness therefore forces \(X_*\mid Y_*\) in
\(\mathcal B\). This is impossible in the actual coordinate frame
\((X_*,Y_*,Z_*,W_*)\): modulo \(X_*\), the image of \(Y_*\) is
still an indeterminate, not zero.

This excludes the entire nonconstant branch in Section3. It requires
neither polynomial entry of \(\mathbb F\) nor an ambient promotion of
x or sigma. Equivalently, the actual quotient at \(X_*=0\) would
give a zero first intercept and contradict the three-dimensional
strong field return, but the prime-divisibility argument supplies the
contradiction directly in \(\mathcal B\).

## 5. The constant branch preserves an actual three-ring

It remains that \(x,\sigma\in L\). Then y=x-p and
\(w=\ell-2\sigma x\) also belong to L. The whole return in (1),(3)
gives
\[
L[\theta]=L[v],\qquad N\theta\in L^*.
\tag{15}
\]
Use the actual auxiliary derivation from298 Section2 and258 Section2,
with the following global construction retained explicitly. Extend N
to \(\mathcal B=A[u]\) by \(Nu=0\), and put
\[
\mathcal P=a_0N-(NX)E.
\tag{16}
\]
This is a derivation of the original polynomial ring. Since
\(Na_0=0\), \([E,N]=0\), and \(E(NX)=N(EX)=0\), it commutes
with E, fixes X, and fixes \(a_0\).
On \(\mathcal B_{a_0}=A_{a_0}[X]\), it is \(a_0N\) on
\(A_{a_0}\) and zero on X. It is locally nilpotent there because
N is locally nilpotent and kills \(a_0\). Its restriction to the
original preserved ring is therefore locally nilpotent as well.

The literal rows in (3) now give
\[
\mathcal PX=\mathcal PY=0,\qquad
\mathcal PZ=\tau,\qquad \mathcal PW=X\tau,
\qquad \tau=a_0N\theta\ne0.
\tag{17}
\]
Although tau belongs to the original ring, it is not assumed to be
an original-ring unit. Make the actual polynomial shear
\[
S=W-XZ,\qquad W=S+XZ.
\tag{18}
\]
In \(\mathcal B=\mathbb C[X,Y,S][Z]\), (17) says
\(\mathcal P=\tau\partial_Z\). The domain property gives
\[
\ker_{\mathcal B}\mathcal P=R:=\mathbb C[X,Y,S],
\qquad E(R)\subset R.
\tag{19}
\]
No slice for \(\mathcal P\), or for the restriction of E to R,
has been asserted.

Write \(\delta=E|_R\). This nonzero LND has
\(\delta X=a_0\ne0\) and \(\delta^2X=0\).
Let c be the gcd in R of its three coordinate coefficients.
Because \(c\mid a_0\) and \(a_0\in\ker\delta\), factorial closure
of the kernel, or additive LND degree, gives \(\delta c=0\).
The quotient \(D=\delta/c\) is consequently an irreducible LND
of the actual three-variable polynomial ring R. It still satisfies
\(DX\ne0,D^2X=0\).

[Dasgupta--Gupta, Theorem4.8, restating Daigle](https://arxiv.org/html/1701.03635v1)
applies precisely to this irreducible LND and the actual coordinate X.
It supplies an invariant coordinate Q of R. Since
\(\mathcal B=R[Z]\), Q is also an actual coordinate of
\(\mathcal B\), and \(EQ=0\).
The original slice makes A affine and regular: \(A[u]=\mathcal B\)
is a regular polynomial extension, and \(A\cong\mathcal B/(u)\)
is affine. Therefore
[Bhatwadekar--Gupta--Lokhande, Theorem3.5](https://arxiv.org/html/1501.01438v1)
applies to the original E fixing the actual coordinate Q and gives
\(A\cong\mathbb C[Q]^{[2]}\cong\mathbb C^{[3]}\).

## 6. Conclusion and scope

Combining the affine-f reduction in Section2 and the two branches
above proves the scoped working implication
\[
\boxed{\text{Under the full actual chart(1),}\quad
k=s,\quad n_s=\ell_s=0
\quad\Longrightarrow\quad A\cong\mathbb C^{[3]}.}
\tag{20}
\]
Moreover, when \(n_{tt}\ne0\), every actual frame in this sector
must have \(y,\sigma\in L\); its nonconstant alternative has been
excluded, not merely recognized. This does not assert that any such
frame exists.

In the excluded alternative, (8),(9) also factor the formal third
level over the exact L. Thus the earlier reducible-surface synthesis
[324](principal-paraboloid-reducible-surface-recognition-synthesis-pass324-working.md)
already supplied recognition for that alternative. The present direct
exclusion and its coefficient restrictions are separate, and the
constant branch does not require the formal surface to be reducible.
The n=0 case was already298. The assembled result here completes the
one-variable n and ell sector without a rational or polynomial ansatz.

No claim is made for arbitrary k, for \(n_s\ne0\), or for
\(\ell_s\ne0\). No normalization of arbitrary1222 frames or
unrestricted cancellation result follows.

## 7. A conditional corollary of the actual normalization334

The complete source
[334](principal-paraboloid-complex-quadratic-normalization-composition-pass334-working.md)
supplies an actual normalization under its precise coefficient-family
conditions. Retain its entire actual input and assume
\[
k_s=m_0\in\mathbb C^*,\qquad k_{ttt}=0,\qquad
n_{ss}=n_{ts}=n_{ttt}=0.
\tag{21}
\]
By334's exact-field integration these are equivalent to
\(k=m_0s+\kappa t^2/2+bt+d\) and
\(n=(B+\kappa/2)k+Dt^2+At+C\), with all the displayed coefficients
complex. Here B is a scalar coefficient, not the original ring.
Its explicit polynomial map and inverse give
\(k_*=s_*,n_*=(D-B^2)t^2\), with all actual chart hypotheses retained.

The complete second-potential transport from334 is
\[
\ell_*=
\ell+\frac{\kappa n}{2}
 +\left(\frac{\kappa B}{2}+B^2\right)k
 +2BC-2B(D-B^2)t^2,
\qquad \partial_{s,*}=m_0^{-1}\partial_s.
\tag{22}
\]
Because \(n_s/m_0=B+\kappa/2\), direct differentiation gives
\[
(\ell_*)_{s,*}
=\frac{\ell_s}{m_0}+\left(B+\frac\kappa2\right)^2
=\frac{m_0\ell_s+n_s^2}{m_0^2}.
\tag{23}
\]
Consequently, under the full actual hypotheses and (21), the additional
identity \(m_0\ell_s+n_s^2=0\) gives both
\((n_*)_{s,*}=(\ell_*)_{s,*}=0\). The main result (20) recognizes A
for every value of the residual \(D-B^2\), including zero.
This is a conditional use of334's actual complex-coefficient map;
it does not assert (21) for arbitrary charts or turn a coefficient-field
reparameterization into an ambient map.

The complete sources264,298,333,334 and the applicable actual three-ring
endpoint in258 Section2 were read. The exact primary statements of
Theorem4.8 and Theorem3.5 were freshly inspected. A fresh unsaved
calculation checked the factor identity, both top coefficients in(10),
the lower linear cancellation, and the entire actual divisibility
identity(14). Those identities do not replace the exact-field and
global-LND arguments above. No saved checker was executed, imported,
compiled, or rerun, and no retained source or canonical index was edited.
