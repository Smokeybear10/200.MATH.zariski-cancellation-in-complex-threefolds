# Radical modification: a sharp obstruction to canonical rescaling

Private bounded pass 18. This note does **not** prove polynomiality for
arbitrary radical-congruence modifications. It proves an exact obstruction
to a specified patching method, explains why all finite plinth jets miss
the obstruction, and identifies what a repair would have to change.
The new arguments below are algebraic working proofs, not externally
reviewed or Lean-verified results. No novelty claim is made.

## 1. Setup and the method being tested

Let
\[
R=\mathbb C[x,y,z],\quad D\ne0\text{ primitive and locally nilpotent},
\quad C=\ker D,\quad P_D=pC,\quad Dr=p.
\]
Thus \(r\) is a minimal local slice. The facts
\(C\cong\mathbb C^{[2]}\) and principality of the plinth ideal are
the standard three-variable inputs.[^1] Put \(p_0=\operatorname{rad}(p)\),
meaning a squarefree generator, and assume
\[
0\ne V=1+p_0Q\in C,\qquad (p,V)C=C,
\qquad M=R[r/V].                                      \tag{1}
\]
The connected-support assumption motivates this form of \(V\), but
the obstruction proved here does not need connectedness.

The [two-way modification proof](arbitrary-invariant-kernel-pass18.md)
gives \(M^{[1]}\cong\mathbb C^{[4]}\), together with
\[
M_V=R_V,\qquad M_p=C_p[w],\qquad R_p=C_p[r],
\qquad w=r/V.                                         \tag{2}
\]
A tempting patch sends \(r\) to \(w\) on the \(p\)-chart while
fixing \(C\). On the overlap, it is the automorphism
\(r\mapsto r/V\) of \(C_{pV}[r]\). The question tested below is
whether **this particular overlap automorphism** extends over \(R_V\).
It is not the question whether some abstract isomorphism \(R\cong M\)
exists after changing the invariant-plane embedding.

## 2. Sharp rescaling criterion

**Proposition.** Let \(0\ne V\in C\) be comaximal with \(p\), and let
\(\lambda\in C_V^*\) satisfy \(\lambda-1\in p_0C_V\). Let
\(\sigma_\lambda\) be the \(C_{pV}\)-automorphism of
\(R_{pV}=C_{pV}[r]\) defined by \(r\mapsto\lambda r\). Then
the following are equivalent:

1. \(\sigma_\lambda(R_V)\subset R_V\).
2. \(\sigma_\lambda\) restricts to an automorphism of \(R_V\).
3. \(\lambda-1\in pC_V\).

In particular, the canonical rescaling in (2) extends over \(R_V\)
if and only if \(V-1\in pC\). The latter equivalence uses
\((p,V)=1\) to contract \(pC_V\) back to \(pC\).

### 2.1. Sufficiency

If \(\lambda-1=pH\), set \(T=Hr\in R_V\). For \(a\in R_V\),
the finite independent-time flow gives the polynomial expression
\[
\sigma_\lambda(a)=
\sum_{j\ge0}\frac{T^j}{j!}D^j(a).                     \tag{3}
\]
It fixes \(C_V\) and sends \(r\) to \(\lambda r\). The same
formula for \(\lambda^{-1}\), with
\((\lambda^{-1}-1)/p\in C_V\), gives its inverse. Thus (3) implies
(2), and (2) implies (1). This is the same finite-flow mechanism used
in [pass 15, Section 6](extension-mixing-pass15.md), not a new
assumption that the variable-time derivation itself is locally nilpotent.

### 2.2. Two valuation facts

Fix an irreducible factor \(f\) of \(p\), of multiplicity \(n\).
The element \(f\) remains irreducible in \(R\): any factorization
in \(R\) has invariant factors by factorial closure, contradicting
irreducibility in \(C\). Let \(v=v_f\) be the valuation of the DVR
\(O=R_{(f)}\). Because \((p,V)=1\), \(R_V\subset O\).

Minimality forces \(v(r)=0\). Otherwise \(r/f\in R\), and
\(D(r/f)=p/f\) would belong to \(P_D=pC\), an impossibility.
Primitivity supplies a coordinate \(a\in\{x,y,z\}\) such that
\(v(Da)=0\). Indeed, otherwise \(f\) would divide all three
coefficients of \(D\).

### 2.3. An integral-iterate argument

Assume (1), and suppose for contradiction that
\[
1\le k=v(\lambda-1)<n.
\]
Let \(\widehat O\) be the \(f\)-adic completion of \(O\), and
write \(\widehat K=\operatorname{Frac}(\widehat O)\). In this
complete characteristic-zero DVR the formal logarithm
\[
L=\log\lambda=\sum_{i\ge1}
\frac{(-1)^{i+1}}{i}(\lambda-1)^i
\]
converges and has valuation \(k\). This is a formal algebraic
device; no analytic convergence or polynomial logarithm is asserted.

Choose \(a\) as in Section 2.2, and let \(d\) be its \(D\)-degree.
In \(R_{pV}\), \(D=p\partial_r\). For every integer \(m\ge0\),
\[
\sigma_\lambda^m(a)=
\sum_{j=0}^{d}
\frac{r^jD^j(a)}{j!p^j}(\lambda^m-1)^j\in R_V\subset O.
                                                               \tag{4}
\]
All nonnegative iterates preserve \(R_V\) by assumption (1).
Introduce an independent formal parameter \(T\) and set
\[
H(T)=\sum_{j=0}^{d}
\frac{r^jD^j(a)}{j!p^j}
\bigl(\exp(TL)-1\bigr)^j\in\widehat K[[T]].            \tag{5}
\]
The coefficients have valuations bounded below by \(-nd\), and
their valuations tend to infinity with the degree in \(T\).
More precisely, the coefficient of \(T^\ell\) in each nonconstant
summand has valuation at least \(k\ell-nj\). Thus, for \(N=nd\),
\(f^NH(T)\) is a restricted series over \(\widehat O\), and its
reduction modulo \(f^N\) is a polynomial in \(T\).

For every integer \(m\ge0\), the formal identity
\(\exp(mL)=\lambda^m\) identifies \(H(m)\) with (4).
Consequently the polynomial \(f^NH(T)\bmod f^N\) vanishes at
every nonnegative integer. It is the zero polynomial: a Vandermonde
matrix evaluated at sufficiently many distinct integers has determinant
a nonzero integer, hence a unit even in the possibly nonreduced ring
\(\widehat O/(f^N)\).

In particular, its linear coefficient vanishes, so \(H'(0)\) lies
in \(\widehat O\). But differentiating (5) gives exactly
\[
H'(0)=\frac{rL}{p}Da,
\qquad v\bigl(H'(0)\bigr)=k-n<0,                     \tag{6}
\]
using the two valuation facts. This is the contradiction.
Therefore \(v_f(\lambda-1)\ge v_f(p)\) for every factor \(f\),
which gives (3) because \(C_V\) is a UFD. The case \(\lambda=1\)
is immediate. This completes the proof.

This proposition excludes a canonical rescaling lift already for
\(p=x^2\), \(V=1+x\). It does not exclude noncanonical relative
isomorphisms, and it does not exclude abstract polynomial coordinates.

## 3. Every finite plinth thickening is already identical

For every \(N\ge1\), the original inclusion \(R\hookrightarrow M\)
induces
\[
R/(p_0^N)\ \xrightarrow{\sim}\ M/(p_0^N).             \tag{7}
\]
Indeed, \(V=1+p_0Q\) is a unit in both quotients, and after
localizing at \(V\) the inclusion is an isomorphism by (2).
The inverse on each quotient uses the finite geometric series for
\(V^{-1}\). These maps are compatible in \(N\), giving an
isomorphism of \(p_0\)-adic completions as well.

Thus the existence of compatible corrections at every nilpotent
order cannot by itself prove that the displayed global inclusion is
an isomorphism. Here is an exact elementary control:
\[
D=x^2\partial_y+2y\partial_z,\quad
C=\mathbb C[x,h],\quad h=x^2z-y^2,\quad r=y,\quad p=x^2,
\]
\[
V=1+x,\qquad M=\mathbb C[x,w,z],\qquad y=(1+x)w.       \tag{8}
\]
For the stated kernel and plinth, localize at \(x\), use
\(R_x=\mathbb C[x,x^{-1},h,y]\), and contract: modulo \(x\),
\(h=-y^2\) makes \(\mathbb C[h]\to\mathbb C[y,z]\) injective,
which removes denominators for invariants. If \(Da=b(x,h)\) is
invariant, then in that chart \(a=b(x,h)y/x^2+c(x,h)\).
If \(v_x(b)<2\), the lowest negative power of \(x\) has an odd
nonzero polynomial in \(y\) from the first term, whereas the
invariant term contributes an even polynomial. They cannot cancel.
Thus \(b\) is divisible by \(x^2\), verifying the plinth claim.

The inclusion in (8) is not surjective: on \(x=-1\), its image has
\(y=0\) while \(w\) is still free. Yet it induces an isomorphism
on every \(x\)-adic thickening. Its Jacobian in the displayed
polynomial coordinates is \(1+x\), not a constant.

There is also a general intrinsic form of the last calculation.
The smooth hypersurface presentation \(M=R[w]/(Vw-r)\) has a
nowhere-vanishing residue volume form \(\omega_M\): on each chart
where one partial derivative of \(Vw-r\) is a unit, divide the
corresponding omitted-coordinate three-form by that derivative.
Differentiating the defining equation shows that these local generators
glue. With a choice
of sign it satisfies
\[
dx\wedge dy\wedge dz=V\omega_M.                       \tag{9}
\]
This follows on the \(V\)-chart from the defining equation and
then globally by equality of regular forms on a dense open set.
Smoothness follows directly from the two charts in (2). Hence the
canonical modification morphism carries a Jacobian factor \(V\),
although that factor is a unit in every formal plinth neighborhood.
For nonconstant \(V\), its zero divisor is exactly the location
that this formal comparison fails to control.

## 4. What determinant balancing does and does not supply

There is no universal obstruction to balancing a nilpotent jet once
two *free* coordinates are available. For example, for \(N\ge1\),
put \(T_N=\sum_{j=0}^{2N-1}(-x)^j\). Then
\[
\begin{pmatrix}1+x&x^N\\-x^N&T_N\end{pmatrix}
\in\operatorname{SL}_2(\mathbb C[x]),
\]
since \((1+x)T_N+x^{2N}=1\). It acts as a genuine polynomial
automorphism on a free coordinate pair and agrees modulo \(x^N\)
with reciprocal diagonal scaling. In a rank-three problem the
generators of \(C\) are not assumed to be ambient coordinates,
and the local fiber offers only the single coordinate \(r\).
Applying this matrix to unspecified free coordinates would therefore
assume the missing structure.

Adding one genuinely free variable does supply a second direction.
The unimodular slice matrix then gives stable polynomiality, already
proved in (4) of the preceding modification note. It does not remove
that added variable. The determinant-balanced rank-two control is
therefore evidence about the required structure of a repair, not a
proof of an unstabilized rank-three lift.

The root investigation's proposed recognition criterion is sound as
a conditional strategy: a globally étale birational morphism, an
isomorphism over the \(p\)-open set, and an isomorphism on the
complementary reduced divisor would be an isomorphism once these
properties are proved. Here no such new morphism has been constructed.
The canonical inclusion fails the \(p\)-open and étaleness conditions,
and the proposition shows that its canonical overlap rescaling cannot
repair it under a merely radical congruence.

The actionable remaining task is a polynomial coordinate construction
that moves the invariant-plane embedding while matching all finite
divisibility constraints, together with a polynomial inverse or a
verified global étale/birational certificate. The
[arbitrary-monic-polynomial extension](polynomial-curve-lift-pass18.md)
accomplishes this for its specified two-chart local-slice presentations,
extending the earlier binomial family. No all-base analogue has been
proved here, and general cancellation remains unresolved.

## Sources and check boundary

[^1]: G. Freudenburg, [*Actions of SL2(k) on affine k-domains and fundamental pairs*, Theorem 2.4](https://arxiv.org/pdf/2108.12021v2), for the standard three-variable kernel and plinth statements. Sections 2 and 3 above are direct deductions, not statements attributed to that theorem. The residue-form calculation is included locally in (9), and no classification theorem for arbitrary affine modifications is assumed.

Audit, 2026-09-12: the complete
[finite Vandermonde reconstruction](rescaling-obstruction-audit-pass18.md)
was independently checked against Section 2 above. No gap was found
for a nonzero primitive LND, a minimal local slice with \(Dr=p\) generating
the plinth, nonzero \(V\) comaximal with \(p\), and the stated
kernel-fixing pure rescaling with unit multiplier congruent to 1 modulo
the radical. Its binomial truncation has valuation error at least
\(nd+1\), while all Taylor denominators cost at most \(nd\);
finite Vandermonde inversion then gives the same contradictory linear
coefficient. It therefore proves the identical necessity statement
without completion or logarithms. This remains an internal algebraic
cross-check, not expert review, a formal proof-assistant certificate,
or evidence establishing novelty.
