# Independent audit of the four-generator conductor presentation

The [four-generator proof](nodal-elimination-pass23.md) passes this
independent audit. The actual ring of the fixed pinched surface is
C[d,e,g,h], where e=du and g,h are the new functions in that note.
No change of the underlying gluing is involved. The resulting bound
is three to four complex algebra generators, not an affine-three-space
embedding or an ambient LND realization.

In addition to checking the author's finite point-and-cotangent
argument, this audit reconstructs a shorter ring-level proof using
the full conductor ideal and a finite module. That proof is included
in Section 6.1 of the final main note, whose transcription was also
checked. No external search, novelty claim, registry
edit or human expert review is part of this audit.

## 1. The ring and line identifications are unchanged

The normalization remains

\[
B=\mathbb C[u,y,z]/((u-1)(u-i)z-y(y-1)),\qquad d=u^4-1.
\]

The coordinate scale from the original construction is uniform:
u=w/a_0, z=a_0^2*z_old and t=a_0^3*t_old, with a_0^4=3.
It preserves all three original identifications. In particular, the
full conductor is still I=dB=(d,du)R, as independently established
before these proposed generators were chosen.

I independently substituted all six original line parametrizations
into the new g,h, without importing a project checker. Their residues
are exactly

\[
(g,h)=(0,t),\quad(1,-t),\quad(i,-t)
\]

on the respective three pairs. Both members of each pair give the
same expressions. The negative signs change the selected function h,
not the equality condition defining the pinch. The elements d,e
vanish on all six lines. Therefore the proposed S=C[d,e,g,h] is
indeed a subring of the original R.

## 2. Recovery is polynomial at every exceptional root

Write A=(u-1)(u-i) and retain the coefficient polynomials a,b,q,r
from the main proof. I independently computed polynomial Bézout
coefficients for (b,Ar) and (A,q). Both gcds are one. The coefficient
of Ar, respectively q, can be chosen as -u, giving exactly

\[
bU_y-uAr=1,\qquad AU_z-uq=1.
\]

The explicit quartic polynomials printed in the note satisfy those
identities. These are polynomial identities over Q(i), not rational
functions assumed to extend at roots.

With v=g-a=by, the key recovery identity is

\[
Ar\,y=Ah+u\,v(v-b)
\]

in B. Before passing to B, the difference of its two sides is
u*b^2 times the defining surface relation. The displayed formula
for y then follows from the first Bézout identity. The second identity
recovers z from Az=y(y-1) and qz=h-ry. Substituting the polynomial
recovery of y into the z formula changes it by another explicit
multiple of the same relation, as verified by the companion checker.

Thus B=S[u] globally. The monic equation u^4=d+1 makes B a finite
S-module, and R is finite as an S-submodule. No claim of module
freeness, a nontrivial fraction-field extension, or generation of R
by u is needed. In fact u belongs only to the normalization before
localization.

## 3. An independent full-conductor proof of equality

This argument gives a ring-level reconstruction separate from tangent
recognition. Since e=du, localization gives u=e/d in S_d. The recovery
above therefore proves

\[
S_d=B_d=R_d.
\tag{1}
\]

The conductor restriction map S->R/I=C[t]^3 is surjective. Indeed
the distinct values 0,1,i of g give the three component idempotents
by polynomial Lagrange interpolation. If E_0(G) is the polynomial
with values 1,0,0 at 0,1,i, then

\[
E_0(G)=1+(i-1)G-iG^2.
\]

The product (2E_0(g)-1)h has residue (t,t,t). The idempotents and
that common parameter generate the whole product C[t]^3. This is
surjectivity of the actual conductor quotient, not just separation
of its closed points.

Let M=R/S, a finite S-module. Quotient surjectivity gives R=S+I.
Since the previously proved full ideal is I=(d,e)R and d,e belong
to S, it follows that

\[
M=(d,e)M.
\tag{2}
\]

At every maximal ideal of S not containing d, (1) makes M vanish.
If d belongs to a maximal ideal, so does e, because the identity

\[
e^4=d^4(d+1)
\tag{3}
\]

holds in S. Equation (2) and local Nakayama then make M vanish at
that ideal too. A finite module vanishing at all maximal ideals is
zero. Hence R=S.

The argument would be invalid if I were replaced by an unsupported
reduced-center approximation. Here I=(d,e)R is the exact conductor
ideal from the independent module calculation B=R+Ru, and its use
does not assume the new generator conclusion.

## 4. Global points and all conductor tangent directions also check

The alternative geometric proof is complete as well. Equation (1)
already gives an isomorphism off the conductor, with no unexamined
exceptional root. On the conductor, g separates the three components
and h=plus or minus t separates their individual points. The value
of d excludes a mixed conductor/nonconductor collision.

At a conductor point the completed local ring is
C[[xi,eta,t]]/(xi*eta), so its cotangent space has two independent
normal directions and one common tangent. The normal derivatives
of d,e on the paired roots u_j,u_k form the matrix

\[
\begin{pmatrix}
4u_j^3&4u_k^3\\
4u_j^4&4u_k^4
\end{pmatrix}.
\]

Its determinant is 16u_j^3u_k^3(u_k-u_j), which is nonzero for
each actual pair. Independently computed values in the specified
pair order are 16+16i, 16-16i and -16+16i. The derivative of h
in the common tangent direction is respectively 1,-1,-1. Therefore
d,e,h span the entire three-dimensional cotangent space of R, not
merely the tangent spaces of the two normalization branches.

Any unknown normal components of dh do not affect the determinant,
because dd and de have zero common-tangent component. The necessary
local coordinates on each normalization branch hold at every point:
q is nonzero on a split line and r is nonzero on an unsplit line.

With the independently proved finiteness, this verifies all hypotheses
of the author's two-stage local Nakayama recognition. That argument
is valid, but the module proof in Section 3 above shows that the
conclusion need not depend on this geometric recognition step.

## 5. The elimination presentation and boundaries

The four-variable elimination presentation also checks. The recovery
polynomials y_*,z_* in the independent variable U satisfy the surface
relation modulo J. The other defining relations recover G,H,D,E
from U,y_*,z_*. Conversely the actual recovery identities show that
the map back to B recovers u,y,z. Thus P[U]/J=B by inverse algebra
maps, and restriction to P yields the prime ideal J cap P defining
the embedded ring. No implicit saturation or unproved elimination
of a denominator is used.

The note does not claim a minimal list of equations or a three-variable
presentation. The lower bound of three generators follows from the
local cotangent dimension. The earlier exclusion of every triple
containing d and e still holds, since R/(d,e)=C[t]^3 cannot be
generated by one element as a complex algebra. That obstruction does
not exclude a different triple. The exact remaining possibilities
for the minimal number of generators are three and four.

## 6. Exact verification record

The original six-method standalone suite
`research/nodal_elimination_checks_pass23.py` was independently run:
all six methods passed in 0.273 seconds. After addition of the exact
conductor-quotient and base-relation control, the complete final
seven-method suite independently passed in 0.291 seconds. Its
controls are
noncircular: the recovery tests establish polynomial errors as
explicit multiples of the original surface equation, and the
conductor restrictions use the original line parametrizations.

Separate inline calculations independently verified both Bézout
pairs, the recovery relation, all six restrictions, the three normal
determinants and the conductor quotient's interpolation polynomials.
These inline checks are not additional regression methods. The main
agent maintains full-project verification counts.

No mathematical defect was found in the proposed reduction. The
four-generator theorem is a proved advance for this particular
surface construction, with exact controls and two ring-recognition
arguments. It is not a proof of the three-space embedding question,
the ambient LND realization, or general complex cancellation.
