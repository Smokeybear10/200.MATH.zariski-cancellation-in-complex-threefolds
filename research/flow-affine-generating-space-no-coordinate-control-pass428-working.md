# A flow-affine algebra-generating space can contain no coordinate

There is an explicit finite-dimensional complex vector space of
polynomials killed by the second iterate of a globally sliced
translation on four-space which generates the entire polynomial ring,
but contains no ambient polynomial coordinate. Adding constants to
this space does not change the obstruction.

This disproves one proposed entry step: first produce a finite set of
flow-affine algebra generators, then extract an ambient coordinate by
a constant linear combination. It does not disprove nonlinear
coordinate recovery or cancellation. In the example, short nonlinear
expressions recover a complete adapted frame.

## 1. The actual ring, action and generating space

Start with independent actual coordinates
\[
B=\mathbb C[u,a,b,c],\qquad E=\partial_u,\qquad E(u)=1.
\tag{1}
\]
Thus the kernel is already the polynomial ring
\(\mathbb C[a,b,c]\). No recognition theorem is used to identify it.

Let \(V\subset B\) be the complex linear span of the following eleven
polynomials:
\[
\begin{aligned}
g_1&=au,&g_2&=(a^2+1)u,\\
g_3&=a^2,&g_4&=a^3,&g_5&=a^5+a,\\
g_6&=b^2,&g_7&=b^3,&g_8&=b^5+b,\\
g_9&=c^2,&g_{10}&=c^3,&g_{11}&=c^5+c.
\end{aligned}
\tag{2}
\]
Their distinct monomial supports show that they are linearly
independent, so \(\dim_{\mathbb C}V=11\). More importantly,
\[
E^2(V)=0,\qquad
a=g_5-g_3g_4,\quad
b=g_8-g_6g_7,\quad
c=g_{11}-g_9g_{10},\quad
u=g_2-(g_5-g_3g_4)g_1.
\tag{3}
\]
These are literal polynomial identities. Consequently
\[
\mathbb C[V]=B.
\tag{4}
\]
The first two velocities generate the unit ideal:
\((E g_1,E g_2)=(a,a^2+1)=B\). Also the differentials of the
eleven generators generate \(\Omega^1_{B/\mathbb C}\), by
differentiating (3). Neither property repairs the linear-extraction
failure proved below.

Every element of \(\mathbb C+V\) has the form
\[
f=A(a)u+B_0(a)+C_0(b)+D_0(c)+\kappa,
\qquad \kappa\in\mathbb C,
\tag{5}
\]
where
\[
\begin{gathered}
A(T)\in\operatorname{span}_{\mathbb C}\{T,T^2+1\},\\
B_0(T),C_0(T),D_0(T)
 \in\operatorname{span}_{\mathbb C}\{T^2,T^3,T^5+T\}.
\end{gathered}
\tag{6}
\]
A nonzero member of the first span has degree one or two and has
at least one complex root. A nonzero member of the second span
has degree exactly two, three or five. In particular, it cannot
be a nonzero linear or constant polynomial.

We prove that no \(f\in\mathbb C+V\) is a coordinate of \(B\).
Here a coordinate means a member of a genuine four-variable
polynomial coordinate system, not merely an element of \(B\) or
of a rational coordinate system.

## 2. The zero-velocity case has a critical point

Suppose \(A=0\) in (5). If the three polynomials \(B_0,C_0,D_0\)
are zero, then \(f\) is constant and is not a coordinate.
Otherwise every nonzero one has degree at least two. Its derivative
is a nonconstant complex polynomial and therefore has a root.
Choose \(a,b,c\) at such roots for the active summands, and
arbitrarily for the zero summands. The \(u\)-derivative is zero
identically. All four partial derivatives of \(f\) vanish at the
resulting point.

A polynomial coordinate has nowhere-vanishing differential:
differentiate a full polynomial inverse and use its invertible
Jacobian. Therefore \(f\) is not a coordinate.

This argument alone would not cover every nonzero \(A\). For
example, a double root of \(A\) can coincide with a nonzero value
of \(B_0'\). The fiber argument below retains that boundary.

## 3. A direct affine plane-fiber Euler calculation

We use compactly supported topological Euler characteristic
\[
\chi_c(X)=\sum_i(-1)^i
 \dim_{\mathbb Q}H_c^i(X(\mathbb C),\mathbb Q).
\tag{7}
\]
It is additive for a closed subvariety and its open complement,
multiplicative for products, and multiplicative by the number
of sheets for the finite unramified covers used here.
In particular \(\chi_c(\mathbb A^n)=1\) and
\(\chi_c(\mathbb A^1\setminus\{r\text{ points}\})=1-r\).
These properties, including equality with the usual Euler
characteristic on complex algebraic varieties, are stated in
Cappell--Maxim--Shaneson, Section 2.[^euler]

Let \(C(T),D(T)\) be arbitrary complex polynomials of degrees
\(m,n\ge2\). For all \(\tau\) outside a finite set,
\[
\chi_c\{(b,c)\in\mathbb A^2:C(b)+D(c)=\tau\}
=m+n-mn=1-(m-1)(n-1).
\tag{8}
\]
Here is a proof which counts the affine curve directly and does
not omit a correction at infinity.

Let \(\Gamma\) be the finite set of critical values of \(C\).
For \(\gamma\in\Gamma\), let
\[
d_\gamma=m-\#\{b\in\mathbb C:C(b)=\gamma\}.
\tag{9}
\]
Factoring \(C(T)-\gamma\) shows that \(d_\gamma\) is the sum of
the root multiplicities minus one in that fiber. At a root of
multiplicity \(r\), the derivative has multiplicity \(r-1\).
Every root of \(C'\) occurs in one of these fibers, so
\[
\sum_{\gamma\in\Gamma}d_\gamma=m-1.
\tag{10}
\]
This includes repeated critical points and repeated critical values.

Choose \(\tau\) outside
\(\Gamma+\operatorname{CritVal}(D)\). For each \(\gamma\in\Gamma\),
the equation \(D(c)=\tau-\gamma\) has \(n\) distinct roots.
The sets of roots for different \(\gamma\)'s are disjoint.

Projection of the curve in (8) to the \(c\)-line is finite of degree
\(m\), since its equation is monic in \(b\) after dividing by the
nonzero leading coefficient of \(C\). Away from these
\(n|\Gamma|\) points it is an unramified complex cover with \(m\)
sheets. Over each of the \(n\) points belonging to a given
\(\gamma\), its set-theoretic fiber has \(m-d_\gamma\) points.
Additivity and the cover formula now give
\[
\begin{aligned}
\chi_c
&=m(1-n|\Gamma|)
  +\sum_{\gamma\in\Gamma}n(m-d_\gamma)\\
&=m-n(m-1)=m+n-mn.
\end{aligned}
\tag{11}
\]
The base is the affine line throughout. Its Euler characteristic
is one, not that of the projective line, and the finite projection
has no missing affine points. No proper compactification or
unaccounted contribution from its boundary is being used.

For use below, the other two cases are even simpler. If exactly
one of \(C,D\) is nonconstant of degree \(m\), then for a generic
\(\tau\) the level consists of \(m\) disjoint affine lines and
has Euler characteristic \(m\). If both are constant, a generic
level is empty and has Euler characteristic zero.

## 4. Every nonzero-velocity case has a non-affine-space fiber

Now suppose \(A\ne0\) in (5), and absorb \(\kappa\) into the
chosen level. Write \(a_1,\ldots,a_r\) for the distinct roots of
\(A\), so \(r\ge1\). Multiplicities of these roots are allowed.
Let \(X_\lambda\) be the complex algebraic variety defined by
\[
A(a)u+B_0(a)+C_0(b)+D_0(c)=\lambda.
\tag{12}
\]
On the open set \(A(a)\ne0\), solving for \(u\) gives an exact
algebraic isomorphism
\[
X_\lambda\cap\{A(a)\ne0\}
 \simeq(\mathbb A^1\setminus\{a_1,\ldots,a_r\})\times\mathbb A^2,
\quad \chi_c=1-r.
\tag{13}
\]
On \(a=a_i\), the coordinate \(u\) is free and the remaining
equation is
\[
C_0(b)+D_0(c)=\lambda-B_0(a_i).
\tag{14}
\]
Choose \(\lambda\) outside the finite union of the exceptional
level sets needed in Section 3 for these \(r\) equations.
When \(C_0=D_0=0\), also exclude the values \(B_0(a_i)\).
This is possible because the ground field is infinite.

The closed pieces over the \(a_i\) are disjoint, each being the
product of the indicated plane curve with the free \(u\)-line.
By (8), (13), (14) and additivity,
\[
\chi_c(X_\lambda)=
\begin{cases}
1-r,&C_0=D_0=0,\\
1+r(m-1),&
 \text{exactly one is nonzero, of degree }m\ge2,\\
1-r(m-1)(n-1),&
 \deg C_0=m\ge2,\ \deg D_0=n\ge2.
\end{cases}
\tag{15}
\]
In every case this number differs from one.
The count uses the distinct roots of \(A\), so it remains valid
when \(A\) has a double root. The chosen levels can in fact be
taken smooth: away from \(A=0\) the \(u\)-derivative is nonzero;
on (14) a nonempty generic curve has a nonzero \(b\)- or
\(c\)-derivative. Smoothness is not needed for the Euler
obstruction.

If \(f\) were an ambient coordinate, every level would be
isomorphic to \(\mathbb A^3\), whose compactly supported Euler
characteristic is one. Equation (15) contradicts this.
Together with Section 2 it proves
\[
\boxed{\quad
\mathbb C[V]=B,\qquad E^2(V)=0,\qquad
(\mathbb C+V)\cap\{\text{ambient coordinates of }B\}
=\varnothing .
\quad}
\tag{16}
\]

## 5. The exact entry obstruction and its limits

For an arbitrary globally sliced polynomial ring
\(B=A[u]\), the flow-affine module is
\(\ker E^2=A\oplus Au\); it contains finite algebra-generating
sets because \(A\) is finitely generated. The example shows that
algebra generation by a selected finite-dimensional subspace of
that module does not supply a coordinate in its complex linear
span. Neither the unit velocity ideal nor generation of the
cotangent module repairs that inference.

This does not say that every such generating subspace fails.
Nor does it say that \(E\) has no flow-affine coordinate:
\(u,a,b,c\) are a complete adapted frame, recovered by (3).
The recovery expressions for \(a,b,c\) have degree two in the
listed generators; that for \(u\) has degree at most three.
There is no lower bound here for unrestricted nonlinear recovery.

The eleven-generator space is not claimed optimal, of minimal
cardinality, or irredundant as an algebra-generating set. It is
not an actual four-coordinate frame. The theorem refutes
promotion of a flow-affine algebra-generating space to an actual
coordinate by constant linear extraction, not a theorem already
requiring a polynomial inverse.

The scope differs from the existing
[projected-generator control95](projected-generator-linear-extraction-obstruction-pass95.md),
which concerns four invariant generators from one specified
slice projection. Here the selected space generates the entire
ambient ring and includes nonzero velocities, while all its
elements still have time degree at most one. It also differs from
the [ordinary-degree obstruction101](global-reduction-audit-pass101.md)
and the [elementary-descent obstruction124](coordinate-degree-elementary-descent-obstruction-pass124.md).
Those statements are retained boundaries, not new results of this note.

No universal low-degree coordinate theorem, degree bound on
coordinate recovery, new recognition class, cancellation proof,
or literature-priority claim follows.

## 6. Source and verification boundary

The fresh unsaved symbolic calculation `2e525b` checked every
identity in (3), all eleven second \(E\)-derivatives, and the
decomposition (5) with eleven independent symbolic coefficients.
It did not prove the all-coefficient exclusion by numerical
sampling; Sections 2--4 give that proof.

The primary Euler-characteristic source was freshly read in its
author-hosted PDF, Section 2, printed page 410, covering precisely
the additivity and multiplicativity used above. Formula (8) is
derived explicitly here for arbitrary polynomials, including
their non-simple critical points. No specialized Milnor-fiber
classification or claim about singularities at infinity is an input.

The current README/frontier and the complete controls43, 95, 101,
124 were read to separate this route from earlier entry
obstructions. No earlier proof, checker, README or ledger is
changed. No saved checker was executed, imported or compiled.
The note has not received human-expert or proof-assistant
verification and makes no historical novelty claim.

[^euler]: Sylvain E. Cappell, Laurentiu G. Maxim and Julius L.
    Shaneson, [*Euler Characteristics of Algebraic Varieties*](https://people.math.wisc.edu/~lmaxim/Euler.pdf),
    Communications on Pure and Applied Mathematics 61 (2008),
    409--421, Section 2, printed page 410. The source states
    \(\chi=\chi_c\) for complex algebraic varieties, additivity
    for a closed subvariety, and multiplicativity for locally
    trivial topological fibrations. Only those properties are
    used here. The unramified covers in (11) are finite covers
    of a punctured affine line.
