# The remaining volume coefficients bound the relative plane relation by degree three

In the actual nonconical constant-acceleration frame, the relative
two-generator ring has a defining equation of degree at most three
in its two relative variables. Over the function field of the invariant
plane, a linear combination of these generators is a polynomial
coordinate of the generic fiber.

Both conclusions use the original coordinate volume, beyond generic
birationality. Neither descends that generic coordinate over the whole
invariant plane or proves cancellation.

## 1. Moving-frame notation

Retain the complete actual hypotheses and conclusions of
[quadratic-potential90](nonconical-quadratic-potential-pass90.md).
Write \(S=\mathbb C[s_1,s_2]\), \(S^\circ=S[1/\Omega]\), and
\(K=\operatorname{Frac}(S)\). Subscripts i,j,k below range over 1,2
and mean base derivatives when attached to base functions.
There are actual elements \(y_1,y_2\in A_\Omega\) such that
\[
\begin{gathered}
x_{\rm tr}=b(u+\rho)+b_{s_1}y_1+b_{s_2}y_2,\qquad
z=\chi-q\Psi+\frac q2u^2,\qquad \rho,\chi\in S^\circ,\\
\Psi=\sum_i\rho_i y_i+\frac12\sum_{i,j}G_{ij}y_i y_j,\qquad
A_\Omega=R_\Omega=S^\circ[y_1,y_2],\\
b_{s_i s_j}=G_{ij}b+\sum_{k=1}^2 C^k_{ij}b_{s_k},
\qquad G_{ij},C^k_{ij}\in S^\circ .
\end{gathered}
\tag{1}
\]
Here \(G_{ij}=\Gamma^0_{ij}\) in the cited note. All G and C arrays
are symmetric in i,j. Partial derivatives of elements of \(S^\circ\)
again belong to \(S^\circ\), even though their denominators can
increase. These are actual base derivatives, not derivatives through
a newly chosen algebraic coefficient field.

Temporarily use formal variables \(Y=(Y_1,Y_2)\), distinct from their
images y in \(A_\Omega\), and set
\[
\begin{gathered}
g_i(s,Y)=\rho_i+\sum_jG_{ij}Y_j,\qquad
\Psi(s,Y)=\sum_i\rho_iY_i+\frac12\sum_{i,j}G_{ij}Y_iY_j,\\
Z_i(s,Y)=\chi_i-q\,\partial_{s_i}\Psi(s,Y)
  +q\rho\,g_i(s,Y)+q\sum_{j,k}g_j(s,Y)C^j_{ik}Y_k .
\end{gathered}
\tag{2}
\]
The derivative in the second line holds Y fixed. In particular each
\(Z_i\) has Y-degree at most two.

## 2. A symmetric cubic potential

Equality of mixed third derivatives of b, followed by taking the
b-component in the same moving basis, gives
\[
\partial_iG_{jk}-\partial_jG_{ik}
=\sum_l\bigl(G_{jl}C^l_{ik}-G_{il}C^l_{jk}\bigr).
\tag{3}
\]
For example, the b-component of \(\partial_i(b_{s_j s_k})\) is
\(\partial_iG_{jk}+\sum_l C^l_{jk}G_{il}\).
Comparing with \(\partial_j(b_{s_i s_k})\) proves (3), including
its signs.

Define arrays over \(S^\circ\) by
\[
\begin{gathered}
B_{ij}=\rho G_{ij}-\rho_{ij}+\sum_l\rho_l C^l_{ij},\\
T_{ijk}=-\partial_iG_{jk}
  +\sum_l\bigl(G_{lj}C^l_{ik}+G_{lk}C^l_{ij}\bigr),\\
\Phi(s,Y)=
\sum_i(\chi_i+q\rho\rho_i)Y_i
  +\frac q2\sum_{i,j}B_{ij}Y_iY_j
  +\frac q6\sum_{i,j,k}T_{ijk}Y_iY_jY_k .
\end{gathered}
\tag{4}
\]
The array B is symmetric. T is symmetric in j,k directly; its
symmetry in i,j follows from (3) and \(C^l_{ij}=C^l_{ji}\).
Thus T is fully symmetric. Expanding (2) by Y-degree and
differentiating (4) now gives the exact identity
\(\partial_{Y_i}\Phi=Z_i\).
In particular the polynomial one-form \(Z_1dY_1+Z_2dY_2\)
is closed for a reason supplied by the actual derivatives of b.

## 3. The linear volume coefficient makes the cubic base-valued

Choose an intrinsic local slice \(v\) only for this computation,
so \(A_{\Omega f}=S_{\Omega f}[v]\) and \(Wv=1\) for some
nonzero \(f\in S\). Put \(\mathcal C=[b,b_{s_1},b_{s_2}]\)
and let \(\eta=\mathcal C^{-1}dx_{\rm tr}\) be a column of
three one-forms, indexed 0,1,2.
Differentiating (1) and using (2) yields
\[
\begin{gathered}
\eta_0=du+\sum_i g_i(s,y)\,ds_i,\\
\eta_j=dy_j+(u+\rho)\,ds_j+
 \sum_{i,k}C^j_{ik}y_k\,ds_i\quad(j=1,2),\\
dz-qu\,\eta_0+q\sum_j g_j(s,y)\eta_j
=\sum_i Z_i(s,y)\,ds_i .
\end{gathered}
\tag{5}
\]
All cancellations in the last line can be checked with Y held fixed
first: \(d\Psi=\sum_i(\partial_i\Psi)ds_i+\sum_jg_jdy_j\).
The terms involving \(u g_i\) cancel, leaving exactly (2).

The determinant \(\mathcal J\) of the original four coordinates
in the variable order \((u,s_1,s_2,v)\) is a unit in
\(S_{\Omega f}\), by the actual differential-basis argument in
the cited proof. Apply the row operations (5) after factoring
out \(\det\mathcal C=\Omega\). With
\[
K_{ji}=\rho\,\delta_{ji}+(y_j)_{s_i}
             +\sum_k C^j_{ik}y_k
\]
this gives
\[
\frac{\mathcal J}{\Omega}
=\det\begin{pmatrix}
u+K_{11}&K_{12}&(y_1)_v\\
K_{21}&u+K_{22}&(y_2)_v\\
Z_1(s,y)&Z_2(s,y)&0
\end{pmatrix},\qquad
[u]\frac{\mathcal J}{\Omega}
=-Z_1(s,y)(y_1)_v-Z_2(s,y)(y_2)_v=0 .
\tag{6}
\]
The sign follows by expansion along the final row. Since
\(\Phi_{Y_i}=Z_i\), (6) says \(W(\Phi(s,y))=0\).
The element already lies in \(A_\Omega\). Its actual W-kernel is
\(S^\circ\), so the auxiliary local-slice factor disappears:
\(\Phi(s,y)=\zeta\in S^\circ\).

The formal polynomial \(\Phi(s,Y)-\zeta\) is nonzero. Otherwise
both formal \(Z_i\) would be zero, making the final row in (6)
zero and contradicting the unit \(\mathcal J\). The same argument
shows that the two evaluated \(Z_i(s,y)\) cannot both vanish as
elements of \(A_\Omega\). No assertion that their ideal is a unit
is needed for this degree argument.

## 4. Degree of the defining equation, locally and globally

The map \(S^\circ[Y_1,Y_2]\to A_\Omega\) is surjective and has
a height-one prime kernel. The source is a UFD, so this kernel
is generated by an irreducible polynomial F. The nonzero relation
just obtained is a multiple of F. Consequently
\[
\Phi(s,y)=\zeta\in S^\circ,\qquad
0\ne\Phi(s,Y)-\zeta\in(F),\qquad
1\le\deg_Y F\le3 .
\tag{7}
\]
Total Y-degree is additive for nonzero products over a domain,
which justifies the final inequality.

This degree bound also holds for the original relative ring
\(R=S[A_1,A_2]\). Its kernel in \(S[T_1,T_2]\) is a height-one
prime: \(R_\Omega=A_\Omega\) has transcendence degree three.
It therefore has an irreducible defining polynomial \(F_0\).
Localization at \(\Omega\) cannot change its total T-degree.

The two rows defining \((y_1,y_2)\) from the centered vector a
and the two rows defining \((A_1,A_2)\) from a are both bases
over \(S^\circ\) of the rank-two module of rows annihilating b.
Thus these two pairs of generators differ by a
\(\operatorname{GL}_2(S^\circ)\) linear transformation. Applying
it to formal variables preserves total relative degree.
It follows that \(\deg_T F_0=\deg_Y F\le3\), even though R
has not been identified with A along \(\Omega=0\).

## 5. An elementary generic linear-coordinate consequence

Here is the elementary plane-curve fact needed for the consequence.
Let K have characteristic zero and suppose
\(K[f(v),g(v)]=K[v]\), with irreducible plane relation of degree
d at most three. Then a K-linear combination of f and g has
v-degree one.

First d equals \(\max(\deg f,\deg g)\). One direct verification is
to extend to an algebraic closure and intersect the parametrized
curve with a generic affine line. Pullback gives a polynomial of
that maximum degree with that many distinct roots. The equality
of coordinate rings makes the parametrization an isomorphism,
so these are exactly the distinct affine intersection points.
A generic line avoids the finitely many points at infinity of
the projective closure, and its intersection number is d.
This argument does not assume an arbitrary birational
parametrization is injective.

If f and g have the same positive degree, subtract a K-multiple
to reduce one degree. Unless a linear polynomial is already
obtained, the only possible nonconstant unequal degree pair with
maximum at most three is (2,3). Constant plus one polynomial of
degree at least two cannot generate \(K[v]\).

For the pair (2,3), a K-affine change of v, scaling and adding
constants, and subtraction of a multiple of the quadratic from
the cubic put the two generators in the form
\[
w^2,\qquad w(a w^2+b),\qquad a\in K^*,\ b\in K .
\tag{8}
\]
If \(b=0\), both derivatives vanish at zero. This is incompatible
with an identity \(w=H(w^2,aw^3)\), by differentiation.
If \(b\ne0\), over an algebraic closure choose
\(w_0^2=-b/a\). The distinct points \(w_0,-w_0\) have equal
images under both generators, contradicting the same
polynomial recovery identity. Thus (2,3) cannot occur.

In the actual setting \(A_K=K[v]\) by an intrinsic local slice,
and \(A_K=K[y_1,y_2]=K[A_1,A_2]\) by (1).
The elementary fact therefore supplies a K-linear combination
of \(A_1,A_2\) generating \(A_K\). Clearing its finitely many
base denominators gives an element of R which still generates
the generic polynomial ring over K. This does not give a
unimodular pair of coefficients over S or a global coordinate.

## 6. Remaining scope

The bounded relative degree and the generic linear coordinate are
stronger than an arbitrary plane embedding of the generic fiber.
They do not control the whole fibers over the zero divisor of
\(\Omega\), force geometric integrality of base divisor fibers,
or produce a global S-retraction. Even a smooth factorial
two-generator ring with a free intrinsic additive action can
have a nontrivial residue-field extension on a base divisor.

Root derived the closed one-form, cubic potential, degree bound,
and elementary generic-coordinate argument from the retained
actual volume calculation. General independently reached the
same residual rows \(Z_i\) while studying the linear and constant
coefficients. This note is a written derivation pending its
separate full-file reconstruction, not a numerical or formal
proof certificate or a novelty claim. Pass89 and earlier files
are unchanged.
