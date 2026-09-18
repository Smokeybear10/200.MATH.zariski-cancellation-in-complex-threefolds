# The generic bad-coordinate pair and commuting determinant actions

In the independent-defect, degree-two residual with rank-two bad
projection, the actual bad coordinates generate the entire generic
leading fiber. This is stronger than a generically finite projection.
The good coordinates form a quadratic graph over that pair, with
coefficients in the common invariant field.

Consequently the bad-projection determinant belongs to the common
invariant ring. The two polynomial determinant actions commute
globally and each has flow degree at most two in the supplied actual
coordinates. None of these conclusions identifies the invariant plane
as an ambient coordinate plane, transfers a slice to the determinant
actions, or recognizes the original kernel.

## 1. Frozen hypotheses and inherited inputs

Retain all assumptions of
[the degree-two reduction](two-quadratic-degree-two-pass42.md) and
[the projection-rank exclusion](bad-projection-rank-closure-pass43.md).
Thus
\[
B=\mathbb C[x_1,x_2,x_3,x_4],\qquad E(s)=1,\qquad E^3x=0,
\]
the good actual partials \(T_1,T_2\) have second adjoint zero,
the bad partials have third adjoint zero, and the two tops
\(V_3,V_4\) are independent. Put
\[
A=\ker E,\quad h=E^2x=(h_1,h_2,0,0)^{\mathsf t},\quad
v=\binom f g=\binom{Ex_3}{Ex_4}.
\tag{1}
\]
We work in the remaining case
\[
\operatorname{rank}\operatorname{Jac}(f,g)
=\operatorname{rank}(L_0[V_3(x)\mid V_4(x)])=2.
\tag{2}
\]
The letter \(L_0\) selects the last two components.

Let \(C\) be the common kernel of the nonzero leading restrictions
on \(A\), and let \(L=\operatorname{Frac}C\).
The inherited intrinsic-quotient theorem already gives
\(C\simeq\mathbb C^{[2]}\) and faithful flatness of \(C\subset A\).
These are not new conclusions of this note.[^intrinsic]
The calculation below needs the common field and the already
proved local-slice chart, not a choice of ambient coordinates
generating \(C\).

After simultaneously swapping the two bad coordinate labels if necessary, the
[simultaneous chart](bad-projection-determinant-pass43.md#2-a-simultaneous-translation-chart-over-the-common-invariant-field)
is
\[
B\otimes_C L=L[r,t],\qquad
E=\partial_t,\quad V_3=\partial_r,\quad
V_4=b_4\partial_r+c_4\partial_t,\quad
b_4,c_4\in L,\ c_4\ne0.
\tag{3}
\]
This is localization at actual common invariants. In particular
\[
B\otimes_C L=L[x_1,x_2,x_3,x_4].
\tag{4}
\]
All original coordinate generators remain present.

Write the bad and good coordinate columns as
\[
x_B:=\binom{x_3}{x_4}=q(r)+t v,\qquad
x_G:=\binom{x_1}{x_2}
=X(r)+tP(r)+\frac{t^2}{2}h_G,
\tag{5}
\]
where \(q,X,P\in L[r]^2\) and \(h_G=(h_1,h_2)^{\mathsf t}\in L^2\).
Both entries of \(v\) belong to \(L\).

## 2. The actual good partials force a constant Schur complement

Since \(f,g\) are algebraically independent, \(L\) is algebraic
over \(\mathbb C(f,g)\). Characteristic zero gives unique extensions
to \(L\) of the two commuting partials with respect to \(f,g\).
Extend them further to \(L[r,t]\) by fixing \(r,t\).
Subscripts \(v\) below mean these base derivatives, and a prime
means \(\partial_r\). This introduces derivations of a field, not
an additional ambient polynomial coordinate assertion.

Put
\[
M=[q'\mid v].
\tag{6}
\]
It is invertible over \(L(r)\): in (3), the bad-component matrix
of \(V_3,V_4\) is
\([q'\mid b_4q'+c_4v]\), whose determinant is
\(c_4\det M\). Use (2).

Let \(U\) be the two-by-two matrix whose columns are
\(T_1(v),T_2(v)\). The earlier good-column identity
\(W_i(v)=0\), where \(W_i=[E,T_i]\), gives
\[
E(T_i v)=W_i v+T_i(Ev)=0.
\]
Thus \(U\in\operatorname{Mat}_2(L[r])\): it is independent of \(t\).
This does not assert that its entries belong to \(L\).

Apply \(T_1,T_2\) to the actual coordinate pair \(x_B\).
Solving for their \(r,t\) components, then applying them to \(x_G\),
gives
\[
K(t)U=I,\qquad
K(t)=X_v+tP_v+\frac{t^2}{2}(h_G)_v
-[X'+tP'\mid P+t h_G]M^{-1}(q_v+tI).
\tag{7}
\]
The right-hand identity uses \(T_i x_j=\delta_{ij}\) for the
actual good coordinates. It is not an imposed matrix ansatz.

Here \(K(t)\) has degree at most two in \(t\).
Since \(U\) is independent of \(t\) and has a right inverse
over a field, it is invertible. Therefore both positive-degree
coefficients of \(K(t)\) vanish.

Write \(H=(h_G)_v\). The quadratic coefficient is
\[
[P'\mid h_G]=\frac12 H[q'\mid v].
\tag{8}
\]
In particular
\[
P=\frac12Hq+k,\qquad Hv=2h_G,
\quad k\in L^2.
\tag{9}
\]
The linear coefficient of (7) is
\[
[X'\mid P]=R[q'\mid v],\qquad
R=P_v-\frac12Hq_v
=\frac12(d_vH)(q)+k_v.
\tag{10}
\]
In the last expression row \(i\), column \(j\) is
\(\frac12\sum_\ell\partial_j\partial_\ell h_i\,q_\ell
+\partial_jk_i\).

Differentiate \(Hv=2h_G\). Symmetry of the base partials gives
\[
\operatorname{Hess}(h_i)v=\nabla h_i,\qquad i=1,2.
\tag{11}
\]
Using the second column of (10), and then (9), yields
\[
k_vv=k.
\tag{12}
\]
Using its first column and integrating in the polynomial variable
\(r\) gives
\[
X_i=\frac14q^{\mathsf t}\operatorname{Hess}(h_i)q
+(\nabla k_i)q+\ell_i,\qquad \ell_i\in L.
\tag{13}
\]
The integration constant belongs to \(L\), since the constants
of \(\partial_r\) in \(L[r]\) are exactly \(L\).

## 3. Generation, not merely a finite bad projection

For independent variables \(\xi=(\xi_3,\xi_4)^{\mathsf t}\), define
\[
\mathcal Q_i(\xi)
=\frac14\xi^{\mathsf t}\operatorname{Hess}(h_i)\xi
+(\nabla k_i)\xi+\ell_i\in L[\xi_3,\xi_4].
\tag{14}
\]
Equations (9), (11)--(13) show, by expansion at \(\xi=q+tv\), that
\[
x_G=\mathcal Q(x_B).
\tag{15}
\]
For the quadratic coefficient, (11) gives
\(v^{\mathsf t}\operatorname{Hess}(h_i)v=2h_i\);
for the linear coefficient use (9) and (12).
Every coefficient and factor in (14) is over the invariant field.

Now use the original-generator equality (4), not only a Jacobian
calculation. All four original generators belong to \(L[x_3,x_4]\)
by (15), so
\[
\boxed{B\otimes_C L=L[x_3,x_4].}
\tag{16}
\]
The two bad coordinates are algebraically independent because
their Jacobian in \(r,t\) is \(M\), which is invertible.
Thus (16) is a polynomial two-ring over \(L\), with the genuine
bad coordinates as its generators.

The original action on this ring is
\(E=f\partial_{x_3}+g\partial_{x_4}\).
Consequently, for the actual polynomial
\[
j=gx_3-fx_4\in A,
\]
one has
\[
A\otimes_C L=L[j]=L[r].
\tag{17}
\]
In particular \(gq_1(r)-fq_2(r)\) has degree exactly one in \(r\).
An arbitrary finite polynomial covering of the transverse line
is excluded. Neither \(j\) nor a generator of \(C\) is thereby
proved to be an ambient coordinate.

## 4. The bad determinant is a common invariant

We next improve the determinant statement from a generic-fiber
fact to a polynomial invariant.

In the coordinates of (16), base differentiation of (15) gives
\[
U=(\mathcal Q_v)^{-1},\qquad
\operatorname{Jac}_x(v)=[U\mid -UN],
\quad N=\mathcal Q_\xi.
\tag{18}
\]
Both \(U\) and \(\mathcal Q_v\) have entries in \(L[x_3,x_4]\).
For \(U\), the original derivations extend to \(B\otimes_C L\)
by the quotient rule; no local nilpotence of those extensions
is needed. For \(\mathcal Q_v\), use (14).
Therefore
\[
\det U\in L^*.
\tag{19}
\]

Put \(P_G=Ex_G\). Formula (9), after replacing \(q+tv\) by
\(x_B\), is
\[
P_G=\frac12Hx_B+k,\qquad (P_G)_v=N.
\tag{20}
\]
The second equality follows by equality of the mixed base
derivatives in (14). The last two columns of the original
Jacobian \(J=\operatorname{Jac}_x(Ex)\) are consequently
\[
J_{\{3,4\}}=
\binom{H/2-NUN}{-UN}.
\tag{21}
\]
The inherited exact bad-projection identity now gives
\[
L_0\mathcal V
=2\operatorname{Jac}_x(v)J_{\{3,4\}}
=UH.
\tag{22}
\]
Since \(h_G\) has Jacobian rank two and \(f,g\) form a
transcendence basis of the common field, \(\det H\ne0\).
Define the original polynomial
\[
\Delta=\det(L_0\mathcal V).
\]
Equations (19)--(22) give \(\Delta\in L^*\).
Since an element of \(B\cap L\) is killed by \(E\) and every
intrinsic leading restriction, \(B\cap L=C\). Hence
\[
\boxed{0\ne\Delta\in C.}
\tag{23}
\]

## 5. Two global commuting determinant actions

The preceding pass already proves that the following polynomial
fields are nonzero global LNDs:
\[
K_3=(V_4x_3)V_3-(V_3x_3)V_4,\qquad
K_4=(V_4x_4)V_3-(V_3x_4)V_4.
\tag{24}
\]
On the whole ring in (16), their actions are now exactly
\[
K_3=-\Delta\partial_{x_4},\qquad
K_4=\Delta\partial_{x_3}.
\tag{25}
\]
They kill \(L\), and (23) makes their coefficients invariant.
Polynomial restriction and injectivity yield the global identities
\[
[K_3,K_4]=[E,K_3]=[E,K_4]=0,\qquad
\Delta E=fK_4-gK_3.
\tag{26}
\]
Moreover the graph (14) is quadratic in the bad coordinates, so
\[
K_i^3(x_\ell)=0\qquad(i=3,4,\ 1\le\ell\le4).
\tag{27}
\]
This is a bound on their coordinate flows, not a proved bound
on all adjoints of their coordinate partials. They are not
asserted to be nice or to have polynomial slices.

Their common kernel in \(B\) is exactly \(C\), and
\[
K_3j=f\Delta,\qquad K_4j=g\Delta.
\tag{28}
\]
Thus \(j\) is a genuine local slice of each nonzero restriction
\(K_i|_A\). More generally every nonzero intrinsic leading
restriction has \(D(j)\in C\setminus\{0\}\), because its localized
action is an LND of the actual one-variable ring \(L[j]\).
This does not assert that \(j\) is a minimal local slice or
generates the full plinth.

## 6. Remaining global denominator problem

Equations (14)--(16) describe the full generic fiber over the
already known affine-plane base \(\operatorname{Spec}C\).
They do not say that the rational coefficients of \(\mathcal Q\)
belong to \(C\). Along their denominator divisors, the bad
coordinates can acquire relations in the special quotient fibers.
No faithful-flatness argument is used to erase those relations.

Likewise, \(\Delta\) may be a nonunit of \(C\).
Dividing (25) by it only defines the displayed coordinate partials
on the generic fiber; their coefficients on the original four-ring
need not remain polynomial. No retraction \(B\to C\), free
intrinsic action, or polynomiality of \(A\) is inferred.

The new restrictions narrow the next task to these actual
quadratic-graph degenerations and admissible denominator removal.
They do not close the complete supplied profile \((1,1,2,2)\)
or unrestricted complex threefold cancellation.

## Attribution and verification boundary

The proof uses the frozen actual-frame identities and local-slice
chart linked above, plus ordinary separable field differentiation,
matrix inversion, polynomial integration and the unit group of a
polynomial ring over a field. No new classification theorem is
invoked. The inherited affine-plane and faithful-flat conclusions
are credited separately and are not needed to justify (7)--(23).

The standalone
[four-method checker](generic_bad_pair_checks_pass44.py) imports only
unittest and SymPy. Its first run passed all four methods in
0.333 seconds, with no failed assertions. It checks the rational-base
Schur coefficients and quadratic graph; the inherited actual
independent-defect frame and global determinant identities; a generic
bad pair with nonlinear common gauge but linear transverse invariant;
and a non-coordinate finite-cover control showing why a graph and
nonzero Jacobian alone do not supply (4).
These finite controls cannot replace the original-generator step (4),
prove a universal frame exists, or establish a global denominator lift.
No novelty, external expert review or proof-assistant verification
is claimed.

[^intrinsic]: The source-audited
[intrinsic quotient proof](intrinsic-quotient-surface-pass.md),
using S. Kaliman and N. Saveliev,
[*C+-actions on contractible threefolds*](https://www.math.miami.edu/~kaliman/library/KaSa.michigan.2004.quotient.pdf),
Lemma 2.1(1), Theorem 2.7 and Corollary 2.8.
The original polynomial-cylinder hypothesis supplies its domination
and contractibility premises, as reconstructed in that frozen note.
