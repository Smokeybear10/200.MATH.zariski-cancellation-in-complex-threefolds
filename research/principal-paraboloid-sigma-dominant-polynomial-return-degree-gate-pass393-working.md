# Polynomial return and a transverse cubic-degree obstruction

Working conditional result: in the actual sigma-dominant quadratic-cubic
chart, the polynomial coefficient normal form described below forces
polynomial-plane return after adjoining the exact one-variable field.
The original slice and actual selected derivation then make both speeds
units of that field. A degree-three sigma in the transverse t direction
is impossible by the characteristic-zero embedding-line degree theorem.

The result does not assume that the one-variable coefficient field is
rational. It does not recognize the original invariant ring or exclude
the remaining transverse degree at most two. The polynomial normal form
is an explicit input, not inferred just from the intrinsic degree pair.

## 1. Complete actual input and the polynomial normal form

Retain all actual264 hypotheses and the strict sigma-dominant entry385/387.
Use the actual complex translation Y*=Y+gamma/2, proved in388--390,
to remove the complex term gamma*t from n. Thus
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A_0[u],\quad E_0=\partial_u,
\quad a_0=E_0X\ne0,\\
\deg_{E_0}(X,Y,Z,W)=(1,2,2,2),\quad
I_{\rm initial}=(X^2Z-Y^2)\text{ is the full initial kernel},\\
N=[u^4]\partial_Z|_{A_0}\in\operatorname{LND}(A_0)\setminus\{0\},
\quad Na_0=Nt=Ns=0,\\
L=\operatorname{Frac}\ker_{A_0}N,\quad [L:\mathbb C(t,s)]<\infty,
\quad K=\operatorname{Frac}A_0=L(r)=\mathbb C(y,z,w),\\
O=L[r]=L[y,\sigma,\theta]=L[y,z,w],\quad Nr=\rho\in L^*,\\
k=s,\quad n=f\in S:=\ker_L\partial_t,\quad
\nu=f_s\ne0,\quad e=f_{ss}\ne0.
\end{gathered}
\tag{1}
\]
The exact coefficient partials commute and have joint constants C.
In particular partial_s preserves S, and t is transcendental over S.
Every coefficient in L and every intercept in K is killed by E0.
The selected partial is the literal actual Z-partial.

Assume the following explicit polynomial normal form, obtained in the
nonzero highest-Q gate investigation but retained here as an input:
\[
\begin{gathered}
F\in S^*,\quad B,D\in S,\qquad
p:=\ell_t=Ft+B,\quad \ell=\tfrac12Ft^2+Bt+D,\\
a\in S^*,\quad b\in S[t],\ \deg_t b\le1,\quad
c\in S[t],\ \deg_t c\le2,\quad C=\ell_s+\nu^2,\\
y=r-\frac{p}{2\nu},\quad \theta=ar^2+br+c,\\
\sigma=\frac{ea^2}{4\nu}r^3+\frac{eab}{2\nu}r^2
 +\left(\frac1{2\nu}+\frac{e(b^2+2ac)}{4\nu}
                    -\frac{Ca}{2\nu}\right)r
 -\frac{p}{2\nu^2}+\frac{ebc-Cb}{2\nu}.
\end{gathered}
\tag{2}
\]
These expressions are polynomials everywhere in t,r, including r=0.
For total degree in t,r over S, y has degree at most one, theta at
most two and sigma at most three. No relation on the leading t
coefficients is silently added.

The complete literal rows and the actual scalar are
\[
\begin{aligned}
z&=2ty+\sigma^2+\theta+f,&
w&=\ell-2\sigma y-\nu\theta,\\
Y&=y+\sigma X+tX^2,\\
Z&=z+(2t\sigma+s)X+t^2X^2,\\
W&=w+\theta X+sX^2,\\
J(X)&:=\det\frac{\partial(Y,Z,W)}{\partial(t,s,r)}
      =-a_0^4/\rho\in L^*.
\end{aligned}
\tag{3}
\]
The coefficient partials in this determinant fix r and the actual X.
All rows in(3) belong to S[X,t,r].

## 2. Strong return first removes only the t extension

Equations(2),(3) place y,z,w in S[t,r]. Since S is contained in L,
strong return in(1) gives the two inclusions
\[
K=\mathbb C(y,z,w)\subseteq S(t,r)\subseteq L(r)=K.
\tag{4}
\]
Thus K=S(t,r). Intersect with L inside L(r). The parameter r is
transcendental over L, so L intersect S(t,r)=S(t): a rational
function in the independent r with coefficients in S(t) which is
constant in r must lie in S(t). Consequently
\[
L=S(t),\qquad K=S(t,r).
\tag{5}
\]
This does not identify S with C(s), and field equality alone does
not imply any of the polynomial equalities proved next.

## 3. The original slice makes a0 an S-unit

Inside the original fraction field put
\[
\mathscr R=S[\mathcal B],\qquad \mathscr T=S[X,t,r].
\tag{6}
\]
The notation means adjoining a field to the actual subring inside
that fraction field. It is not an unsupported tensor-product domain
assertion. Equations(2),(3) give R contained in T. The variables
X,t,r are independent over S: t,r are so by(5), while X is
transcendental over K because E0X=a0 nonzero and B=A0[u].

Since a0 is in B and Na0=0, polynomial independence and(5) give
\[
a_0\in S[X,t,r]\cap S(t)=S[t].
\tag{7}
\]
The actual derivation extends to T as a0(t)*partial_X, since it
kills S,t,r and sends X to a0. The original slice u lies in B,
hence in T, and therefore
\[
1=E_0u=a_0(t)\partial_Xu.
\tag{8}
\]
Both factors belong to the polynomial ring T. Its units are exactly
S*, so
\[
a_0\in S^*.
\tag{9}
\]
This is not an assertion that a0 is a unit of the original A0.

## 4. Actual derivatives give the reverse polynomial inclusion

The actual ring R is E0-stable because B is and E0 kills S.
The literal rows give
\[
t=\frac{E_0^2Y}{2a_0^2},\qquad
\sigma=\frac{E_0Y}{a_0}-2tX,\qquad
y=Y-\sigma X-tX^2,\qquad
r=y+\frac{Ft+B}{2\nu}.
\tag{10}
\]
Each right side is in R, in the indicated order, using only units
already established in S. Hence t,r are in R, and
\[
S[\mathcal B]=S[X,t,r].
\tag{11}
\]
Adjoining S contained in K to B=A0[u] also gives R=S[A0][u].
The kernel of E0 there is S[A0]; by(9),(11), its kernel is S[t,r].
Thus
\[
S[A_0]=S[t,r].
\tag{12}
\]
No generator after adjoining S is declared to be an original
coordinate, and no slice of N in A0 was assumed.

N preserves A0 and kills S. It therefore preserves(12), whence
rho=Nr lies in S[t,r] intersect L=S[t]. All partials in(3) preserve
S[X,t,r], so J(X) lies there as well. Its actual calibration becomes
the polynomial identity
\[
\rho J(X)=-a_0^4\in S^*.
\tag{13}
\]
Both factors on the left are units, proving
\[
\rho,J(X)\in S^*,\qquad N=\rho\partial_r\text{ on }S[A_0].
\tag{14}
\]
In particular J_t=0 as well as its known X,r independence. Its
s derivative is not asserted zero.

Finally specialize X=0 in(11). Since the equality is one of actual
polynomial subrings and both contain X, this gives
\[
S[y,z,w]=S[t,r]=S[t,y].
\tag{15}
\]
The last equality uses the affine inverse r=y+(Ft+B)/(2nu).
This specialization is not an ambient complex coordinate change.

## 5. A degree-three sigma is incompatible with plane return

Set k0=S(y). Since y,t are independent over S, localizing(15) gives
\[
k_0[z,w]=k_0[t].
\tag{16}
\]
All following degrees mean polynomial t degree at fixed y over k0.
The letter y is a nonzero unit in k0, not a chosen numerical value.
By(2), deg sigma<=3 and deg theta<=2. Put
\[
L_2=\ell-\nu\theta\in k_0[t],\quad\deg L_2\le2,
\qquad w=L_2-2y\sigma.
\tag{17}
\]
Suppose deg sigma=3. Then deg w=3 and deg z=6. The invertible
triangular change of the generated k0-algebra
\[
z_1=z-\frac{w^2}{4y^2}
 =\frac{\sigma L_2}{y}-\frac{L_2^2}{4y^2}
                  +\theta+2ty+f
\tag{18}
\]
has the following exhaustive possibilities.

If deg L2=2, the unique top product sigma*L2/y has degree five,
so degrees(w,z1)=(3,5). If deg L2=1, the same product has degree
four, so degrees(w,z1)=(3,4). In either case its coefficient is
nonzero by the definitions of the two degrees.

If L2 is constant in t, including L2=0, a further triangular change
gives
\[
z_2=z_1+\frac{L_2}{2y^2}w
     =\theta+2ty+f+\frac{L_2^2}{4y^2}.
\tag{19}
\]
Here theta=(ell-L2)/nu has exact t degree two with leading
coefficient F/(2nu) nonzero. Thus degrees(w,z2)=(3,2).

Each changed pair still generates k0[t]. In characteristic zero,
two nonconstant polynomials generating a polynomial-line ring have
degrees dividing one another. The three pairs(3,5),(3,4),(3,2)
violate that necessary condition. For a primary proof see Garcia
Barroso and Ploski, *Polynomial automorphisms of the affine plane
and singularities of algebraic curves*, Theorem6.7, p.47, and the
embedding definition on p.35 of the
[author-hosted paper](https://ergarcia.webs.ull.es/2018-GB-Ploski-RACC.pdf).
Its algebraically closed base is obtained by extending k0; polynomial
generation and the exact degrees persist under that field extension.

The contradiction proves the additional necessary gate
\[
\boxed{\deg_t\sigma\le2\quad\text{after }r=y+(Ft+B)/(2\nu).}
\tag{20}
\]
No classification of all lower-degree embeddings is used.

## 6. Scope and verification boundary

This argument depends on the full actual ring, original slice and
selected N, as well as the explicit polynomial hypothesis(2).
Formal polynomial parametrizations with only a constant determinant
need not satisfy the reverse inclusion(10). The proof supplies
neither arbitrary-chart entry nor recognition of A0.

The mechanism in379 was fully reread in16acc3, but the current
reverse inclusion recovers t from E0^2Y, not s from E0^2W; r is
recovered from its current literal definition. All intersections,
derivation extensions and kernel equalities are proved above.
The external degree theorem was freshly retrieved from its primary
author-hosted text in turn4602view0/turn4602view1. No screenshot or
proof-assistant verification is claimed. Independent source review
is pending until the held-source audit is recorded in the ledger.
Fresh unsaved ccc6ca checked both exact triangular reduction identities
in(18),(19), with zero residuals; the ring proof is not a finite test.

No saved checker was executed, imported, compiled or rerun. No
original generator, rational coefficient field, unrestricted
cancellation, novelty or human-expert certification is claimed.
