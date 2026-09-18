# Polynomial-curve extensions and the global cancellation gap

The explicit coordinate theorem now covers an arbitrary monic curve
polynomial, including nonhomogeneous polynomials with distinct or repeated
roots. A separate obstruction identifies exactly when a canonical local-slice
rescaling extends across the plinth divisor. Neither result proves the
unrestricted complex threefold cancellation conjecture.

The distinction is essential: a complete proof for an infinite family is
not a classification of every possible cancellation factor. The base
construction belongs to established local-slice theory. The coordinate
deduction and obstruction have complete working proofs and separate
reconstructions, but their novelty is unestablished and they have not
received human expert review.

## 1. The question and the remaining quantifier

The working target is
\[
X\times_{\mathbb C}\mathbb A^1\cong\mathbb A^4
\quad\Longrightarrow\quad X\cong\mathbb A^3.
\tag{1}
\]
The original email's conclusion had a dimension mismatch. Its intended
field and dimension have not been confirmed; (1) is the interpretation
used throughout this investigation, not a newly supplied assumption from
the professor.

Algebraically, a factorization in (1) gives a locally nilpotent derivation
on a polynomial four-ring with a slice. A derivation \(E\) is locally
nilpotent when repeated differentiation eventually kills each individual
polynomial. A slice is a polynomial \(s\) with \(E(s)=1\). The slice
theorem gives the ring as \((\ker E)[s]\); cancellation asks whether the
three-dimensional invariant ring must itself be polynomial.

This pass treats extensions of a specified polynomial three-ring

\[
R=\mathbb C[x,y,z],\qquad
E=A D+B\partial_t,\qquad A,B\in C:=\ker D.
\tag{2}
\]

Here \(D\ne0\) is locally nilpotent. Its plinth ideal consists of the
invariants that occur as derivatives: \(P_D=D(R)\cap C\). For a
polynomial three-ring the kernel is a polynomial two-ring and the plinth
is principal. These are existing three-variable results, not consequences
of the present computations.[^1]

The previous [affine-replacement proof](research/general-invariant-affine-pass17.md)
gives the source-dependent working criterion

\[
E\text{ has a slice}\quad\Longleftrightarrow\quad
A P_D+B C=C.
\tag{3}
\]

It constructs an affine-in-\(t\) replacement for any slice under these
hypotheses. It does not establish polynomiality of every kernel in (2),
and no proof has been supplied that an arbitrary slice derivation on
four-space can be put into (2). These are two separate missing steps.

## 2. Arbitrary polynomial-curve bases

Let \(F(Y)\) be monic of degree \(d\ge2\), let \(n\ge1\), and let
\(P(X,f)\in\mathbb C[X,f]\) have nonconstant residue \(P(X,0)\).
Define

\[
\begin{aligned}
G(R,S)&=S^dF(R/S), & f&=xz-F(y),\\
r&=xP(x,f)+yf^n, &
h&=\frac{G(r,f^n)+f^{nd+1}}x,\\
\delta&=-\operatorname{Jac}(f,h,\cdot).
\end{aligned}
\tag{4}
\]

The expression for \(G\) denotes its polynomial homogenization, including
at \(S=0\). Taylor's identity shows that \(h\) is polynomial:

\[
h=zf^{nd}+\sum_{k=1}^d\frac{F^{(k)}(y)}{k!}
 x^{k-1}P(x,f)^k f^{n(d-k)}.
\tag{5}
\]

The base derivation is primitive, locally nilpotent, and rank three, with

\[
\ker\delta=\mathbb C[f,h],\qquad
\ker\delta^2=C\oplus Cr,\qquad
P_\delta=f^nhC.
\tag{6}
\]

Primitivity means that the three polynomial coefficients of the derivation
have no common nonconstant factor. Rank three means that no ambient
polynomial coordinate is invariant. Thus this is not simply a triangular
derivation written with an unnecessarily complicated formula.

The [complete base proof](research/polynomial-curve-lift-pass18.md)
uses the exact localized presentation

\[
R_f=C_f[x,r]/\bigl(xh-G(r,f^n)-f^{nd+1}\bigr).
\tag{7}
\]

Its \(C_f\)-basis consists of \(x^b r^i\), with \(b\ge0\) and
\(0\le i<d\). Their derivation degrees \(db+i\) are distinct, so
highest-degree terms cannot cancel. This computes the localized kernel
and first-degree module. Reducing modulo \(f\) then excludes poles in
their coefficients and gives (6) globally.

The key residue comparison is between
\(H_0=x^{d-1}P(x,0)^d\) and \(R_0=xP(x,0)\). If
\(a=\deg_xP(x,0)\ge1\), their degrees are \(d(a+1)-1\) and
\(a+1\). The first is strictly larger, so the corresponding function-field
degrees exclude \(R_0\in\mathbb C(H_0)\). That excludes hidden
first-degree elements with an \(f\)-denominator. Separate coefficient
calculations exclude both possible common factors \(f,h\).

The original construction principle is Freudenburg's: start with
\(D_0=x\partial_y+F'(y)\partial_z\), for which \(D_0r=xf^n\), and
use the minimal irreducible relation modulo \(x\).[^2] Dasgupta--Gaifullin
recall that general theorem and give the displayed monomial subfamily
\(F(Y)=Y^d\), together with rank criteria.[^1] The arbitrary-monic
substitution is an application of this existing machinery. It is not
presented as a new way to construct locally nilpotent derivations.

## 3. Explicit coordinates for every admissible invariant extension

For the bases (4), the extension \(E=A\delta+B\partial_t\) has a
slice precisely when

\[
(A,B)C=C,\qquad B=c+fhQ,
\qquad c\in\mathbb C^*,\quad Q\in C.
\tag{8}
\]

Necessity invokes (3). Its coefficient simplification is elementary:
a unit on either kernel-coordinate axis is constant, and the constants
must agree at their intersection. Sufficiency and the coordinate proof
below are algebraic and need only the right side of (8).

Normalize \(c=1\) by scaling the derivation. Set \(g=f^nh\), choose
\(U,V\in C\) with \(AgU+BV=1\), and put

\[
\rho=Br-Agt,\qquad s=Ur+Vt,\qquad
X=\frac{G(\rho,f^n)+f^{nd+1}}h.
\tag{9}
\]

These expressions satisfy \(E\rho=EX=0\), \(Es=1\), and
\(X\equiv B^d x\pmod{f^n}\). Polynomiality of \(X\) is checked
before reducing modulo \(f^n\): the relevant numerator difference is
divisible by \(hf^n\). In particular, the proof does not cancel a
potential zero divisor in a nonreduced quotient.

The remaining correction is a finite jet. In
\(\mathbb C[X,f]/(f^n)\), solve

\[
H=b_H^{1-d}P(b_H^{-d}X,f),\qquad
b_H=B\bigl(f,X^{d-1}H^d\bigr).
\tag{10}
\]

Starting from \(P(X,f)\), each update improves the congruence by one
power of \(f\). Exactly \(n-1\) updates suffice. Negative powers are
finite expansions of units in this nilpotent quotient, not infinite
analytic series. Use the representative of \(H\) of degree less than
\(n\) in \(f\), and define

\[
Y=\frac{\rho-XH}{f^n},\qquad
S_F=\sum_{k=1}^d\frac{F^{(k)}(Y)}{k!}
 X^{k-1}H^k f^{n(d-k)},\qquad
Z=\frac{h-S_F}{f^{nd}}.
\tag{11}
\]

The finite-jet equation proves polynomiality of \(Y\). Taylor's identity
gives \(X(h-S_F)=f^{nd}(F(Y)+f)\). Since \(f\) is prime and
\(X\equiv x\pmod f\), it also proves polynomiality of \(Z\).
Thus \(f=XZ-F(Y)\).

Showing that these expressions are polynomials is not yet enough. The
[full inverse proof](research/polynomial-curve-lift-pass18.md)
works in independent variables \(X,Y,Z,s\), reconstructs \(f,h,\rho\),
uses the inverse unimodular matrix to recover \(r,t\), and recovers
\(x,y,z\) through polynomial divided differences and the same finite
congruences. The independent reconstructed \(h\) is nonzero: specialize
\(Y\) to any root of \(F\) and \(Z=0\). This handles \(F(0)\ne0\)
and repeated roots without introducing an extra hypothesis.

Composition yields

\[
R[t]=\mathbb C[X,Y,Z,s],\qquad
E=\partial_s,\qquad\ker E=\mathbb C[X,Y,Z]
\tag{12}
\]

in the normalized case. The
[separate coordinate audit](research/polynomial-curve-lift-audit-pass18.md)
checks lower coefficients, both divisions, and the inverse composition.
Finite Taylor and Hermite corrections have predecessors in explicit
Danielewski cylinder isomorphisms; those results do not themselves assert
(12) for this family.[^3]

## 4. Why the general rescaling shortcut fails

For a general \(D\) in (2), choose a minimal local slice \(Dr=p\).
Every invariant affine-slice kernel has the exact presentation

\[
M=R[r/V]=R[w]/(Vw-r),\qquad
0\ne V\in C,\quad(p,V)C=C.
\tag{13}
\]

Conversely, every modification of this form is an invariant-extension
slice kernel. The [two-way proof](research/arbitrary-invariant-kernel-pass18.md)
also gives \(M_V=R_V\) and \(M_p=C_p[w]\). The first chart need
not be polynomial over \(C_V\), so these charts do not prove that \(M\)
is a polynomial three-ring.

Suppose now that \(D\) is primitive, and let \(p_0\) be the squarefree
part of \(p\). Let \(\lambda\in C_V^*\) satisfy
\(\lambda\equiv1\pmod{p_0}\). On the local-slice ring \(R_{pV}\),
consider the specific automorphism fixing \(C_{pV}\) and sending
\(r\) to \(\lambda r\). Then

\[
\boxed{\sigma_\lambda(R_V)\subseteq R_V
\quad\Longleftrightarrow\quad
\sigma_\lambda\in\operatorname{Aut}(R_V/C_V)
\quad\Longleftrightarrow\quad
\lambda\equiv1\pmod{pC_V}.}
\tag{14}
\]

Thus the full plinth multiplicities matter. Agreement only on its reduced
support is insufficient for this canonical rescaling.

The [finite proof](research/rescaling-obstruction-audit-pass18.md)
tests one prime factor \(f^n\mid p\). Minimality makes \(r\) a unit
in \(R_{(f)}\), while primitivity gives a coordinate \(a\) with \(Da\)
a unit there. If \(k=v_f(\lambda-1)<n\), set
\(d=\deg_D(a)\), \(N=nd\), and \(q=\lambda-1\). The finite
binomial polynomial \(c(T)=\sum_{\ell=1}^N\binom T\ell q^\ell\)
agrees with \(\lambda^m-1\) to order at least \(N+1\) at every
nonnegative integer \(m\).

Substitute \(c(T)\) into the finite flow of \(a\) with time \(rc(T)/p\).
If the rescaling extends, every integer evaluation is integral. A finite
Vandermonde matrix then forces every coefficient to be integral. But its
linear coefficient has valuation \(k-n<0\), a contradiction. Conversely,
full divisibility in (14) makes that finite flow and its inverse polynomial.
No completion, convergence, or infinite-iterate limit is needed.

This is a statement about a specified pure rescaling, not every affine
change of the local slice or every abstract isomorphism of rings.
Kernel-fixing automorphisms and their multipliers are already studied by
Kuroda; the inspected source is a primary announcement, not a complete
journal proof.[^4] Stampfli gives a related iterate-and-differentiate
argument for translations inside a centralizer. Its commutation premise
does not hold for a nontrivial rescaling.[^5] The
[statement audit](research/polynomial-curve-literature-pass18.md)
records these exact scope differences without a priority claim.

## 5. Every finite neighborhood can agree while the global map fails

Even the stronger-looking test of comparing all finite neighborhoods
does not repair the shortcut. If \(V\equiv1\pmod{p_0}\), then
the natural inclusion induces isomorphisms

\[
R/(p_0^N)\cong M/(p_0^N)\qquad\text{for every }N\ge1.
\tag{15}
\]

Indeed \(V\) is a unit in each quotient, so adjoining \(r/V\) adds
nothing there. The isomorphisms are compatible, including on completion.
They do not control the locus \(V=0\), which lies away from the plinth.

For an explicit control, use
\(D=x^2\partial_y+2y\partial_z\), \(p=x^2\), \(r=y\),
and \(V=1+x\). Then \(M=\mathbb C[x,w,z]\) with
\(y=(1+x)w\). Both rings are polynomial, but the specified inclusion
is not surjective and has Jacobian \(1+x\). Every quotient modulo
\(x^N\) is nevertheless an isomorphism. This disproves an inference
about the chosen map, not cancellation of these rings.

More generally the smooth hypersurface presentation in (13) has a
nowhere-vanishing residue form \(\omega_M\) satisfying
\(dx\wedge dy\wedge dz=V\omega_M\). The canonical modification
therefore has exactly the global Jacobian factor that formal plinth
comparisons miss. The
[modification analysis](research/radical-modification-attack-pass18.md)
also explains why balancing a determinant with a second free coordinate
proves a stabilized assertion, not removal of that coordinate.

## 6. Disconnected plinth support has a narrower remaining geometry

Kaliman's retained-curve theorem says that each irreducible component
of the relevant primitive exceptional curve has normalization
\(\mathbb A^1\). It does not identify that curve with a smooth line.[^6]
From this input, the [plane-curve deduction](research/disconnected-plinth-pass18.md)
gives an elementary restriction: any disconnected union of such curves
must consist of pairwise disjoint fibers of a single polynomial.

For two disjoint irreducible curves \(f_1=0,f_2=0\), the restriction
of either defining function to the other is a unit and therefore a
nonzero constant. Hence \(f_2-b=f_1h\) and \(f_1-c=f_2k\).
Comparing total degrees forces \(h,k\) to be constants. Applying this
across connected components yields

\[
p=\mu\prod_{i=1}^{r}(F-a_i)^{e_i},\qquad
r\ge2,\quad a_i\ne a_j\ (i\ne j),\quad e_i\ge1.
\tag{16}
\]

For primitive rank three, \(F\) cannot be a kernel coordinate. There
is a stronger restriction: every component in (16) must have a
multibranch singularity. If one were unibranch everywhere, its finite
normalization would be a topological homeomorphism from the affine line.
The contractible-plane-curve theorem puts it into coordinates
\(u^a-v^b=0\), with coprime positive exponents.[^7]

If one exponent is one, the whole pencil consists of parallel coordinate
lines and rank is at most two. Otherwise a disjoint polynomial curve
would give nonconstant polynomials \(A(t),B(t)\) with
\(A^a-B^b=c\ne0\). Coprimality and differentiation imply
\(A^{a-1}\mid B'\) and \(B^{b-1}\mid A'\); their degree
inequalities contradict each other. This excludes the remaining
unibranch case.

It is not valid to omit that singularity qualification. The polynomial
\(F(u,v)=v^2-u^3+3u\) has disjoint irreducible nodal fibers at \(2\)
and \(-2\), both with normalization \(\mathbb A^1\). Their explicit
parametrizations are
\((u,v)=(t^2-2,t(t^2-3))\) and
\((u,v)=(t^2+2,t(t^2+3))\). The polynomial \(F\) is not a
coordinate because its gradient vanishes at the two nodes.

This is plane data, not an actual plinth realization on polynomial
three-space. It disproves the proposed plane-curve shortcut but neither
proves nor refutes connectedness for primitive rank-three plinths.
Coefficients comaximal with (16) reduce to
\(B=b(F)+p_{\rm red}Q\), with \(b(a_i)\ne0\), by interpolation.
That useful simplification still does not construct global coordinates.

The stronger requirement of a single intermediate point over a node
does not close the gap either. For the first nodal cubic, put
\(t=w^2\), \(d=w^4-3\), and
\(T=\mathbb C+d\mathbb C[w]\). The map
\(u=d+1,\ v=dw^2\) defines a finite degree-two morphism
\(\operatorname{Spec}T\to\{F=2\}\). Exactly one point lies over the
node, but its normalization has four distinct points there. The
[explicit ring proof](research/nodal-plinth-realizability-pass18.md)
also supplies an integral node-local lattice control. It does not
construct the exceptional surface or the full quotient homology diagram.

This source boundary was already substantive historically: Kaliman's
2007 problem statement asks whether individual retained components are
contractible or smooth, rather than supplying that conclusion.[^8]
That historical question is not being represented as a verified current
open-status statement. A missing present-day theorem must not be replaced
by a conjectural premise from an older source.

## 7. Verification and reproducibility

The complete regression run finished at **2026-09-13 03:04:53 UTC**:
**404 test methods passed in 29 suites**, including 18 new methods in
two suites. Exact commands, counts, runtimes, and exit codes are recorded
in [verification-pass-18.json](verification-pass-18.json).

| New suite | Methods | Exact controls | Main-run test time |
|---|---:|---|---:|
| [Polynomial-fiber checks](research/polynomial_fiber_checks_pass18.py) | 8 | Physical Jacobians, localized inverses, coefficient gcds, actual finite-jet numerators in both directions | 43.709 s |
| [Rescaling and curve controls](research/rescaling_curve_controls_pass18.py) | 10 | Binomial truncations, Vandermonde determinants, pole orders, Jacobian factor, determinant balancing, nodal fibers and interpolation | 0.204 s |

The new checkers use exact SymPy arithmetic and do not import research
solvers or other checkers. The polynomial-fiber suite covers three monic
polynomials in its jet tests, two choices of \(P\), and \(n=1,2,3\),
with a deliberately uncorrected negative control. Physical coefficient
gcds are checked for eight explicit bases. Neither finite collection is
used to infer the arbitrary-parameter theorems.
Five additional direct exact identities verify the intermediate nodal
ring's equation, squarefreeness and recurrence, and its integral lattice.
They are separate controls, not extra unittest methods in the total.

Run the new suites from the project directory:

```sh
/opt/anaconda3/bin/python research/polynomial_fiber_checks_pass18.py
/opt/anaconda3/bin/python research/rescaling_curve_controls_pass18.py
```

The [README](README.md) contains all 29 commands. Written proofs supply
the general algebra, and the geometric deductions identify their published
dependencies. Separate reconstructions are internal checks, not human peer
review. The repository does not contain a Lean proof of these theorems.

## 8. What completion would still require

The arbitrary-monic family closes because its precise presentation (7)
supports a finite correction and an explicit polynomial inverse. No proof
shows that every primitive rank-three derivation has such a presentation,
or a finite sequence of compatible presentations of this kind.

The general principal-modification route therefore needs an actual
coordinate construction that can change the invariant-plane embedding,
or another global recognition argument. By (14), canonical pure rescaling
cannot repair a merely radical congruence unless full-plinth congruence
also holds. The control in (15) shows that formal agreement alone does
not certify the specified global map; it does not refute an abstract
polynomial-ring recognition implication. Disconnected support requires
additional control of the multibranch configurations in (16).

Even a solution of all invariant extensions in (2) would leave the
arbitrary-slice reduction to that form. A proof of (1) must explicitly
cover that quantifier. None of the restricted results, successful test
runs, or failed searches can replace it.

The finished deliverable is therefore a set of restricted working proofs,
precise negative controls, a reproducible verification record, and a
statement-level literature comparison. The full conjecture remains
unresolved in this investigation. No novelty assertion, submission,
external contact, or publication is included.

## Sources

[^1]: N. Dasgupta and S. A. Gaifullin, [*On locally nilpotent derivations of polynomial algebra in three variables*](https://www.mathnet.ru/eng/sm10094), *Sbornik: Mathematics* 216(4) (2025), 456-484. Published full text: three-variable prerequisites, Theorem 2.17, Lemma 4.3, Corollary 5.6 and Theorem 5.7. The explicit extension-coordinate theorem is not attributed to this paper.
[^2]: G. Freudenburg, [*Local slice constructions in k[X,Y,Z]*](https://ir.library.osaka-u.ac.jp/repo/ouka/all/4752/ojm34_04_02.pdf), *Osaka Journal of Mathematics* 34 (1997), 757-767, Section 2, Theorem 2. General construction, cross-read with its published recall in source 1.
[^3]: L. Moser-Jauslin and P.-M. Poloni, [*Isomorphisms between cylinders over Danielewski surfaces*](https://arxiv.org/html/2002.12202), arXiv:2002.12202v1 (2020), Section 4 and Theorem 4.0.1. Explicit finite-congruence methodological predecessor, not an unrestricted kernel-recognition theorem.
[^4]: S. Kuroda, [*The automorphism group of a UFD over the kernel of a locally nilpotent derivation*](https://www.math.okayama-u.ac.jp/~hashimoto/paper/Comm-Alg/35/jsca35kurodas.pdf), eight-page primary symposium announcement, 2013 context. Propositions 2.1-2.2 and Theorem 2.4. The source explicitly identifies itself as an announcement; no later complete publication is assumed.
[^5]: I. Stampfli, [*Automorphisms of C3 Commuting with a C+-Action*](https://arxiv.org/pdf/1406.6246), arXiv:1406.6246v2; *International Mathematics Research Notices* 2015(19), 9832-9856. Proposition 5.1.1 and Lemma 5.1.2, including the proof and its commutation hypothesis.
[^6]: S. Kaliman, [*Free C+-actions on C3 are translations*](https://www.math.miami.edu/~kaliman/library/Ka.invent.2004.c%2B.pdf), final author version, Proposition 3.2 and Theorem 5.2(i). Polynomial normalization is used with the retained-support hypotheses; arbitrary singular curve factors are not substituted for the actual quotient.
[^7]: K. Palka, [*A new proof of the theorems of Lin-Zaidenberg and Abhyankar-Moh-Suzuki*](https://arxiv.org/pdf/1405.5391), arXiv:1405.5391v2, February 9, 2015, Theorem A. Published-theorem input to the unibranch exclusion; its surface-theoretic proof is not formally verified by the regression suite.
[^8]: S. Kaliman, problem statement in [*Affine Algebraic Geometry*, Oberwolfach Report 01/2007](https://publications.mfo.de/bitstream/handle/mfo/2987/OWR_2007_01.pdf?isAllowed=y&sequence=1), printed pages 68-69. Exact historical questions concerning retained exceptional curves, not a claim about their status in 2026.
