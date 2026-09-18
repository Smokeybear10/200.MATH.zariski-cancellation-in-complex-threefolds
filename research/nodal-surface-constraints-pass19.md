# Actual surface constraints for the two-nodal plinth candidate

The candidate is not excluded. There is, however, a stronger necessary
condition on the actual quotient fibers: the four-branch degree-two
intermediate curve from pass 18 would require exactly three disjoint
contractible irreducible curves above each node. An intersecting tree
of three curves cannot occur there. Scheme-theoretic multiplicities
and unibranch singularities remain possible.

This is a conditional deduction for a hypothetical primitive LND on
\(X=\mathbb C^3\), not a construction of that LND or a novelty claim.

## 1. Setup and exact source dependencies

Write \(\pi:X\to S=\mathbb A^2_{u,v}\),
\(F=v^2-u^3+3u\), and suppose the retained exceptional curve is
\(\Gamma=\Gamma_+\sqcup\Gamma_-\), where
\(\Gamma_\pm=V(F\mp2)\). Put \(E_i=\pi^{-1}(\Gamma_i)\).
The previously documented primitive support identification is needed
to identify this retained curve with the hypothetical plinth support.

The primary input is [Kaliman's final author version](https://www.math.miami.edu/~kaliman/library/Ka.invent.2004.c%2B.pdf):
Lemma 2.1 gives irreducible reduced exceptional surfaces and
one-dimensional fibers; Lemma 2.2 gives \(E\to Z\to\Gamma\)
and a product over suitable punctured curves. Proposition 3.2 gives
finiteness, its exact homology diagram, the one-point condition over
nodes, and the normalization-homology comparison in Step 2. Remark
3.3 gives surjectivity. We use these with smooth contractible
\(X=\mathbb C^3\) and smooth \(S=\mathbb C^2\), so all their
ambient hypotheses hold. No freeness assumption from Proposition
4.2(ii) is imported.

Choose a finite set \(\Sigma\subset\Gamma\), including both nodes,
so that \(\Gamma^*=\Gamma\setminus\Sigma\), \(Z^*\), and
\(E^*\cong Z^*\times\mathbb A^1\) have the properties used in
Kaliman's diagram. Write \(X^*=X\setminus\pi^{-1}(\Sigma)\).
Step 2 shows that \(H_1(Z^{\rm norm},\mathbb Z)=0\), since
\(\Gamma^{\rm norm}\) is two affine lines. Each irreducible
\(Z_i\) therefore also has affine-line normalization.

## 2. The actual fiber-component count

For \(b\in\Sigma\), let \(L_b=\pi^{-1}(b)_{\rm red}\),
let \(c_b\) count its irreducible components, and let \(q_b\)
count points of \(Z^{\rm norm}\) above \(b\). Thus \(q_b\)
counts normalization branches, not just points of \(Z\).
There are no isolated zero-dimensional fiber components: the two
invariant coordinate equations have height two in the regular
three-variable ring and form a complete intersection of pure
dimension one.

Relative homology in the smooth real six-manifold \(X\) gives

\[
H_3(X^*)\cong H_4(X,X^*)
 \cong\bigoplus_{b\in\Sigma}\mathbb Z^{c_b},
\qquad H_2(X^*)=0.
\tag{1}
\]

One can verify the second isomorphism without a smoothness assumption
on \(L_b\): remove its finite singular/intersection set first.
Removing those real codimension-six points does not change the
relevant relative degrees. Thom's isomorphism along the remaining
smooth curves then identifies degree four with their degree-zero
homology, one generator per irreducible component.

Kaliman's diagram consequently has the exact row

\[
0\longrightarrow H_3(X^*)\xrightarrow{\varphi'}H_1(Z^*)
 \longrightarrow H_2(S\setminus\Gamma)\longrightarrow0.
\tag{2}
\]

All groups \(H_1(Z^*)\) and \(H_1(\Gamma^*)\) have bases
consisting of finite puncture loops on their affine-line
normalizations. The base row and Lemma 3.1 give

\[
H_2(S\setminus\Gamma)\cong\mathbb Z^2,
\tag{3}
\]

one generator per node: its two branch loops become negatives of
one another. At a smooth point of \(\Sigma\), its single branch
loop becomes zero. A normalized source loop maps to the corresponding
base loop times its positive ramification index.

The excision-support argument in Proposition 3.2 localizes the
\(b\)-summand of (1) to the puncture loops above \(b\). The kernel
in (2) is therefore a direct sum over \(b\). Its rank is \(q_b\)
at a smooth point and \(q_b-1\) at a node. Hence

\[
\boxed{c_b=q_b\text{ at smooth points of }\Gamma,
\qquad c_b=q_b-1\text{ at its nodes}.}
\tag{4}
\]

This counts actual components of the ambient quotient fiber, not
components of an abstract proposed curve map. Integral surjectivity
in (2) also requires the ramification indices over each node,
taken across both branches, to have greatest common divisor one.
The four-branch degree-two control has all these indices equal to
one and satisfies that necessary condition.

## 3. Euler characteristic forces zero fiber deficits

For any reduced affine complex curve \(L\) with \(c\)
irreducible components,

\[
\chi_c(L)\le c.
\tag{5}
\]

Indeed its normalization is a disjoint union of smooth affine
curves, each with Euler characteristic at most one. Identifying
\(r\) normalization points over a singular point decreases
Euler characteristic by \(r-1\). Equality in (5) holds precisely
when every normalized component is \(\mathbb A^1\) and every
singular point has one branch. In particular distinct irreducible
components cannot intersect. Each component is then topologically
contractible, since its finite bijective normalization is a
homeomorphism. It need not be algebraically smooth.

For each of the two exceptional surfaces, additivity and
\(E_i^*\cong Z_i^*\times\mathbb A^1\) give

\[
\chi_c(E_i)=1-\sum_{b\in\Sigma\cap\Gamma_i}q_b
             +\sum_{b\in\Sigma\cap\Gamma_i}\chi_c(L_b)
           =\sum_{b\in\Sigma\cap\Gamma_i}
                    \bigl(\chi_c(L_b)-c_b\bigr)\le0.
\tag{6}
\]

The second equality uses (4) and the fact that \(\Gamma_i\)
has exactly one node. On the other hand, each nodal affine cubic
has Euler characteristic zero. Therefore
\(\chi_c(S\setminus\Gamma)=1\). The global product
\(X\setminus E\cong(S\setminus\Gamma)\times\mathbb A^1\)
and \(\chi_c(X)=1\) force

\[
\chi_c(E_+)+\chi_c(E_-)=0.
\tag{7}
\]

Every summand in (6) is nonpositive. Equations (6)-(7) imply that
every one is zero. Thus every exceptional fiber is a disjoint union
of unibranch polynomial curves, each with affine-line normalization.
Points not initially in \(\Sigma\) already have the asserted
description by the product construction, or may be included in a
larger \(\Sigma\). Nilpotents and fiber multiplicities are not
detected by this argument.

In particular, for the pass-18 four-branch degree-two model,

\[
L_{(1,0)}=C_1\sqcup C_2\sqcup C_3,
\qquad \chi_c(C_j)=1,
\tag{8}
\]

and the same requirement holds at \((-1,0)\). Three intersecting
lines, for example, fail (8). Three disjoint affine lines pass it.

## 4. Additional ambient surface constraints

The compact-support exact sequences for \(\Gamma\subset S\),
the product complement, and \(E\subset X\) give
\(H_c^3(E)=\mathbb Z^2\), \(H_c^4(E)=\mathbb Z^2\), and
all other compact-support cohomology groups zero. Here
\(H_c^1(\Gamma)=H_c^2(\Gamma)=\mathbb Z^2\), and multiplication
by the affine-line factor shifts compact-support degree by two.
Since the two irreducible surfaces are disjoint and (6)-(7) give
\(\chi_c(E_i)=0\), individually they must satisfy

\[
H_c^3(E_i,\mathbb Z)=\mathbb Z,
\qquad H_c^4(E_i,\mathbb Z)=\mathbb Z,
\qquad H_c^j(E_i,\mathbb Z)=0\quad(j\ne3,4).
\tag{9}
\]

Moreover each entire node fiber belongs to \(\operatorname{Sing}E_i\).
If \(U,V\in\mathbb C[X]\) denote the invariant coordinates,
the exceptional equation is \(F(U,V)\mp2\). Both partial
derivatives of \(F\) vanish at the appropriate node, so the
chain rule makes its differential zero at every point above it.
Reducedness of \(E_i\) does not imply reducedness of these
scheme-theoretic fibers.

## 5. Why there is still no contradiction

Kaliman's one-point condition says that \(\theta^{-1}(b)\)
is a singleton at a node; it does not say that the special fiber
\(\kappa^{-1}(\theta^{-1}(b))\) is connected. In Lemma 2.2,
\(\kappa\) is the restriction of a proper Stein-factor map
to the affine exceptional surface. Deleting the boundary can
disconnect a special fiber. Thus three disjoint curves above one
intermediate point do not contradict the quoted construction.

The missing realization problem is now more constrained: construct,
or rule out, two disjoint irreducible reduced hypersurfaces in
\(\mathbb C^3\), with the product quotient complement, satisfying
(4), (8), (9), the required normalization gluing, and the LND
identities. The finite curve model alone supplies none of these
surfaces. Euler characteristic and the checked integral homology
constraints presently impose these requirements but do not exclude
the degree-two case.
