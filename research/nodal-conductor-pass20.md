# A nodal surface realization through its conductor

The four-branch intermediate curve and three-component node fiber are
compatible with an actual integral affine surface carrying a nonzero
locally nilpotent derivation. The surface constructed below is locally
a hypersurface, has three disjoint singular affine lines, has trivial
dualizing sheaf, and has exactly the compact-support cohomology required
in pass 19. Thus these surface-level conditions do not exclude the
candidate. A global embedding as the required exceptional hypersurface
in a primitive quotient of affine three-space is still missing.

This is a working construction with a written proof and exact algebraic
controls. It is not a claim of priority or an actual nodal plinth on
\(\mathbb C^{[3]}\).

## 1. The conditions being tested

The [pass-19 surface note](nodal-surface-constraints-pass19.md) deduced
the following requirements for the proposed degree-two intermediate
data above \(\Gamma_+:v^2-u^3+3u=2\): four normalization points
above its node, one intermediate point, and three disjoint contractible
components of the actual node fiber. The exceptional surface must be
irreducible and reduced, singular along that entire fiber, and satisfy
\(H_c^3=H_c^4=\mathbb Z\), with the other compact-support groups zero.
These are conditional deductions from Kaliman's quotient and excision
results, not a realization theorem.[^1]

The construction here supplies an actual surface and action with those
properties. Local complete intersection and trivial dualizing sheaf
are additional tests, since a hypersurface in affine three-space has
both properties. Neither is sufficient to supply that global embedding.

## 2. A smooth normalization with six distinguished lines

Fix \(a\in\mathbb C\) with \(a^4=3\), and write
\[
w_1=a,\quad w_2=-a,\quad w_3=ia,\quad w_4=-ia,
\qquad d(w)=w^4-3,\qquad A(w)=(w-w_1)(w-w_3).
\]
Let
\[
B=\mathbb C[w,y,z]/\bigl(A(w)z-y(y-1)\bigr),
\qquad \widetilde E=\operatorname{Spec}B.
\tag{1}
\]
This ring is a domain: the defining polynomial is primitive and linear
in \(z\), with coprime coefficient and constant term. The surface is
smooth. Where \(A\ne0\), eliminate \(z\); where \(A=0\), the
equation gives \(y=0\) or \(1\), so the derivative with respect to
\(y\) is nonzero. In particular \(B\) is normal.

The divisor \(\widetilde L=V(d)\) consists of six disjoint affine
lines. The fibers at \(w_1,w_3\) each have two components,
distinguished by \(y=0,1\); the fibers at \(w_2,w_4\) have one
component each. Use the following pairings:

| Pair | First line | Second line |
| --- | --- | --- |
| 1 | \(w=w_1,y=0\) | \(w=w_3,y=0\) |
| 2 | \(w=w_1,y=1\) | \(w=w_4\) |
| 3 | \(w=w_2\) | \(w=w_3,y=1\) |

For a line at a split fiber \(w=w_j,y=\epsilon\), put
\(\tau=z/(2\epsilon-1)\). At either ordinary distinguished fiber
put \(\tau=y/A(w_j)\). In every case identify the line with
\(\mathbb A^1_t\) by
\[
t=\tau/w_j.
\tag{2}
\]
The factors \(w_j\) in this gluing are important for the dualizing
calculation below.

## 3. The affine pinch and its exact conductor

Because \(d\) is squarefree and the listed fibers are reduced,
\[
B/dB\cong\prod_{\ell=1}^{6}\mathbb C[t].
\]
Embed \(C_0=\mathbb C[t]^3\) in this product by repeating the same
polynomial on the two members of each pair, and define
\[
\mathcal R=B\times_{B/dB}C_0
 =\{b\in B:\text{its two restrictions agree in each pair}\},
\qquad E=\operatorname{Spec}\mathcal R.
\tag{3}
\]
This is an integral affine surface of finite type. Indeed the quotient
map from \(B\) is surjective and \(B/dB\) is finite over \(C_0\).
The affine fiber-product finite-generation lemma applies; it also
shows that \(B\) is finite over \(\mathcal R\). This is an affine
Ferrand pinch, so it makes precisely the three specified line-pair
identifications.[^2]

Since \(dB\subset\mathcal R\) and \(d\in\mathcal R\),
\(\mathcal R_d=B_d\). Therefore their fraction fields coincide,
and \(B\) is exactly the normalization of \(\mathcal R\).
The conductor is exactly
\[
\mathfrak c=dB\subset\mathcal R.
\tag{4}
\]
To see equality, reduce modulo \(dB\). The conductor of a diagonal
copy of \(\mathbb C[t]\) in \(\mathbb C[t]\times\mathbb C[t]\)
is zero: multiplying \((h,h)\) by \((1,0)\) forces \(h=0\).
Apply this to each pair. Thus the conductor downstairs is
\(L=\operatorname{Spec}C_0\), three disjoint affine lines.

At every closed point of \(L\), the two normalization preimages
are smooth surface points on smooth Cartier curves. Completion of
the fiber product gives
\[
\widehat{\mathcal O}_{E,q}
 \cong \mathbb C[[\xi,t]]\times_{\mathbb C[[t]]}
             \mathbb C[[\zeta,t]]
 \cong\mathbb C[[\xi,\zeta,t]]/(\xi\zeta).
\tag{5}
\]
Consequently \(E\) is locally a complete intersection and Gorenstein,
and its singular locus is exactly \(L\). Its global irreducibility
does not prevent these two formal branches at a singular point.

## 4. An actual locally nilpotent derivation and its invariant curve

On \(B\), take
\[
\delta(w)=0,\quad\delta(y)=A(w),\quad\delta(z)=2y-1,
\qquad \partial=w\delta.
\tag{6}
\]
The relation is killed; the triangular formulas show local nilpotence.
On every distinguished line, \(\delta\tau=1\), so
\(\partial t=1\). Thus the derivation induced on \(B/dB\)
preserves \(C_0\), and \(\partial\) restricts to a nonzero LND
on \(\mathcal R\). This checks descent on the actual ring; mere
preservation of the conductor's support would not suffice.

The kernel in \(B\) is \(\mathbb C[w]\). Localization at \(A\)
reduces this to a polynomial translation, and the section
\(y=z=0\) shows \(B\cap\mathbb C(w)=\mathbb C[w]\).
Multiplication of the derivation by nonzero \(w\) does not change
its kernel. The pairing graph is connected on the four vertices
\(w_j\), so an invariant polynomial belongs to \(\mathcal R\)
exactly when its four values coincide. Hence
\[
\ker(\partial|_{\mathcal R})
 =T=\mathbb C+d\mathbb C[w]
 =\mathbb C[d,dw,dw^2,dw^3].
\tag{7}
\]
The quotient \(\kappa:E\to Z=\operatorname{Spec}T\) has three
disjoint lines above the point obtained by identifying the four
\(w_j\). Elsewhere its fibers are affine lines. The action is
nonzero on every conductor line. It has the fixed affine line
\(w=0\), which lies off the conductor.

There is a finite morphism \(\theta:Z\to\Gamma_+\) defined by
\[
u=w^4-2=d+1,\qquad v=(w^4-3)w^2=dw^2.
\tag{8}
\]
Its normalized map is \(w\mapsto w^2\), since the normalization
parameter on \(\Gamma_+\) is \(u=s^2-2,v=s(s^2-3)\).
Finiteness follows from \(w^4=u+2\) and the fact that \(T\) is
a submodule of the finite base module \(\mathbb C[w]\).
It has generic degree two, one intermediate point over the node,
and four unramified normalization branches there. Thus
\(E\to Z\to\Gamma_+\) realizes the earlier curve data on an
actual affine LND surface.

The reduced fiber over the node is exactly \(L\). In fact it is
scheme-theoretically reduced here: on the two branches in (5),
\(u-1=d\) has simple zeros, while \(v/d\) has distinct limiting
values \(w_i^2=\sqrt3\) and \(w_j^2=-\sqrt3\). The two
functions generate \((\xi,\zeta)\) in the completed local ring.

## 5. The compact-support groups match

The common open complement is
\[
E\setminus L\cong\widetilde E\setminus\widetilde L
\cong(\mathbb A^1\setminus\{w_1,w_2,w_3,w_4\})\times\mathbb A^1.
\]
Its only nonzero compact-support cohomology groups are
\(H_c^3=\mathbb Z^4\) and \(H_c^4=\mathbb Z\).
The closed three-line conductor has only \(H_c^2=\mathbb Z^3\).
Their exact sequence becomes
\[
0\longrightarrow H_c^2(E)\longrightarrow\mathbb Z^3
 \xrightarrow{N}\mathbb Z^4\longrightarrow H_c^3(E)
 \longrightarrow0,
\quad
N=\begin{pmatrix}
1&1&0\\0&0&1\\1&0&1\\0&1&0
\end{pmatrix}.
\tag{9}
\]
For clarity, this is an actual connecting map, not a guessed rank
condition. Pull back the closed/open sequence along the finite
normalization. On each conductor line this duplicates its class onto
its two preimage lines. On the smooth normalization each line maps
to the positive puncture generator for its \(w_j\), with coefficient
one because that normalized fiber is reduced. Naturality gives the
three columns \(e_1+e_3,e_1+e_4,e_2+e_3\) in (9).

The matrix has rank three and its maximal minors are \(1,-1,-1,1\).
Its cokernel is therefore \(\mathbb Z\), without torsion. The rest
of the same exact sequence gives
\[
H_c^3(E,\mathbb Z)=H_c^4(E,\mathbb Z)=\mathbb Z,
\qquad H_c^j(E,\mathbb Z)=0\quad(j\ne3,4).
\tag{10}
\]

## 6. Trivial dualizing sheaf is also feasible

A nowhere-vanishing canonical form on the smooth normalization is
\[
\omega=\frac{dw\wedge dy}{A(w)}
       =\frac{dw\wedge dz}{2y-1},
\tag{11}
\]
using whichever denominator is nonzero. The open sets cover
\(\widetilde E\). Consider \(\Omega=\omega/d\), a form with
simple poles along the six conductor lines and no other poles or zeros.

Its residue on a line over \(w_j\), in the gluing coordinate (2), is
\[
\operatorname{Res}_{w_j}\Omega
 =\frac{w_j}{d'(w_j)}\,dt
 =\frac{1}{4w_j^2}\,dt.
\tag{12}
\]
Every paired line joins opposite values of \(w_j^2\). The two
residues therefore sum to zero in each pair. The double-normal-crossing
residue criterion shows that \(\Omega\) descends to a dualizing
section on \(E\).[^3] All its residues are nonzero constants, so
the section is a local generator at the conductor; it is already
nowhere vanishing off the conductor. Thus
\[
\omega_E\cong\mathcal O_E.
\tag{13}
\]
This is why gluing by the unscaled coordinate \(\tau\) was not
used: those residues would not cancel. The scaled gluing simultaneously
respects the action \(w\delta\) and the canonical form.

## 7. The remaining ambient issue is genuinely global

The new evidence rules out a proposed obstruction based only on
non-normality, local hypersurface singularities, trivial dualizing
sheaf, an actual surface LND, the stated fiber counts, or (10).
All of them hold in one concrete affine surface.

Even the two relevant local quotient behaviors have elementary
primitive three-dimensional models. At a double crossing use
\((\xi,\zeta,t)\mapsto(\xi,\zeta)\), with LND
\(\partial_t\), and pull back the nodal equation \(\xi\zeta=0\).
At the smooth point where the normalized cover \(w\mapsto w^2\)
ramifies, use
\[
(s,w,t)\longmapsto(s,w^2+st),\qquad
s\partial_w-2w\partial_t.
\tag{14}
\]
This LND is primitive because \(s\) and \(w\) are coprime;
its kernel is \(\mathbb C[s,w^2+st]\). Restriction to \(s=0\)
has the double-cover map and an LND vanishing along \(w=0\),
as in the surface construction, up to a nonzero local factor.
These are local compatibility models, not gluings into one affine
three-space quotient.

What remains is to construct or rule out a global embedding of this
kind of surface as \(\pi^{-1}(\Gamma_+)\subset\mathbb A^3\),
together with its disjoint partner over \(\Gamma_-\), the product
quotient complement, and one primitive ambient LND with invariant
ring \(\mathbb C[u,v]\). No three-generator presentation of
\(\mathcal R\), such embedding, or ambient quotient is asserted.
Nor is the proper Stein-factor connectedness statement applied to
the special fibers of its affine restriction.

## 8. Exact controls and source scope

SymPy exact arithmetic verified the nodal identity in (8), the rank
and all maximal minors in (9), and the three residue cancellations
in (12). These finite computations check displayed constants and
identities; the ring, normalization, descent, and cohomology arguments
are the proofs above.

[^1]: Shulim Kaliman, [*Free C+-actions on C3 are translations*, final author version](https://www.math.miami.edu/~kaliman/library/Ka.invent.2004.c%2B.pdf), Lemmas 2.1–2.2, Proposition 3.2, and Theorem 5.2. The quotient/Stein-factor passages were reread. Their hypotheses supply the conditional target through the pass-19 note; they are not assumed for the newly constructed surface as an ambient threefold.

[^2]: [Stacks Project, Lemma 15.5.1](https://stacks.math.columbia.edu/tag/08KG), and [Situation 37.67.1 and Proposition 37.67.3](https://stacks.math.columbia.edu/tag/0ECH), including their proofs. The closed immersion is the six-line conductor in the smooth affine surface; the finite morphism folds each line pair onto an affine line. All schemes are affine, so the stated affine-neighborhood hypothesis holds. This is the affine form of Ferrand's established pinching construction, not a new construction principle.

[^3]: János Kollár, [*Semi Log Canonical Pairs*, author chapter draft dated May 31, 2010](https://web.math.princeton.edu/~kollar/book/chap3.pdf), paragraph 8, equation (8.1), and Proposition 9, printed pp. 6–7. These passages and their local residue calculation were read. Only the double-normal-crossing dualizing formula and opposite-residue criterion are used, not a projective moduli or positivity theorem.
