# A moving first slope excludes constant sigma

Working exclusion: in the full actual principal chart264, assume
k=s and n=B(t)s+f(t), with B,f in the exact coefficient curve field
and B' nonzero. Then sigma cannot belong to the intrinsic constant
field L. The proof includes both values of the theta coefficient
in the centered third relation.

One case is contradicted by the fourth-potential level. In the other,
the complete scalar Jacobian factors by a monic quadratic in the
actual variable X. Neither argument makes a field-valued shift of
an original coordinate. This is not recognition of the entire moving-B
family or a claim that an arbitrary frame admits these potentials.

## 1. Full actual inputs and exact coefficient derivatives

Retain the complete actual chart of
[264](principal-one-affine-paraboloid-chart-pass264-working.md) and
the fourth-potential theorem of
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md).
In particular
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,
\qquad \deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the full weighted initial kernel},\qquad a_0=EX\ne0,\\
0\ne N=[u^4]\partial_Z|_A,\quad
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,\\
Nv=1,\quad K=\operatorname{Frac}A=L(v)=\mathbb C(y,z,w),\\
O=L[v]=L[y,z,w]=L[y,\sigma,\theta],\qquad
J_{t,s,v}(X)=-a_0^4\in L^*.
\end{gathered}
\tag{1}
\]
The chosen derivation is the leading part of the literal Z-partial;
it kills a0,t,s. The coefficient partials extend uniquely to L,
commute, and initially fix v. All original intrinsic functions belong
to O. In particular the actual variable X is transcendental over K.

For this bounded result assume
\[
k=s,\qquad n=Bs+f,\qquad
B,f\in\mathbb F:=\ker_L\partial_s,
\qquad b:=B'\ne0.
\tag{2}
\]
The field F is finite over C(t), and its exact t-derivative has
constant field C. Primes on B and f mean that derivative. No assertion
F=C(t), or that these functions are polynomials in t, is made. Thus
n_s=B, n_ts=b, and n_ss=0. All later coefficient derivatives are
the retained exact derivatives, not derivatives of a moving root.

The literal first two potentials are
\[
\begin{aligned}
z&=2ty+\sigma^2+\theta+n,\\
w&=\ell-2\sigma y-n_t\sigma-B\theta,\\
Y&=y+\sigma X+tX^2,\\
Z&=z+(2t\sigma+s)X+t^2X^2,\\
W&=w+\theta X+sX^2 .
\end{aligned}
\tag{3}
\]
The theta coefficient of w is -B; it cannot be discarded even when
y and sigma are constant in the intrinsic parameter.

## 2. The centered third level and the two needed fourth gradients

Use independent formal variables U,P,V. Here264's quadratic F is
F(P,V)=n_tP+BV. Its uncentered third polynomial is exactly
\[
\begin{aligned}
\mathcal H(U,P,V)={}&U^2+(n_t-2BP)U+B\ell-Bn_tP
 +\frac{n_{tt}}2P^2-\ell_tP\\
&+(bP-B^2-\ell_s)V,\qquad
\mathcal H(y,\sigma,\theta)=h\in L.
\end{aligned}
\tag{4}
\]
This follows directly from264's full expression, including H2(n).
In particular the n_ts term bPV has not been suppressed.

Set
\[
\begin{gathered}
x=y+p_0,\qquad p_0=n_t/2-B\sigma,\qquad
A_2=n_{tt}/2-B^2,\qquad C=\ell_s+B^2,\\
\bar h=h-B\ell+n_t^2/4.
\end{gathered}
\tag{5}
\]
Completing the square in(4) gives
\[
x^2+A_2\sigma^2-\ell_t\sigma+(b\sigma-C)\theta=\bar h.
\tag{6}
\]
This centering will only be used when sigma belongs to L, so that
p0 belongs to L too. It is never an original coordinate change.

The fourth polynomial Q from296 satisfies Q(y,sigma,theta)=q in L.
Only two of its formal partials are needed. Since m=1, gamma=2P,
and F_V=B,296 gives
\[
Q_U=\mathcal H_P-2P\mathcal H_V+B\mathcal H_U,
\qquad Q_V=\mathcal H_s-h_s.
\tag{7}
\]
Substitution of the complete polynomial(4) yields
\[
\boxed{\begin{aligned}
Q_U&=-2bP^2+(n_{tt}+2\ell_s)P+bV-\ell_t,\\
Q_V&=bU+\frac{b'}2P^2-(\ell_{ts}+Bb)P
       -\ell_{ss}V+B\ell_s-h_s.
\end{aligned}}
\tag{8}
\]
For the second identity, (n_t)_s=b and (n_tt)_s=b'. These are
coefficient derivatives of the formal polynomial before evaluation.
The level derivative h_s remains in the formula. No closed-form
choice of the other coefficients of Q is required.

## 3. Nonzero theta coefficient: a fourth-level contradiction

Suppose now that sigma belongs to L, and put
\[
D=b\sigma-C\in L.
\tag{9}
\]
First assume D is nonzero. The third level gives
\[
\theta=a_2x^2+d_0,\qquad
a_2=-1/D\in L^*,\qquad
d_0=(\bar h-A_2\sigma^2+\ell_t\sigma)/D\in L.
\tag{10}
\]
Because y=x-p0 and sigma is constant, the whole return gives
O=L[x,theta]=L[x]. Thus x is affine nonconstant in v, and Nx is
an element of L*. In particular theta has exact intrinsic degree
two. This is an exact polynomial-ring consequence, not just a
fraction-field equality.

Use x as the polynomial parameter of O. The coefficient field is
fixed, so differentiation of the fourth level in this parameter is
\[
0=Q_U(x-p_0,\sigma,a_2x^2+d_0)
  +2a_2x\,Q_V(x-p_0,\sigma,a_2x^2+d_0).
\tag{11}
\]
There is no Q_P term because sigma is fixed. Define constants in L
\[
\begin{aligned}
u_0&=-2b\sigma^2+(n_{tt}+2\ell_s)\sigma-\ell_t,\\
v_0&=-bp_0+\frac{b'}2\sigma^2
       -(\ell_{ts}+Bb)\sigma+B\ell_s-h_s.
\end{aligned}
\tag{12}
\]
By(8), the full polynomial on the right of(11) is
\[
-2\ell_{ss}a_2^2x^3+3ba_2x^2
 +2a_2(v_0-\ell_{ss}d_0)x+(bd_0+u_0).
\tag{13}
\]
Its quadratic coefficient 3ba2 is nonzero in characteristic zero,
contradicting its vanishing. Equivalently the cubic coefficient first
forces ell_ss=0, after which the same quadratic contradiction remains.
No division by ell_ss, b', sigma, or x was used.

## 4. Zero theta coefficient: the full scalar cannot be constant

It remains to treat D=0, without dividing by it. Equation(6) says
x^2 belongs to L. Since x belongs to L[v], it follows that x belongs
to L. Consequently y belongs to L. The whole return is now
\[
O=L[\theta]=L[v],\qquad \tau:=N\theta\in L^*.
\tag{14}
\]
In particular theta is not constant. Use the exact separating
variables (t,s,theta) for K. On L the new coefficient derivatives
are the original extensions of partial_t and partial_s; they are
now extended to fix theta. The triangular parameter-change matrix
has determinant tau, even when the old coefficient derivatives of
theta are nonzero. Thus the full actual scalar becomes
\[
\widetilde J(X)
 =\det\frac{\partial(Y,Z,W)}{\partial(t,s,\theta)}
 =-a_0^4/\tau\in L^*.
\tag{15}
\]
It is independent of both X and theta.

Because y and sigma belong to L, write the full literal map as
\[
\begin{aligned}
Y&=y+\sigma X+tX^2,\\
Z&=\theta+Z_0(X),\qquad
Z_0=2ty+\sigma^2+n+(2t\sigma+s)X+t^2X^2,\\
W&=(X-B)\theta+W_0(X),\qquad
W_0=\ell-2\sigma y-n_t\sigma+sX^2,
\end{aligned}
\tag{16}
\]
where Z0,W0 belong to L[X]. For a polynomial row computation only,
put I=W-(X-B)Z=W0-(X-B)Z0 in L[X]. No assertion I belongs to the
original ring or is an original coordinate is made.

Since B_s=0 and B_t=b, differentiation at fixed X gives
\[
dW-(X-B)dZ=dI-bZ\,dt.
\tag{17}
\]
The first row has no dtheta term; the second has dtheta coefficient
one; the new third row has no dtheta term. Expanding this determinant
therefore gives the exact all-X identity
\[
\boxed{\widetilde J=Y_s I_t-Y_t I_s-bZY_s.}
\tag{18}
\]
All derivatives here fix the newly chosen theta. The terms involving
I have no theta dependence. By(16), the theta coefficient of(18) is
\[
-bY_s=-b(y_s+\sigma_sX).
\tag{19}
\]
The scalar(15) has no such coefficient. Because b is nonzero and X
is independent over L, we obtain y_s=sigma_s=0. Equation(18) then
reduces to
\[
\widetilde J=-(X^2+\sigma_tX+y_t)I_s.
\tag{20}
\]
Both factors on the right belong to L[X], and the first is monic
of degree two. If I_s is zero the determinant is zero; otherwise
the product has degree at least two. Both possibilities contradict
the nonzero constant(15). This excludes D=0.

## 5. Exact conclusion and verification boundary

The two cases prove the scoped necessary condition
\[
\boxed{\text{Under the full actual chart(1),(2),}\quad
B'\ne0\quad\Longrightarrow\quad\sigma\notin L.}
\tag{21}
\]
The proof keeps the original scalar, literal map, and whole ring
return. The strong intercept field return remains a hypothesis of
the supplied chart but is not needed for these particular exclusions.
No rationality of L or F is required, and neither the centering x nor
the row polynomial I is promoted to an ambient coordinate.

The nonzero-D case gives a short direct fourth-level obstruction in
one quadratic-projection situation. It does not assert a new general
recognition theorem for all degree-two projections. The zero-D case
uses the full determinant, not merely its value at X=0. Neither
argument removes the genuinely varying-sigma branch. When B'=0,
the decisive coefficients in(13),(19) vanish; that boundary is not
included in this exclusion.

The complete saved264 and296 sources were freshly read before this
note. Fresh unsaved algebra reconstructed(8),(13) from the raw third
polynomial and reconstructed(18)--(20) from the full literal map,
retaining all coefficient jets. Every stated residual was zero.
These finite checks supplement the polynomial-degree arguments, not
the full actual entry or an ambient realization theorem. No saved
checker was executed, imported, compiled, or rerun; no earlier source,
canonical index, or ledger was edited. No unrestricted cancellation,
historical novelty, external review, or proof-assistant certification
is claimed.
