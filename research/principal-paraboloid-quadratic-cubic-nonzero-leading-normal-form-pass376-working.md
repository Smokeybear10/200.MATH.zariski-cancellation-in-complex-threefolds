# Exact coefficient-field normal form for the nonzero quadratic-cubic gate

Working necessary reduction: in the E nonzero alternative of372,
the leading intrinsic coefficient belongs to F, the square-presentation
term G is affine in s with nonzero slope H in F, and
E=d t^3 H^4 for a nonzero complex constant d. The next genuine
fourth-potential coefficient makes every coefficient of sigma a
polynomial in s over F. Exact strong field return then proves
L=F(s), without identifying F with C(t).

This is not exclusion, realization, or kernel recognition. None
of the coefficient-field variables is promoted to an original
polynomial coordinate. The E=0 exclusion374 is a separate result.

## 1. Complete retained chart and notation

Retain the complete actual hypotheses of the fully read
[372](principal-paraboloid-quadratic-cubic-leading-coefficient-gates-pass372-working.md)
and its direct365/369 inputs. In particular
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A_0[u],\qquad E_{\rm slice}=\partial_u,
\qquad \deg_{E_{\rm slice}}(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(X^2Z-Y^2)\text{ is the full initial kernel},
\qquad a_0=E_{\rm slice}X\ne0,\\
N=[u^4]\partial_Z|_{A_0},\qquad L=\operatorname{Frac}\ker_{A_0}N,
\qquad [L:\mathbb C(t,s)]<\infty,\\
O=L[r]=L[y,\sigma,\theta]=L[y,z,w],\qquad
Nr=\rho\in L^*,\qquad K=L(r)=\mathbb C(y,z,w).
\end{gathered}
\tag{1}
\]
Here r is the degree-one intrinsic remainder of372, and the degree
pair is (deg_r sigma,deg_r theta)=(2,3). Write
F=ker_L partial_s, a finite extension of C(t). The exact coefficient
partials commute and have joint constants C; the t-derivative
constants of F are C. All derivatives in this note hold the
independent intrinsic r fixed. No initial equality L=F(s) is used.

The actual normalization369 has arranged
\[
\begin{gathered}
n=-\frac{s^2}{4t^2}+f,\qquad f\in F,\qquad
g=\frac{f''}{2}\in F^*,\qquad E=\frac{g'}3+\frac gt\in F^*,\\
\sigma=A r^2+B r+e,\qquad A\in L^*,\quad B,e\in L,\\
C=\ell_s+\frac{s^2}{4t^4},\qquad
\Lambda=\frac{2sC}{t}+\ell_t,\qquad
G=f-tf'-\frac{3s^2}{2t^2}-2t^2\ell_s.
\end{gathered}
\tag{2}
\]
The coefficient E is not the slice derivation. Uppercase B is
the linear coefficient of sigma, not the eliminated slope of n.
The letter H below will denote G_s, not the full third potential.

The complete third-level parametrization and literal map are
\[
\begin{aligned}
\theta&=\frac tr\left\{g(\sigma^2-e^2)
 -\Lambda(\sigma-e)+\frac{2sr\sigma}{t^2}+r^2-2tCr\right\},\\
y&=r-\frac{\theta}{2t}+\frac{s\sigma}{2t^2}
 -\frac{n_t}{2}-tC,\\
z&=2ty+\sigma^2+\theta+n,\qquad
w=\ell-2\sigma y-n_t\sigma-n_s\theta,\\
Y&=y+\sigma X+tX^2,\quad
Z=z+(2t\sigma+s)X+t^2X^2,\quad
W=w+\theta X+sX^2.
\end{aligned}
\tag{3}
\]
The displayed numerator for theta is divisible by r. These are
polynomials in r, not identities on a punctured line. The exact
calibration, after the intrinsic affine parameter change, is
\[
J_{t,s,r}(X)=-a_0^4/\rho\in L^*.
\tag{4}
\]
Its specialization J0 at actual X=0 is the determinant of the
three intercept rows y,z,w. Coefficient-field changes have not
changed the literal fixed-r differentiation convention.

## 2. The two literal scalar coefficients

For this section only, abbreviate f2=f'' and f3=f'''. Expanding
the full intercept determinant in (3), with all moving A,B,e
derivatives retained, gives
\[
[r^8]J_0=\frac{A^4 A_s f_2(3f_2+tf_3)}4
        =3tA^4A_s gE.
\tag{5}
\]
Every factor other than A_s on the right is nonzero in L. Since
(4) is constant in r, A_s=0 and therefore A belongs to F*.

The high fourth-potential equations already proved in372 are
\[
E+\frac{A g^2G_s}{4}=0,\qquad
2tG_t+(4s+t^2B g)G_s=0.
\tag{6}
\]
The first equation, together with A in F, gives
\[
H:=G_s=-\frac{4E}{A g^2}\in F^*,\qquad
G=Hs+G_0,\qquad G_0\in F.
\tag{7}
\]
This integration uses the exact kernel of partial_s. The second
equation of (6) determines
\[
\boxed{
A=-\frac{4E}{g^2H},\qquad
B=\beta s+\beta_0,\qquad
\beta=-\frac{2tH'+4H}{t^2gH},\quad
\beta_0=-\frac{2G_0'}{tgH}.
}
\tag{8}
\]
All these expressions lie in F[s]; H' or G0' may vanish.

For reference the next exact scalar coefficient, with only A_s=0
imposed, is
\[
\begin{aligned}
[r^7]J_0=\frac{A^4}{8t^3}\big[
&-2A f_2f_3 Ht^3-A'f_2^2Ht^3\\
&+2B_s f_2t^3(3f_2+tf_3)+8t(3f_2+tf_3)\big],
\end{aligned}
\tag{9}
\]
where H initially means G_s=-3s/t^2-2t^2 ell_ss. Thus (9)
is a literal row identity before using the affine form of G.
Inserting (6)--(8), and using f2=2g,f3=2g', reduces (9) to
\[
[r^7]J_0=-\frac{A^5g^2H}{2t}
 \left(2t\frac{g'}g+t\frac{A'}A-3t\frac{H'}H-3\right).
\tag{10}
\]
Consequently
\[
2t\frac{g'}g+t\frac{A'}A-3t\frac{H'}H-3=0.
\tag{11}
\]
Taking the logarithmic derivative of the first identity in (8)
turns (11) into
\[
\frac{E'}E-4\frac{H'}H=\frac3t,
\qquad
\boxed{E=d\,t^3H^4,\quad d\in\mathbb C^*.}
\tag{12}
\]
Indeed E/(t^3H^4) has zero exact t derivative and lies in F.
Its constant is complex by the retained constant-field theorem,
and is nonzero. This is not an integration in a presumed rational
function field. No division by A', H', or g' is made.

Solving the definition of G in (2) and integrating its s derivative
now records the complete second coefficient potential as
\[
\boxed{
\ell=-\frac{s^3}{4t^4}-\frac{Hs^2}{4t^2}
       +\frac{(f-tf'-G_0)s}{2t^2}+l,
\qquad l\in F.
}
\tag{13}
\]

## 3. One lower genuine coefficient determines e

Let Q be the complete fourth polynomial365(7), exactly as used
in372 and374, including all lower coefficient derivatives. Its
evaluation is a coefficient-field constant q0. The terms involving
the third level h_t,h_s are -h_t sigma-h_s theta, of intrinsic
degrees at most two and three. They therefore do not affect the
fourth coefficient calculated here. No other term of Q is dropped.

Substitute (3),(8),(13) into that full primitive. The exact fourth
coefficient is
\[
\boxed{[r^4]Q=A^2E\,(e_0+e_1s+e_2s^2-e),}
\tag{14}
\]
where all three explicitly determined coefficients belong to F:
\[
\begin{aligned}
e_0&=\frac{8E^2l't+2EHg^2t-4Egl'-2Egl''t-Hg^3}
                 {4E^2gt},\\
e_1&=-\frac{4EG_0't+2Egt^2-2G_0'g-G_0''gt}
                  {4Egt^3},\\
e_2&=\frac{-8EHt-4EH't^2+6Hg+6H'gt+H''gt^2}
                 {8Egt^4}.
\end{aligned}
\tag{15}
\]
These identities only require the two high-Q substitutions in
(8), not the scalar differential relation (12). A useful direct
check is that differentiating the fourth coefficient formally in e
gives
\[
\partial_e([r^4]Q)
=-\frac{16E^3}{H^2g^4}=-A^2E\ne0,
\qquad \partial_e^2([r^4]Q)=0.
\tag{16}
\]
The e-independent part is a polynomial in s of degree at most two.
Equations (14),(15) follow by expansion of the full cubic in the
independent intrinsic r, followed by g'=3E-3g/t. They do not
differentiate an evaluated polynomial as though its coefficients
were fixed.

Since the evaluated Q is constant in r, and A,E are nonzero,
\[
\boxed{e=e_0+e_1s+e_2s^2\in F[s].}
\tag{17}
\]
Thus sigma belongs to F[s,r]. Formula (3), whose r numerator is
polynomially divisible by r, then places theta and y in F[s,r].
The literal intercept potentials put z and w there as well.
Derivatives of (13) remain in F[s], since both coefficient partials
preserve that ring.

For a possible subsequent coefficient-field analysis, the binary
quadratic part of sigma in the independent variables r,s is
A r^2+beta r s+e2 s^2. Its discriminant is explicitly
\[
\beta^2-4Ae_2=\frac{2}{g^2t^4}
\left\{\frac{t^2H''}{H}+2t^2\left(\frac{H'}H\right)^2
 +14t\frac{H'}H+14
 -\frac{4tE}{g}\left(t\frac{H'}H+2\right)\right\}.
\tag{18}
\]
No vanishing or nonvanishing of (18) is claimed. This is not a
rank assertion about an original-coordinate quadratic form.

## 4. Exact strong return removes only the finite s extension

The preceding conclusion and the exact retained field return (1)
give both inclusions
\[
K=\mathbb C(y,z,w)\ \subseteq\ F(s,r)\ \subseteq\ L(r)=K.
\tag{19}
\]
Therefore K=F(s,r). Since r is transcendental over L,
\[
L\cap F(s,r)=F(s).
\tag{20}
\]
For an elementary proof, if an element b of L is P(r)/Q(r) with
P,Q in F(s)[r] and Q nonzero, the identity P-bQ=0 is a polynomial
identity over L. Comparing a coefficient where Q is nonzero gives
b in F(s). The reverse inclusion in (20) is immediate.
Combining (19),(20) proves
\[
\boxed{L=F(s),\qquad K=F(s,r),\qquad [F:\mathbb C(t)]<\infty.}
\tag{21}
\]
This return uses the actual equality K=C(y,z,w), not merely a
parametrization of a formal quadric or the whole polynomial-line
ring O. It leaves the finite field F over C(t) completely intact.

## 5. Boundary and evidence

Equations (8),(12),(13),(15),(17),(21) are necessary normal-form
conditions for the E nonzero alternative of372. Remaining lower
fourth-level and full scalar equations still have to hold. They
are not asserted sufficient, and no actual coordinate recognition
or exclusion follows here. The E=0 alternative is handled only
by the separately saved374. Other degree profiles and the general
cancellation objective remain outside this result.

The complete372 source and its365/369 inputs were read through
EOF in0998d4 andb3bc1b, followed by the independent high-Q
reconstruction fa3b19. Fresh unsaved ea1950 reconstructed the
literal three-row determinant coefficients (5),(9), with zero
residuals; the subsequent reduction (10) was independently checked
in6c9787. Fresh f9d202 rebuilt the complete Q4 coefficient and
verified its linear dependence on e and quadratic dependence on s.
A separate expanded reconstruction e0a17c verified every coefficient
in (15) and the exact coefficient -A^2E in (16); the discriminant
in (18) was independently simplified in af1d31.

These exact finite identities supplement the written algebraic
arguments. No saved checker was executed, imported, compiled or
rerun by this author; no earlier source or canonical index was
edited. No novelty, human-expert verification, or proof-assistant
certification is claimed.
