# Independent audit of the nodal embedding tests

Date: 2026-09-13.

Scope: the complete [nodal embedding note](nodal-embedding-pass21.md),
with the complete [pass-20 conductor construction](nodal-conductor-pass20.md)
reread for its inherited hypotheses. No mathematical defect was found in
the module, Picard, Milnor-square, or cotangent-class deductions. In
particular, the note makes no unsupported inference from a vanishing
stable obstruction to an embedding in affine three-space.

This is an independent written audit, not expert review, proof-assistant
verification, or a priority assessment.

## 1. The exact square and preliminary calculations

The square is genuinely a Milnor square: the map
\(B\to D_0=B/dB\) is surjective, and the ideal \(I=dB\)
of \(R=B\times_{D_0}C_0\) maps isomorphically onto that same ideal
of \(B\). Thus the cited sequences apply even though \(R\) is
singular. Neither normality of \(R\) nor higher algebraic
\(K\)-theory excision is required.

The distinct values of \(w\) on each paired pair of lines make the
two-by-two residue interpolation invertible over \(\mathbb C[t]\).
It proves \(B=R+Rw\), hence \(I=(d,dw)R\). The same residue
calculation gives \(\operatorname{Ann}_R(w\bmod R)=I\), which
justifies the stated module exact sequence. These are not assertions
about the number of algebra generators of \(R\).

The divisor calculation for \(B\) also checks: localizing at
\(A=(w-w_1)(w-w_3)\) leaves a factorial ring, and its units give
exactly the two displayed relations among the four removed prime
divisors. Smoothness of \(B\) then gives
\(B^*=\mathbb C^*\) and \(\operatorname{Pic}(B)=\mathbb Z^2\).
The resulting Units–Pic sequence yields the claimed abstract group
extension for \(\operatorname{Pic}(R)\), with a noncanonical splitting.
The source is Weibel's [Chapter I, Theorem 3.10 and proof](https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.I.pdf),
printed pp. 22–23. Its hypotheses match this square exactly.

## 2. Independent reconstruction of the \(SK_0\) argument

The normalization \(B\) is a regular affine surface. Weibel's
[Chapter II, Theorem 8.2 and Example 8.2.2](https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.II.pdf),
printed pp. 76–77, identify \(K_0(B)\) with \(G_0(B)\) and
generate \(SK_0(B)\) by closed-point classes. Each point lies on a
closed reduced affine-line component of a \(w\)-fiber. The multiplication
sequence on that line has zero point class, and closed-immersion
pushforward is exact for coherent modules. It follows that
\(SK_0(B)=0\). This reasoning does not identify \(K_0(R)\)
with \(G_0(R)\).

For completeness, take \(v\in SK_0(R)\). Its pullback to \(B\)
has rank zero and trivial determinant, so it is zero. Its pullback to
\(C_0=\mathbb C[t]^3\) is also zero: \(R\) is connected, its
rank is zero, and \(K_0(C_0)=\mathbb Z^3\). The Milnor sequence
therefore gives
\[
v=\partial u,\qquad u\in K_1(D_0).
\]
Since every factor of \(D_0=\mathbb C[t]^6\) is Euclidean,
\(K_1(D_0)=D_0^*\). For a scalar unit \(u\), patching gives
\(\partial u=[L_u]-[R]\), up to the single consistent boundary
sign. Consequently a trivial determinant of \(v\) means that
\(L_u\) is trivial. Units–Pic exactness puts \(u\) in the image
of \(B^*\times C_0^*\), already an image in the preceding
\(K_1\) map, so \(v=0\).

This is exactly the projective-module sequence and boundary construction
in Weibel's [Chapter III, Theorem 2.6 and full proof](https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.III.pdf),
printed p. 15. Example 1.3.5, printed p. 4, supplies the Euclidean
\(K_1\) calculation. No premise \(SK_1(B)=0\) is needed.
Free modules and \([L]-[R]\) give surjectivity of rank and determinant.
Thus the asserted abelian-group isomorphism
\[
K_0(R)\cong\mathbb Z\oplus\operatorname{Pic}(R)
\]
is justified.

## 3. Cotangent complex: what the equality actually says

The argument retains two specific predecessor hypotheses: \(R\) is
a local complete intersection over \(\mathbb C\), and the particular
scaled gluing has \(\omega_R\cong R\). The latter uses the
opposite-residue construction, not merely the local nodal equation.

The statement and full proof of [Stacks Proposition 92.14.4, tag 08SL](https://stacks.math.columbia.edu/tag/08SL)
give, for a finite polynomial presentation with kernel \(J\),
\[
L_{R/\mathbb C}\simeq[J/J^2\longrightarrow R^N],
\]
where the conormal module is finite projective. The referenced
[Stacks Lemma 15.33.3, tag 08RK](https://stacks.math.columbia.edu/tag/08RK)
also explicitly states that projectivity assertion. Since \(R\)
is an integral surface, the conormal rank is \(N-2\).

Locally, the Koszul resolution gives
\[
\omega_R=\det(R^N)\otimes\det(J/J^2)^{-1}
           =\det L_{R/\mathbb C}.
\]
The change-of-regular-sequence transition factors on both sides agree,
so this is a global line-bundle identification, not only a local
triviality assertion. The complex has rank two and trivial determinant.
The established injectivity of rank and determinant therefore proves
\([L_{R/\mathbb C}]=2[R]\) in \(K_0(R)\).

Nothing in that proof makes \(J/J^2\) free of rank one, makes the
complex isomorphic to \([R\to R^3]\), or supplies three algebra
generators. The note explicitly excludes all of these inferences.
Its final criterion, existence of a surjection
\(\mathbb C[X,Y,Z]\twoheadrightarrow R\), is correct: a
height-one prime in that factorial source is principal. The present
calculation neither constructs nor excludes such a surjection, and
does not establish the stronger ambient locally nilpotent derivation
compatibility required by the research program.
