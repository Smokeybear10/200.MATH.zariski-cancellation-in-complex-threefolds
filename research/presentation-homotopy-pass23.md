# Interpolating modification presentations: exact family and failed transport

The interpolation produces a genuine smooth family, a uniform finite-center
presentation, and compatible trivializations of every finite thickening of
its starting fiber. It does not yet produce polynomial coordinates over the
parameter ring. A natural polynomial horizontal derivation can be constructed
for every input, but it is never locally nilpotent for a nonconstant
interpolation. Thus integrating that derivation is not a valid general
coordinate-descent step.

This bounded pass proves those assertions and isolates an exact additional
hypothesis under which a published residual-variable theorem would finish
the recognition. It neither proves general recognition nor claims novelty.
Date: 2026-09-13. No registry edits or external communications.

## 1. Setup and a uniform Bezout identity

Write \(k=\mathbb C\) for the ground field and reserve C for the invariant ring.
Let
\[
R=\mathbb C[x_1,x_2,x_3],\quad
0\ne D\in\operatorname{LND}(R),\quad C=\ker D,
\quad Dr=p\ne0.
\]
For the research target D is primitive, r is minimal, and C is the
polynomial two-ring. The following construction needs only these displayed
local-slice data and the stated polynomial ambient ring.

Assume p is a nonunit and
\[
V=1+d,\qquad d\in\sqrt{pC},\qquad
v=V_\lambda=1+\lambda d\in C[\lambda].
\tag{1}
\]
The case d=0 is the constant family R[lambda]. The unit-plinth case
already has R=C[r] and is polynomial by eliminating r from the
presentation below. We henceforth treat the nontrivial case d != 0.

Choose k >= 1 with d^k in pC and set
\[
G=\sum_{j=0}^{k-1}(-\lambda d)^j,\qquad
A=\frac{(-\lambda)^k d^k}{p}\in C[\lambda].
\]
Then, exactly in C[lambda],
\[
pA+vG=1.
\tag{2}
\]
In particular (p,v)=1 before any specialization. Since a nonzero
element of sqrt(pC) cannot be a nonzero constant, 1+c d is a nonzero
polynomial for every complex c. Thus the original modification is
defined at every parameter value, not just generically.

## 2. The universal interpolation lemma

Define
\[
\mathcal B=R[\lambda,w]/(vw-r).
\tag{3}
\]
The following statements hold simultaneously:

1. This is the exact domain R[lambda][r/v] in R[lambda,v^-1].
2. For every scalar c in k,
   B/(lambda-c) is the exact modification R[r/(1+c d)]. In particular
   B/(lambda)=R and B/(lambda-1)=R[r/V].
3. B is smooth over k[lambda], of relative dimension three.
4. B[s] is isomorphic to R[lambda,t] as a k[lambda]-algebra.
5. Every finite lambda-adic thickening of B is canonically isomorphic
   to the corresponding thickening of R[lambda], fixing the old R.

Here and below B abbreviates the script B in (3).

**Exact presentation and fibers.** The polynomial v is primitive linear
in lambda and has no common factor with r in the UFD R[lambda]. Thus
vw-r is primitive and irreducible as a polynomial in w. Its quotient
is a domain and embeds into the localization by w=r/v.

For a fixed c, any irreducible common factor g of 1+c d and r would
belong to C by factorial closure of the kernel. Then g would divide
Dr=p, contradicting (2). The same primitive-polynomial argument proves
the claimed fiber presentation. This verifies base change directly;
commutation of arbitrary affine modifications with specialization has
not been assumed.

**Smoothness.** Write F=vw-r. Extend D to kill lambda,w. Then
DF=-p, while partial_w(F)=v. Equation (2) shows that the ideal of
relative partial derivatives of F is the unit ideal. The standard
smooth hypersurface criterion gives smoothness over k[lambda], with
relative dimension three. Its exact algebraic statements are Stacks
Definition 10.137.5 and Lemma 10.137.6.[^1] Consequently the map is
flat; its explicitly nonempty fibers also make it surjective.

**Uniform stable triviality.** On R[lambda,t] the derivation
\[
\mathcal E=A D+G\partial_t
\]
is locally nilpotent, because its two summands commute and their
coefficients are invariant. The element s=r+vt satisfies
\[
\mathcal E(s)=Ap+vG=1.
\]
The slice theorem identifies ker(E) with the quotient by s, which is
(3) under w=-t. Hence
\[
\mathcal B[s]\cong_{\mathbb C[\lambda]}R[\lambda,t].
\tag{4}
\]
The invariant embedding C is also preserved. Specializing this identity
proves stable polynomiality of every fiber, but not polynomiality of
each unstabilized three-ring.

**Finite thickenings.** In R[lambda]/(lambda^m), v has inverse
\[
\sum_{j=0}^{m-1}(-\lambda d)^j.
\]
Eliminating w gives compatible isomorphisms
\[
\mathcal B/(\lambda^m)
\cong_R R[\lambda]/(\lambda^m)
\quad(m\ge1).
\tag{5}
\]
Thus the lambda-adic completion is R[[lambda]]. This is a statement
about the inverse limit of finite quotients. It does not identify
B tensor k[[lambda]] with the polynomial algebra k[[lambda]][x_1,x_2,x_3].
Unbounded degrees in the old coordinates are allowed in R[[lambda]],
but not in a polynomial ring over k[[lambda]].

## 3. The finite-center and chart descriptions are uniform as well

Use the [pass-21 finite-center lemma](universal-bridge-pass21.md).
Choose N with p^N x_i in C[r] for each old coordinate, set
\[
S=C[T],\quad I=p^NR\cap S,
\quad\theta_\lambda(T)=vT,\quad
J_\lambda=\theta_\lambda(I)S[\lambda].
\]
The same N works for the entire interpolation:
\[
\mathcal B\cong_{C[\lambda]}
S[\lambda][J_\lambda/p^N].
\tag{6}
\]
Indeed under T=w, theta_lambda(F)/p^N becomes F(r)/p^N.
Those fractions recover all old coordinates, while w is already
present. Equation (2) makes theta_lambda an automorphism modulo p^N.
Every specialized center gives the correct fiber by Section 2.

There is also an exact two-chart cover:
\[
\mathcal B_v=R[\lambda]_v,\qquad
\mathcal B_p=C_p[\lambda,w],\qquad r=vw
\text{ on the overlap}.
\tag{7}
\]
These are charts controlled by functions on the invariant plane as
well as lambda. They are not an open cover pulled back from the
parameter line, so they do not establish Zariski local triviality
over that line.

The [pass-22 center countercontrol](center-recognition-pass22.md)
also rules out a finite chain that stays inside the same polynomial
ambient S and transports full centers by automorphisms preserving
the same reduced denominator support: composing such a chain would
give the prohibited endpoint automorphism. This statement permits
arbitrary intermediate ideals but fixes that ambient ring and
support. It says nothing against genuinely changing the denominator
presentation or passing through different overrings. No theorem
making those more general changes terminate at polynomial coordinates
has been established here.

## 4. A regular horizontal derivation exists, but its flow is not polynomial

There is an explicit derivation on B that lifts differentiation in
the parameter and fixes the invariant plane:
\[
\nabla(\lambda)=1,\qquad
\nabla|_R=A d w D,\qquad
\nabla(w)=-G d w,
\quad\nabla|_C=0.
\tag{8}
\]
It is well defined because on the polynomial presentation
\[
\nabla(vw-r)=dw-vGdw-Apdw=0.
\]
It obeys nabla(a b)=a' b+a nabla(b) for a in C[lambda],
so is an algebraic connection along the parameter. A one-dimensional
base leaves no independent curvature component to test.

For every d != 0, this particular derivation is **not locally nilpotent**.
To prove this without analytic exponentials, work in the embedded
polynomial subring C[lambda,w], and then over Frac(C). Put
g(lambda)=dG and P_0=1. Recursively,
\[
\nabla^j(w)=P_j(\lambda)w,\qquad
P_{j+1}=P_j'-gP_j.
\tag{9}
\]
If k=1, g=d is a nonzero constant and P_j=(-d)^j. If k>1,
g has degree k-1 with leading coefficient (-1)^(k-1)d^k.
Induction in (9) gives degree j(k-1) and nonzero leading coefficient
((-1)^k d^k)^j for P_j. In either case every iterate is nonzero.
The embedding used here follows already from B_p=C_p[lambda,w].

This failure occurs even in completely polynomial examples. For
\[
R=\mathbb C[x,y,z],\quad D=x^2\partial_y+2y\partial_z,
\quad p=x^2,\quad r=y,\quad d=x,
\]
the total family is explicitly k[lambda,x,w,z], since y=(1+lambda x)w.
Nevertheless (8), with k=2, has
\[
\nabla(w)=-x(1-\lambda x)w
\]
and is not locally nilpotent. The easy polynomial presentation has a
different horizontal LND, differentiation in lambda holding x,w,z
fixed. That LND changes the old invariant
h=x^2z-(1+lambda x)^2w^2. Requiring transport to keep the old invariant
plane pointwise fixed can therefore discard the useful connection.

The falsified inference is precise: a polynomial lift of partial_lambda
and compatible finite-jet trivializations do not make the chosen lift
integrate to a polynomial additive action. This is not a counterexample
to existence of some other successful lift.

## 5. Smoothness and all formal jets do not imply local triviality

A separate elementary control refutes the weaker automatic-algebraization
claim, without pretending to satisfy the stable-triviality hypothesis (4).
Let
\[
\mathcal T=
\mathbb C[\lambda,\xi,\eta,u_1,u_2]/(\xi(1+\lambda\eta)-1).
\tag{10}
\]
This is smooth of relative dimension three over k[lambda]: 1+lambda eta
is a unit on T, being xi^-1, so the xi derivative of the equation is
a unit. Its central fiber is k[eta,u_1,u_2]. For every m its reduction
modulo lambda^m is the corresponding polynomial ring, by eliminating
xi with the finite geometric series.

For every c != 0, however, its fiber is
\[
\mathcal T/(\lambda-c)
\cong\mathbb C[\xi,\xi^{-1},u_1,u_2],
\]
using eta=(xi^-1-1)/c. This cannot be a polynomial three-ring: xi
is a nonconstant unit. Any Zariski neighborhood of zero in the
parameter line contains nonzero closed points. Therefore no such
neighborhood trivializes T as affine three-space, despite all the
compatible finite-order trivializations. The same generic-fiber
argument rules out polynomiality after base change to k[[lambda]].

This example is not an instance of (3) satisfying (4); its nonzero
fibers are not even stably polynomial, because stabilization retains
their nonconstant units. Its role is only to exclude the formal-to-
Zariski inference. Adding stable triviality is a substantive extra
condition, not a detail handled by this counterexample.

## 6. An exact recognition criterion and a usable published sufficient condition

For this family the following equivalence is elementary:
\[
\mathcal B\cong_{\mathbb C[\lambda]}\mathbb C[\lambda]^{[3]}
\quad\Longleftrightarrow\quad
\exists\partial\in\operatorname{LND}_{\mathbb C}(\mathcal B)
\text{ with }\partial\lambda=1.
\tag{11}
\]
The forward implication transports the coordinate partial. For the
reverse implication the slice theorem gives B=(ker partial)[lambda],
and evaluating lambda=0 identifies its kernel with B/(lambda)=R.
No requirement that partial fix C belongs in (11).

Thus the horizontal LND is an exact remaining target; the derivation
in (8) does not supply it. Rephrasing the target does not prove it,
but (8)-(9) identify the failed step in the proposed homotopy proof.

A different sufficient condition is genuinely covered by a published
statement. Suppose one constructs U_1,U_2 in B, algebraically
independent over k[lambda], such that for **every prime** P of
k[lambda], including the generic prime, their residues remain
algebraically independent and
\[
\mathcal B\otimes\kappa(P)
=\kappa(P)[\overline U_1,\overline U_2]^{[1]}.
\tag{12}
\]
Then B is an affine-three-space fibration with a residual pair.
Das-Dutta Corollary 3.8 applies over the Noetherian factorial domain
k[lambda] and gives B=k[lambda,U_1,U_2]^[1].[^2] This condition
allows the invariant-plane embedding to change, as requested.

What is not available is (12). Smoothness and (4) give smooth stably
polynomial fiber rings, not the required polynomial fiber rings or a
common residual pair. In the same source, Theorem 3.13 starts with an
affine-space fibration and residual variables and concludes stable
polynomiality; it is not a theorem cancelling the stabilizing variable.
Their definitions explicitly require the polynomial condition on every
fiber. These are statement-level limitations, not an absence-based
claim that no other theorem can apply.

Likewise the generic-equivalence statement reproduced in
Gurjar-Masuda-Miyanishi requires matching fibers of two families, not
one polynomial fiber and its formal neighborhood.[^3] The family in
(3) has not been shown to meet that hypothesis with the trivial
affine-three-space family.

## 7. Verification and outcome

An independent inline SymPy execution passed 95 exact scalar assertions:
the Bezout and relation-preservation identities for k=1,...,6; the
first five recurrence degrees and leading coefficients for each k;
finite inverses at eight precisions; the triangular example's preserved
relation and invariant; and the formal countercontrol at six precisions.
These are finite assertions, not 95 test methods or an independent
formal verification of the universal proof.

The interpolation is therefore a valid smooth, stably trivial
presentation homotopy, with genuinely trivial central formal completion.
It is not yet a polynomial k[lambda]-presentation. The actual missing
step is a different locally nilpotent horizontal derivation as in (11),
a verified residual pair as in (12), or another theorem controlling
changes of presentation beyond the fixed-support transport already
refuted. Neither arbitrary primitive inputs nor arbitrary cancellation
kernels have been recognized by this pass.

## Sources

[^1]: The Stacks Project, [Definition 10.137.5](https://stacks.math.columbia.edu/tag/00T6) and [Lemma 10.137.6](https://stacks.math.columbia.edu/tag/00T7), standard smooth presentations, their smoothness, and relative dimension. The statements and proof were read directly.

[^2]: P. Das and A. K. Dutta, [*A Note on Residual Variables of an Affine Fibration*](https://arxiv.org/pdf/2002.02128), definitions in Sections 1-2, Corollary 3.8, Theorem 3.13, and Corollary 3.19. The cited implications and their hypotheses were read directly; no present-day general open-status claim is inferred from the preprint's historical remarks.

[^3]: R. V. Gurjar, K. Masuda, and M. Miyanishi, [*Affine Space Fibrations*, public author text](https://oa.tib.eu/renate/bitstreams/2db0f47c-00f9-4195-9c8a-a46722165a99/download), Introduction, printed pages 2-4, especially the stated Generic Equivalence Theorem and definitions distinguishing generic triviality and Zariski local triviality.
