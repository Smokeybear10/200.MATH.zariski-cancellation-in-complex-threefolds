# Zero first normal action forces a quadratic conormal row

For a collapsed double component in the actual quadratic frame, zero
first normal action forces the quotient conormal row to have polynomial
degree at most two in the actual component parameter. Its transverse
quadratic coefficient is a nonzero constant. The weighted leading
derivation is a translation with an invariant linear normal factor.

This does not make the full derivation a translation near the component
or exclude the component. In particular, vanishing of the square of
the leading derivation on the component parameter is not the identity
\(N^2c=0\) in A. The intrinsic control below makes that distinction exact.

## 1. Actual hypotheses and the constant column

Retain the supplied nonconical quadratic frame through
[source-balance97](quadratic-saturated-source-balance-pass97.md).
Let C be a collapsed multiplicity-two fixed component, with prime
\(\mathfrak q\). It may be the whole reduced fiber or the double
component of a (2,1) fiber. The actual centered generators from
[conormal-layer93](nonconical-collapsed-conormal-layer-pass93.md) satisfy
\[
\begin{gathered}
A/\mathfrak q=\mathbb C[\bar c],\qquad
\mathfrak q=(F,G)A,\qquad
\mathfrak qB=(X,Y),\\
F=X-uEX,\qquad G=Y-uEY,\qquad N^3F=N^3G=0,\\
\boxed{\quad N(\mathfrak q)\subset\mathfrak q^2.\quad}
\end{gathered}
\tag{1}
\]
The last line is the extra hypothesis of this note. Because N kills
the reduced component, it is equivalent to zero induced action on
\(\mathfrak q/\mathfrak q^2\). It does not say that \(Nc\) belongs
to \(\mathfrak q^2\).

The local calculation93 identifies this sector with a constant quotient
column direction. A constant linear base change therefore gives actual
centered base parameters x,f with
\[
\begin{gathered}
\mathfrak m=(x,f)S,\qquad
x\equiv p(c)F+q(c)G\pmod{\mathfrak q^2},\qquad
f\in\mathfrak q^2,\\
p,q\in\mathbb C[c],\qquad (p,q)\mathbb C[c]=\mathbb C[c].
\end{gathered}
\tag{2}
\]
Indeed the generic ratio of the two column entries has derivative zero
in \(\mathbb C(c)\), hence is a complex constant. The generic identity
extends to the polynomial conormal matrix on the whole component.
The everywhere-rank theorem95 then says p and q never vanish together,
which is exactly the displayed unit-ideal condition. No polynomial
matrix depending on c has been applied to the actual generators.

## 2. A global transverse coefficient, including every chart

Since F,G are a regular sequence defining the smooth component,
the quadratic normal class of f has a unique expression
\[
\begin{gathered}
f\equiv Q_2(c;F,G)
 =a_{20}(c)F^2+a_{11}(c)FG+a_{02}(c)G^2
 \pmod{\mathfrak q^3},\\
a_{ij}\in\mathbb C[c],\qquad
A(c):=Q_2(c;-q(c),p(c)),\\
\boxed{\quad A(c)\in\mathbb C^*.\quad}
\end{gathered}
\tag{3}
\]
Here the coefficients use the specified polynomial lift c. The
regular-sequence associated graded ring is
\(\mathbb C[c][\bar F,\bar G]\), so the definition is global.

We prove the final assertion at every complex value \(c_0\), not just
where p is nonzero. The componentwise finite-freeness theorem95 gives
its entire whole-fiber thickening as a free module of rank two over
the actual subring \(\mathbb C[c]\). Other reduced components are
disjoint. Consequently
\(\operatorname{length} A_P/(x,f,c-c_0)=2\) at the point P of C with
parameter \(c_0\). The local surface \(A_P/(c-c_0)\) is regular,
with normal parameters F,G, since c restricts to a smooth curve
coordinate.

The linear part of x on that surface is the nonzero row
\((p(c_0),q(c_0))\). Quotienting by x leaves a regular local
one-dimensional ring. Its f-equation must have order exactly two.
Its quadratic coefficient is the restriction of \(Q_2(c_0)\) to
the kernel of that row, spanned by
\((-q(c_0),p(c_0))\). Therefore \(A(c_0)\ne0\).
If \(p(c_0)=0\), then \(q(c_0)\ne0\); solving for G instead of F
gives precisely the same test. Nonlinear terms of x cannot change
this quadratic coefficient, because f has no linear normal term.
Thus A has no complex zero and is a nonzero constant.

This argument uses the whole length-two thickening and the actual
parameter c. Generic multiplicity alone would not prove that its
transverse coefficient has no zero at a special point.

## 3. The exact weighted leading operator

After exchanging F and G by a constant matrix if needed, assume
p is not identically zero. At the generic point of C put y=G.
Then x,y are regular parameters over the actual coefficient field
\(\mathbb C(c)\). In the coefficient-compatible completion, give x
weight two, y weight one, and the coefficient field weight zero.
The actual local Jacobian and volume calculation gives
\[
\begin{gathered}
\widehat{A_{\mathfrak q}}=\mathbb C(c)[[x,y]],\qquad
f=a(c)y^2+f_{>2},\qquad a(c)=A/p(c)^2,\\
N=\epsilon(f_y\partial_c-f_c\partial_y),\qquad Nx=0,\qquad
\epsilon_0=\nu p(c),\quad \nu\in\mathbb C^*,\\
D_*=-\nu p a' y^2\partial_y+2\nu p a y\partial_c,\qquad
N(\mathcal F_{\ge j})\subset\mathcal F_{\ge j+1}.
\end{gathered}
\tag{4}
\]
The coefficient \(a=A/p^2\) follows by solving the linear equation
\(pF+qG=0\) in the quadratic normal form. The prime denotes
differentiation in c.

For the unit factor, the ratio of \(dF\wedge dG\wedge dc\) to the
actual threefold volume restricts to a nowhere-zero polynomial
on the entire affine component, hence to a complex constant.
Changing the differential coordinates from F,G,c to x,G,c
multiplies the relevant Jacobian factor by p. This is the same
actual-volume argument as column94, and does not require that
the quotient column varies. No rational unit is silently
renormalized to a constant.

The strict weight separation in (4) is the retained weighted94
construction. In particular all higher terms in f and epsilon
produce strictly higher operator degree. Set \(v=y/p(c)\) in
the weighted coefficient ring. Direct differentiation gives
\[
\boxed{\quad
D_*v=0,\qquad D_*x=0,\qquad D_*c=2\nu A v,\qquad D_*^2c=0.
\quad}
\tag{5}
\]
Thus, in x,v,c, the leading operator is \(2\nu A v\partial_c\).
It is not being asserted to be an LND on the coefficient field
or on a completed local ring. The displayed identities suffice.

## 4. The two actual cubic identities bound the row

The weight-one parts of the actual centers are
\(F_*=-q(c)v\) and \(G_*=p(c)v\). Every remaining term has
weight at least two. Since the leading operator has degree one,
the weight-four parts of \(N^3F=N^3G=0\) give
\[
\begin{gathered}
D_*^3F_*=-(2\nu A)^3q'''(c)v^4=0,\qquad
D_*^3G_*=(2\nu A)^3p'''(c)v^4=0,\\
\boxed{\quad \deg p\le2,\qquad \deg q\le2.\quad}
\end{gathered}
\tag{6}
\]
If q is identically zero its equation is trivial; p is not zero
in the chosen chart. The roles can be exchanged. The coefficient
\(2\nu A\) is nonzero. Thus no higher weighted term can cancel
the coefficient enforcing the stated degree bounds.

For completeness, the resulting unimodular row spans have an
elementary finite classification. Up to constant row changes and
an affine change of c, their polynomial span is one of
\[
\operatorname{span}\{1\},\qquad
\operatorname{span}\{1,c\},\qquad
\operatorname{span}\{1,c^2\},\qquad
\operatorname{span}\{c,c^2+1\}.
\tag{7}
\]
If the span has dimension one, unimodularity forces its generator
to be constant. Otherwise cancel the leading term to obtain a
basis of degrees n<m<=2. For n=0, an affine change of c and a
constant basis change give the middle two cases. For n=1,m=2,
normalize the first basis element to t. Subtracting a multiple
of t from the second gives \(a t^2+b\), with both a and b nonzero:
b=0 would violate coprimality. Rescaling t over C gives the last
case. This is a classification of conormal data, not of actions.

The actual identity \(N^5c=0\) is available in the supplied frame,
but is not needed for (3)--(7). In particular (5) neither upgrades
to \(N^2c=0\) in A nor makes F,G,x or c ambient coordinates.

## 5. Intrinsic boundary and finite verification

On the polynomial ring \(A_0=\mathbb C[x,y,c]\), set
\[
\begin{gathered}
N_0=-x^2\partial_y+2y\partial_c,\qquad
f_0=y^2+x^2c,\qquad \ker N_0=\mathbb C[x,f_0],\\
\mathfrak q_0=(x,y),\qquad
A_0/(x,f_0)=\mathbb C[y,c]/(y^2),\qquad
N_0(\mathfrak q_0)\subset\mathfrak q_0^2,\\
N_0^3x=N_0^3y=N_0^5c=0,\qquad
N_0c=2y\notin\mathfrak q_0^2,\qquad
N_0^2c=-2x^2\ne0.
\end{gathered}
\tag{8}
\]
This is a primitive triangular LND: the coefficient gcd is one.
After inverting x its invariant coordinate is f0 and its moving
coordinate is y. Kernel descent follows from injectivity of
\(\mathbb C[f_0]\to\mathbb C[y]\), \(f_0\mapsto y^2\), modulo x,
which cancels denominators in x successively. The origin double
fiber has a constant conormal row (1,0), constant transverse
coefficient one, and the constant original polynomial volume.
With weights two on x and one on y its leading operator is
\(2y\partial_c\), whose square kills c, although the full square
in (8) does not.

These intrinsic conditions do not provide the supplied original
four-coordinate nonconical frame or identify this chosen invariant
plane with an actual highest-adjoint kernel. Therefore this is
not a counterexample to the restricted recognition problem.
It specifically blocks a promotion from (5) to a full-ring
square-zero identity or an exclusion from the displayed local
conditions alone.

The [standalone checker](quadratic_zero_normal_checks_pass98.py)
has one method. It checks the exact weighted formulas for general
quadratic row polynomials, a cubic-row negative, a chart where
p vanishes but the quadratic transverse coefficient remains a
unit, and the intrinsic control (8). These finite symbolic
controls do not verify all actual-frame, completion or geometric
hypotheses.

The first author execution of the standalone checker passed its
one method in 0.080 seconds, exit zero, with complete output in
chunk 494882 (wall time 0.562201208 seconds). No assertion failed.
This is a finite symbolic run, not a full regression or a formal
verification of the written theorem.

The full retained conormal93, double-normal93, weighted94,
column94, curvilinear93 and whole-component finite-freeness95
proofs were read for this argument. No fresh primary-source
proof is claimed. All files through97 remain unchanged.
