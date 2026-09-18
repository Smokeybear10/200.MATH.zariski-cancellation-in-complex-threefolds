# Four geometric exclusions in the theta-dominant intercept sector

Working result: retain365's complete actual chart with k=s,
n_ss nonzero, and 1<=deg sigma<deg theta. Four of its seven necessary
degree pairs are impossible:
(3,4), (3,5), (4,5), and (5,6).
The remaining necessary pairs are (1,2), (2,3), and (4,6).

The affine changes used here are over the exact coefficient field L.
They are not actual changes of X,Y,Z,W. The proof transfers the
quadric/cubic geometry of355 and356 only after verifying all its
whole-ring and gradient-minor hypotheses. In the sextic case, the
zero centered level is treated separately. No recognition theorem
or general normalization is claimed.

## 1. Actual input and exact affine recentering

Retain every actual hypothesis of the fully read
[365](principal-paraboloid-nonlinear-intercept-unequal-degree-gate-pass365-working.md):
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad
\deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(X^2Z-Y^2)\text{ is the full initial kernel},\quad
N=[u^4]\partial_Z|_A,\quad a_0=EX\ne0,\\
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,\quad
Nv=1,\quad O=L[v]=L[y,\sigma,\theta],\\
K=L(v)=\mathbb C(y,z,w),\qquad
\det\frac{\partial(Y,Z,W)}{\partial(t,s,v)}=-a_0^4\in L^*.
\end{gathered}
\tag{1}
\]
The literal full map and both lower potentials are those of264,
with k=s and e=n_ss nonzero. We assume
\[
a=\deg_v\sigma\ge1,\qquad h=\deg_v\theta>a.
\tag{2}
\]
The two letters a,h in this note are degrees, not the slice speed
or a potential level.

By365, there is tau in C such that, with T=t-tau,
\[
e=-\frac1{2T^2},\qquad
n=-\frac{s^2}{4T^2}+f_1s+f_0,\qquad
f_1,f_0\in\ker_L\partial_s .
\tag{3}
\]
Use its exact coefficient notation
\[
\begin{gathered}
\nu=n_s,\quad b=n_{ts},\quad
A=n_{tt}/2-\nu^2,\quad C=\ell_s+\nu^2,\quad J=\ell_t,\\
\bar h=h_0-\nu\ell+n_t^2/4,\quad
x_{\rm old}=U+n_t/2-\nu P,\quad
\zeta=x_{\rm old}+V/(2T),\\
\mathcal R=\zeta-TbP+TC,\qquad
\Omega=A+T^2b^2\ne0.
\end{gathered}
\tag{4}
\]
The formal third relation is
\[
H-h_0=\zeta^2+AP^2-JP-\bar h-\frac VT\mathcal R .
\tag{5}
\]
After evaluation,365 proves
\[
\deg\zeta=a,\quad
0\ne\mathcal R^{\rm ev},\quad
r:=\deg\mathcal R^{\rm ev}=2a-h<a,\quad
\max(\deg y,\deg\sigma,\deg\theta)\le6.
\tag{6}
\]
Its full fourth level is a polynomial of exact total degree three,
and the evaluated gradient-minor ideal of the two levels is O.

For a completely explicit further affine change, set
\[
\begin{gathered}
\Lambda=2T^2bC+J,\qquad D=T^2C^2-\bar h,\\
p=\mathcal R,\qquad
x=P+\frac{Tb}{\Omega}p-\frac{\Lambda}{2\Omega},\\
q=V-\frac{TA}{\Omega}p-\frac{T^2b\Lambda}{\Omega}+2T^2C,\\
\beta=-\frac1{T\Omega}\ne0,\qquad
d=\frac{\Lambda^2}{4\Omega^2}-\frac D\Omega .
\end{gathered}
\tag{7}
\]
The inverse is
\[
\begin{aligned}
P&=x-\frac{Tb}{\Omega}p+\frac{\Lambda}{2\Omega},\\
V&=q+\frac{TA}{\Omega}p+\frac{T^2b\Lambda}{\Omega}-2T^2C,\\
\zeta&=TbP-TC+p,\qquad
U=\zeta-\frac{V}{2T}-\frac{n_t}{2}+\nu P .
\end{aligned}
\tag{8}
\]
In particular this is an invertible affine L-change. Completing
the square in (5) gives exactly
\[
\frac{H-h_0}{\Omega}=x^2+\beta pq-d=:H_0.
\tag{9}
\]
It follows after evaluation that
\[
O=L[p,x,q],\qquad
(\deg p,\deg x,\deg q)=(r,a,h),\qquad
(2x,\beta q,\beta p)O=O.
\tag{10}
\]
The degree assertions use r<a<h; no leading cancellation is possible
in x or q in (7).

Let Phi be the same affine substitution in the complete fourth
level Q-q0 of365. An invertible affine substitution preserves its
exact total degree three. Formal gradients transform by invertible
matrices over L, so
\[
\Phi(p(v),x(v),q(v))=0,\qquad
\bigl((H_0)_i\Phi_j-(H_0)_j\Phi_i:i<j\bigr)O=O.
\tag{11}
\]
There is no coefficient differentiation in this formal change.
The new variables need not be polynomials in the original four-ring.

The pairs to exclude become
\[
\begin{array}{c|c}
(\deg\sigma,\deg\theta)&(\deg p,\deg x,\deg q)\\ \hline
(3,4)&(2,3,4)\\
(3,5)&(1,3,5)\\
(4,5)&(3,4,5)\\
(5,6)&(4,5,6).
\end{array}
\tag{12}
\]
Only (9)--(11) and these degrees are used in the next sections.

## 2. Zero centered level, with every parity case separated

Suppose d=0. The unit-gradient identity in (10) gives
gcd(p,q)=1: a common prime would also divide x by x^2=-beta*p*q.
Unique factorization in L[v] therefore gives
\[
p=\lambda R^2,\qquad x=\lambda RS,\qquad
q=-\lambda S^2/\beta,\qquad
\lambda\in L^*,\quad R,S\in L[v],\quad\gcd(R,S)=1.
\tag{13}
\]
No square root of a coefficient-field element is needed. This is
the exact argument of the fully read
[351](principal-paraboloid-variable-first-slope-quadric-fibers-pass351-working.md).
Whole return becomes L[R^2,RS,S^2]=L[v].

For (1,3,5) and (3,4,5), the odd degree of p contradicts (13).
Thus d is nonzero in both degree-five cases.

For (2,3,4), the degrees of R,S are one and two. Take R itself
as an affine parameter xi, and write
S=A1 xi^2+B1 xi+C1, with A1 nonzero. Coprimality makes C1 nonzero.
Then
\[
L[R^2,RS,S^2]
=L[\xi^2,\xi(A_1\xi^2+C_1)]
=L[\xi^2]\oplus\xi(A_1\xi^2+C_1)L[\xi^2].
\tag{14}
\]
For example RS=B1 xi^2+xi(A1 xi^2+C1), and S^2 has the same
odd generator with coefficient 2B1. Its odd module cannot contain
xi because A1 xi^2+C1 is nonconstant. This contradicts whole return.

For (4,5,6), the degrees of R,S are two and three. Whole return
first implies
\[
L[v]=L[R^2,RS,S^2]\subseteq L[R,S]\subseteq L[v],
\]
so L[R,S]=L[v]. This is impossible for a quadratic and a cubic.
Indeed translate the original parameter to make
R=a2 xi^2+c2, with a2 nonzero. Subtract the even part of S using
R and constants. The resulting generators are xi^2 and
xi(A3 xi^2+C3), with A3 nonzero. Their odd module again cannot
contain xi. This treats the cone d=0 without using the geometry
of a smooth quadric.

## 3. The projective geometric inputs when d is nonzero

Extend coefficients to an algebraic closure \(\overline L\) of L. Both the
whole-ring equality and the unit ideal (11) survive this extension.
The affine image is therefore a closed smooth copy of A1, not just
a birational parametrization. Its projective closure C0 lies on
the smooth quadric
\[
\mathcal S:\quad x^2+\beta pq-dz^2=0
\quad\subset\mathbb P^3_{\overline L},
\tag{15}
\]
in projective coordinates [z:p:x:q].

Homogenizing (1,p(v),x(v),q(v)) to its largest degree h gives a
base-point-free birational map P1 to C0. It is its normalization,
has hyperplane pullback O(h), and has just one point above infinity.
Consequently
\[
\deg C_0=h,\qquad
P_\infty=[0:0:0:1].
\tag{16}
\]
In the q-chart at infinity, the orders on the normalization are
\[
\operatorname{ord}(z/q)=h,\quad
\operatorname{ord}(p/q)=h-r,\quad
\operatorname{ord}(x/q)=h-a.
\tag{17}
\]
For h-a=1 this also proves smoothness of C0 at infinity: x/q has
a nonzero linear term in the normalization parameter and generates
its complete power-series ring. The completed curve local ring,
which embeds in that ring and contains the series in x/q, is equal
to it. Since the affine curve was already smooth, C0 is then P1.

The cubic Phi does not vanish identically on S, since otherwise
its affine restriction would be divisible by H0 and the minors
(11) would vanish. Its homogenization cuts an effective divisor
\(\mathcal D\) of class (3,3) on
\(\mathcal S\simeq\mathbb P^1\times\mathbb P^1\).
The two ruling classes have self-intersection zero and mutual
intersection one; the hyperplane class is (1,1).
The degree of D is six. The multiplicity of C0 in D is one,
because a higher multiplicity would kill the restricted cubic
differential along the affine curve, contrary to (11).

These are the geometric inputs used in the fully read
[355](principal-paraboloid-degree-three-sigma-ruling-exclusion-pass355-working.md)
and
[356](principal-paraboloid-degree-two-three-four-exclusion-pass356-working.md).
They depend only on (9)--(11), not on those notes' particular
coefficient formulas for n.
The Segre description and two rulings are checked in
[Vakil, Foundations, Section 5.1, PDF page154](https://virtualmath1.stanford.edu/~vakil/0708-216/216fall0708.pdf).
Degree under the normalization, additive intersections, and
Cartier-divisor restriction are the respective statements in
[Stacks, Section33.45](https://stacks.math.columbia.edu/tag/0BEL).

No residual component of D can meet C0 at an affine point.
At such a point, a local equation on the smooth surface has both
the curve factor and a vanishing residual factor. Its differential
on S is zero, which makes the two ambient gradients dependent.
This contradicts (11), including for repeated residual components.

## 4. The degree-four curve

For (r,a,h)=(2,3,4), Section2 ruled out d=0. Now h-a=1, so C0
is smooth rational. If its bidegree is (u,w), then u,w are positive,
u+w=4, and
\[
g(C_0)=(u-1)(w-1)=0.
\tag{18}
\]
Thus its class is (1,3) or (3,1). The genus formula follows from
the divisor exact sequence on P1 x P1, or adjunction with
canonical class (-2,-2); it is also stated in
[Chao Li, Intersection Theory, Example15](https://www.math.columbia.edu/~chaoli/docs/IntersectionTheory.html).
An integral curve of class (0,w) or (u,0) is a single ruling fiber,
so cannot have degree four.

The residual divisor D-C0 therefore has class (2,0) or (0,2).
It is the sum of two fibers of the same ruling, with repetition
allowed. Every support line R0 has intersection number C0.R0=3.
All those intersections would have to lie at infinity by Section3.
The two ruling lines through P_infinity have local equations
\[
x/q-\varepsilon\sqrt d\,z/q=0,\qquad \varepsilon=1,-1 .
\tag{19}
\]
Their pullbacks have order one by (17). Thus a support line missing
infinity has intersection zero, and a support line through infinity
has intersection one. Both contradict intersection number three.
This excludes the pair (deg sigma,deg theta)=(3,4).

## 5. Both degree-five curves

For (r,a,h)=(1,3,5) or (3,4,5), d is nonzero by Section2.
Since D has degree six and C0 has degree five, its residual divisor
is exactly one reduced ruling line R0. If this line is of class
(1,0), then C0 has class (2,3); the other possibility reverses
the classes. In either case
\[
C_0\mathbin{\cdot}R_0=3.
\tag{20}
\]
The unit minors again prohibit affine intersections. If R0 passes
through infinity, its local equation is one of (19). The two terms
there have orders h-a and h, respectively, so no cancellation is
possible. The local intersection length is h-a, which is two for
(1,3,5) and one for (3,4,5), both less than three.

This length calculation does not assume C0 is smooth at infinity.
Its normalization has one point there. For the local curve ring
A0 and its normalization DVR A1, A1/A0 has finite length.
Multiplication by the ruling equation in
0 -> A0 -> A1 -> A1/A0 -> 0 shows that the two quotient lengths
are equal, since its kernel and cokernel on A1/A0 have equal lengths.
The length in A1 is precisely the order in (17).
This is the same local argument as355, now with order two also
allowed. It excludes both degree pairs (3,5) and (4,5).

## 6. The degree-six curve with smooth infinity

For (r,a,h)=(4,5,6), Section2 already excludes d=0.
For d nonzero, h-a=1, so the projective curve C0 is smooth rational.
It has degree six, the entire degree of the cubic divisor D.
Positivity of the degree of every effective component and the
multiplicity-one conclusion give D=C0. Hence C0 has class (3,3).
But (18) gives
\[
g(C_0)=(3-1)(3-1)=4,
\tag{21}
\]
contrary to its isomorphism with P1. This excludes (5,6).
The smooth-quadric argument was not applied to the cone d=0;
that case was separately settled by the exact degree-(2,3) lift.

## 7. The precise remaining boundary

Combining these four exclusions with365 gives
\[
\boxed{
1\le\deg\sigma<\deg\theta,\ k=s,\ n_{ss}\ne0
\quad\Longrightarrow\quad
(\deg\sigma,\deg\theta)\in\{(1,2),(2,3),(4,6)\}.
}
\tag{22}
\]
These remain necessary patterns only. For the last pair, the
normalized degrees are (2,4,6), not (2,3,4). At zero level,
the square-root degrees in (13) would therefore be (1,3), not
(1,2). A proposed reuse of the quadratic-root odd-module argument
for this boundary is invalid and is not part of the proof.

Indeed the abstract quadric/cubic/unit-minor inputs cannot exclude
(2,4,6), even when d=0. Over any characteristic-zero field, set
\[
p=v^2-d,\qquad x=v+p^2,\qquad q=-1-2vp-p^3,\qquad \beta=1.
\tag{23}
\]
Then x^2+pq=d and v=x-p^2 proves whole return. The cubic
\(\Phi=q+1+2xp-p^3\) vanishes. For
M_xq=H_x Phi_q-H_q Phi_x and
M_pq=H_p Phi_q-H_q Phi_p, evaluation gives
\[
M_{xq}=2v,\qquad M_{pq}=-1-4vp,\qquad
M_{pq}+2pM_{xq}=-1.
\tag{24}
\]
All three degrees are (2,4,6) for every d, including zero.
This is the formal boundary family already present in351.
It is not asserted to be the literal fourth potential of the
current coefficient family, to have strong complex-field return,
or to arise from an actual globally sliced four-ring.

The remaining work must use additional literal coefficients, scalar
identities, or original-ring structure. No actual invariant or
coordinate has been constructed here. In particular an affine
change over L and a geometric ruling over its algebraic closure
are not promoted to a polynomial reframe over C.

The complete365,355,356 and351 sources were read before composing
this transfer. The primary geometric statements were freshly checked.
Fresh unsaved algebra verified (8),(9), its nonzero affine
determinant, and all identities in the formal boundary control.
The intersection, genus, and exact parity arguments are the written
proofs, not finite-test certificates. No saved checker was executed,
imported or compiled, and no retained source or index was edited.
No arbitrary-entry, unrestricted cancellation, novelty, human-expert
review, or proof-assistant certification claim is made.
