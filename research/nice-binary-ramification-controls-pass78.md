# Finite exact Euler, Wronskian and ramification controls

The standalone [checker](nice_binary_ramification_checks_pass78.py) has
four unittest methods. It imports only `unittest` and SymPy and uses
exact polynomial or rational-function arithmetic. No solver/research
module, random sampling, external source access or numerical
approximation is used.

## 1. A formal two-by-two Euler matrix

The first mathematical control takes independent formal symbols
\(p,q,a,b,\gamma\), sets \(\omega=pb-qa\), and checks
\(C=-(\gamma/\omega)(a,b)^t(b,-a)\). It verifies the square,
trace and determinant are zero, \(C(a,b)^t=0\), and
\(C(p,q)^t=-\gamma(a,b)^t\). It computes the exact matrix in
the basis \(((p,q)^t,(a,b)^t)\) and checks the sign by observing
that the opposite sign fails the required radial identity.

The matrix has rank one over this formal fraction field, not rank two.
Its two-dimensional size comes from the rank-two velocity reduction.
No formal symbol is declared to be an actual polynomial derivative,
and no four-variable action is fabricated from this matrix. The
actual-factorization hypotheses are proved in the
[Euler note](binary-euler-reduction-pass78.md), not by this method.

## 2. The actual retained conic action

The conic method uses the original polynomial action with
\(a=xz-y^2+w\) and velocity
\(P=(1,a,a^2,-a^2x+2ay-z)\). It checks both adapted inverse
orders, that the transported action is \(\partial_x\), original
niceness, goodness of the actual \(\partial_w\), and the exact
Jacobian/bracket identities.

The computed determinant of the columns
\((P,e_4,Q(x),[T,Q](x))\) is two, with the same positive sign
as its transverse three-by-three determinant. The method separately
computes the Wronskian of \((1,t,t^2)\), the nonparallel second
iterate \(Q^2(x)=(0,0,0,2)^t\), and the identity
\(J[T,Q](x)=-Q^2(x)\).
It also constructs the binary normal \(N=h_p\times h_q\) and
checks that \(c=N(1,a)\cdot(x,y,z)=-2P_4\) is killed by both
\(E\) and \(Q\) in this actual example.

This is an actual already recognized action, and its binary parameters
\(p=1,q=a\) are dependent with unit ideal. It is not an example of
the independent-parameter Euler construction or a proper parameter
fiber. The third iterate vanishes for this action, but neither the
method nor the [Wronskian theorem](binary-wronskian-derived-rank-pass78.md)
asserts that bound for every action in the remaining branch.

## 3. An actual polynomial-plane pole and its whole socle

The ramification method takes the weaker plane data
\(p=u,q=v^2+uv,P_4=1+v\). It computes \(\Delta=u+2v\), the
extended parameter partials from the inverse Jacobian, their action on
\(p,q\), their commutator on \(u,v\), and the exact chain rule for
the four functions \((p^2,pq,q^2,1+v)\). This list is not asserted
to be a nice four-variable velocity.

For the two specified positive binary degrees \(e=2,3\), the method
checks
\(\gamma=e(1+v)-v^2/(u+2v)\). Its cleared numerator has remainder
\(-v^2\) modulo the prime \((u+2v)\), proving a genuine pole in
this example. Reduction modulo \((p,q)=(u,v^2)\) gives the nonzero
class \(2e\bar v\). Multiplication by that class is computed on
the basis \((1,\bar v)\); its image and kernel are the line
\(\mathbb C\bar v\). The fourth velocity is a unit on this
nonreduced fiber, as checked using the inverse \(1-\bar v\).

These identities illustrate the whole-scheme distinction in the
[ramification and socle note](binary-ramification-socle-pass78.md).
They do not prove the general Jacobian-socle theorem, identify an
unknown intrinsic kernel with this plane, or realize the original
action hypotheses. No division by the nilpotent socle class is made.

## 4. Selected binary Jacobian minors

For the three explicit homogeneous binary triples of degrees two,
three and four listed in the code, the final method forms all three
two-by-two Jacobian minors and checks their coefficient matrix has
rank three. It extracts and inverts a nonzero constant three-by-three
minor. The inverse identity is also checked on a formal vector
\(\alpha+\epsilon\beta\); as a polynomial identity it remains
valid after imposing \(\epsilon^2=0\). Thus the finite control
does not accidentally replace the coefficient algebra by a field.
It additionally extracts degree \(2e-2\) from a formal combination
whose coefficients are \(\alpha_i+\epsilon\beta_i\), while
retaining higher-degree terms and a term that vanishes only modulo
\(\epsilon^2\). The selected constant minor recovers the entire
coefficient vector, including its nilpotent part. The normal-vector
entries are checked to be the same three minors with their exact
signs and order. This models the coefficient step, not the theorem
that an actual proper binary ideal is impossible.

For each triple the full two-by-three formal coefficient matrix is
retained in an exact Cauchy--Binet determinant calculation. A dependent
triple supplies the expected failure of the three-minor independence.
Only these specified triples are tested. The all-degree independence,
nonreduced associated-graded and ambient-socle arguments in the
[regular-derivative exclusion](binary-regular-derivative-exclusion-pass78.md)
remain written proofs.

## 5. Execution and provenance

The author read the complete checker through EOF and checked whitespace.
The first four-method version passed in 0.247 seconds, exit zero. The
socle multiplication matrix was then changed from its explicitly checked
formula to a direct extraction from reduced products; the same four
methods passed in 0.236 seconds. Finally the Euler method was renamed
to say "two-by-two" rather than "rank two", avoiding an ambiguity
about the rank-one matrix C. That four-method file passed in
0.252 seconds, exit zero, with complete output in tool chunk `bb2837`.
At Root's request, the normal-invariant and nonreduced degree-extraction
checks were then added inside the same four methods. The final file
passed all four methods in 0.284 seconds, exit zero, with complete
output in tool chunk `e3c6f0`.
There were no failed runs. Version checks and repeats are not extra
methods.

The final checker SHA-256 is
`472b2d432e92cb48fca192dff7c64ecacb3f400be13c5e6e436f6507fccc7809`.
General independently read the complete final checker and ran the same
four methods in 0.274 seconds, exit zero, with complete output in tool
chunk `ba8841` and the same checker hash. Root independently read the
final mathematical controls and separately integrated them into the
[targeted capture](verification-pass78-working.json): its four-method
run took 0.280 seconds in unittest and 0.602369 seconds of recorded
monotonic elapsed time. These are separate runs of the same four
methods, not additional methods or a fresh full regression.

The controls author did not create a runner, verification/capture file,
full regression or shared metadata; that targeted integration was
Root's separate work. Frozen files through pass77 were not edited. These controls
are not universal proofs, new classification results, historical novelty
claims, primary-source verification, human expert review or a formal
proof certificate.
