# Quadratic-time flow boxes: the exact generic-degree obstruction

A published local straightening theorem for time-polynomial vector fields
does apply to the present sliced action. It gives a local holomorphic
inverse, not a global polynomial inverse. The algebraic flow box from an
actual coordinate hypersurface has generic degree exactly the flow degree
of that coordinate. In particular, a quadratic coordinate produces a
generic double cover. This supplies a precise missing premise, rather
than another classification claim.

The general degree lemma below is an elementary reconstruction in this
note. It is not attributed to the cited source or claimed novel. All
statements retain the original action and actual coordinate ring.

## 1. Input and selected primary result

Let
\[
B=\mathbb C[x_1,x_2,x_3,x_4],\qquad
E\in\operatorname{LND}_{\mathbb C}(B),\qquad E(s_*)=1,
\qquad E^3x_i=0.
\tag{1}
\]
Write \(P=Ex\), \(Q=E^2x\). Then
\[
\Phi_t(x)=x+tP(x)+\frac{t^2}{2}Q(x),\qquad E(Q_i)=0.
\tag{2}
\]
These are bounds in the action parameter, not in the spatial variables.
No adjoint bound on the original coordinate partials is assumed.

Cerveau, Déserti and Lins Neto define this as a *t-polynomial* vector
field. Proposition 4.2 says its top coefficient entries are first
integrals, by comparing the highest time coefficient of the group law.
Theorem 4.5 straightens a nonsingular germ by a holomorphic local
diffeomorphism polynomial in the time coordinate. Its proof takes the
flow from a transverse coordinate hyperplane. It does not assert a
global polynomial inverse. Theorem 4.8 bounds the time degree of a rigid
p-chambar by p−1.[^chambar]

Here the slice makes E nonsingular. If \(\zeta\) is a primitive cube
root of unity, (2) directly gives
\[
\Phi_t+\Phi_{\zeta t}+\Phi_{\zeta^2t}=3\operatorname{Id}.
\tag{3}
\]
Thus the rigid triple \((E,\zeta E,\zeta^2E)\) fits that terminology;
the time bound is recovered, not strengthened. This does not give three
independent vector fields. The source's one-variable and linear-field
classifications have different hypotheses and are not applied.

## 2. Exact generic degree of an actual coordinate flow box

This lemma works in \(B=\mathbb C^{[n]}\) for any LND E, without a
slice or a bound of two. Let \(\ell\) be an actual polynomial coordinate
of B with positive E-degree
\(m=\max\{j:E^j\ell\ne0\}\), and put \(H=V(\ell)\).
Consider the actual polynomial morphism
\[
\Psi:\mathbb A^1\times H\longrightarrow\operatorname{Spec}B,
\qquad (t,y)\longmapsto\Phi_t(y).
\tag{4}
\]
Then \(\Psi\) is dominant and generically finite of degree exactly m.

To prove this, extend E to \(B[T]\) with \(E(T)=0\). Both
\(\exp(TE)\) and \(\exp(-TE)\) are polynomial automorphisms of this
ring. The graph description of (4) gives an isomorphism of B-algebras
\[
\mathbb C[\mathbb A^1\times H]
\simeq B[T]/(G),\qquad
G=\exp(-TE)\ell
 =\sum_{j=0}^{m}\frac{(-T)^j}{j!}E^j\ell.
\tag{5}
\]
Explicitly, apply \(\exp(TE)\) and then reduce modulo \(\ell\).
The inverse description takes the transverse point to
\(y=\Phi_{-T}(x)\); its defining condition is precisely \(G=0\).

Since \(\ell\) is a coordinate, \((\ell)\) is prime in \(B[T]\).
Its image under an automorphism is prime, so G is irreducible in that
UFD. It has positive T-degree m. Therefore its content as a polynomial
over B is a unit: a nonunit content would be a proper factor of G.
Gauss's lemma now makes G irreducible in \(K[T]\), where
\(K=\operatorname{Frac}B\). Also \((G)\cap B=0\), by positive
T-degree. This proves the asserted dominance and the exact equality
\[
[\mathbb C(\mathbb A^1\times H):\operatorname{Frac}B]=m.
\tag{6}
\]
In characteristic zero this field extension is separable. This is a
generic-degree statement, not a claim that \(\Psi\) is finite or
étale everywhere.

For an affine coordinate \(\ell\), the differential of (4) at
\((0,y)\) has columns \(P(y)\) and a basis of \(T_yH\). Its
determinant, up to a nonzero constant, is \(E\ell(y)\).
This restriction is not identically zero. Otherwise
\(\ell\mid E\ell\), which for an LND forces \(E\ell=0\), contrary
to \(m>0\). One elementary proof is E-degree additivity: if
\(E\ell=f\ell\ne0\), then \(m-1=\deg_E f+m\), impossible.
Thus the source's local nonsingular flow-box construction really is
available on a nonempty open subset of H, even when \(m>1\).

## 3. Quadratic and linear controls with original global slices

On \(\mathbb C[x,y,z,w]\), take
\(E=\partial_x+2x\partial_y\), with original slice x. Its flow from
\(H=V(y)\) is
\[
\Psi(t,a,b,c)=(a+t,\,2at+t^2,\,b,\,c),\qquad
G=y-2Tx+T^2,\qquad a^2=x^2-y.
\tag{7}
\]
The determinant in the first two variables is \(-2a\), so local
holomorphic inverses exist near every point with \(a\ne0\).
Nevertheless (6) has degree two. The polynomial map is not a
polynomial automorphism and not even birational. The original action
is already a translation in \((x,y-x^2,z,w)\), so this is an
obstruction to the chosen flow-box construction, not to recognition.

Even m=1 alone does not supply a global inverse. On
\(\mathbb C[s,a,y,z]\), take \(E=\partial_s+a\partial_y\), with
slice s, and again use \(H=V(y)\). Then
\[
\Psi(t,s_0,a,z)=(s_0+t,a,at,z),\qquad G=y-aT.
\tag{8}
\]
This is birational, but it omits every point with \(a=0,y\ne0\).
Its inverse needs \(T=y/a\). A coordinate \(\ell\) with
\(E\ell\in\mathbb C^*\) would instead give the desired polynomial
inverse directly. That is a substantially stronger premise than
positive or unit generic flow degree.

In fact the exact criterion for (4) is
\[
\Psi\text{ is a global polynomial isomorphism}
\quad\Longleftrightarrow\quad E\ell\in\mathbb C^*.
\tag{9}
\]
For the forward direction, (6) first gives m=1. Put
\(g=E\ell\ne0\). An inverse over B makes T an element of B, and
the relation \(\ell-gT=0\) implies \(g\mid\ell\). The coordinate
\(\ell\) is irreducible. Thus g is a unit or is associated to
\(\ell\). The latter alternative contradicts LND self-divisibility,
as proved after (6). All units of B are nonzero constants. Conversely,
if g is such a constant, (5) eliminates T polynomially and gives the
claimed inverse. This criterion concerns the specified coordinate
hypersurface, not existence of some alternative coordinate slice.

The supplied slice \(s_*\) does give
\(\operatorname{Spec}B\simeq\operatorname{Spec}(\ker E)\times
\mathbb A^1\). But \(s_*\) has not been proved an ambient coordinate,
so its zero fiber cannot be replaced by \(\mathbb A^3\) in this
argument. Choosing a known coordinate hypersurface restores an actual
three-space source at the cost measured exactly by (6).

## 4. Applicability, deduplication and access

The [proper-action scope55](proper-quadratic-flow-scope-pass55.md),
[mixed-time addendum](mixed-time-degree-literature-addendum.md),
[mixed-flow audit](mixed-flow-literature-pass.md), and
[coordinate-degree scope58](coordinate-slice-degree-scope-pass58.md)
were read first. Their distinction between time degree, spatial
degree, relative polynomial presentations and actual coordinate
generation remains intact. In particular, the earlier exponential
minimal-polynomial theorem is not a global inverse theorem for (4).

The [acceleration control81](acceleration-field-obstruction-pass81.md)
separately tests why \(E(Q_i)=0\) cannot be promoted to local nilpotence,
niceness or commutation for \(\sum_iQ_i\partial_{x_i}\).
The [scalar-filter obstruction81](universal-slice-filter-obstruction-pass81.md)
addresses universal Taylor-filter degree lowering. Neither problem is
settled by calling (2) a rigid chambar. Those two notes have their own
proof-review provenance; this source note does not add a numerical run.

The freshly accessed primary selections are Definition 4.1,
Proposition 4.2, Theorem 4.5 and Theorem 4.8 with their complete
displayed proofs in v2. Theorem 4.3 and its proof were also read in the
contiguous selection; Theorem 5.1 was checked at statement scope only.
No whole-paper or deeper cited-dependency audit is claimed. The
published bibliographic record was checked, but the final journal
proof was not compared with v2. The unavailable attempted v3 HTML URL
for the separately retained de Bondt quasi-translation paper supplies
no new source input here.

Bounded searches covered time-polynomial vector fields, quadratic
additive flows, rigid chambars and acceleration coefficients. No
applicable global four-variable recognition theorem was established
by this search. This is not a novelty claim, an exhaustive literature
verdict, or evidence that the desired recognition is impossible.
No frozen file, shared metadata, numerical suite or capture was changed.

[^chambar]: Dominique Cerveau, Julie Déserti and Alcides Lins Neto,
[*Holomorphic vector fields with a barycentric condition*](https://arxiv.org/html/2206.06475v2),
arXiv:2206.06475v2, May 12, 2023. The
[primary version record](https://arxiv.org/abs/2206.06475)
lists *Publicacions Matemàtiques* **68** (2024), no. 1, 287–330;
the [author's publication list](https://dominique-cerveau.perso.math.cnrs.fr/)
agrees. Only the selected source statements and proofs listed above
were freshly checked; the generic-degree lemma and controls (4)–(9)
are proved here rather than attributed to that article.
