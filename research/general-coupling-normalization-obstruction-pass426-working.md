# An exact filtered-frame obstruction to normalizing general coupling

Working bounded result: retain every actual hypothesis of264. Among
polynomial coordinate frames of original weighted degree at most
(1,2,2,2) that retain the full paraboloid initial kernel, normalization
to k*=s* is possible if and only if
\[
k_s\in\mathbb C^*,\qquad k_{ttt}=0.
\tag{1}
\]
Thus422 already covers exactly the couplings reachable by this
filtered class. This does not classify polynomial automorphisms whose
higher original weighted terms cancel in E-time. It does not prove
that any actual chart outside(1) exists or that such a chart cannot be
normalized by a different class of maps.

## 1. Actual input and the bounded class

Retain the entire supplied actual chart of
[264](principal-one-affine-paraboloid-chart-pass264-working.md):
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\quad A=\ker E,
\qquad \deg_E(X,Y,Z,W)=(1,2,2,2),\\
a_0=EX\ne0,\qquad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the FULL initial kernel},\\
N=[u^4]\partial_Z|_A\ne0,\qquad
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,
\quad Nv=1,\quad Na_0=Nt=Ns=0,\\
K=\operatorname{Frac}A=L(v)=\mathbb C(y,z,w),\qquad
O=L[v]=L[y,z,w],\qquad J_{t,s,v}(X)=-a_0^4.
\end{gathered}
\tag{2}
\]
The exact coefficient partials commute and have joint constants C.
All six intercept and linear coefficients lie in A localized at a0.
The literal expansions are
\[
Y=y+\sigma X+tX^2,\quad
Z=z+(2t\sigma+k)X+t^2X^2,\quad
W=w+\theta X+sX^2,\qquad k\in L.
\tag{3}
\]
No rationality of L is imposed. If m=k_s is nonzero,264 also gives
O=L[y,sigma,theta]. We will not use that latter assertion when m=0.

The bounded class consists of actual polynomial coordinate frames
(X*,Y*,Z*,W*) whose ORIGINAL polynomial weights satisfy
\[
\operatorname{wt}(X^*)\le1,\qquad
\operatorname{wt}(Y^*),\operatorname{wt}(Z^*),
\operatorname{wt}(W^*)\le2,
\quad \operatorname{wt}(X,Y,Z,W)=(1,2,2,2),
\tag{4}
\]
and whose full E-initial kernel in the new labelled slots is again
X*^2 Z*-Y*^2, with exact profile(1,2,2,2). Condition(4) is stronger
than this time-degree statement. Every coefficient of an actual map
in this class is complex, not an arbitrary element of L.

We use the retained omitted-partial bound of264/158, spelled out in
[384, Section1](principal-paraboloid-actual-filtered-symmetry-obstruction-pass384-working.md):
\[
[u^4]\partial_W|_A=0,\qquad
\deg_u\partial_W(A)\le3.
\tag{5}
\]
It follows from the full initial relation omitting W and does not
require k=s. The old Z-partial has exact shift four.

## 2. Complete shape, inverse and full initial kernel

The shape argument of384 Section5 uses only(2),(4), not k=s.
Here it is reproduced for general coupling. Necessarily
\[
\begin{aligned}
X^*&=\alpha X+x_0,\\
Y^*&=\mu Y+dX^2+\ell_YX+c_Y,\\
Z^*&=\frac{\mu^2}{\alpha^2}Z
       +\frac{2\mu d}{\alpha^2}Y
       +\frac{d^2}{\alpha^2}X^2+\ell_ZX+c_Z,\\
W^*&=qW+bY+cZ+eX^2+\ell_WX+c_W,
\end{aligned}
\qquad \alpha,\mu,q\in\mathbb C^*.
\tag{6}
\]
All other displayed parameters are arbitrary complex constants,
including zero. The letters d,e in(6) are map constants, not time
degrees or derivatives of potentials.

Indeed X* must have the first shape. Before using the new relation,
write the weighted quadratic part of Y* as mu Y+v0 Z+w0 W+dX^2.
Its normalized time leader is
(mu t+v0 t^2+w0 s+d)/alpha^2. The corresponding normalized
leader of Z* is a complex linear combination of 1,t,t^2,s divided
by alpha^2. The new relation requires the latter to be the square
of the former. Independence of t,s first forces w0=0 by the s^2
coefficient, then v0=0 by the t^4 coefficient. If mu=0, t* is
complex constant and the full initial kernel has an extra relation,
contrary to(4). Comparing the other coefficients gives the Z* row
of(6). The actual coordinate property makes the coefficient matrix
of Y,Z,W invertible, so q is nonzero.

Conversely every map(6) is an actual filtered polynomial
automorphism. Its inverse is the following sequential polynomial
substitution, dividing only by nonzero complex constants:
\[
\begin{aligned}
X&=(X^*-x_0)/\alpha,\\
Y&=(Y^*-dX^2-\ell_YX-c_Y)/\mu,\\
Z&=\frac{\alpha^2}{\mu^2}
 \left(Z^*-\frac{2\mu d}{\alpha^2}Y
              -\frac{d^2}{\alpha^2}X^2-\ell_ZX-c_Z\right),\\
W&=(W^*-bY-cZ-eX^2-\ell_WX-c_W)/q.
\end{aligned}
\tag{7}
\]
Its inverse has the same weight bounds. The weighted leading map
is invertible and sends the new labelled initial relation to
mu^2(X^2 Z-Y^2). Thus it preserves the ENTIRE initial ideal.
The leaders below show that all four exact time degrees remain as
stated. In particular no extra leading relation is introduced.

## 3. Literal transport of arbitrary k

At fixed X*, direct expansion of(3),(6) gives
\[
\begin{gathered}
t^*=\frac{\mu t+d}{\alpha^2},\qquad
s^*=\frac{qs+bt+ct^2+e}{\alpha^2},\qquad a_0^*=\alpha a_0,\\
\sigma^*=\frac{\mu\sigma+\ell_Y}{\alpha}-2x_0t^*,\\
\theta^*=\frac{q\theta+(b+2ct)\sigma+ck+\ell_W}{\alpha}
                    -2x_0s^*,\\
y^*=\mu y+c_Y-\frac{x_0}{\alpha}(\mu\sigma+\ell_Y)
                      +\frac{x_0^2}{\alpha^2}(\mu t+d).
\end{gathered}
\tag{8}
\]
In particular the exact transformed coupling is
\[
\boxed{
k^*=\frac{\mu^2}{\alpha^3}k+\frac{\ell_Z}{\alpha}
 -\frac{2\ell_Y(\mu t+d)}{\alpha^3}
 +\frac{2x_0(\mu t+d)^2}{\alpha^4}.
}
\tag{9}
\]
It is the linear Z* coefficient minus twice t* times the linear
Y* coefficient. The last term has denominator alpha^4. The formula
does not involve n,ell or any irreducibility condition on a surface.
Every starred expression is first a pullback to L; derivatives in
starred parameters use the following exact operators:
\[
\partial_{s^*}=\frac{\alpha^2}{q}\partial_s,\qquad
\partial_{t^*}=\frac{\alpha^2}{\mu}\mathcal D_p,
\qquad \mathcal D_p=\partial_t-p(t)\partial_s,
\quad p(t)=\frac{b+2ct}{q}.
\tag{10}
\]
These are not derivatives at fixed old s. The parameter change is
an invertible complex polynomial change, so C(t*,s*)=C(t,s).

Equations(9),(10) give exact differential invariants:
\[
\boxed{m^*:=(k^*)_{s^*}=\frac{\mu^2}{\alpha q}m,
\qquad m=k_s.}
\tag{11}
\]
Thus m=0, m in C*, and m not in C are separately invariant throughout
this filtered class. For arbitrary k the complete third derivative is
\[
(k^*)_{t^*t^*t^*}=\frac{\alpha^3}{\mu}\mathcal D_p^3 k,
\tag{12}
\]
where, since p''=0,
\[
\mathcal D_p^3k=k_{ttt}-3p k_{tts}+3p^2k_{tss}-p^3k_{sss}
                         -3p'k_{ts}+3pp'k_{ss}.
\tag{13}
\]
The complex quadratic added in(9) contributes zero. Formula(13)
records the derivative terms that cannot be dropped for general m.
When m is complex constant all mixed terms vanish, and therefore
\[
\boxed{m\in\mathbb C\quad\Longrightarrow\quad
(k^*)_{t^*t^*t^*}=\frac{\alpha^3}{\mu}k_{ttt}.}
\tag{14}
\]
No equality F=C(t), for F=ker partial_s, has been used.

## 4. Selected partial, both returns and full calibration

The inverse Z* column in(7) gives the literal original-ring identity
\[
\partial_{Z^*}=\frac{\alpha^2}{\mu^2}\partial_Z
              -\frac{c\alpha^2}{q\mu^2}\partial_W,
\qquad N^*=\frac{\alpha^2}{\mu^2}N.
\tag{15}
\]
The second equality follows from(5); no coefficient-dependent
combination is substituted for an original coordinate partial.
The exact constant field remains L. Choose
\[
v^*=\frac{\mu^2}{\alpha^2}v,
\qquad N^*v^*=1,
\qquad L[v^*]=O.
\tag{16}
\]
For m nonzero, the map on(y,sigma,theta) in(8) is invertible affine
over L and preserves their whole O-return. This alone would not
justify a strong return over C. For that use the actual quotient:
\[
\mathcal B_{a_0^*}=A_{a_0^*}[X^*],\qquad
X^*=a_0^*u+x_A^*,\quad x_A^*\in A.
\tag{17}
\]
Evaluation at X*=0 in the actual polynomial frame proves
\[
K=\mathbb C(y^*,z^*,w^*),\qquad
L[y^*,z^*,w^*]=O,
\tag{18}
\]
by exactly264's localized quotient argument. The evaluated denominator
a0* is a polynomial in the three intercepts, being the evaluation of
an original polynomial in the starred frame. This also proves(18)
when m=0, without asserting a three-function return that divides m.

At fixed X*, the bad-coordinate row determinant of(6) is
mu^3 q/alpha^2. The coefficient-parameter determinant from(t,s,v)
to(t*,s*,v*) equals mu^3 q/alpha^6. Consequently
\[
J^*_{t^*,s^*,v^*}(X^*)
 =\alpha^4 J_{t,s,v}((X^*-x_0)/\alpha)
 =-(\alpha a_0)^4=-(a_0^*)^4.
\tag{19}
\]
The original global slice and kernel are unchanged. Thus every
actual hypothesis needed for a new264 chart survives. The genuine
potentials and their full scalar conditions are those derived from
this actual new chart, not independently assigned formal functions.

## 5. Necessary and sufficient normalization criterion

Suppose a frame in the bounded class has k*=s*. Then m*=1, so(11)
forces m=alpha q/mu^2 in C*. Applying(14), the third t* derivative
of k*=s* is zero, hence k_ttt=0. Equivalently, equating(9) with(8)'s
formula for s* directly makes k a complex nonzero multiple of s plus
a complex quadratic in t. This proves necessity in(1).

Conversely suppose(1). Exact joint constants give
\[
k=ms+\gamma t^2/2+bt+d,
\qquad m\in\mathbb C^*,\quad\gamma,b,d\in\mathbb C.
\tag{20}
\]
For clarity, k_tt is killed by both coefficient partials. Subtracting
gamma t^2/2, then a complex linear term in t and a complex constant,
proves(20) without presuming a rational coefficient field.
The actual map of
[363, Sections2--3](principal-paraboloid-first-potential-affine-in-s-recognition-pass363-working.md)
is
\[
X_1=X,\quad Y_1=Y,\quad Z_1=Z,\qquad
W_1=mW+\gamma Z/2+bY+dX^2.
\tag{21}
\]
It is a member of(6), with inverse division only by m. It gives
t1=t,s1=k,k1=s1 and preserves all gates by Section4. This proves
sufficiency, with no assumption on n or ell. The arbitrary-n
potential transport is provided completely in363; nothing from its
earlier n_ss=0 application is needed for(21) itself.

Maps(6) and their inverses preserve the original weighted filtration.
Their compositions do as well. Therefore a finite sequence of such
paraboloid-preserving filtered reframes cannot evade necessity(1).
The working recognition consequence422 is thus maximal with respect
to normalization to k=s by this explicitly bounded class, not maximal
among all possible recognition arguments or all polynomial maps.

## 6. The excluded boundary is substantive

Original weighted degree and E-time degree must not be conflated.
For example(3) gives the literal polynomial identity
\[
Y^2-X^2Z=y^2+2y\sigma X+(\sigma^2+2ty-z)X^2-kX^3.
\tag{22}
\]
Its original weighted degree is four, although its time degree is at
most three, and at most two when k=0. This identity is a cancellation
mechanism, not a claim that the displayed polynomial is a coordinate
or that every formal value of k has an actual realization.

Accordingly, an actual chart with k_s nonconstant, or with constant
k_s and k_ttt nonzero, cannot be normalized to k=s by(4). A successful
normalization in such a case would need a map outside this class,
or a different route through a different supplied chart. The present
result neither rules out those possibilities nor makes an original
coordinate from the formal change s1=k. It also gives no global
cancellation theorem or arbitrary-frame entry argument.

## 7. Verification record

The current sources264,422,348,363 and384 were completely read through
EOF before this proof; the writing guide was also reread. The shape
argument from384 is explicitly extended from k=s to arbitrary k,
with its exact scope preserved. A fresh unsaved symbolic calculation
c39707 reconstructs all literal linear/quadratic coefficients in(8),
the arbitrary-k formula(9), the full derivative ledger(11)--(13), and
the fourth-power calibration factor(19); every residual is zero.
Separate fresh unsaved4b9fa5 checks both full inverse compositions
and the entire leading-relation transport, leaving every optional
map constant free to vanish. The written polynomial inverse and
initial-ideal arguments are supplied above.

No saved checker was executed, imported, compiled or rerun. No earlier
source or canonical index was edited. No independent human-expert
review, proof-assistant certification, historical novelty or public
submission is claimed. Independent source review remains separate
from this author verification.
