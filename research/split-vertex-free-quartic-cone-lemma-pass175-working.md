# A vertex-free quadratic cone has no low-degree projection defect

**Status: working algebraic lemma with an explicit actual-chart application.**

Let \(F\) be a field of characteristic zero. Suppose three
polynomials in one parameter give a closed polynomial embedding
into the quadratic cone \(PS=Q^2\), avoid its vertex, and have
\(\deg P,\deg Q\le4\). Then the first two polynomials already
generate the parameter ring. The vertex condition is essential:
a degree-three nodal projection fails without it.

The actual split chart supplies this condition when its first
potential has the specific completed-square form in Section 4.
This note does not assume that every split chart has that form
or recognize the original four-ring.

## 1. Precise polynomial statement and field extension

Let \(P,Q,S\in F[v]\) satisfy
\[
P\ne0,\qquad PS=Q^2,\qquad
F[P,Q,S]=F[v],\qquad (P,Q,S)F[v]=F[v],\qquad
\max(\deg P,\deg Q)\le4.
\tag{1}
\]
Constants and zero polynomials are allowed when consistent with
(1); the degree of zero is \(-\infty\). The conclusion is
\[
F[P,Q]=F[v].
\tag{2}
\]

It suffices to prove this after extension to an algebraic closure
\(K\) of \(F\). The relations, generation and unit-ideal
conditions persist under extension. Conversely, if
\(K[P,Q]=K[v]\), flatness of the field extension identifies
\[
K\otimes_F\bigl(F[v]/F[P,Q]\bigr)=K[v]/K[P,Q]=0.
\tag{3}
\]
Faithfulness of extension on vector spaces forces the original
quotient to vanish. The quotient in (3) is a vector-space
quotient; \(F[P,Q]\) is not being treated as an ideal.

Work over \(K\) for the remainder of the polynomial proof.

## 2. Coprime squares and the linear-square case

First, if \(Q=0\), then \(S=0\) since \(P\ne0\); the
unit ideal makes \(P\) constant, contradicting generation.
Thus \(P,Q,S\) are all nonzero.

The unit ideal in (1) implies that \(P\) and \(S\) are
coprime. A prime dividing both would divide \(Q\), contrary
to that condition. In the factorization \(PS=Q^2\), every
prime exponent in either coprime factor is therefore even.
Absorb square roots of the constant units into the factors.
After choosing one sign there are coprime polynomials with
\[
P=a^2,\qquad Q=ab,\qquad S=b^2,\qquad
K[a^2,ab,b^2]=K[v],\qquad K[a,b]=K[v].
\tag{4}
\]
The last equality follows by containment in \(K[v]\).
Both \(a,b\) are nonzero. Write \(m=\deg a\),
\(n=\deg b\). The degree bounds give
\(m\le2\) and \(m+n\le4\).

If \(m=0\), the nonzero constant \(a\) makes
\(K[P,Q]=K[b]=K[P,Q,S]=K[v]\).

Suppose \(m=1\), and use \(x=a\) as an affine parameter.
Then \(n\le3\), and coprimality gives
\[
b=b_0+b_1x+b_2x^2+b_3x^3,\qquad b_i\in K,\qquad b_0\ne0.
\tag{5}
\]
Missing higher terms have zero coefficients. If \(b_2\ne0\),
choose \(x_0\in K\) with \(x_0^2=-b_0/b_2\).
Then \(x_0\ne0\), and \(x_0,-x_0\) are distinct. At
these points the even part \(b_0+b_2x^2\) is zero, so
\(b(-x_0)=-b(x_0)\). Hence all three polynomials
\(x^2,xb,b^2\) have the same value at the two points.
This contradicts (4): a ring generating the affine parameter
cannot identify distinct parameter values.
Therefore \(b_2=0\), and
\[
x=\frac{Q-b_1P-b_3P^2}{b_0}\in K[P,Q].
\tag{6}
\]
This proves (2) in the linear-square case.

## 3. The quadratic-square case cannot generate the full line

Suppose \(m=2\). Now \(n\le2\). If \(n=0\), then
\(K[a^2,ab,b^2]=K[a]\), which is not \(K[v]\) since
\(a\) has degree two. For example a polynomial in \(a\)
cannot have degree one in \(v\).

If \(n=1\), use \(x=b\). Write
\(a=a_2x^2+a_1x+a_0\), where \(a_2a_0\ne0\): the
leading coefficient is nonzero by its degree, and the constant
coefficient by \(\gcd(a,x)=1\). Pick
\(x_0^2=-a_0/a_2\). At the distinct points \(x_0,-x_0\),
both \(a\) and \(x\) change sign, so
\(a^2,ax,x^2\) all agree. This again contradicts generation.

Finally let \(n=2\), and choose the ratio \(\lambda\in K^*\)
of the leading coefficients of \(b\) and \(a\). Then
\(x=b-\lambda a\) has degree at most one. If it is constant,
\(K[a,b]=K[a]\ne K[v]\), contrary to (4). Thus \(x\)
is an affine parameter. Moreover
\[
K[a^2,ab,b^2]=K[a^2,ax,x^2],\qquad \gcd(a,x)=1.
\tag{7}
\]
The equality follows by expanding \(b=\lambda a+x\) and
subtracting the corresponding quadratic expressions in both
directions. The coprimality follows from \(\gcd(a,b)=1\).
The preceding quadratic-versus-linear argument now applies to
\(a,x\), giving the same contradiction.
All \(m=2\) possibilities have been excluded. Sections 1--2
therefore prove (2) over the original field \(F\).

## 4. The vertex-free condition from the actual split Jacobian

Retain the exact actual setup and notation of
[chart175](split-cubic-generic-chart-pass175-working.md) and
[the projected quartic bound175](split-cubic-projected-quartic-bound-pass175-working.md).
In particular \(A_L=L[v]\), the coefficient Jacobian is
\(J_0=-a^3\in L^*\), and
\(L[y,\vartheta,w]=L[v]\). Put \(r=k_\rho\) and
\(\mathcal R(U)=r-U\). The first polynomial potential is
\(\mathcal P=\mathcal R W_0+f(U,V)-\ell\), where
\(\deg f\le2\).

Assume the following specific completed-square form over \(L\):
\[
f(U,V)-\ell
=\kappa(V-\vartheta_0)^2+(U-r)D(U,V),\qquad
\kappa\in L^*,\quad\vartheta_0\in L,\quad\deg D\le1.
\tag{8}
\]
This is an additional form hypothesis here, not a conclusion of
the abstract cone lemma. Define evaluated polynomials
\[
P=r-y,\qquad Q=\vartheta-\vartheta_0,\qquad
S=-\frac{w-D(y,\vartheta)}{\kappa}.
\tag{9}
\]
Then \(PS=Q^2\). The affine formulas solve successively for
\(y,\vartheta,w\), so \(L[P,Q,S]=L[v]\). By the separate
[zero-R exclusion175](split-zero-R-exclusion-pass175-working.md),
\(P\ne0\). The projected bound gives
\(\deg P,\deg Q\le4\).

At an alleged common zero of \(P,Q,S\) over an algebraic
closure of \(L\), the formal-variable gradient of
\(\mathcal P=\mathcal R(W_0-D)+\kappa(V-\vartheta_0)^2\)
would vanish. Explicitly its evaluated components are
\[
B=f_U-w=-(w-D)-P D_U,\qquad
A=f_V=2\kappa Q-P D_V,\qquad P .
\tag{10}
\]
They are all zero at that point. But the actual constant
determinant is
\[
J_0=
\left[dy\wedge(P\,d\vartheta+B\,dt+A\,d\rho)\wedge dw
\right]_{dt\wedge d\rho\wedge dv}=-a^3 .
\tag{11}
\]
Its middle row would vanish, contradicting the nonzero scalar.
This evaluation takes place after forming the coefficient
identity. It does not differentiate a moving root.
Thus \(P,Q,S\) have no common zero, equivalently they generate
the unit ideal in \(L[v]\). Applying (2) gives
\(L[y,\vartheta]=L[v]\) in this specific cone case.
No integral coordinate in the original four-ring is inferred.

## 5. Why the vertex condition cannot be omitted

Over any characteristic-zero field, the polynomials
\[
P=v(v-1)^2,\qquad Q=v(v-1),\qquad S=v
\tag{12}
\]
satisfy \(PS=Q^2\), generate \(F[v]\) jointly, and obey the
degree bounds \((\deg P,\deg Q)=(3,2)\). Yet \(P,Q\)
have identical values at \(v=0\) and \(v=1\), so they do
not generate \(F[v]\). The triple meets the cone vertex at
\(v=0\), exactly violating the hypothesis used in (4).
This is a formal polynomial countercontrol, not an actual
split-cubic frame satisfying the calibrated determinant.

The lemma and its application use only the displayed elementary
factorization, degree, evaluation and field-extension arguments.
They do not infer a plane embedding from equality of fraction
fields alone. The source inputs were fully read before writing.
No checker was executed or imported; no frozen file was changed.
No split-case recognition, unrestricted cancellation, external
theorem, historical novelty, human expert review or formal
certification is claimed by this note.
