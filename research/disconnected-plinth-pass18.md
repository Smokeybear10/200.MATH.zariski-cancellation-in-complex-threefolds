# Disconnected plinth support and singular polynomial fibers

The connectedness question for primitive rank-three derivations is
not settled here. The plane-curve shortcut that would settle it is
false: two disjoint polynomial curves can be singular fibers of a
noncoordinate polynomial. An explicit pair of nodal cubics verifies
this failure.

There is nevertheless a sharp reduction. If the reduced plinth
support of a primitive rank-three derivation is disconnected, all
its irreducible components are pairwise disjoint fibers of one
noncoordinate polynomial in the kernel. Every component must have
at least one multibranch singularity. Smooth components, and even
components unibranch at every point, cannot occur in this remaining
configuration.

These conclusions use exact published inputs where specified and
elementary arguments written below. They do not assert that such a
rank-three plinth has been realized, that connectedness is a known
open problem, or that any result here is novel.

## 1. Exact starting point

Let \(0\ne D\in\operatorname{LND}(R)\), where
\(R=\mathbb C^{[3]}\), assume \(D\) primitive, and put
\(C=\ker D\cong\mathbb C^{[2]}\). Write \(P_D=pC\).
For nonunit \(p\), the
[primitive support identification](whole-plinth-component-pass16.md)
identifies \(V(p)_{\rm red}\) with Kaliman's retained exceptional
curve. His Theorem 5.2(i) makes each irreducible component a
polynomial curve, meaning its normalization is \(\mathbb A^1\).
It does not state connectedness, smoothness, or unibranchness.[^1]

The rank input is also precise. If some local slice derivative is
a polynomial in a coordinate of \(C\), that coordinate is an
ambient coordinate and the rank is at most two. Conversely, for
primitive \(D\), a minimal local slice derivative that is not
univariate in any kernel coordinate forces rank three. These are
Dasgupta--Gaifullin, Propositions 5.3-5.4 and the cited coordinate
criterion.[^2] A polynomial expression in a noncoordinate of
\(C\) does not meet the first premise.

## 2. Disjoint polynomial curves lie in one pencil

**Lemma.** Let \(f_1,f_2\in\mathbb C[u,v]\) be irreducible
nonconstant polynomials whose zero curves have normalization
\(\mathbb A^1\). If their zero curves are disjoint, then

\[
f_2=a f_1+b,
\qquad a,b\in\mathbb C^*.
\tag{1}
\]

To prove this, every unit on either curve is constant: its image
and inverse in the normalization ring \(\mathbb C[t]\) are
polynomials with product one. Disjointness makes the restriction
of \(f_2\) to \(V(f_1)\) a unit, so
\(f_2-b=f_1h\) for some nonzero constant \(b\) and polynomial
\(h\). Similarly \(f_1-c=f_2k\) for a nonzero constant \(c\)
and polynomial \(k\). Neither \(h\) nor \(k\) is zero.
Total degrees give

\[
\deg f_2=\deg f_1+\deg h,
\qquad \deg f_1=\deg f_2+\deg k.
\tag{2}
\]

Both \(h,k\) are therefore nonzero constants, proving (1).
This proof does not assume that either curve is an embedded line.

**Corollary.** If a finite union of distinct irreducible polynomial
curves is disconnected, all its irreducible components are pairwise
disjoint and have equations \(F-a_i=0\), up to nonzero scalar
factors, for a single polynomial \(F\) and distinct constants
\(a_i\).

Choose components from two different connected components. Any
other irreducible component is disjoint from at least one of these
two. Applying (1), and composing affine changes in the defining
polynomial, puts every defining equation in the same pencil.
Distinct irreducible members of that pencil have distinct constant
values and are disjoint. Thus a disconnected union cannot contain
an intersecting cluster alongside a separated component.

Applied to the plinth support, this gives

\[
p=\lambda\prod_{i=1}^r(F-a_i)^{e_i},
\qquad r\ge2,\quad e_i\ge1,\quad\lambda\in\mathbb C^*.
\tag{3}
\]

If \(D\) has rank three, \(F\) cannot be a coordinate of
\(C\), by the rank criterion. Equation (3) alone does not say
that it is one.

## 3. An explicit counterexample to the coordinate-pencil shortcut

Consider

\[
F(u,v)=v^2-u^3+3u.
\tag{4}
\]

Its fibers at \(2\) and \(-2\) are disjoint irreducible nodal
cubics:

\[
\begin{aligned}
F=2&:\quad v^2=(u-1)^2(u+2),\\
F=-2&:\quad v^2=(u+1)^2(u-2).
\end{aligned}
\tag{5}
\]

The right sides are not squares in \(\mathbb C[u]\), so these
polynomials, monic quadratic in \(v\), are irreducible. Their
normalization maps are explicitly

\[
\begin{aligned}
F=2&:\quad u=t^2-2,\qquad v=t(t^2-3),\\
F=-2&:\quad u=t^2+2,\qquad v=t(t^2+3).
\end{aligned}
\tag{6}
\]

Each map is finite because \(t\) satisfies the displayed monic
quadratic relation with \(u\), and birational because generically
\(t=v/(u-1)\), respectively \(t=v/(u+1)\). The integral
closure is therefore \(\mathbb C[t]\). The two preimages of
the node are distinct in each case.

The gradient of \(F\) vanishes at \((1,0)\) and \((-1,0)\),
so \(F\) is not a coordinate. Equally, a polynomial automorphism
cannot send a singular nodal cubic to a smooth line. Thus neither
disjointness nor polynomial normalization allows the passage from
(1) to a coordinate pencil.

The plane divisor \(p_0=F^2-4\) satisfies the component-normalization
condition but is not a polynomial in any plane coordinate: such
a polynomial would have smooth coordinate lines as its irreducible
zero components. This is only plane data. No primitive rank-three
LND with this plinth is constructed here.

For later coefficient comparisons, \(B=F+3\) is a unit modulo
\(p_0\), with distinct residues \(5\) and \(1\). The exact
identity is

\[
1=\frac{F^2-4}{5}-\frac{F-3}{5}(F+3).
\tag{7}
\]

Eleven independent SymPy identities checked (5)-(7), the finite
quadratic relations, the two critical points, and the nonzero node
Hessian determinants. They are exact controls for the displayed
example, not evidence of an LND realization or a general theorem.
These identities are now covered by the standalone
[rescaling and curve controls](rescaling_curve_controls_pass18.py),
whose execution is in [the pass-18 log](../verification-pass-18.json).

## 4. A stronger exclusion: no everywhere-unibranch component

**Proposition.** A disconnected union of polynomial curves having
one irreducible component unibranch at every point is a union of
parallel coordinate lines after a polynomial automorphism.

Let \(C_0\) be that component. Its finite normalization
\(\mathbb A^1\to C_0\) is bijective and hence a homeomorphism
in the complex topology. Thus \(C_0\) is topologically contractible.
The Lin--Zaidenberg and Abhyankar--Moh--Suzuki theorem, in the
combined formulation of Palka's Theorem A, gives polynomial
coordinates in which its equation is \(u^a-v^b=0\), with
coprime positive integers \(a,b\).[^3]

If either exponent is one, \(C_0\) is a coordinate line. The
pencil lemma then puts every other component in a parallel
coordinate fiber. Suppose instead that \(a,b\ge2\). Another
disjoint polynomial curve has a nonconstant polynomial
parametrization \((A(t),B(t))\). Constancy of units gives

\[
A(t)^a-B(t)^b=c,\qquad c\in\mathbb C^*.
\tag{8}
\]

Both \(A,B\) must be nonconstant, and they are coprime. Differentiate
(8). Coprimality implies

\[
A^{a-1}\mid B',\qquad B^{b-1}\mid A'.
\tag{9}
\]

Writing \(d_A=\deg A\) and \(d_B=\deg B\), this gives
\((a-1)d_A\le d_B-1\) and
\((b-1)d_B\le d_A-1\). Since both exponents are at least two,
these inequalities contradict one another. Thus the singular
contractible case cannot have a disjoint polynomial curve, proving
the proposition.

Combining this proposition with the plinth rank criterion proves:

\[
\boxed{\text{If a primitive rank-three plinth support is disconnected,
every irreducible component has a multibranch singularity.}}
\tag{10}
\]

This uses the contractible-curve theorem as a published input. It
does not reconstruct Palka's surface-theoretic proof. The nodal
example (5) shows that the remaining multibranch distinction is
substantive.

## 5. Coefficients reduce to interpolation in the same polynomial

In the disconnected situation (3), let
\(p_{\rm red}=\prod_i(F-a_i)\). If \((B,p)C=C\), the
restriction of \(B\) to each component is a nonzero constant
\(c_i\). Choose a Lagrange interpolation polynomial
\(b(T)\in\mathbb C[T]\) with \(b(a_i)=c_i\). Then

\[
B=b(F)+p_{\rm red}Q,
\qquad Q\in C,
\qquad\gcd\bigl(b(T),\prod_i(T-a_i)\bigr)=1.
\tag{11}
\]

Indeed the difference vanishes on every irreducible component,
so is divisible by their squarefree product. Thus in the squarefree
case the coefficient issue is \(B=b(F)+pQ\), with potentially
nonconstant \(b\), not an arbitrary unrelated set of component
functions. This does not itself construct polynomial kernel
coordinates when \(F\) is a noncoordinate.

## 6. What remains unresolved in this investigation

The primitive rank-two example
\(D=u(u-1)\partial_v+2v\partial_w\) has disconnected plinth
support \(u(u-1)=0\); it is documented in the
[unit-restriction note](plinth-units-pass18.md). Hence primitivity
alone does not settle connectedness. The full rank-three
Dasgupta--Gaifullin family treated in pass 17 has plinth \(f^nh\),
whose reduced support is two intersecting kernel-coordinate axes.
It supplies no disconnected rank-three example.

The remaining realization question can now be stated narrowly:

> Can the plinth generator of a primitive rank-three LND on
> \(\mathbb C^{[3]}\) have the form (3), where every fiber
> \(F=a_i\) is an irreducible polynomial curve with a multibranch
> singularity and \(F\) is not a kernel coordinate?

An exclusion of these configurations would prove connectedness.
An actual primitive LND realizing one would disprove it. The
pair of nodal cubics proves neither, because it does not supply
an embedding of the kernel together with the required LND and
minimal local slice on polynomial three-space.

The current Kaliman input gives polynomial normalizations, while
the rank criterion tests coordinates in the kernel. No checked
source in this bounded investigation bridges that remaining gap.
Failed searches are not used as proof that the question is open,
or as evidence of novelty.

## Sources

[^1]: Shulim Kaliman, [*Free C+-actions on C3 are translations*](https://www.math.miami.edu/~kaliman/library/Ka.invent.2004.c%2B.pdf), final author version, Proposition 3.2 and Theorem 5.2(i). Polynomial curve means normalization \(\mathbb A^1\), not a smooth embedded line.
[^2]: Nikhilesh Dasgupta and Sergey Gaifullin, [*On locally nilpotent derivations of polynomial algebra in three variables*](https://www.mathnet.ru/eng/sm10094), *Sbornik: Mathematics* 216(4) (2025), 456-484, Propositions 5.3-5.4 and Theorem 5.7 with its proof. The published full HTML was checked directly.
[^3]: Karol Palka, [*A new proof of the theorems of Lin-Zaidenberg and Abhyankar-Moh-Suzuki*](https://arxiv.org/pdf/1405.5391), arXiv:1405.5391v2, February 9, 2015, Theorems A and B. This is a primary proof source for the contractible-curve classification used in Section 4.
