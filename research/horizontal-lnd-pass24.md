# Horizontal LNDs from the stable cylinder: an exact projection obstruction

Date: 2026-09-13. This bounded pass uses the explicit stable cylinder from
the [pass-23 homotopy](presentation-homotopy-pass23.md). It proves an
obstruction to an entire plane-moving triangular ansatz, not just to
the earlier invariant-preserving connection. In the same example it
constructs a successful horizontal LND and its stable ambient lift,
showing exactly what the failed ansatz excludes.

The universal radical-congruence case remains unresolved. None of the
statements below is a claim of novelty, general cancellation, expert
review, or Lean verification. No registry or old file was edited.

## 1. Stable setup and the exact tangent projection

Write k=\(\mathbb C\) for the ground field and reserve C for the
invariant ring. Use the authoritative homotopy notation

\[
R=\mathbb C^{[3]},\quad C=\ker D,\quad Dr=p\ne0,
\quad d\in\sqrt{pC},\quad v=1+\lambda d.
\]

Choose the explicitly constructed A,G in C[lambda] satisfying
pA+vG=1. In

\[
T=R[\lambda,t],\qquad
E=AD+G\partial_t,\qquad s=r+vt,
\]

we have E(s)=1. Thus T=(ker E)[s], and

\[
B=T/(s)=R[\lambda,w]/(vw-r),\qquad w=-t\pmod s,
\]

is canonically identified with ker E by the slice retraction. These
are the existing exact stable identities, not an assumed polynomial
presentation of B over k[lambda].

**Tangent-projection lemma.** For every k-linear derivation Y of T,
not necessarily fixing C, put

\[
K_Y=Y-Y(s)E.
\tag{1}
\]

Then K_Y(s)=0, so K_Y descends to a derivation delta_Y of B.
If Y(lambda)=1, then delta_Y(lambda)=1. Local nilpotence of Y
does not in general imply local nilpotence of delta_Y.

This is precisely the natural projection through the stable slice,
not an unrelated correction. For an invariant a in ker E,
K_Y(a)=Y(a), so delta_Y corresponds to applying Y and then the
slice retraction. For a general representative a, differentiating
the finite Dixmier expression
sum_j (-s)^j E^j(a)/j! and then setting s=0 gives
Y(a)-Y(s)E(a), the formula in (1).

There is an exact invariance under a large class of proposed repairs:
for H in T and any derivation Z of T,

\[
\delta_{Y+HE+sZ}=\delta_Y.
\tag{2}
\]

Indeed the difference of the K expressions is
s*(Z-Z(s)E), which vanishes modulo s. Thus arbitrary corrections
along the stabilizing LND, or corrections divisible by its slice,
cannot repair a failed projected derivation. This statement remains
true if the corrected ambient derivation happens to be an LND.

## 2. What keeping the old invariant plane fixed would require

There is a complete positive construction when d=pH with H in C:

\[
\delta(\lambda)=1,\qquad \delta(w)=0,\qquad
\delta|_R=HwD.
\tag{3}
\]

The relation is preserved since delta(v)=pH and delta(r)=pHw.
The coefficient Hw is delta-invariant. Hence
delta^j(a)=(Hw)^j D^j(a) for a in R, while lambda and w have
finite delta-degree. This proves local nilpotence on B directly and
constructs an actual horizontal LND, without formal integration.

For primitive D, minimal r, and nonunit p, the previously audited
[common-residue relative obstruction](relative-modification-classification-pass19.md),
Section 5, also gives the converse:

\[
\exists\delta\in\operatorname{LND}(B),\quad
\delta\lambda=1,\quad\delta|_C=0
\quad\Longleftrightarrow\quad d\in pC.
\tag{4}
\]

For necessity the slice theorem identifies every lambda-fiber with
ker delta over C. The fibers at zero and one are R and R[r/(1+d)],
so they would be isomorphic over C. The cited relative theorem,
with common residue one, forces p to divide d. Connectedness is not
needed for its common-residue version. The forward construction (3)
does not need primitivity or minimality.

Consequently a solution in the genuine radical-only region must move
the old invariant plane. The next control allows such movement and
still proves that a broad stable-cylinder projection strategy fails.

## 3. A completely polynomial test family and its stable coordinates

Take

\[
R=\mathbb C[x,y,z],\quad D=x^2\partial_y+2y\partial_z,
\quad r=y,\quad p=x^2,\quad d=x.
\tag{5}
\]

Here D is primitive, C=k[x,h] with h=x^2z-y^2, and r is a
minimal local slice. For completeness, localizing at x gives
R_x=k[x,x^{-1},h][y]. Reduction modulo x separates the even
polynomials in y from y times those polynomials, since h=-y^2.
It follows by removing a hypothetical highest x-pole that
ker D=k[x,h] and ker D^2=C+C*y. Thus the plinth is x^2C.
The reduced support is connected and d is not in pC.

In this example

\[
v=1+\lambda x,\quad G=1-\lambda x,\quad A=\lambda^2,
\quad E=\lambda^2D+G\partial_t,
\quad s=y+vt.
\]

Eliminating y from the modification gives the actual presentation

\[
B=\mathbb C[\lambda,x,w,z],\qquad y=vw.
\tag{6}
\]

The complete stable coordinates on T are

\[
W=Gy-\lambda^2x^2t,
\qquad Z=z-2\lambda^2ys+\lambda^4x^2s^2,
\quad\lambda,x,W,Z,s.
\tag{7}
\]

Both inverse directions are polynomial, with

\[
t=Gs-W,\qquad y=\lambda^2x^2s+vW,
\qquad z=Z+2\lambda^2vWs+\lambda^4x^2s^2.
\tag{8}
\]

Also E(W)=E(Z)=E(x)=E(lambda)=0 and E(s)=1. Thus in these
coordinates E is partial_s. Modulo s, W=w and Z is the physical
z of (6). All the following projection calculations therefore use
the explicit stable trivialization, not just a smoothness connection.

## 4. Every ambient LND in a plane-moving triangular ansatz fails projection

Let a,b,e,c be arbitrary polynomials with

\[
a\in\mathbb C[\lambda],\quad
b,e\in\mathbb C[\lambda,x],\quad
c\in\mathbb C[\lambda,x,y,t].
\]

Consider the ambient derivation

\[
Y=\partial_\lambda+a(\lambda)\partial_x
  +b(\lambda,x)\partial_y+e(\lambda,x)\partial_t
  +c(\lambda,x,y,t)\partial_z.
\tag{9}
\]

It is locally nilpotent by triangularity in the order lambda,x,y,t,z,
and Y(lambda)=1. This class includes every constant horizontal vector
field. It also allows nonzero movement of x and of the old invariant
h; it is not an invariant-plane-preserving ansatz.

**Proposition.** For every choice in (9), the derivation delta_Y
obtained from (1) on B is not locally nilpotent.

**Proof.** Directly

\[
Y(s)=b+ve+(x+\lambda a)t.
\]

Since w=-t modulo s and t=-w,y=vw on that quotient,

\[
\delta_Y\lambda=1,\qquad \delta_Yx=a,
\]
\[
\delta_Yw=-(x+\lambda a)(1-\lambda x)w
              +b(1-\lambda x)-e\lambda^2x^2.
\tag{10}
\]

The polynomial c does not enter this stable subring
k[lambda,x,w]. Choose a polynomial antiderivative A_0 of a and
put q=x-A_0(lambda). Then delta_Y(q)=0. Over k(q), (10) has the
affine differential form

\[
\delta_Y=\partial_\lambda+(-\gamma(\lambda)w+eta(\lambda))\partial_w,
\]
\[
\gamma=(q+A_0+\lambda a)(1-\lambda(q+A_0)).
\tag{11}
\]

The coefficient of q^2 in gamma is -lambda, so gamma is a
nonzero polynomial of positive lambda-degree over k(q). Let m
be that degree and let g be its nonzero leading coefficient. The
coefficient P_j of w in delta_Y^j(w) satisfies

\[
P_0=1,\qquad P_{j+1}=P_j'-\gamma P_j.
\tag{12}
\]

Induction gives degree(P_j)=jm and leading coefficient (-g)^j.
The derivative term has lower degree and cannot cancel the product
term. Hence P_j is nonzero for every j, so no iterate of w vanishes.
This proves the proposition. The affine term beta, and every choice
of c, are immaterial to this obstruction.

For example a=1 makes delta_Y(x)=1, so this failure persists when
the projected connection explicitly moves the old invariant plane.
Equation (2) further shows that arbitrary repairs HE+sZ leave this
entire obstruction unchanged. The false inference is therefore
precise: a triangular horizontal ambient LND, even with plane movement
and these polynomial normal corrections, need not induce a horizontal
LND on the slice quotient.

## 5. The successful lift exists, but uses excluded coupled terms

The polynomial presentation (6) has the horizontal LND
delta_*(lambda)=1 fixing x,w,z. It changes the old invariant:

\[
h=x^2z-v^2w^2,\qquad
\delta_*h=-2xvw^2\ne0.
\tag{13}
\]

Using the explicit stable coordinates (7), extend it to the ambient
coordinate partial that differentiates lambda while fixing x,W,Z,s.
In the original T-coordinates this is the following polynomial LND:

\[
\widehat Y\lambda=1,\qquad \widehat Yx=0,
\]
\[
\widehat Yy=2\lambda x^2s+xW,
\qquad \widehat Yt=-xs,
\]
\[
\widehat Yz=(4\lambda+6\lambda^2x)Ws+4\lambda^3x^2s^2.
\tag{14}
\]

It fixes s,W,Z and commutes with E. Its local nilpotence follows
from (8): the lambda-degrees of y,t,z in the stable coordinates
are at most two, one, and four. Its quotient is precisely delta_*.

The coefficients of partial_y and partial_t in (14) contain coupled
old y,t terms, so this successful derivation is outside (9). These
terms cannot all be removed by the invisible repairs in (2), since
that would contradict the proposition. The example therefore does
not obstruct existence of a horizontal LND; it demonstrates why the
specified broad descent ansatz misses one that actually exists.

## 6. Verification, inherited inputs, and the remaining quantifier

Fifty-six independent inline exact SymPy assertions passed. They
checked both stable inverse compositions, E on the stable coordinates,
the successful ambient lift and its finite generator degrees, the
projected w formula for four polynomial choices of a,b,e, and the
recurrence degrees and leading coefficients. These are scalar controls,
not test methods or a replacement for the universal recurrence proof.
The separate jet-checking agent independently reconstructed (10)-(12)
and found no gap, including the required stable-subring condition on
b,e. No new primary theorem is invoked: the general slice construction
is the authoritative pass-23 one, and (4) explicitly uses the already
audited relative obstruction. The example and all projection statements
are proved directly here.

For arbitrary primitive D with minimal Dr=p and d in sqrt(pC), the
remaining assertion is still

\[
\exists\delta\in\operatorname{LND}_{\mathbb C}(B)
\quad\text{such that}\quad\delta\lambda=1,
\]

without fixing the old invariant plane. Equivalently, in the given
stable cylinder one may seek a horizontal LND fixing s; an extension
of a successful quotient LND can also be chosen to commute with E.
Section 4 refutes a specified attempt to obtain it by projection of
a large old-coordinate triangular class. It does not refute all
ambient LNDs, all changes of stable coordinates, or all horizontal
LNDs of B. Section 5 supplies an actual lift only for the displayed
polynomial test family. A universal procedure constructing the coupled
terms without already recognizing B has not been proved.
