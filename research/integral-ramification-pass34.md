# Integral branch restrictions for additive quotients

An integral necessary condition supplements the rational component count.
For an additive quotient of affine three-space, the greatest common
divisors of the ramification indices above distinct branches of a fully
retained exceptional curve must be pairwise coprime. This does not exclude
a nodal exceptional curve: its two branches can both have gcd one.

The condition is a consequence of the established quotient homology
diagram and elementary integer lattices. No novelty or solution of
complex threefold cancellation is claimed.

## 1. The integer lattice statement

Partition a finite set of columns into nonempty groups indexed by
\(j=1,\ldots,r\). Give column \(a\) in group \(j\) a positive integer
\(e_a\). Define
\[
T:\mathbb Z^q\longrightarrow\mathbb Z^r,
\qquad T(v_a)=e_a w_j,
\qquad m_j=\gcd\{e_a:a\text{ lies in group }j\}.
\tag{1}
\]
Let \(\mathbf 1=w_1+\cdots+w_r\). Then the cokernel of the induced
map into \(\mathbb Z^r/\mathbb Z\mathbf 1\) is
\[
Q=\frac{\mathbb Z^r}{\operatorname{im}T+\mathbb Z\mathbf1}
 \simeq
 \frac{\bigoplus_{j=1}^r\mathbb Z/m_j\mathbb Z}
      {\langle(1,\ldots,1)\rangle},
\qquad
|Q|=\frac{\prod_j m_j}{\operatorname{lcm}(m_1,\ldots,m_r)}.
\tag{2}
\]
For \(m_j=1\), the corresponding summand is zero. In particular, for
one branch the quotient is always zero, including arbitrary ramification.

To prove (2), integer Bezout identities in each disjoint column group
give \(\operatorname{im}T=\bigoplus_j m_j\mathbb Z w_j\).
In the resulting finite product, the diagonal element has order exactly
the displayed least common multiple. Taking the quotient gives its order.
For each prime, equality between the sum and maximum of its valuations
in the \(m_j\) holds exactly when it divides at most one \(m_j\).
Consequently
\[
Q=0\quad\Longleftrightarrow\quad
\gcd(m_j,m_k)=1\text{ for every }j\ne k.
\tag{3}
\]
This is not a condition on every individual ramification index. For
example, indices \((2,3)\) above one branch have gcd one. Replacing that
group by a single index six changes the lattice and is invalid.

## 2. Geometric application and its hypotheses

Let \(D\) be a nonzero locally nilpotent derivation of
\(W=\mathbb C[X,Y,Z]\). Write its invariant ring as
\(C=\mathbb C[f,g]\), with quotient
\(\pi:\mathbb A^3\to\mathbb A^2\). Choose a fully retained reduced
exceptional curve \(\Gamma\) with the product-complement and finite
intermediate-curve properties of Kaliman's construction. In particular,
use the reduction in Theorem 5.2(i), not an arbitrary enlarged divisor.
The required source inputs are Proposition 3.2, including Step 2 of its
proof, and the homology diagram preceding it.[^1]

Let \(Z\to\Gamma\) be that finite intermediate curve. The normalizations
of the retained base components are affine lines. The equality of first
homology ranks in the cited Step 2 implies the same for the source
normalizations. Thus both normalizations are disjoint unions of affine
lines, before removing a finite exceptional set.

Choose a finite set \(\Sigma\) containing all singular and exceptional
values required for the diagram. Write \(\Gamma^*\) and \(Z^*\) for the
resulting smooth punctured curves. Their integral first homology groups
have bases consisting of the normalized puncture loops. There are no
additional handle or infinity classes to use to repair a failure of
surjectivity in an individual support block.

For \(b\in\Sigma\), denote by \(r_b\) the number of normalized base
branches at \(b\), and by \(q_b\) the number of source normalization
points over them. In the corresponding bases, the map on first homology
is exactly (1), with the actual ramification indices. A small three-sphere
about \(b\) maps to the diagonal sum of its \(r_b\) branch loops.

For completeness, the part of the diagram needed here has the form
\[
H_3(X^*)\longrightarrow H_1(Z^*)
 \longrightarrow H_2(\check X)\longrightarrow0,
\]
\[
H_3(Y^*)\longrightarrow H_1(\Gamma^*)
 \longrightarrow H_2(\check Y)\longrightarrow0,
\tag{4}
\]
where \(X^*=\mathbb A^3\setminus\pi^{-1}(\Sigma)\),
\(Y^*=\mathbb A^2\setminus\Sigma\), and the checked spaces are the
product complements. The right vertical map is an isomorphism. The
vanishing needed at the two right ends follows from removing complex
codimension-two sets from the contractible ambient spaces.

It follows that the map
\(H_1(Z^*)\to H_1(\Gamma^*)/\operatorname{im}H_3(Y^*)\)
is surjective. The normalized puncture bases and the sphere classes
decompose this assertion as a direct sum over \(b\). Hence each local
map is surjective modulo its diagonal class. Equations (2)-(3) imply:
\[
\gcd(m_{b,j},m_{b,k})=1\qquad(j\ne k),
\tag{5}
\]
where \(m_{b,j}\) is the gcd of the indices above branch \(j\).

If extra divisor components are retained without verifying the affine-line
normalization condition, this proof cannot simply discard their first
homology. The fully retained hypothesis is part of the argument, not a
cosmetic choice of notation.

### A single irreducible quotient fiber

There is a useful additional consequence when the reduced actual fiber
over \(b\) is irreducible. The preceding rational count gives \(q_b=r_b\).
Every base branch therefore has exactly one normalized source preimage.
If the branch belongs to a retained component of generic cover degree
\(N_j\), its ramification index is \(N_j\ge2\).

The degrees attached to these branches must be pairwise coprime by (5).
In particular, the same retained component cannot have two branches
through this point: they would repeat a degree at least two. Distinct
retained components through it have pairwise coprime cover degrees.

The transverse fiber multiplicity is exactly
\(\operatorname{lcm}(N_1,\ldots,N_r)=\prod_j N_j\).
Indeed the pointwise source Thom group is \(\mathbb Z\), and exactness
identifies its image with the full lattice
\(T^{-1}(\mathbb Z\mathbf1)\), not a finite-index sublattice.
For \(T=\operatorname{diag}(N_1,\ldots,N_r)\), this lattice has
primitive generator \((\ell/N_1,\ldots,\ell/N_r)\), where
\(\ell=\operatorname{lcm}(N_1,\ldots,N_r)\). Its image is
\(\ell\mathbf1\). A transverse complex linking sphere has positive
degree equal to the generic scheme-theoretic fiber multiplicity, proving
the assertion. The support and integral Thom identifications are those
of the [preceding branch-count proof](all-speed-ambient-obstruction-pass33.md).

The argument counts analytic branches. It does not assert that a
unibranch component is smooth, or that all irreducible quotient fibers
are affine lines.

## 3. What the obstruction does and does not say

If every branch has one source point with ramification index two, then
\[
Q\simeq(\mathbb Z/2\mathbb Z)^{r-1}.
\tag{6}
\]
This excludes such data at a point with two or more branches, provided
the geometric hypotheses above have actually been established. A single
branch with a double fiber is not excluded by this calculation.

More generally, when each branch has one point with a common index
\(n\), the quotient is \((\mathbb Z/n\mathbb Z)^{r-1}\). Different
indices such as two and three have no such cokernel. Vanishing of this
cokernel is only necessary; it constructs neither an ambient action nor
its quotient.

There is an actual positive control, not just abstract integer data.
The established crossing-plinth action in
[the intrinsic-rank note](intrinsic-rank-pass34.md) has boundary degrees
five and two at the intersection of its two invariant axes. Its local
matrix is \(\operatorname{diag}(5,2)\); the primitive column
\((2,5)^{\mathsf T}\) maps to \(10(1,1)^{\mathsf T}\).
On the transverse disc \(z=1\), its actual fiber ideal is
\((x-y^2,y^{10})\), of length ten. These coprime degrees are compatible
with the diagram. Neither a fixed fiber nor two exceptional branches
alone is an obstruction.

The fixed conductor surface from the preceding pass has four normalized
points over its nodal base value, two over each branch, all unramified.
Its local map has branch gcds one and one. Thus this integral restriction
does not rule out the node itself. The remaining possible obstruction
involves how other genuine exceptional components could meet that curve,
which additionally requires the actual fiber geometry and linking
multiplicities.

The existence of disjoint nodal polynomial curves is already recorded in
[the pass-18 exact controls](rescaling_curve_controls_pass18.py).
Disjointness of a candidate exceptional component from other components
must not be presented as an impossibility of a plane configuration.

## 4. Verification boundary

[The standalone checker](integral_ramification_checks_pass34.py) tests
integer image indices by maximal minors, the product/lcm formula,
pairwise coprimality, the common-index obstruction and node controls.
It imports no other research code. Those finite checks do not verify
the topological construction, its universal hypotheses, or cancellation.

```
/opt/anaconda3/bin/python research/integral_ramification_checks_pass34.py
```

## Source

[^1]: Shulim Kaliman, [*Free C+-actions on C3 are translations*](https://www.math.miami.edu/~kaliman/library/Ka.invent.2004.c%2B.pdf), final author version, Proposition 3.2 and its proof, especially Step 2, and Theorem 5.2(i). The integer-lattice consequence (2)-(5) is derived here; it is not quoted as the source's theorem. No freeness assumption on the whole action is made.
