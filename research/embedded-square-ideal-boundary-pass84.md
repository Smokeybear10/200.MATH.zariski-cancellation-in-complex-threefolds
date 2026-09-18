# Embedded square defects at the ideal level

There are three-generated ideals in a regular three-variable ring with
no isolated components and an element satisfying the stronger condition
q^N in I^(N+1) for some N, whose square does not belong to the ideal.
The example below has precisely the embedded, critical,
analytic-spread-three behavior left by the
[square-support theorem](rank-one-square-embedded-support-pass84.md).
It is **not an actual speed ideal with the chosen acceleration**:
the required original-action trace relation fails for every admissible
unit bad speed. A second example retains both that trace relation and
the strict power condition but fails the next determinant condition.

These are ideal-level boundaries, not counterexamples to square
membership for actual sliced actions or to cancellation.

## 1. Strict ideal dependence with a nonzero square defect

In the actual polynomial ring R=C[x,y,z], put
\[
f=(x^{10},xy^9,xz^9),\qquad I=(f),\qquad q=x^4y^4z^4.
\tag{1}
\]
These symbols are polynomial data only; no derivation or supplied
slice is being asserted. The monic equation
\[
q^9-x^8f_1^2f_2^4f_3^4=0,
\qquad x^8f_1^2f_2^4f_3^4\in I^{10}.
\tag{2}
\]
proves the strict condition q^9 in I^10, as well as ordinary ideal
integrality, since I^10 is contained in I^9. Yet q squared is
x^8 y^8 z^8, divisible by none of the three monomial generators.
Hence q squared is not
in I, while q cubed is in I, since its x exponent is twelve.

The full scheme and the defect annihilator are explicit:
\[
I=(x)\cap(x^{10},y^9,z^9),\qquad
\sqrt I=(x),\qquad
(I:q^2)=(x^2,y,z).
\tag{3}
\]
The intersection follows by the monomial least-common-multiple rule.
It is an irredundant primary decomposition: the first ideal is prime,
and the second is primary to m=(x,y,z), with finite-dimensional
quotient. Thus Ass(R/I) consists exactly of (x) and m. The underlying
zero set is a plane, with no isolated points, but the origin is an
embedded associated point.

The cyclic square-defect module is R/(x^2,y,z), so it has length two
at the origin. In particular, it need not itself be a socle line:
x q squared is nonzero, although x squared, y and z annihilate q
squared. No reduction of the original speed scheme is used here.

All entries of the full Jacobian matrix of f vanish at the origin.
The analytic spread of I at m is three. Indeed, the generators are
homogeneous of degree ten and their exponent vectors form the columns
of a matrix with determinant 810. Distinct monomials of degree n in
the three generators therefore remain distinct monomials of spatial
degree 10n. None of their nontrivial constant linear combinations
lies in m I^n, whose nonzero homogeneous terms have degree at least
10n+1. Consequently the special fiber algebra is the polynomial
three-ring. This elementary computation proves the stated spread,
not merely a numerical estimate.

## 2. Why these data cannot satisfy the actual trace gate

For an actual rank-one quadratic action in the original coordinates,
ambient zero divergence and the specialization of E(b)=q give
q_0 congruent to -b_0 div(f) modulo I, with b_0 a unit modulo I.
The contribution sum f_i partial_i(b_0) vanishes modulo I; thus
this relation uses the actual specialized speeds, not an arbitrary
choice of generators.

For (1), however,
\[
\operatorname{div}f=10x^9+9xy^8+9xz^8,
\qquad I\subseteq\mathfrak m^{10},\quad q\in\mathfrak m^{12},
\quad \operatorname{ord}_{\mathfrak m}(\operatorname{div}f)=9.
\tag{4}
\]
Multiplication by any unit of R_m preserves the nonzero leading
degree-nine form. Therefore q+b_0 div(f) cannot belong to I R_m
for any such unit b_0. Every quotient-unit bad speed would be a
local unit at this embedded point. This excludes an actual lift
of the displayed pair (f,q) before any return-map consideration.

The Jacobian determinant itself is 810 x^11 y^8 z^8 and belongs to
I. This is consistent with the absence of isolated points, but it
does not repair the failed first trace condition. The example
shows only that even the strict power condition and no isolated
components do not imply square membership without further
actual-action identities.

## 3. A trace-linked first-power boundary

Root supplied the separate polynomial triple
\[
\widetilde f=(y^3+x^3y^2/3,x^3,0),\qquad
\widetilde I=(x^3,y^3),\qquad
\widetilde q=-\operatorname{div}\widetilde f=-x^2y^2.
\tag{5}
\]
With the formal choice b_0=1, its first trace relation holds.
The element -x squared y squared has its cube equal to
-x^6 y^6, a product of four ideal generators up to sign. Thus
it satisfies the strict condition q cubed in the fourth ideal
power. It does not belong to the ideal, but its square does.

This companion still cannot be the required actual specialized
data. If L is the Jacobian matrix of the displayed triple and
d=-x squared y squared, the coefficient of t in
(1+td)det(Id+tL)-1 vanishes, but the coefficient of t squared has
remainder -9x squared y squared modulo the ideal.
Thus trace-linked strict ideal dependence alone does not impose
all the frozen pass82 quotient determinant identities.
No actual action, return involution or coordinate inverse is claimed
for either ideal-only example.

## 4. Exact computation and provenance

The standalone [checker](embedded_square_controls_pass84.py) has
one method and imports only `unittest` and SymPy. It checks the
strict-power monic equation, exact monomial primary intersection
and colon, nonzero square and its annihilators, exponent determinant, critical
Jacobian and degree mismatch. The same method checks the companion's
ideal, trace, integral equation and failed second determinant
coefficient. These finite calculations are not a universal proof
of actual-action recognition or of a source theorem.

The first two attempts failed at a SymPy `GroebnerBasis` object
comparison, first because of QQ versus ZZ coefficient domains and
then because the basis objects compared unequal despite identical displayed
bases. Comparing canonical basis expressions corrected that harness
issue; no polynomial formula or mathematical assertion changed.
The failed output chunks were `8ecb2a` and `49e8e4`.

The earlier weaker examples passed one method in 0.038 seconds,
chunk `4d08f7`. Before freezing this draft, Root requested the stronger
strict-power examples now displayed above. The final one-method run
of that revised control passed in **0.074 seconds**, exit zero,
with complete output chunk `cc352e`. No formula in this stronger
version failed. The final checker SHA256 is

```text
cc97022922c597dc3a428808cb1b478d4eebbf1b18791aa48e039e1cdd8714fd
```

Jet derived the initial square-defect mechanism during the bounded
construction task. Root supplied both strict-power parameter upgrades,
the companion triples and the explicit trace gate. No historical
novelty is asserted for these elementary examples. The later
[print-only pass84 runner](run_targeted_pass84.py) keeps this one
ideal-only method separate from Root's two actual-slice methods.
Its canonical execution and capture belong to Root. No full
regression or search was run here, and no pass83 or earlier file
was changed.
