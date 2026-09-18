# Recognition of every supplied one-variable first potential

Working synthesis, subject to the retained proofs listed below: in the
full actual principal chart264, k=s and n_s=0 imply that the original
sliced kernel is C^[3]. The first potential n may initially belong to
a finite algebraic curve field; it need not be rational or polynomial
in t. There is no added restriction on the second potential ell.

The new direct argument here excludes nonconstant g=f''/2 when the
inverse second-potential slope is complex. The complementary variable
slope exclusion is345. Their combination forces a complex-quadratic
first potential whenever ell_s is nonzero. The case ell_s=0 is337.
This is not an argument that arbitrary charts admit k=s or n_s=0.

## 1. Actual inputs and the remaining two-variable coefficient form

Retain every actual hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md), including
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad A=\ker E,
\quad a_0=EX\ne0,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\quad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the full kernel},\\
N=[u^4]\partial_Z|_A\ne0,\quad L=\operatorname{Frac}\ker_A N,
\quad [L:\mathbb C(t,s)]<\infty,\\
Nv=1,\quad K=\operatorname{Frac}A=L(v)=\mathbb C(y,z,w),\\
L[y,z,w]=L[y,\sigma,\theta]=L[v],\quad
J_{t,s,v}(X)=-a_0^4\in L^*.
\end{gathered}
\tag{1}
\]
The coefficient partials are the exact commuting extensions to L.
Assume k=s and n_s=0, and write
\[
n=f\in\mathbb F:=\ker_L\partial_s,\quad
[\mathbb F:\mathbb C(t)]<\infty,\quad
\ker_{\mathbb F}\partial_t=\mathbb C,
\quad p=f'/2,\quad g=f''/2,\quad x=y+p.
\tag{2}
\]
The notation f(t) means membership in F, not a rationality assumption.

If ell_s=0, the retained full one-variable-pair result
[337](principal-paraboloid-two-one-variable-potentials-recognition-pass337-working.md)
recognizes A. Thus suppose ell_s nonzero. Section4 of
[344](principal-paraboloid-complex-quadratic-family-recognition-pass344-working.md)
proves the necessary identity ell_ss=0, without assuming constant g.
In the exact parameters r=ell, s=H(t,r), this gives
\[
H=c(t)r+d(t),\qquad c,d\in\mathbb F,
\quad c=H_r=1/\ell_s\ne0.
\tag{3}
\]
Here the r-constant field is the same F. No integration through a
presumed rational parameter is required: H_r belongs to F, and
H-H_r r also belongs to F.

If g=0, exact constants make f complex affine. The actual translations
of333 reduce to the retained normalized theorem330. Hence g is
nonzero in the remaining discussion.

## 2. Constant inverse slope and nonconstant g are incompatible

In this section suppose c'=0, so c belongs to C*, and assume for a
contradiction that g' is nonzero. The complete plane primitive of
[333](principal-paraboloid-one-variable-first-potential-plane-reduction-pass333-working.md)
becomes
\[
\Phi(U,P)=-\mathcal L_r U^2+2(1+cg)UP+d'U
 +(d''/2-g\mathcal L_r)P^2+\frac{cg'}3P^3-\mathcal L_tP.
\tag{4}
\]
All coefficients are in the exact L. Its total degree is exactly
three, with leading homogeneous form cg'P^3/3. The full plane return
and unit cofactor give
\[
L[x,\sigma]=L[v],\qquad
\Phi-q=\eta G+G^2R,\quad
q\in L,\quad\eta\in L^*,\quad R\in L[U,P],
\tag{5}
\]
where G is the full irreducible plane equation. The retained plane
facts give deg G=max(deg_v x,deg_v sigma) and a pure-power leading
homogeneous form.

Since G divides Phi-q, its degree is at most three. Degree two is
impossible: with R=0 the degree would be two, while with R nonzero
it would be at least four. Thus its degree is one or three.

### 2.1. The selected line

If deg G=1, then R has degree one and the squared top of G divides
the top P^3 of Phi. After multiplying G by a nonzero scalar in L,
it is G=P-beta for some beta in L. Hence sigma=beta and x is an
affine nonconstant parameter of L[v]. Differentiating(5) formally
in P and restricting to the line gives a nonzero constant in L.
But directly from(4),
\[
\Phi_P(U,\beta)
 =2(1+cg)U+(d''-2g\mathcal L_r)\beta
   +cg'\beta^2-\mathcal L_t.
\tag{6}
\]
The coefficient of U must vanish. Thus 1+cg=0, whose exact
t-derivative gives cg'=0, a contradiction. No coefficient derivative
of beta is introduced by this formal normal derivative.

### 2.2. The selected cubic

If deg G=3, then R=0 and Phi-q=eta G. The top of G is a nonzero
multiple of P^3. Together with the degree formula in(5), this forces
\[
\deg_v x=3,\qquad \deg_v\sigma<3.
\tag{7}
\]
For if sigma had degree three, the P^3 term would have v-degree nine,
whereas every remaining term of G has total degree at most two and
therefore v-degree at most six. If sigma were constant, the whole
return would give L[x]=L[v], contradicting deg_v x=3. The only
remaining sigma-degrees are one and two.

Degree two is excluded by the whole polynomial-ring equality, not by
birationality alone. Translate v over L to complete its square:
\[
\sigma=a z^2+b_0,\quad a\in L^*,\qquad
x=x_{\rm even}(z^2)+z(Az^2+B_0),\quad A\in L^*.
\tag{8}
\]
No square root is needed. Subtracting the even part gives
\[
L[x,\sigma]
=L[z^2,z(Az^2+B_0)]
=L[z^2]\oplus z(Az^2+B_0)L[z^2].
\tag{9}
\]
The last equality holds because the square of the odd generator is
even. This ring cannot contain z: that would require the nonconstant
polynomial Az^2+B0 to be a unit of L[z^2]. This contradicts(5).
The cases B0=0 and a zero of that polynomial at zero cause no exception.

If sigma has degree one, then x=F(sigma) for a degree-three polynomial
F in L[P]. The full equation is a scalar multiple of U-F(P).
Since Phi-q is a scalar multiple of that equation, its U-derivative
must be a nonzero element of L. Yet
\[
\Phi_U=-2\mathcal L_rU+2(1+cg)P+d'.
\tag{10}
\]
This forces Lcal_r=0 and 1+cg=0. Again cg'=0 contradicts the
standing assumptions. Every selected cubic case has been excluded.

We conclude that under(1)--(3),
\[
\boxed{c\in\mathbb C^*,\quad g\ne0\quad\Longrightarrow\quad g'=0.}
\tag{11}
\]
The proof is over the exact coefficient field and uses no promotion
of x, sigma, or its translated parameter to an ambient coordinate.

## 3. Composition with the variable-slope exclusion

The complementary source
[345](principal-one-variable-first-variable-second-slope-exclusion-pass345-working.md)
excludes c' nonzero under(1)--(3) with g nonzero. It uses the full
plane cofactor, exact coefficient compatibility, the nonzero actual
scalar, and a quadratic-degree contradiction to K=C(y,z,w).
It does not infer a contradiction merely from generic polynomial
generation or assume the finite field F rational.

Thus c is complex, and(11) makes g complex nonzero. Exact constants
give
\[
f=gt^2+f_1t+f_0,\qquad f_1,f_0\in\mathbb C.
\tag{12}
\]
The actual constant translations of333 remove f1,f0 while retaining
the complete chart. The full complex-quadratic theorem344 then
recognizes the original A. Combining this with the affine case and
the ell_s=0 theorem337 proves the scoped working implication
\[
\boxed{\text{Under the full actual chart(1),}\quad
k=s,\quad n_s=0\quad\Longrightarrow\quad A\cong\mathbb C^{[3]}.}
\tag{13}
\]
The proof also supplies the necessary coefficient restrictions
\[
\boxed{\ell_{ss}=0,\qquad \ell_s n_{ttt}=0.}
\tag{14}
\]
These are identities in the exact field. They are not assertions
that every formal family satisfying them is realized by an actual
globally sliced polynomial frame.

## 4. Scope and verification boundary

This expands337, which required both n_s and ell_s to vanish, and
the normalized first-potential part of344, which assumed n complex
quadratic. It retains their complete actual input and recognition
dependencies. In particular the general kernel-recognition assertions
in156/257 and the corrected normalized-family inputs have not been
recursively re-proved by this synthesis.

No argument here makes a general coupling potential k equal to s,
makes an arbitrary n independent of s, or puts arbitrary sliced actions
into the supplied principal1222 frame. Those remain genuine parts of
the unrestricted cancellation problem. The theorem is not a proof
of that problem, an expert review, a historical novelty claim, or a
proof-assistant certification. Source-review and finite-control results
belong in the research ledger, with their narrower verification scope.
