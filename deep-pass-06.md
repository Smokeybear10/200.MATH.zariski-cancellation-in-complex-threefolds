# Polynomial slices, quadratic pencils, and the remaining cancellation gap

Continuation: [deep-pass-07.md](deep-pass-07.md) closes the remaining
cubic normal-form gap described in Section 7 below. This report preserves
the preceding pass's proof sequence; the unrestricted cancellation gap
remains.

Two broad polynomial families now have complete slice-to-coordinate arguments.
Neither argument proves that an arbitrary slice polynomial in four variables
belongs to those families. The complex threefold cancellation conjecture
therefore remains unresolved in this investigation.

The first family is

\[
 F=p(x)y+g(x,z,w),\qquad 0\ne p\in\mathbb C[x],
\]

with unrestricted degrees and root multiplicities. The second is

\[
 F(x,v)=v^T(A_0+xA_1)v+b(x)^Tv+c(x),\qquad v=(y,z,w)^T,
\]

with symmetric constant matrices \(A_0,A_1\) and arbitrary polynomial \(b,c\).
In either family, being a slice of a locally nilpotent derivation, being a
stable coordinate, and being an ordinary coordinate are equivalent.

There is substantial overlap with established results. In particular, the
rootwise coordinate criterion for the first family is Maubach's theorem,
not a new discovery. The contribution of the present notes is an explicit
reconstruction, a compact-cohomology route from stability to the root
conditions, a quadratic-pencil argument, and exact checks of the displayed
coordinate formulas. No originality or human expert verification is claimed.

## 1. Relation to the original question

The working target is

\[
 X\times_{\mathbb C}\mathbb A^1\simeq\mathbb A^4
 \quad\Longrightarrow\quad X\simeq\mathbb A^3.
\]

The dimension and field remain an interpretation of the professor's email,
not a clarification received from him. Its literal conclusion
\(X\simeq\mathbb A^1\) has the previously documented dimension mismatch.
The results here concern the corrected complex threefold problem.

Writing the coordinate ring of the cylinder as \(K[s]\), differentiation
with respect to \(s\) gives a locally nilpotent derivation with slice \(s\).
Conversely, if \(D\) is locally nilpotent on \(\mathbb C^{[4]}\) and \(D(s)=1\),
the slice theorem gives \(\mathbb C^{[4]}=(\ker D)[s]\). Thus it would suffice
to prove that every such \(s\) is a polynomial coordinate.

Every slice is a stable coordinate: in

\[
 K[s,t]=K[t][s],
\]

the coefficient ring \(K[t]\) is isomorphic to the given polynomial ring
\(K[s]\). This does not make \(s\) a coordinate before stabilization.
The distinction is precisely why restricted coordinate theorems cannot be
silently upgraded to the full cancellation theorem.[^1]

The new results classify possible **slice polynomials**. Excluding a displayed
polynomial from being a slice does not exclude an abstract cylinder
isomorphism for its zero fiber. Such an isomorphism could produce a different
polynomial presentation, with different other fibers.

## 2. Univariate coefficients and rootwise plane coordinates

For \(F=p(x)y+g(x,z,w)\), let \(D\) be the distinct roots of \(p\). Then

\[
 \boxed{
 F\text{ is a slice}
 \iff F\text{ is stably a coordinate}
 \iff F\text{ is a coordinate}
 \iff
 g(a,z,w)\text{ is a plane coordinate for every }a\in D.}
\]

When \(p\) is constant and nonzero, the root condition is empty and one
eliminates \(y\) directly. For nonconstant \(p\), Maubach's unconditional
Theorem 4.5 supplies sufficiency and Corollary 4.2 records the existing
coordinate classification. Dutta and Lahiri restate the relevant sufficiency
with its precise hypotheses.[^2]

### Why stability forces all root conditions

For a generic \(\lambda\), write \(X_\lambda=\{F=\lambda\}\) and
\(C_a=\{g(a,z,w)=\lambda\}\). The open part with \(p(x)\ne0\) is

\[
 U=(\mathbb A^1\setminus D)\times\mathbb A^2,
\]

and the closed complement is

\[
 Z=\coprod_{a\in D} C_a\times\mathbb A^1.
\]

Stability makes \(X_\lambda\) smooth, contractible, and devoid of nonconstant
algebraic units. The units condition first rules out constant \(g(a,z,w)\):
otherwise \(x-a\) would be a nonconstant unit on a suitable fiber.
Thus all the generic plane curves \(C_a\) are nonempty.

If \(d=|D|\), compactly supported rational cohomology gives

\[
 H_c^i(X_\lambda)=0\ (i\ne6),\quad
 H_c^5(U)=\mathbb Q^d,\quad H_c^6(U)=\mathbb Q.
\]

The closed-open exact sequence then yields the two independent constraints

\[
 \bigoplus_a H_c^1(C_a)=0,\qquad
 \bigoplus_a H_c^2(C_a)\simeq\mathbb Q^d.
\]

The second says that the \(d\) nonempty curves have exactly \(d\) connected
components in total, hence one each. The first says that each component has
genus zero and one puncture. Each \(C_a\) is therefore an embedded affine
line. The plane embedding theorem rectifies its defining polynomial, giving
the required coordinate condition.[^3]

Using only Euler characteristic would lose information: positive component
counts and negative genus or puncture contributions could offset each other.
The two cohomology groups prevent that numerical cancellation. The full
proof, with every degree shift and exact-sequence segment, is in
[the multiple-root appendix](research/multiple-root-linear-pass.md).

### An explicit inverse for a repeated single root

For \(p=x^m\), a plane coordinate change reduces the positive case to

\[
 F=x^my+h(x,z,w),\qquad h=z+xQ(x,z,w).
\]

Construct a finite inverse \(R(x,Z,w)\) of \(h\) modulo \(x^m\). It satisfies

\[
 h(x,R(x,Z,w),w)\equiv Z\pmod{x^m},\qquad
 R(x,h(x,z,w),w)\equiv z\pmod{x^m}.
\]

Then \(x,w,Z=F\), and

\[
 Y=\frac{z-R(x,F,w)}{x^m}
\]

are polynomial coordinates. Their inverse is

\[
 z=R(x,Z,w)+x^mY,\qquad
 y=\frac{Z-h(x,z,w)}{x^m}.
\]

Both quotients are polynomials by the congruences. This is an actual finite
construction, not an infinite formal series being mistaken for a polynomial.

For \(F=x^2y+g\) with \(\deg g\le3\), there is an especially small exact gate:
solve for constants \(\alpha,\beta\) in

\[
 \alpha\,g(0,z,w)_z+\beta\,g(0,z,w)_w=1.
\]

Solvability is equivalent to the slice condition in this cubic family. The
[cubic appendix](research/cubic-linear-variable-pass.md) proves that
low-degree statement directly, including the obstruction to an embedded
line with parameter degrees \((3,2)\). This constant-direction test is not
valid for plane coordinates of arbitrary degree.

## 3. Full-rank affine quadratic pencils

Suppose

\[
 F=v^TA(x)v+b(x)^Tv+c(x),\quad A=A_0+xA_1,\quad
 \det A\not\equiv0.
\]

There is an explicit criterion:

\[
 \boxed{
 F\text{ is a slice or stable coordinate}
 \iff \det A\in\mathbb C^*
       \text{ and }F\text{ has no critical point}.}
\]

### Excluding a nonconstant determinant

Let \(d\ge1\) be the number of distinct determinant roots and put

\[
 h=c-\tfrac14b^TA^{-1}b\in\mathbb C(x).
\]

Critical-point-freeness forces \(h'\ne0\) off those roots, so \(h\) is a
nonconstant rational function of degree \(N\ge1\).
Over the invertible-matrix locus, a generic fiber has Euler characteristic

\[
 2(1-d)-N.
\]

This follows by completing the square. A nonzero fiber of a nondegenerate
quadratic form in three complex variables has Euler characteristic two;
the cone at its center has Euler characteristic one. There are \(N\)
center values above a generic target value.

Each exceptional \(x\)-value contributes at most one. The only seemingly
larger possibility has matrix rank one and no linear term on its radical.
In that case critical-point-freeness forces \(A_1\) to vanish on a
two-dimensional kernel. Because \(A\) is an **affine** pencil, this would
make its determinant identically zero, contrary to the present hypothesis.
Thus

\[
 \chi_c(F^{-1}(\lambda))\le 2-d-N\le0.
\]

A stable coordinate has fiber Euler characteristic one, giving the
contradiction. The argument uses compact-support Euler integration, valid
for algebraic morphisms without a properness assumption.[^4]

### Constructing the positive coordinates

If \(\det A\) is a nonzero constant, put \(L=A_0^{-1}A_1\). Then \(L^3=0\), and

\[
 S=I+\frac{xL}{2}-\frac{x^2L^2}{8},\qquad
 S^{-1}=I-\frac{xL}{2}+\frac{3x^2L^2}{8}
\]

satisfy \(S^TA_0S=A\). The polynomial coordinate change

\[
 u=S\left(v+\tfrac12A^{-1}b\right)
\]

turns \(F\) into \(u^TA_0u+h(x)\). Having no critical point forces
\(h=ax+e\), \(a\ne0\). Consequently \((F,u)\) has the explicit inverse

\[
 x=\frac{F-u^TA_0u-e}{a},\qquad
 v=S^{-1}u-\tfrac12A^{-1}b.
\]

The complete matrix and topology proof is in
[the affine-pencil appendix](research/affine-quadratic-pencil-pass.md).

## 4. Singular quadratic matrices

When \(\det A\equiv0\), choose a nonzero polynomial kernel vector and divide
its entries by their greatest common divisor. Over the PID \(\mathbb C[x]\),
the resulting primitive vector extends to a unimodular matrix \(M(x)\).

In the coordinates \(v=M(x)(Y,Z,W)^T\), symmetry makes the first row and
column of \(M^TAM\) zero. Hence

\[
 F=p(x)Y+G(x,Z,W).
\]

If \(p\ne0\), Section 2 applies. If \(p=0\), \(F\) depends on only three
variables, where stable-coordinate descent is already a theorem.[^5]
This proves the singular-matrix case. It even allows an arbitrary polynomial
matrix \(A(x)\); only the full-rank argument requires \(A\) to be affine.

Combining Sections 3 and 4 gives the claimed slice-to-coordinate theorem
for **all** symmetric affine \(3\times3\) pencils. The kernel vector need not
be constant in \(x\). An exact control uses

\[
 A(x)=\begin{pmatrix}0&0&x\\0&0&-1\\x&-1&0\end{pmatrix},
 \qquad n(x)=(1,x,0)^T,
\]

whose kernels have no nonzero constant vector in common.

## 5. Examples and verification

The polynomial

\[
 F=x+2yz+xz^2+w^2
\]

is a positive full-rank example. Put \(U=y+xz/2\); then
\(F=x+2Uz+w^2\), with an immediate polynomial inverse.
No constant directional derivative of the original \(F\) equals one, so
this example is not settled by the earlier constant-direction shortcut.

The three smooth polynomials

\[
 x+y+xyz+w^2,\qquad xy^2+y+z^2+w^2,\qquad
 x+y^2+2xyz+w^2
\]

are negative examples. Their generic fiber Euler characteristics are
respectively \(0,0,-1\), while their zero fibers have Euler characteristic
one. They fail the stable-coordinate criterion despite having no critical
points.

There is a stronger warning outside affine pencils. For every \(m\ge2\),

\[
 F_m=x+x^muv+w^2
\]

has smooth fibers and \(\chi_c(F_m^{-1}(\lambda))=1\) for every \(\lambda\).
Nevertheless, for \(\lambda\ne0\),
\(H_c^3(F_m^{-1}(\lambda);\mathbb Q)=\mathbb Q\). Hence it is neither a
stable coordinate nor a slice. The
[complete cohomology calculation](research/nonaffine-quadratic-control.md)
uses the open quadric complement and two compact-support exact sequences.
It disproves an Euler-only shortcut, not cancellation of the abstract
zero fiber.

Two new independent checker files contain 26 test methods:

| Checker | Methods | Scope |
|---|---:|---|
| [verify_linear_variable.py](verify_linear_variable.py) | 9 | Truncated inverse, both compositions, cubic gates, scope rejection, slice formula |
| [verify_quadratic_pencils.py](verify_quadratic_pencils.py) | 17 | Nilpotent square root, completed square, two-way inverses, moving kernel, singular and nonsingular controls, nonaffine scope controls |

The nine preceding suites also pass, giving 152 passing methods in total.
These checks use exact arithmetic and do not import a solver. They verify
displayed algebraic identities, not universal topological statements.
The proofs remain human-readable mathematical arguments with separate model
audits, not Lean proofs or human peer review.

Run the new checks from the project directory:

~~~sh
/opt/anaconda3/bin/python verify_linear_variable.py
/opt/anaconda3/bin/python verify_quadratic_pencils.py
~~~

The complete earlier command list remains in [README.md](README.md).

## 6. A conditional theorem from two intrinsic symmetries

Let \(K[s]=\mathbb C^{[4]}\), and suppose two commuting locally nilpotent
derivations \(d_1,d_2\) of \(K\) are generically independent. Their common
invariant ring is \(\mathbb C[t]\). Every \(t-\lambda\) is prime in \(K\),
and each fiber is either a single free additive-group orbit
\(\mathbb A^2\), or a fiber on which the two fields are dependent everywhere.
Only finitely many fibers can be of the second kind.

If the fields are independent at every point, the second kind is absent.
The resulting \(\mathbb A^2\)-fibration over \(\mathbb C[t]\) is polynomial
by Sathaye's DVR theorem and Bass–Connell–Wright globalization. The exact
combined implication is recorded in Babu and Das.[^6] Thus

\[
 \boxed{\text{two commuting pointwise-independent intrinsic LNDs}
 \quad\Longrightarrow\quad K\simeq\mathbb C^{[3]}.}
\]

This is a sufficient theorem, not a property yet derived from the original
cylinder isomorphism. Even on \(\mathbb C[t,u,v]\), the pair
\(t\partial_u,t\partial_v\) has generic rank two and a wholly fixed fiber at
\(t=0\). The ambient leading-field construction can give only rank one.
The [rank-two appendix](research/rank-two-action-pass.md) proves the result
and identifies the support of the bad-fiber set without claiming control
of its scheme multiplicities.

## 7. The remaining cubic and global gaps

These pencil results do not classify every cubic. For a critical-point-free
genuine cubic in four variables, the leading homogeneous cubic surface is
singular, as proved in the preceding pass. Choosing a projective singular
point as the direction of a variable \(u\) yields the form

\[
 F=a u^2+uP(v)+H(v),\qquad
 a\in\mathbb C,\quad\deg P\le2,\quad\deg H\le3.
\]

The missing \(u^3\) and \(u^2v_i\) terms follow from singularity of the
leading form. But this does not put \(F\) into either family above.
When \(a=0\), the coefficient \(P\) can depend on all three remaining
variables, not just one. When \(a\ne0\), completing the square produces

\[
 F=a\left(u+\frac{P}{2a}\right)^2+
       H-\frac{P^2}{4a},
\]

whose remaining polynomial can have degree four.
Neither transformation proves coordinate descent in the general case.

Two exact identities sharpen the remaining tests. In the linear branch,
put \(D=V(P)\) and \(C_\lambda=V(P,H-\lambda)\). Stratifying by \(P=0\)
gives

\[
 \chi_c(F^{-1}(\lambda))=1-\chi_c(D)+\chi_c(C_\lambda).
\]

In the square branch, put \(G=H-P^2/(4a)\). Projection is a double cover
of \(\mathbb A^3\), branched over \(G=\lambda\), so

\[
 \chi_c(F^{-1}(\lambda))=2-\chi_c(G^{-1}(\lambda)).
\]

These are necessary tests, not sufficiency statements.

The [bounded primary-source audit](research/cubic-literature-pass.md)
also records Vénéreau's existing theorem for
\(f_1(x,y)z_1+f_2(x,y)z_2+g(x,y)\): smooth irreducible acyclic zero fiber
implies a coordinate. A stable coordinate meets those hypotheses.
This is another proved class, not a classification of all cubics.
The original article is [Vénéreau, Main Theorem, pp. 622-623](https://doi.org/10.4153/CMB-2005-058-7).

Beyond cubics there is a more basic missing theorem: there is no proved
reduction of an arbitrary slice polynomial to bounded degree or to these
normal forms. The global intrinsic-action route from the previous pass
also still has a degeneration problem. Having nonzero commuting
derivations is not the same as having enough everywhere-independent
derivations or a polynomial slice.

The full target remains open in this project. The next proof task must
address one of these actual gaps, not repeat a bounded search in an already
classified family or treat a known coordinate criterion as a new result.

## Sources

[^1]: L. Makar-Limanov, P. van Rossum, V. Shpilrain, and J.-T. Yu, [*The stable equivalence and cancellation problems*](https://ems.press/content/serial-article-files/43009), *Commentarii Mathematici Helvetici* **79** (2004), 341–349, Theorem 1.2 and its proof.
[^2]: Stefan Maubach, [*The Commuting Derivations Conjecture*](https://www.math.ru.nl/~maubach/Papers/The_Commuting_Dervations.pdf), Theorem 4.5 and Corollary 4.2; published in *Journal of Pure and Applied Algebra* **179** (2003), 159–168. Cross-check: A. K. Dutta and A. Lahiri, [*On Residual and Stable Coordinates*](https://arxiv.org/html/1908.03549), Theorem 1.1, published in *Journal of Pure and Applied Algebra* **225** (2021), 106707.
[^3]: Nguyen Van Chau, [*Polynomial maps of the complex plane with the branched value sets isomorphic to the complex line*](https://math.ac.vn/uploads/files/0202197.pdf), *Acta Mathematica Vietnamica* **27** (2002), 197–202, Section 2 and Lemma 1. Used for the finite exceptional set and affine-line rectification, not as attribution for the new notes' cohomology calculation.
[^4]: Dominic Joyce, [*Constructible functions on Artin stacks*](https://arxiv.org/html/math/0403305), Section 3.2 and Theorem 3.8. Used for compact-support Euler pushforward, not for the pencil classification.
[^5]: V. Shpilrain and J.-T. Yu, [*Affine varieties with equivalent cylinders*](https://arxiv.org/html/math/0110324), Proposition 1.1(c), *Journal of Algebra* **251** (2002), 295–307. The arbitrary-stabilization version is also stated in S. Kuroda, [*Initial forms of stable invariants for additive group actions*](https://arxiv.org/pdf/1304.0313), Section 3.
[^6]: J. R. Babu and P. Das, [*Structure of \(\mathbb A^2\)-fibrations having fixed point free locally nilpotent derivations*](https://arxiv.org/html/2001.07632v5), definition in Section 1 and the discussion of Sathaye and Bass–Connell–Wright in Section 4. Original sources: A. Sathaye, [*Polynomial Ring in Two Variables Over a D.V.R.: A Criterion*](https://doi.org/10.1007/BF01388536), 1983; H. Bass, E. H. Connell, and D. L. Wright, [*Locally Polynomial Algebras Are Symmetric Algebras*](https://doi.org/10.1007/BF01403135), 1976. The original publisher texts were not accessible in full; the exact combined consequence was checked in the accessible Babu–Das paper.

1. Makar-Limanov, van Rossum, Shpilrain, and Yu. [*The stable equivalence and cancellation problems*](https://ems.press/content/serial-article-files/43009). 2004.
2. Maubach. [*The Commuting Derivations Conjecture*](https://www.math.ru.nl/~maubach/Papers/The_Commuting_Dervations.pdf). Author manuscript, 2001; journal publication, 2003.
3. Dutta and Lahiri. [*On Residual and Stable Coordinates*](https://arxiv.org/html/1908.03549). Preprint, 2019; journal publication, 2021.
4. Nguyen Van Chau. [*Polynomial maps of the complex plane with the branched value sets isomorphic to the complex line*](https://math.ac.vn/uploads/files/0202197.pdf). 2002.
5. Joyce. [*Constructible functions on Artin stacks*](https://arxiv.org/html/math/0403305). Version 7, 2006.
6. Shpilrain and Yu. [*Affine varieties with equivalent cylinders*](https://arxiv.org/html/math/0110324). 2002.
7. Kuroda. [*Initial forms of stable invariants for additive group actions*](https://arxiv.org/pdf/1304.0313). arXiv:1304.0313v2.
8. Babu and Das. [*Structure of \(\mathbb A^2\)-fibrations having fixed point free locally nilpotent derivations*](https://arxiv.org/html/2001.07632v5). 2020 preprint; 2021 journal publication.
