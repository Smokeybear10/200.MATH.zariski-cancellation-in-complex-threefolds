# An actual degree-lowering map for an affine two-variable potential

Working result: the actual principal chart264 is recognized when
\(k=s\), \(n=0\), and \(\ell=\lambda t+\beta s+\gamma\), where
\(\lambda,\beta,\gamma\in\mathbb C\) and \(\beta\ne0\).
An explicit polynomial automorphism gives either an invariant actual
coordinate or an exact1122 coordinate frame. The latter is recognized
by the retained synthesis257.

This is a shorter independent coordinate calculation, not new parameter
coverage. The earlier
[301](principal-paraboloid-affine-second-potential-reduction-pass301-working.md),
read with its mandatory
[constant-first correction](principal-paraboloid-affine-second-potential-pass301-correction-working.md),
already recognizes the broader sector \(k=s,n=0,\ell_s\ne0,\ell_{ss}=0\).
In fact its plane-potential argument excludes the present complex-affine
subcase, as explained in Section4 below. The explicit automorphism here
remains valid, but does not assert that this actual subcase is nonempty.

The map works for constant and nonconstant first intercepts, including
the zero denominator in a fourth-potential elimination. It requires
no coefficient-field coordinate descent. The separate \(\ell_s=0\)
sector was already handled in298 and is not reproved here.

## 1. Retained actual entry

Retain the complete actual hypotheses of
[264](principal-one-affine-paraboloid-chart-pass264-working.md):
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,
\qquad A=\ker E,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\qquad a=EX\ne0,\\
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the full weighted initial kernel},\\
L=\operatorname{Frac}\ker_A N,\qquad
[L:\mathbb C(t,s)]<\infty,\qquad
K=\operatorname{Frac}A=L(v),\qquad Nv=1.
\end{gathered}
\tag{1}
\]
Here N is the selected shift-four part of the literal Z-partial,
\(a,t,s\in L\), \(a\ne0\), and t,s are algebraically independent.
The coefficient partials commute and fix v. The actual returns
\(K=\mathbb C(y,z,w)\), \(L[y,z,w]=L[y,\sigma,\theta]=L[v]\)
and the calibration \(J(X)=-a^4\) are retained.

Assume the additional conditions
\[
k=s,\qquad n=0,\qquad
\ell=\lambda t+\beta s+\gamma,
\quad \lambda,\beta,\gamma\in\mathbb C,\quad\beta\ne0.
\tag{2}
\]
The literal first two potentials and actual map are then
\[
\begin{aligned}
z&=2ty+\sigma^2+\theta,& w&=\ell-2\sigma y,\\
Y&=y+\sigma X+tX^2,\\
Z&=z+(2t\sigma+s)X+t^2X^2,\\
W&=w+\theta X+sX^2.
\end{aligned}
\tag{3}
\]
Every coefficient in these X-expansions is killed by E. The third
potential becomes
\[
H(U,P,V)=U^2-\lambda P-\beta V,
\qquad h:=y^2-\lambda\sigma-\beta\theta\in L.
\tag{4}
\]
In fact \(H-h\) is irreducible over L: its V-coefficient is the
nonzero constant \(-\beta\), and its quotient ring is \(L[U,P]\).
The reducible-surface synthesis324 is not being used.

## 2. Polynomial coordinates without a coefficient-field change

Define three elements of the original polynomial ring:
\[
\begin{aligned}
R&=Y^2+XW-X^2Z,\\
T&=XR-\gamma X^2-\lambda Y-\beta W,\\
S&=\beta Z-R.
\end{aligned}
\tag{5}
\]
R is an intermediate polynomial; it is not asserted to be a coordinate.
The actual new coordinate frame is \((X,T,Y,S)\).

To prove this before using the potentials, write
\[
\begin{pmatrix}T-XY^2+\lambda Y+\gamma X^2\\ S+Y^2\end{pmatrix}
=
\begin{pmatrix}-X^3&X^2-\beta\\X^2+\beta&-X\end{pmatrix}
\begin{pmatrix}Z\\W\end{pmatrix}.
\tag{6}
\]
The displayed two-by-two determinant is the complex unit \(\beta^2\).
With
\(U_0=T-XY^2+\lambda Y+\gamma X^2\), \(V_0=S+Y^2\),
the polynomial inverse is
\[
\boxed{
Z=-\frac{XU_0+(X^2-\beta)V_0}{\beta^2},\qquad
W=-\frac{(X^2+\beta)U_0+X^3V_0}{\beta^2}.}
\tag{7}
\]
X and Y are fixed. Multiplication of the matrices, with the indicated
translations in Y, verifies both inverse orders. Thus
\(\mathcal B=\mathbb C[X,T,Y,S]\) as an actual polynomial ring.
Only the complex unit \(\beta^2\) is inverted. No nonconstant element of L,
ambient coordinate, or nonconstant polynomial is inverted in this map.

## 3. Exact time degrees of the new coordinates

Substitute the complete literal map (3) into R. All quadratic and
higher X-coefficients cancel by the first potential, while the
linear coefficient is \(2\sigma y+w=\ell\). Hence
\[
R=y^2+\ell X.
\tag{8}
\]
Equations (2),(3),(5) now give the full expansions
\[
\boxed{
\begin{aligned}
T&=hX+(2\beta\sigma-\lambda)y-\beta\ell,\\
S&=\beta z-y^2+
   \bigl(\beta(2t\sigma+s)-\ell\bigr)X
   +\beta t^2X^2.
\end{aligned}}
\tag{9}
\]
For T, the X-squared coefficient cancels because
\(\ell-\gamma-\lambda t-\beta s=0\); its X-coefficient
is exactly (4). Thus
\[
ET=ah,\qquad E^2T=0,\qquad
E^2S=2a^2\beta t^2\ne0,\qquad E^3S=0.
\tag{10}
\]
The nonvanishing uses the actual nonzero leader a, the hypothesis
\(\beta\ne0\), and the transcendental coefficient t. In particular
S has exact E-degree two, not merely degree at most two. X and Y
retain their exact degrees one and two.

If \(h=0\), T is an invariant actual coordinate. The original slice
makes A affine and regular: \(\mathcal B=A[u]\) is regular, and
regularity descends from a polynomial extension. The nonzero LND E
fixes T, so the precise invariant-coordinate theorem
[Bhatwadekar--Gupta--Lokhande, Theorem3.5](https://arxiv.org/html/1501.01438v1)
gives \(A=\mathbb C[T]^{[2]}\).

If \(h\ne0\), the actual frame has exact profile
\[
\deg_E(X,T,Y,S)=(1,1,2,2).
\tag{11}
\]
The completely read
[full exact1122 synthesis257](full-exact1122-recognition-synthesis-pass257-working.md)
recognizes every such supplied globally sliced frame, without an
additional condition on its full initial kernel. Therefore
\[
\boxed{k=s,\ n=0,\ \ell=\lambda t+\beta s+\gamma,
\quad\beta\in\mathbb C^*
\quad\Longrightarrow\quad A\cong\mathbb C^{[3]}.}
\tag{12}
\]
This invocation retains257's stated working-proof dependencies. It
does not assert a new unconditional proof of those earlier endpoints.

## 4. Scope and the avoided elimination boundary

The degree-lowering identities use the first two literal potentials
and the complex affine form of ell. The third relation identifies
the coefficient h in L, but E-invariance of every coefficient in (9)
already follows from the actual fixed-X expansion. Neither the fourth
potential nor strong field return is needed for the polynomial map.
Both remain part of the original hypotheses and are not contradicted
or silently replaced.

In particular no division by
\(2\beta y-h_t+\lambda h_s/\beta\) occurs. Constant y and its
possible identically zero denominator are covered by the same map.
There is also no need to infer that an affine or quadratic intrinsic
generator is an ambient coordinate.

When \(\beta=0\), the determinant in (6) vanishes, so this map does
not supply coordinates. The already retained
[298](principal-paraboloid-one-variable-potential-recognition-pass298-working.md)
treats the separate \(\ell_s=0\) sector, including nonlinear
one-variable potentials; none of that proof is repeated here.

For the precise earlier overlap, the coefficient parameter \(r=\ell\)
in corrected301 gives \(s=(r-\lambda t-\gamma)/\beta\). Thus all
second derivatives of its function H(t,r) vanish. Its exact plane
primitive has quadratic top \(2UP-\mathcal L_rU^2\), which is not
a square of a linear form. The whole plane-line return and unit-cofactor
identity in301 exclude both possible selected degrees one and two:
degree one would require this top to be a square, and degree two would
require it to be the pure-power top of the full plane equation. Hence
the present actual subcase was already excluded by the earlier proof.
This note records an independent polynomial degree-lowering identity,
not a newly covered or realized family.

This note does not make k affine, remove n, or prove ell affine in
an arbitrary coupled chart. It supplies no arbitrary1222 entry or
unrestricted cancellation claim.

The full sources264,296,298 and257 were read before composition. The
full301 and its mandatory correction were then read to resolve prior-work
overlap, and the scope statement above records that overlap explicitly. The
exact primary invariant-coordinate theorem was freshly inspected.
A new unsaved algebra calculation reconstructed both inverse orders,
the three literal identities (8),(9), and the determinant \(\beta^2\);
all residuals vanished. This finite algebra check does not certify
the retained recognition theorem257. No saved checker was executed,
imported, compiled, or rerun, and no earlier source or index was edited.
