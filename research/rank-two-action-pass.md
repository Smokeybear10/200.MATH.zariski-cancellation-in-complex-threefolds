# Two commuting intrinsic additive actions

This note reconstructs a known sufficient condition and identifies the
remaining degeneration set. Its conclusion is a special case of
[Derksen, van den Essen and Maubach, Theorem 2.1](https://arxiv.org/pdf/0806.2038).
The [subsequent saturation audit](saturated-rank-two-pass.md) supplies this
more direct attribution and shows why saturating the intrinsic pair need
not remove a bad fiber. General cancellation remains unresolved here.

## 1. Result

Let

\[
B=K[s]\cong \mathbb C^{[4]},\qquad X=\operatorname{Spec}K,
\]

and let \(d_1,d_2\in\operatorname{LND}_{\mathbb C}(K)\) commute.  Suppose
they are generically independent over \(\operatorname{Frac}K\).  Put

\[
A=\ker d_1\cap\ker d_2.
\]

Then there is a polynomial \(t\in K\) such that

\[
A=\mathbb C[t].
\tag{1}
\]

Every fiber \(X_\lambda=V(t-\lambda)\) is an integral affine surface.  There
is a finite set \(S\subset\mathbb C\) with the following exact dichotomy:

* if \(\lambda\notin S\), then \(X_\lambda\) is one free
  \(\mathbb G_a^2\)-orbit and hence is \(\mathbb A^2\);
* if \(\lambda\in S\), the two tangent fields are dependent at **every**
  point of \(X_\lambda\).

Consequently, if \(d_1,d_2\) are pointwise independent on all of \(X\), then

\[
K\cong\mathbb C[t]^{[2]}\cong\mathbb C^{[3]}.
\tag{2}
\]

This is a useful closure criterion, but it is not a proof of cancellation.
Stable affineness does not supply pointwise independence.  Indeed, even for
\(K=\mathbb C^{[3]}\), the pair

\[
d_1=t\partial_u,\qquad d_2=t\partial_v
\tag{3}
\]

has generic rank two and common kernel \(\mathbb C[t]\), but the whole fiber
\(t=0\) is fixed.  Thus generic rank two is genuinely insufficient.

Pointwise independence also should not be advertised as logically weaker
than the existence of one proper action.  It avoids assuming properness, but
it is a different two-action hypothesis; the proof ultimately shows that the
pair is a trivial \(\mathbb G_a^2\)-torsor over \(\mathbb A^1\).

## 2. Stable-affine input

The equality \(K[s]\cong\mathbb C^{[4]}\) implies

\[
\dim K=3,\qquad K\text{ is regular and a UFD},\qquad K^*=\mathbb C^*.
\tag{4}
\]

The UFD assertion also follows directly from Gauss's theorem, and the unit
assertion from \((K[s])^*=K^*\).  Regularity descends from a polynomial ring.
Only the UFD and unit parts of (4) are needed to identify the common invariant
ring; regularity is useful for interpreting the rank-drop locus as the zero
locus of \(d_1\wedge d_2\).

Because \([d_1,d_2]=0\), their exponentials define a
\(G=\mathbb G_a^2\)-action on \(X\).  Generic independence means that this
action has generic orbit dimension two.

## 3. The common invariant field has dimension one

Set \(A_1=\ker d_1\).  Commutation gives \(d_2(A_1)\subseteq A_1\).  The
restriction

\[
e=d_2|_{A_1}
\]

is nonzero.  Otherwise both \(d_1\) and \(d_2\) would kill
\(F_1=\operatorname{Frac}(A_1)\).  The local-slice argument gives

\[
F_1=\operatorname{Frac}(K)^{d_1},
\qquad
\operatorname{trdeg}_{F_1}\operatorname{Frac}K=1.
\]

In characteristic zero, the \(\operatorname{Frac}K\)-vector space of
\(F_1\)-derivations of \(\operatorname{Frac}K\) is one-dimensional.  Hence
\(d_1,d_2\) would be generically dependent, a contradiction.

Applying the same local-slice argument to \(e\) yields

\[
\operatorname{Frac}(A)
=\operatorname{Frac}(A_1)^e
=\operatorname{Frac}(K)^{d_1,d_2},
\qquad
\operatorname{trdeg}_{\mathbb C}A=1.
\tag{5}
\]

For completeness, the local-slice field equality needs no finite-generation
theorem.  If \(D\ne0\) is an LND of a characteristic-zero domain, choose
\(r\) with \(D^2r=0\ne Dr\).  After inverting \(Dr\), the element
\(r/Dr\) is a slice, so the fraction field is a rational function field of
degree one over the fraction field of the kernel.

## 4. Why the common invariant ring is exactly \(\mathbb C[t]\)

Kernels of LNDs are factorially closed: the additive \(D\)-degree satisfies
\(\deg_D(fg)=\deg_D(f)+\deg_D(g)\), so an invariant product has invariant
factors.  Therefore \(A\), an intersection of two kernels, is factorially
closed in \(K\).

Since \(K\) is a UFD, factorial closure makes \(A\) a UFD as well.  Indeed,
factor an element of \(A\) into irreducibles of \(K\); factorial closure
puts every factor back in \(A\), and uniqueness is inherited.  Also
\(A^*=\mathbb C^*\) by (4).

Embed \(K\subset B=\mathbb C[x_1,x_2,x_3,x_4]\) and choose a nonconstant
\(t\in A\) of least positive total degree.  For every \(\lambda\in\mathbb C\),
the element \(t-\lambda\) is irreducible in \(A\): a factorization into two
nonunits would express its degree as a sum of two smaller positive degrees.

Let \(p\) be any irreducible of \(A\).  By (5), \(p\) and \(t\) are
algebraically dependent.  Remove the largest common power of the second
variable from a polynomial relation to obtain

\[
a_0(t)+a_1(t)p+\cdots+a_n(t)p^n=0,
\qquad 0\ne a_0\in\mathbb C[T].
\]

Thus \(p\mid a_0(t)\).  Factoring \(a_0(T)\) over \(\mathbb C\), primality
of \(p\) in the UFD \(A\) makes \(p\) associate to some \(t-\lambda\).
Every element of \(A\) is consequently a product of such linear factors and
a constant.  This proves (1).  In particular, this argument bypasses the
general finite-generation problem for unipotent invariants.

## 5. Integral fibers and the orbit dichotomy

The preceding minimal-degree argument shows that \(t-\lambda\) is
irreducible in \(A\).  It stays irreducible in \(K\): any factorization in
\(K\) has both factors in \(A\) by factorial closure.  Since \(K\) is a UFD,
\(t-\lambda\) is prime.  It is not a unit, again by factorial closure and
\(A^*=\mathbb C^*\).  Hence

\[
K/(t-\lambda)K
\]

is a two-dimensional domain for every \(\lambda\), so every fiber is
nonempty, reduced, and irreducible.

Both derivations kill \(t\), so every \(G\)-orbit lies in a fiber.  The
Kostant--Rosenlicht theorem says that every orbit of a unipotent algebraic
group on an affine variety over an algebraically closed field is closed.[^kr]
If \(d_1,d_2\) are independent at one point of \(X_\lambda\), its orbit is
a closed two-dimensional subvariety of the irreducible two-dimensional
fiber.  It must equal the entire fiber.  Its stabilizer has zero Lie algebra;
in characteristic zero \(\mathbb G_a^2\) has no nontrivial finite subgroup,
so the stabilizer is trivial.  Therefore

\[
X_\lambda\cong G\cong\mathbb A^2,
\tag{6}
\]

and the fields are independent at every point of that fiber.  Otherwise they
are dependent everywhere on the fiber.  This proves the claimed dichotomy.

Let \(Z\) be the zero locus of \(d_1\wedge d_2\).  It is a proper closed
subset because the pair is generically independent.  Since \(K\) is a
domain containing \(\mathbb C[t]\), it is torsion-free and hence flat over
the PID \(\mathbb C[t]\).  The morphism

\[
\pi:X\longrightarrow\mathbb A^1_t
\]

is also surjective by the preceding nonempty-fiber result and is of finite
presentation; it is therefore open.  If infinitely many fibers lay in
\(Z\), their parameter values would be dense in \(\mathbb A^1\), and
openness would make their union dense in \(X\), contradicting that \(Z\) is
proper and closed.  The bad set \(S\) is therefore finite, and set-theoretically

\[
Z=\bigcup_{\lambda\in S}X_\lambda
=V\!\left(\prod_{\lambda\in S}(t-\lambda)\right).
\tag{7}
\]

Equation (7) is a statement about the support of the rank-drop scheme; it
does not assert that its determinantal ideal is radical or has multiplicity
one along a bad fiber.

## 6. Pointwise independence closes cancellation

Assume now that \(S=\varnothing\).  Every closed fiber of \(\pi\) is
\(\mathbb A^2_{\mathbb C}\) by (6).  The generic fiber is also
\(\mathbb A^2_{\mathbb C(t)}\).  One way to see the only subtle point is:

1. flat finite presentation and the geometrically integral closed fibers
   imply that the generic fiber is geometrically integral;
2. after extending \(\mathbb C(t)\) to an algebraic closure, every
   \(G\)-orbit is closed, two-dimensional, and has trivial stabilizer;
3. such an orbit is the whole irreducible generic fiber, so that fiber is a
   \(\mathbb G_a^2\)-torsor over the field;
4. \(H^1(\mathbb C(t),\mathbb G_a^2)=0\), so the torsor is trivial.

Thus \(K\) is an \(\mathbb A^2\)-fibration over \(R=\mathbb C[t]\) in the
standard sense: it is finitely generated and flat over \(R\), and every
residue-field fiber is a two-variable polynomial ring.

Sathaye's theorem says that an \(\mathbb A^2\)-fibration over a DVR
containing \(\mathbb Q\) is a polynomial algebra.[^sathaye]  Localizing at
every maximal ideal of the PID \(R\) therefore makes \(K\) locally
\(R^{[2]}\).  The Bass--Connell--Wright theorem identifies a locally
polynomial algebra as the symmetric algebra of a finite projective module;
over a PID that module is free.[^bcw]  Hence

\[
K=R^{[2]}=\mathbb C[t]^{[2]},
\]

which proves (2).  Babu and Das explicitly record this exact
Sathaye-plus-Bass--Connell--Wright implication for an
\(\mathbb A^2\)-fibration over a PID.[^babu-das]

There is also a direct torsor interpretation.  Fiberwise simple transitivity
makes

\[
G\times X\longrightarrow X\times_{\mathbb A^1}X,
\qquad (g,x)\longmapsto(gx,x),
\]

an isomorphism, by the standard fiberwise isomorphism criterion for
finite-presentation flat schemes.  Thus \(X\to\mathbb A^1\) is a
\(\mathbb G_a^2\)-torsor; its class lies in
\(H^1(\mathbb A^1,\mathcal O^{\oplus2})=0\).  The classical
\(\mathbb A^2\)-fibration route above is retained as the cited algebraic
closure argument rather than relying only on this reformulation.

## 7. Why the ambient leading fields do not supply the hypothesis

The four leading LNDs \(\delta_i\) extracted from ambient coordinate
partials commute, but the filtration does not preserve their original frame
rank.  The exact coordinate change in
[`intrinsic-actions-pass.md`](intrinsic-actions-pass.md), equations
(11)--(13), has

\[
\delta_1=\delta_2=\delta_3=\delta_4=2a\partial_c.
\]

All four top fields have generic rank one and vanish along \(a=0\), even
though \(K=\mathbb C[a,b,c]\) and all original ambient partials are
coordinate translations.  Thus stable affineness gives neither generic rank
two nor a pointwise independent pair of leading fields.

If in a particular presentation two fixed constant linear combinations of
the commuting \(\delta_i\) have nowhere-vanishing wedge, the theorem above
does apply: constant sums of commuting LNDs are again locally nilpotent.  But
generic rank two alone leaves exactly the finite bad-fiber set (7).  The
control (3) shows that stable affineness cannot formally force that set to be
empty.  Eliminating or classifying those wholly degenerate fibers is the
precise remaining rank-two proof obligation.

## 8. Claim boundary

The proof gives a complete **conditional** theorem:

\[
\boxed{\text{two commuting pointwise-independent intrinsic LNDs}
\Longrightarrow K\cong\mathbb C^{[3]}.}
\]

It also reduces generic rank two to finitely many entire bad fibers.  It does
not show that arbitrary stably affine \(K\) possesses such a pair, that the
ambient leading fields contain such a pair, or that the bad fibers disappear.
No originality claim is made; the closing input is classical affine-fibration
theory, and this note is a working reconstruction rather than expert review.

## Primary sources and access boundary

[^kr]: Ivan Arzhantsev, [“Limit Points and Additive Group Actions,” Introduction](https://arxiv.org/html/2102.11330v1), arXiv:2102.11330v1.  This primary paper recalls the Kostant--Rosenlicht theorem in the form used here: unipotent-group orbits on affine varieties are closed.
[^sathaye]: Avinash Sathaye, [“Polynomial Ring in Two Variables Over a D.V.R.: A Criterion”](https://doi.org/10.1007/BF01388536), *Inventiones Mathematicae* **74** (1983), 159--168.  The publisher page confirms author, volume, pages, date, and DOI; the full original text was subscription-only in this pass.  Its DVR consequence and the needed characteristic-zero setting were checked against the accessible later primary source in the next note.
[^bcw]: Hyman Bass, Edwin H. Connell, and David L. Wright, [“Locally Polynomial Algebras Are Symmetric Algebras”](https://doi.org/10.1007/BF01403135), *Inventiones Mathematicae* **38** (1976), 279--299.  The publisher page confirms the metadata and theorem scope; the full original text was subscription-only in this pass.
[^babu-das]: Janaki Raman Babu and Prosenjit Das, [“Structure of \(\mathbb A^2\)-Fibrations Having Fixed Point Free Locally Nilpotent Derivations,” §1 definition and discussion preceding Theorem 4.7](https://arxiv.org/pdf/2001.07632v5), arXiv:2001.07632v5 (2020), published in *Journal of Pure and Applied Algebra* **225** (2021), 106763.  The paper defines an \(\mathbb A^2\)-fibration as finite type and flat with polynomial fibers at every prime, and explicitly states that Sathaye proves triviality over a DVR and that Bass--Connell--Wright globalizes it to a PID.
