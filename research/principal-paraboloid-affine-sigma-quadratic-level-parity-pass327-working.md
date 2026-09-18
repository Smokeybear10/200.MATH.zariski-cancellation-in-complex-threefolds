# Exact parity criterion for affine sigma and a quadratic level

Working result: in the actual nonzero-coupling principal chart264, suppose
sigma is affine nonconstant in the generic line parameter and
S=sigma^2+k_t sigma+m theta has degree exactly two. The all-X polynomial
return325 is then equivalent, as a coefficient-field polynomial-generation
condition, to one explicit nonzero constant reflection coefficient.
This determines the even part of y. The retained monic surface bounds
y by degree three, with sharper bounds in two stated subcases.

This is an exact characterization of the polynomial-generation condition
in this degree sector, not a converse to the actual chart hypotheses or
recognition. In particular it does not impose the full calibrated
Jacobian merely by checking the parity criterion.

## 1. Actual assumptions and a coefficient-field centering

Retain all actual assumptions of
[264](principal-one-affine-paraboloid-chart-pass264-working.md) and the
fully read all-specialization result
[325](principal-paraboloid-all-specializations-affine-line-profile-pass325-working.md).
Thus
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad
\deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(X^2Z-Y^2),\quad a=EX\in L^*,\quad
[L:\mathbb C(t,s)]<\infty,\\
K=\operatorname{Frac}A=L(v),\quad Nv=1,\quad Na=Nt=Ns=0,
\quad O=L[v]=L[y,\sigma,\theta],\\
L[X,Y,Z,W]=L[X,v],\qquad m=k_s\ne0.
\end{gathered}
\tag{1}
\]
All these are the retained actual rings and fields. The last ring
equality follows from actual E-stability and the whole-line return,
not merely from the formal equations below. The full calibration
det d(Y,Z,W)/d(t,s,v)=-a^4 remains an assumption of the actual chart.

The literal map and potentials are
\[
\begin{aligned}
Y&=y+\sigma X+tX^2,\\
Z&=z+(2t\sigma+k)X+t^2X^2,\\
W&=w+\theta X+sX^2,\\
z&=2ty+\sigma^2+k_t\sigma+m\theta+n,\\
mw&=\ell-(2\sigma+k_t)y-F(\sigma,\theta),\\
F(P,V)&=\frac{k_{tt}}2P^2+m_tPV+\frac{m_s}2V^2+n_tP+n_sV.
\end{aligned}
\tag{2}
\]
All coefficient derivatives in F are those of the retained chart.
The arguments below take polynomial degrees and formal coefficients;
they do not differentiate a moving centered parameter.

Assume deg_v sigma=1 and deg_v S=2, where
S=sigma^2+k_t sigma+m theta. Translate v by an element of L, with
no square-root extraction, so that
\[
\begin{gathered}
\xi=v-v_c,\qquad S=q\xi^2+s_0,\qquad q\in L^*,\\
\sigma=\beta\xi+\sigma_0,\qquad \beta\in L^*,\\
\theta=\theta_2\xi^2+\theta_1\xi+\theta_0,\qquad
\theta_2=\frac{q-\beta^2}{m},\qquad
\theta_1=-\frac{\beta(2\sigma_0+k_t)}m .
\end{gathered}
\tag{3}
\]
Here v_c is minus the linear coefficient of S divided by twice its
quadratic coefficient. All coefficients in (3) belong to L. The
centering is only an automorphism of L[v], not an original complex
coordinate change. The quadratic coefficient theta2 may vanish.

Write the unique even-odd decompositions, using a formal variable R,
\[
y=E_0(\xi^2)+\xi A(\xi^2),\qquad
w=W_0(\xi^2)+\xi B(\xi^2),
\quad E_0,A,W_0,B\in L[R].
\tag{4}
\]

## 2. Exact odd module and its unit criterion

The combination
\[
Z-2tY-n-kX+t^2X^2=S=q\xi^2+s_0
\tag{5}
\]
puts R=xi^2 in L[X,Y,Z,W]. Conversely (5) recovers Z from
X,Y,R. Subtract the even parts of Y and W, which are polynomials
in X,R already in this ring. Their remaining odd parts are
\[
\xi(A(R)+\beta X),\qquad \xi(B(R)+\theta_1X).
\tag{6}
\]
Consequently, with R identified with xi^2,
\[
\begin{aligned}
L[X,Y,Z,W]
 &=L[X,R,\xi(A+\beta X),\xi(B+\theta_1X)]\\
 &=L[X,R]\ \oplus\ \xi\,(A+\beta X,D)\,L[X,R],\\
D(R)&:=B(R)-\frac{\theta_1}{\beta}A(R).
\end{aligned}
\tag{7}
\]
The second line is an equality of modules inside L[X,xi]. Products
of two odd elements lie in the even ring because xi^2=R; every odd
monomial has coefficient in the displayed ideal. Conversely the two
odd generators supply that entire odd ideal. No normality or
coordinate-descent assertion is involved.

The ring in (7) equals L[X,xi] exactly when its odd ideal is the
unit ideal. Since beta is invertible, quotienting L[X,R] by
A(R)+beta X identifies the quotient with L[R]. The image of that
ideal is (D). Thus
\[
\boxed{
L[X,Y,Z,W]=L[X,\xi]\quad\Longleftrightarrow\quad D\in L^*.
}
\tag{8}
\]
This is valid for the formal polynomial map (2),(3) as a ring
criterion. Its necessity in the actual chart follows from (1).

For completeness, if D is a unit, an explicit inverse for xi is
\[
\xi=D^{-1}\left[
 W-\bigl(W_0(R)+(\theta_2R+\theta_0)X+sX^2\bigr)
 -\frac{\theta_1}{\beta}
 \bigl(Y-E_0(R)-\sigma_0X-tX^2\bigr)\right],
\tag{9}
\]
with R supplied by (5). Together with v=xi+v_c this is a polynomial
inverse over L, not a polynomial inverse over the complex numbers.

The failure when D is not a unit also explains every specialization
edge case. If D is nonzero nonconstant, take a root r over an algebraic
closure of L and set X0=-A(r)/beta. Both odd coefficients in (6)
vanish at R=r. If r is nonzero, xi and -xi at xi^2=r are distinct
points with identical specialized coordinates. If r=0, both odd
coefficients are divisible by R, so every specialized coordinate
has zero xi-derivative at xi=0. They cannot generate the polynomial
ring, by differentiating a proposed inverse. If D is identically
zero, the same argument uses any nonzero r and its corresponding X0.
Thus neither the zero-root nor the identically-zero case is lost.

## 3. The literal potential makes D a reflection coefficient

Put g0=2sigma0+k_t and theta_even(R)=theta2 R+theta0. For the
quadratic polynomial F, its odd coefficient after (3) is exactly
\[
\beta F_P(\sigma_0,\theta_{\rm even}(R))
 +\theta_1F_V(\sigma_0,\theta_{\rm even}(R)).
\tag{10}
\]
Taking odd coefficients in the second potential of (2) therefore gives
\[
mB=-g_0A-2\beta E_0
 -\beta F_P(\sigma_0,\theta_{\rm even})
 -\theta_1F_V(\sigma_0,\theta_{\rm even}).
\tag{11}
\]
Since theta1/beta=-g0/m, the A terms cancel in D. Define
\[
\begin{aligned}
\mathcal C(R)
 &=2E_0(R)+F_P(\sigma_0,\theta_{\rm even}(R))
       -\frac{g_0}{m}F_V(\sigma_0,\theta_{\rm even}(R)),\\
D(R)&=-\frac{\beta}{m}\mathcal C(R).
\end{aligned}
\tag{12}
\]
For the two reflected parameter values xi,-xi, this is exactly the
midpoint expression325: their y-sum is 2E0 and their projected means
are sigma0 and theta_even. Thus (8) strengthens that necessary
no-collision condition to an exact polynomial-generation criterion
for this specified degree sector:
\[
\boxed{\mathcal C(R)=\varepsilon\in L^*.}
\tag{13}
\]
The criterion includes immersion at the reflection-fixed point xi=0.

The last two terms in the first line of (12) have degree at most one
in R. Consequently (13) forces the entire even part of y to be
\[
\begin{aligned}
E_0(R)&=y_0-
 \frac{\theta_2}{2}\left(m_t-\frac{g_0m_s}{m}\right)R,\\
\varepsilon
 &=2y_0+k_{tt}\sigma_0+m_t\theta_0+n_t
       -\frac{g_0}{m}(m_t\sigma_0+m_s\theta_0+n_s)\ne0.
\end{aligned}
\tag{14}
\]
Conversely (14), with the nonvanishing condition, implies (13) and
hence the full coefficient-field polynomial return (8), for the
formal map subject to (2),(3). It does not imply any of the other
actual assumptions in (1).

## 4. What the monic surface adds to the odd part

The actual chart also supplies the nonzero monic relation
\[
\begin{aligned}
H_0(U,P,V)&=U^2+A_1(P,V)U+A_0(P,V),\\
A_1&=F_P-(2P+k_t)F_V/m,\\
A_0&=F_V(\ell-F)/m+H_3(k;P,V)+H_2(n;P,V)
                         -\ell_tP-\ell_sV-h_0,\\
H_0(y,\sigma,\theta)&=0.
\end{aligned}
\tag{15}
\]
The Taylor polynomials H_j have factorial denominators. Under (3),
the evaluated A1 has xi-degree at most three, and the evaluated A0
has degree at most six. Indeed F has degree at most four after
substitution, F_V at most two, and each term of H3(k) at most six.
If y had degree r greater than three, y^2 would have degree 2r
strictly exceeding both r+3 and six, so could not cancel. Hence
\[
\boxed{
y=y_3\xi^3-
 \frac{\theta_2}{2}\left(m_t-\frac{g_0m_s}{m}\right)\xi^2
 +y_1\xi+y_0,
\qquad y_3,y_1,y_0\in L,
}
\tag{16}
\]
with epsilon in (14) nonzero. The criterion alone imposes no
condition on the odd coefficients y3,y1; the surface and remaining
actual differential identities may impose further conditions.

One explicit leading condition from (15), without discarding any
lower-potential coefficients, is
\[
y_3^2-\frac{2\beta m_s\theta_2}{m}y_3
 +\theta_2^3\left(\frac{m_{ss}}6-\frac{m_s^2}{2m}\right)=0.
\tag{17}
\]
This is its xi^6 coefficient: the cubic part of evaluated A1 is
-2 beta m_s theta2/m; the only degree-six terms of A0 are
-m_s^2 theta2^3/(2m) from -F_VF/m and m_ss theta2^3/6 from
H3(k). It is a necessary coefficient identity, not a sufficiency claim.

If m_s=0 as an element of the exact field, then m_ss=0 and (17)
forces y3=0. Equivalently in this subcase evaluated A1 has degree
at most two and A0 at most four. If theta2=0, (17) again gives
y3=0, while (14) gives y2=0. In particular
\[
m_s=0\Longrightarrow\deg_vy\le2,
\qquad
\theta_2=0\Longrightarrow\deg_vy\le1.
\tag{18}
\]
These implications do not assume the surface level is reducible.

## 5. Boundary and verification scope

The exact criterion is special to affine nonconstant sigma and a
quadratic S. It does not assume or prove an arbitrary selected plane
curve is smooth. It supplies no original-ring coordinate, no
normalization of k or n, and no recognition of the remaining sector.

The completely read
[326](principal-paraboloid-all-specializations-differential-obstruction-pass326-working.md)
contains a formal family passing even the full all-X polynomial return,
the first potentials and strong intercept return, while failing the
positive-X coefficient of the calibrated determinant. That family is
not in the precise degree assumptions (3), but it correctly warns
against promoting the ring criterion to the actual chart hypotheses.
The present necessary profile and reflection equations likewise do
not replace the full scalar, fourth potential, or actual entry.

Complete saved264,325,326 and the generation lemma323 were read before
this note was saved. The parity ideal is proved algebraically, including
its zero-polynomial and zero-root boundaries. Formula (12) is derived
from the literal second potential rather than asserted from collision
geometry alone. No saved checker was executed, imported or compiled,
and no held source, checker, index or canonical packet was edited.
