# Exact square speeds are excluded by the full Schur and generation gates

The actual independent-defect quadratic frame cannot have
\(f=a^2,\ g=b^2\) in genuine coordinates \(a,b\) of its full
invariant plane \(C=\mathbb C[a,b]\). The leading determinant
condition alone is automatic. The full determinant, followed by
actual coordinate generation, excludes all three possible ranks
of the odd quartic acceleration terms.

This is an exact square-speed theorem. It does not cover arbitrary
ramified germs with the same initial terms, additional algebraic
extensions of the invariant field, or a universal choice of frame.
No conclusion about unrestricted cancellation is asserted.

## 1. Actual hypotheses and the retained graph

Use the full setup of
[the generic bad-pair theorem](generic-bad-pair-pass44.md):
\[
B=\mathbb C[x_1,x_2,X,Y]=A[s_*],\qquad Es_*=1,
\]
\[
C=\mathbb C[a,b],\qquad L=\mathbb C(a,b),\qquad
B_L=L[X,Y],\qquad B\cap L=C,
\]
\[
f=EX=a^2,\qquad g=EY=b^2,\qquad
E=f\partial_X+g\partial_Y\quad\hbox{on }B_L.
\tag{1}
\]
Here \(X,Y\) are the actual bad coordinates, and the original
ambient good partials satisfy the hypotheses used to derive
that theorem. In particular the actual good coordinates have
the exact expressions
\[
Q_i=x_i=
\frac14(X,Y)\operatorname{Hess}_{f,g}(h_i)\binom XY
+(\nabla_{f,g}k_i)\binom XY+\ell_i,
\]
\[
h_i=E^2x_i\in C,\qquad k_i,\ell_i\in L,\qquad
\mathscr Hh_i=2h_i,\qquad \mathscr Hk_i=k_i,
\tag{2}
\]
where
\[
\partial_f=\frac1{2a}\partial_a,\qquad
\partial_g=\frac1{2b}\partial_b,\qquad
\mathscr H=f\partial_f+g\partial_g
=\frac12(a\partial_a+b\partial_b).
\tag{3}
\]
The \(k_i\) and \(\ell_i\) are not initially assumed regular.

Two separate actual consequences must be retained. First, if
\(Q_v=(\partial Q_i/\partial v_j)\), \(v=(f,g)^{\mathsf t}\),
then the true Schur inverse gives
\[
Q_v\in\operatorname{Mat}_2(L[X,Y]),\qquad
Q_v^{-1}\in\operatorname{Mat}_2(L[X,Y]),
\qquad \det Q_v\in L^*.
\tag{4}
\]
Second, the four original polynomial coordinates generate the
actual fraction field:
\[
\mathbb C(Q_1,Q_2,X,Y)=\operatorname{Frac}B=L(X,Y).
\tag{5}
\]
The equality on the right follows by taking fractions of
\(B_L=L[X,Y]\); invariant localization does not change
\(\operatorname{Frac}B\).
Neither (4) nor (5) follows merely by displaying four quadratic
generators over an invariant base.

**Theorem.** The actual data (1)--(5) are inconsistent.

The proof does not impose a second-image obstruction, a
particular plinth multiplicity, or a bound on the generic degree
of the supplied slice.

## 2. Allowed shears and rational radial coefficients

Because \(h_i\in\mathbb C[a,b]\), equation (3) makes \(h_i\)
a homogeneous binary quartic with complex coefficients. Write
\[
h_i=c_{i0}a^4+\alpha_i a^3b+c_{i2}a^2b^2
+\beta_i ab^3+c_{i4}b^4.
\tag{6}
\]
The even terms belong to \(\mathbb C[f,g]_2\). Their contribution
to (2) is a complex-coefficient quadratic polynomial in \(X,Y\).
Subtracting that polynomial from \(Q_i\) is a genuine polynomial
good-coordinate shear with the bad pair fixed. It removes exactly
the corresponding even acceleration, leaves \(Q_v\) unchanged,
and preserves (5).

A constant invertible change of the two good coordinates likewise
preserves actual coordinate generation and multiplies \(Q_v\)
on the left by a constant invertible matrix. We use these changes
to normalize the rank of the constant odd coefficient matrix
\[
\begin{pmatrix}\alpha_1&\beta_1\\
                \alpha_2&\beta_2\end{pmatrix}.
\tag{7}
\]
Only the already-derived graph equations, determinant condition,
and actual coordinate generation are carried through these
changes. There is no claim that every original bad-adjoint bound
is preserved by the shears.

Put
\[
r=b/a,\qquad L=\mathbb C(a,r).
\]
At fixed \(r\), \(\mathscr H=(a/2)\partial_a\).
The kernel of this derivation on \(L\) is \(\mathbb C(r)\):
a rational function of \(a\) over the characteristic-zero field
\(\mathbb C(r)\) with zero derivative is constant in \(a\).
Consequently
\[
\mathscr Hk_i=k_i
\quad\Longrightarrow\quad
k_i=a^2d_i(r),\qquad d_i(r)\in\mathbb C(r).
\tag{8}
\]
Also
\([\mathscr H,\partial_f]=-\partial_f\) and
\([\mathscr H,\partial_g]=-\partial_g\).
Every Hessian coefficient of \(h_i\) and every gradient
coefficient of \(k_i\) therefore has weight zero. Hence,
after any of the permitted changes, the graph has the form
\[
Q=S(r;X,Y)+\ell(a,r),
\tag{9}
\]
where \(S\in\mathbb C(r)[X,Y]^2\) consists only of its
homogeneous linear and quadratic parts.

The absence of a constant term in \(S\) is a definition:
all such terms are put in \(\ell\). No regularity or pole
restriction on the rational linear coefficients has been used.

## 3. The full determinant aligns every positive-degree coefficient

Let
\[
A_0=\ell_v,\qquad
\lambda=\nabla_{f,g}r
=\left(-\frac{r}{2f},\frac1{2fr}\right).
\]
Holding \(X,Y\) fixed in the base derivatives of (9) gives
\[
Q_v=A_0+S_r\lambda.
\tag{10}
\]
The second summand is a single rank-one update containing
both the quadratic and linear terms.

Since \(\det Q_v\in L^*\), evaluation at \(X=Y=0\) gives
\(\det A_0=\det Q_v\ne0\). The two-by-two determinant formula
for (10) then gives
\[
\det Q_v=\det A_0
 \left(1+\lambda A_0^{-1}S_r\right),
\qquad \lambda A_0^{-1}S_r=0.
\tag{11}
\]
This determinant formula follows directly by multilinearity:
the contribution using both columns of the rank-one summand
vanishes, leaving only the constant and linear-update terms.

The kernel of the nonzero row \(\lambda\) is the line
\(L(f,g)^{\mathsf t}\). Therefore every coefficient vector
of \(S_r\), considered as a polynomial in \(X,Y\), is
collinear with
\[
A_0\binom fg=\mathscr H\ell\ne0.
\]
Equivalently,
\[
\boxed{\det[\,\mathscr H\ell\mid S_r\,]=0.}
\tag{12}
\]
The nonvanishing here follows from \(A_0\) invertible and
\((f,g)\ne0\) over \(L\).

This conclusion uses the full determinant. The degree-four
determinant of the quadratic matrix by itself is automatic,
as shown in
[the separate leading-coefficient note](square-speed-leading-determinant-pass61.md).

## 4. Rank two: the actual coordinate field cannot be generated

Suppose (7) has rank two. A constant good-output change puts
the odd accelerations in the form
\[
h_1=a^3b,\qquad h_2=ab^3
\]
after the even shears. Their quadratic graph pieces are
\[
F_1=\frac{3rX^2+6XY/r-Y^2/r^3}{16},
\qquad
F_2=\frac{-r^3X^2+6rXY+3Y^2/r}{16}.
\tag{13}
\]
Direct differentiation gives
\[
(F_1)_r=\frac3{16}(X-Y/r^2)^2,\qquad
(F_2)_r=-r^2(F_1)_r.
\tag{14}
\]
In particular the quadratic coefficient vectors of \(S_r\)
span the line through \((1,-r^2)^{\mathsf t}\).

Equation (12) now implies
\[
\mathscr H\ell_2=-r^2\mathscr H\ell_1,\qquad
\mathscr H\ell_1\ne0.
\]
Since \(\mathscr Hr=0\), this is exactly
\[
\ell_2+r^2\ell_1=I(r),\qquad I(r)\in\mathbb C(r),
\qquad \partial_a\ell_1\ne0.
\tag{15}
\]
Adding \(r^2Q_1\) to \(Q_2\), and retaining the arbitrary
linear terms, yields
\[
Q_2=-r^2Q_1+
 \frac{r^3X^2+6rXY+Y^2/r}{8}
 +A(r)X+B(r)Y+I(r),
\quad A,B\in\mathbb C(r).
\tag{16}
\]
No regularity of \(k_i\), \(\ell_i\), \(A\), \(B\), or \(I\)
is required for this identity.

### 4.1. Independence of the coefficient field

Over \(\mathbb C(r,X,Y)\), the element \(a\) is transcendental.
The derivative \(\partial_aQ_1=\partial_a\ell_1\ne0\) means
that \(Q_1\) is a nonconstant rational function of \(a\)
over that field. It is therefore transcendental over
\(\mathbb C(r,X,Y)\). For completeness, if a nonconstant
rational function of \(a\) were algebraic over the coefficient
field, the polynomial equation expressing that rational function
in terms of \(a\) would make \(a\) algebraic over an algebraic
extension of the coefficient field, a contradiction.

Thus \(Q_1,r,X,Y\) are algebraically independent. Set
\[
K=\mathbb C(Q_1,X,Y).
\]
Then (16) expresses \(Q_2\) as a rational function
\(\mathcal R(r)\in K(r)\), with \(r\) transcendental over \(K\).

### 4.2. Two unavoidable poles

At \(r=\infty\), the term \(r^3X^2/8\) in (16) forces
a pole of order at least three. At \(r=0\), the term
\(Y^2/(8r)\) forces a pole of order at least one.

These claims permit arbitrary poles in \(A,B,I\). In the
Laurent expansion at either point, every coefficient contributed
by those terms is at most linear in the independent variables
\(X,Y\), while the term \(-r^2Q_1\) is linear in the
independent variable \(Q_1\). The other displayed quadratic
terms have different monomials or different Laurent orders.
In particular the coefficient of \(r^3\) contains the
uncancelled monomial \(X^2/8\), and the coefficient of
\(r^{-1}\) contains the uncancelled monomial \(Y^2/8\).
Terms with still more extreme Laurent orders can increase
the poles but cannot reduce these lower bounds.

It follows that
\[
[K(r):K(Q_2)]\ge4.
\tag{17}
\]
Here is the elementary field-degree fact being used. For a
nonconstant reduced rational function \(P(r)/T(r)\) over any
field \(K\), the polynomial \(P(Z)-uT(Z)\) is irreducible
in \(K[Z,u]\). Indeed it is linear in \(u\), so any
factor independent of \(u\) would divide both \(P\) and \(T\).
Gauss's lemma gives irreducibility over \(K(u)\), and hence
\[
[K(r):K(P(r)/T(r))]=\max(\deg P,\deg T).
\]
The last number is the total degree of its pole divisor.
At the two distinct \(K\)-rational points zero and infinity,
the pole orders already sum to at least four.

### 4.3. Actual generation gives the contradictory degree one

Put \(M=L(X,Y)=\mathbb C(a,r,X,Y)\).
Actual equality (5) says
\[
M=K(Q_2).
\]
But (16) gives \(Q_2\in K(r)\), and \(r\in M\).
Consequently
\[
K(Q_2)\subseteq K(r)\subseteq M=K(Q_2).
\tag{18}
\]
All three fields are equal. This contradicts (17).

Thus rank-two odd support is impossible. The contradiction
requires the actual complex coordinate field (5), not merely
generation of \(B_L\) as an \(L\)-algebra.

## 5. Rank one: a good coordinate becomes affine in the bad pair

Suppose (7) has rank one. After a constant good-output change,
the odd acceleration occurs only in the first row:
\[
h_1=\alpha a^3b+\beta ab^3,\qquad h_2=0,
\qquad (\alpha,\beta)\ne(0,0).
\]
Its quadratic \(r\)-derivative is
\((\alpha-\beta r^2)(F_1)_r\), which is nonzero.
Thus the degree-two coefficient vectors of \(S_r\) span
the first coordinate line.

Equation (12) forces \(\mathscr H\ell\) to lie on that
line. It then also forces every linear coefficient vector
of \(S_r\) to lie on the same line. In particular
\[
\mathscr H\ell_2=0,\qquad (S_2)_r=0.
\tag{19}
\]
The second row has no quadratic term. Its two linear
coefficients belong to \(\mathbb C(r)\), and zero \(r\)
derivative makes them complex constants. Therefore
\[
Q_2=c_1X+c_2Y+\ell_2,\qquad c_1,c_2\in\mathbb C.
\]
Actualness of \(Q_2,X,Y\) gives
\(\ell_2\in B\cap L=C\). A polynomial in \(a,b\) killed
by \(\mathscr H=\frac12(a\partial_a+b\partial_b)\) is
constant, by comparison of homogeneous terms. Hence
\(\ell_2\in\mathbb C\).

This makes \(Q_2\) a complex affine polynomial in \(X,Y\),
contrary to algebraic independence of the four actual
coordinates. Notice that no premature regularity claim
about the original \(k_2\) was needed: regularity of
\(\ell_2\) was obtained only after its actual linear
terms had been proved constant.

## 6. Rank zero: actual velocities and the supplied slice

Suppose both odd vectors vanish. After the even quadratic
shears all accelerations are zero, and
\[
Q_i=(\nabla_{f,g}k_i)\binom XY+\ell_i.
\]
Applying \(E\) to the actual coordinate \(Q_i\), and using
\(\mathscr Hk_i=k_i\), gives
\[
EQ_i=k_i\in B\cap L=C.
\tag{20}
\]
Only at this stage are the \(k_i\) known to be polynomial.
Their weight one implies
\[
k_i=A_i a^2+\mu_i ab+B_i b^2,\qquad
A_i,\mu_i,B_i\in\mathbb C.
\]
Subtract the actual constant-coefficient linear bad terms
\(A_iX+B_iY\) from the good coordinates. The remaining graph is
\[
Q_i=\frac{\mu_i}{2}(rX+Y/r)+\ell_i.
\tag{21}
\]

If the constant vector \(\mu=(\mu_1,\mu_2)^{\mathsf t}\)
is nonzero, a constant good-output change puts it on the
first coordinate line. Now
\[
S_r=\frac12(X-Y/r^2)\binom10
\]
after rescaling. Equation (12) explicitly forces
\(\mathscr H\ell\) onto that same line. Hence
\(Q_2=\ell_2\) is an actual element of \(C\) with
\(\mathscr H\ell_2=0\), so it is constant. This again
contradicts actual coordinate independence.

It remains that \(\mu=0\). All the transformed good
coordinates are then \(\ell_i\in B\cap L=C\).
Let \(R=C_{(a,b)}\). The transformations were genuine
polynomial coordinate changes with the bad pair fixed;
their four functions still generate \(B_R\) over \(R\).
Thus
\[
B_R=R[X,Y].
\tag{22}
\]
On this whole polynomial ring,
\[
E(B_R)\subseteq(a^2,b^2)R[X,Y].
\]
The supplied arbitrary slice \(s_*\in B_R\) still has
\(Es_*=1\). Evaluating the resulting ideal identity at
\(X=Y=0\) would give \(1\in(a^2,b^2)R\), impossible.
No affine-slice assumption has been made. This completes
the theorem.

## 7. Why the generation gate is essential

There is a rational graph with the rank-two odd pair that
satisfies even the full polynomial-inverse condition (4).
It is not an actual coordinate frame.

Take \(h=(a^3b,ab^3)^{\mathsf t}\), \(k=0\), and
\(\ell=(-f,g)^{\mathsf t}\), so \(Q=(F_1-f,F_2+g)^{\mathsf t}\).
Put
\[
J=gX-fY,\qquad c=\frac{3J^2}{32a^5b^5},\qquad
A_0=\begin{pmatrix}-1&0\\0&1\end{pmatrix},\qquad
s=\binom{-f}{g}.
\]
The exact leading factorization gives
\[
Q_v=A_0+c\,s\begin{pmatrix}g&-f\end{pmatrix},
\quad \det Q_v=-1,
\]
\[
Q_v^{-1}=A_0+
 c\binom fg\begin{pmatrix}g&f\end{pmatrix}.
\tag{23}
\]
Multiplying the two displayed matrices proves the inverse:
the possible quadratic-update cross term is killed by
\((g,-f)(f,g)^{\mathsf t}=0\).
Both matrices have entries in \(L[X,Y]\).

Nevertheless \(Q_1,Q_2,X,Y\) are all fixed by the nontrivial
field involution \((a,b)\mapsto(-a,-b)\), with \(X,Y\)
fixed. They cannot generate \(L(X,Y)\), since \(a\) is
not fixed. Thus this control meets the rational determinant
and inverse conditions but fails exactly the actual
coordinate-field gate used above. No actual sliced ring,
ambient coordinate frame, or cancellation counterexample
is claimed for it.

## 8. Attribution, verification, and limits

The source input is the previously proved actual
[pass44 graph and Schur identities](generic-bad-pair-pass44.md).
The separate
[leading-determinant calculation](square-speed-leading-determinant-pass61.md)
explains why the highest determinant coefficient cannot
exclude the square-speed case. The present proof retains
all lower terms and supplies the actual generation argument.
The rational-function field-degree step was proved directly
above; no new curve-classification theorem is invoked.

The argument was developed by the main agent and the affine
agent. The jet and geometry agents each independently read
the complete proof through EOF and reconstructed all 23
numbered equations, the three rank cases, and the stated
scope. Both full-file audits were clean, with no correction.
These are AI proof audits, not external expert review.

A separate scratch exact calculation verified (13)--(14),
the quadratic sum in (16), the direct base Jacobian in
(23), its determinant, and both inverse orders. It added
no suite or test-method count. The affine agent also
fully read the separate leading checker and independently
reran its one method in 0.176 seconds, exit zero.
No new numerical suite is claimed by this proof note.

The exact-field condition \(L=\mathbb C(a,b)\), the exact
speeds \(a^2,b^2\), the whole Schur determinant, and actual
coordinate generation are all essential retained hypotheses.
The result does not apply merely because a speed ideal has
initial form \((a^2,b^2)\), nor to a further algebraic
extension of this field without an additional argument.
It does not identify \(a,b\) as ambient coordinates,
supply a universal low-degree frame, or resolve the other
ramified common-zero types.
