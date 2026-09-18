# The three conductor pairings obstruct every ambient additive action

The investigation started with the next plinth exponent \(k=2\), but the
obstruction below is stronger: **the unchanged pinched surface cannot be the
prescribed exceptional hypersurface of any primitive ambient action extending
\(u\delta_0\), at any exponent.** It is an obstruction to an ambient action,
not to a hypersurface embedding without such an action, and not a solution
of threefold cancellation.

The new ingredient is separatedness of the actual total space. After an
ordinary scheme base change to the completed quotient plane at its node,
the three conductor lines force three specific open quotient charts.
Translation cocycles between those charts cannot define a separated
\(\mathbb G_a\)-torsor. The argument does not assume that the geometric
quotient is an affine scheme, that later centers are monogenic, or that a
restricted invariant lifts to the ambient invariant ring.

## 1. Fixed surface and the actual-realization assumption

Retain precisely the surface and scaling from
[passes 25](ambient-lifting-pass25.md) and
[33](nodal-plinth-realization-pass33.md):
\[
B_0=\mathbb C[u,y,z]/(a(u)z-y(y-1)),\qquad
a(u)=(u-1)(u-i),\qquad d=u^4-1,
\]
\[
R=B_0\times_{\mathbb C[t]^6}\mathbb C[t]^3,
\qquad D=u\delta_0,
\quad\delta_0u=0,\ \delta_0y=a(u),\ \delta_0z=2y-1.
\tag{1}
\]
Write the conductor lines of \(R\) as \(L_A,L_B,L_C\). Their exact
normalization preimages are

| Line | First normalization line | Second normalization line |
| --- | --- | --- |
| \(L_A\) | \(u=1,y=0\) | \(u=i,y=0\) |
| \(L_B\) | \(u=1,y=1\) | the ordinary line \(u=-i\) |
| \(L_C\) | the ordinary line \(u=-1\) | \(u=i,y=1\) |

On every line the already fixed scaled parameter satisfies \(D(t)=1\).
No pairing or parameter is changed in this proof.

Put
\[
s=u^2,\quad S=\mathbb C+d\mathbb C[s]
 \simeq\mathbb C[d,v]/(v^2-d^2(d+1)),\quad v=ds,
\]
\[
T=\ker D=\mathbb C+d\mathbb C[u],\quad
\mathfrak n=(d,v)\subset S,
\quad R/\mathfrak nR=\mathbb C[t]^3.
\tag{2}
\]

Assume for contradiction that a primitive LND \(E\) on
\(W=\mathbb C[X,Y,Z]\) and a prime invariant \(F\) give
\(W/(F)=R\) with induced derivation \(D\). The previously proved
[all-speed reduction](all-speed-ambient-obstruction-pass33.md) gives
\[
C=\ker E\simeq\mathbb C^{[2]},\qquad C/(F)=S
\tag{3}
\]
as the actual embedded residue algebra. Let \(\mathfrak m\subset C\)
be the node ideal over \(\mathfrak n\).
The [isolation theorem](odd-realization-pass34.md) gives
\[
\operatorname{pl}(E)=F^k\beta C,\qquad
\beta=\kappa+FQ,\quad\kappa\in\mathbb C^*,
\tag{4}
\]
so other plinth components do not pass through this node. Pass 35 proves
\(k\ge2\). The proof below does not need the value of \(k\).

## 2. A separated torsor cannot have these three overlaps

Here is the elementary algebraic obstruction used later.

**Fork-torsor lemma.** Let \(A=\mathbb C[[x,y]]\). Suppose an algebraic
space \(Q\) over \(\operatorname{Spec}A\) has three open subspaces
\(U_A,U_B,U_C\), each identified with \(\operatorname{Spec}A\) over
the base, whose intersections under these identifications are
\[
U_A\cap U_B=D(y),\quad
U_A\cap U_C=D(x),\quad
U_B\cap U_C=D(xy).
\tag{5}
\]
There is no \(\mathbb G_a\)-torsor \(X\to Q\) for which
\(X\to\operatorname{Spec}A\) is separated.

Proof. A \(\mathbb G_a\)-torsor over an affine scheme is trivial:
its class lies in \(H^1_{\mathrm{fppf}}(\operatorname{Spec}A,\mathcal O)=0\).
Thus the inverse images \(X_i\) of these opens have coordinates
\(X_i=\operatorname{Spec}A[t_i]\). An equivariant change of these
coordinates is a translation, not an arbitrary affine-linear map. Write
\[
t_B=t_A+\alpha,\quad \alpha\in A[y^{-1}],
\qquad
t_C=t_A+\zeta,\quad \zeta\in A[x^{-1}].
\tag{6}
\]
On the third intersection, \(t_C=t_B+\zeta-\alpha\).

If \(\alpha\in A\), the graph \(t_B-t_A=\alpha\) has points over
the closed base point. But \(X_A\cap X_B\) has none. Its graph over
\(D(y)\) is therefore not closed in
\(X_A\times_A X_B\), contrary to separatedness of \(X\).
Consequently, in a reduced fraction,
\[
\alpha=P/y^n,\quad n\ge1,\quad P\in A,\quad y\nmid P.
\tag{7}
\]
The graph closure is exactly
\[
y^n(t_B-t_A)-P=0.
\tag{8}
\]
Indeed \(A[t_A,t_B]\) is a UFD. The displayed polynomial is
primitive and irreducible, is not divisible by \(y\), and therefore
its ideal is already saturated with respect to \(y\). After inverting
\(y\) it is the graph ideal, proving the asserted contraction.
If \(P\) were in \((x,y)\), (8) would contain the entire closed
product fiber. Thus separatedness forces \(P\in A^*\).
The same argument gives
\[
\zeta=Q_0/x^m,\quad m\ge1,\quad Q_0\in A^*.
\tag{9}
\]

The third translation now has numerator
\[
\zeta-\alpha=\frac{N}{x^my^n},\qquad
N=Q_0y^n-Px^m.
\tag{10}
\]
Since both numerators are units, \(x\nmid N\) and \(y\nmid N\).
The same primitive-polynomial argument shows that its exact graph closure is
\[
x^my^n(t_C-t_B)-N=0.
\tag{11}
\]
However \(N\in(x,y)\), so this closure has points over the closed
base point, whereas \(X_B\cap X_C\) has none. It contradicts
separatedness once more. This proves the lemma.

It is unnecessary for the three opens to cover all of \(Q\).
Additional charts cannot fix a diagonal that is already nonclosed in
\(X_B\times_A X_C\).

## 3. The actual quotient is free and smooth near the node

The restriction of \(E\) to the prescribed surface has its only fixed
line over the distinct smooth point \(s=0\) of \(\operatorname{Spec}S\).
The node is \(s=1\sim-1\). After replacing the base by
\(\operatorname{Spec}C_{\mathfrak m}\), this fixed line is absent.
Outside \(F=0\), (4) makes the local-slice derivative a unit, so the
action has no geometric fixed points there as well. Hence it has none
anywhere over this local base. Scheme-theoretic freeness is verified below.
This does not assert that a free action there has an affine
quotient with connected fibers or a global slice.

For primitive LNDs on \(\mathbb C^{[3]}\), the inherited primitive
Jacobian identity is
\[
E=c\operatorname{Jac}(f,g,\cdot),\quad c\in\mathbb C^*,
\qquad C=\mathbb C[f,g].
\tag{12}
\]
At a free point its coefficient vector is nonzero, so
\(d f,d g\) are independent. The actual quotient morphism is
therefore smooth of relative dimension one everywhere over the local
base, by the Jacobian criterion. These properties persist under the
following ordinary scheme base change.

Take the completed base
\[
A=\widehat{C_{\mathfrak m}}.
\tag{13}
\]
This is a regular complete local ring with residue field \(\mathbb C\).
Choose invariant lifts of \(d,v\). Since \(F\in\mathfrak m^2\),
they are a regular parameter pair and identify
\(A=\mathbb C[[d,v]]\). The kernel of the map to the completed
nodal curve is generated by
\(v^2-d^2(1+d)\). Thus, for a unit \(\epsilon\in A^*\),
\[
F=\epsilon\bigl(v^2-d^2(1+d)\bigr).
\]
Set
\[
x=v-d\sqrt{1+d},\qquad y=v+d\sqrt{1+d}.
\tag{14}
\]
Their independent linear terms show that \(A=\mathbb C[[x,y]]\),
and \(F=\epsilon xy\). The branch \(x=0\) is the normalized base
near \(s=1\); \(y=0\) is the one near \(s=-1\).

Define
\[
X_A=\operatorname{Spec}(W\otimes_C A).
\tag{15}
\]
This is a scheme, affine and separated over \(A\), not a formal scheme
and not the completion of the coordinate ring along all points of a
line. Completion is flat, so its exceptional surface is exactly
\(R_A=R\otimes_S A/(F)\).

To establish scheme-theoretic freeness and the étale quotient, first
consider the action relation
\[
\mathbb G_a\times X_A\longrightarrow X_A\times_A X_A
\tag{16}
\]
Both sides are smooth curves relative to the
first \(X_A\) projection; its relative differential is the nowhere
zero generator \(E\), hence it is étale. Over an algebraically closed
field of characteristic zero a proper subgroup scheme of
\(\mathbb G_a\) is trivial. The nowhere zero tangent vector excludes
the whole stabilizer, so geometric stabilizers are trivial. Thus (16)
is universally injective and therefore an open immersion. In particular
it is a monomorphism, giving freeness on all scheme-valued points,
not just on complex points.

The quotient theorem now supplies the algebraic space
\(Q=X_A/\mathbb G_a\) and actual fppf torsor \(p:X_A\to Q\).
The étale quotient criterion for the open equivalence relation (16)
makes \(q:Q\to\operatorname{Spec}A\) étale. In particular this is
stronger information
than the mere existence of an abstract orbit space.

## 4. Each of the three orbit points has an actual open base chart

The closed fiber of \(X_A\) is the three translating lines in (2).
The torsor quotient consequently has precisely their three orbit
points \(q_A,q_B,q_C\) over the closed point of \(A\).

Since \(A\) is strictly henselian, an étale map to
\(\operatorname{Spec}A\) has a section through any point of its
closed fiber with residue field \(\mathbb C\). This applies to the
algebraic space \(Q\) without assuming it is a scheme: choose an
affine étale scheme chart through that point, apply the henselian
retraction criterion to the resulting étale \(A\)-algebra, and
compose with the chart map. A section of an étale morphism is an
open immersion, by base change of its open diagonal.

Thus there are three actual open immersions
\[
\sigma_i:\operatorname{Spec}A\hookrightarrow Q,
\qquad U_i=\sigma_i(\operatorname{Spec}A),\quad i=A,B,C.
\tag{17}
\]
Their inverse images \(X_i\subset X_A\) are invariant open
subschemes and trivial torsors \(\operatorname{Spec}A[t_i]\).
The closed fiber of \(X_i\) is exactly \(L_i\).

## 5. The section overlaps are forced by the original gluing

This is where the closed conductor labels must be connected to actual
generic orbits. Merely assigning labels to three abstract charts would
not establish the result.

Flat base change preserves the finite normalization/pinching diagram
in (1). Explicitly put
\[
u_r(d)=r(1+d)^{1/4},\qquad r\in\{1,-1,i,-i\}.
\tag{18}
\]
The four factors \(u-u_r(d)\) of \(u^4-(1+d)\) are pairwise
comaximal, since their constant differences are nonzero. The finite
normalization after this base change is
\[
B_A=B_0\otimes_S A/(F)=\prod_{r\in\{1,-1,i,-i\}} B_r,
\]
\[
B_r=\mathbb C[[d]][y,z]/(a(u_r(d))z-y(y-1)),
\qquad v=r^2d\sqrt{1+d}\text{ on this component}.
\tag{19}
\]
For \(r=1,i\), the coefficient \(a(u_r(d))\) is \(d\) times
a unit. These are normal domains with generic fiber an affine line
and closed fiber the two lines \(y=0,1\). For \(r=-1,-i\), that
coefficient is a unit and the ring is \(\mathbb C[[d]][y]\).
Normality in the split case can be checked directly: away from
\(d=0\) the ring is a polynomial ring over \(\mathbb C((d))\),
and at \(d=0\) the derivative \(2y-1\) is a unit at every point
of either closed line. The hypersurface is regular there.

For completeness, these really give the normalization of \(R_A\):
the injection \(R\to B_0\) remains injective after the flat base
change, so \(R_A\) is reduced; the map to (19) is finite and an
isomorphism after inverting \(d\); and (19) is normal. Their total
quotient rings therefore agree. The common conductor-line quotient
and the table in Section 1 are unchanged, because the base action on
each of the six closed lines factors through \(S/\mathfrak n=\mathbb C\).

Now \(X_i/(F)\to\operatorname{Spec}R_A\) is an open immersion,
not merely a map of completed point germs. Its normalization is
\[
\operatorname{Spec}(A/(x))[t_i]
\ \amalg\ \operatorname{Spec}(A/(y))[t_i].
\tag{20}
\]
Normalization commutes with restricting to this open subset, so its
two components are the open restrictions of the two \(B_r\)'s
meeting the actual line \(L_i\). Formula (19) and the unchanged
table consequently give the following generic-orbit incidences:

| Section | Orbit over the generic \(x=0\) branch | Orbit over the generic \(y=0\) branch |
| --- | --- | --- |
| \(U_A\) | the \(r=1\) orbit | the \(r=i\) orbit |
| \(U_B\) | the \(r=1\) orbit | the \(r=-i\) orbit |
| \(U_C\) | the \(r=-1\) orbit | the \(r=i\) orbit |

Each generic line in (19) is one orbit, since \(E\) is nonzero on
it. Thus \(U_A,U_B\) agree over the generic \(x\)-branch,
\(U_A,U_C\) agree over the generic \(y\)-branch, and
\(U_B,U_C\) agree over neither. Over \(D(F)=D(xy)\) the original
local-slice theorem identifies the quotient with the base, so all
three sections agree there. They do not agree at the closed point,
where their images are the three distinct orbit points.

There are no unexamined points outside \(D(xy)\): in the two-dimensional
regular local ring \(A\), the only primes containing \(x\) or \(y\)
are \((x),(y),(x,y)\). Intersections of these open base sections
are themselves open subspaces of \(\operatorname{Spec}A\). The
incidence table therefore proves their exact scheme intersections
\[
U_A\cap U_B=D(y),\qquad U_A\cap U_C=D(x),\qquad
U_B\cap U_C=D(xy).
\tag{21}
\]
No global connected-fiber theorem, properness assumption, or unproved
normalization surjectivity was used to infer them.

## 6. Consequences and precise limits

Equations (17)-(21) put the actual torsor \(X_A\to Q\) under the
fork-torsor lemma. This contradicts the separatedness of the affine
scheme (15). Therefore the primitive ambient realization assumed in
Section 1 does not exist, for **any** \(k\). In particular the next
case \(k=2\) and all higher modification towers are excluded without
assuming a lift \(T\to C\) or any global recursive presentation.

Combining with the already proved all-speed reduction yields a further
conditional statement about embeddings:

**Corollary.** In any hypothetical hypersurface presentation
\(W/(F)\simeq R\) with \(W=\mathbb C^{[3]}\), no ambient LND
preserving \((F)\) can induce a nonzero LND on \(R\).

Indeed an LND preserving the prime equation fixes it, by additivity of
LND degree applied to \(E(F)\in FW\). If its restriction is nonzero,
divide it by its invariant coefficient gcd. The primitive restriction
is still nonzero. The earlier all-speed theorem forces that primitive
restriction, after a nonzero scalar rescaling, to be the same
\(u\delta_0\), and forces the same embedded nodal base \(S\).
The theorem just proved rules it out.

This does **not** exclude a three-generator hypersurface presentation
whose surface actions all fail to extend. The established bound
\(3\le\mu(R)\le4\) is not resolved. The formal/all-thickening lifts
from pass 31 do not contradict the corollary: compatible nilpotent
reductions need not be an ambient algebraic \(\mathbb G_a\)-action.
Nor does this rule out every nodal plinth in every affine threefold;
the actual free-node incidence and inherited base-identification
hypotheses are essential.

## 7. Primary-source and verification boundaries

The quotient and henselian steps were checked against these exact
primary statements and proofs:

- [Stacks 06PH](https://stacks.math.columbia.edu/tag/06PH) supplies the
  algebraic-space fppf torsor for a free flat locally finitely presented
  group action. [Stacks 0DU0, Lemma 101.32.1](https://stacks.math.columbia.edu/tag/0DU0)
  makes its quotient étale when the action equivalence relation is an
  open immersion. Both hypotheses were verified in Section 3.
- [Stacks 025G](https://stacks.math.columbia.edu/tag/025G) identifies an
  étale universally injective scheme morphism as an open immersion.
  [Stacks 04GG, equivalence (8)](https://stacks.math.columbia.edu/tag/04GG)
  gives the henselian retraction, including the chosen closed point;
  its implication from henselianity was read directly.
  [Stacks 024T](https://stacks.math.columbia.edu/tag/024T) gives the
  section/open-diagonal argument, which works identically after an
  étale scheme cover of an algebraic space.
- [Stacks 03AG](https://stacks.math.columbia.edu/tag/03AG) classifies
  abelian torsors by first cohomology. The affine vanishing used in
  Section 2 follows from the fppf comparison in
  [Stacks 0DEV](https://stacks.math.columbia.edu/tag/0DEV), particularly
  the proof of Lemma 59.101.1, and affine quasi-coherent vanishing.
  [Stacks 00MC](https://stacks.math.columbia.edu/tag/00MC) supplies flat
  local completion. No formal algebraization is imported from it.

The companion [five-method exact control suite](nodal_fork_checks_pass36.py)
checks finite branch expansions, the unchanged incidence table,
translation cocycles, exact saturated graph ideals, and the positive
versus nonunit numerator separation controls. It does not verify
algebraic-space descent, unknown ambient equations, or the universal
geometric theorem. Those assertions rest on the written proof and its
stated primary inputs. Independent AI audits are not human expert
review or Lean verification. No novelty or cancellation claim is made.
