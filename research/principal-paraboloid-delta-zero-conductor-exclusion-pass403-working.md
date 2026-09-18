# The equal-degree-one Delta-zero family fails conductor stability

Working exclusion in the supplied actual264 chart with k=s and
n_ss nonzero. If sigma and theta both have intrinsic degree one,
their affine y/sigma slope lambda cannot equal n_s. The exact
necessary family401 and actual field return402 produce a finite
overring with an explicit conductor. The actual slice derivation
preserves both rings, but cannot preserve that conductor.

This excludes only the Delta-zero degree-one subcase. It does not
exclude Delta nonzero, higher equal degrees, other charts or the
unrestricted cancellation problem.

## 1. Actual inputs and the polynomial overring

Retain every actual264 hypothesis, the equal-degree-one presentation
and Delta-zero assumption of
[401](principal-paraboloid-equal-degree-one-delta-zero-necessary-family-pass401-working.md),
and the proved consequences of
[402](principal-paraboloid-delta-zero-finite-normalization-pass402-working.md).
The full initial kernel, original global slice, selected literal
partial, both returns and all genuine coefficient conditions remain
required. In particular B=C[X,Y,Z,W]=A0[u] has the derivation
E=partial_u and a0=EX nonzero.

Use402's notation F,xi,A,B0,Lambda,g,p,R and constants C2. Thus
F is the exact constant field of the coefficient t derivative;
xi,A,B0,Lambda and all their primes belong to F. The prime is the
exact xi derivative. The strong return has proved L=F(g), and
\[
T=F[X,g,R],\qquad B_F=F[B]\subseteq T,\qquad
R=p+tX,
\tag{1}
\]
where X,g,R are algebraically independent over F. The actual E
preserves B_F because it preserves B and kills F. Its action on
T was proved directly in402, not extended by an unproved normality
claim:
\[
\boxed{E=d_0(g)\partial_X+d_1(g)\partial_R,
\qquad d_0=a_0\in F[g]\setminus\{0\},\quad d_1=a_0t\in F[g].}
\tag{2}
\]
The partials in (2) fix g and F. Consequently E also preserves T.
The stronger coprimality and invariant-normalization statements of402
are not needed below.

The literal formulas used here are
\[
\begin{aligned}
Y={}&(\xi+X)R+g/2+(A'/2)(\xi+X)-A/2,\\
Z={}&R^2-A''g/4+C_2-B_0'X,\\
W={}&-2\xi R^2-[g+A'(\xi+X)]R+\Lambda+(X-\xi)\Lambda'\\
&+\xi^2(\xi-X)(A'')^2/8-(A')^2X/2-B_0'X^2\\
&+g[(\xi-X)A''/4-A'/2],\\
C_2={}&B_0-\xi B_0'+\Lambda'-\xi^2(A'')^2/8-(A')^2/4.
\end{aligned}
\tag{3}
\]
Every formula concerns the original X,Y,Z,W inside T; it is not
a replacement by an arbitrary abstract curve with the same degrees.

## 2. A free quadratic presentation and the exact smaller ring

Set S=F[X,Y,Z]. The coefficient of g in Y is 1/2, so
\[
T=F[X,Y,R],\qquad
g=2Y-2(\xi+X)R-A'(\xi+X)+A.
\tag{4}
\]
In this presentation, the Z formula in (3) is a monic quadratic
polynomial in R, with coefficients in F[X,Y]. Explicitly
\[
R^2+qR+b=0,
\tag{5}
\]
where
\[
\begin{aligned}
q&=\tfrac{A''}{2}(\xi+X),\\
b&=C_2-B_0'X-\tfrac{A''}{2}Y
      +\tfrac{A''A'}4(\xi+X)-\tfrac{A''A}4-Z.
\end{aligned}
\tag{6}
\]
In particular X,Y,Z are algebraically independent over F. To see
this and the freeness assertion below, work first over F[X,Y].
Substitution of the monic quadratic Z(R) preserves the highest
even R degree of a nonzero polynomial in Z. It cannot vanish.
Likewise a nonzero f(Z)+R*h(Z) cannot vanish: its two leading
R degrees have different parity. Monic division by (5) gives
existence of such a representation. Thus
\[
\boxed{T=S\oplus S R}
\tag{7}
\]
as an S-module. This is freeness, not just a pair of generators.
It holds when A''=0 as well.

Eliminate g in W by (4), and reduce its R-squared term using (5).
The exact remainder is
\[
W=C+D R,
\tag{8}
\]
where C belongs to S and
\[
\boxed{D=-A+A'(X+\xi)-\tfrac{A''}{2}(X+\xi)^2-2Y.}
\tag{9}
\]
An explicit constant remainder, retaining all lower functions, is
\[
\begin{aligned}
C={}&-AA'/2+AA''(X+\xi)/4+(A')^2(X+\xi)/2\\
&-A'A''(X+\xi)^2/4-A'Y
 +(A'')^2\xi^2(X+\xi)/8+A''(X+\xi)Y/2\\
&-2B_0X+B_0'X^2+2B_0'X\xi+\Lambda
  -\Lambda'(X+\xi)+2XZ.
\end{aligned}
\tag{10}
\]
The coefficient D is nonzero, since its Y coefficient in the
polynomial ring S is -2. No assumption on A'', A''' or a lower
coefficient is used for this nonvanishing.

Because B_F is generated over F by X,Y,Z,W, (8) gives
\[
B_F=S[D R].
\tag{11}
\]
Using (5), the square of D R satisfies
(D R)^2=-qD(D R)-bD^2. It follows that
\[
\boxed{B_F=S\oplus D S R\quad\text{inside }T=S\oplus S R.}
\tag{12}
\]
The module on the right is a ring: multiplication closes by the
displayed square relation. Conversely it is contained in S[D R].
Freeness (7) makes these coefficient descriptions exact.

## 3. Compute the conductor without assuming normality

Define the conductor of B_F in T by
\[
\mathfrak c=\{c\in T:cT\subseteq B_F\}.
\tag{13}
\]
Since 1 belongs to T, every conductor element already belongs to
B_F. Write c=f+hR using (7). Membership in B_F means h belongs
to D S, while f belongs to S. The additional condition cR in B_F
is sufficient for cT in B_F because T=S+S R. By (5),
\[
cR=-bh+(f-qh)R.
\tag{14}
\]
Thus f-qh must belong to D S. Since h already does, this is
equivalent to f belonging to D S. Consequently
\[
\boxed{\mathfrak c=D S\oplus D S R=D T.}
\tag{15}
\]
Neither B_F nor F[A0] has been assumed normal. In fact (15)
measures the exact difference from the finite normalization T.

Both rings are E-stable by (1),(2). This makes their conductor
E-stable as well, by a direct Leibniz argument. If c belongs to
the conductor and z belongs to T, then cz belongs to B_F and
\[
E(c)z=E(cz)-cE(z)\in B_F.
\tag{16}
\]
The first term is in B_F by its stability; the second is in B_F
because E(z) belongs to T. Thus E(c) is again in the conductor.
In particular (15) implies
\[
D\mid E(D)\quad\text{in }T.
\tag{17}
\]
This argument does not require a general theorem extending locally
nilpotent derivations to normalizations.

## 4. The required divisibility is impossible

Rewrite (9) in the independent variables X,g,R using (3):
\[
D=-g-2(X+\xi)R-\tfrac{A''}{2}(X+\xi)^2.
\tag{18}
\]
All of F and g are killed by E. Formula (2) therefore gives
\[
E(D)=-2d_0R-(X+\xi)(A''d_0+2d_1).
\tag{19}
\]
Both (18) and (19) have degree exactly one in R as polynomials
over F[g,X]: their leading coefficients are -2(X+xi) and -2d0,
respectively, and d0 is nonzero.

If (17) held, its quotient would belong to F[g,X] by these R
degrees. Comparing leading coefficients would give
\[
(X+\xi)Q=d_0(g),\qquad Q\in F[g,X].
\tag{20}
\]
Evaluation at X=-xi contradicts d0(g) nonzero. This evaluation
takes place in a polynomial identity, not at a possibly excluded
point of an original coefficient-field chart. It is legitimate
because xi belongs to F and X is an independent polynomial variable.

This contradicts conductor stability. Hence the supplied actual
Delta-zero degree-one family cannot exist. Under the retained
actual hypotheses,
\[
\boxed{\deg\sigma=\deg\theta=1,\quad k=s,\quad n_{ss}\ne0
\quad\Longrightarrow\quad\lambda\ne n_s.}
\tag{21}
\]

## 5. Verification and scope

This proof uses401's complete necessary family,402's genuine
strong-return L=F(g), its literal polynomial overring and the
actual derivative coefficients in F[g]. A field-only ansatz would
not justify E stability of the smaller generated ring.

Fresh unsaved d2d8c3 substituted the full formulas (3), eliminated
g and performed exact monic reduction in R. It recovered the
complete remainder (8)--(10), the pullback (18), and (19). The
free-module, conductor and stability arguments are written above,
not conclusions drawn from sampled coefficients. This saved note
requires a separate complete source review before acceptance.

The result does not assert that a coefficient field can be freely
adjoined while preserving normality. It exploits the conductor
instead. The Delta-nonzero degree-one case, larger equal degrees,
general coupling k, other initial ideals, arbitrary-chart entry
and original-ring recognition remain unresolved. The full
cancellation objective is not solved.

No saved checker was executed, imported, compiled or rerun. No
held earlier source was changed. No novelty, human-expert review
or formal certification is claimed.
