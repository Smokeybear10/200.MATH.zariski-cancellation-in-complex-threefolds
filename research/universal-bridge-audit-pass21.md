# Independent audit of the universal finite-center bridge

**Verdict:** no mathematical flaw found in the finite-center lemma,
the prescribed-jet nonlifting control, or the singular intermediate-ring
control of [the main note](universal-bridge-pass21.md). The entire note
was read. This audit reconstructs its new algebra independently and
rechecks the specific source statements listed below. It does not
assert the missing recognition theorem.

## 1. The finite-center presentation is exact

With \(Dr=p\ne0\), the local-slice localization gives
\(R_p=C_p[r]\), and \(r\) is transcendental over \(C\).
Choosing one common denominator exponent for the three ambient
generators is legitimate. For
\(S=C[r]\) and \(I=p^NR\cap S\), both inclusions
\[
S[I/p^N]\subseteq R\subseteq S[I/p^N]
\]
hold: the first uses the contraction defining \(I\), and the
second uses the three fractions representing the original coordinates.
There is no missing saturation or requirement that \(R\) be a
free module over \(C\).

In the second presentation, the new indeterminate is evaluated at
\(w=r/V\), not at \(r\). Each transformed fraction becomes
\(\theta(F)(w)/p^N=F(r)/p^N\). These fractions and \(w\)
generate exactly \(R[w]\), while every element of the extended
ideal \(J=\theta(I)S\) gives an element of that same ring.
Thus both inclusions in the transformed presentation also hold.

Comaximality of \(p,V\) implies that \(V\) is invertible
modulo every \(p^N\). This justifies the inverse substitution,
surjectivity on the quotient, and equality of the quotient ideals.
The identity
\((p\partial_T)\theta=V\theta(p\partial_T)\) has the correct
factor of \(V\), and proves stability of the extended ideal.
The connectedness assumption is used only to obtain the previously
proved reduced congruence, not in this algebraic lemma.

Here "finite" means a finitely generated ideal and a bounded
thickening. It does not mean that \(S/(p^N)\) or its center
has finite dimension as a \(\mathbb C\)-vector space.

## 2. The counterexample meets the actual hypotheses

For \(D=x^2\partial_y+2y\partial_z\), the coefficient gcd
is one. Localizing at \(x\), then separating even and odd
powers of \(y\) after reducing a minimal pole denominator,
proves
\[
\ker D=\mathbb C[x,h],\qquad
\ker D^2=C\oplus Cy,\qquad h=x^2z-y^2.
\]
Hence the actual full plinth is \(x^2C\), and \(r=y\)
is a minimal local slice. The connected reduced plinth is the
line \(x=0\); \(V=1+x\) is comaximal with \(x^2\) and
is one on that line.

Importantly, the center used in the control is also the *canonical
contraction* in the lemma:
\[
x^2R\cap\mathbb C[x,h,y]=(x^2,h+y^2).
\]
This follows by mapping to \(R/(x^2)\), where \(h=-y^2\)
and \(z\) remains an independent variable. Thus the example
does not exploit a larger class of artificial centers.

If a polynomial automorphism preserves \((x^2)\), unique
factorization makes its image of \(x\) a nonzero constant
multiple of \(x\). The prescribed quotient map forces that
constant to be one. Arbitrary corrections to the other two
coordinates therefore have the forms in the main note, and their
Jacobian is \(1+x\pmod{x^2}\). Its nonzero linear coefficient
contradicts a constant Jacobian. This argument allows arbitrary
\(\mathbb C\)-algebra automorphisms of \(S\), not only
automorphisms fixing the invariant plane pointwise.

The scope separation is essential and correct. The triangular
shift of \(h\) in equation (10) carries the two full ideals
to one another, preserves the denominator, and has a polynomial
inverse. Also \(y=(1+x)w\) proves directly that
\(M=\mathbb C[x,w,z]\). Thus only the specified quotient
automorphism fails to lift; neither center transport nor absolute
polynomiality fails in this example. Likewise, the nonextension
of \(\partial_T\) is exact: fixing \(x,h\) forces the image
of \(z\) to be \(2y/x^2\notin R\).

## 3. Reconstruction-source and singular-stage checks

The [Dasgupta–Gaifullin author text](https://arxiv.org/html/2306.00510v2)
was reopened at Lemma 3.17, Corollary 3.18, Theorem 4.5(i), and
Lemma 5.1, including their relevant proofs. The invariant ambient
coordinates in the modified-commuting construction are explicit.
The rank-three obstruction applies to primitive derivations and
nonequivalent commuting LNDs. Restriction to \(C[r]\) supplies
only a possibly proper polynomial subalgebra. The main note does
not import an unrestricted claim from Remark 5.2.

The [Freudenburg primary preprint](https://arxiv.org/pdf/1602.08786)
was reopened at Theorem 4.4 and Sections 8.2.1–8.2.3. It gives
the stated degree reconstruction and the displayed first two
positive-degree rings. Independently,
\(xg=f^3+r^2\) expands identically. The polynomial
\(XG-F^3-T^2\) is prime, by primitive linearity in \(G\),
and the image contains the three algebraically independent
elements \(f,g,r\). This confirms the presentation, not just
one relation. The origin has tangent dimension four on a
three-dimensional hypersurface, so that intermediate ring is
not a polynomial three-ring. Its singularity is sufficient to
invalidate the proposed polynomial-stage induction.

The graph and suspension comparisons elsewhere in Section 4 were
read as part of the complete note, but their separate primary
papers were not reread in this bounded independent audit. They
are not premises of the new finite-center lemma or either
explicit negative control. No additional inference about graph
connectivity or general cancellation is made here.

## 4. Verification boundary

Independent SymPy execution passed the invariant and local-slice
identities, primitive coefficient gcd, Bezout identity, inverse
quotient scaling, center shift and inverse, arbitrary-correction
Jacobian constant and linear coefficients, the rank-three relation,
and the singular gradient. The command used
`/opt/anaconda3/bin/python` and created no checker file.

The universal equalities are justified by the written inclusion
arguments, not those finite controls. This audit found no
correction requiring a change to the main note or registries.
