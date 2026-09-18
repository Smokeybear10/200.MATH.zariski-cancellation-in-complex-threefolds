# Full-chain audit of the degree-three stable-coordinate argument

This audit reconstructs [deep-pass-07](../deep-pass-07.md), the
[quadratic-coefficient theorem](quadratic-coefficient-theorem.md), and their
linked branches over \(\mathbb C\). No counterexample, omitted coefficient
case, circular dependency, or substantive mathematical gap was found.
The conclusion being audited is only

\[
 F\in\mathbb C^{[4]},\quad \deg F\leq3,\quad F\text{ stably a coordinate}
 \quad\Longrightarrow\quad F\text{ a coordinate}.
\]

This is another model reconstruction, not human expert review, formal
verification, or evidence of novelty. It does not prove unrestricted
cancellation or a degree bound for arbitrary slices.

## 1. Dependency order

The argument can be read without circularity in this order.

1. **Consequences of stabilization.** A coordinate after adjoining \(N\)
   variables has, for every \(\lambda\),
   \(X_\lambda\times\mathbb A^N\simeq\mathbb A^{N+3}\).
   Smoothness descends, units are constant, and compact-support Künneth
   gives \(H_c^i(X_\lambda;\mathbb Z)=0\) except for \(\mathbb Z\) in
   degree six. There is no Tor contribution from the affine-space factor.

2. **Independent cubic reduction.** The
   [infinity argument](cubic-infinity-audit.md) uses only critical-point
   freeness and \(\chi_c(X_\lambda)=1\). It produces a linear change with
   \(F=uP(v)+H(v)\), \(\deg P\leq2\). It does not use the conclusion of
   any coefficient branch.

3. **Quadratic-coefficient descent.** Complete the coefficient cases
   listed below, allowing arbitrary degree for \(H\). This flexibility
   matters when a polynomial base change raises that degree.

4. **Assembly and the kernel.** Apply step 3 to step 2. Lower-degree
   critical-point-free polynomials are handled directly. For an LND slice
   \(s\), the slice theorem gives \(B=K[s]\); hence \(s\) is one-stable
   and, once it is a coordinate, \(K\simeq B/(s)\simeq\mathbb C^{[3]}\).

## 2. Exhaustiveness of the quadratic cases

Write \(P(v)=v^TAv+b^Tv+c\), \(A=A^T\). If \(b\) is nonzero on
\(\ker A\), a radical direction makes \(P=ar+Q(s,t)\), \(a\ne0\).
Thus \(P\) itself is a base coordinate. Otherwise
\(b\in\operatorname{im}A=(\ker A)^\perp\), so translation removes the
linear part and leaves a rank-\(r\) quadratic plus a centered constant.
Over \(\mathbb C\), this gives precisely:

| Case | Independent input |
|---|---|
| \(P\) constant and nonzero | Solve for \(u\) |
| \(P=0\) | Known stable-coordinate descent in three variables |
| \(P\) a base coordinate, or rank one | [Univariate coefficient proof](multiple-root-linear-pass.md) and Maubach |
| Rank two, nonzero centered constant | [\(xy-1\) proof](hyperbolic-coefficient-pass.md) |
| Rank two, zero centered constant | [Nonconstant-axis](crossing-nonconstant-pass.md) or [constant-axis](crossing-coefficient-pass.md) crossing proof |
| Rank three, nonzero centered constant | [Smooth-quadric obstruction](quadratic-coefficient-obstruction.md) |
| Rank three, zero centered constant | [Cone obstruction](quadric-cone-obstruction.md) |

Nonzero scalar factors in \(P\) are absorbed into \(u\). In particular,
the radical-linear case is not lost by prematurely completing the square.

The \(P=0\) step really allows any finite number of stabilizing variables:
[Shpilrain–Yu, Proposition 1.1(c) and its proof](https://arxiv.org/html/math/0110324)
explicitly starts with a three-variable polynomial that is a coordinate
in an \(N\)-variable ring for some \(N>3\). Thus this step does not
improperly iterate one-variable cancellation. For the univariate positive
step, [Maubach, Theorem 4.5](https://www.math.ru.nl/~maubach/Papers/The_Commuting_Dervations.pdf)
explicitly includes arbitrary multiplicities of the roots of \(p(x)\).

## 3. Checks on the vulnerable branch arguments

**Plane fibers and powers.** The univariate and nonconstant-axis arguments
choose generic smooth plane fibers, then show they are connected affine
lines. Choose the level to be a regular value of the defining polynomial.
Its fiber equation \(q-\lambda\) is then reduced. Smoothness and
connectedness make the curve irreducible, so \(q-\lambda\) itself is
irreducible up to a nonzero scalar. Plane-line rectification therefore
makes this polynomial a coordinate, not merely its radical. This is the
precise hypothesis in the Abhyankar–Moh–Suzuki consequence recorded in
[Chau, Section 2](https://math.ac.vn/uploads/files/0202197.pdf).

This is a recommended explicit sentence at the rectification steps, not
a missing hypothesis: their existing generic smooth-fiber choices already
provide regular levels. Merely knowing that the reduced zero set of one
arbitrary level is an affine line would not suffice.

**Relative coordinates.** If \(q(r,z)\) is a plane coordinate and
\(q(0,z)=az+b\), a companion \(V\) maps the line \(r=0\) to a graph
\(V=R(q)\). Both \(r\) and \(V-R(q)\) are irreducible and define that
same curve, so they are associates. Hence \((r,q)\) is a coordinate pair.
An automorphism of \(\mathbb C[r][z]\) fixing \(r\) sends \(z\) to
\(az+Q(r)\). This validates the extra relative conclusion in the
nonconstant-axis crossing branch.

**Constant-axis Laurent step.** The constant-axis proof obtains its curve
types for every \(\lambda\ne b\), not just generic values. Infinitely
many affine-line strata force one plane restriction to be \(ay+b\).
On the other plane's punctured surface, every remaining fiber is
\(\mathbb C^*\), and the unit \(x\) is nonconstant, hence a surjective
étale monomial on that curve. Thus \(h_z\) has no zeros outside \(h=b\).
Any divisor component of its zeros would lie in \(h=b\); submersivity
then forces \(dx=0\) on that component, making it an entire vertical
line. The other fibers would miss this \(x\)-value, contradicting the
surjectivity just proved. This establishes that \(h_z\) is a Laurent
unit. No unsupported implication from generic Euler characteristic is
used here.

**Integral cone obstruction.** For \(D=V(xy-z^2)\), the link is
\(\mathbb{RP}^3\), giving \(H_c^3(D;\mathbb Z)=\mathbb Z/2\) and
\(H_c^4(\mathbb A^3\setminus D;\mathbb Z)=\mathbb Z/2\).
Choose a generic restricted curve away from the vertex; if the
restriction of \(H\) is constant, choose a different value and use the
empty curve. The stable-fiber exact sequence has both adjacent groups
zero and would identify this torsion group with the free group
\(H_c^1(C;\mathbb Z)\). A mere surjection from a free group to torsion
would not suffice, but that is not the argument in the appendix.

## 4. Infinity checks

If \(\operatorname{Sing}V(f_3)\cap V(f_2)\) were empty, the singular
locus would be finite, possibly empty. Repeated factors or two distinct
surface components would instead create a positive-dimensional singular
locus, so the isolated-singularity formulas apply to a reduced surface.
The infinity gradient is exactly \((\nabla f_3,f_2)\), independently of
\(\lambda\). Together with affine critical-point freeness, this really
makes every projective closure \(Y_\lambda\) smooth under the contrary
assumption.

The dimensions and signs are consistent:

\[
 \chi(Y_\lambda)=-6,\qquad
 \chi(V(f_3))=9-\sum\mu_p,\qquad
 \sum\mu_p\leq8,
\]

so \(\chi_c(X_\lambda)=-15+\sum\mu_p\leq-7\). The bound uses the
polar-degree identity with degree zero allowed, not a theorem excluding
cones. The [infinity appendix](cubic-infinity-audit.md) records the exact
Maxim–Păunescu–Tibăr and Huh source locations. The resulting point removes
both the leading \(u^2v\) terms and the lower \(u^2\) term; neither
condition alone supplies the desired linear presentation.

## 5. Verification record and limits

The eight test methods in [verify_quadratic_coefficients.py](../verify_quadratic_coefficients.py)
passed in this audit, including both compositions of the positive
coordinate maps. This run does not independently recertify the earlier
152 methods, and finite identities do not prove the topological or
universal statements.

No substantive repair is required by this audit. The only recommended
clarification is the reduced regular-level sentence before plane-line
rectification. All arguments here are restricted to \(\mathbb C\);
arbitrary-field descent is neither used nor supplied. No extension to
degree four or to unrestricted cancellation follows from this report.

## Additional independent reconstruction

A second model read the assembled cubic proof and the coefficient
appendices independently, and obtained a further hostile review of
the hyperbolic and constant-axis crossing branches. No substantive
gap was found in the normalization, compact-support shifts,
Laurent-unit argument, or inverse formulas. The main agent also
read the complete appendices and directly checked the cited
Euler and polar-degree formulas.

The regular-level clarification is now included explicitly in the
nonconstant-axis and univariate coefficient proofs. An optional
expository refinement is to name the principal ideal theorem when
passing from a nonunit \(h_z\) to a curve component of its zero set.
That argument already uses a nonzero principal ideal in a smooth
surface, so this is not a missing hypothesis.

These additional readings remain model-based checks. They do not
establish originality or replace independent human reconstruction.
