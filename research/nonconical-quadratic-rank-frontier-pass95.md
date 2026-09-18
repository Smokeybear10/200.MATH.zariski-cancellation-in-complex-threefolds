# Quadratic fibers and the remaining cancellation gap

In the supplied nonconical quadratic frame, every reduced fiber
of the canonical quotient is a disjoint union of smooth open
affine lines, and the quotient differential has rank at least
one everywhere. This improves the earlier generic-component
restriction. It does not make the action free and does not
identify the unknown threefold with affine space.

Two other restrictions complement this result. A surviving
quadratic generator gives an exact local differential model
when the first normal action is nonzero. In the cubic branch,
certain rank-zero components force a sharply bounded
polynomial leading model. An explicit polynomial automorphism
also shows that extracting a coordinate by a constant linear
combination of projected generators can fail for every choice
of coefficients, even when the invariant ring is already
polynomial.

The general target remains
\[
A[s]\simeq\mathbb C^{[4]}
\quad\Longrightarrow\quad A\simeq\mathbb C^{[3]}.
\tag{1}
\]
The interpretation of the professor's original statement as
this complex-threefold question is still unconfirmed. The
results below require an additional actual frame; no reduction
from an arbitrary sliced action to that frame is available.

## 1. Assumptions and the whole quadratic fiber

The actual frame is the one specified in
[global Jacobian91](nonconical-global-jacobian-field-pass91.md).
It starts with original polynomial coordinates on
\(B=A[u]=\mathbb C^{[4]}\), a sliced LND E, three coordinates
whose E-second derivatives vanish, and a fourth whose second
derivative is a nonzero complex constant. The nonconical
velocity determinant is nonzero, but need not be a unit.

The retained construction supplies a primitive canonical
Jacobian LND N on A, its actual invariant plane
\(S=\mathbb C[s_1,s_2]\), a faithfully flat quotient, and
relative generators \(A=S[A_1,A_2,c]\). On the generic
fiber \(A_K=K[w]\), the quadratic branch has generator
degrees at most 2,2,4. These are consequences within the
specified frame, not assumptions supplied by cancellation
alone.

For a closed base point m, let \(C=A/mA\). Its generic
component multiplicities satisfy \(\sum\mu_i\le4\), and
the whole ring C is a pure Cohen--Macaulay curve. The
[everywhere-rank proof](quadratic-quotient-rank-everywhere-pass95.md)
gives actual component parameters \(U_i\) and polynomials
\(b_i\) such that
\[
\begin{gathered}
C=\prod_i C_i,\qquad
(C_i)_{\rm red}=\mathbb C[\bar U_i,1/b_i(\bar U_i)],\\
R_i=\mathbb C[U_i,1/b_i(U_i)]\subset C_i,\qquad
C_i\simeq R_i^{\mu_i}\ \text{as an }R_i\text{-module},
\qquad 1\le\mu_i\le3,\\
\boxed{\operatorname{rank}(ds_1,ds_2)_p\ge1
\quad\text{for every }p\in\operatorname{Spec}A.}
\end{gathered}
\tag{2}
\]
The factors describe the entire thickenings, not just their
reductions. The module isomorphism does not specify the
algebra structure.

The proof has four separate steps. A multiplicity-one
component carries a nontrivial translation, so it is an
affine line and cannot meet another component. Two remaining
fixed components would exhaust multiplicity four with
profile (2,2). Their disjointness is the new local argument
described below. A sole component of multiplicity four is
excluded by the retained whole-irreducible-fiber ramification
theorem92, whose applicability uses the actual cylinder
and quotient hypotheses.[^ramification]

Once components are disjoint, their idempotents lift across
the nilradical. Each actual parameter ring embeds into its
component thickening. Every algebra generator differs from
its lifted residue by a nilpotent, proving finiteness over
that ring. The absence of embedded primes gives
torsion-freeness; the parameter ring is a PID, so the finite
module is free of rank \(\mu_i\).

At any closed point of the component, the parameter
transverse section therefore has length \(\mu_i\le3\).
If both base differentials vanished, the two base equations
on the resulting regular surface would lie in its maximal
ideal square. Two equations can kill at most two of the
three independent quadrics, forcing length at least four.
This contradiction proves (2), including isolated points.

## 2. Why two double components cannot meet

The [double-component proof](quadratic-double-components-disjoint-pass95.md)
uses saturation of the degree bound, not an assumption that
all fibers are reduced. In a (2,2) fiber, every admissible
linear projection of the relative generators has total
length four. Applying the projection argument in all
directions forces both reduced components to be actual
affine lines in the relative three-space.

Suppose the lines met. At quotient rank zero, a transverse
surface has a two-generated complete intersection of length
four with both equations of order at least two. Their
quadratic initials must be independent and coprime.
Vanishing of the actual Jacobian field on the two lines
then reduces the leading pencil, by constant linear changes,
to \(P^2,QZ\). Its Jacobian field is a nonzero multiple of
\(P(Q\partial_Q-Z\partial_Z)\), which is not locally
nilpotent.

At quotient rank one, quotienting by one regular invariant
parameter gives a smooth surface. The other invariant has
divisor equal to a unit times \(y^2z^2\); the transverse
length four proves the factor is a unit. The leading
Hamiltonian field is a nonzero multiple of
\(yz(y\partial_y-z\partial_z)\), also not locally nilpotent.

In both cases, actual finite N-degree of the parameter
functions forces their polynomial associated-graded
derivation to be locally nilpotent. This contradiction
does not assume that localization or completion preserves
local nilpotence. Completion is used only for the regular
power-series descriptions.[^complete]

The former power-column alternative for a collapsed double
component required such an intersection, so it is excluded
when the first normal action is nonzero. The remaining
column span is \(\mathbb C+\mathbb Cc\). Its weighted model
has constant coefficients: after the stated normalization,
\(F_*=x+by^2,\ G_*=y\), with \(b\in\mathbb C\), and
\(D_*=\nu(-x\partial_y+2ay\partial_c)\) for nonzero
complex a and \(\nu\). This is a weighted statement.
In particular it does not prove \(N^2G=0\) on A.

## 3. A surviving generator gives actual local parameters

For a noncollapsed fixed component, a constant combination
U of the two good generators survives nontrivially.
The degree bound forces multiplicity two and equality of
its component field with \(\mathbb C(\bar U)\).
All surviving good combinations have field degree one,
which forces both reduced good functions to be affine
linear in \(\bar U\). The third residue can introduce
punctures but no singularity: the reduced ring is
\(\mathbb C[\bar U,1/b(\bar U)]\).

Assume additionally that the first normal action is
nonzero. The [local-model proof](noncollapsed-quadratic-local-translation-model-pass95.md)
constructs actual polynomial functions
\[
\begin{gathered}
r=N^2U\in S,\qquad v=NU,\qquad \eta=2rU-v^2\in S,\\
Nr=0,\qquad Nv=r,\qquad NU=v,\\
\mathfrak qA_{\mathfrak q}=(r,v),\qquad
\mathfrak mS_{\mathfrak m}=(r,\eta),\qquad
N=r\partial_v+v\partial_U .
\end{gathered}
\tag{3}
\]
The differentials \(dr,dv,dU\) form a basis at the
generic component. Both displayed parameter ideals are
actual local ideals; equality on the base follows by
faithfully flat contraction of the length-two ideals.

Equation (3) is stronger than a leading approximation.
Nevertheless, it neither makes r and \(\eta\) global
coordinates of S nor identifies the actual local ring
with a polynomial localization. The nonzero-first-normal
assumption must not be silently dropped.

## 4. The cubic leading pencil

The [cubic-pencil proof](nonconical-cubic-quadratic-pencil-pass95.md)
works on a different branch. At a collapsed rank-zero
component it uses the literal polynomial associated-graded
ring \(\mathbb C[c,\xi,\eta]\), with normal variables of
weight one and c of weight zero. The base quadratic
initials \(\phi,\psi\) give
\(D=\nu\operatorname{Jac}(\phi,\psi,-)\), and the actual
degree bounds force \(D^4\xi=D^4\eta=0,\ D^7c=0\).
Thus D is an LND on this polynomial graded ring.

If \(\phi,\psi\) are independent over \(\mathbb C(c)\)
and the component multiplicity is five or six, they share
a linear factor. The polynomial kernel-plane theorem
is applied only on the literal graded affine three-space,
where its hypotheses hold.[^kernel]
Weight and factorial-closure arguments then give
\[
\begin{gathered}
(\phi,\psi)=(P^2,PQ)\ \text{after a constant pencil change},\\
\binom P Q=M(c)\binom\xi\eta,\qquad
M\in\operatorname{GL}_2(\mathbb C[c]),\qquad \deg_cM\le3,\\
D=\beta P^2\partial_c\quad\text{with }P,Q\text{ held fixed},
\qquad \beta\in\mathbb C^*.
\end{gathered}
\tag{4}
\]
The degree-three bound is sharp for leading operators:
\(P=\xi,\ Q=\eta+c^3\xi\) gives \(D^3\eta\ne0\) and
\(D^4\eta=0\); replacing \(c^3\) by \(c^4\) fails.
These are graded controls, not lifts to the original frame.

The proportional-pencil case has a different conclusion:
when the proportionality function is nonconstant, the
binary quadratic is a repeated linear factor and the
leading field squares to zero on both normal variables.
A constant proportionality can make this whole leading
operator zero, leaving higher orders uncontrolled.

Two explicit complete intersections of lengths five and
six have the same leading pencil \((x^2,xy)\). Therefore
the leading classification alone cannot distinguish all
remaining multiplicities or supply an exclusion.

## 5. A failed global coordinate-extraction shortcut

The [projected-generator obstruction](projected-generator-linear-extraction-obstruction-pass95.md)
is an actual polynomial-ring example, not a hypothetical
threefold. Let
\(F=a^2/2+b^3/3+c^5/5\) and take original coordinates
\(x_0=s+F,\ x_1=a+x_0^2,\ x_2=b+x_0^3,\ x_3=c+x_0^4\).
Both directions of this triangular polynomial inverse
are explicit. For the specified slice s of \(E=\partial_s\),
the four projected generators are
\(F,\ a+F^2,\ b+F^3,\ c+F^4\).

Every nonzero constant linear combination of these four
functions is nonconstant and has a critical point.
For arbitrary coefficients, the proof constructs a
polynomial curve on which all three gradient equations
reduce to one nonconstant complex polynomial with
constant term one. A nonzero root supplies the critical
point. This is an all-coefficient argument, not a sample
of coefficient vectors.

Consequently no such combination is a coordinate.
Nonlinear extraction succeeds immediately, and changing
the slice to \(x_0\) gives ordinary coordinates. The
example therefore defeats the specified linear shortcut,
not cancellation or every possible change of slice.

## 6. Verification and the next mathematical obligations

The three [targeted symbolic checks](verification-pass95-working.json)
pass. They cover the initial operators and weighted
identity, the explicit inverse and gradient calculation,
and the sharp cubic model with the two Artin algebras.
They do not verify universal geometric statements,
the topological dependencies, or equation (1).

The saved proofs have separate AI mathematical reviews.
Human expert review, proof-assistant verification and
historical novelty review have not been completed.
The [proof audit](proof-audits-pass95-working.md) separates
these evidence categories. The
[checkpoint](checkpoint-pass95-working.json) records
the saved artifacts and their checksums.

The immediate special-case obligation is to control the
rank-one fixed components that (2) permits. The exact
model (3), the collapsed weighted model, and compatibility
between different components over one base point are
possible inputs. They must be used with the original
frame identities, not only their intrinsic quotient
properties.

The independent general obligation is still to reduce an
arbitrary sliced action on affine four-space to a
recognizable frame, or to find a different global
recognition argument. Neither improving local multiplicity
bounds nor accumulating symbolic examples fulfills that
obligation.

## Sources

[^ramification]: [Whole-irreducible-fiber ramification92](nonconical-irreducible-fiber-ramification-pass92.md),
    especially equations (5)--(6), derives the needed
    multiplicity statement from Shulim Kaliman,
    [*Free C+-actions on C3 are translations*, final author version](https://www.math.miami.edu/~kaliman/library/Ka.invent.2004.c%2B.pdf).
    The derived statement requires the whole reduced fiber
    to be irreducible. It is not a theorem about one component
    of an arbitrary reducible fiber.

[^complete]: The Stacks Project,
    [Lemma 10.160.10(2), tag 0C0S](https://stacks.math.columbia.edu/tag/0C0S).
    Only the coefficient-compatible description of the
    complete regular local ring is used here.

[^kernel]: Shulim Kaliman and Nikolai Saveliev,
    [*C+-actions on contractible threefolds*, Corollary 2.8(2)](https://www.math.miami.edu/~kaliman/library/KaSa.michigan.2004.quotient.pdf),
    Michigan Mathematical Journal 52 (2004).
    The application in Section 4 is to polynomial affine
    three-space, not to an unverified global model of A.
