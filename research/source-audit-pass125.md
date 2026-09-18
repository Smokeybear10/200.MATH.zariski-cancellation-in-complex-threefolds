# Source audit: supplied quasi-nice frames and the common speed kernel

## 1. Outcome and exact target

The selected published classification implies the speed-dependence claim
in three variables. Its hypotheses do not directly cover the four-variable
case. The general leading-LND construction is published and already retained
in this project; the useful application in pass125 is that one such intrinsic
action fixes **all the specified good-coordinate speeds**. This is not a
historical novelty claim or a recognition theorem.

Let \(n\ge2\) and let \(E\) be locally nilpotent. The supplied setup is
\[
 B=\mathbb C[x_1,\ldots,x_{n-1},z]=A[u],\qquad
 A=\ker E,\qquad E(u)=1,\qquad E^2x_i=0,
 \qquad a_i=Ex_i.
 \tag{1}
\]
There is no degree bound on \(z\). A slice makes \(E\) irreducible:
any principal ideal containing \(E(B)\) contains \(E(u)=1\).
The [volume-rank proof](three-good-speed-rank-bound-pass125.md) proves
\(\operatorname{trdeg}_{\mathbb C}\mathbb C[a_i]\le n-2\).
The [intrinsic-speed proof](three-good-intrinsic-speed-quotient-pass125.md)
proves the stronger common-kernel assertion when some \(a_i\ne0\).
Both saved proofs were independently reconstructed through EOF for this audit.

## 2. What the quasi-nice classifications actually cover

Dasgupta--Lahiri's Definitions 2.2--2.3 use *\(m\)-quasi-nice* for an
actual polynomial coordinate system with \(D^2X_i=0\) for its first
\(m\) variables. Thus (1) is literally \((n-1)\)-quasi-nice; it need
not be *strictly* so. Their principal image-ideal theorems concern actual
\(R[X_1,X_2]\) over a UFD. Theorem 5.2 additionally assumes a
non-fixed-point-free action and an irreducible first image in \(R\),
so it is not a sliced four-variable classification. Lemma 2.12(i),
attributed to Wang, already gives dependence in dimension two: its
good speed lies in the coefficient field.
[Dasgupta--Lahiri, Definitions 2.2--2.3, Lemma 2.12 and Theorems 4.1, 5.2](https://arxiv.org/html/2302.13787v6).

For a characteristic-zero field \(K\), a nonzero irreducible LND on
the **actual** ring \(K[X,Y,Z]\) with \(D^2X=D^2Y=0\) has one of
two forms. Either a constant linear combination of \(X,Y\) is invariant,
or there is an invariant coordinate \(V\) with \(DX,DY\in K[V]\).
Hence the two speeds are algebraically dependent. This is Wang's
Theorem 4.7 and Remark 5, restated as Dasgupta--Gupta Theorem 4.1.
It covers (1) for \(n=3\), even without a slice once irreducibility is
assumed.
[Dasgupta--Gupta, Theorem 4.1](https://arxiv.org/html/1701.03635v1).

This comparison does not reduce \(n=4\) to \(n=3\). Localizing an
unknown invariant subring does not exhibit an actual polynomial
three-ring over its fraction field. Algebraic dependence of the speeds
also does not provide an invariant ambient coordinate. These are missing
hypotheses, not consequences of the displayed classifications.

## 3. Rank and relative-polynomial-ring hypotheses

The published rank measures how many **ambient polynomial coordinates**
remain outside the kernel, not the transcendence degree of selected
speeds. Dasgupta--Gupta's Theorem 2.5 restates the two-variable
fixed-point-free/slice criterion, attributed to Freudenburg's Theorem 4.16:
for an actual \(R[X,Y]\) over a \(\mathbb Q\)-algebra, either condition
gives \(\ker D=R^{[1]}\).
[Dasgupta--Gupta, Section 2 and Theorem 2.5](https://arxiv.org/html/1701.03635v1).

The same actual two-variable premise appears in the UFD theorem of
Daigle--Freudenburg, restated in that paper as Theorem 2.2.
Its original publication is
[Daigle--Freudenburg, *Locally Nilpotent Derivations over a UFD and an Application to Rank Two Locally Nilpotent Derivations of k[X1,...,Xn]*](https://doi.org/10.1006/jabr.1998.7465).
The original proof was not freshly read here. None of these statements
licenses replacing the coefficient ring by a speed algebra and silently
asserting \(B=R^{[2]}\).

In dimension four the new intrinsic-speed note instead invokes the
already retained [intrinsic quotient-surface theorem](intrinsic-quotient-surface-pass.md).
Its conclusion \(S=\ker N\simeq\mathbb C^{[2]}\), with faithful flatness,
has those geometric source dependencies. It is not a deduction from
the rank bound, and this source audit does not repeat that primary-proof audit.

## 4. The leading-LND mechanism has an exact published source

Daigle's Theorem 1.7(a),(d) and Corollary 4.12 establish bounded derivation
degree for the relevant grading or LND filtration. Section 1.9 states
that the associated homogeneous derivation is nonzero when the original
one is nonzero and remains locally nilpotent. The warning in the
introduction matters: arbitrary degree functions on affine domains need
not have this boundedness property. Here the actual \(u\)-grading
\(B=A[u]\), with \(A\) affine, is within the stated hypotheses.
[Daigle, *Tame and wild degree functions*, Theorem 1.7, Section 1.9 and Corollary 4.12](https://arxiv.org/html/1007.0508v1).

Alhajjar's Proposition 2.2 attributes the LND-filtration statement to
Daigle. The proof of Proposition 3.4, attributed to Makar-Limanov,
uses precisely the next mechanism: a nonnegative-degree homogeneous
LND on \(A[u]\) kills \(u\), factors as \(u^dN\), and produces an
LND of \(A\). That proposition concludes semi-rigidity when \(A\)
is rigid; its construction, not a rigidity assumption on the present
\(A\), is the relevant comparison.
[Alhajjar, *LND-Filtrations and Semi-Rigid Domains*, Propositions 2.2 and 3.4](https://arxiv.org/html/1501.00445v1).

The project already used this mechanism in
[intrinsic-actions, Sections 2 and 5](intrinsic-actions-pass.md) and
[leading-derivation23, Section 1](leading-derivation-pass23.md).
Pass125 supplies the additional coefficient identity. With the actual
partial \(T=\partial_z\), some nonzero \(a_i\) forces \(T(A)\ne0\).
Its leading LND has \(H=u^dN\), \(H(u)=0\), \(d\ge0\).
Writing \(x_i=b_i+a_i u\), the top coefficient in \(T(x_i)=0\) gives
\[
 0=[u^{d+1}]\big(T(b_i)+uT(a_i)+a_iT(u)\big)=N(a_i).
 \tag{2}
\]
The new note proves the degree bound, specialization, and local
nilpotence on the actual rings, including \(d=0\). The analogous top
coefficient in \(T(z)=1\) kills the leading coefficient of \(z\)
when its \(E\)-degree is positive. Thus a quadratic acceleration belongs
to the same \(\ker N\). These are the specific common-kernel conclusions
being added to the ledger, not a new general homogenization theorem.

## 5. Reading scope and remaining boundary

Fresh primary-text reading for this comparison included the complete
displayed selected statements above, Dasgupta--Gupta's Proposition 4.4
and Example 4.5 proofs, Alhajjar's Proposition 3.4 proof, and Daigle's
Section 1.9, Proposition 4.6, Corollaries 4.7--4.8, Lemma 4.11 and
Corollary 4.12 statements and displayed proofs. It did not recursively
reaudit all their cited dependencies. Wang's original
[2005 paper](https://doi.org/10.1016/j.jpaa.2004.08.006), the original
Daigle--Freudenburg proof, and Freudenburg's book proof were not obtained
and freshly reconstructed; the exact uses above are research-paper
restatements, explicitly identified as such.

This bounded search did not locate a directly applicable published
all-dimensional classification with precisely (1). That observation
does not prove novelty, an open-problem status, or the nonexistence of
another theorem. The useful next input is already proved in the new
intrinsic-speed note: all supplied speeds, and a quadratic acceleration,
can be placed in a common intrinsic quotient. The independent volume
proof verifies a weaker consequence and is not a second new structural
theorem. Neither result supplies the frame for an arbitrary sliced
derivation, proves that the intrinsic action is free, or recognizes
every supplied three-good-coordinate action.

No tests were run for this audit. No file through pass124, mathematical
proof125, or live index was edited. This is a scoped source comparison
and AI proof reconstruction, not external expert validation.
