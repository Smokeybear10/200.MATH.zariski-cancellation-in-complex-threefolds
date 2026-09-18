# The actual cubic branch excludes a rational ruled nondegenerate metric

In the supplied actual cubic framework, a rank-three ambient metric
cannot restrict to rank one on the plane containing the velocity.
The argument needs neither a polynomial first integral nor a base
coordinate. Relative algebraic closedness supplies a rational point
on the relevant affine line, and commuting rational derivatives
transfer the complete potential and unit-volume argument119.

Consequently, when the ambient metric has rank three, its restriction
to that plane has rank two and its determinant is a nonconstant
element of the rational first-integral field. The lower-rank ambient
cases are not excluded by this note alone. No original-frame entry,
global recognition, or cancellation statement is inferred.

## 1. Retained actual hypotheses and the coefficient field

Retain the full original-coordinate, slice, generation and volume
hypotheses of [cubic-relation90](nonconical-cubic-relation-pass90.md),
in its exact relative degree-three branch. In particular the original
polynomial four-space has three good coordinates with velocity
\(b\in S^3\), where \(S=\mathbb C[s,t]\), the fourth coordinate
has nonzero constant acceleration \(q_0\), and
\(A_K=K[y_1,y_2]=K[v]\) for \(K=\operatorname{Frac}S\).
The actual frame \([b,b_s,b_t]\) is invertible over K. The
nonzero original-coordinate Jacobian is a unit of \(K[v,u]\).

[Moving-frame118](cubic-moving-frame-constraint-pass118.md) supplies
a nonzero rational cubic direction V, its field of constants L,
the ambient symmetric matrix Q, and a normalized normal n. Retain
the rationality conclusion explained in
[the source gate119, Section1](cubic-first-integral-polynomial-gates-pass119.md):
\[
\begin{gathered}
L=\ker(V|K)=\mathbb C(H),\qquad L\text{ relatively algebraically closed in }K,\\
Q\in\operatorname{Sym}_3(L),\quad n\in L^3\setminus\{0\},\quad
n^t b=0,\quad b^tQb=-1,\\
\frac{dQ}{dH}=\kappa nn^t\ne0,\qquad \kappa\in L^*,
\qquad T(V,-,-)=0 .
\end{gathered}
\tag{1}
\]
Here H is merely a rational generator of L. Relative algebraic
closedness also follows directly: applying V to the separable
minimal polynomial of an element of K algebraic over L shows that
the element is killed by V and hence belongs to L.

For precision, the derivative formula in (1) is not a new change
of the metric. Normalize a nonzero component of n to one in the
formula118. Since Q and n have entries in L, differentiating Q
with respect to either original coordinate gives
\(Q_H H_i\), while formula118 makes it a scalar multiple of
\(nn^t\). Choose \(H_i\ne0\). The normalized diagonal entry
shows that the scalar in \(Q_H\) lies in L. It is nonzero
because Q has a nonconstant entry. Thus (1) follows without
assuming H is an original coordinate or introducing a new frame.

## 2. Rank one supplies an affine line over L

Put \(W=\ker(n^t:L^3\to L)\) and suppose that the restriction
of Q to W has rank one. Choose \(p_0\in W\) with
\(c=Q(p_0,p_0)\ne0\), and define
\(\ell(z)=Q(p_0,z)/c\) on W. Rank one and characteristic zero
give \(Q(z,z)=c\ell(z)^2\), with \(\ell(p_0)=1\).
The actual vector b therefore gives
\[
\begin{gathered}
\lambda=\ell(b)\in K,\qquad \lambda^2=-1/c,
\qquad \lambda\in L^*,\\
p=\lambda p_0\in W,\qquad Q(p,p)=-1,\qquad
Lq=\ker\ell\subset W,\quad q\ne0,\\
b=p+wq,\qquad p,q\in L^3\text{ independent},\qquad w\in K\setminus L .
\end{gathered}
\tag{2}
\]
The square root belongs to L because L is relatively algebraically
closed in K. This is the rational-point gate: no point on a conic
over L is assumed beforehand. Then b minus p lies in the
one-dimensional L-defined radical after extension to K, giving w.

If w were in L, all entries of b would be killed by V. The equation
\(V(b)=0\), with V a nonzero K-linear combination of
\(\partial_s,\partial_t\), would make \(b_s,b_t\) dependent,
contrary to the invertible actual frame. Thus w is not in L.
Relative algebraic closedness now makes w transcendental over L.
No claim that p, q, H or w are polynomial is made.

## 3. The finite field extension preserves the needed derivatives

The field K is a finite separable extension of \(L(w)\), since
both have transcendence degree two over \(\mathbb C\). The
coordinate derivations on \(\mathbb C(H,w)\) extend uniquely
to K. Write them as \(D_H,D_w\). They satisfy
\[
\begin{gathered}
D_HH=1,\quad D_Hw=0,\quad D_wH=0,\quad D_ww=1,
\qquad [D_H,D_w]=0,\\
\ker(D_w|K)=L,\qquad D_H|L=d/dH,\qquad
D_w=V/V(w),\\
\Delta=\det\frac{\partial(H,w)}{\partial(s,t)}\in K^* .
\end{gathered}
\tag{3}
\]
For a separable algebraic element with minimal polynomial P,
the extension is forced by
\(D\alpha=-D(P)(\alpha)/P'(\alpha)\). This proves uniqueness;
the commutator is a derivation killing the base field and therefore
vanishes. To check the full constants claim, suppose an element
\(\alpha\in\ker D_w\) were transcendental over L. Then K
would be finite algebraic over \(L(\alpha)\), so the same
uniqueness argument would force \(D_w=0\), contradicting
\(D_ww=1\). Thus \(\alpha\) is algebraic over L and belongs
to L. Equality with \(V/V(w)\) follows from its two values on
H,w and the same uniqueness. Finally dH,dw are independent in
\(\Omega^1_{K/\mathbb C}\), proving \(\Delta\ne0\).

These statements allow K to be a proper finite extension of
\(\mathbb C(H,w)\). They do not identify its generic affine
curve with a line or invert a map of the original affine plane.

## 4. The actual potential and unit volume transfer

Let M be the invertible two-by-two matrix whose columns express
\(D_H,D_w\) in the original coordinate derivatives. In the
actual three-dimensional frame and relative column y, use
\[
\begin{gathered}
\widetilde{\mathcal C}=[b,D_Hb,D_wb]
 =\mathcal C\operatorname{diag}(1,M),\qquad
\widetilde y=M^{-1}y,\\
\widetilde G=M^tGM,\qquad
\widetilde\Omega=\Omega\det M\ne0,\qquad
Q=\widetilde{\mathcal C}^{-t}
           \operatorname{diag}(-1,\widetilde G)
           \widetilde{\mathcal C}^{-1},\\
K[\widetilde y_1,\widetilde y_2]=K[v],\qquad
\deg_{\widetilde Y}\widetilde F=3,\qquad
\widetilde{\mathcal J}=\mathcal J/\Delta\in K^*,
\qquad \widetilde T_{2jk}=0 .
\end{gathered}
\tag{4}
\]
Derivatives of M add only tangential terms to the second derivatives
of b, so the radial matrix transforms as displayed. The expression
\(d\rho(y)+G(y,y)/2\) in90 is unchanged. Equivalently the
quadratic array there is \(\rho G-\nabla d\rho\), and its
cubic array is \(-\nabla G\); both are tensors for the actual
torsion-free moving-frame connection. Their actual potential and
closed linear coefficient therefore transform with y. Alternatively
one can repeat the differentiation90 using the commuting derivatives
(3). All its cancellations hold with coefficients in K.

The original differential volume transforms by
\(dH\wedge dw=\Delta\,ds\wedge dt\). This only multiplies
the actual Jacobian by a member of \(K^*\). We never replace
the generic algebra \(K[v,u]\) by a ring obtained by inverting
a v-dependent polynomial. The final tensor assertion follows from
\(D_w=V/V(w)\). Thus the full conditions used in119, not only
its metric identities, survive. Below suppress tildes and use
primes for derivatives in L with respect to H.

## 5. The ruled computation uses only these field properties

Assume Q has rank three. By (4), G is nondegenerate. With
\(b=p+wq\), one has \(G_{22}=0\), hence \(G_{12}\ne0\).
The exact coefficient computation of
[ruled119, Sections2--4](cubic-ruled-nondegenerate-exclusion-pass119.md)
can now be reconstructed over L. Initially set
\(\Omega_0=\det[p,p',q]\),
\(\Omega_1=\det[p,q',q]\), and
\(N=\det[q',p',q]\). Then
\(\Omega=\Omega_0+w\Omega_1\),
\(G_{12}=N/\Omega\),
\(C^1_{12}=\Omega_1/\Omega\), and
\(T_{212}=2G_{12}\Omega_1/\Omega=0\).
It follows that \(\Omega_1=0\) and
\(q'=ap+\beta q\), with \(a=G_{12}\in L^*\).
Writing \(p''=fp+cp'+hq\), the identity \(T_{211}=0\)
gives the remaining arrays:
\[
\begin{gathered}
c=a'/a-\beta,\qquad
G=\begin{pmatrix}f+2a\beta w-a^2w^2&a\\a&0\end{pmatrix},\\
C^1_{11}=c+aw,\quad C^1_{12}=C^1_{22}=0,
\quad C^2_{12}=\beta-aw,\quad C^2_{22}=0,\\
C^2_{11}=h+(\beta'+2\beta^2-f-a'\beta/a)w
                    -3a\beta w^2+a^2w^3,\\
T_{111}=\tau=-f'+2fc+2ah\in L^*,\qquad
T_{112}=T_{122}=T_{222}=0 .
\end{gathered}
\tag{5}
\]
Every coefficient a, beta, c, f, h lies in L. The assertion
\(\tau\ne0\) follows from the exact cubic degree: the
nonzero potential relation of degree at most three is a nonzero
scalar multiple of the irreducible cubic relation.

The elementary generic-coordinate lemma90 and the sole cubic
monomial \(q_0\tau Y_1^3/6\) force \(y_1\) to have generic
degree one. Indeed degree three would contribute uncancellable
degree nine; degree two would require the impossible generating
pair (2,3); a constant would leave only one generator and a linear
plane relation. Put \(v=y_1\), an affine change of the previous
generic variable over K. Then \(y_2\) has degree three.
The potential's sixth and fourth coefficients force
\(\mathsf B_{22}=\mathsf B_{12}=0\), so
\[
\begin{gathered}
y_2=R=r_0+r_1v+r_2v^2+r_3v^3
 =\frac{\zeta-L_1v-(q_0/2)\mathsf B_{11}v^2
                         -(q_0/6)\tau v^3}{L_2},\\
L_i=D_i(\chi+q_0\rho^2/2),\qquad
D_wL_1=D_HL_2,\qquad
L_2\ne0,\quad r_3=-q_0\tau/(6L_2)\ne0,\quad r_1=-L_1/L_2,\\
\frac{\mathcal J}{\Omega L_2}
=D_HR+R_vD_wR+(\beta-aw)R+C^2_{11}v
                  +(\beta-c-2aw)vR_v\in K^* .
\end{gathered}
\tag{6}
\]
The last equality is the actual determinant90 with the evaluated
gradient \(L_2(-R_v,1)\). No arbitrary choice of a formal cubic
in place of the actual potential is used.

Its fifth, fourth and third coefficients give, successively,
\[
\begin{gathered}
D_wr_3=0,\qquad D_wr_2=0,\qquad
r_3,L_2\in L,\qquad D_wr_1=-L_2'/L_2\in L,\\
0=r_3'+3r_3D_wr_1+(7\beta-3a'/a)r_3-7ar_3w .
\end{gathered}
\tag{7}
\]
The full constants equality (3) and the exactness in (6) justify
the middle assertions. All coefficients of the last affine
expression in w belong to L, while w is transcendental over L
and \(-7ar_3\ne0\). This is the contradiction. In particular
the proof never used polynomiality of p, q or w, nor a root of
an original polynomial base coordinate.

## 6. The surviving rank-three restriction and its determinant

Under rank Q equal to three, restriction to W cannot have rank
zero because \(Q(b,b)=-1\). Rank one has just been excluded,
so it has rank two. Nondegeneracy of Q identifies the orthogonal
complement of W with \(LQ^{-1}n\). Therefore
\[
\begin{gathered}
\operatorname{rank}(Q|W)=2,
\qquad n^tQ^{-1}n\ne0,\\
\frac{d}{dH}\det Q
 =\kappa\det Q\,n^tQ^{-1}n\ne0,
\qquad \det Q\notin\mathbb C .
\end{gathered}
\tag{8}
\]
Indeed the restriction is degenerate precisely when its
orthogonal line lies in W, equivalently when the displayed pairing
is zero. Jacobi's determinant identity and (1) give the derivative.
These are necessary constraints on the remaining rank-three
case, not its exclusion. The complementary lower-rank question
is logically separate.

## Verification and scope

This is a written field-transfer proof and reconstruction of the
actual potential and determinant. The finite ruled identities in
the retained [checker119](cubic_ruled_checks_pass119.py) are reused;
their earlier execution is not a new test of this transfer. They do
not establish relative algebraic closedness, the extension of
derivations, generic generation, or the original volume premise.
No all-order or source theorem is certified by a finite calculation,
and no new original-frame example is asserted.

[One additional transfer method120](cubic_rational_transfer_checks_pass120.py)
uses \(H=s/t\) and \(w=s^2+t^2\). Here
\(K=L(t)\), while \(t^2=w/(H^2+1)\) shows that K has degree
two over \(L(w)\): the right side has odd valuation at w zero
and cannot be a square in \(L(w)\). The method checks the
commuting dual derivatives and \(\Delta=2w/t^2\), then pulls
the four formulas of the principal-open control118 through this
map and checks their volume \(-2\Delta\). All four outputs
are fixed by \((s,t)\mapsto(-s,-t)\). They therefore cannot
recover s or t, even rationally. This is a field-transfer control,
not an original-coordinate example or a test of universal generation.

The author ran this one method in execution `8210e0`: it passed in
0.221 seconds of unittest time and 0.4670375 seconds of command
wall time, exit zero. The complete code read was `353db5`;
`a54683` checked its hash, one AST method, the proof's eight
sequential equation tags and clean trailing whitespace. The earlier
full proof read was `dfe39c`. This paragraph does not add coverage
to the retained119 execution.
