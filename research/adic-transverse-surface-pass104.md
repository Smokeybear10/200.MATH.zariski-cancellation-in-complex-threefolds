# The finite translation kernels form a ramified transverse surface

In the collapsed quadratic sector covered by103, the invariant rings of
the finite translations are not unspecified coefficient rings. They are
the finite neighborhoods of the actual smooth surface cut out by the
global slice. Their completed coefficient ring is finite free of degree
two or three over a corrected copy of the completed invariant base.
Its double factor is a simple formal ramified cover; the mixed case has
an additional unramified factor. This does not identify the original
base embedding with the corrected one or algebraize the translation.

## 1. Actual assumptions and two base embeddings

Retain the actual hypotheses and conclusions of
[finite translations103](quadratic-adic-projected-translation-pass103.md):
the smooth complex threefold ring A, the faithfully flat inclusion
S=C[s1,s2], a closed ideal m, and the whole collapsed double or mixed
(2,1) fiber with L(m) nonzero. Put J=mA. The actual projected derivation
D preserves J and all its powers, and
\[
r=z-q_0u^2/2\in A,\qquad Dr=1,\qquad
A/J=\mathcal D[r],\qquad
\mathcal D=\mathbb C[G]/(H(G)),\quad
H(T)=T^2\text{ or }T^2(T-1).
\tag{1}
\]
Write d=deg H. The identification in (1) retains the full nilpotent
shift r=c-q0 hbar squared/2. On A_k=A/J^k the induced derivation D_k
is locally nilpotent and has slice r_k. Let C_k=ker D_k and let P_k
be its finite slice projection. The maps P_k are compatible ring maps.

There are two maps from S into A_k relevant below. One is the original
inclusion followed by reduction. The other is s mapped to P_k(s),
whose image lies in C_k. No equality between these maps is assumed.

## 2. A single algebraic transverse surface gives every kernel

Let H_A=A/(r), and let j=mH_A. Slice evaluation in the actual
polynomial presentation A_k=C_k[r_k] gives compatible isomorphisms
\[
\boxed{\quad C_k\simeq A_k/(r_k)=H_A/j^k,\qquad
C_\infty:=\varprojlim_k C_k\simeq\widehat{H_A}^{\,j}.\quad}
\tag{2}
\]
Explicitly the inverse from A_k/(r_k) to C_k sends the class of a
to P_k(a); P_k has kernel (r_k). Thus the S-algebra structure on
H_A/j^k is transported to C_k by s mapped to P_k(s). It is not
obtained by asserting that D_k annihilates the original S.

The ring H_A is a smooth affine surface. At any closed point of
Spec A on r=0, membership r in the square of the maximal ideal
would force Dr into that maximal ideal by the Leibniz rule. This
contradicts Dr=1. Thus r has a nonzero differential everywhere
on its zero set. The hypersurface in the smooth threefold is
smooth of dimension two. It is nonempty since its quotient by
j is the nonzero ring D. No global polynomiality, factoriality
or connectedness of this surface is asserted.

## 3. Exact lengths and a compatible finite free basis

Flatness of S into A gives
\[
J^i/J^{i+1}\simeq
(\mathfrak m^i/\mathfrak m^{i+1})\otimes_{\mathbb C}\mathcal D[r].
\tag{3}
\]
Multiplication by r is injective on every layer. If ra belongs
to J^i, successive reduction through the layers of degrees zero
through i-1 therefore proves a in J^i. Consequently
(r) intersect J^i equals rJ^i. To identify the associated graded
of H_A, one also uses the same assertion at i+1: if a in J^i
equals rb modulo J^(i+1), then rb is in J^i, hence b is in J^i.
It follows that
\[
j^i/j^{i+1}\simeq
(\mathfrak m^i/\mathfrak m^{i+1})\otimes_{\mathbb C}\mathcal D,
\qquad
\dim_{\mathbb C}(H_A/j^k)=d\binom{k+1}{2}.
\tag{4}
\]
Here the degree-i piece of the two-variable regular base has
dimension i+1. In particular H_A/j^k is finite dimensional.

Put R_k=S/m^k. The d elements 1,G,...,G^(d-1), now regarded
in H_A/j^k, reduce to a basis modulo the maximal ideal of R_k.
Nakayama gives a surjection R_k^d onto H_A/j^k. Its source and
target have the same complex dimension by (4), so it is an
isomorphism. These chosen bases are compatible as k varies.
Writing Rhat for the m-adic completion of S, we obtain
\[
\boxed{\quad C_\infty\simeq
\widehat R\oplus\widehat R G\oplus\cdots\oplus
\widehat R G^{d-1}\quad\text{as a }\widehat R\text{-module}.\quad}
\tag{5}
\]
In C_k the symbol G in this basis means P_k(G), not necessarily
the original class of G. This distinction also applies in (5).
The completed embedding is the compatible corrected embedding
s mapped to P_k(s). It is injective because the displayed free
module contains 1 as one of its basis elements.

Multiplication by G expresses G^d uniquely in this basis.
There is therefore a unique monic polynomial Q(T) of degree d
over Rhat, reducing to H(T), such that
\[
C_\infty\simeq\widehat R[T]/(Q(T)),\qquad T\longmapsto G.
\tag{6}
\]
The source is free of rank d with the same power basis, so this
surjective map has zero kernel beyond the displayed relation.
The coefficients of Q need only be formal series. Neither
H_A localized over S_m nor A localized there has been proved
finite over S_m by this argument.

## 4. The formal double is simply ramified

The radical of j in H_A is supported at one point in the whole
double case and at two points in the mixed case. The j-adic
topology is equivalent to the topology defined by that radical:
the nilradical of H_A/j is nilpotent. The Chinese remainder
theorem for powers of the distinct maximal ideals identifies
the completion with the product of the completions at those
points. Each point lies on the smooth surface from Section 2,
so each factor is a regular complete local ring of dimension
two with residue field C. These facts about completion and
formal coordinates are standard.[^regular]

For d=2 write Q(T)=T^2+aT+b, where a,b belong to mRhat.
Replace T by Y-a/2 and put Delta=a^2/4-b. Then
\[
C_\infty=\widehat R[Y]/(Y^2-\Delta),\qquad
\Delta\in\mathfrak m\widehat R.
\tag{7}
\]
Regularity of this two-dimensional local hypersurface forces
Delta not to belong to (mRhat)^2. Otherwise its defining
equation is in the square of the maximal ideal of the
three-dimensional regular ambient local ring, giving embedding
dimension three instead of two. Choose t completing Delta to
a regular parameter pair of Rhat. The formal parameter theorem
gives the explicit description
\[
\widehat R=\mathbb C[[\Delta,t]],\qquad
C_\infty=\mathbb C[[Y,t]],\qquad \Delta\longmapsto Y^2.
\tag{8}
\]
Thus the double factor has simple formal ramification. This is
a statement about the map on the transverse surface, not about
the plinth of N or its order in the original invariant base.

For d=3, the simple root 1 of the reduction T^2(T-1) lifts to
a root alpha in Rhat. For completeness, start with alpha=1
modulo m. At each step solve for the next homogeneous correction
using the inverse of Q'(alpha), which is a unit; the errors
increase in m-adic order, so the corrections converge. Dividing
by T-alpha gives a monic quadratic Q2 reducing to T^2. The value
Q2(alpha) is a unit, so the two factors are comaximal and
\[
C_\infty\simeq
\widehat R[T]/(Q_2(T))\ \times\ \widehat R.
\tag{9}
\]
This is the simple-root case of Hensel factorization.[^hensel]
The quadratic factor is regular by the preceding completion
decomposition, so completing its square gives (8). After the
same base parameter change, the mixed transverse cover is
\[
\mathbb C[[\Delta,t]]\longrightarrow
\mathbb C[[Y,t]]\times\mathbb C[[\Delta,t]],\qquad
f\longmapsto\bigl(f(Y^2,t),f(\Delta,t)\bigr).
\tag{10}
\]
Its two components are not a contradiction to A being a domain:
completion along a disconnected fiber can split a domain.

## 5. The remaining algebraic obstruction is explicit

The finite slices still give only
\[
\widehat A\simeq\varprojlim_k C_k[r].
\tag{11}
\]
In this ring an element is a series sum a_n r^n whose coefficient
a_n in C_infinity tends to zero in the j-adic topology. This
allows unbounded r-degree. It is not the ordinary polynomial
ring C_infinity[r]. Under this presentation the original base
function s expands as
sum r^n P_k(D_k^n s)/n! at each finite level. Its constant
coefficient is the corrected base image used above; the positive
coefficients have not been proved to vanish. Thus (8)--(10)
cannot be substituted for a relative trivialization of the
original morphism Spec A to Spec S.

This determines the previously unspecified formal kernel rings
in the actual collapsed sector, including their ranks and their
ramification. To turn it into global recognition one still needs
an algebraic argument controlling the original base embedding
and the unbounded slice degrees, or a different global method.
The abstract control in103 already disproves the inference from
compatible finite translations alone to global local nilpotence.
No original mixed-fiber exclusion, hidden N-degree-two function,
ambient invariant coordinate, or cancellation theorem follows here.

## 6. An exact control separates the two base embeddings

For either polynomial H in (1) and any e at least one, take the
intrinsic polynomial ring A0=C[x,y,r] and set
\[
S_0=\mathbb C[x,f],\qquad f=H(y)-x^er,\qquad
D=\partial_r,\qquad J_0=(x,f)A_0=(x,H(y))A_0.
\tag{12}
\]
Here S0 embeds faithfully flatly in A0: its presentation with
f,x,r and y is monic of degree d in y, hence free of positive
rank over S0[r]. The displayed equality of ideals is exact,
and D preserves every power. The finite translation kernels are
\[
C_k^0=\mathbb C[x,y]/(x,H(y))^k,\qquad
P_k(f)=H(y),\qquad f-P_k(f)=-x^er.
\tag{13}
\]
To verify the kernel, the ideal is independent of r, so its
quotient is the indicated coefficient ring with a polynomial
variable r; differentiation kills exactly its constant terms.
For k>e the difference in (13) is nonzero. For instance, applying
y=0 maps the coefficient quotient onto C[x]/(x^k), where x^e
survives. Thus even in a polynomial threefold with an actual
global translation, the original base need not equal the
corrected translation-invariant base at higher finite orders.

A complex vector-space basis of Ck0 is given by x^a y^b with
0<=a<k and 0<=b<d(k-a). For each x-degree a<k the defining
ideal requires exactly divisibility by H^(k-a) in C[y]. Monic
division proves the basis claim and the length in (4), here
directly for every k. This control does not realize the full
original E-frame, disprove algebraization, or exclude a mixed
fiber. Its D is globally locally nilpotent. The separate
control103 addresses failure of global local nilpotence.

The [finite symbolic checks](adic_transverse_surface_checks_pass104.py)
compare these monomial bases and lengths with exact Groebner
reductions, check the surviving base difference, and check
finite truncations of the mixed ramified parameter. They do
not verify the universal actual-frame or completion arguments.

## Sources

[^regular]: The Stacks Project Authors, [Section 15.44, Lemmas 15.44.1
    and 15.44.4](https://stacks.math.columbia.edu/tag/07NU), and
    [Lemma 10.160.10](https://stacks.math.columbia.edu/tag/0C0S).
    The displayed statements and proofs were read. They preserve
    dimension and regularity under local completion and identify
    a complete regular C-algebra with residue field C as a formal
    power-series ring. Deeper linked dependencies were not freshly
    reconstructed. No novelty is claimed for these structure facts.

[^hensel]: The Stacks Project Authors, [Section 10.153, Definition
    10.153.1 and Lemmas 10.153.2--10.153.3](https://stacks.math.columbia.edu/tag/04GE).
    The displayed characterization and proof were read. Only the
    directly reconstructed complete-ring simple-root argument above
    is used in (9); no general algebraization theorem is invoked.

The actual-coordinate and finite-translation inputs are the linked
private proof103, not an independently published theorem. This note
is a human-readable working proof, not a Lean certificate. Its
universal claims are not certified by a finite symbolic example.
