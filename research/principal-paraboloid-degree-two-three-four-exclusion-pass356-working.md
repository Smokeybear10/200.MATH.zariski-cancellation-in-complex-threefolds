# Excluding the centered degree pattern (2,3,4)

Working exclusion: under the complete actual moving-slope hypotheses
of349, the centered intrinsic degrees
\((\deg p,\deg x,\deg q)=(2,3,4)\) cannot occur. The zero centered
level is excluded by an exact odd-module calculation. The nonzero
level is excluded by the cubic fourth relation and its unit evaluated
gradient minors on the smooth projective quadric.

This eliminates one pattern in354. It is not recognition of the
remaining moving-slope sector, an ambient coordinate change, or a
claim that arbitrary cancellation candidates enter this chart.

## 1. Actual inputs and the bounded claim

Retain the full actual hypotheses of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
the fourth-potential theorem of
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md),
and the specialization in
[349](principal-paraboloid-variable-intercept-slope-quadric-reduction-pass349-working.md).
In particular
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,
\quad \deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\mathrm{initial}}=(X^2Z-Y^2)\text{ is the full initial kernel},\\
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,
\quad O=L[v],\quad Nv=1,\\
K=\operatorname{Frac}A=L(v)=\mathbb C(y,z,w),\qquad
O=L[y,z,w]=L[y,\sigma,\theta],\quad J(X)=-a_0^4\in L^*,\quad a_0=EX,\\
k=s,\qquad n=B(t)s+f(t),\qquad
B,f\in\ker_L\partial_s,\qquad b=B'\ne0.
\end{gathered}
\tag{1}
\]
All coefficient derivatives are the retained exact commuting
extensions. No rationality of the coefficient field is presumed.

The affine transformation over \(L\) in349 and
[351](principal-paraboloid-variable-first-slope-quadric-fibers-pass351-working.md)
defines
\[
\begin{gathered}
A_2=n_{tt}/2-B^2,\qquad C_2=\ell_s+B^2,\qquad T=\ell_t,
\qquad \bar h=h-B\ell+n_t^2/4,\\
x=y+n_t/2-B\sigma,\qquad p=\sigma-C_2/b,\\
q=\theta+(A_2/b)\sigma+A_2C_2/b^2-T/b,\qquad
d=\bar h-A_2C_2^2/b^2+TC_2/b.
\end{gathered}
\tag{2}
\]
Its exact consequences are
\[
H_0=x^2+bpq-d=0,\qquad O=L[x,p,q],\qquad
(2x,bq,bp)O=O.
\tag{3}
\]
These are intrinsic functions, not original coordinates.

Substituting the same affine transformation into the fourth level
of349 gives a polynomial \(\Phi(x,p,q)\) of exact total degree three,
with
\[
\Phi(x(v),p(v),q(v))=0,
\qquad
\bigl((H_0)_i\Phi_j-(H_0)_j\Phi_i: i<j\bigr)O=O,
\tag{4}
\]
where \(i,j\) range over the three independent formal variables.
The last assertion follows from296 because the formal affine change
has an invertible Jacobian over \(L\). No coefficient derivative is
taken in this change of the formal gradient.

The proposed degree pattern in
[354](principal-paraboloid-moving-slope-intrinsic-degree-patterns-pass354-working.md)
is
\[
\deg_v p=2,\qquad \deg_v x=3,\qquad \deg_v q=4.
\tag{5}
\]
We prove a contradiction using (3)--(5). Neither birationality nor
normality of the plane projection is used in the projective argument.

## 2. The zero-level case is an odd-module obstruction

Suppose first that \(d=0\). The exact UFD argument in351 gives
\[
p=\lambda r^2,\qquad x=\lambda r s_1,\qquad
q=-\lambda s_1^2/b,
\quad\lambda\in L^*,\quad r,s_1\in L[v],\quad\gcd(r,s_1)=1.
\tag{6}
\]
By (5), \(r\) is affine nonconstant and \(s_1\) is quadratic.
Use \(r\) itself as a polynomial parameter, denoted \(\xi\). This
is an affine parameter change over \(L\), with no square root of a
coefficient. Write
\[
s_1=A\xi^2+B_1\xi+C,
\qquad A\in L^*,\quad B_1,C\in L,\quad C\ne0.
\tag{7}
\]
The last nonvanishing follows from \(\gcd(\xi,s_1)=1\).
Put \(T_0=\xi(A\xi^2+C)\). The exact decompositions
\[
\xi s_1=T_0+B_1\xi^2,\qquad
s_1^2=(A\xi^2+C)^2+2B_1T_0+B_1^2\xi^2
\tag{8}
\]
show that
\[
L[x,p,q]=L[\xi^2,T_0]
 =L[\xi^2]\ \oplus\ \xi(A\xi^2+C)L[\xi^2].
\tag{9}
\]
The direct-sum description follows because
\(T_0^2=\xi^2(A\xi^2+C)^2\in L[\xi^2]\); every polynomial in
the two generators reduces to the displayed form. Its odd part
cannot contain \(\xi\), since the nonconstant polynomial
\(A\xi^2+C\) does not divide one. This contradicts
\(O=L[x,p,q]=L[\xi]\). Thus \(d=0\) is impossible.

## 3. Nonzero level and the projective closure

Now assume \(d\ne0\). Extend coefficients to an algebraic closure
\(\overline L\). This does not assume that \(L\) is rational or
that its elements are ambient polynomials. The actual whole return
base-changes to \(\overline L[x,p,q]=\overline L[v]\), and the
unit identity in (4) stays a unit identity. Thus the embedded affine
curve is geometrically integral and is a smooth affine line.

Use projective coordinates \([z:p:x:q]\). The projective quadric
\[
S:\quad x^2+bpq-dz^2=0\ \subset\mathbb P^3_{\overline L}
\tag{10}
\]
is smooth, since \(b,d\ne0\). Let \(\mathcal C\) be the projective
closure of the affine line. Homogenizing the polynomial parametrization
\((1,p(v),x(v),q(v))\) to degree four gives a base-point-free morphism
\(\nu:\mathbb P^1\to\mathcal C\). It is birational by whole ring
return and is the normalization of \(\mathcal C\). Its pullback of
the hyperplane bundle is \(\mathcal O_{\mathbb P^1}(4)\), so
\(\deg\mathcal C=4\).

There is exactly one point of \(\mathcal C\) at infinity:
\[
P_\infty=[0:0:0:1].
\tag{11}
\]
In the chart \(q=1\), the orders at the unique preimage of this
point are
\[
\operatorname{ord}_\infty(z/q)=4,\qquad
\operatorname{ord}_\infty(p/q)=2,\qquad
\operatorname{ord}_\infty(x/q)=1.
\tag{12}
\]
They follow from the three exact degrees in (5), not just upper bounds.

In particular \(\mathcal C\) is smooth at \(P_\infty\). To check
this without assuming smoothness of a plane projection, let \(u=1/v\)
be the normalization parameter there. The function \(x/q\) has a
nonzero linear term in \(u\), so it generates \(\overline L[[u]]\)
as a complete power-series ring. There is just one branch at infinity.
The completed curve local ring embeds in this normalization ring and
contains all power series in \(x/q\), hence equals
\(\overline L[[u]]\). The affine part was already smooth. Therefore
\[
\mathcal C\cong\mathbb P^1,\qquad g(\mathcal C)=0.
\tag{13}
\]

## 4. The residual divisor consists of ruling lines

Over \(\overline L\), the smooth quadric is
\(\mathbb P^1\times\mathbb P^1\), with hyperplane class \((1,1)\).
The two ruling classes have self-intersection zero and mutual
intersection one. This standard Segre description is explicitly
given in [Vakil's Foundations notes, page153](https://virtualmath1.stanford.edu/~vakil/0708-216/216fall0708.pdf).

Write the bidegree of \(\mathcal C\) as \((a,c)\). Both integers
are positive: an integral curve with one bidegree zero is a single
fiber of a projection, hence has degree one, contrary to degree four.
For a smooth curve on the quadric, the degree and genus formulas are
\[
\deg\mathcal C=a+c,\qquad
g(\mathcal C)=(a-1)(c-1).
\tag{14}
\]
For example, the genus formula follows from adjunction using
\(K_S=(-2,-2)\), or from
\(0\to\mathcal O_S(-a,-c)\to\mathcal O_S\to\mathcal O_{\mathcal C}\to0\)
and \(\chi(\mathcal O_S(i,j))=(i+1)(j+1)\).
The intersection and adjunction computation is recorded in
[Chao Li's intersection-theory notes, Example15](https://www.math.columbia.edu/~chaoli/docs/IntersectionTheory.html).
Equations (13),(14) give
\[
[\mathcal C]=(1,3)\quad\text{or}\quad(3,1).
\tag{15}
\]

Homogenize \(\Phi\) to its exact degree three. It is not identically
zero on \(S\): otherwise its affine restriction would be divisible
by \(H_0\), contradicting (4). It therefore cuts an effective
Cartier divisor \(\mathcal D\) of class \((3,3)\). The curve
\(\mathcal C\) occurs with multiplicity one. A larger multiplicity
would make the restricted differential of \(\Phi\) vanish along
the affine curve and hence make every minor in (4) zero.
Thus
\[
\mathcal D=\mathcal C+\mathcal R,
\qquad
[\mathcal R]=(2,0)\quad\text{or}\quad(0,2),
\tag{16}
\]
respectively. A nonzero effective divisor of either latter class is
the sum of two fibers of the same ruling, with repetitions allowed.
This follows directly from its binary degree-two equation on the
corresponding \(\mathbb P^1\) factor. Every support line \(R\)
of \(\mathcal R\) satisfies
\[
\mathcal C\cdot R=3.
\tag{17}
\]

## 5. The unit minors forbid the required intersections

No support line \(R\) of \(\mathcal R\) can meet \(\mathcal C\)
in the affine chart. At such an intersection, a local equation for
the cubic divisor on the smooth surface factors as a curve equation
times a residual equation, both vanishing at the point. Its
differential on \(S\) is zero. Since the quadric is smooth, the two
ambient gradients are then proportional, contradicting the unit
ideal in (4). This argument also covers a repeated residual line.

If \(R\) misses \(P_\infty\), there are consequently no intersection
points at all, contradicting (17). If \(R\) contains \(P_\infty\),
it is one of the two ruling lines through that point. In the chart
\(q=1\), its local equation on \(S\) is
\[
x/q-\varepsilon\sqrt d\,z/q=0,
\qquad \varepsilon\in\{1,-1\}.
\tag{18}
\]
Indeed the quadric solves for \(p/q\), and substituting this equation
sets \(p/q=0\); these are exactly the two lines through the point.
By (12), the pullback of (18) to the curve has exact order one.
Therefore its only possible intersection with \(\mathcal C\) has
multiplicity one, again contradicting (17).

This excludes \(d\ne0\). The argument is valid after algebraic
closure and therefore contradicts the original exact-field data as
well. No descent of an individual residual line to \(L\) is needed.

## 6. A formal boundary control and exact conclusion

Smoothness and whole return alone do not exclude this degree profile.
For \(c_0\in L^*\), the formal family
\[
b=1,\quad d=c_0^2,\quad
p=v^2,\quad x=v^3+c_0,\quad q=-v^4-2c_0v
\tag{19}
\]
satisfies \(x^2+pq=d\) and generates the whole line, because
\(v=-(q+p^2)/(2c_0)\). It also has a cubic relation linear in \(x\):
\[
\Phi_0=2c_0(x-c_0)+pq+p^3=0.
\tag{20}
\]
At \(v=0\), however, the gradients of the quadric and this cubic
are both \((2c_0,0,0)\). Every evaluated minor vanishes there.
Thus the full-minor input is essential; this family is not asserted
to satisfy the actual fourth-potential formulas or scalar calibration.

Combining the zero- and nonzero-level arguments proves
\[
\boxed{\text{Under the actual hypotheses (1),}
\quad(\deg_v p,\deg_v x,\deg_v q)\ne(2,3,4).}
\tag{21}
\]
No other pattern in354 is eliminated by this note. The coefficient
functions remain in the exact finite field, and no intrinsic change
has been promoted to an original coordinate or invariant.

The complete264,296,349,351,354 sources were read before this proof.
The primary Segre and adjunction statements above were freshly checked.
Fresh unsaved algebra checked the exact odd-module decompositions and
the formal boundary family's relation, inverse, and failed minor
condition. No saved checker was executed, imported, compiled, or
rerun by this author; no earlier source or canonical index was edited.
No human-expert, proof-assistant, publication, novelty, or unrestricted
cancellation claim is made.
