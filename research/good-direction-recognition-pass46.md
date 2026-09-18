# An omitted good direction recognizes the original kernel

The zero-motion proof requires less than a distinguished highest-flow
direction or a two-quadratic defect frame. Two actual good partials and
a common invariant omitting any one of their constant directions suffice.
This recognizes some moving-highest-direction cases without asserting
that the canonical direction itself has zero motion.

## 1. Statement on the actual four-ring

Let \(B=\mathbb C[x_1,x_2,x_3,x_4]\), let \(E\) be an LND with
an original polynomial slice, and let \(T_1,T_2\) be two independent
constant partials satisfying
\[
[E,[E,T_i]]=0,\qquad W_i=[E,T_i]\quad(i=1,2).
\tag{1}
\]
Assume that
\[
f\in\ker E\cap\ker W_1\cap\ker W_2\setminus\mathbb C
\tag{2}
\]
and that some nonzero constant linear combination
\[
S_0=c_1T_1+c_2T_2
\quad\text{satisfies}\quad S_0f=0.
\tag{3}
\]

**Theorem.** Under (1)--(3), \(E\) fixes an actual ambient
coordinate and \(\ker E\simeq\mathbb C^{[3]}\).

There is no hypothesis on the adjoint heights of the other two
coordinate partials. The polynomial \(f\) need not be a highest-flow
coefficient, a primitive parameter, or an ambient coordinate.

## 2. The good tops and the parallel case

Each \(W_i\) is an LND: the actual Laurent conjugation
\(\varepsilon\exp(\operatorname{ad}_{E/\varepsilon})T_i
=\varepsilon T_i+W_i\) restricts to the polynomial parameter ring
and specializes at zero. The conjugated good partials commute, so
\([W_1,W_2]=0\). They also commute with \(E\) by (1).

Write \(W_0=[E,S_0]\). Suppose first that \(W_0\) is
fraction-field parallel to \(E\), including \(W_0=0\).
Then \(S_0\) preserves \(\ker E\): if \(Ea=0\), then
\(E(S_0a)=W_0a=0\).
The translations \(\Phi_t=\exp(tS_0)\) consequently preserve
\((\ker E)[t]\) setwise.

The original slice makes \(E\) primitive. The fields \(E\) and
\(\Phi_tE\Phi_t^{-1}\) have the same kernel and are rationally
proportional. Both are primitive over \(B[t]\). Reducing their
rational ratio in this UFD makes its numerator and denominator
units. The ratio is therefore a complex constant and equals one
at \(t=0\). Hence
\[
[E,S_0]=0.
\tag{4}
\]
This includes a rational proportionality coefficient; no polynomial
coefficient was silently assumed.

Take an independent complementary good direction \(S_1\).
The actual commuting partial \(S_0\), the good partial \(S_1\),
and the original slice satisfy the
[one-good-output-partial lemma](three-output-cubic-closure-pass41.md#1-a-recognition-lemma-requiring-only-one-good-partial)
with its rational coefficient \(F=0\) and denominator \(g=1\).
That proved lemma supplies an invariant ambient coordinate. No
slice is transferred to an auxiliary derivation.

## 3. Rank three and rank two

By (2), the joint rank of \(E,W_1,W_2\) is at most three.
If it is three, these are independent commuting LNDs with common
invariant \(f\) omitted by the actual direction \(S_0\).
The [omitted-coordinate commuting criterion](commuting-coordinate-descent-pass43.md)
supplies an invariant ambient coordinate.

It remains to handle joint rank two with \(E,W_0\) independent.
Set
\[
C=\ker E\cap\ker W_0.
\tag{5}
\]
The original slice and nonzero induced intrinsic action give
\(\operatorname{trdeg}\operatorname{Frac}C=2\).
Every \(W_i\) lies in the span of \(E,W_0\), and therefore
annihilates \(C\).

The first coefficient of the commuting conjugates of \(S_0,T_i\)
is
\[
[S_0,W_i]+[W_0,T_i]=0.
\tag{6}
\]
Apply it to \(f\). Equations (2)--(3) imply
\(W_0(T_if)=0\), while \(E(T_if)=W_if=0\). Thus
\[
F=\mathbb C[f,T_1f,T_2f]\subset C,\qquad S_0F=0.
\tag{7}
\]
Its transcendence degree is one or two.

## 4. The two gradient-field alternatives

If \(\operatorname{trdeg}F=1\), polynomial curve factorization
gives \(f=P(v)\), \(T_if=P_i(v)\), and
\(B\cap\mathbb C(v)=\mathbb C[v]\), with \(v\in B\) nonconstant.
The actual partial derivatives
\(T_iv=P_i(v)/P'(v)\) belong to \(\mathbb C[v]\).
Their restrictions are LNDs, so \(T_iv\in\mathbb C\).
Also \(S_0v=Ev=0\).

In actual coordinates \(S_0=\partial_a,S_1=\partial_b\),
write \(S_1v=\kappa\). If \(\kappa\ne0\), then
\(v=\kappa b+H(x_3,x_4)\) is an actual triangular coordinate.
If \(\kappa=0\), \(v\) belongs to the actual complementary
two-variable ring. Its nonconstant \(E\)-invariance invokes the
established binary-invariant theorem to obtain an invariant coordinate
of that plane.[^binary] Plane preservation by \(E\) is not required.

If \(\operatorname{trdeg}F=2\), algebraicity gives \(S_0C=0\).
Write
\[
B=R_0[a],\quad R_0=\mathbb C[b,x_3,x_4],
\quad S_0=\partial_a,\quad S_1=\partial_b,\quad C\subset R_0.
\tag{8}
\]
For \(c\in C\), rank two gives \(E(S_1c)=0\), and
\(S_0(S_1c)=0\). Hence
\(W_0(S_1c)=[E,S_0](S_1c)=0\), proving
\[
S_1(C)\subset C.
\tag{9}
\]
The actual three-ring extraction and primitive conjugation proof in
[Sections 5--6 of the dependent zero-motion note](rotating-zero-motion-closure-pass45.md#5-extraction-on-the-actual-three-ring)
now applies with \(W_0\) in place of \(D\). Its hypotheses are
exactly (5), (8), (9), independence of \(E,W_0\), and
\(W_0=[E,S_0]\).

Explicitly, the horizontal part of \(E\) is nonzero, since otherwise
the commutator would be parallel to \(E\). Highest weight in \(a\)
extracts a nonzero LND \(L\) on \(R_0\); a vertical leading term
divisible by \(a\) is forbidden. The exact kernel is \(C\).
Primitive division and the kernel-preserving translations of \(b\)
give \([L_0,\partial_b]=0\). The actual plane restriction of \(L_0\)
is either zero or has a coordinate invariant. In both cases \(C\)
contains an actual ambient coordinate killed by \(E\).

The original kernel is regular by its slice. The fixed-coordinate
regular-kernel theorem then proves the stated polynomiality.[^regular]

## 5. Application and the narrower remaining motion problem

The highest parameters \(g\) in the independent branch and \(u\)
in the dependent branch are killed by \(E,W_1,W_2\), by their
actual highest-column identities. Therefore either branch is recognized
whenever some nonzero constant good direction kills that parameter.
That direction need not be the canonical \(T_c\).

For a parameter \(f\), the new test is the failure of complex-linear
independence of its two good derivatives:
\[
\exists(c_1,c_2)\in\mathbb C^2\setminus\{0\}:
c_1T_1f+c_2T_2f=0.
\tag{10}
\]
After this gate, a remaining moving case must have two complex-linearly
independent good derivatives. This is constant-linear independence,
not algebraic independence. It is not asserted to be impossible.

All mechanisms are supplied by the written proof and previously
audited source gates. No new finite test count is added merely for
reusing the same gradient, primitive and plane mechanisms.
No universal frame, full supplied profile, historical novelty,
human review, formal proof or unrestricted cancellation is claimed.

[^binary]: S. Kuroda, [*Initial forms of stable invariants for additive group actions*](https://arxiv.org/pdf/1304.0313v2), Proposition 3.2, PDF p. 8, recording the characteristic-zero theorem credited to Daigle--Freudenburg. Polynomial curve factorization is M. de Bondt, [Corollary 3.2 and Lemma 3.3](https://arxiv.org/pdf/1501.06046v4), PDF pp. 20--21.

[^regular]: S. M. Bhatwadekar, N. Gupta and S. A. Lokhande, [*Some K-theoretic properties of the kernel of a locally nilpotent derivation on k[X1,...,X4]*](https://arxiv.org/pdf/1501.01438v1), Theorem 3.5. The rank-three and commuting-partial branches retain the complete source obligations of their linked proofs.
