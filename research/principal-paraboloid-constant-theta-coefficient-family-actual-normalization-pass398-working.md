# Actual normalization of the constant-theta coefficient family

Working normalization lemma in the complete actual264 chart with
k=s and theta in the exact coefficient field. If the coefficient
family (3) below holds, a complex polynomial automorphism normalizes
its four constants tau,s0,gamma,c0 to zero. The full initial kernel,
literal selected partial, exact time profile, both actual returns,
and calibrated scalar are preserved. The parameter eta may be zero.

This note does not derive the coefficient family, exclude its
normalized form, or recognize an original invariant coordinate.
In particular it does not apply387's nonconstant-theta rank gate
to the constant-theta boundary.

## 1. Exact actual input and the coefficient family being normalized

Retain every hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md)
and the actual constant-theta line presentation of
[386](principal-paraboloid-nonlinear-constant-theta-line-gates-pass386-working.md).
Use distinct names for the global-slice derivation E and the
complex coefficient constants. Thus
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A_0[u],\qquad E=\partial_u,\qquad
\deg_E(X,Y,Z,W)=(1,2,2,2),\quad a_0=EX\ne0,\\
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2),\qquad
0\ne N=[u^4]\partial_Z|_{A_0},\qquad
L=\operatorname{Frac}\ker_{A_0}N,\\
[L:\mathbb C(t,s)]<\infty,\qquad Nv=1,\qquad
O=L[v]=L[y,\sigma,\theta]=L[y,z,w],\\
K=\operatorname{Frac}A_0=L(v)=\mathbb C(y,z,w),\qquad
\theta\in L,\quad O=L[\sigma],\quad
y=\lambda\sigma+r,\quad \lambda\in L^*,\ r\in L.
\end{gathered}
\tag{1}
\]
The nonzero slope can be supplied by396. This lemma needs no further
conclusion of that note. The exact coefficient partials commute,
are the extensions of partial_t and partial_s, and have joint
constants C. The parameters t,s are algebraically independent over C.

The actual rows, two potentials and scalar are
\[
\begin{aligned}
Y&=y+\sigma X+tX^2,\\
Z&=z+(2t\sigma+s)X+t^2X^2,\\
W&=w+\theta X+sX^2,\\
z&=2ty+\sigma^2+\theta+n,\\
w&=\ell-2\sigma y-n_t\sigma-n_s\theta,\\
\det\frac{\partial(Y,Z,W)}{\partial(t,s,v)}&=-a_0^4\in L^*.
\end{aligned}
\tag{2}
\]
Assume the following exact coefficient identities, rather than a
rational ansatz or only leading asymptotics:
\[
\begin{gathered}
T=t-\tau,\qquad S=s-s_0,\qquad
\tau,s_0,\eta,\gamma,c_0\in\mathbb C,\\
\lambda=\frac{S}{2T^2},\qquad
n=-\frac{S^2}{4T^2}+\frac{\eta S}{T}+\gamma t+c_0.
\end{gathered}
\tag{3}
\]
No nonzero assumption is made on any of these five complex constants.
The denominators T and the slope numerator S are nonzero field
elements because t,s are algebraically independent. Here S is a
new coefficient parameter, not the name of a coefficient subfield.

## 2. Four actual operations and both potentials

First shift the t parameter by the actual polynomial operation
\[
X_1=X,\quad Y_1=Y-\tau X^2,\quad
Z_1=Z-2\tau Y+\tau^2X^2,\quad W_1=W.
\tag{4}
\]
Its inverse is
X=X1, Y=Y1+tau*X1^2, Z=Z1+2tau*Y1+tau^2*X1^2, W=W1.
Substitution into (2) gives t1=T, s1=s, k1=s1 and
\[
\sigma_1=\sigma,\quad\theta_1=\theta,\quad
y_1=y,\quad z_1=z-2\tau y,\quad w_1=w,
\qquad n_1=n,\quad\ell_1=\ell.
\tag{5}
\]
The last two identities are identities of elements of L expressed
using t1,s1. Their derivatives are now taken in the new coefficient
parameters, with partial_t1=partial_t and partial_s1=partial_s.
Indeed z1=2T*y+sigma^2+theta+n, and the second potential in (2)
is unchanged. No term involving ell or n was dropped in the shift.

Next shift the s parameter through
\[
X_2=X_1,\quad Y_2=Y_1,\quad
Z_2=Z_1-s_0X_1,\quad W_2=W_1-s_0X_1^2.
\tag{6}
\]
Its inverse adds s0*X2 to Z2 and s0*X2^2 to W2, fixing X2,Y2.
It gives t2=T, s2=S and k2=S. The intercepts and intrinsic linear
coefficients in (5) are unchanged. The elements n2=n1 and
ell2=ell1 are now expressed using T,S, with the same coefficient
partial operators. In particular the family has become
\[
n_2=-\frac{S^2}{4T^2}+\frac{\eta S}{T}
          +\gamma T+\overline c,\qquad
\overline c=\gamma\tau+c_0\in\mathbb C.
\tag{7}
\]

Third take Y3=Y2+gamma/2, fixing X2,Z2,W2. Its inverse subtracts
gamma/2. The coefficient y changes to y3=y+gamma/2, while sigma,
theta,z2,w and T,S stay unchanged. The first potential gives
\[
n_3=n_2-\gamma T,\qquad \ell_3=\ell_2.
\tag{8}
\]
For the second identity, the term -2sigma*y3 introduces -gamma*sigma,
while (n3)_T=(n2)_T-gamma introduces the opposite term in
-(n3)_T*sigma. The s derivative is unchanged. Thus ell3 really equals
ell2, without assuming n_ts=0 or any other derivative condition.

Finally set Z4=Z3-cbar, fixing X3,Y3,W3. The inverse adds cbar.
Its sole intercept change is z4=z2-cbar. Therefore
\[
n_4=n_3-\overline c=-\frac{S^2}{4T^2}+\frac{\eta S}{T},
\qquad\ell_4=\ell_3.
\tag{9}
\]
The constant subtraction does not change either coefficient derivative
of n3 and consequently leaves the second potential intact.

## 3. The complete map, inverse and literal coefficient transports

Write stars for the resulting actual coordinates. Combining the four
operations gives the single complex polynomial map
\[
\boxed{
\begin{aligned}
X^*&=X,\\
Y^*&=Y-\tau X^2+\gamma/2,\\
Z^*&=Z-2\tau Y+\tau^2X^2-s_0X-(\gamma\tau+c_0),\\
W^*&=W-s_0X^2.
\end{aligned}}
\tag{10}
\]
Its polynomial inverse is
\[
\boxed{
\begin{aligned}
X&=X^*,\\
Y&=Y^*+\tau(X^*)^2-\gamma/2,\\
Z&=Z^*+2\tau Y^*+\tau^2(X^*)^2+s_0X^*+c_0,\\
W&=W^*+s_0(X^*)^2.
\end{aligned}}
\tag{11}
\]
Both orders of substitution give the identity. In particular the
constant in the inverse Z expression is c0, not gamma*tau+c0:
the constant contributed by 2tau*Y cancels the extra gamma*tau.
Both the four-variable Jacobian and the fixed-X three-variable
Jacobian of (10) are one.

The full coefficient data are
\[
\begin{gathered}
t^*=T=t-\tau,\quad s^*=S=s-s_0,\quad k^*=s^*,\\
\sigma^*=\sigma,\quad\theta^*=\theta,\quad
y^*=y+\gamma/2,\quad
z^*=z-2\tau y-(\gamma\tau+c_0),\quad w^*=w,\\
n^*=n-\gamma t-c_0,
\qquad \ell^*=\ell,\qquad
\lambda^*=\lambda=\frac{s^*}{2(t^*)^2},\quad r^*=r+\gamma/2.
\end{gathered}
\tag{12}
\]
The expressions n*,ell* in new parameters are obtained by the
constant substitution t=t*+tau, s=s*+s0. Thus the last ell identity
means pullback of the full coefficient function, not that its
formula in named parameters must look unchanged. In particular
\[
\begin{gathered}
\partial_{t^*}n^*=n_t-\gamma,\quad
\partial_{s^*}n^*=n_s,\quad
\partial_{t^*}\ell^*=\ell_t,\quad
\partial_{s^*}\ell^*=\ell_s,\\
z^*=2t^*y^*+(\sigma^*)^2+\theta^*+n^*,\qquad
w^*=\ell^*-2\sigma^*y^*
      -(n^*)_{t^*}\sigma^*-(n^*)_{s^*}\theta^*.
\end{gathered}
\tag{13}
\]
All derivatives are exact coefficient derivatives at the indicated
holding variables. There is no change of the original slice variable
u and no L-valued translation of an original coordinate.

## 4. Exact time degrees and the full initial kernel

The original derivation E and its kernel A0 do not change. Since
X*=X, its leader is still a0. The new four leaders are
\[
a_0,\quad a_0^2(t-\tau),\quad
a_0^2(t-\tau)^2,\quad a_0^2(s-s_0).
\tag{14}
\]
Algebraic independence of t,s makes all four nonzero. Hence the
exact time profile remains (1,2,2,2), not merely an upper bound.

For full-kernel preservation, use independent weighted symbols with
weights(1,2,2,2). The leading transformation of (10) is the graded
polynomial automorphism
\[
\mathsf X\mapsto\mathsf X,\quad
\mathsf Y\mapsto\mathsf Y-\tau\mathsf X^2,\quad
\mathsf Z\mapsto\mathsf Z-2\tau\mathsf Y+\tau^2\mathsf X^2,\quad
\mathsf W\mapsto\mathsf W-s_0\mathsf X^2.
\tag{15}
\]
It fixes the polynomial \(\mathsf X^2\mathsf Z-\mathsf Y^2\) exactly.
Its inverse is the leading part of (11). Composing the original
leader map with this graded automorphism therefore preserves its
entire kernel ideal, not just membership of the displayed relation.
The new full initial kernel is again
\((\mathsf X^2\mathsf Z-\mathsf Y^2)\).

## 5. Literal partial, exact fields, both returns and calibration

The inverse (11) gives the identity of actual derivations
\[
\partial_{Z^*}=\partial_Z.
\tag{16}
\]
Indeed, when X*,Y*,W* are fixed, only old Z varies, with derivative
one. Thus the selected derivation N*=[u^4]partial_Z* restricted to
A0 is exactly N. Its nonzero shift, kernel field L, generic polynomial
line O, and parameter v with Nv=1 are unchanged.

The coefficient-field bases satisfy C(t*,s*)=C(t,s). The extensions
of their partials to L are identical because the parameter change
is by complex constants. Consequently finiteness, commutation and
the exact joint constant field are all retained. The intrinsic sigma
and theta are unchanged, so theta* remains in L and sigma* remains
affine nonconstant on the same line. Also
\[
L[y^*,\sigma^*,\theta^*]=L[y,\sigma,\theta]=O.
\tag{17}
\]
For the intercept returns, (12) is an invertible complex affine
transformation of (y,z,w). Explicitly
y=y*-gamma/2, z=z*+2tau*y*+c0, w=w*.
It follows directly that
\[
\mathbb C(y^*,z^*,w^*)=K,\qquad
L[y^*,z^*,w^*]=O.
\tag{18}
\]
Thus strong complex-field return and whole polynomial return have
both been checked separately; neither is inferred from the other.

At fixed actual X*=X, the output Jacobian on Y,Z,W is one, and the
coefficient-parameter Jacobian from t,s,v to t*,s*,v is also one.
The full scalar therefore remains
\[
\det\frac{\partial(Y^*,Z^*,W^*)}{\partial(t^*,s^*,v)}
=-a_0^4\in L^*.
\tag{19}
\]
If sigma is used instead of v, put omega=N sigma in L*. This same
identity is -a0^4/omega in either frame. There is no conflation of
that intrinsic derivative with the complex time-shift constant tau.

The resulting data satisfy every actual264 hypothesis again. The
genuine higher potentials are consequently available from their
literal derivation in this new frame, not from an unsupported formal
substitution into an arbitrary curve equation.

## 6. Precisely licensed normalized family

Drop stars only after the actual maps and gates above. The supplied
family is reduced to
\[
\boxed{
\lambda=\frac{s}{2t^2},\qquad
n=-\frac{s^2}{4t^2}+\frac{\eta s}{t},\qquad
\eta\in\mathbb C,\quad
\theta\in L,\quad y=\lambda\sigma+r.
}
\tag{20}
\]
In particular n_ss=-1/(2t^2) is still nonzero, and eta=0 has not
been discarded. No claim that n=f(s), or that an intrinsic parameter
is an original coordinate, is made. Entry into (3) is a separate
coefficient-classification input; the normalization lemma itself is
conditional only on that exact family and the full actual hypotheses.

The entire264 and386 sources were freshly read through EOF in211a1d.
Fresh unsaved441934 reconstructed both orders of the full inverse,
both Jacobians, all literal rows, both potential transports, the
normalized n family, the full graded relation, and the exact
Z*-partial. Every displayed residual was zero. The full-kernel,
exact-field and both-return arguments are given above, not inferred
from those finite identities.

No saved checker was executed, imported, compiled or rerun. No
earlier source or canonical index was edited. This is an actual
normalization license, not an exclusion, original-ring recognition,
arbitrary-chart entry theorem, or unrestricted cancellation result.
No novelty, human-expert review or formal certification is claimed.
