# An initial-growth obstruction for the affine intrinsic line

Working conditional theorem: retain the FULL actual chart264,
nonzero coupling and the intrinsic affine-line data
\[
P=\sigma,\qquad y=\lambda P+r,\qquad
\theta=\mu P+e,\qquad w=\omega P^2+bP+c.
\tag{1}
\]
Then lambda and omega cannot both be noncomplex. Equivalently,
\[
\boxed{\lambda\in\mathbb C\quad\hbox{or}\quad
       \omega\in\mathbb C.}
\tag{2}
\]
The conclusion concerns actual chart data, not arbitrary
coefficient polynomials. It follows from an actual polynomial
three-ring over C(X), its actual W-partial, and the growth of
the invariant ring of a nonzero locally nilpotent derivation.
No coefficient-field coordinate is promoted to an ambient one.

The theorem does not on its own recognize either alternative in
(2), or arrange the affine intrinsic line in an arbitrary chart.
Its use with earlier variable-coupling exclusions is a separate
composition obligation. In particular this note makes no claim
to unrestricted cancellation or historical novelty.

## 1. The actual three-ring and the coefficient embedding

Retain every actual hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md).
The original setup, selected derivation and parameter satisfy
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,
\qquad X=a_0u+x_0,\quad a_0\ne0,\quad x_0\in A,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\qquad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the ENTIRE original initial kernel},\\
0\ne N=[u^4]\partial_Z|_A\in\operatorname{LND}(A),\qquad
Na_0=Nt=Ns=0,\\
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,
\quad O=L[P],\quad P=\sigma,\quad NP=\rho\in L^*,\\
\operatorname{Frac}A=L(P)=\mathbb C(y,z_{\rm int},w),\qquad
L[y,z_{\rm int},w]=L[P].
\end{gathered}
\tag{3}
\]
Here z_int is the literal original Z-intercept. Both returns,
the original slice and the selected partial remain required.
The coefficient partials are the exact commuting extensions
from C(t,s), extended to fix P. No rationality of L is presumed.

Assume (1), with every coefficient in L, and suppose for
contradiction that lambda and omega are both outside C.
The literal rows become
\[
\begin{aligned}
Y&=(X+\lambda)P+r+tX^2,\\
Z&=P^2+(2t\lambda+k_t+m\mu+2tX)P
       +2tr+me+n+kX+t^2X^2,\\
W&=\omega P^2+(b+\mu X)P+c+eX+sX^2,
\qquad m=k_s\ne0.
\end{aligned}
\tag{4}
\]
These are the original ambient coordinates. In particular no
nonconstant multiple of an ambient coordinate has replaced it.
The complete calibrated determinant is
\[
J=\det\frac{\partial(Y,Z,W)}{\partial(t,s,P)}
       =-a_0^4/\rho\in L^*.
\tag{5}
\]
It need not be constant in t or s.

Let k=C(X), F=L(X), and form the ACTUAL polynomial three-ring
\[
R=k[Y,Z,W]\subset F[P].
\tag{6}
\]
X is transcendental over L(P), since it is affine nonconstant
in the original independent slice u. The original ambient
polynomial-ring equality guarantees that Y,Z,W are independent
variables over k. The coefficient field F is finite separable
over k(t,s), and Frac(R)=F(P). The latter follows from the
literal-intercept field return and the original ambient field;
it does not assert R=F[P].

Extend N to A[u] by Nu=0 and put
\[
\Delta=a_0N-(NX)E.
\tag{7}
\]
This is a polynomial derivation of the original ring and kills
X. On its localization A[a_0^{-1}][X], at fixed X it is a_0N,
because Na_0=0 and N(X)=N(x_0). Hence it is locally nilpotent
there and on the original ring. It extends to a nonzero
k-linear locally nilpotent derivation on R. In F[P],
\[
\Delta=a_0\rho\,\partial_P,\qquad \Delta|_F=0.
\tag{8}
\]
In particular ker_R Delta=R intersect F. Its fraction field
has transcendence degree two over k: localization at a local
slice writes R as a polynomial line over its invariant ring.
Consequently ker_R Delta contains two algebraically independent
polynomials over k. This assertion requires neither finite
generation of the invariant ring nor a global slice for Delta.

## 2. The full intrinsic initial kernel

The exact P-degree profile of (4) is (1,2,2). Indeed X+lambda
is nonzero in F and omega is nonzero. Give the independent
source symbols Yhat,Zhat,What weights 1,2,2 and define
\[
\Phi:k[\widehat Y,\widehat Z,\widehat W]\longrightarrow F[T],
\quad (\widehat Y,\widehat Z,\widehat W)
\longmapsto((X+\lambda)T,T^2,\omega T^2).
\tag{9}
\]
This is the ENTIRE initial homomorphism of the actual three-ring,
distinct from the original four-coordinate initial homomorphism
in (3).

Since C is algebraically closed, a noncomplex lambda in L is
transcendental over C and also over C(X). For the second claim,
clearing a purported C(X)-polynomial relation gives a polynomial
in the independent X with coefficients in C[lambda], forcing
a relation over C. It follows that the first two images in (9)
are algebraically independent over k. For example, in each
T-degree, a relation would be a polynomial in X+lambda with
distinct powers over k. Thus the image has transcendence degree
at least two.

Choose any nonconstant Delta-invariant polynomial f in R. Its
actual P degree is zero by (8). Its highest positive-weight
source part f_M must therefore vanish under Phi. In particular
ker(Phi) is nonzero. The image has transcendence degree exactly
two, so this homogeneous prime has height one. The source is
a polynomial UFD, and therefore
\[
\ker\Phi=(H)
\tag{10}
\]
for a nonconstant irreducible weighted-homogeneous polynomial H.
Let its weight be d. Independence of the first two images means
that H involves What. Characteristic zero gives H_What nonzero;
also H cannot divide H_What, which has smaller weight.

## 3. The actual W-partial has degree shift at most two

Use the actual k-derivation D=partial/partial W on R, extended
to Frac(R)=F(P). With X fixed, Cramer's rule in (5) gives
\[
\begin{aligned}
D(t)&=(Y_sZ_P-Y_PZ_s)/J,\\
D(s)&=(Y_PZ_t-Y_tZ_P)/J,\\
D(P)&=(Y_tZ_s-Y_sZ_t)/J.
\end{aligned}
\tag{11}
\]
The coefficient derivatives keep P fixed. Equation (4) shows
that Y_t,Y_s have degree at most one, Z_t,Z_s at most two,
Y_P has degree zero and Z_P degree one. Since J is a unit of
the coefficient field, (11) gives
\[
\deg_P D(t),\deg_P D(s)\le2,\qquad \deg_P D(P)\le3.
\tag{12}
\]
These are upper bounds; a cofactor is allowed to vanish.
The exact partials on F over k(t,s) are uniquely determined
by separability. Thus D on F[P] is the combination of those
partials and partial_P with the coefficients (11). It preserves
F[P] and, for every nonzero g in F[P],
\[
\deg_P D(g)\le\deg_P g+2
\tag{13}
\]
when D(g) is nonzero. Vanishing causes no difficulty.
If f is Delta-invariant, then f belongs to F, and iteration
gives deg_P D^ell(f)<=2ell for every nonzero iterate.

## 4. Invariant multiplicity bounds the relation's weight

For a nonconstant invariant f as above, factor its highest
weighted part maximally as
\[
f_M=H^{\ell}G,\qquad \ell\ge1,\quad H\nmid G,
\quad M=d\ell+\operatorname{wt}(G).
\tag{14}
\]
The polynomial G is weighted homogeneous. Applying ell formal
What-derivatives and reducing modulo H gives
\[
\partial_{\widehat W}^{\ell}(H^{\ell}G)
       \equiv \ell! H_{\widehat W}^{\ell}G\pmod H,
\tag{15}
\]
which is nonzero in the domain defined by H. The actual D in
(11) is precisely differentiation in the independent variable W
of R. All lower source-weight parts of f remain strictly lower
after ell differentiations. Equations (9),(10),(15) therefore
give the EXACT intrinsic degree
\[
\deg_P D^{\ell}(f)=M-2\ell.
\tag{16}
\]
In particular this iterate is nonzero. Combining (13),(16)
gives M<=4ell, and therefore d<=4.

The equality d=4 is impossible. If it held, (14) forces
wt(G)=0 for EVERY nonconstant invariant f, so every such top
part is a scalar in k times a power of H. In the filtration
by source weight, each graded piece of the invariant ring
therefore has dimension at most one, and only weights divisible
by four can occur. Its subspace of weight at most n has dimension
at most 1+floor(n/4).

On the other hand, choose two algebraically independent invariants
f,g and let C0 be the larger of their positive source weights.
For every positive integer q, the monomials f^i g^j with
i+j<=q are independent over k and have weight at most C0*q.
Their number (q+1)(q+2)/2 eventually exceeds the preceding
linear bound. This contradiction proves
\[
\boxed{d\le3.}
\tag{17}
\]
This is a dimension count on finite-dimensional filtered
subspaces, not an assumption that the invariant ring is finitely
generated or that its associated graded ring equals k[H].

## 5. The only remaining relation contradicts varying lambda

A relation of weight one is a scalar multiple of Yhat and
cannot vanish under (9). Every weight-three monomial contains
Yhat, so a weight-three polynomial is divisible by Yhat. Such
a polynomial cannot be the irreducible H involving What.
Thus d=2 and
\[
H=\alpha(X)\widehat Y^2+\beta(X)\widehat Z
                           +\gamma(X)\widehat W,
\qquad \alpha,\beta,\gamma\in\mathbb C(X),\quad\gamma\ne0.
\tag{18}
\]
Its evaluated relation is
\[
\alpha(X)(X+\lambda)^2+\beta(X)+\gamma(X)\omega=0.
\tag{19}
\]
If alpha=0, this makes omega belong to C(X) intersect L=C,
contradicting the assumption. The intersection identity follows
from the transcendence of X over L. Thus alpha is nonzero.
After division, (19) reads
\[
(X+\lambda)^2=A(X)+B(X)\omega,
\qquad A,B\in\mathbb C(X).
\tag{20}
\]
Choose distinct complex numbers x1,x2 avoiding the finitely
many poles of A and B. This specializes a rational-function
identity in L(X), not an actual coordinate fiber or an invariant
denominator. Subtracting its two specializations puts lambda
in span_C{1,omega}. Substituting this back into either square
puts lambda^2 in the same span.

Write lambda=c0+c1*omega with complex c0,c1. Noncomplex lambda
forces c1 nonzero. Its square cannot belong to span_C{1,omega},
because omega is transcendental over the algebraically closed
field C and the coefficient of omega^2 is c1^2 nonzero.
This final contradiction proves (2).

## 6. Verification and retained boundary

The complete264 source and the retained325 affine-line reduction
were read through EOF. The explicit cofactor bounds and invariant
growth argument above are proved here rather than inferred from
a generic degree profile or a rational-function relation alone.
Separate outline checks and a complete independent saved-source
review remain distinct gates, to be recorded in the ledger.

The actual LND, actual polynomial three-ring and complete scalar
are essential. A formal family satisfying high potential equations
alone need not meet them. The necessary square-root families of489
therefore do not supply counterexamples to this theorem, nor does
the theorem retroactively invalidate their stated necessary
coefficient identities.

The original complete initial kernel and chart-entry assumptions
have not been removed. This note does not force affine sigma or
affine theta in arbitrary cancellation data. No saved checker was
executed, imported, compiled or rerun; no earlier source or
canonical record was edited in authoring this note.
