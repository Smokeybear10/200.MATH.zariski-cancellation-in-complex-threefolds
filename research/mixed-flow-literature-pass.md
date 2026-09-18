# Mixed-flow bounds and global descent: literature audit

The bounded primary-source search did not locate a rank or translation
theorem covering the remaining mixed height-nine branch. The useful
global endpoints found require a polynomial invariant base, a verified
affine-space fibration, a globally patchable coordinate tuple, or a
triangular form. None was verified to follow just from the mixed
commutator identities. This records coverage, not novelty or openness.

## 1. The exact target and the degree distinction

Write \(B=\mathbb C[x_1,x_2,x_3,x_4]\), \(D(s)=1\), and
\(\Phi_t=\exp(tD)x\). The branch under investigation satisfies
\[
\operatorname{ad}_D^2(\partial_i)=0\quad(i\leq3),
\qquad \operatorname{ad}_D^3(\partial_4)=0.
\]
With the column convention in
[the height-nine calculation](height-nine-first-pass.md), this gives
\[
(\operatorname{Jac}\Phi_t)^{-1}
=I-tJ+\frac{t^2}{2}v e_4^{\mathsf T},
\qquad \det(\operatorname{Jac}\Phi_t)=1.
\]
The cofactor bound yields \(D^5x_i\in\mathbb C\) and \(D^6x_i=0\).
These are consequences of that calculation, not statements attributed
to a source below.

A bound on \(\deg_t\Phi_t\) is not an ordinary-degree bound on \(Dx_i\).
For example, \(\partial_w+h(x)\partial_y\) has a slice and time-degree
one for any polynomial \(h\), of arbitrarily large ordinary degree.
The inverse-Jacobian column condition also contains more information
than the time-degree bound alone.

The polynomial-flow and full Jacobian-dual-frame criteria were checked
in [the preceding statement audit](height-eight-statement-literature-addendum.md).
They do not supply a four-variable recognition theorem at time-degree
five. The ordinary-quadratic Jacobian results in
[the preceding literature note](height-eight-literature-pass.md)
retain their ordinary-degree assumptions.

## 2. Nice and quasi-nice derivations: exact nearby scope

[Dasgupta and Gupta, *Nice derivations over principal ideal domains*,
Theorem 3.6 and Corollary 3.8](https://arxiv.org/pdf/1701.03635)
prove a rank bound and polynomial kernel for an irreducible nice
\(R\)-LND of \(R[X,Y,Z]\), with \(R\) a PID containing \(\mathbb Q\).
The four-variable corollary assumes \(DX_1=0\) and
\(D^2X_i=0\) for \(i=2,3,4\).

Their terminology “\(m\)-quasi” means that \(D^2\) annihilates \(m\)
members of some coordinate system. It does not refer to iterated
commutators with \(m\) coordinate partials.

Example 4.5 is a useful guardrail:
\[
D(t)=0,\quad D(X)=t,\quad D(Y)=tZ+X^2,\quad D(Z)=-2X.
\]
It has time-degree two, but its kernel is the singular algebra
\[
\mathbb C[t,F,G,H]/(F^2-G^3-tH).
\]
It has no slice: the coefficient ideal vanishes when \(t=X=0\).
Thus it is not a counterexample to the slice target. It does show
that small time-degree alone does not force a polynomial kernel.

## 3. A genuine coordinate-tuple patching theorem

[Derksen, van den Essen and van Rossum, *The Cancellation Problem in
Dimension Four*, Corollary 3.10](https://www.researchgate.net/publication/228571174_The_cancellation_problem_in_dimension_four)
states: if \(R\) is a Hermite domain and a fixed tuple
\((h_1,\ldots,h_r)\subset R[X_1,\ldots,X_n]\) is a partial coordinate
system over \(R_{\mathfrak m}\) for every maximal ideal \(\mathfrak m\),
then it is a partial coordinate system over \(R\).
Theorem 3.9 is the normalized version with prescribed identity linear
terms; Lemma 3.8 patches two principal open sets.

The same original report proves in Theorem 4.4 that a slice \(R\)-LND
of \(R[X,Y,Z]\), for a Dedekind domain \(R\supset\mathbb Q\), has
kernel \(R^{[2]}\). Corollary 4.5 closes a slice LND on \(k^{[4]}\)
if one ambient coordinate \(W\) satisfies \(D(W)\in k[W]\).

This is useful global descent, but requires a fixed polynomial
presentation over \(R\) and the same tuple at every localization.
Generic coordinates, unrelated local invariant tuples, or smoothness
of an unknown quotient do not supply those premises.

## 4. Affine-fibration recognition does not erase relative dimension

[Babu, Das and Lokhande, *Rank and rigidity of locally nilpotent
derivations of affine fibrations*, Corollary 3.11](https://arxiv.org/pdf/2210.10285)
concerns an \(\mathbb A^3\)-fibration \(A\) over a Noetherian domain
\(R\supset\mathbb Q\) and a fixed-point-free \(R\)-LND \(D\).
A slice is equivalent to residual rank at most two, and to
\(\ker D\) being an \(\mathbb A^2\)-fibration with
\(A=(\ker D)^{[1]}\).

Definition 3.1 requires, for residual rank \(r\), an invariant
\(\mathbb A^{n-r}\)-fibration subalgebra whose inclusion becomes a
polynomial extension by \(r\) variables on every base fiber.
This is not the generic rank of commuting vector fields.
Over a field, it reduces to ordinary LND rank.

A possible endpoint is an invariant \(a\) for which \(B\) is proved
to be an \(\mathbb A^3\)-fibration over \(\mathbb C[a]\).
The corollary then supplies an \(\mathbb A^2\)-fibration kernel;
the established affine-plane-fibration theorem over this base closes.
The mixed time bound does not verify that fibration hypothesis.
Taking \(R=\mathbb C\) instead makes the relative dimension four.
Remark 3.10 explicitly explains why the slice argument cannot simply
be extended to that dimension.

## 5. Proper triangular actions: properness is already available

[Dubouloz, Finston and Jaradat, *Proper triangular
\(\mathbb G_a\)-actions on \(\mathbb A^4\) are translations*,
main theorem and corollaries, pp. 1963–1964](https://msp.org/ant/2014/8-8/ant-v8-n8-p06-s.pdf)
prove that a proper locally triangulable action on a locally trivial
\(\mathbb A^3\)-bundle over a normal base has an
\(\mathbb A^2\)-bundle quotient outside codimension at least two.
Over an affine Dedekind base, the vector-bundle case has a rank-two
vector-bundle quotient. In particular, every proper triangular action
on \(\mathbb A^4\) in characteristic zero is a translation.

The triangle condition concerns a suitable polynomial coordinate
system, not a time-degree bound. It is the missing hypothesis here.

Indeed, a slice already writes \(B=K[s]\). The action is translation
on \(\operatorname{Spec}K\times\mathbb A^1\); its action morphism into
the square of that product is a closed immersion, since it identifies
with the locus where the two \(\operatorname{Spec}K\) coordinates agree.
Thus the action is proper. Its affine quotient is
\(\operatorname{Spec}K\), of dimension three, not automatically
\(\mathbb A^3\). Properness adds no new information to this slice setup.

## 6. The available torus is a reformulation, not automatic descent

The slice gives a torus action
\[
\lambda\cdot a=a\quad(a\in K),\qquad
\lambda\cdot s=\lambda s,
\]
on \(B=K[s]\). Its invariant ring and fixed locus are both \(K\).
If this particular action is linearizable on \(\mathbb A^4\), its
fixed locus becomes a linear three-space, so \(K\cong\mathbb C^{[3]}\).
Conversely, a polynomial coordinate system on \(K\), together with
\(s\), linearizes it. This elementary equivalence identifies a global
alternative to frame minimization, but is not itself a proof of
linearizability.

[Masuda, *Equivariant embeddings and semi-invariant locally nilpotent
derivations*, Proposition 5.2](https://sci-tech.ksc.kwansei.ac.jp/~kayo/cmn/papers/eembed.pdf)
contains a related linearization-versus-kernel-recognition equivalence
for the paper's specified semi-invariant commuting derivation systems.
Theorem 5.5 proves equivariant rectifiability for embeddings of complex
torus representations when the target representation has quotient
dimension at most one. Neither the special derivation form nor that
low-dimensional torus quotient has been established for the mixed
branch. The mere presence of the slice-scaling torus does not meet
those hypotheses.

## Bounded conclusion

The exact global targets worth retaining are an invariant
one-dimensional base with an actual \(\mathbb A^3\)-fibration, a
common coordinate tuple satisfying local patching hypotheses, or
linearization of the slice-scaling torus. Each is a concrete
recognition problem; none was proved automatic by the sources checked.

The search covered bounded coordinate nilpotency, strict polynomial
flows, mixed commutators, nice derivations, proper actions, and
coordinate patching. Mathematical claims above use original papers or
author-uploaded original reports. The Masuda title *Torus actions and
kernels of locally nilpotent derivations with slices* was located
bibliographically, but its complete statement was not recovered in
this pass and is not being used as a theorem. No claim of novelty
or exhaustive coverage follows from the unsuccessful exact search.
