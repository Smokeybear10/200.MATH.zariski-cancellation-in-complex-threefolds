# A pointwise plinth criterion from peripheral cycles

Let \(0\ne D\) be a primitive locally nilpotent derivation of

\[
R=\mathbb C^{[3]},\qquad C=\ker D\cong\mathbb C^{[2]},
\qquad \pi:X=\operatorname{Spec}R\longrightarrow S=\operatorname{Spec}C.
\]

Here primitive means that the coefficients of \(D\) have no common
nonconstant factor. The pointwise implication under investigation is

\[
\pi^{-1}(p)\text{ is a reduced single }\mathbb A^1
\text{ with a nonzero translation action}
\quad\Longrightarrow\quad p\notin V(P_D),
\qquad P_D=D(R)\cap C.
\tag{1}
\]

The argument below proves (1) using the peripheral-cycle diagram in
Kaliman's proof of Proposition 3.2. The additional step is a support
calculation near the entire fiber, including every analytic branch of
the exceptional curve. It does not assume that the exceptional surface
or Kaliman's intermediate curve is normal. In particular, it does not
replace surjectivity before normalization by surjectivity after
normalization.

This is a source-dependent proof deduction, not a claim that (1) is
stated as a theorem in the source, and not a novelty or peer-review claim.

## 1. Source inputs and notation

Use the final author version of
[Kaliman, *Free C+-actions on C3 are translations*](https://www.math.miami.edu/~kaliman/library/Ka.invent.2004.c%2B.pdf).
Lemma 2.1, Lemma 2.2, Proposition 3.2, Remark 3.3, and Theorem 5.2(i)
give the following data in the present polynomial-threefold setting.

- The quotient is surjective and faithfully flat.
- There is a reduced exceptional curve \(\Gamma\subset S\), with
  \(\pi^{-1}(S\setminus\Gamma)\cong(S\setminus\Gamma)\times\mathbb A^1\).
- Writing \(E=\pi^{-1}(\Gamma)_{\mathrm{red}}\), there is a factorization
  \(E\xrightarrow{\kappa}Z\xrightarrow{\theta}\Gamma\), with \(\kappa\)
  surjective, \(\theta\) finite, and a product over a dense open curve.
- Each retained component \(Z_i\to\Gamma_i\) has degree at least two.
  The source's implication from nonbijective to nonbirational uses
  Step 1 of Proposition 3.2, as explicitly recalled in Proposition 4.2.
- Each inverse image \(E_i=\pi^{-1}(\Gamma_i)\) is an irreducible
  reduced surface.

For primitive \(D\), the retained curve is exactly \(V(P_D)\), as proved
in [the whole-component note](whole-plinth-component-pass16.md), Section 2.
That support identification uses primitivity; it is false for arbitrary
replicas of a translation.

Choose a finite set \(F\subset\Gamma\), including the point \(p\) under
consideration, so that

\[
\Gamma^*=\Gamma\setminus F,\quad
Z^*=\theta^{-1}(\Gamma^*),\quad
S^*=S\setminus F,\quad X^*=\pi^{-1}(S^*)
\]

are in the setting of the source's diagram (*). Thus \(\Gamma^*,Z^*\)
are smooth, \(E^*=\pi^{-1}(\Gamma^*)\cong Z^*\times\mathbb A^1\),
and the finite covering on these curves is unramified. Enlarge \(F\)
to include all required exceptional values. Put

\[
\widehat S=S\setminus\Gamma,\qquad
\widehat X=X\setminus E\cong\widehat S\times\mathbb A^1,
\qquad L=\pi^{-1}(F).
\]

All homology groups below are ordinary singular homology with rational
coefficients. Rational coefficients suffice for the support argument.

## 2. The exact consequence of the homology diagram

The exact sequences of the pairs \((X^*,\widehat X)\) and
\((S^*,\widehat S)\), followed by the Thom identifications, give the
commutative diagram

\[
\begin{array}{ccccc}
H_3(X^*)&\xrightarrow{\phi'}&H_1(Z^*)&\xrightarrow{\psi'}&H_2(\widehat X)\\
\downarrow&&\downarrow\theta_*&&\downarrow\cong\\
H_3(S^*)&\xrightarrow{\phi}&H_1(\Gamma^*)&\xrightarrow{\psi}&H_2(\widehat S).
\end{array}
\tag{2}
\]

The right vertical isomorphism comes from the product off \(\Gamma\).
The middle map is the ordinary \(\theta_*\): the transverse divisor
multiplicity is one because \(\pi^*\Gamma_i=E_i\) is reduced.
Consequently,

\[
\theta_*\beta\in\operatorname{im}\phi
\quad\Longrightarrow\quad
\beta\in\operatorname{im}\phi'.
\tag{3}
\]

Indeed \(\psi\theta_*\beta=0\), hence the right isomorphism and
commutativity give \(\psi'\beta=0\), and exactness gives (3).

For each \(q\in F\), let \(\gamma_{q,1},\ldots,\gamma_{q,k_q}\)
be positively oriented small loops around its analytic branches in
\(\Gamma^*\). The small three-sphere around \(q\) represents a class
\(\omega_q\in H_3(S^*)\), and

\[
\phi(\omega_q)=\sum_{j=1}^{k_q}\gamma_{q,j}.
\tag{4}
\]

This is the local Thom computation in the source's Lemma 3.1. A branch
loop here is a loop about a point of the normalization, not a loop
assigned only to an underlying singular point of \(\Gamma\).

There is also an essential localization property. Since \(X=\mathbb A^3\),

\[
H_4(X)=H_3(X)=0,
\qquad H_4(X,X^*)\xrightarrow{\sim}H_3(X^*).
\tag{5}
\]

For any sufficiently small Euclidean neighborhood \(U\) of \(L\),
excision represents these relative classes in \((U,U\setminus L)\).
Functoriality of the Thom map for open inclusions therefore gives

\[
\operatorname{im}\phi'
\subseteq
\operatorname{im}\bigl(H_1(E^*\cap U)\longrightarrow H_1(Z^*)\bigr).
\tag{6}
\]

One may take \(U\) to be a disjoint union of neighborhoods \(U_q\) of
\(\pi^{-1}(q)\), for \(q\in F\). Its summand over \(q\) maps into the
span of the peripheral loops of \(Z^*\) above \(q\). The source proves
this localization when establishing \(\operatorname{im}\phi'\subset G'\)
and again in Step 1 of Proposition 3.2. Below we refine the support of
the summand over the particular smooth fiber at \(p\).

## 3. Normalization near a reduced single-line fiber

Assume that \(Y=\pi^{-1}(p)\) is a reduced single \(\mathbb A^1\).
Faithful flatness and smoothness of this scheme-theoretic fiber imply
that \(\pi\) is smooth at every point of \(Y\). This is the pointwise
flat-plus-smooth-fiber criterion, not a properness assertion; see
[Stacks, Lemma 29.35.14](https://stacks.math.columbia.edu/tag/01V9).

Because \(\theta^{-1}(p)\) is finite, \(\kappa(Y)\) is one point:
it is connected, and surjectivity of \(\kappa\) forces

\[
\theta^{-1}(p)=\{z\}.
\tag{7}
\]

The point \(z\) need not be unibranch. Let \(\Gamma_j\) denote an
analytic branch at \(p\), equivalently a point \(p_j\) of the
normalization of the appropriate component \(\Gamma_i\). Work on
an open neighborhood of \(Y\) where \(\pi\) is smooth. On this open,
the normalization of \(E_i\) is its base change by
\(\Gamma_i^\nu\to\Gamma_i\). This follows from
[normalization commuting with smooth base change](https://stacks.math.columbia.edu/tag/03GV).
In particular its fiber over \(p_j\) is one copy \(Y_j\cong Y\), not
several copies associated to branches of \(Z_i\).

The dominant map \(E_i^\nu\to Z_i\) factors through \(Z_i^\nu\).
The finite map

\[
\theta_i^\nu:Z_i^\nu\longrightarrow\Gamma_i^\nu
\]

has degree \(d_i\ge2\). The connected curve \(Y_j\) maps to exactly
one point \(\zeta_j\in(\theta_i^\nu)^{-1}(p_j)\). Call this a
reached branch. The map \(\theta_i^\nu\) is unramified at \(\zeta_j\).
To check this, take local parameters \(u,v\) at \(p_j,\zeta_j\).
If its ramification index were \(e>1\), then

\[
(\theta_i^\nu)^*u=\varepsilon v^e
\]

for a unit \(\varepsilon\). Pullback to \(E_i^\nu\) would make the
differential of \(u\) zero along \(Y_j\), contrary to smoothness of
the map to \(\Gamma_i^\nu\) there. Thus

\[
e(\zeta_j/p_j)=1.
\tag{8}
\]

A finite map between smooth curves has constant degree, counting
ramification indices. Since \(d_i\ge2\), above every such \(p_j\)
there is at least one further normalized point. None is reached
by \(Y_j\). At this stage the escaping-branch possibility is real:
(7) does not rule it out, because several normalized points can
lie over the same singular point \(z\).

## 4. Refining the support in a neighborhood of the whole fiber

The escaping branches cannot contribute cycles to the \(p\)-summand
of (6). Here is the required whole-fiber justification.

Take disjoint small disk neighborhoods in the normalized curves
\(Z_i^\nu\) around the finitely many normalized points above \(p\).
Only the disk about \(\zeta_j\) is selected for each base branch \(j\).
In \(E^\nu\), the inverse image of the union of selected disks is
an open set \(O\) containing the entire inverse image of \(Y\).
There are no additional normalized copies over \(Y\), by the smooth
base-change calculation in Section 3.

Normalization \(\nu_E:E^\nu\to E\) is finite, hence proper in the
Euclidean topology. Thus

\[
E\setminus\nu_E(E^\nu\setminus O)
\]

is an open neighborhood of \(Y\) whose inverse image lies in \(O\).
Choose \(U_p\subset X\) so that its intersection with \(E\) is contained
in this neighborhood, and shrink it inside the inverse image of a
small neighborhood of \(p\) in \(S\). After deleting \(Y\), the images
in \(Z^*\) lie only in punctured disks about reached branches.

Consequently, if \(V_p^{\mathrm{reach}}\subset H_1(Z^*)\) denotes
the span of their peripheral loops, (6) can be refined to

\[
\operatorname{im}\phi'
\subseteq V_p^{\mathrm{reach}}
+\sum_{q\in F\setminus\{p\}}V_q,
\tag{9}
\]

where \(V_q\) is the span of all peripheral loops above \(q\).
This uses neither compactness of \(Y\) nor properness of \(\pi\).
Properness is used only for the finite normalization map when
choosing a neighborhood of the entire \(Y\).

All these peripheral loops are linearly independent in \(H_1(Z^*)\).
Indeed the smooth affine curve \(Z^*\) is a disjoint union of compact
Riemann surfaces with finitely many punctures. In each component,
the only relation among all puncture loops is their total sum.
There is at least one puncture at infinity, not among the points
over \(F\), because \(Z_i\) is affine and positive dimensional.
Hence the loops at the finite points over \(F\) form an independent
set. Singularities of \(Z\) do not add a relation here: they have
been deleted, and distinct normalization branches are distinct
punctures of \(Z^*\).

## 5. The contradiction

Choose one unreached normalized point \(\zeta_0\) above a branch
of \(\Gamma\) at \(p\), as supplied by Section 3. For every other
base branch \(j\), choose any normalized point above it. Let the
chosen points have ramification indices \(e_j>0\), and let
\(\beta_j\in H_1(Z^*)\) be their positively oriented peripheral
loops. Choose the unreached point for its branch, and form

\[
\beta=\sum_j e_j^{-1}\beta_j.
\tag{10}
\]

The finite covering sends \(\beta_j\) to \(e_j\gamma_{p,j}\), so

\[
\theta_*\beta=\sum_j\gamma_{p,j}=\phi(\omega_p).
\]

Equation (3) gives \(\beta\in\operatorname{im}\phi'\). But (10)
has a nonzero coefficient at the unreached puncture \(\zeta_0\),
whereas every element of the right side of (9) has zero coefficient
there. Peripheral-loop independence gives a contradiction.

Therefore \(p\notin\Gamma=V(P_D)\), proving (1).

The argument uses the reduced scheme-theoretic fiber hypothesis.
A set-theoretic line carrying nilpotent thickening does not give
the smoothness used in (8) or the normalized single-copy assertion.
The stated translation hypothesis is retained, although the cycle
argument after selecting the primitive retained curve only uses the
reduced single-line fiber.

## 6. Why the earlier nodal control is not a contradiction

The elementary map

\[
Y_0=\operatorname{Spec}\mathbb C[t,(t+1)^{-1},y],\qquad
u=t^2,\qquad v=t(t^2-1)
\]

factors surjectively through the nodal curve

\[
Z_0=V(v^2-u(u-1)^2)\longrightarrow\mathbb A^1_u.
\]

The finite map has degree two, but its fiber over \(u=1\) is one
singular point. The fiber of \(Y_0\to\mathbb A^1_u\) over (1)
is the reduced line \(t=1\), with free \(\partial_y\)-translation;
the normalization branch \(t=-1\) has escaped. This refutes a
proof based only on finite \(\theta\), surjective \(\kappa\), and
smoothness along a single fiber.

It does not supply the quotient geometry (2). The invariant ring
of \(Y_0\) for \(\partial_y\) is
\(\mathbb C[t,(t+1)^{-1}]\), not \(\mathbb C[u]\), and the surface
map is not the quotient of an action on polynomial three-space.
The new obstruction to realizing this configuration in the actual
setting is exactly the combination of (3), (6), and (9).

## 7. An independent normalization-ring observation

The invariant-ring normalization question can be separated from the
cycle proof. Let \(T\) be an affine domain with a nonzero LND
\(\partial\), let \(\overline T\) be its finite equivariant normalization,
and assume \(C_0=\ker(\partial|_T)\) is Noetherian. Then

\[
\overline C_0=\ker(\partial|_{\overline T})
\quad\text{is finite over }C_0.
\tag{11}
\]

For a direct proof, the conductor

\[
I=\{a\in T:a\overline T\subset T\}
\]

is nonzero and stable under \(\partial\). Stability follows by
differentiating \(ab\in T\), for \(a\in I,b\in\overline T\).
The last nonzero derivative of a nonzero element of \(I\) gives
\(0\ne c\in I\cap C_0\). Thus

\[
c\overline C_0\subset C_0,
\qquad\overline C_0\subset c^{-1}C_0.
\]

The latter is a finitely generated \(C_0\)-module, and its submodule
\(\overline C_0\) is finitely generated because \(C_0\) is Noetherian.
No reductivity of the additive group is used in this conductor argument.

Equation (11) alone does not identify the full invariant ring of an
exceptional surface with the ring of Kaliman's intermediate curve,
or prove finiteness over the exceptional base curve. The proof of
(1) above does not require either identification.

## 8. Scope

The deduction establishes the requested pointwise implication for
primitive additive-group quotients of \(\mathbb A^3\), using the exact
global product and homology framework above. It does not assert this
criterion for arbitrary affine surfaces with additive-group actions,
or infer it from an abstract finite curve factorization. No numerical
or finite symbolic test proves the topological argument. Further uses
of (1), such as the separate DVR-to-affine-slice deduction, should cite
the complete hypotheses and retain their own algebraic checks.
