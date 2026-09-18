# Cancellation: intrinsic boundaries and a nonplanar special fiber

The general cancellation problem has not been solved. This pass closes
one all-degree surface-generation search, removes an unnecessary
hypothesis from the intrinsic action analysis, and disproves a stronger
version of the proposed highest-commutator shortcut.

The working target remains
\[
X\times_{\mathbb C}\mathbb A^1\simeq\mathbb A^4
\quad\Longrightarrow\quad X\simeq\mathbb A^3.
\tag{1}
\]
The professor has not confirmed either the dimension correction to his
email or the field. This is a private research checkpoint, not an
expert-reviewed paper or a claim of a new solution.

The main change is precise: for the fixed candidate surface, no
three-element generating set can contain its function \(h\), even if
both other functions are arbitrary and noninvariant. The proof uses
an actual special fiber, not a bounded generator search.

## 1. What the cylinder already gives for an intrinsic action

Write \(A[s]\simeq\mathbb C^{[4]}\) and let \(D\ne0\) be an
intrinsic locally nilpotent derivation of \(A\).
The previously reconstructed quotient argument gives an invariant
plane \(C=\ker D\simeq\mathbb C^{[2]}\) and a faithfully flat inclusion
\(C\hookrightarrow A\). The cylinder gives smoothness, contractibility
and factoriality of \(A\). The required domination hypothesis in the
Kaliman--Saveliev theorem was established using an actual linear slice
of the cylinder projection.[^1]

A locally nilpotent derivation is a polynomial differentiation rule
whose repeated application eventually kills each polynomial.
A slice is a polynomial \(r\) with \(D(r)=1\). It makes
\(A=(\ker D)[r]\), which would finish recognition here.
A nonzero or primitive action need not have a slice.

The new [intrinsic-boundary note](research/intrinsic-plinth-boundary-pass27.md)
proves that the full plinth is automatically principal:
\[
D(A)\cap C=pC,\qquad Dr=p\text{ for some }r\in A.
\tag{2}
\]
This is not a new structure theorem. It applies the published
faithful-flatness gcd mechanism to the unknown threefold itself.
Daigle and Kaliman give the complete gcd proof; Masuda records its
general factorial faithfully-flat form.[^2][^3]

For clarity, the key algebra is short. If \(Dr_i=f_i\in C\), then
\(r_1f_2-r_2f_1\) is invariant and lies in \((f_1,f_2)A\).
Faithful flatness contracts that ideal to \((f_1,f_2)C\).
Correcting the two \(r_i\) by invariants makes them proportional.
Factorial closure then permits division by the coprime parts of
\(f_1,f_2\), yielding a local slice with derivative
\(\gcd(f_1,f_2)\). Finite generation of the plinth finishes (2).

Thus principality is no longer an extra premise in the
[pass-26 intrinsic centralizer result](research/fence-centralizer-sector-pass26.md).
No conclusion about every higher image ideal \(D^n(A)\cap C\)
has been smuggled into this argument.

### An exact prime-support test, not a polynomiality obstruction

Assume \(D\) is primitive. For every prime element \(f\in C\),
the boundary \(A/fA\) is a domain and the induced derivation
\(\overline D\) is nonzero. Set
\[
K_f=\operatorname{Frac}(C/fC),\qquad
E_f=\operatorname{Frac}(\ker\overline D),\qquad
e_f=[E_f:K_f].
\tag{3}
\]
The degree is finite. Both fields have transcendence degree one,
and the algebraic closure of \(K_f\) in the finitely generated
boundary function field is finite.

The full plinth detects exactly where this extension is nontrivial:
\[
e_f>1\quad\Longleftrightarrow\quad f\mid p.
\tag{4}
\]
Off \(p=0\), the local-slice chart is a polynomial line over \(C_p\).
On a component \(f\mid p\), the residue of \(r\) is invariant.
If it belonged to \(K_f\), write \(br-a=ft\) with \(a,b\in C\)
and \(f\nmid b\). Then \(Dt=bp/f\) belongs to the full plinth
\(pC\), forcing \(f\mid b\), a contradiction. This reconstructs
the boundary obstruction behind the published criterion.[^3]

The test does not exclude our surface candidate. Its proposed
boundary invariant extension is \(\mathbb C(u)/\mathbb C(u^2)\),
of degree two. Even the ordinary polynomial action
\(x^2\partial_y+2y\partial_z\) has boundary degree two at \(x=0\).
A nontrivial boundary extension is not evidence that \(A\) is exotic.

### The remaining fence issue is factoriality of exceptional fibers

If \(p\in\mathbb C[u]\) in adapted invariant coordinates \(C=\mathbb C[u,h]\),
then \(A_p=\mathbb C[u,p^{-1}][h,r]\). A known recognition theorem
gives \(A\simeq\mathbb C^{[3]}\) if every exceptional surface fiber
\(A/(u-c)\), with \(p(c)=0\), is factorial.[^3]
The other fibers are already planes. Factoriality of \(A\) does not
make its hypersurface fibers factorial. This premise remains unproved.

## 2. The relative-plane complement problem is already settled when free

Let \(S\) be a Noetherian domain containing \(\mathbb Q\),
\(B=S[u,v]\) an actual relative plane, and
\(V=a\partial_u+b\partial_v\) an \(S\)-linear LND.
The comaximal case of Bhatwadekar--Dutta's theorem gives
\[
(a,b)B=B
\quad\Longleftrightarrow\quad
V\text{ has a slice}
\quad\Longleftrightarrow\quad
B=S[P,F],\ V=\partial_P.
\tag{5}
\]
Hence a commuting determinant-unit complement exists under these
hypotheses. Its existence is not a further open integrability problem.[^4]

The [relative-completion note](research/relative-completion-pass27.md)
also corrects any chosen determinant-one Bezout complement explicitly.
For \(W_0=c\partial_u+e\partial_v\), \(ae-bc=1\), put
\(q=\operatorname{div}W_0\). The LND has zero divergence, and
\[
[V,W_0]=qV.
\tag{6}
\]
Given the genuine slice \(P\), choose \(N\) with \(V^{N+1}q=0\) and set
\[
g=\sum_{j=0}^{N}
 \frac{(-1)^jP^{j+1}V^j(q)}{(j+1)!},
\qquad W=W_0-gV.
\tag{7}
\]
The sum telescopes to \(Vg=q\), so \(W\) commutes with \(V\)
and still has determinant one. Polynomial integration gives a dual
invariant coordinate, and one final shear makes \(V,W\) actual
coordinate partials. No inference from a unit Jacobian alone is used.

Babu and Das supply a broader published slice theorem when the relative
plane is replaced by an actual \(\mathbb A^2\)-fibration with a free
relative action.[^5] Here that means a finitely generated flat algebra
with a polynomial-plane fiber over every base prime. A generic plane
or two algebraically independent invariants do not meet that hypothesis.

This is not a new intrinsic cancellation regime. A free action on the
actual stably polynomial threefold already suffices by the earlier
Kaliman--Saveliev argument, without a rank bound.[^1] The contribution
here is to stop searching for a complement obstruction after the
relative-plane unit-ideal hypotheses have already been proved.

## 3. Even two sliced actions can have a nonsliced primitive top

The [highest-adjoint note](research/primitive-top-slice-pass27.md)
gives an explicit control on the actual polynomial four-ring:
\[
\delta=\partial_\lambda,\qquad
\Delta=\partial_a+\lambda a\partial_b+\lambda b\partial_c
\quad\text{on }\mathbb C[\lambda,a,b,c].
\tag{8}
\]
Both actions are triangular, primitive and sliced. Actual coordinates
for \(\Delta\) are \(\lambda,a,U,V\), where
\(U=b-\lambda a^2/2\) and
\(V=c-\lambda ab+\lambda^2a^3/3\); the note gives both polynomial
inverse directions.

Nevertheless the highest nonzero adjoint is
\[
L=[\delta,\Delta]=a\partial_b+b\partial_c,\qquad
[\delta,L]=0.
\tag{9}
\]
Its coefficients have gcd one, so it is already primitive.
They vanish together at \(a=b=0\), so no polynomial has \(L\)-derivative
one. More exactly,
\[
\ker L=\mathbb C[\lambda,a,2ac-b^2],\qquad
L(\ker L^2)=a\,\ker L.
\tag{10}
\]
The proof uses localization at \(a\) and separation of even and odd
powers of \(b\) to exclude denominators. It has no degree cutoff.

The original two actions have only constant common rational invariants.
Their Lie algebra is six-dimensional and nilpotent of class five;
every constant linear combination in it is an LND.
Thus even those strong hypotheses do not make the selected primitive
highest adjoint sliced. Every regular rational multiple of \(L\)
still vanishes on its fixed plane.

The successful escape is equally explicit:
\[
[\Delta,L]=\partial_b,\qquad
\partial_b(b)=1,\qquad [\delta,\partial_b]=0.
\tag{11}
\]
This different direction is sliced. The control does not rule out
all Lie-word strategies. Nor is \(\Delta\) claimed to be the canonical
vertical action of a nonunit-plinth modification: its own plinth is
a unit. That narrower possible hypothesis remains separate.

## 4. A complete all-degree obstruction for the actual surface

Keep the unchanged conductor-glued surface
\[
R=\mathbb C[d,e,g,h]\subset
B=\mathbb C[u,y,z]/((u-1)(u-i)z-y(y-1)),
\qquad d=u^4-1,\quad e=du.
\tag{12}
\]
Its functions, finite normalization and three conductor identifications
are the ones proved in passes 20 and 23. No new abstract module is
substituted for that ring.

The [complete special-fiber proof](research/noninvariant-surface-pass27.md)
establishes
\[
\operatorname{Spec}(R/(h))\not\hookrightarrow\mathbb A^2,
\qquad
R\ne\mathbb C[h,f_1,f_2]\quad\text{for all }f_1,f_2\in R.
\tag{13}
\]

Here is the obstruction in concrete terms. The actual \(h=0\) fiber
contains the images \(C_0\) of \(u=0\) and \(C_1\) of \(y=z=0\)
in the normalization. They meet only at \(u=y=z=0\), outside the
conductor. The local surface is the smooth plane with parameters
\(u,y\); the component ideals are \((u)\) and \((y)\).
Their intersection therefore has scheme-theoretic length one.

The normalization of \(C_1\) is the line \(\mathbb A^1_u\).
Its two points \(u=1\) and \(u=i\) are actually identified in \(R\).
Every regular function on \(C_1\) must take equal values at those points.

If the full fiber embedded in a plane, the height-one prime of its
component \(C_0\) in the plane would be principal. Restrict its generator
to the normalization of \(C_1\). The unique intersection and its length
force a polynomial with exactly one simple zero at \(u=0\):
\[
\ell(u)=cu,\quad c\ne0,
\qquad
\ell(1)=\ell(i)\ \Longrightarrow\ c=ci,
\tag{14}
\]
a contradiction. This works even if the entire fiber is nonreduced.
It does not need a theorem rectifying a line embedded in a plane.

Consequently every noninvariant as well as invariant \(j\) fails
\(R=\mathbb C[g,h,j]\). The rank-nine power-basis determinant from
pass 26 must fail already after specialization to \(h=0\).
This is a global obstruction on that fiber, not a claim that one
fixed closed finite fiber obstructs every candidate.

The note also gives an exact collision for a genuine noninvariant
basis element. That finite example checks the machinery; it is
not the proof of the universal statement (13).

A generating triple replacing \(h\) is still possible on the current
evidence. The abstract minimum number of generators remains between
three and four. Triviality of the dualizing module cannot close that
gap: the exact conductor gluing already has a nowhere-vanishing global
dualizing section, as [pass 20](research/nodal-conductor-pass20.md)
proved. That previously settled route was checked and parked.

## 5. Evidence and the next actual proof gap

The main investigator read every new proof and checker.
Separate AI investigators reconstructed the surface nonplanarity,
relative completion, highest-adjoint control and intrinsic boundary
argument. The source audit distinguished established theorems from
new deductions in this project. It is not human expert review,
a comprehensive novelty search or Lean verification.

The full regression and its exact timestamps are in
[verification-pass-27.json](verification-pass-27.json).
There are 605 passing test methods in 49 suites, including 25 new
methods in three standalone unittest/SymPy checkers. Repeated runs
and five orchestration controls are not extra methods.
Finite symbolic controls do not establish the universal assertions;
those are the written proofs above and their cited inputs.

Reproduce from the project directory:

~~~sh
/opt/anaconda3/bin/python research/run_regression_pass27.py
/opt/anaconda3/bin/python research/consistency_checks_pass27.py
~~~

The separate [audit record](research/proof-audits-pass27.md) records
proof reconstruction, source scope, tests and failed alternatives.
The integrity checker verifies links, claim numbering, flags and hashes,
not the truth of a theorem.

The remaining mathematically decisive work is to construct a useful
free intrinsic action, or a genuinely sufficient broader recognition
structure, for every \(A\) in (1). Within the surface branch, an
arbitrary triple must now replace \(h\), and an embedding alone would
still not construct the required ambient primitive action.
Within the commutator branch, a different useful direction must be
proved to exist; extracting only the primitive top is insufficient.
No one of these existence statements has been established.

## Sources

[^1]: S. Kaliman and N. Saveliev, [*C+-actions on contractible threefolds*](https://www.math.miami.edu/~kaliman/library/KaSa.michigan.2004.quotient.pdf), Theorem 2.7 and Corollary 2.8. The exact domination and free-action applications are reconstructed in [the intrinsic quotient note](research/intrinsic-quotient-surface-pass.md). The selected primary statements and proofs were read directly.
[^2]: D. Daigle and S. Kaliman, [*A Note on Locally Nilpotent Derivations and Variables of k[X,Y,Z]*](https://www.math.miami.edu/~kaliman/library/canada.daigle-kaliman.pdf), *Canadian Mathematical Bulletin* 52(4) (2009), 535-543, Theorem 1.5 and the complete gcd argument on printed p. 539.
[^3]: K. Masuda, [*Faithfully flat quotient morphisms by Ga-actions on factorial affine varieties*](https://arxiv.org/html/2512.06687v1), arXiv:2512.06687v1 (December 2025), Proposition 2.5 and remark, Lemma 3.1, Theorem 3.5 and Theorem 4.1. These selected statements and proofs were read. The [author's record](https://researchers.kwansei.ac.jp/view?k=k&l=en&sl=ja&sm=affiliation&sp=0&u=41237) lists the published article in *Journal of Algebra* 691 (2026), 577-596.
[^4]: S. M. Bhatwadekar and A. K. Dutta, [*Kernel of Locally Nilpotent R-Derivations of R[X,Y]*](https://repository.ias.ac.in/3203/1/311.pdf), *Transactions of the AMS* 349(8) (1997), 3303-3319, Theorem 4.7, including its proof and standing base-ring convention. Only the comaximal-coefficient case supplies the slice used here.
[^5]: J. R. Babu and P. Das, [*Structure of A2-fibrations having fixed point free locally nilpotent derivations*](https://arxiv.org/pdf/2001.07632), *Journal of Pure and Applied Algebra* 225(12) (2021), 106763, Theorem 4.4 and its proof. Its definition requires flatness and polynomial fibers over every base prime; it is not the general-fiber convention used in the recognition statement cited from Masuda.
