# A nice coefficient relation forces proportional original speed

In the actual terminal quartic coordinates, a polynomial nice
derivation fixes the surviving good coordinate \(w\).
The known three-variable linear-invariant theorem then supplies
a relation among its coefficients over \(k(w)\).
The highest original flow coefficient of that relation forces
\(Ew\) either to vanish or to be a nonzero complex multiple of
the original invariant factor \(g\).

This is an original-ring speed constraint. By itself it does not
make \(g\) a coordinate, replace a local slice by an original
slice, or recognize the nonzero-speed branch.

## 1. The algebraic lemma and its actual hypotheses

Let
\[
B=k[a,b,z,w],\qquad k=\mathbb C,\qquad
E\in\operatorname{LND}_k(B).
\]
The four displayed generators are actual polynomial coordinates.
Suppose \(g,N,U\in B\), with \(g\ne0\), satisfy
\[
Eg=0,\qquad EN=\frac{g^2}{2},\qquad EU=gN,\qquad
p:=Ew,\qquad Ep=0.
\tag{1}
\]
Define the polynomial derivation
\[
T=\frac U3\,\partial_a+N\,\partial_b+g\,\partial_z,
\qquad Tw=0,
\tag{2}
\]
and suppose that \(Tg=TN=TU=0\).
Then \(T^2\) kills the four actual generators, and the Leibniz
rule proves that \(T\) is locally nilpotent on \(B\).
It is nonzero because \(Tz=g\ne0\).
Equivalently one may assume this actual polynomial nice derivation
has already been established.

**Lemma.** Under (1)--(2),
\[
\boxed{\ p=0\quad\text{or}\quad p=\lambda g
\text{ for some }\lambda\in k^*.\ }
\tag{3}
\]
The proof does not require an original slice or an adjoint-height
assumption. Those additional hypotheses are retained in the
terminal-quartic application below.

## 2. The precise established linear-relation input

Since \(Tw=0\), \(T\) extends to a nonzero
\(k(w)\)-linear LND of the actual polynomial three-ring
\(k(w)[a,b,z]\). It remains nice on these three generators.

Wang's linear-invariant theorem, stated as Theorem 3.1(i) in
Dasgupta and Gupta, applies over any characteristic-zero field,
so in particular over \(k(w)\). It provides a nonzero
\(k(w)\)-linear form in \(a,b,z\) killed by \(T\).[^nice]
Applying \(T\) to that form, absorbing the constant factor \(1/3\),
and clearing a common denominator in \(k[w]\), gives
\[
A(w)U+B(w)N+C(w)g=0,
\qquad A,B,C\in k[W],\quad (A,B,C)\ne(0,0,0).
\tag{4}
\]
Here \(W\) is a formal one-variable argument and \(w\) is its
actual coordinate value. Consequently a nonzero polynomial
coefficient does not vanish upon substitution.

No assertion that \(E\) fixes \(w\) has been used.
Only \(T\) is extended as a \(k(w)\)-linear derivation.
The source's irreducibility hypothesis occurs in its separate
part (iii), not in the linear-form assertion used here.
No primitivity or fixed-point-free premise for \(T\) is inserted.

The cleared relation (4) belongs to the original polynomial ring.
The common denominator need not be \(E\)-invariant: it has already
been cleared before the original derivation is applied.

## 3. Compare the highest original flow coefficient

Assume \(p\ne0\). Equations (1) give the exact finite flow formulas
\[
\exp(tE)w=w+tp,\qquad
\exp(tE)N=N+\frac{t g^2}{2},
\]
\[
\exp(tE)U=U+t gN+\frac{t^2g^3}{4},\qquad
\exp(tE)g=g.
\tag{5}
\]
The coefficient \(1/4\) uses \(E^2U=g^3/2\), followed by
division by \(2!\).

Applying the actual exponential automorphism to (4) gives
\[
A(w+tp)\left(U+t gN+\frac{t^2g^3}{4}\right)
+B(w+tp)\left(N+\frac{t g^2}{2}\right)
+C(w+tp)g=0.
\tag{6}
\]
For zero polynomials omit the associated degree. Put
\[
d=\max\{\deg A+2,\ \deg B+1,\ \deg C\}.
\tag{7}
\]
Define \(A_*\) to be the leading coefficient of \(A\) if
\(\deg A+2=d\), and zero otherwise. Define \(B_*,C_*\)
in the analogous way using the other two weighted degrees.
At least one of these complex constants is nonzero.

The coefficient of \(t^d\) in (6) is
\[
A_*p^{d-2}\frac{g^3}{4}
+B_*p^{d-1}\frac{g^2}{2}
+C_*p^d g=0,
\tag{8}
\]
where a summand with zero starred coefficient is absent.
Every displayed summand with nonzero coefficient has a
nonnegative exponent before division.

In \(\operatorname{Frac}B\), divide (8) by
\(g p^{d-2}\ne0\). This is legitimate even when \(d<2\):
a negative exponent is an inverse in this field, not a claimed
polynomial divisor. The result is
\[
\frac{A_*}{4}g^2+\frac{B_*}{2}pg+C_*p^2=0.
\tag{9}
\]
The homogeneous polynomial
\(A_*X^2/4+B_*XY/2+C_*Y^2\) is nonzero, since its three
monomials are distinct and at least one starred coefficient
is nonzero.

Since \(g\ne0\), the element \(p/g\) is a root of the nonzero
polynomial
\[
A_*/4+(B_*/2)Z+C_*Z^2\in k[Z].
\]
Algebraic closedness of \(k=\mathbb C\) implies \(p/g\in k\).
It is nonzero because \(p\ne0\). This proves (3).

There is no low-degree exception hidden in (7)--(9).
If \(d=0\), only a nonzero constant \(C\) could occur, and
(4) would already contradict \(g\ne0\).
If \(d=1\), the same division by \(g/p\) is valid and gives
(9), with \(A_*=0\); no nonnegative-exponent assumption is
made about that dividing element.
Zero \(A\) or zero \(B\) is handled by the omitted-term rule.

## 4. Application to the actual terminal moving quartic

The [parabolic terminal form](terminal-quartic-parabolic-form-pass71.md)
uses actual coordinates \(a,b,z,w\) obtained by constant
changes and an explicit polynomial shear.
Both \(\partial_a\) and \(\partial_w\) retain their original
good second-adjoint bounds.

Its rational symmetry is
\[
S=\partial_z+\beta\partial_b+\kappa\partial_a,\qquad
Sg=S\beta=S\kappa=Sw=0,
\]
\[
\delta=E/g,\qquad
\delta\beta=\frac12,\qquad
\delta\kappa=\frac{\beta}{3},\qquad
[\delta,S]=0,\qquad \delta^2w=0.
\tag{10}
\]
The original-slice argument in the preceding quartic reduction
established \(Sg=0\) before any local-nilpotence descent.
The original velocities give actual polynomials
\[
N=g\beta\in B,\qquad
U=3g\kappa=Eb-g(z/2+c_0)\in B,
\tag{11}
\]
where \(c_0\) is the complex constant from that form.
Thus \(T=gS\) is exactly (2), and its polynomial coefficients
are fixed by \(T\). This is a single-power polynomial descent,
not just the existence of an unspecified power clearing its poles.

Equations (10)--(11) give
\(EN=g^2/2\), \(EU=gN\), and \(Ep=E^2w=0\).
Every hypothesis of the lemma is therefore satisfied.
Consequently the actual surviving good coordinate obeys
\[
Ew=0\quad\text{or}\quad
Ew=\lambda g,\qquad \lambda\in\mathbb C^*.
\tag{12}
\]
In the nonzero alternative,
\(\delta(w/\lambda)=1\), but \(E(w/\lambda)=g\), not one.
The coordinate \(w/\lambda\) is not promoted to an original
slice when \(g\) is nonconstant.

If \(Ew=0\), the original action fixes the actual ambient
coordinate \(w\). Its supplied original slice makes its kernel
regular, and the already retained invariant-coordinate theorem
recognizes that kernel.
The nonzero alternative of (12) is an exact additional input
for a separate actual-coordinate recognition argument; this
note does not claim that proportional speed alone is that endpoint.

## Source and verification scope

The complete parabolic form and its actual coordinate choices were
read before applying the lemma. The needed polynomiality of \(U\)
follows directly from its original bad velocity as in (11), so no
unverified denominator is being discarded.
The highest-flow coefficient argument above is supplied in full,
including all coefficient-degree boundary cases.

The stated characteristic-zero linear-form theorem was read directly
in the retained primary text. The source attributes it to Wang.
This note does not claim a fresh read of Wang's original proof,
use the source's separate PID kernel-classification theorem,
or infer that a relative coordinate over \(k(w)\) descends to
an ambient coordinate over \(k\).

There is no new numerical suite or method, regression claim,
shared metadata edit, human expert review, proof-assistant
certificate or historical novelty verdict.
The pass70 packet and earlier frozen files are unchanged.

[^nice]: Nikhilesh Dasgupta and Neena Gupta, [*Nice derivations over principal ideal domains*](https://arxiv.org/pdf/1701.03635v1), arXiv:1701.03635v1, January 13, 2017, Theorem 3.1(i), PDF p. 5. The paper states Wang's result for every characteristic-zero field and attributes it to Wang, Proposition 4.6. Only the nonzero linear invariant is used here, not the rank or irreducible normal-form conclusions. The retained text is [dg-nice-1701.03635v1.txt](../tmp/pdfs/dg-nice-1701.03635v1.txt).

