# Cancellation, ambient action obstructions and nonlinear coordinate selection

The unrestricted complex threefold cancellation problem remains unresolved:
\[
A[s]\simeq\mathbb C^{[4]}
\quad\Longrightarrow\quad
A\simeq\mathbb C^{[3]}.
\tag{1}
\]
Here \(A\) is a finitely generated complex domain and the displayed
isomorphism is an algebra isomorphism. This is the working interpretation
of the professor's question, not a confirmed correction. The originally
pasted conclusion \(X\simeq\mathbb A^1\) has the wrong dimension when
\(r>1\); the intended general conclusion would be \(X\simeq\mathbb A^r\).

There are three substantive conclusions. A nonlinear family disproves
another proposed coordinate-selection rule, with exact formulas allowing
arbitrary bad fibers away from the original exceptional fiber. A
conditional surface theorem now excludes every ambient additive extension
of certain actions, even when divergence-free lifts exist at every finite
order. An intrinsic symmetry argument identifies exactly what all
coordinate frames can recover, without assuming that the needed symmetry
exists.

These statements do not prove (1). The surface has not been embedded as a
hypersurface in affine three-space, and its embedding has not been
excluded. Priority and human expert verification remain unestablished.

## 1. An arbitrary-plinth family at the exact minimum degree

A locally nilpotent derivation, abbreviated LND, is a polynomial
derivation \(D\) for which every polynomial is killed by some iterate
\(D^N\). It describes an algebraic additive-group action. A slice is a
polynomial \(r\) with \(D(r)=1\). A primitive derivation has no common
nonconstant factor in its coefficients. These are different requirements:
a primitive LND can have fixed points and no slice.

Keep the same actual polynomial model used in the preceding minimum
calculation:
\[
B=\mathbb C[x,\lambda,w,z],\qquad
v=1+\lambda x,\qquad
\Delta=x^2\partial_w+2v^2w\partial_z.
\tag{2}
\]
The horizontal choices under consideration are actual LNDs \(\delta\)
satisfying \(\delta(x)=0\) and \(\delta(\lambda)=1\). Their degree \(q\)
is the largest nonzero iterated adjoint of \(\Delta\) by \(\delta\).
The minimum over this entire class is one, as proved in
[the exact minimum theorem](research/minimal-horizontal-pass31.md).
The previous pass already refuted the assertion that every minimizer
has a sliced primitive top.

The stronger assertion that the top's bad fibers must stay over \(x=0\)
is also false. Choose any polynomial \(p(x)\) with \(p(0)=1\), and set
\[
H_0=x^2c-b^2,\qquad F=p(x)b+x^2H_0^2,
\]
\[
L=F_c\partial_b-F_b\partial_c
 =2x^4H_0\partial_b+(4x^2bH_0-p)\partial_c.
\tag{3}
\]
The variables \(b,c\) below form an actual horizontal slice ring,
not an assumed rational replacement.

Define the forward coordinate expressions by
\[
H=H_0-2\lambda xpF^2,\qquad
W=b+4\lambda x^3H_0F^2-4\lambda^2x^4pF^4,
\]
\[
w=W,\qquad z=\frac{H+v^2W^2}{x^2}.
\tag{4}
\]
The last expression is polynomial. Modulo \(x^2\),
\(W\equiv b\), \(H\equiv-b^2-2\lambda xb^2\), and
\(v^2W^2\equiv b^2+2\lambda xb^2\). Thus its numerator is divisible
by \(x^2\). Only \(p(0)=1\) is used here.

The inverse is equally explicit. In the original variables put
\[
I=x^2z-v^2w^2,\qquad F_*=pw+x^2I^2,
\]
\[
H_0=I+2\lambda xpF_*^2,\qquad
b=w-4\lambda x^3IF_*^2-4\lambda^2x^4pF_*^4,\qquad
c=\frac{H_0+b^2}{x^2}.
\tag{5}
\]
The same congruence makes \(c\) polynomial. The transformation of
\((b,H_0)\) preserves \(pb+x^2H_0^2\); changing \(\lambda\) to
\(-\lambda\) supplies its inverse. Consequently (4)-(5) are two-sided
polynomial inverse maps, not just birational identities.

The transported derivation is
\[
\widetilde\Delta
=x^2\partial_b+2b\partial_c-4\lambda xpF\,L.
\tag{6}
\]
It is locally nilpotent because it is conjugate to (2).
The actual horizontal \(\partial_\lambda\) has degree exactly one:
the coefficient of \(\lambda\) in (6) is nonzero and the second
\(\lambda\)-derivative vanishes. Its primitive top on the
three-variable slice ring \(\mathbb C[x,b,c]\) is \(L\).

The exact kernel and full plinth are
\[
\ker L=\mathbb C[x,F],\qquad
L(\mathbb C[x,b,c])\cap\ker L=p\,\mathbb C[x,F].
\tag{7}
\]
In particular the plinth is not merely divisible by the prescribed
polynomial; every multiplicity of \(p\) is retained.

To see the polynomial local slice behind (7), let
\[
g(x)=1-2p'(0)x,\qquad
S=\frac{H_0+g(x)F^2}{x^2}.
\tag{8}
\]
Because \(gp^2\equiv1\pmod{x^2}\), this expression is polynomial,
and \(L(S)=-p\). Over \(\mathbb C(x)\), \(F,S\) are coordinates,
so the kernel is \(\mathbb C(x)[F]\) and the second degree module
is \(\mathbb C(x)[F]\oplus\mathbb C(x)[F]S\).

Contraction to \(\mathbb C[x,b,c]\) introduces no denominators.
At \(x=0\), the residues of \(F,S\) are a triangular coordinate pair.
At a nonzero value where \(p\ne0\), they remain coordinates. At a
root \(\alpha\) of \(p\), the variable \(H_0=\alpha^2c-b^2\) is a
plane coordinate, and the residues of \(F\) and \(S\) have respectively
an even quadratic dependence and a nonzero odd linear dependence on
\(H_0\). A relation with coefficients polynomial in \(F\), linear in
\(S\), cannot vanish there. Removing a hypothetical denominator pole
one factor at a time proves (7), including repeated roots.

The field \(L\) is free over \(x=0\), where \(L=-\partial_c\).
At a nonzero root \(\alpha\) of \(p\), it vanishes exactly along
\[
x=\alpha,\qquad \alpha^2c-b^2=0.
\tag{9}
\]
These are affine lines. For nonconstant \(p\), they obstruct a slice.
Since \(p(0)=1\), arbitrary effective divisors supported away from zero
can be normalized and used as its zero divisor.

The entire coefficient ideal is \((p,H_0)\): the polynomial local
slice puts \(p\) in that ideal, and a Bezout identity for \(p,x^4\)
then puts \(H_0\) there. Thus the full fixed-scheme ring is
\((\mathbb C[x]/(p))[b]\), retaining the prescribed multiplicities.

This is an explicit counterexample family within the fixed polynomial
model. It does not say that every minimizing horizontal action is bad:
a good minimizer remains available in this model. The complete proof
and finite controls are in
[the minimum-top note](research/minimum-top-structure-pass33.md).
The general rank and relative-plane background is standard; no new
classification of rank-two LNDs is asserted.

## 2. The unchanged conductor surface

The second investigation concerns a particular auxiliary affine surface.
It is not asserted to be a factor \(A\) in (1).

Its normalization and derivation are
\[
B_0=\mathbb C[u,y,z]/((u-1)(u-i)z-y(y-1)),\qquad d=u^4-1,
\]
\[
\delta_0(u)=0,\quad
\delta_0(y)=(u-1)(u-i),\quad
\delta_0(z)=2y-1.
\tag{10}
\]
Over \(u=1,i\), the fibers split into the two lines \(y=0,1\).
The fibers over \(u=-1,-i\) are ordinary lines. The six lines are
paired as
\(((1,0),(i,0))\),
\(((1,1),(-i,*))\), and
\(((-1,*),(i,1))\).
At a split line \((r,\epsilon)\) the shared parameter is
\(z/[r(2\epsilon-1)]\); at an ordinary line it is
\(y/[r(r-1)(r-i)]\).

Pinching each pair by these parameters defines the domain
\(R=B_0\times_{\mathbb C[t]^6}\mathbb C[t]^3\).
Its singular locus consists of three ordinary-double-crossing affine
lines. The inherited complete action classification gives
\[
\operatorname{LND}(R)=M\delta_0,\qquad
M=\mathbb Cu+d\mathbb C[u],\qquad
\ker(p\delta_0)=T=\mathbb C+d\mathbb C[u]\quad(p\ne0).
\tag{11}
\]
Thus the coefficient of \(u\) modulo \(d\) is the common translation
speed along all three singular lines. The definitions and full
classification are in
[the all-action proof](research/all-noninvariant-surface-pass30.md).

## 3. A branch count removes the nonzero-speed hypothesis

Suppose \(R=W/(F)\) for \(W=\mathbb C[X,Y,Z]\), and an ambient LND
\(E\) induces a nonzero action on \(R\). This is a conditional
hypothesis, not a supplied presentation.

The polynomial-kernel theorem gives \(\ker E=\mathbb C[f,g]\).
Since \(E\) preserves \((F)\), local nilpotence implies \(E(F)=0\),
so \(F=P(f,g)\). Primitive Jacobian normalization gives
\(E=h(f,g)J\), where \(J=\operatorname{Jac}(f,g,\cdot)\) is itself
primitive and locally nilpotent. These inherited statements and their
exact assumptions are proved in
[the preceding residue note](research/ambient-residue-obstruction-pass32.md).

There is a useful count for the quotient
\(\pi:\mathbb A^3\to\mathbb A^2\).
Choose the full reduced exceptional curve \(\Gamma\), including
the component \(P=0\), so the complement has a product trivialization.
Its exceptional surface factors through a curve
\(Z\to\Gamma\) finite over \(\Gamma\), as in Kaliman's quotient
construction.[^1] At a chosen exceptional value \(b\), write
\(r_b\) for the number of analytic branches of the full \(\Gamma\),
\(q_b\) for the number of normalization points of \(Z\) over \(b\),
and \(c_b\) for the number of irreducible components of the actual
reduced quotient fiber. Then
\[
c_b=q_b-r_b+1.
\tag{12}
\]

For clarity, this is a rational-homology rank deduction, not an
unramified-cover assumption. Independent puncture loops give spaces
of dimensions \(q_b,r_b\). The finite map sends each source loop to
a positive ramification multiple of its base loop, hence is surjective
over \(\mathbb Q\). The quotient pair diagram identifies the relevant
kernel with the preimage of the diagonal base-loop line, whose dimension
is \(q_b-r_b+1\). Excision in \(\mathbb A^3\) identifies the same
space with one generator per irreducible fiber component. Retaining
support over \(b\) prevents mixing different exceptional values.

For a single component \(\Gamma_i\), other branches contribute at
least as many source normalization points as base branches. Therefore
\(c_b\ge q_{i,b}-r_{i,b}+1\), even when other plinth components pass
through the same point.

All four conductor root labels map to one point \(b\) of \(P=0\).
If \(n\) further distinct \(u\)-values also map there, they supply
ordinary affine lines. The normalization-field identification gives
\[
q_{i,b}=4+n,\qquad c_b=3+n=q_{i,b}-1.
\tag{13}
\]
Combining this with the preceding inequality forces \(r_{i,b}\ge2\).
Ramification multiplicities and nilpotent fiber structure do not alter
these reduced counts.

At every conductor point the quadratic initial form of \(F\) has
rank two. Pulling back \(P\) through \(f,g\) now forces \(P\) to have
an ordinary node, with \(d(f,g)\) of rank two there. Hence \(J\)
is nonzero everywhere on the conductor. This is the new bridge:
even if \(E\) has zero conductor speed, its primitive normalization
has nonzero speed.

The residue comparison already proved for that primitive case
therefore applies without restriction on \(E\):
\[
S=\operatorname{im}(\ker E\to R)=\mathbb C+d\mathbb C[u^2],
\qquad J|_R=\kappa u\delta_0,\quad\kappa\ne0.
\tag{14}
\]
The full proof, including the normalization-field and support details,
is in [the all-speed obstruction](research/all-speed-ambient-obstruction-pass33.md).

## 4. Exact extendable-action dichotomy and the finite-order boundary

Fix any one hypothetical hypersurface presentation of \(R\).
If a nonzero action extends, (14) gives an ambient extension of
\(u\delta_0\). Every element of \(S\) lifts to an ambient invariant,
so taking invariant replicas gives every action \(uH\delta_0\)
with \(H\in S\). Conversely (14) excludes all other nonzero actions.

Thus the set of extendable surface LNDs is either
\[
\{0\}\quad\text{or}\quad
u\bigl(\mathbb C+d\mathbb C[u^2]\bigr)\delta_0.
\tag{15}
\]
The second alternative is exactly the odd-multiplier subspace of
(11). Its elements may have zero conductor speed. The theorem
does not decide which alternative occurs or whether a presentation
exists.

The invariant \(G=du\) supplies a sharper finite-order control:
\[
D_{\mathrm{even}}
=dG'(u)\delta_0=(u^4-1)(5u^4-1)\delta_0.
\tag{16}
\]
Under every hypothetical presentation, the dualizing-form calculation
gives an ambient Hamiltonian derivation preserving \(F\) exactly,
having zero divergence, and restricting to (16), after a nonzero
constant rescaling. The
[finite-thickening criterion](research/finite-thickening-algebraization-pass31.md)
makes this derivation locally nilpotent modulo every \(F^N\).

Nevertheless its nonzero even multiplier violates (15). No ambient
LND can restrict to this action. This rules out *every* ambient
additive lift of the specified action, not merely a badly chosen
lift. It remains a conditional example, since no presentation of
\(R\) is exhibited. In particular it is not a counterexample to
cancellation or a reason to assume every surface action must extend.

## 5. The compatible odd action has an unavoidable singular first stage

Assume a nonzero action extends in the hypothetical presentation,
and use the primitive ambient lift of \(u\delta_0\) obtained above.
Use \(s_0=u^2\) and
\(v_0=ds_0\). Its forced invariant image is the nodal ring
\(S=\mathbb C[d,v_0]/(v_0^2-d^2(d+1))\).
The full ambient plinth is principal and divisible by \(F\).

Choose an actual minimal local slice \(r\), meaning its derivative
generates the full plinth, and subtract an ambient invariant.
Its residue must then have the form \(du\,b(s_0)\) with \(b\ne0\).
If the residue were in \(S\), subtracting its invariant lift and
dividing by \(F\) would yield a smaller plinth generator, a contradiction.

The residue has degree two over \(\operatorname{Frac}S\).
Its square belongs to the square of the node ideal. For any ambient
invariant lift \(K\) of that square, monic division proves the
exact global first center
\[
\mathbb C[f,g,r]\cap FW=(F,r^2-K)\mathbb C[f,g,r].
\tag{17}
\]
This conclusion does not assume that the singular quotient curve
is factorial.

The corresponding unavoidable subalgebra is
\[
W_1=\mathbb C[f,g,r,(r^2-K)/F]
 \simeq\mathbb C[f,g,r,Y]/(FY-r^2+K).
\tag{18}
\]
Both \(F\) and \(K\) vanish to second order at the base node.
The relation's gradient therefore vanishes along the entire line
over that node with \(r=0\). Its scheme fiber is the doubled line
\(\mathbb C[r,Y]/(r^2)\), and its induced action is zero on the
reduced line.

A smooth final ambient realization must strictly enlarge \(W_1\).
Its three free conductor orbits would each map to a point on the
first stage's fixed line. Later modifications might repair the stage;
none has been constructed or excluded. Masuda's general modification
theory supplies the framework and a localized generic-fiber description,
not a theorem ruling out all later centers at this particular node.[^2]
The precise proof is in
[the forced-first-stage note](research/nodal-plinth-realization-pass33.md).

## 6. All nonlinear coordinate frames recover exactly the intrinsic span

Return to the full hypothesis (1), independently of the surface.
Let \(E=\partial_s\). For every genuine ambient coordinate partial
\(T\), including those obtained from nonlinear polynomial frames
with actual inverses, take its highest nonzero adjoint
\[
K_T=\frac{1}{q!}(\operatorname{ad}E)^qT,\qquad
h_T=K_T|_A,\qquad
\mathcal H_E=\{h_T:h_T\ne0\}.
\tag{19}
\]
Highest-coefficient local nilpotence follows from polynomial conjugation.
Commutation with \(E\) makes the restriction an intrinsic LND.

The nonempty qualification is substantive. Some ambient partial
moves \(A\). If \(e\) is its maximum \(s\)-degree on finite generators
of \(A\), its value on \(s\) has degree at most \(e\). Otherwise the
highest filtered LND would send \(s\) to a nonzero multiple of
\(s\), impossible for an LND. Hence its top restriction is nonzero.
This uses the established associated-graded LND mechanism.[^3]

Let \(F_A=\operatorname{Frac}A\). The complete conclusion is
\[
\operatorname{span}_{F_A}\mathcal H_E
=\operatorname{span}_{F_A}\operatorname{LND}(A).
\tag{20}
\]
More strongly, the conjugacy orbit of any one nonzero member of
\(\mathcal H_E\) under the full intrinsic special automorphism group
already has this span.

Here is the central algebraic argument. For any nonempty family
\(\mathcal N\) of nonzero intrinsic LNDs stable under the full intrinsic
group, put \(V=\operatorname{span}_{F_A}\mathcal N\).
Polynomial conjugation and finite interpolation give
\([L,h]\in V\) for every intrinsic LND \(L\) and \(h\in\mathcal N\).
For \(g\in\ker L\), the replica \(gL\) is again locally nilpotent, and
\[
[gL,h]-g[L,h]=-h(g)L.
\tag{21}
\]
If \(L\notin V\), some \(g\in\ker L\) has \(h(g)\ne0\).
Otherwise the local-slice description
\(F_A=\operatorname{Frac}(\ker L)(r)\) would make \(h\) a rational
multiple of \(L\), a contradiction. Equation (21) then forces
\(L\in V\), proving the claim.

Intrinsic flows extend to actual polynomial automorphisms of \(A[s]\)
by fixing \(s\). They commute with \(E\), so they preserve the extraction
in (19) and carry actual coordinate sources to actual coordinate sources.
This proves (20). Closure only under the family's own generated subgroup
would not suffice; a family of parallel shears is a counterexample to
that weaker premise.

Because \(A\) is a UFD, its common rational LND invariant field is
\(\operatorname{Frac}(\operatorname{ML}(A))\), by the coprime-numerator
divisibility argument. The published open-orbit theorem identifies
trivial rational invariants with generic tangent span of full rank.[^4]
Consequently the earlier determinant certificate is now an equivalence:
\[
\operatorname{ML}(A)=\mathbb C
\quad\Longleftrightarrow\quad
\exists T_1,T_2,T_3:
\det(E,K_{T_1},K_{T_2},K_{T_3})\ne0.
\tag{22}
\]

This removes a separate completeness question about extraction from
all frames. It does not prove either side of (22) from (1).
Nor does a nonzero determinant provide commuting fields, a constant
determinant, slices, or affine-space recognition.

In the open-orbit case, the one-seed spanning conclusion also follows
from the published isotropy theorem: the stabilizer acts on the orbit
tangent space as its special linear group. Conjugates of a nonzero
seed value therefore span that space. This existing mechanism is
explicitly credited, rather than treated as a new flexibility theorem.[^4]

A finite rank increase is available *if* an intrinsic LND outside the
current span is supplied. Equation (21) selects that LND or a replica;
interpolation selects a scalar-time conjugate outside the span.
At most two successful increases take rank one to rank three. This
is not a runtime or degree bound, and no method for finding the
required outside LND under (1) alone has been proved.

The complete reconstruction is in
[the cross-frame saturation note](research/cross-frame-saturation-pass33.md).
The known cylinder comparison for the modified invariant is one-sided;
it does not supply the missing reverse implication.[^5]

## 7. Remaining mathematical obligations

The original recognition gap remains: construct sufficient intrinsic
structure from (1), without assuming polynomiality of \(A\).
Equation (22) identifies full generic additive span exactly, but even
that condition still needs an existence proof here and does not by
itself recognize affine three-space.

The canonical model now permits arbitrary non-origin plinth divisors
in primitive tops at the absolute minimum degree. A future selection
argument must use more than minimum degree and location of the
original exceptional fiber. The existence of a good choice in this
particular model does not establish a universal selection theorem.

For the auxiliary surface, the all-noninvariant three-generator
problem and the compatible odd ambient realization are still separate
open tasks. The first modification is forced and singular, but
excluding all later repairs would require a new argument.

The proof notes include standalone exact polynomial controls.
The saved [complete regression](verification-pass-33.json) contains
757 passing methods across 69 suites, including 25 controls added
with these four proofs.
Those controls verify the displayed finite identities and negative
examples, not universal topological statements, quantification over
all LNDs, or the original conjecture. Independent AI reconstructions
are recorded separately from mathematical statements in the
[proof audit](research/proof-audits-pass33.md).
No expert review, formal proof-assistant verification, or novelty
certification is claimed.

The [bounded literature comparison](research/literature-scope-pass33.md)
separates the published mechanisms from the explicit applications.
It is not an exhaustive priority audit.

## Sources

[^1]: Shulim Kaliman, [*Free C+-actions on C3 are translations*](https://www.math.miami.edu/~kaliman/library/Ka.invent.2004.c%2B.pdf), final author version, Lemmas 2.1-2.2, Notation 2.3, Lemma 3.1 and Proposition 3.2(i), including the homology diagram and excision argument. The branch-rank formula (12) is reconstructed from these ingredients; it is not quoted as the printed proposition. No free-action assumption is used.

[^2]: Kayo Masuda, [*Factorial affine Ga-varieties with principal plinth ideals*](https://arxiv.org/html/2312.05455), 2023, Section 2, Lemma 2.2, Lemma 3.2 and Theorems 3.8-3.9. The monic center (17) is proved directly, while the cited general theorem retains its localization and generic-fiber scope.

[^3]: Bachar Alhajjar, [*LND-Filtrations and Semi-Rigid Domains*](https://arxiv.org/pdf/1501.00445), Proposition 2.2 and Proposition 3.4. The associated-graded theorem is credited there to Daigle. This is an inherited filtration input, not a new theorem of this investigation.

[^4]: Ivan Arzhantsev, Hubert Flenner, Shulim Kaliman, Frank Kutzschebauch and Mikhail Zaidenberg, [*Flexible Varieties and Automorphism Groups*](https://arxiv.org/pdf/1011.5375), version 2, Proposition 1.8, Theorem 1.13, Corollary 1.14, Definition 2.1, Remark 2.7(1), Theorem 4.2 with proof and Proposition 5.1. The orbit and rational-invariant results supply the published bridge in (22). Theorem 4.2 supplies the open-orbit one-seed implication; none proves ML triviality from a polynomial cylinder.

[^5]: Pranavashis Dasgupta and Neena Gupta, [*An Algebraic Characterization of the Affine Three Space*](https://arxiv.org/pdf/1709.00169), version 2, Lemma 3.1 and proof. The one-sided modified Makar-Limanov cylinder comparison cannot be reversed on the strength of an ambient slice alone.
