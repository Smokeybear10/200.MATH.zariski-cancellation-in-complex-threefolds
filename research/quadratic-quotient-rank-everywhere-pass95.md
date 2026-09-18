# The quadratic quotient has no rank-zero points

In the supplied actual nonconical quadratic frame, the quotient
differential has rank at least one at every point, not only at
the generic points of its fiber components. The new step isolates
each disjoint smooth reduced component, proves finite freeness
of its entire thickening over an actual component parameter,
and compares the resulting transverse length with the rank-zero
lower bound.

Rank one still permits fixed points of N. This theorem is not
freeness, recognition of A, or an arbitrary-frame reduction.

## 1. The whole fiber and the retained multiplicity gates

Retain the actual nonconical quadratic hypotheses of
[double-component disjointness95](quadratic-double-components-disjoint-pass95.md).
In particular A is a smooth affine complex threefold, N is its
specified primitive canonical Jacobian LND, and
\[
\begin{gathered}
S=\mathbb C[s_1,s_2]=\ker(N|_A),\qquad K=\operatorname{Frac}S,\qquad
A=S[A_1,A_2,c],\qquad A\text{ faithfully flat over }S,\\
A_K=K[w],\qquad \deg_w A_i\le2,\quad \deg_w c\le4,\\
C=A/\mathfrak mA,\qquad
\operatorname{Min}(\mathfrak mA)=\{\mathfrak q_1,\ldots,\mathfrak q_h\},
\qquad 1\le\mu_i,\qquad \sum_i\mu_i\le4 .
\end{gathered}
\tag{1}
\]
Here \(\mathfrak m\) is any closed base point, and \(\mu_i\)
is the length of the whole fiber localized at its generic
component. The total inequality counts every component, by
[total-fiber92](nonconical-total-fiber-multiplicity-pass92.md).
The two base parameters form a regular sequence on A by
flatness. Thus C is a pure one-dimensional Cohen--Macaulay
ring and has no embedded associated primes.

The additive action preserves each reduced component. The
closure of the image of the product of the connected additive
group with one irreducible component is irreducible, contains
that component at the identity, and stays in the fiber.
Maximality of an irreducible component forces that image to
stay in the same component. Thus N restricts to an LND on
each domain \(A/\mathfrak q_i\).

If \(\mu_i>1\), the quotient differential cannot have rank two
at its generic point. Independent base differentials in the
regular two-dimensional transverse local ring would generate
its maximal ideal and make the length one. Hence the canonical
Jacobian N vanishes generically, and then everywhere on that
reduced component. Such a component is fixed.

Conversely, for \(\mu_i=1\), the generic whole-fiber ring is
the component field. The componentwise theorem in
[primitive-fiber54](primitive-fiber-nonvanishing-pass54.md)
makes its induced derivation nonzero. Therefore the restriction
to the reduced component is a nonzero LND. Its kernel has
transcendence degree zero over the algebraically closed field
\(\mathbb C\), so that kernel is \(\mathbb C\). Choose a local
slice for this LND; its nonzero invariant derivative is a
complex constant and can be divided out. The slice theorem
then identifies the component ring with \(\mathbb C[t]\),
with a nontrivial translation action.

## 2. Components are disjoint and their multiplicities are at most three

Two distinct irreducible affine curves have finite intersection.
That intersection is invariant under the action just described.
A nontrivial translation of the affine line has no nonempty
finite invariant subset. Every multiplicity-one component is
therefore disjoint from every other component.

By (1), there are at most two remaining fixed components.
If there are two, both have multiplicity two, and they exhaust
the entire fiber. The actual theorem
[double-component disjointness95](quadratic-double-components-disjoint-pass95.md)
excludes their intersection. Thus all reduced components of C
are pairwise disjoint.

Also \(\mu_i=4\) is impossible. It would consume the entire
bound in (1), making the whole reduced fiber irreducible and
fixed. The whole-irreducible degree-two ramification conclusion
of [ramification92, equation (6)](nonconical-irreducible-fiber-ramification-pass92.md)
forces its multiplicity to be two, a contradiction. A fixed
fiber lies over the retained exceptional curve, as checked
in that proof. This application uses its entire-fiber theorem,
not a claim about one component of a reducible fiber.
Consequently
\[
\boxed{\quad
V(\mathfrak q_i)\cap V(\mathfrak q_j)=\varnothing\ (i\ne j),
\qquad 1\le\mu_i\le3 .
\quad}
\tag{2}
\]
The retained topology is used here to exclude multiplicity four;
the generic-rank exclusion alone would not justify that step.

## 3. Each reduced component has an actual affine-line parameter

All reduced components are smooth and have rings of one of the
following forms:
\[
A/\mathfrak q_i=
\begin{cases}
\mathbb C[\bar U_i],
 &\mu_i=1,\\
\mathbb C[\bar c],
 &\text{fixed and collapsed},\\
\mathbb C[\bar U_i,1/b_i(\bar U_i)],
 &\text{fixed and noncollapsed}.
\end{cases}
\tag{3}
\]
The first case was proved above. In that case choose any actual
polynomial lift \(U_i\in A\) of its coordinate t. The second
case is the actual collapsed-plane conclusion92, with \(U_i=c\).
The third case is
[the noncollapsed-image proof95](noncollapsed-quadratic-local-translation-model-pass95.md),
which also gives \(\mu_i=2\). Its U_i is an actual surviving
constant combination of the two good relative generators.
That proof of the reduced ring did not require a nonzero first
normal action. Use \(b_i=1\) in either of the first two cases.

There is no assertion that all the U_i are one common projection,
or that a polynomial lift of a reduced parameter is an ambient
coordinate. What is needed is that its restriction is a coordinate
on the displayed open affine line.

## 4. The entire component thickening is finite free

Write J for the nilradical of C. It is nilpotent because C is
Noetherian. Disjointness in (2) and the Chinese remainder theorem
give \(C/J=\prod_i A/\mathfrak q_i\). The corresponding idempotents
lift across a nilpotent ideal, so
\(C=\prod_i C_i\), where \(C_i\) has exactly one minimal prime
and its reduced ring is \(A/\mathfrak q_i\).
For completeness, idempotent lifting is finite here: an approximate
idempotent e has \(2e-1\) invertible when \(e^2-e\) is nilpotent;
the correction \(e-(e^2-e)/(2e-1)\) squares the error order.
Iteration terminates, and the finitely many factors can be
split one at a time.

Let U_i also denote the image of the actual lift in \(C_i\).
The element \(b_i(U_i)\) is a unit in \(C_i\): its reduction
is a unit, and an inverse modulo a nilpotent ideal lifts by
a finite geometric sum. Therefore
\(R_i=\mathbb C[U_i,1/b_i(U_i)]\) embeds into \(C_i\).
The embedding is injective because its composite with reduction
is the identity on the ring in (3).

Each of the finitely many algebra generators of \(C_i\) has
residue equal to an element of \(R_i\). Its difference from
that lifted element is nilpotent, and hence satisfies a monic
power equation over \(R_i\). Thus \(C_i\) is a finite
\(R_i\)-module. This proves finiteness rather than presuming it
from the reduced fiber.

Every nonzero element of \(R_i\) has nonzero reduction on the
unique component. Since \(C_i\) has no embedded associated
primes, such an element is a nonzerodivisor. The finite module
is torsion-free over the PID \(R_i\), and is therefore free.
Its rank is \(\mu_i\): localizing by nonzero elements of \(R_i\)
gives the generic Artinian local ring of this whole component,
with residue field \(\operatorname{Frac}R_i=\kappa(\mathfrak q_i)\).
We have proved
\[
\boxed{\quad
C=\prod_i C_i,\qquad
R_i=\mathbb C[U_i,1/b_i(U_i)]\subset C_i,\qquad
C_i\simeq R_i^{\mu_i}\text{ as a module}.
\quad}
\tag{4}
\]
These are actual subrings and module statements. They do not
identify the thickened algebra with a truncated polynomial ring.

## 5. The local transverse length at every point

Take any closed point p on the ith component and put
\(\alpha=U_i(p)\). Then \(b_i(\alpha)\ne0\), and (4) gives
\(C_i/(U_i-\alpha)\) complex dimension \(\mu_i\).
Its reduction is \(\mathbb C\), so it is supported only at p.
All other components are disjoint from p. Consequently
\[
\boxed{\quad
\operatorname{length}
 A_p/(\mathfrak mA_p,U_i-\alpha)=\mu_i\le3 .
\quad}
\tag{5}
\]
The restriction of U_i is a local parameter on the smooth
reduced curve, so \(dU_i(p)\ne0\) in the ambient cotangent
space. The surface local ring \(R=A_p/(U_i-\alpha)\) is thus
regular of dimension two.

Suppose both base differentials vanished at p. The two
centered base functions f,g would then have images in the
square of the maximal ideal \(\mathfrak n_R\).
In a regular two-dimensional local ring with complex residue
field, two such generators impose at most two relations on
the three-dimensional quadratic part. Hence a finite quotient
satisfies
\[
f,g\in\mathfrak n_R^2
\quad\Longrightarrow\quad
\operatorname{length}R/(f,g)\ge 1+2+1=4 .
\tag{6}
\]
This contradicts (5).

Every closed point of A lies over a closed base point, so no
closed point can have quotient rank zero. The rank-zero
condition defines a closed subset of the finite-type complex
variety A; a nonempty such subset would contain a closed point.
Therefore
\[
\boxed{\qquad
\operatorname{rank}(ds_1,ds_2)_p\ge1
\quad\text{at every point }p\in\operatorname{Spec}A .
\qquad}
\tag{7}
\]

## 6. Scope and proof provenance

This upgrades the generic-component conclusion92 for the
actual nonconical quadratic frame. It does not prove rank two,
so it does not remove the rank-one fixed locus, make N free,
or recognize A as a polynomial ring. The cubic branch and
arbitrary sliced actions are outside its hypotheses.

The finite-freeness argument keeps the whole nonreduced fiber,
constructs the embedded parameter ring explicitly, and uses
the absence of embedded primes. It never assumes a localization
or completion of the original action is locally nilpotent.
The entire-fiber topological multiplicity theorem is used only
where the whole fiber has been shown irreducible.

The retained whole-irreducible ramification and total-fiber
proofs92 were reread through EOF for these applications.
The primitive-fiber54 componentwise theorem and the new
noncollapsed-image and double-disjointness proofs retain their
exact scope. No fresh original-source reconstruction, numerical
method, frozen-file edit, historical novelty, expert review,
formal verification, or general cancellation theorem is claimed.
