# Actual k=s symmetries and a filtered-frame degree obstruction

Working transport lemma: two explicit complex polynomial automorphisms
preserve the supplied actual264 chart with k=s, including its full
initial kernel, literal leading derivation, exact field returns and
calibration. Their first and second coefficient potentials are
transported explicitly.

A separate bounded obstruction classifies the shape of every
original weighted-degree-filtered coordinate frame retaining the
same full paraboloid initial kernel. Such a frame cannot turn
deg(theta)<=deg(sigma), with sigma nonconstant on the intrinsic line,
into a theta-dominant pair. This is not a classification of arbitrary
polynomial automorphisms having low E-time degree after cancellations.

## 1. Actual entry and the omitted-partial bound

Retain the complete actual entry of
[264](principal-one-affine-paraboloid-chart-pass264-working.md), with
the additional coefficient identity k=s. Thus
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\qquad
E=\partial_u,\qquad A=\ker E,\qquad a_0=EX\ne0,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\qquad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2),\\
N=[u^4]\partial_Z|_A\ne0,\qquad
L=\operatorname{Frac}\ker_A N,\qquad
[L:\mathbb C(t,s)]<\infty,\\
K=L(v)=\mathbb C(y,z,w),\qquad Nv=1,\qquad
O=L[y,\sigma,\theta]=L[y,z,w]=L[v].
\end{gathered}
\tag{1}
\]
The exact partials on L commute and extend fixing v. Both t,s and
a0 are N-invariant. At fixed actual X the literal map and the two
coefficient potentials are
\[
\begin{gathered}
Y=y+\sigma X+tX^2,\quad
Z=z+(2t\sigma+s)X+t^2X^2,\quad
W=w+\theta X+sX^2,\\
z=2ty+\sigma^2+\theta+n,\qquad
w+2\sigma y+n_t\sigma+n_s\theta=\ell,\qquad n,\ell\in L,\\
\det\frac{\partial(Y,Z,W)}{\partial(t,s,v)}=-a_0^4.
\end{gathered}
\tag{2}
\]
All further actual potential and scalar conditions remain in force.
No realization is claimed for arbitrary expressions satisfying only(2).

The complete positive-weight bound
[158, Section6](arbitrary-positive-weight-initial-bound-pass158-working.md)
shows that an omitted pivot has shift at most
sum(d_i)-d_j-2. Here the sum is7, dW=2, and the full initial
relation omits W. Consequently
\[
\deg_u\partial_W(A)\le3,\qquad
[u^4]\partial_W|_A=0.
\tag{3}
\]
This is a horizontal bound on the actual original partial, not merely
on a coefficient-field derivation. For Z the shift is exactly4 by264.
These two facts will identify the leading derivation after a W shear.

All formulas below with a star are pullbacks to the old coefficient
field unless a new-variable argument is displayed. Thus a formula
n*=n-cs/2-c^2t^2/4 means that its right side is expressed in the
old t,s and then rewritten in t*,s*. No derivative is taken while
silently holding the wrong s variable fixed.

## 2. A Y correction and a W shear

Let b be any complex constant. Define the actual map
\[
X^*=X,\qquad Y^*=Y-\frac b2X,\qquad
Z^*=Z,\qquad W^*=W+bY.
\tag{4}
\]
Its polynomial inverse is
\[
X=X^*,\quad Y=Y^*+\frac b2X^*,\quad Z=Z^*,\quad
W=W^*-bY^*-\frac{b^2}{2}X^*.
\tag{5}
\]
Both compositions are the identity. The new literal coefficients are
\[
\begin{gathered}
t^*=t,\quad s^*=s+bt,\quad
\sigma^*=\sigma-\frac b2,\quad \theta^*=\theta+b\sigma,\\
y^*=y,\quad z^*=z,\quad w^*=w+by,\quad
k^*=s^*,\quad a_0^*=a_0.
\end{gathered}
\tag{6}
\]
The first potential is therefore
\[
n^*=n-\frac{b^2}{4},\qquad
\partial_{t^*}=\partial_t-b\partial_s,\quad
\partial_{s^*}=\partial_s.
\tag{7}
\]
In particular n*_{t*}=nt-bns and n*_{s*}=ns. Substitution into
w*+2sigma*y*+n*_{t*}sigma*+n*_{s*}theta* gives the second potential
\[
\ell^*=\ell-\frac b2n_t+\frac{b^2}{2}n_s.
\tag{8}
\]
For example explicitly n*(t*,s*)=n(t*,s*-bt*)-b^2/4; the same
pullback convention applies to(8).

The inverse(5) does not mix Z* into any other old coordinate.
Thus the new literal partial is exactly partial_Z, and N*=N.

## 3. An X translation and a Z shear into W

Let c be any complex constant. Define
\[
X^*=X+\frac c2,\qquad Y^*=Y,\qquad
Z^*=Z,\qquad W^*=W+cZ.
\tag{9}
\]
The polynomial inverse is X=X*-c/2, Y=Y*, Z=Z*, W=W*-cZ*.
Expanding the actual rows at fixed X* gives
\[
\begin{gathered}
t^*=t,\qquad s^*=s+ct^2,\qquad
\sigma^*=\sigma-ct,\qquad
\theta^*=\theta+2ct\sigma-c^2t^2,\\
y^*=y-\frac c2\sigma+\frac{c^2t}{4},\qquad
z^*=z-ct\sigma-\frac c2s+\frac{c^2t^2}{4},\\
w^*=w+cz-\frac c2\theta-c^2t\sigma-\frac{c^2s}{4}
                                  +\frac{c^3t^2}{4},\\
k^*=s^*,\qquad a_0^*=a_0.
\end{gathered}
\tag{10}
\]
The first potential and the exact coefficient partials are
\[
\begin{gathered}
n^*=n-\frac c2s-\frac{c^2t^2}{4},\\
\partial_{t^*}=\partial_t-2ct\partial_s,\qquad
\partial_{s^*}=\partial_s,\\
n^*_{t^*}=n_t-2ctn_s+\frac{c^2t}{2},\qquad
n^*_{s^*}=n_s-\frac c2.
\end{gathered}
\tag{11}
\]
Equivalently n*(t*,s*)=n(t*,s*-c(t*)^2)-cs*/2+c^2(t*)^2/4.
The second potential is
\[
\boxed{
\ell^*=\ell+cn-ctn_t+c^2t^2n_s-\frac{c^2s}{4}
                                      -\frac{c^3t^2}{4}.
}
\tag{12}
\]
Indeed inserting(10),(11) into its defining expression cancels
every occurrence of y,sigma,theta. This identity retains arbitrary
n(t,s), including nonzero nss.

The literal new coordinate partial is not partial_Z:
\[
\partial_{Z^*}=\partial_Z-c\partial_W.
\tag{13}
\]
By(3) its coefficient of u^4 on A is nevertheless precisely N.
Thus its shift is still exactly4, N*=N, and its exact kernel field
is the same L. No commutation with a coefficient-dependent linear
combination is being inferred.

## 4. All actual gates retained by the two maps

Both maps have original Jacobian one and polynomial inverses.
Their weighted leading maps, for weights(1,2,2,2), fix X,Y,Z
and send W respectively to W+bY or W+cZ. Each induces a graded
polynomial automorphism fixing X^2Z-Y^2. Therefore the entire new
initial kernel is still that principal ideal, not just an ideal
containing its generator. The new W leader is respectively
a0^2(s+bt) or a0^2(s+ct^2), nonzero because t,s are algebraically
independent. All four exact E-time degrees remain(1,2,2,2).

The field C(t,s) equals C(t*,s*) in either case; the finite extension
L and selected N are unchanged. The maps on (y,sigma,theta) in(6)
and(10) are invertible affine maps over L, so their whole polynomial
line O remains the same. The strong field return
K=C(y*,z*,w*) also holds: the new frame has every actual hypothesis
of264, so its actual X*=0 quotient argument applies. In the translated
case this is not being deduced from a merely L-affine intercept map.

Each coefficient-base change (t,s)->(t*,s*) has determinant one.
The original row operation and X translation also preserve volume.
Consequently the new horizontal scalar is the old scalar evaluated
at X=X* in(4), or at X=X*-c/2 in(9), hence again -a0^4. The old v
still has Nv=1. These statements retain all higher coefficient
conditions automatically because they concern an actual coordinate
map and its exact determinant, not only the first two potentials.

For both transports,
\[
n^*_{s^*s^*}=n_{ss},\qquad
n^*_{t^*s^*}=
\begin{cases}
n_{ts}-b n_{ss},&\text{for(4)},\\
n_{ts}-2ct n_{ss},&\text{for(9)}.
\end{cases}
\tag{14}
\]
Thus neither map is licensed to remove an arbitrary coefficient-field
slope by replacing b or c with a nonconstant function.

## 5. Shape of every bounded weighted-filtered frame

Here impose an explicit additional restriction: a new actual coordinate
frame has original weighted degree at most1 for X* and at most2 for
Y*,Z*,W*, using the original polynomial weights(1,2,2,2). Assume its
exact E-time profile and full initial kernel are again those in(1).
This restriction is stronger than having those E-time degrees.

A degree-bound frame must have X*=alpha X+x0, alpha in C*, and
each other coordinate is a complex linear combination of Y,Z,W,X^2,
X,1. The 3-by-3 matrix of coefficients of Y,Z,W is invertible, since
the whole map is an actual coordinate frame. The new initial relation
forces it to have the following more special shape:
\[
\begin{aligned}
X^*&=\alpha X+x_0,\\
Y^*&=\mu Y+dX^2+\ell_YX+c_Y,\\
Z^*&=\frac{\mu^2}{\alpha^2}Z+\frac{2\mu d}{\alpha^2}Y
       +\frac{d^2}{\alpha^2}X^2+\ell_ZX+c_Z,\\
W^*&=qW+bY+cZ+eX^2+\ell_WX+c_W,
\end{aligned}
\quad
\alpha,\mu,q\in\mathbb C^*,
\tag{15}
\]
with every other displayed coefficient complex.

To prove this, write the old-Y, old-Z, old-W and X^2 coefficients
of Y* as mu,v0,w0,d. Its normalized quadratic leader is
(mu*t+v0*t^2+w0*s+d)/alpha^2. The normalized leader of Z* is a polynomial
linear in t,t^2,s,1 divided by alpha^2. Squaring the first expression
must equal the second, because the full new initial relation is
X*^2Z*-Y*^2. The s^2 coefficient first forces w0=0, and the t^4
coefficient then forces v0=0. Also mu is nonzero: otherwise t* would
be complex constant and the full initial kernel would acquire the
extra relation Y*-constant*X*^2. Comparing the remaining coefficients
gives the Z* row of(15). Matrix invertibility then gives q nonzero.

In particular
\[
t^*=\frac{\mu t+d}{\alpha^2},\qquad
s^*=\frac{qs+bt+ct^2+e}{\alpha^2},
\tag{16}
\]
so C(t*,s*)=C(t,s). The inverse's Z* column gives
\[
\partial_{Z^*}
 =\frac{\alpha^2}{\mu^2}\partial_Z
  -\frac{c\alpha^2}{q\mu^2}\partial_W,\qquad
N^*=\frac{\alpha^2}{\mu^2}N.
\tag{17}
\]
Again(3) is the reason for the second equality. Thus the same exact
kernel field L and intrinsic polynomial-line degree can be used.

Expansion at X* shows, for some eta1,eta2 in L,
\[
\sigma^*=\frac\mu\alpha\sigma+\eta_1,\qquad
\theta^*=\frac q\alpha\theta
                  +\frac{b+2ct}{\alpha}\sigma+\eta_2.
\tag{18}
\]
The X^2 terms and the translation x0 contribute only to eta1,eta2.
Thus these formulas do not assume that an intrinsic parameter or a
coefficient-field shear is an ambient coordinate.

## 6. The intrinsic degree obstruction and k=s subgroup

Suppose sigma is nonconstant in O=L[v], and measure degree in any
affine line parameter v over L. Formula(18) gives
\[
\deg_v\sigma^*=\deg_v\sigma,\qquad
\deg_v\theta^*\le\max\{\deg_v\theta,\deg_v\sigma\}.
\tag{19}
\]
If theta has larger degree than sigma, its nonzero leading term in
(18) cannot cancel. If its degree is at most that of sigma, the new
theta also has degree at most that of the new sigma. Therefore
theta-dominance is preserved in both directions throughout the
bounded class(15). Equal or reversed degrees cannot be moved into
the previously studied theta-dominant sector by these frames.

For equal positive degrees, put lambda=lc(theta)/lc(sigma) in L*.
The new leading ratio before a possible cancellation is
(q/mu)lambda+(b+2ct)/mu. Cancellation can occur only if lambda lies
in the complex affine span C+Ct. Conversely, in that situation a
composition of(4),(9) can cancel it, using constant b,c. This produces
a smaller theta degree, not theta-dominance.

One can also identify exactly when(15) preserves k=s. The linear
Z* coefficient minus twice t* times the linear Y* coefficient is
\[
k^*=\frac{\mu^2s}{\alpha^3}+\frac{\ell_Z}{\alpha}
 -\frac{2\ell_Y(\mu t+d)}{\alpha^3}
 +\frac{2x_0(\mu t+d)^2}{\alpha^4}.
\tag{20}
\]
Comparing with(16), using independence of t,s, gives k*=s* precisely
when
\[
\begin{gathered}
q=\frac{\mu^2}{\alpha},\qquad c=\frac{2x_0\mu^2}{\alpha^2},\\
b=-\frac{2\mu\ell_Y}{\alpha}+\frac{4x_0\mu d}{\alpha^2},\qquad
e=\alpha\ell_Z-\frac{2d\ell_Y}{\alpha}
                           +\frac{2x_0d^2}{\alpha^2}.
\end{gathered}
\tag{21}
\]
This subgroup contains both explicit transports above. Since the
degree obstruction was proved on the larger class(15), it applies
in particular to the k=s subgroup.

## 7. Scope and verification record

The result supplies exact valid actual transports and a bounded
negative normalization result. It does not classify automorphisms
whose large original weighted terms cancel in E-time, and it does
not prohibit a different degree-lowering transformation, different
initial-kernel chart, or different selected partial. In particular
(19) must not be used to conclude that the remaining equal/reversed
sectors are intrinsically unreachable by all ambient automorphisms.

The complete264 source was reread through EOF in10b2a4 and the
complete158 source inb35f7d/2ad3ab. The latter provides the actual
omitted-pivot shift needed in(3),(13),(17).

Fresh unsaved32c192 independently expanded all three literal rows of
the translated frame and both coefficient potentials. Separate
unsaved e8e3b2 checked the other first/second potential transport,
both inverse orders of both actual maps, and the general formula(20)
and coefficient conditions(21). All residuals were zero. These
finite identities support, rather than replace, the written actual
return and filtered-degree arguments.

No saved checker was executed, imported, compiled or rerun. No held
earlier proof or canonical index was edited. No unrestricted
cancellation, novelty, human-expert verification or proof-assistant
certification is claimed.
