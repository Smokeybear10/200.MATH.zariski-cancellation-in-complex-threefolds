# The pointwise plinth criterion applies to the unknown intrinsic threefold

The complete peripheral-cycle proof in
[pass 17](pointwise-plinth-pass17.md) applies to the intrinsic
threefold before cancellation is known. The polynomial presentation
of its total space was not an essential hypothesis of that proof.
The scheme-theoretic reduced-fiber hypothesis remains essential.

## 1. Exact statement and inherited hypotheses

Let \(A\) be a complex domain with
\[
A[s_*]\simeq\mathbb C^{[4]},
\]
and let \(D\ne0\) be a primitive LND of \(A\) with
\(C=\ker D\simeq\mathbb C^{[2]}\). Primitivity means that
the values on a finite algebra generating set have gcd one in
the UFD \(A\). Let \(\pi:X=\operatorname{Spec}A\to
S=\operatorname{Spec}C\) be the actual quotient and
\(P_D=D(A)\cap C\) its full plinth ideal. Then
\[
\boxed{\quad
\pi^{-1}(q)\text{ is a reduced single }\mathbb A^1
\text{ with nonzero induced }D
\quad\Longrightarrow\quad q\notin V(P_D).
\quad}
\tag{1}
\]
The fiber in (1) is the entire scheme-theoretic fiber. The conclusion
is about the actual primitive action, not an arbitrary replica.

Here are all substitutions for the old assumption \(X=\mathbb A^3\).
Finite generation of \(A\) follows by applying \(s_*\mapsto0\)
to four polynomial generators. Smoothness descends from
\(X\times\mathbb A^1\); factoriality descends from \(A[s_*]\).
Projection \(X(\mathbb C)\times\mathbb C\to X(\mathbb C)\)
is a homotopy equivalence, so \(X\) is contractible. In particular
\[
H_2(X;\mathbb Q)=H_3(X;\mathbb Q)=H_4(X;\mathbb Q)=0.
\tag{2}
\]
Thus no additional vanishing theorem for \(H_4\) is needed.
The base \(S\simeq\mathbb A^2\) is smooth and factorial.
The actual quotient is equidimensional and surjective, hence
faithfully flat; these are also inherited in the application
from [the intrinsic quotient setup](quadratic-monodromy-pass46.md).

## 2. Source input versus the deduction

[Kaliman's final 2004 author PDF](https://www.math.miami.edu/~kaliman/library/Ka.invent.2004.c%2B.pdf),
Lemma 2.2, Proposition 3.2, Remark 3.3 and Theorem 5.2(i), apply
to this smooth factorial affine threefold with the vanishings in
(2). They supply the product complement and retained exceptional
factorization used in pass 17. The finiteness part only needs
\(H_3(X)=0\) and smooth \(X^*\); the retained-curve reduction
also uses \(H_2(X)=0\). These statements and their relevant
complete proofs were directly reread.

Write \(E\xrightarrow{\kappa}Z\xrightarrow{\theta}\Gamma\)
for that factorization. Each retained component has degree at
least two, and its pullback divisor is reduced. The equality
\(\Gamma=V(P_D)_{\mathrm{red}}\) for primitive \(D\) was
already extended to the unknown \(A\) by the generator-gcd
argument in [pass 46, Section 3.1](quadratic-monodromy-pass46.md).
No coordinate formula for \(D\) on \(A\) is assumed.

## 3. Complete transfer of the peripheral-cycle argument

Suppose \(q\in\Gamma\) satisfies the fiber premise in (1).
Choose the finite exceptional set \(F\) in the old proof to
contain \(q\) and all necessary singular and ramification values.
The complements \(\widehat X\simeq\widehat S\times\mathbb A^1\)
give the right-hand homology isomorphism in its diagram (2).
Exactness consequently gives
\[
\theta_*\beta\in\operatorname{im}\phi
\quad\Longrightarrow\quad
\beta\in\operatorname{im}\phi'.
\tag{3}
\]
The vanishing \(H_4(X)=H_3(X)=0\) identifies
\(H_3(X^*)\) with \(H_4(X,X^*)\). Excision and Thom
functoriality therefore place the image of \(\phi'\) in
cycles supported near the full fibers over \(F\), exactly as
in pass 17, equations (5)–(6). Neither step used an ambient
polynomial coordinate.

Faithful flatness plus the reduced smooth fiber makes \(\pi\)
smooth at every point of \(Y=\pi^{-1}(q)\), by
[Stacks 01V9](https://stacks.math.columbia.edu/tag/01V9).
Normalization over this smooth neighborhood is obtained by
base-changing the normalization of each base branch, by
[Stacks 03GV](https://stacks.math.columbia.edu/tag/03GV).
Thus each normalized base branch has exactly one connected
copy of \(Y\) above it. It reaches one normalized branch of
\(Z\), and that branch has ramification index one: higher
ramification would make the pulled-back base parameter have
zero differential along this smooth fiber.

Since the finite normalized cover has degree at least two,
each such base branch also has an unreached normalized point.
The finite normalization of \(E\) is proper. Disjoint small
disks around the normalized points, followed by the complement
of the image of the closed unwanted part, therefore give an
open neighborhood of the entire \(Y\) which reaches only the
selected branches. This is the whole-fiber support step of
pass 17, Section 4; it does not require \(Y\) to be compact.

Consequently every element of \(\operatorname{im}\phi'\)
has zero coefficient at an unreached peripheral loop over
\(q\). Those finite peripheral loops are independent: on
each smooth affine normalized component the one total-puncture
relation includes a puncture at infinity. Yet selecting one
loop above every base branch, including an unreached loop,
and weighting it by the reciprocal of its ramification index
produces \(\beta\) with
\(\theta_*\beta=\phi(\omega_q)\). Equation (3) contradicts
the support restriction. Thus \(q\notin\Gamma\), proving (1).

This is precisely the old proof with its actual hypotheses
checked on the unknown threefold, not an additional theorem
attributed verbatim to Kaliman. The nonzero-action premise is
retained, although the support argument itself only uses the
reduced single-line fiber after the primitive retained curve
has been identified.

## 4. Boundaries relevant to second-image gluing

The curve \(Z\) is not defined as the full invariant spectrum
of \(E\). Moreover, surjectivity of \(\kappa\) does not imply
surjectivity after normalizing its target. The proof above
explicitly distinguishes reached and unreached normalized
branches; it never replaces that distinction by surjectivity.

Likewise, a minimal slice being scalar on a full closed fiber
does not assert that the fiber is reduced, irreducible, or
an affine line. Applying (1) to
[the scalar-fiber criterion](second-image-closed-fiber-pass47.md)
requires a separate algebraic argument establishing all these
fiber properties. The curve-level control \(v=w^2,r=w^3\)
from [the source audit](image-ideal-source-scope-pass47.md)
also shows why finiteness alone is insufficient.

No assertion that \(J=C\), no global quadratic presentation,
and no cancellation conclusion follows from this scope extension
alone. It uses no numerical test and changes no frozen proof.
