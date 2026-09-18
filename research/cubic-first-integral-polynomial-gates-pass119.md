# Polynomial first-integral gates and a common-basepoint obstruction

The rational first-integral field in118 is rational, but it need not
have a nonconstant polynomial element. There is an exact criterion for
that additional step. Even a polynomial generator need not be a base
coordinate. The actual moving-frame identities give a separate useful
restriction: a pencil with a finite common basepoint cannot have a
geometric generic affine curve with only constant units.

The last assertion excludes the radial pencil. It does not exclude
all pencils or all generic punctured curves. An explicit polynomial,
unimodular velocity below satisfies the rank-one metric and common-point
conditions without satisfying the constant-units premise. No original
polynomial four-space frame is constructed for that control.

## 1. The exact source gate

Retain the actual cubic setting of
[moving-frame118](cubic-moving-frame-constraint-pass118.md). Write
S=C[s,t], K=Frac(S), and L=ker(V:K to K), where V is the nonzero
rational cubic direction. That proof gives trdeg_C L=1. The classical
Luroth--Igusa statement supplies

\[
L=\mathbb C(H),\qquad H=A/B,\qquad A,B\in S,
\qquad \gcd(A,B)=1 .
\tag{1}
\]

For this reduced pair, de Bondt's Theorem3.1 gives the precise
polynomial improvement:[^field]

\[
\begin{aligned}
L\cap S\ne\mathbb C
&\Longleftrightarrow
\exists\lambda,\mu\in\mathbb C:
\lambda A+\mu B=1\\
&\Longleftrightarrow
L=\mathbb C(g)\text{ for some nonconstant }g\in S.
\end{aligned}
\qquad L\cap S=\mathbb C[g]\text{ in the last case.}
\tag{2}
\]

The last equality is Lemma3.3. The coefficients in the middle condition
are constants, not arbitrary polynomials. This is stronger than the
absence of common zeros of A and B. Neither (1) nor (2) asserts that
g is a coordinate of S.

The rational field L is algebraically closed in K: applying V to a
separable minimal polynomial shows that every element of K algebraic
over L is also killed by V. Clearing denominators in V and removing
the gcd of its two coefficients produces a saturated polynomial
direction with exactly the same field and ring of constants. This
operation does not make that direction locally nilpotent or complete.

## 2. Three elementary boundaries

The following equalities follow by expressing K as a one-variable
rational extension of the displayed invariant field:

\[
\begin{array}{c|c|c}
D&K^D&S^D\\ \hline
s\partial_s+t\partial_t&\mathbb C(s/t)&\mathbb C\\
s\partial_s-t\partial_t&\mathbb C(st)&\mathbb C[st]\\
s^2\partial_s-\partial_t&\mathbb C\bigl(s/(st-1)\bigr)&\mathbb C.
\end{array}
\tag{3}
\]

For the first row use K=C(s/t)(t); D becomes t partial_t.
For the second use K=C(st)(s); D becomes s partial_s. Polynomial
monomials give the asserted rings of constants. The polynomial st is
not a coordinate: its nonzero closed fibers are punctured lines,
whereas a polynomial coordinate has affine-line fibers.

For the third row put H=s/(st-1). Then t=1/H+1/s, so K=C(H)(s)
and D=s^2 partial_s. There is no constant linear combination of s
and st-1 equal to one, proving its polynomial-kernel claim by (2).
Nevertheless their polynomial ideal is the whole ring, since
1=ts-(st-1), and this vector field has no zero anywhere. A general
fiber s-H(st-1)=0 is a punctured line. Thus even saturation and an
everywhere nonzero polynomial direction do not supply the missing
polynomial first integral. None of these directions is claimed to
come from an actual cubic original frame.

## 3. An actual common-basepoint and unit obstruction

In (1), use H also as the coordinate of L=C(H), and form the affine
generic pencil curve

\[
\Gamma=\operatorname{Spec}
L[s,t]/(A-HB).
\tag{4}
\]

This is the whole affine pencil curve, not just its open subset B
nonzero. The latter is the generic fiber of the rational map on its
chosen domain; those two objects can have different unit groups.
The coprime pair makes A-HB irreducible. Since L is algebraically
closed in K and the characteristic is zero, this curve is geometrically
integral. Explicitly, the minimal polynomial of a generator of a finite
extension of L cannot factor over K: its monic factors would have
coefficients algebraic over L and lying in K, hence in L. Therefore
K tensor_L L' is a field for every finite extension L'/L. Passing to
the algebraic closure gives a domain, and the coordinate ring of Gamma
injects into it after that flat field extension.[^geometric]
The actual polynomial entries of b are regular on Gamma.

Assume there is a point p0 in A2(C) with A(p0)=B(p0)=0. It gives an
L-point of Gamma. Put b0=b(p0). Let n denote the normalized normal
vector of118, so n and Q have entries in L. Its rank-one derivative
identity can be written

\[
\frac{dQ}{dH}=\alpha(H)nn^t,\qquad \alpha\in L^*,
\qquad n^tb_0=0,\quad b_0^tQb_0=-1,
\qquad w:=Qb_0\in\mathbb C^3.
\tag{5}
\]

Here is the justification for every specialization and coefficient.
The entries of Q are functions of H, and the normalized n has a
component equal to one. Comparing a nonzero H partial derivative in
118 therefore gives alpha in L, not merely in K. Its nonvanishing
follows from the nonzero cubic tensor. The polynomial identities
n^t b=0 and b^tQb=-1 hold in the coordinate ring of Gamma: it is a
domain inside K. Evaluating them at p0 gives the two middle identities
in (5), including b0 nonzero. Finally Q' b0=0, so Qb0 has constant
entries in the one-variable rational field C(H). In particular
w^t b0=-1.

Suppose now that the only units of the geometric affine curve
Gamma over an algebraic closure of L are scalars. Restrict Q to the
two-dimensional vector plane ker(n^t). Its rank is at least one by
(5). If its rank is two, its level Q(z,z)=-1 is a punctured line
over that algebraic closure: a linear change makes its equation
XY=1. The two coordinate functions pulled back by b are then units
on Gamma, hence constants. Thus b is constant on the geometric
generic curve. Its entries are algebraic over L, hence belong to L,
and V(b)=0. This contradicts the invertibility of [b,b_s,b_t].

If the restriction has rank one, elementary bilinear algebra using
Q(b0,b0)=-1 gives Q(z,z)=-(w^t z)^2 on ker(n^t). Consequently
(w^t b)^2=1 in S. Since S is a domain and evaluation at p0 gives
w^t b0=-1, one obtains w^t b=-1 identically. The entire velocity lies
in a fixed affine plane. Apply w^t to
b_ij=G_ij b+sum C^l_ij b_l: its left side and tangent terms vanish,
so G_ij=0. Its cubic tensor T is then zero, a contradiction again.

Thus an actual cubic pencil having a finite common basepoint must
have a nonconstant unit on its geometric generic affine curve.
For the radial pencil A=s,B=t, Gamma is A1 over L, so that pencil
is excluded. Its rational-map domain t nonzero has generic fiber
C*, but the polynomial velocity extends across the omitted common
point. It is the unit group of the whole curve (4) that matters.

## 4. Why the unit-group hypothesis cannot simply be removed

The following control is solely polynomial velocity and connection
algebra. Set z=s^3+1, w0=z t+1 and a0=s^3+2, and define

\[
\begin{gathered}
b=(z,a_0^2w_0^3/3,s a_0w_0)^t,
\qquad H=\frac{3s}{a_0w_0^2},\qquad
n=(0,H,-1)^t,\\
Q=\begin{pmatrix}
-1&0&0\\
0&H^3/3&-H^2/2\\
0&-H^2/2&H
\end{pmatrix},\qquad
Q'=nn^t,\quad n^tb=0,\quad b^tQb=-1,\\
\Omega=\det[b,b_s,b_t]=-2z a_0^2w_0^3\ne0.
\end{gathered}
\tag{6}
\]

Indeed 3b2(b1^2-1)=b3^3, which gives the quadratic identity after
using b3=H b2. Modulo z, the velocity is (0,1/3,s), so its entries
generate the unit ideal. Its reduced pencil pair 3s,a0 w0^2 has the
common point (s,t)=(0,-1), with b0=(1,0,0). But b does not lie in an
affine plane: in the rational coordinates s,w0, comparing degrees
three and one in w0 in a constant affine-linear relation first kills
the b2 and b3 coefficients, then the b1 coefficient.

These are the actual radial connection and metric identities for
this displayed b, not unrelated arrays. Differentiate b^tQb=-1 and
use n^tb=0 to obtain b_i^tQb=0. Differentiating again shows
G_ij=b_i^tQb_j for the coefficients obtained by decomposing b_ij in
[b,b_s,b_t]. Hence Q equals that frame's canonical metric. Moreover
n^t b_i=-b2 partial_i H, so its actual cubic tensor is
-b2^2(dH) cubed and is nonzero.

The generic pencil is not a unit-constant curve. Its relation
3s=H a0 w0^2 gives
a0[1-H^3 a0^2 w0^6/27]=2, so a0 is a nonconstant unit there.
There is no hidden polynomial generator of its invariant field:
K=C(s,w0), and over an algebraic closure of C(H) the equation
w0^2=3s/[H(s^3+2)] is irreducible, since its right side has a
simple zero at s=0. Thus C(H) is algebraically closed in K and is
the full field of constants of any nonzero rational direction killing
H. Its numerator 3s and denominator a0 w0^2 have no constant linear
combination equal to one: the t-squared coefficient first forces the
denominator's coefficient to vanish. Criterion (2) gives
C(H) intersect S=C for this control.
No original relative generators, unit-volume cubic graph, polynomial
four-space inverse, or sliced global action has been supplied.
In particular this is not an actual-frame counterexample or a
cancellation counterexample. It only defeats the proposed removal
of the constant-units hypothesis using the listed metric, common-point,
unimodularity and nonzero-determinant facts alone.

## 5. What is still missing

The exact algebraic target for polynomial descent is (2), not a
general slogan about rational foliations. A constant linear pencil
combination, or one nonconstant polynomial element of L, would suffice
for a polynomial generator. A further theorem would still be needed
to make it an actual base coordinate. The actual unit-volume and
original-inverse constraints may impose more than the metric data,
but this note does not prove that they do.

The primary theorem statement and attribution for (1), and the full
displayed Theorem3.1, Corollary3.2 and Lemma3.3 proofs for (2), were
read directly. The original classical Luroth proof and every deeper
dependency of those displayed proofs were not re-audited. Failed
AMS and Project Euclid fetches supplied no additional source read.
The selected Stacks field-extension statement and its complete displayed
proof were also read for the explicit geometric-integrality argument.
The control (6) was checked once by an inline symbolic calculation
(`1e20b8`); the all-purpose theorem and applicability gates are written
arguments, not numerical verification. No standalone test suite,
recognition claim, novelty clearance or external contact is asserted.

[^field]: Michiel de Bondt, [*Rational maps H for which K(tH) has
transcendence degree 2 over K*, arXiv:1501.06046v4](https://arxiv.org/html/1501.06046v4),
Theorem1.1 (Luroth--Igusa), Theorem3.1, Corollary3.2 and Lemma3.3.
The polynomial criterion and displayed proof are the selected primary
input here; the classical rationality theorem is explicitly attributed
there to its earlier sources.

[^geometric]: The Stacks Project, [Lemma10.47.8, Tag037P](https://stacks.math.columbia.edu/tag/037P).
Its factor-coefficient proof gives the required irreducibility; in
characteristic zero the finite scalar extension is a field, as used above.
