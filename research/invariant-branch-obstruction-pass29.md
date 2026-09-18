# An invariant-branch obstruction to a three-generator surface presentation

Date: 2026-09-13.

The argument for the fixed conductor surface has the following abstract
form. It requires neither normality of the surface nor a prior
finite-generation hypothesis on its invariant ring. The existence of the
specified common character and of a quadratic local obstruction remains
an explicit hypothesis. No novelty or general cancellation claim is made.

## 1. Precise statement

Let R be a finitely generated complex domain of dimension two, let
partial be a nonzero locally nilpotent derivation of R, and put
T=ker(partial). Assume there is a fixed embedding

\[
T\subseteq\mathbb C[u],\qquad
\operatorname{Frac}T=\mathbb C(u).
\tag{1}
\]

Suppose there are b distinct complex numbers r_1,...,r_b, with b>=3,
such that evaluation at these numbers gives the same character

\[
\chi:T\longrightarrow\mathbb C.
\tag{2}
\]

Thus f(r_i)=chi(f) for every f in T and every i. Suppose moreover
that a closed point q of Spec(R) restricts to chi on T, and that its
local maximal ideal m satisfies

\[
\dim_{\mathbb C}\mathfrak m/\mathfrak m^2=3,
\qquad
\dim_{\mathbb C}\mathfrak m^2/\mathfrak m^3<6.
\tag{3}
\]

Then

\[
R\ne\mathbb C[j,a_1,a_2]
\quad\text{for every }j\in T\text{ and }a_1,a_2\in R.
\tag{4}
\]

The embedding in (1), the equality of fraction fields, and the common
character on all of T are essential stated assumptions. They are not
inferred from the existence of an arbitrary surface LND.

## 2. Automatic finiteness and the precise generic fiber

Fix a nonconstant j in T and put S=C[j], K=C(j), L=C(u), and
N=deg_u(j). The element u is integral over S: divide j(U)-j by
its nonzero constant leading coefficient to get a monic equation.
Consequently C[u] is finite as an S-module. Since S is Noetherian
and T is an S-submodule of C[u], T is finite as an S-module too.
In particular its finite generation is a consequence, not an extra
hypothesis.

The localization T_K is a finite-dimensional domain over K, so it
is a field. Its fraction field remains Frac(T)=L; hence

\[
T\otimes_S K=L.
\tag{5}
\]

Choose a local slice r of partial, with partial(r)=a in T nonzero.
Such a slice follows by taking the next-to-last nonzero derivative
of any element not in T. On R_a, the element v=r/a has derivative
one. Subtracting the leading term
(partial^n f)v^n/n! and inducting on partial-degree proves the usual
slice equality R_a=T_a[v]. No normality is used.
By (5), a is a nonzero scalar in the field T_K and is already
invertible in R_K. Thus

\[
R\otimes_S K=L[v].
\tag{6}
\]

The extension L/K is separable of degree N. One way to verify its
degree is to use the irreducibility of j(U)-J over C(J), obtained
from the prime polynomial j(U)-J in C[U,J] and Gauss's lemma.
Over an algebraic closure Kbar of K, (6) therefore becomes a
product of N reduced polynomial line rings.

## 3. The hypothetical presentation forces a global plane base

Suppose R=C[j,a_1,a_2]. With independent variables J,X,Y, the
surjection W=C[J,X,Y] -> R has a principal height-one prime kernel
(F), where F is irreducible and is not a polynomial in J alone.
Consider the actual S-linear Hamiltonian derivation

\[
H=F_Y\partial_X-F_X\partial_Y.
\tag{7}
\]

By (6), over Kbar the zero scheme of F in the plane is N disjoint
reduced affine lines. The split-line lemma proved in the
[fixed-surface argument](global-invariant-embedding-pass29.md) gives

\[
F=c\prod_{i=1}^N(Q-\alpha_i)
\quad\text{in }\overline K[X,Y],
\tag{8}
\]

where Q is a polynomial coordinate and the alpha_i are distinct.
For clarity, that lemma rectifies one embedded line by
Abhyankar--Moh; the coordinate vanishing on it restricts to a
nonzero constant on every disjoint line, because the only units
of a polynomial line ring are constants. The other components
are therefore distinct fibers of that same coordinate.[^am]

The Hamiltonian in (7) is a nonzero replica of a coordinate partial
after this injective field extension. It is therefore an LND on W
itself: each polynomial iterate that vanishes after extension already
vanishes in W. Divide out its coefficient gcd gamma to obtain a
primitive polynomial S-derivation Delta. The familiar LND-degree
argument gives H(gamma)=0, because H(gamma) is divisible by gamma;
then H^n=gamma^n Delta^n, proving that Delta is an LND as well.

Its coprime coefficients in the UFD W either are comaximal or form
a regular sequence. Bhatwadekar--Dutta Theorem 4.7, with the
Noetherian base S=C[J], gives the global equality

\[
\ker\Delta=\mathbb C[J,P],\qquad
F=\Phi(J,P),\quad \Phi\in\mathbb C[J,Z]\text{ irreducible}.
\tag{9}
\]

Only the kernel conclusion is used. In particular no slice or
fixed-point-free conclusion is inferred from the regular-sequence
case.[^bd] Since F is invariant and W is a domain,

\[
(F)W\cap\ker\Delta=F\ker\Delta.
\tag{10}
\]

Thus the plane curve ring C_0=C[J,Z]/(Phi) injects into R.

The derivation induced by H on the geometric generic fiber acts
nontrivially on each component of (8), because the roots are simple.
Consequently the derivation induced by Delta on R is nonzero.
It kills K and hence its separable algebraic extension L. By (6),
Frac(R)=L(v), so this induced derivation is a nonzero rational
multiple of partial_v and its rational kernel is L. Moreover
R intersect L=T: this follows either from the original local-slice
description or from the original partial having rational kernel L.
Therefore the induced invariant ring is exactly the original T.
In particular p(u), the image of P, belongs to T.

It is important to establish the full field of C_0 rather than just
its inclusion in L. Flat base change in the kernel of the S-linear
map Delta:W -> W gives

\[
\overline K[P]=\ker\Delta_{\overline K}
 =\ker H_{\overline K}=\overline K[Q].
\tag{11}
\]

Hence P is affine-linear in Q over Kbar. Equations (8)--(9) imply
deg_Z(Phi)=N. Irreducibility over K and (10) now yield

\[
[K(p):K]=N=[L:K],\qquad
\operatorname{Frac}C_0=K(p)=L.
\tag{12}
\]

Since C[u] is finite over S, it is finite over the intermediate
ring C_0=C[j,p]. With (12), its normality proves that C[u] is
exactly the finite normalization of C_0.

## 4. The branch count contradicts the quadratic local ring

Set c_0=chi(j) and p_0=chi(p). All b distinct normalization points
u=r_i lie over the single plane-curve point (J,Z)=(c_0,p_0).
The normalization/branch correspondence therefore gives at least
b branches at that point.[^branches]

This is also a formal-branch count, not merely the degree of an
arbitrary finite cover. Completing the finite birational injection
of the local curve ring into its semilocal normalization gives an
injection into the product of the corresponding C[[u-r_i]] factors,
with any other preimages included. A nonzero birational conductor
element has nonzero image on every factor; inverting it makes the
two completed rings equal. Thus their minimal primes correspond.
Each formal plane branch contributes a nonunit factor, so

\[
\Phi\in(J-c_0,Z-p_0)^b.
\tag{13}
\]

At the ambient point qtilde corresponding to q in the hypothetical
presentation, both J-c_0 and P-p_0 vanish, by (2)--(3). The GLOBAL
identity (9) therefore gives

\[
F\in\mathfrak m_{\widetilde q}^{\,b}
 \subseteq\mathfrak m_{\widetilde q}^{\,3}.
\tag{14}
\]

A hypersurface quotient of a smooth three-dimensional local ring
with defining equation in the cube of its maximal ideal has no
quadratic associated-graded relation. Its quadratic Hilbert
dimension is consequently six. This contradicts (3). No
denominator or local unit is discarded in (14).

This proves (4) for nonconstant j. If j is constant, two other
generators would give cotangent dimension at most two at every
closed point, contradicting the first part of (3).

## 5. Relation to the fixed surface and exact threshold

For the surface in
[global-invariant-embedding-pass29.md](global-invariant-embedding-pass29.md),
T=C+dC[u], d=u^4-1. The four values 1,i,-1,-i give the same
character on T. Every conductor point has completed local ring
C[[xi,eta,t]]/(xi eta), with cotangent dimension three and
quadratic Hilbert dimension five. Thus all the hypotheses above
hold with b=4, recovering the exact surface obstruction.

The branch threshold cannot be replaced by b=2 under the remaining
abstract hypotheses. Take

\[
D=u^2-1,\quad E=uD,\quad
T_2=\mathbb C[D,E],\qquad
R_2=T_2[v],\quad \partial=\partial_v.
\tag{15}
\]

Then Frac(T_2)=C(u), the values u=1,-1 induce the same character,
and

\[
R_2\cong\mathbb C[D,E,v]/(E^2-D^2(D+1)).
\tag{16}
\]

The displayed relation is irreducible because D+1 is not a square
in C(D); the polynomial parametrization gives it as the exact kernel.
At the origin the linear relation is absent and the unique initial
quadratic relation is E^2-D^2. Its local dimensions in (3) are
three and five, yet (16) is a three-generator presentation containing
invariants. This is an elementary boundary control, not a new
counted test suite. The parametrized relation and its initial quadratic
form were also checked by exact inline symbolic arithmetic.

The theorem excludes invariant-containing triples only. It does not
exclude three wholly noninvariant generators, construct an ambient
LND, or settle the additional realization conditions of the cancellation
program. No registry, preceding proof or metadata was changed.

## Source and verification boundary

[^am]: E. R. Garcia Barroso and A. Ploski, [*An approach to plane algebroid branches*](https://arxiv.org/pdf/1208.0913), standing algebraically closed field convention and Theorem 6.9 with its proof, read directly in the independent pass-29 audit. The characteristic-zero degree-divisibility statement gives rectification by finite decreasing-degree polynomial shears. The result is credited there to Abhyankar--Moh; the original publisher article was not independently obtained in this pass.
[^bd]: S. M. Bhatwadekar and A. K. Dutta, [*Kernel of Locally Nilpotent R-Derivations of R[X,Y]*](https://repository.ias.ac.in/3203/1/311.pdf), Transactions of the AMS 349(8) (1997), Theorem 4.7. The complete selected statement/proof and base conventions were directly read in this investigator's pass-27 audit; current pass-29 refetches of those pages timed out. The polynomial UFD coefficient argument verifying its two alternatives was independently reconstructed here. This is an inherited kernel theorem, not a new kernel-finiteness result.
[^branches]: The Stacks Project, [Lemma 33.40.1, Tag 0C1S](https://stacks.math.columbia.edu/tag/0C1S), statement and proof directly read in pass 29. The formal completion step is additionally reconstructed above for this finite birational curve normalization.
