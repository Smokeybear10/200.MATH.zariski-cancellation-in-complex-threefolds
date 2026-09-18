# Global recognition gates after the local cyclic-conic theorem

The local theorem114 does not yet meet a global affine-three-space
recognition theorem. There are applicable conditional endpoints, but each
requires an additional global input. In particular, equality of the first
two derivative images and exact cyclic conics near every fixed fiber do
not make the given additive action free.

This is a bounded source and applicability audit, not a new recognition
theorem. The Russell-cubic boundary and the univariate-denominator
criterion already occur in [source79](quadratic-relative-modification-source-pass79.md).
The additional comparison here is with the exact degree filtration now
obtained in114, including a direct calculation of that filtration on the
Russell cubic. No example below is assigned the actual original frame or
a polynomial cylinder.

Forward status within115: the independent
[global patching theorem](quadratic-global-conic-patching-pass115.md)
now proves a global cyclic conic over S in the supplied frame, using
the additional free-fiber theorem. This removes the local-to-global
generation gap. It does not show that its coefficient P depends on
one polynomial coordinate of S or meet either other recognition gate
below. The Russell comparison already has global cyclic generation.

## 1. The established local conclusion and three distinct global targets

Retain the actual supplied quadratic frame. The
[fixed-fiber conclusion114](whole-double-universal-frontier-pass114.md)
gives, at every closed fiber containing an N-fixed point,
\[
\begin{gathered}
R=S_{\mathfrak m},\quad S=\mathbb C[s_1,s_2],\qquad
A_R=R[U,V]/(V^2-2pU+\eta),\\
NU=V,\quad NV=p,\quad p,\eta\in\mathfrak m,\quad p\ne0,\qquad
A_R/\mathfrak mA_R=\mathbb C[U,V]/(V^2),\quad I_1=I_2=pR.
\end{gathered}
\tag{1}
\]
Here the cylinder makes X=Spec A smooth, factorial and contractible.
The quotient S is the actual full kernel and is a polynomial plane.
Formula (1) concerns localizations of that quotient, not an identified
global polynomial coordinate system on A or on S.

| Exact sufficient global input | Recognition theorem | What (1) does not supply |
| --- | --- | --- |
| A global free additive action on X, with plane quotient | Kaliman--Saveliev, Corollary 2.8(1) | A unit image ideal for a global LND |
| A regular function f on X, trivial affine-plane family over a nonempty open of the line, all closed fibers reduced irreducible UFDs | Miyanishi's characterization, in the primary restatement below | Such a global f and the condition on every exceptional surface fiber |
| A global presentation with denominator depending on one polynomial coordinate, plus the required unstabilized invariant condition | Ghosh--Gupta--Pal, Theorem 4.8 | That presentation and ML(A)=C or DK(A)=A |

These are separate targets. A parameter in one localized conic is not
automatically a global function with the second row's properties. A
single analytic prime supporting a localized first image is not
automatically a coordinate of the invariant plane.

## 2. The free-action endpoint really applies to unknown threefolds

Kaliman--Saveliev prove that a free additive action on a smooth
contractible affine complex threefold gives an equivariant product with
its quotient surface. Thus a plane quotient gives affine three-space.
The hypothesis is not that X is already affine three-space. Their
Theorem 2.7 supplies smoothness of the quotient before Corollary 2.8(1).
[Primary paper, Theorem 2.7 and Corollary 2.8](https://www.math.miami.edu/~kaliman/library/KaSa.michigan.2004.quotient.pdf).

For the retained N, its plane quotient is already known, so proving that
N is globally fixed-point-free would be enough. For another proposed
action, its quotient must be justified as well, for example by the
retained cylinder-to-quotient argument. A local slice on an open set does
not supply a global free action on X. Multiplying a derivation by a
nonconstant invariant to clear denominators generally creates zeros.

The underlying author-hosted Kaliman paper states the product result as
Theorem 5.2(ii), under its earlier quotient hypotheses and smoothness of
the quotient. Proposition 5.1 explains the algebraic line-bundle/product
step from an analytic affine-line bundle. Its hypotheses do not follow
from a nonreduced fiber in (1).
[Primary paper, Proposition 5.1 and Theorem 5.2](https://www.math.miami.edu/~kaliman/library/Ka.invent.2004.c%2B.pdf).
This avoids misapplying only the paper's special theorem about actions
on affine three-space.

## 3. Two recognition theorems with explicit missing fiber conditions

Kaliman--Zaidenberg state Miyanishi's characterization for smooth
contractible affine complex threefolds: a regular function which is a
trivial affine-plane family over a nonempty Zariski open recognizes
affine three-space when every closed fiber is reduced, irreducible and
factorial. They also state the variant with general affine-plane fibers
and only isolated singularities in every fiber. The extra exceptional
fiber condition is essential, not a consequence of smoothness of the
total threefold.
[Primary restatement, introduction, pp. 1649--1650](https://www.numdam.org/item/10.5802/aif.1803.pdf).

For a different algebra A0, suppose an actual global presentation is
given over a characteristic-zero field:
\[
A_0=k[X,Y,Z,T]/\bigl(\alpha(X)Y-F(X,Z,T)\bigr),
\qquad \deg\alpha\ge1,\quad A_0\text{ a domain}.
\tag{2}
\]
Ghosh--Gupta--Pal, Theorem 4.8, makes A0 polynomial precisely when all
root specializations F(lambda,Z,T) are plane coordinates; its equivalent
stable-polynomial clauses also require ML(A0)=k or DK(A0)=A0. It is not a
cancellation theorem for (2) from stable polynomiality alone. Its short
proof retains those invariant assumptions through Corollary 4.2.
[Primary preprint v2, Theorem 4.8](https://arxiv.org/pdf/2403.17397v2).
The degree condition in (2) is reconciled against the
[authoritative arXiv HTML, Question 4 and Section 3 setup](https://arxiv.org/html/2403.17397v2),
which states degree at least one. The PDF text extraction lost the
equality bar and displayed a strict inequality. Linear denominators
are included; the ML/DK and global-presentation conditions remain.

For our actual A, the polynomial cylinder supplies the stable condition
but not either unstabilized invariant condition. The global conic
patching115 does not put its denominator in one global base coordinate,
as required by (2). No change of notation removes these gaps.

The retraction and geometric-integrality alternatives previously checked
in [retraction104](cyclic-conic-retraction-obstruction-pass104.md) are
unavailable at an actual fixed double: the local conic has no R-section,
and its relevant generic divisor has a genuine quadratic constant field.
That is a proved failure of those relative hypotheses, not merely a
failure to locate a section.

## 4. The Russell cubic has the same exact cyclic filtration

Let C_R denote the following algebra, independently of the actual A:
\[
\begin{gathered}
C_R=\mathbb C[x,y,z,t]/(x+x^2y+z^2+t^3),\quad S_R=\mathbb C[x,t],\\
N_R=x^2\partial_z-2z\partial_y,\quad U=-y/2,\quad r=z,\\
C_R=S_R[U,r]/(r^2-2x^2U+x+t^3),\quad
N_RU=r,\quad N_Rr=x^2.
\end{gathered}
\tag{3}
\]
The equation is primitive and linear in y over C[x,z,t], hence
irreducible. This hypersurface is smooth: simultaneous vanishing of its four partial
derivatives would force x=z=t=0, where its x-partial is 1. The element x
is prime because C_R/xC_R is the domain
C[y,z,t]/(z squared+t cubed). Its x-localization is
C[x,x inverse,t,z], so Nagata's prime-localization criterion proves
factoriality, as already checked in source79.

The displayed derivation is triangular and locally nilpotent. It is
primitive because x is prime and does not divide z. Inverting x gives
its kernel S_R[1/x]. If F(x,t)/x^d belongs to C_R and d is positive,
reduction modulo x forces F(0,t)=0: C[t] embeds in C_R/xC_R. Removing
denominator powers proves ker N_R=S_R. The monic quadratic in r makes
C_R free over S_R[U], hence faithfully flat over S_R.

Put K=Frac S_R. The monic presentation gives a unique finite S_R-linear
expansion in U^j and rU^j. In K[r], their degrees are respectively 2j
and 2j+1, with nonzero leading coefficients. A finite expansion cannot
cancel its highest degree. Since N_R=x squared partial_r, it follows
directly, for every n, that
\[
\begin{gathered}
\ker N_R^{n+1}
=\bigoplus_{2j\le n}S_R U^j
 \ \oplus\ \bigoplus_{2j+1\le n}S_R rU^j,\\
N_R^n(\ker N_R^{n+1})=x^{2\lceil n/2\rceil}S_R\quad(n\ge1),
\qquad I_1=I_2=x^2S_R.
\end{gathered}
\tag{4}
\]
Indeed the unique degree-n basis element has leading coefficient
(2x squared)^(-floor(n/2)); multiplying by n! x^(2n) gives the stated
ideal, since its remaining scalar is a nonzero complex number.
Thus even global cyclic generation and equality of these image ideals
are compatible with this boundary, not just an isolated formal conic.

At the origin of Spec S_R, the fiber and the conic differentials are
\[
C_R/(x,t)C_R=\mathbb C[U,r]/(r^2),\qquad
p=x^2,\quad\eta=x+t^3,\quad dp=0,\quad d\eta=dx.
\tag{5}
\]
The fixed-point ideal is (x squared,z); its radical in C_R is (x,z,t),
so the reduced fixed locus is the y-line. At the generic divisor x=0,
the whole divisor ring is C(t)(sqrt(-t cubed))[U], with constant-field
degree two because -t cubed is not a square in C(t). At every other
prime divisor of S_R, x is a unit and the model is a polynomial line.
Its divisor constant degrees are therefore exactly one or two.

The smooth contractible non-affine-three-space status of this threefold
is recorded in the primary Kaliman--Zaidenberg discussion cited above.
More precisely, ML(C_R)=C[x] is stated and attributed to Makar-Limanov's
original computation in Dubouloz--Moser-Jauslin--Poloni, Section 2.
This is a result about all LNDs, not a consequence of calculating only
ker N_R here.
[Primary research statement](https://arxiv.org/pdf/0903.4278),
[original 1996 paper record](https://link.springer.com/article/10.1007/BF02937314).

For the global function x, all nonzero fibers are affine planes, but
the zero fiber is the cuspidal cylinder C[y,z,t]/(z squared+t cubed).
It is nonnormal and has a singular line, so it fails both exceptional
surface-fiber tests in Section 3. Its action N_R is not free. In (2),
the specialization z squared+t cubed is not a plane coordinate: its
zero fiber is singular. These are exact missing gates on this model.

No assertion here identifies C_R[w] with a polynomial four-ring.
The older source79 records a dated primary statement of the unresolved
cylinder question; this audit does not claim an exhaustive current
status search. Nor is an original quadratic E-frame constructed on
this model. It is a boundary to recognition from the listed intrinsic
conic data, not a counterexample to the full supplied-frame problem.

## 5. Exact reading scope and next usable target

Retained source79, modification19, free-endpoint90 and retraction104
were checked before the selected primary reads. The withdrawn
arXiv:1502.01849v2 is not used. This note does not claim that these are
all recognition theorems in the literature.

Fresh primary reads covered the complete displayed statements and
proofs of Kaliman--Saveliev Theorem 2.7 and Corollary 2.8, and Kaliman
Proposition 5.1 and Theorem 5.2 with its displayed deduction. Their deeper
topological dependencies were not reconstructed. Miyanishi's theorem
was read in the cited primary research restatement, not in its original
proof. For Ghosh--Gupta--Pal, the complete Theorem 4.8 and short proof,
Corollary 4.2 and proof, and the displayed proofs of Lemmas 4.4--4.5
were read; the longer invoked Theorem 4.1 was not fully audited afresh.
After Root identified the extraction discrepancy, the complete HTML
setup and Theorem 4.8 statement and displayed proof were read to check
the inequality. The corrected degree condition includes degree one;
no counterexample or cylinder-status conclusion is inferred from this
correction.

For the Russell cubic, the cited primary statements of contractibility,
non-isomorphism and the ML value were read. Only the publisher record
and abstract of Makar-Limanov's original paper were accessible here;
no fresh reconstruction of that original ML proof is claimed. The
algebraic calculations (3)--(5) are supplied above. No numerical method
was added or executed, and all files through114 remain unchanged.

An actionable bridge must now supply genuinely global information,
such as a free action on the whole actual X, the required affine-plane
surface fibration, or the global presentation and intrinsic invariant
condition in Section 3. Local cyclic generation alone supplies none of
those missing hypotheses. The polynomial cylinder and the original
frame remain essential inputs to any further recognition argument.
