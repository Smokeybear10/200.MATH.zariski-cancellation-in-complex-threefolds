# The degree-(3,4,5) curve cannot meet the residual ruling correctly

Working exclusion: in the full actual moving-slope chart of349 and354,
the normalized intrinsic degree pattern (deg p,deg x,deg q)=(3,4,5)
is impossible. Together with354, this improves the necessary bound to
1 <= deg sigma <= 2. The proof uses the whole polynomial-line return
and the unit ideal of the two evaluated gradient minors, not merely
the existence of a quadric and a cubic containing a rational curve.

The geometric argument is made after extending the coefficient field
to its algebraic closure. No ruling, square root, or projective
coordinate is promoted to an original coordinate of the four-ring.
There is no recognition conclusion for the remaining degree patterns.

## 1. Retained actual hypotheses and the proposed pattern

Retain every actual hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
the fourth-potential and unit-minor theorem
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md),
and the exact reductions
[349](principal-paraboloid-variable-intercept-slope-quadric-reduction-pass349-working.md),
[350](principal-paraboloid-moving-first-slope-constant-sigma-exclusion-pass350-working.md),
[351](principal-paraboloid-variable-first-slope-quadric-fibers-pass351-working.md),
and
[354](principal-paraboloid-moving-slope-intrinsic-degree-patterns-pass354-working.md).
In particular
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,
\quad \deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the full weighted initial kernel},\\
N=[u^4]\partial_Z|_A\ne0,\quad
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,\\
Nv=1,\quad K=L(v)=\mathbb C(y,z,w),\quad
O=L[v]=L[y,\sigma,\theta],\quad J(X)=-a_0^4\in L^*,\\
k=s,\quad n=Bs+f,\quad B,f\in F:=\ker_L\partial_s,
\quad b=B'\ne0.
\end{gathered}
\tag{1}
\]
Here a0=EX and the coefficient derivatives are the exact commuting
extensions of the selected chart. The field F is finite over C(t).

For clarity,349's invertible affine change over L is
\[
\begin{gathered}
A_2=n_{tt}/2-B^2,\quad C_2=\ell_s+B^2,\quad T=\ell_t,
\quad \bar h=h-B\ell+n_t^2/4,\\
x=y+n_t/2-B\sigma,\qquad p=\sigma-C_2/b,\\
q=\theta+(A_2/b)\sigma+A_2C_2/b^2-T/b,
\qquad d=\bar h-A_2C_2^2/b^2+TC_2/b.
\end{gathered}
\tag{2}
\]
It gives polynomials x,p,q in O satisfying
\[
H=x^2+bpq-d=0,\qquad O=L[x,p,q],\qquad p\notin L.
\tag{3}
\]
When writing H, Phi, or their formal derivatives, the same letters
x,p,q denote independent polynomial variables before evaluation.
The same affine substitution in the fourth level gives a polynomial
Phi in L[x,p,q] of exact total degree three. Its x p^2 coefficient
is -2b, and Phi vanishes on the actual line. All three evaluated
two-by-two minors of the formal gradients of H and Phi generate O:
\[
(H_x\Phi_p-H_p\Phi_x,\ H_x\Phi_q-H_q\Phi_x,
   H_p\Phi_q-H_q\Phi_p)O=O.
\tag{4}
\]
This is296 transported by an invertible formal affine change. It
does not depend on coefficient derivatives of that change.

Assume for a contradiction the only degree-three-p pattern left by354:
\[
(\deg_v p,\deg_v x,\deg_v q)=(3,4,5).
\tag{5}
\]
By351, odd degree of p forces d to be a nonzero square in L.
In particular d is nonzero. The argument below needs only this
nonvanishing and permits passage to an algebraic closure.

## 2. Base change, degree, and the single point at infinity

Let Omega be an algebraic closure of L. Tensoring (3),(4) with Omega
preserves the polynomial-ring equality and the unit ideal:
\[
\Omega[x(v),p(v),q(v)]=\Omega[v].
\tag{6}
\]
Thus the affine image is an integral closed copy of A1 over Omega,
not just a birationally parametrized plane curve. The function field
of that image is Omega(v). We make no descent assertion from Omega.

Use projective coordinates [Z:P:R:Q], whose affine chart Z=1 has
coordinates (p,x,q), respectively. The projective quadric is
\[
S:\quad R^2+bPQ-dZ^2=0\quad\subset\mathbb P^3_\Omega.
\tag{7}
\]
It is smooth, since b and d are nonzero. Let C be the reduced
projective closure of the image in(6). Homogenizing the polynomial
parametrization to degree five gives the base-point-free map
\[
[u:w]\longmapsto
[w^5:\ w^2p_3(u,w):\ wx_4(u,w):\ q_5(u,w)],
\tag{8}
\]
where the subscripts indicate the exact homogenization degrees.
For w nonzero the first coordinate is nonzero, and at w=0 the last
coordinate is nonzero by(5). The map is birational by(6), so it is
the normalization parametrization of C. Its pulled-back hyperplane
bundle has degree five. Therefore
\[
\deg C=5,\qquad C\setminus\mathbb A^3=\{P_\infty\},
\qquad P_\infty=[0:0:0:1].
\tag{9}
\]
The uniqueness follows directly from(8): only the parameter w=0
can map outside Z=1.

For later local calculations take w=1/v near infinity and work in
the projective Q-chart. Write its affine coordinates as
z=Z/Q, p_loc=P/Q, x_loc=R/Q. Their exact orders on the normalization
are
\[
\operatorname{ord}_{w=0}(z)=5,\qquad
\operatorname{ord}_{w=0}(p_{\rm loc})=2,\qquad
\operatorname{ord}_{w=0}(x_{\rm loc})=1.
\tag{10}
\]
These follow by subtracting the degrees in(5). Their leading
coefficients are nonzero; no generic-coefficient assumption is used.

## 3. The cubic leaves exactly one reduced ruling line

Let Phi^h be the homogenization of Phi to degree three. Its restriction
to S is not identically zero. Otherwise H would divide Phi on Z=1,
making the two evaluated gradients dependent and contradicting(4).
It therefore defines an effective cubic-section divisor D on S.

We record explicitly the elementary intersection facts being used.
Over Omega the smooth quadric is P1 x P1 by the Segre embedding.
Let F1,F2 be its two fiber classes. Then
\[
F_1^2=F_2^2=0,\qquad F_1\mathbin{\cdot}F_2=1,
\qquad H_{\rm hyp}=F_1+F_2.
\tag{11}
\]
Distinct fibers of the same projection are disjoint and linearly
equivalent, while fibers of the two different projections meet once.
The Segre coordinates are bilinear, giving the hyperplane class.
Thus the displayed intersection identities can also be read directly
as degrees on either P1 fiber.

For primary references, the Segre identification and its two line
families appear in
[Vakil, Foundations, Section 5.1, PDF page 154](https://virtualmath1.stanford.edu/~vakil/0708-216/216fall0708.pdf).
The additivity and Cartier-divisor restriction of numerical
intersections used here are
[Stacks, Lemmas 33.45.5 and 33.45.8](https://stacks.math.columbia.edu/tag/0BEL).
The degree under the birational parametrization in(9) is the
one-dimensional instance of Lemma 33.45.7 on the same page.

Since D has class 3F1+3F2, its projective degree is six. It contains
the integral degree-five curve C. Effective components have positive
projective degrees, so C has multiplicity exactly one and the
remaining divisor has degree one. An effective degree-one divisor
on the Segre quadric is one reduced ruling line. Consequently
\[
D=C+R_0,\qquad R_0\text{ a reduced line on }S.
\tag{12}
\]
There are no additional curve components or multiplicities. These
are divisors on a smooth surface, so no embedded point is being
counted as a missing degree-one component.

If R0 is of class F1, then C has class 2F1+3F2; if R0 has class F2,
the two coefficients are reversed. In either case(11) gives
\[
C\mathbin{\cdot}R_0=(3H_{\rm hyp}-R_0)\mathbin{\cdot}R_0=3.
\tag{13}
\]
Equivalently restrict the defining section of C to R0=P1. The line
bundle has degree three, and the restriction is nonzero because R0
is not a component of C. Its zero scheme has length three. This
explains the multiplicity count without assuming C is smooth at
infinity or invoking a genus formula.

## 4. Affine intersections are forbidden by the unit minors

Suppose C and R0 met at an affine point of S. Locally on the smooth
surface, the divisor identity(12) writes the restricted cubic as
a unit times a local equation of C times a local equation of R0.
Both factors vanish at that point. The differential of the restricted
cubic therefore vanishes on the tangent space of S there.

In the affine coordinates (x,p,q), this says the gradients of H
and Phi are dependent at that point. The gradient of H is nonzero
since S is smooth, and the statement also follows from the product
rule in any local coordinates on S. Every minor in(4) would vanish,
contradicting its unit ideal after the base change. Hence
\[
C\cap R_0\subseteq\{P_\infty\}.
\tag{14}
\]
The use of(4) is essential. Whole generation and a common quadric
alone do not forbid other components of a cubic from meeting the
actual affine line.

## 5. Either ruling through infinity contributes only one

If R0 does not pass through P_infinity, (14) makes the intersection
empty, already contradicting(13). Suppose it does pass through
that point. Choose delta in Omega* with delta^2=d. The two lines
of S through P_infinity are precisely
\[
P=0,\qquad R=\delta Z,
\quad\text{or}\quad
P=0,\qquad R=-\delta Z.
\tag{15}
\]
Indeed a line through [0:0:0:1] has a direction [z_1:p_1:x_1:q_1].
Substitution in(7) first forces p1=0 and then x1^2=d z1^2;
the nontrivial direction must have z1 nonzero. This gives exactly
the two lines in(15), without assuming they descend to L.

In the Q-chart the quadric is x_loc^2+b p_loc-dz^2=0. The local
ideal on S of either line in(15) is generated by x_loc minus or
plus delta z; the p_loc equation follows from the quadric. By(10),
\[
\operatorname{ord}_{w=0}(x_{\rm loc}\pm\delta z)=1.
\tag{16}
\]
There can be no leading cancellation between orders one and five.

This order is the local intersection multiplicity with C. One can
see this without presuming regularity of C: its normalization has
one point over infinity, and is finite. For its local ring A and
normalization DVR Abar, the quotient Abar/A has finite length.
Multiplication by the local equation f of the ruling in
0 -> A -> Abar -> Abar/A -> 0 shows
length(A/fA)=length(Abar/fAbar); the kernel and cokernel of f on
the finite-length quotient have equal lengths. The last length is
the order in(16). All residue fields are Omega. Thus
\[
i(P_\infty;C,R_0)=1.
\tag{17}
\]
Combining(14),(17), the total intersection length is at most one,
contradicting the exact value three in(13). This excludes(5).

## 6. Scoped consequence and remaining boundary

The only degree-three-p pattern in354 was(5), and p differs from
sigma by an element of L. Its exclusion therefore gives
\[
\boxed{\text{Under the full actual hypotheses(1),}\quad
1\le\deg_v\sigma\le2.}
\tag{18}
\]
No other remaining pattern of354 is excluded by this note. The
coefficient functions still lie in the exact finite field, and full
calibration, strong intercept return, and original-ring questions
remain required beyond the geometric necessary restrictions.

All base changes in the proof preserve the actual polynomial-line
and unit-minor equalities before geometric arguments are applied.
No rationality of L, descent of a ruling, actual polynomial status
of x,p,q, or sufficiency of the two displayed relations is claimed.
The complete direct349--351 and354 sources were read, together with
the retained full264/296 inputs. The primary Segre and intersection
references above were checked directly. The argument is a written
geometric proof, not a numerical test or a saved checker result.
No saved checker was executed, imported, compiled, or rerun, and no
earlier source, canonical index, or ledger was changed. No unrestricted
cancellation, historical novelty, or proof-assistant certification is
claimed.
