# Two rank-one modes excluded by polynomial-generation degrees

Working scoped exclusion: under the complete actual376 entry, the
nonzero logarithmic-slope mode of380 is impossible. The zero-slope
mode is also impossible when G0 is constant. The proof uses the
coefficient-adjoined polynomial return of379 and the characteristic-zero
Abhyankar--Moh degree-divisibility theorem.

The zero-slope case with G0' nonzero is not excluded here. This note
does not identify F with C(t), promote an F-polynomial change to an
original-coordinate change, or assert unrestricted cancellation.
It excludes supplied actual charts in two specified modes.

## 1. Complete retained entry and notation

Retain every actual hypothesis and exact-field identity of
[376](principal-paraboloid-quadratic-cubic-nonzero-leading-normal-form-pass376-working.md),
including its264/365/369/372 entry. In particular the original ring is
globally sliced, its degree profile is exact, and the initial relation
generates the full initial kernel:
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A_0[u],\qquad
\mathscr E=\partial_u,\qquad A_0=\ker\mathscr E,\\
\deg_{\mathscr E}(X,Y,Z,W)=(1,2,2,2),\qquad
I_{\rm initial}=(X^2Z-Y^2),\qquad a_0=\mathscr EX\ne0,\\
N=[u^4]\partial_Z|_{A_0},\qquad
L=\operatorname{Frac}\ker_{A_0}N,\qquad
F=\ker_L\partial_s,\quad [F:\mathbb C(t)]<\infty,\\
L=F(s),\qquad K=F(s,r)=\mathbb C(y,z,w),\qquad
L[r]=L[y,\sigma,\theta]=L[y,z,w].
\end{gathered}
\tag{1}
\]
The exact coefficient partials commute. Primes denote the exact
t derivative on F, whose constants are C. The variables s,r are
algebraically independent over F. None is asserted to be an original
polynomial coordinate.

The literal original map is
\[
Y=y+\sigma X+tX^2,\quad
Z=z+(2t\sigma+s)X+t^2X^2,\quad
W=w+\theta X+sX^2.
\tag{2}
\]
The complete potentials and calibrated scalar, not just these formal
expressions, remain hypotheses. In the nonzero-E quadratic-cubic
case376 gives
\[
\begin{gathered}
n=-\frac{s^2}{4t^2}+f,\qquad
g=f''/2\in F^*,\qquad E=g'/3+g/t\in F^*,\qquad H\in F^*,\\
\ell=-\frac{s^3}{4t^4}-\frac{Hs^2}{4t^2}
       +\frac{(f-tf'-G_0)s}{2t^2}+l,\qquad f,G_0,l\in F,\\
\sigma=A r^2+(\beta s+\beta_0)r+e,\qquad
e=e_2s^2+e_1s+e_0,\qquad A\in F^*,\quad\beta,\beta_0,e_i\in F.
\end{gathered}
\tag{3}
\]
Here E is a coefficient, not the slice derivation. Set
\[
C=\ell_s+\frac{s^2}{4t^4},\qquad
\Lambda=\frac{2sC}{t}+\ell_t,\qquad
\zeta=tH'/H+2.
\tag{4}
\]
The intercept formulas used literally below are
\[
\begin{aligned}
\theta&=\frac tr\left\{
g(\sigma^2-e^2)-\Lambda(\sigma-e)
 +\frac{2sr\sigma}{t^2}+r^2-2tCr\right\},\\
y&=r-\frac{\theta}{2t}+\frac{s\sigma}{2t^2}
       -\frac{n_t}{2}-tC,\\
z&=\left(\sigma+\frac{s}{2t}\right)^2+2tr+Hs+G_0,\\
w&=\ell-2\sigma y-n_t\sigma+\frac{s\theta}{2t^2}.
\end{aligned}
\tag{5}
\]
The numerator defining theta is divisible by r. These are polynomial
identities in F[s,r], including at r=0, not a punctured-line return.

## 2. Polynomial return and the external degree theorem

The fully read and independently reviewed
[379](principal-paraboloid-quadratic-cubic-polynomial-return-speeds-pass379-working.md)
proves, using the original slice and actual E/N stability,
\[
F[\mathcal B]=F[X,s,r],\qquad F[A_0]=F[s,r].
\tag{6}
\]
In particular quotienting(6) by the indeterminate X gives
\[
F[y,z,w]=F[s,r].
\tag{7}
\]
This polynomial-ring equality, stronger than the field equality in(1),
is indispensable. No normality of an arbitrary coefficient-adjoined
ring or slice for N is being presumed.

We use the classical degree consequence: for a characteristic-zero
field k, positive-degree polynomials p(T),q(T) with k[p,q]=k[T]
have degrees one of which divides the other. For a proof over an
algebraically closed field, see García Barroso--Płoski,
*Polynomial automorphisms of the affine plane and singularities of
algebraic curves*, Revista de la Real Academia Canaria de Ciencias
30 (2018), Theorem6.7, p.47. Section3, p.35, defines embedding by this
ring equality. [Primary proof](https://ergarcia.webs.ull.es/2018-GB-Ploski-RACC.pdf).
For arbitrary k, extend to its algebraic closure: generation and both
degrees persist. This application requires no descent of an ambient
plane automorphism.

## 3. Nonzero slope and the exact completed square

The independent necessary gates
[377](principal-paraboloid-quadratic-cubic-lower-potential-two-mode-gate-pass377-working.md)
and
[378](principal-paraboloid-quadratic-cubic-sixth-scalar-gate-pass378-working.md)
are composed in
[380](principal-paraboloid-quadratic-cubic-mode-composition-pass380-working.md).
For zeta nonzero they give
\[
\begin{gathered}
\frac{tE}{g}=\zeta,\qquad
A=-\frac{4\zeta}{tgH},\qquad
\beta=\frac{AH}{2t},\qquad e_2=\frac{AH^2}{16t^2},\\
\beta_0=-\frac{2G_0'}{tgH},\qquad
G_0'=\lambda t^2H^2,\qquad\lambda\in\mathbb C.
\end{gathered}
\tag{8}
\]
The e1 formula of376, with E=zeta*g/t and
G0''=2(zeta-1)G0'/t, further gives
\[
e_1=\frac{\beta_0H}{4t}-\frac1{2t}.
\tag{9}
\]
No division by lambda occurs. Define only over F
\[
\delta=\frac{\beta_0}{2A},\qquad
D=e_0-\frac{\beta_0^2}{4A},\qquad
q=r+\frac{Hs}{4t}+\delta,\qquad
J=\sigma+\frac{s}{2t}=Aq^2+D.
\tag{10}
\]
The symbol J here is a quadratic polynomial, not the scalar Jacobian.
We have F[s,q]=F[s,r]. Equation(5) now becomes
\[
z=J^2+2tq+\frac H2s+G_0-2t\delta,\qquad
s=\frac2H\left(z-J^2-2tq-G_0+2t\delta\right).
\tag{11}
\]
Thus F[z,q]=F[s,r], with z,q algebraically independent over F.
Combining(7),(11), and localizing at the nonzero elements of F[z],
gives
\[
k[y,w]=k[q],\qquad k=F(z).
\tag{12}
\]
This is localization of proved polynomial equalities, not an assertion
that z or q is an original coordinate or that F=C(t).

## 4. Literal row identities and three degree cases

The exact coefficient expansion of(4) is
\[
\Lambda=-\frac{H\zeta s^2}{4t^3}
       -\left(\frac gt+\frac{G_0'}{2t^2}\right)s+l'.
\tag{13}
\]
Equations(8),(9) imply ge-Lambda=g*e0-l'+gs/(2t). Set
\[
\mathcal C(q)=gJ+ge_0-l',\qquad
S(q)=-\frac H{4t}
 +\frac{\zeta\mathcal C(q)/g-J}{t^2}.
\tag{14}
\]
Both are polynomials in q over F. Direct reduction of(5), with the
same original intercepts y,w, gives
\[
\boxed{
\begin{aligned}
2y&=q-\delta-(Aq+\beta_0/2)\mathcal C(q)-f'+sS(q),\\
w&=l-J(2y+f')+\frac st(q-\delta).
\end{aligned}}
\tag{15}
\]
For a short reconstruction, the first equality follows first as
2y=r-(Ar+beta*s+beta0)(g*sigma+g*e-Lambda)-s*sigma/t^2-nt.
Substitute(10),(13), nt=s^2/(2t^3)+f', and use
-AH/(4t)=zeta/(g*t^2). The second follows from the general identity
\[
w=l-J(2y+f')+\frac{sr}{t}+\frac{Hs^2}{4t^2},
\qquad J=\sigma+\frac{s}{2t},
\tag{16}
\]
obtained from(5). Substituting r from(10) cancels the s-squared terms.

Eliminate s by(11) and regard y,w as polynomials in q over k. The
leading coefficient of s is -2A^2/H in degree4.

If zeta is not1, S has degree2 with leading coefficient
(zeta-1)A/t^2. The exact degree pair is
\[
\deg_q y=6,\quad [q^6]y=-\frac{A^3(\zeta-1)}{Ht^2};
\qquad
\deg_q w=8,\quad [q^8]w=\frac{2A^4(\zeta-1)}{Ht^2}.
\tag{17}
\]
For w, -2Jy has degree8, whereas s(q-delta)/t has degree5.
Both leading coefficients are nonzero.

If zeta=1, S(q) is a constant S0 in F. When S0 is nonzero,
\[
\deg_q y=4,\quad [q^4]y=-\frac{A^2S_0}{H};
\qquad
\deg_q w=6,\quad [q^6]w=\frac{2A^3S_0}{H}.
\tag{18}
\]
When zeta=1 and S0=0, y has degree3 and w degree5, with
\[
[q^3]y=-\frac{A^2g}{2},\qquad
[q^5]w=A^2\left(gA-\frac2{Ht}\right)
       =-\frac{6A^2}{Ht}\ne0.
\tag{19}
\]
The last equality uses gA=-4/(Ht) from(8). It explicitly checks
possible cancellation of the two degree5 terms in w.

None of(6,8),(4,6),(3,5) has one degree dividing the other.
Each contradicts(12) and the theorem in Section2. The entire
zeta-nonzero mode is therefore excluded.

## 5. Zero slope with constant G0

Suppose zeta=0 and G0'=0. The zero-mode conclusions of380 and the
exact376 coefficients give
\[
\beta=e_2=\beta_0=0,\qquad e_1=-\frac1{2t},\qquad
\sigma=Ar^2+e_0-\frac{s}{2t},\qquad
J=\sigma+\frac{s}{2t}=Ar^2+e_0.
\tag{20}
\]
The coefficient A is still nonzero. Here Lambda=-gs/t+l', and the
literal rows(5),(16) reduce to
\[
\begin{aligned}
2y&=r-Ar(gJ+ge_0-l')-\frac{sJ}{t^2}-f',\\
z&=J^2+2tr+Hs+G_0,\\
w&=l-J(2y+f')+\frac{sr}{t}+\frac{Hs^2}{4t^2}.
\end{aligned}
\tag{21}
\]
Since H is nonzero, s=(z-J^2-2tr-G0)/H and F[z,r]=F[s,r].
Equation(7) again gives k[y,w]=k[r] over k=F(z). The exact degrees
after this substitution are
\[
\deg_r y=6,\quad [r^6]y=\frac{A^3}{2Ht^2};
\qquad
\deg_r w=8,\quad [r^8]w=-\frac{3A^4}{4Ht^2}.
\tag{22}
\]
For the last coefficient, -2Jy contributes -A^4/(Ht^2) and
Hs^2/(4t^2) contributes A^4/(4Ht^2), while sr/t has degree5.
The pair(6,8) again contradicts polynomial generation.

## 6. Conclusion and verification boundary

Within the retained actual376 family, necessarily zeta=0 and
G0' is nonzero. This note does not exclude or recognize that case.
There the completed quadratic contains an additional s term, so the
polynomial-coordinate elimination of Section5 is not established.

The complete held377,378 and380 sources were read through EOF in
50426c/7db248, d7fe3d and60d003. Their necessary coefficient identities
are separate from the actual polynomial return379, author-read through
bdd81f and independently reviewed through37e0de before this application.
The380 composition was independently reviewed through1c4d3f.

Fresh unsaved1baba4 reconstructed the completed square, both mode-eight
row identities, and all three degree pairs and leading coefficients
with generic coefficient-field symbols. Separate unsaved571e5b rebuilt
the zero-slope identities and(22). All stated identity residuals were
zero. The exact degree theorem and embedding definition were freshly
checked at the cited proof, pp.35 and47.

No saved checker was executed, imported, compiled or rerun. No earlier
source or canonical index was edited. These calculations supplement
the written polynomial-ring argument; no realization, original-ring
coordinate descent, unrestricted cancellation, novelty, human-expert
verification or proof-assistant certification is claimed.

