# The involution degree-band criterion is not an automatic Reynolds inverse

The primary Jurkiewicz theorem requires a particular interval of
nonlinear homogeneous degrees. It does not say that every polynomial
involution, or every involution with a principal odd module, has an
invertible Reynolds average. The actual constant-acceleration control
already constructed in this pass fails that interval and has a
noninvertible average, although its involution is tame and linearizable.

## 1. The retained recognition gate and its tame hypothesis

Use only the actual hypotheses of the
[constant-acceleration reduction](constant-acceleration-involution-boundary-pass87.md):
one original coordinate has nonzero constant acceleration under a
globally sliced LND of a polynomial four-ring. Each coordinate fiber has
\[
C_\lambda\simeq\mathbb C^{[3]},\qquad
C_\lambda=A\oplus Au,\qquad
u^2=2(\lambda-r)/q,\qquad
\iota|_A=\operatorname{id},\quad\iota(u)=-u.
\tag{1}
\]
Its fixed scheme is a nonempty smooth surface. Thus linearizing one
fiber involution as a reflection would give \(A\simeq\mathbb C^{[3]}\).

[Lamy--Przytycki, Corollary B](https://www.math.univ-toulouse.fr/~slamy/stock/translation_immeuble.pdf)
assumes a finite subgroup of \(\operatorname{Tame}(k^3)\), with
\(\operatorname{char}k=0\), and obtains a tame linearizing conjugator.
The complete short proof on printed page 30 uses a CAT(0) fixed point
and averaging within a triangular stabilizer factor. It does not
establish tameness of an arbitrary polynomial involution. Consequently,
\[
\text{one }\iota_\lambda\text{ is conjugate into }\operatorname{Tame}(\mathbb C^3)
\quad\Longrightarrow\quad A\simeq\mathbb C^{[3]}.
\tag{2}
\]
The original theorem is in Annales Henri Lebesgue 4 (2021), 605--651;
the linked author translation is dated 29 October 2022.

A current primary cross-check is Lamy's
[*Tame polynomial automorphisms*](https://arxiv.org/pdf/2609.05655),
submitted 4 September 2026. Its Proposition 4.11, printed page 22,
retains exactly the finite tame-subgroup hypothesis. Its complete
displayed proof was read, not its full construction or dependencies.
This is a scope check, not a claim that a broader theorem cannot exist.

## 2. What the original Jurkiewicz theorem actually assumes

[Kraft--Zaidenberg, Section 9.7](https://arxiv.org/pdf/2403.12489v2),
printed page 22, summarizes a bounded Taylor-decomposition condition.
The cited original is
[Jurkiewicz, *Linearizing some Z/2Z actions on affine space*](https://www.numdam.org/item/CM_1990__76_1-2_243_0.pdf),
Compositio Mathematica 76 (1990), 243--245.

For an involution \(\iota\) fixing the origin, let \(L=d\iota_0\).
Its Reynolds map satisfies
\[
\sigma=\tfrac12(\operatorname{Id}+L\circ\iota),\qquad
\sigma\circ\iota=L\circ\sigma,\qquad d\sigma_0=\operatorname{Id}.
\tag{3}
\]
Theorem case 3, printed page 244, assumes characteristic zero and,
for some integer \(d\ge2\),
\[
\iota=L+\sum_{j=d}^{2d-2}H_j,\qquad H_j\text{ homogeneous of degree }j.
\tag{4}
\]
It concludes that \(\sigma\) is an automorphism. The proof gives an
explicit polynomial inverse. Page 245 also gives a linearizable
involution whose average is not invertible. All three pages, including
the proof and example, were read visually. The earlier 1989 paper
covering cases 1 and 2 was not newly read.

In particular, (4) is not merely finiteness of the homogeneous expansion
of a polynomial map, nor a hypothesis stated as termination of an
arbitrary formal inverse. These distinctions matter when applying the
survey's abbreviated wording.

## 3. The principal odd module does not supply the degree band

The complete actual polynomial control is proved in
[the fiber-row note, Section 4](constant-acceleration-fiber-row-pass87.md).
For clarity, the calculation needed to compare it with (4) is recorded
here. Start with genuine coordinates \((u,a,b,c)\), let
\(E=\partial_u\), and use
\[
\begin{gathered}
x=u,\quad y=(1+u^2)a+ub,\quad z=ua+b,\quad W=c+u^2,\\
u=x,\quad a=y-xz,\quad b=(1+x^2)z-xy,\quad c=W-x^2.
\end{gathered}
\tag{5}
\]
These are inverse polynomial frames. Thus \(W\) is an actual coordinate
with \(E^2W=2\). On \(W=\lambda\), the ring is
\(\mathbb C[u,a,b]\), the fixed ring is
\(\mathbb C[a,b,u^2]\), and the odd module is its free summand generated
by \(u\). The origin in the actual fiber coordinates \((x,y,z)\) is fixed.
Direct substitution gives
\[
\begin{gathered}
\iota(x,y,z)=
\bigl(-x,\ (1+2x^2)y-2x(1+x^2)z,
                 (1+2x^2)z-2xy\bigr),\\
L=\operatorname{diag}(-1,1,1),\qquad
\sigma(x,y,z)=\bigl(x,(1+x^2)(y-xz),(1+x^2)z-xy\bigr),\\
\sigma=(u,(1+u^2)a,b),\qquad
\det\operatorname{Jac}_{x,y,z}\sigma=1+x^2.
\end{gathered}
\tag{6}
\]
The involution has nonzero homogeneous terms of degrees 2, 3, and 4.
If (4) held in this frame, its nonzero quadratic term would force
\(d=2\), whose upper endpoint is also 2. Its cubic and quartic terms
exclude this. Independently, the nonconstant Jacobian determinant in
(6) prevents \(\sigma\) from being a polynomial automorphism.

Its formal inverse at the origin also fails to terminate: in target
coordinates \((U,V,B_0)\), recovery of \(a\) requires
\(a=V/(1+U^2)\). Recovery of the original coordinate \(z\) contains
\(UV/(1+U^2)\), whose geometric expansion has infinitely many nonzero
terms. This is a calculation in the completed local ring, not an
additional source hypothesis.

The three-variable part of (5) is a composition of elementary shears:
first \(b\mapsto b+ua\), then \(a\mapsto a+ub\), with the second
formula using the updated \(b\). Hence the fiber involution is already
tame-conjugate to \(u\mapsto-u\). Its failure of (4) and of this
particular Reynolds inverse does not obstruct linearization in other
coordinates. It disproves automatic applicability in the supplied
frame, not the possibility of finding a better frame.

## 4. Exact remaining gate and evidence scope

Expression (1) supplies the full parity decomposition, and the
fiber-row proof even supplies a unimodular odd coefficient row.
Neither implies (4), as (5)--(6) show. A new argument producing
tamizability, a suitable homogeneous degree band, or an actual global
linearizing coordinate change would still be required to use these
criteria for arbitrary fibers of the constant-acceleration reduction.

The original-coordinate degree of \(W\) under the action is two, but
the ordinary degrees in (4) concern the three-variable fiber involution.
They are different degrees. In (5), the companion \(y\) also has
\(E\)-degree two. This is a control for the broader one-quadratic-
coordinate problem, not for a frame with three \(E\)-affine companions.

This addendum independently fully reviewed the seven-equation
constant-acceleration core and the eight-equation fiber-row proof.
It adds a statement-level source gate and the displayed comparison,
not a numerical method. The primary reads are the selected LP and
2026 corollary proofs, the indicated KZ paragraph, and the complete
three-page Jurkiewicz paper. No full LP metric-proof audit, exhaustive
literature search, novelty claim, or unconditional recognition is made.
Files through pass86 and the existing pass87 core are unchanged.

The visually inspected original Jurkiewicz PDF is retained at
[general-jurkiewicz-reynolds-pass87.pdf](../tmp/pdfs/general-jurkiewicz-reynolds-pass87.pdf).
Its SHA-256 is
98754b6eaf8fad7c8177604228e436e2cfc21315de26af7954d3859ee4fa697d.
The complete saved addendum received an author EOF read before being
sent for independent review. No symbolic execution is claimed for
its displayed comparison; the separate control's verification belongs
to its own record.
