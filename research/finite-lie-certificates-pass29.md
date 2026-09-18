# Exact finite certificates for the algebraic-symmetry criterion

## What is verified

The [standalone verifier](finite_lie_certificate_checks_pass29.py) checks
finite rational polynomial data in the declared free ring
\(\mathbb Q[x_1,x_2,x_3,x_4]\). Extending coefficients to \(\mathbb C\)
preserves its verified identities. It checks the premises of
[the finite-Lie recognition deduction](levi-bridge-pass29.md),
not the proofs of its published structural inputs.

A certificate supplies a polynomial vector field \(\delta\), a finite
list of polynomial vector fields \(V_1,\ldots,V_m\), constant rational
relations placing \(\delta\) and all four coordinate partials in their
span, and a constant rational bracket table for every pair \(i<j\).
It also supplies a polynomial \(s\) and four positive integers \(n_i\)
with the asserted identities
\[
 \delta(s)=1,\qquad \delta^{n_i}(x_i)=0\quad(1\le i\le4).
\]

Every displayed identity is recomputed. The verifier rejects incomplete
tables, omitted translations, polynomial rather than constant structure
coefficients, false slices and inadequate nilpotence bounds. It accepts
only exact rational polynomial expressions, not expression strings,
floating-point coefficients, undeclared variables or rational functions
with a variable denominator.

The supplied spanning list need not be independent. Its length is only
an upper bound on the dimension of the generated Lie algebra.
Its members need not all be locally nilpotent: the known generating
set consists of \(\delta\) and the coordinate translations.

## Why the checked finite identities suffice for the premises

For a monomial \(x_1^{e_1}\cdots x_4^{e_4}\), the iterated Leibniz rule
distributes applications of \(\delta\) among its individual variable
factors. Once their number exceeds
\(\sum_i e_i(n_i-1)\), one factor has received at least its certified
nilpotence order. Every term then vanishes. Linear combinations give
local nilpotence on all polynomials, not just the four generators.

The verified bracket table makes the finite constant span of the
\(V_i\) a Lie subalgebra. Since all five required generators belong to it,
their actual generated Lie algebra is finite-dimensional.
Antisymmetry and vanishing self-brackets account for the unordered-pair
table. Jacobi is automatic for actual polynomial derivations; no abstract
table is being substituted for them.

Together with the verified slice, these are precisely the fourfold
premises used in the cited recognition deduction. Conditional on that
separate mathematical theorem, the complex kernel is polynomial in three
variables. The checker never labels this a solution for arbitrary
cylinders, nor does it claim to construct the kernel coordinates.

The coordinate symbols designate an actual free polynomial ring by the
input contract. A candidate coming from a purported change of coordinates
must separately establish its polynomial inverse before treating that
frame as genuine. No assertion about an unknown variety is encoded by
merely naming four functions.

## The nonsolvable positive certificate

The main fixture uses \(u=x+y^2\) and
\[
 \delta=(1+4yu)\partial_x-2u\partial_y
\]
with two passive variables. The seven-field list is the original
coordinate expression of
\[
 \partial_u,\quad\partial_v,\quad u\partial_v,\quad
 v\partial_u,\quad u\partial_u-v\partial_v,\quad
 \partial_{z_1},\quad\partial_{z_2},\qquad v=y.
\]
It contains semisimple, non-LND fields and nevertheless gives a valid
finite-closure certificate. The bracket constants come from the
independently known \(\mathfrak{sl}_2\ltimes\mathbb C^2\) table, not
a numerical fit or a solver imported by the checker.

The slice is \(u\), and valid original-coordinate nilpotence bounds
are \((5,3,1,1)\). The separate polynomial inverse
\(y=s-u^2,\ x=u-(s-u^2)^2\), with invariant \(s=y+u^2\),
provides an additional explicit recognition control.
Here the \(s\) in that inverse is an invariant coordinate, not the
generic slice variable named \(s\) earlier in the certificate contract.

An independent abelian certificate tests ordinary translation.
A contrasting finite-dimensional affine example
\(\partial_x+y\partial_y\) sends \(x\) to one but is not an LND.
The checker rejects it on its nonvanishing coordinate iterates.
Thus having a slice equation alone is not incorrectly accepted.

## Verification limits

The ten unittest methods passed in the initial main execution in
0.094 seconds. An independent adversarial audit found two input-validation
defects: SymPy could coerce a relation into a polynomial, and Python's
numeric key equality let float/bool indices bypass the table-key check.
The verifier now requires commutative scalar expressions and coordinates,
plus builtin integer table indices. New rejection controls cover both
defects. The corrected main run passed in 0.131 seconds and the independent
run in 0.092 seconds. A redundant spanning-list control still passes with
dimension upper bound eight. Repeated executions do not add methods.

An independent proof-premise reconstruction found no remaining gap in
constant bracket closure, translation inclusion, coordinate nilpotence,
or the separately verified slice. The saved complete regression was
started after these input corrections and the final independent audit.

The implementation deliberately supports a bounded rational certificate
format: at most 64 spanning fields and nilpotence orders at most 128.
These are input limits, not mathematical bounds asserted for arbitrary
LNDs or proof that a rejected certificate has no replacement. It is a
positive verifier, not a terminating search algorithm or a negative
decision procedure.

No solver, old checker, network input, symbolic string evaluation or
proof assistant is imported. SymPy performs the exact polynomial
arithmetic, while the published integration, transitivity and recognition
theorems remain human-readable mathematical dependencies.
