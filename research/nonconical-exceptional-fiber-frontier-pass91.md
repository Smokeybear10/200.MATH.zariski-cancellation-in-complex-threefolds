# Nonconical recognition and the exceptional-fiber boundary

A relative linear equation now gives a complete written recognition
argument within the supplied constant-acceleration frame. In the
remaining cases, the highest adjoint has an exact global primitive
Jacobian factor. Its possible fixed locus lies above finitely many
points of the invariant plane, and every generic divisor constant
extension has degree at most three. The unrestricted cancellation
problem is not solved.

## 1. The question and the restricted hypotheses

The working interpretation of Luo's email is
\[
A[s]\simeq_{\mathbb C}\mathbb C^{[4]}
\quad\Longrightarrow\quad A\simeq_{\mathbb C}\mathbb C^{[3]}.
\tag{1}
\]
Luo has not confirmed the intended correction, field or dimension.
The email's literal conclusion \(X\simeq\mathbb A^1\) has the
wrong dimension for general r. This report keeps (1) as the full
working target, not as a conclusion of the restricted arguments.

The current branch assumes an actual original-coordinate LND
\[
\begin{gathered}
B=\mathbb C[x_1,x_2,x_3,z]=A[u],\qquad A=\ker E,\\
E^2x_i=0\ (i\le3),\qquad E^2z=q\in\mathbb C^*,\qquad
u=Ez/q,\qquad Eu=1,\\
S=\mathbb C[s_1,s_2]=\ker(W|A),\qquad Wu=0,\\
b=(Ex_1,Ex_2,Ex_3)^t\in S^3,\qquad
\Omega=\det[b,b_{s_1},b_{s_2}]\ne0 .
\end{gathered}
\tag{2}
\]
The plane and W are the actual highest-adjoint constructions of
pass88. The exact original good-speed completion supplies
\(R=S[A_1,A_2]\subset A=R[c]\). The pass90 volume argument proves
\(A_\Omega=R_\Omega\), bounds the defining equation of R by
relative degree \(1\le d\le3\), and gives a fixed-point-free
intrinsic action on \(A_\Omega\).

The cylinder makes \(\operatorname{Spec}A\) smooth and contractible.
The published Kaliman--Saveliev quotient theorem, applied with the
actual domination supplied by that cylinder, gives the invariant
plane and the nonempty curve quotient; faithful flatness follows
as recorded in the foundational proof.[^ks] None of these inputs
shows that an arbitrary sliced action admits the special frame (2).

## 2. Recognition for a relative linear equation

Suppose the irreducible defining relation is
\(\alpha A_1+\beta A_2+\delta=0\), with coefficients in S.
Faithful flatness contracts \(\delta\in(\alpha,\beta)A\) back
to \(\delta\in(\alpha,\beta)S\). Translate the generators to
remove that constant term. Primitivity makes \(\alpha,\beta\)
coprime, though their ideal need not be the unit ideal.

Factorial closure and divisibility in the actual UFD A then produce
an actual element \(t\in A\) with translated generators
\(\beta t,-\alpha t\). The zero-coefficient cases are included in
the [complete linear proof](nonconical-linear-relation-recognition-pass91.md).
Generic equality gives \(c\in K[t]\), where \(K=\operatorname{Frac}S\).
If one coefficient of c had a pole at an irreducible p of S,
minimal denominator clearing would make \(\bar t\) algebraic on
the whole generic p-fiber. Both relative generators would become
algebraic there, contradicting the actual-frame noncollapse theorem90.
Consequently
\[
\boxed{\quad d=1\quad\Longrightarrow\quad
A=S[t]\simeq\mathbb C^{[3]},\qquad B=S[t,u].\quad}
\tag{3}
\]
This conclusion does not require \(R=A\). The proof does not need
to exclude a possible failure of the smaller ring to contain t at
codimension-two base points. The linear note illustrates that issue
with an algebra-only example, not a realized nonconical frame.
The result is a restricted recognition theorem, not a claim of
historical novelty or a proof of (1).

## 3. A canonical global field and the size of the remaining support

Let \(T=\partial_z\) in the original coordinates and
\(H=[E,[E,T]]\). Define
\[
N(f)=\det\frac{\partial(s_1,s_2,u,f)}
 {\partial(x_1,x_2,x_3,z)},\qquad
\boxed{\ H=2\Omega N\ }.
\tag{4}
\]
The [global Jacobian proof](nonconical-global-jacobian-field-pass91.md)
derives the sign by Cauchy--Binet and the nilpotent Jacobian identity,
not by dividing on a dense open and presuming extension. N has
polynomial coefficients from its definition. Since it kills Omega,
local nilpotence transfers from H to N globally. It commutes with E,
kills u, and has intrinsic kernel S.

The same proof shows that N has coefficient gcd one. A hypothetical
gcd factor must lie in S; at its generic divisor, independence of
the conormal differential and two surviving differentials contradicts
the vanishing of all the Jacobian minors. On every generic base-divisor
fiber N is therefore a nonzero LND of a one-dimensional domain,
hence a translation over a finite constant extension.

It follows that the fixed locus of N maps to a finite set of closed
points of S. These points lie in \(\Omega=0\), because N is a
base-unit multiple of the already free action on \(A_\Omega\).
This removes an explicit divisor factor from H, but does not remove
all fixed points. The retained Weitzenbock fixed line illustrates
why primitivity and whole-scheme nonvanishing are weaker than freeness.

If N were proved free everywhere, the exact published free-action
theorem would identify \(A=S[t]\).[^ks] Its missing hypothesis has
been narrowed to the finitely supported exceptional locus; it has
not been established.

## 4. Divisor degrees and localized disconnectedness

For any irreducible \(p\in S\), let
\(V=S_{(p)}\) and \(k=\operatorname{Frac}(S/(p))\).
The whole divisor fiber is \(A_V/pA_V=k'[t]\), with k' finite
over k. Here \(A_V=A\otimes_S V\); this is not localization
at the prime pA of A. Choose one actual
relative generator U whose residue is transcendental, as guaranteed
by whole-divisor noncollapse. The
[residue-degree proof](nonconical-residue-degree-bound-pass91.md) gives
\[
\boxed{\quad [k':k]\,\deg_t\bar U
 \le\deg_v U\le d\le3.\quad}
\tag{5}
\]
The key step is the restriction of the actual p-divisor valuation
to the Gauss valuation on K(U). Independent residue classes lift
to independent vectors over K(U), bounding the residue extension
by the generic function-field degree. This avoids assuming that
\(R\to A\) is finite or that its whole p-fiber equals its image.

On \(D(\Omega)\), where the actual smooth presentation
\(A_\Omega=S_\Omega[Y,Z]/(F)\) is available, the
[fiber classification](nonconical-full-gradient-fiber-pass91.md)
gives an exact description of a second obstruction. Every closed
fiber is a disjoint union of curves isomorphic to the affine line.
If it is disconnected, degree at most three forces two or three
parallel straight affine lines. A parabola and a line cannot be
disjoint over C.

For such a fiber, \(F_m=aP(L)\) with P squarefree of degree two
or three. The full formal critical scheme is defined by \(P'(L)\),
can be nonreduced, and misses the entire zero fiber. Consequently
\[
(F_Y,F_Z)S_\Omega[Y,Z]=S_\Omega[Y,Z]
\quad\Longleftrightarrow\quad
\text{all closed fibers on }D(\Omega)\text{ are connected}.
\tag{6}
\]
The precise Bhatwadekar--Dutta criterion would recognize a relative
coordinate under the full-gradient premise.[^bd] The source note
and the fiber proof distinguish that premise from the unit gradient
only modulo F, which is what the actual volume calculation already
gives. Connectedness, and therefore that application, remains unproved.

## 5. A failed shortcut with exact evidence

The [DVR descent and multiplicity control](nonconical-divisor-descent-multiplicity-boundary-pass91.md)
proves a useful conditional statement: if the full smaller-ring
fiber is a domain, its noncollapsing map to the A-fiber is injective,
and repeated p-division gives \(R_V=A_V\) for \(V=S_{(p)}\).

The missing domain premise is substantial. In the polynomial algebra
\(A=\mathbb C[p,y,z]\), set \(\eta=pz-y^2\),
\(S=\mathbb C[p,\eta]\), and \(R=S[py,z]\). Its exact relation
is \(p^3Z-Y^2-p^2\eta=0\). The whole p-fiber of R is a doubled
line, but its image in the whole A-fiber is a polynomial line and
the latter has a quadratic constant extension. A is the finite
normalization of R, so even these additional properties do not
prevent loss of the full fiber information.

This control has a primitive commuting LND, a polynomial cylinder
and an actual quadratic coordinate. It is not the actual nonconical
highest-adjoint construction: the attempted good tuple has Jacobian
\(-y\), not a unit. It invalidates a proof shortcut, not cancellation.

## 6. Verification and remaining obligations

The full written derivations have separate AI reconstructions,
recorded in the [proof audit](proof-audits-pass91-working.md).
The [targeted verification](verification-pass91-working.json) records
finite exact polynomial controls separately from those arguments.
Passing the controls does not certify a universal theorem. The
[checkpoint](checkpoint-pass91-working.json) preserves the evidence
and the unresolved scope.

The next proof target is to use the actual original-coordinate
identities to exclude or resolve the finitely supported fixed locus
and the quadratic/cubic exceptional-fiber mechanisms. Abstract
primitivity, smoothness on an open set and a low-degree equation
have been shown insufficient on their own. An independent larger
obligation remains: reducing an arbitrary sliced four-variable
action to this frame, or finding a route that avoids that reduction.

No human expert review, formal proof certificate, established
novelty, public posting, submission or external contact has occurred.
The full goal remains active and unresolved.

## Sources

[^ks]: Shulim Kaliman and Nikolai Saveliev,
    [*C+-actions on contractible threefolds*](https://www.math.miami.edu/~kaliman/library/KaSa.michigan.2004.quotient.pdf),
    Lemma 2.1, Theorem 2.7 and Corollary 2.8.
    The exact cylinder application is written in
    [intrinsic-quotient](intrinsic-quotient-surface-pass.md).
    The free-action criterion requires absence of fixed points on
    the entire smooth contractible threefold, not just on an open set.

[^bd]: S. M. Bhatwadekar and A. K. Dutta,
    [*Kernel of locally nilpotent R-derivations of R[X,Y]*](https://repository.ias.ac.in/3203/1/311.pdf),
    *Transactions of the AMS* 349 (1997), 3303--3319,
    Proposition 4.4, printed p.3314, with the Section 4 hypotheses.
    Exact applicability and the separating control are recorded in
    [source-gate91](low-degree-full-gradient-source-gate-pass91.md).
