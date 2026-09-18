# Infinitesimal translations and an exact local conic

Two conditional results strengthen the supplied quadratic-frame investigation.
At the collapsed fibers covered by102, the projected original partial gives
compatible translations on every finite base-adic thickening. At a
noncollapsed fixed double component, one actual degree-two function and its
derivative determine the entire algebra over the local invariant base.
Neither result proves global cancellation.

The working target is still the unconfirmed complex-threefold interpretation
of the professor's email:
\[
A[u]\simeq\mathbb C^{[4]}\quad\Longrightarrow\quad A\simeq\mathbb C^{[3]}.
\]
All positive results below require additional actual-coordinate hypotheses.
There is no theorem here reducing an arbitrary sliced action to those
hypotheses. The literal emailed conclusion has a dimension mismatch when
the dimension parameter exceeds one.

## 1. Standing distinction between the original and intrinsic rings

In the conditional frame, the original polynomial ring is
\(B=\mathbb C[x_1,x_2,x_3,z]=A[u]\), with \(E=\partial_u\),
\(E^2x_i=0\), and \(E^2z=q_0\in\mathbb C^*\).
The slice is canonically normalized by \(u=Ez/q_0\), so \(Ez=q_0u\).
The canonical Jacobian locally nilpotent derivation is N. Its kernel on A
is the actual plane \(S=\mathbb C[s_1,s_2]\), and S into A is faithfully
flat. A is smooth over the complex numbers, not necessarily smooth over S.
On the generic line, N is a nonzero constant translation.

The original coordinate partial \(T=\partial_z\) is locally nilpotent on B.
Its projected constant coefficient
\(D_0=(T|_A)|_{u=0}\) is a derivation of A. Projection alone does not make
it locally nilpotent. Keeping this distinction is essential to both the
positive result and the negative control below.

## 2. The collapsed sector lifts to every finite thickening

The [complete adic proof](quadratic-adic-projected-translation-pass103.md)
starts with a whole collapsed double or mixed (2,1) fiber and a nonzero
speed normal \(L(\mathfrak m)\). Write \(J=\mathfrak mA\) and
\(I=JB\). The exact whole-fiber equations99 and the correction-rigidity
proof102 give
\[
T(I)\subset I,\qquad Tu\in I.
\]
The first inclusion makes T preserve every power of I and makes D0
preserve every power of J. The associated-graded action of T is an actual
locally nilpotent derivation on
\((\operatorname{gr}_J A)[u]\). Its value on u is zero because Tu has
positive I-order. Quotienting that graded ring by u gives exactly
\(\operatorname{gr}_J D_0\), which is therefore locally nilpotent.

For any fixed k, successively killing a class in each of the finitely many
J-adic layers proves local nilpotence of D0 on \(A/J^k\). This argument
proves the assertion for every k, rather than extrapolating from a finite
collection of computations. The required exponent can grow with k.

The exact slice is
\(r=z-q_0u^2/2\), for which \(D_0r=1\) globally. It is not, in general,
the specified relative generator c. Those functions differ by
\(q_0h^2/2\). Even on the whole nonreduced fiber the shift can have a
nilpotent part, which must be retained.

Let \(C_k\) be the kernel of the induced derivation on \(A/J^k\).
The finite slice projection gives compatible isomorphisms and surjective
invariant transition maps:
\[
A/J^k\simeq C_k[r],\qquad C_{k+1}\twoheadrightarrow C_k,
\qquad \widehat A\simeq\varprojlim_k C_k[r].
\]
These are actions over the complex numbers. They are not proved to fix
the specified base S, and \(C_k\) is not identified with
\(S/\mathfrak m^k\). The conclusion concerns the projected field D0;
it does not improve the vanishing order of the original commutator.

## 3. Why every finite order is still not a global action

The exact control \(D=\partial_r+x^2\partial_x\) on
\(\mathbb C[x,r]\) is locally nilpotent modulo \(x^k\) for every k,
and \(Dr=1\). Nevertheless
\(D^n x=n!x^{n+1}\) never vanishes in the polynomial ring or its
x-adic completion. Thus the finite-quotient conclusion alone cannot
establish a globally locally nilpotent derivation.

The formal invariant \(y=x/(1+rx)\) has inverse
\(x=y/(1-ry)=\sum_{n\ge0}r^ny^{n+1}\). The inverse has unbounded
r-degree. This is an explicit reason why
\(\varprojlim C_k[r]\) cannot simply be replaced by
\((\varprojlim C_k)[r]\).

This distinction agrees with the established theory of topologically
integrable derivations. Díaz, Dubouloz and Liendo define integrability
using continuity and convergence of the divided iterates; their
Theorem 2.7 gives the restricted exponential correspondence. Their
Theorem 4.4 uses a ring of restricted power series, not an ordinary
polynomial ring, in its slice theorem. Example 3.4 contains the
\(x^2\partial_x\) flow underlying the control above.[^formal]
The direct finite-quotient argument here does not depend on their
general topological slice theorem or its Weierstrass-division input.
No novelty claim is made for the general formal-action distinction.

## 4. A noncollapsed double gives an exact algebraic conic

The [complete cyclic-module proof](noncollapsed-cyclic-degree-module-pass103.md)
uses an actual good projection U with nonconstant residue on a fixed
double component, and sets \(V=NU\), \(p=N^2U\ne0\).
The retained generic local Jacobian calculation makes V a nonzero
square-zero element in the generic Artinian fiber. That calculation
does not require the first normal action to be nonzero.

Put \(R=S_{\mathfrak m}\). The degree modules
\(F_n=\ker N^{n+1}\) are free of rank n+1 by the elementary flat-base
argument102. The monomials \(U^j\) and \(VU^j\) of N-degree at most n
give exactly n+1 independent residues on the single generic double
component. Transcendence of the residue of U and the nonzero nilpotent
residue of V prove independence. Nakayama then makes these monomials
an actual R-basis of F_n for every n.

Taking their union and retaining the invariant
\(\eta=2pU-V^2\) gives the exact presentation
\[
A\otimes_S R
\simeq R[\mathsf U,\mathsf V]/(\mathsf V^2-2p\mathsf U+\eta).
\]
Monicity in the second variable and the generic-line isomorphism rule
out an extra kernel. This is an algebraic presentation over the local
base, not merely a completed differential model. It also recovers the
whole dual-number line as the special fiber, without assuming the
absence of other components in the proof.

Smoothness gives a precise residual choice. In the two-dimensional
cotangent space of R, either \(dp,d\eta\) are independent, or
\(dp=0\) and \(d\eta\ne0\). The second case allows higher-order
plinths. The intrinsic polynomial family
\(p=x^e\), \(\eta=-f\), \(f=V^2-2x^eU\) realizes arbitrarily high
orders e. It is not asserted to realize the full original E-frame.
The conic therefore does not by itself recognize the unknown A.

This result covers the noncollapsed sector with either first normal
action and also when \(L(\mathfrak m)=0\). It does not produce a
nonconstant degree-two function on a collapsed component where none
has yet been found. Existence of such a hidden function is a separate
possible next lemma, not a consequence asserted here.

## 5. An actual original-frame obstruction to a broader shortcut

The [three-good control](three-good-projected-partial-obstruction-pass103.md)
has a polynomial inverse in both directions, nonconstant
\(\Omega=2a\), and the exact original acceleration hypotheses.
In that example
\[
D_0a=-a^4,\qquad
D_0^n a=(-1)^n\left(\prod_{j=0}^{n-1}(1+3j)\right)a^{1+3n}\ne0.
\]
It disproves global local nilpotence of the projected D0 as a
consequence of the broad three-good frame alone, even though D0 has
a slice. The earlier one-quadratic control87 did not satisfy all
three good-coordinate hypotheses.

This example has no T-stable closed fiber of S: T sends a minus any
constant to a surviving polynomial slice variable. It cannot be used
against the stable-fiber adic theorem in Section 2. Its A is already
polynomial and its primitive N is free, so it is not a cancellation
counterexample or a model of the remaining fixed-fiber branch.

## 6. Verification and remaining obligations

The [canonical capture](verification-pass103-working.json) passes one
suite with two finite symbolic methods. The first checks truncated
flows, compatible inverses and the growing slice degree in the
abstract formal control. The second checks the actual coordinate
inverse, the canonical field, the projected derivative and the
absence of a stable fiber. Neither method verifies the universal
adic theorem or the all-degree module argument. Their proofs are
written algebraic reconstructions, not numerical conjectures.

The full saved adic proof has independent Root and Jet reconstructions.
The actual countercontrol has Root and Geometry reconstructions.
The cyclic-module proof has Root and Jet reconstructions, including
the exact retained local-Jacobian gate preceding the first-normal
assumption in95.
These are AI reviews, not human expert review or Lean certification.
The earlier full regression remains the historical 146 suites/1047
methods; no full rerun or registry expansion is represented by this
two-method capture.

~~~sh
/opt/anaconda3/bin/python -m unittest -v research.projected_derivation_thickening_checks_pass103
~~~

The next mathematical targets are existence of a hidden degree-two
parameter using additional actual-frame constraints, a justified algebraic
recognition step beyond the local conic or formal action, and the
unrestricted entry problem. The relative cubic branch also remains
outside these quadratic results. A solution of one of these bounded
questions would not automatically solve the full conjecture.

There is already a concrete boundary to a module-only hidden-parameter
argument. For any integer e at least one, put
\[
A_0=\mathbb C[x,y,c],\quad f=y^2(y-1)-x^ec,\quad
S_0=\mathbb C[x,f],\quad
N_0=x^e\partial_y+(3y^2-2y)\partial_c.
\]
Then N0 is triangular and primitive, S0 is its full kernel, and
\(A_0\) is faithfully flat over S0: its presentation is monic cubic
in y over \(S_0[c]\). Inverting x gives \((S_0)_x[y]\), where
N0 is \(x^e\partial_y\). The exact module is
\[
\ker N_0^3=S_0\oplus S_0y\oplus S_0y^2.
\]
To remove a proposed x-denominator from a generic degree-two
expression, multiply by a minimal power of x and reduce modulo x.
The elements 1,y,y² are independent over \(\mathbb C[f]\) after
\(f\mapsto y^3-y^2\). One direct proof is that the leading degrees
of \(P_i(y^3-y^2)y^i\), for i=0,1,2, have different residues modulo
three. Every coefficient must therefore be divisible by x, contradicting
minimality. The same argument in degree zero gives the full kernel S0.

The fiber at (x,f) is \(\mathbb C[y,c]/(y^2(y-1))\), of profile
(2,1). Every degree-two element has constant reduced values on both
components, so no hidden degree-two parameter exists in this control.
It is not an asserted original quadratic E-frame. Its role is to
show that flatness, primitivity and degree-module freeness alone
cannot supply the next missing parameter. The proof is exact for
every e, and no new numerical method is claimed for it.

No expert contact, submission, publication, or historical novelty
clearance is part of this work. The full goal remains active and
unachieved.

## Sources

[^formal]: Roberto Díaz, Adrien Dubouloz and Alvaro Liendo,
    [*Topologically integrable derivations and additive group actions on affine ind-schemes*](https://arxiv.org/html/2012.14302v2),
    arXiv:2012.14302v2, January 28, 2026. Relevant sections: Definition 2.4,
    Remark 2.5, Theorem 2.7 and its displayed proof; Examples 3.4 and 4.2;
    Theorem 4.4 and its proof with Lemmas 4.3, 4.5 and 4.6. These selected
    statements and proofs were freshly read. Deeper topological and
    Weierstrass dependencies were not independently reconstructed.

The actual-frame and module dependencies are the linked project proofs
in Sections 1--5. They are private working results with explicit scope,
not external peer-reviewed sources.
