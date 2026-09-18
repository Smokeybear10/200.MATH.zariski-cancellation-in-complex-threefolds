# Structural reductions for complex threefold cancellation

The unrestricted implication
\[
X\times_{\mathbb C}\mathbb A^1\cong\mathbb A^4
\quad\Longrightarrow\quad X\cong\mathbb A^3
\tag{1}
\]
is not proved here. The results below apply to an arbitrary putative
counterexample, rather than only to a selected polynomial family.

Every nonzero intrinsic additive-group action has affine-plane quotient,
and that quotient map is surjective and faithfully flat. A single free
intrinsic action would settle (1). Independently, a low-complexity ambient
coordinate frame forces cancellation. Explicit controls show why neither
a polynomial quotient nor simplifying leading vector fields supplies
the missing global step.

These are source-dependent mathematical deductions and exact algebraic
controls. They are not a formally verified solution, an established
novelty claim, or human peer review. Throughout, the field is
\(\mathbb C\). The dimension-three interpretation corrects the dimensional
mismatch in the original conjecture; it has not been confirmed by its
author.

## 1. Algebraic formulation and the remaining task

Write
\[
B=K[s]\cong\mathbb C^{[4]},\qquad
E=\partial_s,\qquad X=\operatorname{Spec}K.
\tag{2}
\]
The notation \(k^{[n]}\) means a polynomial algebra in \(n\) independent
variables. The slice equation \(E(s)=1\) expresses the product
decomposition, but does not say that \(s\) belongs to an ambient
polynomial coordinate system. Establishing polynomiality of \(K\)
would make such an adapted coordinate system available.

A derivation \(d\) is locally nilpotent if every polynomial is killed
by some iterate of \(d\). In characteristic zero its finite exponential
defines an algebraic action of the additive group \(\mathbb G_a\).
An intrinsic action means an action on \(X\), or equivalently an LND
of \(K\), rather than an arbitrary action on the cylinder \(B\).

The product in (2) implies that \(X\) is smooth and contractible.
Smoothness descends across a polynomial extension; topologically,
\(X\) is a deformation retract of \(X\times\mathbb C\).
The ring \(K\) is factorial, has only scalar units, and has dimension
three. None of these properties individually identifies it with a
polynomial ring.

There is at least one nonzero intrinsic LND. Indeed, the one-cylinder
rigidity theorem says that if an affine domain \(A\) is rigid, then
every LND on \(A[t]\) is vertical and
\(\operatorname{ML}(A[t])=A\). Applied to (2), rigidity would contradict
\(\operatorname{ML}(\mathbb C^{[4]})=\mathbb C\).[^1]
This guarantees an action, not a free action.

## 2. Every intrinsic quotient is an affine plane

**Proposition.** If (2) holds and \(0\ne d\in\operatorname{LND}(K)\),
then
\[
A:=\ker d\cong\mathbb C^{[2]}.
\tag{3}
\]
The quotient \(X\to\operatorname{Spec}A\) is surjective and faithfully
flat, with nonempty purely one-dimensional fibers.

The primary geometric input is Kaliman and Saveliev's theorem on
additive actions on smooth contractible affine threefolds.
Their Lemma 2.1 gives nonempty curve fibers. Corollary 2.8(2)
identifies the quotient as an affine plane when the threefold is
dominated by a product of a curve and an affine plane.[^2]

Here the domination hypothesis follows directly from the cylinder.
Transporting the product projection gives a smooth surjective map
\[
P:\mathbb A^4\longrightarrow X.
\]
At any point \(v\), choose a three-dimensional linear subspace
complementary to the one-dimensional kernel of \(dP_v\).
Its affine translate \(L\) through \(v\) is \(\mathbb A^3\), and
\(P|_L\) has full differential rank at \(v\).
Thus \(P|_L\) is dominant. Since
\(\mathbb A^3=\mathbb A^1\times\mathbb A^2\), the cited corollary
applies. The argument works for every nonzero \(d\), proving (3).

No claim that \(P|_L\) is an isomorphism, birational, or surjective
is needed. Nor is \(L\) a presumed algebraic section of \(P\).
Full differential rank is used only to prove dominance.

For flatness, write \(A=\mathbb C[a,b]\). Over a closed point
\((\alpha,\beta)\), the nonempty fiber has dimension one and is
defined by two equations in the regular threefold \(X\).
Every minimal component has codimension two: codimension three
is excluded by the height theorem, and codimension one would
contradict the curve-fiber statement. Locally the equations form
a regular sequence.

At every closed point of this fiber, the local source is
Cohen--Macaulay of dimension three, the local base is regular of
dimension two, and the fiber local ring has dimension one.
Miracle flatness therefore applies.[^3] The flat locus is open
and contains every closed point, so it is all of \(X\).
Surjectivity makes the map faithfully flat.

This settles the quotient-surface identification in the intrinsic
action approach. It does not classify the exceptional fibers.

## 3. The free-action criterion

Kaliman and Saveliev's Corollary 2.8 also states that a free action
on a smooth contractible affine threefold is a translation on
a product with its quotient.[^2] Combining this with (3) gives
\[
d\text{ has no fixed points}
\quad\Longrightarrow\quad K=A[t]\cong\mathbb C^{[3]}.
\tag{4}
\]

Over \(\mathbb C\), a stabilizer subgroup of \(\mathbb G_a\) is
either trivial or the whole group. Thus a nontrivial action is
free precisely when it has no fixed points. Algebraically, the
condition is
\[
(d(K))K=K,
\tag{5}
\]
where the left side is the ideal generated by all derivatives.

Consequently, any nonpolynomial \(K\) satisfying (2) would have
fixed points for **every** nonzero intrinsic additive action.
This is a stronger necessary condition than merely the absence
of a global slice or a proper action.

The local slice theorem still gives a product on a principal
open subset. Choose \(r\) with \(d^2(r)=0\) and
\(f=d(r)\ne0\). Then \(f\in A\), and
\[
K_f=A_f[r/f],\qquad d(r/f)=1.
\tag{6}
\]
The distinction is the denominator \(f\). Removing it globally
is not justified by (3), flatness, or the existence of \(s\)
on the other cylinder.

The full argument and its boundary cases appear in the
[intrinsic quotient note](research/intrinsic-quotient-surface-pass.md).

## 4. A polynomial quotient does not give a section

Consider the exact polynomial example
\[
K=\mathbb C[x,y,z],\qquad
d=x\partial_y+2y\partial_z,\qquad v=xz-y^2.
\tag{7}
\]
Its flow is
\[
(x,y,z)\longmapsto
(x,\ y+tx,\ z+2ty+t^2x),
\]
and
\[
\ker d=\mathbb C[x,v].
\tag{8}
\]

To check the kernel directly, invert \(x\). The localized ring is
\(\mathbb C[x,x^{-1},v,y]\), with \(d=x\partial_y\).
An invariant in \(K\) has the form \(x^{-m}Q(x,v)\).
If a genuine denominator remained, reduction modulo \(x\) would
give \(Q(0,-y^2)=0\) for a nonzero polynomial \(Q(0,v)\).
The substitution \(v\mapsto-y^2\) is injective, a contradiction.

Now suppose the actual inclusion \(\mathbb C[x,v]\subset K\)
admitted an algebra retraction. Images \(Y,Z\in\mathbb C[x,v]\)
of \(y,z\) would satisfy
\[
xZ-Y^2=v.
\]
Modulo \(x\), this becomes
\[
-Y(0,v)^2=v,
\]
which is impossible: a nonzero polynomial square has even degree.
The same argument excludes a retraction
\(\mathbb C[x,v]\subset K[s]\), since restricting it to \(K\)
would give the forbidden one.

The quotient fibers make the distinction visible.

| Base point | Fiber of \((x,y,z)\mapsto(x,xz-y^2)\) |
| --- | --- |
| \(x\ne0\) | One affine line |
| \(x=0,\ v=\beta\ne0\) | Two disjoint affine lines |
| \(x=v=0\) | The nonreduced double line \(\operatorname{Spec}\mathbb C[y,z]/(y^2)\) |

The fixed locus is \(x=y=0\). This example satisfies the exact
polynomial-cylinder premise. It disproves automatic freeness,
a section for the actual inclusion, and globally trivial
affine-line fibers. It is not a cancellation counterexample,
because \(K\) is already polynomial and has other free actions.

## 5. Coordinate-frame complexity

Fix any polynomial coordinates \(x_1,\ldots,x_4\) of \(B\), and
write \(T_i=\partial_{x_i}\). Measure derivations using degree
in the slice variable \(s\):
\[
q_i=\sup_{f\ne0}
\bigl(\deg_s(T_i f)-\deg_s f\bigr),\qquad
H=\sum_{i=1}^4(q_i+1).
\tag{9}
\]
The degrees are finite integers. Finite generators of \(K\),
together with \(s\), suffice to compute them.

Always \(q_i\ge-1\). If \(q_i=-1\), then
\(T_i=fE\) for \(f\in K\). A coordinate partial has a slice,
so \(f\) is a unit and hence a nonzero constant. In that case
\(\ker E=\ker T_i\cong\mathbb C^{[3]}\).

If \(q_i\ge0\), its highest derivation has the form
\[
\widehat T_i=s^{q_i}\delta_i,\qquad
0\ne\delta_i\in\operatorname{LND}(K).
\tag{10}
\]
The highest term on \(s\) is zero: otherwise the homogeneous
LND would send \(s\) to a nonzero multiple of itself.
In particular \(\deg_s T_i(s)\le q_i\).
The \(\delta_i\)'s commute because the \(T_i\)'s commute.

At most one coordinate partial can have degree \(-1\).
Thus \(H\ge3\), and a minimum over all coordinate frames exists.
Moreover,
\[
H_{\min}=3\quad\Longleftrightarrow\quad
K\cong\mathbb C^{[3]}.
\tag{11}
\]
The forward implication uses the negative-degree case; the reverse
uses an adapted frame \((a,b,c,s)\). Equation (11) defines an
equivalent target. Well-ordering alone gives no decreasing move.

### Two degree-zero partials

If \(q_i=0\), then \(T_i(K)\subset K\) and \(T_i(s)\in K\).
Therefore \([T_i,E]=0\).
If two coordinate partials have this property, their common
kernel is an ambient coordinate plane
\(R=\mathbb C[x_3,x_4]\), and \(E\) preserves \(R\).

If \(E|_R=0\), an ambient coordinate is already invariant.
Otherwise Rentschler's planar triangularization theorem gives
an invariant coordinate of \(R\), which remains an ambient
coordinate of \(B\).[^4] The theorem of Bhatwadekar, Gupta and
Lokhande then applies: a nonzero LND of a four-variable
polynomial ring fixing an ambient coordinate and having
regular kernel has a polynomial kernel over that coordinate
ring.[^5] Here regularity follows from (2).

Consequently two degree-zero partials imply cancellation.
In particular \(H\le6\) suffices: absent a negative degree,
four nonnegative integers with sum at most two contain at
least two zeros.

### One degree zero and one degree one suffice

The following lemma supplies a stronger closing condition.

**Single-partial lemma.** Let \(D\ne0\) be an LND on
\(R=\mathbb C[x,y,z]\). If
\[
[D,[D,\partial_x]]=0,
\tag{12}
\]
then \(\ker D\) contains an ambient coordinate of \(R\).

Set \(W=[D,\partial_x]\). The point requiring care is local
nilpotence: a commutator of LNDs need not be an LND.
Here (12) gives the exact identity
\[
\exp(tD)\partial_x\exp(-tD)=\partial_x+tW
\]
on \(R[t]\), with every derivation killing \(t\).
The left side is a conjugate LND. If \(W\ne0\), its highest
\(t\)-coefficient is therefore an LND. Also \([D,W]=0\).

If \(W\ne0\) and \(D,W\) have different kernels, the commuting-pair theorem
of Daigle--Kaliman and Maubach gives an ambient coordinate in
their common kernel.[^4] Otherwise \(W\) is proportional to
\(D\) over \(\operatorname{Frac}R\). Write
\[
D=b_1\partial_x+b_2\partial_y+b_3\partial_z.
\]
The proportionality says that each nonzero ratio \(b_i/b_j\)
is independent of \(x\). This includes \(W=0\).

Let \(g=\gcd(b_1,b_2,b_3)\), and put \(D_0=D/g\).
Since \(D(g)\) is divisible by \(g\), local nilpotence implies
\(D(g)=0\). Hence \(D_0(g)=0\), and
\(D^n=g^nD_0^n\) proves that \(D_0\) is an LND with the same
kernel.

The primitive coefficient vector of \(D_0\) has ratios in
\(\mathbb C(y,z)\). Clear denominators to obtain a primitive
vector in \(\mathbb C[y,z]^3\). The two primitive vectors are
proportional over \(\operatorname{Frac}R\); unique
factorization forces the proportionality factor to be a
nonzero constant. Thus all coefficients of \(D_0\) lie in
\(\mathbb C[y,z]\).

Now \(D_0\) preserves the coordinate plane \(\mathbb C[y,z]\).
If the restriction is zero, \(y\) is invariant. Otherwise
Rentschler gives an invariant plane coordinate. In either
case it is an ambient coordinate of \(R\), proving the lemma.

Return to (2). A degree-zero partial \(T_0\) commutes with
\(E\), so \(E\) preserves its three-variable polynomial
kernel \(R\). A second coordinate partial \(T_1\) of degree
one preserves \(R\) and satisfies
\([E,[E,T_1]]=0\): its coefficients on \(K\) and on \(s\)
are at most linear in \(s\).

If \(E|_R=0\), a coordinate in \(R\) is invariant. Otherwise
the single-partial lemma applied inside \(R\) produces one.
It remains an ambient coordinate of \(B\), so the regular
kernel theorem again identifies \(K\) with \(\mathbb C^{[3]}\).
This proves cancellation for every degree pattern
\((0,1,*,*)\), not just a fixed total height.

It follows that
\[
H\le7\quad\Longrightarrow\quad K\cong\mathbb C^{[3]},
\qquad K\not\cong\mathbb C^{[3]}
\quad\Longrightarrow\quad H_{\min}\ge8.
\tag{13}
\]
Indeed, a hypothetical exotic frame has no negative degree,
at most one zero, and a zero forces all three other degrees
to be at least two. The only surviving sorted pattern at
height eight is \((1,1,1,1)\); at height nine it is
\((1,1,1,2)\). A surviving frame with a zero must have height
at least ten.

These are necessary conditions on a hypothetical
counterexample. No theorem bounds its height from above.
The [height-seven audit](research/height-seven-audit.md)
gives a separate reconstruction and a nonlinear control
showing that the invariant coordinate need not be linear
in the original variables.

## 6. Why simplifying leading fields is not enough

The frame
\[
(a,b,c+(a+b)s,s)
\]
on a known polynomial cylinder has degrees \((1,1,0,0)\).
Its leading intrinsic directions all span the same line,
even though the degree-zero argument proves cancellation.
Thus leading rank alone is a weaker test than the frame criterion.

The stronger obstruction survives division by common polynomial
factors. Take an irreducible rank-three LND \(\delta\) on
\(\mathbb C[a,b,c]\), for example Freudenburg's derivation, and put
\[
\alpha=\exp(s\delta),\qquad
X_i=\alpha(a_i)\ (i=1,2,3),\qquad X_4=s.
\]
These are polynomial coordinates. Their partials are
\[
T_i=\alpha\partial_{a_i}\alpha^{-1},\qquad
T_4=E-\delta.
\tag{14}
\]
For \(i\le3\), write \(T_i=\sum_j s^jD_{ij}\).
Differentiating gives
\(\partial_sT_i=[\delta,T_i]\), so each highest nonzero
coefficient commutes with \(\delta\).
It is itself an LND by the highest-term argument.

Dasgupta and Gaifullin's Theorem 4.5(i) says that every nonzero
LND commuting with an irreducible rank-three LND in three
variables has the same kernel.[^4] It follows that the highest
coefficients are fraction-field multiples \(f_i\delta\).
Since the coefficients of \(\delta\) have gcd one, their
polynomiality forces \(f_i\) to be polynomial.
Commutation then forces \(\delta(f_i)=0\).

Every primitive leading field is therefore a scalar multiple
of \(\delta\). For the concrete choice
\[
f=ac-b^2,\qquad
g=cf^2+2a^2bf+a^5,\qquad
\delta=\operatorname{Jac}(f,g,\cdot),
\tag{15}
\]
the coefficient gcd is one and every coefficient vanishes at
the origin. These primitive fields retain a fixed point and
cannot have a slice. Their rank-three property is a published
property of this example, not something established by a gcd
calculation.

Each of the first three conjugation degrees is at least two:
a degree at most one would give the double-commutator identity
for \(\delta\), contradicting the single-partial lemma and
rank three. The selected frame has height at least ten.

The inverse flow recovers an adapted frame. Thus (14) refutes
a particular normalization shortcut, not the existence of
some good frame. The two meanings of rank must also be kept
separate: one LND having rank three means its kernel contains
no ambient coordinate; the collection of leading fields here
has generic vector-space rank one.

### A lower-degree row need not be a coordinate partial

For one explicit nonlinear frame, a polynomial row combination
cancels the highest term and lowers the filtration degree from
five to three. Its restriction to \(\mathbb C[a,s]\) is
\[
W=(1+4as)\partial_a-2a\partial_s.
\]
The ordinary total-degree highest derivation is
\(4as\partial_a\), whose iterates on \(a\) never vanish.
Hence \(W\) is not locally nilpotent. Merely lowering degree
does not certify a valid frame change.

For an actual elementary change \(x_j\mapsto x_j+P(x_{\ne j})\),
the partials change by
\[
T_i\mapsto T_i-(T_iP)T_j,\quad i\ne j.
\tag{16}
\]
The coefficients must be derivatives of one polynomial \(P\);
they obey compatibility equations and simultaneous degree
bounds. Generic linear dependence of leading fields supplies
neither requirement. The
[frame-minimization note](research/coordinate-frame-minimization-pass.md)
gives explicit successful repairs and the failed row example.

## 7. Orbit rank does not descend from cylinder flexibility

For a UFD \(K\), Daigle's Lemma 3.5 identifies the field
Makar-Limanov invariant with
\(\operatorname{Frac}(\operatorname{ML}(K))\).[^6]
The orbit results for groups generated by additive actions
then give
\[
r=3-\operatorname{trdeg}_{\mathbb C}\operatorname{ML}(K),
\tag{17}
\]
where \(r\) is the generic rank of all intrinsic LND directions.[^7]
Nonrigidity proves \(r\ge1\), but the checked inputs do not
establish \(r\ge2\) for every \(K\) in (2).

Even \(r=3\) would give an open orbit for the group generated
by all additive actions, not three commuting fields.
The distinction matters. Three independent commuting
intrinsic LNDs give a vector-group action with an open orbit;
unipotent orbits in an affine variety are closed,[^9] so this
orbit is the whole irreducible threefold and cancellation
follows. Arbitrary independent LNDs need not commute.

There is a concrete warning against using cylinder orbit rank
alone. Dubouloz constructs a smooth rigid affine surface \(S\)
whose product \(S\times\mathbb A^2\) is flexible in codimension
one.[^8] Put \(Y=S\times\mathbb A^1\).
One-cylinder rigidity implies \(r(Y)=1\), whereas
\(r(Y\times\mathbb A^1)=4\).

This is a single-cylinder jump on a smooth threefold.
It is not an example with polynomial cylinder. It shows
precisely why replacing the polynomial-isomorphism hypothesis
by generic flexibility would lose essential information.
The [orbit literature note](research/stable-factor-orbit-literature.md)
records the related conditional kernel results and their limits.

## 8. Verification and next proof obligation

The standalone quotient checker tests exact flow, invariant,
localization, fiber, and fixed-locus identities for (7), as well
as coefficient controls for (15). The frame checker tests
polynomial inverses, coordinate-partial pairing, heights,
commutation, and explicit descent sequences. Neither imports
the research solver.

All **253 exact tests across nineteen suites** passed in the
recorded run. The [verification log](verification-pass-11.json)
lists each command, observed count, exit code, and test time.
The two additional commands are:

    /opt/anaconda3/bin/python verify_intrinsic_quotients.py
    /opt/anaconda3/bin/python research/frame_height_checks.py

They run twelve and sixteen test methods, respectively.

The no-retraction proof is an arbitrary-degree parity argument.
Testing selected squares is only a regression control for it.
Likewise, polynomial identities do not verify contractibility,
Rentschler's theorem, or the classification results used above.
Source-dependent human-readable proofs and finite symbolic
checks have distinct roles.

The decisive missing assertion can now be stated without an
unproved quotient classification: starting from (2), construct
a nonzero \(d\in\operatorname{LND}(K)\) whose derivative ideal
is the unit ideal, or produce a frame satisfying a proved
closing criterion. No general construction of either kind is
given here.

A universal height-decreasing coordinate operation would also
suffice. The examples establish neither its existence nor its
failure. There is no justified finite height bound for an
arbitrary frame-minimizing slice action, and a bounded
computational search cannot supply such a bound.

At this checkpoint's first surviving pattern \((1,1,1,1)\), the four fields
\(W_i=[E,T_i]\) are LNDs commuting with \(E\). Applying
\(\operatorname{ad}_E^2\) to \([T_i,T_j]=0\) proves
\([W_i,W_j]=0\). If \(E,W_1,\ldots,W_4\) have generic rank
four, the closed-orbit argument makes their action transitive
and identifies \(E\) with a translation. The lower-rank case was
unresolved in this pass, but is now closed by the
[subsequent double-commutator theorem](deep-pass-12.md).
The Riccati identities imply \(E^4(x_i)\in\mathbb C\).
The later proof observes that a nonzero vector \(E^4(x)\)
gives a constant commuting translation, stronger than merely
another slice, and closes the other branches separately.
Neither report establishes an ordinary-degree bound.

The [proof-scope audit](research/pass11-final-proof-audit.md)
reconstructs the single-partial, quotient-flatness, and
primitive-frame arguments and finds no gap in those stated
conclusions. It does not establish the missing global step
or replace expert review.

## Sources

[^1]: Bachar Alhajjar, [*LND-Filtrations and Semi-Rigid Domains*](https://arxiv.org/pdf/1501.00445), Proposition 3.4 and its proof, attributing the one-cylinder rigidity theorem to Makar-Limanov and Crachiola--Makar-Limanov.

[^2]: Shulim Kaliman and Nikolai Saveliev, [*C+-actions on contractible threefolds*](https://www.math.miami.edu/~kaliman/library/KaSa.michigan.2004.quotient.pdf), Lemma 2.1, Theorem 2.7, Corollary 2.8. Also [arXiv:math/0209306](https://arxiv.org/abs/math/0209306).

[^3]: The Stacks Project, [Lemma 10.128.1, Tag 00R4: Miracle flatness](https://stacks.math.columbia.edu/tag/00R4).

[^4]: Nikhilesh Dasgupta and Sergey Gaifullin, [*On locally nilpotent derivations of polynomial algebra in three variables*](https://arxiv.org/pdf/2306.00510), Definition 2.3, Theorem 2.7, Proposition 2.14, Theorem 4.5(i), and Section 5. The planar theorem is Rentschler's; the commuting-pair theorem is attributed there to Daigle--Kaliman and Maubach.

[^5]: S. M. Bhatwadekar, Neena Gupta, and Swapnil A. Lokhande, [*Some K-theoretic properties of the kernel of a locally nilpotent derivation on \(k[X_1,\ldots,X_4]\)*](https://arxiv.org/html/1501.01438v1), Theorem 3.5.

[^6]: Daniel Daigle, [*Locally nilpotent derivations and the structure of rings*](https://arxiv.org/pdf/1806.10742), Lemma 3.5. Its Section 5 distinguishes stably polynomial algebras from field forms of affine space.

[^7]: Ivan Arzhantsev, Hubert Flenner, Shulim Kaliman, Frank Kutzschebauch, and Mikhail Zaidenberg, [*Flexible varieties and automorphism groups*](https://arxiv.org/pdf/1011.5375v2), Corollaries 1.14 and 1.21, Proposition 5.1.

[^8]: Adrien Dubouloz, [*Flexible bundles over rigid affine surfaces*](https://ems.press/content/serial-article-files/43375), *Commentarii Mathematici Helvetici* 90 (2015), Theorem 1.1.

[^9]: Ivan Arzhantsev, [*Limit points and additive group actions*](https://arxiv.org/html/2102.11330v1), introduction, recalling closedness of unipotent orbits on affine varieties.
