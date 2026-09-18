# Adversarial audit of the pointwise plinth criterion

The criterion survives this second audit. I found no counterexample
under the stated polynomial-three-space hypotheses. A sharp control
does show exactly how the conclusion can fail after removing an
invariant line from three-space: a reduced free-orbit fiber survives,
but the missing branch contributes nonzero third homology. This
invalidates the excision support step in the altered space, while
leaving much of the quotient geometry intact.

This is a fresh attack on the proof's assumptions and maps, not a
new claim of human peer review, formal verification, or novelty. The
audited implication remains a source-dependent deduction.

## 1. Statement being attacked

The statement in [the pointwise note](pointwise-plinth-pass17.md) is:
for a primitive nonzero LND \(D\) of \(R=\mathbb C^{[3]}\),
with invariant ring \(C\cong\mathbb C^{[2]}\), a reduced
scheme-theoretic single \(\mathbb A^1\) fiber of
\(\pi:\operatorname{Spec}R\to\operatorname{Spec}C\), carrying
a nonzero translation action, lies outside \(V(P_D)\).

The dangerous inference would be to replace the actual hypotheses
by the assertion that a finite curve factorization has one reached
point. A singular point of an intermediate curve can have another
normalization branch that is not reached by the source fiber. The
current proof permits this configuration locally and rules it out
only by its global homology calculation.

## 2. A control with an actual additive-group action

Start with \(\mathbb A^3_{u,v,w}\) and the primitive LND

\[
D=u\partial_v+2v\partial_w,
\qquad q=v^2-uw.
\tag{1}
\]

Its kernel is \(\mathbb C[u,q]\) and its plinth is
\(u\mathbb C[u,q]\). These claims can be checked without any
geometric classification. On \(u\ne0\),
\(R_u=\mathbb C[u,u^{-1},q][v]\) and \(D=u\partial_v\).
An invariant with a pole in \(u\) would have a nonzero leading
residue polynomial in \(q=v^2\), so could not be polynomial in
\(u,v,w\). Thus the kernel is as stated.

For the plinth calculation, if \(Da=c(u,q)\), then
\(a=c(u,q)v/u+b(u,q)\) with \(b\) Laurent in \(u\).
Any pole of \(b\) of order greater than one has a nonzero residue
in \(v^2\) and cannot cancel. At order one, polynomiality requires
an identity
\(c(0,v^2)v+b_{-1}(v^2)=0\). Its odd and even parts vanish
separately, so \(c(0,q)=0\). Conversely \(Dv=u\).

Remove the invariant line

\[
K=\{u=0,v=-1\},\qquad
X=\mathbb A^3\setminus K.
\tag{2}
\]

The action preserves this open set, since its flow is

\[
(u,v,w)\longmapsto
(u,v+au,w+2av+a^2u),\qquad a\in\mathbb C.
\tag{3}
\]

The regular-function ring is still \(\mathbb C[u,v,w]\):
the two affine opens \(D(u)\) and \(D(v+1)\) cover \(X\),
and their rings intersect in the original polynomial ring because
\(u\) and \(v+1\) are coprime primes. Thus the invariant-ring
morphism is

\[
\pi:X\longrightarrow\mathbb A^2_{u,q}.
\tag{4}
\]

This is the categorical morphism to the spectrum of invariants
among affine targets; no stronger quotient property for arbitrary
nonaffine targets is needed here. It is surjective and flat.
Flatness follows by restricting the original flat morphism, whose
coordinate presentation is free with basis \(1,v\) over
\(\mathbb C[u,q,w]\), using \(v^2=uw+q\).

Over the point \(p=(0,1)\), the original fiber consists of two
reduced lines, \(v=1\) and \(v=-1\). The second has been removed.
Consequently

\[
\pi^{-1}(p)=\{u=0,v=1\}\cong\mathbb A^1_w,
\qquad D|_{\pi^{-1}(p)}=2\partial_w.
\tag{5}
\]

The surviving fiber is reduced and smooth, and the action is free
on it. Nevertheless \(p\) belongs to the support \(u=0\) of
the plinth ideal of the global function ring.

This is not a counterexample to the audited theorem. The space
\(X\) is not affine three-space and is not affine at all: its
affinization is the original three-space and adds the missing line.
Indeed

\[
X\cong(\mathbb C^2\setminus\{0\})\times\mathbb C,
\qquad H_3(X;\mathbb Q)\cong\mathbb Q.
\tag{6}
\]

The coordinate change for this product is \((u,v,w)\mapsto
(u,v+1,w)\). Radial deformation in the first two coordinates
identifies its homotopy type with \(S^3\).

## 3. The escaping puncture and the failed map are explicit

The product away from \(\Gamma=\{u=0\}\) is unchanged:
on \(u\ne0\), use coordinates \((u,q,v)\). The exceptional
surface in \(X\) is
\(E=\operatorname{Spec}\mathbb C[v,w,(v+1)^{-1}]\).
There is even a finite nodal factorization

\[
E\longrightarrow Z=\{a^2=q(q-1)^2\}
\longrightarrow\mathbb A^1_q,
\qquad (v,w)\longmapsto(v^2,v(v^2-1)).
\tag{7}
\]

The first map is surjective: away from \(q=1\), recover
\(v=a/(q-1)\), while the node at \(q=1\) is reached by
\(v=1\). The second map is finite of degree two. Its node
has normalized points \(v=1,-1\); only the first is reached
by (5). This factorization is used as a control, not identified
with a particular Stein factorization in Kaliman's construction.

Take \(F=\{(0,0),(0,1)\}\). Then
\(Z^*\cong\mathbb A^1_v\setminus\{0,1,-1\}\), and
\(E^*=Z^*\times\mathbb A^1_w\). Topologically,

\[
X^*\cong
\bigl(\mathbb C^2\setminus\{(0,0),(0,1),(0,-1)\}\bigr)
\times\mathbb C.
\tag{8}
\]

Thus \(H_3(X^*;\mathbb Q)\cong\mathbb Q^3\). The three
linking spheres correspond under the local Thom calculation to
the three puncture loops \(\beta_0,\beta_1,\beta_{-1}\).
The map on punctures sends

\[
\beta_0\longmapsto2\gamma_0,
\qquad\beta_1\longmapsto\gamma_1,
\qquad\beta_{-1}\longmapsto\gamma_1.
\tag{9}
\]

Here \(\beta_{-1}\) is the escaping branch. It does occur in
\(\operatorname{im}\phi'\), but its class maps nontrivially
to \(H_3(X)\). Therefore it is not a boundary from
\(H_4(X,X^*)\), and cannot be represented in arbitrarily small
neighborhoods of the two fibers that are actually present in \(X\).
This is exactly where the argument requiring \(H_3(X)=0\) stops.

The example tests more than abstract nodal finiteness. It preserves
a genuine additive-group action, the invariant-ring base, flatness,
the off-divisor product, and a reduced free-orbit fiber. Its missing
homology hypothesis accounts precisely for its escaping cycle.

## 4. Why the attempted failure does not occur in polynomial three-space

For the actual theorem, \(X=\mathbb A^3\) makes every class in
\(H_3(X^*)\) a boundary from \(H_4(X,X^*)\). Excision then
places it in any chosen open neighborhood \(U\) of the entire
\(L=\pi^{-1}(F)\). The typed local Thom map is

\[
H_3(U\setminus L)
\longrightarrow H_3(U\setminus L,U\setminus E)
\longrightarrow H_1(E^*\cap U).
\tag{10}
\]

This does not require \(U\) to retract onto \(L\), or either
set to be compact. The vanished \(H_3(X)\), not an assumed
proper quotient, is what excludes the control's missing class.

I separately attacked the normalization support assertion. Smoothness
holds on an open subset of the source containing the whole reduced
fiber. It need not hold over a neighborhood of the point in the
base. On that source open set, normalization of each exceptional
surface component is the smooth base change of normalization of
its base curve. Hence every base branch gives exactly one copy of
the fiber. There is no hidden additional copy available to reach
another normalized point.

Each such copy is connected and reaches one normalized point.
Ramification there would make the pullback differential of a base
parameter zero, contradicting smoothness. Finite degree at least
two supplies an additional normalized point, which is therefore
unreached. These statements remain valid when all normalized points
map to the same singular point of the intermediate curve.

To exclude approach to an unreached point from somewhere far along
the noncompact fiber, take the inverse image \(O\) of the reached
disks in \(E^\nu\). It contains the entire inverse image of the
fiber. Finite normalization is a closed map in the Euclidean
topology, so

\[
E\setminus\nu_E(E^\nu\setminus O)
\tag{11}
\]

is a neighborhood of the entire fiber. Its inverse image lies in
\(O\). This rules out the suggested nonuniformity failure: no
common radius, compact fiber, or properness of \(\pi\) is used.

Finally, no homology relation hides the unreached coefficient.
On each normalization component of the affine curve, the finite
puncture loops are independent because there is also at least one
puncture at infinity. A sum of finite puncture loops cannot use
the total-puncture relation without introducing an infinity loop.
The weighted lift of the sum of base branch loops therefore has
a nonzero unreached coefficient that the support bound forbids.

## 5. Exact external inputs and verdict

The direct source check used Kaliman's final author version.[^1]
The following are the external inputs rather than new assertions
of this audit:

- Lemmas 2.1-2.2 provide the reduced exceptional inverse images and
  intermediate factorization framework.
- Proposition 3.2 provides finiteness and its homology diagram;
  its proof localizes cycles by excision. Lemma 3.1 gives the
  branch-loop sum.
- Theorem 5.2(i) permits the retained curve choice. The invocation
  of Proposition 3.2 Step 1 in Proposition 4.2 makes the retained
  component degrees at least two.
- Remark 3.3 gives the relevant surjectivity and flatness. The
  pointwise smoothness criterion and smooth-base-change normalization
  are the separate Stacks inputs.[^2][^3]

The primitive identification of that retained curve with the plinth
support is reconstructed in the
[whole-component note](whole-plinth-component-pass16.md). The
new pointwise work is the combination of smooth normalization
branches, the whole-fiber neighborhood (11), and the resulting
peripheral support contradiction. None of those steps can be
replaced by saying merely that a finite map has degree at least two.

No omitted hypothesis was found within the stated theorem. The
control above shows that its global topology is a substantive
assumption. The result remains limited to the stated setting;
neither this audit nor its example resolves cancellation.

## Sources

[^1]: Shulim Kaliman, [*Free C+-actions on C3 are translations*](https://www.math.miami.edu/~kaliman/library/Ka.invent.2004.c%2B.pdf), final author version, §§2-5, especially the diagram and excision proof in Proposition 3.2.
[^2]: The Stacks Project, [Lemma 29.35.14, pointwise smoothness criterion](https://stacks.math.columbia.edu/tag/01V9).
[^3]: The Stacks Project, [Lemma 37.19.2, normalization commutes with smooth base change](https://stacks.math.columbia.edu/tag/03GV).
