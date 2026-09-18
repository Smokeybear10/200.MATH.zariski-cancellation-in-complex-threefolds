# Dense three-good speeds force exact bad-partial adjoint degree two

In an actual sliced polynomial fourfold, three affine-in-time
coordinates with rank-two speeds and dense homogeneous speed cone
force the remaining coordinate partial to have adjoint degree exactly
two. There is no bound on the time degree of the remaining coordinate.
The proof uses the actual invariant volume and its cofactors, not a
hypothetical coefficient array.

## 1. Exact hypotheses and conclusion

Assume
\[
\begin{gathered}
B=\mathbb C[x_1,x_2,x_3,z]=A[u],\qquad
E=\partial_u,\qquad A=\ker E,\\
E^2x_i=0,\qquad a_i=Ex_i\in A,\qquad
x_i=b_i+a_i u,\quad b_i\in A,\\
\operatorname{trdeg}_{\mathbb C}\mathbb C(a_1,a_2,a_3)=2,\\
P(a_1,a_2,a_3)\ne0
\quad\text{for every nonzero homogeneous }
P\in\mathbb C[T_1,T_2,T_3].
\end{gathered}
\tag{1}
\]
All four displayed original generators are polynomial coordinates.
The slice \(u\) is not assumed to be one of them or to be an
ambient polynomial coordinate. Define \(T=\partial_z\), holding
the three \(x_i\) fixed, and use
\(\operatorname{ad}_E T=[E,T]\).
Then
\[
(\operatorname{ad}_E)^3T=0,\qquad
(\operatorname{ad}_E)^2T\ne0.
\tag{2}
\]
Thus the selected adjoint degree is exactly two. This is a
strengthening of the retained rank-sensitive upper bound in this
dense-cone case.[^1]

## 2. A separating differential frame

Put \(F=\operatorname{Frac}A\). The equality \(B=A[u]\) gives
\(\operatorname{trdeg}_{\mathbb C}F=3\). Also \(A\simeq B/uB\)
is finitely generated; this quotient assertion does not say that
\(u\) is an ambient coordinate.

Choose two algebraically independent speeds, denoted \(s,t\),
and choose \(v\in A\) transcendental over \(\mathbb C(s,t)\).
Then
\[
F/\mathbb C(s,t,v)\text{ is finite and separable},\qquad
\Omega^1_{F/\mathbb C}
 =F\,ds\oplus F\,dt\oplus F\,dv.
\tag{3}
\]
Finite generation gives finiteness of this algebraic extension,
and characteristic zero gives separability.
The usual partial derivatives on \(\mathbb C(s,t,v)\) extend
uniquely to derivations \(\partial_s,\partial_t,\partial_v\)
of \(F\). Extend them to \(F(u)\) by killing \(u\).

Every \(a_i\) is algebraic over \(\mathbb C(s,t)\), by the
rank-two hypothesis. Differentiating its separable minimal
polynomial therefore gives \(\partial_v a_i=0\).
Consequently, with column vectors \(a=(a_i)\) and \(b=(b_i)\),
the first three rows of the original-coordinate Jacobian relative
to \((s,t,v,u)\) are
\[
\mathcal C=
\begin{pmatrix}
\vert&\vert&\vert&\vert\\
b_s+u a_s&b_t+u a_t&b_v&a\\
\vert&\vert&\vert&\vert
\end{pmatrix}.
\tag{4}
\]
The notation in (4) means a \(3\)-by-\(4\) matrix whose displayed
entries are its four columns. In particular, its third and fourth
columns are independent of \(u\).

## 3. The volume denominator is independent of \(u\)

Let
\(\omega=dx_1\wedge dx_2\wedge dx_3\wedge dz\).
The differentials \(ds,dt,dv,du\) form a basis over \(F(u)\).
Since \(z\in A[u]\), all four Jacobian rows have entries in
\(F[u]\), so
\[
\omega=J\,ds\wedge dt\wedge dv\wedge du,
\qquad 0\ne J\in F[u].
\tag{5}
\]

For an independent parameter \(\lambda\), the flow
\(\exp(\lambda E)\) is an automorphism of the polynomial ring
\(B[\lambda]\) fixing \(\lambda\), with polynomial inverse
\(\exp(-\lambda E)\). Its original-coordinate Jacobian is a
unit of \(B[\lambda]\), hence a complex constant. Evaluation at
\(\lambda=0\) makes this constant \(1\). Thus the flow fixes
\(\omega\).

It also fixes \(F\) pointwise and replaces \(u\) by \(u+\lambda\).
Taking differentials over \(\mathbb C(\lambda)\), it fixes
\(ds,dt,dv,du\). Equation (5) therefore gives
\(J(u+\lambda)=J(u)\), and hence \(J=J_0\in F^*\).
There is no claim that \(J_0\) is a complex constant.

## 4. Cofactors give the upper bound on every coefficient

The defining equations \(Tx_i=0\), \(Tz=1\) determine
\(T(s),T(t),T(v),T(u)\) by the inverse Jacobian. Using the
ordering \((s,t,v,u)\) and the cofactor signs from its last row,
\[
\begin{aligned}
T(s)&=-\frac{\det[b_t+u a_t,b_v,a]}{J_0},\\
T(t)&=\frac{\det[b_s+u a_s,b_v,a]}{J_0},\\
T(v)&=-\frac{\det[b_s+u a_s,b_t+u a_t,a]}{J_0},\\
T(u)&=\frac{\det[b_s+u a_s,b_t+u a_t,b_v]}{J_0}.
\end{aligned}
\tag{6}
\]
Only the good-coordinate rows enter these cofactors. Thus
\(T(s),T(t)\) have \(u\)-degree at most one, and
\(T(v),T(u)\) have \(u\)-degree at most two.
These bounds do not use the degree of \(z\).

For every \(f\in F\), the exact chain rule is
\(T(f)=f_sT(s)+f_tT(t)+f_vT(v)\).
Indeed the difference of these two derivations vanishes on
\(\mathbb C(s,t,v)\), and separable algebraicity forces it
to vanish on \(F\).
Hence \(T(F)\subset F[u]_{\le2}\).

For \(f\in A\), the actual value \(T(f)\) also belongs to
\(B=A[u]\). Uniqueness of coefficients in \(F[u]\) therefore
returns the bound to \(T(A)\subset A[u]_{\le2}\).
Similarly \(T(u)\in A[u]_{\le2}\).
No localization of a locally nilpotent derivation at a
noninvariant polynomial has been used.

Since \(E\) kills \(A\) and \(Eu=1\), for \(k\ge1\) one has
\((\operatorname{ad}_E)^kT(f)=\partial_u^kT(f)\) for
\(f\in A\), and the same identity holds on \(u\).
The coefficient bounds in (6) prove the first assertion of (2).

## 5. Cone density makes the quadratic coefficient nonzero

Introduce an indeterminate \(\tau\) over \(F\). The last
hypothesis of (1) is equivalent to algebraic independence of
\(\tau a_1,\tau a_2,\tau a_3\) over \(\mathbb C\):
separating the powers of \(\tau\) separates the homogeneous
parts of any proposed polynomial relation.

In characteristic zero these three independent functions have
nonzero exterior product of differentials. Because
\(\partial_v a_i=0\), direct expansion gives
\[
\begin{gathered}
d(\tau a_1)\wedge d(\tau a_2)\wedge d(\tau a_3)
 =\tau^2\Delta\,ds\wedge dt\wedge d\tau,\qquad
\Delta=\det[a_s,a_t,a]\ne0,\\
[u^2]\,T(v)=-\Delta/J_0\ne0,\qquad
(\operatorname{ad}_E)^2T(v)=-2\Delta/J_0\ne0.
\end{gathered}
\tag{7}
\]
The sign agrees with the third cofactor in (6).
Since \(v\in A\), this is an actual nonzero value of the
derivation on \(B\), not merely on a generic extension.
In fact \(-\Delta/J_0\in A\) by the coefficient return
already proved. This establishes the second assertion of (2).

Equivalently, the \(u\)-degree shift of \(T\) on \(A[u]\)
is exactly two: its coefficients on \(A\) have degree at most
two, one has degree two, and its coefficient on \(u\) has
degree at most two. This agrees with the intrinsic leading
construction retained in125, but that construction is not
needed for the cofactor proof here.[^2]

## 6. Rank two alone does not suffice

There is an actual rank-two control with adjoint degree one.
In \(\mathbb C[a,b,v,u]\), with \(E=\partial_u\), take
\[
\begin{gathered}
x_1=a,\qquad x_2=b+a^2u,\qquad
x_3=v+bu,\qquad z=u,\\
a=x_1,\qquad u=z,\qquad
b=x_2-x_1^2z,\qquad v=x_3-bz,\\
T=\partial_u-a^2\partial_b+(a^2u-b)\partial_v,\qquad
[E,T]=a^2\partial_v\ne0,\qquad [E,[E,T]]=0.
\end{gathered}
\tag{8}
\]
The displayed triangular recovery proves both polynomial
inverse orders. The good speeds \((0,a^2,b)\) have rank two,
but their cone lies in the first coordinate hyperplane.
Thus this control does not satisfy density. It is the same
kind of conical boundary already present in the retained
cofactor discussion.[^1]

## 7. Consequence and remaining gap

In the dense rank-two three-good class, selected adjoint
degree one is not a remaining case to search for. In
particular, the degree-two conclusion for successful
primitive lifts is a consequence of this broader fact,
not a separate recognition mechanism.

This does not imply that a primitive mixed cubic relation
exists or that either correction test passes. It does not
supply a three-good coordinate frame for an arbitrary
sliced action. The remaining construction and recognition
questions must therefore be pursued inside the actual
degree-two class, without treating hypothetical speed
polynomials or a Jacobian-only ansatz as a coordinate frame.

## Sources and comparison

1. [Rank-sensitive adjoint bounds from an actual three-good frame](three-good-flow-cofactor-bounds-pass126.md).
   The retained rank-sensitive upper bound and its conical
   rank-two degree-one control are comparisons. The complete
   upper and lower bounds used here are proved in Sections 2--5.
2. [An intrinsic additive action fixing every good-coordinate speed](three-good-intrinsic-speed-quotient-pass125.md).
   The retained leading-derivation construction is a comparison
   for the final degree-shift interpretation. It is not used
   to infer nonvanishing of the quadratic cofactor.

[^1]: [Three-good flow-cofactor bounds126](three-good-flow-cofactor-bounds-pass126.md), Sections 1--3 and the explicit degree-one control.
[^2]: [Three-good intrinsic speed quotient125](three-good-intrinsic-speed-quotient-pass125.md), Sections 1--4.
