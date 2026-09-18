# Closest published statements for the double-binomial theorem

This is a bounded statement-level check of
[double-binomial-pass.md](double-binomial-pass.md), specifically

\[
F=A(x,y)u^n+B(x,y)z^q+C(x,y),\qquad A,B\ne0,\quad n,q\ge2,
\]

and the claimed equivalence between stability and base coordinates
\((a,b)\) satisfying \(C=b\), \(A=r(a)\), \(B=p(a)\).
The checked primary papers give the following five close statements.
None is being represented as the exact double-binomial classification.
Failure to locate that classification in this bounded pass is not
evidence of novelty or of its absence from the literature.

Here \(R^{[m]}\) denotes a polynomial algebra in \(m\) variables
over \(R\). All displayed relative ring identifications are
identifications as \(R\)-algebras.

## 1. Kaliman–Zaidenberg: one pure power and an integral-acyclic surface

[Kaliman and Zaidenberg, *Affine modifications and affine
hypersurfaces with a very transitive automorphism group*, Theorem
7.2](https://arxiv.org/pdf/math/9801076), considers a smooth
irreducible surface
\(X=\{f(x,y)v^d+g(x,y)=0\}\subset\mathbb A^3\).
It makes the following equivalent: \(\chi(X)=1\) and
\(H_1(X;\mathbb Z)=0\); integral acyclicity; \(X\simeq\mathbb A^2\);
and rectifiability. When \(d>1\), these are also equivalent to
base rectification \((f,g)\mapsto(p(a),b)\).

This is the closest published simultaneous-pair statement. It has
one pure-power variable and requires integral homology for a single
fiber. Smith theory in the double-binomial proof initially gives
only mod-prime and rational acyclicity of the fixed surface.
The general-level transversality deduction in
[generic-rational-binomial-pass.md](generic-rational-binomial-pass.md)
is therefore a real intervening argument, not a direct application
of Theorem 7.2 with unchanged hypotheses.

## 2. Das–Dutta: Wright's theorem over arbitrary fields

[Das and Dutta, *Planes of the form b(X,Y)Z^n-a(X,Y) over a DVR*,
Theorem 4.5](https://arxiv.org/pdf/2002.02118), proves: if
\(k\) is a field, \(d\ge2\), \(\operatorname{char}k\nmid d\),
\(f,h\in k[X,Y]\), \(f\ne0\), and

\[
k[X,Y,V]/(fV^d-h)\simeq k^{[2]},
\]

then some \(a\in k[X,Y]\) satisfies

\[
k[X,Y]=k[a,h],\qquad f\in k[a],\qquad
k[X,Y,V]=k[a,fV^d-h,V].
\]

The premise is an actual affine-plane quotient, not a rational
homology plane or a stably polynomial threefold. Applying this over
\(\mathbb C(x)\) would first require the corresponding
\(\mathbb C(x)^{[2]}\) quotient.

## 3. Das–Dutta: the relative quotient theorem

The same paper's Theorem 6.2, restricted here to its
characteristic-zero case, says that for a Noetherian domain
\(R\supset\mathbb Q\), \(d\ge2\), \(f,h\in R[X,Y]\),
\(f\ne0\),

\[
R[X,Y,V]/(fV^d-h)\simeq R^{[2]}
\quad\Longrightarrow\quad
R[X,Y,V]=R[fV^d-h,V]^{[1]},\quad R[X,Y]=R[h]^{[1]}.
\]

Taking \(R=\mathbb C[x]\) is legitimate only after proving that
relative polynomial-quotient premise. An abstract
\(\mathbb C^{[3]}\) quotient is not the premise. Neither is
coordinatehood after adjoining unrelated extra variables. See
[Theorem 6.2](https://arxiv.org/pdf/2002.02118).

## 4. Kaliman–Vénéreau–Zaidenberg: residual variable implies variable

[Kaliman, Vénéreau and Zaidenberg, *Simple birational extensions
of the polynomial ring C[3]*, Theorem
4.27](https://arxiv.org/pdf/math/0104204), states that

\[
P=f(x,y,z)u^n+g(x,y,z),\quad n\ge2,
\qquad P\text{ residual }x\text{-variable}
\quad\Longrightarrow\quad P\text{ is an }x\text{-variable}.
\]

Their residual condition means that
\(P(\alpha,y,z,u)\) is a coordinate of \(\mathbb C[y,z,u]\)
for every \(\alpha\in\mathbb C\). Their conclusion preserves
the specified base \(\mathbb C[x]\).

Our \(F\) has the required syntactic pure-power form, with
\(g=Bz^q+C\), but syntax does not verify the residual condition.
The theorem is directly applicable once that condition is known.
It is not a theorem that stability supplies it. Nor does its
statement impose a common plane direction on \(A,B\) with
\(C\) as companion. The new compatibility step in the working
proof must therefore remain explicit.

## 5. Das: cancellation with an already relative pure-power variable

[Prosenjit Das, *On cancellation of variables of the form bT^n-a
over affine normal domains*, Theorem
3.4](https://arxiv.org/pdf/2002.02129), in characteristic zero,
states: for a Noetherian domain \(R\supset\mathbb Q\), an
\(R\)-algebra \(S\), \(a,b\in S\), and \(d\ge2\),

\[
S[T]=R[bT^d-a]^{[2]}=R^{[3]}
\quad\Longrightarrow\quad
S=R[a]^{[1]}=R^{[2]},\qquad
S[T]=R[bT^d-a,T]^{[1]}.
\]

This genuinely allows the coefficient algebra to be unknown and
then proves it polynomial. But the starting equality says the
pure-power polynomial is already a coordinate of a relative
three-variable algebra. The double-binomial problem starts in four
variables with only absolute stability. Choosing a base subring
that makes this hypothesis true cannot be assumed. Thus the title
does not supply unrestricted stable cancellation in four variables.

## Statement distinctions and bounded conclusion

The following must remain separate throughout the report:

- An abstract zero-fiber ring \(\mathbb C[x,y,u,z]/(F)\simeq
  \mathbb C^{[3]}\).
- A relative plane ring over an existing \(\mathbb C[x]\), or
  coordinatehood of every specialization at \(x=\alpha\).
- Absolute stable coordinatehood of \(F\), which makes all level
  hypersurfaces stably affine space but does not immediately make
  their unstabilized rings polynomial.
- Absolute coordinatehood and the stronger simultaneous base form
  \(C=b,A=r(a),B=p(a)\).

The double-binomial argument supplies its own route between these
different types of information: finite fixed surfaces, the
general-fiber binomial deduction, then the quotient/root
compatibility test. The references above do not eliminate those
steps merely by relabeling their hypotheses.

The search covered the exact two-pure-power and trinomial wording,
the Sathaye–Wright family, its field and relative extensions, and
the original KVZ theorem. Some arXiv uploads are later than their
original publications, so upload dates have not been treated as
dates of discovery. This note stops at the five verified statements
above. It does not assert either priority or a complete current
bibliography for the working classification.
