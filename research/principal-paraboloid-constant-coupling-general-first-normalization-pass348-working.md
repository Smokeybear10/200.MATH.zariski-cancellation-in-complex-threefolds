# Actual normalization without a third-derivative bound on the first potential

Working recognition result, with346's retained dependencies: in the full
actual principal chart264, the derivative-only conditions
\[
k_s=m\in\mathbb C^*,\qquad k_{ttt}=0,\qquad
n_{ss}=n_{ts}=0
\tag{1}
\]
suffice to recognize the original kernel as C^[3]. No hypothesis on
n_ttt or on the second potential ell is imposed.

The proof is an explicit complex polynomial reframe to k*=s* and
(n*)_s*=0, followed by346. The remaining first potential is an element
of an exact finite curve field, not necessarily a rational function or
a polynomial in t. This does not normalize variable k_s, nonzero k_ttt,
or variable n_s, and does not address arbitrary-coordinate entry.

## 1. Full actual entry and exact integration

Retain all actual hypotheses of
[264](principal-one-affine-paraboloid-chart-pass264-working.md), including
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,
\quad A=\ker E,\quad a_0=EX\ne0,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\qquad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the full weighted initial kernel},\\
N=[u^4]\partial_Z|_A\ne0,\quad
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,
\quad Na_0=Nt=Ns=0,\quad Nv=1,\\
K=\operatorname{Frac}A=L(v)=\mathbb C(y,z,w),\qquad
L[y,z,w]=L[y,\sigma,\theta]=L[v],\\
\det\frac{\partial(Y,Z,W)}{\partial(t,s,v)}=-a_0^4\in L^*.
\end{gathered}
\tag{2}
\]
All coefficient partials are the exact commuting extensions to L and
fix v. Their joint constant field is C. The original E kills L and
all intercept functions. The literal map is
\[
Y=y+\sigma X+tX^2,\quad
Z=z+(2t\sigma+k)X+t^2X^2,\quad
W=w+\theta X+sX^2.
\tag{3}
\]

Under(1), both partials kill k_tt: its t-derivative is zero by
hypothesis, and its s-derivative is (k_s)_tt=0. Thus k_tt=gamma is
complex. Exact subtraction and the same joint-constant argument give
\[
k=ms+\frac\gamma2t^2+bt+d,
\qquad m\in\mathbb C^*,\quad\gamma,b,d\in\mathbb C.
\tag{4}
\]
Similarly n_s is killed by both partials, so nu:=n_s belongs to C.
Define
\[
\alpha=\nu/m\in\mathbb C,\qquad B=\alpha-\gamma/2\in\mathbb C,
\qquad f=n-\alpha k\in\mathbb F:=\ker_L\partial_s.
\tag{5}
\]
The field F is the relative algebraic closure of C(t) in L, finite
over C(t), and its t-derivative has constants C. Writing f(t) below
means membership in this exact field, not membership in C(t).
Primes on f mean its exact t-derivative. No bound on any derivative
of f is assumed. In particular
\[
n=\alpha k+f,\quad n_t=\alpha k_t+f',\quad
n_s=\alpha m,\quad k_t=\gamma t+b.
\tag{6}
\]
Conversely(4)--(6), with arbitrary f in F, imply all identities(1).

The first two literal potentials consequently take the complete form
\[
\begin{aligned}
z&=2ty+\sigma^2+k_t\sigma+m\theta+n,\\
mw&=\ell-(2\sigma+k_t)y-\frac\gamma2\sigma^2
                  -(\alpha k_t+f')\sigma-\alpha m\theta.
\end{aligned}
\tag{7}
\]
No lower term of ell or f is suppressed.

## 2. First actual stage and both transported potentials

Fix X,Y,Z and define
\[
W_1=mW+\frac\gamma2Z+bY+dX^2,
\qquad
W=\frac{W_1-\gamma Z/2-bY-dX^2}{m}.
\tag{8}
\]
This is an actual polynomial map with polynomial inverse over C.
At fixed X, substitution of(3) gives
\[
\begin{aligned}
t_1&=t,&s_1&=k,&k_1&=s_1,\\
y_1&=y,&\sigma_1&=\sigma,&z_1&=z,\\
\theta_1&=m\theta+k_t\sigma+\gamma k/2,
&w_1&=mw+\gamma z/2+by.
\end{aligned}
\tag{9}
\]
The coefficient derivatives are
\[
\partial_{s_1}=m^{-1}\partial_s,\qquad
\partial_{t_1}=\partial_t-(k_t/m)\partial_s.
\tag{10}
\]
They restrict to the same t-derivative on F. Directly from(7),
\[
\begin{aligned}
z_1&=2ty_1+\sigma_1^2+\theta_1+n_1,
&n_1&=Bk+f=Bs_1+f,\\
w_1+2\sigma_1y_1+f'\sigma_1+B\theta_1&=\ell_1,
&\ell_1&=\ell+\gamma n/2+\gamma Bk/2.
\end{aligned}
\tag{11}
\]
Here (n1)_t1=f' and (n1)_s1=B. In the second identity the sigma
and theta terms cancel using alpha=B+gamma/2; the y terms cancel
using k_t=gamma t+b. Neither cancellation uses f'' or f'''.
This extends the literal transport in302/334 without importing their
earlier factorization or complex-quadratic restrictions.

## 3. Second actual stage with arbitrary f

Starting from(9)--(11), put
\[
X_*=X+B,\quad Y_*=Y,\quad Z_*=Z,\quad W_*=W_1+2BZ.
\tag{12}
\]
This again is an actual complex polynomial automorphism, with inverse
X=X*-B, Y=Y*, Z=Z*, W1=W*-2BZ*. Full substitution at fixed X* gives
\[
\begin{aligned}
t_*&=t,&s_*&=k+2Bt^2,&k_*&=s_*,\\
y_*&=y-B\sigma+B^2t,&\sigma_*&=\sigma-2Bt,\\
z_*&=z-2Bt\sigma-Bk+B^2t^2,\\
\theta_*&=\theta_1+4Bt\sigma-4B^2t^2,\\
w_*&=w_1+2Bz-B\theta_1-4B^2t\sigma-B^2k+2B^3t^2.
\end{aligned}
\tag{13}
\]
The full literal shape is preserved:
\[
\begin{aligned}
Y_*&=y_*+\sigma_*X_*+tX_*^2,\\
Z_*&=z_*+(2t\sigma_*+s_*)X_*+t^2X_*^2,\\
W_*&=w_*+\theta_*X_*+s_*X_*^2.
\end{aligned}
\tag{14}
\]
The combined new coefficient partials in terms of the original ones are
\[
\partial_{s,*}=m^{-1}\partial_s,\qquad
\partial_{t,*}=\partial_t-
 \frac{(\gamma+4B)t+b}{m}\partial_s.
\tag{15}
\]
In particular their s*-constant field is the same F, and they retain
the same t-derivative on F. The complete transported potentials are
\[
\boxed{\begin{aligned}
z_*&=2ty_*+\sigma_*^2+\theta_*+n_*,
&n_*&=f-B^2t^2,\\
w_*+2\sigma_*y_*+(f'-2B^2t)\sigma_*&=\ell_*,\\
\ell_*&=\ell_1+B^2k+2Bf-2Bt f'+2B^3t^2.
\end{aligned}}
\tag{16}
\]
Thus (n*)_s*=0 and (n*)_t*=f'-2B^2t exactly. Equations(16) are
identities in the old field L; expressing them in the new parameters
means substituting the invertible coefficient change(13),(15), not
silently applying old derivatives to functions at fixed s*.

For comparison with the older quadratic formula, if
f=Dt^2+At+C with complex coefficients, the last line becomes
ell1+B^2k+2BC-2B(D-B^2)t^2. The present calculation does not assume
that specialization and does not make the actual translations that
would remove its affine terms.

## 4. Combined inverse and all actual chart gates

The combined map and its inverse are
\[
\boxed{\begin{aligned}
X_*&=X+B,&Y_*&=Y,&Z_*&=Z,\\
W_*&=mW+(\gamma/2+2B)Z+bY+dX^2;
\end{aligned}}
\tag{17}
\]
\[
\begin{aligned}
X&=X_*-B,&Y&=Y_*,&Z&=Z_*,\\
W&=\frac{W_*-(\gamma/2+2B)Z_*-bY_*-d(X_*-B)^2}{m}.
\end{aligned}
\tag{18}
\]
Both inverse orders are literal polynomial identities. The only division
in this actual inverse is by the nonzero complex number m. B, gamma,
b, d and nu may vanish; none of them is divided out.

The weighted leading transformation fixes X,Y,Z and sends W to
mW+(gamma/2+2B)Z+bY+dX^2. It is invertible and fixes the entire
initial ideal X^2Z-Y^2, which is independent of W. The new leading
ratio s*=m s+(gamma/2+2B)t^2+bt+d is nonzero and independent of t
because t,s are algebraically independent and m is nonzero. Thus
all four actual E-degrees remain(1,2,2,2), and EX*=a0.

The new literal selected partial is
\[
\partial_{Z_*}=\partial_Z-
                   \frac{\gamma/2+2B}{m}\partial_W.
\tag{19}
\]
The old W-partial has horizontal shift at most three by the retained
omitted-leading-triple gate: its omitted X,Y,Z leaders satisfy the
relation X^2Z-Y^2, whereas the literal Z-partial has exact shift four.
Thus(19) has the same shift-four leading N. The exact field L, the
line O and the chosen Nv=1 are unchanged. This is the same actual
partial argument supplied in the fully read302,332,334; no claim of
preserving an old chosen surface factor is needed.

The two transformations of (y,sigma,theta) in(9),(13) are invertible
affine maps over L, so their whole O-return is preserved. For the
strong complex intercept return, use the actual quotient separately:
\[
\mathcal B_{a_0}=A_{a_0}[X_*],\qquad
X_*=a_0u+c_*,\quad c_*\in A.
\tag{20}
\]
Evaluation at X*=0 in the actual starred polynomial frame gives
A_a0=C[y*,z*,w*] localized at the evaluated a0. That evaluated
element is a polynomial in the three intercepts, since a0 was an
original polynomial in the starred coordinates and is invariant.
Taking fractions and then the usual N-constant localization proves
\[
K=\mathbb C(y_*,z_*,w_*),\qquad
L[y_*,z_*,w_*]=O.
\tag{21}
\]
These equalities are not inferred from invertibility over L alone.

Finally the row map on Y,Z,W at fixed X* has determinant m. Its
dX^2 term contributes no coefficient differential, because X=X*-B
is held fixed and B,d are complex. The parameter change(t,s) to
(t,s*) also has determinant m, so the inverse chain-rule factor is
1/m. Consequently the entire calibrated polynomial satisfies
\[
J_*(X_*)=J(X_*-B)=-a_0^4.
\tag{22}
\]
All actual hypotheses of264 therefore survive, including the full
initial ideal, particular selected derivation, both returns and scalar.

## 5. Scoped recognition through346

The completely read working theorem
[346](principal-one-variable-first-potential-recognition-pass346-working.md)
recognizes every supplied full actual264 chart with k=s and n_s=0,
allowing the first potential to lie in the exact finite curve field and
placing no additional condition on ell. The starred chart has exactly
these hypotheses by(14)--(22). Therefore, with346's stated retained
working dependencies,
\[
\boxed{\text{Under the full actual chart(2),}\quad
k_s\in\mathbb C^*,\ k_{ttt}=0,\ n_{ss}=n_{ts}=0
\quad\Longrightarrow\quad A\cong\mathbb C^{[3]}.}
\tag{23}
\]
This removes n_ttt=0 from334/344's derivative-only family. It does
not prove that a general actual principal chart satisfies the four
displayed conditions, normalize variable n_s, or allow k_ttt nonzero.
No unrestricted cancellation theorem, historical novelty, or independent
recursive certification of all retained recognition inputs is claimed.

The direct sources264,302,332,334 and346 were read completely before
this proof. A fresh unsaved symbolic reconstruction retained arbitrary
f,f' and ell, verified both full potential transports and all three
whole-X coordinate identities, and checked both inverse orders and
both determinant factors. All residuals were zero. Those finite checks
do not prove the exact-field, localization or recognition statements.
No saved checker was executed, imported or compiled; no earlier proof,
checker, canonical index or ledger was edited.
