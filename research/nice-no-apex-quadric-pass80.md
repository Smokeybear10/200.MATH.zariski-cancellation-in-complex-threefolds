# The no-good velocity cone has a nondegenerate quadratic equation

In an actual complex four-variable nice sliced action, absence of a
nonzero constant good direction forces the homogeneous velocity cone
to be a rank-four quadric. The new input is the full pair-incidence
statement for GN-planes, not the previously used corollary that gives
only a containing hyperplane. An elementary projective line argument
turns that incidence statement into a quadratic equation.

Consequently the primitive normal row is unimodular over the actual
common invariant plane. This removes its proper-zero cases in this
branch, but does not by itself recognize the kernel or construct an
ambient invariant coordinate.

## 1. Actual hypotheses and the source gate

Let
\[
B=\mathbb C[x_1,x_2,x_3,x_4],\qquad
E=P\cdot\partial\in\operatorname{LND}(B),\qquad
E(s_*)=1,\quad E(P)=0,
\quad G_2=\{c\in\mathbb C^4:J^2c=0\}=0,
\qquad J=\operatorname{Jac}_xP.
\tag{1}
\]
The [rank74](nice-slice-adjoint-rank-pass74.md) and
[leading76](nice-leading-boundary-pass76.md) results give
\(J^3=0\), \(\operatorname{rank}J=2\), \(J^2\ne0\), and
\(P\notin\operatorname{im}J\). With \(d=\max_i\deg P_i\), put
\[
\mathcal H(x,z)=(z^dP(x/z),0),\qquad
W=\overline{\mathcal H(\mathbb C^5)}
=V(F)\times\{0\},\qquad \operatorname{rank}\operatorname{Jac}\mathcal H=3.
\tag{2}
\]
Here F is the irreducible homogeneous equation of the velocity cone
in the actual four-dimensional hyperplane. Only the elementary
pre-classification portion of the leading76 argument is needed:
the full homogenized Jacobian has rank three because
\(\operatorname{rank}[J\mid P]=3\). The slice makes the velocity
row a unit ideal, so \(V(\mathcal H)\subseteq\{z=0\}\).
At z=0 at least one component is a nonzero degree-d leading form,
by the choice of d, whence \(\dim V(\mathcal H)\le3\).
The highest flow coefficient gives \(\mathcal H(\mathcal H)=0\),
so the three-dimensional irreducible image closure W lies in
\(V(\mathcal H)\) and is one of its components. It is a conical
hypersurface in the four-dimensional hyperplane, giving F.
There may be other components; only their finite number is used.
Neither the later Corollary 6.4 classification of those components
nor its Lemma 6.1 input is needed for this pass80 incidence argument.

The [apex76 identity](nice-leading-apex-pass76.md) gives
\[
G_2=\{c\in\mathbb C^4:T_cF=0\}.
\tag{3}
\]
That identity uses the rank-three annihilator, homogeneity and
the equation F of W, not a classification of the other components.
Thus the projective surface \(X=\mathbb P(V(F))\subset\mathbb P^3\)
is not a plane and is not a projective cone with a vertex point.
Such a vertex would give a nonzero translation-apex vector of the
affine cone, hence a nonzero element of (3).

De Bondt's Theorem 3.8(i) states that for a homogeneous complex
quasi-translation with \(2\le\operatorname{rank}\operatorname{Jac}
\mathcal H\le(n+1)/2\), any two points of its image closure lie
in GN-planes which intersect nontrivially. A GN-plane is a
two-dimensional linear subspace of \(V(\mathcal H)\). Here n=5
and the rank is exactly three, so its hypotheses hold.[^gn]

Remove from W its intersections with the other irreducible components
of \(V(\mathcal H)\), and remove the origin. This leaves a dense
conical open set. Any GN-plane through one of these points lies in W:
an irreducible plane in the finite union of zero-set components lies
in one component, and W is the only component through that point.
Projectivizing gives a dense open \(X^\circ\subset X\) with
\[
\begin{gathered}
\text{for every }p,q\in X^\circ\text{ there are lines }
L_p,L_q\subset X,\\
p\in L_p,\qquad q\in L_q,\qquad L_p\cap L_q\ne\varnothing.
\end{gathered}
\tag{4}
\]
This is the entire published geometric input needed below. In
particular we do not apply the five-variable theorem requiring
absence of all linear invariants: z is already invariant here.

## 2. An elementary projective incidence lemma

We prove that an irreducible surface \(X\subset\mathbb P^3\) which
is neither a plane nor a cone, and which satisfies (4) on a dense
open, is a nonsingular quadric surface.

The set \(\mathcal F(X)\) of lines contained in X is a closed
projective algebraic subset of \(\operatorname{Gr}(2,4)\): substitution
of two spanning vectors into the homogeneous equation of X and
vanishing of every binary coefficient is the defining condition.
We use its reduced structure. There are finitely many irreducible
components, and the usual closed point-line incidence subset is
projective over either factor.

First, only finitely many lines of X pass through any point p.
Otherwise the projective family of such lines has positive dimension.
Its union is closed and has dimension at least two, since distinct
lines through p meet nowhere else. The union is therefore all X.
Every point of X would lie on a line joining it to p, making X a
cone with vertex p, contrary to hypothesis.

It follows that every positive-dimensional irreducible component
\(C\subset\mathcal F(X)\) is a curve, and its incidence surface
\[
\mathcal I_C=\{(L,p):L\in C,\ p\in L\}
\longrightarrow X
\tag{5}
\]
is surjective and generically finite. Indeed \(\mathcal I_C\) is
an irreducible projective line bundle over C, its fibers over X
are finite, and its image is closed. Infinitely many distinct
lines cannot be contained in a curve. Thus its image has dimension
two, so is X, and \(\dim C=1\). At least one such component exists
because (4) covers a dense open with lines; finitely many isolated
lines cannot do so.

We need one elementary observation. If every pair of lines in an
irreducible curve family C intersects, the lines are either all in
one plane or all through one point. Choose two distinct members
\(L_1,L_2\), their intersection p, and their spanning plane \(\Pi\).
A line meeting both is either contained in \(\Pi\) or passes
through p. These are two closed conditions on C, so irreducibility
puts all of C in one of them. Since the family covers X, either
possibility contradicts the present hypotheses on X.

The map (5) has generic degree one. If a general point lay on two
distinct members of C, the off-diagonal point-line-pair incidence
would have a component of dimension two dominating X. Its map to
\(C\times C\) has fibers of size at most one, since two distinct
lines have at most one intersection point. Its image is consequently
dense in the irreducible two-dimensional \(C\times C\). Intersection
of two projective lines is a closed condition on the Grassmannian.
Every pair in C would intersect, contradicting the observation.
Here characteristic zero ensures the usual generic-degree statement
counts distinct points after restricting to a suitable dense open.

There must be at least two distinct curve components C and D of
\(\mathcal F(X)\). If C were the only one, after removing the
isolated lines and the exceptional locus of (5), a point of
\(X^\circ\) would lie on exactly one line, belonging to C.
Equation (4) would then force generic pairs of members of C to
intersect. Closedness would again make every pair intersect,
contradicting the same observation.

For two distinct covering components C and D, every member of C
meets every member of D. To prove this, take the point-line-pair
incidence over a dense open of X where both families have their
unique line and these two lines are distinct. Such an open exists
because distinct projective curves C,D have only finitely many
common line parameters. This incidence has dimension two and
maps with fibers at most one to \(C\times D\). Its image is dense,
and intersection is closed, proving the assertion.

There exist three pairwise skew lines in C. The set of intersecting
pairs is a proper closed subset of \(C\times C\), by the elementary
observation. Choosing a point of the intersection of the three
nonempty open conditions in the irreducible \(C^3\) gives the
desired triple. Every line of D meets all three.

Here is an explicit coordinate calculation for the final step.
Use the first two skew lines to write \(\mathbb C^4=A\oplus B_0\),
with each summand two-dimensional. The third line is the graph
of an isomorphism \(A\to B_0\); after choosing bases it is the
diagonal. A line meeting both summand lines is spanned by
\((a,0)\) and \((0,b)\). It meets the diagonal exactly when a and
b are proportional. Every such line is therefore contained in
\[
\{[s a_1:s a_2:t a_1:t a_2]:[s:t],[a_1:a_2]\in\mathbb P^1\}
=V(X_1X_4-X_2X_3)\subset\mathbb P^3.
\tag{6}
\]
The lines of D cover X, so X is contained in this irreducible
quadric. Both have dimension two, hence they are equal. The
displayed quadratic form has rank four. This completes the lemma
without assuming smoothness or normality of X at the outset.

## 3. Consequences in the original action

Applying the lemma to (4) proves
\[
\boxed{\deg F=2,\qquad \operatorname{rank}\operatorname{Hess}F=4.}
\tag{7}
\]
Thus an actual constant change of four-coordinate frame puts the
homogeneous velocity relation in the determinant form in (6).
This is a quadratic equation for the velocity cone, not a bound
on the polynomial degrees of the four components of P.

The [common-highest-field note79](nice-common-top-normal-identity-pass79.md)
supplies the actual faithfully flat plane \(S=\mathbb C[u,v]\subset B\),
with P in \(S^4\) and \((P_1,P_2,P_3,P_4)S=S\). Let
\[
n=\nabla F(P),\qquad N\cdot q=\det[P,P_u,P_v,q].
\qquad (n_1,n_2,n_3,n_4)S=S.
\tag{8}
\]
The unit-row assertion follows because \(\nabla F(P)\) is an
invertible constant matrix times P. Both n and N annihilate the
rank-three matrix \([P,P_u,P_v]\), so \(N=g n\) over
\(\operatorname{Frac}S\). A Bezout row for n gives \(g\in S\).
The primitive normal row is therefore n up to a complex unit.
The unnormalized N may retain a nonconstant scalar g; (8) does
not assert that the ideal of N itself is the unit ideal.

As before, \(c=n\cdot x\) belongs to S: E and the common highest
field R kill both its coefficients and its value. The assertion
for R uses \(R(x)\in\operatorname{im}J\), annihilated by n.
Choose a polynomial row of coefficients \(a\in S^4\) with
\(n\cdot a=c\). Then
\[
n\cdot(x-a)=0\text{ in }B,\qquad (n_1,n_2,n_3,n_4)S=S.
\tag{9}
\]
These are global regular statements in the actual common plane.
They do not assert that its inclusion admits a retraction, that
the common highest intrinsic field is free, or that an S-linear
combination of ambient coordinates is an ambient coordinate.

## 4. Source scope and a nonslice boundary

Theorem 3.8(i) does not impose a global slice. Its published
Example 1.3(a2), after setting the fifth variable to one, is
\[
a=x_1x_4-x_2x_3,\qquad
P=(a x_1-x_2,\ a(a x_1-x_2),\ a x_3-x_4,\ a(a x_3-x_4)).
\tag{10}
\]
The author states this is a nonhomogeneous four-variable
quasi-translation. Its homogeneous velocity relation is the
rank-four determinant quadric. To check equality with that cone,
write \(A_0=a x_1-x_2\), \(B_0=a x_3-x_4\).
On \(A_0\ne0\) the identities
\(x_3=(a+B_0x_1)/A_0\), \(x_2=ax_1-A_0\),
\(x_4=ax_3-B_0\) show that a, \(A_0\), \(B_0\) are
algebraically independent. Its image consequently has dimension
three and is dense in the displayed irreducible quadric cone.
It has a zero at the origin,
so it has no global slice. This prevents replacing (7) by a
contradiction based only on the abstract quasi-translation or
no-apex geometry. No assertion about its Jacobian rank being
that of a sliced action is needed here.

The published Hesse theorems require an actual gradient/Hessian
representation, which the common-top79 argument does not supply.
The source's no-linear-invariant five-variable case is also
unavailable because the homogenizing coordinate is invariant.
The useful additional input here is precisely (4), with the
generic-component restriction included, followed by the complete
incidence argument above. No exact literature novelty claim,
kernel recognition, arbitrary nice-frame theorem, numerical
suite, human expert certification or formal verification is
asserted. Files through79 and shared metadata are unchanged.

[^gn]: Michiel de Bondt, [*Homogeneous quasi-translations in dimension 5*](https://arxiv.org/html/1501.04845v3), arXiv:1501.04845v3, October 18, 2017, Theorem 3.8(i), Definition 3.7, and Remark 3.11, printed pages 13--18. The complete displayed Theorem 3.8 statement/proof and Lemmas 3.1--3.4 with their displayed proofs were freshly read in the [retained primary text](../tmp/pdfs/bondt-1501.04845v3.txt); the exact statement, relevant proof and Example 1.3(a2) were also checked in primary HTML. The bounded deduction only needs part (i), not parts (ii)--(iii), the no-linear-invariant classification, or all deeper cited algebraic-geometry proofs. [Published article](https://doi.org/10.1007/s13366-017-0358-2).
