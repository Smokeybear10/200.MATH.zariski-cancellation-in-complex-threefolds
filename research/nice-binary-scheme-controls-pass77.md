# Exact controls for the binary and transverse-scheme reductions

The standalone [checker](nice_binary_scheme_checks_pass77.py) has five
unittest methods and imports only `unittest` and SymPy. It uses no solver,
research-module imports, random samples or numerical approximation. Its
finite checks are separated below from the general written arguments.

## 1. Actual reduced and nonreduced scheme-jet examples

The first method checks the actual action and both adapted inverse orders
from the [scheme-jet note](transverse-ideal-scheme-jets-pass77.md):
\(E=(0,a,b-aw,1)\), with original good partial \(T=\partial_w\).
It also checks the following genuinely nonreduced variant, in the same
original coordinate order \((a,b,c,w)\):
\[
E=(0,a^2,(1+a)b-a^2w,1+a),\qquad Q=[T,E]=-a^2\partial_c.
\]
Put
\[
U=(1+a)b-a^2w,\qquad s=b+(1-a)w,\qquad V=c-Us.
\]
These are actual adapted coordinates \((a,U,V,s)\), with inverse
\[
b=(1-a)U+a^2s,\qquad w=-U+(1+a)s,\qquad c=V+Us.
\]
The checker substitutes both inverse orders simultaneously and computes
that the transported action is \(\partial_s\). It separately verifies
original niceness, the exact original commutator, goodness and the
annihilation of every velocity by \(Q\).

The transverse ideal is exactly \((a^2,b)\), so its coefficient quotient
is \(\mathbb C[a,c]/(a^2)\). In that ring \(\bar a\ne0\), while
\(\bar a^2=0\). The fourth velocity is the nonconstant unit
\(v=1+\bar a\), with inverse \(1-\bar a\), and its original Jacobian
has nonzero fourth row. This tests both features that would disappear
in a reduced quotient with constant fourth speed.

The exact quotient computations verify the full matrix identities
\(\bar N=N_0-wv^{-1}N_0^2\) and
\(\overline{\operatorname{Jac}Q}=-v^{-1}N_0^2\), including all
two-by-two minors and the square-zero identity. They also verify that
the invariant quotient coordinate \(V\) reduces to \(c\), the slice
reduces to \(v^{-1}w\), and a representative ideal-filtration identity.
The unrelated polynomial \(1+\bar a w\) is checked to be a nonconstant
unit with nonzero derivative. Thus constancy of the actual fourth
velocity cannot be justified by a general polynomial-unit assertion.

Both examples are actual linearly triangular nice sliced actions, with
free primitive intrinsic field. They are not examples in the unresolved
nonlinear ternary-cone branch and do not prove a general primitive
freeness statement.

## 2. Representative binary power bounds

The second method checks coprime homogeneous binary triples of degrees
two, three and four. Exact Groebner reductions test all monomial
generators of \((u,v)^{2e-1}\) against their velocity ideal. Homogeneity
checks the other containment in \((u,v)^e\). An explicit common-factor
triple fails the high-power inclusion, as expected.

These checks cover only the listed triples. The all-degree containment,
source parametrization, invariant descent and finite-subalgebra argument
remain written proofs in the
[binary descent note](nice-binary-parameter-descent-pass77.md). No full
original action realizing arbitrary binary data is asserted.

## 3. A bare conormal control

The third method verifies both inverse orders for
\(p=x,\ q=y+x^2w\), with unchanged \(z,w\), as well as
\((p,q)=(x,y)\), \(Tp=0\) and \(Tq=p^2\).
The ideal is proper and the derivative has the required quadratic
order. This is an actual polynomial coordinate map and an actual
constant partial, but no compatible nonlinear-cone action is supplied.
It checks the boundary stated in the
[conormal note](binary-conormal-obstruction-pass77.md), not that note's
general filtration or algebraic-independence reduction.

## 4. Graph Hessians and the square-zero boundary

For \(R=xz-y^2\), the fourth method checks the full scalar Hessian
identity with \(h=(1,t,t^2)\). With \(h=(1,t,t^m)\) for \(m=3,4\),
the same expression is the nonzero polynomial \(2(t^m-t^2)\).
It computes the original good-partial commutator and second velocity
derivative for the actual graph actions with \(m=2,3\), distinguishing
the nice conic action from the nonnice cubic member.

Both inverse orders for \(a=w+R(x,y,z)\) are checked. Separate actual
actions \(E=(1,w,w^m,0)\), at \(m=3,5\), have their translation
inverses, their Jacobian square zero and their homogeneous curve
relation checked exactly. The all-degree
[graph-parameter obstruction](graph-parameter-conic-obstruction-pass77.md)
is not inferred from those finite values of \(m\).

## 5. Stationarity with no omitted constant direction

The fifth method checks the separate
[two-shear omission control](stationary-parameter-omission-control-pass77.md)
at degrees two and three. Both actual inverse orders, the equality of
the proper parameter ideal with \((x,y)\), and the high-order
\(\partial_w\) derivatives are checked. It computes the exact
constant-direction chain rule and the two leading \(w\)-coefficients
used in the written all-polynomial omission proof. Formal symbols for
the two derivatives of a putative polynomial in \(p,q\) are independent
of \(z,w\); there is no finite search over possible such polynomials.

This is still a bare parameter construction, not a compatible nice
four-variable action. It shows why the stationary ideal and omitted-
direction restrictions alone do not exclude the proper ideal. The
all-degree and all-polynomial argument remains the separate written
proof; the method tests only its two specified degrees and identities.
The same method checks the two formal second-derivative identities
that exclude a nonzero nice derivation killing this exact pair:
first \(E^2y=-6p^m z(Ez)^2\), and then the displayed factored
\(E^2x\) after \(Ez=0\). The final factor has coefficient \(-2\)
on \(q\). Inert velocity symbols express the stipulated conditions
\(Ep=Eq=0\) and \(E^2z=E^2w=0\); they do not supply a new
polynomial action. The general nonrealization proof remains written.

## 6. Actual execution and verification boundary

The author fully read the checker through EOF. Its initial four-method
version passed in 0.203 seconds, exit zero, before the nonreduced example
was strengthened to the nonconstant-unit, nonzero-fourth-row version.
The strengthened four-method file passed in 0.199 seconds, exit zero,
with complete merged stdout/stderr retained in tool chunk `da956d`.
Root then requested the distinct fifth method in Section 5. It passed
in 0.366 seconds, exit zero, with complete merged stdout/stderr retained
in tool chunk `d43e07`. The final version additionally checks the two
nonrealization identities inside that same fifth method. All five
methods passed in 0.462 seconds, exit zero, with complete output in
tool chunk `748307`. No version had a failure. The earlier runs and
version history are not extra methods.

The final five-method script SHA-256 is
`670f65c6fabf2594d7f8878260595480ea4203d77cabe5541b3b1fd04fe81967`.
The SHA-256 of its exact five-method output bytes, before the wrapper's
hash report, is
`c3a84d0d6e4c1bf1b17496bfa946756911d81c6d2034dac03ee34d57331fb152`.
The wrapper printed the complete output and calculated those hashes;
it wrote no verification file. Root owns any canonical targeted capture
or runner. No full regression, frozen-pass change, primary-source
proof verification, finite classification, novelty claim, human expert
review or formal proof certificate is reported here.
