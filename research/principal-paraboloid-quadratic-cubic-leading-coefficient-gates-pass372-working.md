# Leading coefficient gates for the remaining quadratic-cubic profile

Working necessary conditions: in the complete actual theta-dominant
chart with intrinsic degrees (deg sigma,deg theta)=(2,3), the actual
normalization369 permits n=-s^2/(4t^2)+f(t). The two highest
coefficients of the genuine fourth potential then determine the
quadratic and linear coefficients of sigma unless a one-variable
derivative E vanishes. That exceptional case forces a complex
constant square-presentation term and explicitly integrates f and
the s dependence of ell.

This is a reduction, not exclusion or recognition of either case.
All coefficient fields remain the exact finite fields of the actual
chart. No coefficient-field parameter becomes an original coordinate.

## 1. Complete actual entry and an affine intrinsic parameter

Retain every actual hypothesis of
[365](principal-paraboloid-nonlinear-intercept-unequal-degree-gate-pass365-working.md),
the genuine fourth potential and calibrated scalar supplied there
from264/296, and the actual normalization of
[369](principal-paraboloid-nonlinear-intercept-linear-coefficient-normalization-pass369-working.md).
In particular
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\quad E_{\rm slice}=\partial_u,
\quad\deg_{E_{\rm slice}}(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(X^2Z-Y^2)\text{ is the full initial kernel},
\quad a_0=E_{\rm slice}X\ne0,\\
N=[u^4]\partial_Z|_A,\quad L=\operatorname{Frac}\ker_A N,
\quad [L:\mathbb C(t,s)]<\infty,\\
O=L[v]=L[y,\sigma,\theta]=L[y,z,w],\quad Nv=1,
\quad L(v)=\mathbb C(y,z,w).
\end{gathered}
\tag{1}
\]
The literal map and its lower potentials are
\[
\begin{aligned}
Y&=y+\sigma X+tX^2,\\
Z&=z+(2t\sigma+s)X+t^2X^2,\\
W&=w+\theta X+sX^2,\\
z&=2ty+\sigma^2+\theta+n,\qquad
w=\ell-2\sigma y-n_t\sigma-n_s\theta,
\end{aligned}
\qquad
J_{t,s,v}(X)=-a_0^4\in L^*.
\tag{2}
\]
The coefficient partials commute, have joint constants C, and
F=ker_L(partial_s) is finite over C(t) with t-derivative constants C.
Neither F=C(t) nor L=F(s) is asserted.

Assume the intrinsic degree pair is (2,3). The actual complex
maps of369 preserve all the inputs and arrange
\[
n=-\frac{s^2}{4t^2}+f,\qquad f\in F.
\tag{3}
\]
Primes on f or on an element of F denote the exact t-derivative.
Set
\[
g=\frac{f''}{2},\quad \nu=-\frac{s}{2t^2},\quad
C=\ell_s+\frac{s^2}{4t^4},\quad
\Lambda=\frac{2sC}{t}+\ell_t.
\tag{4}
\]
The nonzero quadratic coefficient Omega of365 is precisely g,
so g is nonzero. Its formal remainder is
\[
R=U+\frac{V}{2t}+\frac{n_t}{2}-\frac{sP}{2t^2}+tC.
\tag{5}
\]
It has degree 2 deg sigma-deg theta=1 after evaluation at
(U,P,V)=(y,sigma,theta). Use that evaluation as an intrinsic
parameter r. Then O=L[r], rho=Nr belongs to L*, and uniquely
\[
\sigma=a r^2+b r+e,\qquad a\in L^*,\quad b,e\in L.
\tag{6}
\]
Here a is not the slice speed a0; e is a constant coefficient
of sigma, not n_ss. Changing v to r rescales the nonzero scalar
by rho, so J_(t,s,r)(X)=-a0^4/rho in L*. Coefficient partials
on L are unchanged by this parameter change.

## 2. The full quadric determines theta and the level h

In the independent formal variables P,R,V, the third level is
\[
H-h=gP^2+\left(\frac{2sR}{t^2}-\Lambda\right)P
 +R^2-2tCR+D-\frac{RV}{t},
\qquad D=t^2C^2-\bar h,
\quad \bar h=h-\nu\ell+\frac{n_t^2}{4}.
\tag{7}
\]
Substitute R=r and P=sigma. Polynomiality of theta forces
D=Lambda e-g e^2 by the constant coefficient at r=0.
Consequently
\[
\begin{aligned}
\theta&=\frac{t}{r}\left\{
g(\sigma^2-e^2)-\Lambda(\sigma-e)
 +\frac{2sr\sigma}{t^2}+r^2-2tCr\right\},\\
y&=r-\frac{\theta}{2t}+\frac{s\sigma}{2t^2}
 -\frac{n_t}{2}-tC,\\
h&=t^2C^2-\Lambda e+g e^2+\nu\ell-\frac{n_t^2}{4}.
\end{aligned}
\tag{8}
\]
The braces are divisible by r because sigma-e is. Thus (8)
is an identity in L[r], not a localization discarding r=0.
The leading coefficient of theta is t g a^2, which is nonzero.

Define two coefficient functions
\[
G=f-tf'-\frac{3s^2}{2t^2}-2t^2\ell_s,
\qquad E=\frac{g'}3+\frac gt\in F.
\tag{9}
\]
Here E is unrelated to the slice derivation E_slice. Substitution
in the full Z expression of (2) gives the useful exact identity
\[
\boxed{Z=\left(\sigma+tX+\frac{s}{2t}\right)^2+2tr+G.}
\tag{10}
\]
In particular G constant does not alone make an actual coordinate
a square: the extra term 2tr is present and nonzero.

## 3. The two highest coefficients of the genuine fourth potential

Let Q be exactly365 equation(7), with coefficient derivatives taken
before evaluating at (y,sigma,theta), and let q0 be its level in L.
Using (8), define q_i=[r^i]Q(y,sigma,theta). The exact identities are
\[
\begin{aligned}
q_6&=a^3\left(E+\frac{a g^2G_s}{4}\right),\\
q_5-\frac{3b}{a}q_6
 &=a^3g\left(\frac{sG_s}{t^2}
               +\frac{b gG_s}{4}+\frac{G_t}{2t}\right).
\end{aligned}
\tag{11}
\]
These use the complete fourth polynomial, not merely its cubic
homogeneous part. For inspection the two derivatives in (11) are
\[
G_s=-\frac{3s}{t^2}-2t^2\ell_{ss},\qquad
G_t=-tf''+\frac{3s^2}{t^3}-4t\ell_s-2t^2\ell_{ts}.
\tag{12}
\]
One can verify (11) directly without a formula for h_t,h_s:
those appear in Q only as -h_t P-h_s V, which after evaluation
have degrees at most two and three. All other terms of365(7)
are retained. The derivative data needed are
\[
\begin{gathered}
n_t=s^2/(2t^3)+f',\quad n_{tt}=-3s^2/(2t^4)+f'',\quad
n_{ts}=s/t^3,\quad n_{ss}=-1/(2t^2),\\
n_{ttt}=6s^2/t^5+f''',\quad n_{tts}=-3s/t^4,
\quad n_{tss}=1/t^3,\quad n_{sss}=0.
\end{gathered}
\tag{13}
\]
Expanding that finite polynomial with sigma=a r^2+b r+e and
(8) gives (11). Since Q evaluates to a constant, q6=q5=0.
Division only by the already nonzero a,g,t gives
\[
\boxed{
E+\frac{a g^2G_s}{4}=0,\qquad
2tG_t+(4s+t^2b g)G_s=0.
}
\tag{14}
\]

## 4. The nonzero and zero E alternatives

If E is nonzero, then G_s is nonzero, and (14) determines
\[
\boxed{
a=-\frac{4E}{g^2G_s},\qquad
b=-\frac{2tG_t+4sG_s}{t^2gG_s}.
}
\tag{15}
\]
The remaining coefficients, lower fourth-level equations, and full
scalar still constrain G,f,e. Formula (15) is not a realization.

If E=0, the first equation of (14) forces G_s=0 and the second
forces G_t=0. The exact joint constant field therefore gives
G=G0 in C. The equation g'+3g/t=0 gives t^3g=c in C*, so exact
integration in F gives
\[
g=\frac c{t^3},\qquad
f=\frac ct+c_1t+c_0,\qquad c\in\mathbb C^*,\quad c_1,c_0\in\mathbb C.
\tag{16}
\]
Solving (9) for ell_s and then integrating in s gives
\[
\boxed{
\ell=-\frac{s^3}{4t^4}+\frac{cs}{t^3}
       +\frac{(c_0-G_0)s}{2t^2}+\ell_0,
\qquad \ell_0\in F.
}
\tag{17}
\]
These integrations subtract explicit primitives and then use the
appropriate zero-derivative field. They impose no rationality
assumption on ell0 or the still undetermined coefficients.

There is one further useful gate in this exceptional branch.
Substitute the full h from (8) and (16),(17) into the genuine Q.
Its r-fourth coefficient is
\[
q_4=-\frac{a}{2t}
       \left\{a(t\ell_0''+2\ell_0')-2\right\}.
\tag{18}
\]
It follows that t ell0''+2ell0' is nonzero and
\[
\boxed{a=\frac{2}{t\ell_0''+2\ell_0'}\in F^*.}
\tag{19}
\]
The r-cubic and lower equations have not been eliminated here.
In particular (16)--(19) are not an exclusion of E=0.

## 5. Evidence and precise boundary

The complete369 source was freshly read in3670f9; the direct365/367
inputs and complete368 were reread in3ff2cb, following their prior
complete source reviews. The initial generic Q computation2d6d39
completed on its same live session32196 in96ca40. It produced the
two highest coefficients and the exact third-level identity.
A separate formal-jet calculation b4e586 reconstructed all terms
of Q relevant to (11), verified both residuals identically zero,
and also verified the unreduced second identity in (11).
Fresh b2fdf3 used the complete h of (8) in the exceptional branch,
verified (18), and independently checked (10) with G=G0.

Further unsaved scalar exploration4befdd completed on the same
session91324 in f5177e; c27c22 completed on the same session81892
in aac93c. Those exploratory coefficients are not claimed as a
completed exclusion in this note. No saved checker was executed,
imported, compiled or rerun. The coefficient identities supplement
the written exact-field reductions and do not replace them.

Both alternatives of (14) remain research cases. The general
nonlinear sector, equal/reversed degree patterns, arbitrary-chart
entry, and the unrestricted cancellation conjecture remain unsolved.
No novelty, external expert review, or proof-assistant certification
is claimed.
