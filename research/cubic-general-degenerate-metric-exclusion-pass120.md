# The exact cubic branch has no degenerate velocity metric

In the supplied actual constant-acceleration framework, the canonical
quadratic velocity form cannot have rank at most two in the exact cubic
relative branch. No polynomial or coordinate generator of the rational
first-integral field is assumed. In rank two, the metric itself supplies
a constant ambient radical direction. Polynomial projections transverse
to that direction then supply a polynomial first integral, and the
polynomial-curve argument119 extends without making it a base coordinate.

This is an exclusion inside the actual framework90. It neither supplies
that framework for an arbitrary sliced action nor proves cancellation.

## 1. Actual hypotheses and the rational field

Retain the original-coordinate hypotheses and exact identities of
[potential90](nonconical-quadratic-potential-pass90.md),
[cubic-relation90](nonconical-cubic-relation-pass90.md), and
[moving-frame118](cubic-moving-frame-constraint-pass118.md). In particular,

\[
\begin{gathered}
B=\mathbb C[x_1,x_2,x_3,z]=A[u],\quad A=\ker E,\quad
Eu=1,\quad Ez=q_0u,\quad q_0\in\mathbb C^*,\\
S=\mathbb C[s_1,s_2]=\ker(N|A),\quad Nu=0,\quad
K=\operatorname{Frac}(S),\quad Ex_{\rm tr}=b\in S^3,\\
\Omega=\det[b,b_{s_1},b_{s_2}]\ne0,\quad
A_K=K[y_1,y_2]=K[v],\quad \deg_Y F=3,\\
L=\ker(V|K)=\mathbb C(H),\quad
Q\in\operatorname{Sym}_3(L),\quad n\in L^3\setminus\{0\},\\
Q_H=\kappa n n^t\ne0,\quad \kappa\in L^*,\qquad
n^tb=0,\quad b^tQb=-1 .
\end{gathered}
\tag{1}
\]

Here E and N are the actual locally nilpotent derivations, F generates
the generic relative evaluation ideal, and V is the nonzero rational
cubic direction of118. The normal n has been normalized by one of its
nonzero components. The full polynomial-coordinate inverse, not just
a proposed nonzero Jacobian, makes the original volume a unit of the
actual ring K[v,u].

The rationality of L is the retained one-dimensional subfield theorem,
as stated and scoped in [field-gates119](cubic-first-integral-polynomial-gates-pass119.md).
The entries of Q and the normalized n lie in L by118. Comparing one
nonzero derivative of H in its rank-one matrix differential gives the
last line of (1), with coefficient in L. The coefficient is nonzero
because Q has a nonconstant entry. Subscript H below means d/dH on L.

The field L is relatively algebraically closed in K. Indeed, if an
element of K is algebraic over L, differentiate its separable minimal
polynomial by V. Its nonzero polynomial derivative forces V to kill
that element, so it belongs to L by the definition of L. This fact
does not make H polynomial or make V locally nilpotent on S.

## 2. Rank one is impossible without a polynomial first integral

The quadratic value in (1) rules out rank zero. Suppose Q has rank
one. A nonzero rank-one symmetric matrix over L has a nonzero diagonal
entry. Choose its index j and write Q=lambda d d transposed with
lambda in L nonzero and d_j=1. For each i, the corresponding minor
of the derivative matrix is

\[
Q=\lambda d d^t,\quad d_j=1,\qquad
\det\begin{pmatrix}
\lambda_H&\lambda_Hd_i+\lambda(d_i)_H\\
\lambda_Hd_i+\lambda(d_i)_H&
\lambda_Hd_i^2+2\lambda d_i(d_i)_H
\end{pmatrix}
=-\lambda^2((d_i)_H)^2=0 .
\tag{2}
\]

The last equality uses rank Q_H=1. Thus every entry of d is a
complex constant. Consequently Q_H=lambda_H d d transposed. But
Q_H b=0 by (1), whereas lambda(d transposed b) squared=-1.
It follows that lambda_H=0, contradicting Q_H nonzero. This proves
the rank-one exclusion directly over L; no specialization of b or
affine point over L was assumed.

## 3. Rank two has a constant ambient radical

Suppose Q has rank two and choose r in L cubed spanning its kernel.
Its adjugate is a nonzero symmetric matrix of rank one, with image
Lr, so adj(Q)=c r r transposed for some c in L nonzero. Differentiating
det Q=0 gives

\[
0=\operatorname{tr}(\operatorname{adj}(Q)Q_H)
  =c\kappa(n^tr)^2,
\qquad n^tr=0,\qquad
Qr_H=-Q_Hr=0 .
\tag{3}
\]

Thus r_H is proportional to r. Normalize a nonzero entry of r to
one. All the other entry ratios have zero H derivative and lie in
C. There is therefore a constant nonzero column d in C cubed with
ker Q=Ld. Notice that this is a constant ambient direction, not a
primitive column obtained by a matrix over S.

Let W=ker(n transposed) over L. It contains d. The restriction of Q
to W has rank at most one, and its value on b makes that rank exactly
one. Choose e in W with theta=Q(e,e) nonzero. In the basis e,d write
b=beta e+omega d over K. The quadratic value gives theta beta squared
equal to -1. Relative algebraic closedness puts beta in L. Hence

\[
b=p+\omega d,\qquad p=\beta e\in L^3,\quad
d\in\mathbb C^3\setminus\{0\},\quad \omega\in K,\qquad
Q(p,p)=-1,\quad Qd=0,\quad p,d\in W .
\tag{4}
\]

Here omega is not in L. Otherwise b would lie in L cubed, so V(b)=0.
Writing V as a nonzero rational combination of the original two base
derivatives would contradict the independence of b_s1,b_s2 supplied
by Omega nonzero.

## 4. Polynomial projections produce a polynomial field generator

Choose a constant matrix in GL3(C) taking d to the second coordinate
vector, and apply it to the three original good coordinates. This is
an actual ambient linear automorphism. The first and third entries
of the resulting polynomial speed are constant linear projections
annihilating d. By (4) they belong to L intersect S. They cannot both
be complex constants: then the two base derivatives of the speed
would both be multiples of the second coordinate vector, making
Omega zero.

Thus L intersect S contains a nonconstant polynomial. Applying
de Bondt's Theorem3.1 to a reduced polynomial numerator and denominator
of H gives a polynomial generator g of L. Lemma3.3 gives the exact
intersection. In the new constant ambient coordinates we obtain

\[
L=\mathbb C(g),\qquad S\cap L=\mathbb C[g],\qquad
g\in S\setminus\mathbb C,\qquad
b=(a(g),w,f(g))^t,\quad a,f\in\mathbb C[T],\quad w\in S\setminus L .
\tag{5}
\]

The source hypotheses are precisely that L is the rational field
C(H) inside Frac(S) and contains the nonconstant polynomial just
constructed. No assertion that the two projections generate L is
needed. The intersection statement concerns this generator g, not an
arbitrary polynomial member of L.[^field]

The element w is the second entry of the transformed actual polynomial
speed. Its difference from omega in (4) is in L. No polynomiality of
omega or of the entries of p is being asserted. Also g need not be a
coordinate of S, and neither the map (g,w) nor any matrix over L is
claimed to be an ambient automorphism.

As in [polynomial-curve119, Section 1](cubic-polynomial-curve-exclusion-pass119.md),
a constant linear combination of a and f equal to zero contradicts
Omega nonzero. A nonzero constant combination puts b in a fixed affine
plane: applying its constant normal row to the moving-frame second
derivatives forces G=0 and hence the cubic tensor T=0, contradicting
the exact cubic branch. Otherwise constant elimination of leading
coefficients and, if needed, a swap give 0<deg a<deg f. These are
again only constant changes of the actual first and third coordinates.

## 5. The rational derivative transfer does not require g to be a coordinate

Relative algebraic closedness shows that w is transcendental over L.
Thus g,w are a transcendence basis of K over C, and K is finite
separable over C(g,w). Put J=g_s1 w_s2-g_s2 w_s1, which is nonzero.
The dual derivations are explicitly

\[
\begin{gathered}
D_g=J^{-1}(w_{s_2}\partial_{s_1}-w_{s_1}\partial_{s_2}),\qquad
D_w=J^{-1}(-g_{s_2}\partial_{s_1}+g_{s_1}\partial_{s_2}),\\
D_gg=D_ww=1,\quad D_gw=D_wg=0,\quad [D_g,D_w]=0,\quad
\ker(D_w|K)=L,\\
x=a(g),\quad D_x=(a'(g))^{-1}D_g,\quad
[D_x,D_w]=0,\quad
D_x|_L=\delta=(a'(g))^{-1}d/dg,\quad L^\delta=\mathbb C .
\end{gathered}
\tag{6}
\]

The commutator in the first line kills g,w, hence is zero on their
finite separable extension K. For the kernel assertion, D_w kills L.
If an element z of its kernel were transcendental over L, K would
be algebraic over L(z), so D_w would vanish on K, contrary to D_w w=1.
Every kernel element is therefore algebraic over L and lies in L.
The second commutator follows because D_w kills a'(g). The constant
field of delta is C because L=C(g) and a' is nonzero.

The tangent components in the (x,w) frame are obtained from the old
ones by the invertible matrix with rows (x_s1,x_s2) and (w_s1,w_s2).
The base volume changes by det of that matrix, a'(g)J in K nonzero.
The exact degree of F is preserved by this GL2(K) change. The actual
ring remains K[v,u], with no v-dependent localization. Extending the
commuting derivations by killing v,u preserves the potential and
original unit-volume identities90. Equivalently, one can redo their
differential-basis calculation in the basis dx,dw over K. The radial
coefficient rho is unchanged.

These are all the transfer hypotheses used in polynomial-curve119,
Section 2. That proof already allowed the constant field L to be a
nontrivial algebraic extension of C(x). The new point here is that
K itself need not be C(g,w); (6) proves every constant-field assertion
needed for its integrations without assuming such an equality.

## 6. The all-degree scalar argument transfers over C(g)

Set F=f(g), use primes for delta, and put Gamma=F-xF'. The frame
determinant is Gamma, so it is nonzero. The radial connection and
cubic coefficient in the commuting frame, and the necessary scalar
identities from the actual potential and volume, are

\[
\begin{gathered}
\mathfrak g=F''/\Gamma,\qquad
\tau=-\mathfrak g'-2x\mathfrak g^2\ne0,\qquad
\rho=A(g)+c_0w,\quad A(g)\in L,\quad c_0\in\mathbb C,\\
\mathfrak h=-\frac14\left(3x\mathfrak g+\frac{\tau'}{\tau}\right),
\qquad
\mathfrak h'+\mathfrak h^2+x\mathfrak g\mathfrak h-\mathfrak g=0,\\
f(g)=\lambda a(g)^3+\mu a(g),\qquad
\lambda\in\mathbb C^*,\quad\mu\in\mathbb C .
\end{gathered}
\tag{7}
\]

For clarity, the first two lines are not inferred from the metric
alone. They are the coefficient consequences proved in119 from the
full actual cubic potential and unit-volume determinant. Every
integration in w uses ker D_w=L, and every comparison of powers of w
uses its transcendence over L, both proved in (6). The exactness of
the linear potential coefficients is preserved by the commuting
rational frame. Thus the same proof yields those lines here.

The last line uses the full written all-degree argument in
[polynomial-curve119, Sections 3--4](cubic-polynomial-curve-exclusion-pass119.md),
not a finite test. Its formal-series field is formed from the abstract
one-variable field C(g) at g infinity. It uses no property of closed
fibers of the polynomial g in Spec(S). If n=deg a and m=deg f, the
embedding with x=a(g) and formal parameter x to the power -1/n gives
leading exponent r=m/n. The scalar residual has leading coefficient
-(3r-1)(r-3)/16, forcing m=3n. For a lower remainder, the first-variation
coefficient is the product of r-1,r-3,r-5,r-7,r-9 divided by192.
For 0<=r<3 only r=1 can vanish. Subtracting the corresponding multiple
of a leaves exponent less than one and forces the remainder to be zero.
The nonlinear-order comparison in119 applies unchanged, since its
small series and all of their derivatives lie in this same C(g)
Laurent-series field. This proves the last line of (7) under the
changed base hypothesis.

## 7. The global root-divisor contradiction needs only a polynomial g

After the constant first/third coordinate changes above, put
X=x3-mu x1. The exact reconstruction in the (x,w) frame gives

\[
X=3\lambda a(g)^2x_1-2\lambda a(g)^3u
      -2\lambda a(g)^3\rho,\qquad
B\cap K=S,\qquad
T(g):=a(g)^3A(g)\in S\cap L=\mathbb C[g] .
\tag{8}
\]

Indeed, a member of B intersect K is killed by E, hence belongs to A,
and is then killed by N, whose full kernel is S. The converse inclusion
is immediate. The reconstruction first puts a(g) cubed rho in B
intersect K. Subtract c0 a(g) cubed w in S and apply (5) to obtain T.
This does not assert A(g) itself is polynomial.

Choose a complex root g0 of the nonconstant one-variable polynomial a
and put h0=-2lambda T(g0). Substituting rho=A(g)+c0w in (8) gives

\[
X-h_0\in(g-g_0)B,\qquad E(g-g_0)=0,\qquad
E(X-h_0)=\lambda a(g)^3\ne0 .
\tag{9}
\]

The embedded polynomial g-g0 is nonconstant, so is a nonunit of B,
whose units are exactly the nonzero complex constants. The element
X-h0 is an actual affine-linear original coordinate, hence irreducible
in B. Divisibility makes g-g0 associate to X-h0 with a complex unit
as multiplier, contradicting their different E derivatives in (9).
There is no need to assume g-g0 irreducible beforehand; if it were
reducible, the same divisibility would already be impossible. There
is also no need for g to have a polynomial complementary coordinate.

This excludes rank two. Together with Section 2 it proves that Q has
rank three in the actual exact cubic branch.

## 8. Dependency and verification scope

The new argument removes the coordinate-first-integral premise only
for the degenerate-metric cases treated here. It depends on the exact
moving-frame identities118, the stated one-dimensional field results,
and the full scalar polynomial-curve proof119. It does not depend on
a classification of rank-three metrics or on a generic polynomial
inverse for the map (g,w).

The complete saved potential90, cubic-relation90, moving-frame118,
line/rank119, field-gates119, and polynomial-curve119 proofs were read
for this transfer. The displayed primary Theorem3.1, Corollary3.2 and
Lemma3.3 proofs were freshly read, as was the stated Theorem1.1 and
its attribution. No fresh proof audit of the older Luroth--Igusa
theorem or of every deeper dependency is claimed. No numerical test
was run for this note; its field, descent and irreducibility steps
are written proof obligations. All files through119 remain unchanged.

[^field]: Michiel de Bondt, [*Rational maps H for which K(tH) has
transcendence degree 2 over K*, arXiv:1501.06046v4](https://arxiv.org/html/1501.06046v4),
Theorem3.1, implication (2) to (3) to (4), and Lemma3.3. Theorem1.1
states the rationality result already retained in119. These give a
polynomial field generator and its polynomial intersection, not a
coordinate of the invariant plane.
