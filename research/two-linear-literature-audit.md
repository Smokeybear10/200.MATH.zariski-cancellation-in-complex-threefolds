# The two-linear case is already known

The proposed implication for an original LND slice
\[
F=A(x,y)u+B(x,y)z+C(x,y)
\]
is covered by a published theorem. In fact, stability suffices. This is
the known \(n=q=1\) endpoint of the two-pure-power family, not a new
consequence requiring our proposed fibration proof.

## 1. The exact primary theorem

[Kaliman, Vénéreau and Zaidenberg, *Simple birational extensions of the
polynomial ring* \(\mathbb C^{[3]}\)](https://arxiv.org/pdf/math/0104204),
Theorem 3.24, printed pp. 37–38, treats
\[
p=d(au+bv)+c,\qquad a,b,c,d\in\mathbb C[x,y],
\quad d\ne0,\quad(a,b)\ne(0,0),\quad\gcd(a,b)=1.
\]
After a suitable base-plane automorphism, these are equivalent:

1. \(V(p)\) is irreducible, smooth and integrally acyclic.
2. \(V(p)\cong\mathbb A^3\).
3. \(p\) is a residual \(x\)-variable.
4. \(p\) is a coordinate over \(\mathbb C[x]\).
5. \(d\in\mathbb C[x]\), \(\gcd(c,d)=1\),
   \(V(a)\cap V(b)\subseteq V(d)\), and
   \(c(\alpha,y)\in\mathbb C^*y+\mathbb C\) for every root \(\alpha\) of \(d\).

This is **Theorem** 3.24, not a corollary. Its proof obtains the smooth
nonhorizontal-divisor condition from the two-linear form, applies
Theorem 3.21, and establishes the coefficient criterion by specialization
and a Bézout matrix. Coordinatehood is completed by Lemma 4.14 and
Theorem 4.2(b), printed pp. 42–43. Thus coordinate descent is part of
the published result, not an inference from abstract fibers alone.

## 2. Application to stability and an original slice

Suppose \((A,B)\ne(0,0)\). Take \(d=\gcd(A,B)\),
\(a=A/d\), \(b=B/d\), and \(c=C\). This exactly matches the
displayed hypotheses, including cases where one coefficient vanishes.

If \(F\) becomes a coordinate after adjoining \(m\) variables, then
\[
\bigl(\mathbb C[x,y,u,z]/(F)\bigr)^{[m]}
\cong\mathbb C^{[m+3]}.
\]
Consequently \(X=V(F)\) is irreducible and smooth, and
\(X\times\mathbb C^m\) is contractible. Projection onto \(X\) is a
homotopy equivalence, so \(X\) is integrally acyclic. The first
condition of Theorem 3.24 applies directly and proves that \(F\) is
a coordinate.

For an original LND \(D\) with \(D(F)=1\), write
\(S=\ker D\). The slice decomposition is
\(\mathbb C^{[4]}=S[F]\). In \(S[F,T]\), swapping the two
polynomial variables \(F,T\) shows that \(F\) is stable. Thus the
same application is valid without first identifying \(S\) or the
zero fiber with a polynomial threefold. Once \(F\) is a coordinate,
\(S\cong\mathbb C^{[4]}/(F)\cong\mathbb C^{[3]}\).

If \(A=B=0\), the theorem's displayed presentation is outside its
stated hypotheses. The stable case then reduces separately to a plane
polynomial: its zero curve is smooth, irreducible and acyclic, hence
\(\mathbb A^1\), and plane-line rectification makes \(C(x,y)\) a
coordinate. This edge case is not needed for the nonzero-coefficient
two-pure-power statement.

Therefore the all-linear endpoint can be combined with the separately
audited positive-power branches to state stable-to-coordinate for
\(A(x,y)u^n+B(x,y)z^q+C(x,y)\), \(A,B\ne0\), all
\(n,q\ge1\). This audit verifies the published endpoint only; the
other branches retain the proof status recorded in
[the double-binomial note](double-binomial-pass.md).

## 3. The separate affine-plane-over-a-PID route

The exact local and global statements were checked in the original
research article [Derksen, van den Essen and van Rossum, *An Extension
of the Miyanishi-Sugie Cancellation Theorem to Dedekind
Rings*](https://www.researchgate.net/publication/2829804_An_Extension_Of_The_Miyanishi-Sugie_Cancellation_Theorem_To_Dedekind_Rings),
author-uploaded full text, Theorems 1.2 and 1.3, pp. 2–3:

- Sathaye: for a DVR \(R\supseteq\mathbb Q\), fraction field \(K\),
  residue field \(k\), and finitely generated \(R\)-domain \(E\),
  \(E\otimes_RK\cong K^{[2]}\) and
  \(E\otimes_Rk\cong k^{[2]}\) imply \(E\cong R^{[2]}\).
- Bass–Connell–Wright: a finitely presented \(R\)-algebra which is
  polynomial after localization at every maximal ideal is
  \(\operatorname{Sym}_R(P)\) for a finite projective \(R\)-module.

Neither statement assumes that the total algebra is already a
polynomial ring over \(\mathbb C\), or supplies a section as an
additional hypothesis. Over \(R=\mathbb C[t]\), the projective module
is free. The article itself uses these results to prove relative
stable cancellation over a Dedekind ring. Its stability hypothesis is
an \(R\)-algebra isomorphism, not merely a \(\mathbb C\)-algebra one.

For an independently established fibration argument, the necessary
checks are precise. Set \(E=\mathbb C[X]\) and \(R=\mathbb C[t]\).
One needs \(R\hookrightarrow E\), finite generation, a domain,
\[
E\otimes_R\mathbb C(t)\cong\mathbb C(t)^{[2]},\qquad
E/(t-\alpha)E\cong\mathbb C^{[2]}\quad\text{for every }\alpha.
\]
The displayed special fibers are scheme fibers, not only reduced
supports. The generic isomorphism is over \(\mathbb C(t)\), not
only over its algebraic closure. A domain containing \(R\) is
torsion-free and hence flat over this PID. It is finitely presented
because \(R\) is Noetherian. Applying the DVR theorem to each
\(R_{(t-\alpha)}\), followed by the local-to-global theorem,
then gives \(E\cong R^{[2]}\).

Under the coefficient conditions in Section 1, these fiber checks
can also be made explicitly. Away from roots of \(d\), the specialized
pair \((a,b)\) is unimodular over \(\mathbb C[y]\); a determinant-one
Bézout change of \((u,v)\) eliminates one variable from \(p=\lambda\).
At a root of \(d\), the equation becomes a nonconstant affine-linear
equation in \(y\), leaving \(u,v\) free. Over \(\mathbb C(x)\),
\(d\) is invertible and the same Bézout calculation works. This gives
the claimed abstract affine-plane fibration. By itself this route
does not identify \(p\) as an ambient coordinate. For the two-linear
form that last step is already supplied by Theorem 3.24.

## 4. Source-check boundary

The full statement and relevant proof chain of KVZ Theorem 3.24 were
read directly. The two fibration statements were checked as explicitly
reproduced and used in the Derksen–van den Essen–van Rossum research
paper. The original [Sathaye article](https://doi.org/10.1007/BF01388536)
and [Bass–Connell–Wright article](https://doi.org/10.1007/BF01403135)
were bibliographically located, but their original full proofs were
not obtained in this bounded pass. Thus this is not a new audit of
those proofs. No further literature search is needed to identify the
all-linear case as known.
