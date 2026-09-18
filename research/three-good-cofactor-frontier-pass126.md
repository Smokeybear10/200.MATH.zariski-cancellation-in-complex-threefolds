# Cofactor bounds and the remaining joint-curve case

The working complex-threefold cancellation question remains unsolved:
\(A[u]\simeq\mathbb C^{[4]}\) has not been shown to imply
\(A\simeq\mathbb C^{[3]}\) in general. The corrected dimension and
choice of complex ground field are still unconfirmed interpretations
of the professor's email. The conclusions below concern a supplied
coordinate class, not every possible polynomial cylinder.

This investigation gives rank-sensitive bounds on conjugated coordinate
partials and recognizes two additional conditional cases. It also
isolates the exact partial-degree profile left by a one-dimensional
joint speed-and-acceleration image. The proof notes are working
mathematical deductions with separate AI reconstructions. They have
not received human expert review, formal proof verification, or
historical novelty clearance.

## 1. The actual coordinate assumptions

Throughout, the specified generators are genuine polynomial coordinates:
\[
 B=\mathbb C[x_1,x_2,x_3,z]=A[u],\qquad
 E=\partial_u,\qquad A=\ker E,\qquad E^2x_i=0.
 \tag{1}
\]
Write \(a_i=Ex_i\), \(c=Ez\), and
\(r=\operatorname{trdeg}_{\mathbb C}\mathbb C(a_1,a_2,a_3)\).
When the last coordinate is quadratic in time, also write
\(q=E^2z\in A\) and
\(s=\operatorname{trdeg}_{\mathbb C}\mathbb C(a_1,a_2,a_3,q)\).
The independent parameter is the action time, not ordinary spatial
polynomial degree.

The [intrinsic-speed theorem125](three-good-intrinsic-speed-quotient-pass125.md)
provides a nonzero intrinsic LND fixing the speeds, unless they all
vanish and the kernel is immediately polynomial. In the quadratic
case it also fixes \(q\). Its invariant-field dimension gives
\(r\le2\), and \(s\le2\) when defined. These are already established
inputs, not new consequences counted separately in this pass.

## 2. The cofactor bounds

Let \(T_j\) be an original coordinate partial and use
\([E,T]=ET-TE\). The actual flow \(F_t=\exp(tE)x\) has Jacobian
determinant one. The coefficients of its conjugated partial are
exactly the corresponding inverse-Jacobian column. The bad column
deletes the last row and therefore uses only
\(dx_i+t\,da_i\). Its coefficients of degree greater than \(r\)
vanish by alternating multilinearity.

The [full cofactor proof](three-good-flow-cofactor-bounds-pass126.md)
and [joint-rank refinement](three-good-joint-curve-bound-pass126.md)
give the following bounds on the degrees in \(t\) of
\(\exp(tE)T_j\exp(-tE)\):

| Supplied assumptions | Bad partial | Each good partial |
| --- | --- | --- |
| Three good coordinates, no last-degree bound | At most \(r\le2\) | No bound asserted here |
| Quadratic last coordinate | At most \(r\) | At most \(s+1\le3\) |
| Quadratic last coordinate, joint rank one | At most one | At most two |

For nonvertical original partials these degrees agree with their
nonnegative shifts \(d_j\) for the \(u\)-filtration. A vertical
partial already recognizes the kernel. The retained partial height is
\(H=\sum_j(d_j+1)\), so the general quadratic bound is **fifteen**,
not eleven. The [height-ten theorem73](height-ten-closure-pass73.md)
is a separate retained working recognition theorem.

## 3. Two recognition gates

First, if any original partial commutes with \(E\), its kernel is
an actual polynomial three-ring stable under \(E\), with at least
two good generators. Removing the coefficient gcd preserves local
nilpotence and both second-iterate vanishings. Wang's two-quasi
classification supplies an invariant actual coordinate in that
three-ring. It is also a coordinate of \(B\), so regularity of
\(A\) and Bhatwadekar--Gupta--Lokhande's theorem recognize
\(A\simeq\mathbb C^{[3]}\).[^dg][^bgl]

The [complete commuting-partial proof](three-good-common-leading-kernel-boundary-pass126.md)
does not assume a slice for the restricted three-variable derivation,
nor a degree bound on \(z\). This extends the explicitly recorded
bad-partial case to good partials by an existing classification.

Second, suppose \(r=1\) and the selected speed ideal
\(I=(a_1,a_2,a_3)B\) is proper. Polynomial curve factorization gives
\(a_i=f_i(p)\) for a genuine polynomial invariant \(p\), without
asserting that \(p\) is a coordinate.[^curve] If
\(h=\gcd(f_1,f_2,f_3)\), univariate Bezout gives \(I=h(p)B\).
The slice identity makes \(c=Ez\) invertible modulo \(h(p)\).
Consequently
\[
 0=E(p)=h(p)\sum_i (f_i/h)(p)p_{x_i}+c\,p_z
 \quad\Longrightarrow\quad h(p)\mid p_z.
 \tag{2}
\]
Since \(h\) is nonconstant, original \(z\)-degrees force
\(p_z=0\): a nonzero derivative has strictly smaller degree than
the polynomial of which it is the derivative, whereas
\(\deg_z h(p)\ge\deg_zp\). The actual good three-ring is then
stable and its nice derivation has an invariant linear coordinate.
The same regular-kernel theorem finishes this case.

The [nonunit speed-curve proof](three-good-joint-curve-bound-pass126.md)
needs no quadratic assumption on \(z\), no first-power acceleration
membership, and no localization of the original polynomial ring.

## 4. The exact one-parameter frontier

For a hypothetical nonpolynomial kernel in the quadratic joint-rank-one
class, the preceding gates and the height-ten theorem leave
\[
 I=B,\qquad (d_{x_1},d_{x_2},d_{x_3},d_z)=(2,2,2,1),
 \qquad H=11.
 \tag{3}
\]
These are necessary conditions, not evidence that such a counterexample
exists. Recognized polynomial examples can also have a unit speed row.

Write the joint parametrization as \(a_i=f_i(p)\), \(q=g(p)\),
and put \(\alpha=p_z\), \(\delta=c_z\). The case \(\alpha=0\)
is already recognized. Otherwise the exact two-row determinant
calculation in the [joint-curve proof](three-good-joint-curve-bound-pass126.md)
gives
\[
 \begin{gathered}
 \delta^2=\alpha\bigl(g'(p)/2-f'(p)\cdot\nabla_{\rm good}c\bigr),\\
 Q=[E,\partial_z]\in\operatorname{LND}(B),\qquad
 [E,Q]=0,\quad Qp=Q\alpha=E\alpha=0,\\
 Q^2x_i=0,\qquad Qc=-g'(p)\alpha/2,\qquad Q^2z\in A.
 \end{gathered}
 \tag{4}
\]
The invariance of \(\alpha\) is a multiplicity-sensitive content
argument: \(\alpha\mid\delta^2\) implies
\(\alpha\mid\gcd(\alpha,\delta)^2\); the LND kills that gcd,
and factorial closure finishes. The proof extends the old
constant-acceleration curve calculation to variable \(q=g(p)\).

It does not prove \(Q^2z=0\), \(Q^3z=0\), or a slice for \(Q\).
The actual polynomial frame
\(X=u, Y=b+au, Z=c_0+a^2u, W=a+Y^2\) has
\(q=2a^2\) and \(Q^2W=2\). Its inverse is polynomial and
\(X\) is an actual coordinate slice, so it is a boundary control,
not an unresolved instance.

## 5. An actual presentation for the unit-row branch

The [unit-curve normal-form proof](three-good-unit-curve-normal-form-pass126.md)
uses \(Q\) from (4) to extract more than a generic field description.
The primitive univariate normal to \(f,f'\) is a unit row, so a
split basis over \(\mathbb C[p]\) defines a slice \(\sigma\), an
invariant \(Y\), and a common invariant \(h\). It proves
\(N=Q|_A\ne0\) by the explicit nonzero derivative \(NY\).

The retained quotient theorem gives an actual embedded polynomial
plane \(S=\ker N\).[^ks] Applying the slice projection to the
actual coordinate-reconstruction equality yields
\[
 \begin{gathered}
 B=S[\sigma,Y,z],\qquad A=S[Y,d_0],\qquad
 d_0=z-\sigma c+q\sigma^2/2,\\
 K=\operatorname{Frac}S,\quad A_K=K[Y],\qquad
 A\simeq S[y,t]/(a t-F(y))=S[Y,F(Y)/a],\\
 0\ne a\in S,\quad F\in S[y],\qquad
 a\in S^*\ \Longrightarrow\ A\simeq\mathbb C^{[3]}.
 \end{gathered}
 \tag{5}
\]
The denominator \(a\) and the coefficients of \(F\) have no
common nonunit factor. The proof verifies the kernel of the
presentation by prime/Gauss saturation, not by assuming that
generic equality descends. The residual first derivative
\(c-q\sigma\) is affine-linear in \(Y\) over \(K\), with slope
in \(\mathbb C(p)\); its denominators have not been removed.

This identifies a specific affine modification of an actual polynomial
three-ring. It does not show that its denominator is a unit. Nor does
the finite field extension \(\mathbb C(p,h)\subset K\) prove that
\(p,h\) are coordinates of \(S\). Those are concrete global gaps,
not permission to substitute an invariant-coefficient matrix for an
ambient polynomial automorphism.

## 6. A tempting common-kernel shortcut is invalid

When the joint field has rank two, the leading intrinsic derivations
of all four nonvertical original partials have the same kernel.
Their invariant fields are all the relative algebraic closure of the
joint field in \(\operatorname{Frac}A\). Primitive saturation makes
them replicas of a common intrinsic LND.

This controls a selected finite collection, not all intrinsic LNDs.
The [explicit common-kernel control](three-good-common-leading-kernel-boundary-pass126.md)
has \(A=\mathbb C[a,b,c]\) and all four selected tops proportional
to \(\partial_c\), while \(A\) also has the independent translations
\(\partial_a\) and \(\partial_b\). Thus it cannot invoke a theorem
whose hypothesis quantifies over every intrinsic LND. This removes an
invalid inference; it is not a cancellation counterexample.

## 7. Verification and next mathematical obligations

The [exact capture126](verification-pass126-working.json) records six
passing methods in two suites: three new and three retained. The
new [standalone example checker](three_good_cofactor_checks_pass126.py)
imports no earlier solver or checker. It verifies both inverse
compositions, original partials, commutators, exact shifts, cofactor
orientation, rank-one wedge cancellation, and the variable-acceleration
identities including \(Q^2W=2\). Input hashes are unchanged across
the canonical run. Earlier runs are superseded, not additive coverage.

These tests check explicit polynomial examples. They do not verify
the universal proof quantifiers or the published input theorems.
The saved proof notes have separate full-file AI reconstructions.
No result is labeled historically novel or formally verified.

The remaining work has distinct scopes. The joint-curve case still
needs a global recognition argument for (3)--(5), including the
nonunit modification denominator and possible fixed points of the
extracted intrinsic action. The rank-two
joint-field case permits larger partial profiles and does not reduce
to that curve case. Finally, unrestricted cancellation still needs
an argument supplying a usable coordinate frame, or a different
approach that avoids that requirement. None of these gaps is replaced
by the numerical upper bound \(H\le15\).

The bounded source check for this pass reread exact classification
statements and the selected curve-factorization proof. It did not
reconstruct Wang's original proof, all dependencies of the regular-kernel
theorem, or the earlier geometric quotient theorem. It is not a
comprehensive current-status or novelty audit. No external contact,
submission, public posting, paid resource, or new automation occurred.

## Sources

[^dg]: Nikhilesh Dasgupta and Neena Gupta,
    [*Nice derivations over principal ideal domains*](https://arxiv.org/html/1701.03635v1),
    arXiv:1701.03635v1. Theorem 4.1 reproduces Wang's two-quasi
    classification; Theorem 3.1(i) gives the nice-three linear invariant.
    The exact former statement was freshly read, not Wang's original proof.

[^bgl]: S. M. Bhatwadekar, Neena Gupta and Swapnil A. Lokhande,
    [*Some K-theoretic properties of the kernel of a locally nilpotent derivation on k[X1,...,X4]*](https://arxiv.org/html/1501.01438v1),
    arXiv:1501.01438v1, Theorem 3.5. Its exact statement and complete
    short displayed proof were freshly read. Its hypothesis is an
    actual invariant coordinate and regular kernel.

[^curve]: Michiel de Bondt,
    [*Rational maps H for which K(tH) has transcendence degree 2 over K*](https://arxiv.org/html/1501.06046v4),
    arXiv:1501.06046v4, Corollary 3.2 and Lemma 3.3, printed pages
    20--21. Their complete selected statements and proofs were freshly
    read; the earlier Luroth dependencies were not newly reconstructed.

[^ks]: Shulim Kaliman and Nikolai Saveliev,
    [*C+-actions on contractible threefolds*](https://arxiv.org/pdf/math/0209306),
    Lemma 2.1 and Corollary 2.8, through the
    [retained intrinsic quotient-surface application](intrinsic-quotient-surface-pass.md).
    The actual application includes the required three-plane domination;
    its geometric and flatness dependencies were not freshly re-audited here.
