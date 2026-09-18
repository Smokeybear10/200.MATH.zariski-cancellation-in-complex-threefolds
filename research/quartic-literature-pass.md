# Quartic stable coordinates and the first Vénéreau polynomial

The proposed nonconstant-axis target below is subsequently proved in
[the repeated-crossing note](repeated-crossing-pass.md), for all positive
multiplicities and arbitrary remainder degree. The
[original-slice variant](repeated-crossing-slice-descent.md) is also closed
for the constant-axis branch using the published residual-plane theorem.
Neither statement resolves the general Vénéreau embedding question.

The first Vénéreau polynomial is an exact degree-four boundary for the
working cubic theorem. The primary sources inspected prove its one-variable
stability and record its coordinate status as unresolved in the 2022
publication. This bounded search found no later resolution through
12 September 2026. It does **not** establish that no later resolution exists.

## Polynomial and degree audit

The conventions in the original papers identify

\[
 b_m=v_m=v_{z^2,m}
 =y+x^m\bigl(xz+y(yu+z^2)\bigr)
 =y+x^{m+1}z+x^my^2u+x^myz^2.
\]

Directly counting total degrees gives \(\deg b_m=m+3\) for \(m\ge1\).
In particular,

\[
 b_1=xy^2u+H(x,y,z),\qquad
 H=y+x^2z+xyz^2,\qquad \deg b_1=4,
\]

whereas \(b_2\) has degree five. Thus the theorem that the second Vénéreau
polynomial is a coordinate does not settle the quartic first polynomial.
Here degree is total degree in all four original variables, not degree in
the distinguished variable or in a bundle transition function.

[Lewis, *Vénéreau-type polynomials as potential counterexamples*](https://arxiv.org/pdf/1007.2230),
Introduction and Theorem 5, uses \(b_m\).
[Kaliman and Zaidenberg, *Vénéreau polynomials and related fiber bundles*](https://arxiv.org/abs/math/0308191)
uses \(v_m\) and states that every fiber of each \(v_m\) is isomorphic to
\(\mathbb A^3\). That fiber statement is an established property of this
particular family. It must not be inferred for arbitrary stable coordinates.

## Published constructions and their boundary

[Blanc and Poloni, *Bivariables and Vénéreau polynomials*](https://afst.centre-mersenne.org/item/10.5802/afst.1724.pdf),
Introduction, Lemma 2.1, Proposition 2.3 and Example 4.10, supplies the following
facts and constructions. The paper appeared in 2022; its
[arXiv version](https://arxiv.org/abs/2004.10739) is from 2020.

For \(n\ge1\), set

\[
 v_{P,n}=y+x^n(xz+y(yu+P(z))),\qquad q=yu+P(z).
\]

The localized automorphism is

\[
 \varphi(x,y,z,u)=
 \left(x,v_{P,n},xz+yq,
 \frac ux-\frac{P(z+yq/x)-P(z)}{xy}\right).
\]

It is defined over \(k[x,x^{-1}]\). Let \(F=\varphi^*\), extended to fix
\(t\), and let \(T_\xi(y)=y+\xi\), fixing the other variables. Then

\[
 \Phi_\xi=F\circ T_\xi\circ F^{-1},\qquad
 \Phi_\xi(v_{P,n})=v_{P,n}+\xi.
\]

For sufficiently large \(s\), \(\Phi_{x^st}\) is polynomial, and
\(v_{P,n}+x^st\) is a \(k[x,z,u]\)-coordinate. This proves one-variable
stable coordinate status. The proof gives a construction with sufficiently
large \(s\), not a stated minimal exponent.

The introduction explicitly leaves \(v_{z^2,1}\) unresolved even as an
absolute \(k\)-coordinate. The first polynomial's bundle has transition

\[
 f_1(T)=\frac{T}{ab^2}-\frac{T^2}{a^3b}
       -\frac{T^3}{a^2b^2}-\frac{T^4}{ab^3}.
\]

Over \(\mathbb C\), an isomorphic bundle has transition

\[
 g(T)=\frac{T}{ab^2}-\frac{T^2}{a^3b}
                 +\frac{T^3}{\sqrt5\,a^2b^2}.
\]

This is a degree-three transition function, not a reduction of the original
polynomial's total degree. No global coordinate completion for \(b_1\) was
located.

Lewis's Theorem 5 gives an explicit comparison construction. Put

\[
 p=yu+z^2,\quad v=xz+yp,\quad w=x^2u-2xzp-yp^2,
 \qquad
 \psi=\left(y,\frac vx,\frac w{x^2}\right).
\]

With composition interpreted as polynomial maps, define

\[
 \phi_m=\psi^{-1}\circ
 \left(y,z-\tfrac12x^{m+1}u,u\right)\circ
 \left(y+x^{m+1}z,z,u\right)\circ\psi.
\]

For \(m\ge2\) this is a polynomial automorphism over \(\mathbb C[x]\)
whose first component is \(b_m\). Its inverse is the reverse composition
with the two shear signs reversed. Theorem 6 also proves that \(b_1\)
cannot be completed within the specific subgroup intersection

\[
 \mathrm{GA}_3(\mathbb C[x])\cap
 \widetilde\psi^{-1}\mathrm{GA}_3(\mathbb C[x])\widetilde\psi,
 \qquad \widetilde\psi=(y,v,w).
\]

This excludes that construction strategy, not every polynomial automorphism.
[Lewis, Theorems 5 and 6, equations (7), (8), (11), (12)](https://arxiv.org/pdf/1007.2230).

## Exact boundary of a recent linear-hypersurface theorem

[Ghosh, Gupta and Pal, *On embedding of linear hypersurfaces*](https://arxiv.org/pdf/2405.07205),
Theorem 4.11, treats

\[
 G=\alpha(X_1,\ldots,X_m)Y-f(Z,T)-h(X_1,\ldots,X_m,Z,T),
\]

with \(\operatorname{char}k=0\), \(\alpha\notin k\), \(f\ne0\),
\(A=k[X_1,\ldots,X_m,Y,Z,T]/(G)\) a domain, and every prime factor
of \(\alpha\) dividing \(h\). Write \(\alpha=\prod p_i^{s_i}\).
The extra hypothesis is either a simple factor \(s_i=1\), or all
\(s_i>1\) and at least one of:

- \(p_j^2\mid h\) for some \(j\);
- \((p_j,\partial_{X_1}p_j,\ldots,\partial_{X_m}p_j)\) is proper;
- there are at least two distinct prime factors and \((p_l,p_j)\) is proper
  for some \(l\ne j\).

Under these hypotheses, stable polynomiality of \(A\), polynomiality of
\(A\), coordinate status of \(G\), relative coordinate status of \(G\)
together with all \(X_i\), and coordinate status of \(f\) are equivalent.

The dimension accounting is essential. Four ambient variables means
\(m=1\), hence \(\alpha\) is univariate. Choosing \(m=2\) to allow
\(\alpha=xy^2\) introduces five ambient variables. The arbitrary
four-variable expression \(xy^2u+H(x,y,z)\) therefore does not fall under
this theorem. A factor of multiplicity one alone is insufficient to invoke it.

A later primary publication surfaced:
[Ghosh, Gupta and Pal, *On the family of affine threefolds \(a(x)y=F(x,z,t)\)*](https://www.sciencedirect.com/science/article/abs/pii/S0021869326001948),
*Journal of Algebra* **700** (2026), 267–288. Its primary search-indexed
introduction concerns a univariate coefficient \(a(x)\). The full text was
not successfully retrieved in this pass, so no uninspected theorem from it
is being asserted here. It is a follow-up source to inspect, not evidence
for descent with coefficient \(xy^2\).

## Consequences for the next bounded target

The natural coefficient problem is

\[
 F=xy^2u+H(x,y,z),\quad\deg H\le4,\quad F\text{ stable}
 \quad\Longrightarrow\quad F\text{ coordinate}.
\]

Any proof of that complete statement would settle the first Vénéreau
polynomial. This logical implication follows from the displayed formula
and published stability, independently of its current literature status.
It is a substantial target, not a routine multiplicity variant of the
working \(xy\) theorem.

For a genuinely smaller next target, separate the branch where
\(H(0,0,z)\) is nonconstant from the constant branch. The Vénéreau example
lies in the latter because \(H(0,0,z)=0\). A precise candidate is descent
for \(xy^2u+H\) with \(\deg H\le4\) and \(H(0,0,z)\) nonconstant.
This is a proposed research subproblem; no theorem covering it was verified
in the sources inspected. The repeated component demands control beyond
the reduced support \(V(xy)\), so the existing reduced-crossing proof cannot
simply be relabeled.

For this candidate, retain only what stability supplies:
\(V(F-\lambda)\times\mathbb A^N\simeq\mathbb A^{N+3}\), smoothness,
contractibility and the resulting compact-support cohomology. An argument
requiring \(V(F-\lambda)\simeq\mathbb A^3\) must establish that conclusion
separately or restrict the theorem's hypothesis.

## Search coverage and present-status wording

Queries included the exact phrases “first Vénéreau polynomial,” “first
Venereau polynomial,” “Vénéreau polynomials,” and “quartic stable coordinate,”
the aliases \(b_1\) and \(v_1\), and year-filtered searches covering
2023–2026. Primary texts inspected were Blanc–Poloni, Lewis,
Kaliman–Zaidenberg's arXiv record, and Ghosh–Gupta–Pal's 2024 preprint.
Search results containing unrelated uses of “coordinate” were discarded.
No AI-generated repository or anonymous claimed solution was used.

The safe report is: **known one-stable quartic; reported open in the 2022
paper; no later coordinate proof located by this bounded pass.** This is
not a comprehensive current-status certification, a novelty claim for the
proposed coefficient subproblem, or a complete audit of every citation,
thesis, seminar announcement and language.
