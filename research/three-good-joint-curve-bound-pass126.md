# Joint-curve adjoint bounds and nonunit speed-curve recognition

## 1. Two precise refinements

Retain actual polynomial coordinates and a global slice:
\[
 \begin{gathered}
 B=\mathbb C[x_1,x_2,x_3,z]=A[u],\qquad
 E\in\operatorname{LND}_{\mathbb C}(B),\quad A=\ker E,\quad E(u)=1,\\
 E^2x_i=0,\qquad a_i=Ex_i,\qquad c=Ez,\qquad
 r=\operatorname{trdeg}_{\mathbb C}\mathbb C[a_1,a_2,a_3].
 \end{gathered}
 \tag{1}
\]
First, when \(E^3z=0\), write \(q=E^2z\) and let
\(s=\operatorname{trdeg}_{\mathbb C}\mathbb C[a_1,a_2,a_3,q]\).
The joint rank sharpens the all-column cofactor bound: the selected
bad partial has adjoint degree at most \(r\), and every other partial
has adjoint degree at most \(s+1\).

Second, with no degree restriction on \(z\), the case \(r=1\) and
\((a_1,a_2,a_3)B\ne B\) is recognized:
\(A\simeq\mathbb C^{[3]}\). The proof uses the original \(z\)-degree,
not localization at a curve parameter or a first-power
acceleration-membership theorem.

These are statements within a supplied three-good frame, not
unrestricted cancellation. No file through pass125 or the earlier
cofactor126 note is changed.

## 2. The joint rank in every cofactor

Assume \(E^3z=0\). Put \(T_j=\partial_{x_j}\) for \(j\le3\) and
\(T_4=\partial_z\). The
[cofactor proof126](three-good-flow-cofactor-bounds-pass126.md)
establishes the exact conjugation orientation:
\(\exp(tE)T_j\exp(-tE)\) is column \(j\) of
\(\operatorname{Jac}(F_t)^{-1}=\operatorname{adj}(\operatorname{Jac}(F_t))\),
where \(F_t=\exp(tE)x\). Its row one-forms are
\[
 dF_{t,i}=dx_i+t\,da_i\quad(i\le3),\qquad
 dF_{t,4}=dz+t\,dc+\frac{t^2}{2}\,dq.
 \tag{2}
\]
Characteristic zero makes the rank of the covectors \(da_i,dq\)
equal to \(s\).

The last column deletes the fourth row, so its degree is at most
\(r\), as already proved. Any other minor contains two good rows
and the fourth row. Expand it by alternating multilinearity.

- A term using \(dz\) and \(k\) speed differentials has degree
  \(k\le s\).
- A term using \(t\,dc\) and \(k\) speed differentials has degree
  \(k+1\le s+1\), since the \(k\) speed differentials must be independent.
- A term using \(t^2dq/2\) and \(k\) speed differentials has degree
  \(k+2\le s+1\), since it contains \(k+1\) independent differentials
  drawn from the joint field.

Zero covectors and zero terms cause no exception to these bounds.
Thus, on the original polynomial ring,
\[
 \operatorname{ad}_E^{\,r+1}T_4=0,\qquad
 \operatorname{ad}_E^{\,s+2}T_j=0\quad(1\le j\le3).
 \tag{3}
\]
The common intrinsic-kernel theorem125 gives \(s\le2\) if some
speed is nonzero, so \(s=2\) recovers the previous bounds. No
polynomial-plane identification or quotient flatness is needed for
this differential-rank argument.

For \(s=1\), (3) says that the bad adjoint degree is at most one,
and all three other degrees are at most two. Equivalently, the
possible cubic cofactor terms are wedges of two \(da_i\)'s with
\(dc\), or of a \(da_i\), a \(dq\), and an unchanged coordinate
differential. Each vanishes when the joint rank is one.

## 3. The exact joint-curve partial profile

The rank-zero speed endpoints require no classification of the
remaining coordinate. If some \(a_i\) is a nonzero complex constant,
\(x_i/a_i\) is an actual coordinate slice and
\(A\simeq B/(x_i)\simeq\mathbb C^{[3]}\).
If all \(a_i=0\), then \(E=c\partial_z\); the slice identity
\(c\partial_zu=1\) makes \(c\in\mathbb C^*\) and the kernel is
the good-coordinate ring. Thus an unrecognized instance with
\(s=1\) must have \(r=1\).

Let \(\delta_j\) denote the actual partial's degree for the
\(u\)-filtration. A degree-minus-one partial already recognizes
the kernel. For nonnegative degrees, these equal the adjoint
degrees. The
[commuting-partial gate126](three-good-common-leading-kernel-boundary-pass126.md),
Section 3, recognizes any original degree-zero partial, including
a good partial. Therefore a hypothetical nonpolynomial kernel in
the joint-curve case must have all four degrees positive.

The retained
[height-ten theorem73](height-ten-closure-pass73.md)
then leaves exactly
\[
 (\delta_1,\delta_2,\delta_3,\delta_4)=(2,2,2,1),
 \qquad H=\sum_j(\delta_j+1)=11.
 \tag{4}
\]
Indeed (3) gives the displayed componentwise upper bounds; lowering
any one of them lowers \(H\) to at most ten. Here the bad coordinate
is fourth. The sorted profile is \((1,2,2,2)\), not a coordinate
\(E\)-degree profile.

This is a necessary profile for a hypothetical unrecognized instance.
It is not a construction of such an instance or a recognition theorem
for every frame with that profile.

## 4. Polynomial parametrization of a speed curve

Return to (1) without assuming \(E^3z=0\), and suppose \(r=1\).
The exact retained
[polynomial-curve factorization](polynomial-curve-factorization-source.md)
applies to \(\mathbb C[a_1,a_2,a_3]\subset B\). It gives
\[
 p\in B\setminus\mathbb C,\qquad
 a_i=f_i(p),\quad f_i\in\mathbb C[t],\qquad E(p)=0.
 \tag{5}
\]
The parameter is genuinely polynomial in the original coordinates;
it is not asserted to be an ambient coordinate. For the last
equality, choose a nonconstant \(f_i\) and differentiate
\(E(f_i(p))=0\). Then \(f_i'(p)\ne0\), and the domain property
gives \(E(p)=0\).

The source is de Bondt's Corollary 3.2. It places the speed algebra
inside the polynomial ring generated by a polynomial field parameter.
Its selected complete statement and proof and the adjacent
polynomial-intersection Lemma 3.3 were freshly read for this use;
their earlier Lüroth dependencies were not newly reconstructed.
[De Bondt, Corollary 3.2 and Lemma 3.3](https://arxiv.org/html/1501.06046v4).

## 5. A nonunit common factor forces the good ring to be stable

Choose the univariate gcd \(h=\gcd(f_1,f_2,f_3)\), and write
\(f_i=h\,g_i\). The zero entries are harmless since at least one
speed is nonzero. Bézout in \(\mathbb C[t]\) gives
\(\sum_i\lambda_i g_i=1\). Substitution at \(p\) therefore gives
an exact equality of ideals, with their multiplicities:
\[
 I=(a_1,a_2,a_3)B=h(p)B,\qquad (h(p),c)B=B,\qquad
 h(p)\mid p_z .
 \tag{6}
\]
The middle equality follows from the actual slice equation
\(1=\sum_i a_i u_{x_i}+c\,u_z\). To prove the last divisibility,
use (5) in the original derivation:
\[
 0=E(p)=h(p)\sum_i g_i(p)p_{x_i}+c\,p_z.
 \tag{7}
\]
Modulo \(h(p)\), the class of \(c\) is a unit by (6), so
\(p_z\in h(p)B\). This step does not discard nonreduced structure.

If \(I\ne B\), the polynomial \(h\) is nonconstant: a nonzero
constant \(h\) would give \(I=B\). Conversely a nonconstant \(h\)
has nonconstant \(h(p)\), which cannot be a unit in \(B\).
Suppose \(p_z\ne0\), and let \(m=\deg_zp\ge1\), using the
actual original variable \(z\) over \(\mathbb C[x_1,x_2,x_3]\).
Then
\[
 \deg_z h(p)=(\deg h)m\ge m
   >m-1=\deg_z p_z,
 \tag{8}
\]
contradicting the nonzero divisibility in (6). The leading coefficient
of the univariate \(h\) is a nonzero complex constant, so the first
degree equality has no cancellation exception.

Consequently \(p_z=0\), and all \(a_i=f_i(p)\) belong to the
actual three-ring \(R=\mathbb C[x_1,x_2,x_3]\). It is preserved by
\(E\), and the restriction is a nonzero nice LND of \(R\).
The retained three-variable linear-invariant theorem supplies an
invariant constant linear form in the \(x_i\). It is an ambient
coordinate of \(B\). The original slice makes \(A\) regular, so
the retained Bhatwadekar--Gupta--Lokhande Theorem 3.5 recognizes
\(A\simeq\mathbb C^{[3]}\).
The exact source gate is
[linear-invariant71](nice-linear-invariant-source-pass71.md);
its stable-good-ring application was already recorded in
[source-scope85, Section 2](rank-one-quasi-nice-source-scope-pass85.md).

This proves nonunit speed-curve recognition for arbitrary degree
of \(z\). Neither \(q\in I\), the strict power certificate84, nor
the square theorem125 is an input.

## 6. The exact determinant and content identities in the joint-curve case

Assume the quadratic joint rank is one and the speed rank is one.
Apply the polynomial factorization in Section 4 to the entire joint
algebra to choose \(p\in B\setminus\mathbb C\) with
\(a_i=f_i(p)\), \(q=g(p)\), where \(f_i,g\in\mathbb C[t]\).
This choice can differ from a parameter for the speed field alone.
Still \(E(p)=0\). If \(p_z=0\), the good-coordinate subring is
stable and the preceding recognition endpoint applies. Suppose
\(\alpha=p_z\ne0\), and set
\[
 \begin{gathered}
 \delta=c_z,\qquad
 A_0=f'(p)\cdot\nabla_{\rm good}p,\qquad
 C_0=f'(p)\cdot\nabla_{\rm good}c,\\
 U=\begin{pmatrix}f'_1(p)&0\\f'_2(p)&0\\f'_3(p)&0\\0&1\end{pmatrix},
 \qquad V=\begin{pmatrix}dp\\dc\end{pmatrix},\qquad
 M(t)=\begin{pmatrix}t&0\\t^2g'(p)/2&t\end{pmatrix},\\
 \operatorname{Jac}(F_t)=I_4+UM(t)V,\qquad
 VU=\begin{pmatrix}A_0&\alpha\\C_0&\delta\end{pmatrix}.
 \end{gathered}
 \tag{9}
\]
In this display the differentials in \(V\) are their rows in the
original four-coordinate basis. The scalar \(\delta=c_z\) is
different from the partial-degree symbols \(\delta_j\).

The rectangular determinant identity, applied to the actual flow,
gives
\[
 \begin{gathered}
 1=\det(I_2+M(t)VU)
   =1+t(A_0+\delta)
       +t^2\bigl(A_0\delta-\alpha C_0+g'(p)\alpha/2\bigr),\\
 A_0+\delta=0,\qquad
 \delta^2=\alpha\bigl(g'(p)/2-C_0\bigr),\\
 Q=[E,T_4]=-\alpha f'(p)\cdot\partial_{\rm good}-\delta\partial_z,
 \qquad [E,Q]=0,\qquad Q(p)=0,\qquad
 Q(c)=-g'(p)\alpha/2 .
 \end{gathered}
 \tag{10}
\]
In particular \(\alpha\mid\delta^2\) with full multiplicities.
The commutator formula is direct differentiation of the original
coefficient row \((f(p),c)\).
The equality \([E,Q]=0\) follows from (3), since the good-speed rank
is one. The last two identities follow by evaluating this row on
\(p,c\) and using the two determinant coefficients.

The field \(Q\) is a nonzero LND on the actual \(B\).
Indeed \(\exp(tE)T_4\exp(-tE)=T_4+tQ\), and
\(\varepsilon\exp(\varepsilon^{-1}E)T_4
\exp(-\varepsilon^{-1}E)=\varepsilon T_4+Q\).
The latter is an LND on the Laurent extension, preserves
\(B[\varepsilon]\), and specializes to an LND at \(\varepsilon=0\).
Its nonvanishing follows from \(\alpha\ne0\) and the nonzero row
\(f'(p)\), since the speed rank is one.

Let \(d\) be a gcd of \(\alpha,\delta\) in the original polynomial
UFD, allowing \(\delta=0\). It divides every coefficient of \(Q\);
hence \(d\mid Q(d)\), and LND divisibility implies \(Q(d)=0\).
Prime multiplicities in \(\alpha\mid\delta^2\) give
\(\alpha\mid d^2\). For \(\delta=0\) this is immediate from
\(d=\alpha\) up to a unit. Otherwise, at each prime, if the orders
of \(\alpha,\delta\) are \(a,b\), then
\(a\le2b\) implies \(a\le2\min(a,b)\).
Since \(d^2\) is \(Q\)-invariant, factorial closure now gives
\[
 \begin{gathered}
 Q(\alpha)=0,\qquad E(\alpha)=0,\qquad
 Q^2x_i=0\quad(1\le i\le3),\\
 E(\delta)=g'(p)\alpha/2,\qquad Q^2(c)=0,\qquad
 Q^2z\in A.
 \end{gathered}
 \tag{11}
\]
Here \(E(\alpha)=[E,T_4](p)+T_4(Ep)=Qp=0\).
Also \(E(\delta)=Q(c)+T_4(q)=g'(p)\alpha/2\).
The second iterate on each good coordinate vanishes because
\(Qx_i=-\alpha f_i'(p)\) and \(Qp=Q\alpha=0\).
The same two invariances give \(Q^2c=0\), and commutation yields
\(E(Q^2z)=Q^2(Ez)=Q^2c=0\).

Thus the content argument of
[the constant-acceleration speed-curve note89](constant-acceleration-curve-speed-pass89.md)
extends to variable \(q=g(p)\) in this joint-curve setting.
No constant-acceleration division or invariant localization was used.
These identities do not prove \(Q^2z=0\), \(Q^3z=0\), or that
\(Q\) has a slice.

The failure of the first of these possible conclusions occurs in
an actual polynomial control. In adapted coordinates \((a,b,c_0,u)\)
take \(X=u\), \(Y=b+au\), \(Z=c_0+a^2u\), \(W=a+Y^2\).
The inverse is \(u=X\), \(a=W-Y^2\), \(b=Y-aX\),
\(c_0=Z-a^2X\), so both inverse orders are polynomial identities.
Here \(p=a=W-Y^2\), the good speeds are \((1,a,a^2)\),
and \(q=2a^2\). The actual last partial is
\(T_W=\partial_a-u\partial_b-2au\partial_{c_0}\), hence
\(Q=-\partial_b-2a\partial_{c_0}\).
It has \(Q^2W=2\), despite killing the second iterates of all three
good coordinates. This control is already recognized by \(X=u\);
it is not a residual nonpolynomial instance.

## 7. What remains in the curve case

A hypothetical nonpolynomial kernel with speed rank one must
therefore have the **unit** selected speed ideal \(I=B\).
In the quadratic joint-rank-one case it must additionally have
the exact profile (4). These two necessary conditions are compatible
with recognized examples; neither alone produces a counterexample.

The unit row does give a slice
\(\sum_i\lambda_i(p)x_i\) after choosing
\(\sum_i\lambda_i(p)f_i(p)=1\), but a polynomial slice was already
part of (1). This expression has invariant-dependent coefficients.
It has not been shown to be an ambient coordinate, nor has a
matrix in \(\operatorname{GL}_3(\mathbb C[p])\) been shown to induce
an automorphism of the original polynomial ring.
These missing implications cannot be used to close the unit-row case.

The original cofactor bound126 remains correct as a coarser statement;
this note refines it by the joint rank. The constant-acceleration
speed-curve note89 has stronger special hypotheses, notably constant
nonzero acceleration and its centered slice. Its further geometric
arguments are not imported for variable acceleration here.

The new statements use actual flows, exterior algebra, polynomial
curve factorization, univariate Bézout, and original-coordinate degree.
The determinant/content extension was also reconstructed independently
by Root; its displayed matrices are identities in the actual original
ring, not a proposed realization of arbitrary coefficient arrays.
The recognition endpoints retain the established source dependencies
just identified. No tests were run for this proof, no old note was
edited, and no unrestricted frame-entry or cancellation claim is made.
