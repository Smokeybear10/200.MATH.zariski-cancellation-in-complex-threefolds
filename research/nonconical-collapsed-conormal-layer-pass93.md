# The first normal layer of a collapsed rank-one fixed component

In the supplied nonconical quadratic frame, a collapsed rank-one
fixed component has a globally two-generated ideal in A. Its two
centered generators have N-degree at most two. In the original
affine-plane coordinates, some nonzero constant normal direction
has E-speed vanishing to second order along the plane.

This is an actual-coordinate constraint. It does not make that
normal coordinate invariant or exclude the fixed component.

## 1. The retained actual plane and its centered generators

Use the actual quadratic case of
[frontier92](nonconical-fixed-fiber-frontier-pass92.md), with
canonical \(u=Ez/q\), \(q\in\mathbb C^*\), and
\(B=A[u]=\mathbb C[x_1,x_2,x_3,z]\). Let
\(\mathfrak q\subset A\) be the generic prime of a fixed
component over the closed base point \(\mathfrak m\subset
S=\mathbb C[s_1,s_2]\). Assume both relative generators
\(\bar A_1,\bar A_2\) are constants on this component and that
the quotient differential has generic rank one there.

The [actual plane proof92](nonconical-collapsed-component-plane-pass92.md)
gives affine-linear good coordinates X,Y,W with
\[
\begin{gathered}
\mathfrak P=\mathfrak qB=(X,Y),\qquad
B/\mathfrak P=\mathbb C[W,z],\qquad \bar u=W,\\
A/\mathfrak q=\mathbb C[\bar c],\qquad
\bar E=E_0=\partial_W+qW\partial_z,\qquad
\bar h=\eta\in\mathbb C,\\
t=z-\frac q2W^2,\qquad \bar c=t+\frac q2\eta^2.
\end{gathered}
\tag{1}
\]
The letters X,Y,W in this note are actual affine-linear
combinations of the three original good coordinates. They are
not the two formal variables of the relative equation.

Evaluation at canonical \(u=0\) is the retraction
\(\pi:B=A[u]\to A\). For a good affine-linear coordinate,
its E-degree is at most one, so
\(\pi(X)=X-uEX\), and likewise for Y. Applying this retraction
to the exact ideal equality in (1) proves
\[
\begin{gathered}
F=X-uEX,\qquad G=Y-uEY,\qquad
\boxed{\ \mathfrak q=(F,G)A\ },\\
NF=NX,\qquad NG=NY,\qquad
N^3F=N^3G=0 .
\end{gathered}
\tag{2}
\]
Indeed every element of \(\mathfrak q\), expressed using X and Y
in B, remains that same element after applying \(\pi\), which
gives the required ideal inclusion in A. The reverse inclusion
is immediate. This is a global ideal equality, not just a
statement at the generic point.

The identities for N use \(Nu=0\) and \(N(EX)=N(EY)=0\),
since the good speeds belong to S. The last two identities
come from the actual generic degree bound of92:
every centered good coordinate has degree at most two in
\(A_K=K[v]\), and \(N|_{A_K}\) is a constant multiple of
\(\partial_v\). Injection into that localization gives the
identities in A. No claim that F or G is an ambient coordinate
is needed. Their ideal has height two, so it is a complete
intersection in the regular ring A.

## 2. Exact first-layer equations

Write \(s^0=(s_1(\mathfrak m),s_2(\mathfrak m))^t\), and
\(n=(X,Y)^t\). There is a unique polynomial matrix C with
\[
s-s^0\equiv C(W,z)n\pmod{\mathfrak P^2},
\qquad C\in\operatorname{Mat}_2(\mathbb C[W,z]),
\qquad \operatorname{rank}_{\mathbb C(W,z)} C=1.
\tag{3}
\]
The rank is the assumed ambient quotient rank: derivatives in
the two tangent directions vanish modulo \(\mathfrak P\),
and C consists of the two remaining derivative columns.

Let \(\Xi\) be the constant two-by-three matrix defining the
linear parts of X and Y in the original good coordinates.
The good-speed row b belongs to S, and \(\Xi b(\mathfrak m)=0\).
Taylor expansion at the closed base point gives
\[
\begin{gathered}
B_0=\Xi[\,b_{s_1}(\mathfrak m),b_{s_2}(\mathfrak m)\,],
\qquad En\equiv Mn\pmod{\mathfrak P^2},
\qquad M=B_0C,\\
\operatorname{rank}B_0\le1,\qquad
\operatorname{tr}M=0,\qquad M^2=0,\qquad CM=0.
\end{gathered}
\tag{4}
\]
The constant matrix \(B_0\) is distinct from the polynomial
matrix C. Its rank bound follows from
\(\Omega(\mathfrak m)=\det[b,b_{s_1},b_{s_2}](\mathfrak m)=0\):
the quotient of the good three-space by the nonzero vector
\(b(\mathfrak m)\) is identified by \(\Xi\) with the normal
two-space.

For the trace identity, take the actual velocity Jacobian in
X,Y,W,z. Its normal diagonal block modulo \(\mathfrak P\) is
M. The W-speed is one modulo \(\mathfrak P\), while the last
speed is \(qu\) and \(u_z=0\) modulo \(\mathfrak P\).
Thus the remaining two diagonal entries are zero there.
The original nilpotence gives zero trace, proving
\(\operatorname{tr}M=0\).

A rank-at-most-one two-by-two matrix satisfies
\(M^2=(\operatorname{tr}M)M\). Also, over the fraction field,
factor the rank-one matrix \(C=\ell\gamma\), with a column
\(\ell\) and row \(\gamma\). Then
\(CB_0C=(\gamma B_0\ell)C=(\operatorname{tr}M)C\).
These identities prove the last assertions of (4) over the
polynomial ring as well.

Applying \(E(s)=0\) to (3), and using that E preserves
\(\mathfrak P\), yields \(E_0C+CM=0\). Consequently
\[
E_0C=0,\qquad C\in\operatorname{Mat}_2(\mathbb C[t]).
\tag{5}
\]
The kernel calculation is elementary: \(W,t\) are coordinates
on the plane, and \(E_0=\partial_W\) in these coordinates.
The parameter t differs from the actual component coordinate
\(\bar c\) only by the constant in (1).

## 3. A constant affine normal direction

If M is zero, both EX and EY already belong to
\(\mathfrak P^2\). Suppose instead that M is nonzero over
\(\mathbb C(t)\). Then \(B_0\) has rank one and
\(\operatorname{im}M=\operatorname{im}B_0\) is a constant
line. Since \(M^2=0\), this line is also \(\ker M\).
Both C and M have rank one and \(\ker C\subset\ker M\),
so these kernels agree. Choose a nonzero constant row
\(\gamma_0\) annihilating this line. It follows that
\(\gamma_0M=0\). We have proved
\[
\boxed{\quad
\text{There is a nonzero affine-linear good normal }L
\text{ with }L\in\mathfrak P,\quad EL\in\mathfrak P^2.
\quad}
\tag{6}
\]
Its invariant center \(f=L-uEL\) belongs to \(\mathfrak q\),
is equal to L modulo \(\mathfrak P^2\), and satisfies
\(N^3f=0\). This does not assert \(EL=0\).

There is a further conclusion when \(\operatorname{rank}B_0=1\).
If M is nonzero, the constant kernel just proved puts
\(C=\ell(t)\gamma_0\), with a constant row.
If M is zero, its columns lie in the constant line
\(\ker B_0\), so \(C=\ell_0\gamma(t)\), with a constant column.
These two alternatives imply respectively
\[
\begin{array}{ll}
M\ne0:
&Nf\in\mathfrak q^2
 \text{ for } f=L-uEL \text{ from (6)},\\
M=0,\ \operatorname{rank}B_0=1:
&NF,NG\in\mathfrak q^2 .
\end{array}
\tag{7}
\]
Here is the full local calculation. The component and A are
smooth, and (2) is its complete-intersection ideal.
Therefore \(dF,dG,dc\) form a local differential basis at
every point of the component. In that basis N is a unit
multiple of the Jacobian derivation of \(s_1,s_2\), by the
actual volume argument of fixed-scheme92.
Moreover \((F,G)^t\equiv(I-uM)n\) modulo \(\mathfrak P^2\),
and \(CM=0\). Thus the matrix in (3), with the constant
translation from t to \(\bar c\), is also the first
coefficient matrix in F,G on A.

In the constant-row case, make a constant change so f is the
first normal generator. Then \(s_i-s_i^0\equiv\ell_i(\bar c)f\)
modulo \(\mathfrak q^2\). The determinant computing Nf uses
the other normal derivative, which has zero constant term,
and a c-derivative, which has order at least one. Hence it
has order at least two. In the constant-column case, the
two first rows and their c-derivatives are all proportional
to the same constant column \(\ell_0\); their order-one
determinants cancel, proving both assertions. These local
memberships at all component points give the global ideal
memberships in (7).

When \(B_0=0\), equation (6) still holds, but the constant-row
or constant-column assertion need not follow from the
first-layer algebra. No \(Nf\in\mathfrak q^2\) conclusion is
claimed in that subcase.

## 4. Exact limits of the first layer

The retained intrinsic Weitzenbock action already distinguishes
second-order vanishing from invariance. In polynomial coordinates
p,y,c, set \(D=p\partial_y-2y\partial_c\), with kernel
\(\mathbb C[p,pc+y^2]\) and fixed prime \((p,y)\). Then
\[
\begin{gathered}
f_0=p+y^2,\qquad Df_0=2py\in(p,y)^2,\qquad
D^2f_0=2p^2\ne0,\qquad D^3f_0=0;\\
X_0=p-cy,\quad Y_0=y,\quad
C_0(c)=
\begin{pmatrix}1&c\\c&c^2\end{pmatrix},\qquad
D^3X_0=6p^2\ne0.
\end{gathered}
\tag{8}
\]
The second line uses actual polynomial coordinates X0,Y0,c on
this comparison ring, with \(p=X_0+cY_0\). Its quotient
conormal matrix has both projective directions varying.
For a constant nonzero pair \((a,b)\),
\(D(aX_0+bY_0)\equiv(b-ac)(X_0+cY_0)\) modulo
\((X_0,Y_0)^2\), so no constant normal combination is killed
to second order. But \(X_0\) has D-degree three, not the
degree-at-most-two required of the actual centered generators
in (2). This is not a counterexample to a possible stronger
quadratic theorem.

Both comparisons are intrinsic polynomial controls, not
realizations of the supplied original nonconical frame, its
chosen S, or the matrix \(B_0\). They show exactly which
shortcuts are not justified by their displayed conditions.
The remaining question is whether the complete original action
and the quadratic degree bound rule out the \(B_0=0\) variation
or the rank-one fixed component itself.

No full filtration hypothesis from pass54 has been inserted.
No global invariant coordinate, recognition result, numerical
method, external source theorem, or change to pass92 and earlier
is claimed here.

The subsequent [double-fiber normal-order proof93](nonconical-double-fiber-normal-order-pass93.md)
removes the \(B_0=0\) exception when the whole-fiber multiplicity
is exactly two. It uses the actual identities \(N^3F=N^3G=0\)
one normal order further to force a constant row or column
direction and obtain \(Nf\in\mathfrak q^2\) for a centered good
normal generator. The first-layer argument above remains valid
at higher multiplicities, where that additional conclusion has
not been proved. Even the multiplicity-two conclusion does not
make the generator invariant or exclude the component.
