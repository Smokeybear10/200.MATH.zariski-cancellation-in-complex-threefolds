# Recognition with a constant transverse slope

Working corollary, retaining427's recognition dependencies: under
EVERY supplied actual hypothesis of264, assume
\[
k_s=m\in\mathbb C^*,\qquad n_s=\nu\in\mathbb C,
\qquad m\ell_s+\nu^2=0.
\tag{1}
\]
Then the original kernel is isomorphic to C^[3]. There is no
restriction on k_ttt or n_ttt, and nu may be zero. The actual
complex polynomial map reducing this statement to427 is
\[
\boxed{X^*=X+\nu/m,\quad Y^*=Y,\quad Z^*=Z,\quad
W^*=mW+2(\nu/m)Z.}
\tag{2}
\]
It does not remove the arbitrary longitudinal part of k. It makes
both transformed coefficient potentials independent of the second
parameter. All field-valued expressions below are coefficients of
this actual map, not substituted ambient coordinates.

## 1. Full actual input and first scaling

Retain the complete actual entry of
[264](principal-one-affine-paraboloid-chart-pass264-working.md):
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,
\quad A=\ker E,\quad \deg_E(X,Y,Z,W)=(1,2,2,2),\\
a_0=EX\ne0,\qquad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the full initial kernel},\\
N=[u^4]\partial_Z|_A\ne0,\quad
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,
\quad Na_0=Nt=Ns=0,\quad Nv=1,\\
O=L[v]=L[y,\sigma,\theta]=L[y,z,w],\quad
K=\operatorname{Frac}A=L(v)=\mathbb C(y,z,w),\\
J_{t,s,v}(X)=\det\frac{\partial(Y,Z,W)}{\partial(t,s,v)}
                         =-a_0^4\in L^*.
\end{gathered}
\tag{3}
\]
The original global slice, localization, exact commuting coefficient
partials, genuine potential identities and full scalar are retained.
Their joint coefficient constant field is C. The intercept and linear
coefficients lie in A localized at a0. The literal expansions are
\[
Y=y+\sigma X+tX^2,\quad
Z=z+(2t\sigma+k)X+t^2X^2,\quad
W=w+\theta X+sX^2.
\tag{4}
\]

First fix X,Y,Z and set W1=mW. Its inverse divides only by the
nonzero complex number m. At fixed X it gives
\[
t_1=t,\quad s_1=ms,\quad \theta_1=m\theta,
\quad w_1=mw,\quad k_1=k,\quad n_1=n,\quad\ell_1=\ell.
\tag{5}
\]
Here partial_s1=m^(-1)partial_s and partial_t1=partial_t. Thus
\[
(k_1)_{s_1}=1,\qquad(n_1)_{s_1}=B:=\nu/m\in\mathbb C,
\qquad(\ell_1)_{s_1}=-B^2.
\tag{6}
\]
The old and new exact s-constant fields are the same field F,
finite over C(t), with derivative constants C. Consequently, after
renaming this scaled frame and its second parameter as W,s, there
are exact elements f,g,h in F such that
\[
\boxed{k=s+f,\qquad n=Bs+g,\qquad\ell=-B^2s+h.}
\tag{7}
\]
These expressions follow by exact subtraction; they do not assert
F=C(t), or that f,g,h are rational or polynomial in t. Primes below
denote the exact t-derivative on F. In particular f''' may be nonzero.

The complete first two potentials in the scaled frame, initially
keeping n and ell arbitrary to verify the transport, are
\[
\begin{aligned}
z&=2ty+\sigma^2+f'\sigma+\theta+n,\\
w&=\ell-(2\sigma+f')y-\frac{f''}{2}\sigma^2
                        -n_t\sigma-n_s\theta.
\end{aligned}
\tag{8}
\]
The scaling in(5) follows directly from264's undivided second
potential: its leading term m w becomes w1, while the old n_s theta
becomes (n1)_s1 theta1. No derivative of f is discarded.

## 2. Translation and shear with arbitrary longitudinal coupling

In the scaled frame make the actual polynomial map
\[
X^*=X+B,\qquad Y^*=Y,\qquad Z^*=Z,
\qquad W^*=W+2BZ.
\tag{9}
\]
Its inverse is X=X*-B, Y=Y*, Z=Z*, W=W*-2BZ*. Expanding the
literal rows at fixed X* gives the complete coefficients
\[
\begin{aligned}
t^*&=t,&s^*&=s+2Bt^2,&k^*&=s^*+f,\\
y^*&=y-B\sigma+B^2t,&\sigma^*&=\sigma-2Bt,\\
z^*&=z-B(2t\sigma+s+f)+B^2t^2,\\
\theta^*&=\theta+4Bt\sigma+2Bf-4B^2t^2,\\
w^*&=w+2Bz-B\theta-4B^2t\sigma-B^2s-2B^2f+2B^3t^2.
\end{aligned}
\tag{10}
\]
In particular the additional term 2Bf in theta* must be retained.
These coefficients satisfy exactly
\[
\begin{aligned}
Y^*&=y^*+\sigma^*X^*+t(X^*)^2,\\
Z^*&=z^*+(2t\sigma^*+s^*+f)X^*+t^2(X^*)^2,\\
W^*&=w^*+\theta^*X^*+s^*(X^*)^2.
\end{aligned}
\tag{11}
\]
The starred coefficient derivatives, acting on pullbacks to old L,
are
\[
\partial_{s^*}=\partial_s,\qquad
\partial_{t^*}=\partial_t-4Bt\partial_s.
\tag{12}
\]
They restrict to the original exact t-derivative on F.

Direct substitution into the two full potentials gives
\[
\boxed{n^*=n-Bs-B^2t^2+2Bt f'-3Bf,}
\tag{13}
\]
and
\[
\boxed{\begin{aligned}
\ell^*={}&\ell+2Bn-2Bt n_t+4B^2t^2n_s+2Bf n_s-B^2s
             -2B^3t^2\\
          &-2B^2t^2f''+3B^2t f'-4B^2f.
\end{aligned}}
\tag{14}
\]
For explicit verification, before imposing n_s=B,
\[
\begin{aligned}
(n^*)_{s^*}&=n_s-B,\\
(n^*)_{t^*}&=n_t+2B^2t-4Bt n_s+2Bt f''-Bf'.
\end{aligned}
\tag{15}
\]
Inserting(10),(13),(15) into
\[
\begin{aligned}
z^*&=2ty^*+(\sigma^*)^2+f'\sigma^*+\theta^*+n^*,\\
\ell^*&=w^*+(2\sigma^*+f')y^*
              +\frac{f''}{2}(\sigma^*)^2
              +(n^*)_{t^*}\sigma^*+(n^*)_{s^*}\theta^*
\end{aligned}
\tag{16}
\]
cancels all y,sigma,theta terms and gives(13),(14). This proves
the transport with arbitrary n(t,s), ell(t,s) and f in F. It is
not obtained by treating the old fixed-s derivative as fixed-s*.

Differentiating the full identity(14) before applying the constant
slope condition gives
\[
(\ell^*)_{s^*}=\ell_s+2Bn_s-2Bt n_{ts}
                         +(4B^2t^2+2Bf)n_{ss}-B^2.
\tag{17}
\]
Now(6) implies n_ts=n_ss=0, and therefore
\[
\boxed{(n^*)_{s^*}=0,\qquad(\ell^*)_{s^*}=0.}
\tag{18}
\]
Equivalently, using the exact decomposition(7),
\[
\begin{aligned}
n^*&=g-B^2t^2+2Bt f'-3Bf,\\
\ell^*&=h+2Bg-2Bt g'+2B^3t^2
                  -2B^2t^2f''+3B^2t f'-2B^2f,
\end{aligned}
\tag{19}
\]
which are visibly elements of the same exact field F. B=0 is
retained in every formula; it is never divided out.

## 3. Combined original map and all actual gates

Restoring the ORIGINAL W,s before(5), the combined map is(2),
with B=nu/m. Its complete actual inverse is
\[
X=X^*-B,\qquad Y=Y^*,\qquad Z=Z^*,
\qquad W=(W^*-2BZ^*)/m.
\tag{20}
\]
Both inverse orders are polynomial identities. The only inverse
denominator is the nonzero complex constant m. In original parameters
the coefficient changes are
\[
t^*=t,\qquad s^*=ms+2Bt^2,\qquad
k^*=s^*+f,\quad f=k-ms,\qquad a_0^*=a_0,
\tag{21}
\]
with partial_s*=m^(-1)partial_s and
partial_t*=partial_t-(4Bt/m)partial_s. This is the combined
version of(5),(12); the formulas in Section2 use the scaled s.

The weighted leading map fixes X,Y,Z and sends W to mW+2BZ.
It is invertible and preserves the ENTIRE initial ideal
X^2 Z-Y^2. The new W ratio ms+2Bt^2 is nonzero and algebraically
independent of t, so all four actual time degrees remain(1,2,2,2).

The literal selected partial in the ORIGINAL coordinates is
\[
\partial_{Z^*}=\partial_Z-\frac{2B}{m}\partial_W.
\tag{22}
\]
The retained full-initial omitted-pivot bound gives shift at most
three for the old W-partial, whereas the Z-partial has exact shift
four. Hence N*=N, L is unchanged, and the same v has Nv=1. This
also follows from the general actual transport proved in
[426](general-coupling-normalization-obstruction-pass426-working.md).

The transformation of(y,sigma,theta) is invertible affine over L,
so it retains O=L[y*,sigma*,theta*]. The stronger complex return
is rebuilt using the actual localization
B_a0=A_a0[X*]. Evaluation at X*=0 in the new polynomial frame
gives K=C(y*,z*,w*) and L[y*,z*,w*]=O, by264's quotient argument.
Neither conclusion is inferred from a field-valued reframe alone.

The bad-coordinate row determinant in(2) is m at fixed X*. The
coefficient change(t,s,v) to(t*,s*,v) also has determinant m.
Their factors cancel, giving the ENTIRE scalar identity
\[
J^*_{t^*,s^*,v}(X^*)=J_{t,s,v}(X^*-B)=-a_0^4.
\tag{23}
\]
All other actual hypotheses, including the original global slice
and kernel A, therefore survive. This is an actual complex map,
not a field-dependent change with B replaced by a function.

## 4. Recognition and the exact dependency boundary

The completely read working result
[427](principal-paraboloid-arbitrary-longitudinal-coupling-recognition-pass427-working.md)
recognizes every full actual264 chart with k_s a nonzero complex
constant and n_s=ell_s=0. It imposes no k_ttt bound. The starred
chart satisfies precisely those hypotheses by(18),(21)--(23).
Thus, with427's explicitly retained recognition dependencies,
\[
\boxed{\text{Under every actual hypothesis of264,}\quad
k_s=m\in\mathbb C^*,\quad n_s=\nu\in\mathbb C,
\quad m\ell_s+\nu^2=0
\quad\Longrightarrow\quad A\cong\mathbb C^{[3]}.}
\tag{24}
\]

If the original k_ttt is nonzero, then f''' is nonzero in the
starred chart.427 gives y*,sigma* in L, and(10) consequently
gives y,sigma in L as well. Its actual preserved polynomial
three-ring pulls back explicitly to
\[
\mathbb C[X^*,Y^*,W^*-X^*Z^*]
 =\mathbb C[X,Y,mW-(X-B)Z].
\tag{25}
\]
This is an actual coordinate three-ring, with fourth coordinate Z
and inverse division only by m. Its E-stability and primitive
recognition are exactly the original-ring argument in427, not
consequences of a coefficient-field line by itself.

For k_ttt=0,427 instead uses348's actual normalization and337's
retained endpoint. This note does not recursively recertify those
proofs. When nu=0, the present statement is427; for k_ttt=0 it
overlaps422. Its additional conditional coverage is the transverse
relation in(1) without a longitudinal derivative bound. It does
not force that relation in an arbitrary chart or normalize arbitrary
nonconstant k_s. In particular426's filtered obstruction remains
valid: map(2) retains the arbitrary function f rather than setting
k*=s*.

## 5. Source and exact-check record

The full264 source was read for the current general-coupling work.
The full current426 source was reread through5b6ce1+1b4267.
The complete427 source was read through EOF2c41a4 and rehashed in
b2d6c2 at6626b178ea33e9cee5e1d8f697109b8cff3659d60645917cb2b53a690623409e.
General reported its separate complete independent audit clean at
that hash before this corollary was finalized. The recognition
dependencies in427 remain retained, not silently reproved here.

Fresh unsaved510968 reconstructs all three complete rows(10)--(11),
both potentials(13)--(16), the unspecialized transverse derivative(17),
the exact one-variable formulas(19), and both combined inverse orders.
All residuals are zero. These finite identities support the written
actual transport and do not assert that arbitrary formal coefficient
data has an actual realization. Independent saved-source review of
this corollary is separate from author verification.

No saved checker was executed, imported, compiled or rerun. No earlier
proof or canonical file was edited. No unrestricted cancellation,
arbitrary-coordinate entry, expert verification, novelty clearance,
formal proof-assistant certification or external submission is claimed.
