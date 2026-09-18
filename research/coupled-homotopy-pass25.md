# Coupled homotopy: the full invariant-plane normalizer gate

The broadened transport scheme considered here permits arbitrary
lambda-dependent polynomial movement inside the old invariant-plane
subalgebra. It does not require pointwise preservation of that plane.
Nevertheless the scheme still fails, even for the explicit polynomial
test family of pass 24. Its failure is not restricted to triangular
ambient projections or to a bounded degree of a candidate derivation.

There are three general statements below: a normalizer must centralize
the canonical vertical LND and fix its full plinth; a factor-complete
plinth reduces setwise plane preservation to pointwise preservation;
and a residual pair cannot lie entirely in the old invariant plane.
An exact polynomial-ring control excludes every plane-normalizing
horizontal LND, even when a successful horizontal LND exists.

These are obstructions to specified reductions, not a solution to the
universal coupled-horizontal problem or a mathematical priority claim.

## 1. Setup and the canonical vertical action

Work over k=C. Let R=k^[3], let D be a nonzero primitive LND, and let
C=ker D with full plinth pC and minimal local slice Dr=p. Assume p is
nonzero and nonunit, and d belongs to sqrt(pC). Put

\[
v=1+\lambda d,\qquad
B=R[\lambda,w]/(vw-r),\qquad A=C[\lambda].
\tag{1}
\]

The [exact homotopy](presentation-homotopy-pass23.md) gives (p,v)=1,
B[s] isomorphic to R[lambda,t], and the two actual charts

\[
B_v=R[\lambda]_v,\qquad B_p=C_p[\lambda,w].
\tag{2}
\]

In particular B is a UFD with B*=k*. These properties descend from
its polynomial extension; they do not assume B itself is polynomial.

Define the vertical LND

\[
\Delta|_R=vD,\qquad \Delta\lambda=0,\qquad \Delta w=p.
\tag{3}
\]

It preserves vw-r and is locally nilpotent on the given generators.
The two charts prove, exactly,

\[
\ker\Delta=A,\qquad
\ker\Delta^2=A+Aw,\qquad
\Delta(\ker\Delta^2)=pA.
\tag{4}
\]

Indeed on the v-chart the first degree module is A_v+A_v*r,
equally the span of 1,w. On the p-chart it is A_p+A_p*w.
Coefficient uniqueness on the generic line and A_v intersect A_p=A
prove (4). Here the v-localization is of A=C[lambda], since v
itself depends on lambda.
The same two-chart argument proves primitivity: on the first chart
Delta is a unit times the primitive D, and on the second its value
on w is a unit. A common prime coefficient cannot survive this cover.
These are full-ideal and full-module statements, not radical ones.

## 2. A setwise plane normalizer must centralize the vertical action

**Normalizer lemma.** Suppose delta is an LND of B such that

\[
\delta\lambda=1,\qquad \delta(A)\subseteq A.
\tag{5}
\]

Then

\[
[\delta,\Delta]=0,\qquad \delta p=0,\qquad \delta w\in A.
\tag{6}
\]

The premise permits delta(c) to depend on lambda. It is strictly
broader than delta|C=0, or even delta(C) contained in C.

**Proof.** Adjoin an independent parameter tau. The polynomial
automorphism Phi=exp(tau*delta) of B[tau] preserves A[tau] setwise:
both Phi and its inverse preserve it by (5). Thus
Delta'=Phi*Delta*Phi^(-1) is a primitive LND with the same kernel
A[tau] as Delta.

Over Frac(A[tau]), both are nonzero locally nilpotent derivations
of a polynomial line, and hence differ by a nonzero scalar gamma
in that field. Primitivity holds after adjoining tau and after
conjugating. At each prime of the UFD B[tau], the minimum valuation
of the values of either derivation on a finite algebra generating
set is zero. The relation Delta'=gamma*Delta therefore gives
valuation zero for gamma at every prime. Consequently gamma is
a unit of B[tau], and hence lies in k*. At tau=0 it equals one.
It follows that Phi commutes with Delta, so [delta,Delta]=0.

Commutation preserves ker Delta^2. Applying delta to Delta w=p
and using (4) shows delta p lies in pA. For an LND on a
characteristic-zero domain, a nonzero element dividing its own
derivative is invariant: otherwise LND-degree additivity would
give deg(delta p)=deg p-1 at least deg p. Thus delta p=0.
Finally Delta(delta w)=delta p=0, so delta w belongs to A.
This proves (6).

Equivalently, the full polynomial flow preserves the principal
plinth pA[tau], with no nonconstant unit available to change its
generator. The argument tracks the full multiplicity of p.

The same-kernel primitive ratio and additive-flow mechanism are
established tools, not claimed here as a new abstract theorem.
Stampfli's subsection 4.1 records the UFD LND facts; Proposition
5.1.1 and Lemma 5.1.2 provide the inherited centralizer and
kernel-fixing automorphism framework.[^stampfli] Those statements
are not being mislabeled as the lambda-normalizer assertion (6).
The proof above checks the application to the actual UFD B[tau]
without first recognizing B as a polynomial ring.

There is an exact full-algebra interpretation of the premise.
A horizontal LND satisfying (5) exists if and only if there is
a k[lambda]-isomorphism B to R[lambda] carrying A onto C[lambda]
setwise. One direction transports partial_lambda. In the other,
the slice theorem gives B=(ker delta)[lambda] and, separately,
A=(ker delta intersect A)[lambda]. Evaluation at lambda=0
identifies these kernels with R and its included C respectively.
Thus the test excludes precisely this broadened transport of
embedded subalgebras, not only a choice of formula for delta.

## 3. Factor-complete plinths exclude the enlarged scheme generally

Write p=c product_i f_i^(n_i) in C. Suppose that the subfield of
Frac(C) generated over k by the distinct irreducible factors f_i
has transcendence degree two.

Then a horizontal LND satisfying (5) exists if and only if d is
in pC. In particular this conclusion allows arbitrary polynomial
automorphisms inside C[lambda], not just fixed invariant coordinates.

To prove necessity, (6) and LND-degree additivity force delta to
kill every factor f_i. The fraction field Frac(C) is algebraic
over their generated field. In characteristic zero a derivation
killing a field kills its algebraic extension, by differentiating
a separable minimal polynomial. Hence delta kills all C.

The [full-plinth relative theorem](relative-modification-classification-pass19.md),
Section 5, now applies exactly as in the
[horizontal-action proof](horizontal-lnd-pass24.md), Section 2.
The horizontal slice identifies the zero and one fibers over C;
they are R and R[r/(1+d)]. Since 1+d has common residue one on
every plinth component, their relative isomorphism forces p|d.
No connected-support condition is needed here.

Conversely, when d=pH, the explicit horizontal LND
delta lambda=1, delta w=0, delta|R=HwD fixes C and works.
This is the existing positive construction, not a new family result.

For example, a full plinth f^n h in C=k[f,h] satisfies the
factor-field hypothesis. The conclusion excludes plane-normalizing
transport in its radical-only cases, without revisiting their
already classified finite-jet coordinate formulas. If all factors
of p instead lie in a field of transcendence degree one, the
factor argument alone does not force delta|C=0. The next control
treats such a case by a separate exact argument.

The independently written
[non-fence extension](nonfence-plane-rigidity-pass25.md) replaces
the factor-field hypothesis by the more general condition that
div(p) is not a fence. It uses Stampfli's plane-divisor stabilizer
classification and the absence of nonconstant A^1-maps into a
torus, with the parameter-shifted inverse checked explicitly.
The elementary factor argument above is retained as a separate
source-independent sufficient condition.

## 4. No residual pair can stay inside the old invariant subalgebra

For every primitive input in Section 1 with nonunit p, there cannot
be U_1,U_2 in A for which the required residual-pair condition holds
even at lambda=0. Namely, it is impossible to have algebraically
independent residues u_1,u_2 and

\[
R=k[u_1,u_2]^{[1]}.
\tag{7}
\]

Indeed D fixes u_1,u_2. Write the right side as k[u_1,u_2,z].
On the generic polynomial z-line, local nilpotence forces Dz
to be independent of z. Since Dz is polynomial, Dz is in
k[u_1,u_2], and ker D=k[u_1,u_2]. Primitivity then makes Dz a
unit: otherwise it divides all values of D on this polynomial
coordinate ring. The full plinth is therefore the unit ideal,
contradicting the assumption on p.

Thus merely applying lambda-dependent automorphisms of C[lambda]
cannot supply a residual pair for the homotopy. At least one
successful residual variable must leave the old invariant
subalgebra. This does not exclude residual pairs in B itself.
The preceding pass's cited residual-variable theorem still requires
its polynomial-fiber hypotheses; none are inferred here from stable
triviality or smoothness.

## 5. An explicit polynomial family has no plane-normalizing horizontal LND

Retain the already used input

\[
R=k[x,y,z],\quad D=x^2\partial_y+2y\partial_z,
\quad r=y,\quad p=x^2,\quad d=x.
\tag{8}
\]

It is primitive with C=k[x,h], h=x^2z-y^2, and full plinth x^2C.
The exact family is the polynomial ring

\[
B=k[\lambda,x,w,z],\qquad y=vw,\quad v=1+\lambda x,
\]
\[
h=x^2z-v^2w^2,\quad A=k[\lambda,x,h],\quad
\Delta w=x^2,\quad\Delta z=2v^2w,
\quad\Delta x=\Delta\lambda=0.
\tag{9}
\]

**Proposition.** There is no LND delta of B with delta lambda=1
and delta(A) contained in A.

By Section 2, any such delta would fix x^2 and hence x, and
b=delta w would belong to A. Write g=delta h in A.
After inverting x, restrict to the stable polynomial subalgebra
k(x)[lambda,h]. The restriction is the LND

\[
\partial_\lambda+g(\lambda,x,h)\partial_h.
\tag{10}
\]

For completeness, any LND of this form must have g independent
of h. If g has h-degree m>=2, the h-degrees of successive iterates
of h are 1+j(m-1); the g*partial_h term gives a nonzero new leading
term, and partial_lambda has smaller h-degree. If m=1, write
g=gamma(lambda)h+beta(lambda) over k(x). The coefficients of h in
the iterates satisfy P_0=1 and P_(j+1)=P_j'+gamma P_j. For nonzero
gamma, their degrees are j*deg gamma with nonzero leading
coefficient, including the constant-gamma case. No iterate vanishes.
Therefore local nilpotence forces g to belong to k[x,lambda].

Now differentiate the physical polynomial h from (9):

\[
x^2\delta z=g+2vxw^2+2v^2wb.
\tag{11}
\]

Reduce modulo x. The residue of any polynomial in A is obtained
by substituting h=-w^2. Hence (11) says
g(lambda,0)+2w*b(lambda,0,-w^2)=0. Even and odd powers of w
separate, forcing g divisible by x and b divisible by x in A.
Write g=xg_1(lambda,x) and b=xb_1(lambda,x,h). Divide (11)
by x and reduce modulo x again. One obtains

\[
0=g_1(\lambda,0)+2w^2+2w b_1(\lambda,0,-w^2).
\tag{12}
\]

The last term is odd in w, while the first two are even.
Their even part cannot vanish: g_1(lambda,0) is independent
of w. This contradiction proves the proposition.

An equivalent version, before using the h-independence lemma,
forces delta h congruent to 2xh modulo x^2. Local nilpotence
then rules out precisely this surviving linear h term.
Both forms are all-degree arguments, not truncation-based searches.

## 6. Two exact controls distinguish regular transport from a complete action

There is a genuinely plane-moving polynomial horizontal derivation
normalizing A and commuting with Delta:

\[
N\lambda=1,\quad Nx=Nw=0,\qquad
Nz=2xz-2\lambda v w^2.
\tag{13}
\]

It satisfies Nh=2xh and [N,Delta]=0. It is not locally nilpotent,
since N^j h=(2x)^j h for all j. Thus allowing regular movement
of the old plane, and even centralization of the vertical action,
does not by itself supply polynomial additive transport.

In contrast, the actual horizontal coordinate partial
delta_*=partial_lambda holding x,w,z fixed is locally nilpotent
on this polynomial B. But

\[
\delta_*h=-2xvw^2,\qquad
\Delta(\delta_*h)=-4x^3vw\ne0.
\tag{14}
\]

It therefore sends h outside A=ker Delta. The successful action
does not merely apply a complicated automorphism inside the old
invariant plane. It must change that embedded subalgebra itself.
This is stronger than the pass-24 exclusion of a specified family
of triangular ambient projections.

For comparison, replacing d=x by the full-plinth multiple d=x^2
does permit plane-fixing transport: with v=1+lambda*x^2, set
delta lambda=1, delta x=delta w=0, delta z=2v*w^2. This is an
LND, fixes h=x^2z-v^2w^2, and commutes with Delta. It checks
the positive boundary of the earlier relative theorem.

## 7. Verification and the remaining universal question

The standalone checker below uses only unittest and SymPy. It
reconstructs the triangular base, the actual two horizontal controls,
their commutators and kernel behavior, the residue-parity equations,
both all-iterate degree mechanisms in bounded instances, and the
full-plinth positive boundary.

~~~sh
/opt/anaconda3/bin/python research/coupled_homotopy_checks_pass25.py
~~~

All seven unittest methods passed in 0.288 seconds. No old suite
or registry was edited by this pass.

The normalizer lemma, factor-field argument, residual-pair gate,
and universal parity/degree contradiction are the written proofs.
Finite checks are not a substitute for any of those quantifiers.

The remaining construction must be allowed to replace the embedded
subalgebra C[lambda], not only its polynomial generators. No action
or residual pair accomplishing that has been constructed for arbitrary
primitive local-slice data. Nor has an arbitrary sliced polynomial
four-ring been reduced to this homotopy. General cancellation,
novelty, formal verification and expert review remain unresolved.

## Source boundary

[^stampfli]: I. Stampfli, [*Automorphisms of C^3 Commuting with a C+-Action*](https://arxiv.org/pdf/1406.6246v2), arXiv:1406.6246v2, subsection 4.1, Proposition 5.1.1 and Lemma 5.1.2, printed pp. 6-8. These primary passages were read directly. Lemma 4.1.1 includes the UFD same-kernel, factorial-closure, slice and invariant-divisibility facts. The centralizer results supply the existing framework, not the full horizontal-normalizer statement for this homotopy. The non-fence note separately records the additional published stabilizer and algebraic-group inputs it uses.
