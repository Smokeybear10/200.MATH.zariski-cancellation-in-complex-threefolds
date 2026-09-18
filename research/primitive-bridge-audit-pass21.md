# Independent audit of the primitive noninvariant extension

The complete [pass-21 proof](primitive-noninvariant-bridge-pass21.md)
was read and reconstructed independently. Its primitive rank-three
example, fixed-base obstruction, minimum added-variable degree, and
polynomial-kernel conclusion are consistent. The one scope correction
found concerned the coefficient ring in its universal preliminary
identity, not the complex polynomial family. That correction is now
applied in the proof.

## 1. Coefficient-ring correction

Characteristic zero alone does not make the halves and eighths in the
universal formulas polynomial. The original Section 1 therefore needed
to require that the domain contain \(1/2\), or simply require a
\(\mathbb Q\)-algebra, as the corrected version now does.
For example \(a=q=c=1\) over \(\mathbb Z\) meets the written
relation \(ac=q^2\), but \(qx/2-at\) is not integral.

To accommodate the stated dependence on the fixed invariant \(h\)
without ambiguity, one can take \(a,q,c\in K[h]\), with
\(0\ne a\), \(ac=q^2\), and work in \(K[h,x,r,t]\),
fixing \(K[h]\). Here \(K\) is a domain containing \(1/2\).
The physical application has \(K=\mathbb C[f]\), so it already
meets this hypothesis. Renaming the affine-slice coefficient in
Section 5 avoids shadowing the fixed coefficient \(a=f^n\);
that is a notation improvement, not a mathematical defect.

## 2. Exact second image and minimum degree

The monic chart in Section 3 has basis \(x^j r^\epsilon\),
\(\epsilon\in\{0,1\}\), over \(C[f^{-1}]\). Their
distinct derivation degrees \(2j+\epsilon\) justify the full
degree-at-most-two span. The no-poles argument is valid: after reduction
modulo \(f\), the exponent classes \(0,3,1\pmod5\) cannot
cancel. Consequently
\[
\ker D^3=C\oplus Cr\oplus Cx,
\qquad D^2(R)\cap C=f^{2n}hC.
\]
This is a complete second-image calculation, not a bounded search.

For a hypothetical slice \(A t+v\), coefficient comparison gives
\(DA=0\) and \(Dv+A(1+qr)=1\). Applying \(D\) puts
\(A f^nhq\) in the displayed second image. Since
\(q=f^\ell J\) and \(J(0,h)\ne0\), this forces
\(f^{n-\ell}\mid A\). Evaluation at the fixed origin forces
\(A(0)=1\), contradicting that divisibility. This also covers
the possibility of a slice independent of \(t\).

The quadratic coefficient of the displayed slice is \(f^nhq/2\),
which is nonzero. Therefore the claimed minimum \(t\)-degree is
exactly two. The same image calculation proves the exact criterion
\(1+qr\in C+D(R)\) if and only if \(f^n\mid q\), including
the reverse implication via \(D(qx/(2f^n))=qr\).

## 3. Arbitrary invariant coefficient and physical inverse

The argument does not require \(J\) to be constant or a unit.
The condition \(J(0,h)\ne0\) means a nonzero polynomial, not
nonvanishing at every point. It is used for exact \(f\)-valuation.
Meanwhile \(2\ell\ge n\) implies both
\(q^2\equiv0\) and \(q q_h\equiv0\pmod{f^n}\).
These are precisely the two vanishings needed to substitute
\(q(f,X^5)\) into the finite curve formula.

On the universal old curve, put \(q_0=q(f,u^5)\). Modulo
\(f^n\), the parameter is \(X=u+q_0u^4\), with inverse
\(u=X-q(f,X^5)X^4\). Substitution into the displayed
\(\widetilde P\) gives both
\(\rho=X\widetilde P\) and \(h=X\widetilde P^2\).
These are identities in the parameter ring, so they base-change to
the physical ring without cancelling a possibly nonregular parameter.

For the forward physical lift, the first numerator is divisible by
\(f^n\). Multiplication of the second numerator by \(X\)
gives \(f^{2n}(Y^2+f)\). The polynomial
\(f=xz-y^2\) is prime and \(X\equiv x\pmod f\), so
the cancellation establishing polynomial \(Z\) is valid.

For the inverse, \(f=XZ-Y^2\) is likewise prime in the independent
target polynomial ring. The inverse surface map has
\(x\equiv X\pmod f\). The inverse curve identity first gives
polynomial \(y=(r-x^3)/f^n\). Multiplication of the original
\(z\)-numerator by \(x\) then gives
\(f^{2n}(y^2+f)\), proving polynomial \(z\). Thus both maps
are global polynomial maps. Their known inverse identities after
inverting \(f\) imply the global inverse identities, since the
two polynomial rings inject into their localizations.

## 4. Verification and limits

The audit independently ran eleven exact identities for the universal
surface map: the two invariant coordinates, the slice identity, both
quadratic-relation identities, and all six inverse compositions.
Three additional universal square-zero calculations checked the two
curve identities and the coefficient-substitution congruence. These
were actual standalone SymPy calculations, with no project solver
imports; this audit creates no additional test suite or registry entry.

The coefficient-domain correction was applied by the proof author,
as was the renaming of the affine-slice coefficient to \(A\).
No defect was found in the complex family or the physical inverse.
This audit inherits the previously checked base-family and modification
results through their linked proofs. It is not a new primary-source
novelty audit, a formal Lean verification, or human expert review.
It does not establish an invariant-extension frame for every slice LND.

## 5. Standalone checker audit

The complete [fourteen-method checker](primitive_bridge_checks_pass21.py)
was inspected and independently rerun: **14 tests passed in 28.826s**
before the small assertion cleanup described below.
The core controls are not circular. The inverse is written separately
from the forward map; the physical derivation is computed from the
Jacobian; the inverse curve test recomputes \(q(f,h)\) using its
new invariant \(h\); and the relation reduction uses the defining
relation \(q^2-ac\), not an asserted target formula.

Some initial supplementary assertions were redundant rather than
independent formula checks: the final two explicit-curve assertions in
`test_physical_second_denominator_cancellation` merely truncate their
already-written expected polynomials, and the residue-set equality in
`test_second_image_residue_independence` was tautological. The separate
forward and inverse curve methods provide the actual formula controls.
The proof author removed the residue-set assertion and replaced the
two explicit-curve assertions by solving for the correction coefficient
from the actual forward curve. The two affected methods independently
passed again in **0.063s**. These fixes leave the method count at fourteen.

The conductor matrix test verifies only its encoded incidence matrix,
not the derivation of the geometric configuration. Similarly, the
fixed \(H,L\) in the Jacobian-obstruction test are finite instances,
not a symbolic quantification over all polynomial corrections.
The suite does not expand the full physical four-generator inverse;
that conclusion combines the tested surface and curve identities with
the written prime-cancellation argument. Rank classification, the full
second-image equality, and the minimum-degree theorem remain written
proof obligations, not consequences of finite grids.

The negative controls do cover loss of \(ac=q^2\), the gaugeable
boundary \(f^n\mid q\), and failure of polynomial \(q^2/f^n\)
outside the stated valuation window. They do not assert that failure
of the displayed construction proves nonexistence of another slice.

## 6. Bounded primary-source priority check

The additional search targeted quadratic slices, extensions with
coefficient \(1+qr\), the special coefficient \(1+xy\), and
minimum slice degree. It did not establish priority for the conjunction
of the rank-three example, fixed-base obstruction, and exact minimum
\(t\)-degree. In particular, unproductive exact-string searches
are not evidence of novelty.

A definite prior implication applies to a narrower universal model.
Let \(S\) be a \(\mathbb Q\)-domain, \(0\ne p\in S\), \(q\in S\),
and \(p\mid q^2\). On \(S[r,t]\), the derivation
\[
T=p\partial_r+(1+qr)\partial_t
\]
is divergence-free and fixed-point-free, since
\[
(1-qr)(1+qr)+(q^2/p)r^2p=1.
\]
Thus slice existence and a polynomial kernel follow from
[Berson--van den Essen--Maubach, *Derivations having divergence zero on R[X,Y]*](https://www.math.ru.nl/~maubach/Papers/DerivHavingDivZero.pdf),
Theorem 3.7, printed p. 5, in Nijmegen Report 9918 (April 1999), read
with the definition of its property \(B(R)\) on printed p. 3.
The cover makes these PDF pages 6 and 4, respectively.
This deduction covers the preliminary
\(h\)-divisible subfamily with \(p=f^nh\). It does not directly
cover the main weaker divisibility \(f^n\mid q^2\), nor prove
the obstruction for the original rank-three base.

[Freudenburg, *Actions of SL2(k) on affine k-domains and fundamental pairs*](https://arxiv.org/pdf/2108.12021),
Lemma 2.2, already permits arbitrary added coefficients. Its Theorem
7.6 instead assumes a fundamental derivation and an invariant added
coefficient. These statements were read directly; neither supplies the
specific noninvariant minimum-degree conclusion by its stated hypotheses.

[Freudenburg, *Derivations of R[X,Y,Z] with a slice*](https://doi.org/10.1016/j.jalgebra.2008.05.007)
is a concrete remaining comparison lead: the publisher abstract and
[author's 2009 conference abstract](https://www2.cms.math.ca/Events/summer09/abs/pdf/aga-gf.pdf)
describe explicit families over two-parameter polynomial coefficient
rings. The full example formulas were not accessed in this bounded
check. No assertion that those examples are different is justified yet.
This access and comparison limitation keeps the family-level priority
assessment unresolved.
