# General invariant affine replacement over polynomial three-space

Let

\[
R=\mathbb C^{[3]},\qquad 0\ne D\in\operatorname{LND}(R),
\qquad C=\ker D,\qquad P_D=D(R)\cap C.
\]

For invariant coefficients \(A,B\in C\), set
\(E=AD+B\partial_t\) on \(R[t]\). The source-dependent
deduction below gives

\[
\boxed{
E\text{ has a slice}
\quad\Longleftrightarrow\quad
A P_D+BC=C
\quad\Longleftrightarrow\quad
E\text{ has a slice affine in }t.}
\tag{1}
\]

No assumption about the rank of \(D\), principality of its higher
image ideals, or the Freeness Conjecture occurs in this deduction.
The additional geometric input is the pointwise plinth lemma in
[the peripheral-cycle proof](pointwise-plinth-pass17.md). That lemma
is a source-dependent working proof with a [completed separate audit](pointwise-plinth-audit-pass17.md), not a theorem
quoted verbatim from the literature. Equation (1) inherits that proof
dependency. Neither human expert review nor Lean verification has
occurred, and no novelty claim is made.

A [second adversarial audit](pointwise-plinth-second-audit-pass17.md)
also found no gap. Its quasi-affine control identifies the failed
homology step when an invariant line is removed from three-space.

The main algebraic step is that a hypothetical intersection of
\(B=0\) with the plinth support produces a faithfully flat family
over a discrete valuation ring whose entire special fiber is a reduced
line carrying a translation. The pointwise lemma then excludes the
intersection. The argument does not assume that invariants commute with
this base change.

## 1. Inputs and the elementary directions

The invariant ring is \(C\cong\mathbb C^{[2]}\), and the nonzero
plinth ideal is principal. Write \(P_D=p_D C\), choosing
\(r\in R\) with \(Dr=p_D\). These are the three-variable
results recorded in Freudenburg's Theorem 2.4.[^1] The quotient
\(\pi:\operatorname{Spec}R\to\operatorname{Spec}C\) is
surjective and faithfully flat, as recorded in Kaliman's Remark 3.3
in this setting.[^2]

Nonzeroness of \(P_D\) also follows directly: the last nonzero
iterate of \(D\) on a noninvariant polynomial is a nonzero invariant
in the image. Because \(A,B\) are invariant, the summands of
\(E\) commute and are locally nilpotent; their sum is locally
nilpotent by the binomial formula.

If \(A p_D U+BV=1\) for \(U,V\in C\), then

\[
s=Ur+Vt\in R[t],\qquad E(s)=A p_D U+BV=1.
\tag{2}
\]

This proves the middle-to-right direction of (1), and the
right-to-left direction is immediate. The affine criterion itself
can be checked without geometry. If \(A\ne0\) and
\(s=u+vt\), \(u,v\in R\), is a slice, comparison of
coefficients gives

\[
ADv=0,\qquad ADu+Bv=1.
\]

Thus \(v\in C\); applying \(D\) to the second equality gives
\(D^2u=0\). Therefore \(Du\in P_D\), proving
\(A P_D+BC=C\). If \(A=0\), the slice equation forces
\(B\) to be a unit of \(R\), hence a nonzero complex constant,
and the same criterion holds.

It remains to start with a slice of arbitrary degree in \(t\)
and prove the unit-ideal condition.

## 2. Two necessary conditions from an arbitrary slice

Suppose \(S\in R[t]\) satisfies \(E(S)=1\). Since
\(E(R[t])\subseteq(A,B)R[t]\), we have
\((A,B)R[t]=R[t]\). Evaluation at \(t=0\), followed by
faithful-flat contraction from \(R\) to \(C\), gives

\[
(A,B)C=C.
\tag{3}
\]

Equivalently, a common closed zero of \(A,B\) would lift through
the surjective quotient and make \(E\) vanish at every point of
the corresponding extended fiber, contradicting \(E(S)=1\).

The second input is the whole-component exclusion proved in
[the plinth-component note](whole-plinth-component-pass16.md):

\[
\gcd_C(B,p_D)=1.
\tag{4}
\]

For primitive \(D\), that deduction uses the actual finite curve
factorization and local transversal argument in Kaliman's proof, not
an arbitrary finite map of singular curves. For general \(D\), it
uses the invariant-replica reduction detailed below. Equation (4)
excludes common irreducible components, but by itself does not exclude
isolated intersection points. The remaining argument proves the
strictly stronger statement

\[
(B,p_D)C=C.
\tag{5}
\]

## 3. The pointwise input and invariant replicas

The pointwise lemma needed here has the following exact form.

**Pointwise input for a primitive derivation.** Let \(D_0\) be a
nonzero primitive LND of \(\mathbb C^{[3]}\), and let
\(C=\ker D_0\). If the entire scheme-theoretic quotient fiber at
a closed point \(p\in\operatorname{Spec}C\) is a reduced
single \(\mathbb A^1\) with nonzero translation action, then
\(p\notin V(P_{D_0})\).

The proof is given in [the pointwise note](pointwise-plinth-pass17.md),
Sections 1-5. Its substantive new step restricts the support of
peripheral cycles near the whole fiber and excludes normalization
branches not reached by that fiber. Flatness plus smoothness of the
scheme-theoretic fiber yields smoothness along the fiber by the
pointwise criterion in Stacks, Tag 01V9.[^3] A merely set-theoretic
line, or a generic-fiber assertion, is not this input.

For completeness, the same implication holds for every nonzero
\(D\), once the primitive input is supplied. Let \(h\) be the
greatest common divisor of the three polynomial coefficients of
\(D\), and write \(D=hD_0\). Then

\[
h\in C=\ker D_0=\ker D,\qquad
D_0\in\operatorname{LND}(R),\qquad
P_D=hP_{D_0}.
\tag{6}
\]

Here is an elementary justification of the replica assertion. The
polynomial \(h\) divides \(Dh\). For an LND on a domain of
characteristic zero, derivation degree is additive on nonzero
products, whereas applying \(D\) to a noninvariant element lowers
degree by one. Consequently a polynomial dividing its own derivative
has derivative zero. Thus \(Dh=0\), hence \(D_0h=0\);
the identities \(D^j u=h^jD_0^j u\) prove local nilpotence of
\(D_0\). Cancellation by \(h\) proves equality of kernels,
and \(hD_0u\) is invariant exactly when \(D_0^2u=0\),
which proves the plinth identity in (6).

If the quotient fiber at \(p\) carries a nonzero translation by
\(D\), then \(h(p)\ne0\). Indeed \(h(p)=0\) would make
the induced derivation on the entire fiber zero. Hence \(D_0\)
also induces a nonzero translation, scaled by \(h(p)^{-1}\).
The primitive input gives \(p\notin V(P_{D_0})\), and (6)
then gives \(p\notin V(P_D)\). We will use this unrestricted
version of the pointwise input in Section 6.

## 4. A normalized component of the zero locus of \(B\)

For the moment suppose \(A\ne0\), \(B\ne0\), and
\(B\) is not a unit. Assume, for a contradiction, that (5)
fails. The Nullstellensatz gives a closed point

\[
p\in V(B)\cap V(p_D)\subset\operatorname{Spec}C.
\tag{7}
\]

Choose an irreducible factor \(b\) of \(B\) with \(b(p)=0\).
Equation (4) implies that \(b\nmid p_D\). Thus the integral
affine curve

\[
\Lambda=\operatorname{Spec}(C/(b))
\]

is not contained in \(V(p_D)\). Normalize \(\Lambda\),
choose a point \(\widetilde p\) over \(p\), and let

\[
V=\mathcal O_{\widetilde\Lambda,\widetilde p},\qquad
L=\operatorname{Frac}(V),\qquad
\varpi\text{ a uniformizer of }V.
\tag{8}
\]

Finite surjectivity of normalization guarantees such a point; its
one-dimensional normal local ring is a DVR.[^4][^5] Its residue field
is \(\mathbb C\), because the normalization is finite over an
affine complex curve and \(p\) is a closed complex point.

The composite map \(C\to C/(b)\to V\) has kernel exactly
\((b)\). Consequently \(B\) maps to zero, whereas \(p_D\)
maps to a nonzero element of \(\varpi V\). No smoothness or
transversality of \(\Lambda\) at \(p\) is required. Repeated
factors of \(B\) have no effect on the choice of this reduced
component or on the validity of the base-changed slice equation.

## 5. Faithful flatness and the no-pole invariant calculation

Form

\[
T=R\otimes_C V
\]

and let \(D_V\) be the derivation induced by \(D\), acting
trivially on \(V\). Local nilpotence survives this base change:
each tensor is a finite sum, so one common sufficiently high iterate
annihilates all its summands. Faithful flatness of \(R\) over
\(C\) makes \(T\) faithfully flat over \(V\). In particular,

\[
T\hookrightarrow T_L:=T\otimes_V L,
\qquad T/\varpi T\ne0.
\tag{9}
\]

The injection follows from flatness, hence torsion-freeness over the
domain \(V\); the nonzero special fiber uses faithfulness as well.
We do not infer that an arbitrary base change of the domain \(R\)
is a domain.

The image of \(p_D\) is invertible in \(L\). The local-slice
identity gives

\[
R_{p_D}=C_{p_D}[r/p_D],\qquad D(r/p_D)=1.
\]

Therefore, after the base change to \(L\),

\[
T_L=L[\rho],\qquad D_L\rho=1,
\qquad \ker D_L=L.
\tag{10}
\]

Equations (9)-(10) prove that \(T\) is a domain. They also reduce
its invariant-ring calculation to

\[
\ker D_V=T\cap L=V.
\tag{11}
\]

Indeed an invariant in \(T\) becomes an element of \(L\) by
(10). If \(u\varpi^{-n}\in L\setminus V\), where
\(u\in V^*\) and \(n>0\), belonged to \(T\), then
multiplication by \(u^{-1}\varpi^{n-1}\in V\) would put
\(\varpi^{-1}\) in \(T\). This would contradict
\(T/\varpi T\ne0\). The reverse inclusion \(V\subseteq
\ker D_V\) is part of the construction. This is the required
no-pole proof; no general base-change theorem for invariant rings
is being invoked.

## 6. The slice equation forces the entire forbidden fiber

Write the original slice as

\[
S=\sum_{j=0}^N r_jt^j\in R[t].
\]

Base change sends it to a polynomial \(\overline S\in T[t]\)
and preserves the equation \(E(S)=1\). Since \(B\) maps to
zero, the induced derivation is \(\overline A D_V\), with
\(t\) invariant. Its constant coefficient gives

\[
\overline A D_V(\overline r_0)=1.
\]

Because \(\overline A\in V\) is invariant, the element
\(u=\overline A\,\overline r_0\in T\) satisfies

\[
D_Vu=1.
\tag{12}
\]

The characteristic-zero slice theorem, together with (11), now gives

\[
T=(\ker D_V)[u]=V[u].
\tag{13}
\]

This use of the slice theorem needs no threefold cancellation result.
One proves it directly by induction on derivation degree: subtract the
invariant leading coefficient times the appropriate power of the
slice, divided by its factorial. The resulting induction expresses
every element of \(T\) as a polynomial in \(u\) over its kernel;
applying a highest derivative proves algebraic independence of \(u\).

Reducing (13) modulo \(\varpi\) gives

\[
R\otimes_C\mathbb C_p
\;\cong\;T/\varpi T
\;\cong\;\mathbb C[\overline u],
\qquad D_p\overline u=1.
\tag{14}
\]

The first equality is associativity of tensor product and the fact
that \(V\to V/\varpi V=\mathbb C\) lies over the specified
closed point \(p\). It identifies the entire original
scheme-theoretic quotient fiber, not a component of that fiber and
not a nonempty open subset. Thus the fiber is a reduced single line,
and \(D\) acts on it by a nonzero translation.

The pointwise input, extended to replicas in Section 3, now gives
\(p\notin V(P_D)\), contradicting (7). This proves (5).

## 7. The unit ideal and all boundary cases

Combine (3) and (5). In \(C/(B)\), both the image of \(A\)
and the image of \(p_D\) are units, so their product is a unit.
Equivalently,

\[
(A p_D,B)C=C,
\qquad\text{that is,}\qquad A P_D+BC=C.
\tag{15}
\]

One may make this implication explicit. If
\(Aa+Bb=1\) and \(p_Dc+Bd=1\), their product is

\[
1=A p_Dac+B\bigl(Aad+bp_Dc+Bbd\bigr).
\]

Equation (2) then constructs an affine replacement. Its existence
does not imply that every original slice was affine.

The excluded coefficient cases agree with the same criterion.

- If \(B\in\mathbb C^*\), then \(t/B\) is a slice and
  \(A P_D+BC=C\), for every \(A\).
- If \(A=0\), a slice exists exactly when \(B\) is a nonzero
  constant, as proved in Section 1. In particular \(A=B=0\)
  gives neither a slice nor the unit ideal.
- If \(B=0\) and a slice exists, its constant coefficient gives
  \(A Dr_0=1\) in \(R\). Thus \(A\in\mathbb C^*\)
  and \(Dr_0=A^{-1}\), so \(P_D=C\) and (15) holds.
  Conversely those conditions produce a slice in \(R\) itself.
- If \(P_D=C\), the derivation \(D\) already has a slice.
  The criterion is simply \((A,B)C=C\); no intersection argument
  is required. Formula (2) still applies with \(p_D=1\).

There is no primitive-action restriction left in (1). Invariant
replicas with nonconstant \(h\), and arbitrary multiplicities in
\(p_D\) or \(B\), are included. The ambient hypothesis
\(R=\mathbb C^{[3]}\) is essential to the geometric inputs;
the [localized cubic-slice example](../deep-pass-16.md) shows that
affine replacement need not survive arbitrary invariant localization.

## 8. Mathematical scope and verification boundary

The result is an affine-replacement theorem for extensions already
presented as \(AD+B\partial_t\), with both coefficients invariant
under a nonzero LND of polynomial three-space. The proof does not use
principality or saturation of \(D^j(R)\cap C\) for \(j\ge2\).
It therefore closes that part of the argument without proving the
general Freeness Conjecture. It does not imply that those higher image
ideals are principal.

An affine slice only gives

\[
R[t]=(\ker E)[s].
\]

It does not by itself identify \(\ker E\) with
\(\mathbb C^{[3]}\), construct a polynomial coordinate frame for
that kernel, or show that every slice LND on \(\mathbb C^{[4]}\)
admits the invariant-extension presentation used here. Those remain
separate requirements for the full complex threefold cancellation
problem

\[
X\times\mathbb A^1\cong\mathbb A^4
\quad\Longrightarrow\quad X\cong\mathbb A^3.
\]

That full problem is not solved by this note. The current proof status
is a complete algebraic deduction from the two explicitly linked
source-dependent geometric arguments. A finite list of polynomial
tests cannot verify the pointwise topological lemma, and multiple
model audits are not a substitute for human expert review or a formal
proof. A revision to either geometric input must propagate to the
status of (1).

## Sources

[^1]: Gene Freudenburg, [*Actions of SL2(k) on affine k-domains and fundamental pairs*](https://arxiv.org/pdf/2108.12021v2), arXiv:2108.12021v2, June 7, 2022, Theorem 2.4. Used for the polynomial-plane kernel and principal plinth ideal; its higher-image freeness definition in Section 2.2 is not an additional hypothesis here.

[^2]: Shulim Kaliman, [*Free C+-actions on C3 are translations*](https://www.math.miami.edu/~kaliman/library/Ka.invent.2004.c%2B.pdf), final author version, Remark 3.3. Surjectivity and faithful flatness are the direct inputs here. The separate whole-component and pointwise notes document their additional uses of Lemmas 2.1-2.2, Proposition 3.2, Proposition 4.2, and Theorem 5.2(i).

[^3]: The Stacks Project, [Lemma 29.35.14, Tag 01V9](https://stacks.math.columbia.edu/tag/01V9). The exact pointwise flat-plus-smooth-fiber criterion used in the geometric input.

[^4]: The Stacks Project, [Lemma 33.41.2, Tag 0C1R](https://stacks.math.columbia.edu/tag/0C1R). Finite surjective normalization of reduced Nagata curves.

[^5]: The Stacks Project, [Lemma 33.27.6, Tag 0C3P](https://stacks.math.columbia.edu/tag/0C3P), including its proof. The one-dimensional normal local ring of the normalized curve is a DVR.
