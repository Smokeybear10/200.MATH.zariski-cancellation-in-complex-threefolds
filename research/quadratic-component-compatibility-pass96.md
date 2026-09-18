# Noncollapsed quadratic fixed components have no companions

In the actual nonconical quadratic frame, any noncollapsed fixed
component is the whole reduced fiber. In particular a fiber with
two components of multiplicity two has both components collapsed.
The proof does not assume a nonzero first normal action: a
surviving good generator saturates a degree-two local cover at a
closed point, while a companion would survive in that same cover.

This is a compatibility restriction, not exclusion of two collapsed
components, freeness of N, or recognition of A.

## 1. Actual hypotheses and the two different projection bounds

Retain the actual setup of
[quadratic disjointness95](quadratic-double-components-disjoint-pass95.md)
and [everywhere rank95](quadratic-quotient-rank-everywhere-pass95.md):
\[
\begin{gathered}
S=\mathbb C[s_1,s_2]\subset A,\qquad K=\operatorname{Frac}S,
\qquad A=S[A_1,A_2,c],\qquad A_K=K[w],\\
A\text{ is a smooth affine complex threefold, faithfully flat over }S,\\
\ker(N|_A)=S,\qquad N^3A_i=0,\qquad
\deg_w A_i\le2,\quad\deg_w c\le4,\\
C=A/\mathfrak mA,\qquad
\operatorname{Min}(\mathfrak mA)=\{\mathfrak q_1,\mathfrak q_2\},
\qquad \mu_1=\mu_2=2 .
\end{gathered}
\tag{1}
\]
Here N is the actual primitive canonical Jacobian LND, not an
arbitrarily chosen derivation on a polynomial three-ring.
The point \(\mathfrak m\) is closed. A component is collapsed
when both good relative generators \(A_1,A_2\) have constant
residue on it.

Both components cannot be noncollapsed. Otherwise a generic
complex linear combination U of \(A_1,A_2\) would be nonconstant
on both. The excluded combinations form a proper linear subspace
for each component. The actual all-component degree bound92
would give
\[
4\le
2[\kappa(\mathfrak q_1):\mathbb C(\bar U_1)]
+2[\kappa(\mathfrak q_2):\mathbb C(\bar U_2)]
\le\deg_wU\le2,
\tag{2}
\]
a contradiction. This argument uses only good generators, so
its upper bound is two, not the bound four for a projection
also involving c.

Suppose, therefore, that the first component is noncollapsed
and the second is collapsed. Choose a surviving good U on the
first, and let \(u_0\in\mathbb C\) be its constant residue on
the second.

## 2. The surviving generator attains the companion's value

The single-component bound in
[the noncollapsed model95](noncollapsed-quadratic-local-translation-model-pass95.md)
gives \(\deg_wU=2\) and
\(\kappa(\mathfrak q_1)=\mathbb C(\bar U)\).
By itself that proof allows a punctured affine line.
Here the whole profile is (2,2), so the saturated total-four
argument in Section 1 of quadratic disjointness95 applies.
It says that both reduced components are entire affine lines
in the actual relative three-space with coordinates
\((A_1,A_2,c)\). In particular the nonconstant linear projection
\(\bar U\) is an affine coordinate on the first component:
\[
\deg_wU=2,\qquad
A/\mathfrak q_1=\mathbb C[\bar U],\qquad
A/\mathfrak q_2=\mathbb C[\bar c],\qquad
\bar U|_{\mathfrak q_2}=u_0 .
\tag{3}
\]
Thus there is a closed point p on the first component with
U(p)=u_0. The absence of punctures is essential for this step.
The components are disjoint by the full theorem95.

The whole nonreduced fiber is Cohen--Macaulay with no embedded
primes, and disjointness splits it into its two thickenings.
Section 4 of everywhere rank95 applies to the actual parameter
U on the first component: that entire thickening is a free
rank-two module over \(\mathbb C[U]\). Its quotient by
\(U-u_0\) has just the point p as reduced support. Consequently,
putting
\[
\begin{gathered}
T=(S[U])_{\mathfrak n},\qquad
\mathfrak n=\mathfrak mS[U]+(U-u_0),\qquad O=A_p,\\
\dim_{\mathbb C}O/\mathfrak nO
=\operatorname{length}O/\mathfrak nO=2 ,
\end{gathered}
\tag{4}
\]
uses the closed-point length of the whole thickening, not only
its generic multiplicity.

## 3. A dimension-three application of equality in flat rank

Since U is a degree-two polynomial in w, it is transcendental
over K. Hence \(S[U]\) is an actual polynomial three-ring.
The source T in (4) is a Noetherian regular local domain of
dimension three, with residue field \(\mathbb C\), and is
normal. The target O is a regular local domain of dimension
three because A is smooth and p is closed.

The map \(T\to O\) is local: its contracted maximal ideal is
exactly \(\mathfrak nT\), by evaluation at p. It is essentially
of finite type, since A is of finite type over \(S[U]\) and
O is its localization at p. Equation (4) gives a zero-dimensional
closed fiber. The regular-source, Cohen--Macaulay-target
dimension equality is \(3=3+0\). Miracle flatness therefore
makes O flat over T.[^flat] No finiteness of O as a T-module
is used here.

Its generic localization is exactly \(K(w)\). Indeed it is a
domain containing \(A\otimes_{S[U]}K(U)=K(w)\), and is contained
in the same fraction field. The equality on the left follows
because \(K[w]\) is finite over \(K[U]\), and inverting every
nonzero polynomial in U turns it into its fraction field.
Thus
\[
\dim_{K(U)}(O\otimes_T K(U))=2
=\dim_{\mathbb C}(O/\mathfrak nO),
\qquad O\simeq T^2\text{ as a module}.
\tag{5}
\]
The last conclusion is exactly the dimension-free flat-module
lemma in Section 1 of
[saturated flat rank93](nonconical-saturated-flat-rank-pass93.md).
Its hypotheses are a Noetherian local domain, a flat module,
finite generic rank, and equality of that rank with the
residue-vector-space dimension. It does not require the module
to be finite, separated, or complete beforehand. The later
dimension-two cubic application of that note is not the
application being used here.

For clarity about this finiteness gate, its proof lifts a
residue basis and uses the flat associated-graded identifications
to obtain compatible bases modulo every power of the source
maximal ideal. Clear a generic denominator in any element of
the module. Its compatible coefficients in the completion of
the source satisfy the same denominator equation. Faithfully
flat completion contracts the relevant principal ideal back
to T. Torsion-freeness then cancels the denominator and proves
that the original lifts span the module. It is not an
application of Nakayama to a module of unproved finite type.

## 4. The collapsed companion cannot survive this finite cover

Form the actual intermediate ring
\(D=A\otimes_{S[U]}T=(S[U]\setminus\mathfrak n)^{-1}A\).
It is a domain, with inclusions \(T\subset D\subset O\).
The last inclusion is a localization: all denominators defining
T avoid p, and O additionally inverts all elements of A
outside p.

By (5), O is integral over T, and therefore integral over D
using the same monic equations. An integral localization of a
domain is the original domain. Explicitly, if an inverse
\(d^{-1}\) of an element \(d\in D\) satisfies a monic equation
of degree k over D, multiplying by \(d^{k-1}\) expresses
\(d^{-1}\) as an element of D. Apply this to every inverted
element. It follows that
\[
D=O,\qquad
D\text{ is finite over }T,\qquad
D/\mathfrak q_2D\simeq\mathbb C[\bar c],
\qquad
\mathfrak n(D/\mathfrak q_2D)=0 .
\tag{6}
\]
Here the quotient assertion has no hidden denominator deletion.
The contraction \(\mathfrak q_2\cap S[U]\) is exactly
\(\mathfrak n\), since S reduces to its value at \(\mathfrak m\)
and U reduces to \(u_0\). Every element of
\(S[U]\setminus\mathfrak n\) restricts to a nonzero complex
constant on that entire component. Localizing consequently
leaves its polynomial curve ring unchanged.

But the quotient in (6) of a finite T-module, annihilated by
the maximal ideal of T, must have finite complex dimension.
The polynomial ring \(\mathbb C[\bar c]\) does not. This
contradiction excludes the mixed case. Together with (2),
it proves
\[
\boxed{\quad
\text{In an actual quadratic fiber of profile }(2,2),
\text{ both components are collapsed.}
\quad}
\tag{7}
\]

## 5. Any noncollapsed fixed component has no companion

The argument strengthens beyond profile (2,2). Now let the
whole closed fiber have any number of components allowed by
the actual quadratic hypotheses. Suppose its first component
is fixed and noncollapsed, and at least one other component
exists. Its multiplicity is two by the single-component
degree bound95.

Choose a generic complex linear combination U of the good
generators which survives on every noncollapsed component.
There are only finitely many proper linear subspaces to avoid.
On the chosen component the noncollapsed-image theorem95
gives both good residues affine in \(\bar U\) and
\(\bar c=a(\bar U)/b(\bar U)\), with a,b coprime.

Consider the actual projection \(V=U+t c\). For generic
nonzero \(t\in\mathbb C\), it is nonconstant on every component.
On a noncollapsed component U is already nonconstant, so at
most one t can make this combination constant. On a collapsed
component c must be nonconstant because the three relative
functions generate its curve ring, and \(t\ne0\) suffices.
The generic relative degree of V is at most four.

On the chosen component its rational-function degree is
\(\max(\deg b+1,\deg a)\). Indeed the expression
\((Ub+t a)/b\) has coprime numerator and denominator for
nonzero t, and there is at most one leading-degree cancellation.
The field-degree formula is the retained elementary rational
projection formula95. The total weighted bound92 gives twice
this positive integer plus at least one from the companion
components, with sum at most four. Thus that integer equals
one. Consequently b is constant and a has degree at most one:
the chosen reduced component is an entire affine line with
ring \(\mathbb C[\bar U]\). This conclusion no longer needs
the total-four saturation used in Section 2.

All reduced quadratic fiber components are disjoint by
everywhere rank95. Its whole-thickening argument makes the
chosen component a free rank-two module over the actual
\(\mathbb C[U]\). Choose any closed point \(p'\) on a companion,
put \(\alpha=U(p')\), and choose the unique point p on the
first line with \(U(p)=\alpha\). These are distinct points.
Repeat Sections 3--4 with
\(\mathfrak n=\mathfrak mS[U]+(U-\alpha)\). The transverse
length is two and the generic degree of U is two, so the same
local flatness and finite-rank argument gives
\[
\begin{gathered}
D=(S[U]\setminus\mathfrak n)^{-1}A=A_p,\\
\mathfrak pD,\ \mathfrak p'D\text{ are distinct maximal ideals of }D,
\quad\text{a contradiction},\\
\boxed{\quad
\text{Every noncollapsed quadratic fixed component is the
whole reduced fiber.}
\quad}
\end{gathered}
\tag{8}
\]
Here \(\mathfrak p,\mathfrak p'\) are the two closed-point
ideals. Both contract to \(\mathfrak n\) in \(S[U]\).
Every inverted source element therefore has the same nonzero
complex residue at both points. Both maximal ideals survive,
and remain distinct by the localization correspondence for
primes disjoint from its multiplicative set. But \(A_p\)
is local. This gives the contradiction for any companion,
without first requiring it to be collapsed.

Thus a fiber containing such a component has one reduced
component and whole multiplicity two. This is not an exclusion
of that remaining irreducible fiber.

## 6. Relation to the first-normal compatibility question

There is also a direct, but more conditional, jet comparison.
At a generic rank-one fixed component, the action on its
two-dimensional normal space has the form
\(\gamma x\partial_y\). N kills the reduced coefficient field,
so this induced linear action squares to zero. For a collapsed
component, \(A_i-A_i(\mathfrak q)\) belongs to the normal ideal,
and \(N^3A_i=0\) makes its second derivative invariant.
If its first normal action is nonzero, the base-order
contraction theorem94 then gives
\[
N^2A_i\in S\cap(\mathfrak q A_{\mathfrak q})^2
=\mathfrak m^2,\qquad i=1,2.
\tag{9}
\]
On a noncollapsed component with nonzero first normal action,
the exact local model95 instead supplies a surviving good U
with \(N^2U\in\mathfrak m\setminus\mathfrak m^2\).
Those two conditions are incompatible over the same base point.
The proofs of (7)--(8) remove both nonzero-first-normal premises;
they do not establish either premise automatically.

For an explicit boundary, take the intrinsic polynomial LND
\[
A_0=\mathbb C[x,y,U],\qquad
N_0=x^2\partial_y+y\partial_U,\qquad
\eta=2x^2U-y^2,\qquad
\ker N_0=\mathbb C[x,\eta].
\tag{10}
\]
It is primitive, since its nonzero coefficients have gcd one.
The kernel equality follows after inverting x from the slice
\(y/x^2\); contraction removes powers of x because
\(\eta\bmod x=-y^2\) is transcendental over \(\mathbb C\).
The fiber over \((x,\eta)\) is
\(\mathbb C[y,U]/(y^2)\). It has multiplicity two and U survives,
but \(N_0^2U=x^2\) belongs to the square of the base maximal
ideal. On the normal space of \((x,y)\), the induced action
is zero. This is an exact intrinsic control, not an asserted
original constant-acceleration frame with this specified
highest Jacobian field.

## 7. Scope and source provenance

The exclusion uses actual algebra generation, a surviving good
polynomial of generic degree two, an entire reduced parameter
line, and the whole-component finite-free statement95.
Section 2 obtains the entire line by saturated (2,2) geometry;
Section 5 obtains it from the all-component projection bound
whenever any companion is present. Removing these gates would
invalidate the closed-point finite-cover argument. In particular
an abstract completed local model does not replace them.

The separate [affine-line theorem96](quadratic-fiber-affine-lines-pass96.md)
removes punctures from every reduced quadratic fiber component,
including a lone noncollapsed one, by a higher-degree Thom
argument. It is not used above: Section 5 removes punctures
only under its contradiction premise by the projection bound.

No conclusion about the existence or exclusion of two collapsed
double components, a single noncollapsed double component, a
global slice for N, or general cancellation is made. No new
numerical method or frozen-file edit accompanies this proof.
The retained flat-rank93 and the relevant proofs95 were reread;
this is not a fresh audit of their deeper primary dependencies.

[^flat]: The Stacks Project,
    [Lemma 10.128.1, tag 00R4](https://stacks.math.columbia.edu/tag/00R4).
    Its complete displayed statement and proof were freshly read
    on September 14, 2026. It applies to a local homomorphism of
    Noetherian local rings with regular source, Cohen--Macaulay
    target, and the stated dimension equality. The essentially
    finite-type property was additionally checked above, but
    module finiteness is not a premise of this lemma. No fresh
    reading of its deeper referenced flatness criteria is claimed.
