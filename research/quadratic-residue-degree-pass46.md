# The remaining divisor covers are quadratic

Under the actual degree-two independent-defect frame hypotheses,
every intrinsic divisor residue cover has degree at most four. The
cases of degree three or four already force an invariant ambient
coordinate and hence a polynomial sliced quotient. More precisely,
at a common-speed plinth prime, either the bad-coordinate image is
algebraic and supplies that invariant coordinate, or its nonconstant
members are actual parameters of the residue line and the full
residue constant field has degree two.

Thus any still-unrecognized quotient in this frame has only
quadratic primitive plinth covers. This does not extend the full
DVR presentation from pass 45 to every such prime, and it does not
prove that the local data glue to a polynomial three-ring.

The later same-pass [minimal-slice lifting proof](minimal-quadratic-slice-pass46.md)
adds the finite correction needed to obtain the full DVR quadratic
presentation from this degree-two residue conclusion. The present
proof and its original field-level boundary are retained unchanged.

## 1. Original hypotheses and residue notation

Keep precisely the hypotheses of
[the actual quadratic graph](generic-bad-pair-pass44.md) and
[the acceleration extension](acceleration-divisor-extension-pass45.md):
\[
B=A[s_*]=\mathbb C[x_1,x_2,x_3,x_4],\qquad
E(s_*)=1,\qquad A=\ker E,
\]
\[
C\simeq\mathbb C^{[2]},\quad L=\operatorname{Frac}C,
\quad B\otimes_C L=L[x_3,x_4],
\quad x_i=\mathcal Q_i(x_3,x_4),\quad\deg\mathcal Q_i\le2
\quad(i=1,2).
\tag{1}
\]
The polynomials \(f=Ex_3,g=Ex_4,h_1=E^2x_1,h_2=E^2x_2\)
belong to \(C\). The original good and bad partials retain all
their supplied adjoint bounds. Their role here is the already
proved actual-generator equality (1), not an arbitrary quadratic
parametrization.

Choose a primitive intrinsic LND \(D\ne0\) of \(A\) with
\(\ker D=C\). The inherited factorial faithfully-flat theorem
gives a principal full plinth and an actual minimal local slice:
\[
\operatorname{pl}(D)=pC,\qquad Dr=p,\qquad p\ne0.
\tag{2}
\]
Here \(C\subset A\) is faithfully flat and factorially closed,
and \(A,B\) are UFDs. None of these inputs assumes that \(A\)
is polynomial.[^plinth]

Fix any prime element \(\pi\in C\), and put
\[
R=C_{(\pi)},\qquad \kappa=R/\pi R
=\operatorname{Frac}(C/\pi C),\qquad
\overline A=A\otimes_C\kappa,
\quad\overline B=B\otimes_C\kappa.
\tag{3}
\]
An overline denotes this entire generic divisor fiber, not just
the image of the bad-coordinate algebra.

## 2. The full residue is a line over a finite field extension

Factorial closure makes \(\pi\) prime in \(A\), and faithful
flatness makes its generic divisor fiber nonempty. Thus
\(\overline A\) is a one-dimensional affine \(\kappa\)-domain.
Primitivity gives \(D(A)\not\subset\pi A\), so reduction of
\(D\) modulo \(\pi\) is nonzero. It stays nonzero after
localizing by the nonzero elements of \(C/\pi C\), since the
residue is a domain. Denote this nonzero LND by \(\overline D\).

The field of invariants has transcendence degree zero over
\(\kappa\). Hence every member of \(\ker\overline D\) is
algebraic over \(\kappa\). The minimal polynomial of a nonzero
such element supplies its inverse inside the same invariant ring;
therefore that ring is a field, denoted \(F_\pi\).

A local slice for \(\overline D\) now has a nonzero invariant
derivative in this field, which is a unit. The slice theorem gives
\[
\overline A=F_\pi[t],\qquad
\overline B=F_\pi[t,s_*].
\tag{4}
\]
Evaluation at \(t=0\) makes \(F_\pi\) a finitely generated
\(\kappa\)-algebra. Since it is algebraic, it is a finite field
extension. Write
\[
e_\pi=[F_\pi:\kappa].
\tag{5}
\]
The extension is separable in characteristic zero. The parameter
\(t\) in (4) is an intrinsic residue coordinate; no lift of it
to an ambient coordinate or to a global slice is asserted.

The exact primitive support gate has a short algebraic proof:
\[
e_\pi=1\quad\Longleftrightarrow\quad \pi\nmid p.
\tag{6}
\]
If \(p\) is a unit of \(R\), the original local slice in (2)
gives \(A_R=R[r/p]\), proving the forward residue statement.
Conversely suppose \(\pi\mid p\) but \(F_\pi=\kappa\).
Then \(\bar r\in\ker\overline D=\kappa\). Lift its value
to \(a\in R\). The actual element \((r-a)/\pi\in A_R\)
has derivative \(p/\pi\). This contradicts
\(\operatorname{pl}(D|_{A_R})=pR\), since invariant localization
commutes with the full plinth. This is the inherited minimal-slice
argument, not an invocation of an affine-line fibration theorem.

## 3. Coordinate-degree growth bounds every residue cover by four

Let \(V_N\subset B_R\) be the \(R\)-span of all monomials
in the four actual coordinate generators of total degree at most
\(N\). It is a finite torsionfree module over the DVR \(R\),
and is therefore free. By (1), after tensoring with \(L\), its
elements have bad-coordinate degree at most \(2N\). Thus
\[
\operatorname{rank}_R V_N\le\binom{2N+2}{2}.
\tag{7}
\]
Let \(W_N\) be its image in \(\overline B\). The map
\(V_N/\pi V_N\to W_N\) is surjective, so
\[
\dim_\kappa W_N\le\operatorname{rank}_R V_N.
\tag{8}
\]
Injectivity is neither assumed nor needed. In particular this
argument does not identify the lattice quotient with the full
coordinate-degree piece of the special fiber.

Choose two algebraically independent members \(y_1,y_2\) among
the four actual residue generators. They exist because those
generators generate the two-dimensional \(\kappa\)-domain (4).
They remain algebraically independent over the algebraic extension
\(F_\pi\). Choose a \(\kappa\)-basis
\(\xi_1,\ldots,\xi_{e_\pi}\) of \(F_\pi\). Every basis
element belongs to some \(W_M\); one finite \(M\) works for all.

The elements
\(\xi_i y_1^a y_2^b\), for \(a+b\le N-M\), are linearly
independent over \(\kappa\). They all belong to \(W_N\).
Consequently
\[
e_\pi\binom{N-M+2}{2}
\le\dim_\kappa W_N\le\binom{2N+2}{2}.
\]
Comparing quadratic leading terms as \(N\to\infty\) proves
\[
e_\pi\le4.
\tag{9}
\]
This is a finite-module growth argument, not an assumption about
flatness of a projective compactification or a count of components
in a chosen unsaturated center.

## 4. A nonconstant bad residue improves the bound to two

Suppose now that \(\pi\mid f,g\). Both bad residues belong to
\(\ker\overline E=\overline A=F_\pi[t]\).
Assume one of them, denoted \(\bar z\), is nonconstant in
\(t\), and put
\[
d=\deg_t\bar z\ge1.
\tag{10}
\]
Here \(z\) is the actual coordinate \(x_3\) or \(x_4\).

The subring \(R[z]\subset B_R\) is a polynomial ring over
\(R\). Localize it at its prime ideal \(\pi R[z]\):
\[
R'=R[z]_{(\pi)},\qquad
\operatorname{Frac}R'=L(z),\qquad
R'/\pi R'=\kappa(\bar z).
\tag{11}
\]
It is a DVR with uniformizer \(\pi\). Since \(\bar z\)
is transcendental over \(\kappa\), no denominator introduced
in (11) vanishes in the residue domain.

Set \(S=B_R\otimes_{R[z]}R'\). Its generic ring is the
polynomial line \(L(z)[z']\), where \(z'\) is the other bad
coordinate. The remaining actual generators have degree at most
two in \(z'\), by (1). Its full residue is
\[
S/\pi S
=F_\pi(t)[s_*],\qquad
[F_\pi(t):\kappa(\bar z)]=e_\pi d.
\tag{12}
\]
Indeed \(F_\pi[t]\) is finite over \(\kappa[\bar z]\),
and localization by nonzero elements of the latter gives its
fraction field. The degree is the tower product
\([F_\pi(t):F_\pi(\bar z)]
[F_\pi(\bar z):\kappa(\bar z)]=d e_\pi\).

Repeat the finite-free filtration argument over \(R'\), using
the three remaining actual generators. Its generic rank is at
most \(2N+1\). A basis of the finite constant field in (12),
multiplied by powers of any remaining residue generator with
positive \(s_*\)-degree, gives the lower bound
\((e_\pi d)(N-M'+1)\) after a fixed degree shift. Such a
generator exists because the residue ring is generated by these
three elements over \(\kappa(\bar z)\) and has transcendence
degree one. Comparing linear leading terms proves
\[
e_\pi d\le2.
\tag{13}
\]
If \(\pi\mid p\), (6) now forces
\[
e_\pi=2,\qquad d=1.
\tag{14}
\]
Every nonconstant bad residue is therefore a polynomial parameter
of \(F_\pi[t]\). This conclusion is on the full divisor fiber;
it is not a polynomial coordinate assertion on \(A_R\) or \(B\).

## 5. An algebraic bad image gives an actual invariant coordinate

Still suppose \(\pi\mid f,g\), but now assume both bad
residues lie in \(F_\pi\). This case is recognized globally,
without requiring \(\pi\mid p\).

The field \(F_\pi\) is finite over
\(\kappa=\operatorname{Frac}(C/\pi C)\), which has
transcendence degree one over \(\mathbb C\). Thus
\(\bar x_3,\bar x_4\) are algebraically dependent over
\(\mathbb C\). There is a nonzero polynomial
\[
P\in\mathbb C[X_3,X_4],\qquad
P(\bar x_3,\bar x_4)=0.
\tag{15}
\]
The relation initially holds in the generic divisor localization.
Clearing an invariant denominator outside \((\pi)\), and using
that \(\pi\) is prime in \(B\), gives
\[
P(x_3,x_4)\in\pi B.
\tag{16}
\]
It is a nonzero polynomial of \(B\), since \(x_3,x_4\) are
actual independent coordinates.

The actual coordinate subring \(\mathbb C[x_3,x_4]\) is
factorially closed in its polynomial extension \(B\). Equation
(16) therefore puts the nonconstant factor \(\pi\) itself in
\(\mathbb C[x_3,x_4]\). Equivalently, one can factor \(P\)
in that UFD and note that its irreducible factors remain prime
in \(B\). Since \(\pi\in C\), it is killed by \(E\).

Kuroda's Proposition 3.2, which states the inherited
Daigle--Freudenburg stable binary-invariant theorem, now gives
an actual coordinate of \(\mathbb C[x_3,x_4]\) killed by
\(E\).[^binary] The alternative that \(E\) kills both bad
coordinates would give such a coordinate directly; here it is
already excluded by \(f,g\ne0\). No stability of the entire
bad-coordinate ring under \(E\) is assumed.

Finally the original slice makes \(A\) regular. The
fixed-coordinate theorem of Bhatwadekar--Gupta--Lokhande gives
\[
A\simeq\mathbb C^{[3]}.
\tag{17}
\]
Its application occurs only after the actual ambient invariant
coordinate has been obtained.[^fixed]

## 6. Exact consequence for the unresolved divisor set

At a plinth prime where a speed or acceleration is a unit,
pass 45 already gives the full quadratic DVR model and residue
degree two. At a remaining simultaneous-vanishing prime, the
bad image is either algebraic, when Section 5 proves (17), or
nonconstant, when Section 4 gives (14). Consequently
\[
\boxed{\text{Either }A\simeq\mathbb C^{[3]},\text{ or every
primitive plinth divisor has }e_\pi=2.}
\tag{18}
\]
In particular a divisor cover of degree three or four is a
recognition certificate in this actual frame, not an additional
unresolved branch. Equation (9) excludes larger degrees in all
cases, including when the quotient is already polynomial.

For the remaining simultaneous primes, this note supplies a
quadratic full residue field and a bad residue line parameter.
It does not yet supply an affine-linear generic bad-coordinate
\(E\)-slice, the full presentation
\(R[T,Z]/(\pi^nZ-T^2+\eta)\), or a global gluing theorem.
The old residual divisor support
\(\gcd(p,f,g,h_1,h_2)\) is not proved empty.

All degree bounds are all-order filtration arguments. No actual
degree-three or degree-four residual model, universal frame
existence, historical novelty, human expert review or formal
proof-assistant verification is asserted. No new numerical suite
is used to certify these field and dimension quantifiers.

[^plinth]: The exact source-backed intrinsic input and its primitive boundary argument are retained in [the intrinsic plinth note](intrinsic-plinth-boundary-pass27.md) and [the generic-fiber note, Section 2.1](intrinsic-rank-pass34.md#21-regularity-integrality-and-the-exceptional-fibers). The local residue and support arguments needed here are reconstructed in Section 2.

[^binary]: Shigeru Kuroda, [*Initial forms of stable invariants for additive group actions*](https://arxiv.org/pdf/1304.0313v2), Proposition 3.2 and surrounding text, PDF p. 8. This primary statement was directly read. It treats a characteristic-zero LND on the full polynomial ring with a nonconstant invariant in an actual two-variable coordinate subring; it does not require that subring to be stable. The paper attributes the result to Daigle--Freudenburg and Freudenburg's earlier work. Its use in this project is inherited from pass 45, not a novelty claim.

[^fixed]: S. M. Bhatwadekar, Neena Gupta and S. A. Lokhande, [*Some K-theoretic properties of the kernel of a locally nilpotent derivation on k[X1,...,X4]*](https://arxiv.org/pdf/1501.01438v1), Theorem 3.5 and full proof, PDF p. 11, directly reread. The hypotheses are a characteristic-zero LND fixing an actual coordinate and a regular kernel; both are established before (17).
