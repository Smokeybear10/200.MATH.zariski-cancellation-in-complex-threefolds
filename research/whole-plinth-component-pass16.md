# A slice excludes whole plinth components

Let \(R=\mathbb C^{[3]}\), let \(0\ne D\in\operatorname{LND}(R)\),
and put \(C=\ker D\). Let \(p_D\) generate the principal
plinth ideal \(P_D=D(R)\cap C\). For invariant coefficients
\(A,B\in C\), the extension
\[
E=AD+B\partial_t\quad\text{on }R[t]
\tag{1}
\]
satisfies the necessary condition
\[
E\text{ has a slice}\quad\Longrightarrow\quad
\gcd_C(B,p_D)=1.
\tag{2}
\]
The conclusion excludes a common irreducible curve component. It is
not the stronger assertion \((B,p_D)C=C\): isolated intersection
points are not excluded by the geometric argument below.

If all higher image ideals \(D^j(R)\cap C\) are principal, then
(2), together with the higher-image torsion argument, does imply
that every slice of (1) has an affine-in-\(t\) replacement. This
last statement is conditional on principality of all higher image
ideals, not merely of the plinth ideal. Section 6 applies the
published rank-at-most-two freeness result, preserving the exact
source-access boundary of that input.

## 1. Precise source inputs

Use the final author version of
[Kaliman, *Free C+-actions on C3 are translations*](https://www.math.miami.edu/~kaliman/library/Ka.invent.2004.c%2B.pdf),
not an earlier arXiv version. Its Theorem 5.2(i), Lemma 2.2, and
Proposition 3.2 supply an exceptional curve \(\Gamma\subset S\),
where \(S=\operatorname{Spec}C\), a product outside \(\Gamma\),
and a finite factorization over \(\Gamma\). All retained curve
components have nonbijective restrictions of the finite map.

For this particular factorization, nonbijective implies nonbirational.
This is explicitly justified by Step 1 of Proposition 3.2 and invoked
in the last paragraph of Proposition 4.2. It is not a general fact
about finite maps of singular curves. Proposition 4.2's proof also
supplies the local transversal argument at a free point and the
ramification contradiction used in Section 3 below.

The invariant ring \(C\cong\mathbb C^{[2]}\) and principality
of \(P_D\) are the exact three-variable results recalled in
[Freudenburg, Theorem 2.4](https://arxiv.org/pdf/2108.12021).
The argument below uses Kaliman's stated hypotheses only with
\(X=\mathbb A^3\), so smoothness, factoriality, vanishing of
\(H_2,H_3\), and smoothness of \(S\) all hold.

## 2. Primitive actions: the retained curve is the plinth support

First assume \(D\) is primitive: its three coefficients in a
polynomial coordinate system of \(R\) have no common nonunit
factor. Choose \(\Gamma\) as in Theorem 5.2(i). Then
\[
V(P_D)=\Gamma
\quad\text{as reduced closed subsets of }S.
\tag{3}
\]
This statement concerns that retained exceptional curve, not an
arbitrary enlarged curve used to start a local-slice construction.

Since \(C\) is a polynomial plane, write \(\Gamma=V(f)\)
with \(f\in C\) reduced, or \(f=1\) if \(\Gamma\) is empty.
The product outside \(\Gamma\) gives
\[
R_f=C_f[s].
\tag{4}
\]
The localized derivation kills \(C_f\). Local nilpotence on the
one-variable ring in (4) forces
\[
D=a\partial_s,\qquad 0\ne a\in C_f.
\tag{5}
\]
Indeed a coefficient of positive degree in \(s\) would make all
iterates on \(s\) nonzero, by their leading terms.

The element \(a\) must be a unit of \(C_f\). Otherwise, choose
an irreducible factor \(q\in C\) of its numerator not dividing
\(f\). Then (5) shows that \(q\) divides \(D(x_i)\) in
\(R_f\) for every original coordinate \(x_i\).

The kernel \(C\) is factorially closed in \(R\): derivation
degree is additive on nonzero products, so an invariant product
has invariant factors. Thus an irreducible element of \(C\)
remains irreducible in \(R\), whose units are the same nonzero
constants. Also \(q\) and \(f\) remain coprime in \(R\).
Clearing the localization denominator therefore shows that \(q\)
divides every \(D(x_i)\) already in \(R\), contradicting
primitivity.

Consequently \(s/a\in R_f\) is a slice. Clear its denominator:
some \(f^N(s/a)\) belongs to \(R\) and has derivative \(f^N\).
Hence \(f^N\in P_D\), which proves
\[
V(P_D)\subseteq\Gamma.
\tag{6}
\]
This excludes even isolated plinth points outside \(\Gamma\),
not merely generic points of divisors.

For the opposite inclusion, let \(\Gamma_i\) be a retained
component. The finite map over it is nonbirational, hence has
generic degree at least two. The factorization's general fibers
therefore give at least two disjoint affine lines in a general
fiber of \(X\to S\) over \(\Gamma_i\).

If some \(p\in P_D\) did not vanish identically on
\(\Gamma_i\), then \(R_p=C_p[u]\) would make those general
fibers single affine lines. This contradiction proves
\(\Gamma_i\subseteq V(P_D)\) for every component and completes
(3). The upgrade from nonbijective to generic degree at least two
is essential here; the precise source input in Section 1 supplies it.

## 3. Every retained component meets the fixed-point image

For each \(\Gamma_i\), there is a \(D\)-fixed point whose
image in \(S\) lies on \(\Gamma_i\).

Here is the exact local use of Kaliman's proof. The retained finite
curve map has a ramification point of order \(m\ge2\), as used
in the last paragraph of Proposition 4.2. Above that point choose
a general point of the relevant one-dimensional fiber of the
intermediate map and a smooth transverse surface germ. If the
action is free at that point, the first paragraph of the proof
makes the restricted quotient map on the surface germ biholomorphic.
But its last paragraph makes that same map at least \(m\)-sheeted,
a contradiction.

The point and transverse-degree assertion here are the ones used
for Kaliman's actual intermediate map. We do not replace that
point by an arbitrary ramification point on a normalization of a
singular intermediate curve. Such an interchange would require
additional control of the branches reached by the intermediate
map, and is not inferred from abstract finiteness.

The first paragraph requires only freeness at the chosen point:
the vector field stays nonzero in a neighborhood, giving the local
transversality used there. Smoothness of the quotient at general
points of the exceptional surface comes from Lemma 4.1 and does
not require freeness of the action everywhere on \(X\).
Thus the argument can be applied component by component. It does
not apply Proposition 4.2(ii), whose statement assumes a globally
free action, as though that global premise had been established.

Equivalently, if an entire \(\Gamma_i\)-preimage contained no
fixed point, the above local contradiction would occur at its
ramification fiber. We only need the resulting existence of one
fixed point over \(\Gamma_i\). No assertion is made that every
point of that component has a fixed point in its fiber.

If \(B\) vanished identically on \(\Gamma_i\), then at this
fixed point both \(AD\) and \(B\partial_t\) would vanish,
regardless of \(A\). A slice is impossible at a zero of the
derivation. Since (3) identifies all plinth components, this proves
(2) for primitive \(D\).

The component-level conclusion does not conflict with the earlier
escaping-component countercontrol: it uses the actual factorization,
its ramification point, and the local transversal proof. It does not
infer a pointwise plinth criterion from abstract finiteness alone.

## 4. Removing the primitive hypothesis

Let \(h\) be a greatest common divisor of the coefficients of
\(D\) in \(R\), and write \(D=hD_0\). This is an invariant
replica of a primitive LND:
\[
h\in\ker D_0=C,\qquad D_0\in\operatorname{LND}(R),
\qquad \ker D_0=\ker D.
\tag{7}
\]
For completeness, \(Dh=hD_0h\) is divisible by \(h\).
Local nilpotence and additivity of derivation degree imply that
an element dividing its derivative must have zero derivative.
Thus \(Dh=0\), and cancellation gives \(D_0h=0\).
Now \(D^j r=h^jD_0^j r\), so local nilpotence of \(D\)
implies that of \(D_0\).

The plinth ideals satisfy
\[
P_D=hP_{D_0}.
\tag{8}
\]
To see this, \(hD_0r\) is invariant exactly when \(D_0^2r=0\).
The primitive result applied to
\(E=(Ah)D_0+B\partial_t\) excludes common components of
\(B\) and \(P_{D_0}\).

There are no common components of \(B\) and \(h\) either.
If an irreducible invariant \(q\) divided both, choose a closed
point on \(V(q)\subset S\). The quotient of three-space is
surjective, so a point above it exists. The factor \(h\) makes
\(D\) vanish there and \(B\) also vanishes, contradicting the
slice equation. Surjectivity is the exact property recorded in
Kaliman's Remark 3.3.

Together with (8), these two exclusions prove (2) for every
nonzero LND on \(\mathbb C^{[3]}\).

## 5. Conditional closure when higher image ideals are principal

Assume additionally that every
\[
J_j=D^j(R)\cap C,\qquad j\ge2,
\]
is principal. Its radical equals the radical of \(P_D\):
\(J_j\subseteq P_D\), while \(D^j(r^j)=j!p^j\) whenever
\(Dr=p\in P_D\). Thus a generator of \(J_j\) has exactly
the same irreducible factors as \(p_D\).

Equation (2) then yields
\[
(J_j:B)=J_j\qquad(j\ge2).
\tag{9}
\]
This uses factor divisibility in the UFD \(C\), not comaximality
of \(B\) with the generator. In particular isolated intersection
points cause no failure of saturation for a principal ideal.

The higher-image torsion argument in
[invariant-affine-slice-pass16.md](invariant-affine-slice-pass16.md)
now rules out a minimal slice of \(t\)-degree at least two.
Indeed that argument produces, for such a degree \(n\), a
nonzero class \(c_0+J_n\) killed by \(B^n\), contradicting
(9). The coefficient identity \((A,B)C=C\), also used in that
argument, is valid here by faithful flatness of \(C\to R\).
Therefore an affine slice exists and
\[
A P_D+BC=C.
\tag{10}
\]
The cases \(A=0\) or \(B=0\) are immediate from the slice
equation and agree with this conclusion.

This is a genuine consequence under the stated higher-image
principality hypothesis. It does not infer that hypothesis from
principality of \(P_D\). Without such an input, the conclusion
established for an arbitrary rank-three derivation is (2), not (10).

## 6. The rank-at-most-two consequence and source boundary

The published primary abstract of
[Ben Khaddah, El Kahoui and Ouali, *The Freeness Property for Locally Nilpotent Derivations of R[2]*](https://link.springer.com/article/10.1007/s00031-022-09705-z),
*Transformation Groups* 28 (2023), 35-60, states that the freeness
conjecture holds for nonzero LNDs of \(K^{[3]}\) of rank at most
two in characteristic zero. The freeness property is equivalent
to principality of all image ideals, in the formulation recalled
in Freudenburg's Section 2.2, item (9).

Consequently, for every nonzero \(D\) of rank at most two on
\(\mathbb C^{[3]}\), Section 5 applies and gives the exact
equivalence
\[
\boxed{
AD+B\partial_t\text{ has a slice}
\quad\Longleftrightarrow\quad
A P_D+BC=C
\quad\Longleftrightarrow\quad
AD+B\partial_t\text{ has an affine-in-}t\text{ slice}.}
\tag{11}
\]
There is no irreducibility assumption on \(D\), since the
replica reduction in Section 4 and the published rank conclusion
cover that case. An invariant ambient coordinate gives the
relative PID presentation \(\mathbb C[x]^{[2]}\), which is
the setting of the published result.

The original publisher abstract was directly read. The subscription
full text and proof of its Theorem 4.1 were not accessed in this
pass. The exact higher-image formulation and theorem numbering
are also explicitly attributed to that result in
[Dasgupta and Lahiri's introduction](https://arxiv.org/html/2302.13787v6).
The separate [source audit](rank-two-image-ideals-pass16.md) records
this distinction. Equation (11) uses the published result at that
statement level; it is not claimed to reconstruct its proof.

The result does not extend to rank three by citation. In particular
Daigle's withdrawn all-ranks preprint is not an input. The remaining
rank-three case still has potential higher-image saturation
obstructions not ruled out by the whole-component exclusion alone.

No computation is offered as proof of the global geometric input.
The source-dependent reconstruction is separate from the finite
polynomial identity checks in the other pass-16 notes. Novelty
and human expert review are not established.
