# The theta-affine boundary cannot have a t-constant intercept

Working exclusion: in the full actual sigma-dominant chart385,
after387, the remaining pair (deg theta,deg sigma)=(1,2) cannot
have y_t=0. Strong complex-field return makes y_s nonzero, while
four successive coefficients of the calibrated determinant at X=0
force y to vanish.

This handles only the t-constant-y subcase. It does not address the
complementary y_t nonzero branch, the other degree pairs, equal
degrees, or arbitrary coupling. No coefficient-field parameter
change is promoted to an original coordinate.

## 1. Complete actual assumptions and a constant translation

Retain the full actual entry of
[385](principal-paraboloid-nonlinear-sigma-dominant-degree-reduction-pass385-working.md)
and the exact consequence of the fully read
[387](principal-paraboloid-sigma-dominant-coefficient-integrability-pass387-working.md).
In particular
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A_0[u],\quad E=\partial_u,\quad
\deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(X^2Z-Y^2)\text{ is the full initial kernel},\quad
N=[u^4]\partial_Z|_{A_0}\ne0,\quad a_0=EX\ne0,\\
L=\operatorname{Frac}\ker_{A_0}N,\quad [L:\mathbb C(t,s)]<\infty,\quad
Nv=1,\quad O=L[v]=L[y,\sigma,\theta]=L[y,z,w],\\
K=L(v)=\mathbb C(y,z,w),\quad
\det\frac{\partial(Y,Z,W)}{\partial(t,s,v)}=-a_0^4\in L^*.
\end{gathered}
\tag{1}
\]
The coefficient partials on L commute, and their joint constant field
is C. The original global slice, literal selected partial, and full
potential identities are retained, not replaced by a formal
parametrization.

We assume k=s and the remaining intrinsic degrees
\[
\deg_v\theta=1,\qquad \deg_v\sigma=2,\qquad y\in L,\qquad y_t=0.
\tag{2}
\]
By387, n=gamma*t+f, with gamma complex and f_t=0, f_ss nonzero.
The actual complex translation
\[
X^*=X,\quad Y^*=Y+\gamma/2,\quad Z^*=Z,\quad W^*=W
\tag{3}
\]
has inverse Y=Y*-gamma/2, with the other coordinates fixed.
It gives y*=y+gamma/2, sigma*=sigma, theta*=theta, t*=t, s*=s,
z*=z and w*=w. The first two potentials transform to
n*=n-gamma*t=f and ell*=ell.

This translation has Jacobian one, preserves all weighted leaders
and therefore the full initial kernel and exact E-degrees, and leaves
the literal Z-partial and N unchanged. It preserves the scalar
because its differential is unchanged, the whole intrinsic ring
because only a complex constant was added to y, and the strong field
because C(y+gamma/2,z,w)=C(y,z,w). It also preserves y_t=0.
We may therefore drop stars and assume
\[
n=f,\quad f_t=0,\qquad
\nu=f_s,\quad e=f_{ss}\ne0,\qquad \nu_t=e_t=0.
\tag{4}
\]
Since nu_s=e, the field element nu is nonzero. No rationality of
f or of the exact field S=ker_L(partial_t) is assumed.

## 2. The affine intrinsic parameter and the quadratic first intercept

Write V=theta as a new intrinsic polynomial parameter. Since theta
has exact degree one in v, O=L[V] and
\[
\tau:=\partial_v\theta=N\theta\in L^*.
\]
This is only a parameter change over L. The coefficient partials
on L remain the same; the polynomial map is now differentiated
holding V fixed. The chain rule, including the moving coefficients
of theta, gives
\[
J_V(X):=\det\frac{\partial(Y,Z,W)}{\partial(t,s,V)}
=-\frac{a_0^4}{\tau}\in L^*.
\tag{5}
\]
In particular J_V(0) is independent of V and nonzero.

Strong field return is essential here. If y_s were zero, then y_t=0
and exact joint constants would make y complex. But
K=C(y,z,w) would then have transcendence degree at most two,
whereas [L:C(t,s)] is finite and V is transcendental over L, so
trdeg_C K=3. Therefore
\[
y_s\ne0.
\tag{6}
\]

For independent formal P,V, the third level in the current frame is
\[
H(y,P,V)=y^2+\nu\ell-DP+\frac e2V^2-C_2V,\qquad
D=\ell_t+2\nu y,\quad C_2=\ell_s+\nu^2.
\tag{7}
\]
It evaluates to h0 in L. Necessarily D is nonzero: otherwise its
evaluation would be a degree-two polynomial in the independent V
with nonzero leading coefficient e/2, and could not equal h0.
Solving for sigma gives the exact polynomial
\[
P(V):=\sigma=AV^2+BV+C,\qquad
A=\frac e{2D}\ne0,\quad B=-\frac{\ell_s+\nu^2}{D},\quad
C=\frac{y^2+\nu\ell-h_0}{D}.
\tag{8}
\]
The symbol P(V) below denotes this evaluated polynomial, not an
original coordinate. Its t and s derivatives hold V fixed.

## 3. A literal determinant at X=0

The first two potentials give
\[
z=2ty+P^2+V+f,\qquad
w=\ell-2yP-\nu V.
\tag{9}
\]
Using y_t=f_t=nu_t=0, the full literal derivative matrix at X=0 is
\[
\frac{\partial(y,z,w)}{\partial(t,s,V)}
=
\begin{pmatrix}
0&y_s&0\\
2y+2PP_t&2ty_s+2PP_s+\nu&2PP_V+1\\
\ell_t-2yP_t&\ell_s-2y_sP-2yP_s-eV&-2yP_V-\nu
\end{pmatrix}.
\tag{10}
\]
No derivative of C or of the moving affine parameter has been
omitted. Expanding along its first row gives the exact identity
\[
\boxed{
\frac{J_V(0)}{y_s}
=D+2P(\ell_tP_V+\nu P_t)+4y^2P_V-2yP_t.
}
\tag{11}
\]
Division by y_s is valid by(6). The right side is a polynomial
in V and must be constant by(5).

Initially P_t=A_tV^2+B_tV+C_t. The coefficient of V^4 in(11) is
\[
2A\nu A_t.
\tag{12}
\]
Since A and nu are nonzero, A_t=0. Differentiating A=e/(2D),
with e_t=nu_t=y_t=0, now gives D_t=ell_tt=0.

Put p=ell_t. Then p_t=0, and D=p+2nu*y has zero t derivative.
Exact integration in L, if desired, writes ell=p*t+q with
q_t=0; no equality L=S(t) is needed. In particular
\[
B_t=-\frac{p_s}{D}.
\tag{13}
\]
After A_t=0, the V^3 coefficient of(11) is
2A(2Ap+nu B_t). By(8),(13) its vanishing is equivalent to
\[
ep-\nu p_s=0.
\tag{14}
\]
Thus (p/nu)_s=0. Also (p/nu)_t=0, so exact joint constants give
a complex constant c with
\[
p=c\nu,\qquad D=\nu(c+2y)\ne0,\qquad B_t=-2cA.
\tag{15}
\]
The value c=0 has not been divided out.

With these identities imposed, the coefficient of V^2 in(11) is
2A*nu*(C_t+cB). Its vanishing gives C_t=-cB. Consequently the
complete polynomial t derivative, not merely its leading part, is
\[
P_t=-cP_V.
\tag{16}
\]
Substitution in(11) now leaves
\[
\frac{J_V(0)}{y_s}
=(c+2y)\bigl(\nu+2y(2AV+B)\bigr).
\tag{17}
\]
Its V coefficient is 4A*y*(c+2y). Here A is nonzero and
c+2y is nonzero because D=nu(c+2y) is nonzero. Thus y=0.
This contradicts y_s nonzero in(6).

We have proved the scoped exclusion
\[
\boxed{
\text{Under the complete actual385/387 hypotheses,}\quad
(\deg_v\theta,\deg_v\sigma)=(1,2)
\quad\Longrightarrow\quad y_t\ne0.
}
\tag{18}
\]
The derivative is unchanged by the actual constant translation(3),
so the statement applies before or after removal of gamma*t from n.

## 4. Scope and verification boundary

The argument uses the actual strong complex-field return to get(6).
Whole return only over L would not justify that step. No identification
of S=ker(partial_t) with C(s), no algebraic-extension splitting, and
no coefficient-dependent ambient translation is used. In particular
V is not asserted to be an original polynomial coordinate.

Only the calibrated scalar at X=0 was needed after entry; it was
obtained from the full actual scalar, not assumed for an arbitrary
quadratic parametrization. The complete third potential fixes A and B.
No formal constant-y example satisfying fewer identities is claimed
to be an actual frame or a cancellation counterexample.

The complete held387 and the actual transport/boundary source384
were freshly read. Fresh unsaved5d4126 independently reconstructed
the literal matrix(10), the full determinant(11), and all four
successive coefficients(12),(14),(16),(17), with zero residuals.
The exact-field constants, actual translation and strong-return
argument are the written proof, not finite-test certificates.
No saved checker was executed, imported, compiled or rerun.
No held source or canonical record was edited. No recognition,
arbitrary-entry, unrestricted cancellation, novelty, human-expert
review or proof-assistant certification claim is made.

