# Transitive cylinder symmetry need not descend through the chosen slice

Date: 2026-09-13.

This pass gives a precise negative control for a proposed symmetry-transfer
step. It does not settle cancellation or supply the missing finite-closure
frame. The example is classical Danielewski geometry, with the inherited
construction credited below, not a novelty claim.

The false implication is:

> If an affine cylinder has a transitive finite-dimensional algebraic group
> action, then its distinguished cylinder translation has a transitive
> algebraic normalizer, or its base is algebraically homogeneous.

The failure already occurs for a smooth affine surface times one affine
line. It even gives a flexible cylinder whose base is not flexible. The
example is not contractible and its cylinder is not an affine space, so it
does not refute a transfer theorem with the full hypothesis A[s]=C^[4].

## 1. What a centralizer really contains

Let A be a finitely generated complex domain, B=A[s], and delta=partial_s.
For an algebra automorphism phi of B,

\[
\phi\delta=\delta\phi
\quad\Longleftrightarrow\quad
\phi|_A=\sigma\in\operatorname{Aut}(A),\qquad
\phi(s)=s+h,\quad h\in A.
\tag{1}
\]

Indeed commuting with delta preserves its kernel A, and
delta(phi(s))=1 determines the displayed form. Conversely these formulas
define an automorphism, with inverse obtained from sigma^(-1) and -h.
Consequently the centralizer is the semidirect product of Aut(A) and the
additive group of A. Its large additive subgroup h partial_s consists
entirely of vertical fields and gives no tangent directions on Spec(A).

Likewise a derivation commuting with delta is uniquely

\[
\Theta=D+h\partial_s,
\qquad D\in\operatorname{Der}_{\mathbb C}(A),\quad h\in A.
\tag{2}
\]

It is locally nilpotent if and only if D is locally nilpotent. Necessity
is restriction to A. For sufficiency, Theta is locally nilpotent on every
algebra generator of A, while Theta^j(s)=D^(j-1)(h) for j>=1 eventually
vanishes. Local nilpotence on finitely many algebra generators implies
local nilpotence on B.

Thus producing a useful centralizing LND is not a way to bypass the
intrinsic LND problem: its horizontal component is exactly an intrinsic
LND. In particular, the always available centralizer subgroup A_add is
not evidence of a finite-dimensional transitive quotient action.

There is a related statement requiring no choice of generator for the
additive group. Put H=exp(C delta). Every automorphism normalizing H
preserves B^H=A and therefore descends to an automorphism of Spec(A).
If Z is a nonempty proper Aut(A)-invariant closed subset, then
Z times A1 is invariant under the entire normalizer of H. No subgroup
of that normalizer can act transitively on Spec(B).

## 2. An exact one-cylinder stable example

For an integer n>=1 set

\[
X_n=\{(x,y,z)\in\mathbb A^3:x^n z=y^2-1\},
\qquad Y_n=X_n\times\mathbb A^1_s.
\tag{3}
\]

These surfaces are smooth: if x is nonzero the partial derivative in z
is nonzero; if x=0 the equation forces y=+1 or -1 and the partial
derivative in y is nonzero. The two lines

\[
L_+=\{x=0,y=1\},\qquad L_-=\{x=0,y=-1\}
\tag{4}
\]

form the unique reducible fiber of x:X_n -> A1. All nonzero fibers
are affine lines.

### 2.1. The cylinder isomorphism is an actual algebraic isomorphism

Let Z be the affine line with two origins. For epsilon in {+1,-1},
the open set U_epsilon=X_n minus L_(-epsilon) has coordinates

\[
u_\epsilon=\frac{y-\epsilon}{x^n},\qquad
y=\epsilon+x^n u_\epsilon,\qquad
z=2\epsilon u_\epsilon+x^n u_\epsilon^2.
\tag{5}
\]

The apparently rational u_epsilon is regular on this open set. Where
y+epsilon is invertible it equals z/(y+epsilon), and the remaining
points of U_epsilon have x invertible. These two formulas agree.
They exhibit U_epsilon as A2, not just birationally as A2. On the overlap,

\[
u_-=u_++2x^{-n}.
\tag{6}
\]

Therefore X_n -> Z is a Ga torsor, with translations in the u_epsilon
coordinates. This is the classical doubled-line presentation, as read
in Dubouloz's introduction.[^dfs]

Now form W=X_n times_Z X_1. Each projection is the pullback of a
Ga torsor. A Ga torsor over an affine scheme is trivial, by vanishing
of H^1 of its structure sheaf. Since both X_n and X_1 are affine,

\[
X_n\times\mathbb A^1\simeq W\simeq X_1\times\mathbb A^1.
\tag{7}
\]

This is Danielewski's fiber-product argument, explicitly recorded in
Moser-Jauslin and Poloni, Section 2.2. Their Theorem 4.0.1 and Section
5.1 also supply explicit cylinder isomorphisms. No formal neighborhood
or stable equivalence with an unspecified number of variables is used
in (7).[^cylinders]

### 2.2. A finite-dimensional algebraic group is transitive upstairs

Identify X_1 with the following matrix variety:

\[
(x,y,z)\longmapsto
\begin{pmatrix}y&x\\-z&-y\end{pmatrix},
\qquad \operatorname{tr}=0,\quad\det=-1.
\tag{8}
\]

Each matrix has the distinct eigenvalues +1 and -1. It is conjugate to
diag(1,-1); a GL2 conjugating matrix can be multiplied by a scalar to
have determinant one over C. Thus SL2 acts transitively on X_1 by
conjugation. In particular SL2 times Ga acts algebraically and
transitively on X_1 times A1. Transporting this action through (7)
gives a transitive finite-dimensional algebraic group action on Y_n.

This also proves flexibility of Y_n in the usual tangent-spanning
sense. The Lie algebra of SL2 is spanned by nilpotent matrices, whose
one-parameter subgroups are additive, and the extra Ga supplies the
cylinder direction. At each point the orbit differential is
surjective. Hence velocities of additive subgroup actions span the
whole tangent space. No assertion that the original coordinates
exhibit these transported subgroups is needed.

### 2.3. The base and the chosen-translation normalizer are not transitive

For n>=2, Dubouloz and Poloni's Theorem 3.10 describes every
automorphism of X_n by generators all preserving the divisor x=0.
The extra interchange of x and z in that theorem occurs only at n=1.
Equivalently, the unique A1-fibration theorem quoted in their
introduction forces preservation of its unique reducible fiber.[^aut]
It follows that

\[
L_+\cup L_-\subset X_n
\tag{9}
\]

is a nonempty proper closed subset preserved by the full automorphism
group, not merely by a selected LND. Consequently X_n admits no
transitive automorphism group action. It is not flexible either: at
a point of either line all additive orbit directions are tangent to
that line, a proper subspace of the surface tangent space.

Let delta=partial_s on Y_n and H=exp(C delta). It is a sliced,
free, proper additive action with quotient X_n. Every element of
N_Aut(Y_n)(H) descends to Aut(X_n), so the entire normalizer preserves

\[
(L_+\cup L_-)\times\mathbb A^1_s.
\tag{10}
\]

In particular there is no transitive algebraic subgroup of this
normalizer, and none of the centralizer. This conclusion is fully
compatible with the transitive SL2 times Ga subgroup constructed in
Section 2.2: that group cannot normalize the distinguished H.

It is not asserted that H fails to lie in every transitive algebraic
group. Containment and normalization are different hypotheses. The
countercontrol concerns descent through the chosen quotient, not
the separate containment condition of the pass-29 Levi bridge.

## 3. Exact limitation and consequence for the research route

The example cannot be smuggled into the affine-space cancellation
problem. Its two opens U_+,U_- are contractible, and their intersection
is C* times C. The Mayer-Vietoris sequence gives

\[
H_2(X_n,\mathbb Z)\simeq H_1(\mathbb C^*\times\mathbb C,\mathbb Z)
\simeq\mathbb Z.
\tag{11}
\]

Thus neither X_n nor Y_n is contractible, whereas A[s]=C^[4] makes
Spec(A) contractible by the cylinder deformation retraction.
In particular Y_n is not A3. The smooth affine stable example
disproves a general symmetry-transfer principle, not its still
unproved specialization to polynomial cylinders over threefolds.

For the actual target, asking for a transitive finite-dimensional
subgroup of the centralizer merely imposes a strong intrinsic group
action on A. Such an action has not been extracted from the stable
cylinder. The elementary description (1) does not produce it, and
stable flexibility alone cannot justify the extraction in general,
even with only one added variable and with finite-dimensional
homogeneity available upstairs.

The concrete remaining hypothesis is compatibility with the chosen
quotient: one needs intrinsic directions, or an action containing the
chosen translation to which the pass-29 theorem applies. Moving a
point upstairs by an arbitrary cylinder symmetry does not establish
either. The older criterion of an intrinsic free Ga action already
implies A=C^[3] under the stable-cylinder assumptions; this note does
not enlarge that known regime or claim a new positive recognition
theorem. The general existence quantifier remains open.

## 4. Source and verification boundary

The finite-dimensional homogeneous-cylinder control above is an
elementary consequence of established Danielewski isomorphisms and
automorphism descriptions. It is not a new cancellation example.
The primary statements actually read for this pass were the
doubled-line construction in Dubouloz's introduction; Moser-Jauslin
and Poloni Section 2.2 and Theorem 4.0.1; and Dubouloz and Poloni
Theorem 3.10, including its n=1 interchange exception.

An independent algebraic audit by jet_checker17 reconstructed the
torsor pullback, the SL2 orbit identification, and normalizer descent;
its use of the all-automorphisms assertion was explicitly conditional
on the primary statement checked here. No numerical computation or
new unittest method is claimed. No novelty inference is made from
the bounded literature search.

[^dfs]: Adrien Dubouloz, [*Danielewski-Fieseler surfaces*, introduction](https://arxiv.org/pdf/math/0401225), arXiv v3, PDF p. 1; published in *Transformation Groups* 10 (2005), 139-162. The displayed source convention has the opposite sign of the nonzero quadratic constant, immaterial over C; equations (5)-(6) verify the convention used here directly.

[^cylinders]: Lucy Moser-Jauslin and Pierre-Marie Poloni, [*Isomorphisms between cylinders over Danielewski surfaces*, Section 2.2, Theorem 4.0.1 and Section 5.1](https://arxiv.org/pdf/2002.12202), arXiv v1, printed pp. 3 and 8-9. The fiber-product construction is credited there to Danielewski. This source was also used for cylinder comparison in earlier passes; it is not newly discovered prior work.

[^aut]: Adrien Dubouloz and Pierre-Marie Poloni, [*On a class of Danielewski surfaces in affine 3-space*, Theorem 3.10](https://arxiv.org/pdf/math/0602549), arXiv v2, PDF pp. 11-12; *Journal of Algebra* 321 (2009), 1797-1812, DOI [10.1016/j.jalgebra.2008.12.009](https://doi.org/10.1016/j.jalgebra.2008.12.009). Its introduction credits the earlier unique-fibration result for x^n z=P(y), n>=2, to Makar-Limanov. The full theorem, rather than absence of other listed actions, supports (9).
