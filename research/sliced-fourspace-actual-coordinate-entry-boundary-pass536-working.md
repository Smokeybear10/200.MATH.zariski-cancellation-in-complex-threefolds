# Actual-coordinate entry for a sliced polynomial four-ring

This bounded audit separates recognition of the kernel from a possible
weaker coordinate-entry statement. It proves exact equivalences for an
invariant coordinate or a unit-speed coordinate, and records an elementary
sufficient condition using positive diagonal homogeneity. It does not
produce an actual coordinate of E-degree at most one for arbitrary sliced
input. No novelty is claimed for the equivalences or the homogeneity
observation, which may be standard.

## 1. Input and the distinction to preserve

Let

\[
 B=\mathbb C^{[4]},\qquad
 0\ne E\in\operatorname{LND}_{\mathbb C}(B),\qquad
 Eu=1,\qquad A=\ker E.
\tag{1}
\]

The slice theorem gives the actual ring identity

\[
 B=A[u],\qquad E=\partial_u,\qquad
 \ker E^2=A\oplus Au.
\tag{2}
\]

The supplied slice u is not assumed to be an ambient coordinate.
An ACTUAL coordinate f means that B=C[f,g_1,g_2,g_3] for three
polynomials g_i in B. In particular, polynomial completion, not only
completion over Frac(A), is part of the assertion.

Every f in ker(E^2) is uniquely f=au+b with a,b in A. Its E-degree
is zero when a=0 and f is nonzero, and one when a is nonzero.
An actual coordinate is never constant. Since an A-unit is a B-unit,

\[
 A^*=\mathbb C^*.
\tag{3}
\]

Thus degree one has two distinct speed cases: a nonzero complex
constant, or a nonzero nonunit of A.

### Regularity needed for the published endpoint

The ring A is finitely generated because A is isomorphic to B/(u).
It is regular. To see this without assuming that u is a coordinate,
choose any actual polynomial frame x_1,...,x_4 of B. The identity

\[
 1=Eu=\sum_{i=1}^4 E(x_i)\,\frac{\partial u}{\partial x_i}
\tag{4}
\]

shows that the partial derivatives of u generate the unit ideal.
The hypersurface u=0 is therefore smooth by the characteristic-zero
Jacobian criterion. Its ring is A, so A is regular. This proves a
hypothesis of the endpoint below, not polynomiality of A.

## 2. Exact recognition equivalences

Under (1), the following assertions are equivalent:

1. A is isomorphic to C^[3].
2. The supplied slice u is an actual coordinate of B.
3. A contains an actual coordinate of B.
4. There is an actual coordinate f of B with Ef in A^*.

In item4, (3) makes Ef a nonzero complex constant, so E^2f=0
automatically. The equivalence concerns existence; it does not say
that every nonconstant invariant polynomial is a coordinate.

If A=C[a_1,a_2,a_3], then (2) gives the actual coordinate frame
(a_1,a_2,a_3,u), proving items2--4. Item2 implies item1 by taking
B/(u). For item4, write f=au+b using (2), with a in C*. Then

\[
 B/(f-c)\simeq A\quad(c\in\mathbb C),\qquad
 u\longmapsto(c-b)/a.
\tag{5}
\]

An actual coordinate f makes this quotient C^[3], proving item1.
Conversely, if A is polynomial, every f=au+b with a in C* and
b in A is an actual coordinate, by the inverse u=(f-b)/a.

The remaining implication, item3 to item1, uses the primary result
of [Bhatwadekar--Gupta--Lokhande, Theorem3.5](https://arxiv.org/html/1501.01438v1):
over a characteristic-zero field k, a nonzero k[T]-linear LND of
k[T,X,Y,Z] with regular kernel has kernel k[T]^[2].
Given the actual invariant coordinate in item3, use it as T and
complete it to a polynomial frame. Then E(T)=0, E is nonzero,
and regularity was proved above. Every hypothesis is supplied,
so A=C[T]^[2]. The theorem is an endpoint after an invariant
coordinate is known, not a construction of that coordinate.

Consequently, guaranteeing an invariant ambient coordinate for every
input (1) would already guarantee polynomiality of every such A.
The same is true of guaranteeing an actual coordinate with unit speed.
Neither assertion is a weaker entry result in this setting.

## 3. A sufficient additional homogeneity hypothesis

Here is a direct criterion that does not assume the slice is a
coordinate. It is an elementary observation, not a novelty claim.

**Criterion.** Suppose there is an ACTUAL polynomial frame
(x_1,...,x_4) and strictly positive integer weights w_i such that
E is homogeneous for that diagonal grading. Then some x_i has
E(x_i) in C*, and hence is an actual coordinate slice after scaling.
In particular A=C^[3].

Write the homogeneous degree of E as d, so

\[
 \deg_w x_i=w_i>0,\qquad
 E(B_j)\subseteq B_{j+d}.
\tag{6}
\]

Evaluate (4) at the origin of this actual frame. At least one
E(x_i) has nonzero value there. But E(x_i) is homogeneous of
weight w_i+d. A homogeneous polynomial for strictly positive
weights can have a nonzero constant term only when its weight is
zero; the entire weight-zero space is C. Thus

\[
 E(x_i)=c\in\mathbb C^*,\qquad E(c^{-1}x_i)=1.
\tag{7}
\]

The scaled polynomial is still an actual coordinate. Section2
now identifies A. No homogeneity assumption on the supplied u
was used. No generic or localized frame was substituted for the
actual frame in (6).

The intrinsic decomposition B=A[u] has a different grading:
give A weight zero and u weight one. For it E is homogeneous
of degree -1, but its weight-zero ring is all of A, not C.
It supplies neither a strictly positive diagonal grading nor a
homogeneous ambient polynomial coordinate system. Applying the
criterion to this intrinsic grading would omit its essential
actual-frame and positivity hypotheses.

## 4. The nonunit-speed case remains separate

For a proposed actual coordinate f=au+b with nonzero nonunit
a in A, (5) is available only after inverting a. It does not
identify B/(f-c) with A before localization. Sections2 and3
do not settle whether such a coordinate must exist for every
input (1), or whether its existence alone recognizes A.

The held [boundary-primality note525](affine-slice-coordinate-boundary-primality-obstruction-pass525-working.md)
gives a necessary condition for a specified candidate. Its example

\[
 B=\mathbb C[x,y,z,u],\quad E=\partial_u,\quad
 f=x^2u+y^2+x
\tag{8}
\]

has E^2f=0 and Ef nonzero, becomes a coordinate after inverting x,
has unimodular differential, and has smooth integral complex fibers.
Nevertheless f is not an actual coordinate: its fiber f=1 contains
an irreducible nonprime element x. Thus those tests do not certify
a proposed nonunit-speed witness. The same example has the actual
coordinate slice u and invariant coordinates x,y,z. It is not a
counterexample to existence of a different coordinate of degree at
most one, and gives no absence proof for that existence statement.

## 5. Bounded primary-source screen

The following observations concern exact hypotheses, not a
comprehensive account of the literature.

### The 2026 associated multiplicative action

[Cid, arXiv2604.03471v1, Section5 and Theorem5.4](https://arxiv.org/html/2604.03471v1)
equates linearizability of the action generated by NuE with a
polynomial conjugation making E a partial derivative and u its
coordinate slice. This reformulates recognition, without supplying
linearizability. Definition5.1's nice condition already requires
E^2 to kill every member of the specified actual coordinate frame.
Proposition6.11 supplies no obstruction here: ML(B)=C already,
because the ordinary coordinate partial derivatives have common
kernel C.

There is a sign slip in the printed proof of Theorem6.1: with
u'=u+a and a in A, exp(-aE)(u)=u-a, not u'. For the displayed
conjugation towards N(u+a)E, use exp(aE), which commutes with E.
The corrected identity establishes independence of the slice,
but does not establish a coordinate slice. This local correction
is not a criticism of unrelated statements in that paper.

### Polynomial three-rings over an invariant base

[Babu--Das--Lokhande, arXiv2210.10285v1, Corollary1.2](https://arxiv.org/html/2210.10285v1)
concerns a fixed-point-free R-LND on R^[3], with R a PID
containing Q. Its slice criterion yields a polynomial kernel
over R. To use it with R=C[T] inside the present B requires an
invariant T and an actual presentation B=C[T]^[3] first. An
arbitrary invariant, or the intrinsic coefficient ring A in (2),
does not supply that presentation. This result does not remove
the coordinate-entry requirement in Section2.

## 6. Scope and verification record

The bounded conclusion is the equivalence in Section2 and the
conditional criterion in Section3. No unconditional entry theorem
was verified by this screen. That is not a claim that none exists
in the literature, nor a proof that an input (1) can lack every
actual coordinate in ker(E^2). No prescribed chart, initial kernel,
or low-degree frame is inferred from an arbitrary slice.

Note525 was read through EOF at its held SHA
281b494617c8a3e39d74d3d0d567ae577719192ec0aed244b22c4c84576ade0d.
The cited primary statements and their relevant standing hypotheses
were inspected directly. The elementary proofs above are written
arguments; no finite symbolic test replaces a coordinate-completion
claim. The deeper dependencies of the published endpoint are retained,
not recursively certified here.

Only this working note was created. No saved checker was executed,
imported or compiled; no canonical file or prior source was edited.
Author rereading and an independent saved-source audit are separate.
