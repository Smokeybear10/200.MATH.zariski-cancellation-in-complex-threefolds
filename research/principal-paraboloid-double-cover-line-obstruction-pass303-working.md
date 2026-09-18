# Actual recognition and a two-good frontier for double-cover lines

Working result: retain the actual nonzero-coupling principal
paraboloid chart264 and suppose its projection to
\((\sigma,\theta)\) has degree two. The line reduction295
then sharpens as follows.

If \(\sigma\notin L\), an actual polynomial reframe produces an
explicit invariant coordinate, apart from a degenerate family
which is impossible by normality. Thus the original kernel is
recognized in this branch.

If \(\sigma\in L\), the remaining coefficients force
\(k_s=c_1t+c_0\), with complex constants \(c_1,c_0\), and an
actual auxiliary derivation has an exact two-good coordinate
frame. This last statement is a reduction, not recognition of
the original derivation. No full coupled-sector conclusion is made.

## 1. Precise actual input and a quadratic-degree sharpening

Retain the full actual hypotheses, selected literal partial,
exact coefficient field, and both returns of the completely read
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
[290](principal-paraboloid-nonzero-coupling-projection-pass290-working.md),
[295](principal-paraboloid-double-projection-line-reduction-pass295-working.md),
and [296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md):
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad
\deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(X^2Z-Y^2),\quad a=EX\ne0,\quad
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,\\
O=L[v],\quad Nv=1,\quad K=\operatorname{Frac}A=L(v)
=\mathbb C(y,z,w),\quad L[y,z,w]=L[y,\sigma,\theta]=O,\\
m=k_s\ne0,\qquad
[L(v):\operatorname{Frac}L[\sigma,\theta]]=2 .
\end{gathered}
\tag{1}
\]
The literal map and calibration are
\[
\begin{aligned}
Y&=y+\sigma X+tX^2,\\
Z&=z+(2t\sigma+k)X+t^2X^2,\\
W&=w+\theta X+sX^2,\qquad
\det\frac{\partial(Y,Z,W)}{\partial(t,s,v)}=-a^4\in L^*.
\end{aligned}
\tag{2}
\]
Coefficient partials extend uniquely to \(L\), commute, and fix
\(v\). Their common constants are exactly \(\mathbb C\), as
proved in295. Formal \(U,P,V\) derivatives are always taken
before evaluation.

By290 and295 there is \(x=v-\beta_0/2\), with \(Nx=1\), such that
\[
\begin{gathered}
r=x^2,\quad L[\sigma,\theta]=L[r],\\
\sigma=p_1r+p_0,\quad\theta=q_1r+q_2,\quad
(p_1,q_1)\ne(0,0),\\
y=A(r)+\tau x,\quad \tau\in L^*,\quad \deg_r A\le2 .
\end{gathered}
\tag{3}
\]
All the coefficients in (3) belong to \(L\). None is being
declared an ambient coordinate or a complex constant.

Write the third potential as
\[
H-h_0=U^2+A_1(P,V)U+A_0(P,V),\qquad
\Delta=A_1^2-4A_0.
\]
The exact trace and discriminant identities of290 give
\[
2A(r)=-A_1(\sigma,\theta),\qquad
\Delta(\sigma,\theta)=4\tau^2r,\qquad
\deg A_1\le2,\quad\deg A_0\le3.
\tag{4}
\]
If \(A_1(\sigma,\theta)\) had degree two in \(r\), its square
would have degree four. The term \(4A_0(\sigma,\theta)\), of
degree at most three, could not cancel it. Consequently
\[
\boxed{\deg_r A\le1,\qquad
\deg_x y\le2,\quad\deg_x\sigma\le2,\quad\deg_x\theta\le2.}
\tag{5}
\]
This sharpening uses the monic surface and the double-cover
discriminant, not an ambient linear change.

## 2. Remainder identities retained from the actual Jacobian

For reference, use the formal definitions
\[
\begin{aligned}
F&=\frac{k_{tt}}2P^2+m_tPV+\frac{m_s}2V^2+n_tP+n_sV,\\
D&=(2P+k_t)/m,\qquad \lambda=F_V/m,\\
A_1&=F_P-DF_V,\\
A_0&=F_V(\ell-F)/m+H_3(k)+H_2(n)-\ell_tP-\ell_sV-h_0,\\
e&=(k_{tt}-2Dm_t+D^2m_s)/2,\\
R&=A_{0,P}-DA_{0,V}+(\lambda-e)A_1 .
\end{aligned}
\tag{6}
\]
The Taylor polynomials \(H_j\) have the factorial conventions
of264. If \(G(P,V)\) is the irreducible equation of the projected
line, the fourth potential296 and the odd-unit argument295 prove
\[
Q-q_0-e(H-h_0)=RU+S,\qquad
R=G^2R^\sharp,\quad S=\eta_0 G+G^2S^\sharp,\quad\eta_0\in L^*.
\tag{7}
\]
In particular the square divisibility in (7) uses the actual
constant Jacobian through the unit ideal of the two-gradient
minors. It is not a general property of a parametrized conic.
The top coefficient is
\[
R_4=\frac{4P^3m_s(m_tP+m_sV)}{m^3}.
\tag{8}
\]

## 3. Nonconstant sigma forces a complex coefficient family

Suppose \(p_1\ne0\), equivalently \(\sigma\notin L\).
Write the plane equation as
\(G=V-\zeta P-\xi\), with \(\zeta,\xi\in L\).
If \(m_s\ne0\), the two factors in (8) have multiplicities
three and one, so \(G_{\rm top}^2\) could only divide it if
\(G_{\rm top}\) were \(P\). That would make \(\sigma\) constant.
Hence \(m_s=0\).

Now the degree-two part of \(A_1\) is \(-2m_tP^2/m\).
Its evaluation has quadratic \(r\)-coefficient
\(-2m_t p_1^2/m\). Equation (5) makes this zero.
Thus \(m_t=0\), and
\[
m\in\mathbb C^*.
\tag{9}
\]
With all derivatives of \(m\) zero, the entire remainder has
degree at most two, and its quadratic part is
\[
R_2=P\left[\left(\frac{k_{ttt}}2-\frac{2n_{ts}}m\right)P
                         -\frac{2n_{ss}}mV\right].
\tag{10}
\]
This has no \(V^2\) coefficient. A nonzero scalar multiple of
\((V-\zeta P)^2\) does have such a coefficient. Therefore (7)
forces the quadratic part to vanish, and then forces \(R=0\).

The exact lower-coefficient calculation in295, Sections4 and5,
now applies. Its use of a nonlinear projected image was only
to obtain \(R=0\); the subsequent coefficient identities and
actual reframe are valid here. They give
\[
k=m s+\kappa t^2/2+b t+d,\qquad
n=\nu_0s+f_0(t),\qquad
m,\kappa,b,d,\nu_0\in\mathbb C .
\tag{11}
\]
Here \(f_0(t)\) denotes an element killed by \(\partial_s\),
not an assumption that the constant field is rational.

Make the actual polynomial reframe from295,
\[
W_*=mW+\kappa Z/2+bY+dX^2.
\tag{12}
\]
Its inverse, preserved selected intrinsic field, exact finite
coefficient basis \((t,s_*=k)\), both returns and unchanged
calibration were proved there explicitly. In particular
\(\sigma_*=\sigma\) remains nonconstant. Dropping stars, its
new coefficients have
\[
k=s,\qquad m=1,\qquad n=\nu s+f(t),\quad \nu\in\mathbb C .
\]
Do not assume that the old zero remainder transports formally.
Instead, apply (7) anew in this actual frame. Its new remainder is
\[
R=(f''+2\ell_s)P-\ell_t.
\]
It depends only on \(P\) and is divisible by the square of
\(V-\zeta_*P-\xi_*\), so it must be zero. Commuting the
coefficient partials, followed by exact joint-constant integration,
therefore gives
\[
\boxed{
k=s,\qquad
n=\nu s+\alpha t^2/2+\beta t+\delta,\qquad
\ell=-\alpha s/2+\ell_0,\qquad
\nu,\alpha,\beta,\delta,\ell_0\in\mathbb C .}
\tag{13}
\]

## 4. An invariant-coordinate lemma for the entire family (13)

This section assumes the actual chart264 and coefficients (13),
but does not assume any projection degree or that \(\sigma\)
is nonconstant. Put \(f=\alpha t^2/2+\beta t+\delta\).
The literal first and second potentials are
\[
z=2ty+\sigma^2+\theta+\nu s+f,\qquad
w=-\alpha s/2+\ell_0-2\sigma y-f'\sigma-\nu\theta .
\tag{14}
\]
Use only complex shifts of actual coordinates:
\[
Y_0=Y+\beta/2,\qquad Z_0=Z-\delta,\qquad W_0=W-\ell_0,
\qquad \varepsilon=\alpha/2-\nu^2.
\]
Define the actual polynomial
\[
\boxed{
I=Y_0^2+(\alpha/2-X^2)Z_0+(X+\nu)W_0.}
\tag{15}
\]
Substitution of the full expressions (2),(14), including every
power of \(X\), gives
\[
\boxed{
I=(y+\beta/2+\alpha t/2-\nu\sigma)^2
                         +\varepsilon(\sigma^2+\theta).}
\tag{16}
\]
For example the \(\theta\) coefficient in (15) is
\((\alpha/2-X^2)+(X+\nu)(X-\nu)=\varepsilon\);
its \(s\) coefficient is zero. After those cancellations,
the coefficients in \(\sigma y\), \(ty\), \(\sigma^2\),
\(t\sigma\), and \(t^2\) are respectively
\(-2\nu,\alpha,\alpha/2,-\nu\alpha,\alpha^2/4\), as in (16).
Thus (16) lies in \(K\), and \(EI=0\). No polynomiality of
the individual coefficient-field terms on its right is assumed.

Now make the actual triangular shear
\[
V_0=W_0-(X-\nu)Z_0.
\]
Then
\[
\boxed{I=Y_0^2+\varepsilon Z_0+(X+\nu)V_0.}
\tag{17}
\]
If \(\varepsilon\ne0\), this displays an actual coordinate frame
\[
\mathcal B=\mathbb C[X,Y_0,V_0,I],\qquad
Z_0=\frac{I-Y_0^2-(X+\nu)V_0}{\varepsilon},\qquad
W_0=V_0+(X-\nu)Z_0 .
\tag{18}
\]
Both compositions are polynomial, with only a nonzero complex
denominator. Since \(I\) is invariant, the published
[Bhatwadekar--Gupta--Lokhande Theorem3.5](https://arxiv.org/html/1501.01438v1)
applies: a nonzero locally nilpotent derivation of a polynomial
four-ring fixing an actual coordinate has polynomial kernel
over that coordinate if its kernel is regular.
Here \(E\ne0\), and the global slice gives
\(A\simeq\mathcal B/(u)\), hence \(A\) is affine. The equation
\(Eu=1\) makes the hypersurface \(u=0\) smooth, so \(A\) is regular.
Consequently
\[
A=\mathbb C[I]^{[2]}\cong\mathbb C^{[3]}.
\tag{19}
\]

If \(\varepsilon=0\), equation (16) instead makes \(I\) a square
in \(\operatorname{Frac}\mathcal B\).
Its square root is integral over the normal polynomial ring
\(\mathcal B\), so it belongs to \(\mathcal B\).
But (17) has exact degree one in the actual independent coordinate
\(V_0\) over \(\mathbb C[X,Y_0,Z_0]\). A nonzero polynomial square
has even degree there. This is impossible.

Thus every actual member of the full coefficient family (13)
is either recognized by (19), or lies in the impossible
\(\varepsilon=0\) degeneration. Combined with Section3, this
recognizes the nonconstant-\(\sigma\) double-cover branch.
The family lemma itself did not use the third level, the fourth
level, or the projection hypothesis after (14).

## 5. Constant sigma forces affine coupling and a constant ratio

It remains to investigate \(\sigma\in L\). In (3), now
\(q_1\ne0\), so \(\theta=q_1r+q_2\) and the discriminant identity
(4) is affine in the formal variable \(V\) after setting
\(P=\sigma\). The plane equation is \(G=P-\sigma\).

The following two coefficients of the unrestricted formulas (6)
are independent of \(P\):
\[
[V^3]\Delta=-\frac{2(m m_{ss}-3m_s^2)}{3m},\qquad
[V^2]R_P=-\frac{m m_{ss}-m_s^2}{m^2}.
\tag{20}
\]
The first is zero because the evaluated discriminant has degree
one in \(\theta\). The second is zero because
\((P-\sigma)^2\mid R\), and so the formal derivative \(R_P\)
vanishes after \(P=\sigma\).
Subtracting these two equations gives \(m_s=0\).
This proves that no double-cover branch with \(m_s\ne0\) remains.

With \(m_s=m_{ts}=m_{ss}=0\), two further coefficients are
\[
[V^2]\Delta=m_t^2-2n_{ss},\qquad
[V]R_P=\frac{m m_{tt}+m_t^2-2n_{ss}}m .
\tag{21}
\]
They vanish for the same reasons. Hence
\[
\boxed{
m=c_1t+c_0,\qquad n_{ss}=c_1^2/2,\qquad
c_1,c_0\in\mathbb C,\quad (c_1,c_0)\ne(0,0).}
\tag{22}
\]
The complex constants follow by integrating \(m_{tt}=m_s=0\)
in the exact finite field, using the joint-constant gate.
These calculations are formal derivatives before line
evaluation; they do not differentiate a moving root \(\sigma\).

After (22), the coefficient of \(V\) in \(R\) is independent
of \(P\) and equals
\[
[V]R=
\frac{k_t c_1^2-k_{tt}m c_1+2m n_{ts}-2c_1 n_s}{2m}.
\tag{23}
\]
Since \(R(\sigma,V)=0\), this coefficient vanishes. Define
\[
\eta=\frac{c_1k_t/2-n_s}{m}.
\]
Its \(s\)-derivative is zero because \(k_{ts}=c_1\) and
\(n_{ss}=c_1^2/2\). Its \(t\)-derivative is
\(-[V]R/m\), hence also zero. Therefore
\[
\boxed{\eta\in\mathbb C.}
\tag{24}
\]

## 6. Two actual auxiliary affine coordinates, with the boundary retained

Extend the intrinsic \(N\) from \(A\) to \(\mathcal B=A[u]\)
by \(Nu=0\). Define
\[
\mathcal P=aN-(NX)E .
\tag{25}
\]
This is an actual derivation of \(\mathcal B\), fixes \(X\),
and commutes with \(E\). Indeed \(Na=0\), \(E(NX)=Na=0\),
and \(a=EX\) is \(E\)-invariant. On
\(\mathcal B_a=A_a[X]\), it acts as \(aN\) on \(A_a\)
and kills \(X\), so it is locally nilpotent there and hence
on the invariant subring \(\mathcal B\).
On \(K[X]\), it is \(aN\) on coefficients.

Let \(D_0=(2\sigma+k_t)/m\) and
\(\lambda_0=(c_1\sigma+n_s)/m\). The coefficient of \(\theta\)
in \(A_1(\sigma,\theta)\) is \(c_1\). Equation (4) therefore gives
\[
y=-\frac{c_1}{2}\theta+b_0+\tau x,\qquad b_0\in L.
\tag{26}
\]
In the literal map, \(w=-D_0y-\lambda_0\theta+w_0\),
with \(w_0\in L\). Thus all three original entries have
auxiliary degree at most two. More precisely, (22),(24),(26)
give the exact row
\[
\boxed{
\mathcal P^2(Y,Z,W)
=a^2N^2\theta\,(-c_1/2,\ c_0,\ X+\eta),\qquad
N^2\theta=2q_1\ne0.}
\tag{27}
\]
The identity
\(c_1D_0/2-\lambda_0=\eta\) verifies the last component.
Every \(\mathcal P^3\) of these entries vanishes.

If \(c_1\ne0\), use the actual \(\mathbb C[X]\)-triangular changes
\[
U_0=Z+\frac{2c_0}{c_1}Y,\qquad
V_1=W+\frac{2(X+\eta)}{c_1}Y .
\tag{28}
\]
Their inverses subtract the displayed multiples of \(Y\).
They fix \(X,Y\), and \(\mathcal P^2U_0=\mathcal P^2V_1=0\).
Both coordinates have nonzero first derivative:
\[
\mathcal P U_0=\frac{2am\tau}{c_1},\qquad
\mathcal P V_1
=a\tau\left(\frac{2(X+\eta)}{c_1}-D_0\right).
\tag{29}
\]
The first is a nonzero element of \(L\); the second has a
nonzero \(X\)-coefficient. The remaining coordinate \(Y\)
has exact auxiliary degree two by (27).

If \(c_1=0\), then \(m=c_0\in\mathbb C^*\). Use instead
\[
U_0=Y,\qquad
V_1=W-\frac{X+\eta}{c_0}Z .
\tag{30}
\]
The inverse adds that multiple of \(Z\), fixing \(X,Y,Z\).
Here
\[
\mathcal P U_0=a\tau,\qquad
\mathcal P V_1=-a\tau
\left(D_0+\frac{2t(X+\eta)}{c_0}\right),\qquad
\mathcal P^2U_0=\mathcal P^2V_1=0 .
\tag{31}
\]
The displayed first derivative \(\mathcal P V_1\) is nonzero as a polynomial in
\(X\), because \(t\ne0\). The remaining coordinate \(Z\)
has exact auxiliary degree two.

Thus the constant-\(\sigma\) branch has an actual coordinate
frame with auxiliary profile \((0,1,1,2)\), without dividing
by a nonconstant coefficient-field element. This is not the
time profile of the original \(E\), and is not itself a
recognition theorem for \(\ker E\). No unproved descent from a
coordinate over \(\mathbb C(X)\) is asserted.

## 7. Scope

The new conclusions for the double-cover branch are:
\(m_s=0\); all intrinsic generators have degree at most two;
the branch \(\sigma\notin L\) is recognized by an actual
invariant coordinate after the justified reframe; and the
remaining \(\sigma\in L\) branch has the exact auxiliary
two-good frame above.

The standalone coefficient-family lemma of Section4 has no
projection hypothesis. Conversely, that family is not assumed
to contain arbitrary constant-\(\sigma\) data. The latter
endpoint and the birational projection case of290 remain open.
All retained sources and previously completed checkers are
unchanged.

Fresh unsaved algebra reconstructed every coefficient in
(20),(21),(23), the full invariant (16), and both polynomial
inverse identities in (18). The published Theorem3.5 statement
was freshly read in its primary source with the actual fixed
coordinate and regular-kernel hypotheses retained. No saved
checker was executed, imported, compiled or rerun.
No general1222, arbitrary-entry, actual-existence, novelty,
human-expert review or proof-assistant certification claim is made.
