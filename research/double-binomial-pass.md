# Stable coordinates with two pure-power terms

Let \(A,B,C\in\mathbb C[x,y]\), with \(A,B\ne0\), and let
\(n,q\) be positive integers.
Set
\[
F=A(x,y)u^n+B(x,y)z^q+C(x,y).
\]
Then
\[
\boxed{F\text{ is a stable coordinate}\quad\Longrightarrow\quad
F\text{ is a coordinate of }\mathbb C[x,y,u,z].}
\tag{1}
\]
In particular every original LND slice in this family has polynomial
three-variable kernel. No upper degree bound is imposed.

If both \(n,q\ge2\), there is a stronger classification:
stability is equivalent to the existence of base coordinates \(a,b\)
and nonzero univariate polynomials \(r,p\) such that
\[
\boxed{C=b,\qquad A=r(a),\qquad B=p(a).}
\tag{2}
\]
A constant can be absorbed into \(b\), and nonzero constant
coefficient polynomials are permitted. The completion of
\(F=b+r(a)u^n+p(a)z^q\) is immediate.

The argument combines the general rationally acyclic binomial-fiber
criterion with a necessary condition obtained from the cyclic quotient.
It does not reduce arbitrary slices to this presentation. No novelty,
human review, or proof-assistant verification is claimed.

## 1. The general binomial-fiber input

For \(G=f(x,y)v^d+g(x,y)\), \(f\ne0\), \(d\ge1\), a
general smooth rationally acyclic fiber forces \(G\) to be a
coordinate. More specifically, a base automorphism makes \(f\)
univariate; if \(d\ge2\), base coordinates can be chosen with
\[
f=p(a),\qquad g=b.
\tag{3}
\]
The full proof and constant cases are in the
[binomial-fiber note](generic-rational-binomial-pass.md).

The distinction from a single special fiber is essential. A general
level supplies transverse intersection with the reduced coefficient
divisor. The cited affine-modification lemmas make its components
disjoint affine lines. For \(d\ge2\) they also force the general
\(g\)-fiber to have Euler characteristic one. Monodromy is transitive
on its components, so it is one affine line, and plane-line
rectification yields (3).[^1]

## 2. A root-specialization lemma for a pure power

Suppose
\[
L=p(a)v^d+R(a,b,w)
\tag{4}
\]
is stable, with \(0\ne p\in\mathbb C[a]\) and \(d\ge1\).
For every root \(\alpha\) of \(p\),
\[
\boxed{R(\alpha,b,w)\text{ is a coordinate of }\mathbb C[b,w].}
\tag{5}
\]
This is only a necessary condition for general \(d\); no general
converse for (4) is asserted here.

For \(d>1\), take the cyclic quotient \(v\mapsto\zeta v\).
Writing \(W=v^d\), its level hypersurface is
\[
J_\lambda=\{p(a)W+R(a,b,w)=\lambda\}.
\]
Finite-quotient rational cohomology identifies its cohomology with
the invariant part upstairs, so \(J_\lambda\) is rationally
acyclic.[^2] For \(d=1\), use the original fiber itself.

The quotient is smooth. A critical point of its defining polynomial
must have \(p(a)=0\). Choose \(v\) with \(v^d=W\).
The \(a,b,w\) derivatives upstairs agree with those downstairs,
and the \(v\) derivative is \(dp(a)v^{d-1}=0\). Such a point
would therefore be critical for \(L\), contradicting stability.

Let \(\alpha_1,\ldots,\alpha_k\) be the distinct roots of \(p\).
Choose \(\lambda\) generic for the finitely many polynomials
\(R(\alpha_i,b,w)\), avoiding the values of any constant ones.
The open part of \(J_\lambda\) is
\[
U=(\mathbb C\setminus\{\alpha_1,\ldots,\alpha_k\})
\times\mathbb A^2_{b,w},
\]
and its closed part is a disjoint union of smooth divisors
\[
Z_i=C_i\times\mathbb A^1_W,\qquad
C_i=\{R(\alpha_i,b,w)=\lambda\},
\]
some possibly empty at this stage.

The rational Gysin sequence supplies isomorphisms
\[
H^1(U;\mathbb Q)\longrightarrow
\bigoplus_iH^0(Z_i;\mathbb Q),\qquad
0=H^2(U;\mathbb Q)\longrightarrow
\bigoplus_iH^1(Z_i;\mathbb Q).
\tag{6}
\]
The adjacent groups of \(J_\lambda\) vanish by rational acyclicity.
In the first map, the circle class of \(a-\alpha_i\) maps to
one on each component of \(Z_i\), and zero on every other \(Z_j\).
Its vanishing order is one because the quotient by \(a-\alpha_i\)
is reduced at the chosen level, regardless of the multiplicity of
\(\alpha_i\) in \(p\).

Thus the first map can be an isomorphism only if every \(C_i\)
is nonempty and connected. The second gives \(H^1(C_i;\mathbb Q)=0\).
Each \(C_i\) is therefore an affine line. Its reduced irreducible
equation is a plane coordinate by plane-line rectification, proving (5).
For constant \(p\), the assertion has no roots to check.

## 3. A plane-coordinate test

For any \(k\in\mathbb C[b]\) and integer \(n\ge1\),
\[
b+k(b)u^n\text{ is a plane coordinate}
\quad\Longleftrightarrow\quad k\text{ is constant}.
\tag{7}
\]
The reverse implication is triangular.

For necessity, suppose \(k\) is nonconstant and choose a root
\(\beta\). Then
\[
b+k(b)u^n-\beta
=(b-\beta)\left(1+\frac{k(b)}{b-\beta}u^n\right).
\]
The quotient in the second factor is polynomial, and both factors
are nonunits. A coordinate minus a constant is irreducible, giving
a contradiction. A separate argument using a nonconstant unit on a
general affine-line fiber is recorded in the independent audit.

## 4. Compatibility of the two fixed-surface families

Assume now that \(n,q\ge2\) and that \(F\) is stable.
Every \(F\)-fiber is contractible. Choose a prime divisor of \(n\).
The corresponding cyclic action on \(u\) has fixed surface
\[
B(x,y)z^q+C(x,y)=\lambda.
\]
Smith theory makes this surface mod-prime acyclic.[^3] It is smooth:
at \(u=0\), a critical point of the three-variable polynomial
would be critical for \(F\). The finite CW model of a smooth
affine surface then implies rational acyclicity. Apply (3) to obtain
base coordinates \(a,b\) with
\[
C=b,\qquad B=p(a).
\tag{8}
\]

Apply the same argument to a prime divisor of \(q\), fixing \(z=0\).
It gives a base companion \(c\) to \(b=C\) such that
\[
A=r(c),\qquad \mathbb C[a,b]=\mathbb C[c,b].
\]
An automorphism of the one-variable polynomial ring over
\(\mathbb C[b]\) is affine with unit slope. Thus
\[
c=\kappa a+h(b),\qquad \kappa\in\mathbb C^*.
\tag{9}
\]

If \(p\) is constant, use the base pair \(c,b\); both coefficients
are already univariate in \(c\). If \(r\) is constant, use \(a,b\).
These give (2) directly.

Otherwise choose a root \(\alpha\) of \(p\). Regard \(F\) as
a polynomial in \(z\):
\[
F=p(a)z^q+\bigl[b+r(\kappa a+h(b))u^n\bigr].
\]
The root-specialization lemma makes
\[
b+r(\kappa\alpha+h(b))u^n
\]
a plane coordinate. By (7), \(r(\kappa\alpha+h(b))\) is
constant. Since \(r\) is nonconstant, degree of composition in one
variable forces \(h\) to be constant. Equation (9) then makes
both \(A\) and \(B\) univariate in the same coordinate \(a\).
This proves (2).

Conversely, (2) gives a coordinate completion by retaining \(a,u,z\)
and solving
\[
b=F-r(a)u^n-p(a)z^q.
\]
Thus (2) is also sufficient for stability and coordinatehood.

## 5. When exactly one exponent equals one

By symmetry assume \(n\ge2\) and \(q=1\). The fixed-\(u\)
argument still makes a general fiber of \(B(x,y)z+C(x,y)\)
rationally acyclic. Section 1 gives a base coordinate \(a\) with
\(B=p(a)\). It does not assert that \(C\) is a base coordinate.

Writing the other base coordinate as \(b\), the full polynomial is
\[
F=p(a)z+R(a,b,u).
\]
Section 2 shows that \(R(\alpha,b,u)\) is a plane coordinate
at every root of \(p\). The univariate-coefficient coordinate
theorem, including repeated roots, now makes \(F\) a coordinate.[^4]
For constant \(p\), solve directly for \(z\). This completes (1).

The stronger simultaneous statement (2) is not asserted in this
case. For example,
\[
F=a^2z+(1+ab)u^2+b+ab^2
\]
passes the root criterion at \(a=0\), where the remainder is
\(b+u^2\), and is a coordinate. Its base polynomial \(C=b+ab^2\)
is not a plane coordinate: its general fiber is a punctured line.

### The all-linear boundary is already a published theorem

For \(n=q=1\), stability makes the zero hypersurface irreducible,
smooth, and integrally acyclic. Kaliman–Vénéreau–Zaidenberg
Theorem 3.24 applies directly to
\(A(x,y)u+B(x,y)z+C(x,y)\) and makes it a coordinate.[^5]
Thus this boundary is included in (1), with attribution to the
published theorem. It is not a new classification. The stronger
simultaneous form (2) remains restricted to \(n,q\ge2\).

The coprime coefficient branch and the gcd-divisor geometry are
separately reconstructed in the two-linear notes. Neither a
coprime pair nor its normalized pair is silently assumed to
generate the unit ideal.

## 6. A smooth quartic defeats separate fixed-plane tests

Consider
\[
F=b+(a+b)^2u^2+a^2z^2.
\tag{10}
\]
Both fixed-surface polynomials are coordinates:
\(b+a^2z^2\) is a coordinate directly, while
\(b+(a+b)^2u^2\) is one in the base pair \(c=a+b,b\).
Nevertheless the two coefficient directions are incompatible.

The polynomial has no critical point. Indeed, \(F_u=2(a+b)^2u\)
can vanish only when \(u=0\) or \(a+b=0\), and in either case
\(F_b=1\). More explicitly,
\[
1=F_b(2-F_b)+2u^3F_u.
\]
At \(a=0\), however, the root remainder is \(b+b^2u^2\),
which fails (7). Thus (10) is not stable.

The exclusion can also be seen directly by Euler characteristic.
For \(\lambda\ne0\), its quotient under \(z\mapsto-z\) has
open part \(\mathbb C^*\times\mathbb A^2\) and closed part
\[
\{b+b^2u^2=\lambda\}\times\mathbb A^1.
\]
With \(v=bu\), that curve is
\(\mathbb A^1\setminus\{\sqrt\lambda,-\sqrt\lambda\}\):
\(b=\lambda-v^2\), \(u=v/(\lambda-v^2)\). Its Euler
characteristic is \(-1\). The quotient therefore has Euler
characteristic \(-1\), while its branch surface is an affine plane.
The double-cover formula gives
\(\chi(F^{-1}(\lambda))=2(-1)-1=-3\), excluding stability.

This is not a cancellation counterexample. It shows that separate
coordinatehood of the two fixed-surface polynomials, even combined
with global smoothness, does not replace the compatibility argument.

## Scope

The theorem settles the displayed two-pure-power presentation, including
the pure branch \(xu^n+f(x,y)z^q+g(x,y)\) with \(n\ge2,q\ge1\).
It does not settle \(xu^2+G\) for arbitrary three-variable \(G\),
or the unrestricted cancellation
problem. If either \(A\) or \(B\) is zero, the unused-variable
case can instead be handled by the known three-variable
stable-coordinate theorem; it is outside the nonzero-coefficient
statement above.

## Sources

[^1]: Shulim Kaliman and Mikhail Zaidenberg.
[*Affine modifications and affine hypersurfaces with a very transitive
automorphism group*](https://arxiv.org/pdf/math/9801076v2).
Lemmas 7.4–7.6 and Proposition 7.1. The genericity argument and
precise rational-coefficient scope are written in the linked
binomial-fiber note.

[^2]: Carlos Florentino and Jaime Silva.
[*Hodge-Deligne polynomials of character varieties of free abelian
groups*](https://arxiv.org/pdf/1711.07909).
Section 4.2, equation (5) and Proposition 4.3.

[^3]: Peter Symonds. [*Smith theory for algebraic
varieties*](https://personalpages.manchester.ac.uk/staff/peter.symonds/preprints/smith.pdf).
Section 4, Corollary 4.3 and Remark (1).

[^4]: Stefan Maubach.
[*The commuting derivations conjecture*](https://www.math.ru.nl/~maubach/Papers/The_Commuting_Dervations.pdf).
Corollary 4.2 and Theorem 4.5 for the univariate-coefficient
criterion over \(\mathbb C\), including arbitrary root multiplicity.

[^5]: Shulim Kaliman, Stéphane Vénéreau and Mikhail Zaidenberg.
[*Simple birational extensions of the polynomial ring C[3]*](https://arxiv.org/pdf/math/0104204).
Theorem 3.24, especially (i') implies (iv'). This is the exact
published two-linear-variable theorem, not just a theorem asserting
that a known affine-three-space quotient has the desired embedding.
