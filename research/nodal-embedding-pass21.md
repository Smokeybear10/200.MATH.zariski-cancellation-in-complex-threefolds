# Global embedding tests for the conductor surface

This pass does not produce or exclude a closed embedding of the
[pass-20 conductor surface](nodal-conductor-pass20.md) into
\(\mathbb A^3\). It computes three genuinely global invariants:
the normalization is two-generated as a module, the conductor is
two-generated as an ideal, and rank and determinant classify its
\(K_0\) classes. In particular, the stable cotangent obstruction
vanishes. These calculations close specific obstruction attempts,
not the embedding problem or the stronger ambient quotient problem.

All rings below are over \(\mathbb C\). This is a written working
proof, with source-dependent steps identified explicitly. There is
no priority claim or formal proof-assistant verification.

## 1. The exact surface in scope

Fix \(a^4=3\), and set
\[
w_1=a,\quad w_2=-a,\quad w_3=ia,\quad w_4=-ia,
\qquad d=w^4-3,\qquad A=(w-w_1)(w-w_3).
\]
The normalization is the smooth affine surface
\[
B=\mathbb C[w,y,z]/(Az-y(y-1)).
\]
Its six lines over \(d=0\) are paired as
\[
(L_{10},L_{30}),\qquad(L_{11},L_4),\qquad(L_2,L_{31}).
\]
Here \(L_{j\epsilon}\) has \(w=w_j,y=\epsilon\), while
\(L_2,L_4\) are the unsplit fibers. Their common line parameters
in each pair are exactly those of the predecessor note:
\(t=z/[w_j(2\epsilon-1)]\) on a split line and
\(t=y/[w_jA(w_j)]\) on an unsplit line. Put
\[
D_0=B/dB\cong\mathbb C[t]^6,\qquad
C_0=\mathbb C[t]^3,\qquad
R=B\times_{D_0}C_0,
\tag{1}
\]
with \(C_0\) embedded pairwise diagonally. The conductor is
\(I=dB\), and \(R/I=C_0\).

The predecessor establishes that \(R\) is a finite-type integral
surface ring, its normalization is \(B\), its singularities have
completed local equation \(\xi\zeta=0\), and its dualizing sheaf
is trivial. Those statements, including the scaled line gluing,
are retained without changing the surface.

## 2. The global conductor-generator test fails

There is an exact module identity
\[
B=R+Rw.
\tag{2}
\]
To prove it, take any \(b\in B\). On a paired line set over
\(w_i,w_j\), write its two residues as \(b_i(t),b_j(t)\).
Because \(w_i\ne w_j\), there are unique polynomials
\[
c_1(t)=\frac{b_i(t)-b_j(t)}{w_i-w_j},\qquad
c_0(t)=b_i(t)-w_ic_1(t)
\]
with residues \((c_0+w_ic_1,c_0+w_jc_1)\).
Doing this for all three pairs gives \(c_0,c_1\in C_0\).
The map \(R\to C_0\) is surjective, so lift them to
\(r_0,r_1\in R\). Then \(b-r_0-r_1w\in dB\subset R\),
which proves (2). Consequently
\[
I=(d,dw)R.
\tag{3}
\]
At a conductor point, its completed ideal is
\((\xi,\zeta)\subset\mathbb C[[\xi,\zeta,t]]/(\xi\zeta)\).
Its minimal number of generators is two, so (3) is optimal.

There is also an exact sequence
\[
0\longrightarrow R\longrightarrow B
 \longrightarrow R/I\longrightarrow0.
\tag{4}
\]
Indeed \(w\bmod R\) generates \(B/R\) by (2), and its
annihilator is exactly \(I\): the two residues of \(rw\) agree
precisely when \((w_i-w_j)\bar r=0\) in each pair, which forces
\(\bar r=0\).

These are global module statements, not just local generator counts.
They invalidate an obstruction based on requiring more than two
conductor generators. They do not say that \(R\) has three
algebra generators. Also, \(B/R\) being cyclic does not make
\(\operatorname{Frac}(B)/\operatorname{Frac}(R)\) quadratic;
that fraction-field extension is the identity.

## 3. The Picard group can be computed exactly

First,
\[
B^*=\mathbb C^*,\qquad\operatorname{Pic}(B)\cong\mathbb Z^2.
\tag{5}
\]
Here is an elementary divisor calculation. The localization
\(B_A=\mathbb C[w,A^{-1},y]\) is factorial, with units
\(c(w-w_1)^e(w-w_3)^f\). Its complement has the four prime
divisors \(L_{10},L_{11},L_{30},L_{31}\). Their classes generate
\(\operatorname{Cl}(B)\): any divisor becomes principal after
localizing, so subtracting that principal divisor leaves support
in these four lines. The only relations are
\[
[L_{10}]+[L_{11}]=0,\qquad
[L_{30}]+[L_{31}]=0.
\tag{6}
\]
For a principal divisor supported in those four lines, its defining
rational function is a unit of \(B_A\); the displayed unit list
gives exactly (6). The same valuation calculation forces \(e=f=0\)
for a unit of \(B\). Finally, \(B\) is smooth, so Weil and
Cartier divisor classes agree, proving (5).

Apply the Units–Pic exact sequence to the actual Milnor square
(1).[^1] Both \(C_0\) and \(D_0\) have trivial Picard group,
and their units are \((\mathbb C^*)^3\) and
\((\mathbb C^*)^6\). The image of
\(B^*\times C_0^*\to D_0^*\) is the pairwise diagonal
subgroup; the common constant from \(B^*\) adds nothing.
Therefore
\[
0\longrightarrow(\mathbb C^*)^3
 \longrightarrow\operatorname{Pic}(R)
 \longrightarrow\mathbb Z^2\longrightarrow0.
\tag{7}
\]
As an abstract abelian-group sequence it splits because
\(\mathbb Z^2\) is free. Thus, noncanonically,
\[
\operatorname{Pic}(R)\cong(\mathbb C^*)^3\oplus\mathbb Z^2.
\tag{8}
\]
No assertion about a Picard scheme or a preferred splitting is intended.

Nonzero Picard group is not an obstruction to a hypersurface
embedding: \(B\) itself is a smooth hypersurface in
\(\mathbb A^3\) with Picard group \(\mathbb Z^2\).
Likewise, the product of an affine nodal plane curve with
\(\mathbb A^1\) is a hypersurface with a \(\mathbb C^*\)
gluing contribution, by the same conductor-square calculation.
The node calculation also appears explicitly in Weibel's
Example I.3.10.2.[^1] No restriction excluding the combination
in (8) has been established here.

## 4. The stable cotangent obstruction also vanishes

Write \(SK_0(S)=\ker(\operatorname{rank}\oplus\det)\) for
a connected ring \(S\). We first have
\[
SK_0(B)=0.
\tag{9}
\]
For a regular surface, \(K_0=G_0\), and \(SK_0\) is generated
by the classes of its closed points.[^2] Every closed point of
\(\operatorname{Spec}B\) lies on a closed reduced affine-line
component of a fiber of \(w\). On such a line, with coordinate
\(q\), the exact sequence
\[
0\longrightarrow\mathbb C[q]
 \xrightarrow{q-q_0}\mathbb C[q]
 \longrightarrow\mathbb C\longrightarrow0
\]
shows that the point has zero class in \(G_0\). The closed
immersion of the line pushes this exact sequence to \(B\), so
each point class in \(G_0(B)\) is zero. This proves (9).

Now the Milnor square gives the exact segment[^3]
\[
K_1(B)\oplus K_1(C_0)\longrightarrow K_1(D_0)
 \xrightarrow{\partial}K_0(R)
 \longrightarrow K_0(B)\oplus K_0(C_0).
\tag{10}
\]
The Euclidean algorithm gives \(K_1(\mathbb C[t])=\mathbb C^*\),
so \(K_1(D_0)=D_0^*\). Let \(v\in SK_0(R)\).
Its image in \(K_0(B)\) vanishes by (9); its image in
\(K_0(C_0)=\mathbb Z^3\) vanishes because its rank on every
component is zero. Thus \(v=\partial u\) for \(u\in D_0^*\).

The determinant of \(\partial u\) is precisely the line bundle
patched by \(u\), up to the harmless common boundary-sign
convention. Since \(\det v\) is trivial, the Units–Pic sequence
puts \(u\) in the image of \(B^*\times C_0^*\). Such units
also lie in the image of the first map of (10). Hence \(v=0\).
Rank and determinant are always jointly surjective, using free
modules and \([L]-[R]\). We have therefore proved
\[
SK_0(R)=0,\qquad
K_0(R)\xrightarrow{\operatorname{rank}\oplus\det}
 \mathbb Z\oplus\operatorname{Pic}(R)
\text{ is an isomorphism of abelian groups.}
\tag{11}
\]
No vanishing assumption on \(SK_1(B)\) was used.

Because \(R\) is a local complete intersection over \(\mathbb C\),
its cotangent complex \(L_{R/\mathbb C}\) is perfect of amplitude
\([-1,0]\).[^4] For any polynomial presentation
\(P=\mathbb C[x_1,\ldots,x_N]\twoheadrightarrow R\), with
kernel \(J\), it is represented by
\[
[J/J^2\longrightarrow R^N],
\]
where \(J/J^2\) is projective of rank \(N-2\). The local
Koszul resolution identifies its determinant with the dualizing
module: both are
\(\det(R^N)\otimes\det(J/J^2)^{-1}\). The predecessor's
opposite-residue construction gives \(\omega_R\cong R\).
Therefore the rank of this perfect complex is two and its
determinant is trivial. Equation (11) gives the global identity
\[
[L_{R/\mathbb C}]=2[R]\quad\text{in }K_0(R).
\tag{12}
\]
An actual hypersurface in \(\mathbb A^3\) has the same class,
from its complex \([R\to R^3]\). Thus this necessary stable
cotangent test cannot rule out the embedding. Equality (12) is
not a three-generated presentation of \(\Omega_{R/\mathbb C}\),
an identification of complexes with a hypersurface complex, or
a proof of any embedding.

## 5. The exact missing global statement

For this particular \(R\), the embedding question is equivalent
to the existence of \(g_1,g_2,g_3\in R\) with
\[
R=\mathbb C[g_1,g_2,g_3].
\tag{13}
\]
Indeed a resulting surjection from a three-variable polynomial
ring has a nonzero height-one prime kernel, which is principal.
Conversely, a closed embedding supplies these three generators.
The conductor singularities show that fewer than three cannot
suffice. This pass supplies neither a triple satisfying (13)
nor an invariant proving that every such triple fails.

In particular, replacing the two module generators in (2) by
two algebra coordinates, or replacing (12) by a free conormal
presentation of codimension one, would introduce an unjustified
step. Picard and \(K_0\) computations do not authorize either
replacement.

Even a successful (13) would only embed this one surface as
some hypersurface in \(\mathbb A^3\). It would not construct
two disjoint exceptional hypersurfaces, extend its LND to a
primitive LND on \(\mathbb C^{[3]}\), or construct the required
quotient with nodal cubic plinth support. Those are strictly
stronger compatibility requirements. No properness, tameness,
or connectedness theorem for a nonproper affine fiber has been
assumed in this pass.

## Source and verification boundary

The normalization, pinching, local complete-intersection property,
and trivial dualizing module come from the complete written
pass-20 construction, which was reread. The present module,
divisor, point-class, and diagram-chase arguments are explicit
global deductions for that same ring. No numerical experiment
is being used to establish an unrestricted algebra statement.
The primary author references actually read for the new arguments
are the precise passages below; no theorem about all hypersurface
embeddings or all affine \(\mathbb G_a\)-surfaces is imported.

[^1]: Charles Weibel, [*The K-book*, Chapter I](https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.I.pdf), Theorem 3.10 and its full proof, printed p. 22; Example 3.10.2, printed p. 23. The former applies to an arbitrary Milnor square, including (1), not just a normal or smooth ring.

[^2]: Weibel, [*The K-book*, Chapter II](https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.II.pdf), Theorem 8.2, printed p. 76, and Example 8.2.2, printed p. 77; also the rank-and-determinant discussion, Theorem 8.1. The regularity hypothesis is used only for the smooth normalization \(B\), not the singular ring \(R\).

[^3]: Weibel, [*The K-book*, Chapter III](https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.III.pdf), Theorem 2.6 and its full proof, printed p. 15; Example 1.3.5, printed p. 4. This is the Milnor-square exact sequence of projective-module \(K\)-theory, not an asserted normalization-excision statement for all higher \(K\)-groups.

[^4]: The Stacks Project, [the cotangent complex of a local complete intersection, Proposition 92.14.4](https://stacks.math.columbia.edu/tag/08SH), statement and proof. The finite polynomial presentation, projectivity of its conormal module, and amplitude are precisely the assertions used here. The determinant identification is the local Koszul duality calculation described in the text.
