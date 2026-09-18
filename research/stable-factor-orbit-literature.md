# Intrinsic orbit rank of a one-stable polynomial factor

Let \(K\) be a complex affine domain of dimension three with
\[
K[s]\cong\mathbb C^{[4]},\qquad X=\operatorname{Spec}K.
\]
The strongest unconditional action-existence conclusion verified in this
bounded pass is still that \(K\) is nonrigid. No checked theorem forces
two generically independent intrinsic LNDs or a trivial Makar-Limanov
invariant from this hypothesis alone. This is a statement about the
coverage of this pass, not a claim that no stronger theorem exists.

There is, however, an exact reformulation of the remaining question:
\[
\begin{aligned}
&\text{two generically independent intrinsic LNDs}\\
&\quad\Longleftrightarrow\quad
\dim(\text{general }\operatorname{SAut}(X)\text{-orbit})\ge2\\
&\quad\Longleftrightarrow\quad
\operatorname{trdeg}_{\mathbb C}\operatorname{ML}(K)\le1\\
&\quad\Longleftrightarrow\quad K\text{ is not semi-rigid}.
\end{aligned}
\tag{1}
\]
The sources below justify this equivalence and show why cylinder
invariants alone cannot supply its missing premise.

## 1. One-cylinder rigidity: the unconditional lower bound

[Alhajjar, *LND-Filtrations and Semi-Rigid
Domains*](https://arxiv.org/pdf/1501.00445), Proposition 3.4, PDF p. 6,
states and proves the characteristic-zero one-cylinder rigidity result:
if \(A\) is rigid and has finite transcendence degree, then \(A[t]\)
is semi-rigid. The proof actually shows
\[
\operatorname{LND}(A[t])=A\partial_t,
\qquad \operatorname{ML}(A[t])=A.
\]
It attributes this result to Makar-Limanov and to
Crachiola–Makar-Limanov, Theorem 3.1. Propositions 3.2–3.3 also identify
semi-rigidity with a common kernel and describe all LNDs as replicas of
one irreducible LND under the stated ACC and HCF assumptions.

Here \(\operatorname{ML}(K[s])=\mathbb C\). If \(K\) were rigid,
the displayed equality would instead give \(\operatorname{ML}(K[s])=K\).
Thus
\[
\operatorname{LND}(K)\ne\{0\},\qquad
\mathbb C\subseteq\operatorname{ML}(K)\subsetneq K.
\tag{2}
\]
This argument uses exactly one added variable. It cannot be iterated
to rule out rigid factors with two or more added variables: after the
first extension, the intermediate ring is no longer rigid.

## 2. The stable-factor class and conditional kernel structure

[Daigle, *Locally nilpotent derivations and the structure of
rings*](https://arxiv.org/pdf/1806.10742), Lemma 3.5, proves
\[
\operatorname{FML}(K)=\operatorname{Frac}(\operatorname{ML}(K))
\tag{3}
\]
for a UFD. Proposition 5.3.4 puts every stably polynomial algebra in
his class \(\mathcal C_s\): geometrically smooth factorial affine
domains with only scalar units. This applies to arbitrary numbers of
stable variables but does not assert nonrigidity.

Write \(\mathcal A_i(K)\) for intersections of LND kernels having
codimension \(i\) in transcendence degree. Corollary 5.5(a),(b) gives
\[
R\in\mathcal A_2(K)\Longrightarrow R\cong\mathbb C^{[1]},
\quad R\subset A\in\mathcal A_1(K)
\Longrightarrow A=R^{[1]}.
\tag{4}
\]
Theorem 5.7 further makes \(K\otimes_R\operatorname{Frac}R\) a
special Danielewski surface
\(\operatorname{Frac}(R)[U,V,W]/(UV-\phi(W))\), with \(\phi\)
nonconstant. These are conditional statements: they do not produce
\(R\in\mathcal A_2(K)\). Proposition 5.8's stronger conclusion from
two commuting LNDs assumes a **field form** of affine three-space,
not a stably polynomial algebra. Replacing that premise is invalid.

For example, if the missing step established
\(\operatorname{trdeg}\operatorname{ML}(K)=1\), then (4) would
give \(\operatorname{ML}(K)=\mathbb C[h]\) and
\(\ker d=\mathbb C[h]^{[1]}\) for every nonzero intrinsic LND
\(d\). It would not by itself make \(h\) a coordinate of \(K\),
trivialize every fiber of \(h\), or identify \(K\) with a polynomial
ring. If \(\operatorname{trdeg}\operatorname{ML}(K)=2\), all
nonzero LNDs have the same kernel; the source leaves this semi-rigid
possibility available.

## 3. Orbit dimension and the distinction between ML and FML

[Arzhantsev, Flenner, Kaliman, Kutzschebauch and Zaidenberg, *Flexible
varieties and automorphism groups*](https://arxiv.org/pdf/1011.5375),
arXiv v2, Corollaries 1.14 and 1.21, identifies generic orbit
codimension with the transcendence degree of rational invariants and
the orbit tangent space with the span of LND vectors. Proposition 5.1
equates a trivial field Makar-Limanov invariant with an open
\(\operatorname{SAut}\)-orbit and the existence of a flexible point.

Combining these statements with (3) gives the exact identity
\[
r:=\dim_{\operatorname{Frac}K}
\operatorname{Span}_{\operatorname{Frac}K}\operatorname{LND}(K)
=3-\operatorname{trdeg}_{\mathbb C}\operatorname{ML}(K).
\tag{5}
\]
Together with (2), this leaves \(r\in\{1,2,3\}\). For \(r=1\),
all nonzero LNDs are proportional over the fraction field and have the
same kernel; conversely, equal kernels imply that proportionality.
This proves (1).

In particular,
\[
\operatorname{ML}(K)=\mathbb C
\quad\Longleftrightarrow\quad r=3
\quad\Longleftrightarrow\quad
\operatorname{SAut}(X)\text{ has a dense open orbit}.
\tag{6}
\]
An open orbit is not the assertion that every point lies in it.
More importantly, the LNDs spanning it need not commute. Thus (6) is
not the rank-three cancellation argument in the
[intrinsic-actions note](intrinsic-actions-pass.md), which constructs
an action of the algebraic vector group \(\mathbb G_a^3\) from three
commuting fields. An arbitrary collection of three independent LNDs
does not supply that vector-group action.

## 4. A single cylinder can have much larger orbit rank

[Dubouloz, *Flexible bundles over rigid affine
surfaces*](https://ems.press/content/serial-article-files/43375),
Theorem 1.1, constructs a smooth rigid affine surface
\(S=V\setminus D\), where \(V\) is a smooth projective cubic surface
and \(D\) is a hyperplane section consisting of a smooth conic and
its tangent line. It proves that \(S\times\mathbb A^2\) is flexible
in codimension one.

There are two distinct consequences. First, rigidity can disappear
after adding two variables. Second, set
\(Y=S\times\mathbb A^1_t\), now a smooth affine threefold. By
Section 1, every LND of \(\mathbb C[Y]\) is
\(a\partial_t\), \(a\in\mathbb C[S]\). Consequently
\[
r(Y)=1,\qquad
r(Y\times\mathbb A^1)=r(S\times\mathbb A^2)=4.
\tag{7}
\]
Thus even full generic flexibility of a **single** cylinder does not
force two independent intrinsic LNDs on its smooth threefold base.
This is not a counterexample with polynomial cylinder. It demonstrates
the exact failure of replacing polynomial-cylinder structure by orbit
rank alone.

## 5. The Russell-cylinder invariant warning

[Dubouloz, *The cylinder over the Koras–Russell cubic threefold has a
trivial Makar-Limanov invariant*](https://arxiv.org/pdf/0807.4085),
the main theorem, proves for
\[
R=\mathbb C[x,y,z,t]/(x+x^2y+z^2+t^3)
\]
that
\[
\operatorname{ML}(R)=\mathbb C[x],\qquad
\operatorname{ML}(R[w])=\mathbb C.
\tag{8}
\]
The first invariant computation is recalled in the paper; the second
is its result. This is a smooth contractible factorial threefold, much
closer to the cancellation setting than an arbitrary cylinder example.
It refutes the general inference
\(\operatorname{ML}(A[w])=\mathbb C\Rightarrow
\operatorname{ML}(A)=\mathbb C\), including for such threefolds.

It does **not** refute cancellation: the cited theorem does not identify
\(\operatorname{Spec}R\times\mathbb A^1\) with \(\mathbb A^4\).
It also does not refute rank at least two on the base. Indeed the
derivations
\[
\delta_z(x)=\delta_z(t)=0,\quad
\delta_z(z)=x^2,\quad\delta_z(y)=-2z,
\]
\[
\delta_t(x)=\delta_t(z)=0,\quad
\delta_t(t)=x^2,\quad\delta_t(y)=-3t^2
\]
are locally nilpotent and generically independent on \(R\). They
preserve the defining relation by direct substitution. Equation (8)
therefore illustrates rank two on the base, not a semi-rigid base.

## 6. Exact remaining step and coverage

The bounded search checked these five primary papers and their exact
relevant statements, including the proof of the one-cylinder
rigidity lemma. It did not locate a theorem excluding semi-rigidity
for every \(K\) with \(K[s]=\mathbb C^{[4]}\).

The next structural target is therefore precise: use the **polynomial**
cylinder, beyond its trivial invariants and generic orbit rank, to
show that two intrinsic LND kernels differ. That would establish (1),
but still not the stronger (6) or cancellation. A trivial ML invariant
would establish (6), but still needs a separate algebraic recognition
argument. No absence-of-search-result argument is used to declare any
of these statements novel or presently open.
