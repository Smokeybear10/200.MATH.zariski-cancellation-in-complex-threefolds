# Exact return domains and the remaining recognition gap

The rational return in the one-quadratic-coordinate case has an exact
regular locus. It is disjoint from the entire good-speed zero scheme.
This rules out an earlier proposed route through regularity at those
points. Its polynomial fixed functions can also be computed exactly,
but the resulting generically quadratic morphism is not a finite
global quotient in the proper-speed-ideal case.

These statements concern an additional coordinate hypothesis inside
the corrected complex-threefold cancellation problem. They neither
establish that every sliced action has that coordinate form nor
recognize every kernel within the restricted form. General cancellation
remains unproved. Historical novelty, expert review and formal
verification are not established.

## 1. Precise scope

The working interpretation of the professor's question is
A[s] isomorphic to C^[4] implies A isomorphic to C^[3]. The supplied
email's conclusion A^1 has a dimensional mismatch for r greater than
one; the intended correction, field and dimension remain unconfirmed.
The present deduction assumes actual polynomial coordinates and an
actual global slice:
\[
\begin{gathered}
B=\mathbb C[x_1,x_2,x_3,z],\quad E\in\operatorname{LND}(B),
\quad E(s)=1,\quad A=\ker E,\quad B=A[s],\\
a_i=E(x_i),\quad E(a_i)=0,\quad b=E(z),\quad E(b)=q,
\quad E(q)=0,\quad q\ne0,\quad I=(a_1,a_2,a_3)B.
\end{gathered}
\tag{1}
\]
The phrase one-quadratic-coordinate does not mean rank one in the
standard invariant-coordinate definition of the rank of an LND.
No invariant ambient coordinate is supplied by (1).

## 2. An exact pole locus closes the regularity route

The original polynomial flow returns to the same z at rational time
-2b/q. The original polynomial slice recovers precisely that time
from the returned point. With g=gcd(q,b) and h=q/g, the
[regular-locus proof](rank-one-return-regular-locus-pass85.md) gives
\[
\begin{gathered}
\rho=(x-2ba/q,z),\qquad s\circ\rho-s=-2b/q,\\
\operatorname{Reg}(\rho)=D(h),\qquad E(h)=0,\qquad
\operatorname{Reg}(\rho)\cap V(I)=\varnothing.
\end{gathered}
\tag{2}
\]
Here regularity is tested in every local ring of the original source,
not only at generic points of divisors. The slice identity makes
regularity equivalent to membership of b/q in that local ring. The
UFD reduction of the fraction then gives exactly D(h).

The disjointness uses b being a unit modulo I and q belonging to its
radical. The latter has an independent elementary orbit-degree proof:
at a good-speed zero, a genuinely quadratic z orbit could not compose
with the polynomial slice to give a linear time function.

For the z=0 specialization the same statement holds with b_0,q_0
and J=I intersect C[x_1,x_2,x_3], provided q_0 is not identically zero.
Thus the sufficient local membership criterion from the
[pass83 return note](rank-one-return-map-integral-closure-pass83.md)
remains logically valid, but its regular-return premise cannot hold
at an actual speed zero in this nonzero-q_0 branch. Trying to prove
automatic regularity there is no longer an open proof task.

The [actual cancellation control](return-denominator-cancellation-control-pass85.md)
has q=a^3(a-1), b=(a-1)(1+ax) and return
(a,-x-2/a,c,z). It extends across a=1 after common-factor cancellation
and has a genuine pole along a=0. In particular D(q) need not be
the maximal regular locus. Evaluation of an unreduced 0/0 expression
at a=1 is not used.

## 3. The exact fixed ring does not cancel the variable

All factors of an invariant in B are invariant, by additivity of
LND degree. This proves that A is a UFD without first recognizing it
as a polynomial ring. Define
\[
v=b/g-hs\in A,\qquad w=z-bs+qs^2/2\in A,
\qquad T=hs^2+2vs,\qquad z=w+(g/2)T.
\tag{3}
\]
The pair h,v is coprime in A. Over its fraction field the return is
the reflection s to -s-2v/h. Coefficient descent modulo each possible
prime denominator proves the following
[polynomial fixed-ring and finiteness statements](rank-one-centered-return-quotient-pass85.md):
\[
\begin{gathered}
B\cap\operatorname{Fix}_{\operatorname{Frac}B}(\rho)=A[T],\\
B=A[T,S]/(T-hS^2-2vS),\qquad
B\text{ finite over }A[T]\Longleftrightarrow h\in A^*.
\end{gathered}
\tag{4}
\]
After h is inverted the extension is free of rank two. When h is
a nonunit, the return is not a global group action on B. In that
case the intersection in (4) must not be described as the invariant
ring of a globally regular finite-group action.

At h=0,v nonzero, the residue-field map is linear, not quadratic.
At h=v=0 it is constant. The actual speed-zero points belong to the
linear case, because g and v are units at them. When I is proper,
h is a nonunit by (2), so the global morphism is not finite.

The actual two-speed frame in the control note has
h=2ab, v=1+ac+b^2 and w=bc. Their coprimality does not exclude
common zeros: a=0,b=i gives h=v=0. These are not good-speed zeros.
The example refutes an upgrade from coprimality to a unimodular pair,
not cancellation or speed-ideal membership.

Abstractly A[T] is isomorphic to A[s], hence to B. This is another
polynomial cylinder over A, not a proof that A is C^[3]. The status
of z as a coordinate in B cannot be silently transferred to A[T].

## 4. Literature gates remain substantive

The [bounded source audit](rank-one-quasi-nice-source-scope-pass85.md)
checks primary statements about nice and quasi-nice derivations,
image ideals and inner integral closure. It does not locate a theorem
recognizing the whole class (1). A verified invariant ambient
coordinate would allow an established recognition theorem to apply
because the slice already ensures that A is regular.[^recognition]

One sufficient extra hypothesis is stability of the actual good
subring C[x_1,x_2,x_3] under E. The standard three-variable nice
theorem then supplies an invariant linear coordinate.[^nice]
The known inclusion partial_z(a_i) in I is weaker than the required
vanishing of all partial_z(a_i), and the actual two-speed frame
distinguishes them.

The earlier strict-slice certificate contracts exactly to A:
\[
q^N\in I_A^{N+1},\qquad I_A=(a_1,a_2,a_3)A,
\qquad N=(\deg_x(s)-1)^2
\tag{5}
\]
when I is proper and q is nonzero. This is inner integral closure
in the established terminology.[^closure] It is not q in I_A.
Natural closedness of I_A would suffice for that membership, but
is not proved. Likewise the full sliced image ideals are all A,
whereas the selected three-speed ideal I_A need not be A.

## 5. Verification and live obligations

The [standalone checker](return_denominator_checks_pass85.py) has
exactly two finite methods, testing the actual common-factor control
and the retained two-speed frame. Both coordinate inverse orders,
velocity layers, normalized returns and the stated fiber distinctions
are checked symbolically. The universal proofs of (2) and (4) are
written arguments with separate AI reconstructions, not consequences
of these two examples.

The [targeted capture](verification-pass85-working.json),
[proof audit](proof-audits-pass85-working.md) and
[checkpoint](checkpoint-pass85-working.json) give exact run and
integrity scope. No full regression or exhaustive action search ran
in this pass. The research goal remains active.

The next recognition task must use a genuine additional consequence
of the supplied coordinate system. One concrete target is the fact
that z=w+gvs+(gh/2)s^2 is an original coordinate of B, so its
differential is unimodular and every z fiber is affine three-space.
Neither property has yet been converted into an invariant ambient
coordinate or a simultaneous coordinate reduction. The broader
problem of obtaining a restricted frame from an arbitrary sliced
action also remains open in this investigation.

## Sources

[^recognition]: Bhatwadekar, Gupta and Lokhande,
    [*Some K-theoretic properties of the kernel of a locally nilpotent
    derivation on k[X1,...,X4]*](https://arxiv.org/pdf/1501.01438v1),
    Theorem 3.5, PDF p.11. The invariant-coordinate premise is required.

[^nice]: Dasgupta and Gupta,
    [*Nice derivations over principal ideal domains*](https://arxiv.org/pdf/1701.03635v1),
    Theorem 3.1(i), reproducing the relevant three-variable theorem.

[^closure]: Epstein and Hochster,
    [*Continuous Closure, Axes Closure, and Natural Closure*](https://sites.lsa.umich.edu/hochster/wp-content/uploads/sites/1337/2024/08/CnClTAMS.pdf),
    Theorem 5.4 and Definition 5.9. This supplies closure terminology,
    not the proof of the explicit original-action exponent in (5).
