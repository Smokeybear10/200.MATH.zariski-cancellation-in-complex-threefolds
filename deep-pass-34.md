# Cancellation, geometric factoriality and integral quotient restrictions

The complex threefold cancellation conjecture is not solved by the results
below. The working question remains
\[
A[s]\simeq\mathbb C^{[4]}
\quad\Longrightarrow\quad A\simeq\mathbb C^{[3]},
\tag{1}
\]
for a finitely generated complex domain \(A\). This is an unconfirmed
interpretation of the professor's email. The pasted conclusion
\(X\simeq\mathbb A^1\) has the wrong dimension for \(r>1\); the
dimensionally consistent general conclusion is \(X\simeq\mathbb A^r\).
The characteristic-zero problem is distinct from the known negative
answer in positive characteristic.[^1]

There are two concrete advances and one precisely delimited negative
result. An integer obstruction isolates the nodal component in any
hypothetical ambient realization of the fixed conductor surface. An
explicit polynomial path repairs every member of the previously
constructed bad-top family while retaining minimum degree. A divisor
calculation shows why geometric generic factoriality cannot be inferred
from a polynomial cylinder, even after every coordinate change in a
chosen invariant plane.

None supplies an unrestricted intrinsic slice, an affine-space
recognition argument, or a counterexample to (1). The conditional surface
has not been embedded in affine three-space. The claims below are written
arguments with independent AI reconstructions and finite algebra checks,
not human expert verification, formal proof-assistant verification, or
established novelty.

## 1. The intrinsic rank-one gap

A locally nilpotent derivation, or LND, is a polynomial derivation whose
iterates eventually kill each individual polynomial. It describes an
algebraic additive-group action. A slice for \(D\) is an element \(r\)
with \(Dr=1\). A primitive derivation has no common nonconstant factor
in all its coefficients. Primitivity does not imply a slice.

The established consequences of (1) include smoothness, factoriality,
constant units and a nonzero intrinsic LND. For a primitive intrinsic
LND \(D\), the preceding quotient argument gives an invariant plane,
a principal full plinth, and a polynomial local-slice chart:
\[
C=\ker D=\mathbb C[a,b],\qquad
D(A)\cap C=pC,
\qquad Dr=p,\qquad A_p=C_p[r].
\tag{2}
\]
The exact hypotheses and inherited sources are retained in
[the intrinsic plinth proof](research/intrinsic-plinth-boundary-pass27.md).
The plinth measures where this particular action lacks a slice after
localization. It is not a direct invariant distinguishing affine space.

If all intrinsic LNDs span just one direction over \(\operatorname{Frac}A\),
their common kernel is \(C\), and every one is an invariant multiple of
one primitive derivation. The earlier commuting-direction argument
excludes this rank-one situation when \(p\) depends on a coordinate
\(a\) alone. Outside this special case, the existence of a second
intrinsic direction remains unproved.

Smooth contractibility alone cannot supply that direction. Known
Koras-Russell threefolds of the second kind have rank-one additive
symmetry. Their action classification is a warning against dropping
the polynomial-cylinder hypothesis, not evidence that their cylinders
are affine four-space.[^2]

## 2. Exact class groups of the geometric generic surfaces

Here is a complete calculation for the actual data (2). Factor
\(p=c\prod_i f_i^{n_i}\) into distinct prime factors in \(C\).
Fix a coordinate pair \((a,b)\) of that plane. Retain only the indices
\(I_a\) for which \(a\) is nonconstant on \(V(f_i)\), and set
\[
K=\mathbb C(a),\qquad
R_a=A\otimes_{\mathbb C[a]}\overline K,
\]
\[
d_i=[\operatorname{Frac}(C/f_i):K],\qquad
e_i=[\operatorname{Frac}\ker(\overline D:A/f_iA\to A/f_iA)
             :\operatorname{Frac}(C/f_i)].
\tag{3}
\]
The primitive boundary criterion gives \(e_i>1\) for a plinth factor.
The class group is
\[
\boxed{\operatorname{Cl}(R_a)
 \simeq\bigoplus_{i\in I_a}\mathbb Z^{d_i(e_i-1)}.}
\tag{4}
\]
This is an isomorphism of abelian groups, not a canonical choice of basis.

The proof keeps the distinction between ordinary and geometric generic
fibers. The ordinary generic ring is a localization of the regular UFD
\(A\), hence is a regular UFD. It stays regular over \(\overline K\)
because characteristic zero makes \(K\) perfect.[^3] Its geometric
base change injects into the domain
\[
(R_a)_p=\overline K[b,p^{-1},r],
\tag{5}
\]
so it remains integral. Geometric factoriality is a different assertion.

For each horizontal \(f_i\), its boundary ring localized over \(K\)
is a one-dimensional domain with a nonzero LND. Its invariant ring is
a finite algebraic field \(E_i\), and a local slice gives \(E_i[t_i]\).
Separability splits this into \(d_i e_i\) disjoint affine lines over
\(\overline K\). For each of the \(d_i\) roots \(\alpha\) of
\(f_i\) as a polynomial in \(b\), the fiber of \(b-\alpha\) has
\(e_i\) reduced components.

Localizing away from these lines gives the UFD (5). Thus their divisor
classes generate the class group. A relation among them is a principal
divisor whose defining function is a unit on (5). Such units are exactly
constants times integer powers of the factors \(b-\alpha\). The entire
relation list is therefore
\[
\operatorname{div}(b-\alpha)
=D_{\alpha,1}+\cdots+D_{\alpha,e_i}.
\tag{6}
\]
Each disjoint block contributes a free group of rank \(e_i-1\).
This proves (4), including the absence of torsion. The divisor machinery
is standard; the calculation does not assert a new general theorem
about divisor class groups.[^4]

It follows that
\[
R_a\text{ is factorial}\quad\Longleftrightarrow\quad
p\in\mathbb C[a].
\tag{7}
\]
Every ordinary generic ring was already factorial. The additional word
geometric is the entire obstruction. The available arbitrary-field
surface recognition statement explicitly retains it.[^5]

### A countercontrol satisfying the full cylinder hypothesis

Take the established primitive action on the already polynomial ring
\(A_0=\mathbb C[x,y,z]\), with
\[
f=xz-y^2,\quad r=x^3+yf,\quad
h=zf^2+2x^2yf+x^5,
\qquad D=\operatorname{Jac}(f,h,\cdot).
\tag{8}
\]
Its invariant ring is \(\mathbb C[f,h]\), its full plinth is \(fh\),
and the two boundary invariant degrees are five and two. These are
properties of the known Freudenburg example, not a new construction.[^6]

The two coordinate axes \(f=0\) and \(h=0\) intersect. They cannot
both be vertical for any coordinate \(a\) of their plane: otherwise
\(a-c\) would be divisible by \(fh\), contradicting its primality.
Consequently every coordinate in this particular invariant plane gives
a nonfactorial geometric generic surface, although
\(A_0[s]=\mathbb C^{[4]}\) identically.

More precisely, for every integer \(N\ge1\), the plane coordinate
\(a=f+h^N\) gives
\[
\operatorname{Cl}\!\left(A_0\otimes_{\mathbb C[f+h^N]}
              \overline{\mathbb C(f+h^N)}\right)
\simeq\mathbb Z^{4N+1}.
\tag{9}
\]
This rules out a universal shortcut with its full polynomial-cylinder
quantifier. It does not give a rank-one counterexample: the full
intrinsic symmetry rank of \(A_0\) is three. A rank-one exclusion would
still have to use uniqueness of the intrinsic direction, not merely
the geometry of an arbitrarily chosen action.

The [complete class-group proof](research/intrinsic-rank-pass34.md)
contains the boundary-field calculation and all coordinate quantifiers.

## 3. Integer branch obstructions

The second calculation concerns a hypothetical additive action on
\(\mathbb A^3\), not the unknown factor in (1). Use the fully retained
exceptional curve in its invariant plane. Its finite intermediate
curve and product complement have the established integral homology
diagram. The retained base normalizations are affine lines, and the
same diagram excludes additional first-homology classes on the source
normalizations.[^7]

At an exceptional value \(b\), let the base have \(r\) analytic
branches. Above branch \(j\), let the positive ramification indices
be \(e_{j,1},\ldots,e_{j,q_j}\), and let \(m_j\) be their gcd.
Normalized puncture loops give the map
\[
T:\bigoplus_{j,a}\mathbb Z v_{j,a}\longrightarrow\mathbb Z^r,
\qquad v_{j,a}\longmapsto e_{j,a}w_j.
\tag{10}
\]
The small base sphere contributes the diagonal class
\(w_1+\cdots+w_r\). The product-complement homology isomorphism
requires \(T\) to be surjective after quotienting by that class.

Integer Bezout identities give its exact cokernel:
\[
Q_b\simeq
\frac{\bigoplus_j\mathbb Z/m_j\mathbb Z}
     {\langle(1,\ldots,1)\rangle},
\qquad
|Q_b|=\frac{\prod_j m_j}{\operatorname{lcm}(m_1,\ldots,m_r)}.
\tag{11}
\]
Thus the branch gcds must be pairwise coprime. The assertion concerns
gcds, not every individual index. A branch with indices two and three
has gcd one and cannot be replaced by a single index six.

If there is one source point over each branch and all indices equal
two, then \(Q_b=(\mathbb Z/2)^{r-1}\). This excludes two or more
such branches. A single doubled branch is allowed. At the candidate's
node, all four normalized points are unramified, so this calculation
does not exclude the node itself.

The absence of unaccounted normalization cycles is essential. Without
it, cycles outside the puncture blocks could remove the proposed local
cokernel. The [integer lattice note](research/integral-ramification-pass34.md)
states that hypothesis and proves the full gcd/lcm criterion.

## 4. The compatible nodal component must be isolated

Keep the unchanged conductor surface
\[
B_0=\mathbb C[u,y,z]/((u-1)(u-i)z-y(y-1)),\quad d=u^4-1,
\qquad R=B_0\times_{\mathbb C[t]^6}\mathbb C[t]^3.
\tag{12}
\]
The fixed gluing pairs the labeled lines over \((1,i),(1,-i),(-1,i)\),
with the branch choices and scaled parameters from the preceding note.
Write \(\delta_0u=0\), \(\delta_0y=(u-1)(u-i)\),
\(\delta_0z=2y-1\).

Assume both a hypersurface presentation of \(R\) in affine three-space
and a primitive ambient LND restricting to \(u\delta_0\). An embedding
alone does not imply this extension premise. The preceding residue
argument forces the invariant base component
\[
\Gamma_0=\operatorname{Spec}(\mathbb C+d\mathbb C[s]),
\qquad s=u^2,
\tag{13}
\]
whose node identifies \(s=1,-1\). Its fibers are:

| Point on the normalized base | Actual reduced fiber | Action and multiplicity |
| --- | --- | --- |
| Node, identifying \(s=1,-1\) | Three disjoint lines | Free and reduced |
| \(s=0\) | One line | Fixed, with multiplicity two |
| Every other value | Two disjoint lines | Free and reduced |

The prior rational count is \(c_b=q_b-r_b+1\). This component alone
saturates the count at every value. Therefore an additional retained
component through such a value would have exactly one normalized source
point above each of its branches. Each such point has ramification equal
to that component's whole degree, which is at least two.

At a free fiber, a transverse linking sphere maps to the base sphere
with degree one. The integral loop identity would force the other
component's degree to divide one, which is impossible. Hence another
component could meet \(\Gamma_0\) only at \(s=0\).

At \(s=0\), a transverse fiber ideal is \((F,u^2)\), so the linking
degree is two. Every additional component's degree must then be two.
All branch indices at that point would be two, creating exactly the
nonzero cokernel in (11) if there were an additional branch. Thus
\[
\boxed{\Gamma_0\cap\Gamma_j=\varnothing
\quad\text{for every other primitive plinth component }\Gamma_j.}
\tag{14}
\]

This is a stronger necessary condition, not an ambient nonexistence
theorem. The three paired node lines form a full integer basis of the
required node lattice. They have no hidden torsion. Disjoint nodal
polynomial curves also exist, as already checked in pass 18.

If the full ambient plinth is \(F^k\beta\), with \(F\nmid\beta\),
equation (14) gives
\[
\beta=\kappa+FQ,\qquad \kappa\in\mathbb C^*.
\tag{15}
\]
Every other retained polynomial curve lies in a nonzero level of \(F\).
This does not prove that \(\beta\) is a polynomial in \(F\), that those
levels are irreducible, or that no later equivariant modification can
repair the forced singular first stage.

The [complete realization restriction](research/odd-realization-pass34.md)
proves the support decomposition, transverse degrees and node lattice.

## 5. A successful repair inside the explicit minimum-degree family

Return to the fixed polynomial model
\[
\Delta=x^2\partial_w+2(1+\lambda x)^2w\partial_z
\quad\text{on }\mathbb C[x,\lambda,w,z].
\tag{16}
\]
Among actual horizontal LNDs fixing \(x\) and sending \(\lambda\) to
one, the minimum highest-adjoint degree is one. The preceding pass
constructed, for every \(p(x)\) with \(p(0)=1\), an actual horizontal
\(\delta_p\) at this minimum whose primitive top has full plinth \(p\).

Let \(\theta_p\) denote its supplied two-sided polynomial coordinate
map. Put
\[
p_t=p+t(1-p),\qquad G_t=\theta_{p_t}^{-1}\theta_p.
\tag{17}
\]
Both \(G_t\) and its inverse are polynomial over \(\mathbb C[t]\),
since the original divisibility arguments use only \(p_t(0)=1\).
They obey
\[
G_t\delta_pG_t^{-1}=\delta_{p_t},\qquad
q(\delta_{p_\tau})=1\text{ for every scalar }\tau.
\tag{18}
\]
At \(t=1\), the primitive top has a slice. This repairs any supplied
member of the family while keeping the original \(\Delta\) as the
reference action. The gauges do not, in general, normalize \(\Delta\).

The repair is a polynomial path, not generally a single additive-group
flow in four variables. Its first \(\lambda\)-coefficient contains a
nonzero quadratic term in \(t\) for \(p\ne1\), contradicting the
additive group law. After adjoining \(t\), it does lift to a coordinate
additive flow in five variables. These assertions concern different
rings and cannot be interchanged.

For nonconstant \(p\), its degree remains unchanged at every parameter
except the endpoint. The bad divisor disappears there; this is not a
stepwise complexity reduction or a termination proof for arbitrary
horizontal actions.

## 6. Why the universally available scaling path fails

In the known good coordinates, the fixed model becomes the pencil
\[
P_\lambda=D_0+\lambda E,
\quad D_0=x^2\partial_b+2b\partial_c,
\quad E=4xb\partial_c.
\tag{19}
\]
Let \(\phi\) be any actual \(\mathbb C[x,\lambda]\)-automorphism,
equal to the identity at \(\lambda=0\), with
\(\phi^{-1}P_\lambda\phi=D_0+\lambda D_1\). Write
\(C(\lambda)=\phi^{-1}E\phi\), and form \(\phi_t\) by substituting
\(t\lambda\) in the supplied map and its inverse. Exactly,
\[
\phi_t^{-1}P_\lambda\phi_t
=D_0+t\lambda D_1+(1-t)\lambda C(t\lambda).
\tag{20}
\]
If \(N=\deg_\lambda C>0\), every scalar \(t\ne0,1\) has degree
exactly \(N+1\). If \(N=0\), normalization forces \(C=E\).
The path stays at degree one at an intermediate nonzero parameter
if and only if \(\phi\) centralizes \(E\).

The normalized centralizer consists precisely of
\(b\mapsto b\), \(c\mapsto c+K(x,\lambda,b)\). Under the retained
degree-one premise, its primitive top is already \(\partial_c\).
Thus parameter scaling does not furnish a degree-preserving repair
for a nonsliced top.

For the full family in Section 5, the exact value is \(N=4\).
That standard path has degree five at every intermediate nonzero
parameter even though both endpoints have degree one. The different
path (17) avoids this increase. A path that works in one explicit
normal form is not a classification of all degree-one horizontals.

The [full repair and scaling proof](research/plinth-repair-pass34.md)
also proves that marked canonical normalizers preserve the normalized
polynomial \(p\). Their restricted conjugacy invariant does not survive
allowing the successful general gauges.

## 7. The exact outstanding proof obligation

The rank-one route still needs an argument using the entire polynomial
cylinder and uniqueness of the intrinsic action direction to force a
second useful action or a slice. Generic factoriality of a selected
invariant-plane section does not provide it. Full coordinate-frame
extraction still recovers only the intrinsic symmetry that exists.

The surface route still needs either an actual embedding and compatible
ambient action or an obstruction covering every later modification and
every possible generating triple. The new isolated-component condition
does not supply either. The horizontal route still needs a mechanism
for arbitrary input, not just the explicit \(p\)-family.

These are genuine missing implications. Substituting a numerical check,
a favorable coordinate choice, a finite thickening, or an extra variable
for any of them would leave the original conjecture unproved.

## 8. Evidence and source boundaries

The [verification record](verification-pass-34.json) records the executed
regression. Its finite exact methods check polynomial identities, lattice
indices, divisor relation matrices and countercontrols. They do not
formalize the universal topological or recognition arguments. The
[separate audit](research/proof-audits-pass34.md) records reconstruction,
corrections and execution evidence without treating repeated runs as
additional tests.

The [literature scope note](research/literature-scope-pass34.md) separates
directly examined primary statements from inherited inputs. Standard
local-slice, divisor and quotient-homology mechanisms retain their
attribution. No exhaustive priority determination, publication-readiness
claim, external contact or submission is represented by this report.

## Sources

[^1]: Neena Gupta, [*The Zariski Cancellation Problem and related problems in Affine Algebraic Geometry*](https://ems.press/content/book-chapter-files/33171), ICM 2022, Sections 2-3. This is the primary statement and characteristic boundary, not evidence that every later publication has been excluded.

[^2]: Charlie Petitjean, [*Automorphism groups of Koras-Russell threefolds of the second kind*](https://arxiv.org/pdf/1507.06087), Introduction and Section 2. The claim used is the explicit rank-one action classification and smooth contractibility, not a polynomial-cylinder theorem.

[^3]: Stacks Project, [Lemma 33.12.2, Tag 038U](https://stacks.math.columbia.edu/tag/038U), geometric regularity criterion.

[^4]: Stacks Project, [Section 31.27, Tag 0BE0](https://stacks.math.columbia.edu/tag/0BE0), Weil divisors and principal-divisor presentation of the class group.

[^5]: Sai Krishna, [*An algebraic characterization of the affine three space in arbitrary characteristic*](https://arxiv.org/pdf/2308.05424), Theorem 2.9 and Corollary 2.10. The extra geometric-factoriality hypothesis over arbitrary fields is retained.

[^6]: Gene Freudenburg, [*Local slice constructions in k[X,Y,Z]*](https://ir.library.osaka-u.ac.jp/repo/ouka/all/4752/ojm34_04_02.pdf), Section 4.1, and [*Canonical factorization of the quotient morphism for a Ga-action on an affine variety*](https://arxiv.org/pdf/1602.08786), Sections 8.2.1-8.2.2. The source action and full first degree module are established inputs; the class-group consequence is derived above.

[^7]: Shulim Kaliman, [*Free C+-actions on C3 are translations*](https://www.math.miami.edu/~kaliman/library/Ka.invent.2004.c%2B.pdf), final author version, Proposition 3.2 and its integral diagram, Proposition 4.2, and Theorem 5.2. The whole-action freeness conclusion is not applied to the candidate's action with a fixed line.
