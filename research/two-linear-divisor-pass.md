# The common divisor in a two-linear polynomial

Let
\[
F=A(x,y)u+B(x,y)z+C(x,y),\qquad (A,B)\ne(0,0),
\]

and suppose the general fiber of \(F\) is smooth and rationally
acyclic. This hypothesis holds if \(F\) is a stable coordinate.
Suppose the coefficient gcd \(g=\gcd(A,B)\) is nonconstant.

Then the reduced divisor \(D=V(g)_{\mathrm{red}}\) is a disjoint
union of embedded affine lines. More precisely, base coordinates
\(a,b\) can be chosen so that

\[
g=p(a),\qquad
C(\alpha,b)=c_\alpha b+d_\alpha,\quad c_\alpha\ne0
\quad\text{for each root }\alpha\text{ of }p.
\tag{1}
\]

Write \(A=gA_0,\ B=gB_0\). The finite residual common-zero set
\(E=V(A_0,B_0)_{\mathrm{red}}\) satisfies

\[
E\setminus D=\varnothing.
\tag{2}
\]

The set \(E\cap D\) need not be empty, and the coefficient ideal
\((A,B)\) need not be principal. The proof below keeps those points
separate from the removed points in (2).

These are the coefficient conditions in the known
[Kaliman--Vénéreau--Zaidenberg Theorem 3.24(v')](https://arxiv.org/pdf/math/0104204).
That theorem makes \(F\) a coordinate over \(\mathbb C[a]\).
Thus the stable-coordinate and original-slice cases both close.
This note reconstructs the divisor mechanism and its finite-point
bookkeeping; it is not presented as a new classification.

The published theorem already handles a single smooth irreducible
integrally acyclic fiber. The reconstruction below uses the
general-fiber hypothesis to obtain its coefficient criterion from
rational acyclicity. An independent level-ring and original-slice
check is retained in Sections 7 and 8, but the polynomial level
rings alone are not the justification for stable embedding descent.

## 1. A generic level avoids the finite exceptional data

All topology in this note has rational coefficients. Write

\[
D=D_1\cup\cdots\cup D_r,\qquad
E_{\mathrm{out}}=E\setminus D.
\]

Coprimality of \(A_0,B_0\) makes \(E\) finite. This includes the
case where one normalized coefficient is zero: the other is then
a nonzero constant and \(E\) is empty.

Choose a general value \(\lambda\) such that
\(X=F^{-1}(\lambda)\) is smooth and rationally acyclic, and also:

- \(\lambda\notin C(E)\);
- \(\lambda\notin C(\operatorname{Sing}D)\);
- it differs from the constant value of \(C\) on any component
  where that restriction is constant;
- the nonconstant restrictions \(C|_{D_i}\) have their generic
  finite, transverse fibers at \(\lambda\).

Only finitely many further values are excluded. Put

\[
T=D\cap V(C-\lambda).
\]

This is a finite reduced set in the smooth locus of \(D\), disjoint
from \(E\). At this stage some components \(D_i\) might have no
point in \(T\); the residue map will rule that out.

Let \(\pi:X\to\mathbb A^2\) be projection onto the base. Its closed
part over the coefficient-zero set is

\[
Z=\pi^{-1}(D)=T\times\mathbb A^2_{u,z}.
\tag{3}
\]

There is no point of \(X\) over \(E_{\mathrm{out}}\), because
there \(A=B=0\) but \(C\ne\lambda\). The open complement is thus
an affine-line bundle

\[
U=X\setminus Z\ \longrightarrow\
W=\mathbb A^2\setminus(D\cup E_{\mathrm{out}}).
\tag{4}
\]

It is Zariski locally trivial: on \(A\ne0\) solve for \(u\),
and on \(B\ne0\) solve for \(z\). No global section, relative
coordinate, or principal coefficient ideal is asserted. An
affine-line bundle is a topological bundle with contractible fiber,
so (4) induces cohomology isomorphisms.

Every component \(Z_t=\{t\}\times\mathbb A^2\) is a smooth
closed divisor in the smooth threefold \(X\), and these components
are disjoint. If \(h_i\) is a reduced equation of \(D_i\), the
scheme cut out in \(X\) by \(h_i=0\) is

\[
\operatorname{Spec}
\bigl(\mathbb C[x,y]/(h_i,C-\lambda)\bigr)[u,z].
\tag{5}
\]

Generic transversality makes (5) reduced. Hence \(h_i\) has
vanishing order one along every \(Z_t\) above \(D_i\), even when
that component occurs with higher multiplicity in \(g\).

## 2. What Gysin forces on the base complement

The ordinary Gysin sequence for the smooth divisors \(Z\subset X\)
contains

\[
H^k(X)\longrightarrow H^k(U)
\longrightarrow H^{k-1}(Z)
\longrightarrow H^{k+1}(X).
\]

Rational acyclicity of \(X\) and the fact that \(Z\) is a disjoint
union of affine planes give

\[
H^1(W)\simeq H^1(U)\simeq H^0(Z)=\mathbb Q^{|T|},
\qquad H^k(W)=0\quad(k\ge2).
\tag{6}
\]

This is stronger than Euler characteristic alone.

Let \(S=D\sqcup E_{\mathrm{out}}\), a closed reduced subset of
\(\mathbb A^2\). The compact-support closed-open sequence, using
\(H_c^j(\mathbb A^2)=0\) for \(j<4\), gives

\[
H_c^j(S)\simeq H_c^{j+1}(W)\qquad(j=0,1,2).
\]

Poincaré duality on the smooth real four-manifold \(W\) therefore
identifies, up to vector-space duality,

\[
H^3(W)\ \leftrightarrow\ H_c^0(S)
=\mathbb Q^{|E_{\mathrm{out}}|},
\qquad
H^2(W)\ \leftrightarrow\ H_c^1(D).
\tag{7}
\]

Every connected component of the affine curve \(D\) is noncompact,
so it contributes nothing to \(H_c^0(S)\). Equations (6) and (7)
prove

\[
E_{\mathrm{out}}=\varnothing,\qquad H_c^1(D)=0.
\tag{8}
\]

They also give \(\dim H^1(W)=r\), because
\(H_c^2(D)=\mathbb Q^r\), one top-dimensional fundamental class
per irreducible component.

## 3. Normalization removes intersections, but not yet cusps

Let \(\nu:\widetilde D\to D\) be the finite normalization. At a
singular point \(s\), let \(b_s\) be its number of local branches.
The quotient of \(\nu_*\mathbb Q_{\widetilde D}\) by
\(\mathbb Q_D\) is a skyscraper sheaf of rank \(b_s-1\) at \(s\).
Since \(H_c^0(D)=H_c^0(\widetilde D)=0\), its compact-support
sequence gives

\[
0\longrightarrow
\bigoplus_s\mathbb Q^{b_s-1}
\longrightarrow H_c^1(D)
\longrightarrow H_c^1(\widetilde D)
\longrightarrow0.
\tag{9}
\]

By (8), every \(b_s=1\) and \(H_c^1(\widetilde D)=0\).
In particular, different irreducible components of \(D\) do not
meet. Each normalization component is a smooth connected affine
curve with \(H_c^1=0\), hence has genus zero and one point at
infinity. Thus

\[
\widetilde D_i\simeq\mathbb A^1.
\tag{10}
\]

This does not yet prove that \(D_i\) is smooth. A cuspidal affine
line has the topology in (10) and is unibranch. The next residue
calculation is the step that excludes such singularities.

## 4. Residues make the normalization an isomorphism

The classes of the maps \(h_i:W\to\mathbb C^*\) form a basis
of \(H^1(W)\). Their independence is detected by small meridians
at smooth points of the different \(D_i\), and their number is
the dimension \(r\) computed above.

Under the isomorphism in (6), the class of \(h_i\) maps to
the vector equal to one on \(Z_t\) for \(t\in T\cap D_i\),
and zero on the other components. This is the usual winding-number
description of the Gysin residue; its coefficient is one by (5),
not the multiplicity of \(D_i\) in \(g\).

Thus the residue matrix is the component-incidence matrix

\[
\mathbb Q^r\longrightarrow\mathbb Q^{|T|},
\qquad e_i\longmapsto\sum_{t\in T\cap D_i} e_t.
\tag{11}
\]

Because (11) is an isomorphism, every component \(D_i\) contains
exactly one point of the generic set \(T\). A missing component
would give a zero column; two points on one component would leave
a nonconstant vector on those points outside the image.

Pull back \(C\) to the normalization
\(\widetilde D_i=\mathbb A^1_t\). It is a polynomial in \(t\)
with exactly one point in its generic fiber, so it has degree one.
Consequently

\[
\mathbb C[t]=\mathbb C[\nu^*C]
\subseteq\mathbb C[D_i]\subseteq\mathbb C[t].
\]

Both inclusions are equalities. The normalization map is therefore
an isomorphism, and \(C|_{D_i}\) is an affine coordinate. This
proves that the original components, not just their normalizations,
are disjoint embedded affine lines.

For a useful check of this distinction, the cusp
\(D=V(y^2-x^3)\) has \(H_c^1(D)=0\). Its normalization is
\((x,y)=(t^2,t^3)\). The restriction \(C=x\) has two generic
preimages, so its residue matrix would be
\(\mathbb Q\to\mathbb Q^2,\ 1\mapsto(1,1)\), which is not an
isomorphism. The compact-support vanishing alone would miss this
obstruction.

## 5. Rectifying the reduced divisor

Plane-line rectification sends \(D_1\) to \(a=0\). This theorem is
stated, in the exact embedded-affine-line form needed here, in
[Nguyen Van Chau, Section 2, before Lemma
1](https://math.ac.vn/uploads/files/0202197.pdf).

Every other \(D_i\) is disjoint from \(a=0\). Its restriction of
\(a\) is an invertible regular function on \(\mathbb A^1\), hence
a nonzero constant \(\alpha_i\). Since \(D_i\) is a closed
irreducible curve contained in \(a=\alpha_i\), it is that full
line. Distinct components give distinct constants.

Including the original factor multiplicities gives \(g=p(a)\),
up to a nonzero constant. In base coordinates \(a,b\), the result
of Section 4 says precisely that \(C(\alpha_i,b)\) is
affine-linear with nonzero slope. This proves (1).

## 6. Residual points on the divisor really can remain

The polynomial

\[
F=x^2u+xyz+y
\tag{12}
\]

is a coordinate, but

\[
g=x,\quad (A_0,B_0)=(x,y),\quad E=\{(0,0)\}\subset D.
\]

In particular, \((A,B)=(x^2,xy)=x(x,y)\) is not the principal
ideal \((x)\). Its scheme structure has an embedded point on the
divisor, while its reduced support is just the line.

An explicit completion, retaining \(x,z\), is

\[
T=-(1-xz)u+z^2y.
\]

Indeed,

\[
x^2z^2+(1+xz)(1-xz)=1,
\]

and the inverse formulas are

\[
u=z^2F-(1+xz)T,\qquad
y=(1-xz)F+x^2T.
\tag{13}
\]

Thus no proof may replace (2) by \(E=\varnothing\), or replace
the ideal \((A,B)\) by its gcd ideal.

## 7. Every level is an affine-plane fibration over the base line

Use the base coordinates of (1), and fix any \(\lambda\in\mathbb C\).
Set

\[
R_\lambda=\mathbb C[a,b,u,z]/(F-\lambda).
\]

At \(a=\alpha\), a root of \(p\), both linear coefficients
vanish and the remainder is \(c_\alpha b+d_\alpha-\lambda\).
Therefore

\[
R_\lambda/(a-\alpha)R_\lambda\simeq\mathbb C[u,z].
\tag{14}
\]

At \(a=\gamma\) with \(p(\gamma)\ne0\), (2) implies that
\(A(\gamma,b),B(\gamma,b)\) have no common zero. They generate
the unit ideal in the PID \(\mathbb C[b]\). Choose \(P,Q\)
with \(AP+BQ=1\) after this specialization. Then

\[
L=Au+Bz,\qquad T=-Qu+Pz
\]

are coordinates over \(\mathbb C[b]\), with inverse

\[
u=PL-BT,\qquad z=QL+AT.
\]

The equation \(F-\lambda=0\) becomes
\(L=\lambda-C(\gamma,b)\), so this level of \(a\) is also
\(\mathbb A^2\).

The generic row over \(\mathbb C(a)[b]\) is unimodular as well:
its gcd is the image of \(p(a)\), a unit, by Gauss's lemma.
Equivalently, (2) and the Nullstellensatz give
\(p^N\in(A_0,B_0)\) for some \(N\), so the normalized row is
already unimodular after inverting \(p\). The same completion
proves

\[
R_\lambda\otimes_{\mathbb C[a]}\mathbb C(a)
\simeq\mathbb C(a)^{[2]}.
\tag{15}
\]

There is no flatness assumption hidden here. In
\(\mathbb C[a,b]\),

\[
\gcd(A,B,C-\lambda)=\gcd(p(a),C-\lambda)=1,
\]

because no \(a-\alpha\) divides the nonconstant affine-linear
specialization \(C(\alpha,b)-\lambda\). Hence the total-linear
polynomial \(Au+Bz+C-\lambda\) is primitive and irreducible
over the fraction field, and Gauss's lemma makes it irreducible
in the polynomial UFD. Its quotient \(R_\lambda\) is a domain.

The nonzero generic localization in (15) makes
\(\mathbb C[a]\to R_\lambda\) injective. The domain
\(R_\lambda\) is then torsion-free, hence flat over this PID.
It is finitely presented, and (14), the nonroot calculation, and
(15) check the polynomial fiber at every prime of \(\mathbb C[a]\).
It is therefore an \(\mathbb A^2\)-fibration.

Sathaye's DVR theorem and Bass--Connell--Wright globalization give

\[
R_\lambda\simeq\mathbb C[a]^{[2]}.
\tag{16}
\]

The combined PID statement is explicitly recorded in
[Babu and Das, *Structure of A2-fibrations having fixed point free
locally nilpotent derivations*, the discussion between Problem
4.6 and Theorem 4.7](https://arxiv.org/html/2001.07632v5).
Their Section 1 defines the affine-fibration hypotheses used here,
and Theorem 2.2 records the globalization input. No LND relative
to \(\mathbb C[a]\) is required for this PID consequence.

## 8. The known coordinate endpoint and the independent slice check

In the notation of KVZ Theorem 3.24, take
\(d=g,\ a=A_0,\ b=B_0,\ c=C\). Its condition (v') is precisely
univariate \(g\), coprimality \(\gcd(g,C)=1\), the inclusion
\(V(A_0,B_0)\subseteq V(g)\), and a nonconstant affine-linear
restriction of \(C\) on every root line of \(g\).
Coprimality follows from (1), so every part was established above.
The equivalence (v') \(\Rightarrow\) (iv') gives that \(F\) is
a variable over the rectified base-coordinate ring
\(\mathbb C[a]\). This is the exact published endpoint in
[KVZ, *Simple birational extensions of the polynomial algebra
\(\mathbb C^{[3]}\)*, Theorem 3.24, printed pp. 37--38](https://arxiv.org/pdf/math/0104204).

There is also the following independent original-slice check using
the level-ring calculation, without the final equivalence of KVZ.

If an LND \(\delta\) on
\(S=\mathbb C[x,y,u,z]\) satisfies \(\delta(F)=1\), the slice
theorem gives

\[
S=(\ker\delta)[F],\qquad
\ker\delta\simeq S/(F)\simeq\mathbb C^{[3]}
\]

by (16). Choosing three polynomial generators of the kernel
completes \(F\) to a coordinate system of \(S\). The slice theorem
is recalled in [Babu and Das, Section
1](https://arxiv.org/html/2001.07632v5).

This conclusion does not require \(\delta(a)=0\): the
affine-plane fibration was established on the level ring, and
the original slice decomposition transports that ring to the kernel.

The level-ring argument by itself would not produce an original
slice from mere stability. Here that limitation does not leave the
family unresolved: the separate, exact KVZ coefficient criterion
already supplies the coordinate completion. Relative coordinatehood
is a conclusion of that theorem after rectifying \(D\), not an
assumption about the original \(x,y\). Principality of \((A,B)\)
is neither assumed nor concluded.
