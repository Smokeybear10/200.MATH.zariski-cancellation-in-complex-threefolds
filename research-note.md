# Zariski cancellation: an auditable first investigation

## 1. Question and present conclusion

The working question is

\[
 X\times_k\mathbb A_k^1\cong_k\mathbb A_k^4
 \quad\Longrightarrow\quad X\cong_k\mathbb A_k^3,
 \qquad k=\mathbb C.
\]

No proof or counterexample to this general implication is established here.
The results below identify an equivalent algebraic problem, give complete
elementary proofs in explicit subcases, and isolate the missing step. These
subcases are learning and verification baselines, not novelty claims.

The field and dimension are essential. Affine-space cancellation is known
in dimensions one and two. Gupta gives counterexamples in dimension three
over every field of positive characteristic; the characteristic-zero
three-dimensional question remains open in the literature examined.[^1][^2]
Daigle's 2025 course announcement explicitly states the open complex
three-dimensional case.[^3] This is a bounded literature finding, not a
proof that no later resolution could exist.

The originally supplied conclusion `X ≅ A^1` cannot be correct for general
`r`: the hypothesis gives

\[
\dim X+1=r+1,\quad\text{so}\quad\dim X=r.
\]

For example, `X=A^2` satisfies `X×A^1=A^3`, but is not a line. Replacing the
conclusion by `A^r` is a plausible correction, not a confirmed instruction
from the professor. If instead the intended dimension is one, that is a
known case rather than the open problem considered here.

There is a separate, broader cancellation question with an arbitrary variety
`Y` on the right: `X×A^1 ≅ Y×A^1 ⇒ X ≅ Y`. Its known counterexamples do not
automatically give counterexamples when the right-hand cylinder must be
affine space.[^4]

## 2. What the words mean

A polynomial ring `k[x,y,z]` consists of finite polynomial expressions in
three independent variables with coefficients in `k`. Its corresponding
affine space has three algebraic coordinates. Over `C` this means three
complex coordinates, or six real dimensions topologically.

A variety is described locally by polynomial equations. Multiplication by
`A^1` adds a completely independent coordinate. An isomorphism here is an
algebraic isomorphism over the specified field, not a bijection of point
sets, a drawing, a homeomorphism, or an approximate numerical match.

For affine varieties, an isomorphism can be exhibited by regular maps in
both directions whose two compositions are identities. In explicit affine
coordinates, checking the defining equations and both compositions gives
a concrete way to verify such a certificate. A nonzero or constant Jacobian
determinant alone is not an explicit inverse certificate.

To refute the working conjecture, two different statements must both be
proved for one example: its cylinder really is `A^4`, and the original
threefold really is not `A^3`. Showing only that a threefold is exotic, or
that some familiar invariant agrees with affine space, is insufficient.

## 3. Translate the problem into rings

First, `X` is automatically affine: the zero section `X×{0}` is closed in
the affine variety `X×A^1`, and a closed subvariety of an affine variety is
affine. Put `A=Γ(X,O_X)`. The product condition becomes

\[
 B:=A[t]\cong_k k[x_1,x_2,x_3,x_4].
\]

The desired conclusion is `A ≅ k[u_1,u_2,u_3]`. Throughout the remaining
proofs the rings are commutative domains and maps are `k`-algebra maps.

Under a chosen isomorphism, the added variable `t` becomes a polynomial
`s=s(x_1,x_2,x_3,x_4)`. Setting `t=0` gives

\[
 A\cong B/(s).
\]

This observation does not finish the problem. Renaming `s` as `x_4`
would require proving it is a **coordinate**: that some polynomials
`f_1,f_2,f_3` satisfy

\[
 B=k[f_1,f_2,f_3,s]
\]

with these four elements algebraically independent. The existence of a
coordinate system containing `s` is precisely the information missing
from the naive argument.

### Elementary consequences, and their limits

The coefficient inclusion `A→A[t]` and evaluation `t↦0` make `A` a retract
of `B`. In particular `A` is finitely generated: the evaluations of four
polynomial generators of `B` generate it.

Every unit of `A` is a unit in `B`, so `A*=k*`. Also `A` is a unique
factorization domain. Indeed, factor a nonzero element of `A` in the UFD
`A[t]`. Degrees in `t` add for products of nonzero polynomials over a
domain, so all factors have degree zero and lie in `A`. Irreducibility and
uniqueness transfer for the same reason; the units agree.

The retract also proves smoothness without presuming polynomiality. Given
a `k`-algebra map `A→R/I` for a square-zero ideal `I`, compose it with
the retraction `B→A`. A map from the polynomial ring `B` lifts to `R`
by choosing lifts of its four generators. Restrict the lift to `A`.
Thus `A` is formally smooth. It is finitely presented over the Noetherian
field `k`, hence smooth by the finite-presentation criterion.[^5]
In particular it is regular, a fact used in Section 5.

These are necessary conditions. No step above says that every smooth UFD
of dimension three with constant units is a polynomial ring.

## 4. The slice formulation and its exact proof gap

On `A[t]`, differentiation in `t` fixes every element of `A`. Transport
this operator to `B=k[x_1,x_2,x_3,x_4]`, calling it `D`. It satisfies

\[
 D(fg)=fD(g)+gD(f),\qquad D(s)=1,\qquad \ker D=A.
\]

It is **locally nilpotent**: for each polynomial `f`, some power `D^N(f)`
is zero. The exponent may depend on `f`. An element with `D(s)=1` is called
a **slice**. This is the algebraic description of a translation symmetry
along the added direction. It need not look like an ordinary coordinate
translation in the displayed coordinates of `B`.

### Slice theorem, reconstructed

Let `B` be a domain containing `Q`, let `D` be locally nilpotent, and let
`D(s)=1`. Write `A=ker D`. Then `B=A[s]`, with `s` algebraically
independent over `A`.

For a nonzero `f∈B`, let `n` be the largest integer with `D^n(f)≠0`.
Then

\[
 a_n=\frac{D^n(f)}{n!}\in A.
\]

Because `D^n(s^n)=n!`, the element `f-a_n s^n` has strictly smaller
`D`-degree. Induction expresses `f` as a polynomial in `s` with
coefficients in `A`. Conversely, if a nontrivial relation
`a_0+⋯+a_m s^m=0` existed with `a_m≠0`, applying `D^m` would give
`m!a_m=0`, a contradiction. This proves the theorem.

The associated finite Taylor projection is

\[
 \pi(f)=\sum_{j\ge0}\frac{(-s)^j}{j!}D^j(f).
\]

Local nilpotence makes the sum finite. In the proved decomposition
`B=A[s]`, this is evaluation at `s=0`. Consequently it is a ring
retraction onto `A`, its kernel is `sB`, and `A≅B/(s)`.

### What this proves, and what it does not

It proves that the symmetry has a global product decomposition over
`Spec A`. It does **not** prove that `Spec A` is affine three-space.

For a slice derivation on `k^[4]`, the following are equivalent:

1. `ker D` is a polynomial ring in three variables over `k`.
2. The chosen slice `s` is a coordinate of `B`.
3. After a polynomial change of coordinates, `D` is differentiation in one
   coordinate and fixes the other three.

For `1⇒2,3`, combine polynomial generators of the kernel with `s` in
`B=A[s]`. For `2⇒1`, take the quotient by `s`. For `3⇒1`, compute
the kernel of a coordinate derivative in characteristic zero.

This is a reformulation of the conjecture, not a solution obtained by
changing vocabulary.

## 5. A known theorem identifies a concrete obstruction

Bhatwadekar, Gupta, and Lokhande's Theorem 3.5 states: over a field of
characteristic zero, a nonzero locally nilpotent derivation on
`k[T,X,Y,Z]` which fixes `T` and has regular kernel has kernel
`k[T]^[2]`.[^6]

For the slice situation above, regularity is already proved. Therefore
it suffices to exhibit **one ambient coordinate** `q∈B` with `D(q)=0`.
Transport coordinates so that `q=T`, apply the cited theorem, and the
kernel is polynomial.

The word coordinate cannot be replaced by nonconstant polynomial.
The kernel certainly contains nonconstant polynomials, but establishing
that one belongs to a coordinate system of the larger ring is the issue.

In standard derivation terminology, the remaining possible obstruction is
a rank-four locally nilpotent derivation on four-variable polynomial space
with a slice. Rank here means the minimum number of coordinates not fixed
by `D`, after allowing all polynomial coordinate changes. It is not a
matrix rank, and checking the four currently displayed variables does not
establish it.

No argument here rules out this remaining case. The cited theorem is an
external dependency, not a theorem independently re-proved by the exact
companion.

## 6. An explicit positive subcase with a short certificate

The following elementary calculation supplies a model of what a verifiable
positive result looks like. It is not claimed to be new.

Let `R=k[x,y]` and `B=R[z,w]`. Suppose a slice, expressed in these ambient
coordinates, has the form

\[
 s=a z+b w+c,\qquad a,b,c\in R,
\]

and there are `u,v∈R` such that `au+bv=1`. Set

\[
 g=-vz+uw.
\]

The coefficient matrix has determinant one. More importantly, there are
explicit polynomial inverse formulas:

\[
 z=u(s-c)-bg,\qquad w=v(s-c)+ag.
\]

Substitution gives `z` and `w` back because `au+bv=1`; substitution in
the opposite direction gives `s` and `g` back. Thus

\[
 B=R[s,g],\qquad B/(s)\cong R[g]\cong k^{[3]}.
\]

In the cancellation setting, `ker D≅B/(s)`, so this proves the desired
conclusion under these additional hypotheses. It need not mean that
`ker D` is literally the displayed subring `R[g]`: `D` may move `x,y,g`.
The projection `π` supplies the corresponding generators in the kernel.

For a concrete nonlinear example, take

\[
 a=x,\quad b=1-xy,\quad u=y,\quad v=1,\quad c=x^2+y^3.
\]

Then `au+bv=xy+1-xy=1`,

\[
 s=xz+(1-xy)w+x^2+y^3,\qquad g=-z+yw,
\]

with inverse

\[
 z=y(s-x^2-y^3)-(1-xy)g,\qquad
 w=s-x^2-y^3+xg.
\]

Both compositions are exact polynomial identities. In contrast, merely
knowing `gcd(a,b)=1` in a multivariable ring is insufficient: `gcd(x,y)=1`
but the ideal `(x,y)` does not contain `1`. Local formulas involving
`1/x` or `1/y` do not provide the required global polynomial inverse.

This is a sufficient subcase, not evidence that every slice admits this form.

## 7. The entire affine-linear derivation class is tractable

Another complete baseline concerns derivations whose values on the ambient
coordinates are affine-linear. Write the column of coordinates as `v` and

\[
 D(v)=Nv+b,
\]

where `N` is a constant `n×n` matrix and `b` is a constant column, over a
field of characteristic zero.

**Proposition.** Such a derivation is locally nilpotent exactly when `N`
is nilpotent. In that case it has a polynomial slice exactly when
`b∉im N`. Whenever it has a slice, its kernel is `k^[n-1]`.

First,

\[
 D^j(v)=N^jv+N^{j-1}b\quad(j\ge1).
\]

Local nilpotence on the finitely many coordinate generators forces a
common power of `N` to vanish. Conversely, nilpotence of `N` makes a
power of `D` vanish on each generator. The repeated Leibniz formula then
proves local nilpotence on every polynomial, not merely on the generators.

If `b∈im N`, choose `v_0` with `Nv_0+b=0`. For every polynomial `f`,
`D(f)(v_0)=0`, making `D(f)=1` impossible. If `b∉im N`, linear algebra
provides a row `ℓ` with `ℓN=0` and `ℓb=1`. Then `s=ℓv` is a slice.

For `N^ν=0`, the finite polynomial flow is

\[
 \Phi_t(v)=e^{tN}v+
 \sum_{j=0}^{\nu-1}\frac{t^{j+1}}{(j+1)!}N^j b.
\]

Here the exponential is a finite sum. Multiplying the finite exponential
series and applying the binomial formula to the translation terms gives
`Φ_{t+r}=Φ_t∘Φ_r`. Also `ℓN=0` and `ℓb=1` give
`ℓΦ_t(v)=s(v)+t`. Put
`E(v)=Φ_{-s(v)}(v)`. Then `ℓE(v)=0`, and `E` is constant along the
flow. The map

\[
 v\longmapsto(E(v),s(v))\in H\times\mathbb A^1,
 \qquad H=\{y:\ell y=0\},
\]

has the polynomial inverse `(y,t)↦Φ_t(y)`. Since `H≅A^{n-1}`,
the kernel consists of polynomials on this hyperplane. This proves the
proposition for all affine-linear derivations, not a finite sample.

### A four-variable example

Consider

\[
 D(x)=1,\quad D(y)=x,\quad D(z)=y,\quad D(w)=z.
\]

A slice is `x`. Three invariant coordinates are

\[
 U=y-\frac{x^2}{2},\qquad
 V=z-xy+\frac{x^3}{3},\qquad
 H=w-xz+\frac{x^2y}{2}-\frac{x^4}{8}.
\]

Direct differentiation gives `D(U)=D(V)=D(H)=0`. The inverse formulas
for the change of coordinates `(x,y,z,w)↦(S,U,V,H)` are

\[
 x=S,\quad y=U+\frac{S^2}{2},\quad
 z=V+SU+\frac{S^3}{6},\quad
 w=H+SV+\frac{S^2U}{2}+\frac{S^4}{24}.
\]

The two compositions are identities, establishing
`ker D=k[U,V,H]`. This example is a complete checkable calculation.
It does not test the unresolved nonlinear rank-four case. Generating more
conjugates of this translation produces more positive examples by
construction, not new evidence for a universal claim.

## 8. An attempted graded route and its obstruction

A natural approach is to replace a nonlinear derivation by its highest-degree
part, solve the simpler problem, and lift the solution. This requires proving
that the relevant slice information survives. It need not.

Consider the family

\[
 D_\varepsilon=\varepsilon\partial_x+x\partial_y+y\partial_z+z\partial_w.
\]

All members are locally nilpotent: successive derivatives of each generator
terminate. For `ε≠0`, `x/ε` is a slice. At `ε=0`, the vector field
vanishes at the origin, so `D_0(f)(0)=0` for every polynomial `f` and no
slice can exist. For `D_1`, the degree-zero leading derivation under the
standard grading is exactly `D_0`; the translation term has degree minus
one and disappears.

Thus “a slice derivation has a slice leading derivation” is false. This is
a counterexample to a proof shortcut, not to cancellation. Any filtered
argument must retain additional data or separately prove a lifting theorem.

There is also a useful complete observation about positive gradings. Suppose
the variable weights `w_i` are strictly positive and `D` is homogeneous of
degree `d`, meaning `D(x_i)` has weight `w_i+d` when nonzero. If `d≥0`,
every `D(x_i)` has positive weight, so all vanish at the origin. Consequently
`D` has no polynomial slice. If a slice exists, necessarily `d<0`.

For `d<0`, each monomial in `D(x_i)` has weight strictly less than `w_i`.
It can use only variables with strictly smaller weights. Ordering the
variables by weight therefore makes `D` triangular. The smallest-weight
variable maps to a constant or to zero. If `D(x_min)=c≠0`, then
`x_min/c` is a linear slice and hence a coordinate; quotienting by that
slice proves cancellation.
If it is zero, the smallest-weight variable is an invariant ambient
coordinate, and the known theorem in Section 5 applies in dimension four.

This rules out a counterexample within this positive-weight homogeneous
slice class. It is another elementary reduction to known positive cases,
not a new result. Homogeneous calculations alone do not reach the general
nonlinear case, and the deformation above explains one obstruction to
extending them by leading-term arguments.

## 9. Failed shortcuts and useful negative controls

### Projecting a coordinate need not produce a coordinate

In `k[x,y]`, take `D(x)=1`, `D(y)=2x`, and `g=y-x^2`. Then `D(g)=0`
and `s=x-g^2-g` is a slice. The projection from Section 4 gives

\[
 \pi(x)=g^2+g=g(g+1),\qquad
 \pi(y)=(g^2+g)^2+g=g(g^3+2g^2+g+1).
\]

Both are nonconstant invariants, but neither is a coordinate of `k[x,y]`.
The quotient by either has zero divisors, since the displayed factors are
nonunits; quotienting a polynomial ring by a coordinate would yield a
polynomial domain. Nonetheless

\[
 g=\pi(y)-\pi(x)^2
\]

is a coordinate and generates the kernel. Thus a nonlinear combination of
the projected generators may be essential. Failure of an individual
projection does not prove failure of cancellation, and success in finding
invariants does not yet prove they are coordinates.

### Characteristic zero cannot silently disappear

Over characteristic two, `D=d/dt` has `D(t)=1` but `D(t^2)=0`.
The kernel contains `k[t^2]`, so the characteristic-zero assertion that
`t` is algebraically independent over the kernel is false. The factorials
in the slice proof cannot be divided out. Any proposed proof using that
argument over arbitrary fields has a concrete flaw.

For the geometric conjecture itself, a specialization of Gupta's theorem is

\[
 A=k[x,y,z,t]/(x^2y+z^4+t+t^6),\qquad \operatorname{char}k=2.
\]

The parameters are `p=2,m=2,e=2,s=3`: `m>1`, `4∤6`, and `6∤4`.
Her result, combined with Asanuma's stable-polynomial construction, proves
`A[u]≅k^[4]` but `A≄k^[3]`.[^2] The derivative of the defining
polynomial in `t` is `1` in this characteristic, so this example is smooth.
Checking that derivative does not independently establish either of the
two difficult isomorphism assertions. Those remain dependencies on the
original theorem and its proof.

### Familiar invariants can stop distinguishing spaces

The Koras-Russell cubic
`x+x^2y+z^2+t^3=0` is not affine three-space, although its underlying
complex manifold is diffeomorphic to `R^6`. Dubouloz proved that its
cylinder has trivial Makar-Limanov invariant.[^4] This defeats the
suggestion that the original distinguishing invariant must survive the
extra coordinate. It does not prove that the cylinder is affine space.

More recent characteristic-zero families are explicitly described as
potential cancellation counterexamples, not completed ones. Their
homotopy properties and cylinder comparisons are meaningful but do not
establish the required affine-space cylinder isomorphism.[^7]

### Additional errors to watch for

- An isomorphism after inverting a polynomial is not automatically a global
  isomorphism; the removed fibers and all denominators need attention.
- A nonconstant invariant is not necessarily an ambient coordinate.
- A fixed-point-free derivation is not automatically a slice derivation.
- A proof over rational or complex coefficients is not automatically valid
  in positive characteristic.
- A finite list of examples cannot establish a statement about every
  finitely generated algebra and every polynomial degree.
- A new equivalent formulation may leave the entire original difficulty
  intact. The invariant-coordinate reduction must be judged this way.

## 10. How to decide whether an asserted result is trustworthy

Separate five different questions.

**Is the statement even the intended one?** Write the field, characteristic,
dimension, algebraic category, and quantifiers before trying a proof. Here,
changing an exponent or omitting a field restriction changes the answer.

**Is a claimed background theorem real and applicable?** Locate the
original paper, its exact theorem number, and every hypothesis. For the
positive-characteristic example, inspect Theorem 1.1, Theorem 3.8, and
Corollary 3.9 of Gupta's paper. For the invariant-coordinate reduction,
inspect Theorem 3.5 of Bhatwadekar, Gupta, and Lokhande. An abstract or a
second model's agreement is not a replacement for this comparison.

**Does a deduction actually follow?** Demand intermediate steps. In the
slice argument, ask where characteristic zero is used and where
algebraic independence is proved. In a coordinate claim, ask for the
inverse formulas or a precisely applicable theorem. A sentence such as
“choose coordinates so that the slice is a variable” is an unresolved
claim unless justified.

**What exactly was checked computationally?** The companion verifies
the displayed inverse compositions, derivative identities, a concrete
flow law, and negative controls. It deliberately rejects corrupted inverse
formulas and does not silently accept a nonterminating derivative sequence.
These are exact arithmetic checks. They do not certify the external
theorems, arbitrary derivations, or the universal cancellation implication.
The general statements in Sections 4 and 7 rely on their written proofs,
not on the number of examples that pass.

**Has someone independent reconstructed the proof?** A qualified reader
should check the statement and rebuild the argument without taking its
conclusions as premises. Separate model critiques help find mistakes but
are not independent human mathematical review. A formal proof assistant
can check a fully formalized statement; checking a few identities in it
does not establish the original theorem, and an incorrect formal statement
can still have a valid formal proof. No full formalization is supplied here.

A practical exercise is to verify `D(U)=0` in Section 7 by hand:

\[
 D\left(y-\frac{x^2}{2}\right)
 =x-\frac{2xD(x)}{2}=x-x=0.
\]

Then verify the displayed formula for `z` by substituting the definitions
of `U` and `V`. Finally ask why having two invariants would not yet prove
that the entire kernel is polynomial. The inverse-map argument answers
the stronger question; the derivative calculation alone does not.

## 11. A bounded next research task

The main unproved obligation is not to construct another simple example.
It is to establish a new condition forcing an invariant ambient coordinate
for a class of nonlinear slice derivations not already covered by existing
results, or to find an example and a rigorous obstruction to polynomiality.

The first useful discussion with Luo should settle the intended field and
dimension and identify a particular family, lemma, or prior paper. For an
agreed family, a finite deliverable could consist of:

1. An explicit derivation and a proof of local nilpotence on the generators,
   extended to all polynomials by Leibniz.
2. An explicit slice with the identity `D(s)=1`.
3. A record of known coordinate-preserving results that apply or fail to
   apply, with hypotheses checked rather than inferred.
4. Either explicit polynomial kernel generators and inverse maps, or the
   first rigorously stated obstacle to obtaining them.

The missing family is important. There is no specific nonlinear candidate
in the supplied email, and inventing a claim of novelty for a familiar
triangular family would not advance the open question. The reconstructed
baselines above are useful for learning and testing the eventual method,
but they do not reduce the unsolved case by themselves.

One technically meaningful next question is a carefully stated lifting
criterion for a filtered derivation: which additional hypotheses ensure
that an invariant coordinate in an associated graded ring lifts to an
invariant coordinate in the original polynomial ring? Such a criterion
must survive the deformation counterexample in Section 8 and must be
compared with existing results before any novelty claim. No such general
criterion is asserted here.

## Sources

[^1]: Neena Gupta, *The Zariski Cancellation Problem and related problems in Affine Algebraic Geometry*, ICM 2022 contribution, Section 2, [arXiv:2208.14736v1](https://arxiv.org/html/2208.14736v1); [published chapter DOI](https://doi.org/10.4171/ICM2022/151). Used for the statement and low-dimensional status, not as a replacement for each original proof.

[^2]: Neena Gupta, *On the Cancellation Problem for the Affine Space A³ in characteristic p*, arXiv version dated January 23, 2013, Theorem 1.1, Theorem 3.8, Corollary 3.9, [full text](https://arxiv.org/html/1208.0483v2); *Inventiones Mathematicae* 195 (2014), [DOI](https://doi.org/10.1007/s00222-013-0455-2). The stable-polynomial assertion in Theorem 1.1 is credited there to Asanuma.

[^3]: Daniel Daigle, *Affine Algebraic Geometry: An algebraic approach via locally nilpotent derivations*, University of Padova minicourse, October 2025, [official course description](https://www.math.unipd.it/news/minicourse-affine-algebraic-geometry-an-algebraic-approach-via-locally-nilpotent-derivations/). Explicitly identifies complex three-dimensional cancellation as open; not a complete current-status audit.

[^4]: Adrien Dubouloz, *The cylinder over the Koras-Russell cubic threefold has a trivial Makar-Limanov invariant*, 2008 preprint, introduction and main theorem, [full text](https://arxiv.org/html/0807.4085v1); *Transformation Groups* (2009), [DOI](https://doi.org/10.1007/s00031-009-9051-3). Also distinguishes the generalized cancellation problem.

[^5]: The Stacks Project, Proposition 10.138.13, Tag 00TN, [finite presentation and formal smoothness criterion](https://stacks.math.columbia.edu/tag/00TN). Used after the explicit retract lifting argument.

[^6]: S. M. Bhatwadekar, Neena Gupta, and Swapnil A. Lokhande, *Some K-theoretic properties of the kernel of a locally nilpotent derivation on k[X₁,…,X₄]*, January 7, 2015 preprint, Theorem 3.5, [full text](https://arxiv.org/html/1501.01438v1). This note invokes the theorem with all displayed hypotheses; it does not reconstruct the paper's supporting local-fibration results.

[^7]: Adrien Dubouloz and Parnashree Ghosh, *Algebraic families of higher dimensional A¹-contractible affine varieties non-isomorphic to affine spaces*, January 16, 2025, introduction and main theorem, [arXiv:2501.09613v1](https://arxiv.org/html/2501.09613v1). Used only for the distinction between potential and proved cancellation counterexamples.
