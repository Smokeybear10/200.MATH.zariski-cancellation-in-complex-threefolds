# A proper binary parameter scheme has no generically reduced component

In the actual nonlinear supplied-good-direction branch, a proper
binary parameter ideal cannot be generically reduced on even one
of its components. This concerns the ideal of the parameters
themselves, not merely the higher-power transverse velocity ideal.

The proof first descends a hypothetical reduced component through
the faithfully flat intrinsic quotient. This makes parameter
derivatives regular at the relevant base point. A two-variable
homogeneous initial Jacobian then contradicts nilpotence.
No coefficient field is embedded in a local ring.

## 1. Exact original-action hypotheses

Retain the actual data of the
[binary descent](nice-binary-parameter-descent-pass77.md) and
[conormal reduction](binary-conormal-obstruction-pass77.md):
\[
\begin{gathered}
B=\mathbb C[x_1,x_2,x_3,w]=A[s],\qquad
E=P\cdot\partial,\quad E(s)=1,\quad E(P)=0,\\
T=\partial_w,\quad [E,[E,T]]=0,\quad Q=[T,E],\\
0\ne\delta=Q|_A=hD,\qquad
S=\ker D=\ker\delta\simeq\mathbb C[u,v],
\qquad S\subset A\text{ faithfully flat},\\
p,q\in S\text{ independent and coprime in }B,\qquad
P_i=h_i(p,q)\ (i\le3),\qquad \deg h_i=e\ge2.
\end{gathered}
\tag{1}
\]
Here E is a global locally nilpotent derivation of the actual
polynomial ring B, and s is its original polynomial slice.
The three homogeneous binary forms \(h_1,h_2,h_3\) are
linearly independent over \(\mathbb C\). This is part of
the nonlinear ternary-cone branch; it must not be dropped.
Also \(P_4\in S\), since E and Q kill all four velocities.
Set \(I=(p,q)B\), and suppose \(I\ne B\).

The retained identities needed below are
\[
\tau=(Tp,Tq)^t\in I^eB^2,\qquad
J^3=0,\qquad J=\operatorname{Jac}_x P.
\tag{2}
\]
The first is the original slice and conormal calculation,
including its scheme-theoretic unit cancellation.
The second is the
[nice-slice rank theorem](nice-slice-adjoint-rank-pass74.md),
which uses the original global slice.
No rescaled or merely localized action is substituted.

## 2. Reducedness at a component removes the parameter pole

Let \(\mathfrak n\) be any minimal prime of I. Coprimality
in the UFD B and the height theorem give
\(\operatorname{ht}\mathfrak n=2\).
Its contraction \(\mathfrak m=\mathfrak n\cap S\) is a
maximal ideal: a nonzero prime containing p,q on the plane
cannot have height one, again by coprimality.

Put \(R=S_{\mathfrak m}\) and \(L=B_{\mathfrak n}\).
The ring L is a regular local ring of dimension two.
Suppose, toward a contradiction, that the whole local
parameter fiber at this component is reduced:
\[
L/IL\text{ is reduced}.
\tag{3}
\]
Since \(\mathfrak n\) is minimal over I, this is a
zero-dimensional local ring, hence it is the field
\(k=\kappa(\mathfrak n)\). Thus \(IL=\mathfrak nL\).

The map \(R\to L\) is flat and local, hence faithfully flat.
It gives an injection \(R/(p,q)R\to L/IL\).
The source is an Artinian local complex algebra, so (3)
makes it reduced and therefore its residue field.
Consequently
\[
(p,q)R=\mathfrak mR,\qquad
\Delta=\operatorname{Jac}_{u,v}(p,q)\in R^*.
\tag{4}
\]
This is also the reduced-component descent established in the
[ramification and socle note](binary-ramification-socle-pass78.md).
It supplies regularity before an associated-graded calculation:
the unique extended derivatives \(P_{4,p},P_{4,q}\) have
Cramer's-rule denominator \(\Delta\), so belong to R and L.
No pole has been silently discarded.

## 3. The normal associated graded and the transverse rank

The two elements p,q are a regular system of parameters of L.
There is consequently the canonical graded identification
\[
\operatorname{gr}_{IL}L=k[\xi,\eta],
\qquad
\xi=\operatorname{in}(p),\quad
\eta=\operatorname{in}(q).
\tag{5}
\]
This uses the associated graded of a regular local ring, not
a choice of an embedded coefficient field.[^graded]
The residue field k need not be algebraically closed.

Let V be the two-by-four matrix with rows the ordinary
coordinate gradients of p and q. Its reduction at
\(\mathfrak n\) has rank two over k.
Here is the differential gate explicitly. The right-exact
conormal sequence at \(\mathfrak n\) has middle term
\(\Omega_{B/\mathbb C}\otimes_B k\simeq k^4\) and final
term \(\Omega_{k/\mathbb C}\), of dimension two because
\(\operatorname{trdeg}_{\mathbb C}k=2\) in characteristic
zero. Its first term
\(\mathfrak nL/(\mathfrak nL)^2\) has dimension two.
The image is the two-dimensional kernel of the last map,
so this conormal map is injective. The parameter classes
of p,q form its basis, proving the asserted rank.

The fourth column of V is \(\tau\), which reduces to zero
by (2). Hence, if \(V_{\mathrm{tr}}\) denotes its first
three columns and \(V_0\) their residues, then
\[
V_0\in\operatorname{Mat}_{2\times3}(k),\qquad
\operatorname{rank}_k V_0=2.
\tag{6}
\]
This is a rank of the actual transverse ordinary derivatives,
not an assumed choice of two normal coordinate partials.

## 4. The first nonzero homogeneous matrix

Over \(\operatorname{Frac}B\), form the four-by-two matrix
U with rows \((P_{i,p},P_{i,q})\), and put \(C=VU\).
All entries now belong to L by (4).
The chain rule gives \(J=UV\), and U and V have rank two.
For U, two nonproportional homogeneous binary outputs of the
same positive degree are algebraically independent by scaling;
their ordinary Jacobian has rank two in characteristic zero.
Thus \(J^3=UC^2V=0\) implies \(C^2=0\).

Write \(\mathcal H=(h_1,h_2,h_3)^t\). Splitting off the
fourth column gives the exact expression
\[
C=V_{\mathrm{tr}}\operatorname{Jac}_{p,q}\mathcal H
  +\tau(P_{4,p},P_{4,q}),\qquad C^2=0.
\tag{7}
\]
Every entry of the first product has ideal order at least
e-1; the second product has ideal order at least e.
Under (5), the degree-(e-1) part is therefore exactly
\[
C_0=V_0\operatorname{Jac}_{\xi,\eta}\mathcal H(\xi,\eta)
    =\operatorname{Jac}_{\xi,\eta}G,\qquad
G=V_0\mathcal H(\xi,\eta),\qquad C_0^2=0.
\tag{8}
\]
To see the final identity, take the degree-(2e-2) part of
the exact equality \(C^2=0\). Higher-order terms cannot
contribute to that degree. The scalar entries of V0 are
coefficients in k in this graded algebra. They are not
being differentiated as functions on a lifted local chart.

Both entries \(G_1,G_2\) are homogeneous of degree e and
linearly independent over k. Indeed, the coefficient matrix
of \(h_1,h_2,h_3\) has rank three over \(\mathbb C\);
one nonzero complex three-by-three minor remains nonzero
over k. Hence \(k^3\to k[\xi,\eta]\), sending a row to
its combination of the h_i, is injective. The two
independent rows of V0 remain independent after this map.

## 5. Homogeneous binary nilpotence is incompatible with those rows

For completeness, over any characteristic-zero field k,
two nonzero homogeneous polynomials F,G of the same
positive degree e with zero Jacobian determinant must
be proportional over k.
Euler's two identities give
\[
\begin{aligned}
0&=\eta\det\operatorname{Jac}(F,G)
  =e(F_\xi G-FG_\xi),\\
0&=\xi\det\operatorname{Jac}(F,G)
  =e(FG_\eta-F_\eta G).
\end{aligned}
\tag{9}
\]
Thus both derivatives of F/G vanish in \(k(\xi,\eta)\).
The constants of these two ordinary partials are exactly k:
view a rational function first in \(k(\eta)(\xi)\), where
a zero \(\xi\)-derivative in characteristic zero makes it
belong to \(k(\eta)\), and then use its zero
\(\eta\)-derivative. Therefore \(F/G\in k\).
If either polynomial is zero, dependence is immediate.

From (8), \(\det C_0=0\), so (9) applies to \(G_1,G_2\).
It contradicts their proven k-linear independence.
This excludes (3) at every minimal prime of I.

## 6. Exact conclusion and remaining possibilities

The established original-action restriction is
\[
\boxed{\,
B_{\mathfrak n}/(p,q)B_{\mathfrak n}
\text{ is nonreduced for every minimal prime }
\mathfrak n\supset(p,q)B.\ }
\tag{10}
\]
In particular the parameter ideal is not radical. This is
stronger than observing that the transverse velocity ideal
contains powers of p,q. The latter nonreducedness would be
compatible with a reduced parameter ideal and is not the
argument proved here.

Equivalently, the two-by-two minors of the ordinary matrix
\(\operatorname{Jac}_x(p,q)\) vanish on every irreducible
component of the parameter zero set, hence lie in
\(\sqrt{(p,q)B}\). Indeed, rank two at such a generic
point would make the two conormal parameter classes a
basis and give \((p,q)B_{\mathfrak n}=\mathfrak nB_{\mathfrak n}\),
the excluded reduced case.

The conclusion does not show that
\(\operatorname{Jac}_{u,v}(p,q)\) vanishes at every base zero.
A nonreduced component upstairs can remain when the
parameter map on S is étale, because the intrinsic
quotient fiber itself need not be reduced.
Nor does (10) exclude the proper parameter ideal, give an
upper bound on h, or imply primitive fixed-point-freeness.
Those are separate remaining gates.

No new numerical method, regression, historical novelty,
human expert review or formal verification is claimed.
Frozen passes through77 and shared metadata remain unchanged.

[^graded]: The Stacks Project, [Lemma 10.106.1, Section 00NN](https://stacks.math.columbia.edu/tag/00NN), whose complete displayed statement and proof were freshly read. The canonical map from the polynomial ring on the parameter classes to the associated graded is an isomorphism. The use here requires only that result; no coefficient-field embedding or algebraic closure of the residue field is asserted.
