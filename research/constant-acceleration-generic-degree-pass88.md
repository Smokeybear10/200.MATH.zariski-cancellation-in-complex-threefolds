# A velocity determinant controls the generic degree of the generator ring

In the actual three-good-coordinate constant-acceleration setting,
one explicit nonvanishing determinant forces the smaller relative
generator ring to have the same fraction field as the original
kernel. This is a birationality criterion, not descent of its
generators or a new recognition theorem.

## 1. Actual local coordinates and the smaller field

Use the complete hypotheses and constructions of the
[invariant-plane lemma](constant-acceleration-invariant-plane-pass88.md)
and the [generator-pencil proof](universal-generator-pencil-pass88.md).
In particular,
\[
B=\mathbb C[x_1,x_2,x_3,z]=A[u],\quad
E(x_i)=b_i\in S=\mathbb C[s_1,s_2],\quad
E(z)=qu,\quad E(u)=1,\quad q\in\mathbb C^*,
\qquad S=\ker(W|_A).
\tag{1}
\]
Here W restricts to a nonzero actual LND of A and kills u. Set
K=Frac(S). A local slice for W gives a nonzero f in S and an
actual element v of A_f such that
\[
A_f=S_f[v],\qquad B_f=S_f[v,u],\qquad
a_i=x_i-b_i u\in A,\qquad
r=z-\frac q2u^2\in A.
\tag{2}
\]
For the local-slice assertion, choose an element a with W(a)=f
nonzero and W(f)=0, which exists by taking a suitable penultimate
nonzero iterate of W. Then v=a/f satisfies W(v)=1. The ordinary
finite slice projection proves A_f=S_f[v]; it does not assert a
polynomial presentation of A before localization.

Retain the completed matrix and generators from the cited notes.
They satisfy
\[
M b=e_1,\qquad M a=
\begin{pmatrix}-h\\ A_1\\ A_2\end{pmatrix},\qquad
R=S[A_1,A_2],\quad A=R[c],\quad
h=u-\sigma\in A\cap\operatorname{Frac}(R).
\tag{3}
\]
The last membership is the actual pencil consequence already
proved in the cited note. Since M is invertible over S, every a_i
lies in Frac(R). If c is transcendental over Frac(R), that same
note already proves R=S and A is a polynomial three-ring. In what
follows assume the remaining case trdeg_C(R)=3. Thus R_K is a
K-subalgebra of K[v] of transcendence degree one, and
Frac(A)=K(v) is a finite extension of L=Frac(R).

## 2. A critical transverse parameter forces one determinant to vanish

Write a=(a_1,a_2,a_3) transposed. All partial derivatives in the
following matrix are taken in the actual localized presentation
S_f[v,u], holding its other displayed variables fixed. Both the
original coordinate differentials and du,ds_1,ds_2,dv are bases
of the same module of absolute complex differentials. Consequently
their change-of-basis determinant is a unit:
\[
\mathcal J(u,v)=
\det\begin{pmatrix}
b&u b_{s_1}+a_{s_1}&u b_{s_2}+a_{s_2}&a_v\\
qu&r_{s_1}&r_{s_2}&r_v
\end{pmatrix}
\in B_f^*=S_f^*,
\qquad
\Omega=\det[b,b_{s_1},b_{s_2}]\in S.
\tag{4}
\]
In particular this determinant is independent of both u and v.
The unit assertion uses the original polynomial frame and its
actual localized inverse. It does not follow from a formal
coefficient matrix or from a generic rank condition alone.

Suppose there is v_0 in an algebraic closure of K at which all
three entries of a_v vanish. Evaluate the already differentiated
matrix over that field. Its last column then has only its bottom
entry potentially nonzero, so
\[
\mathcal J=
r_v(v_0)\det[b,u b_{s_1}+a_{s_1}(v_0),
                    u b_{s_2}+a_{s_2}(v_0)],
\qquad r_v(v_0)\ne0,
\qquad [u^2]\mathcal J=r_v(v_0)\Omega=0.
\tag{5}
\]
The nonzero assertion follows from the same unit determinant.
Thus the existence of such a common critical point implies
Omega=0. This is substitution into polynomial identities over K,
not differentiation of the algebraic element v_0 or the selection
of a new coefficient-field embedding.

## 3. The exact polynomial-factorization input

The arbitrary-field statement needed here is
[de Bondt, Corollary 3.2, printed pages 20--21](https://arxiv.org/pdf/1501.06046v4).
For a K-subalgebra of a polynomial ring whose fraction field has
transcendence degree one, it supplies a polynomial l generating
that fraction field and the equality K(l) intersect K[v]=K[l].
The field K need not be algebraically closed. The source is already
retained in the [polynomial-curve source note](polynomial-curve-factorization-source.md).

Apply it to R_K inside K[v]. There is l in K[v] such that
L=K(l). By (3), every a_i belongs to K(l) intersect K[v], hence
is a polynomial in l over K. If L is a proper subfield of K(v),
then l has degree at least two: a degree-one l already generates
K(v). Its derivative has a zero v_0 over the algebraic closure
of K, since the characteristic is zero. The chain rule then
makes every a_i,v vanish there. Equation (5) proves
\[
\boxed{\quad
\Omega\ne0\quad\Longrightarrow\quad
\operatorname{Frac}(R)=\operatorname{Frac}(A).
\quad}
\tag{6}
\]
Equivalently, a proper finite generic extension in this actual
construction can occur only when Omega vanishes identically.
The condition is unchanged by choosing different polynomial
coordinates on S: their two-by-two Jacobian determinant is a
nonzero complex constant, and the two derivative columns in (4)
transform by the corresponding invertible matrix.

No conclusion here identifies R with A, places h in R, makes
R normal, or proves that R to A is finite or faithfully flat.
The relevant faithful flatness in the predecessor is S to A.
The [pencil cusp control](universal-generator-pencil-pass88.md)
already demonstrates that equal fraction fields and the exact
pencil identity do not by themselves descend h into R. It is an
algebra-only boundary, not an actual example for (1). Nor does
(6) resolve the case Omega=0 or recognize the unknown kernel.

## 4. Read scope and provenance

The complete saved invariant-plane and generator-pencil proofs
were read through EOF for this argument. The selected primary
reads were de Bondt's complete displayed Corollary 3.2 and Lemma
3.3 proofs, the relevant implications (2) to (3) to (4) of
Theorem 3.1, and the arbitrary-field statement of Theorem 1.1.
This does not claim a new audit of the classical Luroth proof,
all earlier lemmas invoked by that paper, or its whole proof.
The retained versioned inputs are
[the primary PDF](../tmp/pdfs/bondt-1501.06046v4.pdf) and
[its text](../tmp/pdfs/bondt-1501.06046v4.txt).

Geometry proposed the common-critical-point determinant argument
and its application to the generator field. General independently
reconstructed the actual differential-basis unit, substitution
over the geometric generic fiber, and the coefficient comparison,
and identified the exact retained arbitrary-field source. That
outline reconstruction is separate from any subsequent full
saved-file review. This note adds no checker or numerical run and
changes no pass87 or older artifact.
