# A regular radial derivation supplies an actual low-degree slice

The actual determinant actions give a finite sufficient test for
low-degree slice selection. At any chosen invariant origin, regularity
of their generic radial combination is equivalent to two explicit
divisibility conditions in the actual four-ring. If those conditions
hold, a polynomial spectral projection extracts an actual affine
generic slice from any supplied slice, regardless of its degree.

This is a sufficient repair mechanism, not a proof that the
divisibilities hold. It is not a necessary condition for arbitrary
low-degree algebra generation. A change of generic origin must also
be checked in the actual ring.

## 1. The actual determinant fields and a chosen origin

Use the complete supplied independent degree-two frame of the
[generic bad-coordinate theorem](generic-bad-pair-pass44.md):
\[
B=\mathbb C[x_1,x_2,x_3,x_4]=A[s_*],\quad Es_*=1,\quad
C=\ker D\simeq\mathbb C^{[2]},\quad L=\operatorname{Frac}C,
\]
\[
B_L=L[x_3,x_4],\qquad A_L=L[j],\qquad j=gx_3-fx_4,
\quad E=f\partial_{x_3}+g\partial_{x_4}.
\tag{1}
\]
The actual good coordinates have the generic quadratic graph
\[
x_i=\mathcal Q_i(x_3,x_4),\qquad
\mathcal Q_i\in L[X,Y],\quad \deg\mathcal Q_i\le2
\quad(i=1,2).
\tag{2}
\]
The original four generators are actual polynomial coordinates,
not just a parametrization.

The already proved determinant LNDs satisfy
\[
0\ne\Delta\in C,\qquad
K_3=-\Delta\partial_{x_4},\qquad
K_4=\Delta\partial_{x_3}
\quad\text{on }B_L.
\tag{3}
\]
They are actual derivations of \(B\) killing \(C\).
Their construction from the original highest fields and the sign
conventions in (3) are those of the cited actual-frame theorem.

Let \(R\) be an invariant localization of \(C\), put
\(\mathcal B=B_R,\ \mathcal A=A_R\), and choose
\[
\eta=(\eta_3,\eta_4)\in R^2.
\]
Set \(\xi_3=x_3-\eta_3,\ \xi_4=x_4-\eta_4\).
These are still two generators over \(R\) together with
\(x_1,x_2\); they are not asserted to be a new ambient
polynomial coordinate frame over \(\mathbb C\).

In the fraction ring define
\[
\Theta_\eta=
\frac{(x_3-\eta_3)K_4-(x_4-\eta_4)K_3}{\Delta}.
\tag{4}
\]
Generically this is precisely
\[
\Theta_\eta=\xi_3\partial_{\xi_3}+
             \xi_4\partial_{\xi_4},\qquad
\Theta_\eta(L)=0.
\tag{5}
\]
It is a radial derivation, not an LND. No regularity after
division by \(\Delta\) has yet been assumed.

## 2. Exactly two actual divisibility tests

For the two good coordinate indices put
\[
N_i(\eta)=
(x_3-\eta_3)K_4(x_i)-(x_4-\eta_4)K_3(x_i)
\in\mathcal B,\qquad i=1,2.
\tag{6}
\]
Then
\[
\boxed{
\Theta_\eta(\mathcal B)\subseteq\mathcal B
\quad\Longleftrightarrow\quad
N_1(\eta),N_2(\eta)\in\Delta\mathcal B.
}
\tag{7}
\]
Indeed \(\Theta_\eta\) kills \(R\), and its two bad outputs
are already \(\xi_3,\xi_4\in\mathcal B\).
The remaining two outputs are exactly \(N_i(\eta)/\Delta\).
Checking a derivation on the four actual algebra generators is
both necessary and sufficient. Denominators inverted from \(R\)
cause no extra quotient-rule term because they are annihilated.

Condition (7) is divisibility by the full element \(\Delta\),
including all prime multiplicities. Divisibility by its radical,
pointwise vanishing, or regularity on the generic fiber would
not suffice. The numerators in (6) are obtained from actual
polynomial fields. They are not coefficients of a hypothetical
matrix pencil.

The allowed origin has a genuine restriction. One can formally
write (4) for \(\eta\in L^2\), but if it preserves \(\mathcal B\),
then
\[
\eta_3=x_3-\Theta_\eta(x_3),\quad
\eta_4=x_4-\Theta_\eta(x_4)\in\mathcal B\cap L=R.
\tag{8}
\]
For the last equality, an element of \(\mathcal B\cap L\)
first belongs to \(\ker E=\mathcal A\), and its intrinsic
\(D\)-derivative is zero, so it lies in \(R\).
Thus rational origins outside \(R^2\) cannot be used to
silently regularize the operator.

Regularity need not be independent of \(\eta\).
For a different center the operator changes by a rational
combination of \(K_3,K_4\) divided by \(\Delta\).
Each center must meet its own conditions (7).
For a supplied center these are two finite tests; no finite
search over all centers is asserted.

## 3. The same tests detect the homogeneous coefficient pieces

Expand the two generic quadratics about \(\eta\):
\[
\mathcal Q_i(\eta+\xi)=c_i+\ell_i(\xi)+q_i(\xi),
\tag{9}
\]
where \(c_i\in L\), \(\ell_i\) is homogeneous of degree one,
and \(q_i\) is homogeneous of degree two.
Under the generic radial operator,
\[
\begin{aligned}
c_i&=\tfrac12(\Theta_\eta-1)(\Theta_\eta-2)x_i,\\
\ell_i&=\Theta_\eta(2-\Theta_\eta)x_i,\\
q_i&=\tfrac12\Theta_\eta(\Theta_\eta-1)x_i.
\end{aligned}
\tag{10}
\]
Consequently (7) implies
\[
c_i\in R,\qquad \ell_i,q_i\in\mathcal B.
\tag{11}
\]
Conversely, if \(c_i\in R\) and \(\ell_i\in\mathcal B\),
then \(q_i=x_i-c_i-\ell_i\) is actual and
\[
\Theta_\eta(x_i)=2x_i-\ell_i-2c_i\in\mathcal B.
\]
Together with the bad outputs this proves (7).
Thus the two divisibility tests are equivalent to actual
membership of the constant and linear homogeneous pieces
of the two generic quadratics.

This does not require every individual generic coefficient
of the homogeneous quadratic part to belong to \(R\).
It requires membership of the displayed whole functions.
Nor can one assume (11) merely because the unseparated
quadratic \(x_i\) is actual.

## 4. An all-degree polynomial projection extracts the slice

Assume (7). Then \(\Theta_\eta\) is an actual derivation.
Every element of \(\mathcal B\subset L[\xi_3,\xi_4]\) has
finite nonnegative total degree. For any degree bound \(d\),
its degree-one component is the polynomial operator
\[
\Pi_{1,d}(\Theta_\eta)
=\prod_{\substack{0\le k\le d\\ k\ne1}}
  \frac{\Theta_\eta-k}{1-k},
\qquad d\ge1.
\tag{12}
\]
The denominators are nonzero complex integers, hence units.
Because \(\Theta_\eta\) preserves \(\mathcal B\), this
operator also preserves \(\mathcal B\).
Its eigenvalue is one on degree one and zero on every
other homogeneous degree from zero through \(d\).

Apply (12) to the actual supplied slice \(s_*\).
Choose \(d\) at least its generic total degree and put
\[
\sigma_1=\Pi_{1,d}(\Theta_\eta)s_*\in\mathcal B.
\]
The degree bound is finite even if large. If \(s_*\) is
given as a polynomial of degree \(M\) in the four actual
generators with coefficients in \(R\), one may take
\(d=2M\), by (2).

On the generic polynomial ring, \(E\) has homogeneous
degree minus one. Equivalently,
\[
[E,\Theta_\eta]=E,\qquad
E\,P(\Theta_\eta)=P(\Theta_\eta+1)E
\tag{13}
\]
for every scalar polynomial \(P\).
Since \(Es_*=1\), equations (12)--(13) give
\[
E\sigma_1=\Pi_{1,d}(1)\cdot1=1.
\tag{14}
\]
Thus the projected component cannot vanish.
It is homogeneous linear in \(\xi_3,\xi_4\), so it is an
actual affine generic slice in the original bad pair.

This argument removes the high-degree transverse part
using an actual operator. It does not subtract a generic
invariant whose membership in \(\mathcal A\) is unknown.
No integration of \(\Theta_\eta\) as an additive action,
assumed local nilpotence, or arbitrary coordinate inverse
is being used.

## 5. Consequences and the exact remaining obligation

The [actual affine-slice projection theorem](frame-filtration-generation-pass49.md)
now applies: projection of the two bad generators has
intrinsic degree at most one, and projection of the two
good quadratics has degree at most two. Since projection
is a surjective ring map from the actual four-generated
algebra, it follows that
\[
\boxed{
\text{the two conditions (7) imply }
\mathcal A=R[F_2].
}
\tag{15}
\]
This is generation, not only a parametrization.
In the actual quotient setting, the established conic
and fiber-dimension argument therefore excludes a
second-image obstruction point whenever (7) holds.

In particular, at any actual second-image point with
\(R=C_{\mathfrak m}\), every center \(\eta\in R^2\)
must fail at least one of the two divisibilities in (7).
That is a necessary obstruction to this radial repair,
not an existence assertion for such points.

The finite test supplies one concrete next proof
obligation: control the full \(\Delta\)-divisibility of
the two actual numerators (6), possibly at a suitable
actual invariant center. The original quadratic graph
only establishes the rational expression (4); it does
not perform this division. Neither faithful flatness
nor the unit ideal of the original \(E\)-velocities has
been proved here to imply (7).

No converse from low-degree algebra generation to
regularity of \(\Theta_\eta\) is asserted.
Failure of a radial test does not exclude another
slice-selection mechanism or a different generating set.

## 6. Check against the separate weaker countercontrol

The [quadratic intermediate-algebra control](quadratic-slice-selection-boundary-pass55.md)
uses
\[
j=bX-aY,\quad Z=(j^2-b)/a,\quad
W=(1-j^2+b)/b,
\]
with quadratic generators \(Q_1=Z+X^2,\ Q_2=W+Y^2\).
Its radial operator at the zero origin has
\[
\Theta_0(Q_1)=2Q_1+\frac{2b}{a},\qquad
\Theta_0(Q_2)=2Q_2-\frac{2(1+b)}{b}.
\tag{16}
\]
For example \(b/a\) is not in that actual intermediate
algebra: at the height-one base prime \((a)\), the
monic quadratic chart has a nonempty fiber and \(b\)
is a unit, while \(a\) remains a nonunit.
Membership of \(b/a\) would make \(a\) invertible.
Thus (16) does not define a regular radial derivation.

This agrees with the independently proved minimum
generic slice degree three in that example.
It illustrates the need for actual homogeneous-piece
membership rather than a polynomial generic graph.
The countercontrol misses the closed base fiber and
does not satisfy the faithful actual-frame hypotheses;
it cannot refute automatic radial descent under those
stronger premises.

The criterion and projection above are proved by
explicit algebra, with no new numerical suite or
historical novelty assertion. All files from pass54
and earlier remain unchanged.

