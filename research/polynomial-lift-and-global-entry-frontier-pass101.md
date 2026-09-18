# Polynomial lifting and the unrestricted entry problem

The nilpotent correction left by the whole-fiber calculation100 is now
excluded in a concrete infinite family of smooth polynomial threefolds.
This is an all-polynomial obstruction, not a search through bounded jets.
Separately, the supplied actual frame gives one stronger vanishing-order
bound, with an exact example showing why the argument cannot be repeated
indefinitely. An explicit tame family also rules out a dimension-only
degree cutoff for searching for the global coordinate witness.

The full cancellation conjecture remains unsolved. None of these results
proves that an arbitrary cylinder falls into the treated class. Their
scopes differ and should be kept separate:

| Result | Objects covered | What it does not establish |
| --- | --- | --- |
| Exact degree-two module and polynomial-lift obstruction | The specified primitive triangular fields on actual polynomial threefolds, and a stated polynomial shear | A classification of the remaining original four-coordinate frames |
| Stronger base orders | The retained actual quadratic frame with nonzero first normal action and nonzero speed normal | Infinite-order vanishing or a global lift of quotient commutation |
| No dimension-only spatial-degree cutoff | An explicit infinite family of actual tame translations on four-space | Nonexistence of adapted coordinates, or failure of an input-dependent bound |

## The full polynomial module removes the local correction in one family

For every integer \(m\ge1\), set
\[
A_0=\mathbb C[x,y,c],\quad f=y^2+x^m c,\quad
S_0=\mathbb C[x,f],\quad N=-x^m\partial_y+2y\partial_c.
\]
The [complete proof](quadratic-double-polynomial-lift-obstruction-pass101.md)
shows
\[
\ker(N^3)=S_0\oplus S_0y\oplus S_0c.
\]
The kernel here means the elements killed by the third iterate. It is a
free module over the invariant ring, not a claim that this vector space
is itself an invariant subring.

After inverting \(x\), the action is a nonzero constant multiple of
\(\partial_y\) over \((S_0)_x\), and the claim becomes the elementary
degree-two polynomial calculation. The important step is removing all
possible denominators. A relation with a minimal positive power of \(x\)
in the denominator would reduce modulo \(x\) to a relation between
polynomials in \(y^2\), their multiples by \(y\), and their multiples by
the independent variable \(c\). Independence of \(c\) and even/odd
parity force every coefficient to be divisible by \(x\), contradicting
minimality. This covers polynomials of every degree.

The whole fiber at \((x,f)\) is \(\mathbb C[y,c]/(y^2)\). If
\(N^3h=0\) and \(h\) is constant on its reduced line, the exact module
formula forces
\[
h\equiv\eta+d y\pmod{(x,f)A_0},\qquad \eta,d\in\mathbb C.
\]
Thus the variable coefficient \(\beta(c)y\) from100 cannot be lifted
in this family unless \(\beta\) is constant. Adding arbitrary higher
normal-order polynomial corrections cannot change this conclusion.

There are repairs after inverting \(x\), such as
\(yc+y^3/x^m=yf/x^m\), but they do not extend polynomially over the
fixed curve. Merely finding one nonpolynomial repair would not prove
the obstruction; the saturation argument excludes all polynomial ones.

For \(m\ge2\), the first normal action is zero, so this genuinely tests
the case that the leading cubic calculation left open. The proof also
includes \(m=1\), with its different coefficient in the other normal
direction. A stated shear \(C=c+P(x,y)\) preserves the conclusion.
For \(P=y^4+xy+1\), the specified \(c\) has degree four under the
transported derivation while \(C\) has degree two. The obstruction
therefore survives this explicit higher-degree choice of the actual
component parameter; it is not a general normalization theorem.

## One stronger actual bound, and the exact limit of that argument

In the retained original-frame sector with nonzero first normal action,
the [additional-order proof](quadratic-commutator-lift-pass101.md) gives
\[
N^2h\in\mathfrak m^2S,\qquad N^2F\in\mathfrak m^3S.
\]
The action on the component's conormal space is square-zero. The existing
base-order contraction94 converts its normal-order conclusion to base
order. The identity \(N^3h=0\) places the second derivative in \(S\).
The exact volume equation then supplies one additional base-ideal factor
for the second derivative of \(F\). The earlier good-center bound is
credited to94/96, not counted again as a new result.

An intrinsic polynomial control shows that this chain of reasoning is
sharp. With \(f=xc+y^2\), \(N_0=-x\partial_y+2y\partial_c\),
\(F_0=x+fy^2\), and \(h_0=xc\), one has
\[
N_0^2h_0=-2x^2,
\qquad N_0^2F_0=2x^2f.
\]
Their orders in the independent base parameters \((x,f)\) are exactly
two and three. The required cubic iterates vanish and the component and
whole-fiber ideals have the stated exact generators. A further induction
does not follow from those facts.

This control is not an original four-coordinate frame. The additional
original Jacobian identities might still provide information; the attempted
use of them in this bounded pass was inconclusive. It would be incorrect
either to claim a global lift or to claim that those identities can never
give one.

## Why fixed-degree searches cannot supply the unrestricted reduction

The [global entry audit](global-reduction-audit-pass101.md) gives a separate
all-degree result. For any integer \(k\ge2\), start with genuine coordinates
\((u,a,b,c)\), let \(E=\partial_u\), and set
\[
x_1=a+u^k,\quad x_2=b+x_1^k,\quad
x_3=c+x_2^k,\quad x_4=u+x_3^k.
\]
These successive shears have an explicit polynomial inverse. On the orbit
\(a=b=c=0\), their degrees in \(u\) are \(k,k^2,k^3,k^4\).
Distinct monomials of ordinary total degree less than \(k\) have distinct
leading orbit degrees, by uniqueness of base-\(k\) digits. Thus every
nonconstant polynomial of that spatial degree has \(E\)-degree at least
\(k\), regardless of its coefficients.

Consequently no nonconstant invariant, slice, or element killed by \(E^2\)
occurs below spatial degree \(k\). The explicit inverse supplies both a
slice and an invariant ambient coordinate of degree exactly \(k\), so the
bounds are attained. This is an entirely recognized positive example with
a polynomial kernel. It disproves a dimension-only search cutoff, not the
existence of a nonlinear adapted frame. An input-dependent bound remains
possible because the input complexity grows with \(k\).

The entry audit also distinguishes the remaining relative cubic branch
from the supplied quadratic branch. Even recognition of both would leave
the reduction from an arbitrary sliced action to that supplied frame.
The known invariant-coordinate recognition endpoint still requires that
coordinate as a premise.[^bgl] The new cutoff example explains why a
fixed ordinary-degree search cannot replace a proof of that premise.

## Verification and next mathematical obligation

The [canonical capture](verification-pass101-working.json) passes one suite
and two methods in 0.732291625 wall seconds and 0.337 unittest seconds.
The [standalone checker](quadratic_polynomial_lift_checks_pass101.py) tests
finite intrinsic module controls for \(m=1,2,3\), the exact shear and
localized repairs, and the separate sharp-order example with both ideal
equalities. It imports no earlier solver. Its finite parity table is a
control for the saturation argument, not a verification of all polynomials.
The all-\(k\) cutoff theorem has a written proof and no numerical suite.

Root read all three saved mathematical notes and the complete final checker,
reconstructed their key arguments, and inspected the relevant94/96
dependencies and the cited primary recognition statement with its short
proof. The module proof also received a complete independent AI
reconstruction by Geometry. Further saved-file reviews are recorded in the
checkpoint. None of these reviews is human peer review or Lean verification.
Historical full75 remains 146 suites/1047 methods and the registry remains
544. Neither was rerun or expanded as a proxy for the universal proofs.

The next concrete local obligation is to determine whether the saturation
argument has a counterpart for the actual remaining degree-two module,
without assuming a polynomial coordinate on the unknown threefold. The
separate unrestricted obligation is a justified coordinate/frame reduction
whose complexity may depend on the actual action, or a recognition argument
that avoids that reduction. More examples in a recognized intrinsic family
do not by themselves meet either obligation.

## Sources

1. [Whole-fiber actions100](quadratic-whole-fiber-actions-pass100.md), the remaining nilpotent coefficient and its precise scope.
2. [Polynomial lift obstruction101](quadratic-double-polynomial-lift-obstruction-pass101.md), complete family proof and explicitly transported shear.
3. [Additional-order argument101](quadratic-commutator-lift-pass101.md), actual conditional bounds and intrinsic sharpness control.
4. [Global reduction audit101](global-reduction-audit-pass101.md), all-polynomial cutoff theorem, older-result comparison and entry hypotheses.
5. S. M. Bhatwadekar, Neena Gupta and Swapnil A. Lokhande, [*Some K-theoretic properties of the kernel of a locally nilpotent derivation on k[X1,...,X4]*](https://arxiv.org/html/1501.01438v1#S3.Thmtheorem3.5), arXiv:1501.01438v1, Theorem3.5.

[^bgl]: Theorem3.5 of the primary paper listed above. Its statement and displayed short proof were inspected, not all of its deeper dependencies. This is an existing conditional recognition result, not a new arbitrary-frame theorem or a novelty clearance.
