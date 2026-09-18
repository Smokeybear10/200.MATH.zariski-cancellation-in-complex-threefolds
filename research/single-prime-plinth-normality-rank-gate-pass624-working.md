# A normal exceptional surface forces rank two for a single-prime plinth

Private, source-dependent proof note. General complex-threefold cancellation
remains UNSOLVED. This note does not prove that the exceptional surface is
normal, does not construct coordinates on an arbitrary modification, and does
not establish novelty. No human expert or proof-assistant certification is
claimed.

## 1. Statement

Let R=C[x,y,z], let D be a nonzero primitive locally nilpotent derivation,
and write A=ker(D)=C[a,b]. Primitive means that the coefficients of D have
no common nonunit divisor in R. Suppose

    pl(D) = D(R) intersect A = f^e A,

where f is irreducible and nonconstant in A and e>=1. Units can be absorbed
into a choice of local slice, so choose r in R with D(r)=f^e. Put

    Gamma = Spec(A/fA),      E = Spec(R/fR).

Then the following conditions are equivalent:

1. E is normal.
2. E is smooth.
3. E is isomorphic to the affine plane.
4. f is a coordinate of R.
5. f is a coordinate of A.
6. Gamma is smooth.
7. D has rank two.

Here a coordinate of a polynomial ring is an element that belongs to a
polynomial coordinate system. Rank is the least number of moved coordinates
among all coordinate systems of R.

In particular, if E has at most isolated singularities, all seven conditions
hold and E in fact has no singularities. The exponent two is not special:
the assertion holds for every e>=1.

There is also a pointwise obstruction, whether or not E is normal:

    pi^(-1)(Sing Gamma) is contained in the nonnormal locus of E,

where pi:Spec(R)->Spec(A) is the quotient. This is an inclusion, not an
equality.

## 2. Imported results and their exact scopes

The following are inputs, not claims proved computationally here.

- [Kaliman, final author version](https://www.math.miami.edu/~kaliman/library/Ka.invent.2004.c%2B.pdf),
  Lemma 2.1, Remark 3.3 and Theorem 5.2(i): the quotient in the present
  polynomial-threefold setting is surjective, has one-dimensional fibers,
  and is faithfully flat; every component of the retained exceptional
  curve has normalization A1. "Polynomial curve" does not mean smooth.
- The already retained argument in
  [whole-plinth-component-pass16, Section 2](whole-plinth-component-pass16.md)
  identifies that retained exceptional curve with the reduced plinth
  support for a primitive action. This identification is a separate
  deduction, not wording quoted from Kaliman's theorem. Here its support
  has the single component Gamma. Consequently Gamma has normalization A1.
- [Serre's normality criterion](https://stacks.math.columbia.edu/tag/031S):
  a Noetherian ring is normal exactly when it satisfies R1 and S2.
- The complex Abhyankar-Moh-Suzuki embedding theorem, stated with a proof
  in [Vistoli, page 2](https://arxiv.org/pdf/math/9904035v3), rectifies an
  embedded affine line in the affine plane.
- [Dasgupta-Gaifullin, Lemma 2.15(ii)](https://arxiv.org/html/2306.00510v2):
  a kernel coordinate f is an ambient coordinate if some element has
  nonzero derivative in C[f]. We use the actual polynomial ring R and
  the actual equation D(r)=f^e, not an unknown stably polynomial ring.
- [Barkatou-El Houari-El Kahoui, Theorem 4.1](https://arxiv.org/pdf/0705.2489):
  for a primitive LND of rank other than one, rank two is equivalent to
  the plinth generator being a polynomial in one kernel coordinate.

## 3. Integral surface and the singular-fiber obstruction

The kernel A is factorially closed in R. Indeed D-degree is additive on
nonzero products, so every factor of an invariant is invariant. If f
factored nontrivially in R, both factors would lie in A, contradicting its
irreducibility there. R and A have the same units, C*. Since R is a UFD,
f is prime in R. Thus E is an integral hypersurface surface.

An integral hypersurface in smooth three-space is Cohen-Macaulay and
satisfies S2. By Serre's criterion E is normal exactly when it has no
codimension-one singular component. Its singular locus is closed and
proper, so this is equivalent to its having dimension at most zero
(including an empty singular locus).

Write f=F(a,b) for an irreducible polynomial F in two independent
variables. If q is a singular point of Gamma, then

    F_a(q)=F_b(q)=0.

For each ambient coordinate x_i in {x,y,z}, the chain rule gives

    partial_(x_i) f
      = F_a(a,b) partial_(x_i) a + F_b(a,b) partial_(x_i) b.

Both coefficients vanish everywhere on pi^(-1)(q). Therefore that entire
fiber lies in Sing(E), by the hypersurface Jacobian criterion over C.
The fiber is nonempty by surjectivity. Each irreducible component has
dimension one: it has no surface component by the quotient theorem,
and the two defining equations a-a(q), b-b(q) cannot have a
zero-dimensional minimal component in the three-dimensional regular R.

The fiber therefore contains a codimension-one singular component of E.
If E is normal, this contradicts R1. We have proved

    E normal  ==>  Gamma smooth.

The argument is pointwise as well. For any closed point P above q,
choose a curve component of the fiber through P. Its generic point is
singular and has height one in the local surface ring at P. That local
ring fails R1 and is not normal. The generic points of those curve
components also fail normality. This proves the stated nonnormal-locus
inclusion.

There is an independent algebraic reconstruction of the same obstruction.
Base change gives a faithfully flat inclusion A/fA -> R/fR. Normality
descends along this inclusion: if c/d in Frac(A/fA) is integral over A/fA,
it is integral over R/fR. Normality of R/fR puts c/d in R/fR, whence
c belongs to d(R/fR) intersect (A/fA) = d(A/fA) by faithful flatness.
Thus A/fA is normal, and a normal complex curve is smooth. The local
faithfully flat maps give the pointwise conclusion too.

## 4. From a smooth curve to a polynomial coordinate

By the retained-curve input, the normalization of Gamma is A1. If Gamma
is smooth, its normalization map is an isomorphism. Thus Gamma itself
is A1. Abhyankar-Moh-Suzuki sends this embedded curve in Spec(A)=A2
to a coordinate line. The ideals of the two irreducible curves then
differ by a nonzero constant, so their defining polynomials differ by
a nonzero constant. Consequently f is a coordinate of A.

The equation D(r)=f^e belongs to C[f] and is nonzero. The coordinate
transfer lemma applies and makes f a coordinate of R. It follows that
E is A2, hence smooth and normal. A coordinate f of A also directly
makes Gamma a smooth coordinate line. This proves equivalence of
conditions 1 through 6; in particular no converse to normality descent
was assumed.

Since D fixes the ambient coordinate f, its rank is at most two.
Rank zero is excluded by D nonzero. If its rank were one, choose
coordinates u,v,w with D(u)=D(v)=0. Local nilpotence implies
D=h(u,v) partial_w. Primitivity forces h to be a nonzero constant,
giving a slice and unit plinth. This contradicts the nonunit generator
f^e. Its rank is therefore exactly two.

Conversely, suppose the rank is two. The rank criterion says
f^e=ell(u) for some coordinate u of A and nonconstant ell in C[T].
Factor ell over C. Since f is irreducible in A=C[u,v], all its
irreducible factors u-c must be associates of f. There is only one
distinct root, so f is a nonzero constant multiple of u-c. Thus f
is a coordinate of A, proving the remaining equivalence.

## 5. Scope of the reduction

For a hypothetical primitive rank-three action with sole plinth f^2,
Gamma must be singular and E must be nonnormal. Every point above a
singular point of Gamma is nonnormal on E. The same conclusion holds
with any positive exponent e.

This does not eliminate those possibilities. In particular:

- A hypersurface in a smooth ambient threefold can be nonnormal;
  ambient smoothness alone is not a normality argument.
- Normalization Gamma^nu=A1 does not exclude cusps.
- The conclusion cannot be applied separately to a factor of a
  multi-prime plinth: D(r) then need not belong to C[f].
- No finite calculation of higher-image ideals proves their
  principality in every degree.
- None of the equivalences gives an isomorphism for an arbitrary
  threefold whose cylinder is A4.

The conditional criterion follows from the imported results and elementary
algebra. It is not presented as a new theorem. Earlier project notes
nodal-surface-constraints-pass19 and ambient-residue-obstruction-pass32
already contain the singular-fiber chain-rule observation. The general
single-prime equivalence is the point recorded here, not a new claim for
that older observation.

The next proof obligation is to exclude the singular/non-normal
configuration using a property specific to R=C^[3], or to construct and
verify an example in that exact ring. A control in a different smooth
factorial threefold cannot satisfy this obligation by analogy.
