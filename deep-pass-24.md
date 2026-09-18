# Coordinate-reduction obstructions and the invariant-lifting condition

## Result and remaining objective

The main new obstruction concerns positive cases, not failed slice
candidates: some explicitly sliced extensions cannot be changed into
the previously classified coefficient ring by any polynomial change
of the added variable fixing the original base. A complementary
coefficient theorem gives global coordinates for those examples.

The general investigation also rules out three specific shortcuts.
Projecting a broad class of plane-moving triangular horizontal actions
can fail even on a polynomial family. All six primitive canonical
tangent generators can fail local nilpotence even when they descend
correctly. Finally, restriction to the fixed surface necessarily creates
extra invariants, with an exact nonfree module describing the discrepancy
for the prescribed ambient quotient map.

None of these assertions settles
\[
X\times_{\mathbb C}\mathbb A^1\simeq\mathbb A^4
\quad\Longrightarrow\quad X\simeq\mathbb A^3.
\tag{1}
\]
The complete objective remains (1). The professor has not confirmed
this corrected interpretation of the original dimensional typo.
Priority, human expert review and proof-assistant verification remain
unresolved.

The distinction is important: finding a nonzero algebraic additive
symmetry on X is already possible in this setup. What remains is to
construct one strong enough to recognize X, for example one with a
slice. Rephrasing that missing construction is not a proof that it exists.

## 1. Positive cases outside the earlier gauge reduction

Use the canonical primitive rank-three base on R=C[x,y,z]:
\[
\begin{gathered}
f=xz-y^2,\quad a=f^n,\quad \nu=2n+1,\quad r=x^3+ay,\\
h=a^2z+2ax^2y+x^5,\quad D=-\operatorname{Jac}(f,h,\cdot),\\
Dr=ah,\quad Dx=2ar,\quad Dy=h-6x^2r,\quad xh=r^2+f^\nu.
\end{gathered}
\tag{2}
\]
Here n>=1, ker D=C[f,h], and the base construction is inherited.[^1]

For every n>=1, the coefficient
\[
b_*=1+2fxr
\tag{3}
\]
gives a sliced derivation E_*=D+b_*partial_t with global polynomial
coordinates. But for every n>=2,
\[
b_*\notin\mathbb C[f,h,r]+D(R).
\tag{4}
\]
Thus no polynomial automorphism fixing R can move this positive
case into the preceding coefficient class. Such an automorphism
necessarily sends t to lambda*t+g with lambda in C* and g in R,
so it would contradict (4).

### The obstruction is valid for polynomials of every degree

Reduce a hypothetical equality b_*=P(f,h,r)+Dg modulo f^n.
In R/(f^n), x is a non-zero-divisor and
\[
r=x^3,\qquad h=x^5,\qquad
\overline D=-5x^4\delta,\qquad
\delta=x\partial_y+2y\partial_z.
\tag{5}
\]
The earlier coefficient ring becomes C[f,x^3,x^5]. Its only
x-exponents below five are zero and three. Reducing modulo x,
then cancelling x^3 and reducing again, forces those terms of
P to be exactly the constant one. Cancelling x^4 then gives
\[
2f=xQ(f,x)-5\delta g\pmod{f^n}.
\tag{6}
\]
Because n>=2, the ideal (f^n) has no ordinary degree-two part.
The degree-two part of xQ is a multiple of x^2. The image of
delta on all quadratic polynomials is
span{x^2,xy,xz+2y^2,yz}, which does not contain f=xz-y^2.
Equation (6) is impossible.

This is a homogeneous-degree proof after an exact reduction, not
a search bounded by the degrees of P or g. A separate reconstruction
uses the degree-six part of the original equality before quotienting
by f^n and reaches the same contradiction.

The boundary n=1 is explicit: b_*=1+D(x^2/2), so t-x^2/2
is an affine slice. For n=2, with L=fx^2/2-f^2t and
X=x+2rL+hL^2, a polynomial slice is
\[
\sigma=t+\frac{X^2-x^2}{2f}.
\tag{7}
\]
It is polynomial because X=x modulo f, and E_*(sigma)=1.
No minimum-degree claim is made.

The obstruction only forbids base-fixing changes. It does not
exclude nonlinear changes of the entire frame. Such changes do
exist for these examples by the next theorem.

## 2. A complementary coefficient criterion

Let
\[
b=c(f,h)+rB(f,h,x),\qquad
\ell=\frac12\int_0^x B(f,h,v)\,dv,\qquad c_0=c(0,0).
\tag{8}
\]
The coefficient class differs from the earlier C[f,h,r] class;
neither theorem is being mislabeled as a classification of all R.
This class permits arbitrary x-polynomial odd coefficients.

**Working theorem.** E=D+b*partial_t has a polynomial slice
exactly when
\[
\begin{gathered}
c_0\ne0,\qquad c(f,0)=c_0,\\
\bigl(x^3c(0,h)+h\ell(0,h,x)\bigr)\bmod(x^5-h)
=c_0x^3+H(h).
\end{gathered}
\tag{9}
\]
Every positive kernel is C^[3], with a finite global coordinate
construction. The last test is monic division in x.

The [complete coefficient proof](research/odd-coefficient-gauge-pass24.md)
gives both all-degree necessity arguments. Its polynomial primitive
on the auxiliary surface is F=c*r+h*ell, with DF=ah*b.
On h=0, opposite local-slice values at the same physical x
cancel the ell contribution and force c(f,0) to be constant.
On f=0, the fifth-root orbit comparison forces the last condition.
Both contradictions use integral physical endpoints and a pole in
their orbit parameter, with multiple roots allowed.[^2]

For sufficiency, C=(c-c_0)/h is polynomial. Since
Dy=h+delta_0(-x^3), subtracting D(Cy) leaves
c_0+delta_0(ell+Cx^3). The last remainder test gives
\[
\ell+Cx^3=L(h)+(h-x^5)J(h,x)+fK(f,h,x).
\tag{10}
\]
The identity (h-x^5)/f^n=2x^2y+f^nz makes the J term a
genuine polynomial gauge. The remaining coefficient is
1+delta_0(fK/c_0), after constant rescaling.

The previously proved finite nilpotent inverse and two-sided
physical curve lift apply to every f-divisible auxiliary primitive,
including this one. They supply actual polynomial coordinates,
not only a formal series or a generic isomorphism. Their underlying
full-ideal affine-modification principle is established machinery.[^3]

This theorem supplies the positive side of (3). Together with
(4), it shows that a general positive-case reduction must permit
more than a change of the added variable over a fixed base.

## 3. A broad horizontal-action projection still misses actual solutions

For a nonzero LND D on R=C^[3], take a minimal local slice
Dr=p, with p nonzero and nonunit, and d in sqrt(p*ker D).
The earlier stable family is
\[
\mathcal B=R[\lambda,w]/((1+\lambda d)w-r).
\tag{11}
\]
Its stable cylinder has an explicit sliced action E and slice s.
For any ambient derivation Y, the tangent projection
K_Y=Y-Y(s)E kills s and therefore descends to mathcal B.

Projection does not preserve local nilpotence. More strongly,
adding any correction HE+sZ does not change the descended
derivation at all. Those normal corrections cannot repair a
failed projection.

Keeping the old invariant plane fixed has an exact answer:
for primitive D and minimal r, a horizontal LND fixing ker D
exists if and only if p divides d. In the positive case one can
set delta(lambda)=1, delta(w)=0 and delta|R=(d/p)wD.
The converse follows from the earlier full-plinth relative
isomorphism obstruction. Therefore a solution in the radical-only
case must move the old invariant plane.

The [full horizontal-action analysis](research/horizontal-lnd-pass24.md)
tests such movement on the explicit polynomial example
D=x^2*partial_y+2y*partial_z, p=x^2, d=x.
Here mathcal B=C[lambda,x,w,z] really is polynomial.
Nevertheless every ambient triangular horizontal LND
\[
Y=\partial_\lambda+a(\lambda)\partial_x
{}+b(\lambda,x)\partial_y+e(\lambda,x)\partial_t
{}+c(\lambda,x,y,t)\partial_z
\tag{12}
\]
fails after projection.

The projected w-equation is affine in w. After replacing
x by the invariant q=x-integral a, its linear coefficient is
minus the nonzero polynomial
gamma=(q+A_0+lambda*a)(1-lambda(q+A_0)).
The w-coefficients of successive iterates satisfy
P_{j+1}=P_j'-gamma*P_j. Their degrees strictly grow, so no
iterate vanishes.

The same example has an explicitly constructed successful
horizontal LND and stable ambient lift. It uses coupled y,t terms
excluded from (12). Thus the result excludes the stated projection
ansatz, not all horizontal LNDs. A universal construction of the
needed coupled terms remains unproved.

## 4. Genuine tangent generators are not enough

Write a hypothetical sliced polynomial ring as
B=C[x_1,x_2,x_3,x_4]=A[s], with E(s)=1. Let
s_i=partial_i(s), e_i=E(x_i), and
K_ij=s_i*partial_j-s_j*partial_i.
The exact tangent-module identity is
\[
V=\sum_{i<j}(e_i v_j-e_j v_i)K_{ij}
\quad\text{when}\quad V=\sum_jv_j\partial_j,\quad V(s)=0.
\tag{13}
\]
All six generators genuinely kill s. Their quotient module is
Der_C(A), so there is no missing ideal-invariance condition in
this presentation.

There is also already a finite way to extract a nonzero LND in
that tangent module: take the highest s-coefficient of an ambient
coordinate partial moving A, equivalently its highest nonzero
commutator with E, and remove its verified vertical part.
This uses the established leading-LND argument, not a new
recognition theorem.[^4]

What fails is choosing one of the canonical generators. The
[explicit six-generator control](research/intrinsic-frame-repair-pass24.md)
uses polynomial coordinates
a=x_1+x_4, b=x_2+x_4, c=x_3+x_4,
s=x_4-a^2-b^2-c^2. All six K_ij descend, commute with E,
and are primitive. Yet their even iterates on a selected
coordinate are nonzero multiples (-4)^m or (-8)^m.
None is locally nilpotent.

Successful combinations exist in that example and are printed
explicitly. It does not refute arbitrary polynomial combinations.
For an unknown A, the exact recognition condition still requires
a tangent LND V and a polynomial g with V(g)=1. A resulting
intrinsic slice would give a proper additive action and the
published stably affine threefold recognition theorem would
finish (1).[^5] The existence of such a sliced tangent LND has
not been deduced from the module identity.

## 5. The surface quotient requires new invariant lifts

The fixed surface retains its four-generator A^4 embedding.
Its normalization is
B_norm=C[u,y,z]/((u-1)(u-i)z-y(y-1)), d=u^4-1,
with the same three branch-pair identifications.
For its descended LND partial, the full invariant ring is
\[
T=\mathbb C+d\mathbb C[u].
\tag{14}
\]
It has one four-branch point of cotangent dimension four, not
three nodes. Its completion is the four coordinate axes meeting
at their common origin. It cannot be a plane curve ring.

The [complete quotient analysis](research/nodal-hypersurface-pass24.md)
distinguishes that curve from the three singular lines on the
surface. For the prescribed nodal subcurve
A_0=C[d,v], v=du^2 and v^2=d^2(d+1), it proves
\[
T/A_0\simeq\mathbb C[s],\qquad s=u^2,
\tag{15}
\]
as an A_0-module. This normalization module has generic rank one
but requires two generators at the node.

The map from the surface to its full invariant curve T is
nonflat at every conductor point. This is not a contradiction
with flatness of an ambient three-space quotient over its
smaller invariant plane. These are different base rings.

If an ambient realization R_surface=W/(P), W=C^[3], admits
an ambient LND D inducing the prescribed surface derivation,
put C=ker D and mathcal H=W/D(W)
as a C-module, not a quotient ring. There is an elementary exact
sequence
\[
0\longrightarrow C/(P)C\longrightarrow T
\longrightarrow\mathcal H[P]\longrightarrow0.
\tag{16}
\]
For an invariant residue lifted by a, write Da=Pb; its image is
the class of b modulo D(W). This construction proves exactness
and makes the invariant-lifting failure explicit.

For the prescribed nodal map, the last module must be exactly
the nonfree normalization module in (15). Nonzero lifting
defects do occur for primitive LNDs on actual C^[3], so their
mere presence is not an impossibility argument.

Nor do free degree modules and principal higher-image ideals alone
force the defect module to be locally free. An explicit locally
nilpotent module operator satisfies those properties in every degree,
yet has a nonfree torsion summand at the node. Its module is
deliberately not an algebra. Any stronger exclusion must therefore
use multiplication constraints of an actual derivation on C^[3],
which that countercontrol does not decide.

The descended action also has a fixed Cartier curve of exact
order four in the surface Picard group, yet no nonunit common
coefficient. Thus any compatible ambient extension can be
reduced to a primitive one. These are necessary compatibility
conditions, not an A^3 embedding decision.

## 6. Verification and the next proof obligation

The coefficient theorem and obstruction have two independent
written reconstructions, including different all-degree proofs
of (4). Exact companion checks cover the coefficient tests,
gauge identities, positive examples, tangent and horizontal
controls, and the quotient-curve algebra.
The [audit record](research/proof-audits-pass24.md) separates
universal proofs from finite tests and repeated runs.

Execution and artifact integrity are recorded separately in
[verification-pass-24.json](verification-pass-24.json) and
[consistency-pass-24.json](consistency-pass-24.json).
The final complete run passed 525 exact test methods across 40 suites,
including 31 new methods. Repeated executions and parser controls do
not increase those counts.
These are not mathematical novelty certification, human peer
review, or a formal proof of unrestricted cancellation.

The unresolved construction now has a sharper boundary. It must
handle nonlinear changes of the complete frame, rather than only
base-fixing coefficient gauges; it must find appropriate coupled
horizontal terms, rather than project the excluded triangular
class; or it must obtain a sliced tangent LND, not merely a
nonzero one. A surface-based counterexample must satisfy the
actual invariant-lifting module condition rather than identify
two different kernel rings.

The cited construction principles and recognition results remain
credited. The present family statements and explicit controls
have not received a comprehensive novelty audit or expert review.
No public novelty claim, submission or external contact is made.

## Sources

[^1]: N. Dasgupta and S. A. Gaifullin, [*On locally nilpotent derivations of polynomial algebra in three variables*](https://arxiv.org/html/2306.00510v2), Theorem 5.7 and Section 2; G. Freudenburg, [*Canonical Factorization of the Quotient Morphism for an Affine Ga-Variety*](https://arxiv.org/html/1602.08786v3), Section 8.2 for the n=1 base and its degree modules.

[^2]: The Stacks Project, [local dimension bounds](https://stacks.math.columbia.edu/tag/00KW) and [finite normalization](https://stacks.math.columbia.edu/tag/0BXR). The complete proofs display the actual charts and check the special-fiber dimension.

[^3]: S. Kaliman and M. Zaidenberg, [*Affine modifications and affine hypersurfaces with a very transitive automorphism group*](https://arxiv.org/pdf/math/9801076), Proposition 2.1 and Corollary 2.2, applied through the previously audited full-ideal physical lift.

[^4]: B. Alhajjar, [*LND-Filtrations and Semi-Rigid Domains*](https://arxiv.org/pdf/1501.00445), Proposition 2.2 and Proposition 3.4, retaining Daigle and Makar-Limanov credit.

[^5]: R. V. Gurjar, K. Masuda and M. Miyanishi, [*Affine Space Fibrations*](https://oa.tib.eu/renate/bitstreams/2db0f47c-00f9-4195-9c8a-a46722165a99/download), Theorem 4.1.1, printed page 44. It assumes a proper additive action on an affine threefold stably isomorphic to affine space; a merely nonzero intrinsic LND does not verify that premise.
