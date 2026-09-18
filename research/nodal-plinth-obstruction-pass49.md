# An ordinary node cannot support the second-image obstruction

The second-image obstruction cannot occur at an ordinary node of
the full primitive plinth polynomial. The argument does not require
the obstruction scheme to be reduced or the derivative coefficients
to belong to its ideal. It uses the actual quadratic residue fields
and the separately proved surjectivity onto normalized cover points.

This removes one closed-point configuration. It does not recognize
all globally quadratic presentations or settle cancellation.

## 1. Actual local data and the precise claim

Retain the actual degree-two independent-defect setting from
[pass 46](quadratic-residue-degree-pass46.md), after its already
recognized polynomial cases have been removed. Thus every primitive
plinth component has actual residue invariant field of degree two.
Let \(q\) be a closed second-image obstruction point and set
\[
R=C_{\mathfrak m_q},\qquad \mathfrak n=\mathfrak m_qR,
\qquad \mathcal A=A\otimes_C R.
\tag{1}
\]
The invariant base is the smooth plane \(C\simeq\mathbb C^{[2]}\),
and \(A[s_*]\simeq\mathbb C^{[4]}\) remains the original
polynomial-cylinder hypothesis.

The [second-image bundle theorem](second-image-vector-bundle-pass47.md)
and [flat-conic gate](flat-conic-topology-gate-pass47.md) provide
\[
F_2=R\oplus Rz\oplus Rw,\qquad
r=az+bw,\qquad JR=(a,b),\qquad \gcd_R(a,b)=1,
\tag{2}
\]
\[
Dr=p,\qquad Dz=\epsilon br+B_1,
\qquad Dw=-\epsilon ar+B_2,
\tag{3}
\]
\[
p=aB_1+bB_2,
\qquad \epsilon r^2-2B_2z+2B_1w-Q=0,
\qquad \epsilon\in R^*.
\tag{4}
\]
All of \(a,b,B_1,B_2,Q\) belong to \(\mathfrak n\).
No assertion \(B_1,B_2\in J\) is made. The invariant translation
of the actual minimal slice in (2) has already been performed.
In particular,
\[
r\in\mathfrak n\mathcal A,
\tag{5}
\]
so \(r\) vanishes on the entire scheme-theoretic quotient fiber.

**Theorem.** The full polynomial \(p\) cannot have an ordinary
node at \(q\). Here this means that its lowest nonzero term
has order two and is the product of two distinct complex linear
forms in regular parameters of \(R\). Repeated components of
the full divisor are not covered by this condition.

## 2. The normalized-cover input, without a surjectivity assumption

For an irreducible plinth component \(\Gamma_i\) through \(q\),
let \(E_i\) be its actual irreducible reduced pullback surface.
Factorial closure and factoriality make its defining base prime
remain prime in \(A\). The actual Kaliman factorization gives
\[
E_i\longrightarrow Z_i\longrightarrow\Gamma_i,
\]
whose normalized finite curve cover is
\[
Z_i^\nu\longrightarrow\Gamma_i^\nu.
\tag{6}
\]
Its function field is the full actual residue invariant field
\(F_i\), a quadratic extension of \(K_i=\mathbb C(\Gamma_i)\).
This identification is established in the
[intrinsic monodromy note](quadratic-monodromy-pass46.md); it is
not guessed from the conic relation.

The separate [normalized-cover surjectivity proof](normalized-cover-surjectivity-pass49.md)
proves that \(E_i^\nu\to Z_i^\nu\) reaches every normalized
cover point. Its input is the actual global quotient homology
diagram and the whole-fiber support argument, not a claim that
normalizing an arbitrary surjective morphism preserves surjectivity.
No smoothness, reducedness or affine-line description of the
closed quotient fiber is assumed in that lemma.

We record the exact consequence needed here. A rational function
on \(Z_i^\nu\) whose pullback is regular on \(E_i^\nu\)
is regular at every reached point. If it had a pole of order
\(n>0\), a local parameter \(t\) would give an equation
\(t^n h=u\) with \(u\) a unit. Pullback at a point above it
would equate a product containing a vanishing parameter to a unit.
This is impossible in the local domain.

Apply this to the rational function represented by the actual
residue of \(r\). It is invariant because \(Dr=p\), and its
pullback is regular wherever the local coefficients in (2) are
defined. Every point above a branch of \(q\) lies in that
neighborhood. Surjectivity therefore makes \(r\) regular at
every normalized cover point above that branch. By (5), its
value at every such point is zero.

## 3. A trace vanishing statement on each normalized branch

Fix a point \(\xi\in\Gamma_i^\nu\) above \(q\), and let
\(R_\xi\) be its DVR with maximal ideal \(\mathfrak m_\xi\).
The integral closure \(T_\xi\) of \(R_\xi\) in \(F_i\)
is finite and torsion free of rank two, hence free over this
DVR. Its maximal ideals are exactly the normalized cover points
above \(\xi\). The preceding argument puts
\[
r\in\operatorname{rad}(\mathfrak m_\xi T_\xi).
\tag{7}
\]
In particular it is an element of \(T_\xi\): membership in
the local ring at every maximal ideal of this semilocal finite
normal algebra contracts to membership in the algebra.

Multiplication by \(r\) on the finite-dimensional residue algebra
\(T_\xi/\mathfrak m_\xi T_\xi\) is nilpotent. Its trace is
zero, even when that residue algebra is nonreduced. Reducing the
matrix trace of multiplication on the free rank-two module gives
\[
\operatorname{Tr}_{F_i/K_i}(r)\in\mathfrak m_\xi.
\tag{8}
\]
This works at ramified and unramified cover points alike.

The residue of the actual minimal slice is a primitive element
of \(F_i/K_i\). Indeed localizing the full plinth at its base
prime makes \(r\) a minimal local slice; if its residue were
in \(K_i\), lifting that scalar and dividing by the base prime
would lower the plinth valuation. Since the extension has prime
degree two, a non-scalar residue generates it. This is the same
actual minimal-slice gate used in
[the finite quadratic lifting theorem](minimal-quadratic-slice-pass46.md).

Suppose first that the residue of \(b\) is nonzero in \(K_i\).
Eliminate \(w=(r-az)/b\) in (4), and set \(p=0\) on
the component. The resulting equation is
\[
r^2+\frac{2B_1}{\epsilon b}r-\frac{Q}{\epsilon}=0
\quad\text{over }K_i.
\tag{9}
\]
It is the exact quadratic minimal polynomial of \(r\), not
a possibly reducible relation for an unspecified element. Thus
(8) gives
\[
\frac{B_1}{b}\in\mathfrak m_\xi,
\qquad
\operatorname{ord}_\xi(B_1)\geq
\operatorname{ord}_\xi(b)+1\geq2.
\tag{10}
\]
The last inequality uses \(b(q)=0\). Zero values are interpreted
as having infinite order. The local coefficient \(\epsilon\)
stays a unit on this normalized branch.

If instead \(b\) is identically zero on \(\Gamma_i\), its
base prime divides \(b\) in \(R\). Coprimality in (2)
makes \(a\) nonzero on the component. Reducing
\(p=aB_1+bB_2\) therefore gives \(B_1=0\) on the entire
component. This case does not require division by \(b\).

Interchanging the roles of the two generators, when \(a\)
is nonzero on the component the exact polynomial is
\[
r^2-\frac{2B_2}{\epsilon a}r-\frac{Q}{\epsilon}=0,
\tag{11}
\]
so the same reasoning yields
\(\operatorname{ord}_\xi(B_2)\geq2\). If \(a\) is
identically zero there, coprimality and (4) instead give
\(B_2=0\) on that component. These alternatives cover every
branch, including two branches of the same irreducible nodal curve.

## 4. Two distinct tangents force the contradiction

At an ordinary node there are exactly two smooth normalized
branches through \(q\), with distinct tangent directions in
the two-dimensional tangent space of the invariant plane.
By (10) and its companion, the restrictions of \(B_1\) and
\(B_2\) to each of these branches have order at least two,
or vanish identically. Their linear parts consequently vanish
on both tangent directions. Hence
\[
B_1,B_2\in\mathfrak n^2.
\tag{12}
\]
But \(a,b\in\mathfrak n\), so (4) gives
\[
p=aB_1+bB_2\in\mathfrak n^3,
\tag{13}
\]
contradicting the nonzero quadratic initial form of an ordinary
node. This proves the theorem without a reducedness hypothesis
on \(J\) or the cubic coefficient premise \(B_1,B_2\in J\).

For comparison with the original reduced-point question, write
\(B_1=ac+bd\), \(B_2=ae+bf\) when \(J=\mathfrak n=(a,b)\).
The earlier cubic result gives \(\bar c\bar f-\bar d\bar e=0\).
The quadratic discriminant of \(p\) is then
\[
(\bar d+\bar e)^2-4\bar c\bar f=(\bar d-\bar e)^2.
\tag{14}
\]
The node exclusion forces \(\bar d=\bar e\). Thus the
rank-at-most-one first-jet coefficient matrix is also symmetric;
the quadratic tangent cone of \(p\) is a square or is zero.
This is only a first-order restriction, not recognition of the
remaining double-tangent cases.

## Scope and attribution

The normalized-cover surjectivity and its source audit are proved
in the separately linked parallel note. The algebra here uses the
already established actual residue-field identification and a trace
calculation, not a new assertion about normalizing arbitrary
morphisms. No normalization-surjectivity shortcut is assumed.

Together with pass 47, the obstruction support avoids both smooth
points and ordinary nodes of the full plinth divisor. Consequently,
if that full divisor is reduced and has only ordinary nodes as
singularities, \(J=C\) and the prior criterion supplies the global
quadratic equation. This last consequence does not by itself make
that equation a polynomial three-ring when the plinth components
intersect or have nodes. Repeated full components and more singular
points remain outside the conclusion. No numerical suite is used
to certify the trace or topological argument, and no historical
novelty or unrestricted cancellation claim is made.
