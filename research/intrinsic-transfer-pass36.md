# The exact rank-one gate for a degree-one ambient partial

The degree-one adjoint condition does not yet force a new intrinsic
direction. Under the full polynomial-cylinder hypothesis and intrinsic
rank one, it does give a precise equivalence: preservation of the common
invariant ring by the ambient partial is equivalent to local nilpotence
of its first opposite double commutator.

The proof uses the canonical volume supplied by the polynomial cylinder.
Commutation with the slice action alone would not justify the result.
Neither side of the equivalence has been proved automatic. The result
does not establish cancellation, intrinsic rank at least two, novelty,
or expert verification.

## 1. Hypotheses and the actual coefficient decomposition

Let
\[
B=A[s]\simeq\mathbb C^{[4]},\qquad E=\partial_s,
\tag{1}
\]
and assume that the intrinsic generic LND rank of \(A\) is one.
The inherited primitive-saturation and quotient results give
\[
C=\ker D=\operatorname{ML}(A)\simeq\mathbb C^{[2]},\qquad
\operatorname{LND}(A)=CD,
\tag{2}
\]
for a nonzero primitive LND \(D\). The ring \(A\) is a smooth
affine UFD with only constant units.

Take an actual ambient coordinate partial \(T\) satisfying
\[
[E,[E,T]]=0,\qquad [E,T]\ne0.
\tag{3}
\]
In fact the argument below only requires that \(T\) be an LND;
its coordinate-partial status is not used as a hidden statement about
\(s\). In particular \(T(s)\) need not vanish.

The coefficient decomposition relative to the given product is
\[
T=D_0+sD_1+(b_0+s b_1)E,
\qquad D_0,D_1\in\operatorname{Der}_{\mathbb C}(A),
\quad b_0,b_1\in A.
\tag{4}
\]
The standard leading-filtration lemma makes \(D_1\) a nonzero
intrinsic LND. If the horizontal degree were zero, that same lemma
would force \(b_1=0\), contradicting (3). Thus
\[
D_1=fD,\qquad 0\ne f\in C.
\tag{5}
\]
The associated-graded LND input is inherited, not a new assertion of
this investigation.[^filtration]

Set \(S=[E,T]\) and \(U=[T,S]\). Direct calculation gives
\[
S=fD+b_1E,
\tag{6}
\]
\[
\begin{split}
U&=H+qE,\\
H&=[D_0,fD]-b_1fD,\\
q&=D_0(b_1)-fD(b_0)-b_1^2.
\end{split}
\tag{7}
\]
In particular \([E,U]=0\), so \(H\) is an actual derivation
of \(A\), not a rational coefficient or a value obtained by
specializing a non-descending action.

The field \(S\) is an LND: it is the triangular extension of
\(fD\) with \(S(s)=b_1\). This does not make its commutator
with \(T\) locally nilpotent.

## 2. The polynomial cylinder supplies an invariant volume

Choose the standard algebraic volume \(\Omega\) in an ambient
polynomial coordinate frame of \(B\). Every LND of \(B\)
preserves it. Indeed its polynomial additive-group flow has an
inverse, so its Jacobian is a unit in \(B[t]\), necessarily a
nonzero complex constant. Evaluation at \(t=0\) makes it one.

In particular \(\mathcal L_E\Omega=0\). The contraction
\(\iota_E\Omega\) therefore descends to a nowhere-vanishing
top form \(\omega\) on \(A\). Equivalently, the product
decomposition of differentials writes \(\Omega\), up to a sign,
as \(\omega\wedge ds\), with \(\omega\) independent of \(s\).
This also proves the needed triviality of the canonical module of
\(A\), without assuming a polynomial coordinate system on \(A\).

Every intrinsic LND preserves \(\omega\), by the same flow-unit
argument using \(A[t]^*=\mathbb C^*\). Hence
\(\operatorname{div}_{\omega}(fD)=0\). The divergence of (4)
then gives the useful slope identity
\[
b_1=-\operatorname{div}_{\omega}D_0.
\tag{8}
\]

Both \(T\) and \(S\) preserve \(\Omega\), so their
commutator \(U\) preserves it as well. In (7), \(q\) is
independent of \(s\). It follows that
\[
\operatorname{div}_{\omega}H=0.
\tag{9}
\]
This last conclusion is stronger than merely knowing \([E,U]=0\).

## 3. Exact equivalence for the common invariant plane

**Proposition.** Under (1)–(5), the following are equivalent:

1. \(T(C)\subseteq C\).
2. \(H(C)=0\).
3. \(H\in CD\).
4. \(H\) is an LND of \(A\).
5. \(U=[T,[E,T]]\) is an LND of \(B\).

For \(c\in C\), equation (4) first gives
\(T(c)=D_0(c)\in A\). Since \(S(c)=0\), equation (7) gives
\[
H(c)=U(c)=-fD\bigl(T(c)\bigr).
\tag{10}
\]
As \(f\ne0\), this proves equivalence of the first two assertions.

If \(H(C)=0\), the local-slice fraction-field presentation for
\(D\) makes \(H\) a rational multiple of \(D\). Primitivity
and UFD saturation then give \(H=aD\) for some \(a\in A\).
Here the coefficient is initially in \(A\), not automatically in
\(C\). Equation (9) supplies the missing step:
\[
0=\operatorname{div}_{\omega}(aD)=D(a).
\tag{11}
\]
Thus \(a\in C\), proving assertion 3. Such a multiple is an
LND. Conversely every intrinsic LND is in \(CD\) by (2), and
therefore kills \(C\).

Finally, restriction of an LND \(U\) to its stable subring \(A\)
is an LND, so assertion 5 implies assertion 4. In the other
direction, if \(H\) is an LND, then \(U=H+qE\) is a
triangular LND on \(A[s]\): its iterates on \(A\) are those
of \(H\), and \(U^j(s)=H^{j-1}(q)\) for \(j\ge1\).
This proves all five equivalences.

The zero derivation is allowed in assertions 3–5. The nonzero
assumption in (5) is essential in (10); it is already guaranteed
by the genuine degree-one premise.

## 4. What this proves, and the remaining automatic-transfer gap

The equivalence concerns the unique intrinsic invariant ring of a
rank-one candidate. It does not refer to a chosen old invariant-plane
embedding in a separately known polynomial threefold. It also allows
an arbitrary nonzero \(T(s)\) in (4).

It identifies a concrete gate for a proposed preservation proof:
one must prove that the actual opposite double commutator is locally
nilpotent, or prove directly that \(T\) preserves \(C\). Its
commutation with \(E\) and its zero divergence are not replacements
for that missing local-nilpotence statement.

No argument here proves either condition automatic. Moreover,
preservation \(T(C)\subseteq C\) is weaker than annihilation
\(T(C)=0\), and does not by itself provide another intrinsic LND.
An asserted finite-dimensional all-LND closure still needs its own
proof. If such a closure has generic rank at least three, the
[pass 35 group criterion](rank-one-cylinder-pass35.md) rules out
intrinsic rank one. This investigation does not establish the
required closure or its generic rank.

In particular, a coordinate example with a known polynomial quotient
and several intrinsic directions cannot refute the rank-one-specific
equivalence or settle the missing automatic implication. No such
example is counted here as progress against the original hypothesis.
The genuine unresolved step remains local nilpotence or invariant
preservation for a transverse ambient partial under the uniqueness
premise.

## Source and verification boundary

The unique-filtration and leading-filtration facts are published
inputs. The primitive saturation and fraction-field argument are the
inherited UFD/local-slice mechanisms, also used explicitly in the
[pass 35 relative transfer](rank-one-cylinder-pass35.md). The new
written deduction here is the volume-assisted equivalence in Section
3; no statement-level novelty conclusion is drawn.

Finite polynomial controls can check (7)–(11), but cannot decide the
unproved universal implication. No checker is presented as a substitute
for those quantifiers. This note does not claim expert review or Lean
verification.

[^filtration]: Bachar Alhajjar, [*LND-Filtrations and Semi-Rigid Domains*](https://arxiv.org/pdf/1501.00445), Proposition 2.2, Propositions 3.2–3.5 and the proof of Proposition 3.4. The associated-graded result is credited there to Daigle. These are the previously source-audited inputs in the [leading-derivation note](leading-derivation-pass23.md); intrinsic uniqueness does not itself assert stable preservation by ambient translations.
