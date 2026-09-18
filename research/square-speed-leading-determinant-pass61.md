# The leading determinant condition is automatic for square-speed quartics

For \(f=a^2,\ g=b^2\), the degree-four coefficient of the
determinant condition imposes no restriction on a pair of binary
quartics. Euler homogeneity already gives the leading matrix a
common right kernel. Its exact factorization shows that independent
mixed odd terms survive, even after allowing constant invertible
changes of the two outputs.

This concerns only the leading homogeneous determinant condition.
It does not prove constancy or nonvanishing of the full determinant,
actual coordinate generation, or a polynomial inverse.

## 1. The necessary coefficient under investigation

Work over \(L=\mathbb C(a,b)\), with
\[
f=a^2,\qquad g=b^2,\qquad
\partial_f=\frac1{2a}\partial_a,\qquad
\partial_g=\frac1{2b}\partial_b,\qquad
\mathscr H=\frac12(a\partial_a+b\partial_b).
\tag{1}
\]
The field partials are the actual unique extensions to \(L\);
they are not regular at the ramified origin. Let \(h_1,h_2\)
be arbitrary binary quartics with complex coefficients.
Then \(\mathscr Hh_i=2h_i\).

For independent generic bad variables \(\xi=(X,Y)^{\mathsf t}\), set
\[
Q_i^{(2)}=\frac14\,\xi^{\mathsf t}
\operatorname{Hess}_{f,g}(h_i)\xi,\qquad
M_2=
\begin{pmatrix}
\partial_fQ_1^{(2)}&\partial_gQ_1^{(2)}\\
\partial_fQ_2^{(2)}&\partial_gQ_2^{(2)}
\end{pmatrix}.
\tag{2}
\]
These are the quadratic parts and leading base-derivative matrix
in the necessary actual graph of
[pass44](generic-bad-pair-pass44.md).
If the full graph derivative is \(M_2+M_1+M_0\), its determinant's
homogeneous degree-four part in \(X,Y\) is exactly \(\det M_2\).
Thus a full determinant in \(L^*\) requires \(\det M_2=0\).
The question here is what that last necessary condition adds.

## 2. Euler homogeneity already kills the determinant

The field commutators are
\[
[\mathscr H,\partial_f]=-\partial_f,\qquad
[\mathscr H,\partial_g]=-\partial_g.
\]
Since \(h_i\) has Euler weight two, every entry of its Hessian
has weight zero. Holding \(X,Y\) fixed therefore gives
\[
\mathscr H Q_i^{(2)}=0,\qquad
f\,\partial_fQ_i^{(2)}+g\,\partial_gQ_i^{(2)}=0.
\]
Consequently
\[
M_2\binom fg=0,\qquad \boxed{\det M_2=0.}
\tag{3}
\]
The right-kernel column is nonzero over \(L\). This proves the
identity for every pair of quartics, without enumerating supports.
In fact this argument applies to any two weight-two elements of
the relevant characteristic-zero speed field, whenever the
commuting field partials have the indicated Euler commutators.

Equation (3) does not assert \(M_2=0\). Replacing the determinant
condition by entrywise vanishing would introduce a genuinely
stronger, unjustified condition.

## 3. The exact square factor and complete coefficient support

Write the two quartics as
\[
h_i=c_{i0}a^4+\alpha_i a^3b+c_{i2}a^2b^2
       +\beta_i ab^3+c_{i4}b^4.
\tag{4}
\]
The even part is \(c_{i0}f^2+c_{i2}fg+c_{i4}g^2\);
its Hessian is constant and contributes zero to the corresponding
row of \(M_2\). For the odd basis elements, their quadratic graph
parts are
\[
Q_{a^3b}^{(2)}
=\frac{3b}{16a}X^2+\frac{3a}{8b}XY-\frac{a^3}{16b^3}Y^2,
\]
\[
Q_{ab^3}^{(2)}
=-\frac{b^3}{16a^3}X^2+\frac{3b}{8a}XY+\frac{3a}{16b}Y^2.
\tag{5}
\]
Put
\[
J=b^2X-a^2Y.
\]
Differentiating (5) with the actual field partials gives the
complete formula
\[
\boxed{
M_2=\frac{3J^2}{32a^5b^5}
\begin{pmatrix}
\beta_1b^2-\alpha_1a^2\\
\beta_2b^2-\alpha_2a^2
\end{pmatrix}
\begin{pmatrix}b^2&-a^2\end{pmatrix}.}
\tag{6}
\]
All constants, including the factor \(1/4\) in (2), are retained.
This is an outer product over \(L[X,Y]\).

It follows that \(M_2\) has generic rank zero exactly when
\[
\alpha_1=\beta_1=\alpha_2=\beta_2=0,
\tag{7}
\]
and otherwise has generic rank one. Indeed \(J\ne0\), the row
\((b^2,-a^2)\) is nonzero, and the independence of \(a^2,b^2\)
over \(\mathbb C\) makes each coefficient
\(\beta_i b^2-\alpha_i a^2\) zero only when both scalars vanish.
Thus entrywise vanishing detects even quartics, but determinant
vanishing detects none of their odd support.

## 4. A rank-two odd pair survives every leading test here

Take
\[
h_1=a^3b,\qquad h_2=ab^3.
\tag{8}
\]
Their ordinary Jacobian is
\[
\det\operatorname{Jac}_{a,b}(h_1,h_2)=8a^3b^3\ne0.
\tag{9}
\]
Thus they satisfy the required generic rank-two acceleration
condition as a pair of base polynomials. Their leading matrix
in (6) has rank one, and its determinant is identically zero.

Modulo the even subspace \(\mathbb C[f,g]_2\), the odd coefficient
matrix of this pair in the basis \((a^3b,ab^3)\) is the identity.
A constant output change \(N\in\operatorname{GL}_2(\mathbb C)\)
changes that coefficient matrix to \(N\), which still has rank two.
Hence no such change makes either nonzero row even, and in
particular it cannot make both quartics belong to
\(\mathbb C[f,g]_2\).

This is a decisive boundary for the proposed leading-coefficient
argument. It is only polynomial base data satisfying the Euler,
rank, and leading-determinant conditions. No choices of linear
potentials or constants, full determinant claim, actual graph ring,
slice, ambient coordinate frame, or polynomial inverse are
asserted for (8) in this note.

## 5. Verification and remaining condition

[The one-method exact checker](square_speed_leading_checks_pass61.py) uses ten independent quartic
coefficients, directly differentiates their Hessians, and checks
the entire factorization (6), its right kernel and determinant,
and the independent odd pair. It is a symbolic coefficient
identity, not a numerical support grid. Its complete run passed
in 0.176 seconds, exit zero. An initial structural comparison
treated two oppositely signed but squared polynomial factors
as different; normalizing their difference fixed the harness.
No mathematical formula changed.

The new conclusion is that this particular degree-four
determinant condition is automatic, together with its exact
rank-zero versus rank-one factorization. The full lower-degree
determinant equations can still impose additional restrictions.
They must be analyzed separately, retaining the linear and
constant graph terms and all actual generation requirements.

No frozen pass60 file or shared metadata is changed, and no
counterexample to the full-frame or cancellation problem is claimed.
