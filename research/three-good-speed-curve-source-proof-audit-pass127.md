# Source and independent proof audit of speed-curve recognition

## 1. Verdict and exact statement

The complete [speed-curve recognition proof127](three-good-speed-curve-recognition-pass127.md)
reconstructs without a mathematical gap found in this bounded audit.
Its statement concerns an actual sliced derivation on
\(B=\mathbb C[x_1,x_2,x_3,z]=A[u]\), with \(Eu=1\),
\(E^2x_i=0\), and
\(\operatorname{trdeg}_{\mathbb C}\mathbb C[Ex_1,Ex_2,Ex_3]\le1\).
It concludes \(A\simeq\mathbb C^{[3]}\), with no bound on
\(\deg_Ez\). The invariant ambient coordinate is constructed
before applying a published regular-kernel theorem.

This is an independent reconstruction of a working proof, not
external certification or a claim of publication novelty. The final
main-proof SHA-256 is
`47a61666fa56c3d0b4528250aa0fff721fd8811138d2567d147000466db30660`.
The nine equations were read completely before the final elementary
\(p_z=0\) replacement; that complete replacement and the revised
dependency paragraph were then read separately.

## 2. The two primary inputs and nearby results

[De Bondt, Corollary 3.2 and Lemma 3.3](https://arxiv.org/html/1501.06046)
give a polynomial parameter for a transcendence-degree-one
subalgebra of a polynomial ring: if its fraction field is \(L\),
there is \(p\in K[x]\) with \(L=K(p)\) and the subalgebra contained
in \(K[p]\). The complete displayed corollary and lemma proofs
were freshly read. This supplies a polynomial \(p\) for the speed
algebra, not an ambient coordinate, and does not include an unrelated
acceleration in that algebra. The earlier theorem dependencies of
the corollary were not all freshly reconstructed in this pass.

[Bhatwadekar, Gupta and Lokhande, Theorem 3.5](https://arxiv.org/html/1501.01438v1)
applies to a nonzero locally nilpotent \(k[T]\)-derivation of the
actual ring \(k[T,X,Y,Z]\), in characteristic zero, whose kernel
is regular. It concludes that the kernel is \(k[T]^{[2]}\).
The complete statement and displayed short proof were freshly
read. Its DVR and local-to-global dependencies were not fully
reproved here. In the audited application, \(T\) is the invariant
actual coordinate produced by the proof; regularity follows from
the actual slice. Thus neither prerequisite is supplied by an
unproved generic-coordinate assertion.

The following comparisons do not replace those two inputs.

- [Dasgupta and Gupta, Theorem 4.1](https://arxiv.org/html/1701.03635v1)
  records Wang's classification of irreducible derivations of
  \(K[X,Y,Z]\) with \(D^2X=D^2Y=0\). It has three variables over
  a field, not the present four-variable hypothesis. Their
  Proposition 4.4 requires an actual \(R^{[3]}\) over a PID and
  a specified generic alternative. Neither follows merely from
  the polynomial speed parameter. Theorem 3.1(i), for nice
  derivations on \(K^{[3]}\), corroborates the former
  \(p_z=0\) endpoint but is no longer a dependency. These
  statements were freshly read; Wang's original proofs were not.
- [Dasgupta and Lahiri, Definitions 2.2--2.3 and Theorems 4.1, 5.2, 5.9](https://arxiv.org/html/2302.13787v6)
  make the present action three-quasi-nice in their terminology,
  without asserting strictness. The cited image-ideal theorems
  concern actual relative two-variable polynomial rings with
  additional hypotheses. In particular, Theorem 5.2 assumes
  the action is not fixed point free and prescribes a triangular
  coefficient row. A slice here supplies fixed-point-freeness,
  not that relative presentation. The definitions and selected
  theorem statements were freshly read; the displayed proof
  of Theorem 5.2 was also read, not its full dependency tree.

The rank appearing in those classification results is ambient
coordinate rank. It must not be substituted for the transcendence
degree of the three speeds. This bounded primary-source comparison
did not locate a theorem directly giving the complete statement
in Section 1; that is not an exhaustive literature search or
novelty clearance. It supplements, rather than rebrands, the
[earlier source comparison125](source-audit-pass125.md).

## 3. Independent audit of the algebraic gates

Polynomial curve factorization is used only on the three speeds.
Differentiating a nonconstant \(f_i(p)\) gives \(Ep=0\).
For the univariate gcd \(b\) of their coefficient polynomials,
the slice makes \(c=Ez\) a unit modulo the full ideal \((b(p))\).
Consequently \(b(p)\mid p_z\), including multiplicities. A
nonconstant \(b\) contradicts the original \(z\)-degree when
\(p_z\ne0\). No radical contraction is substituted here.

The final \(p_z=0\) proof is elementary. Write
\(f(T)=\sum v_kT^k\), \(L_k=v_k\cdot\partial_{\rm good}\),
and \(d=\deg p\). Nonzero summands in
\(\sum p^kL_kp=0\) have distinct total degrees, since each lies
between \(kd\) and \((k+1)d-1\). Therefore all \(L_kp\) vanish.
The coefficient vectors cannot span \(\mathbb C^3\), or \(p\)
would be constant. A constant annihilator supplies the invariant
linear coordinate. The argument uses distinct total degrees,
not disjoint homogeneous supports of the summands.

For \(\alpha=p_z\ne0\), the inverse-Jacobian column for the
selected original partial uses only the three good rows.
Two copies of \(dp\) wedge to zero. This proves
\(\exp(tE)\partial_z\exp(-tE)=\partial_z+tQ\), hence
\([E,Q]=0\). The actual polynomial flow has determinant one;
its linear coefficient gives the divergence identity used for
\(Qp=E\alpha=0\). No bound on the fourth flow coordinate is
required. The Laurent conjugation construction of \(Q\) preserves
\(B[\varepsilon]\), fixes \(\varepsilon\), and specializes an
LND to an LND. It does not invert an element moved by the
original partial.

The determinant quotient in the main proof is an identity over
\(B/(\alpha)\), which may be nonreduced. Finite polynomial
coefficient comparison proves
\(\alpha\mid\delta^{\ell+1}\), with
\(\delta=(Ez)_z\), \(\ell=\deg_Ez\). The scalar recursion in
that proof independently checks the same exponent. The gcd
argument keeps every prime multiplicity: if
\(d_0=\gcd(\alpha,\delta)\), then
\(d_0\mid Qd_0\) gives \(Qd_0=0\), while
\(\alpha\mid d_0^{\ell+1}\) gives \(Q\alpha=0\) by factorial
closure. The unit and zero-coefficient edge cases are harmless.

The primitive univariate normal to \(f,f'\) is unimodular, so
the proportionality coefficient of the polynomial Wronskian
vector is genuinely in \(B\). This polynomiality is what makes
the \(z\)-degree contradiction valid. Degree-zero and degree-one
normals are treated explicitly, not discarded. If all Wronskians
vanish, the leading coefficient of \(p\) in \(z\) is a complex
unit; the ratio \(p_{x_i}/p_z\) is independent of \(z\), and
its leading coefficient supplies a polynomial gradient.
The result is the actual inverse pair \(v=z+H(x)\),
\(z=v-H(x)\), including \(\deg_zp=1\). The conclusion is
\(p=F(v)\), not the unsupported assertion that \(p\) itself
is a coordinate.

Finally, \(A\cong B/(u)\) and \(Eu=1\) show that this
hypersurface is smooth: the partial derivatives of \(u\)
generate the unit ideal. Thus \(A\) is regular. The constructed
invariant coordinate, the nonzero action, the actual polynomial
presentation, and characteristic zero check every hypothesis
of the stated regular-kernel endpoint.

## 4. A separate Riccati quotient reconstruction

There is another way to obtain the content needed for
\(Q\alpha=0\), without computing the precise exponent
\(\ell+1\). Retain the actual notation of the main proof and put
\(C_0=f'(p)\cdot\nabla_{\rm good}c\). The coefficient row of
\(Q\), together with \([E,Q]z=0\), gives
\[
Qc=-\alpha C_0-\delta^2=-E\delta,
\qquad E\delta=\alpha C_0+\delta^2,
\qquad E\alpha=0.
\tag{1}
\]
The last equality makes \((\alpha)\) an \(E\)-stable ideal.
The induced derivation on its quotient remains locally nilpotent.
Even in this possibly nonreduced ring, induction and the product
rule give
\[
\overline E(\overline\delta)=\overline{\delta}^{2},
\qquad
\overline E^{j}(\overline\delta)
   =j!\,\overline{\delta}^{j+1}.
\tag{2}
\]
Local nilpotence and characteristic zero imply
\(\alpha\mid\delta^M\) for some finite \(M\ge1\).
For \(d_0=\gcd(\alpha,\delta)\), prime-by-prime comparison
then gives \(\alpha\mid d_0^M\). Since every coefficient of
the LND \(Q\) is divisible by \(d_0\), LND degree additivity
gives \(Qd_0=0\), followed by \(Q\alpha=0\).
This alternative proves exactly the content needed for the
Wronskian step. It neither assumes a reduced quotient nor
claims the sharp exponent without the separate finite-flow
argument.

## 5. Read scope and remaining boundary

This audit includes complete saved reads of the main proof and
the retained polynomial-curve source, nice-linear-invariant71,
cofactor126, and relevant joint-curve/common-kernel/unit-normal-form
proofs. The final main-proof delta removes nice-three
classification from the required chain. Primary reads are the
selected statements and proofs identified in Section 2, not
whole-paper or recursive proof-tree audits. No numerical test,
historical-suite rerun, or frozen-file edit was performed.

The separate [canonical-volume result127](three-good-canonical-volume-factorization-pass127.md)
was also reconstructed completely, but it is not an input here.
Its finite-field and affine-modification questions therefore
cannot block this recognition theorem. The speed-rank-one
unit joint-curve frontier of126 is subsumed, without changing
its frozen record. Speed rank two and the existence of a
three-good frame for an arbitrary sliced four-variable action
remain unproved. An abstract numerical partial-degree profile
alone is not being recognized.
