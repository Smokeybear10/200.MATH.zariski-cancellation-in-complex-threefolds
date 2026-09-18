# Second hostile audit of cubic stable-coordinate descent

No fatal gap was found in the intended theorem

\[
 F\in\mathbb C[x_1,x_2,x_3,x_4],\quad\deg F\le3,\quad
 F\text{ stably a coordinate}
 \quad\Longrightarrow\quad F\text{ a coordinate}.
\]

There is one concrete notation issue to repair before circulating the
statement: the singular locus of a possibly nonreduced leading form must
mean its **Jacobian singular locus**, not the singular locus of its reduced
support. The proof already uses the former meaning. The distinction is
essential, and a coordinate supplies an immediate counterexample to the
other interpretation.

This audit reconstructed the delicate implications from the component
arguments and checked the cited inputs against primary texts. It did not
infer correctness from the existing audit conclusions or symbolic test
counts. It remains another model audit, not human peer review or a proof
assistant certificate.

## 1. A real ambiguity: repeated leading factors

Take

\[
 F=x+y^3\in\mathbb C[x,y,z,u].
\]

It is a coordinate, with inverse substitution \(x=F-y^3\). Its leading
form is \(f_3=y^3\). The reduced projective support \(V(y)\subset\mathbb
P^3\) is a smooth plane, so its singular locus is empty. Consequently,
the assertion

\[
 \operatorname{Sing}\bigl(V(f_3)_{\mathrm{red}}\bigr)\cap V(f_2)
 \ne\varnothing
\]

would be false, even for a coordinate.

The correct, unambiguous formulation is

\[
 J(f_3):=V\!\left(
 \frac{\partial f_3}{\partial x_1},\ldots,
 \frac{\partial f_3}{\partial x_4}\right)\subset\mathbb P^3,
 \qquad J(f_3)\cap V(f_2)\ne\varnothing.
\]

Euler's homogeneous identity puts \(J(f_3)\) inside \(V(f_3)\).
For \(f_3=y^3\), it is the full plane \(y=0\), so the example is
handled correctly. This is also the singular locus of the hypersurface
with its defining scheme structure.

The existing infinity proof explicitly computes these partial derivatives
and explicitly treats repeated factors. Thus this is a precision repair
to the statement, not a failure of the intended argument. Use the same
convention in the higher-degree extension.

## 2. Reconstructing the infinity contradiction

Stability gives, for every \(\lambda\),
\(X_\lambda\times\mathbb A^N\simeq\mathbb A^{N+3}\).
Smoothness descends from the product, and compact-support Künneth gives
\(\chi_c(X_\lambda)=1\). No cancellation of the affine-space factor is
used.

Assume \(J(f_3)\cap V(f_2)=\varnothing\). A positive-dimensional
projective component of \(J(f_3)\) meets every positive-degree hypersurface,
so \(J(f_3)\) is finite. The case \(f_2=0\) only makes that implication
stronger. A repeated factor of \(f_3\) puts a surface inside \(J(f_3)\);
two distinct factors put their intersection curve inside it. Hence the
finite-locus case is reduced and irreducible before any isolated-singularity
formula is invoked.

At infinity the gradient of the homogenized fiber equation is exactly
\((\nabla f_3,f_2)\). It is nowhere zero under the contrary assumption.
Together with affine smoothness, this makes its closure \(Y_\lambda\) a
smooth cubic threefold, with boundary \(S=V(f_3)\).

Independently expanding the Chern expressions gives

\[
 \chi(Y_\lambda)=3(10-30+45-27)=-6,\qquad
 \chi(S_{\mathrm{sm}})=3(6-12+9)=9.
\]

An isolated complex surface singularity has Milnor fiber Euler
characteristic \(1+\mu\), so smoothing increases Euler characteristic by
\(\mu\). Thus \(\chi(S)=9-\sum\mu_p\), with this sign confirmed by
[Maxim–Păunescu–Tibăr, Remark 3.2, equation (3.11)](https://www.numdam.org/item/10.5802/aif.3486.pdf).

[Huh's introduction](https://arxiv.org/pdf/1210.2690) explicitly gives
\(\deg\operatorname{grad}(f_3)=8-\sum\mu_p\).
Only nonnegativity is used; no dominance assumption or cone-excluding
inequality is imported. Therefore

\[
 \chi_c(X_\lambda)=-6-(9-\sum\mu_p)
 \le-15+8=-7,
\]

contradicting one. The empty singular locus gives \(-15\), and a cone
with polar degree zero still gives at most \(-7\). Neither evades the
contradiction.

At a point \([1:0:0:0]\) in the asserted intersection, the four cubic
derivatives remove the \(u^3\) and all \(u^2v_i\) coefficients.
The extra equation \(f_2(p)=0\) removes the remaining \(u^2\) term.
No lower-degree term can contain a higher power of \(u\). This really gives
\(F=P(v)u+H(v)\), with \(\deg P\le2\).

## 3. Repeated coefficients do not create an omitted quadratic case

For a ternary polynomial of degree at most two, a repeated nonconstant
irreducible factor must be an affine linear factor squared, up to a scalar.
There is no quadratic analogue of the coefficient \(xy^2\). A repeated
plane coefficient therefore lies in the rank-one, univariate case.

The affine normalization is exhaustive. If the linear part is nonzero on
the radical of the quadratic matrix, the coefficient is itself a
coordinate. Otherwise translation removes its linear part, and its rank
is zero, one, two or three. Over \(\mathbb C\), rank two reduces to
\(xy\) or \(xy-1\), and rank three to a smooth affine quadric or a quadric
cone. Polynomial normalization of a coordinate coefficient may raise the
degree of \(H\), so the use of the arbitrary-degree coefficient theorem
at this step is necessary and legitimate.

For \(p(x)u+H(x,y,z)\), write \(d\) for the number of distinct roots of
\(p\). Reduced closed strata are the correct input for ordinary topology,
even when scheme-theoretic root fibers have multiplicity. The open fiber
is \((\mathbb A^1\setminus\{a_1,\ldots,a_d\})\times\mathbb A^2\).
The two exact-sequence consequences are separately

\[
 \bigoplus_i H_c^1(C_i)=0,\qquad
 \bigoplus_i H_c^2(C_i)\simeq\mathbb Q^d.
\]

No root specialization may be constant, because an omitted root plane
would make \(x-a_i\) a nonconstant unit on a stable fiber. At a common
regular value all \(d\) curves are nonempty and smooth. The second identity
forces exactly one connected component per root; the first then forces
genus zero and exactly one puncture. Each is an embedded affine line.
Regularity also prevents its defining polynomial from being a hidden power.

The crucial multiplicity step is external and correctly scoped:
[Maubach, Theorem 4.5](https://www.math.ru.nl/~maubach/Papers/The_Commuting_Dervations.pdf)
explicitly writes \(p(X)=\prod(X-\alpha_i)^{e_i}\) and permits arbitrary
positive \(e_i\). Its sufficiency is unconditional; it is not the
conditional theorem 4.1. The exact rootwise statement is independently
restated in [Dutta–Lahiri, Theorem 1.1](https://arxiv.org/html/1908.03549).
Thus the proof does not infer a multiplicity-sensitive coordinate conclusion
from topology alone.

## 4. Checks on the two crossing branches

For \(P=xy\), the open fiber is \((\mathbb C^*)^2\times\mathbb A^1\),
with compact-support ranks \((1,2,1)\) in degrees \((4,5,6)\). These
give \(H_c^1(C)=\mathbb Z\) and \(H_c^2(C)=\mathbb Z^2\) for the closed
curve in a stable fiber.

If \(h(z)=H(0,0,z)\) is nonconstant, a generic value gives two nonempty
smooth plane curves meeting at \(d=\deg h\) distinct points. The top group
forces each plane curve to be connected. Closed-cover Mayer–Vietoris gives

\[
 0\longrightarrow\mathbb Z^d\longrightarrow\mathbb Z
 \longrightarrow H_c^1(C_x)\oplus H_c^1(C_y)
 \longrightarrow0.
\]

The \(\mathbb Z^d\) term is correct, rather than \(\mathbb Z^{d-1}\):
the degree-zero compact-support groups of the noncompact pieces vanish.
Thus \(d=1\) and both pieces are affine lines. The line-rectification
input is stated in [Nguyen Van Chau, Section 2](https://math.ac.vn/uploads/files/0202197.pdf).

The relative-coordinate lemma also survives scrutiny. In coordinates
\((q,V)\), the line \(r=0\) is the graph \(V=R(q)\) because its
restriction of \(q\) is linear and invertible. Both \(r\) and
\(V-R(q)\) are irreducible defining equations of that same line; they
are scalar associates. Hence \((r,q)\) is a coordinate pair and
\(q=az+Q(r)\). This does not assume the relative-coordinate conclusion
being proved.

If \(h=b\) is constant, for every \(\lambda\ne b\) both plane curves
are nonempty, smooth and disjoint. Their compact-support ranks force one
to be \(\mathbb A^1\) and the other \(\mathbb C^*\). Infinitely many
affine-line fibers in the same plane force its base coordinate to be
constant on each such line, then force the corresponding plane polynomial
to be \(ay+b\). This prevents an unsupported fixed-branch assumption.

For the other restriction \(g\), the argument across the missing value
\(b\) is essential and is present. If \(g_z\) vanished along a curve
in \(x\ne0\), that curve lies in \(g=b\). Since \(g\) is a submersion,
its restriction forces \(dx=0\), so the curve is a whole vertical line.
Every other \(\mathbb C^*\) fiber maps surjectively to \(\mathbb C^*\)
under its nonconstant unit \(x\), contradicting that vertical line.
This justifies \(g_z=cx^k\), including the exceptional level, and thus the
explicit unimodular-pair completion.

## 5. The remaining coefficient exclusions

For \(xy-1\), critical-point-freeness of \(F\) implies that \(H|_D\)
is a submersion. Every restricted curve has compact-support ranks one in
degrees one and two, so it is \(\mathbb C^*\). The unit \(x\) is
nonconstant: a one-dimensional closed curve inside a vertical affine line
would equal that line. It therefore has form \(ct^n\), \(n\ne0\), whose
derivative never vanishes. This forces \(H_z|_D\) to be a Laurent unit.
The positive coordinate map is a determinant-one matrix, so it is not
relying on the Jacobian conjecture.

For a smooth rank-three quadric, its compactification is
\(\mathbb P^1\times\mathbb P^1\) with a \((1,1)\) conic removed.
Restriction on \(H^2\) is \((a,b)\mapsto a+b\), so
\(H_c^2(D;\mathbb Q)=\mathbb Q\). The open complement shifts this to
\(H_c^3(U;\mathbb Q)\). The generic closed stratum is a smooth affine
curve times \(\mathbb A^1\), or empty, and has \(H_c^2=0\).
Consequently this nonzero class injects into \(H_c^3(X_\lambda)\).

For the quadric cone, the finite quotient presentation
\(D\simeq\mathbb C^2/\{\pm1\}\) gives the open cone on
\(\mathbb{RP}^3\). The suspension and universal-coefficient shifts put
the torsion at \(H_c^3(D;\mathbb Z)=\mathbb Z/2\), hence
\(H_c^4(U;\mathbb Z)=\mathbb Z/2\). Choosing a regular level away from
the vertex is valid. Both adjacent groups
\(H_c^3(X_\lambda)\) and \(H_c^4(X_\lambda)\) vanish under stability,
so the sequence requires an **isomorphism**
\(H_c^1(C_\lambda;\mathbb Z)\simeq\mathbb Z/2\).
A smooth affine curve has free integral first homology, so this is
impossible. A mere surjection would not suffice, but the proof does not
make that mistake.

Finally, the zero coefficient invokes three-variable stable descent.
[Shpilrain–Yu's proof of Proposition 1.1(c)](https://arxiv.org/html/math/0110324)
explicitly allows a coordinate in \(\mathbb C[x_1,\ldots,x_N]\) for
arbitrary \(N>3\), so this dependency does not restrict the number of
stabilizing variables.

## 6. Audit verdict and changes needed

The intended proof chain is intact in this pass. The concrete change needed
is to define the projective Jacobian locus explicitly wherever the leading
form may be nonreduced. The present text already establishes the needed
reducedness before applying Milnor formulas, and already isolates the
multiplicity-sensitive algebra in Maubach's theorem.

The reviewed chain includes
[the main statement](../deep-pass-07.md),
[the infinity argument](cubic-infinity-audit.md),
[the quadratic classification](quadratic-coefficient-theorem.md),
and the linked univariate, hyperbolic, two crossing, smooth-quadric and
quadric-cone arguments. Original files were left unchanged. No new finite
test suite was run: finite coefficient samples would not validate the
universal geometric steps examined here.

This finding supports retaining the degree-at-most-three result as a working
theorem with its proof available for checking. It does not establish novelty,
settle unrestricted cancellation, or justify treating a stable fiber as
\(\mathbb A^3\) before cancellation has been proved.
