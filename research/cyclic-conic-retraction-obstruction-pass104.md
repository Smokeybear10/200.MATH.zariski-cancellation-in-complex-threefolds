# The cyclic conic has no section over its specified invariant base

The exact local conic103 does not merely lack a proved section. Smoothness
forces every such section to be impossible. Consequently the retained
retraction-based algebraic patching theorem is unavailable at this actual
double fiber. This is a restriction on the specified invariant inclusion,
not an obstruction to the unknown threefold being polynomial.

The same equation rules out the specified discriminant invariant eta as an
ambient coordinate. Higher-order first plinths remain compatible with an
absolute polynomial cylinder, as the already retained polynomial example
shows. No new arbitrary-action reduction is supplied.

## 1. Exact local hypotheses

Use the proved presentation in
[cyclic-module103](noncollapsed-cyclic-degree-module-pass103.md). Set
R=S_m for the actual closed point m of S=C[s1,s2], and let n=mR.
The actual elements U,V,p,eta satisfy
\[
\begin{gathered}
B=A[u]\simeq\mathbb C^{[4]},\qquad
\mathcal A=A\otimes_S R
 =R[U,V]\simeq
 R[\mathsf U,\mathsf V]/(\mathsf V^2-2p\mathsf U+\eta),\\
p=N^2U\in\mathfrak m\setminus\{0\},\qquad
\eta=2pU-V^2\in\mathfrak m,\qquad
NU=V,\quad NV=p,\\
\mathcal A/\mathfrak n\mathcal A
 =\mathbb C[\bar U,\bar V]/(\bar V^2),\\
dp=0, d\eta\ne0
\quad\text{or}\quad
dp,d\eta\text{ are independent in }\mathfrak n/\mathfrak n^2.
\end{gathered}
\tag{1}
\]
The last alternative uses absolute smoothness of A at every point of the
whole double line. It is equivalent to
\(d\eta-2t\,dp\ne0\) for every complex t. The two differentials here
belong to the cotangent space of the base, not that of A.

The map S into A is faithfully flat and is the full kernel of N. Every
height-one prime of S stays prime in A by the retained factorial-closure
and factoriality argument. These extra facts will identify the precise
published patching gate in Section 4. The elementary section obstruction
itself uses only the local presentation and the last line of (1).

## 2. No local section, including after an unramified local base change

An R-retraction from the actual algebra to R would send U to a and V to b,
where a,b belong to R. Its defining equation and reduction at n give
\[
b^2-2pa+\eta=0,\qquad b\in\mathfrak n,
\qquad d\eta=2\bar a\,dp
\quad\text{in }\mathfrak n/\mathfrak n^2.
\tag{2}
\]
The last equality contradicts (1). Therefore no such R-retraction exists.
The specified quotient also has no section over any Zariski
neighborhood of m. A section there would localize to the forbidden one.

The same proof works for a local extension R to R' with residue field C
whose induced map on cotangent spaces is injective. The images of
\(d\eta-2t\,dp\) remain nonzero, while a section after this base change
would make one of them zero. In particular, passing to the completion or
to a local etale neighborhood over m does not produce a section. This
does not include a ramified extension that kills a base cotangent class.

There is also no relative polynomial stabilization of this local
inclusion. For any nonnegative k, an R-algebra isomorphism
\(\mathcal A[t_1,\ldots,t_k]\simeq R^{[k+1]}\) would reduce to an
isomorphism
\[
\mathbb C[\bar U,\bar V,t_1,\ldots,t_k]/(\bar V^2)
\simeq\mathbb C^{[k+1]}.
\tag{3}
\]
The left side has the nonzero nilpotent class of V and the right side is
reduced. Thus (3) is impossible. The given absolute isomorphism
\(A[u]\simeq\mathbb C^{[4]}\) does not contradict this relative
obstruction and must not be replaced by an S-algebra isomorphism.

## 3. The specified discriminant is not an ambient coordinate

Because the equality defining eta is an equality of actual global
elements of A, differentiation in A gives
\[
d_A\eta=2U\,d_Ap+2p\,d_AU-2V\,d_AV.
\tag{4}
\]
The whole-fiber presentation supplies an actual complex point P_t over m
with U=t and V=0 for every complex t. Since p vanishes there, (4) gives
\(d_A\eta|_{P_0}=0\). Thus eta has a critical point on the smooth
threefold A. It also has a critical point at every point of the cylinder
over P_0, since eta does not depend on u.

Consequently eta cannot be a member of a polynomial coordinate system
of B. Indeed such a coordinate has a polynomial partial derivation
sending it to 1, which is impossible at a critical point. Nor can eta
be a member of an abstract polynomial coordinate system of A if A is
eventually recognized as polynomial.

More generally, for constants a,b with b nonzero, the invariant
\(ap+b\eta\) has zero differential at P_t with
\(t=-a/(2b)\). In the higher-order first-plinth branch
\(p\in\mathfrak n^2\), the differential of p in A is zero at
every point over m. Formula (4) then makes the differential of eta zero
along the entire reduced line. Every affine combination of p and eta
is critical there. A different invariant base coordinate is not excluded.

This is an actual-coordinate obstruction, but not a recognition theorem:
the local conic does not turn its distinguished discriminant into a
usable ambient invariant coordinate.

## 4. The precise primary patching theorem and the actual divisor fibers

Das and Dutta's Theorem 3.9 assumes a flat algebra over a Krull domain,
a retraction with finitely generated kernel, a generic polynomial line,
and integral height-one fibers. It concludes a symmetric algebra of an
invertible ideal. Corollary 3.10 gives a polynomial algebra over a UFD.
Their proof passes through a DVR criterion and the local-global
Proposition 3.8. The retraction is retained throughout.[^dd]

This is the same source gate already recorded in
[relative-hypersurface79](relative-hypersurface-source-gates-pass79.md),
not a newly discovered general theorem. The new application fact is that
Section 2 proves its retraction premise false at the conic fiber, rather
than leaving construction of that retraction as a possible next step.
If a retraction existed, its kernel would be generated by U-a and V-b,
so finite generation would not be an additional issue.

For completeness, the height-one conditions can be checked directly in
the actual conic. Let pi be an irreducible factor of p in R and put
\(k_\pi=\operatorname{Frac}(R/\pi R)\). Its actual fiber is
\[
\mathcal A\otimes_R k_\pi
 =k_\pi[\mathsf U,\mathsf V]/
   (\mathsf V^2+\bar\eta)
 =k_\pi(\sqrt{-\bar\eta})[\mathsf U],
\qquad
[k_\pi(\sqrt{-\bar\eta}):k_\pi]=2.
\tag{5}
\]
To justify the last equality, pi is associated in R to a prime of the
global base S. That prime stays prime in A and then in the localized
algebra. The displayed fiber is therefore a domain. A monic
quadratic of this form can give a domain only if eta is nonzero modulo
pi and its negative is not a square in k_pi. This also proves
\(\gcd_R(p,\eta)=1\). Away from the factors of p the equation solves
for U and gives a polynomial line.

Thus the integral height-one fibers required by the retraction theorem
are present. They are not geometrically integral along the factors of p:
over an algebraic closure the two distinct roots split the fiber into
two lines. The geometrically integral alternative in the same paper's
Theorem 1.1 is therefore also unavailable. This is an exact failure along
each local plinth component, not an assertion that domain fibers are
geometrically integral.

## 5. Absolute cancellation hypotheses do not remove this obstruction

The polynomial control in103 already supplies every integer e at least
one:
\[
A_0=\mathbb C[x,V,U],\qquad
f=V^2-2x^eU,\qquad S_0=\mathbb C[x,f],\qquad
N_e=x^e\partial_V+V\partial_U,
\qquad p=x^e,\quad\eta=-f.
\tag{6}
\]
Its full kernel, primitivity, faithful flatness and double fiber are
proved in103. In particular \(A_0[u]\) is genuinely a polynomial
four-ring, and A0 is smooth, factorial and contractible. For e at least
two the first plinth still has arbitrary order e. The no-section and
critical-point conclusions above hold for this specified inclusion.
The different element x is already an ambient invariant coordinate.

This reused example is not presented as a realization of the canonical
highest field of the full original three-good E-frame. It proves the
more limited but decisive statement that the absolute cylinder, the
exact cyclic conic and smoothness cannot eliminate the higher-order
plinth or produce a section over the specified kernel plane. A global
recognition argument must use a different invariant coordinate or
additional actual-frame information, rather than this section-patching
route at the double fiber.

## Read scope

The complete saved cyclic-module103 proof and the retained79 and47
source/application notes were reread. The primary paper below was freshly
read in extracted text for its definition of retraction and A1-fibration,
Theorem 1.1, Lemma 3.5 as stated, and the complete displayed Lemma 3.6,
Proposition 3.8 and Theorem 3.9 proofs, with Corollary 3.10. The deeper
external patching proof quoted as Lemma 3.5 was not freshly reconstructed.
No whole-paper, novelty, numerical, human-expert or formal-proof claim is
made. No file through103 was edited.

[^dd]: Prosenjit Das and Amartya K. Dutta,
    [*On codimension-one A1-fibration with retraction*](https://arxiv.org/pdf/1302.5223v1),
    arXiv:1302.5223v1. Theorem 3.9 and Corollary 3.10 are on printed
    pages 9--10; the preceding local-global proof is Proposition 3.8.
    Theorem 1.1 is the paper's explicit restatement of the earlier
    geometrically integral-fiber theorem. This source is used for its
    exact conditional statement, not to claim it applies to (1).
