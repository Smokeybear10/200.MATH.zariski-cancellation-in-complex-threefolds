# Saturation does not automatically remove the bad fiber

The rank-two closure criterion in the earlier note is a special case of
Derksen, van den Essen and Maubach's commuting-derivations theorem. It is
known, not a new result of this investigation. Their Theorem 2.1 gives
the common invariant ring, the finite set of dependent fibers, and the
polynomial conclusion when every fiber is independent. Their Lemma 3.7
also gives the correct saturation operation.[^1]

This pass checks whether that operation eliminates the obstruction we
encountered. In general it does not. The standard Russell cubic supplies
an exact example where the pair is already saturated and a bad fiber remains.
This is an obstruction to a proof strategy, not a cancellation counterexample.

## 1. The known saturation operation

Let \(A\) be a characteristic-zero UFD, \(A^*=\mathbb C^*\), of
transcendence degree three. Suppose \(D_1,D_2\) are commuting,
generically independent locally nilpotent derivations with common kernel
\(\mathbb C[f]\). The relevant module is

\[
 M=\bigl(\mathbb C(f)D_1+\mathbb C(f)D_2\bigr)
       \cap\operatorname{Der}_{\mathbb C}(A).
 \tag{1}
\]

The cited Lemma 3.7 says it has a basis \(E_1,E_2\) over \(\mathbb C[f]\),
still consisting of commuting LNDs. Replacing the original pair by this
basis can remove a spurious dependent fiber, but need not remove all of them.
The question immediately following that lemma explicitly asks whether the
remaining dependent fibers coincide with nonpolynomial fibers.

The underlying mechanism is useful to reconstruct. Simultaneous preslices
\(p_i\) satisfy \(D_jp_i=0\) for \(i\ne j\) and
\(D_ip_i=q_i(f)\ne0\). The map

\[
 E\longmapsto(Ep_1,Ep_2)
\]

embeds \(M\) into \(\mathbb C[f]^2\). Indeed the images belong to
\(A\cap\mathbb C(f)=\mathbb C[f]\), and the nonzero \(q_i\) give
injectivity. A submodule of a finite free module over this PID is finite
free. Its rank is two because it contains the original pair.

Any element of \(M\) is locally nilpotent: after passing to
\(A\otimes_{\mathbb C[f]}\mathbb C(f)\), it is a linear combination of
commuting LNDs with invariant scalar coefficients. On any fixed element,
all sufficiently long mixed derivatives vanish. Since this combination
preserves \(A\), the same vanishing holds there. Invariant coefficients
also show that any two elements of \(M\) commute.

For the artificial pair \(f\partial_u,f\partial_v\) on
\(\mathbb C[f,u,v]\), saturation recovers
\(\mathbb C[f]\partial_u\oplus\mathbb C[f]\partial_v\).
Thus that elementary rank-drop example alone does not obstruct a
saturation-based repair.

## 2. A pair which is already saturated

Use the Russell cubic ring from the paper's Example 1.1:

\[
 A=\mathbb C[x,y,z,t]/(x^2y+x+z^2+t^3).
\]

Write

\[
 D_1=2z\partial_y-x^2\partial_z,\qquad
 D_2=3t^2\partial_y-x^2\partial_t.
 \tag{2}
\]

Both kill the defining relation and commute. They are locally nilpotent:
each is triangular on the indicated generators. On \(A[x^{-1}]\), solving
for \(y\) identifies the ring with
\(\mathbb C[x,x^{-1},z,t]\), and the two fields become
\(-x^2\partial_z,-x^2\partial_t\). Their common kernel in \(A\) is
\(\mathbb C[x]\), as also stated in the source.

**Claim.** This pair is already saturated:

\[
 \bigl(\mathbb C(x)D_1+\mathbb C(x)D_2\bigr)
   \cap\operatorname{Der}_{\mathbb C}(A)
 =\mathbb C[x]D_1\oplus\mathbb C[x]D_2.
 \tag{3}
\]

To prove it, let \(E=r(x)D_1+s(x)D_2\) preserve \(A\). The values
\(E(z)=-x^2r(x)\) and \(E(t)=-x^2s(x)\) belong to
\(A\cap\mathbb C(x)=\mathbb C[x]\). Hence
\(r=a/x^2,\ s=b/x^2\) for \(a,b\in\mathbb C[x]\).
The condition \(E(y)\in A\) says

\[
 2a(x)z+3b(x)t^2\in x^2A.
 \tag{4}
\]

Reduction modulo \(x\) takes place in
\[
 A/(x)=\mathbb C[y,z,t]/(z^2+t^3).
\]
The elements \(z,t^2\) are linearly independent over \(\mathbb C\)
in this ring: the monic relation in \(z\) gives normal forms of
\(z\)-degree at most one. Thus (4) first forces
\(a(0)=b(0)=0\). Write \(a=xa_1,\ b=xb_1\).
Since \(A\) is a domain, cancellation of one \(x\) in (4) gives
\(2a_1z+3b_1t^2\in xA\). The same argument gives
\(a_1(0)=b_1(0)=0\). Therefore \(x^2\mid a,b\), so \(r,s\)
are polynomials. This proves (3).

Nevertheless, modulo \(x\), the pair becomes
\[
 \overline D_1=2z\partial_y,\qquad
 \overline D_2=3t^2\partial_y.
\]
It has generic rank one, not two. Every other basis of the module (3)
differs by a matrix in \(\mathrm{GL}_2(\mathbb C[x])\), whose
specialization at zero is invertible. The rank loss therefore persists.
The bad fiber is the cusp \(z^2+t^3=0\) times an affine line and is
not a polynomial affine plane.

## 3. What this does and does not settle

The argument rules out this general inference:

> Saturate a pair of commuting LNDs over its one-variable invariant
> ring, and every whole-fiber degeneration disappears.

It does not rule out a theorem using the extra hypothesis
\(A[s]\cong\mathbb C^{[4]}\). No such cylinder isomorphism for the
Russell cubic is asserted or refuted here. It also does not rule out a
different intrinsic action outside the rational span of (2).

For the main cancellation investigation, the precise remaining obligation
is to construct a suitable intrinsic pair and prove that stable affineness
excludes the residual bad fibers of its saturated module, or find another
global route. Renaming a leading coefficient or dividing an individual
field is not that proof.

The standalone checker verifies preservation of the relation, commutation,
and the cusp normal-form independence. The all-degree saturation argument
is the written divisibility proof above. There is no human review, formal
proof-assistant certificate, or novelty claim.

## Sources

[^1]: Harm Derksen, Arno van den Essen and Stefan Maubach, [*A commuting derivations theorem on UFD's*](https://arxiv.org/pdf/0806.2038), Theorem 2.1, Example 1.1, Lemmas 3.4 and 3.7, and the question immediately following Lemma 3.7. The arXiv record dates the initial version to 2008. The saturation proof and Russell calculation above are reconstructions with explicit scope, not claimed new theorems.
