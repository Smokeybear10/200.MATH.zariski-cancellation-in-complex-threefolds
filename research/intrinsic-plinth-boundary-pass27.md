# Intrinsic plinths and boundary invariant fields

For every nonzero locally nilpotent derivation of a complex affine
threefold \(A\) satisfying \(A[s]\simeq\mathbb C^{[4]}\), the full
plinth ideal is principal. This removes the extra principality
premise from the previous intrinsic centralizer application.

The mechanism is already published: faithful flatness and factorial
closure give a gcd argument for local slices. The useful consequence
here is that the mechanism applies to the unknown threefold itself,
not only to an ambient ring assumed to be \(\mathbb C^{[3]}\).

For a primitive action, the prime support of this plinth is detected
exactly by nontrivial extensions of boundary invariant function fields.
A separate established recognition theorem closes the intrinsic fence
case when the exceptional surface fibers are factorial. Neither fact
makes that factoriality, or a free intrinsic action, automatic.

## 1. The established intrinsic hypotheses

Let \(A\) be an affine complex domain, \(A[s]\simeq\mathbb C^{[4]}\),
and \(0\ne D\in\operatorname{LND}(A)\). Write \(C=\ker D\).
The [intrinsic quotient argument](intrinsic-quotient-surface-pass.md)
gives
\[
C\simeq\mathbb C^{[2]},\qquad
C\longrightarrow A\text{ faithfully flat}.
\tag{1}
\]
The cylinder makes \(\operatorname{Spec}A\) smooth and contractible.
A dominant affine-three-space slice of its cylinder projection supplies
the exact domination hypothesis in Kaliman and Saveliev's quotient
theorem. That theorem identifies the invariant quotient as an affine
plane; nonempty curve fibers and miracle flatness give (1).[^1]

Also \(A\) is a UFD: factoriality descends through a polynomial
extension. The invariant ring is factorially closed in \(A\).
These conclusions concern the actual inclusions. They do not assert
an algebra retraction \(A\to C\), which is false in a previously
verified polynomial example.

## 2. Faithful flatness makes the plinth principal

The following elementary argument works more generally whenever
\(A\) is a characteristic-zero UFD, \(C=\ker D\) is Noetherian,
and \(A\) is faithfully flat over \(C\).

Let \(f_1,f_2\) be nonzero elements of
\(I=D(A)\cap C\), and choose \(r_i\in A\) with \(Dr_i=f_i\).
Put \(J=(f_1,f_2)C\). The element
\[
c=r_1f_2-r_2f_1
\tag{2}
\]
is invariant and lies in \(JA\).
Faithful flatness gives \(JA\cap C=J\). Hence
\(c=a_1f_2-a_2f_1\) for some \(a_1,a_2\in C\), and
\[
(r_1-a_1)f_2=(r_2-a_2)f_1.
\tag{3}
\]

Let \(g=\gcd_C(f_1,f_2)\) and \(f_i=gq_i\).
Factorial closure ensures that these are also the relevant gcds
in \(A\), so \(q_1,q_2\) are coprime there. Equation (3) implies
\[
r=\frac{r_1-a_1}{q_1}
 =\frac{r_2-a_2}{q_2}\in A,\qquad Dr=g.
\tag{4}
\]
Thus \(I\) is closed under taking gcds. Apply this to a finite set
of ideal generators of \(I\). Their gcd \(p\) belongs to \(I\)
and divides every generator, proving
\[
D(A)\cap C=pC,\qquad Dr=p\text{ for some }r\in A.
\tag{5}
\]

This is the gcd proof in Daigle and Kaliman's Theorem 1.5, printed
p. 539, with exactly its required algebraic hypotheses retained.[^2]
Masuda explicitly states the general factorial faithfully-flat
version in the remark following Proposition 2.5.[^3]
There is no new claim of priority for the argument.

Consequently every primitive intrinsic action under (1) satisfies
the principality premise of the
[pass-26 centralizer proposition](fence-centralizer-sector-pass26.md).
If \(p\) is a unit, a scalar-normalized \(r\) is already a slice and
\(A=C[r]\simeq\mathbb C^{[3]}\).
If \(p\) is not a unit, the fence/non-fence commuting-direction
dichotomy applies without another plinth hypothesis.

This proof does not assert that all higher image ideals
\(D^n(A)\cap C\) are principal. The first-image gcd correction uses
an invariant difference of two local slices; it must not be
replaced silently by a higher-order version.

## 3. Every prime boundary has a well-defined finite invariant degree

Assume now that \(D\) is primitive. For any prime element \(f\in C\),
factorial closure makes \(f\) prime in \(A\), and
\(C/fC\hookrightarrow A/fA\) is injective.
The induced LND \(\overline D\) of \(A/fA\) is nonzero:
otherwise \(D(A)\subset fA\), contradicting primitivity.

Define
\[
K_f=\operatorname{Frac}(C/fC),\qquad
E_f=\operatorname{Frac}\bigl(\ker(\overline D:A/fA\to A/fA)\bigr),
\qquad e_f=[E_f:K_f].
\tag{6}
\]
Both fields have transcendence degree one over \(\mathbb C\).
The extension is finite: the algebraic closure of \(K_f\) in the
finitely generated field \(\operatorname{Frac}(A/fA)\) is finite
over \(K_f\), and \(E_f\) lies in it. Thus \(e_f\) is a positive
integer. No normality of the boundary surface \(A/fA\) is needed.

The precise support test is
\[
\boxed{e_f>1\quad\Longleftrightarrow\quad f\mid p.}
\tag{7}
\]

If \(f\nmid p\), localize the local-slice identity
\(A_p=C_p[r]\) and then reduce modulo \(f\). The induced derivation
is \(p\partial_r\), with \(p\) now invertible. Its invariant field
is \(K_f\), proving \(e_f=1\).

Suppose \(f\mid p\). The residue \(\overline r\) of the minimal
local slice is invariant under \(\overline D\).
If \(\overline r\in K_f\), there would be \(a,b\in C\),
\(f\nmid b\), and \(t\in A\) such that
\[
br-a=ft,\qquad
Dt=\frac{bp}{f}\in C.
\tag{8}
\]
But (5) would require \(bp/f\in pC\).
Cancellation in the fraction field then forces \(b\in fC\),
a contradiction. Therefore \(\overline r\notin K_f\),
and \(e_f>1\), proving (7).

This proof is the elementary minimal-local-slice obstruction behind
the boundary-degree criterion, not an assertion that the boundary
has degree one. Masuda's Lemma 3.1 and Theorem 3.5 record the
corresponding nontrivial boundary extension and birational
recognition mechanism in the broader factorial setting.[^3]

In particular \(D\) has a slice exactly when all degrees in (6)
equal one. A nonsliced primitive intrinsic action therefore has
a nontrivial boundary field extension along every plinth component.
That is a constraint on such actions, not an exclusion of the
underlying threefold.

## 4. Positive and negative boundaries of the field-degree test

The ordinary polynomial action
\[
A=\mathbb C[x,y,z],\qquad
D=x^2\partial_y+2y\partial_z,\qquad
C=\mathbb C[x,H],\qquad H=x^2z-y^2
\tag{9}
\]
is primitive and has full plinth \(x^2C\).
At \(f=x\), the restricted action is \(2y\partial_z\),
its invariant ring is \(\mathbb C[y]\), and
\(K_x=\mathbb C(H)=\mathbb C(-y^2)\).
Thus \(E_x=\mathbb C(y)\) and \(e_x=2\).
A polynomial threefold can have such an action. The presence of
a nontrivial boundary extension cannot prove nonpolynomiality.

For the fixed pinched surface's proposed boundary realization, the
full invariant ring is
\(T=\mathbb C+(u^4-1)\mathbb C[u]\), whereas the prescribed nodal
base is
\[
A_0=\mathbb C[d,v]/(v^2-d^2(d+1)),\qquad
d=u^4-1,\quad v=d\,u^2.
\tag{10}
\]
Their fraction fields are \(\mathbb C(u)\) and \(\mathbb C(u^2)\).
The invariant boundary degree is therefore two, not one.
The new test is compatible with this candidate; it does not eliminate
the prescribed invariant-lifting defect.

The same degree data survive the old-plane principal modification
\(A[w]/((1+d_0)w-r)\) when \(d_0\in\sqrt{pC}\):
for every \(f\mid p\), reduction modulo \(f\) gives \(w=\overline r\)
and the identical boundary ring \(A/fA\).
The vertical modified action reduces to \(\overline D\).
Accordingly the boundary-field degree is unchanged.
This observation is about that specified action and included base,
not every possible action on the modified threefold.

## 5. The remaining intrinsic fence obstruction is in exceptional fibers

If the plinth divisor is a fence, choose adapted coordinates
\(C=\mathbb C[u,h]\) with \(p\in\mathbb C[u]\).
The local-slice chart is
\[
A_p=\mathbb C[u,p^{-1}][h,r].
\tag{11}
\]
Thus \(u:\operatorname{Spec}A\to\mathbb A^1\) has a trivial
affine-plane cylinder away from the finitely many roots of \(p\).

For every \(c\in\mathbb C\), \(u-c\) is a prime nonunit of \(A\)
by factorial closure. The map is surjective and flat over
\(\mathbb C[u]\); all fibers are integral surfaces.
Their factoriality is a separate condition.

If each exceptional fiber \(A/(u-c)A\), for \(p(c)=0\), is a UFD,
the known smooth-acyclic-threefold recognition theorem applies:
a morphism with general affine-plane fibers and factorial closed
fibers has total space \(\mathbb A^3\), with \(u\) a coordinate.
The other fibers are already polynomial by (11).
Masuda's Theorem 4.1 supplies a full proof and credits the earlier
Miyanishi and Kaliman characterization.[^3]

Here “affine-plane fibration” follows that paper's convention of
general fibers being affine planes; the exceptional fibers are
not assumed to be planes beforehand.
This is different from the everywhere-polynomial-fiber convention
sometimes used for an \(\mathbb A^2\)-fibration in commutative algebra.

A hypothetical nonpolynomial \(A\) under the cylinder hypothesis
must therefore, for every intrinsic primitive fence action, have
at least one nonfactorial exceptional \(u\)-fiber.
The cylinder alone has not been shown to rule this out.
An integral hypersurface of a polynomial ring need not be factorial,
so \(A[s]\) being polynomial does not supply the missing assertion.

The non-fence case still provides only invariant-multiple commuting
LNDs of a fixed primitive action. A different, noncommuting useful
action remains possible and is needed by that route.

## Sources

[^1]: S. Kaliman and N. Saveliev, [*C+-actions on contractible threefolds*](https://www.math.miami.edu/~kaliman/library/KaSa.michigan.2004.quotient.pdf), Lemma 2.1(1), Theorem 2.7 and Corollary 2.8, as reconstructed in the linked intrinsic quotient note. That previous proof is the source of the actual faithful-flatness input.
[^2]: D. Daigle and S. Kaliman, [*A Note on Locally Nilpotent Derivations and Variables of k[X,Y,Z]*](https://www.math.miami.edu/~kaliman/library/canada.daigle-kaliman.pdf), *Canadian Mathematical Bulletin* 52(4) (2009), 535-543, Theorem 1.5 and the gcd proof on p. 539. The argument was read directly.
[^3]: K. Masuda, [*Faithfully flat quotient morphisms by Ga-actions on factorial affine varieties*](https://arxiv.org/html/2512.06687v1), arXiv:2512.06687v1 (December 2025), Proposition 2.5 and its following remark, Lemma 3.1, Theorem 3.5, and Theorem 4.1 with proof. The precise sections were read directly. The author's [publication record](https://researchers.kwansei.ac.jp/view?k=k&l=en&sl=ja&sm=affiliation&sp=0&u=41237) identifies the published article in *Journal of Algebra* 691 (2026), 577-596, DOI 10.1016/j.jalgebra.2025.11.020.
