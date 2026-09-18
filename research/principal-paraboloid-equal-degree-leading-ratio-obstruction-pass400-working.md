# Only equal positive degrees with a non-affine leading ratio remain

Working synthesis in the supplied actual264 chart, with k=s and
n_ss nonzero. The constant-theta boundary is excluded by396--399.
Together with395 this leaves equal positive intrinsic degrees.
The actual transports of384 give a further necessary condition:
the leading theta/sigma ratio cannot belong to C+C*t.

These are necessary conditions in a restricted chart. They neither
exclude all equal-degree cases nor show that an arbitrary cancellation
candidate enters this chart. The unrestricted conjecture remains open
within this investigation.

## 1. Complete retained input and conclusion

Retain every actual hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md), not
merely its formal coefficient equations. In particular,
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A_0[u],\qquad E=\partial_u,
\quad a_0=EX\ne0,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\qquad
I_{\rm initial}=(X^2Z-Y^2)\text{ is the full initial kernel},\\
0\ne N=[u^4]\partial_Z|_{A_0},\qquad
L=\operatorname{Frac}\ker_{A_0}N,\quad [L:\mathbb C(t,s)]<\infty,\\
Nv=1,\qquad O=L[v]=L[y,\sigma,\theta]=L[y,z,w],\\
\operatorname{Frac}A_0=L(v)=\mathbb C(y,z,w).
\end{gathered}
\tag{1}
\]
The selected partial is the literal actual Z-partial. The parameters
t,s are algebraically independent, with their commuting exact
partials on L. Retain the actual global slice, every potential
identity, and all evaluated unit and scalar conditions. With k=s,
the literal rows and first two potentials are
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
Assume e=n_ss is nonzero. Degrees mean degree on the intrinsic
polynomial line over L. The zero polynomial has degree minus infinity.

The new necessary conclusion is
\[
\boxed{
1\le d:=\deg_v\theta=\deg_v\sigma\le6,\qquad
\deg_v y\le d,\qquad
\mu:=\frac{\operatorname{lc}_v\theta}
              {\operatorname{lc}_v\sigma}\notin\mathbb C+\mathbb C t.
}
\tag{3}
\]
The leading ratio is in L*. Because the two degrees agree, replacing
v by an affine parameter over L multiplies both leading coefficients
by the same nonzero factor. Thus mu is independent of that choice.
No element of L is asserted to be an original polynomial coordinate.

## 2. Exhaustion of the constant-theta boundary

The separately reviewed synthesis
[395](principal-paraboloid-nonlinear-strict-order-exclusion-pass395-working.md)
proves that nonconstant theta has the same positive degree as sigma,
at most six, and that y has no greater degree. If theta is constant,
the separate argument386 instead gives
\[
O=L[\sigma],\qquad y=\lambda\sigma+r,\qquad \lambda,r\in L.
\tag{4}
\]
The zero-slope proof
[396](principal-paraboloid-constant-theta-zero-slope-exclusion-pass396-working.md)
excludes lambda=0 by four coefficients of the full actual determinant.
It does not assume n_ts=0 or import the strict-degree rank condition.

For lambda nonzero, the necessary classification
[397](principal-paraboloid-constant-theta-nonzero-slope-coefficient-family-pass397-working.md)
proves
\[
\lambda=\frac{s-s_0}{2(t-\tau_0)^2},\qquad
n=-\frac{(s-s_0)^2}{4(t-\tau_0)^2}
  +\frac{\eta(s-s_0)}{t-\tau_0}+\gamma t+c_0,
\quad \tau_0,s_0,\eta,\gamma,c_0\in\mathbb C.
\tag{5}
\]
It proves eta=0 separately and transfers only the autonomous
coefficient-field lemma of387, not its strict-degree contradiction.
The actual normalization
[398](principal-paraboloid-constant-theta-coefficient-family-actual-normalization-pass398-working.md)
then supplies a complex polynomial automorphism reducing (5) to
\[
\lambda=\frac{s}{2t^2},\qquad
n=-\frac{s^2}{4t^2}+\frac{\eta s}{t},\qquad \eta\in\mathbb C.
\tag{6}
\]
That normalization retains every actual hypothesis, both returns,
the literal selected partial, and the nonzero scalar.

The complete scalar exclusion
[399](principal-paraboloid-constant-theta-nonzero-slope-scalar-exclusion-pass399-working.md)
rules out (6), with eta=0 retained. Its two coefficient integrations
leave a complex residue c1. If c1=0, the calibrated determinant is
divisible by its intrinsic parameter. If c1 is nonzero, its remaining
coefficient gives 3*c1*q=0, where q=s/t is nonzero. Both alternatives
contradict the actual nonzero scalar.

The slope split lambda=0 or lambda nonzero is exhaustive. Therefore
theta cannot belong to L. Applying395 proves the first two degree
statements in (3). This composition does not normalize general
coupling k, and does not assert the existence of any surviving case.

## 3. A permitted actual cancellation of an affine leading ratio

Suppose, for contradiction, that mu=alpha+beta*t for complex constants
alpha,beta. Put b=-alpha and c=-beta/2. Compose the two actual
transports of
[384, Sections2--4](principal-paraboloid-actual-filtered-symmetry-obstruction-pass384-working.md),
first its b map and then its c map. In the original coordinates the
composition is
\[
\begin{aligned}
X^*&=X+c/2,& Y^*&=Y-bX/2,\\
Z^*&=Z,& W^*&=W+bY+cZ.
\end{aligned}
\tag{7}
\]
Its explicit polynomial inverse is
\[
\begin{aligned}
X&=X^*-c/2,\\
Y&=Y^*+(b/2)(X^*-c/2),\\
Z&=Z^*,\\
W&=W^*-bY^*-(b^2/2)(X^*-c/2)-cZ^*.
\end{aligned}
\tag{8}
\]
Both Jacobians are one. Directly composing the coefficient transports
in384 gives, expressed in the old coefficient field,
\[
\begin{gathered}
t^*=t,\qquad s^*=s+bt+ct^2,\qquad k^*=s^*,\\
\sigma^*=\sigma-b/2-ct,\\
\theta^*=\theta+(b+2ct)\sigma-bct-c^2t^2,\\
n^*=n-b^2/4-c(s+bt)/2-c^2t^2/4,
\qquad (n^*)_{s^*s^*}=n_{ss}\ne0.
\end{gathered}
\tag{9}
\]
The n* formula is a pullback expression. Its new s* derivative is
the old s derivative, since t*=t; this licenses the final equality.

For completeness, the needed actual gates are not inferred from a
formal coefficient-field shear. The maps (7),(8) are defined over C.
Their weighted leading map fixes X,Y,Z and sends W to W+bY+cZ,
so it preserves the entire initial kernel (X^2Z-Y^2). The new W
leader is a0^2(s+bt+ct^2), nonzero by independence of t,s. The exact
time profile is unchanged. The inverse (8) gives
\[
\partial_{Z^*}=\partial_Z-c\partial_W.
\tag{10}
\]
The actual omitted-partial bound used in384 is
deg_u partial_W(A0)<=3. Therefore [u^4]partial_Z*|A0=N, not a new
coefficient-dependent derivation. In particular L,O,v and a0 remain
the same, and C(t*,s*)=C(t,s).

The full scalar and both returns are retained by384. In particular
the strong complex-field return after X translation comes from the
actual264 quotient argument in the new frame; it is not inferred
from an invertible affine map over L. Thus the new frame satisfies
all hypotheses used in Section2, including n*_{s*s*} nonzero.

Subtracting b/2+ct does not affect the positive intrinsic degree of
sigma, so deg sigma*=d. Equation (9) has theta* leading coefficient
\[
\operatorname{lc}_v(\sigma)\,[\mu+b+2ct]=0.
\tag{11}
\]
Consequently deg theta*<d, including the possibility that theta*
is constant or zero. If it is nonconstant,395 excludes the strict
degree order. If it is constant, Section2 excludes it. This is a
contradiction in every case and proves the final assertion in (3).

The proof permits only complex b,c. It cannot cancel an arbitrary
ratio in L, and it does not classify general polynomial changes of
frame. The bounded-frame obstruction in384 is not being used to
rule out transformations outside its stated scope.

## 4. Verification boundary and remaining work

Root freshly read the complete384,395,396 sources in4b25ab,aa7c65,
and b96108. The complete397 and398 reads are b0786f and5eee1c;
the complete399 read is6e86e3 in the preceding check-in. Fresh
899b36 matched the held384 and397--399 hashes. Their separate
earlier AI reviews and exact reconstructions are retained in the
research ledger. This note requires its own separate source review
before canonical acceptance.

The argument above is a composition of scoped written proofs, not
a fresh recursive formalization of all historical dependencies.
The hypotheses do not show that n_ss vanishes, that an invariant
coordinate exists, or that A0 is C^[3]. Equal-degree cases with a
ratio outside C+C*t, general coupling k, other initial ideals and
arbitrary-chart entry remain unresolved. The professor has not
confirmed the working complex-threefold interpretation of the
original conjecture.

No saved checker was executed, imported, compiled or rerun. No
held earlier proof was edited. No unrestricted cancellation,
novelty, human-expert review or proof-assistant certification is
claimed.
