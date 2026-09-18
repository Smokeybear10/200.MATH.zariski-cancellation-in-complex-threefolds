# Quadratic coefficients, nice flow, and the exact published scope

The bounded source check finds a useful correction to the older
[nice-route inventory](nice-route.md): spatially quadratic **nice**
derivations on the actual complex polynomial four-ring are covered
by a published homogeneous triangularization theorem, followed by
an explicit homogenization and matrix descent. The old inventory's
quadratic Jacobian-rank-three search region should not be treated
as an unclassified region on the strength of that inventory.

This does not settle arbitrary spatially quadratic LNDs, arbitrary
nice four-variable LNDs, or universal cancellation. The exact source
access limitation for the additional theorem is recorded below.
Frozen files are not modified.

## 1. Hypotheses that must stay separate

Write
\[
B=\mathbb C[x_1,x_2,x_3,x_4],\qquad
E=\sum_i F_i\partial_{x_i},\qquad E(s_*)=1.
\tag{1}
\]
The displayed generators and the supplied slice are actual
polynomials. The following are different conditions:

| Condition | Meaning |
| --- | --- |
| Spatial degree at most two | \(\max_i\deg F_i\le2\). |
| Nice in this frame | \(E^2x_i=0\) for all \(i\), equivalently \(JF\,F=0\). |
| Coordinate flow degree at most two | \(E^3x_i=0\), which allows nonzero second iterates. |
| An adjoint-frame bound | An equation for \(\operatorname{ad}_E^r\partial_{x_i}\), not for \(E^r x_i\). |
| A slice | The actual image equation in (1), not merely absence of fixed points. |

A slice implies that the coefficients generate the unit ideal.
The converse is not a general four-variable slice theorem.
Niceness implies the exact polynomial flow identities
\[
\Phi_t(x)=x+tF(x),\qquad \Phi_t^{-1}(x)=x-tF(x).
\tag{2}
\]
These are inverses of the action map at time \(t\), not a
coordinate completion of \(s_*\). De Bondt's Proposition 1.3 and
Remark 1.4 give this correspondence.[^qt]

The [pass58 degree-scope note](coordinate-slice-degree-scope-pass58.md)
already separates the exponential finite-difference identities
from degree-module and slice-selection assertions. The
[quadratic-slice literature note](quadratic-slice-literature.md)
concerns degree of a slice and relative-coordinate hypotheses,
not spatial degree of the vector field. Neither inventory supplies
the missing implication by changing the meaning of “quadratic.”

## 2. A stronger usable theorem for the intersection of the first two conditions

Sun's published result says that a quadratic homogeneous
quasi-translation in dimension at most nine is linearly
triangularizable. This exact conclusion is stated in the primary
publisher abstract. De Bondt and Sun's 2018 paper, printed p.90,
Introduction item (3), literally states the dimension-nine case
over characteristic-zero fields, with reference to Sun's original
paper.[^sun] Its use in lower dimensions can also be justified
without strengthening that literal wording: pad the vector by
zero components to dimension nine, triangularize there, and take
the smaller upper-left blocks of arbitrary Jacobian products.
This gives strong nilpotence in the smaller dimension, to which
the constant-triangularization criterion below applies.

Here is the complete transfer needed for a possibly nonhomogeneous
quadratic nice four-vector. It is a deduction from that published
theorem, not a claimed new classification theorem.

Introduce a homogenizing variable \(z\), and put
\[
\widetilde F(x,z)=\bigl(z^2F(x/z),0\bigr).
\tag{3}
\]
This is a polynomial homogeneous quadratic five-vector, including
when some original components have smaller degree. Its last
component is zero, and the chain rule gives
\[
J\widetilde F\,\widetilde F
=\bigl(z^3(JF\,F)(x/z),0\bigr)=0.
\tag{4}
\]
Thus it is a homogeneous nice derivation, or equivalently a
homogeneous quasi-translation, in dimension five. No slice is
asserted for it.

Sun's conclusion implies strong nilpotence of its Jacobian:
after a constant similarity all Jacobian evaluations are strictly
triangular, so every product of five evaluations is zero.
At \(z=1\) the untransformed Jacobian has the block form
\[
J\widetilde F(x,1)=
\begin{pmatrix}JF(x)&*\\0&0\end{pmatrix}.
\tag{5}
\]
Taking the upper-left block in arbitrary products therefore gives
\[
JF(x^{(1)})JF(x^{(2)})\cdots JF(x^{(5)})=0.
\tag{6}
\]
De Bondt's Proposition 1.3 in the quadratic-Jacobian paper proves
that strong nilpotence over an infinite field is equivalent to
constant similarity to a triangular matrix with zero diagonal.[^rank]
Apply it to \(JF\). If \(P^{-1}JF(x)P\) is strictly triangular,
then
\[
J\bigl(P^{-1}F(Py)\bigr)=P^{-1}JF(Py)P
\]
has the same property. This is an actual linear coordinate change
of the original four-ring, not a dehomogenization of an arbitrary
changed hyperplane. Consequently the original \(F\) is linearly
triangularizable.

An extreme component in that triangular order is a complex
constant. If it is zero, the corresponding actual linear
coordinate is \(E\)-invariant. With the original slice, the
regular-kernel invariant-coordinate theorem recognizes
\(\ker E\simeq\mathbb C^{[3]}\), exactly as in the existing
[recognition-source gate](nice-route.md#three-different-ranks-and-the-first-decisive-closure).
If it is nonzero, the corresponding normalized linear coordinate
is itself a slice; its coordinate hyperplane is affine three-space,
so the slice theorem gives the same conclusion directly.

Hence the published theorem and (3)--(6) give the precise usable
consequence
\[
\boxed{\deg F\le2,\quad E^2x=0,\quad E(s_*)=1
\ \Longrightarrow\ \ker E\simeq\mathbb C^{[3]}.}
\tag{7}
\]
This does not use the supplied two-quadratic adjoint frame.
The homogeneous classification is not simply applied to the
nonhomogeneous four-vector: the full strong-nilpotence descent
is the needed intermediate argument.

The separate [sliced-nice rank-cap proof](nice-slice-adjoint-rank-pass74.md)
subsequently supplies an independent route to (7): it proves
\((JF)^3=0\) and \(\operatorname{rank}JF\le2\) from the original
slice at arbitrary spatial degree, then uses the directly checked
quadratic rank-two theorem. That route does not depend on access
to Sun's original proof. The rank cap alone does not recognize
arbitrary-degree nice actions.

### Source-access boundary

The original Sun publisher PDF and full article body could not
be retrieved in this bounded pass. Its original numbered theorem
and proof were therefore not freshly read. The exact statement
used above was read in the publisher abstract; the dimension-nine
version and definitions of triangularity and linear conjugacy
were read in the later primary paper coauthored by Sun.
The conclusion is explicitly
dependent on this published theorem, not an independent reconstruction
of its proof. The transfer (3)--(6) is fully written here.

## 3. What the other directly checked results do and do not add

De Bondt's Theorem 3.2 applies to quadratic polynomial maps
whose Jacobian is nilpotent **and** has rank at most two.
Theorem 3.3 also gives constant triangularization when the
Jacobian square is zero.[^rank] Their stated degree allows
nonhomogeneous maps. Niceness supplies nilpotence of \(JF\)
through (2). For a general LND, one must not replace the Jacobian
of its actual exponential by \(I+tJF\). The bounded audit has not
established that every quadratic-coefficient LND satisfies the
Jacobian hypotheses of those theorems.

For arbitrary spatial degree, de Bondt's Corollary 5.6 gives
linear invariants in dimension at most three, and for homogeneous
nice vectors in dimension at most four. Corollary 5.9 gives the
latter's explicit linear normal form.[^qt] These are not an
arbitrary nonhomogeneous four-dimensional theorem. Homogenization
of such a four-vector raises the dimension to five, where the
dimension-four statement does not apply. The quadratic-specific
Sun result is why Section 2 succeeds.

Dasgupta--Gupta's Theorem 3.6 assumes a PID containing
\(\mathbb Q\), an actual polynomial three-ring over that PID,
and an irreducible nice relative derivation. Their four-variable
Corollary 3.8 explicitly assumes \(EX_1=0\) and
\(E^2X_i=0\) for \(i=2,3,4\), as well as irreducibility.[^dg]
The slice makes irreducibility automatic, but does not supply
the displayed invariant coordinate. Their result cannot be used
to manufacture that missing coordinate.

Positive-degree homogeneous vector fields vanish at the origin
and cannot satisfy (1). Homogeneous statements are useful here
through the justified algebraic transfer, not by assuming that
an arbitrary sliced action can be homogenized without changing
its dimension or slice.

## 4. Which inverse degree is actually bounded

Equation (2) gives \(\deg_x\Phi_t^{-1}\le\max(1,\deg F)\).
It is not a bound on an adapted inverse map with last coordinate
the supplied \(s_*\).

There is an elementary explicit bound in the linear-slice branch
of Section 2. After an actual linear change let \(Et=1\), with
remaining linear coordinates \(y_1,y_2,y_3\). Niceness gives
\[
u_i=y_i-tEy_i,\qquad
B=\mathbb C[u_1,u_2,u_3,t],\qquad
y_i=u_i+t(Ey_i)(u_1,u_2,u_3,0).
\tag{8}
\]
Both inverse identities follow from the nice flow. If
\(d=\deg s_*\ge1\), then
\(s_*=t+h(u)\), where
\(h(u)=s_*(u,0)\) has degree at most \(d\). Thus the actual
adapted coordinate map \((u_1,u_2,u_3,s_*)\) has degree at most
\(\max(3,d)\), and the inverse obtained by substituting
\(t=s_*-h(u)\) in (8) has degree at most \(d+2\).
This bound is only for this linear-slice branch and is not a
bound supplied by Sun's theorem.

For Section 2's invariant-coordinate branch the cited recognition
theorems give existence of a polynomial kernel, not an explicit
adapted inverse-degree estimate in the original coefficients.
The [finite-family note](universal-family-degree-boundary-pass73.md)
can then supply a conditional uniform bound at fixed complexity
from pointwise existence, but neither its value nor an effective
algorithm follows from that constructibility argument.

The exact remaining targets outside (7) are:

- a theorem recognizing every sliced quadratic-coefficient LND
  without additionally assuming niceness or the checked Jacobian
  conditions;
- a theorem recognizing arbitrary nonhomogeneous nice sliced
  actions on the four-ring without a spatial degree bound;
- an explicit adapted inverse-degree bound for any broader
  recognized family.

No claim that these are historically new open problems is made.
The bounded search did not locate a primary theorem covering those
unrestricted hypotheses. This is a source-applicability report,
not an exhaustive bibliographic classification.

## References and review record

[^sun]: Xiaosong Sun, [*On quadratic homogeneous quasi-translations*](https://doi.org/10.1016/j.jpaa.2009.12.034), *Journal of Pure and Applied Algebra* 214 (2010), 1962--1972. The [publisher abstract](https://www.sciencedirect.com/science/article/pii/S002240490900317X) and author's [publication record](https://teachers.jlu.edu.cn/Sunxiaosong/en/lwcg/8115/content/3877.htm) were accessed. The characteristic-zero dimension-nine statement was also read in Michiel de Bondt and Xiaosong Sun, [*Classification of cubic homogeneous polynomial maps with Jacobian matrices of rank two*](https://doi.org/10.1017/S0004972718000345), *Bulletin of the Australian Mathematical Society* 98 (2018), 89--101, Introduction, printed p.90, item (3), in the directly accessible [publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/C0C49EEB0C49206F6A2D1065A7DA4B00/S0004972718000345a.pdf/classification_of_cubic_homogeneous_polynomial_maps_with_jacobian_matrices_of_rank_two.pdf). The latter article's cubic classification is not used.

[^rank]: Michiel de Bondt, [*Quadratic polynomial maps with Jacobian rank two*](https://arxiv.org/html/1601.00579v4), arXiv:1601.00579v4, November 2, 2017. Proposition 1.3 and its complete proof, Theorem 3.2 and its displayed proof, and Theorem 3.3's statement and proof were read. These are matrix triangularization results, not four-variable slice-classification statements.

[^qt]: Michiel de Bondt, [*Quasi-translations and singular Hessians*](https://arxiv.org/abs/1501.05168), arXiv:1501.05168v1. The [retained text](../tmp/pdfs/bondt-1501.05168v1.txt) of Proposition 5.1's homogenization calculation and Corollaries 5.6--5.9 with their local proof chain was reread. The full linear-invariant source chain had already been separately recorded in [pass71](nice-linear-invariant-source-pass71.md); no fresh full-paper audit is claimed here.

[^dg]: Nikhilesh Dasgupta and Neena Gupta, [*Nice derivations over principal ideal domains*](https://arxiv.org/abs/1701.03635), arXiv:1701.03635v1, Theorem 3.6 and its complete proof, Corollaries 3.7--3.8. The [retained primary text](../tmp/pdfs/dg-nice-1701.03635v1.txt) was directly reread. This report does not claim a new read of Wang's inaccessible original proof.

The three requested earlier inventories were read completely before
the new source search. The algebraic transfer in Section 2 received
an independent conditional algebra review from General before this
file was saved; that review did not claim a fresh primary-source
read. Saved-file review must be recorded separately after it occurs.
No new numerical suite, full regression, metadata change, external
contact, or formal verification is claimed.
