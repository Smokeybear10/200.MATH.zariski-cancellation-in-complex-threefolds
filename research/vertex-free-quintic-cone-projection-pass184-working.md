# A vertex-free quadratic cone has no projection defect through degree five

**Status: working elementary lemma, pending independent saved-source review.**

Let \(F\) be a characteristic-zero field. Suppose
\(P,Q,S\in F[v]\) satisfy
\[
P\ne0,\qquad PS=Q^2,\qquad F[P,Q,S]=F[v],\qquad
(P,Q,S)F[v]=F[v],\qquad
\max(\deg P,\deg Q)\le5.
\tag{1}
\]
Then
\[
F[P,Q]=F[v].
\tag{2}
\]
Zero or constant polynomials are permitted when consistent with (1),
and the degree of zero is \(-\infty\). The bound five is sharp:
Section 5 gives a vertex-free counterexample with degrees \((6,4)\).
These are statements about polynomial rings over a field, not actual
four-dimensional frames or invariant-coordinate recognition.

## 1. Exact-field descent and square factors

Let \(\overline F\) be an algebraic closure of \(F\). All hypotheses
in (1) persist after extension. If (2) holds over \(\overline F\),
then extension of vector spaces gives
\[
\overline F\otimes_F\bigl(F[v]/F[P,Q]\bigr)
 =\overline F[v]/\overline F[P,Q]=0.
\tag{3}
\]
Here the quotient is a vector-space quotient, not a quotient by an
ideal. Faithfulness of extension of scalars implies (2) over \(F\).
The identification of the extended subspace follows because
\(F[P,Q]\) is spanned over \(F\) by the monomials in \(P,Q\).
Thus the descent makes no rationality or algebraic-closedness
assumption about the original field.

Work now over \(\overline F\), written \(K\). If \(Q=0\), the
domain and \(P\ne0\) give \(S=0\). The unit-ideal condition then
makes \(P\) a nonzero constant, contradicting generation of \(K[v]\).
Thus all three polynomials are nonzero.

A prime dividing both \(P\) and \(S\) would divide \(Q\), contrary
to the unit-ideal hypothesis. Hence \(P,S\) are coprime. Their
prime exponents in \(PS=Q^2\) are even. Absorbing square roots
of their constant factors and then choosing a sign gives
\[
P=a^2,\qquad Q=ab,\qquad S=b^2,\qquad
\gcd(a,b)=1,\qquad K[a^2,ab,b^2]=K[v].
\tag{4}
\]
In particular \(K[a,b]=K[v]\). Let \(m=\deg a\), \(n=\deg b\).
The degree bounds give \(m\le2\) and \(m+n\le5\).

Whenever two distinct parameter values have equal values of
\(a^2,ab,b^2\), (4) fails: every polynomial in those three
values agrees at the two points, whereas the affine parameter
does not. We repeatedly use this elementary consequence of
generation, rather than assuming a converse to injectivity.

## 2. Constant and linear square factors

If \(m=0\), the nonzero constant \(a\) gives
\(K[P,Q]=K[b]=K[P,Q,S]=K[v]\).

If \(m=1\), use \(x=a\) as an affine parameter. Write the even
and odd parts of \(b\) as
\[
b(x)=B(x^2)+xC(x^2),\qquad B(0)=b(0)\ne0.
\tag{5}
\]
The last inequality follows from coprimality. In fact this part
of the argument needs no bound on \(\deg b\). If \(B\) were
nonconstant, choose a root \(s\in K\). It is nonzero because
\(B(0)\ne0\). Choose \(x_0^2=s\), so \(x_0\) and \(-x_0\)
are distinct. At these points \(b(-x_0)=-b(x_0)\). Thus both
\(a=x\) and \(b\) change sign, and all three cone coordinates
agree, contradicting (4).

Therefore \(B=b_0\in K^*\), and
\[
x=\frac{Q-P C(P)}{b_0}\in K[P,Q].
\tag{6}
\]
This proves the conclusion whenever \(m\le1\).

## 3. A quadratic square factor and degree at most two partner

Suppose \(m=2\); then \(n\le3\).
If \(n=0\), the generated triple ring is \(K[a]\), which is
not \(K[v]\). For example every nonconstant polynomial in
\(a\) has degree at least two.

If \(n=1\), use \(x=b\) as affine parameter and write
\(a=a_2x^2+a_1x+a_0\), with \(a_2a_0\ne0\). Choose
\(x_0^2=-a_0/a_2\). At the distinct points \(x_0,-x_0\),
both \(a\) and \(x\) change sign, contradicting (4).

If \(n=2\), subtract from \(b\) the scalar multiple of \(a\)
that cancels its quadratic term. Write \(b'=b-\lambda a\).
The substitutions preserve both the coprimality and the generated
triple ring, since
\[
ab'=ab-\lambda a^2,\qquad
(b')^2=b^2-2\lambda ab+\lambda^2a^2.
\tag{7}
\]
The inverse identities use \(b=b'+\lambda a\). If \(b'\) is
constant, \(K[a,b]=K[a]\), contradicting (4). If it is linear,
the preceding quadratic-versus-linear collision applies.
Thus no \(m=2,n\le2\) case satisfies (1).

## 4. The new quadratic-cubic case

It remains to exclude \(m=2,n=3\). Scaling \(a\) by a nonzero
constant scales the three cone generators by invertible constants
and preserves coprimality. After an affine parameter translation
we may therefore write \(a=v^2+c\). Subtracting a scalar multiple
of \(a\) from \(b\) removes its quadratic term, preserving the
triple ring and coprimality by (7). Thus
\[
a=v^2+c,\qquad b=A v^3+Bv+C,
\qquad A\ne0,\qquad \gcd(a,b)=1.
\tag{8}
\]
The \(K\)-coefficients in this display are unrelated to an
original invariant ring or to the ground field symbol \(F\).

Seek two parameters \(v_1,v_2\) for which both \(a\) and
\(b\) change sign. Put \(\sigma=v_1+v_2\) and
\(\pi=v_1v_2\). The two conditions are equivalent to
\[
\pi=\frac{\sigma^2+2c}{2},\qquad
-\frac A2\sigma^3+(B-3Ac)\sigma+2C=0.
\tag{9}
\]
Indeed the first equality is \(v_1^2+v_2^2+2c=0\).
Substitution in
\(A(\sigma^3-3\pi\sigma)+B\sigma+2C=0\)
gives the second.

The second polynomial in (9) has degree three, since \(A\ne0\),
so it has a root in \(K\). For that root choose \(v_1,v_2\)
as the two roots, with multiplicity, of
\(T^2-\sigma T+\pi\). These give both required sign changes.
They cannot coincide: if \(v_1=v_2=v_0\), those same conditions
would give \(2a(v_0)=2b(v_0)=0\), contrary to coprimality in
characteristic zero. We have therefore found two distinct points
with identical \(a^2,ab,b^2\), contradicting (4).

This excludes the last quadratic-square case. Sections 1--4 prove
(2), including descent to the original exact field.

## 5. Two precise boundaries

The vertex hypothesis cannot be omitted, even in lower degree:
\[
P=v(v-1)^2,\qquad Q=v(v-1),\qquad S=v.
\tag{10}
\]
Here \(PS=Q^2\), the triple generates \(F[v]\), and
\((\deg P,\deg Q)=(3,2)\). But \(P,Q\) agree at \(0,1\),
so the plane ring is proper. The triple meets the vertex at zero.

The degree threshold five is sharp even when the vertex is avoided:
\[
P=(v^3+1)^2,\qquad Q=v(v^3+1),\qquad S=v^2,
\qquad v=Q-S^2.
\tag{11}
\]
The cone equation and full triple generation follow directly.
Moreover
\(P-(2v+v^4)S=1\), so the vertex-free unit-ideal condition holds.
The degrees are \((\deg P,\deg Q)=(6,4)\). At the three distinct
roots of \(v^3+1\) over an algebraic closure, both \(P\) and
\(Q\) are zero. Thus the extended plane ring is proper, and
\(F[P,Q]\ne F[v]\). These are formal polynomial examples, not
actual projected charts with a constant fourfold Jacobian.

## Scope and verification

The degree-four cone proof175 and its whole-plane companion were
fully read before this extension. The new step is the quadratic-cubic
collision (9); the even-part argument also treats the linear-square
case uniformly. The algebraic proof above is self-contained and
does not invoke a genus or plane-embedding theorem.

Applying the lemma to a particular chart requires separately proving
every hypothesis in (1), notably the whole triple ring, avoidance
of the vertex, and both degree bounds. Equality of fraction fields
alone supplies none of those ring conclusions. No original-ring
coordinate, invariant lift, recognition, arbitrary-entry statement,
or unrestricted cancellation conclusion follows from this lemma.
No checker was written, executed, imported or compiled, and no
earlier artifact was changed. No novelty, human expert review or
proof-assistant verification is claimed.
