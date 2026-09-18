# Boundary primality for a proposed flow-affine coordinate

This note concerns the missing ACTUAL-coordinate entry step, before
any supplied chart264. It proves an elementary necessary divisorial
condition for a coordinate in ker(E^2), and gives a concrete
counterexample to promoting a generic coordinate using smoothness
and differential tests alone.

The counterexample is inside a translation with polynomial kernel.
It does NOT contradict existence of a different flow-affine actual
coordinate, and does not contradict cancellation. Its underlying
linear-variable family is already covered by an earlier classification
in this workspace; no novelty is asserted for it or for the argument.

## 1. Arbitrary sliced input and what an affine candidate means

Let

\[
 B=A[u]\simeq\mathbb C^{[4]},\qquad
 E=\partial_u,\qquad A=\ker E,\qquad Eu=1.
\tag{1}
\]

The polynomial u is the supplied global slice. It is NOT assumed
to be a member of an ambient polynomial coordinate system.
Calling u an actual coordinate here would already identify
A=B/(u) with a polynomial three-ring.

Characteristic zero gives

\[
 \ker E^2=A\oplus Au.
\tag{2}
\]

Thus every proposed flow-affine coordinate has a unique expression
f=au+b with a,b in A. An ACTUAL coordinate means that there are
three polynomials g_1,g_2,g_3 in B such that
B=C[f,g_1,g_2,g_3], with a polynomial inverse to this presentation.
A generic coordinate over Frac(A), a localized coordinate, or a
unimodular differential is not the same assertion.

Two elementary properties of A will be used, with no recognition
of A assumed:

\[
 A\text{ is a UFD},\qquad A^*=\mathbb C^*.
\tag{3}
\]

For the units, an A-unit is a B-unit and B^*=C*. For factoriality,
factor a nonzero element of A into irreducibles in the polynomial
ring B. Additivity of u-degree in the domain A[u] makes every
factor have u-degree zero, hence belong to A. Each remains
irreducible in A, and uniqueness follows from uniqueness in B,
whose units agree with those of A. This proves (3) directly from
the stable polynomial ring. It does not assume A is itself a
polynomial ring.

## 2. The necessary boundary-primality statement

Suppose

\[
 f=au+b\text{ is an actual coordinate of }B,\qquad
 a\in A\setminus\{0\},\quad b\in A.
\tag{4}
\]

If a is a nonunit, factor it in A as

\[
 a=\varepsilon\prod_{i=1}^r\pi_i^{e_i},\qquad
 \varepsilon\in\mathbb C^*,\quad e_i\ge1,
\tag{5}
\]

with pairwise nonassociate prime elements pi_i. For a chosen i,
put

\[
 \pi=\pi_i,\qquad
 S=\prod_{j\ne i}\pi_j,\qquad A'=A[1/S].
\tag{6}
\]

The empty product is one. No new root or coefficient-field
extension is involved.

**Necessary condition.** For EVERY c in C,

\[
 \boxed{A'/(\pi,b-c)\text{ is either the zero ring or an
 integral domain}.}
\tag{7}
\]

Equivalently, on the divisor pi=0 away from the other speed
divisors, every scheme-theoretic fiber of the restricted b is
empty or integral. Reducedness is included in the word integral.
This is only a necessary condition for the actual coordinate f.

### 2.1. Injection and all localization licenses

Fix c and let

\[
 R_c=B/(f-c).
\tag{8}
\]

Because f is an actual coordinate, R_c is a polynomial three-ring.
In particular it is a nonzero UFD and a domain.

The map A to R_c is injective. Indeed, a nonzero multiple of
au+b-c in A[u] has u-degree at least one, since a is nonzero
and u-degree is additive in this domain. It cannot be a nonzero
element of A. Thus (f-c)B intersect A is zero.

Consequently every pi_j and S in (5),(6) remains nonzero in R_c.
There is no exceptional c for which this localization kills R_c.
Set R'=R_c[1/S], again a nonzero UFD containing A'. Eliminating
u after inverting a gives the exact isomorphism

\[
 R_c[1/a]\simeq A[1/a],\qquad
 u\longmapsto\frac{c-b}{a}.
\tag{9}
\]

In R', a is a unit times pi^{e_i}, so this is also

\[
 R'[1/\pi]\simeq A'[1/\pi].
\tag{10}
\]

The injections and isomorphisms in (9),(10) follow from the stated
relations in domains, not a claim that rational coordinates
extend across the speed divisor.

### 2.2. The unit calculation and the prime boundary

Factoriality (3) gives

\[
 (A'[1/\pi])^*=(A')^*\pi^{\mathbb Z}.
\tag{11}
\]

In more detail, the units of A[1/a] are exactly a nonzero complex
constant times an integral power of each pi_j. Those with no
pi_i contribution are precisely the units of A'. Prime powers
e_i in (5) do not alter this unit description.

If pi is a unit in R', then R'/(pi) is the zero ring. On the
other hand, direct reduction of the defining equation gives

\[
 R'/(\pi)\simeq\bigl(A'/(\pi,b-c)\bigr)[u].
\tag{12}
\]

The coefficient ring on the right is then zero, establishing the
empty case of (7).

Suppose instead that pi is a nonunit in R'. We show that it is
irreducible there. If pi=gh with g,h in R', then both factors
are units after inverting pi. By (10),(11),

\[
 g=\epsilon_1\pi^k,\qquad
 h=\epsilon_1^{-1}\pi^{1-k},
 \qquad \epsilon_1\in(A')^*,\quad k\in\mathbb Z.
\tag{13}
\]

These are identities in the common fraction field, and the
displayed factors lie in R'. If k<0, multiplying g by a unit
of A' and a suitable nonnegative power of pi puts pi^{-1} in
R', contradicting the present nonunit case. If k>1, the same
argument applies to h. Hence k is zero or one. In either case
one of g,h is already a unit in A', and thus in R'. This proves
irreducibility.

Since R' is a UFD, pi is prime. Therefore R'/(pi) is an integral
domain. By (12), its coefficient ring A'/(pi,b-c) is a nonzero
domain as well. This completes the proof of (7), including all
localization and unit cases.

### 2.3. Zero and unit speeds are not silently classified

If a=0, then f belongs to A and the theorem does not apply.
If such an f is an actual coordinate, it is an invariant ambient
coordinate, an additional assertion not supplied by (2).

If a is a unit, then a belongs to C*, and (5) has no prime
factors. The boundary condition is vacuous. In fact
R_c is then isomorphic to A by solving u=(c-b)/a. Calling f
an actual coordinate in this case would again identify A with
C^[3]. The note does not treat the vacuous condition as sufficient,
and does not conclude that every unit-speed slice is a coordinate.

## 3. A smooth flow-affine generic coordinate that is not a coordinate

Take the actual polynomial ring and sliced derivation

\[
 B=\mathbb C[x,y,z,u],\qquad
 E=\partial_u,\qquad A=\mathbb C[x,y,z],
 \qquad f=x^2u+y^2+x.
\tag{14}
\]

Then

\[
 Ef=x^2,\qquad E^2f=0.
\tag{15}
\]

The differential of f is unimodular in the ACTUAL ambient ring,
as the explicit certificate shows:

\[
 (1-2xu)\,f_x+4u^2 f_u
   =(1-2xu)(1+2xu)+4u^2x^2=1.
\tag{16}
\]

Thus there are no critical points. Every hypersurface fiber
f=c is smooth: its ambient partial derivatives generate the
unit ideal after passage to that fiber.

Every such fiber is also nonempty and irreducible. Nonemptiness
follows by taking x=1,y=0 and u=c-1. To prove irreducibility,
regard f-c as a polynomial of degree one in u over the UFD
C[x,y,z]. Its two coefficients x^2 and y^2+x-c are coprime:
modulo x, the latter is y^2-c, which is never the zero polynomial
for any c in C. The polynomial is primitive and is irreducible
over C(x,y,z)[u], so Gauss's lemma proves it irreducible in B.
Since B is a UFD, each fiber ring is a domain.

The function is a coordinate after inverting x, with both inverse
directions explicit:

\[
 B[1/x]=\mathbb C[x,x^{-1},y,z,f],\qquad
 u=\frac{f-y^2-x}{x^2}.
\tag{17}
\]

It is in particular a coordinate in the one-variable polynomial
ring Frac(A)[u]. The denominator x^2 in (17) has not disappeared
from the original ring.

### 3.1. The exact nonfactorial fiber

For c=1, write

\[
 R=\mathbb C[x,y,z,u]/(x^2u+y^2+x-1).
\tag{18}
\]

This is a smooth domain, and

\[
 R[1/x]=\mathbb C[x,x^{-1},y,z],\qquad
 R/(x)=\mathbb C[y,z,u]/(y^2-1).
\tag{19}
\]

The last quotient is nonzero and is not a domain: the two
nonzero classes of y-1 and y+1 multiply to zero. Thus x is a
nonunit and not a prime element of R.

Nevertheless x is irreducible. In any factorization x=gh in R,
both factors become units in the Laurent polynomial ring in
(19), whose units are exactly C*x^Z. Hence
g=lambda*x^k and h=lambda^{-1}*x^{1-k} for an integer k.
If k<0 or k>1, one factor would put x^{-1} in R, contradicting
the nonzero quotient R/(x). Thus k=0 or1, and one factor is a
nonzero complex constant. This proves irreducibility.

So R contains an irreducible nonprime element and is not a UFD.
If f were an actual coordinate of B, then R=B/(f-1) would be
a polynomial three-ring, a contradiction. Therefore

\[
 \boxed{f\text{ is not an actual polynomial coordinate}.}
\tag{20}
\]

This is also the direct failure of (7): here a=x^2, pi=x and
S=1, while

\[
 A/(\pi,b-1)=\mathbb C[y,z]/(y^2-1)
\tag{21}
\]

is neither zero nor a domain. The f-fibers themselves are smooth
integral threefolds. Their further intersections with x=0 need
not be integral; (19) is precisely such a boundary intersection.
There is no conflict between these two statements.

## 4. The entry shortcut that this rules out

Even in an actual sliced polynomial four-ring, the following
properties of a specified f do NOT imply it is an actual coordinate:

- E^2f=0 and Ef nonzero;
- f becomes a coordinate over Frac(A), or after inverting Ef;
- the ambient differential df is unimodular;
- every complex fiber f=c is nonempty, smooth and irreducible.

All four hold simultaneously for (14). The missing issue is
polynomial completion across the speed divisor, not finding a
generic affine parameter or checking nonsingularity alone.

This does not refute the weaker existence assertion

\[
 \mu(E):=\min\{\deg_E g:\ g\text{ an actual coordinate of }B\}\le1.
\tag{22}
\]

For the example, x,y,z are invariant actual coordinates, and u
is an actual coordinate slice. In particular mu(E)=0. Nor is
the example a hypothetical cancellation counterexample:
A=C[x,y,z] is explicitly polynomial. Condition (7) is a way to
reject a proposed coordinate witness, not a construction of a
different witness and not a sufficient condition for one.

The same point applies to arbitrary sliced input (1). The supplied
slice u already makes the unit-speed boundary test vacuous.
An entry theorem must still supply actual polynomial completion,
or use a recognition argument which independently avoids that
completion. This note does not claim to establish such a theorem.

## 5. Provenance, checked source boundary and verification

The full principal chart264 was reread to separate its supplied
actual1222 frame and entire initial-kernel assumption from its
proved consequences. The older global-entry audits108 and124 were
read as scope context, not imported as an arbitrary entry theorem.
This note does not reuse their failed linear or greedy extraction
controls as new evidence.

There is important pre-existing overlap:
the complete
[linear-variable note](cubic-linear-variable-pass.md)
already treats the family x^m*u+g and includes a related smooth
noncoordinate example. Its classification would also decide
(14). The present proof uses neither that classification nor its
Euler/plane-embedding dependencies: (16)--(21) give a direct
unit and factorization proof, and Section2 applies to arbitrary
intrinsic A in (1). No novelty is claimed for the example,
the affine-modification pattern or the boundary argument.

The primary statement and short proof of
[Bhatwadekar--Gupta--Lokhande, Theorem3.5](https://arxiv.org/html/1501.01438v1)
were checked directly. They assume a nonzero LND of a polynomial
four-ring that fixes an ACTUAL coordinate, and a regular kernel;
the conclusion is polynomiality over that coordinate ring.
They do not produce the invariant actual coordinate. This is a
source-scope observation only; that theorem is not used to prove
(7) or (20), and its deeper dependencies are not recertified here.

Fresh unsaved inline computation48a2a4 verifies (15), the entire
unit certificate (16), and both substitutions in the localized
inverse (17), with zero residuals. The all-c irreducibility,
localization-unit calculation, nonfactorial fiber and arbitrary-A
boundary-primality proof are the written arguments above, not
conclusions of a finite symbolic test.

No saved checker was executed, imported, compiled or rerun.
No earlier source, canonical README or verification ledger was
edited. No unheld source was read. Saved-source review remains
separate from this author's reread and the outline discussion.
There is no claim of universal chart entry, unrestricted
cancellation, novelty or external certification.
